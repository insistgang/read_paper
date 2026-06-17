---
title: "SCKansformer: Fine-Grained Classification of Bone Marrow Cells via Kansformer Backbone and Hierarchical Attention Mechanisms"
authors:
  - "Yifei Chen"
  - "Zhu Zhu"
  - "Shenghao Zhu"
  - "Linwei Qiu"
  - "Binfeng Zou"
  - "Fan Jia"
  - "Yunpeng Zhu"
  - "Chenyan Zhang"
  - "Zhaojie Fang"
  - "Feiwei Qin"
  - "Jin Fan"
  - "Changmiao Wang"
  - "Yu Gao"
  - "Gang Yu"
year: 2024
venue: "arXiv:2406.09931 (IEEE Transactions/Journals template)"
doi: 
pdf: [[SCKansformer.pdf]]
primary_topic: A2_医学图像_分类_配准_生成
topics:
  - "A2_医学图像_分类_配准_生成"
  - "B_注意力算子模块"
status: ai-read
reading_stage: ai-fulltext
confidence: high
source_basis: pdf-text
date_added: 2026-06-03
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/SCKansformer.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# SCKansformer: Fine-Grained Classification of Bone Marrow Cells

## 基本信息
- **PDF**: [[SCKansformer.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`, `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SCKansformer: Fine-Grained Classification of Bone Marrow Cells via Kansformer Backbone and Hierarchical Attention Mechanisms |
| **作者** | Yifei Chen; Zhu Zhu; Shenghao Zhu; Linwei Qiu; Binfeng Zou; Fan Jia; Yunpeng Zhu; Chenyan Zhang; Zhaojie Fang; Feiwei Qin; Jin Fan; Changmiao Wang; Yu Gao; Gang Yu (陈逸非与朱竹并列第一作者; 通讯作者 朱竹、秦飞唯) |
| **单位** | 杭州电子科技大学; 浙江大学医学院附属儿童医院; 北京航空航天大学; 深圳市大数据研究院; 浙江医院 |
| **发表时间** | 2024-06-14 (arXiv v1) |
| **刊物/会议** | arXiv:2406.09931 [eess.IV], IEEE Transactions/Journals 模板 |
| **代码/数据** | https://github.com/JustlfC03/SCKansformer (含源码与私有 BMCD-FGCD 数据集) |
| **DOI** | 未明确 |

## 摘要

**清理后的英文原摘要（据 PDF 提取文本整理，修复空格/连字符断裂）：**

> The incidence and mortality rates of malignant tumors, such as acute leukemia, have risen significantly. Clinically, hospitals rely on cytological examination of peripheral blood and bone marrow smears to diagnose malignant tumors, with accurate blood cell counting being crucial. Existing automated methods face challenges such as low feature expression capability, poor interpretability, and redundant feature extraction when processing high-dimensional microimage data. We propose a novel fine-grained classification model, SCKansformer, for bone marrow blood cells, which addresses these challenges and enhances classification accuracy and efficiency. The model integrates the Kansformer Encoder, SCConv Encoder, and Global-Local Attention Encoder. The Kansformer Encoder replaces the traditional MLP layer with the KAN, improving nonlinear feature representation and interpretability. The SCConv Encoder, with its Spatial and Channel Reconstruction Units, enhances feature representation and reduces redundancy. The Global-Local Attention Encoder combines Multi-head Self-Attention with a Local Part module to capture both global and local features. We validated our model using the Bone Marrow Blood Cell Fine-Grained Classification Dataset (BMCD-FGCD), comprising over 10,000 samples and nearly 40 classifications, developed with a partner hospital. Comparative experiments on our private dataset, as well as the publicly available PBC and ALL-IDB datasets, demonstrate that SCKansformer outperforms both typical and advanced microcell classification methods across all datasets. Our source code and private BMCD-FGCD dataset are available at https://github.com/JustlfC03/SCKansformer.

**中文翻译：**

> 急性白血病等恶性肿瘤的发病率与死亡率显著上升。临床上，医院依赖对外周血涂片和骨髓涂片的细胞学检查来诊断恶性肿瘤，其中准确的血细胞计数至关重要。现有自动化方法在处理高维显微图像数据时面临诸多挑战：特征表达能力低、可解释性差、特征提取冗余。本文提出一种新颖的骨髓血细胞细粒度分类模型 SCKansformer，以应对上述挑战并提升分类精度与效率。该模型集成了 Kansformer 编码器、SCConv 编码器与全局-局部注意力编码器（GLAE）。Kansformer 编码器用 KAN 替代传统 MLP 层，改善非线性特征表示与可解释性；SCConv 编码器借助空间重建单元与通道重建单元增强特征表示并降低冗余；全局-局部注意力编码器将多头自注意力与局部部件模块结合，同时捕获全局与局部特征。我们在与合作医院共同构建的"骨髓血细胞细粒度分类数据集（BMCD-FGCD，逾 1 万样本、近 40 个类别）"上验证模型，并在公开的 PBC、ALL-IDB 数据集上做对比实验，结果表明 SCKansformer 在所有数据集上均优于典型与先进的微观细胞分类方法。源码与私有 BMCD-FGCD 数据集已开源。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **临床场景**：恶性血液病（白血病、再生障碍性贫血、多发性骨髓瘤等）的诊断依赖骨髓涂片细胞形态学。与外周血涂片只需区分 3~5 类白细胞不同，**骨髓涂片需检查近 40 种白细胞**，并据原始/幼稚细胞（primitive cells）的占比判断疾病类型与进展。骨髓是主要造血器官，骨髓细胞学结果是临床诊断与治疗的关键参考。
- **现有手段的不足**：
    1. **血液分析仪**（基于 Coulter 原理的三分类/五分类仪、流式细胞术）依赖物理/化学方法计数，只能识别少数几类细胞，且不提供可供进一步评估的显微图像，难以评估异常白细胞形态。
    2. **人工镜检**耗时费力，不同医生因经验与认知差异导致结果不一致、诊断标准不统一。
    3. **传统机器学习方法（如 SVM）**流程繁琐，提取的特征模糊，难以区分相似的骨髓细胞。
    4. **基于 CNN 的方法**受限于卷积核的感受野，**难以学习图像中的长距离依赖关系**，导致对细微特征差异的捕捉能力不足。
- **骨髓显微图像相对自然图像的四大挑战**（论文 I. Introduction 明确列出）：
    1. **成像条件多变（Variability in Imaging Conditions）**：不同医院、设备、成像环境产生颜色各异的骨髓血细胞图像。
    2. **长尾分布（Long-Tail Distribution）**：罕见疾病类别样本极少、常见类别样本充足，类别分布高度异质。
    3. **分辨率与对比度问题（Resolution and Contrast Issues）**：显微图像分辨率和对比度低于自然图像，可辨识特征少。
    4. **类间差异极小（Minimal Differences Between Cell Types）**：例如早幼、中幼、晚幼红细胞之间区别细微，极难区分。
- **核心矛盾**：如何从成像多变、长尾、低分辨率、类间差异极小的骨髓显微图像中，准确、高效地区分**近 40 类**外观高度相似的细胞。

## 关键贡献

论文在引言末尾明确列出四点贡献：

1. **Kansformer 编码器**：在 Transformer 编码器内用 Kolmogorov-Arnold 网络（KAN）替代传统多层感知机（MLP）层，针对显微图像等高维图像数据，**增强非线性特征表示与可解释性**，从而提升骨髓血细胞分类精度。
2. **增强的特征表示（SCConv + GLAE）**：
    - **SCConv 编码器**：通过空间重建单元（SRU）和通道重建单元（CRU）**降低特征冗余**，优化目标细胞的特征表示。
    - **全局-局部注意力编码器（GLAE）**：将多头自注意力（MSA）模块与局部部件（Local Part）模块结合，**同时捕获显微图像的全局与局部特征**，提升分类可靠性。
3. **BMCD-FGCD 数据集**：针对骨髓血样图像采集标注困难、缺乏高分辨率大规模标注数据集的现状，与杭州浙江医院血液科合作，建立并公开"骨髓细胞细粒度分类数据集（Bone Marrow Cell Dataset for Fine-Grained Classification）"，**逾 10,000 个数据点、近 40 个类别**。
4. **实验验证**：在私有 BMCD-FGCD 与公开 PBC、ALL-IDB 数据集上做对比实验，结果表明 SCKansformer **在所有数据集上均优于**其他方法；模型在不平衡和平衡细胞类别数据集上均保持优越性能，体现广泛适用性；并通过消融实验验证各模块的有效性与必要性。

## 方法

**整体框架**（III. Methodology A. Overall Architecture）：SCKansformer 由三个核心组件构成——**Kansformer 编码器、SCConv 编码器、全局-局部注意力编码器（GLAE）**，结构见原文 Fig. 1。

**输入输出**：输入为骨髓血细胞显微图像，输出为对应近 40 个类别的细粒度分类结果。

**关键模块与机制：**

1. **Kansformer 编码器（骨干）**：基于 Vision Transformer（ViT, [25]）结构，但将其中的 **MLP 层 [36]–[38] 替换为 KAN 网络 [16]**。结构由交替的多头自注意力（MSA）层与 KAN 网络层构成。KAN 基于 Kolmogorov-Arnold 表示定理，将可学习的激活函数放在边（权重）上而非节点上，论文据此主张其能提升 ViT 的非线性特征表示与可解释性。
2. **SCConv 编码器**：用于降低从 CNN 提取的特征中的冗余信息。
    - **空间重建单元（SRU）**：针对**空间冗余**，采用**分离-重建（separation-reconstruction）**策略。
    - **通道重建单元（CRU）**：针对**通道冗余**，采用**分离-变换-融合（separation-transformation-fusion）**策略。
3. **全局-局部注意力编码器（GLAE）**：由 MSA 模块和 Local Part 模块构成。
    - **MSA 模块**：通过自注意力机制学习**全局长距离依赖**。
    - **Local Part 模块**：捕获**局部精细特征**（提取文本在 p.12 末尾此处被截断，Local Part 的具体实现细节"据原文后续页，提取缓存未覆盖，待核"）。

**数学公式/机制直观解释**：论文主张 KAN 替代 MLP 增强非线性表示与可解释性；SCConv 通过空间与通道两路重建降低冗余；GLAE 的"全局+局部"双路设计旨在同时获取整体语义与关键局部细节。**KAN/SRU/CRU/GLAE 的具体公式在提取缓存覆盖的前 12 页中未完整给出（方法节在 p.12 被截断），待核。**

**训练方式、推理流程**：提取文本（前 12 页）未涉及训练策略（损失函数、优化器、学习率、数据增强）与详细推理流程，"据原文后续页，提取缓存未覆盖，待核"。

**和已有方法的差异**：相对传统 ViT（用 MLP），本模型用 KAN 提升表示能力与可解释性；相对普通 CNN，引入 Transformer 与全局注意力克服感受野限制；相对已有血细胞分类方法（多为外周血 3~5 类），本方法是专为骨髓细胞近 40 类细粒度分类设计的端到端框架，整合 KAN、SCConv、GLAE 多模块。

**论文类型特化（注意力/算子模块视角）**：
- **注意力作用维度**：GLAE 中 MSA 作用于**全局维度**，Local Part 作用于**局部维度**，构成层级（hierarchical）注意力；SCConv 则分别在**空间**与**通道**维度做特征重建。
- **可插入性**：SCConv、GLAE 设计为可集成的编码器模块；KAN 以"算子替换"方式嵌入 ViT。
- **计算量 vs 效果**：论文主张通过更有效的特征表示（KAN、SCConv）与更强特征捕获（GLAE）提升细粒度分类精度；前 12 页提取文本未给出 FLOPs/参数量等效率数字。

## 实验

> 注意：本地提取缓存仅覆盖 p.1–12（方法节在 p.12 被截断），**未覆盖实验结果表与具体数字**。以下结果框架据论文引言/方法节描述，以及原笔记"全文补读记录"从 p.13-15 捕获的表头与结论线索整理；所有具体数值"据原文后续页，提取缓存未覆盖，待核"。

**使用的数据集**：
- **私有数据集**：BMCD-FGCD（逾 10,000 样本，近 40 类，与浙江医院血液科合作构建并公开）。
- **公开数据集**：PBC（外周血细胞）、ALL-IDB（急性淋巴细胞白血病）。

**评价指标**：据原文 p.13 表头（"Method Precision Recall F1-score Accuracy"），主指标为 **Precision、Recall、F1-score、Accuracy**（据原文后续页，提取缓存未覆盖，具体数值待核）。

**对比实验**：
- 原文 p.13 含 **TABLE II（PBC 公开数据集对比）**、**TABLE III（ALL-IDB 公开数据集对比）**，与 SOTA 模型比较（据原文后续页，提取缓存未覆盖，具体方法名与数值待核）。
- 引言相关工作节（II. Related Work）提及的同领域参照方法包括：Choi 等两阶段 CNN（97.06%）、Reena 等 DeepLabv3+ + AlexNet（98.87%）、Ma Li 等改进 ResNet（BCCD 92%）、Novoselnik 等 LeNet-5（81.11%）等——这些是相关工作中引用的他人结果，非本文 SCKansformer 的实测对比表（待核是否进入本文对比表）。

**消融实验**：原文 p.13 含 **TABLE IV（私有 BMCD-FGCD 上的 SCKansformer 消融实验）**；p.14 提及"在 BMCD-(FGCD) 上进行消融实验"。消融用于验证各模块（KAN、SCConv、GLAE）的有效性与必要性（据原文后续页，提取缓存未覆盖，具体数值待核）。

**主要结论（据 p.13 结论线索）**：论文称 SCKansformer 在所有数据集上均优于其他方法；模块组合"大幅提升分类的精度与可靠性"，在不平衡 BMCD-FGCD 上的补充实验进一步支持该结论。

**效率信息（速度/参数量/FLOPs）**：提取缓存覆盖的前 12 页未提供；后续页是否给出"据原文后续页，提取缓存未覆盖，待核"。

## 局限

1. **本地复核受限于提取缓存**：本地提取缓存仅含前 12 页（方法节被截断），实验结果表、消融数值、效率分析均不可在本地核实，需取原文 p.13-15 或 GitHub 仓库补全。这是笔记的核查限制，非论文本身缺陷。
2. **方法普适性存疑**：模型针对骨髓细胞这一高度专业化场景设计，其组件（KAN、SCConv、GLAE）在通用视觉任务（如 ImageNet 分类）上的迁移效果未知；KAN 在大模型/大规模数据上的收益也需进一步验证。
3. **计算成本未量化**：KAN、SCConv、全局-局部注意力的引入很可能增加模型复杂度与计算开销，临床部署时是潜在限制因素；前 12 页提取文本未见效率对比（待核后续页）。
4. **可解释性承诺的兑现待核**：论文反复强调 KAN 提升可解释性，但前 12 页未展示可解释性实例（如 KAN 激活函数形状可视化、注意力热力图），其兑现程度需结合后续页或代码核实。
5. **私有数据集偏倚**：BMCD-FGCD 来自单一合作医院，长尾且成像条件特定，跨中心泛化能力需外部验证。

## 个人评论

> 本节为 AI 生成的评述，非论文原文结论。

1. **问题驱动的模块化设计**：论文清晰地把骨髓细胞分类的四大挑战（成像多变、长尾、低分辨率/对比度、类间差异极小）与三大模块（Kansformer、SCConv、GLAE）一一对应——KAN 强化非线性表示、SCConv 压冗余、GLAE 补长距离依赖与局部细节。这种"挑战-方案"逐条映射的写法是工程论文值得借鉴的叙事结构。
2. **KAN 进视觉骨干的早期尝试**：在 KAN 刚走红（2024）时就把它嵌入 ViT 替换 MLP，是一个有时效性的探索，为"用 KAN 改善可解释性/非线性能力"提供了视觉侧的可行性样例。但 KAN 在图像任务上的真实收益（相对参数量/算力）仍是开放问题，本文需更扎实的对照才能服人。
3. **医学高维冗余特征的处理思路可迁移**：SCConv 针对显微图像空间/通道冗余做重建、GLAE 针对细胞形态做全局+局部联合建模，这套思路对其他高维、高冗余、需关注局部细节的医学图像（病理切片、内镜、眼底）有直接借鉴价值。
4. **数据集贡献是真实价值点**：与医院合作构建并公开近 40 类、逾 1 万样本的骨髓细胞细粒度数据集，缓解了该领域数据稀缺瓶颈，可能比模型本身更有长期影响力。
5. **可改进处**：模型把多个"现成模块"（ViT + KAN + SCConv + Local Part）拼装，创新更多在工程整合而非单点突破；若要主张每个模块都必要，消融需做到逐模块、逐数据集的细致对照，并补足计算成本曲线，才能让"全面更优"的结论更有说服力。

### 使用建议

- **如果快速了解**：读 **"Abstract"、"I. Introduction"** 与 **"III. Methodology A. Overall Architecture"**，即可掌握动机、四大挑战、核心思想与三模块框架。
- **如果复现**：精读 **"III. Methodology"** 全节（KAN/SRU/CRU/GLAE 公式与连接），结合 Fig. 1 理解数据流；本地提取缓存截断于此节，务必取原文 p.4 起的完整方法节与 GitHub 仓库（`https://github.com/JustlfC03/SCKansformer`）获取代码、超参与数据集。
- **如果借鉴创新点**：
    - 想用 **KAN**：看 Kansformer 编码器如何以 KAN 替换 ViT 的 MLP。
    - 想压**特征冗余**：看 SCConv 中 SRU 的"分离-重建"与 CRU 的"分离-变换-融合"。
    - 想设计**层级注意力**：看 GLAE 中"全局 MSA + 局部 Local Part"的组合。
- **如果写 related work**：可归入 **"基于 Transformer 的医学图像分类"**、**"血/骨髓细胞细粒度分类"** 或 **"注意力/算子模块在医学影像中的应用"**。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**医学图像分析**领域的**细粒度图像分类**方向，具体解决**骨髓血细胞（Bone Marrow Cells）的自动化细粒度分类**问题（近 40 类），是辅助诊断急性白血病等恶性血液病的关键环节。论文提出的 SCKansformer 是一个**视觉 Transformer 变体**，核心创新在于：(1) 用 Kolmogorov-Arnold 网络（KAN）替换 ViT 中的 MLP，(2) 用 SCConv（SRU+CRU）压缩空间/通道冗余，(3) 用全局-局部注意力编码器（GLAE）联合建模长距离依赖与局部细节。论文同时贡献了公开数据集 BMCD-FGCD。

**分类说明**：本笔记将 primary_topic 由 `B_注意力算子模块` 调整为 **`A2_医学图像_分类_配准_生成`**——论文的核心问题、数据集与评测都是医学图像（骨髓细胞）分类，应用域是医学图像分析；KAN/GLAE 等注意力/算子创新是手段而非论文主旨，故保留 `B_注意力算子模块` 为次主题。

## 2. 一句话总结
SCKansformer 把 KAN（替代 MLP）、SCConv（空间+通道重建去冗余）与全局-局部注意力编码器三者集成进 ViT 骨干，构建一个面向骨髓血细胞近 40 类细粒度分类的端到端模型，并公开了逾 1 万样本的 BMCD-FGCD 数据集，在私有与公开（PBC、ALL-IDB）数据集上均称优于现有方法。

## 3. 背景与问题
- **为什么要做**：急性白血病等恶性肿瘤发病率/死亡率上升，临床依赖骨髓涂片细胞形态学确诊；骨髓涂片需区分**近 40 种**白细胞（远多于外周血的 3~5 种），人工镜检耗时、主观、标准不一，血液分析仪只能识别少数几类且不提供显微图像。
- **之前方法的问题**：
    1. 传统机器学习（SVM 等）流程繁琐、特征模糊，难区分相似骨髓细胞。
    2. CNN 受限于感受野，**难学长距离依赖**，对细微差异捕捉不足。
    3. 现有自动化方法处理高维显微图像时**特征表达能力低、可解释性差、特征提取冗余**。
- **四大领域挑战**（论文明列）：成像条件多变、长尾分布、分辨率/对比度低、类间差异极小（如早/中/晚幼红细胞难辨）。
- **核心矛盾**：在上述不利条件下，准确高效区分近 40 类外观高度相似的骨髓细胞。

## 4. 核心贡献
1. **Kansformer 编码器**：用 KAN 替代 ViT 内的 MLP 层，增强高维显微图像的非线性特征表示与可解释性，提升分类精度。
2. **增强特征表示（SCConv + GLAE）**：
    - **SCConv 编码器**：SRU（分离-重建，针对空间冗余）+ CRU（分离-变换-融合，针对通道冗余），降低 CNN 特征冗余。
    - **GLAE**：MSA（全局长距离依赖）+ Local Part（局部精细特征），同时捕获全局与局部特征，提升可靠性。
3. **BMCD-FGCD 数据集**：与浙江医院血液科合作建立并公开，逾 10,000 数据点、近 40 类，填补高分辨率大规模骨髓细胞标注数据空白。
4. **实验验证**：私有 BMCD-FGCD + 公开 PBC、ALL-IDB 上对比，称在所有数据集上均优于典型与先进方法；不平衡与平衡数据集上均表现优；消融验证各模块必要性。

## 5. 方法详解
**整体框架**：三核心组件——Kansformer 编码器、SCConv 编码器、GLAE（结构见 Fig. 1）。
**输入输出**：骨髓血细胞显微图像 → 近 40 类分类结果。
**关键模块**：
1. **Kansformer 编码器（骨干）**：基于 ViT，将 MLP 层替换为 KAN；结构为交替的 MSA 层与 KAN 网络层。KAN 基于 Kolmogorov-Arnold 表示定理，可学习激活函数置于边上而非节点上，论文据此主张提升非线性逼近效率与可解释性。
2. **SCConv 编码器**：降低 CNN 提取特征的冗余。SRU 用分离-重建处理空间冗余；CRU 用分离-变换-融合处理通道冗余。
3. **GLAE**：MSA 模块学全局长距离依赖，Local Part 模块捕获局部特征（**Local Part 的具体实现在提取缓存 p.12 末尾被截断，据原文后续页，提取缓存未覆盖，待核**）。
**机制直观解释**：KAN→非线性+可解释；SCConv→空间/通道去冗余；GLAE→全局语义+局部细节联合。**各模块完整公式在提取缓存覆盖的前 12 页未给全（方法节被截断），待核。**
**训练/推理**：提取缓存（前 12 页）未涉及损失函数、优化器、增强、推理流程，待核后续页。
**与已有方法差异**：vs ViT（用 KAN 替 MLP）；vs CNN（加 Transformer + 全局注意力破感受野）；vs 已有血细胞分类（多为外周血 3~5 类，本文专攻骨髓近 40 类细粒度、端到端多模块）。
**注意力/算子特化**：MSA 作用全局、Local Part 作用局部，构成层级注意力；SCConv 在空间与通道维度做特征重建；SCConv、GLAE 可作为可集成模块插入，KAN 以算子替换方式嵌入。前 12 页未给 FLOPs/参数量对比。

## 6. 实验与结果
> 本地提取缓存仅覆盖 p.1–12（方法节被截断），**实验结果表与具体数字均未覆盖**；以下据论文描述与原笔记从 p.13-15 捕获的表头/结论线索整理，**所有数值"据原文后续页，提取缓存未覆盖，待核"**。

**数据集**：私有 BMCD-FGCD（>10,000 样本，近 40 类）；公开 PBC（外周血细胞）、ALL-IDB（急淋白血病）。
**评价指标**：据 p.13 表头，**Precision / Recall / F1-score / Accuracy**（具体数值待核）。
**对比实验**：p.13 含 TABLE II（PBC）、TABLE III（ALL-IDB），与 SOTA 模型对比（方法名与数值待核）。相关工作节引用的他人成绩（Choi 97.06%、Reena 98.87%、Ma Li BCCD 92%、Novoselnik 81.11% 等）属背景参照，是否进入本文对比表待核。
**消融实验**：p.13 含 TABLE IV（私有 BMCD-FGCD 上的 SCKansformer 消融），p.14 提及在 BMCD-FGCD 上做消融，用于验证 KAN/SCConv/GLAE 的有效性与必要性（数值待核）。
**主要结论（据 p.13 结论线索）**：称在所有数据集上均优于其他方法；模块组合"大幅提升分类精度与可靠性"，不平衡数据补充实验支持该结论。
**效率信息**：前 12 页未提供速度/参数量/FLOPs，后续页是否给出待核。

## 7. 这篇论文真正有价值的地方
1. **问题驱动的模块化设计**：四大挑战（长尾、细粒度、成像差异、低分辨率）与三大模块逐条对应，"问题-方案"映射清晰，叙事结构值得学习。
2. **KAN 进视觉 Transformer 的早期样例**：在 KAN 走红初期就把它嵌入 ViT 替换 MLP，为改善可解释性/非线性能力提供视觉侧可行性参考。
3. **医学高维冗余特征处理思路可迁移**：SCConv 去冗余 + GLAE 全局-局部联合，对病理切片、内镜、眼底等高维高冗余、需关注局部细节的医学图像有直接借鉴价值。
4. **数据集贡献**：与医院合作构建并公开近 40 类、逾 1 万样本的骨髓细胞细粒度数据集，缓解数据稀缺瓶颈，长期价值可能高于模型本身。

## 8. 局限与问题
1. **本地复核受限**：提取缓存仅前 12 页（方法节被截断），实验/消融/效率数字本地不可核实，需取原文 p.13-15 或代码仓库补全（笔记核查限制，非论文缺陷）。
2. **普适性存疑**：组件针对骨髓细胞专用场景设计，在通用视觉任务上的迁移效果与 KAN 在大规模数据上的收益均待验证。
3. **计算成本未量化**：KAN+SCConv+全局-局部注意力可能显著增开销，临床部署是潜在瓶颈，前 12 页无效率分析。
4. **可解释性兑现待核**：反复强调 KAN 提升可解释性，但前 12 页未见可解释性可视化实例，兑现程度需结合后续页/代码核实。
5. **数据偏倚**：单中心私有数据，长尾且成像特定，跨中心泛化需外部验证。

## 9. 我该怎么使用这篇论文
- **快速了解**：读 Abstract、I. Introduction、III.A 整体架构。
- **复现**：精读 III. Methodology（KAN/SRU/CRU/GLAE 公式与连接）+ Fig. 1；本地缓存截断于此节，务必取原文完整方法节与 GitHub 仓库（`https://github.com/JustlfC03/SCKansformer`）。
- **借鉴创新点**：用 KAN → 看 Kansformer 如何替 MLP；压冗余 → 看 SRU/CRU 策略；层级注意力 → 看 GLAE 的"全局 MSA + 局部 Local Part"。
- **写 related work**：归入"基于 Transformer 的医学图像分类""血/骨髓细胞细粒度分类""注意力/算子模块在医学影像中的应用"。

## 10. 和其他论文的关系
按主题 `A2_医学图像_分类_配准_生成`（主）与 `B_注意力算子模块`（次），相关方向：
- **KAN / MLP 变体在视觉中的应用**：原始 KAN 论文（Liu et al. 2024, [16]）、ViT（[25]）、MLP-Mixer 等。
- **注意力/算子模块**：SCConv（SRU/CRU 来源）、各类局部/通道/轴向注意力用于图像分类。
- **医学（血液学/病理）中的 Transformer/CNN**：本文引言相关工作引用的 SVM 法（Ramoser、Duan）、CNN 法（Habibzadeh、Choi、Banik、Novoselnik、Reena DeepLabv3+、Tsykunov U-Net+ResNet、Ma Li 改进 ResNet）。
- **细粒度视觉分类**：通用 FGVC 方法及面向生物医学图像的细粒度分类。

## 11. 关键词
骨髓血细胞分类, 细粒度图像分类, Kolmogorov-Arnold 网络 (KAN), 空间通道重建卷积 (SCConv), 空间重建单元 (SRU), 通道重建单元 (CRU), 全局-局部注意力 (GLAE), Vision Transformer (ViT), 医学图像分析, BMCD-FGCD 数据集, 长距离依赖, 显微图像

## 12. 可信度说明
本精读基于本地 PDF 提取缓存（`# pages_extracted: 12/15`，且因 25000 字符上限在 p.12 方法节被截断）+ 原笔记"全文补读记录"对 p.13-15 捕获的表头/结论线索。**摘要、引言（动机、四大挑战、相关工作）、方法节前半（三模块的定位与 SRU/CRU/MSA/Local Part 的定性描述）可在提取文本逐句核实；而 GLAE 的 Local Part 实现细节、各模块完整公式、训练配置、全部实验/消融/效率数值在本地缓存中缺失**，已逐处以"据原文后续页，提取缓存未覆盖，待核"标注，未编造任何数字。建议结合原文 p.4-15 与 GitHub 仓库完成完整复核。

---

> **可信度补充**: PDF 提取质量 = **medium** (本地缓存仅 12/15 页且 p.12 方法节因 25000 字符上限截断, 实验/消融/效率数值缺失); 来源缓存: `.paper-cache/extracts/SCKansformer.txt` (12/15 页可用; p.13-15 仅有原笔记捕获的表头/结论线索); 生成日期: 2026-06-05; 优化复读: 2026-06-18; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Method Precision Recall F1-score Accuracy
- p.13: Combined with the ablation experiment results on the im-
- p.13: CONCLUSION
- p.13: This paper proposes a novel fine-grained classification
- p.13: This enables the model to accurately extract and represent
- p.13: This combination addresses the difficulty of simultaneously
- p.13: Through these innovative designs, the SCKansformer model
- p.13: In addition, the development of myeloid blood cell clas-
- p.13: The establishment and disclosure of the BMCD-FGCD dataset
- p.13: In comparative experiments, we evaluate the SCKansformer
- p.14: 14 IEEE TRANSACTIONS AND JOURNALS TEMPLATE
- p.14: Additionally, we conduct ablation experiments on the BMCD-

### 缺失页关键摘录

- p.13: TABLE II : Comparison with other state-of-the-art models on the PBC public dataset.
- p.13: Method Precision Recall F1-score Accuracy
- p.13: TABLE III : Comparison with other state-of-the-art models on the ALL-IDB public dataset.
- p.13: TABLE IV : SCKansformer ablation experiments on the private BMCD-FGCD dataset.
- p.13: accuracy, emphasizing the importance of these components
- p.13: Combined with the ablation experiment results on the im-
- p.13: balanced BMCD-FGCD dataset, these supplementary experi-
- p.13: greatly improves the accuracy and reliability of classification.
- p.13: excels in managing the complexity and accuracy requirements
- p.13: have jointly developed the BMCD-FGCD dataset with the
- p.13: Department of Hematology at Zhejiang Hospital. This dataset
- p.13: private dataset publicly available to the academic community.
<!-- AI_READING_NOTE_END -->
</content>
</invoke>
