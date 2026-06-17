---
title: "Uncovering the Size of the Illegal Corporate Service Provider Industry in the Netherlands: A Network Approach"
authors:
  - "Javier Garcia-Bernardo"
  - "Joost Witteman"
  - "Marilou Vlaanderen"
year: 2021
venue: "arXiv (cs.SI), arXiv:2112.05019"
doi: 
pdf: [[2021_Uncovering_the_Size.pdf]]
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
extract_cache: .paper-cache/extracts/2021_Uncovering_the_Size.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/31 pages"
---
# Uncovering the Size of the Illegal Corporate Service Provider Industry in the Netherlands: A Network Approach

## 基本信息
- **PDF**: [[2021_Uncovering_the_Size.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Uncovering the Size of the Illegal Corporate Service Provider Industry in the Netherlands: A Network Approach |
| **作者** | Javier Garcia-Bernardo (Utrecht University, Methodology & Statistics); Joost Witteman; Marilou Vlaanderen (SEO Amsterdam Economics) |
| **发表时间** | 2021 (arXiv v1 2021-12; v2 2022-03-13) |
| **刊物/会议** | arXiv 预印本, arXiv:2112.05019 [cs.SI] |
| **DOI** | PDF 文本未明确 |

## 摘要

> Economic crimes such as money laundering, terrorism financing, tax evasion or corruption almost invariably involve the use of a corporate entity. Such entities are regularly incorporated and managed by corporate services providers (CSPs). Given this potential for enabling economic crime, the CSP industry in the Netherlands is heavily regulated and CSPs require a license to operate. Operating without a licence is illegal. In this paper, we estimate the size of the illegal CSP sector in the Netherlands. For this, we develop a classification method to detect potentially illegal CSPs based on their similarity with licensed CSPs. Similarity is computed based on their position within the network of directors, companies and addresses, and the characteristics of such entities. We manually annotate a sample of the potential illegal CSPs and estimate that illegal CSPs constitute 31–51% of the total number of CSPs and manage 19–27% of all companies managed by CSPs. Our analysis provides a tool to regulators to improve detection and prevention of economic crime, and can be extended to the estimation of other illegal activities.

**中文翻译**：

> 洗钱、恐怖主义融资、逃税或腐败等经济犯罪几乎无一例外都涉及对企业实体的利用。这类实体通常由企业服务提供商（CSP）注册并管理。鉴于 CSP 可能助长经济犯罪，荷兰对该行业实行严格监管，CSP 必须持牌才能运营，无牌经营即属违法。本文估计荷兰非法 CSP 行业的规模。为此，我们开发了一种分类方法，依据潜在 CSP 与持牌 CSP 的相似性来识别可能的非法 CSP；相似性是根据它们在"董事—公司—地址"网络中的位置及这些实体的特征计算的。我们人工标注了潜在非法 CSP 的一个样本，估计非法 CSP 占 CSP 总数的 31–51%，并管理着 CSP 所管理全部公司的 19–27%。本分析为监管者提供了一个改进经济犯罪检测与预防的工具，并可扩展到对其他非法活动规模的估计。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：企业服务提供商（CSP，荷兰语 "trustkantoren"）负责为客户注册和代管公司，可能（往往是无意地）帮助客户隐藏身份或活动性质，从而助长洗钱、逃税、恐怖融资等经济犯罪。荷兰的 CSP 行业受《2018 信托办公室监管法》（Wtt 2018）约束，提供"代持董事（nominee director）"等五类服务须持牌、须做客户尽职调查（KYC）并接受荷兰央行（DNB）监督。无牌提供这些服务即属非法。
- **现实矛盾**：过去十年监管持续收紧，持牌 CSP 数量下降 46%（2013 年 10 月 192 家 → 2020 年 1 月 103 家），而监管成本上升 216–640%。坊间证据表明持牌 CSP 减少的需求至少部分被无牌（非法）CSP 填补。但因无牌者不受 Wtt 2018 约束（仅受反洗钱法 Wwft 约束），监管更弱，金融犯罪风险更高。
- **之前方法有什么问题**：荷兰超过一百万人担任公司董事，而非法 CSP 可能只有几百到几千人，是典型的"大海捞针"。现有监管依赖检查和信号审查，成本高、难以系统性发现隐藏在普通董事中的非法 CSP；PDF 文本未提及此前有任何对非法 CSP 规模的量化估计方法。
- **核心问题**：监管机构缺乏量化这一地下市场规模的工具。本文旨在提供这样一个基于网络相似性的量化工具。

## 关键贡献

1.  **基于网络相似性的分类框架**：不依赖交易数据或直接举报，而是把董事置于"董事—公司—地址—所有者"网络中，用其二阶（depth-two）自我网络（ego network）的结构与特征，识别行为模式与持牌 CSP 相似的潜在非法个体。其依据的直觉是：管理大量公司、这些公司由外国人持有且注册在同一地址的董事，很可能是 CSP。
2.  **48 个董事级网络指标体系**：指标依据团队专业知识及与行业专家的半结构化访谈/工作坊构建（见表 1 与附录 A.8），按图 1 的实体维度组织——董事自身属性、董事-公司组合（如董事名与公司名相似度）、地址（同址注册公司数/集中度）、公司（管理公司数）、所有者（外国 vs 国内）、所有者与公司联合（独立公司数）。
3.  **算法 + 人工标注的混合验证流程**：先用最近邻找候选，再用惩罚逻辑回归补充验证遗漏，最后人工标注 200 个样本（两个候选集各 100 个）来估算精确率、重叠度并给出 95% 置信区间。
4.  **对非法 CSP 规模的首次定量估计**：估计 2019 年存在 402 个"极高风险"非法 CSP（95% CI 212–668），管理 2,414 家公司（95% CI 1,274–4,012），分别占持牌 CSP（103 家）的 31% 和 CSP 所管理公司的 19%；外推到管理 1–2 家公司的小型 CSP 后，比例升至 38–51% 和 23–27%。
5.  **可迁移的监管"红旗（red-flag）"系统思路**：该方法可作为持续监测工具，也可推广到"已标记部分节点、在未标记节点中找相似者"的一般网络场景，例如金融机构的客户尽职调查（CDD）。

> 注：作者强调"非法"是基于团队专业判断的"极高风险"标签，并非正式的监管或司法裁定；文中以"illegal services"代指"very high risk of offering illegal services"。

## 方法

- **整体框架**（图 2，两阶段）：
    1. **数据清洗与特征工程**（黑色部分）：下载持牌 CSP、公司、董事数据；剔除仅任 1–2 家公司的董事，剩 36,543 名董事并入公司数据构建网络特征；左支对持牌 CSP 做数据增强，最终得 909 个持牌 CSP 实体。
    2. **建模与验证**（彩色部分）：最近邻初筛（红支）→ 惩罚逻辑回归补充验证（蓝支）→ 人工抽样估算 → 合并得 402 (212–668) 的最终估计。
- **输入数据**：
    1. **Orbis（商会 KvK）数据**：1,894,265 家公司及其 1,365,181 名董事；其中 36,543 名董事在至少 3 家公司任职。字段含当前/历史地址、当前/历史董事、NACE rev.2 行业与财务信息、全球最终所有者（GUO）所在地。荷兰用"邮编 + 门牌号"唯一标识地址。
    2. **DNB 持牌 CSP 名单**：246 个持牌 CSP，139 个唯一地址、239 个唯一公司名（用 Google 地理编码补全邮编）。
    3. **离岸泄露数据库（ICIJ）**：504,851 个地址、861,576 个公司名、832,468 名高管、13,203 个中介，来自 Bahamas/Offshore/Paradise leaks。用于给同时出现在 Orbis 与泄露库中的地址/公司/董事打"潜在风险"标记（出现在泄露库不等于违法，但是潜在信号）。
- **关键模块**：
    1.  **持牌 CSP 数据增强（左支，扩到 909）**：
        - (i) **分支机构**：用 KvK 编号匹配 Orbis，匹配到 195 个 CSP，地址扩到 409（+270）、公司名扩到 244（+5）；按名称 + 三元组（trigram）+ TF-IDF 余弦相似度 > 90% 再匹配 9 个实体（共 229 个公司董事，阈值 90% 经迭代校准，如 80% 相似的两家是不同公司、92% 的对应同一集团）。229 个中有 155 个管理 ≥3 家公司。
        - (iia) **CSP 员工**：纳入 229 个公司董事的 493 名董事（假设他们只通过所属 CSP 提供服务），列表增至 648。
        - (iib) **按公司特征识别的额外董事**：用两组重叠标准（>25% 所管公司注册在 DNB 持牌 CSP 办公/邮政地址且 >20% 公司另有持牌 CSP 董事，得 257 例；用增强后地址列表时阈值各 50%，得 5 例）识别出 261 名额外董事。人工标注 100 人测试：iia 中 15/15 确为持牌 CSP 工作；iib 中 5 人里 3 人确认、1 人无法判定、1 人为关联持牌 CSP 但不提供 CSP 服务的中国官员。
        - 最终 **909** 个管理 ≥3 家公司的持牌 CSP，共持有 **17,924** 个董事职位、覆盖 **6,913** 家独立公司（其中 155 个 step (i) CSP 持 6,992 职位，493 个 step (iia) CSP 持 8,700 职位，262 个 step (iib) 董事持 2,223 职位）。
    2.  **普通董事过滤**：把仅任 1–2 家公司的董事剔除以降噪，得 36,543 名董事进入分析（4.3 节再外推到小型董事）。
    3.  **网络特征（48 指标）**：基于每位董事 depth-two 的 ego 网络计算（董事 X、其所管公司、这些公司的地址/所有者/其他董事），见图 1、表 1。
    4.  **分类与验证算法**：
        - **最近邻（主方法）**：对每个持牌 CSP 找其 100 个最近邻董事，保留落在 ≥3 个持牌 CSP 的 100-近邻内的董事，得 **2,944** 名候选；人工标注 100 个估算其中含 **161–572** 个非法 CSP。
        - **惩罚逻辑回归（验证）**：正例为持牌 CSP，负例为"生产性行业"的公司董事（即 NACE rev.2 全部行业，排除 64–66 金融保险、69 法律会计、70 总部/管理咨询、82 办公行政支持；图 2 标注创建了 1,551 个 NON-CSP 例）。用全样本预测得 **3,677** 个新候选，人工标注 100 个估算主方法漏掉 **9–199** 个非法 CSP。
        - **人工标注**：两候选集各随机抽 100 人，借助个人/公司网站、LinkedIn、庭审记录等核实，用于估精确率、两集合重叠与置信区间。
- **与已有方法的差异**：核心在于**不依赖直接证据（如交易记录），而从行为模式"相似性"推断**——把监管已知的"好样本"（持牌 CSP）当锚点，在百万级社会网络中搜索行为特征相似的节点，是一种类正例/单类分类思想在网络数据上的应用。利用网络实体间关系检测经济犯罪在文献中已有先例（文中引 [18–21]）。

## 实验

- **数据集**：Orbis（公司/董事/地址/所有权）为主，辅以 DNB 持牌 CSP 名单和 ICIJ 离岸泄露数据库。
- **对比设置**：主要是**最近邻**与**惩罚逻辑回归**两种方法的相互验证与互补，而非与外部基线模型对比。
- **评价指标**：候选董事数、估计非法 CSP 总数及 95% 置信区间、管理公司数、占持牌 CSP 总数与 CSP 管理公司总数的百分比。
- **主结果**：
    - 最近邻：2,944 候选 → 161–572 个非法 CSP。
    - 逻辑回归：3,677 新候选 → 9–199 个（主方法遗漏部分）。
    - 综合：2019 年非法 CSP **402** 家（95% CI 212–668），管理 **2,414** 家公司（95% CI 1,274–4,012），占持牌 CSP（103 家）的 **31%**、占 CSP 管理公司的 **19%**。
    - （据原文后续页，提取缓存未覆盖，待核）p.13–14 Figure 4/5 给出更细的董事/职位/公司分布：非法 CSP 持有约 3,186 个董事职位、管理 2,414 家公司（其中 1,623 家独立公司），而持牌 CSP 对应 17,917 职位 / 10,168 公司 / 6,913 独立公司——非法 CSP 普遍规模更小。
- **稳健性 / 外推**：
    - 剔除经 step (iib) 纳入的董事后，算法检出的潜在 CSP 仍保留 **86%（3,277/3,830）**，说明方法对 CSP 定义扩展有一定鲁棒性。
    - 外推到管理 1–2 家公司的**小型非法 CSP** 后，非法 CSP 比例升至 **38–51%**、管理公司比例升至 **23–27%**。
    - （据原文后续页 p.18，提取缓存未覆盖，待核）真正例率（true positive rate）约 11% 偏低、假阳性较多；并讨论"若实际存在 330 个非法 CSP，精度需提升约 11 倍"一类的精度边界论述。
- **效率信息**：PDF 文本未明确说明计算时间、参数量或 FLOPs 等。本文为社会网络/统计建模工作，效率非其评价重点。

## 局限

1.  **"相似性"不等于"非法性"**：基于与持牌 CSP 的模式相似性会带来**假阳性**——合法的公司秘书、持大量股份的职业经理人，其网络特征可能与 CSP 相似但并不提供需牌照的服务。（据原文 p.18，提取缓存未覆盖，待核）作者自陈真正例率约 11%、假阳性较多。
2.  **违法判定依据专家知识而非审计**：（据原文 p.18，提取缓存未覆盖，待核）"非法"标签来自作者团队判断而非正式审计/司法裁定，本质是"极高风险"而非确证违法。
3.  **依赖公开数据，信息可能不完整**：数据来自商会等公开注册系统，难以覆盖未注册地址、隐藏实控人或复杂代理安排，可能**遗漏完全隐藏的非法活动**；且仅凭公开数据难以区分"只服务一家公司的 CSP"与自由职业者（故剔除 1–2 职位董事）。
4.  **人工标注成本高且主观**：核实 200 个样本需大量专家精力，灰色地带案例（是否属"需牌照服务"）存在主观差异，影响精确度。
5.  **小型 CSP 外推假设**：对管理 1–2 家公司的小型 CSP 的外推，基于"它们与大型 CSP 特征相似"的假设，文中（提取缓存覆盖范围内）未充分验证，外推结果有不确定性。

## 个人评论

1.  **将监管知识转化为可计算特征**：论文把"什么是可疑 CSP 行为"的经验直觉，系统编码成 48 个可量化网络特征。这种**领域知识驱动的特征工程**是它在缺乏大量标注数据时仍能成功的关键，对任何用 AI 解决特定领域问题的项目都有启发。
2.  **"已知找未知"的实用范式**：用少量高质量"白名单"（持牌 CSP），通过网络行为相似性大规模扫描潜在"黑名单"，比从零构建异常检测模型更可行，且天然契合监管现状（监管者手里就有持牌名单）。
3.  **诚实而严谨的混合验证**：不完全依赖单一模型输出，而是**两种算法互验 + 人工抽样核实**，并坦承约 11% 的真正例率与假阳性问题。把"高风险"与"确证违法"明确区分，这种不夸大结论的克制在政策类研究中尤为可贵。
4.  **问题定义清晰、答案有政策价值**：直接回答政策制定者关心的量化问题（"非法 CSP 到底有多少？"），并给出带置信区间的区间估计，对监管资源分配和政策评估有直接指导意义。
5.  **可借鉴的方法论模板**：数据增强（分支/员工/按特征三类）、负样本构造（生产性行业公司董事）、外推到小型实体——这套"把监管对象边界一点点补全"的工程化做法，对壳公司识别、洗钱网络挖掘等相邻任务可直接复用。

### 使用建议

- **如果快速了解**：读**摘要 + 引言末段（402/2,414/31%/19% 那段）+ 第 5 节结论**，即可掌握核心问题、方法与关键结果。
- **如果复现**：重点读**第 3 节（数据与方法）**，尤其 3.1（数据与 909 持牌 CSP 的三步增强）和 3.2（48 特征 + depth-two ego 网络）；建模（最近邻 + 惩罚逻辑回归）相对标准，但要注意其独特的双方法互验与人工标注流程。
- **如果借鉴创新点**：学习**领域知识 → 网络特征**（地址集中度、所有权国籍分布等）与**白名单引导的相似性搜索**范式，可迁移到壳公司/洗钱网络/客户尽职调查等图异常检测任务。
- **如果写 related work**：可归入**经济犯罪检测（反洗钱）**、**社会网络分析在金融监管中的应用**、或**基于图的异常检测/RegTech**类别引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**计算社会科学 / 社会网络分析 / 经济犯罪检测（RegTech）** 的交叉领域，发表为 arXiv 预印本（cs.SI, arXiv:2112.05019, v2 2022-03）。它解决一个具体的实证问题：量化估计荷兰**非法（无牌）企业服务提供商（CSP）** 行业的规模。方法上建模为"在已知部分节点（持牌 CSP）的前提下，识别网络中与其行为相似的未标记节点（潜在非法 CSP）"，本质是网络上的类正例/单类分类。它与计算机视觉无关，在本库中归入通用/其他类（`T_通用_NLP_其他`）是恰当的——更准确的标签应是"网络异常检测 / 反金融犯罪 / 监管科技"。

## 2. 一句话总结
论文用董事在"公司—地址—所有者"网络中的二阶 ego 网络特征（48 个指标）度量其与持牌 CSP 的相似性，结合最近邻与惩罚逻辑回归两套算法并辅以 200 个样本的人工标注，估计 2019 年荷兰有约 402 个（外推后占 31%–51%）非法 CSP，管理约 2,414 家公司（占 19%–27%）。

## 3. 背景与问题
- **为什么要做**：CSP 可能被用于洗钱、逃税、恐怖融资等经济犯罪。荷兰对 CSP 实行持牌监管（Wtt 2018，DNB 监督）。十年监管收紧使持牌 CSP 从 192 家（2013-10）降至 103 家（2020-01，降 46%），监管成本上升 216–640%，需求疑似流向无牌（非法）CSP，金融犯罪风险上升。
- **之前方法有什么问题**：荷兰逾百万人担任董事，非法 CSP 仅几百到几千，是"大海捞针"。现有监管靠检查与信号审查，成本高、难系统性发现。PDF 文本未提及此前有量化方法。
- **核心矛盾**：严监管推高合规成本、把部分市场逼向地下，而监管者缺乏量化地下市场规模的工具。本文提供这样一个工具。

## 4. 核心贡献
1.  **网络相似性分类框架**：不靠交易数据/举报，而靠董事在"董事—公司—地址—所有者"网络中的二阶 ego 网络结构与特征，找出与持牌 CSP"足够相似"的高风险个体。
2.  **48 个董事级网络指标**：基于专家知识与行业访谈构建，覆盖董事属性、董事-公司组合、地址集中度、公司数、所有者国籍、独立公司数等维度。
3.  **算法 + 人工的混合验证**：最近邻初筛 → 惩罚逻辑回归补漏 → 人工标注 200 个样本估精确率、重叠与 95% 置信区间。
4.  **首次定量估计**：2019 年约 402 个非法 CSP（CI 212–668）管理 2,414 家公司（CI 1,274–4,012），占 31% / 19%；外推到小型 CSP 后升至 38–51% / 23–27%。
5.  **可迁移的红旗系统**：可作持续监测工具，并推广到"已标记部分节点、找相似未标记节点"的一般场景（如客户尽职调查）。

## 5. 方法详解
- **两阶段框架（图 2）**：数据清洗与特征工程（黑）→ 建模与验证（彩）。
- **输入**：① Orbis 数据 1,894,265 家公司 + 1,365,181 名董事（36,543 名任职 ≥3 家）；② DNB 持牌 CSP 246 个（139 地址、239 公司名）；③ ICIJ 离岸泄露库（504,851 地址 / 861,576 公司名 / 832,468 高管 / 13,203 中介），用于打潜在风险标记。
- **持牌 CSP 增强（→909）**：
    - (i) 分支：KvK 编号匹配 195 个 CSP，地址扩到 409、公司名扩到 244；名称 TF-IDF（trigram）>90% 再加 9 个，共 229（155 个管理 ≥3 家）。
    - (iia) 员工：纳入 229 个公司董事的 493 名董事 → 648。人工核 15/15 命中。
    - (iib) 按特征识别 261 名额外董事（同址 + 同伴董事比例阈值）；人工核 5 人中 3 确认。
    - 最终 **909** 个持牌 CSP，持 **17,924** 个董事职位、覆盖 **6,913** 家独立公司（155 个持 6,992、493 个持 8,700、262 个持 2,223）。
- **普通董事过滤**：剔除 1–2 职位董事，留 36,543 名。
- **48 特征**：基于 depth-two ego 网络（董事 X + 所管公司 + 这些公司的地址/所有者/其他董事），按图 1 实体维度组织（表 1）。
- **分类与验证**：
    - **最近邻（主）**：每个持牌 CSP 取 100 近邻，保留落在 ≥3 个持牌 CSP 的 100-近邻内者 → **2,944** 候选 → 人工标 100 估 **161–572** 个非法 CSP。
    - **惩罚逻辑回归（验证）**：正例=持牌 CSP，负例=生产性行业公司董事（NACE 排除 64–66、69、70、82；创建 1,551 个 NON-CSP 例）→ **3,677** 新候选 → 估主方法漏 **9–199** 个。
    - **人工标注**：两集各抽 100 人，借个人/公司网站、LinkedIn、庭审记录核实。
- **与已有方法差异**：不依赖直接证据而靠"相似性"推断；以监管已知"好样本"为锚点在大规模网络中搜相似节点（类正例/单类分类）。

## 6. 实验与结果
- **数据集**：Orbis 为主，DNB 名单 + ICIJ 泄露库为辅。
- **对比**：最近邻 vs 惩罚逻辑回归互验互补，无外部基线对比。
- **指标**：候选数、估计总数 + 95% CI、管理公司数、占比。
- **主结果**：最近邻 2,944 候选 → 161–572；逻辑回归 3,677 新候选 → 9–199；综合 **402**（CI 212–668）非法 CSP，管理 **2,414** 家（CI 1,274–4,012），占持牌 CSP（103 家）**31%**、占 CSP 管理公司 **19%**。
- **后续页细节**（据原文 p.13–14，提取缓存未覆盖，待核）：Figure 4/5 给出董事职位/公司/独立公司分布——非法 CSP 约 3,186 职位 / 2,414 公司 / 1,623 独立公司，持牌 CSP 约 17,917 职位 / 10,168 公司 / 6,913 独立公司，非法 CSP 规模普遍更小；两方法标记的董事集合高度重叠（混淆矩阵 Fig.4C）。
- **稳健性/外推**：剔除 step (iib) 董事后仍保留 86%（3,277/3,830）检出；外推到管理 1–2 家公司的小型 CSP 后比例升至 **38–51%** / **23–27%**。
- **精度边界**（据原文 p.18，提取缓存未覆盖，待核）：真正例率约 11%、假阳性较多。
- **效率信息**：PDF 文本未明确（计算时间/参数量/FLOPs），本文非以效率为评价重点。

## 7. 这篇论文真正有价值的地方
1.  **领域知识 → 可计算特征**：把"可疑 CSP 行为"的经验编码为 48 个量化网络特征，是在缺标注数据下取得结果的关键，对领域 AI 项目有普适启发。
2.  **"已知找未知"实用范式**：用持牌名单这一现成"白名单"做锚点扫描潜在黑名单，比从零做异常检测更可落地，且贴合监管现状。
3.  **诚实而严谨的混合验证**：双算法互验 + 人工抽样，并主动披露 ~11% 真正例率与假阳性，明确区分"高风险"与"确证违法"，不夸大结论。
4.  **问题清晰、答案有政策价值**：给出带置信区间的区间估计，直接服务于监管资源分配与政策评估。

## 8. 局限与问题
1.  **相似 ≠ 非法**：模式相似带来假阳性（合法公司秘书、职业经理人特征可能近似 CSP）；作者自陈真正例率约 11%（据原文 p.18，提取缓存未覆盖，待核）。
2.  **违法判定靠专家而非审计**：标签是"极高风险"而非司法/审计确证（据原文 p.18，待核）。
3.  **依赖公开数据**：可能遗漏未注册地址、隐藏实控人、复杂代理；难区分单公司 CSP 与自由职业者（故剔除 1–2 职位董事）。
4.  **人工标注成本高且主观**：核 200 样本耗专家精力，灰色地带判断有主观性。
5.  **小型 CSP 外推假设未充分验证**：外推基于"小型与大型 CSP 特征相似"的假设，提取覆盖范围内未见充分验证。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要 + 引言末段 + 第 5 节结论。
- **复现**：重点第 3 节，尤其 3.1（数据与 909 三步增强）、3.2（48 特征 + depth-two ego 网络）；注意双方法互验 + 人工标注流程。
- **借鉴创新点**：学领域知识 → 网络特征、白名单引导的相似性搜索；可迁移到壳公司/洗钱网络/客户尽职调查等图异常检测。
- **写 related work**：归入经济犯罪检测（反洗钱）、社会网络分析在金融监管中的应用、或基于图的异常检测 / RegTech。

## 10. 和其他论文的关系
本文是网络分析 / 计算社会科学工作，与库内 CV/NLP 论文无直接方法继承关系。其核心思想——利用网络结构关系进行推理与异常检测——与图表示学习、网络嵌入、图异常检测有概念关联；引言也指出利用网络实体间关系检测经济犯罪在文献中已有先例（文中引 [18–21]）。库内若有图表示学习/社交网络分析相关笔记可作概念性对照，但 PDF 文本未给出可直接链接的具体论文，故不做不确切链接。

## 11. 关键词
经济犯罪, 反洗钱, 企业服务提供商(CSP/trustkantoren), 荷兰, 社会网络分析, 监管科技(RegTech), 二阶 ego 网络, 特征工程, 最近邻, 惩罚逻辑回归, 相似性度量, 图异常检测, 类正例分类, 政策评估

## 12. 可信度说明
本精读基于 PDF 提取文本生成。提取缓存实际仅覆盖到正文第 8 页（截断于 25,000 字符、第 3.2 节中段），头部标注 12/31 页。引言、监管背景（第 2 节）、数据与方法（3.1–3.2，含 909 持牌 CSP 的三步增强、48 特征、最近邻 + 逻辑回归、各项数字）均来自提取文本明确表述，已逐一核对。第 4 节结果的细分数字（Figure 4/5 的 3,186 / 10,168 / 1,623 等）和第 5 节结论、约 11% 真正例率等取自原笔记"全文补读记录"中对 p.13–18 的摘录，**提取缓存未覆盖、标注为待核**。"局限/价值/个人评论"中超出提取文本的部分为基于现有文本的合理分析。整体提取质量良好，关键数字均按原文引用。

---

> **可信度补充**: PDF 提取质量 = **high** (提取缓存覆盖正文 p.1-8, 截断于 25,000 字符; 头部标注 12/31 页); 来源缓存: `.paper-cache/extracts/2021_Uncovering_the_Size.txt`; p.13-31 数字据原笔记全文补读记录, 待核; 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-31; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-31。
- **提取情况**: 缺失页 19 页, 其中 18 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 4 Results and Discussion
- p.13: 4.1 Size of the illegal and legal sector
- p.13: Licensed
- p.14: Number of positionsLicensed CSPs
- p.14: Illegal CSPs 3,186 positions 17,917 positions (A)
- p.14: Number of companiesLicensed CSPs
- p.14: Illegal CSPs 2,414 companies 10,168 companies (B)
- p.14: Number of independent companiesLicensed CSPs
- p.14: Illegal CSPs 1,623 companies 6,913 companies (C)
- p.14: Figure 5: Number of (A) directorship position held (B) companies serviced (C) independent companies serviced by
- p.14: 4.2 Characteristics of the illegal CSP sector
- p.15: 4.3 Validation and robustness tests

### 缺失页关键摘录

- p.13: Figure 4 summarizes the application of our estimation methodology (depicted in Fig. 2) at the director level. Out of the
- p.13: accuracy would need to be 11 times larger. Assuming that there actually exist 330 illegal CSPs in the Netherlands,
- p.13: Figure 4: Number of directors ﬂagged and validated in our approach. (A) The nearest neighbor approach (red) identiﬁes
- p.14: methods ﬂag a similar set of directors, as reﬂected in the overlap in Figure 4A and the confusion matrix in Figure 4C.
- p.14: if a director was a CSP or not (dark gray bars in Figure 4B), this market share can be considered as a lower bound.
- p.14: Figure 5 visualizes the number of companies serviced by both licensed and illegal CSPs. Illegal CSPs operate on a
- p.14: Figure 5: Number of (A) directorship position held (B) companies serviced (C) independent companies serviced by
- p.15: robust to outliers. We show the average value of the normalized features in Figure 6. We found that, compared with the
- p.17: of licensed CSPs in Figure 7, gray lines). This implies that the decay should be more pronounced than the estimated
- p.17: Figure 7: Extrapolation to smaller companies for the sample of licensed CSPs downloaded from the DNB (light gray),
- p.18: limitation arises from the assessment of illegality based on the authors’ knowledge instead of an audit process carried
- p.18: the number of false positives. As a result, our true positive rate was relatively low, at around 11%. In a situation
<!-- AI_READING_NOTE_END -->
