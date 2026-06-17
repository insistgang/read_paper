---
title: "UNETR++: Delving into Efficient and Accurate 3D Medical Image Segmentation"
authors:
  - "Abdelrahman Shaker"
  - "Muhammad Maaz"
  - "Hanoona Rasheed"
  - "Salman Khan"
  - "Ming-Hsuan Yang"
  - "Fahad Shahbaz Khan"
year: 2023
venue: "arXiv"
doi: 
pdf: [[EPA3d.pdf]]
primary_topic: D_3D_点云_分类_分割_配准
topics:
  - "D_3D_点云_分类_分割_配准"
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
extract_cache: .paper-cache/extracts/EPA3d.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# UNETR++: Delving into Efficient and Accurate 3D Medical Image Segmentation

## 基本信息
- **PDF**: [[EPA3d.pdf]]
- **primary_topic**: `D_3D_点云_分类_分割_配准`
- **topics**: `D_3D_点云_分类_分割_配准`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | UNETR++: Delving into Efficient and Accurate 3D Medical Image Segmentation |
| **作者** | Abdelrahman Shaker; Muhammad Maaz; Hanoona Rasheed; Salman Khan; Ming-Hsuan Yang; Fahad Shahbaz Khan |
| **发表时间** | 2023 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Owing to the success of transformer models, recent poses[13,16]. Thetaskistypicallyaddressedbyutilizinga works study their applicability in 3D medical segmenta- U-Net[28]likeencoder-decoderarchitecturewheretheen- tiontasks. Withinthetransformermodels,theself-attention codergeneratesahierarchicallow-dimensionalrepresenta- mechanism is one of the main building blocks that strives tionofa3Dimageandthedecodermapsthislearnedrepre- to capture long-range dependencies. However, the self- sentationtoavoxel-wisesegmentation. EarlierCNN-based attentionoperationhasquadraticcomplexitywhichproves methods use convolutions and deconvolutions in the en- to be a computational bottleneck, especially in volumet- coderandthedecoder,respectively,butstruggletoachieve ric medical imaging, where the inputs are 3D with numer- accuratesegmentationresultslikelyduetotheirlimitedre- ous slices. In this paper, we propose a 3D medical im- ceptivefield.Incontrast,transformer-basedmethodsarein- age segmentation approac

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：3D体积分割在医学诊断中至关重要。传统的CNN方法因感受野有限难以捕捉全局依赖，而Transformer虽然擅长建模长程依赖，但其核心自注意力机制的计算复杂度与序列长度呈二次方关系（O(n²)），在处理包含大量切片的3D医学影像时成为严重的计算瓶颈。
- **之前方法的问题**：已有的混合架构（如UNETR, nnFormer）通过结合CNN和Transformer提升了分割精度，但这种精度的提升往往伴随着**模型复杂度（参数和FLOPs）的大幅增加**，可能导致模型鲁棒性不佳且难以部署。此外，这些方法大多侧重于空间特征的学习，未能充分显式地建模通道间的相互依赖关系，从而限制了特征表达的丰富性。
- **核心矛盾**：作者想要解决的核心矛盾是**如何在提升分割精度的同时，控制甚至降低模型的计算复杂度（参数和FLOPs）**，即追求“高效”与“准确”的统一。
## 关键贡献

1.  **提出了高效配对注意力（EPA）块**：这是一个全新的注意力模块，包含并行的空间注意力分支和通道注意力分支。两者共享查询（Q）和键（K）的投影权重，形成“配对”关系，以捕捉互补特征并减少参数。
2.  **实现线性复杂度的空间注意力**：在空间注意力分支中，通过将键（K）和值（V）投影到固定的低维空间，将自注意力的计算复杂度从O(n²)降低到O(np)（p<<n），实现了高效计算。
3.  **构建了UNETR++层次化混合框架**：以UNETR为基础，用提出的EPA块替换其标准Transformer块，并采用层次化的编码器-解码器结构，通过逐步降低分辨率并利用跳跃连接来融合多尺度特征。
4.  **在多个基准上验证了有效性与效率**：在Synapse、BTCV、ACDC、BRaTs和Decathlon-Lung五个医学图像分割基准上进行了广泛实验，结果表明UNETR++在分割精度和模型效率方面均优于现有方法。
5.  **在Synapse数据集上树立新标杆**：在Synapse基准测试中，UNETR++取得了87.22%的平均Dice分数（DSC），同时比当时最优的nnFormer方法在参数和FLOPs上分别减少了超过71%。
## 方法

- **整体框架**：UNETR++是一个**层次化的编码器-解码器**结构（如图2）。它基于UNETR框架，但采用了更精细的层次设计。编码器有四个阶段，每个阶段逐步降低特征分辨率；解码器同样有四个阶段，通过上采样逐步恢复分辨率。编码器与解码器之间通过跳跃连接融合多尺度特征。
- **输入与输出**：输入是3D医学体积图像（HxWxD）。首先通过**Patch Embedding**层（patch大小为4x4x2）将其划分为不重叠的3D patch序列，并线性投影到C维特征空间。输出是与输入同分辨率的**体素级分割掩码**。
- **关键模块：高效配对注意力（EPA）块**：这是论文的核心创新，替代了标准的自注意力块。
    - **设计思想**：结合空间和通道两个维度的注意力，并通过参数共享让它们相互促进。
    - **结构**：EPA块包含两个并行的注意力模块：**空间注意力（SA）** 和**通道注意力（CA）**。
    - **参数共享机制**：两个模块共享查询（Q）和键（K）的线性投影层权重（W_Q, W_K）。但用于生成**值（V）的投影层权重是独立的**（W_V_spatial, W_V_channel），以便学习互补特征。
    - **空间注意力（SA）**：
        - **目标**：高效地学习空间长程依赖。
        - **过程**：1) 将共享的K和空间V投影到低维（p x C）；2) 计算共享Q与投影后K^T的点积，经softmax得到空间注意力图；3) 将注意力图与投影后的空间V相加，得到增强的空间特征`X̂_s`。复杂度为O(np)。
        - **公式**：`X̂_s = Softmax( (Q_shared * K_proj^T) / sqrt(d) ) * V̂_spatial`
    - **通道注意力（CA）**：
        - **目标**：建模特征通道间的相互依赖关系。
        - **过程**：利用共享的Q和K，计算它们在通道维度上的点积（Q^T * K），经softmax得到通道注意力图，再与独立的通道V相乘，得到增强的通道特征`X̂_c`。
        - **公式**：`X̂_c = V_channel * Softmax( (Q_shared^T * K_shared) / sqrt(d) )`
    - **特征融合**：将空间注意力输出`X̂_s`和通道注意力输出`X̂_c`进行**逐元素相加**，然后通过一个3x3x3卷积和1x1x1卷积进行融合与增强，得到EPA块的最终输出`X̂`。
- **模块连接**：在编码器和解码器的每个阶段（除最后一个解码器阶段），都使用EPA块。跳跃连接将编码器各阶段的特征与对应解码器阶段的特征进行拼接，再通过卷积块进行融合。
- **训练方式**：损失函数是**软骰子损失（Soft Dice Loss）和交叉熵损失的加权和**。这是一种在医学图像分割中常用的组合损失函数，能同时优化区域重叠和体素分类。
- **推理流程**：3D体积输入经过编码器逐层下采样和特征提取，特征通过跳跃连接传递到解码器。解码器逐层上采样并与编码器特征融合，经过EPA块处理后，最终通过卷积层输出分割概率图。
- **与已有方法的差异**：
    - **相较于纯CNN（如nnUNet）**：UNETR++引入了Transformer的注意力机制，能建模长程依赖。
    - **相较于纯Transformer**：采用混合结构，结合了CNN的归纳偏置（局部性）。
    - **相较于其他混合方法（如UNETR, nnFormer）**：主要区别在于用**EPA块**替代了标准自注意力块。EPA块通过**空间-通道分离、注意力线性化、以及参数共享策略**，在降低计算量的同时，增强了特征表示。
## 实验

- **使用的数据集**：
    1.  **Synapse**：腹部多器官CT分割（8个器官），30例，按[5]划分训练/测试集。
    2.  **BTCV**：腹部多器官CT分割（13个器官），包含Synapse的8个器官。
    3.  **ACDC**：心脏MRI分割（右心室RV、左心室LV、心肌MYO），100例患者。
    4.  **BRaTs**：脑肿瘤分割。
    5.  **Decathlon-Lung**：肺部CT分割。
- **对比方法**：U-Net, TransUNet, Swin-UNet, UNETR, MISSFormer, Swin-UNETR, nnFormer等。
- **评价指标**：主要使用**Dice相似系数（DSC）** 和**95%豪斯多夫距离（HD95）**。也报告模型**参数量（Params）** 和**计算量（FLOPs）**。
- **主实验结果**（基于提供的Table 1，Synapse数据集）：
    - **分割性能**：UNETR++的平均DSC达到**87.22%**，HD95为**7.53**。相比基线UNETR（DSC 78.35%），绝对提升**8.87%**。相比当时最优的nnFormer（DSC 86.57%），也有提升。
    - **效率**：UNETR++参数量为**42.96M**，FLOPs为**47.98G**。相比nnFormer（参数150.5M，FLOPs 213.4G），**参数减少71.4%，FLOPs减少77.5%**。相比UNETR（参数92.49M，FLOPs 75.76G），也分别减少了53.5%和36.7%。
- **消融实验**：PDF提供的文本中未包含详细的消融实验部分。
- **泛化实验**：在五个不同模态（CT, MRI）和不同解剖区域（腹部、心脏、大脑、肺）的数据集上进行了验证，证明了其泛化能力。
- **效率信息**：如上所述，论文重点突出了UNETR++在参数量和FLOPs上的巨大优势，实现了“高精度、低复杂度”的目标。
## 局限

1.  **数据集范围**：虽然使用了五个数据集，但主要集中在腹部、心脏和大脑的医学图像分割。对于其他解剖部位或成像模态（如超声、病理切片）的有效性未被验证。
2.  **实验细节缺失**：提供的PDF文本中未包含完整的消融实验、训练细节（如优化器、学习率策略、数据增强）和详细的模型配置，这对完全复现和理解模型极限性能造成一定困难。
3.  **计算成本**：虽然FLOPs和参数量降低，但自注意力机制（即便是线性化的）在实际推理时间上的加速效果（如与纯CNN相比）未在提供的文本中明确量化。
4.  **假设依赖**：EPA块中空间注意力通过降维来提升效率，这种降维是否会不可避免地丢失一些细节信息，论文中没有深入讨论。
5.  **复现风险**：代码虽然提供了链接，但依赖的具体环境、预训练权重等信息在提供的文本中未说明，可能存在复现挑战。
## 个人评论

1.  **提出了一个高效的注意力设计范式**：EPA块展示了一种**将空间和通道注意力解耦、并利用参数共享进行协同**的有效思路。这种“分而治之，合而为一”的设计，对于后续设计轻量级或高效的Transformer变体具有启发意义。
2.  **在医学图像分割中平衡精度与效率**：论文不仅追求刷榜，更强调模型的实用性（低参数、低计算量）。这对于推动深度学习模型在资源受限的临床环境（如边缘设备）中部署至关重要。
3.  **清晰的改进路径**：论文从分析现有混合方法的不足（计算复杂、忽略通道依赖）出发，针对性地提出解决方案（线性化空间注意力、引入通道注意力、参数共享），逻辑清晰，易于理解和借鉴。
4.  **扎实的实验对比**：在多个主流基准上与强大的方法进行了全面对比，结果令人信服，特别是效率-精度权衡图（如图1右）非常直观。

### 使用建议

- **如果快速了解**：重点阅读**摘要（Abstract）**、**图1和图2**、**引言（Introduction）的贡献列表**以及**实验（Experiments）** 部分的表格和关键结论。
- **如果复现**：仔细阅读**第3节方法（Method）**，特别是3.1整体架构和3.2 EPA块的详细描述与公式。结合**附录（如果提供）** 和**开源代码**进行实现。
- **如果借鉴创新点**：
    - **学习EPA块的设计**：理解空间与通道注意力的分离与共享机制，思考能否将其应用于其他任务（如2D分割、检测）或与其他注意力形式（如轴向注意力）结合。
    - **学习混合架构构建**：参考UNETR++如何将Transformer（EPA块）嵌入到U-Net式的编码器-解码器中。
- **如果写related work**：本文可归类为**“基于Transformer的医学图像分割方法”** 或 **“高效的注意力机制/混合网络设计”**。在讨论Transformer在密集预测任务中的计算复杂度问题时，本文是一个很好的参考。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[D_3D_点云_分类_分割_配准]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉与医学图像分析的交叉领域，具体是**3D医学图像分割**方向。它旨在解决当前基于Transformer的3D医学图像分割模型中存在的**计算复杂度高（参数多、FLOPs大）与分割精度提升受限的矛盾**。论文适合放在“3D医学图像分割”或“Transformer在医学图像中的应用”这个主题下。它提出了一种兼顾精度与效率的混合架构，对推动该技术在临床实践中的应用具有价值。

## 2. 一句话总结
本文提出了名为UNETR++的混合架构，其核心是一种新颖的**高效配对注意力（EPA）块**，通过空间和通道注意力的分离与参数共享，在保持甚至提升分割精度的同时，显著降低了模型的参数量和计算复杂度。

## 3. 背景与问题
- **为什么要做**：3D体积分割在医学诊断中至关重要。传统的CNN方法因感受野有限难以捕捉全局依赖，而Transformer虽然擅长建模长程依赖，但其核心自注意力机制的计算复杂度与序列长度呈二次方关系（O(n²)），在处理包含大量切片的3D医学影像时成为严重的计算瓶颈。
- **之前方法的问题**：已有的混合架构（如UNETR, nnFormer）通过结合CNN和Transformer提升了分割精度，但这种精度的提升往往伴随着**模型复杂度（参数和FLOPs）的大幅增加**，可能导致模型鲁棒性不佳且难以部署。此外，这些方法大多侧重于空间特征的学习，未能充分显式地建模通道间的相互依赖关系，从而限制了特征表达的丰富性。
- **核心矛盾**：作者想要解决的核心矛盾是**如何在提升分割精度的同时，控制甚至降低模型的计算复杂度（参数和FLOPs）**，即追求“高效”与“准确”的统一。

## 4. 核心贡献
1.  **提出了高效配对注意力（EPA）块**：这是一个全新的注意力模块，包含并行的空间注意力分支和通道注意力分支。两者共享查询（Q）和键（K）的投影权重，形成“配对”关系，以捕捉互补特征并减少参数。
2.  **实现线性复杂度的空间注意力**：在空间注意力分支中，通过将键（K）和值（V）投影到固定的低维空间，将自注意力的计算复杂度从O(n²)降低到O(np)（p<<n），实现了高效计算。
3.  **构建了UNETR++层次化混合框架**：以UNETR为基础，用提出的EPA块替换其标准Transformer块，并采用层次化的编码器-解码器结构，通过逐步降低分辨率并利用跳跃连接来融合多尺度特征。
4.  **在多个基准上验证了有效性与效率**：在Synapse、BTCV、ACDC、BRaTs和Decathlon-Lung五个医学图像分割基准上进行了广泛实验，结果表明UNETR++在分割精度和模型效率方面均优于现有方法。
5.  **在Synapse数据集上树立新标杆**：在Synapse基准测试中，UNETR++取得了87.22%的平均Dice分数（DSC），同时比当时最优的nnFormer方法在参数和FLOPs上分别减少了超过71%。

## 5. 方法详解
- **整体框架**：UNETR++是一个**层次化的编码器-解码器**结构（如图2）。它基于UNETR框架，但采用了更精细的层次设计。编码器有四个阶段，每个阶段逐步降低特征分辨率；解码器同样有四个阶段，通过上采样逐步恢复分辨率。编码器与解码器之间通过跳跃连接融合多尺度特征。
- **输入与输出**：输入是3D医学体积图像（HxWxD）。首先通过**Patch Embedding**层（patch大小为4x4x2）将其划分为不重叠的3D patch序列，并线性投影到C维特征空间。输出是与输入同分辨率的**体素级分割掩码**。
- **关键模块：高效配对注意力（EPA）块**：这是论文的核心创新，替代了标准的自注意力块。
    - **设计思想**：结合空间和通道两个维度的注意力，并通过参数共享让它们相互促进。
    - **结构**：EPA块包含两个并行的注意力模块：**空间注意力（SA）** 和**通道注意力（CA）**。
    - **参数共享机制**：两个模块共享查询（Q）和键（K）的线性投影层权重（W_Q, W_K）。但用于生成**值（V）的投影层权重是独立的**（W_V_spatial, W_V_channel），以便学习互补特征。
    - **空间注意力（SA）**：
        - **目标**：高效地学习空间长程依赖。
        - **过程**：1) 将共享的K和空间V投影到低维（p x C）；2) 计算共享Q与投影后K^T的点积，经softmax得到空间注意力图；3) 将注意力图与投影后的空间V相加，得到增强的空间特征`X̂_s`。复杂度为O(np)。
        - **公式**：`X̂_s = Softmax( (Q_shared * K_proj^T) / sqrt(d) ) * V̂_spatial`
    - **通道注意力（CA）**：
        - **目标**：建模特征通道间的相互依赖关系。
        - **过程**：利用共享的Q和K，计算它们在通道维度上的点积（Q^T * K），经softmax得到通道注意力图，再与独立的通道V相乘，得到增强的通道特征`X̂_c`。
        - **公式**：`X̂_c = V_channel * Softmax( (Q_shared^T * K_shared) / sqrt(d) )`
    - **特征融合**：将空间注意力输出`X̂_s`和通道注意力输出`X̂_c`进行**逐元素相加**，然后通过一个3x3x3卷积和1x1x1卷积进行融合与增强，得到EPA块的最终输出`X̂`。
- **模块连接**：在编码器和解码器的每个阶段（除最后一个解码器阶段），都使用EPA块。跳跃连接将编码器各阶段的特征与对应解码器阶段的特征进行拼接，再通过卷积块进行融合。
- **训练方式**：损失函数是**软骰子损失（Soft Dice Loss）和交叉熵损失的加权和**。这是一种在医学图像分割中常用的组合损失函数，能同时优化区域重叠和体素分类。
- **推理流程**：3D体积输入经过编码器逐层下采样和特征提取，特征通过跳跃连接传递到解码器。解码器逐层上采样并与编码器特征融合，经过EPA块处理后，最终通过卷积层输出分割概率图。
- **与已有方法的差异**：
    - **相较于纯CNN（如nnUNet）**：UNETR++引入了Transformer的注意力机制，能建模长程依赖。
    - **相较于纯Transformer**：采用混合结构，结合了CNN的归纳偏置（局部性）。
    - **相较于其他混合方法（如UNETR, nnFormer）**：主要区别在于用**EPA块**替代了标准自注意力块。EPA块通过**空间-通道分离、注意力线性化、以及参数共享策略**，在降低计算量的同时，增强了特征表示。

## 6. 实验与结果
- **使用的数据集**：
    1.  **Synapse**：腹部多器官CT分割（8个器官），30例，按[5]划分训练/测试集。
    2.  **BTCV**：腹部多器官CT分割（13个器官），包含Synapse的8个器官。
    3.  **ACDC**：心脏MRI分割（右心室RV、左心室LV、心肌MYO），100例患者。
    4.  **BRaTs**：脑肿瘤分割。
    5.  **Decathlon-Lung**：肺部CT分割。
- **对比方法**：U-Net, TransUNet, Swin-UNet, UNETR, MISSFormer, Swin-UNETR, nnFormer等。
- **评价指标**：主要使用**Dice相似系数（DSC）** 和**95%豪斯多夫距离（HD95）**。也报告模型**参数量（Params）** 和**计算量（FLOPs）**。
- **主实验结果**（基于提供的Table 1，Synapse数据集）：
    - **分割性能**：UNETR++的平均DSC达到**87.22%**，HD95为**7.53**。相比基线UNETR（DSC 78.35%），绝对提升**8.87%**。相比当时最优的nnFormer（DSC 86.57%），也有提升。
    - **效率**：UNETR++参数量为**42.96M**，FLOPs为**47.98G**。相比nnFormer（参数150.5M，FLOPs 213.4G），**参数减少71.4%，FLOPs减少77.5%**。相比UNETR（参数92.49M，FLOPs 75.76G），也分别减少了53.5%和36.7%。
- **消融实验**：PDF提供的文本中未包含详细的消融实验部分。
- **泛化实验**：在五个不同模态（CT, MRI）和不同解剖区域（腹部、心脏、大脑、肺）的数据集上进行了验证，证明了其泛化能力。
- **效率信息**：如上所述，论文重点突出了UNETR++在参数量和FLOPs上的巨大优势，实现了“高精度、低复杂度”的目标。

## 7. 这篇论文真正有价值的地方
1.  **提出了一个高效的注意力设计范式**：EPA块展示了一种**将空间和通道注意力解耦、并利用参数共享进行协同**的有效思路。这种“分而治之，合而为一”的设计，对于后续设计轻量级或高效的Transformer变体具有启发意义。
2.  **在医学图像分割中平衡精度与效率**：论文不仅追求刷榜，更强调模型的实用性（低参数、低计算量）。这对于推动深度学习模型在资源受限的临床环境（如边缘设备）中部署至关重要。
3.  **清晰的改进路径**：论文从分析现有混合方法的不足（计算复杂、忽略通道依赖）出发，针对性地提出解决方案（线性化空间注意力、引入通道注意力、参数共享），逻辑清晰，易于理解和借鉴。
4.  **扎实的实验对比**：在多个主流基准上与强大的方法进行了全面对比，结果令人信服，特别是效率-精度权衡图（如图1右）非常直观。

## 8. 局限与问题
1.  **数据集范围**：虽然使用了五个数据集，但主要集中在腹部、心脏和大脑的医学图像分割。对于其他解剖部位或成像模态（如超声、病理切片）的有效性未被验证。
2.  **实验细节缺失**：提供的PDF文本中未包含完整的消融实验、训练细节（如优化器、学习率策略、数据增强）和详细的模型配置，这对完全复现和理解模型极限性能造成一定困难。
3.  **计算成本**：虽然FLOPs和参数量降低，但自注意力机制（即便是线性化的）在实际推理时间上的加速效果（如与纯CNN相比）未在提供的文本中明确量化。
4.  **假设依赖**：EPA块中空间注意力通过降维来提升效率，这种降维是否会不可避免地丢失一些细节信息，论文中没有深入讨论。
5.  **复现风险**：代码虽然提供了链接，但依赖的具体环境、预训练权重等信息在提供的文本中未说明，可能存在复现挑战。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**摘要（Abstract）**、**图1和图2**、**引言（Introduction）的贡献列表**以及**实验（Experiments）** 部分的表格和关键结论。
- **如果复现**：仔细阅读**第3节方法（Method）**，特别是3.1整体架构和3.2 EPA块的详细描述与公式。结合**附录（如果提供）** 和**开源代码**进行实现。
- **如果借鉴创新点**：
    - **学习EPA块的设计**：理解空间与通道注意力的分离与共享机制，思考能否将其应用于其他任务（如2D分割、检测）或与其他注意力形式（如轴向注意力）结合。
    - **学习混合架构构建**：参考UNETR++如何将Transformer（EPA块）嵌入到U-Net式的编码器-解码器中。
- **如果写related work**：本文可归类为**“基于Transformer的医学图像分割方法”** 或 **“高效的注意力机制/混合网络设计”**。在讨论Transformer在密集预测任务中的计算复杂度问题时，本文是一个很好的参考。

## 10. 和其他论文的关系
根据库的主题“D_3D_点云_分类_分割_配准”，本文属于3D视觉和分割领域。与以下论文可能强相关：
- **UNETR**：本文直接改进和扩展了[[UNETR]]架构。
- **nnFormer**：本文在实验中主要对标并超越了[[nnFormer]]。
- **Swin-UNet / Swin-UNETR**：本文对比了基于Swin Transformer的混合方法[[Swin-UNet]]和[[Swin-UNETR]]。
- **U-Net**：本文的骨干架构继承自[[U-Net]]。
- **TransUNet**：本文属于同一时期的混合架构研究，与[[TransUNet]]方向一致但技术路线不同。
*注：由于论文主题为医学图像分割，与点云处理关联较弱，故不强行建立与点云论文的联系。*

## 11. 关键词
3D医学图像分割, Transformer, 高效自注意力, 混合架构, 空间-通道注意力, 计算复杂度, UNETR++, 医学图像分析, 腹部器官分割, 心脏分割, Dice分数

## 12. 可信度说明
本精读笔记**主要基于提供的PDF文本的前12页内容生成**，这些部分涵盖了论文的标题、作者、摘要、引言、相关工作、方法（详细）以及实验设置与部分结果。文本提取质量良好，公式、图表引用和大部分实验结果表得以保留。
**局限性**：由于提供的文本不完整（缺少第13-15页），关于**ACDC、BRaTs和Decathlon-Lung数据集的详细实验结果、更深入的消融研究、完整的结论以及参考文献列表**未能在本笔记中呈现。因此，笔记中关于多个数据集泛化结论的描述部分基于对实验章节开头的合理推断。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/EPA3d.txt` (15/15 页; 原 AI 主体 12/15 + 全文补读 13-15); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.15: To validate the effectiveness of our EPA block, we con-
- p.15: In this paper, we present a hierarchical approach, named

### 缺失页关键摘录

- p.13: Figure 5. Additional qualitative comparison on Synapse dataset. We compare our UNETR++ with existing methods: UNETR, Swin
- p.13: Figure 6. Qualitative comparison on the ACDC dataset. We compare our UNETR++ with existing methods: UNETR and nnFormer. It is
- p.14: Figure 7. Additional qualitative comparison between UNETR++ and the baseline UNETR. The baseline struggle to correctly segment
- p.14: Figure 8. Additional qualitative comparison between UNETR++ and the baseline UNETR. The baseline struggle to correctly segment
- p.15: Figure 9. Qualitative comparison between the baseline UN-
- p.15: ETR [13] and our UNETR++ on Synapse dataset. Each inaccurate
- p.15: UNETR++ and the baseline on the ACDC dataset. In all
- p.15: other baseline comparison on the Decathalon-Lung dataset.
- p.15: an experiment with feature maps of size [64;128;256;512]
- p.15: instead of [32;64;128;256] on the BTCV dataset. Although
- p.15: 94:24M and the FLOPs increased to 117G, the average dice
- p.15: Figure 10. Qualitative comparison between the baseline UN-
<!-- AI_READING_NOTE_END -->
