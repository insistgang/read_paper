#!/bin/bash
# 论文阅读中心 - 快速启动脚本

echo "📚 论文阅读中心"
echo "================"
echo ""

# 显示菜单
show_menu() {
    echo "请选择操作："
    echo "1. 打开Obsidian Vault"
    echo "2. 添加新论文（AI生成笔记）"
    echo "3. 批量处理PDF"
    echo "4. 查看论文统计"
    echo "5. 配置AI设置"
    echo "6. 退出"
    echo ""
    read -p "请输入选项 (1-6): " choice
    echo ""
}

# 打开Obsidian
open_vault() {
    echo "正在打开Obsidian..."
    if command -v obsidian &> /dev/null; then
        obsidian .
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        open -a Obsidian .
    else
        echo "请手动打开Obsidian并选择此文件夹作为Vault"
    fi
}

# 添加新论文
add_paper() {
    read -p "请输入PDF文件路径: " pdf_path
    if [ ! -f "$pdf_path" ]; then
        echo "错误: 文件不存在"
        return
    fi

    # 复制 PDF 到论文目录 (跟笔记同目录, 当前约定)
    pdf_name=$(basename "$pdf_path")
    cp "$pdf_path" "01-Papers/$pdf_name"
    echo "PDF已复制到: 01-Papers/$pdf_name"

    # 使用AI生成笔记
    if command -v python3 &> /dev/null; then
        read -p "是否使用AI生成笔记? (y/n): " use_ai
        if [ "$use_ai" = "y" ] || [ "$use_ai" = "Y" ]; then
            echo "正在生成笔记..."
            python3 scripts/paper_ai.py notes "01-Papers/$pdf_name" -o "01-Papers/${pdf_name%.pdf}.md"
            echo "笔记已生成: 01-Papers/${pdf_name%.pdf}.md"
        fi
    fi

    echo "✅ 论文添加完成"
}

# 批量处理
batch_process() {
    read -p "请输入PDF目录路径: " pdf_dir
    if [ ! -d "$pdf_dir" ]; then
        echo "错误: 目录不存在"
        return
    fi
    
    echo "正在批量处理..."
    python3 scripts/paper_ai.py batch "$pdf_dir" -o "01-Papers"
    echo "✅ 批量处理完成"
}

# 查看统计
show_stats() {
    echo "📊 论文统计"
    echo "============"

    # 统计论文数量
    paper_count=$(find 01-Papers -name "*.md" -type f 2>/dev/null | wc -l)
    # 排除嵌套副本 01-Papers/read_paper/ 下的 PDF, 那是云同步事故产物
    pdf_count=$(find 01-Papers -maxdepth 1 -name "*.pdf" -type f 2>/dev/null | wc -l)

    echo "论文笔记: $paper_count 篇"
    echo "PDF文件 (顶层 01-Papers/): $pdf_count 个"
    echo ""

    # 显示最近添加的论文
    echo "📝 最近添加的论文:"
    find 01-Papers -maxdepth 1 -name "*.md" -type f -exec ls -t {} \; 2>/dev/null | head -5 | while read file; do
        echo "  - $(basename "$file" .md)"
    done
}

# 配置AI
configure_ai() {
    echo "🤖 AI配置"
    echo "=========="
    echo ""
    echo "当前配置:"
    echo "  OLLAMA_BASE_URL: ${OLLAMA_BASE_URL:-http://localhost:11434}"
    echo "  OLLAMA_MODEL: ${OLLAMA_MODEL:-qwen2.5:7b}"
    echo ""
    echo "配置步骤:"
    echo "1. 安装Ollama: brew install ollama"
    echo "2. 下载模型: ollama pull qwen2.5:7b"
    echo "3. 启动服务: ollama serve"
    echo ""
    echo "详细说明请查看: scripts/AI配置指南.md"
}

# 主循环
while true; do
    show_menu
    
    case $choice in
        1) open_vault ;;
        2) add_paper ;;
        3) batch_process ;;
        4) show_stats ;;
        5) configure_ai ;;
        6) echo "👋 再见!"; exit 0 ;;
        *) echo "无效选项，请重新选择" ;;
    esac
    
    echo ""
    read -p "按Enter继续..."
    echo ""
done