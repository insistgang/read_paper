import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_reading_breakdown_table.py"
SPEC = importlib.util.spec_from_file_location("generate_reading_breakdown_table", SCRIPT)
generate_reading_breakdown_table = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(generate_reading_breakdown_table)


def sample_note(primary_topic: str = "B_注意力算子模块", document_type: str = "paper") -> str:
    return f"""---
title: Test Paper
authors:
  - Alice
year: 2024
venue: CVPR
pdf: [[paper.pdf]]
primary_topic: {primary_topic}
status: ai-read
reading_stage: ai-complete
confidence: high
source_basis: pdf-text
document_type: {document_type}
tags:
  - paper
---

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于轻量化视觉模型方向，解决资源受限设备上的部署效率问题。

## 2. 一句话总结
本文提出一种轻量模块，在保持精度的同时降低延迟。

## 3. 背景与问题
- **为什么要做**：现有方法参数量大，难以移动端部署。
- **核心矛盾**：精度与延迟之间的权衡。

## 4. 核心贡献
1. 提出轻量模块。

## 5. 方法详解
- **整体框架**：输入图像经过轻量模块和分类头输出预测。

## 6. 实验与结果
- **使用的数据集**：ImageNet-1K 和 COCO。
- **评价指标**：Top-1、AP、Latency。
- **主实验结果**：在更低延迟下达到相近精度。

## 7. 这篇论文真正有价值的地方
1. 模块设计可作为移动端 baseline。

## 8. 局限与问题
移动端硬件覆盖有限。

## 9. 我该怎么使用这篇论文
- **如果借鉴创新点**：复用轻量模块设计。

## 10. 和其他论文的关系
[[MobileNetV4]]

## 11. 关键词
轻量化，移动端

## 12. 可信度说明
基于 PDF 文本生成。
<!-- AI_READING_NOTE_END -->
"""


class GenerateReadingBreakdownTableTests(unittest.TestCase):
    def test_build_row_extracts_core_breakdown_fields(self):
        row = generate_reading_breakdown_table.build_row(
            Path("02-Notes/Papers/Test.md"), sample_note()
        )

        self.assertEqual(row.title, "Test Paper")
        self.assertEqual(row.year, "2024")
        self.assertEqual(row.venue, "CVPR")
        self.assertIn("ImageNet-1K", row.datasets)
        self.assertIn("Top-1", row.metrics)
        self.assertIn("精度与延迟", row.task_problem)
        self.assertEqual(row.relevance, "高")
        self.assertEqual(row.priority, "精读")
        self.assertEqual(row.thesis_chapter, "方法")

    def test_supplementary_documents_are_marked_to_skip(self):
        row = generate_reading_breakdown_table.build_row(
            Path("02-Notes/Papers/Figure.md"),
            sample_note(primary_topic="Z_工具与杂项_figures", document_type="supplementary"),
        )

        self.assertEqual(row.relevance, "低")
        self.assertEqual(row.priority, "跳过")
        self.assertEqual(row.thesis_chapter, "暂存")

    def test_marked_table_replacement_is_idempotent(self):
        rows = [
            generate_reading_breakdown_table.build_row(
                Path("02-Notes/Papers/Test.md"), sample_note()
            )
        ]
        rendered = generate_reading_breakdown_table.render_batch_section(rows, generated_on="2026-06-08")
        template = "# 论文阅读拆解表\n\n旧内容\n"

        first = generate_reading_breakdown_table.upsert_batch_section(template, rendered)
        second = generate_reading_breakdown_table.upsert_batch_section(first, rendered)

        self.assertEqual(first, second)
        self.assertEqual(first.count(generate_reading_breakdown_table.BATCH_START), 1)
        self.assertIn("| 1 | [[Test]] | Test Paper |", first)

    def test_replaces_existing_section_with_escaped_markdown_pipes(self):
        rows = [
            generate_reading_breakdown_table.BreakdownRow(
                index=1,
                stem="Pipe",
                title="A \\| B",
                year="2024",
                venue="CVPR",
                rank="顶会/顶刊",
                direction="B_注意力算子模块",
                task_problem="A \\| B",
                datasets="未明确",
                metrics="未明确",
                code_model_data="未明确",
                relevance="高",
                priority="精读",
                thesis_chapter="方法",
                one_sentence="A \\| B",
                core_method="A \\| B",
                experiment_result="A \\| B",
                borrow="A \\| B",
                next_action="精读/纳入核心文献池",
            )
        ]
        rendered = generate_reading_breakdown_table.render_batch_section(rows, generated_on="2026-06-08")
        template = "# T\n\n" + generate_reading_breakdown_table.BATCH_START + "\nold\n" + generate_reading_breakdown_table.BATCH_END + "\n"

        output = generate_reading_breakdown_table.upsert_batch_section(template, rendered)

        self.assertIn("A \\| B", output)
        self.assertEqual(output.count(generate_reading_breakdown_table.BATCH_START), 1)


if __name__ == "__main__":
    unittest.main()
