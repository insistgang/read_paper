import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "fill_metadata_fields.py"
SPEC = importlib.util.spec_from_file_location("fill_metadata_fields", SCRIPT)
fill_metadata_fields = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(fill_metadata_fields)


class FillMetadataFieldsTests(unittest.TestCase):
    def test_extracts_arxiv_year_venue_and_authors_from_cached_text(self):
        text = """# pages_extracted: 12/31
# source: 1609.06585v1.pdf

Image Denoising via Multi-scale Nonlinear Diffusion
Models
Wensen Fenga, Peng Qiaob, Xuanyang Xic, Yunjin Chend
aSchool of Automation and Electrical Engineering
Abstract
Body text.
arXiv:1609.06585v1 [cs.CV] 21 Sep 2016
"""

        meta = fill_metadata_fields.infer_metadata(
            stem="1609.06585v1",
            title="1609.06585v1",
            cache_text=text,
        )

        self.assertEqual(meta["year"].value, "2016")
        self.assertEqual(meta["venue"].value, "arXiv")
        self.assertEqual(
            meta["authors"].value,
            ["Wensen Feng", "Peng Qiao", "Xuanyang Xi", "Yunjin Chen"],
        )

    def test_extracts_arxiv_venue_from_embedded_filename_id(self):
        meta = fill_metadata_fields.infer_metadata(
            stem="2023_2307.12248_Bilevel_Peer_Review",
            title="A Bilevel Formalism for the Peer-Reviewing Problem",
            cache_text="",
        )

        self.assertEqual(meta["year"].value, "2023")
        self.assertEqual(meta["venue"].value, "arXiv")

    def test_extracts_arxiv_venue_from_late_cache_marker(self):
        text = "x" * 15000 + " DLKarXiv:1909.12136v1 [cs.CL] 26 Sep 2019"

        meta = fill_metadata_fields.infer_metadata(
            stem="2019_Semantic_Change_and",
            title="Semantic Change and Emerging Tropes",
            cache_text=text,
        )

        self.assertEqual(meta["year"].value, "2019")
        self.assertEqual(meta["venue"].value, "arXiv")

    def test_uses_curated_venue_override_for_verified_local_cache(self):
        meta = fill_metadata_fields.infer_metadata(
            stem="s10462-025-11212-y",
            title="s10462-025-11212-y",
            cache_text="",
        )

        self.assertEqual(meta["venue"].value, "Artificial Intelligence Review")
        self.assertEqual(meta["venue"].source, "curated-cache-venue")

    def test_uses_cjig_filename_hint_for_venue(self):
        meta = fill_metadata_fields.infer_metadata(
            stem="cjig_遥感_高分遥感影像变化检测",
            title="高分遥感影像变化检测",
            cache_text="",
        )

        self.assertEqual(meta["venue"].value, "中国图象图形学报")

    def test_extracts_journal_of_image_and_graphics_venue_from_cache(self):
        meta = fill_metadata_fields.infer_metadata(
            stem="example",
            title="Example",
            cache_text="Citation. Journal of Image and Graphics, 29(10): 2912-2925.",
        )

        self.assertEqual(meta["venue"].value, "中国图象图形学报")

    def test_does_not_treat_generic_machines_as_venue(self):
        meta = fill_metadata_fields.infer_metadata(
            stem="example",
            title="Example",
            cache_text="Botnets consist of compromised machines and can cause threats.",
        )

        self.assertNotIn("venue", meta)

    def test_uses_curated_year_and_author_overrides(self):
        meta = fill_metadata_fields.infer_metadata(
            stem="Attention",
            title="Point MixSwap: Attentional Point Cloud Mixing",
            cache_text="",
        )

        self.assertEqual(meta["year"].value, "2022")
        self.assertEqual(meta["year"].source, "curated-cache-year")
        self.assertEqual(
            meta["authors"].value,
            ["Ardian Umam", "Cheng-Kun Yang", "Yung-Yu Chuang", "Jen-Hui Chuang", "Yen-Yu Lin"],
        )
        self.assertEqual(meta["authors"].source, "curated-cache-authors")

    def test_uses_curated_authors_for_suspicious_metadata_cleanup(self):
        meta = fill_metadata_fields.infer_metadata(
            stem="2010_Detecting_Botnets_Th",
            title="Detecting Botnets Through Log Correlation",
            cache_text="",
        )

        self.assertEqual(meta["authors"].value, ["Yousof Al-Hammadi", "Uwe Aickelin"])
        self.assertEqual(meta["authors"].source, "curated-cache-authors")

    def test_extracts_chinese_author_from_filename_suffix(self):
        meta = fill_metadata_fields.infer_metadata(
            stem="一种针对多分类的网络入侵检测系统模型_杨启成",
            title="一种针对多分类的网络入侵检测系统模型",
            cache_text="",
        )

        self.assertEqual(meta["authors"].value, ["杨启成"])

    def test_extracts_ieee_author_line_with_roles(self):
        authors = fill_metadata_fields.parse_author_line(
            "Bihan Wen, Student Member, IEEE, Yanjun Li, Student Member, IEEE, "
            "and Yoram Bresler, Fellow, IEEE"
        )

        self.assertEqual(authors, ["Bihan Wen", "Yanjun Li", "Yoram Bresler"])

    def test_extracts_uppercase_and_single_author_lines(self):
        self.assertEqual(
            fill_metadata_fields.parse_author_line("ERHAN BAYRAKTAR AND LIFENG LAI"),
            ["Erhan Bayraktar", "Lifeng Lai"],
        )
        self.assertEqual(
            fill_metadata_fields.parse_author_line("Robert M. Hamwey†", allow_single=True),
            ["Robert M. Hamwey"],
        )

    def test_extracts_chinese_author_line_when_separated(self):
        authors = fill_metadata_fields.parse_author_line(
            "包永堂1，武晨曦1，张鹏1*，单彩峰2"
        )

        self.assertEqual(authors, ["包永堂", "武晨曦", "张鹏", "单彩峰"])

    def test_extracts_late_author_line_when_abstract_precedes_title(self):
        text = """# pages_extracted: 6/6
# source: example.pdf

Abstract
Some PDF extraction placed the abstract column first.
Efficient Example Network for Segmentation
Alice Smith, Bob Jones
Department of Computer Science
"""

        meta = fill_metadata_fields.infer_metadata(
            stem="example",
            title="Efficient Example Network for Segmentation",
            cache_text=text,
        )

        self.assertEqual(meta["authors"].value, ["Alice Smith", "Bob Jones"])

    def test_updates_only_blank_frontmatter_fields(self):
        note = """---
title: Test
authors: []
year: 
venue: 
status: ai-read
human_reviewed: false
---

# Body
<!-- AI_READING_NOTE_START -->
body
<!-- AI_READING_NOTE_END -->
"""
        updates = {
            "authors": fill_metadata_fields.InferredValue(["Alice", "Bob"], "test"),
            "year": fill_metadata_fields.InferredValue("2024", "test"),
            "venue": fill_metadata_fields.InferredValue("CVPR", "test"),
        }

        updated, changed = fill_metadata_fields.update_note_frontmatter(note, updates)

        self.assertEqual(changed, ["authors", "year", "venue"])
        self.assertIn('  - "Alice"', updated)
        self.assertIn("year: 2024", updated)
        self.assertIn('venue: "CVPR"', updated)
        self.assertIn("human_reviewed: false", updated)
        self.assertIn("<!-- AI_READING_NOTE_START -->", updated)

    def test_does_not_overwrite_existing_values(self):
        note = """---
title: Test
authors:
  - "Existing Author"
year: 2020
venue: "Existing Venue"
---

body
"""
        updates = {
            "authors": fill_metadata_fields.InferredValue(["Alice"], "test"),
            "year": fill_metadata_fields.InferredValue("2024", "test"),
            "venue": fill_metadata_fields.InferredValue("CVPR", "test"),
        }

        updated, changed = fill_metadata_fields.update_note_frontmatter(note, updates)

        self.assertEqual(changed, [])
        self.assertIn("Existing Author", updated)
        self.assertIn("year: 2020", updated)
        self.assertIn('venue: "Existing Venue"', updated)

    def test_replaces_suspicious_author_values_when_requested(self):
        note = """---
title: Test
authors:
  - "School of Computer Science"
  - "University of Example"
year: 2020
venue: arXiv
---

body
"""
        updates = {
            "authors": fill_metadata_fields.InferredValue(["Alice Smith", "Bob Jones"], "test"),
        }

        updated, changed = fill_metadata_fields.update_note_frontmatter(
            note,
            updates,
            replace_suspicious=True,
        )

        self.assertEqual(changed, ["authors"])
        self.assertIn('  - "Alice Smith"', updated)
        self.assertIn('  - "Bob Jones"', updated)
        self.assertNotIn("University of Example", updated)

    def test_replaces_suspicious_venue_values_when_requested(self):
        note = """---
title: Test
authors:
  - "Alice Smith"
year: 2024
venue: 2 College of Computer Science and Software Engineering, Shenzhen University
---

body
"""
        updates = {
            "venue": fill_metadata_fields.InferredValue("arXiv", "test"),
        }

        updated, changed = fill_metadata_fields.update_note_frontmatter(
            note,
            updates,
            replace_suspicious=True,
        )

        self.assertEqual(changed, ["venue"])
        self.assertIn('venue: "arXiv"', updated)
        self.assertNotIn("Shenzhen University", updated)

    def test_treats_partially_polluted_author_list_as_suspicious(self):
        self.assertTrue(
            fill_metadata_fields.authors_value_is_suspicious(
                '["Yousof Al-Hammadi", "School of Computer Science"]'
            )
        )

    def test_treats_affiliation_venue_as_suspicious(self):
        self.assertTrue(
            fill_metadata_fields.venue_value_is_suspicious(
                "2 College of Computer Science and Software Engineering, Shenzhen University"
            )
        )


if __name__ == "__main__":
    unittest.main()
