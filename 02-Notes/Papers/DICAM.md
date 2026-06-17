---
title: "DICAM: Deep Inception and Channel-wise Attention Modules for underwater image enhancement"
authors:
  - "Hamidreza Farhadi Tolie"
  - "Jinchang Ren"
  - "Eyad Elyan"
year: 2024
venue: "Neurocomputing 584 (2024) 127585"
doi: 10.1016/j.neucom.2024.127585
pdf: [[DICAM.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
extract_cache: .paper-cache/extracts/DICAM.txt
---

# DICAM: Deep Inception and Channel-wise Attention Modules for underwater image enhancement

## 基本信息
- **PDF**: [[DICAM.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`, `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03
- **开源代码**: https://github.com/hfarhaditolie/DICAM

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | DICAM: Deep Inception and Channel-wise Attention Modules for underwater image enhancement |
| **作者** | Hamidreza Farhadi Tolie; Jinchang Ren; Eyad Elyan (Robert Gordon University, UK) |
| **发表时间** | 2024 (Received 11 Sep 2023; Accepted 19 Mar 2024) |
| **刊物/会议** | Neurocomputing, 卷 584, 文章号 127585 (Elsevier) |
| **DOI** | 10.1016/j.neucom.2024.127585 |

## 摘要

**清理后的英文原摘要**（据 PDF 提取文本整理，修复断字与空格）：

> In underwater environments, imaging devices suffer from water turbidity, attenuation of lights, scattering, and particles, leading to low quality, poor contrast, and biased color images. This has led to great challenges for underwater condition monitoring and inspection using conventional vision techniques. In recent years, underwater image enhancement has attracted increasing attention due to its critical role in improving the performance of current computer vision tasks in underwater object detection and segmentation. As existing methods, built mainly from natural scenes, have performance limitations in improving the color richness and distributions, we propose a novel deep learning-based approach namely **Deep Inception and Channel-wise Attention Modules (DICAM)** to enhance the quality, contrast, and color cast of the hazy underwater images. The proposed DICAM model enhances the quality of underwater images, considering both the **proportional degradations** and **non-uniform color cast**. Extensive experiments on two publicly available underwater image enhancement datasets have verified the superiority of our proposed model compared with several state-of-the-art conventional and deep learning-based methods in terms of full-reference and reference-free image quality assessment metrics. The source code of our DICAM model is available at https://github.com/hfarhaditolie/DICAM.

**中文翻译**：

> 在水下环境中，成像设备受水体浑浊、光线衰减、散射和悬浮颗粒影响，得到的图像质量低、对比度差、色彩偏移。这给用常规视觉技术进行水下状态监测与巡检带来巨大挑战。近年来，水下图像增强因在水下目标检测与分割等视觉任务中的关键作用而日益受到关注。鉴于现有方法多为自然场景设计、在提升色彩丰富度与分布方面存在局限，本文提出一种新的基于深度学习的方法——深度 Inception 与通道注意力模块（DICAM），用于提升模糊水下图像的质量、对比度与色偏。所提 DICAM 模型在增强水下图像质量时同时考虑了**比例退化**与**非均匀色偏**两类问题。在两个公开水下图像增强数据集上的大量实验表明，本模型在全参考与无参考图像质量评估指标上优于多种先进的传统及深度学习方法。模型源码已开源于 https://github.com/hfarhaditolie/DICAM。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：随着面向 Net-Zero 的海洋工程与生态发展，海底资源的自动巡检/保护/监测成为热点。水下图像/视频可服务于能源基础设施状态监测、海床视觉测绘、垃圾检测、水下目标与事件（鱼类、物种、管道失效等）的检测分类。但水体浑浊、光线衰减、悬浮颗粒导致原始水下图像（UIs）出现**非均匀色偏**和**模糊**，质量、对比度、亮度都很低。
- **两类核心退化**（论文方法部分明确界定）：
    1. **比例退化（proportional degradation）**：退化程度与"物体到相机的距离"成比例（图 1 中远处高亮区域比近处中心区域模糊得多），即图像不同区域退化率不同。
    2. **非均匀光衰减（non-uniform light attenuation）→ 色偏**：导致大多数水下图像偏蓝或偏绿。
- **三类已有方法及其问题**（论文将 UIE 方法分为三组）：
    1. **非物理模型方法**（HE、CLAHE、ICM、UCM、多尺度融合、各类 Retinex 等）：仅修改像素强度值，依赖经验设定参数，未考虑水下环境复杂性与光照，易产生噪声、伪影、色彩失真，泛化能力差。
    2. **物理模型方法**（IFM、DCP、UDCP、IBLA、ULAP、color-line、分层搜索等）：用数学退化模型 + 先验（如暗通道）求逆问题；因 IFM 病态、参数估计复杂，普遍**耗时、视觉不佳、对海洋/近岸等不同水下类型与退化程度敏感**。
    3. **深度学习方法**（GAN / CNN / 编码器-解码器，如 UResNet、Water-Net、FUnIE-GAN、UIEC²-Net、WaveNet）：多为弱监督 GAN 或通用 CNN，未充分针对水下"颜色非均匀衰减"和"比例退化"——而由于红光衰减最快、其次绿光、再次蓝光，需要**从每个颜色通道以不同比例提取特征并自适应加权融合**才能精确校色。
- **核心矛盾**：水下退化具有**通道相关性**（红光衰减最快）与**空间非均匀性**（远处更模糊、信息损失程度不一），而现有方法缺乏对这两种特性的联合建模与自适应加权融合。作者由此提出"半自适应特征尺寸（semi-adaptive feature size）"来从原始水下图像提取有效特征。

## 关键贡献

论文在引言末尾明确列出**两条**主要贡献（原文 "(1)…(2)…"）：

1.  **多尺度通道级特征提取**：使用 Inception 模块同时量化"与颜色及距离相关的比例退化、颜色与内容信息损失、色彩丰富度"。
2.  **基于自适应融合的恢复与增强**：引入通道注意力模块（CAM）实现自适应融合，并通过专门的颜色校正阶段生成色偏更准、色彩更丰富、外观更自然的高质量增强图像。

> 补充（本笔记归纳，非原文逐字"贡献"项，但有原文支撑）：CAM 在网络中被用于**两个阶段**（通道级特征提取后、颜色校正后）；CAM 相对 CBAM 去除空间注意力、并以 **Softsign** 替代 SE 中的 ReLU/Sigmoid 从而支持**负权重**；在 UIEB 与 EUVP 两个公开数据集上做了全参考与无参考评测，并比较了运行时间。

## 方法

- **整体框架**（图 2）：网络串联三阶段——(1) 通道级颜色恢复（Channel-level color recovery）；(2) 颜色校正（Color correction）；(3) 维度降低（Dimension reduction）。全程保持输入空间分辨率 256×256 不变。
- **关键模块**：
    1. **Inception 模块（Inc）**（图 3(a)、表 1）：并行 1×1、3×3、5×5 卷积与 Max-Pooling 四条支路，分别捕获像素级、局部、更大范围结构信息及（Max-Pooling 得到的）轮廓信息。表 1 给出：每支路 stride=1、padding 分别 0/1/2、输出通道 **64**，输出尺寸 64×256×256；拼接后得 **256×256×256**（即 4×64 通道）。每个卷积层后接 **LeakyReLU**。两个阶段（颜色恢复与颜色校正）的 Inc 模块滤波器数均为 64。
    2. **通道注意力模块（CAM）**（图 3(b)）：受 CBAM 与 Squeeze-and-Excitation 启发，将每个输入特征图映射为单个系数。流程：
        - **全局平均池化（GAP）**：沿空间维 H×W 压缩每个特征图，得 `GAP_m ∈ R^M`（式 1）。
        - **激励（Excitation）**：先以比例 **r=4**（经验设定）降维、再升回原维度；系数向量 `Coeff_m = ψ(C2·ψ(C1·GAP_m))`（式 2），其中 ψ 为 **Softsign**，`C1 ∈ R^{(M/r)×M}`、`C2 ∈ R^{M×(M/r)}` 为两个全连接层。
        - 与 SE 不同的是：在降维**与**升维之后都用 **Softsign**，使权重落在 **[−1, +1]**，从而允许学习**负权重**。
        - **特征加权**：`F_m = F_m ⊗ Coeff_m`（式 3），逐通道相乘精炼特征。
- **三阶段连接**：
    - **阶段 1 通道级颜色恢复**：因颜色按波长以不同速率衰减（红 > 绿 > 蓝），从每个颜色通道**分别**用 Inc 提取多尺度特征，再用 CAM 对各尺度/轮廓特征加权（因 3×3、5×5、轮廓三类信息的退化比例不等），监督学习中据此判别空间域中各颜色通道的信息损失程度。
    - **阶段 2 颜色校正**：将阶段 1 的特征图拼接后，**再过一个 Inc** 在更高层捕获退化，并**再用 CAM** 加权——此处 CAM 让模型对"信息损失率更高的颜色通道"赋更大权重，从而恢复丢失的颜色、完成校色。Softsign 的负权重能**主动压制**偏强的蓝/绿通道，进而更自由有效地利用它们生成真实色彩。
    - **阶段 3 维度降低**：为生成 RGB 输出，仅需减少特征数（空间分辨率全程不变）。采用**渐进式**降通道，初始步用 3×3 卷积以在降维同时保留信息，最后用 **Sigmoid** 把输出归一化到 [0,1]。
- **训练损失**（式 4）：三项之和 `L = L1 + L_SSIM + L_perceptual`。因 L1 与 SSIM 损失更兼容，L1 既直接使用、也用于感知损失中（式 5：`L1 = ‖Ĝ − G‖_1`，G 为真值、Ĝ 为生成图）。
  > 注：提取文本中总损失写作 "= L1 + SSIM + Lp"（系数符号未明确给出加权系数），未见显式权重数值；感知损失基于预训练网络（提取文本未点明具体 backbone，常见为 VGG，待核）。
- **与已有方法的差异**：
    - 对传统方法：DICAM 数据驱动，无需手工特征或物理先验假设，更能处理复杂退化。
    - 对其他深度方法：强调**通道分离 + 多尺度**（区别于直接处理三通道的 UResNet、Water-Net）；CAM 比 CBAM 参数更少（去掉空间注意力、仅用平均池化），降低学习/推理时间并提升增强质量；用 Softsign 引入负权重做校色（区别于 SE 的 ReLU/Sigmoid）。WaveNet 同样分通道处理并分三步融合，但用的是 CBAM。

## 实验

- **使用数据集**：
    1.  **UIEB**：有配对参考图的水下增强数据集（论文用作训练/测试，表 2 在 UIEB 测试子集上评测）。
        > 原笔记记"890 张、500 训练 / 90 测试"——提取缓存（前 5 页）未覆盖此数字，据原文后续页推断，待核。
    2.  **EUVP**：用于无参考质量评估（提取缓存未覆盖其规模/配对情况，据原文后续页，待核）。
- **对比方法**：
    - **传统/物理方法**（表 2 实列）：CLAHE、ICM、DCP、Fusion-based、UDCP、Retinex-based、IBLA、ULAP。
    - **深度学习方法**（引言述及，用作对比基线）：UResNet、Water-Net、FUnIE-GAN、UIEC²-Net、WaveNet。
- **评价指标**：
    - **全参考(FR)**：SSIM↑、PCQI↑、PSNR↑、MSE↓。
    - **无参考(NR)**：UIQM↑、UCIQE↑，以及 MSE_UIQM↓、MSE_UCIQE↓。
- **主实验结果（表 2，UIEB 测试子集，DICAM 与传统方法对比）**：

  | 指标 | DICAM | 该列最优(非DICAM) |
  |---|---|---|
  | SSIM↑ | **0.9375** | 0.8916 (Fusion) |
  | PCQI↑ | 0.9007 | **0.9266 (CLAHE)** |
  | PSNR↑ | **24.43** | 22.10 (Fusion) |
  | MSE↓ | **0.0060** | 0.0119 (Fusion) |
  | UIQM↑ | **3.06** | 2.76 (Retinex) |
  | UCIQE↑ | 0.5547 | **0.5599 (Fusion)** |
  | MSE_UIQM↓ | **0.1188** | 0.1462 (Retinex) |
  | MSE_UCIQE↓ | **0.0012** | 0.0013 (Retinex) |

  - 在 SSIM、PSNR、MSE、UIQM、MSE_UIQM、MSE_UCIQE 上 DICAM 取得（该对比表内）最优；**但 PCQI（0.9007 < CLAHE 0.9266）与 UCIQE（0.5547 < Fusion-based 0.5599）并非最优**——原笔记"在所有全参考指标上均取得最优"的说法不成立，已据表 2 修正。
  - 表 2 仅列传统方法对比；与深度学习方法（UResNet/Water-Net/FUnIE-GAN/UIEC²-Net/WaveNet）的量化对比表在提取缓存未覆盖的后续页，据原文后续页，待核。
- **消融实验**：论文提及验证 CAM 与 Inception 的有效性，但具体消融数值在提取缓存（前 5 页，截断于表 2 后）未覆盖，据原文后续页，待核。
- **泛化/无参考实验**：在 EUVP 上做无参考评测，具体数值同上待核。
- **效率信息**：摘要/引言提到比较了 run-time，CAM 去除空间注意力"减少学习与推理时间"，但具体参数量、FLOPs、运行时间数值在提取缓存未覆盖，据原文后续页，待核。

## 局限

1.  **场景特异性**：模型专为水下增强设计，"通道分离 + 比例退化假设"可能限制其直接迁移到雾天、低光照等其它退化任务（本笔记推断，原文未明确讨论可迁移性）。
2.  **数据依赖**：作为监督式深度模型，性能依赖训练数据规模与多样性；对更极端/罕见水下场景的泛化需进一步检验。
3.  **效率指标缺数**：虽称 CAM 降低时间且做了 run-time 比较，但提取文本（前 5 页）未给出参数量/FLOPs/速度的具体数字（据原文后续页，待核）。
4.  **超参数依赖**：CAM 压缩比 `r` 经验设为 4，其最优性与敏感性论文未深入分析。
5.  **指标非全面领先**：表 2 显示 DICAM 在 PCQI、UCIQE 上未超过部分传统方法，说明其优势集中在保真度/结构与 UIQM 类指标，色彩定量指标上并非全面占优。

## 个人评论

1.  **问题拆解清晰**：把水下退化明确拆为"通道相关衰减（颜色按波长不同速率衰减）"与"空间比例退化（与距离成比例）"，并分别对应"通道分离处理"和"多尺度 Inception"，这种从问题本质出发的模块映射很有借鉴价值。
2.  **轻量且方向独特的注意力**：CAM 简化 CBAM、去掉空间注意力专注通道维；最值得注意的是用 **Softsign** 把权重放到 [−1,+1] 从而允许**负权重**——这让注意力从单纯"增强"扩展到"主动减法/抑制过强色偏（蓝/绿）"，对校色任务很贴切，是对 SE/CBAM 这类"只放大"机制的有益补充。
3.  **两阶段 CAM 的自适应思路**：阶段 1 做"通道内多尺度精炼"、阶段 2 做"通道间融合校色"，把自适应加权布置在网络不同层次，"先分后合、逐步精炼"的范式可迁移到其它存在通道/模态特性差异的任务。
4.  **诚实但可更细的评测**：表 2 显示其优势并非全指标领先（PCQI、UCIQE 落后于个别传统法），若能在笔记/原文中正视这一点，对方法定位会更准确。

### 使用建议

- **快速了解**：读摘要、图 2（框架）、表 2（主结果）即可掌握核心思想、方法与效果。
- **复现**：精读第 2 节（2.1–2.5），重点是表 1（Inc 架构：四支路各 64 通道、拼接 256）、图 3、式 1–5（CAM 与损失），并参考官方代码 https://github.com/hfarhaditolie/DICAM。
- **借鉴创新点**：
    - **CAM 模块**："GAP → FC降维(r=4) → FC升维 → 双 Softsign → 通道加权"，可迁移到需要轻量、且希望支持负权重的通道注意力场景。
    - **多通道分离处理**：对通道/模态特性差异显著的多通道输入，参考其"先分后合"框架。
- **写相关工作**：可置于"基于深度学习的水下图像增强"小节，作为"多尺度特征提取 + 通道注意力 + 显式校色阶段"的代表性 CNN 方法，与 GAN 路线（FUnIE-GAN）和多频带/CBAM 路线（WaveNet）对照。

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
属于**计算机视觉 / 低层视觉**中的**图像复原与增强**方向，具体为**水下图像增强（Underwater Image Enhancement, UIE）**。它是水下目标检测、分割等下游任务的关键前置步骤。方法层面以"多尺度 Inception 特征提取 + 通道注意力（CAM）自适应融合 + 专用校色阶段"为核心，因此主题归到 `E_图像复原_超分_去噪_去雨去雾`（以增强/复原为本质任务），并以 `B_注意力算子模块` 为次要主题（CAM 是其关键算子贡献）。

## 2. 一句话总结
DICAM 用通道分离的多尺度 Inception 提特征、并用引入 Softsign 负权重的轻量通道注意力（CAM）做两阶段自适应加权与显式校色，同时缓解水下图像的**比例退化**与**非均匀色偏**，在 UIEB/EUVP 上的多数全参考与无参考指标上优于传统及部分深度方法。

## 3. 背景与问题
- **为什么做**：水体浑浊、光衰减、散射与颗粒导致原始水下图像低质、低对比、偏色，制约水下监测、目标检测/分割等任务。
- **两类核心退化**：(1) **比例退化**——退化随物体-相机距离成比例（远处更模糊，图 1）；(2) **非均匀光衰减→色偏**——多数图像偏蓝/绿，且红光衰减最快、其次绿、再次蓝。
- **三类已有方法的不足**：非物理模型（HE/CLAHE/ICM/Retinex 等）仅改像素强度、依赖经验参数、易出伪影且泛化差；物理模型（IFM/DCP/UDCP/IBLA/ULAP 等）依赖先验、参数估计复杂、耗时且对水型与退化程度敏感；深度方法（GAN/CNN/编解码，如 UResNet/Water-Net/FUnIE-GAN/UIEC²-Net/WaveNet）多为弱监督或通用结构，未针对"通道非均匀衰减 + 比例退化"做差异化的逐通道多尺度提取与自适应加权。

## 4. 核心贡献
原文明列两条：
1. **多尺度通道级特征提取**：用 Inception 同时量化颜色/距离相关的比例退化、颜色与内容信息损失、色彩丰富度。
2. **自适应融合恢复与增强**：引入 CAM 做自适应融合，并经专门的颜色校正阶段生成色偏更准、色彩更丰富、外观更自然的图像。
（衍生要点：CAM 用于两个阶段；CAM 相对 CBAM 去空间注意力、用 Softsign 支持负权重；UIEB+EUVP 全参考与无参考评测并比较 run-time。）

## 5. 方法详解
- **三阶段框架（图 2）**：通道级颜色恢复 → 颜色校正 → 维度降低；全程保持 256×256 空间分辨率。
- **Inception（表 1、图 3a）**：1×1 / 3×3 / 5×5 / Max-Pooling 四支路，stride=1，输出各 64 通道（64×256×256），拼接 256×256×256（4×64）；每卷积后 LeakyReLU；两阶段 Inc 均 64 滤波器。
- **CAM（图 3b、式 1–3）**：GAP 压缩空间维 → FC 以比例 r=4 降维 → FC 升回原维 → 系数 `Coeff_m = ψ(C2·ψ(C1·GAP_m))`，ψ=Softsign，权重∈[−1,+1]（支持负权重）→ `F_m = F_m ⊗ Coeff_m` 逐通道加权。相对 SE/CBAM：去空间注意力、仅平均池化、参数更少、用 Softsign 引入负权重。
- **阶段语义**：阶段 1 对 R/G/B 分别 Inc 提多尺度特征后 CAM 加权（平衡 3×3/5×5/轮廓退化比例不等）；阶段 2 拼接后再 Inc + CAM，对"信息损失更大的颜色通道"赋更大权重做校色，负权重主动抑制偏强蓝/绿；阶段 3 渐进降通道（初始 3×3 卷积保信息）+ Sigmoid 归一到 [0,1] 出 RGB。
- **训练（式 4–5）**：`L = L1 + L_SSIM + L_perceptual`；L1 既直接用又入感知损失，`L1=‖Ĝ−G‖_1`。感知损失 backbone 提取文本未点明（常见 VGG，待核）。

## 6. 实验与结果
- **数据集**：UIEB（配对，表 2 测试子集评测；890 张 / 500 训 / 90 测 据原文后续页待核）、EUVP（无参考评测，规模据原文后续页待核）。
- **对比**：传统/物理 = CLAHE/ICM/DCP/Fusion-based/UDCP/Retinex-based/IBLA/ULAP（表 2 实列）；深度 = UResNet/Water-Net/FUnIE-GAN/UIEC²-Net/WaveNet（引言述及，量化对比表在提取缓存未覆盖，待核）。
- **指标**：FR = SSIM↑/PCQI↑/PSNR↑/MSE↓；NR = UIQM↑/UCIQE↑/MSE_UIQM↓/MSE_UCIQE↓。
- **表 2 关键数（DICAM）**：SSIM 0.9375、PCQI 0.9007、PSNR 24.43、MSE 0.0060、UIQM 3.06、UCIQE 0.5547、MSE_UIQM 0.1188、MSE_UCIQE 0.0012。DICAM 在 SSIM/PSNR/MSE/UIQM/MSE_UIQM/MSE_UCIQE 上为该表最优；**PCQI 低于 CLAHE(0.9266)、UCIQE 低于 Fusion-based(0.5599)，并非全指标领先**。
- **消融 / 与深度方法对比 / 效率(参数量·FLOPs·速度) / EUVP 数值**：提取缓存截断于表 2 之后，均未覆盖，据原文后续页待核。

## 7. 这篇论文真正有价值的地方
1. **退化拆解→模块映射**：把"通道相关衰减"和"空间比例退化"分别对应"通道分离"和"多尺度 Inception"，问题驱动的设计清晰。
2. **支持负权重的通道注意力**：用 Softsign 把注意力扩展到 [−1,+1]，让模型能"主动抑制"过强色偏通道，契合校色任务，区别于 SE/CBAM 的只放大。
3. **两阶段 CAM + 显式校色**："通道内精炼 + 通道间融合校色"的分层自适应，且把校色单列为一个阶段，思路可迁移到多通道/多模态任务。

## 8. 局限与问题
1. **场景特异**：通道分离与比例退化假设可能限制向雾天/低光等任务迁移（本笔记推断）。
2. **数据依赖**：监督模型，泛化依赖数据规模与多样性。
3. **效率缺数**：称比较了 run-time 且 CAM 省时，但提取文本未给参数量/FLOPs/速度数值（待核）。
4. **超参 r=4 经验设定**，未做敏感性分析。
5. **非全指标领先**：PCQI、UCIQE 落后于个别传统法，色彩定量指标上未占优。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 图 2 + 表 2。
- **复现**：第 2 节 2.1–2.5 + 表 1 + 图 3 + 式 1–5，配合官方代码 https://github.com/hfarhaditolie/DICAM。
- **借鉴**：CAM（GAP→FC降(r=4)→FC升→双Softsign→通道加权，支持负权重）可迁移到轻量通道注意力场景；"先分后合"框架可用于通道/模态差异显著的多通道输入。
- **写相关工作**：列入"深度学习水下图像增强"，作为"多尺度 + 通道注意力 + 显式校色"代表方法，与 FUnIE-GAN（GAN 路线）、WaveNet（CBAM/多频带路线）对照。

## 10. 和其他论文的关系
- **注意力机制**：CAM 借鉴并改进 `[[CBAM: Convolutional Block Attention Module]]` 与 `[[Squeeze-and-Excitation Networks]]`（去空间注意力、引入 Softsign 负权重）。
- **水下图像增强**：与 `[[WaveNet: Multi-band network for underwater image enhancement]]`（同为分通道处理，但用 CBAM）、`[[Water-Net: A Convolutional Neural Network for Underwater Image Enhancement]]`、`[[UIEC2-Net]]`（双色彩空间）同属 CNN 路线；与 `[[FUnIE-GAN: Fast Underwater Image Enhancement]]` 的 GAN 路线对照。
- **多尺度特征提取**：Inc 模块源自 `[[Going Deeper with Convolutions (GoogLeNet/Inception)]]`，是经典 Inception 在 UIE 任务中的应用。

## 11. 关键词
水下图像增强, 深度学习, Inception 模块, 通道注意力模块(CAM), 多尺度特征提取, 自适应融合, 颜色校正, 非均匀色偏, 比例退化, Softsign 负权重, 图像质量评估(SSIM/PSNR/UIQM/UCIQE)

## 12. 可信度说明
本精读基于提取缓存 `.paper-cache/extracts/DICAM.txt`。该缓存标注 11/11 页，但设有 25000 字符上限（原文共约 67104 字符），实际**截断于第 5 页表 2 之后的训练/结果部分**，因此完整覆盖了：标题、作者、摘要、引言（含三类方法综述与两条贡献）、方法全节（2.1–2.5，含表 1 Inc 架构、式 1–5 的 CAM 与损失）、表 2（DICAM 与 8 个传统方法在 UIEB 测试子集的全/无参考指标）。**未覆盖**：消融实验具体数值、与深度学习方法（UResNet/Water-Net/FUnIE-GAN/UIEC²-Net/WaveNet）的量化对比表、参数量/FLOPs/运行时间、UIEB 的 890/500/90 规模与 EUVP 细节、感知损失 backbone——这些点已在正文标注"据原文后续页待核"。已据表 2 纠正原笔记"全参考指标全部最优"的错误（PCQI、UCIQE 非最优）。已修正被乱码污染的标题/刊名/主题分类。

---

> **可信度补充**: PDF 提取质量 = **high**（提取文本清晰、公式与表 1/表 2 可读；但受 25000 字符上限影响，实际只覆盖到第 5 页表 2，约前半篇，后续实验细节未入缓存）；来源缓存: `.paper-cache/extracts/DICAM.txt`（标注 11/11 页，实际截断于约第 5 页）；生成日期: 2026-06-05；模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
