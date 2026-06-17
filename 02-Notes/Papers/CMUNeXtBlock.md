---
title: "CMUNeXt: An Efficient Medical Image Segmentation Network based on Large Kernel and Skip Fusion"
authors:
  - "Fenghe Tang"
  - "Jianrui Ding"
  - "Lingtao Wang"
  - "Chunping Ning"
  - "S. Kevin Zhou"
year: 2023
venue: "arXiv"
doi: 
pdf: [[CMUNeXtBlock.pdf]]
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
extract_cache: .paper-cache/extracts/CMUNeXtBlock.txt
---

# CMUNeXt: An Efficient Medical Image Segmentation Network based on Large Kernel and Skip Fusion

## 基本信息
- **PDF**: [[CMUNeXtBlock.pdf]]
- **primary_topic**: `A1_医学图像_分割`
- **topics**: `A1_医学图像_分割`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | CMUNeXt: An Efficient Medical Image Segmentation Network based on Large Kernel and Skip Fusion |
| **作者** | Fenghe Tang; Jianrui Ding; Lingtao Wang; Chunping Ning; S. Kevin Zhou |
| **发表时间** | 2023 (arXiv:2308.01239v2, 2023-08-03) |
| **刊物/会议** | arXiv (eess.IV) |
| **DOI** | 未明确; 代码: https://github.com/FengheTan9/CMUNeXt |

## 摘要

**英文原摘要（据 PDF 提取文本整理）**：

> The U-shaped architecture has emerged as a crucial paradigm in the design of medical image segmentation networks. However, due to the inherent local limitations of convolution, a fully convolutional segmentation network with U-shaped architecture struggles to effectively extract global context information, which is vital for the precise localization of lesions. While hybrid architectures combining CNNs and Transformers can address these issues, their application in real medical scenarios is limited due to the computational resource constraints imposed by the environment and edge devices. In addition, the convolutional inductive bias in lightweight networks adeptly fits the scarce medical data, which is lacking in the Transformer based network. In order to extract global context information while taking advantage of the inductive bias, we propose CMUNeXt, an efficient fully convolutional lightweight medical image segmentation network, which enables fast and accurate auxiliary diagnosis in real scene scenarios. CMUNeXt leverages large kernel and inverted bottleneck design to thoroughly mix distant spatial and location information, efficiently extracting global context information. We also introduce the Skip-Fusion block, designed to enable smooth skip-connections and ensure ample feature fusion. Experimental results on multiple medical image datasets demonstrate that CMUNeXt outperforms existing heavyweight and lightweight medical image segmentation networks in terms of segmentation performance, while offering a faster inference speed, lighter weights, and a reduced computational cost. The code is available at https://github.com/FengheTan9/CMUNeXt.

**中文翻译**：

> U 型架构已成为医学图像分割网络设计中的关键范式。然而，由于卷积固有的局部性限制，采用 U 型架构的全卷积分割网络难以有效提取全局上下文信息——而这对病灶的精确定位至关重要。虽然结合 CNN 与 Transformer 的混合架构可以解决这些问题，但受环境和边缘设备所施加的计算资源约束，它们在真实医疗场景中的应用受到限制。此外，轻量级网络中的卷积归纳偏置能很好地拟合稀缺的医学数据，这正是基于 Transformer 的网络所缺乏的。为了在利用归纳偏置的同时提取全局上下文信息，我们提出 CMUNeXt，一种高效的全卷积轻量级医学图像分割网络，可在真实场景中实现快速、准确的辅助诊断。CMUNeXt 利用大卷积核与倒瓶颈设计来充分混合远距离的空间和位置信息，从而高效地提取全局上下文信息。我们还引入了 Skip-Fusion 块，以实现平滑的跳跃连接并保证充分的特征融合。在多个医学图像数据集上的实验结果表明，CMUNeXt 在分割性能上优于现有的重量级和轻量级医学图像分割网络，同时具有更快的推理速度、更轻的权重和更低的计算成本。代码已开源于 https://github.com/FengheTan9/CMUNeXt 。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：U 型架构是医学图像分割的主流范式（U-Net 通过跳跃连接增强知识传递、能拟合稀缺医学数据），但其依赖的普通卷积具有局部性限制，难以有效提取对病灶精确定位至关重要的全局上下文信息。结合 CNN 和 Transformer 的混合架构（TransUnet、MedT、Swin-Unet）虽能引入全局建模能力，但需要大量医学数据和计算开销，难以满足边缘/移动设备的部署约束；而 Transformer 缺乏卷积归纳偏置，对稀缺医学数据拟合能力弱。因此，需要一种既能提取全局信息、又轻量高效、适合边缘部署（同时缓解服务器端模型的数据传输隐私问题）的网络。
- **之前方法的问题**：
    1. 全卷积 U 型网络（U-Net 及 Attention U-Net、U-Net++、U-Net3+、CMU-Net 等）受限于普通卷积的局部感受野，全局信息提取能力不足。
    2. CNN-Transformer 混合网络（TransUnet、MedT、Swin-Unet）虽能捕获全局信息，但参数量和计算复杂度高、对数据需求大；即便压缩参数以适配移动端，性能也显著逊于轻量级 CNN。
    3. 现有轻量级网络（UNeXt 为 CNN+MLP 混合，ConvUNeXt 改进 ConvNeXt 块）多通过减少网络宽度和深度来降低复杂度，但这通常导致性能下降。
- **作者的切入点**：近期 ConvMixer、RepLKNet（31×31 超大核）、ConvNeXt 等工作表明，大卷积核 CNN 可作为 Transformer 的替代方案来提取全局上下文，同时保留卷积归纳偏置和更大感受野。但这些工作都面向通用自然图像，自然图像与医学图像差距大，难以直接迁移到医疗场景。CMUNeXt 即把"大核 + 倒瓶颈"范式重新设计并适配到 U 型医学分割网络中。
- **选择超声数据集的理由（原文特别说明）**：超声图像中病灶位置不固定、形态呈多尺度且差异大，更能体现方法在提取医学图像全局上下文信息上的有效性。
- **核心矛盾**：如何在保持网络轻量化（低参数、低计算量、高推理速度）的同时，突破卷积的局部性限制，有效提取医学图像中的全局上下文信息以提升分割精度。

## 关键贡献

1. **提出了 CMUNeXt 网络**：一个轻量级的全卷积医学图像分割网络，采用 U 型五层编解码器结构 + 跳跃连接，在分割性能与计算开销之间取得更好的权衡（更少参数、更低计算量、更快推理）。
2. **提出了 CMUNeXt 块**：编码器核心模块，用大核深度可分离卷积 + 两个倒瓶颈点卷积，以极少参数充分提取和混合医学图像中远距离的空间与位置信息，提取全局上下文。
3. **提出了 Skip-Fusion 块**：用于跳跃连接，以分组卷积 + 倒瓶颈点卷积替代普通卷积，实现编码器知识向解码器的高效迁移与平滑、充分的特征融合。
4. **全面实验验证**：在 4 个乳腺/甲状腺超声数据集上证明 CMUNeXt 及其变体优于现有重量级与轻量级网络，并取得性能-计算开销的更优权衡。
5. **开源基准**：开源了 CMUNeXt，并发布了基于 U 型架构的医学图像分割 benchmark（https://github.com/FengheTan9/Medical-Image-Segmentation-Benchmarks）。

## 方法

- **整体框架**：CMUNeXt 遵循 U 型架构，分为编码器阶段和带跳跃连接的解码器阶段，自上而下共五层。编码器每层由 CMUNeXt 块 + 普通卷积块（扩通道）+ 下采样构成，顶层先用 stem 提取初始特征；解码器每层由 Skip-Fusion 块 + 上采样块构成。每层 CMUNeXt 块的堆叠长度记为 L1–L5、卷积核大小记为 K1–K5、通道数记为 C1–C5。
- **输入与输出**：所有数据 resize 至 256×256，输出对应分割掩码。
- **关键模块**：
    1. **CMUNeXt Block（编码器核心）**：
        - **作用**：在各编码器层级提取不同层次的全局上下文信息。
        - **结构与机制**：
            - 核心是**深度可分离卷积**（由 MobileNetV2、MobileViT 推广）：深度卷积（组数等于通道数）逐通道提取空间维度信息，再由 1×1 点卷积分离空间与通道混合，相比普通卷积大幅减少参数和计算量。
            - 用**大核深度卷积**提取每个通道的全局信息，并接残差连接。
            - 接两个点卷积并做**倒瓶颈设计**：两个点卷积之间的隐藏维度扩展为输入维度的 **4 倍**，以充分混合深度卷积提取到的全局空间维度信息（该设计由 ConvNeXt 推广）。
            - 每个卷积后均使用 **GELU 激活 + 后置 BatchNorm**。
            - 由于 CMUNeXt 块输入输出的分辨率与通道数不变，故其后再接一个**普通卷积块把通道扩大 2 倍**（注意：是块后的扩通道为 ×2，倒瓶颈中间隐藏维度才是 ×4，二者不同）。
        - **公式**（p.3，式 1–3，原文标注 σ1 = GELU，BN = BatchNorm）：
            - `f'_l = BN(σ1(DepthwiseConv(f_{l-1}))) + f_{l-1}`
            - `f''_l = BN(σ1(PointwiseConv(f'_l)))`
            - `f_l = BN(σ1(PointwiseConv(f''_l)))`
    2. **Skip-Fusion Block（跳跃连接核心）**：
        - **作用**：替代传统跳跃连接里"直接、生硬"的普通卷积融合，实现编码器全局语义特征与解码器上采样特征的平滑、充分融合，减轻编解码器负担。
        - **结构与机制**：
            - 以**分组卷积**为核心，将卷积分为两组，分别对跳跃来的编码器特征和上采样的解码器特征做"逐特征"提取与适应（kernel 3×3，stride 1，padding 1）。
            - 两路结果拼接后，接两个**倒瓶颈点卷积**做密集融合：分组卷积负责融合前的特征适配，点卷积承担繁重的特征融合工作。
            - 每个卷积后接 GELU + BatchNorm。
        - **公式**（p.4，式 4–6）：
            - `f_concat = Concat(BN(OrdinaryConv(f_E)), BN(OrdinaryConv(f_D)))`
            - `f'_fusion = BN(σ1(PointwiseConv(f_concat)))`
            - `f_fusion = BN(σ1(PointwiseConv(f'_fusion)))`，其中 f_E、f_D 分别为编码器、解码器特征。
- **其他模块**：
    - **Stem**：不沿用 ResNet/ConvNeXt 那种会降分辨率（导致与顶层跳跃连接不一致）的 stem，而用 3×3 普通卷积块（Conv + BN + ReLU，stride 1，padding 1）提取初始特征，保持与顶层跳跃连接一致，避免编码早期丢失重要特征（p.3）。
    - **Down Sample**：不用步长 2 的卷积下采样，而用 **2×2、步长 2 的最大池化**。理由：医学图像分辨率低、局部边缘变化小，池化能以最小计算开销有效过滤医学图像噪声（p.4）。
    - **Upsampling Block**：双线性插值上采样 2 倍，后接 3×3 卷积（stride 1，padding 1）、BN、ReLU（p.4）。
- **CMUNeXt 变体配置**（Table 1）：
    - **CMUNeXt-S**：C=(8,16,32,64,128)，L=(1,1,1,1,1)，K=(3,3,7,7,9)；底层核增至 9，以补偿更小 compute ratio 带来的全局感受野缩小。
    - **CMUNeXt**：C=(16,32,128,160,256)，L=(1,1,1,3,1)，K=(3,3,7,7,7)。
    - **CMUNeXt-L**：C=(32,64,128,256,512)，L=(1,1,1,6,3)，K=(3,3,7,7,7)，compute ratio (1,1,6,3)。
- **训练方式**：PyTorch 实现；损失为 BCE 与 Dice 的组合 `L = 0.5×BCE + Dice`（注意：原文式 7 中 BCE 前系数 0.5、Dice 前无显式系数，与原笔记"各 0.5"略有出入，以原文为准）。SGD 优化器（动量 0.9、权重衰减 1e-4），初始学习率 0.01、poly 衰减策略，批大小 8，训练 300 轮，单张 NVIDIA RTX4090 GPU。数据增强为随机旋转和翻转（p.5）。
- **推理流程**：文中未单独详述，为标准 U 型网络前向传播。
- **与已有方法的差异**：CMUNeXt 是纯 CNN 架构——区别于 UNeXt（CNN+MLP 混合）和 ConvUNeXt（改进 ConvNeXt 块）等轻量网络的混合/直接套用做法，也区别于 TransUnet 等完全引入 Transformer 的混合网络；它依赖大核深度卷积提取全局信息，在保持轻量的同时获得有竞争力的性能。

## 实验

- **数据集**（均按 70/30 随机划分训练/验证，重复 3 次以评估泛化）：
    - **BUS**（乳腺超声，公开）：562 张，5 种超声设备采集，含 306 良性 + 256 恶性，均有 GT 标注。
    - **BUSI**（乳腺超声，公开）：来自 600 名女性患者共 780 张，含 133 正常 + 487 良性 + 210 恶性；按既有研究惯例仅使用良性与恶性（共 697 张）。
    - **TNSCUI**（甲状腺结节超声，公开，TN-SCUI 2020 挑战赛，由 CAAU 收集）：3644 例，不同年龄与性别，均有 GT 标注。
    - **TUS**（甲状腺超声，**私有**）：青岛大学附属医院超声科采集，3 台不同超声机，192 例、共 1942 张图像，由 3 名经验丰富的放射科医生标注。
- **对比方法**：9 个广泛使用/SOTA 网络——卷积类（U-Net、Attention U-Net、U-Net++、U-Net3+、CMU-Net）、CNN-Transformer 混合类（TransUnet、MedT、Swin-Unet）、轻量类（UNeXt、ConvUNeXt）。
- **评价指标**：分割性能用 IoU、F1-score；效率用参数量（M）、计算复杂度（GFLOPs）、推理速度（FPS）。
- **主实验结果（Table 2，单位 %）**：
    - **综合最优（中型）**：CMUNeXt 在 BUSI 上取得最佳 IoU **71.56** / F1 **79.86**（3.14M，7.41 GFLOPs，471.43 FPS）。
    - **大型变体**：CMUNeXt-L（8.28M，17.18 GFLOPs，281.87 FPS）在 BUS（IoU **87.44**）、TUS（IoU **83.13**）、TNSCUI（IoU **77.83**）上取得 SOTA。
    - **效率对比**：相比重量级网络 CMU-Net / TransUNet，CMUNeXt-L 参数与 GFLOPs 分别减少 **6.03×** 和 **2.24×**，FPS 至少提升 **2.49×**。
    - **最轻变体**：CMUNeXt-S 仅 0.41M 参数、1.09 GFLOPs、657.01 FPS；相比 UNeXt，在四个数据集上 IoU 提升 **1.1%–3.8%**、F1 提升 **0.7%–3.2%**，参数更少且推理更快。
- **消融实验（Table 3，BUSI 列）**：
    - 将原始 U-Net 通道数从 (64,128,256,512,1024) 大幅减到 (16,32,128,160,256) 得到 "Reduced U-Net"（34.52M→3.34M），分割性能仅微降（BUSI IoU 68.61→67.97），说明原始 U-Net 参数冗余严重、单纯增宽无助于性能。
    - 用 CMUNeXt 块替换编码器后（"CMUNeXt Block"，3.18M），性能显著提升（BUSI IoU 67.97→**70.35**）。
    - 再加 Skip-Fusion 块（完整 CMUNeXt，3.14M），性能进一步提升（BUSI IoU 达 **71.56**），验证两个核心模块各自的有效性。
- **效率信息**：CMUNeXt 系列参数 0.41M–8.28M、GFLOPs 1.09–17.18、FPS 281–657，展现优异的效率-性能平衡，适合边缘/移动设备部署；可按需选择变体在精度与推理成本间权衡。Figure 2 给出 IoU 对 FPS/GFLOPs/参数（四数据集均值）的对比图，Figure 3 给出四数据集的可视化分割结果。

## 局限

1. **方法适用性（推断）**：大核卷积可能模糊图像中极细微的局部结构，对依赖超精细局部纹理的病灶（如微钙化点）是否最优存疑；论文仅在病灶整体分割上验证，未涉及需要像素级精细结构的任务（如血管分割）。
2. **数据集范围**：实验仅限**超声图像**（乳腺、甲状腺），未在 CT、MRI、内窥镜等其他模态上验证，泛化性待考察。
3. **计算成本隐忧（推断）**：整体参数/FLOPs 低，但大核深度卷积在部分硬件（如某些移动端 GPU）上的实际推理效率可能因缺乏优化而不及预期；论文 FPS 在 RTX4090 上测得，未报告真实边缘设备实测速度。
4. **临床验证缺失**：研究停留在算法层面，未涉及真实临床工作流集成、医生接受度、对诊断准确率的实际提升等临床意义。
5. **复现风险**：使用了私有数据集 TUS，且部分对比方法结果可能依赖各自实现与调参，完整复现所有对比实验存在一定难度。

> 说明：上述第 1、3 条为基于方法特性的合理推断，论文文本未直接讨论；第 2、4、5 条有提取文本支撑（私有数据集、仅超声模态、纯算法评估）。

## 个人评论

1. **技术路线启发**：论文清晰地展示了在轻量级医学图像分割中，用大核（7×7、9×9）深度可分离卷积替代计算昂贵的 Transformer 模块来捕获全局信息，是可行且高效的方案——并且强调了卷积归纳偏置对稀缺医学数据的拟合优势，这是它相较 Transformer 的关键论点。
2. **模块设计思想**："大核深度卷积提取空间信息 + 倒瓶颈点卷积混合通道信息"这一范式简洁规整、易复现且被消融证明有效；Skip-Fusion 把"融合前适配（分组卷积）"与"密集融合（点卷积）"分工的思路，对改进跳跃连接有借鉴价值。
3. **实用导向**：论文紧扣"边缘部署"实际需求，同时评估参数、GFLOPs、FPS 而非只看精度，并通过多变体（S/M/L）给出可调的精度-成本权衡，面向应用的评估视角值得参考。
4. **实验范式**：在 4 个（含 1 个私有）超声数据集、3 次随机划分上验证，并配以编码器/解码器分步消融，结论较可信，也为后续工作提供了基准与开源代码。
5. **可挑剔处**：性能优势在多数据集上其实相当接近（如 CMUNeXt vs CMU-Net 在 BUS/TUS 的 IoU 差距很小），论文的真正卖点是"在相近甚至更优精度下大幅降低参数/计算/提升速度"，而非纯精度碾压——阅读时不宜把它当作精度 SOTA 来对待。

### 使用建议

- **快速了解**：读**摘要**与**引言**掌握动机、贡献与结论；看 **Table 2** 与 **Figure 2** 快速把握性能-效率全局对比。
- **复现重点**：精读 **Method**（CMUNeXt Block 与 Skip-Fusion Block 的结构与公式 p.3–4）、**Table 1** 的三种变体配置（C/L/K）以及 **Implementation Details**（p.5：BCE+Dice 损失、SGD、lr 0.01 poly、batch 8、300 轮、RTX4090）。
- **借鉴创新点**：
    - **想设计轻量级分割网络**：学习"大核深度可分离卷积 + 倒瓶颈（隐藏维度 ×4）"的模块构建思路。
    - **想改进跳跃连接**：参考 Skip-Fusion 块"分组卷积预适应 + 点卷积密集融合"的分工设计。
    - **做超声图像分割研究**：可直接在文中四个数据集上对比，并复用其开源 benchmark。
- **写 Related Work**：可归入"轻量级医学图像分割网络""基于大卷积核的全局特征提取""U 型架构的模块优化"等类别引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A1_医学图像_分割]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于医学图像分割方向，具体聚焦于设计高效、轻量级的全卷积网络，以解决在资源受限的边缘/移动设备上进行快速、准确医学图像分割的挑战。其核心是提出一种基于 U 型架构的纯 CNN 网络，用大核深度卷积替代计算开销大的 CNN-Transformer 混合网络来提取全局上下文，同时保留卷积归纳偏置以拟合稀缺医学数据。本文适合放在"医学图像分割""轻量级网络设计""大卷积核应用"等主题下。

## 2. 一句话总结
本文提出 CMUNeXt——一种基于大核深度可分离卷积（CMUNeXt 块）与分组卷积融合（Skip-Fusion 块）的轻量级全卷积 U 型网络，以极低参数量和计算开销有效提取医学图像全局上下文，在 4 个超声数据集上实现精度与效率的更优权衡。

## 3. 背景与问题
- **为什么要做**：U 型架构是医学图像分割主流范式，但普通卷积的局部性限制使其难以提取对病灶定位至关重要的全局上下文；CNN-Transformer 混合架构能补全局建模但计算/数据开销大、且 Transformer 缺乏归纳偏置、不适合稀缺医学数据与边缘部署。需要一种"既全局、又轻量、又保留卷积归纳偏置"的网络。
- **之前方法的问题**：
    1. 全卷积 U 型网络（U-Net 系列）受限于局部感受野，全局信息提取不足。
    2. CNN-Transformer 混合网络（TransUnet、MedT、Swin-Unet）参数/计算高、数据需求大；即便压参数适配移动端，性能也明显逊于轻量 CNN。
    3. 现有轻量网络（UNeXt 为 CNN+MLP、ConvUNeXt 改进 ConvNeXt）多靠减宽减深降复杂度，常以性能为代价。
- **作者切入点**：借鉴 ConvMixer / RepLKNet(31×31) / ConvNeXt 的"大核 CNN 替代 Transformer"思路，但这些都面向自然图像；CMUNeXt 把该范式重设计并适配到医学 U 型分割网络。
- **核心矛盾**：如何在轻量化（低参数、低计算、高 FPS）的同时突破卷积局部性、有效提取全局上下文以提升分割精度。

## 4. 核心贡献
1. **CMUNeXt 网络**：轻量全卷积医学分割网络，五层 U 型编解码 + 跳跃连接，取得分割性能与计算开销的更优权衡。
2. **CMUNeXt 块**：编码器核心，大核深度可分离卷积 + 两个倒瓶颈点卷积，以极少参数提取并混合远距离空间/位置信息。
3. **Skip-Fusion 块**：跳跃连接核心，分组卷积 + 倒瓶颈点卷积替代普通卷积，实现编码器知识向解码器的高效、平滑融合。
4. **全面实验**：在 4 个乳腺/甲状腺超声数据集上优于重量级与轻量级网络，并开源代码与 U 型分割 benchmark。

## 5. 方法详解
- **整体框架**：U 型五层结构，分编码器阶段与带跳跃连接的解码器阶段。编码器每层 = CMUNeXt 块 + 普通卷积扩通道 + 下采样，顶层先用 stem；解码器每层 = Skip-Fusion 块 + 上采样。各层堆叠长度 L1–L5、核大小 K1–K5、通道 C1–C5。
- **输入/输出**：图像 resize 256×256，输出分割掩码。
- **CMUNeXt Block**：核心为深度可分离卷积（深度卷积逐通道提空间信息 + 点卷积分离空间/通道混合）。用大核深度卷积提全局信息并加残差；其后两个点卷积做倒瓶颈（中间隐藏维度 = 输入 ×4）充分混合；每卷积后 GELU + 后置 BN。块输入输出分辨率/通道不变，故块后再用普通卷积把通道 ×2。公式见正文式 1–3。
- **Skip-Fusion Block**：用分组卷积（分两组，3×3/s1/p1）分别对编码器跳跃特征与解码器上采样特征做"逐特征"适配，拼接后接两个倒瓶颈点卷积做密集融合（分组卷积管适配、点卷积管融合），每卷积后 GELU + BN。公式见正文式 4–6。
- **Stem / Down Sample / Upsample**：stem 用 3×3 普通卷积块（不降分辨率，保持与顶层跳跃一致）；下采样用 2×2/s2 最大池化（过滤医学图像噪声、开销小）；上采样用双线性 ×2 + 3×3 卷积 + BN + ReLU。
- **变体（Table 1）**：S=C(8,16,32,64,128)/L(1,1,1,1,1)/K(3,3,7,7,9)；M=C(16,32,128,160,256)/L(1,1,1,3,1)/K(3,3,7,7,7)；L=C(32,64,128,256,512)/L(1,1,1,6,3)/K(3,3,7,7,7)。S 把底层核增至 9 以补偿感受野。
- **训练**：损失 L=0.5×BCE+Dice（式 7，以原文为准）；SGD（动量 0.9、wd 1e-4）、lr 0.01 + poly、batch 8、300 epoch、单卡 RTX4090；增强为随机旋转/翻转。
- **与已有方法差异**：纯 CNN，区别于 UNeXt(CNN+MLP)、ConvUNeXt（套用 ConvNeXt 块）与 TransUnet（引入 Transformer），靠大核深度卷积提全局信息。

## 6. 实验与结果
- **数据集**：BUS（562，306 良/256 恶）、BUSI（780 总，仅用良+恶共 697）、TNSCUI（3644）、TUS（私有，192 例/1942 张）；均 70/30 随机划分、重复 3 次。
- **对比方法**：U-Net、Attention U-Net、U-Net++、U-Net3+、CMU-Net、TransUnet、MedT、Swin-Unet、UNeXt、ConvUNeXt（共 9 个 SOTA/常用网络）。
- **指标**：IoU、F1（性能）；Params(M)、GFLOPs、FPS（效率）。
- **主结果（Table 2）**：
    - CMUNeXt（中型，3.14M/7.41 GFLOPs/471.43 FPS）在 BUSI 上最优：IoU 71.56 / F1 79.86。
    - CMUNeXt-L（8.28M/17.18 GFLOPs/281.87 FPS）在 BUS(IoU 87.44)、TUS(IoU 83.13)、TNSCUI(IoU 77.83) 上 SOTA；相比 CMU-Net/TransUNet，参数减 6.03×、GFLOPs 减 2.24×、FPS 至少 +2.49×。
    - CMUNeXt-S（0.41M/1.09 GFLOPs/657.01 FPS）相比 UNeXt，四数据集 IoU +1.1–3.8%、F1 +0.7–3.2%，且更轻更快。
- **消融（Table 3，BUSI）**：原始 U-Net(34.52M, IoU 68.61) → Reduced U-Net(3.34M, IoU 67.97，仅微降，证明参数冗余) → +CMUNeXt 块(3.18M, IoU 70.35) → +Skip-Fusion(完整 3.14M, IoU 71.56)，逐步验证两模块有效。
- **效率**：参数 0.41–8.28M、GFLOPs 1.09–17.18、FPS 281–657，效率-性能平衡优异；Figure 2/3 给出对比图与可视化结果。

## 7. 这篇论文真正有价值的地方
1. **技术路线启发**：清晰证明在轻量医学分割中，用大核（7×7/9×9）深度可分离卷积替代昂贵 Transformer 来捕获全局信息可行且高效，并强调卷积归纳偏置对稀缺医学数据的拟合优势。
2. **模块设计思想**：CMUNeXt 块（大核深度卷积 + 倒瓶颈点卷积）与 Skip-Fusion 块（分组卷积适配 + 点卷积融合）简洁规整、易复现且经消融证明有效，"大核提空间、倒瓶颈点卷积混通道"的范式值得借鉴。
3. **实用导向**：紧扣边缘部署，同时评估大小/计算/速度并给出 S/M/L 可调权衡，面向应用的评估视角有参考价值。
4. **实验范式**：多（含私有）超声数据集 + 3 次划分 + 分步消融，结论较可信，且开源代码与 benchmark。

## 8. 局限与问题
1. **方法适用性（推断）**：大核可能模糊极细微局部结构（如微钙化点），论文仅验证病灶整体分割，未涉及需像素级精细结构的任务。
2. **数据集范围**：仅超声（乳腺、甲状腺），未在 CT/MRI/内窥镜等模态验证，泛化性待考察。
3. **计算成本隐忧（推断）**：FPS 在 RTX4090 上测得，大核深度卷积在部分移动端硬件可能缺乏优化，未报告真实边缘设备实测。
4. **临床验证缺失**：停留在算法层面，未涉及临床工作流集成与诊断收益。
5. **复现风险**：含私有数据集 TUS，部分对比结果依赖各自实现/调参，完整复现有难度。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要+引言掌握动机/贡献/结论；看 Table 2、Figure 2 把握性能-效率全局对比。
- **复现重点**：精读 Method（两模块结构与公式 p.3–4）、Table 1 变体配置、Implementation Details（p.5 超参数）。
- **借鉴创新点**：想做轻量分割→学"大核深度可分离卷积 + 倒瓶颈"；想改跳跃连接→参考 Skip-Fusion 的分工；做超声分割→直接用其四数据集与开源 benchmark 对比。
- **写 Related Work**：归入"轻量级医学图像分割网络""大卷积核全局特征提取""U 型架构模块优化"等类别。

## 10. 和其他论文的关系
根据主题与正文引用，本文与以下工作密切相关：
- [[UNeXt]]：轻量级医学分割（CNN+MLP），本文重要轻量基线，CMUNeXt-S 在四数据集上 IoU/F1 均超越它。
- [[CMU-Net]]：作者团队前期工作（Tang et al. 2022），重量级基线，本文在效率上大幅改进（参数/GFLOPs 减、FPS 增）且精度相近或更优。
- [[ConvNeXt]]：本文"大核 + 倒瓶颈设计"的直接灵感来源，但 ConvNeXt 面向通用图像，本文将其适配到医学分割。
- [[RepLKNet]]：用 31×31 超大核提全局信息，为"大核扩感受野"提供旁证。
- [[MobileNetV2]]：其深度可分离卷积与倒瓶颈结构是 CMUNeXt 块设计基础（原文亦提及 MobileViT）。
- [[TransUnet]] / Swin-Unet / MedT：CNN-Transformer 混合对比基线，本文用纯 CNN 大核方案在效率上显著超越。

## 11. 关键词
医学图像分割, 轻量级网络, 大核卷积, 深度可分离卷积, 倒瓶颈设计, U 型架构, 全局上下文, Skip-Fusion, 跳跃连接, 分组卷积, 超声图像, 边缘部署

## 12. 可信度说明
本精读笔记**完全基于** PDF 提取文本（8/8 页）生成，文本清晰、覆盖标题、作者、摘要、引言、方法、实验（含 Table 1–3 数据）及讨论。所有技术细节、模块描述、公式、实验数据均严格源自该文本并标注页码（p.X）。已修正原笔记中的若干事实错误：年份 2018→2023（arXiv:2308.01239v2）、标题补全"based on Large Kernel and Skip Fusion"、损失函数表述据原文式 7 校正、明确"块后扩通道 ×2 与倒瓶颈隐藏维度 ×4"的区别、补充 stem/下采样动机、变体 C/L/K 配置、RTX4090 训练环境与开源链接。局限中第 1、3 条为基于方法特性的合理推断（已标注），其余均有文本支撑。提取文本质量良好，可支撑对论文核心内容的全面、准确理解。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 8/8 页, 约 3130 字符/页, 正文末尾约 8000 字符为参考文献已截断、不影响正文事实核验); 来源缓存: `.paper-cache/extracts/CMUNeXtBlock.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
