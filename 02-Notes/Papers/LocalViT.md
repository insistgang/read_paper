---
title: "LocalViT: Bringing Locality to Vision Transformers"
authors:
  - "Yawei Li"
  - "Kai Zhang"
  - "Jiezhang Cao"
  - "Radu Timofte"
  - "Luc Van Gool"
year: 2012
venue: "arXiv"
doi: 
pdf: [[LocalViT.pdf]]
primary_topic: A1_医学图像_分割
topics:
  - "A1_医学图像_分割"
status: ai-read
reading_stage: ai-complete
confidence: high
source_basis: pdf-text
date_added: 2026-06-03
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/LocalViT.txt
---

# LocalViT: Bringing Locality to Vision Transformers

## 基本信息
- **PDF**: [[LocalViT.pdf]]
- **primary_topic**: `A1_医学图像_分割`
- **topics**: `A1_医学图像_分割`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | LocalViT: Bringing Locality to Vision Transformers |
| **作者** | Yawei Li; Kai Zhang; Jiezhang Cao; Radu Timofte; Luc Van Gool |
| **发表时间** | 2012 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> We study how to introduce locality mechanisms into vi- siontransformers.Thetransformernetworkoriginatesfrom machine translation and is particularly good at modelling long-rangedependencieswithinalongsequence. Although theglobalinteractionbetweenthetokenembeddingscould bewellmodelledbytheself-attentionmechanismoftrans- formers,whatislackingalocalitymechanismforinforma- tionexchangewithinalocalregion.Yet,localityisessential for images since it pertains to structures like lines, edges, shapes,andevenobjects. We add locality to vision transformers by introducing depth-wiseconvolutionintothefeed-forwardnetwork. This seeminglysimplesolutionisinspiredbythecomparisonbe- tween feed-forward networks and inverted residual blocks. Theimportanceoflocalitymechanismsisvalidatedintwo ways: 1) A wide range of design choices (activation func- tion, layer placement, expansion ratio) are available for incorporating locality mechanisms and all proper choices Figure 1: Comparison between LocalViT and the ba

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：卷积神经网络（CNN）依靠局部感受野和层叠结构来捕获层次化特征，天然具备局部性。而Transformer通过自注意力机制建模长程依赖，擅长全局信息交互，但缺乏处理图像局部结构（如边缘、形状）的专门机制。两者优势互补，因此如何高效地结合CNN的局部性与Transformer的全局性是一个自然而重要的问题。
- **之前方法有什么问题**：现有工作主要关注改进Transformer的输入tokenization或自注意力模块本身，例如引入多尺度token或局部注意力。但较少有工作深入探讨如何改进视觉Transformer中另一个基本组件——前馈网络（FFN），而FFN本身是逐位置处理，缺乏跨相邻位置的信息交互。
- **作者想解决的核心矛盾**：如何在**不显著增加模型参数和计算复杂度**的前提下，为擅长全局建模的视觉Transformer**高效地引入对局部信息聚合至关重要的机制**。
## 关键贡献

1.  **提出LocalViT架构**：通过在前馈网络（FFN）中引入深度可分离卷积，为视觉Transformer带来局部性机制。该架构结合了自注意力机制进行全局关系建模，以及卷积进行局部信息聚合。
2.  **系统分析局部性机制的性质**：通过大量消融实验，分析了局部性机制的关键组成部分（深度卷积、非线性激活函数、网络层放置位置、隐藏层维度扩展比率）各自的影响，并得出具体结论。
3.  **验证方法的普适性**：将所提出的局部性机制成功应用于四种不同的视觉Transformer架构（DeiT、T2T-ViT、PVT、TNT），证明了该概念的通用性和有效性。
4.  **提供简单有效的实现方案**：该方法实现简单，仅需修改FFN部分，且在引入局部性后，对参数量和计算量（FLOPs）的增加可以忽略不计，却带来了显著的准确率提升。
## 方法

- **整体框架**：LocalViT保持了标准Transformer编码器的结构，主要修改在每个Transformer层内的前馈网络（FFN）。它将CNN中高效的“倒残差块”（inverted residual block）的设计思想迁移到FFN中。
- **输入输出**：输入为图像经过分块和嵌入后的token序列（包含一个可学习的`[CLS]`分类token和N个图像patch token）。输出为处理后的token序列，用于下一阶段或最终分类。
- **关键模块**：**带局部性的前馈网络（Locality-enhanced FFN）**。传统FFN是两个全连接层（或1x1卷积）和一个激活函数。改进后的FFN结构为：`1x1卷积 -> 激活函数 -> 深度可分离卷积 -> 激活函数 -> 1x1卷积`。其中，深度卷积（k×k, k>1）是引入局部性的核心。
- **模块连接**：
    1.  从自注意力模块输出的token序列`Z`被拆分成`[CLS]` token和图像token两部分。
    2.  图像token被重排（`Seq2Img`）为2D特征图 `Zr`。
    3.  `Zr`通过上述带深度卷积的FFN进行处理，得到输出特征图 `Yr`。
    4.  `Yr`被重排回序列形式 `Y`（`Img2Seq`）。
    5.  将被旁路（bypass）的`[CLS]` token与`Y`重新拼接，作为下一个Transformer层的输入。
- **数学公式与直观解释**：
    - **传统FFN**：`Y = f(Z * W1) * W2`，其中f是激活函数，W1、W2是全连接层权重。这是一个逐位置操作，token之间无信息交互。
    - **LocalViT的FFN**：`Yr = f( f( Zr * Wr1 ) * Wd ) * Wr2`。`Wr1`和`Wr2`是1x1卷积核，`Wd`是深度卷积核。深度卷积在特征图的空间维度（局部区域）上进行滑动操作，实现了相邻token之间的信息交换，这就是“局部性”的来源。
- **训练方式**：采用标准的有监督训练，基于ImageNet数据集，使用交叉熵损失、标签平滑、AdamW优化器、余弦学习率调度等常见训练策略。训练协议与基线模型DeiT保持一致。
- **推理流程**：与标准Transformer推理流程无异。输入图像 -> patch embedding -> 通过一系列包含LocalViT层的Transformer Block -> 使用最终`[CLS]` token的特征进行分类。
- **与已有方法的差异**：与混合CNN-Transformer架构（如在Transformer前加卷积stem）不同，本文方法完全在Transformer Block内部进行修改。与修改自注意力模块为局部注意力的方法不同，本文保留了全局自注意力，仅在FFN中添加局部操作，结构更简洁。
- **论文类型特化（注意力类）**：
    - **注意力作用维度**：保留了标准的**全局空间**自注意力。
    - **可插入网络**：提出的局部性机制（即修改的FFN）是一个**即插即用**的模块，可替换多个主流视觉Transformer（DeiT, PVT等）的原始FFN。
    - **计算量 vs 效果**：以微小的参数量和计算量增加（如表1所示，Params从5.7M增加到5.8M，FLOPs基本不变）换取了显著的准确率提升（如从72.2%到73.7%），效费比极高。
## 实验

- **数据集**：ImageNet-2012，包含1000类，1.28M训练图像，50K验证图像。
- **对比方法**：主要与原始的视觉Transformer基线进行对比，包括DeiT-T、PVT-T等。
- **评价指标**：图像分类任务中的**Top-1准确率（%）**，以及模型参数量（Params，单位M）和计算量（FLOPs，单位G）。
- **主实验结果**：
    - **DeiT-T (baseline)**: 72.2% Top-1 acc, 5.7M Params, 1.3G FLOPs。
    - **LocalViT-T (本文方法，使用ReLU6)**: 73.7% Top-1 acc, 5.8M Params, 1.3G FLOPs。相比基线**提升1.5%**。
    - **LocalViT-T (扩展比率更大)**: 74.4% (使用h-swish) 至 75.8% (使用h-swish+SE) Top-1 acc。
    - **PVT-T** 提升了3.1%。
- **消融实验**：
    1.  **深度卷积的影响**：仅修改FFN结构（不加深度卷积）就能带来0.3%的微小提升。加入深度卷积后提升显著（表1）。
    2.  **激活函数的影响**：h-swish优于ReLU6。结合通道注意力模块（ECA或SE）可进一步提升，最佳组合（h-swish + SE with reduction ratio=4）达到75.8%（表2）。
    3.  **放置位置的影响**：在较低层（Layers 1-4, 1-8）加入局部性机制效果更好（表3）。
    4.  **隐藏层扩展比率的影响**：更大的扩展比率（如r=6 vs r=4）能提升模型容量和精度。
- **泛化实验**：将同样的方法应用于T2T-ViT-7、PVT-T、TNT-S，均取得了稳定的性能提升（如T2T-ViT-T提升2.2%，PVT-T提升3.1%），证明了方法的普适性。
- **效率信息**：参数量增加通常在0.1M到0.3M之间，计算量（FLOPs）基本不变或仅有极微小增加（通常在0.01-0.02G量级）。
## 局限

- **任务局限性**：论文仅在**图像分类**任务上进行了验证。其在更密集的预测任务（如目标检测、语义分割）上的有效性，尤其是在医学图像分割中的表现，PDF文本中未明确说明。
- **数据集单一性**：实验仅在ImageNet-1k上进行，对于数据分布差异巨大的领域（如医学影像）是否同样有效，尚待验证。
- **对FFN结构的强假设**：方法高度依赖于Transformer FFN的“先升维再降维”的结构。对于那些FFN设计不同的变体，此方法可能无法直接套用。
- **计算成本分析**：虽然作者声称计算增加“可忽略”，但对于某些极端追求效率的场景（如移动端部署），任何额外的卷积操作都可能被严格考量。
- **类token处理**：旁路类token不经过FFN的处理方式，虽然被实验验证“不影响性能”，但在理论上可能损失了部分类token在FFN阶段的上下文细化能力。
## 个人评论

1.  **思想的启发性**：它清晰地展示了如何将CNN中一个经典、高效的模块设计思想（倒残差块）迁移到Transformer的FFN中，以弥补Transformer在结构上的一个先天不足。这为“改造Transformer”提供了一种简洁优雅的思路。
2.  **工程的实用性**：方法极其简单，仅需修改FFN，无需复杂的架构重设计，且代码开销小。其带来的性能增益相对于微不足道的计算开销而言非常可观，对于实际应用和后续研究都有很高的参考价值。
3.  **研究的严谨性**：论文进行了系统而充分的消融实验，孤立变量地分析了每个组成部分的影响，得出的结论具体、可复现（如“深度卷积单独就能提升性能”、“h-swish比ReLU6好”、“局部性对低层更重要”），这为后续工作提供了可靠的实验范式和基线认知。

### 使用建议

- **如果快速了解**：阅读 **Abstract** 和 **Introduction** 部分，可以迅速把握论文的核心思想、动机和主要结论。
- **如果复现**：重点精读 **Methodology (Section 3)** 和 **Experimental Results (Section 4)** 部分，特别是实现细节（4.1节）和各消融实验的具体设置，以便准确复现实验。
- **如果借鉴创新点**：
    - **核心思想**：学习其将CNN模块（深度卷积）嵌入Transformer FFN的思路。
    - **技术细节**：参考其激活函数（h-swish+SE）和模块放置位置（低层更重要）的选择。
    - **实验设计**：模仿其系统性的消融实验设计。
- **如果写Related Work**：可将其放在“视觉Transformer的局部性/结构增强”或“CNN与Transformer混合架构”相关工作的综述中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A1_医学图像_分割]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中的**视觉Transformer（Vision Transformer）** 研究方向，具体是**网络架构设计与优化**。它旨在解决视觉Transformer缺乏**局部性（Locality）** 机制这一核心问题，通过将卷积神经网络（CNN）的局部信息聚合能力引入Transformer架构中。该方法属于通用视觉模型改进，其核心思想和技术路径（在前馈网络中引入深度卷积）可用于多种视觉任务，包括但不仅限于图像分类、检测和分割。基于用户提供的主题 `A1_医学图像_分割`，此方法理论上可应用于医学图像分析网络，但论文本身未涉及医学图像数据或任务。

## 2. 一句话总结
本文提出 **LocalViT**，通过将深度可分离卷积（depth-wise convolution）集成到视觉Transformer的前馈网络（FFN）中，以一种简单、高效的方式为模型引入了关键的局部性机制，从而在多个视觉Transformer架构上实现了显著的性能提升。

## 3. 背景与问题
- **为什么要做**：卷积神经网络（CNN）依靠局部感受野和层叠结构来捕获层次化特征，天然具备局部性。而Transformer通过自注意力机制建模长程依赖，擅长全局信息交互，但缺乏处理图像局部结构（如边缘、形状）的专门机制。两者优势互补，因此如何高效地结合CNN的局部性与Transformer的全局性是一个自然而重要的问题。
- **之前方法有什么问题**：现有工作主要关注改进Transformer的输入tokenization或自注意力模块本身，例如引入多尺度token或局部注意力。但较少有工作深入探讨如何改进视觉Transformer中另一个基本组件——前馈网络（FFN），而FFN本身是逐位置处理，缺乏跨相邻位置的信息交互。
- **作者想解决的核心矛盾**：如何在**不显著增加模型参数和计算复杂度**的前提下，为擅长全局建模的视觉Transformer**高效地引入对局部信息聚合至关重要的机制**。

## 4. 核心贡献
1.  **提出LocalViT架构**：通过在前馈网络（FFN）中引入深度可分离卷积，为视觉Transformer带来局部性机制。该架构结合了自注意力机制进行全局关系建模，以及卷积进行局部信息聚合。
2.  **系统分析局部性机制的性质**：通过大量消融实验，分析了局部性机制的关键组成部分（深度卷积、非线性激活函数、网络层放置位置、隐藏层维度扩展比率）各自的影响，并得出具体结论。
3.  **验证方法的普适性**：将所提出的局部性机制成功应用于四种不同的视觉Transformer架构（DeiT、T2T-ViT、PVT、TNT），证明了该概念的通用性和有效性。
4.  **提供简单有效的实现方案**：该方法实现简单，仅需修改FFN部分，且在引入局部性后，对参数量和计算量（FLOPs）的增加可以忽略不计，却带来了显著的准确率提升。

## 5. 方法详解
- **整体框架**：LocalViT保持了标准Transformer编码器的结构，主要修改在每个Transformer层内的前馈网络（FFN）。它将CNN中高效的“倒残差块”（inverted residual block）的设计思想迁移到FFN中。
- **输入输出**：输入为图像经过分块和嵌入后的token序列（包含一个可学习的`[CLS]`分类token和N个图像patch token）。输出为处理后的token序列，用于下一阶段或最终分类。
- **关键模块**：**带局部性的前馈网络（Locality-enhanced FFN）**。传统FFN是两个全连接层（或1x1卷积）和一个激活函数。改进后的FFN结构为：`1x1卷积 -> 激活函数 -> 深度可分离卷积 -> 激活函数 -> 1x1卷积`。其中，深度卷积（k×k, k>1）是引入局部性的核心。
- **模块连接**：
    1.  从自注意力模块输出的token序列`Z`被拆分成`[CLS]` token和图像token两部分。
    2.  图像token被重排（`Seq2Img`）为2D特征图 `Zr`。
    3.  `Zr`通过上述带深度卷积的FFN进行处理，得到输出特征图 `Yr`。
    4.  `Yr`被重排回序列形式 `Y`（`Img2Seq`）。
    5.  将被旁路（bypass）的`[CLS]` token与`Y`重新拼接，作为下一个Transformer层的输入。
- **数学公式与直观解释**：
    - **传统FFN**：`Y = f(Z * W1) * W2`，其中f是激活函数，W1、W2是全连接层权重。这是一个逐位置操作，token之间无信息交互。
    - **LocalViT的FFN**：`Yr = f( f( Zr * Wr1 ) * Wd ) * Wr2`。`Wr1`和`Wr2`是1x1卷积核，`Wd`是深度卷积核。深度卷积在特征图的空间维度（局部区域）上进行滑动操作，实现了相邻token之间的信息交换，这就是“局部性”的来源。
- **训练方式**：采用标准的有监督训练，基于ImageNet数据集，使用交叉熵损失、标签平滑、AdamW优化器、余弦学习率调度等常见训练策略。训练协议与基线模型DeiT保持一致。
- **推理流程**：与标准Transformer推理流程无异。输入图像 -> patch embedding -> 通过一系列包含LocalViT层的Transformer Block -> 使用最终`[CLS]` token的特征进行分类。
- **与已有方法的差异**：与混合CNN-Transformer架构（如在Transformer前加卷积stem）不同，本文方法完全在Transformer Block内部进行修改。与修改自注意力模块为局部注意力的方法不同，本文保留了全局自注意力，仅在FFN中添加局部操作，结构更简洁。
- **论文类型特化（注意力类）**：
    - **注意力作用维度**：保留了标准的**全局空间**自注意力。
    - **可插入网络**：提出的局部性机制（即修改的FFN）是一个**即插即用**的模块，可替换多个主流视觉Transformer（DeiT, PVT等）的原始FFN。
    - **计算量 vs 效果**：以微小的参数量和计算量增加（如表1所示，Params从5.7M增加到5.8M，FLOPs基本不变）换取了显著的准确率提升（如从72.2%到73.7%），效费比极高。

## 6. 实验与结果
- **数据集**：ImageNet-2012，包含1000类，1.28M训练图像，50K验证图像。
- **对比方法**：主要与原始的视觉Transformer基线进行对比，包括DeiT-T、PVT-T等。
- **评价指标**：图像分类任务中的**Top-1准确率（%）**，以及模型参数量（Params，单位M）和计算量（FLOPs，单位G）。
- **主实验结果**：
    - **DeiT-T (baseline)**: 72.2% Top-1 acc, 5.7M Params, 1.3G FLOPs。
    - **LocalViT-T (本文方法，使用ReLU6)**: 73.7% Top-1 acc, 5.8M Params, 1.3G FLOPs。相比基线**提升1.5%**。
    - **LocalViT-T (扩展比率更大)**: 74.4% (使用h-swish) 至 75.8% (使用h-swish+SE) Top-1 acc。
    - **PVT-T** 提升了3.1%。
- **消融实验**：
    1.  **深度卷积的影响**：仅修改FFN结构（不加深度卷积）就能带来0.3%的微小提升。加入深度卷积后提升显著（表1）。
    2.  **激活函数的影响**：h-swish优于ReLU6。结合通道注意力模块（ECA或SE）可进一步提升，最佳组合（h-swish + SE with reduction ratio=4）达到75.8%（表2）。
    3.  **放置位置的影响**：在较低层（Layers 1-4, 1-8）加入局部性机制效果更好（表3）。
    4.  **隐藏层扩展比率的影响**：更大的扩展比率（如r=6 vs r=4）能提升模型容量和精度。
- **泛化实验**：将同样的方法应用于T2T-ViT-7、PVT-T、TNT-S，均取得了稳定的性能提升（如T2T-ViT-T提升2.2%，PVT-T提升3.1%），证明了方法的普适性。
- **效率信息**：参数量增加通常在0.1M到0.3M之间，计算量（FLOPs）基本不变或仅有极微小增加（通常在0.01-0.02G量级）。

## 7. 这篇论文真正有价值的地方
1.  **思想的启发性**：它清晰地展示了如何将CNN中一个经典、高效的模块设计思想（倒残差块）迁移到Transformer的FFN中，以弥补Transformer在结构上的一个先天不足。这为“改造Transformer”提供了一种简洁优雅的思路。
2.  **工程的实用性**：方法极其简单，仅需修改FFN，无需复杂的架构重设计，且代码开销小。其带来的性能增益相对于微不足道的计算开销而言非常可观，对于实际应用和后续研究都有很高的参考价值。
3.  **研究的严谨性**：论文进行了系统而充分的消融实验，孤立变量地分析了每个组成部分的影响，得出的结论具体、可复现（如“深度卷积单独就能提升性能”、“h-swish比ReLU6好”、“局部性对低层更重要”），这为后续工作提供了可靠的实验范式和基线认知。

## 8. 局限与问题
- **任务局限性**：论文仅在**图像分类**任务上进行了验证。其在更密集的预测任务（如目标检测、语义分割）上的有效性，尤其是在医学图像分割中的表现，PDF文本中未明确说明。
- **数据集单一性**：实验仅在ImageNet-1k上进行，对于数据分布差异巨大的领域（如医学影像）是否同样有效，尚待验证。
- **对FFN结构的强假设**：方法高度依赖于Transformer FFN的“先升维再降维”的结构。对于那些FFN设计不同的变体，此方法可能无法直接套用。
- **计算成本分析**：虽然作者声称计算增加“可忽略”，但对于某些极端追求效率的场景（如移动端部署），任何额外的卷积操作都可能被严格考量。
- **类token处理**：旁路类token不经过FFN的处理方式，虽然被实验验证“不影响性能”，但在理论上可能损失了部分类token在FFN阶段的上下文细化能力。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：阅读 **Abstract** 和 **Introduction** 部分，可以迅速把握论文的核心思想、动机和主要结论。
- **如果复现**：重点精读 **Methodology (Section 3)** 和 **Experimental Results (Section 4)** 部分，特别是实现细节（4.1节）和各消融实验的具体设置，以便准确复现实验。
- **如果借鉴创新点**：
    - **核心思想**：学习其将CNN模块（深度卷积）嵌入Transformer FFN的思路。
    - **技术细节**：参考其激活函数（h-swish+SE）和模块放置位置（低层更重要）的选择。
    - **实验设计**：模仿其系统性的消融实验设计。
- **如果写Related Work**：可将其放在“视觉Transformer的局部性/结构增强”或“CNN与Transformer混合架构”相关工作的综述中。

## 10. 和其他论文的关系
- **直接对比/基于的基线论文**：`[[DeiT]]`， `[[PVT]]`， `[[T2T-ViT]]`， `[[TNT]]`。
- **思想来源论文**：`[[MobileNetV2]]` (倒残差块)， `[[MobileNetV3]]` (h-swish, SE模块)。
- **同领域相关工作**：`[[Swin Transformer]]` (局部窗口注意力)， `[[Conformer]]` (CNN与Transformer结合)， `[[CoAtNet]]` (深度卷积与注意力结合)。

## 11. 关键词
视觉Transformer, 局部性, 深度可分离卷积, 前馈网络, 倒残差块, 图像分类, 注意力机制, 即插即用, 网络架构设计, 消融实验

## 12. 可信度说明
本精读笔记**完全基于**用户提供的PDF提取文本（共10页）生成。内容主要涵盖论文的摘要、引言、相关工作、方法论、实验结果与分析部分。提取的文本信息完整，涵盖了研究动机、方法细节、实验设置和主要结论，足以支撑上述笔记各章节的详细阐述。所有引用的数字（如准确率、参数量）和结论均直接来源于提供的文本。对于文本中未涉及的内容（如具体的检测/分割实验、医学图像应用），已明确标注“PDF文本中未明确说明”。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2504 字符/页)); 来源缓存: `.paper-cache/extracts/LocalViT.txt` (10/10 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
