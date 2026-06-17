---
title: Omni-Kernel Network for Image Restoration
authors:
  - "Yuning Cui"
  - "Wenqi Ren"
  - "Alois Knoll"
year: 2024
venue: AAAI 2024 (The Thirty-Eighth AAAI Conference on Artificial Intelligence)
doi: 
pdf: [[OKM.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
extract_cache: .paper-cache/extracts/OKM.txt
---

# Omni-Kernel Network for Image Restoration

## 基本信息
- **PDF**: [[OKM.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Omni-Kernel Network for Image Restoration |
| **作者** | Yuning Cui (TU Munich); Wenqi Ren (Sun Yat-sen University, 通讯作者); Alois Knoll (TU Munich) |
| **发表时间** | 2024 (AAAI-24, pp. 1426–1433) |
| **刊物/会议** | The Thirty-Eighth AAAI Conference on Artificial Intelligence (AAAI 2024) |
| **代码** | https://github.com/c-yn/OKNet |
| **DOI** | 未明确 |

## 摘要

清理后的英文原摘要（据 PDF 提取文本整理，修复空格/连字符并剔除混入的图轴数字）：

> Image restoration aims to reconstruct a high-quality image from a degraded low-quality observation. Recently, Transformer models have achieved promising performance on image restoration tasks due to their powerful ability to model long-range dependencies. However, the quadratically growing complexity with respect to the input size makes them inapplicable to practical applications. In this paper, we develop an efficient convolutional network for image restoration by enhancing multi-scale representation learning. To this end, we propose an omni-kernel module that consists of three branches, i.e., global, large, and local branches, to learn global-to-local feature representations efficiently. Specifically, the global branch achieves a global perceptive field via the dual-domain channel attention and frequency-gated mechanism. Furthermore, to provide multi-grained receptive fields, the large branch is formulated via different shapes of depth-wise convolutions with unusually large kernel sizes. Moreover, we complement local information using a point-wise depth-wise convolution. Finally, the proposed network, dubbed OKNet, is established by inserting the omni-kernel module into the bottleneck position for efficiency. Extensive experiments demonstrate that our network achieves state-of-the-art performance on 11 benchmark datasets for three representative image restoration tasks, including image dehazing, image desnowing, and image defocus deblurring.

中文翻译：

> 图像复原旨在从退化的低质量观测中重建高质量图像。近期 Transformer 模型凭借强大的长程依赖建模能力在图像复原任务上取得了优异性能，但其复杂度随输入尺寸二次增长，难以用于实际应用。本文通过增强多尺度表示学习，设计了一个高效的卷积网络用于图像复原。为此，我们提出**全核模块 (omni-kernel module, OKM)**，由全局、大尺度、局部三个分支组成，以高效学习从全局到局部的特征表示。具体而言：全局分支通过**双域通道注意力**和**频率门控机制**获得全局感受野；大尺度分支由**不同形状、卷积核异常大的深度卷积**构成，以提供多粒度感受野；并用一个**逐点深度卷积**补充局部信息。最终，将 OKM 插入网络瓶颈位置以保证效率，得到 **OKNet**。大量实验表明，在**图像去雾、去雪、散焦去模糊**三项代表性任务的 **11 个基准数据集**上，OKNet 均取得 SOTA 性能。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：图像复原是低级视觉中的基础问题，旨在从受 haze（雾）、snowflakes（雪）、blur（模糊）等退化的低质量图像中恢复清晰图像，应用于监控、自动驾驶、遥感、医学成像等场景。它是高度病态（ill-posed）问题。早期方法依赖手工特征与先验假设，难以泛化到真实复杂场景；深度学习方法（CNN / Transformer）后来居上。
- **之前方法的问题**：
    1.  **Transformer 方法**：核心组件自注意力的复杂度随输入尺寸**二次增长**，对实际应用代价高昂；为提效常采用限制注意力区域或将注意力从空间维转到通道维（如 Restormer），但这会**牺牲长程信号建模能力**；并且 **Transformer 无法捕捉多尺度感受野**。
    2.  **CNN / 大核方法**：常规卷积感受野有限。近期大核 CNN 反击（RepLKNet 31×31、SLaK 51×51；复原领域 LaKDNet 用 9×9、LKD-Net 分解 21×21、MAN 把大核拆成三种卷积），但**这些方法产生的感受野仍然有限，且都不提供全局感受野**。
- **核心矛盾**：如何设计一种高效卷积网络，在保持低复杂度的同时**同时获得全局感受野、多尺度/多粒度感受野与局部细节捕捉能力**，以应对图像中不同尺度、不同类型的退化。

## 关键贡献

论文原文（贡献小节）实际归纳为两条，本笔记按方法要点展开：

1.  **提出全核模块 OKM**：能高效捕捉多尺度感受野；其中大尺度信息由**双域处理 (dual-domain processing)** 与**不同形状的大核深度卷积**联合调制。模块由全局、大尺度、局部三个分支**并行**组成，使网络具备处理多尺度退化的能力。
2.  **构建 OKNet 并大规模验证**：将 OKM 仅插入**瓶颈位置**形成简洁卷积网络 OKNet；在 **11 个广泛使用的基准数据集**上、针对**散焦去模糊、去雾、去雪**三项代表性任务取得 SOTA。
3.  （方法细节）**首次探索 63×63 异常大核深度卷积**用于图像复原，并用 **1×K / K×1 条状深度卷积**提供不同形状的感受野（K=63）。
4.  （方法细节）**用双域处理提供全尺寸/全局感受野**（DCAM + FSAM，含 FFT/IFFT）。
5.  （方法细节）**用极简的 1×1 深度卷积补充局部信息**，处理小尺寸退化（在表 5 验证其有效性，提取缓存未覆盖具体数字）。

## 方法

- **整体框架（图 2(a)）**：OKNet 采用**编码器-解码器架构**，编码器与解码器各 **3 个尺度**。ResGroup 由多个残差块组成，每个残差块含两个 3×3 卷积、中间夹 GELU 非线性（图 2(e)）。**OKM 仅插入瓶颈位置**（分辨率最低处），以节省计算开销。
- **输入输出与上下采样**：输入退化图像 `I ∈ R^{3×H×W}`，先用 **3×3 卷积**投影为 `C×H×W` 嵌入特征。下采样用**步长卷积（kernel=3, stride=2）**，同时升通道、降空间分辨率；解码阶段把解码特征与编码特征**拼接 (concat)**，再用 **1×1 卷积把通道减半**；上采样用**转置卷积（kernel=4, stride=2）**。最后用一个 **3×3 卷积**输出残差图像，与输入相加得到复原结果。
- **关键模块 — Omni-Kernel Module (OKM)（图 2(b)）**：
    输入特征 `X ∈ R^{C×H×W}` 先过一个 1×1 卷积，再并行送入三个分支；三个分支输出**逐元素相加 (addition) 融合**，最后再过一个 1×1 卷积调制。
    1.  **大尺度分支 (Large Branch)**：
        - **方法**：用 `K×K` 深度卷积追求大感受野，受 strip-based self-attention 启发，**并行**再用 `1×K` 和 `K×1` 深度卷积获取条状上下文。
        - **核尺寸选择**：把 K 从 3 渐增到 63（实验见图 3），PSNR/SSIM 随之上升，最终选 **K=63**。因模块置于瓶颈（特征 64×64），故采用最大的奇数核尺寸 63。
    2.  **全局分支 (Global Branch)**：
        - **动机**：训练时在 256×256 patch 上，瓶颈特征空间尺寸为 **64×64**；但推理时输入图远大于训练 patch，63×63 核不足以覆盖全局，故用**双域处理**补足全局建模能力。由 **DCAM** 与 **FSAM** 顺序连接。
        - **双域通道注意力 DCAM（图 2(c)）**：
            - 频域通道注意力 **FCA**：`X_FCA = IF( F(X_Global) ⊗ W^{FCA}_{1×1}( GAP(X_Global) ) )`，公式(1)。`F`/`IF` 为 FFT 及其逆，`⊗` 为逐元素乘，`GAP` 为全局平均池化。依据谱卷积定理在频域全局调制特征。
            - 空间通道注意力 **SCA**：`X_DCAM = X_FCA ⊗ W^{SCA}_{1×1}( GAP(X_FCA) )`，公式(2)。在空间域再做一次通道注意力。DCAM 仅在**通道级粗粒度**增强双域特征。
        - **基于频率的空间注意力 FSAM（图 2(d)）**：`X_FSAM = IF( F( W^1_{1×1}(X_DCAM) ) ⊗ W^2_{1×1}(X_DCAM) )`，公式(3)。在**空间维**精细调制频谱，使模型关注对复原有用的频率分量。
    3.  **局部分支 (Local Branch)**：仅用一个 **1×1 深度卷积**补充局部信号，处理小尺寸退化（受 Restormer 等"局部信息很关键"的观察启发；有效性在表 5 验证）。
- **损失函数**：
    - 空间域 L1：`Lc = ‖Î − Y‖₁`，公式(4)。
    - 频域 L1：`Lf = ‖F(Î) − F(Y)‖₁`，公式(5)（对预测与真值各做 FFT 后算 L1）。
    - 总损失：`Lo = (1/E)(Lc + λLf)`，公式(6)，`E` 为输出元素个数，`λ = 0.1`。
- **训练配置**：Adam（β1=0.9, β2=0.999）；batch size = 8；学习率初始 2e−4，余弦退火衰减至 1e−6；数据增强为随机水平翻转（p=0.5），训练 patch 为 3×256×256；FLOPs 在 256×256 patch 上测量。
- **网络缩放**：按任务难度调节每个 ResGroup 的残差块数 `N`——**去雾/去雪 N=4，去模糊 N=16**；另设小版本 **OKNet-S（N=1）** 与 Fourmer 对比。各数据集单独训练独立模型。
- **与已有方法的差异（论文明确四点）**：(a) 首次探索**异常大核 63×63**；(b) 除方形深度卷积外用**多方向条状卷积**提供不同形状感受野；(c) 用**双域处理提供全尺寸感受野**；(d) 用**极简 1×1 深度卷积补充局部信息**。仅部署于瓶颈即可与 SOTA Transformer 持平或更优。

## 实验

- **数据集（共 11 个）**：
    - **去雾**：白天合成 RESIDE（SOTS-Indoor / SOTS-Outdoor）；白天真实 Dense-Haze、NH-HAZE、O-Haze、I-Haze；夜间 NHR。
    - **散焦去模糊**：DPDD。
    - **去雪**：CSD（提取缓存未覆盖该结果表；据引言，OKNet 在 CSD 上比 IRNeXt 高 0.7 dB PSNR）。
- **评价指标**：PSNR、SSIM 为主；去模糊任务另用 MAE、LPIPS。表中最优/次优分别加粗与下划线。
- **去雾结果（表 1，与 9 种 SOTA 对比）**：
    - **SOTS-Indoor**：OKNet **40.79 dB / 0.996 SSIM**，比 Transformer 模型 DehazeFormer-L（40.05 dB）高 **0.74 dB**，FLOPs 仅其 **14%**（图 1(a)）；比 Fourmer（37.32 dB）高 **3.47 dB**。
    - **SOTS-Outdoor**：OKNet 37.68 / 0.995。
    - **真实数据集**：OKNet 全面优于专为真实场景设计的 SDCE（如 O-Haze 25.64/0.94、I-Haze 21.72/0.87、Dense-Haze 16.92/0.64、NH-HAZE 20.48/0.80）。
    - **OKNet-S（小模型）**：SOTS-Indoor 37.59 / 0.994，比 Fourmer 高 **0.27 dB** 且 FLOPs 少 13%；并在多个真实集上领先。
- **夜间去雾（NHR，表 2，与 6 种方法对比）**：OKNet **27.92 dB / 0.979 SSIM**，比近期 FocalNet 高 **2.57 dB PSNR / 0.01 SSIM**。
- **散焦去模糊（DPDD，表 3，与 7 种算法对比）**：在 **Combined** 类别 OKNet **26.18 dB / 0.812 SSIM / MAE 0.037 / LPIPS 0.206**，比强 Transformer 模型 Restormer（25.98 dB）高 **0.2 dB**，且参数量少 **46%**（图 1(b)）；Indoor 28.99 dB、Outdoor 23.51 dB 均领先。
- **去雪（CSD）**：据引言比 IRNeXt 高 **0.7 dB PSNR**（结果表在提取缓存截断之后，据原文后续页，提取缓存未覆盖，待核）。
- **消融实验**：
    - **核尺寸（图 3）**：K 从 3 增到 63，PSNR、SSIM 持续上升（同时图中展示 FLOPs/Params 随核增大的变化），验证超大核有效。
    - **局部分支有效性（表 5）**：论文指出在表 5 验证了 1×1 深度卷积局部分支的有效性（据原文后续页，提取缓存未覆盖具体数字，待核）。
- **效率**：图 1 在 FLOPs-PSNR、参数-PSNR 两个维度上均展示出更优的性能-计算权衡。

## 局限

1.  **大核依赖瓶颈尺寸**：63×63 核的可行性建立在瓶颈特征仅 64×64 之上；论文自己指出推理时输入远大于训练 patch，单靠 63×63 核已无法覆盖全局（这正是引入全局分支的原因）。对更高分辨率或不同瓶颈尺寸的迁移仍需重新权衡核尺寸与计算量。
2.  **任务范围**：均为单图像复原（去雾/去雪/散焦去模糊），未验证去噪、超分、去雨、视频复原或检测/分割等更广任务的迁移效果。
3.  **模块开销未细报（提取范围内）**：提取文本未给出单个 OKM 的精确 FLOPs/参数，与 Transformer 块在显存、延迟上的逐项对比也未在提取文本中体现（部分或在截断后的页中）。
4.  **退化-感受野匹配假设**：方法假设不同尺度退化可由三分支分工处理；对退化尺度与网络感受野严重失配的复杂混合退化，效果未知。
5.  **复现细节多**：需正确实现三分支并行、双域注意力的 FFT/IFFT、以及 63×63 深度大核，存在实现偏差风险。

## 个人评论

1.  **"瓶颈处用超大核 + 频域全局处理"的设计哲学**：把昂贵的大核卷积放在分辨率最低的瓶颈，使其计算量可控却换得相对原图的超大感受野；再用频域处理（FCA/FSAM）补全 63×63 仍覆盖不到的全局视野。这种"在便宜的地方花大力气"的取舍很值得借鉴。
2.  **多尺度的显式分工**：局部（1×1）、大尺度（63×63 + 条状）、全局（双域）三分支各司其职，比单纯加深/加宽更直接地覆盖了从像素细节到全局光照的退化谱系。
3.  **频域的双重利用**：频域既进入损失（Lf），又深度集成进注意力（DCAM 的 FCA、FSAM），形成"频域调制特征 + 频域约束输出"的闭环，为如何用谱信息做特征调制提供了范式。
4.  **简洁可落地**：尽管 OKM 内部组件不少，但整网仍是标准编码器-解码器 + GELU 残差块，便于复现，且作者开源了代码（c-yn/OKNet）。
5.  **一个值得追问的点**：贡献正文只列两条（模块 + 实验），其余"四点差异"在 Related Work 中陈述；阅读时需把方法/相关工作两处的卖点合并看，才能完整把握创新边界。

### 使用建议

- **如果快速了解**：读 Abstract、Introduction 首尾段、Figure 1（性能-计算权衡）、Figure 2（架构与 OKM 结构）、Table 1（SOTS 去雾）、Table 3（DPDD 去模糊）即可掌握核心。
- **如果复现**：精读 Methodology 与 Figure 2，注意 OKM 三分支与公式 (1)-(6)；Implementation Details 中的 N（去雾/去雪 4、去模糊 16、OKNet-S 为 1）、Adam/批大小 8/学习率 2e−4→1e−6 余弦退火、λ=0.1 都要照搬；Figure 3 的核尺寸曲线可作调参参考；参考官方代码 https://github.com/c-yn/OKNet。
- **如果借鉴创新点**：
    1.  **多支路并行**：按尺度/类型给特征分流处理。
    2.  **瓶颈处用大核**：在低分辨率层用超大核或动态卷积扩大相对感受野。
    3.  **双域注意力（DCAM/FSAM）**：在需要全局建模或频域线索的任务中，用 FFT/IFFT 做通道与空间调制。
- **如果写 Related Work**：可归入（1）大核卷积网络（RepLKNet、SLaK、LaKDNet、LKD-Net、MAN）；（2）高效复原 Transformer 的 CNN 对手（对标 Restormer、Fourmer、DehazeFormer）；（3）图像复原（去雾/去雪/去模糊）。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**计算机视觉 - 图像复原 (Image Restoration)** 方向，发表于 **AAAI 2024**。它面向去雾、去雪、散焦去模糊三项任务，提出一个高效卷积网络 **OKNet**，其核心是一个新型多分支模块 **Omni-Kernel Module (OKM)**。论文要解决的痛点是：Transformer 复原模型自注意力复杂度随输入二次增长、且无法捕捉多尺度感受野，而传统/大核 CNN 感受野有限、不提供全局感受野。鉴于任务全部为图像复原（去雾/去雪/去模糊），主题归入 `E_图像复原_超分_去噪_去雨去雾`（原误置于 `B_注意力算子模块`：OKM 虽是模块/算子设计，但论文题目与全部实验均围绕图像复原展开，E 更贴切）。

## 2. 一句话总结
本文提出全核模块 OKM——并行的"局部(1×1) / 大尺度(63×63 方形 + 1×63、63×1 条状深度卷积) / 全局(双域通道注意力 DCAM + 频率门控空间注意力 FSAM)"三分支，仅插入编码器-解码器的瓶颈处构成 OKNet，在 11 个基准上对去雾、去雪、散焦去模糊三任务以远低于 Transformer 的计算量取得 SOTA。

## 3. 背景与问题
- **任务**：从受 haze/snow/blur 等退化的低质图像恢复清晰图像，是高度病态问题，广泛用于监控、自动驾驶、遥感、医学成像。
- **两类深度方法的不足**：
    1.  **Transformer**：自注意力复杂度对输入二次增长，代价高；常见提效手段（限制注意力区域、改通道维注意力）会牺牲长程建模；且**无法捕捉多尺度感受野**。
    2.  **CNN / 大核 CNN**：常规卷积感受野有限；RepLKNet(31×31)、SLaK(51×51)、复原领域 LaKDNet(9×9)、LKD-Net(分解 21×21)、MAN(三种卷积分解) 虽扩大了感受野，但**仍有限且不提供全局感受野**。
- **核心矛盾**：在低复杂度下同时拿到**全局 + 多粒度 + 局部**三种感受野，以处理多尺度退化。

## 4. 核心贡献
论文原文贡献小节列两条（OKM 模块 + 11 数据集 SOTA），相关工作中补充了与同类方法的四点差异，合并理解：
1.  **OKM**：并行三分支高效捕捉多尺度感受野，大尺度信息由双域处理 + 多形状大核深度卷积调制。
2.  **OKNet + 大规模验证**：仅在瓶颈插入 OKM，11 个基准、三任务（去模糊/去雾/去雪）SOTA。
3.  首次用 **63×63** 异常大核深度卷积做复原。
4.  用 **1×K、K×1 条状深度卷积**提供不同形状感受野。
5.  用**双域处理 (DCAM+FSAM)** 提供全尺寸/全局感受野；用 **1×1 深度卷积**补局部。

## 5. 方法详解
- **框架（图 2(a)）**：编码器-解码器各 3 个尺度；ResGroup = 多个残差块，每块两个 3×3 卷积夹 GELU；OKM 仅在瓶颈。下采样用 stride=2 的 3×3 卷积，上采样用 stride=2 的 4×4 转置卷积；skip 连接 concat 后用 1×1 卷积减半通道。输入 3×3 卷积投影为 C×H×W，输出 3×3 卷积得残差图与输入相加。
- **OKM（图 2(b)）**：`X` 先过 1×1 卷积 → 三分支并行 → 逐元素相加 → 1×1 卷积调制。
    - **大尺度分支**：K×K 方形深度卷积 + 1×K、K×1 条状深度卷积并行；K 从 3 增到 63 时 PSNR/SSIM 上升（图 3），选 K=63（瓶颈特征 64×64，取最大奇数核）。
    - **全局分支**：动机是推理时图像远大于 256×256 训练 patch，63×63 覆盖不了全局。
        - DCAM（图 2(c)）：FCA `X_FCA = IF(F(X_Global) ⊗ W₁ₓ₁(GAP(X_Global)))` 公式(1)；SCA `X_DCAM = X_FCA ⊗ W₁ₓ₁(GAP(X_FCA))` 公式(2)。依谱卷积定理在频域全局调制，仅通道级粗粒度。
        - FSAM（图 2(d)）：`X_FSAM = IF(F(W¹₁ₓ₁(X_DCAM)) ⊗ W²₁ₓ₁(X_DCAM))` 公式(3)，空间维细化频谱。
    - **局部分支**：1×1 深度卷积补局部信号（表 5 验证）。
- **损失**：Lc=‖Î−Y‖₁(4)；Lf=‖F(Î)−F(Y)‖₁(5)；Lo=(1/E)(Lc+λLf)(6)，λ=0.1。
- **训练**：Adam(0.9,0.999)，batch 8，lr 2e−4→1e−6 余弦退火，256×256 patch 随机水平翻转(p=0.5)；N=4(去雾/去雪)、16(去模糊)、1(OKNet-S)；每数据集单独训模型。

## 6. 实验与结果
- **11 数据集 / 3 任务**。去雾：SOTS-Indoor/Outdoor、Dense-Haze、NH-HAZE、O-Haze、I-Haze、NHR；去模糊：DPDD；去雪：CSD。指标 PSNR/SSIM（去模糊加 MAE/LPIPS）。
- **去雾（表 1，9 法对比）**：SOTS-Indoor OKNet 40.79/0.996，比 DehazeFormer-L(40.05) 高 0.74 dB 且 FLOPs 仅 14%，比 Fourmer(37.32) 高 3.47 dB；SOTS-Outdoor 37.68/0.995；真实集全面优于 SDCE。OKNet-S 37.59/0.994，比 Fourmer 高 0.27 dB、FLOPs 少 13%。
- **夜间去雾（表 2，NHR，6 法对比）**：OKNet 27.92/0.979，比 FocalNet 高 2.57 dB / 0.01 SSIM。
- **散焦去模糊（表 3，DPDD，7 法对比）**：Combined 26.18/0.812/MAE0.037/LPIPS0.206，比 Restormer(25.98) 高 0.2 dB、参数少 46%；Indoor 28.99、Outdoor 23.51 均领先。
- **去雪（CSD）**：引言称比 IRNeXt 高 0.7 dB（结果表在提取缓存截断之后，据原文后续页，提取缓存未覆盖，待核）。
- **消融**：核尺寸图 3（3→63 单调提升）；局部分支表 5（据原文后续页，提取缓存未覆盖具体数字，待核）。

## 7. 这篇论文真正有价值的地方
1.  **瓶颈处大核 + 频域全局**：在 64×64 瓶颈用 63×63 大核，计算可控却得超大相对感受野；再用频域分支补全局视野，是一种清晰的"大感受野与低成本"折中。
2.  **多尺度显式分工**：局部/大尺度/全局三分支各管一段退化谱系，模块化且直观。
3.  **频域双重利用**：频域既进损失又进注意力（FCA/FSAM），形成"频域调制 + 频域约束"闭环。
4.  **简洁可复现 + 开源**：整网为标准编解码器，作者提供代码（c-yn/OKNet）。

## 8. 局限与问题
1.  63×63 核可行性强绑定瓶颈 64×64；换分辨率/瓶颈尺寸需重新权衡（论文自承推理时单核无法覆盖全局，才加全局分支）。
2.  仅单图复原任务，未验证去噪/超分/去雨/视频复原及检测分割等迁移。
3.  提取文本范围内未给单个 OKM 的精确 FLOPs/参数及与 Transformer 块的显存/延迟逐项对比（或在截断后的页）。
4.  "退化尺度可由三分支分工"是较强假设，混合复杂退化效果未知。
5.  三分支并行 + FFT/IFFT + 63×63 深度大核实现细节多，存在偏差风险。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract、Intro 首尾、Fig 1、Fig 2、Table 1、Table 3。
- **复现**：Methodology + Fig 2 + 公式(1)-(6)；N/优化器/lr/λ 照搬；Fig 3 调参参考；官方代码 https://github.com/c-yn/OKNet。
- **借鉴**：多支路并行、瓶颈处用大核、双域注意力（DCAM/FSAM）。
- **写 Related Work**：大核 CNN（RepLKNet/SLaK/LaKDNet/LKD-Net/MAN）、高效复原 Transformer 的 CNN 对手（Restormer/Fourmer/DehazeFormer）、图像复原（去雾/去雪/去模糊）。

## 10. 和其他论文的关系
- **大核 CNN**：`[[RepLKNet]]`(31×31)、`[[SLaK]]`(51×51)、`[[LaKDNet]]`(9×9)、`[[LKD-Net]]`(分解 21×21)、`[[MAN]]`(大核注意力)。
- **复原 Transformer / 频域复原**：`[[Restormer]]`、`[[Fourmer]]`、`[[DehazeFormer]]`、`[[SFNet]]`(动态选频)。
- **通道/频域注意力基础**：`[[FFA-Net]]`(通道+像素注意力)、`[[FcaNet]]`(频域通道注意力)、`[[SENet]]`、`[[CBAM]]`。
- **同主题**：`[[E_图像复原_超分_去噪_去雨去雾]]` 主题首页。

## 11. 关键词
图像复原, 去雾, 去雪, 散焦去模糊, 全核模块 OKM, 大核卷积 (63×63), 条状卷积, 双域通道注意力 DCAM, 频率门控空间注意力 FSAM, FFT/频域处理, 编码器-解码器, 计算效率, OKNet, AAAI 2024

## 12. 可信度说明
本精读基于提取缓存 `.paper-cache/extracts/OKM.txt`。**注意**：该缓存标注 9/9 页，但实际只保留前 **25000 字符**（原文约 41760 字符），覆盖到 DPDD 表 3 即截断；**去雪 CSD 结果表、表 5 局部分支消融、以及后续页的部分内容未包含在提取文本中**，相关数字（如 CSD 上 +0.7 dB 见引言、表 5 仅引言提及）已据原文前文/引言交叉印证并标注"待核"。摘要、引言、方法（架构、全部公式 1-6）、去雾表 1、夜间去雾表 2、去模糊表 3 的全部数字均直接出自提取文本，逐一核对一致。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本清晰, 公式与表格数字完整可读); 但缓存被 25000 字符上限截断 (原文 ~41760 字符), 仅覆盖前 ~6 页内容 (至 DPDD 表 3), 去雪结果表/表 5 消融未包含; 来源缓存: `.paper-cache/extracts/OKM.txt` (标注 9/9 页, 实为前 25000 字符); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
