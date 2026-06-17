---
title: "SFFNet: A Wavelet-Based Spatial and Frequency"
authors:
  - "Yunsong Yang"
  - "Genji Yuan"
  - "Jinjiang Li"
year: 2024
venue: Domain Fusion Network for Remote Sensing
doi: 
pdf: [[FMS&MDAF.pdf]]
primary_topic: B_注意力算子模块
topics:
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
extract_cache: .paper-cache/extracts/FMS&MDAF.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/18 pages"
---
# SFFNet: A Wavelet-Based Spatial and Frequency

## 基本信息
- **PDF**: [[FMS&MDAF.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SFFNet: A Wavelet-Based Spatial and Frequency |
| **作者** | Yunsong Yang; Genji Yuan; Jinjiang Li |
| **发表时间** | 2024 |
| **刊物/会议** | Domain Fusion Network for Remote Sensing |
| **DOI** | 未明确 |

## 摘要

> —In order to fully utilize spatial information for segmentation and address the challenge of handling areas with significant grayscale variations in remote sensing segmentation, we propose the SFFNet (Spatial and Frequency Domain Fusion Network) framework. This framework employs a two-stage net- work design: the first stage extracts features using spatial meth- odstoobtainfeatureswithsufficientspatialdetailsandsemantic information;thesecondstagemapsthesefeaturesinbothspatial and frequency domains. In the frequency domain mapping, we introduce the Wavelet Transform Feature Decomposer (WTFD) structure, which decomposes features into low-frequency and high-frequency components using the Haar wavelet transform andintegratesthemwithspatialfeatures.Tobridgethesemantic gapbetweenfrequencyandspatialfeatures,andfacilitatesignif- icant feature selection to promote the combination of features from different representation domains, we design the Multiscale Dual-Representation Alignment Filter (MDA

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：随着高分辨率遥感影像的普及，精确的图像分割对GIS、资源管理等应用至关重要。然而，现有基于空间域的方法（无论是CNN还是Transformer）在处理阴影、边缘等灰度变化剧烈的区域时表现不佳。
- **之前方法的问题**：
    1. 基于空间域（纯CNN或CNN-Transformer融合）的方法对灰度剧变区域不敏感，导致分割错误。
    2. 少数引入频率域（如Haar小波变换）的研究，往往直接用频域特征替代空间特征，这会导致**空间信息丢失**和信息不清晰。
- **核心矛盾**：如何**有效引入频率域信息**以应对灰度剧变挑战，同时**最大限度地保留空间域的丰富语义和空间结构信息**，实现两种表示域的优势互补。
## 关键贡献

根据论文摘要和引言部分，具体贡献如下：
1.  **提出WTFD（Wavelet Transform Feature Decomposer）模块**：设计一个利用Haar小波变换的分解器，作为额外的频率域特征映射分支。它将空间特征分解为高频和低频信息，分别补充到网络的局部和全局信息流中，在引入频域信息的同时保留了原空间特征。
2.  **提出MDAF（Multiscale Dual-Representation Alignment Filter）模块**：为弥合频率域特征与空间域特征之间的语义鸿沟，并进行有效的特征选择，设计了此模块。它通过多尺度垂直条状卷积和双重交叉注意力机制，实现了跨尺度语义对齐与特征筛选。
3.  **提出SFFNet（Spatial and Frequency Domain Fusion Network）网络架构**：基于上述模块，构建了一个两阶段网络。第一阶段进行空间特征提取；第二阶段通过全局、局部映射保留空间信息，并通过WTFD引入频域信息，最终使用MDAF进行融合，形成一个完整的空间-频域融合分割框架。
## 方法

- **整体框架**：SFFNet是一个两阶段网络（如Fig. 2所示）。
    - **第一阶段（空间特征提取）**：使用ConvNext骨干网络提取多尺度空间特征（`x1, x2, x3, x4`）。然后将后三个尺度的特征通过卷积和插值融合，得到特征 `X‘`。
    - **第二阶段（特征映射与融合）**：以 `X‘` 作为输入，通过三个并行分支进行映射：
        1.  **全局分支（Global Branch）**：使用改进的Swin Transformer进行全局特征映射，得到 `Fg`。
        2.  **局部分支（Local Branch）**：使用池化金字塔进行多尺度局部特征映射，得到 `Fm`。
        3.  **频域分支（WTFD）**：使用Haar小波变换将 `X‘` 分解为低频特征 `Fl` 和高频特征 `Fh`。
        4.  **融合（MDAF）**：将空间特征（`Fg, Fm`）与对应的频域特征（`Fl, Fh`）分别送入MDAF模块进行对齐和选择，得到融合了频域信息的特征 `F‘g` 和 `F‘m`。
        5.  **输出**：将 `F‘g`, `F‘m` 与第一阶段的特征 `x1`、融合特征 `X‘` 一起拼接，通过分割头得到最终分割结果 `Y`。
- **输入输出**：输入为遥感图像 `x`；输出为像素级的语义分割结果 `Y`。
- **关键模块**：
    1.  **全局分支**：改进了Swin Transformer，用更高效的**垂直条状卷积**（`1×ws` 和 `ws×1` 卷积核）替代其复杂的SW-MSA来建立窗口间依赖关系（如Fig. 4所示），以适应遥感任务并降低计算复杂度。
    2.  **WTFD**：核心是Haar小波变换。它将空间特征分解为低频（主体轮廓、平滑区域）和高频（边缘、纹理细节）成分，然后将这些频域特征嵌入到CNN网络中（如Fig. 3(b)所示）。
    3.  **MDAF**：本文最核心的注意力模块。它接收一对空间特征 `S` 和频域特征 `F`，通过**多尺度垂直条状卷积**和**双重交叉注意力**，对齐二者的语义，并进行特征选择，最终输出融合了两者优势的特征。其公式化表示为 `F‘ = fmdaf(S, F)`。
- **模块连接**：如公式(2)-(4)所示，三个映射分支并行工作，然后MDAF模块将空间与频域特征配对处理，最后所有处理后的特征与早期特征融合输出。
- **训练方式**：PDF文本中未明确说明具体的损失函数、优化器等训练细节。
- **推理流程**：与训练流程一致，为端到端的单阶段前向传播。
- **与已有方法的差异**：与之前直接替换或简单拼接频域特征的方法不同，SFFNet**保留了独立的空间信息映射路径**（全局和局部），并**通过专门的MDAF模块进行深度融合**，而非简单叠加，这更好地平衡了空间信息保留与频域信息引入。
- **论文类型特化（注意力类）**：
    - **注意力作用维度**：MDAF模块作用于**空间域与频率域的跨域对齐**，并利用多尺度卷积在**多尺度**上进行特征筛选。
    - **可插入性**：MDAF被设计为SFFNet第二阶段的特征融合组件，用于对齐两个特定的特征图。
    - **计算量 vs 效果**：论文未提供MDAF或SFFNet整体的详细计算量分析（如FLOPs），但从结构描述看，使用垂直条状卷积替代SW-MSA旨在提升效率，而多尺度卷积和双重交叉注意力会带来一定的计算开销，其设计目标是换取在挑战性区域的分割性能提升。
## 实验

- **使用的数据集**：PDF文本中提到在“两个主流遥感分割数据集”上进行实验，但未在提供的文本页（p1-12）中明确给出数据集的具体名称。
- **对比方法**：文中提到了与**ST-Unet**、**XNet**等主流方法进行对比。
- **评价指标**：采用 **mIoU**（平均交并比）作为主要评价指标。
- **主实验结果**：在摘要中给出了关键结果：“SFFNet achieves superior performance in terms of mIoU, reaching **84.80%** and **87.73%** respectively.” 这分别对应两个数据集上的表现。
- **消融实验**：PDF文本中未找到对WTFD、MDAF等模块的消融实验细节。
- **泛化实验**：PDF文本中未找到在其它数据集或任务上的泛化实验描述。
- **速度/参数量/FLOPs**：PDF文本中未找到模型效率相关的具体数字。
## 局限

1.  **场景适用性**：方法主要针对灰度剧变区域设计，对于不存在此问题的简单遥感场景，其频域融合的优势可能不明显，而引入的额外计算（小波变换、MDAF）可能成为负担。
2.  **实验充分性**：根据提供的文本，**缺乏详细的消融实验**来验证WTFD和MDAF各个组成部分（如双重交叉注意力、多尺度卷积）的独立贡献。同时，也**缺少与更多最新频域融合方法**的对比。
3.  **数据集范围**：实验仅在两个遥感数据集上进行，在其他视觉领域或不同特性的遥感数据集上的有效性有待验证。
4.  **计算成本未知**：论文未提供模型参数量、FLOPs、推理速度等效率指标，难以评估其实用性和部署潜力。
5.  **复现风险**：MDAF模块结构较为复杂，包含多尺度卷积和双重交叉注意力，其具体的实现细节（如注意力头数、卷积具体配置）如果缺失，可能会给复现带来困难。
## 个人评论

1.  **思想启发**：展示了**空间域与频率域特征融合**在解决特定视觉难题（如灰度剧变）中的巨大潜力。这提醒研究者，除了关注空间维度，信号处理领域的经典工具（如小波变换）可以作为深度学习特征的强大补充。
2.  **模块设计思路**：MDAF模块提供了一种**跨域特征对齐与选择**的设计范式。它不是简单地拼接或相加，而是通过注意力机制让网络学习如何根据上下文，从两种不同表示域的特征中筛选出最有用的信息进行融合。
3.  **工程借鉴**：全局分支中用垂直条状卷积替代Swin Transformer的Shifted Window，是一种针对特定任务（遥感）**平衡全局建模能力与计算效率**的实用技巧，可被借鉴用于其他需要高效全局感受野的场景。

### 使用建议

- **如果快速了解**：阅读 **Abstract** 和 **Introduction**（第I节），可以迅速掌握论文解决的问题、核心思想和主要贡献。
- **如果复现**：重点精读 **III. METHOD**（第III节），特别是 **A. SFFNet Structure** 和 **B. Feature Mapping** 部分，结合 **Fig. 2, 3, 4** 来理解整体流程和关键模块（全局分支、WTFD、MDAF）的设计。需寻找官方代码库（论文中提供）进行对照。
- **如果借鉴创新点**：
    - 想借鉴 **空间-频域融合思想**：可以学习WTFD模块如何利用小波变换生成频域特征，并与空间特征并行处理。
    - 想借鉴 **跨域特征对齐机制**：可以重点研究MDAF模块，理解其如何使用注意力机制对齐和选择异质特征，并将其应用到自己需要融合多种特征的任务中。
- **如果写Related Work**：这篇论文可以放在以下几个类别中：1) **基于注意力机制的语义分割方法**；2) **频域特征在图像处理中的应用**；3) **Transformer与CNN结合的混合架构**；4) **遥感图像分割方法**。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中的**遥感图像语义分割**方向，具体是设计一种能够融合空间域和频率域信息的深度学习网络。它旨在解决遥感图像中因灰度变化剧烈（如阴影、边缘、纹理变化显著的区域）导致的分割难题。该论文应归类于 **“B_注意力算子模块”** 这一主题下，因为它提出了一个名为MDAF（Multiscale Dual-Representation Alignment Filter）的核心模块，该模块利用多尺度卷积和**双重交叉注意力**来对齐和选择来自不同表示域的特征。

## 2. 一句话总结
本文提出了一种名为SFFNet的两阶段网络，通过先提取空间特征，再利用小波变换引入频率域特征，并通过设计的MDAF注意力模块对二者进行语义对齐与特征选择，以增强遥感图像分割在灰度剧变区域的性能。

## 3. 背景与问题
- **为什么要做**：随着高分辨率遥感影像的普及，精确的图像分割对GIS、资源管理等应用至关重要。然而，现有基于空间域的方法（无论是CNN还是Transformer）在处理阴影、边缘等灰度变化剧烈的区域时表现不佳。
- **之前方法的问题**：
    1. 基于空间域（纯CNN或CNN-Transformer融合）的方法对灰度剧变区域不敏感，导致分割错误。
    2. 少数引入频率域（如Haar小波变换）的研究，往往直接用频域特征替代空间特征，这会导致**空间信息丢失**和信息不清晰。
- **核心矛盾**：如何**有效引入频率域信息**以应对灰度剧变挑战，同时**最大限度地保留空间域的丰富语义和空间结构信息**，实现两种表示域的优势互补。

## 4. 核心贡献
根据论文摘要和引言部分，具体贡献如下：
1.  **提出WTFD（Wavelet Transform Feature Decomposer）模块**：设计一个利用Haar小波变换的分解器，作为额外的频率域特征映射分支。它将空间特征分解为高频和低频信息，分别补充到网络的局部和全局信息流中，在引入频域信息的同时保留了原空间特征。
2.  **提出MDAF（Multiscale Dual-Representation Alignment Filter）模块**：为弥合频率域特征与空间域特征之间的语义鸿沟，并进行有效的特征选择，设计了此模块。它通过多尺度垂直条状卷积和双重交叉注意力机制，实现了跨尺度语义对齐与特征筛选。
3.  **提出SFFNet（Spatial and Frequency Domain Fusion Network）网络架构**：基于上述模块，构建了一个两阶段网络。第一阶段进行空间特征提取；第二阶段通过全局、局部映射保留空间信息，并通过WTFD引入频域信息，最终使用MDAF进行融合，形成一个完整的空间-频域融合分割框架。

## 5. 方法详解
- **整体框架**：SFFNet是一个两阶段网络（如Fig. 2所示）。
    - **第一阶段（空间特征提取）**：使用ConvNext骨干网络提取多尺度空间特征（`x1, x2, x3, x4`）。然后将后三个尺度的特征通过卷积和插值融合，得到特征 `X‘`。
    - **第二阶段（特征映射与融合）**：以 `X‘` 作为输入，通过三个并行分支进行映射：
        1.  **全局分支（Global Branch）**：使用改进的Swin Transformer进行全局特征映射，得到 `Fg`。
        2.  **局部分支（Local Branch）**：使用池化金字塔进行多尺度局部特征映射，得到 `Fm`。
        3.  **频域分支（WTFD）**：使用Haar小波变换将 `X‘` 分解为低频特征 `Fl` 和高频特征 `Fh`。
        4.  **融合（MDAF）**：将空间特征（`Fg, Fm`）与对应的频域特征（`Fl, Fh`）分别送入MDAF模块进行对齐和选择，得到融合了频域信息的特征 `F‘g` 和 `F‘m`。
        5.  **输出**：将 `F‘g`, `F‘m` 与第一阶段的特征 `x1`、融合特征 `X‘` 一起拼接，通过分割头得到最终分割结果 `Y`。
- **输入输出**：输入为遥感图像 `x`；输出为像素级的语义分割结果 `Y`。
- **关键模块**：
    1.  **全局分支**：改进了Swin Transformer，用更高效的**垂直条状卷积**（`1×ws` 和 `ws×1` 卷积核）替代其复杂的SW-MSA来建立窗口间依赖关系（如Fig. 4所示），以适应遥感任务并降低计算复杂度。
    2.  **WTFD**：核心是Haar小波变换。它将空间特征分解为低频（主体轮廓、平滑区域）和高频（边缘、纹理细节）成分，然后将这些频域特征嵌入到CNN网络中（如Fig. 3(b)所示）。
    3.  **MDAF**：本文最核心的注意力模块。它接收一对空间特征 `S` 和频域特征 `F`，通过**多尺度垂直条状卷积**和**双重交叉注意力**，对齐二者的语义，并进行特征选择，最终输出融合了两者优势的特征。其公式化表示为 `F‘ = fmdaf(S, F)`。
- **模块连接**：如公式(2)-(4)所示，三个映射分支并行工作，然后MDAF模块将空间与频域特征配对处理，最后所有处理后的特征与早期特征融合输出。
- **训练方式**：PDF文本中未明确说明具体的损失函数、优化器等训练细节。
- **推理流程**：与训练流程一致，为端到端的单阶段前向传播。
- **与已有方法的差异**：与之前直接替换或简单拼接频域特征的方法不同，SFFNet**保留了独立的空间信息映射路径**（全局和局部），并**通过专门的MDAF模块进行深度融合**，而非简单叠加，这更好地平衡了空间信息保留与频域信息引入。
- **论文类型特化（注意力类）**：
    - **注意力作用维度**：MDAF模块作用于**空间域与频率域的跨域对齐**，并利用多尺度卷积在**多尺度**上进行特征筛选。
    - **可插入性**：MDAF被设计为SFFNet第二阶段的特征融合组件，用于对齐两个特定的特征图。
    - **计算量 vs 效果**：论文未提供MDAF或SFFNet整体的详细计算量分析（如FLOPs），但从结构描述看，使用垂直条状卷积替代SW-MSA旨在提升效率，而多尺度卷积和双重交叉注意力会带来一定的计算开销，其设计目标是换取在挑战性区域的分割性能提升。

## 6. 实验与结果
- **使用的数据集**：PDF文本中提到在“两个主流遥感分割数据集”上进行实验，但未在提供的文本页（p1-12）中明确给出数据集的具体名称。
- **对比方法**：文中提到了与**ST-Unet**、**XNet**等主流方法进行对比。
- **评价指标**：采用 **mIoU**（平均交并比）作为主要评价指标。
- **主实验结果**：在摘要中给出了关键结果：“SFFNet achieves superior performance in terms of mIoU, reaching **84.80%** and **87.73%** respectively.” 这分别对应两个数据集上的表现。
- **消融实验**：PDF文本中未找到对WTFD、MDAF等模块的消融实验细节。
- **泛化实验**：PDF文本中未找到在其它数据集或任务上的泛化实验描述。
- **速度/参数量/FLOPs**：PDF文本中未找到模型效率相关的具体数字。

## 7. 这篇论文真正有价值的地方
1.  **思想启发**：展示了**空间域与频率域特征融合**在解决特定视觉难题（如灰度剧变）中的巨大潜力。这提醒研究者，除了关注空间维度，信号处理领域的经典工具（如小波变换）可以作为深度学习特征的强大补充。
2.  **模块设计思路**：MDAF模块提供了一种**跨域特征对齐与选择**的设计范式。它不是简单地拼接或相加，而是通过注意力机制让网络学习如何根据上下文，从两种不同表示域的特征中筛选出最有用的信息进行融合。
3.  **工程借鉴**：全局分支中用垂直条状卷积替代Swin Transformer的Shifted Window，是一种针对特定任务（遥感）**平衡全局建模能力与计算效率**的实用技巧，可被借鉴用于其他需要高效全局感受野的场景。

## 8. 局限与问题
1.  **场景适用性**：方法主要针对灰度剧变区域设计，对于不存在此问题的简单遥感场景，其频域融合的优势可能不明显，而引入的额外计算（小波变换、MDAF）可能成为负担。
2.  **实验充分性**：根据提供的文本，**缺乏详细的消融实验**来验证WTFD和MDAF各个组成部分（如双重交叉注意力、多尺度卷积）的独立贡献。同时，也**缺少与更多最新频域融合方法**的对比。
3.  **数据集范围**：实验仅在两个遥感数据集上进行，在其他视觉领域或不同特性的遥感数据集上的有效性有待验证。
4.  **计算成本未知**：论文未提供模型参数量、FLOPs、推理速度等效率指标，难以评估其实用性和部署潜力。
5.  **复现风险**：MDAF模块结构较为复杂，包含多尺度卷积和双重交叉注意力，其具体的实现细节（如注意力头数、卷积具体配置）如果缺失，可能会给复现带来困难。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：阅读 **Abstract** 和 **Introduction**（第I节），可以迅速掌握论文解决的问题、核心思想和主要贡献。
- **如果复现**：重点精读 **III. METHOD**（第III节），特别是 **A. SFFNet Structure** 和 **B. Feature Mapping** 部分，结合 **Fig. 2, 3, 4** 来理解整体流程和关键模块（全局分支、WTFD、MDAF）的设计。需寻找官方代码库（论文中提供）进行对照。
- **如果借鉴创新点**：
    - 想借鉴 **空间-频域融合思想**：可以学习WTFD模块如何利用小波变换生成频域特征，并与空间特征并行处理。
    - 想借鉴 **跨域特征对齐机制**：可以重点研究MDAF模块，理解其如何使用注意力机制对齐和选择异质特征，并将其应用到自己需要融合多种特征的任务中。
- **如果写Related Work**：这篇论文可以放在以下几个类别中：1) **基于注意力机制的语义分割方法**；2) **频域特征在图像处理中的应用**；3) **Transformer与CNN结合的混合架构**；4) **遥感图像分割方法**。

## 10. 和其他论文的关系
根据主题“B_注意力算子模块”，这篇论文可能与以下类型的工作相关：
- 使用**交叉注意力**或**多尺度注意力**进行特征融合的论文。
- 探索**Transformer与CNN混合架构**用于分割的论文，如 `[[ST-Unet]]`、`[[SwinUNet]]`。
- 研究**小波变换与深度学习结合**的图像处理论文，如 `[[MWCNN]]`。
- 其他**遥感图像分割**中关注边缘、阴影等细节恢复的论文。
- **注意**：由于提供的文本有限，且未明确其他论文标题，此处仅做基于主题的合理推测，不建立确切的双链关系。

## 11. 关键词
语义分割, 遥感图像, 注意力机制, 频域特征, 小波变换, 特征融合, 多尺度, 全局建模, 深度学习, SFFNet, MDAF, WTFD

## 12. 可信度说明
本精读笔记主要基于提供的PDF文本的前12页内容生成，涵盖了论文的**Abstract, Introduction, Related Work的前两节，以及Method部分的详细描述**。提取的文本质量较好，信息连贯。**主要局限**在于：缺少完整的**实验结果详情**（数据集名、完整消融表）、**训练细节**以及**结论**部分。因此，关于实验具体数字、效率分析、方法局限的讨论等内容部分基于已提供文本的推断，并已明确标注信息缺失处。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/FMS&MDAF.txt` (18/18 页; 原 AI 主体 12/18 + 全文补读 13-18); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-18; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-18。
- **提取情况**: 缺失页 6 页, 其中 6 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: SFFNet on the Vaihingen dataset resulted in a decrease of
- p.13: These reductions in performance are attributed to the semantic
- p.13: Therefore, we are more inclined to consider ConvNext-Tiny
- p.14: For the comparative models, the selected models are as
- p.14: Results of the Vaihingen Dataset: Tab.V presents numeri-
- p.14: ABCNet but also exceeded the DC-Swin network, based on
- p.14: Swintransformer, which has strong global information repre-
- p.14: CNN combined with Transformer network, relies solely on
- p.14: Our SFFNet surpassed XNet, which uses purely frequency
- p.14: In addition to comparing the segmentation accuracy of
- p.14: We selected the results of the first 44 rounds of training as
- p.14: Furthermore, compared to other models, our model exhibits

### 缺失页关键摘录

- p.13: Fig. 18. Local enlarged view of segmentation results of SFFNet and other comparative models on the Potsdam dataset. (a) corresponds to ABCNet. (b)
- p.13: to Xnet. (h) corresponds to SFFNet (Ours). Similar to the results on the Vaihingen dataset, it can be observed from the figure that our model performs better in
- p.13: to a decrease of 1.18% in mIoU and 0.68% in F1. Conversely,
- p.13: mIoU by 1.18% and F1 by 0.73%. On the other hand,
- p.13: SFFNet on the Vaihingen dataset resulted in a decrease of
- p.13: 0.69% in mIoU and 0.41% in F1. Similarly, on the Potsdam
- p.13: dataset, removing the high-frequency features led to a decrease
- p.13: of 0.8% in mIoU and 0.46% in F1. Conversely, adding high-
- p.13: frequency features to the baseline model increased mIoU by
- p.13: Through visualization results in Fig.11, it is observed that
- p.13: Fig.13(e), it can be seen that low-frequency features and
- p.13: On the other hand, through visualization results in Fig.12,
<!-- AI_READING_NOTE_END -->
