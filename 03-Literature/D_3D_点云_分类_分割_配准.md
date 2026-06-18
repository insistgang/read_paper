# 3D 点云分类/分割/配准 (`D_3D_点云_分类_分割_配准`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 3D 点云分类/分割/配准
- **代号**: `D_3D_点云_分类_分割_配准`
- **论文数**: 19
- **年份分布**: 2024: 5, 2023: 4, 2025: 3, 2020: 2, 2019: 1, 2017: 1

## 论文列表 (按年份排序)

- 2014 [[多功能传感器树木分类 Tree Species Classification]]
- 2017 [[3D树木描绘图割 3D Tree Delineation]]
- 2019 [[3D树木分割图 3D Tree Segmentation]]
- 2020 [[3D树木分割图割 3D Tree Graph Cut]]
- 2020 [[GraphLayer]]  _B_注意力算子模块_
- 2021 [[pnp3d(点云)]]
- 2022 [[多特征融合与几何卷积的机载LiDAR点云地物分类]]
- 2023 [[2023_Super_Sparse_3D_Obje]]
- 2023 [[cjig_图像处理_深度学习点云质量增强方法综述]]
- 2023 [[cjig_点云_融合小样本元学习和原型对齐的点云分割算法]]
- 2023 [[cjig_计算机图形学_三维场景点云理解与重建技术]]
- 2024 [[2024_PVAFN_Point-Voxel_A]]
- 2024 [[3DKMI Krawtchouk矩形状签名 3DKMI]]
- 2024 [[可见表面检测 Detect Closer Surfaces]]
- 2024 [[点云神经表示 Neural Varifolds]]
- 2024 [[面向点云几何压缩的隐式编码网络]]
- 2025 [[CornerPoint3D 3D检测新尺度 CornerPoint3D]]
- 2025 [[三维点云场景语义分割研究进展]]
- 2025 [[面向深度学习的三维点云补全算法综述]]

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
WHERE primary_topic = "D_3D_点云_分类_分割_配准"
SORT year DESC
```

如果想包含跨主题的论文 (topics 列表里有本主题代号的, 即多标签), 用 `contains`:

```dataview
TABLE year, primary_topic, status
FROM "02-Notes/Papers"
WHERE contains(topics, "D_3D_点云_分类_分割_配准")
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
