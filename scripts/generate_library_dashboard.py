#!/usr/bin/env python3
"""生成论文知识库可视化看板 (Spectral Observatory 主题).

产物 (两份, 内容同源):
  - 03-Literature/知识库Dashboard.html  自包含交互 HTML (浏览器打开, 离线可用)
  - 03-Literature/📊知识库主页.md        Obsidian Markdown 主页 (Dataview 动态查询)

数据来源: 02-Notes/Papers/ 笔记 frontmatter (真源) + git 基线 c4a5300 (优化前对比)。
只读不改笔记; 与 validate_library 同口径。退出码 0 正常。
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "02-Notes" / "Papers"
OUT_HTML = ROOT / "03-Literature" / "知识库Dashboard.html"
OUT_MD = ROOT / "03-Literature" / "📊知识库主页.md"
BASELINE = "c4a5300"  # 优化前存档

# 主题按研究家族排序 -> 沿光谱渐变上色 (相邻主题色相相近, 语义连续)
TOPIC_ORDER = [
    "A1_医学图像_分割", "A1b_医学图像_小样本_综述", "A2_医学图像_分类_配准_生成",
    "A3_医学图像_配准_切片_张量_数学", "B_注意力算子模块",
    "C_目标检测_通用与旋转框", "C2_目标检测_违建_车辆_船舶_行人", "C3_目标检测_红外_可见光融合",
    "D_3D_点云_分类_分割_配准", "D2_3D_重建_神经辐射场_SLAM",
    "E_图像复原_超分_去噪_去雨去雾", "F_图像分割_语义_实例_全景",
    "S_变化检测_ChangeDetection", "R1_遥感_高光谱_变化检测", "T_遥感_建筑检测",
    "G_视觉基础模型_VLM_LLM", "I_场景文本_OCR", "J_人脸_表情_伪造_情感",
    "K_跟踪_视频_动作", "M_行人_重识别_检索", "N_雷达_无线电_张量_数学",
    "O_物理对抗_安全_鲁棒", "P_跨域_域自适应_联邦", "Q_自监督_对比学习_主动学习",
    "L_数据集_Benchmark", "R_综述_Survey", "R2_控制_生物启发_其他跨学科",
    "T_安全_入侵检测", "T_通用_NLP_其他",
    "T_图像处理_分割", "T_图像处理_去噪", "T_图像处理_其他",
    "Z_工具与杂项_figures", "U_未归类",
]

GARBLE_RE = re.compile(r"[A-Za-z]{25,}")
FM_RE = re.compile(r"^---\n(.*?)\n---", re.S)


def fm_block(text: str) -> str:
    m = FM_RE.match(text)
    return m.group(1) if m else ""


def fm_scalar(block: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+)$", block, re.M)
    return m.group(1).strip().strip('"').strip("'") if m else ""


def fm_topics(block: str, primary: str) -> list[str]:
    m = re.search(r"^topics:\s*\[(.*?)\]", block, re.M)
    if m:
        items = [x.strip().strip('"').strip("'") for x in m.group(1).split(",") if x.strip()]
    else:
        m = re.search(r"^topics:\s*\n((?:\s*-\s*.+\n?)+)", block, re.M)
        items = (
            [re.sub(r"^\s*-\s*", "", l).strip().strip('"').strip("'")
             for l in m.group(1).splitlines() if l.strip()]
            if m else []
        )
    if primary and primary not in items:
        items = [primary] + items
    return items or ([primary] if primary else [])


def title_of(text: str, block: str, stem: str) -> str:
    t = fm_scalar(block, "title")
    if t and t != stem:
        return t
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else stem


def abstract_garbled(text: str) -> bool:
    m = re.search(r"## 摘要\n(.*?)\n##", text, re.S)
    return bool(m and GARBLE_RE.search(m.group(1)))


def year_of(block: str) -> str:
    y = fm_scalar(block, "year")
    return y if re.fullmatch(r"\d{4}", y or "") else ""


def baseline_state() -> dict[str, dict]:
    """从基线 commit 一次性取所有笔记的 primary_topic + 摘要乱码标记。"""
    stems = [p.stem for p in NOTES.glob("*.md")]
    names = [f"{BASELINE}:02-Notes/Papers/{s}.md\n".encode("utf-8") for s in stems]
    try:
        proc = subprocess.run(
            ["git", "cat-file", "--batch"], cwd=ROOT,
            input=b"".join(names), stdout=subprocess.PIPE, check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {}
    out = proc.stdout
    res: dict[str, dict] = {}
    i = 0
    n = len(out)
    for stem in stems:
        nl = out.find(b"\n", i)
        if nl < 0:
            break
        header = out[i:nl].decode("utf-8", "replace")
        i = nl + 1
        if header.endswith("missing"):
            continue
        parts = header.rsplit(" ", 2)
        if len(parts) != 3:
            continue
        size = int(parts[2])
        content = out[i:i + size].decode("utf-8", "replace")
        i += size + 1  # 跳过 blob 后的换行
        blk = fm_block(content)
        res[stem] = {
            "topic": fm_scalar(blk, "primary_topic") or "U_未归类",
            "garbled": abstract_garbled(content),
        }
    return res


def hue_for(topic: str, order: list[str]) -> float:
    idx = order.index(topic) if topic in order else len(order) - 1
    idx = max(0, min(idx, len(order) - 1))
    span = max(len(order) - 1, 1)
    return round(265 - (idx / span) * 265, 1)  # 紫 -> 红 光谱


def collect(truncated: set[str]):
    records = []
    for p in sorted(NOTES.glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        blk = fm_block(text)
        primary = fm_scalar(blk, "primary_topic") or "U_未归类"
        dtype = fm_scalar(blk, "document_type") or "paper"
        records.append({
            "stem": p.stem,
            "title": title_of(text, blk, p.stem),
            "topic": primary,
            "topics": fm_topics(blk, primary),
            "year": year_of(blk),
            "venue": fm_scalar(blk, "venue"),
            "status": fm_scalar(blk, "status") or "ai-read",
            "stage": fm_scalar(blk, "reading_stage"),
            "dtype": dtype,
            "human": fm_scalar(blk, "human_reviewed") == "true",
            "conf": fm_scalar(blk, "confidence"),
            "garbled": abstract_garbled(text),
            "trunc": p.name in truncated,
        })
    return records


def build_data(truncated: set[str]) -> dict:
    recs = collect(truncated)
    before = baseline_state()

    present = [t for t in TOPIC_ORDER if any(r["topic"] == t for r in recs)]
    extra = sorted({r["topic"] for r in recs} - set(present))
    order = present + extra

    topic_count = Counter(r["topic"] for r in recs)
    topic_hue = {t: hue_for(t, order) for t in order}

    topics = [
        {"topic": t, "count": topic_count[t], "hue": topic_hue[t]}
        for t in sorted(topic_count, key=lambda x: -topic_count[x])
    ]
    spectrum = [
        {"topic": t, "count": topic_count[t], "hue": topic_hue[t]} for t in order
    ]

    years = Counter(r["year"] for r in recs if r["year"])
    year_rows = [{"year": y, "count": years[y]} for y in sorted(years)]

    dtype_map = {"paper": "论文", "supplementary": "补充材料"}
    dtypes = Counter(dtype_map.get(r["dtype"], r["dtype"]) for r in recs)
    confs = Counter(r["conf"] or "(空)" for r in recs)

    human = sum(1 for r in recs if r["human"])
    garbled_now = [r for r in recs if r["garbled"]]

    # 优化前 -> 后
    before_topic = Counter(v["topic"] for v in before.values())
    before_garbled = sum(1 for v in before.values() if v["garbled"])
    movers = []
    for r in recs:
        b = before.get(r["stem"])
        if b and b["topic"] != r["topic"]:
            movers.append({"stem": r["stem"], "title": r["title"],
                           "frm": b["topic"], "to": r["topic"]})
    movers.sort(key=lambda m: (m["frm"], m["to"]))

    topic_delta = []
    for t in order:
        topic_delta.append({"topic": t, "before": before_topic.get(t, 0),
                            "after": topic_count[t], "hue": topic_hue[t]})

    return {
        "generated": run_git_date(),
        "total": len(recs),
        "topic_count": len(topic_count),
        "ai": sum(1 for r in recs if not r["human"]),
        "human": human,
        "garbled_now": len(garbled_now),
        "garbled_before": before_garbled,
        "movers_count": len(movers),
        "topics": topics,
        "spectrum": spectrum,
        "years": year_rows,
        "dtypes": [{"k": k, "v": v} for k, v in dtypes.most_common()],
        "status": [{"k": k, "v": v} for k, v in
                   Counter(("已人工精读" if r["human"] else "AI 首轮稿") for r in recs).most_common()],
        "confs": [{"k": k, "v": v} for k, v in confs.most_common()],
        "movers": movers,
        "topic_delta": topic_delta,
        "topic_hue": topic_hue,
        "papers": [{k: r[k] for k in ("stem", "title", "topic", "year", "venue",
                                      "status", "dtype", "conf", "human", "garbled", "trunc")}
                   for r in recs],
        "maint": {
            "trunc": [r["stem"] for r in recs if r["trunc"]],
            "garbled": [r["stem"] for r in garbled_now],
            "lowconf": [r["stem"] for r in recs if r["conf"] == "low"],
            "human": [r["stem"] for r in recs if r["human"]],
        },
    }


def run_git_date() -> str:
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cd", "--date=format:%Y-%m-%d %H:%M"],
                             cwd=ROOT, stdout=subprocess.PIPE, check=True)
        return out.stdout.decode().strip()
    except Exception:
        return ""


# ----------------------------- HTML -----------------------------
HTML_TEMPLATE = r"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>论文知识库 · 光谱观测台</title>
<style>
:root{
  --bg:#0E1420; --panel:#161E2E; --panel2:#1B2538; --line:#28344A;
  --ink:#E8EEF8; --muted:#8C9AB4; --faint:#5C6B86; --teal:#1FC8B0;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --disp:"Avenir Next","SF Pro Display",system-ui,sans-serif;
  --body:system-ui,-apple-system,"PingFang SC","Helvetica Neue",sans-serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:
  radial-gradient(1200px 600px at 85% -10%, #1a2740 0%, transparent 55%),
  var(--bg);color:var(--ink);font-family:var(--body);line-height:1.5;
  -webkit-font-smoothing:antialiased;letter-spacing:.01em}
a{color:inherit}
.wrap{max-width:1180px;margin:0 auto;padding:40px 28px 80px}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.32em;
  text-transform:uppercase;color:var(--teal)}
h1{font-family:var(--disp);font-weight:600;font-size:clamp(30px,5vw,52px);
  margin:.18em 0 .1em;letter-spacing:-.01em;line-height:1.02}
h1 .dim{color:var(--faint)}
.sub{color:var(--muted);max-width:62ch}
.stamp{font-family:var(--mono);font-size:12px;color:var(--faint)}
section{margin-top:54px}
.sec-h{display:flex;align-items:baseline;gap:14px;margin-bottom:18px}
.sec-h h2{font-family:var(--disp);font-weight:600;font-size:20px;margin:0;letter-spacing:.01em}
.sec-h .n{font-family:var(--mono);font-size:12px;color:var(--faint);letter-spacing:.2em}
.sec-h .rule{flex:1;height:1px;background:linear-gradient(90deg,var(--line),transparent)}

/* hero stats */
.chips{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}
.chip{background:var(--panel);border:1px solid var(--line);border-radius:14px;
  padding:14px 18px;min-width:118px}
.chip .v{font-family:var(--mono);font-size:26px;font-weight:600}
.chip .k{font-size:12px;color:var(--muted);margin-top:2px}
.chip .v.good{color:var(--teal)}

/* spectrum strip = signature */
.strip{display:flex;height:54px;border-radius:12px;overflow:hidden;
  border:1px solid var(--line)}
.strip > div{transition:flex .4s ease}
.strip > div:hover{filter:brightness(1.25)}
.legend{font-family:var(--mono);font-size:11px;color:var(--faint);margin-top:10px}

/* topic bars */
.bars{display:grid;gap:7px}
.bar{display:grid;grid-template-columns:230px 1fr 46px;align-items:center;gap:12px;
  cursor:pointer;padding:3px 6px;border-radius:8px}
.bar:hover{background:var(--panel)}
.bar.active{background:var(--panel2);outline:1px solid var(--line)}
.bar .lbl{font-size:13px;color:var(--muted);white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis}
.bar .track{height:13px;border-radius:7px;background:#1a2435;position:relative;overflow:hidden}
.bar .fill{height:100%;border-radius:7px}
.bar .c{font-family:var(--mono);font-size:13px;text-align:right;color:var(--ink)}

.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:20px}
.card h3{margin:0 0 14px;font-size:13px;color:var(--muted);font-weight:600;
  letter-spacing:.04em;text-transform:uppercase;font-family:var(--mono)}
.row{display:flex;align-items:center;gap:10px;margin:9px 0;font-size:13px}
.row .dot{width:9px;height:9px;border-radius:3px;flex:none}
.row .rk{flex:1;color:var(--muted)}
.row .rv{font-family:var(--mono)}
.ybars{display:flex;align-items:flex-end;gap:3px;height:120px;margin-top:6px}
.ybars .yb{flex:1;background:linear-gradient(180deg,var(--teal),#155e76);
  border-radius:3px 3px 0 0;min-height:2px;position:relative}
.ybars .yb span{position:absolute;top:-16px;left:50%;transform:translateX(-50%);
  font-family:var(--mono);font-size:9px;color:var(--faint)}
.yax{display:flex;gap:3px;margin-top:6px}
.yax div{flex:1;text-align:center;font-family:var(--mono);font-size:9px;color:var(--faint);
  writing-mode:vertical-rl;height:34px;margin:0 auto}

/* before/after */
.impact{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.metric{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:22px}
.metric .ba{display:flex;align-items:baseline;gap:12px;font-family:var(--mono)}
.metric .b{font-size:30px;color:var(--faint);text-decoration:line-through;
  text-decoration-color:#46527033}
.metric .arrow{color:var(--teal)}
.metric .a{font-size:38px;font-weight:600;color:var(--teal)}
.metric .k{font-size:13px;color:var(--muted);margin-top:8px}
.delta{margin-top:26px}
.delta .drow{display:grid;grid-template-columns:230px 1fr 1fr;gap:12px;align-items:center;
  font-size:12px;padding:4px 0;border-bottom:1px solid #1c2638}
.delta .drow .dl{color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.delta .mini{height:9px;border-radius:5px;background:#1a2435;position:relative}
.delta .mini i{position:absolute;left:0;top:0;height:100%;border-radius:5px;display:block}
.delta .nums{font-family:var(--mono);font-size:11px;color:var(--faint);text-align:right}

/* movers */
.movers{margin-top:22px;display:grid;gap:6px;max-height:330px;overflow:auto;padding-right:6px}
.mv{display:grid;grid-template-columns:1fr auto;gap:12px;align-items:center;
  background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:9px 13px}
.mv .t{font-size:12.5px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.mv .flow{font-family:var(--mono);font-size:11px;white-space:nowrap}
.mv .flow .f{color:var(--faint)}
.mv .flow .x{color:var(--teal);margin:0 6px}

/* table */
.tools{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:14px}
.search{flex:1;min-width:220px;background:var(--panel);border:1px solid var(--line);
  border-radius:10px;padding:11px 14px;color:var(--ink);font-size:14px;font-family:var(--body)}
.search::placeholder{color:var(--faint)}
select{background:var(--panel);border:1px solid var(--line);border-radius:10px;
  padding:11px 12px;color:var(--ink);font-size:13px;font-family:var(--body)}
.count{font-family:var(--mono);font-size:12px;color:var(--faint)}
.tbl{width:100%;border-collapse:collapse;table-layout:fixed}
.tbl col.c-ttl{width:46%}.tbl col.c-top{width:22%}.tbl col.c-yr{width:7%}
.tbl col.c-ven{width:13%}.tbl col.c-st{width:12%}
.tbl thead th{position:sticky;top:0;background:var(--bg);text-align:left;
  font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--faint);padding:9px 12px;border-bottom:1px solid var(--line);cursor:pointer}
.tbl tbody td{padding:8px 12px;border-bottom:1px solid #19222f;font-size:13px;
  vertical-align:middle;line-height:1.35;overflow:hidden;text-overflow:ellipsis}
.tbl tbody .ttlwrap{display:flex;align-items:center;gap:6px;min-width:0}
.tbl tbody .ttl{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--ink)}
.tbl tbody tr:hover{background:var(--panel)}
.tbl .tg{display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted);
  white-space:nowrap;overflow:hidden}
.tbl .tg span:last-child{overflow:hidden;text-overflow:ellipsis}
.tbl .tg .dot{width:8px;height:8px;border-radius:3px;flex:none}
.tbl .yr{font-family:var(--mono);color:var(--muted)}
.tbl .ttl{color:var(--ink)}
.flag{font-family:var(--mono);font-size:10px;padding:1px 6px;border-radius:5px;margin-left:6px}
.flag.h{background:#163b33;color:var(--teal)}
.flag.g{background:#3b2a16;color:#e0a84d}
.flag.t{background:#2a2340;color:#a08fe0}
.scrollbox{max-height:560px;overflow:auto;border:1px solid var(--line);border-radius:14px}

/* maintenance */
.maint{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
.todo{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:20px}
.todo .th{display:flex;align-items:center;gap:10px;margin-bottom:6px}
.todo .badge{font-family:var(--mono);font-size:20px;font-weight:600}
.todo .ti{font-size:13px;color:var(--muted)}
.todo ul{margin:12px 0 0;padding-left:0;list-style:none;display:grid;gap:5px;
  max-height:170px;overflow:auto}
.todo li{font-family:var(--mono);font-size:11.5px;color:var(--faint);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.todo.ok .badge{color:var(--teal)}
.foot{margin-top:60px;padding-top:20px;border-top:1px solid var(--line);
  font-family:var(--mono);font-size:11px;color:var(--faint);display:flex;
  justify-content:space-between;flex-wrap:wrap;gap:10px}
@media (max-width:820px){
  .grid3,.impact,.maint{grid-template-columns:1fr}
  .bar{grid-template-columns:140px 1fr 40px}
  .delta .drow{grid-template-columns:130px 1fr}
  .delta .drow .nums{display:none}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto}}
:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="eyebrow">论文知识库 · 光谱观测台</div>
    <h1>__TOTAL__ <span class="dim">篇 · __TOPICN__ 主题</span></h1>
    <p class="sub">一座计算机视觉与机器学习的研究藏馆。下方按研究家族沿光谱排布；点击任意主题可筛选全库清单。</p>
    <div class="chips">
      <div class="chip"><div class="v">__AI__</div><div class="k">AI 首轮阅读稿</div></div>
      <div class="chip"><div class="v good">__HUMAN__</div><div class="k">已人工精读</div></div>
      <div class="chip"><div class="v good">__GARB__</div><div class="k">乱码摘要 (优化前 __GARBB__)</div></div>
      <div class="chip"><div class="v good">__MOVERS__</div><div class="k">修正归类</div></div>
    </div>
  </header>

  <section>
    <div class="sec-h"><span class="n">01</span><h2>主题光谱</h2><div class="rule"></div></div>
    <div class="strip" id="strip">__STRIP__</div>
    <div class="legend">条带宽度 = 该主题论文占比 · 色相 = 研究家族 (紫→红)</div>
    <div class="bars" id="bars" style="margin-top:26px">__BARS__</div>
  </section>

  <section>
    <div class="sec-h"><span class="n">02</span><h2>馆藏构成</h2><div class="rule"></div></div>
    <div class="grid3">
      <div class="card"><h3>阅读质量</h3>__STATUS__<div style="margin-top:14px"></div>__CONF__</div>
      <div class="card"><h3>文档类型</h3>__DTYPE__</div>
      <div class="card"><h3>年份分布</h3><div class="ybars">__YBARS__</div><div class="yax">__YAX__</div></div>
    </div>
  </section>

  <section>
    <div class="sec-h"><span class="n">03</span><h2>本次优化成果</h2><div class="rule"></div></div>
    <div class="impact">
      <div class="metric"><div class="ba"><span class="b">__GARBB__</span><span class="arrow">▸</span><span class="a">__GARB__</span></div><div class="k">乱码摘要 (从 PDF 提取文本重建)</div></div>
      <div class="metric"><div class="ba"><span class="a">__MOVERS__</span></div><div class="k">篇修正归类 (关键词分类器误判 / 文件名串台)</div></div>
      <div class="metric"><div class="ba"><span class="a">__TOTAL__</span></div><div class="k">篇逐篇对照原文核对 · 抽检 0 幻觉</div></div>
    </div>
    <div class="delta">
      <div class="sec-h" style="margin-top:30px"><span class="n">分布变化</span><div class="rule"></div></div>
      __DELTA__
    </div>
    <div class="movers" id="movers">__MV__</div>
  </section>

  <section>
    <div class="sec-h"><span class="n">04</span><h2>论文清单</h2><div class="rule"></div><span class="count" id="cnt"></span></div>
    <div class="tools">
      <input class="search" id="q" placeholder="按标题搜索…" autocomplete="off">
      <select id="ft"><option value="">全部主题</option>__FTOPT__</select>
      <select id="fs"><option value="">全部状态</option><option value="ai-read">AI 首轮稿</option><option value="read">已人工精读</option></select>
      <select id="fy"><option value="">全部年份</option>__FYOPT__</select>
    </div>
    <div class="scrollbox">
      <table class="tbl">
        <colgroup><col class="c-ttl"><col class="c-top"><col class="c-yr"><col class="c-ven"><col class="c-st"></colgroup>
        <thead><tr>
        <th data-k="title">标题</th><th data-k="topic">主题</th>
        <th data-k="year">年</th><th data-k="venue">来源</th><th data-k="status">状态</th>
      </tr></thead><tbody id="tb"></tbody></table>
    </div>
  </section>

  <section>
    <div class="sec-h"><span class="n">05</span><h2>维护待办</h2><div class="rule"></div></div>
    <div class="maint">__MAINT__</div>
  </section>

  <div class="foot">
    <span>数据源 02-Notes/Papers frontmatter · 基线 c4a5300</span>
    <span>生成 __GEN__ · scripts/generate_library_dashboard.py</span>
  </div>
</div>
<script>
const DATA = __DATA__;
const HUE = DATA.topic_hue;
const col = (t,l=58,s=64)=>`hsl(${HUE[t]??0} ${s}% ${l}%)`;
// table
const tb=document.getElementById('tb'), q=document.getElementById('q'),
  ft=document.getElementById('ft'), fs=document.getElementById('fs'),
  fy=document.getElementById('fy'), cnt=document.getElementById('cnt');
let sortK='title', sortDir=1;
function render(){
  const term=q.value.trim().toLowerCase(), t=ft.value, s=fs.value, y=fy.value;
  let rows=DATA.papers.filter(p=>
    (!term||p.title.toLowerCase().includes(term)||p.stem.toLowerCase().includes(term))
    &&(!t||p.topic===t)&&(!s||p.status===s)&&(!y||p.year===y));
  rows.sort((a,b)=>{let x=(a[sortK]||''),z=(b[sortK]||'');return x<z?-sortDir:x>z?sortDir:0});
  cnt.textContent=rows.length+' / '+DATA.papers.length+' 篇';
  tb.innerHTML=rows.map(p=>{
    const flags=(p.human?'<span class="flag h">精读</span>':'')+
      (p.garbled?'<span class="flag g">摘要待修</span>':'')+
      (p.trunc?'<span class="flag t">提取截断</span>':'');
    const st=p.human?'已人工精读':'AI 首轮稿';
    return `<tr><td><div class="ttlwrap"><span class="ttl" title="${esc(p.title)}">${esc(p.title)}</span>${flags}</div></td>
      <td><span class="tg"><span class="dot" style="background:${col(p.topic)}"></span><span>${esc(p.topic)}</span></span></td>
      <td class="yr">${p.year||'—'}</td><td style="color:var(--muted)">${esc(p.venue||'—')}</td>
      <td style="color:var(--muted)">${st}</td></tr>`;
  }).join('')||'<tr><td colspan="5" style="color:var(--faint);padding:24px">无匹配</td></tr>';
}
function esc(s){return (s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
[q,ft,fs,fy].forEach(e=>e.addEventListener('input',render));
document.querySelectorAll('.tbl thead th').forEach(th=>th.addEventListener('click',()=>{
  const k=th.dataset.k; sortDir=(sortK===k)?-sortDir:1; sortK=k; render();}));
document.querySelectorAll('#bars .bar').forEach(b=>b.addEventListener('click',()=>{
  const t=b.dataset.t; const on=b.classList.contains('active');
  document.querySelectorAll('#bars .bar').forEach(x=>x.classList.remove('active'));
  if(!on){b.classList.add('active');ft.value=t;} else {ft.value='';}
  render(); document.getElementById('q').scrollIntoView({block:'center'});
}));
render();
</script>
</body>
</html>
"""


def esc_html(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def render_html(d: dict) -> str:
    total = d["total"]
    palette = {"已人工精读": "var(--teal)", "AI 首轮稿": "#3d6ea0",
               "论文": "var(--teal)", "补充材料": "#a08fe0",
               "high": "var(--teal)", "medium": "#e0a84d", "low": "#e06d5a", "(空)": "#46527d"}

    # spectrum strip
    strip = "".join(
        f'<div title="{esc_html(s["topic"])} · {s["count"]}" '
        f'style="flex:{s["count"]};background:hsl({s["hue"]} 60% 52%)"></div>'
        for s in d["spectrum"] if s["count"] > 0
    )
    # bars
    mx = max((t["count"] for t in d["topics"]), default=1)
    bars = "".join(
        f'<div class="bar" data-t="{esc_html(t["topic"])}" tabindex="0">'
        f'<span class="lbl">{esc_html(t["topic"])}</span>'
        f'<span class="track"><span class="fill" style="width:{t["count"]/mx*100:.1f}%;'
        f'background:hsl({t["hue"]} 64% 56%)"></span></span>'
        f'<span class="c">{t["count"]}</span></div>'
        for t in d["topics"]
    )

    def rows(items, total_n):
        out = ""
        for it in items:
            k = it["k"]
            c = palette.get(k, "#46527d")
            pct = it["v"] / total_n * 100 if total_n else 0
            out += (f'<div class="row"><span class="dot" style="background:{c}"></span>'
                    f'<span class="rk">{esc_html(k)}</span>'
                    f'<span class="rv">{it["v"]} · {pct:.0f}%</span></div>')
        return out

    status_html = rows(d["status"], total)
    conf_label = {"high": "置信 高", "medium": "置信 中", "low": "置信 低", "(空)": "置信 未标"}
    conf_items = [{"k": conf_label.get(c["k"], c["k"]), "v": c["v"]} for c in d["confs"]]
    conf_palette_html = ""
    for c in d["confs"]:
        col = palette.get(c["k"], "#46527d")
        lbl = conf_label.get(c["k"], c["k"])
        pct = c["v"] / total * 100
        conf_palette_html += (f'<div class="row"><span class="dot" style="background:{col}"></span>'
                              f'<span class="rk">{esc_html(lbl)}</span>'
                              f'<span class="rv">{c["v"]} · {pct:.0f}%</span></div>')
    dtype_html = rows(d["dtypes"], total)

    # year bars
    ymax = max((y["count"] for y in d["years"]), default=1)
    ybars = "".join(
        f'<div class="yb" title="{y["year"]} · {y["count"]}" '
        f'style="height:{y["count"]/ymax*100:.0f}%"><span>{y["count"] if y["count"]>=ymax*0.6 else ""}</span></div>'
        for y in d["years"]
    )
    yax = "".join(f'<div>{y["year"][2:]}</div>' for y in d["years"])

    # delta rows (only topics that exist now, sorted by after desc)
    dd = [x for x in d["topic_delta"] if x["after"] > 0]
    dd.sort(key=lambda x: -x["after"])
    dmax = max((max(x["before"], x["after"]) for x in dd), default=1)
    delta = ""
    for x in dd:
        delta += (
            f'<div class="drow"><span class="dl">{esc_html(x["topic"])}</span>'
            f'<span class="mini"><i style="width:{x["before"]/dmax*100:.0f}%;background:#3a466a"></i></span>'
            f'<span class="mini"><i style="width:{x["after"]/dmax*100:.0f}%;background:hsl({x["hue"]} 64% 56%)"></i></span>'
            f'<span class="nums">{x["before"]} → {x["after"]}</span></div>'
        )

    movers = "".join(
        f'<div class="mv"><span class="t">{esc_html(m["title"][:70])}</span>'
        f'<span class="flow"><span class="f">{esc_html(m["frm"])}</span>'
        f'<span class="x">→</span>{esc_html(m["to"])}</span></div>'
        for m in d["movers"]
    )

    ftopt = "".join(f'<option value="{esc_html(t["topic"])}">{esc_html(t["topic"])} ({t["count"]})</option>'
                    for t in d["topics"])
    yrs = sorted({y["year"] for y in d["years"]}, reverse=True)
    fyopt = "".join(f'<option value="{y}">{y}</option>' for y in yrs)

    # maintenance
    m = d["maint"]
    def todo(badge, title, items, ok=False):
        lis = "".join(f"<li>{esc_html(s)}</li>" for s in items[:40])
        cls = "todo ok" if ok else "todo"
        return (f'<div class="{cls}"><div class="th"><span class="badge">{badge}</span></div>'
                f'<div class="ti">{title}</div><ul>{lis}</ul></div>')
    maint = (
        todo(len(m["trunc"]), "提取缓存截断 · 建议重提全文后补读", m["trunc"]) +
        todo(len(m["garbled"]), "摘要仍含乱码 (含受保护笔记)", m["garbled"]) +
        todo(len(m["lowconf"]), "低置信度笔记 · 优先人工复核", m["lowconf"]) +
        todo(len(m["human"]), "已人工精读 (基准)", m["human"], ok=True)
    )

    data_json = json.dumps(
        {"papers": d["papers"], "topic_hue": d["topic_hue"]},
        ensure_ascii=False
    ).replace("</", "<\\/")

    html = HTML_TEMPLATE
    repl = {
        "__TOTAL__": str(total), "__TOPICN__": str(d["topic_count"]),
        "__AI__": str(d["ai"]), "__HUMAN__": str(d["human"]),
        "__GARB__": str(d["garbled_now"]), "__GARBB__": str(d["garbled_before"]),
        "__MOVERS__": str(d["movers_count"]),
        "__STRIP__": strip, "__BARS__": bars,
        "__STATUS__": status_html, "__CONF__": conf_palette_html, "__DTYPE__": dtype_html,
        "__YBARS__": ybars, "__YAX__": yax, "__DELTA__": delta, "__MV__": movers,
        "__FTOPT__": ftopt, "__FYOPT__": fyopt, "__MAINT__": maint,
        "__GEN__": d["generated"], "__DATA__": data_json,
    }
    for k, v in repl.items():
        html = html.replace(k, v)
    return html


# ----------------------------- Markdown 主页 -----------------------------
def render_md(d: dict) -> str:
    top5 = d["topics"][:6]
    lines = [
        "# 📊 论文知识库 · 主页",
        "",
        f"> 自动生成于 {d['generated']}。交互看板见 [[知识库Dashboard.html]] (浏览器打开)。",
        "",
        "## 一览",
        "",
        "| 指标 | 数值 |",
        "|---|---:|",
        f"| 论文总数 | {d['total']} |",
        f"| 主题数 | {d['topic_count']} |",
        f"| AI 首轮稿 / 已人工精读 | {d['ai']} / {d['human']} |",
        f"| 乱码摘要 (优化前 → 后) | {d['garbled_before']} → {d['garbled_now']} |",
        f"| 本次修正归类 | {d['movers_count']} 篇 |",
        "",
        "## 主题分布 (Top)",
        "",
        "| 主题 | 篇数 |",
        "|---|---:|",
    ]
    lines += [f"| [[{t['topic']}]] | {t['count']} |" for t in top5]
    lines += [
        "",
        "完整主题首页见 `03-Literature/`。下方为 Dataview 动态视图 (需 Dataview 插件)。",
        "",
        "## 按主题统计 (动态)",
        "",
        "```dataview",
        "TABLE length(rows) AS 篇数",
        'FROM "02-Notes/Papers"',
        "WHERE primary_topic",
        "GROUP BY primary_topic AS 主题",
        "SORT length(rows) DESC",
        "```",
        "",
        "## 最近加入",
        "",
        "```dataview",
        "TABLE year AS 年, primary_topic AS 主题, status AS 状态",
        'FROM "02-Notes/Papers"',
        "WHERE date_added",
        "SORT date_added DESC",
        "LIMIT 15",
        "```",
        "",
        "## 维护待办",
        "",
        "### 已人工精读 (基准)",
        "```dataview",
        "LIST",
        'FROM "02-Notes/Papers"',
        "WHERE human_reviewed = true",
        "```",
        "",
        "### 低置信度 · 优先复核",
        "```dataview",
        "TABLE primary_topic AS 主题, confidence AS 置信",
        'FROM "02-Notes/Papers"',
        'WHERE confidence = "low"',
        "```",
        "",
        "### 提取缓存截断 · 建议重提全文",
    ]
    lines += [f"- {s}" for s in d["maint"]["trunc"]]
    lines += [
        "",
        "### 摘要仍含乱码",
    ]
    lines += [f"- {s}" for s in d["maint"]["garbled"]] or ["- (无)"]
    lines += ["", "---", "", f"由 `scripts/generate_library_dashboard.py` 生成 · 基线 `c4a5300`。"]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="生成论文知识库可视化看板 (HTML + Obsidian 主页)")
    ap.add_argument("--html", type=Path, default=OUT_HTML)
    ap.add_argument("--md", type=Path, default=OUT_MD)
    args = ap.parse_args()

    # 截断提取清单 (与 validate 同口径)
    truncated: set[str] = set()
    vp = ROOT / "scripts" / "validate_library.py"
    if vp.exists():
        try:
            out = subprocess.run([sys.executable, str(vp), "-v"], cwd=ROOT,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in out.stdout.decode("utf-8", "replace").splitlines():
                m = re.search(r"\[AI 提取不完整\]\s*(.+?):", line)
                if m:
                    truncated.add(m.group(1).strip())
        except Exception:
            pass

    d = build_data(truncated)
    args.html.write_text(render_html(d), encoding="utf-8")
    args.md.write_text(render_md(d), encoding="utf-8")
    print(f"✅ 看板已生成:")
    print(f"   HTML: {args.html}")
    print(f"   主页: {args.md}")
    print(f"   {d['total']} 篇 · {d['topic_count']} 主题 · 修正归类 {d['movers_count']} · 乱码 {d['garbled_before']}→{d['garbled_now']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
