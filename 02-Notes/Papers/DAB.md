---
title: "DEFORMTIME: Capturing Variable Dependencies"
authors:
  - "Yuxuan Shu"
year: 2024
venue: "arXiv"
doi: 
pdf: [[DAB.pdf]]
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
extract_cache: .paper-cache/extracts/DAB.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/29 pages"
---
# DEFORMTIME: Capturing Variable Dependencies

## 基本信息
- **PDF**: [[DAB.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | DEFORMTIME: Capturing Variable Dependencies |
| **作者** | Yuxuan Shu |
| **发表时间** | 2024 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> In multivariate time series (MTS) forecasting, existing state-of-the-art deep learningapproachestendtofocusonautoregressiveformulationsandoverlookthe informationwithinexogenousindicators. Toaddressthislimitation,wepresent DEFORMTIME,1aneuralnetworkarchitecturethatattemptstocapturecorrelated temporalpatternsfromtheinputspace,andhence,improveforecastingaccuracy. Itdeploystwocoreoperationsperformedbydeformableattentionblocks(DABs): learningdependenciesacrossvariablesfromdifferenttimesteps(variableDAB), andpreservingtemporaldependenciesindatafromprevioustimesteps(temporal DAB).Inputdatatransformationisexplicitlydesignedtoenhancelearningfromthe deformedseriesofinformationwhilepassingthroughaDAB.Weconductextensive experimentson6MTSdatasets,usingpreviouslyestablishedbenchmarksaswell aschallenginginfectiousdiseasemodellingtaskswithmoreexogenousvariables. TheresultsdemonstratethatDEFORMTIMEimprovesaccuracyagainstprevious competitivemethodsacrossthevastmajorityofMTSforecastingtasks,reducing them

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：在多变量时间序列预测任务中，许多先进的深度学习模型倾向于采用自回归公式，**忽视了外生变量（exogenous indicators）** 中蕴含的丰富信息。同时，部分模型未能有效设计以纳入**变量间的依赖关系**，而这是传统预测器的关键特性。
- **之前方法的问题**：
    1. 基于RNN的模型（如[19,25]）在捕捉跨变量依赖方面能力有限。
    2. 一些尝试建模变量间依赖的模型（如LightTS, Crossformer）后来被**未建立变量间依赖**的更新模型（如DLinear, PatchTST）超越。后者的论点是，不建模变量间依赖可以利用更长的回溯窗口而不显著增加模型复杂度。
    3. 现有文献中存在一个普遍问题，即用于评估的**基准任务可能不恰当**，这使得对一些结论的可靠性产生疑问。
- **作者想解决的核心矛盾**：如何在不过度增加模型复杂度的前提下，**有效捕捉变量间以及时间维度上的动态依赖关系**，并充分利用外生变量信息，从而提升预测性能，尤其是在包含大量外生变量的复杂任务（如传染病预测）上。
## 关键贡献

1.  **提出了 DEFORM TIME 模型**：一个新颖的多变量时间序列预测模型，其核心是部署了两个可变形注意力块。
2.  **设计了两个核心可变形注意力块**：
    - **变量可变形注意力块**：用于捕获**跨变量在不同时间步的依赖关系**。
    - **时间可变形注意力块**：用于**保持和捕捉同一变量在不同时间周期的依赖关系**。
3.  **提出了显式的输入数据变换**：设计了**邻域感知输入嵌入**和**数据分段/重组操作**，以增强模型从经过形变的序列信息中学习的能力。
4.  **进行了全面的实验评估**：在**3个标准基准数据集**和**3个具有挑战性的传染病建模任务**（包含大量外生变量）上进行了评估，覆盖多个预测步长。
5.  **取得了显著的性能提升**：实验结果表明，DEFORM TIME 在绝大多数任务上优于现有的竞争方法，**平均将平均绝对误差降低了10%**，且在更长的预测步长上性能增益保持稳定。
## 方法

**整体框架**：DEFORM TIME 采用编码器-解码器结构。编码器包含两个并行的分支，分别嵌入**变量可变形注意力块**和**时间可变形注意力块**，用于捕捉跨变量和跨时间的依赖关系。解码器是一个两层的GRU网络。

**输入输出**：
- **输入**：在时间步 `t`，输入包括一个外生变量序列 `Q_t` (维度 `L x C`) 和目标变量的历史值 `y_{t-δ}` (维度 `L`)，拼接后得到 `Z` (维度 `L x (C+1)`)。其中 `L` 是回溯窗口长度，`C` 是外生变量数，`δ` 是观测延迟。
- **输出**：预测未来 `H` 步的目标变量值 `ŷ` (维度 `H`)。

**关键模块与连接**：
1.  **邻域感知输入嵌入**：
    - **操作**：首先根据变量与目标变量的线性相关性对输入变量 `Z` 重新排序。然后，将排序后的变量分组为 `G` 个邻域，每个组独立地通过一个全连接层嵌入到 `d/G` 维，最后拼接所有组的嵌入，形成 `L x d` 的嵌入 `E`。再加入正弦位置编码并进行层归一化，得到最终的输入嵌入 `Z_e`。
    - **目的**：通过相关性排序和分组嵌入，将相关的变量放在一起，为后续CNN提取局部邻域信息做准备。
2.  **变量可变形注意力块**：
    - **操作**：将 `Z_e` 沿时间维度分割成重叠的 patch `Z_p`。通过一个小型CNN (`θ_off`) 为每个 patch 生成一个二维偏移量 `Δp`，用于从原始 patch `Z_p` 中采样（通过双线性插值）得到一个**形变后的 patch `Z_d`**。然后，对 `Z_d` 进行标准的单头自注意力计算（Query 来自原始 patch `Z_p`，Key 和 Value 来自形变 patch `Z_d`），并加上一个相对位置偏置 `P_v`。最后，将所有 patch 的注意力输出拼接并通过一个全连接层，输出 `Z_v`。
    - **作用**：允许网络自适应地关注不同变量在不同时间步的信息，打破了固定网格的限制。
3.  **时间可变形注意力块**：
    - **操作**：首先将 `Z_e` 转换为适合处理多种时间粒度的形状。然后，对每个变量（列）的序列进行分组，每组共享一个时间偏移量 `Δp(g)`（通过1D CNN生成）。利用该偏移量对时间序列进行**线性插值**，得到形变后的时间序列。最后，在每个分组内进行多头注意力计算（Query、Key、Value 都经过形变处理），输出 `Z_t`。
    - **作用**：捕捉同一变量在不同时间周期的动态模式，支持多粒度时间依赖建模。
4.  **编码器与解码器**：
    - **编码器**：由两个堆叠的编码器层组成。每一层包含上述的**V-DAB分支**和**T-DAB分支**（两个分支并行处理输入 `Z_e`），每个分支都带有残差连接、层归一化和随机深度。两个分支的输出拼接后通过一个全连接层。
    - **解码器**：编码器的最终输出被送入一个两层的GRU解码器。GRU的输出再通过一个两层MLP和全连接层，投影到预测维度 `H`。

**数学公式或机制的直观解释**：
- 可变形注意力的核心是**偏移量生成**。公式 `Δp = α · tanh(θ_off(Q))` 中，`θ_off` 是一个CNN，`Q` 是Query，`α` 是一个可学习的标量。这个机制使得模型可以根据当前内容（Query）动态地决定“去哪里看”（偏移量），从而关注序列中更相关的位置，而不是固定的邻域。
- 与标准注意力的对比：标准注意力在固定的、规则的序列网格上计算。DEFORM TIME 的注意力则是在一个**由模型根据输入内容动态生成的不规则网格**上计算，提供了更大的灵活性。

**训练方式**：论文未在提供的文本中详细说明损失函数和优化器，但可以推断是使用标准的时间序列预测损失（如MAE）进行端到端训练。

**推理流程**：输入序列 `Z` 经过上述所有模块的变换，最终由解码器输出预测值 `ŷ`。

**和已有方法的差异**：
- **与Crossformer的区别**：Crossformer也使用了基于patch和路由机制来捕捉跨变量依赖，但它是基于固定的patch划分和学习的路由器。DEFORM TIME 则引入了**连续可学习的偏移量**，通过形变直接调整采样位置，机制更灵活。
- **与PatchTST/iTransformer的区别**：这些模型是单变量模型或未显式建模变量间依赖。DEFORM TIME 通过 V-DAB **显式地建模变量间依赖**。
- **与LightTS的区别**：LightTS使用MLP分别建模时间和变量依赖，而DEFORM TIME使用**基于注意力的形变模块**，具有更强的序列建模和上下文捕捉能力。
## 实验

- **使用的数据集**：
    - **3个标准基准**：ETTh1、ETTh2、Weather。
    - **3个疾病预测任务**：ILI-ENG（英格兰流感样病例率）、ILI-US2和ILI-US9（美国HHS区域2和9的ILI率）。这些任务包含**大量外生变量**（如网络搜索频率）。
- **对比方法**：6个竞争模型：LightTS, DLinear, Crossformer, PatchTST, iTransformer, TimeMixer，以及一个朴素持续性模型。
- **评价指标**：**平均绝对误差** 和 **对称平均绝对百分比误差**。
- **主实验结果**（关键数字摘自Table 1）：
    - 在绝大多数任务和预测步长上，**DEFORM TIME 取得了最佳（bold）或次佳（underline）的MAE**。
    - **平均性能提升**：相比最强竞争模型，MAE平均降低了10%。具体地，在标准基准上平均降低7.4%，在疾病预测任务上平均降低12.6%。
    - **例如**：在ETTh1（H=96）上，MAE为0.1941，优于PatchTST的0.2017；在ILI-ENG（H=7）上，MAE为1.6417，优于Crossformer的1.8698。
    - **长程预测**：性能优势在较长的预测步长（如H=720, 28）上保持稳定。
- **消融实验**：文本中提到“we provide an ablation study”，但在提供的前12页文本中未找到具体的消融实验结果细节。
- **效率信息**：文本中提到“we also provide ... computational complexity / efficiency analysis”，但在提供的部分未找到具体的参数量、FLOPs或速度对比数据。
## 局限

1.  **计算复杂度**：可变形注意力模块需要额外的CNN来生成偏移量，并进行插值操作，这可能会**增加模型的计算开销和参数量**，尽管论文声称在长序列下复杂度可控。提供的文本未给出详细的效率对比。
2.  **对输入变换的依赖**：模型性能可能对**邻域感知输入嵌入中的变量排序和分组策略**敏感。这增加了预处理的复杂度和潜在的调参负担。
3.  **数据集规模与多样性**：虽然引入了新的疾病数据集，但论文评估的**标准基准数据集数量（3个）相对有限**，可能不足以全面验证模型的泛化能力。
4.  **可解释性**：虽然偏移量提供了模型关注位置的某种指示，但可变形注意力内部机制的**可解释性**如何，文本中未探讨。
5.  **复现风险**：方法涉及多个自定义模块（NAE, DAB等）和训练细节（随机深度、分组超参数G的设置），完整复现需要仔细参照代码和附录（附录内容在提供的文本中未包含）。
## 个人评论

1.  **思想启发**：将计算机视觉中成功的**可变形卷积/注意力**思想创造性地迁移到时间序列预测领域，解决了传统注意力在固定网格上计算的限制，为动态序列建模提供了新思路。
2.  **模块设计**：提出的**V-DAB**和**T-DAB**两个模块，分别针对“变量间”和“时间轴上”两个关键的依赖维度进行建模，设计清晰且有效。特别是通过偏移量进行形变插值的机制，直观且强大。
3.  **输入处理的强调**：论文不仅设计了新的注意力模块，还特别设计了**邻域感知输入嵌入**等前置操作，体现了“数据表示与模型模块同等重要”的工程思想。这对改进其他模型有启发。
4.  **实验设计的启示**：作者不仅在标准基准上测试，还特别构建了**更具挑战性、外生变量更丰富的疾病预测任务**，并指出模型在这些任务上表现更好。这提醒研究者，任务选择对评估模型的真实能力至关重要。

### 使用建议

- **如果快速了解**：只读**摘要**和**引言**，以及**结果部分的Table 1**，可以迅速把握论文的核心动机、方法和主要成果。
- **如果复现**：重点看**第3节（方法详解）**，结合论文的**图1**理解模块连接。必须查看**附录**（如A.2, A.5, C.1, C）获取具体的数据集处理、评估设置、超参数和实现细节。源代码链接已提供。
- **如果借鉴创新点**：应该学习其**可变形注意力块（DAB）的设计思想**，特别是如何通过生成偏移量来自适应地调整感受野。可以尝试将V-DAB或T-DAB模块迁移到其他需要建模序列动态依赖的任务中。
- **如果写related work**：可将本文放在以下类别中：
    - “基于Transformer的时间序列预测方法”（与PatchTST, Crossformer等对比）。
    - “显式建模变量间依赖的MTS模型”（与Crossformer, LightTS对比）。
    - “可变形/动态注意力机制”（与CV中的Deformable DETR等对比）。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**多变量时间序列预测**方向，特别是**深度学习在时间序列预测中的应用**。它针对现有模型在捕捉变量间依赖和利用外生变量方面的不足，提出了一种新的神经网络架构。论文适合放在 **“注意力算子模块”** 这个主题下，因为其核心创新点是提出了**可变形注意力块**作为关键模块，用于自适应地捕捉变量和时间维度上的动态依赖关系。

## 2. 一句话总结
本文提出了 **DEFORM TIME**，一种利用**可变形注意力块**对输入序列进行自适应形变和注意力计算的神经网络架构，旨在更好地捕捉多变量时间序列中变量间及时间维度上的动态依赖关系，从而显著提升预测精度。

## 3. 背景与问题
- **为什么要做**：在多变量时间序列预测任务中，许多先进的深度学习模型倾向于采用自回归公式，**忽视了外生变量（exogenous indicators）** 中蕴含的丰富信息。同时，部分模型未能有效设计以纳入**变量间的依赖关系**，而这是传统预测器的关键特性。
- **之前方法的问题**：
    1. 基于RNN的模型（如[19,25]）在捕捉跨变量依赖方面能力有限。
    2. 一些尝试建模变量间依赖的模型（如LightTS, Crossformer）后来被**未建立变量间依赖**的更新模型（如DLinear, PatchTST）超越。后者的论点是，不建模变量间依赖可以利用更长的回溯窗口而不显著增加模型复杂度。
    3. 现有文献中存在一个普遍问题，即用于评估的**基准任务可能不恰当**，这使得对一些结论的可靠性产生疑问。
- **作者想解决的核心矛盾**：如何在不过度增加模型复杂度的前提下，**有效捕捉变量间以及时间维度上的动态依赖关系**，并充分利用外生变量信息，从而提升预测性能，尤其是在包含大量外生变量的复杂任务（如传染病预测）上。

## 4. 核心贡献
1.  **提出了 DEFORM TIME 模型**：一个新颖的多变量时间序列预测模型，其核心是部署了两个可变形注意力块。
2.  **设计了两个核心可变形注意力块**：
    - **变量可变形注意力块**：用于捕获**跨变量在不同时间步的依赖关系**。
    - **时间可变形注意力块**：用于**保持和捕捉同一变量在不同时间周期的依赖关系**。
3.  **提出了显式的输入数据变换**：设计了**邻域感知输入嵌入**和**数据分段/重组操作**，以增强模型从经过形变的序列信息中学习的能力。
4.  **进行了全面的实验评估**：在**3个标准基准数据集**和**3个具有挑战性的传染病建模任务**（包含大量外生变量）上进行了评估，覆盖多个预测步长。
5.  **取得了显著的性能提升**：实验结果表明，DEFORM TIME 在绝大多数任务上优于现有的竞争方法，**平均将平均绝对误差降低了10%**，且在更长的预测步长上性能增益保持稳定。

## 5. 方法详解
**整体框架**：DEFORM TIME 采用编码器-解码器结构。编码器包含两个并行的分支，分别嵌入**变量可变形注意力块**和**时间可变形注意力块**，用于捕捉跨变量和跨时间的依赖关系。解码器是一个两层的GRU网络。

**输入输出**：
- **输入**：在时间步 `t`，输入包括一个外生变量序列 `Q_t` (维度 `L x C`) 和目标变量的历史值 `y_{t-δ}` (维度 `L`)，拼接后得到 `Z` (维度 `L x (C+1)`)。其中 `L` 是回溯窗口长度，`C` 是外生变量数，`δ` 是观测延迟。
- **输出**：预测未来 `H` 步的目标变量值 `ŷ` (维度 `H`)。

**关键模块与连接**：
1.  **邻域感知输入嵌入**：
    - **操作**：首先根据变量与目标变量的线性相关性对输入变量 `Z` 重新排序。然后，将排序后的变量分组为 `G` 个邻域，每个组独立地通过一个全连接层嵌入到 `d/G` 维，最后拼接所有组的嵌入，形成 `L x d` 的嵌入 `E`。再加入正弦位置编码并进行层归一化，得到最终的输入嵌入 `Z_e`。
    - **目的**：通过相关性排序和分组嵌入，将相关的变量放在一起，为后续CNN提取局部邻域信息做准备。
2.  **变量可变形注意力块**：
    - **操作**：将 `Z_e` 沿时间维度分割成重叠的 patch `Z_p`。通过一个小型CNN (`θ_off`) 为每个 patch 生成一个二维偏移量 `Δp`，用于从原始 patch `Z_p` 中采样（通过双线性插值）得到一个**形变后的 patch `Z_d`**。然后，对 `Z_d` 进行标准的单头自注意力计算（Query 来自原始 patch `Z_p`，Key 和 Value 来自形变 patch `Z_d`），并加上一个相对位置偏置 `P_v`。最后，将所有 patch 的注意力输出拼接并通过一个全连接层，输出 `Z_v`。
    - **作用**：允许网络自适应地关注不同变量在不同时间步的信息，打破了固定网格的限制。
3.  **时间可变形注意力块**：
    - **操作**：首先将 `Z_e` 转换为适合处理多种时间粒度的形状。然后，对每个变量（列）的序列进行分组，每组共享一个时间偏移量 `Δp(g)`（通过1D CNN生成）。利用该偏移量对时间序列进行**线性插值**，得到形变后的时间序列。最后，在每个分组内进行多头注意力计算（Query、Key、Value 都经过形变处理），输出 `Z_t`。
    - **作用**：捕捉同一变量在不同时间周期的动态模式，支持多粒度时间依赖建模。
4.  **编码器与解码器**：
    - **编码器**：由两个堆叠的编码器层组成。每一层包含上述的**V-DAB分支**和**T-DAB分支**（两个分支并行处理输入 `Z_e`），每个分支都带有残差连接、层归一化和随机深度。两个分支的输出拼接后通过一个全连接层。
    - **解码器**：编码器的最终输出被送入一个两层的GRU解码器。GRU的输出再通过一个两层MLP和全连接层，投影到预测维度 `H`。

**数学公式或机制的直观解释**：
- 可变形注意力的核心是**偏移量生成**。公式 `Δp = α · tanh(θ_off(Q))` 中，`θ_off` 是一个CNN，`Q` 是Query，`α` 是一个可学习的标量。这个机制使得模型可以根据当前内容（Query）动态地决定“去哪里看”（偏移量），从而关注序列中更相关的位置，而不是固定的邻域。
- 与标准注意力的对比：标准注意力在固定的、规则的序列网格上计算。DEFORM TIME 的注意力则是在一个**由模型根据输入内容动态生成的不规则网格**上计算，提供了更大的灵活性。

**训练方式**：论文未在提供的文本中详细说明损失函数和优化器，但可以推断是使用标准的时间序列预测损失（如MAE）进行端到端训练。

**推理流程**：输入序列 `Z` 经过上述所有模块的变换，最终由解码器输出预测值 `ŷ`。

**和已有方法的差异**：
- **与Crossformer的区别**：Crossformer也使用了基于patch和路由机制来捕捉跨变量依赖，但它是基于固定的patch划分和学习的路由器。DEFORM TIME 则引入了**连续可学习的偏移量**，通过形变直接调整采样位置，机制更灵活。
- **与PatchTST/iTransformer的区别**：这些模型是单变量模型或未显式建模变量间依赖。DEFORM TIME 通过 V-DAB **显式地建模变量间依赖**。
- **与LightTS的区别**：LightTS使用MLP分别建模时间和变量依赖，而DEFORM TIME使用**基于注意力的形变模块**，具有更强的序列建模和上下文捕捉能力。

## 6. 实验与结果
- **使用的数据集**：
    - **3个标准基准**：ETTh1、ETTh2、Weather。
    - **3个疾病预测任务**：ILI-ENG（英格兰流感样病例率）、ILI-US2和ILI-US9（美国HHS区域2和9的ILI率）。这些任务包含**大量外生变量**（如网络搜索频率）。
- **对比方法**：6个竞争模型：LightTS, DLinear, Crossformer, PatchTST, iTransformer, TimeMixer，以及一个朴素持续性模型。
- **评价指标**：**平均绝对误差** 和 **对称平均绝对百分比误差**。
- **主实验结果**（关键数字摘自Table 1）：
    - 在绝大多数任务和预测步长上，**DEFORM TIME 取得了最佳（bold）或次佳（underline）的MAE**。
    - **平均性能提升**：相比最强竞争模型，MAE平均降低了10%。具体地，在标准基准上平均降低7.4%，在疾病预测任务上平均降低12.6%。
    - **例如**：在ETTh1（H=96）上，MAE为0.1941，优于PatchTST的0.2017；在ILI-ENG（H=7）上，MAE为1.6417，优于Crossformer的1.8698。
    - **长程预测**：性能优势在较长的预测步长（如H=720, 28）上保持稳定。
- **消融实验**：文本中提到“we provide an ablation study”，但在提供的前12页文本中未找到具体的消融实验结果细节。
- **效率信息**：文本中提到“we also provide ... computational complexity / efficiency analysis”，但在提供的部分未找到具体的参数量、FLOPs或速度对比数据。

## 7. 这篇论文真正有价值的地方
1.  **思想启发**：将计算机视觉中成功的**可变形卷积/注意力**思想创造性地迁移到时间序列预测领域，解决了传统注意力在固定网格上计算的限制，为动态序列建模提供了新思路。
2.  **模块设计**：提出的**V-DAB**和**T-DAB**两个模块，分别针对“变量间”和“时间轴上”两个关键的依赖维度进行建模，设计清晰且有效。特别是通过偏移量进行形变插值的机制，直观且强大。
3.  **输入处理的强调**：论文不仅设计了新的注意力模块，还特别设计了**邻域感知输入嵌入**等前置操作，体现了“数据表示与模型模块同等重要”的工程思想。这对改进其他模型有启发。
4.  **实验设计的启示**：作者不仅在标准基准上测试，还特别构建了**更具挑战性、外生变量更丰富的疾病预测任务**，并指出模型在这些任务上表现更好。这提醒研究者，任务选择对评估模型的真实能力至关重要。

## 8. 局限与问题
1.  **计算复杂度**：可变形注意力模块需要额外的CNN来生成偏移量，并进行插值操作，这可能会**增加模型的计算开销和参数量**，尽管论文声称在长序列下复杂度可控。提供的文本未给出详细的效率对比。
2.  **对输入变换的依赖**：模型性能可能对**邻域感知输入嵌入中的变量排序和分组策略**敏感。这增加了预处理的复杂度和潜在的调参负担。
3.  **数据集规模与多样性**：虽然引入了新的疾病数据集，但论文评估的**标准基准数据集数量（3个）相对有限**，可能不足以全面验证模型的泛化能力。
4.  **可解释性**：虽然偏移量提供了模型关注位置的某种指示，但可变形注意力内部机制的**可解释性**如何，文本中未探讨。
5.  **复现风险**：方法涉及多个自定义模块（NAE, DAB等）和训练细节（随机深度、分组超参数G的设置），完整复现需要仔细参照代码和附录（附录内容在提供的文本中未包含）。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读**摘要**和**引言**，以及**结果部分的Table 1**，可以迅速把握论文的核心动机、方法和主要成果。
- **如果复现**：重点看**第3节（方法详解）**，结合论文的**图1**理解模块连接。必须查看**附录**（如A.2, A.5, C.1, C）获取具体的数据集处理、评估设置、超参数和实现细节。源代码链接已提供。
- **如果借鉴创新点**：应该学习其**可变形注意力块（DAB）的设计思想**，特别是如何通过生成偏移量来自适应地调整感受野。可以尝试将V-DAB或T-DAB模块迁移到其他需要建模序列动态依赖的任务中。
- **如果写related work**：可将本文放在以下类别中：
    - “基于Transformer的时间序列预测方法”（与PatchTST, Crossformer等对比）。
    - “显式建模变量间依赖的MTS模型”（与Crossformer, LightTS对比）。
    - “可变形/动态注意力机制”（与CV中的Deformable DETR等对比）。

## 10. 和其他论文的关系
- **直接对比/竞争的论文**：PatchTST [[PatchTST]], iTransformer [[iTransformer]], Crossformer [[Crossformer]], DLinear [[DLinear]], TimeMixer [[TimeMixer]], LightTS [[LightTS]]。
- **方法启发来源**：Deformable DETR [[Deformable DETR]]（计算机视觉中的可变形注意力思想），以及标准的Transformer [[Transformer]]。
- **属于同一研究脉络的论文**：任何专注于**多变量时间序列预测**或**改进Transformer在时序任务中应用**的论文，如Autoformer [[Autoformer]], FEDformer [[FEDformer]]等。

## 11. 关键词
多变量时间序列预测，可变形注意力，变量间依赖，时间序列依赖，注意力算子模块，输入变换，传染病预测，基准评估，编码器-解码器网络，自适应采样。

## 12. 可信度说明
本精读笔记主要基于用户提供的**PDF提取文本的前12页**生成，涵盖了从摘要、引言、问题定义、方法详解到实验结果的部分内容。提取的文本内容清晰，逻辑连贯，包含了论文的核心框架、关键模块描述（包括数学公式）和主要实验结果表格。然而，由于只提供了前12页，**消融实验的具体结果、详细的效率分析（参数量、FLOPs）、以及附录中的补充细节（如A.5讨论基准问题、C.1的变量排序细节）未能涵盖**。因此，对于这些缺失部分的信息，笔记中已明确标注“PDF文本中未明确说明”或未找到。总体而言，基于提供的文本，能够对论文的核心思想和方法做出准确、完整的解读。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/DAB.txt` (29/29 页; 原 AI 主体 12/29 + 全文补读 13-29); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-29; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-29。
- **提取情况**: 缺失页 17 页, 其中 17 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Supplementary Materials
- p.13: A Data sets for time series forecasting
- p.13: This section offers a detailed description of the data sets used in our experiments to assess the
- p.13: experiments to match the setup in related methods that we compare to). The temporal resolution
- p.13: England (in the United Kingdom) and two US HHS Regions, specifically Region 2 (states of New
- p.14: It should be noted that for RCGP, Monday determines the start of a week, while for CDC this is
- p.14: 2019. However, we note that not all search queries are used as exogenous variables in our forecasting
- p.14: Given that for the US, we can only obtain data at the state level (as opposed to regional), we use a
- p.15: Days020406080ILI rate (per 100K people)Test
- p.15: Train
- p.15: ValidationFigure A1: An example of how the training, validation, and test sets are constructed when the test influenza
- p.15: In this step, we compute the linear correlation between the remaining search queries and the target

### 缺失页关键摘录

- p.14: Training, validation, and test sets. We assess the accuracy of forecasters across the last 4influenza
- p.15: these time points are determined, they become the 30th point in a 60-day validation period. Figure A1
- p.15: A.5 Criticism of data sets used to benchmark forecasting methods
- p.16: forecasting. It captures a negligible portion of meteorological data and, as a result, derived forecasting
- p.16: Hence, using this data set for training and evaluating a forecasting model may, unfortunately, result
- p.16: hourly sampled data set has better accuracy compared to the quarter-hourly sampled data set even at
- p.16: generally provide good accuracy at approximately a 2weeks ahead forecasting horizon [ 31,33].
- p.16: that, in the aforementioned ILI rate benchmark, there were forecasting horizons of 24or60weeks
- p.16: ahead (i.e. even more than a year!). Of course, the accuracy of the forecasting models under these
- p.16: England or the US. The evaluation process is rigorous, i.e. across 4consecutive influenza seasons as
- p.17: each variable, leading to a sub-optimal performance in our empirical evaluation.
- p.18: Table D1: ILI rate forecasting accuracy results in England (ILI-ENG) using web search frequency time series as
<!-- AI_READING_NOTE_END -->
