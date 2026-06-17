---
title: "MixDehazeNet : Mix Structure Block For Image Dehazing Network"
authors:
  - "LiPing Lu"
  - "Qian Xiong"
  - "DuanFeng Chu"
  - "BingRong Xu"
year: 2023
venue: "arXiv"
doi: 
pdf: [[MSPLCK&EPA.pdf]]
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
extract_cache: .paper-cache/extracts/MSPLCK&EPA.txt
---

# MixDehazeNet : Mix Structure Block For Image Dehazing Network

## 基本信息
- **PDF**: [[MSPLCK&EPA.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`, `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | MixDehazeNet : Mix Structure Block For Image Dehazing Network |
| **作者** | LiPing Lu*; Qian Xiong*（共同一作）; DuanFeng Chu; BingRong Xu†（通讯）—— 武汉理工大学 |
| **发表时间** | 2023（arXiv:2305.17654v1, 2023-05-28） |
| **刊物/会议** | arXiv 预印本 |
| **DOI** | 未明确（arXiv:2305.17654） |
| **代码** | https://github.com/AmeryXiong/MixDehazeNet |

## 摘要

清理后的英文原摘要（据 PDF 提取文本整理，修复空格/连字符断裂，剔除杂入的图轴数字）：

> Image dehazing is a typical task in the low-level vision field. Previous studies verified the effectiveness of the large convolutional kernel and attention mechanism in dehazing. However, there are two drawbacks: the multi-scale properties of an image are readily ignored when a large convolutional kernel is introduced, and the standard series connection of an attention module does not sufficiently consider an uneven hazy distribution. In this paper, we propose a novel framework named Mix Structure Image Dehazing Network (MixDehazeNet), which solves two issues mentioned above. Specifically, it mainly consists of two parts: the multi-scale parallel large convolution kernel module and the enhanced parallel attention module. Compared with a single large kernel, parallel large kernels with multi-scale are more capable of taking partial texture into account during the dehazing phase. In addition, an enhanced parallel attention module is developed, in which parallel connections of attention perform better at dehazing uneven hazy distribution. Extensive experiments on three benchmarks demonstrate the effectiveness of our proposed methods. For example, compared with the previous state-of-the-art methods, MixDehazeNet achieves a significant improvement (42.62dB PSNR) on the SOTS indoor dataset. The code is released in https://github.com/AmeryXiong/MixDehazeNet.

中文翻译：

> 图像去雾是底层视觉领域的一项典型任务。已有研究已验证大卷积核与注意力机制在去雾中的有效性。然而存在两个缺陷：引入大卷积核时图像的多尺度特性容易被忽略；注意力模块的标准串联连接方式不足以应对不均匀的雾霾分布。本文提出一个名为 Mix Structure Image Dehazing Network（MixDehazeNet）的新框架，解决上述两个问题。具体而言，它主要由两部分构成：多尺度并行大卷积核模块（MSPLCK）与增强并行注意力模块（EPA）。与单一大核相比，具有多尺度的并行大核更能在去雾阶段兼顾局部纹理。此外，所设计的增强并行注意力模块以注意力的并行连接方式在处理不均匀雾霾分布上表现更好。在三个基准上的大量实验证明了所提方法的有效性。例如，与此前的最先进方法相比，MixDehazeNet 在 SOTS 室内数据集上取得了显著提升（42.62 dB PSNR）。代码已开源。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：图像去雾是底层视觉任务，雾霾会降低人类识别和深度模型的表现，并隐式影响目标检测、重识别（re-recognition）、语义分割等下游高级视觉任务的性能。去雾作为预处理的第一步，对学术界和工业界都很重要。
- **物理基础**：基于大气散射模型 `I(x) = J(x)·t(x) + A·(1 − t(x))`，其中 `A` 是全局大气光，`t(x)` 是透射图，且 `t(x) = e^{-β·d(x)}`（β 为散射系数、d(x) 为场景深度）。早期方法依赖先验估计 `A` 与 `t(x)`，先验不满足时复原会失真。
- **之前方法有什么问题**（论文明确点出两条局限）：
    1.  **多尺度被忽略**：CNN 与 Transformer 方法都能借大有效感受野提升性能，但去雾过程中图像的多尺度特性常被忽略。每张图的雾霾浓度分布不均，不同尺寸的卷积核能有效捕捉不同尺度的雾霾区域。
    2.  **注意力串联不当**：以往去雾网络（FFA-Net、AECR-Net、GCANet 等）的注意力通常**分别单独设计**像素注意力与通道注意力。作者注意到：通道注意力更适合编码全局共享变量 `A`，像素注意力更适合编码位置相关的局部变量 `t(x)`。串联使用时，后一种注意力是在已被前者修改的特征上提取信息，无法从**原始特征**并行提取两类信息，不利于处理不均匀雾霾分布。
- **核心矛盾**：如何在一个去雾网络中**同时且有效地**利用大卷积核的全局/长距离建模能力与多尺度特性，并设计一种能从原始特征**并行**提取全局共享信息与局部依赖信息的注意力机制。
## 关键贡献

论文自述贡献为三条，本笔记按内容展开为五点：

1.  设计了**多尺度并行大卷积核模块（MSPLCK）**，兼具大感受野与多尺度特性。模块内并行三个不同核尺寸的深度膨胀卷积（等效核 7/13/19），大/中核负责捕获大面积雾霾区域（类自注意力的长距离建模），小核负责恢复纹理细节，从而能同时恢复纹理并捕捉大片雾区。
2.  设计了**增强并行注意力模块（EPA）**，**并行**使用简单像素注意力（SPA）、通道注意力（CA）、像素注意力（PA）三种机制，能从原始特征并行地提取共享全局信息（编码 `A`）与位置相关局部信息（编码 `t(x)`），更适合不均匀雾霾分布。三个分支结果经 MLP 融合。
3.  提出**Mix 结构块（Mix Structure Block）**——一个 Transformer 风格的块，用 MSPLCK 替代多头自注意力、用 EPA 替代前馈网络（FFN），构成网络基本单元。
4.  将**对比学习损失**融入训练（受 AECR-Net 启发），并改用预训练 **ResNet-152**（而非 AECR-Net 用的 VGG19）作对比学习骨干，作者发现其对本模型更有效。
5.  在 RESIDE-IN/OUT 与 RESIDE-6K 三个基准上达到当时 SOTA；MixDehazeNet-L 是**首个在 SOTS 室内数据集上 PSNR 超过 42 dB** 的模型。
## 方法

### 整体框架
MixDehazeNet 采用一个**5 阶段 U-Net** 作为骨干，每个阶段嵌入 **Mix 结构块**。下采样用 stride=2 的 3×3 卷积，上采样用点卷积 + PixelShuffle。跳跃连接通过 **SK Fusion**（借自 Dehazeformer）融合主分支与跳跃分支；网络末端用 **soft reconstruction**（软重建，亦借自 Dehazeformer）代替全局残差连接，因为软重建提供比全局残差更强的去雾约束。

### 输入与输出
- **输入**：有雾图像 `I`。
- **输出**：去雾图像 `Ĵ`（`J` 为对应清晰图像，作为真值）。

### 关键模块
1.  **多尺度并行大卷积核模块（MSPLCK）**（论文 3.1 节）
    - **功能**：替代 Transformer 的多头自注意力，提取多尺度特征。
    - **结构（公式 2–3）**：
        - 先对输入 `x` 做 BatchNorm 归一化（加速收敛、提升泛化、抑制过拟合）。
        - `x1 = PWConv(x̂)`（点卷积）；`x2 = Conv(x1)`（核尺寸 5 的卷积）。
        - 并行三个**深度膨胀卷积**，膨胀率均为 3：
            - `DWDConv19`：7×7 深度膨胀卷积，等效核 19×19。
            - `DWDConv13`：5×5 深度膨胀卷积，等效核 13×13。
            - `DWDConv7`：3×3 深度膨胀卷积，等效核 7×7。
        - 沿通道维 Concat 三者，`x3` 通道数变为 `x` 的三倍。
        - 经 MLP（PWConv-GELU-PWConv）把通道降回与 `x` 同维，再与恒等捷径相加：`y = x + PWConv(GELU(PWConv(x3)))`。
    - **设计思想**：大/中膨胀核捕获大面积雾区（类全局特征），小膨胀核恢复纹理细节（局部特征）；并行 Concat 保留多尺度信息，MLP 既融合三类特征又拟合去雾特征。

2.  **增强并行注意力模块（EPA）**（论文 3.2 节）
    - **功能**：替代 Transformer 的前馈网络，通过并行注意力处理不均匀雾霾分布。
    - **结构**：先对 `x` 做 BatchNorm 得 `x̂`，三个**并行**注意力分支处理 `x̂`：
        - **简单像素注意力（SPA，公式 4）**：双分支——特征分支 `PFs = Conv(PWConv(x̂))`（Conv 核尺寸 3），门控分支 `PAs = Sigmoid(PWConv(x̂))`，逐元素相乘 `Fs = PFs ⊗ PAs`，提取**位置依赖**特征。
        - **像素注意力（PA，公式 5）**：`PAp = Sigmoid(PWConv(GELU(PWConv(x̂))))`，作为全局像素门控信号作用于 `x̂`：`Fp = x̂ ⊗ PAp`。
        - **通道注意力（CA，公式 6）**：先全局平均池化 GAP，再 `CAc = Sigmoid(PWConv(GELU(PWConv(GAP(x̂)))))`，作为通道门控信号：`Fc = x̂ ⊗ CAc`，提取**全局共享**信息。
    - **融合（公式 7）**：`F = Concat(Fs, Fc, Fp)`，再经 MLP（PWConv-GELU-PWConv）把通道降回与输入同维，最后与恒等捷径 `x̂` 残差相加。
    - **设计思想**：`A` 为全局共享变量、`t(x)` 为位置依赖局部变量；CA 善编码 `A`，PA 善编码 `t(x)`。串联时通道注意力先改原始特征、像素注意力再在被改特征上提取，达不到全局最优；并行三种注意力可同时从**原始特征**提取共享全局与位置依赖信息，更利于去雾。

3.  **混合结构块（Mix Structure Block）**（论文 3.3 节）
    - **连接方式**：Transformer 风格块，MSPLCK 与 EPA 串联构成完整块；输入依次经 MSPLCK、EPA，各自带残差连接（见上各公式中的 `y = x + ...`）。MSPLCK 补足单 Transformer 自注意力缺乏的多尺度特性，EPA 补足单 Transformer FFN 缺乏的处理不均匀雾霾能力。

### 训练方式（论文 3.4、4.2 节）
- **损失函数**：L1 损失 + **对比学习损失** 的加权和（公式 8）。对比损失分子为 `Ĵ` 与清晰图 `J` 在各层特征上的 L1 距离、分母为 `Ĵ` 与有雾图 `I` 的对应距离（拉近正样本、推远负样本），`D(·,·)` 为 L1 损失。
- **对比学习细节**：固定预训练 **ResNet-152**，提取第 **11、35、143、152** 层特征，对应权重系数 `ωi = 1/16, 1/8, 1/4, 1`；平衡超参 `β = 0.1`。
- **优化器**：AdamW（β1=0.9, β2=0.999），初始学习率 `2×10⁻⁴`，按余弦退火衰减至 `2×10⁻⁶`。
- **训练配置**：4 卡 RTX-3090；训练时随机裁剪到 256×256；ITS 上训 500 epoch、OTS 上训 40 epoch、RESIDE-6K 上训 1000 epoch；提供 -S/-B/-L 三个变体（详细配置见论文 Table 2，提取文本未给出 Table 2 具体数值）。

### 推理流程
有雾图像单次前向通过 5 阶段 U-Net（含多个 Mix 结构块），输出去雾图像。

### 与已有方法的差异
- **与标准 Transformer**：MSPLCK 替代多头自注意力（增强多尺度），EPA 替代 FFN（增强不均匀分布处理）。
- **与 FFA-Net / AECR-Net 等串联/分立注意力**：EPA **并行**使用三种注意力，从原始特征同时提取信息，而非串联递进修改。
- **与大核 CNN（RepLKNet / VAN）**：MSPLCK 用**多个并行不同尺度的膨胀大核**（借鉴 VAN 把大核分解为深度卷积+深度膨胀卷积+1×1 的思路），而非单一超大核，更好保留多尺度信息。
## 实验

- **使用数据集**：RESIDE（含 RESIDE-IN/ITS、RESIDE-OUT/OTS、SOTS 测试集）与 RESIDE-6K。
    - RESIDE-IN：训练 13,990 对，测 SOTS indoor 500 对。
    - RESIDE-OUT：训练 313,950 对，测 SOTS outdoor 500 对。
    - RESIDE-6K：3,000 ITS + 3,000 OTS 训练，余 1,000 室内外混合对测试（实验设置沿用 DA）。
- **对比方法**（Table 1 共 15 个先前方法）：DCP、DehazeNet、MSCNN、AOD-Net、GFN、GCANet、GridDehazeNet、MSBDN、PFDN、FFA-Net、AECR-Net、PMNet、MAXIM、Dehamer、UDN，覆盖先验方法、CNN 方法与 Transformer 方法。
- **评价指标**：PSNR 与 SSIM。
- **主实验结果（Table 1）**：本文模型在三个数据集上 PSNR/SSIM 均超过此前所有方法。
    - **SOTS 室内（RESIDE-IN）**：MixDehazeNet-L 达 **42.62 dB / 0.997**，是首个超过 42 dB 的模型；-B 40.90/0.996，-S 39.47/0.995。此前最佳 UDN 为 38.62/0.991。
    - **SOTS 室外（RESIDE-OUT）**：-L 36.50/0.986，-B 35.67/0.985，-S 35.09/0.985（此前最佳 Dehamer 35.18/0.986、UDN 34.93/0.987）。
    - **RESIDE-6K**：-S 30.18/0.973（此前最佳 FFA-Net 29.96/0.973）；Table 1 中 -B、-L 在该集为空缺（“-”）。
    - PSNR 随 Mix 结构块数量增加而提升；作者建议 -S 用于实时去雾、-L 用于高清晰度要求场景。
    - 定性比较（Fig. 5 室内、Fig. 6 室外）：DCP/GridDehazeNet/FFA-Net 复原结果含不同程度伪影，本文方法更清晰、伪影更少。
- **消融实验**：提取文本（前 11 页正文）未包含独立的消融实验章节与定量结果。
- **效率信息（Table 1 OVERHEAD 列）**：
    - **参数量**：-S 3.16M、-B 6.25M、-L 12.42M。
    - **计算量（MACs）**：-S 22.06G、-B 43.61G、-L 86.7G。
    - **延迟（Latency）**：-S 14.56ms、-B 28.45ms、-L 56.52ms。
    - 对照：FFA-Net 287.8G MACs / 55.91ms，Dehamer 132.45M 参数，PMNet 18.90M/81.13G——本文在参数与计算上更均衡。
## 局限

- **计算成本**：虽比部分 Transformer 高效，MixDehazeNet-L 的 86.7G MACs / 56.52ms 延迟对移动端、自动驾驶等实时场景可能偏高；作者也指出 Transformer 方法参数多、训练难，而本文 CNN 方法复杂度同样不低（最大变体需 4 卡 RTX-3090 训练）。
- **数据集局限**：实验仅在 RESIDE 系列**合成数据集**上进行。真实雾霾的分布与物理特性更复杂，模型在真实数据上的泛化能力未被验证（提取文本中无真实雾图实验）。
- **消融实验缺失（据提取文本）**：前 11 页正文未给出定量消融，无法逐一量化 MSPLCK 三尺度核、EPA 三注意力分支的单独贡献；模块设计必要性论证略显不足（注：完整论文可能含 Table 2 / 消融章节，但提取缓存未覆盖，待核）。
- **结果空缺**：Table 1 中 -B、-L 在 RESIDE-6K 上、以及部分对比方法在 RESIDE-OUT/6K 上无结果，横向比较不完整。
## 个人评论

1.  **并行思想是核心方法论**：MSPLCK 的“并行多尺度大核”与 EPA 的“并行多类型注意力”都把“顺序串联→并行直连原始特征”作为破局点。其价值不在于注意力本身新颖，而在于明确论证了“串联会让后置注意力在被污染的特征上工作、达不到全局最优”，并用并行结构规避。这种从原始特征并行抽取互补信息的思路可迁移到其他多线索任务。
2.  **把退化物理模型映射到模块**：论文将大气散射模型的 `A`（全局共享）与 `t(x)`（位置依赖）分别对应通道注意力与像素注意力，再据此设计 EPA。这种“退化模型 → 特征类型 → 注意力类型”的推导链使模块有针对性，比通用注意力更有解释力。做去雨/去噪/去模糊时，可先问“退化项分别对应什么特征”。
3.  **工程上的可复现性较好**：提供 -S/-B/-L 三档，超参（层数、ResNet-152 第 11/35/143/152 层、ωi、β=0.1、学习率 2e-4→2e-6 余弦退火）写得相当完整，且代码开源，复现门槛低。
4.  **可批判处**：缺正式消融是最大短板（提取文本范围内未见），“并行优于串联”更多靠论证而非对照实验支撑；且全为合成数据，SOTA 数字漂亮但真实场景说服力有限。

### 使用建议

- **快速了解**：读 Abstract、Introduction（两条动机）、Section 3 中 MSPLCK 与 EPA 的图（Fig. 3、4）与公式，以及 Section 4.3 的 Table 1 主结果。
- **复现**：精读 Section 3 全部公式与网络图（Fig. 2/3/4）、Section 4.2 实现细节（优化器、学习率、对比损失层与系数、训练 epoch），并对照仓库代码与论文 Table 2 变体配置。
- **借鉴创新点**：
    - 并行多分支直接处理原始特征的模块设计范式。
    - 将任务退化先验映射到注意力类型的设计方法（去雨/去雾专用注意力）。
    - 用多尺度并行膨胀卷积平衡感受野与多尺度特性。
- **写相关工作**：可归入“图像去雾的深度学习方法”“基于大卷积核/膨胀卷积的 CNN 架构”“注意力机制在图像复原中的应用”“对比学习用于底层视觉”。
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
本文属于计算机视觉**图像复原（low-level vision）**方向下的**单图像去雾**任务。论文提出去雾网络 MixDehazeNet，解决两大问题：引入大卷积核时图像多尺度特性被忽略；标准串联注意力模块无法充分应对不均匀雾霾分布。论文的真实主题是图像去雾，故主题应归 `E_图像复原_超分_去噪_去雨去雾`；同时其核心模块 EPA 是一个注意力算子，文件名亦取自 MSPLCK 与 EPA 两个模块，故保留 `B_注意力算子模块` 作为次主题。

## 2. 一句话总结
MixDehazeNet 用一个 Transformer 风格的 Mix 结构块（以多尺度并行大卷积核模块 MSPLCK 替代自注意力、以增强并行注意力模块 EPA 替代 FFN），在 5 阶段 U-Net 上同时解决去雾中“多尺度被忽略”和“雾霾分布不均匀”两个问题，在三个 RESIDE 基准上达到 SOTA（SOTS 室内首破 42 dB）。

## 3. 背景与问题
- **为什么要做**：雾霾普遍存在于图像/视频，降低人类与深度模型的识别能力，隐式影响目标检测、重识别、语义分割等下游任务；去雾作为底层预处理第一步对学术与工业都重要。
- **物理基础**：大气散射模型 `I(x)=J(x)·t(x)+A·(1−t(x))`，`t(x)=e^{−β·d(x)}`；早期先验方法估计 `A`、`t(x)`，先验不满足则失真。
- **之前方法的两条局限**：
    1.  **多尺度被忽略**：CNN/Transformer 借大感受野提升性能，但去雾中图像多尺度特性常被忽略；雾浓度分布不均，不同核尺寸应捕捉不同尺度区域。
    2.  **注意力串联不当**：以往去雾网络（FFA-Net、AECR-Net、GCANet 等）单独设计像素/通道注意力或串联使用。通道注意力宜编码全局共享变量 `A`，像素注意力宜编码位置相关局部变量 `t(x)`；串联使后者在被前者修改的特征上工作，达不到全局最优。
- **核心矛盾**：如何同时利用大核的全局/长距离建模与多尺度特性，并从原始特征并行提取全局共享信息与局部依赖信息。

## 4. 核心贡献
1.  **MSPLCK**：并行三个不同尺度（等效核 7/13/19）的深度膨胀卷积，兼具大感受野与多尺度，能同时捕大雾区、复原纹理。
2.  **EPA**：并行简单像素注意力（SPA）、通道注意力（CA）、像素注意力（PA），从原始特征并行提取共享全局（`A`）与位置依赖（`t(x)`）信息，适配不均匀雾霾。
3.  **Mix 结构块**：Transformer 风格块，MSPLCK 替自注意力、EPA 替 FFN。
4.  **对比学习损失**：受 AECR-Net 启发引入，改用 ResNet-152（优于 VGG19）作对比骨干。
5.  **SOTA**：三个基准均最优，-L 首破 SOTS 室内 42 dB。

## 5. 方法详解
### 整体框架
5 阶段 U-Net 嵌入 Mix 结构块；下采样 stride=2 的 3×3 卷积，上采样 PWConv+PixelShuffle；跳跃用 SK Fusion 融合，末端用 soft reconstruction 代替全局残差（去雾约束更强）。

### 输入与输出
- **输入**：有雾图 `I`；**输出**：去雾图 `Ĵ`（真值清晰图 `J`）。

### 关键模块
1.  **MSPLCK（3.1，公式 2–3）**：`x̂=BatchNorm(x)` → `x1=PWConv(x̂)` → `x2=Conv₅(x1)` → `x3=Concat(DWDConv19, DWDConv13, DWDConv7)(x2)`（三者膨胀率均 3，深度膨胀卷积底核 7×7/5×5/3×3，等效核 19/13/7；通道变三倍）→ MLP(PWConv-GELU-PWConv) 降维 + 残差 `y=x+...`。大/中核捕大雾区、小核复原纹理。
2.  **EPA（3.2，公式 4–7）**：`x̂=BatchNorm(x)`，三并行分支：
    - SPA：`PFs=Conv₃(PWConv(x̂))`，`PAs=Sigmoid(PWConv(x̂))`，`Fs=PFs⊗PAs`（位置依赖）。
    - PA：`PAp=Sigmoid(PWConv(GELU(PWConv(x̂))))`，`Fp=x̂⊗PAp`（全局像素门控）。
    - CA：`CAc=Sigmoid(PWConv(GELU(PWConv(GAP(x̂)))))`，`Fc=x̂⊗CAc`（全局通道）。
    - 融合：`F=Concat(Fs,Fc,Fp)` → MLP 降维 → `y=x+...`（残差到 `x̂`）。CA 编码 `A`、PA 编码 `t(x)`，并行避免串联污染。
3.  **Mix 结构块（3.3）**：MSPLCK 与 EPA 串联，各带残差；分别补足单 Transformer 自注意力缺乏的多尺度、FFN 缺乏的不均匀雾霾处理能力。

### 训练方式（3.4、4.2）
- L1 损失 + 对比学习损失加权（公式 8）：分子 `Ĵ`–`J` 的逐层 L1、分母 `Ĵ`–`I` 的逐层 L1。
- 对比：固定 ResNet-152 第 11/35/143/152 层，`ωi=1/16,1/8,1/4,1`，`β=0.1`。
- AdamW（0.9/0.999），lr 2e-4 余弦退火至 2e-6；4 卡 RTX-3090，256×256 裁剪；ITS 500 / OTS 40 / RESIDE-6K 1000 epoch。

### 推理流程
单次前向通过 5 阶段 U-Net（多个 Mix 结构块），输出去雾图。

### 与已有方法的差异
- 替换 Transformer 自注意力与 FFN；EPA 并行（非串联）从原始特征取信息；MSPLCK 用多并行膨胀大核（非单一超大核）。

## 6. 实验与结果
- **数据集**：RESIDE-IN（13,990 训 / SOTS indoor 500 测）、RESIDE-OUT（313,950 训 / SOTS outdoor 500 测）、RESIDE-6K（6,000 训测 1,000，设置沿用 DA）。
- **对比方法**：Table 1 共 15 个先前方法（DCP、DehazeNet、MSCNN、AOD-Net、GFN、GCANet、GridDehazeNet、MSBDN、PFDN、FFA-Net、AECR-Net、PMNet、MAXIM、Dehamer、UDN）。
- **指标**：PSNR / SSIM。
- **主结果（Table 1）**：三集均超此前所有方法。
    - SOTS 室内：-L 42.62/0.997（首破 42 dB），-B 40.90/0.996，-S 39.47/0.995；前最佳 UDN 38.62/0.991。
    - SOTS 室外：-L 36.50/0.986，-B 35.67/0.985，-S 35.09/0.985。
    - RESIDE-6K：-S 30.18/0.973（前最佳 FFA-Net 29.96/0.973）；-B、-L 在该集为空缺。
    - PSNR 随块数增加而升；-S 宜实时、-L 宜高清晰度。
- **定性**：Fig. 5/6 显示本文伪影更少、更清晰。
- **效率（Table 1 OVERHEAD）**：参数 3.16/6.25/12.42M，MACs 22.06/43.61/86.7G，延迟 14.56/28.45/56.52ms；对照 FFA-Net 287.8G/55.91ms、Dehamer 132.45M。
- **消融**：提取文本（前 11 页）未含独立消融章节与定量结果。

## 7. 这篇论文真正有价值的地方
1.  **并行 vs 串联的论证**：明确指出串联注意力让后置分支在被污染特征上工作、达不到全局最优，并用并行从原始特征取互补信息规避——这是方法层面最有迁移价值的洞见。
2.  **退化物理模型 → 注意力类型的映射**：把 `A`/`t(x)` 对应 CA/PA，使模块设计有解释力而非堆叠通用注意力。
3.  **多尺度并行膨胀大核**：以并行不同尺度膨胀卷积同时兼顾大感受野与纹理细节，平衡了感受野与多尺度，且计算开销可控。
4.  **完整可复现的配置**：超参、对比损失层与系数、训练设置齐全且代码开源。

## 8. 局限与问题
- **计算成本**：-L 的 86.7G MACs/56.52ms 对实时场景偏高，最大变体需 4 卡 RTX-3090。
- **合成数据**：仅在 RESIDE 合成集评测，真实雾图泛化未验证。
- **消融缺失（据提取文本）**：前 11 页正文无定量消融，模块各分支贡献未单独量化（完整论文或含 Table 2/消融，提取缓存未覆盖，待核）。
- **结果空缺**：Table 1 中 -B/-L 在 RESIDE-6K、部分对比方法在 OUT/6K 上无结果，横比不完整。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Introduction 两条动机 + Fig. 3/4 + Table 1。
- **复现**：精读 Section 3 公式与 Fig. 2/3/4、Section 4.2 实现细节，对照开源仓库与 Table 2。
- **借鉴**：并行多分支处理原始特征的范式；退化先验映射到注意力类型；多尺度并行膨胀卷积。
- **写相关工作**：图像去雾深度学习方法 / 大核与膨胀卷积 CNN / 注意力用于图像复原 / 对比学习用于底层视觉。

## 10. 和其他论文的关系
- **注意力/去雾相关**：与 [[FFA-Net]]（通道+像素注意力、密集连接）、[[AECR-Net]]（引入对比学习去雾，本文沿用其对比损失思路但改用 ResNet-152）相关，本文改为并行注意力。
- **大卷积核相关**：与 [[RepLKNet]]（超大核 31×31）、[[Visual Attention Network]]（大核分解为深度卷积+深度膨胀卷积+1×1）在大感受野思路上相关；MSPLCK 借鉴 VAN 的分解并扩展为多尺度并行。
- **去雾 SOTA / 借用组件相关**：与 [[PMNet]]、[[UDN]]、[[Dehazeformer]] 构成性能对比；SK Fusion 与 soft reconstruction 借自 Dehazeformer，与 [[Dehamer]] 同期对比。

## 11. 关键词
图像去雾, 混合结构块, 多尺度并行大卷积核(MSPLCK), 增强并行注意力(EPA), 注意力机制, 深度膨胀卷积, 对比学习, 大气散射模型, U-Net, 不均匀雾霾分布, SK Fusion, 软重建。

## 12. 可信度说明
本精读基于 PDF 提取文本的**前 11 页**（缓存标注 11/11 页、约 25000 字符上限，提取质量好），涵盖摘要、引言、相关工作、方法（含公式 1–8）、实验数据集与实现细节、Table 1 全部定量/效率数字、Fig. 1–6 描述。提取文本在 25000 字符处截断（原文约 40671 字符），**Table 2 变体详细配置、定量消融实验、参考文献列表等后续内容未被覆盖**，相关处已标注“据提取文本/待核”。已修正原笔记的事实错误：年份 2021→2023（arXiv:2305.17654, 2023-05-28）、作者拆分为四人并标注共同一作/通讯、对比方法数“14→15”、补全训练 epoch 与对照效率数字。主题由 `B_注意力算子模块` 调整为 `E_图像复原_超分_去噪_去雨去雾`（论文真实任务为去雾），保留 B 为次主题。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 11/11 页, 但正文在 25000 字符处截断, 原文约 40671 字符, Table 2 / 消融 / 参考文献未覆盖); 来源缓存: `.paper-cache/extracts/MSPLCK&EPA.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 2026-06-18 据提取文本重核优化。
<!-- AI_READING_NOTE_END -->
