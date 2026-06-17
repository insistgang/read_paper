#!/usr/bin/env python3
"""为每篇 PDF 生成"可直接阅读"的完整 AI 精读笔记 (使用 LLM 生成).

设计原则:
  1. PDF 文本只缓存到 .paper-cache/extracts/<stem>.txt, 永不进笔记
  2. 笔记里放 12 section 完整结构化内容, 短句摘录带页码, 不全文复制
  3. AI 区块用 HTML 注释包起来: <!-- AI_READING_NOTE_START --> ... <!-- AI_READING_NOTE_END -->
  4. 默认: 已生成过 AI 区块的笔记跳过 (找 marker, 看 status: ai-read)
  5. --force 重生成 AI 区块, 但绝不删除/修改人工内容
  6. frontmatter 升级:
     - status: ai-read (除非 human_reviewed=true)
     - reading_stage: ai-complete
     - source_basis: pdf-text
     - confidence: medium/high/low (按 PDF 提取质量)
     - ai_generated: true, human_reviewed: false
     - ai_generated_at: <date>
     - extract_cache: <path>
  7. 不动 01-Papers 任何文件, 不删 .paper-cache, 不动 PDF, 不 commit, 不 push

LLM 接入:
  - 配置 OLLAMA_BASE_URL: 用 ollama /api/chat
  - 配置 OPENAI_API_KEY + OPENAI_BASE_URL: 用 OpenAI 兼容 API
  - 都没配: 仅在显式 --no-llm 时允许生成模板
"""
import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PAPERS = ROOT / "01-Papers"
DEFAULT_NOTES = ROOT / "02-Notes" / "Papers"
DEFAULT_CACHE = ROOT / ".paper-cache" / "extracts"

AI_START_MARKER = "<!-- AI_READING_NOTE_START -->"
AI_END_MARKER = "<!-- AI_READING_NOTE_END -->"

# LLM 默认参数
LLM_MAX_TOKENS = 6000       # 12 section 内容大概 4-5K tokens, 留缓冲
LLM_TEMPERATURE = 0.3
LLM_TIMEOUT = 180


# ============== PDF 文本提取 ==============

def _sanitize_surrogates(s: str) -> str:
    """修复 PyPDF2 提取的未配对 surrogate, 避免后续写盘/JSON 失败.

    PyMuPDF/PyPDF2 偶尔会返回 lone-surrogate (\\uD800-\\uDBFF 无配对 \\uDC00-\\uDFFF),
    Python str 允许但 UTF-8 encode 直接 raise 'surrogates not allowed'.
    这里把这些字符替换为 U+FFFD (replacement char), 文本内容基本不丢, 字符数几乎不变.
    """
    if not s:
        return s
    return s.encode("utf-8", errors="surrogatepass").decode("utf-8", errors="replace")


def extract_pdf_pages(pdf_path: Path, max_pages: int = 0) -> tuple[list[str], int, str]:
    """按页提取 PDF，按 PyMuPDF -> pdfplumber -> PyPDF2 顺序回退。"""
    errors = []

    try:
        import fitz

        document = fitz.open(pdf_path)
        total = document.page_count
        count = min(max_pages, total) if max_pages > 0 else total
        pages = [_sanitize_surrogates(document.load_page(i).get_text("text") or "") for i in range(count)]
        document.close()
        if any(page.strip() for page in pages):
            return pages, total, "pymupdf"
        errors.append("pymupdf: empty text")
    except Exception as exc:
        errors.append(f"pymupdf: {exc}")

    try:
        import pdfplumber

        with pdfplumber.open(pdf_path) as document:
            total = len(document.pages)
            count = min(max_pages, total) if max_pages > 0 else total
            pages = [
                _sanitize_surrogates(document.pages[i].extract_text() or "")
                for i in range(count)
            ]
        if any(page.strip() for page in pages):
            return pages, total, "pdfplumber"
        errors.append("pdfplumber: empty text")
    except Exception as exc:
        errors.append(f"pdfplumber: {exc}")

    try:
        import PyPDF2

        with pdf_path.open("rb") as file_handle:
            reader = PyPDF2.PdfReader(file_handle)
            total = len(reader.pages)
            count = min(max_pages, total) if max_pages > 0 else total
            pages = [
                _sanitize_surrogates(reader.pages[i].extract_text() or "")
                for i in range(count)
            ]
        if any(page.strip() for page in pages):
            return pages, total, "pypdf2"
        errors.append("pypdf2: empty text")
    except Exception as exc:
        errors.append(f"pypdf2: {exc}")

    raise RuntimeError("; ".join(errors))


def format_pages(pages: list[str], first_page: int = 1) -> str:
    return "\n\n".join(
        f"[PAGE {first_page + index}]\n{page.strip()}"
        for index, page in enumerate(pages)
    )


def chunk_pages(pages: list[str], max_chars: int) -> list[str]:
    """按页边界分块；单页超限时保留整页，绝不丢文本。"""
    chunks: list[str] = []
    current_pages: list[str] = []
    current_chars = 0
    for index, page in enumerate(pages, 1):
        raw_size = len(page)
        if current_pages and current_chars + raw_size > max_chars:
            first_page = index - len(current_pages)
            chunks.append(format_pages(current_pages, first_page))
            current_pages = []
            current_chars = 0
        current_pages.append(page)
        current_chars += raw_size
    if current_pages:
        first_page = len(pages) - len(current_pages) + 1
        chunks.append(format_pages(current_pages, first_page))
    return chunks


def _parse_cached_pages(text: str) -> list[str]:
    matches = list(re.finditer(r"^\[PAGE (\d+)\]\n", text, re.MULTILINE))
    pages = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        pages.append(text[start:end].strip())
    return pages


def get_cached_pages(
    pdf_path: Path,
    cache_dir: Path,
    max_pages: int,
    force_extract: bool,
) -> tuple[list[str], int, int, bool, str]:
    """只复用带完整性元数据的新缓存；旧的截断缓存自动重建。"""
    cache_path = cache_dir / f"{pdf_path.stem}.txt"
    if cache_path.exists() and not force_extract:
        try:
            text = cache_path.read_text(encoding="utf-8", errors="replace")
            m = re.search(r"^# pages_extracted: (\d+)/(\d+)", text, re.MULTILINE)
            engine_match = re.search(r"^# extraction_engine: (.+)$", text, re.MULTILINE)
            complete = re.search(r"^# extraction_complete: (true|false)$", text, re.MULTILINE)
            pages = _parse_cached_pages(text)
            if m and complete and pages:
                extracted = int(m.group(1))
                total = int(m.group(2))
                requested = min(max_pages, total) if max_pages > 0 else total
                if extracted == requested:
                    engine = engine_match.group(1).strip() if engine_match else "unknown"
                    return pages, extracted, total, True, engine
        except Exception:
            pass

    pages, total, engine = extract_pdf_pages(pdf_path, max_pages)
    extracted = len(pages)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_content = (
        f"# pages_extracted: {extracted}/{total}\n"
        f"# extraction_complete: {'true' if extracted == total else 'false'}\n"
        f"# extraction_engine: {engine}\n"
        f"# source: {pdf_path.name}\n\n"
        f"{format_pages(pages)}"
    )
    cache_path.write_text(cache_content, encoding="utf-8")
    return pages, extracted, total, False, engine


def assess_extraction_quality(text: str, n_pages: int, total_pages: int) -> tuple[str, str]:
    """评估 PDF 提取质量, 返回 (confidence, reason)."""
    if not text or text.startswith("提取失败"):
        return ("low", "PDF 文本提取失败")
    if len(text) < 500:
        return ("low", f"PDF 文本太短 ({len(text)} 字符), 可能是扫描件")
    # 算 提取字符/页
    chars_per_page = len(text) / max(n_pages, 1)
    if chars_per_page < 100:
        return ("low", f"每页提取字符 < 100 ({chars_per_page:.0f}/页), 可能是图片型 PDF")
    if chars_per_page < 500:
        return ("medium", f"每页提取字符 {chars_per_page:.0f}/页, 内容可能不完整")
    # 检查 garbled 比例: 非 ASCII 字母 / 总字母
    alpha = sum(1 for c in text if c.isalpha() and ord(c) < 128)
    cn = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
    if alpha + cn < len(text) * 0.3:
        return ("medium", f"文本乱码比例高, 可读字符占比低")
    return ("medium", f"PDF 文本可读 ({chars_per_page:.0f} 字符/页), 尚未人工核验")


# ============== LLM 接入 ==============

SYSTEM_PROMPT = """你是一名严谨的学术论文精读助手。你的任务是: 读给定的 PDF 提取文本, 写一份**可直接阅读**的完整精读笔记。

严格规则:
  1. 只基于提供的 PDF 文本内容, 不编造, 不凭印象, 不引用你训练数据里的"已知论文内容"
  2. 找不到的信息明确写 "PDF 文本中未明确说明" 或 "PDF 文本中未找到", 绝不编造
  3. 数字必须从文本里抄, 不创造数字
  4. 章节标题用中文, 内容用中文
  5. 输出必须是 Markdown 格式, 12 个 H2 section, 顺序固定
  6. 引用页码用 p.X 格式
  7. 方法、实验数字、结论和局限等事实必须就近标注真实页码；最终笔记至少包含 3 个 p.X 引用
"""


USER_PROMPT_TEMPLATE = """请基于以下 PDF 提取文本, 写一篇**完整、可直接阅读**的论文精读笔记。

【论文信息】
- 文件名: {pdf_name}
- primary_topic: {primary_topic}
- topics: {topics}

【PDF 提取文本】({n_pages} 页 / 共 {total_pages} 页):
```
{pdf_text}
```

【输出要求】严格按以下 12 个 H2 章节顺序, 每节都要充实写, 不写"待补充"或空话:

# 论文精读

## 1. 论文定位
说明这篇论文属于什么方向, 解决什么问题, 适合放在哪个主题下。

## 2. 一句话总结
用一句话讲清楚这篇论文的核心思想。

## 3. 背景与问题
- 这篇论文为什么要做
- 之前方法有什么问题
- 作者想解决的核心矛盾是什么

## 4. 核心贡献
列出 3-6 条具体贡献. 不要写空话 (如"提出了一个有效方法"), 要写清楚到底提出了什么模块/机制/框架/训练策略/实验发现。

## 5. 方法详解
最重要, 必须写详细, 包括:
- 整体框架
- 输入输出
- 关键模块
- 模块之间怎么连接
- 数学公式或机制的直观解释
- 训练方式
- 推理流程
- 和已有方法的差异
- 论文类型特化:
  * 注意力类: 注意力作用维度 (通道/空间/频域/多尺度/局部全局), 可插入网络, 计算量 vs 效果
  * 检测类: backbone/neck/head, anchor/query/transformer/FPN, 小目标/旋转框/遥感/无人机等
  * 医学类: 任务类型, 图像模态, 数据集, 分割/分类/配准/生成流程, 临床意义
  * 3D 类: 点云/NeRF/SLAM/重建/配准任务, 数据表达, 几何约束, 网络结构, 评价指标

## 6. 实验与结果
整理:
- 使用的数据集
- 对比方法
- 评价指标
- 主实验结果 (有具体数字保留关键数字, 不编造)
- 消融实验
- 泛化实验
- 速度/参数量/FLOPs 等效率信息

## 7. 这篇论文真正有价值的地方
用自己的话总结这篇论文最值得学的点. 重点讲它对后续做研究/改模型/写论文/做实验的启发。

## 8. 局限与问题
分析: 方法不适合什么场景, 实验是否充分, 数据集是否有限, 计算成本, 假设依赖, 复现风险。

## 9. 我该怎么使用这篇论文
- 如果快速了解, 只读哪些部分
- 如果复现, 重点看哪些
- 如果借鉴创新点, 应该学什么
- 如果写 related work, 可放在哪一类

## 10. 和其他论文的关系
根据库里的主题和文件名, 判断可能相关的论文, 用 `[[双链]]` 写法. 如果不确定, 少写, 不要乱连。

## 11. 关键词
5-12 个关键词。

## 12. 可信度说明
说明这篇笔记主要基于 PDF 哪些部分生成, 提取质量如何。

【输出格式】
- 只输出 markdown 内容, 不要前言后语
- 章节标题从 "# 论文精读" 开始
- 不要重复 "## X. 标题" 的提示文字, 直接写该节内容
- 找不到的信息明确标注
"""


CHUNK_PROMPT_TEMPLATE = """你正在分段阅读论文 `{pdf_name}`。
这是第 {chunk_index}/{chunk_count} 个全文分块，页码已用 [PAGE X] 标记。

请只依据本分块，输出供最终综合使用的“证据摘要”，必须保留页码：
1. 本段涉及的章节和研究问题
2. 方法、公式、模块、训练或推理细节
3. 数据集、指标、对比方法、实验数字、消融结果
4. 局限、讨论、结论
5. 可直接引用到精读笔记的关键事实

没有出现的内容不要猜。输出 Markdown，不要写完整 12 节笔记。

【分块原文】
```
{chunk_text}
```
"""


def _request_llm(messages: list[dict[str, str]], max_tokens: int) -> Optional[str]:
    """调用已配置的模型，只返回最终 content。"""
    ollama_url = os.environ.get("OLLAMA_BASE_URL")
    ollama_model = os.environ.get("OLLAMA_MODEL", "qwen2.5:7b")
    openai_key = os.environ.get("OPENAI_API_KEY")
    openai_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
    openai_model = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")

    if ollama_url:
        try:
            import requests
            r = requests.post(
                f"{ollama_url}/api/chat",
                json={
                    "model": ollama_model,
                    "messages": messages,
                    "stream": False,
                    "options": {"temperature": LLM_TEMPERATURE, "num_predict": max_tokens},
                },
                timeout=LLM_TIMEOUT,
            )
            if r.status_code == 200:
                return (r.json()["message"].get("content") or "").strip() or None
            print(f"  [warn] Ollama HTTP {r.status_code}: {r.text[:200]}", file=sys.stderr)
        except Exception as e:
            print(f"  [warn] Ollama 调用失败: {e}", file=sys.stderr)

    if openai_key:
        try:
            import requests
            r = requests.post(
                f"{openai_url}/chat/completions",
                headers={"Authorization": f"Bearer {openai_key}"},
                json={
                    "model": openai_model,
                    "messages": messages,
                    "temperature": LLM_TEMPERATURE,
                    "max_tokens": max_tokens,
                },
                timeout=LLM_TIMEOUT,
            )
            if r.status_code == 200:
                message = r.json()["choices"][0]["message"]
                return (message.get("content") or "").strip() or None
            print(f"  [warn] OpenAI HTTP {r.status_code}: {r.text[:200]}", file=sys.stderr)
        except Exception as e:
            print(f"  [warn] OpenAI 调用失败: {e}", file=sys.stderr)

    return None


def call_llm(
    pages: list[str],
    pdf_name: str,
    primary_topic: str,
    topics: list[str],
    n_pages: int,
    total_pages: int,
    chunk_chars: int,
) -> Optional[str]:
    """全文较短时直接综合；较长时先逐块提证据，再生成最终 12 节笔记。"""
    chunks = chunk_pages(pages, chunk_chars)
    topics_str = ", ".join(topics) if topics else "无"

    if len(chunks) == 1:
        source_text = chunks[0]
    else:
        summaries = []
        for index, chunk in enumerate(chunks, 1):
            print(
                f"\n    [chunk {index}/{len(chunks)}] {len(chunk)} chars ...",
                end=" ",
                flush=True,
            )
            prompt = CHUNK_PROMPT_TEMPLATE.format(
                pdf_name=pdf_name,
                chunk_index=index,
                chunk_count=len(chunks),
                chunk_text=chunk,
            )
            summary = _request_llm(
                [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=2200,
            )
            if not summary:
                print("failed", flush=True)
                print(
                    f"  [error] 分块 {index}/{len(chunks)} 证据摘要失败",
                    file=sys.stderr,
                )
                return None
            print("ok", flush=True)
            summaries.append(f"### 分块 {index}/{len(chunks)}\n{summary}")
        source_text = (
            "以下是覆盖全文各页的分块证据摘要。页码来自原 PDF；"
            "最终笔记只能使用摘要中明确出现的事实。\n\n"
            + "\n\n".join(summaries)
        )

    user_prompt = USER_PROMPT_TEMPLATE.format(
        pdf_name=pdf_name,
        primary_topic=primary_topic,
        topics=topics_str,
        n_pages=n_pages,
        total_pages=total_pages,
        pdf_text=source_text,
    )
    if len(chunks) > 1:
        print("    [synthesis] 12-section note ...", end=" ", flush=True)
    result = _request_llm(
        [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=LLM_MAX_TOKENS,
    )
    if len(chunks) > 1:
        print("ok" if result else "failed", flush=True)
    return result


def validate_ai_note(note: str) -> list[str]:
    """写盘前硬校验结构，阻止模板或残缺输出进入知识库。"""
    errors = []
    for section_number in range(1, 13):
        if not re.search(rf"^##\s+{section_number}\.\s+", note, re.MULTILINE):
            errors.append(f"缺少章节 {section_number}")
    for forbidden in ("无 LLM 模式", "待深入阅读后补充"):
        if forbidden in note:
            errors.append(f"包含禁用占位文本: {forbidden}")
    if not note.lstrip().startswith("# 论文精读"):
        errors.append("缺少主标题 # 论文精读")
    page_refs = [
        ref for ref in re.findall(r"\bp\.\s*\d+", note, re.IGNORECASE)
        if ref.lower().replace(" ", "") != "p.x"
    ]
    if len(page_refs) < 3:
        errors.append("真实页码引用少于 3 个")
    return errors


# ============== 无 LLM fallback (写"未找到" + 真实短句) ==============

def build_no_llm_ai_block(stem: str, primary_topic: str, topics: list[str], text: str, today: str,
                          confidence: str, n_pages: int, total_pages: int) -> str:
    """无 LLM 时的"精读"内容: 模板填充 + 真实摘录 + 明确未找到标注."""
    body = f"""# 论文精读 (无 LLM 模式)

> **本节为无 LLM 模式生成, 内容不完整, 仅供引用**。
> 未配 Ollama / OpenAI key, 走"模板填充 + 真实摘录", 找不到的信息全部标"PDF 文本中未找到"。
> 建议配 LLM 后用 `--llm` 重新生成, 质量会高很多。
> 缓存: `.paper-cache/extracts/{stem}.txt` ({n_pages}/{total_pages} 页, PyPDF2 提取, 质量 {confidence})

## 1. 论文定位

- primary_topic: `{primary_topic}`
- topics: {", ".join(f"`{t}`" for t in topics)}
- 实际方向/子方向: PDF 文本中未明确说明 (无 LLM 模式不编造, 建议读 PDF Title/Abstract)

## 2. 一句话总结

PDF 文本中未明确说明 (无 LLM 模式不编造, 建议读 PDF Abstract)

## 3. 背景与问题

PDF 文本中未明确说明 (建议读 PDF Introduction 段)

## 4. 核心贡献

PDF 文本中未明确列出 (建议读 PDF Abstract 末尾 / Introduction 贡献列表)

## 5. 方法详解

PDF 文本中未明确说明 (建议读 PDF Method/Approach 章节)

### 输入 / 输出 / 主体架构 / 关键模块 / 训练方式

- 全部: PDF 文本中未明确说明

## 6. 实验与结果

PDF 文本中未明确说明 (建议读 PDF Experiments 章节 + 表格)

## 7. 这篇论文真正有价值的地方

PDF 文本中未明确说明 (建议读完 PDF 后人工补充)

## 8. 局限与问题

PDF 文本中未明确说明 (建议读 PDF Discussion / Limitations 章节)

## 9. 我该怎么使用这篇论文

- 必读: Abstract + Introduction + Method + Experiments
- 快速了解: 只读 Abstract + Conclusion
- 复现: Method 章节 + 官方代码 (如有)
- 借鉴: 看核心贡献点是否跟你研究相关

## 10. 和其他论文的关系

- primary_topic: `{primary_topic}` 的主题首页: `[[{primary_topic}]]`
- 相关论文 (无 LLM 模式, 仅按主题): 同主题下的其他论文 (见 `[[{primary_topic}]]` 首页)

## 11. 关键词

- (无 LLM 模式不编造, 建议读 PDF Keywords 段)

## 12. 可信度说明

- **模式**: 无 LLM (模板填充)
- **PDF 提取质量**: {confidence} ({n_pages}/{total_pages} 页, PyPDF2)
- **缓存**: `.paper-cache/extracts/{stem}.txt`
- **建议**: 配 LLM key (`export OPENAI_API_KEY=...`) 后用 `--llm` 重新生成, 质量大幅提升
"""
    return f"{AI_START_MARKER}\n{body}\n{AI_END_MARKER}"


# ============== 笔记操作 ==============

def parse_frontmatter(md_text: str) -> tuple[dict[str, str], str, str]:
    """解析 YAML frontmatter. 支持多行 list:
       authors:
         - "Alice"
         - "Bob"
       被解析成 {'authors': '["Alice", "Bob"]'} (规范化回单行 JSON 字符串)
    """
    if not md_text.startswith("---"):
        return ({}, "", md_text)
    end = md_text.find("\n---", 3)
    if end < 0:
        return ({}, "", md_text)
    block = md_text[3:end].strip()
    body = md_text[end + 4:].lstrip("\n")
    fm = {}
    # 第一遍: 单行 key: value
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
        key, v = m.group(1), m.group(2)
        # 跟进的缩进行 (YAML list 或 YAML dict 子键)
        i += 1
        sub_items: list[str] = []
        while i < len(lines):
            sub = lines[i]
            # 缩进 (空格或 tab 开头) 的项 = list 项
            if sub.startswith(("  ", "\t", "    ")) and sub.strip().startswith("- "):
                item = sub.strip()[2:].strip()  # 去掉 "- "
                if len(item) >= 2 and item[0] == '"' and item[-1] == '"':
                    item = item[1:-1]
                sub_items.append(item.replace('\\"', '"').replace('\\\\', '\\'))
                i += 1
            else:
                break
        if sub_items:
            # 多行 list -> 规范化成单行 JSON 字符串
            fm[key] = json.dumps(sub_items, ensure_ascii=False)
        else:
            # 单行 value
            if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
                v = v[1:-1]
            elif len(v) >= 2 and v[0] == "'" and v[-1] == "'":
                v = v[1:-1]
            fm[key] = v
    return (fm, block, body)


def has_ai_block(body: str) -> bool:
    return AI_START_MARKER in body and AI_END_MARKER in body


def replace_ai_block(body: str, new_ai_block: str) -> str:
    s = body.find(AI_START_MARKER)
    e = body.find(AI_END_MARKER, s) + len(AI_END_MARKER) if s >= 0 else -1
    if s >= 0 and e > 0:
        return body[:s] + new_ai_block + body[e:]
    sep = "" if body.endswith("\n") else "\n"
    return body + sep + "\n" + new_ai_block + "\n"


def build_generated_body(body: str, ai_block: str, title: str, pdf_name: str) -> str:
    """未人工复核的笔记只保留一个阅读入口，移除旧版机器摘要重复正文。"""
    del body
    return (
        f"# {title}\n\n"
        f"> PDF: [[{pdf_name}]] | 本页为 AI 全文精读，尚未人工复核。\n\n"
        f"{ai_block}\n"
    )


def merge_frontmatter(
    orig_fm: dict[str, str],
    stem: str,
    today: str,
    confidence: str,
    n_pages: int,
    total_pages: int,
    engine: str,
) -> dict[str, str]:
    out = dict(orig_fm)
    out["source_basis"] = "pdf-text"
    out["reading_stage"] = "ai-complete"
    cur_human = orig_fm.get("human_reviewed", "").strip('"').strip("'").lower()
    if cur_human == "true":
        pass  # 保留 status=read
    else:
        out["status"] = "ai-read"
    out["confidence"] = confidence
    out["ai_generated"] = "true"
    out["human_reviewed"] = "false"
    out["ai_generated_at"] = today
    out["extract_cache"] = f".paper-cache/extracts/{stem}.txt"
    out["extraction_complete"] = "true" if n_pages == total_pages else "false"
    out["extracted_pages"] = str(n_pages)
    out["total_pages"] = str(total_pages)
    out["content_coverage"] = "full" if n_pages == total_pages else "partial"
    out["extraction_engine"] = engine
    out["full_text_covered"] = "true" if n_pages == total_pages else "false"
    out["full_text_completed_at"] = today if n_pages == total_pages else ""
    out["full_text_completion_basis"] = (
        "full-document chunked LLM synthesis"
        if n_pages == total_pages
        else f"partial extraction {n_pages}/{total_pages} pages"
    )
    if "metadata_verified" not in out:
        out["metadata_verified"] = "false"
    return out


# 字段: 必须是标准 YAML list, 不是 JSON 字符串
LIST_FM_FIELDS = {"authors", "topics", "tags"}


def _normalize_escapes(s: str) -> str:
    """把累积的多重 backslash escape 折半.
    历史 bug: 旧版 write_frontmatter + parse_list_value 错误交互, 每次写会
    把 \ 翻倍一次. 多次累积后产生 200+ backslash.
    本函数把所有连续 \\\\.+  折半, 直至最多 1 个 \\  (因为正常 YAML 字面 \\ 就代表 1 个 \\)
    同时把 \\\"  -> "  (JSON 风格 quote 还原).
    """
    # 1. 还原 \", \\, \n, \t 等 JSON escape
    out = []
    i = 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s):
            nxt = s[i + 1]
            if nxt in ('"', "\\", "n", "t", "r"):
                # JSON-style escape -> 字面字符
                if nxt == "n":
                    out.append("\n")
                elif nxt == "t":
                    out.append("\t")
                elif nxt == "r":
                    out.append("\r")
                else:
                    out.append(nxt)
                i += 2
                continue
        out.append(s[i])
        i += 1
    s = "".join(out)
    # 2. 把剩余的连续 \ 全部去掉 (处理累积: \\\\.+  ->  )
    s = re.sub(r"\\+", "", s)
    return s


def _parse_list_value(s: str) -> Optional[list[str]]:
    """从 '["a", "b"]' / '[a, b]' / '[]' 字符串解析成 list[str].
    解析失败返回 None (让调用者走普通 string 分支).
    重要: 正确处理 JSON 风格 escape (\"  -> ", \\ -> \\)"""
    s = s.strip()
    if not (s.startswith("[") and s.endswith("]")):
        return None
    inner = s[1:-1].strip()
    if not inner:
        return []
    # 抓所有被引号包起来或裸值 (按 , 切但尊重 quote)
    items: list[str] = []
    i = 0
    while i < len(inner):
        c = inner[i]
        if c in ('"', "'"):
            quote = c
            j = i + 1
            buf = []
            while j < len(inner):
                if inner[j] == "\\" and j + 1 < len(inner):
                    # JSON escape: \" -> ", \\ -> \, \n -> \n 等
                    nxt = inner[j + 1]
                    if nxt == "n":
                        buf.append("\n")
                    elif nxt == "t":
                        buf.append("\t")
                    elif nxt == "r":
                        buf.append("\r")
                    else:
                        buf.append(nxt)  # " ' \ 等保持字面
                    j += 2
                    continue
                if inner[j] == quote:
                    break
                buf.append(inner[j])
                j += 1
            items.append("".join(buf))
            i = j + 1
        elif c == "," or c == " ":
            i += 1
        else:
            # 裸值 (无 quote 包裹), 读到 , 或结尾
            j = i
            while j < len(inner) and inner[j] != ",":
                j += 1
            v = inner[i:j].strip()
            if v:
                items.append(v)
            i = j
    return items


def write_frontmatter(fm: dict[str, str]) -> str:
    """标准 YAML frontmatter. list 字段 (authors/topics/tags) 用 YAML list 格式:
       authors:
         - "xxx"
         - "yyy"
    不用 JSON 字符串嵌套, 不用多层反斜杠转义.
    """
    lines = ["---"]
    for k, v in fm.items():
        s = str(v).strip()
        # 去掉外层单/双引号
        if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
            s = s[1:-1]
        if len(s) >= 2 and s[0] == "'" and s[-1] == "'":
            s = s[1:-1]

        # 试解析 list
        items = _parse_list_value(s) if k in LIST_FM_FIELDS else None

        if items is not None:
            # YAML list 写法: 字段名 + 缩进 - "value"
            if not items:
                lines.append(f"{k}: []")
            else:
                lines.append(f"{k}:")
                for item in items:
                    # 1. normalize 多重 backslash 累积
                    item = _normalize_escapes(item)
                    # 2. strip 两端残留的双引号 (item 可能是 "Lunit Inc." 形式)
                    item = item.strip()
                    if len(item) >= 2 and item[0] == '"' and item[-1] == '"':
                        item = item[1:-1]
                    if len(item) >= 2 and item[0] == "'" and item[-1] == "'":
                        item = item[1:-1]
                    # 3. 再 normalize 一次 (strip 后可能产生新累积)
                    item = _normalize_escapes(item)
                    # 4. 按 YAML 规则 escape
                    item_escaped = item.replace("\\", "\\\\").replace('"', '\\"')
                    lines.append(f'  - "{item_escaped}"')
        else:
            # 普通 string 字段
            s = _normalize_escapes(s)
            # strip 两端残留引号
            s = s.strip()
            if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
                s = s[1:-1]
            if len(s) >= 2 and s[0] == "'" and s[-1] == "'":
                s = s[1:-1]
            s = _normalize_escapes(s)
            needs_quote = any(c in s for c in [":", "#", "&", "*", "{", "}", "|", ">", "!", "%", "@", "`"])
            if needs_quote:
                s_inner = s.replace("\\", "\\\\").replace('"', '\\"')
                s = f'"{s_inner}"'
            lines.append(f"{k}: {s}")
    lines.append("---")
    return "\n".join(lines)


# ============== 主流程 ==============

def process_one(
    pdf: Path, notes_dir: Path, cache_dir: Path,
    max_pages: int, max_chars: int, use_llm: bool, today: str,
    force: bool, force_extract: bool,
) -> tuple[str, str]:
    """处理一篇 PDF. Returns (status, message)."""
    stem = pdf.stem
    md_path = notes_dir / f"{stem}.md"
    if not md_path.exists():
        return ("skipped_no_note", f"笔记不存在: {md_path.name}")

    md_text = md_path.read_text(encoding="utf-8", errors="replace")
    fm_orig, fm_block, body = parse_frontmatter(md_text)

    # 人类保护: human_reviewed=true
    human_reviewed = fm_orig.get("human_reviewed", "").strip('"').strip("'").lower() == "true"
    if human_reviewed:
        return ("skipped_human_read", f"human_reviewed=true, 显式人工已读, 跳过")

    # status=ai-read 且已有 AI 区块, 跳过
    cur_status = fm_orig.get("status", "").strip('"').strip("'")
    if cur_status == "ai-read" and has_ai_block(body) and not force:
        return ("skipped_ai_exists", f"status=ai-read 且已有 AI 区块, 跳过")

    # 提取 + 缓存
    try:
        pages, n_pages, total_pages, from_cache, engine = get_cached_pages(
            pdf, cache_dir, max_pages, force_extract,
        )
    except Exception as exc:
        return ("error", f"PDF 文本提取失败: {exc}")
    text = format_pages(pages)
    if not text.strip():
        return ("error", "PDF 文本提取失败: empty text")

    # 评估提取质量
    confidence, conf_reason = assess_extraction_quality(text, n_pages, total_pages)

    # 拿 primary_topic / topics
    primary = fm_orig.get("primary_topic", "U_未归类").strip('"').strip("'") or "U_未归类"
    topics_raw = fm_orig.get("topics", f"[{primary}]").strip('[]')
    topics = [t.strip().strip('"').strip("'") for t in topics_raw.split(",") if t.strip()]
    if not topics:
        topics = [primary]

    # 构造 AI 区块
    if use_llm:
        llm_out = call_llm(
            pages,
            pdf.name,
            primary,
            topics,
            n_pages,
            total_pages,
            max_chars,
        )
        if llm_out:
            # 提取 LLM 输出: 去除可能的 ```markdown 包裹
            llm_out_clean = llm_out.strip()
            if llm_out_clean.startswith("```markdown"):
                llm_out_clean = re.sub(r"^```markdown\s*\n", "", llm_out_clean)
                llm_out_clean = re.sub(r"\n```\s*$", "", llm_out_clean)
            elif llm_out_clean.startswith("```"):
                llm_out_clean = re.sub(r"^```[a-z]*\s*\n", "", llm_out_clean)
                llm_out_clean = re.sub(r"\n```\s*$", "", llm_out_clean)
            validation_errors = validate_ai_note(llm_out_clean)
            if validation_errors:
                return (
                    "llm_failed",
                    "LLM 输出未通过结构校验: " + "; ".join(validation_errors),
                )
            # 加可信度说明 (即使 LLM 输出了, 也要附加缓存路径和质量信息)
            llm_out_clean = llm_out_clean.rstrip() + (
                f"\n\n---\n\n> **可信度补充**: "
                f"PDF 提取质量 = **{confidence}** ({conf_reason}); "
                f"来源缓存: `.paper-cache/extracts/{stem}.txt` ({n_pages}/{total_pages} 页); "
                f"提取引擎: {engine}; 内容覆盖: {'full' if n_pages == total_pages else 'partial'}; "
                f"生成日期: {today}; "
                f"模式: LLM ({os.environ.get('OPENAI_MODEL', os.environ.get('OLLAMA_MODEL', '?'))})."
            )
            ai_block = f"{AI_START_MARKER}\n{llm_out_clean}\n{AI_END_MARKER}"
            return _write_and_return(
                md_path,
                fm_orig,
                body,
                ai_block,
                today,
                confidence,
                stem,
                n_pages,
                total_pages,
                from_cache,
                engine,
                llm_failed=False,
            )
        else:
            # LLM 失败: 严格不写盘, 不 fallback 到 "无 LLM 模式", 不改 frontmatter.
            # 只返回 llm_failed 状态, 让 main 函数记到 failed_files.
            # (--no-llm 模式走下面 else 分支, 显式 fallback 是允许的)
            print(f"  [error] LLM 调用失败, 跳过 (PDF: {pdf.name})", file=sys.stderr)
            return ("llm_failed", f"LLM 调用失败, 跳过 (extract {n_pages}/{total_pages}p, conf={confidence})")
    else:
        # --no-llm 显式模式, 允许 fallback 模板
        ai_block = build_no_llm_ai_block(stem, primary, topics, text, today, confidence, n_pages, total_pages)
        return _write_and_return(
            md_path,
            fm_orig,
            body,
            ai_block,
            today,
            confidence,
            stem,
            n_pages,
            total_pages,
            from_cache,
            engine,
            llm_failed=False,
        )


def _write_and_return(
    md_path,
    fm_orig,
    body,
    ai_block,
    today,
    confidence,
    stem,
    n_pages,
    total_pages,
    from_cache,
    engine,
    llm_failed,
):
    new_fm = merge_frontmatter(
        fm_orig,
        stem,
        today,
        confidence,
        n_pages,
        total_pages,
        engine,
    )
    new_fm_block = write_frontmatter(new_fm)
    title = fm_orig.get("title", stem).strip('"').strip("'") or stem
    new_body = build_generated_body(body, ai_block, title, f"{stem}.pdf")
    new_md = new_fm_block + "\n\n" + new_body
    md_path.write_text(new_md, encoding="utf-8")
    suffix = " (LLM 失败, fallback 无 LLM 模式)" if llm_failed else ""
    return ("created", f"OK (extract {n_pages}/{total_pages}p {'cached' if from_cache else 'fresh'}, conf={confidence}){suffix}")


def main():
    parser = argparse.ArgumentParser(
        description="为 01-Papers/ 下的每篇 PDF 生成完整 AI 精读笔记 (12 section, LLM 生成)"
    )
    parser.add_argument("--limit", type=int, default=0, help="只处理前 N 篇 (0=全部)")
    parser.add_argument("--offset", type=int, default=0, help="跳过前 N 篇 (从第 N+1 开始)")
    parser.add_argument("--only", nargs="+", default=None, help="只处理指定的 stem 列表")
    parser.add_argument("--force", action="store_true", help="覆盖已有 AI 区块")
    parser.add_argument("--force-extract", action="store_true", help="忽略缓存, 重提取 PDF")
    parser.add_argument("--dry-run", action="store_true", help="只统计, 不写文件")
    parser.add_argument("--max-pages", type=int, default=0, help="最多提取 N 页 (默认 0=全文)")
    parser.add_argument("--max-chars", type=int, default=30000, help="单个 LLM 分块字符上限 (默认 30000)")
    parser.add_argument("--llm", action="store_true", help="调用 LLM (需 OLLAMA_BASE_URL 或 OPENAI_API_KEY)")
    parser.add_argument("--no-llm", action="store_true", help="强制无 LLM 模式")
    parser.add_argument("--papers", type=Path, default=DEFAULT_PAPERS)
    parser.add_argument("--notes", type=Path, default=DEFAULT_NOTES)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    args = parser.parse_args()

    if not args.papers.is_dir():
        sys.exit(f"错误: {args.papers} 不存在")
    if not args.notes.is_dir():
        sys.exit(f"错误: {args.notes} 不存在")

    use_llm = args.llm and not args.no_llm
    today = date.today().isoformat()

    pdfs = sorted(args.papers.glob("*.pdf"))
    if args.only:
        only_set = set(args.only)
        pdfs = [p for p in pdfs if p.stem in only_set]
    elif args.offset > 0 or args.limit > 0:
        pdfs = pdfs[args.offset:]
        if args.limit > 0:
            pdfs = pdfs[:args.limit]

    print(f"待处理: {len(pdfs)} 篇 PDF")
    print(f"  PDF:  {args.papers}")
    print(f"  笔记: {args.notes}")
    print(f"  缓存: {args.cache}")
    print(f"  LLM:  {'开' if use_llm else '关 (无 LLM)'}")
    print(f"  参数: max-pages={args.max_pages}, max-chars={args.max_chars}")
    print(f"  标志: force={args.force}, force-extract={args.force_extract}, offset={args.offset}")
    if use_llm:
        model = os.environ.get("OPENAI_MODEL") or os.environ.get("OLLAMA_MODEL") or "?"
        url = os.environ.get("OPENAI_BASE_URL") or os.environ.get("OLLAMA_BASE_URL") or "?"
        print(f"  LLM:  model={model}, base_url={url}")
    print()

    if args.dry_run:
        for pdf in pdfs:
            md = args.notes / f"{pdf.stem}.md"
            cache = args.cache / f"{pdf.stem}.txt"
            print(f"  {pdf.name}  →  [{'笔记在' if md.exists() else '笔记缺'}] [{'缓存在' if cache.exists() else '缓存缺'}]")
        return

    created = skipped_ai = skipped_human = skipped_no = llm_failed_count = errors = 0
    failed_files = []
    low_confidence_files = []

    for i, pdf in enumerate(pdfs, 1):
        print(f"[{i}/{len(pdfs)}] {pdf.stem} ...", end=" ", flush=True)
        try:
            status, msg = process_one(
                pdf, args.notes, args.cache,
                args.max_pages, args.max_chars, use_llm, today,
                args.force, args.force_extract,
            )
            print(f"[{status}] {msg}")
            if status == "created":
                created += 1
                if "conf=low" in msg:
                    low_confidence_files.append(pdf.name)
                if "LLM 失败" in msg:
                    llm_failed_count += 1
            elif status == "skipped_ai_exists":
                skipped_ai += 1
            elif status == "skipped_human_read":
                skipped_human += 1
            elif status == "skipped_no_note":
                skipped_no += 1
            elif status == "llm_failed":
                # LLM 失败 (按用户硬要求): 不写盘, 不改 frontmatter, 计入失败文件
                llm_failed_count += 1
                failed_files.append(f"{pdf.name} (LLM 失败)")
            elif status == "error":
                errors += 1
                failed_files.append(pdf.name)
        except Exception as e:
            print(f"[error] {e}", flush=True)
            errors += 1
            failed_files.append(f"{pdf.name} ({e})")

    print()
    print("=" * 60)
    print(f"=== 处理报告 ===")
    print(f"总计:        {len(pdfs)} 篇")
    print(f"  created (已生成 AI 精读):  {created}")
    print(f"  llm_failed (LLM 失败, 未写盘):   {llm_failed_count}")
    print(f"  skipped_ai_exists:          {skipped_ai}")
    print(f"  skipped_human_read:         {skipped_human}")
    print(f"  skipped_no_note:            {skipped_no}")
    print(f"  errors (PDF 提取失败等):    {errors}")
    if failed_files:
        print(f"\n失败文件:")
        for f in failed_files:
            print(f"  - {f}")
    if low_confidence_files:
        print(f"\nPDF 提取质量 low 的文件 (建议人工读 PDF 后手写笔记):")
        for f in low_confidence_files:
            print(f"  - {f}")
    # 硬验收 (用户要求): 无 LLM 模式必须是 0, 否则说明又 fallback 了
    no_llm_in_output = any("无 LLM 模式" in line for line in _collect_no_llm_lines(args.notes, pdfs))
    if no_llm_in_output:
        print(f"\n⚠️  警告: 检测到笔记里有 '无 LLM 模式' 标记, 说明又走 fallback 了!")


def _collect_no_llm_lines(notes_dir: Path, pdfs: list[Path]) -> list[str]:
    """扫一遍本批处理的 .md, 收集含 '无 LLM 模式' 的行.
    给 main 处理报告用, 当硬验收."""
    hits = []
    for pdf in pdfs:
        md = notes_dir / f"{pdf.stem}.md"
        if not md.exists():
            continue
        try:
            txt = md.read_text(encoding="utf-8", errors="replace")
            for line in txt.splitlines():
                if "无 LLM 模式" in line:
                    hits.append(line)
        except Exception:
            pass
    return hits


if __name__ == "__main__":
    main()
