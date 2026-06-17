#!/usr/bin/env python3
"""Run a three-pass audit over the paper knowledge base.

Pass 1 checks assets: PDF/MD/cache/table coverage.
Pass 2 checks note structure: frontmatter, visible learning sections, AI block.
Pass 3 checks learning usefulness: metadata, human review state, weak content cues.
"""

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_library import (  # noqa: E402
    AI_END_MARKER,
    AI_REQUIRED_HEADINGS,
    AI_START_MARKER,
    REQUIRED_FM_FIELDS,
    frontmatter_scalar,
    is_blank_frontmatter_value,
    parse_frontmatter,
)


ROOT = SCRIPT_DIR.parent
DEFAULT_OUT = ROOT / "03-Literature" / "全库三遍Review报告.md"
BREAKDOWN_START = "<!-- BATCH_READING_BREAKDOWN_START -->"
BREAKDOWN_END = "<!-- BATCH_READING_BREAKDOWN_END -->"
VISIBLE_SECTIONS = (
    "## 摘要",
    "## 研究背景与动机",
    "## 关键贡献",
    "## 方法",
    "## 实验",
    "## 局限",
    "## 个人评论",
)
METADATA_FIELDS = ("authors", "year", "venue")
PLACEHOLDER_RE = re.compile(r"(读完填|待补充|TODO|未填写)")
PDF_LINK_RE = re.compile(r"\[\[([^\]]+?)(?:\.pdf)?\]\]")
AUTHOR_AFFILIATION_RE = re.compile(
    r"\b("
    r"university|institute|department|school|campus|faculty|college|"
    r"laborator(?:y|ies)|centre|center|hospital|ministry|academy|"
    r"corporation|company|ltd|inc|germany|china|hamburg|beijing|shanghai|"
    r"abstract|keywords|corresponding|email"
    r")\b|@",
    re.IGNORECASE,
)
VENUE_AUTHOR_LINE_RE = re.compile(
    r"\b(?:senior\s+member|member|fellow)\s*,\s*IEEE\b|"
    r"\bcorresponding\s+author\b|"
    r"†|"
    r"\b[A-Z][A-Za-z-]+\s+[A-Z][A-Za-z-]*\d+(?:,\d+)+\b"
)
VENUE_AFFILIATION_RE = re.compile(
    r"\b("
    r"university|institute|department|school|faculty|college|"
    r"laborator(?:y|ies)|centre|center|hospital|ministry|academy|"
    r"corporation|research\s+laborator(?:y|ies)|foundation|funding|grant|"
    r"authorized\s+licensed\s+use|downloaded\s+on|abstract|keywords|"
    r"corresponding|email|e-mail"
    r")\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class AuditIssue:
    pass_name: str
    code: str
    severity: str
    stem: str
    detail: str


@dataclass
class AuditResult:
    generated_on: str
    pdf_count: int
    note_count: int
    cache_count: int
    literature_count: int
    breakdown_rows: int
    breakdown_unique_stems: int
    ai_block_count: int
    human_reviewed_count: int
    status_counts: Counter = field(default_factory=Counter)
    topic_counts: Counter = field(default_factory=Counter)
    issue_counts: Counter = field(default_factory=Counter)
    issues: list[AuditIssue] = field(default_factory=list)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def ai_block(text: str) -> str:
    if AI_START_MARKER not in text or AI_END_MARKER not in text:
        return ""
    return text.split(AI_START_MARKER, 1)[1].split(AI_END_MARKER, 1)[0]


def frontmatter_bool(fm: dict[str, str], key: str) -> bool:
    return frontmatter_scalar(fm.get(key, "")).lower() == "true"


def metadata_items(value: str) -> list[str]:
    normalized = frontmatter_scalar(value)
    if is_blank_frontmatter_value(normalized):
        return []
    if normalized.startswith("[") and normalized.endswith("]"):
        inner = normalized[1:-1].strip()
        if not inner:
            return []
        return [
            item.strip().strip('"').strip("'").strip()
            for item in inner.split(",")
            if item.strip().strip('"').strip("'").strip()
        ]
    return [normalized]


def suspicious_authors_reason(value: str) -> Optional[str]:
    items = metadata_items(value)
    if not items:
        return None
    suspicious = [item for item in items if AUTHOR_AFFILIATION_RE.search(item)]
    if suspicious:
        sample = "; ".join(suspicious[:3])
        return f"authors 像机构/地址/正文片段: {sample}"
    return None


def suspicious_venue_reason(value: str) -> Optional[str]:
    normalized = frontmatter_scalar(value)
    if is_blank_frontmatter_value(normalized):
        return None
    if VENUE_AUTHOR_LINE_RE.search(normalized):
        return "venue 像作者署名行或作者身份描述"
    if VENUE_AFFILIATION_RE.search(normalized):
        return "venue 像机构/基金/下载声明/正文片段"
    comma_count = normalized.count(",")
    if len(normalized) > 120 and comma_count >= 4:
        return "venue 过长且包含多段逗号分隔内容，疑似误填"
    return None


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---", 4)
    if end < 0:
        return "", text
    return text[: end + 4], text[end + 4 :]


def parse_breakdown_stems(path: Path) -> list[str]:
    if not path.is_file():
        return []
    text = read_text(path)
    if BREAKDOWN_START not in text or BREAKDOWN_END not in text:
        return []
    inside = text.split(BREAKDOWN_START, 1)[1].split(BREAKDOWN_END, 1)[0]
    stems: list[str] = []
    for line in inside.splitlines():
        if not line.startswith("| ") or line.startswith("| 序号") or line.startswith("|---"):
            continue
        match = re.search(r"\[\[([^\]|]+)", line)
        if match:
            stems.append(match.group(1))
    return stems


def visible_section_body(text: str, heading: str) -> str:
    _, body = split_frontmatter(text)
    start = body.find(heading)
    if start < 0:
        return ""
    next_heading = re.search(r"(?m)^##\s+", body[start + len(heading) :])
    if not next_heading:
        return body[start + len(heading) :].strip()
    end = start + len(heading) + next_heading.start()
    return body[start + len(heading) : end].strip()


def add_issue(
    issues: list[AuditIssue],
    pass_name: str,
    code: str,
    severity: str,
    stem: str,
    detail: str,
) -> None:
    issues.append(AuditIssue(pass_name, code, severity, stem, detail))


def check_assets(
    root: Path,
    pdfs: dict[str, Path],
    notes: dict[str, Path],
    caches: dict[str, Path],
    breakdown_stems: list[str],
    issues: list[AuditIssue],
) -> None:
    for stem in sorted(set(pdfs) - set(notes)):
        add_issue(issues, "第一遍：资产完整性", "note_missing", "error", stem, "有 PDF 但没有同名 Markdown 笔记")
    for stem in sorted(set(notes) - set(pdfs)):
        add_issue(issues, "第一遍：资产完整性", "pdf_missing", "error", stem, "有 Markdown 笔记但没有同名 PDF")
    for stem, pdf in sorted(pdfs.items()):
        try:
            size = pdf.stat().st_size
            header = pdf.read_bytes()[:5]
        except OSError as exc:
            add_issue(issues, "第一遍：资产完整性", "pdf_unreadable", "error", stem, str(exc))
            continue
        if size <= 0:
            add_issue(issues, "第一遍：资产完整性", "pdf_empty", "error", stem, "PDF 文件大小为 0")
        elif not header.startswith(b"%PDF"):
            add_issue(issues, "第一遍：资产完整性", "pdf_header_suspicious", "warning", stem, "文件头不是 %PDF")
        cache = caches.get(stem)
        if cache is None:
            add_issue(issues, "第一遍：资产完整性", "cache_missing", "warning", stem, "缺少 .paper-cache/extracts 同名文本缓存")
        elif cache.stat().st_size <= 0:
            add_issue(issues, "第一遍：资产完整性", "cache_empty", "warning", stem, "文本缓存为空")
        else:
            try:
                if b"\x00" in cache.read_bytes():
                    add_issue(issues, "第一遍：资产完整性", "cache_nul_character", "warning", stem, "文本缓存中存在 NUL 字符")
            except OSError as exc:
                add_issue(issues, "第一遍：资产完整性", "cache_unreadable", "warning", stem, str(exc))

    breakdown_set = set(breakdown_stems)
    for stem in sorted(set(notes) - breakdown_set):
        add_issue(issues, "第一遍：资产完整性", "breakdown_missing", "warning", stem, "论文阅读拆解表缺少该笔记行")
    for stem in sorted(breakdown_set - set(notes)):
        add_issue(issues, "第一遍：资产完整性", "breakdown_orphan", "warning", stem, "论文阅读拆解表中存在无对应笔记的行")

    for required in ("01-Papers", "02-Notes/Papers", "03-Literature", "scripts", "tests"):
        if not (root / required).exists():
            add_issue(issues, "第一遍：资产完整性", "core_dir_missing", "error", required, "核心目录不存在")


def check_note_structure(path: Path, text: str, fm: dict[str, str], issues: list[AuditIssue]) -> None:
    stem = path.stem
    if "\x00" in text:
        add_issue(issues, "第二遍：笔记结构", "nul_character", "error", stem, "Markdown 中存在 NUL 字符")
    if not fm:
        add_issue(issues, "第二遍：笔记结构", "frontmatter_missing", "warning", stem, "缺少 YAML frontmatter")
    else:
        missing = sorted(REQUIRED_FM_FIELDS - set(fm))
        if missing:
            add_issue(issues, "第二遍：笔记结构", "frontmatter_required_missing", "warning", stem, ", ".join(missing))
        pdf_value = frontmatter_scalar(fm.get("pdf", ""))
        pdf_match = PDF_LINK_RE.search(pdf_value)
        if not pdf_match:
            add_issue(issues, "第二遍：笔记结构", "pdf_link_missing", "warning", stem, "frontmatter.pdf 不是 Obsidian PDF 双链")
        else:
            linked = pdf_match.group(1).removesuffix(".pdf")
            if linked != stem:
                add_issue(issues, "第二遍：笔记结构", "pdf_link_mismatch", "warning", stem, f"frontmatter.pdf 指向 {linked}")

    for heading in VISIBLE_SECTIONS:
        content = visible_section_body(text, heading)
        if not content:
            add_issue(issues, "第二遍：笔记结构", "visible_section_missing", "warning", stem, f"缺少或空置 {heading}")
        elif PLACEHOLDER_RE.search(content):
            add_issue(issues, "第二遍：笔记结构", "visible_section_placeholder", "warning", stem, f"{heading} 仍包含占位文本")

    start_count = text.count(AI_START_MARKER)
    end_count = text.count(AI_END_MARKER)
    if start_count != 1 or end_count != 1:
        add_issue(issues, "第二遍：笔记结构", "ai_marker_count", "error", stem, f"START={start_count}, END={end_count}")
        return
    block = ai_block(text)
    missing_ai = [heading for heading in AI_REQUIRED_HEADINGS if heading not in block]
    if missing_ai:
        add_issue(issues, "第二遍：笔记结构", "ai_heading_missing", "error", stem, ", ".join(missing_ai))
    if "无 LLM 模式" in block:
        add_issue(issues, "第二遍：笔记结构", "ai_fallback_left", "error", stem, "AI 区块仍含 fallback 文本")


def check_learning_value(path: Path, text: str, fm: dict[str, str], issues: list[AuditIssue]) -> None:
    stem = path.stem
    status = frontmatter_scalar(fm.get("status", ""))
    document_type = frontmatter_scalar(fm.get("document_type", "paper")) or "paper"
    primary_topic = frontmatter_scalar(fm.get("primary_topic", ""))
    if status != "extraction_failed" and document_type != "supplementary":
        blanks = [
            field
            for field in METADATA_FIELDS
            if field not in fm or is_blank_frontmatter_value(fm[field])
        ]
        if blanks:
            add_issue(issues, "第三遍：学习可用性", "metadata_blank", "warning", stem, ", ".join(blanks))
        authors_reason = suspicious_authors_reason(fm.get("authors", ""))
        if authors_reason:
            add_issue(
                issues,
                "第三遍：学习可用性",
                "metadata_authors_suspicious",
                "warning",
                stem,
                authors_reason,
            )
        venue_reason = suspicious_venue_reason(fm.get("venue", ""))
        if venue_reason:
            add_issue(
                issues,
                "第三遍：学习可用性",
                "metadata_venue_suspicious",
                "warning",
                stem,
                venue_reason,
            )

    if status == "ai-read" and not frontmatter_bool(fm, "human_reviewed"):
        add_issue(issues, "第三遍：学习可用性", "needs_human_review", "info", stem, "AI 首轮阅读稿尚未人工复核")

    if primary_topic == "Z_工具与杂项_figures" and document_type != "supplementary":
        add_issue(issues, "第三遍：学习可用性", "supplementary_candidate", "warning", stem, "疑似图表/补充材料，尚未标记 document_type: supplementary")

    personal = visible_section_body(text, "## 个人评论")
    if personal and len(re.sub(r"\s+", "", personal)) < 40:
        add_issue(issues, "第三遍：学习可用性", "personal_comment_thin", "info", stem, "个人评论较短，学习迁移价值有限")

    block = ai_block(text)
    unknown_count = block.count("未明确")
    if unknown_count >= 8:
        add_issue(issues, "第三遍：学习可用性", "many_unknown_fields", "info", stem, f"AI 精读中出现 {unknown_count} 次“未明确”")


def collect_audit(root: Path = ROOT) -> AuditResult:
    papers = root / "01-Papers"
    notes_dir = root / "02-Notes" / "Papers"
    cache_dir = root / ".paper-cache" / "extracts"
    literature_dir = root / "03-Literature"

    pdfs = {p.stem: p for p in sorted(papers.glob("*.pdf"))} if papers.is_dir() else {}
    notes = {p.stem: p for p in sorted(notes_dir.glob("*.md"))} if notes_dir.is_dir() else {}
    caches = {p.stem: p for p in sorted(cache_dir.glob("*.txt"))} if cache_dir.is_dir() else {}
    breakdown_stems = parse_breakdown_stems(root / "论文阅读拆解表.md")

    issues: list[AuditIssue] = []
    check_assets(root, pdfs, notes, caches, breakdown_stems, issues)

    status_counts: Counter = Counter()
    topic_counts: Counter = Counter()
    ai_block_count = 0
    human_reviewed_count = 0
    for md_path in notes.values():
        text = read_text(md_path)
        fm = parse_frontmatter(text)
        status = frontmatter_scalar(fm.get("status", "unknown")) or "unknown"
        topic = frontmatter_scalar(fm.get("primary_topic", "U_未归类")) or "U_未归类"
        status_counts[status] += 1
        topic_counts[topic] += 1
        if AI_START_MARKER in text and AI_END_MARKER in text:
            ai_block_count += 1
        if frontmatter_bool(fm, "human_reviewed"):
            human_reviewed_count += 1
        check_note_structure(md_path, text, fm, issues)
        check_learning_value(md_path, text, fm, issues)

    issue_counts = Counter(issue.code for issue in issues)
    return AuditResult(
        generated_on=date.today().isoformat(),
        pdf_count=len(pdfs),
        note_count=len(notes),
        cache_count=len(caches),
        literature_count=len(list(literature_dir.glob("*.md"))) if literature_dir.is_dir() else 0,
        breakdown_rows=len(breakdown_stems),
        breakdown_unique_stems=len(set(breakdown_stems)),
        ai_block_count=ai_block_count,
        human_reviewed_count=human_reviewed_count,
        status_counts=status_counts,
        topic_counts=topic_counts,
        issue_counts=issue_counts,
        issues=issues,
    )


def issue_table(issues: list[AuditIssue], limit: int) -> str:
    if not issues:
        return "- 无\n"
    severity_order = {"error": 0, "warning": 1, "info": 2}
    ordered = sorted(
        issues,
        key=lambda issue: (
            severity_order.get(issue.severity, 9),
            issue.code,
            issue.stem,
            issue.detail,
        ),
    )
    rows = ["| 严重级别 | 问题 | 文件 | 说明 |", "|---|---|---|---|"]
    for issue in ordered[:limit]:
        rows.append(f"| {issue.severity} | `{issue.code}` | [[{issue.stem}]] | {issue.detail} |")
    if len(ordered) > limit:
        rows.append(f"| ... | ... | ... | 还有 {len(ordered) - limit} 条 |")
    return "\n".join(rows) + "\n"


def counter_table(counter: Counter, limit: int = 20) -> str:
    if not counter:
        return "- 无\n"
    rows = ["| 项目 | 数量 |", "|---|---:|"]
    for key, count in counter.most_common(limit):
        rows.append(f"| `{key}` | {count} |")
    return "\n".join(rows) + "\n"


def render_report(result: AuditResult, limit: int = 30) -> str:
    by_pass: dict[str, list[AuditIssue]] = defaultdict(list)
    for issue in result.issues:
        by_pass[issue.pass_name].append(issue)
    severity_counts = Counter(issue.severity for issue in result.issues)
    unresolved = len([issue for issue in result.issues if issue.severity in {"error", "warning"}])

    body = f"""# 全库三遍 Review 报告

> 自动生成于 {result.generated_on}。本报告扫描 `01-Papers/`、`02-Notes/Papers/`、`.paper-cache/extracts/` 与 `论文阅读拆解表.md`。

## 结论

| 指标 | 数量 |
|---|---:|
| PDF | {result.pdf_count} |
| Markdown 笔记 | {result.note_count} |
| AI 精读区块 | {result.ai_block_count} |
| PDF 文本缓存 | {result.cache_count} |
| 论文拆解表行数 | {result.breakdown_rows} |
| 论文拆解表唯一论文 | {result.breakdown_unique_stems} |
| 主题/入口文件 | {result.literature_count} |
| 人工复核 | {result.human_reviewed_count} |
| error | {severity_counts.get("error", 0)} |
| warning | {severity_counts.get("warning", 0)} |
| info | {severity_counts.get("info", 0)} |
| 待处理 error/warning | {unresolved} |

## 三遍 Review 口径

1. **第一遍：资产完整性**：PDF、Markdown、缓存、拆解表是否互相覆盖。
2. **第二遍：笔记结构**：frontmatter、可见学习章节、AI 精读 12 节结构是否完整。
3. **第三遍：学习可用性**：元数据、人工复核、补充材料标记、个人评论和“未明确”密度是否足够支撑学习与写作。

## 阅读状态分布

{counter_table(result.status_counts)}

## Top 主题

{counter_table(result.topic_counts, limit=25)}

## 问题类型分布

{counter_table(result.issue_counts, limit=40)}

## 第一遍：资产完整性

{issue_table(by_pass.get("第一遍：资产完整性", []), limit)}

## 第二遍：笔记结构

{issue_table(by_pass.get("第二遍：笔记结构", []), limit)}

## 第三遍：学习可用性

{issue_table(by_pass.get("第三遍：学习可用性", []), limit)}

## 下一步处理顺序

1. 先处理 `error`：PDF/MD 缺配对、AI marker 或 12 节结构问题。
2. 再处理 `warning`：补齐 `authors/year/venue`，补足可见学习章节，把补充材料标记为 `document_type: supplementary`。
3. 最后处理 `info`：人工复核 `ai-read` 笔记，强化 `个人评论`、适用场景、可借鉴点和与其他论文的关系。

---

*由 `scripts/audit_knowledge_base.py` 生成。重新生成：`python3 scripts/audit_knowledge_base.py`。*
"""
    return body


def main() -> int:
    parser = argparse.ArgumentParser(description="生成全库三遍 Review 报告")
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=ROOT,
        help="知识库根目录",
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="输出 Markdown 路径")
    parser.add_argument("--limit", type=int, default=30, help="每类问题最多展示多少条")
    parser.add_argument("--dry-run", action="store_true", help="只打印报告, 不写文件")
    args = parser.parse_args()

    result = collect_audit(args.root)
    report = render_report(result, limit=args.limit)
    if args.dry_run:
        print(report)
    else:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report, encoding="utf-8")
        print(f"已写入 {args.out}")
    errors = sum(1 for issue in result.issues if issue.severity == "error")
    warnings = sum(1 for issue in result.issues if issue.severity == "warning")
    if errors:
        return 2
    if warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
