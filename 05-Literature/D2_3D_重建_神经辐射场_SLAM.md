# 3D 重建/NeRF/SLAM (`D2_3D_重建_神经辐射场_SLAM`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 3D 重建/NeRF/SLAM
- **代号**: `D2_3D_重建_神经辐射场_SLAM`
- **论文数**: 10
- **年份分布**: 2024: 6

## 论文列表 (按年份排序)

- 2024 [[2024_三维人脸成像及重建技术综述]]  _J_人脸_表情_伪造_情感/R_综述_Survey_
- 2024 [[2024_三维场景注视点渲染深度学习方法综述]]  _R_综述_Survey_
- 2024 [[2024_基于单目视觉惯性的同步定位与地图构建方法综述]]  _R_综述_Survey_
- 2024 [[2024_增量式尺度估计下的相机位置解算]]
- 2024 [[2024_数字室内三维场景构建综述]]  _R_综述_Survey_
- 2024 [[2024_面向三维人体坐标及旋转角估计的注意力融合网络]]
- ???? [[cjig_计算机图形学_三维重建场景纹理优化算法综述]]  _R_综述_Survey_
- ???? [[cjig_计算机图形学_几何属性引导的三维语义实例重建]]
- ???? [[基于神经辐射场和三维高斯泼溅的文本指导三维编辑综述]]  _R_综述_Survey_
- ???? [[大规模室外图像3维重建技术研究进展]]  _R_综述_Survey_

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
WHERE primary_topic = "D2_3D_重建_神经辐射场_SLAM"
SORT year DESC
```

如果想包含跨主题的论文 (topics 列表里有本主题代号的, 即多标签), 用 `contains`:

```dataview
TABLE year, primary_topic, status
FROM "02-Notes/Papers"
WHERE contains(topics, "D2_3D_重建_神经辐射场_SLAM")
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
