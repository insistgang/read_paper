---
title: "Adapt or Perish: Adaptive Sparse Transformer with Attentive Feature Refinement for Image Restoration"
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

# Adapt or Perish: Adaptive Sparse Transformer with Attentive Feature Refinement for Image Restoration

## 基本信息
- **PDF**: [[ASSA&FRFN.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Adapt or Perish: Adaptive Sparse Transformer with Attentive Feature Refinement for Image Restoration |
| **作者** | Shihao Zhou; Duosheng Chen; Jinshan Pan; Jinglei Shi; Jufeng Yang（南开大学 VCIP & TMCC & DISSec / 南京理工大学） |
| **发表时间** | 2024 |
| **刊物/会议** | CVPR 2024 |
| **DOI** | 未明确（代码: https://github.com/joshyZhou/AST） |

## 摘要

> **英文原文（据 PDF 提取文本整理）**：Transformer-based approaches have achieved promising performance in image restoration tasks, given their ability to model long-range dependencies, which is crucial for recovering clear images. Though diverse efficient attention mechanism designs have addressed the intensive computations associated with using transformers, they often involve redundant information and noisy interactions from irrelevant regions by considering all available tokens. In this work, we propose an Adaptive Sparse Transformer (AST) to mitigate the noisy interactions of irrelevant areas and remove feature redundancy in both spatial and channel domains. AST comprises two core designs, i.e., an Adaptive Sparse Self-Attention (ASSA) block and a Feature Refinement Feed-forward Network (FRFN). Specifically, ASSA is adaptively computed using a two-branch paradigm, where the sparse branch is introduced to filter out the negative impacts of low query-key matching scores for aggregating features, while the dense one ensures sufficient information flow through the network for learning discriminative representations. Meanwhile, FRFN employs an enhance-and-ease scheme to eliminate feature redundancy in channels, enhancing the restoration of clear latent images. Experimental results on commonly used benchmarks have demonstrated the versatility and competitive performance of our method in several tasks, including rain streak removal, real haze removal, and raindrop removal.

> **中文翻译**：基于 Transformer 的方法因其建模长距离依赖的能力，在图像恢复任务中取得了不错的性能，而这种能力对于恢复清晰图像至关重要。尽管已有各种高效注意力机制设计来缓解 Transformer 的密集计算开销，但它们往往因考虑所有可用 token 而引入冗余信息与来自无关区域的噪声交互。本文提出自适应稀疏 Transformer（AST），在空间域与通道域两个维度同时缓解无关区域的噪声交互并消除特征冗余。AST 由两个核心设计构成：自适应稀疏自注意力（ASSA）模块与特征精炼前馈网络（FRFN）。具体而言，ASSA 采用双分支范式自适应计算——稀疏分支用于过滤低 query-key 匹配分数带来的负面影响，密集分支则保证网络中有足够的信息流以学习判别性表示；FRFN 采用"增强-缓解"方案消除通道维度的特征冗余，从而提升清晰潜在图像的恢复质量。在常用基准上的实验在去雨条纹、真实去雾、去雨滴等多个任务上验证了方法的通用性与有竞争力的性能。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：图像恢复旨在从退化图像中恢复清晰图像。CNN 方法（卷积单元）受限于感受野，难以建模长距离依赖；Transformer 通过自注意力探索全局相关性弥补了这一点，但其原始自注意力具有二次复杂度，难以应用到高分辨率图像。
- **之前方法的问题**：现有高效注意力（Restormer 的通道注意力、Uformer/SwinIR 的窗口注意力、GRL 的窗口+通道组合）虽缓解了计算量，但仍存在两个症结：1) 标准 Transformer 用**密集注意力**聚合特征，会在无关区域引入噪声交互；2) 密集聚合的特征图中存在**冗余信息**，阻碍模型关注信息性特征。已有的去冗余尝试也各有缺陷——DRSformer 用 Top-K 通道选择，但参数 K 对具体恢复任务敏感；CODE 把特征投影到超像素空间，但超像素空间内的自注意力仍涉及所有 token，仍可能引入无关交互。
- **稀疏化的两难**：用平方 ReLU（squared ReLU）激活可实现稀疏注意力，它能移除负相关分数且不依赖像 Top-K 那样的参数设置；但过度稀疏会造成信息损失，通常需要额外设计来"放松"稀疏性，这又与改用稀疏注意力的初衷相矛盾。
- **核心矛盾**：如何在保证网络中有足够信息流的同时，有效**过滤无关区域的噪声交互**并**消除特征冗余**，且对具体恢复任务不敏感。

## 关键贡献

1.  提出**自适应稀疏 Transformer（AST）**——一个高效的 Transformer 图像恢复模型，让最有用的信息向前流动，提取更具建设性的特征用于恢复清晰图像。
2.  设计 **ASSA 块**，包含一个密集自注意力分支（DSA）和一个稀疏自注意力分支（SSA），以自适应权重融合：既能捕获 token 间信息性交互，又能保留必要信息。同时提出**特征精炼前馈网络（FRFN）**，基于特征变换方案"增强有价值特征、抑制次要特征"。
3.  在去雨条纹、去雾、去雨滴三类退化上进行了全面实验，证明 AST 设计的优越性，并提供了大量消融研究佐证各设计的贡献（消融表格在提取缓存覆盖范围之外，未在本笔记中列出）。

## 方法

- **整体框架**（图 2）：AST 采用对称编码器-解码器结构。给定退化图像 `I ∈ R^{H×W×3}`，先经一层卷积得到浅层特征 `F0 ∈ R^{H×W×C}`，再通过 N1=4 个阶段的对称编解码网络得到深层特征 `Fd`，最后一层卷积从 `Fd` 预测残差图 `R ∈ R^{H×W×3}`，恢复图像为 `Î = I + R`。
- **编码器只用 FRFN**：作者刻意在编码器的标准 Transformer 块中省略注意力机制，因为自注意力的"低通滤波"特性会妨碍学习理想的局部模式（尤其在早期阶段）。**解码器的基本块则同时包含 ASSA 和 FRFN**；解码器前还有一个 bottleneck 阶段（与解码器共享同一种 Transformer 块）以捕获更长依赖。编码器特征通过 identity 连接与解码器特征融合。
- **关键模块**：
    1.  **自适应稀疏自注意力（ASSA）**——双分支结构（窗口内计算）。给定归一化特征 `X`，先划分为不重叠的 `M×M` 窗口（默认窗口大小 8），每窗口展平为 `R^{M²×C}`，再生成 `Q=XW_Q, K=XW_K, V=XW_V`（投影矩阵 `W∈R^{C×d}` 跨窗口共享）。通用注意力形式为 `A = f(QKᵀ/√d + B)V`，`B` 为可学习相对位置偏置。
        - **密集分支 DSA**（公式 4）：`DSA = Softmax(QKᵀ/√d + B)`，保留所有 query-key 对，确保信息流但引入无关区域噪声。
        - **稀疏分支 SSA**（公式 5）：`SSA = ReLU²(QKᵀ/√d + B)`，移除负分数交互，实现稀疏，但单用会造成过度稀疏、信息不足。
        - **自适应融合**（公式 6）：`A = (w1·SSA + w2·DSA)V`。权重由可学习参数 `{a1,a2}`（初始化为 1）经类 softmax 归一化得到（公式 7）：`wn = e^{an} / Σ e^{ai}`。这让模型按任务自适应调节稀疏程度，兼取两分支之长。
    2.  **特征精炼前馈网络（FRFN）**——"增强-缓解（enhance-and-ease）"方案，针对**通道维度**的冗余（与 ASSA 在空间域去冗余互补），公式 8 为：
        - 增强：`X̂' = GELU(W1·PConv(X̂))`，用**部分卷积 PConv** 强化特征中信息性元素。
        - 缓解（门控）：沿通道切分 `[X̂'1, X̂'2] = X̂'`；将 `X̂'2` 经 Reshape 转为 2D 特征图后做**深度卷积 DWConv**，再 Flatten，与 `X̂'1` 做矩阵乘（⊗）门控：`X̂'r = X̂'1 ⊗ F(DWConv(R(X̂'2)))`。Reshape/Flatten 用于引入局部性。
        - 输出：`X̂'out = GELU(W2·X̂'r)`。
- **模块连接**：解码器基本块中，特征先 LN → ASSA，再 LN → FRFN（图 2）。
- **训练**：Charbonnier 损失（公式 1）`ℓ = √(‖I'−Î‖² + ε²)`，`ε=10⁻³`。AdamW 优化器，学习率从 0.0002 经余弦衰减降至 0.000001；旋转/翻转数据增强；采用渐进式学习策略以省时。
- **模型变体**：AST-T（C=16，N2=[2,2,2,2]，N3=2）、AST-B（C=32，N2=[1,2,8,8]，N3=2）；带 "+" 表示使用几何自集成（self-ensemble）策略。
- **与已有方法的差异**：用平方 ReLU 替换 softmax 实现稀疏（不像 DRSformer 依赖参数 K）；不靠复杂组件放松稀疏，而用直接的双分支结构解决信息损失；FRFN 沿通道维度做"增强-缓解"，与 ASSA 的空间去冗余互补。

## 实验

- **任务与数据集**（三类退化）：
    - **雨条纹去除**：SPAD [78]。
    - **雨滴去除**：AGAN-Data [58]。
    - **真实雾去除**：Dense-Haze [1]。
- **对比方法**（十余种 CNN/Transformer）：去雨上对比 15 种 SOTA（DDN、RESCAN、PReNet、RCDNet、SPDNet、SPAIR、DualGCN、SEIDNet、MPRNet、Fu et al.、Restormer、SCD-Former、IDT、Uformer、DRSformer）；去雨滴对比 AttenGAN、Uformer、IDT、MAXIM-2S、AWRCP 等；去雾对比 DCP、FFA-Net、Restormer、DeHamer、MB-TaylorFormer-B 等。
- **评价指标**：PSNR、SSIM；去雨任务在 YCbCr 空间的 Y 通道计算 PSNR/SSIM；另用非参考指标 NIQE。
- **主实验结果**（提取缓存覆盖的表 1/2/3，单位 dB）：
    - **去雨条纹**（表 1 SPAD）：AST-B **49.51 / 0.9942**，AST-B+ **49.72 / 0.9944**；优于 DRSformer（48.53 / 0.9924）约 1 dB、Uformer（47.84）。论文称相对此前最佳 **CNN** 方法 PSNR 提升 **4.48 dB**。
    - **去雨滴**（表 2 AGAN-Data，论文表注为"模型效率分析"）：AST-B **32.32 / 0.935**，AST-B+ **32.45 / 0.937**；优于 AWRCP（31.93）、MAXIM-2S（31.87 / 0.935）、AttenGAN（31.59）。
    - **真实去雾**（表 3 Dense-Haze）：AST-B **17.12 / 0.55**，AST-B+ **17.27 / 0.57**；优于 MB-TaylorFormer-B（16.66 / 0.56）、DeHamer（16.62 / 0.56）、Restormer（15.78 / 0.55）。
- **定性结果**：图 3 在 SPAD 上与 SPDNet、Restormer、DRSformer 做去雨视觉对比。
- **消融实验**：论文称提供了大量消融以突出各设计贡献，但具体消融表格在提取缓存（截断于第 4.2 节中途）覆盖范围之外，本笔记未列出具体数据。
- **速度/参数量/FLOPs**：提取文本截断处之前未出现 AST 各变体的具体参数量、FLOPs 或推理速度数据（表 2 标题称"模型效率分析"但缓存仅含其 PSNR/SSIM 列）。

## 局限

- **效率证据不全**：提取缓存（前约 25000 字符，止于第 4.2 节）未含参数量/FLOPs/速度的量化对比，无法核实 AST 相对 Restormer 等的真实效率；双分支（SSA+DSA）并行计算理论上会带来额外开销。
- **任务范围**：实验仅覆盖去雨条纹/去雾/去雨滴三类低级视觉任务，未在去模糊、超分等更广任务或更高分辨率上验证，泛化边界尚不清晰。
- **窗口依赖**：注意力在 `M×M`（默认 8）窗口内计算，对超出窗口的极远距离依赖建模能力受限（虽有 bottleneck 阶段缓解）。
- **稀疏权重行为**：`w1/w2` 由 `a1,a2`（初值 1）学习得到，论文（在缓存覆盖部分）未给出不同任务下学到的权重分布或对初始化敏感性的分析。
- **复现细节**：缓存内可见关键超参（窗口=8、C/N2/N3、学习率），但消融配置、各任务训练 patch 大小/迭代数等完整复现细节在截断之外。

## 个人评论

1.  **稀疏 vs 密集的"既要又要"**：ASSA 没有在稀疏/密集间二选一，而是用一个仅含两个标量参数（`a1,a2`）的极轻量自适应门控把两分支融合，思路简洁却切中"过度稀疏丢信息、密集引噪声"的痛点，是很值得借鉴的注意力设计范式。
2.  **空间-通道解耦去冗余**：把"无关交互（空间）"与"特征冗余（通道）"显式拆成 ASSA 与 FRFN 两个模块分别处理，这种对冗余问题多维度解耦的工程思路具有普适启发性。
3.  **FRFN 的工程性价比**：PConv 增强 + DWConv 门控的"增强-缓解"FFN 实现简单、引入局部性，是可移植到其他视觉骨干的即插即用组件。
4.  **一个值得追问的点**：编码器刻意省略注意力（理由是自注意力的低通特性妨碍早期局部模式学习）是个有意思的设计取舍，但论文需要更强的消融来支撑该决定，缓存内未见相关证据。

### 使用建议

- **快速了解**：读 Abstract、Introduction、Fig. 1（标准 Transformer vs AST 工作流对比）、Fig. 2（总体架构）以及表 1/2/3 的关键数字。
- **复现**：精读 Section 3（3.1 整体流水线 + 3.2 AST Block，公式 1–8）与 4.1 Implementation Details（窗口=8、C/N2/N3、AdamW + 余弦衰减 + 渐进式学习）。
- **借鉴创新点**：改注意力→学 ASSA 双分支与融合公式 6/7；改 FFN→学 FRFN 的增强-缓解与门控公式 8。
- **写 Related Work**：可归入"图像恢复中的高效/稀疏注意力 Transformer"，与 Restormer（通道注意力）、Uformer/SwinIR（窗口注意力）、GRL（窗口+通道）、DRSformer（Top-K）、CODE（超像素）并列对比。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文（CVPR 2024，南开大学 + 南京理工，标题"Adapt or Perish"）属于计算机视觉**图像恢复**（Image Restoration）方向，解决从退化图像（雨条纹/雾/雨滴）恢复清晰图像的问题。其核心创新是两个可即插即用的注意力/前馈算子——自适应稀疏自注意力（ASSA）与特征精炼前馈网络（FRFN），并据此搭建完整恢复模型 AST。因此放在 **"B_注意力算子模块"** 主题下最贴切（它本质是注意力算子模块创新，而非通用去噪/去雨方法本身）。

## 2. 一句话总结
AST 用"稀疏分支（平方 ReLU）+ 密集分支（softmax）"的双分支自适应自注意力（ASSA）在空间域过滤噪声交互、用"增强-缓解"前馈网络（FRFN）在通道域去冗余，在去雨条纹/去雾/去雨滴三任务上达到有竞争力的性能（如 SPAD 49.51 dB）。

## 3. 背景与问题
- **CNN 的短板**：卷积感受野有限，难建模长距离依赖；Transformer 用自注意力补足，但原始自注意力二次复杂度高，难上高分辨率。
- **已有高效注意力的两个症结**：① 密集注意力在无关区域引入噪声交互；② 密集聚合的特征图含冗余信息，阻碍关注信息性特征。
- **去冗余尝试的不足**：DRSformer 的 Top-K 参数 K 对任务敏感；CODE 的超像素自注意力仍涉及全部 token。平方 ReLU 可无参实现稀疏，但过度稀疏丢信息、需额外设计放松——与稀疏初衷矛盾。
- **核心矛盾**：在保证足够信息流的同时去掉噪声交互与冗余，且对任务不敏感。

## 4. 核心贡献
1. 提出高效 Transformer 模型 AST，促进最有用信息前向流动。
2. ASSA 块（DSA 密集分支 + SSA 稀疏分支，自适应权重融合），自适应捕获信息性交互同时保留必要信息。
3. FRFN（基于特征变换的增强-缓解方案，沿通道去冗余）；并提供全面实验与消融。

## 5. 方法详解
- **整体（图 2）**：`I→Conv→F0`，经 N1=4 阶段对称编解码得 `Fd`，再 `Conv` 出残差 `R`，`Î=I+R`。编码器基本块**只含 FRFN**（省注意力，因自注意力低通特性妨碍早期局部模式学习）；解码器基本块含 **ASSA + FRFN**；解码器前有 bottleneck 阶段。
- **ASSA**：窗口（默认 8）内计算。`Q=XW_Q,K=XW_K,V=XW_V`；通用式 `A=f(QKᵀ/√d+B)V`（B 为可学习相对位置偏置）。
  - DSA（式 4）= `Softmax(QKᵀ/√d+B)`；SSA（式 5）= `ReLU²(QKᵀ/√d+B)`。
  - 融合（式 6）`A=(w1·SSA+w2·DSA)V`，`wn=e^{an}/Σe^{ai}`（式 7，`a1,a2` 初值 1）。
- **FRFN（式 8）**：`X̂'=GELU(W1·PConv(X̂))` 增强 → 切分 `[X̂'1,X̂'2]` → `X̂'r=X̂'1⊗F(DWConv(R(X̂'2)))` 门控缓解 → `X̂'out=GELU(W2·X̂'r)`。⊗ 为矩阵乘，R/F 为 Reshape/Flatten 引入局部性，PConv 部分卷积、DWConv 深度卷积。
- **训练**：Charbonnier 损失（式 1，ε=10⁻³），AdamW，学习率 0.0002→0.000001 余弦衰减，旋转/翻转增强，渐进式学习。
- **变体**：AST-T（C=16, N2=[2,2,2,2], N3=2）、AST-B（C=32, N2=[1,2,8,8], N3=2）；"+"=几何自集成。

## 6. 实验与结果
- **数据集**：SPAD（去雨条纹）、AGAN-Data（去雨滴）、Dense-Haze（真实去雾）。
- **指标**：PSNR/SSIM（去雨在 YCbCr 的 Y 通道）+ 非参考 NIQE。
- **主结果**：
  - SPAD（表 1）：AST-B **49.51/0.9942**，AST-B+ 49.72/0.9944；DRSformer 48.53/0.9924，Uformer 47.84。论文称相对最佳 CNN 方法 PSNR +4.48 dB。
  - AGAN-Data（表 2）：AST-B **32.32/0.935**，AST-B+ 32.45/0.937；AWRCP 31.93，MAXIM-2S 31.87/0.935。
  - Dense-Haze（表 3）：AST-B **17.12/0.55**，AST-B+ 17.27/0.57；MB-TaylorFormer-B 16.66/0.56，DeHamer 16.62/0.56，Restormer 15.78/0.55。
- **定性**：图 3 SPAD 去雨视觉对比（vs SPDNet/Restormer/DRSformer）。
- **消融 / FLOPs / 速度 / 参数量**：在提取缓存（止于第 4.2 节）覆盖范围之外，具体数据未在本笔记核实。

## 7. 这篇论文真正有价值的地方
1. **双分支自适应稀疏注意力**：用两个标量参数自适应平衡 SSA/DSA，绕开"稀疏丢信息 vs 密集引噪声"的两难，方法极简且通用。
2. **空间-通道解耦去冗余**：ASSA 管空间、FRFN 管通道，对冗余问题的多维度解耦设计有普适启发。
3. **FRFN 的工程性价比**：PConv 增强 + DWConv 门控，实现简单、引入局部性，易移植。

## 8. 局限与问题
- 效率证据（参数量/FLOPs/速度）在缓存截断之外，无法核实；双分支并行有额外开销之虞。
- 仅验证去雨/雾/雨滴三类低级任务，未及去模糊/超分等更广任务。
- 注意力受窗口（默认 8）大小限制，极远依赖建模有限。
- 学到的 `w1/w2` 分布与初始化敏感性缺少（缓存内可见的）分析。
- 编码器省略注意力的取舍需更强消融支撑（缓存内未见）。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Intro + Fig.1/Fig.2 + 表 1/2/3。
- **复现**：Section 3（公式 1–8）+ 4.1（窗口=8、C/N2/N3、AdamW+余弦+渐进式学习）。
- **借鉴**：改注意力学 ASSA（式 6/7）；改 FFN 学 FRFN（式 8）。
- **写 Related Work**：归入"图像恢复的高效/稀疏注意力 Transformer"，与 Restormer/Uformer/SwinIR/GRL/DRSformer/CODE 对比。

## 10. 和其他论文的关系
- 与 [[Restormer]]（通道注意力）、[[Uformer]]（窗口注意力、AST 多处沿用其设计）、SwinIR（移位窗口）、GRL（窗口+通道）、[[DRSformer]]（Top-K 通道选择）、CODE（超像素投影）等高效注意力工作有直接对比与演进关系。
- 稀疏分支借鉴平方 ReLU（squared ReLU）激活的稀疏注意力思路，与稀疏 Transformer 研究相关；FRFN 借用 PConv（[5]）与 DWConv 的局部性思想。

## 11. 关键词
自适应稀疏 Transformer (AST), 自适应稀疏自注意力 (ASSA), 稀疏/密集双分支自注意力 (SSA/DSA), 特征精炼前馈网络 (FRFN), 增强-缓解 (enhance-and-ease), 平方 ReLU 稀疏注意力, 图像恢复, 去雨条纹/去雾/去雨滴, 部分卷积 (PConv)

## 12. 可信度说明
本精读基于提取缓存（标称 12/12 页，但实际文本在 25000 字符处截断于第 4.2 节"去雨条纹"中途）。覆盖到的内容（摘要、引言、相关工作、完整方法 Section 3 含公式 1–8、实验设置 4.1、表 1/2/3 的全部数值、图 1–3 说明）均严格据提取文本核对，PSNR/SSIM 数字与公式逐一引用自原文。**截断之外**的信息（消融表格、各变体 FLOPs/参数量/速度、NIQE 具体数值、后续任务定量表）已明确标注"缓存覆盖范围之外/未核实"，未据原笔记臆测补全。摘要已从乱码直提（混入了 Fig.1 轴标签如 "MSA FFN"）重建为清理后的英文原文 + 中文翻译。

---

> **可信度补充**: PDF 提取质量 = **medium**（标称 2086 字符/页、12/12 页，但提取缓存实际在 25000 字符处截断，止于第 4.2 节，方法 Section 3 完整、实验仅含表 1/2/3 与设置，消融/效率数据未覆盖）；来源缓存: `.paper-cache/extracts/ASSA&FRFN.txt`；生成日期: 2026-06-05；模式: LLM (mimo-v2.5-pro)；本轮据提取文本重核并修正标题/摘要/数值/分类。
<!-- AI_READING_NOTE_END -->
