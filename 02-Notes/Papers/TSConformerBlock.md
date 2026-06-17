---
title: "CMGAN: Conformer-Based Metric-GAN for"
authors:
  - "Sherif Abdulatif"
  - "Ruizhe Cao"
  - "Bin Yang"
year: 2022
venue: "arXiv"
doi: 
pdf: [[TSConformerBlock.pdf]]
primary_topic: B_注意力算子模块
topics:
  - "B_注意力算子模块"
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
extract_cache: .paper-cache/extracts/TSConformerBlock.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# CMGAN: Conformer-Based Metric-GAN for

## 基本信息
- **PDF**: [[TSConformerBlock.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | CMGAN: Conformer-Based Metric-GAN for |
| **作者** | Sherif Abdulatif; Ruizhe Cao; Bin Yang |
| **发表时间** | 2022 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> —In this work, we further develop the conformer- domain. This limitation is usually reflected as artifacts in the based metric generative adversarial network (CMGAN) model1 reconstructed speech. Another drawback of this paradigm is forspeechenhancement(SE)inthetime-frequency(TF)domain. the ample input space associated with the raw waveforms, This paper builds on our previous work but takes a more in- which often necessitates the utilization of deep computation- depth look by conducting extensive ablation studies on model inputs and architectural design choices. We rigorously tested ally complex frameworks [14], [17]. the generalization ability of the model to unseen noise types In the TF-domain, most conventional model-based or DL and distortions. We have fortified our claims through DNS- techniquesprioritizethemagnitudecomponentandoftenover- MOS measurements and listening tests. Rather than focusing look the phase. This omission stems from the complex and exclusively on the speech den

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**: 现实应用（如语音识别、通信）对语音质量要求高，需要高效的语音增强系统。现有方法存在局限。
- **之前方法的问题**:
    1.  **时域方法**：缺乏显式的频率表征，容易产生伪影；处理原始波形输入空间大，需要很深的复杂网络 (p.1)。
    2.  **传统时频域方法**：大多只增强幅度谱，忽略复杂难处理的相位信息，导致质量下降 (p.1)。
    3.  **直接增强复数谱图**：存在幅度与相位之间的“补偿效应”，即为了补偿相位估计的误差，模型会扭曲幅度估计 (p.3)。
    4.  **优化目标**：常用的逐点损失（如ℓp范数）与最终的感知质量（如PESQ）不总是一致 (p.1)。
- **核心矛盾**：如何在时频域中**同时、有效地建模并增强语音的幅度和相位信息**，并且使模型优化目标与人类的感知质量对齐。
## 关键贡献

1.  **提出CMGAN生成器新架构**：设计了一个共享编码器，同时输入拼接的幅度谱和复数谱（实部与虚部），并采用一个专门的掩模解码器（用于幅度）和一个共享解码器（用于实部和虚部），优化了参数共享和表示学习 (p.2)。
2.  **引入两阶段Conformer块（TS-Conformer）**：作为核心注意力模块，第一阶段捕获时间依赖性，第二阶段捕获频率依赖性，有效利用了Conformer结合CNN（局部特征）和Transformer（全局依赖）的优势 (p.2, p.5)。
3.  **集成度量判别器**：摒弃仅优化点损失的方式，引入一个度量判别器来学习并优化一个不可微的黑盒评估指标（如PESQ），直接提升生成语音的感知质量 (p.2)。
4.  **将模型扩展到多个SE任务**：不仅限于去噪，还系统地探索和验证了模型在**去混响**和**复数时频域超分辨率**任务上的有效性，后者是该领域的早期工作之一 (p.1)。
5.  **全面的实验验证**：通过广泛的消融实验和泛化能力测试（在未见过的噪声和失真上），并结合DNS-MOS和听力测试，强有力地证明了模型的优越性和鲁棒性 (p.1)。
## 方法

### 整体框架
CMGAN是一个生成对抗网络（GAN），包含一个**生成器（Generator）** 和一个**度量判别器（Metric Discriminator）** (p.2)。生成器负责从失真语音的时频表示中估计增强后的语音表示，判别器则用于优化生成器的输出与目标评估指标（如PESQ分数）的匹配程度。

### 输入输出
- **输入**: 语音波形 `y`。首先通过短时傅里叶变换（STFT）转换为复数谱图 `Yo`，再进行**幂律压缩** (公式2, p.4)：`Y = |Yo|^c * exp(jYp)`，其中 `c=0.3`。最终输入是压缩后的幅度谱 `Ym` 与复数谱的实部 `Yr`、虚部 `Yi` **拼接** 而成的 `Yin ∈ R^{B×T×F×3}`。
- **输出**: 增强后的幅度谱掩模 `M`，以及增强后的复数谱残差 `ΔYr` 和 `ΔYi`。最终的增强复数谱通过任务特定的操作（如掩蔽或相加）得到。

### 关键模块与连接方式
1.  **编码器（Encoder）**: 由两个卷积块和一个**膨胀DenseNet**组成 (p.4)。膨胀DenseNet包含四个卷积块（膨胀率分别为1,2,4,8），通过密集连接聚合多尺度特征，同时扩大感受野。最后一个卷积块将频率维度减半以降低复杂度。
2.  **两阶段Conformer块（TS-Conformer）**: **这是论文最核心的注意力模块**。给定编码器输出的特征图 `D`，首先将其重塑为 `DT` 以专注于**时间维度**，送入第一个Conformer块（捕获时间依赖）；输出经残差连接后，再重塑为 `DF` 以专注于**频率维度**，送入第二个Conformer块（捕获频率依赖）；最终输出经残差连接并恢复原始形状 (p.5, Fig. 2b)。每个Conformer块内部集成了多头自注意力（捕获全局依赖）和卷积模块（捕获局部上下文）。
3.  **解码器（Decoder）**: 特征从TS-Conformer输出后，**分流**为两个分支：
    - **掩模解码器（Mask Decoder）**: 预测一个**幅度掩模 `M`**，通过逐元素乘法作用于输入幅度谱，完成幅度增强。
    - **共享解码器（Shared Decoder）**: 预测复数谱的**残差 `ΔYr`, `ΔYi`**，通过**加法**作用于输入的复数谱实部和虚部，完成相位及精细幅度的增强 (Fig. 2a)。
4.  **度量判别器**: 一个独立的网络，用于评估生成语音的特定感知指标分数（如PESQ），并指导生成器进行优化 (Fig. 2c)。

### 训练与推理
- **训练**: 采用对抗训练。生成器使用混合损失：**对抗损失**（让判别器无法区分增强语音与目标语音的评分）和**感知损失**（点损失，如均方误差）。判别器则学习准确预测语音的评估指标分数 (p.1)。
- **推理**: 仅使用生成器。输入失真语音，输出增强后的幅度掩模和复数谱残差，通过任务定义的组合操作得到最终增强复数谱，再进行逆STFT还原为波形。

### 与已有方法的差异
- **不同于传统双分支模型**（为幅度和复数分别使用独立网络），CMGAN使用**共享编码器**学习统一表示，然后分流，参数更少且表示更丰富 (p.1)。
- **区别于仅优化点损失的方法**，CMGAN引入**度量判别器**直接优化感知质量指标。
- **TS-Conformer块**是专为语音时频特性设计的注意力模块，依次建模时间和频率的长距离依赖，区别于单阶段的Transformer或CNN模块。
## 实验

- **使用的数据集**:
    - 去噪: Voice Bank+DEMAND数据集 (p.2)。
    - 泛化测试: 提及在三个不同数据集上测试，但具体名称未在提供的文本中列出 (p.2)。
- **对比方法**: 文中称与现有SOTA方法对比，但具体方法名称在提供的摘要和引言部分未完全列出。
- **评价指标**: PESQ, SSNR (信噪比增益), DNS-MOS (p.1)。
- **主实验结果**:
    - 去噪任务: 在Voice Bank+DEMAND上，CMGAN达到了 **PESQ 3.41** 和 **SSNR 11.10 dB** (p.1)。
- **消融实验**: 论文进行了广泛的消融研究，包括模型输入（p.1）和架构设计选择（p.1），具体结论需阅读全文获取。
- **泛化实验**: 在**未见过的噪声类型和失真**上测试了模型的泛化能力 (p.1)。
- **速度/参数量/FLOPs**: 在提供的文本中未明确说明。
## 局限

- **计算成本**：尽管引入了膨胀DenseNet和TS-Conformer，但GNN和Transformer类模型通常计算量较大，文中未提供详细的FLOPs或推理时间对比，实时部署可能存在挑战。
- **数据集与任务范围**：主要实验基于Voice Bank+DEMAND数据集，虽然测试了泛化性，但未在更大规模、更多样化的工业数据集上验证。超分辨率和去混响的单独实验结果在提供的文本中未详细给出。
- **复现风险**：模型结构较为复杂，涉及多个模块（膨胀DenseNet、两阶段Conformer、双解码器）和训练技巧（GAN训练），完全复现可能需要作者开源的代码。
- **假设依赖**：方法基于时频域处理，需要进行STFT和ISTFT变换，这引入了窗长、帧移等超参数，且对于非平稳噪声的极端情况，时频变换本身可能不是最优选择。
## 个人评论

1.  **模块设计思路**：**TS-Conformer块**的设计非常巧妙。它不直接使用一个庞大的二维注意力，而是将时间建模和频率建模**解耦成两个顺序的一维（或跨维度）注意力阶段**，既降低了计算复杂度，又明确地让模型学习语音信号在时频两个轴上的不同依赖特性，这对于理解如何为语音等序列数据设计高效注意力模块很有启发。
2.  **工程与研究结合**：论文展示了如何将**共享表示学习**（通过共享编码器）和**任务特定解码**（分流的掩模和复数解码器）结合，在减少参数的同时有效处理幅度和相位这两个既相关又不同的目标。
3.  **研究范式**：将**MetricGAN**的思想成功扩展到去混响和超分辨率等多任务，并针对超分辨率任务创新性地提出了**复数域掩模重建**方法，展示了如何将一个核心框架迁移到相关但不同的子问题上。
4.  **严谨性**：论文通过广泛的消融、跨数据集泛化测试以及主观（听力测试）和客观（DNS-MOS）评估相结合，展示了良好的研究严谨性。

### 使用建议

- **快速了解**：阅读**摘要（Abstract）** 和**引言（Introduction）** 的前几页，可以快速掌握论文解决的问题、核心方法和主要结果。
- **重点复现**：仔细研读**方法论（Methodology）** 部分（特别是III-A节）和论文配套的开源代码（https://github.com/ruizhecao96/CMGAN），理解TS-Conformer块的实现细节和整个生成器-判别器的训练流程。
- **借鉴创新点**：
    - **学习模块设计**：重点研究 **TS-Conformer块** 如何拆分并顺序建模时间和频率依赖，可以尝试将其思想应用到其他时序或频谱数据（如音乐生成、EEG分析）的模型中。
    - **学习多任务框架**：学习CMGAN如何通过共享编码器和少量任务特定模块，同时处理幅度和相位两个目标。
- **写Related Work**：可将本论文放在 **“基于时频域的深度学习语音增强方法”** 或 **“注意力机制在语音处理中的应用”** 相关工作章节中，作为结合Conformer和MetricGAN的代表性工作进行引述。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**语音增强（Speech Enhancement, SE）** 领域，专注于利用深度学习技术在**时频（Time-Frequency, TF）域**提升语音质量与可懂度。论文提出了一种名为CMGAN的模型，系统性地解决了语音去噪（denoising）、去混响（dereverberation）和超分辨率（super-resolution）三个核心任务。该论文的核心技术贡献点在于**设计了一种新颖的注意力算子模块（Two-Stage Conformer Block）**，因此适合放在 `B_注意力算子模块` 主题下进行精读。

## 2. 一句话总结
本文提出了CMGAN，一种结合Conformer与度量生成对抗网络（MetricGAN）的时频域语音增强框架，通过共享编码器和两阶段（时间-频率）Conformer注意力块有效建模语音的局部与全局依赖关系，并在去噪、去混响和超分辨率三项任务上达到了当时的最优性能。

## 3. 背景与问题
- **为什么要做**: 现实应用（如语音识别、通信）对语音质量要求高，需要高效的语音增强系统。现有方法存在局限。
- **之前方法的问题**:
    1.  **时域方法**：缺乏显式的频率表征，容易产生伪影；处理原始波形输入空间大，需要很深的复杂网络 (p.1)。
    2.  **传统时频域方法**：大多只增强幅度谱，忽略复杂难处理的相位信息，导致质量下降 (p.1)。
    3.  **直接增强复数谱图**：存在幅度与相位之间的“补偿效应”，即为了补偿相位估计的误差，模型会扭曲幅度估计 (p.3)。
    4.  **优化目标**：常用的逐点损失（如ℓp范数）与最终的感知质量（如PESQ）不总是一致 (p.1)。
- **核心矛盾**：如何在时频域中**同时、有效地建模并增强语音的幅度和相位信息**，并且使模型优化目标与人类的感知质量对齐。

## 4. 核心贡献
1.  **提出CMGAN生成器新架构**：设计了一个共享编码器，同时输入拼接的幅度谱和复数谱（实部与虚部），并采用一个专门的掩模解码器（用于幅度）和一个共享解码器（用于实部和虚部），优化了参数共享和表示学习 (p.2)。
2.  **引入两阶段Conformer块（TS-Conformer）**：作为核心注意力模块，第一阶段捕获时间依赖性，第二阶段捕获频率依赖性，有效利用了Conformer结合CNN（局部特征）和Transformer（全局依赖）的优势 (p.2, p.5)。
3.  **集成度量判别器**：摒弃仅优化点损失的方式，引入一个度量判别器来学习并优化一个不可微的黑盒评估指标（如PESQ），直接提升生成语音的感知质量 (p.2)。
4.  **将模型扩展到多个SE任务**：不仅限于去噪，还系统地探索和验证了模型在**去混响**和**复数时频域超分辨率**任务上的有效性，后者是该领域的早期工作之一 (p.1)。
5.  **全面的实验验证**：通过广泛的消融实验和泛化能力测试（在未见过的噪声和失真上），并结合DNS-MOS和听力测试，强有力地证明了模型的优越性和鲁棒性 (p.1)。

## 5. 方法详解
### 整体框架
CMGAN是一个生成对抗网络（GAN），包含一个**生成器（Generator）** 和一个**度量判别器（Metric Discriminator）** (p.2)。生成器负责从失真语音的时频表示中估计增强后的语音表示，判别器则用于优化生成器的输出与目标评估指标（如PESQ分数）的匹配程度。

### 输入输出
- **输入**: 语音波形 `y`。首先通过短时傅里叶变换（STFT）转换为复数谱图 `Yo`，再进行**幂律压缩** (公式2, p.4)：`Y = |Yo|^c * exp(jYp)`，其中 `c=0.3`。最终输入是压缩后的幅度谱 `Ym` 与复数谱的实部 `Yr`、虚部 `Yi` **拼接** 而成的 `Yin ∈ R^{B×T×F×3}`。
- **输出**: 增强后的幅度谱掩模 `M`，以及增强后的复数谱残差 `ΔYr` 和 `ΔYi`。最终的增强复数谱通过任务特定的操作（如掩蔽或相加）得到。

### 关键模块与连接方式
1.  **编码器（Encoder）**: 由两个卷积块和一个**膨胀DenseNet**组成 (p.4)。膨胀DenseNet包含四个卷积块（膨胀率分别为1,2,4,8），通过密集连接聚合多尺度特征，同时扩大感受野。最后一个卷积块将频率维度减半以降低复杂度。
2.  **两阶段Conformer块（TS-Conformer）**: **这是论文最核心的注意力模块**。给定编码器输出的特征图 `D`，首先将其重塑为 `DT` 以专注于**时间维度**，送入第一个Conformer块（捕获时间依赖）；输出经残差连接后，再重塑为 `DF` 以专注于**频率维度**，送入第二个Conformer块（捕获频率依赖）；最终输出经残差连接并恢复原始形状 (p.5, Fig. 2b)。每个Conformer块内部集成了多头自注意力（捕获全局依赖）和卷积模块（捕获局部上下文）。
3.  **解码器（Decoder）**: 特征从TS-Conformer输出后，**分流**为两个分支：
    - **掩模解码器（Mask Decoder）**: 预测一个**幅度掩模 `M`**，通过逐元素乘法作用于输入幅度谱，完成幅度增强。
    - **共享解码器（Shared Decoder）**: 预测复数谱的**残差 `ΔYr`, `ΔYi`**，通过**加法**作用于输入的复数谱实部和虚部，完成相位及精细幅度的增强 (Fig. 2a)。
4.  **度量判别器**: 一个独立的网络，用于评估生成语音的特定感知指标分数（如PESQ），并指导生成器进行优化 (Fig. 2c)。

### 训练与推理
- **训练**: 采用对抗训练。生成器使用混合损失：**对抗损失**（让判别器无法区分增强语音与目标语音的评分）和**感知损失**（点损失，如均方误差）。判别器则学习准确预测语音的评估指标分数 (p.1)。
- **推理**: 仅使用生成器。输入失真语音，输出增强后的幅度掩模和复数谱残差，通过任务定义的组合操作得到最终增强复数谱，再进行逆STFT还原为波形。

### 与已有方法的差异
- **不同于传统双分支模型**（为幅度和复数分别使用独立网络），CMGAN使用**共享编码器**学习统一表示，然后分流，参数更少且表示更丰富 (p.1)。
- **区别于仅优化点损失的方法**，CMGAN引入**度量判别器**直接优化感知质量指标。
- **TS-Conformer块**是专为语音时频特性设计的注意力模块，依次建模时间和频率的长距离依赖，区别于单阶段的Transformer或CNN模块。

## 6. 实验与结果
- **使用的数据集**:
    - 去噪: Voice Bank+DEMAND数据集 (p.2)。
    - 泛化测试: 提及在三个不同数据集上测试，但具体名称未在提供的文本中列出 (p.2)。
- **对比方法**: 文中称与现有SOTA方法对比，但具体方法名称在提供的摘要和引言部分未完全列出。
- **评价指标**: PESQ, SSNR (信噪比增益), DNS-MOS (p.1)。
- **主实验结果**:
    - 去噪任务: 在Voice Bank+DEMAND上，CMGAN达到了 **PESQ 3.41** 和 **SSNR 11.10 dB** (p.1)。
- **消融实验**: 论文进行了广泛的消融研究，包括模型输入（p.1）和架构设计选择（p.1），具体结论需阅读全文获取。
- **泛化实验**: 在**未见过的噪声类型和失真**上测试了模型的泛化能力 (p.1)。
- **速度/参数量/FLOPs**: 在提供的文本中未明确说明。

## 7. 这篇论文真正有价值的地方
1.  **模块设计思路**：**TS-Conformer块**的设计非常巧妙。它不直接使用一个庞大的二维注意力，而是将时间建模和频率建模**解耦成两个顺序的一维（或跨维度）注意力阶段**，既降低了计算复杂度，又明确地让模型学习语音信号在时频两个轴上的不同依赖特性，这对于理解如何为语音等序列数据设计高效注意力模块很有启发。
2.  **工程与研究结合**：论文展示了如何将**共享表示学习**（通过共享编码器）和**任务特定解码**（分流的掩模和复数解码器）结合，在减少参数的同时有效处理幅度和相位这两个既相关又不同的目标。
3.  **研究范式**：将**MetricGAN**的思想成功扩展到去混响和超分辨率等多任务，并针对超分辨率任务创新性地提出了**复数域掩模重建**方法，展示了如何将一个核心框架迁移到相关但不同的子问题上。
4.  **严谨性**：论文通过广泛的消融、跨数据集泛化测试以及主观（听力测试）和客观（DNS-MOS）评估相结合，展示了良好的研究严谨性。

## 8. 局限与问题
- **计算成本**：尽管引入了膨胀DenseNet和TS-Conformer，但GNN和Transformer类模型通常计算量较大，文中未提供详细的FLOPs或推理时间对比，实时部署可能存在挑战。
- **数据集与任务范围**：主要实验基于Voice Bank+DEMAND数据集，虽然测试了泛化性，但未在更大规模、更多样化的工业数据集上验证。超分辨率和去混响的单独实验结果在提供的文本中未详细给出。
- **复现风险**：模型结构较为复杂，涉及多个模块（膨胀DenseNet、两阶段Conformer、双解码器）和训练技巧（GAN训练），完全复现可能需要作者开源的代码。
- **假设依赖**：方法基于时频域处理，需要进行STFT和ISTFT变换，这引入了窗长、帧移等超参数，且对于非平稳噪声的极端情况，时频变换本身可能不是最优选择。

## 9. 我该怎么使用这篇论文
- **快速了解**：阅读**摘要（Abstract）** 和**引言（Introduction）** 的前几页，可以快速掌握论文解决的问题、核心方法和主要结果。
- **重点复现**：仔细研读**方法论（Methodology）** 部分（特别是III-A节）和论文配套的开源代码（https://github.com/ruizhecao96/CMGAN），理解TS-Conformer块的实现细节和整个生成器-判别器的训练流程。
- **借鉴创新点**：
    - **学习模块设计**：重点研究 **TS-Conformer块** 如何拆分并顺序建模时间和频率依赖，可以尝试将其思想应用到其他时序或频谱数据（如音乐生成、EEG分析）的模型中。
    - **学习多任务框架**：学习CMGAN如何通过共享编码器和少量任务特定模块，同时处理幅度和相位两个目标。
- **写Related Work**：可将本论文放在 **“基于时频域的深度学习语音增强方法”** 或 **“注意力机制在语音处理中的应用”** 相关工作章节中，作为结合Conformer和MetricGAN的代表性工作进行引述。

## 10. 和其他论文的关系
根据主题 `B_注意力算子模块` 和文件名 `2022_注意力算子模块_CMGAN_Conformer-Based.pdf`，本文提出的核心 **TS-Conformer块** 与以下可能相关：
- 其他使用或改进**Conformer**或**Transformer**进行语音/音频处理的论文。
- 提出各种**注意力变体**（如多尺度、局部-全局）用于序列建模的论文。
- 其他将**MetricGAN**应用于不同任务的论文。
（注：由于“库里”的具体内容未知，此处仅根据通用主题进行合理推测，未使用双链。）

## 11. 关键词
语音增强 (Speech Enhancement)
Conformer
度量生成对抗网络 (MetricGAN)
时频域 (Time-Frequency Domain)
注意力机制 (Attention Mechanism)
两阶段Conformer块 (Two-Stage Conformer Block)
去噪 (Denoising)
去混响 (Dereverberation)
超分辨率 (Super-Resolution)
相位处理 (Phase Processing)

## 12. 可信度说明
本精读笔记**完全基于**用户提供的《2022_注意力算子模块_CMGAN_Conformer-Based.pdf》提取文本（前12页）生成。该提取文本覆盖了论文的摘要、引言、相关工作、问题陈述以及详细方法论部分，内容详实，足以支撑对论文核心思想、创新点和技术细节的全面阐述。由于提取文本仅包含前12页（共17页），后续关于完整实验结果、详细消融分析、结论等内容未被包含，因此笔记中“实验与结果”和“局限与问题”部分的相关内容是基于已有文本的合理推断或注明未明确说明，未进行编造。总体而言，文本提取质量良好，关键信息充足。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/TSConformerBlock.txt` (17/17 页; 原 AI 主体 12/17 + 全文补读 13-17); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Experimental results demonstrate that the proposed method
- p.13: Additionally, we conduct an ablation study to verify the
- p.13: ACKNOWLEDGMENTS
- p.13: We would like to thank the Institute of Natural Lan-
- p.13: APPENDIX
- p.13: The complete architectural details of both generator and
- p.13: Additionally, this section presents a visualization of the
- p.13: A wide-band non-stationary cafe noise from the DEMAND
- p.13: In general, stationary noises are less challenging than non-
- p.13: REFERENCES
- p.13: Conference on Latent Variable Analysis and Signal Separation , 2015,
- p.13: International Conference on Acoustics, Speech and Signal Processing

### 缺失页关键摘录

- p.13: by directly enhancing non-differentiable evaluation scores.
- p.13: Additionally, we conduct an ablation study to verify the
- p.13: proposed CMGAN framework. Finally, subjective evaluation
- p.13: discriminator are outlined in Table VI. The hyperparameters
- p.13: CMGAN in comparison to subjective evaluation methods.
- p.13: dataset (SNR = 0 dB) and a narrow-band high-frequency
- p.13: stationary doorbell noise from the Freesound dataset (SNR
- p.13: challenge: Dataset, task and baselines,” in IEEE Workshop on Auto-
- p.14: direct evaluation metrics optimization by fully convolutional neural
- p.15: [94] K. Wilson et al. , “Exploring tradeoffs in models for low-latency speech
- p.15: [99] A. Rix et al. , “Perceptual evaluation of speech quality (PESQ)-a
- p.15: [110] Y . Hu and P. C. Loizou, “Evaluation of objective quality measures
<!-- AI_READING_NOTE_END -->
