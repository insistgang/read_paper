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
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`, `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Dual Residual Attention Network for Image Denoising |
| **作者** | Wencong Wu; Shijie Liu; Yi Zhou; Yungang Zhang; Yu Xiang（云南师范大学信息科学技术学院） |
| **发表时间** | 2023-05（arXiv:2305.04269v1, 7 May 2023） |
| **刊物/会议** | arXiv (eess.IV) |
| **DOI** | 未明确（arXiv 预印本，代码 https://github.com/WenCongWu/DRANet） |

## 摘要

> **英文原文（据 PDF 提取文本清理空格与连字符断裂后整理）**：
>
> In image denoising, deep convolutional neural networks (CNNs) can obtain favorable performance on removing spatially invariant noise. However, many of these networks cannot perform well on removing the real noise (i.e. spatially variant noise) generated during image acquisition or transmission, which severely sets back their application in practical image denoising tasks. Instead of continuously increasing the network depth, many researchers have revealed that expanding the width of networks can also be a useful way to improve model performance. It also has been verified that feature filtering can promote the learning ability of the models. Therefore, in this paper, we propose a novel Dual-branch Residual Attention Network (DRANet) for image denoising, which has both the merits of a wide model architecture and attention-guided feature learning. The proposed DRANet includes two different parallel branches, which can capture complementary features to enhance the learning ability of the model. We designed a new residual attention block (RAB) and a novel hybrid dilated residual attention block (HDRAB) for the upper and the lower branches, respectively. The RAB and HDRAB can capture rich local features through multiple skip connections between different convolutional layers, and the unimportant features are dropped by the residual attention modules. Meanwhile, the long skip connections in each branch, and the global feature fusion between the two parallel branches can capture the global features as well. Moreover, the proposed DRANet uses downsampling operations and dilated convolutions to increase the size of the receptive field, which can enable DRANet to capture more image context information. Extensive experiments demonstrate that compared with other state-of-the-art denoising methods, our DRANet can produce competitive denoising performance both on synthetic and real-world noise removal.
>
> **中文翻译**：
>
> 在图像去噪中，深度卷积神经网络（CNN）在去除空间不变噪声上能取得不错的性能，但许多网络在去除图像采集或传输过程中产生的真实噪声（即空间变化噪声）时表现不佳，这严重制约了它们在实际去噪任务中的应用。与其不断增加网络深度，许多研究者已经表明拓宽网络的宽度同样是提升模型性能的有效途径；同时也有研究验证了特征筛选（feature filtering）能够提升模型的学习能力。为此，本文提出一种新颖的双分支残差注意力网络（Dual-branch Residual Attention Network, DRANet），兼具宽模型架构与注意力引导特征学习两方面优点。DRANet 包含两条不同的并行分支，用以捕获互补特征以增强模型学习能力。我们分别为上、下分支设计了新的残差注意力块（RAB）和新颖的混合扩张残差注意力块（HDRAB）；RAB 与 HDRAB 通过不同卷积层之间的多重跳跃连接捕获丰富的局部特征，并由残差注意力模块丢弃不重要的特征。同时，每条分支内的长跳跃连接以及两条并行分支之间的全局特征融合也能够捕获全局特征。此外，DRANet 借助下采样操作和扩张卷积扩大感受野，从而捕获更多图像上下文信息。大量实验表明，与其他先进去噪方法相比，DRANet 在合成噪声与真实世界噪声去除上均能取得有竞争力的去噪性能。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **这篇论文为什么要做**: 基于深度 CNN 的去噪方法在去除合成的空间不变噪声（如加性高斯白噪声 AWGN）时表现良好，但在去除图像采集/传输过程中产生的**空间变化的真实噪声**时效果不佳，这制约了其实际应用 (p.1, Abstract & Intro)。
- **之前方法有什么问题**:
    1.  传统方法（如 BM3D、WNNM、MCWNNM、TWSC）依赖复杂的优化算法，**推理时间长**，且因超参数多而**去噪性能不稳定**，难以实际部署 (p.1)。
    2.  加深网络虽可能增强学习能力，但会相应**增加参数量与推理时间**，难以部署到存储受限或高实时性要求的场景 (p.2)。许多研究因此转向**加宽网络结构** [8,9,10]。
    3.  现有注意力去噪模型（如 ADNet、RIDNet）性能优异，但作者指出其**特征学习能力仍有提升空间**；跳跃连接 (skip connection) 被验证是增强特征学习的有效工具 (p.2)。
- **作者想解决的核心矛盾**: 如何在**不一味加深网络**的前提下，借助"加宽 + 注意力引导特征筛选"，设计既能捕获丰富局部特征、又能利用全局上下文、参数更少且对真实空间变化噪声有效的盲去噪模型。

## 关键贡献

1.  设计了一个新颖的**双残差注意力网络（DRANet）**用于图像盲去噪，对合成噪声与真实噪声均有效；相比许多 SOTA 盲去噪模型，**架构更简单、网络参数更少** (p.2, 贡献 1)。
2.  分别为模型两条分支提出**残差注意力块（RAB）**与**混合扩张残差注意力块（HDRAB）**，使模型能够捕获互补特征；这两个注意力块还能进行恰当的特征筛选，保证整网能很好地同时提取局部与全局特征 (p.2, 贡献 2)。
3.  通过大量实验证明 DRANet 相较许多其他 SOTA 去噪方法能取得有竞争力的去噪结果 (p.2, 贡献 3)。

## 方法

- **整体框架**: DRANet 是**双子网络并行结构**（Fig. 1, p.4）。上分支由 **5 个 RAB + 1 个卷积层**组成，并使用 **2×2 步长卷积下采样、2×2 转置卷积上采样**来提取多尺度特征并增大感受野；下分支由 **5 个 HDRAB + 1 个卷积层**组成。所有卷积核尺寸统一为 **3×3×128** (p.4)。
- **输入输出**: 去噪问题建模为 `x = y − n`，输入带噪图像 `y`，输出去噪图像 `\hat{x}`。
- **关键模块**:
    1.  **残差注意力块（RAB, Fig. 2, p.5）**:
        - **组成**: 残差块 + **空间注意力模块（SAM）**。
        - **残差块**: 多个标准卷积 (Conv) 与 ReLU，通过卷积层之间的多重逐元素相加跳跃连接提取丰富局部特征。作者强调相比已有残差注意力块 [48,49]，本文 **RAB 拥有更多跳跃连接**，能在不同卷积层间提取并融合特征 (p.5)。
        - **SAM**: 学习卷积特征间的**空间关系**，由 **GMP（全局最大池化）、GAP（全局平均池化）、Conv、ReLU、Sigmoid** 构成。GAP 与 GMP 用于表示整幅图像的统计信息，从而聚焦有用特征、过滤无信息特征；输出注意力图与特征逐元素相乘 (p.5)。
        - **核心作用**: 捕获局部特征 + 用空间注意力做特征筛选。
    2.  **混合扩张残差注意力块（HDRAB, Fig. 3, p.5）**:
        - **组成**: 混合扩张残差块 + **通道注意力模块（CAM）**。
        - **混合扩张残差块**: 多个**扩张率 s 从 1 到 4** 的混合扩张卷积（图中标为 s-DConv，连接顺序为 1-2-3-4-3-2-1）与 ReLU，经多重跳跃连接捕获局部特征。扩张卷积在**不增加网络复杂度**的情况下扩大感受野，混合扩张设计 [38] 用于**消除可能的网格化（gridding）现象**。作者称"据我们所知没有与 HDRAB 类似的块结构" (p.5)。
        - **CAM**: 学习卷积特征间的**通道关系**，由 **GAP、Conv、ReLU、Sigmoid** 构成，输出与特征逐元素相乘 (p.5)。
        - **核心作用**: 扩大感受野捕获更多图像信息 + 用通道注意力做特征筛选。
- **模块之间怎么连接**:
    - 每条分支内部 RAB 之间、HDRAB 之间用**长跳跃连接（Long skip connection）** 相连；长跳跃连接与残差学习既能加速训练收敛，也能提升性能 (p.4)。
    - 两条并行分支最终通过 **Concat（拼接）** 进行全局特征融合，以捕获全局图像特征 (p.4)。
- **数学公式 / 损失函数**:
    - **合成噪声（AWGN）去除**: 用**均方误差 MSE** 优化（公式 1, p.5），衡量预测图 `\hat{x}_j` 与干净图 `x_j` 的差异。
    - **真实噪声去除**: 为避免 MSE 带来的模糊效应（丢失细节与高频纹理），采用 **Charbonnier 损失 L_char（公式 3，常数 ε = 10⁻³）** 作为重建损失，并加上**边缘损失 L_edge（公式 4，基于拉普拉斯算子 △）** 防止高频信息丢失；总损失 `L = L_char + λ_edge · L_edge`，经验设 **λ_edge = 0.1**（公式 2, p.5）。
- **训练方式**: PyTorch + 单张 NVIDIA RTX 3080Ti，Adam 优化器。
    - 合成噪声：共 **6×10⁵ 次迭代**，初始 lr = **1×10⁻⁴**，每 1×10⁵ 次迭代后减半；灰度/彩色模型分别训练约 **65 / 99 小时**。
    - 真实噪声：**120 个 epoch**，初始 lr = **2×10⁻⁴**，按**余弦退火**逐渐降到 1×10⁻⁶；训练约 **190 小时**。
    - 两类模型每个 batch 喂入 **8 个 128×128 图像块**，AWGN 噪声水平随机取自 [0,50]，并用旋转/翻转做数据增强 (p.6)。
- **推理流程**: 标准前向传播，带噪图像经上、下两分支处理并 Concat 融合后输出去噪图像。
- **和已有方法的差异**:
    - 相较单纯加深网络（如 ResNet 系），DRANet 采用**加宽的双分支结构**，以更少深度/参数提升性能。
    - 相较已有残差注意力块 [48,49]，本文 **RAB 拥有更多跳跃连接** (p.5)。
    - 据作者表述，**HDRAB（混合扩张卷积 + 通道注意力）此前无类似块结构** (p.5)；作者团队的 DCANet [24] 被称为首个结合双 CNN 与注意力机制的工作，本文延续并扩展了该思路。

## 实验

- **使用的数据集**（共 7 个公开数据集）:
    - **合成噪声训练**: Flickr2K（2650 张高分辨率彩色图像，裁成 128×128 图块；彩色图块灰度化后用于灰度去噪评测）(p.6)。
    - **合成噪声测试**: Set12, BSD68, CBSD68, Kodak24, McMaster (p.6)。
    - **真实噪声训练**: SIDD Medium（320 对高分辨率带噪/近无噪图像）(p.6)。
    - **真实噪声测试**: SIDD 验证集, DND sRGB 数据集 (p.6)。
- **对比方法**: BM3D, TNRD, DnCNN, IRCNN, FFDNet, BUIFD, BRDNet, DudeNet, ADNet, DSNetB, AINDNet, RIDNet, AirNet 等（p.6，AWGN 评测列表在第 4.4 节，提取文本于此处被截断）。
- **评价指标**: **PSNR** 与 **SSIM** (p.6)。
- **消融实验**（Table 1, p.6；BSD68，AWGN σ=30）:
    - 仅上分支: 27.81 dB / 0.781。
    - 仅下分支: 28.43 dB / 0.807。
    - DRANet 无长跳跃连接: 28.55 dB / 0.808。
    - DRANet 无残差学习: 28.54 dB / 0.807。
    - **完整 DRANet**: **28.56 dB / 0.808**（最佳）。
    - 结论：完整模型 PSNR 比仅上、仅下分支分别高 **0.75 dB / 0.13 dB**；长跳跃连接与残差学习对 PSNR 提升虽小，但能**加速训练与收敛** (p.6)。
- **主实验结果（AWGN / 真实噪声定量对比）**: 提取缓存在第 4.4 节中途截断，**未覆盖**主实验的具体 PSNR/SSIM 对比表。据原文后续页（提取缓存未覆盖，待核）：补读记录显示 p.13-15 含合成/真实噪声的可视化结果（Fig. 5、Fig. 6）与定性结论"DRANet 在真实噪声去除上取得领先的 PSNR/SSIM"，但具体表格数值不在提取文本内。
- **运行时间 / 参数量**: 据原文后续页（提取缓存未覆盖，待核）——补读记录显示 **Table 8 = 三幅合成噪声图像在噪声水平 25 下各模型运行时间（秒）**，**Table 9 = 各模型参数量（单位 K）**，第 4.6 节为"Model complexity analysis"，并称相比 CBDNet、VDN 等 SOTA 盲去噪模型 DRANet 参数更少；具体数值不在提取文本内，待核。

## 局限

- **定量结果不可从提取文本核实**：提取缓存仅覆盖 p.1-12，AWGN/真实噪声主实验对比表、运行时间表（Table 8）、参数量表（Table 9）均在截断之后，本笔记中相关数值标为"待核"。
- **数据集与场景覆盖**：真实噪声实验仅基于 SIDD 与 DND，可能无法完全代表所有真实噪声场景（如低光、极端噪声）。
- **效率论断需更多支撑**：作者强调"参数更少、更适用于实际应用"，相应的运行时间/参数量证据（Table 8/9）不在提取文本内，无法在本笔记内直接核对。
- **模块可解释性**：SAM 与 CAM 的"互补"、双分支为何能捕获互补特征，论文以直觉与图示说明为主，缺少深入的可视化或理论分析（基于提取文本判断）。

## 个人评论

> 以下为 AI 阅读评论，非论文原文结论。

这篇论文的工程价值高于理论新颖性，值得学习之处：
1.  **"加宽而非加深 + 注意力筛选"的取舍**：在去噪社区普遍堆深度的背景下，本文把"双分支加宽 + 长跳跃连接 + 残差学习"与"空间/通道注意力"组合起来，是一个清晰、可复现的轻量化思路样本。消融数据也诚实地显示：长跳跃连接与残差学习对最终 PSNR 提升其实很小（28.55/28.54 vs 28.56），主要收益来自训练加速与收敛，这一点比夸大模块贡献更可信。
2.  **两类注意力分工明确**：上分支 RAB 用**空间注意力（SAM, 含 GAP+GMP）**侧重"哪里重要"，下分支 HDRAB 用**通道注意力（CAM, 仅 GAP）**侧重"哪些通道重要"，再 Concat 融合，是一个把空间/通道注意力拆到不同子网络的干净范例，适合作为"即插即用注意力块"的设计参考。
3.  **真实噪声的损失设计**：用 Charbonnier + 边缘损失替代 MSE 来保高频纹理，是真实噪声去噪里常见但有效的做法，可直接迁移到其他低层视觉任务。

需要保留的怀疑：核心模块（多跳跃连接、混合扩张、双分支）多为已有组件的重组，论文以"据我们所知没有类似结构"主张新颖性；其"参数更少"的核心卖点对应的 Table 9 不在提取文本内，建议复现或引用时回到原文 p.16 核对数值。

### 使用建议

- **如果快速了解**：只读 **Abstract** 与 **Section 1 Introduction**，即可掌握动机、方法与贡献。
- **如果复现**：重点看 **Section 3**（3.1 架构图 Fig.1、3.2 RAB Fig.2、3.3 HDRAB Fig.3、3.4 损失函数）与 **Section 4.2 实验设置**（迭代数、lr 调度、batch、增强）；代码见 https://github.com/WenCongWu/DRANet 。
- **如果借鉴创新点**：
    1.  RAB 如何融合多跳跃连接与空间注意力（SAM）。
    2.  HDRAB 如何把混合扩张卷积（s=1→4）与通道注意力（CAM）结合并消除网格化。
    3.  双分支 + Concat 融合的整体架构与"加宽不加深"的取舍。
- **如果写 related work**：可归入 **图像去噪 / 真实噪声去除**、**注意力机制（空间+通道）**、**残差学习与扩张卷积**、**双流（dual CNN）网络** 几类。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**计算机视觉 / 低层视觉**中的**图像去噪（image denoising）**方向，核心是用**新型网络架构 + 注意力模块**解决深度 CNN 在真实空间变化噪声上性能不佳的问题。它既是一篇**图像复原（去噪）**论文（最贴切的主题为 E_图像复原_超分_去噪_去雨去雾），同时大量笔墨落在 RAB/HDRAB 两个**注意力算子模块**的设计上，因此与 B_注意力算子模块 也强相关。原笔记把 primary_topic 标为 B（注意力算子模块）不算错，但论文的落脚点是"去噪网络"，本次将主主题改为 E、保留 B 为次主题。

## 2. 一句话总结
本文提出双分支残差注意力网络 DRANet，用空间注意力的残差块（RAB，上分支）与通道注意力的混合扩张残差块（HDRAB，下分支）并行提取互补特征再融合，在合成与真实噪声去除上取得有竞争力的性能，且参数更少。

## 3. 背景与问题
- **为什么要做**: 深度 CNN 擅长去除合成空间不变噪声（AWGN），但对采集/传输产生的真实空间变化噪声效果不佳，限制实际应用 (p.1)。
- **之前方法的问题**:
    1.  传统优化类方法（BM3D, WNNM, MCWNNM, TWSC）推理慢、超参多、性能不稳 (p.1)。
    2.  加深网络 → 参数与推理时间上升，难以部署到存储受限/高实时场景 (p.2)。
    3.  已有注意力去噪模型（ADNet, RIDNet）性能虽好但特征学习能力仍可加强；跳跃连接被证明能增强特征学习 (p.2)。
- **核心矛盾**: 在不一味加深的前提下，靠"加宽双分支 + 注意力特征筛选"同时拿到局部与全局特征，处理真实噪声。

## 4. 核心贡献
1.  新颖的双残差注意力网络 DRANet 用于盲去噪，对合成与真实噪声均有效，且架构更简单、参数更少 (p.2)。
2.  分别为上/下分支提出 RAB 与 HDRAB，使模型捕获互补特征并做恰当特征筛选 (p.2)。
3.  大量实验证明 DRANet 相较众多 SOTA 方法有竞争力 (p.2)。

## 5. 方法详解
- **整体框架**: 双子网络并行（Fig.1, p.4）。上分支 = 5×RAB + 1 卷积层，含 2×2 步长卷积下采样 / 2×2 转置卷积上采样以提多尺度特征、扩感受野；下分支 = 5×HDRAB + 1 卷积层。所有卷积核 3×3×128。两分支特征经 Concat 全局融合。
- **输入输出**: 建模 `x = y − n`；输入带噪 `y`，输出去噪 `\hat{x}`。
- **RAB（Fig.2, p.5）**: 残差块（多 Conv+ReLU，多重逐元素相加跳跃连接）+ SAM（GMP+GAP+Conv+ReLU+Sigmoid，学空间关系，注意力图与特征逐元素相乘）。相比 [48,49] 的残差注意力块，RAB **跳跃连接更多**。
- **HDRAB（Fig.3, p.5）**: 混合扩张残差块（扩张率 s=1→4 的 s-DConv + ReLU，多重跳跃连接，扩张卷积不增复杂度地扩感受野，混合扩张消除网格化）+ CAM（GAP+Conv+ReLU+Sigmoid，学通道关系，逐元素相乘）。作者称无类似块结构。
- **连接方式**: 分支内 RAB↔RAB、HDRAB↔HDRAB 用长跳跃连接；两分支末端 Concat 融合。长跳跃连接 + 残差学习既加速训练也提性能。
- **损失函数**: AWGN 用 MSE（式 1）；真实噪声用 Charbonnier L_char（式 3，ε=10⁻³）+ 拉普拉斯边缘损失 L_edge（式 4），总损失 `L = L_char + 0.1·L_edge`（式 2）。
- **训练**: PyTorch + RTX 3080Ti，Adam。合成：6×10⁵ 迭代，lr 1e-4 每 1e5 减半（灰/彩 ~65/99h）；真实：120 epoch，lr 2e-4 余弦退火→1e-6（~190h）；batch=8 个 128×128 块，AWGN∈[0,50]，旋转/翻转增强 (p.6)。
- **与已有方法差异**: 加宽双分支替代加深；RAB 跳跃连接更多；HDRAB 混合扩张+通道注意力为新组合；延续作者团队 DCANet（首个双 CNN+注意力）思路。

## 6. 实验与结果
- **数据集（7 个）**: 合成训练 Flickr2K(2650)；合成测试 Set12/BSD68/CBSD68/Kodak24/McMaster；真实训练 SIDD Medium(320 对)；真实测试 SIDD 验证集 + DND sRGB (p.6)。
- **对比方法**: BM3D, TNRD, DnCNN, IRCNN, FFDNet, BUIFD, BRDNet, DudeNet, ADNet, DSNetB, AINDNet, RIDNet, AirNet 等 (p.6)。
- **指标**: PSNR / SSIM。
- **消融（Table 1, BSD68 σ=30）**: 仅上 27.81/0.781；仅下 28.43/0.807；无长跳跃 28.55/0.808；无残差学习 28.54/0.807；**完整 28.56/0.808**（最佳）。完整比仅上/仅下高 0.75/0.13 dB；长跳跃与残差学习主要贡献是加速训练收敛 (p.6)。
- **主实验定量对比**: 提取缓存在 4.4 节中途截断，未覆盖具体对比表。据原文后续页（提取缓存未覆盖，待核）：p.13-15 有 Fig.5/Fig.6 可视化及"真实噪声去除 DRANet 取得领先 PSNR/SSIM"的定性结论。
- **效率**: 据原文后续页（提取缓存未覆盖，待核）——Table 8 为噪声水平 25 下三幅合成图运行时间（秒），Table 9 为各模型参数量（K），第 4.6 节"Model complexity analysis"称相比 CBDNet/VDN 等参数更少；数值待回原文核对。

## 7. 这篇论文真正有价值的地方
1.  **"加宽不加深 + 注意力筛选"的可复现样本**：双分支 + 长跳跃 + 残差学习 + 空间/通道注意力的组合清晰、易复现。
2.  **空间/通道注意力分到两条子网络**：上分支管"哪里"、下分支管"哪些通道"，再 Concat，是注意力分工的干净范例。
3.  **诚实的消融**：明确指出长跳跃/残差学习对 PSNR 提升很小、主要收益在训练加速，比夸大模块更可信。
4.  **真实噪声损失设计**：Charbonnier + 边缘损失保高频纹理，可迁移到其他低层视觉任务。

## 8. 局限与问题
- 提取缓存仅覆盖 p.1-12，主实验对比表、运行时间（Table 8）、参数量（Table 9）均在截断后，相关数值需回原文核对。
- 真实噪声仅 SIDD/DND，覆盖场景有限（低光、极端噪声未含）。
- "参数更少、更适用实际"的核心卖点对应的效率证据不在提取文本内。
- 核心模块多为已有组件重组，新颖性主张较弱（"据我们所知无类似结构"）。

## 9. 我该怎么使用这篇论文
- **快速了解**: Abstract + Section 1。
- **复现**: Section 3（架构图 + RAB/HDRAB + 损失）+ Section 4.2 训练细节；代码 github.com/WenCongWu/DRANet。
- **借鉴创新点**: RAB 多跳跃+空间注意力；HDRAB 混合扩张+通道注意力；双分支+Concat 与"加宽不加深"取舍。
- **写 related work**: 图像去噪/真实噪声、注意力机制（空间+通道）、残差学习与扩张卷积、双流网络。

## 10. 和其他论文的关系
基于正文引用与方法定位，与以下论文/主题相关（`[[双链]]`为可能关联）：
- **注意力去噪网络**: [[RIDNet]], [[ADNet]], [[RDAN]]（RDAN, ref.48）, [[RNAN]]（ref.49）, [[DeamNet]]（ref.50）。
- **双 CNN / 双分支去噪网络**: [[DualCNN]], [[BRDNet]], [[DudeNet]], [[DCBDNet]], [[DCANet]]（作者团队，首个双 CNN+注意力）。
- **扩张卷积去噪网络**: [[DSNet]], [[IRCNN]]。

## 11. 关键词
图像去噪, 真实噪声去除, 双分支网络 (dual CNN), 残差注意力块 RAB, 混合扩张残差注意力块 HDRAB, 空间注意力 SAM, 通道注意力 CAM, 混合扩张卷积, 长跳跃连接, 残差学习, Charbonnier 损失, 边缘损失, 特征筛选。

## 12. 可信度说明
本精读主要基于提取文本覆盖的 **PDF p.1-12**（摘要、引言、相关工作、方法[架构/RAB/HDRAB/损失]、实验设置、消融实验[Table 1]）。这些部分提供了动机、方法核心设计与实验框架的关键信息，笔记中的方法细节、训练超参、消融数值均可在提取文本直接核对。
**局限性**：提取缓存在第 4.4 节中途截断（原文 35657 字符，只截前 25000），**AWGN/真实噪声主实验定量对比表、运行时间表（Table 8）、参数量表（Table 9）及第 4.6 节复杂度分析的具体数值未被提取文本覆盖**，本笔记中此类内容均标为"据原文后续页，提取缓存未覆盖，待核"，未编造具体数字。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 2086 字符/页; 但提取缓存仅覆盖 12/18 页, 主实验定量表与效率表在截断后); 来源缓存: `.paper-cache/extracts/RAB&HDRAB.txt` (提取 12/18 页; 原 AI 主体 12/18 + 全文补读线索 13-18); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
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
