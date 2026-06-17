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
| **作者** | Xindong Zhang; Hui Zeng; Shi Guo; Lei Zhang (香港理工大学 + OPPO Research) |
| **发表时间** | 2022 |
| **刊物/会议** | ECCV |
| **DOI** | 未明确 |
| **代码** | https://github.com/xindongzhang/ELAN |

## 摘要

**英文原摘要（据 PDF 提取文本整理，修复空格/连字符）**：

> Recently, transformer-based methods have demonstrated impressive results in various vision tasks, including image super-resolution (SR), by exploiting the self-attention (SA) for feature extraction. However, the computation of SA in most existing transformer based models is very expensive, while some employed operations may be redundant for the SR task. This limits the range of SA computation and consequently the SR performance. In this work, we propose an efficient long-range attention network (ELAN) for image SR. Specifically, we first employ shift convolution (shift-conv) to effectively extract the image local structural information while maintaining the same level of complexity as 1×1 convolution, then propose a group-wise multi-scale self-attention (GMSA) module, which calculates SA on non-overlapped groups of features using different window sizes to exploit the long-range image dependency. A highly efficient long-range attention block (ELAB) is then built by simply cascading two shift-conv with a GMSA module, which is further accelerated by using a shared attention mechanism. Without bells and whistles, our ELAN follows a fairly simple design by sequentially cascading the ELABs. Extensive experiments demonstrate that ELAN obtains even better results against the transformer-based SR models but with significantly less complexity.

**中文翻译**：

> 近来，基于 Transformer 的方法通过利用自注意力（SA）进行特征提取，在包括图像超分辨率（SR）在内的多种视觉任务上取得了令人瞩目的成果。然而，现有大多数基于 Transformer 的模型中，SA 的计算开销非常昂贵，其中部分操作对 SR 任务而言可能是冗余的，这限制了 SA 的计算范围，从而限制了 SR 性能。本文提出一种用于图像 SR 的高效长程注意力网络（ELAN）。具体而言：首先采用移位卷积（shift-conv）有效提取图像的局部结构信息，同时保持与 1×1 卷积相同的复杂度；进而提出分组多尺度自注意力（GMSA）模块，在特征的非重叠分组上以不同窗口大小分别计算 SA，以挖掘图像的长程依赖。然后，仅通过级联两个 shift-conv 与一个 GMSA 模块即可构建出高效的长程注意力块（ELAB），并借助共享注意力机制进一步加速。ELAN 无需花哨设计，仅通过顺序级联 ELAB 构成。大量实验表明，ELAN 在显著更低的复杂度下，取得了优于基于 Transformer 的 SR 模型的结果。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

*   **为什么要做**：CNN-based SR 方法用空间不变（spatially invariant）卷积核提取局部特征，难以自适应地建模像素间关系；为扩大感受野，CNN-based SR 往往堆叠很深很复杂的网络拓扑，导致计算资源消耗大。Transformer-based 方法能借自注意力建模长程依赖，但 SA 复杂度随输入特征尺寸**二次方增长**，而 SR 任务的特征尺寸通常很大，因此 SA 的计算范围（窗口）被迫受限，进而限制 SR 性能。
*   **之前方法的问题**（提取文本逐一点名）：
    1.  **Mei 等 [40]**：将图像切成非重叠 patch，独立建模局部特征与 SA，可能引入边界效应（border effect），损害恢复图像的视觉质量。
    2.  **SwinIR [28]**：沿用 Swin Transformer 设计，先用两个级联 1×1 卷积提取局部特征，再在小固定窗口（8×8）内、配合移位机制计算 SA。问题：1×1 卷积感受野小，局部特征表达弱，不利于长程 SA；小窗口 SA 限制了长程依赖建模能力。此外它带有相对位置偏置、遮罩机制、层归一化（LN）、多个残差子分支等组件，对 SR 任务是冗余且碎片化的。
    3.  **Restormer [58]**：在**通道空间**计算 SA，对大图仍适用，但牺牲了对重现高质量 HR 图像很重要的纹理与结构等空间信息。
*   **核心矛盾**：如何用**简洁**的网络结构，在保持低计算复杂度的同时有效挖掘图像长程依赖，以提升 SR 性能。

## 关键贡献

> 论文正文（提取文本 p.3）将贡献归纳为两点；以下为对照正文的细化。

1.  提出**高效长程注意力块（ELAB）**，用于建模对提升 SR 性能至关重要的图像长程依赖；ELAB 仅由两个 shift-conv（局部特征提取）与一个 GMSA 模块级联构成，二者均带残差学习。
2.  提出**移位卷积（shift-conv [56]）**，将输入特征均分 5 组并对其中 4 组分别向左/右/上/下移位、最后 1 组不变，再接 1×1 卷积，从而以**几乎等同 1×1 卷积的算术复杂度**获得更大感受野。
3.  提出**分组多尺度自注意力（GMSA）**，沿通道把特征分成若干组、各组用不同窗口大小分别算 SA，在长程建模能力与计算成本间灵活权衡。
4.  提出**加速自注意力（ASA）**（移除 LN 改用 BN、对称嵌入高斯空间 θ=φ）与**共享注意力机制**进一步加速 SA，并用改进的**移位窗口**连接不同窗口。
5.  基于上述组件，提出**结构极简、仅顺序堆叠 ELAB** 的超分网络 ELAN。
6.  在五个基准上，ELAN（轻量版）以更少的 #Params/#FLOPs，取得了优于或持平于 SwinIR-light 的 PSNR/SSIM，且推理速度约快 **4.5 倍**（论文 abstract/正文表述）。

## 方法

*   **整体框架（Figure 1(a)）**：ELAN 拓扑极简，依次为三模块——**浅层特征提取**、**基于 ELAB 的深层特征提取**、**HR 图像重建**，并有一条从浅层特征到深层特征输出的全局残差短接。
    *   **输入/输出**：输入退化 LR 图像 `X_l ∈ R^{3×H×W}`，输出重建 HR 图像 `X_h`。
    *   **数据流**：浅层模块 `H_SF(·)` 仅含**一个 3×3 卷积**，得 `X_s ∈ R^{C×H×W}`；`X_s` 经 `M` 个级联 ELAB 的 `H_DF(·)` 得 `X_d`；最后 `X_h = H_RC(X_s + X_d)`。重建模块 `H_RC` 仅由**一个 3×3 卷积 + 一个 PixelShuffle** 构成（为求高效）。
    *   **损失**：可用 L2/L1/感知损失；本文取**逐像素 L1 损失**（式 4）。优化器为 **Adam**（在低层视觉任务表现好）。
*   **局部特征提取**：传统做法用 MLP 或两个级联 1×1 卷积，感受野只有 1×1。本文改用**两个 shift-conv，中间夹一个 ReLU**。shift-conv（Figure 1(c)）= 一组移位操作 + 一个 1×1 卷积；不引入额外可学习参数、几乎不增加计算量，却能提供更大感受野。
*   **分组多尺度自注意力（GMSA）**：基于窗口的 SA 用 `M×M` 非重叠窗口时复杂度为 `2M²HWC`。窗口越大越能挖掘自相似信息，但直接增大 `M` 会使开销二次方增长。GMSA（Figure 1(d)）把输入特征 `X` 分成 `K` 组 `{X_k}`，第 k 组用窗口 `M_k` 算 SA；若按 `C/K` 通道等分，`K` 组 SA 的计算成本为 `(2/K)·(Σ_k M_k²)·HWC`。各组 SA 结果拼接后用一个 1×1 卷积融合。这比小固定窗口感受野更大、比大固定窗口更省。
*   **加速自注意力（ASA，Figure 1(e)）**：
    *   **移除 LN，改用 BN**：LN 把 SA 计算碎片化成大量逐元素操作，不利高效推理；BN 既能稳定训练，又能在推理期**融合进卷积**、零额外开销。
    *   **对称嵌入高斯空间**：SwinIR 用三个独立 1×1 卷积 θ、φ、g 映射特征；本文令 `θ=φ`，在每个 SA 中**省下一个 1×1 卷积**，进一步降低计算与显存且不损 SR 性能。
*   **共享注意力（Figure 2(b)）**：即便有 ASA，一次 SA 前向仍含两个 1×1 卷积与四个 IO 密集的 reshape；reshape 虽无 FLOPs 但因 SR 特征尺寸大而耗时。于是让第 i 个 SA 算出的注意力分数被同一尺度上**后续 n 个 SA 直接复用**，可省去后续 n 个 SA 的 `2n` 次 reshape 与 `n` 个 1×1 卷积。实验发现取小的 `n`（如 1 或 2）只带来极轻微性能下降，却大幅节省推理资源。
*   **移位窗口（Figure 2(c)）**：组内多尺度窗口间仍缺连接。本文改进 SwinIR 的移位窗口：先沿**对角线方向循环移位（circular shift，半窗口大小）**、在移位后特征上算 GMSA，再用逆循环移位移回，从而在相邻非重叠窗口间引入连接。少量被移到远端的边界像素在 SR 任务中占比极小，对最终性能影响可忽略。受益于此，**移除了 SwinIR 的遮罩策略与相对位置编码**，网络更简洁高效。
*   **与已有方法的差异**：
    *   vs **SwinIR**：设计更简（无 LN/遮罩/相对位置编码），shift-conv 替代 1×1 卷积提取更强局部特征，GMSA 替代固定小窗口 SA 以探索更大范围依赖，并能在更大窗口算 SA，加上共享注意力进一步加速。
    *   vs **Restormer**：在**空间维度**（而非通道维度）算 SA，保留了重要的空间纹理/结构信息。

## 实验

*   **训练集/测试集**：DIV2K（800 张）训练；Set5、Set14、BSD100、Urban100、Manga109 五个基准测试。
*   **评价指标**：PSNR/SSIM（RGB 转 YCbCr 后在 **Y 通道**计算）；效率指标为 #Params、#FLOPs、Latency（单张 NVIDIA 2080Ti 推理、统一在上采样到 **1280×720** 设置下测量）。论文强调 #Params/#FLOPs 未必能忠实反映复杂度与效率，故以 latency 为主。部分对比方法未开源，只能引用其原文 PSNR/SSIM，无法报告其 latency/FLOPs。
*   **训练细节**（提取文本 p.8 4.1）：ELAN-light = **24 个 ELAB、60 通道**；ELAN-normal = **36 个 ELAB、180 通道**。GMSA 在三个等分尺度上计算，窗口 **4×4 / 8×8 / 16×16**；共享注意力默认 `n=1`。Bicubic 下采样生成训练对；light 版随机裁 **64 个 64×64** patch、normal 版 **32 个 48×48** patch 作 mini-batch；数据增强为随机旋转 90°/180°/270° 与水平翻转。Adam（β1=0.9, β2=0.999, ε=1e-8）训练 **500 epoch**；学习率初始 **2×10⁻⁴**，在第 {250,400,425,450,475} epoch 各乘 0.5；PyTorch 实现，2080Ti GPU。
*   **对比方法**：CNN-based（CARN、EDSR-baseline、IMDN、LAPAR-A、LatticeNet）与 Transformer-based（ESRT、SwinIR-light）。
*   **主结果（轻量级对比，Table 1）**：ELAN-light 在五个数据集 × 三个尺度（×2/×3/×4）上均取得**最优或次优** PSNR/SSIM，同时比 SwinIR-light 约快 **4.5 倍**，#Params/#FLOPs 也更小。关键数值（提取文本 Table 1）：
    *   **×2 · Urban100**：ELAN-light 32.76/0.9340，与 SwinIR-light 32.76/0.9340 持平；ELAN-light 582K / 168.4G / **230ms** vs SwinIR-light 878K / 195.6G / **1007ms**（约 4.4× 提速）。
    *   **×3 · Urban100**：ELAN-light 28.69/0.8624 略优于 SwinIR-light 28.66/0.8624；590K / 75.7G / 105ms vs 886K / 87.2G / 445ms。
    *   **×4 · Urban100**：ELAN-light 26.54/0.7982 优于 SwinIR-light 26.47/0.7980；601K / 43.2G / **62ms** vs 897K / 49.6G / **271ms**（约 4.4× 提速）。
    *   定性观察（提取文本 p.8 末，截断处）：CNN-based 模型在多数图像上边缘模糊/扭曲；SwinIR-light 能恢复主结构但部分结构仍不准（后续 Figure 3/4 完整对比未在提取缓存内）。
*   **消融实验**：提取缓存（前 12 页）未覆盖完整消融正文。据原文后续页线索（提取缓存未覆盖，待核）：p.13 含 Table 2（classic performance-oriented 模型对比）及"将 SA 替换为 ASA 后 latency 从 271→? / 177→66ms 而 PSNR/SSIM 不降""引入长程依赖后 Urban100/Manga109 PSNR 分别 +0.21dB / +0.19dB 而 latency 仅轻微增加"等表述；p.14 起为共享注意力深度（depth of shared attention）的消融。
*   **结论/泛化**：p.16 含 Conclusion（提取缓存未覆盖正文，仅有页眉线索）。视频/遥感/医学等跨域泛化论文中未涉及。

## 局限

1.  **任务范围**：论文聚焦通用单图像 SR（lightweight + classic 两档），对视频 SR、遥感、医学影像等特定域的有效性未做验证。
2.  **提取覆盖局限**：本笔记证据主体为提取缓存前 12 页（含摘要/引言/相关工作/方法/实验设置 + Table 1）。classic 版 ELAN 与大模型 SwinIR 的完整对比（Table 2）、消融细节、定性图、结论位于 p.13-20，仅有页眉/片段线索（提取缓存未覆盖，待核）。
3.  **相对纯 CNN 的开销**：GMSA 即便高效，相对纯 CNN 仍有注意力计算开销；极端资源受限设备上部署可能仍需进一步优化（笔者推断，非原文明述）。
4.  **设计假设**：移位窗口假设"被循环移到远端的边界像素占比小、影响可忽略"，论文以实验佐证；在极复杂纹理或中心区域是否普适，原文未单独消融（笔者补充）。
5.  **超参依赖**：GMSA 的分组与窗口大小、共享注意力的 `n` 需在效率与效果间权衡，迁移到新任务时可能需重新调优（笔者推断）。

## 个人评论

> 以下为 AI 阅读评论，非原文。

这篇论文最值得学习的是其**"以简化繁"的设计哲学**：它不堆叠复杂组件，而是针对 SR 任务的两个特殊性——**特征图大**、**需要可落地的快速推理**——把 Transformer 的每个环节逐一审视、精简。

1.  **局部特征提取**：用零参数、近乎 1×1 复杂度的 shift-conv 替代 MLP / 1×1 卷积，兼顾感受野与算量。这是把"廉价的空间归纳偏置"塞回 Transformer 的一个干净做法。
2.  **注意力计算**：GMSA 的"分组 + 多尺度窗口"巧妙化解了"长程依赖 ↔ 二次方开销"的矛盾——比小固定窗口看得更远，比大固定窗口更省，且通过窗口配比直接调控成本，比固定结构更可控。
3.  **工程级加速**：移除 LN 换 BN（可融进卷积）、对称嵌入 θ=φ（每个 SA 省一个 1×1 卷积）、共享注意力（复用注意力分数省 reshape 与卷积）——这些是可直接迁移到任意窗口 Transformer 的"推理友好"技巧，且论文用 latency（而非仅 FLOPs）这一更诚实的代理来证明收益，值得借鉴。
4.  **整体架构**：浅层特征 + 级联 ELAB + 极简重建（3×3 + PixelShuffle），证明极简流水线也能达 SOTA。

对后续研究者的启发：设计模型时应回到任务核心需求（SR 需要大感受野 + 高效推理），对通用架构（如 Swin）做**解构式针对性优化**，而非整体照搬。需要警惕的是，文中多处加速手段（共享注意力、对称嵌入）以"轻微性能损失换效率"，迁移到对精度更敏感的任务前应重新验证这一权衡。

### 使用建议

*   **快速了解**：读摘要 + 引言后半（贡献总结）+ 方法 Section 3（ELAB/GMSA/ASA）+ Table 1。
*   **复现**：精读 Section 3.2（shift-conv、GMSA、ASA、共享注意力、移位窗口的实现与图示）与 Section 4.1 训练细节（24/60 与 36/180 配置、4×4/8×8/16×16 窗口、500 epoch、lr 2e-4 与衰减节点、patch 配置）。
*   **借鉴创新点**：高效注意力模块可学 GMSA 多尺度分组 + 共享注意力；优化 Transformer 推理可借移除 LN 换 BN、对称嵌入、合并 reshape；改进局部特征提取可研究 shift-conv。
*   **写 Related Work**：可归入"高效/轻量级 Transformer""图像恢复中的注意力机制""长程依赖建模"等类别引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
计算机视觉低层视觉任务，方向是单图像超分辨率（SR）。核心目标：解决基于 Transformer 的 SR 模型计算昂贵、且因特征尺寸大而无法在大窗口上计算自注意力、难以充分挖掘长程依赖的问题。论文以一个高效、可堆叠的长程注意力块 ELAB 为核心贡献，并据此构建极简 SR 网络 ELAN，因此放在主题 `B_注意力算子模块`（注意力算子/模块）下是贴切的——其新颖性正落在注意力算子层面（GMSA + ASA + 共享注意力）；同时它也是一篇图像复原（超分）论文，应用域上与 `E_图像复原_超分_去噪_去雨去雾` 相邻。

## 2. 一句话总结
用零参数的移位卷积高效提取局部结构、用分组多尺度自注意力（GMSA）在不同窗口尺度上挖掘长程依赖，并以移除 LN/对称嵌入/共享注意力等手段加速，仅靠顺序堆叠 ELAB 就构成了 ELAN——在五个 SR 基准上取得优于/持平 SwinIR-light 的精度，同时推理约快 4.5 倍。

## 3. 背景与问题
*   **为什么要做**：CNN-based SR 用空间不变核，难自适应建模像素关系，扩大感受野要靠加深加复杂的网络、开销大；Transformer-based 能建模长程依赖，但 SA 复杂度随特征尺寸二次方增长，而 SR 特征尺寸大，迫使其只能在小窗口算 SA，限制长程建模与 SR 性能。
*   **之前方法的问题**：
    1.  **Mei 等 [40]**：非重叠 patch 独立算局部特征与 SA，可能引入边界效应、降低视觉质量。
    2.  **SwinIR [28]**：1×1 卷积提局部特征感受野小、表达弱；小固定窗口（8×8）SA 限制长程依赖；并带相对位置偏置、遮罩、LN、多残差子分支等对 SR 冗余的组件。
    3.  **Restormer [58]**：在通道空间算 SA 适配大图，但牺牲了重要的空间纹理/结构信息。
*   **核心矛盾**：用简洁结构，在低复杂度下有效建模长程依赖以提升 SR。

## 4. 核心贡献
论文正文明确列两条：(1) 提出高效长程注意力块以建模对 SR 重要的长程依赖；(2) 提出简单而强大的 ELAN，以远低于现有视觉 Transformer SR 方法的复杂度刷新 SR SOTA。展开为：
1.  **ELAB** = 两个 shift-conv（局部特征）+ 一个 GMSA，均带残差。
2.  **shift-conv [56]**：5 组特征中 4 组分别左/右/上/下移位、1 组不动 + 1×1 卷积，以近 1×1 复杂度获更大感受野、零额外可学习参数。
3.  **GMSA**：通道分 K 组、各组不同窗口 `M_k` 算 SA，复杂度 `(2/K)(Σ M_k²)HWC`，灵活权衡长程能力与成本。
4.  **ASA**（移除 LN→BN、对称嵌入 θ=φ）+ **共享注意力**（复用注意力分数）+ **改进移位窗口**（循环移位、去遮罩与相对位置编码）。
5.  **ELAN**：浅层特征 + 级联 ELAB + 3×3 卷积/PixelShuffle 重建，极简拓扑。

## 5. 方法详解
*   **整体框架（Fig.1a）**：浅层提取 `H_SF`（单个 3×3 卷积，`X_s∈R^{C×H×W}`）→ `M` 个级联 ELAB 的深层提取 `H_DF`（得 `X_d`）→ 重建 `H_RC(X_s+X_d)`（3×3 卷积 + PixelShuffle）。全局残差短接 `X_s`。损失为逐像素 L1（式 4），优化器 Adam。
*   **局部特征提取**：两个 shift-conv + 中间一个 ReLU（替代 MLP / 两个 1×1 卷积，把感受野从 1×1 放大）。
*   **GMSA（Fig.1d）**：窗口 SA 复杂度 `2M²HWC`，增大 M 二次方涨开销；GMSA 分 K 组、各组窗口 `M_k`，拼接后 1×1 卷积融合。本文用 4×4 / 8×8 / 16×16 三尺度。
*   **ASA（Fig.1e）**：① 丢 LN 用 BN（BN 推理期融进卷积、零开销；LN 会把 SA 碎片成逐元素操作）；② 对称嵌入高斯空间，令 θ=φ，每个 SA 省一个 1×1 卷积。
*   **共享注意力（Fig.2b）**：第 i 个 SA 的注意力分数被后续 n 个同尺度 SA 复用，省 2n 次 reshape 与 n 个 1×1 卷积；n 取 1 或 2 时性能仅轻微下降。
*   **移位窗口（Fig.2c）**：沿对角线循环移位（半窗口）→ 算 GMSA → 逆循环移位移回，在相邻非重叠窗口间建连接；因被移到远端的边界像素占比小，影响可忽略，故去掉了 SwinIR 的遮罩与相对位置编码。
*   **差异**：vs SwinIR——更简、shift-conv 替 1×1、GMSA 替固定小窗口、可在更大窗口算 SA、共享注意力加速；vs Restormer——在空间（非通道）维算 SA，保留空间信息。

## 6. 实验与结果
*   **数据**：DIV2K（800 训练）；Set5/Set14/BSD100/Urban100/Manga109 测试。指标 PSNR/SSIM（Y 通道），效率 #Params/#FLOPs/Latency（2080Ti，统一上采样到 1280×720）。
*   **训练细节**：ELAN-light 24 ELAB/60 通道、ELAN-normal 36 ELAB/180 通道；窗口 4×4/8×8/16×16；`n=1`；bicubic 降采样；light 取 64 个 64×64 patch、normal 取 32 个 48×48 patch；增强为随机旋转 90/180/270° + 水平翻转；Adam（0.9/0.999/1e-8），500 epoch，lr 2e-4，在 {250,400,425,450,475} epoch 各 ×0.5；PyTorch。
*   **轻量级主结果（Table 1）**：ELAN-light 在五数据集 × 三尺度均最优/次优，且比 SwinIR-light 约快 4.5×、#Params/#FLOPs 更小。Urban100：
    *   ×2：32.76/0.9340（与 SwinIR-light 持平）；582K/168.4G/230ms vs 878K/195.6G/1007ms。
    *   ×3：28.69/0.8624（略优于 28.66/0.8624）；590K/75.7G/105ms vs 886K/87.2G/445ms。
    *   ×4：26.54/0.7982（优于 26.47/0.7980）；601K/43.2G/62ms vs 897K/49.6G/271ms。
    *   观察：相近 #Params/#FLOPs 下 Transformer（尤其 SwinIR-light）PSNR/SSIM 显著优于 CNN，但 SwinIR-light latency 比 CNN 慢 >10×；ELAN-light 兼得精度与速度。
*   **定性**：×4 下 CNN 模型边缘模糊扭曲，SwinIR-light 部分结构仍不准（Fig.3/4 完整对比在提取缓存外，待核）。
*   **消融 / classic 对比 / 结论**：据原文后续页线索（提取缓存未覆盖，待核）：p.13 Table 2 为 classic SR 模型对比，并报告"用 ASA 替换 SA 后 latency 大幅下降而 PSNR/SSIM 不降（如 177→66ms）""引入长程依赖后 Urban100/Manga109 PSNR 分别 +0.21/+0.19 dB"；p.14 起为共享注意力深度的消融；p.16 为 Conclusion。

## 7. 这篇论文真正有价值的地方
"以简化繁"的设计哲学与可迁移的工程技巧：(1) 用 shift-conv 把廉价空间归纳偏置塞回 Transformer；(2) GMSA 用"分组 + 多尺度窗口"以可控方式化解"长程依赖 ↔ 二次方开销"矛盾；(3) 移除 LN 换 BN、对称嵌入 θ=φ、共享注意力等推理友好技巧，可直接迁移到其它窗口 Transformer；(4) 用 latency 这一更诚实的代理（而非仅 FLOPs）证明收益。启发：回到任务核心需求，对通用架构做解构式针对性精简，而非整体照搬。

## 8. 局限与问题
1.  仅在通用单图像 SR 上验证，未涉视频/遥感/医学等域。
2.  本笔记证据主体为提取缓存前 12 页；classic 完整对比（Table 2）、消融、定性图、结论在 p.13-20，仅有片段线索（待核）。
3.  多处加速以"轻微精度损失换效率"（共享注意力、对称嵌入），对精度敏感任务需重新验证此权衡（笔者推断）。
4.  移位窗口"边界像素影响可忽略"以实验佐证，普适性未单独深究（笔者补充）。
5.  GMSA 分组/窗口与共享注意力 `n` 为需调超参，迁移新任务可能需重调（笔者推断）。

## 9. 我该怎么使用这篇论文
*   **快速了解**：摘要 + 引言贡献段 + 方法 Section 3 + Table 1。
*   **复现**：精读 Section 3.2 各模块实现与 Fig.1/2 图示，及 Section 4.1 配置（24/60、36/180、4/8/16 窗口、500 epoch、lr 2e-4 衰减节点、patch 配置）。
*   **借鉴创新点**：高效注意力→GMSA 多尺度分组 + 共享注意力；推理加速→移除 LN 换 BN、对称嵌入、合并 reshape；局部特征→shift-conv。
*   **写 Related Work**：归入"高效/轻量级 Transformer""图像恢复中的注意力""长程依赖建模"。

## 10. 和其他论文的关系
基于主题 `B_注意力算子模块` 与论文内容，本文与以下相关（论文正文点名引用 [28][35][58][40][56][30] 等）：
*   `[[SwinIR]]`：主对比基线，本文对其做多项关键简化（去 LN/遮罩/相对位置编码、换 shift-conv、换 GMSA、加共享注意力）。
*   `[[Restormer]]`：通道维注意力的图像恢复思路，本文与其在空间 vs 通道维度上形成对比。
*   `[[Swin Transformer]]`：SwinIR 的骨干，本文设计源于对其在 SR 上冗余成分的分析与简化。
*   `[[Shift Convolution]]`（shift-conv [56]）：本文局部特征提取核心技术。
*   `[[Non-Local / Embedded Gaussian]]`（[30][5]）：对称嵌入高斯空间设置 θ=φ 的依据来源。

## 11. 关键词
图像超分辨率, 长程注意力, Transformer, 移位卷积 shift-conv, 分组多尺度自注意力 GMSA, 加速自注意力 ASA, 共享注意力, 移位窗口, 高效注意力, ELAN/ELAB

## 12. 可信度说明
本笔记证据主体来自 PDF 提取缓存（前 12 页），完整覆盖了**摘要、引言、相关工作、方法（Section 3 全部：整体流水线 + ELAB + GMSA + ASA + 共享注意力 + 移位窗口）** 与**实验设置（Section 4.1）+ 轻量级主结果（Table 1）**。所有核心贡献、方法细节、训练超参与 Table 1 数值均能在提取文本中直接核对。p.13-20（classic 模型对比 Table 2、组件消融、定性图 Fig.3/4 完整对比、Conclusion）不在提取缓存内，笔记中相关条目均显式标注"据原文后续页，提取缓存未覆盖，待核"。基于已覆盖内容构建的核心脉络可信度高。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本 ~2086 字符/页, 无明显乱码); 来源缓存: `.paper-cache/extracts/ELAB.txt` (提取覆盖 12/20 页; 本次精读以前 12 页为事实主体, p.13-20 仅依页眉/片段线索并已逐处标注待核); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
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
