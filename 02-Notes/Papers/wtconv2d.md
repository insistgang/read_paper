---
title: Wavelet Convolutions for Large Receptive Fields
authors:
  - "Shahaf E. Finder"
  - "Roy Amoyal"
  - "Eran Treister"
  - "Oren Freifeld"
year: 2024
venue: "arXiv"
doi: 
pdf: [[wtconv2d.pdf]]
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
extract_cache: .paper-cache/extracts/wtconv2d.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/27 pages"
---
# Wavelet Convolutions for Large Receptive Fields

## 基本信息
- **PDF**: [[wtconv2d.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Wavelet Convolutions for Large Receptive Fields |
| **作者** | Shahaf E. Finder; Roy Amoyal; Eran Treister; Oren Freifeld |
| **发表时间** | 2024 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> In recent years, there have been attempts to increase the kernel size of Convolutional Neural Nets (CNNs) to mimic the global receptivefieldofVisionTransformers’(ViTs)self-attentionblocks.That approach,however,quicklyhitanupperboundandsaturatedwaybefore achieving a global receptive field. In this work, we demonstrate that by leveragingtheWaveletTransform(WT),itis,infact,possibletoobtain very large receptive fields without suffering from over-parameterization, e.g., for a k×k receptive field, the number of trainable parameters in the proposed method grows only logarithmically with k. The proposed layer, named WTConv, can be used as a drop-in replacement in exist- ing architectures, results in an effective multi-frequency response, and scalesgracefullywiththesizeofthereceptivefield.Wedemonstratethe effectiveness of the WTConv layer within ConvNeXt and MobileNetV2 architectures for image classification, as well as backbones for down- streamtasks,andshowityieldsadditionalpropertiessuchasro

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：近年来，Vision Transformers（ViTs）凭借其自注意力层带来的全局感受野，在多项任务上展现出对CNN的优势。这促使研究者尝试通过增大CNN的卷积核尺寸来弥补差距，但这种方法迅速遇到瓶颈（性能饱和，参数量过大），难以实现真正的全局感受野。
- **之前方法的问题**：1）简单地增大卷积核（如超过7×7）会导致性能下降（Liu et al. [38]）；2）一些改进的大核方法（如RepLKNet [11]）虽然有效，但参数量增长仍是平方级的，限制了其扩展到真正的全局感受野；3）在频域操作的方法（如GFNet [47]）虽然能达到全局感受野，但完全丧失了局部信息，且通常对输入尺寸有固定要求。
- **核心矛盾**：如何在不过度增加参数量（避免过参数化）的情况下，有效地获得非常大的感受野（甚至全局），并同时改善CNN对图像低频成分（形状）的响应能力。
## 关键贡献

1.  **提出了WTConv层**：一种利用级联小波变换（Wavelet Transform, WT）分解和小卷积核的新型卷积层，能在不同频带进行操作。
2.  **设计为即插即用模块**：WTConv被设计为深度可分离卷积（depth-wise convolution）的直接替代品，可以无缝集成到现有的CNN架构（如ConvNeXt, MobileNetV2）中。
3.  **高效的参数缩放特性**：对于 k×k 的感受野，WTConv的可训练参数量仅随k呈对数增长，而非平方增长。
4.  **全面的实证验证**：在图像分类（ImageNet-1K）、语义分割（ADE20K）和目标检测（COCO）等多个关键视觉任务上，证明了WTConv的有效性。
5.  **分析了WTConv带来的额外优势**：包括提升模型的可扩展性、对图像损坏的鲁棒性，以及增强形状偏好（shape-bias）而非纹理偏好。
## 方法

- **整体框架**：WTConv的核心思想是将输入特征图通过小波变换（WT）分解为多个不同频率的子带（subbands），然后对每个子带应用小卷积核，最后通过逆小波变换（IWT）将结果合成。这个过程是递归的，可以级联多层以覆盖更大的感受野。
- **输入输出**：输入是一个特征图张量 X。输出是经过WTConv层处理后的特征图 Y。
- **关键模块**：
    1.  **小波变换（WT）**：论文采用高效的哈尔（Haar）小波。一级2D Haar WT通过一个步长为2的深度卷积实现，使用四个滤波器（f_LL, f_LH, f_HL, f_HH）将输入分解为一个低频分量（X_LL）和三个高频分量（X_LH, X_HL, X_HH），每个分量的空间尺寸是输入的一半。
    2.  **卷积操作**：对每个分解后的频带（包括低频和所有高频）应用一个固定的、小尺寸（如3×3或5×5）的深度卷积核 W。
    3.  **逆小波变换（IWT）**：使用转置卷积将卷积后的频带分量重新合成为空间域特征。
- **模块连接与递归机制**：WTConv采用级联结构（如公式6-8和图3所示）。首先对输入进行WT分解，得到不同频带的分量。然后，对当前层级的所有频带（低频和高频）施加卷积。其中，当前层的**低频分量会再次进行WT分解**，进入下一层级进行更深入的频域操作和更大范围的感受野覆盖。最后，从最深层开始，将卷积结果通过IWT逐级向上合成，并与上一层对应频带的卷积结果相加，最终得到输出。
- **数学机制直观解释**：在更高层级的WT中，一个3×3的卷积核作用于一个低频分量上，该低频分量本身对应原始输入中更大的空间区域（例如，第二层的低频分量对应原始输入中约4×4的区域）。因此，一个在第二层低频分量上的3×3卷积，在原始输入上的等效感受野约为 12×12（(3*2^2) × (3*2^2)）。
- **训练与推理**：论文未在前12页中详细说明特殊的训练或推理策略。从上下文推断，WTConv作为标准层替换原有深度卷积层，训练过程与原网络（如ConvNeXt）一致。
- **与已有方法的差异**：
    1.  vs. 大核卷积（如RepLK [11]）：WTConv的参数增长是对数级的，而非平方级，因此可以更高效地扩展到极大感受野。
    2.  vs. 基于傅里叶变换的方法（如GFNet [47]）：WT在分解时保留了空间局部信息，使得在频域中进行的卷积（局部操作）仍有意义，而傅里叶变换是全局的，失去了局部交互能力。
    3.  vs. 同类小波方法（如[15]）：本文的WTConv是一个通用的、轻量化的即插即用层，可以轻松集成到任何使用深度可分离卷积的网络中，而其他方法通常是高度定制化的架构。
- **论文类型特化（注意力类模块）**：
    - **作用维度**：WTConv在**多尺度频域**维度进行操作。它通过小波变换将输入分解到不同频率带（对应不同的空间尺度），在每个频带上独立进行特征混合（卷积），最后合成。
    - **可插入网络**：被设计为深度可分离卷积的**直接替代品**，可插入任何使用该操作的CNN骨干网络中。
    - **计算量 vs 效果**：论文在计算成本分析（§3.4）中指出，对于相同感受野，WTConv的FLOPs通常低于对应的大核深度卷积。例如，对于512×512输入，WTConv（3级，5×5核，感受野40×40）的FLOPs约为17.9M，而标准31×31深度卷积为252M。实验结果表明，这种计算量的节省带来了准确率的提升（效果更好）。
## 实验

- **使用的数据集**：
    - **图像分类**：ImageNet-1K (§4.1)
    - **语义分割**：ADE20K (§4.2)
    - **目标检测**：COCO (§4.3)
- **对比方法**：ConvNeXt（基准）、Swin Transformer、RepLKNet、SLaK、VAN、GFNet等。
- **评价指标**：图像分类使用Top-1准确率；语义分割使用平均交并比（mIoU）；目标检测使用边界框AP（AP^box）和掩码AP（AP^mask）。
- **主实验结果**：
    - **ImageNet-1K 分类 (120 epochs, Table 1)**：WTConvNeXt-T达到**81.7%** Top-1，优于所有对比方法（如RepLK的81.5%，SLaK的81.5%），且参数量（2.04M）显著低于RepLK（3.84M）和GFNet（4.29M）。
    - **ImageNet-1K 分类 (300 epochs, Table 2)**：WTConvNeXt-T/S/B分别达到**82.5%/83.6%/84.1%** Top-1，均高于同规模的ConvNeXt和Swin Transformer。例如，WTConvNeXt-T比ConvNeXt-T提升0.4%（82.1% -> 82.5%），而参数和FLOPs增加很小。
    - **ADE20K 语义分割 (Table 3)**：WTConvNeXt-T作为骨干，在UperNet上取得**45.4%/46.6%** mIoU（120e/300e预训练），比ConvNeXt-T（44.6%/46.0%）有稳定提升。
    - **COCO 目标检测 (Table 4)**：在Cascade Mask R-CNN框架下，WTConvNeXt-T/S均优于ConvNeXt。例如，WTConvNeXt-T（300e预训练，3x微调）在AP^box上达到**51.0%**，比ConvNeXt-T的50.4%提升0.6。
- **消融实验**：PDF前12页文本中未明确提及系统的消融实验。
- **泛化实验**：论文在摘要和引言中提到WTConv能提升模型对图像损坏的鲁棒性和形状偏好，并在§3.3和§4.4中提及会进行分析，但具体分析结果在提供的文本范围内未找到。
- **效率信息**：
    - **参数量**：WTConvNeXt-T/S/B分别为30M/54M/93M，比对应ConvNeXt分别增加约1M/4M/4M。
    - **FLOPs**：WTConvNeXt-T/S/B分别为4.5G/8.8G/15.5G，与对应ConvNeXt（4.5G/8.7G/15.4G）几乎持平。
    - **感受野**：WTConv通过设置不同层级和核大小，在ConvNeXt各阶段实现了非常大的感受野（如[160,80,40,20]），远大于原7×7卷积。
## 局限

- **场景局限性**：方法基于标准CNN架构，对于本身具有全局感受野的Transformer架构，其改进效果未知。对于极端大尺寸（如4K以上）的图像，其感受野扩展和计算成本是否依然最优未被验证。
- **实验充分性**：提供的文本（前12页）中缺乏深入的消融实验，例如不同小波基（Haar vs. 其他）、级联层级数、卷积核大小等超参数的影响分析。对“形状偏好”和“鲁棒性”的详细分析在所提供的文本中未完全展开。
- **数据集范围**：实验仅涵盖分类、分割和检测三大任务，未涉及视频理解、3D视觉、生成模型等其他领域。
- **假设依赖**：方法的高效性依赖于使用可高效实现的Haar小波。如果使用更复杂的小波基，计算成本可能会增加。
- **复现风险**：算法实现细节（如权重初始化、通道缩放因子的设置）在附录A中，需要参考。论文声称代码已开源（GitHub链接），这降低了复现风险。
## 个人评论

这篇论文最值得学习的点是其**将经典的信号处理工具（小波变换）与现代深度学习架构优雅结合**的思路。它没有发明复杂的新模块，而是找到了一个已有的数学工具（WT）来解决CNN的一个本质痛点（感受野与参数量的矛盾）。这种“老工具新用”的思路极具启发性。它证明了**在频域（特别是多尺度频域）进行特征操作**可以作为一种有效的、与空间域或通道域注意力并行的特征混合维度。此外，它**强调了模型归纳偏置（如形状偏好）可以通过网络结构设计来引导**，而不仅仅是依赖数据。对于后续研究，这意味着可以探索其他频域变换（如更复杂的小波基）或设计更高效的多尺度频域注意力机制。对于改模型，它提供了一个极其轻量且有效的即插即用模块来增强现有CNN。

### 使用建议

- **快速了解**：阅读**摘要**、**引言**（1. Introduction）的最后两段和**实验**（4. Results）中的主表格（Table 1-4）。这些部分能快速抓住论文的核心思想、贡献和效果。
- **复现**：重点阅读**方法**（3. Method）部分，特别是公式(1)-(8)和图3，以及**附录A**（算法描述）。同时需参考其开源代码以了解具体实现细节（如权重初始化、训练超参）。
- **借鉴创新点**：
    1.  学习其**模块设计思想**：如何将多尺度频域分解（WT）与局部卷积结合，实现“小核大感受野”。
    2.  学习其**即插即用模块的评估范式**：在强大的基准架构（ConvNeXt）上替换关键组件，并在多个标准任务上验证。
    3.  关注其**对模型归纳偏置（形状偏好）的分析视角**，可用于自己工作的分析部分。
- **写Related Work**：可将此工作放在以下类别中进行讨论：
    - **大核卷积与CNN感受野扩展**（与RepLK, SLaK等并列）。
    - **频域/信号处理在CNN中的应用**（与基于FFT的方法如GFNet并列）。
    - **轻量化与高效的注意力/混合机制**。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉领域，具体是卷积神经网络（CNN）的优化方向。它聚焦于解决CNN感受野有限的问题，通过引入信号处理工具（小波变换）来设计一种新的卷积层（WTConv），以有效地扩大感受野并提升模型对低频信号（如形状）的响应能力。论文主题为“注意力算子模块”，因为它提出了一种替代传统深度可分离卷积的算子，旨在增强CNN的全局特征混合能力，类似于ViT中注意力机制的效果。

## 2. 一句话总结
本文提出了一种基于小波变换的卷积层WTConv，它通过在多尺度频域上应用小卷积核，能够以对数级增长的参数量实现指数级增长的感受野，从而有效提升CNN的性能并赋予其对图像形状更强的偏好。

## 3. 背景与问题
- **为什么要做**：近年来，Vision Transformers（ViTs）凭借其自注意力层带来的全局感受野，在多项任务上展现出对CNN的优势。这促使研究者尝试通过增大CNN的卷积核尺寸来弥补差距，但这种方法迅速遇到瓶颈（性能饱和，参数量过大），难以实现真正的全局感受野。
- **之前方法的问题**：1）简单地增大卷积核（如超过7×7）会导致性能下降（Liu et al. [38]）；2）一些改进的大核方法（如RepLKNet [11]）虽然有效，但参数量增长仍是平方级的，限制了其扩展到真正的全局感受野；3）在频域操作的方法（如GFNet [47]）虽然能达到全局感受野，但完全丧失了局部信息，且通常对输入尺寸有固定要求。
- **核心矛盾**：如何在不过度增加参数量（避免过参数化）的情况下，有效地获得非常大的感受野（甚至全局），并同时改善CNN对图像低频成分（形状）的响应能力。

## 4. 核心贡献
1.  **提出了WTConv层**：一种利用级联小波变换（Wavelet Transform, WT）分解和小卷积核的新型卷积层，能在不同频带进行操作。
2.  **设计为即插即用模块**：WTConv被设计为深度可分离卷积（depth-wise convolution）的直接替代品，可以无缝集成到现有的CNN架构（如ConvNeXt, MobileNetV2）中。
3.  **高效的参数缩放特性**：对于 k×k 的感受野，WTConv的可训练参数量仅随k呈对数增长，而非平方增长。
4.  **全面的实证验证**：在图像分类（ImageNet-1K）、语义分割（ADE20K）和目标检测（COCO）等多个关键视觉任务上，证明了WTConv的有效性。
5.  **分析了WTConv带来的额外优势**：包括提升模型的可扩展性、对图像损坏的鲁棒性，以及增强形状偏好（shape-bias）而非纹理偏好。

## 5. 方法详解
- **整体框架**：WTConv的核心思想是将输入特征图通过小波变换（WT）分解为多个不同频率的子带（subbands），然后对每个子带应用小卷积核，最后通过逆小波变换（IWT）将结果合成。这个过程是递归的，可以级联多层以覆盖更大的感受野。
- **输入输出**：输入是一个特征图张量 X。输出是经过WTConv层处理后的特征图 Y。
- **关键模块**：
    1.  **小波变换（WT）**：论文采用高效的哈尔（Haar）小波。一级2D Haar WT通过一个步长为2的深度卷积实现，使用四个滤波器（f_LL, f_LH, f_HL, f_HH）将输入分解为一个低频分量（X_LL）和三个高频分量（X_LH, X_HL, X_HH），每个分量的空间尺寸是输入的一半。
    2.  **卷积操作**：对每个分解后的频带（包括低频和所有高频）应用一个固定的、小尺寸（如3×3或5×5）的深度卷积核 W。
    3.  **逆小波变换（IWT）**：使用转置卷积将卷积后的频带分量重新合成为空间域特征。
- **模块连接与递归机制**：WTConv采用级联结构（如公式6-8和图3所示）。首先对输入进行WT分解，得到不同频带的分量。然后，对当前层级的所有频带（低频和高频）施加卷积。其中，当前层的**低频分量会再次进行WT分解**，进入下一层级进行更深入的频域操作和更大范围的感受野覆盖。最后，从最深层开始，将卷积结果通过IWT逐级向上合成，并与上一层对应频带的卷积结果相加，最终得到输出。
- **数学机制直观解释**：在更高层级的WT中，一个3×3的卷积核作用于一个低频分量上，该低频分量本身对应原始输入中更大的空间区域（例如，第二层的低频分量对应原始输入中约4×4的区域）。因此，一个在第二层低频分量上的3×3卷积，在原始输入上的等效感受野约为 12×12（(3*2^2) × (3*2^2)）。
- **训练与推理**：论文未在前12页中详细说明特殊的训练或推理策略。从上下文推断，WTConv作为标准层替换原有深度卷积层，训练过程与原网络（如ConvNeXt）一致。
- **与已有方法的差异**：
    1.  vs. 大核卷积（如RepLK [11]）：WTConv的参数增长是对数级的，而非平方级，因此可以更高效地扩展到极大感受野。
    2.  vs. 基于傅里叶变换的方法（如GFNet [47]）：WT在分解时保留了空间局部信息，使得在频域中进行的卷积（局部操作）仍有意义，而傅里叶变换是全局的，失去了局部交互能力。
    3.  vs. 同类小波方法（如[15]）：本文的WTConv是一个通用的、轻量化的即插即用层，可以轻松集成到任何使用深度可分离卷积的网络中，而其他方法通常是高度定制化的架构。
- **论文类型特化（注意力类模块）**：
    - **作用维度**：WTConv在**多尺度频域**维度进行操作。它通过小波变换将输入分解到不同频率带（对应不同的空间尺度），在每个频带上独立进行特征混合（卷积），最后合成。
    - **可插入网络**：被设计为深度可分离卷积的**直接替代品**，可插入任何使用该操作的CNN骨干网络中。
    - **计算量 vs 效果**：论文在计算成本分析（§3.4）中指出，对于相同感受野，WTConv的FLOPs通常低于对应的大核深度卷积。例如，对于512×512输入，WTConv（3级，5×5核，感受野40×40）的FLOPs约为17.9M，而标准31×31深度卷积为252M。实验结果表明，这种计算量的节省带来了准确率的提升（效果更好）。

## 6. 实验与结果
- **使用的数据集**：
    - **图像分类**：ImageNet-1K (§4.1)
    - **语义分割**：ADE20K (§4.2)
    - **目标检测**：COCO (§4.3)
- **对比方法**：ConvNeXt（基准）、Swin Transformer、RepLKNet、SLaK、VAN、GFNet等。
- **评价指标**：图像分类使用Top-1准确率；语义分割使用平均交并比（mIoU）；目标检测使用边界框AP（AP^box）和掩码AP（AP^mask）。
- **主实验结果**：
    - **ImageNet-1K 分类 (120 epochs, Table 1)**：WTConvNeXt-T达到**81.7%** Top-1，优于所有对比方法（如RepLK的81.5%，SLaK的81.5%），且参数量（2.04M）显著低于RepLK（3.84M）和GFNet（4.29M）。
    - **ImageNet-1K 分类 (300 epochs, Table 2)**：WTConvNeXt-T/S/B分别达到**82.5%/83.6%/84.1%** Top-1，均高于同规模的ConvNeXt和Swin Transformer。例如，WTConvNeXt-T比ConvNeXt-T提升0.4%（82.1% -> 82.5%），而参数和FLOPs增加很小。
    - **ADE20K 语义分割 (Table 3)**：WTConvNeXt-T作为骨干，在UperNet上取得**45.4%/46.6%** mIoU（120e/300e预训练），比ConvNeXt-T（44.6%/46.0%）有稳定提升。
    - **COCO 目标检测 (Table 4)**：在Cascade Mask R-CNN框架下，WTConvNeXt-T/S均优于ConvNeXt。例如，WTConvNeXt-T（300e预训练，3x微调）在AP^box上达到**51.0%**，比ConvNeXt-T的50.4%提升0.6。
- **消融实验**：PDF前12页文本中未明确提及系统的消融实验。
- **泛化实验**：论文在摘要和引言中提到WTConv能提升模型对图像损坏的鲁棒性和形状偏好，并在§3.3和§4.4中提及会进行分析，但具体分析结果在提供的文本范围内未找到。
- **效率信息**：
    - **参数量**：WTConvNeXt-T/S/B分别为30M/54M/93M，比对应ConvNeXt分别增加约1M/4M/4M。
    - **FLOPs**：WTConvNeXt-T/S/B分别为4.5G/8.8G/15.5G，与对应ConvNeXt（4.5G/8.7G/15.4G）几乎持平。
    - **感受野**：WTConv通过设置不同层级和核大小，在ConvNeXt各阶段实现了非常大的感受野（如[160,80,40,20]），远大于原7×7卷积。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的点是其**将经典的信号处理工具（小波变换）与现代深度学习架构优雅结合**的思路。它没有发明复杂的新模块，而是找到了一个已有的数学工具（WT）来解决CNN的一个本质痛点（感受野与参数量的矛盾）。这种“老工具新用”的思路极具启发性。它证明了**在频域（特别是多尺度频域）进行特征操作**可以作为一种有效的、与空间域或通道域注意力并行的特征混合维度。此外，它**强调了模型归纳偏置（如形状偏好）可以通过网络结构设计来引导**，而不仅仅是依赖数据。对于后续研究，这意味着可以探索其他频域变换（如更复杂的小波基）或设计更高效的多尺度频域注意力机制。对于改模型，它提供了一个极其轻量且有效的即插即用模块来增强现有CNN。

## 8. 局限与问题
- **场景局限性**：方法基于标准CNN架构，对于本身具有全局感受野的Transformer架构，其改进效果未知。对于极端大尺寸（如4K以上）的图像，其感受野扩展和计算成本是否依然最优未被验证。
- **实验充分性**：提供的文本（前12页）中缺乏深入的消融实验，例如不同小波基（Haar vs. 其他）、级联层级数、卷积核大小等超参数的影响分析。对“形状偏好”和“鲁棒性”的详细分析在所提供的文本中未完全展开。
- **数据集范围**：实验仅涵盖分类、分割和检测三大任务，未涉及视频理解、3D视觉、生成模型等其他领域。
- **假设依赖**：方法的高效性依赖于使用可高效实现的Haar小波。如果使用更复杂的小波基，计算成本可能会增加。
- **复现风险**：算法实现细节（如权重初始化、通道缩放因子的设置）在附录A中，需要参考。论文声称代码已开源（GitHub链接），这降低了复现风险。

## 9. 我该怎么使用这篇论文
- **快速了解**：阅读**摘要**、**引言**（1. Introduction）的最后两段和**实验**（4. Results）中的主表格（Table 1-4）。这些部分能快速抓住论文的核心思想、贡献和效果。
- **复现**：重点阅读**方法**（3. Method）部分，特别是公式(1)-(8)和图3，以及**附录A**（算法描述）。同时需参考其开源代码以了解具体实现细节（如权重初始化、训练超参）。
- **借鉴创新点**：
    1.  学习其**模块设计思想**：如何将多尺度频域分解（WT）与局部卷积结合，实现“小核大感受野”。
    2.  学习其**即插即用模块的评估范式**：在强大的基准架构（ConvNeXt）上替换关键组件，并在多个标准任务上验证。
    3.  关注其**对模型归纳偏置（形状偏好）的分析视角**，可用于自己工作的分析部分。
- **写Related Work**：可将此工作放在以下类别中进行讨论：
    - **大核卷积与CNN感受野扩展**（与RepLK, SLaK等并列）。
    - **频域/信号处理在CNN中的应用**（与基于FFT的方法如GFNet并列）。
    - **轻量化与高效的注意力/混合机制**。

## 10. 和其他论文的关系
根据提供的论文主题“B_注意力算子模块”，这篇WTConv论文可以视为对该主题的一个重要贡献，它提出了一种基于多尺度频域的特征混合算子，作为传统空间卷积和通道注意力的补充或替代。它可能与该主题下其他关于设计高效大感受野模块（如RepLKNet [[RepLKNet]]）或探索频域特征处理（如GFNet [[GFNet]]）的论文有直接关联。但由于当前知识库中仅提供了该论文的文件名（wtconv2d.pdf），无法确定其他具体论文，因此暂不建立不确定的双链。

## 11. 关键词
Wavelet Transform (WT), Receptive Field, Convolutional Neural Networks (CNNs), Depth-wise Convolution, Multi-frequency Representation, Shape Bias, Drop-in Replacement, Vision Transformers (ViTs), Computational Efficiency

## 12. 可信度说明
本精读笔记完全基于用户提供的PDF提取文本（论文前12页）生成。笔记中所有具体的方法描述、公式、数字和结论均严格引用自该文本。提取的文本质量良好，清晰覆盖了论文的摘要、引言、相关工作、方法主体和实验结果的核心部分。需要说明的是，对于附录、方法部分的算法伪代码细节、以及第4.4节的详细分析，文本并未提供，因此相关结论（如具体的鲁棒性、形状偏好分析）未在本笔记中展开。实验结果部分，所有关键数字均从提供的文本表格中准确抄录。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/wtconv2d.txt` (27/27 页; 原 AI 主体 12/27 + 全文补读 13-27); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-27; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-27。
- **提取情况**: 缺失页 15 页, 其中 15 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Wavelet Convolutions for Large Receptive Fields 13
- p.13: ConvNeXt-T
- p.13: ConvNeXt-S
- p.13: ConvNeXt-B
- p.13: WTConvNeXt-T
- p.13: WTConvNeXt-S
- p.13: WTConvNeXt-B
- p.14: 5 Limitations
- p.14: Although the WTConv layer does not require many FLOPs, its running time
- p.14: 6 Conclusion
- p.14: In this work, we utilize wavelet transforms to introduce WTConv, a drop-in re-
- p.15: Wavelet Convolutions for Large Receptive Fields 15

### 缺失页关键摘录

- p.13: as the size of the receptive field induced by the layer. The empirical evaluation
- p.13: the last layer. The result is visualized in Fig. 1, where high-contribution pixels
- p.13: Ablation Study. We conduct an ablation study to see how different configu-
- p.13: rations of the WTConv layer impact the final result. We train WTConvNeXt-T
- p.13: tions. First, we experiment with different combinations of WT levels and ker-
- p.14: Table 8 shows the results of all the described configurations. Here, increas-
- p.14: Table 8: Ablation study with WTConvNeXt-T. Comparing different configurations of
- p.14: Although the WTConv layer does not require many FLOPs, its running time
- p.15: 6. Contributors, M.: MMDetection: Openmmlab detection toolbox and benchmark.
- p.15: and benchmark. https://github.com/open-mmlab/mmsegmentation (2020)
- p.19: mantic understanding of scenes through the ade20k dataset. International Journal
- p.21: warmup of 50 batches. Table 9 presents the throughput, measured in images per
<!-- AI_READING_NOTE_END -->
