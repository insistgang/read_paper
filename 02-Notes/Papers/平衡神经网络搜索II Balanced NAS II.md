---
title: Balanced Neural Architecture Search and Its
authors:
  - "Mingyang Du"
  - "Xikai He"
  - "Xiaohao Cai"
  - "Daping Bi"
year: 2021
venue: posed balanced-NAS framework, a “block-cell” structure and a
doi: 10.1109/TSP.2021.3107633
pdf: [[平衡神经网络搜索II Balanced NAS II.pdf]]
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/平衡神经网络搜索II Balanced NAS II.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# Balanced Neural Architecture Search and Its

## 基本信息
- **PDF**: [[平衡神经网络搜索II Balanced NAS II.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Balanced Neural Architecture Search and Its |
| **作者** | Mingyang Du; Xikai He; Xiaohao Cai; Daping Bi |
| **发表时间** | 2021 |
| **刊物/会议** | posed balanced-NAS framework, a “block-cell” structure and a |
| **DOI** | 10.1109/TSP.2021.3107633 |

## 摘要

> —Theperformanceofasingleneuralnetworkcanvary performance[3].Therefore,SEIinthecomplexelectromagnetic unexpectedly corresponding to different classification tasks, and environmentisinherentlyanurgentandextremelychallenging thus the network with fixed structure may lack flexibility and problem. In this paper, we endeavor to propose new efficient oftenleadtooverfittingorunderfitting.Itisurgent,alsothemain methods to pave the way for SEI in complex electromagnetic objective of this paper, to deal with the limitation of the fixed neuralnetworkstructureonclassifyingradarsignalsindifferent environments. electromagneticenvironments.Weinthispaperproposeavariable Pulse description word [4] is one of the most common and network architecture search (NAS) mechanism, called balanced- easiest ways to describe radar signal inter-pulse characteris- NASframework,andapplyitinspecificemitteridentification(SEI) ticswhichmainlygatherparametersincludingradiofrequency to greatly improve the flexibility of mod

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：特定辐射源识别（SEI）在军事和民用领域至关重要，但日益复杂的空间频谱（如传感器缺陷、低信噪比环境）使得传统方法和固定结构的深度学习模型（如CNN）表现不稳定。针对不同电磁环境手动设计最优网络结构既耗时又易出错。
- **之前方法有什么问题**：1）传统分类器（如SVM、KNN）表达能力有限；2）现成的深度学习模型（如ResNet、Inception）虽然有效，但其结构是固定的，无法根据输入数据的复杂度（如不同SNR）自适应调整，导致在小数据集或低SNR下可能过拟合且浪费计算资源；3）已有的NAS方法（如基于强化学习或进化算法）能自动搜索网络，但通常需要巨大的计算资源（如数千GPU小时），在SEI应用场景中不现实。
- **作者想解决的核心矛盾**：**固定结构的神经网络与变化多端（特别是噪声水平不同）的电磁环境数据之间的不匹配**。需要一种能够根据具体环境自动“定制”兼具高准确率和高效率的网络结构的机制。
## 关键贡献

1.  **提出了一个可变的NAS框架——balanced-NAS**：基于“块-单元”模式构建搜索空间，能自动生成针对不同电磁环境优化的网络结构，显著提升了模型搜索的灵活性。
2.  **提出了一个新颖的平衡函数（Balance Function）**：在NAS过程中，该函数同时考虑**验证精度**和**计算开销**（以网络可训练参数量为度量），引导控制器选择出在精度和效率上都最优的网络结构。
3.  **采用了渐进式搜索策略（Progressive Strategy）**：从简单模型（单元内块数少）开始搜索，逐步增加复杂度（增加块数），并在每个评估阶段淘汰没有前途的候选模型，从而释放搜索空间，大幅提升搜索效率。
4.  **在SEI任务上进行了全面验证**：构建了一个包含七类常用雷达信号（包括相似时频特征的LFM和多相码）且添加了不同噪声程度的数据集，实验结果表明所提方法能设计出兼具最高准确率和最低计算成本的优化模型。
## 方法

- **整体框架**：balanced-NAS的框架类似于经典的基于强化学习的NAS（图3），核心是一个基于RNN的**控制器（Controller）**。控制器从预定义的搜索空间中采样生成**子网络（child model）** 的架构描述。子网络在训练数据上训练并得到验证精度，该精度作为奖励信号通过**策略梯度**方法更新控制器。本文的关键创新在于控制器受**平衡函数**调控，且搜索空间基于**可变的块-单元结构**。
- **输入输出**：
    - **系统输入**：经过预处理（如去交织）的原始雷达信号，通过STFT转换为二维**时频分布图像**。
    - **最终输出**：雷达信号所属的发射器类别。
- **关键模块**：
    1.  **“块-单元”结构**：这是搜索空间的基本定义。一个**块（Block）** 是一个包含五个元组 `(I1, I2, O1, O2, C)` 的操作单元，其中 `I1`, `I2` 是输入张量，`O1`, `O2` 是卷积等操作，`C` 是结合操作（相加或拼接）。一个**单元（Cell）** 由固定数量 `B` 个这样的块堆叠而成。一个完整的网络由多个这样的单元堆叠构成。**搜索的目标就是最优的单元结构**。
    2.  **基于RNN的控制器**：用于生成候选网络架构。它逐步预测单元内每个块的输入源、操作类型和结合方式，概率性地采样出架构。
    3.  **平衡函数（Balance Function）**：这是本文的核心创新机制。它作用于控制器的输出，旨在平衡**验证精度（`R_acc`）** 和**计算效率（`R_param`，用参数量衡量）**。其目的是激励控制器生成那些在准确率足够高的前提下，参数量尽可能少的网络结构。
    4.  **渐进式搜索策略**：不同于从复杂网络直接搜索，本文从最简单的单元结构（例如每个单元只有1个块，`B=1`）开始。评估并保留表现好的模型后，再将搜索扩展到更复杂的结构（例如`B=2`），同时剪枝掉表现不佳的候选模型。这有效缩小了搜索空间，加速了过程。
- **数学公式或机制的直观解释**：STFT将时域信号`u(mT)`转换为时频表示`X(mT, f)`（公式2），生成用于分类的图像特征。平衡函数的具体数学形式在提供的PDF文本中未明确给出，但其作用机制直观上是将精度和参数量这两个目标结合成一个单一的奖励信号，指导控制器的更新方向。
- **训练方式**：采用强化学习训练控制器。控制器采样多个子网络架构 -> 每个子网络在训练集上从头训练 -> 用验证精度（结合平衡函数）作为奖励 -> 使用策略梯度算法（如PPO）更新控制器参数，使其更倾向于采样出高奖励（即高精度、低参数量）的架构。
- **推理流程**：搜索阶段结束后，控制器输出一个最终的、确定的单元结构。用此结构构建完整网络，在全部训练数据上重新训练至收敛，得到最终模型用于雷达信号分类。
- **和已有方法的差异**：
    - 与手动设计网络相比：自动化，能适应不同环境。
    - 与标准NAS（如[27]）相比：引入了平衡函数进行多目标优化，而非仅追求精度；采用了渐进策略，大幅减少计算开销。
    - 与ENAS（[28]）相比：不仅使用参数共享，更核心的是引入了平衡函数和渐进搜索策略。
    - 与PNAS（[30]）相比：类似渐进思想，但本文是针对SEI任务，并增加了平衡函数来协调精度和计算成本。
## 实验

- **使用的数据集**：论文自建了一个雷达信号数据集，包含**7类**常用雷达信号：具有正斜率和负斜率的线性调频（LFM）、正弦频率调制、以及P1、P2、P3、P4多相码。数据集包含了不同信噪比（SNR）条件下的样本，图2展示了噪声自由和SNR=-10dB下的时频图像对比。
- **对比方法**：文中提及作为背景的对比方法包括传统分类器（SVM， KNN， 随机森林）和其他NAS方法（ENAS[28], NASH[29], PNAS[30]）。实验部分的具体对比算法在提供的PDF前12页中未完整列出。
- **评价指标**：主要指标是**分类准确率（Validation Accuracy）** 和**计算成本（以网络可训练参数量`R_param`度量）**。平衡函数正是围绕这两个指标设计的。
- **主实验结果**：从摘要和引言的结论可知，实验表明该方法是“极其高效”的，并且在不同环境下分类雷达信号时“优于传统算法”。具体的关键数字（如最终准确率）在提供的文本中未明确列出。
- **消融实验**：文中明确提到“different effects of the block and cell are tested and compared in the experiment”，表明对模块（块和单元）的作用进行了消融分析，以指导如何增加网络复杂度来应对更困难的任务。
- **泛化实验**：通过在不同SNR环境下进行实验，验证了方法对不同电磁环境（数据集分布变化）的适应性和泛化能力。
- **速度/参数量/FLOPs等效率信息**：论文将**可训练参数量**作为计算成本的主要代理指标。平衡函数的目标之一就是最小化这个指标。文中强调该方法能在达到最先进准确率的同时，“承担最廉价的计算成本”。
## 局限

- **方法假设依赖**：整个方法严重依赖于STFT生成的时频图像作为特征输入。对于某些时频分析效果不佳的信号调制类型，方法可能受限。
- **实验范围**：数据集仅包含7类雷达信号，虽然包含了具有相似特征的类别（如多种多相码），但相对于真实复杂的电磁环境，其规模和多样性仍然有限。对更广泛信号类型和极端环境的泛化能力有待进一步验证。
- **计算成本**：虽然通过渐进策略和平衡函数大幅优化，但NAS过程本质上仍然需要训练和评估多个子网络，其计算开销远大于手动设计并训练单个网络。论文未提供搜索过程的具体耗时和GPU资源使用量。
- **平衡函数的具体形式未充分揭示**：在提供的文本中，平衡函数的核心思想清晰，但其具体的数学公式和超参数设置未明确说明，这增加了复现的难度。
- **对比基线的完整性**：提供的文本中未详细列出最终实验对比的所有具体算法及其完整结果，难以全面评估其相对于最新SOTA方法的优势程度。
## 个人评论

1.  **问题驱动的NAS设计**：它不是简单地将通用NAS应用到SEI，而是深刻分析了SEI任务的特点（数据集因环境而变、对计算成本敏感），并据此设计了**平衡函数**。这为如何针对特定领域约束定制NAS目标函数提供了优秀范例。
2.  **多目标优化的实用框架**：在深度学习模型部署时，精度和效率（参数量、延迟）的权衡是永恒课题。本文提出的在搜索阶段就引入平衡函数来优化这一对矛盾的思路，具有普适的启发意义。
3.  **高效的搜索策略**：渐进式搜索策略结合剪枝，是降低NAS计算门槛的有效实践，尤其适合资源有限的实验室或工业应用场景。
4.  **对SEI任务的深入洞察**：论文清晰地指出了SEI与一般图像分类的区别，并通过实验证明了为不同“难度”（由噪声、信号相似度定义）的SEI子任务定制不同复杂度网络的必要性和可行性。

### 使用建议

- **如果快速了解**：重点阅读**Abstract**、**Introduction**（特别是末尾的贡献列表）、**Section IV (Balanced-NAS Framework)** 和 **Section VI (Experiments)** 的开头部分。
- **如果复现**：需要仔细研读 **Section IV**（块-单元结构定义、控制器设计）、**Section V**（平衡函数的构建，需寻找论文完整版）和 **Section VI**（实验设置、数据集构建、训练细节）。同时需要参考其引用的早期NAS工作（如[27]）来理解基础框架。
- **如果借鉴创新点**：
    - 借鉴 **“平衡函数”** 的思想：在自己的NAS或多目标优化任务中，设计一个将业务关键指标（如延迟、能耗、存储）与精度相结合的奖励或损失函数。
    - 借鉴 **“渐进式搜索”** 策略：在搜索复杂结构时，从简单结构开始逐步扩展，可以提升效率。
    - 借鉴 **“针对任务特点定制NAS”** 的思路：在应用NAS到新领域前，先分析该领域数据与任务的独特之处（如SEI的环境可变性）。
- **如果写related work**：可以将其放在以下几类中：
    - **NAS在特定领域的应用**（尤其是信号处理、雷达、通信领域）。
    - **高效的NAS方法**（涉及搜索策略加速，如渐进搜索）。
    - **多目标/多准则NAS**（同时优化精度和效率）。
    - **基于深度学习的特定辐射源识别（SEI）**。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于神经网络架构搜索（Neural Architecture Search, NAS）在信号处理领域的应用研究，具体聚焦于**特定辐射源识别（Specific Emitter Identification, SEI）** 任务。它旨在解决在不同电磁环境（特别是不同信噪比水平）下，使用固定结构的神经网络进行雷达信号分类时灵活性不足、容易过拟合或欠拟合的问题。这篇论文可以归类于 **“神经网络架构搜索”** 和 **“雷达信号处理与分类”** 的交叉主题下。

## 2. 一句话总结
本文提出了一个名为**平衡NAS（balanced-NAS）** 的框架，通过基于“块-单元”（block-cell）的可变网络结构和创新的**平衡函数**，自动搜索并生成在验证精度和计算开销之间达到最优平衡的神经网络，以适应复杂多变的电磁环境下的特定辐射源识别任务。

## 3. 背景与问题
- **这篇论文为什么要做**：特定辐射源识别（SEI）在军事和民用领域至关重要，但日益复杂的空间频谱（如传感器缺陷、低信噪比环境）使得传统方法和固定结构的深度学习模型（如CNN）表现不稳定。针对不同电磁环境手动设计最优网络结构既耗时又易出错。
- **之前方法有什么问题**：1）传统分类器（如SVM、KNN）表达能力有限；2）现成的深度学习模型（如ResNet、Inception）虽然有效，但其结构是固定的，无法根据输入数据的复杂度（如不同SNR）自适应调整，导致在小数据集或低SNR下可能过拟合且浪费计算资源；3）已有的NAS方法（如基于强化学习或进化算法）能自动搜索网络，但通常需要巨大的计算资源（如数千GPU小时），在SEI应用场景中不现实。
- **作者想解决的核心矛盾**：**固定结构的神经网络与变化多端（特别是噪声水平不同）的电磁环境数据之间的不匹配**。需要一种能够根据具体环境自动“定制”兼具高准确率和高效率的网络结构的机制。

## 4. 核心贡献
1.  **提出了一个可变的NAS框架——balanced-NAS**：基于“块-单元”模式构建搜索空间，能自动生成针对不同电磁环境优化的网络结构，显著提升了模型搜索的灵活性。
2.  **提出了一个新颖的平衡函数（Balance Function）**：在NAS过程中，该函数同时考虑**验证精度**和**计算开销**（以网络可训练参数量为度量），引导控制器选择出在精度和效率上都最优的网络结构。
3.  **采用了渐进式搜索策略（Progressive Strategy）**：从简单模型（单元内块数少）开始搜索，逐步增加复杂度（增加块数），并在每个评估阶段淘汰没有前途的候选模型，从而释放搜索空间，大幅提升搜索效率。
4.  **在SEI任务上进行了全面验证**：构建了一个包含七类常用雷达信号（包括相似时频特征的LFM和多相码）且添加了不同噪声程度的数据集，实验结果表明所提方法能设计出兼具最高准确率和最低计算成本的优化模型。

## 5. 方法详解
- **整体框架**：balanced-NAS的框架类似于经典的基于强化学习的NAS（图3），核心是一个基于RNN的**控制器（Controller）**。控制器从预定义的搜索空间中采样生成**子网络（child model）** 的架构描述。子网络在训练数据上训练并得到验证精度，该精度作为奖励信号通过**策略梯度**方法更新控制器。本文的关键创新在于控制器受**平衡函数**调控，且搜索空间基于**可变的块-单元结构**。
- **输入输出**：
    - **系统输入**：经过预处理（如去交织）的原始雷达信号，通过STFT转换为二维**时频分布图像**。
    - **最终输出**：雷达信号所属的发射器类别。
- **关键模块**：
    1.  **“块-单元”结构**：这是搜索空间的基本定义。一个**块（Block）** 是一个包含五个元组 `(I1, I2, O1, O2, C)` 的操作单元，其中 `I1`, `I2` 是输入张量，`O1`, `O2` 是卷积等操作，`C` 是结合操作（相加或拼接）。一个**单元（Cell）** 由固定数量 `B` 个这样的块堆叠而成。一个完整的网络由多个这样的单元堆叠构成。**搜索的目标就是最优的单元结构**。
    2.  **基于RNN的控制器**：用于生成候选网络架构。它逐步预测单元内每个块的输入源、操作类型和结合方式，概率性地采样出架构。
    3.  **平衡函数（Balance Function）**：这是本文的核心创新机制。它作用于控制器的输出，旨在平衡**验证精度（`R_acc`）** 和**计算效率（`R_param`，用参数量衡量）**。其目的是激励控制器生成那些在准确率足够高的前提下，参数量尽可能少的网络结构。
    4.  **渐进式搜索策略**：不同于从复杂网络直接搜索，本文从最简单的单元结构（例如每个单元只有1个块，`B=1`）开始。评估并保留表现好的模型后，再将搜索扩展到更复杂的结构（例如`B=2`），同时剪枝掉表现不佳的候选模型。这有效缩小了搜索空间，加速了过程。
- **数学公式或机制的直观解释**：STFT将时域信号`u(mT)`转换为时频表示`X(mT, f)`（公式2），生成用于分类的图像特征。平衡函数的具体数学形式在提供的PDF文本中未明确给出，但其作用机制直观上是将精度和参数量这两个目标结合成一个单一的奖励信号，指导控制器的更新方向。
- **训练方式**：采用强化学习训练控制器。控制器采样多个子网络架构 -> 每个子网络在训练集上从头训练 -> 用验证精度（结合平衡函数）作为奖励 -> 使用策略梯度算法（如PPO）更新控制器参数，使其更倾向于采样出高奖励（即高精度、低参数量）的架构。
- **推理流程**：搜索阶段结束后，控制器输出一个最终的、确定的单元结构。用此结构构建完整网络，在全部训练数据上重新训练至收敛，得到最终模型用于雷达信号分类。
- **和已有方法的差异**：
    - 与手动设计网络相比：自动化，能适应不同环境。
    - 与标准NAS（如[27]）相比：引入了平衡函数进行多目标优化，而非仅追求精度；采用了渐进策略，大幅减少计算开销。
    - 与ENAS（[28]）相比：不仅使用参数共享，更核心的是引入了平衡函数和渐进搜索策略。
    - 与PNAS（[30]）相比：类似渐进思想，但本文是针对SEI任务，并增加了平衡函数来协调精度和计算成本。

## 6. 实验与结果
- **使用的数据集**：论文自建了一个雷达信号数据集，包含**7类**常用雷达信号：具有正斜率和负斜率的线性调频（LFM）、正弦频率调制、以及P1、P2、P3、P4多相码。数据集包含了不同信噪比（SNR）条件下的样本，图2展示了噪声自由和SNR=-10dB下的时频图像对比。
- **对比方法**：文中提及作为背景的对比方法包括传统分类器（SVM， KNN， 随机森林）和其他NAS方法（ENAS[28], NASH[29], PNAS[30]）。实验部分的具体对比算法在提供的PDF前12页中未完整列出。
- **评价指标**：主要指标是**分类准确率（Validation Accuracy）** 和**计算成本（以网络可训练参数量`R_param`度量）**。平衡函数正是围绕这两个指标设计的。
- **主实验结果**：从摘要和引言的结论可知，实验表明该方法是“极其高效”的，并且在不同环境下分类雷达信号时“优于传统算法”。具体的关键数字（如最终准确率）在提供的文本中未明确列出。
- **消融实验**：文中明确提到“different effects of the block and cell are tested and compared in the experiment”，表明对模块（块和单元）的作用进行了消融分析，以指导如何增加网络复杂度来应对更困难的任务。
- **泛化实验**：通过在不同SNR环境下进行实验，验证了方法对不同电磁环境（数据集分布变化）的适应性和泛化能力。
- **速度/参数量/FLOPs等效率信息**：论文将**可训练参数量**作为计算成本的主要代理指标。平衡函数的目标之一就是最小化这个指标。文中强调该方法能在达到最先进准确率的同时，“承担最廉价的计算成本”。

## 7. 这篇论文真正有价值的地方
1.  **问题驱动的NAS设计**：它不是简单地将通用NAS应用到SEI，而是深刻分析了SEI任务的特点（数据集因环境而变、对计算成本敏感），并据此设计了**平衡函数**。这为如何针对特定领域约束定制NAS目标函数提供了优秀范例。
2.  **多目标优化的实用框架**：在深度学习模型部署时，精度和效率（参数量、延迟）的权衡是永恒课题。本文提出的在搜索阶段就引入平衡函数来优化这一对矛盾的思路，具有普适的启发意义。
3.  **高效的搜索策略**：渐进式搜索策略结合剪枝，是降低NAS计算门槛的有效实践，尤其适合资源有限的实验室或工业应用场景。
4.  **对SEI任务的深入洞察**：论文清晰地指出了SEI与一般图像分类的区别，并通过实验证明了为不同“难度”（由噪声、信号相似度定义）的SEI子任务定制不同复杂度网络的必要性和可行性。

## 8. 局限与问题
- **方法假设依赖**：整个方法严重依赖于STFT生成的时频图像作为特征输入。对于某些时频分析效果不佳的信号调制类型，方法可能受限。
- **实验范围**：数据集仅包含7类雷达信号，虽然包含了具有相似特征的类别（如多种多相码），但相对于真实复杂的电磁环境，其规模和多样性仍然有限。对更广泛信号类型和极端环境的泛化能力有待进一步验证。
- **计算成本**：虽然通过渐进策略和平衡函数大幅优化，但NAS过程本质上仍然需要训练和评估多个子网络，其计算开销远大于手动设计并训练单个网络。论文未提供搜索过程的具体耗时和GPU资源使用量。
- **平衡函数的具体形式未充分揭示**：在提供的文本中，平衡函数的核心思想清晰，但其具体的数学公式和超参数设置未明确说明，这增加了复现的难度。
- **对比基线的完整性**：提供的文本中未详细列出最终实验对比的所有具体算法及其完整结果，难以全面评估其相对于最新SOTA方法的优势程度。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**Abstract**、**Introduction**（特别是末尾的贡献列表）、**Section IV (Balanced-NAS Framework)** 和 **Section VI (Experiments)** 的开头部分。
- **如果复现**：需要仔细研读 **Section IV**（块-单元结构定义、控制器设计）、**Section V**（平衡函数的构建，需寻找论文完整版）和 **Section VI**（实验设置、数据集构建、训练细节）。同时需要参考其引用的早期NAS工作（如[27]）来理解基础框架。
- **如果借鉴创新点**：
    - 借鉴 **“平衡函数”** 的思想：在自己的NAS或多目标优化任务中，设计一个将业务关键指标（如延迟、能耗、存储）与精度相结合的奖励或损失函数。
    - 借鉴 **“渐进式搜索”** 策略：在搜索复杂结构时，从简单结构开始逐步扩展，可以提升效率。
    - 借鉴 **“针对任务特点定制NAS”** 的思路：在应用NAS到新领域前，先分析该领域数据与任务的独特之处（如SEI的环境可变性）。
- **如果写related work**：可以将其放在以下几类中：
    - **NAS在特定领域的应用**（尤其是信号处理、雷达、通信领域）。
    - **高效的NAS方法**（涉及搜索策略加速，如渐进搜索）。
    - **多目标/多准则NAS**（同时优化精度和效率）。
    - **基于深度学习的特定辐射源识别（SEI）**。

## 10. 和其他论文的关系
根据论文主题，以下相关论文可能有关联：
- **神经网络架构搜索基础**：[[Neural Architecture Search with Reinforcement Learning]] (Zoph & Le, 2017) [26] [[Learning Transferable Architectures for Scalable Image Recognition]] (Zoph et al., 2018) [27]。这些是本文平衡NAS框架（特别是控制器部分）的重要基础。
- **高效NAS方法**：[[Efficient Neural Architecture Search via Parameter Sharing]] (Pham et al., 2018) [28] (ENAS), [[Progressive Neural Architecture Search]] (Liu et al., 2018) [30] (PNAS)。本文的渐进策略与PNAS思想一脉相承，平衡函数则是对ENAS等效率优化工作的深化。
- **特定辐射源识别**：[[使用CNN进行SEI]] 的相关工作（如文中引用的[18], [19]， [20]-[22]）。本文是对此类使用固定CNN工作的改进和自动化。

## 11. 关键词
特定辐射源识别 (SEI), 神经网络架构搜索 (NAS), 平衡函数 (Balance Function), 时频分析 (Time-Frequency Analysis), 雷达信号处理 (Radar Signal Processing), 强化学习 (Reinforcement Learning), 渐进搜索 (Progressive Search), 模型效率 (Model Efficiency), 多相码 (Polyphase Codes), 线性调频 (LFM), 卷积神经网络 (CNN), 电磁环境 (Electromagnetic Environment)

## 12. 可信度说明
本精读笔记主要基于提供的PDF文本前12页内容生成。提取文本覆盖了论文的摘要、引言、预备知识、相关工作回顾以及部分方法论（块-单元结构）和实验描述。**关于平衡函数的详细数学定义、完整的实验结果表格、以及论文的结论部分**在提供的文本中未完全呈现或缺失。因此，笔记中涉及这些部分的内容主要依赖于引言和摘要中的概括性描述，而非详细的公式和数据。整体上，对于论文的核心思想、动机、框架和贡献的概括是可靠和完整的。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/平衡神经网络搜索II Balanced NAS II.txt` (15/15 页; 原 AI 主体 12/15 + 全文补读 13-15); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: To validate the stability of the proposed balanced-NAS frame-
- p.14: experiments with random seeds. It is illustrated in e.g. [48],
- p.14: In this paper, a new NAS mechanism called balanced-NAS
- p.14: NAS mechanism exploiting the block-cell structure and RNN
- p.14: It is also of great interest to analyse inter-pulse radar features in
- p.14: REFERENCES
- p.15: Hyperparameter optimization in hundreds of dimensions for vision archi-

### 缺失页关键摘录

- p.13: of cells is ﬁxed to 2, and SNR =−10dB. The lines in red and blue show the comparison corresponding to the accuracy and the computation amount, respectively.
- p.13: terms of balancing the accuracy and efﬁciency.
- p.13: accuracy is served as the robustness indicator of the network.
- p.13: the accuracy of the selected models drops signiﬁcantly after
- p.13: the attack, see the orange lines in Fig. 16. This accuracy drop
- p.13: accuracy before adversarial attack, after attack and after ﬁne-tune through the
- p.13: adversarial training. (a)–(b): Accuracy of the top 5 optimized models selected
- p.13: training for the case of SNR =−10dB, the accuracy achieved
- p.14: Fig. 17. Stability comparison in terms of (a) validation accuracy and
- p.14: work, we show the standard deviation of the accuracy and
- p.14: performance as the baseline. The distribution of the accuracy
- p.14: can indeed ﬁnd the cheapest models whose accuracy is also
<!-- AI_READING_NOTE_END -->
