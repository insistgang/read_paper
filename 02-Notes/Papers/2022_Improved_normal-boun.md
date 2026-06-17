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
| **题目** | Improved normal-boundary intersection algorithm: a method for energy optimization strategy in smart buildings |
| **作者** | Jia Cui; Jiang Pan; Shunjiang Wang; Martin Onyeka Okoye; Junyou Yang; Yang Li; Hao Wang |
| **单位** | 沈阳工业大学电气工程学院 / 国网辽宁电力 / 东北电力大学 |
| **发表时间** | 2022 |
| **刊物/会议** | Building and Environment |
| **DOI** | 10.1016/j.buildenv.2022.108846 |

## 摘要

清理后的英文原摘要（据 PDF 提取文本修复空格与连字符断裂）：

> With the widespread use of distributed energy sources, the advantages of smart buildings over traditional buildings are becoming increasingly obvious. Subsequently, its energy optimal scheduling and multi-objective optimization have become more and more complex and need to be solved urgently. This paper presents a novel method to optimize energy utilization in smart buildings. Firstly, multiple transfer-retention ratio (TRR) parameters are added to the evaluation of distributed renewable energy. Secondly, the normal-boundary intersection (NBI) algorithm is improved by the adaptive weight sum, the adjust uniform axes method, and Mahalanobis distance to form the improved normal-boundary intersection (INBI) algorithm. The multi-objective optimization problem in smart buildings is solved by the parameter TRR and INBI algorithm to improve the regulation efficiency. In response to the needs of decision-makers with evaluation indicators, the average deviation is reduced by 60% compared with the previous case. Numerical examples show that the proposed method is superior to the existing technologies in terms of three optimization objectives. The objectives include 8.2% reduction in equipment costs, 7.6% reduction in power supply costs, and 1.6% improvement in occupants' comfort.

中文翻译：

> 随着分布式能源的广泛应用，智能建筑相对传统建筑的优势日益明显，但其能源优化调度与多目标优化问题也变得越来越复杂、亟待解决。本文提出一种优化智能建筑能源利用的新方法。首先，在分布式可再生能源的评价中引入多个"转移-保留率"（TRR）参数；其次，用自适应权值和（AWS）、调整均匀轴法（AUAM）和马氏距离三种手段改进常规边界交集（NBI）算法，构成改进的常规边界交集（INBI）算法。通过 TRR 参数与 INBI 算法求解智能建筑中的多目标优化问题，以提升调控效率。面向决策者对评价指标的需求，平均偏差较原情形降低 60%。数值算例表明，所提方法在三个优化目标上均优于现有技术：设备成本降低 8.2%、供电成本降低 7.6%、用户舒适度提升 1.6%。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **这篇论文为什么要做**：随着分布式能源广泛应用，由多个智能建筑构成的协同体能高效利用可再生能源；智能建筑被定义为配备分布式可再生能源发电设施的新型建筑（p.3，引言 [1]-[6]）。其能源优化与控制的难点在于分布式可再生能源的调控（p.3）。
- **之前方法有什么问题**：
    1.  既有文献（模型预测 [7-9]、可再生发电预测 [10]、基于需求响应的多目标模型 [11-14]）在分析智能建筑时，未充分考虑风/光关联性、负荷不确定性与电气连接对控制的影响（p.3-4）。
    2.  在求解多目标优化方面：粒子群算法 [15,16] 难以求解复杂多目标问题；加权和法 [18]、基于帕累托前沿的方法 [19-21]、用 AUAM 改进 NBI 的方法 [22] 等都存在不足——NBI 与 AUAM 在处理复杂多维问题时难以获得分布广泛且均匀的帕累托前沿，且前沿不够接近真实帕累托前沿（p.4）。
- **作者想解决的核心矛盾**：如何同时给出更全面的评价指标与更优的多目标优化算法，生成分布更广、更均匀、更接近真实前沿的帕累托解集，从而为智能建筑群找到兼顾设备成本、供电成本与用户舒适度的能源优化调度方案。

## 关键贡献

根据论文引言明确列出的两条贡献（p.4）：
1.  **首次提出建筑调控评价指标 TRR（转移-保留率）**：涵盖风、光、空调联合调度系统；它考虑了风电与光伏电气连接的综合效应以及负荷不确定性，使其对分布式能源系统的可解释性更好。
2.  **提出基于 NBI 改进的优化算法 INBI**：集成三项改进：
    a. 改进的自适应权值和（AWS）算法，跨维度增加可行解。
    b. 调整均匀轴法（AUAM），解决帕累托前沿分布广而均匀的问题。
    c. 马氏距离双基点法作为筛选准则，进一步使帕累托前沿分布广泛且均匀。

（提取文本仅列出上述两条编号贡献；TRR 与 INBI 是全文两大支柱。）

## 方法

本文核心方法是**改进的常规边界交集算法（INBI）**，配合 TRR 评价指标，用于求解智能建筑能源系统的多目标优化问题。

- **系统模型（第 2 节）**：智能建筑包含供电侧（电网、风电、光伏）与用电侧（各类负荷），见图 1；图 2 给出各建筑独立配备风/光发电与储能、各建筑储能互联的分布式架构。三个被调控量定义为：设备成本（一个月内所有设备建设与维护总成本）、供电成本（一个月内所有用户负荷的电费）、用户舒适度（一个月内所有住户舒适度均值）（p.4-5）。
- **三个优化目标（公式 1-3）**：
    1.  设备成本 C_w：风电、光伏的安装维护、运行损耗补偿等，公式(1) `C_w = C_l + w1·P0 + w2·Pwm + l·Pc`（p.5）。
    2.  供电成本（分时电价）：公式(2)，谷时 0.3（23:00-06:00）、峰时 0.7（06:00-23:00），为华北地区一般建筑电价标准（p.6）。
    3.  用户舒适度 S_D：公式(3) `S_D = [1 - 2·|6 - 0.25·T_in|]·100%`（基于室内温度，T_in∈[22,30]℃；公式为原文简化的热舒适度定义）（p.6）。
    4.  功率平衡约束：公式(4)，电网交换功率 + 风电 + 光伏 = 可调度负荷 + 关键负荷 + 可切换负荷（p.6）。
- **TRR 参数模型（公式 5-9）**：α、β 分别定义为智能建筑总光伏发电比与总风电发电比，即可再生能源输出与储备之比；每 15 分钟记录一次，一天 96 个值（p.6）。公式(5)(6) 给出 α、β 表达式，含光伏-风电组合效应系数 l、负荷不确定性与电气连接的协调参数 b。公式(7)(8) 分别为风电、光伏发电的功率积分式。公式(9) 将 TRR 约束集成进 INBI：`|αi - αj| ≤ Kα·αmin`、`|βi - βj| ≤ Kβ·βmin`，其中 Kα、Kβ 为电气连接的作用系数矩阵（p.7）。
- **INBI 算法流程（第 3 节，图 3、图 4）**：基于原始 NBI 算法 [35]，顺序步骤为——(a) 给出原始 NBI 优化模型；(b) 用 AWS 算法得到修正后的帕累托前沿；(c) 将修正前沿投影到三目标帕累托前沿；(d) 用 AUAM 对三目标前沿点纠正并筛出非劣解；(e) 用马氏距离双基点法替代原 NBI 的距离法得到妥协解（p.7-8）。图 4 细化：先用 NBI 构建三维帕累托前沿与三个二维前沿，分别用 AWS 修正三个二维前沿并保留修正过程中产生的每个点，再用映射方法合并到三维前沿，AUAM 判断可行解得到非劣解，最后马氏距离双基点法得妥协解（p.10）。
- **关键模块**：
    1.  **AWS（自适应权值和）**：跨维度增加可行解、保证差异、避免同质化。原始 AWS 由一个初始点生成一个修正点，本文将修正过程中每个点扩展为原来的 B 倍；空间复杂度由 o(A) 变为 o(A+BA)，时间复杂度仍为 o(A)（p.8）。
    2.  **AUAM（调整均匀轴法）**：解决帕累托前沿分布不广不均、检测灵敏度不足的问题，基于最优筛选步长优化筛选精度。以三维为例 AWS 产生三种步长，AUAM 需适配多步长、优先取最小步长以保证不漏点、提高检测灵敏度。原始 NBI 生成点数记为 C，经 AUAM 后空间/时间复杂度由 O(C) 变为 o(C+A+BA)（p.8）。
    3.  **马氏距离双基点法**：替代原 NBI 的欧氏距离。传统评价矩阵与距离不考虑相关性；本法基于权重对角矩阵修正正/负理想点，避免信息重叠影响最优决策，并考虑个人偏好因素，被作者认为比其他复杂距离函数更简单、实用、全面、准确（p.8；据原文后续页 p.13-14 给出评价矩阵建立与归一化细节，提取缓存未覆盖具体公式，待核）。
- **与已有方法的差异**：相比原始 NBI，INBI 通过 AWS 增加解的多样性、通过 AUAM 改善前沿分布质量、通过马氏距离改进筛选准则，整体获得更广、更均、更接近真实前沿的帕累托解集（图 3 的映射关系表 Table 1 总结了"限制-解决-验证"三栏）。

## 实验

提取文本（前 12 页）含方法与模型，但案例研究主体在 p.14 之后，未被提取缓存覆盖。**以下数字据原文与提取文本中的线索，部分待核：**

- **案例设置（据原文后续页 p.14，提取缓存未覆盖正文，仅有标题线索）**：基于某地区电网负荷数据做案例研究；以 15 分钟为观测间隔、全天共 96 个观测点（p.14 标题/摘录线索）。该算法适用于含三个及以上优化目标的情形。
- **权重设置（据原文 p.15，提取缓存未覆盖，仅线索）**：权重系数 [0.5, 0.25, 0.25]，详见 Table 2；功率/负荷/风光数据见图 7-9（p.15 线索）；图 10 给出空调开启后室内温度变化（p.17 线索）。结果见 Table 3（不考虑权重分配）、Table 4（考虑权重分配）等（p.17-18 线索）。
- **主要结果（来源摘要 p.1 与映射表 Table 1 p.8-9）**：相比原情形平均偏差降低 60%（结果见图 11）；在设备成本、供电成本、用户舒适度三个目标上分别优化 8.2%、7.6%、1.6%（结果见 Table 3-7）。

（注：8.2%/7.6%/1.6%/60% 这组数字在摘要与映射表中均被明确陈述，可信；但完整的对比方法、数据规模与逐表数值在提取缓存中缺失，标注为线索/待核。）

## 局限

1.  **方法复杂度上升**：INBI 集成 AWS、AUAM、马氏距离三模块，提升解质量的同时显著增加空间复杂度（AWS：o(A)→o(A+BA)；经 AUAM：O(C)→o(C+A+BA)），计算开销随保留点数 B、初始点数增大（p.8 明确给出复杂度变化）。
2.  **实验细节不在提取范围**：完整对比基线、数据规模、逐表结果在缓存外（p.14 之后），其声称的 8.2%/7.6%/1.6% 优势是否来自公平、充分的对比，需核对原文 Table 3-7 与图 11。
3.  **假设依赖强**：模型绑定特定公式——分时电价为华北标准（公式 2）、舒适度为简化热舒适度公式（公式 3），且依赖对负荷、风/光发电的预测精度，跨地区/场景需重新标定。
4.  **复现门槛较高**：TRR 公式(5)(6) 含组合效应系数 l 与协调参数 b，其物理意义与取值需查原文；INBI 流程步骤多（图 4），复现需逐一对照流程图、复杂度推导与公式(1)-(10)。

## 个人评论

1.  **问题定义与建模的启发**：论文把智能建筑群能源优化清晰地表述为一个三目标优化问题，并搭起"技术（设备）— 经济（电费）— 人因（舒适度）"三位一体的目标框架。其成本模型、分时电价、舒适度模型与功率平衡约束的写法，对同类综合能源系统建模有直接参考价值。
2.  **算法改进思路的启发**：面对 NBI 这类经典多目标优化方法，本文给出一条可迁移的"诊断—分模块—组合"改进路线：AWS 增加解多样性 → AUAM 改善前沿分布 → 马氏距离改进筛选准则，且每一步都配了复杂度分析与"限制-解决-验证"映射表（Table 1），方法论值得借鉴。
3.  **引入新评价指标的尝试**：TRR 把系统运行特性（风光关联、负荷不确定性、电气连接）显式编码为优化约束（公式 9），是一种把"领域知识"转成"优化结构"的思路；不过其可解释性与 60% 偏差下降的因果联系，需依赖缓存外的实验验证才能落实。

### 使用建议

- **如果快速了解**：读摘要（p.1）、引言贡献部分（p.4）、图 3 与图 4（p.8、p.10），即可掌握问题、两大贡献（TRR + INBI）与算法框架。
- **如果复现**：精读第 2 节（系统模型、公式 1-9）与第 3 节（INBI 五步、AWS/AUAM/马氏距离的复杂度与实现），并补读 p.13-18 的评价矩阵与案例数据。
- **如果借鉴创新点**：借鉴 TRR——为自己问题设计一个编码系统内部关联性的新指标；借鉴 INBI 框架——把"增解多样性 / 改善前沿分布 / 改进筛选准则"三步套到自己用的多目标算法上。
- **如果写 Related Work**：可归入"智能建筑能源管理"、"多目标优化在能源系统中的应用"、"NBI 算法及其改进"三类。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**智能建筑能源管理与多目标优化算法**方向（发表于建筑环境领域期刊 *Building and Environment*），研究智能建筑群中分布式可再生能源（风、光）与各类负荷、空调的多目标优化调度。论文提出改进优化算法 INBI 与新评价指标 TRR，求解设备成本、供电成本、用户舒适度三者的权衡。文件名携带的分类主题 `T_通用_NLP_其他` 是知识库的"通用/其他"兜底类——本文与自然语言处理无关，其真实归属是能源系统/智能电网/运筹优化，因 taxonomy 无对应能源类，保留兜底类是正确的。

## 2. 一句话总结
本文提出改进的常规边界交集算法（INBI，=NBI + AWS + AUAM + 马氏距离）和转移-保留率指标（TRR），用于求解考虑风光关联、负荷不确定性与电气连接的智能建筑三目标能源优化问题，案例中设备/供电成本与舒适度分别改善 8.2%、7.6%、1.6%。

## 3. 背景与问题
- **为什么要做**：智能建筑（配分布式可再生能源发电的新型建筑）的优势随分布式能源普及日益明显，但其能源优化调度变复杂；难点在分布式可再生能源的调控（p.3）。
- **之前方法的问题**：
    1.  既有研究（模型预测 [7-9]、发电预测 [10]、需求响应多目标模型 [11-14]）未充分考虑风/光关联、负荷不确定性、电气连接对控制的影响（p.3-4）。
    2.  求解层面：PSO [15,16] 难解复杂多目标问题；NBI 与 AUAM [22] 在复杂多维问题上难获分布广、均匀且接近真实的帕累托前沿（p.4）。
- **核心矛盾**：需要同时给出更全面的评价指标与更优的多目标算法，产出更广、更均、更接近真实前沿的帕累托解集，兼顾设备成本、供电成本、用户舒适度。

## 4. 核心贡献
引言列出的两条（p.4）：
1.  **首提 TRR（转移-保留率）评价指标**：涵盖风、光、空调联合调度；考虑风/光电气连接综合效应与负荷不确定性，提升对分布式能源系统的可解释性。
2.  **提出 INBI 算法**：基于改进 AWS 跨维度增可行解；用 AUAM 解决前沿广而均匀；用马氏距离双基点法作筛选准则，进一步使前沿分布广而均匀。

## 5. 方法详解
- **系统模型（第 2 节）**：供电侧 = 电网 + 风电 + 光伏，用电侧 = 各类负荷（图 1）；各建筑独立配风/光发电与储能、储能互联（图 2）。三个被调控量按"月"口径定义：设备成本（设备建设+维护月总额）、供电成本（用户负荷月电费）、舒适度（住户舒适度月均值）（p.4-5）。
- **三目标（公式 1-3）**：设备成本 C_w 含风电运行系数 w1、维护系数 w2 与光伏成本系数 l（公式 1）；供电成本用分时电价，谷 0.3（23:00-06:00）/峰 0.7（06:00-23:00），华北标准（公式 2）；舒适度 `S_D=[1-2|6-0.25·T_in|]·100%`，T_in∈[22,30]℃（公式 3）。功率平衡约束（公式 4）：电网交换 + 风电 + 光伏 = 可调度负荷 + 关键负荷 + 可切换负荷。
- **TRR（公式 5-9）**：α、β 为光伏/风电的"输出与储备之比"，每 15 分钟记一次、一天 96 值（p.6）；含组合效应系数 l、协调参数 b。公式(7)(8) 为风/光功率积分。公式(9) 将 TRR 作约束并入 INBI：`|αi-αj|≤Kα·αmin`、`|βi-βj|≤Kβ·βmin`（Kα/Kβ 为电气连接作用系数矩阵）。
- **INBI 五步（第 3 节，图 3-4）**：(a) 给出原始 NBI 三目标模型（公式 10）；(b) AWS 得修正前沿；(c) 投影到三目标前沿；(d) AUAM 纠正点并选非劣解；(e) 马氏距离双基点法得妥协解。
- **三模块要点与复杂度**：
    - AWS：每修正点扩展为 B 倍，空间 o(A)→o(A+BA)，时间仍 o(A)。
    - AUAM：优先取最小步长以不漏点、提灵敏度；原 NBI 点数 C，经 AUAM 后 O(C)→o(C+A+BA)。
    - 马氏距离：基于权重对角矩阵修正正/负理想点，考虑指标相关性与个人偏好，避免信息重叠（评价矩阵归一化细节在 p.13-14，提取缓存未覆盖具体公式，待核）。
- **与 NBI 差异**：AWS 增多样性、AUAM 改分布、马氏距离改筛选，整体更接近真实前沿；图 3 的 Table 1 用"限制-解决-验证"三栏总结。

## 6. 实验与结果
案例研究主体（p.14 之后）不在提取缓存（前 12 页）内。据原文线索与摘要：
- **据原文后续页（p.14-15 线索，提取缓存未覆盖正文，待核）**：用某地区电网负荷数据做案例，15 分钟一观测、全天 96 点；权重系数 [0.5,0.25,0.25]（Table 2）；数据见图 7-9，室温变化见图 10；结果见 Table 3（不考虑权重）、Table 4（考虑权重）。
- **主结果（摘要 p.1 + 映射表 Table 1 p.8-9，可信）**：平均偏差降 60%（图 11）；设备成本/供电成本/舒适度分别优化 8.2%、7.6%、1.6%（Table 3-7）。
- 完整基线、数据规模、逐表数值需核原文。

## 7. 这篇论文真正有价值的地方
1.  **三位一体建模**：把智能建筑群优化清晰拆成设备成本、供电成本、舒适度三目标，并配齐成本/电价/舒适度/功率平衡的可复用公式。
2.  **可迁移的改进范式**：NBI 的"诊断 → 分模块（AWS/AUAM/马氏距离）→ 组合 + 复杂度分析 + 映射表验证"，方法论清晰。
3.  **领域知识转优化结构**：TRR 把风光关联、负荷不确定性、电气连接编码为约束（公式 9），是把运行特性变成优化约束的有意义尝试。

## 8. 局限与问题
1.  **复杂度上升**：三模块叠加使空间复杂度由 o(A)/O(C) 升到 o(A+BA)/o(C+A+BA)，开销随 B 与点数增大（p.8）。
2.  **实验细节缓存外**：对比基线、数据规模、逐表结果在 p.14 之后，8.2%/7.6%/1.6% 是否来自公平充分对比需核 Table 3-7 与图 11。
3.  **假设依赖强**：分时电价为华北标准、舒适度为简化公式、依赖负荷/发电预测精度，跨地区需重标定。
4.  **复现门槛高**：TRR 公式(5)(6) 的 l、b 取值与 INBI 多步流程需逐一对照原文公式与流程图。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要（p.1）+ 引言贡献（p.4）+ 图 3、图 4（p.8、p.10）。
- **复现**：精读第 2 节（公式 1-9）与第 3 节（INBI 五步 + 复杂度），并补读 p.13-18 评价矩阵与案例数据。
- **借鉴创新点**：仿 TRR 设计编码系统内部关联性的新指标；仿 INBI 把"增多样性/改分布/改筛选"三步套到自己的多目标算法。
- **写 Related Work**：归入"智能建筑能源管理"、"多目标优化在能源系统中的应用"、"NBI 算法及其改进"。

## 10. 和其他论文的关系
本文与 NLP 无关（`T_通用_NLP_其他` 仅为兜底分类）。内容上相关的应是：
- 其他智能建筑、微电网、综合能源系统的多目标优化研究（如引言 [11-14] 的需求响应与多微网工作）。
- 其他对 NBI、NSGA-II、MOEA/D、PSO 等多目标算法的改进（如引言 [15-24]）。
- 受当前库主题分类限制，库内可能没有直接相关的 `[[双链]]` 论文。

## 11. 关键词
智能建筑 (Smart Building), 可再生能源调度 (Renewable Energy Dispatch), 多目标优化 (Multi-objective Optimization), 常规边界交集算法 (NBI), 改进 NBI 算法 (INBI), 转移-保留率 (TRR), 自适应权值和 (AWS), 调整均匀轴法 (AUAM), 马氏距离双基点法 (Mahalanobis Distance Double Base Point), 帕累托前沿 (Pareto Frontier), 分时电价 (TOU Price), 设备成本/供电成本/用户舒适度 (Equipment/Power-supply Cost & Occupants' Comfort)

## 12. 可信度说明
本精读笔记**主体基于提取缓存的前 12 页（共 24 页）**。方法框架、三个优化目标公式（1-9）、TRR 定义、INBI 五步流程、三模块及其复杂度（AWS o(A)→o(A+BA)、AUAM O(C)→o(C+A+BA)）均有提取文本直接支撑，可信度高。**实验部分（第 4 节，p.14 之后）只有提取缓存中的页眉/摘录线索，逐表数值与对比方法缺失**，已标注"据原文后续页…待核"。8.2%/7.6%/1.6%/60% 这组结果在摘要与映射表 Table 1 中均被明确陈述，故保留为可信结论，但其实验背景仍待核原文。局限部分基于已提供文本的方法描述与复杂度分析做合理推断。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2022_Improved_normal-boun.txt` (提取覆盖 12/24 页; 原 AI 主体 12/24 + 全文补读 13-24 线索); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro); 本次重读据提取文本核校三目标公式、TRR、INBI 流程与复杂度，修正摘要乱码并补全副标题/单位/分时电价细节。
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
