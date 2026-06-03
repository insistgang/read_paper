# 场景文本/OCR (`I_场景文本_OCR`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 场景文本/OCR
- **代号**: `I_场景文本_OCR`
- **论文数**: 5
- **年份分布**: 2024: 2

## 论文列表 (按年份排序)

- 2024 [[2024_结合文本自训练和对抗学习的领域自适应工业场景文本检测]]
- 2024 [[2024_融合场景先验的船名文本检测方法]]
- ???? [[cjig_图像处理_深度伪造及其取证技术综述]]  _J_人脸_表情_伪造_情感/R_综述_Survey_
- ???? [[大模型时代的光学文字识别_现状及展望]]
- ???? [[结合提示学习和视觉语义生成融合的东巴画图像描述]]

## 建议阅读顺序 (TODO: 人工)

> 入门 -> 核心 -> 进阶 -> 综述
>
> 命名规则: filename 通常含 `YYYY_关键词`, 可按年份递进。
> 调研时建议先看 Survey / 综述 (主题里带 `_综述` 或 `Survey`), 再读近 2 年的方法。

### 入门
- TODO: 从列表里选 2-3 篇 survey/intro
### 核心
- TODO: 选近 2 年的 SOTA 方法 3-5 篇
### 进阶
- TODO: 选 1-2 篇 method 复杂 / 有数学推导
### 综述
- TODO: 找主题里 _综述 标签的论文

## 关键问题 (TODO: 人工)

> 读了几篇后, 把这个主题下反复出现的核心科学问题列出来。

1.
2.
3.

## 方法分类 (TODO: 人工)

> 按方法族 (CNN / Transformer / Mamba / Diffusion / 等) 或任务范式分类。

- **CNN-based**:
- **Transformer-based**:
- **Mamba/SSM**:
- **其他**:

## 待精读清单

> 还没读但计划要读的论文 (按优先级)。

- [ ] (优先级高) TODO
- [ ] (优先级中) TODO
- [ ] (优先级低) TODO

## Dataview 查询示例

```dataview
TABLE year, primary_topic, status
FROM "01-Papers"
WHERE primary_topic = "I_场景文本_OCR"
SORT year DESC
```

如果想包含跨主题的论文 (topics 列表里有本主题代号的, 即多标签), 用 `contains`:

```dataview
TABLE year, primary_topic, status
FROM "01-Papers"
WHERE contains(topics, "I_场景文本_OCR")
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
