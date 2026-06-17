---
title: "GhostNet: More Features from Cheap Operations"
authors:
  - "Noah’sArkLab"
  - "HuaweiTechnologies. 2PekingUniversity."
  - "SchoolofComputerScience"
  - "FacultyofEngineering"
  - "UniversityofSydney."
year: 2012
venue: "arXiv"
doi: 
pdf: [[GhostModule.pdf]]
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
extract_cache: .paper-cache/extracts/GhostModule.txt
---

# GhostNet: More Features from Cheap Operations

## 基本信息
- **PDF**: [[GhostModule.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | GhostNet: More Features from Cheap Operations |
| **作者** | Noah’sArkLab; HuaweiTechnologies. 2PekingUniversity.; SchoolofComputerScience; FacultyofEngineering; UniversityofSydney. |
| **发表时间** | 2012 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Deployingconvolutionalneuralnetworks(CNNs)onem- bedded devices is difficult due to the limited memory and computation resources. The redundancy in feature maps is an important characteristic of those successful CNNs, buthasrarelybeeninvestigatedinneuralarchitecturede- sign. ThispaperproposesanovelGhostmoduletogener- ate more feature maps from cheap operations. Based on asetofintrinsicfeaturemaps,weapplyaseriesoflinear transformations with cheap cost to generate many ghost featuremapsthatcouldfullyrevealinformationunderlying intrinsicfeatures. TheproposedGhostmodulecanbetaken Figure1.Visualizationofsomefeaturemapsgeneratedbythefirst as a plug-and-play component to upgrade existing convo- residualgroupinResNet-50,wherethreesimilarfeaturemappair lutional neural networks. Ghost bottlenecks are designed examplesareannotatedwithboxesofthesamecolor.Onefeature to stack Ghost modules, and then the lightweight Ghost- mapinthepaircanbeapproximatelyobtainedbytransformingthe otheronethroughcheapope

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：将CNN部署到手机、自动驾驶汽车等嵌入式设备时，面临着内存和计算资源严重受限的挑战。传统的CNN（如ResNet-50）参数量和计算量巨大，无法直接应用。
- **之前方法的问题**：1）**模型压缩方法**（如剪枝、量化、知识蒸馏）的性能通常受限于预训练好的基线模型。2）**紧凑模型设计方法**（如MobileNet、ShuffleNet）虽然引入了深度可分离卷积等高效操作，但论文指出，它们并没有很好地利用特征图之间存在的**相关性和冗余性**。
- **核心矛盾**：成功的CNN中，特征图的冗余性是保证其综合理解输入数据的重要特性。传统方法要么忽略这种冗余，要么通过常规卷积昂贵地生成它们。论文旨在**以一种计算成本高效的方式，主动拥抱并利用这种特征图冗余**。
## 关键贡献

1.  **提出了Ghost模块**：一种新的基础计算单元，它将一个卷积分解为两部分：a) 用少量卷积滤波器生成“本征特征图”；b) 对这些本征特征图施加一系列廉价的线性变换（如深度卷积）来生成更多“幽灵特征图”。
2.  **设计了Ghost Bottleneck（G-bneck）**：基于Ghost模块设计的、适用于小型CNN的瓶颈残差结构，可堆叠构建高效网络。
3.  **构建了GhostNet网络架构**：用Ghost Bottleneck替换MobileNetV3中的标准瓶颈模块，形成一个完整的、高效的轻量级网络。
4.  **提出了宽度乘子（Width Multiplier）**：一个简单的缩放因子 `α`，用于均匀调整网络各层的通道数，从而灵活控制模型的大小和计算成本。
5.  **实验验证**：在多个基准数据集（CIFAR-10, ImageNet, COCO）上验证了Ghost模块的有效性以及GhostNet相比MobileNetV3等SOTA轻量模型的优越性能。
## 方法

- **整体框架**：GhostNet的整体架构借鉴了MobileNetV3，由一系列Ghost Bottleneck堆叠而成，具体结构详见论文中的**Table 1**（p.4）。网络从一个标准卷积层开始，接着是多组G-bneck（部分包含SE模块），最后通过全局平均池化和全连接层进行分类。
- **输入输出**：对于Ghost模块，输入特征图 `X ∈ R^(c×h×w)`，输出特征图 `Y ∈ R^(h0×w0×n)`，其中 `n` 为输出通道数。
- **关键模块**：
    1.  **Ghost模块**：是核心创新。如**Figure 2(b)**(p.3)所示，它包含：
        - **主卷积（Primary Convolution）**：用 `m` (`m ≤ n`) 个滤波器 `f0` 对输入 `X` 进行卷积，生成 `m` 张本征特征图 `Y‘`（Eq.2）。其超参数（滤波器大小、步长、填充）与标准卷积相同，以保证输出特征图的空间尺寸不变。
        - **廉价线性操作（Cheap Linear Operations）**：对每一张本征特征图 `y_i’`，应用 `s-1` 个相同的线性变换 `Φ`（论文中通常为 `d×d` 深度卷积）和一个恒等映射，生成 `s` 张幽灵特征图 `y_ij`（Eq.3）。最终，`n = m × s` 张特征图拼接成最终输出。
    2.  **Ghost Bottleneck（G-bneck）**：是GhostNet的基本构建单元。如**Figure 3**(p.4)所示，它由两个Ghost模块堆叠而成：
        - 第一个Ghost模块作为**扩展层**，使用扩展比（expansion ratio）增加通道数。
        - 第二个Ghost模块**减少通道数**以匹配shortcut路径。
        - 两者之间（在步长为2时）会插入一个深度可分离卷积进行下采样。
        - 整体形成一个残差结构，BN和ReLU（第二个Ghost模块后除外）应用于每层之后。
- **模块连接**：多个G-bneck按**Table 1**中的顺序串联。不同G-bneck的输入输出通道数、是否使用SE模块以及步长都有明确规定，形成从浅层到深层的特征提取流水线。
- **数学公式直观解释**：
    - Eq.1：标准卷积 `Y = X * f + b`，计算量巨大。
    - Eq.2 & Eq.3：Ghost模块首先用更少的参数 (`m` 个滤波器) 得到“精简版”特征图 `Y‘`，然后像“克隆”或“变形”一样，对 `Y‘` 中的每个特征图进行便宜的空间变换（`Φ`），生成一组“幽灵”副本。这样，用 `1/s` 的成本获得了 `n` 倍的特征图。
    - Eq.4 & Eq.5：理论上的加速比和压缩比都近似等于扩展因子 `s`（假设 `d≈k` 且 `s<<c`）。
- **训练方式**：论文中提及遵循常用训练策略（如动量、学习率计划），但具体细节（如学习率、优化器、训练轮数）在提供的文本中**未明确说明**。
- **推理流程**：标准的端到端前向传播，输入图像依次经过Table 1中的各层，得到分类结果。
- **和已有方法的差异**：论文在3.1节“Difference from Existing Methods”中明确对比(p.3)：
    1.  **与MobileNet/ShuffleNet比**：主卷积核大小可定制（不一定是1x1），且处理流程相反（先生成少量特征，再扩充通道，而非先升维再做深度卷积）。
    2.  **线性操作多样性**：操作不限于深度卷积或移位操作，可以是多样化的线性变换。
    3.  **保留本征特征**：通过并行恒等映射，显式保留原始的本征特征图。
## 实验

- **使用数据集**：CIFAR-10（用于模块分析）、ImageNet ILSVRC 2012（主要分类基准）、MS COCO（目标检测任务）。
- **对比方法**：MobileNetV3、ShuffleNet系列、MobileNet系列等轻量级网络。
- **评价指标**：分类准确率（Top-1 Accuracy）、模型大小（参数量）、计算复杂度（FLOPs）、推理延迟。
- **主实验结果**：
    - **CIFAR-10上替换实验**：将VGG-16和ResNet-56中的卷积层替换为Ghost模块（Ghost-VGG-16, Ghost-ResNet-56），在计算量减半的情况下，保持甚至略微提升了原始模型的准确率（例如Table 4，s=2时VGG-16准确率93.7% vs 93.6%）。
    - **ImageNet分类**：GhostNet在**相似的计算量下，达到了75.7%的top-1精度，优于MobileNetV3**（p.1）。
    - **COCO目标检测**：使用SSD框架，GhostNet作为backbone也展现了比MobileNetV2/V3更好的性能-效率权衡（文中提及，具体数字在提供的文本中未完全展示）。
- **消融实验**：
    - **线性操作核大小d**：固定s=2，测试d=1,3,5,7。结果显示**d=3**在准确率和计算量上取得最佳平衡（Table 3, p.5）。
    - **扩展因子s**：固定d=3，测试s=2,3,4,5。结果显示s越大，FLOPs降低越多，但准确率也下降，验证了Eq.4和Eq.5的理论分析（Table 4, p.5）。
- **泛化实验**：在CIFAR-10（分类）、ImageNet（分类）、COCO（检测）三个不同任务和数据集上均验证了方法的有效性。
- **效率信息**：Ghost-VGG-16 (s=2) 的参数量为7.7M（原VGG-16为15.0M），FLOPs为158M（原为313M），压缩和加速约2倍（Table 4）。
## 局限

1.  **假设依赖**：方法的效果依赖于特征图之间存在显著的、可通过简单线性变换（如深度卷积）建模的相关性。在某些任务或数据域中，这种冗余模式可能不同。
2.  **计算成本**：虽然理论FLOPs降低，但生成幽灵特征图的过程引入了额外的、分散的深度卷积操作。在实际硬件上，这些操作的内存访问模式和并行效率可能与标准卷积不同，实际加速比可能低于理论值（论文在实验部分也提及了这一点）。
3.  **实验设置**：提供的文本中未包含完整的训练超参数细节（如学习率、训练周期），这给完全复现带来了一定不确定性。此外，COCO检测实验的详细结果表格（Table 7）在所提供的文本中未完全展示。
4.  **适用场景**：主要面向图像分类和检测任务，在其他任务（如语义分割、实例分割、生成模型）上的效果如何，需要进一步验证。
## 个人评论

1.  **思想启发性**：“特征图冗余是有用的，但可以廉价生成”这一核心思想非常简洁有力。它从一个独特的视角（观察到的特征图相似性）出发，为网络设计提供了新思路。这启发我们不应只关注滤波器层面的效率，也应关注特征图生成过程本身的效率。
2.  **模块的简洁性与普适性**：Ghost模块是一个即插即用的组件，可以轻松替换现有CNN中的标准卷积层。其原理清晰，实现简单（主要涉及常规卷积和深度卷积），易于理解和复现。
3.  **实用的工程价值**：论文不仅提出了模块，还基于它构建了完整的GhostNet架构，并引入了宽度乘子这一实用工具。这使得研究者和工程师可以直接使用或微调该架构来满足不同的部署需求（大小/速度/精度）。
4.  **对后续研究的启示**：这项工作鼓励研究者去探索和利用神经网络中间表征的内在结构（如冗余、相关性、稀疏性），并将其转化为架构设计的优势，而不仅仅是后处理的压缩。

### 使用建议

- **如果快速了解**：重点阅读**Abstract**、**Figure 1和Figure 2**（直观理解Ghost模块思想）、**Table 1**（GhostNet整体架构）、以及**Section 4.1**和**Section 4.2**的开头部分（了解核心实验结论）。
- **如果复现**：精读**Section 3.1 (Ghost Module)** 和 **Section 3.2 (Ghost Bottleneck & GhostNet)**，特别是公式Eq.2、Eq.3以及**Figure 3**。参考**Table 1**搭建网络。结合论文提供的GitHub代码仓库（链接在摘要中）进行验证。
- **如果借鉴创新点**：学习其**将卷积分解为“生成内蕴特征+廉价扩充”的思想**，思考能否将此思想应用于其他操作（如注意力机制）或任务（如Transformer中的Token生成）。此外，Ghost Bottleneck的设计（两个Ghost模块+可选SE+残差连接）也是一个优秀的可复用模块。
- **如果写related work**：应放在“轻量级/高效神经网络设计”、“模型压缩与加速”、“移动端CNN架构”等类别下，与MobileNet、ShuffleNet、EfficientNet等并列讨论。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**轻量级卷积神经网络设计**方向，核心是解决在计算资源受限的嵌入式设备上高效部署深度神经网络的问题。它提出了一种新的基础模块——Ghost模块，用于替代标准卷积层，以更低的计算和参数成本生成同样数量的特征图。论文的标签为“B_注意力算子模块”，虽然Ghost模块本身并非传统的、通过计算权重来强调重要性的“注意力”机制，但它提出了一种高效生成冗余特征图的机制，可以看作是对传统卷积层的一种高效替代或升级，其思想与轻量级注意力模块（如SE模块）的设计目标一致，均旨在提升模型效率。论文中，SE模块也被整合进了其最终架构GhostNet中。

## 2. 一句话总结
Ghost模块通过先用普通卷积生成少量“本征特征图”，再对这些特征图施加一系列廉价的线性变换（如深度可分离卷积），以较低的计算代价生成大量的冗余特征图（“幽灵”特征图），从而构建出高效的轻量级网络GhostNet。

## 3. 背景与问题
- **为什么要做**：将CNN部署到手机、自动驾驶汽车等嵌入式设备时，面临着内存和计算资源严重受限的挑战。传统的CNN（如ResNet-50）参数量和计算量巨大，无法直接应用。
- **之前方法的问题**：1）**模型压缩方法**（如剪枝、量化、知识蒸馏）的性能通常受限于预训练好的基线模型。2）**紧凑模型设计方法**（如MobileNet、ShuffleNet）虽然引入了深度可分离卷积等高效操作，但论文指出，它们并没有很好地利用特征图之间存在的**相关性和冗余性**。
- **核心矛盾**：成功的CNN中，特征图的冗余性是保证其综合理解输入数据的重要特性。传统方法要么忽略这种冗余，要么通过常规卷积昂贵地生成它们。论文旨在**以一种计算成本高效的方式，主动拥抱并利用这种特征图冗余**。

## 4. 核心贡献
1.  **提出了Ghost模块**：一种新的基础计算单元，它将一个卷积分解为两部分：a) 用少量卷积滤波器生成“本征特征图”；b) 对这些本征特征图施加一系列廉价的线性变换（如深度卷积）来生成更多“幽灵特征图”。
2.  **设计了Ghost Bottleneck（G-bneck）**：基于Ghost模块设计的、适用于小型CNN的瓶颈残差结构，可堆叠构建高效网络。
3.  **构建了GhostNet网络架构**：用Ghost Bottleneck替换MobileNetV3中的标准瓶颈模块，形成一个完整的、高效的轻量级网络。
4.  **提出了宽度乘子（Width Multiplier）**：一个简单的缩放因子 `α`，用于均匀调整网络各层的通道数，从而灵活控制模型的大小和计算成本。
5.  **实验验证**：在多个基准数据集（CIFAR-10, ImageNet, COCO）上验证了Ghost模块的有效性以及GhostNet相比MobileNetV3等SOTA轻量模型的优越性能。

## 5. 方法详解
- **整体框架**：GhostNet的整体架构借鉴了MobileNetV3，由一系列Ghost Bottleneck堆叠而成，具体结构详见论文中的**Table 1**（p.4）。网络从一个标准卷积层开始，接着是多组G-bneck（部分包含SE模块），最后通过全局平均池化和全连接层进行分类。
- **输入输出**：对于Ghost模块，输入特征图 `X ∈ R^(c×h×w)`，输出特征图 `Y ∈ R^(h0×w0×n)`，其中 `n` 为输出通道数。
- **关键模块**：
    1.  **Ghost模块**：是核心创新。如**Figure 2(b)**(p.3)所示，它包含：
        - **主卷积（Primary Convolution）**：用 `m` (`m ≤ n`) 个滤波器 `f0` 对输入 `X` 进行卷积，生成 `m` 张本征特征图 `Y‘`（Eq.2）。其超参数（滤波器大小、步长、填充）与标准卷积相同，以保证输出特征图的空间尺寸不变。
        - **廉价线性操作（Cheap Linear Operations）**：对每一张本征特征图 `y_i’`，应用 `s-1` 个相同的线性变换 `Φ`（论文中通常为 `d×d` 深度卷积）和一个恒等映射，生成 `s` 张幽灵特征图 `y_ij`（Eq.3）。最终，`n = m × s` 张特征图拼接成最终输出。
    2.  **Ghost Bottleneck（G-bneck）**：是GhostNet的基本构建单元。如**Figure 3**(p.4)所示，它由两个Ghost模块堆叠而成：
        - 第一个Ghost模块作为**扩展层**，使用扩展比（expansion ratio）增加通道数。
        - 第二个Ghost模块**减少通道数**以匹配shortcut路径。
        - 两者之间（在步长为2时）会插入一个深度可分离卷积进行下采样。
        - 整体形成一个残差结构，BN和ReLU（第二个Ghost模块后除外）应用于每层之后。
- **模块连接**：多个G-bneck按**Table 1**中的顺序串联。不同G-bneck的输入输出通道数、是否使用SE模块以及步长都有明确规定，形成从浅层到深层的特征提取流水线。
- **数学公式直观解释**：
    - Eq.1：标准卷积 `Y = X * f + b`，计算量巨大。
    - Eq.2 & Eq.3：Ghost模块首先用更少的参数 (`m` 个滤波器) 得到“精简版”特征图 `Y‘`，然后像“克隆”或“变形”一样，对 `Y‘` 中的每个特征图进行便宜的空间变换（`Φ`），生成一组“幽灵”副本。这样，用 `1/s` 的成本获得了 `n` 倍的特征图。
    - Eq.4 & Eq.5：理论上的加速比和压缩比都近似等于扩展因子 `s`（假设 `d≈k` 且 `s<<c`）。
- **训练方式**：论文中提及遵循常用训练策略（如动量、学习率计划），但具体细节（如学习率、优化器、训练轮数）在提供的文本中**未明确说明**。
- **推理流程**：标准的端到端前向传播，输入图像依次经过Table 1中的各层，得到分类结果。
- **和已有方法的差异**：论文在3.1节“Difference from Existing Methods”中明确对比(p.3)：
    1.  **与MobileNet/ShuffleNet比**：主卷积核大小可定制（不一定是1x1），且处理流程相反（先生成少量特征，再扩充通道，而非先升维再做深度卷积）。
    2.  **线性操作多样性**：操作不限于深度卷积或移位操作，可以是多样化的线性变换。
    3.  **保留本征特征**：通过并行恒等映射，显式保留原始的本征特征图。

## 6. 实验与结果
- **使用数据集**：CIFAR-10（用于模块分析）、ImageNet ILSVRC 2012（主要分类基准）、MS COCO（目标检测任务）。
- **对比方法**：MobileNetV3、ShuffleNet系列、MobileNet系列等轻量级网络。
- **评价指标**：分类准确率（Top-1 Accuracy）、模型大小（参数量）、计算复杂度（FLOPs）、推理延迟。
- **主实验结果**：
    - **CIFAR-10上替换实验**：将VGG-16和ResNet-56中的卷积层替换为Ghost模块（Ghost-VGG-16, Ghost-ResNet-56），在计算量减半的情况下，保持甚至略微提升了原始模型的准确率（例如Table 4，s=2时VGG-16准确率93.7% vs 93.6%）。
    - **ImageNet分类**：GhostNet在**相似的计算量下，达到了75.7%的top-1精度，优于MobileNetV3**（p.1）。
    - **COCO目标检测**：使用SSD框架，GhostNet作为backbone也展现了比MobileNetV2/V3更好的性能-效率权衡（文中提及，具体数字在提供的文本中未完全展示）。
- **消融实验**：
    - **线性操作核大小d**：固定s=2，测试d=1,3,5,7。结果显示**d=3**在准确率和计算量上取得最佳平衡（Table 3, p.5）。
    - **扩展因子s**：固定d=3，测试s=2,3,4,5。结果显示s越大，FLOPs降低越多，但准确率也下降，验证了Eq.4和Eq.5的理论分析（Table 4, p.5）。
- **泛化实验**：在CIFAR-10（分类）、ImageNet（分类）、COCO（检测）三个不同任务和数据集上均验证了方法的有效性。
- **效率信息**：Ghost-VGG-16 (s=2) 的参数量为7.7M（原VGG-16为15.0M），FLOPs为158M（原为313M），压缩和加速约2倍（Table 4）。

## 7. 这篇论文真正有价值的地方
1.  **思想启发性**：“特征图冗余是有用的，但可以廉价生成”这一核心思想非常简洁有力。它从一个独特的视角（观察到的特征图相似性）出发，为网络设计提供了新思路。这启发我们不应只关注滤波器层面的效率，也应关注特征图生成过程本身的效率。
2.  **模块的简洁性与普适性**：Ghost模块是一个即插即用的组件，可以轻松替换现有CNN中的标准卷积层。其原理清晰，实现简单（主要涉及常规卷积和深度卷积），易于理解和复现。
3.  **实用的工程价值**：论文不仅提出了模块，还基于它构建了完整的GhostNet架构，并引入了宽度乘子这一实用工具。这使得研究者和工程师可以直接使用或微调该架构来满足不同的部署需求（大小/速度/精度）。
4.  **对后续研究的启示**：这项工作鼓励研究者去探索和利用神经网络中间表征的内在结构（如冗余、相关性、稀疏性），并将其转化为架构设计的优势，而不仅仅是后处理的压缩。

## 8. 局限与问题
1.  **假设依赖**：方法的效果依赖于特征图之间存在显著的、可通过简单线性变换（如深度卷积）建模的相关性。在某些任务或数据域中，这种冗余模式可能不同。
2.  **计算成本**：虽然理论FLOPs降低，但生成幽灵特征图的过程引入了额外的、分散的深度卷积操作。在实际硬件上，这些操作的内存访问模式和并行效率可能与标准卷积不同，实际加速比可能低于理论值（论文在实验部分也提及了这一点）。
3.  **实验设置**：提供的文本中未包含完整的训练超参数细节（如学习率、训练周期），这给完全复现带来了一定不确定性。此外，COCO检测实验的详细结果表格（Table 7）在所提供的文本中未完全展示。
4.  **适用场景**：主要面向图像分类和检测任务，在其他任务（如语义分割、实例分割、生成模型）上的效果如何，需要进一步验证。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**Abstract**、**Figure 1和Figure 2**（直观理解Ghost模块思想）、**Table 1**（GhostNet整体架构）、以及**Section 4.1**和**Section 4.2**的开头部分（了解核心实验结论）。
- **如果复现**：精读**Section 3.1 (Ghost Module)** 和 **Section 3.2 (Ghost Bottleneck & GhostNet)**，特别是公式Eq.2、Eq.3以及**Figure 3**。参考**Table 1**搭建网络。结合论文提供的GitHub代码仓库（链接在摘要中）进行验证。
- **如果借鉴创新点**：学习其**将卷积分解为“生成内蕴特征+廉价扩充”的思想**，思考能否将此思想应用于其他操作（如注意力机制）或任务（如Transformer中的Token生成）。此外，Ghost Bottleneck的设计（两个Ghost模块+可选SE+残差连接）也是一个优秀的可复用模块。
- **如果写related work**：应放在“轻量级/高效神经网络设计”、“模型压缩与加速”、“移动端CNN架构”等类别下，与MobileNet、ShuffleNet、EfficientNet等并列讨论。

## 10. 和其他论文的关系
根据提供的主题“B_注意力算子模块”以及文件名“GhostModule.pdf”，这篇论文最直接的相关工作是**轻量级网络设计**领域的论文。
- `[[MobileNetV3]]`：GhostNet的架构直接借鉴了MobileNetV3，并进行了替换和改进。两者是直接的对比和递进关系。
- `[[ShuffleNet]]`：同样是旨在降低模型计算成本的轻量级网络，GhostNet的创新部分源于对其未充分利用特征冗余的观察。
- `[[Squeeze-and-Excitation Networks]]`：SE模块是GhostNet最终架构中集成的一部分，用于通道注意力，两者属于互补组件关系。

## 11. 关键词
Ghost Module, GhostNet, 轻量级神经网络, 特征冗余, 深度可分离卷积, 移动端部署, 模型压缩, MobileNetV3, 计算效率, 特征图生成, 宽度乘子

## 12. 可信度说明
本精读笔记**完全基于**用户提供的PDF提取文本（共10页，覆盖了摘要、引言、相关工作、方法论、实验部分开头和结果分析）。笔记中的所有方法描述、公式解释、实验数字和结论均严格从文本中提取或转述，未编造任何信息。对于文本中未明确提及的信息（如完整训练超参数、部分实验表格细节），已在相应位置明确标注“PDF文本中未明确说明”或“未找到”。提取的文本质量良好，逻辑清晰，足以支撑完成一份准确、详细的精读笔记。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2504 字符/页)); 来源缓存: `.paper-cache/extracts/GhostModule.txt` (10/10 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
