# 视觉基础模型/VLM/LLM (`G_视觉基础模型_VLM_LLM`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 视觉基础模型/VLM/LLM
- **代号**: `G_视觉基础模型_VLM_LLM`
- **论文数**: 16
- **年份分布**: 2025: 4, 2023: 3, 2024: 2

## 论文列表 (按年份排序)

- 2023 [[2023_2307.00056_Proximal_Nested_Sampling]]  _N_雷达_无线电_张量_数学/T_通用_NLP_其他_
- 2023 [[2023_OFAR_A_Multimodal_E]]  _T_通用_NLP_其他_
- 2023 [[2023_Vision-Language_Mode]]  _R_综述_Survey/T_通用_NLP_其他_
- 2024 [[2024_Brain-Inspired_Onlin]]  _T_通用_NLP_其他_
- 2024 [[2024_FreezeAsGuard_Mitig]]  _O_物理对抗_安全_鲁棒_
- 2025 [[2025_2508.08117_GRASPTrack_MultiObject_Tracking]]  _K_跟踪_视频_动作/T_通用_NLP_其他_
- 2025 [[2025_2510.09893_HIPPD_Brain-Inspired_Personality_Detection]]  _T_通用_NLP_其他_
- 2025 [[2025_SAM2-ELNet_Label_En]]  _T_通用_NLP_其他_
- 2025 [[2025_Vision-Language_Mode]]  _R_综述_Survey_
- ???? [[Scaling_Laws_for_Neural_Language_Models]]
- ???? [[cjig_计算机视觉_分割一切模型SAM的潜力与展望]]
- ???? [[多模态大模型驱动的三维视觉理解技术前沿进展]]  _R_综述_Survey_
- ???? [[大小模型端云协同进化技术进展]]
- ???? [[大模型高效微调CALM CALM Fine-tuning]]
- ???? [[视觉基础模型研究现状与发展趋势]]  _R_综述_Survey_
- ???? [[高效PEFT微调 Less but Better PEFT]]

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
WHERE primary_topic = "G_视觉基础模型_VLM_LLM"
SORT year DESC
```

如果想包含跨主题的论文 (topics 列表里有本主题代号的, 即多标签), 用 `contains`:

```dataview
TABLE year, primary_topic, status
FROM "01-Papers"
WHERE contains(topics, "G_视觉基础模型_VLM_LLM")
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
