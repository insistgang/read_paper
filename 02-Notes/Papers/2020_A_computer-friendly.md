---
title: A computer-friendly construction of the monster
authors:
  - "Martin Seysen"
year: 2020
venue: "arXiv"
doi: 
pdf: [[2020_A_computer-friendly.pdf]]
primary_topic: S_变化检测_ChangeDetection
topics:
  - "S_变化检测_ChangeDetection"
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2020_A_computer-friendly.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/43 pages"
---
# A computer-friendly construction of the monster

## 基本信息
- **PDF**: [[2020_A_computer-friendly.pdf]]
- **primary_topic**: `S_变化检测_ChangeDetection`
- **topics**: `S_变化检测_ChangeDetection`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A computer-friendly construction of the monster |
| **作者** | Martin Seysen |
| **发表时间** | 2020 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Let M be the monster group which is the largest sporadic finite simple group, and hasfirstbeenconstructedin1982byGriess. In1985,Conwayhasconstructeda196884- dimensionalrepresentationρofMwithmatrixcoefficientsinZ[1]. Sothesematricesmay bereducedmoduloany(notnecessarilyprime)oddnumberp,leadingtorepresentations of M in odd characteristic. The representation ρ is based on representations of two maximalsubgroupsG andN ofM. InATLASnotation,G hasstructure21+24.Co x0 0 x0 + 1 and N has structure 22+11+22.(M ×S ). Conway has constructed an explicit set of 0 24 3 generators of N , but not of G . 0 x0 ThispaperisessentiallyarewriteofConway’sconstructionaugmentedbyanexplicit construction of an element of G \N . This gives us a complete set of generators of M. x0 0 It turns out that the matrices of all generators of M consist of monomial blocks, and of blocks which are essentially Hadamard matrices scaled by a negative power of two. Multiplication with such a generator can be programmed very effici

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：怪兽群是最大的散在有限单群，其构造和研究是有限群理论的核心。Griess (1982) 和 Conway (1985) 分别给出了开创性的构造，其中Conway给出了一个196884维的有理表示。然而，Conway的构造是不完整的。
- **之前方法的问题**：Conway的构造基于两个极大子群`N0`和`Gx0`，他只显式给出了`N0`的生成元，但没有给出`Gx0 \ N0`中任何元素的显式表示。因此，无法获得`M`的一组完整生成元，也就无法完全基于此构造进行计算。
- **作者想解决的核心矛盾**：如何**显式地构造**出`Gx0 \ N0`中一个生成元`ξ`的表示，并调整整个构造框架（特别是Parker环的余环选择），使得最终得到的所有怪兽群生成元都具有简单的矩阵结构（如单项式块和Hadamard块），从而实现高效的计算机编程。
## 关键贡献

1.  **提供了怪兽群`M`的一组完整的显式生成元**：包括显式构造了一个关键元素`ξ ∈ Gx0 \ N0`的表示（见第9.4节）。
2.  **揭示了生成元矩阵的简单结构**：所有生成元的矩阵均可分解为**单项式块（monomial blocks）** 和**由2x2 Hadamard矩阵缩放而成的块**。
3.  **提出了“Hadamard步”的概念并证明了其充分性**：任何生成元作用于向量的操作，可以分解为**至多6个Hadamard步**加上一些单项式操作，这极大地简化了计算流程。
4.  **针对特定模数优化了实现**：当模数`p`为`2^k - 1`的形式时（如3, 7, 15, 31, 127, 255），利用比特位操作可以同时对向量的多个分量进行模运算，实现了非常高效的计算。
5.  **调整并统一了数学构造**：对Conway原始构造中的某些符号约定进行了两处明确的修改，使得`Gx0`的表示（基于Leach lattice和Clifford群的构造）与`N0`的表示更兼容，整体构造更简洁。
6.  **提供了程序员的实现参考**：论文被定位为“程序员的参考”，并实际提供了`p=3,7,15,31,127,255`下的实现（代码见引用[16]）。
## 方法

- **整体框架**：本文是对Conway 1985年构造的“重写”与“增强”。整体思路是先构造`M`的两个极大子群`N0`和`Gx0`的明确表示，然后通过它们生成整个群`M`。关键创新点在于补充了`Gx0`中一个不在`N0`内的生成元`ξ`的表示。
- **输入/输出**：
    - **输入**：群`M`中一个元素`g`，以及一个奇模数`p`。
    - **输出**：该元素`g`在`p`维表示`ρ_p`下的矩阵，作用于一个向量。
- **关键模块**：
    1.  **Golay码`C`及其码余码`C*`**：这是构造`N0`子群的基础。论文详细描述了利用MOG（奇迹八元生成器）来定义一个具体的Golay码实例（第2.1节），并创新性地将其分解为**灰色子空间`G`** 和**彩色子空间`H`** 的直和 `C = G ⊕ H`（第2.2节）。这个分解对于后续构造`ξ`至关重要。
    2.  **Parker环`P`及其余环`θ`**：`P`是一个非结合的Moufang环，其结构由`C`和`F2`的笛卡尔积定义。一个**余环(cocycle) `θ`** 用于定义`P`上的乘法（式3.2.3）。作者指出，`θ`的选择不是唯一的（引理3.4），为了简化后续生成元`ξ`的表示，需要精心选择一个与`G`/`H`分解兼容的特定余环（第3.3节）。
    3.  **生成元`ξ`的构造**：这是论文的核心新结果。`ξ`应属于`Gx0 \ N0`。作者利用前述`G`和`G*`的互相对偶基（`g0,...,g5` 和 `γ0,...,γ5`），以及一个关键的线性双射`γ: G → G*`（式3.5.2），来定义`ξ`的作用。`ξ`的作用交换了`G`和`G*`，并固定`H`和`H*`，从而实现了从`2^{1+24}.Co1`到`2^{1+24+11}.M24`的跨越。
- **模块连接**：`C`的`G/H`分解 → 定义在`C`上的`Parker`环`P` → 选择与`G/H`分解兼容的余环`θ` → 利用`γ`映射和`θ`定义元素`ξ` → `ξ`与`N0`的生成元一起构成`M`的完整生成元集。
- **数学机制的直观解释**：`G`和`G*`可以看作是同一个6维`F2`空间上的两套基。`ξ`的作用类似于在`G`和`G*`之间做一个“交换”，同时保持由`H`定义的“颜色”部分不变。这反映了`Co1`和`M24`在Leach lattice`Λ/2Λ`自同构群中的关系。
- **计算流程**：计算`ρ_p(g)v`时，将`g`分解为`N0`生成元和`ξ`的乘积。每个生成元的矩阵作用被分解为一系列**Hadamard步**（乘以包含`[1,1;1,-1]`块的矩阵）和单项式操作（置换和缩放）。当`p = 2^k - 1`时，模运算可以利用比特位并行完成。
- **与已有方法的差异**：Holmes & Wilson (特征3的构造)使用了高达276x276的非单项式块。本文通过符号调整和余环选择，将**所有生成元**都限制为仅由单项式和2x2 Hadamard块构成，结构极其规则，计算效率更高。
## 实验

- **使用的数据集/对象**：怪兽群`M`本身。
- **对比方法**：文中提到了Conway (1985) 的原始构造以及Holmes & Wilson 的构造作为背景对比。
- **评价指标**：
    1.  **计算时间**：在特定硬件（Intel Core i7-8750H）上，计算`ρ_p(g)`作用于单个向量的时间。
    2.  **矩阵结构的简洁性**：以是否仅由单项式块和缩放的Hadamard块组成作为标准。
- **主实验结果**：
    - 实现了`M`在模数`p = 3, 7, 15, 31, 127, 255`下的表示（p.1）。
    - **效率基准**：对于`p=3`，单向量操作耗时**0.73 ms**；对于`p=255`，耗时**1.35 ms**（p.2）。
- **消融实验**：文本中未明确说明进行传统的消融实验。其核心“实验”在于通过理论构造保证所有生成元具有相同的简单矩阵结构。
- **泛化实验**：文本中未说明在其它群或其它表示维度上的泛化实验。
- **效率信息**：给出了具体的运行时间基准。并解释了在`p=2^k-1`时，模运算的比特位并行操作带来的效率提升原理（p.2）。
## 局限

- **适用场景有限**：此构造严格依赖于**Golay码**、**Leach lattice**和**Parker环**这些特定的代数结构，是专为怪兽群设计的，不适用于其他群。
- **计算复杂度依然很高**：尽管优化了，但196884维的表示本身就巨大，即使单向量操作在毫秒级，大规模计算或高维表示下的操作成本仍然很高。
- **模数限制**：目前的高效实现严格依赖于模数`p`是`2^k-1`的形式，对于其他奇素数（如5，11）的高效实现方法未在本文中说明。
- **假设依赖**：整个构造依赖于对`MOG`表格（式2.1.1）和`hexacode`等具体实例的固定选择。虽然文中给出了参考，但复现时必须严格遵循同一套实例，否则无法保证正确性。
- **复现风险**：复现的核心难点在于对数学细节的理解，特别是第3.3节关于“选择合适余环”的证明和构造，以及第9.4节关于`ξ`的具体定义。任何符号或约定的微小偏差都可能导致错误。
- **实验不充分**：从提供“完整实验”的角度看，缺乏在不同硬件平台上的性能测试，也未与Holmes & Wilson等构造进行直接的计算时间对比。
## 个人评论

1.  **将深奥的抽象构造“模块化”和“可编程化”**：论文的最大价值在于将Conway等人的高度理论化的数学构造，分解为程序员可以理解和实现的明确模块（Golay码表、Parker环乘法表、生成元矩阵的分解规则）。这为计算群论提供了一个宝贵的实践范本。
2.  **“兼容性设计”的思想**：为了得到一个简洁的生成元`ξ`，作者没有强行在原有框架上修补，而是通过**调整基础（符号约定）和核心结构（Parker环的余环）**，使得`Gx0`和`N0`的表示能够“友好地”对接。这种为下游任务优化顶层设计的思路，对很多数学建模和算法设计有启发。
3.  **对特定算术的高度优化**：敏锐地发现当模数为`2^k-1`时，计算机的位运算与模运算可以完美结合，从而提出并验证了这种极高效的实现方案。这展示了理论数学构造如何针对现代计算机硬件特性进行优化。
4.  **提供了可验证的基准实现**：附带的代码实现（[16]）使得任何研究者都可以验证、使用或基于此进行进一步探索，极大地降低了该领域研究和应用的门槛。

### 使用建议

- **如果快速了解**：只读**摘要**、**引言（第1章）** 以及**第4章（核心贡献）** 的列表。这能让你快速掌握论文的目标、方法和主要成果。
- **如果复现**：重点精读**第2章（Golay码）**、**第3章（Parker环和余环选择）** 以及**第9章（特别是9.4节构造`ξ`）**。必须对照ATLAS符号手册和参考文献[5][7]来理解子群结构。附录或引用[16]中的代码是最终验证的依据。
- **如果借鉴创新点**：应学习其**将复杂代数结构分解为可计算模块**的思路，以及**通过调整基础结构（如余环）来简化上层表示**的设计哲学。此外，针对`2^k-1`模数的位运算并行优化技巧，可应用于其他需要模运算的大规模群表示计算中。
- **如果写related work**：可放在“有限单群的计算表示”、“怪兽群的具体构造与实现”、“基于格或码的群表示”等相关工作的类别中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[S_变化检测_ChangeDetection]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**计算群论**与**表示论**方向，旨在解决“怪兽群”（Monster Group）这一最大散在有限单群的显式、计算友好型构造问题。它为数学家和程序员提供了一个具体、可编程的怪兽群表示实现参考，尤其侧重于实现其在奇特征（odd characteristic）下的矩阵表示。虽然用户指定的主题标签是“S_变化检测_ChangeDetection”，但根据PDF文本内容，这显然是一篇纯数学领域的群论论文。它可能通过提供离散对称结构的实例化工具，与模式识别、异常检测（可视为“结构变化”）等领域有潜在的间接联系，但文本本身未涉及任何这些应用。

## 2. 一句话总结
本文通过对Conway怪兽群构造的系统重写和关键补充，提供了一套完整、显式且计算高效的怪兽群生成元集合及其矩阵表示，特别适合在模`p = 2^k - 1`的算术下进行编程实现。

## 3. 背景与问题
- **为什么要做**：怪兽群是最大的散在有限单群，其构造和研究是有限群理论的核心。Griess (1982) 和 Conway (1985) 分别给出了开创性的构造，其中Conway给出了一个196884维的有理表示。然而，Conway的构造是不完整的。
- **之前方法的问题**：Conway的构造基于两个极大子群`N0`和`Gx0`，他只显式给出了`N0`的生成元，但没有给出`Gx0 \ N0`中任何元素的显式表示。因此，无法获得`M`的一组完整生成元，也就无法完全基于此构造进行计算。
- **作者想解决的核心矛盾**：如何**显式地构造**出`Gx0 \ N0`中一个生成元`ξ`的表示，并调整整个构造框架（特别是Parker环的余环选择），使得最终得到的所有怪兽群生成元都具有简单的矩阵结构（如单项式块和Hadamard块），从而实现高效的计算机编程。

## 4. 核心贡献
1.  **提供了怪兽群`M`的一组完整的显式生成元**：包括显式构造了一个关键元素`ξ ∈ Gx0 \ N0`的表示（见第9.4节）。
2.  **揭示了生成元矩阵的简单结构**：所有生成元的矩阵均可分解为**单项式块（monomial blocks）** 和**由2x2 Hadamard矩阵缩放而成的块**。
3.  **提出了“Hadamard步”的概念并证明了其充分性**：任何生成元作用于向量的操作，可以分解为**至多6个Hadamard步**加上一些单项式操作，这极大地简化了计算流程。
4.  **针对特定模数优化了实现**：当模数`p`为`2^k - 1`的形式时（如3, 7, 15, 31, 127, 255），利用比特位操作可以同时对向量的多个分量进行模运算，实现了非常高效的计算。
5.  **调整并统一了数学构造**：对Conway原始构造中的某些符号约定进行了两处明确的修改，使得`Gx0`的表示（基于Leach lattice和Clifford群的构造）与`N0`的表示更兼容，整体构造更简洁。
6.  **提供了程序员的实现参考**：论文被定位为“程序员的参考”，并实际提供了`p=3,7,15,31,127,255`下的实现（代码见引用[16]）。

## 5. 方法详解
- **整体框架**：本文是对Conway 1985年构造的“重写”与“增强”。整体思路是先构造`M`的两个极大子群`N0`和`Gx0`的明确表示，然后通过它们生成整个群`M`。关键创新点在于补充了`Gx0`中一个不在`N0`内的生成元`ξ`的表示。
- **输入/输出**：
    - **输入**：群`M`中一个元素`g`，以及一个奇模数`p`。
    - **输出**：该元素`g`在`p`维表示`ρ_p`下的矩阵，作用于一个向量。
- **关键模块**：
    1.  **Golay码`C`及其码余码`C*`**：这是构造`N0`子群的基础。论文详细描述了利用MOG（奇迹八元生成器）来定义一个具体的Golay码实例（第2.1节），并创新性地将其分解为**灰色子空间`G`** 和**彩色子空间`H`** 的直和 `C = G ⊕ H`（第2.2节）。这个分解对于后续构造`ξ`至关重要。
    2.  **Parker环`P`及其余环`θ`**：`P`是一个非结合的Moufang环，其结构由`C`和`F2`的笛卡尔积定义。一个**余环(cocycle) `θ`** 用于定义`P`上的乘法（式3.2.3）。作者指出，`θ`的选择不是唯一的（引理3.4），为了简化后续生成元`ξ`的表示，需要精心选择一个与`G`/`H`分解兼容的特定余环（第3.3节）。
    3.  **生成元`ξ`的构造**：这是论文的核心新结果。`ξ`应属于`Gx0 \ N0`。作者利用前述`G`和`G*`的互相对偶基（`g0,...,g5` 和 `γ0,...,γ5`），以及一个关键的线性双射`γ: G → G*`（式3.5.2），来定义`ξ`的作用。`ξ`的作用交换了`G`和`G*`，并固定`H`和`H*`，从而实现了从`2^{1+24}.Co1`到`2^{1+24+11}.M24`的跨越。
- **模块连接**：`C`的`G/H`分解 → 定义在`C`上的`Parker`环`P` → 选择与`G/H`分解兼容的余环`θ` → 利用`γ`映射和`θ`定义元素`ξ` → `ξ`与`N0`的生成元一起构成`M`的完整生成元集。
- **数学机制的直观解释**：`G`和`G*`可以看作是同一个6维`F2`空间上的两套基。`ξ`的作用类似于在`G`和`G*`之间做一个“交换”，同时保持由`H`定义的“颜色”部分不变。这反映了`Co1`和`M24`在Leach lattice`Λ/2Λ`自同构群中的关系。
- **计算流程**：计算`ρ_p(g)v`时，将`g`分解为`N0`生成元和`ξ`的乘积。每个生成元的矩阵作用被分解为一系列**Hadamard步**（乘以包含`[1,1;1,-1]`块的矩阵）和单项式操作（置换和缩放）。当`p = 2^k - 1`时，模运算可以利用比特位并行完成。
- **与已有方法的差异**：Holmes & Wilson (特征3的构造)使用了高达276x276的非单项式块。本文通过符号调整和余环选择，将**所有生成元**都限制为仅由单项式和2x2 Hadamard块构成，结构极其规则，计算效率更高。

## 6. 实验与结果
- **使用的数据集/对象**：怪兽群`M`本身。
- **对比方法**：文中提到了Conway (1985) 的原始构造以及Holmes & Wilson 的构造作为背景对比。
- **评价指标**：
    1.  **计算时间**：在特定硬件（Intel Core i7-8750H）上，计算`ρ_p(g)`作用于单个向量的时间。
    2.  **矩阵结构的简洁性**：以是否仅由单项式块和缩放的Hadamard块组成作为标准。
- **主实验结果**：
    - 实现了`M`在模数`p = 3, 7, 15, 31, 127, 255`下的表示（p.1）。
    - **效率基准**：对于`p=3`，单向量操作耗时**0.73 ms**；对于`p=255`，耗时**1.35 ms**（p.2）。
- **消融实验**：文本中未明确说明进行传统的消融实验。其核心“实验”在于通过理论构造保证所有生成元具有相同的简单矩阵结构。
- **泛化实验**：文本中未说明在其它群或其它表示维度上的泛化实验。
- **效率信息**：给出了具体的运行时间基准。并解释了在`p=2^k-1`时，模运算的比特位并行操作带来的效率提升原理（p.2）。

## 7. 这篇论文真正有价值的地方
1.  **将深奥的抽象构造“模块化”和“可编程化”**：论文的最大价值在于将Conway等人的高度理论化的数学构造，分解为程序员可以理解和实现的明确模块（Golay码表、Parker环乘法表、生成元矩阵的分解规则）。这为计算群论提供了一个宝贵的实践范本。
2.  **“兼容性设计”的思想**：为了得到一个简洁的生成元`ξ`，作者没有强行在原有框架上修补，而是通过**调整基础（符号约定）和核心结构（Parker环的余环）**，使得`Gx0`和`N0`的表示能够“友好地”对接。这种为下游任务优化顶层设计的思路，对很多数学建模和算法设计有启发。
3.  **对特定算术的高度优化**：敏锐地发现当模数为`2^k-1`时，计算机的位运算与模运算可以完美结合，从而提出并验证了这种极高效的实现方案。这展示了理论数学构造如何针对现代计算机硬件特性进行优化。
4.  **提供了可验证的基准实现**：附带的代码实现（[16]）使得任何研究者都可以验证、使用或基于此进行进一步探索，极大地降低了该领域研究和应用的门槛。

## 8. 局限与问题
- **适用场景有限**：此构造严格依赖于**Golay码**、**Leach lattice**和**Parker环**这些特定的代数结构，是专为怪兽群设计的，不适用于其他群。
- **计算复杂度依然很高**：尽管优化了，但196884维的表示本身就巨大，即使单向量操作在毫秒级，大规模计算或高维表示下的操作成本仍然很高。
- **模数限制**：目前的高效实现严格依赖于模数`p`是`2^k-1`的形式，对于其他奇素数（如5，11）的高效实现方法未在本文中说明。
- **假设依赖**：整个构造依赖于对`MOG`表格（式2.1.1）和`hexacode`等具体实例的固定选择。虽然文中给出了参考，但复现时必须严格遵循同一套实例，否则无法保证正确性。
- **复现风险**：复现的核心难点在于对数学细节的理解，特别是第3.3节关于“选择合适余环”的证明和构造，以及第9.4节关于`ξ`的具体定义。任何符号或约定的微小偏差都可能导致错误。
- **实验不充分**：从提供“完整实验”的角度看，缺乏在不同硬件平台上的性能测试，也未与Holmes & Wilson等构造进行直接的计算时间对比。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读**摘要**、**引言（第1章）** 以及**第4章（核心贡献）** 的列表。这能让你快速掌握论文的目标、方法和主要成果。
- **如果复现**：重点精读**第2章（Golay码）**、**第3章（Parker环和余环选择）** 以及**第9章（特别是9.4节构造`ξ`）**。必须对照ATLAS符号手册和参考文献[5][7]来理解子群结构。附录或引用[16]中的代码是最终验证的依据。
- **如果借鉴创新点**：应学习其**将复杂代数结构分解为可计算模块**的思路，以及**通过调整基础结构（如余环）来简化上层表示**的设计哲学。此外，针对`2^k-1`模数的位运算并行优化技巧，可应用于其他需要模运算的大规模群表示计算中。
- **如果写related work**：可放在“有限单群的计算表示”、“怪兽群的具体构造与实现”、“基于格或码的群表示”等相关工作的类别中。

## 10. 和其他论文的关系
根据提供的主题`S_变化检测_ChangeDetection`，本文属于纯数学群论。主题标签可能是文件归档时的系统错误或宽泛关联，PDF文本内容未提及与变化检测、模式识别或任何机器学习应用相关的内容。因此，无法基于文本内容确定与其他论文的直接关联。文中明确引用的论文包括：Griess [9], Conway [5], ATLAS [6], Aschbacher [2], Holmes & Wilson [13], Ivanov [14], Nebe, Rains, and Sloane [15] 等，这些均属于群论领域。

## 11. 关键词
怪兽群 (Monster group), 有限单群 (finite simple groups), 群表示 (group representation), Golay码 (Golay code), 码余码 (cocode), Parker环 (Parker loop), 余环 (cocycle), Leach lattice, Conway群, 计算群论, Hadamard矩阵, 模运算

## 12. 可信度说明
本精读笔记**完全基于**用户提供的PDF提取文本（前12页，共43页）生成。文本提取了论文的**摘要、引言、第2章（Golay码）和第3章（Parker环）的大部分内容**。核心方法部分（特别是第4章之后的贡献详解、第9章构造`ξ`的细节、以及完整的实验结果）在提供的文本中**缺失或不完整**。因此：
- **能可靠获取的信息**：论文的动机、背景、初步框架、部分数学基础（Golay码和Parker环的定义）以及作者声称的贡献和实验结果。
- **可能不完整或缺失的信息**：`ξ`的最终显式表达式、`Gx0`表示的完整细节、完整的实验设置与对比、以及大部分后续章节的内容。
- **提取质量**：提供的文本片段清晰，数学公式（尽管LaTeX渲染可能不完美）基本可读，段落结构完整，有利于对论文前半部分的理解。但基于仅1/4的文本，无法对整篇论文的方法和实验做出全面、深入的评述。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2020_A_computer-friendly.txt` (43/43 页; 原 AI 主体 12/43 + 全文补读 13-43); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-43; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-43。
- **提取情况**: 缺失页 31 页, 其中 31 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: K1,K2,K3/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
- p.13: By omitting the M24generators we obtain a normal subgroup Qand by omitting the S3
- p.13: The centralizer of xinNis calledNxand has structure
- p.13: K1/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
- p.13: K2,K3/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
- p.14: Golay codeCis given on F24
- p.16: 7 Representations of the groups Nx0,Ny0,Nz0
- p.16: In this section we construct a 196884-dimensional real monomial representation 196884xof
- p.16: Similar representations 196884yand196884zofNy0andNz0may be obtained in the same
- p.16: 7.1 Representations 98280 x,98280 y,98280 zofNx0,Ny0,Nz0
- p.16: We will use the same symbol 98280xfor that vector space and the action of the group Nx0on
- p.16: We give 98280xthe structure of an Euclidean space by assigning norm 1to all vectors Xr,

### 缺失页关键摘录

- p.17: action ofNxyz. They are permuted by the cosets of Nxyzas indicated in Table 1 for the coset
- p.17: −1are displayed in Table 1. From these kernels we see that 4096x,4096y,4096zare also
- p.17: Table 1: The kernels of and the action of S3on the subspaces of (6·2048)N
- p.18: xiandτin the following Table 2. This table also displays the kernels of these representations
- p.18: Table 2: Kernels of and action of S3on the subspaces of (3·24)N
- p.18: 196884x,196884yand196884zcan be obtained from Table 3.
- p.19: Table 3: Action of the generators of Non24x,4096xand98280x.
- p.19: entries in Table 3. E.g. from the action of zeond+
- p.19: by applying the triality operation (&↷xyz). In the sequel the phrase ”from Table 3 we obtain
- p.19: sponding basis vector with gand taking the result modulo the kernel K1.
- p.19: d·iin Table 3 is short for all d∈P,i∈˜Ωand all short basis vectors
- p.19: The following table is helpful for computing the last two columns in Table 3:
<!-- AI_READING_NOTE_END -->
