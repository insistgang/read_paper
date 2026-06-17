import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_ai_reading_notes.py"
SPEC = importlib.util.spec_from_file_location("generate_ai_reading_notes", SCRIPT)
generate_ai_reading_notes = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(generate_ai_reading_notes)


class GenerateAIReadingNotesTests(unittest.TestCase):
    def test_chunk_pages_preserves_page_boundaries_and_all_text(self):
        pages = [
            "A" * 40,
            "B" * 40,
            "C" * 40,
        ]

        chunks = generate_ai_reading_notes.chunk_pages(pages, max_chars=100)

        self.assertEqual(2, len(chunks))
        self.assertIn("[PAGE 1]", chunks[0])
        self.assertIn("[PAGE 2]", chunks[0])
        self.assertIn("[PAGE 3]", chunks[1])
        combined = "\n".join(chunks)
        self.assertIn("A" * 40, combined)
        self.assertIn("B" * 40, combined)
        self.assertIn("C" * 40, combined)

    def test_validate_ai_note_requires_all_twelve_sections(self):
        valid = "# 论文精读\n\n" + "\n\n".join(
            f"## {index}. section\ncontent (p.{index})" for index in range(1, 13)
        )
        missing = valid.replace("## 6. section\ncontent (p.6)\n\n", "")

        self.assertEqual([], generate_ai_reading_notes.validate_ai_note(valid))
        self.assertIn("缺少章节 6", generate_ai_reading_notes.validate_ai_note(missing))

    def test_validate_ai_note_rejects_fallback_markers(self):
        note = "# 论文精读\n\n" + "\n\n".join(
            f"## {index}. section\ncontent (p.{index})" for index in range(1, 13)
        )
        note += "\n\n无 LLM 模式"

        errors = generate_ai_reading_notes.validate_ai_note(note)

        self.assertIn("包含禁用占位文本: 无 LLM 模式", errors)

    def test_validate_ai_note_requires_traceable_page_references(self):
        note = "# 论文精读\n\n" + "\n\n".join(
            f"## {index}. section\ncontent" for index in range(1, 13)
        )

        errors = generate_ai_reading_notes.validate_ai_note(note)

        self.assertIn("真实页码引用少于 3 个", errors)

    def test_human_reviewed_note_is_never_overwritten_even_with_force(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            papers = root / "papers"
            notes = root / "notes"
            cache = root / "cache"
            papers.mkdir()
            notes.mkdir()
            pdf = papers / "sample.pdf"
            pdf.write_bytes(b"%PDF-1.4\n")
            note = notes / "sample.md"
            original = (
                "---\n"
                "title: Sample\n"
                "human_reviewed: true\n"
                "---\n\n"
                "Human content\n"
            )
            note.write_text(original, encoding="utf-8")

            status, _ = generate_ai_reading_notes.process_one(
                pdf,
                notes,
                cache,
                max_pages=0,
                max_chars=1000,
                use_llm=True,
                today="2026-06-09",
                force=True,
                force_extract=True,
            )

            self.assertEqual("skipped_human_read", status)
            self.assertEqual(original, note.read_text(encoding="utf-8"))

    def test_generated_body_contains_only_title_pdf_link_and_ai_block(self):
        old_body = (
            "# Old title\n\n"
            "## 摘要\nOld generated summary\n\n"
            "## 方法\nOld generated method\n"
        )
        ai_block = "<!-- AI_READING_NOTE_START -->\n# 论文精读\n<!-- AI_READING_NOTE_END -->"

        body = generate_ai_reading_notes.build_generated_body(
            old_body,
            ai_block,
            title="New title",
            pdf_name="paper.pdf",
        )

        self.assertIn("# New title", body)
        self.assertIn("[[paper.pdf]]", body)
        self.assertIn(ai_block, body)
        self.assertNotIn("Old generated summary", body)
        self.assertNotIn("Old generated method", body)

    def test_unreviewed_note_does_not_keep_stale_high_confidence(self):
        merged = generate_ai_reading_notes.merge_frontmatter(
            {"confidence": "high", "human_reviewed": "false"},
            stem="paper",
            today="2026-06-09",
            confidence="medium",
            n_pages=10,
            total_pages=10,
            engine="pymupdf",
        )

        self.assertEqual("medium", merged["confidence"])
        self.assertEqual("true", merged["full_text_covered"])
        self.assertEqual(
            "full-document chunked LLM synthesis",
            merged["full_text_completion_basis"],
        )


if __name__ == "__main__":
    unittest.main()
