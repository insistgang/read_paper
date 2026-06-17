---
title: "GRFormer: Grouped Residual Self-Attention for Lightweight Single Image Super-Resolution"
authors:
  - "Yuzhen Li"
  - "Zehang Deng"
  - "Yuxin Cao"
  - "Lihua Liu"
year: 2024
venue: "ACM MM '24 (32nd ACM International Conference on Multimedia)"
doi: 10.1145/3664647.3681554
pdf: [[GRSA.pdf]]
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
extract_cache: .paper-cache/extracts/GRSA.txt
---

# GRFormer: Grouped Residual Self-Attention for Lightweight Single Image Super-Resolution

## 基本信息
- **PDF**: [[GRSA.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | GRFormer: Grouped Residual Self-Attention for Lightweight Single Image Super-Resolution |
| **作者** | Yuzhen Li (Tsinghua); Zehang Deng* (Swinburne, 通讯作者); Yuxin Cao (NUS); Lihua Liu (UIBE) |
| **发表时间** | 2024 |
| **刊物/会议** | ACM MM '24 (第 32 届 ACM 国际多媒体会议), 2024-10-28~11-01, Melbourne, VIC, Australia |
| **DOI** | 10.1145/3664647.3681554 |
| **预印本/代码** | arXiv:2408.07484v1 [cs.CV] (2024-08-14); 代码 https://github.com/sisrformer/GRFormer |

## 摘要

**英文原摘要（据 PDF 提取文本整理，已修复空格/连字符断裂、剔除杂入的版式数字）**

> Previous works have shown that reducing parameter overhead and computations for transformer-based single image super-resolution (SISR) models (e.g., SwinIR) usually leads to a reduction of performance. In this paper, we present GRFormer, an efficient and lightweight method, which not only reduces the parameter overhead and computations, but also greatly improves performance. The core of GRFormer is Grouped Residual Self-Attention (GRSA), which is specifically oriented towards two fundamental components. Firstly, it introduces a novel grouped residual layer (GRL) to replace the Query, Key, Value (QKV) linear layer in self-attention, aimed at efficiently reducing parameter overhead, computations, and performance loss at the same time. Secondly, it integrates a compact Exponential-Space Relative Position Bias (ES-RPB) as a substitute for the original relative position bias to improve the ability to represent position information while further minimizing the parameter count. Extensive experimental results demonstrate that GRFormer outperforms state-of-the-art transformer-based methods for ×2, ×3 and ×4 SISR tasks, notably outperforming SOTA by a maximum PSNR of 0.23dB when trained on the DIV2K dataset, while reducing the number of parameter and MACs by about 60% and 49% in only self-attention module respectively. We hope that our simple and effective method that can easily applied to SR models based on window-division self-attention can serve as a useful tool for further research in image super-resolution.

**中文翻译**

> 已有研究表明，对基于 Transformer 的单图像超分辨率（SISR）模型（如 SwinIR）削减参数开销与计算量，通常会带来性能下降。本文提出 GRFormer——一种高效轻量的方法，不仅降低参数开销与计算量，还显著提升性能。GRFormer 的核心是分组残差自注意力（GRSA），它围绕两个基础组件展开：其一，引入新颖的分组残差层（GRL）替代自注意力中的 Query/Key/Value（QKV）线性层，在同一步内高效削减参数、计算量与性能损失；其二，集成紧凑的指数空间相对位置偏置（ES-RPB）替代原始相对位置偏置，在进一步压缩参数量的同时提升位置信息的表达能力。大量实验表明，GRFormer 在 ×2、×3、×4 三个 SISR 任务上均优于当时最先进的 Transformer 方法——在 DIV2K 上训练时最大 PSNR 提升达 0.23dB，同时仅自注意力模块内的参数与 MACs 分别降低约 60% 与 49%。该方法简单有效、可便捷迁移到基于窗口划分自注意力的 SR 模型，期望能成为超分研究的有用工具。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：CNN 与 Transformer 类 SR 模型常靠堆层数、增维度来提性能，代价是参数与计算量上涨。作者由此提出核心问题：**能否在为基于 Transformer 的 SR 模型削减参数与计算的同时提升性能？**（原文 Introduction）。围绕这一问题，作者把自注意力拆成三个子问题：
    - **RQ1**：自注意力内部是否存在冗余？
    - **RQ2**：自注意力的表达能力能否进一步增强？
    - **RQ3**：是否存在比相对位置偏置（RPB）更好的位置信息表示方案？
- **之前方法的问题**：
    1. 已有工作虽观察到自注意力层存在冗余，但其方案主要集中在缩小注意力窗口（RQ1 的现有应对不足）。
    2. 以往 Transformer SR 仅在自注意力**外层**用残差学习，没有把残差引入 QKV 线性层内部（RQ2 的切入点）。
    3. 原始 RPB 有**四个致命缺陷**（原文逐条列出）：① 窗口为 H×W 时 RPB 参数量为 (2H-1)×(2W-1)，开销巨大；② 为窗口内每个位置单独设参数，既冗余又易受训练噪声干扰（Fig.2(a) 中可见许多细微抖动）；③ 每个参数独立训练，忽略不同位置权重间的相对关系；④ 未能直观反映"重建图像时近像素往往比远像素更重要"的先验。
- **核心矛盾**：**模型效率（参数量、MACs）与重建性能（PSNR）之间的权衡**。作者意在打破该权衡，做到"既轻量又高性能"。

## 关键贡献

1. 提出**分组残差自注意力（GRSA）**，可无缝替换其他 Transformer-based SR 模型中的自注意力模块及其变体；**仅在自注意力模块内**即可减少约 **60% 参数**与约 **49% MACs**。
2. GRSA 由三种手段构成两个基础组件：
    - **分组残差层（GRL）**——含两部分：①「QKV 线性层的分组方案」削减参数与计算（解决 RQ1）；②「QKV 线性层的残差」把训练空间从线性空间变到残差空间以补偿分组带来的性能损失（解决 RQ2）。
    - **指数空间相对位置偏置（ES-RPB）**——替代原始 RPB，用指数映射强制注意力对像素距离敏感、用小型 MLP 抑制训练噪声（解决 RQ3）。
3. 基于 GRSA 构建轻量级超分网络 **GRFormer**。
4. 在五个常用基准数据集上的大量实验显示，GRFormer 在 ×2/×3/×4 上多数数据集大幅超越以往轻量级 SISR 方法；在 DIV2K 上训练时**最大 PSNR 提升 0.23dB**（Fig.1 标题另称 ×4 任务上较 SOTA 提升 0.19dB），整体模型参数较 SwinIR（1000k 参数）约减少 **20%**。

## 方法

- **整体框架**（Fig.3，三部分）：
    - **浅层特征提取**：一个 3×3 卷积 `L_SF` 把 LR 图 `I_LR ∈ R^{H×W×C_in}` 映到浅层特征 `X_0 ∈ R^{H×W×C}`（公式 1）。
    - **深层特征提取**：N 个 GRSAB Group（每组含 M 个 GRSAB 块 + 末端 3×3 卷积），组内末端卷积输出与组输入做残差（公式 2、3）。
    - **图像重建**：一个 3×3 卷积做特征聚合后，深浅特征相加，再经 PixelShuffle 上采样得到 `I_HR ∈ R^{H×W×C_out}`（公式 4）。
- **关键模块**：
    - **GRSAB（分组残差自注意力块）**：含 GRSA 与 FFN 两个核心子模块，均采用"先模块、后 LayerNorm、再残差"的结构：`I_GRSA = Norm(L_GRSA(I_in)) + I_in`（公式 5）；`I_out = Norm(L_FFN(I_GRSA)) + I_GRSA`（公式 6）。
    - **GRSA（公式 7、8）**：输入 `X` 经三个 GRL 模块 `L_GRL_Q / L_GRL_K / L_GRL_V` 得到 Q、K、V；对 Q、K 先 Normalize，算 `Q*K^T` 得相似度，乘可训练缩放因子 `λ`，加 ES-RPB 偏置 `B_ES-RPB`，再 Softmax 后与 V 相乘；若用多头自注意力，最后用一个**分组线性层** `L_proj` 把多头投影回单头。即 `GRSA = L_proj( Softmax( λ·Normalize(Q) * Normalize(K)^T + B_ES-RPB ) V )`。
    - **GRL（分组残差层，公式 9）**：作为 QKV 线性层的替代，把输入 `X ∈ R^{H×W×C}` 沿通道维**均分为两份** `X_in1, X_in2`；各自经一个独立线性层后与自身相加（残差），即 `X_out1 = L_Linear1(X_in1) + X_in1`、`X_out2 = L_Linear2(X_in2) + X_in2`；最后在通道维拼接成 `X_out`。其中 `X_in1, X_in2, X_out1, X_out2 ∈ R^{H×W×(C/2)}`。设计动机：分组削减参数与计算，残差把 QKV 投影的训练空间从线性空间变到残差空间以增强特征学习能力。
    - **ES-RPB（公式 10）**：把绝对位置坐标的横、纵坐标差 ΔX、ΔY 从线性空间映到指数空间——`Δ̂X = sign(ΔX)·(1 - exp(-|α·ΔX|))`、`Δ̂Y = sign(ΔY)·(1 - exp(-|β·ΔY|))`，再送入小型 MLP 得 `B_ES-RPB = MLP(Δ̂X, Δ̂Y)`。其中 α、β 为**可训练的距离敏感因子**，控制参考像素与同窗口其他像素间的距离敏感度；MLP 由"两个线性层 + 中间一个激活层"构成。指数映射强制"近像素权重更大"，MLP 拟合所有坐标映射以抗噪、易训练、参数更少。
- **GRL 有效性的数学解释（Section 3.6）**：
    - **效率**：设输入特征数为 N，标准线性层的参数与 MACs 均为 N²；分组成两半、各用输入数为 N/2 的线性层后，两层合计参数与 MACs 仅为 N²/2 ——**分组把参数与 MACs 减半**。
    - **不削弱特征聚合**：担心分组导致两组特征缺乏交互。作者论证至少对 Q、K 这种担忧不必要——把 `X ∈ R^{N×C}` 切成 2×2 块、把两个分组线性层的参数矩阵打包成一个，做 `X` 与 Q/K 投影矩阵的乘积（公式 11、12）后，`QK^T` 的每个子块都会**深度聚合两组特征**，从而弥补分组可能造成的信息隔离。
- **论文类型特化（注意力类）**：
    - **作用维度**：**窗口内**的空间自注意力（window-division self-attention）。
    - **可插入性**：GRSA 被设计为通用即插即用模块，可直接替换 SwinIR 等模型的自注意力模块及其变体。
    - **计算量 vs 效果**：GRL 的分组把 QKV 投影参数/计算理论减半，残差与 ES-RPB 用来补偿并提升性能，实现效率与效果的更好平衡。

## 实验

- **数据集**：训练集 DIV2K；测试集为五个常用基准 Set5、Set14、B100、Urban100、Manga109。
- **评价指标**：PSNR、SSIM 衡量重建质量；#Params、#MACs（MACs 在上采样到 **1280×720** 空间分辨率的图上计算）衡量效率；另用 #Weighted-Avg（按各数据集图像数加权的平均 PSNR/SSIM，`Weighted-Avg = Σ_{i=1}^{5} M_i × Score_i`，M 为图像数）做综合比较（Table 1 标题）。
- **对比方法**（Table 1 / 定性图 Fig.4）：CNN 类 EDSR-baseline、CARN、LatticeNet；Transformer 类 SwinIR-light、SwinIR-NG，以及 SRFormer、HPINet。
- **主结果（提取覆盖部分）**：原文正文称 ×2 任务下 GRFormer 在 Urban100 上取得 **33.17 PSNR**，高于 SwinIR-light（32.76）与当时 SOTA 轻量模型（32.94），且该提升在 ×3、×4 上同样存在。Table 1 的 ×2 行（提取可见部分）给出对比基线数值，例如 SwinIR-light（910K 参数 / 207.5G MACs，Urban100 32.76/0.9340）、SwinIR-NG（1181K / 210.7G，Urban100 32.78/0.9340）。
- **效率结果**：整体模型参数较 SwinIR（1000k 参数、同超参）约减 **20%**；仅自注意力模块内参数减约 **60%**、MACs 减约 **49%**。
- **(据原文后续页，提取缓存未覆盖，待核)** 提取文本在 Table 1 的 ×2 部分（截至 SwinIR-NG 一行）被截断，**GRFormer 自身在 Table 1 中的完整数值、×3/×4 的逐数据集结果、消融实验、训练细节（学习率/迭代步数/优化器等）均不在提取范围内**，需回原 PDF（共 9 页 / 47154 字符，提取仅含前 ~25000 字符）核对。
- **推理速度**：提取文本未给出 FPS/实际推理时间数据（论文是否在后续页提供待核）。

## 局限

1. **分组方式固定**：GRL 是简单的通道二等分 + 两条线性支路，固定二分组未必最优；论文也未讨论更细/更多分组的取舍（提取文本未涉及）。
2. **ES-RPB 的形式约束**：指数映射 `1-exp(-|α·Δ|)` 是一种特定的距离衰减建模，α、β 仅控制单向敏感度，可能不适配所有窗口尺寸与任务的位置先验。
3. **实验范围**：聚焦轻量级 SISR；在大容量/高分辨率模型或非超分任务上，分组带来的参数收益是否同样显著，PDF 未给出（待核后续页）。
4. **退化模式简单**：基准集多为双三次下采样的合成退化，真实世界复杂退化下的泛化能力需进一步验证（论文未涉及）。
5. **效率口径**：报告的是 MACs 与参数量的理论削减，提取文本未见实际推理时延/FPS，理论计算下降未必等比转化为实测加速（取决于硬件与实现）。

## 个人评论

1. **问题—方案的对称性**：论文把"减参—补性能—改位置"拆成 RQ1/RQ2/RQ3，再用分组（GRL 的分组）、残差（GRL 的残差）、ES-RPB 三招一一回应，结构清晰、动机可追溯，是值得借鉴的"分析问题→对称给方案"范式。
2. **把残差下沉到 QKV 内部**：以往 SR Transformer 只在自注意力外层用残差，本文把残差直接加进 QKV 线性层、并配合分组使用，是个小而务实的结构改动——既补偿分组的容量损失，又不引入额外参数。
3. **用先验约束位置偏置**：ES-RPB 把"近像素更重要"这一视觉先验显式编码进指数映射，再用小 MLP 平滑拟合，替代了原 RPB 中逐位置独立、易抖动的参数。这是"领域知识参数化"的好例子。
4. **为经验设计补理论**：Section 3.6 用 2×2 分块矩阵乘法论证"分组不会削弱 QK 的特征聚合"，给经验性结构提供了形式化支撑，提升了说服力——但论证只覆盖 Q、K，对 V 分组的影响未展开。
5. **可迁移性是最大卖点**：GRSA 强调能直接替换 SwinIR 及其变体的自注意力，这让该工作的价值不止于 GRFormer 一个网络，而是一个可移植的算子级改进。

### 使用建议

- **快速了解**：读 Abstract、Introduction 的 RQ1–RQ3、Method 3.3（GRSA 概述）、以及 Table 1 与对应分析。
- **复现**：精读 Method 3.1（整体架构，公式 1–4）、3.2（GRSAB，公式 5–6）、3.3（GRSA，公式 7–8）、3.4（GRL，公式 9）、3.5（ES-RPB，公式 10），对照 Fig.3；尤其注意 GRL 的"二等分 + 残差 + 拼接"和 ES-RPB 的 `sign·(1-exp)` 映射与 MLP 结构。代码见官方仓库。
- **借鉴创新点**：把 GRL（分组 + 残差）思想迁到其他视觉 Transformer 的 QKV 投影；把 ES-RPB 的"先验→参数化函数→位置偏置"路线用到需要显式位置建模的任务。
- **写 related work**：可归入"轻量级超分辨率网络"或"高效视觉 Transformer / 注意力机制"。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的**图像超分辨率**方向，聚焦**轻量级单图像超分（SISR）**，目标是在显著压缩基于 Transformer 的超分模型（以 SwinIR 为基线）参数与计算的同时提升重建性能。其核心产出是一种新的注意力算子——**分组残差自注意力（GRSA）**，可即插即用替换现有 Transformer SR 的自注意力模块。因此放在 **"B_注意力算子模块"** 主题下最贴切（论文创新落点在注意力算子本身，而非超分网络结构或数据集）。

## 2. 一句话总结
本文提出**分组残差自注意力（GRSA）**：用"分组 + 残差"的 GRL 替换 QKV 线性层、用"指数空间映射 + 小 MLP"的 ES-RPB 替换相对位置偏置，在轻量级 SISR 上同时实现参数/计算量大幅下降与性能提升。

## 3. 背景与问题
- **驱动问题**：CNN/Transformer SR 靠堆层增维提性能，参数与计算随之膨胀；作者问"能否对 Transformer SR 边减参减算、边提性能？"，并细化为三问：
    - RQ1 自注意力是否有冗余？
    - RQ2 自注意力的表达力能否再增强？
    - RQ3 有无比 RPB 更好的位置信息表示？
- **既有方法不足**：① 已有冗余研究多只缩小注意力窗口；② 残差仅用于自注意力外层、未进 QKV 内部；③ 原始 RPB 有四个致命缺陷——参数量 (2H-1)×(2W-1) 过大、逐位置设参既冗余又易受训练噪声（Fig.2(a) 抖动）、各参数独立训练忽略位置间相对关系、未能反映"近像素更重要"的先验。
- **核心矛盾**：效率（#Params、#MACs）与重建质量（PSNR）的权衡，作者意在打破它。

## 4. 核心贡献
1. **GRSA**：可无缝替换其他 Transformer SR 的自注意力模块及变体，仅模块内即减约 60% 参数、约 49% MACs。
2. 由三招构成两个组件：GRL 的「分组方案」（解 RQ1）、GRL 的「QKV 残差」（解 RQ2）、**ES-RPB**（解 RQ3）。
3. 基于 GRSA 搭建轻量超分网络 **GRFormer**。
4. 五基准上大量实验，多数数据集大幅领先以往轻量 SISR；DIV2K 训练时最大 PSNR +0.23dB（Fig.1 称 ×4 较 SOTA +0.19dB），整体参数较 SwinIR（1000k）约减 20%。

## 5. 方法详解
- **整体架构（Fig.3）**：3×3 卷积浅层提特征（公式 1）→ N 个 GRSAB Group（每组 M 个 GRSAB + 末端 3×3 卷积 + 组残差，公式 2/3）→ 3×3 卷积聚合 + 深浅特征相加 + PixelShuffle 上采样（公式 4）。`I_LR ∈ R^{H×W×C_in} → I_HR ∈ R^{H×W×C_out}`。
- **GRSAB（公式 5/6）**：GRSA 与 FFN 两子模块，均为"模块 → LayerNorm → 残差"。
- **GRSA（公式 7/8）**：X 经三个 GRL 得 Q/K/V；Q、K 先 Normalize，`λ·Normalize(Q)*Normalize(K)^T + B_ES-RPB` 后 Softmax 再乘 V；多头时末端用分组线性层 `L_proj` 投影回单头。
- **GRL（公式 9）**：通道维二等分 `X_in1,X_in2`；各经独立线性层并加残差 `X_out{i}=L_Linear{i}(X_in{i})+X_in{i}`；通道拼接得 `X_out`。各子张量 ∈ R^{H×W×(C/2)}。分组减参、残差换到残差空间增强学习。
- **ES-RPB（公式 10）**：`Δ̂X=sign(ΔX)(1-exp(-|α·ΔX|))`、`Δ̂Y=sign(ΔY)(1-exp(-|β·ΔY|))`、`B_ES-RPB=MLP(Δ̂X,Δ̂Y)`；α、β 为可训练距离敏感因子；MLP = 两线性层夹一激活层。指数映射强制近像素权重大，MLP 平滑抗噪、参数少。
- **3.6 有效性证明**：① 效率——标准线性层参数/MACs 为 N²，二分组后为两条 N/2 输入的线性层共 N²/2，**减半**；② 不损聚合——把 X 切成 2×2 块、Q/K 投影矩阵打包（公式 11/12），`QK^T` 各子块深度融合两组特征，论证至少对 Q、K 而言分组不削弱交互。
- **类型特化**：窗口内空间自注意力；通用可插拔；以分组换效率、以残差+ES-RPB 保/提性能。

## 6. 实验与结果
- **数据集**：训练 DIV2K；测试 Set5/Set14/B100/Urban100/Manga109。
- **指标**：PSNR、SSIM；#Params；#MACs（在上采样到 1280×720 的图上算）；#Weighted-Avg（按各集图像数加权，`Σ M_i×Score_i`）。
- **对比**：EDSR-baseline、CARN、LatticeNet（CNN）；SwinIR-light、SwinIR-NG、SRFormer、HPINet（Transformer）。
- **可核结果（提取覆盖）**：正文称 ×2 时 GRFormer 在 Urban100 取 33.17 PSNR，高于 SwinIR-light(32.76) 与 SOTA 轻量模型(32.94)，并称该优势延伸到 ×3/×4。Table 1 ×2 可见行示例：SwinIR-light 910K/207.5G、Urban100 32.76/0.9340；SwinIR-NG 1181K/210.7G、Urban100 32.78/0.9340。
- **效率**：整体参数较 SwinIR(1000k) 约减 20%；仅自注意力模块参数减约 60%、MACs 减约 49%。
- **(据原文后续页，提取缓存未覆盖，待核)**：提取文本在 Table 1 的 ×2 段（截至 SwinIR-NG 行）截断。**GRFormer 在 Table 1 的完整逐数据集数值、×3/×4 全部结果、消融实验、训练细节、定量推理速度均未进入提取**，需回 PDF 核对。Fig.4 给出 Urban100 上 ×4 定性对比（img062/074/028）。

## 7. 这篇论文真正有价值的地方
1. **算子级、可迁移**：GRSA 不绑定 GRFormer，能直接替换 SwinIR 及变体的自注意力，影响面超出单一网络。
2. **残差下沉**：把残差从自注意力外层下沉到 QKV 线性层内部，配合分组补偿容量损失，结构改动小但针对性强。
3. **先验参数化**：ES-RPB 用 `sign·(1-exp)` 把"近像素更重要"显式编码，再用小 MLP 平滑，替掉原 RPB 逐位置独立、易抖动的参数。
4. **理论补强**：3.6 用分块矩阵乘法论证"分组不削弱 QK 聚合"，为经验设计提供形式化依据（仅覆盖 Q、K）。

## 8. 局限与问题
1. GRL 固定二等分分组，未必最优，更多/更细分组的权衡未讨论（提取未涉及）。
2. ES-RPB 的指数衰减形式与单向 α/β 是特定建模，对不同窗口/任务的适配性存疑。
3. 实验聚焦轻量 SISR，大容量/高分辨率或跨任务下分组收益是否仍显著，PDF 未给（待核后续页）。
4. 基准多为双三次合成退化，真实复杂退化下泛化未验证。
5. 仅报告理论 #MACs/#Params 削减，提取未见实测 FPS/时延，理论降幅未必等比转化为实测加速。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + RQ1–RQ3 + Method 3.3 + Table 1 分析。
- **复现**：精读 3.1（公式 1–4）、3.2（5–6）、3.3（7–8）、3.4（9）、3.5（10），对照 Fig.3；注意 GRL 的"二分+残差+拼接"与 ES-RPB 的映射/MLP；代码见 github.com/sisrformer/GRFormer。
- **借鉴**：GRL（分组+残差）迁到其他视觉 Transformer 的 QKV 投影；ES-RPB 的"先验→参数化函数→位置偏置"用于显式位置建模任务。
- **写 related work**：归入"轻量级超分辨率网络"或"高效视觉 Transformer/注意力机制"。

## 10. 和其他论文的关系
- **直接基线/改进对象**：`[[SwinIR]]`——GRSA 旨在替代其自注意力模块；总参数对比以 SwinIR(1000k) 为参照。
- **灵感来源**：`[[SwinIR-v2]]`——其 log-spaced 连续位置偏置启发了 ES-RPB 的设计（原文 2.3 节明述"很受启发"）。
- **奠基**：`[[Self-Attention (Attention Is All You Need)]]`（自注意力，2017）、`[[Swin Transformer]]`（层级 + 移位窗口）。
- **竞争/对比**：轻量超分赛道上与 `[[SRFormer]]`、`[[HPINet]]`、`[[SwinIR-NG]]`、`[[CARN]]`、`[[LatticeNet]]`、`[[EDSR]]` 对比。
- **领域**：属 `[[Transformer-based Image Super-Resolution]]` 与 `[[Lightweight Image Super-Resolution]]`。

## 11. 关键词
轻量级图像超分辨率, 自注意力, 参数冗余, 分组, 残差连接, 相对位置偏置, ES-RPB, 指数映射, 窗口自注意力, Transformer, SwinIR, GRFormer

## 12. 可信度说明
本精读基于提取文本的**前 ~25000 字符（约前 5–6 页正文）**，覆盖摘要、引言（RQ1–RQ3 与 RPB 四缺陷）、相关工作、方法全部（整体架构、GRSAB、GRSA、GRL、ES-RPB、3.6 有效性证明，公式 1–12）以及 Table 1 的标题与 ×2 部分基线行。这部分提取质量良好、无明显乱码，模型设计、公式、关键文字数值（33.17 / 32.76 / 32.94、60%/49%/20%/0.23dB/0.19dB、1000k 参数、1280×720）均可核。**主要缺失**：Table 1 中 GRFormer 自身完整数值、×3/×4 逐数据集结果、消融实验、训练细节、定量推理速度——这些在原 PDF 后续页（提取仅含前 ~25000/47154 字符），笔记中相应处已标注"待核"。元数据上，原 frontmatter 的 year=2021、仅 2 位作者、venue 乱码均与提取冲突，已据提取更正为 2024 / 四位作者（含通讯作者 Zehang Deng、Lihua Liu）/ ACM MM '24。

---

> **可信度补充**: PDF 提取质量 = **medium**（提取文本被硬截断至 ~25000/47154 字符，约前 5–6 页；方法与摘要完整可核，但 Table 1 主结果、×3/×4、消融、训练细节未覆盖，已逐处标注"待核"）; 来源缓存: `.paper-cache/extracts/GRSA.txt`（标称 9/9 页, 实际正文截断）; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
