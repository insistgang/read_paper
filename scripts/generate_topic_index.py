#!/usr/bin/env python3
"""为每个主题在 05-Literature/ 下生成主题首页 (index note)。

每个首页包含:
  - 主题定义 (从 primary_topic 名字推断, 留 TODO 让人工润色)
  - 论文列表 (按 primary_topic 归桶, 含多标签提示)
  - 建议阅读顺序 (按文件名推断的年份排序)
  - 关键问题 / 方法分类 / 待精读清单 (TODO 留空)

约定:
  - 不会覆盖已存在的主题首页 (默认行为; --force 可覆盖)
  - 文件名: 05-Literature/<主题代码>.md
  - 不会创建主题代码里没有 PDF 的空首页
"""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PAPERS = ROOT / "01-Papers"
DEFAULT_TOPICS_JSON = DEFAULT_PAPERS / "paper_topics.json"
DEFAULT_LIT = ROOT / "05-Literature"
DEFAULT_CLASSIFY_PY = ROOT / "scripts" / "classify_papers.py"

# 主题代号 -> 主题中文名 + 一句话定义 (粗略, 供首页用)
# 来自 paper_classification.md 已有的主题; 没在表里的主题会用代码本身做名字
TOPIC_NAMES = {
    "A1_医学图像_分割": "医学图像分割",
    "A1b_医学图像_小样本_综述": "医学图像小样本/综述",
    "A2_医学图像_分类_配准_生成": "医学图像分类/配准/生成",
    "A3_医学图像_配准_切片_张量_数学": "医学图像配准/张量数学",
    "B_注意力算子模块": "注意力算子/模块",
    "C_目标检测_通用与旋转框": "通用/旋转框目标检测",
    "C2_目标检测_违建_车辆_船舶_行人": "违建/车辆/船舶/行人检测",
    "C3_目标检测_红外_可见光融合": "红外+可见光融合检测",
    "C4_目标检测_交通_标志_检测器": "交通标志检测",
    "D_3D_点云_分类_分割_配准": "3D 点云分类/分割/配准",
    "D2_3D_重建_神经辐射场_SLAM": "3D 重建/NeRF/SLAM",
    "E_图像复原_超分_去噪_去雨去雾": "图像复原/超分/去噪去雨去雾",
    "F_图像分割_语义_实例_全景": "通用语义/实例/全景分割",
    "G_视觉基础模型_VLM_LLM": "视觉基础模型/VLM/LLM",
    "H_显著性_小目标": "显著性/小目标",
    "I_场景文本_OCR": "场景文本/OCR",
    "J_人脸_表情_伪造_情感": "人脸/表情/伪造/情感",
    "K_跟踪_视频_动作": "跟踪/视频/动作",
    "L_数据集_Benchmark": "数据集/Benchmark",
    "M_行人_重识别_检索": "行人/重识别/检索",
    "N_雷达_无线电_张量_数学": "雷达/无线电/张量/数学",
    "O_物理对抗_安全_鲁棒": "物理对抗/安全/鲁棒",
    "P_跨域_域自适应_联邦": "跨域/域自适应/联邦",
    "Q_自监督_对比学习_主动学习": "自监督/对比学习/主动学习",
    "R_综述_Survey": "综述/Survey",
    "R1_遥感_高光谱_变化检测": "遥感/高光谱/变化检测",
    "R2_控制_生物启发_其他跨学科": "控制/生物启发/其他",
    "S_变化检测_ChangeDetection": "变化检测",
    "T_通用_NLP_其他": "通用/NLP/其他",
    "Z_工具与杂项_figures": "工具/figures/杂项",
}


def extract_year(stem: str) -> Optional[int]:
    m = re.match(r"^(\d{4})", stem)
    return int(m.group(1)) if m else None


def build_index(topic_code: str, papers: list[dict]) -> str:
    """papers: [{name, year, topics}]"""
    name_zh = TOPIC_NAMES.get(topic_code, topic_code.replace("_", " "))
    n = len(papers)
    paper_lines = []
    sorted_papers = sorted(papers, key=lambda p: (p["year"] or 9999, p["name"]))
    for p in sorted_papers:
        year_str = str(p["year"]) if p["year"] else "????"
        other = [t for t in p["topics"] if t != topic_code]
        tag = f"  _{'/'.join(other)}_" if other else ""
        paper_lines.append(f"- {year_str} [[{p['stem']}]]{tag}")
    paper_block = "\n".join(paper_lines) if paper_lines else "_(暂无)_"

    # 简单年份分布
    by_year: dict[int, int] = {}
    for p in papers:
        y = p["year"] or 0
        by_year[y] = by_year.get(y, 0) + 1
    year_dist = ", ".join(
        f"{y}: {c}" for y, c in sorted(by_year.items(), key=lambda kv: -kv[1])[:6]
        if y
    ) or "_(暂未提取到年份)_"

    body = f"""# {name_zh} (`{topic_code}`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: {name_zh}
- **代号**: `{topic_code}`
- **论文数**: {n}
- **年份分布**: {year_dist}

## 论文列表 (按年份排序)

{paper_block}

## 建议阅读顺序 (TODO: 人工)

> 入门 -> 核心 -> 进阶 -> 综述
>
> 命名规则: filename 通常含 `YYYY_关键词`, 可按年份递进。
> 调研时建议先看 Survey / 综述 (主题里带 `_综述` 或 `Survey`), 再读近 2 年的方法。

### 入门
- TODO: 从列表里选 2-3 篇 survey/intro
### 核心
- TODO: 选近 2 年的 SOTA 方法 3-5 篇
### 进阶
- TODO: 选 1-2 篇 method 复杂 / 有数学推导
### 综述
- TODO: 找主题里 _综述 标签的论文

## 关键问题 (TODO: 人工)

> 读了几篇后, 把这个主题下反复出现的核心科学问题列出来。

1.
2.
3.

## 方法分类 (TODO: 人工)

> 按方法族 (CNN / Transformer / Mamba / Diffusion / 等) 或任务范式分类。

- **CNN-based**:
- **Transformer-based**:
- **Mamba/SSM**:
- **其他**:

## 待精读清单

> 还没读但计划要读的论文 (按优先级)。

- [ ] (优先级高) TODO
- [ ] (优先级中) TODO
- [ ] (优先级低) TODO

## Dataview 查询示例

```dataview
TABLE year, primary_topic, status
FROM "{topic_code}" OR "topic/{topic_code}"
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
"""
    return body


def main():
    parser = argparse.ArgumentParser(
        description="为每个主题在 05-Literature/ 下生成主题首页",
    )
    parser.add_argument(
        "--papers", type=Path, default=DEFAULT_PAPERS,
        help="PDF 所在目录 (默认: 01-Papers/)",
    )
    parser.add_argument(
        "--topics-json", type=Path, default=DEFAULT_TOPICS_JSON,
        help="paper_topics.json 路径 (默认: 01-Papers/paper_topics.json)",
    )
    parser.add_argument(
        "--lit", type=Path, default=DEFAULT_LIT,
        help="主题首页输出目录 (默认: 05-Literature/)",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="覆盖已存在的主题首页",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="只统计, 不写文件",
    )
    args = parser.parse_args()

    if not args.papers.is_dir():
        sys.exit(f"错误: 目录不存在: {args.papers}")
    if not args.topics_json.is_file():
        sys.exit(
            f"错误: {args.topics_json} 不存在, 先跑 scripts/classify_papers.py。"
        )

    paper_topics = json.loads(args.topics_json.read_text(encoding="utf-8"))

    # 按 primary_topic 归桶
    by_topic: dict[str, list[dict]] = {}
    for stem, topics in paper_topics.items():
        primary = topics[0] if topics else "U_未归类"
        by_topic.setdefault(primary, []).append({
            "stem": stem,
            "name": f"{stem}.pdf",
            "year": extract_year(stem),
            "topics": topics,
        })

    if not args.dry_run:
        args.lit.mkdir(parents=True, exist_ok=True)

    created, skipped, forced = 0, 0, 0
    for topic, papers in sorted(by_topic.items()):
        # 不为 U_未归类 建首页
        if topic == "U_未归类":
            continue
        out = args.lit / f"{topic}.md"
        if out.exists() and not args.force:
            skipped += 1
            continue
        if out.exists() and args.force:
            forced += 1
        content = build_index(topic, papers)
        if not args.dry_run:
            out.write_text(content, encoding="utf-8")
        created += 1

    print(f"主题数: {len(by_topic)}")
    print(f"主题首页生成: {created} (其中覆盖: {forced})")
    print(f"跳过已存在:  {skipped}")
    if args.dry_run:
        print("(dry-run: 未实际写文件)")


if __name__ == "__main__":
    main()
