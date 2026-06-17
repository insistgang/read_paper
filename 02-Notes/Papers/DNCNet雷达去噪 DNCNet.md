---
title: "DNCNet: Deep Radar Signal Denoising and Recognition"
authors:
  - "Mingyang Du"
  - "Ping Zhong"
  - "Xiaohao Cai"
  - "Daping Bi"
year: 2022
venue: "IEEE Transactions on Aerospace and Electronic Systems (TAES), Vol. 58, No. 4"
doi: 10.1109/TAES.2022.3153756
pdf: [[DNCNet雷达去噪 DNCNet.pdf]]
primary_topic: N_雷达_无线电_张量_数学
topics:
  - "N_雷达_无线电_张量_数学"
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
extract_cache: .paper-cache/extracts/DNCNet雷达去噪 DNCNet.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/14 pages"
---
# DNCNet: Deep Radar Signal Denoising and Recognition

## 基本信息
- **PDF**: [[DNCNet雷达去噪 DNCNet.pdf]]
- **primary_topic**: `N_雷达_无线电_张量_数学`
- **topics**: `N_雷达_无线电_张量_数学`, `E_图像复原_超分_去噪_去雨去雾`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | DNCNet: Deep Radar Signal Denoising and Recognition |
| **作者** | Mingyang Du; Ping Zhong; Xiaohao Cai; Daping Bi |
| **单位** | 国防科技大学 (合肥/长沙) + 南安普顿大学 |
| **发表时间** | 2022 (收稿 2021-08-27, 见刊 2022-08) |
| **刊物/会议** | IEEE Transactions on Aerospace and Electronic Systems (TAES), Vol. 58, No. 4 |
| **DOI** | 10.1109/TAES.2022.3153756 |
| **资助** | 国家自然科学基金 (Grant 61971428) |

## 摘要

**英文原文 (据 PDF 提取文本整理, 已修复空格与连字符断裂):**

> Deep learning with its rapid development and advancement has achieved unparalleled performance in many areas like computer vision as well as cognitive radio and signal recognition. However, the performance of most deep neural networks would suffer from degradation in the data mismatch scenario, e.g., the test dataset has a related but nonidentical distribution with the training dataset. Considering the noise corruption, a classifier's accuracy might drop sharply when it is tested on a dataset with much lower signal-to-noise ratio compared to its training dataset. To address this dilemma, in this work, we propose an efficient denoising and classification network (DNCNet) for radar signals. The DNCNet consists of denoising and classification subnetworks. First, a radar signal detection and synthetic mechanism is designed to generate pairwise clean data and noisy data for the DNCNet to train its denoising subnetwork. Then, a two-phase training procedure is proposed to train the denoising subnetwork in the first phase and strengthen the mapping between the denoising results and perceptual representation in the second. Experiments on synthetic and benchmark datasets validate the excellent performance of the proposed DNCNet against state-of-the-art methods in terms of both signal restoration quality and classification accuracy.

**中文翻译:**

> 深度学习凭借其快速发展, 已在计算机视觉以及认知无线电、信号识别等众多领域取得了无与伦比的性能。然而, 在数据不匹配场景下 (例如测试集与训练集分布相关但不相同), 大多数深度神经网络的性能会出现退化。考虑到噪声污染, 当分类器在信噪比远低于训练集的数据上测试时, 其准确率可能急剧下降。为解决这一困境, 本文提出了一种面向雷达信号的高效去噪与分类网络 (DNCNet)。DNCNet 由去噪子网络和分类子网络构成。首先, 设计了一套雷达信号检测与合成机制, 用于生成成对的纯净数据与带噪数据, 以训练 DNCNet 的去噪子网络; 随后, 提出两阶段训练流程: 第一阶段训练去噪子网络, 第二阶段强化去噪结果与 (分类器) 感知表征之间的映射。在合成数据集和基准数据集上的实验表明, 所提 DNCNet 在信号恢复质量与分类准确率两方面均优于当前最先进方法。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：在拥挤、复杂的电磁环境中即时识别并标注感兴趣的无线电频谱, 是频谱监测、辐射源识别、移动发射机跟踪、认知无线电/雷达等任务的关键。本文聚焦雷达信号识别, 而当数据高度含噪、且训练集与测试集分布不一致时, 该任务极具挑战。战场环境中的环境噪声、有意干扰等会破坏信号质量、降低信噪比 (SNR), 使截获信号分布与训练集不同; 数值实验显示, 在高 SNR 上训练的普通 CNN 分类器在低 SNR 测试时准确率会骤降。
- **之前方法的问题**：
    1.  **传统手工特征方法**：基于专家知识的特征提取器 (如基于 Wigner 与 Choi–Williams 时频分布、短时傅里叶变换), 虽能在频谱域拉开不同信号/辐射源的距离, 但缺乏自动化与泛化能力。
    2.  **基于时频图像的深度学习方法 (文献 [6]–[8])**：先把原始时序信号经时频分析转成 2D 图像再喂给 DNN。缺点: 相比原始时序数据会丢失幅度信息; 与端到端趋势不符; 把所有样本转成时频图像耗时、增加计算负担。
    3.  **直接用原始时序信号的深度学习方法 (文献 [9]–[11])**：将复数输入的实/虚部构成 2×N 向量送入窄 2D CNN, 证明了 CNN 对无线电信号高层表征的有效性。但当测试集分布与训练集不同时, 预训练 DNN 性能仍会退化。此外, 文献中关于基于 DNN 的信号去噪研究稀缺 (而图像去噪已蓬勃发展)。
- **核心矛盾 (data mismatch)**：训练集与实测数据在噪声水平/特性上的分布差异, 与期望分类器在恶劣条件下保持高精度之间的矛盾。本文借鉴"分而治之"思想 (文献 [13]): 先用去噪模型恢复信号, 再用另一分类器识别, 让去噪模型保证对宽 SNR 范围带噪信号的鲁棒性, 从而维持预训练分类器在测试集上的高准确率。

## 关键贡献

论文明确列出三点主贡献:

1.  **雷达信号检测与合成机制**：依据截获信号与现有威胁数据库构建数据集。考虑到基于模型的去噪技术天然需要成对的纯净/带噪数据, 设计了包含信号接收单元 (解交织 + 参数估计 + 标注) 与信号合成单元 (信号生成器据参数估计与电子情报生成同类别的无噪纯净信号) 的雷达系统, 自动产出一一对应的"带噪真实信号—纯净合成信号"配对数据集。
2.  **2D→1D 去噪模型 + DNCNet + 两阶段训练**：将 2D 图像去噪模型适配为 1D 以处理雷达信号恢复, 提出去噪与分类网络 (DNCNet) 及两阶段训练流程, 增强去噪结果与分类器感知表征之间的映射, 进一步提升分类准确率。
3.  **更贴近现实的噪声验证**：除文献中广泛使用的加性高斯白噪声 (AWGN) 外, 额外采用**高斯色噪声**和**脉冲噪声**, 使实验设置更接近信道与环境中实际接收到的噪声, 增强验证与对比的说服力。

## 方法

- **整体框架 (Fig. 2)**：DNCNet 含两个子模型——去噪模型 (cyan) 与分类模型——通过两阶段训练。把去噪 (低层) 任务与高层视觉 (识别) 任务统一在一个框架中, 通过联合优化两个损失同时完成。动机部分源于真实军事背景: 信号恢复只是中间过程, 辐射源识别结果才是指挥员真正关心的高价值信息。
- **输入表示**：复数 (I/Q) 输入的实/虚部分置于两个维度, 构成 2×N 向量 (N 为信号长度); 子网络中的卷积、池化操作全部适配为 1D 以处理时序信号。
- **关键模块详解**：
    1.  **噪声水平估计子网络 (Fig. 3)**：一个 5 层、无池化的 1D 全卷积网络 (FCN)。输入带噪信号 `(64, 2, N)`, 输出与输入同维度的噪声水平图 `ε` (`64×2×N`)。中间卷积层输出通道为 32、最后一层为 2, 卷积核大小为 3, 每个卷积层做 zero-padding 以保持维度。输出与原始输入在通道维拼接成 `64×4×N` 张量, 送入后续 U-Net。噪声水平图 `ε` 概念来自 FFDNet [16], 其所有元素由噪声方差 σ 拉伸 (最初形式为 σ 填满的 2×N 矩阵), 作为正则项让去噪在"降噪"与"保真"间权衡。`ε` 估计采用文献 [19] 提出的非对称损失。
    2.  **U-Net 去噪子网络 (Fig. 4)**：对称的下采样—上采样结构, 利用多尺度信息并逐步扩大感受野。下采样 = 1D 卷积 + 平均池化 (视为特征提取器), 上采样 = 1D 转置卷积 + 填充 (据高层特征重构信息), 去除随机噪声扰动。**共 16 层**, 所有卷积核大小为 3; 除最后一层外每个卷积层后接 ReLU; 各下采样操作的输出通道依次为 **64、128、256**。
    3.  **分类模型 (ResNet18-1D)**：以 ResNet18 [31] 为基础, 将卷积层与平均池化层适配为 1D 以处理 2×N 信号; 并把原始 ResNet18 顶部的 7×7 卷积层与最大池化层替换为单个 3×3 卷积 (提取文本在此处截断)。
- **去噪映射建模**：`ŷ = F(x+n, Θ)`, 引入噪声水平图后改写为 `ŷ = F(x+n, ε, Θ)`, 其中 Θ 为去噪模型可训练参数, ε 为噪声水平图。
- **两阶段训练**：
    1.  **第一阶段 (联合训练)**：级联去噪模型与分类模型, 用**联合损失** = 去噪重建损失 + 分类损失, 共同更新去噪模型参数 (Fig. 2 上图)。联合损失让去噪模型产出对分类有利、感知质量高且语义忠实的结果。
    2.  **第二阶段 (重训练)**：固定已训练好的去噪模型, **仅优化分类模型**参数 (Fig. 2 下图), 强化去噪结果与分类器感知表征的对齐。
- **与已有方法差异**：相对纯分类网络 ([6]–[8]) 增加了去噪前置阶段; 相对图像去噪模型 (U-Net [14]、残差学习 DnCNN [15]、引入噪声水平估计的 FFDNet [16]、面向真实噪声的 [17]) 将 2D 架构适配为 1D 并整合分类联合优化; 相对结合去噪与高层视觉任务的 [18], 本文系统化地应用于 1D 雷达信号并提出具体两阶段训练策略。

## 实验

> 注: 提取缓存覆盖 p.1–12, 在第 IV.B 节分类模型处截断 (Section V 实验主体未进入提取文本)。以下数据集名称据 p.13 的缺失页摘录补充。

- **数据集 (据原文后续页 p.13, 提取缓存未覆盖正文叙述, 待核)**：**SIGNAL-8** 数据集 (8 类) 与 **RADIOML 2018.01A** 数据集 (24 类)。前者应为论文用第三节合成机制生成的合成数据集, 后者为公开基准数据集 (摘要所称 "synthetic and benchmark datasets")。
- **对比方法 (据 p.13 缺失页摘录, 待核)**：包括 **DnCNN-1D** 与 **FFDNet-1D** 等去噪基线 (即把经典图像去噪网络同样适配为 1D)。Table II 还汇总了相关去噪方法的主要属性对比。
- **评价指标**：信号恢复质量 + 分类准确率 (摘要明确两者)。
- **主实验结论**：摘要称所提 DNCNet 在信号恢复质量与分类准确率两方面均优于 SOTA。具体对比数字未进入提取文本, **PDF 文本 (提取部分) 未明确**。
- **噪声类型实验**：在三种噪声下验证——AWGN、高斯色噪声、脉冲噪声 (用 Alpha 稳定分布 S(α,β,γ,δ) 建模, 其中 α 为特征指数刻画尾部、β 为偏度、γ 为尺度、δ 为位置)。
- **消融实验**：提取文本未给出具体消融模块结果, **PDF 文本 (提取部分) 未明确**。
- **效率信息**：参数量/FLOPs/推理速度等, 提取文本未提及。

## 局限

1.  **强依赖参数估计精度**：合成"纯净"信号依赖信号接收单元的参数估计精度——论文明确指出该精度直接影响合成信号特征, 精度低会导致配对数据对齐差、进而损害去噪性能。论文也辩护称现有技术可较好管理该精度 (引文献 [29][30]: SNR 5–25 dB 时时间参数/脉冲幅度估计标准差可低于 0.2; 0 dB 低 SNR 下瞬时相位/频率/幅度估计标准差可低于 0.1)。
2.  **噪声类型假设的局限**：仅验证 AWGN/高斯色噪声/脉冲噪声三类, 真实电磁环境中的非平稳噪声、特定干扰更复杂, 对完全未知噪声的泛化尚不明确。
3.  **信号类型先验假设**：流程假设威胁数据库中已有目标信号的类型与参数 (才能用信号合成器生成对应纯净信号), 对数据库中没有的全新信号类型可能无法直接应用。
4.  **计算成本未讨论**：U-Net 与 ResNet18 级联、加两阶段训练, 其复杂度与训练时间代价未分析 (基于提取部分判断)。
5.  **实验细节受提取截断影响**：完整实验结果、数据集规模/信号类型细节、详细消融分析未进入提取文本, 对方法优势的评判受限 (此为提取缓存的限制, 非论文本身缺陷)。

## 个人评论

1.  **"分而治之"的系统化落地**：把"信号恢复"预处理与"信号识别"高层任务解耦, 再以联合训练 + 阶段化优化有机结合, 为解决噪声层面的 data mismatch 提供了清晰范式。本质上是用一个对宽 SNR 鲁棒的去噪前端, 把测试分布"拉回"分类器熟悉的高 SNR 域。
2.  **跨域迁移的工程细致度**：没有照搬 2D 图像网络, 而是把 FFDNet 的噪声水平图、U-Net 编解码、ResNet18 骨干逐一改造为 1D, 并从军事威胁数据库的应用背景出发设计配对数据合成流程, 体现了问题导向的工程思维。把图像去噪三件套 (U-Net/DnCNN/FFDNet) 系统性 1D 化并作为基线对比, 是这条线的合理实验设计。
3.  **联合损失 + 两阶段训练的价值**：第一阶段联合损失让去噪在重建时就偏向"利于分类的感知特征", 第二阶段冻结去噪、微调分类器进一步对齐, 比简单级联预训练模型更利于下游识别。
4.  **面向真实场景的噪声设计**：引入高斯色噪声与 Alpha 稳定分布脉冲噪声, 比清一色 AWGN 更贴近实际信道, 对后续研究的实验设计有参考价值。

### 使用建议

- **快速了解**：读摘要、引言 (I) 与结论 (VI), 掌握动机、DNCNet 两阶段框架与主要结论。
- **复现重点**：精读第 III 节 (信号检测与合成机制) 与第 IV 节 (DNCNet), 特别是 Fig. 1–4, 以及网络结构 (噪声估计 FCN 通道 32/2、核 3; U-Net 16 层、通道 64/128/256)、联合损失、两阶段训练流程。注意 2D→1D 的具体适配。
- **借鉴创新点**：高层任务与底层恢复联合优化的思路; 领域专用配对数据合成流程; 噪声水平估计子网络与主干的集成方式。
- **写 Related Work**：可放入 1) 信号去噪 2) 雷达信号识别/分类 3) 基于深度学习的信号处理 4) 图像/信号恢复与高层视觉任务结合 这几类。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[N_雷达_无线电_张量_数学]]
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**雷达/无线电信号处理与深度学习交叉领域**, 聚焦**雷达信号的去噪与识别 (recognition)**。它解决的核心问题是: 在低信噪比、且训练—测试分布不匹配 (data mismatch, 尤其噪声水平不同) 条件下, 雷达信号分类器准确率急剧下降。方法上借鉴了图像去噪的 U-Net / FFDNet / DnCNN 思想并 1D 化, 但落脚点是 1D 时序雷达信号与辐射源识别, 发表于 IEEE TAES (航空航天与电子系统), 因此主题归入 **N_雷达_无线电_张量_数学** 更准确; 其图像去噪方法迁移的一面与 **E_图像复原_超分_去噪_去雨去雾** 关联。

## 2. 一句话总结
本文提出 DNCNet——由 1D 去噪子网络 (噪声水平估计 FCN + U-Net) 与分类子网络 (ResNet18-1D) 构成的级联框架, 配合雷达信号检测与合成机制产出配对训练数据, 并用两阶段训练 (先联合训练去噪、后冻结去噪微调分类) 强化去噪结果与分类器感知表征的映射, 从而在 AWGN/色噪声/脉冲噪声等多种环境下同时提升雷达信号的恢复质量与分类准确率。

## 3. 背景与问题
- **为什么做**：拥挤电磁环境中即时识别感兴趣频谱是频谱监测、辐射源识别、跟踪、认知无线电/雷达的关键。战场噪声、有意干扰会降低 SNR, 使截获信号分布偏离训练集; 数值实验表明高 SNR 训练的普通 CNN 在低 SNR 测试时准确率骤降。
- **之前方法的问题**：
    1.  **手工特征** (Wigner/Choi–Williams 时频分布、STFT): 缺乏自动化与泛化。
    2.  **时频图像法 [6]–[8]**: 丢失幅度信息、非端到端、转换耗时。
    3.  **原始时序法 [9]–[11]**: 有效但仍受分布不匹配退化; 且基于 DNN 的信号去噪研究稀缺。
- **核心矛盾**：噪声层面的 data mismatch vs. 期望分类器在恶劣条件下高精度。解法是"分而治之" [13]: 去噪前端 + 分类后端。

## 4. 核心贡献
1.  **雷达信号检测与合成机制**: 据截获信号 + 威胁数据库, 用信号接收单元 (解交织 + 参数估计 + 标注) 与信号合成单元 (生成器据参数生成同类别无噪信号) 构造一一对应的"带噪真实—纯净合成"配对数据集, 满足基于模型去噪对配对数据的需求。
2.  **2D→1D 去噪 + DNCNet + 两阶段训练**: 将图像去噪模型适配为 1D, 提出 DNCNet 与两阶段训练, 增强去噪结果与分类器感知表征的映射、提升分类精度。
3.  **更贴近现实的噪声验证**: 在 AWGN 之外引入高斯色噪声与脉冲噪声 (Alpha 稳定分布), 贴近真实信道环境。

## 5. 方法详解
- **整体框架 (Fig. 2)**: 去噪模型 + 分类模型两子网, 两阶段训练; 低层去噪与高层识别在单一框架内联合优化。动机: 信号恢复是中间过程, 辐射源识别才是指挥员的高价值信息。
- **输入表示**: 复数 I/Q 的实/虚部分置两维构成 2×N 向量; 卷积/池化全部 1D 化。
- **噪声水平估计子网络 (Fig. 3)**: 5 层无池化 1D-FCN, 输入 `(64,2,N)`、输出同维噪声水平图 ε `(64,2,N)`; 中间卷积层 32 通道、末层 2 通道、核 3、各层 zero-padding; 输出与原输入拼成 `64×4×N` 送入 U-Net。ε 源自 FFDNet [16] (元素由噪声方差 σ 拉伸), 作正则项平衡降噪与保真; 用文献 [19] 非对称损失估计。
- **U-Net 去噪子网络 (Fig. 4)**: 对称下/上采样, 共 16 层、核 3, 除末层外每卷积后接 ReLU; 下采样 = 1D 卷积 + 平均池化, 上采样 = 1D 转置卷积 + 填充; 下采样输出通道 64/128/256。
- **分类模型 (ResNet18-1D)**: ResNet18 卷积/平均池化适配 1D, 顶部 7×7 卷积 + 最大池化换成单个 3×3 卷积 (提取文本此处截断)。
- **去噪映射**: `ŷ = F(x+n, ε, Θ)`。
- **两阶段训练**: ① 级联两模型, 联合损失 = 重建损失 + 分类损失, 共同更新去噪模型; ② 冻结去噪模型, 仅优化分类模型。
- **与已有方法差异**: vs 纯分类网 [6]–[8] 加去噪前置; vs 图像去噪 ([14] U-Net、[15] DnCNN 残差学习、[16] FFDNet 噪声水平估计、[17] 真实噪声) 改 1D 且整合分类联合优化; vs [18] 结合去噪与高层视觉, 本文系统化于 1D 雷达信号并给出两阶段策略。

## 6. 实验与结果
> 提取缓存止于第 IV.B 节, Section V 实验主体未进入提取文本; 数据集/基线据 p.13 缺失页摘录补充, 标注待核。
- **数据集 (据 p.13, 待核)**: SIGNAL-8 (8 类合成数据集) 与 RADIOML 2018.01A (24 类公开基准)。
- **对比方法 (据 p.13, 待核)**: DnCNN-1D、FFDNet-1D 等 1D 化去噪基线; Table II 汇总相关去噪方法属性。
- **评价指标**: 信号恢复质量 + 分类准确率。
- **主结论**: 摘要称 DNCNet 在两项指标上均优于 SOTA; 具体数字 PDF 提取部分未明确。
- **噪声类型实验**: AWGN / 高斯色噪声 / 脉冲噪声 (Alpha 稳定分布) 三种。
- **消融/效率**: 提取文本未提供具体结果与参数量/FLOPs/速度。

## 7. 这篇论文真正有价值的地方
1.  **"分而治之"系统化**: 用对宽 SNR 鲁棒的去噪前端把测试分布拉回分类器熟悉域, 为噪声型 data mismatch 提供清晰范式。
2.  **跨域迁移工程细致度**: 噪声水平图、U-Net、ResNet18 逐一 1D 化, 并据军事威胁数据库背景设计配对数据合成流程。
3.  **联合损失 + 两阶段训练**: 联合损失让去噪偏向利于分类的感知特征, 冻结去噪后微调分类器进一步对齐, 优于简单级联预训练。
4.  **真实噪声设计**: 色噪声 + 脉冲噪声贴近实际信道, 对实验设计有参考价值。

## 8. 局限与问题
1.  **依赖参数估计精度**: 合成纯净信号取决于接收单元参数估计精度, 精度低会致配对数据对齐差、损害去噪 (论文以 [29][30] 辩护可控)。
2.  **噪声类型假设局限**: 仅三类噪声, 对未知/非平稳噪声泛化未知。
3.  **信号类型先验**: 假设威胁数据库已有目标信号类型才能合成纯净信号, 全新类型难直接应用。
4.  **计算成本未讨论**: 级联 + 两阶段训练的复杂度未分析 (基于提取部分)。
5.  **实验细节受提取截断**: 完整结果/数据集规模/消融未进入提取文本 (提取缓存限制, 非论文缺陷)。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言 (I) + 结论 (VI)。
- **复现重点**: 第 III、IV 节与 Fig. 1–4; 网络结构 (噪声估计 FCN 通道 32/2 核 3; U-Net 16 层通道 64/128/256)、联合损失、两阶段训练; 注意 2D→1D 适配。
- **借鉴创新点**: 高层 + 底层任务联合优化; 领域专用配对数据合成; 噪声水平估计子网络与主干集成。
- **写 Related Work**: 信号去噪 / 雷达信号识别 / DL 信号处理 / 恢复与高层视觉结合。

## 10. 和其他论文的关系
- **图像去噪骨架 (被 1D 化迁移)**: `[[U-Net]]` (文献 [14])、`[[DnCNN]]` (残差学习 [15])、`[[FFDNet]]` (噪声水平估计子网 [16]) ——本文的噪声水平图与 U-Net 编解码直接来自这条线, 实验基线 DnCNN-1D / FFDNet-1D 也由此而来。
- **去噪结合高层视觉任务**: 文献 [18] 用语义指导提升去噪感知质量, 是本文联合优化思想的来源。
- **雷达/无线电信号识别**: 时频图像法 [6]–[8]、原始时序法 [9]–[11] 是直接对比对象。
- **分类骨干**: `[[ResNet18]]` (文献 [31]) 适配为 ResNet18-1D。
*(注: 库内其他论文具体信息未知, 关联依本文引用与主题推断。)*

## 11. 关键词
雷达信号识别, 深度学习, 信号去噪, data mismatch (分布不匹配), U-Net, FFDNet, DnCNN, ResNet18-1D, 噪声水平估计, 联合损失, 两阶段训练, AWGN, 高斯色噪声, 脉冲噪声 (Alpha 稳定分布), 电磁环境, 辐射源识别

## 12. 可信度说明
本篇精读笔记**严格基于 PDF 提取文本 (覆盖 p.1–12, 在第 IV.B 节分类模型处截断) 生成**, 主要依据**摘要、引言 (I)、雷达信号与噪声模型 (II)、信号检测与合成机制 (III)、去噪与分类框架 (IV)** 的详细描述, 提取质量良好、核心方法描述清晰。**数据集名称 (SIGNAL-8 / RADIOML 2018.01A) 与基线 (DnCNN-1D / FFDNet-1D) 据 p.13 缺失页摘录补充, 已标注"待核"**。**具体实验数字、完整消融、效率信息**因提取截断于第 V 节之前而无法给出, 已在相应位置标注"PDF 文本未明确"。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (约 2086 字符/页)); 来源缓存: `.paper-cache/extracts/DNCNet雷达去噪 DNCNet.txt` (提取覆盖 p.1–12/14; 原 AI 主体 12 页 + 全文补读 13–14 缺失页摘录); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-14; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-14。
- **提取情况**: 缺失页 2 页, 其中 2 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: APPENDIX
- p.13: method, and the classiﬁers DnCNN-1D and FFDNet-1D
- p.13: REFERENCES
- p.13: Radar emitter recognition based on sift position and scale fea-
- p.13: Automatic radar waveform recognition
- p.13: Digital channelized receiver based on time-frequency analysis
- p.13: Experimental evaluation, lessons learned, and challenges
- p.13: Wireless networks design in the era of deep learning: Model-
- p.13: Automatic radar waveform recognition based on time-
- p.14: Automatic LPI radar waveform recognition using CNN
- p.14: Convolutional radio modulation recognition networks
- p.14: An introduction to deep learning for the physical layer

### 缺失页关键摘录

- p.13: for the SIGNAL-8 dataset and 24 for the RADIOML 2018.01 A dataset. The ReLU activations in ResNet18-1D are not shown in this ﬁgure for
- p.13: Experimental evaluation, lessons learned, and challenges
- p.14: Estimation of accuracy of algorithm for measuring radiofre-
- p.14: High accuracy parameter estimation for advanced radar identi-
<!-- AI_READING_NOTE_END -->
