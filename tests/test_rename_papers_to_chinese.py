import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "rename_papers_to_chinese.py"
SPEC = importlib.util.spec_from_file_location("rename_papers_to_chinese", SCRIPT)
rename_papers_to_chinese = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rename_papers_to_chinese
assert SPEC.loader is not None
SPEC.loader.exec_module(rename_papers_to_chinese)


class RenamePapersToChineseTests(unittest.TestCase):
    def test_replace_links_updates_plain_pdf_mentions(self):
        text = "根据文件名 `old-stem.pdf` 和主题判断。"

        output = rename_papers_to_chinese.replace_links(text, {"old-stem": "2024_中文名"})

        self.assertIn("`2024_中文名.pdf`", output)
        self.assertNotIn("old-stem.pdf", output)

    def test_replace_links_does_not_replace_short_stem_inside_long_filename(self):
        text = "当前文件是 `2024_注意力算子模块_MHIASA.pdf`，不是 `SA.pdf`。"

        output = rename_papers_to_chinese.replace_links(text, {"SA": "2019_注意力算子模块_SA"})

        self.assertIn("2024_注意力算子模块_MHIASA.pdf", output)
        self.assertIn("2019_注意力算子模块_SA.pdf", output)


if __name__ == "__main__":
    unittest.main()
