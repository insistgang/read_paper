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
| **作者** | Mingjun Zheng; Long Sun; Jiangxin Dong; Jinshan Pan（南京理工大学计算机科学与工程学院；前两位为共同一作，Jinshan Pan 为通讯作者） |
| **发表时间** | 2024 |
| **刊物/会议** | ECCV |
| **DOI** | 未明确（开源代码: https://github.com/Zheng-MJ/SMFANet） |

## 摘要

> **清理后英文原摘要**: Transformer-based restoration methods achieve significant performance as the self-attention (SA) of the Transformer can explore non-local information for better high-resolution image reconstruction. However, the key dot-product SA requires substantial computational resources, which limits its application in low-power devices. Moreover, the low-pass nature of the SA mechanism limits its capacity for capturing local details, consequently leading to smooth reconstruction results. To address these issues, we propose a self-modulation feature aggregation (SMFA) module to collaboratively exploit both local and non-local feature interactions for a more accurate reconstruction. Specifically, the SMFA module employs an efficient approximation of self-attention (EASA) branch to model non-local information and uses a local detail estimation (LDE) branch to capture local details. Additionally, we further introduce a partial convolution-based feed-forward network (PCFN) to refine the representative features derived from the SMFA. Extensive experiments show that the proposed SMFANet family achieve a better trade-off between reconstruction performance and computational efficiency on public benchmark datasets. In particular, compared to the ×4 SwinIR-light, SMFANet+ achieves 0.14dB higher performance over five public test sets on average, and ×10 times faster runtime, with only about 43% of the model complexity (e.g., FLOPs).

> **中文翻译**: 基于 Transformer 的图像恢复方法因其自注意力（SA）能探索非局部信息、利于高分辨率图像重建而取得显著性能。然而，关键的点积自注意力需要大量计算资源，限制了它在低功耗设备上的应用；此外，SA 机制的低通滤波本质限制了它捕捉局部细节的能力，导致重建结果偏平滑。为解决这些问题，本文提出一个自调制特征聚合（SMFA）模块，协同利用局部与非局部特征交互以实现更精确的重建。具体而言，SMFA 模块用一个高效近似自注意力（EASA）分支建模非局部信息，用一个局部细节估计（LDE）分支捕捉局部细节。此外，本文进一步引入一个基于部分卷积的前馈网络（PCFN），在 SMFA 输出特征基础上做进一步精炼。大量实验表明，所提 SMFANet 系列在公开基准数据集上取得了重建性能与计算效率之间更优的权衡。特别地，相比 ×4 的 SwinIR-light，SMFANet+ 在五个公开测试集上平均 PSNR 高 0.14dB，运行速度约快 10 倍，而模型复杂度（如 FLOPs）仅约为其 43%。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：单图像超分辨率（SISR）是从退化的低分辨率（LR）图像恢复高分辨率（HR）图像。随着流媒体平台兴起和超高清（UHD）内容成为产业标准，SISR 能以更低的传输成本提供更好的观看体验，因而备受关注。但 SISR 是不适定（ill-posed）问题，传统手工先验或插值方法难以很好求解。
- **之前方法的两条技术路线及其问题**：
    1.  **CNN 路线**：卷积算子具有平移不变性但感受野有限，难以建模非局部信息。为提升表达能力，CNN 方法越做越深越大（如 RCAN 有 15.59M 参数、400+ 层），计算开销高，无法部署到智能手机等资源受限设备。
    2.  **ViT/自注意力路线**：自注意力能有效建模非局部信息，但**计算成本高、显存消耗大**。窗口注意力、转置注意力、权重复用等变体虽缓解了开销，仍需较长时间学习特征依赖。更关键的是，研究表明 **ViT 偏好学习低频成分（低通滤波特性）**，导致重建结果平滑、丢失局部高频细节。
- **核心矛盾（论文自问）**：能否设计一个高效的特征调制模块，既能以类似自注意力的方式探索非局部信息，又能建模局部细节，从而实现高效图像超分辨率？

## 关键贡献

论文在 Introduction 末尾给出三条贡献（精确对应原文）：

1.  **提出高效 SMFA 模块**：用于提取表征性特征，其中 EASA 分支探索非局部信息、LDE 分支捕捉局部特征。
2.  **提出轻量级 PCFN**：在空间与通道维度上进一步精炼 SMFA 提取的特征。
3.  **在公开基准上做了定量与定性评估**，结果表明本方法在模型复杂度与重建性能之间取得了有利权衡。

> 摘要补充的量化结论：相比 ×4 SwinIR-light，SMFANet+ 在五个测试集上平均 PSNR 高 0.14dB、速度约快 10 倍、FLOPs 仅约 43%。（注：原笔记将"PCFN/SMFANet"等也算入贡献条目，但原文贡献列表仅 3 条，此处按原文修正。）

## 方法

- **整体框架（3.1）**：输入 LR 图像 → 一个 3×3 卷积提取浅层特征 → 一系列特征调制块（FMB）产生深度特征 → 轻量级图像重建模块（3×3 卷积调整通道数 + PixelShuffle 上采样）输出 HR 图像。为利于高频信息学习，在重建模块之前插入一个**全局残差连接**。每个 FMB 由一个 SMFA 模块和一个 PCFN 组成。
- **SMFA 模块（3.2，公式 1–6）**：核心创新。
    - **输入处理**：对输入特征 $F_{in}\in\mathbb{R}^{H\times W\times C}$ 先做 L2 归一化，再用 1×1 卷积扩展通道，然后通道分割 $S(\cdot)$ 得到 $X\in\mathbb{R}^{H\times W\times C}$ 与 $Y\in\mathbb{R}^{H\times W\times C}$，分别送入 EASA 与 LDE 分支（公式 1）。
    - **EASA 分支（处理 $X$，公式 3–5）**：
        - 自适应最大池化 $D(\cdot)$（缩放因子 8）下采样获取低频成分，再经 3×3 深度卷积生成非局部结构信息 $X_s\in\mathbb{R}^{H/8\times W/8\times C}$。
        - 计算输入 $X$ 的全局方差 $\sigma^2(X)\in\mathbb{R}^{1\times 1\times C}$（作为空间信息的统计描述），与 $X_s$ 相加后经 1×1 卷积得到调制特征 $X_m$（公式 4）。这一**方差调制**机制有助于更好地探索非局部信息。
        - 最终用调制特征聚合输入：$X_l = X\odot\, U(\phi(X_m))$，其中 $\phi$ 为 GELU 激活、$U$ 为最近邻上采样、$\odot$ 为逐元素乘（公式 5）。
    - **LDE 分支（处理 $Y$，公式 6）**：用一个扩展的 3×3 深度卷积编码局部信息 $Y_h\in\mathbb{R}^{H\times W\times 2C}$（$Y_h=\text{Conv}_{1\times1}(\text{DWConv}_{3\times3}(Y))$），再用两个 1×1 卷积夹一个 GELU 生成增强局部特征 $Y_d$。
    - **特征融合（公式 2）**：$F_\rho = \text{Conv}_{1\times1}(X_l + Y_d)$。
- **PCFN（3.3，公式 7）**：改进常规 FFN（FFN 逐像素相同处理、缺乏空间维度的信息交换）。
    - 先用 1×1 卷积 + GELU 在扩展隐空间上做跨通道交互。
    - 将隐特征通道分为两块 $\{F_\rho^1, F_\rho^2\}$，其中 $F_\rho^1\in\mathbb{R}^{H\times W\times C/2}$、$F_\rho^2\in\mathbb{R}^{H\times W\times 3C/2}$（即仅对 1/4 通道做空间卷积，据原文后续页 p.14 "processes only 1/4")。
    - 对 $F_\rho^1$ 用 3×3 卷积 + GELU 编码局部上下文，再与 $F_\rho^2$ 拼接，经 1×1 卷积混合并还原通道数。
- **FMB（3.4，公式 8）**：将 SMFA 与 PCFN 串联并各加残差连接：$F_\rho = \text{SMFA}(F_{in}) + F_{in}$，$\hat{F}_\rho = \text{PCFN}(F_\rho) + F_\rho$，以稳定训练、促进信息流动。
- **训练方式（4.1）**：训练集 DIV2K 或 DF2K；从 LR 随机裁 64 个 64×64 patch，随机水平翻转与旋转。**损失函数与 SAFMN 相同**（原文表述 "trained with the same loss function as SAFMN"，未在提取文本中点名为 L1，此处按原文修正；原笔记直接写"L1 损失"属推断）。优化器 Adam（β1=0.9, β2=0.99），初始学习率 1e-3、最小 1e-5，余弦退火更新；迭代 1,000,000 次；PyTorch + 单卡 NVIDIA RTX 3090。两个版本：标准 SMFANet（8 个 FMB，36 通道）、SMFANet+（12 个 FMB，48 通道）。
- **与已有方法的差异**：
    - 相比**纯 CNN 渐进式特征精炼方法**（IMDN/RFDN/BSRN 等）：SMFANet 通过 EASA 显式建模非局部交互，捕获全局结构。
    - 相比**非局部特征调制方法**（VapSR 用大核卷积扩大感受野、SAFMN 用多下采样率获取多尺度、MDRN 用并行步长卷积+池化）：论文指出仅用聚合的非局部特征、忽略局部特征会在角点/边缘处产生伪影，故 SMFA **协同**建模局部与非局部特征。
    - 相比**ViT 方法**（IPT/SwinIR/ELAN）：这些仍依赖基于窗口的注意力变体，跨窗口特征交互耗时；EASA 以远更低的复杂度近似自注意力。
- **论文类型特化（注意力类）**：本文属**轻量化注意力（替代）模块设计**。EASA 主要作用于**空间维度**，通过 8× 下采样 + 深度卷积 + 方差调制 + 上采样逐元素聚合来近似自注意力的"整合全局信息"功能，避免了 $QK^T$ 的开销；设计为可插入的核心特征提取单元，重点论证 FLOPs/运行时间与 PSNR/SSIM 之间的权衡。

## 实验

- **使用数据集**：
    - **训练集**：DIV2K 或 DIV2K + Flickr2K（DF2K），二选一以与不同 SOTA 公平对比。
    - **测试集**：Set5, Set14, B100, Urban100, Manga109。
- **对比方法**：CNN 轻量级 SR（CARN, IMDN, RFDN, BSRN, SAFMN 等）与 ViT 方法（SwinIR-light, ELAN 等）。提取文本在 4.2 节"Quantitative comparison"处截断（原文 39047 字符，仅提取前 25000），完整对比表格未纳入。
- **评价指标**：PSNR 与 SSIM，均在 YCbCr 色彩空间的 **Y 通道**上计算。
- **主实验结果（据摘要与图 1）**：相比 ×4 SwinIR-light，SMFANet+ 在五个公开测试集上平均 PSNR 高 0.14dB、运行速度约快 10 倍、FLOPs 仅约 43%（即降低约 57%）。
- **消融实验（据原文后续页，提取缓存未覆盖，待核）**：
    - p.13 线索：图 5 给出 SMFA 在 ×4 Urban100 上的有效性，图 6 给出 $F_{in}, X_l, \dots$ 的功率谱密度（PSD）可视化；Table 5 显示移除某组件后 PSNR 在 Urban100/Manga109 上分别下降约 0.06/0.08dB、0.11dB 等。
    - p.14 线索：Table 4 为 ×4 SMFANet 在 Urban100/Manga109 上的消融（"A→B" 表示用 B 替换 A、"A→None" 表示移除 A）；PCFN 移除或替换为标准 FFN 后，Manga109 上 PSNR 下降约 0.34dB / 0.16dB（Table 5）。
    - 以上数字来自提取文本中的缺失页摘录线索，未在主体提取文本中完整呈现，**待核**。
- **结论（据原文后续页 p.14）**：第 6 节 Conclusion 称"提出了一个简单而有效的 SMFANet 来解决图像超分辨率"。
- **效率信息**：图 1 中左图圆圈大小表示模型 FLOPs、右图圆圈大小表示推理所需 GPU 显存；SMFANet 系列在效率-性能权衡上优于其他方法（图 1 以 Manga109 ×4 为例）。

## 局限

提取文本（前 12 页）中未见作者对自身方法局限性的集中讨论；以下为基于方法设计的分析（非原文明述）：
- **适用场景**：方法面向计算效率优化，适合移动端/嵌入式。对计算资源不受限、追求极致保真度的场景，轻量化设计未必最优。
- **固定下采样因子**：EASA 用固定 8× 自适应最大池化获取低频信息，该因子是否最优、是否应随图像内容自适应，是可能的改进点。
- **退化建模**：仅在标准学术 SR 数据集（bicubic 退化）上验证，对真实复杂退化（未知模糊核、复合噪声）的表现未涉及。
- **实验完整性**：提取缓存在 4.2 节截断，完整的逐数据集 PSNR/SSIM 表格、消融全表、可视化结果未纳入分析（部分数字见上方"据后续页"线索）。
- **复现风险**：论文开源代码（GitHub），复现风险较低；但 L2 归一化实现、方差计算维度、损失函数具体形式（"与 SAFMN 相同"）等细节建议对照代码确认。

## 个人评论

这篇论文最值得学习的，是其"协同建模"的设计取向与"高效近似"的实现策略。

1.  **思想启发**：它没有在"自注意力 vs 卷积"之间二选一，而是清醒地认识到非局部全局结构与局部高频细节对图像重建都重要，于是用 EASA + LDE 两个并行分支各司其职、优势互补。这对处理"全局 vs 局部"矛盾的任务是一个清晰范式。
2.  **技术启发**：EASA 用"下采样取低频结构 → 全局**方差**作统计调制 → 上采样后逐元素乘"来近似自注意力，抓住了 SA"整合全局信息"的本质，却绕开了 $QK^T$ 的二次开销。用信号处理/统计量替代复杂算子，这一思路迁移性很强。一个值得复核的细节是：EASA 用的是**方差**（二阶统计量）而非均值，论文强调它作为"空间信息的统计散度"——这点比一般的全局平均池化调制更有信息量。
3.  **工程启发**：把新算子（SMFA）与改进的 FFN（PCFN，部分卷积只动 1/4 通道）用残差连接组装成稳定训练单元（FMB），是模块化设计的良好范例。

### 使用建议

- **快速了解**：读 Abstract、Introduction 末段（核心矛盾自问）、图 1 即可把握动机/贡献/主要结果。
- **如果复现**：精读第 3 节，尤其 3.2（SMFA，公式 1–6）、3.3（PCFN，公式 7）、3.4（FMB，公式 8），结合图 2 与 GitHub 代码；注意损失函数"与 SAFMN 相同"需查代码确认。
- **如果借鉴创新点**：学 EASA 的"下采样→深度卷积→方差调制→上采样聚合"非局部建模范式，以及 PCFN"通道分割、只对部分通道做空间卷积"的省算思路。
- **如果写 Related Work**：可归入"轻量化/高效自注意力替代模块"或"用于图像恢复的局部-非局部特征聚合方法"。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属计算机视觉中的**高效图像超分辨率**方向，发表于 ECCV 2024（南京理工大学 Jinshan Pan 组）。它要解决两个痛点：标准点积自注意力计算/显存开销大，且自注意力的低通滤波特性导致重建结果平滑、丢失高频细节。论文的"头牌"贡献是一个可插入的特征调制算子 SMFA（含 EASA 与 LDE 两分支）及配套前馈网络 PCFN，因此归入"B_注意力算子模块"主题——关注轻量化、高效的自注意力近似/替代算子设计；它同时也是一篇图像复原（超分）论文。

## 2. 一句话总结
本文提出轻量超分网络 SMFANet，核心是自调制特征聚合（SMFA）模块：用 EASA 分支（下采样取低频 + 全局方差调制 + 上采样逐元素聚合）以极低成本近似自注意力建模非局部信息，用 LDE 分支建模局部细节，并以基于部分卷积的前馈网络 PCFN 精炼特征，从而在大幅降低 FLOPs/运行时间的同时取得优于 SwinIR-light 等方法的重建质量。

## 3. 背景与问题
- **为什么要做**：SISR 是从退化 LR 恢复 HR 的不适定问题；UHD/流媒体时代需求大。CNN 路线感受野有限、做大后开销高（RCAN 15.59M 参数、400+ 层）；ViT 路线虽能建模非局部但计算/显存昂贵，且偏好低频导致重建平滑。
- **核心矛盾**：能否设计一个高效特征调制块，既以类自注意力方式探索非局部信息，又能建模局部细节，用于高效超分？
- **两个具体短板**：
    1.  点积自注意力计算资源消耗大，难上低功耗设备。
    2.  自注意力低通特性丢失角点/边缘等局部高频细节。

## 4. 核心贡献
原文 Introduction 末列三条：
1.  **SMFA 模块**：EASA 分支探索非局部信息、LDE 分支捕捉局部特征。
2.  **轻量 PCFN**：在空间与通道维度进一步精炼 SMFA 输出特征。
3.  **公开基准上的定量+定性评估**，证明在模型复杂度与重建性能间取得有利权衡。
量化亮点（摘要）：相比 ×4 SwinIR-light，SMFANet+ 平均 PSNR 高 0.14dB、约快 10×、FLOPs 约 43%。

## 5. 方法详解
- **整体架构（3.1）**：LR → 3×3 卷积浅层特征 → 多个 FMB（SMFA+PCFN）→ 3×3 卷积 + PixelShuffle 重建；重建前有全局残差连接以利高频学习。
- **SMFA（3.2，公式 1–6）**：
    - 公式 1：$\{X,Y\}=S(\text{Conv}_{1\times1}(\lVert F_{in}\rVert_2))$，L2 归一化 + 1×1 升维 + 通道分割。
    - EASA（处理 $X$）：$X_s=\text{DWConv}_{3\times3}(D(X))$（$D$ 为 8× 自适应最大池化，$X_s\in\mathbb{R}^{H/8\times W/8\times C}$，公式 3）；$X_m=\text{Conv}_{1\times1}(X_s+\sigma^2(X))$（$\sigma^2(X)\in\mathbb{R}^{1\times1\times C}$ 为全局方差，公式 4）；$X_l=X\odot U(\phi(X_m))$（GELU + 最近邻上采样 + 逐元素乘，公式 5）。
    - LDE（处理 $Y$）：$Y_h=\text{Conv}_{1\times1}(\text{DWConv}_{3\times3}(Y))$，$Y_d=\text{Conv}_{1\times1}(\phi(Y_h))$（$Y_h\in\mathbb{R}^{H\times W\times 2C}$，公式 6）。
    - 融合：$F_\rho=\text{Conv}_{1\times1}(X_l+Y_d)$（公式 2）。
- **PCFN（3.3，公式 7）**：$\{F_\rho^1,F_\rho^2\}=S(\phi(\text{Conv}_{1\times1}(\lVert F_\rho\rVert_2)))$，$\hat{F}_\rho=\text{Conv}_{1\times1}(C([\phi(\text{Conv}_{3\times3}(F_\rho^1)),F_\rho^2]))$；其中 $F_\rho^1\in\mathbb{R}^{H\times W\times C/2}$、$F_\rho^2\in\mathbb{R}^{H\times W\times 3C/2}$，即只对约 1/4 通道做 3×3 空间卷积（据后续页 p.14）。
- **FMB（3.4，公式 8）**：$F_\rho=\text{SMFA}(F_{in})+F_{in}$，$\hat{F}_\rho=\text{PCFN}(F_\rho)+F_\rho$。
- **训练（4.1）**：DIV2K/DF2K；64 个 64×64 patch + 翻转旋转；损失"与 SAFMN 相同"；Adam(0.9,0.99)，lr 1e-3→1e-5 余弦退火，1,000,000 迭代；单卡 RTX 3090。标准版 8 FMB/36 通道，SMFANet+ 12 FMB/48 通道。
- **与同类差异**：相对 VapSR/SAFMN/MDRN 等"仅聚合非局部特征"方法，SMFA 强调协同建模局部+非局部以避免角点/边缘伪影；相对 SwinIR/ELAN 等窗口注意力，EASA 复杂度远更低。

## 6. 实验与结果
- **数据集**：训练 DIV2K / DF2K；测试 Set5、Set14、B100、Urban100、Manga109。
- **指标**：Y 通道（YCbCr）上的 PSNR 与 SSIM。
- **对比方法**：CNN 轻量级（CARN/IMDN/RFDN/BSRN/SAFMN…）与 ViT（SwinIR-light/ELAN…）。
- **主结果**：相比 ×4 SwinIR-light，SMFANet+ 五测试集平均 PSNR +0.14dB、约 10× 更快、FLOPs ≈43%。
- **消融（据后续页，提取缓存未覆盖，待核）**：Table 4 为 Urban100/Manga109 上的逐组件消融（A→B 替换 / A→None 移除）；移除/替换 PCFN 为标准 FFN 后 Manga109 PSNR 降约 0.34/0.16dB（Table 5）；移除方差调制等组件在 Urban100/Manga109 上 PSNR 降约 0.06–0.11dB；图 5 验证 SMFA 有效性、图 6 用功率谱密度（PSD）展示 EASA 确实补回了被低通抑制的频段。
- **提取局限**：4.2 节定量对比表在提取文本第 25000 字符处截断，完整数值表未纳入。

## 7. 这篇论文真正有价值的地方
1.  **协同建模**：不在"注意力 vs 卷积"间二选一，而是 EASA + LDE 双分支并行，分别管全局结构与局部细节，互补避免单一非局部聚合导致的角点/边缘伪影。
2.  **高效近似**：EASA 用"下采样 + 全局**方差**调制 + 上采样逐元素乘"近似自注意力，抓住"整合全局信息"的本质而绕开 $QK^T$ 开销——用统计量替代复杂算子的范式很值得迁移。方差（二阶统计量）作调制信号，比常见的均值/全局平均池化调制更有判别力。
3.  **频域视角的自洽**：方法在动机层面用"ViT 是低通滤波器"立论，又（据后续页图 6 PSD）从频域验证 EASA 补回高频，论证链条闭合。

## 8. 局限与问题
- 提取的前 12 页未见作者集中讨论局限；以下为分析（非原文）。
- **固定 8× 下采样**：低频获取因子固定，未必对所有内容/尺度最优。
- **退化设定单一**：仅标准 bicubic 退化基准，未涉真实未知退化。
- **损失函数表述含糊**：仅称"与 SAFMN 相同"，未在提取文本中点名为 L1（SAFMN 实际用 L1，但此处不据此断言）。
- **提取截断**：完整 PSNR/SSIM 表与消融全表未在主体提取文本中呈现，部分数字来自缺失页摘录线索，需对照原文核实。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Introduction 末段 + 图 1。
- **复现**：第 3 节（公式 1–8）+ 图 2 + GitHub 代码；注意损失函数需查代码。
- **借鉴创新点**：EASA 的"下采样→深度卷积→方差调制→上采样聚合"非局部范式；PCFN"部分卷积只动 1/4 通道"的省算思路。
- **写 Related Work**：归入"轻量化/高效自注意力替代模块"或"图像恢复的局部-非局部特征聚合"。

## 10. 和其他论文的关系
- **窗口/区域自注意力**：`[[SwinIR]]`、ELAN——本文以更低成本近似/替代这类注意力。
- **非局部特征调制的轻量 SR**：SAFMN（多下采样率多尺度）、VapSR（大核卷积）、MDRN（并行步长卷积+池化）——同目标、不同融合模块；本文强调"协同局部+非局部"。
- **CNN 轻量 SR**：IMDN、RFDN（NTIRE 2022 Efficient SR 冠军方案的前身/改进）、BSRN（蓝图卷积）——同类竞争，本文额外引入非局部建模能力。
- **方差/统计量调制**：与用统计量做特征校准/调制的工作（如 SENet 系全局池化调制）思路相通，但本文用二阶方差而非一阶均值。

## 11. 关键词
高效图像超分辨率, 自注意力近似, 特征聚合, 自调制, 局部与非局部信息, 轻量级网络, 方差调制, 部分卷积, 前馈网络(PCFN), 计算效率(FLOPs/运行时间)

## 12. 可信度说明
本精读主要基于 PDF 提取文本的前 12 页（含标题/作者/摘要、引言、相关工作、方法 3.1–3.4 全部公式、实验设置 4.1 及对比章节开头），提取质量良好（约 2086 字符/页），公式与符号清晰可读。**实验结果的具体数值表（逐数据集 PSNR/SSIM）与完整消融表未纳入主体提取文本**：4.2 节在第 25000 字符处截断（原文 39047 字符）；消融与结论的部分数字（如 PCFN 移除 Manga109 降 0.34/0.16dB、Table 4/5、图 5/6）来自提取文本附带的"缺失页摘录线索（p.13–14）"，标注为"据后续页，待核"。因此涉及实验数字之处可信度受限，方法与动机部分可信度高。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)，主体覆盖 12/17 页，4.2 实验对比表在 25000 字符处截断); 来源缓存: `.paper-cache/extracts/FMB.txt` (12/17 页主体 + 缺失页 p.13-17 摘录线索); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。本轮据提取文本重核: 重建摘要英文+中文、修正贡献为原文 3 条、损失函数改为"与 SAFMN 相同"（不再断言 L1）、补全公式张量维度、消融数字标注"据后续页待核"。
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
