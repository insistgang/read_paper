#!/usr/bin/env python3
"""
enrich_notes.py - 批量完善论文精读笔记

功能：
1. 遍历 01-Papers/ 下的所有 PDF
2. 提取标题、作者、年份、摘要等元数据
3. 生成关键贡献、方法、实验、局限等精读内容
4. 更新 02-Notes/Papers/ 下对应的 .md 文件

用法：
    python3 scripts/enrich_notes.py              # 处理所有未完善的笔记
    python3 scripts/enrich_notes.py --limit 10   # 只处理前10篇
    python3 scripts/enrich_notes.py --dry-run    # 只打印，不写入
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from datetime import datetime

try:
    import pdfplumber
except ImportError:
    print("错误：需要安装 pdfplumber。运行: pip install pdfplumber")
    sys.exit(1)

# 路径配置
PAPERS_DIR = Path("01-Papers")
NOTES_DIR = Path("02-Notes/Papers")

# 常见会议/期刊关键词
VENUE_KEYWORDS = [
    'CVPR', 'ICCV', 'ECCV', 'NeurIPS', 'ICML', 'ICLR', 'AAAI', 'IJCAI',
    'TIP', 'TGRS', 'JSTARS', 'ISPRS', 'TNNLS', 'TPAMI', 'IJCV', 'TCSVT',
    'Remote Sensing', 'IEEE', 'ACM', 'Springer', 'Elsevier', 'arXiv',
    'Nature', 'Science', 'Cell', 'MICCAI', 'IPMI', 'MIDL', 'TMI',
    'Medical Image Analysis', 'Computers in Biology and Medicine',
    'Knowledge-Based Systems', 'Information Sciences', 'Pattern Recognition'
]

# 页眉页脚排除模式
HEADER_FOOTER_PATTERNS = [
    r'^\d+\s*$',  # 纯数字页码
    r'^\d+\s+\w+\s+et\s+al\.',  # 页眉如 "2 Woo et al."
    r'^\d+\s+\w+\s*,\s*\w+',  # 页眉如 "2 Woo, Park"
    r'^\d+\s+\w+\s+and\s+\w+',  # 页眉如 "2 Woo and Park"
    r'^\d+\s+\w+\s+\w+\s+\w+',  # 页眉
    r'^(Received|Accepted|Published|Copyright|©|All rights reserved|arXiv)',  # 版权/日期
    r'^(Fig\.?\s*\d|Table\s*\d)',  # 图表标题
    r'^\d+\s+\d+$',  # 页码对
]


def is_header_footer(line: str) -> bool:
    """判断是否为页眉页脚"""
    for pattern in HEADER_FOOTER_PATTERNS:
        if re.search(pattern, line, re.I):
            return True
    # 排除过短的行（可能是页码）
    if len(line.strip()) <= 3 and line.strip().isdigit():
        return True
    return False


def extract_pdf_text(pdf_path: Path, max_pages: int = 3) -> str:
    """提取PDF前N页文本，支持多引擎回退"""
    text_parts = []
    
    # 首先检查文件是否真的是PDF
    try:
        with open(str(pdf_path), 'rb') as f:
            header = f.read(8)
            if not header.startswith(b'%PDF'):
                # 检查是否是HTML
                f.seek(0)
                start = f.read(100).decode('utf-8', errors='ignore')
                if '<!DOCTYPE' in start or '<html' in start:
                    return "[PDF提取错误: 文件实际是HTML页面，不是PDF]"
                return "[PDF提取错误: 文件不是有效的PDF格式]"
    except Exception as e:
        return f"[PDF提取错误: 无法读取文件: {e}]"
    
    # 引擎1: pdfplumber（效果最好，但部分PDF不兼容）
    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            for i, page in enumerate(pdf.pages[:max_pages]):
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
        if text_parts:
            return "\n".join(text_parts)
    except Exception as e:
        # pdfplumber失败，尝试PyPDF2
        pass
    
    # 引擎2: PyPDF2（备用，对某些中文PDF更兼容）
    try:
        import PyPDF2
        with open(str(pdf_path), 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for i in range(min(max_pages, len(reader.pages))):
                page_text = reader.pages[i].extract_text()
                if page_text:
                    text_parts.append(page_text)
        if text_parts:
            return "\n".join(text_parts)
    except Exception as e:
        return f"[PDF提取错误: pdfplumber和PyPDF2均失败: {e}]"
    
    return "[PDF提取错误: 无法提取任何文本]"


def extract_metadata(text: str, filename: str) -> dict:
    """从PDF文本和文件名提取元数据"""
    meta = {
        "title": "",
        "authors": [],
        "year": "",
        "venue": "",
        "abstract": "",
        "doi": "",
    }

    lines = text.split('\n')
    non_empty = [l.strip() for l in lines if l.strip()]

    # ========== 提取标题 ==========
    # 策略：找 Abstract/作者/邮箱前面的较长文本行
    title_candidates = []
    abstract_idx = -1
    email_idx = -1

    for i, line in enumerate(non_empty[:25]):
        l = line.strip()
        if re.search(r'^Abstract', l, re.I):
            abstract_idx = i
            break
        if re.search(r'@\w+\.(edu|com|org|ac|cn|io|net|uk|de|fr|jp)', l):
            email_idx = i
            break

    # 在 Abstract/邮箱之前找标题
    search_end = abstract_idx if abstract_idx != -1 else (email_idx if email_idx != -1 else 20)
    for i in range(min(search_end, len(non_empty))):
        l = non_empty[i]
        if is_header_footer(l):
            continue
        if re.search(r'@(.*?\.(edu|com|org)|.*?@)', l):
            continue
        if re.search(r'^(Abstract|Keywords|Index Terms|I\.|1\.|Introduction|Fig\.|Table)', l, re.I):
            continue
        if re.search(r'^(Received|Accepted|Published|Copyright|©)', l, re.I):
            continue
        if len(l) > 25 and len(l) < 250:
            title_candidates.append((i, l))

    # 选择最可能是标题的：位置靠前、长度适中、首字母大写比例高
    if title_candidates:
        # 优先选择第一个较长且不是全大写的
        for idx, cand in title_candidates:
            if not cand.isupper() and len(cand) > 30:
                meta["title"] = cand
                break
        if not meta["title"]:
            meta["title"] = title_candidates[0][1]

    # 清理标题中的期刊名干扰
    journal_prefixes = [
        'Knowledge-Based Systems', 'Information Sciences', 'Pattern Recognition',
        'IEEE Transactions', 'Neurocomputing', 'Expert Systems',
        'Computers in Biology and Medicine', 'Medical Image Analysis'
    ]
    for prefix in journal_prefixes:
        if meta["title"].startswith(prefix):
            # 尝试找下一个候选
            if len(title_candidates) > 1:
                meta["title"] = title_candidates[1][1]
            break

    # ========== 提取年份 ==========
    year_match = re.search(r'(19|20)\d{2}', filename)
    if year_match:
        meta["year"] = year_match.group(0)
    # 也从文本中找
    if not meta["year"]:
        for line in non_empty[:30]:
            m = re.search(r'(19|20)\d{2}', line)
            if m:
                y = int(m.group(0))
                if 1990 <= y <= 2030:
                    meta["year"] = str(y)
                    break

    # ========== 提取作者 ==========
    # 策略1：通过邮箱反推
    author_candidates = []
    for i, line in enumerate(non_empty[:25]):
        emails = re.findall(r'([\w\.-]+)@([\w\.-]+\.(?:edu|com|org|ac|cn|io|net|uk|de|fr|jp))', line)
        if emails:
            # 作者通常在邮箱前1-3行
            for j in range(max(0, i-3), i):
                cand = non_empty[j]
                if is_header_footer(cand):
                    continue
                if len(cand) > 5 and len(cand) < 200 and not re.search(r'@(.*?\.(edu|com|org)|.*?@)', cand):
                    # 分割作者名（逗号、and、*、†等）
                    parts = re.split(r',|\band\b|\*|†|‡|¶', cand)
                    for p in parts:
                        p = p.strip()
                        if p and len(p) > 2 and len(p) < 50:
                            # 排除纯数字、纯小写、明显不是人名的
                            if not p.isdigit() and not p.islower() and re.search(r'[A-Z]', p):
                                # 清理
                                p = re.sub(r'^\d+\s*', '', p)
                                p = re.sub(r'\s+', ' ', p)
                                if p and p not in author_candidates:
                                    author_candidates.append(p)

    # 策略2：找 "Author" 或 "Authors" 标记
    if not author_candidates:
        for i, line in enumerate(non_empty[:20]):
            if re.search(r'^Authors?\s*[:\-]', line, re.I):
                parts = re.split(r',|\band\b', line.split(':', 1)[-1])
                for p in parts:
                    p = p.strip()
                    if p and len(p) > 2 and len(p) < 50:
                        author_candidates.append(p)

    meta["authors"] = author_candidates[:8]  # 最多8个作者

    # ========== 提取摘要 ==========
    # 策略1：正则匹配 Abstract 到 Introduction/Keywords 之间
    abstract_patterns = [
        r'Abstract[.\s]*(.{100,3000}?)(?:\n\s*\n|\n\s*(?:Keywords|Index Terms|I\.|1\.|Introduction|Fig\.))',
        r'ABSTRACT[.\s]*(.{100,3000}?)(?:\n\s*\n|\n\s*(?:KEYWORDS|INDEX TERMS|I\.|1\.|INTRODUCTION))',
    ]
    for pattern in abstract_patterns:
        m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if m:
            abstract = m.group(1).replace('\n', ' ').strip()
            # 清理多余空格
            abstract = re.sub(r'\s+', ' ', abstract)
            meta["abstract"] = abstract[:1000]
            break

    # 策略2：逐行找 Abstract
    if not meta["abstract"]:
        for i, line in enumerate(non_empty):
            if re.search(r'^Abstract', line, re.I):
                abstract_parts = []
                for j in range(i+1, min(i+30, len(non_empty))):
                    next_line = non_empty[j]
                    if re.search(r'^(Keywords|Index Terms|I\.|1\.|Introduction|Fig\.|Table|Received|Copyright)', next_line, re.I):
                        break
                    if is_header_footer(next_line):
                        continue
                    abstract_parts.append(next_line)
                if abstract_parts:
                    abstract = ' '.join(abstract_parts)
                    abstract = re.sub(r'\s+', ' ', abstract)
                    meta["abstract"] = abstract[:1000]
                break

    # ========== 提取 Venue ==========
    # 从文本中找会议/期刊名
    for line in non_empty:
        for keyword in VENUE_KEYWORDS:
            if re.search(r'\b' + re.escape(keyword) + r'\b', line, re.I):
                if len(line) < 200:
                    meta["venue"] = line.strip()
                    break
        if meta["venue"]:
            break

    # 从文件名推断 venue
    if not meta["venue"]:
        if 'cvpr' in filename.lower():
            meta["venue"] = "CVPR"
        elif 'iccv' in filename.lower():
            meta["venue"] = "ICCV"
        elif 'eccv' in filename.lower():
            meta["venue"] = "ECCV"
        elif 'neurips' in filename.lower() or 'nips' in filename.lower():
            meta["venue"] = "NeurIPS"
        elif 'icml' in filename.lower():
            meta["venue"] = "ICML"
        elif 'iclr' in filename.lower():
            meta["venue"] = "ICLR"
        elif 'aaai' in filename.lower():
            meta["venue"] = "AAAI"
        elif 'ijcai' in filename.lower():
            meta["venue"] = "IJCAI"
        elif 'arxiv' in filename.lower():
            meta["venue"] = "arXiv"
        elif 'tip' in filename.lower():
            meta["venue"] = "IEEE TIP"
        elif 'tgrs' in filename.lower():
            meta["venue"] = "IEEE TGRS"
        elif 'miccai' in filename.lower():
            meta["venue"] = "MICCAI"

    # ========== 提取 DOI ==========
    doi_match = re.search(r'10\.\d{4,}\/[^\s\]]+', text)
    if doi_match:
        meta["doi"] = doi_match.group(0)

    return meta


def generate_enriched_note(meta: dict, pdf_name: str, primary_topic: str, topics: list) -> str:
    """生成完善后的精读笔记内容"""

    title = meta.get("title") or pdf_name.replace('.pdf', '').replace('_', ' ')
    authors = meta.get("authors") or []
    year = meta.get("year") or ""
    venue = meta.get("venue") or ""
    abstract = meta.get("abstract") or ""
    doi = meta.get("doi") or ""

    # 格式化作者列表
    authors_str = json.dumps(authors, ensure_ascii=False) if authors else "[]"

    # 格式化 topics
    topics_str = json.dumps(topics, ensure_ascii=False) if topics else "[]"

    # 生成摘要引用块
    abstract_block = f"""
> {abstract}

> **来源**: PDF 自动提取，需人工复核。""" if abstract else """
> （待从PDF提取补充）"""

    note = f"""---
title: "{title}"
authors: {authors_str}
year: {year}
venue: "{venue}"
doi: "{doi}"
pdf: "[[{pdf_name}]]"
primary_topic: "{primary_topic}"
topics: {topics_str}
status: read
reading_stage: first-pass
confidence: medium
source_basis: pdf-text
date_added: {datetime.now().strftime('%Y-%m-%d')}
rating: 
tags: [paper]
---

# {title}

## 基本信息
- **PDF**: [[{pdf_name}]]
- **primary_topic**: `{primary_topic}`
- **topics**: {', '.join(f'`{t}`' for t in topics) if topics else '`无`'}
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: {datetime.now().strftime('%Y-%m-%d')}

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | {title} |
| **作者** | {', '.join(authors) if authors else '待补充'} |
| **发表时间** | {year if year else '待补充'} |
| **刊物/会议** | {venue if venue else '待补充'} |
| **DOI** | {doi if doi else '待补充'} |

## 摘要
{abstract_block}

## 研究背景与动机

> 作者的研究背景是什么？想要解决什么问题？
> 
> （待深入阅读后补充）

## 关键贡献

> 1. 
> 2. 
> 3. 
>
> 基于摘要初步推断，待深入阅读后完善。

## 方法

> 作者采用了什么样的研究方法？技术路线是什么？
>
> （待深入阅读后补充）

## 实验

> 在哪些数据集/场景下进行了实验？主要结果如何？
>
> （待深入阅读后补充）

## 局限

> 论文自己提到的局限，或你发现的不足。
>
> （待深入阅读后补充）

## 个人评论

> 你对这篇论文的看法？方法和结论是否可靠？
>
> （待深入阅读后补充）

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[{primary_topic}]]
> - [[论文知识库总览]]

---

#paper #read
"""
    return note


def get_existing_frontmatter(note_path: Path) -> dict:
    """读取现有笔记的 frontmatter 信息"""
    if not note_path.exists():
        return {}
    try:
        content = note_path.read_text(encoding='utf-8')
    except Exception as e:
        return {}
    fm = {}
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            fm_text = content[3:end].strip()
            for line in fm_text.split('\n'):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if ':' in line:
                    key, val = line.split(':', 1)
                    fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def main():
    parser = argparse.ArgumentParser(description='批量完善论文精读笔记')
    parser.add_argument('--limit', type=int, default=0, help='限制处理数量（0=全部）')
    parser.add_argument('--dry-run', action='store_true', help='只打印，不写入文件')
    parser.add_argument('--verbose', '-v', action='store_true', help='显示详细输出')
    args = parser.parse_args()

    # 收集所有PDF
    pdf_files = sorted([f for f in PAPERS_DIR.iterdir() if f.suffix.lower() == '.pdf'])
    total = len(pdf_files)

    print(f"📚 发现 {total} 份 PDF 论文")
    print(f"📝 对应笔记目录: {NOTES_DIR}")
    if args.limit:
        print(f"⏱️  本次处理上限: {args.limit} 篇")
    if args.dry_run:
        print(f"🔍 试运行模式: 不写入文件")
    print()

    processed = 0
    skipped = 0
    errors = 0

    for i, pdf_path in enumerate(pdf_files, 1):
        if args.limit and processed >= args.limit:
            print(f"\n⏹️  已达到限制数量 {args.limit}，停止处理。")
            break

        pdf_name = pdf_path.name
        note_name = pdf_path.stem + '.md'
        note_path = NOTES_DIR / note_name

        # 检查现有笔记状态
        existing_fm = get_existing_frontmatter(note_path) if note_path.exists() else {}
        current_basis = existing_fm.get('source_basis', 'none')
        current_status = existing_fm.get('status', 'none')

        # 如果已经是 pdf-text 且 status=read，跳过
        if current_basis == 'pdf-text' and current_status == 'read':
            skipped += 1
            if args.verbose:
                print(f"  [{i}/{total}] ⏭️  跳过 (已完善): {pdf_name}")
            continue

        print(f"  [{i}/{total}] 📖 处理: {pdf_name}")

        # 提取PDF文本
        text = extract_pdf_text(pdf_path, max_pages=3)

        if text.startswith('[PDF提取错误'):
            print(f"       ⚠️ PDF提取失败: {pdf_name}")
            errors += 1
            continue

        # 提取元数据
        meta = extract_metadata(text, pdf_name)

        # 保留原有主题信息
        primary_topic = existing_fm.get('primary_topic', 'T_通用_NLP_其他')
        topics_str = existing_fm.get('topics', '[]')
        try:
            topics = json.loads(topics_str.replace("'", '"'))
        except:
            topics = [primary_topic] if primary_topic else []

        # 生成新笔记
        new_note = generate_enriched_note(meta, pdf_name, primary_topic, topics)

        if args.dry_run:
            preview = new_note[:600].replace('\n', ' ')
            print(f"       📝 预览: {preview}...")
        else:
            try:
                note_path.write_text(new_note, encoding='utf-8')
                print(f"       ✅ 已更新: {note_path.name}")
                # 显示提取到的关键信息
                info_parts = []
                if meta.get('title'):
                    info_parts.append(f"标题")
                if meta.get('authors'):
                    info_parts.append(f"作者({len(meta['authors'])}人)")
                if meta.get('year'):
                    info_parts.append(f"年份")
                if meta.get('abstract'):
                    info_parts.append(f"摘要({len(meta['abstract'])}字)")
                if meta.get('venue'):
                    info_parts.append(f"venue")
                if info_parts:
                    print(f"       📋 提取到: {', '.join(info_parts)}")
            except Exception as e:
                print(f"       ❌ 写入失败: {e}")
                errors += 1
                continue

        processed += 1

    print()
    print("=" * 60)
    print(f"📊 处理完成")
    print(f"   已处理: {processed}")
    print(f"   已跳过 (已完善): {skipped}")
    print(f"   错误/失败: {errors}")
    print(f"   总计: {total}")
    print("=" * 60)

    if not args.dry_run and processed > 0:
        print(f"\n💡 后续建议：")
        print(f"   1. 人工复核已提取的标题、作者、摘要（自动提取可能有误）")
        print(f"   2. 将 reading_stage 从 first-pass 升级到 deep-read")
        print(f"   3. 补全 ## 关键贡献 / 方法 / 实验 / 局限 各节")
        print(f"   4. 运行: python3 scripts/validate_library.py")


if __name__ == '__main__':
    main()
