---
title: "GhostNetV2: Enhance Cheap Operation with"
authors:
  - "YehuiTang1"
  - "KaiHan2"
  - "JianyuanGuo2"
  - "ChangXu3"
  - "ChaoXu1"
  - "YunheWang2∗"
  - "SchoolofArtificialIntelligence"
  - "PekingUniversity. 2HuaweiNoah’sArkLab."
year: 2022
venue: "arXiv"
doi: 
pdf: [[GhostModuleV2.pdf]]
primary_topic: B_注意力算子模块
topics:
  - "B_注意力算子模块"
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
extract_cache: .paper-cache/extracts/GhostModuleV2.txt
---

# GhostNetV2: Enhance Cheap Operation with

## 基本信息
- **PDF**: [[GhostModuleV2.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | GhostNetV2: Enhance Cheap Operation with |
| **作者** | YehuiTang1; KaiHan2; JianyuanGuo2; ChangXu3; ChaoXu1; YunheWang2∗; SchoolofArtificialIntelligence; PekingUniversity. 2HuaweiNoah’sArkLab. |
| **发表时间** | 2022 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Light-weight convolutional neural networks (CNNs) are specially designed for applications on mobile devices with faster inference speed. The convolutional operationcanonlycapturelocalinformationinawindowregion,whichprevents performancefrombeingfurtherimproved. Introducingself-attentionintoconvolu- tioncancaptureglobalinformationwell,butitwilllargelyencumbertheactual speed. Inthispaper,weproposeahardware-friendlyattentionmechanism(dubbed DFCattention)andthenpresentanewGhostNetV2architectureformobileapplica- tions. TheproposedDFCattentionisconstructedbasedonfully-connectedlayers, whichcannotonlyexecutefastoncommonhardwarebutalsocapturethedepen- dencebetweenlong-rangepixels. Wefurtherrevisittheexpressivenessbottleneck inpreviousGhostNetandproposetoenhanceexpandedfeaturesproducedbycheap operationswithDFCattention,sothataGhostNetV2blockcanaggregatelocaland long-rangeinformationsimultaneously. Extensiveexperimentsdemonstratethesu- periorityofGhostNetV2overexistingarchitectures.Forexample,ita

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：轻量级CNN（如MobileNet、ShuffleNet、GhostNet）是移动端部署的主流方案，但其卷积操作（特别是1×1卷积）只能捕捉局部信息，限制了性能的进一步提升。同时，虽然自注意力机制能有效建模全局依赖，但其理论计算复杂度高，且包含大量硬件不友好的张量重塑操作，导致在移动端实际推理速度急剧下降。
- **之前方法有什么问题**：以GhostNet为代表的轻量级模型，其Ghost模块通过廉价操作（如深度卷积）生成一半的特征，但这些操作的空间交互能力有限；另一半特征仅由1×1卷积生成，完全没有空间像素间的交互，损害了模型捕捉空间信息的能力。若直接引入如MobileViT中的自注意力，虽然能提升准确率（如从73.9%到74.4%），但会导致延迟大幅增加（从31.1ms到72.3ms），理论FLOPs与实际延迟严重不匹配。
- **作者想解决的核心矛盾**：轻量级模型需要长程依赖建模能力来提升性能，但现有注意力机制的计算开销（包括理论FLOPs和实际延迟）过大，与轻量级设计的目标相悖。因此，核心矛盾是**如何在移动端有限的计算和延迟预算内，为轻量级CNN引入有效的长程信息聚合能力**。
## 关键贡献

1.  **提出了DFC注意力机制**：设计了一种基于全连接层（FC）的解耦注意力。它通过水平FC和垂直FC两个方向依次聚合像素，以远低于标准自注意力的计算复杂度（O(H²W+HW²) vs O(H²W²)）捕获全局感受野，并且易于用硬件友好的深度卷积实现。
2.  **揭示了GhostNet的表征瓶颈**：通过分析发现，Ghost模块中由廉价操作生成的特征缺乏足够的空间信息交互，限制了其表征能力。
3.  **提出了基于DFC注意力增强Ghost模块的方法**：将DFC注意力分支并行于Ghost模块，用于增强其生成的“扩展特征”（expanded features），从而同时聚合局部和长程信息。
4.  **设计了新的轻量级视觉骨干网络GhostNetV2**：构建了包含DFC注意力增强模块的GhostV2瓶颈块，在ImageNet分类和MS COCO目标检测任务上，实现了优于现有SOTA轻量级模型的准确率-速度权衡。
## 方法

- **整体框架**：GhostNetV2的核心是改进的GhostV2瓶颈块。它是一个倒残差结构，包含两个Ghost模块。关键改进在于，在第一个Ghost模块（扩展通道数）的旁路并行引入了DFC注意力分支，用于增强该模块输出的“扩展特征”。
- **输入输出**：
    - **输入**：特征图 X ∈ R^{H×W×C}。
    - **输出**：经过增强和通道调整后的特征图 O ∈ R^{H×W×C'}。
- **关键模块**：
    1.  **Ghost模块**：按原文公式(1)(2)，首先用1×1卷积生成通道数较少的“本征特征” Y₀，然后对Y₀应用廉价操作（如深度卷积）生成更多特征，最后拼接得到输出特征Y。
    2.  **DFC注意力模块**：这是本文的核心创新。其设计遵循三个原则：长程性、部署高效性、概念简单性。
        - **数学机制**：给定输入特征图Z，一个直接的全连接注意力计算（公式3）需要O(H²W²)复杂度。作者利用特征图的二维结构将其解耦。首先，沿水平方向（宽度维度）聚合：`a'_{hw} = Σ_{h'} F^H_{h, h'w} ⊙ z_{h'w}`（公式4）。然后，沿垂直方向（高度维度）聚合：`a_{hw} = Σ_{w'} F^W_{w, h w'} ⊙ a'_{h w'}`（公式5）。这样，每个点的注意力值间接地涉及了所有空间位置的像素。
        - **实现与加速**：实际实现时，公式(4)和(5)可用两个深度卷积来近似：一个水平的1×K_H卷积和一个垂直的K_W×1卷积。这避免了耗时的张量重塑和转置操作。此外，为了降低计算量，会对输入特征进行平均池化下采样（宽高减半），在下采样后的特征上计算DFC注意力，再上采样回原尺寸。Sigmoid函数也在下采样后的特征上应用。
- **模块之间怎么连接**：如图4(b)，输入X同时送入两个分支：
    - **分支1（Ghost分支）**：通过第一个Ghost模块得到扩展特征Y（通道数较多）。
    - **分支2（注意力分支）**：先通过一个1×1卷积将X转换为Z（DFC的输入），然后经过DFC注意力模块（包含下采样、水平/垂直FC、上采样、Sigmoid）得到归一化的注意力图A。
    - **融合**：两个分支的输出进行逐元素相乘：`O = Sigmoid(A) ⊙ Y`（公式6），得到增强后的扩展特征，随后送入第二个Ghost模块进行通道压缩。
- **训练方式**：PDF文本中未明确说明，但应为端到端的标准图像分类训练。
- **推理流程**：模型推理时，输入图像经过一系列GhostV2块和其他层，最终得到分类结果。DFC注意力分支在推理时增加的计算量很小。
- **和已有方法的差异**：
    - **与标准自注意力（如ViT， Swin）**：DFC注意力避免了QKV投影和复杂的注意力矩阵计算，用两个方向性的深度卷积替代，计算复杂度和实际延迟大大降低，更适合移动端。
    - **与GhostNet V1**：GhostNetV2通过引入并行的DFC注意力分支来增强Ghost模块的“廉价操作”特征，弥补了V1中这部分特征缺乏空间交互的短板。
## 实验

- **使用的数据集**：ImageNet (ILSVRC 2012) 用于图像分类，MS COCO用于目标检测。
- **对比方法**：MobileNetV1/V2/V3， ShuffleNetV1/V2， GhostNetV1， MnasNet， FBNet， ProxylessNAS， EfficientNet， MobileViT等。
- **评价指标**：Top-1准确率、Top-5准确率、模型参数量(Params)、计算量(FLOPs)、在华为P30 (Kirin 980 CPU) 上的推理延迟(Latency)。
- **主实验结果**：
    - **图像分类**：GhostNetV2 1.0×在167M FLOPs下达到75.3% Top-1准确率，显著超过同计算量的GhostNetV1 1.1× (74.5%, 168M FLOPs)。在不同规模下均优于其他轻量级模型（详见Table 2）。
    - **目标检测**：以YOLOv3为检测头，在MS COCO数据集上，GhostNetV2 1.0×作为骨干网络，其AP指标在320和416输入分辨率下均优于同计算量的MobileNetV2和GhostNetV1（详见Table 3）。
- **消融实验**：
    - Table 1直观展示了DFC注意力的效果：在GhostNet上加入标准自注意力，延迟翻倍(31.1ms -> 72.3ms)；而加入DFC注意力，延迟增加有限(31.1ms -> 37.5ms)，且准确率提升更大(73.9% -> 75.3%)。
    - Section 5.4（Table 8）探讨了DFC注意力放置位置的影响，发现用于增强“扩展特征”比增强“输出特征”更有效。
- **泛化实验**：在ImageNet分类和MS COCO目标检测两个任务上均验证了有效性。
- **速度/参数量/FLOPs等效率信息**：论文提供了详细的对比图表（Figure 1, 2），表明GhostNetV2在相同FLOPs或延迟下，准确率均优于其他模型。
## 局限

- **方法适用场景**：DFC注意力的设计基于对2D特征图进行水平和垂直方向分解，对于非网格结构的数据（如点云）可能不直接适用。其固定的注意力权重（由FC层学习）可能不如动态生成的注意力图灵活。
- **实验充分性**：实验主要在分类和检测任务上验证，对于更密集的任务（如语义分割）的效果未展示。文中提到延迟测量在特定设备（Kirin 980 CPU）上，对于其他硬件平台（如GPU、DSP）的优化效果未讨论。
- **数据集与假设**：实验基于标准学术数据集，对于真实移动场景的复杂性和数据分布变化未做深入探讨。方法隐式假设了特征的水平/垂直方向结构信息是重要的。
- **复现风险**：论文提供了代码链接，复现风险较低。但DFC注意力中下采样和上采样的具体实现细节（如插值方法）可能对最终性能有细微影响。
## 个人评论

这篇论文最值得学习的核心思想是**“用简单、硬件友好的算子去近似实现复杂的全局感受野”**。它没有照搬NLP/CV中复杂的Transformer注意力，而是深入理解移动端硬件和部署的实际瓶颈（张量操作、延迟），提出用两个方向性的深度卷积（DFC）来间接实现全局信息聚合。这种设计思路对于后续研究轻量级高效模型极具启发：
1.  **问题驱动**：从实际部署延迟与理论FLOPs的鸿沟中发现问题。
2.  **硬件意识**：设计算法时就考虑最终实现的硬件友好性。
3.  **分解与近似**：将一个复杂操作分解为多个简单、高效步骤的组合，用线性运算近似非线性交互。
4.  **即插即用**：DFC注意力作为一个独立模块，有潜力增强其他轻量级骨干网络。

### 使用建议

- **如果快速了解**：只读**摘要**和**引言**，即可掌握论文动机、核心思想和主要结果。
- **如果复现**：重点阅读**第4节（Approach）**，特别是4.1节的DFC注意力公式和4.2节的GhostV2块结构图（Figure 4(b)）。结合**第5节实验设置**中的训练细节。
- **如果借鉴创新点**：应深入学习**DFC注意力的设计哲学**（分解为方向性操作）和**增强廉价操作特征**的思路。可以思考如何将DFC注意力应用于其他轻量级网络（如MobileNet）或任务中。
- **如果写related work**：可归入“轻量级注意力机制”或“高效视觉Transformer/混合架构”类别。可与MobileViT、EfficientFormer等进行对比。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中高效神经网络架构设计的方向，具体聚焦于**轻量级注意力算子模块**的设计。论文旨在解决轻量级卷积神经网络(CNN)在移动端部署时，因卷积操作局部性限制而难以有效建模长程依赖的问题，从而提升模型性能。它适合归类于“B_注意力算子模块”主题，探讨如何将注意力机制以高效的方式集成到轻量级CNN中。

## 2. 一句话总结
本文提出了一种硬件友好的解耦全连接(DFC)注意力机制，并将其集成到改进的Ghost模块中，构建了新的轻量级网络GhostNetV2，在保持低计算成本的同时显著增强了模型对长程空间信息的捕获能力。

## 3. 背景与问题
- **这篇论文为什么要做**：轻量级CNN（如MobileNet、ShuffleNet、GhostNet）是移动端部署的主流方案，但其卷积操作（特别是1×1卷积）只能捕捉局部信息，限制了性能的进一步提升。同时，虽然自注意力机制能有效建模全局依赖，但其理论计算复杂度高，且包含大量硬件不友好的张量重塑操作，导致在移动端实际推理速度急剧下降。
- **之前方法有什么问题**：以GhostNet为代表的轻量级模型，其Ghost模块通过廉价操作（如深度卷积）生成一半的特征，但这些操作的空间交互能力有限；另一半特征仅由1×1卷积生成，完全没有空间像素间的交互，损害了模型捕捉空间信息的能力。若直接引入如MobileViT中的自注意力，虽然能提升准确率（如从73.9%到74.4%），但会导致延迟大幅增加（从31.1ms到72.3ms），理论FLOPs与实际延迟严重不匹配。
- **作者想解决的核心矛盾**：轻量级模型需要长程依赖建模能力来提升性能，但现有注意力机制的计算开销（包括理论FLOPs和实际延迟）过大，与轻量级设计的目标相悖。因此，核心矛盾是**如何在移动端有限的计算和延迟预算内，为轻量级CNN引入有效的长程信息聚合能力**。

## 4. 核心贡献
1.  **提出了DFC注意力机制**：设计了一种基于全连接层（FC）的解耦注意力。它通过水平FC和垂直FC两个方向依次聚合像素，以远低于标准自注意力的计算复杂度（O(H²W+HW²) vs O(H²W²)）捕获全局感受野，并且易于用硬件友好的深度卷积实现。
2.  **揭示了GhostNet的表征瓶颈**：通过分析发现，Ghost模块中由廉价操作生成的特征缺乏足够的空间信息交互，限制了其表征能力。
3.  **提出了基于DFC注意力增强Ghost模块的方法**：将DFC注意力分支并行于Ghost模块，用于增强其生成的“扩展特征”（expanded features），从而同时聚合局部和长程信息。
4.  **设计了新的轻量级视觉骨干网络GhostNetV2**：构建了包含DFC注意力增强模块的GhostV2瓶颈块，在ImageNet分类和MS COCO目标检测任务上，实现了优于现有SOTA轻量级模型的准确率-速度权衡。

## 5. 方法详解
- **整体框架**：GhostNetV2的核心是改进的GhostV2瓶颈块。它是一个倒残差结构，包含两个Ghost模块。关键改进在于，在第一个Ghost模块（扩展通道数）的旁路并行引入了DFC注意力分支，用于增强该模块输出的“扩展特征”。
- **输入输出**：
    - **输入**：特征图 X ∈ R^{H×W×C}。
    - **输出**：经过增强和通道调整后的特征图 O ∈ R^{H×W×C'}。
- **关键模块**：
    1.  **Ghost模块**：按原文公式(1)(2)，首先用1×1卷积生成通道数较少的“本征特征” Y₀，然后对Y₀应用廉价操作（如深度卷积）生成更多特征，最后拼接得到输出特征Y。
    2.  **DFC注意力模块**：这是本文的核心创新。其设计遵循三个原则：长程性、部署高效性、概念简单性。
        - **数学机制**：给定输入特征图Z，一个直接的全连接注意力计算（公式3）需要O(H²W²)复杂度。作者利用特征图的二维结构将其解耦。首先，沿水平方向（宽度维度）聚合：`a'_{hw} = Σ_{h'} F^H_{h, h'w} ⊙ z_{h'w}`（公式4）。然后，沿垂直方向（高度维度）聚合：`a_{hw} = Σ_{w'} F^W_{w, h w'} ⊙ a'_{h w'}`（公式5）。这样，每个点的注意力值间接地涉及了所有空间位置的像素。
        - **实现与加速**：实际实现时，公式(4)和(5)可用两个深度卷积来近似：一个水平的1×K_H卷积和一个垂直的K_W×1卷积。这避免了耗时的张量重塑和转置操作。此外，为了降低计算量，会对输入特征进行平均池化下采样（宽高减半），在下采样后的特征上计算DFC注意力，再上采样回原尺寸。Sigmoid函数也在下采样后的特征上应用。
- **模块之间怎么连接**：如图4(b)，输入X同时送入两个分支：
    - **分支1（Ghost分支）**：通过第一个Ghost模块得到扩展特征Y（通道数较多）。
    - **分支2（注意力分支）**：先通过一个1×1卷积将X转换为Z（DFC的输入），然后经过DFC注意力模块（包含下采样、水平/垂直FC、上采样、Sigmoid）得到归一化的注意力图A。
    - **融合**：两个分支的输出进行逐元素相乘：`O = Sigmoid(A) ⊙ Y`（公式6），得到增强后的扩展特征，随后送入第二个Ghost模块进行通道压缩。
- **训练方式**：PDF文本中未明确说明，但应为端到端的标准图像分类训练。
- **推理流程**：模型推理时，输入图像经过一系列GhostV2块和其他层，最终得到分类结果。DFC注意力分支在推理时增加的计算量很小。
- **和已有方法的差异**：
    - **与标准自注意力（如ViT， Swin）**：DFC注意力避免了QKV投影和复杂的注意力矩阵计算，用两个方向性的深度卷积替代，计算复杂度和实际延迟大大降低，更适合移动端。
    - **与GhostNet V1**：GhostNetV2通过引入并行的DFC注意力分支来增强Ghost模块的“廉价操作”特征，弥补了V1中这部分特征缺乏空间交互的短板。

## 6. 实验与结果
- **使用的数据集**：ImageNet (ILSVRC 2012) 用于图像分类，MS COCO用于目标检测。
- **对比方法**：MobileNetV1/V2/V3， ShuffleNetV1/V2， GhostNetV1， MnasNet， FBNet， ProxylessNAS， EfficientNet， MobileViT等。
- **评价指标**：Top-1准确率、Top-5准确率、模型参数量(Params)、计算量(FLOPs)、在华为P30 (Kirin 980 CPU) 上的推理延迟(Latency)。
- **主实验结果**：
    - **图像分类**：GhostNetV2 1.0×在167M FLOPs下达到75.3% Top-1准确率，显著超过同计算量的GhostNetV1 1.1× (74.5%, 168M FLOPs)。在不同规模下均优于其他轻量级模型（详见Table 2）。
    - **目标检测**：以YOLOv3为检测头，在MS COCO数据集上，GhostNetV2 1.0×作为骨干网络，其AP指标在320和416输入分辨率下均优于同计算量的MobileNetV2和GhostNetV1（详见Table 3）。
- **消融实验**：
    - Table 1直观展示了DFC注意力的效果：在GhostNet上加入标准自注意力，延迟翻倍(31.1ms -> 72.3ms)；而加入DFC注意力，延迟增加有限(31.1ms -> 37.5ms)，且准确率提升更大(73.9% -> 75.3%)。
    - Section 5.4（Table 8）探讨了DFC注意力放置位置的影响，发现用于增强“扩展特征”比增强“输出特征”更有效。
- **泛化实验**：在ImageNet分类和MS COCO目标检测两个任务上均验证了有效性。
- **速度/参数量/FLOPs等效率信息**：论文提供了详细的对比图表（Figure 1, 2），表明GhostNetV2在相同FLOPs或延迟下，准确率均优于其他模型。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的核心思想是**“用简单、硬件友好的算子去近似实现复杂的全局感受野”**。它没有照搬NLP/CV中复杂的Transformer注意力，而是深入理解移动端硬件和部署的实际瓶颈（张量操作、延迟），提出用两个方向性的深度卷积（DFC）来间接实现全局信息聚合。这种设计思路对于后续研究轻量级高效模型极具启发：
1.  **问题驱动**：从实际部署延迟与理论FLOPs的鸿沟中发现问题。
2.  **硬件意识**：设计算法时就考虑最终实现的硬件友好性。
3.  **分解与近似**：将一个复杂操作分解为多个简单、高效步骤的组合，用线性运算近似非线性交互。
4.  **即插即用**：DFC注意力作为一个独立模块，有潜力增强其他轻量级骨干网络。

## 8. 局限与问题
- **方法适用场景**：DFC注意力的设计基于对2D特征图进行水平和垂直方向分解，对于非网格结构的数据（如点云）可能不直接适用。其固定的注意力权重（由FC层学习）可能不如动态生成的注意力图灵活。
- **实验充分性**：实验主要在分类和检测任务上验证，对于更密集的任务（如语义分割）的效果未展示。文中提到延迟测量在特定设备（Kirin 980 CPU）上，对于其他硬件平台（如GPU、DSP）的优化效果未讨论。
- **数据集与假设**：实验基于标准学术数据集，对于真实移动场景的复杂性和数据分布变化未做深入探讨。方法隐式假设了特征的水平/垂直方向结构信息是重要的。
- **复现风险**：论文提供了代码链接，复现风险较低。但DFC注意力中下采样和上采样的具体实现细节（如插值方法）可能对最终性能有细微影响。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读**摘要**和**引言**，即可掌握论文动机、核心思想和主要结果。
- **如果复现**：重点阅读**第4节（Approach）**，特别是4.1节的DFC注意力公式和4.2节的GhostV2块结构图（Figure 4(b)）。结合**第5节实验设置**中的训练细节。
- **如果借鉴创新点**：应深入学习**DFC注意力的设计哲学**（分解为方向性操作）和**增强廉价操作特征**的思路。可以思考如何将DFC注意力应用于其他轻量级网络（如MobileNet）或任务中。
- **如果写related work**：可归入“轻量级注意力机制”或“高效视觉Transformer/混合架构”类别。可与MobileViT、EfficientFormer等进行对比。

## 10. 和其他论文的关系
根据主题“B_注意力算子模块”，本文提出的DFC注意力是一种**空间注意力**。它可能与以下论文相关（基于文中引用推断）：
- **[[MobileViT]]**：作为引入自注意力到轻量级模型的代表，是本文重要的对比基线，其高延迟问题催生了DFC注意力的设计。
- **[[Swin Transformer]]**：使用窗口注意力降低复杂度，是另一种高效注意力的思路，与本文的全局但解耦的DFC思路形成对比。
- **[[GhostNet]]**：本文的直接改进基础，V1的表征瓶颈是V2改进的出发点。
- **[[MobileNet系列]]**：同属轻量级CNN，是更广泛的竞争和参考对象。

## 11. 关键词
GhostNetV2, DFC注意力, 轻量级CNN, 移动设备, 长程依赖, 硬件友好, 注意力机制, 图像分类, 目标检测, Ghost模块, 倒残差瓶颈

## 12. 可信度说明
这篇精读笔记**完全基于**提供的PDF提取文本（共12页）生成。核心内容，特别是DFC注意力的数学公式、GhostV2块的结构、主实验结果（如75.3% Top-1精度， 167M FLOPs）和关键消融实验（Table 1）均直接从文本中提取。对于PDF文本中**未明确说明**的部分（如训练细节、某些局限性），已在相应章节中明确标注“PDF文本中未明确说明”。提取文本涵盖了论文的主要技术部分，信息质量足以支撑一份完整、可信的精读笔记。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/GhostModuleV2.txt` (12/12 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
