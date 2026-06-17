---
title: A Survey of Self-Supervised and
authors:
  - "Gabriel Huang"
  - "Issam Laradji"
  - "David Vázquez"
  - "Simon Lacoste-Julien"
  - "Pau Rodríguez"
year: 2021
venue: ACM-MetaRCNN Meta-RCNN MPSR
doi: 
pdf: [[2021_A_Survey_of_Self-Sup.pdf]]
primary_topic: Q_自监督_对比学习_主动学习
topics:
  - "Q_自监督_对比学习_主动学习"
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
extract_cache: .paper-cache/extracts/2021_A_Survey_of_Self-Sup.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/20 pages"
---
# A Survey of Self-Supervised and

## 基本信息
- **PDF**: [[2021_A_Survey_of_Self-Sup.pdf]]
- **primary_topic**: `Q_自监督_对比学习_主动学习`
- **topics**: `Q_自监督_对比学习_主动学习`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A Survey of Self-Supervised and |
| **作者** | Gabriel Huang; Issam Laradji; David Vázquez; Simon Lacoste-Julien; Pau Rodríguez |
| **发表时间** | 2021 |
| **刊物/会议** | ACM-MetaRCNN Meta-RCNN MPSR |
| **DOI** | 未明确 |

## 摘要

> segmentation,whichrequiredenselabelingoftheimage.Whilefew-shotobjectdetectionisabouttrainingamodelonnovel(unseen) objectclasseswithlittledata,itstillrequirespriortrainingonmanylabeledexamplesofbase(seen)classes.Ontheotherhand, self-supervisedmethodsaimatlearningrepresentationsfromunlabeleddatawhichtransferwelltodownstreamtaskssuchasobject detection.Combiningfew-shotandself-supervisedobjectdetectionisapromisingresearchdirection.Inthissurvey,wereviewand characterizethemostrecentapproachesonfew-shotandself-supervisedobjectdetection.Then,wegiveourmaintakeawaysand discussfutureresearchdirections.Projectpage:https://gabrielhuang.github.io/fsod-survey/ IndexTerms—self-supervised,few-shot,low-data,objectdetection,instancesegmentation (cid:70) 1 INTRODUCTION TRADITIONAL object detectors rely on large supervised thus the representation might discard critical information objectdetectiondatasetssuchasPASCALVOC[28]and forobjectdetection.Moreover,ithasbeenshownthathigher MS COCO [71], which have ove

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **论文为什么要做**：传统目标检测严重依赖大规模人工标注数据集（如PASCAL VOC， MS COCO），而为对象检测和实例分割进行密集标注（边界框/掩码）成本极高且耗时，尤其是在专业领域（如植物物种识别）。小样本目标检测（FSOD）旨在用少量样本识别新类别，但仍需在大量标注的基类数据上进行预训练。因此，探索如何利用更易获取的无标签数据来辅助这一过程变得至关重要。
- **之前方法有什么问题**：
    1.  **对分类任务的依赖**：主流的自监督方法（如SimCLR, MoCo）主要为图像分类任务设计，旨在最大化ImageNet Top-1准确率。然而，分类任务中学到的某些不变性（如对平移的不变性）可能不利于需要精确定位的目标检测任务，导致表征丢弃对检测至关重要的信息。
    2.  **预训练不全面**：早期的小样本检测方法主要预训练骨干网络（Backbone），而未对区域建议网络（RPN）、检测头等目标检测器的关键组件进行预训练。
    3.  **研究割裂**：自监督学习和小样本目标检测作为两个快速发展但独立的领域，此前缺乏一篇综述将它们系统性地联系起来进行讨论。
- **作者想解决的核心矛盾**：**无标签数据的充裕性**与**小样本检测对高质量、任务相关表征的迫切需求**之间的矛盾。即，如何设计自监督预训练任务，使其学到的表征能够更好地服务于目标检测（尤其是小样本场景）的定位与分类需求。
## 关键贡献

1.  **首篇交叉综述**：这是第一篇同时系统综述小样本目标检测（FSOD）和自监督目标检测（SSOD）预训练方法的学术工作，填补了两者结合的研究空白。
2.  **系统性分类法**：基于预训练方式（监督/自监督）、预训练范围（仅骨干/骨干+检测头）以及是否属于小样本方法，对现有方法提出了一个清晰的分类框架（如图1所示）。
3.  **深入分析FSOD框架**：详细阐述了标准FSOD框架（基类训练 -> 小样本微调 -> 评估）的流程，并明确指出了其与传统小样本分类（FSC）在“多对象/图像”、“基类与新类联合预测”、“评估方式”等方面的**关键差异**。
4.  **全面回顾SSOD预训练**：系统梳理了用于目标检测的自监督预训练方法，包括仅预训练骨干的方法（如MoCo）和预训练整个检测器的方法（如DETReg），并讨论了它们的设计动机和与检测任务的适配性。
5.  **提出研究启示与未来方向**：基于综述分析，总结了主要结论，并讨论了将自监督、小样本检测与主动学习、Transformer架构等相结合的未来研究趋势。
## 方法

作为一篇综述，本节将梳理论文所介绍的几类核心方法框架。

**整体框架与分类**：
论文将方法分为三大类（图1）：
1.  **基于监督骨干预训练的小样本检测方法**：传统做法，使用ImageNet分类预训练的骨干网络初始化。
2.  **基于自监督骨干预训练的小样本检测方法**：使用自监督任务（如对比学习）在无标签数据上预训练骨干网络，然后用于初始化小样本检测器。
3.  **自监督骨干与检测头预训练方法**：不仅预训练骨干，还预训练RPN、检测头等组件。这类方法（如DETReg）被认为更能适应检测任务。

**关键模块与机制**：
- **小样本目标检测（FSOD）的标准流程**（第4.1节， p.4-5）：
    - **输入**：带标注的基类图像、少量（K-shot）带标注的支持集图像（包含基类和新类）、测试图像。
    - **输出**：在测试图像上同时检测基类和新类对象的边界框及类别。
    - **训练/推理流程**：
        1.  **基类训练**：在大量标注的基类数据上训练一个标准的目标检测器。
        2.  **小样本微调/条件化**：使用包含少量基类和新类样本的支持集，对模型进行微调（fine-tuning）或条件化（conditioning）。
        3.  **小样本评估**：在测试集上评估模型对基类和新类的联合检测性能，分别报告基类AP（bAP）和新类AP（nAP）。
- **用于检测的自监督预训练**：
    - **骨干预训练**：采用对比学习（如MoCo, SimCLR）或聚类（如SwAV）等方法，在ImageNet或COCO的无标签图像上预训练骨干网络，目标是学习**通用的视觉表征**。论文指出，这些表征可能对平移不变性过强，不利于定位（p.1）。
    - **整体检测器预训练（以DETReg为例）**（第5.2节）：这类方法更进一步。例如DETReg，它不仅利用对比学习预训练骨干，还设计自监督任务来预训练**区域建议网络（RPN）**，使其学会在无标签数据中定位“显著区域”（可能的对象），从而为整个检测器提供更好的初始化（p.1, p.5）。
- **主流目标检测器回顾**（第3.1节， p.2-3）：
    - **两阶段检测器（如Faster R-CNN）**：骨干 -> 特征金字塔网络（FPN） -> 区域建议网络（RPN）生成候选框 -> RoIAlign池化 -> 检测头（分类+回归）。需要后处理NMS。
    - **单阶段检测器（如YOLO, SSD）**：直接从特征图预测物体，更快但精度可能稍低。
    - **基于Transformer的检测器（如DETR）**：骨干 -> Transformer编码器 -> Transformer解码器（使用可学习的“对象查询”）。采用**匈牙利匹配**损失进行端到端训练，无需NMS，架构更简洁。

**数学公式或机制的直观解释**：
- **匈牙利匹配损失（用于DETR）**：在训练时，通过二分图匹配算法，将模型预测的固定数量个框（如100个）与真实标签框进行最优的一一匹配，然后仅对匹配上的预测计算损失（分类+边界框回归）。这使得模型学会输出一组不重复的预测，从而取代传统的NMS（p.3）。
## 实验

由于提供的文本主要是综述框架而非单一实验论文，具体实验结果数字未在提供的摘录中列出，但论文讨论了实验设计的标准。
- **使用的数据集**：**PASCAL VOC** 和 **MS COCO** 是FSOD和SSOD社区最常用的基准数据集（p.3）。
- **对比方法**：综述中列举并分类了众多方法，如基于微调的TFA、MPSR，基于元学习的Meta-RCNN，以及自监督的DETReg等。
- **评价指标**：主要使用**平均精度均值（mAP）** 的变体。对于PASCAL VOC，常用**mAP50**（IoU阈值为50%）。对于MS COCO，使用更严格的COCO-style mAP（在不同IoU阈值上平均）。在小样本设定下，会分别报告基类AP（bAP50, bAP75, bAP）和新类AP（nAP50, nAP75, nAP）（p.4, p.5）。
- **主实验结果**：文本中提到，当前MS COCO上的小样本检测**最优结果（state-of-the-art）是由DETReg方法取得的**，该方法使用了自监督预训练整个检测器（骨干+检测头）的策略（p.1）。
- **消融与评估设计**：论文强调了**多次评估的重要性**。由于小样本微调时支持集是随机采样的，单次评估的方差很大。研究应报告多次（如20次以上）随机采样支持集后的平均性能和方差，以获得稳定可靠的结果（图5及p.6）。
- **速度/参数量等效率信息**：PDF文本中未明确说明。
## 局限

1.  **综述的固有局限**：作为一篇综述，它没有提出新的算法或进行全新的实验验证，主要是对现有工作的梳理和评述。
2.  **领域覆盖范围**：主要聚焦于**通用的物体检测**，对于特定领域（如医学影像、遥感、视频）中的小样本/自监督检测方法可能未深入涉及。
3.  **技术发展的时变性**：文中讨论的某些“最新”方法（如截至2022年）可能已有更新或更优的替代方案出现，阅读时需注意论文的发表时间。
4.  **对基类数据的依赖假设**：标准FSOD框架依然假设拥有大量标注的基类数据。文中提到DETReg探索了移除基类训练阶段（p.5），但这会带来性能下降，表明完全摆脱大规模标注仍然很困难。
5.  **复现风险**：由于不同论文的实验设置（如基类/新类划分、支持集采样方式、骨干网络细节）可能存在差异，复现具体方法时需仔细对照原论文的实验协议。
## 个人评论

1.  **提供清晰的领域地图**：对于刚进入该领域的研究者，本文的**分类框架（图1）** 是极佳的路线图，能快速理清自监督预训练、小样本学习与目标检测之间错综复杂的关系。
2.  **指出关键洞察**：论文明确指出了“**为分类设计的自监督表征可能不适合检测**”以及“**预训练整个检测器比仅预训练骨干更重要**”这两个核心洞察，这直接指导了后续方法的设计方向（如DETReg）。
3.  **强调严谨的实验范式**：对**小样本评估中多次采样支持集以报告均值和方差**的强调，是确保研究结果可信、可复现和可比的关键实践。
4.  **界定研究边界与未来**：清晰地对比了FSOD与FSC的差异，避免了方法的混淆应用。同时提出的未来方向（如与主动学习结合、利用Transformer）为后续研究打开了思路。

### 使用建议

- **如果快速了解**：重点阅读**摘要（Abstract）**、**引言（Introduction）**、**第4.1节（FSOD框架）**、**第5节开头（自监督检测预训练概述）** 以及**第6节（主要结论和未来趋势）**。这能让你在30分钟内掌握核心思想。
- **如果复现**：详细阅读**第3节（背景）** 了解检测器架构，精读**第4.1节**掌握FSOD标准评估流程，以及**第5.2节**关于自监督整体检测器预训练（如DETReg）的具体描述。
- **如果借鉴创新点**：学习论文的**分类框架（图1）** 的构建思路，以及它如何从“表征与任务的不匹配”中提炼出研究问题。思考如何将其他模态（如文本、音频）或任务（如分割、跟踪）与自监督和小样本结合。
- **如果写Related Work**：可以将本文放在“自监督学习”或“小样本学习”的相关工作部分，作为对**自监督学习应用于视觉检测任务**或**小样本检测方法综述**的权威引用。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[Q_自监督_对比学习_主动学习]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**计算机视觉**领域的**综述论文**，具体聚焦于**自监督学习**和**小样本目标检测**两个方向的交叉与结合。它旨在解决目标检测中**数据标注成本高昂**的问题，并评估自监督预训练技术对提升小样本检测性能的作用。该论文适合作为“自监督表征学习在目标检测中的应用”或“低资源目标检测”主题下的系统性文献梳理。

## 2. 一句话总结
这篇综述系统地回顾并分类了小样本目标检测和自监督目标检测预训练的最新方法，特别强调了自监督预训练技术如何作为一种有效的“桥梁”，将无标签数据利用与小样本检测需求连接起来，并展望了未来研究方向。

## 3. 背景与问题
- **论文为什么要做**：传统目标检测严重依赖大规模人工标注数据集（如PASCAL VOC， MS COCO），而为对象检测和实例分割进行密集标注（边界框/掩码）成本极高且耗时，尤其是在专业领域（如植物物种识别）。小样本目标检测（FSOD）旨在用少量样本识别新类别，但仍需在大量标注的基类数据上进行预训练。因此，探索如何利用更易获取的无标签数据来辅助这一过程变得至关重要。
- **之前方法有什么问题**：
    1.  **对分类任务的依赖**：主流的自监督方法（如SimCLR, MoCo）主要为图像分类任务设计，旨在最大化ImageNet Top-1准确率。然而，分类任务中学到的某些不变性（如对平移的不变性）可能不利于需要精确定位的目标检测任务，导致表征丢弃对检测至关重要的信息。
    2.  **预训练不全面**：早期的小样本检测方法主要预训练骨干网络（Backbone），而未对区域建议网络（RPN）、检测头等目标检测器的关键组件进行预训练。
    3.  **研究割裂**：自监督学习和小样本目标检测作为两个快速发展但独立的领域，此前缺乏一篇综述将它们系统性地联系起来进行讨论。
- **作者想解决的核心矛盾**：**无标签数据的充裕性**与**小样本检测对高质量、任务相关表征的迫切需求**之间的矛盾。即，如何设计自监督预训练任务，使其学到的表征能够更好地服务于目标检测（尤其是小样本场景）的定位与分类需求。

## 4. 核心贡献
1.  **首篇交叉综述**：这是第一篇同时系统综述小样本目标检测（FSOD）和自监督目标检测（SSOD）预训练方法的学术工作，填补了两者结合的研究空白。
2.  **系统性分类法**：基于预训练方式（监督/自监督）、预训练范围（仅骨干/骨干+检测头）以及是否属于小样本方法，对现有方法提出了一个清晰的分类框架（如图1所示）。
3.  **深入分析FSOD框架**：详细阐述了标准FSOD框架（基类训练 -> 小样本微调 -> 评估）的流程，并明确指出了其与传统小样本分类（FSC）在“多对象/图像”、“基类与新类联合预测”、“评估方式”等方面的**关键差异**。
4.  **全面回顾SSOD预训练**：系统梳理了用于目标检测的自监督预训练方法，包括仅预训练骨干的方法（如MoCo）和预训练整个检测器的方法（如DETReg），并讨论了它们的设计动机和与检测任务的适配性。
5.  **提出研究启示与未来方向**：基于综述分析，总结了主要结论，并讨论了将自监督、小样本检测与主动学习、Transformer架构等相结合的未来研究趋势。

## 5. 方法详解
作为一篇综述，本节将梳理论文所介绍的几类核心方法框架。

**整体框架与分类**：
论文将方法分为三大类（图1）：
1.  **基于监督骨干预训练的小样本检测方法**：传统做法，使用ImageNet分类预训练的骨干网络初始化。
2.  **基于自监督骨干预训练的小样本检测方法**：使用自监督任务（如对比学习）在无标签数据上预训练骨干网络，然后用于初始化小样本检测器。
3.  **自监督骨干与检测头预训练方法**：不仅预训练骨干，还预训练RPN、检测头等组件。这类方法（如DETReg）被认为更能适应检测任务。

**关键模块与机制**：
- **小样本目标检测（FSOD）的标准流程**（第4.1节， p.4-5）：
    - **输入**：带标注的基类图像、少量（K-shot）带标注的支持集图像（包含基类和新类）、测试图像。
    - **输出**：在测试图像上同时检测基类和新类对象的边界框及类别。
    - **训练/推理流程**：
        1.  **基类训练**：在大量标注的基类数据上训练一个标准的目标检测器。
        2.  **小样本微调/条件化**：使用包含少量基类和新类样本的支持集，对模型进行微调（fine-tuning）或条件化（conditioning）。
        3.  **小样本评估**：在测试集上评估模型对基类和新类的联合检测性能，分别报告基类AP（bAP）和新类AP（nAP）。
- **用于检测的自监督预训练**：
    - **骨干预训练**：采用对比学习（如MoCo, SimCLR）或聚类（如SwAV）等方法，在ImageNet或COCO的无标签图像上预训练骨干网络，目标是学习**通用的视觉表征**。论文指出，这些表征可能对平移不变性过强，不利于定位（p.1）。
    - **整体检测器预训练（以DETReg为例）**（第5.2节）：这类方法更进一步。例如DETReg，它不仅利用对比学习预训练骨干，还设计自监督任务来预训练**区域建议网络（RPN）**，使其学会在无标签数据中定位“显著区域”（可能的对象），从而为整个检测器提供更好的初始化（p.1, p.5）。
- **主流目标检测器回顾**（第3.1节， p.2-3）：
    - **两阶段检测器（如Faster R-CNN）**：骨干 -> 特征金字塔网络（FPN） -> 区域建议网络（RPN）生成候选框 -> RoIAlign池化 -> 检测头（分类+回归）。需要后处理NMS。
    - **单阶段检测器（如YOLO, SSD）**：直接从特征图预测物体，更快但精度可能稍低。
    - **基于Transformer的检测器（如DETR）**：骨干 -> Transformer编码器 -> Transformer解码器（使用可学习的“对象查询”）。采用**匈牙利匹配**损失进行端到端训练，无需NMS，架构更简洁。

**数学公式或机制的直观解释**：
- **匈牙利匹配损失（用于DETR）**：在训练时，通过二分图匹配算法，将模型预测的固定数量个框（如100个）与真实标签框进行最优的一一匹配，然后仅对匹配上的预测计算损失（分类+边界框回归）。这使得模型学会输出一组不重复的预测，从而取代传统的NMS（p.3）。

## 6. 实验与结果
由于提供的文本主要是综述框架而非单一实验论文，具体实验结果数字未在提供的摘录中列出，但论文讨论了实验设计的标准。
- **使用的数据集**：**PASCAL VOC** 和 **MS COCO** 是FSOD和SSOD社区最常用的基准数据集（p.3）。
- **对比方法**：综述中列举并分类了众多方法，如基于微调的TFA、MPSR，基于元学习的Meta-RCNN，以及自监督的DETReg等。
- **评价指标**：主要使用**平均精度均值（mAP）** 的变体。对于PASCAL VOC，常用**mAP50**（IoU阈值为50%）。对于MS COCO，使用更严格的COCO-style mAP（在不同IoU阈值上平均）。在小样本设定下，会分别报告基类AP（bAP50, bAP75, bAP）和新类AP（nAP50, nAP75, nAP）（p.4, p.5）。
- **主实验结果**：文本中提到，当前MS COCO上的小样本检测**最优结果（state-of-the-art）是由DETReg方法取得的**，该方法使用了自监督预训练整个检测器（骨干+检测头）的策略（p.1）。
- **消融与评估设计**：论文强调了**多次评估的重要性**。由于小样本微调时支持集是随机采样的，单次评估的方差很大。研究应报告多次（如20次以上）随机采样支持集后的平均性能和方差，以获得稳定可靠的结果（图5及p.6）。
- **速度/参数量等效率信息**：PDF文本中未明确说明。

## 7. 这篇论文真正有价值的地方
1.  **提供清晰的领域地图**：对于刚进入该领域的研究者，本文的**分类框架（图1）** 是极佳的路线图，能快速理清自监督预训练、小样本学习与目标检测之间错综复杂的关系。
2.  **指出关键洞察**：论文明确指出了“**为分类设计的自监督表征可能不适合检测**”以及“**预训练整个检测器比仅预训练骨干更重要**”这两个核心洞察，这直接指导了后续方法的设计方向（如DETReg）。
3.  **强调严谨的实验范式**：对**小样本评估中多次采样支持集以报告均值和方差**的强调，是确保研究结果可信、可复现和可比的关键实践。
4.  **界定研究边界与未来**：清晰地对比了FSOD与FSC的差异，避免了方法的混淆应用。同时提出的未来方向（如与主动学习结合、利用Transformer）为后续研究打开了思路。

## 8. 局限与问题
1.  **综述的固有局限**：作为一篇综述，它没有提出新的算法或进行全新的实验验证，主要是对现有工作的梳理和评述。
2.  **领域覆盖范围**：主要聚焦于**通用的物体检测**，对于特定领域（如医学影像、遥感、视频）中的小样本/自监督检测方法可能未深入涉及。
3.  **技术发展的时变性**：文中讨论的某些“最新”方法（如截至2022年）可能已有更新或更优的替代方案出现，阅读时需注意论文的发表时间。
4.  **对基类数据的依赖假设**：标准FSOD框架依然假设拥有大量标注的基类数据。文中提到DETReg探索了移除基类训练阶段（p.5），但这会带来性能下降，表明完全摆脱大规模标注仍然很困难。
5.  **复现风险**：由于不同论文的实验设置（如基类/新类划分、支持集采样方式、骨干网络细节）可能存在差异，复现具体方法时需仔细对照原论文的实验协议。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**摘要（Abstract）**、**引言（Introduction）**、**第4.1节（FSOD框架）**、**第5节开头（自监督检测预训练概述）** 以及**第6节（主要结论和未来趋势）**。这能让你在30分钟内掌握核心思想。
- **如果复现**：详细阅读**第3节（背景）** 了解检测器架构，精读**第4.1节**掌握FSOD标准评估流程，以及**第5.2节**关于自监督整体检测器预训练（如DETReg）的具体描述。
- **如果借鉴创新点**：学习论文的**分类框架（图1）** 的构建思路，以及它如何从“表征与任务的不匹配”中提炼出研究问题。思考如何将其他模态（如文本、音频）或任务（如分割、跟踪）与自监督和小样本结合。
- **如果写Related Work**：可以将本文放在“自监督学习”或“小样本学习”的相关工作部分，作为对**自监督学习应用于视觉检测任务**或**小样本检测方法综述**的权威引用。

## 10. 和其他论文的关系
根据提供的主题 `Q_自监督_对比学习_主动学习`，可能相关的论文包括：
- **自监督对比学习奠基工作**：`MoCo` (Momentum Contrast), `SimCLR` (A Simple Framework for Contrastive Learning), `BYOL` (Bootstrap Your Own Latent)。这些是本文讨论的骨干预训练方法的基础。
- **小样本学习/元学习工作**：`MAML` (Model-Agnostic Meta-Learning)， 本文将其作为小样本分类的代表进行了对比。
- **自监督目标检测代表工作**：`DETReg`， 本文重点讨论的将自监督预训练扩展到整个检测器的方法。
- **基础目标检测架构**：`Faster R-CNN`, `DETR`, `Deformable DETR`， 本文作为背景介绍。
- **主动学习**：本文在第6节（未来方向，未提供全文）提到了主动学习是潜在的结合方向，因此与该主题下的方法（如主动选择最有价值的样本进行标注）相关。

## 11. 关键词
自监督学习， 小样本学习， 目标检测， 实例分割， 预训练， 表征学习， 对比学习， Transformer， DETR， 元学习

## 12. 可信度说明
本篇精读笔记主要基于提供的PDF文本的前12页内容生成，该部分涵盖了摘要、引言、相关工作、背景知识（目标检测架构与评估）、小样本目标检测框架与方法，以及自监督目标检测预训练的起始部分。文本提取质量良好，内容连贯，信息丰富。然而，关于后续的自监督检测方法详细分类（第5节后半部分）、主要结论（第6节）、未来趋势（第7节）以及参考文献的完整列表在提供的摘录中缺失或不完整，因此笔记中这些部分的描述基于现有文本的概括性提及，而非完整的详细内容。文中所有引用和数字均严格来自提供的文本段落。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2021_A_Survey_of_Self-Sup.txt` (20/20 页; 原 AI 主体 12/20 + 全文补读 13-20); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-20; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-20。
- **提取情况**: 缺失页 8 页, 其中 8 页提取到可读文本。缺失页包含正文/附录内容, 其中约 3 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: IEEE TRANSACTIONS ON PATTERN ANAL YSIS AND MACHINE INTELLIGENCE 13
- p.13: 5.3 Object Detection Pretraining
- p.13: Self-supervised object detection approaches attempt to rem-
- p.13: 5.3.1 Predictive approaches 3
- p.13: DETReg, a training-free heuristic based on iteratively merg-
- p.13: To pretrain DETR on unsupervised images, the multi-
- p.13: DETR loss is used, except that the matching cost used to
- p.13: On top of the DETR loss, an additional reconstruction
- p.13: 1. Also, an interesting by-product of UP-
- p.13: DETR is that it learns a conditioning branch, which can be
- p.13: 5.3.2 Local Contrastive Learning 3
- p.13: 14. Note that Selective Search used to be a popular training-free

### 缺失页关键摘录

- p.13: class classiﬁcation heads (see Figure 3) which would nor-
- p.13: in Figure 3). This is done by partitioning the object queries
- p.13: 16. Not reported in Table 4 due to using different splits.learning location-aware representations. Some of them, such
- p.13: locations and scales onto other images of the dataset (the
- p.14: In Table 4, we review the self-supervised object detection
- p.14: on the labeled dataset, which could render self-supervision
- p.15: in Figure 7. More generally, there is growing belief from
- p.15: 6.5 Problems with current evaluation procedures
- p.15: Comparisons such as Table 3 and Table 4 should only be
- p.15: plored for each benchmark. Results could be presented
- p.16: work and reviewed the main benchmarks and evaluation
- p.18: [41] A. Gupta, P . Dollar, and R. Girshick. Lvis: A dataset
<!-- AI_READING_NOTE_END -->
