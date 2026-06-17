---
title: "DGMA -Net: A Difference-Guided Multiscale"
authors:
  - "Zilu Ying"
  - "Zijun Tan"
  - "Yikui Zhai"
  - "Xudong Jia"
  - "Wenba Li"
  - "Junying Zeng"
  - "Angelo Genovese"
  - "Vincenzo Piuri"
  - "Fabio Scotti"
year: 2024
venue: "IEEE TGRS"
doi: 10.1109/TGRS.2024.3390206
pdf: [[MDFM.pdf]]
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
extract_cache: .paper-cache/extracts/MDFM.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/16 pages"
---
# DGMA -Net: A Difference-Guided Multiscale

## 基本信息
- **PDF**: [[MDFM.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | DGMA -Net: A Difference-Guided Multiscale |
| **作者** | Zilu Ying; Zijun Tan; Yikui Zhai; Xudong Jia; Wenba Li; Junying Zeng; Angelo Genovese; Vincenzo Piuri; Fabio Scotti |
| **发表时间** | 2024 |
| **刊物/会议** | IEEE TGRS |
| **DOI** | 10.1109/TGRS.2024.3390206 |

## 摘要

> —Remote sensing change detection (RSCD) focuses DGMA2-Net, a series of experiments are conducted on three onidentifyingregionsthathaveundergonechangesbetweentwo publicRSCDbenchmarkdatasets[LEVIRbuildingchangedetec- remote sensing images captured at different times. Recently, tion dataset (LEVIR-CD), Wuhan University building change convolutional neural networks (CNNs) have shown promising detection dataset (BCDD), and Sun Yat-Sen University dataset resultsinthechallengingtaskofRSCD.However,thesemethods (SYSU-CD)].TheexperimentalresultsdemonstratethatDGMA2- do not efficiently fuse bitemporal features and extract useful Netsurpassesthecurrenteightstate-of-the-artmethodsinRSCD. informationthatisbeneficialtosubsequentRSCDtasks.Inaddi- Ourcodeisreleasedathttps://github.com/yikuizhai/DGMA2-Net. tion, they did not consider multilevel feature interactions in

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么做**：遥感变化检测在灾害评估、环境监测等领域至关重要。尽管CNN方法已超越传统方法，但在特征融合和聚合环节仍存在瓶颈，导致检测结果不够理想。
- **之前方法的问题**：
    1.  **特征融合不高效**：现有方法多采用简单的特征拼接或减法操作进行双时相特征融合，融合操作局限于局部交互，且很少利用多尺度特征学习机制，导致融合后的特征包含较多噪声。
    2.  **特征聚合不充分**：广泛使用的U-Net结构通过跳跃连接聚合多层特征，但缺乏**多层级特征间的有效交互**。此外，现有方法忽略了**差异特征与双时相特征之间关系**的挖掘。
- **核心矛盾**：如何设计一个网络，既能进行**多尺度的双时相特征融合**以生成高质量的差异特征，又能实现**跨层级的特征有效交互与聚合**，并强化变化区域的表征。
## 关键贡献

1.  **提出多尺度差异融合模块(MDFM)**：这是论文最主要的贡献之一。MDFM首次将多尺度特征学习机制应用于双时相特征融合，通过不同尺寸卷积核的并行分支提取多尺度上下文，并利用通道权重进行融合，旨在生成噪声更少、信息更丰富的差异特征。
2.  **提出差异聚合模块(DAM)**：区别于仅关注特征内部交互的现有方法，DAM旨在探索**多层级特征之间的交互**。它通过上采样和下采样操作，将深层特征与浅层特征进行聚合，实现不同深度语义信息的充分利用。
3.  **提出差异增强注意力模块(DEAM)**：论文指出DEAM是首个基于自注意力机制研究**差异特征与双时相特征交互**的模块，旨在进一步增强变化区域并精炼差异特征。
4.  **构建完整的DGMA2-Net**：将上述三个模块（MDFM, DAM, DEAM）集成到一个编码器-解码器框架中，形成一个新的遥感变化检测网络。在三个公开数据集上的实验验证了其优越性。
## 方法

- **整体框架**：DGMA2-Net采用编码器-解码器架构（如图2所示）。编码器使用**预训练的权重共享ResNet-18**提取双时相图像的多层级特征，随后通过MDFM进行融合。融合后的差异特征经过DAM进行层级聚合，再经过DEAM进行增强，最终在解码器中从深层到浅层叠加特征并生成变化图。
- **输入输出**：输入是一对配准好的、同步获取的遥感图像（T1和T2）。输出是一个二值变化图。
- **关键模块详解**：
    1.  **多尺度差异融合模块 (MDFM)**：(p.3, Fig.3, Fig.4)
        - **作用**：融合双时相特征，生成多尺度的差异特征。
        - **机制**：首先，对来自ResNet-18同一阶段的双时相特征`F1_i`和`F2_i`做像素级减法、取绝对值，再经过3x3卷积，得到**初始差异特征**`Di`：`Di = Conv3×3(|F1_i - F2_i|)`。
        - **核心**：引入**多尺度特征融合(MSFF)单元**。该单元包含四个并行分支：三个分别使用[1x1, 3x3, 1x1]、[1x1, 5x5, 1x1]、[1x1, 7x7, 1x1]的卷积组合，以及一个仅使用1x1卷积的分支。它们分别处理特征，然后拼接，得到多尺度特征`Mi`。
        - **融合**：计算一个**元素级通道权重**`Wi = Fi × σ(Conv3×3(Di))`，该权重利用了差异信息`Di`来调制原始特征`Fi`。然后，将`Wi`与多尺度特征`Mi`相加，得到融合特征`Si = Wi + Mi`。
        - **最终输出**：使用**通道卷积块(CWCB)**（Fig.5），将双时相的`S1_i`和`S2_i`在通道维度拼接，进行深度可分离卷积，再与权重`Wi`相乘，最后通过3x3卷积得到**最终融合的差异特征**`Ci`。
    2.  **差异聚合模块 (DAM)**：(p.4, Fig.6, Fig.7)
        - **作用**：聚合不同层级的差异特征，进行多层级特征交互。
        - **机制**：包含**上采样模块(UM)**和**下采样模块(DM)**。
        - **上采样聚合**：将深层特征上采样至与浅层特征相同尺寸，经过3x3卷积后，与浅层特征拼接，再通过3x3卷积，完成**深层到浅层的信息融合**：`A_{i-1} = Conv3×3(Cat(shallow, Conv3×3(UP(deep))))`。
        - **下采样精炼**：最深层的聚合特征`A1`需要被恢复到与`Ci`相同的尺寸。通过平均池化进行下采样，并配合卷积操作，得到最终送入解码器的精炼特征`Qi`。
- **模块连接方式**：ResNet-18的四个阶段输出分别进入对应的MDFM，生成C1-C4。DAM按照从深到浅的顺序聚合特征（如C4与C3聚合，再与C2聚合，最后与C1聚合）。聚合后的特征Q1-Q4（尺寸与C1-C4对应）与原始的双时相特征一同送入DEAM（文本中未详细描述DEAM内部结构），最后进行上采样和叠加。
- **训练与推理**：PDF文本中未明确说明具体的损失函数、优化器等训练细节和详细的推理流程。
- **与已有方法的差异**：核心差异在于引入了**多尺度机制**进行特征融合（MDFM），并设计了**显式的多层级交互**聚合模块（DAM），同时试图通过DEAM建模差异特征与双时相特征的关系，这比简单的拼接、减法和基于固定U-Net的跳跃连接更为精细。
## 实验

- **使用的数据集**：论文提到了三个公开的RSCD基准数据集：
    1.  LEVIR建筑变化检测数据集 (LEVIR-CD)
    2.  武汉大学建筑变化检测数据集 (BCDD)
    3.  中山大学数据集 (SYSU-CD)
- **对比方法**：论文声称超越了“当前八种state-of-the-art方法”，但**提供的PDF文本中未列出具体的对比方法名称**。
- **评价指标**：PDF文本中未明确说明。
- **主实验结果**：**在提供的PDF文本中未出现具体的性能数字（如F1值、IoU等）**。摘要和结论仅定性描述为“demonstrates that DGMA2-Net surpasses the current eight state-of-the-art methods”。
- **消融实验**：PDF文本中未找到对MDFM、DAM、DEAM等模块的消融实验分析。
- **泛化实验**：PDF文本中未找到。
- **效率信息**：PDF文本中未提供速度、参数量、FLOPs等数据。
## 局限

- **场景限制**：模型主要针对建筑物变化检测任务设计，在其他类型（如自然植被、道路）的变化检测效果未在文中验证。
- **实验不充分**：基于提供的文本，缺少详细的消融实验来验证每个新模块（MDFM, DAM, DEAM）的独立贡献。同时，缺乏与更多前沿方法（特别是基于Transformer的方法）的对比。
- **计算成本未知**：引入的MSFF单元（多个并行分支）和DAM模块可能会增加模型的计算复杂度和参数量，但文中未讨论效率问题。
- **假设依赖**：性能在一定程度上依赖于骨干网络（ResNet-18）提取的特征质量。
- **复现风险**：DEAM的具体结构在提供的文本中缺失，完全复现该模型存在困难。论文的代码开源部分缓解了此问题。
## 个人评论

这篇论文最值得学习的地方在于其**模块化的设计思想和问题导向的解决方案**。
1.  **对“多尺度”的创造性应用**：它没有简单地在骨干网络后添加多尺度模块，而是将多尺度特征学习机制（MSFF）直接**嵌入到双时相特征融合的过程中**（MDFM），从源头上提升差异特征的丰富性，这是一个很好的创新思路。
2.  **强调“层级交互”**：在特征聚合阶段，它明确指出并设计了DAM来促进多层级特征之间的交互，而不仅仅是浅层对高层的单向补充。这种设计能更好地融合上下文语义信息。
3.  **启发**：对于后续研究，可以借鉴其“差异引导”和“多尺度融合”的思想，应用到其他图像融合或变化检测任务中。DAM的上采样-下采样聚合结构也提供了一种比简单跳跃连接更复杂的跨层交互范式。

### 使用建议

- **快速了解**：阅读**摘要 (Abstract)** 和**引言 (I. INTRODUCTION)** 部分，可以快速掌握论文要解决的问题、核心思路和主要贡献。
- **复现**：重点精读**方法部分 (III. METHOD)**，尤其是图2（整体架构）、图3和图4（MDFM及MSFF结构）、图5（CWCB）、图6和图7（DAM结构）以及相关的公式(1)-(7)。但需注意，要完整复现必须参考作者开源的代码。
- **借鉴创新点**：
    - 借鉴**MDFM的多尺度融合思路**，可思考如何将其应用到其他需要特征融合的任务中。
    - 借鉴**DAM的跨层级交互设计**，可以改进自己模型中的特征聚合部分，而不仅限于U-Net。
- **写Related Work**：可放在“基于深度学习的变化检测方法”下的“**特征融合与聚合策略**”小节，作为介绍**利用多尺度机制和注意力进行特征交互**的代表工作之一。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**遥感变化检测**领域，专注于解决基于深度学习的方法在特征融合和聚合方面存在的不足。它适合放在**注意力算子模块**这个主题下，因为论文的核心创新点是设计了三个新颖的注意力相关模块（MDFM, DAM, DEAM）来增强特征表达和交互。该研究旨在提升复杂场景下建筑物等目标的变化检测精度。

## 2. 一句话总结
这篇论文提出了一种名为DGMA2-Net的差异引导多尺度聚合注意力网络，通过创新的多尺度特征融合模块和层级聚合注意力模块，更有效地融合双时相特征并提取丰富的上下文信息，从而提升遥感变化检测的性能。

## 3. 背景与问题
- **为什么做**：遥感变化检测在灾害评估、环境监测等领域至关重要。尽管CNN方法已超越传统方法，但在特征融合和聚合环节仍存在瓶颈，导致检测结果不够理想。
- **之前方法的问题**：
    1.  **特征融合不高效**：现有方法多采用简单的特征拼接或减法操作进行双时相特征融合，融合操作局限于局部交互，且很少利用多尺度特征学习机制，导致融合后的特征包含较多噪声。
    2.  **特征聚合不充分**：广泛使用的U-Net结构通过跳跃连接聚合多层特征，但缺乏**多层级特征间的有效交互**。此外，现有方法忽略了**差异特征与双时相特征之间关系**的挖掘。
- **核心矛盾**：如何设计一个网络，既能进行**多尺度的双时相特征融合**以生成高质量的差异特征，又能实现**跨层级的特征有效交互与聚合**，并强化变化区域的表征。

## 4. 核心贡献
1.  **提出多尺度差异融合模块(MDFM)**：这是论文最主要的贡献之一。MDFM首次将多尺度特征学习机制应用于双时相特征融合，通过不同尺寸卷积核的并行分支提取多尺度上下文，并利用通道权重进行融合，旨在生成噪声更少、信息更丰富的差异特征。
2.  **提出差异聚合模块(DAM)**：区别于仅关注特征内部交互的现有方法，DAM旨在探索**多层级特征之间的交互**。它通过上采样和下采样操作，将深层特征与浅层特征进行聚合，实现不同深度语义信息的充分利用。
3.  **提出差异增强注意力模块(DEAM)**：论文指出DEAM是首个基于自注意力机制研究**差异特征与双时相特征交互**的模块，旨在进一步增强变化区域并精炼差异特征。
4.  **构建完整的DGMA2-Net**：将上述三个模块（MDFM, DAM, DEAM）集成到一个编码器-解码器框架中，形成一个新的遥感变化检测网络。在三个公开数据集上的实验验证了其优越性。

## 5. 方法详解
- **整体框架**：DGMA2-Net采用编码器-解码器架构（如图2所示）。编码器使用**预训练的权重共享ResNet-18**提取双时相图像的多层级特征，随后通过MDFM进行融合。融合后的差异特征经过DAM进行层级聚合，再经过DEAM进行增强，最终在解码器中从深层到浅层叠加特征并生成变化图。
- **输入输出**：输入是一对配准好的、同步获取的遥感图像（T1和T2）。输出是一个二值变化图。
- **关键模块详解**：
    1.  **多尺度差异融合模块 (MDFM)**：(p.3, Fig.3, Fig.4)
        - **作用**：融合双时相特征，生成多尺度的差异特征。
        - **机制**：首先，对来自ResNet-18同一阶段的双时相特征`F1_i`和`F2_i`做像素级减法、取绝对值，再经过3x3卷积，得到**初始差异特征**`Di`：`Di = Conv3×3(|F1_i - F2_i|)`。
        - **核心**：引入**多尺度特征融合(MSFF)单元**。该单元包含四个并行分支：三个分别使用[1x1, 3x3, 1x1]、[1x1, 5x5, 1x1]、[1x1, 7x7, 1x1]的卷积组合，以及一个仅使用1x1卷积的分支。它们分别处理特征，然后拼接，得到多尺度特征`Mi`。
        - **融合**：计算一个**元素级通道权重**`Wi = Fi × σ(Conv3×3(Di))`，该权重利用了差异信息`Di`来调制原始特征`Fi`。然后，将`Wi`与多尺度特征`Mi`相加，得到融合特征`Si = Wi + Mi`。
        - **最终输出**：使用**通道卷积块(CWCB)**（Fig.5），将双时相的`S1_i`和`S2_i`在通道维度拼接，进行深度可分离卷积，再与权重`Wi`相乘，最后通过3x3卷积得到**最终融合的差异特征**`Ci`。
    2.  **差异聚合模块 (DAM)**：(p.4, Fig.6, Fig.7)
        - **作用**：聚合不同层级的差异特征，进行多层级特征交互。
        - **机制**：包含**上采样模块(UM)**和**下采样模块(DM)**。
        - **上采样聚合**：将深层特征上采样至与浅层特征相同尺寸，经过3x3卷积后，与浅层特征拼接，再通过3x3卷积，完成**深层到浅层的信息融合**：`A_{i-1} = Conv3×3(Cat(shallow, Conv3×3(UP(deep))))`。
        - **下采样精炼**：最深层的聚合特征`A1`需要被恢复到与`Ci`相同的尺寸。通过平均池化进行下采样，并配合卷积操作，得到最终送入解码器的精炼特征`Qi`。
- **模块连接方式**：ResNet-18的四个阶段输出分别进入对应的MDFM，生成C1-C4。DAM按照从深到浅的顺序聚合特征（如C4与C3聚合，再与C2聚合，最后与C1聚合）。聚合后的特征Q1-Q4（尺寸与C1-C4对应）与原始的双时相特征一同送入DEAM（文本中未详细描述DEAM内部结构），最后进行上采样和叠加。
- **训练与推理**：PDF文本中未明确说明具体的损失函数、优化器等训练细节和详细的推理流程。
- **与已有方法的差异**：核心差异在于引入了**多尺度机制**进行特征融合（MDFM），并设计了**显式的多层级交互**聚合模块（DAM），同时试图通过DEAM建模差异特征与双时相特征的关系，这比简单的拼接、减法和基于固定U-Net的跳跃连接更为精细。

## 6. 实验与结果
- **使用的数据集**：论文提到了三个公开的RSCD基准数据集：
    1.  LEVIR建筑变化检测数据集 (LEVIR-CD)
    2.  武汉大学建筑变化检测数据集 (BCDD)
    3.  中山大学数据集 (SYSU-CD)
- **对比方法**：论文声称超越了“当前八种state-of-the-art方法”，但**提供的PDF文本中未列出具体的对比方法名称**。
- **评价指标**：PDF文本中未明确说明。
- **主实验结果**：**在提供的PDF文本中未出现具体的性能数字（如F1值、IoU等）**。摘要和结论仅定性描述为“demonstrates that DGMA2-Net surpasses the current eight state-of-the-art methods”。
- **消融实验**：PDF文本中未找到对MDFM、DAM、DEAM等模块的消融实验分析。
- **泛化实验**：PDF文本中未找到。
- **效率信息**：PDF文本中未提供速度、参数量、FLOPs等数据。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的地方在于其**模块化的设计思想和问题导向的解决方案**。
1.  **对“多尺度”的创造性应用**：它没有简单地在骨干网络后添加多尺度模块，而是将多尺度特征学习机制（MSFF）直接**嵌入到双时相特征融合的过程中**（MDFM），从源头上提升差异特征的丰富性，这是一个很好的创新思路。
2.  **强调“层级交互”**：在特征聚合阶段，它明确指出并设计了DAM来促进多层级特征之间的交互，而不仅仅是浅层对高层的单向补充。这种设计能更好地融合上下文语义信息。
3.  **启发**：对于后续研究，可以借鉴其“差异引导”和“多尺度融合”的思想，应用到其他图像融合或变化检测任务中。DAM的上采样-下采样聚合结构也提供了一种比简单跳跃连接更复杂的跨层交互范式。

## 8. 局限与问题
- **场景限制**：模型主要针对建筑物变化检测任务设计，在其他类型（如自然植被、道路）的变化检测效果未在文中验证。
- **实验不充分**：基于提供的文本，缺少详细的消融实验来验证每个新模块（MDFM, DAM, DEAM）的独立贡献。同时，缺乏与更多前沿方法（特别是基于Transformer的方法）的对比。
- **计算成本未知**：引入的MSFF单元（多个并行分支）和DAM模块可能会增加模型的计算复杂度和参数量，但文中未讨论效率问题。
- **假设依赖**：性能在一定程度上依赖于骨干网络（ResNet-18）提取的特征质量。
- **复现风险**：DEAM的具体结构在提供的文本中缺失，完全复现该模型存在困难。论文的代码开源部分缓解了此问题。

## 9. 我该怎么使用这篇论文
- **快速了解**：阅读**摘要 (Abstract)** 和**引言 (I. INTRODUCTION)** 部分，可以快速掌握论文要解决的问题、核心思路和主要贡献。
- **复现**：重点精读**方法部分 (III. METHOD)**，尤其是图2（整体架构）、图3和图4（MDFM及MSFF结构）、图5（CWCB）、图6和图7（DAM结构）以及相关的公式(1)-(7)。但需注意，要完整复现必须参考作者开源的代码。
- **借鉴创新点**：
    - 借鉴**MDFM的多尺度融合思路**，可思考如何将其应用到其他需要特征融合的任务中。
    - 借鉴**DAM的跨层级交互设计**，可以改进自己模型中的特征聚合部分，而不仅限于U-Net。
- **写Related Work**：可放在“基于深度学习的变化检测方法”下的“**特征融合与聚合策略**”小节，作为介绍**利用多尺度机制和注意力进行特征交互**的代表工作之一。

## 10. 和其他论文的关系
由于提供的知识库主题为“B_注意力算子模块”，这篇论文与以下方向的研究可能高度相关：
-  [[基于U-Net的特征聚合方法]]：本文的DAM可视为对U-Net跳跃连接的一种增强和替代。
-  [[自注意力机制在图像任务中的应用]]：本文的DEAM属于自注意力机制的一种变体，旨在处理特定的双流特征交互。
-  [[多尺度特征学习]]：本文的MDFM是多尺度特征学习在双时相融合中的一个具体应用案例。
*注：因知识库内具体论文未知，以上为根据主题推测的可能关联方向。*

## 11. 关键词
- Remote Sensing Change Detection (遥感变化检测)
- Siamese Network (孪生网络)
- Multiscale Fusion (多尺度融合)
- Feature Aggregation (特征聚合)
- Attention Mechanism (注意力机制)
- Difference Feature (差异特征)
- Bitemporal Image (双时相图像)
- Encoder-Decoder (编码器-解码器)

## 12. 可信度说明
本精读笔记主要基于提供的PDF文本的**前12页内容**生成，该部分完整包含了**摘要、引言、相关工作、以及方法部分（包括MDFM和DAM的详细描述）**。提取质量良好，关键模块的结构、公式和动机描述清晰。
**然而，笔记中“实验与结果”部分显得空泛**，这是因为提供的文本片段中**未包含实验结果的详细数据和分析**。结论中提到的“超越八种SOTA方法”等论断缺乏具体数据支撑。此外，**DEAM（差异增强注意力模块）的具体结构在提供的文本中未描述**，仅出现其名称和作用。因此，对于该模块的原理，本笔记无法给出详解。如需全面评估论文的实验说服力和方法完整性，需参考后续包含实验和DEAM结构的页面。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/MDFM.txt` (16/16 页; 原 AI 主体 12/16 + 全文补读 13-16); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-16; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-16。
- **提取情况**: 缺失页 4 页, 其中 4 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: TABLE V
- p.13: THEBESTVALUES ARE IN BOLD
- p.13: TABLE VI
- p.13: O/W R EPRESENTS THE DGMA2-NETWITHOUT /WITHDEAM
- p.13: TABLE VII
- p.13: QUANTITATIVE ANALYSIS OF MODELS ON PARAMS , FLOPS ,AS WELL AS
- p.13: For example, FPS dropped from 35 to 22, and the training
- p.13: DAM consume more computing resources, and lightweight
- p.13: In this work, a difference-guided multiscale multilevel
- p.13: DGMA2-Net comprises three main components: MDFM,
- p.13: The MDFM is proven to be a new approach in fusing seman-
- p.13: In addition, the DAMs are instrumental in effectively aggre-

### 缺失页关键摘录

- p.13: ABLATION EXPERIMENT ON DEAM. T HEBEST VALUES ARE IN BOLD.
- p.13: QUANTITATIVE ANALYSIS OF MODELS ON PARAMS , FLOPS ,AS WELL AS
- p.13: table that without MDFM, the model’s Params, Flops, training
- p.13: ablation tests provide results that indicate that the MDFM,
- p.14: dataset for remote sensing change detection,” IEEE Trans. Geosci.
- p.14: new dataset for remote sensing image change detection,” Remote Sens.,
- p.14: and a dataset for remote sensing building change detection,” IEEE Trans.
<!-- AI_READING_NOTE_END -->
