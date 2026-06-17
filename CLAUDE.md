# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 这是什么仓库

一个 Obsidian 论文知识库（约 547 篇论文），不是常规软件项目。内容主体是 Markdown 笔记和 PDF，`scripts/` 下的 Python 脚本负责生成、同步和校验。仓库工作语言是中文，新增文档、提交信息延续中文风格。

## 常用命令

```bash
# 跑全部脚本测试（标准库 unittest，无需额外依赖）
python3 -m unittest discover -s tests

# 跑单个测试文件 / 单个用例
python3 -m unittest tests.test_validate_library
python3 -m unittest tests.test_validate_library.SomeTestCase.test_something

# 校验整个库（孤立 PDF/笔记、frontmatter 字段、PDF md5 重复）
# 退出码: 0 正常, 1 有 warning, 2 有 error, 3 参数错误
python3 scripts/validate_library.py

# 统计 / 仪表盘 / 三遍 Review 报告
./scripts/paper stats
python3 scripts/generate_dashboard.py
python3 scripts/audit_knowledge_base.py
```

新增或改动论文后的完整再生成流水线（顺序固定）：

```bash
python3 scripts/generate_skeleton_notes.py      # 为缺笔记的 PDF 生成骨架
python3 scripts/classify_papers.py              # 主题分类
python3 scripts/generate_topic_index.py --force # 03-Literature/ 主题首页
python3 scripts/generate_overview.py --force    # 论文知识库总览
python3 scripts/generate_dashboard.py           # 阅读质量仪表盘
python3 scripts/validate_library.py             # 最后校验
```

`scripts/paper_ai.py`（及包装脚本 `scripts/paper-ai`）调用 LLM 生成阅读稿，依赖环境变量 `OPENAI_API_KEY`/`OPENAI_BASE_URL` 或本地 `OLLAMA_BASE_URL`。依赖见 `requirements.txt`（PyPDF2、pdfplumber、requests、tiktoken）。

## 核心架构与不变量

**文件名词干（stem）是唯一关联键。** 三处文件靠同名词干一一对应，重命名必须三件套一起改（用 `scripts/rename_papers_to_chinese.py`，它还会同步更新 Obsidian 链接）：

- `01-Papers/<stem>.pdf` — PDF 原文
- `02-Notes/Papers/<stem>.md` — 论文笔记（一篇 PDF 对应一篇）
- `.paper-cache/extracts/<stem>.txt` — PDF 文本提取缓存（不是正式笔记）

**生成产物 vs 手写内容。** 以下文件/区块由脚本生成，不要手工编辑，改了也会被 `--force` 重新覆盖：

- `03-Literature/` 下的主题首页、`论文知识库总览.md`、`阅读质量仪表盘.md`、`全库三遍Review报告.md`
- `01-Papers/paper_classification.md` 和 `paper_topics.json`
- `论文阅读拆解表.md`（由 `generate_reading_breakdown_table.py` 从笔记 frontmatter + AI_READING_NOTE 区块聚合）
- 笔记内的 `AI_READING_NOTE` 区块

笔记正文中的人工补充内容和 frontmatter 的人工字段是 source of truth，脚本设计上都不覆盖已有值（如 `fill_metadata_fields.py` 只补空值，`sync_paper_note_body.py` 不重命名文件）。

**笔记 frontmatter 契约**（`validate_library.py` 强制）：

- 必填（骨架阶段也要求）：`title, pdf, primary_topic, status, date_added, tags`
- 推荐（`source_basis: pdf-text` 时要求）：`authors, year, venue, topics, source_basis, reading_stage, confidence`
- 质量口径：所有笔记默认是"AI 首轮阅读稿"（`ai_generated: true`）；只有 `human_reviewed: true` + `status: read/done` + 人工补充内容才算人工精读完成。脚本绝不把仅追加摘录的笔记标成全文完成（见 `complete_partial_notes.py` 的设计原则）。
- 例外：`示例-*`/`模板-*`/`template-*` 开头的笔记允许没有对应 PDF。

**脚本与测试一一对应。** `tests/test_<script>.py` 对应 `scripts/<script>.py`，改脚本时同步跑对应测试。脚本均为单文件、argparse 风格、只依赖标准库 + requirements.txt。

**目录可被环境变量覆盖**（`scripts/paper` CLI）：`PAPER_PDF_DIR`、`PAPER_NOTES_DIR`。统计时用 `-maxdepth 1` 防嵌套副本混入。
