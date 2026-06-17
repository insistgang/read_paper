---
title: "Oriented object detection in optical remote sensing images using deep learning: a survey"
authors:
  - "Kun Wang"
  - "Zi Wang"
  - "Zhang Li"
  - "Ang Su"
  - "Xichao Teng"
  - "Erting Pan"
  - "Minhao Liu"
  - "Qifeng Yu"
year: 2025
venue: "Artificial Intelligence Review"
doi: 10.1007/s10462-025-11256-0
pdf: [[2023_Oriented_object_dete.pdf]]
primary_topic: C_目标检测_通用与旋转框
topics:
  - "C_目标检测_通用与旋转框"
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2023_Oriented_object_dete.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/61 pages"
---
# Oriented object detection in optical remote sensing images using deep learning: a survey

## 基本信息
- **PDF**: [[2023_Oriented_object_dete.pdf]]
- **primary_topic**: `C_目标检测_通用与旋转框`
- **topics**: `C_目标检测_通用与旋转框`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Oriented object detection in optical remote sensing images using deep learning: a survey |
| **作者** | Kun Wang; Zi Wang; Zhang Li（三人并列一作）; Ang Su; Xichao Teng; Erting Pan; Minhao Liu; Qifeng Yu |
| **发表时间** | 2025（Accepted 2 May 2025）|
| **刊物/会议** | Artificial Intelligence Review (2025) 58:350 |
| **DOI** | 10.1007/s10462-025-11256-0 |

> 注：文件名词干以 "2023" 开头，但据提取文本 PDF 首页，本文实际为 2025 年录用、刊于 *Artificial Intelligence Review* 卷 58 文章号 350。原 frontmatter 的 year=2023、venue=题目均系骨架阶段误填，已据提取文本订正为 year=2025、venue=Artificial Intelligence Review。

## 摘要

> Oriented object detection is a fundamental yet challenging task in remote sensing (RS), aiming to locate and classify objects with arbitrary orientations. Recent advancements in deep learning have significantly enhanced the capabilities of oriented object detection methods. Given the rapid development of this field, a comprehensive survey of the recent advances in oriented object detection is presented in this paper. Specifically, we begin by tracing the technical evolution from horizontal object detection to oriented object detection and highlighting the specific related challenges, including feature misalignment, spatial misalignment, oriented bounding box (OBB) regression problems, and common issues encountered in RS. Subsequently, we further categorize the existing methods into detection frameworks, OBB regression techniques, feature representation approaches, and solutions to common issues and provide an in-depth discussion of how these methods address the above challenges. In addition, we cover several publicly available datasets and evaluation protocols. Furthermore, we provide a comprehensive comparison and analysis involving the state-of-the-art methods. Toward the end of this paper, we identify several future directions for oriented object detection research.
>
> **关键词**: Oriented object detection · Remote sensing · Deep learning

> **中文翻译**: 定向目标检测是遥感（RS）中一项基础却富有挑战的任务，目标是定位并分类具有任意朝向的物体。深度学习近年的进展显著提升了定向目标检测方法的能力。鉴于该领域发展迅速，本文对定向目标检测的最新进展做一次全面综述。具体而言，我们首先梳理从水平目标检测到定向目标检测的技术演进，并指出其特有的相关挑战，包括特征错位（feature misalignment）、空间错位（spatial misalignment）、旋转框（OBB）回归问题，以及遥感中遇到的常见问题。随后，我们将现有方法进一步归类为检测框架、OBB 回归技术、特征表示方法、以及针对常见问题的解决方案四大维度，并深入讨论这些方法如何应对上述挑战。此外，我们梳理了若干公开数据集与评估协议，并对最先进（SOTA）方法做了全面的对比与分析。文末，我们指出了定向目标检测研究的若干未来方向。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：随着遥感技术快速发展，光学卫星与无人机（UAV）能以各种分辨率、不同光谱便捷获取海量图像，研究界迫切需要自动、高效地处理与分析这些遥感图像的先进技术。目标检测是自动分析遥感图像的关键基础，已广泛用于智能监控、精准农业、城市规划、港口管理、军事侦察等应用（p.1-2）。由于遥感图像多采用鸟瞰视角（BEV）拍摄，物体（车辆、船舶、建筑等）往往呈任意朝向，通用的水平目标检测方法因此显得力不从心；定向目标检测（又称旋转目标检测）改用旋转框（OBB）紧贴物体，既能提供朝向信息又能精确定位（p.2，图1）。
- **之前方法的问题**：
    1.  **水平框检测的局限性**：直接将水平目标检测器用于遥感图像会导致：（1）在密集排列场景、尤其大长宽比物体上，一个 HBB 与相邻 HBB 之间的 IoU 可能很大（图1b），非极大值抑制（NMS）容易造成漏检；（2）HBB 倾向于包含大量背景区域，而 OBB 能紧贴物体、定位更精确（图1a）（p.6）。
    2.  **定向检测的特定挑战**：把水平检测器改造为预测旋转框（增加额外参数表示 OBB）时，会引入若干额外挑战（p.6-8）：
        - **特征错位（feature misalignment）**：通用检测器的特征由轴对齐卷积提取，与旋转物体之间存在不可忽视的错位（图3a），特征缺乏旋转信息，使检测器难以识别物体并回归精确 OBB；
        - **空间错位（spatial misalignment）**：基于锚点的检测器以水平锚点为先验，与旋转物体（尤其大长宽比）IoU 很小（图4a），按 IoU 划分正负样本的标签分配策略难以提供足够正样本；
        - **旋转框回归问题（OBB regression problems）**：最常用的 θ-based 表示存在角度周期性（PoA），当角度逼近边界时微小角差会引起损失剧变，造成角度边界不连续；四边形表示则面临顶点排序问题，预测 OBB 与真值（GT）的顶点序列可能不一致。两者都会严重干扰网络、导致训练不稳定（p.7-8，细节见原文附录 A、B 节）。
- **核心矛盾**：如何有效化解定向检测引入的**特征错位、空间错位、旋转框回归**三大难题，同时克服遥感图像本身固有的**尺度变化、复杂背景、弱特征响应**等常见问题（p.6 列出三类常见问题并各给出代表性文献）。
## 关键贡献

据提取文本第 1.3 节（p.5），本文贡献明确归纳为四点：
1.  **全面回顾从水平目标检测到定向目标检测的技术演进**，并基于遥感图像特性与现有检测模型，把定向目标检测的主要挑战归纳为四类：特征错位、空间错位、OBB 回归问题、遥感常见问题（p.5，1.3节(1)）。
2.  **提出对现有定向目标检测方法的系统分类体系（Taxonomy）**，从检测框架、OBB 回归技术、特征表示方法、常见问题解决方案四个维度组织现有方法（p.5，1.3节(2)；结构化分类见 p.9 图5）。
3.  **在典型数据集上对 SOTA 方法做全面对比**，并深入分析这些方法的优劣，旨在为方法的选择与改进提供有价值的见解（p.5，1.3节(3)；具体对比在第8节）。
4.  **梳理开放性问题并展望未来方向**：轻量化方法、场景特定数据集、多模态数据集、大规模数据集，以及多模态大模型（p.5，1.3节(4)）。
## 方法

**重要说明**：本文是一篇综述，**并未提出全新的检测方法或框架**。其“方法”核心在于**对现有方法的系统分类、分析与总结**。论文章节结构（p.5）：第2节 水平→定向的演进与挑战；第3节 检测框架；第4节 OBB 回归技术；第5节 特征表示方法；第6节 遥感常见问题的解决方案；第7节 数据集概览；第8节 SOTA 对比分析；第9节 结论与未来方向。
- **整体逻辑**：“提出挑战 → 分类解决挑战的方法”。图5（p.9）给出结构化分类体系。
- **分类体系详解**：
    1.  **检测框架（第3节）**：分为四类——
        - **两阶段方法（two-stage，3.1节）**：以“粗到精（coarse-to-fine）”范式工作，先生成旋转候选区域、再分类与精修；常用旋转候选生成网络或改进的标签分配缓解特征/空间错位。
        - **单阶段方法（one-stage）**：一步完成分类与回归，效率高但精度相对较低（提取文本 p.8 原文表述：单阶段“high efficiency but poor accuracy”）。常配合精修头（refined head，3.2节，如 R3Det、S2A-Net）做特征对齐。
        - **无锚点方法（anchor-free，3.3节）**：不依赖预定义锚点直接检测物体，从根本上规避锚点带来的空间错位；据补读线索（p.13-14）进一步含基于关键点（keypoint-based）与基于中心点（center-based，多概率热图）两类。
        - **DETR类方法（3.4节）**：把检测视为集合预测（set prediction）任务，借助 Transformer 去除 NMS、锚点等手工组件，为定向检测提供端到端新范式。
    2.  **OBB 回归技术（第4节）**：针对旋转框参数化带来的训练难题——
        - **损失函数设计（4.1节）**：设计新损失缓解角度周期性（PoA）或顶点排序问题。
        - **OBB 表示方法（4.2节）**：探索 θ-based 与四边形之外的新参数化方式；据补读线索，第4节末以 Table 2 总结各类 OBB 表示方法的优劣（p.19-20）。
    3.  **特征表示方法（第5节）**：
        - **旋转不变特征表示（5.1节）**：通过特定模块/变换使特征对旋转不敏感。
        - **高级特征表示（5.2节）**：用注意力、FPN 等增强对多尺度、复杂背景、弱纹理目标的表达；补读线索提到 ARC（以数据相关方式捕捉物体旋转信息，p.22）等代表工作，并讨论纯 CNN 与 ViT 的对比（p.23）。
    4.  **遥感常见问题的解决方案（第6节）**：处理尺度变化、复杂背景、弱特征响应等遥感特有挑战；补读线索提到 SCRDet（Yang et al. 2019，p.25-26）等改善定位精度与正样本筛选的工作。
- **与已有综述的差异**：相比聚焦通用检测、其他领域（文本/行人/小样本/小目标）、水平遥感检测、或仅覆盖有限旋转模型的前作（Zhang et al. 2023 只简要介绍 OBB 表示与旋转不敏感特征；Wen et al. 2023 仅描述既有定向方法细节），本文系统而全面地综述该领域，提供更深入的分析、更优的文献分类，并讨论当前挑战、对比与未来方向（p.3-4，1.1节；Table 1 汇总了 14 篇相关综述）。
## 实验

作为综述，本文**没有提出新方法做实验**，而是汇总该领域的数据集、协议与 SOTA 对比：
- **数据集与评估协议**：第7节概述常用公开数据集与评估协议（摘要与 p.5 章节安排均提及）。**具体数据集列表与指标（如 mAP、AP75 等）落在第7-8节，超出提取缓存覆盖的前12页，提取文本未明确列出**（补读线索 p.15 出现 "AP75" 这一更严格指标的讨论，据原文后续页，提取缓存未覆盖具体数值，待核）。
- **SOTA 对比与主结果**：第8节做全面对比与优劣分析（p.5）。**第8节的具体对比表格、方法列表与关键性能数字落在提取缓存（前12页/至 p.9）之外，提取文本未找到**；据原文后续页补读线索，第4节 OBB 表示对比见 Table 2（p.19-20），但本笔记不复述其中具体数值（提取缓存未覆盖，待核）。
- **消融/泛化/效率信息**：综述会汇总各代表方法的实验发现，但这些细节同样不在提取缓存覆盖的前12页内，提取文本未明确。
## 局限

1.  **领域聚焦**：本文明确聚焦**光学遥感图像**中、且**针对单幅图像**的定向目标检测（p.5 范围一节明确 "restrict our attention to oriented object detection methods for single images"）。其结论与分类体系是否适用于 SAR 图像、无人机视频、自然场景文本等其他旋转目标场景，需读者自行判断。
2.  **时效性**：综述发表必然滞后于最新进展。本文 2025 年5月录用，但该领域发展迅速，作者亦在范围一节坦言论文爆发式增长“无法尽览”、只能筛选顶刊顶会的有影响力工作，故对未入选工作致歉（p.4-5）——部分最新突破可能未被涵盖。
3.  **广度与深度的权衡**：面对海量文献，综述不得不在广度与深度间取舍；对某一具体被引方法，其核心细节仍需读原文。
4.  **主观性**：分类体系的划分、重要论文的筛选、优劣的评判，都不可避免带有作者视角与判断。
## 个人评论

这篇综述的最大价值在于其**系统性梳理与结构化思考**。对研究者的启发：
1.  **清晰的问题定义**：把定向检测的挑战明确拆成“特征错位 / 空间错位 / OBB 回归 / 遥感常见问题”四维，并将每类挑战与对应解决方案的章节一一映射（3.1/3.2 治特征错位、3.1/3.3 治空间错位、4.1/4.2 治回归、5 治特征、6 治常见问题），为理解问题、定位研究空白提供了清晰路线图。
2.  **方法论地图**：四维分类体系（框架 / 回归 / 特征 / 常见问题）像一张“技术树地图”，便于快速判断自己的工作（改进既有方法或提新方法）在领域中的位置。
3.  **研究起点**：Table 1 对 14 篇相关综述的定位、以及正文对经典方法（R3Det、S2A-Net、SCRDet、ARC 等）的串联，是高效进入该子领域的入口。
4.  **批判性视角**：对各方法优劣的分析与未来方向（轻量化、场景/多模态/大规模数据集、多模态大模型）的展望，有助激发新思路。

### 使用建议

- **快速了解领域**：重点读 **Abstract、第1节（引言）、第2节（水平→定向的挑战）、图5（分类体系）**，可在短时间内建立框架性认识。
- **若要复现某个具体方法**：本文不能直接复现；应据其分类与引用找到原始论文作为复现依据。
- **若要借鉴创新点**：重点学第2节对挑战的归纳与第3-6节的解决方案论述，思考能否针对某个未解决挑战提出新模块或策略。
- **撰写 Related Work**：若你的论文属定向目标检测领域，可把本文的四维分类体系作为组织相关工作的骨架，并引用本文作为领域综述的代表。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C_目标检测_通用与旋转框]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇关于**光学遥感图像中定向（旋转）目标检测**的综述（Survey），刊于 *Artificial Intelligence Review* (2025) 58:350，2025年5月录用，正文 61 页。它属于计算机视觉（CV）目标检测下的**旋转框检测**方向、专注遥感（RS）场景，系统回顾、分类并分析近年基于深度学习的定向目标检测方法的进展、挑战与未来方向。归类于 **“C_目标检测_通用与旋转框”** 主题恰当。

## 2. 一句话总结
本文系统综述基于深度学习的光学遥感定向目标检测，将该任务的核心挑战归纳为特征错位、空间错位、OBB 回归问题与遥感常见问题四类，并据“检测框架 / OBB 回归技术 / 特征表示 / 常见问题解决方案”四维分类体系组织现有方法，配合数据集梳理、SOTA 对比与未来方向展望。

## 3. 背景与问题
- **为什么要做**：遥感技术（光学卫星、无人机）让海量、多分辨率、多光谱图像唾手可得，自动分析需求迫切。目标检测是自动分析遥感图像的关键基础，应用于智能监控、精准农业、城市规划、港口管理、军事侦察等。遥感图像多为鸟瞰视角，物体任意朝向，通用水平检测器力不从心，故需用旋转框（OBB）紧贴物体——既给朝向又精定位（p.1-2，图1）。
- **之前方法的问题**：
    1.  **水平框（HBB）的局限**：（1）密集场景、大长宽比物体上相邻 HBB 间 IoU 过大（图1b），NMS 易漏检；（2）HBB 含大量背景、定位不精，OBB 则能紧贴物体（图1a）（p.6）。
    2.  **改造为定向检测引入的额外挑战**（p.6-8）：
        - **特征错位**：轴对齐卷积提取的特征与旋转物体错位（图3a），缺旋转信息，难以精确回归 OBB；
        - **空间错位**：水平锚点与旋转物体 IoU 很小（图4a），按 IoU 分配正负样本难以提供足够正样本；
        - **OBB 回归问题**：θ-based 存在角度周期性（PoA）——角度逼近边界时微小角差引起损失剧变、边界不连续；四边形表示面临顶点排序、易致预测与 GT 顶点序列不一致；两者都引起训练不稳定（细节见原文附录 A、B 节）。
- **核心矛盾**：在化解特征错位、空间错位、OBB 回归三大难题的同时，克服遥感固有的尺度变化、复杂背景、弱特征响应。

## 4. 核心贡献
据 1.3 节（p.5），四点贡献：
1.  全面回顾水平→定向的技术演进，并把主要挑战归纳为四类（特征错位、空间错位、OBB 回归、遥感常见问题）。
2.  提出对现有方法的系统分类体系：检测框架、OBB 回归技术、特征表示方法、常见问题解决方案（图5，p.9）。
3.  在典型数据集上对 SOTA 方法做全面对比并分析优劣（第8节）。
4.  梳理开放问题与未来方向：轻量化方法、场景特定数据集、多模态数据集、大规模数据集、多模态大模型。

## 5. 方法详解
**说明**：综述本身不提新方法，核心是对现有方法的分类、分析与总结。章节结构：第2节挑战、第3节框架、第4节 OBB 回归、第5节特征表示、第6节遥感常见问题、第7节数据集、第8节 SOTA 对比、第9节结论与未来方向（p.5）。
- **检测框架（第3节）**，四类：
    - **两阶段**：粗到精，旋转候选生成 + 精修；缓解特征/空间错位（3.1）。
    - **单阶段**：一步分类+回归，效率高、精度相对低（原文 p.8 表述）；常配精修头（3.2，如 R3Det、S2A-Net 用额外精修头做特征对齐，据补读线索 p.13）。
    - **无锚点（3.3）**：不依赖锚点，规避空间错位；含关键点法与中心点法（多概率热图，补读线索 p.13-14）。
    - **DETR类（3.4）**：集合预测，去 NMS/锚点等手工组件，端到端。
- **OBB 回归技术（第4节）**：损失函数设计（4.1，缓解 PoA / 顶点排序）+ OBB 表示方法（4.2，超越 θ-based 与四边形；据补读线索以 Table 2 总结各表示法优劣，p.19-20）。
- **特征表示（第5节）**：旋转不变特征（5.1）+ 高级特征（5.2，注意力/FPN 等；补读线索提及 ARC 以数据相关方式捕捉旋转信息 p.22、纯 CNN 与 ViT 之争 p.23）。
- **遥感常见问题（第6节）**：尺度变化、复杂背景、弱特征响应（补读线索提及 SCRDet 等，p.25-26）。
- **与已有综述差异**：相比 Zhang et al. 2023（仅简要介绍 OBB 表示与旋转不敏感特征）与 Wen et al. 2023（仅描述既有方法细节），本文更深更全、分类更优，并讨论挑战/对比/未来（p.3-4；Table 1 汇总 14 篇相关综述）。

## 6. 实验与结果
作为综述，本文不做新方法实验，但汇总数据集、协议与 SOTA 对比：
- **数据集与协议（第7节）**：摘要明确“covers several publicly available datasets and evaluation protocols”。**具体数据集列表与指标落在第7-8节，超出提取缓存（前12页），提取文本未明确列出**；补读线索 p.15 出现更严格指标 AP75 的讨论（据原文后续页，提取缓存未覆盖具体数值，待核）。
- **SOTA 对比（第8节）**：在典型数据集上全面对比并分析优劣（p.5）。**第8节对比表格、方法列表、关键性能数字超出提取缓存覆盖范围，提取文本未找到**；第4节 OBB 表示对比据补读线索见 Table 2（p.19-20），本笔记不复述其数值（提取缓存未覆盖，待核）。
- **效率/消融**：综述汇总各代表方法的实验发现，细节同样不在前12页提取范围内，提取文本未明确。

## 7. 这篇论文真正有价值的地方
1.  **清晰的问题定义**：四维挑战拆解（特征错位/空间错位/OBB 回归/遥感常见问题），并把每类挑战映射到具体章节的解决方案，给出研究路线图。
2.  **方法论地图**：四维分类体系帮助快速判断自身工作在技术树中的位置。
3.  **研究起点**：Table 1（14 篇相关综述对位）+ 正文对 R3Det、S2A-Net、SCRDet、ARC 等经典方法的串联，是进入该子领域的高效入口。
4.  **批判性视角**：对各法优劣的分析与未来方向（轻量化、场景/多模态/大规模数据集、多模态大模型）的展望，利于激发新思路。

## 8. 局限与问题
1.  **领域聚焦**：仅针对光学遥感、且单幅图像的定向检测（原文范围一节明确 single images）；对 SAR、无人机视频、场景文本等是否适用需读者自判。
2.  **时效性**：2025年5月录用，作者自陈论文爆发式增长无法尽览、只筛顶刊顶会有影响力工作（p.4-5），部分最新突破可能未涵盖。
3.  **广度/深度权衡**：具体被引方法的核心细节仍需读原文。
4.  **主观性**：分类划分、论文筛选、优劣评判带作者视角。

## 9. 我该怎么使用这篇论文
- **快速了解领域**：读 Abstract、第1节、第2节、图5（分类体系）。
- **复现具体方法**：本文不能直接复现，据其分类与引用找原始论文。
- **借鉴创新点**：学第2节挑战归纳与第3-6节解决方案，针对未解决挑战提新模块/策略。
- **写 Related Work**：以本文四维分类体系为骨架组织相关工作，并引用本文作为领域综述代表。

## 10. 和其他论文的关系
作为定向（旋转）目标检测的综合性综述，本文与本库中所有旋转目标检测论文构成“综述—具体研究”关系：
- 与其他旋转检测综述形成对照（本文 Table 1 已对位 Zhang et al. 2023、Wen et al. 2023 等 14 篇相关综述）。
- 与文中重点串联的经典方法（如 R3Det、S2A-Net、SCRDet、ARC 等）构成“综述—被综述方法”关系。
- 与遥感图像通用目标检测综述互补。
（注：具体可链接的库内笔记需以实际存在的文件名为准，此处不臆造链接。）

## 11. 关键词
定向目标检测, 旋转目标检测, 遥感图像, 深度学习, 旋转框（OBB）, 综述, 特征错位, 空间错位, OBB 回归, 角度周期性（PoA）, 顶点排序, 检测框架, 特征表示, 两阶段/单阶段/无锚点/DETR

## 12. 可信度说明
本精读笔记基于提取缓存（前12页/共61页）生成。提取文本质量良好，清晰覆盖标题、作者、摘要、引言、与相关综述的对比（Table 1）、研究范围、四点贡献、水平→定向的演进与三大挑战、以及第3节检测框架分类的开头。
- **可据提取文本核实的内容**：论文定位、背景问题、四维挑战、四维分类体系、四点贡献、章节结构、Table 1 综述对位、R3Det 特征对齐（图3b）、θ-based/四边形表示的 PoA 与顶点排序问题等，均直接来自提取文本前12页。
- **依赖原文后续页/补读线索、提取缓存未覆盖的内容**：第4节 OBB 表示对比 Table 2（p.19-20）、AP75 讨论（p.15）、ARC（p.22）、纯 CNN vs ViT（p.23）、SCRDet（p.25-26）等，均来自补读阶段记录的“章节线索/关键摘录”，**具体数值与完整论述未进入提取缓存，已标注“据原文后续页，提取缓存未覆盖，待核”**。第7节数据集清单、第8节 SOTA 对比的方法列表与性能数字在前12页提取文本中未出现。
- 想获取全部方法细节与实验结果，须阅读完整 PDF 原文。

---

> **可信度补充**: PDF 提取质量 = **high** (提取缓存前12页质量好, 约2086 字符/页; 补读线索覆盖 p.13-61); 来源缓存: `.paper-cache/extracts/2023_Oriented_object_dete.txt` (提取缓存 12/61 页; 原 AI 主体 12/61 + 全文补读 13-61); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-61; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-61。
- **提取情况**: 缺失页 49 页, 其中 49 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Both R3Det and S2A-Net utilize an extra refined head for feature alignment, making
- p.13: 3.3 Anchor-free detectors
- p.13: The above two categories follow the anchor paradigm, which suffers from spatial misalign -
- p.13: Keypoint-based methods first locate a set of adaptive or self-constrained keypoints and
- p.13: The convex hull, which is represented by irregular sample points, is refined using a convex
- p.14: Center-based methods typically generate multiple probabilistic heatmaps and a series of
- p.14: Hence, an effective scheme for increasing the performance of such an approach is to
- p.14: In contrast with the above two methods, which capitalize on the merits of anchor-free
- p.15: 3.4 DETR-based detectors
- p.15: In addition to the above convolution-based methods, DETR-based detectors, including
- p.15: 3.5 Discussion
- p.15: Feature misalignment and spatial misalignment severely impair the performance of ori -

### 缺失页关键摘录

- p.15: et al. 2022 ), resulting in dramatic breakthroughs in terms of accuracy and convergence
- p.15: it achieves greater detection accuracy in terms of a more rigorous metric (i.e., AP75), but
- p.16: choice for the regression task may not guarantee high localization accuracy in terms of
- p.19: and disadvantages of the above OBB representation methods are summarized in Table 2.
- p.20: Table 2 Comparison among different OBB representation methods
- p.21: localization and classification tasks. As a result, the most recent improvements in detec -
- p.21: tion accuracy have been attained via research conducted on enhancing feature representa -
- p.22: a data-dependent manner. As a result, ARC can capture the rotation information of objects
- p.22: corresponding discussion will be brief in this context.
- p.23: 2021 ) and demonstrated that pure CNNs outperform ViTs in terms of accuracy and robust -
- p.25: Oriented object detection in optical remote sensing images using deep…improving their object localization accuracy. In addition, SCRDet (Yang et al. 2019 ) adopts
- p.26: the evaluation criteria for screening positive samples. This scheme can push detectors to
<!-- AI_READING_NOTE_END -->
