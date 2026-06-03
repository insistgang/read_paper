#!/usr/bin/env python3
"""为 01-Papers/ 下的每个 PDF 生成同名 .md 骨架笔记。

骨架只基于文件名 + 主题分类, 不读 PDF 内容。读 PDF 后用 scripts/paper_ai.py
升级正文, 但 frontmatter 不动 (primary_topic/topics 由本脚本写入, 是机器
推断的初版, 人工读 PDF 后可改 confidence/source_basis)。

frontmatter (与 Obsidian 兼容):
---
title:
pdf: "[[xxx.pdf]]"
primary_topic:
topics: []
status: unread
reading_stage: filename-only
confidence: low
source_basis: filename
date_added:
tags: [paper]
---

约定:
  - 默认: 不会覆盖已存在的 .md, 跳过
  - --force: 只覆盖 status=unread + source_basis=filename 的骨架笔记,
    已读笔记(status=read 或 source_basis=pdf-text)自动保护
  - --really-force: 无条件覆盖所有 .md, 包括已读笔记 (日常增量用 --force 即可)
  - 不读 PDF 内容, 不编造作者/会议/实验
  - 标题用 PDF stem (去除扩展名 + 清理下划线/短横线/年份前缀)
  - keywords 从文件名提取 1-3 个有意义的 token
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

# 仓库根
ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PAPERS = ROOT / "01-Papers"
DEFAULT_TOPICS_JSON = DEFAULT_PAPERS / "paper_topics.json"
DEFAULT_LIT = ROOT / "05-Literature"

# 中文停用词（不作为关键词保留）
STOP_WORDS_ZH = {
    "的", "是", "在", "和", "与", "及", "或", "基于", "用于", "通过", "一种",
    "方法", "研究", "分析", "一种", "本文", "研究进展", "综述",
}
STOP_WORDS_EN = {
    "a", "an", "the", "of", "for", "on", "in", "and", "or", "to", "with",
    "based", "via", "towards", "from", "by", "using", "study", "review",
    "survey", "paper", "approach", "method", "analysis",
}


def clean_title(stem: str) -> str:
    """从 PDF stem 推断可读标题。"""
    t = stem
    # 去掉开头的年份
    t = re.sub(r"^\d{4}_+", "", t)
    # 替换分隔符为空格
    t = re.sub(r"[_\-]+", " ", t)
    # 移除多余空格
    t = re.sub(r"\s+", " ", t).strip()
    return t or stem


def extract_keywords(stem: str, primary_topic: str, max_kw: int = 3) -> list[str]:
    """从文件名提取 1-3 个有意义的关键词 token。"""
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9-]{2,}|[\u4e00-\u9fff]{2,}", stem)
    kws = []
    seen = set()
    for tok in tokens:
        low = tok.lower()
        if low in STOP_WORDS_EN or tok in STOP_WORDS_ZH:
            continue
        if low in seen:
            continue
        # 太通用的英文 token 跳过 (单字母/超长缩写)
        if len(tok) < 3 and tok.isascii():
            continue
        seen.add(low)
        kws.append(tok)
    return kws[:max_kw]


def yaml_escape(s: str) -> str:
    """粗略 YAML 字符串转义 (双引号 + 转义双引号/反斜杠)。"""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def parse_frontmatter(md_text: str) -> dict[str, str]:
    """粗略解析 YAML frontmatter, 不依赖 PyYAML, 跟 validate_library.py 行为一致。"""
    if not md_text.startswith("---"):
        return {}
    end = md_text.find("\n---", 3)
    if end < 0:
        return {}
    block = md_text[3:end].strip()
    out: dict[str, str] = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*?)\s*$", line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def build_note(stem: str, primary_topic: str, topics: list[str], today: str) -> str:
    title = clean_title(stem)
    kws = extract_keywords(stem, primary_topic)
    pdf_link = f"[[{stem}.pdf]]"
    topics_yaml = ", ".join(topics)

    # 关键词展示
    if kws:
        kw_lines = "\n".join(f"- {k}" for k in kws)
    else:
        kw_lines = "- (无明显关键词, 依赖读 PDF 后补充)"

    body = f"""---
title: {yaml_escape(title)}
pdf: {yaml_escape(pdf_link)}
primary_topic: {yaml_escape(primary_topic)}
topics: [{topics_yaml}]
status: unread
reading_stage: filename-only
confidence: low
source_basis: filename
date_added: {today}
tags: [paper]
---

# {title}

## 基本信息
- **PDF**: {pdf_link}
- **primary_topic**: `{primary_topic}`
- **topics**: {', '.join(f'`{t}`' for t in topics)}
- **状态**: unread (仅根据文件名推断, 待阅读全文确认)
- **date_added**: {today}

## 文件名推断

> 仅根据文件名推断, 未读 PDF 内容。读完 PDF 后请把 `source_basis` 改为 `pdf-text`,
> 并把 `confidence` / `reading_stage` 升级。

**提取的关键词**:

{kw_lines}

**文件名模式**: `{stem}`

## 可能研究方向

> 基于 primary_topic + topics 推测, 仅作入门指引。

- 属于主题: **{primary_topic}**
- 关联主题: {', '.join(t for t in topics if t != primary_topic) or '(无)'}

## 待读问题

> 读 PDF 前先列 2-3 个你想在论文里找到答案的问题。

1.
2.
3.

## 阅读笔记

> 边读边记; 用 `[[双链]]` 关联到其他论文笔记 / 主题首页。

## 关键贡献

> 读完填

## 方法

> 读完填

## 实验

> 读完填

## 局限

> 读完填

## 相关论文

> 用 `[[]]` 链接到其他论文笔记或主题首页, 例如 [[{primary_topic}]]。

"""
    return body


def main():
    parser = argparse.ArgumentParser(
        description="为 01-Papers/ 下的每个 PDF 生成同名 .md 骨架笔记",
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
        "--force", action="store_true",
        help="覆盖 status=unread + source_basis=filename 的骨架笔记 (保护已读笔记)",
    )
    parser.add_argument(
        "--really-force", action="store_true",
        help="无条件覆盖所有 .md, 包括 status=read 或 source_basis=pdf-text 的笔记。"
             "日常增量用 --force 即可, 除非要重置整个库",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="只统计将生成/跳过的数量, 不实际写文件",
    )
    args = parser.parse_args()

    if not args.papers.is_dir():
        sys.exit(f"错误: 目录不存在: {args.papers}")
    if not args.topics_json.is_file():
        sys.exit(
            f"错误: {args.topics_json} 不存在, 先跑 scripts/classify_papers.py 生成。"
        )

    paper_topics = json.loads(args.topics_json.read_text(encoding="utf-8"))

    pdfs = sorted(p for p in args.papers.iterdir() if p.suffix.lower() == ".pdf")
    # 排除非论文文件 (paper_classification.md 等)
    today = date.today().isoformat()

    created, skipped, forced, protected = 0, 0, 0, 0
    for pdf in pdfs:
        md_path = pdf.with_suffix(".md")
        # 跳过清单文件
        if md_path.name in {"paper_classification.md", "paper_topics.json"}:
            continue
        if md_path.exists() and not args.force and not args.really_force:
            skipped += 1
            continue
        if md_path.exists():
            # 已存在: 检查要不要保护
            if not args.really_force:
                # --force 模式: 只覆盖骨架 (status=unread + source_basis=filename)
                text = md_path.read_text(encoding="utf-8", errors="replace")
                fm = parse_frontmatter(text)
                if fm:
                    status = fm.get("status", "")
                    source = fm.get("source_basis", "")
                    if status != "unread" or source != "filename":
                        # 已是精读/非骨架, 保护
                        protected += 1
                        continue
            forced += 1

        primary = paper_topics.get(pdf.stem, ["U_未归类"])[0]
        topics = paper_topics.get(pdf.stem, [primary])
        content = build_note(pdf.stem, primary, topics, today)

        if not args.dry_run:
            md_path.write_text(content, encoding="utf-8")
        created += 1

    print(f"总计 PDF: {len(pdfs)}")
    print(f"骨架笔记生成: {created} (其中覆盖: {forced})")
    print(f"跳过已存在:  {skipped}")
    if args.force and not args.really_force:
        print(f"保护已读笔记: {protected} (status=read 或 source_basis=pdf-text, 未覆盖)")
    if args.dry_run:
        print("(dry-run: 未实际写文件)")


if __name__ == "__main__":
    main()
