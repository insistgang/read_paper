#!/usr/bin/env python3
"""论文库健康检查。

扫描仓库, 检测:
  1. 孤立 PDF (没有同名 .md)
  2. 孤立 .md (指向不存在的 PDF); 例外: "示例-*"/"模板-*"/"template-*" 开头
     的笔记视为模板, 允许没 PDF
  3. frontmatter 必填/推荐字段缺失
     - 必填 (骨架阶段也要求): title, pdf, primary_topic, status, date_added, tags
     - 推荐 (仅 source_basis=pdf-text 时要求): authors, year, venue,
       topics, source_basis, reading_stage, confidence
  4. PDF 重复 (按 md5)

退出码:
  0  一切正常
  1  有 warning (建议处理)
  2  有 error (必须处理)
  3  参数错误
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path
from typing import Optional

# 必填: 不管骨架还是完整笔记都要有
REQUIRED_FM_FIELDS = {"title", "pdf", "primary_topic", "status", "date_added", "tags"}
# 推荐: 完整笔记应该有, 骨架阶段(source_basis=filename)允许空
RECOMMENDED_FM_FIELDS = {"authors", "year", "venue", "topics", "source_basis", "reading_stage", "confidence"}
AI_START_MARKER = "<!-- AI_READING_NOTE_START -->"
AI_END_MARKER = "<!-- AI_READING_NOTE_END -->"
AI_REQUIRED_HEADINGS = tuple(f"## {number}." for number in range(1, 13))
COVERAGE_RE = re.compile(r"\((\d+)/(\d+)\s*页(?:\)|[;；])")


def md5_of(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def parse_frontmatter(md_text: str) -> dict[str, str]:
    """粗略解析 YAML frontmatter, 不依赖 PyYAML, 容错好。"""
    if not md_text.startswith("---"):
        return {}
    end = md_text.find("\n---", 3)
    if end < 0:
        return {}
    block = md_text[3:end].strip()
    out: dict[str, str] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line or line.startswith("#") or line.startswith("-"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*?)\s*$", line)
        if not m:
            i += 1
            continue
        key, value = m.group(1), m.group(2)
        i += 1
        list_items = []
        while i < len(lines):
            item = re.match(r'^\s+-\s+(.+?)\s*$', lines[i])
            if not item:
                break
            list_items.append(item.group(1).strip())
            i += 1
        out[key] = f"[{', '.join(list_items)}]" if list_items else value
    return out


def is_blank_frontmatter_value(value: str) -> bool:
    normalized = value.strip().strip('"').strip("'").strip()
    return normalized in {"", "[]", "null", "None", "~"}


def frontmatter_scalar(value: str) -> str:
    return value.strip().strip('"').strip("'").strip()


def parse_coverage_marker(text: str) -> Optional[tuple[int, int]]:
    """解析 `(N/M 页)` 和补读后的 `(M/M 页; 原 AI 主体...)` 覆盖标记。"""
    match = COVERAGE_RE.search(text)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def check_ai_note(md_path: Path, text: str, fm: dict[str, str]) -> tuple[list[str], list[str]]:
    """检查 AI 笔记状态、区块结构和提取覆盖范围。"""
    errors, warnings = [], []
    status = frontmatter_scalar(fm.get("status", ""))
    start_count = text.count(AI_START_MARKER)
    end_count = text.count(AI_END_MARKER)

    if status == "ai-read":
        if start_count != 1 or end_count != 1:
            errors.append(
                f"[AI 区块错误] {md_path.name}: "
                f"START={start_count}, END={end_count}, ai-read 必须各有 1 个"
            )
            return errors, warnings

        ai_block = text.split(AI_START_MARKER, 1)[1].split(AI_END_MARKER, 1)[0]
        missing = [heading for heading in AI_REQUIRED_HEADINGS if heading not in ai_block]
        if missing:
            errors.append(
                f"[AI 章节缺失] {md_path.name}: {', '.join(missing)}"
            )
        if "无 LLM 模式" in ai_block:
            errors.append(f"[AI fallback 残留] {md_path.name}")

        coverage = parse_coverage_marker(ai_block)
        if coverage and coverage[0] < coverage[1]:
            warnings.append(
                f"[AI 提取不完整] {md_path.name}: "
                f"只覆盖 {coverage[0]}/{coverage[1]} 页"
            )

    if status == "extraction_failed":
        expected = {
            "reading_stage": "extraction-failed",
            "confidence": "low",
            "source_basis": "pdf-extraction-failed",
        }
        mismatches = []
        for key, expected_value in expected.items():
            actual = frontmatter_scalar(fm.get(key, ""))
            if actual != expected_value:
                mismatches.append(f"{key}={actual or '(空)'}")
        if start_count or end_count:
            mismatches.append(f"AI markers={start_count}/{end_count}")
        if mismatches:
            errors.append(
                f"[提取失败状态错误] {md_path.name}: " + ", ".join(mismatches)
            )

    return errors, warnings


# 统一"非论文笔记"排除规则 (跟 start.sh / scripts/paper / generate_skeleton_notes 一致):
#   - paper_classification.md: 分类清单, 机器生成的索引
#   - 示例-* / 模板-* / template-*: 用户的参考笔记, 允许没 PDF
# 真实论文卡片数应该 == PDF 数
_NON_PAPER_NOTE_STEMS = ("paper_classification",)
_NON_PAPER_NOTE_PREFIXES = ("示例-", "模板-", "template-")


def is_paper_note(name: str) -> bool:
    """判定一个 .md 文件名 (含扩展名) 是不是真实论文笔记。"""
    stem = Path(name).stem
    if stem in _NON_PAPER_NOTE_STEMS:
        return False
    return not any(stem.startswith(p) for p in _NON_PAPER_NOTE_PREFIXES)


def check_library(papers: Path, notes: Path) -> tuple[list, list]:
    """检查 PDF (在 papers/) 和 .md 笔记 (在 notes/) 是否一一对应。

    返回 (errors, warnings) 列表。
    """
    errors, warnings = [], []
    if not papers.is_dir():
        return ([f"01-Papers/ 不存在: {papers}"], [])
    if not notes.is_dir():
        return ([f"02-Notes/Papers/ 不存在: {notes}"], [])

    pdfs = {p.stem: p for p in papers.glob("*.pdf")}
    mds = {p.stem: p for p in notes.glob("*.md")}

    # 1. 孤立 PDF (有 PDF 但没同名 .md)
    orphan_pdfs = sorted(set(pdfs) - set(mds))
    for stem in orphan_pdfs:
        warnings.append(f"[孤立 PDF] 没有同名 .md: {pdfs[stem].name}")

    # 2. 孤立 .md (有笔记但 PDF 不存在)
    orphan_mds = sorted(set(mds) - set(pdfs))
    for stem in orphan_mds:
        warnings.append(f"[孤立 .md] 找不到同名 PDF: {mds[stem].name}")

    # 3. frontmatter 完整性
    for stem, md_path in sorted(mds.items()):
        text = md_path.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        if not fm:
            warnings.append(f"[无 frontmatter] {md_path.name}")
            continue
        missing = REQUIRED_FM_FIELDS - set(fm.keys())
        if missing:
            warnings.append(f"[frontmatter 缺字段] {md_path.name}: {', '.join(sorted(missing))}")
        # 推荐字段: 只在 source_basis == 'pdf-text' 时警告, 骨架阶段不警告
        document_type = frontmatter_scalar(fm.get("document_type", "paper")) or "paper"
        if frontmatter_scalar(fm.get("source_basis", "")) == "pdf-text" and document_type != "supplementary":
            optional_missing = RECOMMENDED_FM_FIELDS - set(fm.keys())
            if optional_missing:
                warnings.append(
                    f"[推荐字段缺失 - 完整笔记阶段] {md_path.name}: "
                    f"{', '.join(sorted(optional_missing))}"
                )
            optional_blank = sorted(
                field
                for field in RECOMMENDED_FM_FIELDS
                if field in fm and is_blank_frontmatter_value(fm[field])
            )
            if optional_blank:
                warnings.append(
                    f"[推荐字段为空 - 完整笔记阶段] {md_path.name}: "
                    f"{', '.join(optional_blank)}"
                )

        ai_errors, ai_warnings = check_ai_note(md_path, text, fm)
        errors.extend(ai_errors)
        warnings.extend(ai_warnings)

    # 4. PDF 重复 (md5)
    by_hash: dict[str, list[Path]] = {}
    for p in pdfs.values():
        try:
            h = md5_of(p)
        except OSError as e:
            warnings.append(f"[无法读取] {p.name}: {e}")
            continue
        by_hash.setdefault(h, []).append(p)
    for h, group in sorted(by_hash.items(), key=lambda kv: -len(kv[1])):
        if len(group) > 1:
            warnings.append(
                f"[重复 PDF] {len(group)} 个文件内容相同 ({h[:8]}...): "
                + ", ".join(p.name for p in group)
            )

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(
        description="论文库健康检查 (孤立文件 / frontmatter / 重复 / inbox 残留)",
    )
    parser.add_argument(
        "root", nargs="?", type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="仓库根目录 (默认: 脚本同级的上级目录)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="显示全部 warning, 不截断",
    )
    args = parser.parse_args()

    root = args.root
    if not root.is_dir():
        sys.exit(f"错误: 仓库根目录不存在: {root}")

    papers = root / "01-Papers"
    notes = root / "02-Notes" / "Papers"
    verbose = args.verbose

    print(f"📚 论文库健康检查 — 根目录: {root}\n")

    errs, warns = check_library(papers, notes)

    # 统计
    pdf_count = len(list(papers.glob("*.pdf"))) if papers.is_dir() else 0
    md_count = len(list(notes.glob("*.md"))) if notes.is_dir() else 0
    print(f"📊 PDF (01-Papers/): {pdf_count} / 论文笔记 (02-Notes/Papers/): {md_count}")
    print()

    # 按类别统计 warnings
    by_kind: dict[str, int] = {}
    for w in warns:
        m = re.match(r"^\[([^\]]+)\]", w)
        kind = m.group(1) if m else "其他"
        by_kind[kind] = by_kind.get(kind, 0) + 1

    if errs:
        print(f"❌ Errors ({len(errs)}):")
        for e in errs:
            print(f"  {e}")
        print()
    if warns:
        print(f"⚠️  Warnings 总计: {len(warns)}")
        for kind, n in sorted(by_kind.items(), key=lambda kv: -kv[1]):
            print(f"   - {kind}: {n}")
        print()
        # 默认每类最多展示 5 条, 用 --verbose 看全部
        limit = None if verbose else 5
        for kind in sorted(by_kind.keys()):
            items = [w for w in warns if w.startswith(f"[{kind}]")]
            shown = items if limit is None else items[:limit]
            for w in shown:
                print(f"  {w}")
            if limit and len(items) > limit:
                print(f"  ... [{kind}] 还有 {len(items) - limit} 条, 加 -v/--verbose 看全部")
        print()

    if not errs and not warns:
        print("✅ 一切正常, 论文库很健康。")
        return 0
    if errs:
        return 2
    return 1


if __name__ == "__main__":
    sys.exit(main())
