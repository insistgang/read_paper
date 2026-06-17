---
title: "CM-UNet: Hybrid CNN-Mamba UNet for Remote"
authors:
  - "Mushui Liu"
  - "Jun Dan"
  - "Ziqian Lu"
  - "Yunlong Yu"
  - "Yingming Li"
  - "Xi Li"
year: 2015
venue: for remote sensing image semantic segmentation are suboptimal
doi: 
pdf: [[MSAA.pdf]]
primary_topic: B_注意力算子模块
topics:
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
extract_cache: .paper-cache/extracts/MSAA.txt
---

# CM-UNet: Hybrid CNN-Mamba UNet for Remote

## 基本信息
- **PDF**: [[MSAA.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | CM-UNet: Hybrid CNN-Mamba UNet for Remote |
| **作者** | Mushui Liu; Jun Dan; Ziqian Lu; Yunlong Yu; Yingming Li; Xi Li |
| **发表时间** | 2015 |
| **刊物/会议** | for remote sensing image semantic segmentation are suboptimal |
| **DOI** | 未明确 |

## 摘要

> —Due to the large-scale image size and object vari- Convolution Kernel Self-Attention State Space Model ations, current CNN-based and Transformer-based approaches for remote sensing image semantic segmentation are suboptimal Local Contextual for capturing the long-range dependency or limited to the Information complex computational complexity. In this paper, we propose CM-UNet,comprisingaCNN-basedencoderforextractinglocal image features and a Mamba-based decoder for aggregating Glo I b n a fo l r C m on at t i e o x n tual Glo I b n a fo l r C m on at t i e o x n tual andintegratingglobalinformation,facilitatingefficientsemantic segmentationofremotesensingimages.Specifically,aCSMamba blockisintroducedtobuildthecoresegmentationdecoder,which (a （ ) a C ） N CN N N ( （ b) b） T T r r a an n sf s or f m o e r r mer (c （ ) c S ） S SS M M employs channel and spatial attention as the gate activation condition of the vanilla Mamba to enhance the feature inter- Fig.1. Illustrationofdifferentarchi

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：遥感图像具有尺寸大、目标变化多样的特点。现有的基于CNN或Transformer的UNet架构在处理这类图像时存在局限：CNN可能难以充分捕获全局上下文信息，而Transformer虽然能建模全局依赖，但其自注意力机制的计算复杂度（随序列长度呈平方增长）在处理大规模遥感图像时效率低下。
- **之前方法的问题**：作者指出，现有的基于Mamba的遥感图像处理方法（如PanMamba， RMamba等）要么直接替换网络并从头训练，要么直接应用预训练的Mamba模块，但都“很少考虑遥感图像中局部与全局信息的融合”，可能无法充分利用预训练CNN模型提供的特征。
- **核心矛盾**：如何在保持计算效率的同时，有效捕获并融合遥感图像中的**局部细节信息与全局长程依赖信息**，以提升语义分割精度。
## 关键贡献

1. 提出了一个名为CM-UNet的混合框架，该框架利用CNN编码器提取局部特征，并利用基于Mamba的解码器聚合全局信息，以实现高效的遥感图像语义分割。
2. 设计了CSMamba解码器块，该模块将**通道和空间注意力**作为激活条件融入原始的Mamba模块，以增强特征交互和全局-局部信息融合。
3. 引入了一个**多尺度注意力聚合（MSAA）模块**，用于融合CNN编码器不同尺度的特征，替代传统UNet的简单跳跃连接。
4. 采用了**多输出监督策略**，在解码器的每个CSMamba块处施加监督，以逐步生成更精细的分割结果。
5. 在ISPRS Potsdam、ISPRS Vaihingen和LoveDA三个公开的遥感分割数据集上进行了广泛实验，验证了方法的优越性。
## 方法

### 整体框架
CM-UNet遵循经典的U型编码器-解码器结构，如图2(a)所示。
- **编码器**：采用ResNet（如R18）作为骨干网络，提取多尺度（F1, F2, F3）的局部纹理特征。
- **解码器**：由一系列设计的CSMamba块构成，用于聚合语义信息。
- **连接部分**：引入**MSAA模块**替代原始的跳跃连接，对编码器输出的多尺度特征进行融合与优化，再送入解码器。

### 输入与输出
- **输入**：遥感图像。
- **输出**：像素级的语义分割图。模型在解码器的多个阶段（每个CSMamba块后）都产生中间输出，最终通过多输出监督获得最终分割结果。

### 关键模块详解
1. **CSMamba块**（核心，图2(b)）：
   - 这是解码器的基本单元，旨在高效捕获长程依赖并融合注意力信息。
   - 输入特征 `X ∈ R^{H×W×C}` 经过两个并行分支：
     - **分支1**：特征通道通过线性层扩展至 `λC`（λ为扩展因子），经过深度卷积（DWConv）、SiLU激活、**2D-SSM模块**和层归一化（LN）。
     - **分支2**：输入特征通过**通道与空间注意力（CS）模块**进行特征选择，然后经过SiLU激活。
   - 两个分支的输出通过**Hadamard乘积（⊙）** 进行融合。
   - 最后，通过线性层将通道数投影回 `C`，得到输出 `X_out`，形状与输入 `X` 相同。
   - **数学公式**：
     ```
     X1 = LN(2D-SSM(SiLU(DWConv(Linear(X)))))
     X2 = SiLU(CS(X))
     X_out = Linear(X1 ⊙ X2)
     ```
   - **2D-SSM模块**（图2(c)）：为适应图像数据，将2D特征图展平为1D序列，并沿**四个方向**（左上→右下， 右下→左上， 右上→左下， 左下→右上）进行扫描。每个方向通过选择性状态空间模型捕获长程依赖，最后合并四个方向的序列以恢复2D结构。
   - **通道与空间注意力（CS）**：作为Mamba块的“门控激活条件”，用于在分支2中对输入特征进行通道和空间维度的自适应加权，实现特征选择。

2. **多尺度注意力聚合（MSAA）模块**（图3）：
   - 用于融合编码器不同阶段的特征（F1, F2, F3）。首先，将相邻尺度的特征进行拼接：`ˆF_i = Concat(F_i, F_{i-1}, F_{i+1})`。
   - 模块内部包含**两条路径**：
     - **空间聚合路径**：通过1×1卷积进行通道投影降低维度，然后进行**多尺度融合**（使用不同尺寸的卷积核，如3×3, 5×5, 7×7进行求和），接着使用平均池化和最大池化进行空间特征聚合，再通过7×7卷积和Sigmoid激活生成空间注意力图，并与原特征进行逐元素乘法。
     - **通道聚合路径**：使用全局平均池化将空间维度降至1×1，然后通过1×1卷积和ReLU激活生成通道注意力图，并扩展至与输入相同尺寸。
   - 两条路径的输出**相加融合**，得到增强后的特征图，富含空间和通道维度的上下文信息。

3. **多输出监督**：
   - 在解码器的每个CSMamba块 `i` 处，其特征 `F_cs` 通过一个卷积层映射为类别预测图 `p_i`，用于计算损失。
   - **训练损失**：使用**交叉熵损失**和**Dice损失**的组合进行训练。

### 训练与推理
- **训练**：使用AdamW优化器，基础学习率6e-4，采用余弦策略调整。输入图像随机裁剪为512×512，并采用多种数据增强（随机缩放、翻转、旋转）。训练100个epoch，批大小16。
- **推理**：使用测试时增强（TTA），如垂直和水平翻转。

### 与已有方法的差异
与传统的基于Transformer（如Swin Transformer）的UNet相比，CM-UNet的核心优势在于其解码器使用**CSMamba块**替代了Transformer块。Mamba基于状态空间模型（SSM），能够以**线性时间复杂度**建模长程依赖，而自注意力机制的复杂度是序列长度的平方，因此CM-UNet在处理大规模图像时理论上更高效。同时，通过融入通道和空间注意力，弥补了Mamba在特征选择上的不足，实现了更有效的全局-局部信息融合。
## 实验

- **数据集**：ISPRS Potsdam、ISPRS Vaihingen、LoveDA。
- **对比方法**：DeepLabV3+, DANet, ABCNet, BANet, CMTFNet, UNetformer, ESDINet, Segmenter等，这些方法使用了R18, VMamba, Swin-Base等骨干。
- **评价指标**：平均F1分数（mF1）、平均交并比（mIoU）、总体精度（OA）。
- **主实验结果**：
    - **ISPRS Potsdam**：CM-UNet达到mF1 93.05%， OA 91.86%， mIoU 87.21%。在mIoU上比UNetformer高0.41%，比DANet和Segmenter分别高6.91%和6.51%（p.3, 表I）。
    - **ISPRS Vaihingen**：CM-UNet达到mIoU 85.48%， mF1 92.01%， OA 93.81%。在mIoU上大幅超越所有对比方法（2.78%至16.08%），在Imp.surf.类别上F1比UNetformer高4.42%（p.3-4, 表II）。
    - **LoveDA**：CM-UNet在Urban子集上达到mIoU 52.17%（p.4, 表III）。
- **消融实验**（表IV）：
    - 仅使用MSAA模块：mIoU从83.53%提升至84.45%。
    - 仅使用多输出监督：mIoU提升至83.91%。
    - **同时使用MSAA和多输出**：取得最佳性能（mIoU 85.48%），证明了二者协同作用的有效性。
- **模型复杂度分析**（表V）：
    - 以在Vaihingen数据集上的结果为例，CM-UNet的FLOPs为6.01G，参数量为12.89M，内存占用366.33MB。在参数量与UNetformer相近（12.89M vs 11.69M）的情况下，其mIoU（85.48%）显著优于后者（82.70%），展现了良好的性价比。
## 局限

1. **方法场景限制**：模型设计主要针对大规模遥感图像的语义分割，对于小规模图像或需要实时性极高的场景，Mamba及其2D扫描带来的序列化处理是否仍具优势，需要进一步验证。
2. **实验充分性**：论文在三个数据集上进行了验证，但缺乏更多样化、更具挑战性的遥感基准测试（如更复杂的场景、不同的传感器模态）。
3. **计算成本细节**：虽然报告了FLOPs和参数量，但对于Mamba（2D-SSM）的实际推理速度、以及CSMamba块中各部分（如注意力计算、四方向扫描）的具体开销分析不够深入。
4. **复现风险**：论文依赖于Mamba这一较新的模型架构，其官方实现和社区支持的稳定性可能影响复现。此外，CSMamba块中通道扩展因子λ等超参数的设定未在文本中详细说明。
5. **与纯Mamba方法对比**：文本中未提供与RS3Mamba等纯Mamba或Vision Mamba方法在相同骨干下的详细公平对比（如表II中RS3Mamba使用的是R18-Mamba骨干），难以严格剥离混合架构带来的具体增益。
## 个人评论

1. **架构创新思路**：提出了“CNN编码器 + Mamba解码器”的混合架构范式，为高效处理大规模图像（如遥感）提供了新思路。它充分利用了CNN在提取局部特征上的成熟性和Mamba在长程建模上的高效性。
2. **模块融合启发**：CSMamba块的设计展示了如何将传统的**注意力机制（CS Attention）** 与新兴的**状态空间模型（Mamba）** 有机结合。这种“门控”或“条件激活”的思想，为改进或设计新的基础模块（尤其是`B_注意力算子模块`）提供了具体范例。
3. **跳连优化方案**：MSAA模块提供了一个比简单拼接或相加更有效的特征融合方案，通过显式地建模空间和通道注意力来优化跳跃连接，这对任何编码器-解码器网络都有借鉴意义。
4. **系统化设计**：论文没有只关注单个点，而是从模块设计（CSMamba, MSAA）、训练策略（多输出监督）到实验验证进行了完整呈现，是一个“小而精”的系统化工作范例。

### 使用建议

- **快速了解**：阅读**摘要（Abstract）** 和**图2**，可以快速把握CM-UNet的整体架构、核心模块（CSMamba, MSAA）以及混合设计思路。
- **如果复现**：重点精读**II. METHODOLOGY**部分，特别是**CSMamba块（公式1）** 和**MSAA模块（图3）** 的详细描述，以及**III. EXPERIMENTS**中的**Implementation details**部分。
- **如果借鉴创新点**：
    - 若关注**注意力与Mamba的结合**，应深入学习CSMamba块中通道空间注意力作为门控条件的设计。
    - 若关注**多尺度特征融合**，应学习MSAA模块如何通过双路径（空间、通道）聚合不同尺度特征。
    - 若关注**训练策略**，可借鉴其多输出监督的方法。
- **如果写Related Work**：可放在以下几个部分：1）遥感图像语义分割的UNet改进工作；2）Mamba/Vision State Space Model在视觉任务中的应用；3）结合CNN与Transformer/Mamba的混合架构研究；4）通道/空间注意力机制的应用。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**计算机视觉**领域的**遥感图像语义分割**方向。它旨在解决现有基于CNN和Transformer的方法在处理大规模遥感图像时，难以高效捕获长程依赖或计算复杂度过高的问题。其核心主题是设计一个**混合CNN-Mamba的UNet架构**，因此适合放在**B_注意力算子模块**这一主题下，因为它核心的CSMamba块中创新性地融合了通道与空间注意力机制。

## 2. 一句话总结
本文提出CM-UNet，一个混合CNN-Mamba的UNet框架，通过设计CSMamba解码器块和MSAA多尺度注意力聚合模块，高效融合CNN的局部特征与Mamba的全局建模能力，以提升遥感图像语义分割的性能。

## 3. 背景与问题
- **为什么要做**：遥感图像具有尺寸大、目标变化多样的特点。现有的基于CNN或Transformer的UNet架构在处理这类图像时存在局限：CNN可能难以充分捕获全局上下文信息，而Transformer虽然能建模全局依赖，但其自注意力机制的计算复杂度（随序列长度呈平方增长）在处理大规模遥感图像时效率低下。
- **之前方法的问题**：作者指出，现有的基于Mamba的遥感图像处理方法（如PanMamba， RMamba等）要么直接替换网络并从头训练，要么直接应用预训练的Mamba模块，但都“很少考虑遥感图像中局部与全局信息的融合”，可能无法充分利用预训练CNN模型提供的特征。
- **核心矛盾**：如何在保持计算效率的同时，有效捕获并融合遥感图像中的**局部细节信息与全局长程依赖信息**，以提升语义分割精度。

## 4. 核心贡献
1. 提出了一个名为CM-UNet的混合框架，该框架利用CNN编码器提取局部特征，并利用基于Mamba的解码器聚合全局信息，以实现高效的遥感图像语义分割。
2. 设计了CSMamba解码器块，该模块将**通道和空间注意力**作为激活条件融入原始的Mamba模块，以增强特征交互和全局-局部信息融合。
3. 引入了一个**多尺度注意力聚合（MSAA）模块**，用于融合CNN编码器不同尺度的特征，替代传统UNet的简单跳跃连接。
4. 采用了**多输出监督策略**，在解码器的每个CSMamba块处施加监督，以逐步生成更精细的分割结果。
5. 在ISPRS Potsdam、ISPRS Vaihingen和LoveDA三个公开的遥感分割数据集上进行了广泛实验，验证了方法的优越性。

## 5. 方法详解
### 整体框架
CM-UNet遵循经典的U型编码器-解码器结构，如图2(a)所示。
- **编码器**：采用ResNet（如R18）作为骨干网络，提取多尺度（F1, F2, F3）的局部纹理特征。
- **解码器**：由一系列设计的CSMamba块构成，用于聚合语义信息。
- **连接部分**：引入**MSAA模块**替代原始的跳跃连接，对编码器输出的多尺度特征进行融合与优化，再送入解码器。

### 输入与输出
- **输入**：遥感图像。
- **输出**：像素级的语义分割图。模型在解码器的多个阶段（每个CSMamba块后）都产生中间输出，最终通过多输出监督获得最终分割结果。

### 关键模块详解
1. **CSMamba块**（核心，图2(b)）：
   - 这是解码器的基本单元，旨在高效捕获长程依赖并融合注意力信息。
   - 输入特征 `X ∈ R^{H×W×C}` 经过两个并行分支：
     - **分支1**：特征通道通过线性层扩展至 `λC`（λ为扩展因子），经过深度卷积（DWConv）、SiLU激活、**2D-SSM模块**和层归一化（LN）。
     - **分支2**：输入特征通过**通道与空间注意力（CS）模块**进行特征选择，然后经过SiLU激活。
   - 两个分支的输出通过**Hadamard乘积（⊙）** 进行融合。
   - 最后，通过线性层将通道数投影回 `C`，得到输出 `X_out`，形状与输入 `X` 相同。
   - **数学公式**：
     ```
     X1 = LN(2D-SSM(SiLU(DWConv(Linear(X)))))
     X2 = SiLU(CS(X))
     X_out = Linear(X1 ⊙ X2)
     ```
   - **2D-SSM模块**（图2(c)）：为适应图像数据，将2D特征图展平为1D序列，并沿**四个方向**（左上→右下， 右下→左上， 右上→左下， 左下→右上）进行扫描。每个方向通过选择性状态空间模型捕获长程依赖，最后合并四个方向的序列以恢复2D结构。
   - **通道与空间注意力（CS）**：作为Mamba块的“门控激活条件”，用于在分支2中对输入特征进行通道和空间维度的自适应加权，实现特征选择。

2. **多尺度注意力聚合（MSAA）模块**（图3）：
   - 用于融合编码器不同阶段的特征（F1, F2, F3）。首先，将相邻尺度的特征进行拼接：`ˆF_i = Concat(F_i, F_{i-1}, F_{i+1})`。
   - 模块内部包含**两条路径**：
     - **空间聚合路径**：通过1×1卷积进行通道投影降低维度，然后进行**多尺度融合**（使用不同尺寸的卷积核，如3×3, 5×5, 7×7进行求和），接着使用平均池化和最大池化进行空间特征聚合，再通过7×7卷积和Sigmoid激活生成空间注意力图，并与原特征进行逐元素乘法。
     - **通道聚合路径**：使用全局平均池化将空间维度降至1×1，然后通过1×1卷积和ReLU激活生成通道注意力图，并扩展至与输入相同尺寸。
   - 两条路径的输出**相加融合**，得到增强后的特征图，富含空间和通道维度的上下文信息。

3. **多输出监督**：
   - 在解码器的每个CSMamba块 `i` 处，其特征 `F_cs` 通过一个卷积层映射为类别预测图 `p_i`，用于计算损失。
   - **训练损失**：使用**交叉熵损失**和**Dice损失**的组合进行训练。

### 训练与推理
- **训练**：使用AdamW优化器，基础学习率6e-4，采用余弦策略调整。输入图像随机裁剪为512×512，并采用多种数据增强（随机缩放、翻转、旋转）。训练100个epoch，批大小16。
- **推理**：使用测试时增强（TTA），如垂直和水平翻转。

### 与已有方法的差异
与传统的基于Transformer（如Swin Transformer）的UNet相比，CM-UNet的核心优势在于其解码器使用**CSMamba块**替代了Transformer块。Mamba基于状态空间模型（SSM），能够以**线性时间复杂度**建模长程依赖，而自注意力机制的复杂度是序列长度的平方，因此CM-UNet在处理大规模图像时理论上更高效。同时，通过融入通道和空间注意力，弥补了Mamba在特征选择上的不足，实现了更有效的全局-局部信息融合。

## 6. 实验与结果
- **数据集**：ISPRS Potsdam、ISPRS Vaihingen、LoveDA。
- **对比方法**：DeepLabV3+, DANet, ABCNet, BANet, CMTFNet, UNetformer, ESDINet, Segmenter等，这些方法使用了R18, VMamba, Swin-Base等骨干。
- **评价指标**：平均F1分数（mF1）、平均交并比（mIoU）、总体精度（OA）。
- **主实验结果**：
    - **ISPRS Potsdam**：CM-UNet达到mF1 93.05%， OA 91.86%， mIoU 87.21%。在mIoU上比UNetformer高0.41%，比DANet和Segmenter分别高6.91%和6.51%（p.3, 表I）。
    - **ISPRS Vaihingen**：CM-UNet达到mIoU 85.48%， mF1 92.01%， OA 93.81%。在mIoU上大幅超越所有对比方法（2.78%至16.08%），在Imp.surf.类别上F1比UNetformer高4.42%（p.3-4, 表II）。
    - **LoveDA**：CM-UNet在Urban子集上达到mIoU 52.17%（p.4, 表III）。
- **消融实验**（表IV）：
    - 仅使用MSAA模块：mIoU从83.53%提升至84.45%。
    - 仅使用多输出监督：mIoU提升至83.91%。
    - **同时使用MSAA和多输出**：取得最佳性能（mIoU 85.48%），证明了二者协同作用的有效性。
- **模型复杂度分析**（表V）：
    - 以在Vaihingen数据集上的结果为例，CM-UNet的FLOPs为6.01G，参数量为12.89M，内存占用366.33MB。在参数量与UNetformer相近（12.89M vs 11.69M）的情况下，其mIoU（85.48%）显著优于后者（82.70%），展现了良好的性价比。

## 7. 这篇论文真正有价值的地方
1. **架构创新思路**：提出了“CNN编码器 + Mamba解码器”的混合架构范式，为高效处理大规模图像（如遥感）提供了新思路。它充分利用了CNN在提取局部特征上的成熟性和Mamba在长程建模上的高效性。
2. **模块融合启发**：CSMamba块的设计展示了如何将传统的**注意力机制（CS Attention）** 与新兴的**状态空间模型（Mamba）** 有机结合。这种“门控”或“条件激活”的思想，为改进或设计新的基础模块（尤其是`B_注意力算子模块`）提供了具体范例。
3. **跳连优化方案**：MSAA模块提供了一个比简单拼接或相加更有效的特征融合方案，通过显式地建模空间和通道注意力来优化跳跃连接，这对任何编码器-解码器网络都有借鉴意义。
4. **系统化设计**：论文没有只关注单个点，而是从模块设计（CSMamba, MSAA）、训练策略（多输出监督）到实验验证进行了完整呈现，是一个“小而精”的系统化工作范例。

## 8. 局限与问题
1. **方法场景限制**：模型设计主要针对大规模遥感图像的语义分割，对于小规模图像或需要实时性极高的场景，Mamba及其2D扫描带来的序列化处理是否仍具优势，需要进一步验证。
2. **实验充分性**：论文在三个数据集上进行了验证，但缺乏更多样化、更具挑战性的遥感基准测试（如更复杂的场景、不同的传感器模态）。
3. **计算成本细节**：虽然报告了FLOPs和参数量，但对于Mamba（2D-SSM）的实际推理速度、以及CSMamba块中各部分（如注意力计算、四方向扫描）的具体开销分析不够深入。
4. **复现风险**：论文依赖于Mamba这一较新的模型架构，其官方实现和社区支持的稳定性可能影响复现。此外，CSMamba块中通道扩展因子λ等超参数的设定未在文本中详细说明。
5. **与纯Mamba方法对比**：文本中未提供与RS3Mamba等纯Mamba或Vision Mamba方法在相同骨干下的详细公平对比（如表II中RS3Mamba使用的是R18-Mamba骨干），难以严格剥离混合架构带来的具体增益。

## 9. 我该怎么使用这篇论文
- **快速了解**：阅读**摘要（Abstract）** 和**图2**，可以快速把握CM-UNet的整体架构、核心模块（CSMamba, MSAA）以及混合设计思路。
- **如果复现**：重点精读**II. METHODOLOGY**部分，特别是**CSMamba块（公式1）** 和**MSAA模块（图3）** 的详细描述，以及**III. EXPERIMENTS**中的**Implementation details**部分。
- **如果借鉴创新点**：
    - 若关注**注意力与Mamba的结合**，应深入学习CSMamba块中通道空间注意力作为门控条件的设计。
    - 若关注**多尺度特征融合**，应学习MSAA模块如何通过双路径（空间、通道）聚合不同尺度特征。
    - 若关注**训练策略**，可借鉴其多输出监督的方法。
- **如果写Related Work**：可放在以下几个部分：1）遥感图像语义分割的UNet改进工作；2）Mamba/Vision State Space Model在视觉任务中的应用；3）结合CNN与Transformer/Mamba的混合架构研究；4）通道/空间注意力机制的应用。

## 10. 和其他论文的关系
根据给定的主题 `B_注意力算子模块`，本文核心的**CSMamba块**直接与各类注意力机制论文相关。特别是其内部的**通道与空间注意力（CS）**，与经典的`SENet`（通道注意力）、`CBAM`（通道+空间注意力）等一脉相承，可以看作是这些注意力模块在Mamba架构中的特定应用与融合。
- `[[CBAM]]`：CSMamba块中的CS注意力可视为CBAM思想的一个具体实现，用于引导Mamba的特征流动。
- `[[SENet]]`：CSMamba中的通道注意力部分参考了SE模块的全局平均池化后接全连接层的思路。
- `[[Vision Mamba (Vim)]]` 和 `[[VMamba]]`：本文的2D-SSM模块直接基于VMamba的工作，是其核心组件的直接应用。
- `[[UNetformer]]`：作为本文的主要对比基线，CM-UNet可看作是UNetformer思路（用高效注意力改进UNet解码器）在Mamba架构下的延伸与进化。

## 11. 关键词
CM-UNet, 遥感图像语义分割, 状态空间模型 (SSM), Mamba, 通道空间注意力, 多尺度特征聚合, UNet, 混合架构, CS-Mamba, MSAA模块

## 12. 可信度说明
本篇精读笔记**完全基于**用户提供的PDF提取文本（共5页）生成。笔记中的所有技术细节、方法描述、实验数据和结论均严格引用自该文本，并标注了可能的页码引用（p.X）。对于文本中未明确说明的信息（如某些超参数具体值、与个别方法的详细速度对比），已在相应部分注明“PDF文本中未明确说明”。整体提取文本覆盖了论文的摘要、引言、方法、实验和结论的主要内容，信息完整，质量较高。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (5007 字符/页)); 来源缓存: `.paper-cache/extracts/MSAA.txt` (5/5 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
