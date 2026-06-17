import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_knowledge_base.py"
SPEC = importlib.util.spec_from_file_location("audit_knowledge_base", SCRIPT)
audit_knowledge_base = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(audit_knowledge_base)


def note_text(**overrides: str) -> str:
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
        "date_added": "2026-06-09",
        "tags": "[paper]",
        "human_reviewed": "false",
    }
    values.update(overrides)
    lines = ["---"]
    lines.extend(f"{key}: {value}" for key, value in values.items())
    lines.append("---")
    return "\n".join(lines)


def ai_block() -> str:
    sections = "\n".join(f"## {number}. Section {number}\ncontent" for number in range(1, 13))
    return (
        "<!-- AI_READING_NOTE_START -->\n"
        f"{sections}\n"
        "> 来源缓存: `.paper-cache/extracts/paper.txt` (10/10 页); 模式: LLM (test).\n"
        "<!-- AI_READING_NOTE_END -->\n"
    )


class AuditKnowledgeBaseTests(unittest.TestCase):
    def test_collect_audit_tracks_three_review_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "01-Papers").mkdir(parents=True)
            (root / "02-Notes" / "Papers").mkdir(parents=True)
            (root / ".paper-cache" / "extracts").mkdir(parents=True)
            (root / "03-Literature").mkdir(parents=True)

            (root / "01-Papers" / "paper.pdf").write_bytes(b"%PDF-test")
            (root / "02-Notes" / "Papers" / "paper.md").write_text(
                note_text()
                + "\n\n"
                + "# Test Paper\n\n"
                + "## 摘要\n\n有摘要。\n"
                + ai_block(),
                encoding="utf-8",
            )
            (root / "论文阅读拆解表.md").write_text(
                "<!-- BATCH_READING_BREAKDOWN_START -->\n"
                "| 序号 | 论文 |\n"
                "|---|---|\n"
                "| 1 | [[paper]] |\n"
                "<!-- BATCH_READING_BREAKDOWN_END -->\n",
                encoding="utf-8",
            )

            result = audit_knowledge_base.collect_audit(root)
            report = audit_knowledge_base.render_report(result, limit=10)

        self.assertEqual(result.pdf_count, 1)
        self.assertEqual(result.note_count, 1)
        self.assertEqual(result.breakdown_rows, 1)
        self.assertTrue(any(issue.code == "cache_missing" for issue in result.issues))
        self.assertTrue(any(issue.code == "visible_section_missing" for issue in result.issues))
        self.assertTrue(any(issue.code == "metadata_blank" for issue in result.issues))
        self.assertIn("第一遍", report)
        self.assertIn("第二遍", report)
        self.assertIn("第三遍", report)

    def test_learning_value_flags_suspicious_author_metadata(self):
        issues = []
        text = note_text(
            authors='["Am Schwarzenberg-Campus 1", "Hamburg", "Germany"]',
            year="2019",
            venue="",
        )
        fm = audit_knowledge_base.parse_frontmatter(text)

        audit_knowledge_base.check_learning_value(Path("paper.md"), text, fm, issues)

        self.assertTrue(
            any(issue.code == "metadata_authors_suspicious" for issue in issues),
            issues,
        )

    def test_learning_value_flags_suspicious_venue_metadata(self):
        issues = []
        text = note_text(
            authors="[Runwei Guan, Ruixiao Zhang]",
            year="2025",
            venue=(
                "Ming Xu2,5, Jeremy Smith2, Eng Gee Lim5, "
                "Senior Member, IEEE, Yutao Yue6,7,1 †, Hui Xiong6, Fellow, IEEE"
            ),
        )
        fm = audit_knowledge_base.parse_frontmatter(text)

        audit_knowledge_base.check_learning_value(Path("paper.md"), text, fm, issues)

        self.assertTrue(
            any(issue.code == "metadata_venue_suspicious" for issue in issues),
            issues,
        )

    def test_learning_value_flags_affiliation_as_venue_metadata(self):
        issues = []
        text = note_text(
            authors="[Hang Guo, Jinmin Li]",
            year="2024",
            venue="2 College of Computer Science and Software Engineering, Shenzhen University",
        )
        fm = audit_knowledge_base.parse_frontmatter(text)

        audit_knowledge_base.check_learning_value(Path("paper.md"), text, fm, issues)

        self.assertTrue(
            any(issue.code == "metadata_venue_suspicious" for issue in issues),
            issues,
        )

    def test_asset_pass_flags_cache_nul_characters(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "01-Papers").mkdir(parents=True)
            (root / "02-Notes" / "Papers").mkdir(parents=True)
            (root / ".paper-cache" / "extracts").mkdir(parents=True)
            (root / "03-Literature").mkdir(parents=True)

            pdf = root / "01-Papers" / "paper.pdf"
            note = root / "02-Notes" / "Papers" / "paper.md"
            cache = root / ".paper-cache" / "extracts" / "paper.txt"
            pdf.write_bytes(b"%PDF-test")
            note.write_text(note_text() + "\n\n" + ai_block(), encoding="utf-8")
            cache.write_text("hello\x00world", encoding="utf-8")

            result = audit_knowledge_base.collect_audit(root)

        self.assertTrue(
            any(issue.code == "cache_nul_character" for issue in result.issues),
            result.issues,
        )


if __name__ == "__main__":
    unittest.main()
