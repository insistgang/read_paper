# 视觉基础模型/VLM/LLM (`G_视觉基础模型_VLM_LLM`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 视觉基础模型/VLM/LLM
- **代号**: `G_视觉基础模型_VLM_LLM`
- **论文数**: 12
- **年份分布**: 2025: 6, 2024: 5, 2023: 1

## 论文列表 (按年份排序)

- 2023 [[2023_Vision-Language_Mode]]
- 2024 [[2024_FreezeAsGuard_Mitig]]
- 2024 [[2024_Remote_Sensing_ChatG]]
- 2024 [[2024_Remote_Sensing_Spati]]
- 2024 [[cjig_计算机视觉_分割一切模型SAM的潜力与展望]]
- 2024 [[大小模型端云协同进化技术进展]]
- 2025 [[2025_Genes_Shells_AI_Scientific_Reports]]
- 2025 [[2025_SAM2-ELNet_Label_En]]
- 2025 [[2025_Vision-Language_Mode]]
- 2025 [[多模态大模型驱动的三维视觉理解技术前沿进展]]
- 2025 [[结合提示学习和视觉语义生成融合的东巴画图像描述]]
- 2025 [[视觉基础模型研究现状与发展趋势]]

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
FROM "02-Notes/Papers"
WHERE primary_topic = "G_视觉基础模型_VLM_LLM"
SORT year DESC
```

如果想包含跨主题的论文 (topics 列表里有本主题代号的, 即多标签), 用 `contains`:

```dataview
TABLE year, primary_topic, status
FROM "02-Notes/Papers"
WHERE contains(topics, "G_视觉基础模型_VLM_LLM")
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
