#!/usr/bin/env python3
"""Generate an aggregate paper reading breakdown table.

The source of truth is the existing Markdown note body:
frontmatter plus the `AI_READING_NOTE` block. This script keeps the
single-paper template intact and appends/replaces a generated batch section.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Optional

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_library import AI_END_MARKER, AI_START_MARKER, frontmatter_scalar, parse_frontmatter


ROOT = SCRIPT_DIR.parent
DEFAULT_NOTES = ROOT / "02-Notes" / "Papers"
DEFAULT_TEMPLATE = ROOT / "论文阅读拆解表.md"
BATCH_START = "<!-- BATCH_READING_BREAKDOWN_START -->"
BATCH_END = "<!-- BATCH_READING_BREAKDOWN_END -->"

CORE_TOPICS = {
    "B_注意力算子模块",
    "C_目标检测_通用与旋转框",
    "C2_目标检测_违建_车辆_船舶_行人",
    "C3_目标检测_红外_可见光融合",
    "F_图像分割_语义_实例_全景",
    "E_图像复原_超分_去噪_去雨去雾",
    "D_3D_点云_分类_分割_配准",
    "D2_3D_重建_神经辐射场_SLAM",
    "I_场景文本_OCR",
    "R1_遥感_高光谱_变化检测",
    "T_遥感_建筑检测",
}

MEDIUM_TOPICS = {
    "A1_医学图像_分割",
    "A1b_医学图像_小样本_综述",
    "A2_医学图像_分类_配准_生成",
    "A3_医学图像_配准_切片_张量_数学",
    "G_视觉基础模型_VLM_LLM",
    "L_数据集_Benchmark",
    "O_物理对抗_安全_鲁棒",
    "P_跨域_域自适应_联邦",
    "Q_自监督_对比学习_主动学习",
    "R_综述_Survey",
    "S_变化检测_ChangeDetection",
}

TOP_VENUE_RE = re.compile(
    r"\b(CVPR|ICCV|ECCV|NeurIPS|NIPS|ICLR|AAAI|IJCAI|ACL|EMNLP|TPAMI|T-PAMI|TIP|TGRS|IJCV)\b",
    re.I,
)
NON_PAPER_RE = re.compile(r"不是一篇典型的学术研究论文|非学术文档|不属于任何类型的学术论文|购物发票|行政管理表格")


@dataclass
class BreakdownRow:
    index: int
    stem: str
    title: str
    year: str
    venue: str
    rank: str
    direction: str
    task_problem: str
    datasets: str
    metrics: str
    code_model_data: str
    relevance: str
    priority: str
    thesis_chapter: str
    one_sentence: str
    core_method: str
    experiment_result: str
    borrow: str
    next_action: str


def _strip_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", text)
    text = re.sub(r"(?m)^\s*>+\s?", "", text)
    text = re.sub(r"(?m)^\s*[-*]\s+", "", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = text.replace("|", "\\|")
    text = re.sub(r"\s+", " ", text)
    return text.strip(" -:：")


def _cell(text: str, limit: int = 120) -> str:
    text = _strip_markdown(text)
    if not text:
        return "未明确"
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def _frontmatter_list(value: str) -> str:
    value = frontmatter_scalar(value)
    if value.startswith("[") and value.endswith("]"):
        return value.strip("[] ")
    return value


def _ai_block(text: str) -> str:
    if AI_START_MARKER not in text or AI_END_MARKER not in text:
        return ""
    return text.split(AI_START_MARKER, 1)[1].split(AI_END_MARKER, 1)[0]


def parse_ai_sections(block: str) -> dict[int, str]:
    matches = list(re.finditer(r"(?m)^##\s+(\d+)\.\s+.*$", block))
    sections: dict[int, str] = {}
    for idx, match in enumerate(matches):
        number = int(match.group(1))
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(block)
        sections[number] = block[start:end].strip()
    return sections


def _extract_labeled(section: str, labels: tuple[str, ...], limit: int = 140) -> str:
    for line in section.splitlines():
        cleaned = line.strip()
        if not cleaned:
            continue
        match = re.match(r"^(?:[-*]\s*)?(?:\*\*)?([^*：:]{2,30})(?:\*\*)?\s*[：:]\s*(.+)$", cleaned)
        if not match:
            continue
        label = match.group(1).strip()
        value = match.group(2).strip()
        if any(key in label for key in labels):
            return _cell(value, limit)
    return ""


def _first_useful_line(section: str, limit: int = 140) -> str:
    for line in section.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line in {"---", "无", "不适用"}:
            continue
        return _cell(line, limit)
    return ""


def _first_numbered_or_bulleted(section: str, limit: int = 140) -> str:
    for line in section.splitlines():
        if re.match(r"^\s*(?:[-*]|\d+[.)、])\s+", line):
            return _cell(line, limit)
    return _first_useful_line(section, limit)


def _rank_from_venue(venue: str) -> str:
    if TOP_VENUE_RE.search(venue or ""):
        return "顶会/顶刊"
    if venue:
        return "待查"
    return "未明确"


def _is_supplementary(fm: dict[str, str], block: str) -> bool:
    document_type = frontmatter_scalar(fm.get("document_type", "paper")) or "paper"
    primary_topic = frontmatter_scalar(fm.get("primary_topic", ""))
    return document_type == "supplementary" or primary_topic == "Z_工具与杂项_figures" or bool(NON_PAPER_RE.search(block))


def _relevance(primary_topic: str, supplementary: bool) -> str:
    if supplementary:
        return "低"
    if primary_topic in CORE_TOPICS:
        return "高"
    if primary_topic in MEDIUM_TOPICS:
        return "中"
    return "中"


def _priority(relevance: str, confidence: str, supplementary: bool) -> str:
    if supplementary or relevance == "低":
        return "跳过"
    if relevance == "高" and confidence in {"high", "medium"}:
        return "精读"
    return "泛读"


def _thesis_chapter(primary_topic: str, priority: str) -> str:
    if priority == "跳过":
        return "暂存"
    if primary_topic in {"B_注意力算子模块", "D_3D_点云_分类_分割_配准", "D2_3D_重建_神经辐射场_SLAM"}:
        return "方法"
    if primary_topic in {"L_数据集_Benchmark", "C2_目标检测_违建_车辆_船舶_行人", "T_遥感_建筑检测"}:
        return "实验"
    if "综述" in primary_topic or primary_topic.startswith("R_"):
        return "绪论/相关工作"
    return "相关工作"


def _code_model_data(block: str) -> str:
    if re.search(r"GitHub|github|源代码|代码|开源|预训练模型|pretrained|source code", block):
        return "提到代码/模型"
    if re.search(r"数据集|dataset|benchmark", block, re.I):
        return "提到数据"
    return "未明确"


def build_row(path: Path, text: str, index: int = 0) -> BreakdownRow:
    fm = parse_frontmatter(text)
    block = _ai_block(text)
    sections = parse_ai_sections(block)

    title = frontmatter_scalar(fm.get("title", "")) or path.stem
    year = frontmatter_scalar(fm.get("year", "")) or "未明确"
    venue = frontmatter_scalar(fm.get("venue", "")) or "未明确"
    primary_topic = frontmatter_scalar(fm.get("primary_topic", "")) or "未归类"
    confidence = frontmatter_scalar(fm.get("confidence", "")) or "low"
    supplementary = _is_supplementary(fm, block)
    relevance = _relevance(primary_topic, supplementary)
    priority = _priority(relevance, confidence, supplementary)

    one_sentence = _first_useful_line(sections.get(2, ""), 150)
    task_problem = (
        _extract_labeled(sections.get(3, ""), ("核心矛盾", "作者想解决"), 140)
        or _extract_labeled(sections.get(3, ""), ("为什么要做",), 140)
        or _first_useful_line(sections.get(1, ""), 140)
    )
    core_method = (
        _extract_labeled(sections.get(5, ""), ("整体框架", "核心思想", "关键模块"), 140)
        or one_sentence
        or _first_useful_line(sections.get(5, ""), 140)
    )
    datasets = _extract_labeled(sections.get(6, ""), ("使用的数据集", "数据集"), 100)
    metrics = _extract_labeled(sections.get(6, ""), ("评价指标", "指标"), 100)
    experiment_result = (
        _extract_labeled(sections.get(6, ""), ("主实验结果", "主实验结论", "结论"), 140)
        or _first_useful_line(sections.get(6, ""), 140)
    )
    borrow = (
        _first_numbered_or_bulleted(sections.get(7, ""), 140)
        or _extract_labeled(sections.get(9, ""), ("如果借鉴创新点", "借鉴创新点"), 140)
        or "未明确"
    )
    next_action = {
        "精读": "精读/纳入核心文献池",
        "泛读": "泛读/保留为相关工作",
        "跳过": "标注为补充材料或暂存",
    }[priority]

    return BreakdownRow(
        index=index,
        stem=path.stem,
        title=_cell(title, 80),
        year=_cell(year, 16),
        venue=_cell(venue, 60),
        rank=_rank_from_venue(venue),
        direction=_cell(primary_topic, 48),
        task_problem=task_problem or "未明确",
        datasets=datasets or "未明确",
        metrics=metrics or "未明确",
        code_model_data=_code_model_data(block),
        relevance=relevance,
        priority=priority,
        thesis_chapter=_thesis_chapter(primary_topic, priority),
        one_sentence=one_sentence or "未明确",
        core_method=core_method or "未明确",
        experiment_result=experiment_result or "未明确",
        borrow=borrow,
        next_action=next_action,
    )


def collect_rows(notes_dir: Path = DEFAULT_NOTES) -> list[BreakdownRow]:
    rows = []
    for path in sorted(notes_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        rows.append(build_row(path, text, index=len(rows) + 1))
    return rows


def _render_row(row: BreakdownRow, index: int) -> str:
    cells = [
        str(index),
        f"[[{row.stem}]]",
        row.title,
        row.year,
        row.venue,
        row.rank,
        row.direction,
        row.task_problem,
        row.core_method,
        row.datasets,
        row.metrics,
        row.experiment_result,
        row.borrow,
        row.code_model_data,
        row.relevance,
        row.priority,
        row.thesis_chapter,
        row.next_action,
    ]
    return "| " + " | ".join(cells) + " |"


def render_batch_section(rows: list[BreakdownRow], generated_on: Optional[str] = None) -> str:
    generated_on = generated_on or date.today().isoformat()
    header = [
        BATCH_START,
        "",
        "## 9. 五百篇论文批量阅读拆解总表",
        "",
        f"> 自动生成于 {generated_on}。来源为 `02-Notes/Papers/*.md` 的 frontmatter 与 `AI_READING_NOTE` 区块；分区/等级未联网核验，除常见顶会/顶刊外保留为“待查”。",
        f"> 当前填入 {len(rows)} 篇。相关度和阅读优先级按视觉/遥感/检测/分割/模型模块课题方向做粗判，后续可人工覆盖。",
        "",
        "| 序号 | 论文 | 论文标题 | 年份 | 期刊/会议 | 分区/等级 | 研究方向 | 任务/问题 | 核心方法 | 数据集 | 评价指标 | 实验主要证明 | 可借鉴点 | 代码/模型/数据 | 相关度 | 阅读优先级 | 可用于我论文哪一章 | 下一步动作 |",
        "|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    body = [_render_row(row, index) for index, row in enumerate(rows, 1)]
    return "\n".join(header + body + ["", BATCH_END, ""])


def upsert_batch_section(template: str, batch_section: str) -> str:
    pattern = re.compile(re.escape(BATCH_START) + r".*?" + re.escape(BATCH_END) + r"\n?", re.S)
    if pattern.search(template):
        return pattern.sub(lambda _match: batch_section, template)
    stripped = template.rstrip()
    return stripped + "\n\n" + batch_section


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notes", type=Path, default=DEFAULT_NOTES)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--out", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--generated-on", default=None, help="Date shown in the generated section.")
    args = parser.parse_args(argv)

    rows = collect_rows(args.notes)
    batch = render_batch_section(rows, generated_on=args.generated_on)
    template = args.template.read_text(encoding="utf-8")
    output = upsert_batch_section(template, batch)
    args.out.write_text(output, encoding="utf-8")

    priority_counts: dict[str, int] = {}
    for row in rows:
        priority_counts[row.priority] = priority_counts.get(row.priority, 0) + 1
    print(f"wrote {args.out}")
    print(f"rows {len(rows)}")
    for key in sorted(priority_counts):
        print(f"{key} {priority_counts[key]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
