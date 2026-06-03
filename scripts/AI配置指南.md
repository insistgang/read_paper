# AI配置指南

## 🚀 快速开始

### 方案一：使用Ollama（推荐）

#### 1. 安装Ollama

```bash
# macOS
brew install ollama

# 或访问 https://ollama.ai 下载安装
```

#### 2. 下载模型

```bash
# 下载Qwen2.5 7B模型（推荐，中文效果好）
ollama pull qwen2.5:7b

# 或其他模型
ollama pull llama3:8b
ollama pull mistral:7b
```

#### 3. 启动Ollama服务

```bash
ollama serve
```

#### 4. 配置环境变量

```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
export OLLAMA_BASE_URL="http://localhost:11434"
export OLLAMA_MODEL="qwen2.5:7b"
```

### 方案二：使用OpenAI API

#### 1. 获取API Key

访问 https://platform.openai.com 获取API Key

#### 2. 配置环境变量

```bash
export OPENAI_API_KEY="your-api-key"
export OPENAI_BASE_URL="https://api.openai.com/v1"  # 或其他兼容API
```

### 方案三：使用其他兼容API

```bash
# DeepSeek
export OPENAI_API_KEY="your-deepseek-key"
export OPENAI_BASE_URL="https://api.deepseek.com/v1"

# 通义千问
export OPENAI_API_KEY="your-qwen-key"
export OPENAI_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"

# 智谱AI
export OPENAI_API_KEY="your-zhipu-key"
export OPENAI_BASE_URL="https://open.bigmodel.cn/api/paas/v4"
```

## 📝 使用方法

### 命令行使用

```bash
# 给脚本添加执行权限
chmod +x scripts/paper-ai

# 生成论文摘要
./scripts/paper-ai summarize paper.pdf

# 提取关键词
./scripts/paper-ai keywords paper.pdf -n 10

# 回答问题
./scripts/paper-ai qa paper.pdf "这篇论文的主要贡献是什么？"

# 生成阅读笔记
./scripts/paper-ai notes paper.pdf -o notes.md

# 批量处理
./scripts/paper-ai batch ./pdfs -o ./01-Papers
```

### Python代码调用

```python
from scripts.paper_ai import *

# 提取文本
text = extract_text_from_pdf_advanced("paper.pdf")

# 生成摘要
summary = summarize_paper(text)
print(summary)

# 提取关键词
keywords = extract_keywords(text)
print(keywords)

# 回答问题
answer = answer_question(text, "方法的创新点是什么？")
print(answer)
```

## 🔧 Obsidian集成

### 使用Templater调用AI

在Obsidian中，你可以使用Templater调用Python脚本：

```javascript
<%*
// 调用AI脚本生成笔记
const pdfPath = tp.file.title + ".pdf";
const command = `python3 scripts/paper_ai.py notes "04-Attachments/PDFs/${pdf_path}"`;
const result = await tp.system.exec(command);
tR += result;
%>
```

### 使用Dataview查询论文

```dataview
TABLE year, venue, rating, status
FROM #paper
SORT date_added DESC
```

```dataview
LIST
FROM #paper AND #unread
SORT file.ctime DESC
```

## 🎯 最佳实践

### 1. 模型选择

- **中文论文**: qwen2.5:7b 或 qwen2.5:14b
- **英文论文**: llama3:8b 或 mistral:7b
- **代码相关**: codellama:7b

### 2. 性能优化

- 使用GPU加速: `OLLAMA_GPU=1`
- 调整上下文长度: `OLLAMA_NUM_CTX=4096`
- 批量处理时使用并行

### 3. 提示词优化

- 明确指定输出格式
- 限制输出长度
- 提供示例

## 🐛 常见问题

### Q: Ollama连接失败

```bash
# 检查Ollama服务是否运行
curl http://localhost:11434

# 重启服务
ollama serve
```

### Q: PDF提取文本失败

```bash
# 安装更多PDF库
pip install PyPDF2 pdfplumber pymupdf
```

### Q: 内存不足

```bash
# 使用更小的模型
ollama pull qwen2.5:3b
```

## 📚 更多资源

- [Ollama文档](https://ollama.ai)
- [LangChain文档](https://python.langchain.com)
- [OpenAI API文档](https://platform.openai.com/docs)