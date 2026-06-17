---
title: Simple Baselines for Image Restoration
authors:
  - "Liangyu Chen"
  - "Xiaojie Chu"
  - "Xiangyu Zhang"
  - "Jian Sun"
year: 2022
venue: "arXiv"
doi: 
pdf: [[NAF.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
extract_cache: .paper-cache/extracts/NAF.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/21 pages"
---
# Simple Baselines for Image Restoration

## 基本信息
- **PDF**: [[NAF.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`, `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Simple Baselines for Image Restoration |
| **作者** | Liangyu Chen; Xiaojie Chu; Xiangyu Zhang; Jian Sun (MEGVII Technology) |
| **发表时间** | 2022 (arXiv:2204.04676v4, 2022-08-01) |
| **刊物/会议** | arXiv (ECCV 2022) |
| **DOI** | 未明确 |

## 摘要

清理后的英文原摘要（修复空格与连字符、剔除杂入的图表数字）：

> Although there have been significant advances in the field of image restoration recently, the system complexity of the state-of-the-art (SOTA) methods is increasing as well, which may hinder the convenient analysis and comparison of methods. In this paper, we propose a simple baseline that exceeds the SOTA methods and is computationally efficient. To further simplify the baseline, we reveal that the nonlinear activation functions, e.g. Sigmoid, ReLU, GELU, Softmax, etc. are not necessary: they could be replaced by multiplication or removed. Thus, we derive a Nonlinear Activation Free Network, namely NAFNet, from the baseline. SOTA results are achieved on various challenging benchmarks, e.g. 33.69 dB PSNR on GoPro (for image deblurring), exceeding the previous SOTA 0.38 dB with only 8.4% of its computational costs; 40.30 dB PSNR on SIDD (for image denoising), exceeding the previous SOTA 0.28 dB with less than half of its computational costs. The code and the pre-trained models are released at github.com/megvii-research/NAFNet.

中文翻译：

> 尽管近年图像恢复领域取得显著进展，但 SOTA 方法的系统复杂度也在不断攀升，妨碍了对各方法的便捷分析与比较。本文提出一个超越 SOTA 且计算高效的简单基线。为进一步简化该基线，我们揭示出非线性激活函数（如 Sigmoid、ReLU、GELU、Softmax 等）并非必需：它们可以被乘法替代或直接去除。由此我们从基线推导出一个"无非线性激活网络"，即 NAFNet。它在多个高难度基准上取得 SOTA：例如在 GoPro（图像去模糊）上达 33.69 dB PSNR，以仅 8.4% 的计算量超越前 SOTA 0.38 dB；在 SIDD（图像去噪）上达 40.30 dB PSNR，以不到一半的计算量超越前 SOTA 0.28 dB。代码与预训练模型已开源于 github.com/megvii-research/NAFNet。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：随着深度学习发展，图像恢复方法性能显著提升，但 SOTA 方法的系统复杂度也随之增加，妨碍了方法间的便捷分析与比较。作者把系统复杂度拆为两部分：**块间复杂度（inter-block）** 和 **块内复杂度（intra-block）**。(p.1)
- **之前方法的问题**：
    - 块间复杂度高：[37,5] 是多阶段网络（后一阶段精修前一阶段结果）；[7,25] 单阶段但在不同尺寸特征图间引入复杂连接。(p.1, p.4)
    - 块内复杂度高：如 Restormer[39] 的 Multi-Dconv Head Transposed Attention 与 Gated-Dconv Feed-Forward、Swin Transformer Block[22]、HINBlock[5] 等，逐个评估这些设计不现实。(p.1, p.3)
- **核心矛盾**：作者提出一个根本问题——一个**块间复杂度低**（用经典单阶段 UNet）且**块内复杂度低**（用简单组件）的网络，能否也达到 SOTA 性能？为此从含 convolution / ReLU / shortcut 的 plain block 出发，逐个添加或替换 SOTA 组件并验证各自的增益。(p.1, p.2)
## 关键贡献

1.  **构建了一个简单高效的基线网络**：通过对 SOTA 方法做"分解—提取必要组件"的系统性消融，从最基础的 PlainNet 块出发，逐步验证并加入必要组件（Layer Normalization、GELU、Channel Attention），形成一个超越当时 SOTA 且计算成本更低的基线网络（Baseline）。(p.2)
2.  **提出了 NAFNet**：通过揭示 GELU、Channel Attention 与门控线性单元（GLU）的内在联系，用 **SimpleGate** 替换 GELU、用 **简化通道注意力（Simplified Channel Attention, SCA）** 替换标准通道注意力，从而去除网络中所有非线性激活函数（Sigmoid、ReLU、GELU 等），得到 NAFNet——它在被简化后仍能匹配甚至超越基线。(p.2, p.3, p.8, p.9)
3.  **证明了非线性激活函数的可替代性**：作者声称这是首个在 SOTA 计算机视觉模型上证明"非线性激活函数可能并非必需"的工作——它们可被简单的逐元素乘法替代或去除而不损失性能，从而有望扩展 SOTA 视觉方法的设计空间。(p.2, p.3)
4.  **提出了两个具体的简化算子**：**SimpleGate**（把特征图在通道维度平分为两半并逐元素相乘）和 **SCA**（对全局平均池化后的特征仅用一个线性层算通道权重，去掉 ReLU 与 Sigmoid）。(p.8, p.9)
## 方法

### 整体框架
- 采用经典的**单阶段 U 形（UNet）架构 + skip-connection**（图 2c），以降低块间复杂度，沿用 [39,36] 的做法。作者认为架构本身不会成为性能瓶颈。(p.4, p.5)
- **输入**：退化图像（如模糊、含噪）；**输出**：恢复后的清晰图像。

### 关键模块与连接（从 PlainNet 到 NAFNet 的演进）
1.  **PlainNet 块**（图 3b）：含最常见的组件——**卷积**、**ReLU**、**残差连接（shortcut）**，排布沿用 [13,22]。用卷积而非 transformer，理由是 depthwise 卷积比 self-attention 更简单，且有工作[13,23]表明 transformer 对 SOTA 并非必需。这是研究起点。(p.5)
2.  **基线块（Baseline）**（图 3c）：在 PlainNet 基础上：
    - 加入 **Layer Normalization (LN)**：稳定训练，使学习率可提高 10 倍（1e-4 → 1e-3），由此带来显著增益。(p.5)
    - 将 **ReLU 替换为 GELU**。(p.6)
    - 末尾加入 **Channel Attention (CA)**，聚合全局信息（受 [39] 通道注意力启发）。(p.7)
    - 连接顺序大致为：LN → 卷积 → GELU → 卷积 → CA → 残差。
3.  **NAFNet 块**（图 3d）：对基线做终极简化：
    - **SimpleGate 替换 GELU**：`SimpleGate(X, Y) = X ⊙ Y`，X、Y 是把输入特征图在通道维度平分得到的两半，用一次逐元素乘法引入非线性（Eqn.4）。(p.8)
    - **SCA 替换标准 CA**：`SCA(X) = X * W·pool(X)`，`pool` 为全局平均池化、`W` 为单个全连接层（channelwise 乘）。去掉了原 CA 中的 ReLU 与 Sigmoid，仅保留"聚合全局信息 + 通道交互"两个核心功能（Eqn.7）。(p.9)
    - 连接顺序大致为：LN → 卷积 → SimpleGate → 卷积 → SCA → 残差。
    - **关键点**：此时网络中已**不存在任何非线性激活函数**（ReLU/GELU/Sigmoid）。(p.9)

### 数学公式与机制的直观解释
- **GLU 一般式**：`Gate(X, f, g, σ) = f(X) ⊙ σ(g(X))`，f、g 为线性变换，σ 为非线性激活（如 Sigmoid），⊙ 为逐元素乘（Eqn.1）。(p.8)
- **GELU 是 GLU 的特例**：`GELU(x) = xΦ(x)`，Φ 为标准正态分布的累积分布函数（Eqn.2，并可由 `0.5x(1+tanh[√(2/π)(x+0.044715x³)])` 近似，Eqn.3）。对照 Eqn.1，GELU 相当于 f、g 取恒等、σ 取 Φ。(p.8)
- **核心洞察**：GLU 结构 `f(X) ⊙ g(X)` 本身（即使去掉 σ）就因"两个线性变换之积"而带有非线性。因此网络中的非线性可来自这种乘积结构，而非传统激活函数——这正是 SimpleGate 与 SCA 能去掉激活函数却不掉点的根据。(p.8)
- **CA 原式**：`CA(X) = X * σ(W2·max(0, W1·pool(X)))`（Eqn.5，σ=Sigmoid，两全连接层间夹 ReLU），可抽象为 `CA(X)=X*Ψ(X)`（Eqn.6），其形式与 GLU 的 Eqn.1 高度相似，于是可像 GLU 一样简化为 SCA。(p.9)

### 训练方式
- Adam 优化器（β1=0.9, β2=0.9, weight decay=0）。(p.10)
- 共 200K 次迭代，初始学习率 1e-3，余弦退火降至 1e-6。(p.10)
- 训练块大小 256×256，批大小 32；消融预算约 16 GMACs（沿用 HINet Simple[5]），并用 gradient clip 与 PSNR loss。(p.4, p.10)
- 默认宽度 32、块数 36；改变块数时调整宽度以维持计算预算。(p.10)
- **TLC（Test-time Local Converter，引自 [8]）**：解决"按块训练、整图测试"导致的性能下降（GoPro 上效果见 Tab.4）。(p.10)
- **skip-init[11]**：稳定训练（沿用 [23]）。(p.10)
- 速度/显存/复杂度评测在 256×256 输入、NVIDIA 2080Ti GPU 上进行。(p.10)

### 推理流程
测试时使用完整图像，并应用 TLC 策略以避免按块测试带来的伪影与掉点；提取文本未给出更细的逐步推理流程。(p.10)

### 和已有方法的差异
- **与 Restormer[39] 等相比**：Restormer 用通道维转置注意力与带非线性激活的门控前馈网络（图 3a）；NAFNet 用更简单的深度卷积 + 通道交互，且完全去除非线性激活，结构更简单、计算更高效。(p.1, p.3, p.6)
- **与窗口注意力（如 Uformer[36]/Swin[22]）相比**：作者不采用窗口注意力，认为局部信息已能被 plain block 中的 depthwise 卷积充分捕获。(p.7)
- **与传统 CNN 相比**：传统 CNN 依赖 ReLU 等激活；NAFNet 用 SimpleGate（乘法）+ 线性变换组合产生非线性，提供了新的设计范式。(p.8)
## 实验

### 使用的数据集
- **图像去噪**：SIDD[1]。**图像去模糊**：GoPro[26]。这两个是消融与主实验的主战场。(p.4)
- 此外 NAFNet 还被应用于 **raw 图像去噪（4Scenes，39 张 raw、4 个场景）** 与 **带 JPEG 伪影的图像去模糊**（据原文后续页 p.13-14，提取缓存未覆盖，待核）。(p.9; p.13-14)

### 对比方法
HINet[5], Restormer[39], MPRNet[37], Uformer[36], NBNet, MIMO-UNet, DeepRFT, MAXIM-3S, MIRNet, PMRID（raw 去噪）等当时多个 SOTA。(p.2; 据原文后续页 p.13)

### 评价指标
- 主要指标：**PSNR**（峰值信噪比）与 **SSIM**（结构相似性）。(p.10)
- 效率指标：计算复杂度 **MACs（乘加次数，G）**，输入 256×256。(p.4, p.10)

### 主实验结果
- **GoPro（去模糊）**：NAFNet 达 **33.69 dB PSNR**，超前 SOTA[8] **0.38 dB**，计算量仅 **8.4%**；Baseline 达 33.40 dB（超前 SOTA 0.09 dB）。(p.2)
- **SIDD（去噪）**：NAFNet 达 **40.30 dB PSNR**，超前 SOTA[39] **0.28 dB**，计算量 **不到一半**。Baseline 在 SIDD 同样达 40.30 dB。(p.2)
- 据原文后续页的对比表（提取缓存未覆盖，待核）：SIDD Table 6 的 PSNR 阶梯为 …39.99 / 40.02 / 40.30(Baseline) / 40.30(NAFNet)；GoPro Table 7 的阶梯为 …33.31 / 33.40(Baseline) / 33.69(NAFNet)。(p.13)

### 消融实验
- **从 PlainNet 到基线（Table 1）**：
    - PlainNet 在默认大学习率下训练不稳定，需把 lr 降 10×（1e-3→1e-4）才能训练。引入 **LN** 后 lr 可恢复到 1e-3 且训练更稳：第 3.3 节给出 **+0.44 dB（SIDD 39.29→39.73）/ +3.39 dB（GoPro 28.51→31.90）**；第 5.1 节的消融小结复述为 **+0.46 dB / +3.39 dB**（两处数字略有出入，以 LN 带来巨大增益这一结论为准）。(p.5, p.10)
    - **ReLU→GELU**：SIDD 几乎持平（39.73→39.71，略降 0.02 dB），GoPro **+0.21 dB**（31.90→32.11）；故采用 GELU（保去噪、提去模糊）。(p.6)
    - **加 CA**：SIDD **+0.14 dB**（39.71→39.85），GoPro **+0.24 dB**（32.11→32.35）。(p.7)
- **从基线到 NAFNet（Table 2）**：
    - **GELU→SimpleGate**：SIDD **+0.08 dB**（39.85→39.93），GoPro **+0.41 dB**（32.35→32.76）。(p.8)
    - **CA→SCA**：SIDD **+0.03 dB**（39.93→39.96），GoPro **+0.09 dB**（32.76→32.85）。(p.9)
    - 该简化总计在 SIDD/GoPro 上 PSNR 还**净涨 0.11 dB / 0.50 dB**——简化非但不掉点反而提升。(p.10)

### 泛化实验
- **raw 图像去噪**：在 4Scenes 上 NAFNet 在数量与质量上均超过 PMRID（Table 8/Figure 7）。(据原文后续页 p.13-14，提取缓存未覆盖，待核)
- **带 JPEG 伪影的去模糊** 及 **NTIRE 2021（REDS）** 相关结果亦在后续页提及（据原文后续页 p.13-14，提取缓存未覆盖，待核）。(p.13-14)

### 速度/参数量/FLOPs
- 主要以 **MACs（G）** 衡量计算成本，输入 256×256，硬件 NVIDIA 2080Ti。图 1 给出 PSNR-vs-MACs 的帕累托前沿，NAFNet/Baseline 处于"更高 PSNR、更低算力"的有利位置。提取文本未给出统一的参数量(Params)与 FPS 数值。(p.2, p.10)
## 局限

- **适用任务范围有限**：消融与主实验集中在去噪（SIDD）与去模糊（GoPro）；raw 去噪与 JPEG 去模糊虽有验证（后续页），但"非线性激活非必需"是否推广到超分、图像生成等任务仍待检验。
- **基准代表性**：SIDD/GoPro 不能代表全部恢复场景，更广泛基准上的泛化性需进一步验证。
- **参数量与实际速度披露不足**：论文以 MACs 为主，提取文本未系统给出 Params 与 FPS，对部署评估不够。
- **对超参与训练技巧的依赖**：默认宽度 32、块数 36，以及 TLC、skip-init、gradient clip 等技巧对复现很关键，其细节需结合开源代码。
- **"无激活"的边界**：去掉激活后非线性来自乘积结构（SimpleGate/SCA），论文未深入分析这种非线性的表达能力上限与在更深/更宽网络上的稳定性。
## 个人评论

1.  **"做减法"的研究范式**：本文最值得学习的是其思路——不堆砌 SOTA 组件，而是从最简 plain block 出发，用系统消融**严格验证每个组件的必要性**，最终甚至敢去掉"理所当然"的非线性激活。这给高效模型设计提供了清晰可迁移的方法论。
2.  **对非线性来源的重新定位**：揭示 GELU/CA 与 GLU 的形式同构，并指出"两个线性变换之积本身即含非线性"，把问题从"选哪种激活函数"升级为"非线性该从哪里来"，扩展了设计空间。
3.  **算子可直接复用**：SimpleGate 与 SCA 实现极简（一次逐元素乘 / 池化+单线性层），却能稳定带来增益，非常适合作为轻量模块插入他人网络——这也是 NAFNet 之后被广泛"拿来即用"的原因。
4.  **效率—性能平衡的范例**：在达到/超越 SOTA 的同时把算力降一个数量级（GoPro 仅 8.4% 算力），图 1 的帕累托前沿很有说服力。
5.  **可商榷处**：消融两处 LN 增益数字（0.44 vs 0.46 dB）不一致；"无激活"主要在两个 low-level 任务上验证，结论强度受任务范围约束，宜谨慎外推。

### 使用建议

- **快速了解**：读摘要、引言（第 1 节）与贡献即可掌握核心思想、动机与主要成果。
- **复现**：精读第 3 节（构建基线）、第 4 节（NAFNet 详解）与第 5.1 节（消融与训练设置），结合开源代码，关注优化器/学习率/TLC/skip-init/宽度·块数。
- **借鉴创新点**：直接学习 SimpleGate 与 SCA 的实现，作为轻量高效模块插入自己的网络；并学习"从简单基线做系统消融"的评估方法。
- **写 related work**：可归入 `[[图像恢复/去噪/去模糊]]`、`[[注意力机制/通道注意力]]` 的简化、`[[轻量化网络设计]]`、`[[激活函数/非线性]]` 的延伸。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉的底层（low-level）视觉方向，核心是**图像恢复（Image Restoration）**，落地任务为**图像去噪（SIDD）** 与 **图像去模糊（GoPro）**，并延伸到 raw 去噪与 JPEG 去模糊。它提出一个计算高效、结构极简的网络 NAFNet，以远低于 SOTA 的算力达到或超越 SOTA。因此主题归入 `E_图像复原_超分_去噪_去雨去雾` 最贴切；同时其核心贡献之一是提出"简化通道注意力（SCA）"这一注意力算子，故并列保留 `B_注意力算子模块` 作为次主题。

## 2. 一句话总结
通过构建并逐步简化一个通用图像恢复基线，作者揭示并实证了非线性激活函数（Sigmoid/ReLU/GELU 等）在高性能恢复网络中并非必需——可用逐元素乘法替代或直接去除——由此得到无非线性激活的 NAFNet，在 SIDD/GoPro 上以更低算力刷新 SOTA。

## 3. 背景与问题
- **为什么要做**：深度学习让图像恢复性能大涨，但 SOTA 方法系统复杂度同步攀升，妨碍方法间的分析与比较。作者把复杂度拆为**块间复杂度**（多阶段、跨尺度连接）与**块内复杂度**（转置注意力、门控前馈、Swin/HIN 块等）。(p.1)
- **之前方法的问题**：多阶段网络[37,5]与跨尺度融合[7,25]推高块间复杂度；Restormer[39]、Uformer[36] 等在单阶段 UNet 上推高块内复杂度。逐一评估这些设计不现实。(p.1, p.3)
- **核心矛盾**：能否用"块间 + 块内都低复杂度"的网络达到 SOTA？作者用单阶段 UNet 固定块间复杂度，聚焦块内：从 conv+ReLU+shortcut 的 plain block 起，逐组件添加/替换并量化增益。(p.1, p.2)

## 4. 核心贡献
1.  **简单高效基线**：分解 SOTA、提取必要组件，从 PlainNet 出发加入 LN/GELU/CA，得到超越前 SOTA 且算力更低的 Baseline，便于他人快速验证新想法。(p.2)
2.  **NAFNet**：揭示 GELU、CA 与 GLU 的联系，用 SimpleGate 替 GELU、用 SCA 替 CA，去除全部非线性激活；简化后仍匹配/超越基线。(p.2, p.3, p.8, p.9)
3.  **"非线性激活非必需"的首次实证**：作者称这是首个无非线性激活却达 SOTA 的 CV 模型，有望扩展 SOTA 视觉方法的设计空间。(p.3)
4.  **两个即插即用算子**：SimpleGate（通道平分后逐元素乘）与 SCA（池化 + 单线性层 + channelwise 乘）。(p.8, p.9)

## 5. 方法详解
### 整体框架
- 经典单阶段 U 形架构 + skip-connection（图 2c），沿用 [39,36]，用以压低块间复杂度；作者用 Table 6/7、图 1 验证架构不构成瓶颈。(p.4, p.5)
- 输入退化图像，输出清晰图像。

### 关键模块与连接（PlainNet → NAFNet）
1.  **PlainNet 块**（图 3b）：conv + ReLU + shortcut，排布沿用 [13,22]；选卷积而非 transformer，因 depthwise 卷积更简单且 transformer 对 SOTA 非必需。(p.5)
2.  **基线块**（图 3c）：加 LN（稳定训练、可用 10× 学习率）→ ReLU 换 GELU → 末尾加 CA。顺序约为 LN→conv→GELU→conv→CA→残差。(p.5–p.7)
3.  **NAFNet 块**（图 3d）：
    - GELU→**SimpleGate**：`SimpleGate(X,Y)=X⊙Y`，X、Y 为通道平分两半（Eqn.4）。(p.8)
    - CA→**SCA**：`SCA(X)=X*W·pool(X)`（Eqn.7），去掉 ReLU/Sigmoid。(p.9)
    - 顺序约为 LN→conv→SimpleGate→conv→SCA→残差；**全网无任何非线性激活**。(p.9)

### 数学公式与机制
- GLU 一般式 `f(X)⊙σ(g(X))`（Eqn.1）；GELU `xΦ(x)`（Eqn.2，近似式 Eqn.3）是其特例（f,g 取恒等、σ=Φ）。(p.8)
- 关键洞察：`f(X)⊙g(X)` 去掉 σ 仍含非线性（两线性变换之积），故可用乘法替代激活。(p.8)
- CA `X*σ(W2 max(0,W1 pool(X)))`（Eqn.5）≈ `X*Ψ(X)`（Eqn.6），形似 GLU，可被简化为 SCA。(p.9)

### 训练方式
- Adam(β1=0.9, β2=0.9, wd=0)，200K 迭代，lr 1e-3→1e-6 余弦退火；patch 256×256，batch 32；约 16 GMACs 预算 + gradient clip + PSNR loss；默认宽度 32、块数 36；TLC 解决 patch 训练/整图测试落差；skip-init 稳定训练；评测于 2080Ti。(p.4, p.10)

### 推理流程
测试用整图 + TLC；提取文本未给更细步骤。(p.10)

### 和已有方法的差异
- vs Restormer：去掉转置注意力与带激活的门控前馈，改用 depthwise 卷积 + 通道交互，结构更简、算力更省。(p.1, p.3, p.6)
- vs 窗口注意力：不用窗口注意力，局部信息交给 depthwise 卷积。(p.7)
- vs 传统 CNN：用 SimpleGate（乘法）+ 线性变换提供非线性。(p.8)

## 6. 实验与结果
### 数据集
SIDD[1]（去噪）、GoPro[26]（去模糊）为主；raw 去噪（4Scenes，39 张 raw/4 场景）与 JPEG 去模糊为扩展。(p.4, p.9; p.13-14 据后续页待核)

### 对比方法
HINet, Restormer, MPRNet, Uformer, NBNet, MIMO-UNet, DeepRFT, MAXIM-3S, MIRNet, PMRID 等。(p.2; p.13 据后续页待核)

### 评价指标
PSNR、SSIM；效率用 MACs(G)（256×256）。(p.4, p.10)

### 主实验结果
- GoPro：NAFNet 33.69 dB（+0.38 dB，8.4% 算力）；Baseline 33.40 dB（+0.09 dB）。(p.2)
- SIDD：NAFNet 40.30 dB（+0.28 dB，<½ 算力）；Baseline 亦 40.30 dB。(p.2)
- Table 6/7 PSNR 阶梯（据后续页 p.13，提取缓存未覆盖，待核）：SIDD …40.02 / 40.30 / 40.30；GoPro …33.31 / 33.40 / 33.69。(p.13)

### 消融
- PlainNet→Baseline（Table 1）：LN +0.44 dB(SIDD)/+3.39 dB(GoPro)（3.3 节；5.1 节复述为 +0.46/+3.39，存细微出入）；ReLU→GELU −0.02/+0.21；+CA +0.14/+0.24。(p.5–p.7, p.10)
- Baseline→NAFNet（Table 2）：GELU→SimpleGate +0.08/+0.41；CA→SCA +0.03/+0.09；简化总计净涨 0.11(SIDD)/0.50(GoPro) dB。(p.8–p.10)

### 泛化
raw 去噪超过 PMRID（Table 8/Fig.7）、JPEG 去模糊、NTIRE 2021(REDS) 相关结果在后续页（据 p.13-14，提取缓存未覆盖，待核）。(p.9, p.13-14)

### 速度/参数量/FLOPs
以 MACs(G) 为主，2080Ti、256×256；图 1 显示 PSNR-MACs 帕累托前沿占优；提取文本未给统一 Params/FPS。(p.2, p.10)

## 7. 这篇论文真正有价值的地方
1.  **"做减法"的方法论**：从最简基线出发、系统消融验证每个组件必要性，最终敢去掉非线性激活——一套可迁移的高效设计范式。
2.  **重新定位非线性的来源**：GELU/CA ↔ GLU 的同构 + "两线性变换之积即非线性"，把"选激活函数"升级成"非线性从哪来"。
3.  **算子可直接复用**：SimpleGate / SCA 实现极简却稳定增益，易插入他人网络（NAFNet 之后被大量沿用即证）。
4.  **效率—性能平衡范例**：达/超 SOTA 同时算力降一个数量级，帕累托前沿很有说服力。

## 8. 局限与问题
- 任务范围限于去噪/去模糊（+raw/JPEG），结论外推到超分、生成等仍待验证。
- SIDD/GoPro 代表性有限。
- 提取文本未系统给出 Params 与 FPS，部署评估不足。
- 成功依赖 TLC、skip-init、gradient clip、宽度·块数等技巧，细节需看代码。
- 两处 LN 增益数字不一致（0.44 vs 0.46 dB）。

## 9. 我该怎么使用这篇论文
- 快速了解：读摘要 + 引言 + 贡献。
- 复现：精读第 3/4/5.1 节 + 开源代码，关注训练设置（优化器、lr、TLC、skip-init、宽度/块数）。
- 借鉴：直接用 SimpleGate 与 SCA 作为轻量模块；学习"简单基线 + 系统消融"的评估法。
- 写 related work：图像恢复/去噪去模糊、通道注意力简化、轻量网络、激活函数/非线性。

## 10. 和其他论文的关系
- **图像恢复网络**：`[[Restormer]]`(p.1,3,6)、`[[HINet]]`(p.5,10)、`[[MPRNet]]`(p.2)、`[[Uformer]]`(p.3,7)、MIMO-UNet/DeepRFT/MAXIM/MIRNet/NBNet(p.2)。
- **门控线性单元**：理论根基 `[[Gated Linear Units (GLU)]]`(p.3,8)，本文做了 CV 领域的应用与简化。
- **通道注意力**：标准实现参考 `[[Squeeze-and-Excitation (SE)]]`(p.7,9)，本文将其简化为 SCA。
- **UNet 架构**：基础架构 `[[UNet]]`(p.4)。
- **raw 去噪**：与 `[[PMRID]]` 对比（p.13，据后续页待核）。

## 11. 关键词
图像恢复, 图像去噪, 图像去模糊, NAFNet, 简单基线, 非线性激活自由, 通道注意力, 简化通道注意力(SCA), SimpleGate, GLU, GELU, Layer Normalization, TLC, 计算效率, MACs

## 12. 可信度说明
本笔记的顶部各节与精读 1–9 节主要基于提取缓存（PDF p.1-12），涵盖摘要、引言、相关工作、方法核心（第 3、4 节，含 Eqn.1-7 与关键公式）以及实验设置与消融的开头（第 5.1 节）。这部分提取质量良好（约 2086 字符/页），核心动机、方法演进、公式与主要定量增益均可逐条核对。涉及 PDF p.13-21 的内容（Table 6/7/8/9 完整对比、raw 去噪 vs PMRID、JPEG 去模糊、NTIRE 2021 等）不在提取缓存内，依据原笔记"全文补读记录"的页面线索保留并已逐处标注"据原文后续页 p.13-x，提取缓存未覆盖，待核"。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页), 提取缓存覆盖 p.1-12); 来源缓存: `.paper-cache/extracts/NAF.txt` (12/21 页; 原 AI 主体 12/21 + 全文补读线索 13-21); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-21; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-21。
- **提取情况**: 缺失页 9 页, 其中 9 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Nonlinear Activation Free Network 13
- p.13: MethodMPRNet MIRNet NBNet UFormer MAXIM HINet Restormer Baseline NAFNet
- p.13: MethodMIMO-UNet HINet MAXIM Restormer UFormer DeepRFT MPRNet Baseline NAFNet
- p.14: Noisy Image
- p.14: Reference, PSNR
- p.14: Table 8: Raw image denoising results
- p.14: Method PSNR SSIM MACs(G)
- p.14: 6 Conclusions
- p.14: By decomposing the SOTA methods, we extract the essential components and
- p.14: Acknowledgements: This research was supported by National Key R&D Pro-
- p.15: Appendix
- p.15: A Other Details

### 缺失页关键摘录

- p.13: PSNR MPRNet [37] MPRNet-local [8] NAFNet( ours )
- p.13: Table 6: Image Denoising Results on SIDD[1]
- p.13: PSNR 39.71 39.72 39.75 39.89 39.96 39.99 40.02 40.30 40.30
- p.13: set as 4Scenes (as the dataset contains 39 raw images of 4 different scenes in
- p.13: shown in Table 8 and Figure 7 demonstrate NAFNet can surpass PMRID quan-
- p.13: titatively and qualitatively. In addition, this experiment indicates our NAFNet
- p.13: dataset, the training setting follows [5,32], and we evaluate the result on 300 im-
- p.13: in Table 9, our method outperforms other competing methods, including the
- p.13: Table 7: Image Deblurring Results on GoPro[26]
- p.13: PSNR 32.68 32.71 32.86 32.92 32.97 33.23 33.31 33.40 33.69
- p.14: previous winning solution (HINet) on the REDS dataset of NTIRE 2021 Image
- p.15: We first discuss the setting of the ablation studies. In the baseline, the channel
<!-- AI_READING_NOTE_END -->
