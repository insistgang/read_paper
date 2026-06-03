# 📚 论文阅读中心

基于Obsidian构建的个人论文管理和阅读系统，支持PDF阅读、笔记标注、AI辅助等功能。

## 📁 目录结构

```
read_paper/
├── .obsidian/              # Obsidian配置
├── 00-Inbox/              # 收件箱（新论文暂存）
├── 01-Papers/             # 论文 PDF + 笔记 (按主题组织, PDF 与同名 .md 放一起)
├── 02-Notes/              # 阅读笔记和想法
├── 03-Templates/          # 模板文件
├── 04-Attachments/        # 附件 (备用, 目前 PDF 都直接放 01-Papers/)
├── 05-Literature/         # 文献综述
├── 06-Projects/           # 研究项目
├── 07-Archive/            # 归档
└── scripts/               # AI辅助脚本
```

> **PDF 存放约定**：当前所有 PDF 都在 `01-Papers/` 下，笔记同名 `.md` 也放同一目录。
> `04-Attachments/PDFs/` 保留为可选备用目录，如果你想把 PDF 单独集中管理可以把 PDF
> 移过去，然后改 `scripts/paper` 里的 `PDF_DIR` 指向新位置。

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
   - 将PDF文件放入 `01-Papers/`（与笔记同目录）
   - 在 `01-Papers/` 创建同名笔记 `.md`
   - 使用模板 `Paper Template.md`

2. **方法二：使用Zotero（推荐）**
   - 安装Zotero Integration插件
   - 从Zotero自动导入文献

3. **方法三：AI自动生成**
   ```bash
   # 使用AI脚本自动生成笔记
   ./scripts/paper-ai notes paper.pdf -o 01-Papers/paper.md
   ```

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
- PDF文件：与笔记同名

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