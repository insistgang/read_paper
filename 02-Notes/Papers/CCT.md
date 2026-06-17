---
title: Escaping the Big Data Paradigm with
authors:
  - "Ali Hassani"
  - "Steven Walton"
  - "Nikhil Shah"
  - "Abulikemu Abuduweili"
  - "Jiachen Li"
  - "Humphrey Shi"
year: 2022
venue: mains, such as science and medicine, would hardly have
doi: 
pdf: [[CCT.pdf]]
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
extract_cache: .paper-cache/extracts/CCT.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/18 pages"
---
# Escaping the Big Data Paradigm with

## 基本信息
- **PDF**: [[CCT.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Escaping the Big Data Paradigm with |
| **作者** | Ali Hassani; Steven Walton; Nikhil Shah; Abulikemu Abuduweili; Jiachen Li; Humphrey Shi |
| **发表时间** | 2022 |
| **刊物/会议** | mains, such as science and medicine, would hardly have |
| **DOI** | 未明确 |

## 摘要

> Class Duck Compact Compact Convolutional MLPHead Vision Transformer Transformer SequencePooling TransformerEncoders (Optional) Positional 0 1 2 3 4 Embedding Reshape With the rise of Transformers as the standard for lan- Convolution Patching ··· guageprocessing, andtheiradvancementsincomputervi- sion, there has been a corresponding growth in parameter sizeandamountsoftrainingdata. Manyhavecometobe- lievethatbecauseofthis,transformersarenotsuitablefor Figure 1: Overview of CVT (right), the basic compact small sets of data. This trend leads to concerns such as: transformer, and CCT (left), the convolutional variant of limitedavailabilityofdataincertainscientificdomainsand our compact transformer models. CCT can be quickly the exclusion of those with limited resource from research trainedfromscratchonsmalldatasets,whileachievinghigh inthefield.Inthispaper,weaimtopresentanapproachfor accuracy (in under 30 minutes one can get 90% on an small-scalelearningbyintroducingCompactTransformers. NV

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：随着Transformer在CV领域的成功，模型规模和数据需求急剧增长，形成了“大数据范式”。这导致在数据有限（如医学、科研）或计算资源有限的研究场景下，使用Transformer变得不现实，限制了研究和应用的普及。
- **之前方法的问题**：
  1. 原始的Vision Transformer (ViT) 在数据量不足时容易过拟合，其作者也明确指出“在没有足够数据时，Transformer的泛化能力不如CNN”。
  2. 后续的改进工作如DeiT、T2T-ViT等，虽然提升了数据效率，但主要关注中等规模数据集（如ImageNet），且DeiT的知识蒸馏方法增加了复杂性和对预训练模型的依赖。
- **核心矛盾**：Transformer凭借自注意力机制具有强大的长程建模能力，但缺乏CNN固有的平移不变性等归纳偏置，导致其在小数据场景下难以学习有效特征，而CNN虽有归纳偏置但缺乏长程依赖建模能力。作者试图在模型设计层面弥合这一矛盾。
## 关键贡献

1. **提出了ViT-Lite**：一个尺寸更小、更紧凑的ViT变体，能够从头在CIFAR-10等小数据集上训练并获得超过90%的准确率，证明了Transformer在小数据场景下的可行性。
2. **引入了序列池化策略（SeqPool）**：一种基于注意力的池化方法，用于替代ViT中的`[class]`令牌或简单的平均池化。该方法对Transformer编码器输出的所有令牌序列进行加权聚合，以生成用于分类的全局表示。
3. **提出了紧凑卷积Transformer (CCT)**：在CVT的基础上，将ViT简单的线性分块和嵌入替换为卷积化的分词器（Convolutional Tokenizer）。这能更好地保留图像的局部信息和跨patch边界的信息，提升性能并增强对输入图像尺寸的灵活性。
4. **在多个基准上取得了有竞争力的结果**：例如，在CIFAR-10上达到98%准确率（仅3.7M参数），在Flowers-102上达到新的SOTA（99.76%），在ImageNet上以远少于ViT的参数量达到了82.71%的准确率。
## 方法

- **整体框架**：论文提出三种模型，其演进关系为：ViT-Lite（小模型） -> CVT（加入序列池化） -> CCT（再加入卷积分词器）。整体流程如图2所示：输入图像经过一个分词阶段（可能是线性投影或卷积），生成一个令牌序列；该序列加入位置编码后输入到一系列Transformer编码器层中；编码器输出的令牌序列通过一个池化阶段（`[class]`令牌、平均池化或序列池化）映射为一个全局特征向量；最后该向量通过一个MLP头进行分类。
- **输入输出**：输入为图像，输出为类别概率分布。
- **关键模块**：
  1. **卷积分词器 (Convolutional Tokenizer)**：这是CCT的核心改进。它首先通过一个或多个卷积层（文中示例为一个卷积层后接一个最大池化层）处理输入图像，然后将特征图展平为一个序列，再通过一个线性层投影到嵌入维度`d`。这取代了ViT中直接将图像划分为不重叠patch并线性嵌入的方法，能够更好地建模局部结构和边界信息。
  2. **Transformer编码器**：与标准ViT相同，由多头自注意力（MHSA）层和MLP层堆叠而成，每层后使用层归一化和残差连接。自注意力作用于整个令牌序列，在空间维度上建立长程依赖。
  3. **序列池化 (SeqPool)**：给定编码器输出序列`x_L ∈ R^{b×n×d}`，通过一个线性层`g`将其映射为`R^{b×n×1}`，然后应用softmax得到每个令牌的注意力权重`x'_L ∈ R^{b×1×n}`。最后，将这些权重与原始序列`x_L`相乘（`z = x'_L * x_L`），得到全局特征向量`z ∈ R^{b×d}`。这本质上是一个注意力加权的全局平均池化。
- **模块连接**：以CCT为例：`输入图像` -> `卷积层 + 池化层` -> `展平与线性投影` -> `（可选）位置嵌入` -> `多层Transformer编码器` -> `序列池化` -> `MLP分类头` -> `输出`。
- **数学公式**：序列池化的核心公式为：`z = softmax( g(x_L)^T ) * x_L`，其中`g`是线性变换。
- **与已有方法的差异**：
  - **与ViT相比**：使用了更小的模型尺寸（ViT-Lite），引入了卷积分词器和序列池化。
  - **与DeiT/T2T-ViT相比**：不依赖大规模数据集或知识蒸馏，专注于小数据场景下的从头训练。
  - **与ConViT/CvT等卷积Transformer相比**：结构更简单直接，专注于模型的小型化和在小数据集上的有效性验证。
- **论文类型特化（注意力类）**：本文的注意力模块（MHSA）作用于图像被分割/卷积后形成的**空间维度**的令牌序列，属于**空间注意力**。CCT通过卷积分词器隐含地引入了**局部**归纳偏置，再通过Transformer编码器中的全局自注意力捕获**全局**依赖。CCT模型本身可视为一个完整的视觉主干网络，其设计（特别是卷积分词器和小尺寸）使其**计算量与参数量远低于标准ViT**，从而在效果和效率之间取得了良好平衡。
## 实验

- **使用的数据集**：CIFAR-10, CIFAR-100, ImageNet-1k, Flowers-102，以及部分NLP任务（具体任务未在提供的文本中详细说明）。
- **对比方法**：标准的ViT、DeiT、各种尺寸的ResNet、以及一些基于神经架构搜索（NAS）的CNN模型。
- **评价指标**：Top-1分类准确率（%）、参数量（Parameters）、计算量（MACs）。
- **主实验结果**：
  - **CIFAR-10**：最佳CCT模型达到98%准确率，仅使用3.7M参数。CCT的轻量版（0.28M参数）仍可达到约90%准确率。
  - **Flowers-102**：CCT取得了99.76%的top-1准确率，为新的SOTA。
  - **ImageNet**：CCT达到82.71%准确率，参数量仅为ViT的29%，同时性能优于DeiT等同规模模型。
  - **与CNN对比**：CCT在CIFAR-10上优于多数CNN模型，进入了该数据集的top-25榜单（无预训练），仅某些通过NAS找到的CNN模型性能更优。
- **消融实验**：PDF提供的文本中未明确说明详细的消融实验表格。但从模型演进（ViT-Lite -> CVT -> CCT）来看，可以推断序列池化和卷积分词器分别带来了性能提升。
- **泛化实验**：实验跨越了图像分类（CIFAR, ImageNet, Flowers）和NLP任务，展示了模型的泛化潜力。
- **速度/参数量/FLOPs等效率信息**：
  - **训练速度**：在单张NVIDIA 2080Ti GPU上，CCT可在30分钟内于CIFAR-10上达到90%准确率；在AMD 5900X CPU上可在30分钟内达到80%准确率。
  - **参数量**：模型最小可达0.22M参数，用于小规模学习的最大模型仅3.8M参数。
  - **计算效率**：由于模型小巧，对硬件要求低，可在普通GPU甚至CPU上进行快速实验。
## 局限

1.  **任务范围有限**：论文主要在图像分类任务上进行验证，未涉及目标检测、语义分割、实例分割等其他核心视觉任务。其方法在更复杂任务上的效果有待验证。
2.  **数据集的局限性**：虽然强调了小数据集，但所用数据集（CIFAR, Flowers-102, ImageNet）仍是标准计算机视觉数据集。在真正的、领域特定的“小数据”（如小众医学影像、遥感图像）上，模型的有效性和泛化能力需要进一步测试。
3.  **实验分析深度**：提供的文本中未包含详细的消融实验和可视化分析（如注意力图），这使得我们难以精确理解每个改进模块（如不同卷积核大小、不同池化策略）的具体贡献机制。
4.  **模型容量天花板**：为了保持紧凑性，模型的设计可能限制了其在更复杂任务或更大规模数据集（如ImageNet）上达到最高精度的潜力，其性能可能无法匹敌那些专为大规模数据设计的巨型模型。
## 个人评论

1.  **思维范式的突破**：它挑战了“Transformer必须搭配大数据”的固有认知，为在资源受限场景下应用Transformer提供了切实可行的方案。这启发研究者不应盲目追求模型和数据规模的扩大，而应思考如何根据具体场景设计更高效、更合适的架构。
2.  **优雅而有效的模块设计**：卷积分词器和序列池化是两个非常简单但效果显著的改进。它们没有引入复杂的注意力变体，而是巧妙地结合了CNN和Transformer的优点。这对于如何改进现有模型提供了很好的示范：从解决核心瓶颈（如信息丢失、表示池化）入手，用最小的改动获得最大的收益。
3.  **极高的实用性和可及性**：论文强调模型可以快速训练、参数少、对硬件要求低。这降低了进入Transformer视觉研究的门槛，使得个人研究者、学生或资源有限的实验室也能复现和拓展前沿工作，这对促进研究的可复现性和民主化非常重要。
4.  **对后续工作的启发**：它证明了将轻量级CNN模块（如卷积层）作为Transformer前端的可行性，这一思路可以延伸到更复杂的视觉任务（如检测、分割）中，设计更高效、数据高效的任务特定Transformer。

### 使用建议

- **如果快速了解**：阅读**摘要**、**引言**（尤其是第一段和最后一段）、以及**实验结果**部分的表格和关键结论。
- **如果复现**：重点阅读**方法**部分，特别是第3.3节（SeqPool）和第3.4节（Convolutional Tokenizer）的具体实现细节，以及论文的附录（文中提及Appendix A总结了模型变体细节）。论文代码已开源，应结合代码阅读。
- **如果借鉴创新点**：
  1.  学习**卷积分词器**的设计思想：用卷积层替代线性投影作为Transformer的输入端，以注入局部归纳偏置。
  2.  学习**序列池化**的实现：作为一种即插即用的、基于注意力的池化策略，可尝试用于其他序列转换任务。
  3.  学习其**“紧凑设计”** 的思路：如何通过调整深度、宽度、头数、patch size等超参数，构建适用于不同场景的轻量级模型。
- **如果写Related Work**：可将本文归类于“**高效Vision Transformer**”或“**面向小数据的视觉Transformer**”这一分支，与ViT、DeiT、T2T-ViT、ConViT等工作进行对比和联系。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于机器学习、计算机视觉领域，具体聚焦于改进Vision Transformer架构，以使其能够高效、有效地在小规模数据集上进行训练。它解决的核心问题是Transformer模型“数据饥渴”的问题，即通常需要海量数据和计算资源才能训练出高性能的模型，这限制了其在数据稀缺的科学、医学等领域的应用。该论文适合放在“B_注意力算子模块”主题下，因为它提出了一种更紧凑、高效的Transformer变体（CCT），其核心是引入了卷积分词器和序列池化这两种注意力机制相关的模块改进。

## 2. 一句话总结
该论文通过引入紧凑的卷积分词器和序列池化机制，证明了经过适当设计的Vision Transformer可以在小数据集上从头训练，并达到与大型CNN模型相媲美甚至超越的性能。

## 3. 背景与问题
- **为什么要做**：随着Transformer在CV领域的成功，模型规模和数据需求急剧增长，形成了“大数据范式”。这导致在数据有限（如医学、科研）或计算资源有限的研究场景下，使用Transformer变得不现实，限制了研究和应用的普及。
- **之前方法的问题**：
  1. 原始的Vision Transformer (ViT) 在数据量不足时容易过拟合，其作者也明确指出“在没有足够数据时，Transformer的泛化能力不如CNN”。
  2. 后续的改进工作如DeiT、T2T-ViT等，虽然提升了数据效率，但主要关注中等规模数据集（如ImageNet），且DeiT的知识蒸馏方法增加了复杂性和对预训练模型的依赖。
- **核心矛盾**：Transformer凭借自注意力机制具有强大的长程建模能力，但缺乏CNN固有的平移不变性等归纳偏置，导致其在小数据场景下难以学习有效特征，而CNN虽有归纳偏置但缺乏长程依赖建模能力。作者试图在模型设计层面弥合这一矛盾。

## 4. 核心贡献
1. **提出了ViT-Lite**：一个尺寸更小、更紧凑的ViT变体，能够从头在CIFAR-10等小数据集上训练并获得超过90%的准确率，证明了Transformer在小数据场景下的可行性。
2. **引入了序列池化策略（SeqPool）**：一种基于注意力的池化方法，用于替代ViT中的`[class]`令牌或简单的平均池化。该方法对Transformer编码器输出的所有令牌序列进行加权聚合，以生成用于分类的全局表示。
3. **提出了紧凑卷积Transformer (CCT)**：在CVT的基础上，将ViT简单的线性分块和嵌入替换为卷积化的分词器（Convolutional Tokenizer）。这能更好地保留图像的局部信息和跨patch边界的信息，提升性能并增强对输入图像尺寸的灵活性。
4. **在多个基准上取得了有竞争力的结果**：例如，在CIFAR-10上达到98%准确率（仅3.7M参数），在Flowers-102上达到新的SOTA（99.76%），在ImageNet上以远少于ViT的参数量达到了82.71%的准确率。

## 5. 方法详解
- **整体框架**：论文提出三种模型，其演进关系为：ViT-Lite（小模型） -> CVT（加入序列池化） -> CCT（再加入卷积分词器）。整体流程如图2所示：输入图像经过一个分词阶段（可能是线性投影或卷积），生成一个令牌序列；该序列加入位置编码后输入到一系列Transformer编码器层中；编码器输出的令牌序列通过一个池化阶段（`[class]`令牌、平均池化或序列池化）映射为一个全局特征向量；最后该向量通过一个MLP头进行分类。
- **输入输出**：输入为图像，输出为类别概率分布。
- **关键模块**：
  1. **卷积分词器 (Convolutional Tokenizer)**：这是CCT的核心改进。它首先通过一个或多个卷积层（文中示例为一个卷积层后接一个最大池化层）处理输入图像，然后将特征图展平为一个序列，再通过一个线性层投影到嵌入维度`d`。这取代了ViT中直接将图像划分为不重叠patch并线性嵌入的方法，能够更好地建模局部结构和边界信息。
  2. **Transformer编码器**：与标准ViT相同，由多头自注意力（MHSA）层和MLP层堆叠而成，每层后使用层归一化和残差连接。自注意力作用于整个令牌序列，在空间维度上建立长程依赖。
  3. **序列池化 (SeqPool)**：给定编码器输出序列`x_L ∈ R^{b×n×d}`，通过一个线性层`g`将其映射为`R^{b×n×1}`，然后应用softmax得到每个令牌的注意力权重`x'_L ∈ R^{b×1×n}`。最后，将这些权重与原始序列`x_L`相乘（`z = x'_L * x_L`），得到全局特征向量`z ∈ R^{b×d}`。这本质上是一个注意力加权的全局平均池化。
- **模块连接**：以CCT为例：`输入图像` -> `卷积层 + 池化层` -> `展平与线性投影` -> `（可选）位置嵌入` -> `多层Transformer编码器` -> `序列池化` -> `MLP分类头` -> `输出`。
- **数学公式**：序列池化的核心公式为：`z = softmax( g(x_L)^T ) * x_L`，其中`g`是线性变换。
- **与已有方法的差异**：
  - **与ViT相比**：使用了更小的模型尺寸（ViT-Lite），引入了卷积分词器和序列池化。
  - **与DeiT/T2T-ViT相比**：不依赖大规模数据集或知识蒸馏，专注于小数据场景下的从头训练。
  - **与ConViT/CvT等卷积Transformer相比**：结构更简单直接，专注于模型的小型化和在小数据集上的有效性验证。
- **论文类型特化（注意力类）**：本文的注意力模块（MHSA）作用于图像被分割/卷积后形成的**空间维度**的令牌序列，属于**空间注意力**。CCT通过卷积分词器隐含地引入了**局部**归纳偏置，再通过Transformer编码器中的全局自注意力捕获**全局**依赖。CCT模型本身可视为一个完整的视觉主干网络，其设计（特别是卷积分词器和小尺寸）使其**计算量与参数量远低于标准ViT**，从而在效果和效率之间取得了良好平衡。

## 6. 实验与结果
- **使用的数据集**：CIFAR-10, CIFAR-100, ImageNet-1k, Flowers-102，以及部分NLP任务（具体任务未在提供的文本中详细说明）。
- **对比方法**：标准的ViT、DeiT、各种尺寸的ResNet、以及一些基于神经架构搜索（NAS）的CNN模型。
- **评价指标**：Top-1分类准确率（%）、参数量（Parameters）、计算量（MACs）。
- **主实验结果**：
  - **CIFAR-10**：最佳CCT模型达到98%准确率，仅使用3.7M参数。CCT的轻量版（0.28M参数）仍可达到约90%准确率。
  - **Flowers-102**：CCT取得了99.76%的top-1准确率，为新的SOTA。
  - **ImageNet**：CCT达到82.71%准确率，参数量仅为ViT的29%，同时性能优于DeiT等同规模模型。
  - **与CNN对比**：CCT在CIFAR-10上优于多数CNN模型，进入了该数据集的top-25榜单（无预训练），仅某些通过NAS找到的CNN模型性能更优。
- **消融实验**：PDF提供的文本中未明确说明详细的消融实验表格。但从模型演进（ViT-Lite -> CVT -> CCT）来看，可以推断序列池化和卷积分词器分别带来了性能提升。
- **泛化实验**：实验跨越了图像分类（CIFAR, ImageNet, Flowers）和NLP任务，展示了模型的泛化潜力。
- **速度/参数量/FLOPs等效率信息**：
  - **训练速度**：在单张NVIDIA 2080Ti GPU上，CCT可在30分钟内于CIFAR-10上达到90%准确率；在AMD 5900X CPU上可在30分钟内达到80%准确率。
  - **参数量**：模型最小可达0.22M参数，用于小规模学习的最大模型仅3.8M参数。
  - **计算效率**：由于模型小巧，对硬件要求低，可在普通GPU甚至CPU上进行快速实验。

## 7. 这篇论文真正有价值的地方
1.  **思维范式的突破**：它挑战了“Transformer必须搭配大数据”的固有认知，为在资源受限场景下应用Transformer提供了切实可行的方案。这启发研究者不应盲目追求模型和数据规模的扩大，而应思考如何根据具体场景设计更高效、更合适的架构。
2.  **优雅而有效的模块设计**：卷积分词器和序列池化是两个非常简单但效果显著的改进。它们没有引入复杂的注意力变体，而是巧妙地结合了CNN和Transformer的优点。这对于如何改进现有模型提供了很好的示范：从解决核心瓶颈（如信息丢失、表示池化）入手，用最小的改动获得最大的收益。
3.  **极高的实用性和可及性**：论文强调模型可以快速训练、参数少、对硬件要求低。这降低了进入Transformer视觉研究的门槛，使得个人研究者、学生或资源有限的实验室也能复现和拓展前沿工作，这对促进研究的可复现性和民主化非常重要。
4.  **对后续工作的启发**：它证明了将轻量级CNN模块（如卷积层）作为Transformer前端的可行性，这一思路可以延伸到更复杂的视觉任务（如检测、分割）中，设计更高效、数据高效的任务特定Transformer。

## 8. 局限与问题
1.  **任务范围有限**：论文主要在图像分类任务上进行验证，未涉及目标检测、语义分割、实例分割等其他核心视觉任务。其方法在更复杂任务上的效果有待验证。
2.  **数据集的局限性**：虽然强调了小数据集，但所用数据集（CIFAR, Flowers-102, ImageNet）仍是标准计算机视觉数据集。在真正的、领域特定的“小数据”（如小众医学影像、遥感图像）上，模型的有效性和泛化能力需要进一步测试。
3.  **实验分析深度**：提供的文本中未包含详细的消融实验和可视化分析（如注意力图），这使得我们难以精确理解每个改进模块（如不同卷积核大小、不同池化策略）的具体贡献机制。
4.  **模型容量天花板**：为了保持紧凑性，模型的设计可能限制了其在更复杂任务或更大规模数据集（如ImageNet）上达到最高精度的潜力，其性能可能无法匹敌那些专为大规模数据设计的巨型模型。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：阅读**摘要**、**引言**（尤其是第一段和最后一段）、以及**实验结果**部分的表格和关键结论。
- **如果复现**：重点阅读**方法**部分，特别是第3.3节（SeqPool）和第3.4节（Convolutional Tokenizer）的具体实现细节，以及论文的附录（文中提及Appendix A总结了模型变体细节）。论文代码已开源，应结合代码阅读。
- **如果借鉴创新点**：
  1.  学习**卷积分词器**的设计思想：用卷积层替代线性投影作为Transformer的输入端，以注入局部归纳偏置。
  2.  学习**序列池化**的实现：作为一种即插即用的、基于注意力的池化策略，可尝试用于其他序列转换任务。
  3.  学习其**“紧凑设计”** 的思路：如何通过调整深度、宽度、头数、patch size等超参数，构建适用于不同场景的轻量级模型。
- **如果写Related Work**：可将本文归类于“**高效Vision Transformer**”或“**面向小数据的视觉Transformer**”这一分支，与ViT、DeiT、T2T-ViT、ConViT等工作进行对比和联系。

## 10. 和其他论文的关系
本文与库中“注意力算子模块”主题下的多篇论文直接相关，是一篇承上启下的工作。
- 它基于并改进了 [[ViT (Vision Transformer)]]。
- 它与 [[DeiT (Data-Efficient Image Transformers)]] 都在探索数据高效性，但路径不同（DeiT依赖训练技巧和蒸馏，CCT依赖架构修改）。
- 它与 [[T2T-ViT]] 都改进了ViT的分词模块，但CCT使用了更简单的卷积分词器。
- 它与 [[ConViT]]、[[CvT]] 等“卷积+Transformer”混合架构属于同类工作，但更侧重于模型的小型化和在小数据上的验证。

## 11. 关键词
Compact Transformers, Vision Transformer, Small-scale Learning, Convolutional Tokenization, Sequence Pooling, Data Efficiency, Lightweight Model, CIFAR-10, ImageNet, Inductive Bias

## 12. 可信度说明
本笔记主要基于提供的PDF文本的前12页内容生成，涵盖了摘要、引言、相关工作、方法详解（部分）以及部分实验结果。提取质量较好，关键的方法描述（如SeqPool公式、CCT架构图）、核心贡献和实验结果数字均直接来源于文本。然而，由于文本截断，以下信息在笔记中未详细涉及或标注为“未明确说明”：**方法部分的完整细节**（如卷积分词器的具体层配置）、**完整的实验结果表格**、**详细的消融实验分析**、以及**附录中的模型配置表**。论文的后6页内容（如完整的实验设置、更多的结果对比、NLP任务结果等）未被包含在提供的文本中。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/CCT.txt` (18/18 页; 原 AI 主体 12/18 + 全文补读 13-18); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-18; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-18。
- **提取情况**: 缺失页 6 页, 其中 6 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: ViT-Lite-7/4CCT-7/3x2
- p.13: ViT-Lite-7/4
- p.13: CIFAR-10 image height and widthTop-1 validation accuracy Figure 5: Image Size vs Accuracy (CIFAR-10)
- p.13: Within this appendix, we extend the analysis from Ap-
- p.13: For our small-scale small-resolution experiments, we con-
- p.13: For CNNs, we observed that some models and datasets
- p.13: We provide a full list of ablated terms showing which fac-
- p.13: To demonstrate the general purpose nature of our model
- p.14: Model PE CIFAR-10 CIFAR-100
- p.14: Conventional Vision Transformers are more dependent on Positional Embedding
- p.14: Compact Convolutional Transformers are less dependent on Positional Embedding
- p.15: Table 9: Difference between tuned and not tuned runs in

### 缺失页关键摘录

- p.13: CIFAR-10 image height and widthTop-1 validation accuracy Figure 5: Image Size vs Accuracy (CIFAR-10)
- p.13: Within this appendix, we extend the analysis from Ap-
- p.13: using different types of positional embedding. Figure 6
- p.13: shows the difference of the accuracy when models are be-
- p.13: ing trained from scratch. On the other hand, Figure 7
- p.13: ages. We note that in Figure 7(a) that we do not provide
- p.13: attention to Figure 6(c) and Figure 7(c) to denote the large
- p.13: dataset separately. However, all experiments that trained
- p.13: Here in Table 8 we present the results from section 4.4.
- p.13: umn refers to variant (see Table 5 for details), “Conv” spec-
- p.13: ble 9). The ﬁrst row in Table 8 is essentially ViT. The next
- p.13: numbers reported in this table are best out of 4.
<!-- AI_READING_NOTE_END -->
