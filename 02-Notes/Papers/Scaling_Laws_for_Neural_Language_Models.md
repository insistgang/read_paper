---
title: Scaling Laws for Neural Language Models
authors:
  - "Scaling Laws for Neural Language Models"
  - "JaredKaplan∗ SamMcCandlish∗"
  - "JohnsHopkinsUniversity"
  - "OpenAI OpenAI"
  - "TomHenighan TomB.Brown BenjaminChess RewonChild"
  - "OpenAI OpenAI OpenAI OpenAI"
  - "ScottGray AlecRadford JeffreyWu DarioAmodei"
year: 2020
venue: "arXiv"
doi: 
pdf: [[Scaling_Laws_for_Neural_Language_Models.pdf]]
primary_topic: G_视觉基础模型_VLM_LLM
topics:
  - "G_视觉基础模型_VLM_LLM"
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
extract_cache: .paper-cache/extracts/Scaling_Laws_for_Neural_Language_Models.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/30 pages"
---
# Scaling Laws for Neural Language Models

## 基本信息
- **PDF**: [[Scaling_Laws_for_Neural_Language_Models.pdf]]
- **primary_topic**: `G_视觉基础模型_VLM_LLM`
- **topics**: `G_视觉基础模型_VLM_LLM`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Scaling Laws for Neural Language Models |
| **作者** | Scaling Laws for Neural Language Models; JaredKaplan∗ SamMcCandlish∗; JohnsHopkinsUniversity; OpenAI OpenAI; TomHenighan TomB.Brown BenjaminChess RewonChild; OpenAI OpenAI OpenAI OpenAI; ScottGray AlecRadford JeffreyWu DarioAmodei |
| **发表时间** | 2020 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Westudyempiricalscalinglawsforlanguagemodelperformanceonthecross-entropyloss. The loss scales as a power-law with model size, dataset size, and the amount of compute usedfortraining,withsometrendsspanningmorethansevenordersofmagnitude. Other architectural details such as network width or depth have minimal effects within a wide range.Simpleequationsgovernthedependenceofoverfittingonmodel/datasetsizeandthe dependenceoftrainingspeedonmodelsize. Theserelationshipsallowustodeterminethe optimalallocationofafixedcomputebudget.Largermodelsaresignificantlymoresample- efficient,suchthatoptimallycompute-efficienttraininginvolvestrainingverylargemodels onarelativelymodestamountofdataandstoppingsignificantlybeforeconvergence. ∗Equalcontribution. Contributions: Jared Kaplan and Sam McCandlish led the research. Tom Henighan contributed the LSTM ex- periments. Tom Brown, Rewon Child, and Scott Gray, and Alec Radford developed the optimized Transformer implementation. Jeff Wu, Benjamin Chess, and Alec

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：尽管深度学习在语言建模上取得了巨大进步，但模型性能如何依赖于模型架构、规模、计算量和数据量等因素，缺乏系统的、定量的理解。研究者通常凭经验或直觉来设计模型和分配资源，缺乏理论指导。
- **之前方法有什么问题**：PDF文本中未明确说明之前方法的具体问题，但从上下文可以推断，缺乏对上述因素间定量关系的普适性总结，导致在扩大模型规模时资源配置可能不是最优的。
- **作者想解决的核心矛盾是**：在计算资源（C）有限的情况下，如何平衡模型大小（N）和训练数据量（D），以达到最低的测试损失（L）。即，应该把计算预算更多地花在构建更大的模型上，还是花在训练更多的数据上？
## 关键贡献

1.  **发现性能与规模的幂律关系**：语言模型的测试损失（L）分别与模型参数量（N）、数据集大小（D）和最优计算预算（C_min）呈现跨越多个数量级的幂律关系（`L(N) ∝ N^{-α_N}`, `L(D) ∝ D^{-α_D}`, `L(C_min) ∝ C_min^{-α_C}`）。具体地，α_N ≈ 0.076, α_D ≈ 0.095, α_C ≈ 0.050。
2.  **证明性能弱依赖于模型形状**：在固定的非嵌入参数量（N）下，模型的性能对深度、宽度、注意力头数等架构细节非常不敏感（p.7, p.8）。
3.  **建立过拟合的普遍规律**：模型大小N和数据量D需要协同扩展。性能惩罚取决于比率 N^{0.74}/D。这意味着，模型大小每增加8倍，数据量只需增加约5倍即可避免性能下降（p.4, p.10）。
4.  **发现训练曲线的普遍性**：不同大小模型的训练曲线（损失随训练步数变化）遵循可预测的幂律，且其参数大致与模型大小无关，允许通过早期训练预测最终性能（p.5, p.12）。
5.  **提出最优计算分配策略**：在固定计算预算C下，最优策略是将大部分计算用于增加模型大小，而不是大幅增加训练步数或数据量。具体增长关系为：N ∝ C^{0.73}, B ∝ C^{0.24}, S ∝ C^{0.03}（p.6, p.14）。这表明大模型更样本高效。
## 方法

- **整体框架**：本研究是实证研究。作者训练了数百个不同配置的Transformer语言模型，系统性地改变一个变量（如模型大小、数据量、模型形状）而控制其他变量，记录其测试损失，然后拟合经验性的幂律公式。
- **输入输出**：输入是一系列文本序列（1024 token上下文）。模型的任务是自回归预测下一个token。输出是每个token的预测概率分布。性能指标是平均交叉熵损失（以nats为单位）。
- **关键模块与连接**：研究的是标准的、仅解码器（decoder-only）的Transformer架构。关键组件包括嵌入层、多层自注意力机制和前馈神经网络。模块按标准Transformer结构堆叠连接。研究的重点不在于架构创新，而在于衡量架构规模（N）的影响。
- **数学公式/机制的直观解释**：
    - 核心是几个幂律公式。例如，`L(N) = (N_c / N)^{α_N}`。直观上，随着模型参数N的增加，损失L以幂律形式下降。指数α_N（约0.076）衡量了损失对模型规模的敏感度，值很小意味着需要大幅增加模型规模才能显著降低损失。
    - 最优分配公式（1.7）揭示了计算预算增长的“流向”：大部分（由α_N/α_C主导）应流向更大的模型。
- **训练方式**：使用Adam优化器，大多数模型训练固定的2.5×10^5步，批大小为512个序列（p.7）。采用线性学习率预热加余弦衰减的策略。
- **推理流程**：模型训练完成后，在WebText2测试集以及其他数据集（如Books Corpus， Wikipedia）上计算交叉熵损失。
- **和已有方法的差异**：本文的差异不在于提出新模型，而在于进行了一项前所未有的、大规模的系统性实证研究，量化了现有主流架构（Transformer）的性能与关键因素之间的**定量关系**。它将实践中模糊的“规模直觉”转变为可预测的数学公式。
## 实验

- **使用的数据集**：主要训练和测试数据集是**WebText2**，这是一个基于Reddit高赞链接的网页文本数据集，包含约2.29×10^10个token（p.7）。泛化测试使用了Books Corpus、Common Crawl、English Wikipedia和互联网书籍（p.8）。
- **对比方法**：主要对比了不同规模（从768到1.5B非嵌入参数）的**Transformer**模型。此外，还将Transformer与**LSTM**模型以及**循环Transformer（Universal Transformers）** 进行了比较（p.8）。
- **评价指标**：主要指标是在测试集上的**交叉熵损失（cross-entropy loss）**，单位是nats（p.7）。
- **主实验结果**：
    - **幂律验证**：损失L分别与N、D、C呈现清晰的幂律关系，拟合趋势跨越超过6个数量级（p.4, p.8）。
    - **模型形状不敏感**：在N固定时，改变模型深度、宽度等，损失变化仅在几个百分点之内（p.8， 图5）。
    - **过拟合规律**：给出了联合依赖N和D的公式 `L(N,D) = [(N_c/N)^{α_N/α_D} + (D_c/D)]^{α_D}`，并验证了其有效性（p.5， 图4左）。
    - **训练曲线规律**：给出了依赖N和训练步数S的公式 `L(N,S) = (N_c/N)^{α_N} + (S_c/S_min(S))^{α_S}`（p.5， 图4右）。
    - **LSTM对比**：LSTM在上下文前期的token上性能与Transformer相当，但在后期token上性能显著下降，无法有效利用长距离上下文（p.9， 图7）。
    - **泛化能力**：在WebText2上训练的模型，在其他数据分布上的损失也随N平滑改善，改善程度与在WebText2测试损失强相关（p.9， 图8）。
- **消融实验**：文本中未明确使用“消融实验”一词，但通过**控制变量**的方法系统研究了每个因素（N， D， 形状， 批大小等）的影响，这本质上构成了对模型规模各个维度的消融研究。
- **泛化实验**：见上述“主实验结果”中的泛化能力部分。
- **速度/参数量/FLOPs**：
    - 模型参数量N定义为非嵌入参数数量，近似公式为 `N ≈ 12 * n_layer * d_model^2`（p.6）。
    - 训练计算量C估算为 `C ≈ 6 * N * B * S` 浮点运算次数（p.6），其中B是批大小，S是步数。数值以PF-days为单位（1 PF-day = 8.64×10^19 FLOPs）。
    - 论文详细分析了计算效率，指出最优训练在收敛前很早就停止，是计算高效的（p.6）。
## 局限

- **架构依赖性**：所有实验和结论均基于**Transformer架构**，特别是仅解码器（decoder-only）变体。对于其他架构（如编码器-解码器、混合专家模型等），这些幂律关系是否完全相同，PDF文本中未明确说明。
- **数据集特异性**：实验主要基于WebText2数据集。其幂律公式的具体常数（如N_c, D_c）可能与数据的特性（如分布、质量、token化方式）强相关。论文提到这些常数“依赖于词汇表大小和token化方式，因此没有根本意义”（p.5）。
- **外推风险**：虽然观察到的趋势跨越了多个数量级，且“在高端没有观察到偏离趋势的迹象”（p.4），但论文承认损失“最终必须在达到零损失之前趋于平稳”（p.4）。将这些关系外推到训练数据或模型规模超出当前研究范围更远的程度，其有效性未经验证。
- **计算成本高昂**：为了获得这些经验公式，作者需要训练数百个不同规模的模型，总计算量巨大。这本身是一个很高的门槛。
- **假设依赖**：最优分配策略（1.7）的推导依赖于一些假设，例如批大小可以自由调整。论文指出最优批大小大约是损失的一个幂函数（公式1.4），并可通过梯度噪声尺度来确定（p.5）。
## 个人评论

这篇论文最核心的价值在于，它**将深度学习，特别是大模型训练，从一门“艺术”向一门“工程科学”推进了关键一步**。它提供的几个幂律公式，就像是一个“晶体球”，让研究者可以在真正进行昂贵的大规模训练之前，**预测**不同资源配置下的模型性能。
- **对后续研究的启发**：它确立了“规模即性能”的实证基础，极大地推动了后续更大规模模型（如GPT-3， GPT-4）的研发。任何想训练或改进大型语言模型的工作，都必须考虑或参考这些缩放定律。
- **对改模型/做实验的启发**：它提供了明确的指导：如果想提升模型性能，最有效的途径是**同时增加模型大小和数据量**，但模型大小的增长应快于数据量。在资源有限时，应该优先训练一个**远大于收敛所需规模**的模型，并使用**较少的数据**，然后**提前停止**训练。这彻底改变了“用小模型在大数据上训练到收敛”的传统思维。
- **对写论文的启发**：它是一个如何进行大规模、系统性实证研究并从中提炼出简洁优美公式的典范。其论文结构清晰，从观测现象到拟合公式，再到推论和应用，逻辑链条完整。

### 使用建议

- **如果快速了解**：重点阅读 **摘要（Abstract）**、**1.1节总结（Summary）** 和 **1.2节缩放定律总结（Summary of Scaling Laws）**。这能让你用最少时间掌握核心发现和公式。
- **如果复现**：重点阅读 **第2节 背景与方法（Background and Methods）**，了解模型细节、训练过程、计算量估算方式。并查看附录中的具体实验设置。
- **如果借鉴创新点**：应重点学习**第3节和第4节**，理解他们如何设计实验来隔离和验证单个变量（N， D）的影响。以及他们如何从数据中拟合出幂律公式（1.1-1.6）。
- **如果写related work**：可将本文放在**“大语言模型的规模定律”、“Transformer训练动力学”、“计算效率与样本效率”** 这一类中。它是该方向的开创性、奠基性工作。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[G_视觉基础模型_VLM_LLM]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于机器学习领域，具体是**深度学习的规模扩展规律（Scaling Laws）研究**。它通过大规模实证研究，系统性地量化了神经语言模型（特别是Transformer架构）的性能（以交叉熵损失衡量）如何随着模型参数规模、训练数据集规模和计算预算的变化而变化。论文旨在为大型语言模型的训练提供理论指导和预测公式，帮助研究者更高效地分配计算资源。适合放在“G_视觉基础模型_VLM_LLM”主题下，因为它奠定了大型语言模型训练的核心理论基础之一。

## 2. 一句话总结
这篇论文通过实证发现，Transformer语言模型的损失与模型大小、数据大小和计算量之间存在平滑的幂律关系，并基于此提出了在固定计算预算下最优分配模型大小和数据量的策略，即“训练一个非常大的模型但提前停止”是最高效的。

## 3. 背景与问题
- **这篇论文为什么要做**：尽管深度学习在语言建模上取得了巨大进步，但模型性能如何依赖于模型架构、规模、计算量和数据量等因素，缺乏系统的、定量的理解。研究者通常凭经验或直觉来设计模型和分配资源，缺乏理论指导。
- **之前方法有什么问题**：PDF文本中未明确说明之前方法的具体问题，但从上下文可以推断，缺乏对上述因素间定量关系的普适性总结，导致在扩大模型规模时资源配置可能不是最优的。
- **作者想解决的核心矛盾是**：在计算资源（C）有限的情况下，如何平衡模型大小（N）和训练数据量（D），以达到最低的测试损失（L）。即，应该把计算预算更多地花在构建更大的模型上，还是花在训练更多的数据上？

## 4. 核心贡献
1.  **发现性能与规模的幂律关系**：语言模型的测试损失（L）分别与模型参数量（N）、数据集大小（D）和最优计算预算（C_min）呈现跨越多个数量级的幂律关系（`L(N) ∝ N^{-α_N}`, `L(D) ∝ D^{-α_D}`, `L(C_min) ∝ C_min^{-α_C}`）。具体地，α_N ≈ 0.076, α_D ≈ 0.095, α_C ≈ 0.050。
2.  **证明性能弱依赖于模型形状**：在固定的非嵌入参数量（N）下，模型的性能对深度、宽度、注意力头数等架构细节非常不敏感（p.7, p.8）。
3.  **建立过拟合的普遍规律**：模型大小N和数据量D需要协同扩展。性能惩罚取决于比率 N^{0.74}/D。这意味着，模型大小每增加8倍，数据量只需增加约5倍即可避免性能下降（p.4, p.10）。
4.  **发现训练曲线的普遍性**：不同大小模型的训练曲线（损失随训练步数变化）遵循可预测的幂律，且其参数大致与模型大小无关，允许通过早期训练预测最终性能（p.5, p.12）。
5.  **提出最优计算分配策略**：在固定计算预算C下，最优策略是将大部分计算用于增加模型大小，而不是大幅增加训练步数或数据量。具体增长关系为：N ∝ C^{0.73}, B ∝ C^{0.24}, S ∝ C^{0.03}（p.6, p.14）。这表明大模型更样本高效。

## 5. 方法详解
- **整体框架**：本研究是实证研究。作者训练了数百个不同配置的Transformer语言模型，系统性地改变一个变量（如模型大小、数据量、模型形状）而控制其他变量，记录其测试损失，然后拟合经验性的幂律公式。
- **输入输出**：输入是一系列文本序列（1024 token上下文）。模型的任务是自回归预测下一个token。输出是每个token的预测概率分布。性能指标是平均交叉熵损失（以nats为单位）。
- **关键模块与连接**：研究的是标准的、仅解码器（decoder-only）的Transformer架构。关键组件包括嵌入层、多层自注意力机制和前馈神经网络。模块按标准Transformer结构堆叠连接。研究的重点不在于架构创新，而在于衡量架构规模（N）的影响。
- **数学公式/机制的直观解释**：
    - 核心是几个幂律公式。例如，`L(N) = (N_c / N)^{α_N}`。直观上，随着模型参数N的增加，损失L以幂律形式下降。指数α_N（约0.076）衡量了损失对模型规模的敏感度，值很小意味着需要大幅增加模型规模才能显著降低损失。
    - 最优分配公式（1.7）揭示了计算预算增长的“流向”：大部分（由α_N/α_C主导）应流向更大的模型。
- **训练方式**：使用Adam优化器，大多数模型训练固定的2.5×10^5步，批大小为512个序列（p.7）。采用线性学习率预热加余弦衰减的策略。
- **推理流程**：模型训练完成后，在WebText2测试集以及其他数据集（如Books Corpus， Wikipedia）上计算交叉熵损失。
- **和已有方法的差异**：本文的差异不在于提出新模型，而在于进行了一项前所未有的、大规模的系统性实证研究，量化了现有主流架构（Transformer）的性能与关键因素之间的**定量关系**。它将实践中模糊的“规模直觉”转变为可预测的数学公式。

## 6. 实验与结果
- **使用的数据集**：主要训练和测试数据集是**WebText2**，这是一个基于Reddit高赞链接的网页文本数据集，包含约2.29×10^10个token（p.7）。泛化测试使用了Books Corpus、Common Crawl、English Wikipedia和互联网书籍（p.8）。
- **对比方法**：主要对比了不同规模（从768到1.5B非嵌入参数）的**Transformer**模型。此外，还将Transformer与**LSTM**模型以及**循环Transformer（Universal Transformers）** 进行了比较（p.8）。
- **评价指标**：主要指标是在测试集上的**交叉熵损失（cross-entropy loss）**，单位是nats（p.7）。
- **主实验结果**：
    - **幂律验证**：损失L分别与N、D、C呈现清晰的幂律关系，拟合趋势跨越超过6个数量级（p.4, p.8）。
    - **模型形状不敏感**：在N固定时，改变模型深度、宽度等，损失变化仅在几个百分点之内（p.8， 图5）。
    - **过拟合规律**：给出了联合依赖N和D的公式 `L(N,D) = [(N_c/N)^{α_N/α_D} + (D_c/D)]^{α_D}`，并验证了其有效性（p.5， 图4左）。
    - **训练曲线规律**：给出了依赖N和训练步数S的公式 `L(N,S) = (N_c/N)^{α_N} + (S_c/S_min(S))^{α_S}`（p.5， 图4右）。
    - **LSTM对比**：LSTM在上下文前期的token上性能与Transformer相当，但在后期token上性能显著下降，无法有效利用长距离上下文（p.9， 图7）。
    - **泛化能力**：在WebText2上训练的模型，在其他数据分布上的损失也随N平滑改善，改善程度与在WebText2测试损失强相关（p.9， 图8）。
- **消融实验**：文本中未明确使用“消融实验”一词，但通过**控制变量**的方法系统研究了每个因素（N， D， 形状， 批大小等）的影响，这本质上构成了对模型规模各个维度的消融研究。
- **泛化实验**：见上述“主实验结果”中的泛化能力部分。
- **速度/参数量/FLOPs**：
    - 模型参数量N定义为非嵌入参数数量，近似公式为 `N ≈ 12 * n_layer * d_model^2`（p.6）。
    - 训练计算量C估算为 `C ≈ 6 * N * B * S` 浮点运算次数（p.6），其中B是批大小，S是步数。数值以PF-days为单位（1 PF-day = 8.64×10^19 FLOPs）。
    - 论文详细分析了计算效率，指出最优训练在收敛前很早就停止，是计算高效的（p.6）。

## 7. 这篇论文真正有价值的地方
这篇论文最核心的价值在于，它**将深度学习，特别是大模型训练，从一门“艺术”向一门“工程科学”推进了关键一步**。它提供的几个幂律公式，就像是一个“晶体球”，让研究者可以在真正进行昂贵的大规模训练之前，**预测**不同资源配置下的模型性能。
- **对后续研究的启发**：它确立了“规模即性能”的实证基础，极大地推动了后续更大规模模型（如GPT-3， GPT-4）的研发。任何想训练或改进大型语言模型的工作，都必须考虑或参考这些缩放定律。
- **对改模型/做实验的启发**：它提供了明确的指导：如果想提升模型性能，最有效的途径是**同时增加模型大小和数据量**，但模型大小的增长应快于数据量。在资源有限时，应该优先训练一个**远大于收敛所需规模**的模型，并使用**较少的数据**，然后**提前停止**训练。这彻底改变了“用小模型在大数据上训练到收敛”的传统思维。
- **对写论文的启发**：它是一个如何进行大规模、系统性实证研究并从中提炼出简洁优美公式的典范。其论文结构清晰，从观测现象到拟合公式，再到推论和应用，逻辑链条完整。

## 8. 局限与问题
- **架构依赖性**：所有实验和结论均基于**Transformer架构**，特别是仅解码器（decoder-only）变体。对于其他架构（如编码器-解码器、混合专家模型等），这些幂律关系是否完全相同，PDF文本中未明确说明。
- **数据集特异性**：实验主要基于WebText2数据集。其幂律公式的具体常数（如N_c, D_c）可能与数据的特性（如分布、质量、token化方式）强相关。论文提到这些常数“依赖于词汇表大小和token化方式，因此没有根本意义”（p.5）。
- **外推风险**：虽然观察到的趋势跨越了多个数量级，且“在高端没有观察到偏离趋势的迹象”（p.4），但论文承认损失“最终必须在达到零损失之前趋于平稳”（p.4）。将这些关系外推到训练数据或模型规模超出当前研究范围更远的程度，其有效性未经验证。
- **计算成本高昂**：为了获得这些经验公式，作者需要训练数百个不同规模的模型，总计算量巨大。这本身是一个很高的门槛。
- **假设依赖**：最优分配策略（1.7）的推导依赖于一些假设，例如批大小可以自由调整。论文指出最优批大小大约是损失的一个幂函数（公式1.4），并可通过梯度噪声尺度来确定（p.5）。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读 **摘要（Abstract）**、**1.1节总结（Summary）** 和 **1.2节缩放定律总结（Summary of Scaling Laws）**。这能让你用最少时间掌握核心发现和公式。
- **如果复现**：重点阅读 **第2节 背景与方法（Background and Methods）**，了解模型细节、训练过程、计算量估算方式。并查看附录中的具体实验设置。
- **如果借鉴创新点**：应重点学习**第3节和第4节**，理解他们如何设计实验来隔离和验证单个变量（N， D）的影响。以及他们如何从数据中拟合出幂律公式（1.1-1.6）。
- **如果写related work**：可将本文放在**“大语言模型的规模定律”、“Transformer训练动力学”、“计算效率与样本效率”** 这一类中。它是该方向的开创性、奠基性工作。

## 10. 和其他论文的关系
- 根据文件名`Scaling_Laws_for_Neural_Language_Models.pdf`和主题`G_视觉基础模型_VLM_LLM`，本文与后续的大模型工作如 **GPT-3**（其训练直接受到本文缩放定律的指导）和 **Chinchilla**（进一步优化了N和D的分配关系）有直接的理论承继关系。
- 本文对比了LSTMs和Universal Transformers [[DGV+18]]，因此与循环神经网络和Transformer变体的研究相关。
- 论文中提到了一些被引用的工作，如优化器Adam [[KB14]]，梯度噪声尺度 [[MKAT18]]，以及原始的WebText数据集和GPT-2 [[RWC+19]]。
- *注：由于提供的文本仅为前12页，未能包含完整的参考文献列表和所有相关讨论，因此无法进行更全面的关联。*

## 11. 关键词
缩放定律， 幂律， Transformer， 语言模型， 计算效率， 样本效率， 模型大小， 数据集大小， 最优计算分配， 交叉熵损失， 过拟合， 训练动态。

## 12. 可信度说明
本篇精读笔记**主要基于提供的PDF文本前12页内容生成**，包括：摘要、目录、第1节（引言与总结）、第2节（背景与方法）、第3节（部分实证结果）。其中包含的关键公式、数字和结论均直接引用或总结自这几页文本，并注明了可能的页码（p.X）。
提取质量总体较好，文本覆盖了论文的核心框架、主要贡献和部分关键实验结果。但需注意，**论文的后半部分（如第4、5、6节的完整细节，第7、8节的讨论，以及所有附录）未在提供的文本中**，因此关于最优分配策略的完整数学推导、训练曲线拟合的更多细节、以及与其他方法的深入讨论等信息，在本笔记中可能不完整或未提及。对于这些缺失部分，笔记中已明确标注“PDF文本中未明确说明”。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/Scaling_Laws_for_Neural_Language_Models.txt` (30/30 页; 原 AI 主体 12/30 + 全文补读 13-30); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-30; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-30。
- **提取情况**: 缺失页 18 页, 其中 18 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Bcritminimizes the number of training steps, while B
- p.13: Bcritminimizes
- p.13: In Figure 10 we have plotted the critical batch size and gradient noise scale5as a function of training loss for
- p.13: We have chosen this parameterization for Bcrit(L)because as the loss approaches its minimum value Lmin,
- p.13: We will use Bcrit(L)to estimate the relation between the number of training steps Swhile training at batch
- p.14: Parameters (non-embedding)2345678Test LossPerformance vs Compute Budget
- p.14: PF-dayss
- p.14: Parameter
- p.14: SNcSc
- p.14: 5.3 Lower Bound on Early Stopping Step
- p.14: 6 Optimal Allocation of the Compute Budget
- p.14: We displayed the empirical trend of performance as a function of the computation used during training in

### 缺失页关键摘录

- p.13: We demonstrate the relation (5.1) for Transformers in Figure 18 in the appendix. This relation deﬁnes the
- p.13: In Figure 10 we have plotted the critical batch size and gradient noise scale5as a function of training loss for
- p.14: With these parameters, we obtain the learning curve ﬁts in Figure 4. Though the ﬁts are imperfect, we believe
- p.14: The data and ﬁts can be visualized in a different and more interesting way, as shown in Figure 11. There we
- p.14: parison to the empirical data is displayed in Figure 16 in the appendix. In that ﬁgure, the values of Sstop
- p.14: the top-right of Figure 1. However, this result involved training at a ﬁxed batch size B, whereas we know
- p.15: Figure 12 Left: Given a ﬁxed compute budget, a particular model size is optimal, though somewhat larger
- p.15: Figure 13 When adjusting performance to simulate training far below the critical batch size, we ﬁnd a
- p.15: Let us ﬁrst study the loss as a function of the optimally allocated compute from Equation (5.5). The result is
- p.15: plotted in Figure 13, along with a power-law ﬁt. We see that as compared to the compute plot of Figure 1, the
- p.15: given quantity of training compute. The optimal model size is shown in Figure 14. We observe that N(Cmin)
- p.16: S (fixed-batch)Figure 14 Left: Each value of the compute budget Cminhas an associated optimal model size N. Optimal
<!-- AI_READING_NOTE_END -->
