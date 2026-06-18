# 通用/旋转框目标检测 (`C_目标检测_通用与旋转框`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 通用/旋转框目标检测
- **代号**: `C_目标检测_通用与旋转框`
- **论文数**: 24
- **年份分布**: 2024: 8, 2025: 5, 2021: 3, 2022: 3, 2023: 3, 2016: 1

## 论文列表 (按年份排序)

- 2016 [[2016_A_Survey_on_Object_D]]
- 2019 [[2019_Object_detection_on]]
- 2021 [[2021_CFC-Net_A_Critical]]
- 2021 [[一阶全卷积遥感图像倾斜目标检测]]
- 2021 [[增强小目标特征的航空遥感目标检测]]
- 2022 [[2022_Deep_object_detectio]]
- 2022 [[2022_Object_Detection_in]]
- 2022 [[基于深度学习的视觉目标检测技术综述]]  _R_综述_Survey_
- 2023 [[AFPN]]
- 2023 [[无人机视角下的目标检测研究进展]]
- 2023 [[遥感影像小目标检测研究进展]]
- 2024 [[1-s2.0-S0950705124009833-main]]  _B_注意力算子模块_
- 2024 [[2024_Correlation_of_Objec]]
- 2024 [[2024_Improving_the_Detect]]
- 2024 [[2024_NBBOX_Noisy_Boundin]]
- 2024 [[2024_改进YOLOv7的交通标志识别模型]]
- 2024 [[CAA&PKIBlock]]  _B_注意力算子模块_
- 2024 [[cjig_目标检测_融合点云与图像的环境目标检测研究进展]]
- 2024 [[基于深度学习的有向目标检测研究进展_基于深度学习的有向目标检测研究进展]]
- 2025 [[2023_Oriented_object_dete]]
- 2025 [[2025_Are_Open-Vocabulary]]
- 2025 [[2025_Cross-View_Open-Voca]]  _P_跨域_域自适应_联邦/G_视觉基础模型_VLM_LLM_
- 2025 [[2025_UAV-DETR_Efficient]]
- 2025 [[光学遥感图像小目标检测深度学习算法综述]]

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
WHERE primary_topic = "C_目标检测_通用与旋转框"
SORT year DESC
```

如果想包含跨主题的论文 (topics 列表里有本主题代号的, 即多标签), 用 `contains`:

```dataview
TABLE year, primary_topic, status
FROM "02-Notes/Papers"
WHERE contains(topics, "C_目标检测_通用与旋转框")
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
