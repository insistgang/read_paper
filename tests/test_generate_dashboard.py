import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_dashboard.py"
SPEC = importlib.util.spec_from_file_location("generate_dashboard", SCRIPT)
generate_dashboard = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(generate_dashboard)


def note_text(**overrides: str) -> str:
    values = {
        "title": "Test Paper",
        "authors": "[Alice]",
        "year": "2024",
        "venue": "CVPR",
        "pdf": "[[paper.pdf]]",
        "primary_topic": "B_注意力算子模块",
        "topics": "[B_注意力算子模块]",
        "status": "ai-read",
        "reading_stage": "ai-complete",
        "confidence": "high",
        "source_basis": "pdf-text",
        "date_added": "2026-06-06",
        "tags": "[paper]",
    }
    values.update(overrides)
    lines = ["---"]
    lines.extend(f"{key}: {value}" for key, value in values.items())
    lines.append("---")
    return "\n".join(lines)


def ai_block(pages: str = "12/20") -> str:
    return (
        "<!-- AI_READING_NOTE_START -->\n"
        f"> 来源缓存: `.paper-cache/extracts/paper.txt` ({pages} 页); 模式: LLM (test).\n"
        "<!-- AI_READING_NOTE_END -->\n"
    )


class GenerateDashboardTests(unittest.TestCase):
    def test_collect_stats_tracks_quality_work_queue(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "01-Papers"
            notes = root / "02-Notes" / "Papers"
            papers.mkdir(parents=True)
            notes.mkdir(parents=True)

            for stem in ("paper", "failed", "supplement"):
                (papers / f"{stem}.pdf").write_bytes(b"%PDF-test")

            (notes / "paper.md").write_text(
                note_text(authors="[]", venue="") + "\n\n" + ai_block("12/20"),
                encoding="utf-8",
            )
            (notes / "failed.md").write_text(
                note_text(
                    status="extraction_failed",
                    reading_stage="extraction-failed",
                    confidence="low",
                    source_basis="pdf-extraction-failed",
                ),
                encoding="utf-8",
            )
            (notes / "supplement.md").write_text(
                note_text(
                    primary_topic="Z_工具与杂项_figures",
                    topics="[Z_工具与杂项_figures]",
                    document_type="supplementary",
                    status="reference",
                ),
                encoding="utf-8",
            )

            stats = generate_dashboard.collect_stats(root)

        self.assertEqual(stats.pdf_count, 3)
        self.assertEqual(stats.note_count, 3)
        self.assertEqual(stats.status_counts["ai-read"], 1)
        self.assertEqual(stats.status_counts["extraction_failed"], 1)
        self.assertEqual(stats.metadata_blank_counts["authors"], 1)
        self.assertEqual(stats.metadata_blank_counts["venue"], 1)
        self.assertEqual(len(stats.partial_extractions), 1)
        self.assertEqual(stats.partial_extractions[0].coverage, "12/20")
        self.assertEqual(stats.document_type_counts["supplementary"], 1)
        self.assertEqual(len(stats.supplementary_candidates), 1)

    def test_dashboard_renders_next_actions(self):
        stats = generate_dashboard.DashboardStats(
            generated_on="2026-06-08",
            pdf_count=2,
            note_count=2,
        )
        stats.status_counts.update({"ai-read": 1, "extraction_failed": 1})
        stats.metadata_blank_counts.update({"authors": 3})
        stats.partial_extractions.append(generate_dashboard.NoteIssue("paper.md", "12/20"))
        stats.extraction_failed.append(generate_dashboard.NoteIssue("failed.md"))

        content = generate_dashboard.build_dashboard(stats, limit=5)

        self.assertIn("# 阅读质量仪表盘", content)
        self.assertIn("部分页提取", content)
        self.assertIn("元数据缺口", content)
        self.assertIn("提取失败", content)

    def test_supplemented_fulltext_marker_counts_as_full_coverage(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "01-Papers"
            notes = root / "02-Notes" / "Papers"
            papers.mkdir(parents=True)
            notes.mkdir(parents=True)
            (papers / "paper.pdf").write_bytes(b"%PDF-test")
            (notes / "paper.md").write_text(
                note_text()
                + "\n\n"
                + ai_block("20/20 页; 原 AI 主体 12/20 + 全文补读 13-20"),
                encoding="utf-8",
            )

            stats = generate_dashboard.collect_stats(root)

        self.assertEqual(stats.full_extraction_count, 1)
        self.assertEqual(stats.unknown_extraction_count, 0)
        self.assertEqual(len(stats.partial_extractions), 0)


if __name__ == "__main__":
    unittest.main()
