#!/usr/bin/env python3
"""生成论文库阅读质量仪表盘。

这个脚本不修改论文笔记正文, 只扫描 01-Papers/ 和 02-Notes/Papers/,
输出一个可在 Obsidian 里打开的维护入口页。
"""
import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_library import (  # noqa: E402
    AI_END_MARKER,
    AI_START_MARKER,
    frontmatter_scalar,
    is_blank_frontmatter_value,
    parse_coverage_marker,
    parse_frontmatter,
)

ROOT = SCRIPT_DIR.parent
DEFAULT_PAPERS = ROOT / "01-Papers"
DEFAULT_NOTES = ROOT / "02-Notes" / "Papers"
DEFAULT_OUT = ROOT / "03-Literature" / "阅读质量仪表盘.md"
METADATA_FIELDS = ("authors", "year", "venue")
SUPPLEMENTARY_TOPIC = "Z_工具与杂项_figures"


@dataclass
class NoteIssue:
    name: str
    detail: str = ""
    coverage: str = ""


@dataclass
class DashboardStats:
    generated_on: str
    pdf_count: int
    note_count: int
    status_counts: Counter = field(default_factory=Counter)
    source_basis_counts: Counter = field(default_factory=Counter)
    reading_stage_counts: Counter = field(default_factory=Counter)
    topic_counts: Counter = field(default_factory=Counter)
    document_type_counts: Counter = field(default_factory=Counter)
    metadata_blank_counts: Counter = field(default_factory=Counter)
    partial_extractions: list[NoteIssue] = field(default_factory=list)
    full_extraction_count: int = 0
    unknown_extraction_count: int = 0
    extraction_failed: list[NoteIssue] = field(default_factory=list)
    ai_marker_issues: list[NoteIssue] = field(default_factory=list)
    supplementary_candidates: list[NoteIssue] = field(default_factory=list)
    missing_frontmatter: list[NoteIssue] = field(default_factory=list)


def _coverage_from_text(text: str) -> Optional[tuple[int, int]]:
    return parse_coverage_marker(text)


def _counter_value(counter: Counter, key: str) -> int:
    return int(counter.get(key, 0))


def _is_blank_or_missing(fm: dict[str, str], field_name: str) -> bool:
    return field_name not in fm or is_blank_frontmatter_value(fm[field_name])


def collect_stats(root: Path = ROOT) -> DashboardStats:
    papers = root / "01-Papers"
    notes = root / "02-Notes" / "Papers"
    pdfs = sorted(papers.glob("*.pdf")) if papers.is_dir() else []
    note_files = sorted(notes.glob("*.md")) if notes.is_dir() else []
    stats = DashboardStats(
        generated_on=date.today().isoformat(),
        pdf_count=len(pdfs),
        note_count=len(note_files),
    )

    for md_path in note_files:
        text = md_path.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        if not fm:
            stats.missing_frontmatter.append(NoteIssue(md_path.name))
            continue

        status = frontmatter_scalar(fm.get("status", "unknown")) or "unknown"
        source_basis = frontmatter_scalar(fm.get("source_basis", "unknown")) or "unknown"
        reading_stage = frontmatter_scalar(fm.get("reading_stage", "unknown")) or "unknown"
        primary_topic = frontmatter_scalar(fm.get("primary_topic", "U_未归类")) or "U_未归类"
        document_type = frontmatter_scalar(fm.get("document_type", "paper")) or "paper"

        stats.status_counts[status] += 1
        stats.source_basis_counts[source_basis] += 1
        stats.reading_stage_counts[reading_stage] += 1
        stats.topic_counts[primary_topic] += 1
        stats.document_type_counts[document_type] += 1

        if primary_topic == SUPPLEMENTARY_TOPIC or document_type == "supplementary":
            stats.supplementary_candidates.append(NoteIssue(md_path.name, primary_topic))

        if status == "extraction_failed":
            stats.extraction_failed.append(NoteIssue(md_path.name))
            continue

        if document_type != "supplementary":
            for field_name in METADATA_FIELDS:
                if _is_blank_or_missing(fm, field_name):
                    stats.metadata_blank_counts[field_name] += 1

        start_count = text.count(AI_START_MARKER)
        end_count = text.count(AI_END_MARKER)
        if start_count != end_count:
            stats.ai_marker_issues.append(
                NoteIssue(md_path.name, f"START={start_count}, END={end_count}")
            )

        if status == "ai-read" and start_count == 1 and end_count == 1:
            coverage = _coverage_from_text(text)
            if coverage is None:
                stats.unknown_extraction_count += 1
            else:
                current, total = coverage
                if current < total:
                    stats.partial_extractions.append(
                        NoteIssue(md_path.name, coverage=f"{current}/{total}")
                    )
                else:
                    stats.full_extraction_count += 1

    return stats


def _count_table(title: str, counter: Counter, limit: int = 12) -> str:
    if not counter:
        return f"## {title}\n\n_(暂无)_\n"
    rows = ["| 项目 | 数量 |", "|---|---:|"]
    for key, value in counter.most_common(limit):
        rows.append(f"| `{key}` | {value} |")
    return f"## {title}\n\n" + "\n".join(rows) + "\n"


def _issue_lines(issues: list[NoteIssue], limit: int) -> str:
    if not issues:
        return "- 无\n"
    lines = []
    for issue in issues[:limit]:
        stem = Path(issue.name).stem
        suffix = ""
        if issue.coverage:
            suffix = f" - {issue.coverage} 页"
        elif issue.detail:
            suffix = f" - {issue.detail}"
        lines.append(f"- [[{stem}]]{suffix}")
    if len(issues) > limit:
        lines.append(f"- ... 还有 {len(issues) - limit} 条")
    return "\n".join(lines) + "\n"


def build_dashboard(stats: DashboardStats, limit: int = 25) -> str:
    partial_count = len(stats.partial_extractions)
    failed_count = len(stats.extraction_failed)
    metadata_gap_total = sum(stats.metadata_blank_counts.values())
    supplementary_count = len(stats.supplementary_candidates)
    ai_read_count = _counter_value(stats.status_counts, "ai-read")
    read_like_count = (
        _counter_value(stats.status_counts, "read")
        + _counter_value(stats.status_counts, "done")
        + ai_read_count
    )

    next_actions = [
        f"- [ ] 重新处理部分页提取笔记: {partial_count} 篇",
        f"- [ ] 修复 PDF 文本提取失败: {failed_count} 篇",
        f"- [ ] 补齐 authors/year/venue 元数据空值: {metadata_gap_total} 处",
        f"- [ ] 复核补充材料/图表类文件标记: {supplementary_count} 篇",
        "- [ ] 跑 `python3 scripts/validate_library.py --verbose` 做最终验收",
    ]

    body = f"""# 阅读质量仪表盘

> 自动生成于 {stats.generated_on}。这是维护入口页, 用来区分 AI 首轮阅读稿、人工精读、提取失败和补充材料。

## 总览

| 指标 | 数量 |
|---|---:|
| PDF 文件 | {stats.pdf_count} |
| Markdown 笔记 | {stats.note_count} |
| 已有阅读稿或已读 | {read_like_count} |
| AI 首轮阅读稿 | {ai_read_count} |
| 完整页数覆盖的 AI 稿 | {stats.full_extraction_count} |
| 部分页提取的 AI 稿 | {partial_count} |
| 未记录页数覆盖的 AI 稿 | {stats.unknown_extraction_count} |
| 提取失败 | {failed_count} |
| 元数据空值 | {metadata_gap_total} |
| 补充材料/图表类文件 | {supplementary_count} |
| 缺 frontmatter | {len(stats.missing_frontmatter)} |

## 下一步维护队列

{chr(10).join(next_actions)}

{_count_table("阅读状态分布", stats.status_counts)}

{_count_table("来源依据分布", stats.source_basis_counts)}

{_count_table("阅读阶段分布", stats.reading_stage_counts)}

{_count_table("文档类型分布", stats.document_type_counts)}

## 元数据缺口

| 字段 | 空值/缺失数量 |
|---|---:|
| `authors` | {stats.metadata_blank_counts.get("authors", 0)} |
| `year` | {stats.metadata_blank_counts.get("year", 0)} |
| `venue` | {stats.metadata_blank_counts.get("venue", 0)} |

## 部分页提取

{_issue_lines(stats.partial_extractions, limit)}

## 提取失败

{_issue_lines(stats.extraction_failed, limit)}

## 补充材料/图表类文件

{_issue_lines(stats.supplementary_candidates, limit)}

## AI marker 异常

{_issue_lines(stats.ai_marker_issues, limit)}

{_count_table("Top 主题", stats.topic_counts, limit=20)}

## Dataview 工作台

### 未完成人工复核的 AI 阅读稿

```dataview
TABLE primary_topic, year, venue, confidence
FROM "02-Notes/Papers"
WHERE status = "ai-read" AND human_reviewed != true
SORT primary_topic ASC, file.name ASC
```

### 元数据待补

```dataview
TABLE primary_topic, authors, year, venue
FROM "02-Notes/Papers"
WHERE status != "extraction_failed" AND document_type != "supplementary"
  AND (length(authors) = 0 OR !year OR !venue)
SORT primary_topic ASC, file.name ASC
```

### 补充材料/图表类文件

```dataview
TABLE status, document_type, primary_topic
FROM "02-Notes/Papers"
WHERE primary_topic = "{SUPPLEMENTARY_TOPIC}" OR document_type = "supplementary"
SORT file.name ASC
```

---

*由 `scripts/generate_dashboard.py` 生成。重新生成: `python3 scripts/generate_dashboard.py`。*
"""
    return body


def main() -> int:
    parser = argparse.ArgumentParser(description="生成 03-Literature/阅读质量仪表盘.md")
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=ROOT,
        help="知识库根目录 (默认: 当前脚本上级目录)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help="输出 Markdown 路径",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        help="每个问题清单最多展示多少条",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只打印结果, 不写文件",
    )
    args = parser.parse_args()

    stats = collect_stats(args.root)
    content = build_dashboard(stats, limit=args.limit)
    if args.dry_run:
        print(content)
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(content, encoding="utf-8")
    print(f"已写入 {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
