#!/usr/bin/env python3
"""Sync paper note display fields and fill old placeholders from AI notes.

This script intentionally does not rename Markdown/PDF files. File stems are
still used as the stable link between `01-Papers/*.pdf` and
`02-Notes/Papers/*.md`.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_library import AI_END_MARKER, AI_START_MARKER, frontmatter_scalar, parse_frontmatter


ROOT = SCRIPT_DIR.parent
DEFAULT_NOTES = ROOT / "02-Notes" / "Papers"
PLACEHOLDER_RE = re.compile(
    r"待补充|待深入阅读后补充|待从PDF提取补充|基于摘要初步推断|"
    r"作者的研究背景是什么|作者采用了什么样的研究方法|"
    r"在?哪些数据集/场景下进行了实验|论文自己提到的局限|"
    r"你对这篇论文的看法"
)

SECTION_TO_AI = {
    "摘要": 2,
    "研究背景与动机": 3,
    "关键贡献": 4,
    "方法": 5,
    "实验": 6,
    "局限": 8,
    "个人评论": 7,
}


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---", 4)
    if end < 0:
        return "", text
    return text[: end + 5], text[end + 5 :]


def ai_block(text: str) -> str:
    if AI_START_MARKER not in text or AI_END_MARKER not in text:
        return ""
    return text.split(AI_START_MARKER, 1)[1].split(AI_END_MARKER, 1)[0]


def parse_ai_sections(block: str) -> dict[int, str]:
    matches = list(re.finditer(r"(?m)^##\s+(\d+)\.\s+.*$", block))
    sections: dict[int, str] = {}
    for index, match in enumerate(matches):
        number = int(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        sections[number] = block[start:end].strip()
    return sections


def normalize_yaml_value(value: str) -> str:
    value = frontmatter_scalar(value)
    if not value or value in {"[]", "null", "None", "~"}:
        return "未明确"
    if value.startswith("[") and value.endswith("]"):
        inner = value.strip("[] ")
        if not inner:
            return "未明确"
        parts = [part.strip().strip('"').strip("'") for part in inner.split(",")]
        parts = [part for part in parts if part]
        return "; ".join(parts) if parts else "未明确"
    return value


def escape_table_cell(value: str) -> str:
    return value.replace("|", "\\|")


def table_value(fm: dict[str, str], key: str, fallback: str = "未明确") -> str:
    value = normalize_yaml_value(fm.get(key, ""))
    if value == "未明确" and fallback != "未明确":
        value = fallback
    return escape_table_cell(value)


def replace_first_h1(body: str, title: str) -> str:
    lines = body.splitlines()
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            if line[2:].strip() == title:
                return body
            lines[idx] = f"# {title}"
            return "\n".join(lines) + ("\n" if body.endswith("\n") else "")
        if line.strip():
            break
    return f"\n# {title}\n" + body.lstrip("\n")


def sync_article_table(body: str, fm: dict[str, str], fallback_title: str) -> str:
    replacements = {
        "题目": table_value(fm, "title", fallback=fallback_title),
        "作者": table_value(fm, "authors"),
        "发表时间": table_value(fm, "year"),
        "刊物/会议": table_value(fm, "venue"),
        "DOI": table_value(fm, "doi"),
    }
    for label, value in replacements.items():
        pattern = re.compile(rf"(?m)^(\| \*\*{re.escape(label)}\*\* \|).*?(\|\s*)$")
        body = pattern.sub(lambda match, v=value: f"{match.group(1)} {v} {match.group(2)}", body, count=1)
    return body


def should_replace_section(content: str) -> bool:
    return bool(PLACEHOLDER_RE.search(content))


def replacement_for_section(title: str, sections: dict[int, str]) -> Optional[str]:
    number = SECTION_TO_AI[title]
    content = sections.get(number, "").strip()
    if not content:
        return None
    if title == "个人评论" and sections.get(9):
        content = content + "\n\n### 使用建议\n\n" + sections[9].strip()
    return f"## {title}\n\n{content.strip()}\n"


def replace_section_if_placeholder(body: str, title: str, replacement: str) -> str:
    pattern = re.compile(rf"(?ms)^## {re.escape(title)}\n(.*?)(?=^## |\Z)")
    match = pattern.search(body)
    if not match:
        return body
    original = match.group(0)
    content = match.group(1)
    if not should_replace_section(content):
        return body
    return body[: match.start()] + replacement + body[match.end() :]


def sync_placeholder_sections(body: str, sections: dict[int, str]) -> str:
    for title in SECTION_TO_AI:
        replacement = replacement_for_section(title, sections)
        if replacement:
            body = replace_section_if_placeholder(body, title, replacement)
    return body


def sync_note_text(text: str, fallback_title: str = "未明确") -> tuple[str, bool]:
    original = text
    frontmatter_text, rest = split_frontmatter(text)
    fm = parse_frontmatter(text)
    if not frontmatter_text or not fm:
        return text, False

    block = ai_block(text)
    sections = parse_ai_sections(block)
    before_ai, sep, after_ai = rest.partition(AI_START_MARKER)
    if not sep:
        return text, False

    title = table_value(fm, "title", fallback=fallback_title)
    before_ai = replace_first_h1(before_ai, title)
    before_ai = sync_article_table(before_ai, fm, fallback_title=fallback_title)
    before_ai = sync_placeholder_sections(before_ai, sections)
    updated = frontmatter_text + before_ai + sep + after_ai
    return updated, updated != original


def sync_notes(notes_dir: Path, dry_run: bool = False, limit: Optional[int] = None) -> tuple[int, int]:
    changed = 0
    total = 0
    for path in sorted(notes_dir.glob("*.md")):
        total += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        updated, did_change = sync_note_text(text, fallback_title=path.stem)
        if did_change:
            changed += 1
            if not dry_run:
                path.write_text(updated, encoding="utf-8")
        if limit and total >= limit:
            break
    return total, changed


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notes-dir", type=Path, default=DEFAULT_NOTES)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args(argv)

    total, changed = sync_notes(args.notes_dir, dry_run=args.dry_run, limit=args.limit)
    print(f"notes_scanned {total}")
    print(f"notes_changed {changed}")
    print(f"dry_run {args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
