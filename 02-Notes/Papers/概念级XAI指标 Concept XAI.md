---
title: "Concept-Based Explainable Artificial Intelligence: Metrics and Benchmarks"
authors:
  - "Halil Ibrahim Aysel"
  - "Xiaohao Cai"
  - "Adam Prugel-Bennett"
year: 2017
venue: "arXiv"
doi: 
pdf: [[概念级XAI指标 Concept XAI.pdf]]
primary_topic: A2_医学图像_分类_配准_生成
topics:
  - "A2_医学图像_分类_配准_生成"
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
extract_cache: .paper-cache/extracts/概念级XAI指标 Concept XAI.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# Concept-Based Explainable Artificial Intelligence: Metrics and Benchmarks

## 基本信息
- **PDF**: [[概念级XAI指标 Concept XAI.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Concept-Based Explainable Artificial Intelligence: Metrics and Benchmarks |
| **作者** | Halil Ibrahim Aysel; Xiaohao Cai; Adam Prugel-Bennett |
| **发表时间** | 2017 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> moreunderstandabletothelaymantherehasbeenagrow- ingdrivetodeveloptechniquesthatprovideexplanationsin Concept-basedexplanationmethods,suchascon- termsofhuman-understandableconcepts(Bauetal.,2017; ceptbottleneckmodels(CBMs),aimtoimprove Kimetal.,2018;Kohetal.,2020;Havasietal.,2022;Aysel theinterpretabilityofmachinelearningmodelsby etal.,2023;Shinetal.,2023). Oneofthebigchallenges linkingtheirdecisionstohuman-understandable ofconcept-basedXAImethodsisthatofparamountimpor- concepts,underthecriticalassumptionthatsuch tanceyetlacksasystematicstudytoensurethattheconcepts conceptscanbeaccuratelyattributedtothenet- identifiedasimportanttomakingadecisionproperlyalign work’sfeaturespace. However,thisfoundational withhumanunderstandingoftheconcepts. assumption has not been rigorously validated, mainlybecausethefieldlacksstandardisedmet- Inthispaper,weproposethreenewmetricsformeasuring ricsandbenchmarkstoassesstheexistenceand thisalignment. Thefirstistheconceptglobalimportance spatial alignment of 

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：基于概念的XAI方法（如概念瓶颈模型CBMs）旨在通过将模型决策与人类可理解的概念联系起来以提高可解释性。但这些方法建立在一个关键假设之上：即这些概念能被准确地归因到网络的特征空间中。
- **之前方法的问题**：这个关键假设缺乏严格的验证，主要是因为该领域缺乏标准化的指标和基准来评估这些概念的“存在性”和“空间对齐性”。
- **核心矛盾**：概念可解释性方法承诺提供人类可理解的解释，但我们无法系统地判断这些“解释性概念”是否真的在输入图像中存在，以及模型关注到的概念区域是否正确。这使得其可靠性存疑。
## 关键贡献

1.  提出了**概念激活映射**框架，用于可视化输入图像中与特定概念对应的激活区域。
2.  提出了**三个定量评估指标**：
    - **概念全局重要性指标**：评估XAI方法得出的全局概念重要性（如分类器权重）与真实概念重要性的对齐程度。
    - **概念存在性指标**：评估被XAI方法识别为重要的概念，是否真的存在于该图像中。
    - **概念位置指标**：评估概念激活热图的空间区域是否与概念在图像中的真实位置对齐。
3.  基于**CUB-200-2011数据集**，利用提出的方法创建了一个基准，并对**后验概念瓶颈模型**进行了系统的评估实验。
4.  通过实验发现，后验CBMs即使在被认为最重要的概念上，也经常**无法在输入图像中找到该概念**；即使概念存在，其显著性图也常常**无法正确对齐**相关区域（如激活遍布整个物体或错误识别区域）。
5.  分析了这些局限性的根本原因，例如**概念的自然相关性**。
## 方法

- **整体框架**：论文的评估流程分为“全局评估”和“局部评估”两部分，如图1的下半部分所示。核心是利用提出的**CoAM框架**生成概念激活图，并在此基础上计算三个指标。
- **输入输出**：
    - 输入：一个已训练好的后验CBMs模型（包含特征提取器`f`和概念向量库`C`），以及带有概念存在标签`u_i`和概念中心点坐标`P_i`的测试图像`X_i`。
    - 输出：三个指标的数值（CGIM, CEM, CLM），以及每张图像上每个概念的激活热图`F_ij`。
- **关键模块与连接**：
    1.  **概念激活映射 (CoAM)**：这是可视化和位置度量的核心。给定图像`X_i`的**预-GAP特征图** `E_i`（尺寸 H×W×d）和概念向量`c_j`（第j个概念），第j个概念的激活图`F_ij`通过对每个通道的特征图用对应的概念向量权重进行加权求和得到：`F_ij = (1/d) * Σ_{k=1}^d c_jk * E_i(:,:,k)`。直观理解，这是将高维特征空间中与概念`j`相关的方向“投影”回图像空间，显示该概念在图像中的激活强度分布。
    2.  **概念全局重要性指标 (CGIM)**：用于全局评估。定义了三个变体（ρ_CGIM1, ρ_CGIM2, ρ_CGIM3），核心是比较从分类器权重`θ`或平均概念值`U*`中得到的**估计重要性向量**与真实的**概念-类别重要性矩阵`V`**之间的相似度（使用余弦相似度）。这评估了模型学到的概念与真实世界概念关系的对齐程度。
    3.  **概念存在性指标 (CEM)**：用于局部评估。对于一张图像，首先计算每个概念的**局部重要性得分**（`θ_jk * ŭ_ij`，其中`θ_jk`是权重，`ŭ_ij`是预测的概念值），并据此对所有概念进行排名。CEM检查排名前`l`个概念中，有多少个真正存在于该图像的真实概念集合`Λ_i`中。这是一个准确率指标。
    4.  **概念位置指标 (CLM)**：用于局部评估。在CEM检查概念存在性后，CLM进一步检查：对于这些重要的概念，其通过CoAM生成的激活热图（经过上采样和阈值化得到区域`Ω_ij`），是否包含了该概念在图像中的**真实中心点坐标`p_ij`**。这是一个基于中心点包含关系的准确率指标。
- **训练与推理**：本文**提出的方法本身不涉及模型训练**，它是一个**事后评估框架**。它需要：
    - 一个已训练好的特征提取器（如ResNet）。
    - 一个已构建好的概念向量库（通过SVM在正负样本图像的特征上训练得到）。
    - 一个已训练好的单层分类器`h`（用于提取权重`θ`）。
    - 推理时，对每张测试图像，提取特征，计算概念值，然后依次计算CGIM（全局）、CEM（局部存在）、CoAM+CLM（局部位置）。
- **与已有方法的差异**：本文的核心差异在于提出了**系统性的评估方法**，而不是提出一个新的可解释性模型本身。它填补了概念可解释性领域缺乏定量评估工具的空白。
## 实验

- **使用数据集**：**Caltech-UCSD Birds (CUB-200-2011)**。包含200个类别，112个二元概念标签（如翅膀颜色、喙形状），约11，800张图像。数据集还提供了12个身体部位的中心像素坐标，用于概念位置评估。
- **对比方法**：本文主要评估了**后验概念瓶颈模型**。实验本身是“被评估模型”与“评估指标”之间的关系，而非不同模型间的对比。
- **评价指标**：本文提出的三个指标：CGIM， CEM， CLM。
- **主实验结果**：
    - **全局评估 (CGIM)**：图2显示，CGIM分数（无论是按类别还是按概念）普遍较低，分布广泛，表明后验CBMs的**全局概念重要性**与真实情况对齐很差。
    - **局部评估 (CEM)**：实验结果（如p.8提到）显示，CEM得分非常低。例如，在评估最重要的3个概念时，平均得分可能在0.06到0.40之间（具体数值依赖于实验设置），表明**被模型认为最重要的概念往往根本不存在于图像中**。
    - **局部评估 (CLM)**：在那些确实存在的概念上，CLM得分同样很低（如p.9提到可能在0.15到0.51之间），表明即使概念存在，**激活热图也无法准确定位到概念所在区域**。
- **消融实验**：PDF文本中未明确说明针对提出指标本身的消融实验。但论文分析了不同超参数（如用于计算CAV的正负样本数m）对后验CBMs性能的影响。
- **泛化实验**：PDF文本中未明确说明在其他数据集上的泛化实验。实验集中于CUB数据集。
- **效率信息**：PDF文本中未明确说明模型的计算量、参数量或速度等效率信息。评估重点是概念对齐质量。
## 局限

1.  **评估假设的局限性**：CLM依赖概念的**中心像素点**作为真值，这是一个简化的假设。更精确的评估需要像素级的分割掩码，但获取成本高。阈值`τ`的选择也会影响CLM的结果。
2.  **数据集的局限性**：实验仅在CUB鸟类数据集上进行。该数据集有相对明确的部件（鸟喙、翅膀）和颜色概念，这些概念视觉上较为局部化。方法在概念更抽象（如“快乐”）、更全局化（如“风景”）或定义更模糊的数据集上的效果有待验证。
3.  **计算成本未讨论**：论文未详细讨论使用该评估框架（特别是需要为每张图像的每个概念生成热图）的计算开销。
4.  **对后验CBMs的依赖**：本文的评估完全基于后验CBMs，未对传统CBMs或其他概念可解释性方法（如TCAV）进行同样系统的评估，尽管指标本身是通用的。
## 个人评论

1.  **提出了一个急需的评估框架**：在概念可解释性研究火热但评估缺失的背景下，本文的指标和基准是极具实用价值的工具。它提醒研究者不能只看“解释”的形式，必须验证其内容的真实性。
2.  **深刻的实验发现**：论文用实验证据表明，当前流行的后验CBMs在概念对齐上存在根本性缺陷，这动摇了其可解释性的基础。这对于正视该方法的局限性、推动下一代更可靠概念解释方法的发展至关重要。
3.  **强调了空间可解释性的重要性**：通过CLM指标，论文凸显了在视觉任务中，解释必须具有空间准确性，而不仅仅是一个抽象的标签。
4.  **启发研究思路**：它为后续研究指明了方向，即开发能够**保证概念存在性和空间一致性**的新方法，而不仅仅是利用概念进行分类。

### 使用建议

- **如果快速了解**：直接阅读**摘要、第1节引言**和**第4.2、4.3节**的实验结果部分（特别是其中的总结性段落），即可掌握核心问题和主要发现。
- **如果复现**：重点看**第3节方法详解**，特别是CoAM的公式（2）、CEM和CLM的定义（公式9、11），以及**第4.1节**中关于后验CBMs复现的设置细节。
- **如果借鉴创新点**：应学习其**评估思路**——如何从“全局重要性”、“局部存在性”、“局部位置”三个维度构建评估体系。以及**CoAM这种将概念向量反投影到特征图进行可视化**的技术。
- **如果写related work**：可将其归类在“**XAI评估方法**”或“**概念可解释性**”相关的文献综述中，作为提出评估指标的代表作之一。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于可解释人工智能（XAI）方向，具体聚焦于**概念可解释性**的评估方法。论文解决的核心问题是：如何系统性地评估基于概念的可解释性方法（如概念瓶颈模型）所识别出的概念是否真实存在于输入数据中，且其空间位置是否与人类预期相符。该研究适合放在“可解释人工智能评估”或“概念可解释性基准测试”主题下。虽然论文使用了鸟类数据集进行实验，但其提出的评估框架旨在成为通用工具。

## 2. 一句话总结
本文提出了三个定量指标（概念全局重要性、概念存在性、概念位置度量）和一个概念激活映射可视化框架，用于评估基于概念的可解释性方法，发现后验概念瓶颈模型在概念对齐上存在严重缺陷。

## 3. 背景与问题
- **为什么要做**：基于概念的XAI方法（如概念瓶颈模型CBMs）旨在通过将模型决策与人类可理解的概念联系起来以提高可解释性。但这些方法建立在一个关键假设之上：即这些概念能被准确地归因到网络的特征空间中。
- **之前方法的问题**：这个关键假设缺乏严格的验证，主要是因为该领域缺乏标准化的指标和基准来评估这些概念的“存在性”和“空间对齐性”。
- **核心矛盾**：概念可解释性方法承诺提供人类可理解的解释，但我们无法系统地判断这些“解释性概念”是否真的在输入图像中存在，以及模型关注到的概念区域是否正确。这使得其可靠性存疑。

## 4. 核心贡献
1.  提出了**概念激活映射**框架，用于可视化输入图像中与特定概念对应的激活区域。
2.  提出了**三个定量评估指标**：
    - **概念全局重要性指标**：评估XAI方法得出的全局概念重要性（如分类器权重）与真实概念重要性的对齐程度。
    - **概念存在性指标**：评估被XAI方法识别为重要的概念，是否真的存在于该图像中。
    - **概念位置指标**：评估概念激活热图的空间区域是否与概念在图像中的真实位置对齐。
3.  基于**CUB-200-2011数据集**，利用提出的方法创建了一个基准，并对**后验概念瓶颈模型**进行了系统的评估实验。
4.  通过实验发现，后验CBMs即使在被认为最重要的概念上，也经常**无法在输入图像中找到该概念**；即使概念存在，其显著性图也常常**无法正确对齐**相关区域（如激活遍布整个物体或错误识别区域）。
5.  分析了这些局限性的根本原因，例如**概念的自然相关性**。

## 5. 方法详解
- **整体框架**：论文的评估流程分为“全局评估”和“局部评估”两部分，如图1的下半部分所示。核心是利用提出的**CoAM框架**生成概念激活图，并在此基础上计算三个指标。
- **输入输出**：
    - 输入：一个已训练好的后验CBMs模型（包含特征提取器`f`和概念向量库`C`），以及带有概念存在标签`u_i`和概念中心点坐标`P_i`的测试图像`X_i`。
    - 输出：三个指标的数值（CGIM, CEM, CLM），以及每张图像上每个概念的激活热图`F_ij`。
- **关键模块与连接**：
    1.  **概念激活映射 (CoAM)**：这是可视化和位置度量的核心。给定图像`X_i`的**预-GAP特征图** `E_i`（尺寸 H×W×d）和概念向量`c_j`（第j个概念），第j个概念的激活图`F_ij`通过对每个通道的特征图用对应的概念向量权重进行加权求和得到：`F_ij = (1/d) * Σ_{k=1}^d c_jk * E_i(:,:,k)`。直观理解，这是将高维特征空间中与概念`j`相关的方向“投影”回图像空间，显示该概念在图像中的激活强度分布。
    2.  **概念全局重要性指标 (CGIM)**：用于全局评估。定义了三个变体（ρ_CGIM1, ρ_CGIM2, ρ_CGIM3），核心是比较从分类器权重`θ`或平均概念值`U*`中得到的**估计重要性向量**与真实的**概念-类别重要性矩阵`V`**之间的相似度（使用余弦相似度）。这评估了模型学到的概念与真实世界概念关系的对齐程度。
    3.  **概念存在性指标 (CEM)**：用于局部评估。对于一张图像，首先计算每个概念的**局部重要性得分**（`θ_jk * ŭ_ij`，其中`θ_jk`是权重，`ŭ_ij`是预测的概念值），并据此对所有概念进行排名。CEM检查排名前`l`个概念中，有多少个真正存在于该图像的真实概念集合`Λ_i`中。这是一个准确率指标。
    4.  **概念位置指标 (CLM)**：用于局部评估。在CEM检查概念存在性后，CLM进一步检查：对于这些重要的概念，其通过CoAM生成的激活热图（经过上采样和阈值化得到区域`Ω_ij`），是否包含了该概念在图像中的**真实中心点坐标`p_ij`**。这是一个基于中心点包含关系的准确率指标。
- **训练与推理**：本文**提出的方法本身不涉及模型训练**，它是一个**事后评估框架**。它需要：
    - 一个已训练好的特征提取器（如ResNet）。
    - 一个已构建好的概念向量库（通过SVM在正负样本图像的特征上训练得到）。
    - 一个已训练好的单层分类器`h`（用于提取权重`θ`）。
    - 推理时，对每张测试图像，提取特征，计算概念值，然后依次计算CGIM（全局）、CEM（局部存在）、CoAM+CLM（局部位置）。
- **与已有方法的差异**：本文的核心差异在于提出了**系统性的评估方法**，而不是提出一个新的可解释性模型本身。它填补了概念可解释性领域缺乏定量评估工具的空白。

## 6. 实验与结果
- **使用数据集**：**Caltech-UCSD Birds (CUB-200-2011)**。包含200个类别，112个二元概念标签（如翅膀颜色、喙形状），约11，800张图像。数据集还提供了12个身体部位的中心像素坐标，用于概念位置评估。
- **对比方法**：本文主要评估了**后验概念瓶颈模型**。实验本身是“被评估模型”与“评估指标”之间的关系，而非不同模型间的对比。
- **评价指标**：本文提出的三个指标：CGIM， CEM， CLM。
- **主实验结果**：
    - **全局评估 (CGIM)**：图2显示，CGIM分数（无论是按类别还是按概念）普遍较低，分布广泛，表明后验CBMs的**全局概念重要性**与真实情况对齐很差。
    - **局部评估 (CEM)**：实验结果（如p.8提到）显示，CEM得分非常低。例如，在评估最重要的3个概念时，平均得分可能在0.06到0.40之间（具体数值依赖于实验设置），表明**被模型认为最重要的概念往往根本不存在于图像中**。
    - **局部评估 (CLM)**：在那些确实存在的概念上，CLM得分同样很低（如p.9提到可能在0.15到0.51之间），表明即使概念存在，**激活热图也无法准确定位到概念所在区域**。
- **消融实验**：PDF文本中未明确说明针对提出指标本身的消融实验。但论文分析了不同超参数（如用于计算CAV的正负样本数m）对后验CBMs性能的影响。
- **泛化实验**：PDF文本中未明确说明在其他数据集上的泛化实验。实验集中于CUB数据集。
- **效率信息**：PDF文本中未明确说明模型的计算量、参数量或速度等效率信息。评估重点是概念对齐质量。

## 7. 这篇论文真正有价值的地方
1.  **提出了一个急需的评估框架**：在概念可解释性研究火热但评估缺失的背景下，本文的指标和基准是极具实用价值的工具。它提醒研究者不能只看“解释”的形式，必须验证其内容的真实性。
2.  **深刻的实验发现**：论文用实验证据表明，当前流行的后验CBMs在概念对齐上存在根本性缺陷，这动摇了其可解释性的基础。这对于正视该方法的局限性、推动下一代更可靠概念解释方法的发展至关重要。
3.  **强调了空间可解释性的重要性**：通过CLM指标，论文凸显了在视觉任务中，解释必须具有空间准确性，而不仅仅是一个抽象的标签。
4.  **启发研究思路**：它为后续研究指明了方向，即开发能够**保证概念存在性和空间一致性**的新方法，而不仅仅是利用概念进行分类。

## 8. 局限与问题
1.  **评估假设的局限性**：CLM依赖概念的**中心像素点**作为真值，这是一个简化的假设。更精确的评估需要像素级的分割掩码，但获取成本高。阈值`τ`的选择也会影响CLM的结果。
2.  **数据集的局限性**：实验仅在CUB鸟类数据集上进行。该数据集有相对明确的部件（鸟喙、翅膀）和颜色概念，这些概念视觉上较为局部化。方法在概念更抽象（如“快乐”）、更全局化（如“风景”）或定义更模糊的数据集上的效果有待验证。
3.  **计算成本未讨论**：论文未详细讨论使用该评估框架（特别是需要为每张图像的每个概念生成热图）的计算开销。
4.  **对后验CBMs的依赖**：本文的评估完全基于后验CBMs，未对传统CBMs或其他概念可解释性方法（如TCAV）进行同样系统的评估，尽管指标本身是通用的。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：直接阅读**摘要、第1节引言**和**第4.2、4.3节**的实验结果部分（特别是其中的总结性段落），即可掌握核心问题和主要发现。
- **如果复现**：重点看**第3节方法详解**，特别是CoAM的公式（2）、CEM和CLM的定义（公式9、11），以及**第4.1节**中关于后验CBMs复现的设置细节。
- **如果借鉴创新点**：应学习其**评估思路**——如何从“全局重要性”、“局部存在性”、“局部位置”三个维度构建评估体系。以及**CoAM这种将概念向量反投影到特征图进行可视化**的技术。
- **如果写related work**：可将其归类在“**XAI评估方法**”或“**概念可解释性**”相关的文献综述中，作为提出评估指标的代表作之一。

## 10. 和其他论文的关系
根据给定的主题 `A2_医学图像_分类_配准_生成`，本文本身**不是**医学图像领域的论文。它属于通用的XAI评估方法论。
可能相关的论文包括：
- [[Concept Bottleneck Models]] (Koh et al., 2020): 本文评估的核心对象之一。
- [[TCAV]] (Kim et al., 2018): 概念激活向量的原始提出者，本文方法基于此。
- [[Post-hoc Concept Bottleneck Models]] (Yuksekgonul et al., 2023): 本文直接评估的具体后验CBMs方法。
- 其他在医学影像领域应用概念可解释性的工作，这些工作可能会受益于本文提出的评估框架。

## 11. 关键词
可解释人工智能（XAI），概念可解释性，概念瓶颈模型（CBMs），评估指标，概念激活映射（CoAM），概念存在性，概念定位，后验解释，显著性对齐，CUB数据集

## 12. 可信度说明
本精读笔记完全基于用户提供的**PDF提取文本（前12页）**生成。提取文本内容清晰，包含了摘要、引言、方法、实验设置和部分实验结果等核心部分。
**需要注意的局限**：提供的文本在**第4.2节中间截止**，因此关于CGIM的详细实验结果表格（如表6、7、8）以及CEM和CLM的具体数字结果、后续的讨论和结论部分**未能包含**。笔记中涉及的具体结果数字（如CEM得分范围）是根据已有文本中提及的描述性语句归纳的，可能不完整。对于更全面的结果分析，建议查阅完整论文。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/概念级XAI指标 Concept XAI.txt` (17/17 页; 原 AI 主体 12/17 + 全文补读 13-17); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Concept-Based Explainable Artificial Intelligence: Metrics and Benchmarks
- p.13: Input Concept-wise maps Class maps
- p.13: PartTypeColor Pattern Shape Total
- p.13: Beak 3 2 4 9
- p.13: Wing 6 4 2 12
- p.13: Tail 10 3 1 14
- p.13: Total 82 18 12 112
- p.14: PartTypeColor Pattern (length for beak) Shape
- p.14: Beak grey, black, buff same-as-head, shorter-than-head dagger, hooked-seabird, all-purpose, cone
- p.14: Wing brown, grey, yellow, black, white, buff solid, spotted, striped, multi-coloured rounded, pointed
- p.14: Tail brown, grey, black, white, buff solid, striped, multi-colored notched
- p.14: Algorithm 2 Feature Visualisation in CoAM

### 缺失页关键摘录

- p.13: D. Concept Localisation Evaluation – Figures and Tables
- p.13: Figure 4 presents some examples of class and concept visualisation by using our CoAM. The matching between the concept
- p.13: groups and the body parts for the CUB dataset is given in Tables 4 and 5.
- p.13: Figure 4. Class and concept visualisation with our CoAM. All images (on the left) are correctly classified and their class-wise saliency
- p.13: Table 4. The number of concepts, grouped based on their types, and mapped to the body parts (see Table 5 for more details).
- p.14: Table 5. Details of the concepts and the body parts they are mapped to.
- p.14: Figure 2 presents the histograms of the CGIM scores. The full list of CGIM scores for every concept and every class is
- p.14: presented below in Table 6 and in Tables 7 and 8, respectively.
- p.15: Table 6. Full list of CGIM scores for concepts in CUB dataset (Wah et al., 2011) with reproduced post-hoc CBMs (Yuksekgonul et al.,
- p.16: Table 7. Full list of CGIM scores for classes in CUB dataset (Wah et al., 2011) with reproduced post-hoc CBMs (Yuksekgonul et al., 2023).
- p.17: Table 8. Full list of CGIM scores for classes in CUB dataset (Wah et al., 2011) with reproduced post-hoc CBMs (Yuksekgonul et al., 2023)
<!-- AI_READING_NOTE_END -->
