---
title: Efficient Long-Range Attention Network for Image Super-resolution
authors:
  - "Xindong Zhang"
  - "Hui Zeng"
  - "Shi Guo"
  - "Lei Zhang"
year: 2022
venue: "ECCV"
doi: 
pdf: [[ELAB.pdf]]
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
extract_cache: .paper-cache/extracts/ELAB.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/20 pages"
---
# Efficient Long-Range Attention Network for Image Super-resolution

## 基本信息
- **PDF**: [[ELAB.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Efficient Long-Range Attention Network for Image Super-resolution |
| **作者** | Xindong Zhang; Hui Zeng; Shi Guo; Lei Zhang |
| **发表时间** | 2022 |
| **刊物/会议** | ECCV |
| **DOI** | 未明确 |

## 摘要

> Recently,transformer-basedmethodshavedemonstratedim- pressive results in various vision tasks, including image super-resolution (SR), by exploiting the self-attention (SA) for feature extraction. How- ever, the computation of SA in most existing transformer based models isveryexpensive,whilesomeemployedoperationsmayberedundantfor the SR task. This limits the range of SA computation and consequently theSRperformance.Inthiswork,weproposeanefficientlong-rangeat- tentionnetwork(ELAN)forimageSR.Specifically,wefirstemployshift convolution (shift-conv) to effectively extract the image local structural information while maintaining the same level of complexity as 1x1 con- volution, then propose a group-wise multi-scale self-attention (GMSA) module, which calculates SA on non-overlapped groups of features us- ing different window sizes to exploit the long-range image dependency. A highly efficient long-range attention block (ELAB) is then built by simply cascading two shift-conv with a GMSA mod

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

*   **为什么要做**：现有的CNN-based SR方法使用空间不变核，难以自适应建模像素间关系；而Transformer-based方法虽然能利用自注意力建模长程依赖，但SA计算复杂度随特征尺寸呈二次方增长，限制了其在特征尺寸大的SR任务中的应用。
*   **之前方法的问题**：
    1.  **SwinIR**：虽然结合了CNN和Transformer，但其设计（如相对位置偏移、遮罩机制、层归一化、多个残差子分支）对SR任务来说是冗余的。它在小固定窗口（8x8）内计算SA，限制了建模长程依赖的能力；使用1x1卷积提取局部特征，感受野小。
    2.  **Restormer**：在通道维度计算SA，但牺牲了重要的空间纹理和结构信息。
    3.  **其他尝试**（如Mei等）：将图像分成不重叠的patch独立计算SA，可能引入边界效应。
*   **核心矛盾**：如何在保持较低计算复杂度的同时，有效地建模图像中的长程依赖关系，以提升SR性能。
## 关键贡献

1.  提出了**高效长程注意力模块（ELAB）**，通过级联移位卷积和GMSA来建模图像长程依赖。
2.  提出了**移位卷积（shift-conv）**，以接近1x1卷积的计算复杂度有效提取局部结构信息，提供更大的感受野。
3.  提出了**分组多尺度自注意力模块（GMSA）**，将特征分组并在不同窗口大小下计算SA，以灵活平衡长程建模能力与计算成本。
4.  提出了**共享注意力机制**和**改进的移位窗口机制**，进一步加速SA计算并连接不同窗口。
5.  基于上述组件，提出了一个**架构简单高效、仅通过堆叠ELAB构建的超分辨率网络ELAN**。
6.  在多个基准数据集上，ELAN-light以显著更低的参数和计算量，达到了与SwinIR-light相当甚至更优的PSNR/SSIM性能，且推理速度快约4.5倍。
## 方法

*   **整体框架**：ELAN遵循一个非常简单的拓扑结构，依次包含三个模块：**浅层特征提取**、**基于ELAB的深度特征提取**、**HR图像重建**。存在从浅层特征到深度特征输出的全局残差连接。
    *   **输入/输出**：输入是退化的LR图像 `X_l ∈ R^{3×H×W}`，输出是重建的HR图像 `X_h`。
    *   **连接**：浅层特征 `X_s` 经过 `M` 个级联的ELAB得到深度特征 `X_d`，然后 `X_s + X_d` 通过重建模块得到 `X_h`。重建模块仅由一个3x3卷积和一个PixelShuffle操作构成。
*   **关键模块 - 高效长程注意力块（ELAB）**：
    *   结构：由**局部特征提取模块**和**GMSA模块**组成，两者都带有残差学习。
    *   **局部特征提取**：使用**两个移位卷积（shift-conv）**，中间加ReLU激活。移位卷积（p.5, Figure 1(c)）将输入特征平均分成5组，前4组分别沿左、右、上、下方向移位，最后一组不变，随后接一个1x1卷积。这使1x1卷积能利用邻域像素信息，以几乎相同的算术复杂度获得更大的感受野。
    *   **分组多尺度自注意力（GMSA）**：核心是解决窗口大小与计算成本的矛盾。给定 `C×H×W` 的特征，GMSA将其沿通道维度分成 `K` 组 `{X_k}`，每组使用不同的窗口大小 `M_k` 分别计算SA。最后将各组的SA结果拼接并通过1x1卷积融合。计算复杂度为 `2/K * (Σ_k M_k^2) * HWC`，比使用统一的大窗口 `M` 更高效。
*   **加速自注意力（ASA）**：
    *   **丢弃层归一化（LN）**，改用批归一化（BN），因为LN在推理时会产生许多碎片化的逐元素操作，且BN可合并到卷积中。
    *   **对称嵌入高斯空间**：标准SA用三个独立的1x1卷积（θ, φ, g）生成query, key, value。本文设置 `θ=φ`，节省了一个1x1卷积。
*   **共享注意力**：为进一步加速，让连续 `n` 个SA模块共享前一个模块计算出的注意力图，避免了重复的reshape和1x1卷积操作。
*   **移位窗口**：改进自SwinIR。在连续的ELAB中，通过沿对角线方向的循环移位（半窗口大小）来重新划分特征图分区，建立不同窗口间的连接，从而避免了SwinIR中的遮罩策略和相对位置编码。
*   **训练方式**：
    *   **损失函数**：使用像素级的L1损失。
    *   **优化器**：Adam优化器。
    *   **具体设置**：在DIV2K数据集上训练。ELAN-light模型包含24个ELAB，通道数60；ELAN-normal包含36个ELAB，通道数180。GMSA在三个窗口尺寸（4×4, 8×8, 16×16）上计算。共享注意力中 `n=1`。使用随机裁剪、旋转和翻转进行数据增强。
*   **推理流程**：与前向传播流程一致。BN层可以融合进卷积，共享注意力避免了重复计算，整体效率高。
*   **与已有方法的差异**：
    *   vs **SwinIR**：ELAN设计更简洁（无LN、遮罩、相对位置编码），使用移位卷积替代1x1卷积提取更强局部特征，用GMSA替代固定窗口SA以探索更大范围依赖，并通过共享注意力进一步加速。
    *   vs **Restormer**：ELAN在空间维度（而非通道维度）计算SA，保留了重要的空间信息。
## 实验

*   **数据集**：训练集为DIV2K（800张）。测试基准为Set5, Set14, BSD100, Urban100, Manga109。
*   **对比方法**：分为两类：CNN-based（CARN, IMDN, LAPAR-A, LatticeNet）和Transformer-based（ESRT, SwinIR-light）。
*   **评价指标**：图像质量：PSNR和SSIM（在Y通道计算）。效率：参数量（#Params）、浮点运算数（#FLOPs）、推理延迟（Latency，在单个NVIDIA 2080Ti GPU上测量，上采样至1280×720分辨率）。
*   **主实验结果（轻量级模型对比，表1）**：
    *   **性能**：在所有三个缩放因子（×2, ×3, ×4）和所有五个测试集上，ELAN-light取得了最佳或次佳的PSNR/SSIM。例如，在最具挑战性的Urban100数据集上：
        *   ×2: ELAN-light (32.76/0.9340) vs SwinIR-light (32.76/0.9340) 打平，且远超CNN方法。
        *   ×3: ELAN-light (28.69/0.8624) 略优于 SwinIR-light (28.66/0.8624)。
        *   ×4: ELAN-light (26.54/0.7982) 优于 SwinIR-light (26.47/0.7980)。
    *   **效率**：ELAN-light的优势极其明显。
        *   **参数量**：582K（×2） vs SwinIR-light的878K。
        *   **FLOPs**：168.4G（×2） vs 195.6G。
        *   **延迟**：230ms（×2） vs SwinIR-light的1007ms，**提速约4.4倍**。在×4时提速约4.4倍（62ms vs 271ms）。
*   **消融实验**：PDF文本中未完整呈现，但文中提到对ELAN的组件设计进行了综合消融研究。
*   **泛化实验**：PDF文本中未明确说明。
*   **效率信息**：已如上所述，ELAN-light在保持甚至超越SwinIR-light性能的同时，在参数、FLOPs和推理延迟上均有巨大优势。
## 局限

1.  **场景局限性**：论文主要在通用图像超分辨率上验证，对于特定领域（如遥感、医学影像、视频SR）的有效性未进行探讨。
2.  **实验完整性**：提供的PDF文本仅包含了轻量级模型的对比结果，未展示“经典版”ELAN（更大模型）与SwinIR等完整模型的对比细节。
3.  **计算成本**：尽管比SwinIR高效，但GMSA相对于纯CNN方法仍有一定计算开销，在极端资源受限的移动设备上部署可能仍需进一步优化。
4.  **假设依赖**：移位窗口中的循环移位假设边界像素被移走影响不大，这在纹理极其复杂或位于图像中心的区域可能不完全成立（尽管实验显示影响可忽略）。
5.  **复现风险**：GMSA的分组策略和窗口大小选择可能需要根据具体任务调优；共享注意力中 `n` 的设置需要在效率和效果间权衡。
## 个人评论

这篇论文最值得学习的是其**“以简化繁”的设计哲学和模块化创新思路**。它没有盲目堆叠复杂的组件，而是针对SR任务的特殊性（特征图大、需要高效推理），对Transformer的每个环节进行审视和精简：
1.  **局部特征提取**：用极其轻量的移位卷积替代常规卷积或MLP，兼顾感受野与计算量。
2.  **注意力计算**：用GMSA分组多尺度策略，优雅地解决了长程依赖与计算成本的矛盾，比固定窗口更灵活，比大窗口更高效。
3.  **加速技巧**：提出共享注意力、对称嵌入、移除LN等具体工程优化手段，这些技巧可直接借鉴到其他Transformer模型中。
4.  **整体架构**：构建了一个非常简洁的流水线（浅层特征提取 + 级联ELAB + 简单重建），证明了极致简洁的设计也能达到SOTA。
这对后续研究者的启发是：在设计模型时，应始终思考任务的核心需求（SR需要大感受野和高效推理），并据此对现有通用架构（如Swin Transformer）进行解构和针对性优化，而不是简单套用。

### 使用建议

*   **如果快速了解**：阅读**摘要（Abstract）**、**引言（Introduction）** 的后半部分（贡献总结）、**方法部分（Section 3）** 的ELAB介绍和**实验结果表格（Table 1）**。
*   **如果复现**：重点精读**方法部分（Section 3.2）**，特别是移位卷积、GMSA、ASA和共享注意力的具体实现描述与图示。仔细阅读**实验设置（Section 4.1）**，包括网络具体配置（通道数、层数、窗口大小、训练 patch size、学习率策略等）。
*   **如果借鉴创新点**：
    *   想设计**高效注意力模块**：可学习**GMSA的分组多尺度**思想和**共享注意力**机制。
    *   想**优化Transformer推理速度**：可借鉴**移除LN换BN**、**对称嵌入**、**合并reshape操作**等技巧。
    *   想**改进局部特征提取**：可研究**移位卷积**的实现。
*   **如果写Related Work**：可将本文放在**“高效/轻量级Transformer模型”**、**“用于图像恢复的注意力机制”** 或**“长程依赖建模”** 的类别下进行引用和讨论。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中的低层视觉任务，具体方向是单图像超分辨率。它旨在解决基于Transformer的超分辨率模型计算成本高昂、无法充分利用长程依赖的问题。本文适合放在“B_注意力算子模块”这一主题下，因为其核心贡献是设计了一个高效、可插拔的长程注意力模块ELAB，并以此构建了完整的SR网络ELAN。

## 2. 一句话总结
本文通过移位卷积高效提取局部特征，并提出分组多尺度自注意力模块，以简单堆叠的方式构建了一个高效长程注意力网络ELAN，在图像超分辨率任务中实现了优于现有Transformer方法的性能与显著更低的计算复杂度。

## 3. 背景与问题
*   **为什么要做**：现有的CNN-based SR方法使用空间不变核，难以自适应建模像素间关系；而Transformer-based方法虽然能利用自注意力建模长程依赖，但SA计算复杂度随特征尺寸呈二次方增长，限制了其在特征尺寸大的SR任务中的应用。
*   **之前方法的问题**：
    1.  **SwinIR**：虽然结合了CNN和Transformer，但其设计（如相对位置偏移、遮罩机制、层归一化、多个残差子分支）对SR任务来说是冗余的。它在小固定窗口（8x8）内计算SA，限制了建模长程依赖的能力；使用1x1卷积提取局部特征，感受野小。
    2.  **Restormer**：在通道维度计算SA，但牺牲了重要的空间纹理和结构信息。
    3.  **其他尝试**（如Mei等）：将图像分成不重叠的patch独立计算SA，可能引入边界效应。
*   **核心矛盾**：如何在保持较低计算复杂度的同时，有效地建模图像中的长程依赖关系，以提升SR性能。

## 4. 核心贡献
1.  提出了**高效长程注意力模块（ELAB）**，通过级联移位卷积和GMSA来建模图像长程依赖。
2.  提出了**移位卷积（shift-conv）**，以接近1x1卷积的计算复杂度有效提取局部结构信息，提供更大的感受野。
3.  提出了**分组多尺度自注意力模块（GMSA）**，将特征分组并在不同窗口大小下计算SA，以灵活平衡长程建模能力与计算成本。
4.  提出了**共享注意力机制**和**改进的移位窗口机制**，进一步加速SA计算并连接不同窗口。
5.  基于上述组件，提出了一个**架构简单高效、仅通过堆叠ELAB构建的超分辨率网络ELAN**。
6.  在多个基准数据集上，ELAN-light以显著更低的参数和计算量，达到了与SwinIR-light相当甚至更优的PSNR/SSIM性能，且推理速度快约4.5倍。

## 5. 方法详解
*   **整体框架**：ELAN遵循一个非常简单的拓扑结构，依次包含三个模块：**浅层特征提取**、**基于ELAB的深度特征提取**、**HR图像重建**。存在从浅层特征到深度特征输出的全局残差连接。
    *   **输入/输出**：输入是退化的LR图像 `X_l ∈ R^{3×H×W}`，输出是重建的HR图像 `X_h`。
    *   **连接**：浅层特征 `X_s` 经过 `M` 个级联的ELAB得到深度特征 `X_d`，然后 `X_s + X_d` 通过重建模块得到 `X_h`。重建模块仅由一个3x3卷积和一个PixelShuffle操作构成。
*   **关键模块 - 高效长程注意力块（ELAB）**：
    *   结构：由**局部特征提取模块**和**GMSA模块**组成，两者都带有残差学习。
    *   **局部特征提取**：使用**两个移位卷积（shift-conv）**，中间加ReLU激活。移位卷积（p.5, Figure 1(c)）将输入特征平均分成5组，前4组分别沿左、右、上、下方向移位，最后一组不变，随后接一个1x1卷积。这使1x1卷积能利用邻域像素信息，以几乎相同的算术复杂度获得更大的感受野。
    *   **分组多尺度自注意力（GMSA）**：核心是解决窗口大小与计算成本的矛盾。给定 `C×H×W` 的特征，GMSA将其沿通道维度分成 `K` 组 `{X_k}`，每组使用不同的窗口大小 `M_k` 分别计算SA。最后将各组的SA结果拼接并通过1x1卷积融合。计算复杂度为 `2/K * (Σ_k M_k^2) * HWC`，比使用统一的大窗口 `M` 更高效。
*   **加速自注意力（ASA）**：
    *   **丢弃层归一化（LN）**，改用批归一化（BN），因为LN在推理时会产生许多碎片化的逐元素操作，且BN可合并到卷积中。
    *   **对称嵌入高斯空间**：标准SA用三个独立的1x1卷积（θ, φ, g）生成query, key, value。本文设置 `θ=φ`，节省了一个1x1卷积。
*   **共享注意力**：为进一步加速，让连续 `n` 个SA模块共享前一个模块计算出的注意力图，避免了重复的reshape和1x1卷积操作。
*   **移位窗口**：改进自SwinIR。在连续的ELAB中，通过沿对角线方向的循环移位（半窗口大小）来重新划分特征图分区，建立不同窗口间的连接，从而避免了SwinIR中的遮罩策略和相对位置编码。
*   **训练方式**：
    *   **损失函数**：使用像素级的L1损失。
    *   **优化器**：Adam优化器。
    *   **具体设置**：在DIV2K数据集上训练。ELAN-light模型包含24个ELAB，通道数60；ELAN-normal包含36个ELAB，通道数180。GMSA在三个窗口尺寸（4×4, 8×8, 16×16）上计算。共享注意力中 `n=1`。使用随机裁剪、旋转和翻转进行数据增强。
*   **推理流程**：与前向传播流程一致。BN层可以融合进卷积，共享注意力避免了重复计算，整体效率高。
*   **与已有方法的差异**：
    *   vs **SwinIR**：ELAN设计更简洁（无LN、遮罩、相对位置编码），使用移位卷积替代1x1卷积提取更强局部特征，用GMSA替代固定窗口SA以探索更大范围依赖，并通过共享注意力进一步加速。
    *   vs **Restormer**：ELAN在空间维度（而非通道维度）计算SA，保留了重要的空间信息。

## 6. 实验与结果
*   **数据集**：训练集为DIV2K（800张）。测试基准为Set5, Set14, BSD100, Urban100, Manga109。
*   **对比方法**：分为两类：CNN-based（CARN, IMDN, LAPAR-A, LatticeNet）和Transformer-based（ESRT, SwinIR-light）。
*   **评价指标**：图像质量：PSNR和SSIM（在Y通道计算）。效率：参数量（#Params）、浮点运算数（#FLOPs）、推理延迟（Latency，在单个NVIDIA 2080Ti GPU上测量，上采样至1280×720分辨率）。
*   **主实验结果（轻量级模型对比，表1）**：
    *   **性能**：在所有三个缩放因子（×2, ×3, ×4）和所有五个测试集上，ELAN-light取得了最佳或次佳的PSNR/SSIM。例如，在最具挑战性的Urban100数据集上：
        *   ×2: ELAN-light (32.76/0.9340) vs SwinIR-light (32.76/0.9340) 打平，且远超CNN方法。
        *   ×3: ELAN-light (28.69/0.8624) 略优于 SwinIR-light (28.66/0.8624)。
        *   ×4: ELAN-light (26.54/0.7982) 优于 SwinIR-light (26.47/0.7980)。
    *   **效率**：ELAN-light的优势极其明显。
        *   **参数量**：582K（×2） vs SwinIR-light的878K。
        *   **FLOPs**：168.4G（×2） vs 195.6G。
        *   **延迟**：230ms（×2） vs SwinIR-light的1007ms，**提速约4.4倍**。在×4时提速约4.4倍（62ms vs 271ms）。
*   **消融实验**：PDF文本中未完整呈现，但文中提到对ELAN的组件设计进行了综合消融研究。
*   **泛化实验**：PDF文本中未明确说明。
*   **效率信息**：已如上所述，ELAN-light在保持甚至超越SwinIR-light性能的同时，在参数、FLOPs和推理延迟上均有巨大优势。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的是其**“以简化繁”的设计哲学和模块化创新思路**。它没有盲目堆叠复杂的组件，而是针对SR任务的特殊性（特征图大、需要高效推理），对Transformer的每个环节进行审视和精简：
1.  **局部特征提取**：用极其轻量的移位卷积替代常规卷积或MLP，兼顾感受野与计算量。
2.  **注意力计算**：用GMSA分组多尺度策略，优雅地解决了长程依赖与计算成本的矛盾，比固定窗口更灵活，比大窗口更高效。
3.  **加速技巧**：提出共享注意力、对称嵌入、移除LN等具体工程优化手段，这些技巧可直接借鉴到其他Transformer模型中。
4.  **整体架构**：构建了一个非常简洁的流水线（浅层特征提取 + 级联ELAB + 简单重建），证明了极致简洁的设计也能达到SOTA。
这对后续研究者的启发是：在设计模型时，应始终思考任务的核心需求（SR需要大感受野和高效推理），并据此对现有通用架构（如Swin Transformer）进行解构和针对性优化，而不是简单套用。

## 8. 局限与问题
1.  **场景局限性**：论文主要在通用图像超分辨率上验证，对于特定领域（如遥感、医学影像、视频SR）的有效性未进行探讨。
2.  **实验完整性**：提供的PDF文本仅包含了轻量级模型的对比结果，未展示“经典版”ELAN（更大模型）与SwinIR等完整模型的对比细节。
3.  **计算成本**：尽管比SwinIR高效，但GMSA相对于纯CNN方法仍有一定计算开销，在极端资源受限的移动设备上部署可能仍需进一步优化。
4.  **假设依赖**：移位窗口中的循环移位假设边界像素被移走影响不大，这在纹理极其复杂或位于图像中心的区域可能不完全成立（尽管实验显示影响可忽略）。
5.  **复现风险**：GMSA的分组策略和窗口大小选择可能需要根据具体任务调优；共享注意力中 `n` 的设置需要在效率和效果间权衡。

## 9. 我该怎么使用这篇论文
*   **如果快速了解**：阅读**摘要（Abstract）**、**引言（Introduction）** 的后半部分（贡献总结）、**方法部分（Section 3）** 的ELAB介绍和**实验结果表格（Table 1）**。
*   **如果复现**：重点精读**方法部分（Section 3.2）**，特别是移位卷积、GMSA、ASA和共享注意力的具体实现描述与图示。仔细阅读**实验设置（Section 4.1）**，包括网络具体配置（通道数、层数、窗口大小、训练 patch size、学习率策略等）。
*   **如果借鉴创新点**：
    *   想设计**高效注意力模块**：可学习**GMSA的分组多尺度**思想和**共享注意力**机制。
    *   想**优化Transformer推理速度**：可借鉴**移除LN换BN**、**对称嵌入**、**合并reshape操作**等技巧。
    *   想**改进局部特征提取**：可研究**移位卷积**的实现。
*   **如果写Related Work**：可将本文放在**“高效/轻量级Transformer模型”**、**“用于图像恢复的注意力机制”** 或**“长程依赖建模”** 的类别下进行引用和讨论。

## 10. 和其他论文的关系
基于给定的主题 `B_注意力算子模块` 和论文内容，本论文可能与以下主题下的论文相关：
*   `[[SwinIR]]`：本文的主要对比基线，并对其进行了多项关键改进。
*   `[[Restormer]]`：另一种用于图像恢复的Transformer思路（通道注意力），本文与其形成对比。
*   `[[Swin Transformer]]`：SwinIR的骨干网络，本文的设计源于对其的分析和简化。
*   `[[Shift Convolution]]` 或 `[[Efficient Convolution]]`：本文局部特征提取模块的核心技术。
*   `[[Grouped Attention]]` 或 `[[Multi-Scale Attention]]`：本文GMSA模块的设计思路。

## 11. 关键词
图像超分辨率, 长程注意力, Transformer, 移位卷积, 分组多尺度自注意力, 高效注意力, ELAN, 自注意力加速, 窗口注意力, 共享注意力

## 12. 可信度说明
本笔记主要基于提供的PDF提取文本（前12页）生成，该文本完整包含了论文的**摘要（Abstract）、引言（Introduction）、相关工作（Related Work）、方法（Methodology）** 以及**实验（Experiments）** 的前半部分（包含实验设置和主要定量结果表Table 1）。笔记中的所有核心贡献、方法细节和关键实验结果均能在所提供的文本中找到直接依据。由于文本提取不完整（截至第12页），论文后续可能包含的更多消融实验、可视化结果、经典模型对比及讨论部分未能纳入本笔记，但基于已有内容构建的论文核心脉络和贡献是可信的。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/ELAB.txt` (20/20 页; 原 AI 主体 12/20 + 全文补读 13-20); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-20; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-20。
- **提取情况**: 缺失页 8 页, 其中 8 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Efficient Long-Range Attention Network for Image Super-resolution 13
- p.13: PSNR/SSIM
- p.13: We then replace the SA calculation with our proposed ASA, the inference
- p.15: Efficient Long-Range Attention Network for Image Super-resolution 15
- p.16: Shifted
- p.16: 5 Conclusion
- p.16: In this paper, we proposed an efficient long-range attention network (ELAN) for
- p.16: References
- p.17: Efficient Long-Range Attention Network for Image Super-resolution 17
- p.17: 2005 IEEE Computer Society Conference on Computer Vision and Pattern Recog-
- p.19: Efficient Long-Range Attention Network for Image Super-resolution 19
- p.19: In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern

### 缺失页关键摘录

- p.13: Table 2. Performance comparison of different classic performance-oriented SR models
- p.13: on five benchmarks. PSNR/SSIM on Y channel are reported on each dataset. #Params
- p.13: and #FLOPs are the total number of network parameters and floating-point opera-
- p.13: tions, respectively. Noted that all the efficiency proxies (#Params, #FLOPs and La-
- p.13: on all scales. Best and second best PSNR/SSIM indexes are marked in red and blue
- p.13: on a single NVIDIA 2080Ti GPU. ’–’ means that the result is not available.
- p.13: drop compared with the SwinIR-light while reducing the latency from 271ms
- p.13: latency is greatly reduced from 177ms to 66ms without losing PSNR/SSIM per-
- p.13: pendency, the PSNR and SSIM indexes get significantly improved on all five
- p.13: datasets. Specifically, the PSNR increases by 0.21dB and 0.19dB on the Ur-
- p.13: ban100 and Manga109 datasets, respectively, while the latency is only slightly
- p.14: Depth of shared attention . We further conduct a detailed ablation study
<!-- AI_READING_NOTE_END -->
