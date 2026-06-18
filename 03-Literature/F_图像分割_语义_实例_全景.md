# 通用语义/实例/全景分割 (`F_图像分割_语义_实例_全景`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 通用语义/实例/全景分割
- **代号**: `F_图像分割_语义_实例_全景`
- **论文数**: 20
- **年份分布**: 2024: 7, 2019: 3, 2018: 2, 2023: 2, 2021: 1, 2015: 1

## 论文列表 (按年份排序)

- 2013 [[多类ROF分割 Iterated ROF]]
- 2015 [[SLaT三阶段分割 SLaT Segmentation]]
- 2016 [[生物孔隙分割 Bio-Pores]]
- 2017 [[TPAMI.2017.2699184]]
- 2018 [[2018_Application_of_a_sem]]
- 2018 [[分割恢复联合模型 Segmentation Restoration]]
- 2019 [[2019_Object_Contour_and_E]]
- 2019 [[变分分割基础Mumford-Shah与ROF Mumford-Shah ROF]]
- 2019 [[球面小波分割 Wavelet Sphere]]
- 2021 [[2021_Exploring_Depth_Cont]]
- 2023 [[深度学习背景下的图像语义分割方法综述]]  _R_综述_Survey_
- 2023 [[语义比例分割 Semantic Proportions]]
- 2024 [[MSAA]]  _B_注意力算子模块/R1_遥感_高光谱_变化检测_
- 2024 [[MSAF]]
- 2024 [[cjig_图像识别_弱监督语义分割方法综述]]
- 2024 [[cjig_图像识别_深度学习实时语义分割综述_完整版]]  _R_综述_Survey_
- 2024 [[cjig_遥感_面向无人机海岸带生态系统监测的语义分割基准数据集]]
- 2024 [[互补特征交互融合的RGB_D实时显著目标检测]]
- 2024 [[跨层细节感知和分组注意力引导的遥感图像语义分割]]
- 2025 [[注意力与方向特征增强的遥感图像语义分割]]

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
WHERE primary_topic = "F_图像分割_语义_实例_全景"
SORT year DESC
```

如果想包含跨主题的论文 (topics 列表里有本主题代号的, 即多标签), 用 `contains`:

```dataview
TABLE year, primary_topic, status
FROM "02-Notes/Papers"
WHERE contains(topics, "F_图像分割_语义_实例_全景")
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
