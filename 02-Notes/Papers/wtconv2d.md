---
title: Wavelet Convolutions for Large Receptive Fields
authors:
  - "Shahaf E. Finder"
  - "Roy Amoyal"
  - "Eran Treister"
  - "Oren Freifeld"
year: 2024
venue: "arXiv"
doi: 
pdf: [[wtconv2d.pdf]]
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
extract_cache: .paper-cache/extracts/wtconv2d.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/27 pages"
---
# Wavelet Convolutions for Large Receptive Fields

## 基本信息
- **PDF**: [[wtconv2d.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Wavelet Convolutions for Large Receptive Fields |
| **作者** | Shahaf E. Finder; Roy Amoyal; Eran Treister; Oren Freifeld（Ben-Gurion University of the Negev, Israel） |
| **发表时间** | 2024（arXiv:2407.05848v2, 2024-07-15；ECCV 2024 工作） |
| **刊物/会议** | arXiv（预印本） |
| **代码** | https://github.com/BGU-CS-VIL/WTConv |
| **DOI** | 未明确 |

## 摘要

> **清理后英文原文**：In recent years, there have been attempts to increase the kernel size of Convolutional Neural Nets (CNNs) to mimic the global receptive field of Vision Transformers' (ViTs) self-attention blocks. That approach, however, quickly hit an upper bound and saturated way before achieving a global receptive field. In this work, we demonstrate that by leveraging the Wavelet Transform (WT), it is, in fact, possible to obtain very large receptive fields without suffering from over-parameterization, e.g., for a k×k receptive field, the number of trainable parameters in the proposed method grows only logarithmically with k. The proposed layer, named WTConv, can be used as a drop-in replacement in existing architectures, results in an effective multi-frequency response, and scales gracefully with the size of the receptive field. We demonstrate the effectiveness of the WTConv layer within ConvNeXt and MobileNetV2 architectures for image classification, as well as backbones for downstream tasks, and show it yields additional properties such as robustness to image corruption and an increased response to shapes over textures. Our code is available at https://github.com/BGU-CS-VIL/WTConv.

> **中文翻译**：近年来，研究者尝试增大卷积神经网络（CNN）的卷积核尺寸，以模拟视觉 Transformer（ViT）自注意力块的全局感受野。然而这种做法很快触及上界，在远未达到全局感受野前性能就已饱和。本文证明：借助小波变换（WT），实际上可以在不发生过参数化的前提下获得非常大的感受野——例如，对于一个 k×k 的感受野，本方法的可训练参数量仅随 k 呈对数级增长。所提出的层（命名为 WTConv）可作为现有架构中的即插即用替换件，能产生有效的多频响应，并随感受野尺寸优雅地扩展。我们在 ConvNeXt 与 MobileNetV2 架构上验证了 WTConv 在图像分类中的有效性，并将其作为下游任务的骨干网络，还展示了它带来的额外性质，如对图像损坏的鲁棒性、以及相对纹理更偏向形状的响应。代码已开源。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：过去十年 CNN 主导了大量视觉任务，但 ViT 出现后凭借多头自注意力带来的**全局特征混合**能力，在多项任务上对 CNN 形成压力——卷积按构造只能做局部混合。为弥补差距，Liu et al. [38]（ConvNeXt）重构 ResNet 并增大卷积核，但经验上核尺寸增大到 **7×7 即饱和**，再增大反而损害性能。
- **之前方法的问题**：
    1. **朴素增大卷积核**（>7×7）会损害卷积的局部性、性能下降（Liu et al. [38]）。
    2. **改进的大核方法**：RepLKNet（Ding et al. [11]）用小核并联大核求和，成功训到 31×31；SLaK（Liu et al. [36]）把 51×51 分解为 51×5 与 5×51 并引入稀疏性扩宽通道，训到 51×51。但参数随核尺寸**平方增长**，最终过参数化、在达到全局感受野之前就饱和。
    3. **频域（傅里叶）方法**（如 GFNet [47]）可获全局感受野，但傅里叶变换把输入完全转到频域，**丢失相邻像素的局部交互**；且权重数依赖固定输入尺寸，难用于下游任务。
- **一个关键观察**：Ding et al. [11] 发现更大核会让 CNN 更**形状偏好（shape-biased）**，即更善于捕捉图像低频。这与卷积层通常响应高频的常识相反，而注意力头则被发现更偏向低频。这启发本文：能否用信号处理工具有效扩大感受野、同时引导 CNN 更好响应低频？
- **选小波而非傅里叶的动机**：WT 在分解到不同频带时**保留部分空间分辨率**，使得在小波域内做空间操作（卷积）仍有意义；傅里叶变换则做不到这点。
- **核心矛盾**：如何在不过参数化的前提下，有效获得非常大（乃至全局）的感受野，并改善 CNN 对低频成分（形状）的响应。
## 关键贡献

论文在引言中明确列出四条核心贡献：

1.  **提出 WTConv 层**：利用小波变换有效扩大卷积感受野的新型层。
2.  **即插即用**：WTConv 被设计为**深度可分离（depth-wise）卷积的直接替换件**，可不加修改地用于任意 CNN 架构。
3.  **广泛实证**：在多个关键视觉任务上证明 WTConv 提升 CNN 结果。
4.  **额外性质分析**：分析 WTConv 对 CNN 的可扩展性（scalability）、鲁棒性（robustness）、形状偏好（shape-bias）与有效感受野（ERF）的贡献。
5.  **参数效率特性**（贡献的量化支撑）：对 k×k 感受野，可训练参数仅随 k 对数级增长（与平方增长的大核方法相反）；从层级角度看，ℓ 级级联下参数随级数**线性**增长（ℓ·4·c·k²），感受野随级数**指数**增长（2ℓ·k）。
## 方法

- **整体框架**：将输入特征图经小波变换（WT）分解为多频子带，对每个子带施加小卷积核，再经逆小波变换（IWT）合成。该过程可级联（cascade）多层，对低频分量反复分解以覆盖更大感受野。核心公式：`Y = IWT(Conv(W, WT(X)))`（式 5）。
- **输入输出**：输入特征图张量 X；输出 Y。其中权重张量 W 是 k×k 的深度卷积核，但其输入通道数是 X 的 **4 倍**（因 WT 把每通道分成 LL/LH/HL/HH 四个子带）。
- **关键模块**：
    1.  **小波变换（WT，§3.1）**：采用 **Haar 小波**（高效、直观，但论文强调方法不限于此，可用其他小波基，代价是计算量增加）。单维一级 Haar WT = 用核 `[1,1]/√2`、`[1,−1]/√2` 做深度卷积后再 2 倍下采样。2D 情形组合两维，等价于一个**步长 2 的深度卷积**，用四个滤波器 f_LL（低通）、f_LH、f_HL、f_HH（高通），把输入分解为低频 X_LL 与水平/垂直/对角三个高频分量 X_LH/X_HL/X_HH（式 1-2），每个子带空间分辨率减半。
    2.  **小波域卷积（§3.2）**：对分解后的各频带施加固定小核（如 3×3 或 5×5）深度卷积。这既把不同频率分量的卷积分离开，又让小核在原始输入上覆盖更大区域。
    3.  **逆小波变换（IWT）**：因式 1 的核构成正交基，IWT 即**转置卷积**（式 3），可无损还原。
- **级联机制与求和（§3.2，式 6-8）**：对当前层的低频分量 X^(i−1)_LL 再次 WT 得到下一级的 LL 与高频 X^(i)_H（式 6）；对每级 (X^(i)_LL, X^(i)_H) 施加该级卷积权重 W^(i) 得 (Y^(i)_LL, Y^(i)_H)（式 7）。由于 WT/IWT 是线性算子，满足 IWT(X+Y)=IWT(X)+IWT(Y)，于是用 `Z^(i)=IWT(Y^(i)_LL + Z^(i+1), Y^(i)_H)` 自最深级向上逐级合成并累加（式 8），相当于把不同级（不同感受野尺度）的卷积输出求和——这一点与 RepLK [11] 把不同尺寸卷积输出求和的思想一致。
- **归一化的差异**：与 RepLK [11] 不同，本文**不能**对各 Y^(i)_LL、Y^(i)_H 单独归一化（因为分别归一化不对应原域中的归一化）；作者发现只需做**逐通道缩放（channel-wise scaling）**来加权各频率分量的贡献即可。
- **数学机制（感受野放大，Fig.2）**：在第二级小波域的低频带 X^(2)_LL 上做一个 3×3（9 参数）卷积，因 X^(2)_LL 经两次 2 倍下采样，其在原始输入 X 上的等效感受野为 **12×12**，且专门响应该区域的低频。更一般地，ℓ 级、核 k 时单层感受野约 2ℓ·k。
- **训练与推理**：WTConv 直接替换原网络的深度卷积层，训练遵循原网络（如 ConvNeXt）配置、无需额外调参；完整算法见附录 A，训练细节见附录 B。
- **与已有方法的差异**：
    1.  vs. 大核卷积（RepLK [11] / SLaK [36]）：本文参数随感受野**对数/级数线性**增长而非平方，且求和的是输入**不同频率分量**而非不同尺寸核的并联输出。
    2.  vs. 傅里叶频域方法（GFNet [47]）：WT 保留空间局部信息，使频域卷积仍是有意义的局部操作；傅里叶完全全局化、丢失局部交互，且依赖固定输入尺寸。
    3.  vs. 同类小波网络（[1,15,35]）：那些是高度定制的架构（改造 U-Net / DenseNet），无法无缝嵌入其他 CNN；本文是更轻、更易用的**线性即插即用层**，可用于任何使用深度卷积的网络、不限于单一任务。
- **论文类型特化（注意力/算子类模块）**：
    - **作用维度**：在**多尺度频域**做特征混合——分解到不同频带（对应不同空间尺度），逐带独立卷积后合成。
    - **可插入网络**：深度可分离卷积的直接替换件，论文在 ConvNeXt 与 MobileNetV2 上验证。
    - **计算量 vs 效果（§3.4）**：以 512×512 单通道输入为例，7×7 深度卷积 = 12.8M FLOPs，31×31 = 252M FLOPs；而 3 级、5×5 核的 WTConv（感受野 40×40 = (5·2³)×(5·2³)）卷积部分约 15.1M FLOPs，加上 WT+IWT 的 2.8M，合计 **17.9M FLOPs**——相比同等感受野的标准深度卷积仍是大幅节省。
## 实验

- **使用的数据集**：
    - **图像分类**：ImageNet-1K（§4.1）
    - **语义分割**：ADE20K（§4.2，框架 UperNet，工具 MMSegmentation）
    - **目标检测/实例分割**：COCO（§4.3，框架 Cascade Mask R-CNN，工具 MMDetection）
- **骨干设置**：以 ConvNeXt 为基，把 7×7 深度卷积替换为 WTConv；四个 stage 的 WT 级数设为 **[5,4,3,2]**、核 5×5，使 224×224 输入在每个 stage 都达到全局感受野；分类用 120 与 300 epoch 两套训练计划。
- **对比方法**：ConvNeXt（基准）、Swin Transformer、RepLKNet、SLaK、VAN、GFNet。
- **评价指标**：分类用 Top-1 准确率；分割用 mIoU（单尺度测试）；检测用 AP^box 与 AP^mask。
- **主实验结果**：
    - **ImageNet-1K（120 epochs, Table 1）**：在统一 ConvNeXt-T 架构下报告**深度卷积部分**的参数量。WTConv 感受野 **[160,80,40,20]**、D-W 参数 **2.04M**、Top-1 **81.7**，优于 RepLK（3.84M/81.5）、SLaK（2.52M/81.5）、GFNet（4.29M/81.2，FFT 全局）、VAN（0.38M/81.1）、ConvNeXt-T（0.32M/81.0）。WTConv 是 top 方法中最省参的，且以不到 GFNet 一半的参数达到全局感受野。
    - **ImageNet-1K（300 epochs, Table 2）**：WTConvNeXt-T/S/B = 30M/4.5G/**82.5**、54M/8.8G/**83.6**、93M/15.5G/**84.1**，均高于同规模 Swin（81.3/83.0/83.5）与 ConvNeXt（82.1/83.1/83.8）。论文强调效率：ConvNeXt-S→B 加 39M 参数 +6.7 GFLOPs 仅换 0.7% 提升，而升到 WTConvNeXt-S 只加 4M 参数 +0.1 GFLOPs 就换 0.5% 提升。
    - **ADE20K 分割（Table 3）**：WTConvNeXt-T 作 UperNet 骨干（62M/939G）取得 **45.4**（120e 预训+80K）、**46.6**（300e 预训+160K）mIoU，对应 ConvNeXt-T 为 44.6/46.0；整体 mIoU 提升 **0.3–0.6%**（FLOPs 基于 2048×512 输入）。
    - **COCO 检测（Table 4，Cascade Mask R-CNN，FLOPs 基于 1280×800）**：WTConvNeXt-T 在 120e+1x 下 AP^box/AP^mask = **47.9/41.5**（ConvNeXt-T 47.3/41.1）；在 300e+3x 下 = **51.0/44.4**（ConvNeXt-T 与 Swin-T 均 50.4/43.7），AP^box 提升 0.6。WTConvNeXt-S 在 300e+3x 下 = 52.6/45.6。
- **消融实验**：提取缓存（前 12 页）未含表 8；据原文后续页（p.13-14，提取缓存未覆盖，待核）有针对 WTConvNeXt-T 的消融，比较不同 WT 级数与核尺寸组合，Table 8 显示相应结果。
- **额外性质分析（§4.4）**：摘要与 §3.3 声称 WTConv 提升可扩展性、对损坏/分布偏移的鲁棒性、形状偏好，并通过 ERF 可视化（Fig.1）佐证——Fig.1 显示 WTConv 用更少可训练参数获得比 RepLK、SLaK 更大的有效感受野。具体定量分析在提取缓存覆盖的前 12 页未展开。
- **效率信息**：
    - **参数量**：WTConvNeXt-T/S/B = 30M/54M/93M（对应 ConvNeXt 29M/50M/89M，分别增约 1M/4M/4M）。
    - **FLOPs**：4.5G/8.8G/15.5G（对应 ConvNeXt 4.5G/8.7G/15.4G，几乎持平）。
    - **感受野**：四 stage 实现 [160,80,40,20] 的超大感受野，远超原 7×7。
## 局限

- **运行时开销**：据原文后续页（p.14 §5 Limitations，提取缓存未覆盖，待核）作者承认——虽然 WTConv 的 FLOPs 不高，但其**实际运行时间**（wall-clock running time）偏高，这是已知局限（提取缓存前 12 页未含此节，但 §3.4 已暗示需额外计入 WT/IWT 的实现成本）。
- **小波基依赖**：高效性建立在 Haar 小波之上；论文明确指出可用其他小波基，但**会带来计算成本增加**。
- **架构范围**：方法面向使用深度可分离卷积的 CNN；对本身具全局感受野的纯 Transformer 是否有效未涉及。
- **任务范围**：实验集中于分类/分割/检测三类，未涉及视频、3D、生成等。
- **复现依赖**：算法细节在附录 A、训练超参在附录 B，需结合开源代码（已提供 GitHub）。本节关于运行时与小波基的判断部分依据原文后续页线索，提取缓存未直接覆盖。
## 个人评论

这篇论文最值得学习的，是把**经典信号处理工具（小波变换）与现代 CNN 优雅嫁接**的思路：它没造复杂新模块，而是抓住一个本质矛盾——感受野与参数量的平方耦合——用 WT 的"分解-小核卷积-合成"把这个耦合从平方降到对数/级数线性。三处设计尤其干净：(1) 用步长 2 的深度卷积实现 Haar WT、用转置卷积实现 IWT，使整层是纯卷积、可微、可高效落地；(2) 利用 WT 线性性把多级输出直接求和（式 8），结构上呼应 RepLK 的多尺度求和，却换成了"多频率"求和；(3) 放弃逐子带归一化、改用逐通道缩放这一务实选择，暴露了"频域操作不能简单照搬空间域直觉"的工程细节。

更深一层，它把"卷积偏高频、注意力偏低频"这条经验观察转化为**结构性归纳偏置的设计杠杆**：反复分解低频 = 主动给低频"加权重"，从而把 shape-bias 做成架构性质而非数据依赖。这对做即插即用模块的研究者有两点启发：其一，频域（尤其多尺度频域）是与空间/通道注意力并列的第三类特征混合维度，值得继续挖（换更复杂小波基、可学习小波、频带级注意力都是自然延伸）；其二，论文坦承的"FLOPs 低但 wall-clock 慢"提醒——评估即插即用算子不能只看理论 FLOPs，访存与算子实现效率往往是落地瓶颈。对改模型而言，这是一个极轻量、可直接替换 7×7 深度卷积的增强件，几乎零额外参数/FLOPs 就能换取分类/分割/检测的一致小幅提升。

### 使用建议

- **快速了解**：读**摘要**、引言最后两段、以及 Table 1-4。能快速抓住核心思想（小核大感受野）、贡献与效果。
- **复现**：精读 §3（式 1-8 与 Fig.2/Fig.3），并对照**附录 A（算法）+ 附录 B（训练细节）+ 开源代码**；注意 WT/IWT 的高效实现与逐通道缩放。
- **借鉴创新点**：
    1.  **小核大感受野**的实现范式：多尺度 WT 分解 + 局部卷积 + 线性合成求和。
    2.  **即插即用评估范式**：在强基准（ConvNeXt）上替换关键算子，跨分类/分割/检测多任务统一验证、不调参。
    3.  **归纳偏置（shape-bias / ERF）的分析视角**，可移植到自己工作的分析章节。
- **写 Related Work** 可归入：大核卷积与感受野扩展（与 RepLK/SLaK 并列）、频域/信号处理在 CNN 中的应用（与 FFT 类 GFNet 并列）、轻量高效混合机制。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中 CNN 算子设计方向，提出一种可替换深度可分离卷积的新算子 WTConv（Wavelet Transform Convolution）。它瞄准 CNN 的本质短板——卷积只能局部混合特征、靠增大核扩感受野又会过参数化——用小波变换把输入分解到多尺度频带后再做小核卷积，以远低于大核方法的参数代价获得超大（乃至全局）感受野，并刻意增强模型对低频（形状）的响应。归入"注意力/算子模块（B）"主题，因为它本质是一种与自注意力目标一致（扩大有效混合范围）、可即插即用的**特征混合算子**，是空间/通道注意力之外的"多频率混合"维度。

## 2. 一句话总结
WTConv 通过级联小波变换把特征分解到多尺度频带、对各频带施加固定小核卷积再逆变换合成，使参数量随感受野仅对数/级数线性增长、而感受野随级数指数增长，从而以近乎零额外开销作为深度卷积的即插即用替换件，提升 CNN 在分类/分割/检测上的表现并增强其形状偏好。

## 3. 背景与问题
- **为什么要做**：ViT 的多头自注意力带来全局特征混合，对只能局部混合的 CNN 形成压力。ConvNeXt（Liu et al. [38]）增大卷积核以追赶 Swin，但经验上 7×7 即饱和、再大反而变差。
- **之前方法的问题**：① 朴素增大核（>7×7）损害局部性、性能下降；② RepLK [11]（并联小核+大核求和，训到 31×31）、SLaK [36]（51×51 分解为 51×5+5×51 并稀疏扩宽，训到 51×51）虽有效但参数随核**平方增长**，达到全局前先过参数化饱和；③ 傅里叶频域法（GFNet [47]）能全局但丢失局部交互、依赖固定输入尺寸。
- **核心矛盾**：在不过参数化前提下有效获得超大/全局感受野，并改善对低频（形状）的响应。
- **关键洞见**：大核会让 CNN 更形状偏好（[11]）；卷积偏高频、注意力偏低频；WT（不同于傅里叶）在分频时**保留空间分辨率**，使频域卷积仍有意义——这三点共同支撑了"用小波扩感受野"的选择。

## 4. 核心贡献
1. **WTConv 层**：用小波变换有效扩大卷积感受野。
2. **即插即用**：作为深度可分离卷积的直接替换件，无需改动即可用于任意 CNN（验证于 ConvNeXt、MobileNetV2）。
3. **参数效率**：k×k 感受野下参数随 k **对数增长**；ℓ 级级联下参数随级数线性（ℓ·4·c·k²）、感受野随级数指数（2ℓ·k）。
4. **广泛实证 + 性质分析**：在分类/分割/检测上一致提升，并分析对可扩展性、鲁棒性、形状偏好、ERF 的贡献。

## 5. 方法详解
- **核心式（式 5）**：`Y = IWT(Conv(W, WT(X)))`。W 是 k×k 深度核，输入通道为 X 的 4 倍（WT 把每通道分成 LL/LH/HL/HH）。
- **WT 即卷积（§3.1）**：用 Haar 小波。2D 一级 Haar WT = 步长 2 的深度卷积，四滤波器 f_LL（低通）、f_LH/f_HL/f_HH（高通）（式 1）；输出四个半分辨率子带（式 2）。因构成正交基，IWT = 转置卷积（式 3）。级联即对低频 X^(i−1)_LL 反复 WT（式 4）。
- **级联与合成（式 6-8）**：每级对 (X^(i)_LL, X^(i)_H) 施加 W^(i) 卷积；利用 WT 线性性，自最深级向上逐级求和合成 `Z^(i)=IWT(Y^(i)_LL+Z^(i+1), Y^(i)_H)`（式 8）——等价于把不同频率/尺度的卷积输出相加（呼应 [11] 的多尺度求和）。
- **归一化（务实细节）**：不能逐子带单独归一化（不对应原域归一化），改用**逐通道缩放**加权各频率分量。
- **感受野直觉（Fig.2）**：在第二级低频 X^(2)_LL 上的 3×3（9 参数）卷积，因两次下采样，在原图上等效 **12×12** 感受野且响应低频。
- **计算量（§3.4）**：512×512 单通道下，7×7=12.8M、31×31=252M FLOPs；3 级 5×5 WTConv（感受野 40×40）卷积部分 15.1M、加 WT+IWT 2.8M 合计 **17.9M FLOPs**，相比同感受野大核仍大幅省。
- **与他法差异**：vs RepLK/SLaK（参数对数/线性 vs 平方，且求和多频分量而非多尺寸核）；vs GFNet（保留局部信息、不依赖输入尺寸）；vs 定制小波网络 [1,15,35]（轻量线性、可嵌任意 CNN）。

## 6. 实验与结果
- **数据集/框架**：ImageNet-1K（分类）；ADE20K + UperNet（分割，MMSegmentation）；COCO + Cascade Mask R-CNN（检测，MMDetection）。
- **设置**：ConvNeXt 中把 7×7 深度卷积换为 WTConv，四 stage 级数 [5,4,3,2]、核 5×5；分类 120/300 epoch 两套计划。
- **ImageNet-1K（Table 1, 120e，报告 D-W 参数）**：WTConv 感受野 [160,80,40,20]、2.04M、**Top-1 81.7**，胜 RepLK（3.84M/81.5）、SLaK（2.52M/81.5）、GFNet（4.29M/81.2）、VAN（0.38M/81.1）、ConvNeXt-T（0.32M/81.0），最省参且全局感受野。
- **ImageNet-1K（Table 2, 300e）**：WTConvNeXt-T/S/B = 30M/4.5G/**82.5**、54M/8.8G/**83.6**、93M/15.5G/**84.1**，全面超 Swin（81.3/83.0/83.5）与 ConvNeXt（82.1/83.1/83.8）；性价比远高（S 仅 +4M/+0.1G 换 0.5%）。
- **ADE20K（Table 3）**：WTConvNeXt-T（62M/939G）mIoU **45.4**（120e+80K）/ **46.6**（300e+160K），对 ConvNeXt-T 44.6/46.0，整体 +0.3–0.6%。
- **COCO（Table 4）**：WTConvNeXt-T 120e+1x AP^box/AP^mask **47.9/41.5**（ConvNeXt-T 47.3/41.1）；300e+3x **51.0/44.4**（ConvNeXt-T/Swin-T 均 50.4/43.7）。
- **ERF（Fig.1）**：WTConv 用更少参数取得比 RepLK、SLaK 更大的有效感受野。
- **消融（Table 8）**：据原文后续页（p.13-14，提取缓存未覆盖，待核）对 WT 级数与核尺寸组合做消融，原文称增大级数等带来相应变化（具体数值未在提取缓存内）。

## 7. 这篇论文真正有价值的地方
价值在"老工具新用"的范式与三个可迁移的设计点：① 把感受野-参数的平方耦合降到对数/线性，用纯卷积（WT=步长2深度卷积、IWT=转置卷积）实现，落地友好；② 用 WT 线性性把多级输出直接求和（式 8），把 RepLK 的"多尺寸核求和"换成"多频率求和"；③ 把"卷积偏高频"这条经验转成结构杠杆——反复分解低频 = 主动强化低频响应，从而把 shape-bias 做成架构性质。它证明**多尺度频域**是与空间/通道注意力并列的第三类特征混合维度。

## 8. 局限与问题
- **运行时**：据原文后续页（p.14 §5，提取缓存未覆盖，待核）FLOPs 虽低但 wall-clock 运行时间偏高。
- **小波基依赖**：高效性绑定 Haar；换更复杂小波基会增计算量（论文明言）。
- **架构/任务范围**：面向用深度卷积的 CNN，未涉纯 Transformer；任务限分类/分割/检测，未及视频/3D/生成。
- **复现**：算法在附录 A、训练超参在附录 B，需配合开源代码；本笔记关于运行时与消融的判断部分依据后续页线索，提取缓存（前 12 页）未直接覆盖。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言末两段 + Table 1-4。
- **复现**：精读 §3（式 1-8、Fig.2/3）+ 附录 A/B + 开源代码，注意 WT/IWT 高效实现与逐通道缩放。
- **借鉴**：小核大感受野范式；强基准上替换关键算子的跨任务评估范式；ERF / shape-bias 分析视角。
- **写 Related Work**：归入"大核卷积与感受野扩展""频域信号处理在 CNN 中的应用""轻量高效混合机制"。

## 10. 和其他论文的关系
本文在主题"B_注意力算子模块"下是一个**多频率特征混合算子**，与该主题中其他扩大感受野/高效混合的工作互补。论文正文显式对照的近邻工作有：RepLKNet（Ding et al. [11]，大核求和，本文借鉴其多尺度求和思想）、SLaK（Liu et al. [36]，超大核分解+稀疏）、GFNet（[47]，FFT 频域全局混合，本文对照的频域方法）、ConvNeXt（[38]，基准骨干）、Swin（[37]，Transformer 对比）、以及小波类网络 [1,15,35]（定制 U-Net/DenseNet）。当前知识库未确认这些论文已有对应笔记，故暂不建立可能落空的双链。

## 11. 关键词
Wavelet Transform (WT), Haar Wavelet, Receptive Field, Effective Receptive Field (ERF), Convolutional Neural Networks (CNN), Depth-wise / Separable Convolution, Multi-frequency Representation, Cascade Decomposition, Shape Bias, Drop-in Replacement, ConvNeXt, MobileNetV2

## 12. 可信度说明
本精读主要基于 PDF 提取文本（缓存覆盖前 12 页，即论文 p.1-12，含摘要、引言、相关工作、方法 §3 全部与实验 Table 1-4），其中所有方法描述、公式（式 1-11）、感受野/FLOPs/参数/准确率数字均严格抄录自该文本。涉及 §5 Limitations、§4.4 详细性质分析、Table 8 消融、附录的内容，提取缓存未直接覆盖，已据"全文补读记录"中的后续页线索标注为"据原文后续页，提取缓存未覆盖，待核"。摘要已修复 PDF 直提的空格/连字符断裂并剔除图轴杂入数字。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/wtconv2d.txt` (覆盖 12/27 页, max_chars=25000 截断于 §4.3; 原 AI 主体 12/27 + 全文补读线索 13-27); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮据提取文本重核摘要/方法/实验数字, 修正一句话总结的"对数/指数"措辞、补全归一化与逐通道缩放细节、订正计算量口径(15.1M 卷积 + 2.8M WT/IWT = 17.9M 合计)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-27; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-27。
- **提取情况**: 缺失页 15 页, 其中 15 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Wavelet Convolutions for Large Receptive Fields 13
- p.13: ConvNeXt-T
- p.13: ConvNeXt-S
- p.13: ConvNeXt-B
- p.13: WTConvNeXt-T
- p.13: WTConvNeXt-S
- p.13: WTConvNeXt-B
- p.14: 5 Limitations
- p.14: Although the WTConv layer does not require many FLOPs, its running time
- p.14: 6 Conclusion
- p.14: In this work, we utilize wavelet transforms to introduce WTConv, a drop-in re-
- p.15: Wavelet Convolutions for Large Receptive Fields 15

### 缺失页关键摘录

- p.13: as the size of the receptive field induced by the layer. The empirical evaluation
- p.13: the last layer. The result is visualized in Fig. 1, where high-contribution pixels
- p.13: Ablation Study. We conduct an ablation study to see how different configu-
- p.13: rations of the WTConv layer impact the final result. We train WTConvNeXt-T
- p.13: tions. First, we experiment with different combinations of WT levels and ker-
- p.14: Table 8 shows the results of all the described configurations. Here, increas-
- p.14: Table 8: Ablation study with WTConvNeXt-T. Comparing different configurations of
- p.14: Although the WTConv layer does not require many FLOPs, its running time
- p.15: 6. Contributors, M.: MMDetection: Openmmlab detection toolbox and benchmark.
- p.15: and benchmark. https://github.com/open-mmlab/mmsegmentation (2020)
- p.19: mantic understanding of scenes through the ade20k dataset. International Journal
- p.21: warmup of 50 batches. Table 9 presents the throughput, measured in images per
<!-- AI_READING_NOTE_END -->
