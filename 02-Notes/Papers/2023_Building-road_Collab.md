---
title: This article has been accepted for publication in IEEE Transactions on Geoscience and Remote Sensing. This is the author's version which has not been fully edited and
authors:
  - "Haonan Guo"
  - "Chen Wu"
year: 2023
venue: This article has been accepted for publication in IEEE Transactions on Geoscience and Remote Sensing. This is the author's version which has not been fully edited and
doi: 10.1109/TGRS.2024.3383057
pdf: [[2023_Building-road_Collab.pdf]]
primary_topic: C2_目标检测_违建_车辆_船舶_行人
topics:
  - "C2_目标检测_违建_车辆_船舶_行人"
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2023_Building-road_Collab.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# This article has been accepted for publication in IEEE Transactions on Geoscience and Remote Sensing. This is the author's version which has not been fully edited and

## 基本信息
- **PDF**: [[2023_Building-road_Collab.pdf]]
- **primary_topic**: `C2_目标检测_违建_车辆_船舶_行人`
- **topics**: `C2_目标检测_违建_车辆_船舶_行人`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | This article has been accepted for publication in IEEE Transactions on Geoscience and Remote Sensing. This is the author's version which has not been fully edited and |
| **作者** | Haonan Guo; Chen Wu |
| **发表时间** | 2023 |
| **刊物/会议** | This article has been accepted for publication in IEEE Transactions on Geoscience and Remote Sensing. This is the author's version which has not been fully edited and |
| **DOI** | 10.1109/TGRS.2024.3383057 |

## 摘要

> made environments that carry and interconnect human society. multitask learning, deep learning. Building and road information has important application value in B the frontier fields of regional coordinated development, disaster I. INTRODUCTION prevention, auto-driving, etc. Mapping buildings and roads from uildings and roads are the two most basic man-made elements very high-resolution (VHR) remote sensing images has become a of our society. To be specific, buildings are basic carriers for hot research topic. However, the existing methods often extract buildings and roads with separate models, ignoring their strong social production and human life, while roads interconnect spatial correlation. To fully utilize their complementary relation, social network that enables goods and information we propose a method that simultaneously extracts buildings and transportation[1], [2]. The geodata of buildings and roads are roads from remote sensing images. The accuracy of both tasks can valuable

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：建筑物和道路是承载人类社会的基本人造环境，其地理信息对城市规划、自动驾驶、灾害防控等至关重要。利用高分辨率遥感影像自动提取它们已成为研究热点。
- **之前方法的问题**：
    1.  **孤立提取**：主流方法通常为建筑物和道路分别设计和训练独立的模型，忽略了它们之间强烈的空间相关性（如：建筑边界常邻接道路，道路网络贯穿建筑群）。
    2.  **简单多任务的缺陷**：一些现有方法虽然采用统一的网络结构，但仍分别训练（导致计算冗余）；或者简单添加多个分类器进行多任务预测，容易引发“**跷跷板现象**”（seesaw phenomenon），即提升一个任务的性能会损害另一个任务。
    3.  **感受野统一**：建筑物和道路在形态、尺度上差异大，对模型感受野的需求不同，但现有方法通常使用统一的感受野，无法为不同任务优化特征表示。
- **核心矛盾**：如何设计一个单一模型，在实现建筑和道路**协同提取**、利用其**互补性**的同时，**避免任务间的性能冲突**，并**自适应地为不同任务优化特征感受野**。
## 关键贡献

1.  **提出了建筑-道路协同提取网络（CRIN）**：设计了一个单一模型同时输出建筑和道路预测图，通过**多任务交互模块（MTI/MFI）** 在特征层面实现任务间信息交互，利用建筑与道路的互补性提升两者精度，并将推理时间减半。
2.  **设计了多任务特征交互模块（MFI）**：该模块将解码器阶段的特征融合分为**内任务融合**和**跨任务交互**两个阶段。内任务融合分别提炼建筑和道路的特征；跨任务交互则将特征空间分离为**任务特定空间**和**任务共享空间**，在保留任务独特信息的同时促进信息共享，缓解“跷跷板现象”。
3.  **设计了跨尺度交互模块（CSI）**：针对建筑和道路对模型感受野需求不同的问题，该模块能够**自动学习并选择最优的感受野尺度**，为任务特定和任务共享特征空间分别匹配最适合的特征表示。
4.  **广泛的实验验证**：在涵盖广泛城市场景和乡村场景的数据集上进行实验，证明了所提方法在建筑和道路提取任务上均能达到最高精度，并且在效率上优于分开训练的模型。
## 方法

- **整体框架**：论文提出了一个基于编码器-解码器（Encoder-Decoder）架构的**CRoss-Interaction (CRIN) 网络**（Fig. 3）。
- **输入输出**：
    - **输入**：高分辨率（VHR）遥感图像。
    - **输出**：同时预测的建筑掩膜图和道路掩膜图。
- **关键模块与连接**：
    1.  **共享编码器网络**：用于提取输入图像的层级特征。提取的特征会被复制并传递给后续的解码器阶段。
    2.  **多任务特征交互模块（MFI）**：位于解码器的每个阶段，是核心创新之一（Fig. 4）。
        - **输入**：来自上一解码器阶段的深层特征（富含语义但边缘粗糙）和来自编码器对应阶段的浅层特征（富含边缘细节）。
        - **内任务融合阶段**：将输入特征分组、交替拼接，然后通过**组卷积**（Group Convolution, group size=2）分别生成专属于建筑和道路的融合特征。这引导模型为不同任务关注输入特征的不同细节。
        - **跨任务交互阶段**：将融合后的特征投影到三个空间：**建筑特定特征空间**、**道路特定特征空间**和**任务共享特征空间**。任务特定空间用于学习各自任务的最优表示；任务共享空间则允许建筑和道路的特征相互交互，利用其互补性。
    3.  **跨尺度交互模块（CSI）**：位于每个MFI模块之后。其目的是自动为不同任务（任务特定空间和任务共享空间）选择并融合来自不同感受野尺度的特征，以优化特征表示。
- **数学公式/机制直观解释**：论文未提供具体数学公式，但机制可理解为：MFI通过“分治”策略（分离特征空间）和“交互”策略（共享空间交互）来协调多任务学习；CSI则相当于一个自适应的多尺度特征选择器。
- **训练方式**：使用建筑物和道路的标注真值（Ground Truths）作为监督信号，对整个CRIN网络进行端到端优化。
- **推理流程**：单次前向传播即可同时获得建筑和道路的预测结果。
- **与已有方法的差异**：
    - 相比**分开训练的模型**：CRIN共享主干网络，仅需一次推理，计算效率更高（减半）。
    - 相比**简单多任务分类器**：CRIN的MFI模块通过分离任务特定和共享特征空间，有效缓解了“跷跷板现象”，而不是粗暴地共享所有特征。
    - 相比**统一感受野的多任务模型**：CRIN的CSI模块为不同任务动态选择最优感受野，特征表示更优。
## 实验

- **使用的数据集**：PDF文本中提及“a wide range of urban and rural scenarios”，但**未提供具体的公共数据集名称**（如Massachusetts, DeepGlobe等）。数据集详情可能在未提供的后半部分（p.13-17）。
- **对比方法**：PDF文本中提到了与“separate models”、“multitask model”等架构的对比，但**未列出具体的对比算法名称列表**（如FCN, U-Net, DeepLabV3+等）。
- **评价指标**：**PDF文本中未明确说明**具体的评价指标（如IoU, F1, Accuracy等）。
- **主实验结果**：PDF文本中声明“achieves the highest accuracy”，但**未提供具体的定量数值**（如IoU提升多少）。
- **消融实验**：从贡献部分可推断应有对MFI和CSI模块的消融，但**具体结果数字未在提供的文本中**。
- **泛化实验**：提及在“urban and rural scenes”上验证，表明关注泛化性，但**具体跨场景结果未提供**。
- **效率信息**：明确提到提出的单模型方法可将**推理时间减半**（相比分别运行两个独立模型）。参数量、FLOPs等信息**未在提供文本中找到**。
## 局限

1.  **强假设依赖**：方法的有效性依赖于建筑和道路在特征空间确实存在强互补性。在某些场景（如极度密集的棚户区，道路被建筑完全遮挡；或特殊材质的道路与建筑材质相近）中，这种互补性可能减弱，方法优势可能不明显。
2.  **实验完整性未知**：由于提供的PDF文本不完整（仅前12页），无法评估实验部分的完整性，例如是否进行了跨数据集的泛化测试、是否对比了足够多的先进方法。
3.  **计算成本细节缺失**：虽然声称推理时间减半，但未报告模型的参数量、FLOPs等详细效率指标，无法评估其作为多任务模型的轻量化程度。
4.  **泛化能力待全面验证**：文本中仅提及“urban and rural”，但未说明场景多样性的具体程度（如包含不同气候、地貌、城市风格），其泛化能力需通过完整论文的实验部分来判断。
## 个人评论

1.  **思路的普适性**：它展示了一种利用具有强空间相关性的多任务之间**特征互补性**来提升性能的通用思路。这启发我们，在进行遥感地物提取（如建筑-阴影、水体-岸线、车辆-道路）时，不应孤立看待，而应主动设计协同学习机制。
2.  **模块设计的巧妙**：MFI模块中“分组交替拼接+组卷积”进行内任务融合，以及将特征空间显式分为任务特定和共享空间进行交互，是一种简单有效且可解释的多任务特征处理范式，值得借鉴。
3.  **对“跷跷板现象”的明确针对**：论文清晰地定义了问题并提出了针对性解决方案（特征空间分离），这对设计其他多任务学习系统有指导意义。
4.  **自适应感受野的重要性**：CSI模块强调了在多任务学习中，不同任务对特征尺度/感受野的需求可能不同，自适应选择比统一设计更优。

### 使用建议

- **如果快速了解**：重点阅读 **Abstract** 和 **Introduction** 的后半部分（问题提出与贡献），以及 **Fig. 1, Fig. 2, Fig. 3**。这些部分清晰展示了论文的动机、核心思路和整体框架。
- **如果复现**：重点精读 **III. METHODOLOGY** 部分，特别是 **Fig. 3**（整体流程）和 **Fig. 4**（MFI模块细节）的描述。需要关注特征分组、拼接、组卷积的具体实现，以及CSI模块的设计。实验设置部分（应位于未提供的文本中）至关重要。
- **如果借鉴创新点**：应该学习 **MFI模块中任务特定/共享特征空间的设计思想** 以及 **CSI模块的自适应尺度选择机制**。思考如何将这种“交互”思想应用到其他相关的双任务（如语义分割中的“物体”与“边界”提取）中。
- **如果写related work**：可以将本论文放在 **“遥感图像建筑物提取”** 或 **“遥感图像道路提取”** 的 **多任务学习/协同提取** 子类别下进行引用和讨论，作为利用地物间空间关系提升提取性能的代表性工作。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C2_目标检测_违建_车辆_船舶_行人]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**遥感图像理解**领域的**目标提取**方向，具体研究**从高分辨率遥感图像中同时提取建筑物和道路**的方法。它解决的是现有方法将两者孤立提取，未能充分利用其空间相关性，从而导致精度和效率无法最优的问题。根据其技术核心（利用多任务学习和特征交互进行地物提取）和应用对象（建筑物、道路），它非常适合放在用户提供的主题 **“C2_目标检测_违建_车辆_船舶_行人”** 下，作为其中关于建筑物与道路协同检测/分割的代表性工作。

## 2. 一句话总结
本文提出了一种名为CRIN的跨交互网络，通过**多任务特征交互模块**和**跨尺度交互模块**，在单一模型中同时从遥感图像提取建筑物和道路，利用二者在特征空间中的互补关系来提升两项任务的精度与推理效率。

## 3. 背景与问题
- **为什么要做**：建筑物和道路是承载人类社会的基本人造环境，其地理信息对城市规划、自动驾驶、灾害防控等至关重要。利用高分辨率遥感影像自动提取它们已成为研究热点。
- **之前方法的问题**：
    1.  **孤立提取**：主流方法通常为建筑物和道路分别设计和训练独立的模型，忽略了它们之间强烈的空间相关性（如：建筑边界常邻接道路，道路网络贯穿建筑群）。
    2.  **简单多任务的缺陷**：一些现有方法虽然采用统一的网络结构，但仍分别训练（导致计算冗余）；或者简单添加多个分类器进行多任务预测，容易引发“**跷跷板现象**”（seesaw phenomenon），即提升一个任务的性能会损害另一个任务。
    3.  **感受野统一**：建筑物和道路在形态、尺度上差异大，对模型感受野的需求不同，但现有方法通常使用统一的感受野，无法为不同任务优化特征表示。
- **核心矛盾**：如何设计一个单一模型，在实现建筑和道路**协同提取**、利用其**互补性**的同时，**避免任务间的性能冲突**，并**自适应地为不同任务优化特征感受野**。

## 4. 核心贡献
1.  **提出了建筑-道路协同提取网络（CRIN）**：设计了一个单一模型同时输出建筑和道路预测图，通过**多任务交互模块（MTI/MFI）** 在特征层面实现任务间信息交互，利用建筑与道路的互补性提升两者精度，并将推理时间减半。
2.  **设计了多任务特征交互模块（MFI）**：该模块将解码器阶段的特征融合分为**内任务融合**和**跨任务交互**两个阶段。内任务融合分别提炼建筑和道路的特征；跨任务交互则将特征空间分离为**任务特定空间**和**任务共享空间**，在保留任务独特信息的同时促进信息共享，缓解“跷跷板现象”。
3.  **设计了跨尺度交互模块（CSI）**：针对建筑和道路对模型感受野需求不同的问题，该模块能够**自动学习并选择最优的感受野尺度**，为任务特定和任务共享特征空间分别匹配最适合的特征表示。
4.  **广泛的实验验证**：在涵盖广泛城市场景和乡村场景的数据集上进行实验，证明了所提方法在建筑和道路提取任务上均能达到最高精度，并且在效率上优于分开训练的模型。

## 5. 方法详解
- **整体框架**：论文提出了一个基于编码器-解码器（Encoder-Decoder）架构的**CRoss-Interaction (CRIN) 网络**（Fig. 3）。
- **输入输出**：
    - **输入**：高分辨率（VHR）遥感图像。
    - **输出**：同时预测的建筑掩膜图和道路掩膜图。
- **关键模块与连接**：
    1.  **共享编码器网络**：用于提取输入图像的层级特征。提取的特征会被复制并传递给后续的解码器阶段。
    2.  **多任务特征交互模块（MFI）**：位于解码器的每个阶段，是核心创新之一（Fig. 4）。
        - **输入**：来自上一解码器阶段的深层特征（富含语义但边缘粗糙）和来自编码器对应阶段的浅层特征（富含边缘细节）。
        - **内任务融合阶段**：将输入特征分组、交替拼接，然后通过**组卷积**（Group Convolution, group size=2）分别生成专属于建筑和道路的融合特征。这引导模型为不同任务关注输入特征的不同细节。
        - **跨任务交互阶段**：将融合后的特征投影到三个空间：**建筑特定特征空间**、**道路特定特征空间**和**任务共享特征空间**。任务特定空间用于学习各自任务的最优表示；任务共享空间则允许建筑和道路的特征相互交互，利用其互补性。
    3.  **跨尺度交互模块（CSI）**：位于每个MFI模块之后。其目的是自动为不同任务（任务特定空间和任务共享空间）选择并融合来自不同感受野尺度的特征，以优化特征表示。
- **数学公式/机制直观解释**：论文未提供具体数学公式，但机制可理解为：MFI通过“分治”策略（分离特征空间）和“交互”策略（共享空间交互）来协调多任务学习；CSI则相当于一个自适应的多尺度特征选择器。
- **训练方式**：使用建筑物和道路的标注真值（Ground Truths）作为监督信号，对整个CRIN网络进行端到端优化。
- **推理流程**：单次前向传播即可同时获得建筑和道路的预测结果。
- **与已有方法的差异**：
    - 相比**分开训练的模型**：CRIN共享主干网络，仅需一次推理，计算效率更高（减半）。
    - 相比**简单多任务分类器**：CRIN的MFI模块通过分离任务特定和共享特征空间，有效缓解了“跷跷板现象”，而不是粗暴地共享所有特征。
    - 相比**统一感受野的多任务模型**：CRIN的CSI模块为不同任务动态选择最优感受野，特征表示更优。

## 6. 实验与结果
- **使用的数据集**：PDF文本中提及“a wide range of urban and rural scenarios”，但**未提供具体的公共数据集名称**（如Massachusetts, DeepGlobe等）。数据集详情可能在未提供的后半部分（p.13-17）。
- **对比方法**：PDF文本中提到了与“separate models”、“multitask model”等架构的对比，但**未列出具体的对比算法名称列表**（如FCN, U-Net, DeepLabV3+等）。
- **评价指标**：**PDF文本中未明确说明**具体的评价指标（如IoU, F1, Accuracy等）。
- **主实验结果**：PDF文本中声明“achieves the highest accuracy”，但**未提供具体的定量数值**（如IoU提升多少）。
- **消融实验**：从贡献部分可推断应有对MFI和CSI模块的消融，但**具体结果数字未在提供的文本中**。
- **泛化实验**：提及在“urban and rural scenes”上验证，表明关注泛化性，但**具体跨场景结果未提供**。
- **效率信息**：明确提到提出的单模型方法可将**推理时间减半**（相比分别运行两个独立模型）。参数量、FLOPs等信息**未在提供文本中找到**。

## 7. 这篇论文真正有价值的地方
1.  **思路的普适性**：它展示了一种利用具有强空间相关性的多任务之间**特征互补性**来提升性能的通用思路。这启发我们，在进行遥感地物提取（如建筑-阴影、水体-岸线、车辆-道路）时，不应孤立看待，而应主动设计协同学习机制。
2.  **模块设计的巧妙**：MFI模块中“分组交替拼接+组卷积”进行内任务融合，以及将特征空间显式分为任务特定和共享空间进行交互，是一种简单有效且可解释的多任务特征处理范式，值得借鉴。
3.  **对“跷跷板现象”的明确针对**：论文清晰地定义了问题并提出了针对性解决方案（特征空间分离），这对设计其他多任务学习系统有指导意义。
4.  **自适应感受野的重要性**：CSI模块强调了在多任务学习中，不同任务对特征尺度/感受野的需求可能不同，自适应选择比统一设计更优。

## 8. 局限与问题
1.  **强假设依赖**：方法的有效性依赖于建筑和道路在特征空间确实存在强互补性。在某些场景（如极度密集的棚户区，道路被建筑完全遮挡；或特殊材质的道路与建筑材质相近）中，这种互补性可能减弱，方法优势可能不明显。
2.  **实验完整性未知**：由于提供的PDF文本不完整（仅前12页），无法评估实验部分的完整性，例如是否进行了跨数据集的泛化测试、是否对比了足够多的先进方法。
3.  **计算成本细节缺失**：虽然声称推理时间减半，但未报告模型的参数量、FLOPs等详细效率指标，无法评估其作为多任务模型的轻量化程度。
4.  **泛化能力待全面验证**：文本中仅提及“urban and rural”，但未说明场景多样性的具体程度（如包含不同气候、地貌、城市风格），其泛化能力需通过完整论文的实验部分来判断。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读 **Abstract** 和 **Introduction** 的后半部分（问题提出与贡献），以及 **Fig. 1, Fig. 2, Fig. 3**。这些部分清晰展示了论文的动机、核心思路和整体框架。
- **如果复现**：重点精读 **III. METHODOLOGY** 部分，特别是 **Fig. 3**（整体流程）和 **Fig. 4**（MFI模块细节）的描述。需要关注特征分组、拼接、组卷积的具体实现，以及CSI模块的设计。实验设置部分（应位于未提供的文本中）至关重要。
- **如果借鉴创新点**：应该学习 **MFI模块中任务特定/共享特征空间的设计思想** 以及 **CSI模块的自适应尺度选择机制**。思考如何将这种“交互”思想应用到其他相关的双任务（如语义分割中的“物体”与“边界”提取）中。
- **如果写related work**：可以将本论文放在 **“遥感图像建筑物提取”** 或 **“遥感图像道路提取”** 的 **多任务学习/协同提取** 子类别下进行引用和讨论，作为利用地物间空间关系提升提取性能的代表性工作。

## 10. 和其他论文的关系
基于给定的主题“C2_目标检测_违建_车辆_船舶_行人”，本论文的核心“建筑与道路协同提取”与之相关。可能相关的论文方向包括：
- 其他采用多任务学习进行遥感地物提取的工作。
- 专注于建筑物单类提取的先进模型（如使用Transformer或新型注意力机制的方法）。
- 专注于道路单类提取的先进模型（如关注道路连通性、拓扑关系的方法）。
由于具体论文库未知，**无法确定具体论文**，故不在此使用`[[双链]]`写法。

## 11. 关键词
建筑物提取, 道路分割, 多任务学习, 深度学习, 遥感图像理解, 特征交互, 跨尺度特征, 编码器-解码器网络, 高分辨率遥感, 空间相关性

## 12. 可信度说明
本精读笔记主要基于提供的PDF文本**前12页**内容生成，该部分完整包含了论文的**标题、摘要、引言、相关工作、方法概述及MFI模块的详细描述**。提取文本质量良好，结构清晰。主要局限性在于：**实验部分（包括数据集、对比方法、具体结果、消融实验等）几乎完全缺失**（应位于第13-17页），因此笔记中关于实验结果的陈述多为定性描述或基于论文声明，缺乏定量数据支撑。其他部分（如动机、方法）的描述是忠实于原文的。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2023_Building-road_Collab.txt` (17/17 页; 原 AI 主体 12/17 + 全文补读 13-17); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Massachusetts dataset is approximately 3 ti mes lower than the
- p.13: AIOI dataset, we suppose that the optimal reception field of
- p.13: Although our proposed method achieves better accuracy than
- p.13: The ground truth labels are usua lly not strictly aligned with the
- p.13: Explor ing noisy label learning to achieve more robust building -
- p.13: Moreover, generating fine-grained and up -to-date building and
- p.13: Buildings are the basic carrier of social production and
- p.13: The geodata of buildings and roads are valuable for various
- p.13: Furthermore, a cross -scale interaction module is proposed to
- p.13: REFERENCES
- p.13: Aligned Representations With Multimodel Transformers
- p.13: Networks (CNNs) for fused airborne lidar and image data

### 缺失页关键摘录

- p.13: dataset. Considering that the spatial resolution of the
- p.13: Massachusetts dataset is approximately 3 ti mes lower than the
- p.13: AIOI dataset, we suppose that the optimal reception field of
- p.13: Although our proposed method achieves better accuracy than
- p.13: limitation s and can be further improved from the following
- p.13: the “seesaw phenomenon” where the accuracy of one task is
- p.13: recognition accuracy through the proposed cross -task and
- p.13: accuracy, showing great pot ential in large -scale mapping.
- p.16: dataset for building and road detection, and building
<!-- AI_READING_NOTE_END -->
