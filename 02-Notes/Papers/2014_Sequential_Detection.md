---
title: Sequential Detection of an Abrupt Change in a
authors:
  - "James Falt"
  - "Steven D. Blostein"
year: 2014
venue: "arXiv"
doi: 
pdf: [[2014_Sequential_Detection.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
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
extract_cache: .paper-cache/extracts/2014_Sequential_Detection.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/30 pages"
---
# Sequential Detection of an Abrupt Change in a

## 基本信息
- **PDF**: [[2014_Sequential_Detection.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Sequential Detection of an Abrupt Change in a |
| **作者** | James Falt; Steven D. Blostein |
| **发表时间** | 2014 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Theproblemofsequentiallydetectinganabruptchangeinasequenceofindependentandidentically distributed(IID)randomvariablesisaddressed.Whereaspreviousapproachesassumeaknownprobabil- itydensityfunction(PDF)atthestartofthesequence,theproblemaddressedisthedetectionofasingle change in distribution among a finite number of known ’equal-energy’PDFs, but where the initial and final distributions are not known a priori. A Bayesian multiple hypothesis approach is proposed where (i) unlike previous threshold policies, the minimum cost hypothesis is tracked through time, (ii) under an exponential delay-cost function that satisfies an upper bound determined by the distances between hypotheses, the probability of detecting a change from an incorrect initial distribution asymptotically vanishes with time, (iii) computation is recursive and constant per unit time, and (iv) the unknown initial state gives rise to unavoidable incorrect detections that be made to vanish with a constant test thresholdwithnegli

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：传统最快检测方法通常假设序列的初始概率密度函数（PDF）已知。然而，在许多实际应用中（如认知无线电），初始状态是未知的。如果假设的初始状态错误，检测性能会急剧下降。因此，需要研究初始状态未知情况下的变化检测问题。
- **之前方法的问题**：
    1. 绝大多数现有方法（如CUSUM及其变体、贝叶斯公式）都假设初始状态已知。
    2. 已知初始状态下的最优检测器在初始状态未知时性能会严重退化。
    3. 2-sided测试或处理多终态的方法，也均以已知初始状态为前提。
- **核心矛盾**：如何在**初始分布和变化后分布均未知**的条件下，设计一个能够有效积累信息、抑制错误初始状态假设、并快速正确检测变化的**因果（在线）顺序检测器**。
## 关键贡献

1.  **提出了针对未知初始状态的贝叶斯多假设顺序检测框架**：将问题建模为在 `D`（初始状态）+ `(n-1)D!/(D-2)!`（可能的单次变化）个假设中进行选择，并定义了初始状态错误和终态错误的事件。
2.  **设计了一套包含指数延迟成本和错误检测惩罚的结构化成本函数**：成本函数（式11-15）显式地惩罚了：
    - 检测延迟（指数成本 `a^i`）
    - 假警报（固定成本 `b`）
    - 终态误判（固定成本 `b`）
    - **初始状态误判**（与错误样本数相关的指数成本 `c^i` 和固定成本 `τ`）
3.  **实现了常数时间复杂度的递归贝叶斯风险计算**：证明了在所提成本结构下，最小风险假设可以通过跟踪一组固定数量的状态（`D + 2D!/(D-2)!`）来递归更新，每单位时间的计算量恒定，与观测序列长度 `n` 无关（见Section II尾部及[26]）。
4.  **给出了成本参数 `a` 和 `c` 的界限与设计准则**：通过分析期望风险，证明了当 `a` 和 `c` 满足特定下界时，对应于**正确初始状态**假设的风险会收敛，而对应于**错误初始状态**假设的风险会发散，从而使得错误初始状态的检测概率随时间渐近消失（Section III）。
5.  **通过模拟验证了理论分析，并展示了其性能**：模拟表明，经过一个初始瞬态期后，所提算法的平均检测延迟接近已知初始状态下的最优CUSUM检测器的性能。
## 方法

- **整体框架**：采用**贝叶斯多假设检验**的顺序决策框架。在每个时刻 `n`，算法计算所有可能假设的**后验风险**，并选择风险最小的假设作为当前决策。停止规则是：当某个变化假设 `H_{m,n}(j,k)` 的风险小于所有无变化假设 `H_{1,n}(j)` 的风险时，宣布检测到变化。
- **输入输出**：输入是顺序观测到的随机变量序列 `X_1, X_2, ...`。输出是在某个时刻 `n`，判定一个假设 `H_{m,n}(j,k)`（表示变化发生在时刻 `m`，初始分布为 `f_j`，变为 `f_k`）或 `H_{1,n}(j)`（表示未检测到变化）。
- **关键模块**：
    1.  **假设与风险定义**：定义了无变化假设 `H_{1,n}(j)` 和单次变化假设 `H_{m,n}(j,k)`，以及它们的后验风险 `R_{1,n}(j)` 和 `R_{m,n}(j,k)`（式8, 9）。
    2.  **成本结构**：这是方法的核心，通过精心设计的成本 `L(·,·)` 和 `I(·,·)`（式11-15）来引导检测器的行为。关键特性是**指数成本**。
    3.  **递归贝叶斯风险计算**：利用独立性假设，风险 `R_{1,n}(j)` 和 `R_{m,n}(j,k)` 可以通过 `R_{1,n-1}(j)` 和 `R_{m',n-1}(j,k)` 加上新观测 `x_n` 递归更新，无需重新计算全部历史数据（式16, 17, 18及后续说明）。
- **模块间连接**：新观测 `x_n` 到来后，递归模块利用它更新所有跟踪的风险值 `R_{1,n}(j)` 和 `R_{m,n}(j,k)`。然后，决策模块比较这些风险值，根据停止规则（式10）做出决策。
- **数学公式与机制直观解释**：
    - **贝叶斯风险**（式3, 8, 9）：综合了错误决策的代价和各个假设为真的后验概率。风险越小，该假设越可信。
    - **指数延迟成本 `a^i`**：强制算法在积累足够证据后尽早做出正确检测，避免不必要的拖延。
    - **指数错误初始状态成本 `c^i`**：这是针对未知初始状态的关键设计。当算法考虑一个以 `f_j` 为初始状态的假设，但真实初始状态是 `f_r` (≠`f_j`) 时，随着观测样本增加，`f_r` 和 `f_j` 分布不同所产生的“证据”会使该假设的代价 `c^i` 指数增长，从而抑制错误假设的风险。
    - **界限分析**：通过期望风险分析，`a` 和 `c` 必须大于1，且存在下界，保证正确假设的风险收敛、错误假设的风险发散，从而“排除”错误初始状态（Section III-A）。
- **推理流程**：
    1. 初始化：设定参数 `a, c, b, τ`，以及初始风险。
    2. 顺序接收观测 `x_n`。
    3. 对于每个当前跟踪的假设（`D` 个无变化假设和 `2D!/(D-2)!` 个具有最小风险变化时间 `m` 的变化假设），使用递归公式计算其新风险 `R_{1,n}(j)` 和 `R_{m,n}(j,k)`。
    4. 在所有变化假设中，找出新的最小风险 `R_{m,n}(j,k)`（式17）。
    5. 比较 `min_{(j,k)} R_{m,n}(j,k)` 和 `min_j R_{1,n}(j)`。如果前者更小，则停止并宣布检测到变化（式10）。
    6. 否则，返回步骤2。
- **和已有方法的差异**：
    - **处理未知初始状态**：与CUSUM、Page’s test等已知初始状态的检测器根本不同。
    - **多假设跟踪**：不仅检测变化是否发生，还同时估计变化时刻 `m`、初始分布 `j` 和终态分布 `k`。
    - **成本驱动**：不是基于似然比或统计量阈值，而是基于结构化的后验风险最小化。
    - **递归计算**：虽然假设数量随时间增长，但通过跟踪最小风险时间 `m`，将状态数量固定下来，实现了常数复杂度。
## 实验

- **使用的数据集**：PDF文本中提到使用了“Monte Carlo simulations”（第IV节，p.10）。但**提供的文本中未明确说明具体的仿真数据集或生成数据的分布细节**。
- **对比方法**：PDF文本中提到“draws performance comparisons to optimal one-sided quickest detection methods for known initial state [11][12]”（p.10）。具体为与已知初始状态下的最优CUSUM检测器进行对比。
- **评价指标**：**PDF文本中未明确列出具体的性能评价指标**，但根据上下文推断，应包括平均检测延迟（Average Detection Delay）和错误检测概率（Probability of Incorrect Detection）。
- **主实验结果**：**提供的文本中未包含任何具体的实验结果数字或图表**。仅摘要和引言中描述性提到：“average delay approaches that of the optimal CUSUM test after an initial transient period”。
- **消融实验**：**PDF文本中未提及消融实验**。
- **泛化实验**：**PDF文本中未提及泛化实验**。
- **效率信息**：**PDF文本中未提供关于速度、参数量或FLOPs的具体信息**。但算法被描述为“computation is recursive and constant per unit time”（p.1）。
## 局限

1.  **强假设**：假设所有候选PDF是“equal-energy”（等能量，即 `E[fj(X)]` 相同），这限制了应用场景。论文未说明如果此条件不满足会怎样。
2.  **参数选择**：算法依赖于参数 `a`, `b`, `c`, `τ` 的选择。虽然论文给出了参数下界理论分析，但实际应用中如何在这些界限内选取最优参数以达到期望的延迟-误报率权衡，仍是一个挑战，可能需要先验知识或调参。
3.  **计算复杂度**：虽然每步计算复杂度是常数 `O(D^2)`，但随着候选分布数量 `D` 的增加，需要跟踪的状态数 `D + 2D!/(D-2)!` 会快速增长，可能限制其在 `D` 很大时的应用。
4.  **验证不充分**：从提供的文本看，实验部分似乎仅限于Monte Carlo模拟，缺乏在真实世界数据集上的验证，其实用性和鲁棒性有待考察。
5.  **对分布的依赖**：性能（如延迟）取决于分布间的“距离”（体现在 `d_i(j,k)` 中）。如果分布非常接近，检测会非常困难。
## 个人评论

1.  **问题定义本身**：首次系统地研究了初始状态和终态都未知的单次变化顺序检测问题，并给出了严谨的数学公式化，为后续研究设定了框架。
2.  **成本结构设计思想**：巧妙利用**指数成本**来惩罚延迟和特定类型的错误（初始状态误判）。通过设置足够高的基数（`a`, `c`），可以在数学上保证不期望的假设（如错误初始状态）的风险发散，从而被“淘汰”。这种将“渐近性能保证”编码进成本函数的思想非常强大。
3.  **递归贝叶斯风险实现**：展示了在复杂的多假设、成本依赖历史的情况下，如何通过固定状态数实现高效递归算法，这为在线贝叶斯决策提供了可行范例。
4.  **对后续研究的启发**：该论文启发研究者，在面对模型不确定性（如初始状态未知）时，可以通过**设计合适的损失函数**来显式地约束和引导学习/检测过程，而不必直接估计不确定的参数。

### 使用建议

- **如果快速了解**：只读 **Abstract**、**Section I (Introduction)** 的最后几段（介绍本文方法的部分）以及 **Section II** 的开头部分（问题建模）。
- **如果复现**：重点看 **Section II** 的全部内容，特别是成本结构定义（式11-15）和风险递归更新公式（式16-18）。同时需要参考其引用的技术报告[26]以获取完整的递归细节。
- **如果借鉴创新点**：
    - 学习其**将不确定参数的负面影响转化为成本函数设计**的思路。
    - 学习其**使用指数成本来获得渐近性能保证**的方法。
    - 学习其**在多假设框架下实现常数复杂度递归**的技巧。
- **如果写 Related Work**：可将本文归类为 **“未知初始状态的变化检测”** 或 **“贝叶斯顺序假设检验”**，与经典的CUSUM、Shiryaev-Roberts方法以及处理多终态的2-sided测试并列讨论。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**统计信号处理**中的**顺序变化检测**方向。它解决的核心问题是：在一系列独立同分布的随机变量中，当序列的**初始分布**和**变化后的最终分布都未知**时，如何快速、准确地检测出一个单一的分布变化。该问题适合放在**变化检测**、**顺序分析**或**假设检验**等主题下。其应用场景例如认知无线电中信号存在与否的检测。

## 2. 一句话总结
针对初始和最终分布都未知的随机序列，该论文提出了一种贝叶斯多假设顺序检测方法，通过递归计算后验风险并采用指数延迟成本结构，使得错误初始状态的检测概率随时间渐近消失。

## 3. 背景与问题
- **为什么要做**：传统最快检测方法通常假设序列的初始概率密度函数（PDF）已知。然而，在许多实际应用中（如认知无线电），初始状态是未知的。如果假设的初始状态错误，检测性能会急剧下降。因此，需要研究初始状态未知情况下的变化检测问题。
- **之前方法的问题**：
    1. 绝大多数现有方法（如CUSUM及其变体、贝叶斯公式）都假设初始状态已知。
    2. 已知初始状态下的最优检测器在初始状态未知时性能会严重退化。
    3. 2-sided测试或处理多终态的方法，也均以已知初始状态为前提。
- **核心矛盾**：如何在**初始分布和变化后分布均未知**的条件下，设计一个能够有效积累信息、抑制错误初始状态假设、并快速正确检测变化的**因果（在线）顺序检测器**。

## 4. 核心贡献
1.  **提出了针对未知初始状态的贝叶斯多假设顺序检测框架**：将问题建模为在 `D`（初始状态）+ `(n-1)D!/(D-2)!`（可能的单次变化）个假设中进行选择，并定义了初始状态错误和终态错误的事件。
2.  **设计了一套包含指数延迟成本和错误检测惩罚的结构化成本函数**：成本函数（式11-15）显式地惩罚了：
    - 检测延迟（指数成本 `a^i`）
    - 假警报（固定成本 `b`）
    - 终态误判（固定成本 `b`）
    - **初始状态误判**（与错误样本数相关的指数成本 `c^i` 和固定成本 `τ`）
3.  **实现了常数时间复杂度的递归贝叶斯风险计算**：证明了在所提成本结构下，最小风险假设可以通过跟踪一组固定数量的状态（`D + 2D!/(D-2)!`）来递归更新，每单位时间的计算量恒定，与观测序列长度 `n` 无关（见Section II尾部及[26]）。
4.  **给出了成本参数 `a` 和 `c` 的界限与设计准则**：通过分析期望风险，证明了当 `a` 和 `c` 满足特定下界时，对应于**正确初始状态**假设的风险会收敛，而对应于**错误初始状态**假设的风险会发散，从而使得错误初始状态的检测概率随时间渐近消失（Section III）。
5.  **通过模拟验证了理论分析，并展示了其性能**：模拟表明，经过一个初始瞬态期后，所提算法的平均检测延迟接近已知初始状态下的最优CUSUM检测器的性能。

## 5. 方法详解
- **整体框架**：采用**贝叶斯多假设检验**的顺序决策框架。在每个时刻 `n`，算法计算所有可能假设的**后验风险**，并选择风险最小的假设作为当前决策。停止规则是：当某个变化假设 `H_{m,n}(j,k)` 的风险小于所有无变化假设 `H_{1,n}(j)` 的风险时，宣布检测到变化。
- **输入输出**：输入是顺序观测到的随机变量序列 `X_1, X_2, ...`。输出是在某个时刻 `n`，判定一个假设 `H_{m,n}(j,k)`（表示变化发生在时刻 `m`，初始分布为 `f_j`，变为 `f_k`）或 `H_{1,n}(j)`（表示未检测到变化）。
- **关键模块**：
    1.  **假设与风险定义**：定义了无变化假设 `H_{1,n}(j)` 和单次变化假设 `H_{m,n}(j,k)`，以及它们的后验风险 `R_{1,n}(j)` 和 `R_{m,n}(j,k)`（式8, 9）。
    2.  **成本结构**：这是方法的核心，通过精心设计的成本 `L(·,·)` 和 `I(·,·)`（式11-15）来引导检测器的行为。关键特性是**指数成本**。
    3.  **递归贝叶斯风险计算**：利用独立性假设，风险 `R_{1,n}(j)` 和 `R_{m,n}(j,k)` 可以通过 `R_{1,n-1}(j)` 和 `R_{m',n-1}(j,k)` 加上新观测 `x_n` 递归更新，无需重新计算全部历史数据（式16, 17, 18及后续说明）。
- **模块间连接**：新观测 `x_n` 到来后，递归模块利用它更新所有跟踪的风险值 `R_{1,n}(j)` 和 `R_{m,n}(j,k)`。然后，决策模块比较这些风险值，根据停止规则（式10）做出决策。
- **数学公式与机制直观解释**：
    - **贝叶斯风险**（式3, 8, 9）：综合了错误决策的代价和各个假设为真的后验概率。风险越小，该假设越可信。
    - **指数延迟成本 `a^i`**：强制算法在积累足够证据后尽早做出正确检测，避免不必要的拖延。
    - **指数错误初始状态成本 `c^i`**：这是针对未知初始状态的关键设计。当算法考虑一个以 `f_j` 为初始状态的假设，但真实初始状态是 `f_r` (≠`f_j`) 时，随着观测样本增加，`f_r` 和 `f_j` 分布不同所产生的“证据”会使该假设的代价 `c^i` 指数增长，从而抑制错误假设的风险。
    - **界限分析**：通过期望风险分析，`a` 和 `c` 必须大于1，且存在下界，保证正确假设的风险收敛、错误假设的风险发散，从而“排除”错误初始状态（Section III-A）。
- **推理流程**：
    1. 初始化：设定参数 `a, c, b, τ`，以及初始风险。
    2. 顺序接收观测 `x_n`。
    3. 对于每个当前跟踪的假设（`D` 个无变化假设和 `2D!/(D-2)!` 个具有最小风险变化时间 `m` 的变化假设），使用递归公式计算其新风险 `R_{1,n}(j)` 和 `R_{m,n}(j,k)`。
    4. 在所有变化假设中，找出新的最小风险 `R_{m,n}(j,k)`（式17）。
    5. 比较 `min_{(j,k)} R_{m,n}(j,k)` 和 `min_j R_{1,n}(j)`。如果前者更小，则停止并宣布检测到变化（式10）。
    6. 否则，返回步骤2。
- **和已有方法的差异**：
    - **处理未知初始状态**：与CUSUM、Page’s test等已知初始状态的检测器根本不同。
    - **多假设跟踪**：不仅检测变化是否发生，还同时估计变化时刻 `m`、初始分布 `j` 和终态分布 `k`。
    - **成本驱动**：不是基于似然比或统计量阈值，而是基于结构化的后验风险最小化。
    - **递归计算**：虽然假设数量随时间增长，但通过跟踪最小风险时间 `m`，将状态数量固定下来，实现了常数复杂度。

## 6. 实验与结果
- **使用的数据集**：PDF文本中提到使用了“Monte Carlo simulations”（第IV节，p.10）。但**提供的文本中未明确说明具体的仿真数据集或生成数据的分布细节**。
- **对比方法**：PDF文本中提到“draws performance comparisons to optimal one-sided quickest detection methods for known initial state [11][12]”（p.10）。具体为与已知初始状态下的最优CUSUM检测器进行对比。
- **评价指标**：**PDF文本中未明确列出具体的性能评价指标**，但根据上下文推断，应包括平均检测延迟（Average Detection Delay）和错误检测概率（Probability of Incorrect Detection）。
- **主实验结果**：**提供的文本中未包含任何具体的实验结果数字或图表**。仅摘要和引言中描述性提到：“average delay approaches that of the optimal CUSUM test after an initial transient period”。
- **消融实验**：**PDF文本中未提及消融实验**。
- **泛化实验**：**PDF文本中未提及泛化实验**。
- **效率信息**：**PDF文本中未提供关于速度、参数量或FLOPs的具体信息**。但算法被描述为“computation is recursive and constant per unit time”（p.1）。

## 7. 这篇论文真正有价值的地方
1.  **问题定义本身**：首次系统地研究了初始状态和终态都未知的单次变化顺序检测问题，并给出了严谨的数学公式化，为后续研究设定了框架。
2.  **成本结构设计思想**：巧妙利用**指数成本**来惩罚延迟和特定类型的错误（初始状态误判）。通过设置足够高的基数（`a`, `c`），可以在数学上保证不期望的假设（如错误初始状态）的风险发散，从而被“淘汰”。这种将“渐近性能保证”编码进成本函数的思想非常强大。
3.  **递归贝叶斯风险实现**：展示了在复杂的多假设、成本依赖历史的情况下，如何通过固定状态数实现高效递归算法，这为在线贝叶斯决策提供了可行范例。
4.  **对后续研究的启发**：该论文启发研究者，在面对模型不确定性（如初始状态未知）时，可以通过**设计合适的损失函数**来显式地约束和引导学习/检测过程，而不必直接估计不确定的参数。

## 8. 局限与问题
1.  **强假设**：假设所有候选PDF是“equal-energy”（等能量，即 `E[fj(X)]` 相同），这限制了应用场景。论文未说明如果此条件不满足会怎样。
2.  **参数选择**：算法依赖于参数 `a`, `b`, `c`, `τ` 的选择。虽然论文给出了参数下界理论分析，但实际应用中如何在这些界限内选取最优参数以达到期望的延迟-误报率权衡，仍是一个挑战，可能需要先验知识或调参。
3.  **计算复杂度**：虽然每步计算复杂度是常数 `O(D^2)`，但随着候选分布数量 `D` 的增加，需要跟踪的状态数 `D + 2D!/(D-2)!` 会快速增长，可能限制其在 `D` 很大时的应用。
4.  **验证不充分**：从提供的文本看，实验部分似乎仅限于Monte Carlo模拟，缺乏在真实世界数据集上的验证，其实用性和鲁棒性有待考察。
5.  **对分布的依赖**：性能（如延迟）取决于分布间的“距离”（体现在 `d_i(j,k)` 中）。如果分布非常接近，检测会非常困难。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读 **Abstract**、**Section I (Introduction)** 的最后几段（介绍本文方法的部分）以及 **Section II** 的开头部分（问题建模）。
- **如果复现**：重点看 **Section II** 的全部内容，特别是成本结构定义（式11-15）和风险递归更新公式（式16-18）。同时需要参考其引用的技术报告[26]以获取完整的递归细节。
- **如果借鉴创新点**：
    - 学习其**将不确定参数的负面影响转化为成本函数设计**的思路。
    - 学习其**使用指数成本来获得渐近性能保证**的方法。
    - 学习其**在多假设框架下实现常数复杂度递归**的技巧。
- **如果写 Related Work**：可将本文归类为 **“未知初始状态的变化检测”** 或 **“贝叶斯顺序假设检验”**，与经典的CUSUM、Shiryaev-Roberts方法以及处理多终态的2-sided测试并列讨论。

## 10. 和其他论文的关系
根据论文内容和引用，它与以下方向或论文密切相关：
- 与Page的**CUSUM**检测器[[8]]、Lorden的**minimax**最优性结果[[9]]以及Moustakides的**最优平均延迟**结果[[11]]是经典已知初始状态变化检测的基础，本文是其在未知初始状态下的扩展和对比基线。
- 与处理**多分布变化**或**ON-OFF过程**的论文[[13]]相关，但本文强调初始状态未知。
- 与贝叶斯变化检测的**指数延迟成本**模型[[24]]相关，本文扩展了其成本结构以涵盖初始状态不确定性。
- 应用上与**认知无线电**中的频谱感知[[6][7]]直接相关，其中初始状态未知是一个核心难题。

## 11. 关键词
顺序检测, 变化检测, 未知初始状态, 贝叶斯假设检验, 后验风险, 指数成本, 递归算法, 最小风险, 平均检测延迟, 错误检测概率, 认知无线电

## 12. 可信度说明
本笔记主要基于提供的PDF文本前12页内容生成，涵盖了摘要、引言、问题公式化（Section II）、成本参数分析（Section III的一部分）以及实验描述的起始部分。**关键的贡献、方法框架、数学公式和理论分析都基于此文本**。然而，由于PDF提取不完整（仅前12页/共30页），以下信息在提供的文本中**未找到或不明确**：
- 完整的模拟实验设置、具体结果和图表（应位于Section IV）。
- 成本参数界限的完整证明（应位于Section III）。
- 完整的递归算法伪代码（应在技术报告[26]或附录中）。
因此，关于“实验与结果”一节的内容非常有限。笔记的其余部分均严格依据所提供的文本进行总结和阐释。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2017 字符/页)); 来源缓存: `.paper-cache/extracts/2014_Sequential_Detection.txt` (30/30 页; 原 AI 主体 12/30 + 全文补读 13-30); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-30; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-30。
- **提取情况**: 缺失页 18 页, 其中 18 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: Next, we need to establish
- p.14: Rm,n(j,k)P(X1,n)/bracketrightbig
- p.14: We then have
- p.16: For any particular risk corresponding to change, when the re cursively tracked time is small,
- p.16: DKL/parenleftbig
- p.16: In Theorem 2, a value of the minimum change time (32) is used to showcase performance
- p.17: Nevertheless, from Theorem 2, there exists an irreducible m inimum change time required for
- p.19: For the PDFs (35) and parameter values selected in Section IV -A, Figures 1, 2, and 3 plot
- p.19: From Figure 1 it is clear that average detection delay increa ses for any given change time
- p.20: Change TimeAverage Detection Delay
- p.20: CUSUM
- p.20: Figure 3 shows the false alarm rates achieved by the proposed change detection scheme for

### 缺失页关键摘录

- p.14: cost function deﬁnition. It can similarly be shown that choo sing1<c<d minwill result in the
- p.18: compared with observed results and trends. Finally, Sectio n IV-D provides summary discussion.
- p.18: requires knowledge of the change time, which is unrealizabl e, this is only used as a benchmark;
- p.19: From Figure 1 it is clear that average detection delay increa ses for any given change time
- p.19: Observing Figure 2, it is clear that each value of τachieve a minimum probability of incorrect
- p.20: Figure 3 shows the false alarm rates achieved by the proposed change detection scheme for
- p.22: for CUSUM in Figure 3 is there to justify the selected CUSUM th reshold of 102.157for the
- p.22: presented in the proof of Theorem 2. As pointed out previousl y from Figure 2, once the initial
- p.23: with Figure 2, (36) is a loose upper bound: incorrect detecti on probabilities for τ= 101and
- p.24: from Figure 2 it can be observed that, for each value of τ, the incorrect detection rate achieved
- p.30: [6] J. K. Liang and S. Blostein, “Performance evaluation of m ultiband multi-sensor spectrum sensing systems,” in IEEE
<!-- AI_READING_NOTE_END -->
