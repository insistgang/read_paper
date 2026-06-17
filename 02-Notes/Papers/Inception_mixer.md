---
title: "Inception Transformer (iFormer)"
authors:
  - "Chenyang Si"
  - "Weihao Yu"
  - "Pan Zhou"
  - "Yichen Zhou"
  - "Xinchao Wang"
  - "Shuicheng Yan"
year: 2022
venue: "arXiv (NeurIPS 2022)"
doi: 
pdf: [[Inception_mixer.pdf]]
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
extract_cache: .paper-cache/extracts/Inception_mixer.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# Inception Transformer (iFormer)

## 基本信息
- **PDF**: [[Inception_mixer.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Inception Transformer |
| **作者** | Chenyang Si, Weihao Yu, Pan Zhou, Yichen Zhou, Xinchao Wang, Shuicheng Yan |
| **机构** | Sea AI Lab; National University of Singapore |
| **发表时间** | 2022 (arXiv:2205.12956v2, 26 May 2022) |
| **刊物/会议** | arXiv 预印本 (后被 NeurIPS 2022 接收) |
| **代码** | https://github.com/sail-sg/iFormer |
| **DOI** | 未明确 |

## 摘要

清理后的英文原摘要（修复空格与连字符断裂）：

> Recent studies show that Transformer has strong capability of building long-range dependencies, yet is incompetent in capturing high frequencies that predominantly convey local information. To tackle this issue, we present a novel and general-purpose Inception Transformer, or iFormer for short, that effectively learns comprehensive features with both high- and low-frequency information in visual data. Specifically, we design an Inception mixer to explicitly graft the advantages of convolution and max-pooling for capturing the high-frequency information to Transformers. Different from recent hybrid frameworks, the Inception mixer brings greater efficiency through a channel splitting mechanism to adopt parallel convolution/max-pooling path and self-attention path as high- and low-frequency mixers, while having the flexibility to model discriminative information scattered within a wide frequency range. Considering that bottom layers play more roles in capturing high-frequency details while top layers more in modeling low-frequency global information, we further introduce a frequency ramp structure, i.e., gradually decreasing the dimensions fed to the high-frequency mixer and increasing those to the low-frequency mixer, which can effectively trade-off high- and low-frequency components across different layers. We benchmark the iFormer on a series of vision tasks, and showcase that it achieves impressive performance on image classification, COCO detection and ADE20K segmentation. For example, our iFormer-S hits the top-1 accuracy of 83.4% on ImageNet-1K, much higher than DeiT-S by 3.6%, and even slightly better than much bigger model Swin-B (83.3%) with only 1/4 parameters and 1/3 FLOPs.

中文翻译：

> 近期研究表明，Transformer 擅长建立长程依赖，却不善于捕捉主要承载局部信息的高频成分。为此，本文提出一种新颖且通用的 Inception Transformer（简称 iFormer），它能有效学习视觉数据中同时包含高频与低频信息的全面特征。具体而言，我们设计了一个 Inception mixer，将卷积与最大池化擅长捕捉高频信息的优势显式地嫁接到 Transformer 中。与近期的混合框架不同，Inception mixer 通过通道拆分机制，把并行的卷积/最大池化路径与自注意力路径分别作为高频与低频混合器，从而带来更高的效率，同时具备建模散布于宽频带内判别性信息的灵活性。考虑到底层更多承担捕捉高频细节的角色、顶层更多承担建模低频全局信息的角色，我们进一步引入频率坡道（frequency ramp）结构，即从底层到顶层逐渐减少送入高频混合器的通道维度、增加送入低频混合器的通道维度，从而在不同层之间有效权衡高低频成分。我们在一系列视觉任务上对 iFormer 进行评测，结果表明它在图像分类、COCO 检测和 ADE20K 分割上均取得出色性能。例如，iFormer-S 在 ImageNet-1K 上取得 83.4% 的 top-1 准确率，比 DeiT-S 高 3.6%，甚至以仅 1/4 的参数量和 1/3 的 FLOPs 略胜参数量大得多的 Swin-B（83.3%）。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：ViT 及其变体擅长捕捉视觉数据中的低频信息（全局形状与结构），但学习高频信息（局部边缘与纹理）的能力较弱。原文从傅里叶频谱角度直观解释（图 1(a)、1(b)）：自注意力是非重叠 patch token 间交换信息的全局操作，更擅长聚合全局信息（低频），而对局部信息（高频）建模不足；这与文献 [14] 中"ViT 表现出低通滤波器特性"的经验结论一致。
- **低频偏好的两点危害**：1) 各层都填充低频信息会破坏高频成分（如局部纹理），削弱 ViT 的建模能力；2) 高频信息同样具有判别性，能使许多任务（如细粒度分类）受益。原文还引用人类视觉系统：低频提供视觉刺激的全局信息，高频传达图像中的局部空间变化（如局部边缘/纹理）。
- **之前方法的问题**：
    1.  **串行混合**（如 CvT、CoAtNet、PVT-v2、ViT_C、UniFormer）：在 Transformer 不同位置堆叠卷积与注意力层，但单层只能处理一种依赖（全局或局部），在建模局部时丢弃全局信息，反之亦然。
    2.  **并行混合**（如 CoaT、ViTAE）：把卷积作为与注意力并行的分支并用逐元素相加融合；但 Raghu 等人 [27] 发现部分通道倾向处理局部依赖、另一部分倾向建模全局信息，说明"对所有通道都跑两个分支"存在信息冗余。GLiT 虽用并行结构，但直接拼接卷积与注意力特征作为输出，缺乏不同频率特征的融合。
- **核心矛盾**：如何在一个 Transformer 层中高效且显式地同时、互补地学习视觉数据中的高频（局部）与低频（全局）信息，避免信息冗余与性能损失。

## 关键贡献

1.  提出 **Inception Transformer (iFormer)**，一种通用的层次化视觉骨干网络，将 CNN 捕捉高频的能力嫁接到 ViT。
2.  设计 **Inception token mixer (ITM)**：先沿通道拆分输入，分别送入高频混合器（最大池化 + 并行深度卷积）与低频混合器（自注意力），并通过显式融合模块合并不同频率分支的输出，从而在对应通道上各自捕捉特定频率信息，减少冗余。命名灵感来自多分支的 Inception 模块 [46, 56–58]。
3.  引入 **频率坡道结构（frequency ramp structure）**：从浅层到深层逐渐减少高频混合器的通道维度、增加低频混合器的通道维度（Ch/C 递减、Cl/C 递增），在所有层之间权衡高低频成分。
4.  在 ImageNet 分类、COCO 检测与实例分割、ADE20K 语义分割上取得 SOTA 性能，验证有效性与泛化性。

## 方法

**整体框架（图 2）**：
iFormer 采用层次化金字塔结构，含 4 个 Stage。输入图像 3×H×W 经各 Stage 的 Patch Embedding 下采样，依次得到 Stage1~4 的特征图，空间分辨率分别为 H/4、H/8、H/16、H/32（通道为 C1~C4）。每个 Stage 由若干 iFormer Block 堆叠。

**关键模块 — Inception Token Mixer (ITM)（图 3）**：
给定输入特征 X ∈ R^{N×C}，沿通道拆分为 X_h ∈ R^{N×Ch} 与 X_l ∈ R^{N×Cl}（Ch + Cl = C），分别送入高频与低频混合器。

1.  **高频混合器（High-frequency Mixer）**：进一步将 X_h 沿通道二分为 X_h1、X_h2 ∈ R^{N×(Ch/2)}，并行两路：
    - X_h1 路：最大池化 + 线性层，利用最大滤波器对锐利变化的敏感性。`Y_h1 = FC(MaxPool(X_h1))`（式 1）。
    - X_h2 路：线性层 + 深度卷积，利用卷积的细节感知能力。`Y_h2 = DwConv(FC(X_h2))`（式 2）。
2.  **低频混合器（Low-frequency Mixer）**：用标准多头自注意力（MSA）在所有 token 间交换信息。为降低底层大分辨率特征图的计算开销，先用平均池化下采样，注意力后再上采样恢复尺寸。`Y_l = Upsample(MSA(AvePooling(X_l)))`（式 7）。注意：池化与上采样的 kernel/stride 仅在前两个 Stage 设为 2。
3.  **拼接与融合（Fusion）**：三路输出沿通道拼接 `Y_c = Concat(Y_l, Y_h1, Y_h2)`（式 3）。由于式 7 的上采样采用最近邻插值，会导致相邻 token 过度平滑，原文设计融合模块：用一个深度卷积在 patch 间交换信息，同时保留逐位置工作的跨通道线性层，`Y = FC(Y_c + DwConv(Y_c))`（式 4）。

**iFormer Block**：在 ITM 与 FFN 前各加 LayerNorm，残差连接：
- `Y = X + ITM(LN(X))`（式 5）
- `H = Y + FFN(LN(Y))`（式 6）

**频率坡道结构（Frequency Ramp）**：受层次化表示（如 ResNet：底层捕细节、顶层建全局）与人类视觉系统启发，为每个 block 定义通道比 Ch/C 与 Cl/C（二者和为 1）；从浅到深 Ch/C 逐渐减小、Cl/C 逐渐增大。各 iFormer 变体的具体配置在附录给出（提取缓存未完整覆盖，见下文补读记录）。

**训练设置（分类）**：ImageNet 上用 AdamW，初始学习率 1×10⁻³（cosine decay），动量 0.9，weight decay 0.05，训练 300 epoch，输入 224×224；数据增强与正则化沿用 DeiT；用 LayerScale 训练深层模型，并用 Timm 实现。微调到 384×384 时 weight decay 1×10⁻⁸、学习率 1×10⁻⁵、batch size 512。

**与已有并行方法的差异**：iFormer 按"高频/低频"语义对通道分组（而非所有通道都跑所有分支），减少冗余；并通过频率坡道显式控制高低频在不同深度的比重；相比 GLiT 直接拼接，iFormer 设计了显式融合模块合并不同频率分支。

## 实验

- **数据集**：ImageNet-1K（分类）、COCO（检测与实例分割）、ADE20K（语义分割）。
- **对比方法**：CNN（RSB-ResNet、ConvNeXt、RegNetY）、ViT（DeiT、PVT、T2T、Swin、Focal、CSwin）、混合 ViT（CvT、CoAtNet、Container、ViTAE/ViTAEv2、UniFormer、BoTNet）。
- **指标**：ImageNet Top-1/Top-5；COCO 边界框 AP^b 与掩码 AP^m；ADE20K mIoU/MS mIoU。
- **图像分类（表 1，224×224）**：
    - **iFormer-S**：20M 参数、4.8G FLOPs，**83.4% Top-1 / 96.6% Top-5**；比 DeiT-S(79.8%) 高 3.6%，比 SOTA ViT（CSwin-T）高 0.7%、比混合 ViT（UniFormer-S）高 0.5%；甚至略胜参数量约 4 倍、FLOPs 约 3 倍的 Swin-B（83.3%）。
    - **iFormer-B**：48M、9.4G，**84.6% Top-1 / 97.0% Top-5**；比相近规模的 SOTA ViT 与混合 ViT 分别高 1.0% 与 0.7%，比 ConvNeXt-S(83.1%) 高 1.5%（亦高于 Swin-S 的 83.0%）。
    - **iFormer-L**：87M、14.0G，**84.8% Top-1 / 97.0% Top-5**，在大模型档位延续优势（参数量与 FLOPs 均低于 CoAtNet-3 的 168M/34.7G 而精度更高）。
- **更大分辨率微调（表 2，384×384）**：iFormer-S↑384 达 84.6%（20M/16.1G），iFormer-B↑384 达 85.7%，iFormer-L↑384 达 85.8%，跨不同计算档位均显著领先。
- **目标检测与实例分割（表 3，COCO val2017，Mask R-CNN，1× schedule，800×1280）**：
    - **iFormer-S**（40M、263G）：**46.2 AP^b / 41.9 AP^m**；相比 ResNet50 提升 8.2 AP^b / 7.5 AP^m，并优于 Swin-T、Focal-T、UniFormer-S。
    - **iFormer-B**（67M、351G）：**48.3 AP^b / 43.4 AP^m**，超过 Focal-S、CSWin-S、UniFormer-B。
- **语义分割（ADE20K，UperNet 框架，表 6）**（据原文 p.15，提取缓存仅含关键摘录，待核）：iFormer 取得 **48.4 mIoU / 48.8 MS mIoU**；iFormer-S 用更少参数比 Swin-T 高 3.9 mIoU，比 UniFormer-S 高 0.8 mIoU。
- **消融与可视化**：原文称在第 4 节做了消融分析以展示各创新点贡献（提取缓存中具体表格数据未覆盖，待核）；图 6 给出 iFormer-S 第 6/12/18 层的傅里叶频谱，显示高频信息从第 6 层到第 18 层逐渐减少，印证频率坡道结构的设计意图。

## 局限

1.  **保留自注意力的计算开销**：低频分支虽用平均池化降分辨率，但仍保留 MSA，整体效率难以匹敌极致轻量的纯卷积网络（如 MobileNet）或专门优化的 Transformer（如 EfficientFormer）。（此为笔记推断，原文未直接讨论。）
2.  **频率坡道配置依赖经验**：各 Stage 的 Ch/C 取值在附录给出（提取缓存未完整覆盖），原文未提供普适的理论或经验公式，复现/迁移可能带来调参负担。
3.  **高频组件贡献未细分**：高频混合器由最大池化与深度卷积并行构成，原文消融在提取缓存中未覆盖，无法从本缓存判断两个分支各自贡献及是否存在更优组合。
4.  **本笔记证据覆盖**：提取缓存为前 12 页正文，ADE20K 分割、附录配置表、完整消融的数值依赖原文后续页摘录，已分别标注"待核"。

## 个人评论

1.  **研究视角的启发**：从**频率分析**角度诊断并设计视觉 Transformer，把 ViT 的缺陷明确归因于对高频信号不敏感（并用傅里叶频谱可视化佐证）。把信号处理思想（频域分析）引入网络设计，对理解与改进模型有启发。
2.  **模块设计的启发**：Inception Mixer 的"**拆分-处理-融合**"框架清晰优雅。对于视觉特征中固有的不同模式（全局与局部），通过**显式的通道路由**让网络不同部分"各司其职"，比让所有通道做同样的事更高效——这点直接呼应了 [27] 关于"不同通道处理不同频率"的观察。
3.  **层次化设计的启发**：频率坡道结构把"高低频通道比"这一全局设计原则与网络深度动态结合，实现**自适应的多尺度特征学习**，启发我们让不同深度的层自动承担不同角色。
4.  **可迁移点**：融合模块用深度卷积缓解最近邻上采样的过度平滑，是一个值得借鉴的小技巧；高频混合器中"最大池化 ∥ 深度卷积"可作为即插即用的局部敏感性增强组件单独尝试。

### 使用建议

- **快速了解**：读摘要、图 2（整体架构）、图 3（Inception Mixer），以及表 1/表 3 关键结果。
- **复现**：重点研读第 3 节（方法），特别是 3.2 节式 (1)-(7) 与结构图，并查附录中各变体的通道数/阶段/池化 stride 配置（表 7）；分类训练设置见 4.1 节。
- **借鉴创新点**：迁移"通道拆分分别处理不同模式信息"的思想（如视频理解拆分时空信息）；借鉴频率坡道做随深度变化的自适应模块配置；尝试高频混合器作为即插即用组件。
- **写 Related Work**：可归入"视觉 Transformer 与 CNN 的混合架构"或"频域感知的视觉模型设计"流派，与 CoAtNet、UniFormer、Focal/CSwin Transformer 等对比。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉骨干网络（Backbone）设计方向，是对视觉 Transformer（ViT）的改进。它要解决的核心问题是：ViT 不擅长捕捉视觉数据中的高频信息（局部边缘、纹理）。作者提出一种混合架构，在单个 token mixer 内同时学习高低频特征。归入"B_注意力算子模块"主题恰当——其核心是名为 Inception mixer 的新型 token 混合算子，把自注意力与卷积、池化以"通道拆分 + 显式融合"的方式集成在一个算子里。

## 2. 一句话总结
iFormer 通过 Inception token mixer 显式地把 CNN 捕捉高频信息的能力嫁接到 Transformer，并用频率坡道结构在不同层间权衡高低频，从而学习更全面的视觉特征，在分类/检测/分割上取得 SOTA。

## 3. 背景与问题
- **为什么要做**：ViT 的自注意力是全局操作，倾向捕捉低频（全局形状/结构），对高频（局部边缘/纹理）建模弱；傅里叶频谱（图 1a/1b）显示 ViT 几乎只保留低频，表现为低通滤波器特性 [14]。低频偏好会破坏局部纹理等高频成分、削弱建模能力，而高频对细粒度分类等任务也是判别性的。
- **之前方法的问题**：
    1.  **串行混合**（CvT、CoAtNet、PVT-v2、UniFormer 等）：单层只能处理一种依赖，建模局部时丢全局，反之亦然。
    2.  **并行混合**（CoaT、ViTAE 用逐元素相加；GLiT 直接拼接）：Raghu 等 [27] 指出部分通道处理局部、另一部分处理全局，对所有通道跑两个分支存在冗余；GLiT 则缺乏不同频率特征的融合。
- **核心矛盾**：如何在一层内高效、显式、互补地同时学习高频与低频，避免冗余与性能损失。

## 4. 核心贡献
1.  提出通用层次化视觉骨干 iFormer，将 CNN 的高频能力嫁接到 ViT。
2.  设计 Inception token mixer：通道拆分 → 高频混合器（最大池化 + 并行深度卷积）/ 低频混合器（自注意力）→ 显式融合，按频率语义路由通道、减少冗余。
3.  提出频率坡道结构：浅到深 Ch/C 递减、Cl/C 递增，跨层权衡高低频。
4.  在 ImageNet、COCO、ADE20K 取得 SOTA。

## 5. 方法详解
**整体框架（图 2）**：4-Stage 金字塔结构，输入 3×H×W，各 Stage 经 Patch Embedding 下采样，输出空间分辨率 H/4、H/8、H/16、H/32（通道 C1~C4），每 Stage 堆叠若干 iFormer Block。

**Inception Token Mixer（图 3）**：输入 X ∈ R^{N×C} 沿通道拆为 X_h ∈ R^{N×Ch}、X_l ∈ R^{N×Cl}（Ch+Cl=C）。
1.  **高频混合器**：X_h 再二分为 X_h1、X_h2 ∈ R^{N×(Ch/2)}：
    - `Y_h1 = FC(MaxPool(X_h1))`（式 1，最大滤波器对锐利变化敏感）。
    - `Y_h2 = DwConv(FC(X_h2))`（式 2，卷积捕捉局部细节）。
2.  **低频混合器**：`Y_l = Upsample(MSA(AvePooling(X_l)))`（式 7）。先平均池化降分辨率以省算力，注意力后上采样恢复；池化/上采样的 kernel 与 stride 仅在前两个 Stage 设为 2。
3.  **拼接 + 融合**：`Y_c = Concat(Y_l, Y_h1, Y_h2)`（式 3）；因式 7 的最近邻上采样会使相邻 token 过度平滑，融合模块用深度卷积跨 patch 交换信息、并保留逐位置的跨通道线性层：`Y = FC(Y_c + DwConv(Y_c))`（式 4）。

**iFormer Block**：`Y = X + ITM(LN(X))`（式 5）、`H = Y + FFN(LN(Y))`（式 6）。

**频率坡道结构**：每个 block 定义 Ch/C 与 Cl/C（和为 1），浅到深 Ch/C 递减、Cl/C 递增；具体配置见附录表 7（提取缓存仅含线索，待核）。

**训练**：ImageNet，AdamW，lr 1e-3（cosine），动量 0.9，weight decay 0.05，300 epoch，224×224，DeiT 增强 + LayerScale + Timm；384 微调 weight decay 1e-8、lr 1e-5、batch 512。

## 6. 实验与结果
- **分类（表 1，224²）**：iFormer-S 20M/4.8G → 83.4%/96.6%（比 DeiT-S 高 3.6%，比 CSwin-T 高 0.7%、UniFormer-S 高 0.5%，略胜 Swin-B 83.3% 且仅 1/4 参数 1/3 FLOPs）；iFormer-B 48M/9.4G → 84.6%/97.0%（比 ConvNeXt-S 高 1.5%、Swin-S 高 1.6%）；iFormer-L 87M/14.0G → 84.8%/97.0%。
- **384 微调（表 2）**：iFormer-S↑384 84.6%、B↑384 85.7%、L↑384 85.8%。
- **检测/实例分割（表 3，COCO val2017，Mask R-CNN 1×）**：iFormer-S 40M/263G → 46.2 AP^b/41.9 AP^m（较 ResNet50 +8.2 AP^b/+7.5 AP^m）；iFormer-B 67M/351G → 48.3 AP^b/43.4 AP^m（超 Focal-S、CSWin-S、UniFormer-B）。
- **分割（ADE20K，UperNet，表 6，据原文 p.15 摘录，待核）**：48.4 mIoU/48.8 MS mIoU；iFormer-S 比 Swin-T 高 3.9 mIoU、比 UniFormer-S 高 0.8 mIoU。
- **可视化（图 6，据原文 p.17 摘录）**：iFormer-S 第 6/12/18 层傅里叶频谱显示高频随层加深而减少，印证频率坡道动机。
- **消融**：原文第 4 节称做了消融分析（提取缓存未覆盖具体数值，待核）。

## 7. 这篇论文真正有价值的地方
1.  **频域视角**：把 ViT 的缺陷量化为傅里叶频谱上的高频缺失，并据此设计补偿模块——诊断与方案一致、有据可循。
2.  **拆分-处理-融合范式**：按频率语义路由通道、显式融合，比"所有通道跑所有分支"更省、更有针对性；融合模块还顺手解决了上采样过度平滑。
3.  **频率坡道**：把"高低频通道比"与深度耦合，是对层次化特征学习的精细建模，且被图 6 的频谱可视化佐证。

## 8. 局限与问题
1.  低频分支仍保留 MSA，整体效率难匹敌极致轻量网络（笔记推断，原文未直接讨论）。
2.  各 Stage 的 Ch/C 取值依赖经验（附录配置），无普适公式，迁移有调参成本。
3.  高频混合器两分支（最大池化/深度卷积）各自贡献，因提取缓存未覆盖消融而无法从本缓存判断。
4.  本笔记的 ADE20K、附录配置、完整消融数值依赖原文后续页摘录，已标"待核"。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 图 2 + 图 3 + 表 1/表 3。
- **复现**：第 3 节式 (1)-(7) 与结构图 + 附录表 7 配置 + 4.1 训练设置。
- **借鉴**：迁移"通道按模式拆分处理"思想；借鉴频率坡道做随深度自适应配置；把高频混合器当即插即用组件试用。
- **写 Related Work**：归入"ViT-CNN 混合架构"或"频域感知视觉模型"，对比 CoAtNet、UniFormer、Focal/CSwin。

## 10. 和其他论文的关系
同属主题"B_注意力算子模块"，相关工作（据原文引用与对比）：
- [[Swin Transformer]]：层次化 ViT，用窗口/移位窗口引入局部性；iFormer 用显式高频混合器引入局部性。
- [[CoAtNet]] / [[UniFormer]]：串行/并行混合 CNN 与 Transformer 的代表；iFormer 是更结构化、按频率拆分的并行方案。
- [[Focal Transformer]] / [[CSwin Transformer]]：从注意力机制（焦点/十字窗口）改进局部建模；iFormer 从频率分解切入。
- CoaT / ViTAE / GLiT：原文直接对照的并行混合基线，iFormer 以"通道拆分 + 显式融合"区别于它们。

## 11. 关键词
视觉Transformer, 骨干网络, 混合架构, Inception token mixer, 通道拆分, 频率分解, 高频信息, 低频信息, 频率坡道结构, 深度卷积, 最大池化, 图像分类, 目标检测, 语义分割

## 12. 可信度说明
本精读笔记主要基于提取缓存覆盖的 PDF 前 12 页（摘要、引言、相关工作、方法第 3 节、实验第 4.1/4.2 节，含表 1/表 2/表 3）生成，这些数值均与提取文本逐项核对。ADE20K 分割（48.4/48.8 mIoU）、图 6 频谱、附录配置（表 7）来自原文 p.13-17，提取缓存仅含关键摘录，已在正文标注"待核"。消融实验的具体数值在提取缓存中未出现。撰写时严格遵守"仅基于提取文本、不编造"的原则。

---

> **可信度补充**: PDF 提取质量 = **high** (提取缓存覆盖 p.1-12/17, 约 2086 字符/页, 清晰); 后续页 p.13-17 仅有关键摘录(见全文补读记录), ADE20K/附录数值标注待核; 来源缓存: `.paper-cache/extracts/Inception_mixer.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: Ziwei Liu, Jiarui Xu, Zheng Zhang, Dazhi Cheng, Chenchen Zhu, Tianheng Cheng, Qijie Zhao, Buyu
- p.14: Li, Xin Lu, Rui Zhu, Yue Wu, Jifeng Dai, Jingdong Wang, Jianping Shi, Wanli Ouyang, Chen Change
- p.15: A Appendix
- p.15: Results. Table 6 shows the mIoU and MS mIoU results of different backbones based on the
- p.15: Method#Param. FLOPs mIoU MS mIoU
- p.15: Frequency ramp structure plays an important role in iFormer, which is designed to learn hierarchical
- p.17: Moreover, the high-frequency information gradually decreases from 6- thlayer to 18- thlayer, and
- p.17: Stage Layer iFormer-S iFormer-B iFormer-L
- p.17: Block2

### 缺失页关键摘录

- p.14: Loy, and Dahua Lin. MMDetection: Open mmlab detection toolbox and benchmark. arXiv preprint
- p.14: benchmark. https://github.com/open-mmlab/mmsegmentation , 2020.
- p.15: Results. Table 6 shows the mIoU and MS mIoU results of different backbones based on the
- p.15: UperNet [ 81] framework. From these results, it can be seen that our iFormer achieves 48.4 mIoU
- p.15: and 48.8 MS mIoU, consistently surpassing previous backbones on this task. For instance, our
- p.15: iFormer-S outperforms the Swin-T [ 5] by 3.9 mIoU while using fewer parameters. Compered with
- p.15: UniFormer-S [22], iFormer-S still achieves 0.8 mIoU improvement.
- p.15: Table 6: Semantic segmentation with semantic UperNet [ 81] on ADE20K [ 32]. The FLOPs are
- p.15: Figure 6: (a) Fourier spectrum of 6- th, 12-thand 18- thlayers for the iFormer-S.
- p.17: i.e., iFormer-S, iFormer-B and iFormer-L. Table 7 shows their detailed conﬁgurations. Following
- p.17: Cl=Care used to balance the high-frequency and low frequency components. As shown in Table 7,
- p.17: Table 7: Conﬁgurations of the variants of iFormer. Pool stride denotes the stride of the pooling and
<!-- AI_READING_NOTE_END -->
