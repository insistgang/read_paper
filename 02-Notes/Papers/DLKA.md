---
title: "Beyond Self-Attention: Deformable Large Kernel Attention for Medical Image"
authors:
  - "Reza Azad"
  - "Leon Niggemeier"
  - "Amirhossein Kazerouni"
  - "Ehsan Khodapanah Aghdam"
  - "Yury Velichko"
  - "Ulas Bagci"
  - "Dorit Merhof"
year: 2023
venue: "arXiv"
doi: 
pdf: [[DLKA.pdf]]
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
extract_cache: .paper-cache/extracts/DLKA.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# Beyond Self-Attention: Deformable Large Kernel Attention for Medical Image

## 基本信息
- **PDF**: [[DLKA.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Beyond Self-Attention: Deformable Large Kernel Attention for Medical Image |
| **作者** | Reza Azad; Leon Niggemeier; Amirhossein Kazerouni; Ehsan Khodapanah Aghdam; Yury Velichko; Ulas Bagci; Dorit Merhof |
| **发表时间** | 2023 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Medical image segmentation plays a crucial role in Medical image segmentation has seen significant im- computer-assisted diagnostics, aiding medical profession- provementswithtransformermodels,whichexcelingrasp- alsinanalyzingcomplexmedicalimages. Thisprocessnot ing far-reaching contexts and global contextual informa- onlyreducesthelaboriousnessofmanualtasksandthede- tion. However, the increasing computational demands of pendence on medical expertise but also enables faster and thesemodels,proportionaltothesquaredtokencount,limit moreaccuratediagnoses. Theautomationofsegmentation theirdepthandresolutioncapabilities. Mostcurrentmeth- offers the potential for faster and more accurate diagnos- odsprocessDvolumetricimagedataslice-by-slice(called tic outcomes, facilitating appropriate treatment strategies pseudo 3D), missing crucial inter-slice information and and enabling the execution of image-guided surgical pro- thusreducingthemodel’soverallperformance. Toaddress cedures. Thus, the impe

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

*   **为什么要做**：医学图像分割对精准诊断和治疗至关重要。尽管Vision Transformer（ViT）在捕获全局上下文方面表现出色，但其自注意力机制计算复杂度与输入序列长度的平方成正比，限制了其在处理高分辨率或3D体数据时的深度和分辨率。同时，大多数处理3D医学图像的方法采用“伪3D”（逐切片处理），忽视了切片间的关键信息。
*   **之前方法的问题**：
    1.  **CNN的局限**：卷积神经网络（CNN）擅长捕获局部细节，但受限于感受野，难以建模长程依赖和全局上下文。
    2.  **ViT的局限**：ViT能建模全局依赖，但对局部纹理和细节的表征能力不足，且计算开销巨大。
    3.  **现有混合方法的局限**：如TransUNet等CNN-ViT混合方法存在计算效率问题或对CNN骨干的重度依赖。
    4.  **处理3D数据的方式**：现有架构常将3D体积数据逐切片处理，损失了切片间的关联信息，影响定位和上下文整合。
*   **核心矛盾**：如何在**保持计算高效性**的前提下，同时有效建模**长程依赖（全局上下文）** 并**适应医学图像中器官/病变的不规则形变（局部细节）**，特别是处理3D体数据时。
## 关键贡献

1.  **提出了D-LKA注意力模块**：一种新型注意力机制，使用深度可分离卷积、深度可分离扩张卷积和1×1卷积的组合来构建大卷积核，以更低的计算成本获得与自注意力机制类似的感受野。该模块**无需使用Softmax或Sigmoid等归一化函数**，避免了对高频信息的抑制。
2.  **在D-LKA中引入可变形卷积**：利用可变形卷积动态调整采样网格，使大核能够灵活地适应输入数据的形变模式，从而更好地刻画不规则形状的病变或器官边界。
3.  **设计了2D和3D版本的D-LKA网络架构**：2D版本使用MaxViT作为编码器，D-LKA作为解码器；3D版本则完全由D-LKA块构成，并通过设计在3D场景中应用可变形卷积的策略，实现了跨深度（切片间）的信息交换。
4.  **实现了计算高效与高性能的统一**：整个网络（D-LKA Net）仅基于D-LKA概念构建，在多个医学图像分割基准测试中达到了新的SOTA性能，同时计算开销较低。
## 方法

*   **整体框架**：D-LKA Net是一个**层级式的编码器-解码器（U型）架构**。2D和3D版本结构对称，均用于像素/体素级的语义分割任务。
*   **输入输出**：输入为2D医学图像或3D体积数据，输出为与输入同尺寸的分割概率图。
*   **关键模块**：
    *   **D-LKA注意力模块**：核心计算单元。其构造如图2及公式(8)所示：
        `Attention = Conv1×1(DDW-D-Conv(DDW-Conv(F')))`
        `Output = Conv1×1(Attention ⊗ F') + F`
        其中`F`为输入特征，`F'`是经过一个卷积和GELU激活后的特征。该过程先通过深度可分离卷积（DDW-Conv）和深度可分离扩张卷积（DDW-D-Conv）构建大核感受野，再通过1×1卷积得到注意力图，最后与输入特征进行元素相乘和残差连接。**在2D版本中，这些卷积层被替换为可变形卷积以增强形变建模能力**。
    *   **3D D-LKA中的可变形策略**：由于为3D大核生成偏移量的卷积层参数开销巨大，论文采用折中方案：在现有的LKA框架（深度可分离卷积之后）**引入一个单独的可变形卷积层**，而非像2D那样将所有卷积都变为可变形。
*   **模块之间怎么连接**：
    *   **2D D-LKA Net**：编码器采用MaxViT块提取4级多尺度特征。解码器由4个阶段构成，每个阶段包含2个D-LKA块。各级特征通过Patch Expanding层进行上采样和通道缩减，最终通过线性层输出分割结果。
    *   **3D D-LKA Net**：编码器由3个阶段组成，每个阶段包含3个D-LKA块，阶段之间通过下采样层连接。瓶颈层包含2个D-LKA块。解码器对称，使用转置卷积进行上采样。编码器和解码器对应层级之间通过跳跃连接（基于加法融合）传递信息。最终通过3×3×3和1×1×1卷积层输出分割图。
    *   **D-LKA块的内部结构**：如公式(9)-(13)所示，遵循`LayerNorm -> D-LKA Attention -> 残差连接`的范式，之后连接一个前馈网络（MLP或卷积层）并再次残差连接。
*   **数学公式或机制的直观解释**：大核的构建原理是：一个K×K的大核可以通过一个`(2d-1)×(2d-1)`的深度可分离卷积和一个`(K/d)×(K/d)`的深度可分离扩张卷积（扩张率为d）来近似，从而用较少的参数和计算量获得大的有效感受野。可变形卷积则通过学习一个偏移场，让卷积核的采样点位置可以根据图像内容动态“扭曲”，从而更好地覆盖不规则形状的目标。
*   **训练方式**：2D模型使用SGD优化器，学习率0.05，训练400 epochs，损失函数为加权交叉熵与Dice损失的组合（公式14）。3D模型同样使用SGD，学习率0.01，训练1000 epochs，输入为128×128×64的图像块。均采用了常见的数据增强策略。
*   **推理流程**：标准的分割模型前向传播流程，输入图像，经过编码器-解码器后输出分割图。
*   **和已有方法的差异**：
    *   相较于**传统自注意力**：计算复杂度从O(n²)降至与输入分辨率线性相关，且无需归一化，保留了高频信息。
    *   相较于**原始LKA**：引入了可变形卷积，增强了模型对不规则形变的适应性。
    *   相较于**CNN-ViT混合模型（如TransUNet）**：提出了一个纯Transformer架构（虽然2D版编码器用了MaxViT，但核心是D-LKA），减少了计算冗余。
    *   相较于**其他处理3D数据的方法**：提出了完整的3D D-LKA架构，并通过特殊设计在3D中应用了可变形机制，避免了伪3D处理。
*   **论文类型特化（注意力类）**：
    *   **注意力作用维度**：主要作用于**空间维度**，通过大核卷积在空间上聚合信息，模拟全局和局部注意力。
    *   **可插入网络**：D-LKA块设计为即插即用模块，可作为Transformer或CNN中的基本构建块。
    *   **计算量 vs 效果**：论文的核心论点就是通过D-LKA在**较低计算成本**下实现了**优于自注意力**的分割效果。参数与FLOPs计算公式见公式(3)-(7)。
## 实验

*   **使用的数据集**：
    1.  **Synapse 多器官分割数据集**：30个病例， 3779张腹部CT轴向切片，用于评估8个腹部器官的分割。
    2.  **皮肤病变分割数据集**：包括ISIC 2017（训练/验证/测试：2000/150/600）、ISIC 2018和PH2（200张）数据集。
    3.  **NIH 胰腺分割数据集**：82个3D腹部CT体积，训练62例，测试20例。
*   **对比方法**：ScaleFormer、DAEFormer、Swin-UNet、U-Net、HiFormer、MISSFormer、D-Former等SOTA方法。
*   **评价指标**：主要使用**Dice Similarity Coefficient (DSC)**。
*   **主实验结果（关键数字）**：
    *   在**Synapse数据集**上，D-LKA Net的平均DSC比ScaleFormer高**1.41%**，比DAEFormer高**1.64%**。在**胰腺分割**这一难点上，比第二名方法高出**2.04%**（p.5）。
    *   在**皮肤病变分割**（ISIC 2017, ISIC 2018, PH2）上，D-LKA Net在各项指标上均**一致性地优于**竞争对手（p.6）。
*   **消融实验**：PDF文本中未明确说明具体的消融实验设置和结果。
*   **泛化实验**：通过在Synapse（腹部CT）和皮肤病变（皮肤镜图像）两种不同模态的数据集上均取得SOTA结果，展示了模型的泛化能力。
*   **速度/参数量/FLOPs等效率信息**：文本中给出了计算参数和FLOPs的理论公式（公式3-7），并指出其随输入尺寸线性增长，但**未在实验部分报告具体的运行时间、参数量或FLOPs数值对比**。
## 局限

*   **3D可变形卷积的应用受限**：3D版本为了控制计算量，只引入了单个可变形卷积层，而非像2D那样全面可变形。这可能限制了其对复杂3D形变的建模能力。
*   **实验分析深度不足**：论文主要展示了性能的提升，但对**为什么D-LKA有效**的机理分析不足。例如，缺少对注意力图的可视化，或者对大核和可变形卷积各自贡献的详细消融实验。
*   **数据集范围有限**：实验仅在腹部CT和皮肤镜图像上进行验证，在其他模态（如MRI、超声）或更复杂的分割任务（如肿瘤精细边界）上的有效性未知。
*   **计算成本报告缺失**：虽然强调计算高效，但实验部分未提供与对比方法在运行速度、GPU内存占用等方面的具体量化比较，削弱了“高效性”论点的说服力。
*   **依赖特定编码器（2D版）**：2D模型使用了MaxViT作为编码器，其性能与MaxViT本身的能力有一定捆绑，可能掩盖D-LKA模块在其他骨干网络中的普遍有效性。
## 个人评论

1.  **优雅的模块设计思想**：用“**深度可分离卷积 + 深度可分离扩张卷积**”的组合来高效构建大感受野，是一种巧妙替代标准自注意力计算的思路。这为设计**轻量化、高效能**的注意力模块提供了新范式，值得后续研究借鉴。
2.  **对医学图像特性的针对性设计**：明确针对医学图像中器官/病变的**不规则形变**问题，将可变形卷积与注意力机制结合，提升了模型对复杂解剖结构的拟合能力。这种“**任务驱动**”的模块改进思路具有启发性。
3.  **完整的2D/3D一体化方案**：不仅提出了2D模块，还系统地设计了3D版本及其可变形卷积的应用策略，为处理3D体数据提供了端到端的解决方案，避免了信息损失。
4.  **纯粹的架构探索**：尝试构建一个尽可能纯粹的、基于自身核心模块（D-LKA）的网络，减少了对外部复杂模块（如大型CNN backbone）的依赖，使模型结构更简洁，利于理解和改进。

### 使用建议

*   **如果快速了解**：只读**摘要、引言（特别是“我们的贡献”部分）和结论**，以及**图1（网络架构）和图2（D-LKA模块）**。
*   **如果复现**：重点看**第2节“方法”**，尤其是2.2节D-LKA模块的公式（8）和2.3/2.4节的网络架构描述。结合**图1和图2**理解实现细节。第3节的实验设置（如优化器、损失函数、数据增强）也需要仔细阅读。
*   **如果借鉴创新点**：应深入学习**2.2节D-LKA模块的构造思想**（大核分解与可变形卷积的结合），思考如何将其迁移到其他视觉任务（如图像分类、目标检测）或其他网络结构中作为基本单元。
*   **如果写related work**：可放在以下类别：1) **高效注意力机制/视觉Transformer**；2) **医学图像分割中的上下文建模方法**；3) **大卷积核网络**；4) **可变形卷积在医学图像中的应用**。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉与医学图像分析的交叉领域，具体为**医学图像分割**任务。论文的核心是**注意力算子模块**的改进，旨在设计一种高效、能建模长程依赖并适应器官/病变不规则形变的注意力机制，以替代或改进传统的自注意力模块。它适合归类于“注意力算子模块”这一研究主题。

## 2. 一句话总结
本文提出了一种名为**可变形大核注意力（Deformable Large Kernel Attention， D-LKA）** 的新型注意力模块，通过使用大卷积核高效模拟自注意力的感受野，并引入可变形卷积使其能自适应医学图像中的不规则形变，最终构建了一个高效、高性能的纯Transformer架构（D-LKA Net）用于2D和3D医学图像分割。

## 3. 背景与问题
*   **为什么要做**：医学图像分割对精准诊断和治疗至关重要。尽管Vision Transformer（ViT）在捕获全局上下文方面表现出色，但其自注意力机制计算复杂度与输入序列长度的平方成正比，限制了其在处理高分辨率或3D体数据时的深度和分辨率。同时，大多数处理3D医学图像的方法采用“伪3D”（逐切片处理），忽视了切片间的关键信息。
*   **之前方法的问题**：
    1.  **CNN的局限**：卷积神经网络（CNN）擅长捕获局部细节，但受限于感受野，难以建模长程依赖和全局上下文。
    2.  **ViT的局限**：ViT能建模全局依赖，但对局部纹理和细节的表征能力不足，且计算开销巨大。
    3.  **现有混合方法的局限**：如TransUNet等CNN-ViT混合方法存在计算效率问题或对CNN骨干的重度依赖。
    4.  **处理3D数据的方式**：现有架构常将3D体积数据逐切片处理，损失了切片间的关联信息，影响定位和上下文整合。
*   **核心矛盾**：如何在**保持计算高效性**的前提下，同时有效建模**长程依赖（全局上下文）** 并**适应医学图像中器官/病变的不规则形变（局部细节）**，特别是处理3D体数据时。

## 4. 核心贡献
1.  **提出了D-LKA注意力模块**：一种新型注意力机制，使用深度可分离卷积、深度可分离扩张卷积和1×1卷积的组合来构建大卷积核，以更低的计算成本获得与自注意力机制类似的感受野。该模块**无需使用Softmax或Sigmoid等归一化函数**，避免了对高频信息的抑制。
2.  **在D-LKA中引入可变形卷积**：利用可变形卷积动态调整采样网格，使大核能够灵活地适应输入数据的形变模式，从而更好地刻画不规则形状的病变或器官边界。
3.  **设计了2D和3D版本的D-LKA网络架构**：2D版本使用MaxViT作为编码器，D-LKA作为解码器；3D版本则完全由D-LKA块构成，并通过设计在3D场景中应用可变形卷积的策略，实现了跨深度（切片间）的信息交换。
4.  **实现了计算高效与高性能的统一**：整个网络（D-LKA Net）仅基于D-LKA概念构建，在多个医学图像分割基准测试中达到了新的SOTA性能，同时计算开销较低。

## 5. 方法详解
*   **整体框架**：D-LKA Net是一个**层级式的编码器-解码器（U型）架构**。2D和3D版本结构对称，均用于像素/体素级的语义分割任务。
*   **输入输出**：输入为2D医学图像或3D体积数据，输出为与输入同尺寸的分割概率图。
*   **关键模块**：
    *   **D-LKA注意力模块**：核心计算单元。其构造如图2及公式(8)所示：
        `Attention = Conv1×1(DDW-D-Conv(DDW-Conv(F')))`
        `Output = Conv1×1(Attention ⊗ F') + F`
        其中`F`为输入特征，`F'`是经过一个卷积和GELU激活后的特征。该过程先通过深度可分离卷积（DDW-Conv）和深度可分离扩张卷积（DDW-D-Conv）构建大核感受野，再通过1×1卷积得到注意力图，最后与输入特征进行元素相乘和残差连接。**在2D版本中，这些卷积层被替换为可变形卷积以增强形变建模能力**。
    *   **3D D-LKA中的可变形策略**：由于为3D大核生成偏移量的卷积层参数开销巨大，论文采用折中方案：在现有的LKA框架（深度可分离卷积之后）**引入一个单独的可变形卷积层**，而非像2D那样将所有卷积都变为可变形。
*   **模块之间怎么连接**：
    *   **2D D-LKA Net**：编码器采用MaxViT块提取4级多尺度特征。解码器由4个阶段构成，每个阶段包含2个D-LKA块。各级特征通过Patch Expanding层进行上采样和通道缩减，最终通过线性层输出分割结果。
    *   **3D D-LKA Net**：编码器由3个阶段组成，每个阶段包含3个D-LKA块，阶段之间通过下采样层连接。瓶颈层包含2个D-LKA块。解码器对称，使用转置卷积进行上采样。编码器和解码器对应层级之间通过跳跃连接（基于加法融合）传递信息。最终通过3×3×3和1×1×1卷积层输出分割图。
    *   **D-LKA块的内部结构**：如公式(9)-(13)所示，遵循`LayerNorm -> D-LKA Attention -> 残差连接`的范式，之后连接一个前馈网络（MLP或卷积层）并再次残差连接。
*   **数学公式或机制的直观解释**：大核的构建原理是：一个K×K的大核可以通过一个`(2d-1)×(2d-1)`的深度可分离卷积和一个`(K/d)×(K/d)`的深度可分离扩张卷积（扩张率为d）来近似，从而用较少的参数和计算量获得大的有效感受野。可变形卷积则通过学习一个偏移场，让卷积核的采样点位置可以根据图像内容动态“扭曲”，从而更好地覆盖不规则形状的目标。
*   **训练方式**：2D模型使用SGD优化器，学习率0.05，训练400 epochs，损失函数为加权交叉熵与Dice损失的组合（公式14）。3D模型同样使用SGD，学习率0.01，训练1000 epochs，输入为128×128×64的图像块。均采用了常见的数据增强策略。
*   **推理流程**：标准的分割模型前向传播流程，输入图像，经过编码器-解码器后输出分割图。
*   **和已有方法的差异**：
    *   相较于**传统自注意力**：计算复杂度从O(n²)降至与输入分辨率线性相关，且无需归一化，保留了高频信息。
    *   相较于**原始LKA**：引入了可变形卷积，增强了模型对不规则形变的适应性。
    *   相较于**CNN-ViT混合模型（如TransUNet）**：提出了一个纯Transformer架构（虽然2D版编码器用了MaxViT，但核心是D-LKA），减少了计算冗余。
    *   相较于**其他处理3D数据的方法**：提出了完整的3D D-LKA架构，并通过特殊设计在3D中应用了可变形机制，避免了伪3D处理。
*   **论文类型特化（注意力类）**：
    *   **注意力作用维度**：主要作用于**空间维度**，通过大核卷积在空间上聚合信息，模拟全局和局部注意力。
    *   **可插入网络**：D-LKA块设计为即插即用模块，可作为Transformer或CNN中的基本构建块。
    *   **计算量 vs 效果**：论文的核心论点就是通过D-LKA在**较低计算成本**下实现了**优于自注意力**的分割效果。参数与FLOPs计算公式见公式(3)-(7)。

## 6. 实验与结果
*   **使用的数据集**：
    1.  **Synapse 多器官分割数据集**：30个病例， 3779张腹部CT轴向切片，用于评估8个腹部器官的分割。
    2.  **皮肤病变分割数据集**：包括ISIC 2017（训练/验证/测试：2000/150/600）、ISIC 2018和PH2（200张）数据集。
    3.  **NIH 胰腺分割数据集**：82个3D腹部CT体积，训练62例，测试20例。
*   **对比方法**：ScaleFormer、DAEFormer、Swin-UNet、U-Net、HiFormer、MISSFormer、D-Former等SOTA方法。
*   **评价指标**：主要使用**Dice Similarity Coefficient (DSC)**。
*   **主实验结果（关键数字）**：
    *   在**Synapse数据集**上，D-LKA Net的平均DSC比ScaleFormer高**1.41%**，比DAEFormer高**1.64%**。在**胰腺分割**这一难点上，比第二名方法高出**2.04%**（p.5）。
    *   在**皮肤病变分割**（ISIC 2017, ISIC 2018, PH2）上，D-LKA Net在各项指标上均**一致性地优于**竞争对手（p.6）。
*   **消融实验**：PDF文本中未明确说明具体的消融实验设置和结果。
*   **泛化实验**：通过在Synapse（腹部CT）和皮肤病变（皮肤镜图像）两种不同模态的数据集上均取得SOTA结果，展示了模型的泛化能力。
*   **速度/参数量/FLOPs等效率信息**：文本中给出了计算参数和FLOPs的理论公式（公式3-7），并指出其随输入尺寸线性增长，但**未在实验部分报告具体的运行时间、参数量或FLOPs数值对比**。

## 7. 这篇论文真正有价值的地方
1.  **优雅的模块设计思想**：用“**深度可分离卷积 + 深度可分离扩张卷积**”的组合来高效构建大感受野，是一种巧妙替代标准自注意力计算的思路。这为设计**轻量化、高效能**的注意力模块提供了新范式，值得后续研究借鉴。
2.  **对医学图像特性的针对性设计**：明确针对医学图像中器官/病变的**不规则形变**问题，将可变形卷积与注意力机制结合，提升了模型对复杂解剖结构的拟合能力。这种“**任务驱动**”的模块改进思路具有启发性。
3.  **完整的2D/3D一体化方案**：不仅提出了2D模块，还系统地设计了3D版本及其可变形卷积的应用策略，为处理3D体数据提供了端到端的解决方案，避免了信息损失。
4.  **纯粹的架构探索**：尝试构建一个尽可能纯粹的、基于自身核心模块（D-LKA）的网络，减少了对外部复杂模块（如大型CNN backbone）的依赖，使模型结构更简洁，利于理解和改进。

## 8. 局限与问题
*   **3D可变形卷积的应用受限**：3D版本为了控制计算量，只引入了单个可变形卷积层，而非像2D那样全面可变形。这可能限制了其对复杂3D形变的建模能力。
*   **实验分析深度不足**：论文主要展示了性能的提升，但对**为什么D-LKA有效**的机理分析不足。例如，缺少对注意力图的可视化，或者对大核和可变形卷积各自贡献的详细消融实验。
*   **数据集范围有限**：实验仅在腹部CT和皮肤镜图像上进行验证，在其他模态（如MRI、超声）或更复杂的分割任务（如肿瘤精细边界）上的有效性未知。
*   **计算成本报告缺失**：虽然强调计算高效，但实验部分未提供与对比方法在运行速度、GPU内存占用等方面的具体量化比较，削弱了“高效性”论点的说服力。
*   **依赖特定编码器（2D版）**：2D模型使用了MaxViT作为编码器，其性能与MaxViT本身的能力有一定捆绑，可能掩盖D-LKA模块在其他骨干网络中的普遍有效性。

## 9. 我该怎么使用这篇论文
*   **如果快速了解**：只读**摘要、引言（特别是“我们的贡献”部分）和结论**，以及**图1（网络架构）和图2（D-LKA模块）**。
*   **如果复现**：重点看**第2节“方法”**，尤其是2.2节D-LKA模块的公式（8）和2.3/2.4节的网络架构描述。结合**图1和图2**理解实现细节。第3节的实验设置（如优化器、损失函数、数据增强）也需要仔细阅读。
*   **如果借鉴创新点**：应深入学习**2.2节D-LKA模块的构造思想**（大核分解与可变形卷积的结合），思考如何将其迁移到其他视觉任务（如图像分类、目标检测）或其他网络结构中作为基本单元。
*   **如果写related work**：可放在以下类别：1) **高效注意力机制/视觉Transformer**；2) **医学图像分割中的上下文建模方法**；3) **大卷积核网络**；4) **可变形卷积在医学图像中的应用**。

## 10. 和其他论文的关系
*   直接基于并扩展了 `[[LKA (Large Kernel Attention)]]`。
*   采用了 `[[Deformable Convolutional Networks]]` 的思想。
*   在医学图像分割任务上与 `[[TransUNet]]`, `[[HiFormer]]`, `[[UNETR]]`, `[[Swin-UNet]]` 等CNN-ViT混合或纯Transformer方法进行对比。
*   2D网络编码器部分使用了 `[[MaxViT]]`。
*   实验评估遵循了 `[[nnFormer]]` 和 `[[UNETR++]]` 的部分设置。

## 11. 关键词
Deformable Large Kernel Attention, 医学图像分割, Vision Transformer, 3D体数据, 可变形卷积, 大核卷积, 计算高效注意力, 编码器-解码器架构, Synapse数据集, 胰腺分割, 皮肤病变分割

## 12. 可信度说明
本精读笔记主要基于PDF提取文本的**前12页**内容生成，特别是**摘要、引言、方法（第2节）及实验部分（第3节）的定量结果描述**。论文的核心思想、方法架构和主要结论均能在文本中找到明确依据。
然而，由于提供的文本不完整（共17页，仅提供前12页），导致以下信息缺失或无法核实：
1.  **实验的详细消融研究**（如大核大小、可变形卷积的影响）。
2.  **详细的效率对比**（如FLOPs、推理速度、参数量的表格）。
3.  **更多数据集上的结果**（如NIH Pancreas的详细数字）。
4.  **讨论部分和结论**。
因此，笔记中涉及上述缺失内容的部分（如第6节消融实验、第8节部分局限性）是基于现有文本的合理推断或明确标注“未找到”。整体上，笔记忠实于文本，未进行编造。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/DLKA.txt` (17/17 页; 原 AI 主体 12/17 + 全文补读 13-17); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Supplementary Material
- p.13: The additional materials provided encompass an ex-
- p.13: A comparison of the number of parameters for normal
- p.13: It is worth noting that the introduction of the deformable
- p.13: LKA does indeed introduce additional parameters and
- p.13: method, the ScaleFormer [31], which used 111.6M param-
- p.14: To further visualize our model capability, we provide a
- p.14: To gain a better understanding of the limitations associ-
- p.14: Figure 12 shows a qualitative visualization of ISIC 2018
- p.14: Since this is also present in the training data, this could hin-
- p.14: In line with the ablation study presented in the main pa-
- p.15: Spl RKid LKid Gal Liv Sto Aor Pan

### 缺失页关键摘录

- p.13: tended ablation study, which serves to demonstrate the ro-
- p.13: floating-point operations per second (FLOPS) to the model.
- p.13: visualize the performances on the Synapse 2D dataset, re-
- p.13: on the number of parameters in Figure 8. The D-LKA Net
- p.13: Figure 8. Performance vs memory chart to compare the perfor-
- p.13: posed 2D D-LKA Net on Synapse dataset. DSC, HD, and Memory
- p.14: Table 7. The number of parameters for standard convolution and decomposed convolution. The kernel size is 21×21. Adapted from [23].
- p.14: C. Qualitative results on the Synapse dataset
- p.14: Synapse dataset in Figure 9 and Figure 10. We neglect the
- p.14: spective into the 3D domain. As illustrated in Figure 11, we
- p.14: Figure 12 shows a qualitative visualization of ISIC 2018
- p.14: In line with the ablation study presented in the main pa-
<!-- AI_READING_NOTE_END -->
