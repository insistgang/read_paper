---
title: Rethinking Convolutional Neural Networks for
authors:
  - "Ionut Cosmin Duta"
  - "Li Liu"
  - "Fan Zhu"
  - "Ling Shao"
year: 2020
venue: "arXiv"
doi: 
pdf: [[PyConv.pdf]]
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
extract_cache: .paper-cache/extracts/PyConv.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/16 pages"
---
# Rethinking Convolutional Neural Networks for

## 基本信息
- **PDF**: [[PyConv.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Rethinking Convolutional Neural Networks for |
| **作者** | Ionut Cosmin Duta; Li Liu; Fan Zhu; Ling Shao |
| **发表时间** | 2020 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Thisworkintroducespyramidalconvolution(PyConv),whichiscapableofprocess- ingtheinputatmultiplefilterscales. PyConvcontainsapyramidofkernels,where eachlevelinvolvesdifferenttypesoffilterswithvaryingsizeanddepth,whichare abletocapturedifferentlevelsofdetailsinthescene. Ontopoftheseimproved recognition capabilities, PyConv is also efficient and, with our formulation, it does not increase the computational cost and parameters compared to standard convolution. Moreover,itisveryflexibleandextensible,providingalargespaceof potentialnetworkarchitecturesfordifferentapplications. PyConvhasthepotential toimpactnearlyeverycomputervisiontaskand,inthiswork,wepresentdifferent architecturesbasedonPyConvforfourmaintasksonvisualrecognition: image classification,videoactionclassification/recognition,objectdetectionandsemantic imagesegmentation/parsing. Ourapproachshowssignificantimprovementsover allthesecoretasksincomparisonwiththebaselines. Forinstance,onimagerecog- nition,our50-layersnetworkoutperformsi

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

*   **为什么要做**：标准卷积神经网络（CNN）通常使用小尺寸卷积核（如3x3），为了扩大感受野，不得不依赖于堆叠小卷积核和逐步下采样。然而，研究表明网络的理论感受野远大于其实际有效感受野。此外，在获得足够上下文信息之前就进行下采样，会丢失对识别复杂场景中有用的空间细节（如不同大小、部分遮挡的目标）。
*   **之前方法的问题**：标准卷积核尺寸单一，无法直接、高效地处理图像中物体的巨大尺度变化。虽然存在如Squeeze-and-Excitation、Non-local blocks等模块来捕获上下文，但它们是附加模块，通常会显著增加模型参数和计算复杂度，且仍需要空间卷积作为基础。
*   **作者想解决的核心矛盾**：如何在**不增加计算成本和参数量**的前提下，让卷积算子本身具备**多尺度并行处理能力**，从而更早、更有效地捕获从局部细节到全局上下文的丰富信息。
## 关键贡献

1.  **提出了金字塔卷积（PyConv）模块**：该模块包含一个卷积核金字塔，随着核尺寸（如3x3, 5x5, 7x7, 9x9）的增加，核的深度（通道连接数）相应减少。这种设计使得PyConv能在并行处理多尺度信息的同时，维持与单一小核标准卷积相似的参数量和计算量。
2.  **设计了用于图像分类的PyConvResNet架构**：将PyConv集成到残差瓶颈块中，构建了PyConvResNet网络。该网络在ImageNet上，其50层版本在性能上超越了152层的ResNet基线，且参数更少（少2.39倍）、计算量更低（少2.52倍）、网络层数更少。
3.  **提出了用于语义分割的PyConv解析头（PyConvPH）**：设计了一种包含局部和全局PyConv块的解析头，用于高效地聚合从局部细节到全局语义的多尺度上下文信息。基于此框架（PyConvSegNet）在ADE20K场景解析基准上取得了当时的最佳性能。
4.  **展示了PyConv在多种视觉任务上的通用性和有效性**：在目标检测和视频动作识别等任务上应用基于PyConv的架构，并报告了相对于基线的显著性能提升。
## 方法

*   **整体框架与输入输出**：PyConv并非一个独立的网络，而是一个可替换标准卷积的**基础算子模块**。其输入为上一层的特征图（尺寸为H×W×FMi），输出为多尺度聚合后的特征图（尺寸为H×W×FMo）。
*   **关键模块（PyConv的核心机制）**：
    1.  **金字塔结构**：PyConv包含`n`个层级。从第1层到第n层，卷积核的空间尺寸`K`逐渐增大（如`K1`到`Kn`），而核的深度（即分组数`G`）逐渐增加，导致每个分组内的通道连接数（核深度）`FMi/G`逐渐减小。这形成了一个“双向金字塔”：一个金字塔（空间尺寸）底大顶小，另一个金字塔（核深度）底小顶大。
    2.  **分组卷积实现**：为了实现不同层级的核深度，输入特征图`FMi`在每个层级被均匀分成若干组（`G`组），然后独立地对每组应用对应尺寸的卷积核。分组数`G`的增大降低了连接性，从而在增大核尺寸的同时控制了计算量。
    3.  **并行与合并**：所有`n`个层级在输入特征图上并行计算，各自产生一组输出特征图（`FMo1, FMo2, ..., FMon`），最后将这些输出在通道维度上拼接，形成最终的输出特征图`FMo`。
*   **数学公式与直观解释**：标准卷积的计算量为 `FLOPs = K² × FMi × FMo × H × W`。PyConv的计算量由公式(1)给出，是各层级计算量之和。作者通过精心设计（如令每层输出的特征图数`FMoi`与`K²`成反比），使得PyConv的总计算量与使用最小核`K1`的标准卷积相当。直观上，PyConv让网络用“细密连接的小核”看细节，同时用“粗略连接的大核”看全局，两者并行互补。
*   **和已有方法的差异**：与标准卷积相比，PyConv具备内在的多尺度处理能力。与额外的上下文模块（如SE、Non-local）相比，PyConv是一个替代基础卷积的算子，不引入额外的插入式模块，且能保持计算效率。
*   **在具体任务中的应用**：
    *   **图像分类**：将PyConv嵌入ResNet的瓶颈结构中（见图4）。作者还创新地将最大池化层从网络前端移至第一个残差块的短连接上，使PyConv能在更高分辨率的特征图上进行多尺度下采样。
    *   **语义分割**：设计PyConv解析头（PyConvPH），包含一个**局部PyConv块**（用于捕获局部细节）和一个**全局PyConv块**（结合自适应平均池化捕获全局上下文），两者输出拼接后用于最终分类。该头取代了PSPNet中的金字塔池化模块（PPM）或DeepLab中的ASPP模块。
## 实验

*   **使用的数据集**：ImageNet（图像分类）、ADE20K（语义分割）、以及附录中提及的用于目标检测和视频分类的相应数据集（PDF文本中未具体列出后两者的名称）。
*   **对比方法**：主要基线是ResNet系列（如ResNet-50, ResNet-152）。在语义分割中，还与PSPNet（使用PPM）和使用ASPP的模型进行了比较。
*   **评价指标**：图像分类使用Top-1和Top-5准确率；语义分割使用平均交并比（mIo）和像素准确率。
*   **主实验结果**：
    *   **图像分类**：PyConvResNet-50在ImageNet上Top-1准确率**22.1%**（误差），优于ResNet-50的**23.9%**，并超越了更深的ResNet-152（**21.7%**），同时参数量（**24.85M** vs 60.19M）和FLOPs（**3.88G** vs 11.58G）大幅降低。
    *   **语义分割**：基于PyConvResNet-50和PyConvPH的框架在ADE20K验证集上达到**44.6%** mIo，优于PSPNet和DeepLab v3等方法，**设置了新的state-of-the-art**。
*   **消融实验**：PDF文本中未提供详细的消融实验表格，但讨论了不同PyConv设置（如层级数、分组数、每层输出特征图数）对性能的影响，强调了其灵活性。
*   **泛化实验**：论文展示了在图像分类、语义分割、目标检测、视频动作识别四个核心视觉任务上的改进，证明了PyConv的泛化能力。
*   **效率信息**：论文提供了详细的参数量（# params）和计算量（FLOPs）比较。例如，PyConvResNet-50比ResNet-50参数少约2.39倍，FLOPs低约2.52倍，同时性能更优。
## 局限

1.  **超参数调整**：PyConv的具体配置（如每层的核尺寸、分组数、输出通道数）是一个设计空间，论文提供了指导原则（如使用2的幂次），但针对特定任务找到最优配置可能需要实验搜索，增加了设计复杂度。
2.  **分组卷积的固有局限**：PyConv依赖于分组卷积，这可能会限制不同分组之间的特征交互。虽然论文通过金字塔结构中的不同连接度进行了弥补，但这是否是最佳的平衡点值得探讨。
3.  **实验深度**：PDF文本提供的消融实验细节有限，对于PyConv内部各个设计选择（如为什么选择这些特定的核尺寸组合）的贡献分析不够深入。
4.  **对特定硬件的依赖**：虽然PyConv在理论上是高效的，但其并行计算的效率和实际推理速度可能依赖于硬件对分组卷积和不同尺寸卷积核的优化程度。
## 个人评论

1.  **优雅的“以小换大”思想**：PyConv的核心思想非常巧妙——通过分组卷积，用增加分组数（减少连接密度）来换取更大的卷积核尺寸，从而在**几乎不增加计算成本**的情况下获得**多尺度感受野**。这种在计算约束下进行资源再分配的设计哲学非常值得学习。
2.  **模块化与即插即用**：PyConv被设计为一个可替换标准卷积的模块，理论上可以应用于任何CNN架构中。这种设计使其易于集成和借鉴，为改进现有网络提供了一个新的基础组件选择。
3.  **对多尺度问题的一站式解决方案**：PyConv不仅解决了分类网络中的多尺度问题，其衍生的解析头（PyConvPH）也为语义分割中的多尺度上下文聚合提供了高效方案。这种从基础算子到任务头的一体化设计思路很有启发性。
4.  **实验结果的说服力**：用更浅、更小的模型（50层）在多个任务上超越了更深、更大的基线（152层ResNet），以效率换性能的成果非常扎实，具有很强的实用价值。

### 使用建议

*   **如果快速了解**：阅读**摘要**和**第3节（Pyramidal Convolution）**，查看**图2**理解核心结构，以及**表1**了解其在分类网络中的具体配置和性能优势。
*   **如果复现**：重点精读**第4节（PyConv Networks for Image Classification）**中的架构设计细节（如图4、表1），以及**第5节（PyConv Network on Semantic Segmentation）**中的解析头设计（图5、图6）。结合**公式(1)**理解其计算量平衡原理。
*   **如果借鉴创新点**：可以学习其“**用分组换尺寸**”的设计思想，并尝试将PyConv模块（或类似多尺度分组卷积的思想）移植到自己的骨干网络或任务头中，以增强模型的多尺度能力。
*   **如果写Related Work**：可以将其放在“**多尺度特征表示**”、“**高效卷积神经网络设计**”或“**改进的卷积算子**”等相关工作的分类中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中**卷积神经网络（CNN）基础架构**的研究方向，核心解决**多尺度特征表示与上下文信息捕获**的问题。其主要内容是提出一种新的卷积模块——金字塔卷积（Pyramidal Convolution, PyConv），并设计了基于该模块的网络架构，应用于图像分类、语义分割等多个视觉识别任务。因此，它非常适合放在“**B_注意力算子模块**”这一主题下，因为PyConv通过设计多尺度、不同连接度的卷积核并行处理输入，在功能上类似于一种多尺度特征聚合与“注意力”机制，但其本质是一种改进的卷积算子，旨在增强网络的多尺度感知能力。

## 2. 一句话总结
本文提出了一种名为金字塔卷积（PyConv）的新型卷积模块，它通过一个包含不同尺寸和深度的卷积核金字塔来并行处理输入特征，从而以与标准卷积相当的计算成本高效地捕获多尺度上下文信息，并显著提升多种视觉识别任务的性能。

## 3. 背景与问题
*   **为什么要做**：标准卷积神经网络（CNN）通常使用小尺寸卷积核（如3x3），为了扩大感受野，不得不依赖于堆叠小卷积核和逐步下采样。然而，研究表明网络的理论感受野远大于其实际有效感受野。此外，在获得足够上下文信息之前就进行下采样，会丢失对识别复杂场景中有用的空间细节（如不同大小、部分遮挡的目标）。
*   **之前方法的问题**：标准卷积核尺寸单一，无法直接、高效地处理图像中物体的巨大尺度变化。虽然存在如Squeeze-and-Excitation、Non-local blocks等模块来捕获上下文，但它们是附加模块，通常会显著增加模型参数和计算复杂度，且仍需要空间卷积作为基础。
*   **作者想解决的核心矛盾**：如何在**不增加计算成本和参数量**的前提下，让卷积算子本身具备**多尺度并行处理能力**，从而更早、更有效地捕获从局部细节到全局上下文的丰富信息。

## 4. 核心贡献
1.  **提出了金字塔卷积（PyConv）模块**：该模块包含一个卷积核金字塔，随着核尺寸（如3x3, 5x5, 7x7, 9x9）的增加，核的深度（通道连接数）相应减少。这种设计使得PyConv能在并行处理多尺度信息的同时，维持与单一小核标准卷积相似的参数量和计算量。
2.  **设计了用于图像分类的PyConvResNet架构**：将PyConv集成到残差瓶颈块中，构建了PyConvResNet网络。该网络在ImageNet上，其50层版本在性能上超越了152层的ResNet基线，且参数更少（少2.39倍）、计算量更低（少2.52倍）、网络层数更少。
3.  **提出了用于语义分割的PyConv解析头（PyConvPH）**：设计了一种包含局部和全局PyConv块的解析头，用于高效地聚合从局部细节到全局语义的多尺度上下文信息。基于此框架（PyConvSegNet）在ADE20K场景解析基准上取得了当时的最佳性能。
4.  **展示了PyConv在多种视觉任务上的通用性和有效性**：在目标检测和视频动作识别等任务上应用基于PyConv的架构，并报告了相对于基线的显著性能提升。

## 5. 方法详解
*   **整体框架与输入输出**：PyConv并非一个独立的网络，而是一个可替换标准卷积的**基础算子模块**。其输入为上一层的特征图（尺寸为H×W×FMi），输出为多尺度聚合后的特征图（尺寸为H×W×FMo）。
*   **关键模块（PyConv的核心机制）**：
    1.  **金字塔结构**：PyConv包含`n`个层级。从第1层到第n层，卷积核的空间尺寸`K`逐渐增大（如`K1`到`Kn`），而核的深度（即分组数`G`）逐渐增加，导致每个分组内的通道连接数（核深度）`FMi/G`逐渐减小。这形成了一个“双向金字塔”：一个金字塔（空间尺寸）底大顶小，另一个金字塔（核深度）底小顶大。
    2.  **分组卷积实现**：为了实现不同层级的核深度，输入特征图`FMi`在每个层级被均匀分成若干组（`G`组），然后独立地对每组应用对应尺寸的卷积核。分组数`G`的增大降低了连接性，从而在增大核尺寸的同时控制了计算量。
    3.  **并行与合并**：所有`n`个层级在输入特征图上并行计算，各自产生一组输出特征图（`FMo1, FMo2, ..., FMon`），最后将这些输出在通道维度上拼接，形成最终的输出特征图`FMo`。
*   **数学公式与直观解释**：标准卷积的计算量为 `FLOPs = K² × FMi × FMo × H × W`。PyConv的计算量由公式(1)给出，是各层级计算量之和。作者通过精心设计（如令每层输出的特征图数`FMoi`与`K²`成反比），使得PyConv的总计算量与使用最小核`K1`的标准卷积相当。直观上，PyConv让网络用“细密连接的小核”看细节，同时用“粗略连接的大核”看全局，两者并行互补。
*   **和已有方法的差异**：与标准卷积相比，PyConv具备内在的多尺度处理能力。与额外的上下文模块（如SE、Non-local）相比，PyConv是一个替代基础卷积的算子，不引入额外的插入式模块，且能保持计算效率。
*   **在具体任务中的应用**：
    *   **图像分类**：将PyConv嵌入ResNet的瓶颈结构中（见图4）。作者还创新地将最大池化层从网络前端移至第一个残差块的短连接上，使PyConv能在更高分辨率的特征图上进行多尺度下采样。
    *   **语义分割**：设计PyConv解析头（PyConvPH），包含一个**局部PyConv块**（用于捕获局部细节）和一个**全局PyConv块**（结合自适应平均池化捕获全局上下文），两者输出拼接后用于最终分类。该头取代了PSPNet中的金字塔池化模块（PPM）或DeepLab中的ASPP模块。

## 6. 实验与结果
*   **使用的数据集**：ImageNet（图像分类）、ADE20K（语义分割）、以及附录中提及的用于目标检测和视频分类的相应数据集（PDF文本中未具体列出后两者的名称）。
*   **对比方法**：主要基线是ResNet系列（如ResNet-50, ResNet-152）。在语义分割中，还与PSPNet（使用PPM）和使用ASPP的模型进行了比较。
*   **评价指标**：图像分类使用Top-1和Top-5准确率；语义分割使用平均交并比（mIo）和像素准确率。
*   **主实验结果**：
    *   **图像分类**：PyConvResNet-50在ImageNet上Top-1准确率**22.1%**（误差），优于ResNet-50的**23.9%**，并超越了更深的ResNet-152（**21.7%**），同时参数量（**24.85M** vs 60.19M）和FLOPs（**3.88G** vs 11.58G）大幅降低。
    *   **语义分割**：基于PyConvResNet-50和PyConvPH的框架在ADE20K验证集上达到**44.6%** mIo，优于PSPNet和DeepLab v3等方法，**设置了新的state-of-the-art**。
*   **消融实验**：PDF文本中未提供详细的消融实验表格，但讨论了不同PyConv设置（如层级数、分组数、每层输出特征图数）对性能的影响，强调了其灵活性。
*   **泛化实验**：论文展示了在图像分类、语义分割、目标检测、视频动作识别四个核心视觉任务上的改进，证明了PyConv的泛化能力。
*   **效率信息**：论文提供了详细的参数量（# params）和计算量（FLOPs）比较。例如，PyConvResNet-50比ResNet-50参数少约2.39倍，FLOPs低约2.52倍，同时性能更优。

## 7. 这篇论文真正有价值的地方
1.  **优雅的“以小换大”思想**：PyConv的核心思想非常巧妙——通过分组卷积，用增加分组数（减少连接密度）来换取更大的卷积核尺寸，从而在**几乎不增加计算成本**的情况下获得**多尺度感受野**。这种在计算约束下进行资源再分配的设计哲学非常值得学习。
2.  **模块化与即插即用**：PyConv被设计为一个可替换标准卷积的模块，理论上可以应用于任何CNN架构中。这种设计使其易于集成和借鉴，为改进现有网络提供了一个新的基础组件选择。
3.  **对多尺度问题的一站式解决方案**：PyConv不仅解决了分类网络中的多尺度问题，其衍生的解析头（PyConvPH）也为语义分割中的多尺度上下文聚合提供了高效方案。这种从基础算子到任务头的一体化设计思路很有启发性。
4.  **实验结果的说服力**：用更浅、更小的模型（50层）在多个任务上超越了更深、更大的基线（152层ResNet），以效率换性能的成果非常扎实，具有很强的实用价值。

## 8. 局限与问题
1.  **超参数调整**：PyConv的具体配置（如每层的核尺寸、分组数、输出通道数）是一个设计空间，论文提供了指导原则（如使用2的幂次），但针对特定任务找到最优配置可能需要实验搜索，增加了设计复杂度。
2.  **分组卷积的固有局限**：PyConv依赖于分组卷积，这可能会限制不同分组之间的特征交互。虽然论文通过金字塔结构中的不同连接度进行了弥补，但这是否是最佳的平衡点值得探讨。
3.  **实验深度**：PDF文本提供的消融实验细节有限，对于PyConv内部各个设计选择（如为什么选择这些特定的核尺寸组合）的贡献分析不够深入。
4.  **对特定硬件的依赖**：虽然PyConv在理论上是高效的，但其并行计算的效率和实际推理速度可能依赖于硬件对分组卷积和不同尺寸卷积核的优化程度。

## 9. 我该怎么使用这篇论文
*   **如果快速了解**：阅读**摘要**和**第3节（Pyramidal Convolution）**，查看**图2**理解核心结构，以及**表1**了解其在分类网络中的具体配置和性能优势。
*   **如果复现**：重点精读**第4节（PyConv Networks for Image Classification）**中的架构设计细节（如图4、表1），以及**第5节（PyConv Network on Semantic Segmentation）**中的解析头设计（图5、图6）。结合**公式(1)**理解其计算量平衡原理。
*   **如果借鉴创新点**：可以学习其“**用分组换尺寸**”的设计思想，并尝试将PyConv模块（或类似多尺度分组卷积的思想）移植到自己的骨干网络或任务头中，以增强模型的多尺度能力。
*   **如果写Related Work**：可以将其放在“**多尺度特征表示**”、“**高效卷积神经网络设计**”或“**改进的卷积算子**”等相关工作的分类中。

## 10. 和其他论文的关系
根据主题“B_注意力算子模块”和论文内容，可能相关的论文包括：
*   [[ResNet]]：本文的主要基线和骨干网络来源。
*   [[ResNeXt]]：本文使用了分组卷积，这与ResNeXt的思路有相似之处，但PyConv的分组是动态且伴随核尺寸变化的。
*   [[SENet]] (Squeeze-and-Excitation Networks)：作为另一种增强特征表示的方法（通道注意力），与本文的多尺度空间卷积形成对比或互补。
*   [[PSPNet]] 和 [[DeepLab系列]]：在语义分割任务中的主要对比方法，本文的PyConvPH头旨在替代或改进它们的上下文聚合模块。
*   [[Non-local Neural Networks]]：另一种捕获长距离依赖的注意力模块，与本文方法目标相似但路径不同。

## 11. 关键词
金字塔卷积， 多尺度特征， 分组卷积， 卷积神经网络， 图像分类， 语义分割， 计算效率， 感受野， 上下文信息， 残差学习

## 12. 可信度说明
本篇精读笔记主要基于用户提供的 **PDF提取文本的前12页** 生成。内容涵盖了论文的标题、摘要、引言、相关工作、方法论（PyConv核心思想、图像分类网络架构、语义分割框架）、以及部分实验结果和结论。提取质量良好，覆盖了论文的主要贡献和关键技术细节。但需注意，由于只提供了前12页（共16页），关于**目标检测和视频分类**的详细实验结果（位于附录）在笔记中无法展开，相关描述在“核心贡献”和“实验与结果”部分仅作概括性提及。整体而言，基于给定文本，笔记内容可信。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/PyConv.txt` (16/16 页; 原 AI 主体 12/16 + 全文补读 13-16); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-16; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-16。
- **提取情况**: 缺失页 4 页, 其中 4 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: PyConvPH Figure 10: Visual comparison results of our approach PyConSegNet (with PyConvPH head) with
- p.15: References

### 缺失页关键摘录

- p.13: PyConvPH Figure 10: Visual comparison results of our approach PyConSegNet (with PyConvPH head) with
- p.13: The images are from ADE20K dataset [20] validation.
- p.14: (a)Image (b) Groud Truth (c) PyConvResNet-50 (d) PyConvResNet-101 (e) PyConvResNet-152 Figure 11: Visual results of our approach, PyConSegNet, on 50-, 101-, 152-layers deep backbone
- p.14: PyConvResNet. The images are from ADE20K dataset [20] validation set.
- p.15: scenes through the ade20k dataset,” IJCV , vol. 127, no. 3, pp. 302–321, 2019.
- p.16: P. Natsev, et al. , “The kinetics human action video dataset,” ArXiv:1705.06950 , 2017.
<!-- AI_READING_NOTE_END -->
