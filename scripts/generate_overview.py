#!/usr/bin/env python3
"""生成 05-Literature/论文知识库总览.md, 作为整个知识库的入口页。

包含:
  - 仓库统计
  - 主题列表 (按 paper 数降序), 链接到 05-Literature/<主题>.md
  - Dataview 查询示例
  - 后续维护说明

约定:
  - 不覆盖已存在总览 (默认; --force 覆盖)
"""
import argparse
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PAPERS = ROOT / "01-Papers"          # PDF 原文目录
DEFAULT_NOTES = ROOT / "02-Notes" / "Papers"  # 论文笔记目录
DEFAULT_TOPICS_JSON = DEFAULT_PAPERS / "paper_topics.json"
DEFAULT_LIT = ROOT / "05-Literature"
DEFAULT_OVERVIEW = DEFAULT_LIT / "论文知识库总览.md"

# 主题 -> 中文显示名 (跟 generate_topic_index 保持一致)
TOPIC_DISPLAY = {
    "A1_医学图像_分割": "医学图像分割",
    "A1b_医学图像_小样本_综述": "医学图像小样本/综述",
    "A2_医学图像_分类_配准_生成": "医学图像分类/配准/生成",
    "A3_医学图像_配准_切片_张量_数学": "医学图像配准/张量数学",
    "B_注意力算子模块": "注意力算子/模块",
    "C_目标检测_通用与旋转框": "通用/旋转框目标检测",
    "C2_目标检测_违建_车辆_船舶_行人": "违建/车辆/船舶/行人检测",
    "C3_目标检测_红外_可见光融合": "红外+可见光融合检测",
    "C4_目标检测_交通_标志_检测器": "交通标志检测",
    "D_3D_点云_分类_分割_配准": "3D 点云分类/分割/配准",
    "D2_3D_重建_神经辐射场_SLAM": "3D 重建/NeRF/SLAM",
    "E_图像复原_超分_去噪_去雨去雾": "图像复原/超分/去噪去雨去雾",
    "F_图像分割_语义_实例_全景": "通用语义/实例/全景分割",
    "G_视觉基础模型_VLM_LLM": "视觉基础模型/VLM/LLM",
    "H_显著性_小目标": "显著性/小目标",
    "I_场景文本_OCR": "场景文本/OCR",
    "J_人脸_表情_伪造_情感": "人脸/表情/伪造/情感",
    "K_跟踪_视频_动作": "跟踪/视频/动作",
    "L_数据集_Benchmark": "数据集/Benchmark",
    "M_行人_重识别_检索": "行人/重识别/检索",
    "N_雷达_无线电_张量_数学": "雷达/无线电/张量/数学",
    "O_物理对抗_安全_鲁棒": "物理对抗/安全/鲁棒",
    "P_跨域_域自适应_联邦": "跨域/域自适应/联邦",
    "Q_自监督_对比学习_主动学习": "自监督/对比学习/主动学习",
    "R_综述_Survey": "综述/Survey",
    "R1_遥感_高光谱_变化检测": "遥感/高光谱/变化检测",
    "R2_控制_生物启发_其他跨学科": "控制/生物启发/其他",
    "S_变化检测_ChangeDetection": "变化检测",
    "T_通用_NLP_其他": "通用/NLP/其他",
    "Z_工具与杂项_figures": "工具/figures/杂项",
}


def build_overview(paper_topics: dict, today: str) -> str:
    total = len(paper_topics)
    primary_counter = Counter()
    multi_label = 0
    for stem, topics in paper_topics.items():
        primary_counter[topics[0]] += 1
        if len(topics) > 1:
            multi_label += 1

    # 主题表格: 按 primary_topic 论文数降序
    rows = []
    for code, n in primary_counter.most_common():
        if code == "U_未归类":
            continue
        name_zh = TOPIC_DISPLAY.get(code, code.replace("_", " "))
        rows.append(f"| [{name_zh}]({code}.md) | `{code}` | {n} |")

    rows_block = "\n".join(rows)

    body = f"""# 论文知识库总览

> 这是整个 Obsidian 论文库的入口页。生成于 {today}, 共收录 {total} 份 PDF。
> 主题分类基于**文件名**, 未读 PDF 内容。读 PDF 后请到对应笔记里升级 `source_basis`。

## 快速导航

- **PDF 原文目录**: `01-Papers/` (只放 PDF, 499 份)
- **论文笔记目录**: `02-Notes/Papers/` (一篇论文对应一个 .md, 499 篇)
- **论文清单 (分类索引)**: `01-Papers/paper_classification.md`
- **主题首页**: `05-Literature/<主题>.md` (下表每个主题都对应一个首页)
- **AI 临时缓存**: `.paper-cache/extracts/` (不进入正式知识库, 已被 .gitignore)
- **Dataview 查询**: 见 [[#Dataview 查询示例]]

## 主题分布 (按 primary_topic 论文数降序)

| 主题 | 代号 | 论文数 |
|------|------|--------|
{rows_block}

## 多标签论文

- 共 {multi_label} 篇论文 (总 {total}) 同时属于多个主题 (基于文件名的次要关键词)
- 这些论文在 [[paper_classification]] 里以 `topics: ...` 行标注

## Dataview 查询示例

### 按状态查看所有未读论文
```dataview
TABLE primary_topic, date_added, status
FROM "02-Notes/Papers"
WHERE status = "unread" AND source_basis = "filename"
SORT date_added DESC
```

### 按主题看论文数
```dataview
TABLE length(rows) AS 数量
FROM "02-Notes/Papers"
GROUP BY primary_topic
SORT 数量 DESC
```

### 已读且 confidence = high
```dataview
LIST
FROM "02-Notes/Papers"
WHERE status = "read" AND confidence = "high"
```

### 找带双链的笔记 (你开始建立知识网络时用)
```dataview
TABLE length(file.outlinks) AS "链接数"
FROM "02-Notes/Papers"
WHERE length(file.outlinks) > 0
SORT length(file.outlinks) DESC
```

## 维护流程

1. **新增 PDF**: 放到 `01-Papers/`, 跑
   ```
   python3 scripts/generate_skeleton_notes.py
   ```
   自动在 `02-Notes/Papers/` 生成同名 .md 骨架 (如果已有同名 .md 会跳过)。

2. **重新分类** (新增/删 PDF 后):
   ```
   python3 scripts/classify_papers.py
   python3 scripts/generate_skeleton_notes.py
   python3 scripts/generate_topic_index.py --force
   python3 scripts/generate_overview.py --force
   ```

3. **健康检查**:
   ```
   python3 scripts/validate_library.py
   ```

4. **读 PDF 后升级笔记**:
   - 把 `source_basis` 改为 `pdf-text`
   - 把 `reading_stage` 改为 `first-pass` / `skimming` / `deep-read` / `done`
   - 把 `confidence` 改为 `medium` / `high`
   - 补全 `## 关键贡献 / 方法 / 实验 / 局限` 几节
   - 主题首页里更新"建议阅读顺序", 加入自己的判断

## 主题首页索引

- [[B_注意力算子模块]] (134 篇)
- [[T_通用_NLP_其他]] (66 篇)
- [[C_目标检测_通用与旋转框]] (29 篇)
- [[D_3D_点云_分类_分割_配准]] (28 篇)
- [[A2_医学图像_分类_配准_生成]] (26 篇)
- [[C2_目标检测_违建_车辆_船舶_行人]] (23 篇)
- [[N_雷达_无线电_张量_数学]] (22 篇)
- [[R_综述_Survey]] (19 篇)
- ... 其余见上方"主题分布"表, 全部已生成在 05-Literature/

---

*本总览由 `scripts/generate_overview.py` 自动生成, 主题数量/链接请以文件为准。*
"""
    return body


def main():
    parser = argparse.ArgumentParser(
        description="生成 05-Literature/论文知识库总览.md",
    )
    parser.add_argument(
        "--papers", type=Path, default=DEFAULT_PAPERS,
    )
    parser.add_argument(
        "--topics-json", type=Path, default=DEFAULT_TOPICS_JSON,
    )
    parser.add_argument(
        "--out", type=Path, default=DEFAULT_OVERVIEW,
        help="总览输出路径 (默认: 05-Literature/论文知识库总览.md)",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="覆盖已存在总览",
    )
    args = parser.parse_args()

    if not args.topics_json.is_file():
        sys.exit(
            f"错误: {args.topics_json} 不存在, 先跑 scripts/classify_papers.py。"
        )

    paper_topics = json.loads(args.topics_json.read_text(encoding="utf-8"))
    today = date.today().isoformat()
    content = build_overview(paper_topics, today)

    if args.out.exists() and not args.force:
        sys.exit(
            f"错误: {args.out} 已存在, 加 --force 覆盖。"
        )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(content, encoding="utf-8")
    print(f"已写入 {args.out}")


if __name__ == "__main__":
    main()
