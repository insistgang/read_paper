---
title: "SMFANet: A Lightweight Self-Modulation Feature Aggregation Network for Efficient Image Super-Resolution"
authors:
  - "Mingjun Zheng"
  - "Long Sun"
  - "Jiangxin Dong"
  - "Jinshan Pan"
year: 2024
venue: "ECCV"
doi: 
pdf: [[FMB.pdf]]
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
extract_cache: .paper-cache/extracts/FMB.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# SMFANet: A Lightweight Self-Modulation Feature Aggregation Network for Efficient Image Super-Resolution

## 基本信息
- **PDF**: [[FMB.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SMFANet: A Lightweight Self-Modulation Feature Aggregation Network for Efficient Image Super-Resolution |
| **作者** | Mingjun Zheng; Long Sun; Jiangxin Dong; Jinshan Pan |
| **发表时间** | 2024 |
| **刊物/会议** | ECCV |
| **DOI** | 未明确 |

## 摘要

> Transformer-based restoration methods achieve significant performance as the self-attention (SA) of the Transformer can explore non-local information for better high-resolution image reconstruction. However, the key dot-product SA requires substantial computational resources, which limits its application in low-power devices. Moreover, the low-pass nature of the SA mechanism limits its capacity for cap- turing local details, consequently leading to smooth reconstruction re- sults. To address these issues, we propose a self-modulation feature ag- gregation(SMFA)moduletocollaborativelyexploitbothlocalandnon- localfeatureinteractionsforamoreaccuratereconstruction.Specifically, the SMFA module employs an efficient approximation of self-attention (EASA) branch to model non-local information and uses a local detail estimation (LDE) branch to capture local details. Additionally, we fur- therintroduceapartialconvolution-basedfeed-forwardnetwork(PCFN) to refine the representative features deriv

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：单图像超分辨率在流媒体和超高清内容时代有重要应用价值。基于Transformer的方法利用自注意力（SA）探索非局部信息取得了显著性能，但其存在两个关键问题。
- **之前方法的问题**：
    1.  **计算成本高**：标准的点积自注意力机制需要大量的计算资源和内存，限制了其在智能手机等资源受限设备上的应用。
    2.  **细节丢失**：自注意力机制具有低通滤波器的性质，倾向于学习低频成分，导致重建结果平滑，丢失了局部高频细节（如边缘、角点）。
- **核心矛盾**：如何设计一个计算高效的特征调制模块，能够像自注意力一样有效探索非局部信息，同时又能充分建模局部细节，以实现更好的图像超分辨率重建。
## 关键贡献

1.  **提出自调制特征聚合（SMFA）模块**：该模块包含两个并行分支：一个用于高效近似自注意力的EASA分支（通过下采样、方差调制和特征聚合来建模非局部信息）和一个用于捕捉局部特征的LDE分支（基于卷积层）。
2.  **提出基于部分卷积的前馈网络（PCFN）**：这是一个轻量级的前馈网络，通过部分卷积操作在空间和通道维度上进一步精炼由SMFA模块提取的特征。
3.  **构建完整的SMFANet网络**：将SMFA和PCFN整合进一个端到端的可训练网络中，用于解决单图像超分辨率任务。
4.  **实现效率与性能的优越平衡**：在多个公共基准数据集上的实验表明，SMFANet家族在模型复杂度（参数量、FLOPs）和重建性能之间达到了更有利的权衡。具体地，与SwinIR-light相比，SMFANet+在五个测试集上平均PSNR高0.14dB，运行速度快10倍，且模型复杂度（如FLOPs）仅约为43%。
## 方法

- **整体框架**：SMFANet的输入是低分辨率图像，经过一个3×3卷积层提取浅层特征。随后，这些特征通过一系列特征调制块（FMB）产生深度特征。每个FMB由一个SMFA模块和一个PCFN组成。最后，通过一个轻量级的图像重建模块（3×3卷积+PixelShuffle）生成高分辨率输出。在重建模块前设有全局残差连接。
- **输入输出**：网络输入为低分辨率图像，输出为对应的高分辨率重建图像。
- **关键模块**：
    1.  **SMFA模块**：是核心创新。
        - **输入处理**：对输入特征 $F_{in}$ 进行L2归一化，然后通过一个1×1卷积层扩展通道数，再通过通道分割操作 $S(\cdot)$ 得到两个部分 $X$ 和 $Y$。
        - **EASA分支**（处理 $X$）：
            - 通过自适应最大池化 $D(\cdot)$ 将特征下采样8倍。
            - 使用3×3深度卷积生成非局部结构信息 $X_s$。
            - 计算输入特征 $X$ 的全局方差 $\sigma^2(X)$，它提供了对空间信息的统计描述。
            - 将方差 $\sigma^2(X)$ 与 $X_s$ 相加，并通过1×1卷积得到调制后的特征 $X_m$。方差调制机制有助于更好地探索非局部信息。
            - 将 $X_m$ 经过GELU激活和最近邻上采样 $U(\cdot)$ 后，与原始特征 $X$ 进行逐元素相乘，得到最终的非局部特征 $X_l$。
        - **LDE分支**（处理 $Y$）：
            - 使用扩展的3×3深度卷积编码局部信息 $Y_h$。
            - 通过两个1×1卷积和一个GELU激活，生成增强后的局部特征 $Y_d$。
        - **特征融合**：将EASA分支的非局部特征 $X_l$ 与LDE分支的局部特征 $Y_d$ 进行逐元素相加，再通过一个1×1卷积得到SMFA模块的最终输出 $F_\rho$。
    2.  **PCFN**：对SMFA输出的特征 $F_\rho$ 进行精炼。
        - 先用1×1卷积和GELU激活进行跨通道交互。
        - 将特征在通道维度上分成两部分 $\{F_\rho^1, F_\rho^2\}$。
        - 对 $F_\rho^1$ 使用3×3卷积和GELU激活来编码局部上下文信息。
        - 将处理后的 $F_\rho^1$ 与 $F_\rho^2$ 进行拼接，再通过一个1×1卷积混合特征并还原通道数。
- **模块连接与网络结构**：特征调制块（FMB）将SMFA和PCFN串联起来，并加入了残差连接。具体为：$F_\rho = \text{SMFA}(F_{in}) + F_{in}$， $\hat{F}_\rho = \text{PCFN}(F_\rho) + F_\rho$。
- **训练方式**：在DIV2K或DF2K数据集上训练，使用L1损失。采用Adam优化器，学习率从1e-3余弦退火至1e-5。训练了两个版本：标准版（8个FMB，36通道）和SMFANet+（12个FMB，48通道）。
- **推理流程**：输入低分辨率图像，依次经过浅层特征提取、多个FMB深度特征提取、图像重建模块（上采样），最后加上全局残差连接（即双三次插值上采样的输入图像）得到最终输出。
- **与已有方法的差异**：
    - 相比**纯CNN方法**（如IMDN, BSRN）：SMFANet通过EASA分支显式地建模了非局部特征交互，能更好地捕获全局结构。
    - 相比**标准ViT/SwinT方法**（如IPT, SwinIR）：SMFANet使用EASA分支（下采样+方差调制）近似自注意力，计算成本极低，避免了昂贵的点积注意力计算。同时，通过LDE分支显式建模局部细节，克服了自注意力低通滤波的缺陷。
    - 相比其他**高效注意力/非局部方法**（如SAFMN, VapSR）：本文认为仅使用聚合的非局部特征进行重建会导致局部细节出现伪影，因此SMFA模块协同建模了局部和非局部特征。
- **论文类型特化（注意力类）**：本文属于**轻量化注意力模块设计**。其注意力（EASA）主要作用于**空间维度**，通过下采样降低计算复杂度，实现对全局（非局部）信息的建模。它设计为可插入模块，作为网络中的核心特征提取单元。论文重点论证了该模块在**计算量（FLOPs、运行时间）与效果（PSNR/SSIM）** 之间取得的优越权衡。
## 实验

- **使用数据集**：
    - **训练集**：DIV2K, DIV2K + Flickr2K (DF2K)。
    - **测试集**：Set5, Set14, B100, Urban100, Manga109。
- **对比方法**：文中主要对比了基于CNN的轻量级SR方法（如CARN, IMDN, RFDN, BSRN, SAFMN）以及基于ViT的方法（如SwinIR-light）。具体对比列表在提供的文本中未完全列出，但提到了与这些主流方法的比较。
- **评价指标**：PSNR 和 SSIM（均在YCbCr色彩空间的Y通道上计算）。
- **主实验结果**：根据摘要和图1的描述，与×4 SwinIR-light相比，SMFANet+在五个公共测试集上**平均PSNR高0.14dB**，运行速度快约10倍，且FLOPs仅为SwinIR-light的约43%。这表明在显著降低计算成本的同时，性能还有所提升。
- **消融实验**：文本中未提供详细的消融实验结果。但通过章节5.2和5.3对SMFA和PCFN设计的详细描述，隐含了这些设计都是经过验证的核心组件。
- **泛化实验**：文本中未明确说明。
- **效率信息**：图1的标题说明，左图圆圈大小代表模型FLOPs，右图圆圈大小代表推理所需的GPU使用量。文中强调SMFANet家族在效率-性能权衡上优于其他方法。摘要中给出了具体数字：相比SwinIR-light，SMFANet+运行时间快约10倍，FLOPs降低约57%（即约为其43%）。
## 局限

基于提供的文本，未找到作者对自身方法局限性的明确讨论。但可以分析如下：
- **适用场景**：论文聚焦于计算效率，适合移动端或嵌入式设备。但对于需要极高重建保真度、且计算资源不受限的应用场景，其轻量化设计可能不是最优选择。
- **实验充分性**：提供的文本只展示了部分实验结果（主要是性能对比摘要），完整的消融实验、不同尺度下的结果、在其他任务（如去噪、去模糊）上的泛化能力等细节缺失，需要查看论文全文。
- **数据集**：主要在标准的学术SR数据集上验证，其对于真实世界复杂退化场景（如未知模糊核、复合噪声）的表现未有体现。
- **假设依赖**：EASA分支依赖于通过固定下采样因子（8倍）来获取低频信息。这个因子是否最优、是否应随图像内容自适应调整，是一个可能的改进点。
- **复现风险**：论文提供了开源代码，复现风险较低。但一些细节，如L2归一化的具体实现、方差计算的维度等，需要参照代码确认。
## 个人评论

这篇论文最值得学习的点是其 **“协同建模”** 的设计思想和 **“高效近似”** 的实现策略。
1.  **思想启发**：它没有简单地抛弃自注意力或纯粹依赖卷积，而是清醒地认识到非局部信息（全局结构）和局部细节（高频信息）对于图像重建都至关重要。因此，设计了EASA和LDE两个并行分支，让它们各司其职、优势互补。这为处理类似“全局vs局部”矛盾的任务提供了清晰的设计思路。
2.  **技术启发**：EASA分支通过**下采样**获取低频（全局）结构，引入**特征方差**作为统计量进行调制，最后通过**逐元素乘法**聚合特征。这一套操作是对标准自注意力的一种非常聪明且轻量化的“功能近似”，它抓住了自注意力能够整合全局信息的本质，但避免了计算$QK^T$的巨大开销。这种“用信号处理/统计量的思维来替代复杂算子”的思路极具启发性。
3.  **工程启发**：论文展示了如何将新模块（SMFA）与经典的前馈网络（FFN）改进（PCFN）结合，并利用残差连接构建稳定的训练单元（FMB），最终组合成有效的网络。这是模块化设计的良好范例。

### 使用建议

- **快速了解**：阅读 **Abstract**（摘要）、**Introduction**（引言）的最后部分和 **Figure 1**（图1）的说明，可以快速把握论文动机、核心贡献和主要结果。
- **如果复现**：重点研读 **3. Proposed Method** 部分，特别是3.1（整体架构）、3.2（SMFA模块，公式1-6）、3.3（PCFN，公式7）的描述，并结合论文中的 **Figure 2** 和作者提供的GitHub开源代码。
- **如果借鉴创新点**：
    - 学习 **SMFA模块的设计**：尤其是EASA分支中“下采样->深度卷积->方差调制->上采样聚合”这一套实现高效非局部建模的范式。
    - 学习 **PCFN的部分卷积思想**：如何通过通道分割和仅对部分通道进行空间卷积来增强模型的空间建模能力。
- **如果写Related Work**：可以将本文放在“**轻量化/高效自注意力模块设计**”或“**用于图像恢复的局部-非局部特征聚合方法**”这个类别下进行综述。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中的高效图像超分辨率方向，聚焦于解决传统自注意力机制计算开销大、且其低通特性导致重建图像细节模糊的问题。它适合归类于“B_注意力算子模块”主题下，特别是关注轻量化、高效的自注意力变体或替代方案的设计。

## 2. 一句话总结
本文提出了一种名为自调制特征聚合网络（SMFANet）的轻量级超分辨率模型，其核心是自调制特征聚合（SMFA）模块，该模块通过一个高效近似自注意力（EASA）分支捕获非局部信息，并通过一个局部细节估计（LDE）分支建模局部特征，从而在显著降低计算成本的同时，实现了优于现有方法的重建质量。

## 3. 背景与问题
- **为什么要做**：单图像超分辨率在流媒体和超高清内容时代有重要应用价值。基于Transformer的方法利用自注意力（SA）探索非局部信息取得了显著性能，但其存在两个关键问题。
- **之前方法的问题**：
    1.  **计算成本高**：标准的点积自注意力机制需要大量的计算资源和内存，限制了其在智能手机等资源受限设备上的应用。
    2.  **细节丢失**：自注意力机制具有低通滤波器的性质，倾向于学习低频成分，导致重建结果平滑，丢失了局部高频细节（如边缘、角点）。
- **核心矛盾**：如何设计一个计算高效的特征调制模块，能够像自注意力一样有效探索非局部信息，同时又能充分建模局部细节，以实现更好的图像超分辨率重建。

## 4. 核心贡献
1.  **提出自调制特征聚合（SMFA）模块**：该模块包含两个并行分支：一个用于高效近似自注意力的EASA分支（通过下采样、方差调制和特征聚合来建模非局部信息）和一个用于捕捉局部特征的LDE分支（基于卷积层）。
2.  **提出基于部分卷积的前馈网络（PCFN）**：这是一个轻量级的前馈网络，通过部分卷积操作在空间和通道维度上进一步精炼由SMFA模块提取的特征。
3.  **构建完整的SMFANet网络**：将SMFA和PCFN整合进一个端到端的可训练网络中，用于解决单图像超分辨率任务。
4.  **实现效率与性能的优越平衡**：在多个公共基准数据集上的实验表明，SMFANet家族在模型复杂度（参数量、FLOPs）和重建性能之间达到了更有利的权衡。具体地，与SwinIR-light相比，SMFANet+在五个测试集上平均PSNR高0.14dB，运行速度快10倍，且模型复杂度（如FLOPs）仅约为43%。

## 5. 方法详解
- **整体框架**：SMFANet的输入是低分辨率图像，经过一个3×3卷积层提取浅层特征。随后，这些特征通过一系列特征调制块（FMB）产生深度特征。每个FMB由一个SMFA模块和一个PCFN组成。最后，通过一个轻量级的图像重建模块（3×3卷积+PixelShuffle）生成高分辨率输出。在重建模块前设有全局残差连接。
- **输入输出**：网络输入为低分辨率图像，输出为对应的高分辨率重建图像。
- **关键模块**：
    1.  **SMFA模块**：是核心创新。
        - **输入处理**：对输入特征 $F_{in}$ 进行L2归一化，然后通过一个1×1卷积层扩展通道数，再通过通道分割操作 $S(\cdot)$ 得到两个部分 $X$ 和 $Y$。
        - **EASA分支**（处理 $X$）：
            - 通过自适应最大池化 $D(\cdot)$ 将特征下采样8倍。
            - 使用3×3深度卷积生成非局部结构信息 $X_s$。
            - 计算输入特征 $X$ 的全局方差 $\sigma^2(X)$，它提供了对空间信息的统计描述。
            - 将方差 $\sigma^2(X)$ 与 $X_s$ 相加，并通过1×1卷积得到调制后的特征 $X_m$。方差调制机制有助于更好地探索非局部信息。
            - 将 $X_m$ 经过GELU激活和最近邻上采样 $U(\cdot)$ 后，与原始特征 $X$ 进行逐元素相乘，得到最终的非局部特征 $X_l$。
        - **LDE分支**（处理 $Y$）：
            - 使用扩展的3×3深度卷积编码局部信息 $Y_h$。
            - 通过两个1×1卷积和一个GELU激活，生成增强后的局部特征 $Y_d$。
        - **特征融合**：将EASA分支的非局部特征 $X_l$ 与LDE分支的局部特征 $Y_d$ 进行逐元素相加，再通过一个1×1卷积得到SMFA模块的最终输出 $F_\rho$。
    2.  **PCFN**：对SMFA输出的特征 $F_\rho$ 进行精炼。
        - 先用1×1卷积和GELU激活进行跨通道交互。
        - 将特征在通道维度上分成两部分 $\{F_\rho^1, F_\rho^2\}$。
        - 对 $F_\rho^1$ 使用3×3卷积和GELU激活来编码局部上下文信息。
        - 将处理后的 $F_\rho^1$ 与 $F_\rho^2$ 进行拼接，再通过一个1×1卷积混合特征并还原通道数。
- **模块连接与网络结构**：特征调制块（FMB）将SMFA和PCFN串联起来，并加入了残差连接。具体为：$F_\rho = \text{SMFA}(F_{in}) + F_{in}$， $\hat{F}_\rho = \text{PCFN}(F_\rho) + F_\rho$。
- **训练方式**：在DIV2K或DF2K数据集上训练，使用L1损失。采用Adam优化器，学习率从1e-3余弦退火至1e-5。训练了两个版本：标准版（8个FMB，36通道）和SMFANet+（12个FMB，48通道）。
- **推理流程**：输入低分辨率图像，依次经过浅层特征提取、多个FMB深度特征提取、图像重建模块（上采样），最后加上全局残差连接（即双三次插值上采样的输入图像）得到最终输出。
- **与已有方法的差异**：
    - 相比**纯CNN方法**（如IMDN, BSRN）：SMFANet通过EASA分支显式地建模了非局部特征交互，能更好地捕获全局结构。
    - 相比**标准ViT/SwinT方法**（如IPT, SwinIR）：SMFANet使用EASA分支（下采样+方差调制）近似自注意力，计算成本极低，避免了昂贵的点积注意力计算。同时，通过LDE分支显式建模局部细节，克服了自注意力低通滤波的缺陷。
    - 相比其他**高效注意力/非局部方法**（如SAFMN, VapSR）：本文认为仅使用聚合的非局部特征进行重建会导致局部细节出现伪影，因此SMFA模块协同建模了局部和非局部特征。
- **论文类型特化（注意力类）**：本文属于**轻量化注意力模块设计**。其注意力（EASA）主要作用于**空间维度**，通过下采样降低计算复杂度，实现对全局（非局部）信息的建模。它设计为可插入模块，作为网络中的核心特征提取单元。论文重点论证了该模块在**计算量（FLOPs、运行时间）与效果（PSNR/SSIM）** 之间取得的优越权衡。

## 6. 实验与结果
- **使用数据集**：
    - **训练集**：DIV2K, DIV2K + Flickr2K (DF2K)。
    - **测试集**：Set5, Set14, B100, Urban100, Manga109。
- **对比方法**：文中主要对比了基于CNN的轻量级SR方法（如CARN, IMDN, RFDN, BSRN, SAFMN）以及基于ViT的方法（如SwinIR-light）。具体对比列表在提供的文本中未完全列出，但提到了与这些主流方法的比较。
- **评价指标**：PSNR 和 SSIM（均在YCbCr色彩空间的Y通道上计算）。
- **主实验结果**：根据摘要和图1的描述，与×4 SwinIR-light相比，SMFANet+在五个公共测试集上**平均PSNR高0.14dB**，运行速度快约10倍，且FLOPs仅为SwinIR-light的约43%。这表明在显著降低计算成本的同时，性能还有所提升。
- **消融实验**：文本中未提供详细的消融实验结果。但通过章节5.2和5.3对SMFA和PCFN设计的详细描述，隐含了这些设计都是经过验证的核心组件。
- **泛化实验**：文本中未明确说明。
- **效率信息**：图1的标题说明，左图圆圈大小代表模型FLOPs，右图圆圈大小代表推理所需的GPU使用量。文中强调SMFANet家族在效率-性能权衡上优于其他方法。摘要中给出了具体数字：相比SwinIR-light，SMFANet+运行时间快约10倍，FLOPs降低约57%（即约为其43%）。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的点是其 **“协同建模”** 的设计思想和 **“高效近似”** 的实现策略。
1.  **思想启发**：它没有简单地抛弃自注意力或纯粹依赖卷积，而是清醒地认识到非局部信息（全局结构）和局部细节（高频信息）对于图像重建都至关重要。因此，设计了EASA和LDE两个并行分支，让它们各司其职、优势互补。这为处理类似“全局vs局部”矛盾的任务提供了清晰的设计思路。
2.  **技术启发**：EASA分支通过**下采样**获取低频（全局）结构，引入**特征方差**作为统计量进行调制，最后通过**逐元素乘法**聚合特征。这一套操作是对标准自注意力的一种非常聪明且轻量化的“功能近似”，它抓住了自注意力能够整合全局信息的本质，但避免了计算$QK^T$的巨大开销。这种“用信号处理/统计量的思维来替代复杂算子”的思路极具启发性。
3.  **工程启发**：论文展示了如何将新模块（SMFA）与经典的前馈网络（FFN）改进（PCFN）结合，并利用残差连接构建稳定的训练单元（FMB），最终组合成有效的网络。这是模块化设计的良好范例。

## 8. 局限与问题
基于提供的文本，未找到作者对自身方法局限性的明确讨论。但可以分析如下：
- **适用场景**：论文聚焦于计算效率，适合移动端或嵌入式设备。但对于需要极高重建保真度、且计算资源不受限的应用场景，其轻量化设计可能不是最优选择。
- **实验充分性**：提供的文本只展示了部分实验结果（主要是性能对比摘要），完整的消融实验、不同尺度下的结果、在其他任务（如去噪、去模糊）上的泛化能力等细节缺失，需要查看论文全文。
- **数据集**：主要在标准的学术SR数据集上验证，其对于真实世界复杂退化场景（如未知模糊核、复合噪声）的表现未有体现。
- **假设依赖**：EASA分支依赖于通过固定下采样因子（8倍）来获取低频信息。这个因子是否最优、是否应随图像内容自适应调整，是一个可能的改进点。
- **复现风险**：论文提供了开源代码，复现风险较低。但一些细节，如L2归一化的具体实现、方差计算的维度等，需要参照代码确认。

## 9. 我该怎么使用这篇论文
- **快速了解**：阅读 **Abstract**（摘要）、**Introduction**（引言）的最后部分和 **Figure 1**（图1）的说明，可以快速把握论文动机、核心贡献和主要结果。
- **如果复现**：重点研读 **3. Proposed Method** 部分，特别是3.1（整体架构）、3.2（SMFA模块，公式1-6）、3.3（PCFN，公式7）的描述，并结合论文中的 **Figure 2** 和作者提供的GitHub开源代码。
- **如果借鉴创新点**：
    - 学习 **SMFA模块的设计**：尤其是EASA分支中“下采样->深度卷积->方差调制->上采样聚合”这一套实现高效非局部建模的范式。
    - 学习 **PCFN的部分卷积思想**：如何通过通道分割和仅对部分通道进行空间卷积来增强模型的空间建模能力。
- **如果写Related Work**：可以将本文放在“**轻量化/高效自注意力模块设计**”或“**用于图像恢复的局部-非局部特征聚合方法**”这个类别下进行综述。

## 10. 和其他论文的关系
根据主题“B_注意力算子模块”，本文可能与以下方向的论文强相关：
- **高效的窗口/区域自注意力**：如 `[[SwinIR]]`, `[[ELAN]]`，本文旨在用更低的成本替代或近似这类注意力。
- **局部-非局部融合的恢复网络**：如 `[[SAFMN]]`, `[[MDRN]]`，本文与它们目标类似，但提出了不同的融合模块（SMFA）。
- **基于CNN的轻量SR网络**：如 `[[IMDN]]`, `[[RFDN]]`, `[[BSRN]]`，本文与它们属于同类竞争方法，但引入了非局部建模能力。
- **方差在注意力或特征聚合中的应用**：可能与一些利用统计量进行特征校准或调制的工作相关。

## 11. 关键词
高效图像超分辨率, 自注意力, 特征聚合, 自调制, 局部与非局部信息, 轻量级网络, 方差调制, 部分卷积, 前馈网络, 计算效率

## 12. 可信度说明
本篇精读笔记主要基于PDF提取文本的前12页内容生成，涵盖了论文的标题、作者、摘要、引言（第1-2页）、相关工作（第3-4页）、方法详解（第4-7页）、实验设置和部分对比结果描述（第8页）。提取的文本质量良好，公式和符号基本清晰可读。但需要注意的是，由于只提供了前12页，后续更详细的实验结果（如各测试集上的具体PSNR/SSIM数值表格）、完整的消融实验、更多的可视化结果以及结论部分未能纳入分析，因此关于实验部分的具体数字和全面性讨论的完整性可能受限。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/FMB.txt` (17/17 页; 原 AI 主体 12/17 + 全文补读 13-17); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: SMFANet for Efficient Image Super-Resolution 13
- p.13: HR image Input feature Fin Xlfrom EASA Ydfrom LDE
- p.14: Thus, our PCFN introduces a partial convolution that processes only 1/4 of
- p.14: 6 Conclusion
- p.14: We have proposed a simple yet effective SMFANet method to solve image super-
- p.15: SMFANet for Efficient Image Super-Resolution 15
- p.15: Acknowledgements
- p.15: ThisworkhasbeenpartlysupportedbytheNationalNaturalScienceFoundation
- p.15: References
- p.15: BMVC (2012)
- p.15: ICLR (2021)
- p.16: In: NeurIPS (2020)

### 缺失页关键摘录

- p.13: Fig.5: Effectiveness of the SMFA for image super-resolution on the ×4 Ur-
- p.13: Fig.6: The power spectral density (PSD) visualizations of feature Fin,Xl,
- p.13: Table 5 presents that the PSNR values drop by 0.06dB and 0.08dB on the
- p.13: and 0.11dB PSNR reduction on Urban100 and Manga109, respectively. This
- p.14: Table 4: Ablation experiments for ×4 SMFANet on Urban100 and
- p.14: Table 1. “ A →B ” is to replace A with B, and “A →None” is to remove operator A.
- p.14: Ablation Variant #Params(K) #FLOPs(G) #GPU Mem.(M) #Avg.Time(ms) Urban100 Manga109
- p.14: effectiveness of this module, we performed ablation experiments with removal of
- p.14: PCFN and replacement of FFN [40], respectively. Table 5 shows that the exclu-
- p.14: in PSNR values of 0.34dB and 0.16dB on the Manga109 [33] dataset, compared
- p.14: while efficiently encoding local information. Table 4 shows that PCFN achieves
- p.15: don’t walk: Chasing higher flops for faster neural networks. In: CVPR (2023)
<!-- AI_READING_NOTE_END -->
