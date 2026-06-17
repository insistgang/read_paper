---
title: et al. [full author details at the end of the article]
authors:
  - "Kun Wang"
  - "Zi Wang"
  - "Zhang Li"
  - "Ang Su"
  - "Xichao Teng"
  - "Erting Pan"
  - "Minhao Liu"
  - "Qifeng Yu"
year: 2023
venue: Oriented object detection in optical remote sensing images
doi: 10.1007/s10462-025-11256-0
pdf: [[2023_Oriented_object_dete.pdf]]
primary_topic: C_目标检测_通用与旋转框
topics:
  - "C_目标检测_通用与旋转框"
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
extract_cache: .paper-cache/extracts/2023_Oriented_object_dete.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/61 pages"
---
# et al. [full author details at the end of the article]

## 基本信息
- **PDF**: [[2023_Oriented_object_dete.pdf]]
- **primary_topic**: `C_目标检测_通用与旋转框`
- **topics**: `C_目标检测_通用与旋转框`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | et al. [full author details at the end of the article] |
| **作者** | Kun Wang; Zi Wang; Zhang Li; Ang Su; Xichao Teng; Erting Pan; Minhao Liu; Qifeng Yu |
| **发表时间** | 2023 |
| **刊物/会议** | Oriented object detection in optical remote sensing images |
| **DOI** | 10.1007/s10462-025-11256-0 |

## 摘要

> Oriented object detection is a fundamental yet challenging task in remote sensing (RS), aiming to locate and classify objects with arbitrary orientations. Recent advancements in deep learning have significantly enhanced the capabilities of oriented object detection methods. Given the rapid development of this field, a comprehensive survey of the recent advances in oriented object detection is presented in this paper. Specifically, we begin by tracing the technical evolution from horizontal object detection to oriented object de- tection and highlighting the specific related challenges, including feature misalignment, spatial misalignment, oriented bounding box (OBB) regression problems, and common issues encountered in RS. Subsequently, we further categorize the existing methods into detection frameworks, OBB regression techniques, feature representation approaches, and solutions to common issues and provide an in-depth discussion of how these methods ad- dress the above challenges. In

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：随着遥感技术发展，光学卫星和无人机获取的图像数量激增，需要自动化分析技术。定向目标检测是其中的关键基础任务，因为遥感图像通常采用鸟瞰视角拍摄，图像中的物体（如车辆、船舶、建筑物）往往具有任意方向，使用水平边界框（HBB）进行检测效果不佳，容易造成漏检和定位不精确。
- **之前方法的问题**：
    1.  **水平框检测的局限性**：直接将用于自然场景的水平目标检测器应用于遥感图像会导致：（1）在密集场景或大长宽比物体中，水平框之间的IoU可能非常大，导致非极大值抑制（NMS）后漏检；（2）水平框会包含大量背景区域，定位精度低（p.6）。
    2.  **定向检测的特定挑战**：在改造水平检测器以预测旋转框时，会面临额外的挑战：（1）**特征错位**：轴对齐的卷积提取的特征与旋转物体之间存在错位；（2）**空间错位**：基于水平锚点的检测器与旋转物体的IoU计算困难，导致标签分配困难；（3）**旋转框回归问题**：常用的角度表示（θ-based）存在角度周期性问题，四边形表示存在顶点排序问题，都会导致训练不稳定（p.7-8）。
- **核心矛盾**：如何有效解决定向目标检测中引入的**特征错位、空间错位和旋转框回归难题**，同时克服遥感图像本身固有的**尺度变化、复杂背景和弱特征响应**等挑战。
## 关键贡献

基于提供的文本，本文的主要贡献可归纳为四点：
1.  **系统性地回顾了从水平目标检测到定向目标检测的技术演进**，并首次将定向目标检测面临的主要挑战明确归纳为四个方面：特征错位、空间错位、旋转框回归问题以及遥感场景中的常见问题（p.5, 1.3节）。
2.  **提出了一个更全面、细致的定向目标检测方法分类体系（Taxonomy）**。该体系将现有方法从四个维度进行组织：检测框架（如两阶段、单阶段、无锚点、DETR）、旋转框回归技术、特征表示方法、以及针对遥感常见问题的解决方案（p.5, p.9图5）。
3.  **提供了对当前最先进（SOTA）方法在典型数据集上的全面比较和深入分析**，包括对这些方法优缺点的评估，旨在为研究者选择和改进方法提供有价值的见解（p.5）。
4.  **系统性地审视了开放性问题并展望了未来研究方向**，包括轻量化方法、场景特定数据集、多模态数据集、大规模数据集以及多模态大模型等（p.5）。
## 方法

**重要说明**：本文本身是一篇综述论文，**并未提出一种全新的检测方法或框架**。其“方法”核心在于**对现有方法的系统性分类、分析和总结**。
- **整体结构**：论文按照“提出挑战 -> 分类解决挑战的方法”的逻辑展开。图5展示了其结构化分类体系。
- **分类体系详解**：
    1.  **检测框架**：根据处理流程，将定向检测器分为四类。
        - **两阶段方法**：首先生成可能包含物体的旋转候选区域（Region Proposals），然后对这些区域进行分类和精修。其设计思想是“粗到精”，以解决特征错位和空间错位问题（p.8, 3.1节）。
        - **单阶段方法**：直接在特征图上进行密集预测，效率更高。通过设计旋转锚点或改进标签分配策略来解决空间错位问题（p.8）。
        - **无锚点方法**：完全抛弃锚点机制，直接预测物体的中心点、尺寸和角度，从而从根本上避免了与锚点相关的空间错位问题（p.8, 3.3节）。
        - **DETR类方法**：将检测视为集合预测问题，利用Transformer的全局注意力机制和端到端训练，去除了NMS和锚点等手工组件，为定向检测提供了新范式（p.8）。
    2.  **旋转框回归技术**：专注于解决旋转框参数化带来的训练难题。
        - **损失函数设计**：通过设计新的损失函数来缓解角度周期性问题或顶点排序问题。
        - **旋转框表示方法**：探索超越简单(θ-based)和四边形之外的新的旋转框参数化方式（p.8, 4节）。
    3.  **特征表示方法**：致力于提取更具旋转不变性或更适合检测旋转物体的特征。
        - **旋转不变特征表示**：通过设计特定的网络模块或变换操作，使提取的特征对物体的旋转不敏感（p.8, 5.1节）。
        - **高级特征表示**：利用注意力机制、特征金字塔网络（FPN）等先进模块，增强特征对多尺度、复杂背景和弱纹理目标的表达能力（p.8, 5.2节）。
    4.  **针对遥感常见问题的解决方案**：处理遥感图像特有的挑战，如尺度变化、复杂背景和弱纹理目标等（p.8, 6节）。
- **与已有方法的差异**：与之前的综述（如Wen et al. 2023, Zhang et al. 2023）相比，本文提供了更深入、更全面的分析，其分类体系（特别是将挑战与解决方案明确对应）被认为更系统、更优（p.4）。
## 实验

作为一篇综述，本文**没有提出新方法并进行实验**。但是，它提供了以下与实验相关的综合信息：
- **使用的数据集**：论文在第7节概述了该领域常用的公开数据集（p.5）。但由于提供的文本未包含第7-8节内容，**具体数据集列表和评估指标（如mAP、角度IoU等）在提供的文本中未明确列出**。
- **对比方法与主实验结果**：论文声称在第8节对最先进方法进行了全面比较和分析（p.5）。然而，**由于提供的文本仅包含前12页（至第9页），第8节的具体对比表格、方法列表和关键性能数字在提供的文本中未找到**。
- **消融/泛化实验及效率信息**：这些通常出现在具体方法论文中，作为综述，本文会汇总相关方法的实验发现，但同样，**这些具体信息在提供的文本片段中未出现**。
## 局限

1.  **领域聚焦**：本文明确关注于**光学遥感图像**中的定向目标检测。其结论和分类体系是否完全适用于其他场景（如SAR图像、无人机视频、自然场景文本检测）中的旋转目标检测，需要读者自行判断。
2.  **时效性**：综述论文的发表总会滞后于最新研究进展。本文接受日期为2025年5月，但鉴于该领域发展迅速，2024-2025年出现的最新突破（如基于基础模型的新方法）可能未被涵盖。
3.  **深度的权衡**：尽管声称比前人综述更深入，但面对海量文献，任何综述都不得不在广度与深度之间做出权衡。对于具体某一篇被引用的方法，其核心细节仍需阅读原文。
4.  **主观性**：分类体系的选择、重要论文的筛选、优缺点的分析都不可避免地带有作者的视角和判断。
## 个人评论

这篇综述的最大价值在于其**系统性梳理和结构化思考**。对于研究者，它的启发在于：
1.  **清晰的问题定义**：它将定向检测的挑战明确定义为四个维度，这为研究者理解问题、定位研究空白提供了清晰的路线图。
2.  **方法论地图**：其提出的四维分类体系（框架、回归、特征、常见问题）就像一张“方法论地图”，可以帮助研究者快速理解现有技术树，判断自己研究（无论是改进现有方法还是提出新方法）在领域中的位置。
3.  **研究起点**：通过本文的文献综述和分类，可以高效地找到该子领域的关键论文和代表性工作，是进入该领域研究的极佳入口。
4.  **批判性视角**：文中对各种方法优缺点的分析，以及对未来方向的展望，有助于激发新的研究思路。

### 使用建议

- **快速了解领域**：重点阅读 **Abstract, 第1节（引言），第2节（从水平检测到定向检测的挑战），以及图5（分类体系图）**。这能在短时间内建立对整个领域的框架性认识。
- **若要复现某个具体方法**：本文不能用于复现。应根据本文的分类和引用，找到该方法的原始论文，并以其作为复现依据。
- **若要借鉴创新点**：应重点学习本文第2节对挑战的归纳，以及第3-6节对各类解决方案的论述。思考自己能否针对其中某个未解决的挑战，提出新的模块或策略。
- **撰写Related Work**：如果你的论文属于定向目标检测领域，本文是一个极佳的Related Work写作模板和参考来源。你可以将其分类体系作为组织你自己相关工作综述的骨架，并引用本文作为领域综述的代表。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C_目标检测_通用与旋转框]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文是一篇关于**光学遥感图像中定向目标检测**的综述（Survey）。它属于计算机视觉（CV）中**目标检测**领域的特定方向——**旋转框目标检测**，专注于遥感（RS）场景。该论文旨在系统性地回顾、分类和分析近年来基于深度学习的定向目标检测方法的进展、挑战与未来方向。它适合被归类在 **“C_目标检测_通用与旋转框”** 这一主题下。

## 2. 一句话总结
本文系统性地回顾了基于深度学习的光学遥感图像定向目标检测方法，通过提出新的分类体系（涵盖检测框架、旋转框回归技术、特征表示方法和常见问题解决方案），全面分析了该领域从水平检测到定向检测的技术演进、核心挑战以及未来的研究方向。

## 3. 背景与问题
- **为什么要做**：随着遥感技术发展，光学卫星和无人机获取的图像数量激增，需要自动化分析技术。定向目标检测是其中的关键基础任务，因为遥感图像通常采用鸟瞰视角拍摄，图像中的物体（如车辆、船舶、建筑物）往往具有任意方向，使用水平边界框（HBB）进行检测效果不佳，容易造成漏检和定位不精确。
- **之前方法的问题**：
    1.  **水平框检测的局限性**：直接将用于自然场景的水平目标检测器应用于遥感图像会导致：（1）在密集场景或大长宽比物体中，水平框之间的IoU可能非常大，导致非极大值抑制（NMS）后漏检；（2）水平框会包含大量背景区域，定位精度低（p.6）。
    2.  **定向检测的特定挑战**：在改造水平检测器以预测旋转框时，会面临额外的挑战：（1）**特征错位**：轴对齐的卷积提取的特征与旋转物体之间存在错位；（2）**空间错位**：基于水平锚点的检测器与旋转物体的IoU计算困难，导致标签分配困难；（3）**旋转框回归问题**：常用的角度表示（θ-based）存在角度周期性问题，四边形表示存在顶点排序问题，都会导致训练不稳定（p.7-8）。
- **核心矛盾**：如何有效解决定向目标检测中引入的**特征错位、空间错位和旋转框回归难题**，同时克服遥感图像本身固有的**尺度变化、复杂背景和弱特征响应**等挑战。

## 4. 核心贡献
基于提供的文本，本文的主要贡献可归纳为四点：
1.  **系统性地回顾了从水平目标检测到定向目标检测的技术演进**，并首次将定向目标检测面临的主要挑战明确归纳为四个方面：特征错位、空间错位、旋转框回归问题以及遥感场景中的常见问题（p.5, 1.3节）。
2.  **提出了一个更全面、细致的定向目标检测方法分类体系（Taxonomy）**。该体系将现有方法从四个维度进行组织：检测框架（如两阶段、单阶段、无锚点、DETR）、旋转框回归技术、特征表示方法、以及针对遥感常见问题的解决方案（p.5, p.9图5）。
3.  **提供了对当前最先进（SOTA）方法在典型数据集上的全面比较和深入分析**，包括对这些方法优缺点的评估，旨在为研究者选择和改进方法提供有价值的见解（p.5）。
4.  **系统性地审视了开放性问题并展望了未来研究方向**，包括轻量化方法、场景特定数据集、多模态数据集、大规模数据集以及多模态大模型等（p.5）。

## 5. 方法详解
**重要说明**：本文本身是一篇综述论文，**并未提出一种全新的检测方法或框架**。其“方法”核心在于**对现有方法的系统性分类、分析和总结**。
- **整体结构**：论文按照“提出挑战 -> 分类解决挑战的方法”的逻辑展开。图5展示了其结构化分类体系。
- **分类体系详解**：
    1.  **检测框架**：根据处理流程，将定向检测器分为四类。
        - **两阶段方法**：首先生成可能包含物体的旋转候选区域（Region Proposals），然后对这些区域进行分类和精修。其设计思想是“粗到精”，以解决特征错位和空间错位问题（p.8, 3.1节）。
        - **单阶段方法**：直接在特征图上进行密集预测，效率更高。通过设计旋转锚点或改进标签分配策略来解决空间错位问题（p.8）。
        - **无锚点方法**：完全抛弃锚点机制，直接预测物体的中心点、尺寸和角度，从而从根本上避免了与锚点相关的空间错位问题（p.8, 3.3节）。
        - **DETR类方法**：将检测视为集合预测问题，利用Transformer的全局注意力机制和端到端训练，去除了NMS和锚点等手工组件，为定向检测提供了新范式（p.8）。
    2.  **旋转框回归技术**：专注于解决旋转框参数化带来的训练难题。
        - **损失函数设计**：通过设计新的损失函数来缓解角度周期性问题或顶点排序问题。
        - **旋转框表示方法**：探索超越简单(θ-based)和四边形之外的新的旋转框参数化方式（p.8, 4节）。
    3.  **特征表示方法**：致力于提取更具旋转不变性或更适合检测旋转物体的特征。
        - **旋转不变特征表示**：通过设计特定的网络模块或变换操作，使提取的特征对物体的旋转不敏感（p.8, 5.1节）。
        - **高级特征表示**：利用注意力机制、特征金字塔网络（FPN）等先进模块，增强特征对多尺度、复杂背景和弱纹理目标的表达能力（p.8, 5.2节）。
    4.  **针对遥感常见问题的解决方案**：处理遥感图像特有的挑战，如尺度变化、复杂背景和弱纹理目标等（p.8, 6节）。
- **与已有方法的差异**：与之前的综述（如Wen et al. 2023, Zhang et al. 2023）相比，本文提供了更深入、更全面的分析，其分类体系（特别是将挑战与解决方案明确对应）被认为更系统、更优（p.4）。

## 6. 实验与结果
作为一篇综述，本文**没有提出新方法并进行实验**。但是，它提供了以下与实验相关的综合信息：
- **使用的数据集**：论文在第7节概述了该领域常用的公开数据集（p.5）。但由于提供的文本未包含第7-8节内容，**具体数据集列表和评估指标（如mAP、角度IoU等）在提供的文本中未明确列出**。
- **对比方法与主实验结果**：论文声称在第8节对最先进方法进行了全面比较和分析（p.5）。然而，**由于提供的文本仅包含前12页（至第9页），第8节的具体对比表格、方法列表和关键性能数字在提供的文本中未找到**。
- **消融/泛化实验及效率信息**：这些通常出现在具体方法论文中，作为综述，本文会汇总相关方法的实验发现，但同样，**这些具体信息在提供的文本片段中未出现**。

## 7. 这篇论文真正有价值的地方
这篇综述的最大价值在于其**系统性梳理和结构化思考**。对于研究者，它的启发在于：
1.  **清晰的问题定义**：它将定向检测的挑战明确定义为四个维度，这为研究者理解问题、定位研究空白提供了清晰的路线图。
2.  **方法论地图**：其提出的四维分类体系（框架、回归、特征、常见问题）就像一张“方法论地图”，可以帮助研究者快速理解现有技术树，判断自己研究（无论是改进现有方法还是提出新方法）在领域中的位置。
3.  **研究起点**：通过本文的文献综述和分类，可以高效地找到该子领域的关键论文和代表性工作，是进入该领域研究的极佳入口。
4.  **批判性视角**：文中对各种方法优缺点的分析，以及对未来方向的展望，有助于激发新的研究思路。

## 8. 局限与问题
1.  **领域聚焦**：本文明确关注于**光学遥感图像**中的定向目标检测。其结论和分类体系是否完全适用于其他场景（如SAR图像、无人机视频、自然场景文本检测）中的旋转目标检测，需要读者自行判断。
2.  **时效性**：综述论文的发表总会滞后于最新研究进展。本文接受日期为2025年5月，但鉴于该领域发展迅速，2024-2025年出现的最新突破（如基于基础模型的新方法）可能未被涵盖。
3.  **深度的权衡**：尽管声称比前人综述更深入，但面对海量文献，任何综述都不得不在广度与深度之间做出权衡。对于具体某一篇被引用的方法，其核心细节仍需阅读原文。
4.  **主观性**：分类体系的选择、重要论文的筛选、优缺点的分析都不可避免地带有作者的视角和判断。

## 9. 我该怎么使用这篇论文
- **快速了解领域**：重点阅读 **Abstract, 第1节（引言），第2节（从水平检测到定向检测的挑战），以及图5（分类体系图）**。这能在短时间内建立对整个领域的框架性认识。
- **若要复现某个具体方法**：本文不能用于复现。应根据本文的分类和引用，找到该方法的原始论文，并以其作为复现依据。
- **若要借鉴创新点**：应重点学习本文第2节对挑战的归纳，以及第3-6节对各类解决方案的论述。思考自己能否针对其中某个未解决的挑战，提出新的模块或策略。
- **撰写Related Work**：如果你的论文属于定向目标检测领域，本文是一个极佳的Related Work写作模板和参考来源。你可以将其分类体系作为组织你自己相关工作综述的骨架，并引用本文作为领域综述的代表。

## 10. 和其他论文的关系
根据主题“C_目标检测_通用与旋转框”和文件名，本文作为一篇综合性综述，与该库中所有关于旋转目标检测的论文都构成“综述与具体研究”的关系。可能特别相关的论文包括：
- 其他针对旋转检测的综述论文，如 `[[2023_A_Survey_of_Oriented_Object_Detection_in_Remote_Sensing_Images.pdf]]`。
- 本文中重点分析的经典旋转检测方法论文，例如可能涉及的 `[[2021_R3Det_Delving_into_Rotated_Object_Detection.pdf]]`（对应文中提到的R3Det）。
- 遥感图像目标检测的通用综述论文。

## 11. 关键词
定向目标检测， 遥感图像， 深度学习， 旋转框， 综述， 特征错位， 空间错位， 检测框架， 旋转框回归， 特征表示， 角度周期性问题

## 12. 可信度说明
本精读笔记**严格基于用户提供的PDF提取文本（前12页/共61页）生成**。提取文本质量良好，清晰涵盖了论文的标题、作者、摘要、引言、与相关综述的比较、研究范围、主要贡献以及从水平检测到定向检测的演进和挑战、检测框架分类体系的开头部分。
- **笔记中明确的信息**：如论文定位、背景问题、核心贡献、方法分类体系框架等，均直接来源于提供的文本。
- **笔记中缺失的信息**：由于提供的文本仅占全文约1/5，论文后续关于旋转框回归技术（第4节）、特征表示（第5节）、遥感常见问题解决方案（第6节）、数据集（第7节）、实验对比（第8节）、未来方向（第9节）的**具体细节、方法对比数字、图表内容等均无法在提供的文本中找到**。因此，笔记中在这些部分明确标注了“在提供的文本中未找到”或基于已有文本进行了概括性描述。**对于想要获取论文全部方法细节和实验结果的研究者，必须阅读完整的PDF原文。**

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2023_Oriented_object_dete.txt` (61/61 页; 原 AI 主体 12/61 + 全文补读 13-61); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-61; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-61。
- **提取情况**: 缺失页 49 页, 其中 49 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Both R3Det and S2A-Net utilize an extra refined head for feature alignment, making
- p.13: 3.3 Anchor-free detectors
- p.13: The above two categories follow the anchor paradigm, which suffers from spatial misalign -
- p.13: Keypoint-based methods first locate a set of adaptive or self-constrained keypoints and
- p.13: The convex hull, which is represented by irregular sample points, is refined using a convex
- p.14: Center-based methods typically generate multiple probabilistic heatmaps and a series of
- p.14: Hence, an effective scheme for increasing the performance of such an approach is to
- p.14: In contrast with the above two methods, which capitalize on the merits of anchor-free
- p.15: 3.4 DETR-based detectors
- p.15: In addition to the above convolution-based methods, DETR-based detectors, including
- p.15: 3.5 Discussion
- p.15: Feature misalignment and spatial misalignment severely impair the performance of ori -

### 缺失页关键摘录

- p.15: et al. 2022 ), resulting in dramatic breakthroughs in terms of accuracy and convergence
- p.15: it achieves greater detection accuracy in terms of a more rigorous metric (i.e., AP75), but
- p.16: choice for the regression task may not guarantee high localization accuracy in terms of
- p.19: and disadvantages of the above OBB representation methods are summarized in Table 2.
- p.20: Table 2 Comparison among different OBB representation methods
- p.21: localization and classification tasks. As a result, the most recent improvements in detec -
- p.21: tion accuracy have been attained via research conducted on enhancing feature representa -
- p.22: a data-dependent manner. As a result, ARC can capture the rotation information of objects
- p.22: corresponding discussion will be brief in this context.
- p.23: 2021 ) and demonstrated that pure CNNs outperform ViTs in terms of accuracy and robust -
- p.25: Oriented object detection in optical remote sensing images using deep…improving their object localization accuracy. In addition, SCRDet (Yang et al. 2019 ) adopts
- p.26: the evaluation criteria for screening positive samples. This scheme can push detectors to
<!-- AI_READING_NOTE_END -->
