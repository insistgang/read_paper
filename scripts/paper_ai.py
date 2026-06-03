#!/usr/bin/env python3
"""
论文阅读中心 - AI辅助脚本
用于论文总结、问答、关键词提取等功能
"""

import os
import json
import argparse
from pathlib import Path
from typing import Optional, List
import re

# ============== 配置 ==============

# OpenAI API配置（可选）
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")

# 本地模型配置（推荐使用Ollama）
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5:7b")

# ============== PDF处理 ==============

def extract_text_from_pdf(pdf_path: str) -> str:
    """从PDF提取文本"""
    try:
        import PyPDF2
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                # page.extract_text() 在某些 PDF (扫描件/无文本层) 上可能返回 None,
                # 之前会直接 None + "\n" 抛 TypeError。这里兜成空串。
                page_text = page.extract_text() or ""
                text += page_text + "\n"
            return text
    except ImportError:
        print("请安装PyPDF2: pip install PyPDF2")
        return ""

def extract_text_from_pdf_advanced(pdf_path: str) -> str:
    """使用pdfplumber提取文本（更好的格式保留）"""
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
    except ImportError:
        print("请安装pdfplumber: pip install pdfplumber")
        return ""

# ============== AI功能 ==============

def call_local_llm(prompt: str, system_prompt: str = "") -> str:
    """调用本地LLM（Ollama）"""
    try:
        import requests
        
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json={
                "model": OLLAMA_MODEL,
                "messages": messages,
                "stream": False
            }
        )
        
        if response.status_code == 200:
            return response.json()["message"]["content"]
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error calling local LLM: {str(e)}"

def call_openai_api(prompt: str, system_prompt: str = "") -> str:
    """调用OpenAI API"""
    try:
        import requests
        
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            f"{OPENAI_BASE_URL}/chat/completions",
            headers=headers,
            json={
                "model": "gpt-3.5-turbo",
                "messages": messages,
                "temperature": 0.7
            }
        )
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error calling OpenAI API: {str(e)}"

def call_llm(prompt: str, system_prompt: str = "") -> str:
    """根据配置调用LLM"""
    if OPENAI_API_KEY:
        return call_openai_api(prompt, system_prompt)
    return call_local_llm(prompt, system_prompt)

# ============== 论文分析功能 ==============

def summarize_paper(text: str, max_length: int = 2000) -> str:
    """生成论文摘要"""
    system_prompt = """你是一个学术论文分析专家。请对以下论文内容进行总结，包括：
1. 研究问题
2. 核心方法
3. 主要贡献
4. 实验结果
5. 局限性

请用中文回答，保持学术严谨性。"""
    
    prompt = f"""请总结以下论文内容（限制在{max_length}字以内）：

{text[:8000]}

请按照上述格式进行总结。"""
    
    return call_llm(prompt, system_prompt)

def extract_keywords(text: str, num_keywords: int = 10) -> List[str]:
    """提取论文关键词"""
    system_prompt = """你是一个学术论文分析专家。请从论文内容中提取最重要的关键词。"""
    
    prompt = f"""请从以下论文内容中提取{num_keywords}个最重要的关键词，用逗号分隔：

{text[:5000]}

只返回关键词列表，不要其他内容。"""
    
    result = call_llm(prompt, system_prompt)
    keywords = [kw.strip() for kw in result.split(",")]
    return keywords[:num_keywords]

def answer_question(text: str, question: str) -> str:
    """基于论文内容回答问题"""
    system_prompt = """你是一个学术论文分析专家。请基于提供的论文内容回答用户的问题。
如果论文中没有相关信息，请明确说明。请用中文回答。"""
    
    prompt = f"""论文内容：
{text[:6000]}

问题：{question}

请基于论文内容回答上述问题。"""
    
    return call_llm(prompt, system_prompt)

def generate_reading_notes(text: str) -> str:
    """生成阅读笔记模板"""
    system_prompt = """你是一个学术论文分析专家。请根据论文内容生成结构化的阅读笔记。"""
    
    prompt = f"""请根据以下论文内容生成阅读笔记，包括：

1. 一句话总结
2. 研究动机（2-3点）
3. 核心方法（3-5点）
4. 关键创新（2-3点）
5. 实验结果要点
6. 局限性
7. 未来工作方向
8. 相关研究方向

论文内容：
{text[:6000]}

请用Markdown格式输出。"""
    
    return call_llm(prompt, system_prompt)

def compare_papers(texts: List[str], titles: List[str]) -> str:
    """比较多篇论文"""
    system_prompt = """你是一个学术论文分析专家。请比较多篇论文的异同点。"""
    
    papers_info = ""
    for i, (title, text) in enumerate(zip(titles, texts)):
        papers_info += f"\n\n论文{i+1}: {title}\n{text[:2000]}"
    
    prompt = f"""请比较多篇论文的异同点，包括：
1. 研究问题的异同
2. 方法的异同
3. 实验设置的异同
4. 结果的对比
5. 各自的优势和局限性

{papers_info}

请用表格和文字结合的方式进行对比分析。"""
    
    return call_llm(prompt, system_prompt)

# ============== Obsidian集成 ==============

def create_paper_note(pdf_path: str, output_dir: str = "01-Papers") -> str:
    """创建论文笔记"""
    # 提取文本
    text = extract_text_from_pdf_advanced(pdf_path)
    if not text:
        text = extract_text_from_pdf(pdf_path)
    
    if not text:
        return "无法提取PDF文本"
    
    # 生成笔记
    notes = generate_reading_notes(text)
    keywords = extract_keywords(text)
    
    # 获取文件名
    pdf_name = Path(pdf_path).stem
    
    # 创建笔记内容
    note_content = f"""---
title: "{pdf_name}"
authors: 
  - 
year: 
venue: 
doi: 
pdf: "[[{pdf_name}.pdf]]"
tags:
  - paper
  - {', '.join(keywords[:5])}
status: unread
date_added: "{Path(pdf_path).stat().st_mtime}"
---

# {pdf_name}

## AI生成的笔记

{notes}

## 关键词

{', '.join(keywords)}

## 原文摘要

{text[:500]}...

---

*此笔记由AI自动生成，请根据需要修改和补充*
"""
    
    return note_content

def batch_process_pdfs(pdf_dir: str, output_dir: str = "01-Papers") -> None:
    """批量处理PDF文件"""
    pdf_dir_path = Path(pdf_dir)
    output_dir_path = Path(output_dir)
    
    if not pdf_dir_path.exists():
        print(f"PDF目录不存在: {pdf_dir}")
        return
    
    output_dir_path.mkdir(parents=True, exist_ok=True)
    
    pdf_files = list(pdf_dir_path.glob("*.pdf"))
    print(f"找到 {len(pdf_files)} 个PDF文件")
    
    for pdf_file in pdf_files:
        print(f"处理: {pdf_file.name}")
        
        # 创建笔记
        note_content = create_paper_note(str(pdf_file))
        
        # 保存笔记
        note_path = output_dir_path / f"{pdf_file.stem}.md"
        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(note_content)
        
        print(f"  -> 笔记已保存: {note_path}")

# ============== 命令行接口 ==============

def main():
    parser = argparse.ArgumentParser(description="论文阅读中心 - AI辅助工具")
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # 总结命令
    summarize_parser = subparsers.add_parser("summarize", help="生成论文摘要")
    summarize_parser.add_argument("pdf", help="PDF文件路径")
    summarize_parser.add_argument("-o", "--output", help="输出文件路径")
    
    # 关键词命令
    keywords_parser = subparsers.add_parser("keywords", help="提取关键词")
    keywords_parser.add_argument("pdf", help="PDF文件路径")
    keywords_parser.add_argument("-n", "--num", type=int, default=10, help="关键词数量")
    
    # 问答命令
    qa_parser = subparsers.add_parser("qa", help="基于论文回答问题")
    qa_parser.add_argument("pdf", help="PDF文件路径")
    qa_parser.add_argument("question", help="问题")
    
    # 笔记命令
    notes_parser = subparsers.add_parser("notes", help="生成阅读笔记")
    notes_parser.add_argument("pdf", help="PDF文件路径")
    notes_parser.add_argument("-o", "--output", help="输出文件路径")
    
    # 批量处理命令
    batch_parser = subparsers.add_parser("batch", help="批量处理PDF")
    batch_parser.add_argument("dir", help="PDF目录")
    batch_parser.add_argument("-o", "--output", default="01-Papers", help="输出目录")
    
    # 比较命令
    compare_parser = subparsers.add_parser("compare", help="比较多篇论文")
    compare_parser.add_argument("pdfs", nargs="+", help="PDF文件路径")
    
    args = parser.parse_args()
    
    if args.command == "summarize":
        text = extract_text_from_pdf_advanced(args.pdf)
        if text:
            summary = summarize_paper(text)
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(summary)
                print(f"摘要已保存到: {args.output}")
            else:
                print(summary)
    
    elif args.command == "keywords":
        text = extract_text_from_pdf_advanced(args.pdf)
        if text:
            keywords = extract_keywords(text, args.num)
            print("关键词:")
            for i, kw in enumerate(keywords, 1):
                print(f"{i}. {kw}")
    
    elif args.command == "qa":
        text = extract_text_from_pdf_advanced(args.pdf)
        if text:
            answer = answer_question(text, args.question)
            print(answer)
    
    elif args.command == "notes":
        # 之前这里只跑 extract_text_from_pdf_advanced(), 提不出文本就什么都不做。
        # 真正的 PyPDF2 fallback 在 create_paper_note() 里, 之前根本走不到。
        # 改成直接调 create_paper_note, 让它内部 pdfplumber -> PyPDF2 兜底都跑一遍。
        output_dir = str(Path(args.output).parent) if args.output else str(Path(args.pdf).parent)
        note_content = create_paper_note(args.pdf, output_dir=output_dir)
        # create_paper_note 提不出文本时会返回错误字符串
        if note_content and not note_content.startswith("无法提取"):
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(note_content)
                print(f"笔记已保存到: {args.output}")
            else:
                print(note_content)
        else:
            print(note_content, file=sys.stderr)
            sys.exit(2)
    
    elif args.command == "batch":
        batch_process_pdfs(args.dir, args.output)
    
    elif args.command == "compare":
        texts = []
        titles = []
        for pdf_path in args.pdfs:
            text = extract_text_from_pdf_advanced(pdf_path)
            if text:
                texts.append(text)
                titles.append(Path(pdf_path).stem)
        
        if texts:
            comparison = compare_papers(texts, titles)
            print(comparison)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()