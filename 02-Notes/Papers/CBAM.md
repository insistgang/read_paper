---
title: "CBAM: Convolutional Block Attention Module"
authors:
  - "Sanghyun Woo"
  - "Jongchan Park"
  - "Joon-Young Lee"
  - "In So Kweon"
year: 2018
venue: ECCV
doi:
pdf: [[CBAM.pdf]]
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
extract_cache: .paper-cache/extracts/CBAM.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# CBAM: Convolutional Block Attention Module

## 基本信息
- **PDF**: [[CBAM.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | CBAM: Convolutional Block Attention Module |
| **作者** | Sanghyun Woo; Jongchan Park; Joon-Young Lee; In So Kweon |
| **发表时间** | 2018 |
| **刊物/会议** | ECCV |
| **DOI** | 未明确 |

## 摘要

> WeproposeConvolutionalBlockAttentionModule(CBAM), a simple yet effective attention module for feed-forward convolutional neural networks. Given an intermediate feature map, our module se- quentiallyinfersattentionmapsalongtwoseparatedimensions,channel and spatial, then the attention maps are multiplied to the input feature mapforadaptivefeaturerefinement.BecauseCBAMisalightweightand general module, it can be integrated into any CNN architectures seam- lessly with negligible overheads and is end-to-end trainable along with base CNNs. We validate our CBAM through extensive experiments on ImageNet-1K, MS COCO detection, and VOC 2007 detection datasets. Ourexperimentsshowconsistentimprovementsinclassificationandde- tection performances with various models, demonstrating the wide ap- plicability of CBAM. The code and models will be publicly available.

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：提升CNN性能的传统研究主要关注网络深度、宽度和基数（cardinality）。本文作者希望从一个不同的角度——“注意力”——来进一步增强网络的表示能力，使模型能更专注于重要特征并抑制无关信息。
- **之前方法的问题**：先前的注意力工作（如Squeeze-and-Excitation, SE模块）主要关注通道维度的注意力，使用了全局平均池化来聚合信息，但忽略了最大池化所能提供的关于显著特征的线索。同时，它们也完全缺失了空间维度的注意力，而空间注意力决定了“在哪里”聚焦，这对于视觉任务至关重要。
- **核心矛盾**：如何设计一个轻量、通用且高效的模块，能够同时利用通道和空间两个关键维度的注意力信息，以实现比仅使用单一维度注意力更优的特征细化效果。
## 关键贡献

1.  提出了一个简单且高效的注意力模块——卷积块注意力模块（CBAM），它由两个顺序的子模块（通道注意力模块和空间注意力模块）构成，可广泛应用于增强各种CNN的表示能力。
2.  通过详尽的消融实验，验证了其设计选择的有效性，特别是证明了同时使用平均池化和最大池化的特征来计算通道注意力，以及顺序地（通道优先）组合两种注意力模块是最优策略。
3.  在多个标准基准（ImageNet-1K、MS COCO、VOC 2007）上，将CBAM应用于多种基础网络（ResNet、WideResNet、ResNeXt），均取得了显著的性能提升，证明了其广泛的适用性。
## 方法

- **整体框架**：CBAM是一个即插即用的模块，旨在被嵌入到CNN的每个卷积块中（如图3所示）。它顺序地对输入特征图应用通道注意力模块和空间注意力模块，以生成细化的特征图。
- **输入输出**：输入是CNN中间层的一个三维特征图 \( F \in \mathbb{R}^{C \times H \times W} \)。输出是经过注意力加权后得到的细化特征图 \( F'' \in \mathbb{R}^{C \times H \times W} \)。
- **关键模块**：
    1.  **通道注意力模块 (Channel Attention Module)**：旨在学习“什么”是重要特征。它首先通过**平均池化（AvgPool）** 和**最大池化（MaxPool）** 两个操作，将输入特征图 \( F \) 的空间信息压缩，分别得到两个通道描述符 \( F_c^{avg} \) 和 \( F_c^{max} \)。这两个描述符被送入一个**共享的MLP**网络进行处理。MLP的输出通过逐元素求和合并，并经过Sigmoid激活函数，得到一维的通道注意力图 \( M_c \in \mathbb{R}^{C \times 1 \times 1} \)。
    2.  **空间注意力模块 (Spatial Attention Module)**：旨在学习“哪里”是重要区域。它首先对输入特征图（经过通道注意力细化后）沿通道维度进行**平均池化**和**最大池化**，得到两个二维的空间描述符 \( F_s^{avg} \) 和 \( F_s^{max} \)。这两个描述符被拼接（concatenate）起来，然后通过一个**卷积核大小为7x7的卷积层**进行处理，最后经过Sigmoid激活函数，得到二维的空间注意力图 \( M_s \in \mathbb{R}^{1 \times H \times W} \)。
- **模块连接**：两个子模块是**顺序连接**的。具体过程如下：
    \( F' = M_c(F) \otimes F \) （通道注意力加权）
    \( F'' = M_s(F') \otimes F' \) （空间注意力加权）
    其中 \( \otimes \) 表示逐元素相乘。在乘法操作中，注意力值会沿相应维度进行广播（broadcast）。
- **数学公式/机制直观解释**：
    - **通道注意力**：\( M_c(F) = \sigma(MLP(AvgPool(F)) + MLP(MaxPool(F))) \)。直观上，平均池化捕获了全局语义信息，而最大池化捕获了最具区分性的局部特征。使用共享的MLP处理它们，并将结果相加，能更全面地评估每个通道的重要性。
    - **空间注意力**：\( M_s(F) = \sigma(f^{7 \times 7}([AvgPool(F); MaxPool(F)])) \)。沿通道的平均和最大池化分别生成了不同侧重的空间摘要图，将它们拼接后用大卷积核（7x7）进行融合，能够综合信息并利用较大的感受野来决定重要的空间位置。
- **训练方式**：CBAM是端到端可训练的，可以与基础CNN架构无缝集成并联合训练。其引入的参数量和计算量（GFLOPs）增加非常微小，几乎可以忽略。
- **推理流程**：在推理时，输入特征图依次经过通道注意力图和空间注意力图的逐元素乘法调制，输出细化后的特征图。
- **和已有方法的差异**：
    1.  相比SE模块，CBAM不仅使用了通道注意力，还增加了空间注意力。
    2.  在通道注意力计算上，CBAM不仅使用了SE中的平均池化，还引入了最大池化，并通过共享MLP进行融合，从而获取更丰富的通道间关系信息。
    3.  相比同期的BAM模块，CBAM被设计在每一个卷积块中插入，而BAM则放置在网络的每个瓶颈层（bottleneck）。
## 实验

- **使用的数据集**：ImageNet-1K（图像分类）、MS COCO（目标检测）、VOC 2007（目标检测）。
- **对比方法**：主要对比基线网络（如ResNet系列）和先前的注意力方法SE。
- **评价指标**：分类任务使用Top-1和Top-5错误率；检测任务的指标在提供的文本中未明确列出（通常是mAP）。
- **主实验结果**：
    - 在ImageNet-1K上，将CBAM应用于多种网络均带来了一致提升。例如，ResNet50的Top-1错误率从24.56%降至22.66%；ResNet101的Top-1错误率从23.38%降至21.51%（p.9-10, Table 4）。
    - 在MS COCO和VOC 2007检测任务上，CBAM也验证了其有效性，尤其是通过在现有单阶段检测器上添加模块，在VOC2007测试集上取得了当时领先的性能（p.2）。
- **消融实验**：
    1.  **通道注意力**：对比了仅用平均池化（SE）、仅用最大池化、以及同时使用两者（CBAM的设计）。结果证明，结合平均和最大池化的方法（Top-1 Error 22.80%）优于单独使用任一方法，也优于SE（23.14%）（p.7, Table 1）。
    2.  **空间注意力**：对比了不同的空间描述符生成方式（通道池化 vs. 1x1卷积）和不同的后续卷积核大小（3x3 vs. 7x7）。结果表明，使用通道池化并搭配7x7卷积核的组合效果最佳（Top-1 Error 22.66%）（p.8, Table 2）。
    3.  **注意力模块组合方式**：对比了顺序（通道优先、空间优先）和并行两种组合策略。结果表明顺序组合优于并行，且通道优先的顺序效果略好（p.9, Table 3）。
- **泛化实验**：在ImageNet-1K上，CBAM在不同深度（ResNet-18/34/50/101）、不同宽度（WideResNet）和不同基数（ResNeXt）的多种网络架构上都取得了稳定提升，证明了其泛化能力（p.9-10, Table 4）。
- **效率信息**：CBAM引入的额外计算量很小。例如，在ResNet50上，参数量从25.56M增至28.09M（增加2.53M），GFLOPs从3.858增至3.864（增加0.006）（p.7, Table 1 & p.10, Table 4）。
## 局限

- **适用场景**：论文主要聚焦于图像分类和目标检测。其在其他视觉任务（如语义分割、姿态估计、视频理解）中的有效性在提供的文本中未提及。
- **实验充分性**：消融实验非常充分，但所有实验均在标准基准数据集上进行。对于更复杂或分布差异大的场景（如小样本、域适应），其效果未知。
- **数据集局限性**：实验验证了其在主流数据集上的性能，但未探讨其在极端不平衡数据或特定领域数据（如医学、遥感）上的表现。
- **计算成本**：虽然模块本身是轻量的，但将其嵌入网络的所有卷积块后，总增加的计算量是否在所有情况下都“可忽略”可能需要根据具体应用场景和硬件平台来评估。
- **假设依赖**：该方法的有效性依赖于一个基本假设：特征图的不同通道和空间位置对任务的贡献是不平等的。在特征表示本身已足够均匀的任务中，其增益可能有限。
- **复现风险**：论文提到了代码和模型将公开，这降低了复现风险。但未提供的文本部分（如训练细节的全部超参数）可能需要参考其官方代码。
## 个人评论

1.  **提出了一个清晰且通用的设计原则**：通过将复杂的3D注意力图分解为顺序的1D通道注意力和2D空间注意力，并分别进行高效计算，为设计轻量级注意力模块提供了优秀范例。
2.  **重视并验证了池化操作的信息互补性**：明确指出平均池化（捕捉全局统计）和最大池化（捕捉显著性特征）对于理解特征都是重要的，并通过共享MLP融合它们来增强通道注意力，这一思想非常值得借鉴。
3.  **通过扎实的消融实验指导设计**：论文不是直接提出最终方案，而是系统性地对通道注意力、空间注意力和它们的组合方式进行了详尽的实验对比，每一步设计都有实验数据支撑，使结论更具说服力。
4.  **证明了“注意力”是提升网络性能的一个有效正交维度**：在深度、宽度、基数之外，注意力机制是另一个能有效提升模型表示能力的设计维度，且与前者结合能带来持续收益。

### 使用建议

- **如果快速了解**：阅读**摘要（Abstract）**、**引言（Introduction）** 的最后一段贡献总结，以及**实验（Experiments）** 部分的**主实验结果表格（Table 4）** 和**消融实验结论**。
- **如果复现**：重点精读**第3节（Convolutional Block Attention Module）** 的方法细节，特别是两个注意力模块的公式（Eq.2, Eq.3）和**图2（Fig. 2）**。同时，仔细阅读**4.1节消融实验**中关于超参数（如MLP的缩减比`r=16`，空间卷积核大小`k=7`）的选择。
- **如果借鉴创新点**：应学习其**将注意力分解为通道和空间并顺序应用的设计思路**，以及**在通道注意力中联合使用平均池化和最大池化的策略**。可以尝试将这种设计模式应用到自己的网络改进中。
- **如果写Related Work**：可以放在“注意力机制”或“网络结构设计/特征增强模块”的相关工作部分，与SENet、BAM等并列讨论。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中的注意力机制方向，特别是针对卷积神经网络（CNN）的特征增强模块。它解决的核心问题是：如何在不显著增加模型复杂度的前提下，通过引入轻量级的注意力机制，自适应地细化CNN的特征图，从而提升模型在图像分类和目标检测等任务上的性能与可解释性。该论文适合放在“注意力算子模块”这一主题下。

## 2. 一句话总结
本文提出了一个轻量级的卷积块注意力模块（CBAM），通过顺序地应用通道注意力和空间注意力，自适应地细化CNN的中间特征图，从而有效提升模型的表示能力和性能。

## 3. 背景与问题
- **为什么要做**：提升CNN性能的传统研究主要关注网络深度、宽度和基数（cardinality）。本文作者希望从一个不同的角度——“注意力”——来进一步增强网络的表示能力，使模型能更专注于重要特征并抑制无关信息。
- **之前方法的问题**：先前的注意力工作（如Squeeze-and-Excitation, SE模块）主要关注通道维度的注意力，使用了全局平均池化来聚合信息，但忽略了最大池化所能提供的关于显著特征的线索。同时，它们也完全缺失了空间维度的注意力，而空间注意力决定了“在哪里”聚焦，这对于视觉任务至关重要。
- **核心矛盾**：如何设计一个轻量、通用且高效的模块，能够同时利用通道和空间两个关键维度的注意力信息，以实现比仅使用单一维度注意力更优的特征细化效果。

## 4. 核心贡献
1.  提出了一个简单且高效的注意力模块——卷积块注意力模块（CBAM），它由两个顺序的子模块（通道注意力模块和空间注意力模块）构成，可广泛应用于增强各种CNN的表示能力。
2.  通过详尽的消融实验，验证了其设计选择的有效性，特别是证明了同时使用平均池化和最大池化的特征来计算通道注意力，以及顺序地（通道优先）组合两种注意力模块是最优策略。
3.  在多个标准基准（ImageNet-1K、MS COCO、VOC 2007）上，将CBAM应用于多种基础网络（ResNet、WideResNet、ResNeXt），均取得了显著的性能提升，证明了其广泛的适用性。

## 5. 方法详解
- **整体框架**：CBAM是一个即插即用的模块，旨在被嵌入到CNN的每个卷积块中（如图3所示）。它顺序地对输入特征图应用通道注意力模块和空间注意力模块，以生成细化的特征图。
- **输入输出**：输入是CNN中间层的一个三维特征图 \( F \in \mathbb{R}^{C \times H \times W} \)。输出是经过注意力加权后得到的细化特征图 \( F'' \in \mathbb{R}^{C \times H \times W} \)。
- **关键模块**：
    1.  **通道注意力模块 (Channel Attention Module)**：旨在学习“什么”是重要特征。它首先通过**平均池化（AvgPool）** 和**最大池化（MaxPool）** 两个操作，将输入特征图 \( F \) 的空间信息压缩，分别得到两个通道描述符 \( F_c^{avg} \) 和 \( F_c^{max} \)。这两个描述符被送入一个**共享的MLP**网络进行处理。MLP的输出通过逐元素求和合并，并经过Sigmoid激活函数，得到一维的通道注意力图 \( M_c \in \mathbb{R}^{C \times 1 \times 1} \)。
    2.  **空间注意力模块 (Spatial Attention Module)**：旨在学习“哪里”是重要区域。它首先对输入特征图（经过通道注意力细化后）沿通道维度进行**平均池化**和**最大池化**，得到两个二维的空间描述符 \( F_s^{avg} \) 和 \( F_s^{max} \)。这两个描述符被拼接（concatenate）起来，然后通过一个**卷积核大小为7x7的卷积层**进行处理，最后经过Sigmoid激活函数，得到二维的空间注意力图 \( M_s \in \mathbb{R}^{1 \times H \times W} \)。
- **模块连接**：两个子模块是**顺序连接**的。具体过程如下：
    \( F' = M_c(F) \otimes F \) （通道注意力加权）
    \( F'' = M_s(F') \otimes F' \) （空间注意力加权）
    其中 \( \otimes \) 表示逐元素相乘。在乘法操作中，注意力值会沿相应维度进行广播（broadcast）。
- **数学公式/机制直观解释**：
    - **通道注意力**：\( M_c(F) = \sigma(MLP(AvgPool(F)) + MLP(MaxPool(F))) \)。直观上，平均池化捕获了全局语义信息，而最大池化捕获了最具区分性的局部特征。使用共享的MLP处理它们，并将结果相加，能更全面地评估每个通道的重要性。
    - **空间注意力**：\( M_s(F) = \sigma(f^{7 \times 7}([AvgPool(F); MaxPool(F)])) \)。沿通道的平均和最大池化分别生成了不同侧重的空间摘要图，将它们拼接后用大卷积核（7x7）进行融合，能够综合信息并利用较大的感受野来决定重要的空间位置。
- **训练方式**：CBAM是端到端可训练的，可以与基础CNN架构无缝集成并联合训练。其引入的参数量和计算量（GFLOPs）增加非常微小，几乎可以忽略。
- **推理流程**：在推理时，输入特征图依次经过通道注意力图和空间注意力图的逐元素乘法调制，输出细化后的特征图。
- **和已有方法的差异**：
    1.  相比SE模块，CBAM不仅使用了通道注意力，还增加了空间注意力。
    2.  在通道注意力计算上，CBAM不仅使用了SE中的平均池化，还引入了最大池化，并通过共享MLP进行融合，从而获取更丰富的通道间关系信息。
    3.  相比同期的BAM模块，CBAM被设计在每一个卷积块中插入，而BAM则放置在网络的每个瓶颈层（bottleneck）。

## 6. 实验与结果
- **使用的数据集**：ImageNet-1K（图像分类）、MS COCO（目标检测）、VOC 2007（目标检测）。
- **对比方法**：主要对比基线网络（如ResNet系列）和先前的注意力方法SE。
- **评价指标**：分类任务使用Top-1和Top-5错误率；检测任务的指标在提供的文本中未明确列出（通常是mAP）。
- **主实验结果**：
    - 在ImageNet-1K上，将CBAM应用于多种网络均带来了一致提升。例如，ResNet50的Top-1错误率从24.56%降至22.66%；ResNet101的Top-1错误率从23.38%降至21.51%（p.9-10, Table 4）。
    - 在MS COCO和VOC 2007检测任务上，CBAM也验证了其有效性，尤其是通过在现有单阶段检测器上添加模块，在VOC2007测试集上取得了当时领先的性能（p.2）。
- **消融实验**：
    1.  **通道注意力**：对比了仅用平均池化（SE）、仅用最大池化、以及同时使用两者（CBAM的设计）。结果证明，结合平均和最大池化的方法（Top-1 Error 22.80%）优于单独使用任一方法，也优于SE（23.14%）（p.7, Table 1）。
    2.  **空间注意力**：对比了不同的空间描述符生成方式（通道池化 vs. 1x1卷积）和不同的后续卷积核大小（3x3 vs. 7x7）。结果表明，使用通道池化并搭配7x7卷积核的组合效果最佳（Top-1 Error 22.66%）（p.8, Table 2）。
    3.  **注意力模块组合方式**：对比了顺序（通道优先、空间优先）和并行两种组合策略。结果表明顺序组合优于并行，且通道优先的顺序效果略好（p.9, Table 3）。
- **泛化实验**：在ImageNet-1K上，CBAM在不同深度（ResNet-18/34/50/101）、不同宽度（WideResNet）和不同基数（ResNeXt）的多种网络架构上都取得了稳定提升，证明了其泛化能力（p.9-10, Table 4）。
- **效率信息**：CBAM引入的额外计算量很小。例如，在ResNet50上，参数量从25.56M增至28.09M（增加2.53M），GFLOPs从3.858增至3.864（增加0.006）（p.7, Table 1 & p.10, Table 4）。

## 7. 这篇论文真正有价值的地方
1.  **提出了一个清晰且通用的设计原则**：通过将复杂的3D注意力图分解为顺序的1D通道注意力和2D空间注意力，并分别进行高效计算，为设计轻量级注意力模块提供了优秀范例。
2.  **重视并验证了池化操作的信息互补性**：明确指出平均池化（捕捉全局统计）和最大池化（捕捉显著性特征）对于理解特征都是重要的，并通过共享MLP融合它们来增强通道注意力，这一思想非常值得借鉴。
3.  **通过扎实的消融实验指导设计**：论文不是直接提出最终方案，而是系统性地对通道注意力、空间注意力和它们的组合方式进行了详尽的实验对比，每一步设计都有实验数据支撑，使结论更具说服力。
4.  **证明了“注意力”是提升网络性能的一个有效正交维度**：在深度、宽度、基数之外，注意力机制是另一个能有效提升模型表示能力的设计维度，且与前者结合能带来持续收益。

## 8. 局限与问题
- **适用场景**：论文主要聚焦于图像分类和目标检测。其在其他视觉任务（如语义分割、姿态估计、视频理解）中的有效性在提供的文本中未提及。
- **实验充分性**：消融实验非常充分，但所有实验均在标准基准数据集上进行。对于更复杂或分布差异大的场景（如小样本、域适应），其效果未知。
- **数据集局限性**：实验验证了其在主流数据集上的性能，但未探讨其在极端不平衡数据或特定领域数据（如医学、遥感）上的表现。
- **计算成本**：虽然模块本身是轻量的，但将其嵌入网络的所有卷积块后，总增加的计算量是否在所有情况下都“可忽略”可能需要根据具体应用场景和硬件平台来评估。
- **假设依赖**：该方法的有效性依赖于一个基本假设：特征图的不同通道和空间位置对任务的贡献是不平等的。在特征表示本身已足够均匀的任务中，其增益可能有限。
- **复现风险**：论文提到了代码和模型将公开，这降低了复现风险。但未提供的文本部分（如训练细节的全部超参数）可能需要参考其官方代码。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：阅读**摘要（Abstract）**、**引言（Introduction）** 的最后一段贡献总结，以及**实验（Experiments）** 部分的**主实验结果表格（Table 4）** 和**消融实验结论**。
- **如果复现**：重点精读**第3节（Convolutional Block Attention Module）** 的方法细节，特别是两个注意力模块的公式（Eq.2, Eq.3）和**图2（Fig. 2）**。同时，仔细阅读**4.1节消融实验**中关于超参数（如MLP的缩减比`r=16`，空间卷积核大小`k=7`）的选择。
- **如果借鉴创新点**：应学习其**将注意力分解为通道和空间并顺序应用的设计思路**，以及**在通道注意力中联合使用平均池化和最大池化的策略**。可以尝试将这种设计模式应用到自己的网络改进中。
- **如果写Related Work**：可以放在“注意力机制”或“网络结构设计/特征增强模块”的相关工作部分，与SENet、BAM等并列讨论。

## 10. 和其他论文的关系
- **[[SENet]]**：CBAM可以看作是对SENet的扩展和改进，继承了其通道注意力思想，并增加了空间注意力模块，同时在通道注意力计算中引入了最大池化。
- **[[BAM]]**：论文明确提到了BAM作为同期工作，两者都将3D注意力分解为通道和空间部分。主要区别在于模块的放置位置（CBAM在每个卷积块，BAM在瓶颈层）。

## 11. 关键词
注意力机制，通道注意力，空间注意力，卷积神经网络，特征细化，Squeeze-and-Excitation，ImageNet，目标检测，轻量级模块，自适应特征，池化策略

## 12. 可信度说明
本精读笔记主要基于提供的PDF提取文本的前12页（共17页）生成。文本内容完整覆盖了摘要、引言、相关工作、方法（CBAM）的详细描述、以及实验部分的消融研究和主实验结果。提取的文本质量良好，文字连续可读。但需要注意，由于提取未包含图表（Fig. 1, 2, 3）的视觉信息，因此在“方法详解”部分对模块结构的描述主要基于文字和公式的理解，未包含图示的细节。总体而言，基于现有文本，已能准确把握论文的核心思想、方法、实验和贡献。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/CBAM.txt` (17/17 页; 原 AI 主体 12/17 + 全文补读 13-17); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Convolutional Block Attention Module 13
- p.13: 4.5 MS COCO Object Detection
- p.13: 4.6 VOC 2007 Object Detection
- p.13: For the experiment, we reproduce SSD and StairNet in our PyTorch platform
- p.14: 14 Woo, Park, Lee, Kweon
- p.14: CBAM favorably improves all the strong baselines with negligible additional
- p.14: 5 Conclusion
- p.14: We have presented the convolutional block attention module (CBAM), a new
- p.14: For the channel attention, we suggest to use the max-pooled features along with
- p.14: experiments with various state-of-the-art models and conﬁrmed that CBAM
- p.14: Acknowledgement
- p.15: Convolutional Block Attention Module 15

### 缺失页关键摘录

- p.13: The results are shown in the Table 6. We can clearly see that CBAM outperforms
- p.13: We conduct object detection on the Microsoft COCO dataset [ 3]. This dataset
- p.13: for evaluation. According to [ 39,40], we trained our model using all the training
- p.13: power, given by our module CBAM. As shown in the Table 7, we observe signiﬁ-
- p.13: For the experiment, we reproduce SSD and StairNet in our PyTorch platform
- p.13: The experimental results are summarized in Table 8. We can clearly see
- p.13: that CBAM improves the accuracy of all strong baselines with two backbone
- p.13: networks. Note that accuracy improvement of CBAM comes with a negligible
- p.13: increment but because of our eﬀective feature reﬁnement. In addition, the result
- p.14: Table 7: Object detection mAP(%) on the MS COCO validation set . We
- p.14: Table 8: Object detection mAP(%) on the VOC 2007 test set . We adopt
- p.14: outperforms all the baselines on three diﬀerent benchmark datasets: ImageNet-
<!-- AI_READING_NOTE_END -->
