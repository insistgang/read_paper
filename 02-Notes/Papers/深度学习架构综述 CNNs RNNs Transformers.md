---
title: "CNNs, RNNs and Transformers in Human Action Recognition: A Survey and a Hybrid Model"
authors:
  - "Khaled Alomar"
  - "Halil Ibrahim Aysel"
  - "Xiaohao Cai"
year: 2024
venue: "arXiv"
doi: 
pdf: [[深度学习架构综述 CNNs RNNs Transformers.pdf]]
primary_topic: R_综述_Survey
topics:
  - "R_综述_Survey"
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
extract_cache: .paper-cache/extracts/深度学习架构综述 CNNs RNNs Transformers.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/29 pages"
---
# CNNs, RNNs and Transformers in Human Action Recognition:

## 基本信息
- **PDF**: [[深度学习架构综述 CNNs RNNs Transformers.pdf]]
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | CNNs, RNNs and Transformers in Human Action Recognition: A Survey and a Hybrid Model |
| **作者** | Khaled Alomar; Halil Ibrahim Aysel; Xiaohao Cai（英国南安普顿大学 电子与计算机科学学院） |
| **发表时间** | 2024（arXiv:2407.06162v2, 2024-08-15；提取缓存仅含前 12 页） |
| **刊物/会议** | arXiv 预印本 |
| **DOI** | 未明确（arXiv:2407.06162） |

## 摘要

> **英文原摘要（据提取文本整理，修复断词与空格）：**
> Human action recognition (HAR) encompasses the task of monitoring human activities across various domains, including but not limited to medical, educational, entertainment, visual surveillance, video retrieval, and the identification of anomalous activities. Over the past decade, the field of HAR has witnessed substantial progress by leveraging convolutional neural networks (CNNs) and recurrent neural networks (RNNs) to effectively extract and comprehend intricate information, thereby enhancing the overall performance of HAR systems. Recently, the domain of computer vision has witnessed the emergence of Vision Transformers (ViTs) as a potent solution. The efficacy of Transformer architecture has been validated beyond the confines of image analysis, extending their applicability to diverse video-related tasks. Notably, within this landscape, the research community has shown keen interest in HAR, acknowledging its manifold utility and widespread adoption across various domains. This article aims to present an encompassing survey that focuses on CNNs and the evolution of RNNs to ViTs given their importance in the domain of HAR. By conducting a thorough examination of existing literature and exploring emerging trends, this study undertakes a critical analysis and synthesis of the accumulated knowledge in this field. Additionally, it investigates the ongoing efforts to develop hybrid approaches. Following this direction, this article presents a novel hybrid model that seeks to integrate the inherent strengths of CNNs and ViTs.
>
> **中文翻译：**
> 人类动作识别（HAR）涉及对人类活动的监测，应用领域广泛，包括但不限于医疗、教育、娱乐、视觉监控、视频检索以及异常活动识别。过去十年间，HAR 借助卷积神经网络（CNN）和循环神经网络（RNN）有效提取并理解复杂信息，取得了实质性进展，提升了 HAR 系统的整体性能。近期，计算机视觉领域涌现出 Vision Transformer（ViT）这一强有力的方案。Transformer 架构的有效性已超越图像分析的范畴，被验证可推广到多种视频相关任务。研究界对 HAR 表现出浓厚兴趣，认可其在各领域的多重价值与广泛应用。本文旨在围绕 CNN 及"RNN 向 ViT 演进"这一主线，呈现一篇涵盖性的综述（因二者在 HAR 中的重要地位）。通过系统梳理已有文献、考察新兴趋势，本研究对该领域积累的知识进行批判性分析与综合，并探讨当前发展混合方案的诸多努力。沿此方向，本文进一步提出一个旨在融合 CNN 与 ViT 内在优势的新颖混合模型。
>
> **关键词（原文）：** Human action recognition · Convolutional neural networks · Recurrent neural networks · Vision Transformers · Deep learning · Video classification

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **任务定义**：HAR 聚焦于对给定视频中所展现的特定动作进行**分类**；与之相对，动作检测与分割关注从视频中精确定位或提取单个动作实例（Ulhaq et al. 2022）。深度模型捕捉视频中空间与时间复杂性的能力，是动作识别与理解的关键。
- **为什么要做**：过去十年的 HAR 综述（Pareek and Thakkar 2021；Sun et al. 2022；Kong and Fu 2022）绝大多数聚焦于 **CNN 与传统机器学习**模型。Transformer（Vaswani et al. 2017）以多头自注意力带来范式转移，在表征质量上超越卷积与递归操作且计算资源更省，并催生了 GPT（Brown et al. 2020）、BERT（Devlin et al. 2018）等 NLP 模型；其衍生的 ViT（Dosovitskiy et al. 2020）在 ImageNet 等大规模数据上达到甚至超越 CNN 的图像识别性能，预示 ViT 有可能像 RNN 被取代那样，撼动 CNN 在 CV 中的主导地位。
- **之前方法的问题**：现有综述**覆盖范围不全**，缺乏一篇能系统纳入 ViT 及 CNN-Transformer 混合模型、同时兼顾 CNN 与 RNN 的近期 HAR 综述，以指引未来研究方向。
- **核心矛盾**：如何系统梳理从 CNN、RNN 到 ViT 的技术演进脉络，并探索将 CNN 的局部特征提取能力与 ViT 的全局关系建模能力相结合，以推动 HAR 技术发展。
## 关键贡献

根据论文引言（Section 1）明确列出，其贡献包括：
1.  **全面的技术回顾**：对 CNN、RNN 和 ViT 进行详尽的技术与演进回顾，考察从传统方法到最新架构的发展。
2.  **广泛的文献综述**：对与 HAR 相关的现有文献进行广泛的审查与分析。
3.  **提出新颖的混合模型**：提出一个融合 CNN 与 ViT 优势的新颖混合模型，并给出该模型与现有模型的详细性能对比分析，凸显其在复杂 HAR 任务上以更高准确率与效率的处理能力（注：模型与实验位于第 4 节，提取缓存的前 12 页未覆盖该部分细节）。
4.  **趋势与方向讨论**：讨论 HAR 技术的新兴趋势与未来方向，强调混合模型对增强 HAR 系统**可解释性与鲁棒性**的重要意义。
## 方法

- **整体框架（论文结构）**：第 2 节为背景（CNN、RNN、ViT 的按时间线技术回顾）；第 3 节综述相关 HAR 工作并简要讨论；**第 4 节提出 CNN+ViT 混合模型，含实验设置与结果**；第 5 节讨论挑战与未来方向；第 6 节结论。提取缓存仅覆盖前 12 页，截至第 2.2.5 节"注意力机制"（停在 Luong et al. 2015 处），**故第 4 节混合模型的具体架构与实验细节在提取文本中未覆盖**。
- **对现有架构的回顾**：
    - **CNNs（第 2.1 节）**：从 Neocognitron（Fukushima 1980）、LeNet-5（LeCun et al. 1998）到 AlexNet（Krizhevsky et al. 2012），并归因于 ImageNet（Deng et al. 2009）大数据与 GPU 算力；随后是 VGGNet（统一小卷积核设计）、GoogLeNet（Inception 多尺度模块）、ResNet（残差学习训练极深网络）。
    - **时空 CNN（第 2.1.1 节）**：三类主流路线——(1) **3D 卷积**将 2D 核扩展到 3D、第三维表示时间（Hara et al. 2018；Tran et al. 2015）；(2) **双流 CNN**并行运行空间流（单帧）与时间流（通常基于光流捕捉帧间运动）（Simonyan and Zisserman 2014a；Feichtenhofer et al. 2016）；(3) **CNN+RNN**用 CNN 提空间特征、用 LSTM/GRU 处理时间依赖（Yue-Hei Ng et al. 2015；Donahue et al. 2015）。
    - **RNNs（第 2.2 节）**：统一记号——输入嵌入 xₜ∈ℝ^{n_x}、隐状态 hₜ₋₁∈ℝ^{n_h}、隐到隐权重 W∈ℝ^{n_h×n_h}、输入到隐权重 U∈ℝ^{n_h×n_x}、偏置 b，每个 cell 输出新隐状态 hₜ∈ℝ^{n_h}。
    - **注意力与 Transformer（第 2.2.5 节）**：Graves（2013）最早提出注意力概念；Bahdanau et al.（2014）提出**加性注意力**（用前馈网络计算权重，改进机器翻译）；Luong et al.（2015）提出**乘性/点积注意力**（query 与所有 key 做点积，简化计算）。Transformer（Vaswani et al. 2017）以多头自注意力彻底改变序列建模范式（注：自注意力与 ViT 的具体公式位于 2.2.5 节之后，提取文本截断未覆盖）。
- **关键模块与机制（含公式编号）**：
    - **Vanilla RNN（2.2.1）**：无 cell state，仅靠隐状态记忆，hₜ = tanh(W·hₜ₋₁ + U·xₜ + b)（公式 1）。局限：序列计算难以并行（Graves et al. 2013）、长序列易梯度爆炸/消失（Bengio et al. 1994）。
    - **LSTM（2.2.2）**：Hochreiter & Schmidhuber（1997）提出，引入独立的 cell state cₜ（如"高速公路"使信息平稳流动），Gers et al.（2000）加入遗忘门。三门——遗忘门 fₜ（公式 2）决定从 cₜ₋₁ 丢弃多少，输入门 iₜ（公式 3）+ 候选值 c̃ₜ（公式 4）、更新 cₜ = fₜ⊙cₜ₋₁ + iₜ⊙c̃ₜ（公式 5，⊙ 为 Hadamard 积），输出门 oₜ（公式 6）、隐状态 hₜ = tanh(cₜ)⊙oₜ（公式 7）。长短期记忆能力优于 vanilla RNN，但复杂度上升。
    - **GRU（2.2.3）**：Chung et al.（2014）提出，将 cell state 与隐状态合并、把遗忘门与输入门合并为"更新门"，权重更少、计算更高效。更新门 zₜ（公式 8）、重置门 rₜ（公式 9）、候选 h̃ₜ = tanh(W·(rₜ⊙hₜ₋₁) + U·xₜ + b)（公式 10）、hₜ = zₜ⊙h̃ₜ + (1−zₜ)⊙hₜ₋₁（公式 11）。
    - **RNN 四种结构（2.2.4）**：一对一（标准网络）、一对多（如图像描述生成）、多对一（如情感分析）、多对多（等长 / 不等长两类；不等长用编码器-解码器，编码器为多对一、解码器为一对多）。Kalchbrenner & Blunsom（2013）首倡将整句映射为向量，Cho et al.（2014）、Sutskever et al.（2014）相关；上下文向量长度通常为 **256、512 或 1024**；带注意力的 seq2seq 见图 3b。
- **与已有方法的差异**：核心在于**视角与整合**——不同于以往只关注 CNN 或 CNN+RNN 的 HAR 综述，本文首次系统串起"RNN→Transformer"演进线，并将 ViT 与混合模型作为关键部分纳入 HAR 综述框架。
- **论文类型特化**：本文为**综述类**论文，主体是系统梳理、比较与分析现有技术并指明方向（如混合模型），同时附带一个自提出的 CNN-ViT 混合模型作为实证补充。
## 实验

**提取缓存（前 12 页）未包含实验部分。** 据论文结构，实验设置、混合模型结果与性能对比位于**第 4 节**，该节内容不在提取文本中。因此具体数据集、对比方法、评价指标、主实验/消融结果、效率信息在提取文本中**均未找到**。

据原文后续页（全文补读记录，提取缓存未覆盖，待核）：第 3 节的综述提到 3D CNN 路线上的代表工作，涉及 **C3D（通用 3D CNN）、P3D（2D+3D 结合）、X3D（Feichtenhofer 2020，沿多维扩展的高效视频模型族）、长时程时序卷积、时序 3D ConvNet** 等，常用基准为 **UCF-101 与 HMDB-51**（见原文 Table 2「3D CNN-based approaches in HAR」）。这些线索来自补读记录的页面摘录，具体数值与表格内容尚待核对。
## 局限

- **混合模型与实验在提取文本中缺失**：提取缓存仅含前 12 页（背景与回顾），论文核心创新点之一——所提 CNN-ViT 混合模型的设计、实验与结果（第 4 节）——不在其中，无法据提取文本评估其有效性与实用性。
- **时效性与覆盖范围**：作为 2024-08 的 arXiv 预印本（v2），虽能覆盖较近期工作，但综述对"最新"的界定与文献选择的全面性仍可能存在局限。
- **效率/计算成本分析（提取部分内）未见对比**：在提取到的前 12 页中，未对不同架构（尤其 Transformer 与混合模型）的计算复杂度（FLOPs、参数量、训练/推理速度）作系统量化对比；这对实际部署很关键（注：相关讨论可能在未覆盖的后续页）。
- **综述固有局限**：综述本身不提供新的实证基准，读者需回到原文第 4 节与所引文献核对具体结论。
## 个人评论

1.  **清晰的演进脉络梳理**：论文把 CNN、RNN（含 LSTM、GRU）到 Transformer 的演进，从数学公式（公式 1–11）到架构思想都讲得连贯，是理解这些基础模型如何迁移到时序/视频数据的优秀入门材料；尤其 LSTM/GRU 的门控公式与 seq2seq 编码器-解码器部分讲解扎实。
2.  **凸显混合模型趋势**：明确指出纯 CNN 或纯 Transformer 都未必最优，**CNN 的局部归纳偏置 + Transformer 的全局关系建模**是值得探索的方向，对设计高效视频理解模型有直接启发。
3.  **综合性视角**：在 HAR 这一具体任务下把 CNN、RNN、ViT 与混合模型串联讨论，避免孤立看待某类模型，便于全面评估不同技术路线优缺点。
4.  **可改进处**：摘要+前 12 页主要停留在"教科书式"的架构回顾，真正的差异化价值（自提混合模型、与 SOTA 的定量对比）集中在第 4 节；若要据本笔记判断方法新颖性与实证强度，必须补读原文后半部分。

### 使用建议

- **如果快速了解**：重点读**摘要**、**引言（Section 1）** 与**背景（Section 2）** 的概要和子标题，可快速掌握目的、范围与三类架构的技术精髓。
- **如果复现**：需获取**完整版本**，尤其**第 4 节**的混合模型架构图、训练细节、超参、数据集预处理与实验代码/链接（提取缓存未覆盖）。
- **如果借鉴创新点**：深入其对 CNN/RNN/Transformer 技术特点的对比，以及"如何构思融合不同架构优势的混合模型"，关注背景里强调的"时空特征提取"与"全局关系建模"两个核心需求。
- **如果写 Related Work**：可作为"HAR 综述 / 视频理解深度学习架构综述"的关键参考；若自己工作涉及 **CNN-Transformer 混合架构**，本文引言与相关讨论是极佳引用来源。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属计算机视觉中的**深度学习架构综述（Survey）**方向，具体聚焦**人类动作识别（HAR）**任务，系统梳理 CNN、RNN 及其向 Vision Transformer（ViT）演进的三类核心架构，并自提一个 CNN-ViT 混合模型。来自英国南安普顿大学（Alomar, Aysel, Cai；arXiv:2407.06162v2, 2024-08-15）。其核心目的是填补现有综述（多偏 CNN 与传统机器学习）的空白，提供涵盖 CNN、RNN、最新 ViT 及混合模型的全面视角。归入"R_综述_Survey"主题恰当。

## 2. 一句话总结
本文系统回顾用于 HAR 的 CNN、RNN 与 ViT 架构演进（含 LSTM/GRU/注意力的数学推导），并提出一个旨在融合 CNN 与 ViT 优势的混合模型以提升识别性能。

## 3. 背景与问题
- **为什么要做**：过去十年 HAR 综述多偏 CNN 与传统机器学习；Transformer（Vaswani et al. 2017）以多头自注意力带来范式转移并在 NLP（GPT、BERT）大获成功，衍生的 ViT（Dosovitskiy et al. 2020）在大规模图像识别上比肩甚至超越 CNN，预示其可能像 RNN 被取代那样撼动 CNN 在 CV 的主导地位。视频识别相较图像更难（需理解视频序列中的事件），因此亟需一篇纳入 ViT 与混合模型、兼顾 CNN/RNN 的近期 HAR 综述。
- **之前方法的问题**：现有综述覆盖不全，未及时纳入并分析以 ViT 为代表的新兴架构在 HAR 的进展。
- **核心矛盾**：如何系统梳理 CNN→RNN→ViT 的演进，并探索 CNN 局部特征提取 + ViT 全局关系建模相结合的路径。

## 4. 核心贡献
据引言明确列出：
1.  **全面技术回顾**：CNN、RNN、ViT 的演进与技术回顾（从传统方法到最新架构）。
2.  **广泛文献综述**：对 HAR 相关文献的广泛审查与分析。
3.  **新颖混合模型**：提出融合 CNN 与 ViT 优势的混合模型，并给出与现有模型的详细性能对比，凸显其在复杂 HAR 任务上更高的准确率与效率（模型/实验在第 4 节，提取缓存未覆盖）。
4.  **趋势与方向**：讨论 HAR 新兴趋势与未来方向，强调混合模型对增强系统**可解释性与鲁棒性**的意义。

## 5. 方法详解
- **整体结构**：第 2 节背景（CNN/RNN/ViT 按时间线回顾）→ 第 3 节相关 HAR 工作综述 → 第 4 节自提 CNN-ViT 混合模型（含实验设置与结果）→ 第 5 节挑战与未来 → 第 6 节结论。提取缓存仅前 12 页，截至 2.2.5 注意力（停在 Luong et al. 2015），故第 4 节细节不在提取文本中。
- **CNN 线（2.1 / 2.1.1）**：Neocognitron→LeNet-5→AlexNet→VGGNet/GoogLeNet/ResNet；时空 CNN 三路线——3D 卷积（Hara 2018, Tran 2015）、双流 CNN（空间流 + 光流时间流；Simonyan & Zisserman 2014a, Feichtenhofer 2016）、CNN+RNN（CNN 提空间、LSTM/GRU 处理时间；Yue-Hei Ng 2015, Donahue 2015）。
- **RNN 线（2.2.1–2.2.4）**：
    - **Vanilla RNN**：hₜ = tanh(W·hₜ₋₁ + U·xₜ + b)（公式 1）；无 cell state，长序列梯度爆炸/消失、难并行。
    - **LSTM**：cell state cₜ + 三门（遗忘 fₜ 公式 2、输入 iₜ 公式 3 与候选 c̃ₜ 公式 4、cₜ 更新公式 5、输出 oₜ 公式 6、hₜ 公式 7）；长短期记忆优于 vanilla 但更复杂。
    - **GRU**：合并 cell/隐状态、合并遗忘+输入门为更新门；更新门 zₜ（8）、重置门 rₜ（9）、候选 h̃ₜ（10）、hₜ = zₜ⊙h̃ₜ +(1−zₜ)⊙hₜ₋₁（11）；权重更少、效率更高、性能与 LSTM 相当。
    - **四种结构**：一对一/一对多（图像描述）/多对一（情感分析）/多对多（等长 + 不等长；不等长用编码器-解码器，上下文向量长度 256/512/1024，编码器与解码器均为 RNN）。
- **注意力线（2.2.5）**：Graves（2013）提出注意力概念；Bahdanau（2014）加性注意力（前馈网络算权重）；Luong（2015）乘性/点积注意力（query·key 简化计算）。Transformer（Vaswani 2017）多头自注意力革新序列建模（具体公式在截断点之后，提取文本未覆盖）。
- **与已有差异 / 类型**：核心是视角与整合——首次把 RNN→Transformer 演进线与 ViT、混合模型纳入 HAR 综述框架；属综述类论文，附带自提混合模型作为实证。

## 6. 实验与结果
**提取缓存（前 12 页）未包含实验。** 据论文结构，实验、混合模型结果与性能对比位于**第 4 节**，不在提取文本中；具体数据集、对比方法、评价指标、主实验/消融结果、效率信息在提取文本中均未找到。

据原文后续页（全文补读记录，提取缓存未覆盖，待核）：第 3 节综述涉及 **C3D、P3D、X3D（Feichtenhofer 2020）、长时程时序卷积、时序 3D ConvNet** 等 3D CNN 路线工作，常用基准为 **UCF-101 / HMDB-51**（原文 Table 2「3D CNN-based approaches in HAR」）。这些来自补读页面摘录，数值与表格内容待核。

## 7. 这篇论文真正有价值的地方
1.  **演进脉络清晰**：CNN→RNN（LSTM/GRU）→Transformer 从公式（1–11）到架构思想讲得连贯，是时序/视频建模基础的优秀入门。
2.  **凸显混合模型趋势**：明确"纯 CNN / 纯 Transformer 未必最优"，**局部归纳偏置 + 全局关系建模**结合是重要方向，对设计高效视频理解模型有直接启发。
3.  **综合性视角**：在 HAR 任务下把 CNN/RNN/ViT/混合模型串联评估，避免孤立看模型。

## 8. 局限与问题
- **混合模型与实验在提取文本中缺失**：提取缓存仅前 12 页（背景+回顾），第 4 节混合模型设计/实验/结果不在其中，无法据提取文本评估其有效性。
- **时效性与覆盖范围**：2024-08 的 arXiv v2 预印本，"最新"界定与文献全面性可能有局限。
- **效率分析（提取部分内）未见对比**：前 12 页未对不同架构作 FLOPs/参数量/速度的系统量化对比（相关讨论或在未覆盖的后续页）。
- **综述固有局限**：不提供新实证基准，需回原文第 4 节与引文核对。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要、引言（Section 1）、背景（Section 2）概要与子标题。
- **复现**：取完整版本，尤其第 4 节混合模型架构图、训练细节、超参、数据集预处理与实验代码/链接（提取缓存未覆盖）。
- **借鉴创新点**：学其 CNN/RNN/Transformer 技术对比，及"如何构思融合不同架构优势的混合模型"，关注"时空特征提取 + 全局关系建模"两个核心需求。
- **写 Related Work**：作为 HAR / 视频理解架构综述的关键参考；涉及 CNN-Transformer 混合架构时，本文引言与讨论是极佳引用源。

## 10. 和其他论文的关系
- [[Vision Transformer (ViT) (Dosovitskiy et al., 2020)]]：本文将 ViT 作为 CNN 的重要竞争者与潜在替代者讨论。
- [[AlexNet (Krizhevsky et al., 2012)]]、[[ResNet (He et al., 2016)]]、VGGNet（Simonyan & Zisserman 2014a）、GoogLeNet（Szegedy et al. 2015）：作为 CNN 里程碑被回顾。
- [[LSTM (Hochreiter and Schmidhuber, 1997)]]、[[GRU (Chung et al., 2014)]]：作为 RNN 关键改进被深入解析（含完整门控公式）。
- [[Attention Is All You Need (Vaswani et al., 2017)]]：Transformer 奠基工作；注意力前驱包括 Graves(2013)、Bahdanau(2014) 加性、Luong(2015) 乘性。
- [[Two-Stream CNNs (Simonyan and Zisserman, 2014a)]]、3D 卷积（Tran 2015 / Hara 2018）、CNN+RNN（Donahue 2015 / Yue-Hei Ng 2015）：处理视频时空信息的经典 CNN 方法。
- HAR 基准数据集（据补读记录提到 UCF-101、HMDB-51；提取文本前 12 页未列出具体数据集名称）。

## 11. 关键词
人类动作识别 (Human Action Recognition), 卷积神经网络 (CNN), 循环神经网络 (RNN), Vision Transformer (ViT), 深度学习, 混合模型, 注意力机制, LSTM, GRU, 时空特征, 视频分类, 综述

## 12. 可信度说明
本精读笔记**严格基于提供的 PDF 提取文本（前 12 页，约 25000 字符）生成**，内容主要来源于论文的**摘要、引言（Section 1）与背景（Section 2，至 2.2.5 注意力、停在 Luong et al. 2015）**。这些部分对论文定位、动机、贡献与主要技术回顾（CNN/RNN/Transformer 演进、LSTM/GRU/注意力公式）有清晰阐述。
**提取质量评估**：文本提取质量良好、内容连贯；少量数学符号与图轴标注（图 1–3 的 cell 标签）在纯文本中有粘连，已在引用时还原为标准记号。
**重要限制**：提取缓存仅覆盖全文 29 页中的前 12 页，**论文后半的关键内容（第 3 节详细文献综述、第 4 节混合模型架构与实验、第 5 节挑战与未来方向、第 6 节结论）均不在提取文本中**。涉及混合模型细节、实验数据集（UCF-101/HMDB-51）、指标与趋势的部分系据"全文补读记录"的页面线索标注，**数值与具体结论待核**。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (约 2086 字符/页), 提取缓存覆盖前 12/29 页); 来源缓存: `.paper-cache/extracts/深度学习架构综述 CNNs RNNs Transformers.txt` (提取 12/29 页; 原 AI 主体 12/29 + 全文补读 13-29); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。本次复读据提取文本核对并修正: 标题补全副标题、年份 2022→2024 (arXiv:2407.06162v2, 2024-08-15)、摘要去乱码重建并附中译、各节补全引用与公式编号。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-29; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-29。
- **提取情况**: 缺失页 17 页, 其中 17 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Feichtenhofer (2020) proposed X3D, a family of efficient video models by expanding architectures along
- p.13: Paper Model Dataset Novelty
- p.13: HMDB-51Introduced 3D CNNs for HAR, effectively capturing
- p.13: UCF-101Introduced C3D, a generic 3D CNN for
- p.13: HMDB-51Introduced long-term temporal convolutions to
- p.13: UCF-101Proposed P3D networks combining 2D and 3D
- p.13: Carreira and
- p.13: Zisserman
- p.13: UCF-101Evaluated the scalability of 3D CNNs with
- p.13: HMDB-51Introduced a new temporal 3D ConvNet architecture
- p.13: UCF-101Conducted a comprehensive analysis of
- p.13: UCF-101Explored speed-accuracy trade-offs in

### 缺失页关键摘录

- p.13: using depthwise separable convolutions and achieved competitive accuracy with significantly reduced com-
- p.13: temporal attention mechanism and achieved high accuracy with efficient computation by focusing on salient
- p.13: selectively focusing on important temporal features to enhance the efficiency and accuracy of 3D CNNs,
- p.13: Table 2 presents the works discussed in this section that utilized 3D CNN approaches.
- p.13: Table 2 : 3D CNN-based approaches in HAR.
- p.13: UCF-101Explored speed-accuracy trade-offs in
- p.13: complexity without sacrificing accuracy.
- p.14: competitive accuracy with reduced computational
- p.14: enhance efficiency and accuracy in 3D CNNs.
- p.14: effective video representation learning on the UCF-101 dataset, showcasing the versatility and potential of
- p.14: UCF-101 and HMDB-51 datasets, demonstrated substantial improvements in video classification accuracy.
- p.14: UCF-101 datasets, achieved notable improvements in accuracy and efficiency, showcasing the practicality of
<!-- AI_READING_NOTE_END -->
