---
title: "Haar wavelet downsampling: A simple but effective downsampling module for semantic segmentation"
authors:
  - "Guoping Xu"
  - "Wentao Liao"
  - "Xuan Zhang"
  - "Chang Li"
  - "Xinwei He"
  - "Xinglong Wu"
year: 2023
venue: Pattern Recognition
doi: 10.1016/j.patcog.2023.109819
pdf: [[HWD下采样.pdf]]
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
extract_cache: .paper-cache/extracts/HWD下采样.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/14 pages"
---
# Haar wavelet downsampling: A simple but effective downsampling module for semantic segmentation

## 基本信息
- **PDF**: [[HWD下采样.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Haar wavelet downsampling: A simple but effective downsampling module for semantic segmentation |
| **作者** | Guoping Xu; Wentao Liao; Xuan Zhang; Chang Li; Xinwei He; Xinglong Wu（通讯，xwu@wit.edu.cn） |
| **单位** | 武汉工程大学计算机科学与工程学院（湖北智能机器人重点实验室）；合肥工业大学生物医学工程系；华中科技大学电子信息与通信学院 |
| **发表时间** | 2023（在线 2023-07-13；收稿 2022-08-04，修回 2023-06-15，录用 2023-07-12） |
| **刊物/会议** | Pattern Recognition 143 (2023) 109819 |
| **DOI** | 10.1016/j.patcog.2023.109819 |
| **代码** | https://github.com/apple1986/HWD |

## 摘要

**英文原文（据 PDF 提取文本整理，已修复断字与空格）：**

> Downsampling operations such as max pooling or strided convolution are ubiquitously utilized in Convolutional Neural Networks (CNNs) to aggregate local features, enlarge receptive field, and minimize computational overhead. However, for a semantic segmentation task, pooling features over the local neighbourhood may result in the loss of important spatial information, which is conducive for pixel-wise predictions. To address this issue, we introduce a simple yet effective pooling operation called the Haar Wavelet-based Downsampling (HWD) module. This module can be easily integrated into CNNs to enhance the performance of semantic segmentation models. The core idea of HWD is to apply Haar wavelet transform for reducing the spatial resolution of feature maps while preserving as much information as possible. Furthermore, to investigate the benefits of HWD, we propose a novel metric, named as feature entropy index (FEI), which measures the degree of information uncertainty after downsampling in CNNs. Specifically, the FEI can be used to indicate the ability of downsampling methods to preserve essential information in semantic segmentation. Our comprehensive experiments demonstrate that the proposed HWD module could (1) effectively improve the segmentation performance across different modality image datasets with various CNN architectures, and (2) efficiently reduce information uncertainty compared to the conventional downsampling methods. Our implementation are available at https://github.com/apple1986/HWD.

**中文翻译：**

> 最大池化、步长卷积等下采样操作在卷积神经网络（CNN）中被广泛用于聚合局部特征、扩大感受野、降低计算开销。但在语义分割任务中，对局部邻域做池化会丢失对逐像素预测有利的重要空间信息。为解决这一问题，我们提出一种简单而有效的池化操作——基于 Haar 小波的下采样模块（HWD）。该模块可轻松集成进 CNN 以提升语义分割模型性能。HWD 的核心思想是用 Haar 小波变换在降低特征图空间分辨率的同时尽可能保留信息。此外，为考察 HWD 的收益，我们提出一个新指标——特征熵指数（FEI），用于度量 CNN 中下采样后信息不确定性的程度；FEI 可指示一种下采样方法在语义分割中保留关键信息的能力。综合实验表明，HWD 模块能够：(1) 在多种 CNN 架构、不同模态图像数据集上有效提升分割性能；(2) 相比常规下采样方法更有效地降低信息不确定性。代码见 https://github.com/apple1986/HWD。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：语义分割要为图像每个像素分配标签（应用如车辆导航、医学图像分析），依赖丰富的空间信息（边界、纹理）。但 DCNN 中作为基础组件反复使用的下采样操作（最大池化、平均池化、步长卷积）在改变分辨率、降低计算量、扩大感受野的同时，会丢失这些对像素级预测至关重要的边界/纹理信息。
- **之前方法的问题（论文归纳为四类补偿策略）**：
  1. **跳跃连接**把编码器下采样特征送入解码器（U-Net、LCU-Net、CENet、LinkNet、RefineNet）；
  2. **多尺度特征提取**用空间金字塔池化或空洞卷积融合（DeepLab 的 ASPP、PSPNet 的金字塔池化、PCPLP-Net、BiSeNet、ICNet）；
  3. **多模态输入**利用不同模态互补性缓解信息丢失（DiSegNet、MMADT、CANet、CCFFNet）；
  4. **引入先验信息**（轮廓增强注意力、超像素、对抗样本增强、类别先验）。
  这些方法的共同思路是"事后聚合更多信息来补偿损失"。但作者指出：简单聚合（求和、拼接）可能引入无关信息，反而阻碍判别性特征学习；本质上未能从源头阻止下采样的信息丢失，尤其对小尺度目标、前背景混淆目标更不利。
- **核心矛盾与两个问题**：编码器需要下采样以降算力、扩感受野，却与保留精确像素预测所需的高分辨率空间信息冲突。论文由此提出两个问题：(Q1) 能否设计一个"信息保留型"下采样模块，在 DCNN 中尽量保留信息？(Q2) 如何确认/度量后续卷积层学到的"关键特征"的量？前者引出 HWD，后者引出 FEI。

## 关键贡献

1.  **提出基于小波的下采样模块 HWD**：作者称这是首次尝试在 DCNN 的下采样阶段"阻止/阻碍（prohibiting/impeding）信息丢失"（而非事后补偿）用于语义分割任务的工作。灵感来自无损信息变换方法，借用 Haar 小波"多尺度无损快速信号分解"的优势。
2.  **提出特征熵指数（FEI）**：借鉴信息熵思想，把神经网络视为通信系统，提出新指标度量下采样特征图与预测结果之间的信息不确定性（或特征重要性），可指示不同下采样方法保留关键信息的能力。
3.  **即插即用且高效**：HWD 可直接替换步长卷积或池化层，不显著增加计算开销，易集成进现有分割架构；论文称在与七种 SOTA 分割方法对比的大量实验中验证了有效性。

## 方法

- **整体框架（图3）**：HWD 模块由两个块串联：(1) **无损特征编码块**（lossless feature encoding block）+ (2) **特征表示学习块**（feature representation learning block）。前者负责变换特征并降低空间分辨率，后者负责提取判别性特征。
- **输入输出**：输入特征图 H×W×C；下采样后空间分辨率减半。提取文本明确写到"the size of downsampled feature maps is H/2×W/2×C"，并指出通道数可由表示学习块（1×1 卷积）调整，以对齐后续层。
- **关键块详解**：
    1.  **无损特征编码块**：核心是 **Haar 小波变换层**。Haar 小波是紧支、二进、正交规范的变换。对二维信号（如灰度图）做 Haar 变换得到四个分量，每个分量分辨率为输入的一半（H/2×W/2）：近似（低频）分量 A，以及水平 H、垂直 V、对角 D 三个细节（高频）分量。即用低通滤波器 H0 与高通滤波器 H1 + ↓2 下采样得到。空间分辨率减半的同时通道数变为 4 倍——也就是把部分空间维信息**无损地编码到通道维**，而非丢弃。论文用公式(1)-(4)给出 1 阶一维 Haar 基函数与尺度函数（j 为尺度/阶，k 为方向/序），并说明长度 L 的信号被分成两段长度 L/2，对应低通与高通分解滤波器。
    2.  **特征表示学习块**：由标准 **1×1 卷积层 + 批归一化（BN）+ ReLU** 组成。两个作用：(a) 用 1×1 卷积调整通道数以对齐后续层；(b) 尽量**过滤冗余信息**，使后续层更有效地学习判别性特征。正是这一块让 HWD 能像最大池化、步长卷积那样被替换。
- **可视化论证**：图1 在 DeepLabv3 上对比平均池化/最大池化/步长卷积/HWD 四种下采样，红框标注的树枝细节在 HWD 输出中保留得更好；图5 把 HWD 与最大池化在 RGB 图上对比（沿通道方向取最大），HWD 输出细节更丰富。
- **与已有方法的差异**：传统池化/步长卷积在降分辨率时直接丢信息；HWD 把"下采样"视为信息编码过程，用 Haar 变换在降分辨率的同一步实现信息无损保留，再用卷积学习筛选——是从下采样源头解决，而非事后补偿。
- **计算开销**：论文在**表1**对比 HWD 与 3×3 步长 2 卷积、平均池化的参数量与 FLOPs。提取文本止于此句（"It can be seen that average pooling outperforms in terms of parameters and Floating Point Opera…"），即平均池化在参数/计算量上最优，HWD 的开销处于可接受范围（具体数值在提取缓存截断处之后，PDF 文本未明确）。

## 实验

- **任务与数据**：论文声称在"various CNN architectures"和"different modality image datasets"上验证。提取文本（前12页）未给出完整实验表；据原文后续页线索（缺失页摘录，待核）涉及 **CamVid** 详细结果、**Synapse** 数据集（医学多器官分割）等。原笔记列出的 Cityscapes / PASCAL VOC 2012 / ADE20K / ISIC 2018 / PH2 / DRIVE 在提取文本中未出现，**PDF 文本未明确**，待核。
- **对比方法**：论文摘要与贡献中明确对比 **七种 SOTA 分割方法**（具体名称在提取文本前12页未列全）。据原文后续页线索（待核），Synapse 上测试了 HRNet、ConvNeXt、UNext、TransUNet 等（含纯卷积网络与 transformer），"simply replace the downsampling operation" 做对比。
- **评价指标**：分割主指标为平均交并比（**mIoU**）；论文另用自提的**特征熵指数 FEI** 评估信息不确定性。
- **主结果**：提取文本前12页未含具体 mIoU 数字。据原文后续页线索（p.13 摘录，提取缓存未覆盖，待核）："0.8% mIoU on seven segmentation architectures, demonstrating our…"，即在七种分割架构上平均提升约 0.8% mIoU，并提到"在准确率、时延、参数量之间取得平衡"。
- **消融实验**：据原文后续页线索（待核），论文做了"替换 HWD 的无损特征编码块/表示学习块"的实验（Table C.1 给出 mean IoU），并讨论了对大场景中小尺度目标的性能改善与跨主干网络的适配性。提取文本前12页未含消融细节。
- **泛化性**：论文声称 HWD 能"在不同模态图像数据集、多种 CNN 架构上有效提升分割性能"，即做了跨数据集、跨网络的泛化验证。
- **效率**：见"方法-计算开销"，表1 对比参数量与 FLOPs，平均池化最优、HWD 可接受；具体数值 PDF 文本未明确。

## 局限

- **计算/参数成本**：相对无参数的池化，引入 Haar 变换与 1×1 卷积（+BN+ReLU）会增加参数与计算量；表1 中平均池化在参数/FLOPs 上优于 HWD。极低功耗或强实时场景需权衡。
- **任务范围**：论文聚焦语义分割（含医学分割）。对实例分割、关键点检测等其他高分辨率依赖任务，以及对本就不需细节的分类任务，HWD 的增益是否成立未在本文充分验证。
- **提取覆盖**：提取缓存仅前12页（含摘要、引言、相关工作、方法主体与表1开头），完整实验数值表、详细消融、推理速度对比、结论与未来工作在缓存截断之后，本笔记相应部分多为概括或据后续页线索标注"待核"。
- **理论深度**：虽借用信息熵并提出 FEI，但从"无损编码"到"学到更判别特征→提升分割"的因果链，论文给出的理论分析相对偏直觉。
- **复现门槛**：需正确实现 Haar 小波变换层（与标准 PyTorch/TF 算子略有差异），可参考官方仓库 https://github.com/apple1986/HWD 。

## 个人评论

1.  **范式价值**：把"下采样必丢信息、只能事后补偿"的隐含假设换成"在降分辨率这一步就做信息无损编码"。从信号处理（小波）反哺深度学习基础算子，思路干净且有迁移潜力。
2.  **工程友好**：HWD 本质是"Haar 变换（空间→通道，无参）+ 1×1 卷积 + BN + ReLU"，与池化/步长卷积接口一致，替换成本低，便于他人快速试验与消融。
3.  **度量工具**：FEI 把"中间层特征对最终预测的不确定性贡献"显式量化，为诊断/比较下采样算子提供了一个超越 mIoU 的视角，值得关注其与最终精度的相关性是否稳健。
4.  **可延展性**：该"无损可逆变换 + 学习筛选"双块设计可推广到傅里叶、其他小波等变换，也提示"用信息论指标指导算子设计"的方法论。

### 使用建议

- **快速了解**：读摘要、引言末尾的三条贡献、方法 3.1（无损特征编码块）与 3.2（表示学习块），配合图1、图3-5。
- **如果复现**：精读第3节，结合图3-5 理解 Haar 分解 → 通道4倍 → 1×1 卷积调通道的流程；参考官方仓库，并据第4节补全实验设置（缓存截断部分）。
- **如果借鉴创新点**：学习"无损可逆变换 + 卷积学习筛选"的双块范式，以及"用信息熵类指标（FEI）指导/评估下采样算子"的方法论。
- **如果写 Related Work**：放入"下采样方法改进"或"小波变换在 CNN 中的应用"小节，作为替代传统池化/步长卷积的无损下采样代表。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
计算机视觉语义分割方向，研究对象是 CNN 中的**下采样算子**。论文要解决传统下采样（最大池化、平均池化、步长卷积）在分割任务中丢失边界/纹理等空间信息的问题，提出可替换标准下采样层的 HWD 模块，外加一个度量信息不确定性的指标 FEI。它属于"网络基础算子/模块设计"范畴：HWD 本身不是注意力机制，而是一个即插即用的特征下采样算子；归入主题 `B_注意力算子模块`（广义"算子模块"）是因为它与该主题下其他可插入算子模块在使用方式上一致。

## 2. 一句话总结
用 Haar 小波变换在下采样时把空间信息无损编码到通道维（再以 1×1 卷积筛选），从源头减少信息丢失以提升语义分割，并提出特征熵指数 FEI 量化下采样后的信息不确定性。

## 3. 背景与问题
- **为什么做**：分割是逐像素打标签的任务，强依赖边界、纹理等空间信息；但 DCNN 反复使用的下采样在降算力、扩感受野时直接丢这些信息，对小尺度/前背景混淆目标尤其不利。
- **之前方法的问题**：已有四类补偿策略——跳跃连接（U-Net、LCU-Net、CENet、LinkNet、RefineNet）、多尺度融合（DeepLab/ASPP、PSPNet、BiSeNet、ICNet）、多模态输入（DiSegNet、MMADT、CANet、CCFFNet）、先验信息（轮廓注意力、超像素、对抗增强、类别先验）。它们都是"事后聚合补偿"，而简单求和/拼接可能引入无关信息、阻碍判别性学习，本质未在源头阻止丢失。
- **核心矛盾与两问**：下采样的算力/感受野收益 vs 精确像素预测所需的高分辨率信息。论文据此提两问：能否设计信息保留型下采样（→HWD）？如何度量后续层学到的关键特征量（→FEI）？

## 4. 核心贡献
1.  **HWD 模块**：作者称首次在 DCNN 下采样阶段"阻止信息丢失"（而非补偿）用于分割；借 Haar 小波"多尺度无损快速分解"的优势。
2.  **FEI 指标**：把网络视为通信系统，用信息熵思想度量下采样特征图与预测之间的不确定性/特征重要性，指示下采样方法保留关键信息的能力。
3.  **即插即用 + 高效**：可直接替换步长卷积/池化，不显著增开销，易集成；论文称与七种 SOTA 分割方法对比验证有效。

## 5. 方法详解
- **两块串联（图3）**：无损特征编码块（Haar 变换，降分辨率+保信息）→ 特征表示学习块（1×1 卷积+BN+ReLU，提判别特征）。
- **无损特征编码块**：对二维特征做 Haar 小波变换，用低通 H0、高通 H1 滤波器 + ↓2 得到四个 H/2×W/2 分量：近似 A（低频）+ 水平 H / 垂直 V / 对角 D（高频）。结果是**空间分辨率减半、通道数变 4 倍**——把空间维信息无损搬到通道维。论文公式(1)-(4)给出 1 阶一维 Haar 基/尺度函数（j=尺度、k=方向），长度 L 信号分成两段 L/2 对应低/高通分解滤波。
- **特征表示学习块**：标准 1×1 卷积 + BN + ReLU。作用：(a) 调通道数对齐后续层（可减回原通道数）；(b) 过滤冗余信息以利后续判别特征学习。
- **尺寸**：输入 H×W×C → 输出 H/2×W/2×C（通道可由 1×1 卷积调整）。
- **与传统下采样的本质区别**：传统方法降分辨率即丢信息；HWD 把下采样当作信息编码，在同一步无损保留，再学习筛选。
- **训练/推理**：论文未提特殊训练策略；推理即 Haar 变换层 → 1×1 卷积+BN+ReLU。
- **开销**：表1 对比 HWD vs 3×3/stride2 卷积 vs 平均池化的参数与 FLOPs，平均池化最优、HWD 可接受（具体数值在提取缓存截断之后，PDF 文本未明确）。

## 6. 实验与结果
- **数据/任务**：声称跨多种 CNN 架构、不同模态图像数据集。提取文本（前12页）无完整结果表；据后续页线索（待核）含 CamVid 详细结果与 Synapse（医学多器官分割）。原笔记所列 Cityscapes/VOC2012/ADE20K/ISIC2018/PH2/DRIVE 在提取文本中未见，PDF 文本未明确，待核。
- **对比方法**：明确"七种 SOTA 分割方法"；据后续页线索（待核）Synapse 上含 HRNet、ConvNeXt、UNext、TransUNet 等（卷积 + transformer），做"直接替换下采样"对比。
- **指标**：mIoU + 自提 FEI。
- **主结果**：提取文本无具体数值；据后续页 p.13 摘录（提取缓存未覆盖，待核）"0.8% mIoU on seven segmentation architectures"，即在七种架构上平均约 +0.8% mIoU，并称在准确率/时延/参数间取得平衡。
- **消融**：据后续页线索（待核）做了替换 HWD 两个子块的实验（Table C.1 给 mean IoU），并讨论对大场景小目标的改善。提取文本前12页无消融细节。
- **泛化**：声称跨数据集、跨网络均提升。

## 7. 这篇论文真正有价值的地方
1.  **范式创新**：把"下采样必丢信息/只能事后补偿"改成"在下采样这一步做无损编码"，从信号处理反哺基础算子设计。
2.  **即插即用**：接口与池化/步长卷积一致，替换成本极低，利于复现与组合。
3.  **量化工具 FEI**：为研究中间层特征与预测之间的不确定性提供超越 mIoU 的量化视角。
4.  **可迁移方法论**：双块"无损可逆变换 + 学习筛选"思路可推广到傅里叶、其他小波；"以信息论指标指导算子设计"具普适性。

## 8. 局限与问题
- **成本**：相对无参池化，Haar 变换 + 1×1 卷积增加参数/计算，表1 中平均池化在参数/FLOPs 上优于 HWD；强实时/低功耗需权衡。
- **任务范围**：主要验证语义分割（含医学），对实例分割、关键点、分类等任务的增益未充分验证。
- **提取覆盖**：缓存仅前12页，完整数值、详细消融、速度对比、结论在截断之后，相关结论多为概括或据后续页线索标注"待核"。
- **理论深度**：从无损编码到判别特征提升的因果链偏直觉，理论分析较浅。
- **复现门槛**：需正确实现 Haar 小波层，建议参考官方仓库。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言三条贡献 + 方法 3.1/3.2，配图1、3-5。
- **复现**：精读第3节，理解"Haar 分解→通道4倍→1×1 卷积调通道"，参考 https://github.com/apple1986/HWD ，据第4节补全实验设置。
- **借鉴创新点**：复用"无损可逆变换 + 卷积学习筛选"双块范式，以及"用 FEI 类信息论指标评估下采样算子"的方法论。
- **写 Related Work**：归入"下采样方法改进"或"小波变换在 CNN 中的应用"，作为替代传统池化/步长卷积的无损下采样代表。

## 10. 和其他论文的关系
- 主题 `B_注意力算子模块`：HWD 不是注意力，但作为可插入基础算子与该主题下其他高效/轻量算子模块同类。
- 直接对话对象：经典分割架构（U-Net、DeepLab/v3、PSPNet 等）的下采样组件，以及小波在 CNN 中的工作（文献 [40] wavelet CNN、[41] MWCNN、[43] Wavelet-SRNet、[48] wavelet pooling 等）。与 [48] 的 wavelet pooling 区别明显：后者丢弃一级子带降维（面向分类抗过拟合），HWD 不丢子带、保留全部信息并面向分割。[[HWD下采样]] 可视为对经典架构基础下采样组件的改进方案。

## 11. 关键词
语义分割, 下采样, Haar 小波变换, 信息熵, 特征熵指数 FEI, 特征保留, 无损编码, 1×1 卷积, 池化, 步长卷积, 卷积神经网络

## 12. 可信度说明
本笔记主要基于 PDF 提取文本前12页（缓存标注 12/14 页），文本质量良好，完整覆盖摘要、引言、相关工作、方法主体（含公式与图说）及表1开头。摘要、方法、动机、贡献部分有逐句文本支撑，可靠性高。**实验具体数值（mIoU、表格）、详细消融、推理速度、结论与未来工作**在提取缓存截断处（表1 数值之后）之后，本笔记相应内容来自"全文补读记录"中 p.13-14 的零散摘录线索，已逐条标注"据原文后续页/提取缓存未覆盖，待核"。原笔记所列若干数据集（Cityscapes/VOC/ADE20K/ISIC/PH2/DRIVE）在提取文本中无依据，已降级为"PDF 文本未明确，待核"。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/HWD下采样.txt` (提取 12/14 页, 前 25000 字符; 原 AI 主体 12/14 + 全文补读 13-14 线索); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮优化: 据提取文本重建摘要、修正题名乱码、补足方法细节并对实验数值统一标注"待核"。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-14; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-14。
- **提取情况**: 缺失页 2 页, 其中 2 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Pattern Recognition 143 (2023) 109819
- p.13: We also conduct experiments by replacing the lossless feature
- p.13: This section contains detailed results for CamVid dataset with
- p.13: method could be adapted in other backbones too. Specifically, our
- p.13: method could improve the performance of small-scale objects in a large
- p.13: In this section, we test six SOTA segmentation methods on Synapse
- p.13: HRNet and ConvNeXt are pure convolution neural network, the UNext
- p.13: References
- p.13: Joint segmentation and detection of COVID-19 via a sequential region generation
- p.13: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition,
- p.13: LCU-Net: a novel low-cost U-Net for environmental microorganism image
- p.13: Symposium on Biomedical Imaging: From Nano to Macro, IEEE, 2009,

### 缺失页关键摘录

- p.13: learning block of HWD. Table C.1 shows the performance of mean IoU of
- p.13: This section contains detailed results for CamVid dataset with
- p.13: striking a balance between accuracy, latency, and parameter count for
- p.13: the considering of the accuracy and efficiency.
- p.13: 0.8% mIoU on seven segmentation architectures, demonstrating our
- p.13: convolution and transformer on synapse dataset
- p.13: dataset. They are HRNet [66], ConvNeXt [67], UNext [68], TransUNet
- p.13: these methods on Synapse dataset, and the comparative results are
- p.13: shown in Table E.1. Here, we simply replace the downsampling opera -
<!-- AI_READING_NOTE_END -->
