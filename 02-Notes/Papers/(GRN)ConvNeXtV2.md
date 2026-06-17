---
title: "ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders"
authors:
  - "Sanghyun Woo"
  - "Shoubhik Debnath"
  - "Ronghang Hu"
  - "Xinlei Chen"
  - "Zhuang Liu"
  - "In So Kweon"
  - "Saining Xie"
year: 2023
venue: "CVPR"
doi: "10.1109/CVPR52729.2023.01548"
arxiv: "2301.00808"
pdf: [[(GRN)ConvNeXtV2.pdf]]
primary_topic: B_注意力算子模块
topics:
  - "B_注意力算子模块"
status: read
reading_stage: manual-reviewed
confidence: high
source_basis: pdf-text
document_type: paper
date_added: 2026-06-03
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: true
human_reviewed_at: 2026-06-08
review_basis: "PDF full text pages 1-15; CVPR Open Access metadata"
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/(GRN)ConvNeXtV2.txt
---

# ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders

## 基本信息
- **PDF**: [[(GRN)ConvNeXtV2.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders |
| **作者** | Sanghyun Woo; Shoubhik Debnath; Ronghang Hu; Xinlei Chen; Zhuang Liu; In So Kweon; Saining Xie |
| **发表时间** | 2023 |
| **刊物/会议** | CVPR |
| **DOI** | 10.1109/CVPR52729.2023.01548 |

## 摘要

> 86.0 Drivenbyimprovedarchitecturesandbetterrepresenta- tionlearningframeworks,thefieldofvisualrecognitionhas 84.0 enjoyedrapidmodernizationandperformanceboostinthe early 2020s. For example, modern ConvNets, represented 82.0 byConvNeXt[52],havedemonstratedstrongperformance in various scenarios. While these models were originally 80.0 designed for supervised learning with ImageNet labels, theycanalsopotentiallybenefitfromself-supervisedlearn- 78.0 ing techniques such as masked autoencoders (MAE) [31]. However, we found that simply combining these two ap- 76.0 proaches leads to subpar performance. In this paper, we propose a fully convolutional masked autoencoder frame- work and a new Global Response Normalization (GRN) 74.0 Atto Femto Pico Nano Tiny Base Large Huge layer that can be added to the ConvNeXt architecture to enhanceinter-channelfeaturecompetition. Thisco-design ofself-supervisedlearningtechniquesandarchitecturalim- provement results in a new model family called ConvNeXt V2, w

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：视觉表征学习的进步依赖于架构创新、训练方法和数据。虽然ConvNeXt架构证明了纯卷积模型也具备强大的可扩展性，但其最初是为监督学习设计的。与此同时，自监督学习方法（如掩码自编码器MAE）已成为表征学习的主流范式。然而，直接将MAE应用于ConvNeXt架构会导致性能不佳（“subpar performance”）。
- **之前方法的问题**：1）MAE的非对称编码器-解码器设计是为Transformer的序列处理能力优化的，不适用于使用密集滑动窗口的卷积网络。2）直接在卷积网络上进行基于掩码的自监督训练很困难，且实验证据表明Transformer和ConvNets可能具有不同的特征学习行为。3）直接组合现有架构和训练方法无法达到最优性能。
- **核心矛盾**：如何让以密集计算为特性的卷积网络，有效地适配到以处理“稀疏可见patches”为核心的掩码自编码器预训练框架中，并解决因此产生的特征表示质量问题。
## 关键贡献

1. **提出了全卷积掩码自编码器（FCMAE）框架**：通过将掩码输入视为稀疏数据，并利用稀疏卷积使编码器仅处理可见像素，成功将MAE适配到纯卷积网络中。
2. **提出了全局响应归一化（GRN）层**：一个轻量、无额外参数（除了两个可学习缩放/偏置参数）的模块，通过全局特征聚合和divisive normalization促进通道间的特征竞争，有效解决了在FCMAE训练中观察到的“特征坍缩”问题。
3. **协同设计了ConvNeXt V2模型家族**：将GRN层整合到ConvNeXt架构中，移除了LayerScale，并联合FCMAE框架进行训练，形成了一套有效的模型与训练方案。
4. **发布了多样化的预训练模型**：提供了从高效的3.7M参数Atto模型到650M参数Huge模型的完整系列，并在多个视觉基准上取得了显著的性能提升。
5. **通过实验验证了协同设计的必要性**：发现仅使用FCMAE预训练的ConvNeXt V1模型性能仍不及最佳监督模型，而加入GRN后（ConvNeXt V2）的自监督预训练性能则显著超越了监督基线。
## 方法

本文的方法是架构（GRN）与训练框架（FCMAE）的协同设计。

- **整体框架**：FCMAE框架包含一个基于稀疏卷积的ConvNeXt编码器和一个轻量的单个ConvNeXt块解码器。预训练任务是随机掩盖输入图像的大部分区域（60%），让模型重建被掩盖的区域。
- **输入输出**：输入为原始图像，经过随机掩码（生成稀疏像素集）后送入编码器；输出是重建的图像像素。
- **关键模块**：
  1. **稀疏卷积编码器**：为了处理掩码后的稀疏输入，避免信息泄露，作者将ConvNeXt编码器中的标准卷积层替换为**子流形稀疏卷积**。这种卷积只在有数据的点（即可见像素）上进行计算，从而阻止了模型从掩码区域复制信息的捷径。在微调阶段，这些稀疏卷积层的权重可以无缝转换回标准密集卷积。
  2. **轻量解码器**：使用一个单独的ConvNeXt块（维度设为512）作为解码器。实验表明，这种简单的解码器在微调精度和预训练效率上优于更复杂的解码器（如UNet、Transformer）。
  3. **全局响应归一化（GRN）层**：这是解决特征坍缩的核心。GRN被插入到ConvNeXt模块的MLP之后，其计算过程分为三步：
     a) **全局特征聚合**：对每个通道的特征图进行L2范数计算，得到一个全局的通道重要性向量。
     b) **特征归一化**：使用divisive normalization，计算每个通道的L2范数相对于所有通道L2范数之和的比值，从而衡量该通道的相对重要性。
     c) **特征校准**：将归一化后的权重乘回原始特征图，并加上一个残差连接。
     其核心公式为：`Xi = γ * Xi * ( ||Xi|| / ∑j||Xj|| ) + β + Xi`，其中γ和β是可学习的缩放和偏置参数（初始化为0），用于保证训练初期层的功能为恒等映射。
- **训练方式**：在ImageNet-1K上进行800个epoch的FCMAE预训练，然后在下游任务上进行100个epoch的端到端微调。
- **推理流程**：预训练完成后，模型可以转换为标准ConvNeXt架构（稀疏卷积转为密集卷积），用于各种下游任务的推理。
- **与已有方法的差异**：
  - **与标准MAE**：标准MAE使用Transformer，依赖掩码令牌（mask tokens）输入；FCMAE使用稀疏卷积，不引入掩码令牌，避免了训练/测试不一致和效率问题。
  - **与监督ConvNeXt**：ConvNeXt V2通过加入GRN并采用自监督预训练，在相同架构下获得了更好的性能。
  - **与其他归一化/注意力**：GRN不同于LayerNorm（LN）或BatchNorm（BN），它不进行特征中心化或方差归一化，而是通过全局聚合和divisive normalization直接促进通道间的竞争；与SE等通道注意力模块相比，GRN不增加参数量（除了两个标量参数），且其归一化操作基于所有通道的响应。
- **论文类型特化（注意力类）**：GRN作用于通道维度，通过聚合全局空间信息来重新校准每个通道的响应，是一种**通道注意力机制**。它可即插即用到网络中（文中插入在MLP后），其计算开销很小（仅涉及范数计算和除法），但能有效提升特征多样性和模型性能。
## 实验

- **ImageNet-1K 分类**: ConvNeXt V2 通过 FCMAE 预训练 + GRN 在多个模型尺度上稳定超过 ConvNeXt V1。Atto 模型约 3.7M 参数达到约 76.7/76.8% Top-1, Huge 模型约 650M 参数在公开数据下达到 88.9%。
- **COCO / ADE20K 迁移**: 论文报告 ConvNeXt V2 在目标检测、实例分割和语义分割上也优于对应的 ConvNeXt V1, 说明 FCMAE 学到的表征可迁移到密集预测任务。
- **关键消融**: GRN 的全局聚合、divisive normalization 和残差校准要同时存在才稳定有效。masking ratio 在 0.5-0.7 区间较好, 0.6 最优。
- **与对比式 SSL 对比**: 在 ConvNeXt V2-Base 上, FCMAE 微调结果为 84.9, 高于 MoCo v3 的 83.7 和 300 epoch 监督基线 84.3。

## 局限

- 论文主要证明了 ImageNet/COCO/ADE20K 这类通用视觉基准, 对医学、遥感、小样本等领域迁移没有直接实验。
- FCMAE 预训练需要 800 epoch, 算力门槛不低；稀疏卷积在不同硬件和框架上的实际吞吐收益需要单独评估。
- GRN 解决了观察到的特征坍缩, 但论文更偏经验分析, 对坍缩机制的理论解释有限。

## 个人评论

这篇的价值不只是提出一个 GRN 小模块, 而是说明“自监督目标 + 架构模块”需要一起设计。对自己的模块改进工作来说, GRN 是一个很适合复用的基线: 参数少、实现简单、消融完整, 可以和 SE/CBAM/ECA 等通道重标定方法放在同一组对比。

## 人工复核记录

- **复核日期**: 2026-06-08
- **复核范围**: PDF 1-15 页全文；原 AI 缓存只覆盖 12/15 页。
- **元数据修正**: 年份从误提取的 2020 改为 2023；venue 补为 CVPR；补全 7 位作者、DOI 和 arXiv 编号。
- **补读页 13-15 的新增信息**: 第 13 页补充 masking ratio 消融, 0.6 效果最好；同页给出与 MoCo v3 的 SSL 对比, FCMAE 84.9 高于 MoCo v3 83.7 和监督基线 84.3；第 14-15 页主要是参考文献。
- **当前判断**: 可作为 GRN / 通道竞争 / ConvNeXt 自监督预训练的核心论文。后续若写综述, 建议和 [[CBAM]]、[[SE]]、[[ECA]]、[[MAE]]、[[ConvNeXt]] 放在一组。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中的表征学习方向，特别是卷积神经网络（ConvNets）与自监督学习（SSL）的结合。它旨在解决“如何让纯卷积架构（以ConvNeXt为代表）有效利用掩码自编码器（MAE）进行自监督预训练”的问题，并为此协同设计了一个新的网络架构（ConvNeXt V2）和一个专用的自监督学习框架（FCMAE）。论文的核心主题是提出一种新的注意力类算子——全局响应归一化（GRN），以增强通道间的特征竞争。因此，它非常适合放在“B_注意力算子模块”这一主题下。

## 2. 一句话总结
这篇论文提出了一个全卷积掩码自编码器（FCMAE）框架和一个用于增强通道间特征竞争的全局响应归一化（GRN）层，通过架构与自监督学习框架的协同设计，显著提升了纯卷积网络（ConvNeXt）在各种视觉识别任务上的性能。

## 3. 背景与问题
- **为什么要做**：视觉表征学习的进步依赖于架构创新、训练方法和数据。虽然ConvNeXt架构证明了纯卷积模型也具备强大的可扩展性，但其最初是为监督学习设计的。与此同时，自监督学习方法（如掩码自编码器MAE）已成为表征学习的主流范式。然而，直接将MAE应用于ConvNeXt架构会导致性能不佳（“subpar performance”）。
- **之前方法的问题**：1）MAE的非对称编码器-解码器设计是为Transformer的序列处理能力优化的，不适用于使用密集滑动窗口的卷积网络。2）直接在卷积网络上进行基于掩码的自监督训练很困难，且实验证据表明Transformer和ConvNets可能具有不同的特征学习行为。3）直接组合现有架构和训练方法无法达到最优性能。
- **核心矛盾**：如何让以密集计算为特性的卷积网络，有效地适配到以处理“稀疏可见patches”为核心的掩码自编码器预训练框架中，并解决因此产生的特征表示质量问题。

## 4. 核心贡献
1. **提出了全卷积掩码自编码器（FCMAE）框架**：通过将掩码输入视为稀疏数据，并利用稀疏卷积使编码器仅处理可见像素，成功将MAE适配到纯卷积网络中。
2. **提出了全局响应归一化（GRN）层**：一个轻量、无额外参数（除了两个可学习缩放/偏置参数）的模块，通过全局特征聚合和divisive normalization促进通道间的特征竞争，有效解决了在FCMAE训练中观察到的“特征坍缩”问题。
3. **协同设计了ConvNeXt V2模型家族**：将GRN层整合到ConvNeXt架构中，移除了LayerScale，并联合FCMAE框架进行训练，形成了一套有效的模型与训练方案。
4. **发布了多样化的预训练模型**：提供了从高效的3.7M参数Atto模型到650M参数Huge模型的完整系列，并在多个视觉基准上取得了显著的性能提升。
5. **通过实验验证了协同设计的必要性**：发现仅使用FCMAE预训练的ConvNeXt V1模型性能仍不及最佳监督模型，而加入GRN后（ConvNeXt V2）的自监督预训练性能则显著超越了监督基线。

## 5. 方法详解
本文的方法是架构（GRN）与训练框架（FCMAE）的协同设计。

- **整体框架**：FCMAE框架包含一个基于稀疏卷积的ConvNeXt编码器和一个轻量的单个ConvNeXt块解码器。预训练任务是随机掩盖输入图像的大部分区域（60%），让模型重建被掩盖的区域。
- **输入输出**：输入为原始图像，经过随机掩码（生成稀疏像素集）后送入编码器；输出是重建的图像像素。
- **关键模块**：
  1. **稀疏卷积编码器**：为了处理掩码后的稀疏输入，避免信息泄露，作者将ConvNeXt编码器中的标准卷积层替换为**子流形稀疏卷积**。这种卷积只在有数据的点（即可见像素）上进行计算，从而阻止了模型从掩码区域复制信息的捷径。在微调阶段，这些稀疏卷积层的权重可以无缝转换回标准密集卷积。
  2. **轻量解码器**：使用一个单独的ConvNeXt块（维度设为512）作为解码器。实验表明，这种简单的解码器在微调精度和预训练效率上优于更复杂的解码器（如UNet、Transformer）。
  3. **全局响应归一化（GRN）层**：这是解决特征坍缩的核心。GRN被插入到ConvNeXt模块的MLP之后，其计算过程分为三步：
     a) **全局特征聚合**：对每个通道的特征图进行L2范数计算，得到一个全局的通道重要性向量。
     b) **特征归一化**：使用divisive normalization，计算每个通道的L2范数相对于所有通道L2范数之和的比值，从而衡量该通道的相对重要性。
     c) **特征校准**：将归一化后的权重乘回原始特征图，并加上一个残差连接。
     其核心公式为：`Xi = γ * Xi * ( ||Xi|| / ∑j||Xj|| ) + β + Xi`，其中γ和β是可学习的缩放和偏置参数（初始化为0），用于保证训练初期层的功能为恒等映射。
- **训练方式**：在ImageNet-1K上进行800个epoch的FCMAE预训练，然后在下游任务上进行100个epoch的端到端微调。
- **推理流程**：预训练完成后，模型可以转换为标准ConvNeXt架构（稀疏卷积转为密集卷积），用于各种下游任务的推理。
- **与已有方法的差异**：
  - **与标准MAE**：标准MAE使用Transformer，依赖掩码令牌（mask tokens）输入；FCMAE使用稀疏卷积，不引入掩码令牌，避免了训练/测试不一致和效率问题。
  - **与监督ConvNeXt**：ConvNeXt V2通过加入GRN并采用自监督预训练，在相同架构下获得了更好的性能。
  - **与其他归一化/注意力**：GRN不同于LayerNorm（LN）或BatchNorm（BN），它不进行特征中心化或方差归一化，而是通过全局聚合和divisive normalization直接促进通道间的竞争；与SE等通道注意力模块相比，GRN不增加参数量（除了两个标量参数），且其归一化操作基于所有通道的响应。
- **论文类型特化（注意力类）**：GRN作用于通道维度，通过聚合全局空间信息来重新校准每个通道的响应，是一种**通道注意力机制**。它可即插即用到网络中（文中插入在MLP后），其计算开销很小（仅涉及范数计算和除法），但能有效提升特征多样性和模型性能。

## 6. 实验与结果
- **使用的数据集**：主要在ImageNet-1K (IN-1K)上进行预训练和分类评估。下游任务评估在COCO（目标检测）和ADE20K（语义分割）上进行。
- **对比方法**：ConvNeXt V1（监督和自监督版本）、MAE预训练的ViT、其他归一化方法（LRN, BN, LN）、其他通道注意力/重加权方法（SE, CBAM）。
- **评价指标**：ImageNet验证集Top-1准确率，以及检测、分割任务上的标准指标（如AP、mIoU）。
- **主实验结果**：
  - 模型规模上，ConvNeXt V2在从Atto（3.7M参数）到Huge（650M参数）的整个范围内，均比ConvNeXt V1监督模型有显著提升，平均提升约1%（图1）。
  - ConvNeXt V2 Huge模型在使用IN-22K标签预训练后，在ImageNet上达到了**88.9%** 的top-1准确率（摘要）。
  - 仅使用FCMAE预训练的ConvNeXt V1-Base准确率为**83.7%**，略低于其监督基准（300 epochs）的**83.8%**。
  - 加入GRN后（即ConvNeXt V2-Base），FCMAE预训练的微调准确率提升至**84.6%**（表2）。
- **消融实验**（论文中提供了大量消融）：
  - **FCMAE设计**：稀疏卷积对性能至关重要（79.3% vs 83.7%）（第3节）。简单的单个ConvNeXt块解码器在精度和效率上取得最佳平衡（表1）。
  - **GRN设计**：L2范数聚合优于平均池化；divisive normalization效果最好；残差连接必不可少（表2a, b, c）。GRN优于LN、BN等标准归一化方法（表2d），且不增加参数（优于SE、CBAM）（表2e）。GRN必须在预训练和微调阶段都使用才能生效（表2f）。
- **泛化实验**：结果表明，ConvNeXt V2在COCO检测和ADE20K分割任务上也超越了ConvNeXt V1（摘要及引言中提及，具体数据在未提供的文本部分）。
- **效率信息**：论文提供了不同规模的模型参数量（如Atto: 3.7M, Huge: 650M）。GRN层本身计算开销小，不增加模型参数（除γ, β外）。FCMAE预训练因使用稀疏卷积和轻量解码器，效率较高。

## 7. 这篇论文真正有价值的地方
1.  **“协同设计”的理念**：本文最重要的启示是，架构设计与自监督学习框架不应孤立考虑。为了在ConvNets上实现有效的MAE训练，不仅需要修改训练框架（FCMAE），还需要修改架构本身（GRN）。这种系统性的视角对后续研究有很强的指导意义。
2.  **GRN机制的简洁与有效**：GRN实现极其简单（核心三行代码），通过促进通道间竞争来防止特征坍缩，效果显著。这为设计轻量、高效的通道注意力或特征正则化模块提供了新思路。
3.  **将稀疏计算引入视觉预训练**：将3D点云处理中常用的稀疏卷积创造性地应用于2D掩码图像建模，是一种巧妙的工程实践，有效解决了卷积网络处理稀疏输入的难题。
4.  **提供了可直接使用的模型和训练方案**：论文发布了一系列经过验证的预训练模型，为希望在纯卷积架构上应用自监督学习的研究者和工程师提供了即用型工具和明确的改进路线。

## 8. 局限与问题
1.  **自监督优势仍有差距**：即使在ConvNeXt V2上，FCMAE预训练的微调性能（84.6%）与其在最佳监督设置下的性能（83.8%）提升幅度约为0.8%，虽然显著，但与ViT上MAE相比监督基线的大幅提升相比，优势可能仍不够突出，表明纯卷积架构的自监督潜力可能仍未被完全挖掘。
2.  **特征坍缩的根源分析**：论文通过实验观察到了特征坍缩现象并提出了GRN解决方案，但对于坍缩现象产生的根本原因（例如，是否与卷积的归纳偏置、MAE目标函数等有关）的理论分析较少。
3.  **实验场景的局限性**：实验主要在ImageNet、COCO、ADE20K等标准学术数据集上进行，对于更复杂、数据更稀疏或领域特异性更强的场景（如医学影像、遥感）的适用性未在提供文本中得到验证。
4.  **计算成本**：尽管提到了效率，但800个epoch的预训练在ImageNet上仍需要相当大的计算资源。稀疏卷积虽然能减少计算量，但在通用硬件上的实际加速效果可能因实现而异。

## 9. 我该怎么使用这篇论文
- **快速了解**：阅读**摘要**、**引言**、**方法部分的概述（第3、4节开头）** 以及**实验结果表**（如表1、2和图1），可以快速掌握核心思想、方法和主要成果。
- **如果复现**：重点精读**第3节（FCMAE）** 和**第4节（GRN）** 的方法细节，特别是**稀疏卷积的实现**、**FCMAE框架图（Figure 2）**、**GRN的伪代码（Algorithm 1）** 以及**所有消融实验表（Table 1, 2）** 中的具体设计和参数选择。
- **如果借鉴创新点**：
  - 可以学习其“协同设计”思路，思考如何针对自己的特定任务或架构修改自监督预训练目标。
  - **GRN层**本身可以作为一个即插即用的模块，尝试加入到其他存在特征冗余或通道竞争不足的CNN模型中。
  - “用稀疏卷积处理掩码输入”的思想，可以借鉴到其他需要处理不完整或稀疏视觉输入的任务中。
- **如果写Related Work**：这篇论文可以放在**自监督学习（特别是掩码图像建模）**、**卷积神经网络架构现代化**以及**通道注意力/特征归一化技术**这几个类别下进行引用。

## 10. 和其他论文的关系
根据论文内容和提供的主题“B_注意力算子模块”，可以推断出以下关系：
- 本文是 [[ConvNeXt]] 的后续工作，提出了其V2版本。
- 本文是 [[Masked Autoencoders (MAE)]] 在卷积网络上的重要适配和改进工作。
- 本文提出的GRN层与经典的通道注意力模块 [[SENet]] 有相似的设计目标（增强通道表示），但采用了不同的计算机制（全局归一化 vs. 压缩-激励）。
- 本文的GRN层也可以与 [[CBAM]] 等结合空间和通道注意力的模块进行对比。
- 论文中提到了与 [[MAE]] 预训练的 [[Vision Transformer (ViT)]] 的性能对比。

## 11. 关键词
ConvNeXt V2， 全局响应归一化（GRN）， 掩码自编码器（MAE）， 自监督学习， 全卷积掩码自编码器（FCMAE）， 特征坍缩， 稀疏卷积， 通道竞争， 协同设计， 视觉表征学习， 纯卷积网络， 特征多样性

## 12. 可信度说明
本精读笔记主要基于提供的PDF文本的前12页内容生成，涵盖了摘要、引言、相关工作、核心方法（FCMAE和GRN）的详解以及部分实验结果和消融研究。提取的文本质量良好，结构清晰，包含了关键的方法描述、公式、图表引用和实验数据。因此，笔记中关于方法动机、框架设计、GRN机制和主要消融实验结果的内容具有较高的可信度。未能在笔记中呈现的细节（如具体的下游任务实验数据、不同模型规模的完整配置、训练超参数等）主要存在于PDF文本未提供的后3页中，对此已在相应部分标注了信息缺失。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/(GRN)ConvNeXtV2.txt` (12/15 页); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
