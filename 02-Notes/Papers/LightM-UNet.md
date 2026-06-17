---
title: "LightM-UNet: Mamba Assists in Lightweight"
authors:
  - "Weibin Liao"
  - "Yinghao Zhu"
  - "Xinyuan Wang"
  - "Chengwei Pan"
  - "Yasha Wang"
  - "Liantao Ma"
year: 2024
venue: "arXiv"
doi: 
pdf: [[LightM-UNet.pdf]]
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
extract_cache: .paper-cache/extracts/LightM-UNet.txt
---

# LightM-UNet: Mamba Assists in Lightweight

## 基本信息
- **PDF**: [[LightM-UNet.pdf]]
- **primary_topic**: `A1_医学图像_分割`
- **topics**: `A1_医学图像_分割`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | LightM-UNet: Mamba Assists in Lightweight |
| **作者** | Weibin Liao; Yinghao Zhu; Xinyuan Wang; Chengwei Pan; Yasha Wang; Liantao Ma |
| **发表时间** | 2024 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> UNet and its variants have been widely used in medical image segmentation. However, these models, especially those based on Transformer architectures, pose challenges due to their large number of parameters and computational loads, making them unsuitable for mo- bile health applications. Recently, State Space Models (SSMs), exem- plified by Mamba, have emerged as competitive alternatives to CNN and Transformer architectures. Building upon this, we employ Mamba asalightweightsubstituteforCNNandTransformerwithinUNet,aim- ingattacklingchallengesstemmingfromcomputationalresourcelimita- tionsinrealmedicalsettings.Tothisend,weintroducetheLightweight Mamba UNet (LightM-UNet) that integrates Mamba and UNet in a lightweight framework. Specifically, LightM-UNet leverages the Residual Vision Mamba Layer inapureMambafashiontoextractdeepsemantic features and model long-range spatial dependencies, with linear compu- tationalcomplexity.Extensiveexperimentsconductedontworeal-world 2D/3Ddatasetsdemonst

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：UNet及其变体是医学图像分割的基石，但基于CNN的变体存在固有的局部性限制，难以捕捉长程依赖；基于Transformer的变体通过自注意力机制解决了长程依赖问题，但引入了与图像大小相关的二次计算复杂度，导致参数量和计算开销巨大，难以部署在计算资源有限的移动医疗设备上。 (p.1-2)
- **之前方法的问题**：1）CNN-based UNet：感受野有限，建模长程依赖能力弱。2）Transformer-based UNet（如TransUNet）：自注意力机制计算复杂度高，模型参数量大。3）现有基于Mamba的尝试（如U-Mamba）：虽然结合了CNN的局部性和SSM的长程建模能力，但其混合架构本身并不轻量，参数量（173.53M）和计算量（18,057.20 GFLOPs）依然很大，不适合移动医疗场景。 (p.1-3)
- **核心矛盾**：如何在赋予UNet强大的长程依赖建模能力的同时，不引入额外的参数和计算负担？ (p.2)
## 关键贡献

1.  **提出LightM-UNet框架**：一个将Mamba与UNet集成的轻量级框架，总参数量仅约1M。在2D和3D数据集上超越了当前SOTA模型，相比nnU-Net和U-Mamba，参数量分别减少116倍和224倍。 (p.3, Table 1, 2)
2.  **提出残差视觉Mamba层 (RVM Layer)**：该层以纯Mamba方式提取深度图像特征。通过引入残差连接和可学习的调整因子（`s`），在几乎不增加新参数和计算开销的情况下，增强了SSM对视觉图像长程空间依赖的建模能力。 (p.3, 4-5)
3.  **首次倡导将Mamba用于UNet轻量化**：与U-Mamba等将Mamba与CNN混合的工作不同，本文首次提出并验证了将Mamba作为CNN和Transformer的**轻量化替代品**集成到UNet中，以解决计算资源受限问题的研究思路。 (p.3)
## 方法

- **整体框架**：LightM-UNet是一个标准的U型编码器-解码器结构。编码器由三个Encoder Block和一个Bottleneck Block组成，用于逐步提取深层特征并降低分辨率；解码器由三个Decoder Block组成，用于逐步恢复分辨率。编码器与解码器之间通过跳跃连接进行多尺度特征融合。 (p.3, Fig. 2)
- **输入输出**：输入为3D医学图像 `I ∈ R^{C×H×W×D}`。经过网络后，输出与输入同分辨率的分割掩码。 (p.3)
- **关键模块**：
    1.  **残差视觉Mamba层 (RVM Layer)**：这是特征提取的核心模块。给定输入特征 `M_{in}`，首先进行LayerNorm，然后通过**视觉状态空间模块 (VSS Module)** 建模长程依赖。接着，在残差连接中引入一个可学习的**调整因子 `s`** 来加权输入特征，与VSSM的输出相加。公式为：`fM = VSSM(LayerNorm(M_{in})) + s · M_{in}`。最后再经过LayerNorm和投影层得到输出。 (p.4-5, Fig. 2(a))
    2.  **视觉状态空间模块 (VSS Module)**：用于具体的长程空间建模。它采用双分支结构：第一分支对输入特征进行线性扩展、深度可分离卷积（DWConv）、SiLU激活、SSM处理和LayerNorm；第二分支进行线性扩展和SiLU激活。最后将两个分支的输出通过Hadamard积（逐元素相乘）聚合，并投影回原始通道数。公式为：`W_{out} = Linear(LayerNorm(SSM(SiLU(DWConv(Linear(W_{in})))))) ⊙ SiLU(Linear(W_{in}))`。 (p.5, Fig. 2(b))
- **模块连接与数据流**：
    1.  **浅层特征提取**：输入图像首先通过一个DWConv层生成32通道的浅层特征图 `F_S`。
    2.  **编码过程**：`F_S` 依次通过三个**Encoder Block**。每个Encoder Block内部包含N个连续的RVM Layer（最后一个RVM Layer会增加通道数），之后通过Max-Pooling将特征图分辨率减半、通道数加倍。
    3.  **瓶颈处理**：经过编码器后，特征图进入由四个连续RVM Layer构成的**Bottleneck Block**，进一步建模长程依赖，同时保持分辨率不变。
    3.  **解码过程**：瓶颈特征依次通过三个**Decoder Block**。每个Decoder Block首先将来自上一层的特征与来自编码器的跳跃连接特征进行加法融合，然后经过DWConv、残差连接（同样包含调整因子 `s'`）和ReLU激活进行解码，最后通过双线性插值上采样恢复分辨率。
    4.  **最终输出**：解码器输出经过一个DWConv层映射到目标类别数，并通过SoftMax函数生成最终的分割掩码。
- **训练方式**：
    - **优化器**：SGD，初始学习率1e-4。
    - **学习率调度**：PolyLRScheduler。
    - **训练轮数**：100 epochs。
    - **损失函数**：交叉熵损失与Dice损失的简单组合。
    - **数据预处理**：3D数据集（LiTs）归一化并调整为128×128×128，batch size为2；2D数据集调整为512×512，batch size为12。
- **推理流程**：与标准UNet推理流程一致，输入图像经过编码器、瓶颈、解码器生成分割图。
- **与已有方法的差异**：最大的差异在于其**轻量化设计思想**。不同于U-Mamba等采用CNN+Mamba混合块的方式，LightM-UNet在编码器和瓶颈中完全使用RVM Layer（基于Mamba）替代CNN和Transformer模块，实现了更彻底的轻量化。其RVM Layer通过残差连接和调整因子，在不增加参数的情况下增强了SSM的建模能力，这也是一个关键的结构差异。
## 实验

- **使用的数据集**：
    1.  **LiTs**：包含3D CT肝脏及肿瘤图像，用于验证模型的3D分割能力。 (p.6)
    2.  **Montgomery&Shenzhen**：包含2D胸部X光片图像，用于验证模型的2D分割能力。 (p.6)
- **对比方法**：分为三类基线模型。CNN-based: nnU-Net, SegResNet；Transformer-based: UNETR, SwinUNETR；Mamba-based: U-Mamba。 (p.6)
- **评价指标**：平均交并比（mIoU）和Dice相似系数（DSC）。 (p.6)
- **主实验结果**：
    - **在3D LiTs数据集上**：LightM-UNet（1.87M参数，457.62 GFLOPs）在**平均DSC (84.58%) 和平均mIoU (77.48%)** 上均取得最佳性能。相比nnU-Net（88.62M参数），参数量减少47.39倍，计算量减少15.82倍；相比同期U-Mamba（173.53M参数），参数量减少93倍，计算量减少39.5倍，且平均mIoU提升2.11%。尤其在小目标“肿瘤”的mIoU上提升显著（3.63%）。 (Table 1, p.6-7)
    - **在2D Montgomery&Shenzhen数据集上**：LightM-UNet（1.09M参数，267.19 GFLOPs）同样取得最佳DSC (96.17%) 和mIoU (92.74%)。相比U-Mamba，参数量减少约224倍。 (Table 2, p.7)
- **消融实验**：
    - **核心组件替换**：将RVM Layer中的VSS Module替换为3×3卷积或自注意力机制，性能均下降，且参数量/计算量显著增加，验证了Mamba模块的有效性。 (Table 3, p.7-8)
    - **关键设计移除**：在RVM Layer中分别移除调整因子（`s`）和残差连接，模型参数和计算量基本不变，但平均mIoU分别下降0.44%和0.69%，证明了这两个设计对提升性能的有效性，且符合“无额外开销增强性能”的原则。 (Table 3, p.8)
- **泛化实验**：论文在2D和3D两种模态的数据集上都进行了验证，展示了方法的泛化能力。PDF文本中未明确说明在更多数据集或不同器官任务上的泛化实验。 (p.6)
- **效率信息**：模型参数量极低（约1M），计算量（GFLOPs）相比Transformer和混合Mamba模型有量级上的降低。例如，在LiTs上比nnU-Net计算量降低15.82倍，比U-Mamba降低39.5倍。 (Table 1, 2)
## 局限

1.  **数据集与任务有限**：实验仅在两个公开数据集（肝脏CT和胸部X光）上进行，涉及的器官和任务相对单一。对于更复杂的器官结构、其他成像模态（如MRI、超声）或更精细的分割任务，其性能和轻量化优势是否依然显著，需要进一步验证。 (p.6)
2.  **轻量化可能伴随性能上限**：模型参数仅1M，虽然在报告的指标上超越了基线，但在处理极度复杂或需要超精细分割的任务时，其模型容量可能成为瓶颈。论文未讨论在需要更高容量模型的任务上的权衡。
3.  **计算成本评估平台**：所有实验在单一的Quadro RTX 8000 GPU上进行。该GPU性能强大，其报告的推理速度或延迟可能与实际部署的移动或嵌入式设备（如手机、边缘计算单元）有较大差异。PDF文本中未明确说明在实际资源受限设备上的运行效率。
4.  **架构假设**：其轻量化优势建立在“Mamba能高效替代CNN和Transformer”的假设上。对于某些特定任务，CNN的归纳偏置（如平移不变性）或Transformer的全局注意力可能仍是不可或缺的，此方法可能不适用。
## 个人评论

1.  **验证了Mamba作为轻量化核心组件的潜力**：它清晰地展示了，不同于将Mamba视为一个与CNN并列的“增强模块”，将其作为CNN和Transformer的“**替代品**”来构建网络主干，能够实现极致的参数和计算效率。这为设计面向边缘设备或移动医疗的模型提供了新思路。
2.  **提出了简单有效的RVM层设计**：该设计思想很有启发性——利用轻量化的调整因子和残差连接，对标准SSM模块进行“微调”，在零额外参数开销下提升其视觉建模能力。这种“低成本增强”策略在其他轻量化网络设计中也很有借鉴价值。
3.  **实验对比全面，结论有说服力**：不仅与经典的CNN、Transformer模型对比，还与同期的Mamba模型（U-Mamba）对比，并通过详实的消融实验（组件替换、关键设计移除）验证了自己每个设计选择的有效性，使得论文的结论更加扎实可靠。

### 使用建议

- **如果快速了解**：重点阅读**摘要**、**图1**（性能-参数可视化）、**表1和表2**（核心结果对比）以及**结论**部分。这些部分能快速把握论文的核心思想、主要成果和贡献。
- **如果复现**：必须精读**2. Methodologies**部分，特别是**2.1 Architecture Overview**（整体架构）、**2.2 Encoder Block**（RVM Layer和VSS Module的公式与描述）以及**3. Experiments**中的“Datasets and Experimental Setups”段落（超参数、训练细节）。Fig. 2的结构图也至关重要。
- **如果借鉴创新点**：应深入理解**RVM Layer (Section 2.2)** 的设计，特别是其如何通过调整因子和残差连接优化SSM模块。其将Mamba视为轻量化主干而非混合组件的思想，是值得借鉴的核心创新点。
- **如果写Related Work**：可将其放在“**轻量化医学图像分割网络**”或“**基于状态空间模型（SSM/Mamba）的视觉模型**”这两个类别下进行引用和讨论。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A1_医学图像_分割]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**医学图像分割**领域的**轻量化模型设计**研究方向。具体解决的是在移动健康等计算资源受限的真实医疗场景下，现有基于CNN和Transformer的UNet变体模型参数量和计算负载过大的问题。论文旨在探索将新兴的状态空间模型Mamba作为CNN和Transformer的轻量化替代，以构建参数少、计算高效的分割网络。该主题适合归类于 `A1_医学图像_分割`，特别是其中关于轻量化、高效模型设计的子方向。

## 2. 一句话总结
本文提出LightM-UNet，将Mamba作为CNN和Transformer的轻量化替代引入UNet框架，以极低的参数和计算成本实现了先进的医学图像分割性能。

## 3. 背景与问题
- **为什么要做**：UNet及其变体是医学图像分割的基石，但基于CNN的变体存在固有的局部性限制，难以捕捉长程依赖；基于Transformer的变体通过自注意力机制解决了长程依赖问题，但引入了与图像大小相关的二次计算复杂度，导致参数量和计算开销巨大，难以部署在计算资源有限的移动医疗设备上。 (p.1-2)
- **之前方法的问题**：1）CNN-based UNet：感受野有限，建模长程依赖能力弱。2）Transformer-based UNet（如TransUNet）：自注意力机制计算复杂度高，模型参数量大。3）现有基于Mamba的尝试（如U-Mamba）：虽然结合了CNN的局部性和SSM的长程建模能力，但其混合架构本身并不轻量，参数量（173.53M）和计算量（18,057.20 GFLOPs）依然很大，不适合移动医疗场景。 (p.1-3)
- **核心矛盾**：如何在赋予UNet强大的长程依赖建模能力的同时，不引入额外的参数和计算负担？ (p.2)

## 4. 核心贡献
1.  **提出LightM-UNet框架**：一个将Mamba与UNet集成的轻量级框架，总参数量仅约1M。在2D和3D数据集上超越了当前SOTA模型，相比nnU-Net和U-Mamba，参数量分别减少116倍和224倍。 (p.3, Table 1, 2)
2.  **提出残差视觉Mamba层 (RVM Layer)**：该层以纯Mamba方式提取深度图像特征。通过引入残差连接和可学习的调整因子（`s`），在几乎不增加新参数和计算开销的情况下，增强了SSM对视觉图像长程空间依赖的建模能力。 (p.3, 4-5)
3.  **首次倡导将Mamba用于UNet轻量化**：与U-Mamba等将Mamba与CNN混合的工作不同，本文首次提出并验证了将Mamba作为CNN和Transformer的**轻量化替代品**集成到UNet中，以解决计算资源受限问题的研究思路。 (p.3)

## 5. 方法详解
- **整体框架**：LightM-UNet是一个标准的U型编码器-解码器结构。编码器由三个Encoder Block和一个Bottleneck Block组成，用于逐步提取深层特征并降低分辨率；解码器由三个Decoder Block组成，用于逐步恢复分辨率。编码器与解码器之间通过跳跃连接进行多尺度特征融合。 (p.3, Fig. 2)
- **输入输出**：输入为3D医学图像 `I ∈ R^{C×H×W×D}`。经过网络后，输出与输入同分辨率的分割掩码。 (p.3)
- **关键模块**：
    1.  **残差视觉Mamba层 (RVM Layer)**：这是特征提取的核心模块。给定输入特征 `M_{in}`，首先进行LayerNorm，然后通过**视觉状态空间模块 (VSS Module)** 建模长程依赖。接着，在残差连接中引入一个可学习的**调整因子 `s`** 来加权输入特征，与VSSM的输出相加。公式为：`fM = VSSM(LayerNorm(M_{in})) + s · M_{in}`。最后再经过LayerNorm和投影层得到输出。 (p.4-5, Fig. 2(a))
    2.  **视觉状态空间模块 (VSS Module)**：用于具体的长程空间建模。它采用双分支结构：第一分支对输入特征进行线性扩展、深度可分离卷积（DWConv）、SiLU激活、SSM处理和LayerNorm；第二分支进行线性扩展和SiLU激活。最后将两个分支的输出通过Hadamard积（逐元素相乘）聚合，并投影回原始通道数。公式为：`W_{out} = Linear(LayerNorm(SSM(SiLU(DWConv(Linear(W_{in})))))) ⊙ SiLU(Linear(W_{in}))`。 (p.5, Fig. 2(b))
- **模块连接与数据流**：
    1.  **浅层特征提取**：输入图像首先通过一个DWConv层生成32通道的浅层特征图 `F_S`。
    2.  **编码过程**：`F_S` 依次通过三个**Encoder Block**。每个Encoder Block内部包含N个连续的RVM Layer（最后一个RVM Layer会增加通道数），之后通过Max-Pooling将特征图分辨率减半、通道数加倍。
    3.  **瓶颈处理**：经过编码器后，特征图进入由四个连续RVM Layer构成的**Bottleneck Block**，进一步建模长程依赖，同时保持分辨率不变。
    3.  **解码过程**：瓶颈特征依次通过三个**Decoder Block**。每个Decoder Block首先将来自上一层的特征与来自编码器的跳跃连接特征进行加法融合，然后经过DWConv、残差连接（同样包含调整因子 `s'`）和ReLU激活进行解码，最后通过双线性插值上采样恢复分辨率。
    4.  **最终输出**：解码器输出经过一个DWConv层映射到目标类别数，并通过SoftMax函数生成最终的分割掩码。
- **训练方式**：
    - **优化器**：SGD，初始学习率1e-4。
    - **学习率调度**：PolyLRScheduler。
    - **训练轮数**：100 epochs。
    - **损失函数**：交叉熵损失与Dice损失的简单组合。
    - **数据预处理**：3D数据集（LiTs）归一化并调整为128×128×128，batch size为2；2D数据集调整为512×512，batch size为12。
- **推理流程**：与标准UNet推理流程一致，输入图像经过编码器、瓶颈、解码器生成分割图。
- **与已有方法的差异**：最大的差异在于其**轻量化设计思想**。不同于U-Mamba等采用CNN+Mamba混合块的方式，LightM-UNet在编码器和瓶颈中完全使用RVM Layer（基于Mamba）替代CNN和Transformer模块，实现了更彻底的轻量化。其RVM Layer通过残差连接和调整因子，在不增加参数的情况下增强了SSM的建模能力，这也是一个关键的结构差异。

## 6. 实验与结果
- **使用的数据集**：
    1.  **LiTs**：包含3D CT肝脏及肿瘤图像，用于验证模型的3D分割能力。 (p.6)
    2.  **Montgomery&Shenzhen**：包含2D胸部X光片图像，用于验证模型的2D分割能力。 (p.6)
- **对比方法**：分为三类基线模型。CNN-based: nnU-Net, SegResNet；Transformer-based: UNETR, SwinUNETR；Mamba-based: U-Mamba。 (p.6)
- **评价指标**：平均交并比（mIoU）和Dice相似系数（DSC）。 (p.6)
- **主实验结果**：
    - **在3D LiTs数据集上**：LightM-UNet（1.87M参数，457.62 GFLOPs）在**平均DSC (84.58%) 和平均mIoU (77.48%)** 上均取得最佳性能。相比nnU-Net（88.62M参数），参数量减少47.39倍，计算量减少15.82倍；相比同期U-Mamba（173.53M参数），参数量减少93倍，计算量减少39.5倍，且平均mIoU提升2.11%。尤其在小目标“肿瘤”的mIoU上提升显著（3.63%）。 (Table 1, p.6-7)
    - **在2D Montgomery&Shenzhen数据集上**：LightM-UNet（1.09M参数，267.19 GFLOPs）同样取得最佳DSC (96.17%) 和mIoU (92.74%)。相比U-Mamba，参数量减少约224倍。 (Table 2, p.7)
- **消融实验**：
    - **核心组件替换**：将RVM Layer中的VSS Module替换为3×3卷积或自注意力机制，性能均下降，且参数量/计算量显著增加，验证了Mamba模块的有效性。 (Table 3, p.7-8)
    - **关键设计移除**：在RVM Layer中分别移除调整因子（`s`）和残差连接，模型参数和计算量基本不变，但平均mIoU分别下降0.44%和0.69%，证明了这两个设计对提升性能的有效性，且符合“无额外开销增强性能”的原则。 (Table 3, p.8)
- **泛化实验**：论文在2D和3D两种模态的数据集上都进行了验证，展示了方法的泛化能力。PDF文本中未明确说明在更多数据集或不同器官任务上的泛化实验。 (p.6)
- **效率信息**：模型参数量极低（约1M），计算量（GFLOPs）相比Transformer和混合Mamba模型有量级上的降低。例如，在LiTs上比nnU-Net计算量降低15.82倍，比U-Mamba降低39.5倍。 (Table 1, 2)

## 7. 这篇论文真正有价值的地方
1.  **验证了Mamba作为轻量化核心组件的潜力**：它清晰地展示了，不同于将Mamba视为一个与CNN并列的“增强模块”，将其作为CNN和Transformer的“**替代品**”来构建网络主干，能够实现极致的参数和计算效率。这为设计面向边缘设备或移动医疗的模型提供了新思路。
2.  **提出了简单有效的RVM层设计**：该设计思想很有启发性——利用轻量化的调整因子和残差连接，对标准SSM模块进行“微调”，在零额外参数开销下提升其视觉建模能力。这种“低成本增强”策略在其他轻量化网络设计中也很有借鉴价值。
3.  **实验对比全面，结论有说服力**：不仅与经典的CNN、Transformer模型对比，还与同期的Mamba模型（U-Mamba）对比，并通过详实的消融实验（组件替换、关键设计移除）验证了自己每个设计选择的有效性，使得论文的结论更加扎实可靠。

## 8. 局限与问题
1.  **数据集与任务有限**：实验仅在两个公开数据集（肝脏CT和胸部X光）上进行，涉及的器官和任务相对单一。对于更复杂的器官结构、其他成像模态（如MRI、超声）或更精细的分割任务，其性能和轻量化优势是否依然显著，需要进一步验证。 (p.6)
2.  **轻量化可能伴随性能上限**：模型参数仅1M，虽然在报告的指标上超越了基线，但在处理极度复杂或需要超精细分割的任务时，其模型容量可能成为瓶颈。论文未讨论在需要更高容量模型的任务上的权衡。
3.  **计算成本评估平台**：所有实验在单一的Quadro RTX 8000 GPU上进行。该GPU性能强大，其报告的推理速度或延迟可能与实际部署的移动或嵌入式设备（如手机、边缘计算单元）有较大差异。PDF文本中未明确说明在实际资源受限设备上的运行效率。
4.  **架构假设**：其轻量化优势建立在“Mamba能高效替代CNN和Transformer”的假设上。对于某些特定任务，CNN的归纳偏置（如平移不变性）或Transformer的全局注意力可能仍是不可或缺的，此方法可能不适用。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**摘要**、**图1**（性能-参数可视化）、**表1和表2**（核心结果对比）以及**结论**部分。这些部分能快速把握论文的核心思想、主要成果和贡献。
- **如果复现**：必须精读**2. Methodologies**部分，特别是**2.1 Architecture Overview**（整体架构）、**2.2 Encoder Block**（RVM Layer和VSS Module的公式与描述）以及**3. Experiments**中的“Datasets and Experimental Setups”段落（超参数、训练细节）。Fig. 2的结构图也至关重要。
- **如果借鉴创新点**：应深入理解**RVM Layer (Section 2.2)** 的设计，特别是其如何通过调整因子和残差连接优化SSM模块。其将Mamba视为轻量化主干而非混合组件的思想，是值得借鉴的核心创新点。
- **如果写Related Work**：可将其放在“**轻量化医学图像分割网络**”或“**基于状态空间模型（SSM/Mamba）的视觉模型**”这两个类别下进行引用和讨论。

## 10. 和其他论文的关系
根据库中主题 `A1_医学图像_分割` 和文件名，这篇论文很可能与以下工作相关：
- `[[U-Mamba]]`：本文直接对比并超越的同期Mamba-UNet混合架构。
- `[[TransUNet]]`：引入Transformer到UNet的开创性工作，本文将其作为Transformer-based基线之一。
- `[[nnU-Net]]`：著名的自配置分割框架，本文作为CNN-based的主要基线。
- `[[SwinUNETR]]`：基于Swin Transformer的3D分割模型，本文将其作为更强的Transformer基线。
- `[[CE-Net]]` / `[[Attention Gated Networks]]`：采用空洞卷积或注意力机制来增强UNet感受野的早期工作，属于本文背景中提到的“尝试解决CNN局部性限制”的方法。

## 11. 关键词
医学图像分割，轻量级模型，状态空间模型 (SSM)，Mamba，UNet，深度学习，移动医疗，长程依赖，残差学习，3D分割，2D分割。

## 12. 可信度说明
本精读笔记**完全基于**提供的PDF提取文本（前10页）生成。笔记中所有观点、数据、方法描述均直接来源于文本内容。提取文本质量较高，包含了论文的标题、摘要、引言、方法、实验、结论和参考文献列表，使得能够全面覆盖论文的核心信息。对于文本中未提供的细节（如在移动设备上的实际推理速度、更多数据集的验证结果），已在相应位置明确标注“PDF文本中未明确说明”。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2504 字符/页)); 来源缓存: `.paper-cache/extracts/LightM-UNet.txt` (10/10 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
