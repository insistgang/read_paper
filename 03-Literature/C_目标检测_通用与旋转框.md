# 通用/旋转框目标检测 (`C_目标检测_通用与旋转框`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 通用/旋转框目标检测
- **代号**: `C_目标检测_通用与旋转框`
- **论文数**: 29
- **年份分布**: 2024: 10, 2023: 5, 2025: 4, 2022: 3, 2021: 3, 2016: 1

## 论文列表 (按年份排序)

- 1996 [[增强小目标特征的航空遥感目标检测]]
- 2016 [[2016_A_Survey_on_Object_D]]
- 2019 [[2019_Object_detection_on]]
- 2020 [[2020_DiResNet_Direction-]]
- 2021 [[一阶全卷积遥感图像倾斜目标检测]]
- 2021 [[基于深度学习的视觉目标检测技术综述]]
- 2021 [[适合跨域目标检测的雾霾图像增强]]
- 2022 [[2022_Deep_object_detectio]]
- 2022 [[2022_Object_Detection_in]]
- 2022 [[2022_SODA_Site_Object_De]]
- 2023 [[2023_Oriented_object_dete]]
- 2023 [[2023_Super_Sparse_3D_Obje]]
- 2023 [[Mask_to_Height_YOLOv11_2510.27224]]
- 2023 [[无人机视角下的目标检测研究进展]]
- 2023 [[遥感影像小目标检测研究进展]]
- 2024 [[2024_NBBOX_Noisy_Boundin]]
- 2024 [[2024_PVAFN_Point-Voxel_A]]
- 2024 [[2024_YOLOv5-Based_Object]]
- 2024 [[2024_单帧红外图像多尺度小目标检测技术综述]]
- 2024 [[2024_改进YOLOv7的交通标志识别模型]]
- 2024 [[PPA&DASI&MDCR(红外小目标检测)]]
- 2024 [[cjig_图像识别_红外与可见光图像特征动态选择的目标检测网络]]
- 2024 [[cjig_目标检测_融合点云与图像的环境目标检测研究进展]]
- 2024 [[互补特征交互融合的RGB_D实时显著目标检测]]
- 2024 [[基于深度学习的有向目标检测研究进展_基于深度学习的有向目标检测研究进展]]
- 2025 [[2025_Lightweight_Object_D]]
- 2025 [[2025_Object_Detection_wit]]
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
