---
title: Dual Residual Attention Network for Image Denoising
authors:
  - "Wencong Wu"
  - "Shijie Liu"
  - "Yi Zhou"
  - "Yungang Zhang"
  - "Yu Xiang"
year: 2023
venue: "arXiv"
doi: 
pdf: [[RAB&HDRAB.pdf]]
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
extract_cache: .paper-cache/extracts/RAB&HDRAB.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/18 pages"
---
# Dual Residual Attention Network for Image Denoising

## 基本信息
- **PDF**: [[RAB&HDRAB.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Dual Residual Attention Network for Image Denoising |
| **作者** | Wencong Wu; Shijie Liu; Yi Zhou; Yungang Zhang; Yu Xiang |
| **发表时间** | 2023 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Inimagedenoising,deepconvolutionalneuralnetworks(CNNs)canobtainfavorableperformanceonremovingspa- tiallyinvariantnoise. However,manyofthesenetworkscannotperformwellonremovingtherealnoise(i.e. spatially variantnoise)generatedduringimageacquisitionortransmission,whichseverelysetsbacktheirapplicationinpracti- calimagedenoisingtasks. Insteadofcontinuouslyincreasingthenetworkdepth,manyresearchershaverevealedthat expandingthewidthofnetworkscanalsobeausefulwaytoimprovemodelperformance. Italsohasbeenverified that feature filtering can promote the learning ability of the models. Therefore, in this paper, we propose a novel Dual-branchResidualAttentionNetwork(DRANet)forimagedenoising,whichhasboththemeritsofawidemodel architecture and attention-guided feature learning. The proposed DRANet includes two different parallel branches, which can capture complementary features to enhance the learning ability of the model. We designed a new resid- ualattentionblock(RAB)andanovelhybriddilatedresidualatten

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**: 传统的基于深度CNN的去噪方法在处理合成空间不变噪声（如加性高斯白噪声AWGN）时表现良好，但在去除图像采集或传输过程中产生的**空间变化的真实噪声**时效果不佳，这限制了其实际应用 (p.1)。
- **之前方法有什么问题**:
    1.  传统方法（如BM3D, WNNM）依赖于复杂的优化算法，导致**推理时间长**，且因超参数过多而**性能不稳定** (p.1)。
    2.  一些DNN方法通过增加网络深度来提升能力，但这会**增加参数量和推理时间**，难以部署或应用于实时场景 (p.2)。
    3.  一些现有的注意力去噪模型（如ADNet, RIDNet）虽然性能优异，但其**特征学习能力仍有提升空间** (p.2)。
- **作者想解决的核心矛盾**: 如何在**不过度增加网络深度和复杂度**的前提下，设计出既能捕获丰富局部特征，又能利用全局上下文信息，从而有效处理真实空间变化噪声的轻量高效去噪模型。
## 关键贡献

1.  设计了一个新颖的**双支路残差注意力网络（DRANet）**用于图像盲去噪，该模型架构简洁，参数较少，对合成噪声和真实噪声均有效 (p.2)。
2.  提出了两个新的注意力模块：**残差注意力模块（RAB）**和**混合扩张残差注意力模块（HDRAB）**，分别用于模型的上、下分支，使模型能够捕获互补特征并进行有效的特征筛选 (p.2)。
3.  通过广泛的实验证明，DRANet在去噪性能上能与许多最先进的方法相竞争 (p.2)。
## 方法

- **整体框架**: DRANet是一个**双支路并行结构**（如Fig. 1所示, p.4）。上分支包含5个**残差注意力模块（RAB）**，下分支包含5个**混合扩张残差注意力模块（HDRAB）**。两个分支的特征通过**拼接（Concat）** 进行全局融合。
- **输入输出**: 输入为带噪图像 `y`，输出为去噪图像 `\hat{x}`。
- **关键模块**:
    1.  **残差注意力模块（RAB，如Fig. 2所示, p.5）**:
        - **组成**: 由**残差块**和**空间注意力模块（SAM）**构成。
        - **残差块**: 包含多个标准卷积和ReLU激活，通过多个跳跃连接提取丰富的局部特征。
        - **SAM**: 用于学习卷积特征之间的**空间关系**。它使用全局平均池化（GAP）和全局最大池化（GMP）来表示图像的全局统计信息，从而聚焦有用特征并过滤不重要特征。其输出通过Sigmoid生成空间注意力图，与输入特征进行逐元素相乘。
        - **核心作用**: 捕获**局部特征**并通过**空间注意力**进行特征筛选。
    2.  **混合扩张残差注意力模块（HDRAB，如Fig. 3所示, p.5）**:
        - **组成**: 由**混合扩张残差块**和**通道注意力模块（CAM）**构成。
        - **混合扩张残差块**: 包含多个具有不同扩张率`s`（从1到4）的混合扩张卷积。扩张卷积能在**不增加参数和计算量**的情况下扩大感受野，而混合设计旨在**消除网格化现象**。
        - **CAM**: 用于学习卷积特征之间的**通道关系**。由GAP、卷积、ReLU和Sigmoid构成，生成通道注意力图，对特征通道进行加权。
        - **核心作用**: 在**扩大感受野**捕获更多图像信息的同时，通过**通道注意力**进行特征筛选。
- **模块之间怎么连接**:
    - 每个分支内部，RAB/HDRAB之间通过**长跳跃连接（Long skip connection）** 连接，以缓解梯度消失/爆炸并加速训练。
    - 两个并行分支最终通过**拼接（Concat）** 操作融合特征，以捕获全局图像特征。
- **数学公式或机制的直观解释**:
    - 训练阶段的损失函数：
        - 对于**合成噪声（AWGN）去除**：使用**均方误差（MSE）** (公式1, p.5)。
        - 对于**真实噪声去除**：为避免模糊效应，采用**Charbonnier损失**（Lchar，公式3）和**边缘损失**（Ledge，公式4，基于拉普拉斯算子）的加权和（公式2，权重λedge=0.1）。
- **训练方式**: 使用Adam优化器。合成噪声模型训练6×10⁵次迭代，初始学习率1×10⁻⁴；真实噪声模型训练120个epoch，初始学习率2×10⁻⁴并采用余弦退火策略 (p.6)。
- **推理流程**: 标准的前向传播过程，带噪图像输入网络，经过两个分支处理和特征融合后输出去噪图像。
- **和已有方法的差异**:
    - 相较于单纯加深网络（如ResNet），DRANet采用**加宽的双支路结构**，以更少的深度提升性能。
    - 相较于其他注意力模块（如[48, 49]中的残差注意力块），本文的**RAB拥有更多的跳跃连接**以增强特征提取与融合 (p.5)。
    - 相较于使用标准卷积的模块，本文的**HDRAB创新性地结合了混合扩张卷积和通道注意力**，在扩大感受野的同时进行特征选择 (p.5)。
## 实验

- **使用的数据集**:
    - **合成噪声训练**: Flickr2K (2650张高分辨率彩色图像) (p.6)。
    - **合成噪声测试**: Set12, BSD68, CBSD68, Kodak24, McMaster (p.6)。
    - **真实噪声训练**: SIDD Medium (320对图像) (p.6)。
    - **真实噪声测试**: SIDD 验证集, DND sRGB数据集 (p.6)。
- **对比方法**: BM3D, TNRD, DnCNN, IRCNN, FFDNet, BUIFD, BRDNet, DudeNet, ADNet, DSNetB, AINDNet, RIDNet, AirNet 等 (p.6)。
- **评价指标**: **PSNR** 和 **SSIM** (p.6)。
- **主实验结果**: PDF文本中**未提供**主实验（如AWGN去除、真实噪声去除）的具体对比数字结果（这些结果可能在文本未提供的第6页之后）。
- **消融实验**: 在BSD68数据集，噪声水平σ=30的AWGN上进行。
    - 上分支单独: 27.81 dB / 0.781 SSIM。
    - 下分支单独: 28.43 dB / 0.807 SSIM。
    - 无长跳跃连接: 28.55 dB / 0.808 SSIM。
    - 无残差学习: 28.54 dB / 0.807 SSIM。
    - **完整DRANet**: **28.56 dB / 0.808 SSIM** (Table 1, p.6)。
    - 结论：完整模型性能最佳，双支路和辅助连接设计有效。
- **泛化实验**: 模型在多个合成和真实数据集上进行测试，但具体泛化结果数字**未在提供的文本中找到**。
- **速度/参数量/FLOPs等效率信息**: PDF提供的文本中**未明确说明**具体的模型参数量、FLOPs或推理速度数据。
## 局限

- **计算成本**：虽然作者声称DRANet参数较少，但**未在提供的文本中报告具体的参数量、FLOPs和推理时间**。双支路结构和拼接操作可能带来额外的计算开销。
- **数据集与场景**：真实噪声实验仅基于SIDD和DND数据集，可能**无法完全代表所有真实世界噪声场景**（如低光、极端噪声等）。
- **效率验证不充分**：论文缺乏与其他方法在推理速度、内存占用方面的详细比较，其“更适用于实际应用”的论断需要更多效率数据支撑。
- **模块解释性**：尽管SAM和CAM有直觉上的解释，但它们具体如何筛选特征、在双支路中如何实现“互补”仍缺乏深入的可视化或理论分析。
## 个人评论

这篇论文最值得学习的点在于其**模块化的设计思想**和**多维度的特征处理策略**：
1.  **双支路互补设计**：展示了如何通过两个结构不同但功能互补的子网络（一个侧重局部与空间注意力，一个侧重扩大感受野与通道注意力）来协同工作，提升模型整体的特征捕获能力。这对于设计轻量且有效的网络有启发。
2.  **注意力模块的具体实现**：RAB和HDRAB提供了将**跳跃连接、卷积、不同类型的注意力（空间/通道）以及扩张卷积**有机结合的清晰范例。这种“即插即用”模块的设计思路值得借鉴。
3.  **平衡性能与复杂度的探索**：论文反复强调在“不过度增加深度”的前提下提升性能，并通过实验证明了双支路、长跳跃连接等设计的有效性。这为后续研究如何设计高效网络结构提供了参考。

### 使用建议

- **如果快速了解**：只读 **Abstract** 和 **Section 1 Introduction**，即可掌握研究动机、核心方法和主要贡献。
- **如果复现**：重点看 **Section 3 The proposed model**，特别是3.1（网络架构图）、3.2（RAB）和3.3（HDRAB）的结构描述和图表，以及 **Section 4.2 Experimental settings** 中的训练细节。
- **如果借鉴创新点**：
    1.  学习 **RAB** 如何融合多个跳跃连接和空间注意力（SAM）。
    2.  学习 **HDRAB** 如何结合混合扩张卷积与通道注意力（CAM）。
    3.  参考其**双支路+拼接融合**的整体架构设计思想。
- **如果写related work**：可放在 **图像去噪**、**注意力机制**、**残差学习**、**双流网络** 这几个类别下。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**计算机视觉与图像处理**领域的**图像去噪**方向。它旨在解决深度卷积神经网络在处理真实图像中的空间变化噪声（即真实噪声）时性能不佳的问题。其核心是通过设计新型的网络架构和注意力模块来提升模型的去噪能力与效率。根据提供的PDF文本中的主题“B_注意力算子模块”，这篇论文非常适合归类于**基于注意力机制的图像复原网络设计**这一主题下。

## 2. 一句话总结
本文提出了一种名为DRANet的双支路残差注意力网络，该网络包含两个创新的注意力模块——残差注意力模块（RAB）和混合扩张残差注意力模块（HDRAB），用于有效去除图像中的合成噪声和真实噪声。

## 3. 背景与问题
- **这篇论文为什么要做**: 传统的基于深度CNN的去噪方法在处理合成空间不变噪声（如加性高斯白噪声AWGN）时表现良好，但在去除图像采集或传输过程中产生的**空间变化的真实噪声**时效果不佳，这限制了其实际应用 (p.1)。
- **之前方法有什么问题**:
    1.  传统方法（如BM3D, WNNM）依赖于复杂的优化算法，导致**推理时间长**，且因超参数过多而**性能不稳定** (p.1)。
    2.  一些DNN方法通过增加网络深度来提升能力，但这会**增加参数量和推理时间**，难以部署或应用于实时场景 (p.2)。
    3.  一些现有的注意力去噪模型（如ADNet, RIDNet）虽然性能优异，但其**特征学习能力仍有提升空间** (p.2)。
- **作者想解决的核心矛盾**: 如何在**不过度增加网络深度和复杂度**的前提下，设计出既能捕获丰富局部特征，又能利用全局上下文信息，从而有效处理真实空间变化噪声的轻量高效去噪模型。

## 4. 核心贡献
1.  设计了一个新颖的**双支路残差注意力网络（DRANet）**用于图像盲去噪，该模型架构简洁，参数较少，对合成噪声和真实噪声均有效 (p.2)。
2.  提出了两个新的注意力模块：**残差注意力模块（RAB）**和**混合扩张残差注意力模块（HDRAB）**，分别用于模型的上、下分支，使模型能够捕获互补特征并进行有效的特征筛选 (p.2)。
3.  通过广泛的实验证明，DRANet在去噪性能上能与许多最先进的方法相竞争 (p.2)。

## 5. 方法详解
- **整体框架**: DRANet是一个**双支路并行结构**（如Fig. 1所示, p.4）。上分支包含5个**残差注意力模块（RAB）**，下分支包含5个**混合扩张残差注意力模块（HDRAB）**。两个分支的特征通过**拼接（Concat）** 进行全局融合。
- **输入输出**: 输入为带噪图像 `y`，输出为去噪图像 `\hat{x}`。
- **关键模块**:
    1.  **残差注意力模块（RAB，如Fig. 2所示, p.5）**:
        - **组成**: 由**残差块**和**空间注意力模块（SAM）**构成。
        - **残差块**: 包含多个标准卷积和ReLU激活，通过多个跳跃连接提取丰富的局部特征。
        - **SAM**: 用于学习卷积特征之间的**空间关系**。它使用全局平均池化（GAP）和全局最大池化（GMP）来表示图像的全局统计信息，从而聚焦有用特征并过滤不重要特征。其输出通过Sigmoid生成空间注意力图，与输入特征进行逐元素相乘。
        - **核心作用**: 捕获**局部特征**并通过**空间注意力**进行特征筛选。
    2.  **混合扩张残差注意力模块（HDRAB，如Fig. 3所示, p.5）**:
        - **组成**: 由**混合扩张残差块**和**通道注意力模块（CAM）**构成。
        - **混合扩张残差块**: 包含多个具有不同扩张率`s`（从1到4）的混合扩张卷积。扩张卷积能在**不增加参数和计算量**的情况下扩大感受野，而混合设计旨在**消除网格化现象**。
        - **CAM**: 用于学习卷积特征之间的**通道关系**。由GAP、卷积、ReLU和Sigmoid构成，生成通道注意力图，对特征通道进行加权。
        - **核心作用**: 在**扩大感受野**捕获更多图像信息的同时，通过**通道注意力**进行特征筛选。
- **模块之间怎么连接**:
    - 每个分支内部，RAB/HDRAB之间通过**长跳跃连接（Long skip connection）** 连接，以缓解梯度消失/爆炸并加速训练。
    - 两个并行分支最终通过**拼接（Concat）** 操作融合特征，以捕获全局图像特征。
- **数学公式或机制的直观解释**:
    - 训练阶段的损失函数：
        - 对于**合成噪声（AWGN）去除**：使用**均方误差（MSE）** (公式1, p.5)。
        - 对于**真实噪声去除**：为避免模糊效应，采用**Charbonnier损失**（Lchar，公式3）和**边缘损失**（Ledge，公式4，基于拉普拉斯算子）的加权和（公式2，权重λedge=0.1）。
- **训练方式**: 使用Adam优化器。合成噪声模型训练6×10⁵次迭代，初始学习率1×10⁻⁴；真实噪声模型训练120个epoch，初始学习率2×10⁻⁴并采用余弦退火策略 (p.6)。
- **推理流程**: 标准的前向传播过程，带噪图像输入网络，经过两个分支处理和特征融合后输出去噪图像。
- **和已有方法的差异**:
    - 相较于单纯加深网络（如ResNet），DRANet采用**加宽的双支路结构**，以更少的深度提升性能。
    - 相较于其他注意力模块（如[48, 49]中的残差注意力块），本文的**RAB拥有更多的跳跃连接**以增强特征提取与融合 (p.5)。
    - 相较于使用标准卷积的模块，本文的**HDRAB创新性地结合了混合扩张卷积和通道注意力**，在扩大感受野的同时进行特征选择 (p.5)。

## 6. 实验与结果
- **使用的数据集**:
    - **合成噪声训练**: Flickr2K (2650张高分辨率彩色图像) (p.6)。
    - **合成噪声测试**: Set12, BSD68, CBSD68, Kodak24, McMaster (p.6)。
    - **真实噪声训练**: SIDD Medium (320对图像) (p.6)。
    - **真实噪声测试**: SIDD 验证集, DND sRGB数据集 (p.6)。
- **对比方法**: BM3D, TNRD, DnCNN, IRCNN, FFDNet, BUIFD, BRDNet, DudeNet, ADNet, DSNetB, AINDNet, RIDNet, AirNet 等 (p.6)。
- **评价指标**: **PSNR** 和 **SSIM** (p.6)。
- **主实验结果**: PDF文本中**未提供**主实验（如AWGN去除、真实噪声去除）的具体对比数字结果（这些结果可能在文本未提供的第6页之后）。
- **消融实验**: 在BSD68数据集，噪声水平σ=30的AWGN上进行。
    - 上分支单独: 27.81 dB / 0.781 SSIM。
    - 下分支单独: 28.43 dB / 0.807 SSIM。
    - 无长跳跃连接: 28.55 dB / 0.808 SSIM。
    - 无残差学习: 28.54 dB / 0.807 SSIM。
    - **完整DRANet**: **28.56 dB / 0.808 SSIM** (Table 1, p.6)。
    - 结论：完整模型性能最佳，双支路和辅助连接设计有效。
- **泛化实验**: 模型在多个合成和真实数据集上进行测试，但具体泛化结果数字**未在提供的文本中找到**。
- **速度/参数量/FLOPs等效率信息**: PDF提供的文本中**未明确说明**具体的模型参数量、FLOPs或推理速度数据。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的点在于其**模块化的设计思想**和**多维度的特征处理策略**：
1.  **双支路互补设计**：展示了如何通过两个结构不同但功能互补的子网络（一个侧重局部与空间注意力，一个侧重扩大感受野与通道注意力）来协同工作，提升模型整体的特征捕获能力。这对于设计轻量且有效的网络有启发。
2.  **注意力模块的具体实现**：RAB和HDRAB提供了将**跳跃连接、卷积、不同类型的注意力（空间/通道）以及扩张卷积**有机结合的清晰范例。这种“即插即用”模块的设计思路值得借鉴。
3.  **平衡性能与复杂度的探索**：论文反复强调在“不过度增加深度”的前提下提升性能，并通过实验证明了双支路、长跳跃连接等设计的有效性。这为后续研究如何设计高效网络结构提供了参考。

## 8. 局限与问题
- **计算成本**：虽然作者声称DRANet参数较少，但**未在提供的文本中报告具体的参数量、FLOPs和推理时间**。双支路结构和拼接操作可能带来额外的计算开销。
- **数据集与场景**：真实噪声实验仅基于SIDD和DND数据集，可能**无法完全代表所有真实世界噪声场景**（如低光、极端噪声等）。
- **效率验证不充分**：论文缺乏与其他方法在推理速度、内存占用方面的详细比较，其“更适用于实际应用”的论断需要更多效率数据支撑。
- **模块解释性**：尽管SAM和CAM有直觉上的解释，但它们具体如何筛选特征、在双支路中如何实现“互补”仍缺乏深入的可视化或理论分析。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读 **Abstract** 和 **Section 1 Introduction**，即可掌握研究动机、核心方法和主要贡献。
- **如果复现**：重点看 **Section 3 The proposed model**，特别是3.1（网络架构图）、3.2（RAB）和3.3（HDRAB）的结构描述和图表，以及 **Section 4.2 Experimental settings** 中的训练细节。
- **如果借鉴创新点**：
    1.  学习 **RAB** 如何融合多个跳跃连接和空间注意力（SAM）。
    2.  学习 **HDRAB** 如何结合混合扩张卷积与通道注意力（CAM）。
    3.  参考其**双支路+拼接融合**的整体架构设计思想。
- **如果写related work**：可放在 **图像去噪**、**注意力机制**、**残差学习**、**双流网络** 这几个类别下。

## 10. 和其他论文的关系
基于论文内容和文件名`2023_注意力算子模块_Dual_Residual_图像去噪_注意力_网络_图像_去噪.pdf`，它很可能与以下主题的论文相关（使用`[[双链]]`表示可能的关联）：
- **注意力机制去噪网络**：[[RIDNet]]，[[RDAN]]，[[ADNet]]，[[RNAN]]，[[DeamNet]]。
- **双支路/双CNN去噪网络**：[[DualCNN]]，[[BRDNet]]，[[DudeNet]]，[[DCBDNet]]，[[DCANet]]。
- **基于扩张卷积的去噪网络**：[[DSNet]]，[[IRCNN]]。

## 11. 关键词
图像去噪， 双支路网络， 残差注意力块（RAB）， 混合扩张残差注意力块（HDRAB）， 空间注意力， 通道注意力， 混合扩张卷积， 真实噪声去除， 特征筛选， 长跳跃连接， 注意力机制。

## 12. 可信度说明
本精读笔记主要基于提供的PDF文本的**前12页**内容生成，包括摘要、引言、相关工作、方法（网络架构、RAB、HDRAB、损失函数）以及实验设置、消融实验部分。这些部分提供了关于论文动机、方法核心设计、实验框架的关键信息。
**局限性**：由于提供的文本仅覆盖论文的前12页（共18页），**第4.4节“主实验结果”及之后的具体定量结果（如各方法PSNR对比表）、参数量分析、更多可视化结果等关键信息缺失**。因此，笔记中关于主实验结果和效率分析的内容标注为“未找到”或“未在提供的文本中说明”。笔记中的所有信息均严格引自提供的文本，未进行编造。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/RAB&HDRAB.txt` (18/18 页; 原 AI 主体 12/18 + 全文补读 13-18); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-18; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-18。
- **提取情况**: 缺失页 6 页, 其中 6 页提取到可读文本。缺失页包含正文/附录内容, 其中约 3 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: The visual e
- p.14: Figure 6: Visual results of di
- p.14: 4.6. Model complexity analysis
- p.14: TNRD, MCWNNM, and TWSC were implemented in the Matlab (R2020a) environment, other denoising models
- p.14: The running time of the di
- p.15: Gray Color Gray Color Gray Color
- p.15: Table 9 gives the numbers of model parameters of the compared models, where the number of parameters of
- p.15: One can see that compared with many state-of-the-art image blind denoising models, such as the CBDNet, VDN,
- p.15: 5. Conclusion and future work
- p.15: Compared with other state-of-the-art methods, DRANet achieves competitive denoising performance on di
- p.16: Table 9: The numbers of parameters (in K) of di
- p.16: ModelsParameters

### 缺失页关键摘录

- p.13: Figure 5: Visual results of synthetic noise removal for color image at the noise level 50. (i) Ground-truth image, (ii) Noisy image /14.16dB, (iii)
- p.14: remove real noise, and the TWSC produces a blurred and over-smoothed result. In contrast, the AINDNet, VDN,
- p.14: DRANet obtains the leading PSNR and SSIM values. It can be seen that for real-world noise removal, the DRANet
- p.14: erent denoising models on the real-world noisy image. (i) Ground-truth image /(PSNR /SSIM), (ii) Noisy image /
- p.14: erent models is displayed in Table 8, where three synthetic images containing di
- p.15: erent denoising models at noise level 25. The time values in Table 8 are the results obtained by calculating
- p.15: Table 8: Running time (in seconds) evaluation results on three synthetic noisy images.
- p.15: Table 9 gives the numbers of model parameters of the compared models, where the number of parameters of
- p.16: Table 9: The numbers of parameters (in K) of di
- p.18: [63] A. Abdelhamed, S. Lin, M. S. Brown, A high-quality denoising dataset for smartphone cameras, IEEE Conference on Computer Vision and
<!-- AI_READING_NOTE_END -->
