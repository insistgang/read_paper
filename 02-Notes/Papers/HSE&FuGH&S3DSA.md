---
title: "DEFN: Dual-Encoder Fourier Group Harmonics Network for Three-Dimensional"
authors:
  - "Xiaohua Jiang"
  - "Yihao Guo"
  - "Jian Huang"
  - "Yuting Wu"
  - "Meiyi Luo"
  - "Zhaoyang Xu"
  - "Qianni Zhang"
  - "Xingru Huang"
  - "Hong He"
  - "Shaowei Jiang"
  - "Jing Ye"
  - "Mang Xiao"
year: 2024
venue: "arXiv"
doi: 
pdf: [[HSE&FuGH&S3DSA.pdf]]
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
extract_cache: .paper-cache/extracts/HSE&FuGH&S3DSA.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/36 pages"
---
# DEFN: Dual-Encoder Fourier Group Harmonics Network for Three-Dimensional

## 基本信息
- **PDF**: [[HSE&FuGH&S3DSA.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | DEFN: Dual-Encoder Fourier Group Harmonics Network for Three-Dimensional |
| **作者** | Xiaohua Jiang; Yihao Guo; Jian Huang; Yuting Wu; Meiyi Luo; Zhaoyang Xu; Qianni Zhang; Xingru Huang; Hong He; Shaowei Jiang; Jing Ye; Mang Xiao |
| **发表时间** | 2024 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Theprecisespatialandquantitativedelineationofindistinct-boundarymedicalobjectsisparamountfortheaccuracy ofdiagnosticprotocols,efficacyofsurgicalinterventions,andreliabilityofpostoperativeassessments. Despitetheir significance,theeffectivesegmentationandinstantaneousthree-dimensionalreconstructionaresignificantlyimpeded by the paucity of representative samples in available datasets and noise artifacts. To surmount these challenges, we introduced Stochastic Defect Injection (SDi) to augment the representational diversity of challenging indistinct- boundary objects within training corpora. Consequently, we propose the Dual-Encoder Fourier Group Harmonics Network (DEFN) to tailor noise filtration, amplify detailed feature recognition, and bolster representation across diversemedicalimagingscenarios. ByincorporatingDynamicWeightComposing(DWC)lossdynamicallyadjusts model’sfocusbasedontrainingprogression,DEFNachievesSOTAperformanceontheOIMHSpublicdataset,show- casingeffectivenessinindistinctb

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么做**：医学图像中许多重要目标（如黄斑裂孔、下咽癌）具有边界模糊、难以辨识的特点。精确分割这些目标对于诊断、手术规划和疗效评估至关重要，但现有方法效果不佳 (p.1-2)。
- **之前方法的问题**：
    1.  **数据稀缺与噪声干扰**：可用数据集中代表性样本不足，且成像存在噪声伪影，限制了数据驱动模型的性能 (p.1)。
    2.  **现有技术局限**：传统方法和深度学习模型在应对具有“概念性边界”（如黄斑裂孔的上边界需推断）或被阴影遮挡的区域时表现不佳 (p.1-2)。
    3.  **损失函数单一**：常用的损失函数（如Dice loss, Cross-entropy loss）通常在特定方面（如边界、类别不平衡）有效，但缺乏普适性，无法完美应对所有分割挑战 (p.6)。
- **核心矛盾**：如何在**训练数据稀缺且质量不高（噪声大、边界模糊）** 的约束下，实现对**三维医学图像中边界模糊目标的精确、鲁棒分割**。
## 关键贡献

1.  **提出`SDi`数据增强技术**：通过序列扩展和模拟缺陷注入（孤立注入与综合注入两种策略），专门用于人工增加稀缺的边界模糊目标（如黄斑裂孔）的样本多样性，缓解数据不足问题 (p.3, 7-8)。
2.  **提出`DEFN`分割网络**：这是一个双编码器网络，其核心创新在于集成了三个关键模块：
    - **`FuGH`模块**：通过频域组卷积增强对周期性模式的识别，实现噪声抑制和特征增强。
    - **`S3DSA`模块**：简化的3D空间注意力，通过调整空间区域信息权重来增强模型对关键区域（如病灶）的聚焦能力。
    - **`HSE`模块**：谐波挤压激励模块，通过学习复杂的通道间权重模式来精确强调关键特征 (p.4)。
3.  **提出`DWC`动态权重合成损失策略**：一种网络优化策略，允许根据训练进程动态融合和调整多个损失函数，以适应不同训练阶段的需求，从而提升分割精度和鲁棒性 (p.4)。
4.  **开发三维重建方案**：基于分割结果，能够对视网膜结构进行精确建模和定量分析 (p.4)。
## 方法

- **整体框架**：如图2 (p.2) 所示，项目流程包含一个利用`SDi`进行数据增强的管道、`DEFN`模型的预训练和微调阶段，以及最终的分割推理管道。
- **输入与输出**：输入为1通道的三维医学图像（尺寸`1×W×H×D`），输出为`C`通道的三维分割图（尺寸`C×W×H×D`）。
- **关键模块详解**：
    1.  **`FuGH`（傅里叶组谐波）模块**：这是频域注意力或处理的核心。论文描述其通过“频域组卷积”来增强对周期性模式的识别，从而抑制噪声、增强细节特征并提供更广的全局感受野 (p.4, 6)。
    2.  **`S3DSA`（简化3D空间注意力）模块**：这是空间注意力模块。其作用是通过“调整空间区域信息的权重”，让模型更专注于图像中的关键区域（如边界模糊的病灶），从而提高识别精度 (p.4)。
    3.  **`HSE`（谐波挤压激励）模块**：这是通道注意力模块。它通过“学习复杂的通道间权重模式”，实现对关键特征的精确加权强调 (p.4)。
- **模块连接**：根据图2的架构图，`FuGH`、`HSE`和`Norm`（归一化）在编码器和解码器的主分支中交替使用。`S3DSA`（图中标注为“Simplified 3D Spatial Attention”）可能作用于特征图，其具体位置在文本描述中未详述，但根据功能推断可能在编码器后或与解码器特征结合。
- **训练方式**：采用两阶段训练。首先使用大型的`CARS-30k`数据集进行**预训练**，然后使用目标数据集（如OIMHS中的黄斑裂孔数据）进行**微调** (p.2)。损失函数使用了`DWC`策略动态组合了多种损失，包括边界损失(`Boundary`)、Dice损失(`Dice`)、交叉熵损失(`CE`)、焦点损失(`Focal`)、深度排序损失(`DeepRanking`)和DWC损失自身 (p.2)。
- **推理流程**：输入一张三维图像，经过训练好的`DEFN`网络前向传播，输出像素级的类别预测，得到分割结果。该结果还可用于后续的三维重建 (p.4)。
- **与已有方法的差异**：与传统3D U-Net等相比，DEFN引入了专门的频域滤波(`FuGH`)、简化的3D空间注意力(`S3DSA`)和通道注意力(`HSE`)，并配合专门针对稀缺目标的数据增强(`SDi`)和动态损失(`DWC`)，形成了一个为边界模糊医学图像分割任务量身定制的解决方案。
- **论文类型特化（医学类）**：
    - **任务类型**：三维体素级语义分割。
    - **图像模态**：主要面向光学相干断层扫描（OCT）和血管内超声（IVUS）等医学图像。
    - **数据集**：自建`CARS-30k`数据集用于预训练，公开`OIMHS`数据集用于评估和微调。
    - **临床意义**：旨在辅助医生精确量化黄斑裂孔等病变的大小、位置和形状，从而指导分类、制定手术方案（如填充物类型和剂量）并评估疗效 (p.3)。
## 实验

- **使用的数据集**：
    - **`CARS-30k`**：作者历时五年构建的大规模视网膜分割数据集，用于模型预训练 (p.4)。
    - **`OIMHS`**：公开的黄斑分割数据集，用于模型微调和最终性能评估 (p.4, 7)。
- **对比方法**：论文中提到与13个基线模型进行了对比 (p.4)，但具体模型列表在提供的文本中未列出。
- **评价指标**：PDF文本中未明确列出所使用的具体评价指标（如Dice系数、IoU等）。仅提到“achieves SOTA performance” (p.2)。
- **主实验结果**：文本指出DEFN在`OIMHS`数据集上达到了“SOTA性能”，但**未提供具体的数值结果**。
- **消融实验**：在提供的文本中未找到相关描述。
- **泛化实验**：在提供的文本中未找到相关描述。
- **速度/参数量/FLOPs等效率信息**：PDF文本中未提供。
## 局限

1.  **场景依赖性**：方法专门针对边界模糊、噪声大的医学目标设计，可能不适用于边界清晰、结构简单的分割任务。
2.  **实验充分性**：基于提供的文本，实验部分缺乏细节（具体指标、消融分析、效率比较），难以全面评估模型的有效性和效率。性能宣称为SOTA，但缺乏具体数字佐证。
3.  **数据集局限**：核心评估仅在`OIMHS`一个公开数据集上进行，虽然也使用了自建的`CARS-30k`进行预训练，但模型的跨模态、跨疾病泛化能力未知。
4.  **计算成本未知**：双编码器结构、3D卷积以及频域操作可能带来较高的计算复杂度和显存消耗，但文中未提及。
5.  **假设与依赖**：`SDi`增强依赖于对目标形状的先验建模（如模拟黄斑裂孔），其生成样本的真实性对下游任务的影响值得探究。三维重建部分依赖分割结果的准确性。
## 个人评论

1.  **问题导向的模块设计**：`FuGH`（频域滤波去噪）、`S3DSA`（空间注意力聚焦）、`HSE`（通道特征选择）三个模块的设计都紧密围绕解决“噪声”和“边界模糊”这两个核心痛点，具有明确的物理或功能意义，而非单纯堆砌模块。
2.  **端到端的系统方案**：论文没有局限于网络结构，而是从数据（`SDi`增强）、模型（`DEFN`网络）、训练策略（`DWC`动态损失）到应用（三维重建）提出了一个完整的流程。特别是`SDi`为解决小样本、稀缺类别问题提供了一个具体可行的思路。
3.  **动态损失组合的思路**：`DWC`策略承认不同损失函数在不同训练阶段的重要性可能变化，并尝试让模型自动调整，这种自适应训练的思路对研究者设计训练策略有启发。
4.  **对后续研究的启发**：在医学图像处理中，可以更多地探索**频域（傅里叶变换）与空间、通道注意力机制的多维度结合**，以同时实现去噪和特征增强。`SDi`的模拟缺陷注入思想也可以迁移到其他存在稀缺异常样本的领域。

### 使用建议

- **如果快速了解**：重点阅读 **Abstract** 和 **1. Introduction**，它们清晰阐述了问题和核心贡献。**3. Method** 部分的开头和各小节概述也能快速了解方法框架。
- **如果复现**：必须仔细研读 **3. Method** 整个章节（特别是3.1 SDi、3.2 FuGH、3.3 S3DSA、3.4 DWC），并结合**Fig. 2**的框架图理解模块连接。实验细节需要查阅论文后续未提供的部分。
- **如果借鉴创新点**：
    - **`FuGH`模块**：学习其如何将频域变换（FFT）与分组卷积结合进行特征处理。
    - **`S3DSA`模块**：学习其如何设计一个轻量的3D空间注意力机制。
    - **`DWC`策略**：学习其动态融合多个损失函数的实现思路。
    - **`SDi`增强**：学习如何针对特定稀缺目标设计模拟数据增强的策略。
- **如果写Related Work**：可将本文置于“**频域信息融合在深度学习中的应用**”、“**医学图像分割中的注意力机制**”、“**小样本或数据稀缺下的医学图像分析**”以及“**三维医学图像分割**”这几个相关工作类别中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**医学图像分割**方向，具体聚焦于**三维边界模糊目标**的精确分割。它针对医学成像中因噪声干扰、样本稀缺和目标边界不清晰（如黄斑裂孔、下咽癌）导致的分割难题，提出了一个结合频域滤波和注意力机制的深度学习网络。根据用户提供的`primary_topic: B_注意力算子模块`以及论文中`FuGH`、`S3DSA`和`HSE`三个核心模块的名称与设计，本文非常适合作为**注意力算子模块**主题下的一个具体案例，展示了如何在医学图像分割网络中集成频域、空间和通道维度的注意力机制。

## 2. 一句话总结
针对医学图像中边界模糊目标的分割难题，本文提出了一个包含频域滤波、空间注意力和通道注意力模块的`DEFN`网络，配合`SDi`数据增强和`DWC`动态损失策略，在`OIMHS`数据集上达到了先进水平。

## 3. 背景与问题
- **为什么做**：医学图像中许多重要目标（如黄斑裂孔、下咽癌）具有边界模糊、难以辨识的特点。精确分割这些目标对于诊断、手术规划和疗效评估至关重要，但现有方法效果不佳 (p.1-2)。
- **之前方法的问题**：
    1.  **数据稀缺与噪声干扰**：可用数据集中代表性样本不足，且成像存在噪声伪影，限制了数据驱动模型的性能 (p.1)。
    2.  **现有技术局限**：传统方法和深度学习模型在应对具有“概念性边界”（如黄斑裂孔的上边界需推断）或被阴影遮挡的区域时表现不佳 (p.1-2)。
    3.  **损失函数单一**：常用的损失函数（如Dice loss, Cross-entropy loss）通常在特定方面（如边界、类别不平衡）有效，但缺乏普适性，无法完美应对所有分割挑战 (p.6)。
- **核心矛盾**：如何在**训练数据稀缺且质量不高（噪声大、边界模糊）** 的约束下，实现对**三维医学图像中边界模糊目标的精确、鲁棒分割**。

## 4. 核心贡献
1.  **提出`SDi`数据增强技术**：通过序列扩展和模拟缺陷注入（孤立注入与综合注入两种策略），专门用于人工增加稀缺的边界模糊目标（如黄斑裂孔）的样本多样性，缓解数据不足问题 (p.3, 7-8)。
2.  **提出`DEFN`分割网络**：这是一个双编码器网络，其核心创新在于集成了三个关键模块：
    - **`FuGH`模块**：通过频域组卷积增强对周期性模式的识别，实现噪声抑制和特征增强。
    - **`S3DSA`模块**：简化的3D空间注意力，通过调整空间区域信息权重来增强模型对关键区域（如病灶）的聚焦能力。
    - **`HSE`模块**：谐波挤压激励模块，通过学习复杂的通道间权重模式来精确强调关键特征 (p.4)。
3.  **提出`DWC`动态权重合成损失策略**：一种网络优化策略，允许根据训练进程动态融合和调整多个损失函数，以适应不同训练阶段的需求，从而提升分割精度和鲁棒性 (p.4)。
4.  **开发三维重建方案**：基于分割结果，能够对视网膜结构进行精确建模和定量分析 (p.4)。

## 5. 方法详解
- **整体框架**：如图2 (p.2) 所示，项目流程包含一个利用`SDi`进行数据增强的管道、`DEFN`模型的预训练和微调阶段，以及最终的分割推理管道。
- **输入与输出**：输入为1通道的三维医学图像（尺寸`1×W×H×D`），输出为`C`通道的三维分割图（尺寸`C×W×H×D`）。
- **关键模块详解**：
    1.  **`FuGH`（傅里叶组谐波）模块**：这是频域注意力或处理的核心。论文描述其通过“频域组卷积”来增强对周期性模式的识别，从而抑制噪声、增强细节特征并提供更广的全局感受野 (p.4, 6)。
    2.  **`S3DSA`（简化3D空间注意力）模块**：这是空间注意力模块。其作用是通过“调整空间区域信息的权重”，让模型更专注于图像中的关键区域（如边界模糊的病灶），从而提高识别精度 (p.4)。
    3.  **`HSE`（谐波挤压激励）模块**：这是通道注意力模块。它通过“学习复杂的通道间权重模式”，实现对关键特征的精确加权强调 (p.4)。
- **模块连接**：根据图2的架构图，`FuGH`、`HSE`和`Norm`（归一化）在编码器和解码器的主分支中交替使用。`S3DSA`（图中标注为“Simplified 3D Spatial Attention”）可能作用于特征图，其具体位置在文本描述中未详述，但根据功能推断可能在编码器后或与解码器特征结合。
- **训练方式**：采用两阶段训练。首先使用大型的`CARS-30k`数据集进行**预训练**，然后使用目标数据集（如OIMHS中的黄斑裂孔数据）进行**微调** (p.2)。损失函数使用了`DWC`策略动态组合了多种损失，包括边界损失(`Boundary`)、Dice损失(`Dice`)、交叉熵损失(`CE`)、焦点损失(`Focal`)、深度排序损失(`DeepRanking`)和DWC损失自身 (p.2)。
- **推理流程**：输入一张三维图像，经过训练好的`DEFN`网络前向传播，输出像素级的类别预测，得到分割结果。该结果还可用于后续的三维重建 (p.4)。
- **与已有方法的差异**：与传统3D U-Net等相比，DEFN引入了专门的频域滤波(`FuGH`)、简化的3D空间注意力(`S3DSA`)和通道注意力(`HSE`)，并配合专门针对稀缺目标的数据增强(`SDi`)和动态损失(`DWC`)，形成了一个为边界模糊医学图像分割任务量身定制的解决方案。
- **论文类型特化（医学类）**：
    - **任务类型**：三维体素级语义分割。
    - **图像模态**：主要面向光学相干断层扫描（OCT）和血管内超声（IVUS）等医学图像。
    - **数据集**：自建`CARS-30k`数据集用于预训练，公开`OIMHS`数据集用于评估和微调。
    - **临床意义**：旨在辅助医生精确量化黄斑裂孔等病变的大小、位置和形状，从而指导分类、制定手术方案（如填充物类型和剂量）并评估疗效 (p.3)。

## 6. 实验与结果
- **使用的数据集**：
    - **`CARS-30k`**：作者历时五年构建的大规模视网膜分割数据集，用于模型预训练 (p.4)。
    - **`OIMHS`**：公开的黄斑分割数据集，用于模型微调和最终性能评估 (p.4, 7)。
- **对比方法**：论文中提到与13个基线模型进行了对比 (p.4)，但具体模型列表在提供的文本中未列出。
- **评价指标**：PDF文本中未明确列出所使用的具体评价指标（如Dice系数、IoU等）。仅提到“achieves SOTA performance” (p.2)。
- **主实验结果**：文本指出DEFN在`OIMHS`数据集上达到了“SOTA性能”，但**未提供具体的数值结果**。
- **消融实验**：在提供的文本中未找到相关描述。
- **泛化实验**：在提供的文本中未找到相关描述。
- **速度/参数量/FLOPs等效率信息**：PDF文本中未提供。

## 7. 这篇论文真正有价值的地方
1.  **问题导向的模块设计**：`FuGH`（频域滤波去噪）、`S3DSA`（空间注意力聚焦）、`HSE`（通道特征选择）三个模块的设计都紧密围绕解决“噪声”和“边界模糊”这两个核心痛点，具有明确的物理或功能意义，而非单纯堆砌模块。
2.  **端到端的系统方案**：论文没有局限于网络结构，而是从数据（`SDi`增强）、模型（`DEFN`网络）、训练策略（`DWC`动态损失）到应用（三维重建）提出了一个完整的流程。特别是`SDi`为解决小样本、稀缺类别问题提供了一个具体可行的思路。
3.  **动态损失组合的思路**：`DWC`策略承认不同损失函数在不同训练阶段的重要性可能变化，并尝试让模型自动调整，这种自适应训练的思路对研究者设计训练策略有启发。
4.  **对后续研究的启发**：在医学图像处理中，可以更多地探索**频域（傅里叶变换）与空间、通道注意力机制的多维度结合**，以同时实现去噪和特征增强。`SDi`的模拟缺陷注入思想也可以迁移到其他存在稀缺异常样本的领域。

## 8. 局限与问题
1.  **场景依赖性**：方法专门针对边界模糊、噪声大的医学目标设计，可能不适用于边界清晰、结构简单的分割任务。
2.  **实验充分性**：基于提供的文本，实验部分缺乏细节（具体指标、消融分析、效率比较），难以全面评估模型的有效性和效率。性能宣称为SOTA，但缺乏具体数字佐证。
3.  **数据集局限**：核心评估仅在`OIMHS`一个公开数据集上进行，虽然也使用了自建的`CARS-30k`进行预训练，但模型的跨模态、跨疾病泛化能力未知。
4.  **计算成本未知**：双编码器结构、3D卷积以及频域操作可能带来较高的计算复杂度和显存消耗，但文中未提及。
5.  **假设与依赖**：`SDi`增强依赖于对目标形状的先验建模（如模拟黄斑裂孔），其生成样本的真实性对下游任务的影响值得探究。三维重建部分依赖分割结果的准确性。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读 **Abstract** 和 **1. Introduction**，它们清晰阐述了问题和核心贡献。**3. Method** 部分的开头和各小节概述也能快速了解方法框架。
- **如果复现**：必须仔细研读 **3. Method** 整个章节（特别是3.1 SDi、3.2 FuGH、3.3 S3DSA、3.4 DWC），并结合**Fig. 2**的框架图理解模块连接。实验细节需要查阅论文后续未提供的部分。
- **如果借鉴创新点**：
    - **`FuGH`模块**：学习其如何将频域变换（FFT）与分组卷积结合进行特征处理。
    - **`S3DSA`模块**：学习其如何设计一个轻量的3D空间注意力机制。
    - **`DWC`策略**：学习其动态融合多个损失函数的实现思路。
    - **`SDi`增强**：学习如何针对特定稀缺目标设计模拟数据增强的策略。
- **如果写Related Work**：可将本文置于“**频域信息融合在深度学习中的应用**”、“**医学图像分割中的注意力机制**”、“**小样本或数据稀缺下的医学图像分析**”以及“**三维医学图像分割**”这几个相关工作类别中。

## 10. 和其他论文的关系
根据`primary_topic: B_注意力算子模块`及论文内容，本文可能与其他包含注意力机制的分割网络相关。但由于库里具体论文未知，仅根据常识推测可能相关的工作类型：
- `[[FuGH]]` 模块涉及傅里叶变换，与基于 `FFT` 的 `[[Fast Fourier Convolution]]` 或 `[[LCSeg-Net]]` (p.6) 等工作相关。
- `[[S3DSA]]` 是空间注意力，与 `[[CBAM]]` (Convolutional Block Attention Module) 等空间注意力模块相关。
- `[[HSE]]` 是通道注意力，与 `[[SENet]]` (Squeeze-and-Excitation Network) 等工作相关。
- 整体网络结构基于编码器-解码器，与 `[[3D U-Net]]` (p.5) 相关。
*(注：由于不确定其他论文的具体存在，此部分仅作形式示范，未使用`[[]]`进行链接)*

## 11. 关键词
三维分割, 边界模糊, 黄斑裂孔, 频域谐波 (FuGH), 空间注意力 (S3DSA), 通道注意力 (HSE), 数据增强 (SDi), 动态损失 (DWC), 医学图像分割, 下咽癌, OCT图像

## 12. 可信度说明
本精读笔记主要基于提供的PDF文本的前12页内容生成，该部分完整覆盖了**摘要 (Abstract)**、**引言 (Introduction)**、**相关工作 (Related Work)** 和**方法 (Method)** 章节。笔记中对论文动机、核心贡献、模型框架、关键模块(`FuGH`, `S3DSA`, `HSE`, `SDi`, `DWC`)的原理描述均直接引自文本，具有高可信度。
然而，由于提取文本不完整（仅前12/36页），**实验与结果 (Experiments)** 章节的具体数据（如对比基线、评价指标数值、消融实验结果）在提供的文本中缺失，因此笔记中该部分的信息相对简略。后续章节（如详细实验设置、更多结果讨论、结论）的完整信息有待查阅全文。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/HSE&FuGH&S3DSA.txt` (36/36 页; 原 AI 主体 12/36 + 全文补读 13-36); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-36; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-36。
- **提取情况**: 缺失页 24 页, 其中 24 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: DropPath
- p.13: SE Block
- p.13: 2 FUGH Block
- p.13: The SE block is a dynamic recalibration module that enhances the representation ability by adaptively recalibrating
- p.13: Specifically, by focusing on the feature channels that distinctly represent the macular hole and macular edema, and
- p.13: The HSE module integrates a FuGH module and the SE block to constitute an advanced feature extraction and
- p.13: Gaussian Error Linear Unit, which is a specific type of activation function employed to introduce non-linearity in the
- p.14: 3.3. Dynamic Weight Composing
- p.14: Conventional loss functions are inadequate to accommodate the complexity of segmenting fuzzy boundary objects
- p.14: To overcome these limitations, we propose an innovative network optimization strategy, namely, the dynamic
- p.14: LBoundary : To emphasize the accuracy of segmenting objects with conceptual boundary, LBoundary is introduced
- p.15: LDeepRanking : To further improve the segmentation performance of the model, LDeepRanking is introduced into the

### 缺失页关键摘录

- p.13: processing unit, as illustrated in Fig.7. For an input x, it goes through the following process:
- p.14: portance of hard-to-classify samples, the target is the result after one-hot encoding of the ground truth, Nis the total
- p.14: LBoundary : To emphasize the accuracy of segmenting objects with conceptual boundary, LBoundary is introduced
- p.16: The DEFN is evaluated on the OIMHS [7] dataset. A subset of OIMHS serves as the test set, while the remainder,
- p.16: The OCT Image Macular Hole Segmentation (OIMHS) dataset is a publicly accessible retinal OCT segmentation
- p.16: repository, distinguished by its composition of 3,859 B-scan SD-OCT images featuring macular holes. This dataset
- p.16: choroid, with the choroid category not considered in this experiment.
- p.16: A multicentre dataset from the retinal OCT scans of patients was collected, named Comprehensive Archive for
- p.16: retinal research. The CARS-30k dataset encompasses 30,684 B-scan SD-OCT images, carefully annotated, depicting
- p.16: ing, followed by a validation step executed by two senior retinal specialists to ascertain the accuracy and consistency
- p.16: Some statistics of the two datasets are given in Table 1.
- p.16: Table 1: Detailed information of OIMHS and CARS-30k, including patient number, sequence number, and slice number.
<!-- AI_READING_NOTE_END -->
