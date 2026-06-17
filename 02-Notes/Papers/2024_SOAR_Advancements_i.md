---
title: "SOAR: Advancements in Small Body Object"
authors:
  - "Tushar Verma"
  - "Yash Bhartari"
  - "Rishi Jarwal"
  - "Suraj Singh"
  - "Shubhkarman Singh"
  - "Jyotsna Singh"
year: 2024
venue: it particularly effective in remote sensing image classification.
doi: 
pdf: [[2024_SOAR_Advancements_i.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2024_SOAR_Advancements_i.txt
---

# SOAR: Advancements in Small Body Object

## 基本信息
- **PDF**: [[2024_SOAR_Advancements_i.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SOAR: Advancements in Small Body Object |
| **作者** | Tushar Verma; Yash Bhartari; Rishi Jarwal; Suraj Singh; Shubhkarman Singh; Jyotsna Singh |
| **发表时间** | 2024 |
| **刊物/会议** | it particularly effective in remote sensing image classification. |
| **DOI** | 未明确 |

## 摘要

> significant challenges in computer vision due to the minimal because it was monitored from a distance. Their tiny size data inherent in small-sized objects and their propensity to be sometimesleadstothembeingconfusedfornoise,whichhasa obscured by larger objects and background noise. Traditional detrimental effect on tracking accuracy. The small objects can methods using transformer-based models often face limitations stemmingfromthelackofspecializeddatabases,whichadversely be defined as MS-COCO [1] metric evaluation, small objects affecttheirperformancewithobjectsofvaryingorientationsand are defined as having an area of 32 × 32 pixels or less, scales.Thisunderscorestheneedformoreadaptable,lightweight which is a commonly used threshold for datasets including models. In response, this paper introduces two innovative ap- commonobjects.Therehavebeensomemodelsthathavebeen proaches that significantly enhance detection and segmentation developed to help in the particular problem and continuou

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**: 航空影像中的小目标检测是自动驾驶、交通监控等应用的关键，但小目标信息少、易被背景噪声和遮挡影响，是当前目标检测领域的重大挑战。
- **之前方法的问题**:
    1. 基于Transformer的模型在处理不同方向和尺度的对象时性能受限，且需要专门的数据库。
    2. 传统的检测器（如Faster R-CNN, RetinaNet）多在低分辨率、包含大目标的数据集（如MS COCO）上训练，对高分辨率影像中的小目标检测效果不佳。
    3. 虽然多尺度特征融合等方法被应用，但网络加深会导致参数量和计算量增加，如何在保持精度的同时提升效率是关键。
    4. 定向目标检测（OBB）虽能改善定位，但并未专门针对“小尺寸”这一核心问题。
- **核心矛盾**: 需要在**有限的计算资源**下，设计出既能**有效提取小目标微弱特征**（对抗信息损失），又能**建模长距离全局上下文**，同时保持**实时性**的轻量化检测模型。
## 关键贡献

1. **将YOLOv9与SAHI框架结合**：首次在新型轻量级架构YOLOv9上部署SAHI，并应用于DOTA数据集，通过切片推理和微调提升小目标检测性能。
2. **提出SOAR框架**：设计了一个基于Vision Mamba架构的动态小目标检测框架，并进行了实验验证。该框架引入了**双向状态空间模型**进行视觉上下文建模。
3. **提出融合PGI与SSM的新框架**：提出了一个将**可编程梯度信息**（PGI）与**状态空间模型表示**相结合的框架，旨在为有效的视觉和计算机视觉任务提供新方案。
## 方法

- **整体框架 (SOAR encoder)**: 如图1所示，SOAR框架首先将2D图像分割成展平的2D patches，然后进行线性投影并加入位置嵌入。这些tokens被送入SOAR编码器层进行处理。
- **输入输出**:
    - **输入**: 航空影像 `I ∈ R^{H×W×C}`。
    - **输出**: 经过检测头（如MLP）处理后的目标检测结果。
- **关键模块**:
    1. **SAHI (Sliced Aided Hyper Inference)**: 一种切片辅助超推理方法，将输入图像切分成重叠的小块进行推理，然后将结果合并。它包含“切片辅助微调”和“切片辅助超推理”两个部分，能增大图像中小目标的相对尺寸。
    2. **Programmable Gradient Information (PGI)**: 源自YOLOv9的核心思想。为了解决深层网络中信息瓶颈导致的原始数据信息损失问题，PGI通过引入一个辅助的可逆分支和多层次辅助信息，确保关键梯度信息能传回浅层网络，从而减少信息损失（公式5-7）。
    3. **Vision Mamba 与 状态空间模型**: 借鉴Vision Mamba模型，SOAR编码器层的核心是双向SSM。SSM用于描述一维函数/序列（公式1），通过离散化（公式2-3）和全局卷积（公式4）来处理序列数据。它能以线性复杂度模拟类似CNN的局部性和Transformer的全局感受野。在SOAR中，输入token序列经过归一化和线性投影后，沿**前向**和**后向**两个方向分别应用1D卷积和SSM进行处理。
    4. **位置嵌入**: 使用随机初始化的可学习参数，为图像patches提供位置感知能力。
- **模块连接**: 图像 -> 切片/分块 -> 线性投影 + 位置嵌入 -> (多层) SOAR Encoder (内含归一化、线性投影、双向1D-Conv、双向SSM) -> MLP检测头。
- **数学公式/机制解释**:
    - **信息瓶颈理论** (公式5): 说明数据在通过网络层层变换时，会不可避免地丢失信息（`I(X, X) ≥ I(X, f(X))`）。
    - **PGI解决方案** (公式6-7): 利用可逆函数保证信息不丢失，并通过PGI将关键梯度信息绕过深层网络直接回传，以指导浅层网络的学习。
    - **SSM** (公式1-4): 核心是利用状态方程 `z(t)=Ez(t)+Fu(t)` 和输出方程 `v(t)=Gz(t)` 建模序列，通过离散化实现可计算，并通过构建结构化卷积核 `K` 实现高效计算。
- **训练方式**:
    - 输入尺寸固定为224×224。
    - 使用数据增强：随机裁剪、翻转、光度失真、mixup、cutmix等。
    - 优化器：AdamW，初始学习率5e-4，权重衰减0.05。
    - 学习率调度：带线性预热的余弦退火调度器。
    - 批次大小：16，32，64。
    - 训练轮次：200个epoch。
    - 损失函数：交叉熵损失。
- **推理流程**:
    1. 对输入图像应用SAHI，将其切分为重叠的patches。
    2. 将每个patch送入训练好的SOAR模型进行独立的前向推理。
    3. 将所有patch的预测结果合并回原始图像坐标系，得到最终检测结果。
- **和已有方法的差异**:
    - 相较于传统的CNN或Transformer backbone，SOAR引入了**SSM**，试图在计算效率（线性复杂度）和全局上下文建模能力之间取得更好平衡。
    - 不同于单纯使用YOLOv9，论文结合了**SAHI**来直接增强模型对高分辨率图像中小目标的检测能力。
    - 融合了**PGI**的思想来缓解深层网络的信息损失问题，这是一个针对模型可学习性的改进。
## 实验

- **数据集**: **DOTA v1.5**。这是一个用于航空影像目标检测的大型数据集，图像尺寸从800×800到20000×20000像素不等。包含1869张图像（1410训练，438验证，21测试），涵盖18类目标。数据被预处理为灰度图，并将标签格式从DOTA转换为COCO格式。
- **对比方法**:
    - SNUNet (一个CNN-based模型)
    - TransUNetCD (一个Transformer-based模型)
    - SwinSUNet (一个基于Swin Transformer的模型)
- **评价指标**:
    - **精确率** (Precision, Pre)
    - **召回率** (Recall, Rec)
    - **F1分数** (F1)
    - **整体准确率** (Overall Accuracy, OA)
    - **交并比** (Intersection over Union, IoU)
    - **Kappa系数** (KC)
    - **计算效率**: 参数量 (Params, M) 和 浮点运算量 (GFLOPs)
- **主实验结果**:
    - **准确率** (表格 II): SOAR模型的性能与最好的SwinSUNet非常接近，但略有不及。
        - SOAR: Rec=79.59, Pre=83.06, OA=91.36, F1=81.29, IoU=68.48, KC=75.68
        - SwinSUNet (最佳): Rec=79.75, Pre=83.50, OA=91.51, F1=81.58, IoU=68.89, KC=76.06
    - **计算效率** (表格 I): SOAR在参数量和计算量上具有明显优势。
        - SOAR: **17.13M** 参数, **45.74** GFLOPs
        - TransUNetCD: 28.37M 参数, 244.54 GFLOPs
        - SwinSUNet: 39.28M 参数, 43.50 GFLOPs (注：SwinSUNet的GFLOPs低于SOAR，但参数量远高于SOAR)
- **消融实验**: PDF文本中未明确说明是否进行了详细的消融实验（例如，分别验证PGI、SSM、SAHI各组件的效果）。
- **泛化实验**: PDF文本中仅在DOTA v1.5上进行了实验，未提及其他数据集的泛化性测试。
- **速度/参数量/FLOPs**: 如上所述，在参数量方面，SOAR（17.13M）是最轻量化的；在GFLOPs方面，SOAR（45.74）介于SwinSUNet和TransUNetCD之间，远低于TransUNetCD。
## 局限

- **实验充分性**: 实验仅在一个数据集（DOTA v1.5）上进行，缺乏在其他主流小目标数据集（如VisDrone， AI-TOD）或不同领域数据集上的泛化性验证。
- **对比基线**: 对比的基线模型（SNUNet, TransUNetCD等）可能不是当前小目标检测领域的SOTA模型。缺乏与最新YOLO系列（如YOLOv8）或其他高效检测器的对比。
- **模型分析**: 论文未提供详细的消融实验来量化SOAR框架中各个组件（如双向SSM、PGI、位置嵌入）的贡献。
- **可视化与定性分析**: 虽然有图3的推断结果展示，但缺乏对模型在**困难样本**（如密集、严重遮挡的小目标）上性能的深入定性分析。
- **计算成本**: 论文使用了双机训练（各24GB GPU），且提到模型太大无法在单卡上训练，暗示其训练成本可能较高，这可能影响其在资源受限场景下的应用。
- **复现风险**: 论文将发布代码，但依赖Vision Mamba这一较新的模型架构，其稳定性和社区支持尚在发展中。
## 个人评论

1. **方法论启发**: 论文展示了将**状态空间模型 (SSM)** 引入视觉任务（尤其是目标检测）的可行性。SSM的线性复杂度和长程建模能力，为解决Transformer在视觉任务中计算成本高的问题提供了一个有潜力的方向。
2. **工程实践价值**: 对**SAHI框架**与先进检测器（如YOLOv9）结合的实践进行了验证。SAHI是一种即插即用的、能显著提升现有模型在小目标场景下性能的工程技巧，具有很高的实用价值。
3. **模型设计思想**: 对**PGI**（可编程梯度信息）理念的借鉴，强调了在深层网络中保留原始数据信息和关键梯度流的重要性，这对设计更有效的骨干网络有启发。

### 使用建议

- **如果快速了解**: 重点阅读 **摘要**、**引言** 的最后部分（贡献总结）、**方法部分的图表** (图1)、**实验部分的表格** (表格I, II) 和 **结论**。
- **如果复现**: 重点精读 **方法详解 (III)**，特别是公式 (1)-(8) 和对SOAR编码器的描述；**实验部分 (IV)** 的实验设置、数据集处理和实现细节。
- **如果借鉴创新点**:
    - 学习**如何将SAHI应用于新模型**以提升小目标性能。
    - 研究**SSM在视觉backbone中的集成方式**，特别是其双向处理机制。
    - 理解**PGI**的核心思想，看是否可以将类似的可逆分支或梯度指导策略应用于其他深度网络。
- **如果写相关工作**: 可将本文归类为以下相关工作的延伸：
    - **小目标检测方法**（特别是航空/遥感场景）。
    - **基于YOLO的实时检测器改进**。
    - **状态空间模型 (Mamba) 在计算机视觉中的应用**。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**计算机视觉**领域，具体是**航空影像中的小目标检测**方向。它旨在解决由于小目标像素少、易被遮挡而导致的检测难题。论文结合了新兴的**状态空间模型**（State Space Models, SSMs）与轻量化的**YOLO系列检测器**，并引入了切片推理的辅助框架。因此，它可以被归类到“通用计算机视觉”或“目标检测与识别”主题下，特别是专注于小目标、遥感或航空场景的优化。

## 2. 一句话总结
本文提出了SOAR框架，通过将切片辅助超推理（SAHI）应用于YOLOv9并融合Vision Mamba模型中的双向状态空间模型，以提升航空影像中小目标的检测精度与效率。

## 3. 背景与问题
- **为什么要做**: 航空影像中的小目标检测是自动驾驶、交通监控等应用的关键，但小目标信息少、易被背景噪声和遮挡影响，是当前目标检测领域的重大挑战。
- **之前方法的问题**:
    1. 基于Transformer的模型在处理不同方向和尺度的对象时性能受限，且需要专门的数据库。
    2. 传统的检测器（如Faster R-CNN, RetinaNet）多在低分辨率、包含大目标的数据集（如MS COCO）上训练，对高分辨率影像中的小目标检测效果不佳。
    3. 虽然多尺度特征融合等方法被应用，但网络加深会导致参数量和计算量增加，如何在保持精度的同时提升效率是关键。
    4. 定向目标检测（OBB）虽能改善定位，但并未专门针对“小尺寸”这一核心问题。
- **核心矛盾**: 需要在**有限的计算资源**下，设计出既能**有效提取小目标微弱特征**（对抗信息损失），又能**建模长距离全局上下文**，同时保持**实时性**的轻量化检测模型。

## 4. 核心贡献
1. **将YOLOv9与SAHI框架结合**：首次在新型轻量级架构YOLOv9上部署SAHI，并应用于DOTA数据集，通过切片推理和微调提升小目标检测性能。
2. **提出SOAR框架**：设计了一个基于Vision Mamba架构的动态小目标检测框架，并进行了实验验证。该框架引入了**双向状态空间模型**进行视觉上下文建模。
3. **提出融合PGI与SSM的新框架**：提出了一个将**可编程梯度信息**（PGI）与**状态空间模型表示**相结合的框架，旨在为有效的视觉和计算机视觉任务提供新方案。

## 5. 方法详解
- **整体框架 (SOAR encoder)**: 如图1所示，SOAR框架首先将2D图像分割成展平的2D patches，然后进行线性投影并加入位置嵌入。这些tokens被送入SOAR编码器层进行处理。
- **输入输出**:
    - **输入**: 航空影像 `I ∈ R^{H×W×C}`。
    - **输出**: 经过检测头（如MLP）处理后的目标检测结果。
- **关键模块**:
    1. **SAHI (Sliced Aided Hyper Inference)**: 一种切片辅助超推理方法，将输入图像切分成重叠的小块进行推理，然后将结果合并。它包含“切片辅助微调”和“切片辅助超推理”两个部分，能增大图像中小目标的相对尺寸。
    2. **Programmable Gradient Information (PGI)**: 源自YOLOv9的核心思想。为了解决深层网络中信息瓶颈导致的原始数据信息损失问题，PGI通过引入一个辅助的可逆分支和多层次辅助信息，确保关键梯度信息能传回浅层网络，从而减少信息损失（公式5-7）。
    3. **Vision Mamba 与 状态空间模型**: 借鉴Vision Mamba模型，SOAR编码器层的核心是双向SSM。SSM用于描述一维函数/序列（公式1），通过离散化（公式2-3）和全局卷积（公式4）来处理序列数据。它能以线性复杂度模拟类似CNN的局部性和Transformer的全局感受野。在SOAR中，输入token序列经过归一化和线性投影后，沿**前向**和**后向**两个方向分别应用1D卷积和SSM进行处理。
    4. **位置嵌入**: 使用随机初始化的可学习参数，为图像patches提供位置感知能力。
- **模块连接**: 图像 -> 切片/分块 -> 线性投影 + 位置嵌入 -> (多层) SOAR Encoder (内含归一化、线性投影、双向1D-Conv、双向SSM) -> MLP检测头。
- **数学公式/机制解释**:
    - **信息瓶颈理论** (公式5): 说明数据在通过网络层层变换时，会不可避免地丢失信息（`I(X, X) ≥ I(X, f(X))`）。
    - **PGI解决方案** (公式6-7): 利用可逆函数保证信息不丢失，并通过PGI将关键梯度信息绕过深层网络直接回传，以指导浅层网络的学习。
    - **SSM** (公式1-4): 核心是利用状态方程 `z(t)=Ez(t)+Fu(t)` 和输出方程 `v(t)=Gz(t)` 建模序列，通过离散化实现可计算，并通过构建结构化卷积核 `K` 实现高效计算。
- **训练方式**:
    - 输入尺寸固定为224×224。
    - 使用数据增强：随机裁剪、翻转、光度失真、mixup、cutmix等。
    - 优化器：AdamW，初始学习率5e-4，权重衰减0.05。
    - 学习率调度：带线性预热的余弦退火调度器。
    - 批次大小：16，32，64。
    - 训练轮次：200个epoch。
    - 损失函数：交叉熵损失。
- **推理流程**:
    1. 对输入图像应用SAHI，将其切分为重叠的patches。
    2. 将每个patch送入训练好的SOAR模型进行独立的前向推理。
    3. 将所有patch的预测结果合并回原始图像坐标系，得到最终检测结果。
- **和已有方法的差异**:
    - 相较于传统的CNN或Transformer backbone，SOAR引入了**SSM**，试图在计算效率（线性复杂度）和全局上下文建模能力之间取得更好平衡。
    - 不同于单纯使用YOLOv9，论文结合了**SAHI**来直接增强模型对高分辨率图像中小目标的检测能力。
    - 融合了**PGI**的思想来缓解深层网络的信息损失问题，这是一个针对模型可学习性的改进。

## 6. 实验与结果
- **数据集**: **DOTA v1.5**。这是一个用于航空影像目标检测的大型数据集，图像尺寸从800×800到20000×20000像素不等。包含1869张图像（1410训练，438验证，21测试），涵盖18类目标。数据被预处理为灰度图，并将标签格式从DOTA转换为COCO格式。
- **对比方法**:
    - SNUNet (一个CNN-based模型)
    - TransUNetCD (一个Transformer-based模型)
    - SwinSUNet (一个基于Swin Transformer的模型)
- **评价指标**:
    - **精确率** (Precision, Pre)
    - **召回率** (Recall, Rec)
    - **F1分数** (F1)
    - **整体准确率** (Overall Accuracy, OA)
    - **交并比** (Intersection over Union, IoU)
    - **Kappa系数** (KC)
    - **计算效率**: 参数量 (Params, M) 和 浮点运算量 (GFLOPs)
- **主实验结果**:
    - **准确率** (表格 II): SOAR模型的性能与最好的SwinSUNet非常接近，但略有不及。
        - SOAR: Rec=79.59, Pre=83.06, OA=91.36, F1=81.29, IoU=68.48, KC=75.68
        - SwinSUNet (最佳): Rec=79.75, Pre=83.50, OA=91.51, F1=81.58, IoU=68.89, KC=76.06
    - **计算效率** (表格 I): SOAR在参数量和计算量上具有明显优势。
        - SOAR: **17.13M** 参数, **45.74** GFLOPs
        - TransUNetCD: 28.37M 参数, 244.54 GFLOPs
        - SwinSUNet: 39.28M 参数, 43.50 GFLOPs (注：SwinSUNet的GFLOPs低于SOAR，但参数量远高于SOAR)
- **消融实验**: PDF文本中未明确说明是否进行了详细的消融实验（例如，分别验证PGI、SSM、SAHI各组件的效果）。
- **泛化实验**: PDF文本中仅在DOTA v1.5上进行了实验，未提及其他数据集的泛化性测试。
- **速度/参数量/FLOPs**: 如上所述，在参数量方面，SOAR（17.13M）是最轻量化的；在GFLOPs方面，SOAR（45.74）介于SwinSUNet和TransUNetCD之间，远低于TransUNetCD。

## 7. 这篇论文真正有价值的地方
1. **方法论启发**: 论文展示了将**状态空间模型 (SSM)** 引入视觉任务（尤其是目标检测）的可行性。SSM的线性复杂度和长程建模能力，为解决Transformer在视觉任务中计算成本高的问题提供了一个有潜力的方向。
2. **工程实践价值**: 对**SAHI框架**与先进检测器（如YOLOv9）结合的实践进行了验证。SAHI是一种即插即用的、能显著提升现有模型在小目标场景下性能的工程技巧，具有很高的实用价值。
3. **模型设计思想**: 对**PGI**（可编程梯度信息）理念的借鉴，强调了在深层网络中保留原始数据信息和关键梯度流的重要性，这对设计更有效的骨干网络有启发。

## 8. 局限与问题
- **实验充分性**: 实验仅在一个数据集（DOTA v1.5）上进行，缺乏在其他主流小目标数据集（如VisDrone， AI-TOD）或不同领域数据集上的泛化性验证。
- **对比基线**: 对比的基线模型（SNUNet, TransUNetCD等）可能不是当前小目标检测领域的SOTA模型。缺乏与最新YOLO系列（如YOLOv8）或其他高效检测器的对比。
- **模型分析**: 论文未提供详细的消融实验来量化SOAR框架中各个组件（如双向SSM、PGI、位置嵌入）的贡献。
- **可视化与定性分析**: 虽然有图3的推断结果展示，但缺乏对模型在**困难样本**（如密集、严重遮挡的小目标）上性能的深入定性分析。
- **计算成本**: 论文使用了双机训练（各24GB GPU），且提到模型太大无法在单卡上训练，暗示其训练成本可能较高，这可能影响其在资源受限场景下的应用。
- **复现风险**: 论文将发布代码，但依赖Vision Mamba这一较新的模型架构，其稳定性和社区支持尚在发展中。

## 9. 我该怎么使用这篇论文
- **如果快速了解**: 重点阅读 **摘要**、**引言** 的最后部分（贡献总结）、**方法部分的图表** (图1)、**实验部分的表格** (表格I, II) 和 **结论**。
- **如果复现**: 重点精读 **方法详解 (III)**，特别是公式 (1)-(8) 和对SOAR编码器的描述；**实验部分 (IV)** 的实验设置、数据集处理和实现细节。
- **如果借鉴创新点**:
    - 学习**如何将SAHI应用于新模型**以提升小目标性能。
    - 研究**SSM在视觉backbone中的集成方式**，特别是其双向处理机制。
    - 理解**PGI**的核心思想，看是否可以将类似的可逆分支或梯度指导策略应用于其他深度网络。
- **如果写相关工作**: 可将本文归类为以下相关工作的延伸：
    - **小目标检测方法**（特别是航空/遥感场景）。
    - **基于YOLO的实时检测器改进**。
    - **状态空间模型 (Mamba) 在计算机视觉中的应用**。

## 10. 和其他论文的关系
根据主题，本论文可能与以下类型的论文相关，但具体论文未知，故不使用双链：
- YOLO系列的最新改进工作，特别是 **YOLOv9** [22]。
- **Vision Mamba** [26] 及后续将Mamba应用于视觉任务的论文。
- **SAHI** (Slicing Aided Hyper Inference) [25] 框架的提出或应用论文。
- 关于**状态空间模型 (SSM)** 在序列建模和视觉中应用的论文，如 **S4, Mamba** 等。
- 航空影像**小目标检测**和**旋转目标检测**的专题论文。

## 11. 关键词
小目标检测， 状态空间模型， YOLOv9， 航空影像， Vision Mamba， 可编程梯度信息， 切片辅助超推理， 遥感， 轻量化模型， 特征融合， 目标检测

## 12. 可信度说明
本精读笔记主要基于提供的 **PDF文本的前7页内容** 生成，包括标题、作者、摘要、引言、相关工作、方法论部分、实验设置、部分实验结果和结论。文本提取质量整体良好，但存在一些局限：
- 部分图表信息（如图1、图4）的细节无法从纯文本中完全获取。
- 实验结果的具体数值和对比信息主要来源于 **表格I和表格II**，这些关键数据是可靠的。
- 论文中提到的“Fig. 4”（可能展示训练曲线）的具体内容未在提供的文本中描述。
- 方法论部分的部分数学描述（如公式）在文本中是完整的，但其与图示的对应关系需结合论文原文理解。
因此，笔记内容严格基于文本，对于文本中未明确说明的信息（如消融实验）已标注。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (3577 字符/页)); 来源缓存: `.paper-cache/extracts/2024_SOAR_Advancements_i.txt` (7/7 页); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
