---
title: "TaesungKim∗ JinheeKim* YunwonTae"
authors:
  - "Taesung Kim"
  - "Jinhee Kim"
  - "Yunwon Tae"
  - "Cheonbok Park"
  - "Jang-Ho Choi"
  - "Jaegul Choo"
year: 2022
venue: "ICLR"
doi: 
pdf: [[RevIN(时序预测).pdf]]
primary_topic: R2_控制_生物启发_其他跨学科
topics:
  - "R2_控制_生物启发_其他跨学科"
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
extract_cache: .paper-cache/extracts/RevIN(时序预测).txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/25 pages"
---
# TaesungKim∗ JinheeKim* YunwonTae

## 基本信息
- **PDF**: [[RevIN(时序预测).pdf]]
- **primary_topic**: `R2_控制_生物启发_其他跨学科`
- **topics**: `R2_控制_生物启发_其他跨学科`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | TaesungKim∗ JinheeKim* YunwonTae |
| **作者** | Taesung Kim; Jinhee Kim; Yunwon Tae; Cheonbok Park; Jang-Ho Choi; Jaegul Choo |
| **发表时间** | 2022 |
| **刊物/会议** | ICLR |
| **DOI** | 未明确 |

## 摘要

> Statistical properties such as mean and variance often change over time in time series,i.e.,time-seriesdatasufferfromadistributionshiftproblem.Thischange intemporaldistributionisoneofthemainchallengesthatpreventaccuratetime- series forecasting. To address this issue, we propose a simple yet effective nor- malizationmethodcalledreversibleinstancenormalization(RevIN),agenerally- applicablenormalization-and-denormalizationmethodwithlearnableaffinetrans- formation. The proposed method is symmetrically structured to remove and re- store the statistical information of a time-series instance, leading to significant performance improvements in time-series forecasting, as shown in Fig. 1. We demonstratetheeffectivenessofRevINviaextensivequantitativeandqualitative analysesonvariousreal-worlddatasets,addressingthedistributionshiftproblem. ∗Bothauthorscontributedequally.Theorderofthefirstauthorswasdeterminedbycoinflip. 1 INTRODUCTION Time-series forecasting plays a significant role in addressing v

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：时间序列数据的统计特性（如均值、方差）常常随时间变化，即存在**分布偏移**问题。这导致模型的训练数据与测试数据分布不一致，是影响预测准确性的主要障碍之一 (p.1, p.3)。
- **之前方法的问题**：
    1. 传统的深度学习时间序列预测模型（如Informer, N-BEATS, SCINet）通常只对输入进行简单的全局预处理（如标准化），并期望端到端模型能自行处理分布差异，但效果有限 (p.2)。
    2. 如果直接对输入进行实例归一化（去除均值、方差），虽然能减少不同序列间的分布差异，但同时也**移除了对预测未来值可能至关重要的原始分布信息**，迫使模型必须仅从归一化后的输入中重构原始分布，增加了模型负担 (p.2)。
    3. 领域适应和领域泛化方法通常需要定义明确的“领域”，而在非平稳时间序列中，“领域”的定义并不直观（p.4）。
- **核心矛盾**：需要**归一化**输入以消除分布差异、降低预测难度，但归一化又会**丢失**对预测任务重要的原始分布统计信息。作者试图解决如何“既消除差异，又不丢失信息”这一矛盾。
## 关键贡献

1. **提出RevIN方法**：设计了一种对称的**归一化-反归一化**层。归一化层移除输入实例的均值和方差；反归一化层使用**相同的统计量**对模型输出进行逆变换，将原始分布信息显式地“还给”模型输出 (p.2, p.4)。
2. **显著提升模型性能**：通过将RevIN作为即插即用模块添加到三个先进的基线模型（Informer, N-BEATS, SCINet）上，在七个大规模真实世界数据集上取得了显著的性能提升，达到了当时的最佳水平 (p.2, p.6)。
3. **广泛的实验验证**：通过定量分析和定性可视化，深入验证了RevIN在缓解分布偏移问题上的有效性 (p.2, p.5)。
4. **方法的灵活性与通用性**：RevIN是一个**灵活、端到端可训练的层**，可以应用于网络中任意对称位置（通常是输入和输出层），且开销可忽略，具有模型无关性 (p.2, p.5)。
## 方法

- **整体框架**：RevIN被对称地应用在模型的**输入层和输出层**（图2）。整体流程为：输入序列 → RevIN归一化 → 主模型预测 → RevIN反归一化 → 最终预测。
- **输入输出**：输入为多变量时间序列 `x(i) ∈ R^{K × Tx}`，K是变量数，Tx是输入序列长度。输出为预测序列 `y(i) ∈ R^{K × Ty}`，Ty是预测长度。输入和输出长度可以不同 (p.3-4)。
- **关键模块**：
    1. **实例归一化**：对每个输入实例（每个变量的整个时间序列）计算其均值和方差，然后进行标准化，并引入**可学习的仿射变换参数** `γ, β`（公式2）。`ε` 是防止除零的小常数 (p.4)。
        ```
        ^x_{kt}^{(i)} = γ_k * ( (x_{kt}^{(i)} - μ_k) / (σ_k + ε) ) + β_k
        ```
    2. **反归一化**：使用**完全相同的均值、方差以及可学习参数**对模型输出进行逆变换（公式3）。
        ```
        ỹ_{kt}^{(i)} = σ_k * ( (ỹ_{kt}^{(i)} - β_k) / γ_k ) + μ_k
        ```
        其中 `μ_k`, `σ_k` 来自输入序列，`γ_k`, `β_k` 是共享的可学习参数。
- **模块连接与直观解释**：两个模块通过对称的数学操作（先减均值除方差，再乘方差加均值）连接。直观理解是：归一化层**移除**每个实例的独特统计特性，让模型看到一个“标准化”的、分布对齐的输入；反归一化层则将这些“个性化”的统计特性**重新附加**到模型输出上，使其还原到原始数据分布。这相当于先“简化问题”（消除分布差异），让模型专注于学习序列内部模式，再“恢复复杂性”（p.5）。
- **训练方式**：端到端训练。`γ` 和 `β` 作为可学习参数与主模型参数一起通过反向传播更新。
- **推理流程**：给定新输入，首先用其自身的均值和方差进行归一化，然后送入模型得到预测，最后用同样的均值、方差和学到的 `γ, β` 进行反归一化，得到最终预测值。
- **与已有方法差异**：
    1. 与传统全局预处理不同，RevIN是**实例级别**的，每个序列有自己的统计量。
    2. 与单纯的实例归一化不同，RevIN包含**对称的反归一化步骤**，显式恢复原始信息。
    3. 相比Adaptive RNNs等方法，RevIN**更简单、计算成本更低，且模型无关** (p.4)。
- **论文类型特化**：本文属于**时间序列预测方法论**研究。其核心创新点是一个通用的**归一化/后处理模块**，不涉及特定的注意力机制或网络架构修改，因此可应用于任何深度学习预测骨干网络。
## 实验

- **使用数据集**：主要在4个大规模真实数据集上评估：ETTh1, ETTh2, ETTm1 (电力变压器温度), ECL (电力消耗) (p.6)。附录中提到了更多数据集（空气质量、纳斯达克、M4竞赛数据）。
- **对比方法**：三个先进的非自回归深度学习预测模型：**Informer**, **N-BEATS**, **SCINet** (p.6)。
- **评价指标**：**均方误差** 和 **平均绝对误差** (p.6)。
- **主实验结果**：
    - **Table 1** 显示，在绝大多数设置和数据集上，为基线模型添加RevIN后，**MSE和MAE都获得显著降低**。
    - **示例** (p.6 Table 1)：在ETTh1数据集上，预测长度为24步时：
        - Informer：MSE 0.550 → **Informer+RevIN**：0.504 (↓8.4%)
        - N-BEATS：MSE 0.478 → **N-BEATS+RevIN**：0.330 (↓30.9%)
        - SCINet：MSE 0.338 → **SCINet+RevIN**：0.308 (↓8.9%)
    - 随着预测长度增加，提升往往更加明显（如ETTh2数据集，长预测时误差降低可达数倍）。
- **消融实验**：在提供的文本中未明确说明，但论文提到在附录A.4中验证了将RevIN应用于中间层的效果 (p.5)。
- **泛化实验**：通过在Informer, N-BEATS, SCINet三种不同架构的模型上均取得显著提升，证明了RevIN的**模型泛化性** (p.6)。
- **效率信息**：在提供的文本中未找到关于速度、参数量或FLOPs的具体数据。但文中描述其开销可“忽略不计”(negligible cost) (p.2)。
## 局限

- **适用场景假设**：RevIN假设一个输入实例的时间序列具有统计代表性（即能计算出有意义的均值和方差）。对于**分布完全随机、无统计规律**的序列，或**单点序列**，其效果可能有限。
- **实验覆盖面**：基于提供的文本，主要实验仅详细报告了4个数据集。虽然论文声称在7个数据集上有效，但未在此部分列出所有细节。方法对**极短序列**或**单变量序列**的适用性未在提供的文本中充分探讨。
- **计算成本**：文中声称开销可忽略，但未在提供的文本中给出具体的**运行时间、参数量或FLOPs**对比数据，无法精确评估其效率。
- **假设依赖**：方法核心依赖于输入序列和输出序列使用**相同的归一化统计量**。如果输入和输出序列的统计特性分布发生根本性变化（非平稳性极强），这一假设可能不成立。
- **复现风险**：方法本身简单，复现难度低。但最佳性能可能依赖于**可学习仿射参数 `γ, β` 的初始化**以及与主模型训练的协调，这些细节在提供的文本中未说明（可能在附录）。
## 个人评论

这篇论文最值得学习的是其**核心思想和问题洞察**：
1. **问题抽象的准确性**：作者将预测不准的一个关键原因抽象为“分布偏移”，并清晰地分析了归一化与信息保留之间的矛盾，这为解决问题指明了方向。
2. **解决方案的优雅与简洁**：RevIN并非设计一个复杂的网络模块，而是从数据预处理/后处理的视角，用一个**对称、可学习、即插即用**的层来解决问题。这启示我们，有时候一个设计精巧的“外围”模块，比直接修改复杂的核心网络结构更有效、更通用。
3. **方法论的启发**：**“先简化问题，再恢复复杂性”** 的思路具有普适性。这鼓励研究者在遇到复杂问题时，思考是否可以通过输入输出变换，将难题转化为模型更容易处理的形式。
4. **对实验严谨性的示范**：通过在多种基线模型和数据集上的一致性验证，以及直观的分布可视化（图3），有力地证明了方法的有效性，这种论证方式值得借鉴。

### 使用建议

- **如果快速了解**：只读**摘要**、**第1节（引言）**、**图2和图3**，以及**Table 1**，即可理解论文的核心思想、动机、方法和显著效果。
- **如果复现**：重点精读**第3节（Proposed Method）**，尤其是**公式1、2、3**。关注附录中关于**超参数、训练细节**的说明（A.11节）以及**基线模型复现细节**（A.12节）。
- **如果借鉴创新点**：
    1. 学习其**“对称归一化/反归一化”** 的模块设计思路，思考如何将此思想应用于其他有分布偏移问题的任务（如图像风格迁移、跨域分类）。
    2. 学习其**模块通用性**的设计，一个简单的、可插拔的层如何为整个模型带来稳定提升。
    3. 学习其**实验验证**方法，特别是用数据分布可视化来直观证明方法有效性。
- **如果写related work**：可将本论文放在以下类别：
    1. **时间序列归一化方法**。
    2. **处理分布偏移的深度学习方法**（与领域适应、领域泛化并列）。
    3. **时间序列预测的通用模块/组件**。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R2_控制_生物启发_其他跨学科]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**时间序列预测**领域，专注于解决时间序列数据中广泛存在的**分布偏移**问题。论文提出了一种名为**可逆实例归一化**的通用方法，旨在提升深度学习模型在面对非平稳时间序列时的预测准确性。根据提供的主题标签，它可归类于“R2_控制_生物启发_其他跨学科”，但更准确地说，是**时间序列预测与分布适应**方向的交叉研究。

## 2. 一句话总结
本文提出了一种简单而有效的、对称结构的归一化与反归一化方法——**可逆实例归一化**，通过在输入层移除时间序列实例的均值和方差等非平稳信息，并在输出层将其显式地恢复回来，从而有效缓解分布偏移问题，显著提升各类深度学习时间序列预测模型的性能。

## 3. 背景与问题
- **为什么要做**：时间序列数据的统计特性（如均值、方差）常常随时间变化，即存在**分布偏移**问题。这导致模型的训练数据与测试数据分布不一致，是影响预测准确性的主要障碍之一 (p.1, p.3)。
- **之前方法的问题**：
    1. 传统的深度学习时间序列预测模型（如Informer, N-BEATS, SCINet）通常只对输入进行简单的全局预处理（如标准化），并期望端到端模型能自行处理分布差异，但效果有限 (p.2)。
    2. 如果直接对输入进行实例归一化（去除均值、方差），虽然能减少不同序列间的分布差异，但同时也**移除了对预测未来值可能至关重要的原始分布信息**，迫使模型必须仅从归一化后的输入中重构原始分布，增加了模型负担 (p.2)。
    3. 领域适应和领域泛化方法通常需要定义明确的“领域”，而在非平稳时间序列中，“领域”的定义并不直观（p.4）。
- **核心矛盾**：需要**归一化**输入以消除分布差异、降低预测难度，但归一化又会**丢失**对预测任务重要的原始分布统计信息。作者试图解决如何“既消除差异，又不丢失信息”这一矛盾。

## 4. 核心贡献
1. **提出RevIN方法**：设计了一种对称的**归一化-反归一化**层。归一化层移除输入实例的均值和方差；反归一化层使用**相同的统计量**对模型输出进行逆变换，将原始分布信息显式地“还给”模型输出 (p.2, p.4)。
2. **显著提升模型性能**：通过将RevIN作为即插即用模块添加到三个先进的基线模型（Informer, N-BEATS, SCINet）上，在七个大规模真实世界数据集上取得了显著的性能提升，达到了当时的最佳水平 (p.2, p.6)。
3. **广泛的实验验证**：通过定量分析和定性可视化，深入验证了RevIN在缓解分布偏移问题上的有效性 (p.2, p.5)。
4. **方法的灵活性与通用性**：RevIN是一个**灵活、端到端可训练的层**，可以应用于网络中任意对称位置（通常是输入和输出层），且开销可忽略，具有模型无关性 (p.2, p.5)。

## 5. 方法详解
- **整体框架**：RevIN被对称地应用在模型的**输入层和输出层**（图2）。整体流程为：输入序列 → RevIN归一化 → 主模型预测 → RevIN反归一化 → 最终预测。
- **输入输出**：输入为多变量时间序列 `x(i) ∈ R^{K × Tx}`，K是变量数，Tx是输入序列长度。输出为预测序列 `y(i) ∈ R^{K × Ty}`，Ty是预测长度。输入和输出长度可以不同 (p.3-4)。
- **关键模块**：
    1. **实例归一化**：对每个输入实例（每个变量的整个时间序列）计算其均值和方差，然后进行标准化，并引入**可学习的仿射变换参数** `γ, β`（公式2）。`ε` 是防止除零的小常数 (p.4)。
        ```
        ^x_{kt}^{(i)} = γ_k * ( (x_{kt}^{(i)} - μ_k) / (σ_k + ε) ) + β_k
        ```
    2. **反归一化**：使用**完全相同的均值、方差以及可学习参数**对模型输出进行逆变换（公式3）。
        ```
        ỹ_{kt}^{(i)} = σ_k * ( (ỹ_{kt}^{(i)} - β_k) / γ_k ) + μ_k
        ```
        其中 `μ_k`, `σ_k` 来自输入序列，`γ_k`, `β_k` 是共享的可学习参数。
- **模块连接与直观解释**：两个模块通过对称的数学操作（先减均值除方差，再乘方差加均值）连接。直观理解是：归一化层**移除**每个实例的独特统计特性，让模型看到一个“标准化”的、分布对齐的输入；反归一化层则将这些“个性化”的统计特性**重新附加**到模型输出上，使其还原到原始数据分布。这相当于先“简化问题”（消除分布差异），让模型专注于学习序列内部模式，再“恢复复杂性”（p.5）。
- **训练方式**：端到端训练。`γ` 和 `β` 作为可学习参数与主模型参数一起通过反向传播更新。
- **推理流程**：给定新输入，首先用其自身的均值和方差进行归一化，然后送入模型得到预测，最后用同样的均值、方差和学到的 `γ, β` 进行反归一化，得到最终预测值。
- **与已有方法差异**：
    1. 与传统全局预处理不同，RevIN是**实例级别**的，每个序列有自己的统计量。
    2. 与单纯的实例归一化不同，RevIN包含**对称的反归一化步骤**，显式恢复原始信息。
    3. 相比Adaptive RNNs等方法，RevIN**更简单、计算成本更低，且模型无关** (p.4)。
- **论文类型特化**：本文属于**时间序列预测方法论**研究。其核心创新点是一个通用的**归一化/后处理模块**，不涉及特定的注意力机制或网络架构修改，因此可应用于任何深度学习预测骨干网络。

## 6. 实验与结果
- **使用数据集**：主要在4个大规模真实数据集上评估：ETTh1, ETTh2, ETTm1 (电力变压器温度), ECL (电力消耗) (p.6)。附录中提到了更多数据集（空气质量、纳斯达克、M4竞赛数据）。
- **对比方法**：三个先进的非自回归深度学习预测模型：**Informer**, **N-BEATS**, **SCINet** (p.6)。
- **评价指标**：**均方误差** 和 **平均绝对误差** (p.6)。
- **主实验结果**：
    - **Table 1** 显示，在绝大多数设置和数据集上，为基线模型添加RevIN后，**MSE和MAE都获得显著降低**。
    - **示例** (p.6 Table 1)：在ETTh1数据集上，预测长度为24步时：
        - Informer：MSE 0.550 → **Informer+RevIN**：0.504 (↓8.4%)
        - N-BEATS：MSE 0.478 → **N-BEATS+RevIN**：0.330 (↓30.9%)
        - SCINet：MSE 0.338 → **SCINet+RevIN**：0.308 (↓8.9%)
    - 随着预测长度增加，提升往往更加明显（如ETTh2数据集，长预测时误差降低可达数倍）。
- **消融实验**：在提供的文本中未明确说明，但论文提到在附录A.4中验证了将RevIN应用于中间层的效果 (p.5)。
- **泛化实验**：通过在Informer, N-BEATS, SCINet三种不同架构的模型上均取得显著提升，证明了RevIN的**模型泛化性** (p.6)。
- **效率信息**：在提供的文本中未找到关于速度、参数量或FLOPs的具体数据。但文中描述其开销可“忽略不计”(negligible cost) (p.2)。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的是其**核心思想和问题洞察**：
1. **问题抽象的准确性**：作者将预测不准的一个关键原因抽象为“分布偏移”，并清晰地分析了归一化与信息保留之间的矛盾，这为解决问题指明了方向。
2. **解决方案的优雅与简洁**：RevIN并非设计一个复杂的网络模块，而是从数据预处理/后处理的视角，用一个**对称、可学习、即插即用**的层来解决问题。这启示我们，有时候一个设计精巧的“外围”模块，比直接修改复杂的核心网络结构更有效、更通用。
3. **方法论的启发**：**“先简化问题，再恢复复杂性”** 的思路具有普适性。这鼓励研究者在遇到复杂问题时，思考是否可以通过输入输出变换，将难题转化为模型更容易处理的形式。
4. **对实验严谨性的示范**：通过在多种基线模型和数据集上的一致性验证，以及直观的分布可视化（图3），有力地证明了方法的有效性，这种论证方式值得借鉴。

## 8. 局限与问题
- **适用场景假设**：RevIN假设一个输入实例的时间序列具有统计代表性（即能计算出有意义的均值和方差）。对于**分布完全随机、无统计规律**的序列，或**单点序列**，其效果可能有限。
- **实验覆盖面**：基于提供的文本，主要实验仅详细报告了4个数据集。虽然论文声称在7个数据集上有效，但未在此部分列出所有细节。方法对**极短序列**或**单变量序列**的适用性未在提供的文本中充分探讨。
- **计算成本**：文中声称开销可忽略，但未在提供的文本中给出具体的**运行时间、参数量或FLOPs**对比数据，无法精确评估其效率。
- **假设依赖**：方法核心依赖于输入序列和输出序列使用**相同的归一化统计量**。如果输入和输出序列的统计特性分布发生根本性变化（非平稳性极强），这一假设可能不成立。
- **复现风险**：方法本身简单，复现难度低。但最佳性能可能依赖于**可学习仿射参数 `γ, β` 的初始化**以及与主模型训练的协调，这些细节在提供的文本中未说明（可能在附录）。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读**摘要**、**第1节（引言）**、**图2和图3**，以及**Table 1**，即可理解论文的核心思想、动机、方法和显著效果。
- **如果复现**：重点精读**第3节（Proposed Method）**，尤其是**公式1、2、3**。关注附录中关于**超参数、训练细节**的说明（A.11节）以及**基线模型复现细节**（A.12节）。
- **如果借鉴创新点**：
    1. 学习其**“对称归一化/反归一化”** 的模块设计思路，思考如何将此思想应用于其他有分布偏移问题的任务（如图像风格迁移、跨域分类）。
    2. 学习其**模块通用性**的设计，一个简单的、可插拔的层如何为整个模型带来稳定提升。
    3. 学习其**实验验证**方法，特别是用数据分布可视化来直观证明方法有效性。
- **如果写related work**：可将本论文放在以下类别：
    1. **时间序列归一化方法**。
    2. **处理分布偏移的深度学习方法**（与领域适应、领域泛化并列）。
    3. **时间序列预测的通用模块/组件**。

## 10. 和其他论文的关系
根据论文主题和内容，可能相关的方向包括：
- **其他分布适应/归一化方法**：如用于图像的Batch Normalization，用于域适应的DANN [[Domain-Adversarial Training of Neural Networks]]。
- **时间序列预测基准模型**：论文中作为基线的 [[Informer]], [[N-BEATS]], [[SCINet]]。
- **处理非平稳时间序列的方法**：如自适应RNN [[Adaptive RNNs]] (文中引用)。
（由于知识库中未提供具体论文列表，此处仅根据论文内容提及相关概念，不编写具体双链）。

## 11. 关键词
可逆实例归一化， 时间序列预测， 分布偏移， 归一化与反归一化， 深度学习， 模型无关， 可训练层， 非平稳时间序列， ETT数据集， ECL数据集， MSE， MAE

## 12. 可信度说明
本篇精读笔记主要基于提供的PDF文本内容生成，覆盖了论文的**前12页**（共25页），包括标题、作者、摘要、引言、相关工作、方法详述、实验设置及部分结果（主要结果表）。因此：
- **方法部分**（RevIN的原理、公式、框架）的描述是完整且可靠的。
- **核心动机、贡献和实验设置**的描述是准确的。
- **局限**：由于未提供论文的后13页（包含附录、更多实验细节、讨论等），因此关于**附录中的消融实验、所有数据集上的完整结果、训练细节、与其他更先进方法的对比**等信息无法在此笔记中呈现，存在信息缺口。对于速度/参数量等效率指标，也因文本未提及而无法说明。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/RevIN(时序预测).txt` (25/25 页; 原 AI 主体 12/25 + 全文补读 13-25); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-25; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-25。
- **提取情况**: 缺失页 13 页, 其中 13 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Published as a conference paper at ICLR 2022
- p.13: M45competition dataset consists of six different hourly, daily, weekly, monthly, quarterly, and
- p.13: Additionally, we conduct a qualitative analysis on the Nasdaq dataset to verify the effectiveness
- p.14: Train ETTh 1 ETTh 2 ETTm 1
- p.14: Test ETTh 2 ETTm 1 ETTh 1 ETTm 1 ETTh 1 ETTh 2
- p.14: Prediction length 336 960 336 960 336 960 336 960 288 1344 288 1344
- p.14: As RevIN can alleviate the distribution discrepancy between the training and test data, we investigate
- p.14: ETTh 2datasets are collected from different locations, and the ETTh and ETTm 1datasets have dif-
- p.14: In Table 5, despite the difference in the data distributions, RevIN shows remarkable performance in
- p.14: results demonstrate that RevIN successfully solves the distribution shift problem by alleviating data
- p.14: We analyze the hyperparameter sensitivity of the proposed method compared with the baseline mod-
- p.14: MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE

### 缺失页关键摘录

- p.13: Figure 6: Prediction results on the Nasdaq dataset. The results on three variables in the data,
- p.13: M45competition dataset consists of six different hourly, daily, weekly, monthly, quarterly, and
- p.13: competition (Makridakis et al., 2020). For evaluation, we measure the micro-averaged mean ab-
- p.13: As shown in Table 4, RevIN signiﬁcantly improves the forecasting performance of the baselines on
- p.13: all three datasets. Notably, RevIN shows outstanding performance on the Nasdaq dataset, reducing
- p.13: Additionally, we conduct a qualitative analysis on the Nasdaq dataset to verify the effectiveness
- p.13: distribution. As a result, even existing state-of-the-art models often cannot predict the future values
- p.14: Table 5: Cross-domain time-series forecasting results. We conduct a cross-domain evaluation on
- p.14: the data is collected. We use the ETT datasets for the experiment since they have the same feature
- p.14: ferent measurement time intervals. Thus, we alternately use each ETT dataset as a source domain
- p.14: In Table 5, despite the difference in the data distributions, RevIN shows remarkable performance in
- p.14: Figure 7: Impacts of the input sequence length on RevIN compared with the baselines. We
<!-- AI_READING_NOTE_END -->
