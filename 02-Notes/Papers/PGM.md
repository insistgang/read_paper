---
title: "PromptIR: Prompting for All-in-One Blind Image Restoration"
authors:
  - "Vaishnav Potlapalli"
  - "Syed Waqas Zamir"
  - "Salman Khan"
  - "Fahad Shahbaz Khan"
year: 2023
venue: "NeurIPS 2023 (arXiv:2306.13090, Preprint Under review)"
doi: 
pdf: [[PGM.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
extract_cache: .paper-cache/extracts/PGM.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/18 pages"
---
# PromptIR: Prompting for All-in-One Blind Image Restoration

## 基本信息
- **PDF**: [[PGM.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | PromptIR: Prompting for All-in-One Blind Image Restoration |
| **作者** | Vaishnav Potlapalli; Syed Waqas Zamir; Salman Khan; Fahad Shahbaz Khan |
| **单位** | Mohamed bin Zayed University of AI (MBZUAI); Inception Institute of AI |
| **发表时间** | 2023 |
| **刊物/会议** | NeurIPS 2023 (arXiv:2306.13090v1, 2023-06-22, "Preprint. Under review") |
| **代码** | https://github.com/va1shn9v/PromptIR |
| **DOI** | 未明确 |

## 摘要

> **英文原摘要（据 PDF 提取文本整理）**：Image restoration involves recovering a high-quality clean image from its degraded version. Deep learning-based methods have significantly improved image restoration performance, however, they have limited generalization ability to different degradation types and levels. This restricts their real-world application since it requires training individual models for each specific degradation and knowing the input degradation type to apply the relevant model. We present a prompt-based learning approach, PromptIR, for All-In-One image restoration that can effectively restore images from various types and levels of degradation. In particular, our method uses prompts to encode degradation-specific information, which is then used to dynamically guide the restoration network. This allows our method to generalize to different degradation types and levels, while still achieving state-of-the-art results on image denoising, deraining, and dehazing. Overall, PromptIR offers a generic and efficient plugin module with few lightweight prompts that can be used to restore images of various types and levels of degradation with no prior information on the corruptions present in the image. Our code and pre-trained models are available here: https://github.com/va1shn9v/PromptIR

> **中文翻译**：图像恢复旨在从退化版本中恢复出高质量的干净图像。基于深度学习的方法显著提升了图像恢复性能，但它们对不同退化类型和退化水平的泛化能力有限。这限制了其实际应用，因为它需要为每种具体退化单独训练模型，并且在推理时需要知道输入的退化类型才能选用对应模型。我们提出一种基于提示（prompt）学习的方法 PromptIR，用于"全能型（All-In-One）"图像恢复，能够有效地从多种类型与水平的退化中恢复图像。具体而言，我们的方法用提示来编码退化特定的信息，再用这些信息动态地引导恢复网络。这使得方法能够泛化到不同的退化类型与水平，同时在图像去噪、去雨、去雾任务上仍取得当前最优（SOTA）结果。总体而言，PromptIR 提供了一个通用且高效的即插即用插件模块，仅用少量轻量提示即可恢复多种类型与水平的退化图像，且无需关于图像中所含退化的任何先验信息。代码与预训练模型已开源。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：图像采集时常因相机物理限制或环境条件而引入噪声、模糊、雾霾、雨等退化；图像恢复就是从退化图像中恢复干净图像，因其病态（ill-posed）性质（存在多个可行解）而极具挑战。现有深度学习恢复方法对每种退化类型/水平需训练一份单独的网络副本，且推理时需先知道退化类型来选模型——这对计算受限的移动/边缘设备而言代价高、且不切实际。
- **之前方法的问题**：1）任务特定方法（去噪/去模糊/去雾各自专门设计）缺乏跨退化泛化能力；2）通用架构方法虽隐式学习先验，但仍要为不同退化/水平/数据集训练多份副本；3）全能方法 AirNet [29] 用对比学习训练一个额外编码器来区分退化类型，但难以建模完全解耦的退化表示，且额外编码器带来两阶段训练负担、其效果还高度依赖正负样本对的选取与数据量。
- **核心矛盾**：需要一种既能用**单一模型**盲处理**多种未知退化**、又能**避免复杂训练流程**（对比学习、两阶段训练）、且能**随输入内容动态适应**具体退化的图像恢复方法。
## 关键贡献

1.  提出**基于提示学习的全能型盲恢复框架 PromptIR**：仅依赖输入图像即可恢复干净图像，无需关于退化的任何先验知识（p. 2）。
2.  设计**即插即用、架构无关的提示模块（prompt block）**：可轻松集成进任意现有恢复网络，由**提示生成模块 PGM** 与**提示交互模块 PIM** 构成。PGM 生成富含退化上下文的输入条件提示，PIM 用这些提示引导恢复网络去除退化（p. 2）。
3.  **综合实验验证动态适应行为**：仅用一个统一的 PromptIR 模型，即在图像去噪、去雨、去雾多任务上达到 SOTA（p. 3）。tSNE 可视化（Fig. 2）显示 PromptIR 的退化嵌入比 AirNet 聚类得更好，说明提示 token 能学到更有判别力的退化上下文。
## 方法

**整体框架**：采用基于 Restormer [67] 的 4 级 UNet 式编码器-解码器，编码/解码各级均用若干 Transformer 块，块数从顶层到底层逐渐增加以控制计算量（实现细节给出为 [4, 6, 6, 8]，level-1 至 level-4）。输入退化图 I ∈ R^{H×W×3} 先经一次卷积提取低层特征 F0 ∈ R^{H×W×C}，经 4 级编解码后得到深层特征；编码器逐步降空间分辨率、升通道，得到低分辨率潜在特征 F_l ∈ R^{(H/8)×(W/8)×8C}。核心创新是在**解码器每两个相邻层级之间顺序插入一个提示模块**（共 3 个），在上采样解码过程中动态注入退化信息（p. 3-6, Fig. 3）。

**输入输出**：输入退化图像 I（˜I），输出恢复后的高质量干净图像。

**关键模块——提示模块 (Prompt Block)**：总过程为 ˆF_l = PIM(PGM(P_c, F_l), F_l)（式 1），由 PGM、PIM 两个子模块组成。
- **PGM（提示生成模块）**：
    - **输入**：N 个可学习的提示组件 P_c ∈ R^{N×ˆH×ˆW×ˆC}（实现中 N=5）和解码器某层输入特征 F_l ∈ R^{ˆH×ˆW×ˆC}。
    - **动机**：直接用静态提示标定特征会与输入内容无关、效果次优；PGM 改为**根据输入特征动态预测注意力权重**再加权提示，得到输入条件提示 P，并在提示组件间建立共享空间以促进相关知识共享。
    - **流程**：对 F_l 做空间维全局平均池化 GAP 得向量 v ∈ R^{ˆC}；经通道下采样卷积 + Softmax 得提示权重 w ∈ R^N；用 w 加权提示组件后再过 3×3 卷积，得提示 P。公式（式 2）：P = Conv3×3(Σ_{c=1}^{N} w_i · P_c)，w_i = Softmax(Conv1×1(GAP(F_l)))。为处理推理时不同分辨率，提示组件经**双线性上采样**到与 F_l 相同空间尺寸。
- **PIM（提示交互模块）**：
    - **输入**：PGM 生成的提示 P 和特征 F_l。
    - **流程**：先将 P 与 F_l 沿**通道维拼接**，再送入一个 Transformer 块（直接复用 Restormer [67] 的块，体现"插件、架构无关"），输出 ˆF_l = Conv3×3(GDFN(MDTA[F_l; P]))（式 3）。该 Transformer 块含两个串联子模块：
        - **MDTA（Multi-Dconv head transposed attention）**：在**通道维而非空间维**计算自注意力，复杂度对图像尺寸线性。公式 Y = W_p·V·Softmax(K·Q/α) + X，Q/K/V 由对层归一化输入做 1×1 逐点卷积 + 3×3 深度卷积得到，α 为可学习缩放参数。
        - **GDFN（Gated-Dconv feedforward network）**：通过门控机制抑制低信息特征、只让有用特征传播。公式 Z = W^0_p[ϕ(W^1_d W^1_p(LN(Y))) ⊙ W^2_d W^2_p(LN(Y))] + Y，ϕ 为 GELU。

**训练**：端到端、无需任何组件预训练。L1 损失，Adam（β1=0.9, β2=0.999），学习率 2e-4，训练 200 epochs；训练裁剪 128×128 patch，随机水平/垂直翻转增强。全能设置批大小 32，单任务设置批大小 8（p. 6）。

**推理**：输入退化图过编解码网络；解码阶段 PGM 据输入特征自动算出提示权重、动态生成提示，PIM 引导特征恢复，全程无需用户提供退化类型。

**与 AirNet [29] 的差异**：PromptIR 是**单阶段训练**、概念更简单的 drop-in 模块，**不需要额外的对比学习编码器**，避免了正负样本对选择与两阶段训练；提示模块作为轻量适配器插入现有网络（如 Restormer），架构无关。
## 实验

- **任务与设置**：去雾、去雨、去噪三个代表性任务；遵循 AirNet [29] 设两种设置：(a) All-in-One（合并所有数据训单一统一模型）、(b) Single-task（每任务单独训）。
- **使用的数据集**：
    - **去噪**：训练 BSD400（400 张）+ WED（4,744 张）；从干净图加高斯噪声 σ ∈ {15, 25, 50}；测试 BSD68 与 Urban100。
    - **去雨**：Rain100L（200 训 / 100 测 对）。
    - **去雾**：SOTS（72,135 训 / 500 测）。
    - **全能设置**：合并上述全部数据训一个模型（p. 6）。
- **关键超参（实现细节）**：4 级编解码，Transformer 块 [4, 6, 6, 8]；解码器每两相邻层间 1 个提示块、共 **3 个**；提示组件数 **N=5**（p. 6）。
- **对比方法**：通用恢复方法（BRDNet, LPNet, FDGAN, MPRNet, DL 等）与专门全能方法 AirNet [29]，单任务还含基线 Restormer [67]（p. 6-7, Tables 1-4）。
- **评价指标**：PSNR / SSIM。
- **主实验结果**：
    - **全能设置**（Table 1，平均 PSNR）：PromptIR 比 AirNet 平均高 **0.86 dB**、比第二名 DL 高 2.08 dB。去雾 SOTS 27.94→**30.58**（比 AirNet +2.64 dB）；去雨 Rain100L 34.90→**36.37**（比 AirNet +1.47 dB，比 DL +3.73 dB）；去噪 σ=50 BSD68 比 DL +1.16 dB。注：全能设置去雨 PromptIR 为 36.37（37.04 是单任务数值，勿混淆）。
    - **单任务设置**（Tables 2-4）：去雾 SOTS PromptIR 31.31，比 AirNet（23.18）+**8.13 dB**、比 Restormer（30.87）+0.44 dB；去雨 Rain100L PromptIR 37.04，比 AirNet（34.90）+**2.13 dB**；去噪 Urban100 σ=50 PromptIR 29.39，比 AirNet（28.88）+**0.51 dB**。
- **定性结果**：Figs. 4-6（全能去雾/去雨/去噪），附录 Figs. C.1-C.3（单任务去雾/去雨/去噪 σ=50）显示比 AirNet 视觉更优。
- **消融实验**：提取缓存仅覆盖 p.1-12，正文未含消融；据原文后续页线索，附录 A 含两项消融——退化嵌入对比（Table A.1：PGM 提示 vs 对比学习退化编码器嵌入）、仅解码器加提示块 vs 编解码均加（Table A.2）。（据原文后续页，提取缓存未覆盖，待核）
- **效率信息（参数量 / FLOPs / 速度）**：提取文本未明确给出 PromptIR 的具体参数量、计算量与推理速度对比。（据原文后续页，提取缓存未覆盖，待核）
## 局限

- **方法局限性**：提示模块虽宣称架构无关，但本文实例化与验证均绑定在 Restormer 的 Transformer 块（MDTA+GDFN）上，对纯 CNN 或其他架构的有效性未经实验验证。
- **实验充分性**：提取文本（p.1-12）未含消融与效率分析；提示块引入的额外计算（PGM 的注意力权重 + PIM 的 Transformer 块）对推理速度/显存的影响在可见文本中未量化。（据原文后续页，附录 A 含消融，提取缓存未覆盖，待核）
- **数据集与任务**：实验仅覆盖去噪、去雨、去雾三类退化；对混合退化、真实世界退化、运动/散焦模糊等更复杂退化的泛化未评估。
- **复现**：代码与预训练模型开源（GitHub），复现风险较低；关键超参（[4,6,6,8] 块数、3 提示块、N=5 提示组件、L1、200 epoch、128 patch）已在正文给出。
## 个人评论

> 以下为 AI 阅读评论，非论文原文结论。

1.  **把"提示学习"从高层视觉引入低层视觉的范式**：NLP / 高层视觉里的可学习提示通常用于冻结大模型的参数高效微调；本文把它落到图像恢复这一低层任务，且关键创新在于提示不是静态的，而是**由输入特征动态加权生成（input-conditioned）**——这正是它能"盲"适应未知退化的关键。这一"轻量、可学习、内容触发的上下文注入"机制对超分、去模糊、图像修复等其他低层任务有迁移价值。
2.  **极简的即插即用设计**：提示块只做"GAP→权重→加权提示→通道拼接→复用现成 Transformer 块"，不改主干、不新增对比学习编码器、单阶段端到端，却拿下三任务 SOTA。相比 AirNet 的两阶段对比学习，这是一种"用更少机制换更好结果"的思路，工程落地性强。
3.  **统一多任务建模的隐式路线**：不显式解耦退化、不显式分类退化类型，而是让输入特征隐式触发对应提示，是一条比"显式判别退化再选分支"更简单的统一建模路径；tSNE 聚类更优的证据也支持该隐式机制确实学到了判别性退化上下文。
4.  **可质疑点**：PIM 直接复用 Restormer 块，"架构无关"目前更多是论断而非实证；提示组件数 N=5、提示块数 3 等设计是否最优，需附录消融（提取缓存未覆盖）来支撑。

### 使用建议

- **快速了解**：读摘要、引言（第1节）、Fig. 1（总体思想）与 Fig. 3（框架），即可掌握核心。
- **复现**：精读第3节方法（式 1/2/3）与第4节实现细节（[4,6,6,8] 块、3 提示块、N=5、L1、Adam 2e-4、200 epoch、128 patch、批 32/8）及数据集准备，结合开源代码。
- **借鉴创新点**：重点学"输入条件动态提示生成（PGM）"与"提示通道拼接 + 复用注意力块（PIM）"的即插即用模块化思路，可迁移到 Uformer/SwinIR 等其他恢复网络或其他任务。
- **写 related work**：可归入 1）图像恢复/增强；2）提示学习/适配器在视觉中的应用；3）多任务/全能型恢复；4）基于 Transformer 的图像处理。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的**低层视觉 / 图像恢复（Image Restoration）**方向，具体聚焦"**全能型（All-in-One）盲图像恢复**"——用一个统一模型处理多种未知类型与水平的退化（去噪、去雨、去雾）。因此最贴切的主题是 **E_图像复原_超分_去噪_去雨去雾**。（说明：本文的提示块内部确实复用了 Restormer 的通道注意力 MDTA，因而与"注意力算子模块"有交集，但论文的任务域、数据集、指标、对比对象全部围绕图像复原展开，故归 E 类更准确，而非 B_注意力算子模块。）

## 2. 一句话总结
PromptIR 用一个**输入条件、可学习的即插即用提示块**（PGM 生成提示 + PIM 用提示引导恢复），在不改主干、不用对比学习、单阶段训练的前提下，用一个统一模型在去噪、去雨、去雾上达到 SOTA，且推理时无需知道退化类型。

## 3. 背景与问题
- **为什么要做**：噪声、模糊、雾、雨等退化在采集时不可避免；现有深度方法对每种退化/水平要训一份单独网络，推理还需先知道退化类型来选模型，对移动/边缘设备代价高、不实际。
- **之前方法的问题**：1）任务特定方法不跨退化泛化；2）通用架构仍需训多份副本；3）全能方法 AirNet[29] 用对比学习训额外编码器区分退化，难以建完全解耦表示，且两阶段训练负担重、依赖正负样本对选取与数据量。
- **核心矛盾**：要"单模型 + 盲处理多种未知退化 + 避免复杂训练 + 内容自适应"四者兼得。

## 4. 核心贡献
1.  提示学习驱动的全能盲恢复框架 PromptIR，仅靠输入图像、无退化先验即可恢复（p. 2）。
2.  即插即用、架构无关的提示块 = PGM（生成输入条件提示）+ PIM（用提示引导恢复），可集成进任意现有恢复网络（p. 2）。
3.  统一单模型在去噪/去雨/去雾三任务上 SOTA；tSNE（Fig. 2）显示其退化嵌入比 AirNet 聚类更好（p. 3）。

## 5. 方法详解
**整体框架**：基于 Restormer 的 4 级 UNet 编解码，各级用若干 Transformer 块、块数自顶向下递增（[4,6,6,8]）。输入 I∈R^{H×W×3} 先卷积得 F0∈R^{H×W×C}，编码到低分辨率潜在 F_l∈R^{(H/8)×(W/8)×8C}，解码恢复高分辨率。**解码器每两相邻层间插一个提示块，共 3 个**，在解码时动态注入退化信息（p. 3-6, Fig. 3）。

**提示块**：ˆF_l = PIM(PGM(P_c, F_l), F_l)（式 1）。
- **PGM**：输入 N=5 个可学习提示组件 P_c∈R^{N×ˆH×ˆW×ˆC} 与特征 F_l。动机是静态提示与输入无关、次优，故据输入动态预测注意力权重再加权。流程：GAP(F_l)→v；过通道下采样 1×1 卷积 + Softmax→权重 w∈R^N；加权提示组件后过 3×3 卷积得 P。式 2：P=Conv3×3(Σ w_i·P_c)，w_i=Softmax(Conv1×1(GAP(F_l)))。推理多分辨率时用**双线性上采样**把提示组件放到与 F_l 同尺寸。
- **PIM**：把 P 与 F_l **沿通道拼接**，过 Restormer 的 Transformer 块得 ˆF_l=Conv3×3(GDFN(MDTA[F_l;P]))（式 3）。MDTA 在**通道维**做自注意力、线性复杂度（Y=W_p V·Softmax(K·Q/α)+X，Q/K/V 由 1×1 逐点卷积 + 3×3 深度卷积得到，α 可学习）；GDFN 用门控（GELU ϕ + 逐元素相乘）抑制低信息特征。论文强调直接复用现成块以体现"插件、架构无关"。

**训练**：端到端、无组件预训练；L1 损失，Adam(0.9,0.999)，lr 2e-4，200 epoch，128×128 patch，随机水平/垂直翻转；批大小全能 32 / 单任务 8（p. 6）。

**与 AirNet 差异**：单阶段、无对比学习编码器、drop-in 模块，概念更简单。

## 6. 实验与结果
- **数据集**：去噪 BSD400(400)+WED(4744) 训、测 BSD68/Urban100，σ∈{15,25,50}；去雨 Rain100L(200/100)；去雾 SOTS(72135/500)；全能=四者合并（p. 6）。
- **超参**：4 级 [4,6,6,8] 块、3 提示块、N=5 提示组件。
- **对比**：BRDNet/LPNet/FDGAN/MPRNet/DL 等通用法 + AirNet[29] 全能法 + 单任务基线 Restormer[67]。
- **指标**：PSNR/SSIM。
- **全能（Table 1，平均 PSNR）**：PromptIR 比 AirNet +**0.86 dB**、比 DL +2.08 dB；去雾 27.94→30.58（+2.64 dB）；去雨 34.90→36.37（+1.47 dB，比 DL +3.73 dB）；σ=50 去噪比 DL +1.16 dB。（注意：全能去雨是 36.37，单任务才是 37.04。）
- **单任务（Tables 2-4）**：去雾 SOTS 31.31，比 AirNet(23.18) +**8.13 dB**、比 Restormer(30.87) +0.44 dB；去雨 Rain100L 37.04，比 AirNet(34.90) +**2.13 dB**；去噪 Urban100 σ=50 29.39，比 AirNet(28.88) +**0.51 dB**。
- **定性**：Figs. 4-6 与附录 Figs. C.1-C.3 视觉优于 AirNet。
- **消融**：提取缓存仅 p.1-12，正文无消融；据原文后续页线索，附录 A 有两项（PGM 提示 vs 对比学习退化嵌入 Table A.1；仅解码器提示 vs 编解码均加 Table A.2）（提取缓存未覆盖，待核）。
- **效率**：参数量/FLOPs/速度在可见文本中未明确（提取缓存未覆盖，待核）。

## 7. 这篇论文真正有价值的地方
1.  **把"内容触发的动态提示"引入低层视觉**：提示不是静态查表，而是由输入特征 GAP→Softmax 权重动态合成，这是"盲"适应未知退化的核心机理，可迁移到超分、去模糊、修复等任务。
2.  **极简即插即用、单阶段**：不改主干、不加对比学习编码器、复用现成 Transformer 块，却三任务 SOTA——"用更少机制换更好结果"，工程落地友好。
3.  **统一多任务的隐式路线**：不显式判别退化类型/解耦表示，靠输入隐式触发对应提示；tSNE 聚类更优佐证其确实学到判别性退化上下文。

## 8. 局限与问题
- **方法**：声称架构无关，但仅在 Restormer 块上实例化/验证；纯 CNN 等架构未实证。
- **实验**：可见文本（p.1-12）无消融与效率分析；提示块额外计算开销未量化（据原文后续页附录 A 有消融，提取缓存未覆盖，待核）。
- **任务范围**：仅去噪/去雨/去雾，未评估混合退化、真实世界退化、模糊等。
- **复现**：代码与预训练模型开源，关键超参齐全，复现风险低。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + Fig. 1/Fig. 3。
- **复现**：第3节式 1/2/3 + 第4节实现细节（[4,6,6,8]、3 提示块、N=5、L1、Adam 2e-4、200 epoch、128 patch、批 32/8）+ 开源代码。
- **借鉴创新点**：PGM 动态提示生成 + PIM 通道拼接复用注意力块的模块化思路，迁移到 Uformer/SwinIR 等。
- **写 related work**：图像恢复/增强、提示学习/适配器、全能型恢复、基于 Transformer 的图像处理。

## 10. 和其他论文的关系
- [[Restormer]]：PromptIR 的主干，其高效通道注意力 MDTA 与 GDFN 被直接用于 PIM 的 Transformer 块；单任务表中也是强基线。
- [[SwinIR]]：另一基于 Transformer 的高效恢复网络（窗口自注意力），论文称提示块理论上也可用于此类架构。
- [[AirNet]]：本文主要对比的全能方法，用对比学习训退化编码器；PromptIR 旨在用更简单的提示学习方案超越它。
- **Visual Prompting / 视觉提示学习**：更广义地将提示用于视觉任务的工作，PromptIR 是其在低层视觉的具体落地。

## 11. 关键词
图像恢复, 全能型恢复, 盲恢复, 提示学习, 输入条件提示, 提示生成模块 PGM, 提示交互模块 PIM, 即插即用插件, Restormer, MDTA, GDFN, UNet, Transformer, 去噪, 去雨, 去雾, 多任务统一

## 12. 可信度说明
本精读笔记主要基于 PDF 提取文本的前 12 页（提取缓存标注 12/18 页，max_chars 25000，原文 41118 字符仅展示前 25000）。这些页覆盖了摘要、引言、相关工作、完整方法（含式 1/2/3 与 Fig. 3）、实验设置与主结果（Tables 1-4、Figs. 4-6）。笔记中所有方法描述、公式、数据集与 PSNR/SSIM 数值均严格来自该文本并标注页码。由于可见文本不含 p.13-18，关于**消融实验（附录 A 的 Table A.1/A.2）、Transformer 块图示（附录 B）、更多定性结果（附录 C）以及参数量/FLOPs/速度等效率信息**仅据原文后续页线索标注，标记为"提取缓存未覆盖，待核"。

---

> **可信度补充**: PDF 提取质量 = **high** (提取缓存 12/18 页, 约 2086 字符/页, 主方法与主结果完整); 来源缓存: `.paper-cache/extracts/PGM.txt`; 原 AI 主体覆盖 p.1-12 + 全文补读记录覆盖 p.13-18 线索; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。本轮据提取文本重核: 修复 frontmatter 标题/作者/venue 乱码, 重建摘要, 补 N=5 提示组件与 [4,6,6,8] 块配置, 厘清全能去雨 36.37 vs 单任务 37.04, primary_topic 由 B_注意力算子模块 改为 E_图像复原_超分_去噪_去雨去雾。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-18; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-18。
- **提取情况**: 缺失页 6 页, 其中 6 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: Appendix
- p.14: A Additional Ablation Studies
- p.14: We conduct further ablation studies to illustrate the effectiveness of various design choices of the
- p.14: PGM module with embeddings extracted from the Contrastive- learning based Degradation Encoder
- p.14: Method Dehazing Deraining Denoising on BSD68 dataset [41]) Average
- p.14: We study the importance of decoder-only prompting by evaluating the usage of prompt blocks on
- p.14: B Transformer Block in PromptIR Framework
- p.16: C Qualitative results:
- p.16: We present more qualitative results from single-task models to further elucidate the effectiveness of

### 缺失页关键摘录

- p.14: We conduct further ablation studies to illustrate the effectiveness of various design choices of the
- p.14: Table A.1: Comparisons under all-in-one setting: between the usage of degradation embedding
- p.14: Method Dehazing Deraining Denoising on BSD68 dataset [41]) Average
- p.14: Table A.2: Comparisons under the all-in-one setting: between the usage of the Prompt-block on both
- p.15: Figure B.1: Overview of the Transformer block used in the PromptIR framework. The Transformer
- p.16: Figure C.1: Image deraining comparisons under single task setting on images from the SOTS
- p.16: dataset [31]. Our method effectively removes haze to produce visually better images.
- p.17: Figure C.2: Image deraining comparisons under single task setting on images from the Rain100L
- p.17: dataset [16]. Our method effectively removes rain streaks to generate rain-free images.
- p.18: Figure C.3: Image deraining comparisons under single task setting on images from the URBAN100
- p.18: dataset [ 22] with σ= 50 . Our method produces visually better images as compared to previous
<!-- AI_READING_NOTE_END -->
