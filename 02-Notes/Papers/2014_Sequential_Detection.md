---
title: Sequential Detection of an Abrupt Change in a Random Sequence with Unknown Initial State
authors:
  - "James Falt"
  - "Steven D. Blostein"
year: 2014
venue: "arXiv (math.ST, arXiv:1401.6044)"
doi: 
pdf: [[2014_Sequential_Detection.pdf]]
primary_topic: N_雷达_无线电_张量_数学
topics:
  - "N_雷达_无线电_张量_数学"
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
extract_cache: .paper-cache/extracts/2014_Sequential_Detection.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/30 pages"
---
# Sequential Detection of an Abrupt Change in a Random Sequence with Unknown Initial State

## 基本信息
- **PDF**: [[2014_Sequential_Detection.pdf]]
- **primary_topic**: `N_雷达_无线电_张量_数学`
- **topics**: `N_雷达_无线电_张量_数学`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Sequential Detection of an Abrupt Change in a Random Sequence with Unknown Initial State |
| **作者** | James Falt; Steven D. Blostein (Senior Member, IEEE), Dept. of Electrical and Computer Eng., Queen's University, Kingston, ON, Canada |
| **发表时间** | 2014 (arXiv v4 标注 2017-12-08) |
| **刊物/会议** | arXiv:1401.6044v4 [math.ST] |
| **DOI** | 未明确 |

> 注: 提取缓存只覆盖 PDF 前 12 页 (共 30 页)。涉及后续页 (Section III 余下、Section IV 仿真、附录) 的内容均依据原笔记"全文补读记录"中的页面线索, 并明确标注"(据原文后续页, 提取缓存未覆盖, 待核)"。

## 摘要

清理后的英文原摘要 (修复空格与连字符断裂):

> The problem of sequentially detecting an abrupt change in a sequence of independent and identically distributed (IID) random variables is addressed. Whereas previous approaches assume a known probability density function (PDF) at the start of the sequence, the problem addressed is the detection of a single change in distribution among a finite number of known 'equal-energy' PDFs, but where the initial and final distributions are not known a priori. A Bayesian multiple hypothesis approach is proposed where (i) unlike previous threshold policies, the minimum cost hypothesis is tracked through time, (ii) under an exponential delay-cost function that satisfies an upper bound determined by the distances between hypotheses, the probability of detecting a change from an incorrect initial distribution asymptotically vanishes with time, (iii) computation is recursive and constant per unit time, and (iv) the unknown initial state gives rise to unavoidable incorrect detections that [can] be made to vanish with a constant test threshold with negligibly small effect on correct detection delay for change times beyond a lower bound. Simulations illustrate the analysis and reveal that average delay approaches that of the optimal CUSUM test after an initial transient period determined by an incorrect detection probability constraint.

中文翻译:

> 本文研究在一列独立同分布 (IID) 随机变量中顺序检测一个突变的问题。以往方法都假设序列开头的概率密度函数 (PDF) 已知; 本文所处理的问题是: 在有限多个已知的"等能量 (equal-energy)" PDF 之间, 检测分布发生的一次单一变化, 但初始分布与最终分布都事先未知。文中提出一种贝叶斯多假设方法, 其特点为: (i) 不同于以往的阈值策略, 它随时间跟踪最小代价假设; (ii) 在一个满足由假设间距离决定的上界的指数延迟代价函数下, 从错误初始分布检测出变化的概率随时间渐近趋于零; (iii) 计算是递归的, 每单位时间为常数计算量; (iv) 未知初始状态会带来不可避免的错误检测, 但可通过一个常数检验阈值使其消失, 同时对于超过某下界的变化时刻, 对正确检测延迟的影响可忽略不计。仿真验证了分析, 并表明: 经过一段由"错误检测概率约束"决定的初始瞬态期后, 平均延迟逼近最优 CUSUM 检验。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 经典的最快变化检测 (quickest change detection) 通常假设序列开头的初始 PDF 已知。但在不少实际场景中初始状态未知 —— 论文明确给出的例子是**认知无线电 (cognitive radio)**: $f_0$ 表示"只有噪声 (信道空闲, 无导频信号)"的分布, $f_1$ 表示"导频信号存在于同一背景噪声中"的分布; 观测开始时 $X_1$ 处于哪个状态是未知的。文献 [6] 已观察到: **若假设的初始状态错误, 最快检测性能会急剧 (drastically) 下降**。
- **之前方法的问题**:
    1. 已知初始状态的解法 (CUSUM [8]、minimax [9]、Bayesian [10][14] 等, 综述见 [12]) 都以初始 PDF 已知为前提。
    2. 对标准 ($D=2$) 问题的推广 [3][4] (变化后分布时变 / 变化前后非 IID) 仍假设初始 PDF 已知。
    3. 处理多次变化的 ON-OFF 过程 [13]、以及两个可能终态的 "2-sided test" [15]-[21] (含布朗运动漂移变化检测 [18]-[20]、去中心化版本 [21]), 即便变化本身是双向的, **初始状态仍被假定完全已知**。
    4. 阈值确定问题本身一般是难解的, 只有少数特例 (如先验 Bernoulli PDF + 几何变化时刻分布) 可精确给出虚警概率 [10][12][14]。
- **核心矛盾**: 如何在**初始分布与变化后分布均未知**的条件下, 设计一个能随时间积累信息、抑制错误初始状态假设、并快速正确检测变化的**因果 (在线) 顺序检测器**。论文给出的充分条件直觉是: 让"正确初始状态"对应的贝叶斯风险收敛, 同时让"错误初始状态"对应的风险无界发散, 从而随观测增多排除错误初始状态。
- **与早期版本的关系**: 本文扩展自作者早期会议版 [1][2]。[1] 在指数延迟代价模型下首次提出未知初始状态的贝叶斯检测器, 但仅限 $D=2$ 且只分析渐近行为 (对应本文 Theorem 1 的雏形); [2] 加入"初始状态不确定性代价"以降低初始状态误判概率。本文将其推广到 $D\ge2$ 个等能量、有限方差的 PDF, 并强化和完整化了性能分析。

## 关键贡献

1.  **未知初始状态下的贝叶斯多假设顺序检测框架**: 在时刻 $n$, 序列可能取 $M(n)=D+\frac{(n-1)D!}{(D-2)!}$ 个联合分布之一 —— 其中 $D$ 个对应"无变化"(全程同一 $f_j$), 其余 $\frac{(n-1)D!}{(D-2)!}$ 个对应在第一个样本之后某时刻发生一次 $(j,k)$ 变化 ($j\neq k$)。无变化假设记 $H_{1,n}(j)$ (式1), 单次变化假设记 $H_{m,n}(j,k)$ (式2)。论文明确定义了四类事件: 虚警、检测延迟、**终态误判**、**初始状态误判** (后者: 选中的假设其初始分布 $f_j$ 与真实初始分布不符, 无论终态/变化时刻是否正确)。
2.  **结构化代价函数, 含指数延迟代价与指数初始状态误判代价**: 代价 $L(H_1,H_2)$ (式11-14) 按四条规则给出 ——
    - 零代价: $H_1=H_2$;
    - 固定代价 $b$: 虚警 (同初/终态但 $H_1$ 变化时刻更早) 或终态误判 (同初态、不同终态);
    - 指数延迟代价 $a^{i}$ ($a>1$): 同初/终态但 $H_1$ 变化时刻晚于 $H_2$, $i$ 为延迟样本数;
    - 指数初始状态误判代价 $c^{i}$ ($c>1$): 两假设初态不同, $i$ 为两者分布相异的样本数 (式11 中按 $j,k$ 关系给出 $c^{m-1}$、$c^{n}$、$c^{n-m+1}c^{m-1}$ 等具体形式)。
    - 另设初始状态不确定性代价 $I(j,k)=\tau$ (当 $j\neq k$), $\tau>0$ (式15)。
3.  **常数时间复杂度的递归贝叶斯风险计算**: 虽然假设数 $M(n)$ 随 $n$ 线性增长, 但利用条件独立性 (式4,5), 风险可递归更新: 通过跟踪每个 $(j,k)$ 的**最小风险变化时刻** $m$ —— $R_{m,n}(j,k)=\min\{R_{n,n}(j,k),\,R_{m',n}(j,k)\}$ (式17, $m'$ 为 $n-1$ 时的最小风险变化时刻) —— 只需维护 $D+\frac{2D!}{(D-2)!}$ 个风险状态 (而非全部 $M(n)$ 个), 每单位时间计算量恒定, 与 $n$ 无关。完整递归细节见技术报告 [26]。
4.  **代价参数界限与权衡 (Section III)**: 通过对去掉公共因子 $1/P(X_{1,n})$ 后的"似然加权期望风险"求期望 (式19-26), 引入分布距离比 $d_i(j,k)\triangleq E_i[f_j(X)]/E_i[f_k(X)]$。Lemma 1 证明对等能量 PDF 有 $d_j(j,k)>1$ 且 $d_j(k,j)<1$。据此可给出 $a,c$ 的界限 (如 $1<c<d_{\min}$ 这一线索见后续页), 使正确初始状态假设的风险收敛、错误初始状态假设的风险发散, 从而错误初始状态检测概率随时间渐近消失。
5.  **Monte Carlo 仿真验证 (Section IV)**: 与已知初始状态的最优单边最快检测方法 (CUSUM [11][12]) 对比, 表明经过一段初始瞬态期后, 所提算法平均检测延迟逼近最优 CUSUM。具体图表与数值见"全文补读记录"(提取缓存未覆盖)。

## 方法

- **整体框架**: 贝叶斯多假设检验的顺序决策。在等先验 ($\pi\equiv\pi_1(j)=\pi_m(j,k)=1/M(n)$) 与等可能初态 ($\phi\equiv\phi(j)=1/D$) 假设下, 每个时刻 $n$ 计算各假设的后验风险, 选风险最小者。停止规则 (式10): 当某变化假设的最小风险小于所有无变化假设的最小风险时停止并宣布检测到变化:
$$\psi(n):\ \min\{R_{m,n}(j,k)\}_{(j,k)\in S^2,1<m\le n}\ <\ \min\{R_{1,n}(i)\}_{i\in S}$$
- **输入输出**: 输入是顺序观测的随机序列 $X_1,X_2,\dots$, 每个 $X_i$ 服从 $D$ 个已知等能量 PDF $f_j$ ($j\in\{0,\dots,D-1\}$) 之一, 满足 $E_i[f_i(X)]=E_j[f_j(X)]$ 且方差有限。输出是某时刻 $n$ 判定的假设: $H_{m,n}(j,k)$ (变化发生在 $m$, 初态 $f_j$ 变为 $f_k$) 或 $H_{1,n}(j)$ (无变化)。
- **关键模块**:
    1.  **假设与后验风险定义**: 由 Bayes 规则 (式3) 写出后验概率, 似然按独立性因式分解 (式4,5)。后验风险 $R_{1,n}(j)$ (式8) 和 $R_{m,n}(j,k)$ (式9), 后者额外含初始状态不确定性风险项 $\sum_r I(j,r)P(H_{1,m-1}(r)|\cdot)$。
    2.  **代价结构** (式11-15): 方法核心, 用指数代价把"延迟"和"错误初始状态"编码进风险, 使不期望假设的风险随样本数指数增长。
    3.  **递归贝叶斯风险计算** (式16-18): $R_{1,n}(j)$ 的展开式 (式16) 与 $R_{m,n}(j,k)$ 的完整展开式 (式18) 均可用最新观测 $x_n$ 递归更新; 对 $R_{n,n}(j,k)$ 而言式18 中 $m+1$ 到 $n$ 的求和项省略。
- **数学公式与机制直观解释**:
    - **指数延迟代价 $a^i$**: 强制算法积累足够证据后尽早正确检测, 避免无谓拖延 (体现于式16 中 $a^{n-i+1}$ 项)。
    - **指数初始状态误判代价 $c^i$**: 针对未知初始状态的关键设计。当假设以 $f_j$ 为初态但真实初态为 $f_r\neq f_j$ 时, 两分布相异产生的"证据"使该假设代价 $c^i$ 指数增长, 抑制其风险。
    - **分布距离比 $d_i(j,k)=E_i[f_j(X)]/E_i[f_k(X)]$** (式27): 期望风险分析的核心量。Lemma 1 给出 $d_j(j,k)>1,\ d_j(k,j)<1$, 决定了正确/错误初态风险项的收敛或发散方向; $a\cdot d_j(k,j)$ 这类乘积项 (见式末期望风险展开) 决定延迟代价项是否收敛。
- **推理流程**:
    1. 初始化参数 $a,b,c,\tau$ 与初始风险。
    2. 顺序接收观测 $x_n$。
    3. 对每个跟踪的假设 ($D$ 个无变化 $H_{1,n}(j)$ 与 $\frac{2D!}{(D-2)!}$ 个带最小风险变化时刻的 $H_{m,n}(j,k)$), 用递归式更新风险。
    4. 由式17 求各 $(j,k)$ 的新最小风险变化时刻。
    5. 由式10 比较两类最小风险; 变化假设更小则停止并报告检测。
    6. 否则回到步骤2。
- **和已有方法的差异**:
    - **处理未知初始状态**: 与 CUSUM、Page's test 等已知初态检测器根本不同。
    - **多假设跟踪**: 不只检测是否变化, 还同时估计变化时刻 $m$、初态 $j$、终态 $k$。
    - **成本驱动**: 不基于似然比/统计量阈值, 而基于结构化后验风险最小化。
    - **递归 + 常数复杂度**: 通过跟踪最小风险变化时刻把状态数固定为 $D+\frac{2D!}{(D-2)!}$。

## 实验

- **使用的数据集**: Section IV 使用 Monte Carlo 仿真 (合成数据)。提取缓存未覆盖具体生成分布; 据原文后续页 (p.19) 提到"the PDFs (35)", 即使用了式 (35) 定义的一组 PDF (具体形式提取缓存未覆盖, 待核)。
- **对比方法**: 与已知初始状态的最优单边最快检测方法 CUSUM [11][12] 对比 (p.10 明确)。据原文后续页 (p.22), CUSUM 阈值选为 $10^{2.157}$ (待核)。
- **评价指标**: 据原文后续页线索 (提取缓存未覆盖, 待核): **平均检测延迟 (Average Detection Delay)** (Figure 1, 横轴为 Change Time)、**错误检测概率 (Probability of Incorrect Detection)** (Figure 2, 随参数 $\tau$ 变化)、**虚警率 (False Alarm Rate)** (Figure 3)。
- **主实验结果**: 提取缓存只到 p.12, 不含图表数值。描述性结论 (摘要/引言): 经过初始瞬态期后, 平均延迟逼近最优 CUSUM。据原文后续页线索 (p.19): 对给定变化时刻, 平均检测延迟随之增大; 每个 $\tau$ 值都达到一个错误检测概率的最小值 (待核)。
- **消融实验**: 可视作对 $\tau$ 等参数的扫描 (Figure 2 显示不同 $\tau$ 的错误检测概率), 但提取缓存未覆盖具体设置 (待核)。
- **泛化实验**: PDF 文本中未提及。
- **效率信息**: 算法被描述为"computation is recursive and constant per unit time"(p.1); 每步复杂度由跟踪 $D+\frac{2D!}{(D-2)!}$ 个风险状态决定。未给出墙钟时间/FLOPs。

## 局限

1.  **强假设 (equal-energy)**: 所有候选 PDF 须满足 $E_i[f_i(X)]=E_j[f_j(X)]$ (等能量, 即内积 $\langle f_j,f_j\rangle$ 对所有 $j$ 相等, Lemma 1 前提)。该条件不满足时的行为论文未讨论。
2.  **参数选择**: 算法依赖 $a,b,c,\tau$。论文给出参数下界的理论分析 (Section III), 但承认全联合优化是难解的 (intractable); 实际如何在界限内选取以达到期望的延迟-虚警权衡仍需调参/先验知识。
3.  **状态数随 $D$ 增长**: 每步复杂度对 $n$ 为常数, 但跟踪的状态数 $D+\frac{2D!}{(D-2)!}$ 随候选分布数 $D$ 快速增长, 限制 $D$ 很大时的应用。
4.  **仅合成数据验证**: 实验限于 Monte Carlo 仿真, 缺乏真实世界数据 (如真实认知无线电采集) 的验证。
5.  **依赖分布间距离**: 性能 (延迟) 取决于分布距离 $d_i(j,k)$; 分布过于接近时检测困难, 且据原文后续页 (Theorem 2) 存在不可约的最小变化时刻 (irreducible minimum change time), 早于此变化时刻无法保证性能 (待核)。

## 个人评论

1.  **问题定义的价值**: 系统化地把"初始状态与终态都未知"的单次变化顺序检测问题公式化, 并明确区分了虚警、延迟、终态误判、初始状态误判四类事件, 为后续研究设定了清晰框架。
2.  **代价结构设计思想**: 把"渐近性能保证"编码进代价函数 —— 用指数代价 ($a,c>1$) 使不期望假设 (尤其错误初始状态) 的风险发散从而被淘汰 —— 是很强的思路。它把"无法直接估计的初始状态不确定性"转化为一个可调的损失项, 而非去显式估计未知参数。
3.  **递归实现**: 在多假设、代价依赖历史的复杂情形下, 通过只跟踪最小风险变化时刻把状态数固定, 实现常数复杂度递归, 是在线贝叶斯决策的一个可行范例。
4.  **对后续研究的启发**: 面对模型不确定性 (如初始状态未知) 时, 可通过设计合适的损失函数显式约束/引导检测过程, 而不必直接估计不确定参数。
5.  **可读性提醒**: 论文符号密集 (式11-18 一连串求和), 复现门槛主要在式16-18 的递归与技术报告 [26]; 若只用其思想 (指数代价淘汰错误初态), 读到 Section II 末与 Section III-A 即可。

### 使用建议

- **如果快速了解**: 读 Abstract、Section I 末几段 (本文方法定位)、Section II 开头 (问题建模, 式1-2 与 $M(n)$)。
- **如果复现**: 重点看 Section II 全部 —— 代价结构 (式11-15) 与风险递归 (式16-18); 并参考技术报告 [26] 获取完整递归细节。
- **如果借鉴创新点**:
    - 将不确定参数的负面影响转化为代价函数设计的思路;
    - 用指数代价获得渐近性能保证的方法;
    - 多假设框架下用"最小风险变化时刻"实现常数复杂度递归的技巧。
- **如果写 Related Work**: 可归类为"未知初始状态的变化检测"或"贝叶斯顺序假设检验", 与 CUSUM [8]、Lorden minimax [9]、Moustakides 最优平均延迟 [11]、ON-OFF 多变化 [13]、2-sided test [15]-[21] 并列讨论。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[N_雷达_无线电_张量_数学]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**统计信号处理 / 数理统计 (arXiv 分类 math.ST)** 中的**顺序变化检测 (sequential / quickest change detection)** 方向。核心问题: 在一列 IID 随机变量中, 当序列的**初始分布**和**变化后的最终分布都未知**时, 如何快速、准确地检测一个单一的分布变化。问题落在"变化检测 / 顺序分析 / 假设检验"主题下, 唯一给出的具体应用是**认知无线电的频谱感知** (噪声-only 与有导频信号两种状态)。鉴于本仓库 taxonomy 无统计学专门主题, 而本方向兼具"数学"与"无线电"属性, 归入 `N_雷达_无线电_张量_数学` 比泛化的 `T_通用_NLP_其他` 更贴切。

## 2. 一句话总结
针对初始与最终分布都未知的 IID 随机序列, 本文提出一种贝叶斯多假设顺序检测方法: 通过递归计算各假设的后验风险, 并用指数延迟代价 ($a$) 与指数初始状态误判代价 ($c$) 结构化代价函数, 使错误初始状态的检测概率随时间渐近消失, 且每单位时间计算量恒定。

## 3. 背景与问题
- **为什么要做**: 经典最快检测假设初始 PDF 已知; 但认知无线电等场景中初始状态 ($X_1$ 是噪声-only 还是含导频) 未知, 且文献 [6] 表明假设错误初态会使检测性能急剧下降。
- **之前方法的问题**:
    1. 已知初态解法 (CUSUM [8]、minimax [9]、Bayesian [10][14], 综述 [12]) 都要求初始 PDF 已知。
    2. 对 $D=2$ 标准问题的推广 [3][4] 仍假设初始 PDF 已知。
    3. ON-OFF 多变化 [13] 与两终态 "2-sided test" [15]-[21] 均假设初始状态完全已知。
    4. 精确虚警概率的阈值确定一般难解, 仅少数特例 ([10][12][14]) 可得。
- **核心矛盾**: 在初始与终态分布均未知下, 设计因果在线检测器, 让正确初态对应风险收敛、错误初态对应风险发散, 从而随观测增多排除错误初态。

## 4. 核心贡献
1.  **未知初态贝叶斯多假设框架**: 假设空间 $M(n)=D+\frac{(n-1)D!}{(D-2)!}$ (式起自 p.4-5); 无变化 $H_{1,n}(j)$ (式1)、单次变化 $H_{m,n}(j,k)$ (式2); 明确定义虚警、延迟、终态误判、初始状态误判四类事件。
2.  **结构化代价函数** (式11-15): 固定虚警/终态代价 $b$、指数延迟代价 $a^i$ ($a>1$)、指数初态误判代价 $c^i$ ($c>1$)、初态不确定性代价 $\tau$。
3.  **常数时间递归** (式16-18): 只跟踪 $D+\frac{2D!}{(D-2)!}$ 个风险状态 (用最小风险变化时刻 $m$, 式17), 每步复杂度与 $n$ 无关; 细节见 [26]。
4.  **参数界限与权衡** (Section III): 引入 $d_i(j,k)=E_i[f_j]/E_i[f_k]$ (式27), Lemma 1 给 $d_j(j,k)>1,\ d_j(k,j)<1$; 据此定 $a,c$ 界限使错误初态风险发散。
5.  **Monte Carlo 仿真**: 与最优 CUSUM [11][12] 对比, 瞬态期后平均延迟逼近 CUSUM (具体数值在提取缓存未覆盖页)。

## 5. 方法详解
- **整体框架**: 等先验、等可能初态下的贝叶斯多假设检验; 停止规则式10: 变化假设的最小风险 $<$ 无变化假设的最小风险时停止报告。
- **输入输出**: 输入 IID 序列 $X_1,\dots$, 每个 $X_i$ 服从 $D$ 个等能量 PDF $f_j$ 之一 ($E_i[f_i(X)]=E_j[f_j(X)]$, 方差有限); 输出 $H_{m,n}(j,k)$ 或 $H_{1,n}(j)$。
- **关键模块**:
    1.  **假设与后验风险**: Bayes 规则式3, 似然按独立性分解 (式4,5); 风险 $R_{1,n}(j)$ (式8)、$R_{m,n}(j,k)$ (式9, 含初态不确定性项 $\sum_r I(j,r)P(H_{1,m-1}(r)|\cdot)$)。
    2.  **代价结构** (式11-15): 用 $a^i,c^i,b,\tau$ 把延迟与错误初态编码进风险。
    3.  **递归计算** (式16-18): 用最新 $x_n$ 递归更新; $R_{n,n}(j,k)$ 时省略式18 中 $m+1\to n$ 的求和。
- **机制直观**:
    - $a^i$: 惩罚延迟, 促使尽早正确检测。
    - $c^i$: 真实初态 $f_r\neq f_j$ 时, 分布相异证据使该假设代价 $c^i$ 指数增长。
    - $d_i(j,k)$ (式27): 期望风险分析核心; Lemma 1 决定收敛/发散方向, $a\cdot d_j(k,j)$ 之类乘积项决定延迟代价收敛性。
- **推理流程**: 初始化 $a,b,c,\tau$ → 接收 $x_n$ → 递归更新 $D+\frac{2D!}{(D-2)!}$ 个风险 → 式17 求最小风险变化时刻 → 式10 决策 → 循环。
- **和已有方法差异**: 处理未知初态; 多假设联合估计 $(m,j,k)$; 后验风险最小化而非阈值统计量; 固定状态数的常数复杂度递归。

## 6. 实验与结果
- **数据集**: Monte Carlo 仿真 (合成); 据原文后续页 p.19 用式 (35) 定义的 PDF (具体形式提取缓存未覆盖, 待核)。
- **对比方法**: 已知初态的最优 CUSUM [11][12] (p.10); 据原文 p.22, CUSUM 阈值取 $10^{2.157}$ (待核)。
- **评价指标** (据原文后续页, 提取缓存未覆盖, 待核): 平均检测延迟 (Fig.1, 横轴 Change Time)、错误检测概率 (Fig.2, 随 $\tau$)、虚警率 (Fig.3)。
- **主结果**: 提取缓存只到 p.12, 无图表数值; 描述性结论 —— 瞬态期后平均延迟逼近最优 CUSUM; 据 p.19, 平均延迟随给定变化时刻增大, 每个 $\tau$ 达到一个错误检测概率最小值 (待核)。
- **消融/泛化**: 可视作对 $\tau$ 的扫描 (Fig.2); 无泛化实验。
- **效率**: 递归、每单位时间常数计算; 无墙钟时间/FLOPs。

## 7. 这篇论文真正有价值的地方
1.  **问题定义本身**: 首次系统化"初态与终态都未知"的单次变化顺序检测, 四类错误事件定义清晰, 数学公式化严谨。
2.  **代价结构设计思想**: 把渐近性能保证编码进代价函数, 用指数代价 ($a,c>1$) 让错误初态风险发散被淘汰; 把"无法估计的初态不确定性"转化为可调损失项。
3.  **递归实现**: 多假设、历史依赖代价下用最小风险变化时刻把状态数固定, 实现常数复杂度递归, 是在线贝叶斯决策的可行范例。
4.  **对后续研究启发**: 面对模型不确定性, 可设计损失函数显式约束/引导检测, 而非直接估计未知参数。

## 8. 局限与问题
1.  **强假设 equal-energy**: 须 $E_i[f_i(X)]=E_j[f_j(X)]$ (Lemma 1 前提); 不满足时行为未讨论。
2.  **参数选择**: 全联合优化 intractable; 界限内如何选 $a,b,c,\tau$ 达到延迟-虚警权衡仍需调参。
3.  **状态数随 $D$ 增长**: $D+\frac{2D!}{(D-2)!}$ 随 $D$ 快速增长。
4.  **仅合成数据**: 限 Monte Carlo, 无真实数据验证。
5.  **依赖分布距离**: 性能取决于 $d_i(j,k)$; 据 p.16-17 存在不可约最小变化时刻 (Theorem 2), 早于此无法保证性能 (待核)。

## 9. 我该怎么使用这篇论文
- **快速了解**: Abstract + Section I 末几段 + Section II 开头 (式1-2, $M(n)$)。
- **复现**: Section II 全部 (式11-15 代价、式16-18 递归) + 技术报告 [26]。
- **借鉴创新点**: 不确定参数→代价函数设计; 指数代价→渐近保证; 最小风险变化时刻→常数复杂度递归。
- **写 Related Work**: 归类"未知初始状态的变化检测"/"贝叶斯顺序假设检验", 与 CUSUM [8]、Lorden minimax [9]、Moustakides [11]、ON-OFF [13]、2-sided test [15]-[21] 并列。

## 10. 和其他论文的关系
- 经典已知初态基线: Page CUSUM [8]、Lorden minimax 最优性 [9]、Moustakides 等最优平均延迟 [11][22][23]; 本文是它们在未知初态下的扩展与对比对象。
- 多变化 / ON-OFF 过程 [13]: 相关但 [13] 仍假设初态已知。
- 两终态 2-sided test [15]-[21] (含布朗运动漂移 [18]-[20]、去中心化 [21]): 变化双向但初态已知。
- 指数延迟代价模型 [24]: 本文借用并扩展其代价结构以涵盖初态不确定性。
- 应用关联: 认知无线电频谱感知 [6][7] (其中 [6] 即作者团队对多频段多传感器频谱感知的性能评估), 初态未知是核心难题。
- 自身前身: 会议版 [1] ($D=2$, 渐近) 与 [2] (加初态不确定性代价); 本文推广到 $D\ge2$。

## 11. 关键词
顺序检测, 最快变化检测, 未知初始状态, 等能量 PDF, 贝叶斯多假设检验, 后验风险, 指数延迟代价, 指数初态误判代价, 递归常数复杂度, 最小风险变化时刻, 平均检测延迟, 错误检测概率, CUSUM, 认知无线电频谱感知

## 12. 可信度说明
本笔记的"摘要、研究背景、问题公式化 (Section II 全部: 式1-18)、代价结构 (式11-15)、风险递归 (式16-18)、参数分析起始 (Section III-A: 式19-27, Lemma 1)"均**严格基于提取文本 (PDF p.1-12)**, 可信度高。提取缓存只覆盖前 12 页 (共 30 页), 以下信息在提取文本中**未覆盖**, 本笔记凡引用处均标注"(据原文后续页, 提取缓存未覆盖, 待核)":
- 完整的仿真设置、具体结果数值与三张图 (Section IV, p.18-24 线索): 仿真 PDF 式(35)、CUSUM 阈值 $10^{2.157}$、Fig.1-3 的延迟/错误检测概率/虚警率曲线。
- 参数界限的完整证明与 Theorem 2 (不可约最小变化时刻, p.16-17)。
- $1<c<d_{\min}$ 这一参数选择线索 (p.14)。
- 技术报告 [26] 中的完整递归伪代码。
因此"实验与结果"一节的具体数字均为待核状态; 其余各节均依据所提供文本总结。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2017 字符/页)); 来源缓存: `.paper-cache/extracts/2014_Sequential_Detection.txt` (提取 12/30 页; 原 AI 主体 12/30 + 全文补读 13-30 依页面线索); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-30; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-30。
- **提取情况**: 缺失页 18 页, 其中 18 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: Next, we need to establish
- p.14: Rm,n(j,k)P(X1,n)/bracketrightbig
- p.14: We then have
- p.16: For any particular risk corresponding to change, when the re cursively tracked time is small,
- p.16: DKL/parenleftbig
- p.16: In Theorem 2, a value of the minimum change time (32) is used to showcase performance
- p.17: Nevertheless, from Theorem 2, there exists an irreducible m inimum change time required for
- p.19: For the PDFs (35) and parameter values selected in Section IV -A, Figures 1, 2, and 3 plot
- p.19: From Figure 1 it is clear that average detection delay increa ses for any given change time
- p.20: Change TimeAverage Detection Delay
- p.20: CUSUM
- p.20: Figure 3 shows the false alarm rates achieved by the proposed change detection scheme for

### 缺失页关键摘录

- p.14: cost function deﬁnition. It can similarly be shown that choo sing1<c<d minwill result in the
- p.18: compared with observed results and trends. Finally, Sectio n IV-D provides summary discussion.
- p.18: requires knowledge of the change time, which is unrealizabl e, this is only used as a benchmark;
- p.19: From Figure 1 it is clear that average detection delay increa ses for any given change time
- p.19: Observing Figure 2, it is clear that each value of τachieve a minimum probability of incorrect
- p.20: Figure 3 shows the false alarm rates achieved by the proposed change detection scheme for
- p.22: for CUSUM in Figure 3 is there to justify the selected CUSUM th reshold of 102.157for the
- p.22: presented in the proof of Theorem 2. As pointed out previousl y from Figure 2, once the initial
- p.23: with Figure 2, (36) is a loose upper bound: incorrect detecti on probabilities for τ= 101and
- p.24: from Figure 2 it can be observed that, for each value of τ, the incorrect detection rate achieved
- p.30: [6] J. K. Liang and S. Blostein, “Performance evaluation of m ultiband multi-sensor spectrum sensing systems,” in IEEE
<!-- AI_READING_NOTE_END -->
