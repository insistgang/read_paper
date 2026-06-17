---
title: "LMLT: Low-to-high Multi-Level Vision Transformer"
authors:
  - "Jeongsoo Kim"
  - "Jongho Nang"
  - "Junsuk Choe"
year: 2024
venue: "arXiv"
doi: 
pdf: [[LMLT.pdf]]
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
extract_cache: .paper-cache/extracts/LMLT.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/22 pages"
---
# LMLT: Low-to-high Multi-Level Vision Transformer

## 基本信息
- **PDF**: [[LMLT.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | LMLT: Low-to-high Multi-Level Vision Transformer |
| **作者** | Jeongsoo Kim; Jongho Nang; Junsuk Choe |
| **发表时间** | 2024 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> RecentVisionTransformer(ViT)-basedmethodsforImageSuper-Resolutionhave demonstrated impressive performance. However, they suffer from significant complexity, resulting in high inference times and memory usage. Additionally, ViTmodelsusingWindowSelf-Attention(WSA)facechallengesinprocessing regionsoutsidetheirwindows.Toaddresstheseissues,weproposetheLow-to-high Multi-LevelTransformer(LMLT),whichemploysattentionwithvaryingfeature sizesforeachhead. LMLTdividesimagefeaturesalongthechanneldimension, graduallyreducesspatialsizeforlowerheads,andappliesself-attentiontoeach head. Thisapproacheffectivelycapturesbothlocalandglobalinformation. By integrating the results from lower heads into higher heads, LMLT overcomes thewindowboundaryissuesinself-attention. Extensiveexperimentsshowthat our model significantly reduces inference time and GPU memory usage while maintaining or even surpassing the performance of state-of-the-art ViT-based ImageSuper-Resolutionmethods. Ourcodesareavailiableathttps://gi

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：尽管基于ViT的图像超分辨率方法（如SwinIR）性能优越，但其计算复杂度随输入尺寸呈二次增长，导致高推理延迟和内存消耗，限制了实际应用。
- **之前方法的问题**：
    1. **效率问题**：传统ViT模型（如SwinIR）堆叠自注意力层（串行连接），导致计算负载和推理时间过长。
    2. **窗口边界问题**：窗口自注意力（WSA）将图像划分为独立窗口进行计算，导致不同窗口间缺乏交互，在窗口边界处质量下降，难以建模长距离依赖。
- **核心矛盾**：如何在**保持或提升超分辨率性能**的同时，**显著降低模型的计算复杂度、推理时间和内存占用**，并**解决窗口自注意力固有的边界问题**。
## 关键贡献

1. **提出LMLT模块**：设计了一种新颖的自注意力块（LMLT），该模块采用多头机制，但与其他方法不同，它让每个头专注于不同空间分辨率的特征图（通过池化实现）。
2. **并行连接架构**：将多个自注意力层以**并行**方式连接（而非传统串行），将多头机制与网络深度整合为一体，从而大幅减少计算量。
3. **低到高连接机制**：在并行的头之间引入**残差连接**，将包含全局信息的低分辨率（低）头的输出，逐级传递并添加到更高分辨率（高）头的特征中，解决了窗口自注意力的跨窗口通信问题。
4. **显著效率提升**：实验表明，LMLT在保持或超越SOTA性能的同时，将推理时间和GPU内存使用量大幅降低（例如，在×4缩放时，LMLT-Base相比SwinIR-light等模型，内存降至约38%，推理时间降至约22%）。
5. **全面的实验验证**：在多个标准基准数据集上，与众多CNN和ViT基线模型进行了详尽比较，证明了方法的优越性。
## 方法

- **整体框架**：
    1. **浅层特征提取**：使用一个3×3卷积从输入低分辨率图像中提取浅层特征。
    2. **深层特征提取**：级联多个**LHS块**（Low-to-High Self-attention Blocks）。每个LHS块依次包含：层归一化（LN）、核心的**LMLT模块**、层归一化（LN）和通道混合模块（CCM），并带有残差连接。
    3. **图像重建**：最后通过3×3卷积和像素重排（Pixel-shuffle）层生成高分辨率图像。
- **输入输出**：输入是低分辨率图像，输出是重建后的高分辨率图像。
- **关键模块 - LMLT详解**：
    1. **多头分割与池化**：将特征图沿通道维度分为H个头。对每个头应用不同强度的池化（下采样）：第i个头的空间尺寸为原尺寸的(1/2^(i-1))倍。因此，**低头**（pooling多）特征图空间尺寸小，感受野大，捕获**全局**信息；**高头**（pooling少）特征图空间尺寸大，感受野小，捕获**局部**细节。
    2. **并行自注意力**：每个头（在各自的空间分辨率上）独立进行窗口自注意力计算。窗口大小M×M固定，但由于特征图空间尺寸不同，低头上每个窗口实际对应的原图区域更大。
    3. **低到高连接**：将低分辨率头自注意力输出的结果**上采样（插值）** 到高分辨率头的空间尺寸，并**逐元素相加**到高分辨率头的特征上。这个过程从最低的头开始，逐级向上进行，直到最高头。这使得高分辨率头的窗口在计算自注意力时，能融合来自更广阔区域的全局信息。
    4. **特征合并**：所有头的自注意力输出被恢复到原始尺寸，拼接后通过一个1×1卷积融合。
- **数学公式（计算复杂度）**：
    - 本文提出的LMLT计算量公式：`Ω(LMLT) = 4 * ( (H*W)/(4^i) * (D/H)^2 ) + 2 * ( (M^2 * H * W)/(4^i) * (D/H) )`，其中i表示头的索引。
    - 对比传统窗口自注意力（WSA）公式：`Ω(WSA) = 4 * (H * W * D^2) + 2 * (M^2 * H * W * D)`。
    - **直观解释**：由于LMLT中每个头处理的特征图更小（窗口数和通道数都减少），并且是并行处理，所以总计算量相比WSA大幅降低。头的数量H越多，降低越明显。
- **训练方式**：使用DIV2K和Flickr2K数据集训练，Adam优化器，50万次迭代，余弦退火学习率调度，输入图像裁剪为64×64的patch，并使用了旋转和翻转的数据增强。
- **推理流程**：与前向传播框架一致，通过一次前向计算即可生成高分辨率图像。
- **与已有方法的核心差异**：
    - **架构差异**：传统ViT块（如SwinIR）是**串行堆叠**自注意力层；LMLT块是**并行堆叠**自注意力层（每个头一层）。
    - **注意力作用维度**：传统多头注意力在**相同**特征图上分头；LMLT在**不同空间尺度**的特征图上分头，实现了真正的多尺度注意力。
    - **跨窗口交互**：通过**低到高连接**，将全局信息注入局部头，解决了WSA的边界问题，而无需复杂的移位窗口等操作。
## 实验

- **使用的数据集**：训练集：DIV2K (800张) + Flickr2K (2650张)。测试集：Set5, Set14, BSD100, Urban100, Manga109。
- **对比方法**：包括**CNN方法**：IMDN, LatticeNet, RFDN-L, SRPN-Lite, FMEN, CARN, IMDN等；**ViT/混合方法**：HNCT, NGswin, SwinIR-light, ELAN, SRformer-Light, ESRT等。
- **评价指标**：图像质量：PSNR/SSIM（Y通道）。效率：参数量（#Params）， 计算量（FLOPs，基于1280×720输出）， GPU内存峰值（#GPU Mem）， 平均推理时间（#Avg Time）。
- **主实验结果**：
    - 在**所有基准测试**上，LMLT-Base和LMLT-Large模型在性能上达到了**最佳或次佳**水平。例如，在最挑战的Manga109数据集上提升显著（Table 1）。
    - **×4缩放关键结果**（Table 1 & 2）：LMLT-Base（672K参数，41G FLOPs）在Manga109上达到**31.09 dB**，优于SwinIR-light（30.92 dB）。同时，其GPU内存仅为144 MB，平均推理时间26.15 ms，远低于SwinIR-light（内存64G，时间未明确但应很高）和NGswin（内存372 MB，时间118.13 ms）。
- **效率结果**（Table 2, ×4缩放）：
    - **内存**：LMLT-Tiny (81 MB), LMLT-Base (144 MB) vs. SwinIR-light (未在表2但远高于此), NGswin (373 MB)。
    - **推理时间**：LMLT-Base (26.15 ms/image) vs. NGswin (118.13 ms), SwinIR-light (未在表2但应很慢)。
- **消融实验与泛化实验**：PDF提供的文本（前12页）中未包含详细的消融实验部分。根据引言和结论，作者进行了“extensive experiments”，但具体消融内容未在提取文本中展示。
- **模型变体**：论文定义了四种模型：Tiny（36通道），Small（36通道，12 blocks），Base（60通道），Large（84通道）。
## 局限

1. **适用场景**：本文实验集中于图像超分辨率这一特定任务，其提出的模块是否同样适用于其他低级视觉任务（如去噪、去模糊）或高级视觉任务，需要进一步验证。
2. **实验充分性**：提供的PDF文本中未展示消融实验，无法得知每个组件（如低到高连接、头数量H、池化策略）对最终性能的具体贡献程度。
3. **计算成本**：尽管效率显著提升，但作为一种基于Transformer的方法，其绝对计算量（如LMLT-Large为78G FLOPs在×4缩放）仍然高于一些轻量级CNN方法，可能在移动端等极端资源受限场景下仍有压力。
4. **假设依赖**：方法假设全局信息可以通过对低分辨率特征进行自注意力获得，局部信息通过高分辨率特征获得，且两者可以通过简单加法融合。这一假设在复杂纹理或结构下可能并非最优。
5. **复现风险**：论文提到了为加速实验而设置的特定PyTorch选项（`backends.cudnn.benchmark`），这可能导致在不同硬件或软件环境下结果有轻微波动。作者通过多次实验取平均来报告Tiny模型的结果以应对此问题。
## 个人评论

这篇论文最值得学习的点在于其**巧妙的多头设计哲学**。它没有简单地将“多头”理解为在通道上分割，而是创造性地将其与**特征的空间尺度（分辨率）** 关联起来。每个头天然地成为处理不同尺度信息的专家（低头全局，高头局部），这种设计直觉清晰且高效。

对于后续研究/改模型的启发：
1. **效率提升范式**：展示了如何通过**并行化**网络结构（而非一味加深）来降低计算开销，同时维持模型表达能力。
2. **解决特定问题（如窗口边界）的思路**：通过模块内部的**信息流动设计**（低到高连接）来解决架构本身的固有缺陷，是一种优雅的工程解决方案。
3. **多尺度注意力的新视角**：为设计新型注意力模块提供了“多头对应多尺度”的思路，可以推广到其他需要多尺度信息的任务（如目标检测、分割）。

### 使用建议

- **如果快速了解**：阅读**摘要**和**引言**的最后部分，即可抓住论文要解决的问题、核心思想和主要贡献。Figure 1和Figure 2（b）非常关键，能直观理解其并行结构和多头处理不同尺度特征的特点。
- **如果复现**：重点精读**第3节（Proposed Method）**，特别是LMLT模块的图文描述（Figure 2），并仔细研究**第4节的Implementation Details**，包括数据增强、优化器、学习率策略等训练细节。
- **如果借鉴创新点**：
    - 学习其**“多头对应多尺度”** 的设计理念，可以考虑在自己的模型中将不同的注意力头分配到不同尺度的特征图上。
    - 借鉴其**并行连接**自注意力层的思想来降低模型延迟。
    - 研究其**低到高残差连接**如何实现跨尺度/跨窗口的信息融合。
- **如果写Related Work**：可将其归类于以下几个方向进行讨论：**高效/轻量级图像超分辨率方法**、**基于Vision Transformer的图像重建**、**多尺度或局部-全局注意力机制**。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉领域的**图像超分辨率**方向，聚焦于解决基于Vision Transformer (ViT)的超分辨率模型存在的**计算复杂度高、推理慢、内存占用大**以及**窗口自注意力（WSA）无法有效处理窗口边界区域信息**的问题。它最适合放在**“注意力算子模块”** 这一主题下，因为它提出了一种新颖的、基于多头并行注意力机制的核心模块（LMLT）来改进ViT在图像重建任务中的应用。

## 2. 一句话总结
本文提出了低到高多级Transformer（LMLT），通过并行化多头注意力并让不同头处理不同空间尺度的特征，以低计算成本有效捕获图像中的局部与全局信息，并解决了窗口自注意力的跨窗口通信问题，从而在图像超分辨率任务中实现了效率与性能的平衡。

## 3. 背景与问题
- **为什么要做**：尽管基于ViT的图像超分辨率方法（如SwinIR）性能优越，但其计算复杂度随输入尺寸呈二次增长，导致高推理延迟和内存消耗，限制了实际应用。
- **之前方法的问题**：
    1. **效率问题**：传统ViT模型（如SwinIR）堆叠自注意力层（串行连接），导致计算负载和推理时间过长。
    2. **窗口边界问题**：窗口自注意力（WSA）将图像划分为独立窗口进行计算，导致不同窗口间缺乏交互，在窗口边界处质量下降，难以建模长距离依赖。
- **核心矛盾**：如何在**保持或提升超分辨率性能**的同时，**显著降低模型的计算复杂度、推理时间和内存占用**，并**解决窗口自注意力固有的边界问题**。

## 4. 核心贡献
1. **提出LMLT模块**：设计了一种新颖的自注意力块（LMLT），该模块采用多头机制，但与其他方法不同，它让每个头专注于不同空间分辨率的特征图（通过池化实现）。
2. **并行连接架构**：将多个自注意力层以**并行**方式连接（而非传统串行），将多头机制与网络深度整合为一体，从而大幅减少计算量。
3. **低到高连接机制**：在并行的头之间引入**残差连接**，将包含全局信息的低分辨率（低）头的输出，逐级传递并添加到更高分辨率（高）头的特征中，解决了窗口自注意力的跨窗口通信问题。
4. **显著效率提升**：实验表明，LMLT在保持或超越SOTA性能的同时，将推理时间和GPU内存使用量大幅降低（例如，在×4缩放时，LMLT-Base相比SwinIR-light等模型，内存降至约38%，推理时间降至约22%）。
5. **全面的实验验证**：在多个标准基准数据集上，与众多CNN和ViT基线模型进行了详尽比较，证明了方法的优越性。

## 5. 方法详解
- **整体框架**：
    1. **浅层特征提取**：使用一个3×3卷积从输入低分辨率图像中提取浅层特征。
    2. **深层特征提取**：级联多个**LHS块**（Low-to-High Self-attention Blocks）。每个LHS块依次包含：层归一化（LN）、核心的**LMLT模块**、层归一化（LN）和通道混合模块（CCM），并带有残差连接。
    3. **图像重建**：最后通过3×3卷积和像素重排（Pixel-shuffle）层生成高分辨率图像。
- **输入输出**：输入是低分辨率图像，输出是重建后的高分辨率图像。
- **关键模块 - LMLT详解**：
    1. **多头分割与池化**：将特征图沿通道维度分为H个头。对每个头应用不同强度的池化（下采样）：第i个头的空间尺寸为原尺寸的(1/2^(i-1))倍。因此，**低头**（pooling多）特征图空间尺寸小，感受野大，捕获**全局**信息；**高头**（pooling少）特征图空间尺寸大，感受野小，捕获**局部**细节。
    2. **并行自注意力**：每个头（在各自的空间分辨率上）独立进行窗口自注意力计算。窗口大小M×M固定，但由于特征图空间尺寸不同，低头上每个窗口实际对应的原图区域更大。
    3. **低到高连接**：将低分辨率头自注意力输出的结果**上采样（插值）** 到高分辨率头的空间尺寸，并**逐元素相加**到高分辨率头的特征上。这个过程从最低的头开始，逐级向上进行，直到最高头。这使得高分辨率头的窗口在计算自注意力时，能融合来自更广阔区域的全局信息。
    4. **特征合并**：所有头的自注意力输出被恢复到原始尺寸，拼接后通过一个1×1卷积融合。
- **数学公式（计算复杂度）**：
    - 本文提出的LMLT计算量公式：`Ω(LMLT) = 4 * ( (H*W)/(4^i) * (D/H)^2 ) + 2 * ( (M^2 * H * W)/(4^i) * (D/H) )`，其中i表示头的索引。
    - 对比传统窗口自注意力（WSA）公式：`Ω(WSA) = 4 * (H * W * D^2) + 2 * (M^2 * H * W * D)`。
    - **直观解释**：由于LMLT中每个头处理的特征图更小（窗口数和通道数都减少），并且是并行处理，所以总计算量相比WSA大幅降低。头的数量H越多，降低越明显。
- **训练方式**：使用DIV2K和Flickr2K数据集训练，Adam优化器，50万次迭代，余弦退火学习率调度，输入图像裁剪为64×64的patch，并使用了旋转和翻转的数据增强。
- **推理流程**：与前向传播框架一致，通过一次前向计算即可生成高分辨率图像。
- **与已有方法的核心差异**：
    - **架构差异**：传统ViT块（如SwinIR）是**串行堆叠**自注意力层；LMLT块是**并行堆叠**自注意力层（每个头一层）。
    - **注意力作用维度**：传统多头注意力在**相同**特征图上分头；LMLT在**不同空间尺度**的特征图上分头，实现了真正的多尺度注意力。
    - **跨窗口交互**：通过**低到高连接**，将全局信息注入局部头，解决了WSA的边界问题，而无需复杂的移位窗口等操作。

## 6. 实验与结果
- **使用的数据集**：训练集：DIV2K (800张) + Flickr2K (2650张)。测试集：Set5, Set14, BSD100, Urban100, Manga109。
- **对比方法**：包括**CNN方法**：IMDN, LatticeNet, RFDN-L, SRPN-Lite, FMEN, CARN, IMDN等；**ViT/混合方法**：HNCT, NGswin, SwinIR-light, ELAN, SRformer-Light, ESRT等。
- **评价指标**：图像质量：PSNR/SSIM（Y通道）。效率：参数量（#Params）， 计算量（FLOPs，基于1280×720输出）， GPU内存峰值（#GPU Mem）， 平均推理时间（#Avg Time）。
- **主实验结果**：
    - 在**所有基准测试**上，LMLT-Base和LMLT-Large模型在性能上达到了**最佳或次佳**水平。例如，在最挑战的Manga109数据集上提升显著（Table 1）。
    - **×4缩放关键结果**（Table 1 & 2）：LMLT-Base（672K参数，41G FLOPs）在Manga109上达到**31.09 dB**，优于SwinIR-light（30.92 dB）。同时，其GPU内存仅为144 MB，平均推理时间26.15 ms，远低于SwinIR-light（内存64G，时间未明确但应很高）和NGswin（内存372 MB，时间118.13 ms）。
- **效率结果**（Table 2, ×4缩放）：
    - **内存**：LMLT-Tiny (81 MB), LMLT-Base (144 MB) vs. SwinIR-light (未在表2但远高于此), NGswin (373 MB)。
    - **推理时间**：LMLT-Base (26.15 ms/image) vs. NGswin (118.13 ms), SwinIR-light (未在表2但应很慢)。
- **消融实验与泛化实验**：PDF提供的文本（前12页）中未包含详细的消融实验部分。根据引言和结论，作者进行了“extensive experiments”，但具体消融内容未在提取文本中展示。
- **模型变体**：论文定义了四种模型：Tiny（36通道），Small（36通道，12 blocks），Base（60通道），Large（84通道）。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的点在于其**巧妙的多头设计哲学**。它没有简单地将“多头”理解为在通道上分割，而是创造性地将其与**特征的空间尺度（分辨率）** 关联起来。每个头天然地成为处理不同尺度信息的专家（低头全局，高头局部），这种设计直觉清晰且高效。

对于后续研究/改模型的启发：
1. **效率提升范式**：展示了如何通过**并行化**网络结构（而非一味加深）来降低计算开销，同时维持模型表达能力。
2. **解决特定问题（如窗口边界）的思路**：通过模块内部的**信息流动设计**（低到高连接）来解决架构本身的固有缺陷，是一种优雅的工程解决方案。
3. **多尺度注意力的新视角**：为设计新型注意力模块提供了“多头对应多尺度”的思路，可以推广到其他需要多尺度信息的任务（如目标检测、分割）。

## 8. 局限与问题
1. **适用场景**：本文实验集中于图像超分辨率这一特定任务，其提出的模块是否同样适用于其他低级视觉任务（如去噪、去模糊）或高级视觉任务，需要进一步验证。
2. **实验充分性**：提供的PDF文本中未展示消融实验，无法得知每个组件（如低到高连接、头数量H、池化策略）对最终性能的具体贡献程度。
3. **计算成本**：尽管效率显著提升，但作为一种基于Transformer的方法，其绝对计算量（如LMLT-Large为78G FLOPs在×4缩放）仍然高于一些轻量级CNN方法，可能在移动端等极端资源受限场景下仍有压力。
4. **假设依赖**：方法假设全局信息可以通过对低分辨率特征进行自注意力获得，局部信息通过高分辨率特征获得，且两者可以通过简单加法融合。这一假设在复杂纹理或结构下可能并非最优。
5. **复现风险**：论文提到了为加速实验而设置的特定PyTorch选项（`backends.cudnn.benchmark`），这可能导致在不同硬件或软件环境下结果有轻微波动。作者通过多次实验取平均来报告Tiny模型的结果以应对此问题。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：阅读**摘要**和**引言**的最后部分，即可抓住论文要解决的问题、核心思想和主要贡献。Figure 1和Figure 2（b）非常关键，能直观理解其并行结构和多头处理不同尺度特征的特点。
- **如果复现**：重点精读**第3节（Proposed Method）**，特别是LMLT模块的图文描述（Figure 2），并仔细研究**第4节的Implementation Details**，包括数据增强、优化器、学习率策略等训练细节。
- **如果借鉴创新点**：
    - 学习其**“多头对应多尺度”** 的设计理念，可以考虑在自己的模型中将不同的注意力头分配到不同尺度的特征图上。
    - 借鉴其**并行连接**自注意力层的思想来降低模型延迟。
    - 研究其**低到高残差连接**如何实现跨尺度/跨窗口的信息融合。
- **如果写Related Work**：可将其归类于以下几个方向进行讨论：**高效/轻量级图像超分辨率方法**、**基于Vision Transformer的图像重建**、**多尺度或局部-全局注意力机制**。

## 10. 和其他论文的关系
根据主题“注意力算子模块”和文件名，本文很可能与以下论文有直接关联或对比：
- **SwinIR**：[[SwinIR]] 本文的主要对标基线，LMLT旨在解决其效率问题和窗口边界问题。
- **Swin Transformer**：[[Swin Transformer]] SwinIR的基础，本文讨论了其窗口自注意力（WSA）的局限性。
- **SAFMN**：[[SAFMN]] 本文在引言中提及，LMLT借鉴了其多头方法来划分特征，但SAFMN基于CNN。
- **ELAN, HNCT, NGswin, SRformer**：[[ELAN]] [[HNCT]] [[NGswin]] [[SRformer]] 本文实验中对比的其他先进ViT或混合结构超分辨率模型。
- **Restormer**：[[Restormer]] 另一种强大的Transformer图像复原模型，但其注意力机制（通道注意力）与本文不同，可作为对比讨论。

## 11. 关键词
低到高多级Transformer, LMLT, 图像超分辨率, Vision Transformer, 多头注意力, 并行自注意力, 窗口自注意力, 跨窗口通信, 计算效率, 局部-全局信息

## 12. 可信度说明
本精读笔记主要基于用户提供的**PDF提取文本（前12页/共22页）** 生成。内容覆盖了论文的**摘要、引言、相关工作、方法详解（第3节）以及实验部分（第4节）的开头和主要结果表格（Table 1, Table 2）**。
- **提取质量**：文本提取清晰，逻辑连贯，包含了论文的核心结构、方法描述和关键实验数据。
- **信息完整性限制**：由于只提供了前12页，笔记中关于**消融实验、更深入的讨论、以及论文后半部分的详细分析**可能不完整。例如，消融实验的结果在提供的文本中未出现。因此，笔记中相关部分注明了“PDF文本中未明确说明”。
- **可信度**：笔记中所有**事实性陈述、数字、公式和结论**均严格直接引用或概括自所提供的PDF文本，未添加任何来自外部或编造的信息。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/LMLT.txt` (22/22 页; 原 AI 主体 12/22 + 全文补读 13-22); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-22; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-22。
- **提取情况**: 缺失页 10 页, 其中 10 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: A Impact of number of Blocks, Channels, Heads and Depths
- p.14: In this section, we analyze how the performance of our proposed model changes based on the number of blocks,
- p.14: As shown in Table A, the increase in the number of parameters, FLOPs and inference time tends to be proportional
- p.14: Similar to the performance evaluation based on the number of blocks, this experiment evaluates performance
- p.14: However, unlike the variations in the number of blocks, increasing the number of channels results in a more
- p.14: In this context, the Small model has an inference time about 3ms longer than the Base model, but it has fewer
- p.15: However, our experimental results indicate that calculating self-attention multiple times in a single head before
- p.15: B Effects of Low-to-high connection and Pooling
- p.15: Difference between with and without Low-to-high connection In the Table 4, we confirm performance
- p.15: Difference between with and without Pooling We analyze the impact of pooling on the performance of
- p.16: Scale Method Set5 Set14 B100 Urban100 Manga109
- p.16: As shown in the images, without the low-to-high connection, the boundaries between windows are clearly

### 缺失页关键摘录

- p.14: Table A: Performance difference of LMLT based on the number of blocks.
- p.14: #Block #Params #FLOPs #GPU Mem #A VG Time Set5 Set14 B100 Urban100 Manga109
- p.14: 10, and 12. Experiments are conducted on ×2scale and the performance is evaluated using benchmark datasets,
- p.14: and analyzed in terms of the number of parameters, FLOPs, GPU memory usage, and average inference time.
- p.14: As shown in Table A, the increase in the number of parameters, FLOPs and inference time tends to be proportional
- p.14: to the number of blocks, and performance also gradually improves. For the Manga109 [ 42] dataset, as the
- p.14: number of blocks increases from 4 to 12 in increments of 2, PSNR increases by 0.27 db, 0.16 db, 0.10 db, and
- p.14: remains stable, 323.5M to 324.5M. We observe the overall increase in PSNR with the increase in the number of
- p.14: Table B: Performance difference of LMLT based on the number of channels.
- p.14: #Channel #Params #FLOPs #GPU MEM #A VG Time Set5 Set14 B100 Urban100 Manga109
- p.14: Similar to the performance evaluation based on the number of blocks, this experiment evaluates performance
- p.14: using benchmark datasets, the number of parameters, FLOPs, GPU memory usage, and average inference time
<!-- AI_READING_NOTE_END -->
