---
title: "Run, Don’t Walk: Chasing Higher FLOPS for Faster Neural Networks"
authors:
  - "Jierun Chen"
  - "Shiu-hong Kao"
  - "Hao He"
  - "Weipeng Zhuo"
  - "Song Wen"
  - "Chul-Ho Lee"
  - "S.-H. Gary Chan"
year: 2023
venue: By nature, PConv has lower FLOPs than the regular Conv
doi: 
pdf: [[PConv.pdf]]
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
extract_cache: .paper-cache/extracts/PConv.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# Run, Don’t Walk: Chasing Higher FLOPS for Faster Neural Networks

## 基本信息
- **PDF**: [[PConv.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Run, Don’t Walk: Chasing Higher FLOPS for Faster Neural Networks |
| **作者** | Jierun Chen; Shiu-hong Kao; Hao He; Weipeng Zhuo; Song Wen; Chul-Ho Lee; S.-H. Gary Chan |
| **发表时间** | 2023 |
| **刊物/会议** | By nature, PConv has lower FLOPs than the regular Conv |
| **DOI** | 未明确 |

## 摘要

> ∗ … = ∗ … = To design fast neural networks, many works have been focusing on reducing the number of floating-point opera- (a) Convolution (b) Depthwise/GroupConvolution tions (FLOPs). We observe that such reduction in FLOPs, however, doesnotnecessarilyleadtoasimilarlevelofre- ductioninlatency. Thismainlystemsfrominefficientlylow Input/output Filter floating-point operations per second (FLOPS). To achieve ∗ … = ∗ Convolution faster networks, we revisit popular operators and demon- (c) Partial Convolution (ours) Identity stratethatsuchlowFLOPSismainlyduetofrequentmem- Figure1. Ourpartialconvolution(PConv)isfastandefficientby ory access of the operators, especially the depthwise con- applying filters on only a few input channels while leaving the volution. We hence propose a novel partial convolution remainingonesuntouched. PConvobtainslowerFLOPsthanthe (PConv) that extracts spatial features more efficiently, by regularconvolutionandhigherFLOPSthanthedepthwise/group cutting down redundant

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：设计低延迟、高吞吐的快速神经网络对于实时应用至关重要。传统方法主要关注减少模型的浮点运算次数（FLOPs），但作者发现，FLOPs的减少并不总能带来相应的延迟降低。
- **之前方法有什么问题**：以深度可分离卷积（DWConv）为代表的主流轻量化算子，虽然大幅降低了FLOPs，但会引入频繁的内存访问和低效的计算模式，导致**有效计算速度（FLOPS）很低**。此外，许多网络还引入了拼接、通道混洗等额外数据操作，进一步拖慢速度。即使是ViT/MLP类模型，也因依赖DWConv或复杂的注意力机制而存在类似问题。
- **作者想解决的核心矛盾**：**FLOPs降低与实际延迟降低之间的矛盾**。目标是设计一种新算子，在减少FLOPs的同时，不降低甚至提高设备的实际计算利用率（FLOPS），从而真正实现低延迟。
## 关键贡献

1.  **指出了优化FLOPS的重要性**：强调了在降低FLOPs的同时必须考虑计算速度（FLOPS），才能实现真正的低延迟。
2.  **提出了部分卷积（PConv）算子**：一种简单、高效、硬件友好的卷积算子，通过对特征图的部分通道（如1/4）进行常规卷积，同时减少计算量和内存访问，具有比DWConv更高的FLOPS。
3.  **设计了FasterNet网络家族**：基于PConv和逐点卷积（PWConv）构建的全新骨干网络，在多种视觉任务（分类、检测、分割）上实现了高精度和极低延迟。
4.  **提供了广泛的实验验证**：在GPU、CPU和ARM处理器上验证了PConv和FasterNet的高速度和有效性，并展示了其在ImageNet、COCO等标准数据集上的竞争力。
## 方法

- **整体框架**：FasterNet是一个分层的卷积神经网络，由四个阶段组成。每个阶段以嵌入层（Embedding）或合并层（Merging）开始进行空间下采样和通道扩展，随后堆叠多个FasterNet块。最后使用全局平均池化、1x1卷积和全连接层进行分类。
- **输入输出**：输入为图像，输出为分类标签或用于下游任务的特征图。
- **关键模块**：
    1.  **部分卷积（PConv）**：核心算子。对于输入特征图 `I ∈ R^(c×h×w)`，PConv只选取前 `c_p` 个连续通道（通常取 `r = c_p / c = 1/4`）应用一个常规的 `k×k` 卷积（如3x3），其余通道保持不变。其FLOPs为 `h×w×k²×c_p²`，内存访问约为 `h×w×2c_p`。
    2.  **逐点卷积（PWConv）**：即1x1卷积，紧跟在PConv之后。**PConv + PWConv** 的组合在功能上等效于一个 **T形卷积**（T-shaped Conv），更关注感受野的中心位置，这与特征重要性分析（中心位置权重更大）相吻合。
    3.  **FasterNet块**：每个块由一个PConv层和两个PWConv层构成，形成一个类似倒残差的结构，中间PWConv层会扩展通道数。块之间使用残差连接。**与标准ResNet块的关键区别**在于：将批归一化（BN）和激活函数（如GELU/ReLU）**仅放置在中间PWConv层之后**，以保留特征多样性并减少计算延迟。
- **模块间连接**：PConv处理部分空间特征 -> PWConv（1x1卷积）混合所有通道信息 -> 第二个PWConv调整通道数并添加残差连接。
- **数学公式**：PConv的FLOPs公式见上文。论文通过理论推导证明，将T形卷积分解为PConv+PWConv比直接使用T形卷积更节省FLOPs。
- **训练方式**：使用标准的分类、检测、分割训练流程。在推理时，BN层会被融合到相邻的卷积层中以加速。
- **推理流程**：前向传播依次通过嵌入/合并层、四个阶段的FasterNet块、最后的全局池化和分类层。
- **和已有方法的差异**：
    - **与DWConv/GConv相比**：PConv利用特征图通道间的冗余，而DWConv利用滤波器冗余。PConv具有**更高的FLOPS和更低的内存访问**，无需为补偿精度而过度增加通道宽度。
    - **与常规Conv相比**：PConv的FLOPs和内存访问均大幅降低。
    - **与注意力机制相比**：PConv是纯粹的卷积操作，更简单、更易部署，不依赖特殊硬件支持。
- **论文类型特化（通用视觉Backbone）**：本文提出的是通用特征提取骨干网络，主要创新点在于底层算子（PConv）设计，而非特定的注意力维度或任务特定模块。
## 实验

- **使用的数据集**：ImageNet-1k（分类），COCO（检测），ADE20K（分割）。
- **对比方法**：MobileViT-XXS, MobileNetV3, EfficientNet, Swin-B, CycleMLP-B1, ResNet50等。
- **评价指标**：Top-1准确率、延迟（Latency）、吞吐量（Throughput）、FLOPs、参数量。
- **主实验结果**：
    - **分类（ImageNet-1k）**：FasterNet-T0比MobileViT-XXS快2.8×(GPU)、3.3×(CPU)、2.4×(ARM)，且准确率高2.9%。FasterNet-L达到83.5% top-1准确率，与Swin-B相当，但GPU吞吐量高36%，CPU计算时间节省37%。
    - **检测与分割**：在COCO和ADE20K上，基于FasterNet骨干的模型在速度和精度上均表现优异。
- **消融实验**：
    - **PConv算子效率**：PConv的FLOPS远高于DWConv和GConv，同时FLOPs远低于常规Conv（见论文Table 1）。
    - **PConv+PWConv的有效性**：在近似常规卷积特征变换的任务中，PConv+PWConv的测试损失最低（见论文Table 2）。
    - **归一化与激活函数位置**：仅在中间PWConv后使用BN和激活函数能提升性能并降低延迟。
- **泛化实验**：在不同设备（GPU, CPU, ARM）和不同视觉任务上均验证了通用性。
- **速度/参数量/FLOPs**：论文强调，FasterNet在相同或更低FLOPs下，实现了显著更低的延迟和更高的吞吐量。
## 局限

1.  **场景依赖性**：PConv的有效性依赖于特征图通道间存在足够冗余的假设。在极低计算预算或任务非常特殊的情况下，DWConv或更激进的轻量化方法可能仍是更优解。
2.  **实验范围**：主要实验集中在主流视觉任务和标准数据集上，在更复杂的场景（如视频、多模态、域自适应）中的表现未知。
3.  **理论深度**：对PConv为何能有效提取空间特征，除了T形感受野的直观解释和位置重要性分析外，更深入的理论分析较少。
4.  **复现风险**：虽然代码已开源，但在不同硬件和软件环境下，延迟的绝对数值可能有差异，但相对趋势应一致。
## 个人评论

1.  **问题洞察深刻**：明确提出“FLOPs不等于延迟”，并指出**内存访问是关键瓶颈**，这为后续高效网络设计提供了更本质的视角。
2.  **算子设计思路新颖**：PConv的设计非常巧妙，利用了特征图通道的冗余性，用最简单的“只卷积一部分”思路，同时攻击了计算量和内存访问两个痛点。
3.  **工程导向强**：PConv实现简单（基于现有卷积算子），不引入特殊结构，硬件友好，易于部署和复现。
4.  **启发性**：启示研究者在设计算子时，不仅要考虑理论计算量（FLOPs），更要关注其在真实硬件上的计算效率（FLOPS）和内存访问模式。对特征图冗余性的利用是一个值得深入探索的方向。

### 使用建议

- **如果快速了解**：阅读**摘要**和**引言**，查看**图1、图4**理解PConv和FasterNet的设计，浏览**实验部分的关键表格**（如Table 1, Table 3）。
- **如果复现**：重点看**3.2节（PConv设计）** 和**3.4节（FasterNet架构）**，并参考**附录**（论文中提到）的具体架构规格表。代码仓库是重要参考。
- **如果借鉴创新点**：
    - 学习PConv“部分卷积”的思想，可尝试将其应用于自己模型的任意阶段，替代DWConv。
    - 借鉴“只在必要时使用归一化和激活函数”的设计哲学。
    - 思考如何针对自己模型的特征图冗余性进行优化。
- **如果写related work**：可放在“高效卷积算子设计”（如与DWConv, GConv对比）或“轻量级网络架构设计”（如与MobileNet, ShuffleNet对比）的部分。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**高效神经网络设计**方向，具体聚焦于**设计更快的卷积算子**。它解决的核心问题是：现有轻量级网络（如MobileNet）在追求低FLOPs时，由于频繁的内存访问导致实际运行速度（延迟/吞吐量）并未得到预期提升，即**FLOPs与延迟之间存在不匹配**。因此，本文适合放在 **“B_注意力算子模块”** 或更广泛的 **“高效网络设计与推理加速”** 主题下。

## 2. 一句话总结
本文提出**部分卷积（PConv）** 算子，通过仅对输入特征图的一部分通道应用常规卷积，在显著降低计算量（FLOPs）的同时，大幅减少内存访问，从而获得更高的有效计算速度（FLOPS），并基于此构建了真正快速的**FasterNet**网络家族。

## 3. 背景与问题
- **这篇论文为什么要做**：设计低延迟、高吞吐的快速神经网络对于实时应用至关重要。传统方法主要关注减少模型的浮点运算次数（FLOPs），但作者发现，FLOPs的减少并不总能带来相应的延迟降低。
- **之前方法有什么问题**：以深度可分离卷积（DWConv）为代表的主流轻量化算子，虽然大幅降低了FLOPs，但会引入频繁的内存访问和低效的计算模式，导致**有效计算速度（FLOPS）很低**。此外，许多网络还引入了拼接、通道混洗等额外数据操作，进一步拖慢速度。即使是ViT/MLP类模型，也因依赖DWConv或复杂的注意力机制而存在类似问题。
- **作者想解决的核心矛盾**：**FLOPs降低与实际延迟降低之间的矛盾**。目标是设计一种新算子，在减少FLOPs的同时，不降低甚至提高设备的实际计算利用率（FLOPS），从而真正实现低延迟。

## 4. 核心贡献
1.  **指出了优化FLOPS的重要性**：强调了在降低FLOPs的同时必须考虑计算速度（FLOPS），才能实现真正的低延迟。
2.  **提出了部分卷积（PConv）算子**：一种简单、高效、硬件友好的卷积算子，通过对特征图的部分通道（如1/4）进行常规卷积，同时减少计算量和内存访问，具有比DWConv更高的FLOPS。
3.  **设计了FasterNet网络家族**：基于PConv和逐点卷积（PWConv）构建的全新骨干网络，在多种视觉任务（分类、检测、分割）上实现了高精度和极低延迟。
4.  **提供了广泛的实验验证**：在GPU、CPU和ARM处理器上验证了PConv和FasterNet的高速度和有效性，并展示了其在ImageNet、COCO等标准数据集上的竞争力。

## 5. 方法详解
- **整体框架**：FasterNet是一个分层的卷积神经网络，由四个阶段组成。每个阶段以嵌入层（Embedding）或合并层（Merging）开始进行空间下采样和通道扩展，随后堆叠多个FasterNet块。最后使用全局平均池化、1x1卷积和全连接层进行分类。
- **输入输出**：输入为图像，输出为分类标签或用于下游任务的特征图。
- **关键模块**：
    1.  **部分卷积（PConv）**：核心算子。对于输入特征图 `I ∈ R^(c×h×w)`，PConv只选取前 `c_p` 个连续通道（通常取 `r = c_p / c = 1/4`）应用一个常规的 `k×k` 卷积（如3x3），其余通道保持不变。其FLOPs为 `h×w×k²×c_p²`，内存访问约为 `h×w×2c_p`。
    2.  **逐点卷积（PWConv）**：即1x1卷积，紧跟在PConv之后。**PConv + PWConv** 的组合在功能上等效于一个 **T形卷积**（T-shaped Conv），更关注感受野的中心位置，这与特征重要性分析（中心位置权重更大）相吻合。
    3.  **FasterNet块**：每个块由一个PConv层和两个PWConv层构成，形成一个类似倒残差的结构，中间PWConv层会扩展通道数。块之间使用残差连接。**与标准ResNet块的关键区别**在于：将批归一化（BN）和激活函数（如GELU/ReLU）**仅放置在中间PWConv层之后**，以保留特征多样性并减少计算延迟。
- **模块间连接**：PConv处理部分空间特征 -> PWConv（1x1卷积）混合所有通道信息 -> 第二个PWConv调整通道数并添加残差连接。
- **数学公式**：PConv的FLOPs公式见上文。论文通过理论推导证明，将T形卷积分解为PConv+PWConv比直接使用T形卷积更节省FLOPs。
- **训练方式**：使用标准的分类、检测、分割训练流程。在推理时，BN层会被融合到相邻的卷积层中以加速。
- **推理流程**：前向传播依次通过嵌入/合并层、四个阶段的FasterNet块、最后的全局池化和分类层。
- **和已有方法的差异**：
    - **与DWConv/GConv相比**：PConv利用特征图通道间的冗余，而DWConv利用滤波器冗余。PConv具有**更高的FLOPS和更低的内存访问**，无需为补偿精度而过度增加通道宽度。
    - **与常规Conv相比**：PConv的FLOPs和内存访问均大幅降低。
    - **与注意力机制相比**：PConv是纯粹的卷积操作，更简单、更易部署，不依赖特殊硬件支持。
- **论文类型特化（通用视觉Backbone）**：本文提出的是通用特征提取骨干网络，主要创新点在于底层算子（PConv）设计，而非特定的注意力维度或任务特定模块。

## 6. 实验与结果
- **使用的数据集**：ImageNet-1k（分类），COCO（检测），ADE20K（分割）。
- **对比方法**：MobileViT-XXS, MobileNetV3, EfficientNet, Swin-B, CycleMLP-B1, ResNet50等。
- **评价指标**：Top-1准确率、延迟（Latency）、吞吐量（Throughput）、FLOPs、参数量。
- **主实验结果**：
    - **分类（ImageNet-1k）**：FasterNet-T0比MobileViT-XXS快2.8×(GPU)、3.3×(CPU)、2.4×(ARM)，且准确率高2.9%。FasterNet-L达到83.5% top-1准确率，与Swin-B相当，但GPU吞吐量高36%，CPU计算时间节省37%。
    - **检测与分割**：在COCO和ADE20K上，基于FasterNet骨干的模型在速度和精度上均表现优异。
- **消融实验**：
    - **PConv算子效率**：PConv的FLOPS远高于DWConv和GConv，同时FLOPs远低于常规Conv（见论文Table 1）。
    - **PConv+PWConv的有效性**：在近似常规卷积特征变换的任务中，PConv+PWConv的测试损失最低（见论文Table 2）。
    - **归一化与激活函数位置**：仅在中间PWConv后使用BN和激活函数能提升性能并降低延迟。
- **泛化实验**：在不同设备（GPU, CPU, ARM）和不同视觉任务上均验证了通用性。
- **速度/参数量/FLOPs**：论文强调，FasterNet在相同或更低FLOPs下，实现了显著更低的延迟和更高的吞吐量。

## 7. 这篇论文真正有价值的地方
1.  **问题洞察深刻**：明确提出“FLOPs不等于延迟”，并指出**内存访问是关键瓶颈**，这为后续高效网络设计提供了更本质的视角。
2.  **算子设计思路新颖**：PConv的设计非常巧妙，利用了特征图通道的冗余性，用最简单的“只卷积一部分”思路，同时攻击了计算量和内存访问两个痛点。
3.  **工程导向强**：PConv实现简单（基于现有卷积算子），不引入特殊结构，硬件友好，易于部署和复现。
4.  **启发性**：启示研究者在设计算子时，不仅要考虑理论计算量（FLOPs），更要关注其在真实硬件上的计算效率（FLOPS）和内存访问模式。对特征图冗余性的利用是一个值得深入探索的方向。

## 8. 局限与问题
1.  **场景依赖性**：PConv的有效性依赖于特征图通道间存在足够冗余的假设。在极低计算预算或任务非常特殊的情况下，DWConv或更激进的轻量化方法可能仍是更优解。
2.  **实验范围**：主要实验集中在主流视觉任务和标准数据集上，在更复杂的场景（如视频、多模态、域自适应）中的表现未知。
3.  **理论深度**：对PConv为何能有效提取空间特征，除了T形感受野的直观解释和位置重要性分析外，更深入的理论分析较少。
4.  **复现风险**：虽然代码已开源，但在不同硬件和软件环境下，延迟的绝对数值可能有差异，但相对趋势应一致。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：阅读**摘要**和**引言**，查看**图1、图4**理解PConv和FasterNet的设计，浏览**实验部分的关键表格**（如Table 1, Table 3）。
- **如果复现**：重点看**3.2节（PConv设计）** 和**3.4节（FasterNet架构）**，并参考**附录**（论文中提到）的具体架构规格表。代码仓库是重要参考。
- **如果借鉴创新点**：
    - 学习PConv“部分卷积”的思想，可尝试将其应用于自己模型的任意阶段，替代DWConv。
    - 借鉴“只在必要时使用归一化和激活函数”的设计哲学。
    - 思考如何针对自己模型的特征图冗余性进行优化。
- **如果写related work**：可放在“高效卷积算子设计”（如与DWConv, GConv对比）或“轻量级网络架构设计”（如与MobileNet, ShuffleNet对比）的部分。

## 10. 和其他论文的关系
- 与轻量级卷积网络相关：`[[MobileNet系列]]`， `[[ShuffleNet]]`， `[[GhostNet]]`
- 与高效Transformer相关：`[[MobileViT]]`， `[[EfficientFormer]]`
- 与分析计算瓶颈的论文相关：后续可能会有专门分析`[[内存访问]]`或`[[计算图优化]]`的工作引用本文。
（注：由于知识库主题和文件名是“B_注意力算子模块”，而本文核心是卷积算子，直接关联的确定性不高，故此处链接较少，避免乱连。）

## 11. 关键词
Partial Convolution (PConv), FLOPS, Efficient Neural Networks, Low-Latency Inference, Memory Access Optimization, FasterNet, Depthwise Convolution (DWConv), Lightweight Architecture, Image Classification, Hardware-Friendly Design.

## 12. 可信度说明
本篇精读笔记主要基于用户提供的PDF提取文本（论文前12页）生成。该文本覆盖了论文的摘要、引言、相关工作、核心方法（PConv和FasterNet设计）、以及大部分实验结果（包括关键对比表格和图表说明）。文本提取质量良好，核心思想、关键公式、主要实验数据均得以保留。对于论文末尾（如附录中的详细架构表、更多消融实验）的信息，由于文本未提供，故未在笔记中编造。所有数字均严格引用于提供的文本。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/PConv.txt` (15/15 页; 原 AI 主体 12/15 + 全文补读 13-15); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Accelerating deep network training by reducing internal co-
- p.13: Imagenet classification with deep convolutional neural net-
- p.13: Mengchen Liu, Lu Yuan, Zicheng Liu, Lei Zhang, and Nuno
- p.13: Fitsum A Reda, Karan Sapra, Zhiding Yu, Xiaodong Yang,
- p.13: Proceedings of the IEEE/CVF Conference on Computer Vi-
- p.13: Proceedings of the IEEE/CVF International Conference on
- p.13: Hang Xu, Weiguo Gao, Chunjing Xu, Tao Xiang, and Li
- p.13: Shufflenet v2: Practical guidelines for efficient cnn architec-
- p.13: Cholakkal, Salman Khan, Syed Waqas Zamir, Rao Muham-
- p.13: Dudziak, Hongsheng Li, Georgios Tzimiropoulos, and Brais
- p.14: IEEE conference on computer vision and pattern recogni-
- p.14: Conference on Computer Vision and Pattern Recognition ,

### 缺失页关键摘录

- p.13: extremely low flops. In Proceedings of the IEEE/CVF In-
<!-- AI_READING_NOTE_END -->
