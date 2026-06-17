---
title: A Progressive Image Restoration Network for
authors:
  - "Yujie Feng"
  - "Yin Yang"
  - "Xiaohong Fan"
  - "Zhengpeng Zhang"
  - "Lijing Bu"
  - "Jianping Zhang"
year: 2024
venue: "ACCEPTEDTOIEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,JULY,2025. DOI:10.1109/TGRS.2025.35907531"
doi: 10.1109/TGRS.2025.35907531
pdf: [[2024_A_Progressive_Image.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
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
extract_cache: .paper-cache/extracts/2024_A_Progressive_Image.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# A Progressive Image Restoration Network for

## 基本信息
- **PDF**: [[2024_A_Progressive_Image.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A Progressive Image Restoration Network for |
| **作者** | Yujie Feng; Yin Yang; Xiaohong Fan; Zhengpeng Zhang; Lijing Bu; Jianping Zhang |
| **发表时间** | 2024 |
| **刊物/会议** | ACCEPTEDTOIEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,JULY,2025. DOI:10.1109/TGRS.2025.35907531 |
| **DOI** | 10.1109/TGRS.2025.35907531 |

## 摘要

> —Recently, deep learning methods have gained re- application in high-level remote sensing tasks directly. To markable achievements in the field of image restoration for address this problem efficiently with minimal cost, employing remotesensing(RS).However,mostexistingRSimagerestoration image restoration techniques is optimal, as it avoids the need methods focus mainly on conventional first-order degradation forupgradingequipment.Thesetechniquesreconstructahigh- models, which may not effectively capture the imaging mecha- nisms of remote sensing images. Furthermore, many RS image resolution (HR) image, enriched with detailed high-frequency restorationapproachesthatusedeeplearningareoftencriticized textures,fromalow-resolution(LR)image.Asaresult,image for their lacks of architecture transparency and model inter- restoration has become increasingly popular in the fields of pretability. To address these problems, we propose a novel pro- remote sensing and computer vision. gressiverestorat

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：遥感图像在成像过程中不可避免地会退化，影响其在下游任务中的应用。现有的深度学习图像恢复方法虽然性能强大，但存在诸多问题。
- **之前方法的问题**：
    1. **退化模型过于简单**：大多数方法聚焦于传统的一阶退化模型（仅包含模糊、下采样、噪声），无法有效捕获遥感图像真实的高阶复杂退化机制（如大气传输、传感器系统、平台抖动等）。
    2. **模型缺乏可解释性**：许多端到端的深度学习方法是“黑盒”的，难以解释网络架构如何影响其预测，透明度与可解释性不足。
    3. **网络设计效率问题**：一些方法通过堆叠更深、更宽的网络来提升性能，导致计算量增大，且网络架构设计的智能性不足。
- **核心矛盾**：如何在提升遥感图像恢复性能的同时，增强基于物理成像机制的深度学习模型的可解释性。
## 关键贡献

1. **提出HD1-PRNet框架**：构建了一个基于反向马尔可夫过程的高阶渐进式遥感图像恢复网络（HDI-PRNet）。该框架将复杂的退化机制建模为马尔可夫链，通过对齐反向退化任务与相应模块，使模型更透明、更具可解释性。
2. **开发近端映射先验学习去噪模块**：利用多尺度编码器-解码器学习和注意力机制，开发了一个基于近端映射算子学习的去噪模块，在每个阶段强调关键的去噪先验细节并保留精细信息。
3. **设计双域退化学习去模糊模块**：设计了一个去模糊模块，该模块结合了诺伊曼（Neumann）级数展开与双域（空间域和频域）退化学习模块，从而有效获取模糊退化算子的先验知识，实现双域表示的融合。
4. **实验验证有效性**：通过大量实验确认，HD1-PRNet框架在各种随机退化的合成低分辨率图像和真实遥感图像上均能获得高质量的恢复结果。
## 方法

### 整体框架
本文提出了HDI-PRNet（High-order Degradation Imaging Progressive Restoration Network）。其核心思想源于将高阶退化过程建模为马尔可夫链，并通过最大后验概率（MAP）估计进行反向求解。整体框架如图1(a)所示，包含k个阶段，每个阶段对应高阶退解模型中的一步反向过程（公式8）。每个阶段内部又由三个模块组成，分别对应求解能量最小化模型（公式12）分解出的三个子问题（公式13-15）。

### 输入与输出
- **输入**：退化观测图像`g_ℓ`（第ℓ阶段的输入）。
- **输出**：恢复的图像`g_{ℓ-1}`（第ℓ阶段的输出），最终目标是得到原始干净图像`g_0`。

### 关键模块
1.  **图像去噪模块**：
    - **作用**：求解子问题(13)，即从退化图像`g_ℓ`中去除噪声，得到去噪后的图像`g^dn_ℓ`。
    - **机制**：该模块通过学习一个**近端映射算子**（公式16）来实现。它被设计为一个**多尺度编码器-解码器网络**，并利用**残差通道注意力块（RCAB）** 来提取特征。网络通过中间损失监督，确保其专注于去噪任务。

2.  **超分辨率（SR）模块**：
    - **作用**：求解子问题(14)，即将去噪图像`g^dn_ℓ`的分辨率提升，得到超分辨率图像`g^sr_ℓ`。
    - **机制**：模块结构相对简单，包含卷积层和**双三次插值**上采样层，旨在利用多尺度表示来改善图像质量。

3.  **图像去模糊模块**：
    - **作用**：求解子问题(15)，即对超分辨率图像`g^sr_ℓ`进行去模糊，得到第ℓ阶段的最终恢复结果`g_{ℓ-1}`。
    - **机制**：该模块是创新核心。它没有直接学习一个复杂的反向算子`B⁻¹`，而是通过**诺伊曼级数展开**来近似求解。网络由多个**双域退化学习块（DDLB）** 堆叠而成，每个块对应级数展开的一项。DDLB内部包含**空间交互聚合（SIA）** 和**频域交互聚合（CIA）** 子模块，并利用**快速傅里叶变换（RFFT/IRFFT）** 来在空间域和频域同时学习退化特性，实现双域融合。

### 模块连接方式
三个模块在每个阶段内是**顺序连接**的：输入`g_ℓ` → 去噪模块 → 超分辨率模块 → 去模糊模块 → 输出`g_{ℓ-1}`。整个框架通过k个这样的阶段**级联**，逐步反向恢复图像。

### 数学公式与机制直观解释
- **理论基础**：高阶退化被建模为马尔可夫链（公式5），其反向过程通过MAP估计（公式7）求解。
- **优化求解**：最终的能量最小化问题（公式12）被分解为三个更易处理的子问题：去噪、超分、去模糊。
- **直观解释**：整个过程好比修复一幅层层损坏的名画。首先小心翼翼地扫除灰尘（去噪），然后仔细放大细节（超分），最后修正因潮湿等原因产生的模糊（去模糊）。每一层损坏（退化）都被这样依次“剥离”和修复。

### 训练方式
- 采用**多监督损失函数**。在每个阶段的每个模块输出后，都计算损失（如图1(a)中的`Loss`所示）。这种中间监督有助于引导各模块学习对应的子任务，并加速训练收敛。

### 推理流程
推理时，给定一张退化图像`g_k`（即`g`），从第k阶段开始，依次通过去噪、超分、去模糊模块得到`g_{k-1}`，然后将`g_{k-1}`作为第k-1阶段的输入，重复此过程，直到第1阶段结束，最终输出恢复的图像`g_0`。

### 和已有方法的差异
1.  **模型驱动 vs. 数据驱动**：不同于纯粹数据驱动的黑盒网络（如RCAN, SwinIR），本方法严格基于物理退化模型（高阶退化）和优化理论（MAP估计）进行网络架构设计，具有明确的数学可解释性。
2.  **渐进式 vs. 端到端**：采用渐进式恢复，逐步处理不同层次的退化，而非一次性完成恢复，这更符合物理退解过程。
3.  **双域去模糊**：去模糊模块创新性地结合了诺伊曼级数展开和双域学习，比单纯在空域或频域学习的去模糊方法更具表达能力。
## 实验

由于提供的PDF文本仅包含前12页，实验与结果部分（Section IV）的内容不完整。以下信息根据已有文本整理：

- **使用的数据集**：文本中提到在“各种随机退化的合成低分辨率图像和真实遥感图像”上进行实验。具体数据集名称在提供的文本中未明确列出。
- **对比方法**：未在提供的文本中列出具体对比的算法名称。
- **评价指标**：未在提供的文本中明确列出，但通常此类工作使用PSNR、SSIM等指标。
- **主实验结果**：文本中仅提到“实验结果确认...可以获得高质量的恢复图像”，并指出在“真实遥感应用”中性能提升显著。具体数字（如PSNR/SSIM值）在提供的文本中未找到。
- **消融实验**：文本提到“在第IV节分析实验结果和消融实验”，但具体内容未包含在提供的文本中。
- **泛化实验**：同样，在“真实远程感应图像”上进行了实验，但具体结果未提供。
- **速度/参数量/FLOPs**：在提供的文本中未找到相关信息。
## 局限

- **场景限制**：方法基于马尔可夫链假设，将退化过程分解为一系列顺序的一阶退化。对于非顺序或非马尔可夫特性的复杂退化，该模型的适用性可能受限。
- **实验不完整**：根据提供的文本，详细的实验结果、消融研究和对比分析部分缺失，无法全面评估该方法的具体性能优势、各模块的实际贡献以及计算效率。
- **退化先验依赖**：网络的每个阶段被设计为解决特定类型的退化（去噪、去模糊、超分）。对于退化类型未知或顺序错乱的真实图像，其效果可能受到影响。
- **计算成本**：框架包含k个阶段，每个阶段有多个复杂模块（如DDLB），整体计算复杂度和推理时间可能较高，尽管文本中未提供具体数据。
- **复现风险**：论文涉及复杂的模块设计（如DDLB、CIA、SIA）和特定的训练策略（多阶段监督），完整复现需要细致的工程实现。
## 个人评论

1.  **物理模型与深度学习的优雅结合**：本文最大的价值在于展示了一种如何将领域物理知识（遥感成像退化模型）与深度学习强大拟合能力相结合的范式。它不是简单地用网络拟合数据，而是用网络去实现一个基于物理模型的优化求解过程，这为提升模型可解释性和泛化性提供了重要思路。
2.  **渐进式框架的启示**：将复杂问题分解为多个子问题并逐步解决的思路，不仅符合物理过程，也使得网络设计更模块化、更易于调试和理解。
3.  **双域退化学习的有效性**：在去模糊模块中同时利用空间域和频域信息是一个实用且有效的设计思路，对于其他需要处理模糊、振铃效应的图像复原任务有借鉴意义。
4.  **对遥感图像恢复的针对性**：明确针对遥感图像的高阶退化问题进行建模，比通用图像超分方法更贴近实际应用场景，对相关领域的研究者有直接参考价值。

### 使用建议

- **如果快速了解**：重点阅读**摘要**和**引言（Section I）**，可以快速掌握论文要解决的问题、核心思想和主要贡献。
- **如果复现**：需要仔细精读**方法部分（Section III）**，特别是对公式(12)-(15)的分解、图1的框架和各个子模块的详细设计描述。同时，必须寻找并仔细阅读完整的论文原文，以获取详细的实验设置、超参数和训练细节。
- **如果借鉴创新点**：
    - 学习其**“基于物理模型设计网络”** 的思路，思考如何将自己领域的先验知识转化为网络结构。
    - 借鉴其**渐进式/分阶段处理**的框架设计思想。
    - 参考其**双域（空间+频域）特征学习**模块（DDLB）的设计。
- **如果写Related Work**：可以将其放在以下类别中：“基于模型的深度展开网络（Deep Unfolding Networks）”、“遥感图像恢复（Remote Sensing Image Restoration）”、“高阶/复杂退化图像恢复（High-order/Complex Degradation Image Restoration）”。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉与遥感图像处理领域，具体方向为图像恢复/超分辨率。它旨在解决遥感图像因复杂成像环境导致的高阶退化（如模糊、噪声、下采样等复合退化）问题。该论文适合放在“基于模型的深度展开网络”和“遥感图像恢复”主题下。

## 2. 一句话总结
本文提出了一个名为HDI-PRNet的渐进式恢复网络，通过将高阶退化建模为反向马尔可夫过程，并利用最大后验概率（MAP）估计理论进行深度展开，设计去噪、去模糊和超分辨率三个模块，以逐步恢复不同层次的退化，从而提升遥感图像恢复的性能和模型可解释性。

## 3. 背景与问题
- **为什么要做**：遥感图像在成像过程中不可避免地会退化，影响其在下游任务中的应用。现有的深度学习图像恢复方法虽然性能强大，但存在诸多问题。
- **之前方法的问题**：
    1. **退化模型过于简单**：大多数方法聚焦于传统的一阶退化模型（仅包含模糊、下采样、噪声），无法有效捕获遥感图像真实的高阶复杂退化机制（如大气传输、传感器系统、平台抖动等）。
    2. **模型缺乏可解释性**：许多端到端的深度学习方法是“黑盒”的，难以解释网络架构如何影响其预测，透明度与可解释性不足。
    3. **网络设计效率问题**：一些方法通过堆叠更深、更宽的网络来提升性能，导致计算量增大，且网络架构设计的智能性不足。
- **核心矛盾**：如何在提升遥感图像恢复性能的同时，增强基于物理成像机制的深度学习模型的可解释性。

## 4. 核心贡献
1. **提出HD1-PRNet框架**：构建了一个基于反向马尔可夫过程的高阶渐进式遥感图像恢复网络（HDI-PRNet）。该框架将复杂的退化机制建模为马尔可夫链，通过对齐反向退化任务与相应模块，使模型更透明、更具可解释性。
2. **开发近端映射先验学习去噪模块**：利用多尺度编码器-解码器学习和注意力机制，开发了一个基于近端映射算子学习的去噪模块，在每个阶段强调关键的去噪先验细节并保留精细信息。
3. **设计双域退化学习去模糊模块**：设计了一个去模糊模块，该模块结合了诺伊曼（Neumann）级数展开与双域（空间域和频域）退化学习模块，从而有效获取模糊退化算子的先验知识，实现双域表示的融合。
4. **实验验证有效性**：通过大量实验确认，HD1-PRNet框架在各种随机退化的合成低分辨率图像和真实遥感图像上均能获得高质量的恢复结果。

## 5. 方法详解
### 整体框架
本文提出了HDI-PRNet（High-order Degradation Imaging Progressive Restoration Network）。其核心思想源于将高阶退化过程建模为马尔可夫链，并通过最大后验概率（MAP）估计进行反向求解。整体框架如图1(a)所示，包含k个阶段，每个阶段对应高阶退解模型中的一步反向过程（公式8）。每个阶段内部又由三个模块组成，分别对应求解能量最小化模型（公式12）分解出的三个子问题（公式13-15）。

### 输入与输出
- **输入**：退化观测图像`g_ℓ`（第ℓ阶段的输入）。
- **输出**：恢复的图像`g_{ℓ-1}`（第ℓ阶段的输出），最终目标是得到原始干净图像`g_0`。

### 关键模块
1.  **图像去噪模块**：
    - **作用**：求解子问题(13)，即从退化图像`g_ℓ`中去除噪声，得到去噪后的图像`g^dn_ℓ`。
    - **机制**：该模块通过学习一个**近端映射算子**（公式16）来实现。它被设计为一个**多尺度编码器-解码器网络**，并利用**残差通道注意力块（RCAB）** 来提取特征。网络通过中间损失监督，确保其专注于去噪任务。

2.  **超分辨率（SR）模块**：
    - **作用**：求解子问题(14)，即将去噪图像`g^dn_ℓ`的分辨率提升，得到超分辨率图像`g^sr_ℓ`。
    - **机制**：模块结构相对简单，包含卷积层和**双三次插值**上采样层，旨在利用多尺度表示来改善图像质量。

3.  **图像去模糊模块**：
    - **作用**：求解子问题(15)，即对超分辨率图像`g^sr_ℓ`进行去模糊，得到第ℓ阶段的最终恢复结果`g_{ℓ-1}`。
    - **机制**：该模块是创新核心。它没有直接学习一个复杂的反向算子`B⁻¹`，而是通过**诺伊曼级数展开**来近似求解。网络由多个**双域退化学习块（DDLB）** 堆叠而成，每个块对应级数展开的一项。DDLB内部包含**空间交互聚合（SIA）** 和**频域交互聚合（CIA）** 子模块，并利用**快速傅里叶变换（RFFT/IRFFT）** 来在空间域和频域同时学习退化特性，实现双域融合。

### 模块连接方式
三个模块在每个阶段内是**顺序连接**的：输入`g_ℓ` → 去噪模块 → 超分辨率模块 → 去模糊模块 → 输出`g_{ℓ-1}`。整个框架通过k个这样的阶段**级联**，逐步反向恢复图像。

### 数学公式与机制直观解释
- **理论基础**：高阶退化被建模为马尔可夫链（公式5），其反向过程通过MAP估计（公式7）求解。
- **优化求解**：最终的能量最小化问题（公式12）被分解为三个更易处理的子问题：去噪、超分、去模糊。
- **直观解释**：整个过程好比修复一幅层层损坏的名画。首先小心翼翼地扫除灰尘（去噪），然后仔细放大细节（超分），最后修正因潮湿等原因产生的模糊（去模糊）。每一层损坏（退化）都被这样依次“剥离”和修复。

### 训练方式
- 采用**多监督损失函数**。在每个阶段的每个模块输出后，都计算损失（如图1(a)中的`Loss`所示）。这种中间监督有助于引导各模块学习对应的子任务，并加速训练收敛。

### 推理流程
推理时，给定一张退化图像`g_k`（即`g`），从第k阶段开始，依次通过去噪、超分、去模糊模块得到`g_{k-1}`，然后将`g_{k-1}`作为第k-1阶段的输入，重复此过程，直到第1阶段结束，最终输出恢复的图像`g_0`。

### 和已有方法的差异
1.  **模型驱动 vs. 数据驱动**：不同于纯粹数据驱动的黑盒网络（如RCAN, SwinIR），本方法严格基于物理退化模型（高阶退化）和优化理论（MAP估计）进行网络架构设计，具有明确的数学可解释性。
2.  **渐进式 vs. 端到端**：采用渐进式恢复，逐步处理不同层次的退化，而非一次性完成恢复，这更符合物理退解过程。
3.  **双域去模糊**：去模糊模块创新性地结合了诺伊曼级数展开和双域学习，比单纯在空域或频域学习的去模糊方法更具表达能力。

## 6. 实验与结果
由于提供的PDF文本仅包含前12页，实验与结果部分（Section IV）的内容不完整。以下信息根据已有文本整理：

- **使用的数据集**：文本中提到在“各种随机退化的合成低分辨率图像和真实遥感图像”上进行实验。具体数据集名称在提供的文本中未明确列出。
- **对比方法**：未在提供的文本中列出具体对比的算法名称。
- **评价指标**：未在提供的文本中明确列出，但通常此类工作使用PSNR、SSIM等指标。
- **主实验结果**：文本中仅提到“实验结果确认...可以获得高质量的恢复图像”，并指出在“真实遥感应用”中性能提升显著。具体数字（如PSNR/SSIM值）在提供的文本中未找到。
- **消融实验**：文本提到“在第IV节分析实验结果和消融实验”，但具体内容未包含在提供的文本中。
- **泛化实验**：同样，在“真实远程感应图像”上进行了实验，但具体结果未提供。
- **速度/参数量/FLOPs**：在提供的文本中未找到相关信息。

## 7. 这篇论文真正有价值的地方
1.  **物理模型与深度学习的优雅结合**：本文最大的价值在于展示了一种如何将领域物理知识（遥感成像退化模型）与深度学习强大拟合能力相结合的范式。它不是简单地用网络拟合数据，而是用网络去实现一个基于物理模型的优化求解过程，这为提升模型可解释性和泛化性提供了重要思路。
2.  **渐进式框架的启示**：将复杂问题分解为多个子问题并逐步解决的思路，不仅符合物理过程，也使得网络设计更模块化、更易于调试和理解。
3.  **双域退化学习的有效性**：在去模糊模块中同时利用空间域和频域信息是一个实用且有效的设计思路，对于其他需要处理模糊、振铃效应的图像复原任务有借鉴意义。
4.  **对遥感图像恢复的针对性**：明确针对遥感图像的高阶退化问题进行建模，比通用图像超分方法更贴近实际应用场景，对相关领域的研究者有直接参考价值。

## 8. 局限与问题
- **场景限制**：方法基于马尔可夫链假设，将退化过程分解为一系列顺序的一阶退化。对于非顺序或非马尔可夫特性的复杂退化，该模型的适用性可能受限。
- **实验不完整**：根据提供的文本，详细的实验结果、消融研究和对比分析部分缺失，无法全面评估该方法的具体性能优势、各模块的实际贡献以及计算效率。
- **退化先验依赖**：网络的每个阶段被设计为解决特定类型的退化（去噪、去模糊、超分）。对于退化类型未知或顺序错乱的真实图像，其效果可能受到影响。
- **计算成本**：框架包含k个阶段，每个阶段有多个复杂模块（如DDLB），整体计算复杂度和推理时间可能较高，尽管文本中未提供具体数据。
- **复现风险**：论文涉及复杂的模块设计（如DDLB、CIA、SIA）和特定的训练策略（多阶段监督），完整复现需要细致的工程实现。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**摘要**和**引言（Section I）**，可以快速掌握论文要解决的问题、核心思想和主要贡献。
- **如果复现**：需要仔细精读**方法部分（Section III）**，特别是对公式(12)-(15)的分解、图1的框架和各个子模块的详细设计描述。同时，必须寻找并仔细阅读完整的论文原文，以获取详细的实验设置、超参数和训练细节。
- **如果借鉴创新点**：
    - 学习其**“基于物理模型设计网络”** 的思路，思考如何将自己领域的先验知识转化为网络结构。
    - 借鉴其**渐进式/分阶段处理**的框架设计思想。
    - 参考其**双域（空间+频域）特征学习**模块（DDLB）的设计。
- **如果写Related Work**：可以将其放在以下类别中：“基于模型的深度展开网络（Deep Unfolding Networks）”、“遥感图像恢复（Remote Sensing Image Restoration）”、“高阶/复杂退化图像恢复（High-order/Complex Degradation Image Restoration）”。

## 10. 和其他论文的关系
根据主题`T_通用_NLP_其他`和文件名`2024_A_Progressive_Image.pdf`，可以推断可能相关的论文方向：
- **深度展开网络**：如基于半二次分裂（HQS）、ADMM等传统优化算法展开的网络，例如 `[[Deep Plug-and-Play Super-Resolution for Arbitrary Blur Kernels]]`、`[[Learning Deep CNN Denoiser Prior for Image Restoration]]`。
- **高阶退化模型**：如 `[[Real-World Super-Resolution via Kernel Estimation and Noise Injection]]` (BSRGAN)、`[[Designing a Practical Degradation Model for Deep Blind Image Super-Resolution]]` 等致力于模拟真实退化的工作。
- **双域图像恢复**：如 `[[Focal Frequency Loss for Image Reconstruction and Synthesis]]`、`[[Learning in the Frequency Domain]]` 等利用频域信息的工作。
- **遥感图像超分辨率**：众多针对遥感场景设计的网络，如 `[[LGCNet: A Novel Local-Global Combined Network for Remote Sensing Image Super-Resolution]]`、`[[A Novel Mixed High-Order Attention Network for Remote Sensing Image Super-Resolution]]` 等。

## 11. 关键词
高阶退化模型，图像恢复，马尔可夫过程，遥感图像，深度展开网络，近端映射，诺伊曼级数，双域学习，渐进式恢复，可解释性

## 12. 可信度说明
本精读笔记主要基于提供的PDF前12页文本生成，该部分包含了论文的标题、摘要、引言、相关工作、方法论的绝大部分内容（包括整体框架、三个核心模块的详细设计、数学推导）。**笔记的“方法详解”部分可信度高，内容详实。**
**主要局限性在于**：由于实验与结果部分（Section IV）和结论部分（Section V）的内容在提供的文本中缺失，因此“实验与结果”一节信息严重不全，“局限与问题”中关于实验充分性的分析也受限于此。此外，论文的图表信息（如图1）是通过文本描述复现的，可能丢失了部分视觉细节。整体而言，对于理解论文的核心思想和方法设计，本文提供的文本质量较高且足够。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2024_A_Progressive_Image.txt` (17/17 页; 原 AI 主体 12/17 + 全文补读 13-17); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: HDI-PRNet DAT
- p.13: TTST Patch SwinIR SwinIR(Bicubic) MHAN(Bicubic) MHAN Gaofen -2
- p.13: HDI-PRNet DATHDI-PRNet DAT
- p.13: TTST Patch SwinIR SwinIR(Bicubic) MHAN(Bicubic) MHAN Gaofen -1
- p.13: TTST Patch SwinIR SwinIR(Bicubic) MHAN(Bicubic) MHAN Gaofen -6
- p.13: TTST Patch SwinIR SwinIR(Bicubic) MHAN(Bicubic) MHAN Gaofen -7
- p.13: TTST Patch SwinIR SwinIR(Bicubic) MHAN(Bicubic) MHAN Jilin-1
- p.14: TABLE IX
- p.14: ClassCTNet HSENet D-DBPNRDN TransE- RCAN SAN MHAN SwinIR HAUNet TTST CAT RGT DAT HDI-
- p.14: results on real images from five different satellites. Although
- p.14: MHAN records the highest score on Jilin-1, its predictions are
- p.14: In this paper, we proposed a novel remote sensing high-

### 缺失页关键摘录

- p.14: COMPARISON OF DIFFERENT SR×4MODELS ON VARIOUS SCENE CLASSES OF UCM ERCED (PSNR ( dB)). T HE BEST AND SECOND -BEST RESULTS ARE
- p.14: in Table XI, HDI-PRNet achieves the best or second-best
- p.15: COMPARISON OF DIFFERENT SR×3MODELS ON VARIOUS SCENE CLASSES OF NWPU-RESISC45 (PSNR ( dB)). T HE BEST AND SECOND -BEST
- p.16: “Aid: A benchmark data set for performance evaluation of aerial scene
- p.16: M. Pelillo, and L. Zhang, “Dota: A large-scale dataset for object
- p.17: cation: Benchmark and state of the art,” Proceedings of the IEEE , vol.
<!-- AI_READING_NOTE_END -->
