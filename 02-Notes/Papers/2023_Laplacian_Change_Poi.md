---
title: Laplacian Change Point Detection for Single and Multi-view Dynamic Graphs
authors:
  - "Shenyang Huang"
  - "Samy Coulombe"
  - "Yasmeen Hitti"
  - "Reihaneh Rabbany"
  - "Guillaume Rabusseau"
year: 2023
venue: "arXiv"
doi: 
pdf: [[2023_Laplacian_Change_Poi.pdf]]
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
extract_cache: .paper-cache/extracts/2023_Laplacian_Change_Poi.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/30 pages"
---
# Laplacian Change Point Detection for Single and Multi-view Dynamic Graphs

## 基本信息
- **PDF**: [[2023_Laplacian_Change_Poi.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Laplacian Change Point Detection for Single and Multi-view Dynamic Graphs |
| **作者** | Shenyang Huang; Samy Coulombe; Yasmeen Hitti; Reihaneh Rabbany; Guillaume Rabusseau (Mila / McGill University / Université de Montréal, CIFAR AI chair) |
| **发表时间** | 2023 (arXiv:2302.01204v1 [cs.LG], 2023-02-02) |
| **刊物/会议** | arXiv (本文是作者 KDD 2020 工作 "Laplacian Change Point Detection for Dynamic Graphs" [25] 的扩展版) |
| **DOI** | 未明确 |

## 摘要

**清理后的英文原摘要**（据 PDF 提取文本修复空格/连字符，剔除杂入字符）:

> Dynamic graphs are rich data structures that are used to model complex relationships between entities over time. In particular, anomaly detection in temporal graphs is crucial for many real world applications such as intrusion identification in network systems, detection of ecosystem disturbances and detection of epidemic outbreaks. In this paper, we focus on change point detection in dynamic graphs and address three main challenges associated with this problem: i) how to compare graph snapshots across time, ii) how to capture temporal dependencies, and iii) how to combine different views of a temporal graph. To solve the above challenges, we first propose Laplacian Anomaly Detection (LAD) which uses the spectrum of graph Laplacian as the low dimensional embedding of the graph structure at each snapshot. LAD explicitly models short term and long term dependencies by applying two sliding windows. Next, we propose MultiLAD, a simple and effective generalization of LAD to multi-view graphs. MultiLAD provides the first change point detection method for multi-view dynamic graphs. It aggregates the singular values of the normalized graph Laplacian from different views through the scalar power mean operation. Through extensive synthetic experiments, we show that i) LAD and MultiLAD are accurate and outperform state-of-the-art baselines and their multi-view extensions by a large margin, ii) MultiLAD's advantage over contenders significantly increases when additional views are available, and iii) MultiLAD is highly robust to noise from individual views. In five real world dynamic graphs, we demonstrate that LAD and MultiLAD identify significant events as top anomalies such as the implementation of government COVID-19 interventions which impacted the population mobility in multi-view traffic networks.

**中文翻译**:

> 动态图是用于建模实体之间随时间演变的复杂关系的丰富数据结构。其中，时序图上的异常检测对许多现实应用至关重要，例如网络系统中的入侵识别、生态系统扰动检测和流行病暴发检测。本文聚焦于动态图中的变化点检测，并应对该问题的三大挑战：i) 如何跨时间比较图快照，ii) 如何捕获时间依赖性，iii) 如何融合时序图的不同视图。为解决上述挑战，我们首先提出拉普拉斯异常检测 (LAD)，它用图拉普拉斯矩阵的谱作为每个快照图结构的低维嵌入；LAD 通过两个滑动窗口显式建模短期与长期依赖。其次，我们提出 MultiLAD——LAD 面向多视图图的简单而有效的推广，是首个针对多视图动态图的变化点检测方法；它通过标量幂均值 (scalar power mean) 操作聚合来自不同视图的**归一化**图拉普拉斯矩阵的奇异值。通过大量合成实验，我们证明：i) LAD 与 MultiLAD 准确度高，并大幅优于最先进基线及其多视图扩展；ii) 视图数量增加时 MultiLAD 相对竞争者的优势显著扩大；iii) MultiLAD 对单个视图的噪声高度鲁棒。在五个真实世界动态图上，我们证明 LAD 与 MultiLAD 能把重大事件识别为最显著的异常，例如影响多视图交通网络中人口流动的政府 COVID-19 干预措施的实施。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：现实世界中政治、生物、化学、社会学等领域的关系都可建模为随时间演变的网络。随着社交媒体、公共卫生、交通等领域动态网络数据的增多，能够随时间识别异常的方法成为重要研究方向。动态图异常检测的目标是识别显著偏离图底层分布"正常/期望"行为的、随时间变化的实体。
- **变化点 vs 事件（论文给出的关键区分，沿用 [52] 定义）**：
    - **变化点 (change point)**：底层网络生成过程发生突变、且该新过程在此时点之后**持续延续**的时间点（$\cdots\simeq H_{t-2}\simeq H_{t-1};\ H_t\simeq H_{t+1}\simeq\cdots$）。
    - **事件 (event)**：网络显著偏离期望行为、但**之后又恢复正常**的一次性时间点（$H_{t-1};H_t$ 且 $H_{t-1}\simeq H_{t+1}$）。
- **三大核心挑战（论文明确提出）**：
    1. **如何跨时间比较图快照**——为不同时刻的图快照生成可比较的低维表示。已有的 activity vector 方法 [26] 用加权邻接矩阵 $W$ 的主特征向量作表示。
    2. **如何捕获时间依赖性**——事件与变化点的检测都需要同时与近期和远期快照比较。
    3. **如何融合时序图的不同视图**——现实中多个网络可描述同一组实体的关系（多视图 / multiplex 网络），但据作者所知，已有变化点检测方法 [2,25,26,40,52] 都只针对单视图动态网络。
- **多视图的两点动机（论文给出）**：① 不同来源的数据具有不同特征与价值，提供互补信息（如出租车与网约车记录刻画同一交通网络但人群不同）；② 单一来源噪声大，跨视图共有的异常更可信。简单地在异常分数层面做聚合（max / mean）不足以处理"视图分歧"问题，视图越多分歧越严重。

## 关键贡献

1. **提出 LAD**：用拉普拉斯矩阵的奇异值得到图快照的低维嵌入（签名向量），用于变化点检测。论文声称这是**首次将拉普拉斯谱用于变化点检测**。
2. **显式建模双重时间依赖**：用两个独立滑动窗口分别捕获短期与长期时间关系，从而同时检测事件与变化点。
3. **在 3 个合成任务 + 3 个真实数据集上评估 LAD**，证明其比当时最先进方法更有效。
4. **提出 MultiLAD**：把 LAD 推广到多视图设置，是**首个面向多视图动态网络的变化点检测方法**。它通过**标量幂均值**聚合各视图**归一化**拉普拉斯矩阵的奇异值，识别各视图中最有信息量的奇异值。
5. **在合成实验上评估 MultiLAD**，证明：① 视图越多性能增益越大；② 对噪声高度鲁棒；③ 大幅超过最先进单视图基线及其多视图扩展。
6. **在两个真实多视图交通网络上应用 MultiLAD**，正确检测出 COVID-19 居家令实施、圣诞节等重大交通扰动。
7. **开源**：LAD 与 MultiLAD 代码公开（github.com/shenyangHuang/LAD.git 与 .../multiLAD.git）。

## 方法

### 整体框架
LAD 的核心思想是从低维嵌入（称作**签名向量 / signature vector**）中检测高层图变化：先为每个时间步的图快照计算签名向量，再从签名向量流中提取短期与长期依赖下的"典型 / 正常"行为，最后比较当前签名向量相对正常行为的偏离程度作为异常分数。

### 输入输出
- **输入**：多视图动态图 $\mathcal{G}=\{\mathcal{G}_t\}_{t=1}^{T}$，其中 $\mathcal{G}_t=\{G_{t,r}\}_{r=1}^{m}$，$G_{t,r}=(V,E_{t,r})$ 是第 $t$ 步、第 $r$ 个视图（关系）的图。论文为表述清晰**假设节点集 $V$ 固定、各视图节点数相同**（但注明 MultiLAD 可处理该假设不成立的情形，见 Section 6.1）。边 $e=(i,j,w)$ 带正权 $w\in\mathbb{R}^+$。$A_{t,r}\in\mathbb{R}^{n\times n}$ 为邻接矩阵，$n=|V|$。当视图数 $m=1$ 时退化为单视图设置（同 [26,52]）。
- **输出**：异常分数序列；高分对应潜在变化点 / 事件。变化点检测目标是找到集合 $S\subseteq\{1,\dots,T\}$，使得对每个 $t\in S$，底层（不可观测的）生成模型 $H_t$ 相对此前显著不同且延续。

**1. 图嵌入：拉普拉斯谱（Laplacian Spectrum）**
- 定义（未归一化）拉普拉斯矩阵 $L=D-A$（$D$ 为度对角阵）。对 $L$ 做 SVD，用其奇异值向量作为该快照的图嵌入（签名向量）。
- 注意：**LAD 用未归一化拉普拉斯**；**MultiLAD 聚合的是归一化拉普拉斯的奇异值**（摘要明确写 normalized graph Laplacian）。
- **选择拉普拉斯谱的四点理由（论文逐条给出）**：
    1. 与拉普拉斯谱相关，而拉普拉斯谱与图的结构属性（社区结构、度分布、连通分量数、直径、顶点连通度等）根本相关——例如特征值 0 的重数 $k$ 等于图的连通分量数。对称半正定矩阵的奇异值与特征值一致。
    2. 编码了对拉普拉斯矩阵做低秩近似的压缩损失（Eckart–Young 定理：第 $(k+1)$ 个奇异值 $\sigma_{k+1}$ 对应最优秩-$k$ 近似在 2-范数下的重构误差），奇异值剧烈波动反映全局图结构的剧变。
    3. **节点排列不变**（对行列置换不变）——图学习的理想性质之一。
    4. 对真实稀疏矩阵可高效计算（稀疏 SVD）。

**2. 刻画正常行为（Characterizing Normal Behavior）**
- 对截至当前的拉普拉斯谱 $\sigma_0,\dots,\sigma_t\in\mathbb{R}^n$ 先做 **L2 归一化**得到单位向量。
- 构造上下文矩阵 $C\in\mathbb{R}^{n\times l}$（公式 (1)），其列为窗口内前 $l$ 步的签名向量 $[\sigma_{t-l},\dots,\sigma_{t-1}]$，$l$ 为窗口大小。
- 对 $C$ 做 SVD，取其**左奇异向量** $\tilde{\sigma}_t$ 作为"正常行为向量"（可解释为滑窗内谱的加权平均，沿用 [2]）。
- 用**两个独立滑动窗口**：**短期窗口**（编码最近趋势，捕获突变）与**长期窗口**（捕获相对长期模式的偏离），把当前签名向量与两个窗口的典型行为分别比较得到异常分数。窗口长度可按应用调整。
  *(据原文后续页线索：真实数据中常用短期窗口约 7 天、并只取 top 6 奇异值即可获得强性能；具体异常分数 $Z^*$ 的合成方式见 PDF p.13+，提取缓存未完整覆盖，待核。)*

**3. 多视图聚合（MultiLAD）**
- MultiLAD 在**得到各视图签名向量之后、计算异常分数之前**做视图融合。
- 先计算每个视图**归一化**拉普拉斯矩阵的奇异值作为视图特定特征向量，再用**标量幂均值 (scalar power mean)** 跨视图聚合，得到聚合向量；据此推断异常分数。直观上：跨视图一致的关键模式被保留，单视图噪声被削弱。
- 聚合后，MultiLAD 复用与 LAD 相同的异常检测流程（双滑动窗口 + 与正常行为比较），故可视为 LAD 的多视图推广。
  *(注：标量幂均值的具体公式 $\sigma_i^{agg}=(\frac{1}{m}\sum_r (\sigma_{r,i})^p)^{1/p}$ 形式与论文文字描述一致，但精确定义、$p$ 取值及其消融在提取缓存未覆盖的页中，待核。)*

### 训练与推理
- **无监督 / 免训练**：LAD 与 MultiLAD 均无需标签。窗口大小、幂均值参数等为超参，凭经验或验证集设定。
- **推理**：在线逐时间步处理——为新快照算签名向量（MultiLAD 先各视图算签名再聚合）→ 更新滑窗历史 → 与窗口内典型行为比较 → 输出异常分数。

### 与已有方法的差异（论文 Related Work 对照，Table 1）
- **vs. activity vector [26]（Idé & Kashima）**：后者用正加权邻接矩阵 $W$ 的主特征向量作 activity vector，只用一个短期窗口；LAD 改用拉普拉斯谱并显式构造长/短期两个窗口。
- **vs. TENSORSPLAT [30]**：把动态图视为高阶张量做 PARAFAC 分解得签名向量。多视图动态图可看作 4 阶张量，作者把它推广到多视图作为基线。
- **vs. SPOTLIGHT [14]**：聚焦异常子图（大 / 稠密子图的出现 / 消失），是相关但不同的任务；本文检测的是异常图快照（时间点）。
- **vs. EdgeMonitoring [52]（Wang et al.）**：将网络演化建模为一阶马尔可夫过程 + 蒙特卡洛采样，被视为当时变化点检测的 SOTA；但它要求所有时间步节点顺序一致且节点数恒定，在用户频繁增减的大型社交网络中易被违反；LAD 可处理节点数随时间变化。
- **vs. 多视图聚类 PML [34]（Mercado et al.）**：对多层图拉普拉斯取**矩阵幂均值**做谱聚类（静态图）；本文受其启发但改用**标量幂均值**处理动态图变化点检测。
- **vs. 多视图节点 / 实例异常检测 [20,43,45,48]**：它们检测异常节点；本文检测整图结构变化的异常时间戳。Sohn et al. [45] 的贝叶斯多层 SBM 仅限块结构网络，MultiLAD 适用于任意图（含 Barabási–Albert 等无已知社区结构的图）。
- **Table 1 性质对比**：论文用 multi-view / robust to noise / event / change point / evolving # nodes / node permutation invariant 六项性质对比 activity vector、TENSORSPLAT、EdgeMonitoring、LAD、MultiLAD，结论是**只有 MultiLAD 满足全部理想性质**。

## 实验

> 说明：提取缓存仅覆盖 PDF p.1-12（摘要、引言、相关工作、问题定义、LAD 第 4 章），实验章节（第 7、8 章）主要落在未覆盖页；以下数据集 / 结论部分来自原笔记全文补读时从 p.13-30 摘录的线索，已标注"据原文后续页，提取缓存未覆盖，待核"。

- **使用的数据集**：
    - **合成数据集**：三类合成任务（Pure / Hybrid / Resample 等，据原文 p.16 表头线索，待核），用于可控验证不同变化类型、噪声水平、视图数量下的性能。
    - **真实单视图数据集**：UCI Message（每天为一个时间点，共 59,835 条消息；据 [37] 取短期窗口 7 天，据 p.13 线索）、Senate co-sponsorship 网络（两位议员若共同提案则连边）、Congress（图 2 来自 Senate co-sponsorship 网络可视化）、NYC Transit 2015-2016（取自 SPOTLIGHT [14]）。LAD 在 UCI 与 Senate 实验中**仅用 top 6 奇异值 / 特征值**即获强性能（据 p.13-15 线索，待核）。
    - **真实多视图数据集**：NYC Transit 多视图交通网络，含四个视图——Green Taxi、Yellow Taxi、For Hire Vehicles、High Volume For Hire Vehicles（图 1）。摘要称共"五个真实世界动态图"。
- **对比方法**：单视图基线 activity vector [26]、TENSORSPLAT [30]、EdgeMonitoring [52]，以及它们的多视图扩展（max / mean / concat 等朴素聚合）。
- **评价指标**：检测到的变化点 / 事件与真实标注（或注入变化）的匹配程度；原笔记记为精度 / 召回 / F1（具体数值在提取缓存未覆盖页，待核）。
- **主结果（据摘要与后续页线索）**：
    - 合成实验中 LAD 与 MultiLAD **大幅优于**所有对比方法；MultiLAD 随视图增多优势扩大，且对单视图噪声高度鲁棒。
    - 真实实验中，**MultiLAD 准确把 2020-03-22（纽约州 "NYS on Pause" 计划首日、所有非必要岗位居家令生效日）识别为异常日**（图 1）；并能检出圣诞节等扰动。LAD 在 Senate 数据上能检出 2013、2015 等显著变化点（如 2015-10-19 加拿大大选自由党增 148 席的众议院数据，据 p.15 线索，待核）。
- **效率信息**：提取文本提到奇异值可由稀疏计算高效获得，复杂度分析见原文 Section 6.2（提取缓存未覆盖，待核）；据 p.14 线索，activity vector 方法需完整 SVD、计算昂贵。具体 FLOPs / 运行时间数字 PDF 提取文本未明确。

## 局限

- **固定节点假设的表述**：问题定义为表述清晰假设节点集固定、各视图节点数相同；论文虽称 MultiLAD 可处理该假设不成立的情形（Section 6.1），但该机制落在提取缓存未覆盖页，PDF 文本（已提取部分）未给出细节。
- **每步 SVD 的计算成本**：对每个图快照（每视图）都要做 SVD，超大规模动态图上可能成为瓶颈；论文有复杂度讨论（Section 6.2）但不在已提取文本中。
- **参数选择**：短/长期窗口大小、幂均值参数 $p$、取多少奇异值（如 top 6）、L2 归一化等需按数据调，已提取文本未给出自动化选参指导。
- **阈值 / 异常分数解释**：方法输出异常分数序列，把分数转为"是否变化点"通常需设阈值；已提取文本未讨论阈值选择策略。
- **视图 / 维度权重**：标量幂均值对所有视图同等聚合，未显式学习各视图或各奇异值维度的重要性权重。
- **真实数据领域偏窄**：真实多视图验证集中在交通网络；社交 / 生物等其他领域在已提取文本中未展示。

## 个人评论

1. **问题定义清晰且占位首发**：把多视图动态图的变化点检测形式化（区分 change point 与 event），并提供该问题的首个方法 MultiLAD，是清楚的"定义 + 基线"贡献。
2. **优雅的特征工程**：用拉普拉斯谱（奇异值）作图快照"指纹"——既有谱图理论支撑（连通分量数 = 0 特征值重数）、又对节点排列不变、还能稀疏高效计算，是少见的"可解释 + 可计算 + 敏感"三者兼得的设计。
3. **轻量的多视图聚合**：标量幂均值是一个几乎无参（仅一个 $p$）、可解释的聚合算子；"在特征层而非分数层聚合"这一选择回应了引言里 max/mean 分数聚合在视图分歧时失效的痛点，思想可迁移到多模态时间序列融合。
4. **双窗口的直觉**：短/长期双窗口分别对应 event（突变后恢复）与 change point（突变后延续），与论文对两类异常的定义形成漂亮的对应。
5. **可复现**：两套代码均开源，且本文是 KDD 2020 LAD 工作的扩展，方法成熟度较高。
6. **可改进方向**：缺少对视图 / 奇异值维度的自适应加权；阈值选择与超参（窗口、$p$、top-k）仍偏经验；真实评测领域偏窄。

### 使用建议

- **快速了解**：读摘要 + 引言（第 1 节）即可掌握问题、三大挑战、双方法与主结果。
- **复现**：重点读方法（第 4 章 LAD：公式 (1) 上下文矩阵、双滑窗；第 5 章 MultiLAD 的标量幂均值，本提取缓存未覆盖）及实验设置（第 7、8 章），并参考开源代码。
- **借鉴创新点**：① 把谱图理论（拉普拉斯谱）用于图序列分析；② 双滑窗同时捕短/长期模式；③ 标量幂均值做多视图 / 多模态特征融合。
- **写 related work**：可归入"动态图异常 / 变化点检测""多视图 / 多层图学习""谱图方法在机器学习中的应用"。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**图机器学习 / 谱图方法 + 时序异常（变化点）检测**的交叉方向，解决**动态图（尤其是多视图动态图）的变化点检测问题**——识别图底层生成过程发生显著且持续改变的时间点。它把谱图理论（拉普拉斯谱）与时间序列的滑动窗口比较相结合。这不是计算机视觉的图像变化检测，因此在本知识库中应归入 **`T_通用_NLP_其他`**（与同库的 [[2013_Quickest_Change_Poi]]、[[2014_Sequential_Detection]] 等统计 / CS 变化点检测论文同类），而非遥感 / 影像类的 `S_变化检测_ChangeDetection`。

## 2. 一句话总结
本文提出基于图拉普拉斯谱（奇异值）的单视图方法 LAD 与多视图方法 MultiLAD：LAD 用未归一化拉普拉斯的奇异值作签名向量、并用短/长期双滑动窗口检测变化点与事件；MultiLAD 用标量幂均值聚合各视图归一化拉普拉斯的奇异值，成为首个面向多视图动态图的变化点检测方法，对噪声鲁棒且视图越多优势越大。

## 3. 背景与问题
- **任务**：动态图异常检测，聚焦"变化点检测"——找到底层生成模型 $H_t$ 显著改变且延续的时间步。论文明确区分**变化点**（突变后延续：$H_{t-1};H_t\simeq H_{t+1}$）与**事件**（突变后恢复：$H_{t-1}\simeq H_{t+1}$）。
- **三大挑战（论文原话）**：i) 如何跨时间比较图快照；ii) 如何捕获时间依赖；iii) 如何融合时序图的不同视图。
- **多视图动机**：① 不同来源提供互补信息；② 单源噪声大，跨视图一致的异常更可信。朴素的分数级 max/mean 聚合在"视图分歧"下失效，视图越多越严重——这是 MultiLAD 在特征级聚合的直接动机。据作者所知，此前变化点检测方法 [2,25,26,40,52] 全是单视图。

## 4. 核心贡献
1. **LAD**：首次用拉普拉斯谱（奇异值）作图快照低维嵌入做变化点检测。
2. **双时间窗口**：短期 + 长期两个独立滑窗，同时检测事件与变化点。
3. **3 合成任务 + 3 真实数据集**评估 LAD，优于当时 SOTA。
4. **MultiLAD**：LAD 的多视图推广，**首个多视图动态图变化点检测方法**，用标量幂均值聚合各视图**归一化**拉普拉斯奇异值。
5. **合成实验**证明 MultiLAD 视图越多增益越大、对噪声鲁棒、大幅超单视图基线及其多视图扩展。
6. **两个真实多视图交通网络**上正确检出 COVID-19 居家令、圣诞节等扰动。
7. **开源**：LAD 与 MultiLAD 代码均公开。

## 5. 方法详解
### 整体框架
为每个时间步图快照算低维"签名向量"→ 从签名向量流中提取短/长期"正常行为"→ 比较当前签名向量与正常行为的偏离作为异常分数。

### 输入输出
- **输入**：多视图动态图 $\mathcal{G}=\{\mathcal{G}_t\}_{t=1}^T$，$\mathcal{G}_t=\{G_{t,r}\}_{r=1}^m$，$G_{t,r}=(V,E_{t,r})$，边带正权。为表述清晰假设节点集固定、各视图节点数相同（MultiLAD 可放宽，见 Section 6.1）。$m=1$ 退化为单视图。
- **输出**：异常分数序列；目标是找到 $H_t$ 显著改变的时间点集 $S$。

### 关键模块
**(1) 拉普拉斯谱（图嵌入）**：$L=D-A$，对 $L$ 做 SVD 取奇异值向量作签名向量。选它的四点理由：与图结构属性相关（0 特征值重数 = 连通分量数）、编码低秩近似压缩损失（Eckart–Young）、节点排列不变、稀疏高效。LAD 用未归一化 $L$；MultiLAD 聚合归一化 $L$ 的奇异值。

**(2) 正常行为刻画**：对截至当前的谱做 L2 归一化；构造上下文矩阵 $C\in\mathbb{R}^{n\times l}$（公式 (1)，列为前 $l$ 步签名向量）；对 $C$ 做 SVD 取左奇异向量 $\tilde\sigma_t$ 作正常行为向量（窗口内谱的加权平均）。用短期 + 长期两个独立窗口分别比较。*(异常分数 $Z^*$ 的精确合成、top-6 奇异值的使用在 PDF p.13+，提取缓存未覆盖，待核。)*

**(3) MultiLAD 多视图聚合**：各视图先算归一化拉普拉斯奇异值作视图特征 → 标量幂均值跨视图聚合 → 复用 LAD 的双滑窗异常检测流程。*(幂均值精确定义、$p$ 取值与消融在提取缓存未覆盖页，待核。)*

### 训练与推理
无监督、免训练；窗口大小 / 幂均值参数为超参。在线逐步：算签名（MultiLAD 先各视图后聚合）→ 更新滑窗 → 比较 → 输出分数。

### 与已有方法差异
activity vector [26]（邻接矩阵主特征向量 + 单短窗）、TENSORSPLAT [30]（张量 PARAFAC）、SPOTLIGHT [14]（异常子图，任务不同）、EdgeMonitoring [52]（一阶马尔可夫 + MC，要求固定节点顺序 / 数量，被视为 SOTA）、PML [34]（矩阵幂均值，静态多层聚类——本文改用标量幂均值做动态变化点）。Table 1：仅 MultiLAD 同时满足 multi-view / robust to noise / event / change point / evolving #nodes / permutation invariant 六性质。

## 6. 实验与结果
> 实验章节主要落在提取缓存未覆盖的 p.13-30；以下含原笔记从后续页摘录的线索，标"待核"。
- **数据集**：合成（Pure/Hybrid/Resample 等）；真实单视图 UCI Message（59,835 条消息、短窗 7 天）、Senate co-sponsorship、Congress（图 2）、NYC Transit 2015-2016；真实多视图 NYC Transit 四视图（Green/Yellow Taxi、For Hire、High Volume For Hire）；摘要称共五个真实图。
- **对比**：activity vector、TENSORSPLAT、EdgeMonitoring 及其多视图扩展（max/mean/concat）。
- **指标**：检测点与真实事件 / 注入变化的匹配（精度 / 召回 / F1，具体数值 PDF 提取文本未明确，待核）。
- **结果**：合成上 LAD/MultiLAD 大幅领先；MultiLAD 视图越多越好、抗噪强；真实上 **MultiLAD 把 2020-03-22（NYS on Pause 首日）识别为异常日**（图 1），LAD 在 Senate 上检出 2013/2015 等变化点（待核）；activity vector 需完整 SVD、昂贵（p.14 线索）。

## 7. 这篇论文真正有价值的地方
1. **范式 + 首发基线**：把多视图动态图变化点检测形式化，提供首个方法。
2. **拉普拉斯谱作"图指纹"**：可解释（连通分量 / 低秩近似误差）、排列不变、稀疏高效。
3. **特征级 vs 分数级聚合的洞察**：标量幂均值在特征层聚合，回应了分数级 max/mean 在视图分歧下失效的问题，思想可迁移到多模态融合。
4. **双窗口对应两类异常**：短窗 ↔ event，长窗 ↔ change point，设计与定义自洽。
5. **开源 + KDD 2020 扩展**：成熟、可复现。

## 8. 局限与问题
- 固定节点假设的放宽机制（Section 6.1）在已提取文本中无细节。
- 每快照 / 每视图 SVD 的成本，超大图可能成瓶颈（复杂度见 Section 6.2，未在已提取文本）。
- 窗口 / $p$ / top-k / L2 归一化等超参靠经验，无自动选参。
- 异常分数转判定需设阈值，未讨论阈值策略。
- 各视图 / 各奇异值维度未自适应加权。
- 真实评测偏交通领域，其他领域未展示。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言。
- **复现**：方法第 4/5 章（公式 (1)、双滑窗、标量幂均值）+ 实验第 7/8 章 + 开源代码。
- **借鉴**：谱图理论用于图序列；双滑窗捕短/长期；标量幂均值做多视图 / 多模态融合。
- **写 related work**：动态图异常 / 变化点检测、多视图 / 多层图学习、谱图方法。

## 10. 和其他论文的关系
- 本库中与统计 / CS 变化点检测论文同类：[[2013_Quickest_Change_Poi]]、[[2014_Sequential_Detection]]（序贯 / 快速变化点检测）。
- 论文内对比 / 引用的方法：activity vector（Idé & Kashima [26]）、TENSORSPLAT [30]、SPOTLIGHT [14]、EdgeMonitoring（Wang et al. [52]）、多视图聚类 PML（Mercado et al. [34]）、Sohn et al. [45] 的贝叶斯多层 SBM。
- 经典时间序列变化点检测（CUSUM 等）思想相关。
**注意**：本库其余论文与本文的双链以实际存在的笔记为准，未凭空臆造。

## 11. 关键词
动态图，多视图 / 多层图，变化点检测，事件检测，图异常检测，拉普拉斯谱，奇异值分解 (SVD)，谱图方法，标量幂均值 (scalar power mean)，短/长期滑动窗口，签名向量，节点排列不变，无监督。

## 12. 可信度说明
本笔记的 PDF 提取缓存仅覆盖前 12 页（约 40%）：摘要、引言（第 1 节）、相关工作（第 2 节）、问题定义（第 3 节）、LAD 方法（第 4 章至 4.2 节"刻画正常行为"，含上下文矩阵公式 (1)）。这些部分——论文动机、三大挑战、变化点 / 事件定义、LAD 的拉普拉斯谱与双滑窗、MultiLAD 的标量幂均值设计意图、Table 1 性质对比、各对比方法的差异——均有**直接文本依据**。
**限制**：① MultiLAD 标量幂均值的精确公式、$p$ 取值与消融（第 5 章），② 异常分数 $Z^*$ 的精确计算、top-6 奇异值的使用，③ 全部实验数值（F1 等）、复杂度分析（Section 6.2）、固定节点假设放宽机制（Section 6.1），均落在提取缓存未覆盖的 p.13-30；相关内容来自原笔记全文补读时的页面线索摘录，已逐处标"据原文后续页，提取缓存未覆盖，待核"。本次优化修正了原笔记把本文误归 CV 影像类 `S_变化检测` 的分类问题，并明确了 LAD（未归一化）与 MultiLAD（归一化）拉普拉斯的区别。

---

> **可信度补充**: PDF 提取质量 = **medium**（提取缓存仅覆盖 12/30 页，方法第 5 章与实验章节未覆盖，关键数值"待核"）; 来源缓存: `.paper-cache/extracts/2023_Laplacian_Change_Poi.txt` (头标 12/30 页, 25000 字符截断; 原文约 38122 字符); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-30; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-30。
- **提取情况**: 缺失页 18 页, 其中 18 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Laplacian Change Point Detection for Multi-view Dynamic Graphs 13
- p.13: 7.4 Real-world Experiments
- p.13: UCI Message and Senate co-sponsorship experiments, LAD is able to achieve strong performance using only the top 6
- p.14: May June July August September October
- p.14: The activity vector method requires full SVD which are computationally expensive and it is only able to detect
- p.15: Laplacian Change Point Detection for Multi-view Dynamic Graphs 15
- p.15: Equally, on October 19th 2015 an election took place and the Liberal party won an additional 148 seats, with a total
- p.15: 7.5 Summary of LAD Results
- p.15: In the UCI message and senate co-sponsorship experiments, LAD achieves strong performance using only the top 6
- p.16: Dataset Pure Hybrid Resample UCI Senate
- p.16: Lastly, synthetic experiment results suggest that LAD can be used in a hybrid environment where both change points
- p.16: 8 MULTI-VIEW EXPERIMENTS

### 缺失页关键摘录

- p.13: Fig. 3. LAD perfectly recovers all events and change points defined in Table 2.
- p.13: Here, we evaluate the performance of LAD on two real-world benchmark datasets, as well as an original dataset. For
- p.13: is the number of seats in the House of Commons of Canada. More information regarding each dataset can be found in
- p.13: 7.4.1 UCI Message .In this dataset, we treat each day as an individual time point. There are 59,835 total messages
- p.13: usernames, email and IP addresses were removed thus we use the dataset description provided in [ 37] to find significant
- p.13: events in the dataset. We select the short term window to be 7 days as suggested by Panzarasa et al . [37] . The long term
- p.13: Figure 4 shows the 𝑍∗scores predicted from both the short term and long term window (with top 6 eigenvalues).
- p.13: has strongest correlation to the average edge weight per snapshot in this dataset.
- p.13: 7.4.2 Senate co-sponsorship Network .In this dataset, an edge is formed between two congresspersons if they are
- p.14: From Figure 5, it is clear that LAD can easily detect the above change points (using only the top 6 singular values).
- p.15: LAD detects 2013 and 2015 as two significant change points. Figure 6 shows the 𝑍∗scores predicted by LAD. 2013 is
- p.15: Table 3 summarizes the empirical performances of LAD and its comparison to alternative methods. We observe that
<!-- AI_READING_NOTE_END -->
</content>
</invoke>
