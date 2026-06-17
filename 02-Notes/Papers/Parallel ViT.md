---
title: Three things everyone should know
authors:
  - "Hugo Touvron"
  - "Matthieu Cord"
  - "Alaaeldin El-Nouby"
  - "Jakob Verbeek"
  - "Hervé Jégou"
year: 2022
venue: "ECCV"
doi: 
pdf: [[Parallel ViT.pdf]]
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
extract_cache: .paper-cache/extracts/Parallel ViT.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/22 pages"
---
# Three things everyone should know

## 基本信息
- **PDF**: [[Parallel ViT.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Three things everyone should know about Vision Transformers |
| **作者** | Hugo Touvron; Matthieu Cord; Alaaeldin El-Nouby; Jakob Verbeek; Hervé Jégou (Meta AI / Sorbonne University / Inria) |
| **发表时间** | 2022 |
| **刊物/会议** | ECCV |
| **DOI** | 未明确 |

## 摘要

> After their initial success in natural language processing, transformer architectures have rapidly gained traction in computer vision, providing state-of-the-art results for tasks such as image classification, detection, segmentation, and video analysis. We offer three insights based on simple and easy to implement variants of vision transformers. (1) The residual layers of vision transformers, which are usually processed sequentially, can to some extent be processed efficiently in parallel without noticeably affecting the accuracy. (2) Fine-tuning the weights of the attention layers is sufficient to adapt vision transformers to a higher resolution and to other classification tasks. This saves compute, reduces the peak memory consumption at fine-tuning time, and allows sharing the majority of weights across tasks. (3) Adding MLP-based patch pre-processing layers improves Bert-like self-supervised training based on patch masking. We evaluate the impact of these design choices using the ImageNet-1k dataset, and confirm our findings on the ImageNet-v2 test set. Transfer performance is measured across six smaller datasets.

> **中文翻译**：在自然语言处理中取得初步成功后，Transformer 架构迅速进入计算机视觉领域，在图像分类、检测、分割和视频分析等任务上取得了 SOTA 结果。本文基于若干简单、易实现的视觉 Transformer 变体，给出三点见解：(1) ViT 通常顺序处理的残差层，在一定程度上可以高效地并行处理，且不会明显影响精度；(2) 仅微调注意力层的权重，就足以让 ViT 适配更高分辨率和其他分类任务，这既节省算力、降低微调时的峰值显存，又允许在多个任务间共享大部分权重；(3) 加入基于 MLP 的 patch 预处理层，能改善基于 patch 掩码的 BERT 式自监督训练。本文在 ImageNet-1k 上评估这些设计选择的影响，并在 ImageNet-v2 测试集上验证结论，迁移性能则在六个较小数据集上测量。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：ViT 是 Transformer 在视觉上的直接搬运（图像切成不重叠 patch，经线性投影后送入标准 Transformer），相比卷积网络它在单层内即可获得并行处理和完整感受野。然而原文指出，ViT 的**设计和训练流程**至今只被有限地探索过，仍有简单却未被充分挖掘的改进空间。
- **之前方法的问题**：
  1. 标准 ViT 采用顺序层结构。在网络很深时优化会受阻——原文回顾了 GoogleNet/ResNet 的深度-宽度之争，指出即便有残差连接，过深仍会妨碍优化；已有工作（如 LayerScale）就是为缓解 ViT 的深层优化问题而提出。
  2. 跨分辨率或下游分类任务的迁移通常需要全参数微调，计算成本和峰值显存高，且占参数主体的权重无法在任务间复用。
  3. 基于 patch 掩码的自监督方法（如 BeiT、MAE）需要把掩码施加在 patch 上。但常用的卷积 stem 会在 patch 之间传播信息，破坏掩码预测任务所要求的 patch 独立性，因此卷积式预处理与掩码自监督**先天不兼容**。
- **核心矛盾**：如何在**不显著损害精度**的前提下，分别从三条相互独立的路径改进 ViT——并行化以降延迟/简化优化、只调注意力以降低适配成本、用禁止 patch 间通信的 stem 兼容掩码自监督。

## 关键贡献

本文不提出新架构，而是给出三个具体、易实现的见解（对应正文第 3/4/5 节）：
1. **并行 ViT（Depth vs Width）**：把原本顺序的成对 (MHSA, FFN) 残差块重组为并行结构，得到更"宽"更"浅"、但**参数量和 FLOPs 完全不变**的网络。原文强调该方案比 Non-deep Networks 等并行分支设计更简单、更灵活，直接构建在标准 ViT 之上。
2. **微调注意力足矣（Fine-tuning attention is all you need）**：在适配更高分辨率或迁移到其他分类任务时，**仅微调 MHSA 层、冻结 FFN 层**即可——跨分辨率微调时精度差异在统计上不显著（标准差 ±0.1 内），对大模型迁移到其他分类任务时精度损失也有限。由于 FFN 参数约是 MHSA 的两倍（占参数主体），冻结它可大量复用权重、降低算力与峰值显存。
3. **用于掩码自监督的 hMLP stem**：提出分层 MLP（hMLP）stem，交替使用 MLP 层与 patch 聚合操作，**严格禁止 patch 间通信**，从而把掩码施加在预处理之后仍然成立，兼容 BeiT。原文还发现现有卷积 stem 与 BeiT 结合并不奏效，而 hMLP 在有监督设置下与对比中最佳的卷积 stem 持平。

## 方法

### 整体框架
本文在标准 ViT（Dosovitskiy 的原始设计，外加 Touvron 等提出的小模型 ViT-Ti/ViT-S）基础上，提出三种**相互独立、可组合**的改进策略，均围绕 ViT 的两个基本构建块——多头自注意力（MHSA）残差块和前馈网络（FFN）残差块——展开重组或选择性训练。所有模型均用 16×16 patch、class-token pooling，默认 224×224 输入。

### 关键模块与机制
#### 1. 并行 ViT (Parallel ViT)
- **机制**：把顺序处理的两层 Transformer 块重组为并行结构，"成对"打平。
- **数学公式**（取自原文式 (1)/(2)）：
  - 顺序处理：`x'_{l+1}=x_l+mhsa_l(x_l)`，`x_{l+1}=x'_{l+1}+ffn_l(x'_{l+1})`；`x'_{l+2}=x_{l+1}+mhsa_{l+1}(x_{l+1})`，`x_{l+2}=x'_{l+2}+ffn_{l+1}(x'_{l+2})`。
  - 并行处理：`x_{l+1}=x_l+mhsa_{l,1}(x_l)+mhsa_{l,2}(x_l)`；`x_{l+2}=x_{l+1}+ffn_{l,1}(x_{l+1})+ffn_{l,2}(x_{l+1})`。
  - 直观解释（原文给出）：随网络变深，任一残差块 `r(·)` 对整体函数的贡献越来越小，近似 `r'(x+r(x))≈r'(x)` 越来越成立；可验证在该近似下式 (1) 与式 (2) 等价。这把层数减半、并行处理量翻倍。
- **可扩展性**：并行分支数不限于 2，分支数为 1 时即退化回顺序设计。
- **与已有方法的差异**：不同于直接增大工作维度 d（会让参数和 FLOPs 随宽度二次增长、推理峰值显存也二次增长），并行化对参数和计算量**完全中性**；是否真正并行只影响推理峰值显存与延迟。

#### 2. 选择性微调（仅调 MHSA）
- **机制**：微调时只更新 MHSA 层权重，冻结 FFN 层（来自预训练）。原文明确该选择显著优于反向做法（只调参数更重的 FFN）。
- **适用场景**：(a) 低分辨率预训练 → 高分辨率（如 224→384）微调，可减小训练/测试因数据增强带来的尺度差异；(b) 迁移到其他分类数据集。
- **直观解释**：MHSA 负责 token 间依赖与全局上下文，分辨率/任务改变时需调整；FFN 是逐 token 的独立非线性变换，预训练后相对稳定，可跨任务复用。原文将其与 adapter 类参数高效微调方法并列对照，但本文选择直接微调原版 ViT 的注意力层。

#### 3. hMLP Patch 预处理 stem
- **动机**：Transformer 前几层感受野相对局部、行为近似卷积；混合架构常用卷积 stem 提升精度和训练稳定性。但卷积 stem 会跨 patch 传播信息，与 BeiT/MAE 掩码不兼容。
- **设计**：分层 MLP stem 交替"MLP 层（逐 token 独立变换）+ patch 聚合（缩短序列/降分辨率）"，并**禁止任何 patch 间通信**，使每个输出 token 只依赖原图的一个局部区域。
- **训练方式**：自监督时先过 hMLP stem 得到 patch 序列，再在序列上做随机掩码、送入 Transformer 重建。原文做法是在 patch 预处理之后再施加掩码，从而让掩码自监督与 stem 共存。

## 实验

### 数据集
- 主数据集：**ImageNet-1k**（训练 + 验证）。
- 独立测试集：**ImageNet-V2**（matched frequency），提供互补视角。
- 迁移学习：**六个较小数据集**（摘要明确提及"six smaller datasets"；具体名称在提取覆盖的前 12 页未列出，原文后续/附录可能给出，待核）。

### 基线与训练设置
- 基线模型（Table 1，均 16×16 patch、224×224、ImageNet-1k val top-1）：ViT-Ti/16（depth 12, width 192, 3 heads, 5.7M 参数, 1.3G FLOPs, 3796 im/s；300ep 72.7 / 400ep+LS 73.5）、ViT-S/16（22.1M, 4.6G, 1827 im/s；79.7 / 80.7）、ViT-B/16（86.6M, 17.6G, 799 im/s；82.2 / 82.7）、ViT-L/16（depth 24, width 1024, 16 heads, 304.4M, 61.6G, 277 im/s；83.0 / 84.0）。
- 训练流程：采用 Wightman 等的 **A2 流程**（**二元交叉熵损失** BCE，固定多数超参），并针对 ViT 做改动：学习率 ViT-Ti/S 用 `lr=4e-3`、ViT-B/L 用 `lr=3e-3`；随机深度 drop-rate `sd` 按模型设 `0`(Ti)/`0.05`(S)/`0.1`(B)/`0.4`(L)；大模型用 **LayerScale (LS)** 并配更长训练。两套基线：300 epochs 无 LS，以及 400 epochs + LS。所有实验 seed=0。

### 评价指标
- 精度：ImageNet-1k val 与 ImageNet-V2 的 Top-1。
- 效率：参数量、FLOPs、推理速度 (im/s)、推理峰值显存 (MB)。

### 主实验结果
- **并行 vs 顺序（Figure 1/2/3, Table 2/3）**：
  - 给定固定总块数（如 36 = 36×1 / 18×2 / 12×3 / 9×4），**两条并行分支在所有测试容量下最佳**；超过两条分支在精度上一般不划算。
  - 在 36/60 块这种"较深、顺序版难优化"的区间，并行（×2）更易训练且足够深以受益于层组合性。在仅 24 块、变宽度时（Figure 2），小模型 ViT-Ti/ViT-S 的顺序版更好（24 层易优化），B24×1 与 B12×2 相当，而 ViT-L12×2 强于其顺序版（顺序 L 即便用 LS 也更难优化；不用 LS 时 300ep 仅 83%）。
  - 配合 LayerScale 后（Table 2），ViT-B36×1（顺序）与 ViT-B18×2（并行）在 400ep+LS 下 ImageNet-val 均为 **84.1%**（v2 分别 73.9 / 73.5）——即"足够大且优化得当时，顺序与并行大致等价"。
- **增加块数 vs 增大工作维度（Table 3，均用 LS）**：在参数/FLOPs 近似对齐下，顺序与并行模型精度都**明显高于**单纯增大工作维度 d 的模型，且后者推理峰值显存更高。36 块时顺序与并行相当；48 块时并行更优（因顺序版深度更大更难优化）。例如 B36×1 与 B18×2 同为 256.7M 参数 / 52.5G FLOPs，val 83.9 / 83.8。
- **选择性微调（Table 5，224→384）**：**仅微调 MHSA** 的精度与全参数微调在 ImageNet-val 和 V2 上差异都在标准差 **±0.1** 内；而只微调 FFN（参数量是 MHSA 两倍）则做不到这一点。预训练模型已训练 400 epochs 以确保收敛。*(Table 5 的具体数值落在提取缓存覆盖的 12 页之外，待核)*
- **hMLP stem（第 5 节，Table 7 / Figure 6）**：在 BeiT 自监督框架下 hMLP stem 优于卷积 stem；有监督设置下与最佳卷积 stem 持平。*(据原文后续页 p.13 线索，提取缓存未覆盖完整数值，待核)*

### 效率分析
- **并行化吞吐（Table 4，V100，im/s）**：并行 ViT 的残差块既可顺序也可并行执行。增益集中在**小 batch**：ViT-S18×2 在 batch=1 时由 44→61（+38%），ViT-B18×2 由 42→61（+45%）；batch 增大后增益逐步消失，B18×2 在 batch≥8、S18×2 在 batch≥16 时并行实现已不快于顺序（best gain=0%）。原文指出当前是缺少专用 CUDA kernel 的朴素实现，要在吞吐上拿到稳定收益需专门的硬件或 kernel。
- **选择性微调**：冻结约占参数 2/3 的 FFN，大幅减少可训练参数、计算与训练峰值显存。
- **参数/计算对比**：并行模型与同深度顺序模型参数量、FLOPs 完全一致（Table 3）。

### 消融与泛化
- **消融**：并行分支数 1/2/3/4 对精度的影响（Figure 1）——两条分支是最优平衡点。
- **泛化**：把"仅调 MHSA"用于六个较小数据集的迁移分类，发现对大模型（ViT-L）精度损失有限。

## 局限

1. **方法适用边界**：并行 ViT 的优势集中在**深层、高容量**模型；中小模型（≤24 层）顺序结构往往更好也更易优化。
2. **任务/方法覆盖**：
   - 迁移实验只测**分类**，未涉及检测、分割等更复杂下游任务。
   - 自监督只围绕 **BeiT**，未验证与 MAE 等其他掩码方法的兼容性。
   - 速度增益强依赖实现与硬件——朴素实现仅在小 batch 有增益，大 batch 增益消失甚至变慢，需要定制 CUDA kernel 才能充分发挥并行性。
3. **数据局限**：核心实验基于 ImageNet-1k 及其变体，更广领域（医学、遥感等）的泛化性待验证。
4. **理论分析较浅**：并行化的有效性依赖直觉（深层残差块贡献变小的近似）与实验，缺乏更深入的理论保证。

## 个人评论

这篇论文的价值在于**简洁性与实用性**：不堆新模块，而是揭示三条基于标准 ViT、即插即用的改进洞察，对研究和工程都有直接启发。
1. **对架构研究的启发**：并行化提供了一种在**不增加参数/FLOPs** 的前提下改变网络"形状"（更宽更浅）的视角，把"深度 vs 宽度"的老问题重新带回 ViT 语境；后续 ViT-22B 等大模型采用并行 attention/MLP 也印证了这条思路的可扩展性。
2. **对高效适配的启发**：**只调注意力**是极简的参数高效微调——比 adapter 更直接，且天然支持"共享一份 FFN、按任务换一份注意力"的多任务部署模式。值得注意的是它的结论方向（调 MHSA 优于调 FFN）本身就有信息量，可作为后续"哪些层该解冻"研究的先验。
3. **对实验方法的启发**：论文反复强调对齐参数量与 FLOPs 再比较（否则并行 vs 增宽的对比不公平），这是架构论文容易踩的坑。
4. **对自监督的启发**：hMLP stem 的"禁止 patch 间通信"原则，给"如何把卷积式归纳偏置引入 Transformer 而不破坏掩码自监督"提供了一个清晰范式。

### 使用建议
- **快速了解**：读摘要 + 引言的三点编号 + 第 3/4/5 节开头总结段 + 结论，即可抓住三个贡献。
- **复现实验**：精读第 2.2 节训练设置（A2 流程、BCE、各模型 lr / sd / 是否 LS、seed=0）与第 3.3/4/5 节实验细节。
- **借鉴创新点**：改效率→第 3 节并行化；省微调→第 4 节只调注意力；做掩码自监督→第 5 节 hMLP stem。
- **写 Related Work**：可归入"视觉 Transformer 架构优化 / 高效 Transformer / Transformer 迁移与微调 / 自监督视觉 Transformer"。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉领域的 **Vision Transformer (ViT) 架构与训练优化** 方向。它不提出新网络，而是围绕 ViT 的两个基本残差块（MHSA、FFN）给出三条独立、易实现的改进：层并行化、仅微调注意力、禁止 patch 间通信的 hMLP stem。其中并行化（成对重组 MHSA/FFN）和"调注意力即可"两点都直接作用于注意力算子的组织与训练方式，因此归入 **B_注意力算子模块** 主题是贴切的——它是研究 Transformer 注意力机制效率与实用性的高质量参考。作者团队即 DeiT/LayerScale/CaiT 的同一支 Meta AI + Sorbonne + Inria 团队。

## 2. 一句话总结
本文给出三条简单却有效的 ViT 改进洞见：成对残差块可并行（参数/算力不变、更宽更浅）、跨分辨率/跨任务只需微调注意力层、用禁止 patch 间通信的 hMLP stem 让掩码自监督与 patch 预处理兼容。

## 3. 背景与问题
- **为什么要做**：ViT 是 Transformer 在视觉上的极简搬运，单层即有完整感受野和并行性；但其设计与训练流程被探索得很有限，仍有简单改进空间。
- **之前方法的问题**：
  1. 顺序层结构在很深时优化受阻（即便有残差连接，过深仍妨碍优化，需 LayerScale 之类技巧）。
  2. 跨分辨率/下游任务需全参数微调，算力与峰值显存高，参数主体无法跨任务复用。
  3. 卷积 stem 会跨 patch 传播信息，破坏 BeiT/MAE 掩码预测所需的 patch 独立性。
- **核心矛盾**：在不明显损精度的前提下，分别从并行化、选择性微调、兼容掩码自监督三条独立路径改进 ViT。

## 4. 核心贡献
1. **并行 ViT**：把成对 (MHSA, FFN) 块从顺序重组为并行，得到参数量/FLOPs 完全不变、更宽更浅的网络；比 Non-deep Networks 等更简单，直接构建在标准 ViT 之上，分支数可任意（=1 即退化为顺序）。
2. **微调注意力足矣**：跨分辨率微调时只调 MHSA 与全微调差异在 ±0.1 标准差内，远优于只调参数更重的 FFN；对大模型跨任务迁移精度损失也有限。冻结占参数主体的 FFN 可省算力/显存并跨任务共享。
3. **hMLP stem**：交替 MLP 层与 patch 聚合、禁止 patch 间通信，使掩码可施加在预处理之后，兼容 BeiT；现有卷积 stem 与 BeiT 结合无效，而 hMLP 有监督下与最佳卷积 stem 持平。

## 5. 方法详解
### 整体框架
在标准 ViT（Dosovitskiy 原版 + Touvron 的 ViT-Ti/S）上提出三种相互独立、可组合的改进，均针对 MHSA / FFN 两个构建块。统一用 16×16 patch、class-token pooling、默认 224×224。

### 关键模块与机制
#### 1. 并行 ViT
- 顺序（式 1）：`x'_{l+1}=x_l+mhsa_l(x_l)`，`x_{l+1}=x'_{l+1}+ffn_l(x'_{l+1})`；`x'_{l+2}=x_{l+1}+mhsa_{l+1}(x_{l+1})`，`x_{l+2}=x'_{l+2}+ffn_{l+1}(x'_{l+2})`。
- 并行（式 2）：`x_{l+1}=x_l+mhsa_{l,1}(x_l)+mhsa_{l,2}(x_l)`；`x_{l+2}=x_{l+1}+ffn_{l,1}(x_{l+1})+ffn_{l,2}(x_{l+1})`。
- 直观：深层时残差块贡献变小，近似 `r'(x+r(x))≈r'(x)` 越成立，此近似下式 (1)、(2) 等价。层数减半、并行量翻倍；分支数可任意。
- 与增宽的差异：增大工作维度 d 使参数/FLOPs/峰值显存随宽度二次增长，而并行化对参数和计算量中性，只改变（在真正并行执行时的）峰值显存与延迟。

#### 2. 选择性微调（仅调 MHSA）
- 只更新 MHSA、冻结 FFN（来自预训练），显著优于反向只调 FFN。
- 适用：低→高分辨率（224→384，缩小训练/测试尺度差异）与跨分类任务迁移。
- 直观：MHSA 管 token 间依赖与全局上下文，需随分辨率/任务调整；FFN 是逐 token 独立非线性，预训练后稳定可复用。与 adapter 类方法并列对照，但本文直接调原版 ViT 的注意力。

#### 3. hMLP stem
- 动机：Transformer 前几层近似卷积、局部；卷积 stem 提精度但跨 patch 传播信息，与掩码自监督不兼容。
- 设计：交替"MLP 层（逐 token）+ patch 聚合（缩短序列）"，禁止 patch 间通信，每个输出 token 只依赖一个局部区域。
- 训练：先过 stem 得 patch 序列，再随机掩码、送 Transformer 重建（掩码施加在预处理之后）。

## 6. 实验与结果
### 数据集
- 主：ImageNet-1k（训练+验证）；独立测试：ImageNet-V2 (matched frequency)；迁移：六个较小数据集（具体名称在前 12 页未列出，待核）。

### 基线与训练设置（Table 1 + 2.2 节）
- ViT-Ti/16: 12 层 / 宽 192 / 3 头 / 5.7M / 1.3G / 3796 im/s；72.7(300ep) / 73.5(400ep+LS)。
- ViT-S/16: 12 / 384 / 6 / 22.1M / 4.6G / 1827；79.7 / 80.7。
- ViT-B/16: 12 / 768 / 12 / 86.6M / 17.6G / 799；82.2 / 82.7。
- ViT-L/16: 24 / 1024 / 16 / 304.4M / 61.6G / 277；83.0 / 84.0。
- 训练：Wightman A2 流程 + 二元交叉熵；`lr=4e-3`(Ti/S)、`3e-3`(B/L)；`sd=0/0.05/0.1/0.4`(Ti/S/B/L)；大模型用 LayerScale；两套基线 300ep(无LS) 与 400ep+LS；seed=0。

### 评价指标
- 精度：ImageNet-val / V2 Top-1。效率：参数、FLOPs、im/s、峰值显存(MB)。

### 主实验结果
- **并行 vs 顺序**：固定总块数下两条并行分支在所有容量下最优；>2 分支不划算。深（36/60 块）区间并行更易训且足够深；24 块时小模型（Ti/S）顺序更好，B24×1≈B12×2，L12×2 强于顺序 L（顺序 L 即便 LS 也难优化，不用 LS 时 300ep 仅 83%）。加 LS 后（Table 2）B36×1 与 B18×2 在 400ep+LS 均 84.1(val)（v2: 73.9 / 73.5）——大模型且优化得当时顺序≈并行。
- **增块数 vs 增宽（Table 3, 均 LS）**：参数/FLOPs 近似对齐下，顺序与并行都明显优于增大工作维度 d 的模型（后者峰值显存更高）；36 块顺序≈并行，48 块并行更优。B36×1 与 B18×2 同为 256.7M / 52.5G，val 83.9 / 83.8。
- **选择性微调（Table 5, 224→384）**：仅调 MHSA 与全微调差异在 ±0.1 标准差内（val 与 V2 皆是），只调 FFN 做不到；预训练已 400ep 确保收敛。*(Table 5 具体数值在 12 页提取范围之外，待核)*
- **hMLP stem（第 5 节，p.13 Table 7 / Figure 6）**：BeiT 框架下 hMLP 优于卷积 stem；有监督下与最佳卷积 stem 持平。*(据原文后续页线索，提取缓存未覆盖完整数值，待核)*

### 效率分析
- **吞吐（Table 4, V100, im/s）**：增益集中在小 batch——batch=1 时 S18×2 44→61(+38%)、B18×2 42→61(+45%)；随 batch 增大增益递减，B18×2 在 batch≥8、S18×2 在 batch≥16 已无增益（best gain=0）。朴素实现缺专用 CUDA kernel，需定制硬件/kernel 才有稳定吞吐收益。
- **选择性微调**：冻结约占参数 2/3 的 FFN，大减可训练参数/算力/训练峰值显存。
- **参数/计算**：并行与同深度顺序完全一致。

### 消融与泛化
- 消融：并行分支数 1/2/3/4（Figure 1），两条分支最优。
- 泛化：仅调 MHSA 用于六个小数据集迁移，大模型 ViT-L 精度损失有限。

## 7. 这篇论文真正有价值的地方
价值在于**简洁性与实用性**，三条洞见都即插即用：
1. **架构研究**：并行化在不增参数/FLOPs 下改变网络形状（更宽更浅），把"深度 vs 宽度"重新带回 ViT；后续超大模型采用并行 attention/MLP 也印证了其可扩展性。
2. **高效适配**："只调注意力"比 adapter 更直接，并支持"共享 FFN、按任务换注意力"的多任务部署；其"调 MHSA 优于调 FFN"的方向性结论本身就有信息量。
3. **实验方法**：强调对齐参数量与 FLOPs 再比较，否则并行 vs 增宽的对比不公平。
4. **自监督**：hMLP 的"禁止 patch 间通信"为把卷积式归纳偏置引入 Transformer 而不破坏掩码自监督提供清晰范式。

## 8. 局限与问题
1. 并行 ViT 优势集中在深层高容量模型，中小模型顺序更优。
2. 迁移只测分类（未测检测/分割）；自监督只围绕 BeiT（未验证 MAE 等）；速度增益强依赖实现与硬件，大 batch 增益消失甚至变慢，需定制 CUDA kernel。
3. 核心实验限于 ImageNet 系，更广领域泛化待验证。
4. 并行化有效性靠直觉近似与实验，缺乏深入理论。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言三点编号 + 第 3/4/5 节开头 + 结论。
- **复现**：第 2.2 节（A2 流程、BCE、各模型 lr/sd/是否 LS、seed=0）与第 3.3/4/5 节细节。
- **借鉴**：改效率→并行化（第 3 节）；省微调→只调注意力（第 4 节）；掩码自监督→hMLP stem（第 5 节）。
- **写 Related Work**：视觉 Transformer 架构优化 / 高效 Transformer / Transformer 迁移与微调 / 自监督视觉 Transformer。

## 10. 和其他论文的关系
- [[ViT (Dosovitskiy et al., 2020)]]：基线架构（原文 [16]）。
- [[DeiT (Touvron et al., 2021)]]：同团队前作，提供 ViT-Ti/S 与训练经验。
- [[LayerScale / CaiT (Touvron et al., 2021)]]：原文 [64]，稳定大/深模型训练的关键技术，并行实验大量依赖它。
- [[Wightman et al. (2021) A2 训练程序]]：原文 [69]，本文基线训练流程（BCE 损失）。
- [[BeiT (Bao et al., 2021)]]：原文 [3]，hMLP stem 所兼容/改进的掩码自监督框架。
- [[MAE (He et al., 2022)]]：原文 [24]，另一种掩码自监督；本文方法思路相关但未实验验证。
- [[Non-deep Networks (Goyal et al., 2021)]]：原文 [20]，更复杂的并行分支设计，本文作为对照提出更简单的方案。

## 11. 关键词
视觉 Transformer (ViT), 并行残差块, 深度 vs 宽度, 选择性微调, MHSA, FFN, LayerScale, A2 训练流程, 掩码自监督, BeiT, hMLP stem, patch 预处理, 计算效率, 峰值显存, 参数共享, ImageNet, ImageNet-V2, 迁移学习

## 12. 可信度说明
本笔记顶部各节与精读 1-12 节的事实，均以提取缓存覆盖的 PDF **前 12 页（共 22 页）** 为唯一依据，已逐条对照原文核验：摘要、引言三点、第 2 节背景与训练设置（含 Table 1 全部数值、A2/BCE/lr/sd/LS/seed）、第 3 节并行 ViT 全文（式 1/2、Figure 1-3、Table 2-4 数值）、第 4 节"只调注意力"前半部分（含"±0.1 标准差内"结论）均直接摘自文本。

**提取缓存未覆盖**（前 12 页之后，标注"待核"）：Table 5 的具体微调数值；第 5 节 hMLP stem 的完整实验与 Table 7 / Figure 6 数值；六个迁移数据集的具体名称；结论与完整参考文献。涉及这些部分时，本笔记只复述提取文本/原文 p.13 线索中已有的概述，未编造数字。需要原笔记曾出现、但落在提取范围外的具体数（如 ViT-S 微调 84.4%/84.3%）已删除，因无法据提取文本核实。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 2086 字符/页); 来源缓存: `.paper-cache/extracts/Parallel ViT.txt` (提取覆盖 12/22 页, max_chars 截断在 25000 字符 ≈ 前 12 页; 原 AI 主体 12/22 + 全文补读 13-22 页章节线索); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-22; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-22。
- **提取情况**: 缺失页 10 页, 其中 10 页提取到可读文本。缺失页包含正文/附录内容, 其中约 6 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Figure 6: Performance of patch pre-processing in the
- p.13: Results with BeiT training. We report the results with BeiT, fine-tuned on ImageNet-
- p.14: 6 Conclusion
- p.14: First, we investigated a simple but effective way to parallelize them, showing a
- p.14: Last, we introduced a simple patch pre-processing stem, which processes patches
- p.15: References
- p.15: Conference on Computer Vision (2019)
- p.15: Computer Vision (2020)
- p.15: ConViT: Improving vision transformers with soft convolutional inductive bi-
- p.15: Recognition (2021)
- p.16: International Conference on Learning Representations (2021)
- p.17: Computer Vision and Pattern Recognition (2019)

### 缺失页关键摘录

- p.13: Table 7: Patch pre-processing: Performance in top1 accuracy with for a ViT-B12. All models are (1)
- p.13: when used with BeiT. We report the result of a ViT-B13 to provide the performance of a vanilla trans-
- p.13: former with more FLOPS. We measure the standard deviation for the two linear stem baselines and our
- p.13: Figure 6: Performance of patch pre-processing in the
- p.13: plexity (+0.8% FLOPS compared to the ViT-B12 in
- p.13: lar number of FLOPS. Our hMLP stem obtains a comparable performance but with
- p.13: val, in the right-most column of Table 7. We use the code of BeiT [3] with their
- p.13: effective and provides an improvement of +0.3/+0.4 top1 accuracy compared to
- p.13: est of hMLP in the context of masked self-supervised learning is clear in Figure 6,
- p.14: tuning large models or/and transferring to a dataset with few training images.
- p.16: P ., Belongie, S.J.: The inaturalist challenge 2017 dataset. arXiv preprint
- p.21: Table 8: Comparison our baseline with previous training procedures. We only include results that
<!-- AI_READING_NOTE_END -->
