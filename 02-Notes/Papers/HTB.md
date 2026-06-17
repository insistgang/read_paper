---
title: Restoring Images in Adverse Weather Conditions
authors:
  - "Shangquan Sun"
  - "Wenqi Ren"
  - "Xinwei Gao"
  - "Rui Wang"
  - "Xiaochun Cao"
year: 2024
venue: "arXiv (ECCV 2024)"
doi: 
pdf: [[HTB.pdf]]
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
extract_cache: .paper-cache/extracts/HTB.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/19 pages"
---
# Restoring Images in Adverse Weather Conditions

## 基本信息
- **PDF**: [[HTB.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Restoring Images in Adverse Weather Conditions via Histogram Transformer |
| **作者** | Shangquan Sun; Wenqi Ren; Xinwei Gao; Rui Wang; Xiaochun Cao |
| **发表时间** | 2024 (arXiv:2407.10172v1, 14 Jul 2024) |
| **刊物/会议** | arXiv (据后续页/外部信息为 ECCV 2024, 提取文本仅标注 arXiv) |
| **DOI** | 未明确（arXiv ID: 2407.10172） |

> 注：作者单位为中科院信工所、中山大学网络科学与技术学院、腾讯微信事业群等；代码已在 GitHub 开源（摘要末句）。

## 摘要

**清理后英文原摘要（据提取文本整理，修复断词与空格）：**

> Transformer-based image restoration methods in adverse weather have achieved significant progress. Most of them use self-attention along the channel dimension or within spatially fixed-range blocks to reduce computational load. However, such a compromise results in limitations in capturing long-range spatial features. Inspired by the observation that the weather-induced degradation factors mainly cause similar occlusion and brightness, in this work, we propose an efficient Histogram Transformer (Histoformer) for restoring images affected by adverse weather. It is powered by a mechanism dubbed histogram self-attention, which sorts and segments spatial features into intensity-based bins. Self-attention is then applied across bins or within each bin to selectively focus on spatial features of dynamic range and process similar degraded pixels of the long range together. To boost histogram self-attention, we present a dynamic-range convolution enabling conventional convolution to conduct operation over similar pixels rather than neighbor pixels. We also observe that the common pixel-wise losses neglect linear association and correlation between output and ground-truth. Thus, we propose to leverage the Pearson correlation coefficient as a loss function to enforce the recovered pixels following the identical order as ground-truth. Extensive experiments demonstrate the efficacy and superiority of our proposed method. We have released the codes in Github.

**中文翻译：**

> 面向恶劣天气的基于 Transformer 的图像复原方法已取得显著进展。其中大多数为降低计算开销，沿通道维度或在空间固定范围块内执行自注意力。然而这种妥协导致难以捕获长距离空间特征。受"天气引起的退化因子主要造成相似的遮挡与亮度"这一观察启发，本文提出一种高效的直方图 Transformer（Histoformer）用于复原受恶劣天气影响的图像。其核心是一种称为"直方图自注意力"的机制：将空间特征排序并按强度分入若干"箱（bin）"，再在箱间或箱内执行自注意力，从而有选择地关注动态范围内的空间特征，并把长距离上退化相似的像素一并处理。为增强直方图自注意力，本文提出动态范围卷积，使常规卷积能够在"相似像素"而非"邻近像素"上进行运算。此外，本文观察到常见的逐像素损失忽略了输出与真值之间的线性关联与相关性，因此提出以皮尔逊相关系数作为损失函数，强制复原像素遵循与真值一致的顺序。大量实验证明了所提方法的有效性与优越性。代码已在 GitHub 开源。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：恶劣天气（雨、雾、雪等）会显著降低视觉质量，影响下游任务（如目标检测 [3,60]、深度估计 [16,18]），因此恶劣天气下的图像复原对视觉美学与安全都至关重要。早期方法依赖天气先验对退化统计特性建模；随后 CNN 在去雨/去雾/去雪上成为主力，但**每个任务需单独训练、多模型切换复杂**，不利于实际部署。Li 等人 [33] 因此提出"单一统一模型去除多种天气退化"的挑战（All-in-One weather removal）。
- **之前方法的问题**：近期基于 Transformer 的统一去除方法虽超越 CNN，但为节省显存，通常把自注意力**限制在固定空间范围内或仅沿通道维度**执行（Figure 1b）。这种妥协违背了 Transformer 本应擅长的全局特征建模能力，进而损害复原性能。
- **核心观察/动机**：作者观察到天气引起的退化往往呈现**相似但区别于背景**的模式（Figure 1a）——退化像素彼此相似、与背景不同。由此提出按强度（descending intensities）把"受天气影响的像素"和"背景像素"分入不同的直方图箱，再在箱内与箱间做自注意力（Figure 1c），从而把空间上分散、退化性质相似的长距离像素关联并一起处理。

## 关键贡献

> 原文（p.3）将贡献明确总结为 **three folds（三点）**，下面按原文三点列出，并补充损失函数细节。

1.  **提出面向统一恶劣天气去除的新型 Transformer，配备新的直方图自注意力**：具备动态范围空间注意力，可全局且高效地去除天气引起的遮挡退化。
2.  **提出双尺度门控前馈模块（DGFF）与相关性损失（correlation loss）**：DGFF 用于捕获多范围信息；相关性损失增强复原图像与真值之间的整体线性关联（基于皮尔逊相关系数 [12]）。
3.  **方法在多个数据集上取得 SOTA**：并验证了对真实世界图像的复原能力，以及对下游检测任务的增益。

> 补充：动态范围卷积（dynamic-range convolution）在原文 Introduction 中作为 DHSA 的组成部分介绍，并非独立列入"三点贡献"，但属于关键技术点（见方法节）。原笔记将贡献拆为 4 点系对原文的重新归并，本次已对齐原文表述。

## 方法

- **整体框架（3.1）**：Histoformer 采用 U-Net 型编码器-解码器结构（Figure 2）。输入低质图像 `I_lq ∈ R^(3×H×W)` 先经 **3×3 卷积**做重叠式块嵌入（patch-embedding）；编码器与解码器各阶段堆叠**直方图 Transformer 块（HTB）**；同阶段编/解码器通过跳跃连接相连以稳定训练；阶段间用 **pixel-unshuffle / pixel-shuffle** 做下/上采样。
- **粗跳连（crude skip-connection）**：编码阶段额外引入一条"粗跳连"补充输入原始特征，由平均池化 + 逐点卷积（1×1）+ 深度卷积 组成；从第一阶段之后开始启用，使编码器更专注于学习天气残差，便于把退化从潜在干净背景中分离。
- **关键模块**：
    1.  **直方图 Transformer 块（HTB）**：核心构建单元，由两部分以层归一化交错组成（公式 1-2）：
        - `F_l = F_{l-1} + DHSA(LN(F_{l-1}))`
        - `F_l = F_l + DGFF(LN(F_l))`
    2.  **动态范围直方图自注意力（DHSA）**：含动态范围卷积 + 双路直方图自注意力，输出投影前会把重排后的特征**排序回原位置**以保持空间一致性。
        - **动态范围卷积（公式 3）**：将输入特征沿通道拆为两支 `F1, F2`；对 `F1` 先水平排序 `Sort_h` 再垂直排序 `Sort_v`，与 `F2` 在通道拼接，再经 1×1 逐点卷积 + 3×3 深度可分离卷积。排序把高/低强度像素分别聚到矩阵对角区域，使卷积可在"动态范围"上计算——退化像素聚到相邻位置、与干净像素分离，让卷积核能分别保留干净信息、复原退化特征。
        - **直方图自注意力（公式 4-5）**：由动态范围卷积输出分出 Value `V ∈ R^(C×H×W)` 与两对 Query-Key `F_{QK,1}, F_{QK,2} ∈ R^(2C×H×W)`。先对 `V` 排序得到索引 `d`，并据 `d` 用 Gather 对 QK 重排（保证 Q/K/V 同序）。给定箱数 `B`，把排序后的 `C×HW` 特征重塑为 `C×B×(HW/B)`，并定义两种重塑：
            - **箱间直方图重塑（BHR）**：箱数 = `B`，每箱含 `HW/B` 个像素 → 每箱跨更大强度范围、含大量动态分布像素，利于**全局/大尺度信息**整合。
            - **频率直方图重塑（FHR）**：每箱频率 = `B`，箱数 = `HW/B` → 每箱仅含少量强度相邻像素，利于**细粒度/局部信息**。
            - 两路分别做自注意力得 `A_B`、`A_F`，逐元素相乘得最终注意力（公式 5）：`A = A_B ⊙ A_F`，`k` 为头数（注意力按 `1/√k` 缩放）。实现时为并行计算令每箱含相同数量像素。
        - **双尺度门控前馈（DGFF）**：在标准前馈网络中集成**两条具有不同尺度的深度卷积路径**（不仅靠增大核尺寸，也借助空洞/膨胀机制 [36,84,85]），以建模多尺度、多范围信息并通过门控融合；针对动态分布退化之间的相关性弥补单尺度前馈的不足。
- **损失函数（相关性损失）**：作者指出常规损失只关注逐像素接近、忽视 patch 级整体相关性，因此引入**皮尔逊相关系数 [12] 作为损失**，强制复原图像与真值之间的线性关系/像素顺序一致（联合常规重建损失训练；逐像素损失具体形式提取文本未逐项列出）。
- **和已有方法的差异**：
    - **vs 通道注意力（如 Restormer）**：本文注意力作用于空间，但通过直方图分组获得动态范围感受野，而非固定通道维度。
    - **vs 窗口注意力（如 Swin-IR）**：不受固定空间窗口约束，而是按像素强度动态分箱，可关联全图任意位置的强度相似像素。
    - **核心差异**：传统注意力作用于固定空间或通道维度，本文作用于**按像素强度动态划分的语义组（bin）**。

## 实验

- **使用的数据集**：去雪 Snow100K-S / Snow100K-L [44]；去雨去雾 Outdoor-Rain [32]；雨滴去除 RainDrop [57]。
- **对比方法**：
    - 任务特定方法：SPANet、JSTASR、RESCAN、DesnowNet、DDMSNet、NAFNet、Restormer（去雪）；CycleGAN、pix2pix、HRGAN、PCNet、MPRNet、NAFNet、Restormer（去雨去雾）；pix2pix、DuRN、RaindropAttn、AttentiveGAN、IDT、MAXIM、Restormer（雨滴）。
    - 统一多天气方法：All-in-One、TransWeather、Chen et al.、WGWSNet、WeatherDiff₆₄/₁₂₈、AWRCP（其中 All-in-One、AWRCP 源码不可得，标 ∗）。
- **评价指标**：PSNR、SSIM（越高越好）。
- **主实验结果（Table 1，p.9）**：
    - **去雪 Snow100K-S**：Histoformer **37.41 / 0.9656**（PSNR、SSIM 均为最佳；第二 AWRCP 36.92 / 0.9652，Restormer 36.01 / 0.9579）。
    - **去雪 Snow100K-L**：Histoformer **32.16 / 0.9261**（PSNR 最佳，超 AWRCP 31.92；但 SSIM 最高者为 AWRCP 0.9341，Histoformer 0.9261 非最佳）。
    - **去雨去雾 Outdoor-Rain**：Histoformer **32.08 / 0.9389**（PSNR、SSIM 均最佳；第二 AWRCP 31.39 / 0.9329）。
    - **雨滴去除 RainDrop**：Histoformer **32.52 / 0.9419**（PSNR、SSIM 最佳，第二 WGWSNet 32.38 / 0.9378）。*（注：Histoformer 在 RainDrop 的具体行落在提取缓存表格截断处——提取文本到 AWRCP "31.93 / 0.9…" 即中断；该 32.52/0.9419 据原笔记/原文表格后续行，提取缓存未覆盖，待核。WGWSNet 32.38/0.9378 行已在提取文本中确认。）*
- **消融实验（Table 2-6，p.13-14，提取缓存仅含线索）**：
    - **自注意力类型（Table 3）**：DHSA 相比 TKSA 提升 **PSNR 0.96 dB**（验证捕获长距离空间特征的价值；TKSA 等通道注意力会损失跨空间长距离信息）。
    - **动态范围卷积（Table 2）**、**箱数 B（Table 4）**、**前馈类型（Table 5）**：DHSA/DGFF 配置在 Outdoor-Rain 上达 32.08/0.9389；增大箱数 B 有相应影响（具体数值提取缓存未完整覆盖）。
    - **前馈（Table 5）**：DGFF 相比 MSFN 提升约 **PSNR 0.3 dB**。
    - **相关性损失（Table 6）**：验证相关性损失 `L_cor` 的有效性（具体增益数值提取缓存未给出）。
- **泛化/真实世界**：作者称验证了对真实世界图像的复原以及对下游检测的增益（Introduction 与后续页，提取缓存未含完整定量表）。

## 局限

- **效率"高效"缺定量支撑（在提取文本内）**：标题与正文强调"efficient"，但提取缓存未含 FLOPs / 参数量 / 推理速度的对照表；排序（Sort_h/Sort_v、Value 排序）与 Gather 操作会引入额外开销，文本未量化（部分效率/复杂度分析可能在提取缓存未覆盖的后续页）。
- **假设的适用边界**：方法依赖"天气退化主要引起相似遮挡与亮度"的假设；对非亮度主导、模式高度多变的复杂退化（特殊光晕、强非均匀雨雾）分箱有效性可能下降。
- **评测以合成数据为主**：主结果在 Snow100K、Outdoor-Rain、RainDrop 等（多为合成）数据集上；真实世界结果以定性展示为主，提取缓存未含系统性大规模真实场景定量评测。
- **复现细节依赖代码**：箱数 `B`、DGFF 膨胀率、头数 `k` 等超参数提取文本未逐一给出，复现需参考官方 GitHub 代码。

## 个人评论

1.  **"按强度分箱"是一个优雅的注意力分组新范式**：打破"空间邻近"或"同通道"的常规分组依据，改为按像素强度（语义近似）动态分组。这与天气退化"强度一致"（雪点偏亮、阴影偏暗）的物理共性高度契合，是领域知识驱动归纳偏置的好例子。
2.  **BHR×FHR 的乘积设计兼顾全局与细粒度**：箱间（大尺度/全局）与箱内（细粒度/局部）两路注意力逐元素相乘，使像素最终权重由"所属箱的重要性"与"箱内重要性"共同决定，思想清晰且可解释。
3.  **排序 + 卷积/注意力是关键的工程巧思**：通过先排序把相似强度像素聚到相邻位置，再让常规卷积/注意力在"相似而非相邻"像素上运算，复用了成熟算子；但排序/Gather 的可微性、稳定性与开销是该范式可迁移性的关键变量，论文层面未充分展开。
4.  **相关性损失补齐了"序"的监督**：以皮尔逊相关系数约束输出-真值的线性关联，对去雨雾这类整体对比度/亮度结构敏感的任务直觉上合理，且 0.3 dB 级别的逐模块增益（DGFF）与 0.96 dB（DHSA vs TKSA）说明各组件并非堆砌。

### 使用建议

- **如果快速了解**：读 Abstract、Introduction 前三段与贡献段、Figure 1/2 图注，以及 3.2 节 DHSA 描述与公式 (3)-(5)。
- **如果复现**：精读 Section 3，尤其 3.2 中 DHSA（动态范围卷积 + BHR/FHR 双路注意力 + 排序回位）与 DGFF；务必参考官方 GitHub 代码获取箱数 B、膨胀率、头数等超参。
- **如果借鉴创新点**：
    1.  借鉴"按属性（强度/边缘/运动）排序 + 分箱"构建动态范围注意力的思路。
    2.  借鉴"双路（大尺度 BHR × 细粒度 FHR）注意力乘积融合"的设计模式。
    3.  借鉴"先分析退化物理共性、再转化为网络归纳偏置"的领域知识驱动方法论。
- **如果写 Related Work**：可归入 **"Transformer-based Image Restoration"** 或 **"All-in-One Weather Removal"**，强调其相对固定窗口/通道注意力 Transformer 的动态范围空间注意力差异。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉**低层视觉 / 图像复原**方向，聚焦**恶劣天气下的统一图像复原**（去雪、去雨、去雾、雨滴去除）。它提出一个能用单一模型处理多种天气退化的方案，核心是一种新的注意力算子——直方图自注意力。鉴于任务本体是"去雨去雾去雪雨滴"的图像复原，本文最贴切的主题是 **"E_图像复原_超分_去噪_去雨去雾"**；其方法贡献又同时是一种注意力模块（与 B_注意力算子模块 强相关），但归类应以任务本体为主。

## 2. 一句话总结
本文提出高效的**直方图 Transformer（Histoformer）**：通过把像素按强度排序并分入若干直方图"箱"，在箱内（细粒度）与箱间（全局）执行自注意力（A = A_B ⊙ A_F），并辅以动态范围卷积与皮尔逊相关性损失，使注意力/卷积都能在"相似而非相邻"的像素上运算，从而高效统一地复原受恶劣天气影响的图像。

## 3. 背景与问题
- **为什么做**：恶劣天气（雨、雾、雪）严重降低图像质量并影响目标检测、深度估计等下游任务；逐任务单独训练 + 多模型切换不利于实际部署，故需统一去除（All-in-One，Li et al. [33]）。
- **之前方法的问题**：基于 Transformer 的统一方法为省显存，把自注意力限制在**固定空间范围**或**仅通道维度**（Figure 1b），削弱了 Transformer 的全局建模能力，损害复原性能。
- **核心观察**：天气退化往往造成**相似的遮挡与亮度**，且与背景区别明显（Figure 1a）。据此把"退化像素"与"背景像素"按强度分箱，在箱内/箱间做注意力（Figure 1c），将空间分散但退化相似的长距离像素关联处理。

## 4. 核心贡献
原文（p.3）将贡献总结为**三点**：
1.  **面向统一恶劣天气去除的新型 Transformer + 直方图自注意力**：赋予自注意力动态范围空间感受野，全局且高效地去除天气遮挡。
2.  **双尺度门控前馈（DGFF）+ 相关性损失**：DGFF 捕获多范围信息；相关性损失（基于皮尔逊相关系数 [12]）增强复原图与真值的整体线性关联。
3.  **多数据集 SOTA**：并验证真实世界图像复原与下游检测增益。

> 关键技术点"动态范围卷积"在引言中作为 DHSA 的组成部分介绍。原笔记把贡献拆成 4 点系重新归并，本次对齐原文"三点"表述。

## 5. 方法详解
- **整体架构（3.1）**：U-Net 型编码器-解码器（Figure 2）。`I_lq ∈ R^(3×H×W)` → 3×3 卷积做重叠块嵌入 → 各阶段堆叠 HTB → 同阶段编/解码器跳跃连接 → 阶段间用 pixel-unshuffle/pixel-shuffle 下/上采样。编码阶段还设"粗跳连"（平均池化 + 1×1 卷积 + 深度卷积，从第一阶段后启用），使编码器更专注学习天气残差、便于分离退化与干净背景。
- **HTB（3.2，公式 1-2）**：`F_l = F_{l-1} + DHSA(LN(F_{l-1}))`；`F_l = F_l + DGFF(LN(F_l))`。
- **动态范围卷积（公式 3）**：`F1, F2 = Split(F)`；`F1 = Sort_v(Sort_h(F1))`；`F = Conv^d_{3×3}(Conv_{1×1}(Concat(F1, F2)))`。排序把高/低强度像素聚到矩阵对角区域，使卷积在动态范围上计算，把退化像素聚到一起、与干净像素分离。
- **直方图自注意力（公式 4-5）**：由动态范围卷积输出得 `V ∈ R^(C×H×W)` 与两对 QK `F_{QK,1}, F_{QK,2} ∈ R^(2C×H×W)`。对 `V` 排序得索引 `d`，用 Gather 按 `d` 重排 QK 保证同序（公式 4）。给定箱数 `B`，把 `C×HW` 重塑为 `C×B×(HW/B)`：
    - **BHR**：箱数 = B，每箱 HW/B 个像素 → 大尺度/全局信息。
    - **FHR**：每箱频率 = B、箱数 = HW/B → 每箱少量强度相邻像素 → 细粒度信息。
    - `A_B = softmax(R_B(Q1)R_B(K1)^T/√k)R_B(V)`；`A_F` 同理用 R_F；**`A = A_B ⊙ A_F`**（公式 5，k 为头数）。最终输出前把特征排序回原位置。实现时每箱含相同像素数以便并行。
- **DGFF**：前馈中集成两条不同尺度的深度卷积路径（结合膨胀机制 [36,84,85]）+ 门控融合，建模多尺度多范围信息，弥补单尺度前馈忽略退化相关性的不足。
- **损失**：常规重建损失 + **皮尔逊相关系数相关性损失** `L_cor`，约束输出-真值线性关联/像素顺序一致（逐像素损失的具体形式提取文本未逐项列出）。

## 6. 实验与结果
- **数据集**：Snow100K-S/L（去雪）、Outdoor-Rain（去雨去雾）、RainDrop（雨滴）。
- **对比**：任务特定方法（DesnowNet/JSTASR/RESCAN/Restormer/NAFNet/MPRNet/IDT/MAXIM 等）与统一方法（All-in-One/TransWeather/Chen et al./WGWSNet/WeatherDiff/AWRCP）。
- **指标**：PSNR / SSIM。
- **主结果（Table 1，p.9）**：
    - Snow100K-S：**37.41 / 0.9656**（PSNR、SSIM 均最佳）。
    - Snow100K-L：**32.16 / 0.9261**（PSNR 最佳；SSIM 最高者为 AWRCP 0.9341，本文非最佳）。
    - Outdoor-Rain：**32.08 / 0.9389**（PSNR、SSIM 均最佳）。
    - RainDrop：**32.52 / 0.9419**（PSNR、SSIM 最佳，第二 WGWSNet 32.38/0.9378）。*RainDrop 的 Histoformer 行落在提取缓存表格截断处（提取到 AWRCP "31.93/0.9…" 即中断），32.52/0.9419 据原文表格后续行，提取缓存未覆盖，待核；WGWSNet 32.38/0.9378 已在提取文本确认。*
- **消融（Table 2-6，p.13-14，提取缓存仅含线索）**：DHSA 相比 TKSA **+0.96 dB PSNR**；DGFF 相比 MSFN 约 **+0.3 dB PSNR**；另有动态范围卷积（Table 2）、箱数 B（Table 4）、前馈类型（Table 5）、相关性损失（Table 6）消融，具体数值提取缓存未完整覆盖。

## 7. 这篇论文真正有价值的地方
1.  **"按强度分箱"的注意力分组新范式**：以像素强度（语义近似）替代"空间邻近/同通道"作为分组依据，与天气退化的强度一致性物理共性契合。
2.  **BHR×FHR 乘积融合**：箱间全局 × 箱内细粒度，权重由"所属箱重要性 × 箱内重要性"共同决定，清晰可解释。
3.  **排序 + 成熟算子的工程巧思**：把"相似像素"重排为"相邻"，让常规卷积/注意力直接适用，复用成熟实现。
4.  **相关性损失补"序"的监督**：皮尔逊相关系数约束输出-真值线性关联，逐模块消融（0.3/0.96 dB）说明组件有效而非堆砌。

## 8. 局限与问题
- **"efficient"缺定量支撑**：提取缓存未含 FLOPs/参数量/速度对照表；排序与 Gather 引入开销未量化（可能在未覆盖页）。
- **假设适用边界**：依赖"退化≈相似遮挡与亮度"假设，对非亮度主导/模式多变退化分箱可能失效。
- **以合成数据为主**：主结果多为合成集，真实世界以定性为主，缺系统性大规模定量评测（在提取范围内）。
- **复现依赖代码**：箱数 B、膨胀率、头数等超参文本未逐一给出。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract、Introduction、Figure 1/2 图注、3.2 节与公式 (3)-(5)。
- **复现**：精读 Section 3（DHSA 的动态范围卷积 + BHR/FHR + 排序回位、DGFF），参考官方 GitHub 代码补超参。
- **借鉴**：① 按属性排序+分箱构建动态范围注意力；② 双路（大尺度×细粒度）注意力乘积融合；③ 退化物理共性→网络归纳偏置的方法论。
- **写 Related Work**：归入 Transformer-based Image Restoration / All-in-One Weather Removal，强调动态范围空间注意力的差异。

## 10. 和其他论文的关系
本论文的对比/参考工作（据提取文本 Related Work 与 Table 1）：
- **Restormer**：通道（转置）注意力的高效复原 Transformer，是主要对比基线，也是 DHSA 对照的"通道注意力（TKSA/MDTA 类）"代表。
- **Swin-IR**：基于 Swin 窗口注意力的图像复原 Transformer，是"固定窗口注意力"的对照。
- **U-former**：基于 U-Net 的复原 Transformer 架构。
- **TransWeather**、**WGWSNet**、**AWRCP**、**WeatherDiff**：统一恶劣天气去除的代表性对比方法。
- **ViT**：视觉 Transformer 的奠基工作。
- 任务特定基线：DesnowNet/JSTASR/DDMSNet（去雪）、HRGAN/MPRNet（去雨去雾）、AttentiveGAN/IDT/MAXIM（雨滴）。

## 11. 关键词
图像复原, 恶劣天气去除, 统一去除(All-in-One), 直方图自注意力, 动态范围注意力/卷积, BHR/FHR, Transformer, 去雪, 去雨, 去雾, 雨滴去除, 皮尔逊相关性损失, Histoformer

## 12. 可信度说明
本篇精读主要基于提取缓存（详写覆盖 p.1-9，含 Abstract、Introduction、Related Work、Method 3.1-3.2、Table 1）生成，来源包括：
- **标题、作者、单位、摘要** (p.1)
- **Figure 1/2 说明与 Introduction 动机/贡献** (p.2-5)
- **Method 整体架构与 DHSA/DGFF 公式 (1)-(5)** (p.5-8)
- **Table 1 主实验结果** (p.9)
- **消融线索（Table 2-6）** 来自补读记录的 p.13-14 摘录（DHSA vs TKSA +0.96 dB、DGFF vs MSFN +0.3 dB）

**提取质量评估**：提取缓存清晰覆盖核心思想、方法框架与主实验，但 **Table 1(c) RainDrop 的 Histoformer 行在缓存中截断**（32.52/0.9419 待核），消融表的完整数值、训练细节与真实世界定量评测在缓存中缺失或仅有线索。除上述标注"待核"项外，笔记数字均直接来自给定文本段落。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/HTB.txt` (头部标注 12/19 页, 详细文本覆盖 p.1-9; 补读记录补足 p.13-19 线索); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本次复读据提取文本核对并修正了贡献点数(4→对齐原文3点)、补全公式(3)-(5)与消融线索、标注 RainDrop 行截断、并将 primary_topic 由 B_注意力算子模块 修正为 E_图像复原_超分_去噪_去雨去雾。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-19; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-19。
- **提取情况**: 缺失页 7 页, 其中 7 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Restoring Images in Adverse Weather Conditions via Histogram Transformer 13
- p.13: Table 3: Ablation studies on the design
- p.13: SA type PSNR SSIM
- p.13: 44 Out of memory
- p.13: Table 5: Ablation studies on the choice
- p.13: Feed-Forward PSNR SSIM
- p.13: Both MDTA and TKSA integrate rich information across channels, which
- p.14: Show JSON
- p.14: FacesObjects
- p.14: Labels
- p.14: Proper ties
- p.14: Safe Sear ch

### 缺失页关键摘录

- p.13: Table 2: Ablation studies on the dynamic-range convolution.
- p.13: DHSA 32.08 0.9389Table 4: Ablation studies on the number
- p.13: DGFF 32.08 0.9389Table 6: Ablation studies on the setting
- p.13: branch. The quantitative analysis results are presented in Table 3.
- p.13: may result in a loss of the exploitation of long-range information across spatial
- p.13: extracting long-range spatial features, our DHSA enhances performance, result-
- p.13: ing in a PSNR improvement of 0.96 dB compared to TKSA.
- p.13: sults are presented in Table 4. It is observed that increasing the number of bins
- p.14: The quantitative analysis results are presented in Table 5. While MSFN inte-
- p.14: resulting in a PSNR gain of 0.3 dB over MSFN.
- p.14: Correlation Loss. Table 6 shows the effectiveness of the correlation loss Lcor
- p.18: single-image deraining with a high quality real rain dataset. In: CVPR (2019)
<!-- AI_READING_NOTE_END -->
