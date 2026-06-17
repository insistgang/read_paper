#!/usr/bin/env python3
"""Rename paper PDFs/notes/caches to Chinese-oriented stems.

The library invariant is:

  01-Papers/<stem>.pdf
  02-Notes/Papers/<stem>.md
  .paper-cache/extracts/<stem>.txt

This script builds a deterministic Chinese-oriented stem for every note from
frontmatter title/topic/year and then renames the three files together. It also
updates Obsidian links and cache paths that mention old stems.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_library import frontmatter_scalar, parse_frontmatter  # noqa: E402


ROOT = SCRIPT_DIR.parent
PAPERS_DIR = ROOT / "01-Papers"
NOTES_DIR = ROOT / "02-Notes" / "Papers"
CACHE_DIR = ROOT / ".paper-cache" / "extracts"
DEFAULT_MAPPING = ROOT / "03-Literature" / "中文重命名映射.json"
FILENAME_BOUNDARY_CHARS = r"A-Za-z0-9_\-\u4e00-\u9fff&()（）+., "


TOPIC_LABELS = {
    "A1_医学图像_分割": "医学图像分割",
    "A1b_医学图像_小样本_综述": "医学图像小样本综述",
    "A2_医学图像_分类_配准_生成": "医学图像分类配准生成",
    "A3_医学图像_配准_切片_张量_数学": "医学图像配准张量",
    "B_注意力算子模块": "注意力算子模块",
    "C_目标检测_通用与旋转框": "目标检测",
    "C2_目标检测_违建_车辆_船舶_行人": "遥感目标检测",
    "C3_目标检测_红外_可见光融合": "红外可见光目标检测",
    "D_3D_点云_分类_分割_配准": "三维点云",
    "D2_3D_重建_神经辐射场_SLAM": "三维重建",
    "E_图像复原_超分_去噪_去雨去雾": "图像复原增强",
    "F_图像分割_语义_实例_全景": "图像分割",
    "G_视觉基础模型_VLM_LLM": "视觉大模型",
    "I_场景文本_OCR": "场景文本OCR",
    "J_人脸_表情_伪造_情感": "人脸表情伪造",
    "K_跟踪_视频_动作": "视频跟踪动作",
    "L_数据集_Benchmark": "数据集基准",
    "M_行人_重识别_检索": "行人重识别",
    "N_雷达_无线电_张量_数学": "雷达无线电数学",
    "O_物理对抗_安全_鲁棒": "物理对抗鲁棒",
    "P_跨域_域自适应_联邦": "跨域自适应联邦",
    "Q_自监督_对比学习_主动学习": "自监督主动学习",
    "R_综述_Survey": "综述",
    "R1_遥感_高光谱_变化检测": "遥感高光谱变化检测",
    "R2_控制_生物启发_其他跨学科": "控制生物启发",
    "S_变化检测_ChangeDetection": "变化检测",
    "T_遥感_建筑检测": "遥感建筑检测",
    "T_安全_入侵检测": "安全入侵检测",
    "T_通用_NLP_其他": "通用其他",
    "Z_工具与杂项_figures": "补充材料",
}

PHRASE_MAP = (
    ("remote sensing", "遥感"),
    ("medical image", "医学图像"),
    ("medical imaging", "医学影像"),
    ("object detection", "目标检测"),
    ("semantic segmentation", "语义分割"),
    ("instance segmentation", "实例分割"),
    ("image segmentation", "图像分割"),
    ("change detection", "变化检测"),
    ("super resolution", "超分辨率"),
    ("super-resolution", "超分辨率"),
    ("image restoration", "图像复原"),
    ("image denoising", "图像去噪"),
    ("image deblurring", "图像去模糊"),
    ("low-light image enhancement", "低光图像增强"),
    ("point cloud", "点云"),
    ("neural radiance fields", "神经辐射场"),
    ("gaussian splatting", "三维高斯泼溅"),
    ("human action recognition", "人体动作识别"),
    ("facial expression recognition", "面部表情识别"),
    ("person re-identification", "行人重识别"),
    ("person reidentification", "行人重识别"),
    ("optical character recognition", "光学文字识别"),
    ("scene text", "场景文本"),
    ("building detection", "建筑检测"),
    ("illegal construction", "违建检测"),
    ("ship matching", "船舶匹配"),
    ("satellite imagery", "卫星影像"),
    ("hyperspectral", "高光谱"),
    ("synthetic aperture radar", "合成孔径雷达"),
    ("intrusion detection", "入侵检测"),
    ("botnet", "僵尸网络"),
    ("voice presentation attack", "语音呈现攻击"),
    ("foundation model", "基础模型"),
    ("large multimodal model", "多模态大模型"),
    ("diffusion model", "扩散模型"),
    ("contrastive learning", "对比学习"),
    ("self-supervised", "自监督"),
    ("active learning", "主动学习"),
    ("domain adaptation", "域自适应"),
    ("federated", "联邦学习"),
    ("adversarial", "对抗"),
    ("uncertainty", "不确定性"),
    ("tensor", "张量"),
    ("wireless", "无线电"),
    ("radar", "雷达"),
    ("dataset", "数据集"),
    ("benchmark", "基准"),
    ("survey", "综述"),
    ("review", "综述"),
)

WORD_MAP = {
    "attention": "注意力",
    "transformer": "Transformer",
    "mamba": "Mamba",
    "yolo": "YOLO",
    "detr": "DETR",
    "cnn": "CNN",
    "rnn": "RNN",
    "vit": "ViT",
    "network": "网络",
    "networks": "网络",
    "model": "模型",
    "models": "模型",
    "learning": "学习",
    "deep": "深度",
    "detection": "检测",
    "detector": "检测器",
    "segmentation": "分割",
    "classification": "分类",
    "recognition": "识别",
    "matching": "匹配",
    "tracking": "跟踪",
    "restoration": "复原",
    "enhancement": "增强",
    "denoising": "去噪",
    "deblurring": "去模糊",
    "fusion": "融合",
    "registration": "配准",
    "reconstruction": "重建",
    "completion": "补全",
    "compression": "压缩",
    "estimation": "估计",
    "prediction": "预测",
    "localization": "定位",
    "optimization": "优化",
    "efficient": "高效",
    "lightweight": "轻量化",
    "robust": "鲁棒",
    "adaptive": "自适应",
    "multi": "多尺度",
    "multiscale": "多尺度",
    "scale": "尺度",
    "feature": "特征",
    "features": "特征",
    "image": "图像",
    "images": "图像",
    "video": "视频",
    "visual": "视觉",
    "vision": "视觉",
    "remote": "遥感",
    "sensing": "感知",
    "satellite": "卫星",
    "aerial": "航空",
    "building": "建筑",
    "buildings": "建筑",
    "ship": "船舶",
    "tree": "树木",
    "forest": "森林",
    "medical": "医学",
    "brain": "脑",
    "mri": "MRI",
    "ct": "CT",
    "face": "人脸",
    "facial": "人脸",
    "emotion": "情感",
    "expression": "表情",
    "text": "文本",
    "ocr": "OCR",
    "point": "点云",
    "cloud": "点云",
    "three": "三维",
    "3d": "三维",
    "graph": "图",
    "graphical": "图形",
    "semantic": "语义",
    "instance": "实例",
    "object": "目标",
    "objects": "目标",
    "change": "变化",
    "illegal": "非法",
    "construction": "建设",
    "survey": "综述",
    "review": "综述",
    "dataset": "数据集",
    "benchmark": "基准",
}

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "based", "by", "for", "from", "in", "is",
    "of", "on", "or", "the", "to", "toward", "towards", "using", "via", "with",
    "without", "into", "its", "their", "this", "that", "be", "been", "new",
}
BAD_TITLE_RE = re.compile(
    r"^(?:\d{4}\.\d{4,5}v\d*|contentslistsavailableatsciencedirect|www\.|"
    r"ijcsiinternationaljournal)",
    re.I,
)


@dataclass(frozen=True)
class RenameItem:
    old_stem: str
    new_stem: str
    title: str
    topic: str
    year: str


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def clean_piece(text: str) -> str:
    text = text.replace("$^2$", "2")
    text = re.sub(r"[\u0000-\u001f\u007f]", " ", text)
    text = re.sub(r"[\\/:*?\"<>|#\[\]\n\r\t]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = text.strip(" ._-，,；;：:")
    return text


def title_is_usable(title: str) -> bool:
    title = clean_piece(title)
    compact = title.replace(" ", "")
    if not title:
        return False
    if BAD_TITLE_RE.search(compact):
        return False
    if re.fullmatch(r"\d{4}\.\d{4,5}v?\d*", title, re.I):
        return False
    if len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]+", title)) >= 4 and "," in title:
        return False
    return True


def cache_path_for(stem: str, fm: dict[str, str]) -> Path:
    cache = frontmatter_scalar(fm.get("extract_cache", ""))
    if cache:
        path = ROOT / cache
        if path.is_file():
            return path
    return CACHE_DIR / f"{stem}.txt"


def title_from_cache(stem: str, fm: dict[str, str]) -> str:
    path = cache_path_for(stem, fm)
    if not path.is_file():
        return ""
    raw_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    lines: list[str] = []
    for raw in raw_lines[:60]:
        if raw.strip().startswith("#"):
            continue
        line = clean_piece(raw)
        if not line:
            continue
        low = line.lower()
        if low in {"abstract", "a b s t r a c t", "article info", "i. introduction", "1. introduction"}:
            break
        if low.startswith(("contents lists available", "journal homepage", "keywords", "citation:")):
            continue
        if low in {
            "knowledge-based systems",
            "medical image analysis",
            "pattern recognition",
            "information sciences",
            "remote sensing",
            "sensors",
            "electronics",
            "machines",
        }:
            continue
        if re.search(r"@|doi\.org|arxiv:\d{4}\.\d{4,5}|^\d+$", line, re.I):
            continue
        if re.search(r"\b(university|institute|department|school|college|laboratory|china|usa|uk)\b", line, re.I):
            if lines:
                break
            continue
        lines.append(line)
        if len(lines) >= 3:
            break
    if not lines:
        return ""
    title = " ".join(lines[:2])
    return title if title_is_usable(title) else ""


def shorten(text: str, limit: int = 68) -> str:
    text = clean_piece(text)
    if len(text) <= limit:
        return text
    return text[:limit].rstrip(" _-，,；;：:")


def extract_existing_chinese(stem: str, title: str) -> str:
    source = stem if has_cjk(stem) else title if has_cjk(title) else ""
    if not source:
        return ""
    parts = re.split(r"[\s_]+", source)
    kept: list[str] = []
    for part in parts:
        part = clean_piece(part)
        if not part:
            continue
        if has_cjk(part):
            kept.append(part)
            continue
        # Keep useful technical acronyms next to Chinese titles.
        if re.fullmatch(r"[A-Z0-9][A-Za-z0-9&+\-.]{1,16}", part):
            kept.append(part)
    if not kept:
        return shorten(source)
    return shorten("_".join(kept))


def extract_model_names(text: str) -> list[str]:
    names: list[str] = []
    for match in re.finditer(r"\b[A-Z][A-Za-z0-9]*(?:[-_][A-Za-z0-9]+)*\b", text):
        token = match.group(0).strip("_-")
        if len(token) < 2 or token.lower() in STOPWORDS:
            continue
        if token in {"Abstract", "Introduction", "Journal", "Conference", "Proceedings"}:
            continue
        if token not in names:
            names.append(token)
        if len(names) >= 3:
            break
    return names


def chinese_from_english(title: str, stem: str, topic: str) -> str:
    source = title if title and not title.endswith(".pdf") else stem
    source = clean_piece(source)
    lower = source.lower()
    labels: list[str] = []

    for phrase, label in PHRASE_MAP:
        if phrase in lower and label not in labels:
            labels.append(label)

    words = re.findall(r"[A-Za-z0-9]+", lower)
    for word in words:
        if word in STOPWORDS:
            continue
        label = WORD_MAP.get(word)
        if label and label not in labels:
            labels.append(label)
        if len(labels) >= 8:
            break

    model_names = extract_model_names(source)
    topic_label = TOPIC_LABELS.get(topic, "论文")
    pieces = model_names[:2] + labels[:6]
    if not pieces:
        pieces = [shorten(source, 36)] if source else [topic_label]
    return shorten("_".join([topic_label] + pieces), limit=68)


def candidate_stem(note: Path) -> str:
    text = note.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    title = frontmatter_scalar(fm.get("title", ""))
    if not title_is_usable(title):
        title = title_from_cache(note.stem, fm) or title
    topic = frontmatter_scalar(fm.get("primary_topic", ""))
    year = frontmatter_scalar(fm.get("year", ""))

    base = extract_existing_chinese(note.stem, title)
    if not base:
        base = chinese_from_english(title, note.stem, topic)
    year_prefix = year if re.fullmatch(r"(19|20)\d{2}", year) else ""
    if year_prefix and not base.startswith(year_prefix):
        base = f"{year_prefix}_{base}"
    return shorten(base, limit=76)


def unique_stems(notes: Iterable[Path]) -> list[RenameItem]:
    used: dict[str, int] = {}
    items: list[RenameItem] = []
    for note in sorted(notes, key=lambda p: p.stem):
        text = note.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        title = frontmatter_scalar(fm.get("title", ""))
        if not title_is_usable(title):
            title = title_from_cache(note.stem, fm) or title
        topic = frontmatter_scalar(fm.get("primary_topic", ""))
        year = frontmatter_scalar(fm.get("year", ""))
        base = candidate_stem(note)
        count = used.get(base, 0) + 1
        used[base] = count
        new_stem = base if count == 1 else shorten(f"{base}_{count}", limit=80)
        existing_targets = {item.new_stem for item in items}
        while new_stem in existing_targets:
            count += 1
            used[base] = count
            new_stem = shorten(f"{base}_{count}", limit=80)
        items.append(RenameItem(note.stem, new_stem, title, topic, year))
    return items


def replace_links(text: str, mapping: dict[str, str]) -> str:
    updated = text
    for old, new in sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True):
        old_esc = re.escape(old)
        updated = re.sub(rf"\[\[{old_esc}\.pdf(?=([\]|]))", f"[[{new}.pdf", updated)
        updated = re.sub(rf"\[\[{old_esc}(?=([\]|]))", f"[[{new}", updated)
        updated = updated.replace(f".paper-cache/extracts/{old}.txt", f".paper-cache/extracts/{new}.txt")
        updated = updated.replace(f"# source: {old}.pdf", f"# source: {new}.pdf")
        updated = re.sub(
            rf"(?<![{FILENAME_BOUNDARY_CHARS}]){old_esc}\.pdf(?![{FILENAME_BOUNDARY_CHARS}])",
            f"{new}.pdf",
            updated,
        )
    return updated


def replace_frontmatter_value(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf"(?m)^{re.escape(key)}:\s*.*$")
    if pattern.search(text):
        return pattern.sub(f"{key}: {value}", text, count=1)
    end = text.find("\n---", 4)
    if end < 0:
        return text
    return text[:end] + f"\n{key}: {value}" + text[end:]


def update_note_text(text: str, old_stem: str, new_stem: str, mapping: dict[str, str]) -> str:
    updated = replace_links(text, mapping)
    updated = replace_frontmatter_value(updated, "pdf", f"[[{new_stem}.pdf]]")
    updated = replace_frontmatter_value(updated, "extract_cache", f".paper-cache/extracts/{new_stem}.txt")
    updated = updated.replace(f"- **PDF**: [[{old_stem}.pdf]]", f"- **PDF**: [[{new_stem}.pdf]]")
    return updated


def rename_with_temp(pairs: list[tuple[Path, Path]], apply: bool) -> None:
    changed = [(src, dst) for src, dst in pairs if src != dst]
    missing = [src for src, _ in changed if not src.exists()]
    if missing:
        raise SystemExit("missing files before rename:\n" + "\n".join(str(p) for p in missing[:20]))
    conflicts = [dst for src, dst in changed if dst.exists() and dst != src]
    if conflicts:
        raise SystemExit("target conflicts:\n" + "\n".join(str(p) for p in conflicts[:20]))
    if not apply:
        return
    temp_pairs: list[tuple[Path, Path]] = []
    for index, (src, dst) in enumerate(changed):
        tmp = src.with_name(f".rename_tmp_{index}_{src.name}")
        src.rename(tmp)
        temp_pairs.append((tmp, dst))
    for tmp, dst in temp_pairs:
        dst.parent.mkdir(parents=True, exist_ok=True)
        tmp.rename(dst)


def update_json_keys(path: Path, mapping: dict[str, str], apply: bool) -> bool:
    if not path.is_file():
        return False
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return False
    changed = False
    new_data = {}
    for key, value in data.items():
        new_key = mapping.get(key, key)
        changed = changed or new_key != key
        new_data[new_key] = value
    if changed and apply:
        path.write_text(json.dumps(new_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="执行重命名；默认只 dry-run")
    parser.add_argument("--mapping-out", type=Path, default=DEFAULT_MAPPING)
    args = parser.parse_args()

    notes = sorted(NOTES_DIR.glob("*.md"))
    items = unique_stems(notes)
    mapping = {item.old_stem: item.new_stem for item in items}
    changed_mapping = {old: new for old, new in mapping.items() if old != new}

    if len(set(mapping.values())) != len(mapping):
        raise SystemExit("generated duplicate target stems")

    records = [
        {
            "old": item.old_stem,
            "new": item.new_stem,
            "title": item.title,
            "year": item.year,
            "topic": item.topic,
        }
        for item in items
    ]
    if args.apply:
        args.mapping_out.parent.mkdir(parents=True, exist_ok=True)
        args.mapping_out.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    pdf_pairs = [(PAPERS_DIR / f"{old}.pdf", PAPERS_DIR / f"{new}.pdf") for old, new in mapping.items()]
    md_pairs = [(NOTES_DIR / f"{old}.md", NOTES_DIR / f"{new}.md") for old, new in mapping.items()]
    cache_pairs = [
        (CACHE_DIR / f"{old}.txt", CACHE_DIR / f"{new}.txt")
        for old, new in mapping.items()
        if (CACHE_DIR / f"{old}.txt").exists()
    ]

    rename_with_temp(pdf_pairs, args.apply)
    rename_with_temp(md_pairs, args.apply)
    rename_with_temp(cache_pairs, args.apply)

    text_paths = (
        list(NOTES_DIR.glob("*.md"))
        + list((ROOT / "03-Literature").glob("*.md"))
        + [ROOT / "论文阅读拆解表.md", ROOT / "README.md", PAPERS_DIR / "paper_classification.md"]
        + list(CACHE_DIR.glob("*.txt"))
    )
    changed_text_files = 0
    if args.apply:
        for path in text_paths:
            if not path.is_file():
                continue
            old_text = path.read_text(encoding="utf-8", errors="replace")
            new_text = replace_links(old_text, changed_mapping)
            if path.parent == NOTES_DIR:
                current_stem = path.stem
                old_stem = next((old for old, new in mapping.items() if new == current_stem), current_stem)
                new_text = update_note_text(new_text, old_stem, current_stem, changed_mapping)
            if new_text != old_text:
                path.write_text(new_text, encoding="utf-8")
                changed_text_files += 1
        for json_path in (PAPERS_DIR / "paper_topics.json",):
            if update_json_keys(json_path, changed_mapping, args.apply):
                changed_text_files += 1

    print("mode", "APPLY" if args.apply else "DRY_RUN")
    print("items", len(items))
    print("renamed_stems", len(changed_mapping))
    print("mapping_out", args.mapping_out)
    print("changed_text_files", changed_text_files)
    for item in records[:30]:
        if item["old"] != item["new"]:
            print(f"{item['old']} -> {item['new']}")
    if not args.apply:
        print("dry-run only; pass --apply to rename files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
