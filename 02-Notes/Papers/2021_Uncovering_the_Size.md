---
title: JavierGarcia-Bernardo JoostWitteman,MarilouVlaanderen
authors:
  - "JavierGarcia-Bernardo JoostWitteman"
  - "MarilouVlaanderen"
  - "UtrechtUniversity"
  - "theNetherlands Amsterdam"
  - "theNetherlands"
year: 2021
venue: "arXiv"
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
# JavierGarcia-Bernardo JoostWitteman,MarilouVlaanderen

## 基本信息
- **PDF**: [[2021_Uncovering_the_Size.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | JavierGarcia-Bernardo JoostWitteman,MarilouVlaanderen |
| **作者** | JavierGarcia-Bernardo JoostWitteman; MarilouVlaanderen; UtrechtUniversity; theNetherlands Amsterdam; theNetherlands |
| **发表时间** | 2021 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Economiccrimessuchasmoneylaundering,terrorismfinancing,taxevasionorcorruptionalmost invariablyinvolvetheuseofacorporateentity. Suchentitiesareregularlyincorporatedandmanaged bycorporateservicesproviders(CSPs). Giventhispotentialforenablingeconomiccrime,theCSP industryintheNetherlandsisheavilyregulatedandCSPsrequirealicensetooperate. Operating without a licence is illegal. In this paper, we estimate the size of the illegal CSP sector in the Netherlands. Forthis,wedevelopaclassificationmethodtodetectpotentiallyillegalCSPsbasedon theirsimilaritywithlicensedCSPs. Similarityiscomputedbasedontheirpositionwithinthenetwork ofdirectors,companiesandaddresses,andthecharacteristicsofsuchentities. Wemanuallyannotate asampleofthepotentialillegalCSPsandestimatethatillegalCSPsconstitute31–51%ofthetotal numberofCSPsandmanage19–27%ofallcompaniesmanagedbyCSPs. Ouranalysisprovidesa tooltoregulatorstoimprovedetectionandpreventionofeconomiccrime,andcanbeextendedtothe estimationofotherillegalactivities.

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：企业服务提供商（CSP）可能被用于洗钱、逃税等经济犯罪。荷兰的CSP行业受到严格监管，需要持牌运营。然而，监管收紧导致持牌CSP数量减少（从192家降至103家），但有证据表明部分需求可能被非法（无牌）CSP填补。非法CSP的规模未知，对金融犯罪构成潜在风险。
- **之前方法有什么问题**：PDF文本中未明确说明此前用于估计非法CSP规模的具体量化方法。现有监管主要依赖检查和信号审查，成本高昂且可能无法系统性地发现“隐藏”在众多普通董事中的非法CSP，如同“大海捞针”。
- **核心矛盾**：**监管目标是遏制经济犯罪，但严厉监管可能导致合规成本上升，促使部分市场转向地下（非法）运营，而监管机构缺乏有效的工具来量化这一地下市场的规模。** 论文旨在提供这样一个量化工具。
## 关键贡献

1.  **提出一个基于网络相似性的分类框架**：该框架不依赖于交易数据或直接举报，而是通过分析董事在“董事-公司-地址-所有者”网络中的结构位置和特征，来识别其行为模式与持牌CSP相似的潜在非法个体。
2.  **开发了一套包含48个特征的网络指标体系**：这些特征从董事的二阶自我网络中提取，涵盖董事自身属性、所管理公司的特征、地址集中度、所有者国籍分布等多个维度，为相似性度量提供了全面基础。
3.  **设计了一个结合算法与人工标注的验证流程**：先用最近邻算法找到候选者，再用惩罚逻辑回归进行补充验证，最后通过人工标注200个样本来校准和估算最终规模，并给出了置信区间。
4.  **对非法CSP行业规模给出了首次定量估计**：估计2019年存在402个高风险非法CSP，管理2414家公司，分别占持牌CSP和公司总数的31%和19%；并外推考虑小型非法CSP后，比例升至38-51%和23-27%。
5.  **提供了一种可扩展的监管“红旗”系统思路**：该网络分析方法可作为监测工具，用于持续发现CSP行业中的异常模式，并可迁移到客户尽职调查等其他反金融犯罪场景。
## 方法

- **整体框架**：方法分为两大阶段（如论文图2所示）：1）**数据清洗与特征工程**：获取并整合公司、董事、地址、持牌CSP数据，构建网络特征；2）**建模与验证**：利用最近邻算法初筛，再用逻辑回归验证，最后人工抽样估算。
- **输入**：1）商会（Orbis）数据：1,894,265家公司及其1,365,181名董事；2）荷兰中央银行（DNB）发布的246家持牌CSP名单；3）离岸泄露数据库（用于风险标记）。
- **输出**：一个高风险非法CSP列表及其管理的公司数量估计值。
- **关键模块**：
    1.  **数据增强与清洗**：
        - 对持牌CSP：通过公司ID匹配分支机构，通过名称相似度（三元组+TF-IDF余弦相似度>90%）匹配关联实体，并纳入其董事，最终扩充至**909**个持牌CSP实体。
        - 对普通董事：剔除仅担任1-2家公司董事的个体，剩余**36,543**名董事进入分析，以降低噪声。
    2.  **网络特征构建**：计算每位董事二阶自我网络的**48个特征**（见表1），例如：
        - 董事特征：是个人还是法人实体。
        - 公司组合特征：管理的公司数量、公司名称与董事名称的相似度。
        - 地址特征：管理的公司注册在同一地址的比例（地址集中度）。
        - 所有者特征：公司全球最终所有者（GUO）为外国的比例。
        - 跨实体特征：董事管理的独立公司数量。
    3.  **分类与验证**：
        - **最近邻方法（主要）**：计算每个普通董事与909个持牌CSP的特征空间距离，找出其100个最近邻中至少包含3个持牌CSP的董事，作为候选非法CSP（**2,944**名）。
        - **惩罚逻辑回归（验证）**：使用持牌CSP作为正例，**生产性行业的公司董事**作为负例训练模型，在剩余董事中找到新的潜在候选者（**3,677**名），用于评估最近邻方法的遗漏率。
        - **人工标注**：分别在上述两个候选集中随机抽取100人进行人工核实（参考个人网站、LinkedIn、庭审记录等），以估计候选集的精确率和两个集合的重叠情况。
- **推理流程**：首先用最近邻模型对全体董事打分并筛选；然后用逻辑回归模型独立筛选，并与前者结果对比；最后将两者的估计结果合并，并考虑小型CSP（管理1-2家公司）进行外推，得到最终规模估计。
- **与已有方法的差异**：该方法的核心差异在于**不依赖直接证据（如交易记录），而是从行为模式的“相似性”进行推断**。它将监管已知的“好样本”（持牌CSP）作为锚点，在大规模社会网络中搜索具有类似“行为特征”的节点，这是一种典型的**正例分类**或**单类分类**思想在网络数据中的应用。
## 实验

- **数据集**：主要数据来自Orbis（公司、董事、地址、所有权数据），辅以DNB的持牌CSP名单和国际调查记者联盟的离岸泄露数据库。
- **对比方法**：论文的主要对比是**最近邻算法**和**惩罚逻辑回归**两种方法之间的相互验证与补充，并非与外部基线模型对比。
- **评价指标**：候选CSP的数量、预估非法CSP总数及其**95%置信区间**、管理公司数量、占持牌CSP总数和管理公司总数的百分比。
- **主实验结果**：
    - 通过最近邻方法找到2,944名候选董事，人工标注估算其中包含**161-572**家非法CSP。
    - 通过逻辑回归方法找到3,677名新候选董事，人工标注估算其中包含**9-199**家非法CSP，而这些新候选者中有大部分（未明确具体数字）未被最近邻方法覆盖。
    - 综合估计，2019年非法CSP总数为**402家**（95% CI: 212-668），管理**2,414家**公司（95% CI: 1,274-4,012）。这分别占当时持牌CSP（103家）的**31%** 和CSP管理公司总数的**19%**。
- **消融/外推实验**：论文尝试了剔除部分通过数据增强纳入的CSP（步骤iib），结果发现模型检测出的候选CSP中仍有86%被保留，说明方法对CSP定义的扩展具有一定鲁棒性。此外，论文将结果**外推至包括管理1-2家公司的小型CSP**，估计非法CSP比例上升至**38-51%**，管理公司比例上升至**23-27%**。
- **效率信息**：PDF文本中未明确说明计算时间、参数量或FLOPs等效率信息。
## 局限

1.  **“相似性”不等于“非法性”**：方法基于与持牌CSP的模式相似性，这可能导致**假阳性**。例如，一些合法的公司秘书或持有大量股份的职业经理人，其网络特征可能与CSP相似，但并非提供需要牌照的服务。
2.  **依赖公开数据，信息可能不完整**：数据来源于商会等公开注册系统，可能不包含未注册的地址、隐藏的实际控制人或复杂的代理安排，从而**遗漏部分完全隐藏的非法活动**。
3.  **人工标注成本高且存在主观性**：核实200个样本需要大量专家精力，且对于处于灰色地带的案例，判断是否为“需要牌照的服务”可能存在主观差异，影响估计的精确度。
4.  **外推假设的局限性**：对管理1-2家公司的“小型CSP”的规模外推，基于“它们与大型CSP特征相似”的假设，但文中未提供验证。小型CSP的行为模式可能不同，导致外推结果存在不确定性。
## 个人评论

1.  **将监管知识转化为可计算特征**：论文将“什么是可疑CSP行为”这一直觉和经验，系统性地编码成了48个可量化的网络特征。这种**领域知识驱动的特征工程**是其在没有大量标注数据情况下取得成功的关键，对任何应用AI解决特定领域问题的项目都有启发。
2.  **“已知找未知”的实用范式**：它展示了一种在监管场景下非常实用的思路：利用少量高质量的“白名单”（持牌CSP），通过网络行为相似性来大规模扫描潜在的“黑名单”。这比从零开始构建一个异常检测模型更可行。
3.  **严谨的混合验证设计**：它没有完全依赖模型输出，而是结合了**多种算法相互验证**和**必不可少的人工抽样核实**，这提高了研究结论的可靠性，也为实际应用中的结果评估提供了方法论参考。
4.  **问题定义清晰，答案有实际价值**：它直接回答了政策制定者关心的量化问题（“非法CSP到底有多少？”），并给出了有置信区间的估计。这种研究对公共政策评估和监管资源分配有直接指导意义。

### 使用建议

- **如果快速了解**：只读**摘要**和**第5节（结论）**，即可掌握论文的核心问题、方法和关键结果。
- **如果复现**：重点阅读**第3节（数据与方法）**，特别是3.1（数据）和3.2（特征构建）部分，理解数据来源、清洗步骤和48个特征的定义。建模部分相对标准，但需注意其独特的验证流程。
- **如果借鉴创新点**：应该学习其**将领域知识转化为网络特征的思路**（如地址集中度、所有权国籍分布等），以及**“白名单”引导的相似性搜索**这一混合方法范式。这可用于其他网络异常检测任务（如识别壳公司、洗钱网络）。
- **如果写related work**：可将其放在**经济犯罪检测**（尤其是反洗钱）、**社会网络分析在金融监管中的应用**、或**基于图的异常检测**这些类别下进行引述。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**计算社会科学、社会网络分析和经济犯罪检测**的交叉领域。它主要解决一个具体的实际问题：量化估计荷兰非法企业服务提供商（CSP）行业的规模。该方法基于网络分析和机器学习分类，将问题建模为在已知部分节点（持牌CSP）的情况下，识别网络中与其相似的未标记节点（潜在非法CSP）。因此，它适合放在**网络异常检测、金融犯罪分析或监管科技（RegTech）** 的主题下。

## 2. 一句话总结
这篇论文提出了一种基于网络特征相似性的分类方法，通过比较董事在公司、地址、所有者构成的网络中的位置，来识别并估计荷兰非法企业服务提供商的规模，发现其可能占该行业总量的31%-51%。

## 3. 背景与问题
- **为什么要做**：企业服务提供商（CSP）可能被用于洗钱、逃税等经济犯罪。荷兰的CSP行业受到严格监管，需要持牌运营。然而，监管收紧导致持牌CSP数量减少（从192家降至103家），但有证据表明部分需求可能被非法（无牌）CSP填补。非法CSP的规模未知，对金融犯罪构成潜在风险。
- **之前方法有什么问题**：PDF文本中未明确说明此前用于估计非法CSP规模的具体量化方法。现有监管主要依赖检查和信号审查，成本高昂且可能无法系统性地发现“隐藏”在众多普通董事中的非法CSP，如同“大海捞针”。
- **核心矛盾**：**监管目标是遏制经济犯罪，但严厉监管可能导致合规成本上升，促使部分市场转向地下（非法）运营，而监管机构缺乏有效的工具来量化这一地下市场的规模。** 论文旨在提供这样一个量化工具。

## 4. 核心贡献
1.  **提出一个基于网络相似性的分类框架**：该框架不依赖于交易数据或直接举报，而是通过分析董事在“董事-公司-地址-所有者”网络中的结构位置和特征，来识别其行为模式与持牌CSP相似的潜在非法个体。
2.  **开发了一套包含48个特征的网络指标体系**：这些特征从董事的二阶自我网络中提取，涵盖董事自身属性、所管理公司的特征、地址集中度、所有者国籍分布等多个维度，为相似性度量提供了全面基础。
3.  **设计了一个结合算法与人工标注的验证流程**：先用最近邻算法找到候选者，再用惩罚逻辑回归进行补充验证，最后通过人工标注200个样本来校准和估算最终规模，并给出了置信区间。
4.  **对非法CSP行业规模给出了首次定量估计**：估计2019年存在402个高风险非法CSP，管理2414家公司，分别占持牌CSP和公司总数的31%和19%；并外推考虑小型非法CSP后，比例升至38-51%和23-27%。
5.  **提供了一种可扩展的监管“红旗”系统思路**：该网络分析方法可作为监测工具，用于持续发现CSP行业中的异常模式，并可迁移到客户尽职调查等其他反金融犯罪场景。

## 5. 方法详解
- **整体框架**：方法分为两大阶段（如论文图2所示）：1）**数据清洗与特征工程**：获取并整合公司、董事、地址、持牌CSP数据，构建网络特征；2）**建模与验证**：利用最近邻算法初筛，再用逻辑回归验证，最后人工抽样估算。
- **输入**：1）商会（Orbis）数据：1,894,265家公司及其1,365,181名董事；2）荷兰中央银行（DNB）发布的246家持牌CSP名单；3）离岸泄露数据库（用于风险标记）。
- **输出**：一个高风险非法CSP列表及其管理的公司数量估计值。
- **关键模块**：
    1.  **数据增强与清洗**：
        - 对持牌CSP：通过公司ID匹配分支机构，通过名称相似度（三元组+TF-IDF余弦相似度>90%）匹配关联实体，并纳入其董事，最终扩充至**909**个持牌CSP实体。
        - 对普通董事：剔除仅担任1-2家公司董事的个体，剩余**36,543**名董事进入分析，以降低噪声。
    2.  **网络特征构建**：计算每位董事二阶自我网络的**48个特征**（见表1），例如：
        - 董事特征：是个人还是法人实体。
        - 公司组合特征：管理的公司数量、公司名称与董事名称的相似度。
        - 地址特征：管理的公司注册在同一地址的比例（地址集中度）。
        - 所有者特征：公司全球最终所有者（GUO）为外国的比例。
        - 跨实体特征：董事管理的独立公司数量。
    3.  **分类与验证**：
        - **最近邻方法（主要）**：计算每个普通董事与909个持牌CSP的特征空间距离，找出其100个最近邻中至少包含3个持牌CSP的董事，作为候选非法CSP（**2,944**名）。
        - **惩罚逻辑回归（验证）**：使用持牌CSP作为正例，**生产性行业的公司董事**作为负例训练模型，在剩余董事中找到新的潜在候选者（**3,677**名），用于评估最近邻方法的遗漏率。
        - **人工标注**：分别在上述两个候选集中随机抽取100人进行人工核实（参考个人网站、LinkedIn、庭审记录等），以估计候选集的精确率和两个集合的重叠情况。
- **推理流程**：首先用最近邻模型对全体董事打分并筛选；然后用逻辑回归模型独立筛选，并与前者结果对比；最后将两者的估计结果合并，并考虑小型CSP（管理1-2家公司）进行外推，得到最终规模估计。
- **与已有方法的差异**：该方法的核心差异在于**不依赖直接证据（如交易记录），而是从行为模式的“相似性”进行推断**。它将监管已知的“好样本”（持牌CSP）作为锚点，在大规模社会网络中搜索具有类似“行为特征”的节点，这是一种典型的**正例分类**或**单类分类**思想在网络数据中的应用。

## 6. 实验与结果
- **数据集**：主要数据来自Orbis（公司、董事、地址、所有权数据），辅以DNB的持牌CSP名单和国际调查记者联盟的离岸泄露数据库。
- **对比方法**：论文的主要对比是**最近邻算法**和**惩罚逻辑回归**两种方法之间的相互验证与补充，并非与外部基线模型对比。
- **评价指标**：候选CSP的数量、预估非法CSP总数及其**95%置信区间**、管理公司数量、占持牌CSP总数和管理公司总数的百分比。
- **主实验结果**：
    - 通过最近邻方法找到2,944名候选董事，人工标注估算其中包含**161-572**家非法CSP。
    - 通过逻辑回归方法找到3,677名新候选董事，人工标注估算其中包含**9-199**家非法CSP，而这些新候选者中有大部分（未明确具体数字）未被最近邻方法覆盖。
    - 综合估计，2019年非法CSP总数为**402家**（95% CI: 212-668），管理**2,414家**公司（95% CI: 1,274-4,012）。这分别占当时持牌CSP（103家）的**31%** 和CSP管理公司总数的**19%**。
- **消融/外推实验**：论文尝试了剔除部分通过数据增强纳入的CSP（步骤iib），结果发现模型检测出的候选CSP中仍有86%被保留，说明方法对CSP定义的扩展具有一定鲁棒性。此外，论文将结果**外推至包括管理1-2家公司的小型CSP**，估计非法CSP比例上升至**38-51%**，管理公司比例上升至**23-27%**。
- **效率信息**：PDF文本中未明确说明计算时间、参数量或FLOPs等效率信息。

## 7. 这篇论文真正有价值的地方
1.  **将监管知识转化为可计算特征**：论文将“什么是可疑CSP行为”这一直觉和经验，系统性地编码成了48个可量化的网络特征。这种**领域知识驱动的特征工程**是其在没有大量标注数据情况下取得成功的关键，对任何应用AI解决特定领域问题的项目都有启发。
2.  **“已知找未知”的实用范式**：它展示了一种在监管场景下非常实用的思路：利用少量高质量的“白名单”（持牌CSP），通过网络行为相似性来大规模扫描潜在的“黑名单”。这比从零开始构建一个异常检测模型更可行。
3.  **严谨的混合验证设计**：它没有完全依赖模型输出，而是结合了**多种算法相互验证**和**必不可少的人工抽样核实**，这提高了研究结论的可靠性，也为实际应用中的结果评估提供了方法论参考。
4.  **问题定义清晰，答案有实际价值**：它直接回答了政策制定者关心的量化问题（“非法CSP到底有多少？”），并给出了有置信区间的估计。这种研究对公共政策评估和监管资源分配有直接指导意义。

## 8. 局限与问题
1.  **“相似性”不等于“非法性”**：方法基于与持牌CSP的模式相似性，这可能导致**假阳性**。例如，一些合法的公司秘书或持有大量股份的职业经理人，其网络特征可能与CSP相似，但并非提供需要牌照的服务。
2.  **依赖公开数据，信息可能不完整**：数据来源于商会等公开注册系统，可能不包含未注册的地址、隐藏的实际控制人或复杂的代理安排，从而**遗漏部分完全隐藏的非法活动**。
3.  **人工标注成本高且存在主观性**：核实200个样本需要大量专家精力，且对于处于灰色地带的案例，判断是否为“需要牌照的服务”可能存在主观差异，影响估计的精确度。
4.  **外推假设的局限性**：对管理1-2家公司的“小型CSP”的规模外推，基于“它们与大型CSP特征相似”的假设，但文中未提供验证。小型CSP的行为模式可能不同，导致外推结果存在不确定性。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读**摘要**和**第5节（结论）**，即可掌握论文的核心问题、方法和关键结果。
- **如果复现**：重点阅读**第3节（数据与方法）**，特别是3.1（数据）和3.2（特征构建）部分，理解数据来源、清洗步骤和48个特征的定义。建模部分相对标准，但需注意其独特的验证流程。
- **如果借鉴创新点**：应该学习其**将领域知识转化为网络特征的思路**（如地址集中度、所有权国籍分布等），以及**“白名单”引导的相似性搜索**这一混合方法范式。这可用于其他网络异常检测任务（如识别壳公司、洗钱网络）。
- **如果写related work**：可将其放在**经济犯罪检测**（尤其是反洗钱）、**社会网络分析在金融监管中的应用**、或**基于图的异常检测**这些类别下进行引述。

## 10. 和其他论文的关系
根据给定的库主题`T_通用_NLP_其他`和文件名，本文主要涉及**网络分析**而非NLP。因此，与库内其他NLP论文可能没有直接的方法继承关系。但其核心思想——利用网络结构信息进行推理——与图神经网络（GNN）的应用有关联。如果库中有其他关于**图表示学习、网络嵌入或社交网络分析**的论文，可能存在潜在的概念关联，但文中未提供具体论文信息，故不在此处进行不确切的链接。

## 11. 关键词
经济犯罪， 网络分析， 企业服务提供商， 荷兰， 社会网络分析， 监管科技， 反洗钱， 特征工程， 相似性度量， 异常检测， 正例分类， 政策评估

## 12. 可信度说明
本精读笔记**严格基于用户提供的PDF提取文本（前12页）生成**。笔记内容均来自文本中的明确表述，包括研究问题、方法框架、关键结果和部分讨论。论文的后半部分（如完整的结果分析、相关工作的详细比较、更详细的结论讨论等）由于**提供的文本不完整（仅12/31页）** 而未能涵盖，因此笔记中涉及“局限与问题”、“真正价值”的部分是基于现有文本的分析和推断。整体提取质量良好，关键信息（如数字、方法流程）均按原文引用。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2021_Uncovering_the_Size.txt` (31/31 页; 原 AI 主体 12/31 + 全文补读 13-31); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
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
