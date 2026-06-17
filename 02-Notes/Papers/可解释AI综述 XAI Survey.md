---
title: "Explainable Artificial Intelligence: Advancements and Limitations"
authors:
  - "Explainable Artificial Intelligence: Advancements"
  - "Limitations"
  - "HalilIbrahimAysel"
  - "XiaohaoCai andAdamPrugel-Bennett"
  - "SchoolofElectronicsandComputerScience"
  - "UniversityofSouthampton"
  - "SouthamptonSO171BJ"
year: 2025
venue: "Electronics"
doi: 10.3390/app15137261
pdf: [[可解释AI综述 XAI Survey.pdf]]
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
extract_cache: .paper-cache/extracts/可解释AI综述 XAI Survey.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/26 pages"
---
# Explainable Artificial Intelligence: Advancements and Limitations

## 基本信息
- **PDF**: [[可解释AI综述 XAI Survey.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Explainable Artificial Intelligence: Advancements and Limitations |
| **作者** | Explainable Artificial Intelligence: Advancements; Limitations; HalilIbrahimAysel; XiaohaoCai andAdamPrugel-Bennett; SchoolofElectronicsandComputerScience; UniversityofSouthampton; SouthamptonSO171BJ |
| **发表时间** | 2025 |
| **刊物/会议** | Electronics |
| **DOI** | 10.3390/app15137261 |

## 摘要

> Explainableartificialintelligence(XAI)hasemergedasacrucialfieldforunderstandingand interpretingthedecisionsofcomplexmachinelearningmodels,particularlydeepneural networks.ThisreviewpresentsastructuredoverviewofXAImethodologies,encompassing a diverse range of techniques designed to provide explainability at different levels of abstraction.Wecoverpixel-levelexplanationstrategiessuchassaliencymaps,perturbation- basedmethodsandgradient-basedvisualisations,aswellasconcept-basedapproaches thatalignmodelbehaviourwithhuman-understandablesemantics. Additionally,wetouch upon the relevance of XAI in the context of weakly supervised semantic segmentation. By synthesising recent developments, this paper aims to clarify the landscape of XAI methodsandofferinsightsintotheircomparativeutilityandroleinfosteringtrustworthy AIsystems.

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：深度神经网络在医学、机器人、经济等领域取得了卓越的预测性能，但其复杂的、端到端学习的决策过程（p.3）导致了“黑箱”特性，阻碍了用户对其预测的信任。模型的可解释性对于在医疗、法律等敏感领域安全部署AI系统至关重要，甚至受到GDPR等法规的强制要求（p.2）。
- **之前方法有什么问题**：尽管已有大量XAI综述，但它们侧重点各异，有的聚焦术语定义，有的关注特定领域应用。这些综述缺少一个统一的、结构化的框架来全面涵盖现有及未来可能的XAI方法（p.2）。
- **作者想解决的核心矛盾**：核心矛盾是深度学习模型追求高性能（依赖于自动学习复杂特征）与人类理解需求（需要透明、可解释的决策逻辑）之间的差距。传统机器学习方法（如决策树）使用手动设计的、人类可理解的特征，决策过程相对透明；而CNN自动学习到的特征高度复杂且非线性，导致决策过程不透明（p.3）。
## 关键贡献

根据文本，本综述的核心贡献如下：
1.  **首次明确定义了XAI的六个关键维度**：解释阶段、解释层级、模型特异性、目标受众、粒度和解释模态（p.2, p.4）。作者声称任何现有或未来的XAI方法都可以归入这些类别。
2.  **对多种XAI方法的优势与局限性进行了跨类别的分析**（p.2），为从业者选择合适的技术提供了指导。
3.  **重点分析了“解释模态”这一维度**，并深入探讨了其下的“视觉解释”和“概念解释”两大子类（p.2, p.4）。作者认为这对于视觉任务尤其关键。
4.  **揭示了XAI与弱监督语义分割（WSSS）之间的紧密联系**（p.2, p.3）。
5.  **为从业者和研究者提供了明确的指引**：为终端用户选择X技术提供指南，为研究者指明当前领域的空白与挑战（p.2）。
## 方法

本文是**综述论文**，不提出新的XAI方法，而是对现有方法进行分类、描述和对比。其“方法”即指所提出的分类框架和对各类XAI技术的解析。
- **整体框架**：论文提出了一个六维分类框架（图1）。
    1.  **解释阶段**：分为**后验（Post-hoc）** 方法（模型训练后解释，不改变模型）和**内置（Ad-hoc）** 方法（模型本身具有可解释性，或训练时嵌入可解释性）。
    2.  **解释层级**：分为**全局（Global）**（解释模型整体行为）和**局部（Local）**（解释单个预测）。
    3.  **模型特异性**：分为**模型特定（Model-specific）**（针对特定架构如CNN）和**模型无关（Model-agnostic）**（适用于任何模型）。
    4.  **目标受众**：分为**研究人员**（需要深入技术洞察）和**终端用户**（需要简单易懂的解释）。
    5.  **粒度**：分为**细粒度（Fine-grained）**（如概念级洞察）和**粗粒度（Coarse-grained）**（如类级或物体级洞察）。
    6.  **解释模态**：分为**视觉（Visual）**（如热力图）和**概念（Conceptual）**（如人类可理解的概念）。
- **关键模块/技术**：论文在框架下重点介绍了视觉解释（图2左）和概念解释（图2右）。
    - **视觉解释**：
        - **激活最大化**：通过优化噪声图像或检索训练样本，找到能最强激活某个神经元、层或类的模式（p.7）。优点是能洞察网络学习到的表示；缺点包括生成图像抽象不清晰、计算昂贵、易受对抗性扰动影响（p.7）。
        - **像素归因**：旨在找出对类别预测贡献最大的图像区域，生成热力图（显著图）（p.8）。其基础思想源于线性模型的加权求和思想（p.8）。具体技术包括：
            - **基于反向传播的显著图**：如Simonyan等人提出的方法（文中提及但未展开）。
            - （根据图2）其他类别包括：**扰动方法**和**类激活映射（CAM）**。
    - **概念解释**：（根据文本和图2）旨在将模型学习到的高层特征与人类可理解的语义概念对齐，主要方法包括**网络剖析**、**概念瓶颈模型（CBM）**、**概念白化**、**概念激活向量（CAV）** 及其后验版本。
- **与已有方法的差异**：本文的框架更强调“解释模态”的重要性，并认为未来的XAI方法需要同时提供视觉和概念上的解释（p.2, p.4）。此外，它明确将XAI与WSSS关联起来。
## 实验

本文是**综述性论文**，旨在总结和评估已有的XAI方法，**并未提出新的模型或算法，因此没有包含独立的实验、数据集、评价指标或结果**。它通过对现有文献的梳理和分析来构建其分类框架和观点。文中提及的如“ImageNet LSVRC-2012”竞赛（p.3）等是作为背景知识介绍，而非本文的实验。
## 局限

1.  **范围限制**：明确声明专注于处理静态数据的架构，未深入探讨针对序列数据（如LSTMs, Transformers）的动态XAI（p.3）。
2.  **技术深度不均**：根据提供的文本（仅前12页），对**视觉解释**（特别是像素归因）进行了较详细的机制解释，但对**概念解释**的多种方法（如CBM、TCAV）仅提及名称和分类，未展开原理和优缺点分析，这部分深度可能不足。
3.  **缺乏统一的性能评估**：作为综述，它提供了分类和定性分析，但缺乏对不同XAI方法在**一致性、保真度、稳定性**等可量化指标上的系统对比和实验数据，难以直接判断哪个方法在特定场景下绝对“更好”。
4.  **实时性与大规模应用挑战**：文中指出激活最大化等方法计算昂贵（p.7），暗示了许多XAI方法在实时或大规模应用中可能面临效率瓶颈，但综述本身未对此进行深入解决方案的探讨。
## 个人评论

1.  **结构化分类框架**：提出的六个维度提供了一个清晰、系统的“地图”，帮助读者快速定位和理解各种XAI方法的属性、适用场景和局限性，是入门和选型的极佳工具。
2.  **强调“解释模态”的未来方向**：指出理想的XAI方法应同时提供“视觉”和“概念”解释，这对设计下一代XAI方法有重要启发。例如，在医学图像分析中，既需要知道模型关注图像的哪个区域（视觉），也需要知道它用什么病理特征（概念）做出判断。
3.  **连接XAI与WSSS**：揭示了这两个领域的共同目标——理解模型对图像中语义概念的识别与定位，为跨领域研究提供了思路。
4.  **清晰的综述写法范式**：本文逻辑清晰，从背景问题、分类框架，到具体技术分支的深入剖析，为撰写同类综述论文提供了良好的结构范例。

### 使用建议

- **如果快速了解XAI领域**：重点阅读**摘要（p.1）**、**引言（p.1-2）**、**第3章XAI分类概述（p.4-6）**，以及**表1（p.5）**，可以快速掌握XAI的核心问题、分类维度和主流方法概览。
- **如果复现或深入理解某类方法**：由于本文是综述，复现的重点是阅读它引用的**原始论文**（如LIME, Grad-CAM, TCAV等）。本文的作用是提供背景和分类，帮助理解这些原始工作在整体图谱中的位置。
- **如果借鉴创新点**：应学习其**构建分类框架的思路**（如何定义维度、如何兼顾全面性与实用性），以及**将XAI与下游任务（如WSSS）相结合的视角**。这对于在自己的研究领域中系统性地分析问题或提出新分类很有帮助。
- **如果写相关工作**：可将其作为XAI领域的**权威综述**来引用，用于介绍XAI的定义、发展背景、主要技术类别和挑战。尤其适合放在论文的“相关工作”或“背景”章节，为读者提供领域全景。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇关于可解释人工智能（XAI）的综述论文，系统梳理和分析了用于理解和解释复杂机器学习模型（特别是深度神经网络）决策的各类方法。它属于人工智能可解释性方向，核心目标是解决深度学习模型的“黑箱”问题，即其决策过程不透明、难以理解的问题。这篇综述旨在为从业者和研究者提供XAI方法的全景视图和选型指南。根据提供的主题信息，该论文适合放在“A2_医学图像_分类_配准_生成”主题下，因为文中明确提及XAI在医疗等敏感领域部署的重要性（p.2），并且其讨论的方法（如显著图、概念对齐）是理解和改进医学图像分析模型的关键。

## 2. 一句话总结
这篇综述通过提出一个包含六个关键维度的分类框架，对XAI方法（特别是针对视觉任务的像素级和概念级方法）进行了结构化梳理，旨在澄清XAI方法的全景并阐明其在建立可信AI系统中的作用。

## 3. 背景与问题
- **这篇论文为什么要做**：深度神经网络在医学、机器人、经济等领域取得了卓越的预测性能，但其复杂的、端到端学习的决策过程（p.3）导致了“黑箱”特性，阻碍了用户对其预测的信任。模型的可解释性对于在医疗、法律等敏感领域安全部署AI系统至关重要，甚至受到GDPR等法规的强制要求（p.2）。
- **之前方法有什么问题**：尽管已有大量XAI综述，但它们侧重点各异，有的聚焦术语定义，有的关注特定领域应用。这些综述缺少一个统一的、结构化的框架来全面涵盖现有及未来可能的XAI方法（p.2）。
- **作者想解决的核心矛盾**：核心矛盾是深度学习模型追求高性能（依赖于自动学习复杂特征）与人类理解需求（需要透明、可解释的决策逻辑）之间的差距。传统机器学习方法（如决策树）使用手动设计的、人类可理解的特征，决策过程相对透明；而CNN自动学习到的特征高度复杂且非线性，导致决策过程不透明（p.3）。

## 4. 核心贡献
根据文本，本综述的核心贡献如下：
1.  **首次明确定义了XAI的六个关键维度**：解释阶段、解释层级、模型特异性、目标受众、粒度和解释模态（p.2, p.4）。作者声称任何现有或未来的XAI方法都可以归入这些类别。
2.  **对多种XAI方法的优势与局限性进行了跨类别的分析**（p.2），为从业者选择合适的技术提供了指导。
3.  **重点分析了“解释模态”这一维度**，并深入探讨了其下的“视觉解释”和“概念解释”两大子类（p.2, p.4）。作者认为这对于视觉任务尤其关键。
4.  **揭示了XAI与弱监督语义分割（WSSS）之间的紧密联系**（p.2, p.3）。
5.  **为从业者和研究者提供了明确的指引**：为终端用户选择X技术提供指南，为研究者指明当前领域的空白与挑战（p.2）。

## 5. 方法详解
本文是**综述论文**，不提出新的XAI方法，而是对现有方法进行分类、描述和对比。其“方法”即指所提出的分类框架和对各类XAI技术的解析。
- **整体框架**：论文提出了一个六维分类框架（图1）。
    1.  **解释阶段**：分为**后验（Post-hoc）** 方法（模型训练后解释，不改变模型）和**内置（Ad-hoc）** 方法（模型本身具有可解释性，或训练时嵌入可解释性）。
    2.  **解释层级**：分为**全局（Global）**（解释模型整体行为）和**局部（Local）**（解释单个预测）。
    3.  **模型特异性**：分为**模型特定（Model-specific）**（针对特定架构如CNN）和**模型无关（Model-agnostic）**（适用于任何模型）。
    4.  **目标受众**：分为**研究人员**（需要深入技术洞察）和**终端用户**（需要简单易懂的解释）。
    5.  **粒度**：分为**细粒度（Fine-grained）**（如概念级洞察）和**粗粒度（Coarse-grained）**（如类级或物体级洞察）。
    6.  **解释模态**：分为**视觉（Visual）**（如热力图）和**概念（Conceptual）**（如人类可理解的概念）。
- **关键模块/技术**：论文在框架下重点介绍了视觉解释（图2左）和概念解释（图2右）。
    - **视觉解释**：
        - **激活最大化**：通过优化噪声图像或检索训练样本，找到能最强激活某个神经元、层或类的模式（p.7）。优点是能洞察网络学习到的表示；缺点包括生成图像抽象不清晰、计算昂贵、易受对抗性扰动影响（p.7）。
        - **像素归因**：旨在找出对类别预测贡献最大的图像区域，生成热力图（显著图）（p.8）。其基础思想源于线性模型的加权求和思想（p.8）。具体技术包括：
            - **基于反向传播的显著图**：如Simonyan等人提出的方法（文中提及但未展开）。
            - （根据图2）其他类别包括：**扰动方法**和**类激活映射（CAM）**。
    - **概念解释**：（根据文本和图2）旨在将模型学习到的高层特征与人类可理解的语义概念对齐，主要方法包括**网络剖析**、**概念瓶颈模型（CBM）**、**概念白化**、**概念激活向量（CAV）** 及其后验版本。
- **与已有方法的差异**：本文的框架更强调“解释模态”的重要性，并认为未来的XAI方法需要同时提供视觉和概念上的解释（p.2, p.4）。此外，它明确将XAI与WSSS关联起来。

## 6. 实验与结果
本文是**综述性论文**，旨在总结和评估已有的XAI方法，**并未提出新的模型或算法，因此没有包含独立的实验、数据集、评价指标或结果**。它通过对现有文献的梳理和分析来构建其分类框架和观点。文中提及的如“ImageNet LSVRC-2012”竞赛（p.3）等是作为背景知识介绍，而非本文的实验。

## 7. 这篇论文真正有价值的地方
1.  **结构化分类框架**：提出的六个维度提供了一个清晰、系统的“地图”，帮助读者快速定位和理解各种XAI方法的属性、适用场景和局限性，是入门和选型的极佳工具。
2.  **强调“解释模态”的未来方向**：指出理想的XAI方法应同时提供“视觉”和“概念”解释，这对设计下一代XAI方法有重要启发。例如，在医学图像分析中，既需要知道模型关注图像的哪个区域（视觉），也需要知道它用什么病理特征（概念）做出判断。
3.  **连接XAI与WSSS**：揭示了这两个领域的共同目标——理解模型对图像中语义概念的识别与定位，为跨领域研究提供了思路。
4.  **清晰的综述写法范式**：本文逻辑清晰，从背景问题、分类框架，到具体技术分支的深入剖析，为撰写同类综述论文提供了良好的结构范例。

## 8. 局限与问题
1.  **范围限制**：明确声明专注于处理静态数据的架构，未深入探讨针对序列数据（如LSTMs, Transformers）的动态XAI（p.3）。
2.  **技术深度不均**：根据提供的文本（仅前12页），对**视觉解释**（特别是像素归因）进行了较详细的机制解释，但对**概念解释**的多种方法（如CBM、TCAV）仅提及名称和分类，未展开原理和优缺点分析，这部分深度可能不足。
3.  **缺乏统一的性能评估**：作为综述，它提供了分类和定性分析，但缺乏对不同XAI方法在**一致性、保真度、稳定性**等可量化指标上的系统对比和实验数据，难以直接判断哪个方法在特定场景下绝对“更好”。
4.  **实时性与大规模应用挑战**：文中指出激活最大化等方法计算昂贵（p.7），暗示了许多XAI方法在实时或大规模应用中可能面临效率瓶颈，但综述本身未对此进行深入解决方案的探讨。

## 9. 我该怎么使用这篇论文
- **如果快速了解XAI领域**：重点阅读**摘要（p.1）**、**引言（p.1-2）**、**第3章XAI分类概述（p.4-6）**，以及**表1（p.5）**，可以快速掌握XAI的核心问题、分类维度和主流方法概览。
- **如果复现或深入理解某类方法**：由于本文是综述，复现的重点是阅读它引用的**原始论文**（如LIME, Grad-CAM, TCAV等）。本文的作用是提供背景和分类，帮助理解这些原始工作在整体图谱中的位置。
- **如果借鉴创新点**：应学习其**构建分类框架的思路**（如何定义维度、如何兼顾全面性与实用性），以及**将XAI与下游任务（如WSSS）相结合的视角**。这对于在自己的研究领域中系统性地分析问题或提出新分类很有帮助。
- **如果写相关工作**：可将其作为XAI领域的**权威综述**来引用，用于介绍XAI的定义、发展背景、主要技术类别和挑战。尤其适合放在论文的“相关工作”或“背景”章节，为读者提供领域全景。

## 10. 和其他论文的关系
根据给定的主题 `A2_医学图像_分类_配准_生成`，本综述与该主题下的研究有密切关联。它可以作为任何涉及**可解释医学图像分析**工作的理论基础和文献回顾的起点。
- **潜在相关论文**：在医学图像分类任务中应用Grad-CAM进行可视化的论文；在医学图像生成任务中评估模型可解释性的论文；探索概念瓶颈模型在病理图像分析中应用的论文。由于具体库中论文未知，无法建立确切的双链，但上述方向的论文均可与本综述建立关联。
- **可能引用的本综述**：本综述可能会引用（或其内容涉及）**概念激活向量（TCAV）**、**类激活映射（CAM及其变体）** 等在医学影像中常用的XAI技术的原论文。

## 11. 关键词
可解释AI (XAI)， 后验解释， 显著图， 像素归因， 概念级XAI， 深度神经网络， 卷积神经网络 (CNN)， 语义分割， 激活最大化， 模型可解释性

## 12. 可信度说明
本精读笔记主要基于所提供的**PDF文本的前12页**生成，该部分包含了论文的标题、作者、摘要、引言、CNN黑箱特性介绍、XAI分类框架概述（六维度），以及视觉解释部分的起始内容（激活最大化和像素归因简介）。文本提取质量良好，内容连贯。
- **已涵盖内容**：论文定位、背景、核心贡献（分类框架）、部分方法详解（激活最大化、像素归因基础）、与其他工作的关系。
- **未涵盖或需补充说明的内容**：由于仅提供了前12页，以下部分在笔记中只能基于已有信息推测或标注“未找到”：
    - **方法详解的完整性**：概念解释（第5章）、XAI与WSSS（第6章）的详细内容在提供的文本中未出现。
    - **实验与结果**：作为综述，本身无实验，此结论基于论文性质判断。
    - **结论与未来展望**（第7章）未提供。
    - 文中提及的**具体技术细节**（如LIME、SHAP、Grad-CAM的具体公式或算法流程）未在提取文本中展开。
因此，对于方法细节、优缺点的深入分析，以及完整的论文结论，需要参考完整的论文全文（共26页）才能获得更全面的信息。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/可解释AI综述 XAI Survey.txt` (26/26 页; 原 AI 主体 12/26 + 全文补读 13-26); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-26; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-26。
- **提取情况**: 缺失页 14 页, 其中 14 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: One major issue that LIME and other linear approximation approaches face is to
- p.14: To address these performance limitations, model-specific variants of SHAP have been
- p.14: SHAP leverages the structure of these models to compute exact SHAP values much more
- p.14: Perturbation-based XAI methodologies, such as SHAP and LIME, have gained consid-
- p.14: 5. Conceptual Explanations
- p.14: While visual explanations by activation maximisation and pixel attribution techniques
- p.15: Additionally, network dissection focuses on individual units, which may fail to account
- p.15: Lastly, it is better suited for static, pre-trained models and may struggle to offer insights for
- p.15: This is achieved by calculating directional derivatives of model predictions with respect
- p.15: CAV approach to address its limitations in modelling scattered concept examples in a
- p.16: DNNs to autonomously identify established scientific concepts such as grading systems in
- p.16: These models were designed to provide interpretable decisions by incorporating human-

### 缺失页关键摘录

- p.13: Figure 4. The difference between LIME ( a) and Anchors approaches ( b). LIME fits the best possible
- p.13: of the newly fitted model. An attempt to mitigate this limitation was performed by the
- p.13: Figure 4b . Anchors aim to fix a local area where all the instances are from the same class to
- p.14: and accuracy depending on the model type. For instance, Kernel SHAP is the most general
- p.16: a completely different dataset to form concept banks which then can be employed to explain
- p.16: ditional CBMs, which hinders the possibility to do any direct evaluation on individual
- p.17: standardised evaluation metrics and benchmark datasets, making it challenging to compare
- p.17: lack of evaluation tools, Aysel et al. [ 113] proposed novel metrics for concept prediction
- p.17: and localisation while advocating for the use of an existing dataset, Caltech-UCSD Birds
- p.17: (CUB) [114], as a benchmark to evaluate concept-based explanation methodologies. These
- p.18: mentation accuracy while minimising annotation costs. By aligning model interpretability
- p.18: pixel-level annotations while improving model accuracy [ 138]. This integration of inter-
<!-- AI_READING_NOTE_END -->
