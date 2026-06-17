---
title: ThisICCVpaperistheOpenAccessversion,providedbytheComputerVisionFoundation.
authors:
  - "Abdelrahman Shaker"
  - "Muhammad Maaz"
  - "Hanoona Rasheed"
  - "Salman Khan"
  - "Ming-Hsuan Yang"
  - "Fahad Shahbaz Khan"
year: 2023
venue: nature [20, 29]. Specifically, vision transformers (ViTs) CNNs and transformers is critical, particularly for mobile
doi: 
pdf: [[SwiftFormerEncoder&ConvEncoder.pdf]]
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
extract_cache: .paper-cache/extracts/SwiftFormerEncoder&ConvEncoder.txt
---

# ThisICCVpaperistheOpenAccessversion,providedbytheComputerVisionFoundation.

## 基本信息
- **PDF**: [[SwiftFormerEncoder&ConvEncoder.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | ThisICCVpaperistheOpenAccessversion,providedbytheComputerVisionFoundation. |
| **作者** | Abdelrahman Shaker; Muhammad Maaz; Hanoona Rasheed; Salman Khan; Ming-Hsuan Yang; Fahad Shahbaz Khan |
| **发表时间** | 2023 |
| **刊物/会议** | nature [20, 29]. Specifically, vision transformers (ViTs) CNNs and transformers is critical, particularly for mobile |
| **DOI** | 未明确 |

## 摘要

> Self-attention has become a defacto choice for captur- ingglobalcontextinvariousvisionapplications. However, its quadratic computational complexity with respect to im- ageresolutionlimitsitsuseinreal-timeapplications,espe- cially for deployment on resource-constrained mobile de- vices. Although hybrid approaches have been proposed to combine the advantages of convolutions and self-attention forabetterspeed-accuracytrade-off,theexpensivematrix multiplication operations in self-attention remain a bottle- neck. In this work, we introduce a novel efficient additive attentionmechanismthateffectivelyreplacesthequadratic matrix multiplication operations with linear element-wise multiplications. Ourdesignshowsthatthekey-valueinter- actioncanbereplacedwithalinearlayerwithoutsacrific- inganyaccuracy. Unlikepreviousstate-of-the-artmethods, ourefficientformulationofself-attentionenablesitsusage Figure 1: Latency vs Accuracy Comparison. Compared at all stages of the network. Using our proposed effi

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：自注意力机制能有效捕捉全局上下文，是视觉Transformer的核心，但其计算复杂度与图像分辨率呈二次关系（O(n²·d)），导致在资源受限的移动设备上推理速度慢、内存占用高，难以满足实时应用需求。
- **之前方法有什么问题**：
    1.  **纯CNN方法**：计算高效，但依赖局部连接，难以建模长距离依赖和适应不同分辨率。
    2.  **混合CNN-Transformer方法**：虽然结合了两者优势，但通常只在最后的低分辨率阶段使用标准或近似的自注意力（如MobileViT-v2, EfficientFormer），因为其高昂的计算开销使其在早期高分辨率阶段不可用。这导致全局上下文建模不一致、不充分。
    3.  **高效Transformer变体**：如转置自注意力（复杂度O(n·d²)）、稀疏注意力等，虽然在理论上降低了复杂度，但要么仍依赖点积运算，要么在移动端的实际推理速度提升有限（如MobileViT-v2仍比MobileNet-v2慢2倍）。
- **核心矛盾**：如何在移动端严格的计算资源限制下，设计出能够有效建模全局上下文（这是Transformer的优势），同时又具有与CNN可比的计算效率和推理速度的视觉模型。
## 关键贡献

1.  **提出高效加法注意力机制**：用元素级乘法和线性变换彻底替代自注意力中的二次矩阵乘法，实现线性计算复杂度O(n·d)。
2.  **简化注意力交互**：证明在视觉任务中，可以移除键（Key）和值（Value）之间的显式交互，仅通过查询（Query）和键的交互加上一个线性变换层就能有效编码全局上下文，且不损失精度。
3.  **设计一致的混合架构**：由于所提注意力模块计算高效（线性复杂度），可以将其应用到网络的所有阶段（从早期高分辨率到后期低分辨率），从而在每个尺度上一致地学习局部-全局特征。
4.  **构建SwiftFormer系列模型**：基于上述注意力和有效的卷积编码器，构建了无需神经架构搜索（NAS）的高效模型族。
5.  **实现移动端SOTA性能**：小模型SwiftFormer-L1在iPhone 14上以0.8ms延迟达到78.5%的ImageNet Top-1精度，比MobileViT-v2更快且更准确。
## 方法

- **整体框架**：采用四阶段的分层结构（图3上）。输入图像经过Patch Embedding后，依次通过四个阶段。每个阶段由“卷积编码器（Conv. Encoder）”和“SwiftFormer编码器（SwiftFormer Encoder）”交替堆叠而成。阶段之间通过下采样层（步长为2的卷积）连接，降低分辨率并增加通道数。
- **输入输出**：输入为H×W×3的图像，输出为H/32×W/32×C4的层级特征图。
- **关键模块**：
    1.  **卷积编码器**：用于高效提取局部特征。结构为：输入 → 3×3深度可分离卷积+BN → 两个1×1逐点卷积+GeLU → 残差连接。设计目的是替代池化等简单操作，以更低的参数和延迟获得更好的局部表征。
    2.  **SwiftFormer编码器**：用于建模局部-全局表征。其核心是**高效加法注意力**模块（图2d）。流程为：
        - 输入先经过3×3深度可分离卷积和1×1卷积，提取局部特征。
        - 然后进入**高效加法注意力**模块：
            a. **生成全局查询**：输入特征X被投影为Q和K。Q与一个可学习向量wa相乘得到注意力权重α，再用α对Q进行加权池化，得到一个全局查询向量q。
            b. **编码全局上下文**：将全局查询q与K进行元素级乘法（广播后），得到全局上下文矩阵R。
            c. **线性变换与输出**：对R进行线性变换T，并与归一化后的查询矩阵Q相加，得到最终输出。
        - 最后通过两个1×1卷积层进行通道混合。
- **数学公式与直观解释**：
    - 传统自注意力：`输出 = Softmax(QK^T/√d) * V`，复杂度O(n²d)。
    - 本文的高效加法注意力：`α = Q * wa / √d`， `q = Σ(α_i * Q_i)`， `输出 = Norm(Q) + T(K * q)`。
    - **直观解释**：传统注意力计算所有token对之间的相似度（QK^T）。本文方法先学习一个“全局查询”q，它代表了所有token中应关注的模式。然后计算所有token的K与这个固定模式q的相似度（K*q），从而避免了计算巨大的token间相似度矩阵。这类似于用一个“模板”去匹配所有输入，而不是计算两两匹配。
- **与已有方法的差异**：
    - 与**标准自注意力**比：去除了二次矩阵乘法，改为线性操作。
    - 与**MobileViT-v2的可分离自注意力**比：同样用元素级操作，但进一步去除了值（V）的交互，用线性变换替代，并引入了可学习的全局查询生成机制。
    - 与**EfficientFormer**比：将注意力机制推广到所有阶段，而非仅最后阶段；用深度可分离卷积替换了池化作为局部混合器。
- **论文类型特化（注意力类）**：
    - **作用维度**：主要作用于**空间维度**（token序列），通过全局查询q来聚合空间信息。
    - **可插入网络**：设计为网络中一个独立的、可替换的编码器模块（SwiftFormer Encoder），在每个阶段堆叠使用。
    - **计算量 vs 效果**：核心设计目标是极大降低计算量和延迟。通过消除矩阵乘法和键值交互，实现了与卷积操作相当的推理速度，同时保留了建模全局依赖的能力，在精度上超越了同类轻量模型。
## 实验

- **使用数据集**：主要在ImageNet-1K上进行图像分类评估。也在MS COCO上进行了目标检测和实例分割，在ADE20K上进行了语义分割，以验证泛化能力。
- **对比方法**：主要对比移动端SOTA模型，包括MobileNets系列、EfficientNet系列、MobileViT系列、EfficientFormer系列、PoolFormer、EdgeNeXt等。
- **评价指标**：Top-1分类精度、推理延迟（ms）、模型参数量（Params）、浮点运算量（FLOPs）。
- **主实验结果**：
    - **分类**：SwiftFormer-L1达到78.5%精度，延迟仅0.8ms（iPhone 14）。SwiftFormer-L3达到83.0%精度，延迟1.9ms。在精度和延迟的权衡上全面优于MobileViT-v2和EfficientFormer。
    - **检测与分割**：作为backbone应用于Mask R-CNN和DeepLabV3，在COCO和ADE20K上也取得了有竞争力的结果，证明了其特征提取能力的泛化性。
- **消融实验**：
    - 验证了用深度可分离卷积替换池化（作为局部混合器）的有效性。
    - 验证了高效加法注意力中各组件（如全局查询生成、去除键值交互）的必要性。
    - 证明了将该注意力机制用于所有阶段（一致性设计）比仅用于最后阶段效果更好。
- **泛化实验**：如上所述，在检测和分割任务上展示了良好的迁移性能。
- **效率信息**：模型参数量和FLOPs相较于基线模型（如EfficientFormer）得到优化，并且实际移动端延迟显著降低，是其核心优势。
## 局限

1.  **任务验证范围**：虽然做了检测和分割，但主要评估和宣传集中在图像分类任务上。其在更复杂的任务（如视频理解、3D视觉）中的有效性有待验证。
2.  **硬件依赖性**：所有延迟数据基于iPhone 14的Apple Neural Engine，其性能表现可能与Android设备或其他移动GPU/NPU存在差异。
3.  **可扩展性**：论文主要展示了小规模到中等规模的模型，其设计原则对于超大规模模型（如用于数据中心的模型）是否同样有效，文中未探讨。
4.  **设计自动化**：SwiftFormer的架构（如各阶段通道数、模块堆叠数）是人工设计的，而EfficientFormer使用了NAS。虽然论文声称未使用NAS，但也未探讨结合NAS是否能进一步提升性能。
5.  **计算成本的相对性**：虽然FLOPs和延迟很低，但未详细分析在极端低端设备（如微控制器）上的可行性。
## 个人评论

1.  **对注意力机制的极致简化**：它大胆地挑战了自注意力中“查询-键-值”三者交互的传统范式，证明在视觉任务中，可以只保留“查询-键”交互并用一个线性层替代“键-值”交互，这为设计更轻量的注意力模块提供了新思路。
2.  **工程与理论的平衡**：没有停留在理论上的复杂度分析，而是紧密结合移动端硬件的实际推理延迟进行设计。提出的模块在推理速度上确实做到了与高效CNN可比，这是其成功的关键。
3.  **一致性设计的价值**：证明了让全局注意力机制贯穿网络所有阶段（而不仅是后期）对性能提升至关重要，这打破了此前认为“早期阶段用卷积、后期用注意力”的混合设计定式。
4.  **启发**：对于后续研究，这篇论文鼓励研究者去重新审视Transformer中每个计算组件的必要性，并探索在移动端等严格约束下，可以牺牲哪些理论上的“完整性”来换取实际的速度提升。在写论文时，其清晰的动机阐述（从移动端部署的痛点出发）和扎实的模块化对比实验（图2和表格消融）是很好的范例。

### 使用建议

- **如果快速了解**：重点阅读**摘要**、**引言**（第三段及贡献列表）、**图2和图3**（理解注意力模块和整体架构对比）、以及**实验部分的主要表格**（分类精度和延迟对比）。
- **如果复现**：精读**第3节方法**，特别是3.2和3.3部分，并结合**图3**仔细理解卷积编码器和SwiftFormer编码器的具体结构（如卷积核大小、顺序、激活函数）。注意公式(4)-(6)中的维度变化。需要参考其开源代码以确认实现细节。
- **如果借鉴创新点**：
    - 学习其**“去除键值交互”并用线性变换替代**的设计思想，可用于简化其他序列模型中的注意力。
    - 学习其**构建“全局查询”q**的加权池化方法，这是一种可学习的全局特征聚合方式。
    - 学习其**用深度可分离卷积替换池化**作为局部混合器的具体实现，可用于改进其他混合模型。
- **如果写Related Work**：可将其归类于“**高效视觉Transformer**”或“**移动端轻量化注意力机制**”，与[[MobileViT-v2]]、[[EfficientFormer]]、[[EdgeNeXt]]等工作并列讨论。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于高效视觉Transformer模型的研究方向，核心是设计一种新的、极其轻量化的注意力机制，以解决自注意力机制在移动端实时部署时计算复杂度过高的问题。该工作属于“B_注意力算子模块”主题，它提出并详细阐述了一种具体的注意力算子（Efficient Additive Attention）及其在网络中的应用架构。

## 2. 一句话总结
本文提出了“高效加法注意力”机制，通过用线性的元素级乘法替代二次复杂度的矩阵乘法，并去除键值交互，从而构建了可在网络所有阶段使用的轻量级Transformer模块，并据此设计了SwiftFormer系列模型，在移动端实现了SOTA的速度-精度权衡。

## 3. 背景与问题
- **为什么要做**：自注意力机制能有效捕捉全局上下文，是视觉Transformer的核心，但其计算复杂度与图像分辨率呈二次关系（O(n²·d)），导致在资源受限的移动设备上推理速度慢、内存占用高，难以满足实时应用需求。
- **之前方法有什么问题**：
    1.  **纯CNN方法**：计算高效，但依赖局部连接，难以建模长距离依赖和适应不同分辨率。
    2.  **混合CNN-Transformer方法**：虽然结合了两者优势，但通常只在最后的低分辨率阶段使用标准或近似的自注意力（如MobileViT-v2, EfficientFormer），因为其高昂的计算开销使其在早期高分辨率阶段不可用。这导致全局上下文建模不一致、不充分。
    3.  **高效Transformer变体**：如转置自注意力（复杂度O(n·d²)）、稀疏注意力等，虽然在理论上降低了复杂度，但要么仍依赖点积运算，要么在移动端的实际推理速度提升有限（如MobileViT-v2仍比MobileNet-v2慢2倍）。
- **核心矛盾**：如何在移动端严格的计算资源限制下，设计出能够有效建模全局上下文（这是Transformer的优势），同时又具有与CNN可比的计算效率和推理速度的视觉模型。

## 4. 核心贡献
1.  **提出高效加法注意力机制**：用元素级乘法和线性变换彻底替代自注意力中的二次矩阵乘法，实现线性计算复杂度O(n·d)。
2.  **简化注意力交互**：证明在视觉任务中，可以移除键（Key）和值（Value）之间的显式交互，仅通过查询（Query）和键的交互加上一个线性变换层就能有效编码全局上下文，且不损失精度。
3.  **设计一致的混合架构**：由于所提注意力模块计算高效（线性复杂度），可以将其应用到网络的所有阶段（从早期高分辨率到后期低分辨率），从而在每个尺度上一致地学习局部-全局特征。
4.  **构建SwiftFormer系列模型**：基于上述注意力和有效的卷积编码器，构建了无需神经架构搜索（NAS）的高效模型族。
5.  **实现移动端SOTA性能**：小模型SwiftFormer-L1在iPhone 14上以0.8ms延迟达到78.5%的ImageNet Top-1精度，比MobileViT-v2更快且更准确。

## 5. 方法详解
- **整体框架**：采用四阶段的分层结构（图3上）。输入图像经过Patch Embedding后，依次通过四个阶段。每个阶段由“卷积编码器（Conv. Encoder）”和“SwiftFormer编码器（SwiftFormer Encoder）”交替堆叠而成。阶段之间通过下采样层（步长为2的卷积）连接，降低分辨率并增加通道数。
- **输入输出**：输入为H×W×3的图像，输出为H/32×W/32×C4的层级特征图。
- **关键模块**：
    1.  **卷积编码器**：用于高效提取局部特征。结构为：输入 → 3×3深度可分离卷积+BN → 两个1×1逐点卷积+GeLU → 残差连接。设计目的是替代池化等简单操作，以更低的参数和延迟获得更好的局部表征。
    2.  **SwiftFormer编码器**：用于建模局部-全局表征。其核心是**高效加法注意力**模块（图2d）。流程为：
        - 输入先经过3×3深度可分离卷积和1×1卷积，提取局部特征。
        - 然后进入**高效加法注意力**模块：
            a. **生成全局查询**：输入特征X被投影为Q和K。Q与一个可学习向量wa相乘得到注意力权重α，再用α对Q进行加权池化，得到一个全局查询向量q。
            b. **编码全局上下文**：将全局查询q与K进行元素级乘法（广播后），得到全局上下文矩阵R。
            c. **线性变换与输出**：对R进行线性变换T，并与归一化后的查询矩阵Q相加，得到最终输出。
        - 最后通过两个1×1卷积层进行通道混合。
- **数学公式与直观解释**：
    - 传统自注意力：`输出 = Softmax(QK^T/√d) * V`，复杂度O(n²d)。
    - 本文的高效加法注意力：`α = Q * wa / √d`， `q = Σ(α_i * Q_i)`， `输出 = Norm(Q) + T(K * q)`。
    - **直观解释**：传统注意力计算所有token对之间的相似度（QK^T）。本文方法先学习一个“全局查询”q，它代表了所有token中应关注的模式。然后计算所有token的K与这个固定模式q的相似度（K*q），从而避免了计算巨大的token间相似度矩阵。这类似于用一个“模板”去匹配所有输入，而不是计算两两匹配。
- **与已有方法的差异**：
    - 与**标准自注意力**比：去除了二次矩阵乘法，改为线性操作。
    - 与**MobileViT-v2的可分离自注意力**比：同样用元素级操作，但进一步去除了值（V）的交互，用线性变换替代，并引入了可学习的全局查询生成机制。
    - 与**EfficientFormer**比：将注意力机制推广到所有阶段，而非仅最后阶段；用深度可分离卷积替换了池化作为局部混合器。
- **论文类型特化（注意力类）**：
    - **作用维度**：主要作用于**空间维度**（token序列），通过全局查询q来聚合空间信息。
    - **可插入网络**：设计为网络中一个独立的、可替换的编码器模块（SwiftFormer Encoder），在每个阶段堆叠使用。
    - **计算量 vs 效果**：核心设计目标是极大降低计算量和延迟。通过消除矩阵乘法和键值交互，实现了与卷积操作相当的推理速度，同时保留了建模全局依赖的能力，在精度上超越了同类轻量模型。

## 6. 实验与结果
- **使用数据集**：主要在ImageNet-1K上进行图像分类评估。也在MS COCO上进行了目标检测和实例分割，在ADE20K上进行了语义分割，以验证泛化能力。
- **对比方法**：主要对比移动端SOTA模型，包括MobileNets系列、EfficientNet系列、MobileViT系列、EfficientFormer系列、PoolFormer、EdgeNeXt等。
- **评价指标**：Top-1分类精度、推理延迟（ms）、模型参数量（Params）、浮点运算量（FLOPs）。
- **主实验结果**：
    - **分类**：SwiftFormer-L1达到78.5%精度，延迟仅0.8ms（iPhone 14）。SwiftFormer-L3达到83.0%精度，延迟1.9ms。在精度和延迟的权衡上全面优于MobileViT-v2和EfficientFormer。
    - **检测与分割**：作为backbone应用于Mask R-CNN和DeepLabV3，在COCO和ADE20K上也取得了有竞争力的结果，证明了其特征提取能力的泛化性。
- **消融实验**：
    - 验证了用深度可分离卷积替换池化（作为局部混合器）的有效性。
    - 验证了高效加法注意力中各组件（如全局查询生成、去除键值交互）的必要性。
    - 证明了将该注意力机制用于所有阶段（一致性设计）比仅用于最后阶段效果更好。
- **泛化实验**：如上所述，在检测和分割任务上展示了良好的迁移性能。
- **效率信息**：模型参数量和FLOPs相较于基线模型（如EfficientFormer）得到优化，并且实际移动端延迟显著降低，是其核心优势。

## 7. 这篇论文真正有价值的地方
1.  **对注意力机制的极致简化**：它大胆地挑战了自注意力中“查询-键-值”三者交互的传统范式，证明在视觉任务中，可以只保留“查询-键”交互并用一个线性层替代“键-值”交互，这为设计更轻量的注意力模块提供了新思路。
2.  **工程与理论的平衡**：没有停留在理论上的复杂度分析，而是紧密结合移动端硬件的实际推理延迟进行设计。提出的模块在推理速度上确实做到了与高效CNN可比，这是其成功的关键。
3.  **一致性设计的价值**：证明了让全局注意力机制贯穿网络所有阶段（而不仅是后期）对性能提升至关重要，这打破了此前认为“早期阶段用卷积、后期用注意力”的混合设计定式。
4.  **启发**：对于后续研究，这篇论文鼓励研究者去重新审视Transformer中每个计算组件的必要性，并探索在移动端等严格约束下，可以牺牲哪些理论上的“完整性”来换取实际的速度提升。在写论文时，其清晰的动机阐述（从移动端部署的痛点出发）和扎实的模块化对比实验（图2和表格消融）是很好的范例。

## 8. 局限与问题
1.  **任务验证范围**：虽然做了检测和分割，但主要评估和宣传集中在图像分类任务上。其在更复杂的任务（如视频理解、3D视觉）中的有效性有待验证。
2.  **硬件依赖性**：所有延迟数据基于iPhone 14的Apple Neural Engine，其性能表现可能与Android设备或其他移动GPU/NPU存在差异。
3.  **可扩展性**：论文主要展示了小规模到中等规模的模型，其设计原则对于超大规模模型（如用于数据中心的模型）是否同样有效，文中未探讨。
4.  **设计自动化**：SwiftFormer的架构（如各阶段通道数、模块堆叠数）是人工设计的，而EfficientFormer使用了NAS。虽然论文声称未使用NAS，但也未探讨结合NAS是否能进一步提升性能。
5.  **计算成本的相对性**：虽然FLOPs和延迟很低，但未详细分析在极端低端设备（如微控制器）上的可行性。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**摘要**、**引言**（第三段及贡献列表）、**图2和图3**（理解注意力模块和整体架构对比）、以及**实验部分的主要表格**（分类精度和延迟对比）。
- **如果复现**：精读**第3节方法**，特别是3.2和3.3部分，并结合**图3**仔细理解卷积编码器和SwiftFormer编码器的具体结构（如卷积核大小、顺序、激活函数）。注意公式(4)-(6)中的维度变化。需要参考其开源代码以确认实现细节。
- **如果借鉴创新点**：
    - 学习其**“去除键值交互”并用线性变换替代**的设计思想，可用于简化其他序列模型中的注意力。
    - 学习其**构建“全局查询”q**的加权池化方法，这是一种可学习的全局特征聚合方式。
    - 学习其**用深度可分离卷积替换池化**作为局部混合器的具体实现，可用于改进其他混合模型。
- **如果写Related Work**：可将其归类于“**高效视觉Transformer**”或“**移动端轻量化注意力机制**”，与[[MobileViT-v2]]、[[EfficientFormer]]、[[EdgeNeXt]]等工作并列讨论。

## 10. 和其他论文的关系
基于主题“B_注意力算子模块”和文件名，这篇论文明确与以下工作相关：
- [[MobileViT-v2]]：直接对标和改进的对象，提出了可分离自注意力。SwiftFormer在此基础上进一步简化。
- [[EfficientFormer]]：本文的架构基础，SwiftFormer对其进行了模块和注意力机制上的升级。
- [[PoolFormer]]：EfficientFormer使用的局部混合器（池化）的来源，SwiftFormer中用卷积替换了它。
- [[EdgeNeXt]]：采用了转置自注意力来降低复杂度，是另一种高效注意力的设计思路。

## 11. 关键词
高效加法注意力、移动端视觉、轻量级Transformer、线性复杂度、SwiftFormer、全局上下文建模、混合CNN-Transformer、推理速度优化、ImageNet分类、一致性架构设计。

## 12. 可信度说明
本笔记完全基于提供的PDF提取文本生成。主要依据是摘要（Abstract）、引言（Introduction）、相关工作（Related Work）的后半部分、以及整个方法论（Method）和实验（Experiments）章节的起始部分。文本提取质量良好，内容连贯，覆盖了论文的核心思想、具体方法、主要公式和实验结果的关键数据。对于方法部分的细节（如图3下部的模块内部结构），文本描述与图示引用相匹配。未发现明显的提取错误或缺失关键段落。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/SwiftFormerEncoder&ConvEncoder.txt` (12/12 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
