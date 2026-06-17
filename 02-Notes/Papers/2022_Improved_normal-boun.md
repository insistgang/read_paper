---
title: "Improved normal-boundary intersection algorithm: a method for energy optimization"
authors:
  - "Jia Cui"
  - "Jiang Pan"
  - "Shunjiang Wang"
  - "Martin Onyeka Okoye"
  - "Junyou Yang"
  - "Yang Li"
  - "Hao Wang"
year: 2022
venue: "Building and Environment"
doi: 10.1016/j.buildenv.2022.108846
pdf: [[2022_Improved_normal-boun.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
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
extract_cache: .paper-cache/extracts/2022_Improved_normal-boun.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/24 pages"
---
# Improved normal-boundary intersection algorithm: a method for energy optimization

## 基本信息
- **PDF**: [[2022_Improved_normal-boun.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Improved normal-boundary intersection algorithm: a method for energy optimization |
| **作者** | Jia Cui; Jiang Pan; Shunjiang Wang; Martin Onyeka Okoye; Junyou Yang; Yang Li; Hao Wang |
| **发表时间** | 2022 |
| **刊物/会议** | Building and Environment |
| **DOI** | 10.1016/j.buildenv.2022.108846 |

## 摘要

> With the widespread use of distributed energy sources, the advantages of smart buildings over traditional buildings are becoming increasingly obvious. Subsequently, its energy optimal scheduling and multi-objective optimization have become more and more complex and need to be solved urgently. This paper presents a novel method to optimize energy utilization in smart buildings. Firstly, multiple transfer- retention ratio (TRR) parameters are added to the evaluation of distributed renewable energy. Secondly, the normal-boundary intersection (NBI) algorithm is improved by the adaptive weight sum, the adjust uniform axes method, and Mahalanobis distance to form the improved normal-boundary intersection (INBI) algorithm. The multi-objective optimization problem in smart buildings is solved by the parameter TRR and INBI algorithm to improve the regulation efficiency. In response to the needs of decision-makers with evaluation indicators, the average deviation is reduced by 60% compared with 

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：随着分布式能源的广泛应用，智能建筑的优势日益明显，其能源优化调度和多目标优化问题变得复杂且亟待解决（p.1, p.3）。
- **之前方法有什么问题**：
    1.  现有研究在分析智能建筑时，未充分考虑风/光关联性、负荷不确定性和电气连接对控制的影响（p.3）。
    2.  用于求解多目标优化问题的NBI算法和调整均匀轴法（AUAM）在处理复杂多维问题时，难以获得分布广泛且均匀的帕累托前沿，且其前沿不够接近真实帕累托前沿（p.4）。
- **作者想解决的核心矛盾**：如何提出一个更优的多目标优化算法和更全面的评价指标，以生成分布更广、更均匀的帕累托前沿，从而为智能建筑群找到兼顾设备成本、供电成本和用户舒适度的能源优化调度方案。
## 关键贡献

根据论文引言部分明确列出的贡献（p.4）：
1.  **首次提出了建筑调控评价指标 TRR**：该指标（转移-保留率）考虑了风力发电和光伏发电的电气连接的综合效应以及负荷的不确定性，使得对分布式能源系统的评价更具解释性。
2.  **提出了基于改进NBI算法的优化算法 INBI**：该算法集成了三种改进：
    a. 基于自适应权值和（AWS）算法，增加了跨维度的可行解。
    b. 利用调整均匀轴法（AUAM）解决帕累托前沿分布广泛且均匀的问题。
    c. 利用马氏距离双基点法替代原始NBI中的距离方法，进一步使帕累托前沿分布广泛且均匀。
## 方法

本文的核心方法是**改进的常规边界交集算法（INBI）**，用于求解智能建筑能源系统的多目标优化问题。
- **整体框架**：INBI算法的流程如图4所示（p.10）。首先使用原始NBI算法构建三维帕累托前沿；然后分别对三个二维帕累托前沿应用AWS算法进行修正并保留所有修正点；将这些点通过映射方法合并到三维帕累托前沿中；接着使用AUAM算法判断可行解以获取非劣解；最后通过马氏距离双基点法获得妥协解。
- **输入输出**：
    - **输入**：智能建筑系统模型参数（各类负荷、发电单元、成本模型、约束条件等）。
    - **输出**：多目标优化问题的妥协解，即一组在设备成本、供电成本和用户舒适度之间达到较好平衡的决策方案。
- **关键模块**：
    1.  **TRR 参数模型**：用于评价分布式可再生能源的调节能力。公式(5)和(6)定义了光伏和风力的TRR参数（α, β），其值每15分钟记录一次（p.6）。公式(9)将TRR约束集成到优化问题中（p.7）。
    2.  **自适应权值和（AWS）算法**：用于增加可行解数量。在AWS修正过程中，一个初始点会被扩展为多个点，从而增加解的多样性，避免同质化（p.7, p.10）。
    3.  **调整均匀轴法（AUAM）**：用于解决帕累托前沿分布不广不均匀的问题。通过基于最优筛选步长来优化筛选精度（p.8）。在INBI中，AUAM需要适应AWS产生的多个步长。
    4.  **马氏距离双基点法**：替代原始NBI算法中的欧氏距离。该方法基于权重对角矩阵修正正理想点和负理想点，考虑了评价指标之间的相关性，避免信息重叠影响决策结果，被认为比其他复杂距离函数更简单、实用、全面且准确（p.8）。
- **数学公式或机制的直观解释**：优化目标包含三个：设备成本（风力、光伏发电的安装维护成本，公式(1)）、供电成本（分时电价，公式(2)）、用户舒适度（基于室内温度，公式(3)）。INBI算法的目标是找到一个“妥协解”，使得这三个目标尽可能地都得到优化。
- **与已有方法的差异**：相比原始NBI算法，INBI通过AWS增加了可行解的多样性，通过AUAM改善了帕累托前沿的分布质量，通过马氏距离改进了解的筛选准则。整体目标是获得更广泛、均匀且更接近真实前沿的帕累托解集。
## 实验

**PDF文本中未明确说明**。提供的文本（前12页）包含了方法的描述和部分模型，但具体的实验设置、数据集、对比方法和详细结果数据未在提取范围内。论文摘要中声称：
- 平均偏差比之前情况降低了60%。
- 数值例子表明，所提方法在三个优化目标上优于现有技术：设备成本降低8.2%，供电成本降低7.6%，用户舒适度提高1.6%。
（注：这些数字来源于摘要p.1，但具体的实验场景、数据集和对比方法在提供的文本中未找到。）
## 局限

1.  **方法复杂度**：INBI算法集成了多种改进（AWS、AUAM、马氏距离），虽然可能提升解的质量，但也增加了算法的复杂度和计算开销（文中图3, 4讨论了复杂度增加）。
2.  **实验验证不足**：根据提供的文本，无法评估其在何种规模的建筑群、何种数据条件下进行了验证。其声称的优越性能（如成本降低8.2%）需要看具体的对比实验是否公平、充分。
3.  **假设依赖**：模型依赖于特定的成本公式（如分时电价）、舒适度公式以及对负荷、发电的预测精度。这些公式在不同地区和应用场景下可能需要调整。
4.  **复现风险**：TRR参数公式(5)(6)较为复杂，其物理意义和参数（γ_l, ρ_b）的确定需要仔细查阅原文后续部分。INBI算法流程步骤较多，复现时需仔细对照流程图和公式。
## 个人评论

1.  **问题定义与建模的启发**：论文将智能建筑群能源优化问题清晰地定义为一个多目标优化问题，并提出了一个综合考虑技术、经济与人因（舒适度）的框架。其建模思路（如成本模型、舒适度模型、功率平衡约束）对类似能源系统问题有参考价值。
2.  **算法改进思路的启发**：对于NBI这类经典多目标优化算法，本文展示了一套系统的改进流程：通过AWS增加解的多样性 -> 通过AUAM改善前沿分布 -> 通过更好的距离度量（马氏距离）改进解的筛选。这种“诊断问题 -> 多模块组合改进”的思路值得学习。
3.  **引入新评价指标的尝试**：提出TRR指标来量化和约束可再生能源的协同调度能力，这是一个将系统运行特性（风光关联、不确定性）转化为优化问题约束/目标的创新尝试。

### 使用建议

- **如果快速了解**：重点阅读**摘要**（p.1）、**引言**的贡献总结部分（p.4）以及**图3和图4**（p.8, p.10），可以快速掌握论文提出的问题、核心贡献和算法框架。
- **如果复现**：需要精读**第2节**（系统模型、成本、舒适度、约束的具体公式）和**第3节**（INBI算法的每一步，特别是AWS、AUAM和马氏距离的具体实现）。公式(1)-(10)是关键。
- **如果借鉴创新点**：
    - 借鉴**TRR指标**的思路，为自己的研究问题设计一个考虑系统内部关联性的新评价指标。
    - 借鉴**INBI的改进框架**，思考如何将“增加解多样性”、“改善前沿分布”、“改进筛选标准”这三个步骤应用到自己使用的其他多目标优化算法中。
- **如果写 Related Work**：可将其放在“**智能建筑能源管理**”、“**多目标优化算法在能源系统中的应用**”、“**NBI算法及其改进**”这些类别下。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**智能建筑能源管理与多目标优化算法**方向。它主要研究智能建筑群中分布式可再生能源（风、光）与各类负荷的多目标优化调度问题。论文提出了一种改进的优化算法（INBI）和新的评估指标（TRR），以解决设备成本、供电成本和用户舒适度之间的权衡问题。基于文件名的分类主题“T_通用_NLP_其他”，本文内容与自然语言处理无直接关联，更应归入能源系统、智能电网或运筹优化领域。

## 2. 一句话总结
本文提出了一种改进的常规边界交集（INBI）算法和转移-保留率（TRR）指标，用于解决智能建筑中考虑风光关联、负荷不确定性和电气连接的多目标能源优化问题。

## 3. 背景与问题
- **这篇论文为什么要做**：随着分布式能源的广泛应用，智能建筑的优势日益明显，其能源优化调度和多目标优化问题变得复杂且亟待解决（p.1, p.3）。
- **之前方法有什么问题**：
    1.  现有研究在分析智能建筑时，未充分考虑风/光关联性、负荷不确定性和电气连接对控制的影响（p.3）。
    2.  用于求解多目标优化问题的NBI算法和调整均匀轴法（AUAM）在处理复杂多维问题时，难以获得分布广泛且均匀的帕累托前沿，且其前沿不够接近真实帕累托前沿（p.4）。
- **作者想解决的核心矛盾**：如何提出一个更优的多目标优化算法和更全面的评价指标，以生成分布更广、更均匀的帕累托前沿，从而为智能建筑群找到兼顾设备成本、供电成本和用户舒适度的能源优化调度方案。

## 4. 核心贡献
根据论文引言部分明确列出的贡献（p.4）：
1.  **首次提出了建筑调控评价指标 TRR**：该指标（转移-保留率）考虑了风力发电和光伏发电的电气连接的综合效应以及负荷的不确定性，使得对分布式能源系统的评价更具解释性。
2.  **提出了基于改进NBI算法的优化算法 INBI**：该算法集成了三种改进：
    a. 基于自适应权值和（AWS）算法，增加了跨维度的可行解。
    b. 利用调整均匀轴法（AUAM）解决帕累托前沿分布广泛且均匀的问题。
    c. 利用马氏距离双基点法替代原始NBI中的距离方法，进一步使帕累托前沿分布广泛且均匀。

## 5. 方法详解
本文的核心方法是**改进的常规边界交集算法（INBI）**，用于求解智能建筑能源系统的多目标优化问题。
- **整体框架**：INBI算法的流程如图4所示（p.10）。首先使用原始NBI算法构建三维帕累托前沿；然后分别对三个二维帕累托前沿应用AWS算法进行修正并保留所有修正点；将这些点通过映射方法合并到三维帕累托前沿中；接着使用AUAM算法判断可行解以获取非劣解；最后通过马氏距离双基点法获得妥协解。
- **输入输出**：
    - **输入**：智能建筑系统模型参数（各类负荷、发电单元、成本模型、约束条件等）。
    - **输出**：多目标优化问题的妥协解，即一组在设备成本、供电成本和用户舒适度之间达到较好平衡的决策方案。
- **关键模块**：
    1.  **TRR 参数模型**：用于评价分布式可再生能源的调节能力。公式(5)和(6)定义了光伏和风力的TRR参数（α, β），其值每15分钟记录一次（p.6）。公式(9)将TRR约束集成到优化问题中（p.7）。
    2.  **自适应权值和（AWS）算法**：用于增加可行解数量。在AWS修正过程中，一个初始点会被扩展为多个点，从而增加解的多样性，避免同质化（p.7, p.10）。
    3.  **调整均匀轴法（AUAM）**：用于解决帕累托前沿分布不广不均匀的问题。通过基于最优筛选步长来优化筛选精度（p.8）。在INBI中，AUAM需要适应AWS产生的多个步长。
    4.  **马氏距离双基点法**：替代原始NBI算法中的欧氏距离。该方法基于权重对角矩阵修正正理想点和负理想点，考虑了评价指标之间的相关性，避免信息重叠影响决策结果，被认为比其他复杂距离函数更简单、实用、全面且准确（p.8）。
- **数学公式或机制的直观解释**：优化目标包含三个：设备成本（风力、光伏发电的安装维护成本，公式(1)）、供电成本（分时电价，公式(2)）、用户舒适度（基于室内温度，公式(3)）。INBI算法的目标是找到一个“妥协解”，使得这三个目标尽可能地都得到优化。
- **与已有方法的差异**：相比原始NBI算法，INBI通过AWS增加了可行解的多样性，通过AUAM改善了帕累托前沿的分布质量，通过马氏距离改进了解的筛选准则。整体目标是获得更广泛、均匀且更接近真实前沿的帕累托解集。

## 6. 实验与结果
**PDF文本中未明确说明**。提供的文本（前12页）包含了方法的描述和部分模型，但具体的实验设置、数据集、对比方法和详细结果数据未在提取范围内。论文摘要中声称：
- 平均偏差比之前情况降低了60%。
- 数值例子表明，所提方法在三个优化目标上优于现有技术：设备成本降低8.2%，供电成本降低7.6%，用户舒适度提高1.6%。
（注：这些数字来源于摘要p.1，但具体的实验场景、数据集和对比方法在提供的文本中未找到。）

## 7. 这篇论文真正有价值的地方
1.  **问题定义与建模的启发**：论文将智能建筑群能源优化问题清晰地定义为一个多目标优化问题，并提出了一个综合考虑技术、经济与人因（舒适度）的框架。其建模思路（如成本模型、舒适度模型、功率平衡约束）对类似能源系统问题有参考价值。
2.  **算法改进思路的启发**：对于NBI这类经典多目标优化算法，本文展示了一套系统的改进流程：通过AWS增加解的多样性 -> 通过AUAM改善前沿分布 -> 通过更好的距离度量（马氏距离）改进解的筛选。这种“诊断问题 -> 多模块组合改进”的思路值得学习。
3.  **引入新评价指标的尝试**：提出TRR指标来量化和约束可再生能源的协同调度能力，这是一个将系统运行特性（风光关联、不确定性）转化为优化问题约束/目标的创新尝试。

## 8. 局限与问题
1.  **方法复杂度**：INBI算法集成了多种改进（AWS、AUAM、马氏距离），虽然可能提升解的质量，但也增加了算法的复杂度和计算开销（文中图3, 4讨论了复杂度增加）。
2.  **实验验证不足**：根据提供的文本，无法评估其在何种规模的建筑群、何种数据条件下进行了验证。其声称的优越性能（如成本降低8.2%）需要看具体的对比实验是否公平、充分。
3.  **假设依赖**：模型依赖于特定的成本公式（如分时电价）、舒适度公式以及对负荷、发电的预测精度。这些公式在不同地区和应用场景下可能需要调整。
4.  **复现风险**：TRR参数公式(5)(6)较为复杂，其物理意义和参数（γ_l, ρ_b）的确定需要仔细查阅原文后续部分。INBI算法流程步骤较多，复现时需仔细对照流程图和公式。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**摘要**（p.1）、**引言**的贡献总结部分（p.4）以及**图3和图4**（p.8, p.10），可以快速掌握论文提出的问题、核心贡献和算法框架。
- **如果复现**：需要精读**第2节**（系统模型、成本、舒适度、约束的具体公式）和**第3节**（INBI算法的每一步，特别是AWS、AUAM和马氏距离的具体实现）。公式(1)-(10)是关键。
- **如果借鉴创新点**：
    - 借鉴**TRR指标**的思路，为自己的研究问题设计一个考虑系统内部关联性的新评价指标。
    - 借鉴**INBI的改进框架**，思考如何将“增加解多样性”、“改善前沿分布”、“改进筛选标准”这三个步骤应用到自己使用的其他多目标优化算法中。
- **如果写 Related Work**：可将其放在“**智能建筑能源管理**”、“**多目标优化算法在能源系统中的应用**”、“**NBI算法及其改进**”这些类别下。

## 10. 和其他论文的关系
根据提供的主题标签“T_通用_NLP_其他”和文件名，本文与自然语言处理无直接关联。论文内容主要涉及优化算法和能源系统，因此可能相关的论文是：
- 其他关于**智能建筑、微电网、综合能源系统**多目标优化的研究。
- 其他对**NBI算法、NSGA-II、MOEA/D**等多目标进化算法进行改进的研究。
- 由于主题分类限制，在当前库中可能没有直接相关的 `[[双链]]` 论文。

## 11. 关键词
智能建筑 (Smart Building), 可再生能源调度 (Renewable Energy Dispatch), 多目标优化 (Multi-objective Optimization), 常规边界交集算法 (Normal-boundary Intersection Algorithm), 改进的NBI算法 (Improved NBI Algorithm), 转移-保留率 (Transfer-retention Ratio), 自适应权值和 (Adaptive Weight Sum), 调整均匀轴法 (Adjust Uniform Axes Method), 马氏距离 (Mahalanobis Distance), 帕累托前沿 (Pareto Frontier), 设备成本 (Equipment Cost), 用户舒适度 (Occupants' Comfort)

## 12. 可信度说明
本精读笔记**严格基于用户提供的PDF提取文本（前12页，共24页）生成**。笔记中所有具体描述、公式引用、图表引用均来自该文本，并标注了大致页码（p.X）。由于提供的文本不完整，**实验部分（第4节及之后）和完整的数学公式推导、算法细节在提取文本中缺失**，因此相关内容在笔记中明确标注为“PDF文本中未明确说明”。笔记中的分析（如局限与问题）部分基于已提供文本中的方法描述进行合理推断，而非论文原文陈述。整体上，对于论文的核心思想、问题背景、贡献和主要方法框架，本笔记具有较高的可信度；对于实验验证和部分技术细节，则信息不完整。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2022_Improved_normal-boun.txt` (24/24 页; 原 AI 主体 12/24 + 全文补读 13-24); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-24; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-24。
- **提取情况**: 缺失页 12 页, 其中 12 页提取到可读文本。缺失页包含正文/附录内容, 其中约 3 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Based on AUAM, the problem of a wide and uniform Pareto frontier is solved to optimize the
- p.13: 3.5 The compromise solution obtained by the Mahalanobis distance double base point method
- p.13: In the original NBI algorithm, the Euclidean distance double base point method is used as the Pareto
- p.13: The element
- p.13: T T 1
- p.13: T T 1( ) ( )
- p.14: Considering the influence factors of personal preference, Mahalanobis distance is used instead of
- p.14: 4. Analysis of samples
- p.14: 4.1 Initial data and cases setting
- p.14: In this section, a case study is performed using INBI based on the power grid load data of a region
- p.14: Taking 15 minutes as an observation time interval, a total of 96 observations were made throughout the
- p.14: This algorithm is suitable for the case which includes three or more optimization objectives, and has

### 缺失页关键摘录

- p.13: 1) Establishment of an evaluation matrix .
- p.13: iju of the evaluation matrix U is the normalized value of the
- p.14: Euclidean distance. The traditional evaluation matrix and distance do not consider the correlation. Also,
- p.14: the evaluation criteria. Compared with other complex distance functions, Mahalanobis distance is more
- p.15: coefficients are [ 0.5, 0.25, 0.25]. The details are shown in Table 2.
- p.15: Table 2. Considerations and weight distribution
- p.15: as shown in Figure 7. The power at the supply side, i.e., the load, is also required, as shown in Figure 8.
- p.15: The photovoltaic power and wind pow er are shown in Figure 9. At the same time, to prove the
- p.17: Figure 10 shows the indoor temperature changes after turning -ON the air conditioner in the smart
- p.17: 4.2 Calculation result and analysis of smart building s
- p.17: Table 3. Calculation results without considering weight distribution
- p.18: Table 4. Calculation results considering weight distribution (1)
<!-- AI_READING_NOTE_END -->
