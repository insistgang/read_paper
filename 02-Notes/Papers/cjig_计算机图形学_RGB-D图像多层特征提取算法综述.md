---
title: Li Y and Wu X Q. 2024. Survey of multilevel feature extraction methods for RGB D images. Journal of Image and Graphics 29 05
authors:
  - "李洋"
  - "吴晓群"
year: 2024
venue: "中国图象图形学报"
doi: 
pdf: [[cjig_计算机图形学_RGB-D图像多层特征提取算法综述.pdf]]
primary_topic: D_3D_点云_分类_分割_配准
topics:
  - "D_3D_点云_分类_分割_配准"
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
extract_cache: .paper-cache/extracts/cjig_计算机图形学_RGB-D图像多层特征提取算法综述.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/18 pages"
---
# Li Y and Wu X Q. 2024. Survey of multilevel feature extraction methods for RGB D images. Journal of Image and Graphics 29 05

## 基本信息
- **PDF**: [[cjig_计算机图形学_RGB-D图像多层特征提取算法综述.pdf]]
- **primary_topic**: `D_3D_点云_分类_分割_配准`
- **topics**: `D_3D_点云_分类_分割_配准`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Li Y and Wu X Q. 2024. Survey of multilevel feature extraction methods for RGB D images. Journal of Image and Graphics 29 05 |
| **作者** | 李洋; 吴晓群 |
| **发表时间** | 2024 |
| **刊物/会议** | 中国图象图形学报 |
| **DOI** | 未明确 |

## 摘要

> RGB D images contain rich multilevel features such as low level line planar and high level semantic fea⁃ tures. These different levels of features provide valuable information for various computer vision tasks. Computer vision - ， algorithms can extract meaningful information from RGB D images and improve the performance of various tasks including ， ， ， object detection tracking and indoor scene reconstruction by leveraging these multilevel features. Terms such as feature - and contour lines can be used when describing existing line features in a single RGB D image. Line features provide crucial ， information regarding the spatial relationships and boundaries in the input image aiding in the understanding and interpre⁃ tation of input data. Plane and surface are used to describe planar features and those refer to flat or nearly flat regions in the - RGB D image. Terms such as instance and semantic labels can be used when describing an object. Instance labels refer to ， unique identifie

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：RGB-D图像同时包含颜色/纹理信息（RGB）和几何信息（深度），从中提取的线、平面、语义等多层特征可作为高质量先验，用于提升室内场景重建、SLAM、自动驾驶等任务的性能。随着深度相机普及，RGB-D数据易获取，但高质量特征提取仍是研究热点。
- **之前方法有什么问题**：1) 传统方法严重依赖输入数据的质量，而商业深度相机采集的RGB-D数据常因环境、材质、遮挡等因素存在噪声和深度缺失，导致传统算法提取结果不佳（如过度分割、边缘粗糙）。2) 许多特征提取算法（尤其是线特征）仅利用RGB信息，未充分利用深度图的几何信息，限制了在纹理差异小、几何差异显著的场景中的表现。3) 基于深度学习的语义分割等方法需要大规模精确标注数据，获取成本高昂。
- **核心矛盾**：**如何在质量受限的RGB-D数据上，有效融合RGB的纹理/颜色信息和深度图的几何信息，鲁棒地提取高质量的多层特征**。
## 关键贡献

1.  **系统性综述**：首次系统性地面向RGB-D图像，从线、平面、语义三个层次全面梳理和总结了多层特征提取算法，填补了该领域综述文献的空白。
2.  **数据集与评价指标汇总**：详细汇总了NYU v2、SUN RGB-D、ScanNet等多个常用于多层特征提取任务的RGB-D数据集，并系统整理了各任务（线特征、像素级平面/语义特征）的常用定量评价指标（如P, R, IoU, PA, mIoU等）及其计算公式。
3.  **多维度算法对比**：对总结的各类算法从**传统方法**与**基于深度学习的方法**两个视角进行了阐述，并从原理、优缺点、适用场景等多个维度进行了详细的对比分析（如表2、3、4所示）。
4.  **实验分析与定量比较**：不仅进行定性对比，还基于NYU v2等数据集，对线特征和部分平面特征提取算法的性能进行了定量比较分析（如表2）。
5.  **趋势展望**：总结了当前领域亟待解决的问题（如数据标注成本高、深度学习模型依赖大量训练数据）并展望了未来发展趋势（如探索弱监督/无监督学习、设计更高效的RGB-D融合架构）。
## 方法

本文作为综述，**本身不提出新方法**，而是系统总结现有方法。核心框架是按特征层次（线、平面、语义）组织，在每个层次内再按技术路线（传统、深度学习）分类介绍。

- **整体框架**：
  1.  **输入**：RGB-D图像（一对RGB图像和对应的深度图）。
  2.  **处理流程**：根据目标特征类型，选择对应算法。算法可能直接处理2D图像（RGB/深度图），或将RGB-D转换为点云数据再处理。
  3.  **输出**：线特征（线段列表）、平面特征（平面分割掩码或平面参数）、语义特征（每个像素的类别标签）。

- **关键模块与方法（摘要）**：
  - **线特征提取**：
    - **传统方法（2D）**：将深度图视为2D灰度图，利用梯度信息。如LSD、EDLines（速度快）、CannyLines（自适应阈值）。**缺点**：未利用深度几何信息。
    - **传统方法（2.5D）**：充分利用深度几何差异。如FDED（深度边界）、**SFLine**（结合Canny强度边和深度法向，效果优于纯2D方法）。
    - **深度学习方法**：如PPGNet（图推理）、LETR（Transformer，由粗到细）。**关键问题**：若仅输入RGB，则无法区分几何边界与纹理边界。
  - **平面特征提取**：
    - **传统方法**：
      - **区域增长**：如DPD，以种子点生长，对参数和噪声敏感。
      - **RANSAC**：随机采样拟合平面，有一定抗噪性但计算量大。
    - **深度学习方法**：如PlaneNet、PlaneRCNN（输入单张RGB，预测深度和平面）、**PlaneMVS**（利用多视图几何，效果更优）。深度学习的优势在于泛化能力和对噪声的鲁棒性。
  - **语义特征提取**：
    - **全监督学习**：如FCN、RedNet、ESANet（融合RGB和深度编码器）、**ACNet**（使用注意力模块选择性融合RGB和深度特征）。
    - **弱监督学习**：为减少标注成本，探索使用图像级标签、点云等进行训练。**PDF文本中未提供具体的弱监督方法名称和细节。**

- **与已有方法的差异**：本综述的核心差异在于其**聚焦于RGB-D多模态数据**，并**按特征层次（线-面-物体）进行系统组织**，这不同于以往仅针对单一特征（如仅语义分割）或单一数据模态（如仅RGB图像）的综述。
## 实验

- **使用的数据集**：主要提及NYU v2（1449幅，26类场景）、SUN RGB-D（10335幅，47类场景）、ScanNet（1513个场景）等室内RGB-D数据集。
- **对比方法**：在线特征部分，对比了LSD, EDLines, AG3line, CannyLines, SFLine等。在平面特征部分，对比了区域增长、RANSAC及其变种，以及PlaneNet, PlaneRCNN, PlaneMVS等深度学习模型。
- **评价指标**：线特征用Precision (P), Recall (R), IoU；平面和语义特征用Pixel Accuracy (PA), Mean PA (MPA), IoU, Mean IoU (mIoU), Variation of Information (VI), Rand Index (RI), Segmentation Covering (SC)。
- **主实验结果**：提供了线特征在NYU v2上的定量对比（表2）。其中，面向2D输入的方法，**CannyLines**的P, R, IoU均为最优（0.66, 0.42, 0.34）。面向2.5D输入的**SFLine**在可视化结果中明显优于所有仅使用深度图的2D方法（如图3所示）。对于平面和语义特征，文中提到进行了定量比较，但具体数值在提供的文本中未找到。
- **消融/泛化实验**：作为综述，本文未进行自提出方法的消融实验。但总结了所综述方法的优缺点，例如深度学习方法在复杂场景和噪声数据上泛化能力更强，但训练依赖大量数据。
- **效率信息**：提及EDLines速度是LSD的11倍。但PDF文本中未提供其他算法的详细速度、参数量或FLOPs信息。
## 局限

1.  **综述的局限性**：作为综述，本文的核心价值在于梳理和对比，而非提出创新方法。其深度受限于所引用的文献。
2.  **数据集偏向**：总结的数据集（如NYU v2, SUN RGB-D, ScanNet）和算法主要针对**室内静态场景**，对室外、动态或大规模城市场景的覆盖不足。
3.  **效率讨论不足**：对各类算法的计算效率、实时性、部署难度的讨论相对较少，而这对实际应用至关重要。
4.  **最新进展可能缺失**：论文发表于2024年5月，但引用文献截止年份可能在2023年及以前，最前沿的进展（如基于大规模预训练模型的方法）可能未被涵盖。
5.  **“弱监督”部分缺失**：在语义特征部分提到了弱监督学习的重要性，但在提供的文本中，该部分的具体方法介绍缺失。
## 个人评论

1.  **系统性入门指南**：对于刚接触RGB-D多层特征提取的研究者，本文提供了一个清晰、结构化的知识图谱，涵盖了从数据集、评价指标到各层次算法的全貌，是极佳的入门综述。
2.  **清晰的对比视角**：通过“传统 vs. 深度学习”、“2D vs. 2.5D”的对比框架，清晰地揭示了**融合几何信息（深度）的重要性**。例如，对比显示，合理利用深度信息的算法（如SFLine）性能显著优于仅用RGB信息的算法。
3.  **方法论启发**：本文强调了**多模态信息融合**是核心。它启发研究者在设计新算法时，应思考如何更智能、自适应地融合RGB的纹理语义和深度的几何结构，而非简单拼接。例如ACNet的注意力融合机制就是一个很好的例子。
4.  **研究缺口指引**：明确指出了当前领域的挑战，如**高质量数据标注的成本问题**、**深度学习模型对计算资源的需求**、以及**对复杂真实场景（如室外、动态物体）的泛化能力不足**，为后续研究指明了方向。

### 使用建议

- **如果快速了解**：阅读**摘要（Abstract）** 和 **引言（Introduction）** 部分，即可掌握论文的核心动机、研究问题和主要结论。再浏览一下**第1节（数据集和评价指标）** 和**最后一节（总结与展望）** 即可。
- **如果复现**：复现本文无需，因为它是综述。若想复现其对比的某个具体算法，应重点阅读该算法对应的章节（如2.1.2节的SFLine、3.2节的PlaneMVS），并查找对应的原始论文。
- **如果借鉴创新点**：应深入学习**不同特征提取方法之间的融合思路**（如线特征如何指导平面分割、深度信息如何增强语义分割），以及**评价指标的设计和选用**（如mIoU, VI, SC的适用场景）。这些是设计新任务或新模型时的宝贵参考。
- **如果写related work**：可将本文作为“RGB-D图像多层特征提取”或“多模态场景理解”领域的权威综述进行引用。在分类上，它可归入“RGB-D处理”、“特征工程”、“深度学习在计算机图形学中的应用”等相关类别。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[D_3D_点云_分类_分割_配准]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文是一篇**综述（Survey）论文**。它属于计算机图形学与计算机视觉的交叉领域，具体研究方向为**多模态数据（RGB-D图像）的特征提取与理解**。论文旨在系统梳理从RGB-D图像中提取不同层次（线、平面、语义）特征的方法。它适合放在“RGB-D图像处理”、“多模态特征提取”、“室内场景理解”等主题下，与用户提供的主题 `D_3D_点云_分类_分割_配准` 高度相关，因为高质量的线、平面、语义特征是后续点云处理（如配准、分割）和场景重建的重要先验。

## 2. 一句话总结
本文系统综述了从RGB-D图像中提取线特征、平面特征和语义特征三类多层特征的传统及深度学习方法，并对其性能、优缺点进行了对比分析。

## 3. 背景与问题
- **为什么要做**：RGB-D图像同时包含颜色/纹理信息（RGB）和几何信息（深度），从中提取的线、平面、语义等多层特征可作为高质量先验，用于提升室内场景重建、SLAM、自动驾驶等任务的性能。随着深度相机普及，RGB-D数据易获取，但高质量特征提取仍是研究热点。
- **之前方法有什么问题**：1) 传统方法严重依赖输入数据的质量，而商业深度相机采集的RGB-D数据常因环境、材质、遮挡等因素存在噪声和深度缺失，导致传统算法提取结果不佳（如过度分割、边缘粗糙）。2) 许多特征提取算法（尤其是线特征）仅利用RGB信息，未充分利用深度图的几何信息，限制了在纹理差异小、几何差异显著的场景中的表现。3) 基于深度学习的语义分割等方法需要大规模精确标注数据，获取成本高昂。
- **核心矛盾**：**如何在质量受限的RGB-D数据上，有效融合RGB的纹理/颜色信息和深度图的几何信息，鲁棒地提取高质量的多层特征**。

## 4. 核心贡献
1.  **系统性综述**：首次系统性地面向RGB-D图像，从线、平面、语义三个层次全面梳理和总结了多层特征提取算法，填补了该领域综述文献的空白。
2.  **数据集与评价指标汇总**：详细汇总了NYU v2、SUN RGB-D、ScanNet等多个常用于多层特征提取任务的RGB-D数据集，并系统整理了各任务（线特征、像素级平面/语义特征）的常用定量评价指标（如P, R, IoU, PA, mIoU等）及其计算公式。
3.  **多维度算法对比**：对总结的各类算法从**传统方法**与**基于深度学习的方法**两个视角进行了阐述，并从原理、优缺点、适用场景等多个维度进行了详细的对比分析（如表2、3、4所示）。
4.  **实验分析与定量比较**：不仅进行定性对比，还基于NYU v2等数据集，对线特征和部分平面特征提取算法的性能进行了定量比较分析（如表2）。
5.  **趋势展望**：总结了当前领域亟待解决的问题（如数据标注成本高、深度学习模型依赖大量训练数据）并展望了未来发展趋势（如探索弱监督/无监督学习、设计更高效的RGB-D融合架构）。

## 5. 方法详解
本文作为综述，**本身不提出新方法**，而是系统总结现有方法。核心框架是按特征层次（线、平面、语义）组织，在每个层次内再按技术路线（传统、深度学习）分类介绍。

- **整体框架**：
  1.  **输入**：RGB-D图像（一对RGB图像和对应的深度图）。
  2.  **处理流程**：根据目标特征类型，选择对应算法。算法可能直接处理2D图像（RGB/深度图），或将RGB-D转换为点云数据再处理。
  3.  **输出**：线特征（线段列表）、平面特征（平面分割掩码或平面参数）、语义特征（每个像素的类别标签）。

- **关键模块与方法（摘要）**：
  - **线特征提取**：
    - **传统方法（2D）**：将深度图视为2D灰度图，利用梯度信息。如LSD、EDLines（速度快）、CannyLines（自适应阈值）。**缺点**：未利用深度几何信息。
    - **传统方法（2.5D）**：充分利用深度几何差异。如FDED（深度边界）、**SFLine**（结合Canny强度边和深度法向，效果优于纯2D方法）。
    - **深度学习方法**：如PPGNet（图推理）、LETR（Transformer，由粗到细）。**关键问题**：若仅输入RGB，则无法区分几何边界与纹理边界。
  - **平面特征提取**：
    - **传统方法**：
      - **区域增长**：如DPD，以种子点生长，对参数和噪声敏感。
      - **RANSAC**：随机采样拟合平面，有一定抗噪性但计算量大。
    - **深度学习方法**：如PlaneNet、PlaneRCNN（输入单张RGB，预测深度和平面）、**PlaneMVS**（利用多视图几何，效果更优）。深度学习的优势在于泛化能力和对噪声的鲁棒性。
  - **语义特征提取**：
    - **全监督学习**：如FCN、RedNet、ESANet（融合RGB和深度编码器）、**ACNet**（使用注意力模块选择性融合RGB和深度特征）。
    - **弱监督学习**：为减少标注成本，探索使用图像级标签、点云等进行训练。**PDF文本中未提供具体的弱监督方法名称和细节。**

- **与已有方法的差异**：本综述的核心差异在于其**聚焦于RGB-D多模态数据**，并**按特征层次（线-面-物体）进行系统组织**，这不同于以往仅针对单一特征（如仅语义分割）或单一数据模态（如仅RGB图像）的综述。

## 6. 实验与结果
- **使用的数据集**：主要提及NYU v2（1449幅，26类场景）、SUN RGB-D（10335幅，47类场景）、ScanNet（1513个场景）等室内RGB-D数据集。
- **对比方法**：在线特征部分，对比了LSD, EDLines, AG3line, CannyLines, SFLine等。在平面特征部分，对比了区域增长、RANSAC及其变种，以及PlaneNet, PlaneRCNN, PlaneMVS等深度学习模型。
- **评价指标**：线特征用Precision (P), Recall (R), IoU；平面和语义特征用Pixel Accuracy (PA), Mean PA (MPA), IoU, Mean IoU (mIoU), Variation of Information (VI), Rand Index (RI), Segmentation Covering (SC)。
- **主实验结果**：提供了线特征在NYU v2上的定量对比（表2）。其中，面向2D输入的方法，**CannyLines**的P, R, IoU均为最优（0.66, 0.42, 0.34）。面向2.5D输入的**SFLine**在可视化结果中明显优于所有仅使用深度图的2D方法（如图3所示）。对于平面和语义特征，文中提到进行了定量比较，但具体数值在提供的文本中未找到。
- **消融/泛化实验**：作为综述，本文未进行自提出方法的消融实验。但总结了所综述方法的优缺点，例如深度学习方法在复杂场景和噪声数据上泛化能力更强，但训练依赖大量数据。
- **效率信息**：提及EDLines速度是LSD的11倍。但PDF文本中未提供其他算法的详细速度、参数量或FLOPs信息。

## 7. 这篇论文真正有价值的地方
1.  **系统性入门指南**：对于刚接触RGB-D多层特征提取的研究者，本文提供了一个清晰、结构化的知识图谱，涵盖了从数据集、评价指标到各层次算法的全貌，是极佳的入门综述。
2.  **清晰的对比视角**：通过“传统 vs. 深度学习”、“2D vs. 2.5D”的对比框架，清晰地揭示了**融合几何信息（深度）的重要性**。例如，对比显示，合理利用深度信息的算法（如SFLine）性能显著优于仅用RGB信息的算法。
3.  **方法论启发**：本文强调了**多模态信息融合**是核心。它启发研究者在设计新算法时，应思考如何更智能、自适应地融合RGB的纹理语义和深度的几何结构，而非简单拼接。例如ACNet的注意力融合机制就是一个很好的例子。
4.  **研究缺口指引**：明确指出了当前领域的挑战，如**高质量数据标注的成本问题**、**深度学习模型对计算资源的需求**、以及**对复杂真实场景（如室外、动态物体）的泛化能力不足**，为后续研究指明了方向。

## 8. 局限与问题
1.  **综述的局限性**：作为综述，本文的核心价值在于梳理和对比，而非提出创新方法。其深度受限于所引用的文献。
2.  **数据集偏向**：总结的数据集（如NYU v2, SUN RGB-D, ScanNet）和算法主要针对**室内静态场景**，对室外、动态或大规模城市场景的覆盖不足。
3.  **效率讨论不足**：对各类算法的计算效率、实时性、部署难度的讨论相对较少，而这对实际应用至关重要。
4.  **最新进展可能缺失**：论文发表于2024年5月，但引用文献截止年份可能在2023年及以前，最前沿的进展（如基于大规模预训练模型的方法）可能未被涵盖。
5.  **“弱监督”部分缺失**：在语义特征部分提到了弱监督学习的重要性，但在提供的文本中，该部分的具体方法介绍缺失。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：阅读**摘要（Abstract）** 和 **引言（Introduction）** 部分，即可掌握论文的核心动机、研究问题和主要结论。再浏览一下**第1节（数据集和评价指标）** 和**最后一节（总结与展望）** 即可。
- **如果复现**：复现本文无需，因为它是综述。若想复现其对比的某个具体算法，应重点阅读该算法对应的章节（如2.1.2节的SFLine、3.2节的PlaneMVS），并查找对应的原始论文。
- **如果借鉴创新点**：应深入学习**不同特征提取方法之间的融合思路**（如线特征如何指导平面分割、深度信息如何增强语义分割），以及**评价指标的设计和选用**（如mIoU, VI, SC的适用场景）。这些是设计新任务或新模型时的宝贵参考。
- **如果写related work**：可将本文作为“RGB-D图像多层特征提取”或“多模态场景理解”领域的权威综述进行引用。在分类上，它可归入“RGB-D处理”、“特征工程”、“深度学习在计算机图形学中的应用”等相关类别。

## 10. 和其他论文的关系
- **`[[3D点云分割]]`**：本文综述的平面和语义特征提取结果，可直接作为3D点云分割的先验或输入。
- **`[[3D点云配准]]`**：提取的线、平面等几何特征可用于构建更鲁棒的点云配准特征描述符和约束。
- **`[[FCN]]`、`[[DeepLabv3+]]`**：本文在语义特征部分引用的经典深度学习语义分割模型。
- **`[[NYU v2数据集]]`、`[[ScanNet数据集]]`**：本文重点介绍的、在RGB-D特征提取任务中广泛使用的基准数据集。

## 11. 关键词
RGB-D图像， 多层特征， 特征提取， 线特征， 平面特征， 语义分割， 计算机图形学， 深度学习， 室内场景理解， 综述

## 12. 可信度说明
本精读笔记**完全基于用户提供的PDF提取文本**（前12页/共18页）生成。笔记中所有具体方法、数据集信息、数字（如NYU v2的1449幅图像）和对比结果（如表2中的P, R, IoU值）均直接来源于提供的文本。对于文本中未明确说明的信息（如语义特征部分弱监督学习的具体方法、平面特征定量比较的表5内容），已在相应章节标注“PDF文本中未提供”或“未找到”。由于提供的文本不完整（缺少第6页及后续部分），关于语义特征提取方法的详细描述（尤其是基于弱监督学习的部分）和部分实验结果可能不完整，因此笔记中对此部分的概述基于已有文本，可能不全面。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/cjig_计算机图形学_RGB-D图像多层特征提取算法综述.txt` (18/18 页; 原 AI 主体 12/18 + 全文补读 13-18); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-18; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-18。
- **提取情况**: 缺失页 6 页, 其中 6 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Table 6 Comparison of semantic feature extraction methods with RGB -D input
- p.13: Table 7 Quantitative comparison of several semantic segmentation methods
- p.13: RGB -D
- p.15: RGB -D SLAM//Proceedings of 2016 IEEE International Conference
- p.15: Encoder -decoder with atrous separable convolution for semantic
- p.16: RANSAC for 3D point cloud plane segmentation based on normal
- p.16: Proceedings of 2022 IEEE/CVF Conference on Computer Vision
- p.16: International Conference on Medical Image Computing and
- p.17: method based on RANSAC and support vector machine//Proceed ⁃
- p.17: Learning attraction field representation for robust line segment
- p.17: 2015 IEEE International Conference on Communication Software

### 缺失页关键摘录

- p.13: Table 6 Comparison of semantic feature extraction methods with RGB -D input
- p.13: Table 7 Quantitative comparison of several semantic segmentation methods
- p.15: rell T . 2011 . A category -level 3-D object dataset ： putting the kinect
- p.16: multi -view RGB -D object dataset//Proceedings of 2011 IEEE Inter ⁃
- p.16: scene understanding benchmark suite//Proceedings of 2015 IEEE
- p.17: benchmark for the evaluation of RGB -D SLAM systems//Proceed ⁃
<!-- AI_READING_NOTE_END -->
