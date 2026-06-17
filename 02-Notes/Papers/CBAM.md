---
title: "CBAM: Convolutional Block Attention Module"
authors:
  - "Sanghyun Woo"
  - "Jongchan Park"
  - "Joon-Young Lee"
  - "In So Kweon"
year: 2018
venue: ECCV
doi:
pdf: [[CBAM.pdf]]
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
extract_cache: .paper-cache/extracts/CBAM.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# CBAM: Convolutional Block Attention Module

## 基本信息
- **PDF**: [[CBAM.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | CBAM: Convolutional Block Attention Module |
| **作者** | Sanghyun Woo; Jongchan Park; Joon-Young Lee; In So Kweon |
| **单位** | KAIST (Woo, Kweon); Lunit Inc. (Park, 工作于 KAIST 期间完成); Adobe Research (Lee) |
| **发表时间** | 2018 |
| **刊物/会议** | ECCV 2018 |
| **DOI** | 未明确 |

## 摘要

清理后的英文原摘要(据 PDF 提取文本整理, 修复了断词与空格):

> We propose Convolutional Block Attention Module (CBAM), a simple yet effective attention module for feed-forward convolutional neural networks. Given an intermediate feature map, our module sequentially infers attention maps along two separate dimensions, channel and spatial, then the attention maps are multiplied to the input feature map for adaptive feature refinement. Because CBAM is a lightweight and general module, it can be integrated into any CNN architectures seamlessly with negligible overheads and is end-to-end trainable along with base CNNs. We validate our CBAM through extensive experiments on ImageNet-1K, MS COCO detection, and VOC 2007 detection datasets. Our experiments show consistent improvements in classification and detection performances with various models, demonstrating the wide applicability of CBAM. The code and models will be publicly available.

中文翻译:

> 我们提出卷积块注意力模块(CBAM), 一个面向前馈卷积神经网络的简单而有效的注意力模块。给定一张中间特征图, 本模块沿通道与空间两个独立维度依次推断注意力图, 再将注意力图与输入特征图相乘, 实现自适应的特征细化。由于 CBAM 是轻量且通用的模块, 它能以可忽略的开销无缝集成进任何 CNN 架构, 并可与基础 CNN 端到端联合训练。我们在 ImageNet-1K、MS COCO 检测、VOC 2007 检测三个数据集上做了大量实验来验证 CBAM。实验表明, CBAM 在多种模型上的分类与检测性能均有一致提升, 证明了其广泛的适用性。代码与模型将公开。

> **关键词**(据原文): 物体识别(object recognition)、注意力机制(attention mechanism)、门控卷积(gated convolution)。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 提升 CNN 性能的研究主流集中在网络的三个因素——深度(depth)、宽度(width)、基数(cardinality)。本文从架构设计的另一个侧面切入: 注意力(attention)。作者的目标是用注意力机制提升表示能力——聚焦重要特征、抑制无关特征。论文还强调注意力"不仅告诉网络在哪里聚焦, 还提升了感兴趣区域的表示"。
- **之前方法的问题**:
  - Squeeze-and-Excitation (SE, Hu et al.) 只用全局平均池化(global average-pooling)来计算通道注意力; 作者认为这是次优(suboptimal)的, 因为忽略了最大池化所携带的"最显著局部特征"线索。
  - SE 还完全缺失空间注意力(spatial attention), 而空间注意力决定"在哪里"聚焦, 对视觉任务至关重要。
  - Residual Attention Network (Wang et al.) 用编码器-解码器式注意力直接计算 3D 注意力图, 计算与参数开销较大; CBAM 则把通道与空间分开学习, 开销小得多, 可作为即插即用模块。
- **核心矛盾**: 如何设计一个轻量、通用、高效的模块, 同时利用通道与空间两个维度的注意力信息, 比仅用单一维度注意力获得更好的特征细化效果, 且开销可忽略。
- **可解释性论据**: 论文用 grad-CAM 可视化, 观察到 CBAM 增强的网络比基线更准确地聚焦目标物体; 并通过用户研究(user study)定量评估可解释性提升, 论证"更好的性能"与"更好的可解释性"可同时获得。

## 关键贡献

论文自述贡献为三点(Contribution 部分):

1. 提出了一个简单而有效的注意力模块 CBAM, 可广泛应用于提升各种 CNN 的表示能力。它由两个顺序子模块(通道注意力 + 空间注意力)构成。
2. 通过大量消融实验(extensive ablation studies)验证了注意力模块的有效性与各项设计选择(双池化、顺序通道优先组合等)。
3. 在多个基准(ImageNet-1K、MS COCO、VOC 2007)上, 把这个轻量模块插入多种网络后, 性能均大幅提升。

## 方法

- **整体框架**: CBAM 是即插即用模块, 在深度网络的每个卷积块(convolutional block)处对中间特征图自适应细化(Fig. 1)。它顺序地先施加通道注意力、再施加空间注意力。集成示例见 Fig. 3——CBAM 应用在 ResNet 的 ResBlock 中每个卷积块的卷积输出上。
- **输入输出**: 输入是中间特征图 \( F \in \mathbb{R}^{C \times H \times W} \); CBAM 依次推断一维通道注意力图 \( M_c \in \mathbb{R}^{C \times 1 \times 1} \) 和二维空间注意力图 \( M_s \in \mathbb{R}^{1 \times H \times W} \), 输出细化特征图 \( F'' \)。
- **整体注意力过程(Eq.1)**:
    \( F' = M_c(F) \otimes F \) (通道注意力加权)
    \( F'' = M_s(F') \otimes F' \) (空间注意力加权)
    其中 \( \otimes \) 表示逐元素相乘; 相乘时注意力值会广播(复制): 通道注意力沿空间维广播, 空间注意力沿通道维广播。\( F'' \) 为最终细化输出。
- **关键模块**:
    1. **通道注意力模块 (Channel Attention Module)**: 学习"什么(what)"是重要特征。把输入特征图 \( F \) 同时做**平均池化**和**最大池化**压缩空间维, 得到两个空间上下文描述符 \( F_c^{avg} \) 与 \( F_c^{max} \)。二者送入一个**共享网络(shared MLP, 含一个隐藏层)**: 隐藏层激活尺寸压缩为 \( \mathbb{R}^{C/r \times 1 \times 1} \)(r 为缩减比, 消融固定为 16), \( W_0 \) 后接 ReLU。两路输出逐元素求和后经 Sigmoid, 得到 \( M_c \in \mathbb{R}^{C \times 1 \times 1} \)。
    2. **空间注意力模块 (Spatial Attention Module)**: 学习"哪里(where)"是重要区域, 与通道注意力互补。对(经通道细化后的)特征图沿**通道轴**做平均池化与最大池化, 得到两张二维图 \( F_s^{avg}, F_s^{max} \in \mathbb{R}^{1 \times H \times W} \); 拼接(concatenate)后过一个**标准卷积层**生成空间注意力图, 再经 Sigmoid。消融确定卷积核为 **7×7**。
- **数学公式**:
    - 通道注意力(Eq.2): \( M_c(F) = \sigma(MLP(AvgPool(F)) + MLP(MaxPool(F))) = \sigma(W_1(W_0(F_c^{avg})) + W_1(W_0(F_c^{max}))) \), 其中 \( W_0 \in \mathbb{R}^{C/r \times C} \), \( W_1 \in \mathbb{R}^{C \times C/r} \), 两路共享同一组 MLP 权重 \( W_0, W_1 \)。直观上平均池化软性编码全局统计, 最大池化编码最显著部分, 二者互补。
    - 空间注意力(Eq.3): \( M_s(F) = \sigma(f^{7 \times 7}([AvgPool(F); MaxPool(F)])) = \sigma(f^{7 \times 7}([F_s^{avg}; F_s^{max}])) \), 其中 \( f^{7 \times 7} \) 表示滤波器尺寸 7×7 的卷积。
- **模块排布**: 通道与空间两模块可并行或顺序放置; 论文实验得到**顺序优于并行**, 且**通道优先**略好于空间优先(详见消融 Sec. 4.1)。
- **训练方式**: 端到端可训练, 与基础 CNN 无缝集成并联合训练; 参数与计算(GFLOPs)增量在多数情况下可忽略。
- **和已有方法的差异**:
    1. 相比 SE, CBAM 在通道注意力之外增加了空间注意力。
    2. 通道注意力上, CBAM 在 SE 的平均池化之外引入最大池化, 用共享 MLP 融合两路。注意: SE 模块即"仅用平均池化的通道注意力"这一特例。
    3. 相比同期工作 BAM(同样把 3D 注意力分解为通道与空间), CBAM 插在**每个卷积块**, 而 BAM 放在网络的**每个瓶颈(bottleneck)**处。

## 实验

- **使用的数据集**: ImageNet-1K(图像分类, 120 万训练图 / 5 万验证图 / 1000 类)、MS COCO(目标检测)、VOC 2007(目标检测)。所有评测网络都在 PyTorch 中复现以做公平对比。
- **训练协议(消融与分类)**: 基础架构 ResNet-50; 数据增强同 ResNet; 测试用 224×224 单裁剪(single-crop); 学习率从 0.1 起每 30 epoch 衰减; 共训练 90 epoch; 在验证集报告分类错误率。
- **对比方法**: 基线网络(ResNet/WideResNet/ResNeXt 等)与先前注意力方法 SE。
- **评价指标**: 分类用 Top-1 / Top-5 错误率; 检测用 mAP(%)(据原文后续页 Table 7/8, 提取缓存未覆盖, 待核)。
- **主实验结果(ImageNet-1K, Table 4)**:
    - ResNet50: 24.56% → CBAM 22.66% (SE 为 23.14%); Top-5 7.50% → 6.31%。
    - ResNet101: 23.38% → CBAM 21.51% (SE 22.35%); Top-5 6.88% → 5.69%。
    - ResNet18: 29.60% → CBAM 29.27%; ResNet34: 26.69% → CBAM 25.99%。
    - WideResNet18(widen=1.5): 26.85% → CBAM 26.10%; (widen=2.0): 25.63% → CBAM 24.84%。
    - ResNeXt50(32×4d): 22.85% → CBAM 21.92%; ResNeXt101(32×4d): 21.54% → CBAM 21.07%。
    - 多数情形下 CBAM 优于(或持平于)同等配置的 SE, 且参数/GFLOPs 增量极小。
- **消融实验**:
    1. **通道注意力(Table 1)**: ResNet50 基线 24.56%; +AvgPool(即 SE) 23.14%; +MaxPool 23.20%; **+AvgPool & MaxPool(双池化, CBAM 设计) 22.80%**(Top-5 6.52%)。说明最大池化与平均池化同样有意义, 二者并用最优, 且不增加可学习参数。本实验固定缩减比 r=16。
    2. **空间注意力(Table 2, 在通道模块之后接空间模块)**: channel(SE) 23.14%; channel(双池化) 22.80%; +spatial(1×1 conv, k=3) 22.96%; (1×1 conv, k=7) 22.90%; (通道池化 avg&max, k=3) 22.68%; **(通道池化 avg&max, k=7) 22.66%**(Top-5 6.31%)。结论: 显式的通道池化优于用 1×1 卷积学权重的池化; 更大卷积核(7 优于 3)更好, 说明确定空间重要区域需要较大感受野。
    3. **注意力模块组合(Table 3)**: channel(SE) 23.14%; **顺序 channel+spatial 22.66%**(最优); 顺序 spatial+channel 22.78%; 并行 22.95%。结论: 顺序优于并行, 通道优先略好于空间优先; 且所有组合都优于只用通道注意力。
- **泛化实验**: CBAM 在不同深度(ResNet-18/34/50/101)、不同宽度(WideResNet18 widen=1.5/2.0)、不同基数(ResNeXt50/101 32×4d)上均稳定提升, 证明在大规模数据集上对多种架构泛化良好(Table 4)。
- **效率信息(Table 1 / Table 4)**:
    - 通道注意力单模块(Table 1): 参数 25.56M → 25.92M; GFLOPs 3.86 → 4.02(双池化)。
    - 完整 CBAM(Table 4, ResNet50): 参数 25.56M → 28.09M(增 2.53M, 与 SE 同量级); GFLOPs 3.858 → 3.864(增 0.006)。
    - 注: Table 2 中 channel-only 也列为 28.09M/3.860, 与 SE 完全同量级; 加上空间模块后参数几乎不变(28.09~28.10M), GFLOPs 仅微增。
- **检测实验**: MS COCO 与 VOC 2007 上, 把 CBAM 加到现有检测器(包括复现的 SSD、StairNet)均提升 mAP; 特别地, 把模块放在已有单阶段检测器之上, 在 VOC 2007 test 上取得当时 SOTA(据原文后续页 Table 7/8 与 4.5/4.6 节, 提取缓存只覆盖前 12 页, 待核)。

## 局限

- **适用任务范围**: 论文聚焦图像分类与目标检测; 对语义分割、姿态估计、视频理解等其他视觉任务的有效性论文未实验。
- **数据集范围**: 实验全在标准基准(ImageNet/COCO/VOC)上, 未涉及小样本、域自适应、极端不平衡或特定领域(医学/遥感)等分布差异大的场景。
- **检测细节缺失于提取**: COCO/VOC 的具体 mAP 数值在本提取缓存(前 12 页)未覆盖, 只能据后续页线索定性描述, 复现需查原文 Table 7/8。
- **"开销可忽略"的边界**: 模块本身轻量, 但插入网络所有卷积块后总增量是否在所有硬件/部署场景都可忽略, 需按具体平台评估。
- **方法的隐含假设**: 有效性依赖"不同通道与空间位置对任务贡献不等"这一前提; 若特征本身已较均匀, 增益可能有限。
- **可视化与图信息**: 提取缓存不含图(Fig.1/2/3)与 grad-CAM 可视化图, 方法结构理解基于文字与公式。

## 个人评论

1. **将 3D 注意力分解为 1D 通道 + 2D 空间的范式很有价值**: 用两个低维注意力顺序逼近高维注意力, 既省算力又省参数, 是后续大量轻量注意力工作(乃至 transformer 时代之前的 CNN 注意力)的标准做法之一。
2. **"双池化互补"是一个可迁移的设计直觉**: 平均池化编码全局软统计、最大池化编码最显著响应, 用共享 MLP 融合两者, 且不增加可学习参数就把 SE 的 23.14% 推到 22.80% —— 这个"免费午餐"很有说服力。
3. **每步设计都有消融背书**: 论文不是直接给最终方案, 而是分通道/空间/组合三步逐项做对照(Table 1/2/3), 数值差距虽小但方向一致, 结论可信。这种"设计即实验"的写法值得学习。
4. **正交维度的价值得到验证**: 在深度、宽度、基数之外, 注意力被证明是又一个能稳定提升表示能力的设计轴, 且与前三者叠加仍有收益。
5. **可改进之处**: 消融的数值差异(如 22.66 vs 22.68 vs 22.78)较小, 论文未给方差/多次运行结果, 部分"略好"的结论稳健性有待考量; 空间注意力固定 7×7 卷积是否在更大特征图上仍最优也未深究。

### 使用建议

- **如果快速了解**: 读摘要、引言末尾的三点贡献, 以及实验部分的 Table 4(主实验)与三张消融表(Table 1/2/3)的结论。
- **如果复现**: 精读第 3 节方法, 重点是 Eq.1/2/3 与 Fig.2/3 的集成位置; 关注超参数——通道注意力缩减比 r=16、空间卷积核 k=7、通道优先顺序; 训练协议是 90 epoch、lr 0.1 每 30 epoch 衰减、224 单裁剪。
- **如果借鉴创新点**: 学"通道+空间顺序分解"与"平均+最大双池化共享 MLP"两个核心套路, 可直接迁移到自己的网络改进。
- **如果写 Related Work**: 放在"注意力机制 / 特征增强模块", 与 SENet、BAM、Residual Attention Network 并列讨论。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页:
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是计算机视觉中注意力机制方向的代表性工作(ECCV 2018), 属于"面向 CNN 的即插即用特征增强模块"这一类。它解决的核心问题是: 如何在几乎不增加参数与算力的前提下, 用轻量注意力自适应细化 CNN 的中间特征图, 同时提升分类/检测性能与可解释性。该论文归在"B_注意力算子模块"主题下最贴切——它是一个通用算子模块, 而非某个具体任务的方法。它与 SENet(只做通道注意力)、BAM(同期, 放在瓶颈处)构成同一谱系。

## 2. 一句话总结
CBAM 把代价高的 3D 注意力分解为顺序的"1D 通道注意力 + 2D 空间注意力", 并在通道注意力中联合使用平均池化与最大池化(共享 MLP), 以可忽略的开销稳定提升多种 CNN 在 ImageNet/COCO/VOC 上的表现。

## 3. 背景与问题
- **为什么要做**: 提升 CNN 的主流路线是加深度、加宽度、加基数; 本文换一个维度——注意力——来增强表示, 让网络聚焦重要特征、抑制无关信息。论文强调注意力"既告诉网络在哪聚焦, 也提升感兴趣区域的表示"。
- **之前方法的问题**: (1) SE 只用全局平均池化算通道注意力, 作者论证这是次优的, 漏掉了最大池化携带的显著特征线索; (2) SE 完全没有空间注意力, 而空间注意力决定"在哪里"聚焦; (3) Residual Attention Network 直接算 3D 注意力图, 开销大, 难做即插即用。
- **核心矛盾**: 既要同时用上通道与空间两个维度, 又要保持轻量、通用、可端到端训练且开销可忽略。

## 4. 核心贡献
1. 提出 CBAM——简单有效、可广泛提升 CNN 表示能力的注意力模块, 由通道与空间两个顺序子模块组成。
2. 通过大量消融验证了各项设计选择: 双池化(avg+max)、显式通道池化、7×7 大核空间卷积、顺序且通道优先的组合。
3. 在 ImageNet-1K、MS COCO、VOC 2007 上把模块插入多种网络(ResNet/WideResNet/ResNeXt)均显著提升, 证明广泛适用性。

## 5. 方法详解
- **整体框架(Eq.1)**: 给定 \( F \in \mathbb{R}^{C \times H \times W} \), 先 \( F' = M_c(F) \otimes F \), 再 \( F'' = M_s(F') \otimes F' \); \( \otimes \) 为逐元素乘, 注意力沿对应维广播。CBAM 插在每个卷积块的卷积输出处(ResNet 中即 ResBlock 内, 见 Fig.3)。
- **通道注意力(Eq.2)**: \( M_c(F) = \sigma(MLP(AvgPool(F)) + MLP(MaxPool(F))) \)。对 \( F \) 同时做全局平均池化与全局最大池化得 \( F_c^{avg}, F_c^{max} \), 送入共享单隐层 MLP(隐层尺寸 \( C/r \), r 为缩减比, 取 16; \( W_0 \) 后接 ReLU), 两路求和过 Sigmoid, 得 \( M_c \in \mathbb{R}^{C \times 1 \times 1} \)。关键: 两路共享 \( W_0, W_1 \), 因此不增加可学习参数。
- **空间注意力(Eq.3)**: \( M_s(F) = \sigma(f^{7 \times 7}([AvgPool(F); MaxPool(F)])) \)。沿通道轴做平均与最大池化得两张 \( 1 \times H \times W \) 图, 拼接后过 7×7 卷积再 Sigmoid, 得 \( M_s \in \mathbb{R}^{1 \times H \times W} \)。
- **排布**: 顺序优于并行, 通道优先略优于空间优先(消融定的)。
- **直觉**: 平均池化软编码全局统计, 最大池化编码最显著局部响应, 互补; 沿通道池化能突出信息区域; 大核给空间注意力更大感受野来决定"哪里重要"。
- **训练**: 端到端, 与基础 CNN 联合训练, 开销可忽略。
- **与 SE/BAM 差异**: SE = 仅平均池化的通道注意力(CBAM 的一个特例); BAM 同期、分解思路类似但放在每个瓶颈处, CBAM 放在每个卷积块。

## 6. 实验与结果
- **数据集**: ImageNet-1K(分类, 1.2M/50K, 1000 类)、MS COCO、VOC 2007(检测)。全部在 PyTorch 复现对比。训练: ResNet-50 基座, 90 epoch, lr 0.1 每 30 epoch 衰减, 224 单裁剪。
- **指标**: 分类 Top-1/Top-5 错误率; 检测 mAP(%)(检测数值在提取缓存前 12 页外, 待核)。
- **通道注意力消融(Table 1)**: 基线 24.56 → +AvgPool(SE) 23.14 → +MaxPool 23.20 → **+双池化 22.80**(Top-5 6.52)。双池化不加参数即超过 SE。
- **空间注意力消融(Table 2)**: channel 22.80 →(1×1 conv,k=3) 22.96 →(1×1,k=7) 22.90 →(通道池化,k=3) 22.68 → **(通道池化,k=7) 22.66**(Top-5 6.31)。显式通道池化 + 7×7 大核最优。
- **组合消融(Table 3)**: SE 23.14; **顺序 channel→spatial 22.66**(最优); spatial→channel 22.78; 并行 22.95。顺序优于并行, 通道优先略好。
- **主实验/泛化(Table 4)**: ResNet50 24.56→22.66; ResNet101 23.38→21.51; ResNet18 29.60→29.27; ResNet34 26.69→25.99; WideResNet18(×1.5) 26.85→26.10, (×2.0) 25.63→24.84; ResNeXt50 22.85→21.92; ResNeXt101 21.54→21.07。多数优于同配置 SE。
- **效率**: ResNet50 上完整 CBAM 参数 25.56M→28.09M、GFLOPs 3.858→3.864, 与 SE 同量级。
- **检测(据后续页线索, 提取缓存未覆盖, 待核)**: COCO/VOC 上把 CBAM 加到检测器(含复现的 SSD、StairNet)均提升 mAP; 置于单阶段检测器之上在 VOC2007 test 取得当时 SOTA。

## 7. 这篇论文真正有价值的地方
1. **3D→(1D 通道 + 2D 空间)的分解范式**: 用两个低维注意力顺序近似高维注意力, 省算力省参数, 成为后续 CNN 注意力模块的通用模板。
2. **双池化互补且零额外参数**: 平均(全局统计)+ 最大(显著响应)共享 MLP 融合, 仅靠改进特征聚合就把 SE 推进一步。
3. **设计即实验**: 通道/空间/组合三步逐项消融, 每个超参选择(r=16、k=7、通道优先)都有数据支撑。
4. **正交维度**: 在深度/宽度/基数之外验证注意力是又一有效设计轴, 且与三者叠加仍有收益; 同时用 grad-CAM + 用户研究论证可解释性也一并提升。

## 8. 局限与问题
- 只在分类与检测上验证, 未涉及分割/姿态/视频等其他任务。
- 全部用标准基准, 未触及小样本/域自适应/不平衡/特定领域(医学、遥感)数据。
- 消融数值差异小(如 22.66 vs 22.68 vs 22.78)但未报告方差或多次运行, 部分"略好"结论的稳健性可商榷。
- 检测 mAP 具体数值在本提取缓存外(前 12 页), 复现需查原文 Table 7/8。
- "开销可忽略"在不同硬件/部署下需具体评估; 方法有效性依赖"通道与空间位置贡献不等"的隐含假设。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言三点贡献 + Table 1/2/3/4。
- **复现**: 精读第 3 节与 Eq.1/2/3、Fig.2/3; 记牢 r=16、k=7、通道优先、90 epoch/lr 0.1 衰减/224 单裁剪。
- **借鉴**: 套用"通道+空间顺序分解"与"avg+max 双池化共享 MLP"。
- **写 Related Work**: 与 SENet、BAM、Residual Attention Network 并列于"注意力机制 / 特征增强模块"。

## 10. 和其他论文的关系
- **[[SENet]]**: CBAM 是对 SE 的扩展——继承通道注意力, 增加最大池化(双池化)与空间注意力模块; SE 即 CBAM 通道分支只用平均池化的特例。
- **[[BAM]]**: 同期工作, 同样把 3D 注意力分解为通道+空间; 区别在放置位置(BAM 在每个瓶颈, CBAM 在每个卷积块)。
- **[[Residual Attention Network]]**: 用编码器-解码器直接算 3D 注意力, 开销大; CBAM 的分解设计正是为降低此类开销。

## 11. 关键词
注意力机制, 通道注意力, 空间注意力, 双池化(平均+最大), 共享 MLP, 卷积神经网络, 特征细化, Squeeze-and-Excitation, BAM, 即插即用模块, ImageNet, 目标检测, grad-CAM

## 12. 可信度说明
本精读主要基于 PDF 提取文本的前 12 页(共 17 页)。这 12 页完整覆盖了摘要、引言、相关工作、方法(CBAM 全部公式与模块描述)以及实验中的全部消融研究(Table 1/2/3)与 ImageNet 主实验/泛化(Table 4)。提取文本质量好(约 2086 字符/页), 文字连续可读, 表格数值清晰, 因此分类与 ImageNet 部分的数值均可直接核对。需注意: (1) 检测部分(4.5 COCO / 4.6 VOC, Table 7/8 的 mAP 数值)位于第 13 页及以后, 不在本提取缓存内, 笔记中相关数值已标注"据原文后续页, 待核"; (2) 提取不含图(Fig.1/2/3)与 grad-CAM 可视化, 模块结构理解基于文字与公式。总体而言, 论文核心思想、方法与分类实验已被准确把握。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页), 前 12/17 页, 文字连续, 表格数值可核); 来源缓存: `.paper-cache/extracts/CBAM.txt` (覆盖 1-12 页; 检测 Table 7/8 在 13+ 页, 未覆盖, 待核); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Convolutional Block Attention Module 13
- p.13: 4.5 MS COCO Object Detection
- p.13: 4.6 VOC 2007 Object Detection
- p.13: For the experiment, we reproduce SSD and StairNet in our PyTorch platform
- p.14: 14 Woo, Park, Lee, Kweon
- p.14: CBAM favorably improves all the strong baselines with negligible additional
- p.14: 5 Conclusion
- p.14: We have presented the convolutional block attention module (CBAM), a new
- p.14: For the channel attention, we suggest to use the max-pooled features along with
- p.14: experiments with various state-of-the-art models and conﬁrmed that CBAM
- p.14: Acknowledgement
- p.15: Convolutional Block Attention Module 15

### 缺失页关键摘录

- p.13: The results are shown in the Table 6. We can clearly see that CBAM outperforms
- p.13: We conduct object detection on the Microsoft COCO dataset [ 3]. This dataset
- p.13: for evaluation. According to [ 39,40], we trained our model using all the training
- p.13: power, given by our module CBAM. As shown in the Table 7, we observe signiﬁ-
- p.13: For the experiment, we reproduce SSD and StairNet in our PyTorch platform
- p.13: The experimental results are summarized in Table 8. We can clearly see
- p.13: that CBAM improves the accuracy of all strong baselines with two backbone
- p.13: networks. Note that accuracy improvement of CBAM comes with a negligible
- p.13: increment but because of our eﬀective feature reﬁnement. In addition, the result
- p.14: Table 7: Object detection mAP(%) on the MS COCO validation set . We
- p.14: Table 8: Object detection mAP(%) on the VOC 2007 test set . We adopt
- p.14: outperforms all the baselines on three diﬀerent benchmark datasets: ImageNet-
<!-- AI_READING_NOTE_END -->
