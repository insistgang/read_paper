---
title: ThisCVPRpaperistheOpenAccessversion,providedbytheComputerVisionFoundation.
authors:
  - "Shihao Zhou"
  - "Duosheng Chen"
  - "Jinshan Pan"
  - "Jinglei Shi"
  - "Jufeng Yang"
year: 2024
venue: "CVPR"
doi: 
pdf: [[ASSA&FRFN.pdf]]
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
extract_cache: .paper-cache/extracts/ASSA&FRFN.txt
---

# ThisCVPRpaperistheOpenAccessversion,providedbytheComputerVisionFoundation.

## 基本信息
- **PDF**: [[ASSA&FRFN.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | ThisCVPRpaperistheOpenAccessversion,providedbytheComputerVisionFoundation. |
| **作者** | Shihao Zhou; Duosheng Chen; Jinshan Pan; Jinglei Shi; Jufeng Yang |
| **发表时间** | 2024 |
| **刊物/会议** | CVPR |
| **DOI** | 未明确 |

## 摘要

> Transformer-basedapproacheshaveachievedpromising performance in image restoration tasks, given their ability tomodellong-rangedependencies,whichiscrucialforre- Dense Redundant Relations Features covering clear images. Though diverse efficient attention mechanism designs have addressed the intensive compu- MSA FFN MSA FFN tations associated with using transformers, they often in- (a)PreviousstandardTransformer-basedmethod volve redundant information and noisy interactions from irrelevant regions by considering all available tokens. In this work, we propose an Adaptive Sparse Transformer (AST)tomitigatethenoisyinteractionsofirrelevantareas and remove feature redundancy in both spatial and chan- Sparse Compact nel domains. AST comprises two core designs, i.e., an Relations Features Adaptive Sparse Self-Attention (ASSA) block and a Fea- ture Refinement Feed-forward Network (FRFN). Specifi- ASSA FRFN ASSA FRFN cally, ASSA is adaptively computed using a two-branch (b)OurAdaptiveSparseTransfo

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：Transformer因其建模长距离依赖的能力在图像恢复中表现出色。然而，标准Transformer的**密集注意力机制**会引入无关区域的噪声交互，且通过所有可用token计算会带来**特征冗余**问题，阻碍了模型关注信息性特征。
- **之前方法的问题**：1) 为了降低计算复杂度，高效注意力机制（如窗口注意力、通道注意力）被提出，但它们仍会考虑所有token，无法避免噪声交互和冗余。2) 一些方法（如Top-K选择、超像素投影）试图解决冗余，但Top-K的参数K对任务敏感，而超像素空间内的注意力仍会涉及所有token。
- **核心矛盾**：如何在保证网络中有足够信息流的同时，有效**过滤掉无关区域的噪声交互**，并**消除特征表示中的冗余信息**。
## 关键贡献

1.  提出了**自适应稀疏变换器（AST）**，一个用于图像恢复的高效Transformer模型，通过促进最有用信息的流动来提取更有效的特征。
2.  设计了**自适应稀疏自注意力（ASSA）块**，它包含一个密集自注意力分支（DSA）和一个稀疏自注意力分支（SSA），通过自适应权重融合，既能过滤噪声交互又能保留必要信息。
3.  开发了**特征精炼前馈网络（FRFN）**，采用“增强-缓解”方案，增强特征图中有用的部分，同时通过门控机制减少通道维度的冗余，与ASSA形成空间与通道的互补。
## 方法

- **整体框架**：AST采用对称的编码器-解码器结构（见图2）。编码器阶段仅使用FRFN，解码器阶段使用ASSA和FRFN。编码器和解码器之间通过跳跃连接融合特征。一个共享的瓶颈阶段位于解码器之前。
- **输入输出**：输入为退化图像 `I`，先通过卷积层得到浅层特征 `F0`，经过编码器-解码器网络得到深层特征 `Fd`，最后通过卷积层预测残差图像 `R`。输出恢复图像为 `Î = I + R`。
- **关键模块**：
    1.  **自适应稀疏自注意力（ASSA）**：其核心是**双分支结构**。
        - **稀疏自注意力分支（SSA）**：使用平方ReLU激活函数 `ReLU^2(QK^T/√d + B)` 来计算注意力分数。这会过滤掉负值（低相关性）的交互，实现稀疏性，但可能导致信息损失。
        - **密集自注意力分支（DSA）**：使用标准的Softmax函数 `Softmax(QK^T/√d + B)` 计算注意力分数。这能保留所有交互，确保信息流，但会引入噪声。
        - **自适应融合**：两个分支的注意力结果 `A_ssa` 和 `A_dsa` 通过可学习的权重 `w1` 和 `w2` 进行加权融合 `A = (w1 * SSA + w2 * DSA) V`。权重通过一个类似softmax的公式自适应计算，使模型能根据任务需要平衡稀疏性与信息保留。
    2.  **特征精炼前馈网络（FRFN）**：采用“增强-缓解”方案。
        - 首先使用**部分卷积（PConv）** 和线性投影增强特征的有用部分。
        - 然后将特征通道分割为两部分，其中一部分经过重塑（Reshape）为2D特征图后，通过深度可分离卷积（DWConv）和门控机制（与另一部分进行矩阵乘法）来**抑制冗余信息**。
        - 最后通过另一个线性投影输出精炼后的特征。
- **模块连接**：在解码器的基本块中，特征先经过Layer Norm，然后输入到ASSA模块，之后再经过Layer Norm输入到FRFN模块。
- **数学公式**：关键公式如公式(5) SSA， 公式(6)自适应融合，以及公式(8) FRFN的操作流程，直观地展示了稀疏化、融合与精炼的过程。
- **训练方式**：使用Charbonnier损失函数（公式1）进行端到端训练。采用AdamW优化器、余弦学习率衰减策略和渐进式学习策略。
- **推理流程**：与标准编码器-解码器网络推理流程一致，输入退化图像，输出恢复图像。文中也提到了可采用几何自集成策略（“+”版本）来提升性能。
- **与已有方法的差异**：
    - **注意力作用维度**：ASSA作用于**空间维度**（在窗口内计算），通过稀疏化来减少空间域的噪声交互。而FRFN作用于**通道维度**，通过门控机制减少通道冗余。两者形成空间-通道的互补。
    - **计算量 vs 效果**：通过稀疏化和自适应选择，AST旨在用相对更少的噪声交互获得更好的恢复效果，但文中未明确说明AST相比标准Transformer或Restormer等方法的详细计算量（FLOPs）对比。
    - **论文类型特化**：作为注意力算子模块，ASSA的设计思想（双分支稀疏-密集融合）可以作为一个可插入的组件，其计算量主要增加了一个并行的注意力分支和自适应权重计算，但旨在通过过滤噪声来提升模型效能。
## 实验

- **使用数据集**：
    - **雨条纹去除**：SPAD [78] 数据集。
    - **真实雾去除**：Dense-Haze [1] 数据集。
    - **雨滴去除**：AGAN-Data [58] 数据集。
- **对比方法**：DDN, RESCAN, PReNet, RCDNet, SPDNet, SPAIR, DualGCN, SEIDNet, MPRNet, Restormer, SCD-Former, IDT, Uformer, DRSformer等十余种CNN和Transformer方法。
- **评价指标**：PSNR, SSIM（对去雨任务在YCbCr空间的Y通道计算），以及非参考指标NIQE（文本中提及）。
- **主实验结果**：
    - **雨条纹去除**（表1）：AST-B在SPAD数据集上取得**49.51 dB**的PSNR和0.9942的SSIM，相比之前的最佳方法DRSformer（48.53 dB）提升了近1 dB。
    - **真实雾去除**（表3）：AST-B在Dense-Haze数据集上取得**17.12 dB**的PSNR和0.55的SSIM，优于Restormer（15.78 dB）和DeHamer（16.62 dB）等。
    - **雨滴去除**（表2）：AST-B在AGAN-Data数据集上取得**32.32 dB**的PSNR和0.935的SSIM，同样取得了最佳性能。
- **消融实验**：文中提到了进行了广泛的消融研究以验证设计的有效性（在摘要和贡献部分提及），但提供的PDF文本中未包含具体的消融实验表格和数据。
- **泛化实验**：论文在三个不同类型（雨、雾、雨滴）的退化任务上验证了方法的**泛化能力**和**多功能性**。
- **速度/参数量/FLOPs**：提供的PDF文本中**未明确说明**AST模型（如AST-B）的具体参数量、FLOPs或推理速度。
## 局限

- **计算成本**：尽管旨在高效，但双分支注意力（SSA和DSA）的并行计算可能仍会带来一定的计算开销，论文未详细分析其与轻量级方法（如纯通道注意力）的效率对比。
- **参数敏感性**：ASSA的自适应权重由可学习参数初始化，其最终学习到的权重如何随任务变化，以及是否对初始化敏感，值得探讨。
- **实验全面性**：虽然覆盖了三类退化，但都是低级视觉任务。未在更广泛的视觉任务（如去模糊、超分辨率）或更高分辨率图像上验证，其泛化边界尚不完全清晰。
- **假设依赖**：方法建立在窗口划分和自注意力计算之上，对于非局部模式或极远距离依赖的建模能力，受限于窗口大小。
- **复现细节**：提供的PDF文本中**未找到**关于具体窗口划分策略、相对位置偏置实现细节以及完整的网络层数配置等足以完全复现的细节。
## 个人评论

1.  **双分支自适应注意力机制**：ASSA模块的设计思想非常值得学习。它没有在“稀疏”和“密集”之间二选一，而是创新性地将两者结合，并通过一个简单的自适应权重让模型自己学习如何平衡。这为设计更灵活、鲁棒的注意力机制提供了新思路。
2.  **空间与通道的互补精炼**：论文清晰地指出了ASSA解决空间域冗余，FRFN解决通道域冗余，两者协同工作。这种对特征冗余问题进行多维度解耦并分别处理的设计策略，对于改进网络模块具有普适的启发意义。
3.  **简洁有效的FRFN设计**：FRFN中的“增强-缓解”方案（PConv增强 + 门控缓解）实现简单，效果显著，展示了在前馈网络（FFN）中进行精细特征控制的潜力，是一个可以借鉴到其他视觉任务中的有效模块。

### 使用建议

- **快速了解**：只读**Abstract**、**Introduction**、**Fig. 1** 和 **Fig. 2**，以及 **Experiments** 部分的表格和关键结论，即可掌握核心思想和主要成果。
- **复现**：重点精读 **Section 3 (Proposed Method)**，尤其是3.1整体流水线和3.2 AST Block Design中的公式与描述，并结合 **Section 4.1 Implementation Details** 中的超参数设置。
- **借鉴创新点**：
    - 若想改进注意力机制，可深入学习**ASSA的双分支设计**及其自适应融合公式（6, 7）。
    - 若想改进前馈网络（FFN），可借鉴**FRFN的“增强-缓解”方案**和门控机制（公式8）。
- **写Related Work**：可将本文归类在“图像恢复中的Transformer方法”或“高效/稀疏注意力机制”相关工作中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的**图像恢复**（Image Restoration）方向，旨在解决从退化图像（如含雨条纹、雾、雨滴的图像）中恢复出清晰图像的问题。论文的核心创新点在于提出了一个新的注意力算子模块（Attention Operator Module），即自适应稀疏自注意力（ASSA）和特征精炼前馈网络（FRFN），并基于此构建了一个完整的图像恢复模型。因此，本文非常适合放在 **“B_注意力算子模块”** 这一主题下。

## 2. 一句话总结
本文提出了一种自适应稀疏变换器（AST），通过双分支的自适应稀疏自注意力（ASSA）和特征精炼前馈网络（FRFN），自适应地过滤掉注意力计算中的噪声交互并减少特征图中的冗余信息，从而在多个图像恢复任务中取得优异性能。

## 3. 背景与问题
- **为什么要做**：Transformer因其建模长距离依赖的能力在图像恢复中表现出色。然而，标准Transformer的**密集注意力机制**会引入无关区域的噪声交互，且通过所有可用token计算会带来**特征冗余**问题，阻碍了模型关注信息性特征。
- **之前方法的问题**：1) 为了降低计算复杂度，高效注意力机制（如窗口注意力、通道注意力）被提出，但它们仍会考虑所有token，无法避免噪声交互和冗余。2) 一些方法（如Top-K选择、超像素投影）试图解决冗余，但Top-K的参数K对任务敏感，而超像素空间内的注意力仍会涉及所有token。
- **核心矛盾**：如何在保证网络中有足够信息流的同时，有效**过滤掉无关区域的噪声交互**，并**消除特征表示中的冗余信息**。

## 4. 核心贡献
1.  提出了**自适应稀疏变换器（AST）**，一个用于图像恢复的高效Transformer模型，通过促进最有用信息的流动来提取更有效的特征。
2.  设计了**自适应稀疏自注意力（ASSA）块**，它包含一个密集自注意力分支（DSA）和一个稀疏自注意力分支（SSA），通过自适应权重融合，既能过滤噪声交互又能保留必要信息。
3.  开发了**特征精炼前馈网络（FRFN）**，采用“增强-缓解”方案，增强特征图中有用的部分，同时通过门控机制减少通道维度的冗余，与ASSA形成空间与通道的互补。

## 5. 方法详解
- **整体框架**：AST采用对称的编码器-解码器结构（见图2）。编码器阶段仅使用FRFN，解码器阶段使用ASSA和FRFN。编码器和解码器之间通过跳跃连接融合特征。一个共享的瓶颈阶段位于解码器之前。
- **输入输出**：输入为退化图像 `I`，先通过卷积层得到浅层特征 `F0`，经过编码器-解码器网络得到深层特征 `Fd`，最后通过卷积层预测残差图像 `R`。输出恢复图像为 `Î = I + R`。
- **关键模块**：
    1.  **自适应稀疏自注意力（ASSA）**：其核心是**双分支结构**。
        - **稀疏自注意力分支（SSA）**：使用平方ReLU激活函数 `ReLU^2(QK^T/√d + B)` 来计算注意力分数。这会过滤掉负值（低相关性）的交互，实现稀疏性，但可能导致信息损失。
        - **密集自注意力分支（DSA）**：使用标准的Softmax函数 `Softmax(QK^T/√d + B)` 计算注意力分数。这能保留所有交互，确保信息流，但会引入噪声。
        - **自适应融合**：两个分支的注意力结果 `A_ssa` 和 `A_dsa` 通过可学习的权重 `w1` 和 `w2` 进行加权融合 `A = (w1 * SSA + w2 * DSA) V`。权重通过一个类似softmax的公式自适应计算，使模型能根据任务需要平衡稀疏性与信息保留。
    2.  **特征精炼前馈网络（FRFN）**：采用“增强-缓解”方案。
        - 首先使用**部分卷积（PConv）** 和线性投影增强特征的有用部分。
        - 然后将特征通道分割为两部分，其中一部分经过重塑（Reshape）为2D特征图后，通过深度可分离卷积（DWConv）和门控机制（与另一部分进行矩阵乘法）来**抑制冗余信息**。
        - 最后通过另一个线性投影输出精炼后的特征。
- **模块连接**：在解码器的基本块中，特征先经过Layer Norm，然后输入到ASSA模块，之后再经过Layer Norm输入到FRFN模块。
- **数学公式**：关键公式如公式(5) SSA， 公式(6)自适应融合，以及公式(8) FRFN的操作流程，直观地展示了稀疏化、融合与精炼的过程。
- **训练方式**：使用Charbonnier损失函数（公式1）进行端到端训练。采用AdamW优化器、余弦学习率衰减策略和渐进式学习策略。
- **推理流程**：与标准编码器-解码器网络推理流程一致，输入退化图像，输出恢复图像。文中也提到了可采用几何自集成策略（“+”版本）来提升性能。
- **与已有方法的差异**：
    - **注意力作用维度**：ASSA作用于**空间维度**（在窗口内计算），通过稀疏化来减少空间域的噪声交互。而FRFN作用于**通道维度**，通过门控机制减少通道冗余。两者形成空间-通道的互补。
    - **计算量 vs 效果**：通过稀疏化和自适应选择，AST旨在用相对更少的噪声交互获得更好的恢复效果，但文中未明确说明AST相比标准Transformer或Restormer等方法的详细计算量（FLOPs）对比。
    - **论文类型特化**：作为注意力算子模块，ASSA的设计思想（双分支稀疏-密集融合）可以作为一个可插入的组件，其计算量主要增加了一个并行的注意力分支和自适应权重计算，但旨在通过过滤噪声来提升模型效能。

## 6. 实验与结果
- **使用数据集**：
    - **雨条纹去除**：SPAD [78] 数据集。
    - **真实雾去除**：Dense-Haze [1] 数据集。
    - **雨滴去除**：AGAN-Data [58] 数据集。
- **对比方法**：DDN, RESCAN, PReNet, RCDNet, SPDNet, SPAIR, DualGCN, SEIDNet, MPRNet, Restormer, SCD-Former, IDT, Uformer, DRSformer等十余种CNN和Transformer方法。
- **评价指标**：PSNR, SSIM（对去雨任务在YCbCr空间的Y通道计算），以及非参考指标NIQE（文本中提及）。
- **主实验结果**：
    - **雨条纹去除**（表1）：AST-B在SPAD数据集上取得**49.51 dB**的PSNR和0.9942的SSIM，相比之前的最佳方法DRSformer（48.53 dB）提升了近1 dB。
    - **真实雾去除**（表3）：AST-B在Dense-Haze数据集上取得**17.12 dB**的PSNR和0.55的SSIM，优于Restormer（15.78 dB）和DeHamer（16.62 dB）等。
    - **雨滴去除**（表2）：AST-B在AGAN-Data数据集上取得**32.32 dB**的PSNR和0.935的SSIM，同样取得了最佳性能。
- **消融实验**：文中提到了进行了广泛的消融研究以验证设计的有效性（在摘要和贡献部分提及），但提供的PDF文本中未包含具体的消融实验表格和数据。
- **泛化实验**：论文在三个不同类型（雨、雾、雨滴）的退化任务上验证了方法的**泛化能力**和**多功能性**。
- **速度/参数量/FLOPs**：提供的PDF文本中**未明确说明**AST模型（如AST-B）的具体参数量、FLOPs或推理速度。

## 7. 这篇论文真正有价值的地方
1.  **双分支自适应注意力机制**：ASSA模块的设计思想非常值得学习。它没有在“稀疏”和“密集”之间二选一，而是创新性地将两者结合，并通过一个简单的自适应权重让模型自己学习如何平衡。这为设计更灵活、鲁棒的注意力机制提供了新思路。
2.  **空间与通道的互补精炼**：论文清晰地指出了ASSA解决空间域冗余，FRFN解决通道域冗余，两者协同工作。这种对特征冗余问题进行多维度解耦并分别处理的设计策略，对于改进网络模块具有普适的启发意义。
3.  **简洁有效的FRFN设计**：FRFN中的“增强-缓解”方案（PConv增强 + 门控缓解）实现简单，效果显著，展示了在前馈网络（FFN）中进行精细特征控制的潜力，是一个可以借鉴到其他视觉任务中的有效模块。

## 8. 局限与问题
- **计算成本**：尽管旨在高效，但双分支注意力（SSA和DSA）的并行计算可能仍会带来一定的计算开销，论文未详细分析其与轻量级方法（如纯通道注意力）的效率对比。
- **参数敏感性**：ASSA的自适应权重由可学习参数初始化，其最终学习到的权重如何随任务变化，以及是否对初始化敏感，值得探讨。
- **实验全面性**：虽然覆盖了三类退化，但都是低级视觉任务。未在更广泛的视觉任务（如去模糊、超分辨率）或更高分辨率图像上验证，其泛化边界尚不完全清晰。
- **假设依赖**：方法建立在窗口划分和自注意力计算之上，对于非局部模式或极远距离依赖的建模能力，受限于窗口大小。
- **复现细节**：提供的PDF文本中**未找到**关于具体窗口划分策略、相对位置偏置实现细节以及完整的网络层数配置等足以完全复现的细节。

## 9. 我该怎么使用这篇论文
- **快速了解**：只读**Abstract**、**Introduction**、**Fig. 1** 和 **Fig. 2**，以及 **Experiments** 部分的表格和关键结论，即可掌握核心思想和主要成果。
- **复现**：重点精读 **Section 3 (Proposed Method)**，尤其是3.1整体流水线和3.2 AST Block Design中的公式与描述，并结合 **Section 4.1 Implementation Details** 中的超参数设置。
- **借鉴创新点**：
    - 若想改进注意力机制，可深入学习**ASSA的双分支设计**及其自适应融合公式（6, 7）。
    - 若想改进前馈网络（FFN），可借鉴**FRFN的“增强-缓解”方案**和门控机制（公式8）。
- **写Related Work**：可将本文归类在“图像恢复中的Transformer方法”或“高效/稀疏注意力机制”相关工作中。

## 10. 和其他论文的关系
- 本文主要针对图像恢复任务中的注意力机制进行创新。与[[Restormer]]（提出通道注意力）、[[Uformer]]（提出窗口注意力）、[[DRSformer]]（提出Top-K通道选择）等同领域高效注意力论文有直接对比和演进关系。
- 其双分支稀疏-密集注意力思想，也可能与通用的稀疏Transformer研究相关。

## 11. 关键词
自适应稀疏变换器 (Adaptive Sparse Transformer, AST), 自适应稀疏自注意力 (Adaptive Sparse Self-Attention, ASSA), 特征精炼前馈网络 (Feature Refinement Feed-forward Network, FRFN), 图像恢复 (Image Restoration), 雨条纹去除 (Rain Streak Removal), 注意力稀疏化 (Attention Sparsification), 双分支架构 (Two-Branch Architecture)

## 12. 可信度说明
本精读笔记主要基于提供的**PDF文本前12页**生成，内容涵盖了摘要、引言、相关工作、方法详情和部分实验结果。笔记中所有具体数字（如PSNR、SSIM值）和公式均严格引用自文本。对于文本中未提及的信息（如部分消融实验细节、具体FLOPs、完整复现细节），已明确标注“PDF文本中未明确说明”或“PDF文本中未找到”。整体提取质量完整，核心方法与实验结果描述清晰。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/ASSA&FRFN.txt` (12/12 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
