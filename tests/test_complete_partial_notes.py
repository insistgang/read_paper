import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "complete_partial_notes.py"
SPEC = importlib.util.spec_from_file_location("complete_partial_notes", SCRIPT)
complete_partial_notes = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(complete_partial_notes)


class CompletePartialNotesTests(unittest.TestCase):
    def test_update_note_keeps_partial_status_and_inserts_supplement(self):
        note = """---
title: Test
status: ai-read
reading_stage: ai-complete
human_reviewed: false
---

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
content

## 12. 可信度说明
> 来源缓存: `.paper-cache/extracts/test.txt` (12/20 页); 模式: LLM.
<!-- AI_READING_NOTE_END -->
"""
        supplement = complete_partial_notes.build_supplement(
            stem="test",
            old_pages=12,
            total_pages=20,
            page_texts=["13 page results", "14 page conclusion"],
            completed_at="2026-06-08",
        )

        updated = complete_partial_notes.update_note_text(note, supplement, 20, "2026-06-08")
        updated_again = complete_partial_notes.update_note_text(updated, supplement, 20, "2026-06-08")

        self.assertIn("reading_stage: ai-partial-supplement", updated)
        self.assertIn("full_text_covered: false", updated)
        self.assertIn("content_coverage: partial", updated)
        self.assertIn("(12/20 页)", updated)
        self.assertIn("## 全文补读记录", updated)
        self.assertEqual(updated_again.count("## 全文补读记录"), 1)


if __name__ == "__main__":
    unittest.main()
