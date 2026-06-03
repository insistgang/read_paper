# 📚 论文阅读中心

基于Obsidian构建的个人论文管理和阅读系统，支持PDF阅读、笔记标注、AI辅助等功能。

## 🎯 系统定位

**Obsidian 论文库 + 自动化加工脚本 + Git 版本管理** 三件套：

- **Obsidian** 负责阅读、链接、知识网络
- **Markdown frontmatter** 负责结构化数据
- **paper_classification.md** 负责总览
- **scripts/** 负责批处理和一致性检查
- **Git** 负责版本和同步
- **AI** 负责初稿，不负责最终分类和判断

PDF **不**进 Git（默认 `.gitignore` 排除）；如果你长期在 GitHub 同步大文件，请改用 **Git LFS**。
AI 提取的 PDF 原文缓存在 `.paper-cache/`（被 `.gitignore` 排除，不进正式知识库）。

## 📁 目录结构

```
read_paper/
├── .obsidian/              # Obsidian配置
├── .paper-cache/           # AI 临时缓存 (不入 Git, 不入正式知识库)
│   └── extracts/           #   PDF 原文机器提取, 一篇一个 .txt
├── 00-Inbox/               # 收件箱 (新论文临时入口)
├── 01-Papers/              # 论文 PDF 原文 (只放 PDF, 499 份)
│   ├── paper_classification.md    # 分类索引 (机器生成)
│   ├── paper_topics.json          # 主题映射 (机器生成)
│   └── *.pdf                       # 论文 PDF
├── 02-Notes/               # 笔记根目录
│   └── Papers/             #   论文笔记 (一篇论文对应一个 .md, 499 篇)
├── 03-Templates/           # Obsidian 模板
├── 04-Attachments/         # 非论文附件 (图片, 截图, 补充材料)
├── 05-Literature/          # 主题综述 (机器生成首页 + 人工精读)
├── 06-Projects/            # 研究项目
├── 07-Archive/             # 归档
└── scripts/                # 自动化脚本
```

> **目录约定**：
> - `01-Papers/` **只**放 PDF (499 份) + 机器生成的分类索引文件
> - `02-Notes/Papers/` 放所有论文笔记 (499 篇)，每篇对应 `01-Papers/*.pdf` 的同名 stem
> - `05-Literature/` 是主题首页 (`<主题代号>.md`) + `论文知识库总览.md`
> - `.paper-cache/extracts/` 是 AI 提取的 PDF 原文临时缓存，**不进正式知识库**

## 🚀 快速开始

### 1. 安装Obsidian

访问 [obsidian.md](https://obsidian.md) 下载并安装Obsidian。

### 2. 打开Vault

1. 打开Obsidian
2. 选择 "Open folder as vault"
3. 选择 `read_paper` 文件夹

### 3. 安装推荐插件

进入设置 → 第三方插件 → 浏览，安装以下插件：

**必装插件**：
- **Templater** - 高级模板系统
- **PDF++** (或 Annotator) - PDF阅读和标注
- **Dataview** - 数据查询
- **Calendar** - 日历视图

**推荐插件**：
- **Tag Wrangler** - 标签管理
- **Obsidian Git** - 版本控制
- **Admonition** - 美化提示框

详见 `03-Templates/插件推荐.md`

### 4. 配置Templater

1. 设置 → Templater
2. Template folder location: `03-Templates`
3. Trigger Templater on new file creation: ✅
4. Enable folder templates: ✅

## 📖 使用流程

### 添加新论文

1. **方法一：直接添加**
   - 将 PDF 文件放入 `01-Papers/`
   - 在 `02-Notes/Papers/` 创建同名笔记 `.md`
   - 使用模板 `Paper Template.md`

2. **方法二：使用Zotero（推荐）**
   - 安装Zotero Integration插件
   - 从Zotero自动导入文献

3. **方法三：AI自动生成**
   ```bash
   # 使用AI脚本自动生成笔记
   ./scripts/paper-ai notes 01-Papers/paper.pdf -o 02-Notes/Papers/paper.md
   ```

### 论文库健康检查

整理前先跑这个，扫孤立文件、缺 frontmatter、PDF 重复等：

```bash
python3 scripts/validate_library.py            # 默认: 每类 warning 最多 5 条
python3 scripts/validate_library.py --verbose  # 全部 warning
```

退出码: 0 健康 / 1 有 warning / 2 有 error。

### 重新生成主题分类清单

```bash
python3 scripts/classify_papers.py                              # 默认扫 01-Papers/
python3 scripts/classify_papers.py /path/to/papers --out foo.md  # 自定义
```

输出 `01-Papers/paper_classification.md`, 给 Obsidian 当总览页用。

## 🛠 脚本分工

| 脚本 | 职责 |
|------|------|
| `scripts/paper` | 本地 CLI: list / search / stats / new |
| `scripts/paper-ai` / `scripts/paper_ai.py` | PDF 文本提取、AI 摘要、笔记、问答 |
| `scripts/classify_papers.py` | 基于规则分类，输出 `paper_classification.md` |
| `scripts/validate_library.py` | 健康检查：孤立文件 / frontmatter / 重复 / inbox 残留 |
| `start.sh` | 交互菜单，适合日常使用 |

## 📄 论文笔记 frontmatter 约定

`tags` 给 Obsidian 看, `topics` / `primary_topic` 给分类系统看。骨架阶段不读 PDF, 不编造作者/会议; 读完后人工升级。

### 骨架阶段（机器生成, source_basis=filename）

由 `scripts/generate_skeleton_notes.py` 一次性生成 499 篇, 字段:

```yaml
---
title: "论文标题 (从文件名推断)"
pdf: "[[xxx.pdf]]"
primary_topic: B_注意力算子模块      # 由 classify_papers.py 决定
topics: [B_注意力算子模块, ...]      # 多标签, 来自 paper_topics.json
status: unread                       # 还没读
reading_stage: filename-only         # 只看了文件名
confidence: low                      # 推断置信度低
source_basis: filename               # 关键: 告诉 validate 这是骨架
date_added: 2026-06-03
tags: [paper]
---
```

**必填字段** (validate 必检): `title, pdf, primary_topic, status, date_added, tags`
**推荐字段** (仅在 `source_basis: pdf-text` 时必检): `authors, year, venue, topics, source_basis, reading_stage, confidence`

### 精读后（人工升级, source_basis=pdf-text）

读完 PDF 后**人工**改这些字段, validate 会重新要求必填/推荐字段:

```yaml
---
title: "论文标题 (从 PDF 抄)"
authors: [作者1, 作者2]               # 必填 (补上)
year: 2024                            # 必填
venue: CVPR                           # 必填
doi: 10.xxxx/xxxxx                    # 选填
pdf: "[[xxx.pdf]]"
primary_topic: B_注意力算子模块
topics: [B_注意力算子模块, C_目标检测]   # 读完后可以手工调整
status: read                          # 升级
reading_stage: deep-read              # first-pass / skimming / deep-read / done
confidence: high                      # low / medium / high
source_basis: pdf-text                # 关键: 升级这一行, validate 才会要求 authors/year/venue
date_added: 2026-06-03
rating: 4                             # 1-5, 主观
tags: [paper, transformer, segmentation]
---
```

升级 frontmatter 后, 把正文的 `## 关键贡献 / 方法 / 实验 / 局限` 五节也填上, 形成可被 Dataview 检索的知识卡片。

### 阅读和标注

1. **PDF阅读**
   - 在笔记中点击PDF链接打开
   - 使用PDF++进行高亮和批注
   - 标注自动同步到笔记

2. **做笔记**
   - 在论文笔记中记录想法
   - 使用 `[[双链]]` 关联相关论文
   - 添加标签 `#paper` `#主题`

### 管理论文

1. **使用标签**
   - `#paper` - 论文
   - `#unread` / `#reading` / `#read` - 阅读状态
   - `#主题标签` - 研究方向

2. **使用Dataview查询**
   ```dataview
   TABLE year, venue, rating
   FROM #paper
   SORT date_added DESC
   ```

3. **使用看板**
   - 安装Kanban插件
   - 创建论文阅读计划

## 🤖 AI功能

### 配置AI

1. **安装Ollama**（推荐）
   ```bash
   brew install ollama
   ollama pull qwen2.5:7b
   ```

2. **配置环境变量**
   ```bash
   export OLLAMA_BASE_URL="http://localhost:11434"
   export OLLAMA_MODEL="qwen2.5:7b"
   ```

详见 `scripts/AI配置指南.md`

### 使用AI功能

```bash
# 生成论文摘要
./scripts/paper-ai summarize paper.pdf

# 提取关键词
./scripts/paper-ai keywords paper.pdf

# 回答问题
./scripts/paper-ai qa paper.pdf "这篇论文的创新点是什么？"

# 批量处理
./scripts/paper-ai batch ./pdfs
```

## 📝 模板说明

### Paper Template.md

论文笔记主模板，包含：
- 基本信息（标题、作者、年份等）
- 一句话总结
- 研究动机和方法
- 实验结果
- 创新点和局限性
- 个人想法

### Literature Review Template.md

文献综述模板，用于：
- 整理特定主题的论文
- 对比分析不同方法
- 发现研究空白

### Daily Reading Note.md

每日阅读笔记，记录：
- 今日阅读计划
- 阅读收获
- 灵感和想法

### Project Template.md

研究项目模板，管理：
- 研究问题
- 文献基础
- 实验计划
- 进度跟踪

## 💡 最佳实践

### 1. 命名规范

- 论文笔记：`作者年份-关键词.md`
  - 例：`Vaswani2017-Attention.md`
- PDF 文件：与笔记同名 stem，但 PDF 在 `01-Papers/`，笔记在 `02-Notes/Papers/`

### 2. 标签体系

```
#paper              # 所有论文
#unread             # 未读
#reading            # 正在阅读
#read               # 已读
#transformer        # 研究方向
#nlp                # 领域
#attention          # 技术
```

### 3. 链接习惯

- 使用 `[[双链]]` 关联相关论文
- 在笔记中引用其他论文
- 建立知识网络

### 4. 定期回顾

- 每周回顾新增论文
- 每月整理文献综述
- 更新阅读状态

## 🔧 自定义和扩展

### 修改模板

编辑 `03-Templates` 中的模板文件。

### 添加新查询

参考 `03-Templates/Dataview查询示例.md`。

### 扩展AI功能

编辑 `scripts/paper_ai.py` 添加新功能。

## 📚 相关资源

- [Obsidian官方文档](https://help.obsidian.md)
- [Obsidian中文社区](https://forum.obsidian.md/c/chinese/50)
- [Zotero文献管理](https://www.zotero.org)
- [Ollama本地AI](https://ollama.ai)

## 🆘 常见问题

### Q: 如何备份数据？

```bash
# 使用Obsidian Git插件自动备份
# 或手动复制整个文件夹
```

### Q: 如何在多设备间同步？

- 使用Obsidian Sync（付费）
- 使用iCloud/Dropbox同步文件夹
- 使用Git + GitHub

### Q: PDF标注无法同步？

确保：
1. 安装了PDF++或Annotator插件
2. PDF文件在 `01-Papers/` 目录（当前约定）
3. 笔记中正确引用了PDF

### Q: Dataview查询无结果？

检查：
1. 是否正确添加了标签
2. 查询语法是否正确
3. 是否启用了Dataview插件

---

**享受你的论文阅读之旅！** 📖
