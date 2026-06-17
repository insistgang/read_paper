#!/usr/bin/env python3
"""为旧版部分分页 AI 笔记追加缺失页线索。

该脚本只处理已有 AI 区块中标记为 `(N/M 页)` 且 N < M 的笔记:
  - 从 PDF 中提取缺失页文本
  - 在 AI 区块尾部插入/替换 `## 全文补读记录`
  - 保留原 AI 主体的 `(N/M 页)` 覆盖标记
  - frontmatter 明确保持 `content_coverage: partial`

追加摘录不等于重新基于全文综合，因此该脚本绝不把笔记标成全文完成。
需要完整精读时使用 generate_ai_reading_notes.py 的全文分块模式。
"""
import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PAPERS = ROOT / "01-Papers"
DEFAULT_NOTES = ROOT / "02-Notes" / "Papers"
AI_START_MARKER = "<!-- AI_READING_NOTE_START -->"
AI_END_MARKER = "<!-- AI_READING_NOTE_END -->"
SUPPLEMENT_HEADING = "## 全文补读记录"


@dataclass
class Coverage:
    old_pages: int
    total_pages: int


def parse_coverage(text: str) -> Optional[Coverage]:
    matches = list(re.finditer(r"\((\d+)/(\d+)\s*页\)", text))
    if not matches:
        return None
    match = matches[-1]
    old_pages = int(match.group(1))
    total_pages = int(match.group(2))
    if old_pages >= total_pages:
        return None
    return Coverage(old_pages, total_pages)


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---", 4)
    if end < 0:
        return "", text
    return text[: end + 4], text[end + 4 :].lstrip("\n")


def set_frontmatter_scalar(fm: str, key: str, value: str) -> str:
    if not fm:
        return fm
    pattern = re.compile(rf"^{re.escape(key)}:\s*.*$", re.MULTILINE)
    line = f"{key}: {value}"
    if pattern.search(fm):
        return pattern.sub(line, fm)
    return fm[:-4].rstrip() + "\n" + line + "\n---"


def extract_pages(pdf_path: Path, start_page: int, end_page: int) -> list[str]:
    try:
        import PyPDF2
    except ImportError:
        raise SystemExit("PyPDF2 未安装, 无法提取 PDF 文本")

    texts: list[str] = []
    with pdf_path.open("rb") as fh:
        reader = PyPDF2.PdfReader(fh)
        actual_end = min(end_page, len(reader.pages))
        for page_index in range(start_page - 1, actual_end):
            page_text = reader.pages[page_index].extract_text() or ""
            page_text = page_text.encode("utf-8", errors="surrogatepass").decode(
                "utf-8", errors="replace"
            )
            texts.append(page_text)
    return texts


def clean_line(line: str) -> str:
    return re.sub(r"\s+", " ", line).strip()


def likely_heading(line: str) -> bool:
    line = clean_line(line)
    if len(line) < 5 or len(line) > 120:
        return False
    if line.endswith(".") and len(line.split()) > 6:
        return False
    if re.match(r"^(\d+(\.\d+)*\.?\s+)?[A-Z][A-Za-z0-9 ,:/&()\-]{4,}$", line):
        return True
    if re.match(r"^(Abstract|Introduction|Related Work|Method|Experiments?|Results?|Discussion|Conclusion|References)\b", line, re.I):
        return True
    return False


def references_like(text: str) -> bool:
    lines = [clean_line(line) for line in text.splitlines() if clean_line(line)]
    if not lines:
        return False
    ref_lines = sum(1 for line in lines if re.match(r"^\[\d+\]", line) or "doi.org" in line)
    return "References" in text[:1000] or ref_lines >= max(3, len(lines) // 4)


def collect_headings(page_texts: list[str], first_page: int, limit: int = 12) -> list[str]:
    headings: list[str] = []
    seen = set()
    for offset, text in enumerate(page_texts):
        page_no = first_page + offset
        for raw in text.splitlines():
            line = clean_line(raw)
            if likely_heading(line) and line not in seen:
                headings.append(f"p.{page_no}: {line}")
                seen.add(line)
            if len(headings) >= limit:
                return headings
    return headings


def collect_key_snippets(page_texts: list[str], first_page: int, limit: int = 12) -> list[str]:
    keywords = re.compile(
        r"\b(Table|Fig\.|Figure|Conclusion|Experiment|Result|Dataset|Ablation|Limitation|Discussion|Benchmark|Evaluation|Accuracy|PSNR|AP|mIoU|FLOPs|latency)\b",
        re.I,
    )
    snippets: list[str] = []
    seen = set()
    for offset, text in enumerate(page_texts):
        page_no = first_page + offset
        lines = [clean_line(line) for line in text.splitlines()]
        for line in lines:
            if len(line) < 40 or len(line) > 260:
                continue
            if not keywords.search(line):
                continue
            key = line.lower()
            if key in seen:
                continue
            snippets.append(f"p.{page_no}: {line}")
            seen.add(key)
            if len(snippets) >= limit:
                return snippets
    if snippets:
        return snippets

    for offset, text in enumerate(page_texts[: min(6, len(page_texts))]):
        page_no = first_page + offset
        cleaned = clean_line(text)
        sentences = re.split(r"(?<=[.!?。！？])\s+", cleaned)
        for sentence in sentences:
            if 60 <= len(sentence) <= 260:
                snippets.append(f"p.{page_no}: {sentence}")
                break
        if len(snippets) >= limit:
            break
    return snippets


def build_supplement(
    stem: str,
    old_pages: int,
    total_pages: int,
    page_texts: list[str],
    completed_at: str,
) -> str:
    first_missing = old_pages + 1
    missing_range = f"{first_missing}-{total_pages}" if first_missing < total_pages else str(total_pages)
    nonempty_pages = sum(1 for text in page_texts if clean_line(text))
    reference_pages = sum(1 for text in page_texts if references_like(text))
    headings = collect_headings(page_texts, first_missing)
    snippets = collect_key_snippets(page_texts, first_missing)

    if reference_pages == len(page_texts) and page_texts:
        page_summary = "缺失页主要为参考文献或文献列表, 对方法和实验正文影响较小。"
    elif reference_pages:
        page_summary = f"缺失页包含正文/附录内容, 其中约 {reference_pages} 页偏参考文献。"
    else:
        page_summary = "缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。"

    heading_block = "\n".join(f"- {item}" for item in headings) if headings else "- 未从缺失页稳定识别到章节标题"
    snippet_block = "\n".join(f"- {item}" for item in snippets) if snippets else "- 缺失页可提取文本较少, 未形成稳定摘录"

    return f"""{SUPPLEMENT_HEADING}

- **补读日期**: {completed_at}
- **补充浏览范围**: PDF p.{missing_range}; 原 AI 主体仍只覆盖 p.1-{old_pages}，本记录仅提供后续页线索。
- **提取情况**: 缺失页 {len(page_texts)} 页, 其中 {nonempty_pages} 页提取到可读文本。{page_summary}
- **状态说明**: 这是缺失页线索摘录，不是基于全文重新综合的精读；`content_coverage` 仍为 `partial`，`human_reviewed` 仍为 `false`。

### 缺失页章节线索

{heading_block}

### 缺失页关键摘录

{snippet_block}
"""


def replace_or_insert_supplement(ai_block: str, supplement: str) -> str:
    if SUPPLEMENT_HEADING in ai_block:
        pattern = re.compile(
            rf"\n{re.escape(SUPPLEMENT_HEADING)}\n.*?(?=\n<!-- AI_READING_NOTE_END -->)",
            re.S,
        )
        return pattern.sub("\n" + supplement.rstrip() + "\n", ai_block)
    return ai_block.replace(AI_END_MARKER, supplement.rstrip() + "\n" + AI_END_MARKER)


def update_note_text(text: str, supplement: str, total_pages: int, completed_at: str) -> str:
    coverage = parse_coverage(text)
    if coverage is None:
        return text

    fm, body = split_frontmatter(text)
    if fm:
        fm = set_frontmatter_scalar(fm, "reading_stage", "ai-partial-supplement")
        fm = set_frontmatter_scalar(fm, "content_coverage", "partial")
        fm = set_frontmatter_scalar(fm, "full_text_covered", "false")
        fm = set_frontmatter_scalar(fm, "full_text_completed_at", completed_at)
        fm = set_frontmatter_scalar(
            fm,
            "full_text_completion_basis",
            f'"supplemental page clues only; AI synthesis remains {coverage.old_pages}/{coverage.total_pages} pages"',
        )

    start = body.find(AI_START_MARKER)
    end = body.find(AI_END_MARKER, start)
    if start < 0 or end < 0:
        return text
    end += len(AI_END_MARKER)
    ai_block = body[start:end]

    ai_block = replace_or_insert_supplement(ai_block, supplement)
    body = body[:start] + ai_block + body[end:]
    return (fm + "\n" + body) if fm else body


def complete_one(stem: str, papers_dir: Path, notes_dir: Path, completed_at: str, dry_run: bool) -> str:
    md_path = notes_dir / f"{stem}.md"
    pdf_path = papers_dir / f"{stem}.pdf"
    if not md_path.is_file():
        return f"skip {stem}: note missing"
    if not pdf_path.is_file():
        return f"skip {stem}: pdf missing"

    text = md_path.read_text(encoding="utf-8", errors="replace")
    coverage = parse_coverage(text)
    if coverage is None:
        return f"skip {stem}: no partial coverage marker"

    page_texts = extract_pages(pdf_path, coverage.old_pages + 1, coverage.total_pages)
    supplement = build_supplement(
        stem=stem,
        old_pages=coverage.old_pages,
        total_pages=coverage.total_pages,
        page_texts=page_texts,
        completed_at=completed_at,
    )
    updated = update_note_text(text, supplement, coverage.total_pages, completed_at)
    if updated == text:
        return f"skip {stem}: unchanged"
    if not dry_run:
        md_path.write_text(updated, encoding="utf-8")
    return f"done {stem}: {coverage.old_pages}/{coverage.total_pages} -> {coverage.total_pages}/{coverage.total_pages}"


def main() -> int:
    parser = argparse.ArgumentParser(description="补全部分页提取论文笔记的缺失页记录")
    parser.add_argument("--only", nargs="+", required=True, help="要处理的 PDF stem")
    parser.add_argument("--papers", type=Path, default=DEFAULT_PAPERS)
    parser.add_argument("--notes", type=Path, default=DEFAULT_NOTES)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    for stem in args.only:
        print(complete_one(stem, args.papers, args.notes, args.date, args.dry_run))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
