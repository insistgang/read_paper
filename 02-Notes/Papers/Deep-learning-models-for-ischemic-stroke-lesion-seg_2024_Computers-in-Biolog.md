---
title: "Deep learning models for ischemic stroke lesion segmentation in medical images: A survey"
authors:
  - "Jialin Luo"
  - "Peishan Dai"
  - "Zhuang He"
  - "Zhongchao Huang"
  - "Shenghui Liao"
  - "Kun Liu"
year: 2024
venue: "Computers in Biology and Medicine 175 (2024) 108509"
doi: 10.1016/j.compbiomed.2024.108509
pdf: [[Deep-learning-models-for-ischemic-stroke-lesion-seg_2024_Computers-in-Biolog.pdf]]
primary_topic: A1_医学图像_分割
topics:
  - "A1_医学图像_分割"
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
extract_cache: .paper-cache/extracts/Deep-learning-models-for-ischemic-stroke-lesion-seg_2024_Computers-in-Biolog.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/24 pages"
---
# Deep learning models for ischemic stroke lesion segmentation in medical images: A survey

## 基本信息
- **PDF**: [[Deep-learning-models-for-ischemic-stroke-lesion-seg_2024_Computers-in-Biolog.pdf]]
- **primary_topic**: `A1_医学图像_分割`
- **topics**: `A1_医学图像_分割`, `R_综述_Survey`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Deep learning models for ischemic stroke lesion segmentation in medical images: A survey |
| **作者** | Jialin Luo; Peishan Dai (通讯, daipeishan@csu.edu.cn); Zhuang He; Zhongchao Huang; Shenghui Liao; Kun Liu |
| **机构** | 中南大学计算机科学与工程学院 / 基础医学院生物医学工程系；湖南省脑科医院（湖南省第二人民医院），长沙 |
| **发表时间** | 2024（投稿 2023-11-02，修回 2024-02-09，录用 2024-04-21，在线 2024-04-25） |
| **刊物/会议** | Computers in Biology and Medicine 175 (2024) 108509 |
| **DOI** | 10.1016/j.compbiomed.2024.108509 |

## 摘要

**英文原摘要（据 PDF 提取文本整理，已修复断字与空格）**

> This paper provides a comprehensive review of deep learning models for ischemic stroke lesion segmentation in medical images. Ischemic stroke is a severe neurological disease and a leading cause of death and disability worldwide. Accurate segmentation of stroke lesions in medical images such as MRI and CT scans is crucial for diagnosis, treatment planning and prognosis. This paper first introduces common imaging modalities used for stroke diagnosis, discussing their capabilities in imaging lesions at different disease stages from the acute to chronic stage. It then reviews three major public benchmark datasets for evaluating stroke segmentation algorithms: ATLAS, ISLES and AISD, highlighting their key characteristics. The paper proceeds to provide an overview of foundational deep learning architectures for medical image segmentation, including CNN-based and transformer-based models. It summarizes recent innovations in adapting these architectures to the task of stroke lesion segmentation across the three datasets, analyzing their motivations, modifications and results. A survey of loss functions and data augmentations employed for this task is also included. The paper discusses various aspects related to stroke segmentation tasks, including prior knowledge, small lesions, and multimodal fusion, and then concludes by outlining promising future research directions. Overall, this comprehensive review covers critical technical developments in the field to support continued progress in automated stroke lesion segmentation.

**中文翻译**

> 本文对用于医学图像中缺血性卒中病灶分割的深度学习模型进行了全面综述。缺血性卒中是一种严重的神经系统疾病，也是全球主要的致死与致残原因之一。在 MRI、CT 等医学图像上对卒中病灶进行准确分割，对诊断、治疗规划和预后判断都至关重要。本文首先介绍卒中诊断常用的成像模态，讨论它们在从急性期到慢性期不同病程阶段成像病灶的能力；随后回顾三个用于评估卒中分割算法的主要公开基准数据集——ATLAS、ISLES 和 AISD，并梳理其关键特性；接着概述医学图像分割的基础深度学习架构，包括基于 CNN 与基于 Transformer 的模型；进一步总结近期针对这三个数据集、把上述架构适配到卒中病灶分割任务的创新工作，分析其动机、改动与结果；同时综述了该任务采用的损失函数与数据增强策略。文章还讨论了与卒中分割相关的若干方面，包括先验知识、小病灶和多模态融合，最后展望了有前景的未来研究方向。总体而言，本综述覆盖了该领域的关键技术进展，以支持自动化卒中病灶分割的持续发展。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：卒中是常见的脑血管疾病，是全球**第二大致死原因、第三大致残原因**。卒中按成因分两类：血栓栓塞导致**缺血性卒中**，血管破裂导致**出血性卒中**；其中缺血性卒中最常见，约占所有卒中病例的 **87%**，其血栓多源于大动脉粥样硬化和心脏疾病。2017 年全球约有 **270 万**患者死于缺血性卒中。本文专注于缺血性卒中。对卒中病灶进行分割，对量化梗死体积、检测可能被忽略的小病灶、自动化病情评估、以及预测出血转化等预后具有重要意义。
- **之前方法的问题 / 任务难点**：卒中病灶分割属于医学图像分割的一个专门应用，难点在于病灶在**外观、形状、大小和位置上变异巨大**；更关键的是**缺乏大规模、公开可用的标注数据集**。与自然图像不同，医学图像（CT 体素值以 Hounsfield 单位计，范围约 −1000~1000）承载具体物理含义；卒中病灶常呈不规则、非凸形状，边界模糊；急性期因缺血、出血、水肿并存信号不均匀，慢性期边界更清晰、信号更均匀。此外，病灶常多发、跨血管区域，并与微出血、白质高信号、脑萎缩等其他病变共存；不同扫描仪、磁场强度、采集协议、对比度造成进一步的异质性。
- **核心矛盾**：深度学习在医学图像分割上进展显著，但针对**缺血性卒中病灶**这一特定目标，有效分割仍因病灶异质性、边界模糊、与其他病变共存、模态/协议多样、标注数据稀缺而极具挑战。作者旨在系统总结该领域 state-of-the-art 并指出有前景的研究方向。文中以 RapidAI 为例说明 AI 工具在临床卒中诊断中正变得不可或缺。

## 关键贡献

1.  **梳理临床成像模态与病程阶段**：系统介绍 CT、MRI、血管造影、灌注成像在卒中诊断中的作用，并对超急性期、急性期、亚急性期、慢性期四个阶段的时间窗、影像特征与治疗目标做对照（Table 1、Table 2、Table 3）。
2.  **梳理三个公开基准数据集**：系统介绍 **ATLAS、ISLES、AISD**，说明各自模态、卒中阶段、图像间距、扫描数量与研究目的（Table 4）。
3.  **综述基础深度学习架构**：概述医学图像分割的基础架构，包括基于 **CNN** 的模型（如 U-Net）和日益流行的基于 **Transformer** 的模型。
4.  **总结针对卒中任务的模型创新**：分析在上述数据集上，针对卒中分割对基础架构所做的适配性修改、动机与结果（据原文后续页 Table 5，提取缓存未覆盖，待核）。
5.  **综述损失函数与数据增强**：梳理常用损失函数（CE Loss、Dice Loss、Focal Loss、Focal Dice Loss 等）及其改进版本，以及数据增强策略。
6.  **讨论关键挑战与未来方向**：聚焦**先验知识（如大脑左右半球准对称性）的利用、小病灶检测、多模态信息融合**等议题，并展望未来研究方向。

## 方法

**重要提示**：本文为**综述论文**，本身**不提出新的分割方法**，而是对现有方法做系统回顾。本节概述论文所归纳的方法框架与关键技术点。

- **整体框架**：把现有分割模型归纳为两大类基础架构——**CNN-based**（以 U-Net 及其变体为代表）和 **Transformer-based**（利用自注意力建模长程依赖）。这些模型应用于从 2D/3D 脑部医学图像（MRI 或 CT）中分割卒中病灶。
- **输入输出**：
    - **输入**：患者脑部 **CT 或 MRI 扫描**（T1w、T2w、DWI、ADC、FLAIR、NCCT 等），可为单模态或多模态。
    - **输出**：与输入同尺寸的**二值/概率掩膜**，标识病灶区域（像素级分类：病灶 vs 背景）。
- **关键机制与先验知识**：
    - **CNN-based（U-Net 类）**：编码器-解码器结构，靠跳跃连接融合低层细节与高层语义。
    - **脑部对称先验**：大脑左右半球在脑图像中**准对称**，部分模型利用该先验改进分割性能（文中引用 [21,22]）。
    - **Transformer-based**：用自注意力捕捉长程依赖，理解病灶与周围组织的全局上下文；文中点名 **Factorizer** 作为有潜力广泛应用于该领域的稳健方法。
    - **时间演变特性**：同一模态下卒中病灶影像特征随时间演变（如 MR 上可由高信号变为低信号或等信号，反之亦然），增加分割难度。
- **损失函数（直观解释）**：
    - **Dice Loss**：直接优化分割与真值的重叠度，对类别不平衡（小病灶）更敏感。
    - **Focal Loss**：降低易分样本权重，使模型更关注难分样本（如模糊边界）。
    - **Focal Dice Loss** 等为上述的改进组合。
- **训练方式**：基于带标注数据集做**有监督训练**，并配合数据增强提升泛化（详见第 6 节，据原文后续页，提取缓存未覆盖）。
- **本文（综述）的定位差异**：聚焦"缺血性卒中"这一特定病种，从**数据、模型、损失函数、领域挑战**多个维度系统梳理，而非对比单个新旧方法的性能。

**论文类型特化（医学类）**：
- **任务类型**：**语义分割**（逐像素分类为病灶或背景）。
- **图像模态**：主要为 **MRI**（T1w, T2w, DWI, ADC, FLAIR）和 **CT**（NCCT）；也涉及血管造影（CTA/MRA）与灌注成像（PWI: CTP/MRP），但指出后两类公开数据集稀缺。文中提到约 90% 患者为急性（含超急性）缺血性卒中；NCCT 因可及性高、采集快常作首选初查，并用 ASPECTS 评分估计严重程度；DWI/ADC 对急性缺血灶敏感（症状发作 1–2 h 内即可识别），DWI 与 FLAIR 的 mismatch 可用于估计发病时间。
- **数据集**：**ATLAS, ISLES, AISD** 为主要评估基准。
- **临床意义**：分割用于**量化梗死体积、辅助治疗决策（识别可挽救的缺血半暗带）、评估病情、预测预后**，是 RapidAI 等临床 AI 工具的关键一环。

## 实验

本文为综述，其"实验"主要体现在对现有研究结果的**系统性比较与总结**，而非作者自行开展的实验。

- **使用/综述的数据集**：
    1.  **ATLAS**（Anatomical Tracings of Lesions After Stroke）：多中心采集的脑部 **T1 加权 MRI**，覆盖亚急性期与慢性期病灶。初版 R1.2（2018）含 304 例但无预设训练/测试划分；R2.0（2022）扩大到 **1271 例**，划分为训练集 **655** / 测试集 **300** / 泛化集 **316**；其中**仅训练集标签公开**，测试集标签不公开（评估需提交）。p.3-4
    2.  **ISLES**：**多模态 MRI** 图像，覆盖急性期至亚急性期；其 ISLES-SPES、ISLES2018 等子集含 CTP 等灌注数据，但数据量仍相对有限。p.4
    3.  **AISD**：**早期非对比 CT（NCCT）扫描**，旨在推动面向一线急性卒中诊断的分割算法。p.4
- **对比方法**：文中按 CNN-based 与 Transformer-based 两大家族归纳具体卒中分割模型并汇总核心思想（据原文后续页 Table 5，提取缓存未覆盖，待核）。提取文本（前 12 页）未列出各方法的逐一性能数字。
- **评价指标**：提取文本（前 12 页）未集中列出指标定义；据原文后续页提到 **Dice 系数**作为主要指标（"1.7%~3.7% in terms of the Dice coefficient on ATLAS dataset"，据原文 p.16，提取缓存未覆盖，待核）。
- **主实验结果**：提取文本（前 12 页）未含各方法在各数据集上的完整性能对比表；相关定量比较位于原文后续页（提取缓存未覆盖，待核）。
- **泛化实验**：ATLAS R2.0 专门划分了"泛化集"（316 例）用于评估模型泛化能力。p.4
- **速度/参数量/FLOPs**：提取文本中未找到相关信息。

## 局限

1.  **公开数据集仍有限**：文中明确指出针对 **CTA/MRA 与灌注成像（CTP/MRP）** 的公开数据集非常稀缺，且 CTA/MRA 自动化分析研究相对滞后，限制了相关算法的发展与评估。
2.  **缺乏统一/跨阶段数据集**：据原文后续页（p.13，提取缓存未覆盖，待核），缺少覆盖不同卒中阶段的统一数据集；超急性期数据尤其匮乏，受关注较少；即使同一数据集，不同研究之间也存在划分/评估口径不一致的问题（如 ATLAS R2.0 测试集标签不公开导致评估方式受限）。
3.  **病程阶段时间界定不统一**：不同研究对各阶段（亚急性/慢性等）的时间划分不一致（文中举出 [41]/[28]/[40] 三种不同划分），阶段边界依赖临床观察、治疗反应与恢复过程，并非绝对。
4.  **泛化性挑战未完全解决**：病灶异质性、扫描仪/磁场/协议差异、对比度差异、部分容积效应、运动伪影等，仍是构建鲁棒、可泛化分割模型的主要障碍；综述无法提供单一解决方案。
5.  **作为综述的固有局限**：对具体模型技术细节的剖析深度不及单篇论文解读；全面性依赖文献选取。
6.  **本笔记的覆盖局限**：提取缓存仅含原文前 12/24 页，第 4 节（基础架构与卒中模型创新）、第 5 节（含 5.5 Summary）、第 6 节（数据增强）、讨论与结论的具体定量内容主要据后续页线索标注，未逐字核实（详见文末"全文补读记录"）。

## 个人评论

这篇综述的最大价值在于为研究者提供了一张 **"缺血性卒中病灶分割"领域的全景地图与快速入门指南**：

1.  **系统性**：把零散研究（数据、模型、损失、技巧）整合进清晰框架，从"病程阶段—成像模态—数据集—基础架构—任务适配—损失/增强—领域难题"逐层展开，帮助读者快速建立整体认知。
2.  **针对性**：不泛谈医学图像分割，而是深入卒中这一具体病种，揭示其独有挑战——病灶随时间演变（信号翻转）、不同模态/阶段表现差异、小病灶检测、与其他病变共存。
3.  **数据视角扎实**：对 ATLAS（含 R1.2→R2.0 演进与测试集标签不公开这一实务细节）、ISLES、AISD 的对照尤其实用；明确点出 CTA/MRA 与灌注数据稀缺是领域明显空白，对找选题很有价值。
4.  **实践性**：对损失函数、数据增强、脑对称先验等的讨论，直接为模型设计与训练提供技术参考。

**对后续研究的启发**：若做卒中分割相关研究，本文能快速回答——用什么数据（及其坑，如测试集标签不公开）？前人用了哪些框架、做了哪些改进？哪些公认难题未解（多模态融合、跨域泛化、小病灶、超急性期数据缺失）？从而高效设计研究方案。需注意：本综述前半（成像与数据集）信息密度高且可直接采用；涉及具体模型性能对比时应回到原文后半部分与 Table 5 核对，不要据本笔记的二手描述直接引用数字。

### 使用建议

- **如果快速了解**：读摘要、引言（第 1 节）和结论；浏览第 3 节数据集表（Table 4）快速掌握领域常用"比赛场地"。
- **如果复现**：精读第 3 节，了解 ATLAS/ISLES/AISD 的模态、划分、间距与预处理要求（特别注意 ATLAS R2.0 仅训练集标签公开）。模型细节见第 4–5 节（原文后半，本笔记未覆盖）。
- **如果借鉴创新点**：重点读讨论章节关于**先验知识、小病灶、多模态融合**的部分及未来方向。
- **如果写 Related Work**：本综述是极佳的 Related Work 素材，可归为"医学图像分割综述"或更具体的"缺血性卒中病灶分割综述"，引用其对数据集、基础模型与领域挑战的总结。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A1_医学图像_分割]]
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇发表于 *Computers in Biology and Medicine* (2024, 175:108509) 的**综述论文**，由中南大学 Jialin Luo、Peishan Dai 等人撰写。它聚焦于**医学图像分割**的一个具体临床应用——**缺血性卒中病灶分割**，系统回顾在 MRI/CT 等医学图像中分割缺血性卒中病灶的深度学习模型，覆盖临床成像模态与病程阶段、公开数据集、基础网络架构（CNN / Transformer）、任务适配创新、损失函数与数据增强、以及先验知识/小病灶/多模态融合等领域难题与未来方向。按主题分类，它属于 **A1_医学图像_分割**，并具备 **R_综述_Survey** 属性。（注：原笔记将其归入 A2_分类_配准_生成，与论文实际主题"分割"不符，本次已修正。）

## 2. 一句话总结
本综述系统梳理了缺血性卒中病灶分割的深度学习方法，从成像模态/病程阶段、ATLAS/ISLES/AISD 三大公开数据集、CNN 与 Transformer 基础架构、任务适配创新、到损失函数/数据增强与先验知识/小病灶/多模态融合等难题，给出该领域的全景与未来方向。

## 3. 背景与问题
- **为什么要做**：卒中是全球第二大致死、第三大致残原因；缺血性卒中约占 87%，2017 年全球约 270 万人死于缺血性卒中。卒中病灶分割对量化梗死体积、检测易漏小病灶、自动化病情评估、预测出血转化等预后至关重要，是 AI 在卒中诊疗中的关键应用（如 RapidAI）。
- **任务难点**：病灶在外观、形状、大小、位置上变异巨大；非凸不规则、边界模糊；急性期信号不均、慢性期趋于均匀；常多发、跨血管区域，并与微出血/白质高信号/脑萎缩共存；扫描仪、磁场、协议、对比度差异带来异质性；同模态下病灶信号随时间演变。最核心的瓶颈是**缺乏大规模公开标注数据**。
- **核心矛盾**：通用深度学习分割已较成熟，但卒中病灶这一特定目标因上述异质性 + 数据稀缺，仍难以稳健分割。本文不提新方法，而是系统总结现状与方向。

## 4. 核心贡献
1.  **临床成像模态与病程阶段梳理**：CT/MRI/血管造影/灌注成像在四个阶段（超急性/急性/亚急性/慢性）的作用、影像特征与治疗目标（Table 1–3）；指出约 90% 患者为急性（含超急性），NCCT 常作初查并配 ASPECTS 评分，DWI/ADC 对急性灶敏感，DWI–FLAIR mismatch 可估发病时间。
2.  **三大公开数据集对照**：ATLAS（T1w，亚急/慢性）、ISLES（多模态 MRI，急性~亚急性）、AISD（早期 NCCT，急性一线诊断），含模态/阶段/间距/扫描数/研究目的（Table 4）。
3.  **基础架构综述**：CNN-based（U-Net 类）与 Transformer-based 两大家族。
4.  **任务适配创新总结**：针对三数据集对架构的修改、动机与结果（Table 5，原文后续页）。
5.  **损失函数与数据增强综述**：CE / Dice / Focal / Focal Dice Loss 等及改进版。
6.  **领域难题与未来方向**：先验知识（脑对称性）、小病灶、多模态融合。

## 5. 方法详解
本文为综述，不提新方法。其归纳的方法体系如下：
- **两大基础架构**：CNN-based（编码器-解码器 + 跳跃连接，如 U-Net）与 Transformer-based（自注意力建模长程依赖，文中点名 **Factorizer** 为有潜力的稳健方法）。
- **输入**：脑部 CT/MRI（NCCT、T1w、T2w、DWI、ADC、FLAIR 等），单/多模态；**输出**：同尺寸二值/概率分割掩膜（病灶 vs 背景）。
- **卒中专属先验**：大脑左右半球准对称，可作先验改进分割（[21,22]）；病灶信号随病程演变需在建模时考虑。
- **损失函数**：Dice Loss 优化重叠度、对小病灶/类别不平衡敏感；Focal Loss 降低易分样本权重、聚焦难分样本（模糊边界）；Focal Dice Loss 等为组合改进。
- **训练**：有监督 + 数据增强（第 6 节，据原文后续页 p.13 起，提取缓存未覆盖，待核：数据增强对解决数据稀缺很关键；并提到需要图像 harmonization 以保证跨中心风格一致）。
- **临床意义**：分割支撑梗死体积量化、半暗带识别、病情评估与预后预测。

## 6. 实验与结果
本文为综述，"实验"即对现有研究结果的系统比较与总结。
- **数据集**：
    1.  **ATLAS**：T1w MRI，亚急/慢性；R1.2(2018) 304 例无划分 → R2.0(2022) 1271 例 = 训练 655 / 测试 300 / 泛化 316；仅训练集标签公开，测试集标签不公开。p.3-4
    2.  **ISLES**：多模态 MRI，急性~亚急性；含 CTP 等灌注子集（ISLES-SPES、ISLES2018），数据量仍有限。p.4
    3.  **AISD**：早期 NCCT，面向一线急性诊断。p.4
- **对比方法**：按 CNN / Transformer 两族汇总核心思想（Table 5，原文后续页，提取缓存未覆盖，待核）。
- **评价指标**：以 **Dice 系数**为主（"1.7%~3.7% Dice 提升 on ATLAS"，据原文 p.16，提取缓存未覆盖，待核）；前 12 页未集中给出指标定义。
- **主结果 / 消融**：完整定量对比表位于原文后半（提取缓存未覆盖，待核）。
- **泛化**：ATLAS R2.0 设泛化集 316 例。p.4
- **速度/参数量/FLOPs**：提取文本未找到。

## 7. 这篇论文真正有价值的地方
1.  **系统性**：把数据、模型、损失、技巧整合进"阶段—模态—数据—架构—适配—损失/增强—难题"的清晰框架。
2.  **针对性**：深入卒中病种，揭示其独有挑战（信号随时间翻转、多模态/多阶段差异、小病灶、与其他病变共存）。
3.  **数据视角扎实且实务**：ATLAS R1.2→R2.0 演进、测试集标签不公开、CTA/MRA 与灌注数据稀缺等细节，对选题与避坑直接有用。
4.  **实践性**：损失函数、数据增强、脑对称先验等讨论可直接指导建模。

## 8. 局限与问题
1.  **公开数据有限**：CTA/MRA、灌注（CTP/MRP）数据稀缺，相关研究滞后。
2.  **缺统一/跨阶段数据集**、阶段时间界定不一致、同数据集评估口径不一（据原文后续页 p.13，提取缓存未覆盖，待核）。
3.  **泛化性挑战未解**：异质性、扫描仪/协议差异、伪影/部分容积效应等仍是主要障碍。
4.  **综述固有局限**：对单模型技术细节剖析深度有限；全面性依赖文献选取。
5.  **本笔记覆盖局限**：提取缓存仅前 12/24 页，后半（第 4–6 节、讨论、结论）的定量内容主要据后续页线索标注，未逐字核实。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + 结论；浏览数据集表（Table 4）掌握"比赛场地"。
- **复现**：精读第 3 节数据集（注意 ATLAS R2.0 仅训练集标签公开）；模型细节见第 4–5 节（原文后半）。
- **借鉴创新**：读讨论中先验知识/小病灶/多模态融合与未来方向。
- **写 Related Work**：作为卒中分割综述直接引用其数据集、基础模型与挑战总结；引用具体性能数字前回原文核对。

## 10. 和其他论文的关系
- 本综述是对大量原始研究的总结，与其讨论的每项具体工作存在直接引用关系。
- 关联类型：
    - 其他医学图像分割综述（尤其脑部疾病，如脑肿瘤）。
    - 在 ATLAS/ISLES/AISD 上提出新方法的具体论文。
    - 通用医学图像分割架构论文（如 U-Net、nnU-Net、Transformer 分割模型 Factorizer 等）。
    - 损失函数相关论文（Dice Loss、Focal Loss [38]、Focal Dice Loss [39] 等）。
- 本文自身：`[[Deep learning models for ischemic stroke lesion segmentation in medical images: A survey]]`

## 11. 关键词
缺血性卒中, 病灶分割, 分割技术, 深度学习, 医学图像分析, MRI, CT, NCCT, DWI, FLAIR, 公开数据集（ATLAS/ISLES/AISD）, U-Net, Transformer, Factorizer, 损失函数（Dice/Focal/Focal Dice）, 数据增强, 先验知识, 小病灶, 多模态融合, 综述

## 12. 可信度说明
本篇精读笔记的**前半部分（成像模态、病程阶段、ATLAS/ISLES/AISD 数据集、CNN/Transformer 基础架构、损失函数清单）严格依据提取缓存的前 12/24 页**，事实（87% 占比、270 万死亡、第二/三大致死致残、ATLAS 1271=655/300/316 且仅训练集标签公开、Factorizer、CE/Dice/Focal/Focal Dice Loss、CTA/MRA 与灌注数据稀缺等）均可在提取文本中逐条核对。**论文后半（第 4 节卒中模型创新、第 5 节及 5.5 Summary、第 6 节数据增强、讨论与结论的具体定量对比，以及 "1.7%~3.7% Dice on ATLAS" 等数字）超出提取缓存覆盖范围，依据原文后续页的缺失页线索整理并已逐处标注"据原文后续页，提取缓存未覆盖，待核"**。笔记未编造提取文本之外的具体数字或结论。

---

> **可信度补充**: PDF 提取质量 = **high** (提取质量好, 约 2086 字符/页); 来源缓存: `.paper-cache/extracts/Deep-learning-models-for-ischemic-stroke-lesion-seg_2024_Computers-in-Biolog.txt` (提取缓存覆盖 12/24 页; 原 AI 主体 12/24 + 全文补读线索 13-24); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本次优化以提取文本前 12 页为唯一事实来源, 后半内容据缺失页线索标注待核。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-24; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-24。
- **提取情况**: 提取缓存实际仅含前 12/24 页可读文本（max_chars=25000 截断于 3.1 节 ATLAS）。p.13-24 的内容依据下方缺失页线索标注, 未进入提取缓存正文。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Computers in Biology and Medicine 175 (2024) 108509
- p.13: 5.5. Summary
- p.13: The lack of publicly available hyperacute stage data means that
- p.13: Due to the absence of a unified dataset covering stroke data at dif-
- p.13: Models based on AISD or APIS, on the other hand, focuses on acute
- p.13: Even within the same dataset, there is inconsistency among studies
- p.13: 6. Data augmentations
- p.13: Data augmentation plays a crucial role in medical image segmen-
- p.13: It enables the generation of additional training samples, addressing
- p.13: As one of the most influential frameworks for automated medical
- p.14: Therefore, image harmonization is required to ensure consistency in
- p.14: Therefore, it is essential to achieve harmonization to ensure the style

### 缺失页关键摘录

- p.13: We summarized the core ideas of the above work in Table 5. In
- p.13: peracute stage stroke dataset, there is relatively less attention given to
- p.13: potentially encompassing hyperacute stage data in their SPES dataset.
- p.13: Due to the absence of a unified dataset covering stroke data at dif-
- p.13: stroke stages within the same image. Our discussion is also dataset-
- p.13: Even within the same dataset, there is inconsistency among studies
- p.13: ATLAS R2.0, although the dataset is divided into training and test set,
- p.13: the labels for the test set are not publicly available, and evaluation
- p.14: demonstrated the efficacy of this approach in enhancing the accuracy
- p.14: 2018 dataset, the task is to segment the infarct core of stroke from
- p.16: 1.7% ∼3.7% in terms of the Dice coefficient on ATLAS dataset.
- p.16: minimally to the overall loss, and as a result, it is often overlooked.
<!-- AI_READING_NOTE_END -->
