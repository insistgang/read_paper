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
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | An Efficient Two-Sided Sketching Method |
| **作者** | Zhiguang Cheng; Gaohang Yu; Xiaohao Cai; Liqun Qi |
| **发表时间** | 2024 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Large tensors are frequently encountered in various fields such as computer vision, scientific simulations, sensor networks, and data mining. However, these tensors are often too large for convenient processing, transfer, or storage. Fortu- nately, they typically exhibit a low-rank structure that can be leveraged through tensordecomposition. However, performinglarge-scaletensordecompositioncan be time-consuming. Sketching is a useful technique to reduce the dimensional- ity of the data. In this paper, we propose a novel two-sided sketching method based on the ⋆ -product decomposition and transformed domains like the dis- L crete cosine transformation. A rigorous theoretical analysis is also conducted to assess the approximation error of the proposed method. Specifically, we improve our method with power iteration to achieve more precise approximate solutions. Extensive numerical experiments and comparisons on low-rank approximation of synthetic large tensors and real-world data like co

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：在计算机视觉、传感器网络等领域，数据常以大规模张量形式存在，且通常具有低秩结构。计算这些大规模张量的精确分解非常耗时，需要高效的近似算法。Sketching是一种通过随机投影或采样来降维的技术，能显著降低计算和存储成本。
- **之前方法有什么问题**：已有的基于t-product的张量Sketching方法（如T-Sketch，rt-SVD）在计算上可以进一步优化。具体而言，t-product在实数域上实现时可能涉及更昂贵的复数中间运算（p. 2, p. 6）。先前的双面张量Sketching算法（如Qi和Yu提出的方法）仅考虑了输入张量的范围和协范围，没有充分利用“核心Sketch”来改进估计。
- **作者想解决的核心矛盾**：在大规模张量低秩近似中，如何平衡**计算效率**与**近似精度**。作者希望通过设计更高效的Sketching算法，在保持理论误差保证和近似精度的同时，大幅降低分解计算的时间复杂度。
## 关键贡献

1.  **提出新的双面Sketching方法**：基于*`L`*-乘积分解和变换域（如DCT），设计了高效的双面Sketching算法（L-TRP-SKETCH），提升了T-Sketch和rt-SVD等方法的计算效率（p. 3, p. 10）。
2.  **建立并扩展低管秩近似模型**：基于*`L`*-乘积分解建立了低管秩张量近似模型，并将Tropp等人提出的矩阵双面Sketching算法与子空间幂迭代技术扩展到了张量情形（p. 3, p. 12）。
3.  **进行严格的理论误差分析**：对所提出方法的近似误差进行了严格的理论评估，为算法提供了理论保障（p. 3, p. 4）。
4.  **提出幂迭代扩展**：展示了如何将幂迭代技术与所提出的Sketching算法结合（以DCT-Gaussian-Sketch-PI为例），通过构造奇异值衰减更快的辅助张量来获得更精确的近似解（p. 3, p. 12）。
5.  **广泛的数值验证**：在合成大张量、彩色图像和灰度视频等多种数据上进行了大量实验，验证了方法在CPU时间和近似精度上的效率和有效性（p. 3, p. 4）。
## 方法

**整体框架**：算法的核心是通过四个张量Sketching算子（`Υ`, `Ω`, `Φ`, `Ψ`）对输入张量`A`进行三次随机投影，得到三个关键Sketch：`X`（捕获协范围）、`Y`（捕获范围）和`Z`（捕获核心信息）。随后，通过一个三步过程从这些Sketch中重构出目标秩为`k`的张量近似`A`。

**输入输出**：
- **输入**：原始张量 `A ∈ R^{m×n×p}`，目标管秩 `k`，以及用于核心Sketch的尺寸参数 `s`（满足 `k ≤ s`），和（可选的）幂迭代次数 `q`。
- **输出**：原始张量`A`的秩为`k`的近似张量 `A^`。

**关键模块与连接**：
1.  **生成随机Sketch**：利用选定的张量Sketching算子（如高斯、SRHT、Count Sketch）生成`X = Υ ∗_L A`, `Y = A ∗_L Ω^H`, `Z = Φ ∗_L A ∗_L Ψ^H` (公式3.14-3.16)。`X`和`Y`分别用于获取`A`的协范围和范围信息，`Z`则提供了直接用于估计核心矩阵的新信息。
2.  **三步重构过程**：
    - **步骤(I)：L-正交三角分解**。对`X^H`和`Y`进行QR分解，得到正交张量`P`和`Q`以及上三角张量`R1`, `R2` (公式3.17)。`P`和`Q`近似张成了`A`的协范围和范围。
    - **步骤(II)：计算核心近似**。利用已知的`P, Q, Φ, Ψ, Z`，通过求解一个基于*`L`*-乘积的最小二乘问题来计算核心张量`C` (公式3.18, 3.19)。这避免了直接计算核心`Q^H ∗_L A ∗_L P`。
    - **步骤(III)：构造最终近似**。将正交张量和核心近似组合，得到低秩近似 `A^ = Q ∗_L C ∗_L P^H` (公式3.21)。

**数学机制的直观解释**：整个过程类似于矩阵的双面投影和截断SVD。`Q`和`P`分别提供了对`A`的行空间和列空间的近似正交基。核心张量`C`近似于`A`在这些基下的坐标（即`Q^H A P`）。由于`C`是通过额外的随机投影`Z`估计而来，而不是通过完整的`A`计算，因此大大降低了计算量。核心Sketch `Z`对于提高`C`的估计精度至关重要。

**与已有方法的差异**：与仅使用范围和协范围Sketch的方法（如Qi和Yu的方法）相比，本文的方法**引入了核心Sketch `Z`**，从而改进了对奇异值和奇异向量的估计，提升了近似精度。与基于t-product（使用DFT）的方法相比，本文基于*`L`*-乘积（使用DCT等实数变换）可以避免或减轻实数张量分解中的中间复数运算开销（p. 2, p. 6）。

**幂迭代扩展（训练/推理流程的一部分）**：为了处理奇异值衰减缓慢的情况，算法2（DCT-Gaussian-Sketch-PI）展示了幂迭代技巧。它不直接对`A`进行Sketching，而是对构造的辅助张量`B = (A ∗_L A^H)^q ∗_L A`进行操作。根据变换张量SVD (公式3.26)，`B`的奇异值`(S)^{2q+1}`比`A`的奇异值`S`衰减更快，从而能让Sketching算法更好地捕获主要成分。在实际实现中，幂迭代通过交替投影`A`和`A^H`到当前的`Q`和`P`上来实现（算法2，第8-14行），而无需显式构造`B`。
## 实验

- **使用的数据集**：合成大张量、真实世界的彩色图像和灰度视频（p. 3, p. 4）。PDF文本前12页中未明确列出具体数据集名称。
- **对比方法**：PDF文本前12页中未明确列出具体对比方法。
- **评价指标**：近似误差（如Frobenius范数误差）、CPU时间（p. 3, p. 4）。
- **主实验结果**：PDF文本前12页中未提供具体的实验结果数字。
- **消融实验**：PDF文本前12页中未提及。
- **泛化实验**：通过在不同类型数据（合成、图像、视频）上进行实验来展示方法的通用性。
- **效率信息**：算法1的存储复杂度为`O(mkp + nkp + kkp)`浮点数（p. 10）。论文强调了方法在CPU时间上的优势。
## 局限

- **假设依赖**：理论分析依赖于输入张量具有低管秩的结构，或近似低管秩（即尾部能量较小）。对于秩不低的张量，方法可能失效或优势不明显。
- **参数选择**：算法需要用户指定目标秩`k`、Sketch尺寸`s`和（如果使用幂迭代）迭代次数`q`。这些参数的选择可能需要先验知识或调参。
- **线性变换的选择**：虽然论文提供了DFT、DCT和U三种选择，但最优的变换`L`可能依赖于数据，如何自适应选择未在文中讨论。
- **应用场景限制**：论文主要关注张量的低秩近似任务。该方法是否适用于其他张量计算任务（如回归、优化）尚未可知。
- **复现风险**：论文涉及多种张量算子和变换，实现时需注意细节，如共轭转置在变换域中的定义、正交三角分解的`qr`函数实现等。部分实验细节在前12页未完全给出。
## 个人评论

这篇论文最值得学习的点在于其**将矩阵双面Sketching思想系统化地扩展到张量领域，并通过巧妙的变换域设计和核心Sketch的引入来优化计算**。它对后续研究的启发包括：
1.  **模块化设计思路**：将张量分解问题转化为一系列矩阵操作（在变换域逐切片进行），这种分治思想可以用于解决其他高维数据问题。
2.  **理论结合实践**：论文不仅提出算法，还提供了严格的误差界分析（定理4.1-4.3等，虽未在前文详述），这种严谨性值得借鉴。
3.  **灵活性**：框架允许灵活选择不同的线性变换`L`（DFT, DCT, U）和不同的随机投影算子，为针对不同应用场景的定制化提供了空间。
4.  **针对实数张量的优化**：通过使用DCT等实数变换，避免了t-product中不必要的复数运算，这对处理大规模实数数据（如图像）具有实际意义。

### 使用建议

- **如果快速了解**：重点阅读**摘要（Abstract）**、**引言（Introduction）**的后半部分（贡献和论文结构）以及**第3节（方法）**的3.1小节（算法描述）。
- **如果复现**：必须精读**第3节（方法）**中的算法1和算法2伪代码，并结合**第2节（符号与预备知识）**中对*`L`*-乘积、变换SVD和张量Sketching算子的定义。附录A和B中的详细理论证明和矩阵Sketching技术也需参考。
- **如果借鉴创新点**：应学习其**将问题分解到变换域处理**的框架，以及**引入核心Sketch改进估计**的策略。幂迭代技术是提升低秩近似精度的一种通用技巧，可以借鉴到其他随机化算法中。
- **如果写related work**：可放在“**随机化张量分解**”、“**基于Sketching的张量近似**”或“**基于t-product及其变体的计算**”等相关工作类别中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[N_雷达_无线电_张量_数学]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**张量计算与随机化算法**方向。它主要解决**大规模张量分解计算效率低下**的核心问题。通过引入基于特定线性变换（如离散余弦变换DCT）的双面Sketching方法，旨在高效、准确地计算大规模张量的低秩（具体为低管秩）近似。该工作可归类于“**张量分解与近似**”这一主题下，涉及随机化数值线性代数、数据压缩和张量分析。

## 2. 一句话总结
本文提出了一种基于变换域的**双面张量Sketching方法**，通过构建输入张量的范围、协范围和核心信息的随机化概要（Sketch），显著提升了大规模张量低管秩近似的计算效率，同时保持了较高的近似精度。

## 3. 背景与问题
- **这篇论文为什么要做**：在计算机视觉、传感器网络等领域，数据常以大规模张量形式存在，且通常具有低秩结构。计算这些大规模张量的精确分解非常耗时，需要高效的近似算法。Sketching是一种通过随机投影或采样来降维的技术，能显著降低计算和存储成本。
- **之前方法有什么问题**：已有的基于t-product的张量Sketching方法（如T-Sketch，rt-SVD）在计算上可以进一步优化。具体而言，t-product在实数域上实现时可能涉及更昂贵的复数中间运算（p. 2, p. 6）。先前的双面张量Sketching算法（如Qi和Yu提出的方法）仅考虑了输入张量的范围和协范围，没有充分利用“核心Sketch”来改进估计。
- **作者想解决的核心矛盾**：在大规模张量低秩近似中，如何平衡**计算效率**与**近似精度**。作者希望通过设计更高效的Sketching算法，在保持理论误差保证和近似精度的同时，大幅降低分解计算的时间复杂度。

## 4. 核心贡献
1.  **提出新的双面Sketching方法**：基于*`L`*-乘积分解和变换域（如DCT），设计了高效的双面Sketching算法（L-TRP-SKETCH），提升了T-Sketch和rt-SVD等方法的计算效率（p. 3, p. 10）。
2.  **建立并扩展低管秩近似模型**：基于*`L`*-乘积分解建立了低管秩张量近似模型，并将Tropp等人提出的矩阵双面Sketching算法与子空间幂迭代技术扩展到了张量情形（p. 3, p. 12）。
3.  **进行严格的理论误差分析**：对所提出方法的近似误差进行了严格的理论评估，为算法提供了理论保障（p. 3, p. 4）。
4.  **提出幂迭代扩展**：展示了如何将幂迭代技术与所提出的Sketching算法结合（以DCT-Gaussian-Sketch-PI为例），通过构造奇异值衰减更快的辅助张量来获得更精确的近似解（p. 3, p. 12）。
5.  **广泛的数值验证**：在合成大张量、彩色图像和灰度视频等多种数据上进行了大量实验，验证了方法在CPU时间和近似精度上的效率和有效性（p. 3, p. 4）。

## 5. 方法详解
**整体框架**：算法的核心是通过四个张量Sketching算子（`Υ`, `Ω`, `Φ`, `Ψ`）对输入张量`A`进行三次随机投影，得到三个关键Sketch：`X`（捕获协范围）、`Y`（捕获范围）和`Z`（捕获核心信息）。随后，通过一个三步过程从这些Sketch中重构出目标秩为`k`的张量近似`A`。

**输入输出**：
- **输入**：原始张量 `A ∈ R^{m×n×p}`，目标管秩 `k`，以及用于核心Sketch的尺寸参数 `s`（满足 `k ≤ s`），和（可选的）幂迭代次数 `q`。
- **输出**：原始张量`A`的秩为`k`的近似张量 `A^`。

**关键模块与连接**：
1.  **生成随机Sketch**：利用选定的张量Sketching算子（如高斯、SRHT、Count Sketch）生成`X = Υ ∗_L A`, `Y = A ∗_L Ω^H`, `Z = Φ ∗_L A ∗_L Ψ^H` (公式3.14-3.16)。`X`和`Y`分别用于获取`A`的协范围和范围信息，`Z`则提供了直接用于估计核心矩阵的新信息。
2.  **三步重构过程**：
    - **步骤(I)：L-正交三角分解**。对`X^H`和`Y`进行QR分解，得到正交张量`P`和`Q`以及上三角张量`R1`, `R2` (公式3.17)。`P`和`Q`近似张成了`A`的协范围和范围。
    - **步骤(II)：计算核心近似**。利用已知的`P, Q, Φ, Ψ, Z`，通过求解一个基于*`L`*-乘积的最小二乘问题来计算核心张量`C` (公式3.18, 3.19)。这避免了直接计算核心`Q^H ∗_L A ∗_L P`。
    - **步骤(III)：构造最终近似**。将正交张量和核心近似组合，得到低秩近似 `A^ = Q ∗_L C ∗_L P^H` (公式3.21)。

**数学机制的直观解释**：整个过程类似于矩阵的双面投影和截断SVD。`Q`和`P`分别提供了对`A`的行空间和列空间的近似正交基。核心张量`C`近似于`A`在这些基下的坐标（即`Q^H A P`）。由于`C`是通过额外的随机投影`Z`估计而来，而不是通过完整的`A`计算，因此大大降低了计算量。核心Sketch `Z`对于提高`C`的估计精度至关重要。

**与已有方法的差异**：与仅使用范围和协范围Sketch的方法（如Qi和Yu的方法）相比，本文的方法**引入了核心Sketch `Z`**，从而改进了对奇异值和奇异向量的估计，提升了近似精度。与基于t-product（使用DFT）的方法相比，本文基于*`L`*-乘积（使用DCT等实数变换）可以避免或减轻实数张量分解中的中间复数运算开销（p. 2, p. 6）。

**幂迭代扩展（训练/推理流程的一部分）**：为了处理奇异值衰减缓慢的情况，算法2（DCT-Gaussian-Sketch-PI）展示了幂迭代技巧。它不直接对`A`进行Sketching，而是对构造的辅助张量`B = (A ∗_L A^H)^q ∗_L A`进行操作。根据变换张量SVD (公式3.26)，`B`的奇异值`(S)^{2q+1}`比`A`的奇异值`S`衰减更快，从而能让Sketching算法更好地捕获主要成分。在实际实现中，幂迭代通过交替投影`A`和`A^H`到当前的`Q`和`P`上来实现（算法2，第8-14行），而无需显式构造`B`。

## 6. 实验与结果
- **使用的数据集**：合成大张量、真实世界的彩色图像和灰度视频（p. 3, p. 4）。PDF文本前12页中未明确列出具体数据集名称。
- **对比方法**：PDF文本前12页中未明确列出具体对比方法。
- **评价指标**：近似误差（如Frobenius范数误差）、CPU时间（p. 3, p. 4）。
- **主实验结果**：PDF文本前12页中未提供具体的实验结果数字。
- **消融实验**：PDF文本前12页中未提及。
- **泛化实验**：通过在不同类型数据（合成、图像、视频）上进行实验来展示方法的通用性。
- **效率信息**：算法1的存储复杂度为`O(mkp + nkp + kkp)`浮点数（p. 10）。论文强调了方法在CPU时间上的优势。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的点在于其**将矩阵双面Sketching思想系统化地扩展到张量领域，并通过巧妙的变换域设计和核心Sketch的引入来优化计算**。它对后续研究的启发包括：
1.  **模块化设计思路**：将张量分解问题转化为一系列矩阵操作（在变换域逐切片进行），这种分治思想可以用于解决其他高维数据问题。
2.  **理论结合实践**：论文不仅提出算法，还提供了严格的误差界分析（定理4.1-4.3等，虽未在前文详述），这种严谨性值得借鉴。
3.  **灵活性**：框架允许灵活选择不同的线性变换`L`（DFT, DCT, U）和不同的随机投影算子，为针对不同应用场景的定制化提供了空间。
4.  **针对实数张量的优化**：通过使用DCT等实数变换，避免了t-product中不必要的复数运算，这对处理大规模实数数据（如图像）具有实际意义。

## 8. 局限与问题
- **假设依赖**：理论分析依赖于输入张量具有低管秩的结构，或近似低管秩（即尾部能量较小）。对于秩不低的张量，方法可能失效或优势不明显。
- **参数选择**：算法需要用户指定目标秩`k`、Sketch尺寸`s`和（如果使用幂迭代）迭代次数`q`。这些参数的选择可能需要先验知识或调参。
- **线性变换的选择**：虽然论文提供了DFT、DCT和U三种选择，但最优的变换`L`可能依赖于数据，如何自适应选择未在文中讨论。
- **应用场景限制**：论文主要关注张量的低秩近似任务。该方法是否适用于其他张量计算任务（如回归、优化）尚未可知。
- **复现风险**：论文涉及多种张量算子和变换，实现时需注意细节，如共轭转置在变换域中的定义、正交三角分解的`qr`函数实现等。部分实验细节在前12页未完全给出。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**摘要（Abstract）**、**引言（Introduction）**的后半部分（贡献和论文结构）以及**第3节（方法）**的3.1小节（算法描述）。
- **如果复现**：必须精读**第3节（方法）**中的算法1和算法2伪代码，并结合**第2节（符号与预备知识）**中对*`L`*-乘积、变换SVD和张量Sketching算子的定义。附录A和B中的详细理论证明和矩阵Sketching技术也需参考。
- **如果借鉴创新点**：应学习其**将问题分解到变换域处理**的框架，以及**引入核心Sketch改进估计**的策略。幂迭代技术是提升低秩近似精度的一种通用技巧，可以借鉴到其他随机化算法中。
- **如果写related work**：可放在“**随机化张量分解**”、“**基于Sketching的张量近似**”或“**基于t-product及其变体的计算**”等相关工作类别中。

## 10. 和其他论文的关系
根据文件名“双面Sketching张量”和内容，这篇论文直接建立在以下工作的基础上，并进行了扩展：
- `[[Tropp et al. 2017 Fixed-Rank Approximation on a Budget]]`：本文提出的张量双面Sketching模型是对该文中矩阵双面Sketching算法的张量扩展（p. 2, p. 12）。
- `[[Qi and Yu 2022 T-Sketch]]`：本文指出其方法是对T-Sketch的改进，通过使用*`L`*-乘积和引入核心Sketch来提升效率和精度（p. 2, p. 9）。
- `[[Kernfeld et al. 2015 Popov-Terdemite]]`：本文采用的*`L`*-乘积框架来源于此工作，以避免t-product在实数域中的复数运算问题（p. 2, p. 6）。

## 11. 关键词
大规模张量， 张量分解， Sketching， 低秩近似， *`L`*-乘积， 变换域， 离散余弦变换 (DCT)， 双面投影， 幂迭代， 计算效率

## 12. 可信度说明
本篇精读笔记**严格基于用户提供的PDF前12页文本内容生成**。所有描述、贡献、算法步骤和引用均来源于此文本。由于提供的文本仅覆盖论文的前12页（共37页），因此**完整的实验结果、部分理论证明细节（如定理4.1-4.3）、以及附录内容未能在本笔记中详尽呈现**。笔记中对实验数据集、对比方法等的具体描述已标注为“PDF文本中未明确说明”。提取的文本质量良好，关键公式和算法伪代码清晰，足以支撑对论文核心思想、方法和框架的理解。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2077 字符/页)); 来源缓存: `.paper-cache/extracts/双面Sketching张量 Two-Sided Sketching.txt` (37/37 页; 原 AI 主体 12/37 + 全文补读 13-37); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
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
