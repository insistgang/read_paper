"""generate_library_dashboard 纯函数冒烟测试。"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import generate_library_dashboard as g  # noqa: E402


class TestFrontmatter(unittest.TestCase):
    NOTE = '---\ntitle: "Foo Bar"\nprimary_topic: B_注意力算子模块\n' \
           'topics:\n  - "B_注意力算子模块"\n  - "E_图像复原_超分_去噪_去雨去雾"\n' \
           'year: 2024\nvenue: "CVPR"\nconfidence: high\n---\n\n# Foo Bar\n\n## 摘要\nclean text here\n##\n'

    def setUp(self):
        self.blk = g.fm_block(self.NOTE)

    def test_fm_block_extracts_yaml(self):
        self.assertIn("primary_topic", self.blk)
        self.assertNotIn("# Foo Bar", self.blk)

    def test_scalar_strips_quotes(self):
        self.assertEqual(g.fm_scalar(self.blk, "title"), "Foo Bar")
        self.assertEqual(g.fm_scalar(self.blk, "primary_topic"), "B_注意力算子模块")
        self.assertEqual(g.fm_scalar(self.blk, "missing"), "")

    def test_topics_block_form_with_primary_first(self):
        tops = g.fm_topics(self.blk, "B_注意力算子模块")
        self.assertEqual(tops[0], "B_注意力算子模块")
        self.assertIn("E_图像复原_超分_去噪_去雨去雾", tops)

    def test_topics_inline_form(self):
        blk = 'primary_topic: A1\ntopics: [A1, B, C]'
        self.assertEqual(g.fm_topics(blk, "A1"), ["A1", "B", "C"])

    def test_year_only_four_digits(self):
        self.assertEqual(g.year_of(self.blk), "2024")
        self.assertEqual(g.year_of("year: venue:"), "")
        self.assertEqual(g.year_of("year: "), "")


class TestAbstractGarble(unittest.TestCase):
    def test_clean_abstract(self):
        text = "## 摘要\n这是干净的中文摘要 with normal words.\n## 下一节\n"
        self.assertFalse(g.abstract_garbled(text))

    def test_garbled_abstract(self):
        text = "## 摘要\nDrivenbyimprovedarchitecturesandbetterrepresentation no spaces.\n## x\n"
        self.assertTrue(g.abstract_garbled(text))


class TestHueAndEscape(unittest.TestCase):
    def test_hue_spectrum_endpoints(self):
        order = ["A", "B", "C"]
        self.assertEqual(g.hue_for("A", order), 265.0)
        self.assertEqual(g.hue_for("C", order), 0.0)
        self.assertTrue(0 <= g.hue_for("B", order) <= 265)

    def test_hue_unknown_topic_falls_off_end(self):
        order = ["A", "B"]
        self.assertEqual(g.hue_for("ZZ", order), 0.0)

    def test_esc_html(self):
        self.assertEqual(g.esc_html('a & b <c> "d"'),
                         "a &amp; b &lt;c&gt; &quot;d&quot;")


if __name__ == "__main__":
    unittest.main()
