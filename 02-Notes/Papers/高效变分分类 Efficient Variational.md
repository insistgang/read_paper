---
title: "JournalofScientificComputing(2024)100:81"
authors:
  - "Xiaohao Cai"
  - "Raymond H. Chan"
  - "Xiaoyu Xie"
  - "Tieyong Zeng"
year: 2024
venue: science. In this paper, we propose an efficient and versatile multi-class semi-supervised
doi: 10.1007/s10915-024-02644-9
pdf: [[高效变分分类 Efficient Variational.pdf]]
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
extract_cache: .paper-cache/extracts/高效变分分类 Efficient Variational.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/25 pages"
---
# JournalofScientificComputing(2024)100:81

## 基本信息
- **PDF**: [[高效变分分类 Efficient Variational.pdf]]
- **primary_topic**: `N_雷达_无线电_张量_数学`
- **topics**: `N_雷达_无线电_张量_数学`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | JournalofScientificComputing(2024)100:81 |
| **作者** | Xiaohao Cai; Raymond H. Chan; Xiaoyu Xie; Tieyong Zeng |
| **发表时间** | 2024 |
| **刊物/会议** | science. In this paper, we propose an efficient and versatile multi-class semi-supervised |
| **DOI** | 10.1007/s10915-024-02644-9 |

## 摘要

> High-dimensionaldataclassificationisafundamentaltaskinmachinelearningandimaging science. In this paper, we propose an efficient and versatile multi-class semi-supervised classificationmethodforclassifyinghigh-dimensionaldataandunstructuredpointclouds. Tobeginwith,awarminitializationisgeneratedbyusingafuzzyclassificationmethodsuch as the standard support vector machine or random labeling. Then an unconstraint convex variationalmodelisproposedtopurifyandsmooththeinitialization,followedbyastepwhich istoprojectthesmoothedpartitionobtainedpreviouslytoabinarypartition.Thesestepscan berepeated,withthelatestresultasanewinitialization,tokeepimprovingtheclassification quality.Weshowthattheconvexmodelofthesmoothingstephasauniquesolutionandcan besolvedbyaspecificallydesignedprimal–dualalgorithmwhoseconvergenceisguaranteed. Wetestourmethodandcompareitwiththestate-of-the-artmethodsonseveralbenchmark datasets.Thoroughexperimentalresultsdemonstratethatourmethodissuperiorinboththe classificationaccurac

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：高维数据分类是机器学习和成像科学的基础任务。在实际应用中（如遥感、计算机视觉），数据通常具有高维特性，且标注成本高昂，因此半监督分类方法具有重要意义。
- **之前方法的问题**：现有的基于图模型的变分分类方法（如基于图割、MBO方案等）通常需要在优化模型中施加“无真空无重叠”约束（即每个点必须且只能属于一个类）。该约束导致优化问题非凸且是NP难的，计算非常耗时。即使是通过凸松弛（如单位单纯形约束）或特殊技巧（如相场表示）来近似求解，模型整体往往仍是非凸的，效率依然受限。
- **作者想解决的核心矛盾**：如何在**保证分类精度**的前提下，**大幅提升计算效率**，并**避免NP难问题**，使方法能够高效处理高维数据和点云。
## 关键贡献

1.  **提出无约束的凸变分模型**：为平滑步骤设计了一个包含数据保真项、图拉普拉斯项和图上全变分项的目标函数，该模型对于每个类别的标签函数是独立且**强凸**的，从而保证了**唯一全局最优解**，彻底规避了传统方法的NP难问题。
2.  **设计高效的两步迭代框架**：该框架将分类问题解耦为“平滑”（求解凸优化）和“二值化”（简单投影）两个步骤，并可迭代执行以逐步提升分类质量，灵活性高。
3.  **证明模型的唯一解性**：通过论证模型的强凸性，从数学上保证了所提凸优化问题解的存在性与唯一性（**定理1**）。
4.  **设计可保证收敛的优化算法**：针对所提模型设计了基于**原始-对偶（primal-dual）算法**的求解方案，并提供了收敛性保证。
5.  **实现计算效率与精度的双重提升**：由于K个子问题相互独立，**并行计算**得以直接应用，显著提升了处理大规模数据的速度。实验证明，该方法在分类精度和计算速度上均优于当前先进的变分分类方法。
6.  **方法具有通用性与鲁棒性**：框架允许使用任意快速的分类方法（如SVM、随机标签）进行初始化，且能够处理**极不平衡的数据集**，展现出良好的鲁棒性。
## 方法

- **整体框架**：方法的核心是一个**迭代过程**，包含三个关键组件：**初始化**、**平滑步骤**和**二值化步骤**。
- **输入与输出**：输入为一个包含N个点的点云（或高维数据）V，以及一个包含少量已标记点的训练集T。输出为最终的二值分类矩阵U*，满足“无真空无重叠”约束。
- **关键模块与连接**：
    1.  **初始化**：使用标准快速方法（如SVM）或随机方法生成一个**模糊分类结果**U_hat（即每个点属于各类的概率）。此结果质量要求不高。
    2.  **平滑步骤（Step One）**：这是方法的核心。通过求解一个**无约束的凸优化模型**来优化当前的模糊分类U_hat，得到更平滑的标签函数U。模型形式如下（p.7）：
        `min_U Σ_j [ (β/2) ||u_j - û_j||²_2 + (α/2) u_j^T L u_j + ||∇ u_j||_1 ]`
        - **数据保真项** `||u_j - û_j||²_2`：使优化结果不偏离当前初始化太远。
        - **图拉普拉斯项** `u_j^T L u_j`：促进标签函数的平滑性。
        - **全变分项** `||∇ u_j||_1`：促使图上特征相似的点被归为同一类。
        - 该模型对每个类别j的u_j独立求解，K个子问题无耦合约束，支持并行。
    3.  **二值化步骤（Step Two）**：将平滑步骤得到的模糊解U投影为满足约束的二值解。具体做法是对每个点x，取其标签函数中最大值对应的类别作为最终标签（公式14）。
    4.  **迭代更新**：将二值化结果作为新的初始化，重复平滑和二值化步骤，直到分类结果不再变化。为加速收敛，在迭代中会将参数β加倍。
- **数学机制的直观解释**：模型可以看作在图上进行一种“带约束的去噪”或“保结构平滑”。它试图找到一组标签函数，这些函数既要与初始的模糊猜测保持一致（保真项），又要在图的几何结构上尽可能光滑（拉普拉斯项），同时鼓励在图上相邻且相似的节点拥有相同的标签（全变分项）。由于是凸模型，优化过程高效且结果稳定。
- **推理流程**：即执行算法1的迭代过程，直至收敛。
- **与已有方法的差异**：与需在优化过程中处理非凸约束（如单位单纯形约束、类别点数约束）的传统变分方法（如[2,7,12]）不同，本方法将约束满足推迟到简单的二值化投影步骤，从而将核心优化问题转化为一个**无约束、可分离、强凸**的问题，极大简化了求解过程并提升了效率。
## 实验

- **使用的数据集**：PDF文本中提到在“几个基准数据集”上进行了测试，但具体数据集名称在提供的文本片段中未明确列出（如MNIST, COIL-20, USPS, MNIST-70k, Point Clouds等可能在第5节）。
- **对比方法**：与“state-of-the-art methods”进行比较，根据引言推测可能包括基于MBO、图割、谱方法等的变分分类方法。
- **评价指标**：主要为**分类精度（clustering accuracy）**。也应关注**计算速度**。
- **主实验结果**：PDF文本明确指出“thorough experimental results demonstrate that our method is superior in both the classification accuracy and computation speed for high-dimensional data and point clouds”（p.1）。具体数字（如准确率百分比）在提供的文本片段中未找到。
- **消融实验**：实验展示了**迭代过程**的有效性，指出分类精度会随着迭代显著提升（p.4, p.8）。例如，与首次初始化的结果相比，经过迭代后精度会有“a significant margin”的提高。
- **泛化实验**：方法不仅适用于多类分类，也被证明能处理**一类分类（one-class classification）问题**和**极不平衡数据集**（p.3），展示了其通用性。
- **效率信息**：强调模型的**计算高效性**是核心优势，因为K个子问题独立且为凸，可并行求解。文中提到“a few iterations (∼10) are generally enough in practice”（p.8）。具体的速度比较（如运行时间秒数）在提供的文本片段中未找到。
## 局限

- **对图结构的依赖**：方法的性能高度依赖于构建的图的质量，特别是权重函数（如RBF核、k-NN图）的选择和参数（如ξ, k）的设定。这些需要根据具体数据进行调优。
- **初始化敏感度**：虽然论文强调对初始化要求不高，但极端糟糕的初始化（如随机）可能需要更多迭代才能收敛，或可能收敛到次优解。
- **参数选择**：模型中有两个关键正则化参数α和β需要调整。虽然论文提到迭代时β会加倍，但其初始值以及α的设定仍需实验确定。
- **实验全面性**：基于提供的文本，无法确认是否与所有主流的最新方法进行了全面比较，以及是否在更多样化的真实世界复杂数据上进行了测试。
- **可复现性细节**：具体实现细节（如k-NN图中k的具体值、迭代终止阈值等）在提供的文本片段中未完全给出。
## 个人评论

1.  **问题分解的范式**：将困难的整体约束优化问题，巧妙地分解为一个**无约束凸优化问题**加上一个**简单的后处理投影**。这种“平滑+二值化”（SaT）的思路极具启发性，展示了如何通过分解来绕过NP难问题，在保证理论性质的同时获得实际计算效率。
2.  **对并行计算的天然友好性**：由于K个子问题完全独立，该方法可以直接应用并行计算，这在大数据时代是关键优势。这提示我们在设计模型时，考虑子问题的可分离性可以带来巨大的工程收益。
3.  **理论保证与实验效果的结合**：论文不仅提出了高效的方法，还严格证明了凸模型解的唯一性，并设计了有收敛保证的算法。这种“理论+高效算法+优越实验”的闭环，是一篇优秀计算数学或机器学习论文的典范。
4.  **框架的灵活性与鲁棒性**：初始化部分允许“即插即用”各种分类器，甚至随机初始化也能通过迭代改善，这增强了方法的实用性和鲁棒性，降低了使用门槛。

### 使用建议

- **如果快速了解**：重点阅读**摘要（Abstract）**、**引言（Introduction）** 的最后几段（总结贡献）以及**第3节（Proposed Data Classification Method）** 中的“Step one”和“Step two”描述。
- **如果复现**：需要精读**第3节（方法详解）**、**第4节（算法细节）**，特别是凸模型（15）和原始-对偶算法的更新公式（20-22）。同时需要仔细阅读**第5节（实验部分）** 获取数据集处理、参数设置和评估流程的完整信息。
- **如果借鉴创新点**：
    - **学习其“分解-迭代”的框架**：思考如何将自己研究领域中一个带有复杂约束的优化问题，分解为一个核心凸优化步骤和一个简单后处理步骤，并设计迭代策略。
    - **学习其利用问题结构（子问题独立）进行并行化**的思路。
    - **借鉴其将图拉普拉斯正则项和全变分正则项结合**来同时处理平滑性和聚类性的建模思想。
- **如果写Related Work**：可将其归类于“**图上的半监督学习**”、“**基于变分方法的分类/分割**”以及“**非凸优化的凸松弛**”这几个类别中进行引用和比较。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[N_雷达_无线电_张量_数学]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**机器学习**与**图像科学**领域的**数据分类**方向，具体聚焦于**高维数据**和**无结构点云**的**多类半监督分类**问题。它提出了一种基于图的变分方法，旨在解决传统变分分类方法中常见的非凸性和计算效率低下的核心矛盾。该论文适合放在“半监督学习”、“图上的学习”、“变分方法与优化”以及“点云处理”等相关主题下。

## 2. 一句话总结
本文提出了一种高效且通用的两步迭代变分方法：首先通过最小化一个无约束的凸优化模型来平滑和优化初始的模糊分类结果，然后将平滑结果投影为二值解，从而实现对高维数据和点云的快速、高精度分类。

## 3. 背景与问题
- **为什么要做**：高维数据分类是机器学习和成像科学的基础任务。在实际应用中（如遥感、计算机视觉），数据通常具有高维特性，且标注成本高昂，因此半监督分类方法具有重要意义。
- **之前方法的问题**：现有的基于图模型的变分分类方法（如基于图割、MBO方案等）通常需要在优化模型中施加“无真空无重叠”约束（即每个点必须且只能属于一个类）。该约束导致优化问题非凸且是NP难的，计算非常耗时。即使是通过凸松弛（如单位单纯形约束）或特殊技巧（如相场表示）来近似求解，模型整体往往仍是非凸的，效率依然受限。
- **作者想解决的核心矛盾**：如何在**保证分类精度**的前提下，**大幅提升计算效率**，并**避免NP难问题**，使方法能够高效处理高维数据和点云。

## 4. 核心贡献
1.  **提出无约束的凸变分模型**：为平滑步骤设计了一个包含数据保真项、图拉普拉斯项和图上全变分项的目标函数，该模型对于每个类别的标签函数是独立且**强凸**的，从而保证了**唯一全局最优解**，彻底规避了传统方法的NP难问题。
2.  **设计高效的两步迭代框架**：该框架将分类问题解耦为“平滑”（求解凸优化）和“二值化”（简单投影）两个步骤，并可迭代执行以逐步提升分类质量，灵活性高。
3.  **证明模型的唯一解性**：通过论证模型的强凸性，从数学上保证了所提凸优化问题解的存在性与唯一性（**定理1**）。
4.  **设计可保证收敛的优化算法**：针对所提模型设计了基于**原始-对偶（primal-dual）算法**的求解方案，并提供了收敛性保证。
5.  **实现计算效率与精度的双重提升**：由于K个子问题相互独立，**并行计算**得以直接应用，显著提升了处理大规模数据的速度。实验证明，该方法在分类精度和计算速度上均优于当前先进的变分分类方法。
6.  **方法具有通用性与鲁棒性**：框架允许使用任意快速的分类方法（如SVM、随机标签）进行初始化，且能够处理**极不平衡的数据集**，展现出良好的鲁棒性。

## 5. 方法详解
- **整体框架**：方法的核心是一个**迭代过程**，包含三个关键组件：**初始化**、**平滑步骤**和**二值化步骤**。
- **输入与输出**：输入为一个包含N个点的点云（或高维数据）V，以及一个包含少量已标记点的训练集T。输出为最终的二值分类矩阵U*，满足“无真空无重叠”约束。
- **关键模块与连接**：
    1.  **初始化**：使用标准快速方法（如SVM）或随机方法生成一个**模糊分类结果**U_hat（即每个点属于各类的概率）。此结果质量要求不高。
    2.  **平滑步骤（Step One）**：这是方法的核心。通过求解一个**无约束的凸优化模型**来优化当前的模糊分类U_hat，得到更平滑的标签函数U。模型形式如下（p.7）：
        `min_U Σ_j [ (β/2) ||u_j - û_j||²_2 + (α/2) u_j^T L u_j + ||∇ u_j||_1 ]`
        - **数据保真项** `||u_j - û_j||²_2`：使优化结果不偏离当前初始化太远。
        - **图拉普拉斯项** `u_j^T L u_j`：促进标签函数的平滑性。
        - **全变分项** `||∇ u_j||_1`：促使图上特征相似的点被归为同一类。
        - 该模型对每个类别j的u_j独立求解，K个子问题无耦合约束，支持并行。
    3.  **二值化步骤（Step Two）**：将平滑步骤得到的模糊解U投影为满足约束的二值解。具体做法是对每个点x，取其标签函数中最大值对应的类别作为最终标签（公式14）。
    4.  **迭代更新**：将二值化结果作为新的初始化，重复平滑和二值化步骤，直到分类结果不再变化。为加速收敛，在迭代中会将参数β加倍。
- **数学机制的直观解释**：模型可以看作在图上进行一种“带约束的去噪”或“保结构平滑”。它试图找到一组标签函数，这些函数既要与初始的模糊猜测保持一致（保真项），又要在图的几何结构上尽可能光滑（拉普拉斯项），同时鼓励在图上相邻且相似的节点拥有相同的标签（全变分项）。由于是凸模型，优化过程高效且结果稳定。
- **推理流程**：即执行算法1的迭代过程，直至收敛。
- **与已有方法的差异**：与需在优化过程中处理非凸约束（如单位单纯形约束、类别点数约束）的传统变分方法（如[2,7,12]）不同，本方法将约束满足推迟到简单的二值化投影步骤，从而将核心优化问题转化为一个**无约束、可分离、强凸**的问题，极大简化了求解过程并提升了效率。

## 6. 实验与结果
- **使用的数据集**：PDF文本中提到在“几个基准数据集”上进行了测试，但具体数据集名称在提供的文本片段中未明确列出（如MNIST, COIL-20, USPS, MNIST-70k, Point Clouds等可能在第5节）。
- **对比方法**：与“state-of-the-art methods”进行比较，根据引言推测可能包括基于MBO、图割、谱方法等的变分分类方法。
- **评价指标**：主要为**分类精度（clustering accuracy）**。也应关注**计算速度**。
- **主实验结果**：PDF文本明确指出“thorough experimental results demonstrate that our method is superior in both the classification accuracy and computation speed for high-dimensional data and point clouds”（p.1）。具体数字（如准确率百分比）在提供的文本片段中未找到。
- **消融实验**：实验展示了**迭代过程**的有效性，指出分类精度会随着迭代显著提升（p.4, p.8）。例如，与首次初始化的结果相比，经过迭代后精度会有“a significant margin”的提高。
- **泛化实验**：方法不仅适用于多类分类，也被证明能处理**一类分类（one-class classification）问题**和**极不平衡数据集**（p.3），展示了其通用性。
- **效率信息**：强调模型的**计算高效性**是核心优势，因为K个子问题独立且为凸，可并行求解。文中提到“a few iterations (∼10) are generally enough in practice”（p.8）。具体的速度比较（如运行时间秒数）在提供的文本片段中未找到。

## 7. 这篇论文真正有价值的地方
1.  **问题分解的范式**：将困难的整体约束优化问题，巧妙地分解为一个**无约束凸优化问题**加上一个**简单的后处理投影**。这种“平滑+二值化”（SaT）的思路极具启发性，展示了如何通过分解来绕过NP难问题，在保证理论性质的同时获得实际计算效率。
2.  **对并行计算的天然友好性**：由于K个子问题完全独立，该方法可以直接应用并行计算，这在大数据时代是关键优势。这提示我们在设计模型时，考虑子问题的可分离性可以带来巨大的工程收益。
3.  **理论保证与实验效果的结合**：论文不仅提出了高效的方法，还严格证明了凸模型解的唯一性，并设计了有收敛保证的算法。这种“理论+高效算法+优越实验”的闭环，是一篇优秀计算数学或机器学习论文的典范。
4.  **框架的灵活性与鲁棒性**：初始化部分允许“即插即用”各种分类器，甚至随机初始化也能通过迭代改善，这增强了方法的实用性和鲁棒性，降低了使用门槛。

## 8. 局限与问题
- **对图结构的依赖**：方法的性能高度依赖于构建的图的质量，特别是权重函数（如RBF核、k-NN图）的选择和参数（如ξ, k）的设定。这些需要根据具体数据进行调优。
- **初始化敏感度**：虽然论文强调对初始化要求不高，但极端糟糕的初始化（如随机）可能需要更多迭代才能收敛，或可能收敛到次优解。
- **参数选择**：模型中有两个关键正则化参数α和β需要调整。虽然论文提到迭代时β会加倍，但其初始值以及α的设定仍需实验确定。
- **实验全面性**：基于提供的文本，无法确认是否与所有主流的最新方法进行了全面比较，以及是否在更多样化的真实世界复杂数据上进行了测试。
- **可复现性细节**：具体实现细节（如k-NN图中k的具体值、迭代终止阈值等）在提供的文本片段中未完全给出。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**摘要（Abstract）**、**引言（Introduction）** 的最后几段（总结贡献）以及**第3节（Proposed Data Classification Method）** 中的“Step one”和“Step two”描述。
- **如果复现**：需要精读**第3节（方法详解）**、**第4节（算法细节）**，特别是凸模型（15）和原始-对偶算法的更新公式（20-22）。同时需要仔细阅读**第5节（实验部分）** 获取数据集处理、参数设置和评估流程的完整信息。
- **如果借鉴创新点**：
    - **学习其“分解-迭代”的框架**：思考如何将自己研究领域中一个带有复杂约束的优化问题，分解为一个核心凸优化步骤和一个简单后处理步骤，并设计迭代策略。
    - **学习其利用问题结构（子问题独立）进行并行化**的思路。
    - **借鉴其将图拉普拉斯正则项和全变分正则项结合**来同时处理平滑性和聚类性的建模思想。
- **如果写Related Work**：可将其归类于“**图上的半监督学习**”、“**基于变分方法的分类/分割**”以及“**非凸优化的凸松弛**”这几个类别中进行引用和比较。

## 10. 和其他论文的关系
基于给定的论文主题`N_雷达_无线电_张量_数学`和文件名，可能相关的论文包括：
- **图半监督分类经典方法**：如Zhu, Ghahramani, Lafferty的“Semi-Supervised Learning Using Gaussian Fields and Harmonic Functions”（基于图的谐波函数）。
- **MBO (Merriman-Bence-Osher) 扩散方法**：用于分类，如论文中引用的[7,8,13]。
- **其他基于图的变分分割模型**：如Mumford-Shah模型在图上的推广、总变分（TV）在图上的应用。
- **点云处理与深度学习**：如PointNet等网络，但本文是传统的图模型方法，可作为对比或互补。
- **原始-对偶优化算法**：如Chambolle-Pock算法。
*注：由于库中具体论文列表未知，以上为基于常见关联论文的合理推测。*

## 11. 关键词
半监督分类， 变分方法， 图拉普拉斯， 全变分， 点云分类， 凸优化， 原始-对偶算法， 迭代阈值， 高维数据， 机器学习， 图像分割

## 12. 可信度说明
本篇精读笔记**完全基于用户提供的PDF提取文本**（共12页）生成。笔记内容严格遵循了文本中的描述，未编造任何信息。对于在提供的文本片段中明确提及的内容（如模型公式、定理、算法框架、优势描述）进行了直接提炼和转述。对于文本中未明确给出的信息（如具体实验数据集名称、精确的实验结果数字、某些超参数的具体值），已在相应章节中明确标注“PDF文本中未明确说明”或根据上下文进行合理推断并注明。提供的文本质量良好，主要包含论文的框架、核心方法和理论部分，但实验结果的细节数据不完整，因此相关部分的信息相对概括。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/高效变分分类 Efficient Variational.txt` (25/25 页; 原 AI 主体 12/25 + 全文补读 13-25); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-25; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-25。
- **提取情况**: 缺失页 13 页, 其中 13 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: method TVRF [ 2] and our proposed method, respectively
- p.13: We then have
- p.13: The convergence of Algorithm 2proved in Theorem 3ensures the convergence of step
- p.13: 5 Numerical Results
- p.13: In this section, we evaluate the performance of our proposed method on four benchmark
- p.13: The COIL ,Opt- Digits ,a n d MNIST data sets can be found in the supplementary material
- p.14: Table 1 Basic properties of the
- p.14: Three Moon 3 100 1500
- p.14: COIL 6 241 1500
- p.14: Opt- Digits 10 64 5620
- p.14: MNIST 10 784 70 ,000
- p.14: To implement our method, k-NN graphs are constructed for the test data sets, using the

### 缺失页关键摘录

- p.13: In this section, we evaluate the performance of our proposed method on four benchmark
- p.13: The basic properties of these test data sets are shown in Table 1. It indicates that the number
- p.14: test benchmark data setsData set No. of classes Dim. No. of points
- p.14: each test data set. The classiﬁcation accuracy is deﬁned as the percentage of correctly labeleddata points.
- p.14: smaller initial βis required to achieve reasonable accuracy. We comment that the accuracy
- p.14: The properties shown in Table 1, including the individual points with no clear tex-
- p.15: with randomly selected labeled samples, and taking the average of the accuracies. The accu-racies of method CVM are obtained from the original paper [ 1]. The accuracy comparison is
- p.15: reported in Table 2, showing that our proposed method gives the highest accuracy; see also
- p.15: number of iterations taken for our proposed method is 3 .8. Figure 4a gives the convergence
- p.16: data set, with uniformly selectedtraining pointsMethod Accuracy (%)
- p.16: data set, with non-uniformlyselected training pointsMethod Accuracy (%)
- p.16: uniformly selected training pointsMethod Accuracy (%)
<!-- AI_READING_NOTE_END -->
