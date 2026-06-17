---
title: "RegionViT: Regional-to-Local Attention for Vision Transformers"
authors:
  - "Chun-Fu (Richard) Chen"
  - "Rameswar Panda"
  - "Quanfu Fan"
year: 2022
venue: "ICLR 2022"
doi: 
pdf: [[regionvit.pdf]]
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
extract_cache: .paper-cache/extracts/regionvit.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/19 pages"
---
# RegionViT: Regional-to-Local Attention for Vision Transformers

## 基本信息
- **PDF**: [[regionvit.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | RegionViT: Regional-to-Local Attention for Vision Transformers |
| **作者** | Chun-Fu (Richard) Chen; Rameswar Panda; Quanfu Fan（MIT-IBM Watson AI Lab） |
| **发表时间** | 2022（arXiv:2106.02689v3, 31 Mar 2022） |
| **刊物/会议** | ICLR 2022 (Published as a conference paper) |
| **DOI** | 未明确（arXiv:2106.02689） |
| **代码** | https://github.com/IBM/RegionViT |

## 摘要

> **英文原摘要（据提取文本清理）**：Vision transformer (ViT) has recently shown its strong capability in achieving comparable results to convolutional neural networks (CNNs) on image classification. However, vanilla ViT simply inherits the same architecture from the natural language processing directly, which is often not optimized for vision applications. Motivated by this, in this paper, we propose a new architecture that adopts the pyramid structure and employ novel regional-to-local attention rather than global self-attention in vision transformers. More specifically, our model first generates regional tokens and local tokens from an image with different patch sizes, where each regional token is associated with a set of local tokens based on the spatial location. The regional-to-local attention includes two steps: first, the regional self-attention extracts global information among all regional tokens and then the local self-attention exchanges the information among one regional token and the associated local tokens via self-attention. Therefore, even though local self-attention confines the scope in a local region but it can still receive global information. Extensive experiments on four vision tasks, including image classification, object and keypoint detection, semantics segmentation and action recognition, show that our approach outperforms or is on par with state-of-the-art ViT variants including many concurrent works. Our source codes and models are available at https://github.com/IBM/RegionViT.

> **中文翻译**：视觉 Transformer（ViT）近期在图像分类上展现出可与卷积神经网络（CNN）相媲美的能力。然而，原始 ViT 直接照搬了自然语言处理的架构，往往未针对视觉应用做优化。为此，本文提出一种新架构：采用金字塔结构，并以新颖的"区域到局部注意力（regional-to-local attention）"替代视觉 Transformer 中的全局自注意力。具体而言，模型先用不同的 patch 大小从图像生成"区域 token"和"局部 token"，每个区域 token 依据空间位置关联一组局部 token。区域到局部注意力分两步：先用区域自注意力在所有区域 token 间提取全局信息，再用局部自注意力让某个区域 token 与其关联的局部 token 之间交换信息。因此，局部自注意力虽然把作用范围限制在局部区域，仍能接收到全局信息。在图像分类、目标与关键点检测、语义分割、动作识别四类视觉任务上的大量实验表明，本方法优于或持平于包括众多同期工作在内的最先进 ViT 变体。源码与模型已开源。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

*   **为什么要做**：原始的 Vision Transformer（ViT）直接继承了为 NLP 设计的各向同性（isotropic）架构——固定的 token 数量与不变的嵌入维度。这种结构无法在不同尺度上建模上下文、也无法在不同尺度分配计算量，对需要多尺度特征和高分辨率细节的视觉任务（如目标检测、语义分割）并非最优；相比之下，多数 CNN 采用金字塔结构高效计算多尺度特征。
*   **之前方法的问题**：
    1.  **计算与内存瓶颈**：自注意力相对序列长度（token 数）呈二次方（O(N²)）的内存与计算开销。图像是二维的，token 数与分辨率呈二次关系，因此 ViT 的复杂度相对图像分辨率是**四次方**增长，导致难以在细粒度 patch 上训练，也限制了在检测/分割等高分辨率任务上的应用。
    2.  **缺乏多尺度建模**：各向同性结构无法像 CNN 的金字塔（如 PVT、PiT 已引入）那样高效生成多尺度特征。
    3.  **局部与全局的权衡**：Swin、ViL、Twins 等把自注意力限制在局部区域以降复杂度，但需要额外机制（移位窗口、重叠窗口、子采样全局 token）实现区域间信息交换。
*   **作者想解决的核心矛盾**：如何在**显著降低 ViT 的计算和内存开销**的同时，**保留捕捉长距离依赖（全局信息）与精细局部特征的能力**。作者提出一种"由粗到细（coarse-to-fine）"的层次化自注意力来回答这一矛盾。
## 关键贡献

1.  **提出 RegionViT 架构**：基于"区域到局部注意力（R2L attention）"的金字塔式 Vision Transformer，同时学习局部与全局特征。R2L 既缓解了标准全局注意力 token 过多的开销，也弥补了纯局部注意力区域间无交互的弱点。
2.  **R2L 注意力机制**：先用区域自注意力（RSA）在数量很少的"区域 token"间提取全局信息；再用局部自注意力（LSA），把每个区域的"区域 token"与其关联"局部 token"拼接后做自注意力。LSA 输入中多出的这一个区域 token，使局部 token 在专注局部的同时也能拿到全局上下文。
3.  **显著降低内存复杂度**：相对标准自注意力，R2L 把内存复杂度降低约 O(N/M²)（M 为区域窗口大小，N 为 token 总数），从而能在相当复杂度下训练更深的网络；默认设置下**内存节省最高可达 73%**。
4.  **多任务验证**：在图像分类、目标检测、关键点检测、语义分割、动作识别上，RegionViT 优于或持平于多个同期金字塔式 ViT 工作。
## 方法

*   **整体框架**（图2）：**双路径金字塔结构**。输入图像经两个不同 patch 大小的卷积分别 tokenize 成**区域 token**（大 patch，默认 28×28）和**局部 token**（小 patch，默认 4×4）。因 28/4=7，一个区域 token 在空间上覆盖 7×7=49 个局部 token，即局部区域窗口大小为 7²=49。网络含 4 个 Stage，每个 Stage 由 R2L Transformer Encoder 组成；Stage 之间用下采样把空间分辨率减半、通道数加倍（像 CNN），从而生成多尺度特征。
*   **输入输出**：输入为图像。**分类**任务输出为对最后阶段所有区域 token 求平均得到的嵌入向量；**检测等下游任务**则使用各阶段的全部局部 token 特征图（位置信息更细粒度）。
*   **关键模块**：
    1.  **Tokenization**：用卷积把图像转成 token。局部 token 的 patch 始终为 4，区域 token 的 patch 为 4×M（默认 M=7，即 28）。具体见表2：小模型（Ti/S）用 3-conv（三层 3×3 卷积级联，中间夹 LayerNorm+GeLU）线性投影；大模型（M/B）用 1-conv（k=8, s=4, p=3）。
    2.  **R2L Transformer Encoder**（图3）：核心模块，含 R2L 注意力 + FFN，并配 LayerNorm 与残差连接。
        *   **步骤一 区域自注意力（RSA）**：对所有**区域 token**做多头自注意力（MSA）。区域 token 数量很少，故以极低成本完成**全局信息交互**，覆盖整图上下文。
        *   **步骤二 局部自注意力（LSA）**：对每个区域，把更新后的区域 token 与该区域内全部局部 token **拼接**为一个序列做 MSA。多出的这一区域 token 充当"全局信息收发器"，使局部 token 既聚焦邻域、又能跨区域获取全局信息。各区域的 LSA **并行**执行。
        *   **权重共享**：RSA 与 LSA **共享相同的注意力权重，仅 LayerNorm 不共享**，因此参数量相比标准 encoder 不会显著增加。
*   **数学表述**（公式2）：给定层 d 的区域/局部输入 x_r^{d-1}、x_l^{d-1}：
    y_r^d = x_r^{d-1} + RSA(LN(x_r^{d-1}))；
    y_{i,j}^d = [ y_{r_{i,j}}^d ‖ {x_{l_{i,j,m,n}}^{d-1}}_{m,n∈M} ]（拼接区域 token 与其局部 token）；
    z_{i,j}^d = y_{i,j}^d + LSA(LN(y_{i,j}^d))；
    x_{i,j}^d = z_{i,j}^d + FFN(LN(z_{i,j}^d))。
    其中 i,j 是区域 token 的空间索引，m,n 是窗口 M² 内局部 token 的索引；拼接保证了区域与局部 token 间的信息交换。
*   **相对位置偏置（公式3）**：不用 ViT 的绝对位置嵌入，而向 R2L 注意力图引入**相对位置偏置** b，取自可学习参数 B ∈ R^{(2M-1)×(2M-1)}。**该偏置只加在局部 token 之间的注意力上，不加在区域 token 与局部 token 之间**。注意力值 a = softmax(q·kᵀ + b)。
*   **内存复杂度推导**：标准自注意力为 O(N²)。当每区域含 M 个局部 token、共 N/M 个区域时，局部注意力复杂度为 O((M+1)²×(N/M))，区域注意力复杂度为 O((N/M)²)，总体 O((M+1)²×(N/M) + (N/M)²)。以 RegionViT 主体 Stage 3 为例（M=49，N=196），内存节省约 **73%**（各模型/各阶段节省随配置变化）。
*   **下采样**：阶段间用 3×3 深度可分离卷积（depth-wise convolution）改变空间与通道维度（提取文本在此处截断，深度可分离卷积的完整描述据原文后续，待核）。
*   **模型规格**（表2）：每头维度 32，FFN 扩展比 r=4，窗口 M=7。
    - RegionViT-Ti：dim {64,128,256,512}，encoder 数 {2,2,8,2}，3-conv tokenization。
    - RegionViT-S：dim {96,192,384,768}，encoder 数 {2,2,8,2}，3-conv。
    - RegionViT-M：dim {96,192,384,768}，encoder 数 {2,2,14,2}，1-conv。
    - RegionViT-B：dim {128,256,512,1024}，encoder 数 {2,2,14,2}，1-conv。
*   **训练方式**：基于标准视觉 Transformer 训练流程；在 ImageNet-1K 上从头训练，并探索了 ImageNet-21K 预训练（提取缓存仅见 p.16 提到 ImageNet21K 预训练/微调设置，具体超参待核）。
*   **和已有方法的差异**（表1）：
    *   vs **ViT**：各向同性 + 全局注意力，无窗口划分、无全局 token。
    *   vs **PVT**：金字塔结构，但注意力仍是全局的、计算量大。
    *   vs **Swin**：均为金字塔 + 非重叠窗口局部注意力；Swin 靠**移位窗口**实现跨区域交换，无全局 token；RegionViT 靠**显式区域 token + R2L 注意力**。
    *   vs **ViL**：ViL 用**重叠窗口**做局部注意力 + 一个可学习全局 token；RegionViT 用非重叠窗口 + 区域 token。
    *   vs **Twins**：Twins 把局部 token 子采样成全局 token 作为 key 来跨区域交互；RegionViT 引入独立的、与局部 token 关联的区域 token。一大区别是 RegionViT 的局部自注意力序列里**额外含一个区域 token**。
*   **注意力类论文特化分析**：
    *   **作用维度**：**空间维度**上的**局部 + 区域（全局）混合注意力**；通过非重叠区域划分在局部窗口内做细粒度注意力，并经区域 token 完成全局交互。
    *   **可插入网络**：不是即插即用模块，而是一个完整的网络设计范式。
    *   **计算量 vs 效果**：以约 73% 内存节省为代价，性能与全局注意力模型持平甚至更优，效率与效果权衡良好。
## 实验

*   **使用的数据集**：ImageNet-1K（分类，另有 ImageNet-21K 预训练）；COCO（目标检测、关键点检测）；ADE20K（语义分割）；Something-Something V2（动作识别）。
*   **对比方法**：ViT、DeiT、PVT、Swin、T2T-ViT、CrossViT、CaiT、LV-ViT、LocalViT、ConT、Twins、ViL、BoTNet、LambdaNetwork 等同期/相关 ViT 与注意力工作。
*   **评价指标**：Top-1 准确率（分类）、box/mask mAP（检测）、mIoU（分割）、Top-1 准确率（动作识别）。
*   **主实验结果**（以下具体数值据原文后续页 p.10-12，提取缓存仅覆盖到方法节，待核）：
    *   **图像分类**：ImageNet-1K 上 RegionViT-S 约 **83.6% Top-1**，在相当参数/算力下优于 Swin-S（83.2%）与 Twins-SVT-S（83.2%）。（据原文表3，提取缓存未覆盖，待核）
    *   **目标检测**：COCO + Mask R-CNN，RegionViT-S 骨干约 44M 参数达 **45.8 box mAP**。（据原文表4，待核）
    *   **语义分割**：ADE20K + Semantic FPN，RegionViT-S 约 **45.6 mIoU**。（据原文表5，待核）
    *   **动作识别**：Something-Something V2，RegionViT-S 约 **65.0%**。（据原文表6，待核）
*   **消融实验**：原文通过对比验证区域 token 与 R2L 注意力的有效性（移除区域 token 或改用全局注意力会掉点）。（据原文，提取缓存未覆盖具体表格，待核）
*   **泛化实验**：横跨分类/检测/分割/动作识别四任务均表现良好，体现架构泛化性。
*   **效率信息**：R2L 在主体 Stage 3（M=49，N=196）带来约 **73%** 内存复杂度节省（此结论在提取文本 p.5 有明确依据）；精度与 Swin 等持平，参数/FLOPs 有竞争力。
## 局限

*   **超参数依赖**：区域窗口大小 M 是关键超参，默认 7（对应 28×28 区域 patch）；提取文本未给出不同 M 的系统消融，敏感性待核。
*   **信息瓶颈风险**：跨区域全局信息须经数量有限的区域 token 中转，可能成为信息瓶颈，尤其在需捕捉极精细跨区域关系时。
*   **刚性区域划分**：将图像硬性切成非重叠区域，可能与图像内容的语义边界不吻合。
*   **大数据规模未充分探索**：提取文本提到 ImageNet-21K 预训练，但相对 ViT 原始的 JFT-300M 级规模实验，更大规模数据下的表现讨论有限（待核）。
*   **权重共享是否最优**：RSA/LSA 共享权重（仅 LN 不共享）是工程性折中，是否最优未充分讨论。
*   **复现**：作者提供开源代码（IBM/RegionViT），复现风险较低。
## 个人评论

这篇论文最值得学习的核心在于其**优雅高效的注意力设计思想**：引入一组独立的"区域 token"作为全局信息的**代表与桥梁**，再把它当作"一个额外的局部 token"塞进局部窗口一起做自注意力。这种设计带来三点价值：
1.  **解耦与桥接**：把昂贵的全局交互交给数量极少的"区域代表"（RSA），再让它们去"通知 + 收集"海量局部 token（LSA），实现全局与局部的解耦和高效连接。相比 Swin 的移位窗口、Twins 的子采样全局 token，R2L 用"显式 token + 拼接"的方式更直接、概念更清晰。
2.  **复杂度与效果的强权衡**：没有简单丢弃全局信息，而是用结构化方式近似全局交互，在大幅降本的同时保住性能；且 RSA/LSA 共享权重让参数几乎不增。
3.  **启发性**：提供了一条清晰思路——设计高效 Transformer 时，可通过**引入不同粒度的 token 并定义其交互规则**来显式建模多尺度，而不只是机械模仿 CNN 分层。"桥梁 token"思想可迁移到其他层次化/多尺度任务。

一点保留：所有跨区域信息必须经少量区域 token 中转，理论上存在瓶颈；同时区域划分是刚性的非重叠窗口，与语义边界未必对齐——这两点是该范式后续可改进的方向。

### 使用建议

*   **快速了解**：读**摘要**、**第1节引言**、**图1/2/3**，再看实验结果，即可掌握动机、核心机制与效果。
*   **复现**：精读**第3节方法**（尤其公式(2)、相对位置偏置公式(3)、表2 的 tokenization/窗口/维度配置）与**图3**，参考开源代码（https://github.com/IBM/RegionViT）。关注 R2L Encoder 实现、RSA/LSA 权重共享、并行 LSA。
*   **借鉴创新点**：深入理解 R2L 的设计哲学——用辅助 token + 分阶段注意力解耦全局与局部计算。
*   **写 Related Work**：放在"改进 Vision Transformer 效率与结构"或"局部-全局注意力机制"类别，与 Swin、PVT、Twins、ViL 并列讨论。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的 Vision Transformer 方向，聚焦于**注意力算子模块的改进**：用层次化的"区域到局部注意力（R2L）"替代 ViT 的全局自注意力，以解决全局自注意力的高内存/计算复杂度问题。归入"B_注意力算子模块"主题贴切。发表于 ICLR 2022（arXiv:2106.02689v3）。

## 2. 一句话总结
RegionViT 提出**区域到局部（Regional-to-Local, R2L）注意力**：先在少量"区域 token"间做区域自注意力提取全局信息，再让每个区域 token 与其关联"局部 token"拼接做局部自注意力，从而以远低于全局注意力的内存成本（默认设置最高省约 73%）在金字塔式 ViT 中同时学到全局上下文与局部细节。

## 3. 背景与问题
*   **为什么要做**：ViT 直接继承 NLP 的各向同性架构（固定 token 数、不变嵌入维度），无法像 CNN 金字塔那样在不同尺度分配计算、生成多尺度特征，对检测/分割等高分辨率任务并非最优。
*   **之前方法的问题**：
    1.  **二次方/四次方复杂度**：自注意力相对序列长度 O(N²)；图像二维使 token 数与分辨率呈二次关系，ViT 复杂度相对分辨率为四次方，难以在细粒度 patch 上训练。
    2.  **缺乏多尺度**：各向同性结构难高效产出多尺度特征（PVT、PiT 已引入金字塔改善）。
    3.  **局部-全局权衡**：Swin（移位窗口）、ViL（重叠窗口 + 1 个全局 token）、Twins（子采样全局 token）虽降复杂度，但跨区域通信机制各异、不够直接。
*   **核心矛盾**：在显著降低计算/内存开销的同时，保留长距离依赖与精细局部特征建模能力。作者用"由粗到细"的层次化自注意力回应。

## 4. 核心贡献
1.  **RegionViT 架构**：基于 R2L 注意力，兼顾局部与全局，既缓解全局注意力 token 过多、又补足纯局部注意力区域间无交互的缺陷。
2.  **R2L 注意力**：RSA（区域 token 间）→ LSA（区域 token + 其局部 token 拼接），区域 token 充当跨区域全局信息的桥梁；RSA/LSA 共享权重（仅 LN 不共享），参数几乎不增。
3.  **内存复杂度降低约 O(N/M²)**：默认设置最高省约 73%，可在相当复杂度下训练更深网络。
4.  **四任务验证**：分类、检测、关键点检测、分割、动作识别上优于或持平同期金字塔 ViT。

## 5. 方法详解
*   **整体框架**（图2）：双路径金字塔。两套卷积 tokenization 分别产生区域 token（patch 28²）与局部 token（patch 4²），故一个区域 token 覆盖 7×7=49 个局部 token（窗口 M²=49）。4 个 Stage，阶段间下采样把空间减半、通道加倍。分类用末阶段区域 token 平均；检测用各阶段全部局部 token。
*   **R2L Transformer Encoder**（图3，公式2）：
    *   **RSA**：对所有区域 token 做 MSA，低成本完成全局交互。
    *   **LSA**：每区域把（更新后的）区域 token 与其全部局部 token 拼接做 MSA，各区域并行；多出的区域 token 让局部 token 跨区域拿全局信息。
    *   公式2：y_r = x_r + RSA(LN(x_r))；y_{i,j} = [y_{r_{i,j}} ‖ 局部 token]；z = y + LSA(LN(y))；x = z + FFN(LN(z))。
    *   **权重共享**：RSA 与 LSA 共享注意力权重，仅 LayerNorm 不同。
*   **相对位置偏置**（公式3）：用相对位置偏置 B ∈ R^{(2M-1)×(2M-1)} 替代 ViT 的绝对位置嵌入；**仅加在局部 token 之间**，不加在区域-局部之间。
*   **内存复杂度**：O((M+1)²×(N/M) + (N/M)²)；Stage 3（M=49, N=196）约省 73%。
*   **下采样**：3×3 深度可分离卷积（细节据原文后续，待核）。
*   **模型规格**（表2）：每头维 32、FFN 扩展比 4、M=7。Ti/S 用 3-conv，M/B 用 1-conv(k=8,s=4,p=3)；维度与 encoder 数见表2（{2,2,8,2} 或 {2,2,14,2}）。
*   **与相关工作差异**（表1）：ViT/PVT 全局注意力无窗口；Swin 移位窗口、无全局 token；ViL 重叠窗口 + 1 个学习全局 token；Twins 子采样全局 token；RegionViT 用非重叠窗口 + 显式区域 token，且 LSA 序列额外含一个区域 token。

## 6. 实验与结果
*   **数据集**：ImageNet-1K（+ ImageNet-21K 预训练）、COCO、ADE20K、Something-Something V2。
*   **对比**：ViT、DeiT、PVT、Swin、Twins、ViL、T2T-ViT、CrossViT、CaiT、LV-ViT、LocalViT、ConT、BoTNet、LambdaNetwork 等。
*   **指标**：Top-1（分类/动作）、mAP（检测）、mIoU（分割）。
*   **主结果**（具体数值据原文后续页 p.10-12，提取缓存未覆盖，待核）：
    *   分类：RegionViT-S 约 **83.6%** Top-1，优于 Swin-S/Twins-SVT-S（均 83.2%）。
    *   检测：COCO + Mask R-CNN，RegionViT-S ~44M 参数约 **45.8** box mAP。
    *   分割：ADE20K + Semantic FPN 约 **45.6** mIoU。
    *   动作识别：SSv2 约 **65.0%**。
*   **消融**：验证区域 token 与 R2L 的必要性（去掉会掉点）——据原文，提取缓存未覆盖具体表，待核。
*   **效率**：主体 Stage 3 省约 **73%** 内存（此点提取文本 p.5 有明确依据）。

## 7. 这篇论文真正有价值的地方
最核心的价值是其**"桥梁 token"式的注意力设计**：用极少的区域 token 承担全局交互（RSA），再把区域 token 当作额外局部 token 注入局部窗口（LSA），实现：
1.  **解耦与桥接**——把昂贵全局交互交给少量代表，再让它们通知/收集海量局部 token。
2.  **复杂度-效果强权衡**——结构化近似全局交互，降本不丢性能；RSA/LSA 共享权重使参数几乎不增。
3.  **方法论启发**——通过"引入不同粒度 token + 定义交互规则"显式建模多尺度，而非机械模仿 CNN 分层。

## 8. 局限与问题
*   **超参 M 依赖**：默认 7，不同 M 的系统消融在提取文本中未见（待核）。
*   **信息瓶颈**：跨区域全局信息须经少量区域 token 中转。
*   **刚性非重叠区域**：与语义边界未必对齐。
*   **大规模数据**：见 ImageNet-21K 预训练，但相对 JFT-300M 级规模的讨论有限（待核）。
*   **权重共享是否最优**：RSA/LSA 共享权重为工程折中，未充分讨论替代方案。

## 9. 我该怎么使用这篇论文
*   **快速了解**：摘要 + 引言 + 图1/2/3 + 实验。
*   **复现**：精读第3节方法（公式2、公式3、表2），看开源代码（IBM/RegionViT），关注 RSA/LSA 权重共享与并行 LSA、相对位置偏置只加在局部 token 之间。
*   **借鉴创新点**：R2L 的"辅助 token + 分阶段注意力"解耦全局/局部，可迁移到多尺度层次化任务。
*   **写 Related Work**：放在"高效 ViT 结构 / 局部-全局注意力"，与 Swin、PVT、Twins、ViL 并列。

## 10. 和其他论文的关系
*   **ViT (Dosovitskiy et al., 2021)**：起点与基础架构，所有改进针对其各向同性 + 全局注意力的问题。
*   **PVT (Wang et al., 2021)**：率先把金字塔结构引入 ViT，但注意力仍全局；RegionViT 在金字塔上加高效局部-全局交互。
*   **Swin (Liu et al., 2021)**：同为金字塔 + 非重叠窗口局部注意力，最主要对比基线；跨区域机制为移位窗口 vs 区域 token。
*   **ViL (Zhang et al., 2021a)**：重叠窗口局部注意力 + 1 个可学习全局 token；RegionViT 用非重叠窗口 + 区域 token。
*   **Twins (Chu et al., 2021a)**：子采样局部 token 作全局 token 跨区域交互；与 RegionViT 的区域 token 方案对照。

## 11. 关键词
Vision Transformer, 区域到局部注意力(R2L), 区域 token, 局部注意力, 金字塔结构, 多尺度特征, 相对位置偏置, 内存复杂度, 图像分类, 目标检测, 语义分割, 动作识别

## 12. 可信度说明
本精读基于 PDF 提取文本生成。提取缓存实际覆盖 p.1-约 p.5（25000 字符截断，含摘要、引言、相关工作、方法、表1/表2、公式1-3、内存复杂度推导、相对位置偏置），这部分文本提取质量良好，核心机制与"73% 内存节省""M=49/N=196""窗口 7²""相对位置偏置只加局部 token"等均直接来自原文。实验数值（83.6%、45.8 mAP、45.6 mIoU、65.0%）位于提取截断之后的页（p.10-12），由原笔记保留并已逐条标注"据原文后续页，提取缓存未覆盖，待核"。下采样的深度可分离卷积完整描述、消融具体表格亦在截断之后，相应标注待核。

---

> **可信度补充**: PDF 提取质量 = **high** (提取覆盖 p.1-约5/19, 25000 字符截断; 方法与机制部分文本清晰); 来源缓存: `.paper-cache/extracts/regionvit.txt` (头部标 12/19 页, 实际正文展示至方法节即被 25000 字符上限截断); 实验数值据原文后续页保留并标注待核; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-19; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-19。
- **提取情况**: 缺失页 7 页, 其中 7 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Published as a conference paper at ICLR 2022
- p.13: Will Kay, Joao Carreira, Karen Simonyan, Brian Zhang, Chloe Hillier, Sudheendra Vijaya-
- p.13: Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pi etro Perona, Deva Ramanan, Piotr
- p.14: Prajit Ramachandran, Niki Parmar, Ashish Vaswani, Irwan Be llo, Anselm Levskaya, and Jonathon
- p.14: Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco Mas sa, Alexandre Sablayrolles, and
- p.14: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit , Llion Jones, Aidan N Gomez, ukasz
- p.14: Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao Song, Ding Liang, Tong Lu, Ping Luo,
- p.14: Xiaosong Wang, Yifan Peng, Le Lu, Zhiyong Lu, Mohammadhadi B agheri, and Ronald M Sum-
- p.15: Li Yuan, Yunpeng Chen, Tao Wang, Weihao Yu, Yujun Shi, Franci s EH Tay, Jiashi Feng, and
- p.15: Multi-Scale Vision Longformer: A New Vision Transformer fo r High-Resolution Image Encod-
- p.15: Proceedings of the IEEE/CVF Conference on Computer Vision a nd Pattern Recognition (CVPR) ,
- p.16: Batch size 4,096 4,096 1,024 768

### 缺失页关键摘录

- p.13: ken Labeling: Training a 85.4% Top-1 Accuracy Vision Transf ormer with 56M Parameters on
- p.15: parsing through ade20k dataset. In Proceedings of the IEEE Conference on Computer Vision and
- p.16: Table A1: Details of training settings for image classiﬁcation on Ima geNet1K and ImageNet21K.
- p.16: and action recognition separately. Then, we provide detail ed results on object detection and ablation
- p.16: 256 for evaluation. While pretraining on ImageNet21K ( Deng et al. ,2009 ), we use similar settings
- p.16: During evaluation, we resize the shorter side of an image to 2 56 and then take a 224 ×224 region at
- p.16: the center and report top-1 accuracy. For ﬁnetuning experim ents from ImageNet21K, we ﬁnetune
- p.16: evaluation, we directly resize the shorter side to 384 and th en take center 384 ×384 crop. We trained
- p.17: crop a 448 ×448 region for training. During the evaluation, we take the w hole image after resizing
- p.17: as 8×224×224. During evaluation, we use the same way to sample frames b ut take 3 224 ×224
- p.17: We provided more details of some Tables shown in the main pape r here. Table A2and Table A3
- p.17: include more metrics as compared to Table 5. Table A4shows the results on keypoint detection.
<!-- AI_READING_NOTE_END -->
