---
title: "SFFNet: A Wavelet-Based Spatial and Frequency Domain Fusion Network for Remote Sensing Segmentation"
authors:
  - "Yunsong Yang"
  - "Genji Yuan"
  - "Jinjiang Li"
year: 2024
venue: "arXiv:2405.01992 (preprint)"
doi: 
pdf: [[FMS&MDAF.pdf]]
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
extract_cache: .paper-cache/extracts/FMS&MDAF.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/18 pages"
---
# SFFNet: A Wavelet-Based Spatial and Frequency Domain Fusion Network for Remote Sensing Segmentation

## 基本信息
- **PDF**: [[FMS&MDAF.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SFFNet: A Wavelet-Based Spatial and Frequency Domain Fusion Network for Remote Sensing Segmentation |
| **作者** | Yunsong Yang; Genji Yuan; Jinjiang Li（山东工商学院 计算机科学与技术学院, 烟台） |
| **发表时间** | 2024-05-03（arXiv:2405.01992v1） |
| **刊物/会议** | arXiv 预印本（提取文本未给出正式期刊/会议） |
| **代码** | https://github.com/yysdck/SFFNet |
| **DOI** | 未明确 |

## 摘要

**清理后的英文原摘要**（据提取文本修复空格与连字符断裂）：

> In order to fully utilize spatial information for segmentation and address the challenge of handling areas with significant grayscale variations in remote sensing segmentation, we propose the SFFNet (Spatial and Frequency Domain Fusion Network) framework. This framework employs a two-stage network design: the first stage extracts features using spatial methods to obtain features with sufficient spatial details and semantic information; the second stage maps these features in both spatial and frequency domains. In the frequency domain mapping, we introduce the Wavelet Transform Feature Decomposer (WTFD) structure, which decomposes features into low-frequency and high-frequency components using the Haar wavelet transform and integrates them with spatial features. To bridge the semantic gap between frequency and spatial features, and facilitate significant feature selection to promote the combination of features from different representation domains, we design the Multiscale Dual-Representation Alignment Filter (MDAF). This structure utilizes multiscale convolutions and dual-cross attentions. Comprehensive experimental results demonstrate that, compared to existing methods, SFFNet achieves superior performance in terms of mIoU, reaching 84.80% and 87.73% respectively. The code is located at https://github.com/yysdck/SFFNet.

**中文翻译**：

> 为了充分利用空间信息进行分割，并应对遥感分割中灰度剧变区域难以处理的挑战，我们提出 SFFNet（空间与频率域融合网络）框架。该框架采用两阶段设计：第一阶段用空间方法提取具有充分空间细节和语义信息的特征；第二阶段在空间域和频率域同时映射这些特征。在频率域映射中，我们引入小波变换特征分解器（WTFD），用 Haar 小波变换将特征分解为低频和高频分量，并与空间特征融合。为弥合频率特征与空间特征之间的语义鸿沟、促成跨表示域特征的有效选择与组合，我们设计了多尺度双表示对齐滤波器（MDAF），它使用多尺度卷积和双重交叉注意力。综合实验表明，相较已有方法，SFFNet 在 mIoU 上取得更优性能，分别达到 84.80% 和 87.73%。代码地址：https://github.com/yysdck/SFFNet。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：随着卫星与航天传感器的发展，高分辨率遥感影像易于获取，覆盖城市、农田、森林、湖泊等多样场景。遥感图像分割对地理信息系统（GIS）、资源管理、环境监测、危机管理等应用至关重要（土地覆盖制图、变化检测、道路与建筑提取等）。
- **之前方法的问题**：
    1. **纯 CNN 方法**：感受野有限，难以处理小目标、高相似度、相互遮挡等复杂目标特性；后续注意力机制（Dual Attention、Criss-cross、多尺度注意力）虽建立长程依赖，但仍依赖把全局信息转化为 CNN 的局部聚合，难以直接编码全局上下文。
    2. **CNN+Transformer 融合方法**（如 ST-Unet、CSTUnet）：能在一定程度上结合全局与局部信息，但**仅在空间域分割，不利用频率域信息**。在遥感图像复杂背景下，灰度剧变（边缘、阴影、纹理显著变化区域）会导致分割错误，而**频率域特征对这些区域更敏感**。
    3. **少数引入频率域（Haar 小波）的分割研究**：往往**直接用频域特征替代空间特征**，由于遥感图像的特殊性，单纯使用频域特征会带来信息不清晰和**空间信息丢失**（论文 Fig.1(d)：XNet 因空间信息丢失把一辆车分割成两半）。
- **核心矛盾**：如何**有效引入频率域信息**以应对灰度剧变挑战，同时**最大限度保留空间域丰富的语义与空间结构信息**，实现两种表示域的优势互补。

## 关键贡献

据论文摘要与引言中的"In summary, the contributions"列举，共三条：
1.  **WTFD（Wavelet Transform Feature Decomposer）**：引入 Haar 小波变换分解器，作为额外的频率域特征映射分支。将空间特征分解为高频和低频信息，分别补充网络中的局部和全局信息流，从而在引入额外频域信息的同时保留空间特征与丰富语义。
2.  **MDAF（Multiscale Dual-Representation Alignment Filter）**：为实现频率域信息与空间域信息之间的**跨尺度语义对齐与特征选择**，设计该模块。它通过**多尺度垂直条状卷积**和**双重交叉注意力**弥合频域与空间域特征的语义鸿沟，并为分割筛选更具代表性的特征，内部实现"双表示对齐滤波器（DAF）"。
3.  **SFFNet（Spatial and Frequency Domain Fusion Network）**：基于上述两个模块构建两阶段网络。第一阶段做空间特征提取；第二阶段通过全局映射和局部映射保证充分的空间信息，通过 WTFD 引入额外频域信息，再由 MDAF 完成频域与空间特征的语义对齐与特征选择，最终融合输出。
> 注：引言原文存在两处明显笔误——将 MDAF 误写成 "Wavelet Transform Feature Decomposer (MDAF)"，并把 SFFNet 写成 "SSFNet"。据上下文应为 MDAF / SFFNet。

## 方法

- **整体框架**：SFFNet 是两阶段网络（Fig. 2），刻意保持简洁、不使用复杂解码器。
    - **第一阶段（空间特征提取）**：用 **ConvNext** 骨干提取多尺度空间特征 `x1, x2, x3, x4`。具体维度：`x1∈R^{C×H×W}`、`x2∈R^{2C×(H/2)×(W/2)}`、`x3∈R^{4C×(H/4)×(W/4)}`、`x4∈R^{8C×(H/8)×(W/8)}`，其中 **C=96**。将后三个尺度的特征经卷积与插值调到同一尺度并拼接，得到融合特征 `X′∈R^{3C×(H/2)×(W/2)}`（公式(1)），兼顾深层语义与浅层空间信息。
    - **第二阶段（特征映射与融合）**：以 `X′` 作为输入，经三个并行分支映射（公式(2)）：
        1.  **全局分支（Global Branch）**：改进的 Swin Transformer，输出全局特征 `Fg`。
        2.  **局部分支（Local Branch）**：池化金字塔做多尺度局部特征映射，输出 `Fm`。
        3.  **频域分支（WTFD）**：Haar 小波变换将 `X′` 分解为低频特征 `Fl` 和高频特征 `Fh`。
        - `Fg, Fm, Fl, Fh` 维度均为 `C×(H/4)×(W/4)`。
        4.  **融合（MDAF，公式(3)）**：按表示域配对送入 MDAF —— **全局特征配低频**：`F′g = fmdaf(Fg, Fl)`；**多尺度局部特征配高频**：`F′m = fmdaf(Fm, Fh)`。
        5.  **输出（公式(4)）**：`Y = δ(Cat(φ(F′g), φ(F′m), x1, δ(X′)))`，即把带频域信息的全局/局部特征、第一阶段浅层特征 `x1`、融合特征 `X′` 一起拼接，经分割头得到最终结果 `Y`（维度 `C×(H/2)×(W/2)`）。
- **输入输出**：输入遥感图像 `x∈R^{3×h×w}`；输出像素级语义分割结果 `Y`。
- **关键模块**：
    1.  **全局分支**：先下采样，再像 Swin 一样用 W-Trans 块做窗口划分并在窗内建立全局特征；但**放弃 Swin 复杂的 SW-Trans（SW-MSA）块**，改用更高效的**垂直条状卷积**（核尺寸 `(1×ws)` 和 `(ws×1)`，`ws` 为窗口大小）建立窗口间的远程依赖（Fig. 4），以降低计算复杂度并更适配遥感任务。
    2.  **WTFD**（Fig. 3(b)）：核心是 Haar 小波变换，将原始特征分解为**低频**（主体轮廓、平滑区域）和**高频**（边缘、纹理细节）成分，再嵌入 CNN 网络，与空间特征结合，使模型在新表示域中考虑特征。
    3.  **MDAF**（本文最核心的注意力模块）：接收一对空间特征 `S` 和频域特征 `F`，通过**多尺度垂直条状卷积**和**双重交叉注意力**对齐二者语义并做特征选择，内部实现"双表示对齐滤波器（DAF）"，公式化为 `F′ = fmdaf(S, F)`。
- **训练方式 / 损失函数**：论文 III 节末提到"最后介绍所采用的损失函数（loss function）"，但**该部分位于提取缓存未覆盖的后续页（提取在 III.B 全局分支处截断）**，具体损失函数与训练细节 PDF 提取文本未覆盖，待核。
- **推理流程**：端到端单次前向，与训练一致。
- **与已有方法的差异**：不同于"直接替换/简单拼接频域特征"的做法，SFFNet **保留独立的空间信息映射路径**（全局 + 局部），并**通过专门的 MDAF 做深度跨域融合**，而非简单叠加，更好地平衡了空间信息保留与频域信息引入。
- **论文类型特化（注意力类）**：
    - **注意力作用维度**：MDAF 作用于**空间域与频率域的跨域对齐**，并以多尺度卷积在**多尺度**上做特征筛选；其双重交叉注意力让空间与频域特征互为 query/key。
    - **可插入性**：MDAF 是 SFFNet 第二阶段的特征融合组件，用于对齐两组特定特征图（全局-低频、局部-高频）。
    - **计算量 vs 效果**：用垂直条状卷积替代 SW-MSA 旨在提升全局映射效率；多尺度卷积与双重交叉注意力会带来一定开销，目标是换取灰度剧变区域的分割性能提升。具体 FLOPs/参数量在提取缓存覆盖范围（p.1-4 内容）未给出。

## 实验

> 说明：提取缓存仅覆盖至 III.B 全局分支（约前 4 页正文），实验章节大多在未覆盖页。以下数据集名、消融数字来自**原笔记的全文补读记录（据原文 p.13-14，提取缓存未覆盖，待核）**与摘要。

- **使用的数据集**：摘要称在"两个主流遥感分割数据集"上实验；据原文后续页补读，为 **Vaihingen** 和 **Potsdam**（ISPRS 遥感语义分割基准）（提取缓存未覆盖，待核）。
- **对比方法**：引言/补读中出现 **ST-Unet**、**XNet**（纯频域）、**ABCNet**、**DC-Swin** 等（提取缓存未覆盖，待核）。
- **评价指标**：**mIoU**（主要）与 **F1**（据补读记录）。
- **主实验结果**：摘要明确 —— "SFFNet achieves superior performance in terms of mIoU, reaching **84.80%** and **87.73%** respectively."（分别对应两个数据集）。
- **消融实验**：据原文 p.13 补读，存在针对高/低频特征的消融，例如"在 baseline 上加入高频特征使 mIoU 提升…"、"移除某成分使 Vaihingen 上 mIoU 下降约 1.18%、F1 下降 0.68%"、"Potsdam 上移除高频特征使 mIoU 下降 0.8%、F1 下降 0.46%"等（具体数字据原文后续页，提取缓存未覆盖，待核）。
- **可视化**：Fig.11-13、Fig.18 等给出分割结果局部放大对比与频域特征可视化（据补读记录，提取缓存未覆盖，待核）。
- **速度/参数量/FLOPs**：提取缓存覆盖范围内未见效率数字。

## 局限

1.  **场景适用性**：方法主要针对灰度剧变区域设计；对不存在该问题的简单遥感场景，频域融合优势可能不明显，而额外计算（小波变换、MDAF）可能成为负担。
2.  **效率指标缺失（就提取文本而言）**：提取缓存覆盖页未给出参数量、FLOPs、推理速度等，难据此评估部署潜力（完整论文是否提供需核后续页）。
3.  **数据集范围**：实验仅在两个遥感数据集（Vaihingen/Potsdam）上进行，在其他视觉领域或不同特性遥感数据上的有效性有待验证。
4.  **复现风险**：MDAF 含多尺度卷积与双重交叉注意力，结构较复杂；提取文本未给出注意力头数、卷积具体配置等细节（损失函数页亦未覆盖），需结合官方代码 https://github.com/yysdck/SFFNet 对照复现。
5.  **笔误**：原文将 MDAF 误标为 WTFD、SFFNet 误写为 SSFNet，对快速阅读者可能造成混淆。

## 个人评论

1.  **思想启发**：展示了**空间域与频率域特征融合**在解决特定视觉难题（灰度剧变）中的潜力。提醒研究者：除了空间维度，信号处理领域的经典工具（小波变换）可作为深度学习特征的强力补充，且不必以丢弃空间信息为代价——关键在"补充"而非"替换"。
2.  **模块设计思路**：MDAF 给出一种**跨域特征对齐与选择**范式——不是简单拼接或相加，而是用双重交叉注意力让网络按上下文从两种表示域特征中筛选最有用信息再融合。其"全局配低频、局部配高频"的配对（公式(3)）有明确语义动机：低频对应大尺度/平滑结构与全局轮廓，高频对应边缘细节与局部纹理。
3.  **工程借鉴**：全局分支用垂直条状卷积 `(1×ws)`/`(ws×1)` 替代 Swin 的 Shifted Window，是一种针对遥感任务**平衡全局建模能力与计算效率**的实用技巧，可迁移到其他需要高效全局感受野的稠密预测场景。

### 使用建议

- **如果快速了解**：读 **Abstract** 与 **Introduction**（第 I 节），迅速掌握问题、核心思想与三条贡献。
- **如果复现**：精读 **III. METHOD**，重点 **A. SFFNet Structure**（公式(1)-(4)）和 **B. Feature Mapping**（全局分支/局部分支/WTFD），结合 **Fig. 2, 3, 4**；MDAF 内部细节与损失函数需查后续页与官方代码库 https://github.com/yysdck/SFFNet 对照。
- **如果借鉴创新点**：
    - 借鉴 **空间-频域融合思想**：看 WTFD 如何用 Haar 小波生成高/低频特征并与空间特征并行处理。
    - 借鉴 **跨域特征对齐机制**：研究 MDAF 如何用双重交叉注意力对齐和选择异质特征。
- **如果写 Related Work**：可归入 1) 基于注意力机制的语义分割；2) 频域/小波特征在图像处理中的应用；3) Transformer 与 CNN 混合架构；4) 遥感图像分割。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的**遥感图像语义分割**方向，核心是设计一种**融合空间域与频率域信息**的深度网络，解决遥感图像中灰度剧变区域（阴影、边缘、纹理显著变化）的分割难题。归类于 **"B_注意力算子模块"**：其头牌创新是名为 **MDAF（Multiscale Dual-Representation Alignment Filter）** 的注意力模块，用**多尺度（垂直条状）卷积**和**双重交叉注意力**对齐并选择来自不同表示域的特征。（次级主题亦贴合"遥感图像分割 / 频域特征"。）论文为 arXiv:2405.01992v1（2024-05-03），代码开源于 https://github.com/yysdck/SFFNet。

## 2. 一句话总结
SFFNet 是一个两阶段网络：先用 ConvNext 提取空间特征，再在第二阶段并行做全局映射、局部映射和 Haar 小波频域分解（WTFD），并用 MDAF 注意力模块把"全局-低频""局部-高频"两对特征做语义对齐与特征选择，从而在保留空间信息的同时引入频域信息，提升灰度剧变区域的分割性能（两数据集 mIoU 84.80% / 87.73%）。

## 3. 背景与问题
- **为什么要做**：高分辨率遥感影像普及，分割对 GIS、资源管理、环境监测等至关重要。纯空间域方法（CNN 或 CNN-Transformer 融合）在阴影、边缘等灰度剧变区域表现不佳，而频域特征对这些区域更敏感。
- **之前方法的问题**：
    1. 纯 CNN 感受野有限；注意力机制（Dual Attention、Criss-cross、多尺度注意力）仍把全局信息化为 CNN 局部聚合，难直接编码全局上下文。
    2. CNN+Transformer 融合（ST-Unet、CSTUnet）仅在空间域分割，不用频域信息。
    3. 少数引入 Haar 小波的分割工作**直接用频域特征替换空间特征**，导致空间信息丢失、信息不清晰（Fig.1(d)：XNet 把车切成两半）。
- **核心矛盾**：如何在**有效引入频域信息**的同时**最大限度保留空间域语义与结构信息**，实现优势互补。

## 4. 核心贡献
1.  **WTFD**：Haar 小波分解器作为额外的频域映射分支，把空间特征分解为高/低频信息分别补充局部/全局信息流，引入频域信息的同时保留空间特征与语义。
2.  **MDAF**：用多尺度垂直条状卷积 + 双重交叉注意力实现频域与空间特征的跨尺度语义对齐与特征选择（内部即"双表示对齐滤波器 DAF"）。
3.  **SFFNet**：两阶段架构——一阶段空间特征提取，二阶段全局/局部映射保空间信息 + WTFD 引频域 + MDAF 融合，结构简洁、不用复杂解码器。
> 原文笔误：引言把 MDAF 写成 "WTFD"、把 SFFNet 写成 "SSFNet"。

## 5. 方法详解
- **整体框架**（Fig. 2，两阶段，无复杂解码器）：
    - **一阶段**：ConvNext 提取 `x1..x4`（`x1∈R^{C×H×W}` … `x4∈R^{8C×(H/8)×(W/8)}`，**C=96**）；后三尺度经卷积+插值调同尺度并拼接为 `X′∈R^{3C×(H/2)×(W/2)}`（公式(1)）。
    - **二阶段**（输入 `X′`，三并行分支，公式(2)）：
        1.  **全局分支**：改进 Swin → `Fg`。
        2.  **局部分支**：池化金字塔多尺度局部映射 → `Fm`。
        3.  **WTFD**：Haar 小波分解 → 低频 `Fl`、高频 `Fh`。`Fg/Fm/Fl/Fh` 维度均 `C×(H/4)×(W/4)`。
        4.  **MDAF 配对融合**（公式(3)）：`F′g = fmdaf(Fg, Fl)`（全局+低频）、`F′m = fmdaf(Fm, Fh)`（局部+高频）。
        5.  **输出**（公式(4)）：`Y = δ(Cat(φ(F′g), φ(F′m), x1, δ(X′)))`，经分割头得 `Y`（`C×(H/2)×(W/2)`）。
- **输入输出**：输入 `x∈R^{3×h×w}`；输出像素级分割 `Y`。
- **关键模块**：
    1.  **全局分支**（Fig.3(a)/Fig.4）：下采样后用 W-Trans 块做窗内全局建模；**放弃 Swin 的 SW-MSA**，改用垂直条状卷积 `(1×ws)`、`(ws×1)` 建立窗口间远程依赖，更高效、更适配遥感。
    2.  **WTFD**（Fig.3(b)）：Haar 小波把特征分解为低频（轮廓/平滑）与高频（边缘/纹理）成分，嵌入 CNN 与空间特征结合。
    3.  **MDAF**：接收空间特征 `S` 与频域特征 `F`，多尺度垂直条状卷积 + 双重交叉注意力做对齐与选择，`F′ = fmdaf(S, F)`。
- **损失函数 / 训练细节**：III 节末提到将介绍损失函数，但**该部分在提取缓存未覆盖的后续页**，具体损失/优化器/超参 PDF 提取文本未覆盖，待核（可查代码库）。
- **与已有方法差异**：保留独立空间映射路径（全局+局部），用专门 MDAF 做深度跨域融合，而非替换或简单叠加。

## 6. 实验与结果
> 提取缓存仅覆盖至 III.B；以下数据集/数字来自原笔记全文补读（据原文 p.13-14，提取缓存未覆盖，待核）与摘要。
- **数据集**：Vaihingen、Potsdam（ISPRS 遥感语义分割，据补读，待核）。
- **对比方法**：ST-Unet、XNet（纯频域）、ABCNet、DC-Swin 等（据补读，待核）。
- **指标**：mIoU（主）、F1（据补读）。
- **主结果**：mIoU 分别达 **84.80%** 和 **87.73%**（摘要明确）。
- **消融**：含高/低频特征消融，如移除某成分使 Vaihingen mIoU 下降约 1.18%、F1 下降 0.68%；Potsdam 移除高频使 mIoU 下降 0.8%、F1 下降 0.46%（具体数字据原文后续页，提取缓存未覆盖，待核）。
- **可视化**：Fig.11-13、Fig.18 分割局部放大对比与频域可视化（据补读，待核）。
- **效率**：提取缓存覆盖页未见 FLOPs/参数量。

## 7. 这篇论文真正有价值的地方
1.  **空间-频域融合范式**：用小波在不丢弃空间信息的前提下补充频域线索，应对灰度剧变——"补充而非替换"是相对前作（XNet 等）的关键改进。
2.  **MDAF 的跨域对齐设计**：双重交叉注意力 + 多尺度卷积，让网络按上下文从异质表示域中选优融合；"全局配低频、局部配高频"的配对有清晰语义动机。
3.  **高效全局建模技巧**：垂直条状卷积替代 SW-MSA，平衡全局感受野与计算效率，可迁移至其他稠密预测任务。

## 8. 局限与问题
1.  **场景适用性**：主要针对灰度剧变区域；简单场景下频域融合优势可能不抵其额外计算开销。
2.  **效率指标（就提取文本而言）缺失**：提取缓存覆盖页未给出参数量/FLOPs/速度，需核后续页。
3.  **数据集范围**：仅两个遥感数据集，跨域/跨数据集泛化待验证。
4.  **复现风险**：MDAF 复杂（多尺度卷积 + 双重交叉注意力），头数、卷积配置、损失函数等细节未在提取文本出现，需对照官方代码。
5.  **原文笔误**：MDAF↔WTFD、SFFNet↔SSFNet 混写，易误导。

## 9. 我该怎么使用这篇论文
- **快速了解**：读 Abstract + Introduction（第 I 节）。
- **复现**：精读 III. METHOD（A. SFFNet Structure 公式(1)-(4)；B. Feature Mapping），结合 Fig.2/3/4；MDAF 内部与损失函数查后续页 + 官方代码 https://github.com/yysdck/SFFNet。
- **借鉴创新点**：空间-频域融合看 WTFD；跨域对齐看 MDAF。
- **写 Related Work**：可放入 1) 注意力机制语义分割；2) 频域/小波特征图像处理；3) Transformer+CNN 混合架构；4) 遥感图像分割。

## 10. 和其他论文的关系
基于主题"B_注意力算子模块"，本文与以下方向相关（提取文本中实际出现的对照/引用方法已注明，其余为基于主题的合理推测，不建立确切双链）：
- **CNN+Transformer 遥感分割**：`[[ST-Unet]]`、CSTUnet、DC-Swin、ABCNet（文中作为对比/相关方法出现）。
- **纯 Transformer 分割**：Segmenter、SwinUNet。
- **小波 + 深度学习图像处理**：`[[MWCNN]]`（多级小波 CNN，图像复原）、Wavelet-SRNet（人脸超分）。
- **纯频域替换式分割**：XNet（文中作为反例：空间信息丢失）。
- **多尺度/交叉注意力特征融合**：与本文 MDAF 同属注意力融合范式的工作。

## 11. 关键词
语义分割, 遥感图像, 注意力机制, 双重交叉注意力, 频域特征, Haar小波变换, 空间-频域融合, 多尺度, 垂直条状卷积, 全局建模, ConvNext, SFFNet, MDAF, WTFD

## 12. 可信度说明
本精读基于 PDF 提取文本，但提取缓存实际只覆盖到 **III.B 全局分支**（约前 4 页正文：Abstract、Introduction、Related Work、Method 的 A 节及 B 节开头），在 25000 字符处截断。**确凿支撑**：标题/作者/单位、arXiv 号、代码地址、两数据集 mIoU 84.80%/87.73%、两阶段结构、公式(1)-(4)、C=96、各特征维度、WTFD/MDAF/全局分支设计、垂直条状卷积替代 SW-MSA 等。**未被提取文本覆盖、保留自原笔记全文补读并标注"待核"**：数据集名（Vaihingen/Potsdam）、消融具体数字、F1 指标、对比方法细节、损失函数与训练细节、效率指标。这些内容已逐处标明来源与不确定性。

---

> **可信度补充**: PDF 提取质量 = **high**（提取页面文本清晰，约 2086 字符/页）；但**提取缓存仅 12/18 页且在 25000 字符处截断**，实际覆盖到正文 III.B；来源缓存: `.paper-cache/extracts/FMS&MDAF.txt`；原 AI 主体覆盖 p.1-12 文本 + 全文补读补足 p.13-18 摘录；生成日期: 2026-06-05；模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-18; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-18。
- **提取情况**: 缺失页 6 页, 其中 6 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: SFFNet on the Vaihingen dataset resulted in a decrease of
- p.13: These reductions in performance are attributed to the semantic
- p.13: Therefore, we are more inclined to consider ConvNext-Tiny
- p.14: For the comparative models, the selected models are as
- p.14: Results of the Vaihingen Dataset: Tab.V presents numeri-
- p.14: ABCNet but also exceeded the DC-Swin network, based on
- p.14: Swintransformer, which has strong global information repre-
- p.14: CNN combined with Transformer network, relies solely on
- p.14: Our SFFNet surpassed XNet, which uses purely frequency
- p.14: In addition to comparing the segmentation accuracy of
- p.14: We selected the results of the first 44 rounds of training as
- p.14: Furthermore, compared to other models, our model exhibits

### 缺失页关键摘录

- p.13: Fig. 18. Local enlarged view of segmentation results of SFFNet and other comparative models on the Potsdam dataset. (a) corresponds to ABCNet. (b)
- p.13: to Xnet. (h) corresponds to SFFNet (Ours). Similar to the results on the Vaihingen dataset, it can be observed from the figure that our model performs better in
- p.13: to a decrease of 1.18% in mIoU and 0.68% in F1. Conversely,
- p.13: mIoU by 1.18% and F1 by 0.73%. On the other hand,
- p.13: SFFNet on the Vaihingen dataset resulted in a decrease of
- p.13: 0.69% in mIoU and 0.41% in F1. Similarly, on the Potsdam
- p.13: dataset, removing the high-frequency features led to a decrease
- p.13: of 0.8% in mIoU and 0.46% in F1. Conversely, adding high-
- p.13: frequency features to the baseline model increased mIoU by
- p.13: Through visualization results in Fig.11, it is observed that
- p.13: Fig.13(e), it can be seen that low-frequency features and
- p.13: On the other hand, through visualization results in Fig.12,
<!-- AI_READING_NOTE_END -->
