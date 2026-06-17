---
title: "DEA-Net: Single image dehazing based on detail-enhanced convolution and content-guided attention"
authors:
  - "Zixuan Chen"
  - "Zewei He"
  - "Zhe-Ming Lu"
year: 2023
venue: arXiv
doi: 
pdf: [[CGAFusion.pdf]]
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
extract_cache: .paper-cache/extracts/CGAFusion.txt
---

# DEA-Net: Single image dehazing based on detail-enhanced convolution and content-guided attention

## 基本信息
- **PDF**: [[CGAFusion.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`, `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | DEA-Net: Single image dehazing based on detail-enhanced convolution and content-guided attention |
| **作者** | Zixuan Chen; Zewei He; Zhe-Ming Lu (浙江大学航空航天学院; 前两位作者贡献相同; 通讯作者 Zhe-Ming Lu) |
| **发表时间** | 2023 (arXiv:2301.04805v1, 2023-01-12) |
| **刊物/会议** | arXiv 预印本 (LaTeX 期刊模板, IEEE 风格) |
| **DOI** | 未明确 (arXiv:2301.04805) |
| **代码** | https://github.com/cecret3350/DEA-Net |

## 摘要

清理后的英文原摘要 (修复空格与连字符断裂, 剔除杂入的图轴数字 41/40/39 等):

> Single image dehazing is a challenging ill-posed problem which estimates latent haze-free images from observed hazy images. Some existing deep learning based methods are devoted to improving the model performance via increasing the depth or width of convolution. The learning ability of convolutional neural network (CNN) structure is still under-explored. In this paper, a detail-enhanced attention block (DEAB) consisting of the detail-enhanced convolution (DEConv) and the content-guided attention (CGA) is proposed to boost the feature learning for improving the dehazing performance. Specifically, the DEConv integrates prior information into normal convolution layer to enhance the representation and generalization capacity. Then by using the re-parameterization technique, DEConv is equivalently converted into a vanilla convolution with NO extra parameters and computational cost. By assigning unique spatial importance map (SIM) to every channel, CGA can attend more useful information encoded in features. In addition, a CGA-based mixup fusion scheme is presented to effectively fuse the features and aid the gradient flow. By combining above mentioned components, we propose our detail-enhanced attention network (DEA-Net) for recovering high-quality haze-free images. Extensive experimental results demonstrate the effectiveness of our DEA-Net, outperforming the state-of-the-art (SOTA) methods by boosting the PSNR index over 41 dB with only 3.653 M parameters. The source code of our DEA-Net will be made available at https://github.com/cecret3350/DEA-Net.

中文翻译:

> 单幅图像去雾是一个有挑战性的病态 (ill-posed) 问题, 目标是从观测到的有雾图像估计出潜在的无雾图像。一些现有的基于深度学习的方法致力于通过增加卷积的深度或宽度来提升模型性能, 而 CNN 结构本身的学习能力仍未被充分挖掘。本文提出一个细节增强注意力块 (DEAB), 由细节增强卷积 (DEConv) 和内容引导注意力 (CGA) 组成, 用以增强特征学习、提升去雾性能。具体而言, DEConv 将先验信息融入普通卷积层以增强表示与泛化能力; 随后借助重参数化 (re-parameterization) 技术, DEConv 可被等价转换为一个普通卷积, 不带来任何额外的参数和计算开销。通过为每个通道分配独特的空间重要性图 (SIM), CGA 能够关注特征中编码的更有用的信息。此外, 本文还提出一种基于 CGA 的 mixup 融合方案, 以有效融合特征并辅助梯度流。将上述组件结合, 作者构建了细节增强注意力网络 (DEA-Net) 来恢复高质量无雾图像。大量实验结果表明 DEA-Net 有效, 以仅 3.653 M 参数将 PSNR 指标提升至超过 41 dB, 优于当前最先进 (SOTA) 方法。源代码将在 https://github.com/cecret3350/DEA-Net 公开。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做:** 雾天拍摄的图像通常在对比度和颜色上明显退化, 会导致后续高层视觉任务 (目标检测、语义分割) 的性能显著下降。因此单幅图像去雾作为一项底层 (low-level) 图像复原任务, 可以充当高层任务的预处理步骤, 十余年来在学术界和工业界都受到广泛关注。
- **之前方法的两类问题 (提取文本 Introduction 明确列举):**
  1. **香草卷积效力不足 (Less effectiveness of vanilla convolution):** 已有工作证明精心设计的先验 (暗通道先验 DCP、非局部 haze-line 先验、颜色衰减先验 CAP) 有助于恢复缺失信息, 但大多数去雾方法仍使用经典卷积层做特征提取而不利用这些先验。香草卷积在巨大的解空间里无约束地搜索, 限制了表达/建模能力。基于 transformer 的方法 (如 Dehamer) 虽可扩大感受野挖掘长程依赖, 但代价是复杂的训练策略、繁琐的超参调优, 以及高昂的计算和显存开销。理想方案是把设计良好的先验嵌入 CNN 来提升特征学习能力。
  2. **雾的非均匀性 (Haze non-uniformity):** 去雾问题存在两种非均匀性 —— **图像层面**的雾分布不均 (厚雾/薄雾), 以及**特征层面**通道间的雾信息差异。FFA-Net (Qin 等) 用像素注意力 (即空间注意力) 生成空间重要性图 SIM 来区分厚薄雾区; PMDNet (Ye 等) 用密度估计模块建模雾密度, 本质也是空间注意力。但**特征层面**的非均匀性鲜有人关注: FFA-Net 用的通道注意力只产出一个通道注意力向量, 无法考虑空间维度的上下文信息。由于不同通道因滤波器作用不同而含义不同, 作者主张**空间重要性图应当是通道特异 (channel-specific) 的**, 并同时考虑图像层面和特征层面两种非均匀性。
- **核心矛盾:** 如何在不显著增加参数和计算成本的前提下, 把传统先验 (尤其是梯度先验) 有效融入 CNN, 并同时处理图像级与特征级两种非均匀性。

## 关键贡献

提取文本 Introduction 末尾"main contributions"明确列出三条贡献 (笔记按其行文拆为四点叙述):

1.  **细节增强卷积 (DEConv):** 包含并行部署的香草卷积与差分卷积。据作者所述, 这是首次将差分卷积引入图像去雾问题。通过把先验信息编码进普通卷积层增强了 DEConv 的表示与泛化能力, 并借助重参数化技术将其等价转换为普通卷积, **没有额外的参数和计算开销**。
2.  **内容引导注意力 (CGA):** 一种以"由粗到精 (coarse-to-fine)"方式生成**通道特异 SIM** 的新颖注意力机制。利用输入特征自身的内容来引导 SIM 的生成, CGA 为每个通道分配独特的 SIM, 使模型能关注每个通道的显著区域, 从而强调特征中更有用的信息。
3.  **基于 CGA 的 mixup 融合方案:** 用于有效融合编码器部分的低层特征与对应的高层特征, 辅助梯度流。
4.  **DEA-Net 整网:** 结合 DEConv、CGA 与 CGA-based mixup 融合, 构建端到端去雾网络 DEA-Net。它在多个基准数据集上优于 SOTA 去雾方法, 以更快的推理速度取得更精确的结果 —— 摘要给出的代表性数字是 **PSNR > 41 dB、参数仅 3.653 M** (该数值据 Fig.1 caption 在 SOTS-indoor 上测得)。

## 方法

### 整体框架
DEA-Net (Fig.2(a)) 由三部分组成: **编码器部分 (encoder part)、特征变换部分 (feature transform part)、解码器部分 (decoder part)**, 是一个**三层级 (three-level) 的编码器-解码器结构**。不同层级使用不同的块: **level 1 & 2 用 DEB, level 3 (核心特征变换部分) 用堆叠的 DEAB** 来学习无雾特征。图中编码器/解码器各层标注了块的重复次数 (DEB×N1…N5, DEAB×N3), 并通过下采样/上采样和两处 Fusion 连接收缩-扩张路径。

### 输入与输出
- **输入:** 雾天图像 `I ∈ R^{3×H×W}`
- **输出:** 恢复后的无雾图像 `J ∈ R^{3×H×W}`

### 关键模块
1.  **细节增强卷积 (DEConv):**
    - **结构 (Fig.3):** 5 个并行部署的卷积层 —— 1 个香草卷积 (VC) 和 4 个差分卷积: 中心差分卷积 (CDC)、角度差分卷积 (ADC)、水平差分卷积 (HDC)、垂直差分卷积 (VDC)。其中 CDC、ADC 源自已有工作 (Yu 等的 CDC 等), HDC、VDC 是本文新推导的。
    - **机制:** 香草卷积负责获取强度级 (intensity-level) 信息; 差分卷积先计算像素对的差值再与卷积核卷积, 用于增强梯度级 (gradient-level) 信息。以 **HDC (Fig.4)** 为例, 先计算所选像素对的水平梯度差; 训练后将学到的核权重等价重排, 直接作用于未改动的输入特征。等价核具有与传统局部描述子相似的形式 (**水平方向权重之和为零**), Sobel、Prewitt、Scharr 的水平核可看作该等价核的特例; VDC 通过把水平梯度换成垂直梯度做类似推导。各卷积输出特征图**直接相加**得到 DEConv 输出。
    - **重参数化 (Fig.5, 公式1):** 5 个并行卷积会增加参数和推理时间, 故利用卷积的**可加性 (additivity)**: 若多个同尺寸 2D 核以相同 stride/padding 作用于同一输入且输出求和, 则可把这些核在对应位置相加得到一个等价核, 产生相同输出。公式: `F_out = DEConv(F_in) = Σ_{i=1..5} F_in * K_i = F_in * (Σ_{i=1..5} K_i) = F_in * K_cvt` (偏置略去), 其中 `K_{1..5}` 分别为 VC/CDC/ADC/HDC/VDC 的核, `K_cvt` 为合并后的转换核。反向传播阶段五个核各自按链式法则独立更新; 前向传播阶段固定核权重并按位相加得到 `K_cvt`。重参数化能**同时加速训练与测试** (二者都含前向传播)。因此推理时 DEConv 的计算成本与一个标准卷积完全相同。
    - **与已有方法的差异:** 不是靠堆深/堆宽, 而是把领域先验 (梯度) 直接嵌入卷积算子, 在保持效率的同时增强特征提取的针对性。

2.  **内容引导注意力 (CGA) —— 据提取文本 Introduction 描述 (详细架构在缓存未覆盖页, 待核):**
    - **作用维度:** 生成**通道特异的空间注意力图 (channel-specific SIM)**, 同时考虑空间与通道维度。
    - **两步生成 (coarse-to-fine):**
        a. **粗略生成:** 对输入特征, 用文献 [19] 的空间注意力机制和文献 [20] 的通道注意力分别生成初始的 (粗略) SIM。
        b. **内容引导细化:** 依据输入特征的**每个通道**对初始 SIM 进行细化, 得到最终的通道特异 SIM, 使模型聚焦每个通道的独特部分。
    - **可插入性:** 作者强调 CGA 是通用基础块, 可插入各种网络以提升多种图像复原任务的性能。
    - **(注: CGA 内部空间/通道注意力的具体算子细节、细化方式公式在提取缓存未覆盖的后续页, 此处仅据 Introduction 概述, 待核。)**

3.  **细节增强 (注意力) 块 DEB / DEAB (Fig.2(b)(c)):**
    - **DEB:** 据图示为 `DEConv -> 3×3 Conv -> ReLU -> DEConv -> 3×3 Conv -> ReLU`, 带一条逐元素相加的跳跃连接。部署在编码器/解码器 (level 1 & 2)。
    - **DEAB:** 在 DEB 基础上插入 CGA (图中含逐元素相乘 ×) 与跳跃连接, 部署在 level 3 的特征变换部分。(块内算子的精确顺序以原文图为准, 提取文本未给出文字化的逐层公式。)

4.  **基于 CGA 的 mixup 融合方案 (Fig.2(d)):**
    - **动机:** 浅层特征与深层特征因感受野不同而编码信息差异巨大 (深层一个像素源自浅层一片区域), 简单相加或拼接无法解决感受野不匹配 (receptive field mismatch) 问题。
    - **机制:** 用 CGA 处理低层特征 `F_low` 生成空间权重 `W`, 再以 `W` 和 `1−W` 对低层与高层特征做加权混合 (mixup), 自适应地融合 `F_low` 与 `F_high` 得到 `F_fuse` (图中还含 1×1 Conv 与逐元素加/乘), 以增强信息流和梯度回传。

### 模块连接
整体流程 (Fig.2(a)): 输入雾图经编码器逐步下采样提取特征, 进入由多个 DEAB 组成的特征变换部分做深度处理, 再经解码器逐步上采样并通过两处 CGA-based Fusion 融合浅深特征, 输出无雾图。U-net 式框架使主要耗时的卷积计算在低分辨率空间进行 (沿用 [6][10][21][22])。

### 训练方式
- 训练阶段, DEConv 的 5 个并行卷积按链式法则**各自独立**更新梯度。
- **损失函数:** 提取缓存 (前约 5 页, 截至重参数化公式) **未覆盖**实验/实现细节, 因此损失函数在提取文本中未明确; 图像去雾常用像素级 L1/L2 重建损失, 此为一般推断而非原文明示。

### 推理流程
- 推理阶段先对所有 DEConv 做重参数化, 将 5 个核合并为单个标准卷积核 `K_cvt`, 使 DEB/DEAB 退化为含标准卷积的轻量结构, 再前向得到去雾结果。

## 实验

> 说明: 本仓库的提取缓存 `max_chars=25000`, 实际只覆盖到第 5 页 (摘要、引言、相关工作、方法的 DEConv/重参数化部分), **完整的实验章节 (Sec. IV) 不在提取文本内**。以下数字凡来自摘要/图1 caption 的, 标"(提取文本支持)"; 凡只见于原笔记或原文后续页的, 标"(据原文后续页, 提取缓存未覆盖, 待核)"。

- **数据集:** 提取文本明确提到的是 **SOTS-indoor** (Fig.1 的 PSNR-vs-参数图在 SOTS-indoor 上测得)。RESIDE 其他子集、SOTS-outdoor、真实雾图等是否使用, 提取缓存未覆盖, 待核。
- **对比方法 (提取文本支持, 见 Fig.1 caption 与相关工作):** FFA-Net (AAAI 2020)、MSBDN (CVPR 2020)、AECR-Net (CVPR 2021)、SGID-PFF (TIP 2022)、UDN (AAAI 2022)、PMDNet (ECCV 2022)、Dehamer (CVPR 2022)。图中本文方法标为 DEA-Net 及其变体 DEA-Net-CR。
- **评价指标:** **PSNR** 与模型**参数量 (M)** (提取文本支持; Fig.1 为 PSNR vs. number of parameters)。SSIM 等其他指标在提取缓存未覆盖, 待核。
- **主结果 (提取文本支持, 摘要+图1):** DEA-Net 以仅 **3.653 M** 参数将 SOTS-indoor 的 PSNR 提升至**超过 41 dB**, 在参数量-PSNR 权衡上优于 2020 年后的多个 SOTA 方法。
- **消融实验:** 摘要仅称"Extensive experimental results demonstrate the effectiveness", 具体消融表 (DEConv 各差分卷积组合、CGA 有无、融合方案对比等) 在提取缓存未覆盖, 待核。
- **效率:** 重参数化使 DEConv 在推理时**相对香草卷积无额外参数/计算开销**; 摘要称推理速度更快、结果更精确 (提取文本支持)。

## 局限

1.  **任务范围:** 论文针对静态**单幅图像去雾**, 未探讨视频去雾或动态场景。
2.  **提取证据有限:** 本仓库提取缓存仅到第 5 页, 完整实验/消融/泛化结果不在其内, 因此本笔记对实验部分的核实程度有限 (待核)。
3.  **假设依赖:** 方法有效性部分依赖"梯度先验对去雾有帮助"这一假设。对雾气非常均匀或纹理极简的场景, DEConv 的差分分支收益可能减弱。
4.  **CGA 复杂度:** CGA 是两步 (空间注意力+通道注意力+内容引导细化) 机制, 比单一通道或空间注意力更复杂; 其在整网中的计算占比, 提取文本未给出。
5.  **核心结果集中在 SOTS-indoor:** 提取文本展示的代表性数字主要基于 SOTS-indoor, 跨数据集泛化在提取缓存未覆盖, 存在对特定数据集过拟合的潜在担忧 (待核)。

## 个人评论

1.  **先验嵌入卷积的范式:** 将传统图像处理先验 (梯度, 经 Sobel/Prewitt/Scharr 视角) 以可学习方式嵌入卷积算子 (DEConv), 并用重参数化消解多分支带来的参数/计算代价。这种"重新设计卷积核"的思路对去噪、超分等底层视觉任务有迁移价值。
2.  **通道特异空间注意力:** CGA 的核心主张 —— 不同通道编码不同语义, 因而空间重要性图应当通道特异 —— 比统一空间注意力或纯通道注意力更细。这一观点本身 (而非仅去雾) 是其作为通用注意力算子模块的价值所在, 也是本笔记同时挂 `B_注意力算子模块` 的原因。
3.  **训练-推理解耦的工程优雅:** 训练多分支 (强表达) / 推理单分支 (高效率) 的重参数化与 RepVGG 思路相通, 在轻量化设计中值得借鉴。
4.  **以小参数取得高 PSNR:** 3.653 M 参数 / >41 dB 的权衡, 印证了精心设计模块往往比堆深堆宽更有效 —— 但需注意该数字目前只在 SOTS-indoor 一个设置上得到提取文本支持。

### 使用建议

- **快速了解:** 读摘要、Fig.1 (PSNR vs 参数量)、Fig.2 (整体框架+各模块图) 即可掌握核心思想与性能优势。
- **复现:** 精读 Sec. III METHODOLOGY, 研究 Fig.2–5, 理解 DEConv 并行结构与重参数化公式 (公式1)、CGA 两步生成、以及 CGA-based mixup 融合的连接方式; 直接参考官方代码 https://github.com/cecret3350/DEA-Net。
- **借鉴创新点:**
    - **DEConv:** 学习如何把梯度/LBP 等手工先验设计成可学习差分卷积, 并用重参数化解决多分支效率。
    - **CGA:** 学习"粗略生成 + 内容引导细化"以产出通道特异空间注意力的思路, 可迁移到其他注意力设计。
    - **融合策略:** 用基于注意力的自适应 mixup 融合替代简单相加/拼接以缓解感受野不匹配。
- **写 Related Work:** 可归入"基于注意力的去雾方法""先验嵌入的 CNN 设计""网络重参数化/训练-推理解耦"等类别引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页:
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉**底层图像复原 (low-level image restoration)** 方向, 具体任务是**单幅图像去雾 (single image dehazing)**。其技术核心是两个新模块: 细节增强卷积 (DEConv) 与内容引导注意力 (CGA), 以及一个基于 CGA 的 mixup 融合方案, 组合成 DEA-Net。因此本笔记的**主主题定为 `E_图像复原_超分_去噪_去雨去雾`** (去雾属该主题), 同时因 CGA 是一个可复用的通用注意力算子、且仓库文件名 (stem=CGAFusion) 也以此为切入点, 把 `B_注意力算子模块` 作为次主题保留。

## 2. 一句话总结
本文提出细节增强卷积 (DEConv, 把差分/梯度先验嵌入卷积并经重参数化零开销化) 与内容引导注意力 (CGA, 为每个通道生成通道特异空间重要性图), 组合为 DEA-Net, 在 SOTS-indoor 上以 3.653 M 参数取得 >41 dB 的去雾 PSNR。

## 3. 背景与问题
- **为什么要做:** 雾天图像在对比度/颜色上退化, 拖累下游高层视觉任务; 去雾作为底层复原任务可作其预处理, 价值长期受关注。
- **之前方法的两个问题 (提取文本明确):**
  1. **香草卷积效力不足:** DCP、非局部 haze-line、CAP 等先验对恢复缺失信息有用, 但多数去雾网络仍用无约束的经典卷积, 限制表达能力; transformer 类方法虽扩大感受野却带来训练复杂度与算力/显存开销。理想做法是把先验嵌入 CNN。
  2. **雾的非均匀性:** 图像级 (厚/薄雾) 与特征级 (通道间雾信息差异) 两种非均匀性。前者已有空间注意力 (FFA-Net 像素注意力、PMDNet 密度估计) 处理; 后者鲜有人做 —— 现有通道注意力只给出一个通道向量, 丢失空间上下文。作者主张 SIM 应通道特异, 并同时建模两种非均匀性。
- **核心矛盾:** 在不增加参数/算力的前提下嵌入梯度先验, 并同时解决图像级与特征级非均匀性。

## 4. 核心贡献
1.  **DEConv:** 并行的香草卷积 + 四种差分卷积 (CDC/ADC/HDC/VDC); 据作者所述首次把差分卷积用于去雾; 经重参数化等价为单个普通卷积, **无额外参数与计算开销**。
2.  **CGA:** 以由粗到精方式生成**通道特异 SIM** 的注意力机制; 用输入特征内容引导, 为每个通道分配独特 SIM, 强调特征中更有用的信息; 作者称其为可插拔的通用基础块。
3.  **CGA-based mixup 融合:** 有效融合编码器低层特征与对应高层特征, 辅助梯度流。
4.  **DEA-Net:** 三者组合的端到端去雾网络, 在多个基准上优于 SOTA, 代表性数字为 SOTS-indoor 上 3.653 M 参数 / PSNR >41 dB。

## 5. 方法详解
### 整体框架
三部分 (编码器 / 特征变换 / 解码器)、三层级的编码器-解码器结构 (Fig.2(a)): level 1&2 用 DEB, level 3 用堆叠 DEAB 学习无雾特征; 经下采样-上采样 U-net 路径与两处 CGA-based Fusion 连接, 把主要卷积计算放在低分辨率空间。

### 输入与输出
- 输入: 雾图 `I ∈ R^{3×H×W}`; 输出: 无雾图 `J ∈ R^{3×H×W}`。

### 关键模块
1.  **DEConv (Fig.3):** 5 路并行 —— VC + CDC + ADC + HDC + VDC。VC 取强度级信息, 差分卷积 (先算像素对差值再卷积) 取梯度级信息。HDC (Fig.4) 计算水平梯度差, 训练后等价重排核权重直接作用于原输入; 等价核**水平权重和为零**, Sobel/Prewitt/Scharr 水平核为其特例; VDC 同理换为垂直方向。各路输出**直接相加**。
2.  **重参数化 (Fig.5, 公式1):** 利用卷积可加性, `F_out = Σ_{i=1..5} F_in*K_i = F_in*(Σ K_i) = F_in*K_cvt` (偏置略)。反向传播时五核独立更新, 前向传播时按位相加成 `K_cvt`; **同时加速训练与测试**, 推理成本等同单个标准卷积。
3.  **CGA (据 Introduction 概述, 详细算子在提取缓存未覆盖页, 待核):** 两步生成通道特异 SIM —— (a) 用 [19] 的空间注意力与 [20] 的通道注意力生成粗 SIM; (b) 依据每个通道内容细化得到最终 SIM, 聚焦各通道独特部分。
4.  **DEB / DEAB (Fig.2(b)(c)):** DEB = 两段 `DEConv->3×3Conv->ReLU` + 跳跃连接; DEAB = DEB 内插入 CGA (含逐元素相乘) 与跳跃连接, 用于 level 3。块内精确算子顺序以原图为准。
5.  **CGA-based mixup 融合 (Fig.2(d)):** 深浅特征因感受野不同, 简单加/拼无法解决感受野不匹配; 用 CGA 从 `F_low` 生成空间权重 `W`, 以 `W`/`1−W` 混合 `F_low` 与 `F_high` 得 `F_fuse`, 增强信息流与梯度回传。

### 训练方式
DEConv 五分支各自按链式法则独立更新。损失函数: 提取缓存 (至第 5 页) 未覆盖实现细节, 原文损失未在提取文本中明示; 去雾常用 L1/L2 重建损失系一般推断, 非原文明示。

### 推理流程
先对所有 DEConv 重参数化合核为 `K_cvt`, 将 DEB/DEAB 简化为标准卷积结构, 再前向得到去雾图。

## 6. 实验与结果
> 提取缓存仅覆盖到第 5 页, **完整实验章节不在提取文本内**。下列数字凡来自摘要/图1的标"(提取支持)", 其余标"(提取缓存未覆盖, 待核)"。
- **数据集:** SOTS-indoor (提取支持, Fig.1)。其他子集/真实雾图 (待核)。
- **对比方法 (提取支持):** FFA-Net(AAAI20)、MSBDN(CVPR20)、AECR-Net(CVPR21)、SGID-PFF(TIP22)、UDN(AAAI22)、PMDNet(ECCV22)、Dehamer(CVPR22); 本文方法含 DEA-Net 与 DEA-Net-CR 变体。
- **指标:** PSNR + 参数量 (提取支持); SSIM 等 (待核)。
- **主结果 (提取支持):** SOTS-indoor 上 3.653 M 参数、PSNR >41 dB, 参数-PSNR 权衡优于 2020 后多个 SOTA。
- **消融 (待核):** 摘要称"extensive experimental results", 具体消融表不在提取文本内。
- **效率 (提取支持):** 重参数化使推理相对香草卷积无额外参数/算力开销, 摘要称推理更快。

## 7. 这篇论文真正有价值的地方
1.  **先验嵌入 + 零开销:** 把梯度先验以差分卷积形式嵌入卷积算子, 再用重参数化抹平多分支的参数/算力代价 —— 一种可迁移到去噪/超分的"重设计卷积核"范式。
2.  **通道特异空间注意力:** CGA 提出"不同通道应有不同空间重要性图", 比统一空间注意力或纯通道注意力更细, 是其作为通用注意力算子的核心卖点。
3.  **训练-推理解耦:** 训练多分支强表达、推理单分支高效率 (思路同 RepVGG), 在轻量化设计中值得借鉴。
4.  **小参数高 PSNR:** 3.653 M / >41 dB 的权衡 (目前仅 SOTS-indoor 由提取文本支持) 印证精心设计模块优于盲目堆深堆宽。

## 8. 局限与问题
1.  仅针对静态单幅图像去雾, 未涉视频/动态场景。
2.  本仓库提取缓存仅到第 5 页, 实验/消融/泛化无法据提取文本核实 (待核)。
3.  方法有效性依赖"梯度先验有助于去雾"的假设; 极均匀雾或极简纹理下 DEConv 差分分支收益可能减弱。
4.  CGA 两步机制较复杂, 其在整网中的算力占比提取文本未给出。
5.  提取文本展示的代表数字集中在 SOTS-indoor, 跨数据集泛化待核。

## 9. 我该怎么使用这篇论文
- **快速了解:** 摘要 + Fig.1 + Fig.2。
- **复现:** 精读 Sec.III, 研究 Fig.2–5 与公式1, 参考官方代码 https://github.com/cecret3350/DEA-Net。
- **借鉴:** DEConv (先验→可学习差分卷积 + 重参数化)、CGA (粗→精的通道特异空间注意力)、CGA-based mixup 融合 (替代简单加/拼)。
- **写 Related Work:** 归入"基于注意力的去雾""先验嵌入的 CNN 设计""网络重参数化/训练-推理解耦"。

## 10. 和其他论文的关系
- **FFA-Net (AAAI 2020) [[FFA-Net]]:** 重要基线与对比对象, 用特征注意力 (像素注意力 + 通道注意力) 处理图像级非均匀性; CGA 针对其通道注意力丢失空间上下文的不足, 改进为通道特异 SIM。
- **AECR-Net (CVPR 2021) [[AECR-Net]]:** 复用 FFA-Net 的特征注意力块并引入对比正则化; 本文对比基线之一。
- **差分卷积谱系 [[CDC]] [[ADC]] [[HDC]] [[VDC]]:** 源自 LBP→LBC→Yu 等的 CDC; 本文沿用 CDC/ADC 并新推导 HDC/VDC, 首次用于去雾。
- **重参数化 [[RepVGG]]:** 论文未直接引用, 但 DEConv 的训练多分支/推理单分支思想与 RepVGG 一脉相承。

## 11. 关键词
图像去雾, 单幅图像, 细节增强卷积 (DEConv), 差分卷积 (CDC/ADC/HDC/VDC), 内容引导注意力 (CGA), 通道特异空间重要性图 (SIM), 重参数化, mixup 融合, 梯度先验, 图像复原, 高效网络设计。

## 12. 可信度说明
本精读基于 `.paper-cache/extracts/CGAFusion.txt`, 该缓存 `max_chars=25000`, **实际只覆盖到原文第 5 页** (摘要、引言、相关工作、方法的 DEConv 与重参数化部分, 至公式1处截断; 文件末尾标注"原文 62262 字符, 只展示前 25000")。因此:
- 摘要、Introduction 的动机/两类问题、贡献三条、DEConv/HDC/VDC/重参数化公式、Fig.1 的数据集 (SOTS-indoor)/对比方法/3.653 M/>41 dB 等, 均能在提取文本找到支撑。
- **CGA 内部算子细节、CGA-based 融合的精确公式、完整实验/消融/泛化、损失函数**等在提取缓存未覆盖, 笔记中相应处已标注"待核/提取文本未明确/据原文后续页未覆盖", 未编造具体数字。

---

> **可信度补充**: PDF 提取质量 = **medium** (提取缓存按 max_chars=25000 截断, 仅覆盖原文约前 5 页, 实验章节未包含); 来源缓存: `.paper-cache/extracts/CGAFusion.txt` (头部标注 12/12 页, 实际文本截断于第 5 页公式1处); 生成日期: 2026-06-05; 复核优化日期: 2026-06-18; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
