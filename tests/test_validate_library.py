import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_library.py"
SPEC = importlib.util.spec_from_file_location("validate_library", SCRIPT)
validate_library = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validate_library)


def frontmatter(**overrides: str) -> str:
    values = {
        "title": "Test Paper",
        "authors": "[]",
        "year": "",
        "venue": "",
        "pdf": "[[paper.pdf]]",
        "primary_topic": "B_注意力算子模块",
        "topics": "[B_注意力算子模块]",
        "status": "ai-read",
        "reading_stage": "ai-complete",
        "confidence": "high",
        "source_basis": "pdf-text",
        "date_added": "2026-06-06",
        "tags": "[paper]",
        "ai_generated": "true",
        "human_reviewed": "false",
    }
    values.update(overrides)
    lines = ["---"]
    lines.extend(f"{key}: {value}" for key, value in values.items())
    lines.append("---")
    return "\n".join(lines)


def ai_block(pages: str = "12/20") -> str:
    sections = "\n".join(f"## {number}. Section {number}\ncontent" for number in range(1, 13))
    return (
        "<!-- AI_READING_NOTE_START -->\n"
        f"# 论文精读\n{sections}\n"
        f"> 来源缓存: `.paper-cache/extracts/paper.txt` ({pages} 页); 模式: LLM (test).\n"
        "<!-- AI_READING_NOTE_END -->\n"
    )


class ValidateLibraryTests(unittest.TestCase):
    def run_check(self, note_text: str):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "01-Papers"
            notes = root / "02-Notes" / "Papers"
            papers.mkdir(parents=True)
            notes.mkdir(parents=True)
            (papers / "paper.pdf").write_bytes(b"%PDF-test")
            (notes / "paper.md").write_text(note_text, encoding="utf-8")
            return validate_library.check_library(papers, notes)

    def test_ai_read_requires_exact_markers_and_all_sections(self):
        errors, _ = self.run_check(frontmatter() + "\n\n# Test\n")

        self.assertTrue(any("[AI 区块错误]" in error for error in errors))

    def test_partial_extraction_and_blank_metadata_are_warnings(self):
        errors, warnings = self.run_check(frontmatter() + "\n\n" + ai_block("12/20"))

        self.assertEqual(errors, [])
        self.assertTrue(any("[推荐字段为空 - 完整笔记阶段]" in warning for warning in warnings))
        self.assertTrue(any("[AI 提取不完整]" in warning for warning in warnings))

    def test_quoted_pdf_text_source_still_checks_blank_metadata(self):
        note = frontmatter(source_basis='"pdf-text"')
        errors, warnings = self.run_check(note + "\n\n" + ai_block("10/10"))

        self.assertEqual(errors, [])
        self.assertTrue(any("[推荐字段为空 - 完整笔记阶段]" in warning for warning in warnings))

    def test_complete_ai_note_passes_ai_quality_checks(self):
        note = frontmatter(authors="[Alice]", year="2024", venue="CVPR")
        errors, warnings = self.run_check(note + "\n\n" + ai_block("10/10"))

        self.assertEqual(errors, [])
        self.assertFalse(any("[AI " in warning for warning in warnings))

    def test_supplementary_document_does_not_require_bibliographic_metadata(self):
        note = frontmatter(document_type="supplementary")
        errors, warnings = self.run_check(note + "\n\n" + ai_block("10/10"))

        self.assertEqual(errors, [])
        self.assertFalse(any("[推荐字段为空 - 完整笔记阶段]" in warning for warning in warnings))

    def test_supplemented_fulltext_marker_counts_as_complete(self):
        note = frontmatter(authors="[Alice]", year="2024", venue="CVPR")
        errors, warnings = self.run_check(
            note
            + "\n\n"
            + ai_block("20/20 页; 原 AI 主体 12/20 + 全文补读 13-20")
        )

        self.assertEqual(errors, [])
        self.assertFalse(any("[AI 提取不完整]" in warning for warning in warnings))

    def test_multiline_yaml_list_is_not_treated_as_blank(self):
        note = frontmatter(authors="[Alice]", year="2024", venue="CVPR").replace(
            "authors: [Alice]",
            'authors:\n  - "Alice"\n  - "Bob"',
        )
        errors, warnings = self.run_check(note + "\n\n" + ai_block("10/10"))

        self.assertEqual(errors, [])
        self.assertFalse(any("authors" in warning for warning in warnings))

    def test_extraction_failed_state_must_be_consistent(self):
        note = frontmatter(
            status="extraction_failed",
            reading_stage="filename-only",
            confidence="high",
            source_basis="filename",
            ai_generated="false",
        )
        errors, _ = self.run_check(note + "\n\n# Test\n")

        self.assertTrue(any("[提取失败状态错误]" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
