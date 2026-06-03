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
  5. 00-Inbox 残留 (有 PDF 但没导入到 01-Papers)
  6. 04-Attachments/PDFs/ 不再作为论文主入口 (警告)

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

# 必填: 不管骨架还是完整笔记都要有
REQUIRED_FM_FIELDS = {"title", "pdf", "primary_topic", "status", "date_added", "tags"}
# 推荐: 完整笔记应该有, 骨架阶段(source_basis=filename)允许空
RECOMMENDED_FM_FIELDS = {"authors", "year", "venue", "topics", "source_basis", "reading_stage", "confidence"}


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
    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.startswith("#") or line.startswith("-"):
            # 简化: 不展开 list/block, 只把第一行 key: value 抓出来
            continue
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*?)\s*$", line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


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


def check_papers_dir(papers: Path) -> tuple[list, list]:
    """返回 (errors, warnings) 列表"""
    errors, warnings = [], []
    if not papers.is_dir():
        return ([f"01-Papers/ 不存在: {papers}"], [])

    pdfs = {p.stem: p for p in papers.glob("*.pdf")}
    # 真实论文卡片: 排除分类清单 + 示例/模板笔记
    mds = {p.stem: p for p in papers.glob("*.md") if is_paper_note(p.name)}

    # 1. 孤立 PDF (有 PDF 但没同名 .md)
    orphan_pdfs = sorted(set(pdfs) - set(mds))
    for stem in orphan_pdfs:
        warnings.append(f"[孤立 PDF] 没有同名 .md: {pdfs[stem].name}")

    # 2. 孤立 .md (有笔记但 PDF 不存在) -- 因为 mds 已经过滤了非论文笔记, 这里不用再判
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
        if fm.get("source_basis") == "pdf-text":
            optional_missing = RECOMMENDED_FM_FIELDS - set(fm.keys())
            if optional_missing:
                warnings.append(
                    f"[推荐字段缺失 - 完整笔记阶段] {md_path.name}: "
                    f"{', '.join(sorted(optional_missing))}"
                )

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


def check_inbox(inbox: Path) -> list:
    warnings = []
    if not inbox.is_dir():
        return []
    pdfs = list(inbox.glob("*.pdf"))
    mds = list(inbox.glob("*.md"))
    if pdfs and not mds:
        warnings.append(
            f"[00-Inbox 残留] {len(pdfs)} 个 PDF 没导入到 01-Papers, "
            f"跑 ./start.sh 选项 2 或 scripts/paper_ai.py batch 处理"
        )
    return warnings


def check_attachments_pdfs(att: Path) -> list:
    warnings = []
    if not att.is_dir():
        return []
    pdfs = list(att.glob("*.pdf"))
    if pdfs:
        warnings.append(
            f"[04-Attachments/PDFs 残留] {len(pdfs)} 个 PDF, 当前约定 PDF 应在 01-Papers/. "
            f"如果是临时附件可忽略, 否则建议合并到 01-Papers/。"
        )
    return warnings


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
    inbox = root / "00-Inbox"
    attachments = root / "04-Attachments" / "PDFs"
    verbose = args.verbose

    print(f"📚 论文库健康检查 — 根目录: {root}\n")

    errs, warns = check_papers_dir(papers)
    warns += check_inbox(inbox)
    warns += check_attachments_pdfs(attachments)

    # 统计
    pdf_count = len(list(papers.glob("*.pdf"))) if papers.is_dir() else 0
    md_count = len([p for p in papers.glob("*.md") if is_paper_note(p.name)]) if papers.is_dir() else 0
    print(f"📊 01-Papers/ 下: {pdf_count} PDF / {md_count} 笔记")
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
