---
title: "MSGNet: Learning Multi-Scale Inter-Series Correlations for Multivariate Time"
authors:
  - "SichuanUniversity"
  - "BeijingInstituteofTechnology"
year: 2018
venue: Intelligence(www.aaai.org).Allrightsreserved.
doi: 
pdf: [[ScaleGraphBlock.pdf]]
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
extract_cache: .paper-cache/extracts/ScaleGraphBlock.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/14 pages"
---
# MSGNet: Learning Multi-Scale Inter-Series Correlations for Multivariate Time

## 基本信息
- **PDF**: [[ScaleGraphBlock.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | MSGNet: Learning Multi-Scale Inter-Series Correlations for Multivariate Time |
| **作者** | SichuanUniversity; BeijingInstituteofTechnology |
| **发表时间** | 2018 |
| **刊物/会议** | Intelligence(www.aaai.org).Allrightsreserved. |
| **DOI** | 未明确 |

## 摘要

> pos corr Multivariate time series forecasting poses an ongoing chal- neg corr lenge across various disciplines. Time series data often ex- hibit diverse intra-series and inter-series correlations, con- tributingtointricateandinterwovendependenciesthathave been the focus of numerous studies. Nevertheless, a signif- icant research gap remains in comprehending the varying scale1 inter-series correlations across different time scales among observation multipletimeseries,anareathathasreceivedlimitedatten- tionintheliterature.Tobridgethisgap,thispaperintroduces MSGNet,anadvanceddeeplearningmodeldesignedtocap- turethevaryinginter-seriescorrelationsacrossmultipletime scales using frequency domain analysis and adaptive graph convolution.Byleveragingfrequencydomainanalysis,MS- GNeteffectivelyextractssalientperiodicpatternsanddecom- posesthetimeseriesintodistincttimescales.Themodelin- corporatesaself-attentionmechanismtocaptureintra-series dependencies, while introducing an adaptive mixhop graph 

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：现实世界中的多元时间序列（如金融、生态数据）存在复杂的序列间相关性，且这些相关性会随着时间尺度（如日、月、年）的不同而变化（例如，两个股票在长周期上正相关，在短周期上可能负相关）。现有模型对此关注不足。
- **之前方法的问题**：
    1.  许多使用图神经网络（GNN）的模型采用**固定的或单一的图结构**来描述序列间关系，无法捕捉这种随尺度变化的相关性。
    2.  一些方法考虑使用**动态图结构**，但忽略了图结构可能与**稳定的、有意义的时间周期**（如经济周期）密切相关这一事实。
- **核心矛盾**：现有深度学习模型难以**同时、准确地建模序列内依赖（intra-series）和跨尺度的序列间依赖（inter-series）**，尤其是后者在不同时间尺度上的多样性。
## 关键贡献

1.  **关键观察与问题定义**：明确指出多元时间序列的序列间相关性与不同的时间尺度紧密相关。
2.  **提出MSGNet框架**：设计了新颖的`ScaleGraphBlock`，首次将序列间相关性建模与时间尺度（通过FFT识别）显式关联。
3.  **多尺度图卷积模块**：引入**自适应混合跳（adaptive Mixhop）图卷积层**，为每个时间尺度动态学习一个独立的邻接矩阵，以捕捉该尺度下特定的序列间依赖。
4.  **联合建模策略**：将用于序列内相关性建模的**多头自注意力机制**与上述多尺度图卷积模块结合，形成统一的框架。
5.  **实验与泛化验证**：在多个真实世界数据集上验证了模型的有效性和优越性，特别是通过COVID-19期间的航班数据（OOD样本）展示了模型强大的泛化能力。
## 方法

- **整体框架**：如图2所示，MSGNet由多个相同的`ScaleGraphBlock`堆叠而成，并通过残差连接。每个`ScaleGraphBlock`包含四个核心步骤：尺度识别、多尺度图卷积、多头注意力、尺度聚合。
- **输入与输出**：
    - 输入：`X_{t-L:t} \in R^{N×L}`，表示N个变量在回看窗口L个时间点的观测值。
    - 输出：`\hat{X}_{t:t+T} \in R^{N×T}`，表示对N个变量未来T个时间步的预测。
- **关键模块详解**：
    1.  **输入嵌入与残差连接** (Eq.1, Eq.2)
        - 先对输入进行归一化，然后通过1D卷积、位置编码和可学习的时间戳编码将其嵌入到`d_model`维空间，得到`X_emb`。
        - 模型主体采用残差结构：`X^l = ScaleGraphBlock(X^{l-1}) + X^{l-1}`。
    2.  **尺度识别** (Eq.3, Eq.4) - **FFT模块**
        - 对嵌入后的序列进行**快速傅里叶变换(FFT)**，计算频率幅值并平均，得到频谱`F`。
        - 选取幅值最大的`k`个频率对应的周期`s_i = L / f_i`作为主要时间尺度。
        - 根据尺度`s_i`和对应的周期数`f_i`，将原始输入`X_in`通过零填充和重塑，得到`k`个尺度的3D张量`X_i ∈ R^{d_model × s_i × f_i}`。这是将长序列“折叠”成多个二维序列（周期×个数）。
    3.  **多尺度自适应图卷积** (Eq.5, Eq.6, Eq.7) - **图卷积模块**
        - 对于每个尺度张量`X_i`，先通过线性层投影回`N`个变量维度，得到`H_i ∈ R^{N × s_i × f_i}`。
        - **自适应图学习**：为每个尺度学习两个可训练参数矩阵`E1_i`, `E2_i ∈ R^{N×h}`，通过`A_i = SoftMax(ReLU(E1_i * E2_i^T))`生成该尺度的邻接矩阵`A_i ∈ R^{N×N}`。
        - **Mixhop图卷积**：在邻接矩阵`A_i`及其幂次`(A_i)^j`上对`H_i`进行图卷积，然后拼接结果，通过激活函数，得到融合了多跳邻居信息的输出`H_i^out`。最后再通过MLP映射回`d_model`维。
    4.  **多头注意力与尺度聚合** (Eq.8, Eq.9) - **注意力模块**
        - 对每个尺度的张量`\hat{X}_i`，在**时间尺度维度(s_i)** 上应用**多头自注意力(MHA)**，捕捉该尺度内的序列内时序依赖。
        - **尺度聚合**：将各尺度输出重塑回2D矩阵`\hat{X}_i^out ∈ R^{d_model × L}`。根据FFT计算的对应幅值`F_{f_i}`，通过SoftMax计算权重`\hat{a}_i`，对各尺度结果进行加权求和，得到最终聚合表示`\hat{X}_{out}`。这是一种“专家混合”(MoE)策略。
- **输出层** (Eq.10)：通过两个线性层分别沿变量维度(`W_s`)和时间维度(`W_t`)投影`\hat{X}_{out}`，得到最终预测`\hat{X}_{t:t+T}`。
- **训练方式**：使用均方误差(MSE)作为损失函数。
- **推理流程**：与前向传播流程一致，给定输入序列，通过上述步骤生成预测。
- **与已有方法的差异**：
    - 与传统使用固定图的GNN（如MTGnn）不同，MSGNet为每个有意义的周期学习独立的图结构。
    - 与TimesNet（也用FFT）不同，TimesNet将序列变换到二维空间是为了更好地进行卷积，而MSGNet是为了学习不同尺度下的图结构关系。
    - 核心创新在于首次将“时间尺度”作为学习序列间相关性的一个显式维度。
- **论文类型特化 (注意力类)**：
    - **注意力作用维度**：本文的多头注意力作用在**时间尺度维度**（即每个周期内部的时间步），而非传统的通道或空间维度。这可以看作是一种在频率分解后的子序列上应用的注意力。
    - **可插入网络**：`ScaleGraphBlock`是模块化的设计，可以堆叠（公式2），具有即插即用的潜力。
    - **计算量 vs 效果**：论文通过结合轻量的FFT和有效的图卷积、注意力机制，在多个基准上取得了SOTA效果，但未在提供的文本中给出具体的计算量（FLOPs）或参数量对比数据。
## 实验

- **使用的数据集**：共8个，包括：**Flight**（COVID-19期间航班数据，用于OOD测试）、**Weather**、**ETTh1, ETTh2, ETTm1, ETTm2**、**Exchange-Rate**、**Electricity**。
- **对比方法**：6个基线模型：**Informer**, **Autoformer** (Transformer类), **MTGnn** (图卷积类), **DLinear, NLinear** (线性模型), **TimesNet** (基于周期分解的SOTA)。
- **评价指标**：均方误差(**MSE**)。
- **主实验结果**：论文声称“MSGNet consistently outperforms existing deep learning models”，但提供的文本中**未给出具体的MSE数值表格**。因此无法列出关键数字。
- **消融实验**：论文提及在附录中有关于注意力模块有效性和尺度聚合策略等的消融实验，但**提供的PDF文本中未包含**。
- **泛化实验**：使用**Flight**数据集评估。该数据包含COVID-19冲击导致的分布外(OOD)样本。论文指出模型在此数据上表现出“strong generalization capabilities”，但具体性能数字**未在提供的文本中给出**。
- **速度/参数量/FLOPs**：**PDF文本中未提供**任何关于模型效率（如训练时间、推理速度、参数量、FLOPs）的具体信息。
## 局限

1.  **计算复杂度**：为每个时间尺度学习一个完整的N×N邻接矩阵，并进行图卷积，当变量N很大时，计算和内存开销可能很高。论文**未讨论此问题**。
2.  **假设依赖**：模型效果依赖于数据中存在**强且稳定的周期性**。对于随机性强、无明显周期的数据（如某些金融高频数据），FFT可能无法提取有效尺度，模型性能可能下降。
3.  **实验深度**：提供的文本中缺乏关键的消融实验细节和具体的性能数字，使得对各模块贡献的评估不够直观。
4.  **数据集范围**：实验虽涵盖了多个数据集，但领域仍相对有限（能源、天气、金融），在更广泛领域（如医学信号、社交网络）的有效性有待验证。
## 个人评论

1.  **洞察与视角**：提出了“序列间相关性具有多尺度性”这一关键且直观的洞见，为多元时间序列建模提供了新的思考维度。
2.  **框架创新**：设计了优雅的`ScaleGraphBlock`，将**频率分析(FFT)、图结构学习(自适应GNN)、序列内注意力(MHA)** 三者有机结合，逻辑清晰，模块化强。特别是“为每个频率/周期学习一个图”的思路极具启发性。
3.  **方法设计**：将频率幅值作为聚合权重的“专家混合”策略简单有效；使用Mixhop图卷积来增强图表示能力。
4.  **研究示范**：展示了如何从具体问题（多尺度相关性）出发，设计一个端到端的深度学习解决方案，并从多个角度（方法、实验、可视化）进行论证，是很好的研究范例。

### 使用建议

- **如果快速了解**：阅读**Abstract、Introduction**和**Conclusion**部分，重点关注图1和图2，可以快速理解其核心动机和框架。
- **如果复现**：重点精读**Methodology**部分，特别是公式(3)-(9)关于尺度识别、图学习和卷积的具体实现步骤。需参考其**官方代码库**（链接在摘要中）及附录中的超参数设置。
- **如果借鉴创新点**：
    - 可以借鉴“**为不同频率分量学习独立关系**”的思想，应用于其他需要处理多尺度依赖的时序任务（如检测、分类）。
    - 学习其**模块组合方式**（FFT+GNN+Attention）的设计思路。
    - 参考其利用**频率幅值进行动态加权聚合**的技巧。
- **如果写related work**：
    - 可放在**GNN用于时间序列预测**小节，作为使用可学习图结构的先进工作。
    - 可放在**时间序列多尺度分析或周期建模**小节。
    - 可放在**序列间相关性建模**小节。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**多元时间序列预测**研究方向，聚焦于解决不同时间尺度下时间序列之间相关性（inter-series correlation）建模不充分的问题。该论文的核心是提出了一个结合频率分析、图神经网络和注意力机制的新模块。因此，它最适合放在**B_注意力算子模块**这一主题下，但更准确地定位是“结合注意力与图卷积的多尺度序列建模模块”。

## 2. 一句话总结
本文提出MSGNet模型，通过**频率域分解识别多个时间尺度**，并为每个尺度**学习独立的图结构**来捕捉多元序列间在不同周期下的动态相关性，同时利用**多头注意力机制**建模序列内依赖，从而显著提升多元时间序列预测的准确性。

## 3. 背景与问题
- **为什么要做**：现实世界中的多元时间序列（如金融、生态数据）存在复杂的序列间相关性，且这些相关性会随着时间尺度（如日、月、年）的不同而变化（例如，两个股票在长周期上正相关，在短周期上可能负相关）。现有模型对此关注不足。
- **之前方法的问题**：
    1.  许多使用图神经网络（GNN）的模型采用**固定的或单一的图结构**来描述序列间关系，无法捕捉这种随尺度变化的相关性。
    2.  一些方法考虑使用**动态图结构**，但忽略了图结构可能与**稳定的、有意义的时间周期**（如经济周期）密切相关这一事实。
- **核心矛盾**：现有深度学习模型难以**同时、准确地建模序列内依赖（intra-series）和跨尺度的序列间依赖（inter-series）**，尤其是后者在不同时间尺度上的多样性。

## 4. 核心贡献
1.  **关键观察与问题定义**：明确指出多元时间序列的序列间相关性与不同的时间尺度紧密相关。
2.  **提出MSGNet框架**：设计了新颖的`ScaleGraphBlock`，首次将序列间相关性建模与时间尺度（通过FFT识别）显式关联。
3.  **多尺度图卷积模块**：引入**自适应混合跳（adaptive Mixhop）图卷积层**，为每个时间尺度动态学习一个独立的邻接矩阵，以捕捉该尺度下特定的序列间依赖。
4.  **联合建模策略**：将用于序列内相关性建模的**多头自注意力机制**与上述多尺度图卷积模块结合，形成统一的框架。
5.  **实验与泛化验证**：在多个真实世界数据集上验证了模型的有效性和优越性，特别是通过COVID-19期间的航班数据（OOD样本）展示了模型强大的泛化能力。

## 5. 方法详解
- **整体框架**：如图2所示，MSGNet由多个相同的`ScaleGraphBlock`堆叠而成，并通过残差连接。每个`ScaleGraphBlock`包含四个核心步骤：尺度识别、多尺度图卷积、多头注意力、尺度聚合。
- **输入与输出**：
    - 输入：`X_{t-L:t} \in R^{N×L}`，表示N个变量在回看窗口L个时间点的观测值。
    - 输出：`\hat{X}_{t:t+T} \in R^{N×T}`，表示对N个变量未来T个时间步的预测。
- **关键模块详解**：
    1.  **输入嵌入与残差连接** (Eq.1, Eq.2)
        - 先对输入进行归一化，然后通过1D卷积、位置编码和可学习的时间戳编码将其嵌入到`d_model`维空间，得到`X_emb`。
        - 模型主体采用残差结构：`X^l = ScaleGraphBlock(X^{l-1}) + X^{l-1}`。
    2.  **尺度识别** (Eq.3, Eq.4) - **FFT模块**
        - 对嵌入后的序列进行**快速傅里叶变换(FFT)**，计算频率幅值并平均，得到频谱`F`。
        - 选取幅值最大的`k`个频率对应的周期`s_i = L / f_i`作为主要时间尺度。
        - 根据尺度`s_i`和对应的周期数`f_i`，将原始输入`X_in`通过零填充和重塑，得到`k`个尺度的3D张量`X_i ∈ R^{d_model × s_i × f_i}`。这是将长序列“折叠”成多个二维序列（周期×个数）。
    3.  **多尺度自适应图卷积** (Eq.5, Eq.6, Eq.7) - **图卷积模块**
        - 对于每个尺度张量`X_i`，先通过线性层投影回`N`个变量维度，得到`H_i ∈ R^{N × s_i × f_i}`。
        - **自适应图学习**：为每个尺度学习两个可训练参数矩阵`E1_i`, `E2_i ∈ R^{N×h}`，通过`A_i = SoftMax(ReLU(E1_i * E2_i^T))`生成该尺度的邻接矩阵`A_i ∈ R^{N×N}`。
        - **Mixhop图卷积**：在邻接矩阵`A_i`及其幂次`(A_i)^j`上对`H_i`进行图卷积，然后拼接结果，通过激活函数，得到融合了多跳邻居信息的输出`H_i^out`。最后再通过MLP映射回`d_model`维。
    4.  **多头注意力与尺度聚合** (Eq.8, Eq.9) - **注意力模块**
        - 对每个尺度的张量`\hat{X}_i`，在**时间尺度维度(s_i)** 上应用**多头自注意力(MHA)**，捕捉该尺度内的序列内时序依赖。
        - **尺度聚合**：将各尺度输出重塑回2D矩阵`\hat{X}_i^out ∈ R^{d_model × L}`。根据FFT计算的对应幅值`F_{f_i}`，通过SoftMax计算权重`\hat{a}_i`，对各尺度结果进行加权求和，得到最终聚合表示`\hat{X}_{out}`。这是一种“专家混合”(MoE)策略。
- **输出层** (Eq.10)：通过两个线性层分别沿变量维度(`W_s`)和时间维度(`W_t`)投影`\hat{X}_{out}`，得到最终预测`\hat{X}_{t:t+T}`。
- **训练方式**：使用均方误差(MSE)作为损失函数。
- **推理流程**：与前向传播流程一致，给定输入序列，通过上述步骤生成预测。
- **与已有方法的差异**：
    - 与传统使用固定图的GNN（如MTGnn）不同，MSGNet为每个有意义的周期学习独立的图结构。
    - 与TimesNet（也用FFT）不同，TimesNet将序列变换到二维空间是为了更好地进行卷积，而MSGNet是为了学习不同尺度下的图结构关系。
    - 核心创新在于首次将“时间尺度”作为学习序列间相关性的一个显式维度。
- **论文类型特化 (注意力类)**：
    - **注意力作用维度**：本文的多头注意力作用在**时间尺度维度**（即每个周期内部的时间步），而非传统的通道或空间维度。这可以看作是一种在频率分解后的子序列上应用的注意力。
    - **可插入网络**：`ScaleGraphBlock`是模块化的设计，可以堆叠（公式2），具有即插即用的潜力。
    - **计算量 vs 效果**：论文通过结合轻量的FFT和有效的图卷积、注意力机制，在多个基准上取得了SOTA效果，但未在提供的文本中给出具体的计算量（FLOPs）或参数量对比数据。

## 6. 实验与结果
- **使用的数据集**：共8个，包括：**Flight**（COVID-19期间航班数据，用于OOD测试）、**Weather**、**ETTh1, ETTh2, ETTm1, ETTm2**、**Exchange-Rate**、**Electricity**。
- **对比方法**：6个基线模型：**Informer**, **Autoformer** (Transformer类), **MTGnn** (图卷积类), **DLinear, NLinear** (线性模型), **TimesNet** (基于周期分解的SOTA)。
- **评价指标**：均方误差(**MSE**)。
- **主实验结果**：论文声称“MSGNet consistently outperforms existing deep learning models”，但提供的文本中**未给出具体的MSE数值表格**。因此无法列出关键数字。
- **消融实验**：论文提及在附录中有关于注意力模块有效性和尺度聚合策略等的消融实验，但**提供的PDF文本中未包含**。
- **泛化实验**：使用**Flight**数据集评估。该数据包含COVID-19冲击导致的分布外(OOD)样本。论文指出模型在此数据上表现出“strong generalization capabilities”，但具体性能数字**未在提供的文本中给出**。
- **速度/参数量/FLOPs**：**PDF文本中未提供**任何关于模型效率（如训练时间、推理速度、参数量、FLOPs）的具体信息。

## 7. 这篇论文真正有价值的地方
1.  **洞察与视角**：提出了“序列间相关性具有多尺度性”这一关键且直观的洞见，为多元时间序列建模提供了新的思考维度。
2.  **框架创新**：设计了优雅的`ScaleGraphBlock`，将**频率分析(FFT)、图结构学习(自适应GNN)、序列内注意力(MHA)** 三者有机结合，逻辑清晰，模块化强。特别是“为每个频率/周期学习一个图”的思路极具启发性。
3.  **方法设计**：将频率幅值作为聚合权重的“专家混合”策略简单有效；使用Mixhop图卷积来增强图表示能力。
4.  **研究示范**：展示了如何从具体问题（多尺度相关性）出发，设计一个端到端的深度学习解决方案，并从多个角度（方法、实验、可视化）进行论证，是很好的研究范例。

## 8. 局限与问题
1.  **计算复杂度**：为每个时间尺度学习一个完整的N×N邻接矩阵，并进行图卷积，当变量N很大时，计算和内存开销可能很高。论文**未讨论此问题**。
2.  **假设依赖**：模型效果依赖于数据中存在**强且稳定的周期性**。对于随机性强、无明显周期的数据（如某些金融高频数据），FFT可能无法提取有效尺度，模型性能可能下降。
3.  **实验深度**：提供的文本中缺乏关键的消融实验细节和具体的性能数字，使得对各模块贡献的评估不够直观。
4.  **数据集范围**：实验虽涵盖了多个数据集，但领域仍相对有限（能源、天气、金融），在更广泛领域（如医学信号、社交网络）的有效性有待验证。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：阅读**Abstract、Introduction**和**Conclusion**部分，重点关注图1和图2，可以快速理解其核心动机和框架。
- **如果复现**：重点精读**Methodology**部分，特别是公式(3)-(9)关于尺度识别、图学习和卷积的具体实现步骤。需参考其**官方代码库**（链接在摘要中）及附录中的超参数设置。
- **如果借鉴创新点**：
    - 可以借鉴“**为不同频率分量学习独立关系**”的思想，应用于其他需要处理多尺度依赖的时序任务（如检测、分类）。
    - 学习其**模块组合方式**（FFT+GNN+Attention）的设计思路。
    - 参考其利用**频率幅值进行动态加权聚合**的技巧。
- **如果写related work**：
    - 可放在**GNN用于时间序列预测**小节，作为使用可学习图结构的先进工作。
    - 可放在**时间序列多尺度分析或周期建模**小节。
    - 可放在**序列间相关性建模**小节。

## 10. 和其他论文的关系
基于主题“B_注意力算子模块”和论文中频繁引用的工作，可能相关的论文包括：
- `[[TimesNet]]`：同为使用FFT进行周期分解的SOTA工作，是本文的主要对比基线和灵感来源之一。
- `[[MTGnn]]`：使用图神经网络进行多元时间序列预测的代表工作，使用固定/可学习图结构，是本文的对比基线。
- `[[Informer]]`, `[[Autoformer]]`：基于Transformer的时序预测模型，是本文的对比基线。
- `[[DLinear]]`, `[[NLinear]]`：证明线性模型有效的颠覆性工作，是本文的对比基线。

## 11. 关键词
多元时间序列预测， 多尺度相关性， 图神经网络， 自适应图学习， 频率分析， 快速傅里叶变换(FFT)， 多头自注意力， 时间序列建模， 时空数据挖掘， 模块化网络

## 12. 可信度说明
本篇精读笔记主要基于**提供的PDF提取文本（前12页）**生成，该部分覆盖了论文的**标题、作者、摘要、引言、相关工作、问题定义、完整的方法论（Methodology）描述**以及实验设置的开头部分。
- **提取质量**：方法论部分（第4-5页）描述非常详细完整，是生成笔记的主要依据。
- **信息缺失**：由于文本截止于第12页（实验设置部分），因此**缺乏具体的实验结果表格、详细的消融实验分析、效率对比数据以及结论部分**。笔记中关于实验结果和局限性的部分是基于文本中已有描述的合理推断和标注，相关具体数字和细节被明确标记为“未提供”。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/ScaleGraphBlock.txt` (14/14 页; 原 AI 主体 12/14 + 全文补读 13-14); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-14; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-14。
- **提取情况**: 缺失页 2 页, 其中 2 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 2023. Accurate medium-range global weather forecasting
- p.13: Long-term Forecasting with TiDE: Time-series Dense En-
- p.13: Convolutional neural networks on graphs with fast localized
- p.13: 2023. A Time Series is Worth 64 Words: Long-term Fore-
- p.13: 2020. N-BEATS: Neural basis expansion analysis for inter-
- p.13: 2020. DeepAR: Probabilistic forecasting with autoregres-
- p.13: Decomposition transformers with auto-correlation for long-
- p.14: 2022. Fedformer: Frequency enhanced decomposed trans-

### 缺失页关键摘录

- p.13: Accurate medium-range global weather forecasting with 3D neural networks.
- p.14: Fedformer: Frequency enhanced decomposed trans- former for long-term series forecasting.
<!-- AI_READING_NOTE_END -->
