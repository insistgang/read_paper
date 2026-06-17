---
title: "MOGO: Residual Quantized Hierarchical Causal Transformer for Real-Time and"
authors:
  - "DongjieFu2"
  - "TengjiaoSun1"
  - "PengchengFang1"
  - "XiaohaoCai1 HansungKim1"
  - "UniversityofSouthampton"
  - "MogoAI"
year: 2023
venue: Intelligence(www.aaai.org).Allrightsreserved. autoregressively generates multi-layer motion tokens in
doi: 
pdf: [[MOGO 3D人体运动生成 MOGO Motion.pdf]]
primary_topic: D_3D_点云_分类_分割_配准
topics:
  - "D_3D_点云_分类_分割_配准"
status: ai-read
reading_stage: ai-complete
confidence: high
source_basis: pdf-text
date_added: 2026-06-03
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/MOGO 3D人体运动生成 MOGO Motion.txt
---

# MOGO: Residual Quantized Hierarchical Causal Transformer for Real-Time and

## 基本信息
- **PDF**: [[MOGO 3D人体运动生成 MOGO Motion.pdf]]
- **primary_topic**: `D_3D_点云_分类_分割_配准`
- **topics**: `D_3D_点云_分类_分割_配准`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | MOGO: Residual Quantized Hierarchical Causal Transformer for Real-Time and |
| **作者** | DongjieFu2; TengjiaoSun1; PengchengFang1; XiaohaoCai1 HansungKim1; UniversityofSouthampton; MogoAI |
| **发表时间** | 2023 |
| **刊物/会议** | Intelligence(www.aaai.org).Allrightsreserved. autoregressively generates multi-layer motion tokens in |
| **DOI** | 未明确 |

## 摘要

> model(LLM)-basedtechniquestogeneratehigh-quality3D Recentadvancesintransformer-basedtext-to-motiongener- humanmotionfromtextdescriptions,typicallyusingvector- ation have significantly improved motion quality. However, quantized variational autoencoders (VQ-VAE) and autore- achievingbothreal-timeperformanceandlong-horizonscal- gressive decoding strategies (Guo et al. 2024; Zhang et al. abilityremainsanopenchallenge.Inthispaper,wepresent MOGO(MotionGenerationwithOne-pass),anovelautore- 2023a; Pinyoanuntapong et al. 2024; Zhong et al. 2023). gressiveframeworkforefficientandscalable3Dhumanmo- Meanwhile, diffusion-based approaches (Sun et al. 2025; tion generation. MOGO consists of two key components. Wangetal.2025)havealsodemonstratedstronggeneration First,weintroduceMoSA-VQ,amotionscale-adaptiveresid- performance,particularlyintermsofmotionfidelityanddi- ualvectorquantizationmodulethathierarchicallydiscretizes versity(Tevetetal.2022). motionsequencesthroughlearnablescalingparameters,en- D

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：文本驱动3D人体运动生成在游戏、AR/VR和机器人等领域应用前景广阔。尽管基于大语言模型（LLM）和扩散模型的方法在生成质量上取得进展，但它们分别面临**推理延迟高**（扩散模型依赖迭代求精）和**计算与内存开销大**（LLM模型参数量大、上下文长）的问题，难以满足实时交互应用的需求。
- **之前方法有什么问题**：
    - **扩散模型**：需要多步迭代去噪，推理速度慢，阻碍了实时应用。
    - **LLM-based模型（如T2M-GPT, MoMask）**：虽然可以自回归生成，但通常参数量巨大，对长序列的依赖导致高计算成本。此外，一些方法（如基于掩码的双向模型）在生成可扩展输出和泛化到分布外数据方面存在困难。
- **作者想解决的核心矛盾**：在保证**高运动质量（保真度、多样性）**的同时，实现**极低的推理延迟**和**灵活的时域可扩展性（无限长度生成）**。
## 关键贡献

1.  **提出了MoSA-VQ（运动尺度自适应残差向量量化）模块**：通过可学习的缩放和偏置参数动态调整残差幅度，并引入**跨级去相关损失**强制量化层间的统计正交性，从而获得更紧凑、层次解耦的离散表示。
2.  **设计了RQHC-Transformer（残差量化分层因果Transformer）**：一个与MoSA-VQ量化层次严格对齐的自回归解码器。每个Transformer块对应一个量化层级，实现从粗到细的层次化生成，并支持**单次前向传播**完成解码。
3.  **实现了无缝的无限长度运动生成**：利用框架的自回归特性，支持从任意时间点开始，通过替换文本提示词进行灵活的运动续写，生成任意长度且结构一致、保真度高的运动。
4.  **引入了文本条件对齐（TCA）策略**：利用大语言模型进行**风格标准化**和**指令分解**，将复杂或抽象的用户指令分解为原子动作步骤，显著提升模型对分布内外文本提示的泛化能力和生成精度。
## 方法

- **整体框架**：如图1所示，MOGO由四个核心组件构成：1）**MoSA-VQ编码器**，将连续运动序列离散化为多层次潜在码；2）**RQHC-Transformer解码器**，自回归地生成这些多层次码；3）**无限长度生成机制**；4）**TCA文本增强模块**。
- **输入输出**：
    - **输入**：自然语言文本描述。
    - **输出**：与文本描述匹配的3D人体运动序列（关节位置/旋转序列）。
- **关键模块**：
    1.  **MoSA-VQ**：
        - **机制**：基于残差向量量化（RVQ）。对于每个量化层级 *l*，输入残差 *rₗ* 先通过一个**可学习的仿射变换**（缩放矩阵 *Wₗ* 和偏置 *bₗ*）进行调制，然后进行最近邻量化。解码时执行逆变换。
        - **数学解释**：公式 (1) `qₗ = Q(Wₗrₗ + bₗ)` 和 `ϕₗ = (Wₗ)⁻¹(qₗ - bₗ)`。这允许每一级自适应地分配其表示容量。
        - **训练损失**：由四部分构成（公式3）：运动重建损失（L1）、码本承诺损失、**调制参数正则化损失**、以及创新的**跨级去相关损失**（Lₐₑcₒᵣ）。后者最小化量化向量 *ϕₗ* 与下一级残差 *rₗ₊₁* 的协方差，强制信息解耦。
    2.  **RQHC-Transformer**：
        - **结构**：一个因果Transformer，其“堆栈”结构与MoSA-VQ的量化层级对齐。生成第 *l* 层的token序列时，输入序列 *sₗ* 包含文本嵌入 *p*、当前层嵌入 *q_emb* 以及**聚合了所有更粗层级嵌入**的上下文 *t¹:ₙₗ*（公式4）。
        - **位置编码**：采用**相对位置编码**（公式6），以更好地处理变长序列和捕捉长程依赖。
        - **生成过程**：自回归地生成多层级token。训练目标是所有量化层级上的交叉熵损失之和（公式8）。
    3.  **无限长度生成**：在第 *n* 步，模型可以接收新的文本提示 *pₙₑw*，并基于之前生成的token序列 *t¹:ₙ₋₁ₗ* 继续自回归生成（公式9）。新提示立即生效，无需重新生成先前的运动。
    4.  **TCA**：推理时策略。给定原始提示 *cᵣₐw*，先用大语言模型 *T* 进行风格标准化得到 *cₙₒᵣₘ*，再通过思维链（Chain-of-Thought）提示将其分解为一系列原子子指令 *[c⁽¹⁾, ..., c⁽ᴷ⁾]*（公式10），供运动生成模型使用。
- **模块连接**：文本首先可能通过TCA处理，然后由CLIP编码器编码。运动序列经MoSA-VQ编码为多层次离散码。RQHC-Transformer以文本嵌入和更粗层的码为条件，自回归地生成所有层级的码，最后通过MoSA-VQ的解码器重建为连续运动。
- **训练方式**：端到端训练。MoSA-VQ的损失（Lᵥq）和RQHC-Transformer的损失（Lcₑ）联合优化。
- **推理流程**：文本输入 -> (可选TCA) -> 文本嵌入 -> RQHC-Transformer自回归生成多层次运动token序列 -> MoSA-VQ解码器重建为运动序列。
- **与已有方法的差异**：与标准RVQ（如MoMask）相比，MoSA-VQ增加了**可学习缩放**和**跨级去相关损失**。与单分辨率解码器或每层独立解码器相比，RQHC-Transformer是**层次化因果**的，结构与量化过程严格对齐。与扩散模型相比，是**单次前向传播**；与标准LLM解码器相比，是**层次化**且参数可能更高效。
## 实验

- **使用的数据集**：
    - 训练与评估：**HumanML3D** 和 **KIT-ML**。
    - 零样本泛化评估：**CMP** 数据集（未在训练中使用）。
- **对比方法**：PDF前9页未列出完整的对比方法列表，但提到了扩散模型、LLM-based模型（如MoMask, T2M-GPT, AttT2M, MotionGPT）等相关工作。
- **评价指标**：PDF前9页未列出具体指标，但常见指标包括运动质量（如FID）、文本-运动对齐度（如R-Precision）、多样性（如Diversity）等。
- **主实验结果**：PDF前9页未提供具体的数字结果。摘要声称“MOGO outperforms prior methods in generation quality, inference efficiency, and temporal scalability”。
- **消融实验**：PDF前9页未详细描述，但提到“Ablation studies are provided in the appendix”。
- **泛化实验**：在**CMP**数据集上的零样本评估，用于检验分布外泛化能力。具体结果未在前9页给出。
- **速度/参数量/FLOPs等效率信息**：摘要和引言强调了“real-time performance”和“lower inference latency”，但前9页未提供具体的推理时间、参数量或FLOPs数据。RQHC-Transformer的设计声称支持“one-pass inference”和“efficient decoding”。
## 局限

1.  **实验细节不完整**：提供的文本（前9页）缺失了关键的实验结果数字、完整的对比方法列表、具体的评价指标结果以及详细的消融实验，无法完全评估其性能优势的幅度。
2.  **对TCA的依赖**：为了达到最佳的泛化性能，模型依赖于一个外部的、通常很大的预训练语言模型（TCA中的 *T*），这增加系统的整体复杂度和部署成本。
3.  **数据领域限制**：实验局限于人体运动生成，其方法（特别是MoSA-VQ的尺度自适应机制）在其他类型的序列生成任务（如文本、语音）中的有效性有待验证。
4.  **长序列质量的潜在衰减**：虽然声称支持无限长度生成，但自回归方法固有的误差累积问题是否在极长序列中依然可控，文本未进行深入分析。
5.  **复现依赖**：完整复现需要MoSA-VQ的编码器/解码器架构细节、RQHC-Transformer的具体层配置（如头数、层数在图1中有示意，但不完整）、以及TCA使用的具体大语言模型和提示词模板，这些在前9页中部分缺失。
## 个人评论

1.  **层次化解耦的表示学习思想**：MoSA-VQ通过可学习缩放和跨级去相关损失，将运动信号分层解耦为不同抽象级别的特征，这为其他领域的序列生成（如音频、时序数据）提供了有启发性的编码范式。
2.  **结构对齐的生成范式**：将编码器（MoSA-VQ）的层次结构直接映射到解码器（RQHC-Transformer）的网络结构上，实现了信息流的高效与稳定。这种“编码-解码结构强耦合”的设计哲学值得借鉴。
3.  **实用的无限长度生成机制**：通过简单的提示词切换和自回归续写，实现了真正灵活、可控的无限长度生成，这比需要固定长度或重新开始生成的方法更贴近实际应用需求。
4.  **无需微调的推理时增强**：TCA策略利用外部大语言模型在推理时提升小模型的理解和泛化能力，是一种高效提升生成质量的后处理思路，可应用于其他生成任务。

### 使用建议

- **如果快速了解**：只读**摘要**、**引言**的第四段（四个贡献点）和**图1**及其说明。这能快速掌握核心思想和框架。
- **如果复现**：重点看**第5节（Methods）**，特别是MoSA-VQ的公式1、2、3和RQHC-Transformer的公式4、5、6、8。结合**图1**理解整体数据流。需要查阅**附录**（如文中所述）获取实验和实现细节。
- **如果借鉴创新点**：
    - **想改进运动/序列量化**：深入学习**MoSA-VQ**的可学习缩放和跨级去相关损失。
    - **想设计高效生成器**：学习**RQHC-Transformer**的层次化因果结构及其与编码器的对齐思想。
    - **想提升模型对复杂文本的泛化力**：借鉴**TCA**的指令分解策略。
- **如果写Related Work**：可放在**分层/多尺度Transformer**、**向量量化与离散表示学习**、**文本到3D/运动生成**这几个相关工作类别中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[D_3D_点云_分类_分割_配准]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉与图形学领域中的**3D人体运动生成**方向，具体聚焦于**文本驱动运动生成（Text-to-Motion）**。它旨在解决现有方法在**实时推理**与**无限长度生成**之间难以兼顾的问题。根据给定的主题标签“D_3D_点云_分类_分割_配准”，本文可归类于3D数据生成与理解范畴，因为3D人体运动序列本质上是一种时序化的3D点云（关节轨迹）数据。

## 2. 一句话总结
本文提出MOGO框架，通过引入**运动尺度自适应残差向量量化（MoSA-VQ）**和**残差量化分层因果Transformer（RQHC-Transformer）**，实现了单次前向传播的实时、高保真3D人体运动生成，并支持通过提示词切换实现无限长度的无缝扩展。

## 3. 背景与问题
- **这篇论文为什么要做**：文本驱动3D人体运动生成在游戏、AR/VR和机器人等领域应用前景广阔。尽管基于大语言模型（LLM）和扩散模型的方法在生成质量上取得进展，但它们分别面临**推理延迟高**（扩散模型依赖迭代求精）和**计算与内存开销大**（LLM模型参数量大、上下文长）的问题，难以满足实时交互应用的需求。
- **之前方法有什么问题**：
    - **扩散模型**：需要多步迭代去噪，推理速度慢，阻碍了实时应用。
    - **LLM-based模型（如T2M-GPT, MoMask）**：虽然可以自回归生成，但通常参数量巨大，对长序列的依赖导致高计算成本。此外，一些方法（如基于掩码的双向模型）在生成可扩展输出和泛化到分布外数据方面存在困难。
- **作者想解决的核心矛盾**：在保证**高运动质量（保真度、多样性）**的同时，实现**极低的推理延迟**和**灵活的时域可扩展性（无限长度生成）**。

## 4. 核心贡献
1.  **提出了MoSA-VQ（运动尺度自适应残差向量量化）模块**：通过可学习的缩放和偏置参数动态调整残差幅度，并引入**跨级去相关损失**强制量化层间的统计正交性，从而获得更紧凑、层次解耦的离散表示。
2.  **设计了RQHC-Transformer（残差量化分层因果Transformer）**：一个与MoSA-VQ量化层次严格对齐的自回归解码器。每个Transformer块对应一个量化层级，实现从粗到细的层次化生成，并支持**单次前向传播**完成解码。
3.  **实现了无缝的无限长度运动生成**：利用框架的自回归特性，支持从任意时间点开始，通过替换文本提示词进行灵活的运动续写，生成任意长度且结构一致、保真度高的运动。
4.  **引入了文本条件对齐（TCA）策略**：利用大语言模型进行**风格标准化**和**指令分解**，将复杂或抽象的用户指令分解为原子动作步骤，显著提升模型对分布内外文本提示的泛化能力和生成精度。

## 5. 方法详解
- **整体框架**：如图1所示，MOGO由四个核心组件构成：1）**MoSA-VQ编码器**，将连续运动序列离散化为多层次潜在码；2）**RQHC-Transformer解码器**，自回归地生成这些多层次码；3）**无限长度生成机制**；4）**TCA文本增强模块**。
- **输入输出**：
    - **输入**：自然语言文本描述。
    - **输出**：与文本描述匹配的3D人体运动序列（关节位置/旋转序列）。
- **关键模块**：
    1.  **MoSA-VQ**：
        - **机制**：基于残差向量量化（RVQ）。对于每个量化层级 *l*，输入残差 *rₗ* 先通过一个**可学习的仿射变换**（缩放矩阵 *Wₗ* 和偏置 *bₗ*）进行调制，然后进行最近邻量化。解码时执行逆变换。
        - **数学解释**：公式 (1) `qₗ = Q(Wₗrₗ + bₗ)` 和 `ϕₗ = (Wₗ)⁻¹(qₗ - bₗ)`。这允许每一级自适应地分配其表示容量。
        - **训练损失**：由四部分构成（公式3）：运动重建损失（L1）、码本承诺损失、**调制参数正则化损失**、以及创新的**跨级去相关损失**（Lₐₑcₒᵣ）。后者最小化量化向量 *ϕₗ* 与下一级残差 *rₗ₊₁* 的协方差，强制信息解耦。
    2.  **RQHC-Transformer**：
        - **结构**：一个因果Transformer，其“堆栈”结构与MoSA-VQ的量化层级对齐。生成第 *l* 层的token序列时，输入序列 *sₗ* 包含文本嵌入 *p*、当前层嵌入 *q_emb* 以及**聚合了所有更粗层级嵌入**的上下文 *t¹:ₙₗ*（公式4）。
        - **位置编码**：采用**相对位置编码**（公式6），以更好地处理变长序列和捕捉长程依赖。
        - **生成过程**：自回归地生成多层级token。训练目标是所有量化层级上的交叉熵损失之和（公式8）。
    3.  **无限长度生成**：在第 *n* 步，模型可以接收新的文本提示 *pₙₑw*，并基于之前生成的token序列 *t¹:ₙ₋₁ₗ* 继续自回归生成（公式9）。新提示立即生效，无需重新生成先前的运动。
    4.  **TCA**：推理时策略。给定原始提示 *cᵣₐw*，先用大语言模型 *T* 进行风格标准化得到 *cₙₒᵣₘ*，再通过思维链（Chain-of-Thought）提示将其分解为一系列原子子指令 *[c⁽¹⁾, ..., c⁽ᴷ⁾]*（公式10），供运动生成模型使用。
- **模块连接**：文本首先可能通过TCA处理，然后由CLIP编码器编码。运动序列经MoSA-VQ编码为多层次离散码。RQHC-Transformer以文本嵌入和更粗层的码为条件，自回归地生成所有层级的码，最后通过MoSA-VQ的解码器重建为连续运动。
- **训练方式**：端到端训练。MoSA-VQ的损失（Lᵥq）和RQHC-Transformer的损失（Lcₑ）联合优化。
- **推理流程**：文本输入 -> (可选TCA) -> 文本嵌入 -> RQHC-Transformer自回归生成多层次运动token序列 -> MoSA-VQ解码器重建为运动序列。
- **与已有方法的差异**：与标准RVQ（如MoMask）相比，MoSA-VQ增加了**可学习缩放**和**跨级去相关损失**。与单分辨率解码器或每层独立解码器相比，RQHC-Transformer是**层次化因果**的，结构与量化过程严格对齐。与扩散模型相比，是**单次前向传播**；与标准LLM解码器相比，是**层次化**且参数可能更高效。

## 6. 实验与结果
- **使用的数据集**：
    - 训练与评估：**HumanML3D** 和 **KIT-ML**。
    - 零样本泛化评估：**CMP** 数据集（未在训练中使用）。
- **对比方法**：PDF前9页未列出完整的对比方法列表，但提到了扩散模型、LLM-based模型（如MoMask, T2M-GPT, AttT2M, MotionGPT）等相关工作。
- **评价指标**：PDF前9页未列出具体指标，但常见指标包括运动质量（如FID）、文本-运动对齐度（如R-Precision）、多样性（如Diversity）等。
- **主实验结果**：PDF前9页未提供具体的数字结果。摘要声称“MOGO outperforms prior methods in generation quality, inference efficiency, and temporal scalability”。
- **消融实验**：PDF前9页未详细描述，但提到“Ablation studies are provided in the appendix”。
- **泛化实验**：在**CMP**数据集上的零样本评估，用于检验分布外泛化能力。具体结果未在前9页给出。
- **速度/参数量/FLOPs等效率信息**：摘要和引言强调了“real-time performance”和“lower inference latency”，但前9页未提供具体的推理时间、参数量或FLOPs数据。RQHC-Transformer的设计声称支持“one-pass inference”和“efficient decoding”。

## 7. 这篇论文真正有价值的地方
1.  **层次化解耦的表示学习思想**：MoSA-VQ通过可学习缩放和跨级去相关损失，将运动信号分层解耦为不同抽象级别的特征，这为其他领域的序列生成（如音频、时序数据）提供了有启发性的编码范式。
2.  **结构对齐的生成范式**：将编码器（MoSA-VQ）的层次结构直接映射到解码器（RQHC-Transformer）的网络结构上，实现了信息流的高效与稳定。这种“编码-解码结构强耦合”的设计哲学值得借鉴。
3.  **实用的无限长度生成机制**：通过简单的提示词切换和自回归续写，实现了真正灵活、可控的无限长度生成，这比需要固定长度或重新开始生成的方法更贴近实际应用需求。
4.  **无需微调的推理时增强**：TCA策略利用外部大语言模型在推理时提升小模型的理解和泛化能力，是一种高效提升生成质量的后处理思路，可应用于其他生成任务。

## 8. 局限与问题
1.  **实验细节不完整**：提供的文本（前9页）缺失了关键的实验结果数字、完整的对比方法列表、具体的评价指标结果以及详细的消融实验，无法完全评估其性能优势的幅度。
2.  **对TCA的依赖**：为了达到最佳的泛化性能，模型依赖于一个外部的、通常很大的预训练语言模型（TCA中的 *T*），这增加系统的整体复杂度和部署成本。
3.  **数据领域限制**：实验局限于人体运动生成，其方法（特别是MoSA-VQ的尺度自适应机制）在其他类型的序列生成任务（如文本、语音）中的有效性有待验证。
4.  **长序列质量的潜在衰减**：虽然声称支持无限长度生成，但自回归方法固有的误差累积问题是否在极长序列中依然可控，文本未进行深入分析。
5.  **复现依赖**：完整复现需要MoSA-VQ的编码器/解码器架构细节、RQHC-Transformer的具体层配置（如头数、层数在图1中有示意，但不完整）、以及TCA使用的具体大语言模型和提示词模板，这些在前9页中部分缺失。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读**摘要**、**引言**的第四段（四个贡献点）和**图1**及其说明。这能快速掌握核心思想和框架。
- **如果复现**：重点看**第5节（Methods）**，特别是MoSA-VQ的公式1、2、3和RQHC-Transformer的公式4、5、6、8。结合**图1**理解整体数据流。需要查阅**附录**（如文中所述）获取实验和实现细节。
- **如果借鉴创新点**：
    - **想改进运动/序列量化**：深入学习**MoSA-VQ**的可学习缩放和跨级去相关损失。
    - **想设计高效生成器**：学习**RQHC-Transformer**的层次化因果结构及其与编码器的对齐思想。
    - **想提升模型对复杂文本的泛化力**：借鉴**TCA**的指令分解策略。
- **如果写Related Work**：可放在**分层/多尺度Transformer**、**向量量化与离散表示学习**、**文本到3D/运动生成**这几个相关工作类别中。

## 10. 和其他论文的关系
根据给定主题“D_3D_点云_分类_分割_配准”和文件名“MOGO 3D人体运动生成 MOGO Motion.pdf”，可能相关的论文包括：
- [[MoMask]]：同为基于残差向量量化（RVQ）的文本运动生成工作，是MOGO的重要对比基线。
- [[T2M-GPT]]：基于GPT的自回归运动生成模型，MOGO旨在改进其效率和质量。
- [[MotionGPT]]：尝试将运动生成建模为多模态语言任务的工作。
- [[HumanML3D]]：本文使用的主要基准数据集。
（注：由于提供的相关工作部分引用了大量文献，但未提供完整的参考文献列表，以上链接仅为基于提及内容的推测。）

## 11. 关键词
3D人体运动生成，文本到运动，向量量化，残差量化，分层Transformer，因果Transformer，实时生成，无限长度生成，可学习缩放，跨级去相关，文本条件对齐（TCA），MoSA-VQ，RQHC-Transformer。

## 12. 可信度说明
本精读笔记**严格基于用户提供的PDF提取文本（前9页）**生成。该文本涵盖了论文的标题、作者、摘要、引言、相关工作、方法概述（包括图1）以及实验部分的开头。笔记中所有对方法、贡献的描述和公式的引用均来自此文本。实验结果、消融研究和部分技术细节（如具体的评价指标数值、网络层配置细节、TCA的完整示例）**在提供的文本中未明确说明或不完整**，因此笔记中相应部分明确指出了信息的缺失。总体而言，文本提取质量较好，核心思想和框架描述清晰，但支撑实验的完整数据缺失。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2782 字符/页)); 来源缓存: `.paper-cache/extracts/MOGO 3D人体运动生成 MOGO Motion.txt` (9/9 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
