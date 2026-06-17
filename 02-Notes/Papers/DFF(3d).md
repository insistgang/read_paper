---
title: "D-Net: Dynamic Large Kernel with Dynamic Feature Fusion for Volumetric Medical Image Segmentation"
authors:
  - "Jin Yang"
  - "Peijie Qiu"
  - "Yichi Zhang"
  - "Daniel S. Marcus"
  - "Aristeidis Sotiras"
year: 2024
venue: "arXiv"
doi: 
pdf: [[DFF(3d).pdf]]
primary_topic: A1_医学图像_分割
topics:
  - "A1_医学图像_分割"
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
extract_cache: .paper-cache/extracts/DFF(3d).txt
---

# D-Net: Dynamic Large Kernel with Dynamic Feature Fusion for Volumetric Medical Image Segmentation

## 基本信息
- **PDF**: [[DFF(3d).pdf]]
- **primary_topic**: `A1_医学图像_分割`
- **topics**: `A1_医学图像_分割`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | D-Net: Dynamic Large Kernel with Dynamic Feature Fusion for Volumetric Medical Image Segmentation |
| **作者** | Jin Yang; Peijie Qiu; Yichi Zhang; Daniel S. Marcus; Aristeidis Sotiras（华盛顿大学医学院放射科 / 复旦大学数据科学学院） |
| **发表时间** | 2024（arXiv:2403.10674v1, 2024-03-15） |
| **刊物/会议** | arXiv (eess.IV) |
| **代码** | https://github.com/sotiraslab/DLK |
| **DOI** | 未明确（arXiv preprint） |

## 摘要

> **清理后英文原摘要**（据 PDF 提取文本，修复空格/连字符、剔除杂入图表数字）：
> Hierarchical transformers have achieved significant success in medical image segmentation due to their large receptive field and capabilities of effectively leveraging global long-range contextual information. Convolutional neural networks (CNNs) can also deliver a large receptive field by using large kernels, enabling them to achieve competitive performance with fewer model parameters. However, CNNs incorporated with large convolutional kernels remain constrained in adaptively capturing multi-scale features from organs with large variations in shape and size due to the employment of fixed-sized kernels. Additionally, they are unable to utilize global contextual information efficiently. To address these limitations, we propose Dynamic Large Kernel (DLK) and Dynamic Feature Fusion (DFF) modules. The DLK module employs multiple large kernels with varying kernel sizes and dilation rates to capture multi-scale features. Subsequently, a dynamic selection mechanism is utilized to adaptively highlight the most important spatial features based on global information. Additionally, the DFF module is proposed to adaptively fuse multi-scale local feature maps based on their global information. We integrate DLK and DFF in a hierarchical transformer architecture to develop a novel architecture, termed D-Net. D-Net is able to effectively utilize a multi-scale large receptive field and adaptively harness global contextual information. Extensive experimental results demonstrate that D-Net outperforms other state-of-the-art models in the two volumetric segmentation tasks, including abdominal multi-organ segmentation and multi-modality brain tumor segmentation. Our code is available at https://github.com/sotiraslab/DLK.

> **中文翻译**：
> 层次化 Transformer 凭借大感受野以及高效利用全局长程上下文信息的能力，在医学图像分割中取得了显著成功。卷积神经网络（CNN）也可以通过使用大卷积核获得大感受野，从而以更少的模型参数实现具有竞争力的性能。然而，采用大卷积核的 CNN 由于使用固定尺寸的核，在自适应捕获形状和尺寸差异巨大的器官的多尺度特征方面仍受到限制；此外，它们也无法高效利用全局上下文信息。为解决这些局限，本文提出动态大核（DLK）和动态特征融合（DFF）两个模块。DLK 模块采用多个不同核尺寸与膨胀率的大核来捕获多尺度特征，随后利用动态选择机制基于全局信息自适应地突出最重要的空间特征。DFF 模块则基于多尺度局部特征图的全局信息对其进行自适应融合。我们将 DLK 与 DFF 集成进一个层次化 Transformer 架构，构建出新架构 D-Net。D-Net 能够有效利用多尺度大感受野并自适应地利用全局上下文信息。大量实验结果表明，在腹部多器官分割和多模态脑肿瘤分割两项体积分割任务上，D-Net 均优于其他最先进模型。代码已开源于 https://github.com/sotiraslab/DLK 。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：视觉 Transformer（ViT）凭借注意力机制获得了大感受野和利用全局上下文的能力，但其自注意力在高分辨率图像上计算复杂度高。为降低复杂度，层次化 ViT 被提出，以近似线性复杂度对多尺度密集特征建模，因性能优异被广泛用作医学图像分割骨干（p.1-2）。然而注意力机制往往限制了（层次化）ViT 模型有效提取**局部**上下文信息（p.2）。
- **之前方法的问题**：CNN 在局部特征提取上有优势，但小卷积核限制了感受野。为扩大感受野，大卷积核（LCK）被引入 CNN 架构并在医学分割中受到关注，但这类网络依赖**单一固定尺寸**的大核，难以捕获器官（存在巨大的器官间与个体间形状/尺寸差异）的多尺度特征；同时它们**缺乏增强局部特征与全局上下文交互的机制**（p.2）。
- **核心矛盾**：**如何在保持 CNN 局部特征提取优势并利用大感受野的同时，增强模型对多尺度形态变化的自适应能力，并有效融合全局上下文信息以提升体积分割精度**。
## 关键贡献

论文自述贡献为三点（p.2）：

1.  **动态大核模块（DLK）**：用于通用特征提取。采用多个大卷积核捕获多尺度特征，随后利用动态选择机制基于全局上下文信息自适应地突出最重要的空间特征（p.2-3）。与 ASPP 等并行聚合多核不同，DLK **级联**（cascade）逐渐增大核尺寸和膨胀率的大核，使有效感受野递进式增长（p.2）。
2.  **动态特征融合模块（DFF）**：用于自适应特征融合。通过通道维动态选择机制保留重要特征图，再通过空间维动态选择机制突出重要空间区域，整个融合过程由全局信息引导（p.2, p.4-5）。
3.  **D-Net 架构**：将 DLK 与 DFF 集成进层次化 ViT 架构，构建用于 3D 体积医学图像分割的 D-Net，在较低模型复杂度下实现更高分割精度（p.2-3）。
## 方法

- **整体框架**：D-Net 是编码器-解码器结构，由编码器、瓶颈（bottleneck）、解码器和一个**显著性层（salience layer）**组成（Fig. 3, p.5-6）。显著性层用于从原始图像提取显著空间特征，编码器-解码器负责学习层次化特征表示。
- **输入输出**：输入是 3D 医学图像体素块（CT/MRI），通道维起始为单/多模态；输出是体素级分割预测（p.5-7）。嵌入维度 C = 48（p.6）。
- **关键模块**：
    - **DLK（动态大核）**：级联两个大深度可分离卷积核——DWConv(5,1)（5×5×5 核、膨胀率 1）与 DWConv(7,3)（7×7×7 核、膨胀率 3），其中 X₂ 在 X₁ 之上提取，二者级联后的等效感受野相当于 23×23×23 核（p.3）。随后对拼接特征 [X₁;X₂] 沿通道做平均池化（AVP）和最大池化（MAP）得到 w_avg、w_map，再经一个 7×7×7 卷积（Conv7）使空间描述子间交互、Sigmoid 激活生成动态选择权重 [w₁;w₂]。最终输出为 `Xl = ((w₁⊗X₁) ⊕ (w₂⊗X₂)) + Xl`（残差）（p.3-4）。
    - **DLK 模块**：将 DLK 嵌入两个 1×1×1 卷积（线性层 Conv1）之间、其间用 GELU 激活，并加残差连接（p.4）。
    - **DLK 块（block）**：用 DLK 模块替换标准层次化 ViT 块中的多头自注意力，一个 DLK 块由一个 DLK 模块和一个 MLP 模块组成，每个模块前加 LayerNorm、后加残差，与 ViT 块同构（p.4）。
    - **DFF（动态特征融合）**：用于编码器-解码器跳跃连接特征 F₁、F₂ 的融合（Fig. 2, p.4-5）。① **通道路径**：对拼接特征 [F₁;F₂] 级联 AVGPool→Conv1→Sigmoid 得到全局通道重要性 `w_ch = Sigmoid(Conv1(AVGPool([F₁;F₂])))`，用其校准拼接特征后再经 1×1×1 卷积做通道缩减并选择重要特征图 `Fl = Conv1(w_ch ⊗ [F₁;F₂])`，把通道数降回原始数。② **空间路径**：`w_sp = Sigmoid(Conv1(F₁) ⊕ Conv1(F₂))` 提取全局空间重要性，用以重新校准 Fl 得到最终融合特征 `F̂l = w_sp ⊗ Fl`（p.5）。
- **网络结构细节**：
    - **编码器**：不展平 patch，而用步长为 2 的 7×7×7 卷积把图像分块为 H/2×W/2×D/2 的特征嵌入并投影到 C=48 维；每阶段用 2 个连续 DLK 块；下采样用 2×2×2、步长 2 的卷积，特征图缩半、通道翻倍。各阶段输出维度依次为 H/4×W/4×D/4×2C、H/8×…×4C、H/16×…×8C、H/32×…×16C（p.6）。
    - **瓶颈**：2 个连续 DLK 块，输入输出均为 H/32×W/32×D/32×16C（p.6）。
    - **解码器**：每阶段用 2×2×2、步长 2 的转置卷积上采样、通道减半，再通过 **DFF 模块**与编码器跳跃连接特征融合，随后接 2 个连续 DLK 块；最后一层转置卷积上采样到 H×W×D×C（p.6-7）。
    - **显著性层**：用两个连续 3×3×3 卷积块从输入图像生成 H×W×D×C 特征，经 DFF 与解码器特征融合，再接卷积块，最后 1×1×1 卷积输出体素级分割预测（p.7）。
- **与已有方法差异**：① 不同于 ASPP 等并行多核设计，DLK 级联大核以递归扩大感受野（p.2-3）；② 不同于静态卷积，DLK/DFF 借鉴动态卷积、SKNet 等动态机制，依据全局信息自适应选择空间特征与融合通道特征（p.2, p.4-5）。
- **医学类特化**：3D 体积分割；模态含 CT（腹部多器官，AMOS2022）与 4 模态 MRI（脑肿瘤，MSD BraTS）；端到端体素级预测；临床意义在于辅助自动化、精确的器官与肿瘤分割（p.7）。
## 实验

- **数据集**：
    1. **MICCAI 2022 AMOS（AMOS2022）**：300 例多对比腹部 CT，手工标注 15 个解剖器官；用 MONAI 预处理与增强为 96×96×96 体素块（p.7）。
    2. **MSD Brain Tumours（Medical Segmentation Decathlon）**：484 例，每例含 4 个 3D MRI 模态（FLAIR、T1w、T1gd、T2w），3 类前景标注——水肿（ED）、增强肿瘤（ET）、非增强肿瘤（NET）；用 nnUNet 流程预处理为 128×128×128 体素块（p.7）。
- **实现细节**：PyTorch 实现；损失函数 = Dice loss + 交叉熵 loss。AMOS 任务用 AdamW，初始 lr=0.0001，ReduceLROnPlateau 衰减；脑肿瘤任务遵循 nnUNet 协议，用 SGD，初始 lr=0.001，poly 学习率衰减。所有对比方法均由作者在相同设置下复现（p.7）。
- **对比方法**：3D U-Net (nnUNet)、TransUNet、TransBTS、UNETR、nnFormer、3D UX-Net（p.7-8）。（注：Table 1/AMOS 列中未含 TransUNet，含其余基线；Table 2/MSD 含 TransUNet 而未含 UX-Net。）
- **评价指标**：Dice 系数（%）。
- **主实验结果**：
    - **AMOS 腹部多器官（Table 1, p.8）**：D-Net 平均 Dice **89.01**，为最佳；DLK-Net（消融版）88.18，次优；其余 3D UNet 87.16、UX-Net 86.70、TransBTS 85.76、UNETR 83.87、nnFormer 71.76。D-Net 在所有器官上均有提升（与基线差异 Wilcoxon 符号秩检验 p<0.01）。
    - **MSD 脑肿瘤（Table 2, p.8）**：D-Net 平均 Dice **75.70**，最佳；分项 ET 80.52 / ED 83.86 / NET 62.72。DLK-Net 74.57，nnFormer 74.37，3D UNet 74.18，UNETR 73.12，TransBTS 72.81，TransUNet 71.36。
- **消融实验**：把 D-Net 退化为 **DLK-Net**——移除显著性层，并把每个 DFF 模块替换为「拼接 + 1×1×1 卷积」。结果 DLK-Net 在两项任务上仍优于其他基线，且模型复杂度最低（params 29.17M、AMOS FLOPs 47.14G），说明 DLK 块本身即贡献主要精度，显著性层与 DFF 进一步提升（p.9, Table 1&2）。
- **效率信息（Table 1, AMOS）**：D-Net params **29.96M**、FLOPs **236.90G**。对比：3D UNet 107.71M/1046.39G、nnFormer 149.33M/284.28G、UX-Net 53.01M/632.33G、UNETR 92.78M/82.73G、TransBTS 31.58M/110.71G。D-Net 参数量在所有方法中接近最低（仅高于 DLK-Net 29.17M），FLOPs 适中。参数量与 FLOPs 由 ptflops 计算（p.8）。
## 局限

> 论文正文未单列「局限」一节，以下为据方法/实验合理推断：

1.  **计算成本与实时性**：D-Net FLOPs 236.90G，虽远低于 3D UNet/UX-Net，但对资源受限或实时临床场景可能仍偏高；论文未报告推理速度。
2.  **数据集与泛化**：仅在 AMOS 腹部 CT 与 MSD 脑肿瘤两项任务上验证，对其他器官、模态或更小目标的泛化能力待考。
3.  **方法假设依赖**：DLK/DFF 的动态选择权重来自全局池化信息，对极小目标或细节区域可能丢失关键信息，自适应能力在极端情况下受限。
4.  **复现风险**：论文已开源代码（github.com/sotiraslab/DLK），但脑肿瘤任务直接「遵循 nnUNet 协议」，且超参/增强策略需严格对齐，复现需仔细遵循其设置。
## 个人评论

1.  **动态机制的设计思想**（AI 评论）：本文的关键不只是「用多尺度大核」，而是用轻量级全局信息（通道/空间池化）数据驱动地校准特征权重——比固定权重的静态融合更灵活，对医学图像中高度变异、尺寸跨度大的器官很有针对性。DLK 的「级联大核 + 空间动态选择」与 DFF 的「通道选择 + 空间校准」两阶段融合是可迁移的通用模块设计。
2.  **CNN 模块替换注意力的范式**（AI 评论）：把精心设计的纯卷积 DLK 模块整体替换层次化 ViT 块中的多头自注意力，保留 LN+残差+MLP 的块结构，是「CNN 现代化 / 大核复兴」（ConvNeXt、3D UX-Net 路线）在 3D 医学分割上的一个干净实例，对设计混合架构有参考价值。
3.  **以低复杂度换 SOTA 的权衡**（AI 评论）：消融中的 DLK-Net 用最低参数量（29.17M）、最低 FLOPs（47.14G）即超过所有基线，凸显核心模块的有效性；DFF 与显著性层带来约 +0.8 Dice（AMOS 88.18→89.01）的额外提升，是否值得这部分 FLOPs 增量（47.14G→236.90G）值得使用者按场景权衡。

### 使用建议

- **快速了解**：读 Abstract (p.1)、Introduction (p.1-2)、Conclusion (p.9)，看 Table 1/2 与 Fig. 1/2/3 即可掌握核心结果与架构。
- **复现**：精读 Method 2.1-2.3 (p.3-7) 与 Implementation details (p.7)，对照 Fig. 1/2/3 结构图；从 GitHub 仓库 sotiraslab/DLK 获取代码。
- **借鉴创新点**：DLK 的「级联大核 + 空间动态选择」、DFF 的「通道-空间两阶段动态融合」，可迁移到自己的特征提取/跳跃连接融合模块。
- **写 Related Work**：可归入「基于大卷积核的 CNN（LCK）」「混合 CNN-Transformer / 大核现代化」「自适应/动态特征处理（动态卷积、SKNet）」三类讨论。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A1_医学图像_分割]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**计算机视觉 - 医学图像分析**方向，聚焦 **3D 体积（体素级）医学图像分割** 任务（注意：不是 3D 点云）。它针对「大核 CNN 用固定尺寸核难以自适应捕获多尺度特征、且不善于利用全局上下文」这一痛点，提出动态大核（DLK）与动态特征融合（DFF）两个即插即用模块并组装成 D-Net。适合放在「医学图像分割」「大卷积核 CNN / 大核现代化」「CNN-Transformer 混合架构」「动态/自适应特征模块」等主题下。

## 2. 一句话总结
D-Net 用级联大核 + 动态空间选择的 DLK 块替换层次化 ViT 中的多头自注意力，并用通道-空间两阶段动态选择的 DFF 模块融合跳跃连接，在腹部多器官（AMOS2022，Dice 89.01）与脑肿瘤（MSD，Dice 75.70）两项 3D 分割任务上以较低复杂度超过现有 SOTA。

## 3. 背景与问题
- **为什么做**：层次化 ViT 以近似线性复杂度建模多尺度特征、利用全局信息，在医学分割中表现优异，但注意力机制限制了对**局部**上下文的有效提取（p.1-2）。CNN 局部建模强但感受野受小核约束；引入大卷积核（LCK）虽扩大感受野，却依赖**单一固定尺寸**核，无法捕获器官间/个体间巨大形状-尺寸差异的多尺度特征，且**缺乏局部-全局信息交互机制**（p.2）。
- **之前方法的问题**：1) 大核 CNN 固定核尺寸 → 无法自适应多尺度；2) 缺乏机制高效利用全局上下文指导特征提取与融合（p.2）。
- **核心矛盾**：在保留 CNN 局部优势与大感受野的同时，增强对多尺度形态变化的自适应性并有效融合全局上下文，以提升体积分割精度。

## 4. 核心贡献
1.  **DLK 模块**：多个变尺寸大深度卷积核**级联**（而非 ASPP 式并行）以递归扩大有效感受野，并用空间维动态选择机制基于全局信息突出最重要空间特征（p.2-3）。
2.  **DFF 模块**：通道维动态选择保留重要特征图、空间维动态选择突出重要区域，由全局信息引导地自适应融合多尺度局部特征（p.2, p.4-5）。
3.  **D-Net 架构**：将 DLK、DFF 集成进层次化 ViT 架构用于 3D 体积医学分割，在低复杂度下取得更高精度（p.2-3）。

## 5. 方法详解
- **整体框架**：编码器 + 瓶颈 + 解码器 + 显著性层（Fig. 3, p.5-6）。嵌入维度 C=48。
- **DLK 单元**：X₁=DWConv(5,1)(X)，X₂=DWConv(7,3)(X₁)，级联等效 23×23×23 感受野（p.3）。对 [X₁;X₂] 沿通道做 AVP 与 MAP，经 7×7×7 卷积 + Sigmoid 得 [w₁;w₂]，输出 Xl=((w₁⊗X₁)⊕(w₂⊗X₂))+Xl（p.3-4）。
- **DLK 模块/块**：DLK 夹在两层 1×1×1 卷积（GELU 居中）+残差中；DLK 块 = DLK 模块 + MLP，前置 LN、后接残差，替换标准层次化 ViT 的多头自注意力（p.4）。
- **DFF**：通道路径 w_ch=Sigmoid(Conv1(AVGPool([F₁;F₂])))，Fl=Conv1(w_ch⊗[F₁;F₂]) 完成通道缩减与选择；空间路径 w_sp=Sigmoid(Conv1(F₁)⊕Conv1(F₂))，F̂l=w_sp⊗Fl（p.4-5）。
- **编码器**：步长 2 的 7×7×7 卷积做 patch 投影到 C=48 维；每阶段 2 个 DLK 块；下采样用 2×2×2/步长 2 卷积（特征图减半、通道翻倍）。
- **瓶颈/解码器/显著性层**：瓶颈 2 个 DLK 块（H/32×W/32×D/32×16C）；解码器各阶段转置卷积上采样 + DFF 融合编码器特征 + 2 个 DLK 块；显著性层用两个 3×3×3 卷积块从原图取特征经 DFF 融合，末端 1×1×1 卷积输出体素分割（p.6-7）。
- **差异点**：级联大核 vs ASPP 并行；动态选择 vs 静态卷积（借鉴动态卷积[6]、SKNet[14]）。

## 6. 实验与结果
- **数据集**：AMOS2022（300 腹部 CT，15 器官，MONAI 预处理为 96³ 块）；MSD Brain Tumours（484 例，4 模态 MRI FLAIR/T1w/T1gd/T2w，标注 ED/ET/NET，nnUNet 预处理为 128³ 块）（p.7）。
- **训练**：Dice + 交叉熵损失；AMOS 用 AdamW（lr 1e-4，ReduceLROnPlateau）；脑肿瘤遵循 nnUNet，用 SGD（lr 1e-3，poly 衰减）；所有基线由作者同设置复现（p.7）。
- **对比方法**：3D U-Net(nnUNet)、TransUNet、TransBTS、UNETR、nnFormer、3D UX-Net、以及消融版 DLK-Net（p.7-8）。
- **AMOS（Table 1, p.8）**：D-Net 平均 Dice **89.01**（最佳，p<0.01），DLK-Net 88.18，3D UNet 87.16，UX-Net 86.70，TransBTS 85.76，UNETR 83.87，nnFormer 71.76。params 29.96M / FLOPs 236.90G（DLK-Net 29.17M/47.14G 最省）。
- **MSD 脑肿瘤（Table 2, p.8）**：D-Net 平均 Dice **75.70**（最佳，p<0.01），ET 80.52 / ED 83.86 / NET 62.72；DLK-Net 74.57、nnFormer 74.37、3D UNet 74.18、UNETR 73.12、TransBTS 72.81、TransUNet 71.36。
- **消融**：D-Net→DLK-Net（去显著性层，DFF→拼接+1×1×1 卷积），DLK-Net 仍优于全部基线且复杂度最低，说明 DLK 块为主要精度来源，DFF+显著性层进一步小幅提升（AMOS 88.18→89.01）。
- **效率**：params 与 FLOPs 由 ptflops 计算；D-Net 参数量近最低（仅高于 DLK-Net），FLOPs 远低于 3D UNet(1046.39G)/UX-Net(632.33G)（p.8）。

## 7. 这篇论文真正有价值的地方
1.  **级联大核 + 动态空间选择**：用「逐步增大核 + 膨胀率」级联递归扩张有效感受野（等效 23³），再用 AVP/MAP+7³ 卷积+Sigmoid 的轻量动态权重在两条大核分支间做空间自适应选择——是对 SKNet 思想在 3D 大核场景的具体落地。
2.  **DFF 的通道-空间两阶段融合**：跳跃连接处先按全局通道重要性做有引导的通道缩减、再按全局空间重要性校准，比简单「拼接 + 1×1 卷积」更精细，且消融证明其带来真实增益。
3.  **低复杂度换 SOTA**：DLK-Net 用最低参数量/FLOPs 即超越所有基线，说明收益主要来自模块设计而非堆参数，对设计高效 3D 分割网络有启发。

## 8. 局限与问题
1.  **计算/实时**：236.90G FLOPs 对实时或边缘场景可能偏高；未报告推理速度。
2.  **泛化**：仅 AMOS（腹部 CT）与 MSD（脑肿瘤 MRI）两任务验证，跨器官/模态/小目标泛化待考。
3.  **动态权重依赖全局池化**：极小目标或细节处可能丢信息，自适应在极端情况受限。
4.  **复现**：已开源（sotiraslab/DLK），但脑肿瘤直接套 nnUNet 协议、超参与增强需严格对齐。
5.  论文未单列局限节，上述 1-4 多为合理推断而非作者自述。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract(p.1)+Intro(p.1-2)+Conclusion(p.9)+Table 1/2+Fig. 1/2/3。
- **复现**：精读 Method 2.1-2.3(p.3-7) 与 Implementation details(p.7)，对照结构图，取 GitHub 代码。
- **借鉴**：DLK 的级联大核+空间动态选择、DFF 的通道-空间两阶段融合，可迁移到自己的提取/融合模块。
- **写 Related Work**：归入「大卷积核 CNN(LCK)」「CNN-Transformer 混合/大核现代化」「动态/自适应特征(动态卷积、SKNet)」。

## 10. 和其他论文的关系
据正文与参考文献，可能相关的工作：
- [[Swin-UNet]] (ref [3])：U 形纯 Transformer 医学分割代表。
- [[UNETR]] (ref [10], Table 1/2 基线)：Transformer 编码器用于 3D 医学分割，本文重要基线。
- [[Swin UNETR]] (ref [9])：Swin Transformer 用于脑肿瘤 MRI 分割。
- [[3D UX-Net]] (ref [13], Table 1 基线)：大核 ConvNet 现代化层次化 Transformer，本文直接对比与改进的对象。
- [[nnFormer]] (ref [25], Table 1/2 基线)：体积分割的 Transformer 变体，本文基线。
- [[nnU-Net]] (ref [11])：自配置分割框架，本文用其作 3D UNet 实现并提供脑肿瘤预处理流程。
- [[DeepLab]] / ASPP (ref [5])：并行多核（空洞空间金字塔池化），本文以「级联」与之对照。
- [[Selective Kernel Networks]] (ref [14]) 与 Dynamic Convolution (ref [6])：动态选择机制的思想来源。
- RepLKNet「Scaling up your kernels to 31×31」(ref [7])：大核设计与等效感受野计算的依据。

## 11. 关键词
动态大核(DLK), 动态特征融合(DFF), 医学图像分割, 3D 体积分割, 大卷积核, 级联大核, 大感受野, 层次化 Transformer, CNN-Transformer 混合架构, 自适应/动态特征选择, 腹部多器官分割(AMOS), 脑肿瘤分割(MSD/BraTS)

## 12. 可信度说明
本精读笔记基于 PDF 提取文本（共 12 页，提取缓存覆盖 12/12 页，但原文 26546 字符仅展示前 25000 字符，参考文献末尾少量条目被截断，不影响正文）。所有方法描述、网络结构、数据集规模、训练设置、Dice/参数/FLOPs 数值、引用页码均严格来源于该文本，未编造或引入外部知识。需提示：原笔记把 primary_topic 误标为「D_3D_点云_分类_分割_配准」，本次复核已据正文（CT/MRI 体素级医学图像分割）改正为「A1_医学图像_分割」；并补全了被截断的论文标题与第 5 位作者 Aristeidis Sotiras。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 2086 字符/页, 12/12 页, 但末尾参考文献因 25000 字符上限略有截断, 不影响正文事实); 来源缓存: `.paper-cache/extracts/DFF(3d).txt`; 生成日期: 2026-06-05; 复核优化: 2026-06-18; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
