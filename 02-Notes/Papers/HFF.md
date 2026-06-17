---
title: "HiFuse: Hierarchical multi-scale feature fusion network for medical image classification"
authors:
  - "Xiangzuo Huo"
  - "Gang Sun"
  - "Shengwei Tian"
  - "Yan Wang"
  - "Long Yu"
  - "Jun Long"
  - "Wendong Zhang"
  - "Aolun Li"
year: 2024
venue: "Biomedical Signal Processing and Control"
doi: 10.1016/j.bspc.2023.105534
pdf: [[HFF.pdf]]
primary_topic: A2_医学图像_分类_配准_生成
topics:
  - "A2_医学图像_分类_配准_生成"
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
extract_cache: .paper-cache/extracts/HFF.txt
---

# HiFuse: Hierarchical multi-scale feature fusion network for medical image classification

## 基本信息
- **PDF**: [[HFF.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`, `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | HiFuse: Hierarchical multi-scale feature fusion network for medical image classification |
| **作者** | Xiangzuo Huo; Gang Sun; Shengwei Tian; Yan Wang; Long Yu; Jun Long; Wendong Zhang; Aolun Li |
| **发表时间** | 2024（在线 2023-09-30；收稿 2023-02-24，修回 2023-08-15，录用 2023-09-24） |
| **刊物/会议** | Biomedical Signal Processing and Control, 87 (2024) 105534 |
| **DOI** | 10.1016/j.bspc.2023.105534 |
| **开源代码** | https://github.com/huoxiangzuo/HiFuse |

## 摘要

> 来源: 据 PDF 提取文本整理。

**英文原文（清理后）**:
Effective fusion of global and local multi-scale features is crucial for medical image classification. Medical images have many noisy, scattered features, intra-class variations, and inter-class similarities. Many studies have shown that global and local features are helpful to reduce noise interference in medical images. It is difficult to capture the global features of images due to the fixed size of the receptive domain of the convolution kernel. Although the self-attention-based Transformer can model long-range dependencies, it has high computational complexity and lacks local inductive bias. In this paper, we propose a three-branch hierarchical multi-scale feature fusion network structure termed as HiFuse, which can fuse multi-scale global and local features without destroying the respective modeling, thus improving the classification accuracy of various medical images. There are two key characteristics: (i) a parallel hierarchical structure consisting of global and local feature blocks; (ii) an adaptive hierarchical feature fusion block (HFF block) and inverted residual multi-layer perceptron (IRMLP). The advantage of this network structure lies in that the resulting representation is semantically richer and the local features and global representations can be effectively extracted at different semantic scales. Our proposed model's ACC and F1 values reached 85.85% and 75.32% on the ISIC2018 dataset, 86.12% and 86.13% on the Kvasir dataset, 76.88% and 76.31% on the Covid-19 dataset, 92.31% and 88.81% on the esophageal cancer pathology dataset. The HiFuse model performs the best compared to other advanced models. Our code is open source and available from https://github.com/huoxiangzuo/HiFuse.

**中文翻译**:
全局与局部多尺度特征的有效融合对医学图像分类至关重要。医学图像往往含有大量噪声、特征散在、类内差异大、类间相似度高；已有研究表明，全局与局部特征都有助于抑制医学图像中的噪声干扰。由于卷积核感受野大小固定，难以捕获图像的全局特征；而基于自注意力的 Transformer 虽能建模长距离依赖，却计算复杂度高且缺乏局部归纳偏置。本文提出一种三分支层次化多尺度特征融合网络 HiFuse，它能在不破坏各自建模的前提下融合多尺度的全局与局部特征，从而提升各类医学图像的分类精度。其两个关键特性是：(i) 由全局特征块与局部特征块构成的并行层次化结构；(ii) 一个自适应层次特征融合块（HFF block）以及反转残差多层感知机（IRMLP）。该结构的优势在于所得表征语义更丰富，且能在不同语义尺度上有效提取局部特征与全局表示。模型在 ISIC2018 上 ACC/F1 达 85.85%/75.32%，Kvasir 上达 86.12%/86.13%，Covid-19 上达 76.88%/76.31%，食管癌病理数据集上达 92.31%/88.81%，整体优于其他先进模型。代码已开源。

## 研究背景与动机

- **为什么做**：医学图像分类是计算机辅助诊断、医学图像检索与挖掘中的关键任务。由于成像模态与临床病理的高相似度和细节多样性，医学图像呈现显著的**类内差异大、类间相似度高**、且**噪声多、特征散在**，因此需要引入全局语义信息来提升性能。
- **之前方法的问题**：
    1.  **CNN/DCNN**：卷积核**感受野大小固定**，难以捕获图像的全局特征，无法收集足够的上下文信息。
    2.  **Transformer/ViT**：虽能建模长距离依赖与全局语义，但**计算复杂度高**，且**缺乏局部归纳偏置**，常忽略局部特征细节（弱局部特征时难以区分目标与背景），并影响模型收敛速度与性能。
    3.  **已有 CNN-Transformer 融合方法**（如 ViTAE、StoHisNet、TransFuse、CMT、Conformer、Focal 等）在 ImageNet 等自然图像与下游任务上表现良好，但**应用到医学图像领域时效果不理想**——因为医学图像数据不足、病理特征比普通图像更散在、更难发现。
- **核心矛盾**：需要设计一种能**并行、互不干扰**地分别提取全局与局部特征，并在**不同层次上自适应融合**的通用骨干网络，同时保持相对较低的计算复杂度。作者认为一个好的分类模型应具备四个特征：(i) 鲁棒的骨干网络，(ii) 多尺度全局与局部特征融合，(iii) 注意力机制，(iv) 相对低的计算复杂度。
- **定位**：与 TransFuse、GasHis Transformer、Medical Transformer 等"为分割/检测等特定下游任务设计"的工作不同，本文目标是设计一个**通用的医学特征提取骨干**，强调在编码器侧高效提取并融合全局–局部特征，让并行分支保持各自建模而不引入新噪声。

## 关键贡献

1.  **提出 HiFuse 网络框架**：结合并优化"好分类模型应具备的特征"，提出一个**三分支并行层次化融合结构**。全局特征块（基于 Swin-Transformer 的 W-MSA/SW-MSA）与局部特征块（基于深度卷积）分别在不同尺度上高效提取全局语义信息与局部空间特征，并行设计使两类特征互不干扰地建模。
2.  **提出自适应层次特征融合块（HFF block）**：在每个分支的不同尺度特征间有效融合语义信息。该块包含：
    - **空间注意力（SA）机制**：作用于局部特征，选择性增强重要区域、抑制无关信息。
    - **通道注意力（CA）机制**：作用于全局特征，利用通道图间的相互依赖改进特定语义的特征表示。
    - **反转残差多层感知机（IRMLP）**：对融合特征做非线性变换，补偿被去掉的 FFN。
    - **捷径连接（shortcut）**：引入上一层 HFF 块的输出信息。
3.  **在多个医学数据集上验证有效性**：在 ISIC2018（皮肤病变）、Kvasir（胃肠道）、Covid-19-CT（胸部 CT）和食管癌病理数据集上均取得优于现有先进模型的分类结果；其中 HiFuse-T 在参数量相近的情况下，仅用约 1/3 的计算成本（8.13 GFLOPs vs. Conformer-base-p16 的 22.89 GFLOPs）即超过 Conformer-base-p16。

## 方法

- **整体框架**（图 1）：HiFuse 由一个 **Stem 层**和**四个阶段（Stage）**组成。每个阶段包含**并行的局部特征块、全局特征块和一个 HFF 融合块**。全局分支通过 patch merging 下采样，局部分支通过步长 2、卷积核 2 的卷积下采样；特征经四个阶段逐步下采样并融合，最终送入**全局平均池化 + LayerNorm 的线性分类器**输出分类结果。
- **输入输出**：输入为医学图像，输出为分类标签。
- **关键模块详解**：
    1.  **Stem**：用一个**步长 4、核 4×4 的卷积**将图像切成 4×4 的 patch，分辨率降至 1/4（H×W 由 224 降到 56×56）。之后全局路径经**线性嵌入**、局部路径经 **LayerNorm** 分别进入两个分支。
    2.  **全局特征块**：引入 Swin-Transformer 的**窗口多头自注意力 W-MSA** 与**移位窗口 SW-MSA**。W-MSA 把特征图划分为 M×M 窗口后逐窗自注意，计算复杂度由公式(1)给出：MSA 为 4hwC²+2(hw)²C，W-MSA 为 4hwC²+2M²hwC，显著降低二次项开销。**关键设计**：作者**去掉常规自注意力后接的 FFN**，仅用 W-MSA + GELU 做非线性变换，把被省略的非线性变换**补偿到 HFF 块**中以进一步降低计算量；每个模块后加残差连接、使用相对位置偏置（rel. pos.），下一模块引入 Shift W-MSA。过程见公式(2)。
    3.  **局部特征块**：使用 **3×3 深度卷积（depthwise convolution）**——分组卷积的特例，分组数等于通道数——提取局部空间特征，有效降低 FLOPs；随后经线性层做跨通道信息交互，并加残差连接，过程见公式(3)。（注：原文为 depthwise convolution，非 depthwise separable，特此修正。）
    4.  **HFF 块（核心融合机制）**（图 2，公式(4)）：
        - 接收三个输入：当前层全局特征 `G_i`、局部特征 `L_i` 和**上一层 HFF 块输出** `F_{i-1}`。
        - **注意力选择**：`Ĝ_i = CA(G_i) ⊗ G_i`（全局特征过**通道注意力**），`L̂_i = SA(L_i) ⊗ L_i`（局部特征过**空间注意力**），⊗ 为逐元素相乘。
        - **前层特征下采样**：`F̃_i = Avgpool(f_{1×1}(F_{i-1}))`。
        - **跨支拼接**：`F̂_i = f_{1×1}(Concat[G_i, L_i, F̃_i])`，得到全局–局部与前层融合的结果。
        - **最终融合**：`F_i = IRMLP(LN(Concat[Ĝ_i, L̂_i, F̂_i])) + F̃_i`，将三路注意力/融合结果拼接送入 IRMLP，并以 `F̃_i` 作残差。
    5.  **注意力实现**（公式(5)）：`CA(x) = σ(MLP(AvgPool(x)) + MLP(MaxPool(x)))`；`SA(x) = σ(f_{7×7}(Concat[AvgPool(x), MaxPool(x)]))`，σ 为 Sigmoid，f_{7×7} 为 7×7 卷积。
    6.  **IRMLP**（公式(6)，图 2）：`IRMLP(x) = f_{1×1}(f_{1×1}(f_{depth 3×3}(x) + x))`，即一个带残差的 3×3 深度卷积接两个 1×1 线性层，在扩张通道维上用 GELU 做非线性，**补偿被去掉的 FFN**，并在一定程度上防止梯度消失/爆炸与网络退化。
- **具体参数**（表 2）：四个阶段输出尺寸 56×56→28×28→14×14→7×7，通道 96→192→384→768；全局分支各阶段 W-MSA 窗口 **win 7×7**、注意力头数依次为 **3/6/12/24**、带相对位置与 SW-MSA。总参数 **82.49 M**，**FLOPs 8.13 G**。
- **三种变体**（按各阶段 block 数）：
    - HiFuse-Tiny: Block numbers = (2, 2, 2, 2)
    - HiFuse-Small: Block numbers = (2, 2, 6, 2)
    - HiFuse-Base: Block numbers = (2, 2, 18, 2)
- **与已有方法的差异**：
    - **并行而非串行**：并行分支提取特征，使全局与局部分支互不干扰、不在提取阶段引入新噪声（区别于串行的 CNN→Transformer 拼接）。
    - **层次化融合**：HFF 块在每个阶段的多个语义尺度上逐层融合，而非最后一次性融合。
    - **注意力分维度施加**：融合阶段对**全局特征施加通道注意力（CA）**、对**局部特征施加空间注意力（SA）**，有针对性地强化各自特征。
- **训练与推理流程**：具体训练超参数（优化器、学习率策略等）在提取缓存覆盖的前 6 页内未明确给出。

## 实验

- **数据集**（共四个）：
    1.  **ISIC2018**：皮肤病变诊断，**7 类**（黑素细胞痣、皮肤纤维瘤、黑色素瘤、光化性角化病、良性角化病、基底细胞癌、血管病变），**10,015 张**图像，原始 650×450，缩放至 **224×224**；按 Chen[23] 的划分方式，**70% 样本（7010 张）用于训练与验证**（提取缓存在此处截断，后续具体划分待核）。
    2.  **Kvasir**：胃肠道图像分类（前 6 页仅提及，详细划分未在提取覆盖范围内）。
    3.  **Covid-19-CT**：COVID-19 胸部 CT 图像分类（前 6 页仅提及，详细划分未在提取覆盖范围内）。
    4.  **食管癌病理数据集**（前 6 页仅提及，详细划分未在提取覆盖范围内）。
- **对比方法**：明确提及与 **Conformer-base-p16** 的效率/性能对比；相关工作中列举了 ViTAE、StoHisNet、TransFuse、CMT、Conformer、Focal、DeiT、T2T-ViT 等。
- **评价指标**：准确率（ACC）和 F1 分数（F1）。
- **主实验结果**（据摘要，均为 HiFuse 最佳）：
    - ISIC2018：ACC **85.85%**，F1 **75.32%**。
    - Kvasir：ACC **86.12%**，F1 **86.13%**。
    - Covid-19：ACC **76.88%**，F1 **76.31%**。
    - 食管癌病理数据集：ACC **92.31%**，F1 **88.81%**。
- **效率对比**：HiFuse-T（Tiny）计算成本 **8.13 GFLOPs**，约为 Conformer-base-p16（22.89 GFLOPs）的 **1/3**，在参数量相近的情况下性能更优；HiFuse 总参数量 **82.49 M**。
- **消融实验**：第 4 章正文声明"将在 ISIC2018 上进行一系列消融研究"，但**消融的具体设计与结果在提取缓存覆盖的前 6 页内未包含**（提取在第 6 页训练样本划分处截断，缓存未覆盖后续页面，待核）。
- **泛化实验**：前 6 页未明确描述跨数据集泛化实验。

## 局限

- **场景局限性**：方法定位为医学图像**分类**骨干，作者称其层次化设计对下游任务友好，但是否适用于检测、分割、配准等任务需进一步验证。
- **计算成本**：虽比 Conformer 等高效，但引入 Transformer 分支仍带来可观的计算量与参数量（**82.49 M / 8.13 GFLOPs**），在移动端或资源受限的临床设备上部署可能存在挑战。
- **数据集范围**：实验集中在皮肤病变、胃肠道、胸部 CT 和病理切片四种类型，对其他成像模态（如 MRI、超声、X 光）的泛化能力未在提取文本中体现。
- **实验完整性（提取受限）**：提取缓存只覆盖前 6 页且在训练样本划分处截断，**消融实验**的具体设计与结果未包含在内，无法据本笔记确认各组件（SA、CA、IRMLP、并行结构）的独立贡献。
- **复现风险**：虽已开源代码，但医学图像数据集常具隐私性与特殊性，完整复现需自行获取相关数据。

## 个人评论

1.  **融合范式清晰可借鉴**：提出"并行提取–层次化自适应融合"的范式。**并行不干扰**的设计理念，以及 HFF 块按特征来源**分维度施加不同注意力**（全局→通道注意力 CA，局部→空间注意力 SA）的做法，对设计其他多分支/多模态融合网络很有借鉴意义——它把"注意力应作用在哪个维度"和"特征语义角色"绑定，而非无差别堆叠注意力。
2.  **FFN 外移是一处巧思**：把全局块里常规的 FFN 去掉、只留 W-MSA + GELU，再用 HFF 中的 IRMLP 统一补偿非线性。这等于把"特征变换"从各分支抽出来集中到融合点，既省算力又让融合块承担更多表达职责，值得在做混合架构时参考。
3.  **模块化程度高**：HFF 块把通道注意力、空间注意力、IRMLP 与残差/捷径连接组合成一个功能完整的融合单元，接口清晰（三输入一输出），易于理解并插入其他网络。
4.  **需要警惕的点**：参数量 82.49 M 并不算小，"轻量"主要体现在 FLOPs 而非参数；且四个数据集的绝对精度（尤其 Covid-19 的 76.88%）并不高，更应理解为"在相同算力预算下相对最优"，而非分类问题已被解决。消融细节超出本提取范围，组件贡献需回原文核对。

### 使用建议

- **快速了解**：读**摘要**、引言的贡献四要素（鲁棒骨干 / 多尺度融合 / 注意力 / 低复杂度）、以及方法节的图 1、图 2 与公式(4)，即可掌握核心思想。
- **复现**：重点看 **GitHub 开源代码**（https://github.com/huoxiangzuo/HiFuse），结合第 3 节与**表 2 的具体参数**（通道 96/192/384/768、头数 3/6/12/24、win 7×7、block 数）复现网络；数据集需自行准备。
- **借鉴创新点**：三分支并行设计；HFF 块的**注意力分维度应用**（CA 用于全局、SA 用于局部）与 **IRMLP**；**逐层融合前层特征**的信息流动方式；以及**把 FFN 外移到融合块**的算力分配思路。
- **写 Related Work**：可归入"基于 Transformer 的医学图像分类"、"CNN-Transformer 混合架构"、"多尺度特征融合"等类别。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**计算机视觉 / 医学图像分析**下的**医学图像分类**方向，致力于解决医学图像中**全局语义与局部细节特征的有效融合**问题，目标是给出一个**通用的医学特征提取骨干网络**（而非面向某类下游任务的专用模型）。其方法核心是一个层次化的多分支特征融合架构与自适应融合块（HFF）。因此一级主题归入 **A2_医学图像_分类_配准_生成**；同时因为 HFF 块以通道/空间注意力为核心算子，与 **B_注意力算子模块** 高度相关，作为二级主题。

## 2. 一句话总结
本文提出三分支并行层次化多尺度特征融合网络 HiFuse：用 Swin 风格 W-MSA 的全局分支与深度卷积的局部分支并行提取特征，再用自适应层次特征融合块（HFF：全局走通道注意力、局部走空间注意力、经 IRMLP 融合并接力前层输出）在不同语义尺度上融合，从而提升医学图像分类精度。

## 3. 背景与问题
- **为什么做**：医学图像分类是计算机辅助诊断的关键任务；医学图像类内差异大、类间相似度高、噪声多、特征散在，需要全局语义 + 局部细节共同抑制噪声、提升分类精度。
- **之前方法的问题**：
    1.  **CNN**：感受野固定，难捕全局特征，上下文信息不足。
    2.  **Transformer/ViT**：能建模长距离依赖但计算复杂度高、缺局部归纳偏置，常忽略弱局部细节，影响收敛与性能。
    3.  **已有融合方法**（ViTAE / StoHisNet / TransFuse / CMT / Conformer / Focal 等）在自然图像上好，但医学领域因数据不足、病理特征更散在而效果不理想。
- **核心矛盾**：要并行且互不干扰地提取全局/局部特征，并在多个层次上自适应融合，同时算力可控。作者据此提出好模型的四要素：鲁棒骨干、多尺度全局–局部融合、注意力、低复杂度。

## 4. 核心贡献
1.  **HiFuse 框架**：三分支并行层次化结构；全局特征块（W-MSA/SW-MSA）与局部特征块（深度卷积）分别高效提取不同尺度的全局语义与局部空间特征，并行互不干扰。
2.  **自适应层次特征融合块（HFF block）**：含空间注意力（用于局部）、通道注意力（用于全局）、反转残差 MLP（IRMLP）和捷径连接，在不同尺度特征间有效融合语义。
3.  **实证有效**：ISIC2018 / Kvasir / Covid-19-CT / 食管癌病理四个数据集均优于先进模型；HiFuse-T 在参数量相近时仅用约 1/3 算力（8.13 vs 22.89 GFLOPs）即超过 Conformer-base-p16。

## 5. 方法详解
- **整体框架**（图 1）：Stem + 四个阶段，每阶段含并行的局部块、全局块、HFF 块；全局分支用 patch merging 下采样，局部分支用步长 2/核 2 卷积下采样；末端全局平均池化 + LayerNorm 线性分类。
- **Stem**：步长 4、核 4×4 卷积切 4×4 patch，分辨率降至 1/4（56×56）；全局路径过线性嵌入、局部路径过 LayerNorm。
- **全局特征块**：Swin 的 W-MSA + SW-MSA（公式(1)给出 MSA 与 W-MSA 复杂度对比，窗口化把二次项 2(hw)²C 降为 2M²hwC）；**去掉 FFN，仅 W-MSA + GELU 做非线性，非线性补偿移至 HFF**；带残差、相对位置偏置，下模块用 Shift W-MSA（公式(2)）。
- **局部特征块**：3×3 **深度卷积**（depthwise，分组数=通道数，降 FLOPs）+ 线性层跨通道交互 + 残差（公式(3)）。
- **HFF 块**（图 2，公式(4)）：`Ĝ_i=CA(G_i)⊗G_i`，`L̂_i=SA(L_i)⊗L_i`，`F̃_i=Avgpool(f_{1×1}(F_{i-1}))`，`F̂_i=f_{1×1}(Concat[G_i,L_i,F̃_i])`，`F_i=IRMLP(LN(Concat[Ĝ_i,L̂_i,F̂_i]))+F̃_i`。即全局走通道注意力、局部走空间注意力、前层输出下采样后接力，三路拼接经 IRMLP 融合并加残差。
- **注意力**（公式(5)）：CA=σ(MLP(AvgPool)+MLP(MaxPool))；SA=σ(f_{7×7}(Concat[AvgPool,MaxPool]))。
- **IRMLP**（公式(6)）：f_{1×1}(f_{1×1}(f_{depth 3×3}(x)+x))，补偿缺失的 FFN，缓解梯度消失/爆炸与退化。
- **参数**（表 2）：四阶段输出 56→28→14→7，通道 96/192/384/768，头数 3/6/12/24，窗口 7×7；总参数 82.49 M，FLOPs 8.13 G。
- **变体**：Tiny (2,2,2,2) / Small (2,2,6,2) / Base (2,2,18,2)。
- **训练设置**：提取缓存覆盖的前 6 页未给出具体超参。

## 6. 实验与结果
- **数据集**：ISIC2018（皮肤病变，7 类，10,015 张，原始 650×450→缩放 224×224，按 Chen[23] 划分，70%/7010 张用于训练验证，后续划分在提取截断处之后，待核）；Kvasir（胃肠道）、Covid-19-CT、食管癌病理（后三者前 6 页仅提及）。
- **对比方法**：明确对比 Conformer-base-p16；相关工作列举 ViTAE/StoHisNet/TransFuse/CMT/Conformer/Focal/DeiT/T2T-ViT 等。
- **指标**：ACC、F1。
- **主结果（据摘要）**：ISIC2018 85.85%/75.32%；Kvasir 86.12%/86.13%；Covid-19 76.88%/76.31%；食管癌病理 92.31%/88.81%，HiFuse 均最佳。
- **效率**：HiFuse-T 8.13 GFLOPs ≈ Conformer-base-p16（22.89 GFLOPs）的 1/3，参数量相近时更优；总参数 82.49 M。
- **消融**：第 4 章声明将在 ISIC2018 上做消融，但**提取缓存只到第 6 页训练划分处截断，消融细节未覆盖（待核）**。

## 7. 这篇论文真正有价值的地方
1.  **"并行提取–层次化自适应融合"范式**：并行分支互不干扰地建模，避免提取阶段引入噪声；HFF 在每阶段多尺度上逐层融合而非末端一次融合。
2.  **注意力与特征角色绑定**：对全局特征用通道注意力、对局部特征用空间注意力——把"注意力作用维度"与"特征语义来源"对应起来，是比无差别堆注意力更有原则的设计。
3.  **算力再分配**：去掉全局块 FFN、把非线性变换集中到 HFF 的 IRMLP，既省 FLOPs 又让融合块承担更多表达职责。
4.  **工程可用**：深度卷积降算力、模块化 HFF 块接口清晰，易于复用与移植。

## 8. 局限与问题
- **任务范围**：定位医学图像分类骨干，向检测/分割/配准迁移的效果待验证。
- **计算成本**：参数量 82.49 M 不小，"轻量"主要体现在 FLOPs；部署到资源受限临床设备有挑战。
- **数据模态**：实验限于皮肤/胃肠/胸部 CT/病理四类，MRI、超声、X 光等模态未覆盖。
- **绝对精度有限**：Covid-19 仅 76.88%，宜理解为同算力下相对最优而非问题已解决。
- **提取受限**：缓存只到第 6 页且在训练样本划分处截断，消融、完整对比表、讨论等需回原文核对，本笔记无法据提取确认组件独立贡献。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要 + 贡献四要素 + 图 1/图 2/公式(4)。
- **复现**：看 GitHub（huoxiangzuo/HiFuse），对照表 2 参数（通道 96/192/384/768、头数 3/6/12/24、win 7×7、各变体 block 数）复现，数据集自备。
- **借鉴创新点**：三分支并行；HFF 的注意力分维度应用（CA→全局、SA→局部）；IRMLP；前层特征接力的信息流；FFN 外移到融合块的算力分配思路。
- **写 Related Work**：归入"基于 Transformer 的医学图像分类""CNN-Transformer 混合架构""多尺度特征融合"。

## 10. 和其他论文的关系
- **Swin-Transformer [18]**：全局分支直接采用其 W-MSA/SW-MSA、相对位置偏置与 patch merging；并被列为灵感来源之一。
- **ResNet [16] / ConvNeXt [17]**：被列为灵感来源；图 3 将 ResNet、ConvNeXt、Swin-Transformer 与 HFF 的 block 设计做对比；局部分支的深度卷积设计与 ConvNeXt 现代化卷积思路一脉相承。
- **Conformer [15]**：重要对比基线（Conformer-base-p16），同为 CNN-Transformer 混合，但 HiFuse 强调并行与层次化融合、且算力仅其约 1/3。
- **TransFuse [13] / GasHis Transformer [40] / Medical Transformer [36]**：同为医学领域 CNN+Transformer 融合，但主要服务于分割/检测等下游任务；HiFuse 区别在于做**通用骨干**、并行不干扰地在编码器侧融合。
- **HIGF-Net [41]**：文中提到其层次化全局–局部融合可同时捕获高层语义与低层空间特征，与本文动机相近。

## 11. 关键词
医学图像分类, 特征融合, Swin-Transformer, CNN-Transformer 混合网络, 多尺度特征, 层次化融合, 通道注意力, 空间注意力, HiFuse, HFF 块, IRMLP, 并行三分支结构

## 12. 可信度说明
本精读笔记基于提取缓存覆盖的**前 6 页**（缓存上限 25000 字符，原文约 62369 字符，实际在第 6 页"训练样本 70%/7010 张"处截断）。已核对的内容包括：标题、作者与单位、摘要全部指标、引言四要素、相关工作脉络、方法详解（Stem、多阶段设计、全局块 W-MSA/SW-MSA 与去 FFN 设计、局部深度卷积块、HFF 块公式(4)、注意力公式(5)、IRMLP 公式(6)）、表 2 参数（82.49 M / 8.13 GFLOPs、通道与头数）、三种变体 block 数。**未被提取覆盖**的部分：消融实验的具体设计与结果、Kvasir/Covid-19/食管癌数据集的详细划分、完整对比表、讨论与结论——这些标注为"待核"。摘要中的四组 ACC/F1 直接来自提取文本的摘要原文。一处对原笔记的事实修正：局部块为 **depthwise convolution（深度卷积）**，非"深度可分离卷积"。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/HFF.txt` (前 6 页, 缓存上限 25000 字符截断, 后续页未覆盖); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
