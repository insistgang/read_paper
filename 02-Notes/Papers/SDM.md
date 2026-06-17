---
title: "PnPNet: Pull-and-Push Networks for Volumetric"
authors:
  - "Xin You"
  - "Ming Ding"
  - "Minghui Zhang"
  - "Hanxiao Zhang"
  - "Yi Yu"
  - "Jie Yang"
  - "Yun Gu"
year: 2023
venue: "arXiv"
doi: 
pdf: [[SDM.pdf]]
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
extract_cache: .paper-cache/extracts/SDM.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/27 pages"
---
# PnPNet: Pull-and-Push Networks for Volumetric

## 基本信息
- **PDF**: [[SDM.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | PnPNet: Pull-and-Push Networks for Volumetric |
| **作者** | Xin You; Ming Ding; Minghui Zhang; Hanxiao Zhang; Yi Yu; Jie Yang; Yun Gu |
| **发表时间** | 2023 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Preciseboundarysegmentationofvolumetricimagesisacriticaltaskforimage- guideddiagnosisandcomputer-assistedintervention,especiallyforboundarycon- fusioninclinicalpractice. However, U-shapedeepnetworkscannoteffectively resolve this challenge due to the lack of boundary shape constraints. Besides, existingmethodsofrefiningboundariesoveremphasizetheslenderstructure,which resultsintheoverfittingphenomenonduetoneuralnetworks’limitedabilitiesto modeltinyobjects. Inthispaper,wereconceptualizethemechanismofboundary generationbyencompassingthedynamicsofinteractionswithadjacentregions. Moreover,weproposeaunifiednetworktermedPnPNettomodelshapecharacter- isticsoftheconfusedboundaryregion. ThecoreingredientsofPnPNetcontain the pushing and pulling branches. Specifically, based on diffusion theory, we devisethesemanticdifferenceguidancemodule(SDM)fromthepushingbranchto squeezetheboundaryregion. Explicitandimplicitdifferentialinformationinside SDMwillsignificantlyboosttherepresentationabilitiesforinter-

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么做**：精确的体素医学图像分割对临床诊断和治疗至关重要，其本质是准确的边界定位。然而，在实践中普遍存在的“边界混淆”（如边界模糊、标注不一致、相似外观结构相邻）是核心挑战，U型网络因缺乏有效的边界形状约束而难以处理。
- **之前方法的问题**：
    1.  **损失函数约束**：通过多任务学习或专用损失函数对边界进行硬约束。但这种方法对形状不规则的解剖结构泛化能力差，且当边界真值本身不确定时，监督信息会失效。
    2.  **后处理优化**：如PointRend、SegFix等，依赖于高质量、边界清晰的图像，不适用于医学领域模糊或不清晰的边界，且非端到端，计算开销大。
    3.  **基于注意力的增强**：引入先验信息来增强边界特征，但通常是针对特定解剖结构和单一类型的边界混淆设计的，泛化性不足。
    - **共同根本缺陷**：现有方法本质上是将“边界”作为一个独立的、宽度仅为单体素的**细长结构**来增强。但神经网络不擅长建模这种微小物体，导致过拟合和效果不佳。
- **核心矛盾**：如何突破将“边界”视为独立微小结构的传统思路，从边界与相邻区域相互作用的**动态机制**出发，设计一种能够泛化处理多种边界混淆的模型。
## 关键贡献

1.  **问题总结与框架提出**：系统总结了导致边界混淆的三种数据集特征（边界不清/噪声、标注标准不一、相邻相似外观结构），并提出了**PnPNet框架**，通过建模边界区域与其相邻区域的交互动态来解决此问题。
2.  **提出推力分支（SDM）**：基于扩散理论，设计了**语义差分模块（SDM）** 作为推力，用于压缩边界区域。核心改进是引入了**显式与隐式微分关系（EID核）**，增强了其对混淆边界的表示能力。
3.  **提出拉力分支（CCM）**：受K-means和Mask2former启发，设计了**类聚类模块（CCM）** 作为拉力，通过可学习的对象查询（聚类中心）和迭代更新机制来拉伸边界区域。同时，通过引入**中心图谱和语义先验**来生成高质量的初始聚类中心。
4.  **模块的通用性**：证明了SDM和CCM可以作为**即插即用模块**，用于增强包括3D UNet、nnUNet、Swin UNETR在内的多种经典基线模型的分割性能。
5.  **实验验证**：在四个包含不同类型边界混淆的挑战性数据集上，PnPNet在**豪斯多夫距离（HD）和平均对称表面距离（ASSD）** 等边界敏感指标上优于其他CNN和Transformer方法。
## 方法

### 整体框架
PnPNet基于编码器-解码器架构（如3D UNet），其核心是在跳跃连接处并行插入**推力分支（SDM）** 和**拉力分支（CCM）**，形成对抗性动态。

### 输入输出
- **输入**：3D体素医学图像。
- **输出**：像素级的分割掩码。

### 关键模块与连接
1.  **推力分支（SDM - Semantic Difference Module）**
    - **机制**：受**扩散理论**启发。将特征图的平滑过程建模为偏微分方程 `∂F/∂t = D·∇²F` (p.6)。目标是：在远离边界处促进扩散（平滑），在靠近边界处抑制扩散（保持特征），从而“推”开相邻区域，压缩边界不确定性。
    - **核心改进 - EID核**：为了约束卷积核，防止其所有值为负（导致差分信息消失），论文提出了**显式与隐式微分关系（EID）** 的3x3x3卷积核。显式关系通过将立方体的顶点设置为固定正负值来建立；隐式关系由核中剩余的19个可学习值产生（p.4）。
    - **连接**：SDM作用于编码器的跳跃连接特征，生成边界增强（压缩后）的特征，再送入解码器。

2.  **拉力分支（CCM - Class Clustering Module）**
    - **机制**：受**K-means聚类**和Mask2former中的对象查询启发。引入一组可学习的**对象查询**，视为不同类别的聚类中心（p.4）。
    - **工作流程**：
        a. 计算聚类中心与跳跃连接特征（体素嵌入）的相似度，得到**聚类分割掩码**。
        b. 利用该掩码对特征进行加权聚合，**迭代更新聚类中心**。
        c. 在此过程中，聚类中心沿着等值面梯度方向移动至真实中心，同时边界两侧区域被“拉”向各自的中心，从而拉伸了边界区域。
    - **初始化优化**：为促进可学习中心的收敛，引入了**中心图谱（Center Atlas）** 和**语义先验信息**来生成高质量的初始聚类中心（p.4）。
    - **连接**：CCM同样作用于跳跃连接特征，生成拉伸边界后的特征表示。

### 数学公式与直观解释
- **SDM的数学基础**：扩散方程 `∂F/∂t = D·∇²F`。直观理解：想象一滴墨水（边界混淆区域）在清水中扩散。扩散系数`D`控制速度，目标是让边界清晰（墨水停留在原区域，清水保持清澈）。
- **CCM的数学基础**：基于相似度的聚类。直观理解：把每个体素分配给距离最近的类中心，然后更新类中心。这个过程会把边界附近的体素“拉”向正确的类别，从而明确边界。

### 训练与推理
- **训练方式**：PDF文本中未明确说明具体的损失函数细节，但指出两个分支在训练中提供对抗力并达到动态平衡（p.6）。
- **推理流程**：PDF文本中未明确说明。基于框架图推断，推理时图像经过编码器，在跳跃连接处通过SDM和CCM处理特征，再由解码器融合输出分割结果。

### 与已有方法的差异
已有方法将边界视为**被动增强的独立细长结构**，而本文将其视为由相邻区域交互产生的**动态界面**，并通过模拟“推力”（SDM，压缩）和“拉力”（CCM，拉伸）这对**对抗过程**来主动建模这种动态，这是根本性的差异。

### 论文类型特化（注意力类）
- **作用维度**：SDM可视为一种**空间和通道混合的、基于物理模型的注意力机制**。它通过扩散过程（PDE）在空间上引导特征平滑与否，并利用深层语义信息指导，最终作用于编码器的多尺度特征图上。
- **可插入性**：SDM和CCM均被设计为**即插即用模块**，可应用于CNN（如UNet）、Transformer（如Swin UNETR）等多种骨干网络。
- **计算量 vs 效果**：PDF文本中未提供具体的计算量（FLOPs）或参数量对比数据，但强调其模块设计是模块化的，且实验中展示了作为插件时的有效性提升。
## 实验

- **使用的数据集**：三个具有挑战性的**公开数据集**和一个**内部数据集**，涵盖了三种不同类型的边界混淆（p.1）。具体数据集名称在提供的文本中未列出。
- **对比方法**：PDF文本中未明确列出所有对比方法，但提到了与其他CNN和Transformer模型的比较（p.5）。
- **评价指标**：**豪斯多夫距离（Hausdorff Distance, HD）** 和 **平均对称表面距离（Average Symmetric Surface Distance, ASSD）** 被特别强调为关键指标（p.1, p.5）。此外，通常也会使用Dice系数。
- **主实验结果**：**PDF文本中未提供具体的数字结果**。结论指出PnPNet在以上指标上优于其他方法，特别是在HD和ASSD上表现突出（p.1, p.5）。
- **消融实验**：**PDF文本中未明确说明**。但从贡献描述中可以推断，应包含对SDM和CCM各自作用、以及它们联合作用的消融。
- **泛化实验**：验证了SDM和CCM作为即插即用模块，能够提升多种基线模型（如3D UNet, MedNeXt, TransUNet, UNeXt等）在四个数据集上的性能（p.6, p.3）。
- **效率信息**：**PDF文本中未提供**具体的速度、参数量或FLOPs比较。
## 局限

1.  **数据集信息缺失**：在提供的文本中，未提及具体使用的公开数据集名称，这影响了对实验泛化性的具体判断。
2.  **计算成本未知**：论文未讨论SDM和CCM引入的额外计算开销（参数、内存、推理时间），这对于模型的实际部署是一个重要考量。
3.  **训练细节不明确**：损失函数的具体形式（特别是如何平衡推力、拉力与主分割损失）在提供的文本中没有说明，这对复现至关重要。
4.  **理论假设的依赖性**：方法依赖于“边界由相邻区域动态生成”这一物理隐喻，其普遍有效性在更极端的边界混淆场景（如肿瘤浸润性边界）中可能受限。
5.  **泛化性验证范围**：虽然声称在多种数据集上有效，但提供的文本中数据集的具体情况和数量有限，其对于完全不同成像模态（如MRI、超声）和分割任务的泛化能力有待进一步验证。
## 个人评论

1.  **新颖的问题建模视角**：将边界问题从“增强一个细长结构”重新定义为“建模相邻区域的对抗性动态”，这个思路具有启发性，可能适用于其他需要精细边缘划分的领域（如遥感、自然图像抠图）。
2.  **模块化的设计理念**：将核心创新（SDM和CCM）设计为独立的、即插即用的组件，极大地提升了其实用价值。研究者可以轻松地将它们移植到自己的基线模型中，快速验证其有效性。
3.  **物理模型的融合**：将扩散理论（PDE）和聚类思想（K-means）创造性地融合到神经网络模块中，为设计具有可解释性的深度学习模块提供了范例。
4.  **对边界敏感指标的重视**：明确以Hausdorff距离等作为优化目标，这在临床应用中比单纯的区域重叠度量（Dice）更具实际意义，推动了领域关注更贴近临床需求的评估标准。

### 使用建议

- **快速了解**：精读**摘要（Abstract）** 和 **引言（Introduction）** 的后半部分，特别是问题分类、动机图示（Figure 2）和贡献列表。
- **复现**：重点研究**方法论（Methodology）** 部分，特别是SDM的EID核设计和CCM的迭代聚类中心更新流程。同时，需要寻找论文的补充材料或开源代码（文中已给出GitHub链接）以获取训练损失、超参数等细节。
- **借鉴创新点**：
    - **思路借鉴**：学习其“从交互动态出发”的问题建模方式，应用于自己领域的边界/边缘相关问题。
    - **模块借鉴**：直接尝试将**SDM或CCM模块**插入到自己正在使用的分割网络中，尤其是当任务对边界精度要求很高时。
- **写Related Work**：可将其归类在 **“医学图像分割中的边界精炼方法”** 或 **“基于物理模型或注意力机制的边界增强模块”** 相关工作的综述中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**医学图像分割**领域，具体聚焦于解决体素（3D）医学图像中**相邻类别边界模糊或混淆（boundary confusion）** 的精确分割难题。该问题在肺部分叶、心房结构分割等临床场景中普遍存在。论文提出了一个名为PnPNet的对抗性推拉网络架构，并包含了两个核心的、可即插即用的**注意力算子模块**（SDM和CCM），因此适合归入“B_注意力算子模块”这一主题下。

## 2. 一句话总结
针对医学图像中常见的三类边界混淆问题，PnPNet提出一个对抗性“推拉”机制：通过“语义差分模块”（SDM）产生推力压缩边界不确定区域，同时通过“类聚类模块”（CCM）产生拉力拉伸该区域，两力动态平衡以实现更精确的边界分割。

## 3. 背景与问题
- **为什么做**：精确的体素医学图像分割对临床诊断和治疗至关重要，其本质是准确的边界定位。然而，在实践中普遍存在的“边界混淆”（如边界模糊、标注不一致、相似外观结构相邻）是核心挑战，U型网络因缺乏有效的边界形状约束而难以处理。
- **之前方法的问题**：
    1.  **损失函数约束**：通过多任务学习或专用损失函数对边界进行硬约束。但这种方法对形状不规则的解剖结构泛化能力差，且当边界真值本身不确定时，监督信息会失效。
    2.  **后处理优化**：如PointRend、SegFix等，依赖于高质量、边界清晰的图像，不适用于医学领域模糊或不清晰的边界，且非端到端，计算开销大。
    3.  **基于注意力的增强**：引入先验信息来增强边界特征，但通常是针对特定解剖结构和单一类型的边界混淆设计的，泛化性不足。
    - **共同根本缺陷**：现有方法本质上是将“边界”作为一个独立的、宽度仅为单体素的**细长结构**来增强。但神经网络不擅长建模这种微小物体，导致过拟合和效果不佳。
- **核心矛盾**：如何突破将“边界”视为独立微小结构的传统思路，从边界与相邻区域相互作用的**动态机制**出发，设计一种能够泛化处理多种边界混淆的模型。

## 4. 核心贡献
1.  **问题总结与框架提出**：系统总结了导致边界混淆的三种数据集特征（边界不清/噪声、标注标准不一、相邻相似外观结构），并提出了**PnPNet框架**，通过建模边界区域与其相邻区域的交互动态来解决此问题。
2.  **提出推力分支（SDM）**：基于扩散理论，设计了**语义差分模块（SDM）** 作为推力，用于压缩边界区域。核心改进是引入了**显式与隐式微分关系（EID核）**，增强了其对混淆边界的表示能力。
3.  **提出拉力分支（CCM）**：受K-means和Mask2former启发，设计了**类聚类模块（CCM）** 作为拉力，通过可学习的对象查询（聚类中心）和迭代更新机制来拉伸边界区域。同时，通过引入**中心图谱和语义先验**来生成高质量的初始聚类中心。
4.  **模块的通用性**：证明了SDM和CCM可以作为**即插即用模块**，用于增强包括3D UNet、nnUNet、Swin UNETR在内的多种经典基线模型的分割性能。
5.  **实验验证**：在四个包含不同类型边界混淆的挑战性数据集上，PnPNet在**豪斯多夫距离（HD）和平均对称表面距离（ASSD）** 等边界敏感指标上优于其他CNN和Transformer方法。

## 5. 方法详解
### 整体框架
PnPNet基于编码器-解码器架构（如3D UNet），其核心是在跳跃连接处并行插入**推力分支（SDM）** 和**拉力分支（CCM）**，形成对抗性动态。

### 输入输出
- **输入**：3D体素医学图像。
- **输出**：像素级的分割掩码。

### 关键模块与连接
1.  **推力分支（SDM - Semantic Difference Module）**
    - **机制**：受**扩散理论**启发。将特征图的平滑过程建模为偏微分方程 `∂F/∂t = D·∇²F` (p.6)。目标是：在远离边界处促进扩散（平滑），在靠近边界处抑制扩散（保持特征），从而“推”开相邻区域，压缩边界不确定性。
    - **核心改进 - EID核**：为了约束卷积核，防止其所有值为负（导致差分信息消失），论文提出了**显式与隐式微分关系（EID）** 的3x3x3卷积核。显式关系通过将立方体的顶点设置为固定正负值来建立；隐式关系由核中剩余的19个可学习值产生（p.4）。
    - **连接**：SDM作用于编码器的跳跃连接特征，生成边界增强（压缩后）的特征，再送入解码器。

2.  **拉力分支（CCM - Class Clustering Module）**
    - **机制**：受**K-means聚类**和Mask2former中的对象查询启发。引入一组可学习的**对象查询**，视为不同类别的聚类中心（p.4）。
    - **工作流程**：
        a. 计算聚类中心与跳跃连接特征（体素嵌入）的相似度，得到**聚类分割掩码**。
        b. 利用该掩码对特征进行加权聚合，**迭代更新聚类中心**。
        c. 在此过程中，聚类中心沿着等值面梯度方向移动至真实中心，同时边界两侧区域被“拉”向各自的中心，从而拉伸了边界区域。
    - **初始化优化**：为促进可学习中心的收敛，引入了**中心图谱（Center Atlas）** 和**语义先验信息**来生成高质量的初始聚类中心（p.4）。
    - **连接**：CCM同样作用于跳跃连接特征，生成拉伸边界后的特征表示。

### 数学公式与直观解释
- **SDM的数学基础**：扩散方程 `∂F/∂t = D·∇²F`。直观理解：想象一滴墨水（边界混淆区域）在清水中扩散。扩散系数`D`控制速度，目标是让边界清晰（墨水停留在原区域，清水保持清澈）。
- **CCM的数学基础**：基于相似度的聚类。直观理解：把每个体素分配给距离最近的类中心，然后更新类中心。这个过程会把边界附近的体素“拉”向正确的类别，从而明确边界。

### 训练与推理
- **训练方式**：PDF文本中未明确说明具体的损失函数细节，但指出两个分支在训练中提供对抗力并达到动态平衡（p.6）。
- **推理流程**：PDF文本中未明确说明。基于框架图推断，推理时图像经过编码器，在跳跃连接处通过SDM和CCM处理特征，再由解码器融合输出分割结果。

### 与已有方法的差异
已有方法将边界视为**被动增强的独立细长结构**，而本文将其视为由相邻区域交互产生的**动态界面**，并通过模拟“推力”（SDM，压缩）和“拉力”（CCM，拉伸）这对**对抗过程**来主动建模这种动态，这是根本性的差异。

### 论文类型特化（注意力类）
- **作用维度**：SDM可视为一种**空间和通道混合的、基于物理模型的注意力机制**。它通过扩散过程（PDE）在空间上引导特征平滑与否，并利用深层语义信息指导，最终作用于编码器的多尺度特征图上。
- **可插入性**：SDM和CCM均被设计为**即插即用模块**，可应用于CNN（如UNet）、Transformer（如Swin UNETR）等多种骨干网络。
- **计算量 vs 效果**：PDF文本中未提供具体的计算量（FLOPs）或参数量对比数据，但强调其模块设计是模块化的，且实验中展示了作为插件时的有效性提升。

## 6. 实验与结果
- **使用的数据集**：三个具有挑战性的**公开数据集**和一个**内部数据集**，涵盖了三种不同类型的边界混淆（p.1）。具体数据集名称在提供的文本中未列出。
- **对比方法**：PDF文本中未明确列出所有对比方法，但提到了与其他CNN和Transformer模型的比较（p.5）。
- **评价指标**：**豪斯多夫距离（Hausdorff Distance, HD）** 和 **平均对称表面距离（Average Symmetric Surface Distance, ASSD）** 被特别强调为关键指标（p.1, p.5）。此外，通常也会使用Dice系数。
- **主实验结果**：**PDF文本中未提供具体的数字结果**。结论指出PnPNet在以上指标上优于其他方法，特别是在HD和ASSD上表现突出（p.1, p.5）。
- **消融实验**：**PDF文本中未明确说明**。但从贡献描述中可以推断，应包含对SDM和CCM各自作用、以及它们联合作用的消融。
- **泛化实验**：验证了SDM和CCM作为即插即用模块，能够提升多种基线模型（如3D UNet, MedNeXt, TransUNet, UNeXt等）在四个数据集上的性能（p.6, p.3）。
- **效率信息**：**PDF文本中未提供**具体的速度、参数量或FLOPs比较。

## 7. 这篇论文真正有价值的地方
1.  **新颖的问题建模视角**：将边界问题从“增强一个细长结构”重新定义为“建模相邻区域的对抗性动态”，这个思路具有启发性，可能适用于其他需要精细边缘划分的领域（如遥感、自然图像抠图）。
2.  **模块化的设计理念**：将核心创新（SDM和CCM）设计为独立的、即插即用的组件，极大地提升了其实用价值。研究者可以轻松地将它们移植到自己的基线模型中，快速验证其有效性。
3.  **物理模型的融合**：将扩散理论（PDE）和聚类思想（K-means）创造性地融合到神经网络模块中，为设计具有可解释性的深度学习模块提供了范例。
4.  **对边界敏感指标的重视**：明确以Hausdorff距离等作为优化目标，这在临床应用中比单纯的区域重叠度量（Dice）更具实际意义，推动了领域关注更贴近临床需求的评估标准。

## 8. 局限与问题
1.  **数据集信息缺失**：在提供的文本中，未提及具体使用的公开数据集名称，这影响了对实验泛化性的具体判断。
2.  **计算成本未知**：论文未讨论SDM和CCM引入的额外计算开销（参数、内存、推理时间），这对于模型的实际部署是一个重要考量。
3.  **训练细节不明确**：损失函数的具体形式（特别是如何平衡推力、拉力与主分割损失）在提供的文本中没有说明，这对复现至关重要。
4.  **理论假设的依赖性**：方法依赖于“边界由相邻区域动态生成”这一物理隐喻，其普遍有效性在更极端的边界混淆场景（如肿瘤浸润性边界）中可能受限。
5.  **泛化性验证范围**：虽然声称在多种数据集上有效，但提供的文本中数据集的具体情况和数量有限，其对于完全不同成像模态（如MRI、超声）和分割任务的泛化能力有待进一步验证。

## 9. 我该怎么使用这篇论文
- **快速了解**：精读**摘要（Abstract）** 和 **引言（Introduction）** 的后半部分，特别是问题分类、动机图示（Figure 2）和贡献列表。
- **复现**：重点研究**方法论（Methodology）** 部分，特别是SDM的EID核设计和CCM的迭代聚类中心更新流程。同时，需要寻找论文的补充材料或开源代码（文中已给出GitHub链接）以获取训练损失、超参数等细节。
- **借鉴创新点**：
    - **思路借鉴**：学习其“从交互动态出发”的问题建模方式，应用于自己领域的边界/边缘相关问题。
    - **模块借鉴**：直接尝试将**SDM或CCM模块**插入到自己正在使用的分割网络中，尤其是当任务对边界精度要求很高时。
- **写Related Work**：可将其归类在 **“医学图像分割中的边界精炼方法”** 或 **“基于物理模型或注意力机制的边界增强模块”** 相关工作的综述中。

## 10. 和其他论文的关系
基于提供的主题“B_注意力算子模块”，这篇论文提出的SDM模块本身是一种空间注意力机制，因此可能与以下类型的论文相关：
- `[[Diffusion Models in Vision]]`：因其核心模块SDM基于扩散理论。
- `[[Mask2Former]]` 和 `[[MaskFormer]]`：论文的CCM部分受这些工作中的对象查询机制启发。
- `[[Attention Modules for Medical Segmentation]]`：如`[[CBAM]]`, `[[SENet]]`, `[[XBound-Former]]`等，PnPNet提出了针对边界问题的专用注意力模块。
- `[[Boundary-aware Losses]]`：如`[[Hausdorff Distance Loss]]`, `[[Boundary Loss]]`，PnPNet从模型结构而非仅损失函数层面解决边界问题。

## 11. 关键词
医学图像分割，边界混淆，注意力模块，语义差分模块（SDM），类聚类模块（CCM），即插即用，扩散理论，体素分割，豪斯多夫距离，推拉机制，对抗动态。

## 12. 可信度说明
本精读笔记**完全基于提供的PDF文本（前12页）生成**。关键信息如问题定义、核心思想、模块设计（SDM、CCM）、贡献点均来自原文。由于提供的文本仅为论文部分内容（27页中的前12页），以下信息**在提供的文本中未找到**或**不完整**：
- 实验所用的**具体数据集名称**。
- 详细的**实验结果数字**（如具体的Dice、HD值）。
- 完整的**对比方法列表**。
- **消融实验**的具体设置和结果。
- **效率数据**（参数量、FLOPs、推理速度）。
- **训练细节**（损失函数具体形式、优化器参数等）。
- **方法论**中关于**训练和推理流程**的完整描述。
因此，笔记中对这些部分的描述要么基于原文零星提及的信息进行概括，要么明确标注“PDF文本中未明确说明”。提取质量对于理解论文的核心动机、框架和主要模块设计是充足的，但对于复现实验和了解全部细节，则需要参考论文的完整版本和补充材料。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/SDM.txt` (27/27 页; 原 AI 主体 12/27 + 全文补读 13-27); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-27; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-27。
- **提取情况**: 缺失页 15 页, 其中 15 页提取到可读文本。缺失页包含正文/附录内容, 其中约 4 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 4.2 Implementation Details
- p.13: And for both VerSe 2019 and LA/LAA, the settings of the optimizer, the initial learning rate, and the
- p.13: 4.3 Results
- p.13: 4.3.1 Comparisons with other segmentation models
- p.13: results are illustrated in Table 1. Our model achieves the best segmentation performance across the
- p.14: Cervical Thoracic Lumbar Mean Cervical Thoracic Lumbar Mean
- p.14: LAA LA Mean LAA LA Mean
- p.14: COVID-19 infections bear uncertain boundaries with noise adjacent to them, which brings a huge
- p.14: Thus, it is more difficult to train a model to implement the segmentation task for the fused lung
- p.15: Push GT Pull Push GT Pull Push GT Pull
- p.15: experiments on the LA/LAA dataset, which is deficient in the uniform standard for annotations of
- p.15: 4.3.2 Comparisons with other modules on refining boundary confusion

### 缺失页关键摘录

- p.13: Figure 6: Qualitative visualizations. From the first row to the last row: the clean lung lobe, the fused
- p.13: a batch size of 2 in each GPU. For the clean pulmonary lobe dataset, all models are trained with the
- p.13: [75] as the baseline model. For the fused pulmonary lobe dataset, the experimental setting is the
- p.13: same as that of the clean dataset. For the VerSe 2019 dataset, we train all models for 1000 epochs.
- p.13: Here MedNeXt [ 55] is chosen as the baseline model. For the LA/LAA dataset, models are trained
- p.13: learning rate scheduler remain the same as those for the clean pulmonary lobe dataset. For the choice
- p.13: inter-class boundaries, we firstly conduct experiments on the clean lung lobe dataset. The quantitative
- p.13: results are illustrated in Table 1. Our model achieves the best segmentation performance across the
- p.14: Table 3: Comparison with other models on VerSe 2019. (Cerv: Cervical vertebrae, Thor: Thoracic
- p.14: vertebrae, Lumb: Lumbar vertebrae, Mean: the average evaluation metric of all vertebrae. Bold
- p.14: MethodDice score (%) ↑ HD95(mm)↓Params (M) FLOPs (T)
- p.14: Table 4: Comparison with other models on LA/LAA. (LA: Left Atrium, LAA: Left Atrium Ap-
<!-- AI_READING_NOTE_END -->
