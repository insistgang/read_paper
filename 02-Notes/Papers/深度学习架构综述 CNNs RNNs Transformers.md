---
title: "CNNs, RNNs and Transformers in Human Action Recognition:"
authors:
  - "Khaled Alomar"
  - "Halil Ibrahim Aysel"
  - "Xiaohao Cai"
year: 2022
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
| **题目** | CNNs, RNNs and Transformers in Human Action Recognition: |
| **作者** | Khaled Alomar; Halil Ibrahim Aysel; Xiaohao Cai |
| **发表时间** | 2022 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Human action recognition (HAR) encompasses the task of monitoring human activities across various domains, including but not limited to medical, educational, entertainment, visual surveillance, video retrieval,andtheidentificationofanomalousactivities.Overthepastdecade,thefieldofHARhaswit- nessed substantial progress by leveraging convolutional neural networks (CNNs) and recurrent neural networks (RNNs) to effectively extract and comprehend intricate information, thereby enhancing the overall performance of HAR systems. Recently, the domain of computer vision has witnessed the emer- gence of Vision Transformers (ViTs) as a potent solution. The efficacy of Transformer architecture has been validated beyond the confines of image analysis, extending their applicability to diverse video- related tasks. Notably, within this landscape, the research community has shown keen interest in HAR, acknowledgingitsmanifoldutilityandwidespreadadoptionacrossvariousdomains.Thisarticleaimsto present an e

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：过去十年，HAR领域主要依赖CNN和RNN。然而，近期Vision Transformer（ViT）在计算机视觉（包括图像和视频任务）中展现出强大潜力，可能取代CNN的主导地位（如同Transformer在NLP中取代RNN）。现有综述论文大多仅关注CNN和传统方法，缺乏对最新Transformer架构及混合模型在HAR中应用的全面审视。
- **之前方法的问题**：现有综述论文存在**覆盖范围不全**的问题，未能及时纳入和分析以ViT为代表的新兴架构及其在HAR中的研究进展。
- **核心矛盾**：如何系统梳理从CNN、RNN到ViT的技术演进脉络，并探索将CNN的局部特征提取能力与ViT的全局建模能力相结合，以推动HAR技术发展的路径。
## 关键贡献

根据论文引言明确列出，其贡献包括：
1.  **全面的技术回顾**：对CNN、RNN和ViT进行了详尽的技术和演进回顾，考察了从传统方法到最新架构的发展。
2.  **广泛的文献综述**：对与HAR相关的现有文献进行了广泛的审查和分析。
3.  **提出新颖的混合模型**：提出了一个结合CNN和ViT优势的新颖混合模型，并提供了该模型与现有模型的详细性能对比分析，突显其在处理复杂HAR任务时的准确性和效率。
4.  **趋势与方向讨论**：讨论了HAR技术的新兴趋势和未来方向，强调了混合模型在增强HAR系统可解释性和鲁棒性方面的重要性。
## 方法

- **整体框架**：本文是一篇综述论文，其主体结构分为对CNN、RNN到ViT的技术背景回顾（第2节），对现有HAR工作的综述（第3节），以及一个**新提出的CNN-ViT混合模型**（第4节）。由于提供的PDF文本仅包含前12页，截至第2.2.5节“注意力机制”，因此**新混合模型的具体架构细节（第4节）在提供的文本中未包含**。
- **对现有架构的回顾**：
    - **CNNs**：回顾了从Neocognitron、LeNet-5到AlexNet、VGGNet、GoogLeNet、ResNet的演进。重点介绍了用于视频的**时空CNN**，包括3D卷积、双流CNN（RGB + 光流）以及CNN与RNN的结合。
    - **RNNs**：详细解释了**Vanilla RNN**、**LSTM**和**GRU**的数学原理（包含公式）和门控机制。阐述了RNN的四种结构（一对一、一对多、多对一、多对多），并介绍了用于序列到序列任务的编码器-解码器架构。
    - **注意力机制与Transformer**：从Graves的早期工作，到Bahdanau的加性注意力和Luong的乘性注意力，阐述了注意力机制如何被引入以增强序列模型。文中指出，Transformer架构（Vaswani et al., 2017）通过多头自注意力机制彻底改变了序列建模范式。
- **关键模块与机制解释**：
    - **LSTM**：通过遗忘门、输入门、输出门和一个独立的“细胞状态”来选择性记忆和遗忘信息，以解决长期依赖和梯度问题（公式2-7）。
    - **GRU**：将LSTM的细胞状态和隐藏状态合并，用“更新门”和“重置门”简化结构，在保持性能的同时提高计算效率（公式8-11）。
    - **注意力**：通过计算查询（Query）与键（Key）之间的相关性分数，为数值（Value）分配动态权重，使模型能够聚焦于输入序列中最相关的部分。
- **与已有方法的差异**：本文的核心在于**视角和整合**。它不同于以往只关注CNN或CNN+RNN的HAR综述，首次系统地将从RNN到Transformer的演进线，并将新兴的ViT和混合模型作为关键部分纳入HAR的综述框架中。
- **论文类型特化**：本文为**综述类**论文，没有提出单一的新网络模块，而是系统梳理、比较和分析现有技术，并为后续研究指明方向（如混合模型）。
## 实验

**提供的文本中未包含实验部分。** 根据论文结构描述，实验、结果及性能对比应位于第4节，但该部分内容未在提供的前12页文本中。因此，关于具体使用的数据集、对比方法、评价指标、主实验结果、消融实验、效率信息等，在**提供的文本中均未找到**。
## 局限

- **时效性与覆盖范围**：作为2024年8月发布的arXiv预印本，它应能覆盖近期工作，但作为综述，其“最新”的界定和文献选择的全面性可能存在局限。
- **混合模型细节缺失**：由于只提供了文本的前半部分（背景和回顾），**论文的核心创新点之一——所提出的CNN-ViT混合模型的具体设计、实验细节和结果——在提供的文本中完全缺失**，无法对其有效性和实用性进行评估。
- **实验验证不充分**：基于提供的文本，无法判断其提出的混合模型是否在多个主流数据集上进行了充分实验，与最前沿的模型相比是否有竞争力。
- **计算成本分析缺乏**：文中未在提供部分讨论不同架构（尤其是Transformer和混合模型）的计算复杂度（如FLOPs、参数量、训练/推理速度）对比，这对实际部署至关重要。
## 个人评论

1.  **清晰的演进脉络梳理**：论文对CNN、RNN（包括LSTM、GRU）以及向Transformer的演进提供了从数学原理到架构思想的清晰图解和解释，是理解这些基础模型如何应用于时序/视频数据的优秀入门资料。
2.  **凸显混合模型的趋势**：明确指出单纯依赖某一种架构（如纯CNN或纯Transformer）可能不是最优解，探索**CNN的局部归纳偏置与Transformer的全局建模能力相结合**是未来的重要方向。这对后续研究如何设计高效的视频理解模型具有直接启发。
3.  **综述的综合性视角**：在HAR这个具体任务下，将CNN、RNN、ViT及混合模型串联起来进行讨论，避免了孤立地看某一类模型，有助于研究者全面评估不同技术路线的优缺点。

### 使用建议

- **如果快速了解**：重点阅读**摘要（Abstract）**、**引言（Section 1）** 以及**背景部分（Section 2）** 的概要和子标题。这能快速掌握论文的目的、范围和核心架构的技术精髓。
- **如果复现**：需要查找并阅读论文的**完整版本**，特别是**第4节**，以获取所提混合模型的完整架构图、训练细节、超参数设置、数据集预处理以及实验结果代码或链接。
- **如果借鉴创新点**：应深入学习其对CNN、RNN、Transformer技术特点的对比分析，以及**如何构思一个融合不同架构优势的混合模型**。关注其在“背景”中强调的“时空特征提取”与“全局关系建模”这两个核心需求。
- **如果写Related Work**：本文可作为“HAR综述”或“视频理解深度学习架构综述”的关键参考文献。如果自己的工作涉及**CNN-Transformer混合架构**，本文的引言和相关讨论部分是极佳的引用来源。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉（CV）领域中深度学习架构综述（Survey）方向。具体聚焦于**人类动作识别**任务，系统性地梳理了用于该任务的三种核心深度学习架构：卷积神经网络（CNN）、循环神经网络（RNN）及其向Vision Transformer（ViT）的演进。其核心目的是填补现有综述的空白（主要关注CNN和传统机器学习），提供一个涵盖CNN、RNN、最新ViT架构以及混合模型的全面视角。该论文适合放在“计算机视觉-视频理解-动作识别-深度学习架构综述”这个主题下。

## 2. 一句话总结
本文系统回顾了用于人类动作识别（HAR）的CNN、RNN和Vision Transformer（ViT）架构的演进，并提出了一种旨在结合CNN与ViT优势的混合模型以提升识别性能。

## 3. 背景与问题
- **为什么要做**：过去十年，HAR领域主要依赖CNN和RNN。然而，近期Vision Transformer（ViT）在计算机视觉（包括图像和视频任务）中展现出强大潜力，可能取代CNN的主导地位（如同Transformer在NLP中取代RNN）。现有综述论文大多仅关注CNN和传统方法，缺乏对最新Transformer架构及混合模型在HAR中应用的全面审视。
- **之前方法的问题**：现有综述论文存在**覆盖范围不全**的问题，未能及时纳入和分析以ViT为代表的新兴架构及其在HAR中的研究进展。
- **核心矛盾**：如何系统梳理从CNN、RNN到ViT的技术演进脉络，并探索将CNN的局部特征提取能力与ViT的全局建模能力相结合，以推动HAR技术发展的路径。

## 4. 核心贡献
根据论文引言明确列出，其贡献包括：
1.  **全面的技术回顾**：对CNN、RNN和ViT进行了详尽的技术和演进回顾，考察了从传统方法到最新架构的发展。
2.  **广泛的文献综述**：对与HAR相关的现有文献进行了广泛的审查和分析。
3.  **提出新颖的混合模型**：提出了一个结合CNN和ViT优势的新颖混合模型，并提供了该模型与现有模型的详细性能对比分析，突显其在处理复杂HAR任务时的准确性和效率。
4.  **趋势与方向讨论**：讨论了HAR技术的新兴趋势和未来方向，强调了混合模型在增强HAR系统可解释性和鲁棒性方面的重要性。

## 5. 方法详解
- **整体框架**：本文是一篇综述论文，其主体结构分为对CNN、RNN到ViT的技术背景回顾（第2节），对现有HAR工作的综述（第3节），以及一个**新提出的CNN-ViT混合模型**（第4节）。由于提供的PDF文本仅包含前12页，截至第2.2.5节“注意力机制”，因此**新混合模型的具体架构细节（第4节）在提供的文本中未包含**。
- **对现有架构的回顾**：
    - **CNNs**：回顾了从Neocognitron、LeNet-5到AlexNet、VGGNet、GoogLeNet、ResNet的演进。重点介绍了用于视频的**时空CNN**，包括3D卷积、双流CNN（RGB + 光流）以及CNN与RNN的结合。
    - **RNNs**：详细解释了**Vanilla RNN**、**LSTM**和**GRU**的数学原理（包含公式）和门控机制。阐述了RNN的四种结构（一对一、一对多、多对一、多对多），并介绍了用于序列到序列任务的编码器-解码器架构。
    - **注意力机制与Transformer**：从Graves的早期工作，到Bahdanau的加性注意力和Luong的乘性注意力，阐述了注意力机制如何被引入以增强序列模型。文中指出，Transformer架构（Vaswani et al., 2017）通过多头自注意力机制彻底改变了序列建模范式。
- **关键模块与机制解释**：
    - **LSTM**：通过遗忘门、输入门、输出门和一个独立的“细胞状态”来选择性记忆和遗忘信息，以解决长期依赖和梯度问题（公式2-7）。
    - **GRU**：将LSTM的细胞状态和隐藏状态合并，用“更新门”和“重置门”简化结构，在保持性能的同时提高计算效率（公式8-11）。
    - **注意力**：通过计算查询（Query）与键（Key）之间的相关性分数，为数值（Value）分配动态权重，使模型能够聚焦于输入序列中最相关的部分。
- **与已有方法的差异**：本文的核心在于**视角和整合**。它不同于以往只关注CNN或CNN+RNN的HAR综述，首次系统地将从RNN到Transformer的演进线，并将新兴的ViT和混合模型作为关键部分纳入HAR的综述框架中。
- **论文类型特化**：本文为**综述类**论文，没有提出单一的新网络模块，而是系统梳理、比较和分析现有技术，并为后续研究指明方向（如混合模型）。

## 6. 实验与结果
**提供的文本中未包含实验部分。** 根据论文结构描述，实验、结果及性能对比应位于第4节，但该部分内容未在提供的前12页文本中。因此，关于具体使用的数据集、对比方法、评价指标、主实验结果、消融实验、效率信息等，在**提供的文本中均未找到**。

## 7. 这篇论文真正有价值的地方
1.  **清晰的演进脉络梳理**：论文对CNN、RNN（包括LSTM、GRU）以及向Transformer的演进提供了从数学原理到架构思想的清晰图解和解释，是理解这些基础模型如何应用于时序/视频数据的优秀入门资料。
2.  **凸显混合模型的趋势**：明确指出单纯依赖某一种架构（如纯CNN或纯Transformer）可能不是最优解，探索**CNN的局部归纳偏置与Transformer的全局建模能力相结合**是未来的重要方向。这对后续研究如何设计高效的视频理解模型具有直接启发。
3.  **综述的综合性视角**：在HAR这个具体任务下，将CNN、RNN、ViT及混合模型串联起来进行讨论，避免了孤立地看某一类模型，有助于研究者全面评估不同技术路线的优缺点。

## 8. 局限与问题
- **时效性与覆盖范围**：作为2024年8月发布的arXiv预印本，它应能覆盖近期工作，但作为综述，其“最新”的界定和文献选择的全面性可能存在局限。
- **混合模型细节缺失**：由于只提供了文本的前半部分（背景和回顾），**论文的核心创新点之一——所提出的CNN-ViT混合模型的具体设计、实验细节和结果——在提供的文本中完全缺失**，无法对其有效性和实用性进行评估。
- **实验验证不充分**：基于提供的文本，无法判断其提出的混合模型是否在多个主流数据集上进行了充分实验，与最前沿的模型相比是否有竞争力。
- **计算成本分析缺乏**：文中未在提供部分讨论不同架构（尤其是Transformer和混合模型）的计算复杂度（如FLOPs、参数量、训练/推理速度）对比，这对实际部署至关重要。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**摘要（Abstract）**、**引言（Section 1）** 以及**背景部分（Section 2）** 的概要和子标题。这能快速掌握论文的目的、范围和核心架构的技术精髓。
- **如果复现**：需要查找并阅读论文的**完整版本**，特别是**第4节**，以获取所提混合模型的完整架构图、训练细节、超参数设置、数据集预处理以及实验结果代码或链接。
- **如果借鉴创新点**：应深入学习其对CNN、RNN、Transformer技术特点的对比分析，以及**如何构思一个融合不同架构优势的混合模型**。关注其在“背景”中强调的“时空特征提取”与“全局关系建模”这两个核心需求。
- **如果写Related Work**：本文可作为“HAR综述”或“视频理解深度学习架构综述”的关键参考文献。如果自己的工作涉及**CNN-Transformer混合架构**，本文的引言和相关讨论部分是极佳的引用来源。

## 10. 和其他论文的关系
- [[Vision Transformer (ViT) (Dosovitskiy et al., 2020)]]：本文将ViT作为CNN的重要竞争者和潜在替代者进行详细讨论。
- [[AlexNet (Krizhevsky et al., 2012)]]、[[ResNet (He et al., 2016)]]：作为CNN里程碑模型被回顾。
- [[LSTM (Hochreiter and Schmidhuber, 1997)]]、[[GRU (Chung et al., 2014)]]：作为RNN的关键改进模型被深入解析。
- [[Attention Is All You Need (Vaswani et al., 2017)]]：Transformer架构的奠基性工作，本文详细介绍了其自注意力机制。
- [[Two-Stream CNNs (Simonyan and Zisserman, 2014a)]]：作为处理视频时空信息的经典CNN方法被提及。
- 其他可能的HAR数据集论文（如UCF101, Kinetics, Something-Something-V2等），但文中未列出具体数据集名称。

## 11. 关键词
人类动作识别 (Human Action Recognition), 卷积神经网络 (CNN), 循环神经网络 (RNN), Vision Transformer (ViT), 深度学习, 混合模型, 注意力机制, 时空特征, 视频分类, 综述

## 12. 可信度说明
本精读笔记**严格基于提供的PDF文本（论文前12页）生成**。内容主要来源于论文的**摘要、引言（Section 1）以及背景部分（Section 2）**。这些部分对论文的定位、动机、贡献和主要技术回顾（CNN, RNN, Transformer）有清晰阐述。
**提取质量评估**：文本提取质量良好，内容连贯，数学公式和图表描述基本清晰。
**重要限制**：由于提供的文本仅占全文（29页）的前12页，**论文后半部分的关键内容，包括详细的文献综述（第3节）、所提出的混合模型架构与实验（第4节）、挑战与未来方向（第5节）以及结论（第6节），均未包含在提供的材料中**。因此，笔记中涉及模型细节、实验结果和未来趋势的部分，存在信息缺失，已根据前文内容进行了合理推断并明确了限制。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/深度学习架构综述 CNNs RNNs Transformers.txt` (29/29 页; 原 AI 主体 12/29 + 全文补读 13-29); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
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
