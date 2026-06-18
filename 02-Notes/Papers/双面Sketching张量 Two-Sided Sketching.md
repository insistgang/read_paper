---
title: An Efficient Two-Sided Sketching Method
authors:
  - "Zhiguang Cheng"
  - "Gaohang Yu"
  - "Xiaohao Cai"
  - "Liqun Qi"
year: 2024
venue: "arXiv"
doi: 
pdf: [[双面Sketching张量 Two-Sided Sketching.pdf]]
primary_topic: N_雷达_无线电_张量_数学
topics:
  - "N_雷达_无线电_张量_数学"
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
extract_cache: .paper-cache/extracts/双面Sketching张量 Two-Sided Sketching.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/37 pages"
---
# An Efficient Two-Sided Sketching Method

## 基本信息
- **PDF**: [[双面Sketching张量 Two-Sided Sketching.pdf]]
- **primary_topic**: `N_雷达_无线电_张量_数学`
- **topics**: `N_雷达_无线电_张量_数学`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | An Efficient Two-Sided Sketching Method for Large-Scale Tensor Decomposition Based on Transformed Domains |
| **作者** | Zhiguang Cheng; Gaohang Yu; Xiaohao Cai; Liqun Qi |
| **发表时间** | 2024-09-26 (arXiv:2404.16580v4) |
| **刊物/会议** | arXiv (math.OC); 标注 "Submitted to the editors" |
| **DOI** | 未明确 (arXiv ID: 2404.16580) |
| **MSC codes** | 68Q25, 68R10, 68U05 |

## 摘要

清理后的英文原摘要（修复了 PDF 提取中的断词与空格）：

> Large tensors are frequently encountered in various fields such as computer vision, scientific simulations, sensor networks, and data mining. However, these tensors are often too large for convenient processing, transfer, or storage. Fortunately, they typically exhibit a low-rank structure that can be leveraged through tensor decomposition. However, performing large-scale tensor decomposition can be time-consuming. Sketching is a useful technique to reduce the dimensionality of the data. In this paper, we propose a novel two-sided sketching method based on the ⋆L-product decomposition and transformed domains like the discrete cosine transformation. A rigorous theoretical analysis is also conducted to assess the approximation error of the proposed method. Specifically, we improve our method with power iteration to achieve more precise approximate solutions. Extensive numerical experiments and comparisons on low-rank approximation of synthetic large tensors and real-world data like color images and grayscale videos illustrate the efficiency and effectiveness of the proposed approach in terms of both CPU time and approximation accuracy.

中文翻译：

> 大规模张量频繁出现在计算机视觉、科学仿真、传感器网络和数据挖掘等领域。然而这些张量往往过于庞大，不便于处理、传输或存储。幸运的是它们通常具有低秩结构，可以通过张量分解加以利用。但对大规模张量做分解相当耗时。Sketching（概要化）是一种有效的降维技术。本文提出一种新颖的双面 Sketching 方法，它基于 ⋆L-乘积分解与变换域（如离散余弦变换 DCT）。论文还进行了严格的理论分析以评估所提方法的近似误差。具体而言，我们用幂迭代（power iteration）改进了方法，以获得更精确的近似解。在合成大张量以及彩色图像、灰度视频等真实数据上的大量数值实验与对比表明，所提方法在 CPU 时间和近似精度两方面都高效且有效。
>
> **关键词**（原文 Key words）：大规模张量、张量分解、sketching、t-product、离散余弦变换、幂迭代。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **这篇论文为什么要做**：视频、高光谱图像、多线性信号、通信网络等高维数据常用张量表示，且通常具有低秩结构，可由张量分解近似（Introduction, p.2）。但对大规模数据计算张量分解通常计算量极大，因此"高效地求出大规模数据的精确近似"在张量数据分析中至关重要。Sketching 利用随机投影或采样来近似原始数据，虽然会略微降低近似精度，但能显著降低计算与存储复杂度（p.2，文献 [11]）。
- **之前方法有什么问题**：(1) 已有大量基于 CP、Tucker、Tensor-Train (TT) 分解的随机化张量近似算法（Introduction 第 2-4 段大量综述，p.2-3）。(2) 在基于 t-product 的方向上，Qi 和 Yu [22] 提出了基于 t-product 的张量 sketching 方法以快速得到低管秩近似，但如 Kernfeld 等人 [37] 指出，t-product 对**实数张量**存在缺陷：其实现与基于 t-product 的分解需要中间的**复数运算**，即使利用傅里叶域的复对称性，也比实数运算更昂贵（p.2 末段, p.6）。(3) Qi 和 Yu [22] 的双面张量 sketching 仅考虑输入张量的 range 与 co-range，未利用"核心 sketch (core sketch)"来改进估计（p.9）。
- **作者想解决的核心矛盾**：在大规模张量低管秩近似中，如何在**保持理论误差保证与近似精度**的前提下，**降低分解的计算时间**。作者的思路是改用 ⋆L-乘积（可选 DCT 等实数变换）以规避复数运算，并引入核心 sketch 改进估计精度。
## 关键贡献

> 据 Introduction "main contributions" 段落（p.3）整理为四点。

1.  **提出基于变换域的新双面 Sketching 方法**：能显著提升 T-Sketch 与 rt-SVD 方法用于低管秩近似的计算效率（p.3）。该方法被命名为 L-TRP-SKETCH（L Transformed Randomized Projection Sketching，算法 1，p.10）。
2.  **建立低管秩近似模型并扩展到张量**：基于 ⋆L-乘积分解建立低管秩张量近似模型，并将 Tropp 等人 [34] 提出的矩阵双面 sketching 算法结合子空间幂迭代扩展到张量情形（p.3）。
3.  **进行严格的理论误差分析**：对所提双面 sketching 方法的近似误差进行了严格的理论评估（p.3；定理在第 4 节，提取缓存仅覆盖到 p.12，定理正文据原文后续页，提取缓存未覆盖, 待核）。
4.  **广泛的数值验证**：在不同模态的大张量（合成大张量、彩色图像、灰度视频）上做了大量实验与对比，从 CPU 时间和近似精度两方面验证了方法的高效与有效（p.3）。

> 注：原笔记将"幂迭代扩展"单列为第 5 条贡献。按原文 main contributions 段落，幂迭代是第 3 节的方法扩展（3.3 Extension），并非并列的第 5 条贡献，故此处合并说明：论文另以 DCT-Gaussian-Sketch-PI（算法 2，p.12）为例展示了幂迭代扩展。
## 方法

**整体框架**：用四个张量 sketching 算子 `Υ ∈ R^{k×m×p}`, `Ω ∈ R^{k×n×p}`, `Φ ∈ R^{s×m×p}`, `Ψ ∈ R^{s×n×p}`（公式 2.13）对输入张量 `A ∈ R^{m×n×p}` 做随机投影，得到三个 sketch：`X`（捕获 co-range）、`Y`（捕获 range）、`Z`（核心 sketch，携带改进奇异值/奇异向量估计的新信息）。随后通过三步过程重构出目标管秩为 `k` 的近似 `Â`。

**输入输出**：
- **输入**：原始张量 `A ∈ R^{m×n×p}`，目标管秩 `k`，核心 sketch 尺寸参数 `s`（满足 `k ≤ s`），（幂迭代版本）迭代次数 `q`。
- **输出**：`A` 的管秩为 `k` 的近似张量 `Â`，以及因子 `(Q, C, P)`。

**关键预备（第 2 节）**：
- **⋆L-乘积**：`Z = X ⋆L Y = L^H[fold(block(X̄_L) block(Ȳ_L))]`（定义 2.1，公式 2.4），其中 `L` 为任意可逆线性变换，沿第三维对所有 tube 作用。t-product 是其取 `L = F_{n3}`（DFT）时的特例（p.6，由块循环矩阵可被 DFT 对角化推出）。
- **变换张量 SVD**：`A = U ⋆L S ⋆L V^H`（定理 2.5，公式 2.7）；变换管秩 = `S` 非零奇异 tube 的个数（公式 2.8）。
- **张量 sketching 算子**：由三种矩阵 sketching 技术生成——高斯投影、SRHT（subsampled randomized Hadamard transform）、Count Sketch（第 2.2 节，附录 A 给伪代码）。

**三步重构过程（公式 3.14-3.21）**：
1.  **生成随机 sketch**：`X := Υ ⋆L A ∈ R^{k×n×p}`（捕获 co-range，公式 3.14）、`Y := A ⋆L Ω^H ∈ R^{m×k×p}`（捕获 range，公式 3.15）、`Z := Φ ⋆L A ⋆L Ψ^H ∈ R^{s×s×p}`（核心 sketch，公式 3.16）。
2.  **步骤 (I)：L-正交三角分解**。对 `X^H` 与 `Y` 做 QR 分解：`X^H := P ⋆L R1`, `Y := Q ⋆L R2`（公式 3.17）。其中 `P ∈ R^{n×k×p}`、`Q ∈ R^{m×k×p}` 是部分正交张量，`R1, R2 ∈ R^{k×k×p}` 是 f-upper 三角张量。`P, Q` 近似张成 `A` 的 co-range 与 range。
3.  **步骤 (II)：计算核心近似**。`C := (Φ ⋆L Q)^† ⋆L Z ⋆L ((Ψ ⋆L P)^†)^H ∈ R^{k×k×p}`（公式 3.18）。等价于求解基于 ⋆L-乘积的最小二乘问题 `min_C ½‖G ⋆L C ⋆L M^H − Z‖_F²`，其中 `G = Φ ⋆L Q`、`M = Ψ ⋆L P`（公式 3.19）；由 Lemma 2.3，该问题在变换域逐切片求解（公式 3.20）。
4.  **步骤 (III)：构造最终近似**。`Â := Q ⋆L C ⋆L P^H`（公式 3.21）。

**数学机制的直观解释（3.2 Principle）**：理想分解为 `A ≈ Q ⋆L (Q^H ⋆L A ⋆L P) ⋆L P^H`（公式 3.22），但核心张量 `Q^H ⋆L A ⋆L P` 不能由线性 sketch 直接算出（因为 `P, Q` 本身是 `A` 的函数）。于是用核心 sketch 估计：`Z = Φ ⋆L A ⋆L Ψ^H ≈ (Φ ⋆L Q) ⋆L (Q^H ⋆L A ⋆L P) ⋆L (P^H ⋆L Ψ^H)`（公式 3.23），把外侧矩阵移到左边即得 `C ≈ Q^H ⋆L A ⋆L P`（公式 3.24）。最终 `A ≈ Q ⋆L C ⋆L P^H = Â`（公式 3.25），误差取决于 `A` 的最优管秩 `k` 近似误差。

**与已有方法的差异**：相比仅用 range/co-range sketch 的 Qi 和 Yu [22] 方法，本文**引入核心 sketch `Z`**，带来对变换张量奇异值/奇异向量更好的估计，是性能提升的关键（p.9 开头）。相比基于 t-product（DFT，复数运算）的方法，本文用 ⋆L-乘积（可选 DCT 等实数变换）规避实数张量分解中的中间复数运算开销（p.2, p.6）。

**存储成本**：sketch `(X,Y,Z)` 的存储为 `p(nk+mk+s²)` 浮点数；算法 1 对原始数据 `A` 的存储复杂度为 `O(mkp+nkp+kkp)` 浮点数（p.10）。

**变换 L 的选择**：除 DFT 矩阵 `F_{n3}`（此处 `n3 = p`）与 DCT 矩阵 `C` 外，还可选 U 变换矩阵——将 `A` 沿 mode-3 展开为矩阵 `W ∈ R^{p×mn}`，对 `W` 做 SVD 得到酉变换矩阵 `U ∈ R^{p×p}`（p.10-11）。据此命名出 U-/DFT-/DCT- 与 -Count-/-Gaussian-/-SRHT-Sketch 等一系列算法；不指定变换域时统称 L-…-Sketch（p.11，Naming 段）。

**幂迭代扩展（3.3 Extension，算法 2 DCT-Gaussian-Sketch-PI）**：对奇异值衰减慢的张量，构造辅助张量 `B = (A ⋆L A^H)^q ⋆L A`（`q` 为非负整数），对 `B` 而非 `A` 做 sketching。由变换张量 SVD `A = U ⋆L S ⋆L V^H`，可得 `B = U ⋆L S^{2q+1} ⋆L V^H`（公式 3.26），即 `B` 的变换张量奇异值衰减更快，从而改善近似。实现上不显式构造 `B`，而是在变换域逐切片交替把 `A`、`A^H` 投影到当前 `Q`、`P` 上并重做 QR（算法 2 第 8-14 行）。
## 实验

> 提取缓存仅覆盖 p.1-12（即第 5 节实验之前）。以下"数据/指标"信息综合自摘要、引言，以及笔记下方"全文补读记录"对 p.13-37 的章节线索；具体数值据原文后续页，提取缓存未覆盖, 待核。

- **使用的数据集**：合成大张量、真实世界彩色图像、灰度视频（摘要 + Introduction 贡献段，p.3）。具体数据集名称在提取缓存（p.1-12）中未给出。
- **对比方法**：据补读线索（p.15），对比包括 rt-SVD、T-Sketch、truncated-t-SVD，以及本文不同变换域版本（如 DFT-Gaussian-Sketch、DCT-Gaussian-Sketch）。具体对比集合据原文后续页，提取缓存未覆盖, 待核。
- **评价指标**：相对误差（relative error）、CPU 时间、峰值信噪比 PSNR（ρ_psnr）（据补读线索 p.14-15）。
- **实验结构**：第 5 节分 5.1 合成实验（含 5.1.1 关于变换域的实验、5.1.2 关于张量 sketching 算子的实验）等小节（补读线索 p.14-15）。
- **主实验结论（定性）**：据补读线索（p.15），在不同变换域下本文双面 sketching 方法的精度均超过 rt-SVD 与 T-Sketch；对快速衰减谱的输入张量，本文方法在精度上仅次于 truncated-t-SVD，但 CPU 时间更优。具体数值据原文后续页，提取缓存未覆盖, 待核。
- **效率信息**：sketch 存储 `p(nk+mk+s²)` 浮点数；算法 1 存储复杂度 `O(mkp+nkp+kkp)`（p.10）。
## 局限

- **假设依赖**：方法面向"低管秩 / 近似低管秩（尾部能量 τ_j² 较小）"的张量（尾部能量定义见 2.7、命题 2.8）。秩不低时优势可能不明显。
- **参数选择**：需用户指定目标管秩 `k`、核心 sketch 尺寸 `s`（要求 `k ≤ s`）、（幂迭代时）迭代次数 `q`，可能需先验或调参。
- **线性变换的选择**：提供 DFT、DCT、U 三种 `L`，但最优变换可能依赖数据，文中未讨论自适应选择。
- **应用场景**：聚焦低管秩近似任务；是否适用于回归、优化等其他张量计算任务文中未涉及。
- **复现风险**：涉及多种张量算子与变换，需注意变换域中共轭转置定义、逐切片 `qr` 实现等细节。第 4 节定理证明与第 5 节实验数值在提取缓存（p.1-12）中未覆盖。
## 个人评论

> 本节为 AI 评论，非论文原文。

这篇论文最值得学习之处在于：把矩阵双面 sketching（Tropp 等人）系统地扩展到张量域，并通过两处设计取得效率/精度平衡——(1) 用 ⋆L-乘积 + 实数变换（DCT/U）替代 t-product 的 DFT，规避实数数据上的中间复数运算；(2) 在 range/co-range sketch 之外引入核心 sketch `Z`，用一次额外随机投影换取更准的核心张量估计。对后续研究的启发：

1.  **变换域分治**：把张量分解化为变换域中逐 frontal slice 的矩阵运算（QR + 最小二乘），这种"先变换、再逐片处理、最后逆变换"的范式可迁移到其他高维数据问题。
2.  **理论 + 实践**：不仅给算法，还配套误差界分析（第 4 节，提取缓存未覆盖），严谨性值得借鉴。
3.  **可插拔设计**：变换 `L`（DFT/DCT/U）与随机投影算子（Gaussian/SRHT/Count）可自由组合，命名体系清晰，便于按场景定制。
4.  **幂迭代加速谱衰减**：用 `S^{2q+1}` 加快谱衰减是随机化低秩近似的通用技巧，可借鉴到其他随机算法。

可改进/存疑：变换 `L` 的最优选择缺乏自适应准则；核心 sketch 尺寸 `s` 与精度/成本的权衡在前 12 页未量化（实验细节在提取缓存外）。

### 使用建议

- **如果快速了解**：读摘要、引言后半（贡献与组织结构）、第 3.1 节算法 1 描述。
- **如果复现**：精读第 3 节算法 1（L-TRP-SKETCH）与算法 2（DCT-Gaussian-Sketch-PI）伪代码，结合第 2 节对 ⋆L-乘积、变换张量 SVD、张量 sketching 算子的定义；附录 A（三种矩阵 sketching 技术）、附录 B（理论保证）需参考。
- **如果借鉴创新点**：学习"变换域逐切片处理"框架，以及"引入核心 sketch 改进估计"的策略；幂迭代是提升随机化低秩近似精度的通用技巧。
- **如果写 related work**：可归入"随机化张量分解"、"基于 sketching 的张量近似"或"基于 t-product / ⋆L-乘积及其变体的计算"。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[N_雷达_无线电_张量_数学]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**随机化数值线性代数 / 张量计算**方向，核心解决**大规模张量低管秩分解计算耗时**的问题。做法是在 ⋆L-乘积（Kernfeld-Kilmer 变换张量框架，文献 [37]）与可逆线性变换（DFT/DCT/U）之下，设计**双面张量 sketching** 算法，高效求大规模张量的低管秩近似，并辅以幂迭代提升精度、配套误差界分析。论文标注 math.OC，MSC 68Q25/68R10/68U05。可归类于"张量分解与近似 / 随机化降维"。

## 2. 一句话总结
本文提出基于变换域（DCT 等）和 ⋆L-乘积的**双面张量 sketching 方法 L-TRP-SKETCH**：在 range/co-range sketch 之外引入**核心 sketch**，通过变换域逐切片的 QR + 最小二乘重构低管秩近似，并用幂迭代加速谱衰减；在合成张量、彩色图像、灰度视频上于 CPU 时间与精度两方面优于 rt-SVD、T-Sketch。

## 3. 背景与问题
- **为什么要做**：视频、高光谱图像、多线性信号、通信网络等高维数据常以低秩张量表示（Introduction, p.2），但大规模张量分解计算量大。Sketching 用随机投影/采样降维，虽略损精度却能大幅降低计算与存储成本（文献 [11]）。
- **之前方法的问题**：(1) Qi 和 Yu [22] 的 t-product sketching 对**实数张量**需中间复数运算，比实数运算更昂贵（Kernfeld 等 [37] 指出，p.2, p.6）。(2) 其双面 sketching 仅用 range/co-range，未用核心 sketch 改进估计（p.9）。
- **核心矛盾**：在保证理论误差界与精度的同时降低计算时间。作者用 ⋆L-乘积（可选实数变换）+ 核心 sketch 来同时改善效率与精度。

## 4. 核心贡献
1.  **基于变换域的新双面 sketching 方法（L-TRP-SKETCH，算法 1）**：显著提升 T-Sketch 与 rt-SVD 的计算效率（p.3, p.10）。
2.  **低管秩近似模型 + 张量化扩展**：基于 ⋆L-乘积建立低管秩近似模型，将 Tropp 等 [34] 的矩阵双面 sketching 结合子空间幂迭代扩展到张量（p.3, p.12）。
3.  **严格误差分析**：对所提方法近似误差给出理论评估（第 4 节；定理正文据原文后续页，提取缓存未覆盖, 待核）。
4.  **广泛数值验证**：在合成大张量、彩色图像、灰度视频上从 CPU 时间与精度两方面验证（p.3）。
> 幂迭代扩展（DCT-Gaussian-Sketch-PI，算法 2）作为第 3.3 节方法扩展给出，原文 main contributions 未将其单列为并列贡献。

## 5. 方法详解
**整体框架**：四个 sketching 算子 `Υ(k×m×p), Ω(k×n×p), Φ(s×m×p), Ψ(s×n×p)`（公式 2.13，由 Gaussian/SRHT/Count 三种矩阵 sketching 生成）对 `A ∈ R^{m×n×p}` 投影，得 `X`（co-range）、`Y`（range）、`Z`（核心）三个 sketch，再三步重构出管秩 `k` 近似 `Â`。

**输入输出**：输入 `A`、目标管秩 `k`、核心 sketch 尺寸 `s`（`k ≤ s`）、（PI 版本）`q`；输出 `Â` 及因子 `(Q, C, P)`。

**三步过程（公式 3.14-3.21）**：
1.  生成 sketch：`X := Υ ⋆L A ∈ R^{k×n×p}`（3.14）、`Y := A ⋆L Ω^H ∈ R^{m×k×p}`（3.15）、`Z := Φ ⋆L A ⋆L Ψ^H ∈ R^{s×s×p}`（3.16）。
2.  步骤 (I) L-正交三角分解：`X^H := P ⋆L R1`, `Y := Q ⋆L R2`（3.17），`P(n×k×p)`、`Q(m×k×p)` 部分正交，`R1,R2(k×k×p)` 为 f-upper 三角。
3.  步骤 (II) 核心近似：`C := (Φ ⋆L Q)^† ⋆L Z ⋆L ((Ψ ⋆L P)^†)^H ∈ R^{k×k×p}`（3.18），等价于 ⋆L-最小二乘 `min_C ½‖G ⋆L C ⋆L M^H − Z‖_F²`（`G=Φ⋆LQ, M=Ψ⋆LP`，3.19），在变换域逐切片解 `C̄_L^{(i)} = (Ḡ_L^{(i)})^† Z̄_L^{(i)} ((M̄_L^{(i)})^†)^H`（3.20）。
4.  步骤 (III) 构造近似：`Â := Q ⋆L C ⋆L P^H`（3.21）。

**原理（3.2）**：理想 `A ≈ Q ⋆L (Q^H ⋆L A ⋆L P) ⋆L P^H`（3.22），核心 `Q^H ⋆L A ⋆L P` 不能由线性 sketch 直接得（`P,Q` 是 `A` 的函数），故由核心 sketch 估计 `Z ≈ (Φ⋆LQ)(Q^H⋆LA⋆LP)(P^H⋆LΨ^H)`（3.23），移项得 `C ≈ Q^H ⋆L A ⋆L P`（3.24），最终 `A ≈ Q ⋆L C ⋆L P^H = Â`（3.25），误差取决于最优管秩 `k` 近似误差。

**与已有方法差异**：相比 Qi 和 Yu [22]（仅 range/co-range）多了**核心 sketch `Z`**，改进奇异值/向量估计（p.9）；相比 t-product（DFT 复数运算）用 ⋆L-乘积（DCT/U 实数变换）规避中间复数运算（p.2, p.6）。

**复杂度**：sketch 存储 `p(nk+mk+s²)`；算法 1 存储复杂度 `O(mkp+nkp+kkp)`（p.10）。

**变换 L**：DFT `F_{n3}`、DCT `C`，或 U 变换（`A` mode-3 展开为 `W ∈ R^{p×mn}` 后 SVD 取酉阵 `U ∈ R^{p×p}`）（p.10-11）。

**幂迭代扩展（3.3，算法 2）**：构造 `B = (A ⋆L A^H)^q ⋆L A`，由 `A = U ⋆L S ⋆L V^H` 得 `B = U ⋆L S^{2q+1} ⋆L V^H`（3.26），谱衰减更快；实现上在变换域逐切片交替投影 `A`、`A^H` 到 `Q`、`P` 并重做 QR（算法 2 第 8-14 行），不显式构造 `B`。

## 6. 实验与结果
> 提取缓存覆盖 p.1-12（第 5 节实验之前）。以下结合摘要/引言与笔记"全文补读记录"对 p.13-37 的线索；具体数值据原文后续页，提取缓存未覆盖, 待核。
- **数据集**：合成大张量、彩色图像、灰度视频（p.3）；具体名称提取缓存内未给出。
- **对比方法**：据补读线索（p.15）含 rt-SVD、T-Sketch、truncated-t-SVD 及本文各变换域版本（DFT-/DCT-Gaussian-Sketch 等）。
- **评价指标**：相对误差、CPU 时间、PSNR（据补读线索 p.14-15）。
- **结构**：第 5 节含 5.1 合成实验（5.1.1 变换域对比、5.1.2 sketching 算子对比）等。
- **定性结论**：据补读线索（p.15），各变换域下本文方法精度均超过 rt-SVD 与 T-Sketch；对快速衰减谱输入，精度仅次于 truncated-t-SVD，但 CPU 时间更优。具体数字待核。
- **效率**：sketch 存储 `p(nk+mk+s²)`，算法 1 存储复杂度 `O(mkp+nkp+kkp)`（p.10）。

## 7. 这篇论文真正有价值的地方
1.  **变换域分治范式**：把张量分解化为变换域逐 frontal slice 的矩阵 QR + 最小二乘，"变换→逐片→逆变换"可迁移到其他高维问题。
2.  **理论结合实践**：算法 + 误差界分析（第 4 节，提取缓存未覆盖）。
3.  **可插拔灵活性**：变换 `L`（DFT/DCT/U）× 随机算子（Gaussian/SRHT/Count）自由组合，命名体系清晰。
4.  **实数张量优化**：用 DCT/U 实数变换规避 t-product 的中间复数运算，对图像等实数大数据有实际意义。

## 8. 局限与问题
- **假设依赖**：面向低管秩 / 近似低管秩（尾部能量 τ_j² 小，定义 2.7、命题 2.8）的张量。
- **参数选择**：需指定 `k`、`s`（`k ≤ s`）、`q`。
- **变换选择**：DFT/DCT/U 最优者依赖数据，自适应选择未讨论。
- **应用范围**：聚焦低管秩近似，回归/优化等任务未涉及。
- **复现风险**：变换域共轭转置定义、逐切片 `qr` 等细节需谨慎；第 4 节证明与第 5 节数值在提取缓存外。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言后半（贡献/组织）+ 第 3.1 节算法 1。
- **复现**：精读算法 1、算法 2 伪代码，结合第 2 节定义（⋆L-乘积、变换张量 SVD、sketching 算子）、附录 A/B。
- **借鉴创新点**：学"变换域逐切片处理"框架 + "核心 sketch 改进估计"策略；幂迭代为通用加速技巧。
- **写 related work**：归入"随机化张量分解" / "基于 sketching 的张量近似" / "t-product 与 ⋆L-乘积变体计算"。

## 10. 和其他论文的关系
- `[[Tropp et al. Two-Sided Matrix Sketching]]`（文献 [33, 34]）：本文的张量双面 sketching 是对 Tropp 等矩阵双面 sketching 算法的张量扩展（结合子空间幂迭代）（p.2-3, p.12）。
- `[[Qi and Yu t-product Tensor Sketch]]`（文献 [22]）：本文是对其改进——用 ⋆L-乘积替代 t-product 并引入核心 sketch，提升效率与精度（p.2, p.9）。
- `[[Kernfeld et al. star-L product]]`（文献 [37]）：本文采用的 ⋆L-乘积变换张量框架来源于此，以规避 t-product 在实数域的复数运算（p.2, p.6）。
> 上述链接名按提取文本中的引用关系拟定，文献编号据正文方括号引用；引用论文确切标题在提取缓存内未完整给出，待核。

## 11. 关键词
大规模张量、张量分解、sketching、低管秩近似、⋆L-乘积、变换域、离散余弦变换 (DCT)、t-product、核心 sketch、双面投影、幂迭代、CPU 时间。（前 7 项 + t-product + 幂迭代为原文 Key words，余为本笔记补充）

## 12. 可信度说明
本精读笔记的**方法、贡献、算法伪代码、复杂度与原理推导均严格基于提取文本 p.1-12**（即第 1-3 节，公式 2.1-3.26、算法 1-2），事实可核。**第 4 节误差界定理、第 5 节实验全部数值、附录 A/B 内容不在提取缓存（p.1-12）内**；这部分的对比方法、指标、定性结论来自笔记"全文补读记录"对 p.13-37 的章节线索（系 AI 补读，非提取缓存逐字文本），相应处已标注"据原文后续页，提取缓存未覆盖, 待核"。提取文本质量良好（约 2077 字符/页），公式与算法清晰。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本 p.1-12 质量好, 约 2077 字符/页; 方法与原理部分可逐字核对); 提取缓存仅含 p.1-12, 实验/定理数值据补读线索待核; 来源缓存: `.paper-cache/extracts/双面Sketching张量 Two-Sided Sketching.txt` (缓存 12/37 页; 笔记补读线索覆盖 p.13-37); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-37; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-37。
- **提取情况**: 缺失页 25 页, 其中 25 页提取到可读文本。缺失页包含正文/附录内容, 其中约 4 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 4 Theoretical Analysis
- p.13: The error bound of the proposed two-sided sketching algorithms is given in Theorems
- p.14: 5 Numerical Experiments
- p.14: This section showcases numerical experiments validating the efficiency and effectiveness
- p.14: 5.1 Synthetic Experiments
- p.15: 5.1.1 Experiments Regarding the Transformed Domains
- p.15: We first examine the performance of different transformed domains in our two-sided
- p.15: Sketch, and DFT-Gaussian-Sketch algorithms) in terms of the relative error, CPU
- p.15: As shown in the second row of Figure 1, our two-sided sketching method with
- p.15: It is worth highlighting that, for input tensors exhibiting a fast decay spectrum, our
- p.15: method is the second only to the truncated-t-SVD algorithm in terms of accuracy, but
- p.15: 5.1.2 Experiments Regarding the Tensor Sketching Operators

### 缺失页关键摘录

- p.14: ratio (PSNR) ρpsnrare used as metrics of the low-rank approximation ˆAto the input
- p.15: error, CPU time, and PSNR, as the size of the sketch parameter kvaries; see more
- p.15: sketching method. Figure 1 shows the results of different methods and our method
- p.15: time, and PSNR. Figure 1 illustrates that among our two-sided Gaussian sketching
- p.15: of the relative error and PSNR. Regarding the CPU time, our DCT-Gaussian-Sketch
- p.15: As shown in the second row of Figure 1, our two-sided sketching method with
- p.15: different transformed domains all surpasses the accuracy of the rt-SVD and T-Sketch
- p.15: different transformed domains provides superior accuracy in low-rank approximations.
- p.15: method is the second only to the truncated-t-SVD algorithm in terms of accuracy, but
- p.15: than our method (see the middle plot of the second column of Figure 1).
- p.15: transformed domain. Figure 2 shows the results of different methods and our method
- p.16: CPU time ( middle column), and PSNR ( right column). In particular, the first row is
<!-- AI_READING_NOTE_END -->
