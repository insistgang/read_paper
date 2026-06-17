---
title: Spatially-Adaptive Feature Modulation for Efficient Image Super-Resolution
authors:
  - "Long Sun"
  - "Jiangxin Dong"
  - "Jinhui Tang"
  - "Jinshan Pan"
year: 2023
venue: "ICCV"
doi: 
pdf: [[FMM.pdf]]
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
extract_cache: .paper-cache/extracts/FMM.txt
---

# Spatially-Adaptive Feature Modulation for Efficient Image Super-Resolution

## 基本信息
- **PDF**: [[FMM.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`, `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Spatially-Adaptive Feature Modulation for Efficient Image Super-Resolution |
| **作者** | Long Sun; Jiangxin Dong; Jinhui Tang; Jinshan Pan（南京理工大学计算机科学与工程学院） |
| **发表时间** | 2023 |
| **刊物/会议** | ICCV |
| **DOI** | 未明确 |
| **代码** | https://github.com/sunny2109/SAFMN |

## 摘要

> **英文原摘要（据 PDF 提取文本整理，已修复空格/连字符断裂、剔除混入的图轴数字）**：
> Although deep learning-based solutions have achieved impressive reconstruction performance in image super-resolution (SR), these models are generally large, with complex architectures, making them incompatible with low-power devices with many computational and memory constraints. To overcome these challenges, we propose a spatially-adaptive feature modulation (SAFM) mechanism for efficient SR design. In detail, the SAFM layer uses independent computations to learn multi-scale feature representations and aggregates these features for dynamic spatial modulation. As the SAFM prioritizes exploiting non-local feature dependencies, we further introduce a convolutional channel mixer (CCM) to encode local contextual information and mix channels simultaneously. Extensive experimental results show that the proposed method is 3× smaller than state-of-the-art efficient SR methods, e.g., IMDN, and yields comparable performance with much less memory usage. Our source codes and pre-trained models are available at: https://github.com/sunny2109/SAFMN.

> **中文翻译**：尽管基于深度学习的图像超分辨率（SR）方案已取得令人印象深刻的重建性能，但这些模型普遍庞大、结构复杂，难以适配计算与内存受限的低功耗设备。为应对这些挑战，本文提出一种空间自适应特征调制（SAFM）机制以实现高效 SR 设计。具体而言，SAFM 层使用相互独立的计算来学习多尺度特征表示，并将这些特征聚合用于动态空间调制。由于 SAFM 侧重于挖掘非局部特征依赖，本文进一步引入一个卷积通道混合器（CCM）来编码局部上下文信息并同时混合通道。大量实验结果表明，所提方法比当前最先进的高效 SR 方法（如 IMDN）小 3 倍，且在显著更少的内存占用下取得了相当的性能。源代码与预训练模型见 https://github.com/sunny2109/SAFMN。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：基于深度学习的 SR 方法性能优异，但模型普遍庞大复杂。论文以 RCAN 为典型反例——它有 15.59M 参数、深度超过 400 层，高计算成本使其难以部署。同时，视觉 Transformer（ViT，如 SwinIR）通过自注意力捕捉非局部特征交互，在低层视觉任务上超越 CNN，证明非局部特征交互对高质量重建至关重要；但现有自注意力机制计算昂贵，不利于高效 SR 设计。作者由此希望融合卷积与自注意力的优点，设计轻量而有效的 SR 模型。
- **之前方法的两条技术路线及其问题**：
    1. **减少模型参数/复杂度（FLOPs）**：采用递归（recursive）、参数共享、稀疏卷积等策略。这些方法虽减小了模型，但常因共享递归模块或稀疏卷积带来性能下降，往往要靠增加深度/宽度来补偿，反而影响 SR 重建时的推理效率。
    2. **加速推理时间**：后上采样（post-upsampling，替代预定义放大输入）显著加快运行时；模型量化降低延迟与能耗（尤其边缘设备）；结构重参数化提升已训练模型的推理速度。这些方法运行快但重建性能较差。
- **核心矛盾**：模型效率与重建性能之间的权衡仍有提升空间。论文强调效率应从多维度衡量——参数量、FLOPs、激活数、内存占用、推理时间，目标是在这些维度上找到更优的折中点。

## 关键贡献

1.  开发了一种高效的**特征调制机制（SAFM）**，用以学习特征依赖关系，兼具"CNN 般的高效"与"Transformer 般的自适应性"。它借鉴多头自注意力（MHSA）的并行独立计算范式，让各分支处理不同尺度信息，再聚合生成注意力图进行空间自适应调制。
2.  提出一个紧凑的**卷积通道混合器（CCM）**，基于 FMBConv 设计，能同时编码局部上下文信息并执行通道混合，以补充 SAFM 侧重的非局部信息。
3.  在基准数据集上对所提方法进行定量与定性评估，结果表明 SAFMN 在**精度与模型复杂度之间取得良好权衡**（模型规模约为 IMDN 的 1/3，×4 时参数 240K vs IMDN 715K）。

## 方法

- **整体框架（图 3）**：SAFMN 由三部分组成——(1) 一个 3×3 浅层卷积，将 LR 图像变换到特征空间得到浅层特征 F₀；(2) 多个堆叠的特征混合模块（FMM）从 F₀ 提取更精细的深层特征；(3) 一个轻量上采样器（仅含一个 3×3 卷积 + 一个 pixel-shuffle 层）重建 HR 图像。网络使用全局残差连接来学习高频细节。
- **输入输出**：输入低分辨率（LR）图像，输出对应高分辨率（HR）图像。
- **关键模块**：
    1.  **空间自适应特征调制（SAFM，图 4，公式 1-3）**：
        - **动机**：标准卷积高效但受静态权重和局部性限制；MHSA 具长程交互与动态空间加权能力但昂贵。SAFM 借鉴 MHSA 的"多头并行独立计算"思想来增强卷积的表达能力。
        - **多尺度特征生成（MFGU）**：先将归一化后的输入特征 X 沿通道分为 4 组 [X₀,X₁,X₂,X₃]。第一组 X₀ 用一个 3×3 深度卷积处理（X̂₀ = DW-Conv₃ₓ₃(X₀)）；其余三组先经**自适应最大池化**下采样到 p/2ⁱ（i=1,2,3，即原尺寸的 1/2、1/4、1/8），再过 3×3 深度卷积，最后用最近邻插值上采样回原分辨率 p（X̂ᵢ = ↑ₚ(DW-Conv₃ₓ₃(↓ₚ/2ⁱ(Xᵢ)))）。这样从不同表示子空间获得不同感受野的短程/长程特征。
        - **特征聚合（公式 2）**：将四分支特征沿通道拼接，再过 1×1 卷积融合，得到聚合表示 X̂ = Conv₁ₓ₁(Concat([X̂₀,X̂₁,X̂₂,X̂₃]))。
        - **空间自适应调制（公式 3）**：对 X̂ 施加 GELU 非线性 φ(·) 估计注意力图，再与原始输入 X 逐元素相乘得调制输出 X̄ = φ(X̂)⊙X。论文在表 3 中比较了这些算子的收益（消融，提取文本未含表 3 数值）。
    2.  **卷积通道混合器（CCM）**：基于 FMBConv。结构为 3×3 卷积（编码空间局部上下文，并将通道数**加倍**用于通道混合）→ 隐藏层 GELU 非线性 → 1×1 卷积（将通道数降回原始输入维度）。
    3.  **特征混合模块（FMM，公式 4）**：将 SAFM 与 CCM 统一为一个 FMM：
        - `Y = SAFM(LN(X)) + X`
        - `Z = CCM(LN(Y)) + Y`
        - 其中 LN 为 LayerNorm。两处残差学习用于稳定训练、学习高频细节以利于高质量重建。
- **训练方式**：
    - 数据：DIV2K + Flickr2K 作训练集，通过 bicubic 下采样生成 LR；数据增强为随机水平翻转和旋转。
    - 输入块：从 LR 图像随机裁剪 64 个 64×64 像素块作为基本训练输入。
    - 网络配置：FMM 数量 = 8，特征通道数 = 36。
    - 优化：Adam（β₁=0.9, β₂=0.99），迭代 500,000 次；学习率由 1×10⁻³ 余弦退火至 1×10⁻⁵。
    - 损失：MAE 损失 + 基于 FFT 的频率损失（与 ShuffleMixer 一致）。
    - 平台：PyTorch，单张 NVIDIA GeForce RTX 3090。
- **推理流程**：标准前馈——LR 输入 → 浅层卷积 → 堆叠 FMM → 上采样器 → HR 输出。
- **和已有方法的差异**：相比基于自注意力的 ViT（如 SwinIR），SAFMN 避开了昂贵的标准自注意力，用更轻量的多尺度池化 + 深度卷积实现动态空间加权；相比传统 CNN（如 IMDN），SAFMN 引入显式的多尺度空间调制机制来捕捉非局部依赖，而非仅靠局部卷积。

## 实验

- **数据集**：训练集 DIV2K + Flickr2K；测试集为五个常用基准 Set5、Set14、B100、Urban100、Manga109。
- **对比方法**：SRCNN, FSRCNN, ESPCN, VDSR, LapSRN, CARN/CARN-M, EDSR-baseline, IMDN, PAN, LAPAR-A, ECBSR-M16C64, SMSR, ShuffleMixer。
- **评价指标**：PSNR 与 SSIM（在 YCbCr 色彩空间的 Y 通道计算）。效率指标：#Params、#FLOPs、#Acts（卷积层输出元素总数）。其中 #FLOPs 与 #Acts 在"将 LR 超分到 1280×720"的设定下用 fvcore 库测量；论文强调 #Params 与 #Acts 关联内存消耗、#FLOPs 关联能耗，并引用近期工作指出 **#Acts 是比参数量和 FLOPs 更好的效率度量**。
- **主实验结果（Table 1，×4 放大，PSNR dB）**：
    - **性能**：SAFMN 在 Set5 32.18 / Set14 28.60 / B100 27.58 / Urban100 25.97 / Manga109 30.43。对比当前最优的 ShuffleMixer（Set5 32.21、Manga109 30.65）和 IMDN（Set5 32.21、Manga109 30.45），SAFMN 各项略低但十分接近；在 Urban100 上差距相对明显（25.97 vs ShuffleMixer 26.08 / PAN 26.11）。
    - **效率（×4）**：SAFMN #Params **240K**、#FLOPs **14G**、#Acts **77M**——参数远低于 CARN 1592K、IMDN 715K、ShuffleMixer 411K；FLOPs（14G）也远低于 IMDN 41G、ShuffleMixer 28G；激活数 77M 约为 IMDN（108M）的 71%、ShuffleMixer（269M）的 29%。
    - **论文文本中的相对量化结论（B100 ×4）**：SAFMN 参数比 CARN 少约 85%、比 IMDN 少 66%、比 ShuffleMixer 少 42%；激活数分别比三者少 60%、29%、71%；而性能与它们相近。
    - **×2 / ×3 结果（Table 1）**：×2 时 SAFMN 228K/52G/299M，Set5 38.00、Manga109 38.71；×3 时 233K/23G/134M，Set5 34.34、Manga109 33.52。三个尺度上 SAFMN 都以远小的模型换取相近的 PSNR/SSIM。
    - **结论**：SAFMN 在模型尺寸（参数量、激活数）上有显著优势，性能与高效 SOTA 方法相当，实现了更好的性能-效率权衡（图 1：Set5 ×2 上 PSNR vs FLOPs vs Params 的帕累托更优）。
- **可解释性分析（图 2、图 5）**：用 LAM（局部归因图）和 DI（diffusion index）对比 SAFMN 与 CARN/EDSR-baseline/PAN——SAFMN 的 DI 值更大（图 2 中标注 10.4295 等），表示其超分某 patch 时利用了更宽范围的输入像素，即更强的非局部信息利用能力。图 5 展示了 SAFM 各尺度分支（scale 1/2/4/8）、聚合特征与最终调制输出的可视化。
- **消融实验**：论文表 3 比较了 SAFM 内算子（如调制方式）的收益，但提取文本未包含表 3 的具体数值。
- **泛化实验**：提取文本未明确说明。
- **未提供的对比**：受页数限制，更多比较结果放在补充材料；提取文本中也未见推理时间 / 峰值内存的实测数值。

## 局限

- **适用场景**：方法专为资源受限场景下的高效 SR 设计，绝对重建性能不与超大模型（RCAN、SwinIR）正面比较；在 Urban100 这类含大量重复结构的数据上，SAFMN 相对 PAN/ShuffleMixer 略逊（×4 时 25.97 vs 26.08/26.11），提示其非局部建模仍有上限。
- **实验充分性**：提取文本仅覆盖前 10 页，表 3（消融）数值、图 6 完整视觉对比及补充材料均未含入，无法据此完整评述各组件贡献。
- **数据集与退化设定**：实验均在 bicubic 下采样的学术基准上进行，未涉及真实世界退化或盲超分，泛化性有待验证。
- **效率度量的缺口**：虽强调 #Acts 与内存的关联，但提取文本中未给出实测推理时间 / 峰值显存对比，"内存更省"主要由 #Params/#Acts 间接论证。
- **复现风险**：论文提供源代码与预训练模型，复现风险较低；但 FFT 频率损失的权重等训练细节（沿用 ShuffleMixer）可能需要仔细对齐。

## 个人评论

1.  **多尺度调制模拟多头注意力**：SAFM 用"通道分组 + 不同尺度自适应最大池化 + 深度卷积 + 上采样回原分辨率 + 聚合生成空间注意力"这一串轻量操作，模拟了 MHSA"并行处理不同子空间信息"的能力，却把复杂度压到深度卷积级别。把"多尺度表征"与"空间自适应动态加权"耦合在一个模块里，对设计轻量注意力/调制算子很有启发。
2.  **非局部/局部解耦的模块化设计**：SAFM 管非局部、CCM 管局部 + 通道混合，二者经 LayerNorm + 残差封装成 FMM，结构干净、易迁移。这种"一个 block 内分工明确"的设计哲学值得借鉴。
3.  **以激活数为主的效率视角**：论文不止看 FLOPs/参数，而把 #Acts 当作更贴近实际显存占用的主指标，并据此论证"内存更省"。这提醒做轻量模型时要关注硬件相关指标，而非仅 FLOPs。
4.  **诚实的权衡叙事**：论文没有声称全面 SOTA，而是明确把卖点定位在"相近性能 + 远小模型"，并用 LAM/DI 给出非局部能力的可视化证据，论证链条比较扎实。

### 使用建议

- **如果快速了解**：读摘要、图 1（性能-复杂度权衡）、图 3（整体框架）、图 4（SAFM 结构）、表 1（量化对比）、第 3.1 节（SAFM 详解）。
- **如果复现**：精读第 3 节（公式 1-4）与第 4.1 节实现细节（8 个 FMM、通道 36、64×64 patch、500k 迭代、余弦退火 1e-3→1e-5、MAE+FFT 损失、RTX 3090），并取用其 GitHub 仓库。
- **如果借鉴创新点**：吃透 SAFM 的多尺度生成-聚合-调制三步与 FMM 的"非局部 + 局部 + 残差"组合，可尝试把 SAFM 作即插即用模块移植到去噪、去模糊等轻量级复原网络。
- **如果写 related work**：放在"高效图像超分辨率"或"轻量级注意力/特征调制模块"下，与 IMDN、ShuffleMixer、PAN、BSRN 并列讨论。

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
本文属于计算机视觉的**高效图像超分辨率（efficient image SR）**方向，目标是在低功耗、内存受限设备上以极小的模型规模实现有竞争力的重建质量。它同时跨"注意力/特征调制算子模块"主题——核心创新 SAFM 是一个借鉴多头自注意力思想、却用多尺度卷积/池化实现的轻量空间调制算子。因此本笔记主题以 SR（图像复原）为主、注意力模块为辅。

## 2. 一句话总结
本文提出高效 SR 网络 SAFMN，其核心是用空间自适应特征调制模块（SAFM）以多尺度独立计算捕捉非局部依赖并做动态空间加权、再配一个卷积通道混合器（CCM）补充局部信息与混合通道，从而在参数/激活数远小于现有方法（约为 IMDN 的 1/3）的同时取得相当的 PSNR/SSIM。

## 3. 背景与问题
- **为什么要做**：深度 SR 模型性能强但普遍庞大（RCAN 15.59M 参数、>400 层），高算力/内存成本阻碍部署；ViT 证明非局部特征交互对高质量重建很重要，但自注意力昂贵，不利于高效 SR。作者欲融合卷积的高效与自注意力的自适应。
- **之前方法的问题**：(1) 减参/降 FLOPs 路线（递归、参数共享、稀疏卷积）常致性能下降，靠加深/加宽补偿反伤推理效率；(2) 加速推理路线（后上采样、量化、结构重参数化）运行快但重建质量差。
- **核心矛盾**：效率（参数、FLOPs、激活数、内存、推理时间多维度）与重建性能的权衡仍有改进空间。

## 4. 核心贡献
1.  高效特征调制机制 **SAFM**：借鉴多头并行独立计算，学习多尺度特征并聚合生成注意力图做空间自适应调制，兼具 CNN 高效与 Transformer 自适应。
2.  紧凑的 **CCM**（基于 FMBConv）：3×3 卷积加倍通道编码局部上下文 + GELU + 1×1 卷积降回原维度，编码局部上下文并混合通道。
3.  将 SAFM + CCM 统一为 **FMM** 并堆叠构成 **SAFMN**，在基准上取得精度与复杂度的良好权衡（×4 时 240K 参数，约为 IMDN 715K 的 1/3）。

## 5. 方法详解
- **整体框架（图 3）**：浅层 3×3 卷积 → 8 个堆叠 FMM → 轻量上采样器（3×3 卷积 + pixel-shuffle），外加全局残差连接学高频。
- **SAFM（公式 1-3）**：
    - 通道分 4 组；X₀ 过 3×3 深度卷积；X₁/X₂/X₃ 分别自适应最大池化到 1/2、1/4、1/8（↓ₚ/2ⁱ），过 3×3 深度卷积后最近邻上采样回原分辨率 → 得不同子空间的多尺度特征（公式 1）。
    - 四分支沿通道拼接，1×1 卷积融合得聚合表示 X̂（公式 2）。
    - 对 X̂ 施 GELU φ(·) 估计注意力图，与原输入 X 逐元素相乘得调制输出 X̄ = φ(X̂)⊙X（公式 3）。
- **CCM**：3×3 卷积（通道加倍，编码局部上下文）→ GELU → 1×1 卷积（降回原维度，混合通道）。
- **FMM（公式 4）**：Y = SAFM(LN(X)) + X；Z = CCM(LN(Y)) + Y。LN = LayerNorm，两处残差稳定训练并保高频。
- **训练**：DIV2K+Flickr2K，bicubic 退化；随机翻转/旋转增强；64 个 64×64 patch；8 个 FMM、通道 36；Adam(β₁=0.9, β₂=0.99)；500k 迭代；lr 1e-3→1e-5 余弦退火；MAE+FFT 频率损失；RTX 3090 + PyTorch。
- **与已有方法差异**：相比 SwinIR 避开标准自注意力；相比 IMDN 引入显式多尺度空间调制捕捉非局部依赖。

## 6. 实验与结果
- **数据集**：训练 DIV2K+Flickr2K；测试 Set5/Set14/B100/Urban100/Manga109。
- **对比方法**：SRCNN, FSRCNN, ESPCN, VDSR, LapSRN, CARN(-M), EDSR-baseline, IMDN, PAN, LAPAR-A, ECBSR, SMSR, ShuffleMixer。
- **指标**：PSNR/SSIM（Y 通道）；效率 #Params/#FLOPs/#Acts，FLOPs 与 Acts 在超分到 1280×720 下用 fvcore 测；论文主张 #Acts 是更好的效率度量（与内存更相关）。
- **关键数字（Table 1，×4）**：
    - SAFMN：#Params **240K** / #FLOPs **14G** / #Acts **77M**；Set5 32.18 / Set14 28.60 / B100 27.58 / Urban100 25.97 / Manga109 30.43。
    - 对照：IMDN 715K/41G/108M（Set5 32.21、Manga109 30.45）；ShuffleMixer 411K/28G/269M（Set5 32.21、Manga109 30.65）；CARN 1592K/91G/194M。
    - 论文文本（B100 ×4）：参数比 CARN/IMDN/ShuffleMixer 少 85%/66%/42%，激活数少 60%/29%/71%，性能相近。
    - ×2：SAFMN 228K/52G/299M，Set5 38.00；×3：233K/23G/134M，Set5 34.34。
- **可解释性（图 2/图 5）**：LAM/DI 显示 SAFMN 的 DI 更大（利用更宽范围像素），非局部信息利用更强；图 5 可视化各尺度分支、聚合与调制输出。
- **消融**：表 3 比较 SAFM 内算子收益，但提取文本未含其数值。
- **未覆盖**：推理时间/峰值显存实测、补充材料、图 6 完整视觉对比均不在提取文本内。

## 7. 这篇论文真正有价值的地方
1.  **用轻量算子模拟多头注意力**：多尺度池化 + 深度卷积 + 聚合 + 空间调制，以深度卷积级别复杂度近似 MHSA 的"多子空间并行 + 动态加权"，是高效注意力替代的好范式。
2.  **非局部/局部解耦的 FMM**：SAFM（非局部）+ CCM（局部+通道混合）+ LayerNorm + 残差，结构清晰、可即插即用。
3.  **以 #Acts 为主的效率观**：把激活数（与显存强相关）置于参数/FLOPs 之上作主指标，提醒轻量化设计要看硬件相关指标。

## 8. 局限与问题
- 绝对性能不与超大模型（RCAN/SwinIR）比，且在 Urban100 上略逊于 PAN/ShuffleMixer，提示非局部建模有上限。
- 提取文本仅前 10 页：表 3 消融数值、图 6 完整视觉对比、补充材料缺失，组件贡献无法据此完整评述。
- 仅 bicubic 退化的学术基准，未涉真实退化/盲 SR，泛化待验证。
- 缺实测推理时间/峰值显存，"省内存"由 #Params/#Acts 间接论证。
- FFT 频率损失权重等细节沿用 ShuffleMixer，复现需对齐。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要、图 1、图 3、图 4、表 1、第 3.1 节。
- **复现**：第 3 节公式 1-4 + 第 4.1 节（8 FMM、通道 36、64×64 patch、500k 迭代、余弦退火 1e-3→1e-5、MAE+FFT 损失、RTX 3090）+ GitHub 仓库。
- **借鉴创新点**：吃透 SAFM 多尺度生成-聚合-调制三步与 FMM 组合方式，可移植到去噪/去模糊等轻量复原网络。
- **写 related work**：归入"高效图像超分辨率"或"轻量级注意力/特征调制模块"，与 IMDN、ShuffleMixer、PAN、BSRN 并列。

## 10. 和其他论文的关系
- 直接对比对象：`[[IMDN]]`、`[[ShuffleMixer]]`、`[[CARN]]`、`[[PAN]]`、`[[EDSR]]`、`[[BSRN]]` 等高效 SR 方法；性能参照的大模型有 `[[RCAN]]`、`[[SwinIR]]`、`[[EDSR]]`、`[[NLSA]]`。
- 上采样器借鉴自 ESPCN 的 pixel-shuffle（`[[ESPCN]]`）；CCM 基于 FMBConv；SAFM 思想源自多头自注意力（`[[Self-Attention]]`、`[[Multi-Head Attention]]`、`[[ViT]]`）。
- 主题上同时关联 `[[E_图像复原_超分_去噪_去雨去雾]]`（SR 复原网络）与 `[[B_注意力算子模块]]`（SAFM 作为轻量调制算子）。

## 11. 关键词
空间自适应特征调制 (SAFM), 卷积通道混合器 (CCM), 特征混合模块 (FMM), SAFMN, 高效图像超分辨率, 轻量级网络, 多尺度特征, 非局部特征依赖, 空间注意力, 激活数 (#Acts), 多头自注意力借鉴

## 12. 可信度说明
本篇精读主要基于 PDF 提取文本（前 10 页，10/10 页提取但原文共约 49764 字符、缓存仅截取前 25000 字符）。该范围已完整覆盖摘要、引言、相关工作、方法（公式 1-4）与表 1（×2/×3/×4 全部主实验数值），所有引用的参数/FLOPs/激活数/PSNR 均直接取自表 1。**主要局限**：表 3（SAFM 内算子消融）的具体数值、图 6 完整视觉对比及补充材料未在提取范围内，故组件级消融结论无法据原文核实；推理时间/峰值显存等实测亦未出现在文本中。除上述标注的缺口外，本笔记声明均可在提取文本找到支撑。

---

> **可信度补充**: PDF 提取质量 = **high** (前 10 页提取完整, ~2504 字符/页, 已覆盖全部主实验表 1); 来源缓存: `.paper-cache/extracts/FMM.txt` (10/10 页, 缓存截取前 25000/49764 字符); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮据提取文本核对修订摘要/方法/实验数值与分类。
<!-- AI_READING_NOTE_END -->
