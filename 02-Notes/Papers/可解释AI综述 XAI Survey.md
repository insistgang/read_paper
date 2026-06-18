---
title: "Explainable Artificial Intelligence: Advancements and Limitations"
authors:
  - "Halil Ibrahim Aysel"
  - "Xiaohao Cai"
  - "Adam Prugel-Bennett"
year: 2025
venue: "Applied Sciences (Appl. Sci.)"
doi: 10.3390/app15137261
pdf: [[可解释AI综述 XAI Survey.pdf]]
primary_topic: R_综述_Survey
topics:
  - "R_综述_Survey"
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
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Explainable Artificial Intelligence: Advancements and Limitations |
| **作者** | Halil Ibrahim Aysel; Xiaohao Cai; Adam Prugel-Bennett (University of Southampton, School of Electronics and Computer Science) |
| **发表时间** | 2025 (Received 8 May 2025; Accepted 25 June 2025; Published 27 June 2025) |
| **刊物/会议** | Applied Sciences (Appl. Sci.), MDPI, 2025, 15, 7261 — 文章类型 Review |
| **DOI** | 10.3390/app15137261 |

> 说明: 原 frontmatter 的 venue 误写为 "Electronics"，据 PDF 提取文本中的 Citation 与页眉 "Appl. Sci. 2025, 15, 7261" 应为 **Applied Sciences (Appl. Sci.)**，已更正。原 authors 字段为乱码直提，已据扉页更正为三位作者。

## 摘要

清理后英文原摘要（据 PDF 提取文本，修复了无空格直提与断行）：

> Explainable artificial intelligence (XAI) has emerged as a crucial field for understanding and interpreting the decisions of complex machine learning models, particularly deep neural networks. This review presents a structured overview of XAI methodologies, encompassing a diverse range of techniques designed to provide explainability at different levels of abstraction. We cover pixel-level explanation strategies such as saliency maps, perturbation-based methods and gradient-based visualisations, as well as concept-based approaches that align model behaviour with human-understandable semantics. Additionally, we touch upon the relevance of XAI in the context of weakly supervised semantic segmentation. By synthesising recent developments, this paper aims to clarify the landscape of XAI methods and offer insights into their comparative utility and role in fostering trustworthy AI systems.

中文翻译：

> 可解释人工智能 (XAI) 已成为理解和解读复杂机器学习模型（尤其是深度神经网络）决策的关键领域。本综述对 XAI 方法体系给出结构化梳理，涵盖一系列在不同抽象层级提供可解释性的技术。我们既覆盖像素级解释策略（如显著图、基于扰动的方法、基于梯度的可视化），也覆盖将模型行为与人类可理解语义对齐的概念级方法。此外，我们还探讨了 XAI 在弱监督语义分割 (WSSS) 中的相关性。通过综合近期进展，本文旨在厘清 XAI 方法的整体图谱，并就这些方法的相对效用及其在构建可信 AI 系统中的作用提供见解。

> **关键词** (原文): explainable AI; post hoc explanations; saliency maps; concept-based XAI; deep neural networks; semantic segmentation

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **这篇论文为什么要做**：深度神经网络 (DNN) 在医学、机器人、经济等领域取得了优异的预测性能，应用范围涵盖目标检测、股价预测、图像生成、机器翻译等（p.1）。但由于其决策过程复杂、不透明，获得用户对其预测的信任仍是难题（p.1-2）。模型可解释性对在医疗、法律等敏感领域安全部署 AI 至关重要；自 2018 年起，欧洲 GDPR 已强制要求 AI 系统为其决策提供合理解释，进一步凸显 XAI 的关键作用（p.2）。
- **之前方法有什么问题**：已有大量 XAI 综述，但侧重点各异——有的聚焦可解释性的定义与类型，有的关注术语区分（explainability/interpretability/transparency）的详细分类法，有的强调工业 4.0 等特定应用域。作者指出，此前**从未有人显式地把 XAI 的各个"维度"系统地整合在一起**（p.2）。
- **作者想解决的核心矛盾**：高性能（依赖自动学习的复杂特征）与人类可理解性（需要透明、可解释的决策逻辑）之间的差距。传统 ML（决策树、SVM）使用专家手工设计、人类可理解的特征（边缘/纹理检测器、颜色直方图），推理过程相对可追溯；而 CNN 通过多层抽象自动从数据学习特征，学到的表示高度复杂、决策过程非线性，导致"黑箱"式的不透明决策（p.3）。

## 关键贡献

据提取文本，本综述的核心贡献如下：
1.  **首次显式整合 XAI 的六个维度**：解释阶段、解释层级、模型特异性、目标受众、粒度、解释模态（p.2-3, 图1）。作者声称"现有或未来的任何 XAI 方法都可归入这些类别"，且每个维度再分两个子类。作者也强调这些类别是重叠的——同一方法常同时落入多个子类（如既给视觉又给概念解释）（p.2）。
2.  **跨类别分析多种 XAI 方法的优势与局限**（p.2），既服务终端用户（指导其为具体场景选择合适技术），也服务研究者（指出当前领域的空白与挑战、启发未来方向）。
3.  **聚焦"解释模态"维度**，深入其下的"视觉解释"与"概念解释"两大子类（p.2-3）。作者主张"模态是最关键的方面，尤其对视觉任务而言"，并断言可解释性的未来取决于方法能否**同时提供视觉与概念解释**（p.2-3）。
4.  **揭示 XAI 与弱监督语义分割 (WSSS) 的紧密联系**（p.2-3，第 6 章），强调二者的共同目标。
5.  **提供方法选型参考表**：表 1（p.5）按六维度标注了一批代表性方法的归类，可直接作为选型指南。

## 方法

本文是**综述论文**，不提出新的 XAI 方法，而是对现有方法进行分类、描述与对比。其"方法"即所提的分类框架与对各类 XAI 技术的解析。

- **整体框架（六维分类，图1；表1为方法归类示例）**：
    1.  **解释阶段 (Explanation Phase)**：**后验 (Post-hoc)** — 训练后施加，不改变模型结构、无训练/测试期干预；**内置 (Ad-hoc)** — 模型本身可解释（线性模型、决策树）或在训练时把可解释性嵌入架构。内置法常面临"预测能力受限"或"性能折损"的代价，但能即时给出附带的可解释性（p.4）。
    2.  **解释层级 (Explanation Level)**：**全局 (Global)**（跨大量输入刻画模型整体行为）与**局部 (Local)**（针对单个预测说明原因）（p.6）。
    3.  **模型特异性 (Model Specificity)**：**模型特定 (Model-specific)**（利用特定架构如 CNN 的结构）与**模型无关 (Model-agnostic)**（仅需测试输入与预测函数，可用于任意模型）（p.6）。
    4.  **目标受众 (Target Audience)**：**研究者/开发者**（需要深入的技术洞察来改进架构）与**终端用户**（需要交互式可视化或简化解释）。文中点名的面向终端用户的工具有 Google What-If 工具、IBM AI Explainability 360、H2O AutoML 平台（p.6）。
    5.  **粒度 (Granularity)**：**细粒度 (Fine-grained)**（如概念级、特征级洞察）与**粗粒度 (Coarse-grained)**（如类级/物体级）。例：动物分类中，粗粒度=高亮目标类的显著图，细粒度=逐概念的热力图并配文字描述（p.6）。
    6.  **解释模态 (Modality)**：**视觉 (Visual)**（如高亮重要区域的热力图）与**概念 (Conceptual)**（如把斑马图像解释为"条纹"这类人类可理解概念）（p.6）。

- **表 1（p.5）按六维度归类的代表方法**（按 阶段/层级/特异性/受众/粒度/模态 标注）：Activation maximisation、Saliency mapping、Integrated Gradients、Multilevel XAI、CBM、CAM、LIME、Anchors、Network dissection、TCAVs、Post hoc CBM。其中 LIME / Anchors 为后验、局部、模型无关、视觉；TCAVs / Post hoc CBM / CBM 为概念模态；Multilevel XAI 与 Network dissection 同时具备视觉与概念模态。

- **视觉解释（第 4 章，提取文本覆盖到此）**：
    - **激活最大化 (Activation Maximisation)**（p.7）：寻找能最强激活某神经元、特征图、整层或预测类的模式。代表做法之一是**随机噪声图像优化**：从随机噪声出发，对目标单元求梯度，迭代出能最大化其响应的"幻象"图。优点是洞察网络学到的表示；缺点是生成图像高度抽象、对高层神经元尤其不直观、需大量优化步骤因而**计算昂贵**、难以实时或大规模应用。**替代做法**是把整个训练集喂给模型、挑出能强激活某单元的真实图像（避免抽象图），但需用户人工翻检、易引入人类偏差。两类做法都**易受对抗性扰动影响**——输入微小变化即可大幅改变激活而无实际意义，削弱解释可靠性（p.7）。
    - **像素归因 (Pixel Attribution)**（p.8）：通过给每个像素/像素组赋"重要性分数"生成热力图（显著图），高亮对类别预测贡献最大的区域。其直觉源于**线性模型**：线性分类器中类别分数 Sc = Σ w_c^(i) · x^(i)，每个特征按其权重贡献于总分。CNN 含多层非线性，无法直接套用线性权重，故提出各种近似。形式化地，输入图像 x ∈ R^P（P 个像素）经训练好的映射 f: R^P → R^C 得到概率向量，归因法为每个像素赋相关性分数 r_c = [r_c^(1), …, r_c^(P)]，据此掩蔽输入得到显著图（p.8）。
        - **基于反向传播的显著图 (Backpropagation-based Saliency Mapping)**（p.8）：提取文本在此处截断于 "Simonyan et al. pres…"（即 Simonyan 等人提出的方法），未展开。
        - 据图 2，像素归因下还包含**基于扰动 (Perturbation-based)** 与**类激活映射 (CAM)** 两个分支。

- **概念解释（第 5 章，据原文后续页，提取缓存未覆盖, 待核）**：图 2 列出的概念模态方法包括**网络剖析 (Network Dissection)**、**概念瓶颈模型 (CBM)**、**概念白化 (Concept Whitening)**、**概念激活向量 (CAV/TCAV)**。原笔记补读记录显示第 5 章涉及 SHAP 的模型特定变体、TCAV 的方向导数计算、CBM/后验 CBM、以及概念解释缺乏标准化评测指标的问题（详见文末"全文补读记录"，提取缓存未覆盖，待核）。

- **与已有方法的差异**：本框架更强调"解释模态"的重要性，主张理想的 XAI 应**同时**把高层特征对齐到人类可理解概念、并在输入中**空间定位**这些概念（"既知道学到了什么，也知道在哪里"，p.3-4）；并显式把 XAI 与 WSSS 关联起来。

## 实验

本文是**综述性论文**，旨在梳理与评估已有 XAI 方法，**未提出新模型/算法，因此没有独立实验、数据集、评价指标或定量结果**。文中提及的 ImageNet 数据集、AlexNet 在 ImageNet LSVRC-2012 夺冠（p.3）、表 1 的方法归类等，均为背景介绍或定性分类，而非本文的实验。表 1 是定性的"维度归类表"而非性能对比表。

## 局限

1.  **范围限制（作者自陈）**：本综述聚焦处理**静态数据**的架构，明确**不深入序列/动态 XAI**（LSTM、GRU、Transformer 等）。作者承认动态 XAI 日益重要、并列举了 TimeSHAP（扩展 KernelSHAP 解释 RNN）、RETAIN、Temporal Fusion Transformer 等方向，但表示留待单独的后续工作（p.2）。
2.  **缺乏统一的定量评估**：作为综述仅提供分类与定性分析，未对不同方法在一致性、保真度、稳定性等可量化指标上做系统对比，难以直接判断某方法在特定场景下绝对"更好"。（原笔记补读记录亦提到概念解释普遍缺乏标准化评测指标与基准——据原文后续页，提取缓存未覆盖, 待核。）
3.  **效率/实时性挑战**：文中指出激活最大化等方法需大量优化步骤、计算昂贵，实时或大规模应用受限（p.7），但综述本身未给出系统的提效方案。
4.  **解释可靠性**：激活最大化等方法易受对抗性扰动影响，显著图近似方法的保真度也依赖于近似质量（p.7-8）。
5.  **提取覆盖局限（笔记层面）**：本地提取缓存仅覆盖 p.1-12（截止于第 4.2.1 节 Simonyan 句中），第 5 章（概念解释完整内容）、第 6 章（XAI 与 WSSS）、第 7 章（结论与展望）的细节本笔记依赖原笔记的全文补读记录，标注"待核"。

## 个人评论

1.  **结构化分类框架的价值**：六个维度提供了一张清晰的"地图"，能快速定位任一 XAI 方法的属性（何时解释/全局或局部/是否依赖架构/给谁看/多细/什么模态），配合表 1 是入门与选型的好工具。作者强调维度间"重叠"也很务实——真实方法很少只属一类。
2.  **"解释模态"作为主线**：作者把"视觉 + 概念"双模态提为未来方向（既要知道模型看哪里，也要知道它用什么语义概念判断），这一立场贯穿全文，是本综述区别于一般"罗列方法"型综述的主张。落到医学影像等场景尤其有共鸣（既要病灶定位，也要病理概念）。
3.  **连接 XAI 与 WSSS**：把可解释性与弱监督分割的共同目标（理解模型对语义概念的识别与定位）联系起来，为跨领域研究提供了视角——不过这部分内容在本地提取缓存中未覆盖，强度待核。
4.  **写作范式清晰**：从背景问题 → 六维框架 → 模态分支深入，逻辑层次分明，可作为撰写同类综述的结构范例。

### 使用建议

- **快速了解 XAI 领域**：读摘要、引言（p.1-2）、第 3 章六维概述（p.4-6）与表 1（p.5），可掌握核心问题、分类维度与主流方法概览。
- **复现/深入某类方法**：本文是综述，应回到其引用的原始论文（如 LIME、SHAP、CAM/Grad-CAM、TCAV、Anchors 等）；本文的作用是提供背景与"在整体图谱中的位置"。
- **借鉴创新点**：学习其**构建分类框架的思路**（如何定义维度、兼顾全面性与实用性），以及把 XAI 与下游任务（WSSS）结合的视角。
- **写相关工作**：可作为 XAI 领域较新的（2025）综述来引用，介绍 XAI 的定义、动机（含 GDPR）、主要技术类别与挑战。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇关于可解释人工智能 (XAI) 的**综述 (Review)** 论文，发表于 MDPI 期刊 Applied Sciences (Appl. Sci. 2025, 15, 7261)，作者来自英国 University of Southampton（Halil Ibrahim Aysel、Xiaohao Cai、Adam Prugel-Bennett）。它系统梳理用于理解和解释复杂机器学习模型（尤其是深度神经网络）决策的各类方法，核心目标是解决深度模型的"黑箱"问题——决策过程不透明、难以理解。论文属人工智能可解释性方向，定位是为从业者和研究者提供 XAI 方法的全景视图与选型指南。**主题应归入 `R_综述_Survey`**：这是一篇横跨多种 XAI 技术的方法学综述，而非某一具体 CV 任务（医学影像、检测、分割等）的研究论文；原归类 `A2_医学图像_分类_配准_生成` 是误判——医学只是文中举的若干应用域之一。

## 2. 一句话总结
这篇综述提出一个"六维度（解释阶段/层级/模型特异性/目标受众/粒度/解释模态）"分类框架来结构化梳理 XAI 方法（尤以视觉解释与概念解释两大模态为重点），并主张未来的 XAI 应同时提供视觉与概念解释，以构建可信 AI 系统。

## 3. 背景与问题
- **为什么要做**：DNN 在医学、机器人、经济、目标检测、股价预测、图像生成、机器翻译等领域性能优异（p.1），但决策过程复杂不透明，难以获得信任（p.1-2）。可解释性对敏感领域（医疗、法律）安全部署至关重要；自 2018 年起欧洲 GDPR 强制要求 AI 为决策提供解释（p.2）。
- **之前综述的问题**：已有大量 XAI 综述各有侧重（定义与类型、术语分类法、工业 4.0 应用等），但**从未有人显式地把 XAI 的"维度"系统整合在一起**（p.2）。
- **核心矛盾**：高性能（依赖自动学习的复杂非线性特征）与人类可理解性之间的差距。传统 ML（决策树、SVM）用手工设计、人类可理解的特征（边缘/纹理检测器、颜色直方图），推理可追溯；CNN 通过多层抽象自动学特征，表示高度复杂、决策非线性，因而不透明（p.3）。

## 4. 核心贡献
1.  **首次显式整合 XAI 六维度**（解释阶段/层级/模型特异性/目标受众/粒度/解释模态），每维再分两子类，并指出"任何现有/未来 XAI 方法都可归入"且类别间重叠（p.2-3，图1）。
2.  **跨类别分析方法优劣**，兼顾终端用户选型与研究者找空白（p.2）。
3.  **聚焦"解释模态"**，深入视觉解释与概念解释，主张模态是最关键维度、未来 XAI 须同时给视觉+概念解释（p.2-3）。
4.  **关联 XAI 与 WSSS**（p.2-3，第 6 章）。
5.  **提供选型参考表 1**（p.5）：按六维度归类一批代表方法（见下）。

## 5. 方法详解
本文是综述，"方法"即六维分类框架与对各类技术的解析。

**六维框架（图1 / 表1）**：
1. 解释阶段：后验 Post-hoc（训练后施加、不改模型）/ 内置 Ad-hoc（本身可解释或训练时嵌入；常有性能折损，但即时可解释）（p.4）。
2. 解释层级：全局 Global / 局部 Local（p.6）。
3. 模型特异性：模型特定 Model-specific（利用 CNN 等架构）/ 模型无关 Model-agnostic（仅需输入与预测函数）（p.6）。
4. 目标受众：研究者-开发者（深技术洞察）/ 终端用户（交互可视化、简化解释；点名工具：Google What-If、IBM AI Explainability 360、H2O AutoML）（p.6）。
5. 粒度：细粒度（概念级/特征级）/ 粗粒度（类级/物体级）。例：动物分类中粗=类显著图，细=逐概念热力图+文字描述（p.6）。
6. 解释模态：视觉（热力图高亮区域）/ 概念（人类可理解概念，如斑马的"条纹"）（p.6）。

**表 1（p.5）代表方法归类**：Activation maximisation、Saliency mapping、Integrated Gradients、Multilevel XAI、CBM、CAM、LIME、Anchors、Network dissection、TCAVs、Post hoc CBM。其中 Activation maximisation 为后验/全局/模型特定/视觉；Saliency mapping、Integrated Gradients、CAM 为后验/局部/模型特定/视觉；LIME、Anchors 为后验/局部/模型无关/视觉；CBM 为内置/概念，TCAVs、Post hoc CBM 为后验/模型特定/概念；Multilevel XAI、Network dissection 同时具视觉+概念模态。

**视觉解释（第 4 章，提取文本覆盖到此为止）**：
- **激活最大化**（4.1, p.7）：找能最强激活神经元/特征图/层/类的模式。(a) 随机噪声图优化——对目标单元求梯度迭代出"幻象图"，可洞察学到的表示，但抽象不直观、需大量优化步骤、计算昂贵、难实时；(b) 真实图像检索——喂全训练集挑强激活图，避免抽象图但需人工翻检、易引入偏差。两者都易受对抗性扰动影响，削弱可靠性。
- **像素归因**（4.2, p.8）：给每像素赋重要性分数生成显著图/热力图。直觉源于线性模型 Sc = Σ w_c^(i)·x^(i)；CNN 非线性无法直套，故用各种近似（形式化：f: R^P→R^C，归因得 r_c = [r_c^(1),…,r_c^(P)]，据此掩蔽输入得显著图）。
  - 4.2.1 基于反向传播的显著图：提取文本在此截断于 "Simonyan et al. pres…"，未展开。
  - 据图 2，像素归因还含**基于扰动**与**类激活映射 (CAM)** 分支。

**概念解释（第 5 章及之后，据原文后续页，提取缓存未覆盖, 待核）**：图 2 列出网络剖析、概念瓶颈模型 (CBM)、概念白化、概念激活向量 (CAV/TCAV)。原笔记补读记录提及 SHAP 模型特定变体、TCAV 方向导数、CBM/后验 CBM、概念解释缺标准化评测（含 Aysel 等人提出概念预测与定位的新指标并倡用 CUB 鸟类数据集为基准）、以及第 6 章 XAI 与 WSSS——均"待核"。

## 6. 实验与结果
本文是综述，**无独立实验、数据集、指标或定量结果**。文中 ImageNet/AlexNet（LSVRC-2012 夺冠，p.3）、表 1 等为背景或定性分类。表 1 是维度归类表而非性能对比表。

## 7. 这篇论文真正有价值的地方
1.  **六维结构化"地图"**：能快速刻画任一 XAI 方法的属性，配表 1 是选型利器；坦承维度重叠很务实。
2.  **"视觉+概念"双模态主线**：把模态提为最关键维度与未来方向，是本综述的核心主张，区别于纯罗列型综述。
3.  **XAI↔WSSS 桥接**：为跨领域研究提供视角（共同目标=识别+定位语义概念）。
4.  **清晰的综述写作范式**：背景→框架→模态分支深入，结构层次分明。

## 8. 局限与问题
1.  **作者自限范围**：聚焦静态数据架构，不深入动态/序列 XAI（LSTM/GRU/Transformer，列举 TimeSHAP、RETAIN、TFT 等），留待后续工作（p.2）。
2.  **无统一定量评估**：仅定性分类，未在保真度/一致性/稳定性等指标上系统对比；概念解释普遍缺标准化基准（据原文后续页，待核）。
3.  **效率瓶颈**：激活最大化等计算昂贵，实时/大规模应用受限（p.7）。
4.  **可靠性**：激活最大化易受对抗扰动；显著图保真度依赖近似质量（p.7-8）。
5.  **笔记层面**：本地提取缓存仅 p.1-12，第 5-7 章细节依赖原笔记补读记录，标"待核"。

## 9. 我该怎么使用这篇论文
- **快速了解 XAI**：读摘要、引言（p.1-2）、第 3 章六维概述（p.4-6）、表 1（p.5）。
- **复现/深入某类方法**：回到原始论文（LIME、SHAP、CAM/Grad-CAM、TCAV、Anchors 等）；本文给背景与"图谱位置"。
- **借鉴创新点**：学其构建分类框架的思路，及 XAI 与下游任务（WSSS）结合的视角。
- **写相关工作**：作为较新（2025）的 XAI 综述引用，介绍定义、动机（含 GDPR）、技术类别与挑战。

## 10. 和其他论文的关系
本文是 XAI 方法学综述，可作为可解释性相关工作的文献回顾起点，横向连接库内涉及显著图/Grad-CAM/CAM、概念瓶颈、注意力可解释、弱监督分割等主题的论文。
- **被本综述覆盖/引用的代表技术**：激活最大化、显著图、Integrated Gradients、CAM、LIME、Anchors、SHAP/KernelSHAP、网络剖析、CBM/后验 CBM、TCAV、概念白化等。
- **同库关联方向**：任何把 Grad-CAM/CAM 用于可视化的检测/分割/分类工作，以及概念瓶颈、弱监督语义分割相关论文，均可与本综述建立关联（库内具体双链待人工补）。

## 11. 关键词
可解释AI (XAI)，后验解释 (post hoc)，显著图 (saliency map)，像素归因，概念级 XAI，概念瓶颈模型 (CBM)，概念激活向量 (TCAV)，激活最大化，深度神经网络，卷积神经网络 (CNN)，弱监督语义分割 (WSSS)，模型可解释性

## 12. 可信度说明
本精读笔记的**顶部各节与第 1-4 章内容**基于本地提取缓存（PDF 前 12 页，p.1-12，截止于第 4.2.1 节 Simonyan 句中），覆盖标题、作者、摘要、引言、CNN 黑箱特性、六维分类框架（含表 1）、视觉解释（激活最大化、像素归因基础）。这部分**提取质量良好、可逐条对照**。
- **已据提取文本核实**：论文定位、venue 更正（Applied Sciences 而非 Electronics）、作者更正、动机（含 GDPR）、六维框架与各维定义、表 1 方法归类、激活最大化与像素归因机制。
- **依赖原笔记补读记录、提取缓存未覆盖（待核）**：第 5 章概念解释完整内容（SHAP 变体、TCAV、CBM/后验 CBM、概念评测指标与 CUB 基准）、第 6 章 XAI 与 WSSS、第 7 章结论与展望。这些已在正文与文末"全文补读记录"中明确标注"待核"。

---

> **可信度补充**: PDF 提取质量 = **high** (本地缓存 12/26 页, 2086 字符/页, 文本连贯); 提取缓存 `.paper-cache/extracts/可解释AI综述 XAI Survey.txt` 仅覆盖 p.1-12, p.13-26 据原文后续页补读、待核; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。本轮优化: 更正 venue/authors、重建摘要、按提取文本补足六维框架与视觉解释细节、纠正主题分类 A2→R_综述_Survey。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-26; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-26。
- **提取情况**: 本地提取缓存仅含 p.1-12; 以下 p.13-26 线索与摘录来自原笔记的全文补读记录，本地提取缓存未覆盖，**待核**。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索（据原文后续页, 提取缓存未覆盖, 待核）

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

### 缺失页关键摘录（据原文后续页, 提取缓存未覆盖, 待核）

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
