import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync_paper_note_body.py"
SPEC = importlib.util.spec_from_file_location("sync_paper_note_body", SCRIPT)
sync_paper_note_body = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(sync_paper_note_body)


def sample_note() -> str:
    return """---
title: "Actual Paper Title"
authors:
  - Alice
  - Bob
year: 2024
venue: CVPR
doi: 10.1234/test
pdf: [[paper.pdf]]
primary_topic: B_注意力算子模块
status: ai-read
date_added: 2026-06-09
---

# Old File Stem

## 基本信息
- **PDF**: [[paper.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Old File Stem |
| **作者** | 待补充 |
| **发表时间** | 待补充 |
| **刊物/会议** | 待补充 |
| **DOI** | 待补充 |

## 摘要

> （待从PDF提取补充）

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

> （待深入阅读后补充）

## 实验

> （待深入阅读后补充）

## 局限

> （待深入阅读后补充）

## 个人评论

> （待深入阅读后补充）

## 相关论文与链接

> - [[B_注意力算子模块]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文定位为高效视觉模型。

## 2. 一句话总结
本文提出一个轻量模块，用于提升速度和精度。

## 3. 背景与问题
- **为什么要做**：现有方法太慢。
- **核心矛盾**：精度和延迟之间的矛盾。

## 4. 核心贡献
1. 提出轻量模块。

## 5. 方法详解
- **整体框架**：输入图像经过模块后输出预测。

## 6. 实验与结果
- **使用的数据集**：ImageNet。
- **评价指标**：Top-1。
- **主实验结果**：更快且精度相近。

## 7. 这篇论文真正有价值的地方
1. 可作为轻量模块样板。

## 8. 局限与问题
硬件覆盖有限。

## 9. 我该怎么使用这篇论文
- **如果借鉴创新点**：复用模块结构。

## 10. 和其他论文的关系
[[MobileNet]]

## 11. 关键词
轻量模型

## 12. 可信度说明
基于 PDF。
<!-- AI_READING_NOTE_END -->
"""


class SyncPaperNoteBodyTests(unittest.TestCase):
    def test_syncs_heading_table_and_placeholder_sections(self):
        updated, changed = sync_paper_note_body.sync_note_text(sample_note())

        self.assertTrue(changed)
        self.assertIn("# Actual Paper Title", updated)
        self.assertIn("| **作者** | Alice; Bob |", updated)
        self.assertIn("| **发表时间** | 2024 |", updated)
        self.assertIn("| **刊物/会议** | CVPR |", updated)
        self.assertIn("| **DOI** | 10.1234/test |", updated)
        self.assertIn("本文提出一个轻量模块", updated)
        self.assertIn("精度和延迟之间的矛盾", updated)
        self.assertNotIn("待深入阅读后补充", updated.split("<!-- AI_READING_NOTE_START -->", 1)[0])

    def test_does_not_overwrite_manual_section_without_placeholder(self):
        note = sample_note().replace(
            "## 方法\n\n> （待深入阅读后补充）",
            "## 方法\n\n这里是人工写好的方法段落。",
        )

        updated, _changed = sync_paper_note_body.sync_note_text(note)

        self.assertIn("这里是人工写好的方法段落。", updated)
        self.assertNotIn("## 方法\n\n- **整体框架**：输入图像经过模块后输出预测。", updated)

    def test_idempotent_after_sync(self):
        first, changed = sync_paper_note_body.sync_note_text(sample_note())
        second, changed_again = sync_paper_note_body.sync_note_text(first)

        self.assertTrue(changed)
        self.assertFalse(changed_again)
        self.assertEqual(first, second)

    def test_escapes_pipe_values_and_uses_fallback_title(self):
        note = sample_note().replace('title: "Actual Paper Title"', 'title: ""').replace(
            "  - Alice\n  - Bob",
            '  - "Alice | Lab"\n  - Bob',
        )

        updated, changed = sync_paper_note_body.sync_note_text(note, fallback_title="fallback_stem")
        updated_again, changed_again = sync_paper_note_body.sync_note_text(
            updated, fallback_title="fallback_stem"
        )

        self.assertTrue(changed)
        self.assertFalse(changed_again)
        self.assertIn("# fallback_stem", updated)
        self.assertIn("| **作者** | Alice \\| Lab; Bob |", updated)
        self.assertEqual(updated, updated_again)


if __name__ == "__main__":
    unittest.main()
