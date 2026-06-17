---
title: "Practical Sketching Algorithms for Low-Rank Tucker Approximation of Large Tensors"
authors:
  - "Wandi Dong"
  - "Gaohang Yu"
  - "Liqun Qi"
  - "Xiaohao Cai"
year: 2023
venue: "Journal of Scientific Computing"
doi: 10.1007/s10915-023-02172-y
pdf: [[Tucker近似 Tucker Approximation.pdf]]
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
extract_cache: .paper-cache/extracts/Tucker近似 Tucker Approximation.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/26 pages"
---
# Practical Sketching Algorithms for Low-Rank Tucker Approximation of Large Tensors

## 基本信息
- **PDF**: [[Tucker近似 Tucker Approximation.pdf]]
- **primary_topic**: `N_雷达_无线电_张量_数学`
- **topics**: `N_雷达_无线电_张量_数学`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Practical Sketching Algorithms for Low-Rank Tucker Approximation of Large Tensors |
| **作者** | Wandi Dong; Gaohang Yu; Liqun Qi; Xiaohao Cai |
| **发表时间** | 2023 (收稿 2022-10-24; 接收 2023-02-28; 在线 2023-03-29) |
| **刊物/会议** | Journal of Scientific Computing (2023) 95:52 |
| **DOI** | 10.1007/s10915-023-02172-y |
| **MSC 分类** | 68W20, 15A18, 15A69 |
| **作者单位** | 杭州电子科技大学数学系; 华为理论研究实验室 (香港); 南安普顿大学电子与计算机学院 |

## 摘要

> **英文原摘要（据 PDF 提取文本整理，修复空格/连字符）**：
> Low-rank approximation of tensors has been widely used in high-dimensional data analysis. It usually involves singular value decomposition (SVD) of large-scale matrices with high computational complexity. Sketching is an effective data compression and dimensionality reduction technique applied to the low-rank approximation of large matrices. This paper presents two practical randomized algorithms for low-rank Tucker approximation of large tensors based on sketching and power scheme, with a rigorous error-bound analysis. Numerical experiments on synthetic and real-world tensor data demonstrate the competitive performance of the proposed algorithms.

> **中文翻译**：
> 张量的低秩近似在高维数据分析中已被广泛使用。它通常涉及对大规模矩阵做奇异值分解（SVD），计算复杂度很高。Sketching（草图化）是一种应用于大矩阵低秩近似的有效数据压缩与降维技术。本文提出两种实用的随机化算法，基于 sketching 与幂方案（power scheme）来计算大规模张量的低秩 Tucker 近似，并给出严格的误差界分析。在合成数据与真实世界张量数据上的数值实验表明，所提算法具有有竞争力的性能。
>
> **关键词**：张量 sketching、随机化算法、Tucker 分解、子空间幂迭代、高维数据。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

*   **这篇论文为什么要做**：在科学计算、机器学习、信号/图像处理、数据挖掘等领域，高维数据（论文举例：彩色图像、高光谱图像、视频）常表现出低秩结构。张量低秩近似已成为压缩与近似高维数据的通用工具。常见的张量分解模型包括 CP 分解、Tucker 分解、Hierarchical Tucker (HT) 与 Tensor Train (TT)；本文聚焦 **低秩 Tucker 分解（即张量的低多线性秩近似）**。当目标秩远小于原始维度时，Tucker 分解有很好的压缩效果。
*   **之前方法有什么问题**：最常用的非迭代算法是 THOSVD（截断高阶 SVD）和 STHOSVD（顺序截断高阶 SVD）。它们结果通常次优，但可作 HOOI 等迭代法的初值。问题在于：两者在计算中间矩阵奇异向量时**直接依赖 SVD**，张量规模大时内存需求大、计算复杂度高。随机化算法（如 Minster 等人提出的 R-THOSVD / R-STHOSVD）用随机投影降低了 SVD 规模，但其底层 R-SVD 采用**单侧随机投影**，当模式展开矩阵 `G(n)` 的**两个维度都很大**时计算成本依然高昂。
*   **作者想解决的核心矛盾**：如何在**保持（甚至提升）近似精度**的前提下，**进一步降低**大规模张量 Tucker 近似的**计算复杂度**，并让算法对任意数据张量都能快速收敛、**不依赖奇异值间隔（gap）**。
## 关键贡献

论文在引言中明确给出三点主要贡献：
1.  提出了一种新的**单趟（one-pass）sketching 算法 Sketch-STHOSVD（算法 6）**，用于低秩 Tucker 近似，可显著提升经典 STHOSVD 的计算效率。
2.  提出了一种新的**矩阵 sketching 算法（算法 7，sub-Sketch）**：将 Tropp 等人提出的**双侧 sketching 算法**与**子空间幂迭代**相结合，能准确且高效地计算大规模矩阵的低秩近似。
3.  在此基础上提出改进的 **sub-Sketch-STHOSVD（算法 8）**：通过结合子空间幂迭代，比更简单的随机化算法产生**更精确**的 Tucker 近似；更重要的是，它对任意数据张量都能**快速收敛**且**独立于奇异值间隔**。
## 方法

*   **整体框架**：核心思想是用对大矩阵/张量做随机线性投影（sketching）得到的"草图"来近似原数据，从而在小得多的规模上做 SVD/QR 等运算，最终得到原数据的低秩近似。整个过程沿处理顺序 `sp` **顺序处理张量的各个模式（mode）**，每处理完一个模式立即更新核心张量（继承 STHOSVD 的思路）。
*   **输入输出**：
    *   **输入**：N 阶张量 `X ∈ R^{I1×...×IN}`，目标 Tucker 秩 `(r1,...,rN)`，处理顺序 `sp:{i1,...,iN}`，sketch 尺寸参数 `{l1,...,lN}`（算法 6/8；算法 8 另需幂迭代次数 `q`）。
    *   **输出**：Tucker 近似 `X̂ = G ×1 U(1) ×2 U(2) ... ×N U(N)`，其中 `U(n)` 是因子矩阵、`G` 是核心张量。
*   **关键模块**：
    1.  **双侧 sketching（算法 5，Sketch for low-rank approximation）**：基础模块。对矩阵 `A∈R^{m×n}`，固定两个独立标准正态矩阵 `Ω∈R^{n×k}`、`Ψ∈R^{l×m}`（尺寸需满足 `r≤k≤min{l,n}, 0<l≤m`），先对 `Ω`、`Ψ^T` 做正交化（orth）以获得更小误差和更好数值稳定性；再得两份草图 `Y=AΩ`（压缩列信息）、`W=ΨA`（压缩行信息）；对 `Y` 做 thinQR 得正交基 `Q`；最后解线性系统 `X=(ΨQ)†W`，从而 `A ≈ QX`（秩-k 近似）。`A` 稠密时算术成本约 `O((k+l)mn + kl(m+n))` flops。其次优误差界由定理 3（引自 Tropp 等人，需 `l>k+1`）给出，且该界**自动利用尾能量 τ 的衰减**。
    2.  **子空间幂迭代（算法 7，sub-Sketch）**：增强模块。原始矩阵很大或奇异谱衰减缓慢时，算法 5 可能给出较差的基。借鉴 Halko 等人的幂迭代思想，用 `(AA^T)^q A` 代替 `A`。由 `A=USV^T` 可得 `(AA^T)^q A = U S^{2q+1} V^T`：左右奇异向量不变，但奇异值衰减更快、尾能量更小。直接幂迭代会因舍入误差丢失小奇异模信息，故算法 7 在**每次交替应用 `A` 与 `A^T` 之间插入 thinQR 正交化**。`A` 稠密时成本约 `O((q+1)(k+l)mn + kl(m+n))` flops；论文指出取 `q=1` 或 `2` 通常即可获得好的近似。
*   **模块连接与流程**：
    *   **Sketch-STHOSVD（算法 6）**：流程同 STHOSVD，初始化 `G←X`，依处理顺序逐模式处理。处理第 `n` 个模式时，对当前中间核张量的模式-n 展开矩阵 `G(n)` 调用**算法 5** 得 `(Q,X)`：令 `U(n)←Q`，再 `G←fold_n(X)` 折叠回更新后的核张量。
    *   **sub-Sketch-STHOSVD（算法 8）**：与算法 6 流程一致，唯一区别是处理每个 `G(n)` 时改调用**算法 7**（带子空间幂迭代）来计算低秩近似。
*   **理论分析**：
    *   定理 1/2 给出 THOSVD、STHOSVD 的经典误差界，二者误差界相同（均 `≤ Σ_n Δ²_n(X) ≤ N·||X−X̂_opt||²_F`），但 STHOSVD 计算量与存储更省。
    *   **定理 4（本文核心）**：Sketch-STHOSVD 的期望误差界 `E||X−X̂||²_F ≤ Σ_n [r_n/(l_n−r_n−1)] · min_{ρ_n<r_n−1}[r_n/(r_n−ρ_n−1)] · Δ²_n(X) ≤ (同式)·||X−X̂_opt||²_F`。证明思路是**组合定理 2（STHOSVD 误差按模式逐项分解）与定理 3（单矩阵 sketching 误差界）**。
*   **复杂度对比（表 2）**：以稠密张量、`r_j ≪ I_j` 为前提，列出 THOSVD、STHOSVD、R-STHOSVD、Sketch-STHOSVD 在一般张量 `R^{I1×...×IN}` 与立方张量 `R^{I×...×I}` 两种情形下的算术成本表达式（理论 flops 量级，非实测）。
*   **与已有方法的差异**：
    *   vs **R-STHOSVD**：后者底层 R-SVD 用**单侧**随机投影，`G(n)` 两维都大时投影成本高；本文用**双侧 sketching**，更高效处理两维都大的情形。
    *   vs **基础 Sketch-STHOSVD**：sub-Sketch-STHOSVD 加入**子空间幂迭代**，对奇异值衰减缓慢的矩阵显著提升精度与收敛速度，且不依赖奇异值 gap。
*   **论文类型特化**：属**数值线性代数/算法**论文，核心创新是**算法设计 + 严格误差界分析**，而非网络结构或特定下游任务，为大规模数据处理提供底层计算工具。
## 实验

> 提取缓存仅覆盖 PDF 前 12 页（第 5 节实验在 p.13 起），下列实验细节据原文后续页（p.13-26）的章节线索与摘录，**提取缓存未覆盖，待核**。

*   **使用的数据集（据原文后续页, 提取缓存未覆盖, 待核）**：
    *   **合成稠密张量**：Hilbert 张量，规模 `500×500×500`（表 4 随目标秩增大比较相对误差与运行时间）。
    *   **稀疏张量**：第 5.2 节 "Sparse Tensor" 在稀疏张量 `X` 上测试，并研究奇异值 gap 增大→尾能量减小→精度提升的规律（图 2 一带），另含加噪实验（噪声在 gap 小时更明显影响精度，但不改变无噪情形的结论）。
    *   **真实世界张量**：第 5.3 节 "Real-World Data Tensor" 用彩色图像 "HDU picture"，规模 `1200×1800×3`，目标秩 `(500,500,3)`，以 PSNR 与 CPU 时间评价（图 4，括号内如 (2.62; 40.61) 分别为 CPU 时间与 PSNR）。
*   **对比方法（据原文后续页, 提取缓存未覆盖, 待核）**：THOSVD、STHOSVD、R-STHOSVD，以及本文 Sketch-STHOSVD、sub-Sketch-STHOSVD（见 p.13 表头）。
*   **评价指标**：相对误差（相对 Frobenius 范数误差）、CPU 运行时间；真实图像实验另用 **PSNR**。
*   **主要结论（据原文后续页, 提取缓存未覆盖, 待核）**：随机化算法精度高于确定性算法；**Sketch-STHOSVD 最快**，**sub-Sketch-STHOSVD 高效地取得最高精度**；随 gap 参数 γ 增大，sub-Sketch-STHOSVD 可在与 R-STHOSVD 相当的 CPU 时间内逼近 THOSVD/STHOSVD 的精度。原文 p.18 小结称数值结果显示 sub-Sketch-STHOSVD 的优越性。
*   **复杂度信息**：表 2 仅给各算法**理论**算术成本对比，非实验实测 FLOPs。
## 局限

1.  **参数选择**：性能依赖 sketch 尺寸 `{l_n}`、`{k_n}` 与幂迭代次数 `q`。文中有理论指导（如定理 3 要求 `l>k+1`，建议 `q=1` 或 `2`），但实践中如何对不同数据自动选最优参数仍是挑战。
2.  **计算开销**：子空间幂迭代（算法 7）引入多次矩阵乘法，`q` 较大或矩阵很大时累积开销需权衡。
3.  **假设依赖**：误差界基于随机测试矩阵为标准高斯/标准正态分布等理想假设；非高斯数据或特定结构对性能的影响文中未详细探讨。
4.  **实验范围（基于提取缓存覆盖范围的判断，原文 p.13-26 实验需进一步核对）**：缓存内未见实测数字；据后续页线索，实验集中在 Hilbert/稀疏合成张量与单张彩色图像，对更高阶张量（N 很大）与更广泛真实大规模数据集的系统验证有限。
## 个人评论

1.  **实用的算法框架**：论文给出清晰、可直接实现的算法伪代码（算法 1-8），把随机化数值线代的思想转化为可落地工具，复现门槛低。
2.  **严谨的理论分析**：为 Sketch-STHOSVD 给出严格期望误差界（定理 4），并通过"STHOSVD 逐模式分解 + 单矩阵 sketching 界"的组合把张量误差归约到矩阵情形，将误差与经典最优解误差、尾能量关联，论证链条干净。
3.  **关键技术结合**："双侧 sketching + 子空间幂迭代 + 交替正交化"这一组合，是在两维都大、奇异谱衰减慢时同时稳住精度与效率的有效手段，借鉴价值高。
4.  **清晰的演进脉络**：THOSVD → STHOSVD → R-STHOSVD → Sketch-STHOSVD → sub-Sketch-STHOSVD，展示了如何通过随机化与迭代增强一步步优化同一问题，方法论对研究者有启发。
5.  **可改进处**：核心实验数字位于提取缓存未覆盖的后续页，本笔记对实验的判断尚待核对原文图表；且论文未深入讨论非高斯草图、超高阶张量与自适应选秩。

### 使用建议

*   **如果快速了解**：读**摘要**、**引言最后一段（三点贡献）** 与**第 6 节结论**。
*   **如果复现**：精读第 3、4 节，吃透**算法 5（基础 sketching）、算法 7（子空间幂迭代 sketching）及算法 6/8**；表 2 复杂度分析有助评估成本；注意基础算法 R-SVD（算法 3）、STHOSVD（算法 2）。
*   **如果借鉴创新点**：学习**"双侧 sketching + 子空间幂迭代"组合机制**，以及**如何把随机化矩阵近似系统集成进 STHOSVD 框架**；定理 4 的"逐模式归约"证明思路值得参考。
*   **如果写 related work**：归入 **"随机化张量分解 (Randomized Tensor Decomposition)"** 与 **"基于 sketching 的低秩近似 (Sketching-based Low-Rank Approximation)"** 两条脉络。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[N_雷达_无线电_张量_数学]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**数值线性代数**与**张量计算**领域，具体是**随机化算法（sketching + 子空间幂迭代）在张量低秩 Tucker 近似中的应用**。它解决**大规模张量 Tucker 分解（低多线性秩近似）** 计算复杂度过高的问题，适用于"张量计算""大规模数据分析""随机化数值线性代数"等主题。MSC 分类 68W20（算法）、15A18（特征值/奇异值）、15A69（多线性代数/张量）也印证了这一定位。

## 2. 一句话总结
论文提出两种实用随机化算法——单趟双侧 sketching 的 Sketch-STHOSVD 与叠加子空间幂迭代的 sub-Sketch-STHOSVD——用于高效准确地计算大规模张量的低秩 Tucker 近似，并给出以定理 4 为核心的严格误差界。

## 3. 背景与问题
*   **为什么要做**：高维数据（彩色图像、高光谱图像、视频）常具低秩结构，张量低秩近似是其压缩/表示的通用工具。但 THOSVD、STHOSVD 等确定性算法直接依赖大矩阵 SVD，张量大时内存与计算复杂度高。
*   **之前方法的问题**：R-STHOSVD 用随机投影降低 SVD 规模，但底层 R-SVD 是**单侧投影**，当模式展开矩阵 `G(n)` 两维都大时成本仍高。
*   **核心矛盾**：在**保持/提升精度**的同时**进一步降低复杂度**，并做到对任意数据张量**快速收敛、独立于奇异值 gap**。

## 4. 核心贡献
1.  单趟 sketching 算法 **Sketch-STHOSVD（算法 6）**，显著提升 STHOSVD 效率。
2.  新矩阵 sketching 算法 **算法 7（sub-Sketch）**：Tropp 双侧 sketching + 子空间幂迭代，准确高效近似大矩阵。
3.  改进的 **sub-Sketch-STHOSVD（算法 8）**：比简单随机化算法更精确，快速收敛且独立于奇异值间隔。

## 5. 方法详解
*   **整体框架**：用随机线性投影（sketching）的"草图"在小规模上做 SVD/QR，沿处理顺序 `sp` 逐模式处理张量并即时更新核张量（继承 STHOSVD）。
*   **输入输出**：输入张量 `X`、目标秩 `(r1..rN)`、处理顺序 `sp`、sketch 尺寸 `{l1..lN}`（算法 8 另需 `q`）；输出 `X̂ = G ×1 U(1) ... ×N U(N)`。
*   **算法 5（双侧 sketching）**：固定标准正态 `Ω∈R^{n×k}`、`Ψ∈R^{l×m}`（`r≤k≤min{l,n}, 0<l≤m`），正交化后取 `Y=AΩ`、`W=ΨA`，`Q=thinQR(Y)`，`X=(ΨQ)†W`，得 `A≈QX`。成本 `O((k+l)mn+kl(m+n))`，误差由定理 3（`l>k+1`）保证并自动利用尾能量衰减。
*   **算法 7（子空间幂迭代）**：用 `(AA^T)^q A = U S^{2q+1} V^T` 加速奇异值衰减、压低尾能量；为防舍入误差丢失小奇异模，在每次交替应用 `A` 与 `A^T` 间插入 thinQR 正交化。成本 `O((q+1)(k+l)mn+kl(m+n))`，`q=1`/`2` 通常足够。
*   **算法 6 vs 8**：流程相同（`G←X`，逐模式对 `G(n)` 求低秩近似，`U(n)←Q`，`G←fold_n(X)`），区别仅在调用算法 5 还是算法 7。
*   **误差界**：定理 4 由定理 2（STHOSVD 逐模式分解）+ 定理 3（单矩阵 sketching 界）组合证得，期望误差 `E||X−X̂||²_F ≤ Σ_n [r_n/(l_n−r_n−1)]·min[r_n/(r_n−ρ_n−1)]·Δ²_n(X)`。
*   **复杂度**：表 2 给 THOSVD/STHOSVD/R-STHOSVD/Sketch-STHOSVD 在一般张量与立方张量下的理论算术成本。

## 6. 实验与结果
> 提取缓存仅到 p.12；以下据原文 p.13-26 的章节线索与摘录，**提取缓存未覆盖，待核**。
*   **合成稠密**：Hilbert 张量 `500×500×500`（表 4，随目标秩增大比较相对误差与时间）。
*   **稀疏张量**（5.2 节）：研究奇异值 gap 增大→尾能量减小→精度提升，并做加噪鲁棒性实验。
*   **真实图像**（5.3 节）：HDU 彩色图像 `1200×1800×3`，目标秩 `(500,500,3)`，以 PSNR 与 CPU 时间评价（图 4）。
*   **结论**：随机化算法精度高于确定性算法；Sketch-STHOSVD 最快，sub-Sketch-STHOSVD 高效取得最高精度，且随 γ 增大可在与 R-STHOSVD 相当时间内逼近 THOSVD/STHOSVD 精度。

## 7. 这篇论文真正有价值的地方
1.  **可落地的算法框架**：算法 1-8 伪代码完整，复现门槛低。
2.  **严谨的误差界**：定理 4 把张量误差归约到矩阵 sketching 界，与最优解误差、尾能量挂钩。
3.  **关键技术组合**："双侧 sketching + 子空间幂迭代 + 交替正交化"在两维都大、奇异谱衰减慢时兼顾精度与效率。
4.  **清晰演进脉络**：THOSVD→STHOSVD→R-STHOSVD→Sketch-STHOSVD→sub-Sketch-STHOSVD。

## 8. 局限与问题
1.  **参数选择**：`{l_n}`、`{k_n}`、`q` 的自动调优在实践中是挑战（理论上 `l>k+1`，`q=1/2`）。
2.  **计算开销**：幂迭代引入多次矩阵乘，`q` 大或矩阵大时需权衡。
3.  **假设依赖**：误差界依赖标准高斯/正态草图等理想假设。
4.  **实验范围**：据后续页线索，实验集中在合成张量与单张彩色图像，高阶张量与广泛真实数据的系统验证有限（待核原文图表）。

## 9. 我该怎么使用这篇论文
*   **快速了解**：摘要 + 引言三点贡献 + 第 6 节结论。
*   **复现**：精读第 3、4 节，吃透算法 5/6/7/8，参考表 2 复杂度与基础算法 R-SVD/STHOSVD。
*   **借鉴创新**：学"双侧 sketching + 子空间幂迭代"组合与"集成进 STHOSVD"的做法；参考定理 4 的逐模式归约证明。
*   **写 related work**：归入"随机化张量分解"与"基于 sketching 的低秩近似"两条脉络。

## 10. 和其他论文的关系
*   随机化 Tucker 分解的相关工作：Zhou 等人的随机化 HOOI、Che 与 Wei 的自适应随机化算法、Minster 等人的 R-THOSVD/R-STHOSVD、Sun 等人的单趟随机化算法（论文引言 [12–20] 综述）。
*   矩阵/张量 sketching 基础工作：Tropp 等人的双侧 sketching（本文算法 5/7 的出发点）、Halko 等人的随机化 SVD 与幂迭代。
*   经典确定性基线：Vannieuwenhoven 等人的 STHOSVD、THOSVD/HOSVD、HOOI。
*   竞争性分解模型：CP、Hierarchical Tucker、Tensor Train。
（上述链接均来自论文引用与正文，具体笔记是否存在于本库需另行核对。）

## 11. 关键词
张量 sketching, 随机化算法, Tucker 分解, 子空间幂迭代, 高维数据, 低秩近似, 双侧草图, STHOSVD, 误差界, 数值线性代数

## 12. 可信度说明
本精读主要基于 PDF 提取缓存的**前 12 页**：覆盖摘要、引言、预备知识（符号/定义/THOSVD/STHOSVD/R-STHOSVD）、第 3 节（算法 5/6 与定理 3/4 及证明）、第 4 节（算法 7/8）。这些足以支撑对论文定位、背景、贡献、方法原理与理论分析的完整、准确理解。
**提取质量评估**：前 12 页文本清晰连贯，含定义、定理、算法伪代码与公式（约 2086 字符/页），素材质量高；但数学公式经 OCR 后部分符号断裂，已据上下文还原。
**主要信息缺失**：第 5 节实验（p.13-26）、第 6 节结论、参考文献列表未进入提取缓存。本笔记"实验与结果"中的数据集名称、规模、目标秩、PSNR 等均来自原 AI 全文补读对 p.13-26 的页级摘录，**缓存未覆盖，标注待核**。

---

> **可信度补充**: PDF 提取质量 = **high** (前 12 页 2086 字符/页, 清晰连贯; 实验页 p.13-26 仅有页级线索, 实验数字待核); 来源缓存: `.paper-cache/extracts/Tucker近似 Tucker Approximation.txt` (缓存 12/26 页; 原 AI 主体 12/26 + 全文补读 13-26 页级摘录); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-26; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-26。
- **提取情况**: 缺失页 14 页, 其中 14 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Target rank THOSVD STHOSVD R-STHOSVD Sketch-STHOSVD Sub-Sketch-STHOSVD
- p.13: Bold values indicate the best results
- p.15: 5.2 Sparse Tensor
- p.17: 5.3 Real-World Data Tensor
- p.17: In this experiment, we test the performance of different algorithms on a colour image, called
- p.18: Firstly, we conduct an experiment on the HDU picture with target rank (500,500,3),a n d
- p.18: In summary, the numerical results show the superiority of the sub-sketch STHOSVD algo-
- p.23: 6 Conclusion
- p.23: Acknowledgements We would like to thank the anonymous referees for their comments and suggestions on
- p.24: Declarations
- p.24: Appendix
- p.24: F (24)

### 缺失页关键摘录

- p.14: Table 4 Results comparison in terms of the relative error (in second) on the Hilbert tensor with a size of 500 ×500×500 as the target rank increases
- p.15: respectively. The results show that the randomized algorithms can achieve higher accuracy
- p.15: than the deterministic algorithms. The proposed Sketch-STHOSVD algorithm is the fastest,and the sub-Sketch-STHOSVD algorithm achieves the highest accuracy efﬁciently.
- p.15: In this experiment, we test the performance of different algorithms on a sparse tensor X∈
- p.15: are tested. The increase of gap means that the tail energy will be reduced, and the accuracy ofthe algorithms will be improved. Our numerical experiments also veriﬁed this result. Figure 2
- p.15: and keep the rest parameters the same as the settings in the previous experiment. The relative
- p.16: noise indeed affects the accuracy of the low-rank approximation, especially when the gap is
- p.16: small. However, the inﬂuence of noise does not change the conclusion obtained on the casewithout noise. The accuracy of our sub-Sketch-STHOSVD algorithm is the highest amongthe randomized algorithms. As γincreases, sub-Sketch-STHOSVD can achieve almost the
- p.16: same accuracy as that of THOSVD and STHOSVD in a comparable CPU time against R-STHOSVD.
- p.17: In this experiment, we test the performance of different algorithms on a colour image, called
- p.18: Fig. 4 Results comparison on a HDU picture with a size of 1200 ×1800×3 in terms of PSNR (i.e., peak
- p.18: signal-to-noise ratio) and CPU time. The target rank is (500,500,3). The two values in e.g. (2.62; 40.61)represent the CPU time and the PSNR, respectively
<!-- AI_READING_NOTE_END -->
