---
title: "SCKansformer: Fine-Grained Classification of"
authors:
  - "Yifei Chen"
  - "Zhu Zhu"
  - "Shenghao Zhu"
  - "Linwei Qiu"
  - "Binfeng Zou"
  - "Fan Jia"
  - "Yunpeng Zhu"
  - "Chenyan Zhang"
  - "Zhaojie Fang"
  - "Feiwei Qin"
  - "Jin Fan"
  - "Changmiao Wang"
  - "Yu Gao"
  - "Gang Yu"
year: 2024
venue: Index Terms—Cell Classification, Kolmogorov-Arnold
doi: 
pdf: [[SCKansformer.pdf]]
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
extract_cache: .paper-cache/extracts/SCKansformer.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# SCKansformer: Fine-Grained Classification of

## 基本信息
- **PDF**: [[SCKansformer.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SCKansformer: Fine-Grained Classification of |
| **作者** | Yifei Chen; Zhu Zhu; Shenghao Zhu; Linwei Qiu; Binfeng Zou; Fan Jia; Yunpeng Zhu; Chenyan Zhang; Zhaojie Fang; Feiwei Qin; Jin Fan; Changmiao Wang; Yu Gao; Gang Yu |
| **发表时间** | 2024 |
| **刊物/会议** | Index Terms—Cell Classification, Kolmogorov-Arnold |
| **DOI** | 未明确 |

## 摘要

> —The incidence and mortality rates of malig- classification methods across all datasets. Our source nant tumors, such as acute leukemia, have risen signifi- code and private BMCD-FGCD dataset are available at cantly.Clinically,hospitalsrelyoncytologicalexamination https://github.com/JustlfC03/SCKansformer. of peripheral blood and bone marrow smears to diagnose

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：急性白血病等恶性肿瘤发病率和死亡率上升，临床依赖骨髓涂片细胞学检查确诊。骨髓涂片需分类**近40种**白血细胞，其形态相似，人工分类耗时、主观性强且易出错。自动化分类对辅助诊断至关重要。
- **之前方法的问题**：
    1.  传统机器学习方法（如SVM）流程繁琐，提取的特征模糊，难以区分相似的骨髓细胞。
    2.  基于CNN的方法受限于卷积核的感受野，**难以学习图像中的长距离依赖关系**，导致对细微特征差异的捕捉能力不足。
    3.  现有自动化方法在处理高维显微图像时存在**特征表达能力低、可解释性差、特征提取冗余**等问题。
- **核心矛盾**：如何从**成像条件多变、类别间差异极小、长尾分布严重、分辨率对比度较低**的骨髓显微图像中，准确、高效地提取并区分**近40类**外观高度相似的细胞。
## 关键贡献

1.  **Kansformer编码器**：提出用Kolmogorov-Arnold网络（KAN）替代Vision Transformer（ViT）中的传统MLP层，构成Kansformer编码器。这增强了模型对高维图像数据的**非线性特征表示能力和可解释性**（p.2）。
2.  **增强的特征表示模块**：模型集成了SCConv编码器和全局-局部注意力编码器（GLAE）。
    - **SCConv编码器**：包含空间重建单元（SRU）和通道重建单元（CRU），通过分离-重建和分离-变换-融合策略，**减少CNN提取特征中的空间和通道冗余**（p.2）。
    - **全局-局部注意力编码器（GLAE）**：结合多头自注意力（MSA）模块与局部部件（Local Part）模块，**同时捕捉显微图像的全局长距离依赖和局部精细特征**，提升分类可靠性（p.2）。
3.  **BMCD-FGCD数据集**：与浙江大学医学院附属儿童医院合作，构建并公开了一个**超过10,000个样本、涵盖近40个分类**的“骨髓细胞细粒度分类数据集（BMCD-FGCD）”（p.3）。
4.  **实验验证**：在私有BMCD-FGCD数据集以及公开的PBC和ALL-IDB数据集上进行的对比实验表明，SCKansformer模型**在所有数据集上均优于**典型和先进的微观细胞分类方法（p.1, p.3）。
## 方法

**整体框架**：SCKansformer模型主要由三个核心组件构成：**Kansformer编码器**、**SCConv编码器**和**全局-局部注意力编码器（GLAE）**（p.4）。
**输入输出**：输入为骨髓血细胞显微图像，输出为对应近40个类别的分类结果。
**关键模块与连接方式**：
1.  **Kansformer编码器**：这是模型的骨干部分。它基于Vision Transformer（ViT）结构，但将其中的**MLP层替换为KAN网络**。结构由交替的多头自注意力（MSA）层和KAN网络层构成。KAN基于Kolmogorov-Arnold表示定理，其可学习的激活函数放置在神经元（边）上，而非节点上，这被认为能提升函数逼近效率和可解释性（p.4）。
2.  **SCConv编码器**：用于优化从CNN（可能指图像Patch嵌入或中间特征）提取的特征。
    - **空间重建单元（SRU）**：针对**空间冗余**，采用分离-重建策略。
    - **通道重建单元（CRU）**：针对**通道冗余**，采用分离-变换-融合策略。
    这两个单元协同工作，降低特征冗余，使模型更高效（p.4）。
3.  **全局-局部注意力编码器（GLAE）**：
    - **MSA模块**：学习**全局**的长距离依赖关系。
    - **局部部件（Local Part）模块**：专注于捕获**局部**精细特征。
    该编码器将两者结合，以更全面地表征细胞图像的显式和隐式特征（p.2, p.4）。
**数学公式或机制的直观解释**：论文指出KAN替代MLP增强了非线性表示和可解释性；SCConv通过空间和通道的重建降低冗余；GLAE的“全局-局部”设计是为了同时获取图像的整体语义和关键局部细节。
**训练方式、推理流程**：PDF文本中未明确说明具体训练策略（如损失函数、优化器）和详细的推理流程步骤。
**和已有方法的差异**：与传统ViT（使用MLP）相比，本模型用KAN提升了表示能力；与普通CNN相比，引入了Transformer结构和全局注意力来克服感受野限制；与已有血液细胞分类方法相比，本方法是一个专门为骨髓细胞细粒度分类设计的端到端框架，整合了多种模块。
**论文类型特化（注意力类）**：
- **注意力作用维度**：GLAE中的MSA模块作用于**全局（整个图像或长序列）维度**，Local Part模块作用于**局部维度**，实现了多尺度或跨尺度的注意力。
- **可插入网络**：SCConv和GLAE设计为可集成的编码器模块。
- **计算量 vs 效果**：论文旨在通过更有效的特征表示（KAN， SCConv）和更强的特征捕获能力（GLAE）来提升分类准确率，以应对细粒度分类的挑战。PDF文本中未提供具体的计算量（如FLOPs）与效果对比分析。
## 实验

**使用的数据集**：
- **私有数据集**：BMCD-FGCD（超过10,000个样本，近40个分类）（p.1, p.3）。
- **公开数据集**：PBC（外周血细胞）和ALL-IDB（急性淋巴细胞白血病）数据集（p.1, p.3）。
**对比方法**：论文提及与“典型和先进的微观细胞分类方法”进行比较（p.1, p.3），但**PDF文本中未列出具体的对比方法名称**。
**评价指标**：**PDF文本中未明确说明**使用的具体评价指标（如准确率、F1分数等）。
**主实验结果**：论文称SCKansformer“在所有数据集上均优于其他方法”（p.1, p.3）。然而，在提供的文本中**未给出任何具体的性能数字（如准确率百分比）**。
**消融实验**：论文提到进行了消融实验以验证SCKansformer中每个模块的有效性和必要性（p.3），但**PDF文本中未提供任何消融实验的结果**。
**泛化实验**：论文提及模型在处理不平衡细胞类别数据集和平衡数据集时均表现优异，展示了其广泛适用性（p.3）。
**速度/参数量/FLOPs等效率信息**：**PDF文本中未提供**任何关于模型效率的信息。
## 局限

1.  **实验细节缺失**：基于提供的PDF文本，无法评估实验的充分性。缺少具体的对比方法、详细的实验结果数字、消融实验数据以及效率分析，使得模型的优越性论证不够扎实。
2.  **方法普适性存疑**：模型针对骨髓细胞这一高度专业化场景设计，其组件（如SCConv）在通用视觉任务（如ImageNet分类）中的效果未知。KAN的引入是否会在大模型或大规模数据集上带来显著收益，也需要进一步验证。
3.  **计算成本未知**：KAN、SCConv以及全局-局部注意力模块的引入很可能增加了模型复杂度和计算开销，但文本未提供相关分析，这在实际临床部署中可能是一个关键限制因素。
4.  **可解释性承诺未充分兑现**：论文声称KAN提升了可解释性，但文本中未展示任何关于模型决策过程可解释性的实例或分析（如注意力可视化、KAN的函数形状可视化）。
## 个人评论

1.  **问题驱动的模块化设计**：论文清晰地指出了骨髓细胞分类的四大挑战（长尾、细粒度、成像差异、低分辨率），并针对性地提出三大模块（Kansformer、SCConv、GLAE）分别应对特征表示、冗余和长距离依赖问题。这种“问题-方案”对应的研究思路值得学习。
2.  **KAN在视觉Transformer中的应用**：展示了将新兴的、理论背景更强的Kolmogorov-Arnold网络引入视觉主干网络的可行性，为改善模型的可解释性和非线性能力提供了新思路。
3.  **医疗数据特化处理**：SCConv的设计思想——针对显微图像特征冗余进行优化，以及全局-局部注意力针对细胞形态分析的设计，对处理其他高维、高冗余、需关注局部细节的医学图像（如病理切片）有直接借鉴意义。
4.  **构建并公开高质量私有数据集**：与医院合作构建并共享了规模较大、分类细致的BMCD-FGCD数据集，解决了该领域数据稀缺的瓶颈问题，为后续研究提供了重要资源。

### 使用建议

- **如果快速了解**：只读 **“摘要”、“I. 引言”** 和 **“III. 方法 A. 整体架构”** 部分，即可掌握论文动机、核心思想和框架概览。
- **如果复现**：重点精读 **“III. 方法”** 部分，尤其是对Kansformer、SCConv、GLAE三个模块的描述，并结合论文图示（Fig. 1）理解数据流。同时需要去其提供的GitHub仓库（`https://github.com/JustlfC03/SCKansformer`）获取代码、模型细节和数据集。
- **如果借鉴创新点**：
    - 想应用**KAN**：学习Kansformer编码器如何用KAN替代MLP。
    - 想优化**特征冗余**：学习SCConv中SRU和CRU的“分离-重建/变换-融合”策略。
    - 想设计**多尺度注意力**：学习GLAE中“全局（MSA）+局部（Local Part）”的结合方式。
- **如果写related work**：可放在 **“基于Transformer的医学图像分类”**、**“细胞图像细粒度分类”** 或 **“注意力机制在医学影像中的应用”** 这一类别的相关工作中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**医学图像分析**领域的**细粒度图像分类**方向，具体解决**骨髓血细胞（Bone Marrow Cells）的自动化细粒度分类**问题。该任务是辅助诊断急性白血病等恶性血液病的关键环节。论文提出的SCKansformer模型是一个**视觉Transformer变体**，其核心创新在于引入了改进的注意力算子模块（KAN替代MLP，全局-局部注意力）和空间通道重建卷积。因此，该论文适合放在 **“B_注意力算子模块”** 主题下，重点学习其如何将新型网络（KAN）与注意力机制结合以解决特定医学图像分类难题。

## 2. 一句话总结
SCKansformer通过结合Kolmogorov-Arnold网络（KAN）替代传统MLP、空间通道重建卷积（SCConv）以及全局-局部注意力编码器，构建了一个高效的骨干网络，用于应对骨髓血细胞图像细粒度分类中特征冗余、可解释性差和长距离依赖捕捉不足的挑战。

## 3. 背景与问题
- **为什么要做**：急性白血病等恶性肿瘤发病率和死亡率上升，临床依赖骨髓涂片细胞学检查确诊。骨髓涂片需分类**近40种**白血细胞，其形态相似，人工分类耗时、主观性强且易出错。自动化分类对辅助诊断至关重要。
- **之前方法的问题**：
    1.  传统机器学习方法（如SVM）流程繁琐，提取的特征模糊，难以区分相似的骨髓细胞。
    2.  基于CNN的方法受限于卷积核的感受野，**难以学习图像中的长距离依赖关系**，导致对细微特征差异的捕捉能力不足。
    3.  现有自动化方法在处理高维显微图像时存在**特征表达能力低、可解释性差、特征提取冗余**等问题。
- **核心矛盾**：如何从**成像条件多变、类别间差异极小、长尾分布严重、分辨率对比度较低**的骨髓显微图像中，准确、高效地提取并区分**近40类**外观高度相似的细胞。

## 4. 核心贡献
1.  **Kansformer编码器**：提出用Kolmogorov-Arnold网络（KAN）替代Vision Transformer（ViT）中的传统MLP层，构成Kansformer编码器。这增强了模型对高维图像数据的**非线性特征表示能力和可解释性**（p.2）。
2.  **增强的特征表示模块**：模型集成了SCConv编码器和全局-局部注意力编码器（GLAE）。
    - **SCConv编码器**：包含空间重建单元（SRU）和通道重建单元（CRU），通过分离-重建和分离-变换-融合策略，**减少CNN提取特征中的空间和通道冗余**（p.2）。
    - **全局-局部注意力编码器（GLAE）**：结合多头自注意力（MSA）模块与局部部件（Local Part）模块，**同时捕捉显微图像的全局长距离依赖和局部精细特征**，提升分类可靠性（p.2）。
3.  **BMCD-FGCD数据集**：与浙江大学医学院附属儿童医院合作，构建并公开了一个**超过10,000个样本、涵盖近40个分类**的“骨髓细胞细粒度分类数据集（BMCD-FGCD）”（p.3）。
4.  **实验验证**：在私有BMCD-FGCD数据集以及公开的PBC和ALL-IDB数据集上进行的对比实验表明，SCKansformer模型**在所有数据集上均优于**典型和先进的微观细胞分类方法（p.1, p.3）。

## 5. 方法详解
**整体框架**：SCKansformer模型主要由三个核心组件构成：**Kansformer编码器**、**SCConv编码器**和**全局-局部注意力编码器（GLAE）**（p.4）。
**输入输出**：输入为骨髓血细胞显微图像，输出为对应近40个类别的分类结果。
**关键模块与连接方式**：
1.  **Kansformer编码器**：这是模型的骨干部分。它基于Vision Transformer（ViT）结构，但将其中的**MLP层替换为KAN网络**。结构由交替的多头自注意力（MSA）层和KAN网络层构成。KAN基于Kolmogorov-Arnold表示定理，其可学习的激活函数放置在神经元（边）上，而非节点上，这被认为能提升函数逼近效率和可解释性（p.4）。
2.  **SCConv编码器**：用于优化从CNN（可能指图像Patch嵌入或中间特征）提取的特征。
    - **空间重建单元（SRU）**：针对**空间冗余**，采用分离-重建策略。
    - **通道重建单元（CRU）**：针对**通道冗余**，采用分离-变换-融合策略。
    这两个单元协同工作，降低特征冗余，使模型更高效（p.4）。
3.  **全局-局部注意力编码器（GLAE）**：
    - **MSA模块**：学习**全局**的长距离依赖关系。
    - **局部部件（Local Part）模块**：专注于捕获**局部**精细特征。
    该编码器将两者结合，以更全面地表征细胞图像的显式和隐式特征（p.2, p.4）。
**数学公式或机制的直观解释**：论文指出KAN替代MLP增强了非线性表示和可解释性；SCConv通过空间和通道的重建降低冗余；GLAE的“全局-局部”设计是为了同时获取图像的整体语义和关键局部细节。
**训练方式、推理流程**：PDF文本中未明确说明具体训练策略（如损失函数、优化器）和详细的推理流程步骤。
**和已有方法的差异**：与传统ViT（使用MLP）相比，本模型用KAN提升了表示能力；与普通CNN相比，引入了Transformer结构和全局注意力来克服感受野限制；与已有血液细胞分类方法相比，本方法是一个专门为骨髓细胞细粒度分类设计的端到端框架，整合了多种模块。
**论文类型特化（注意力类）**：
- **注意力作用维度**：GLAE中的MSA模块作用于**全局（整个图像或长序列）维度**，Local Part模块作用于**局部维度**，实现了多尺度或跨尺度的注意力。
- **可插入网络**：SCConv和GLAE设计为可集成的编码器模块。
- **计算量 vs 效果**：论文旨在通过更有效的特征表示（KAN， SCConv）和更强的特征捕获能力（GLAE）来提升分类准确率，以应对细粒度分类的挑战。PDF文本中未提供具体的计算量（如FLOPs）与效果对比分析。

## 6. 实验与结果
**使用的数据集**：
- **私有数据集**：BMCD-FGCD（超过10,000个样本，近40个分类）（p.1, p.3）。
- **公开数据集**：PBC（外周血细胞）和ALL-IDB（急性淋巴细胞白血病）数据集（p.1, p.3）。
**对比方法**：论文提及与“典型和先进的微观细胞分类方法”进行比较（p.1, p.3），但**PDF文本中未列出具体的对比方法名称**。
**评价指标**：**PDF文本中未明确说明**使用的具体评价指标（如准确率、F1分数等）。
**主实验结果**：论文称SCKansformer“在所有数据集上均优于其他方法”（p.1, p.3）。然而，在提供的文本中**未给出任何具体的性能数字（如准确率百分比）**。
**消融实验**：论文提到进行了消融实验以验证SCKansformer中每个模块的有效性和必要性（p.3），但**PDF文本中未提供任何消融实验的结果**。
**泛化实验**：论文提及模型在处理不平衡细胞类别数据集和平衡数据集时均表现优异，展示了其广泛适用性（p.3）。
**速度/参数量/FLOPs等效率信息**：**PDF文本中未提供**任何关于模型效率的信息。

## 7. 这篇论文真正有价值的地方
1.  **问题驱动的模块化设计**：论文清晰地指出了骨髓细胞分类的四大挑战（长尾、细粒度、成像差异、低分辨率），并针对性地提出三大模块（Kansformer、SCConv、GLAE）分别应对特征表示、冗余和长距离依赖问题。这种“问题-方案”对应的研究思路值得学习。
2.  **KAN在视觉Transformer中的应用**：展示了将新兴的、理论背景更强的Kolmogorov-Arnold网络引入视觉主干网络的可行性，为改善模型的可解释性和非线性能力提供了新思路。
3.  **医疗数据特化处理**：SCConv的设计思想——针对显微图像特征冗余进行优化，以及全局-局部注意力针对细胞形态分析的设计，对处理其他高维、高冗余、需关注局部细节的医学图像（如病理切片）有直接借鉴意义。
4.  **构建并公开高质量私有数据集**：与医院合作构建并共享了规模较大、分类细致的BMCD-FGCD数据集，解决了该领域数据稀缺的瓶颈问题，为后续研究提供了重要资源。

## 8. 局限与问题
1.  **实验细节缺失**：基于提供的PDF文本，无法评估实验的充分性。缺少具体的对比方法、详细的实验结果数字、消融实验数据以及效率分析，使得模型的优越性论证不够扎实。
2.  **方法普适性存疑**：模型针对骨髓细胞这一高度专业化场景设计，其组件（如SCConv）在通用视觉任务（如ImageNet分类）中的效果未知。KAN的引入是否会在大模型或大规模数据集上带来显著收益，也需要进一步验证。
3.  **计算成本未知**：KAN、SCConv以及全局-局部注意力模块的引入很可能增加了模型复杂度和计算开销，但文本未提供相关分析，这在实际临床部署中可能是一个关键限制因素。
4.  **可解释性承诺未充分兑现**：论文声称KAN提升了可解释性，但文本中未展示任何关于模型决策过程可解释性的实例或分析（如注意力可视化、KAN的函数形状可视化）。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读 **“摘要”、“I. 引言”** 和 **“III. 方法 A. 整体架构”** 部分，即可掌握论文动机、核心思想和框架概览。
- **如果复现**：重点精读 **“III. 方法”** 部分，尤其是对Kansformer、SCConv、GLAE三个模块的描述，并结合论文图示（Fig. 1）理解数据流。同时需要去其提供的GitHub仓库（`https://github.com/JustlfC03/SCKansformer`）获取代码、模型细节和数据集。
- **如果借鉴创新点**：
    - 想应用**KAN**：学习Kansformer编码器如何用KAN替代MLP。
    - 想优化**特征冗余**：学习SCConv中SRU和CRU的“分离-重建/变换-融合”策略。
    - 想设计**多尺度注意力**：学习GLAE中“全局（MSA）+局部（Local Part）”的结合方式。
- **如果写related work**：可放在 **“基于Transformer的医学图像分类”**、**“细胞图像细粒度分类”** 或 **“注意力机制在医学影像中的应用”** 这一类别的相关工作中。

## 10. 和其他论文的关系
根据主题 `B_注意力算子模块` 和文件名`SCKansformer.pdf`，可能相关的论文包括：
- 其他将**KAN或MLP变体**用于视觉任务的论文，如原始的**KAN论文**或**MLP-Mixer**等。
- 提出各种**注意力机制**（如局部注意力、轴向注意力、通道注意力）用于图像分类的论文。
- 在**医学图像**（尤其是病理学、血液学）中应用**Transformer**的论文。
- 讨论**细粒度视觉分类**的通用方法或针对**生物医学图像**的方法。

## 11. 关键词
骨髓血细胞分类, 细粒度图像分类, Kolmogorov-Arnold网络 (KAN), 空间通道重建卷积 (SCConv), 全局-局部注意力, Vision Transformer (ViT), 医学图像分析, 特征冗余, 长距离依赖, 显微图像

## 12. 可信度说明
本精读笔记**完全基于用户提供的PDF提取文本（前12页/共15页）** 生成。内容忠实于原文，所有陈述、引用和结论均源自该文本。笔记中所有未能找到的信息（如具体实验结果、对比方法列表、评价指标等）均已明确标注“PDF文本中未明确说明”或“PDF文本中未提供”。由于提供的文本不完整，主要缺少实验与结果部分（第6节），因此该部分内容较为简略。整体而言，提取的文本质量良好，清晰地呈现了论文的动机、核心思想和方法框架，但缺乏支撑完整评估的实验细节。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/SCKansformer.txt` (15/15 页; 原 AI 主体 12/15 + 全文补读 13-15); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Method Precision Recall F1-score Accuracy
- p.13: Combined with the ablation experiment results on the im-
- p.13: CONCLUSION
- p.13: This paper proposes a novel fine-grained classification
- p.13: This enables the model to accurately extract and represent
- p.13: This combination addresses the difficulty of simultaneously
- p.13: Through these innovative designs, the SCKansformer model
- p.13: In addition, the development of myeloid blood cell clas-
- p.13: The establishment and disclosure of the BMCD-FGCD dataset
- p.13: In comparative experiments, we evaluate the SCKansformer
- p.14: 14 IEEE TRANSACTIONS AND JOURNALS TEMPLATE
- p.14: Additionally, we conduct ablation experiments on the BMCD-

### 缺失页关键摘录

- p.13: TABLE II : Comparison with other state-of-the-art models on the PBC public dataset.
- p.13: Method Precision Recall F1-score Accuracy
- p.13: TABLE III : Comparison with other state-of-the-art models on the ALL-IDB public dataset.
- p.13: TABLE IV : SCKansformer ablation experiments on the private BMCD-FGCD dataset.
- p.13: accuracy, emphasizing the importance of these components
- p.13: Combined with the ablation experiment results on the im-
- p.13: balanced BMCD-FGCD dataset, these supplementary experi-
- p.13: greatly improves the accuracy and reliability of classification.
- p.13: excels in managing the complexity and accuracy requirements
- p.13: have jointly developed the BMCD-FGCD dataset with the
- p.13: Department of Hematology at Zhejiang Hospital. This dataset
- p.13: private dataset publicly available to the academic community.
<!-- AI_READING_NOTE_END -->
