# 综述/Survey (`R_综述_Survey`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 综述/Survey
- **代号**: `R_综述_Survey`
- **论文数**: 19
- **年份分布**: 2024: 3, 2017: 1, 2020: 1

## 论文列表 (按年份排序)

- 2017 [[2017_A_Comprehensive_Surv]]
- 2020 [[2020_A_Comparison_of_Deep]]
- 2024 [[2024_基于物理的可微渲染综述]]
- 2024 [[2024_轻量化视觉定位技术综述]]
- 2024 [[2024_面向增强现实的虚实遮挡技术综述]]
- ???? [[cjig_图像识别_高质量超声成像与重建研究综述]]
- ???? [[cjig_计算机视觉_无人集群系统协同决策与博弈控制综述]]  _T_通用_NLP_其他_
- ???? [[cjig_计算机视觉_沉浸式环境和多场景中的视觉提示信息综述]]  _T_通用_NLP_其他_
- ???? [[cjig_遥感_多模态遥感图像配准方法研究综述]]
- ???? [[cjig_遥感_小样本SAR图像分类方法综述]]
- ???? [[人工智能在文物行业的应用与展望]]
- ???? [[图像重定向质量评价的研究进展]]
- ???? [[基于深度学习的图像融合方法综述]]
- ???? [[室内场景拟人交互研究进展]]
- ???? [[数据增强综述 Data Augmentation]]
- ???? [[无参考图像质量评价研究进展]]
- ???? [[深度学习单目深度估计研究进展]]  _T_通用_NLP_其他_
- ???? [[深度学习架构综述 CNNs RNNs Transformers]]  _T_通用_NLP_其他_
- ???? [[高光谱图像智能分类研究综述与展望]]  _R1_遥感_高光谱_变化检测_

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
WHERE primary_topic = "R_综述_Survey"
SORT year DESC
```

如果想包含跨主题的论文 (topics 列表里有本主题代号的, 即多标签), 用 `contains`:

```dataview
TABLE year, primary_topic, status
FROM "01-Papers"
WHERE contains(topics, "R_综述_Survey")
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
