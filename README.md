# 论文阅读中心

这是一个精简后的 Obsidian 论文知识库。当前结构只保留正在使用的部分：论文笔记、主题索引、总拆解表、维护脚本、测试与 Obsidian 配置。

> 2026-11-01 起，PDF 原文与 PDF 文本缓存按「精确重复文件去重」批次移出本仓库（副本暂存于系统废纸篓批次 `pdf-exact-duplicates-20261101-211037`，清空废纸篓后不可恢复）；Git 历史中仍可取回曾被跟踪的 50 份 PDF。仓库当前定位为**笔记与索引库**，PDF 原文由本机同步盘或单独副本维护。

## 当前规模

| 项目 | 数量 |
|---|---:|
| PDF 原文 | 0（已按去重清理移出本仓库） |
| Markdown 论文笔记 | 547 |
| AI 精读区块 | 547 |
| 主题索引/仪表盘文件 | 39 |
| PDF 文本缓存 | 0（`.paper-cache/extracts/` 已随 PDF 一并移出） |

## 目录结构

```text
read_paper/
├── 01-Papers/                # PDF 已移出（去重清理），仅留分类索引
│   ├── paper_classification.md
│   └── paper_topics.json
├── 02-Notes/
│   └── Papers/               # 547 篇论文笔记，含 PDF wikilink 指向
├── 03-Literature/            # 主题索引、总览、阅读质量仪表盘
├── scripts/                  # 批处理、同步、校验、生成脚本
├── tests/                    # 脚本回归测试
├── .obsidian/                # Obsidian vault 配置
├── 论文阅读拆解表.md          # 547 篇论文批量拆解总表
├── requirements.txt
└── start.sh
```

已删除的预留目录：`00-Inbox/`、`03-Templates/`、`04-Attachments/`、`06-Projects/`、`07-Archive/`。以后新增论文直接进 `01-Papers/` 和 `02-Notes/Papers/`，不再走预留收件箱。

## 常用入口

- 总览：[03-Literature/论文知识库总览.md](03-Literature/论文知识库总览.md)
- 阅读质量仪表盘：[03-Literature/阅读质量仪表盘.md](03-Literature/阅读质量仪表盘.md)
- 全库三遍 Review 报告：[03-Literature/全库三遍Review报告.md](03-Literature/全库三遍Review报告.md)
- 批量拆解总表：[论文阅读拆解表.md](论文阅读拆解表.md)
- 论文笔记：[02-Notes/Papers](02-Notes/Papers)
- PDF 原文：本仓库已不再保留；见上文去重清理说明

## 日常命令

```bash
# 统计 PDF 和笔记数量
./scripts/paper stats

# 生成阅读质量仪表盘
python3 scripts/generate_dashboard.py

# 生成全库三遍 Review 报告
python3 scripts/audit_knowledge_base.py

# 重新生成主题分类、主题首页和总览
python3 scripts/classify_papers.py
python3 scripts/generate_topic_index.py --force
python3 scripts/generate_overview.py --force

# 重新生成 547 篇论文拆解总表
python3 scripts/generate_reading_breakdown_table.py

# 校验 PDF 与笔记、frontmatter、AI 精读区块
python3 scripts/validate_library.py

# 跑脚本测试
python3 -m unittest discover -s tests
```

## 新增论文

1. 把 PDF 放到 `01-Papers/`（PDF 不进 Git，用同步盘或 Git LFS 跨设备同步）。
2. 生成或补齐同名 Markdown：

```bash
python3 scripts/generate_skeleton_notes.py
```

3. 如果要生成 AI 阅读稿：

```bash
python3 scripts/paper_ai.py notes "01-Papers/example.pdf" -o "02-Notes/Papers/example.md"
```

4. 重新生成索引和仪表盘：

```bash
python3 scripts/classify_papers.py
python3 scripts/generate_topic_index.py --force
python3 scripts/generate_overview.py --force
python3 scripts/generate_dashboard.py
python3 scripts/validate_library.py
```

## 质量口径

当前 547 篇都有 AI 精读区块，但默认仍按“AI 首轮阅读稿”管理。是否算人工精读完成，以笔记中的 `human_reviewed: true`、`status: read/done` 和人工补充内容为准。

重点维护项：

- 补齐 `authors/year/venue` 等元数据。
- 标记或排除 `Z_工具与杂项_figures` 中的补充材料。
- 人工复核高优先级论文，把 `status` 从 `ai-read` 升级为 `read` 或 `done`。
- 修改脚本后运行 `python3 -m unittest discover -s tests`。

## Git 说明

PDF 和 `.paper-cache/` 默认不进入 Git。需要跨设备同步 PDF 时，建议使用本地同步盘或 Git LFS，不要直接把大 PDF 普通提交到 GitHub。
