---
title: "SwiftFormer: Efficient Additive Attention for Transformer-based Real-time Mobile Vision Applications"
authors:
  - "Abdelrahman Shaker"
  - "Muhammad Maaz"
  - "Hanoona Rasheed"
  - "Salman Khan"
  - "Ming-Hsuan Yang"
  - "Fahad Shahbaz Khan"
year: 2023
venue: "ICCV 2023"
doi: 
pdf: [[SwiftFormerEncoder&ConvEncoder.pdf]]
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
extract_cache: .paper-cache/extracts/SwiftFormerEncoder&ConvEncoder.txt
---

# SwiftFormer: Efficient Additive Attention for Transformer-based Real-time Mobile Vision Applications

## 基本信息
- **PDF**: [[SwiftFormerEncoder&ConvEncoder.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SwiftFormer: Efficient Additive Attention for Transformer-based Real-time Mobile Vision Applications |
| **作者** | Abdelrahman Shaker; Muhammad Maaz; Hanoona Rasheed; Salman Khan; Ming-Hsuan Yang; Fahad Shahbaz Khan（MBZUAI / UC Merced / Yonsei / Google Research / Linköping University） |
| **发表时间** | 2023 |
| **刊物/会议** | ICCV 2023（CVF Open Access 版） |
| **DOI** | 未明确 |
| **代码** | https://tinyurl.com/5ft8v46w |

## 摘要

> Self-attention has become a de facto choice for capturing global context in various vision applications. However, its quadratic computational complexity with respect to image resolution limits its use in real-time applications, especially for deployment on resource-constrained mobile devices. Although hybrid approaches have been proposed to combine the advantages of convolutions and self-attention for a better speed-accuracy trade-off, the expensive matrix multiplication operations in self-attention remain a bottleneck. In this work, we introduce a novel efficient additive attention mechanism that effectively replaces the quadratic matrix multiplication operations with linear element-wise multiplications. Our design shows that the key-value interaction can be replaced with a linear layer without sacrificing any accuracy. Unlike previous state-of-the-art methods, our efficient formulation of self-attention enables its usage at all stages of the network. Using our proposed efficient additive attention, we build a series of models called "SwiftFormer" which achieves state-of-the-art performance in terms of both accuracy and mobile inference speed. Our small variant achieves 78.5% top-1 ImageNet-1K accuracy with only 0.8 ms latency on iPhone 14, which is more accurate and 2× faster compared to MobileViT-v2.

> **中文翻译**：自注意力已成为各类视觉应用中捕捉全局上下文的事实标准。然而其计算复杂度相对图像分辨率呈二次增长，限制了它在实时应用、尤其是资源受限移动设备上的部署。尽管已有混合方法尝试结合卷积与自注意力以获得更好的速度-精度折中，但自注意力中昂贵的矩阵乘法运算仍是瓶颈。本文提出一种新颖的高效加法注意力（efficient additive attention）机制，用线性的逐元素乘法有效替代二次的矩阵乘法运算。我们的设计表明：键-值（key-value）交互可以用一个线性层替代而不损失任何精度。与以往 SOTA 方法不同，我们对自注意力的高效形式化使其能用于网络的所有阶段。基于该机制，我们构建了一系列称为 "SwiftFormer" 的模型，在精度与移动端推理速度上均达到 SOTA。小模型在 iPhone 14 上仅 0.8 ms 延迟即达到 78.5% 的 ImageNet-1K top-1 精度，比 MobileViT-v2 更准且快 2 倍。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：自注意力能有效建模输入 token 间的全局交互，是 ViT 的核心，但其复杂度 O(n²·d) 相对图像分辨率呈二次增长，在低功耗移动设备上推理慢、内存占用高，难以满足实时需求。因此 CNN 仍是移动端实时部署的首选（卷积计算高效），但 CNN 依赖局部连接和固定权重，难以适应变化分辨率、难以捕捉长程依赖。如何兼取两者之长是核心动机。
- **之前方法有什么问题**：
    1.  **纯 CNN（MobileNet 系列）**：高效但缺乏特征间的全局交互，性能受限。
    2.  **混合 CNN-Transformer**：通常只在高分辨率早期阶段用轻量 CNN、在低分辨率后期阶段用自注意力（如 EfficientFormer 仅最后阶段用 MHSA），因 MHSA 二次复杂度无法用于早期高分辨率阶段 → 全局上下文建模不一致、不充分。
    3.  **高效自注意力变体**：跨特征维度计算注意力（EdgeNeXt 转置自注意力，O(n·d²)）、局部窗口注意力、注意力前先池化、稀疏 token 注意力（EdgeViT）、LSH（Reformer，O(n log n)，仅对长序列有效）、低秩分解（LinFormer，O(n)）等。它们**理论上**降低了复杂度，但仍依赖矩阵乘法 / 昂贵投影，FLOPs/参数的下降未必转化为移动端实际加速（如 MobileViT-v2 仍比 MobileNet-v2 慢 2 倍）。
- **最接近的前驱**：MobileViT-v2 的可分离自注意力（separable self-attention）用逐元素运算替代点积来算上下文向量（公式 3），但仍保留了与 V 的交互。
- **核心矛盾**：在移动端严格算力约束下，既要像 Transformer 那样建模全局上下文，又要有与 CNN 可比的实际推理速度。

## 关键贡献

1.  **提出高效加法注意力（Efficient Additive Attention）**：在视觉骨干网中彻底去除昂贵的矩阵乘法运算，显著降低计算复杂度。
2.  **去除显式 key-value 交互**：证明仅用 query-key 交互再接一个线性变换层即可有效编码全局上下文，去掉 V 交互而不损失精度。
3.  **可用于所有阶段的一致混合设计**：因注意力为线性复杂度，可在网络每个阶段（含早期高分辨率阶段）一致地学习局部-全局表征，获得更优的速度-精度折中。
4.  **构建 SwiftFormer 模型族**：基于该注意力 + 有效卷积编码器，**无需 NAS**（与 EfficientFormer 的延迟驱动瘦身不同）。
5.  **移动端 SOTA**：小模型 0.8 ms 延迟达 78.5% top-1（iPhone 14），比 MobileViT-v2 更准且快 2 倍；大模型 1.9 ms 达 83.0%；相比 EfficientFormer-L1，SwiftFormer-L1 在同延迟下 top-1 绝对提升 1.7%（图 1）。

## 方法

- **整体框架**：四阶段分层结构（图 3 上行）。输入图像经 Patch Embedding（两个 stride=2 的 3×3 卷积）得到 H/4×W/4×C1 特征；随后依次过 4 个阶段，每阶段在 {1/4, 1/8, 1/16, 1/32} 尺度上由「卷积编码器（Conv. Encoder）」后接「SwiftFormer 编码器」组成，**所有阶段结构一致**。相邻阶段间插入下采样层（增加通道、减半 token 长度）。
- **输入输出**：输入 H×W×3，四阶段分别输出 H/4×W/4×C1、H/8×W/8×C2、H/16×W/16×C3、H/32×W/32×C4 的层级特征。
- **关键模块**：
    1.  **有效卷积编码器（Conv. Encoder）**：替代 EfficientFormer/PoolFormer 用作局部 token mixer 的 3×3 平均池化。结构（公式 7）：X → 3×3 深度卷积 DWConv + BN → 两个 1×1 逐点卷积 Conv₁（其中带 GeLU 激活）做通道混合 → 残差。论文指出：用深度卷积替换池化**不增加延迟**，却在不增加参数与延迟的情况下提升性能。
        - 公式 7：`X̂ᵢ = Conv₁(Conv₁,G(DWConv_BN(Xᵢ))) + Xᵢ`
    2.  **SwiftFormer 编码器**：学习每个尺度的局部-全局表征。先经 3×3 深度卷积 + 1×1 逐点卷积提取局部特征 → 进入**高效加法注意力**模块 → 最后接 Linear 块（两个 1×1 逐点卷积）做通道混合。
- **高效加法注意力（核心，3.2 节）**：
    - 输入 x 经两矩阵 W_q、W_k 投影为 Q、K ∈ ℝ^{n×d}（W_q, W_k ∈ ℝ^{d×d}）。
    - **(a) 学习注意力权重**：Q 与可学习参数向量 w_a ∈ ℝ^d 相乘得全局注意力权重 α ∈ ℝ^n（公式 4）：`α = Q·w_a / √d`。
    - **(b) 池化得全局查询**：按 α 对 Q 加权池化为单一全局查询向量 q ∈ ℝ^d（公式 5）：`q = Σᵢ αᵢ * Qᵢ`。
    - **(c) 编码全局上下文**：将广播后的 q 与 K ∈ ℝ^{n×d} 做逐元素乘，得全局上下文 ℝ^{n×d}。该矩阵与 MHSA 的注意力矩阵相似——捕获每个 token 的信息、能学习输入序列的相关性，但计算开销远低于 MHSA、且相对 token 长度线性。
    - **(d) 线性变换与输出**（公式 6）：`x̂ = Q̂ + T(K * q)`，其中 Q̂ 是归一化后的查询矩阵，T 是线性变换层。
- **与已有方法的差异（对应图 2 a-d）**：
    - 与 **(a) 标准自注意力**（公式 1，O(n²·d)，点积 + Softmax）比：去掉二次矩阵乘法。
    - 与 **(b) EdgeNeXt 转置自注意力**（公式 2，O(n·d²)）比：后者跨通道维做点积、相对 d 仍二次，且仍用点积；本文不用点积。
    - 与 **(c) MobileViT-v2 可分离自注意力**（公式 3）比：MobileViT-v2 仍保留与 V 的逐元素交互；本文**进一步去除 K-V 交互**，改用线性变换 T，并引入可学习的全局查询生成机制。
    - 与 **EfficientFormer** 比：将注意力推广到**所有阶段**（而非仅最后阶段），并用 Conv. Encoder 替换池化作为局部混合器。
    - 与 NLP 中的加法注意力比：标准加法注意力对 Q、K、V 三步顺序处理；本文去掉 K-V 交互，仅编码 query-key 交互再接线性变换。
- **论文类型特化（注意力类）**：
    - **作用维度**：作用于**空间维度**（token 序列），通过单一全局查询 q 聚合全局空间信息。
    - **可插入网络**：作为独立可替换的编码器模块（SwiftFormer Encoder），在每个阶段堆叠。
    - **计算量 vs 效果**：核心目标是把延迟降到与高效 CNN 可比；消除矩阵乘法与 K-V 交互后，相对 token 长度为线性复杂度，仍保留全局建模能力。

## 实验

> 注：提取缓存仅覆盖到方法 3.3 节（前约 5 页正文），实验表格的具体数值多在后续页，相关条目按原文摘要/引言可确认者保留，表级细节标注待核。

- **使用数据集**：ImageNet-1K 图像分类（主）。目标检测、实例分割、语义分割（用于验证泛化，摘要与 3.2 节明确提及在 detection、segmentation 上验证；具体数据集如 MS COCO / ADE20K 及检测/分割框架据原文后续页，提取缓存未覆盖，待核）。
- **对比方法**：移动端 SOTA，引言/相关工作中点名的有 MobileViT-v2、EfficientFormer、MobileNet 系列、EdgeNeXt、PoolFormer、EdgeViT、GCViT 等（完整对比表据原文后续页，提取缓存未覆盖，待核）。
- **评价指标**：Top-1 分类精度、iPhone 14 推理延迟（ms）、参数量、FLOPs。
- **主实验结果（摘要/引言已确认）**：
    - SwiftFormer 小模型：78.5% top-1，0.8 ms（iPhone 14），比 MobileViT-v2 更准且快 2 倍。
    - SwiftFormer 大模型：83.0% top-1，1.9 ms。（原文称 "our large model"，未在提取文本中点名具体变体编号如 L3；变体命名据原文后续页，待核）
    - 相比 EfficientFormer-L1，SwiftFormer-L1 在**相同延迟**下 top-1 绝对提升 1.7%，且无需 NAS（图 1）。
- **消融实验（据原文后续页，提取缓存未覆盖，待核）**：论文设计上应包含——深度卷积替换池化作为局部混合器的收益、高效加法注意力各组件（全局查询生成、去除 K-V 交互）的必要性、注意力用于全部阶段 vs 仅最后阶段。具体表格数值待核。
- **效率信息**：核心卖点是参数/FLOPs 优化的同时，移动端**实际延迟**显著降低（强调理论复杂度下降要落到真实推理加速）。

## 局限

1.  **任务验证范围**：宣传与主评估集中在 ImageNet 分类；检测/分割结果的具体表格未在提取文本中出现；更复杂任务（视频、3D）未涉及。
2.  **硬件依赖性**：延迟数据基于 iPhone 14（Apple Neural Engine），在 Android / 其他移动 GPU/NPU 上的表现可能不同。
3.  **可扩展性**：主要展示中小规模模型，设计原则在超大规模模型上是否成立未讨论。
4.  **设计自动化**：架构（各阶段通道数、堆叠数）人工设计、未用 NAS；论文以「无需 NAS」为卖点，但也未探讨结合 NAS 能否进一步提升。
5.  **极端低端设备**：未分析在微控制器等极低算力设备上的可行性。
6.  **单一全局查询的表达瓶颈（评注）**：将整张特征图压成一个全局查询向量 q，可能在需要细粒度空间区分的密集预测任务上不及完整 MHSA——这是用速度换全局交互精度的内在折中，文中未作上界分析。

## 个人评论

1.  **对注意力机制的极致简化**：大胆挑战 Q-K-V 三者交互的传统范式，证明视觉任务中可仅保留 query-key 交互、用线性层替代 key-value 交互。这为更轻量的注意力模块提供了清晰思路。
2.  **工程与理论的平衡**：不停留在复杂度分析，而是紧扣移动端实际延迟设计——直接点名「理论 FLOPs 下降未必转化为移动端加速」「MobileViT-v2 比 MobileNet-v2 慢 2×」，把「实际推理速度」当作一等约束，是其成功关键。
3.  **一致性设计的价值**：证明让全局注意力贯穿网络**所有阶段**（而非仅后期）对性能很重要，打破了「早期卷积、后期注意力」的混合设计定式，也使模型对高分辨率输入更可扩展。
4.  **一个值得追问的点**：把全局上下文压成单个 q 向量，本质是一种激进的低秩近似。它在分类上不掉点，但对密集预测是否同样无损，依赖后续页未覆盖的检测/分割表格——读者复现时应优先核对这部分。
5.  **写作范例**：动机从移动端部署痛点逐层推进（CNN 局部性 → 混合设计的不一致 → 高效变体的「理论降复杂度但实际不快」），图 2(a-d) 把四种注意力并排对比，是很好的 related work 组织方式。

### 使用建议

- **如果快速了解**：读**摘要**、**引言贡献列表**、**图 1**（延迟-精度）、**图 2**（四种注意力对比）、**图 3**（整体架构 + 两个编码器）。
- **如果复现**：精读 **3.2 高效加法注意力**（公式 4-6 的维度变化：α∈ℝⁿ、q∈ℝ^d、输出 ℝ^{n×d}）与 **3.3 架构**（Conv. Encoder 公式 7、SwiftFormer Encoder 的局部卷积 + 注意力 + Linear 块顺序）；结合开源代码确认实现细节与各变体配置。
- **如果借鉴创新点**：
    - **去除 key-value 交互 + 线性变换替代** 的思想，可用于简化其他序列模型的注意力。
    - **加权池化构建全局查询 q** 是一种可学习的全局特征聚合方式。
    - **用深度卷积替换池化** 作为局部混合器、且不增延迟的工程做法。
- **如果写 Related Work**：归类于「高效视觉 Transformer / 移动端轻量化注意力」，与 [[MobileViT-v2]]、[[EfficientFormer]]、[[EdgeNeXt]] 等并列讨论。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
高效视觉 Transformer 方向，核心是设计一种极轻量的注意力算子——高效加法注意力（Efficient Additive Attention），解决自注意力二次复杂度在移动端实时部署的瓶颈。属于「B_注意力算子模块」主题：论文提出了一个具体的注意力算子（公式 4-6）及其在分层骨干网各阶段的一致部署方式，并据此构建 SwiftFormer 模型族。ICCV 2023。

## 2. 一句话总结
本文提出「高效加法注意力」：用线性逐元素乘法替代二次矩阵乘法、并去除显式 key-value 交互（改用一个线性变换层），从而把注意力做成线性复杂度、可用于网络所有阶段；据此构建的 SwiftFormer 在 iPhone 14 上以 0.8 ms 达 78.5% top-1，比 MobileViT-v2 更准且快 2 倍。

## 3. 背景与问题
- **为什么要做**：自注意力复杂度 O(n²·d) 相对分辨率二次增长，移动端推理慢、内存高；CNN 高效但缺全局交互。需要兼取两者之长。
- **之前方法的问题**：
    1.  纯 CNN（MobileNet）缺全局交互。
    2.  混合设计（EfficientFormer）只在最后阶段用 MHSA，早期阶段因二次复杂度无法用注意力 → 上下文建模不一致。
    3.  高效注意力变体（EdgeNeXt 转置 O(n·d²)、EdgeViT 稀疏、Reformer LSH、LinFormer 低秩、MobileViT-v2 可分离）理论降复杂度，但仍依赖矩阵乘法/昂贵投影，FLOPs 下降不等于移动端实际加速（MobileViT-v2 仍比 MobileNet-v2 慢 2×）。
- **核心矛盾**：移动端算力约束下，同时要全局建模能力与 CNN 级实际推理速度。

## 4. 核心贡献
1.  提出高效加法注意力，去除昂贵矩阵乘法，显著降复杂度。
2.  去除显式 K-V 交互，仅用 query-key 交互 + 线性变换即可编码全局上下文、不掉精度。
3.  线性复杂度使注意力可用于**所有阶段**，获得一致的局部-全局表征与更优速度-精度折中。
4.  构建 SwiftFormer 模型族，**无需 NAS**。
5.  移动端 SOTA：小模型 0.8 ms/78.5%（比 MobileViT-v2 准且快 2×）、大模型 1.9 ms/83.0%；SwiftFormer-L1 较 EfficientFormer-L1 同延迟 +1.7% top-1（图 1）。

## 5. 方法详解
- **整体框架**：四阶段分层（图 3 上），尺度 {1/4,1/8,1/16,1/32}。Patch Embed（两个 stride=2 的 3×3 卷积）→ 各阶段「Conv. Encoder + SwiftFormer Encoder」，结构一致；阶段间下采样增通道、减 token。四阶段输出 H/4·C1、H/8·C2、H/16·C3、H/32·C4。
- **Conv. Encoder（公式 7）**：DWConv 3×3 + BN → 两个 1×1 逐点卷积（含 GeLU）→ 残差。替代 EfficientFormer/PoolFormer 的 3×3 平均池化局部混合器，不增延迟、不增参数却提性能。
- **SwiftFormer Encoder**：3×3 DWConv + 1×1 逐点卷积（局部）→ 高效加法注意力 → Linear 块（两个 1×1 逐点卷积，通道混合）。
- **高效加法注意力（4 步，对应图 2d）**：
    - 投影：x → Q, K ∈ ℝ^{n×d}（W_q, W_k ∈ ℝ^{d×d}）。
    - 公式 4：`α = Q·w_a / √d`，w_a ∈ ℝ^d 可学习，得 α ∈ ℝ^n。
    - 公式 5：`q = Σᵢ αᵢ * Qᵢ`，按 α 加权池化得全局查询 q ∈ ℝ^d。
    - 全局上下文：广播 q 与 K 逐元素乘 → ℝ^{n×d}，类似 MHSA 注意力矩阵但线性复杂度、开销远低。
    - 公式 6：`x̂ = Q̂ + T(K * q)`，Q̂ 为归一化查询，T 为线性变换。
- **直观解释**：标准注意力算所有 token 两两相似度（QK^T，二次）。本文先学一个代表「全局应关注模式」的查询向量 q，再算每个 token 的 K 与该固定模式的相似度（K*q），从而避免 token 间相似度大矩阵——相当于用一个「模板」匹配所有输入，而非两两匹配。
- **与各注意力差异**：vs 标准（去二次矩阵乘）；vs EdgeNeXt 转置（不用点积、相对 d 不再二次）；vs MobileViT-v2 可分离（再去掉 V 交互，换线性变换 T，加可学习全局查询）；vs EfficientFormer（推广到全部阶段 + 卷积替池化）。
- **作用维度/可插入性**：作用于空间维度，通过 q 聚合全局；作为可替换编码器在每阶段堆叠。

## 6. 实验与结果
> 提取缓存覆盖到 3.3 节，实验表格多在后续未覆盖页。以下区分「已确认」与「待核」。
- **已确认（摘要/引言/图 1）**：
    - ImageNet-1K 分类；指标含 top-1、iPhone 14 延迟、参数、FLOPs。
    - 小模型 78.5% top-1 @ 0.8 ms，比 MobileViT-v2 准且快 2×。
    - 大模型 83.0% top-1 @ 1.9 ms。
    - SwiftFormer-L1 较 EfficientFormer-L1 同延迟 +1.7% top-1、无 NAS。
- **待核（据原文后续页，提取缓存未覆盖）**：
    - 检测/实例分割/语义分割的具体数据集（如 COCO/ADE20K）、骨干所接的检测/分割框架、各变体（L1/L3 等）完整对比表与 mAP/mIoU 数值。
    - 消融表数值：深度卷积 vs 池化、各注意力组件、全阶段 vs 仅最后阶段。
- **对比方法**：MobileViT-v2、EfficientFormer、MobileNet 系列、EdgeNeXt、PoolFormer、EdgeViT、GCViT 等（引言/相关工作点名；完整列表待核）。

## 7. 这篇论文真正有价值的地方
1.  **对注意力的极致简化**：证明视觉任务可只保留 query-key 交互、用线性层替代 key-value 交互而不掉精度——为轻量注意力提供新范式。
2.  **工程与理论平衡**：以移动端实际延迟为一等约束，直指「理论降复杂度 ≠ 实际加速」的痛点，并用 0.8 ms 等真实数字验证。
3.  **一致性设计**：注意力贯穿所有阶段对性能与可扩展性都重要，打破「早卷积晚注意力」定式。
4.  **方法论范例**：动机推进清晰、图 2 四注意力并排对比、公式化每个模块（4-7），便于复现与借鉴。

## 8. 局限与问题
1.  评估/宣传集中于分类；检测分割表格未在提取文本中确认，更复杂任务（视频/3D）未涉及。
2.  延迟基于 iPhone 14 ANE，跨硬件可比性存疑。
3.  仅中小规模模型，超大规模未验证。
4.  架构人工设计、无 NAS；未探讨结合 NAS 的潜力。
5.  极低端设备（微控制器）可行性未分析。
6.  单一全局查询 q 是激进低秩近似，对密集预测的无损性需后续页表格佐证。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 贡献列表 + 图 1/2/3。
- **复现**：精读 3.2（公式 4-6 维度：α∈ℝⁿ、q∈ℝ^d、输出 ℝ^{n×d}）与 3.3（公式 7 及两编码器顺序），核对开源代码与变体配置。
- **借鉴创新点**：去 K-V 交互 + 线性替代；加权池化构建全局查询 q；深度卷积替池化且不增延迟。
- **写 Related Work**：归入「高效视觉 Transformer / 移动端轻量注意力」，与 [[MobileViT-v2]]、[[EfficientFormer]]、[[EdgeNeXt]] 并列。

## 10. 和其他论文的关系
- [[MobileViT-v2]]：最直接的对标对象，其可分离自注意力（公式 3）保留 V 交互；SwiftFormer 在此基础上去掉 V 交互并加全局查询机制，且快 2×。
- [[EfficientFormer]]：本文架构基础（4D/3D MetaBlock、PoolFormer 池化混合、仅末阶段 MHSA）；SwiftFormer 升级其 token mixing（卷积替池化）并把注意力推广到所有阶段，同延迟下 +1.7%。
- [[PoolFormer]]：EfficientFormer 局部混合器（平均池化）的来源，本文用深度卷积替换。
- [[EdgeNeXt]]：转置自注意力（跨通道、O(n·d²)）的代表，另一种高效注意力思路，图 2(b) 对比对象。
- EdgeViT / GCViT / Reformer / LinFormer：相关工作中列举的其他高效/稀疏/低秩注意力路线，作为对比背景。

## 11. 关键词
高效加法注意力、移动端视觉、轻量级 Transformer、线性复杂度、全局查询、去除 key-value 交互、一致性混合架构、深度可分离卷积、ImageNet 分类、ICCV 2023、SwiftFormer。

## 12. 可信度说明
本笔记基于提取缓存（12/12 页，但字符级仅前约 25000 字符，覆盖到方法 3.3 节）。摘要、引言、相关工作、整个方法（含公式 1-7、图 2/3 描述）均有原文支撑，已据原文修正乱码标题/会议（ICCV 2023）、清理摘要、对齐公式与模块结构。实验部分：分类关键数字（78.5%/0.8 ms、83.0%/1.9 ms、+1.7%、2×）可确认；检测/分割数据集与框架、消融表数值、各变体命名（如 L3）在提取文本中未出现，已显式标注「据原文后续页，提取缓存未覆盖，待核」，未编造具体数字。

---

> **可信度补充**: PDF 提取质量 = **high**（提取覆盖到方法 3.3 节，公式与模块描述完整；实验表级数值未覆盖，已标注待核）; 来源缓存: `.paper-cache/extracts/SwiftFormerEncoder&ConvEncoder.txt` (12/12 页, 前 25000 字符); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本次优化: 重建摘要、修正乱码 title/venue、对齐公式 4-7 与图 2/3、标注实验待核项。
<!-- AI_READING_NOTE_END -->
