---
title: "JournalofScientificComputing(2023)95:52"
authors:
  - "Wandi Dong"
  - "Gaohang Yu"
  - "Liqun Qi"
  - "Xiaohao Cai"
year: 2023
venue: "Electronics"
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
# JournalofScientificComputing(2023)95:52

## 基本信息
- **PDF**: [[Tucker近似 Tucker Approximation.pdf]]
- **primary_topic**: `N_雷达_无线电_张量_数学`
- **topics**: `N_雷达_无线电_张量_数学`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | JournalofScientificComputing(2023)95:52 |
| **作者** | Wandi Dong; Gaohang Yu; Liqun Qi; Xiaohao Cai |
| **发表时间** | 2023 |
| **刊物/会议** | Electronics |
| **DOI** | 10.1007/s10915-023-02172-y |

## 摘要

> Low-rank approximation of tensors has been widely used in high-dimensional data anal- ysis. It usually involves singular value decomposition (SVD) of large-scale matrices with highcomputationalcomplexity.Sketchingisaneffectivedatacompressionanddimension- ality reduction technique applied to the low-rank approximation of large matrices. This paperpresentstwopracticalrandomizedalgorithmsforlow-rankTuckerapproximationof largetensorsbasedonsketchingandpowerscheme,witharigorouserror-boundanalysis. Numericalexperimentsonsyntheticandreal-worldtensordatademonstratethecompetitive performanceoftheproposedalgorithms.

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

*   **这篇论文为什么要做**：在科学计算、机器学习等领域，高维数据（如图像、视频）常表现出低秩结构。张量低秩Tucker近似是压缩和表示此类数据的通用工具。然而，传统的确定性算法（如THOSVD、STHOSVD）核心步骤依赖于矩阵的奇异值分解（SVD），当处理的大规模张量维度很高时，直接SVD计算内存需求大、计算复杂度高。
*   **之前方法有什么问题**：经典的随机化算法（如R-STHOSVD）虽然通过随机投影降低了SVD的计算规模，但当模式展开矩阵的两个维度都很大时，其计算成本依然高昂。
*   **作者想解决的核心矛盾**：如何在**保持（甚至提升）近似精度**的前提下，**进一步大幅降低**大规模张量Tucker近似的**计算复杂度**，使其更适用于实际的大规模数据处理。
## 关键贡献

论文的主要贡献有三点：
1.  提出了一种新的**单趟sketching算法（Sketch-STHOSVD，算法6）**，用于低秩Tucker近似，可以显著提升经典STHOSVD算法的计算效率。
2.  设计了一种新的**矩阵sketching算法（算法7）**。该算法将Troop等人提出的双侧sketching算法与子空间幂迭代相结合，能够更准确、高效地计算大规模矩阵的低秩近似。
3.  在此基础上，提出了一种改进的**sub-Sketch-STHOSVD算法（算法8）**。该算法通过结合子空间幂迭代，能够比更简单的随机化算法产生更精确的Tucker近似，并且能快速收敛，且不依赖于奇异值的间隔。
## 方法

*   **整体框架**：本文方法基于一个核心思想：用对原始大矩阵/张量进行随机线性投影（sketching）得到的“草图”来近似原数据，从而在小得多的规模上进行SVD等运算，最终得到原数据的低秩近似。整个过程是顺序处理张量的各个模式（mode）。
*   **输入输出**：
    *   **输入**：N阶张量 `X`，目标Tucker秩 `(r1, r2, ..., rN)`，处理顺序 `sp`，以及sketch尺寸参数 `{l1, l2, ..., lN}`（对于算法6/8）。
    *   **输出**：Tucker近似 `X_hat = G ×1 U(1) ×2 U(2) ... ×N U(N)`，其中 `U(n)` 是因子矩阵，`G` 是核心张量。
*   **关键模块**：
    1.  **双侧sketching算法（算法5）**：这是基础模块。对于一个矩阵 `A`，它通过左乘随机矩阵 `Ψ` 和右乘随机矩阵 `Ω` 得到两个“草图” `W=ΨA` 和 `Y=AΩ`，然后从 `Y` 获得正交基 `Q`，最后通过求解一个线性系统得到近似 `X = (ΨQ)†W`，从而得到 `A ≈ QX`。
    2.  **子空间幂迭代（sub-Sketch，算法7）**：这是增强模块。为了处理奇异值衰减缓慢的矩阵，在算法5的基础上引入幂迭代。核心思想是用 `(A A^T)^q A` 代替 `A` 进行计算，这会加速奇异值的衰减，使得尾部能量更小，从而获得更精确的基。算法7在每次应用 `A` 和 `A^T` 之间都进行了正交化，以减少舍入误差。
*   **模块连接与流程**：
    *   **Sketch-STHOSVD (算法6)**：流程与经典STHOSVD类似，依次处理张量的每个模式。在处理第 `n` 个模式时，将当前中间核心张量 `G` 的模式-`n` 展开矩阵 `G(n)` 作为输入，调用**基础的双侧sketching算法（算法5）** 来计算其低秩近似 `QX`。其中 `Q` 成为第 `n` 个因子矩阵 `U(n)`，`X` 被重新折叠（fold）为更新后的核心张量。
    *   **sub-Sketch-STHOSVD (算法8)**：与算法6流程一致，唯一区别在于：在处理每个模式展开矩阵 `G(n)` 时，调用**增强的子空间幂迭代sketching算法（算法7）** 来计算其低秩近似。
*   **数学公式直观解释**：
    *   **sketching**：`Y = A Ω` 相当于用 `Ω` 的列对 `A` 的列进行随机线性组合，得到一个压缩了列信息的矩阵。`W = Ψ A` 是压缩行信息的矩阵。利用这两部分信息可以重建 `A` 的低秩近似。
    *   **幂迭代**：`(A A^T)^q A = U S^(2q+1) V^T`。与 `A = U S V^T` 相比，奇异值 `S` 被提升到了 `(2q+1)` 次方，这使得前 `r` 个大奇异值与后续小奇异值之间的差距被急剧放大，从而让基于随机投影的方法更容易捕捉到主要的奇异子空间。
*   **与已有方法的差异**：
    *   与 **R-STHOSVD** 相比：R-STHOSVD 使用单侧随机投影（R-SVD），当 `G(n)` 很大时投影计算成本高。本文的sketching算法使用**双侧投影**，能更高效地处理两个维度都很大的情况。
    *   与基础的 **Sketch-STHOSVD** 相比：**sub-Sketch-STHOSVD** 加入了**子空间幂迭代**，显著提升了对奇异值衰减缓慢的矩阵的近似精度和收敛速度。
*   **论文类型特化**：本文属于**数值方法/算法**论文，专注于张量分解。核心创新是**算法设计**和**理论分析**，而非网络结构或特定任务。它为大规模数据处理提供了一种底层计算工具。
## 实验

根据提供的PDF文本（前12页），实验部分（第5节）仅提及标题为“Numerical experiments on synthetic and real-world data tensors”，但具体实验细节尚未出现。
*   **使用的数据集**：文本中提到包括“合成数据（synthetic）”和“真实世界张量数据（real-world data tensors）”，但**PDF文本中未明确说明具体数据集名称**。
*   **对比方法**：根据引文和预备知识，预期对比方法包括 **THOSVD, STHOSVD, R-STHOSVD** 以及论文提出的新算法。
*   **评价指标**：预期包括**近似误差**（如相对Frobenius范数误差）和**计算效率**（如CPU运行时间）。
*   **主实验结果**：在提供的文本中，**未找到具体实验结果的数字**。
*   **消融实验/泛化实验/效率信息**：在提供的文本中，**未找到关于消融实验、泛化实验或具体效率（如FLOPs）的描述**。表2仅给出了各算法在理论上的一般算术成本比较，而非实验实测数据。
## 局限

1.  **参数选择**：算法性能依赖于sketch尺寸参数 `{l_n}` 和幂迭代次数 `q` 的选择。文中虽有理论指导（如定理3要求 `l > k+1`），但在实践中如何为不同数据自动选择最优参数，可能是一个挑战。
2.  **计算开销**：虽然新算法降低了总体复杂度，但子空间幂迭代（算法7）会引入多次矩阵乘法，当 `q` 较大或矩阵本身很大时，这些乘法的累积开销可能需要权衡。
3.  **假设依赖**：误差分析基于一些理想假设，如随机矩阵为标准高斯分布。在实际应用中，非高斯数据或特定数据结构可能影响算法性能，但文中未详细探讨。
4.  **实验范围**：在提供的文本片段中，未能看到在多样化的、极具挑战性的大规模真实数据集上的广泛验证，无法全面评估其实际优势。对于高阶张量（N很大）的性能表现，也未见详细讨论。
## 个人评论

1.  **实用的算法框架**：论文没有停留在理论，而是给出了清晰、可直接实现的算法伪代码（算法5-8），将复杂的数学思想转化为实用工具。
2.  **严谨的理论分析**：论文为所提出的算法（算法6）给出了严格的误差上界（定理4），并将误差与经典最优解的误差、尾部能量等关联起来，这为理解算法性能和参数选择提供了理论依据。
3.  **关键技术结合**：将“双侧sketching”与“子空间幂迭代”有机结合，并正交化以稳定计算，这个组合技是提升大规模矩阵低秩近似精度和效率的有效手段，具有很好的借鉴价值。
4.  **清晰的演进脉络**：从THOSVD -> STHOSVD -> R-STHOSVD -> Sketch-STHOSVD -> sub-Sketch-STHOSVD，论文展示了如何通过引入随机化和迭代增强，一步步优化同一问题，这种问题解决的思路对研究者非常有启发。

### 使用建议

*   **如果快速了解**：重点阅读**摘要（Abstract）**、**引言（Introduction）** 的最后一段（贡献总结）和**第6节结论（Conclusion）**。
*   **如果复现**：重点精读**第3节和第4节**，完全理解**算法5（基础sketching）、算法7（子空间幂迭代sketching）以及算法6和8**的步骤。注意参考文献中的基础算法（如R-SVD, STHOSVD）。表2的复杂度分析有助于评估计算成本。
*   **如果借鉴创新点**：应学习**“双侧sketching+子空间幂迭代”这一组合机制**，以及**如何将这种随机化矩阵近似算法系统地集成到张量分解框架（如STHOSVD）中**。误差分析的思路（定理4的证明）也值得参考。
*   **如果写related work**：可将本文归类到 **“随机化张量分解 (Randomized Tensor Decomposition)”** 和 **“基于sketching的低秩近似 (Sketching-based Low-Rank Approximation)”** 两个相关工作的脉络中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[N_雷达_无线电_张量_数学]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**数值线性代数**和**张量计算**领域，具体是**随机化算法在张量低秩近似中的应用**。它主要解决**大规模张量的Tucker分解（低多线性秩近似）** 中计算复杂度过高的问题。该论文适用于“**张量计算**”、“**大规模数据分析**”、“**随机化数值线性代数**”等主题。

## 2. 一句话总结
这篇论文提出了两种基于数据压缩（sketching）和子空间幂迭代的实用随机化算法，用于高效、准确地计算大规模张量的低秩Tucker近似，并给出了严格的误差界分析。

## 3. 背景与问题
*   **这篇论文为什么要做**：在科学计算、机器学习等领域，高维数据（如图像、视频）常表现出低秩结构。张量低秩Tucker近似是压缩和表示此类数据的通用工具。然而，传统的确定性算法（如THOSVD、STHOSVD）核心步骤依赖于矩阵的奇异值分解（SVD），当处理的大规模张量维度很高时，直接SVD计算内存需求大、计算复杂度高。
*   **之前方法有什么问题**：经典的随机化算法（如R-STHOSVD）虽然通过随机投影降低了SVD的计算规模，但当模式展开矩阵的两个维度都很大时，其计算成本依然高昂。
*   **作者想解决的核心矛盾**：如何在**保持（甚至提升）近似精度**的前提下，**进一步大幅降低**大规模张量Tucker近似的**计算复杂度**，使其更适用于实际的大规模数据处理。

## 4. 核心贡献
论文的主要贡献有三点：
1.  提出了一种新的**单趟sketching算法（Sketch-STHOSVD，算法6）**，用于低秩Tucker近似，可以显著提升经典STHOSVD算法的计算效率。
2.  设计了一种新的**矩阵sketching算法（算法7）**。该算法将Troop等人提出的双侧sketching算法与子空间幂迭代相结合，能够更准确、高效地计算大规模矩阵的低秩近似。
3.  在此基础上，提出了一种改进的**sub-Sketch-STHOSVD算法（算法8）**。该算法通过结合子空间幂迭代，能够比更简单的随机化算法产生更精确的Tucker近似，并且能快速收敛，且不依赖于奇异值的间隔。

## 5. 方法详解
*   **整体框架**：本文方法基于一个核心思想：用对原始大矩阵/张量进行随机线性投影（sketching）得到的“草图”来近似原数据，从而在小得多的规模上进行SVD等运算，最终得到原数据的低秩近似。整个过程是顺序处理张量的各个模式（mode）。
*   **输入输出**：
    *   **输入**：N阶张量 `X`，目标Tucker秩 `(r1, r2, ..., rN)`，处理顺序 `sp`，以及sketch尺寸参数 `{l1, l2, ..., lN}`（对于算法6/8）。
    *   **输出**：Tucker近似 `X_hat = G ×1 U(1) ×2 U(2) ... ×N U(N)`，其中 `U(n)` 是因子矩阵，`G` 是核心张量。
*   **关键模块**：
    1.  **双侧sketching算法（算法5）**：这是基础模块。对于一个矩阵 `A`，它通过左乘随机矩阵 `Ψ` 和右乘随机矩阵 `Ω` 得到两个“草图” `W=ΨA` 和 `Y=AΩ`，然后从 `Y` 获得正交基 `Q`，最后通过求解一个线性系统得到近似 `X = (ΨQ)†W`，从而得到 `A ≈ QX`。
    2.  **子空间幂迭代（sub-Sketch，算法7）**：这是增强模块。为了处理奇异值衰减缓慢的矩阵，在算法5的基础上引入幂迭代。核心思想是用 `(A A^T)^q A` 代替 `A` 进行计算，这会加速奇异值的衰减，使得尾部能量更小，从而获得更精确的基。算法7在每次应用 `A` 和 `A^T` 之间都进行了正交化，以减少舍入误差。
*   **模块连接与流程**：
    *   **Sketch-STHOSVD (算法6)**：流程与经典STHOSVD类似，依次处理张量的每个模式。在处理第 `n` 个模式时，将当前中间核心张量 `G` 的模式-`n` 展开矩阵 `G(n)` 作为输入，调用**基础的双侧sketching算法（算法5）** 来计算其低秩近似 `QX`。其中 `Q` 成为第 `n` 个因子矩阵 `U(n)`，`X` 被重新折叠（fold）为更新后的核心张量。
    *   **sub-Sketch-STHOSVD (算法8)**：与算法6流程一致，唯一区别在于：在处理每个模式展开矩阵 `G(n)` 时，调用**增强的子空间幂迭代sketching算法（算法7）** 来计算其低秩近似。
*   **数学公式直观解释**：
    *   **sketching**：`Y = A Ω` 相当于用 `Ω` 的列对 `A` 的列进行随机线性组合，得到一个压缩了列信息的矩阵。`W = Ψ A` 是压缩行信息的矩阵。利用这两部分信息可以重建 `A` 的低秩近似。
    *   **幂迭代**：`(A A^T)^q A = U S^(2q+1) V^T`。与 `A = U S V^T` 相比，奇异值 `S` 被提升到了 `(2q+1)` 次方，这使得前 `r` 个大奇异值与后续小奇异值之间的差距被急剧放大，从而让基于随机投影的方法更容易捕捉到主要的奇异子空间。
*   **与已有方法的差异**：
    *   与 **R-STHOSVD** 相比：R-STHOSVD 使用单侧随机投影（R-SVD），当 `G(n)` 很大时投影计算成本高。本文的sketching算法使用**双侧投影**，能更高效地处理两个维度都很大的情况。
    *   与基础的 **Sketch-STHOSVD** 相比：**sub-Sketch-STHOSVD** 加入了**子空间幂迭代**，显著提升了对奇异值衰减缓慢的矩阵的近似精度和收敛速度。
*   **论文类型特化**：本文属于**数值方法/算法**论文，专注于张量分解。核心创新是**算法设计**和**理论分析**，而非网络结构或特定任务。它为大规模数据处理提供了一种底层计算工具。

## 6. 实验与结果
根据提供的PDF文本（前12页），实验部分（第5节）仅提及标题为“Numerical experiments on synthetic and real-world data tensors”，但具体实验细节尚未出现。
*   **使用的数据集**：文本中提到包括“合成数据（synthetic）”和“真实世界张量数据（real-world data tensors）”，但**PDF文本中未明确说明具体数据集名称**。
*   **对比方法**：根据引文和预备知识，预期对比方法包括 **THOSVD, STHOSVD, R-STHOSVD** 以及论文提出的新算法。
*   **评价指标**：预期包括**近似误差**（如相对Frobenius范数误差）和**计算效率**（如CPU运行时间）。
*   **主实验结果**：在提供的文本中，**未找到具体实验结果的数字**。
*   **消融实验/泛化实验/效率信息**：在提供的文本中，**未找到关于消融实验、泛化实验或具体效率（如FLOPs）的描述**。表2仅给出了各算法在理论上的一般算术成本比较，而非实验实测数据。

## 7. 这篇论文真正有价值的地方
1.  **实用的算法框架**：论文没有停留在理论，而是给出了清晰、可直接实现的算法伪代码（算法5-8），将复杂的数学思想转化为实用工具。
2.  **严谨的理论分析**：论文为所提出的算法（算法6）给出了严格的误差上界（定理4），并将误差与经典最优解的误差、尾部能量等关联起来，这为理解算法性能和参数选择提供了理论依据。
3.  **关键技术结合**：将“双侧sketching”与“子空间幂迭代”有机结合，并正交化以稳定计算，这个组合技是提升大规模矩阵低秩近似精度和效率的有效手段，具有很好的借鉴价值。
4.  **清晰的演进脉络**：从THOSVD -> STHOSVD -> R-STHOSVD -> Sketch-STHOSVD -> sub-Sketch-STHOSVD，论文展示了如何通过引入随机化和迭代增强，一步步优化同一问题，这种问题解决的思路对研究者非常有启发。

## 8. 局限与问题
1.  **参数选择**：算法性能依赖于sketch尺寸参数 `{l_n}` 和幂迭代次数 `q` 的选择。文中虽有理论指导（如定理3要求 `l > k+1`），但在实践中如何为不同数据自动选择最优参数，可能是一个挑战。
2.  **计算开销**：虽然新算法降低了总体复杂度，但子空间幂迭代（算法7）会引入多次矩阵乘法，当 `q` 较大或矩阵本身很大时，这些乘法的累积开销可能需要权衡。
3.  **假设依赖**：误差分析基于一些理想假设，如随机矩阵为标准高斯分布。在实际应用中，非高斯数据或特定数据结构可能影响算法性能，但文中未详细探讨。
4.  **实验范围**：在提供的文本片段中，未能看到在多样化的、极具挑战性的大规模真实数据集上的广泛验证，无法全面评估其实际优势。对于高阶张量（N很大）的性能表现，也未见详细讨论。

## 9. 我该怎么使用这篇论文
*   **如果快速了解**：重点阅读**摘要（Abstract）**、**引言（Introduction）** 的最后一段（贡献总结）和**第6节结论（Conclusion）**。
*   **如果复现**：重点精读**第3节和第4节**，完全理解**算法5（基础sketching）、算法7（子空间幂迭代sketching）以及算法6和8**的步骤。注意参考文献中的基础算法（如R-SVD, STHOSVD）。表2的复杂度分析有助于评估计算成本。
*   **如果借鉴创新点**：应学习**“双侧sketching+子空间幂迭代”这一组合机制**，以及**如何将这种随机化矩阵近似算法系统地集成到张量分解框架（如STHOSVD）中**。误差分析的思路（定理4的证明）也值得参考。
*   **如果写related work**：可将本文归类到 **“随机化张量分解 (Randomized Tensor Decomposition)”** 和 **“基于sketching的低秩近似 (Sketching-based Low-Rank Approximation)”** 两个相关工作的脉络中。

## 10. 和其他论文的关系
基于论文主题（张量、数学、近似），可能高度相关的论文包括：
*   其他经典的随机化Tucker分解算法，如 [[Randomized HOOI for Tucker Decomposition]]。
*   矩阵和张量sketching的基础工作，如 [[Practical Sketching Algorithms for Low-Rank Matrix Approximation (Tropp et al.)]]。
*   张量分解的综述文章，如 [[A review of randomized algorithms for Tucker decomposition]]。
*   张量Train分解等竞争性分解方法的相关工作，如 [[Tensor Train decomposition]]。

## 11. 关键词
张量sketching, 随机化算法, Tucker分解, 子空间幂迭代, 高维数据, 低秩近似, 大规模计算, 数值线性代数, 数据压缩, 计算复杂度

## 12. 可信度说明
本精读笔记主要基于提供的PDF提取文本**前12页**内容生成，这部分包含了论文的**摘要、引言、预备知识（符号、算法介绍）以及核心方法（第3、4节）的详细介绍**。这些内容足以支撑对论文定位、背景、核心贡献、方法原理和理论分析的完整理解。
**提取质量评估**：提供的文本清晰、连贯，包含了关键的定义、定理、算法伪代码和数学公式，为精读提供了高质量的素材。
**主要信息缺失**：由于只提供了前12页，论文**完整的实验结果（第5节）、结论（第6节）以及参考文献列表**未能获取。因此，在“实验与结果”部分无法提供具体的数字结果和数据集细节，这些信息需要在完整论文中查找。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/Tucker近似 Tucker Approximation.txt` (26/26 页; 原 AI 主体 12/26 + 全文补读 13-26); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
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
