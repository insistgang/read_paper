---
title: Restoring Images in Adverse Weather Conditions
authors:
  - "Shangquan Sun"
  - "Wenqi Ren"
  - "Xinwei Gao"
  - "Rui Wang"
  - "Xiaochun Cao"
year: 2024
venue: "arXiv"
doi: 
pdf: [[HTB.pdf]]
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
extract_cache: .paper-cache/extracts/HTB.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/19 pages"
---
# Restoring Images in Adverse Weather Conditions

## 基本信息
- **PDF**: [[HTB.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Restoring Images in Adverse Weather Conditions |
| **作者** | Shangquan Sun; Wenqi Ren; Xinwei Gao; Rui Wang; Xiaochun Cao |
| **发表时间** | 2024 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Transformer-basedimagerestorationmethodsinadversewea- ther have achieved significant progress. Most of them use self-attention along the channel dimension or within spatially fixed-range blocks to reduce computational load. However, such a compromise results in lim- itations in capturing long-range spatial features. Inspired by the ob- servation that the weather-induced degradation factors mainly cause similar occlusion and brightness, in this work, we propose an efficient HistogramTransformer(Histoformer)forrestoringimagesaffectedby adverse weather. It is powered by a mechanism dubbed histogram self- attention,whichsortsandsegmentsspatialfeaturesintointensity-based bins. Self-attention is then applied across bins or within each bin to selectively focus on spatial features of dynamic range and process simi- lar degraded pixels of the long range together. To boost histogram self- attention,wepresentadynamic-rangeconvolutionenablingconventional convolutiontoconductoperationoversimilarpix

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么做**：恶劣天气（雨、雾、雪等）会严重降低图像质量，影响下游任务（如目标检测、深度估计）。现有方法通常是针对单一任务（如只去雨或只去雾）训练，切换模型复杂，不利于实际应用。
- **之前方法的问题**：基于Transformer的统一去除方法，为了降低计算量，通常在**通道维度**或**固定空间范围的块内**执行自注意力（p.2）。这种妥协限制了Transformer建模长距离空间特征的能力，导致恢复性能受损。
- **核心矛盾**：天气退化（如雨滴、雪、雾）往往导致图像中出现具有**相似遮挡和亮度模式**的像素（p.2）。然而，传统的自注意力机制在固定空间邻域或通道上操作，无法有效地将这些空间上分散但退化性质相似的长距离像素关联起来。
## 关键贡献

1.  **提出了新型的直方图自注意力机制**：基于观察到天气退化模式具有相似性，将像素按强度值排序并分箱，在箱内和箱间执行自注意力，实现了动态范围的空间注意力，能全局高效地处理相似退化像素。
2.  **提出了动态范围卷积层**：在应用可分离卷积前，对输入特征在水平和垂直方向进行排序，使卷积操作能够跨越相似强度（动态位置）的像素进行，而不仅仅是空间相邻像素。
3.  **提出了双尺度门控前馈模块**：整合了两个具有不同扩张率的深度可分离卷积路径，以捕获多尺度和多范围信息，增强特征表示。
4.  **提出了基于皮尔逊相关系数的相关性损失**：指出传统逐像素损失忽略了输出与真值之间的线性相关性，利用该损失函数来约束恢复图像的像素顺序与真值图像保持一致。
## 方法

- **整体框架**：Histoformer采用类似U-Net的编码器-解码器结构。输入为退化图像，通过卷积进行块嵌入后，在编码器和解码器的每个阶段堆叠**直方图Transformer块**。编码器和解码器通过跳跃连接相连，阶段间使用PixelShuffle/PixelUnshuffle进行下上采样。
- **输入输出**：输入 `I_lq ∈ R^(3×H×W)`，输出恢复后的图像。
- **关键模块**：
    1.  **直方图Transformer块**：是核心构建单元，包含两个子模块：
        - **动态范围直方图自注意力**：这是论文的核心注意力算子。
            - **直方图分组**：将特征图的像素值（或特征值）按强度排序，然后平均分成 `B` 个“箱子”。每个箱子包含 `HW/B` 个像素，这些像素在空间上分散，但强度值相近。
            - **双路注意力**：采用两种重塑方式进行注意力计算：
                - **箱间直方图重塑**：将排序后的特征重塑为 `(C, B, HW/B)`。注意力在 `B` 个箱子之间计算，每个箱子包含大量像素，用于聚合**全局信息**。
                - **频率直方图重塑**：将特征重塑为 `(C, HW/B, B)`。注意力在每个箱子内的 `B` 个频率（即箱子内像素）间计算，每个箱子只包含少量像素，用于聚合**局部/细粒度信息**。
            - **输出**：两路注意力的输出进行逐元素相乘，得到最终的注意力结果。
        - **双尺度门控前馈模块**：使用两个不同膨胀率的并行深度可分离卷积路径来处理特征，然后通过门控机制（逐元素相乘）融合，以捕获多尺度信息。
    2.  **动态范围卷积**：在DHSA内部。首先将输入特征沿通道分为两部分 `F1` 和 `F2`。对 `F1` 先进行水平排序再垂直排序，然后与 `F2` 在通道维度拼接，最后通过一个1x1卷积和一个3x3深度可分离卷积。排序操作将高低强度像素分别聚集在特征图的对角区域，使后续卷积能够在跨动态范围的相似像素上进行计算。
- **模块连接**：每个HTB内部，输入特征先经过层归一化和DHSA，再进行残差连接；然后经过层归一化和DGFF，再次残差连接。
- **数学公式/机制直观解释**：
    - **直方图自注意力核心公式 (5)**：`A = A_B ⊙ A_F`，其中 `A_B` 是箱间注意力图，`A_F` 是频率（箱内）注意力图。两者相乘意味着一个像素的最终重要性由它**所属箱子的重要性**和**它在该箱子内的重要性**共同决定。
    - **排序的直观意义**：排序将图像中“亮的退化”（如雪、雾）和“暗的背景”自然分开，使得强度相近的退化像素在重塑后成为相邻的“token”，便于注意力处理。
- **训练方式**：采用 `L1` 逐像素损失和提出的**皮尔逊相关系数损失** `L_pcc` 联合训练。`L_pcc` 衡量输出图像块和真值图像块之间的线性相关性。
- **推理流程**：与标准的图像到图像转换网络推理流程一致。
- **和已有方法的差异**：
    - **vs 通道注意力 (Restormer等)**：本文的注意力在空间上，但通过直方图分组实现了动态范围。
    - **vs 窗口注意力 (Swin Transformer等)**：本文的注意力不受固定空间窗口限制，而是基于像素值动态分组，理论上可以关联全图任意位置的相似像素。
    - **核心差异**：传统注意力作用于固定空间或通道维度；本文注意力作用于**按像素强度动态划分的语义组**。
## 实验

- **使用的数据集**：Snow100K-S/L（去雪），Outdoor-Rain（去雨），RainDrop（雨滴去除）。
- **对比方法**：任务特定方法（如DesnowNet, JSTASR, RESCAN）和统一多天气方法（如All-in-One, TransWeather, WGWSNet, WeatherDiff, AWRCP）。
- **评价指标**：PSNR 和 SSIM。
- **主实验结果**：Histoformer在多个数据集和任务上均取得了最优性能。
    - **去雪 (Snow100K-L)**：**32.16 dB** PSNR / **0.9261** SSIM，超越第二名AWRCP (31.92/0.9341) 和第三名Restormer (30.36/0.9068) (p.9)。
    - **去雨 (Outdoor-Rain)**：**32.08 dB** PSNR / **0.9389** SSIM，大幅超越所有对比方法 (p.9)。
    - **雨滴去除 (RainDrop)**：**32.52 dB** PSNR / **0.9419** SSIM，优于第二名WGWSNet (32.38/0.9378) (p.9)。
- **消融实验**：PDF文本中未明确提供详细的消融实验结果表格或分析。但文中各处解释了各模块（DHSA, DGFF, 动态范围卷积, 相关损失）的设计动机。
- **泛化实验**：论文在多个不同类型（雪、雨、雾、雨滴）的退化数据集上测试，验证了模型的统一去除能力。
- **效率信息**：PDF文本中未提供FLOPs、参数量或运行速度的具体数据。
## 局限

- **计算效率未知**：论文未提供与对比方法在计算量（FLOPs）、参数量和推理速度上的详细比较，不清楚其“高效”的具体程度。
- **假设的局限性**：方法依赖于“天气退化主要引起相似遮挡和亮度”的观察。对于某些非亮度主导或模式多变的复杂退化（如特殊光晕、非均匀雨雾），其分箱效果可能打折扣。
- **数据集局限性**：主要在合成数据集上进行评估，尽管在真实世界图像展示中有效（p.19-20），但系统性的大规模真实世界评测未在提供文本中体现。
- **排序操作的开销**：动态范围卷积和直方图自注意力中的排序操作会引入额外的计算开销，这在文本中没有被量化。
- **复现细节**：对于分箱数量 `B`、DGFF中具体的膨胀率等超参数，文本中未明确给出，复现时需要参考代码。
## 个人评论

1.  **提出了一个优雅的注意力分组思想**：打破“空间位置邻近”或“同通道”的常规分组依据，提出了**按像素值强度（语义）动态分组**的新范式。这对于处理那些退化模式具有强度一致性（如所有雪点都是亮的）的任务非常有效。
2.  **双重注意力的巧妙结合**：箱间注意力和箱内注意力的乘积设计，巧妙地兼顾了“对同类像素组的全局关注”和“组内像素的细粒度差异处理”，思想深刻。
3.  **将领域知识融入网络设计**：没有盲目堆叠模块，而是深入分析了天气退化的共同模式（相似遮挡和亮度），并据此设计了直方图机制，体现了领域知识驱动的网络设计。
4.  **启发新的损失函数设计**：指出传统逐像素损失的不足，并提出皮尔逊相关系数损失来保持恢复图像的“序”，这为图像恢复的损失函数设计提供了新思路。

### 使用建议

- **如果快速了解**：重点阅读 **Abstract**、**Introduction** 的前三段和最后一段（贡献）、**Figure 1** 和 **Figure 2** 的图注，以及 **Section 3.2** 中关于“Dynamic-range Histogram Self-Attention”的描述和**公式(5)**。
- **如果复现**：精读 **Section 3 (Method)**，尤其是 **3.2 Histogram Transformer Block** 中对DHSA和DGFF的每一步描述，并结合 **Figure 2** 理解数据流。务必参考官方代码以获取超参数和实现细节。
- **如果借鉴创新点**：
    1.  学习其 **“基于像素值排序和分组”** 的注意力构建思路，可尝试将其迁移到其他需要对特定属性（如边缘、纹理、运动）进行动态关注的任务中。
    2.  学习其 **“双路（粗粒度+细粒度）注意力融合”** 的设计模式。
    3.  借鉴其 **“领域知识驱动”** 的模块设计思路，分析所研究问题的共性，并将其转化为网络结构的归纳偏置。
- **如果写 Related Work**：可将其归类于 **“Transformer-based Image Restoration”** 或 **“All-in-One Weather Removal”** 章节，并强调其与固定窗口/通道注意力Transformer的区别。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉领域的**图像恢复**方向，具体聚焦于**恶劣天气条件下的图像恢复**（如去雨、去雾、去雪、雨滴去除等）。它提出了一种统一的解决方案，能够处理多种天气退化。本文适合作为 **“B_注意力算子模块”** 主题下的精读论文，因其核心创新点是一种新型的、基于直方图的注意力机制。

## 2. 一句话总结
本文提出了一种高效的**直方图Transformer (Histoformer)**，其核心是**直方图自注意力机制**，通过将图像像素按强度排序并分组到不同的直方图“箱子”中，使得注意力能够动态地聚焦于具有相似退化模式的像素，从而在全局范围内高效地恢复恶劣天气影响的图像。

## 3. 背景与问题
- **为什么做**：恶劣天气（雨、雾、雪等）会严重降低图像质量，影响下游任务（如目标检测、深度估计）。现有方法通常是针对单一任务（如只去雨或只去雾）训练，切换模型复杂，不利于实际应用。
- **之前方法的问题**：基于Transformer的统一去除方法，为了降低计算量，通常在**通道维度**或**固定空间范围的块内**执行自注意力（p.2）。这种妥协限制了Transformer建模长距离空间特征的能力，导致恢复性能受损。
- **核心矛盾**：天气退化（如雨滴、雪、雾）往往导致图像中出现具有**相似遮挡和亮度模式**的像素（p.2）。然而，传统的自注意力机制在固定空间邻域或通道上操作，无法有效地将这些空间上分散但退化性质相似的长距离像素关联起来。

## 4. 核心贡献
1.  **提出了新型的直方图自注意力机制**：基于观察到天气退化模式具有相似性，将像素按强度值排序并分箱，在箱内和箱间执行自注意力，实现了动态范围的空间注意力，能全局高效地处理相似退化像素。
2.  **提出了动态范围卷积层**：在应用可分离卷积前，对输入特征在水平和垂直方向进行排序，使卷积操作能够跨越相似强度（动态位置）的像素进行，而不仅仅是空间相邻像素。
3.  **提出了双尺度门控前馈模块**：整合了两个具有不同扩张率的深度可分离卷积路径，以捕获多尺度和多范围信息，增强特征表示。
4.  **提出了基于皮尔逊相关系数的相关性损失**：指出传统逐像素损失忽略了输出与真值之间的线性相关性，利用该损失函数来约束恢复图像的像素顺序与真值图像保持一致。

## 5. 方法详解
- **整体框架**：Histoformer采用类似U-Net的编码器-解码器结构。输入为退化图像，通过卷积进行块嵌入后，在编码器和解码器的每个阶段堆叠**直方图Transformer块**。编码器和解码器通过跳跃连接相连，阶段间使用PixelShuffle/PixelUnshuffle进行下上采样。
- **输入输出**：输入 `I_lq ∈ R^(3×H×W)`，输出恢复后的图像。
- **关键模块**：
    1.  **直方图Transformer块**：是核心构建单元，包含两个子模块：
        - **动态范围直方图自注意力**：这是论文的核心注意力算子。
            - **直方图分组**：将特征图的像素值（或特征值）按强度排序，然后平均分成 `B` 个“箱子”。每个箱子包含 `HW/B` 个像素，这些像素在空间上分散，但强度值相近。
            - **双路注意力**：采用两种重塑方式进行注意力计算：
                - **箱间直方图重塑**：将排序后的特征重塑为 `(C, B, HW/B)`。注意力在 `B` 个箱子之间计算，每个箱子包含大量像素，用于聚合**全局信息**。
                - **频率直方图重塑**：将特征重塑为 `(C, HW/B, B)`。注意力在每个箱子内的 `B` 个频率（即箱子内像素）间计算，每个箱子只包含少量像素，用于聚合**局部/细粒度信息**。
            - **输出**：两路注意力的输出进行逐元素相乘，得到最终的注意力结果。
        - **双尺度门控前馈模块**：使用两个不同膨胀率的并行深度可分离卷积路径来处理特征，然后通过门控机制（逐元素相乘）融合，以捕获多尺度信息。
    2.  **动态范围卷积**：在DHSA内部。首先将输入特征沿通道分为两部分 `F1` 和 `F2`。对 `F1` 先进行水平排序再垂直排序，然后与 `F2` 在通道维度拼接，最后通过一个1x1卷积和一个3x3深度可分离卷积。排序操作将高低强度像素分别聚集在特征图的对角区域，使后续卷积能够在跨动态范围的相似像素上进行计算。
- **模块连接**：每个HTB内部，输入特征先经过层归一化和DHSA，再进行残差连接；然后经过层归一化和DGFF，再次残差连接。
- **数学公式/机制直观解释**：
    - **直方图自注意力核心公式 (5)**：`A = A_B ⊙ A_F`，其中 `A_B` 是箱间注意力图，`A_F` 是频率（箱内）注意力图。两者相乘意味着一个像素的最终重要性由它**所属箱子的重要性**和**它在该箱子内的重要性**共同决定。
    - **排序的直观意义**：排序将图像中“亮的退化”（如雪、雾）和“暗的背景”自然分开，使得强度相近的退化像素在重塑后成为相邻的“token”，便于注意力处理。
- **训练方式**：采用 `L1` 逐像素损失和提出的**皮尔逊相关系数损失** `L_pcc` 联合训练。`L_pcc` 衡量输出图像块和真值图像块之间的线性相关性。
- **推理流程**：与标准的图像到图像转换网络推理流程一致。
- **和已有方法的差异**：
    - **vs 通道注意力 (Restormer等)**：本文的注意力在空间上，但通过直方图分组实现了动态范围。
    - **vs 窗口注意力 (Swin Transformer等)**：本文的注意力不受固定空间窗口限制，而是基于像素值动态分组，理论上可以关联全图任意位置的相似像素。
    - **核心差异**：传统注意力作用于固定空间或通道维度；本文注意力作用于**按像素强度动态划分的语义组**。

## 6. 实验与结果
- **使用的数据集**：Snow100K-S/L（去雪），Outdoor-Rain（去雨），RainDrop（雨滴去除）。
- **对比方法**：任务特定方法（如DesnowNet, JSTASR, RESCAN）和统一多天气方法（如All-in-One, TransWeather, WGWSNet, WeatherDiff, AWRCP）。
- **评价指标**：PSNR 和 SSIM。
- **主实验结果**：Histoformer在多个数据集和任务上均取得了最优性能。
    - **去雪 (Snow100K-L)**：**32.16 dB** PSNR / **0.9261** SSIM，超越第二名AWRCP (31.92/0.9341) 和第三名Restormer (30.36/0.9068) (p.9)。
    - **去雨 (Outdoor-Rain)**：**32.08 dB** PSNR / **0.9389** SSIM，大幅超越所有对比方法 (p.9)。
    - **雨滴去除 (RainDrop)**：**32.52 dB** PSNR / **0.9419** SSIM，优于第二名WGWSNet (32.38/0.9378) (p.9)。
- **消融实验**：PDF文本中未明确提供详细的消融实验结果表格或分析。但文中各处解释了各模块（DHSA, DGFF, 动态范围卷积, 相关损失）的设计动机。
- **泛化实验**：论文在多个不同类型（雪、雨、雾、雨滴）的退化数据集上测试，验证了模型的统一去除能力。
- **效率信息**：PDF文本中未提供FLOPs、参数量或运行速度的具体数据。

## 7. 这篇论文真正有价值的地方
1.  **提出了一个优雅的注意力分组思想**：打破“空间位置邻近”或“同通道”的常规分组依据，提出了**按像素值强度（语义）动态分组**的新范式。这对于处理那些退化模式具有强度一致性（如所有雪点都是亮的）的任务非常有效。
2.  **双重注意力的巧妙结合**：箱间注意力和箱内注意力的乘积设计，巧妙地兼顾了“对同类像素组的全局关注”和“组内像素的细粒度差异处理”，思想深刻。
3.  **将领域知识融入网络设计**：没有盲目堆叠模块，而是深入分析了天气退化的共同模式（相似遮挡和亮度），并据此设计了直方图机制，体现了领域知识驱动的网络设计。
4.  **启发新的损失函数设计**：指出传统逐像素损失的不足，并提出皮尔逊相关系数损失来保持恢复图像的“序”，这为图像恢复的损失函数设计提供了新思路。

## 8. 局限与问题
- **计算效率未知**：论文未提供与对比方法在计算量（FLOPs）、参数量和推理速度上的详细比较，不清楚其“高效”的具体程度。
- **假设的局限性**：方法依赖于“天气退化主要引起相似遮挡和亮度”的观察。对于某些非亮度主导或模式多变的复杂退化（如特殊光晕、非均匀雨雾），其分箱效果可能打折扣。
- **数据集局限性**：主要在合成数据集上进行评估，尽管在真实世界图像展示中有效（p.19-20），但系统性的大规模真实世界评测未在提供文本中体现。
- **排序操作的开销**：动态范围卷积和直方图自注意力中的排序操作会引入额外的计算开销，这在文本中没有被量化。
- **复现细节**：对于分箱数量 `B`、DGFF中具体的膨胀率等超参数，文本中未明确给出，复现时需要参考代码。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读 **Abstract**、**Introduction** 的前三段和最后一段（贡献）、**Figure 1** 和 **Figure 2** 的图注，以及 **Section 3.2** 中关于“Dynamic-range Histogram Self-Attention”的描述和**公式(5)**。
- **如果复现**：精读 **Section 3 (Method)**，尤其是 **3.2 Histogram Transformer Block** 中对DHSA和DGFF的每一步描述，并结合 **Figure 2** 理解数据流。务必参考官方代码以获取超参数和实现细节。
- **如果借鉴创新点**：
    1.  学习其 **“基于像素值排序和分组”** 的注意力构建思路，可尝试将其迁移到其他需要对特定属性（如边缘、纹理、运动）进行动态关注的任务中。
    2.  学习其 **“双路（粗粒度+细粒度）注意力融合”** 的设计模式。
    3.  借鉴其 **“领域知识驱动”** 的模块设计思路，分析所研究问题的共性，并将其转化为网络结构的归纳偏置。
- **如果写 Related Work**：可将其归类于 **“Transformer-based Image Restoration”** 或 **“All-in-One Weather Removal”** 章节，并强调其与固定窗口/通道注意力Transformer的区别。

## 10. 和其他论文的关系
基于文件名 `2024_注意力算子模块_Restoring_Images_图像.pdf` 和主题 `B_注意力算子模块`，本论文可能相关的工作包括：
- **Swin-IR** [[Swin-IR]]：使用窗口注意力的图像恢复Transformer，是本文的重要对比基线。
- **Restormer** [[Restormer]]：使用通道注意力的高效Transformer，是本文的重要对比基线。
- **U-former** [[U-former]]：基于U-Net的Transformer图像恢复框架。
- **TransWeather** [[TransWeather]]：统一恶劣天气去除的早期Transformer工作，是本文的对比方法之一。
- **视觉Transformer的基础工作** [[ViT]]。

## 11. 关键词
图像恢复, 恶劣天气去除, 直方图自注意力, 动态范围注意力, Transformer, 统一模型, 去雪, 去雨, 去雾, 雨滴去除, 皮尔逊相关损失, Histoformer

## 12. 可信度说明
本篇精读笔记主要基于提供的PDF文本（前12页）中的信息生成，具体来源于：
- **论文标题、作者、摘要** (p.1)
- **Figure 1 的说明** (p.2)
- **Introduction** (p.1-3)
- **Method 的整体架构和核心模块描述** (p.5-9)
- **Table 1 的实验结果** (p.9)

**提取质量评估**：提供的文本清晰地包含了论文的核心思想、方法框架和主要实验结果。缺失的部分可能包括详细的消融实验表格、训练细节、更深入的可视化分析以及后续章节（如完整实验、结论、参考文献列表）。尽管如此，现有文本对于理解论文的主要贡献和创新点已经足够。所有在笔记中引用的数字和描述均直接来源于给定的文本段落。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/HTB.txt` (19/19 页; 原 AI 主体 12/19 + 全文补读 13-19); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-19; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-19。
- **提取情况**: 缺失页 7 页, 其中 7 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Restoring Images in Adverse Weather Conditions via Histogram Transformer 13
- p.13: Table 3: Ablation studies on the design
- p.13: SA type PSNR SSIM
- p.13: 44 Out of memory
- p.13: Table 5: Ablation studies on the choice
- p.13: Feed-Forward PSNR SSIM
- p.13: Both MDTA and TKSA integrate rich information across channels, which
- p.14: Show JSON
- p.14: FacesObjects
- p.14: Labels
- p.14: Proper ties
- p.14: Safe Sear ch

### 缺失页关键摘录

- p.13: Table 2: Ablation studies on the dynamic-range convolution.
- p.13: DHSA 32.08 0.9389Table 4: Ablation studies on the number
- p.13: DGFF 32.08 0.9389Table 6: Ablation studies on the setting
- p.13: branch. The quantitative analysis results are presented in Table 3.
- p.13: may result in a loss of the exploitation of long-range information across spatial
- p.13: extracting long-range spatial features, our DHSA enhances performance, result-
- p.13: ing in a PSNR improvement of 0.96 dB compared to TKSA.
- p.13: sults are presented in Table 4. It is observed that increasing the number of bins
- p.14: The quantitative analysis results are presented in Table 5. While MSFN inte-
- p.14: resulting in a PSNR gain of 0.3 dB over MSFN.
- p.14: Correlation Loss. Table 6 shows the effectiveness of the correlation loss Lcor
- p.18: single-image deraining with a high quality real rain dataset. In: CVPR (2019)
<!-- AI_READING_NOTE_END -->
