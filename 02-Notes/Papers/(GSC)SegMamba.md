---
title: "SegMamba: Long-range Sequential Modeling Mamba For 3D Medical Image Segmentation"
authors:
  - "Zhaohu Xing"
  - "Tian Ye"
  - "Yijun Yang"
  - "Guang Liu"
  - "Lei Zhu"
year: 2024
venue: "arXiv (arXiv:2401.13560v3)"
doi: 
pdf: [[(GSC)SegMamba.pdf]]
primary_topic: A1_医学图像_分割
topics:
  - "A1_医学图像_分割"
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
extract_cache: .paper-cache/extracts/(GSC)SegMamba.txt
---

# SegMamba: Long-range Sequential Modeling

## 基本信息
- **PDF**: [[(GSC)SegMamba.pdf]]
- **primary_topic**: `A1_医学图像_分割`
- **topics**: `A1_医学图像_分割`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03
- **代码**: https://github.com/ge-xing/SegMamba

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SegMamba: Long-range Sequential Modeling Mamba For 3D Medical Image Segmentation |
| **作者** | Zhaohu Xing; Tian Ye; Yijun Yang; Guang Liu; Lei Zhu |
| **单位** | 香港科技大学(广州) / 北京智源人工智能研究院(BAAI) / 香港科技大学 |
| **发表时间** | 2024 (arXiv:2401.13560v3, 2024-02-25) |
| **刊物/会议** | arXiv (后被 MICCAI 2024 收录, 据原文外信息, 提取缓存未覆盖, 待核) |
| **DOI** | 未明确 |

## 摘要

> **英文原摘要 (清理后)**: The Transformer architecture has demonstrated remarkable ability in modeling global relationships. However, it presents a significant computational challenge when processing high-dimensional medical images. Mamba, as a State Space Model (SSM), has recently emerged as a notable approach for modeling long-range dependencies in sequential data, excelling in the field of natural language processing with its remarkable memory efficiency and computational speed. Inspired by its success, we introduce SegMamba, a novel 3D medical image Segmentation Mamba model, designed to effectively capture long-range dependencies within whole-volume features at every scale. Our SegMamba, in contrast to Transformer-based methods, excels in whole-volume feature modeling, maintaining superior processing speed, even with volume features at a resolution of 64×64×64 (the sequential length is about 260k). Comprehensive experiments on three datasets demonstrate the effectiveness and efficiency of our SegMamba. Additionally, to facilitate research in 3D colorectal cancer (CRC) segmentation, we contribute a new large-scale dataset (named CRC-500). The code for SegMamba and information about the CRC-500 dataset are available at: https://github.com/ge-xing/SegMamba.

> **中文翻译**: Transformer 架构在建模全局关系上表现卓越, 但在处理高维医学图像时面临显著的计算挑战。Mamba 作为一种状态空间模型(SSM), 近期凭借其出色的内存效率与计算速度, 在自然语言处理领域建模长程序列依赖方面崭露头角。受其成功启发, 我们提出 SegMamba——一种新颖的 3D 医学图像分割 Mamba 模型, 旨在于每个尺度上有效捕获整卷(whole-volume)特征中的长程依赖。与基于 Transformer 的方法相比, SegMamba 在整卷特征建模上表现优异, 即便面对 64×64×64 分辨率(序列长度约 26 万)的体特征仍能保持更优的处理速度。在三个数据集上的综合实验验证了 SegMamba 的有效性与高效性。此外, 为推动 3D 结直肠癌(CRC)分割研究, 我们贡献了一个新的大规模数据集 CRC-500。代码与 CRC-500 数据集信息见: https://github.com/ge-xing/SegMamba。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 准确的 3D 医学图像分割能减轻医生的诊断负担, 而扩大模型感受野以提取大范围(全局)信息是该任务的关键。
- **之前方法有什么问题**:
    1.  **CNN-based 方法**: 传统 CNN 难以从高分辨率 3D 医学图像中提取大范围信息; 大卷积核(如 3D UX-Net 的 7×7×7)虽能扩大感受野, 但受卷积局部性所限, 仍难以建模全局关系。
    2.  **Transformer-based 方法**: 如 UNETR(以 ViT 为编码器)、SwinUNETR(以 Swin Transformer 为编码器, 并设计多尺度解码器), 利用自注意力提取全局信息并取得了不错效果。但 3D 医学图像通常分辨率很高, 自注意力的计算复杂度随序列长度二次增长, 带来显著的计算负担和速度下降。为压缩序列长度, UNETR 等直接把 D×H×W 的输入下采样到 D/16×H/16×W/16, 但这会牺牲对解码器至关重要的多尺度特征。
    3.  **已有视觉 Mamba 工作**: U-Mamba 把 Mamba 层集成进 nnUNet 编码器; Vision Mamba 提出含双向 SSM 的 Vim 块; VMamba 设计 CSM 模块弥合 1D 扫描与 2D 遍历的鸿沟。但这些方法**都不是专门为 3D 医学图像分割设计**的。
- **作者想解决的核心矛盾**: **在 3D 医学图像分割中, 如何同时实现高效的长程(全局)依赖建模与低计算/内存开销, 并保留多尺度特征**。即找到一种既能像 Transformer 一样建模全局关系、又能保持高效率的方法。

## 关键贡献

1.  **首个面向 3D 医学图像分割的 Mamba 架构**: 提出 SegMamba, 将 U 形结构与 Mamba 结合, 在多尺度上建模整卷全局特征。作者称这是首个专门将 Mamba 用于 3D 医学图像分割的方法。
2.  **三向 Mamba(ToM)模块**: 将 3D 特征沿**前向、反向、跨切片(inter-slice)**三个方向展平成序列分别用 Mamba 建模再融合, 增强对高维 3D 特征的全局序列建模。
3.  **门控空间卷积(GSC)模块**: 在每个 ToM 之前增强空间维度的特征表示。Mamba 把 3D 特征展平为 1D 序列会损失空间关系, GSC 通过门控机制(逐像素相乘控制信息流, 类似 GLU)在序列建模前先提取空间上下文。
4.  **提出大规模结直肠癌分割数据集 CRC-500**: 包含 500 个带专家精确标注的 3D CT 体, 同时覆盖直肠癌与结肠癌, 是同类数据集中规模最大且开源的(详见 Table 1: 3D RU-Net 64 例、MSDenseNet 43 例、MSD 190 例、Zhang et al. 388 例, 其中仅 MSD 开源但缺直肠癌数据; CRC-500 为 500 例且开源)。数据集按 "upon request" 方式供研究使用。
5.  **高效且有效的全局建模**: 在序列长度高达约 26 万(128³ 输入展平至 262144)的情况下, SegMamba 相比 Transformer 方法在保持更优分割性能的同时, 拥有更低训练内存与更短推理时间, 且自注意力在该规模下直接 OOM。

## 方法

### 整体框架
SegMamba 主要由三部分组成(见论文图 2, p.4): 1) 带多个 **三向空间 Mamba 块(TSMamba Block)** 的 3D 特征编码器, 在不同尺度上建模全局信息; 2) 基于卷积层的 3D 解码器, 用于预测分割结果; 3) 跳跃连接, 把多尺度全局特征接到解码器以复用特征。整体为 **U 形编码器-解码器** 结构。

### 输入与输出
- **输入**: 3D 医学体积图像 `I ∈ R^{C×D×H×W}`(C 为输入通道数)。
- **输出**: 逐体素的分割结果。

### 关键模块详解
#### a) Stem 层
- 采用一个 **7×7×7** 大卷积核的 **深度可分离卷积(depth-wise conv)**, padding=3×3×3, stride=2×2×2, 将输入下采样并映射到 48 通道, 得到第一尺度特征 `z_0 ∈ R^{48×D/2×H/2×W/2}`。**（p.4）**

#### b) TSMamba Block
编码器核心模块, 由若干堆叠的基础单元组成。对第 m 个 TSMamba block, 第 l 层(l ∈ {0,...,N_m−1})的计算流程(公式 1, p.4):
`ẑ_l_m = GSC(z_l_m)`
`z̃_l_m = ToM(LN(ẑ_l_m)) + ẑ_l_m` （残差连接, LN 为层归一化）
`z_{l+1}_m = MLP(LN(z̃_l_m)) + z̃_l_m` （残差连接, MLP 丰富特征表示）
其中 GSC 与 ToM 是本文设计的两个核心算子。

#### c) 门控空间卷积（GSC）模块
- **目的**: Mamba 层把 3D 特征展平为 1D 序列来建模依赖, 会损失空间关系; GSC 在进入 Mamba 前先提取**空间维度**的上下文。
- **结构与机制**（图 3(a), p.5）:
    1.  输入 3D 特征送入两个卷积块(每个卷积块含 Norm + Conv + 非线性层), 卷积核分别为 **3×3×3** 和 **1×1×1**。
    2.  两个分支输出**逐像素相乘**, 以门控机制控制信息传递。
    3.  再用一个卷积块进一步融合, 并以残差连接复用输入特征。
- **公式(式 2)**: `GSC(z) = z + C_{3×3×3}(C_{3×3×3}(z) · C_{1×1×1}(z))`, 其中 C 表示卷积块。**（p.5）**
- **直观理解**: 类似空间门控单元, 为后续序列建模提供更丰富的空间特征。

#### d) 三向 Mamba（ToM）模块
- **目的**: 从三个方向对高维 3D 特征计算特征依赖, 实现全局建模。
- **机制**（图 3(b), p.5）: 将 3D 输入展平成三个序列分别用 Mamba 层建模, 再相加得到融合的 3D 特征。
- **公式(式 3)**: `ToM(z) = Mamba(z_f) + Mamba(z_r) + Mamba(z_s)`, 其中 f=前向(forward)、r=反向(reverse)、s=跨切片(inter-slice)方向。**（p.5）**
- **三个方向**:
    1.  **前向(f)**: 按固定顺序扫描整卷。
    2.  **反向(r)**: 与前向相反。
    3.  **跨切片(s)**: 沿切片间方向交互。原文仅以图 3(b) 示意, **未给出 inter-slice 的精确展开顺序**(PDF 文本未明确)。
- **与已有方法的差异**:
    - **与 CNN**: 替代卷积的局部操作, 实现对整卷的全局建模。
    - **与 Transformer**: Mamba 基于 SSM 的选择机制与硬件感知算法, 复杂度随序列长度呈**线性**, 而自注意力为二次, 故长序列(约 26 万)下效率极高。
    - **与单向 Mamba**: 通过多方向扫描弥补单向扫描丢失上下文的不足, 更全面地捕捉 3D 空间依赖。

### 解码器（3.2 节）
- 沿用以往工作的做法, 采用**基于 CNN 的解码器**配合跳跃连接来预测分割结果(图 2 中各级 Res-block + Transpose Conv + Concatenation, 末端 Seg-head)。

### 训练方式（4.2 Implementation Details, p.6）
- **实现框架**: PyTorch 2.0.1-cuda11.7, Monai 1.2.0。
- **数据输入**: 随机裁剪 **128×128×128** patch, batch size **2/GPU**。
- **优化器**: SGD + 多项式学习率调度器, 初始学习率 **1e-2**, 衰减 **1e-5**。
- **损失函数**: 全部实验用**交叉熵损失**。
- **训练轮次**: 所有数据集 **1000 epochs**。
- **数据增强**: additive brightness、gamma、rotation、scaling、mirror、elastic deformation。
- **硬件**: 云平台 4× NVIDIA A100。
- **数据划分**: 每个数据集随机取 70% 训练 / 10% 验证 / 20% 测试。

### 推理流程
推理时输入完整 3D 体(或滑窗裁剪), 经训练好的 SegMamba: 编码器提取多尺度全局特征, 解码器结合跳跃连接特征, 输出每个体素的类别预测。

## 实验

### 使用的数据集
1.  **BraTS2023**: 1251 个 3D 脑部 MRI 体, 每体 4 模态(T1、T1Gd、T2、T2-FLAIR), 三个分割目标 WT(全肿瘤)/TC(肿瘤核心)/ET(增强肿瘤)。
2.  **AIIB2023**: 120 个高分辨率 CT(HRCT)扫描, 首个公开的气道分割挑战数据集(面向纤维化肺病)。
3.  **CRC-500**(本文提出): 500 个 3D 结直肠癌 CT 体, 含专家精确标注。CT 采集于 2008.01–2020.04, 已去除敏感患者信息, 经一位医生标注、另一位医生校准。in-plane 统一 512×512, z 轴维度 94–238(中位 166); in-plane spacing 0.685×0.685–0.925×0.925mm(中位 0.826), z 轴 spacing 3.0–3.75mm(中位 3.75)。

### 对比方法（六个 SOTA）
- **CNN-based**: SegresNet, 3D UX-Net, MedNeXt
- **Transformer-based**: UNETR, SwinUNETR, SwinUNETR-V2
- 为公平对比, 作者用公开实现重新训练这些方法以得到其最佳结果。

### 评价指标
- **BraTS2023 / CRC-500**: Dice 相似系数(Dice↑), 95% 豪斯多夫距离(HD95↓)。
- **AIIB2023 气道专用**: 交并比 IoU↑, 探测长度比 DLR↑, 探测分支比 DBR↑。

### 主实验结果
- **BraTS2023（Table 2, p.6）**: 对比方法中最佳为 CNN 的 UX-Net(Avg Dice 89.69, HD95 4.81)。SegMamba 在 WT/TC/ET 上 Dice 分别 **93.61 / 92.65 / 87.71**, HD95 分别 **3.37 / 3.85 / 3.48**, **平均 Dice 91.32 / 平均 HD95 3.56**, 全面领先(SwinUNETR-V2 Avg 89.39)。
- **AIIB2023（Table 2, p.6）**: SegMamba 气道树 IoU **88.59** / DLR **70.21** / DBR **61.33**, 均为最优, 显示更好的分割连续性。
- **CRC-500（Table 3, p.7）**: 癌区通常很小且具挑战性, SegMamba 取得最高 Dice **48.02** 与最低 HD95 **30.89**(次优 SegresNet Dice 46.10 / UX-Net 45.73)。

### 消融实验
- **GSC 与 ToM 模块有效性（Table 4, p.7, 在 CRC-500 上）**:
    - M1 基础(仅原始 Mamba 层): Dice **45.34**, HD95 43.01。
    - M2 加 GSC: Dice **46.65**, HD95 37.01(相对 M1 Dice 提升 2.88%、HD95 提升 13.95%), 证明序列建模前增强空间特征有效。
    - M3 加 ToM: Dice **47.22**, HD95 33.32(相对 M2 Dice 提升 1.22%、HD95 提升 9.97%), 证明三向全局建模有效。
    - Ours(GSC + ToM): Dice **48.02**, HD95 **30.89**, 最优。
    - (作为参照, Table 4 中 UX-Net 用大卷积核 LC 的结果为 Dice 45.73 / HD95 49.73。)
- **全局建模模块效率对比（Table 5, p.7-8, 输入 128³, 序列长度 262144）**:
    - M4 大卷积核(UX-Net): 训练内存 TM **18852M**, 推理内存 IM 5776M, 推理时间 IT **1.92 case/s**, 非全局。
    - M5 Swin Transformer(SwinUNETR): TM **34000M**, IM 9480M, IT **1.68 case/s**, 非全局。
    - M6 自注意力: 因计算负担 **OOM(内存溢出)**, 不可行(虽为全局)。
    - Ours TSMamba: TM **17976M**, IM **6279M**, IT **1.51 case/s**, 是唯一可行的全局建模方案, 在 26 万级序列长度下内存与时间均优于上述方法。

### 泛化实验
在三种成像模态/任务(MRI 脑瘤、HRCT 气道、CT 结直肠癌)的公开与自建数据集上验证, 取得全面领先结果, 体现方法的泛化能力。可视化对比见图 4。

### 速度/参数量
PDF 文本未提供 FLOPs 或具体参数量(PDF 文本未明确), 效率优势主要由 Table 5 的内存与推理时间体现。

## 局限

1.  **扫描顺序的启发式设计**: ToM 的前向/反向/跨切片三种扫描顺序, 尤其 inter-slice 方向的精确展开方式, 原文仅以图示意而未详述, 最优扫描策略仍有探索空间。
2.  **对 Mamba 的依赖**: 核心优势建立在 Mamba 架构(选择机制 + 硬件感知算法)之上, 性能与效率受其实现与硬件优化影响。
3.  **解码器相对简单**: 解码器采用标准卷积结构, 未利用 Mamba 特性, 仍有优化空间。
4.  **数据集可获取性**: CRC-500 虽规模最大且声明开源, 但仅以 "upon request" 方式提供, 伦理审批/隐私处理细节有限, 可能影响复现广度。
5.  **未报告参数量/FLOPs**: 效率论证主要依赖内存与推理时间, 缺少参数量与计算量的直接对比(PDF 文本未明确)。

## 个人评论

1.  **把 Mamba 引入 3D 医学分割这一新范式**: 为高维体数据展示了一种替代 Transformer 的线性复杂度长序列建模工具, 在 26 万级序列长度上自注意力直接 OOM 而 SegMamba 仍能跑, 这个对比很有说服力。
2.  **GSC + ToM 的组合思路清晰且可迁移**: "先空间预增强、再多方向序列建模"对所有把 3D 体展平进 SSM 的方法都是合理的补救——展平天然破坏空间邻接, 用轻量门控卷积找回局部空间关系, 思路朴素但有效(消融中 GSC 单独带来约 +1.3 Dice)。两个模块可作为通用即插即用组件。
3.  **CRC-500 是实打实的贡献**: 直接回应了"3D 结直肠癌分割数据集小且多不公开"的痛点(Table 1), 同时覆盖直肠癌与结肠癌, 规模 500 为同类最大。
4.  **实验较严谨但单点偏少**: 三数据集、六对比方法、两组消融、效率分析齐全; 但效率对比缺参数量/FLOPs, 且 inter-slice 扫描细节、解码器结构描述偏简, 复现需结合开源代码。

### 使用建议

- **如果快速了解**: 读摘要(p.1)、引言(p.1-2)、图 2 整体框架(p.4)、Table 2/3/5, 即可掌握核心思想、创新点与结果。
- **如果复现**: 精读 3. Method(GSC 式 2、ToM 式 3 与图 3)及 4.2 Implementation Details, 并参考开源代码补齐 inter-slice 扫描与解码器细节; CRC-500 需联系作者获取。
- **如果借鉴创新点**:
    - **直接替换**: 把 TSMamba Block(GSC + ToM)作为编码器模块换进其他 U-Net 类网络。
    - **模块化借鉴**: 单独用 GSC 作 3D 网络的前置空间增强层; 或把多方向序列扫描思想用于其他 SSM 视觉任务。
- **如果写 Related Work**: 可置于"3D 医学图像分割""SSM/Mamba 在视觉中的应用""长程依赖建模"等小节下。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A1_医学图像_分割]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**3D 医学图像分割**方向, 在本库分类下最贴切的主题是 **A1_医学图像_分割**(此前曾归在"注意力算子模块", 但论文本质是一个完整的 3D 医学分割架构而非通用算子, 故修正)。它要解决的是: Transformer 自注意力在处理高分辨率/高维 3D 医学图像时复杂度二次增长、计算与内存负担巨大的问题。作者提出基于状态空间模型(SSM)Mamba 的 U 形架构 SegMamba, 用线性复杂度的选择性 SSM 替代自注意力来做全局序列建模, 并配套设计了门控空间卷积(GSC)与三向 Mamba(ToM)两个模块。

## 2. 一句话总结
SegMamba 是首个专门为 3D 医学图像分割设计的 Mamba 架构, 通过**三向 Mamba(ToM)**做前向/反向/跨切片的全局序列建模、**门控空间卷积(GSC)**做序列建模前的空间增强, 以线性复杂度高效建模整卷长程依赖, 在 BraTS2023/AIIB2023/自建 CRC-500 上全面超越 CNN 与 Transformer 方法。

## 3. 背景与问题
- **为什么要做**: 准确的 3D 医学分割能减轻诊断负担, 扩大感受野以获取全局信息是关键。
- **之前方法有什么问题**:
    1.  **CNN(含大卷积核, 如 3D UX-Net 的 7×7×7)**: 受卷积局部性所限, 难以建模真正的全局关系。
    2.  **Transformer(UNETR/SwinUNETR/SwinUNETR-V2)**: 自注意力随序列长度二次增长, 高分辨率 3D 图像下计算负担重、速度慢; 为省算力直接 16 倍下采样又损失多尺度特征。
    3.  **已有视觉 Mamba(U-Mamba/Vision Mamba/VMamba)**: 验证了 Mamba 在视觉可用, 但都不是专为 3D 医学分割设计。
- **核心矛盾**: 如何在 3D 医学分割中同时做到高效全局建模 + 低计算/内存开销 + 保留多尺度特征。

## 4. 核心贡献
1.  **首个面向 3D 医学图像分割的 Mamba 架构 SegMamba**(U 形 + Mamba, 多尺度整卷全局建模)。
2.  **三向 Mamba(ToM)**: 前向/反向/跨切片三方向展平 + Mamba 建模 + 相加融合(式 3)。
3.  **门控空间卷积(GSC)**: 序列建模前用 3×3×3 与 1×1×1 双卷积分支逐像素相乘门控 + 残差(式 2), 找回展平丢失的空间关系。
4.  **大规模结直肠癌数据集 CRC-500**: 500 例、含直肠癌+结肠癌、同类最大且开源(Table 1)。
5.  **高效全局建模**: 26 万级序列长度下内存/速度优于 Transformer, 自注意力则 OOM(Table 5)。

## 5. 方法详解
### 整体框架
三部分(图 2, p.4): 多个 TSMamba Block 的 3D 编码器(多尺度全局建模)、基于卷积的 3D 解码器(预测分割)、跳跃连接(多尺度特征复用)。整体 U 形。

### 输入与输出
- **输入**: `I ∈ R^{C×D×H×W}`。
- **输出**: 逐体素分割结果。

### 关键模块详解
#### a) Stem 层
7×7×7 深度可分离卷积, padding 3×3×3, stride 2×2×2, 映射到 48 通道, 得 `z_0 ∈ R^{48×D/2×H/2×W/2}`(p.4)。

#### b) TSMamba Block
基础单元计算流程(式 1, p.4):
`ẑ_l_m = GSC(z_l_m)`
`z̃_l_m = ToM(LN(ẑ_l_m)) + ẑ_l_m`
`z_{l+1}_m = MLP(LN(z̃_l_m)) + z̃_l_m`
其中 l ∈ {0,...,N_m−1}, LN 为层归一化, MLP 丰富特征表示。

#### c) 门控空间卷积（GSC）
- **动机**: Mamba 把 3D 特征展平成 1D 序列损失空间关系, 需在 Mamba 前提取空间上下文。
- **结构(图 3a)**: 输入分别过两个卷积块(Norm+Conv+非线性), 核大小 3×3×3 与 1×1×1; 两支逐像素相乘做门控; 再过一个卷积块融合 + 残差。
- **公式(式 2)**: `GSC(z) = z + C_{3×3×3}(C_{3×3×3}(z) · C_{1×1×1}(z))`。

#### d) 三向 Mamba（ToM）
- **动机**: 高维特征需多方向全局建模。
- **机制(图 3b)**: 展平成三序列分别 Mamba 建模后相加。
- **公式(式 3)**: `ToM(z) = Mamba(z_f) + Mamba(z_r) + Mamba(z_s)`, f 前向 / r 反向 / s 跨切片。inter-slice 的精确展开顺序原文未详述(PDF 文本未明确)。
- **差异**: 相对 CNN 实现全局; 相对自注意力为线性复杂度; 相对单向 Mamba 多方向扫描补足上下文。

### 解码器（3.2）
基于 CNN 的解码器 + 跳跃连接(沿用以往工作), 见图 2 的 Res-block / Transpose Conv / Concatenation / Seg-head。

### 训练方式（4.2, p.6）
PyTorch 2.0.1-cuda11.7 + Monai 1.2.0; 随机裁 128³, batch 2/GPU; SGD + 多项式调度, lr 1e-2、decay 1e-5; 交叉熵损失; 1000 epochs; 增强含 brightness/gamma/rotation/scaling/mirror/elastic; 4× A100; 70/10/20 划分。

### 推理流程
输入完整 3D 体(或滑窗), 编码器提多尺度全局特征, 解码器结合跳跃连接输出逐体素预测。

## 6. 实验与结果
### 使用的数据集
1.  **BraTS2023**: 1251 个脑 MRI 体, 4 模态, WT/TC/ET。
2.  **AIIB2023**: 120 个 HRCT, 气道分割。
3.  **CRC-500**(本文): 500 个结直肠癌 CT 体; 512×512 in-plane, z 94–238(中位 166), in-plane spacing 0.685–0.925mm(中位 0.826), z spacing 3.0–3.75mm(中位 3.75)。

### 对比方法
- CNN: SegresNet, 3D UX-Net, MedNeXt
- Transformer: UNETR, SwinUNETR, SwinUNETR-V2

### 评价指标
- BraTS2023/CRC-500: Dice↑, HD95↓; AIIB2023: IoU↑, DLR↑, DBR↑。

### 主实验结果
- **BraTS2023(Table 2)**: Ours WT/TC/ET Dice 93.61/92.65/87.71, HD95 3.37/3.85/3.48, 平均 Dice 91.32 / HD95 3.56; 最佳对比方法 UX-Net 平均 Dice 89.69, SwinUNETR-V2 89.39。
- **AIIB2023(Table 2)**: Ours IoU 88.59 / DLR 70.21 / DBR 61.33, 均最优。
- **CRC-500(Table 3)**: Ours Dice 48.02 / HD95 30.89, 最优(次优 SegresNet 46.10)。

### 消融实验
- **GSC/ToM 有效性(Table 4, CRC-500)**: M1(仅 Mamba) 45.34 → M2(+GSC) 46.65(Dice +2.88%) → M3(+ToM) 47.22(较 M2 +1.22%) → Ours(GSC+ToM) 48.02, HD95 由 43.01 降至 30.89。
- **效率对比(Table 5, 128³, 序列 262144)**: M4 大卷积核 TM 18852M/IM 5776M/IT 1.92(非全局); M5 Swin TM 34000M/IM 9480M/IT 1.68(非全局); M6 自注意力 OOM(全局但不可行); Ours TSMamba TM 17976M/IM 6279M/IT 1.51(唯一可行全局方案)。

### 泛化实验
跨 MRI/HRCT/CT 三模态、脑瘤/气道/结直肠癌三任务全面领先, 可视化见图 4。

### 速度/参数量
未提供 FLOPs/参数量(PDF 文本未明确), 效率由 Table 5 内存与推理时间体现。

## 7. 这篇论文真正有价值的地方
1.  **Mamba 用于 3D 医学分割的范式开创**: 线性复杂度让 26 万级序列长度的整卷全局建模变得可行, 而自注意力在该规模直接 OOM。
2.  **GSC + ToM 的即插即用设计**: "空间预增强 + 多方向序列建模"对所有展平 3D 进 SSM 的方法都通用, 可作为高效 3D 视觉模型的通用组件。
3.  **CRC-500 基准**: 解决结直肠癌分割数据集小且多不开源的痛点, 500 例同类最大并覆盖直肠+结肠癌。
4.  **较完整的实验链条**: 三数据集对比 + 模块消融 + 效率消融。

## 8. 局限与问题
1.  **扫描顺序启发式**: inter-slice 等方向的精确展开原文未详述, 最优扫描策略待探索。
2.  **依赖 Mamba 实现/硬件优化**。
3.  **解码器为标准卷积**, 未利用 Mamba 特性。
4.  **CRC-500 仅 upon request 提供**, 伦理/隐私细节有限, 影响复现广度。
5.  **缺参数量/FLOPs 直接对比**(PDF 文本未明确)。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言 + 图 2 + Table 2/3/5。
- **复现**: 精读 Method(式 2/式 3、图 3)与 4.2, 结合开源代码补 inter-slice 扫描与解码器细节; CRC-500 需联系作者。
- **借鉴**: 整体换入 TSMamba Block; 或单用 GSC 作前置空间增强; 或迁移多方向扫描思想到其他 SSM 视觉任务。
- **写 Related Work**: 置于"3D 医学图像分割""SSM/Mamba 视觉应用""长程依赖建模"小节。

## 10. 和其他论文的关系
- **核心相关(同为视觉 Mamba 先驱)**: [[U-Mamba]](Mamba 层入 nnUNet 编码器)、[[Vision Mamba]](Vim 块, 双向 SSM)、[[VMamba]](CSM 模块)。SegMamba 是首个**专为 3D 医学分割**设计并引入 GSC/ToM 的 Mamba 架构。
- **任务/对比相关**: [[UNETR]]、[[SwinUNETR]]、[[SwinUNETR-V2]]、[[3D UX-Net]]、[[MedNeXt]]、[[SegresNet]]——论文主要对比的 SOTA CNN/Transformer 方法。
- **基础方法**: [[Mamba]](Gu & Dao 2023, 选择性 SSM)。
- **数据相关**: [[BraTS Challenge]]、[[AIIB23 Challenge]]。

## 11. 关键词
Mamba, 3D 医学图像分割, 状态空间模型(SSM), 长序列建模, 三向 Mamba(ToM), 门控空间卷积(GSC), U 形编码器-解码器, 结直肠癌分割(CRC-500), 线性复杂度, 全局特征建模

## 12. 可信度说明
本精读笔记**基于完整的 PDF 提取文本(10/10 页, 含摘要/引言/CRC-500 数据集/方法/实验/消融/结论/参考文献)**生成。核心方法、公式(式 1/2/3)、Table 2-5 的数字、模块描述与结论均能在文本中找到明确依据。少数细节(inter-slice 扫描的精确展开顺序、参数量/FLOPs)原文未给出, 已如实标注"PDF 文本未明确"。venue 在提取文本中仅见 arXiv 标识, 关于 MICCAI 2024 收录的说法属提取缓存外信息, 已标注待核。整体提取质量良好, 足以支撑一篇准确完整的精读笔记。

---

> **可信度补充**: PDF 提取质量 = **high** (10/10 页全覆盖, 含全部正文表格与参考文献, 约 2504 字符/页); 来源缓存: `.paper-cache/extracts/(GSC)SegMamba.txt` (10/10 页); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
