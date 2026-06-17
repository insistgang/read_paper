---
title: The Language of Legal and Illegal Activity on the Darknet
authors:
  - "Leshem Choshen"
  - "Dan Eldad"
  - "Daniel Hershcovich"
  - "Elior Sulem"
  - "Omri Abend"
year: 2019
venue: "arXiv"
doi: 
pdf: [[2019_The_Language_of_Lega.pdf]]
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
extract_cache: .paper-cache/extracts/2019_The_Language_of_Lega.txt
---

# The Language of Legal and Illegal Activity on the Darknet

## 基本信息
- **PDF**: [[2019_The_Language_of_Lega.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | The Language of Legal and Illegal Activity on the Darknet |
| **作者** | Leshem Choshen; Dan Eldad; Daniel Hershcovich; Elior Sulem; Omri Abend（均为共同贡献，希伯来大学耶路撒冷分校计算机科学与工程学院） |
| **发表时间** | 2019（arXiv:1905.05543v2, cs.CL, 2019-06-04） |
| **刊物/会议** | arXiv preprint |
| **DOI** | 未明确（arXiv ID: 1905.05543） |
| **代码** | https://github.com/huji-nlp/cyber（数据需邮件申请） |

## 摘要

**清理后的英文原摘要**（据 PDF 提取文本整理，修复断词与空格）：

> The non-indexed parts of the Internet (the Darknet) have become a haven for both legal and illegal anonymous activity. Given the magnitude of these networks, scalably monitoring their activity necessarily relies on automated tools, and notably on NLP tools. However, little is known about what characteristics texts communicated through the Darknet have, and how well off-the-shelf NLP tools do on this domain. This paper tackles this gap and performs an in-depth investigation of the characteristics of legal and illegal text in the Darknet, comparing it to a clear net website with similar content as a control condition. Taking drug-related websites as a test case, we find that texts for selling legal and illegal drugs have several linguistic characteristics that distinguish them from one another, as well as from the control condition, among them the distribution of POS tags, and the coverage of their named entities in Wikipedia.

**中文翻译**：

> 互联网中未被索引的部分（即"暗网"）已成为合法与非法匿名活动的温床。鉴于这些网络规模庞大，对其活动进行可扩展的监控必然依赖自动化工具，尤其是 NLP 工具。然而，人们对暗网文本具有哪些特征、现成 NLP 工具在该领域表现如何知之甚少。本文填补这一空白，深入考察暗网中合法与非法文本的特征，并以一个内容相近的明网网站作为对照条件进行比较。以毒品类网站为测试案例，我们发现售卖合法与非法毒品的文本具有若干可将彼此区分、也可与对照条件区分的语言学特征，其中包括词性（POS）标签的分布，以及命名实体在 Wikipedia 中的覆盖程度。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：暗网（Darknet，指未被搜索引擎索引、常通过 Tor 网络以 ".onion" 域名匿名访问的站点）在匿名掩护下藏匿大量非法活动（Moore and Rid, 2016）。要对其规模化执法与情报监控，需把 NLP 工具应用于暗网文本；但人们对暗网语言的特征、特别是"什么区分了从事合法与非法活动的网站文本"几乎一无所知。
- **之前方法的问题**：作者所知唯一一项把暗网文本分为合法/非法的工作是 Avarikioti et al. (2018)，但该工作并未探究这两类文本在"哪些方面"存在差异。其余相关工作（如 Biryukov 2014 把 Tor 隐藏服务分成 18 个主题类、Graczyk & Kinningham 2015 用无监督特征选择+SVM 分类毒品销售）多停留在主题分类，并未直接处理合法/非法之分。
- **作者想解决的核心矛盾**：不止于"能否自动分类"，而要回答"凭什么能分类"——区分到底来自词汇选择、句法结构（词性分布）还是命名实体/语义知识的差异，从而为暗网监控 NLP 工具的开发提供语言学依据，并预判领域适配（domain adaptation）的难点。

## 关键贡献

1.  **确认并扩展词汇层面的可分性**：复现 Avarikioti et al. (2018) 的结论——仅凭内容词身份（词袋）即可在均衡样本上以约 **90%** 准确率区分合法/非法文本（对照其报告的 F1=85%、accuracy=89%）。
2.  **首次发现句法层面的可分性**：仅凭文档中**词性（POS）标签的分布**就是强区分线索（约 **71%** 准确率），说明两类文本在句法结构上存在根本差异——这是本文相对前人的核心新发现。
3.  **提出"三个独立领域"视角**：定量证明合法暗网、非法暗网与 eBay 文本两两之间的词分布距离（Jensen-Shannon 散度约 **0.60–0.65**）远大于各自的"自距离"（约 0.40–0.45），三者在词分布空间中近似构成一个**等边三角形**；因此非法文本并非合法文本的子领域，而应视为三个独立领域。这解释了可分性，也预示了领域适配的障碍。
4.  **揭示知识库覆盖差距**：用 Wiki 化（Wikification）分析发现，非法暗网站点的命名实体在 Wikipedia 中的覆盖率明显低于合法暗网站点（约 **32.5% vs 50.8%**，eBay 约 38.6%），原因是非法文本含大量毒品俚语/缩写（如 "kush"、"GBL"），通用知识库与 spaCy NER 难以覆盖、且误报较多。
5.  **验证跨领域泛化**：在 DUTA-10K 的"论坛"（用户生成内容）子领域重复实验，并把毒品域训练的分类器迁移到论坛域测试，证明合法/非法的语言区分具有一定跨领域泛化能力。

## 方法

本文不提出单一模型，而是一个以实证分析与对照实验为主的研究框架，核心在于**特征隔离（消融）**与**领域距离量化**。

- **整体框架**：(1) 数据收集与清洗；(2) 领域差异分析（词汇分布 + 命名实体）；(3) 分类实验与跨领域验证。
- **输入与输出**：
    - **输入**：三个语料的文本段落——非法暗网毒品站点、合法暗网毒品站点、eBay 毒品相关页面；外加 DUTA-10K"论坛"语料用于跨领域测试。
    - **输出**：领域差异统计量（Jensen-Shannon 散度、L1/变分距离、可 Wiki 化实体百分比）与分类**准确率**。
- **关键模块**：
    1.  **清洗模块**：原始数据集已去 HTML 标记，但仍残留按钮、加密密钥、元数据、URL 等非语言内容；本文移除这些文本，把段落合并为单行，并删除重复段落（"除数字外完全相同"即视为重复，以避免 "Showing all 9 results" 之类残留文本被过度统计）。
    2.  **词汇差异模块**：对每个领域计算词频分布，用 Jensen-Shannon 散度与变分距离（L1/Manhattan，遵循 Plank & van Noord 2011）度量领域间差异；并把每个语料随机对半切，用两半之间的分布相似度作为"自距离"基准。
    3.  **命名实体模块**：用 spaCy 做 NER 抽取全部命名实体（用所有实体类型而非仅 "Product"），再经 DBpedia Ontology API（Daiber et al., 2013）查询每个实体是否有对应 Wikipedia 条目，按站点求"可 Wiki 化实体百分比"的平均并报告标准误。
    4.  **分类模块**：5 类分类器 × 5 种输入操作的笛卡尔实验，以隔离词汇/句法/功能词各自的贡献。
- **分类器（5 种）**：
    - **NB**：scikit-learn `BernoulliNB`（α=1），二值词袋指示特征。
    - **SVM**：scikit-learn `SVC`，RBF 核，gamma=scale，tol=1e-5，计数词袋特征。
    - **BoE**：每词用 100 维 GloVe（Pennington 2014），求和（BoE sum）或平均（BoE average）后接 100 维全连接 + ReLU + dropout p=0.2；词向量训练中不更新，GloVe 未覆盖词从 N(μ_GloVe, σ²_GloVe) 随机初始化。
    - **seq2vec**：同 BoE，但用单层 100 维 BiLSTM，取前后向最终隐状态拼接后接全连接。
    - **attention**：用 ELMo（Peters 2018）上下文表示替换词向量，再叠加自注意力分类网络（McCann 2017）。
    - 神经网络分类器用 AllenNLP（Gardner 2018）实现。
- **输入数据操作（5 种）**：full（全词）、drop cont.（删内容词）、drop func.（删功能词）、pos cont.（内容词换成其通用 POS）、pos func.（功能词换成其通用 POS）。内容词定义为 spaCy 通用词性属于 {ADJ, ADV, NOUN, PROPN, VERB, X, NUM} 者，其余为功能词。
- **数据划分**：{eBay, Legal Onion, Illegal Onion} 每类随机下采样为 456 训练 / 57 验证 / 58 测试段落（约 80/10/10），保证标签均衡。
- **与已有方法的差异**：相比 Avarikioti et al. (2018) 主用 SVM + 词袋，本文 (1) 系统分析了词性等句法特征；(2) 引入同等规模、同为合法的 eBay 明网语料作为更合理的对照组；(3) 使用更多样的模型（含 ELMo 预训练表示）；(4) 设计了系统的输入特征消融。

## 实验

- **使用的数据集**：
    1.  **主语料（Onion）**：DUTA-10K（Al Nabki et al., 2019）中"drugs"子领域的合法与非法站点文本——选它是因为该域大、且有可靠区分的 legal/illegal 子类。
    2.  **对照（eBay）**：明网、合法、规模相近的语料，含 **118** 条商品描述（每条多于一句），由搜索 eBay 的毒品相关词（marijuana, weed, grass, drug）并按价格/模式过滤、去重后收集；含正式与非正式语言、缩写与俚语，但均假定为合法活动（即使涉及毒品也只是周边商品/工具而非售卖非法毒品）。
    3.  **跨领域（论坛）**：DUTA-10K"forums"子领域；合法论坛多讨论网页设计等技术话题，非法论坛涉及网络犯罪指南、毒品、种族主义等；为用户生成内容，更杂更噪。
- **对比对象**：不同**语言特征**（通过 5 种输入操作）与不同**分类器**（NB / SVM / BoE sum / BoE average / seq2vec / attention）。
- **评价指标**：准确率（accuracy），均衡测试集。
- **主实验结果（Table 3，毒品域）**：
    - **eBay vs. Legal Onion（对照实验）**：NB(full)=**91.4%**，说明合法暗网内容与明网 eBay 很容易区分；pos func.=**92.2%**（功能词换 POS 反而略升），drop cont.=**57.8%**（删内容词后大跌），印证**内容词是该任务主因**；但 drop cont. 下 SVM 仍达 **64.7%**，说明单凭功能词分布也有非平凡区分度。注意力（attention）最高 82.8%/85.3%，仍低于 NB。
    - **Legal vs. Illegal Onion（核心任务，更难）**：NB(full)=**77.6%**；**关键发现**——pos cont.（内容词换成 POS）下 SVM=**70.7%**，证明仅靠句法/语法范畴分布即可较好区分合法与非法；drop func.（删功能词）下 NB 升至 **87.9%**。
    - **反直觉现象**：更复杂的神经分类器（BoE/seq2vec/attention）普遍逊于朴素贝叶斯，作者归因于训练数据规模小、且该域专业词汇难被预训练嵌入良好支持。
- **领域差异结果**：
    - 词汇（Table 1）：各语料自距离 JSD≈0.40–0.45，两两领域间 JSD≈0.60–0.65，近似等边三角形。
    - 命名实体（Table 2）：可 Wiki 化实体平均百分比约为 eBay≈38.6%、Illegal Onion≈32.5%、Legal Onion≈50.8%（数值附标准误；提取文本中该表为 OCR 错乱的 "值:标准误" 形式，故百分比为最合理读数）。spaCy 在 Onion/eBay 上 NER 误报较多，尤其在非法站点把 "kush"、"GBL" 等毒品俚语/缩写误判为命名实体。
- **跨领域实验（Table 4，论坛域）**：
    - **Legal vs. Illegal Onion Forums（直接训练/测试）**：SVM(full)=**85.3%**（论坛域中 SVM 明显优于 NB 的 74.1%，与毒品域相反，反映用户生成内容特性不同）。
    - **Trained on Drugs, Tested on Forums（跨域迁移）**：NB(full)=**78.4%**，drop func.=**89.7%**，证明在毒品域学到的合法/非法区分能迁移到论坛域。
- **消融结论**：内容词是区分所有领域的最强特征；句法（POS）分布能有效区分合法/非法暗网文本；功能词分布也含领域信息。
- **效率信息**：PDF 文本未明确说明速度、参数量或 FLOPs 等效率信息。

## 局限

1.  **数据时效与可获得性**：暗网站点生命周期短，DUTA-10K 可能很快过时；非法数据的采集与发布受伦理/法律约束（本文数据"需邮件申请"），影响可复现性。
2.  **分类边界模糊**：合法/非法依赖人工标注且存在灰色地带（Avarikioti 等采用保守口径——内容目的明显非法即判为非法，即使技术上合法）；本文沿用 DUTA-10K 的既有分类，边界模糊性仍是挑战。
3.  **通用 NLP 工具不适配**：spaCy 在暗网（尤其非法）文本上 NER 误报多、Wiki 化覆盖低，说明需要专门的知识库与领域适配工具，前期成本高。
4.  **模型性能与数据规模**：合法/非法暗网分类最优准确率约 70%–88%，仍有空间；每类仅约 456 训练段落，规模偏小，限制了复杂神经模型发挥（反被 NB 超越）。
5.  **泛化边界**：仅验证了毒品→论坛的同语言、同语种泛化，未探索更远的跨域（如不同语言、代码/对话等其他模态）。

## 个人评论

这篇论文的价值不在于刷新某个 SOTA 模型，而在于其**系统性实证范式**与**对"为什么能分类"的语言学追问**。

1.  **问题导向清晰**：把"区分合法/非法暗网文本"这一执法/情报相关的实际问题，拆成"词汇—句法—语义知识"三条可量化的证据链。
2.  **多维特征分析**：不止词袋，而是从**词汇分布、句法结构（POS）、命名实体覆盖**三个维度剖析，这套框架对任何"特定领域文本分析"都有迁移价值。
3.  **实验设计稳健**：引入 eBay 作合法对照组、设计"自距离"基准、把 5×5（分类器×输入操作）做成完整消融，使"三个独立领域"和"句法可分"的结论有据可依；"等边三角形"的几何直觉尤其漂亮。
4.  **诚实的负面结果**：坦承神经模型在小数据+专业词汇下不敌朴素贝叶斯，并给出合理归因，比强行包装更可信。
5.  **指向明确的未来工作**：非法文本命名实体在通用知识库中覆盖不足，直接点出"需为暗网非法活动构建专业知识库 / 领域适配 NER"这一方向。

对后续研究的启发：在网络安全等垂直领域用 NLP 时，先深入分析该域文本与已知领域的差异所在，再选型，而非一上来套复杂模型。

### 使用建议

- **快速了解**：读摘要、第 1 节（引言）与第 5.1 节（结果），即可掌握动机、三大发现与主要结论。
- **复现研究**：精读第 3 节（数据集）与第 5 节（分类实验），关注实验设置、模型超参（GloVe 100 维、BiLSTM、ELMo、NB/SVM 超参）与 5 种输入操作；代码已开源（huji-nlp/cyber），数据需申请。
- **借鉴创新点**：学习其多维特征分析框架（词汇/句法/语义知识）与对照实验设计（控制组 + 自距离 + 消融）。
- **写 Related Work**：可归入"网络安全中的 NLP 应用""特定领域文本分类""领域适配"。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算语言学（NLP）与网络安全交叉领域，聚焦"把 NLP 用于暗网监控"这一应用场景。它要回答的不是"能否自动分类暗网合法/非法网站"，而是更本质的"凭什么能分类"——即合法与非法文本在语言学上究竟差在哪里。以暗网毒品销售网站为测试案例，并以明网 eBay 同主题页面为对照。归类上属于"NLP 特定领域应用 / 网络安全中的文本分析"，与具体计算机视觉主题无关，故 primary_topic 取 `T_通用_NLP_其他`。

## 2. 一句话总结
本文以暗网毒品站点与 eBay 对照组为材料，从词汇分布、词性（POS）分布、命名实体 Wiki 化覆盖三个维度量化合法/非法文本的语言差异，证明它们构成三个独立领域、并在句法层面亦可分（POS 即达约 71%），同时指出通用 NLP 工具与知识库在暗网非法文本上需大量领域适配。

## 3. 背景与问题
- **为什么要做**：暗网在匿名掩护下藏匿大量非法活动，规模化监控必须依赖自动化 NLP 工具；但对暗网语言特征、尤其"什么区分合法与非法网站文本"几乎一无所知。
- **之前方法的问题**：唯一做过合法/非法分类的 Avarikioti et al. (2018) 未探究两类"差在哪里"；其余工作（Biryukov 2014 的 18 类主题分类、Graczyk & Kinningham 2015 的毒品销售 SVM 分类、Morris & Hirst 2012 的性侵者识别、Latapy 2013 的儿童色情检测）多为主题/特定违法类型分类，未正面处理 legal/illegal 之分，也多只用词汇特征。
- **作者想解决的核心矛盾**：在匿名、噪声大的暗网环境中，既要能分类，更要理解分类的语言学依据（词汇 / 句法 / 命名实体），以指导专门工具与知识库的开发，并预判领域适配难点。

## 4. 核心贡献
1.  **词汇可分性（复现）**：内容词词袋在均衡样本上约 **90%** 准确率区分合法/非法，复现并对照 Avarikioti et al. (2018) 的 F1=85% / acc=89%。
2.  **句法可分性（新发现）**：仅 **POS 标签分布**即达约 **71%**，证明两类句法结构根本不同——本文相对前人的核心增量。
3.  **三独立领域**：合法暗网 / 非法暗网 / eBay 两两 JSD≈0.60–0.65 远大于自距离 0.40–0.45，近似等边三角形；非法非合法之子域，而是独立域 → 解释可分性、预示领域适配障碍。
4.  **知识库覆盖差距**：可 Wiki 化命名实体比例 Legal Onion≈50.8% > eBay≈38.6% > Illegal Onion≈32.5%；非法文本含大量毒品俚语，通用 KB/NER 覆盖差且误报多。
5.  **跨领域泛化**：在论坛域重做并做毒品→论坛迁移，证明合法/非法语言区分可跨域泛化。

## 5. 方法详解
本文是实证分析框架，核心是**特征隔离消融**与**领域距离量化**，而非单一模型。
- **流程**：数据清洗 → 领域差异分析（词汇 + 命名实体）→ 5×5 分类实验 → 跨域验证。
- **清洗**：去按钮/密钥/元数据/URL，合并段落为单行，删"除数字外相同"的重复段落。
- **领域距离**：词频分布 + Jensen-Shannon 散度 + 变分距离（L1）；每语料对半切得"自距离"基准（Plank & van Noord 2011）。
- **命名实体**：spaCy NER（全部实体类型）抽取 → DBpedia Ontology API 查 Wikipedia 条目 → 按站点求可 Wiki 化百分比均值 + 标准误。
- **5 分类器**：NB（BernoulliNB, α=1, 二值词袋）、SVM（SVC, RBF, gamma=scale, tol=1e-5, 计数词袋）、BoE sum/average（100 维 GloVe + FC+ReLU+dropout 0.2，词向量冻结）、seq2vec（单层 100 维 BiLSTM 前后向末隐状态拼接）、attention（ELMo + 自注意力分类网，McCann 2017）；神经模型用 AllenNLP。
- **5 输入操作**：full / drop cont. / drop func. / pos cont.（内容词→POS）/ pos func.（功能词→POS）。内容词 = spaCy 通用词性 ∈{ADJ,ADV,NOUN,PROPN,VERB,X,NUM}，余为功能词。
- **数据划分**：每类 456/57/58（约 80/10/10），下采样保持均衡。
- **两种设置**：eBay vs Legal Onion（对照，验证明网/暗网差异）；Legal vs Illegal Onion（核心，验证合法/非法差异）。

## 6. 实验与结果
- **数据集**：DUTA-10K "drugs" 子域合法/非法站点；eBay 118 条商品描述（搜 marijuana/weed/grass/drug 收集）；DUTA-10K "forums" 子域做跨域。
- **指标**：均衡测试集准确率。
- **毒品域（Table 3）**：
    - eBay vs Legal Onion：NB(full)=91.4，pos func.=92.2，drop cont.=57.8（但 SVM drop cont.=64.7 → 功能词亦有区分度）；attention≤85.3，均不及 NB。
    - Legal vs Illegal Onion（更难）：NB(full)=77.6，drop func.=87.9；**SVM pos cont.=70.7（仅句法即可较好区分）**。神经模型普遍逊于 NB（小数据 + 专业词汇所致）。
- **领域差异**：JSD 自距离 0.40–0.45 / 域间 0.60–0.65（Table 1，等边三角形）；可 Wiki 化 Legal 50.8% > eBay 38.6% > Illegal 32.5%（Table 2，附标准误）；spaCy 在非法站点把 "kush"/"GBL" 误判为实体。
- **论坛域（Table 4）**：Legal vs Illegal Forums SVM(full)=85.3（此域 SVM>NB=74.1）；Trained on Drugs→Tested on Forums NB(full)=78.4、drop func.=89.7，证明跨域迁移有效。
- **效率信息**：PDF 文本未明确速度 / 参数量 / FLOPs。

## 7. 这篇论文真正有价值的地方
价值在**系统性实证范式**与**对问题本质的语言学洞察**，而非新模型。
1.  问题导向：把"区分合法/非法暗网文本"拆为词汇—句法—语义知识三条证据链。
2.  多维特征：词汇分布 + 句法（POS）+ 命名实体覆盖，三角度框架可迁移到其他垂直域文本分析。
3.  实验稳健：eBay 对照组 + 自距离基准 + 5×5 消融，使"三独立领域 / 句法可分"结论有据。
4.  诚实的负面结果：坦承神经模型不敌 NB 并给出合理归因（数据小 + 专业词汇 + 嵌入不支持）。
5.  指向未来工作：非法文本命名实体在通用 KB 覆盖不足 → 需建暗网专业知识库 / 领域适配 NER。

启发：垂直域（网络安全）用 NLP 前先分析文本与已知域的差异，再选型，勿急于套复杂模型。

## 8. 局限与问题
1.  **数据时效/可获得性**：暗网站点短命，DUTA-10K 易过时；非法数据受伦理法律约束、需申请，影响复现。
2.  **分类边界模糊**：合法/非法依赖人工标注，存在灰色地带（Avarikioti 取保守口径）；本文沿用既有分类。
3.  **通用工具不适配**：spaCy NER 误报多、Wiki 化覆盖低，需专门知识库与领域适配，前期成本高。
4.  **性能与规模**：合法/非法分类最优约 70%–88%，每类仅约 456 训练段落，规模偏小，复杂神经模型反被 NB 超越。
5.  **泛化边界**：仅验证同语言毒品→论坛迁移，未探索跨语言 / 跨模态等更远泛化。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要、第 1 节、第 5.1 节，掌握动机、三大发现与结论。
- **复现研究**：精读第 3 节（数据集）、第 5 节（分类实验），关注超参与 5 种输入操作；代码 huji-nlp/cyber 已开源，数据需申请。
- **借鉴创新点**：多维特征分析（词汇/句法/语义知识）+ 对照实验（控制组/自距离/消融）。
- **写 Related Work**：归入"网络安全中的 NLP""特定领域文本分类""领域适配"。

## 10. 和其他论文的关系
- `[[Avarikioti et al., 2018]]`：唯一在先的合法/非法暗网分类（SVM + 词袋 + 主动学习，F1=85%/acc=89%），本文复现其词汇结论并新增句法分析。
- `[[Al Nabki et al., 2017]]`：提出首个公开暗网数据集 DUTA（含主题分类，部分类区分合法/非法）。
- `[[Al Nabki et al., 2019]]`：扩展为 DUTA-10K（本文数据来源），报告约 20% 隐藏服务属"可疑"活动。
- `[[Plank and van Noord, 2011]]`：本文领域距离度量（JSD/变分距离/自距离）的方法来源。
- 其他涉及"暗网文本分类""领域自适应""特定领域 NER"的工作可能关联，但提取文本未给具体内容，无法建立确定双链。

## 11. 关键词
暗网（Darknet/Onion）, 合法/非法文本分类, 词性（POS）分布, 命名实体 Wiki 化, 领域差异/Jensen-Shannon 散度, 自距离, spaCy/ELMo/朴素贝叶斯, 领域适配, 网络安全 NLP, DUTA-10K

## 12. 可信度说明
本精读笔记基于 9/9 页 PDF 提取文本生成；提取文本覆盖摘要、引言、相关工作、数据集、领域差异分析（4.1 词汇 / 4.2 命名实体）、分类实验（第 5 节，含 Table 3）、跨域实验（第 6 节，含 Table 4）。所有关键数字（91.4/57.8/64.7/77.6/70.7/87.9/85.3/78.4/89.7、JSD 0.40–0.65、456/57/58、118 条 eBay、GloVe 100 维、dropout 0.2、NB α=1、SVM tol=1e-5、Avarikioti F1=85%/acc=89%、Al Nabki 20%）均在提取文本中找到出处。两点需注意：(1) Table 2 的可 Wiki 化百分比在提取缓存中为 OCR 错乱的 "值:标准误" 形式（如 "Illegal Onion 32:51:35"），笔记中 32.5%/50.8%/38.6% 为最合理读数，精确值待核原表；(2) 提取缓存在 25000 字符处截断（原文约 37210 字符），第 7 节深入讨论、参考文献与可能附录未覆盖，相关信息标注为"PDF 文本未明确"或据原文后续页待核。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 2782 字符/页; 但缓存在 25000 字符处截断, 后文与第7节讨论未覆盖); 来源缓存: `.paper-cache/extracts/2019_The_Language_of_Lega.txt` (9/9 页); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
