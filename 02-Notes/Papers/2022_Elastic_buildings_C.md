---
title: "Elastic buildings: Calibrated district-scale simulation of occupant-flexible campus operation for hybrid work optimization"
authors:
  - "Martín Mosteiro-Romero"
  - "Clayton Miller"
  - "Adrian Chong"
  - "Rudi Stouffs"
year: 2022
venue: "arXiv 2210.06124 (preprint, submitted to Building and Environment)"
doi: 
pdf: [[2022_Elastic_buildings_C.pdf]]
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
extract_cache: .paper-cache/extracts/2022_Elastic_buildings_C.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/43 pages"
---
# Elastic buildings: Calibrated district-scale simulation of

## 基本信息
- **PDF**: [[2022_Elastic_buildings_C.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Elastic buildings: Calibrated district-scale simulation of occupant-flexible campus operation for hybrid work optimization |
| **作者** | Martín Mosteiro-Romero; Clayton Miller; Adrian Chong; Rudi Stouffs（新加坡国立大学 / Singapore-ETH Centre） |
| **发表时间** | 2022（arXiv v1）；v2 于 2023-04-25 提交至 Building and Environment |
| **刊物/会议** | arXiv:2210.06124 [physics.soc-ph] 预印本（拟投 Building and Environment） |
| **DOI** | PDF 文本未明确（arXiv 编号 2210.06124v2） |

> **分类说明**：本文是「城市建筑能源建模 / 需求驱动建筑控制」的跨学科工作（arXiv 分类 physics.soc-ph），与计算机视觉目标检测无关。原 `primary_topic = C2_目标检测_违建_车辆_船舶_行人` 系误归类，已改为 `T_通用_NLP_其他`（taxonomy 中无对应的建筑能源/控制主题，归入通用其他类）。

## 摘要

**英文原摘要（据 PDF 提取文本整理，修复空格与连字符断裂、剔除杂入字符）：**

> Before 2020, the way occupants utilized the built environment had been changing slowly towards scenarios in which occupants have more choice and flexibility in where and how they work. The global COVID-19 pandemic accelerated this phenomenon rapidly through lockdowns and hybrid work arrangements. Many occupants and employers are considering keeping some of these flexibility-based strategies due to their benefits and cost impacts. This paper explores how demand-driven control strategies in the built environment might support the transition to increased workplace flexibility by simulating various scenarios related to the operational technologies and policies of a real-world campus using a district-scale City Energy Analyst (CEA) model that is calibrated with measured energy demand data and occupancy profiles extracted from WiFi data. These scenarios demonstrate the energy impact of ramping building operations up and down more rapidly and effectively to the flex-based work strategies that may solidify. The scenarios show a 5–15% decrease in space cooling demand due to occupant absenteeism of 25–75% if centralized building system operation is in place, but as high as 17–63% if occupancy-driven building controls are implemented. The paper discusses technologies and strategies that are important in this paradigm shift of operations.
>
> **Keywords**: demand-driven controls; flexible work arrangements; urban building energy modeling; data-driven occupancy modeling

**中文翻译：**

> 在 2020 年之前，人们使用建成环境的方式正缓慢地朝着「在何处、以何种方式工作上拥有更多选择与灵活性」的方向变化。全球性的 COVID-19 疫情通过封锁与混合办公安排，迅速加速了这一进程。鉴于灵活办公带来的收益与成本优势，许多员工与雇主正考虑长期保留其中部分策略。本文探讨建成环境中的需求驱动控制策略如何支撑向更高工作灵活性的转型：以一座真实校园的运营技术与政策为对象，使用区域尺度的 City Energy Analyst（CEA）模型模拟多种场景；该模型用实测能耗数据与从 WiFi 数据提取的占用剖面进行校准。这些场景展示了根据可能固化下来的弹性办公策略、更快更有效地上下调节建筑运行所带来的能源影响。结果表明：在 25–75% 的人员缺勤下，若采用集中式建筑系统运行，空间冷却需求下降 5–15%；但若实施占用驱动的建筑控制，则降幅可高达 17–63%。文章讨论了在这一运营范式转变中至关重要的技术与策略。
>
> **关键词**：需求驱动控制；灵活办公安排；城市建筑能源建模；数据驱动占用建模

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：办公模式正从「固定工位」转向灵活办公（hot-desking、co-working、desk-sharing、office hoteling、activity-based workspaces 等），COVID-19 疫情更将其急剧加速（2020 年 10 月一项 10,332 人美国调查显示在家办公比例从疫前 20% 升至 71%）。然而建筑系统（尤其 HVAC、通风）仍普遍按「峰值设计容量 + 人工排定的固定时间表」运行，与实际多变的低占用率严重脱节。一篇 2014 综述指出建筑 26–65% 的能耗发生在非工作时段（夜间与周末），灵活办公会进一步放大这种浪费。
- **之前方法的问题**：① 现有占用感知/控制研究绝大多数聚焦于单房间、单分区或单建筑层级的照明与 HVAC 节能（PIR、CO₂ 等），属「被动响应式（reactive）」控制，在过渡期还会因热/空气质量瞬态而引发不适；② 建筑规范中与占用相关的条款过于简化，建模者常为规避责任而沿用默认/规范假设，即便明知其不真实；③ 缺少把控制维度从「建筑内」扩展到「园区/区域间」的空间协同优化视角。文中亦提到一个关键悖论：疫情期间某些校园占用率虽降至 25%，能耗却仅降 3%（荷兰某大学），原因正是固定 HVAC 时间表使占用率与能耗仅弱相关；2020 年全球建筑部门最终能耗反而上升 3%。
- **核心矛盾**：建筑系统「刚性」的运营方式（固定排程、按峰值设计）与办公人员日益「弹性」的时空使用模式之间的矛盾——如何让建筑像弹簧一样随实际需求（人数、位置）高效伸缩。

## 关键贡献

1. **提出「弹性建筑（elastic buildings）」概念**：常规建筑只把需求响应做进分区级控制；弹性建筑在 zone、system、building 乃至 district（区域）尺度上综合运用占用驱动策略，并叠加「空间分配（space allocation）」政策——按需把人与空间配对，从而不仅在建筑尺度、更在区域尺度上降低能源需求。
2. **构建 WiFi 校准的园区尺度能源需求模型**：基于开源工具 CEA，footprint 取自 OpenStreetMap 并按楼层数挤出体量，结合新加坡/瑞士原型数据库，再用实测小时级冷却、用电、天气与 WiFi 连接数据进行校准，提取园区尺度的占用剖面。
3. **量化三类运营策略在不同 WFH 比例下的节能潜力**：横向对比集中式、占用驱动、弹性建筑三种运营，纵向对比不同缺勤率（25–75%），给出空间冷却需求降幅区间（集中式 5–15%、占用驱动最高 17–63%）。
4. **梳理范式转变所需的技术与策略**：系统综述占用感知传感器（PIR、RFID、视觉、超声、声学、CO₂、电表隐式感知、WiFi）、传感器融合、proactive 预测控制等，并讨论 WiFi 占用数据的局限（多设备重复计数、无设备者漏计、静止设备、室内定位误差）。

## 方法

- **整体框架（Figure 1 工作流）**：在 CEA 上做园区尺度建筑能源需求建模 → 用实测能耗/天气/WiFi 数据校准 → 在校准模型上对「WFH 比例 × 运营策略」组合做场景评估（含当前及未来气候）。
- **输入与输出**：
    - **输入**：① 建筑物理特性（footprint 取自 OpenStreetMap，按楼层数挤出体量；材料热工属性、照明/设备功率密度、系统设定点取自 CEA 新加坡/瑞士原型数据库）；② 校准用的小时级实测冷却需求、用电需求、天气、WiFi 连接数据（因新加坡无供暖需求，能表数据仅含冷却与用电）；③ 场景参数（WFH 比例、运营策略类型）。
    - **输出**：各场景下园区建筑群的**空间冷却需求**，用于评估节能潜力。
- **关键模块**：
    1. **WiFi 占用模型**：以 WiFi 连接设备数作为占用代理；文中明确指出设备数仅是人数指标，需估计「检测到的移动设备数 ↔ 实际人数」的关系（引 Balaji 等系统 86% 检测准确率、6.2% 漏检、单日实验降电 17.8%）。补读线索显示论文用聚类把每天指派到一个占用模式簇（occupancy pattern cluster）以提取典型占用剖面。
    2. **CEA 能源模型校准**：把原型数据库参数用实测数据调整以提升基准精度。
    3. **运营策略模拟（三种）**：
        - **集中式（centralized）**：整栋建筑按冷却时间表统一开关。
        - **占用驱动 / 全需求驱动（occupant-driven）**：仅对被占用空间供冷供风，未占用空间维持在对应的回退温度（setback temperature）；引入分区级部分负荷（part load）运行。
        - **弹性建筑（elastic）**：在占用驱动基础上叠加区域级空间分配——按需分配空间，仅当现有建筑容量不足时才开启额外建筑，且优先运行能效高、冷却需求低的建筑。
- **数学/机制直观解释**：核心是用「被调节空间面积」去逼近「实际被占用空间」。集中式调节面积恒为 100%；占用驱动把调节面积缩到实际占用部分；弹性策略进一步通过区域调度，保证被调节面积落在园区中能效最高的建筑上。
- **与已有方法差异**：① 控制维度从「建筑内」扩展到「园区/区域间」，引入空间调度；② 从被动响应转向结合预测与调度的主动优化（呼应文中 proactive control 思路，如 Gunay 等通过优化 setback 起止时间获供暖 30%、制冷 13% 节能）；③ 用真实 WiFi 数据校准使模拟贴近现实。

## 实验

- **使用的数据集**：新加坡国立大学校园的实测数据——建筑小时级冷却与用电需求、天气数据、WiFi 连接数据；补读线索（Figure 3）显示选取了少数同时具备电力、冷却需求与 WiFi 数据的建筑（含一座 performance hall），覆盖完整的三年期。
- **对比方法**：三种运营策略横向对比（集中式 vs 占用驱动 vs 弹性）× 不同 WFH 缺勤率（25–75%，摘要表述为 25%、50%、75% 区间）纵向对比；基准为 100% 出勤 + 集中式运营。
- **评价指标**：空间冷却需求相对基准的下降百分比。
- **主实验结果（据摘要确证）**：
    - **集中式**运营：缺勤率 25–75% 时，空间冷却需求下降 **5–15%**。
    - **占用驱动**控制：下降幅度最高可达 **17–63%**，显著优于集中式。
    - **弹性建筑**运营：摘要将其与「占用驱动控制」合并表述为可达 17–63% 的高降幅；提取正文（前 12 页）未给出弹性策略相对占用驱动的单独增量数字（结果在第 6 节，超出 12 页提取范围；补读线索见 Figure 2 场景矩阵、Figure 5/6）。
- **占用感知技术节能参照（文中综述引用，非本文实验）**：照明占用传感器 20–60%；占用驱动 HVAC+照明 20–50%；Erickson 视觉传感网 42%；Agarwal PIR+门磁 10–15%；Nagy 自适应照明 37.9%；Peng 制冷 21.2–39.4%（低中占用办公室）。
- **消融/泛化/效率信息**：提取正文（前 12 页）未明确。论文偏宏观策略模拟，非算法模块消融或计算效率分析。

## 局限

- **能耗范畴单一**：聚焦**空间冷却需求**（新加坡热带气候、无供暖），未全面评估照明、办公设备、通风等其他能耗，也未量化居家办公带来的住宅侧能耗增量（文中提到封锁期住宅能耗上升 11–32%、存在 rebound 效应）。结论仅代表建筑冷却侧节能的一部分。
- **WiFi 占用代理的固有缺陷**：多设备重复计数、无 WiFi 设备者漏计、长期连接的静止/共享设备、室内定位误差；单传感器系统失效即失能。文中倡导传感器融合以缓解，但会增加数据处理与响应延迟。
- **弹性策略依赖理想化假设**：空间分配算法、建筑优先级排序、「按能效优先开启建筑」等均为模拟假设，实际可调度性与管理可行性需进一步验证。
- **地理与气候特异性**：案例位于新加坡（全年高冷却需求），结论对供暖为主的温带/寒冷地区适用性需另行验证；论文虽提及「未来气候」场景，但提取正文未含其结果。
- **缺乏经济性分析**：讨论了所需技术（占用传感、WiFi 融合、空间调度系统），但提取正文未对传感器/控制系统升级成本及成本效益做评估。

## 个人评论

1. **问题视角的启发**：把建筑节能从「设备效率提升」转向「空间利用模式与运营系统动态匹配」的系统视角，并首次把这个匹配从建筑内扩展到园区/区域尺度——在混合办公趋势下点出了一个被忽视的重大节能方向。
2. **低成本数据复用的范式价值**：展示了把现成、零额外硬件成本的 WiFi 连接数据转化为可校准并驱动大规模 UBEM 的占用输入，为机构利用既有数字基础设施做能效管理提供了可落地路径。
3. **「弹性建筑」是个有张力的设计理念**：它提醒工程师，未来建筑系统的目标不应是覆盖峰值负荷的「刚性强大」，而应是高效响应变化的「弹性智能」；与之相对的「区域级空间调度优先运行高能效建筑」是其最具新意、也最难落地（涉及组织调度与人因）的一步。
4. **研究范式可迁移**：「真实数据校准模型 → 定义政策/技术场景 → 模拟能源影响」这一范式适合评估新政策/新技术的宏观节能潜力；但也要警惕其结论强依赖 CEA 原型库与 WiFi 代理的假设，跨气候、跨建筑类型迁移前需重新校准。

### 使用建议

- **如果快速了解**：读摘要（p.1）、引言与论文范围（1–1.1 节，p.2–4）即可掌握动机、弹性建筑定义与三类策略；主要数字结论在摘要与第 6 节（第 6 节超出 12 页提取范围）。
- **如果复现**：重点是方法论（第 3 节，p.11 起：CEA 建模、WiFi 占用建模、校准、场景评估）与案例研究/数据收集（第 4–5 节，超出提取范围）；需准备 OpenStreetMap footprint、CEA 原型库、小时级冷却/用电/天气/WiFi 数据。
- **如果借鉴创新点**：学其「WiFi 占用数据 + UBEM 校准」的数据融合（3 节）与「集中式/占用驱动/弹性」三层运营对比框架。
- **如果写相关工作**：可归入「城市建筑能源建模（UBEM）」「需求驱动/占用驱动建筑控制」「混合办公/后疫情设施管理」「数据驱动占用建模」。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**城市建筑能源建模（UBEM）与需求驱动建筑控制**方向（arXiv 分类 physics.soc-ph，拟投 Building and Environment），与计算机视觉目标检测无关。它要解决的核心问题是：在 COVID-19 之后混合/灵活办公常态化、建筑实际占用率大幅波动且降低的背景下，沿用「按峰值设计容量 + 固定时间表」运行的建筑系统会造成大量能源浪费；论文用数据驱动模拟探索如何让建筑运营随真实占用「弹性伸缩」，并把优化尺度从建筑扩展到园区/区域。适合放在「智能建筑」「UBEM」「占用驱动控制」主题下。

## 2. 一句话总结
本文提出「弹性建筑」概念，用基于 WiFi 占用数据校准的园区尺度 CEA 能源模型，模拟新加坡某大学校园在不同居家办公（WFH）比例下三种运营策略的空间冷却需求，证明占用驱动控制相比集中式控制能把冷却需求降幅从 5–15% 提升到最高 17–63%。

## 3. 背景与问题
- **为什么要做**：灵活办公（hot-desking、office hoteling、ABW 等）在疫前已是趋势，COVID-19 急剧加速之（美国 WFH 比例 20%→71%，且 54% 员工希望长期居家）。但建筑 HVAC/通风仍按峰值设计与固定排程运行，与低且多变的实际占用脱节；2014 综述指出建筑 26–65% 能耗发生在非工作时段。
- **之前方法的问题**：① 占用感知/控制研究多停留在房间/分区/单建筑层级，属被动响应式控制，过渡期还会有热与空气质量瞬态不适；② 规范中占用条款过于简化，建模者沿用不真实的默认假设以规避责任；③ 缺少把控制扩展到园区/区域尺度的空间协同视角。一个有力佐证：荷兰某校园占用率降到 25% 而能耗仅降 3%，因固定 HVAC 排程使二者仅弱相关；2020 年全球建筑部门最终能耗反升 3%。
- **核心矛盾**：建筑「刚性」运营与人员「弹性」时空使用之间的矛盾，需让建筑能随实际需求高效伸缩。

## 4. 核心贡献
1. **提出「弹性建筑」概念**：把需求响应从分区级扩展到 zone/system/building/district 多尺度，叠加「空间分配」政策按需配对人与空间，在建筑与区域两个尺度同时降能耗。
2. **WiFi 校准的园区尺度 CEA 模型**：footprint 取自 OpenStreetMap，热工/功率/设定点取自 CEA 原型库，再用实测小时级冷却、用电、天气、WiFi 数据校准并提取占用剖面。
3. **量化三类运营策略 × WFH 比例的节能潜力**：集中式、占用驱动、弹性建筑三策略横向对比，缺勤率 25–75% 纵向对比，给出冷却需求降幅区间。
4. **梳理范式转变所需技术与策略**：综述占用感知传感器谱系、传感器融合、proactive 预测控制，并明确 WiFi 占用数据的四类局限。

## 5. 方法详解
- **整体框架（Figure 1）**：CEA 园区建模 → 实测能耗/天气/WiFi 校准 → 「WFH 比例 × 运营策略」场景评估（含当前与未来气候）。
- **输入**：① 建筑物理特性（OpenStreetMap footprint 按楼层挤出 + CEA 新加坡/瑞士原型库参数）；② 校准用小时级实测冷却、用电、天气、WiFi 数据（新加坡无供暖，能表仅含冷却与用电）；③ 场景参数（WFH 比例、运营策略）。**输出**：各场景园区建筑群的空间冷却需求。
- **关键模块**：
    1. **WiFi 占用模型**：以连接设备数为占用代理，需估计「设备数 ↔ 人数」关系（Balaji 系统 86% 准确、6.2% 漏检、单日降电 17.8%）；补读线索显示用聚类把每天指派到占用模式簇以提取典型剖面。
    2. **CEA 校准**：用实测数据调整原型库参数提升基准精度。
    3. **三种运营策略**：集中式（整栋按时间表统一开关）；占用驱动（只给占用空间供冷供风、未占用区维持回退温度、引入分区部分负荷）；弹性（在占用驱动上加区域级空间分配，按需开建筑、优先运行高能效建筑）。
- **机制直观**：用「被调节空间面积」逼近「实际占用空间」——集中式恒 100%，占用驱动缩到实际占用，弹性再通过调度保证被调节面积落在最高能效建筑上。
- **与已有方法差异**：控制维度从建筑内扩到园区间；从被动响应转向预测+调度的主动优化（呼应 Gunay 等 setback 优化获供暖 30%/制冷 13%）；用真实 WiFi 数据校准。

## 6. 实验与结果
- **数据集**：新加坡国立大学校园实测——建筑小时级冷却与用电需求、天气、WiFi 连接数据；补读线索（Figure 3）显示选取了少数同时具备三类数据的建筑（含 performance hall），覆盖完整三年期。
- **对比**：三策略横向 × WFH 缺勤率 25–75% 纵向；基准 = 100% 出勤 + 集中式。
- **指标**：空间冷却需求相对基准的下降百分比。
- **主结果（据摘要确证）**：集中式 5–15%；占用驱动控制最高 17–63%。摘要将弹性建筑与占用驱动合并在 17–63% 这一档表述，弹性相对占用驱动的单独增量数字在第 6 节（超出 12 页提取范围，补读线索见 Figure 2 场景矩阵、Figure 5/6）。
- **综述引用的技术节能参照（非本文实验）**：照明占用传感器 20–60%；占用驱动 HVAC+照明 20–50%；Erickson 视觉网 42%；Agarwal PIR+门磁 10–15%；Nagy 自适应照明 37.9%；Peng 制冷 21.2–39.4%。
- **消融/泛化/效率**：提取正文（前 12 页）未明确，论文偏宏观策略模拟。

## 7. 这篇论文真正有价值的地方
1. **视角转换**：从「设备效率」转到「空间利用模式 × 运营系统动态匹配」，并把这一匹配从建筑内推进到园区/区域尺度。
2. **低成本数据复用**：把零额外硬件的 WiFi 数据转化为可校准并驱动大规模 UBEM 的占用输入，路径可复制。
3. **「弹性建筑」框架**：把设计目标从「刚性覆盖峰值」重定义为「弹性高效响应」，其区域级空间调度（优先开高能效建筑）是最具新意也最难落地的一环。
4. **范式可迁移**：「真实数据校准 → 政策/技术场景 → 模拟能源影响」适合评估宏观节能潜力，但结论强依赖 CEA 原型库与 WiFi 代理假设。

## 8. 局限与问题
- **能耗范畴单一**：聚焦空间冷却（新加坡无供暖），未评估照明/设备/通风及居家办公的住宅侧能耗增量（封锁期住宅能耗 +11–32%、存在 rebound）。
- **WiFi 代理缺陷**：多设备重复计数、无设备者漏计、静止/共享设备、室内定位误差；单传感器失效即失能，需融合但增延迟。
- **弹性策略理想化**：空间分配算法、建筑优先级、按能效开启等均为模拟假设，落地可行性待验证。
- **气候/地理特异性**：新加坡热带高冷却需求，结论对温带/寒冷供暖区适用性需另证；未来气候场景结果未在提取正文中。
- **无经济性分析**：未评估传感/控制升级成本与成本效益（提取正文范围内）。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要（p.1）+ 引言与范围（1–1.1 节，p.2–4），掌握动机、弹性建筑定义、三类策略；主数字在摘要与第 6 节。
- **复现**：方法论（第 3 节，p.11 起）+ 案例研究/数据收集（第 4–5 节，超出提取范围）；需 OpenStreetMap footprint、CEA 原型库、小时级冷却/用电/天气/WiFi 数据。
- **借鉴创新点**：学「WiFi 占用 + UBEM 校准」数据融合与三层运营对比框架。
- **写相关工作**：归入「城市建筑能源建模」「需求/占用驱动建筑控制」「混合办公设施管理」「数据驱动占用建模」。

## 10. 和其他论文的关系
本文是一篇综述 + 模拟研究，核心落在 **城市建筑能源建模（UBEM）** 与 **占用驱动建筑控制**。相关方向：
- 数据驱动建筑能源预测与校准（CEA 等 UBEM 工具）
- 基于 WiFi 的占用检测与室内定位（Balaji、Trivedi、Hobson 等）
- 混合/灵活办公环境下的设施管理与空间调度
- COVID-19 对建筑/能源系统影响的实证研究
（注：原分类 `C2_目标检测_违建_车辆_船舶_行人` 与本文无关，已改为 `T_通用_NLP_其他`，不建立基于 CV 检测分类的链接。）

## 11. 关键词
弹性建筑（elastic buildings），需求驱动/占用驱动控制，混合/灵活办公，WiFi 占用数据，城市建筑能源建模（UBEM），City Energy Analyst（CEA），空间冷却需求，校准模型，空间分配/调度，COVID-19

## 12. 可信度说明
本篇精读基于 PDF 提取文本——确切地说，缓存提取仅覆盖论文前 12 页（标题、作者、摘要、引言、第 2 节背景综述、第 3 节方法论开头），约 25,000 字符上限内的内容。对**研究动机、背景综述、「弹性建筑」核心概念、三类运营策略定义、方法论框架**的总结是可靠且详细的。
但提取文本**不完整**：第 3 节后半（占用建模、校准细节）、第 4–5 节（案例研究与数据收集、基线性能）、第 6 节（仿真结果讨论）、第 7 节（区域能源系统设计启示）、结论均缺失。因此**弹性策略相对占用驱动的单独增量数字、详细案例与完整结果分析**无法在本笔记充分体现；笔记中的主结果数字（集中式 5–15%、占用驱动 17–63%）均直接引自摘要，缺失部分已标注。原 AI 笔记把 venue 误标为「Sensors」，实为 arXiv:2210.06124v2（拟投 Building and Environment），已订正；原 `primary_topic` 误归入 CV 目标检测，已改为 `T_通用_NLP_其他`。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页); 但缓存仅含前 12/43 页, 字符上限 25000); 来源缓存: `.paper-cache/extracts/2022_Elastic_buildings_C.txt` (实际仅 12/43 页; p.13-43 见下方全文补读记录的页级线索); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。本次优化订正了 venue（Sensors→arXiv/Building and Environment）与 primary_topic（C2 CV 检测→T_通用_NLP_其他）两处事实性错误。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-43; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-43。
- **提取情况**: 缺失页 31 页, 其中 31 页提取到可读文本。缺失页包含正文/附录内容, 其中约 8 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Finally, during extended unoccupied times, concurrent electricity and cooling loads were
- p.13: 3.3. Occupant modeling
- p.13: Realistic occupancy schedules for the buildings in the case study area during normal operation
- p.13: While the number of devices connected to the WiFi network is an indicator of the number of
- p.13: In order to obtain typical occupancy patterns from the WiFi connection data, an approach
- p.14: 3.4. Scenario assessment
- p.14: The calibrated building energy demand model with realistic occupancy patterns and associ-
- p.14: result of the COVID-19 pandemic. Figure 2 shows the scenarios de
- p.14: Furthermore, three di
- p.14: While reducing space cooling demand, in this case, a signi
- p.14: Part load operation, as introduced in the zone-based occupant-driven scenario, can a
- p.15: Centralized

### 缺失页关键摘录

- p.13: shown to improve the model's prediction accuracy [65].
- p.13: building. Each day in the dataset was assigned an occupancy pattern cluster, and subsequently
- p.14: ated electricity demands was then used for scenario evaluation. Di
- p.14: result of the COVID-19 pandemic. Figure 2 shows the scenarios de
- p.15: Figure 2: Scenario matrix showing the di
- p.17: Figure 3: View of the university campus model in CEA (left) and selected buildings in the present case study
- p.17: Figure 3, which are the only buildings for which electricity and cooling demand, as well as WiFi
- p.17: performance hall. Within this dataset, energy demand and WiFi data for the full three-year
- p.18: As a result of the demand and occupancy patterns observed above, the electricity and cooling
- p.18: cantly, as shown in Figure 5. This would appear to indicate that building systems
- p.18: as the ones seen in Figure 6. These outliers were detected by their Z-score:
- p.18: ve were recursively removed until no value in the dataset
<!-- AI_READING_NOTE_END -->
