---
title: "Mining Illegal Insider Trading of Stocks: A Proactive Approach"
authors:
  - "Sheikh Rabiul Islam"
  - "Sheikh Khaled Ghafoor"
  - "William Eberle"
year: 2018
venue: "arXiv:1807.00939 [q-fin.ST]"
doi: 
pdf: [[2018_Mining_Illegal_Insid.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
status: ai-read
reading_stage: ai-complete
confidence: high
source_basis: pdf-text
date_added: 2026-06-03
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2018_Mining_Illegal_Insid.txt
---

# Mining Illegal Insider Trading of Stocks: A Proactive Approach

## 基本信息
- **PDF**: [[2018_Mining_Illegal_Insid.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Mining Illegal Insider Trading of Stocks: A Proactive Approach |
| **作者** | Sheikh Rabiul Islam; Sheikh Khaled Ghafoor; William Eberle（均属 Tennessee Technological University, Cookeville, U.S.） |
| **发表时间** | 2018 |
| **刊物/会议** | arXiv:1807.00939v3 [q-fin.ST], 2018-11-07 |
| **DOI** | 未明确（arXiv 预印本，PDF 文本未给出 DOI） |

## 摘要

> **英文（据 PDF 提取文本整理）**: Illegal insider trading of stocks is based on releasing non-public information (e.g., new product launch, quarterly financial report, acquisition or merger plan) before the information is made public. Detecting illegal insider trading is difficult due to the complex, nonlinear, and non-stationary nature of the stock market. In this work, we present an approach that detects and predicts illegal insider trading proactively from large heterogeneous sources of structured and unstructured data using a deep-learning based approach combined with discrete signal processing on the time series data. In addition, we use a tree-based approach that visualizes events and actions to aid analysts in their understanding of large amounts of unstructured data. Using existing data, we have discovered that our approach has a good success rate in detecting illegal insider trading patterns.

> **中文翻译**: 股票的非法内幕交易，指在非公开信息（如新产品发布、季度财报、并购计划）被正式公开之前，基于该信息进行的交易。由于股票市场具有复杂、非线性、非平稳的特性，检测非法内幕交易十分困难。本文提出一种方法，从大规模、异构的结构化与非结构化数据源中，结合基于深度学习的方法与对时间序列数据的离散信号处理，主动地检测和预测非法内幕交易。此外，本文采用一种基于树的可视化方法来呈现事件与动作，帮助分析师理解大量非结构化数据。基于现有数据，作者发现该方法在检测非法内幕交易模式方面有较好的成功率（a good success rate）。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：非法内幕交易（illegal insider trading）发生在交易者依据非公开（私有、泄露、被授意 tipped）信息抢先交易、而该信息尚未公开之时，破坏了市场的公平有序。论文将其置于证券欺诈（securities fraud）大背景下：FBI 报告列出的高发欺诈类型包括市场操纵（market manipulation）、收盘后非法交易（late day trading）和高收益投资欺诈（high yield investment fraud）。股票市场数据复杂、非线性、非平稳，使非法内幕交易检测和股价预测都很困难。
- **之前方法的问题**：（1）现有研究多聚焦于**市场操纵**而非内幕交易；论文在 Background 中系统综述了 Contextual Anomaly Detection (CAD)、基于规则/专家知识的方法、Naive Bayes/SVM/CART/KNN/Random Forest 等机器学习方法、Coupled Behaviors Analysis (CBA)、基于金融本体（financial ontology）的文本挖掘等工作，指出针对内幕交易的研究极少。（2）检测多为**事后分析**——投资者往往等到 SEC 立案才知情，已无可操作的预警价值。（3）从模型角度看，普通神经网络（ANN）缺乏对历史的记忆，RNN 虽有有限记忆但受梯度消失/爆炸问题困扰，远端步的梯度贡献趋零、学习率快速下降。
- **核心矛盾**：要在官方消息公开**之前**，从异构（结构化交易量 + 非结构化诉讼文本）数据中主动识别可能由非法内幕交易引起的异常交易模式，实现“事前预警”而非“事后取证”。作者强调，据其所知这是首次用计算智能（computational intelligence）从多源数据中综合性地挖掘非法内幕交易，也正因新颖性，缺乏可对标的基准方法。

## 关键贡献

1.  **主动式检测框架（首创性声明）**：首次（作者自述）用计算智能、结合异构数据源，在官方新闻发布前主动预测并挖掘非法内幕交易，而非依赖事后 SEC 起诉信息。论文也因此声明无法与已有方法做基准对比（benchmark）。
2.  **LSTM 交易量预测**：用 LSTM RNN 基于历史**交易量（transaction volume）**而非股价，对目标公司未来交易量进行预测，采用三种预测方式（详见方法节）。选用交易量的理由：S 股的价格可能远高/低于 S，但其交易量恰好就是 S，更稳定可比；且交易量比其他可得特征波动更明显。
3.  **ANOMALOUS 异常检测算法**：提出一个以**归一化互相关（Normalized Cross-Correlation, NCC）** 为核心度量的算法，将 LSTM 产生的信号与从历史案例中提取的已知非法交易模式（ground truth）做相似性匹配，并考虑不同的“天滞后（day lag）”以容忍信号未严格对齐。
4.  **非结构化数据处理（NLP + 决策树）**：从 SEC 诉讼新闻稿中分类出内幕交易案例——分词构造特征向量，用 **Extra Trees（极端随机树）** 算法做特征排序/筛选，再训练分类器，使其可推广到未来数据（如社交网络帖子）的分类。
5.  **树状可视化**：开发基于树的可视化，帮助分析师理解一个案例为何归入内幕交易类别、以及事件（events）与动作（actions）之间的关联，并据此下钻提取公司名、内幕人、知情日期、公开日期、非法获利额等属性。
6.  **长跨度案例数据集**：构建覆盖 1996–2018 共 22 年的 SEC 诉讼档案数据集（7988 份诉讼新闻稿），并据此提取作为 ground truth 的“异常模式”。

## 方法

**整体框架**（对应 Figure 1 流程图，A→B→C 标注）：端到端流水线——**目标公司识别（A）→ 历史交易量数据收集（B）→ 模式发现/异常模式提取（C）→ LSTM 多策略预测 → 生成离散时间序列信号 → 以滑动窗口方式用 NCC 与已知非法交易模式做相似性匹配 → 输出异常检测/预测结果**。

- **输入**：
    1.  目标公司列表：由树状可视化筛选、且被 SEC 认定为显著内幕交易案例的公司。
    2.  目标公司的逐日历史交易量（Yahoo Finance）。采集**起始日 = 内幕人知情日期前 3 个月**，终止日 = 实验执行日。
    3.  从 SEC 诉讼档案提取的已知非法内幕交易模式（ground truth）。
- **输出**：
    1.  LSTM 预测的多种未来交易量时间序列信号。
    2.  预测/真实信号与已知异常模式之间的 NCC 相似度，用以指示非法内幕交易的可能性。
- **关键模块**：
    1.  **模式发现（Pattern Discovery, C）**：窗口（window）= 连续 50 个交易日的交易量集合。作者发现内幕人通常在知情后极短时间（1–2 天）内完成交易，故选取 50 天窗口、并令“知情日期居于窗口中间”。同一公司多次发生内幕交易（如 Wells Fargo）则得到多个模式（窗口）。这些窗口构成 ANOMALOUS 的 ground truth。
    2.  **LSTM 预测模块**：对历史交易量用 LSTM RNN，采用三种预测方式：**a)** 基于前一个窗口预测后一个窗口（如未来 50 天）；**b)** 基于前一个窗口预测下一天；**c)** 基于全部历史数据预测未来一个窗口。窗口大小 50 与 Jia et al. [9]（用 LSTM 预测股价）一致，但本文预测的是交易量而非价格。数据预处理：将交易量转换为**相对于窗口首日的百分比变化**以提升可解释性（例：首三日 100、120、115 → 输入 0、0.20、0.15）。选 LSTM 是因其门控机制可按需长期记忆/遗忘信息，适合带季节性、噪声和趋势的时间序列。
    3.  **离散信号生成**：LSTM RNN 的输出共**四类离散信号（时间序列）**：实际交易量信号、窗口级预测信号（下一窗口）、天级预测信号（下一天）、以及基于全历史数据的预测信号（下一窗口）。
    4.  **ANOMALOUS 异常检测模块**：核心用 **NCC** 度量两个离散信号在不同 day lag 下的相似度——先将信号归一化到同一尺度再比较，衡量其线性相关强弱；day lag 用于容忍信号首/尾缺值导致的非垂直对齐。把上述四类信号与已知非法交易模式逐窗、逐段（窗口再细分到天）比较。算法参数为 **C, M, W, P, Data**：C = 选定公司集合，M = 三种 LSTM 应用方式之一，W = 窗口数，P = 提取的内幕交易模式（ground truth），Data = LSTM 预测交易量的多维数组。算法对每个公司 c、每种方式 m、每个窗口 w，将预测信号同时与**实际信号**和**欺诈/异常模式信号**做 NCC 比较。
- **模块连接**：模式发现离线产出 ground truth 模式库；LSTM 输出的四类信号在线送入 ANOMALOUS，以滑动窗口方式与模式库做 NCC 匹配。
- **与已有方法的差异**：
    1.  **目标不同**：针对更难检测的非法内幕交易，而非更常见的市场操纵。
    2.  **策略前瞻**：旨在“预测/事前”异常，而非对已知欺诈“事后检测/分析”。
    3.  **方法综合**：NLP（决策树/Extra Trees 处理诉讼文本）+ LSTM（预测结构化交易量）+ 信号处理（NCC 模式匹配）多学科融合，作者称为首次综合性尝试。

## 实验

> 说明：提取缓存为 PDF 前 10 页、约 25k 字符，正文止于第四节（Experimental Results）A 小节“Litigation Classification and Visual Analytics”的 Extra Trees 描述处即被截断，**后续的量化结果（如检测成功率、NCC 阈值、各公司匹配结果）不在提取文本中**。

- **使用的数据集**：
    1.  **SEC 诉讼档案**：Python 爬虫抓取 1996–2018 的诉讼新闻稿，共 **7988** 份。关键词“insider”分布：标题含 605 份、正文含 1142 份、标题或正文含 1222 份、标题与正文均含 525 份；据此约 **15%** 为内幕交易相关指控，其余为其他欺诈。按关键词将案例标注为 insider / non-insider，并训练分类器。
    2.  **股票交易数据**：来自 Yahoo Finance，针对 **10 家公司**收集约 **14,842** 条时间序列数据。其中 9 家有历史内幕交易案例：Wells Fargo、BP plc、GTx、Oracle、American Semiconductor、Spectrum Pharmaceuticals、Allscripts Healthcare Solutions、Herbalife、Evercore；第 10 家为 Google 母公司 Alphabet Inc.（2015 年成立、无内幕交易记录），用于验证。
- **对比方法**：论文明确声明，由于工作的新颖性，**无法与其他方法做基准对比（benchmark）**；提取文本中亦未列出量化对比基线。
- **评价指标**：以 **NCC** 衡量预测/真实信号与已知异常模式的相似度。摘要与引言称方法有“a good success rate”，但**提取文本未给出精确率/召回率/F1 等量化指标及数值**。
- **主实验结果**：引言中给出两条实验结论：(1) 可在短时间内从受影响与未受影响公司的混合数据中检测出非法内幕交易；(2) 可对大量非结构化数据进行分类并直观可视化。**具体成功率/准确率数字不在提取文本中**。
- **消融实验**：提取文本未找到消融实验描述。
- **泛化/验证实验**：用无已知欺诈案例的 Alphabet Inc. 全部公开交易量数据做验证，检查是否存在与异常模式匹配的窗口（用于检验误报/泛化）。
- **效率信息**：提取文本未提供计算速度、参数量、FLOPs 等效率信息，亦未给出 LSTM 训练超参数。

## 局限

1.  **Ground truth 不完整**：异常模式来自已被 SEC 查处的案例，只是“被抓到”的部分，模式库难以覆盖全部非法交易形态。
2.  **实验充分性不足**：提取文本中缺量化指标与对比实验，“good success rate”缺乏数据支撑（部分原因是作者自述无可对标基线）。
3.  **特征与模式单一**：仅以交易量为主特征、异常模式固定为 50 天窗口，可能过于简化；内幕交易也可能体现在价格、波动率、期权等多维度上。
4.  **流程自动化程度低**：从诉讼文本提取关键属性（公司名、知情日期、非法获利额等）目前为**手动**（作者明确指出，自动化留待 future work），限制可扩展性。
5.  **复现风险**：LSTM 训练细节（超参、训练轮次）、NCC 的具体阈值与窗口滑动策略在提取文本中未充分说明。

## 个人评论

1.  **问题视角独特**：聚焦非法内幕交易的“主动预测”，是研究相对稀少但实务价值很高的方向，把问题从事后取证推向事前预警。
2.  **框架设计思路**：示范了 NLP（文本）+ LSTM（序列）+ 信号处理（NCC 匹配）解决复杂金融问题的完整流水线，这种“文本筛案例 → 提取模式 → 预测 → 模式匹配”的设计值得借鉴。
3.  **数据利用巧妙**：把公开的 SEC 诉讼判例转化为可计算的监督信号（异常模式 ground truth），是一种弱监督/案例驱动的思路。
4.  **可解释性**：树状可视化降低分析师审阅成本（按案例过滤），并用百分比变化预处理提升预测结果可读性，在金融风控这类高解释性需求场景里是务实选择。
5.  **诚实但偏弱的实证**：作者坦承无基准、属首次尝试，但也因此让“good success rate”这类结论显得证据单薄；从工程角度看，这更像一个可行性原型（proof-of-concept）而非经充分验证的系统。

### 使用建议

- **如果快速了解**：读摘要、引言（I. Introduction）的 Contribution 段，以及方法节（III）对 LSTM 三种预测方式和 ANOMALOUS 的概述。
- **如果复现**：精读 III. Methodology——LSTM 三种预测方式、四类离散信号、NCC + day lag 的匹配逻辑、以及 ANOMALOUS 的参数 C/M/W/P/Data；需自行从 SEC 网站构建诉讼数据集、从 Yahoo Finance 采集交易量，并注意“百分比变化”预处理。NCC 阈值与训练超参文中未给，需自定。
- **如果借鉴创新点**：
    1.  融合 NLP（Extra Trees 选特征）与时间序列分析的异构数据处理框架。
    2.  把法律/判例文本转化为可计算监督信号的思路，可迁移到其他领域的异常检测。
    3.  NCC + day lag 在比较带时间偏移的金融序列模式中的应用。
- **如果写 related work**：可归入“金融欺诈/异常检测”和“LSTM 时间序列预测”两类；因方法综合，也可作为“跨模态金融数据分析”的相关工作。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本论文属于**金融数据挖掘 / 金融时间序列异常检测**方向（arXiv 分类 q-fin.ST），核心是用计算智能在信息公开前主动检测和预测股票市场的**非法内幕交易（illegal insider trading）**。方法上融合了 NLP（决策树 / Extra Trees 处理 SEC 诉讼文本）、LSTM（预测交易量时间序列）与离散信号处理（NCC 模式匹配）。它与计算机视觉的目标检测无关——原 primary_topic 标为 “C2_目标检测_违建_车辆_船舶_行人” 系明显的分类错误，本次复核已改为 `T_通用_NLP_其他`。

## 2. 一句话总结
本文提出一套主动式流水线：用 LSTM 预测目标公司股票**交易量**，再用自研 ANOMALOUS 算法以归一化互相关（NCC）将预测/真实信号与从 SEC 诉讼档案挖出的已知内幕交易模式（ground truth）做相似度匹配，从而在信息公开前预警潜在的非法内幕交易；同时用 NLP+树状可视化处理海量诉讼文本。

## 3. 背景与问题
- **为什么要做**：非法内幕交易依据非公开信息抢先交易，破坏市场公平；其检测与股价预测因市场的复杂、非线性、非平稳特性而困难。投资者通常等 SEC 立案才知情——为时已晚，缺乏可操作的预警。
- **之前方法的问题**：研究多集中于市场操纵（CAD、规则/专家系统、Naive Bayes/SVM/CART/KNN/RF、CBA、金融本体文本挖掘等），针对内幕交易者极少且多为事后分析；模型层面 ANN 无记忆、RNN 受梯度消失/爆炸困扰，远端梯度贡献趋零。
- **核心矛盾**：在信息公开**前**，从异构（交易量 + 诉讼文本）数据中识别由内幕交易引起的异常模式，做到事前而非事后。作者称这是首次此类综合尝试，也因此无可对标基线。

## 4. 核心贡献
1.  **主动式框架**：用计算智能 + 异构数据在官方消息前预测内幕交易（首创性声明）。
2.  **LSTM 预测交易量**（而非股价）：三种预测方式；选交易量因其等于成交股数、更稳定可比、波动更明显。
3.  **ANOMALOUS 算法**：以 NCC（含 day lag 容错）匹配信号与 ground-truth 异常模式。
4.  **NLP + Extra Trees**：从 7988 份诉讼稿中筛特征、分类内幕交易案例，可推广到未来数据。
5.  **树状可视化**：辅助分析师理解事件-动作关联并下钻提取案例属性。
6.  **22 年（1996–2018）SEC 诉讼数据集**及其异常模式 ground truth。

## 5. 方法详解
**流程（Fig.1，A→B→C）**：树状可视化 + SEC 认定 → 锁定目标公司（A）→ Yahoo Finance 采逐日交易量，起始日 = 知情日前 3 个月（B）→ 选 50 天窗口、令知情日居中，提取内幕交易模式作 ground truth（C）→ LSTM 三方式预测交易量 → 生成四类离散信号 → ANOMALOUS 以滑动窗口 + NCC 匹配 → 输出异常/预测结果。

- **窗口与模式发现**：window = 连续 50 个交易日；内幕人通常 1–2 天内完成交易，故 50 天窗口让知情日居中；多次涉案公司（如 Wells Fargo）产生多个模式。
- **LSTM 三种预测方式**：a) 前窗口→后窗口；b) 前窗口→次日；c) 全历史→未来窗口。窗口 50 与 Jia et al.[9] 一致（其预测股价，本文预测交易量）。预处理：相对窗口首日的百分比变化（100,120,115 → 0,0.20,0.15）。
- **四类离散信号**：实际交易量、窗口级预测、天级预测、全历史预测。
- **ANOMALOUS（参数 C,M,W,P,Data）**：对每公司 c / 每方式 m / 每窗口 w，把预测信号与实际信号及欺诈模式信号做 **NCC**——先归一化到同尺度再比较线性相关，并按 day lag 容忍首尾缺值的非对齐。窗口再细分到天逐段比较。
- **差异**：目标（内幕交易 vs 市场操纵）、策略（预测 vs 事后检测）、方法（NLP+LSTM+信号处理综合）三方面区别于已有工作。

## 6. 实验与结果
- **数据集**：(1) SEC 诉讼稿 7988 份（insider 关键词：标题 605 / 正文 1142 / 标题或正文 1222 / 二者皆含 525；约 15% 为内幕交易相关）；(2) Yahoo Finance 交易量约 14,842 条，覆盖 10 家公司（9 家涉案：Wells Fargo、BP plc、GTx、Oracle、American Semiconductor、Spectrum Pharmaceuticals、Allscripts、Herbalife、Evercore；Alphabet Inc. 无案例，用于验证）。
- **分类实验（IV.A）**：对诉讼文本分词构造特征向量，用 **Extra Trees（极端随机树）** 排序特征，再建分类器区分内幕/非内幕案例（提取文本在此处被截断）。
- **对比方法**：作者明确声明因新颖性**无法 benchmark**；提取文本无量化基线。
- **评价指标**：NCC 相似度。摘要/引言称“good success rate”，但**精确率/召回率/F1 等数值不在提取文本中**。
- **主结果**：引言给出两条结论——可短期内从混合公司中检出内幕交易、可分类并可视化大量非结构化数据；**具体数字不在提取文本中**。
- **泛化/验证**：用 Alphabet Inc. 全量数据检查是否误匹配异常模式。
- **消融 / 效率**：提取文本均未提供。

## 7. 这篇论文真正有价值的地方
1.  **问题选得好**：内幕交易的“事前预测”研究稀少、实务价值高。
2.  **流水线设计**：NLP（选案例/特征）→ 模式提取 → LSTM 预测 → NCC 匹配，跨模态、可解释，整体思路可迁移。
3.  **判例即监督信号**：把 SEC 诉讼判例转成可计算的异常模式 ground truth，是案例驱动的弱监督思路。
4.  **务实的可解释性**：树状可视化 + 百分比变化预处理，贴合金融风控对解释性的要求。
5.  **选交易量而非价格**：交易量等于成交股数、跨公司更可比、波动更显著——是一个有洞察力的特征选择。

## 8. 局限与问题
1.  **Ground truth 偏差**：仅含被查处案例，模式库不完整。
2.  **实证偏弱**：无基线、无量化指标，结论证据单薄，更像可行性原型。
3.  **特征/模式单一**：仅交易量、固定 50 天窗口，未用价格/波动率/期权等多维信息。
4.  **半自动**：诉讼文本属性提取仍为手动（作者自承，留待 future work）。
5.  **复现难**：LSTM 超参、NCC 阈值、窗口滑动策略未充分披露。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 Contribution 段 + 方法节对 LSTM 三方式与 ANOMALOUS 的概述。
- **复现**：精读 III. Methodology（三种预测、四类信号、NCC+day lag、参数 C/M/W/P/Data），自建 SEC 诉讼集与 Yahoo 交易量，注意百分比变化预处理；阈值与超参需自定。
- **借鉴创新**：异构 NLP+时间序列框架、判例转监督信号、NCC+day lag 处理时间偏移序列。
- **写 related work**：归入“金融欺诈/异常检测”与“LSTM 时间序列预测”，或作为“跨模态金融数据分析”相关工作。

## 10. 和其他论文的关系
本论文为金融时间序列 / 欺诈检测 + NLP 工作，与本知识库以计算机视觉为主的主题库交集很小，故暂不与具体 CV 论文建立双链。它在方法谱系上承接：市场操纵检测（CAD[4]、Golmohammadi[1]、Diaz[5]、CBA/Song[10]、金融本体 Zaki[11]）与 LSTM 股价预测（Jia[9]，本文借用其 50 天窗口设定但改预测交易量）。归类已修正为 `T_通用_NLP_其他`。

## 11. 关键词
非法内幕交易, 股票市场, 证券欺诈, LSTM RNN, 交易量预测, 时间序列, 异常检测, ANOMALOUS, 归一化互相关 NCC, day lag, 自然语言处理, Extra Trees, 决策树, 树状可视化, SEC 诉讼档案, 主动预测。

## 12. 可信度说明
本精读完全基于提供的 PDF 提取文本生成，未编造信息。提取缓存为 PDF 前 10 页、约 25k 字符，覆盖摘要、引言（I）、背景（II）、方法（III）以及实验结果第四节（IV）的 A 小节起始——正文在 IV.A 的 Extra Trees 描述处被截断。因此**具体量化结果（检测成功率、NCC 阈值、各公司匹配数字）、消融与效率信息、完整结论与参考文献均不在提取文本中**，相关处已标注“未在提取文本中”。文本提取质量清晰，足以支撑对动机、框架与核心方法的准确理解。本次复核还修正了 frontmatter 中被乱码污染的作者（应为 Sheikh Rabiul Islam / Sheikh Khaled Ghafoor / William Eberle）、venue（arXiv:1807.00939 [q-fin.ST]）以及明显错误的主题分类（由 CV 目标检测改为 T_通用_NLP_其他）。

---

> **可信度补充**: PDF 提取质量 = **high** (提取清晰, 约 2.5k 字符/页); 提取覆盖 10/10 页但内容截断于约 25k 字符 (IV.A 节), 故定量实验结果不在文本内; 来源缓存: `.paper-cache/extracts/2018_Mining_Illegal_Insid.txt`; 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro); 本次复核日期: 2026-06-18 (仅 AI 复核, 未经人工精读)。
<!-- AI_READING_NOTE_END -->
