---
title: "Concurrent Spatial and Channel 'Squeeze & Excitation' in Fully Convolutional Networks"
authors:
  - "Abhijit Guha Roy"
  - "Nassir Navab"
  - "Christian Wachinger"
year: 2018
venue: "arXiv (MICCAI 2018)"
doi: 
pdf: [[scSE.pdf]]
primary_topic: B_注意力算子模块
topics:
  - "B_注意力算子模块"
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/scSE.txt
---

# Concurrent Spatial and Channel 'Squeeze & Excitation' in Fully Convolutional Networks

## 基本信息
- **PDF**: [[scSE.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Concurrent Spatial and Channel 'Squeeze & Excitation' in Fully Convolutional Networks |
| **作者** | Abhijit Guha Roy; Nassir Navab; Christian Wachinger (LMU München / TU München / Johns Hopkins) |
| **发表时间** | 2018 (arXiv:1803.02579v2, 8 Jun 2018; 后发表于 MICCAI 2018) |
| **刊物/会议** | arXiv / MICCAI |
| **DOI** | 未明确 |

## 摘要

清理后的英文原摘要（修复了 PDF 提取的断字与缺空格）：

> Fully convolutional neural networks (F-CNNs) have set the state-of-the-art in image segmentation for a plethora of applications. Architectural innovations within F-CNNs have mainly focused on improving spatial encoding or network connectivity to aid gradient flow. In this paper, we explore an alternate direction of recalibrating the feature maps adaptively, to boost meaningful features, while suppressing weak ones. We draw inspiration from the recently proposed squeeze & excitation (SE) module for channel recalibration of feature maps for image classification. Towards this end, we introduce three variants of SE modules for image segmentation: (i) squeezing spatially and exciting channel-wise (cSE), (ii) squeezing channel-wise and exciting spatially (sSE), and (iii) concurrent spatial and channel squeeze & excitation (scSE). We effectively incorporate these SE modules within three different state-of-the-art F-CNNs (DenseNet, SD-Net, U-Net) and observe consistent improvement of performance across all architectures, while minimally affecting model complexity. Evaluations are performed on two challenging applications: whole brain segmentation on MRI scans and organ segmentation on whole body contrast-enhanced CT scans.

中文翻译：

> 全卷积神经网络（F-CNNs）在众多应用中刷新了图像分割的最高水平。F-CNN 内部的架构创新主要集中在改进空间编码或网络连通性以辅助梯度流。本文探索另一个方向——自适应地重标定特征图，以增强有意义的特征、抑制弱特征。我们从近期提出的、用于图像分类中通道重标定的挤压-激励（SE）模块中获得启发，为图像分割引入三种 SE 模块变体：(i) 空间挤压、通道激励（cSE），(ii) 通道挤压、空间激励（sSE），(iii) 空间与通道并发挤压激励（scSE）。我们将这些 SE 模块有效地嵌入三种不同的先进 F-CNN（DenseNet、SD-Net、U-Net），观察到在所有架构上性能都获得一致提升，同时对模型复杂度影响极小。评估在两个具有挑战性的应用上进行：MRI 扫描的全脑分割与全身对比增强 CT 扫描的器官分割。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：F-CNN 是医学图像分割与计算机视觉分割的主流工具，其基本构件是卷积层——它在所有输入通道上学习滤波器、联合编码空间与通道信息。大量工作改进的是这种"空间+通道的联合编码"，而**独立地对空间模式和通道模式建模**则探索不足。近期 SE 块（Hu et al., CVPR 2018）通过显式建模通道间依赖关系来部分解决这一问题，并凭此在 ILSVRC 2017 ImageNet 分类竞赛夺冠，证明了其有效性。
- **之前方法的问题**：原始 SE 块（本文称 cSE）通过全局平均池化沿空间维度"挤压"、沿通道"激励"，仅做通道重标定，是为**分类**设计的。作者假设：对于图像分割这种需要逐像素预测的任务，**逐像素的空间信息更具信息量**，仅做通道激励并不充分。
- **核心矛盾**：如何把在分类上表现优异的 SE 思想迁移到 F-CNN 分割中，并让重标定**同时利用空间与通道两个维度**，以更好服务于像素级预测。
## 关键贡献

1.  **提出空间挤压与激励（sSE）模块**：沿通道挤压、沿空间激励。作者称这是**首次为神经网络提出"空间挤压激励"**。
2.  **首次将 SE 块集成进 F-CNN 用于分割**：把 SE 思想引入图像分割领域，并验证其作为通用网络组件的有效性（作者称这也是 SE 在 F-CNN 中的首次集成）。
3.  **提出并发空间与通道 SE 块（scSE）**：将 cSE 与 sSE 的输出做**元素级加法**实现并发重标定，鼓励特征图在空间和通道上都更具信息量。
4.  **在多种先进网络和多个任务上验证有效性**：将 cSE/sSE/scSE 集成到 U-Net、SD-Net 和全卷积 DenseNet 三种编码器-解码器架构中，在脑部 MRI 分割（27 结构）与全身 ceCT 器官分割（10 脏器）两个医学应用上评估。
5.  **发现空间激励对分割更重要**：sSE 带来的提升通常高于 cSE，支持"空间激励对分割更重要"的假设。
6.  **以极低代价实现性能提升**：以 U-Net 为例，scSE 仅增加约 3.3×10⁴ 参数、整体约 +1.5%，却带来统计显著（Wilcoxon 符号秩检验，p≤0.001）的提升（脑分割 +4~8% Dice，全身 +2~3% Dice）。
## 方法

- **整体框架与输入输出**：输入特征图 `X ∈ R^{H×W×C0}` 经编码器/解码器块 `Ftr: X→U` 得到 `U ∈ R^{H×W×C}`。SE 块 `FSE(·)` 作用于 `U`，将其重标定为 `^U`，再送入后续的池化/上采样层。SE 块可无缝插入任意 F-CNN，**置于每个编码器和解码器块之后**（p.3, Fig. 1(a)）。
- **关键模块详解**：
    1.  **空间挤压与通道激励（cSE）模块**（沿用 Hu et al. 的原始 SE）：
        - **输入**：特征图 `U`，视为通道集合 `[u1,…,uC]`，`u_i ∈ R^{H×W}`。
        - **机制**：先用**全局平均池化**做空间挤压，得通道描述向量 `z ∈ R^{1×1×C}`，其第 k 元 `z_k = (1/(H·W)) Σ_i Σ_j u_k(i,j)`（公式(1)）。再经两层全连接 `^z = W1(δ(W2 z))`，其中 `W2 ∈ R^{(C/2)×C}`、`W1 ∈ R^{C×(C/2)}`、`δ` 为 ReLU（先降维到 C/2 再升回 C）；经 **sigmoid σ(·)** 把激活压到 [0,1]，逐通道乘回 `U`：`^U^{cSE} = [σ(^z_1)u_1,…,σ(^z_C)u_C]`（公式(2)，Fig. 1(b)）。
        - **作用**：自适应增强信息量大的通道、抑制次要通道。
    2.  **通道挤压与空间激励（sSE）模块**：
        - **输入**：特征图 `U`，按空间位置切片 `[u_{1,1},…,u_{i,j},…,u_{H,W}]`，`u_{i,j} ∈ R^{1×1×C}`。
        - **机制**：用一个 **1×1 卷积** `q = W_sq * U`，`W_sq ∈ R^{1×1×C×1}`，沿通道挤压得投影张量 `q ∈ R^{H×W}`，每个 `q_{i,j}` 是该空间位置上所有 C 个通道的线性组合表示。经 **sigmoid** 得空间权重，逐位置乘回 `U` 全部通道：`^U^{sSE} = [σ(q_{1,1})u_{1,1},…,σ(q_{H,W})u_{H,W}]`（公式(3)，Fig. 1(c)）。
        - **作用**：自适应增强相关空间区域、忽略无关区域。
    3.  **并发空间与通道 SE（scSE）模块**：
        - **机制**：同时计算 cSE 与 sSE，再做**元素级加法** `^U^{scSE} = ^U^{cSE} + ^U^{sSE}`（Fig. 1(d)）。某个位置 (i,j,c) 只有在通道与空间重标定上**都获得高重要性**时才被显著激活。
        - **作用**：在空间和通道两个维度上同时重标定，鼓励学到空间与通道双重相关的特征图。
- **模型复杂度（Model Complexity）**：对输出 C 通道的编/解码块，cSE 引入 `C²/2` 个新权重（两层 FC：C×C/2 与 C/2×C），sSE 引入 `C` 个新权重。含 h 个编/解码块的 F-CNN 复杂度增量为 `Σ_{i=1}^h (C_i²/2 + C_i)`。具体例：本文 U-Net 约 2.1×10⁶ 参数，scSE 块新增约 3.3×10⁴ 参数，约 **+1.5%**。
- **训练方式（Model Learning，p.5）**：三种 F-CNN 均为 **4 个编码块 + 1 个瓶颈层 + 4 个解码块 + 末端分类层**；逻辑（logistic）损失用**中值频率平衡（median frequency balancing）** 加权以补偿类别不平衡（SD-Net 本身联合优化 logistic 与 Dice 损失）；学习率初始 0.01，每 10 个 epoch 降一个数量级；动量 0.95，权重衰减 10⁻⁴，mini-batch=4，用 SGD 优化，训练至验证损失收敛；实验在单张 NVIDIA Titan Xp（12GB）上进行。
- **推理流程**：与标准前向传播相同，仅在每个编/解码块后多出 SE 块的计算。
- **与已有方法的差异**：原始 SE（cSE）只做通道重标定、为分类设计；本文 sSE 专做空间重标定、更契合分割；scSE 把二者并发相加，是本文核心创新。
- **论文类型特化（注意力类）**：
    - **注意力作用维度**：cSE 作用于**通道**，sSE 作用于**空间**，scSE **同时作用于通道与空间**。
    - **可插入性**：即插即用，可无缝插入任意编码器-解码器 F-CNN，位于每块之后。
    - **计算量 vs 效果**：参数量增加极小（U-Net 约 +1.5%），但带来显著且一致的性能提升（脑 +4~8% Dice、全身 +2~3% Dice）。
## 实验

- **数据集**：
    1.  **MALC 数据集**（来自 OASIS）：MRI T1 全脑分割，27 个皮层与皮层下结构；按挑战赛设置训练 15 例、测试 15 例。挑战：训练数据有限、目标结构间类别严重不平衡。人工标注由 Neuromorphometrics, Inc. 提供。
    2.  **Visceral 数据集**：全身对比增强 CT（ceCT）的 10 个脏器分割；训练用 silver corpus 65 例（多算法融合自动标注，标签含噪），测试用 gold corpus 20 例（人工标注）。挑战：脏器形状高度多变、且要在含噪标签上训练后仍能泛化。
- **对比方法**：三种基础网络的原始（vanilla）版本：U-Net、SD-Net、全卷积 DenseNet。
- **评价指标**：平均 Dice 分数（全局 Dice）。显著性用 Wilcoxon 符号秩检验。
- **主实验结果**（p.5-6, Table 1，均值±标准差）：
    - **脑部分割 (MALC)**：
        - DenseNet: 0.842±0.058 → +cSE 0.865 → +sSE 0.876 → +scSE 0.882±0.063（+4.0%）
        - SD-Net: 0.771±0.150 → +cSE 0.790 → +sSE 0.860 → +scSE 0.862±0.082（+9.1%）
        - U-Net: 0.763±0.110 → +cSE 0.825 → +sSE 0.837 → +scSE 0.843±0.062（+8.0%）
    - **全身分割 (Visceral)**：
        - DenseNet: 0.892±0.068 → +cSE 0.903 → +sSE 0.912 → +scSE 0.918±0.051（+2.6%）
        - SD-Net: 0.871±0.064 → +cSE 0.892 → +sSE 0.901 → +scSE 0.907±0.057（+3.6%）
        - U-Net: 0.857±0.106 → +cSE 0.865 → +sSE 0.872 → +scSE 0.881±0.082（+2.4%）
    - **关键发现**：任意 SE 块都带来统计显著（p≤0.001）的 Dice 提升；空间激励（sSE）提升普遍高于通道激励（cSE），验证"空间激励对分割更重要"的假设；scSE 整体最优（脑 +4~8%、全身 +2~3%）；跨架构看 **DenseNet 表现最佳**。
- **消融实验**：Table 1 本身即消融，逐列对比 No SE / +cSE / +sSE / +scSE 四种配置。
- **结构级分析**：Fig. 2（MALC 左半脑结构）与 Fig. 3（Visceral 各脏器）显示，sSE 与 scSE 在几乎所有结构上一致优于基线；cSE 在多数结构上优于基线，但在第三/四脑室、杏仁核、腹侧 DC（ventral DC）等**小而难的结构上性能下降**，作者推测这些结构太小、仅激励通道易被忽略；sSE 与 scSE 性能非常接近。
- **定性结果**（Fig. 4）：脑 MRI 中 DenseNet 对左壳核（left putamen）欠分割，加 scSE 后改善；全身 ceCT 中脾脏（spleen）被过分割，加 scSE 后得到纠正。
- **效率信息**：以 U-Net 为例，scSE 增加约 3.3×10⁴ 参数、整体约 +1.5%。文中**未提供 FLOPs 或推理速度**的具体数据，但强调复杂度增加"可忽略不计"。
## 局限

1.  **应用场景有限**：实验仅在两个**医学图像分割**任务上进行，未在自然图像分割或分类上验证。虽声称 SE 块为通用组件，泛化性仍待更多证明。
2.  **对网络架构的依赖**：提升幅度随基础网络容量/结构而异（如脑分割上 SD-Net 与 U-Net 提升远大于 DenseNet），对更简单或更复杂的网络效果可能不同。
3.  **对小结构的效果不确定**：cSE 对某些极小解剖结构（三/四脑室、杏仁核、ventral DC）无效甚至有害，提示通道注意力可能更适用于中大尺度目标。
4.  **实验细节有缺口**：给出了主要训练超参与 Table 1 的标准差，但未提供超参搜索过程、多次运行的方差，也未提供推理时间/FLOPs 等详细效率对比。
5.  **scSE 的组合方式简单**：scSE 仅把 cSE 与 sSE 输出相加，未探讨是否存在更优融合（如加权相加、串联、门控等）。
## 个人评论

1.  **设计思想简单而有效**：把"挤压（聚合全局信息）—激励（自适应重加权）"范式从通道一维扩展到空间维度，框架清晰、易于理解，启发性强。
2.  **通用性与即插即用**：SE 模块是独立、轻量的"构建块"，可加到任意编码器-解码器网络的每个块之后，无需改动原架构，工程实用性高。
3.  **以极小代价换显著收益**：参数与计算量近乎可忽略（U-Net +1.5%），却在多数据集、多架构上获得一致且统计显著的提升，性价比突出。
4.  **引导后续注意力研究**：本文与其前身 SE-Net 是通道/空间注意力在深度学习中早期且重要的工作，启发了 CBAM 等更复杂的注意力模块；scSE 至今仍是分割网络常用的轻量注意力组件。
5.  **清晰的实验范式**：在三种基础网络、两个任务上充分验证，含主表消融 + 结构级箱线图 + 定性可视化，是评估一个新模块通用性/有效性的良好范例。

### 使用建议

- **快速了解**：读摘要、Fig. 1、Table 1 与结论即可掌握核心思想、方法框架和主要结果。
- **复现**：重点读方法（2.1–2.3 与 Fig. 1）和实验中的 Model Learning 子节（4+1+4 块结构、median frequency balancing、LR 0.01/每 10 epoch 降一阶、动量 0.95、weight decay 1e-4、batch 4、SGD）。
- **借鉴创新点**：
    - 学习 SE 的"挤压—激励"轻量特征校准范式；
    - 借鉴 scSE 的并行结构（通道、空间两分支元素级相加）；
    - 借鉴其实验验证思路（多骨干 + 多任务评估通用性）。
- **写 Related Work**：可归入注意力机制 / 特征重标定 / 医学图像分割网络改进，定位为 SE-Net 在分割领域的直接拓展。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉与深度学习领域的**注意力算子模块**研究，核心方向是**改进全卷积神经网络（F-CNNs）在医学图像分割中的性能**。论文把分类领域的挤压-激励（SE）思想迁移到分割，并扩展出空间维度的重标定，提出 cSE/sSE/scSE 三个即插即用模块。归类于"B_注意力算子模块"主题，特别是**通道与空间注意力结合、用于图像分割**的轻量模块一类。

## 2. 一句话总结
本文为图像分割提出三种挤压-激励变体（cSE 通道、sSE 空间、scSE 并发），通过同时重标定特征图的空间与通道维度，以约 +1.5% 的参数代价在脑/全身两个医学分割任务、三种骨干网上获得一致且统计显著的 Dice 提升。

## 3. 背景与问题
- **为什么要做**：卷积层联合编码空间与通道信息，但"独立地对空间和通道建模"探索不足。SE 块（Hu et al.）显式建模通道依赖、夺得 ILSVRC 2017 分类冠军，但它只做通道激励、为分类设计。
- **之前方法的问题**：原始 SE（cSE）沿空间挤压、沿通道激励，对像素级分割而言，**空间信息可能比通道信息更重要**，仅通道激励不够。
- **核心矛盾**：如何把 SE 迁移到 F-CNN 分割，并让重标定**同时高效利用空间与通道**，服务于精细的逐像素预测。

## 4. 核心贡献
1.  **sSE 模块**：沿通道挤压、沿空间激励——作者称首次为神经网络提出空间挤压激励。
2.  **首次把 SE 集成进 F-CNN 用于分割**，验证其作为通用网络组件。
3.  **scSE 模块**：cSE 与 sSE 输出元素级相加，实现并发空间+通道重标定。
4.  **多骨干多任务验证**：U-Net / SD-Net / FC-DenseNet × 脑 MRI（27 结构）/ 全身 ceCT（10 脏器）。
5.  **发现 sSE > cSE**：空间激励提升通常高于通道激励，支持空间信息对分割更关键的假设。
6.  **极低代价**：U-Net 上 scSE 仅 +3.3×10⁴ 参数（约 +1.5%），却带来统计显著（p≤0.001）提升。

## 5. 方法详解
- **整体框架**：`X ∈ R^{H×W×C0} --Ftr--> U ∈ R^{H×W×C}`，SE 块 `FSE` 把 `U` 重标定为 `^U`，再进后续池化/上采样；置于每个编/解码块之后（Fig. 1(a)）。
- **cSE（公式 1-2，Fig. 1(b)）**：`z_k = (1/HW) Σ_{i,j} u_k(i,j)`（GAP 空间挤压）→ `^z = W1(δ(W2 z))`，`W2∈R^{(C/2)×C}`、`W1∈R^{C×(C/2)}`、δ=ReLU（降维到 C/2 再升回 C）→ `σ(^z)` 逐通道缩放 `U`。直观：先全局描述每个通道，再学通道重要性。
- **sSE（公式 3，Fig. 1(c)）**：`q = W_sq * U`，`W_sq∈R^{1×1×C×1}`（1×1 卷积沿通道挤压）→ `q∈R^{H×W}` → `σ(q)` 逐空间位置缩放 `U` 全部通道。直观：用一卷积学每个空间位置的重要性。
- **scSE（Fig. 1(d)）**：`^U^{scSE} = ^U^{cSE} + ^U^{sSE}`（元素级加法）。位置 (i,j,c) 需在通道与空间上都重要才被显著激活。
- **复杂度**：cSE 加 `C²/2` 权重、sSE 加 `C` 权重；h 块总增量 `Σ(C_i²/2 + C_i)`。U-Net 约 2.1×10⁶ 参数，scSE 加约 3.3×10⁴（+1.5%）。
- **训练（p.5）**：4 编码块 + 1 瓶颈 + 4 解码块 + 分类层；logistic 损失 × median frequency balancing 抗类别不平衡（SD-Net 联合 logistic+Dice）；LR 0.01、每 10 epoch 降一阶；动量 0.95、weight decay 1e-4、batch 4、SGD；训练至验证损失收敛；单卡 Titan Xp(12GB)。
- **与已有方法差异**：cSE=原始 SE（仅通道，分类用）；sSE=本文（仅空间，更契合分割）；scSE=二者并发相加（核心创新）。
- **注意力类特化**：cSE→通道、sSE→空间、scSE→两者并发；即插即用置于每块后；参数增量极小但增益显著一致。

## 6. 实验与结果
- **数据集**：MALC（OASIS，MRI T1 全脑 27 结构，15 训/15 测；标注 by Neuromorphometrics）；Visceral（全身 ceCT 10 脏器，silver 65 训-含噪 / gold 20 测）。
- **对比**：U-Net、SD-Net、FC-DenseNet 的 vanilla 版。
- **指标**：平均（全局）Dice；显著性 Wilcoxon 符号秩检验。
- **主结果（Table 1，均值±标准差）**：
    - **MALC（脑）**：DenseNet 0.842 → scSE 0.882；SD-Net 0.771 → scSE 0.862；U-Net 0.763 → scSE 0.843。
    - **Visceral（全身）**：DenseNet 0.892 → scSE 0.918；SD-Net 0.871 → scSE 0.907；U-Net 0.857 → scSE 0.881。
    - 逐列均为 No SE < +cSE < +sSE ≤ +scSE。
- **关键发现**：任意 SE 块均带来 p≤0.001 的显著提升；sSE > cSE（空间激励更重要）；scSE 最优（脑 +4~8% Dice、全身 +2~3% Dice）；跨架构 DenseNet 最佳。
- **结构级（Fig. 2/3）**：sSE/scSE 几乎对所有结构都优于基线；cSE 在第三/四脑室、杏仁核、ventral DC 等小结构上下降（推测因结构太小、仅通道激励易忽略）；sSE 与 scSE 很接近。
- **定性（Fig. 4）**：左壳核欠分割经 scSE 改善；脾脏过分割经 scSE 纠正。
- **效率**：scSE +1.5% 参数；文中未给 FLOPs/速度。

## 7. 这篇论文真正有价值的地方
1.  **简单而有效**：把"挤压-激励"范式优雅地扩展到空间维度，框架清晰、可解释性好。
2.  **即插即用**：轻量独立构件，可加进任意编码器-解码器网络的每个块后，零侵入。
3.  **极小代价大收益**：约 +1.5% 参数换多数据集/多架构一致且显著的提升，性价比高。
4.  **承上启下**：是 SE-Net 之后通道+空间注意力的早期重要工作，启发 CBAM 等；scSE 至今仍是分割中常用的轻量注意力。
5.  **范式清晰**：多骨干 + 多任务 + 主表消融 + 结构级箱线图 + 定性图，实验设计严谨可信。

## 8. 局限与问题
1.  **仅医学分割两任务**，未验证自然图像分割/分类，通用性声明证据有限。
2.  **效果随架构而异**（脑分割上 SD-Net/U-Net 提升远大于 DenseNet），对其他网络可能不同。
3.  **对极小结构 cSE 可能有害**（三/四脑室、杏仁核、ventral DC），通道注意力或更适合中大目标。
4.  **细节缺口**：无超参搜索过程、无多次运行方差、无 FLOPs/推理时间对比。
5.  **scSE 融合方式简单**：仅相加，未探讨加权/串联/门控等是否更优。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + Fig. 1 + Table 1 + 结论。
- **复现**：方法 2.1–2.3 + Fig. 1，加 Model Learning（4+1+4 块、median frequency balancing、LR 0.01/10ep 降阶、动量 0.95、wd 1e-4、batch 4、SGD）。
- **借鉴创新点**：SE 的挤压-激励轻量校准范式；scSE 的并行（通道+空间相加）结构；多骨干+多任务的验证思路。
- **写 Related Work**：归入注意力机制 / 特征重标定 / 医学图像分割改进，定位为 SE-Net 在分割领域的直接拓展。

## 10. 和其他论文的关系
- [[SE-Net (Squeeze-and-Excitation Networks)]]：本文直接沿用并拓展其通道 SE（cSE），是方法的直接前身（参考文献 [10]，Hu et al. CVPR 2018）。
- [[CBAM (Convolutional Block Attention Module)]]：将通道与空间注意力以串联方式结合（其空间注意力实现与本文 sSE 不同）；与 scSE 同为通道-空间混合注意力的重要工作，可对比"并发相加 vs 串联"两条路线。
- [[U-Net]]、[[SD-Net]]、[[FC-DenseNet]]：本文验证 SE 块所用的三种基础骨干（参考文献 [3][4][9]）。
- [[Attention U-Net]]：另一种为医学分割设计的注意力门控（侧重跳跃连接中的空间注意力），与本文将 SE 作为独立插件的路径不同。

## 11. 关键词
注意力机制，特征重标定，挤压激励，全卷积网络，医学图像分割，脑分割，器官分割，cSE，sSE，scSE，U-Net，SD-Net，DenseNet，通道注意力，空间注意力，median frequency balancing

## 12. 可信度说明
本精读笔记**完全基于**提供的 PDF 提取文本生成，所有论述、数据、公式、引用均来自该文本，未编造信息。提取缓存覆盖论文全部 8 页（8/8），含摘要、引言、方法（含公式 1-3 与复杂度推导）、实验（Table 1、Fig. 2-4、Model Learning 训练细节）、结论与参考文献，信息完整。本次复核相对原稿的修正：(1) 补全论文完整标题；(2) cSE 全连接为先降维到 C/2 再升回 C，新增权重为 C²/2（原稿"FC2(ReLU(FC1))"方向正确但未点明降维比）；(3) 补全此前缺失的训练超参（median frequency balancing、LR/动量/weight decay/batch/SGD/4+1+4 块结构、Titan Xp）；(4) 明确 Dice 增益为脑 +4~8%、全身 +2~3%（原稿个别处误写为 2~8%）；(5) 补充 SD-Net 联合 logistic+Dice 损失、定性结果（左壳核/脾脏）等细节。文中未提供的信息（FLOPs、推理时间、多次运行方差）已标注"未提供"。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2427 字符/页)); 来源缓存: `.paper-cache/extracts/scSE.txt` (8/8 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮据提取文本复核校正(标题/cSE降维比/训练超参/Dice增益区间)。
<!-- AI_READING_NOTE_END -->
