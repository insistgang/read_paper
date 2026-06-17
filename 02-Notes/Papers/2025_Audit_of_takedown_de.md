---
title: Audit of takedown delays across social media reveals failure to
authors:
  - "Bao Tran Truong"
  - "Sangyeon Kim"
  - "Gianluca Nogara"
  - "Enrico Verdolotti"
  - "Erfan Samieyan Sahneh"
  - "Florian Saurwein"
  - "Natascha Just"
  - "Luca Luceri"
  - "Silvia Giordano"
  - "Filippo Menczer"
year: 2025
venue: "arXiv"
doi: 
pdf: [[2025_Audit_of_takedown_de.pdf]]
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/2025_Audit_of_takedown_de.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/19 pages"
---
# Audit of takedown delays across social media reveals failure to

> **完整题目**（frontmatter 因换行被截断，据 PDF p.1 补全）：*Audit of takedown delays across social media reveals failure to **reduce exposure to illegal content***
> **arXiv 标识**（据 PDF p.1）：arXiv:2502.08841v3 [cs.SI]，2 Feb 2026。这是一篇计算社会科学 / 在线平台治理论文（cs.SI 社会与信息网络），不是 CV/NLP 模型论文。

## 基本信息
- **PDF**: [[2025_Audit_of_takedown_de.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: ai-read (已 AI 全文覆盖, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Audit of takedown delays across social media reveals failure to reduce exposure to illegal content |
| **作者** | Bao Tran Truong; Sangyeon Kim; Gianluca Nogara; Enrico Verdolotti; Erfan Samieyan Sahneh; Florian Saurwein; Natascha Just; Luca Luceri; Silvia Giordano; Filippo Menczer |
| **机构** | Indiana University (Observatory on Social Media); TU Dresden; SUPSI/USI (Switzerland); Univ. of Bologna; Univ. of Zurich; USC (p.1) |
| **发表时间** | 2025 (arXiv v3 标注 2 Feb 2026) |
| **刊物/会议** | arXiv (预印本, cs.SI) |
| **DOI** | 未明确; arXiv:2502.08841 |

## 摘要

**清理后英文原摘要**（据 PDF 提取文本整理，修复断词与空格）：

> Illegal content on social media poses significant societal harm and necessitates timely removal. However, the impact of the speed of content removal on prevalence, reach, and exposure to illegal content remains underexplored. This study examines the relationship with a systematic audit of takedown delays using data from the EU Digital Services Act Transparency Database, covering five major platforms over a one-year period. We find substantial variation in takedown delay, with some content remaining online for weeks or even months. To evaluate how these delays affect the prevalence and reach of illegal content and exposure to it, we develop an agent-based model and calibrate it to empirical data. We simulate illegal content diffusion, revealing that rapid takedown (within hours) significantly reduces prevalence, reach, and exposure to illegal content, while the longer delays measured by the audit fail to reduce its spread. Though the link between delay and spread is intuitive, our simulations quantify exactly how takedown speed shapes exposure to illegal content. Building on these results, we point to the benefits of faster content removal to effectively curb the spread of illegal content, while also considering the limitations of strict enforcement policies.

**中文翻译**：

> 社交媒体上的非法内容造成严重的社会危害，需要及时移除。然而，移除速度对非法内容的**流行度（prevalence）**、**覆盖范围（reach）**和**用户暴露（exposure）**的影响一直缺乏研究。本研究利用欧盟《数字服务法》透明度数据库（DSA-TDB）的数据，对五大平台一整年的移除延迟进行系统审计来考察这一关系。我们发现移除延迟差异极大，部分内容可在线存留数周乃至数月。为评估这些延迟如何影响非法内容的流行度、覆盖范围与暴露，我们构建了一个基于代理的模型并用经验数据进行校准。模拟非法内容扩散后发现：**数小时内的快速移除**能显著降低流行度、覆盖与暴露，而审计中实测到的**较长延迟则无法遏制其传播**。延迟与传播之间的关联虽然直观，但我们的模拟精确量化了移除速度如何塑造对非法内容的暴露。在此基础上，我们既指出更快移除有助于有效遏制非法内容传播的益处，也讨论了严格执法政策的局限。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **这篇论文为什么要做**：非法内容（版权侵权、CSAM 儿童性虐待材料、煽动暴力/恐怖主义等）在社交媒体上造成严重危害，需要有效审核 (p.1)。监管框架普遍强调"及时"移除，但移除速度对非法内容流行度、覆盖、暴露的实际影响**至今没有经验数据**，使政策制定者难以设计和评估合适的政策 (p.1)。
- **之前方法有什么问题**：已有关于移除速度的研究 (引用 24–26) 大多聚焦于**错误信息/虚假信息**（误导性主张、阴谋论），其结论未必能推广到非法内容；且很多工作集中在**紧急事件**期间（如 COVID-19 反疫苗叙事、2021 年 1 月 6 日国会山骚乱），此时平台采取了例外措施 (p.1)。要为法律框架提供依据，需要考察平台在**常规、非紧急时期的标准操作流程**。此外，大规模实验研究内容移除政策在伦理上不可行（不能拿有害/非法内容做实验）且涉及隐私问题 (p.1)。
- **作者想解决的核心矛盾**：**监管对移除"及时性"的要求**（NetzDG/KoPl-G/Loi Avia 曾要求"明显非法"内容 24 小时内、其他非法内容 7 天内移除；DSA 第 16(6)、6(1) 条改为"及时"和"迅速"等更模糊表述，放弃了可强制执行的时限）与**平台实际操作中的较长延迟**之间的矛盾 (p.2)。作者旨在量化这种延迟并精确评估其对非法内容传播的后果。

## 关键贡献

1.  **首次跨平台系统审计非法内容移除延迟**：基于欧盟 DSA 透明度数据库（DSA-TDB）的案例级"理由声明"（SoRs），对 Facebook、Instagram、YouTube、TikTok、Snapchat 五大平台 **2024 全年**的非法内容移除记录进行审计，量化延迟分布（从数天到数周，部分长达一年）(p.2, p.4)。
2.  **开发并校准了内容移除传播模型**：扩展开源 `SimSoM` 基于代理的社交媒体模型，纳入内容移除机制；用 DSA-TDB 估计的**期望移除延迟 τ** 和政策报告估计的**非法内容概率 p** 校准参数 (p.2, p.5–6)。
3.  **量化了延迟与传播的陡峭非线性关系**：模拟揭示，随移除延迟增加，非法内容流行度与暴露**陡峭上升**；当延迟超过约两周（据数据是多数平台的典型延迟）后，移除对遏制传播的效果**变得可忽略** (p.2)。
4.  **指出监管框架改进方向并讨论其局限**：更快移除能有效遏制非法内容，DSA 等框架可能受益于更强的执法条款；但作者在讨论中也指出严格时限的局限，强调法律框架需在移除及时性、审核质量与平台运营约束间平衡 (p.2)。

## 方法

整体是图 1 所示的三步流水线 (p.3)。

- **整体框架**：
  1.  **(a) 经验数据校准**：从政策报告估计非法内容概率 p 的合理区间；从 DSA-TDB 的 SoRs 推断各平台的**期望移除延迟 τ**。模拟跑在从 Twitter 数据构建的关注网络上。
  2.  **(b) SimSoM 模拟扩散与移除**：基于代理的模型在网络上模拟内容传播。每个时间步非法内容以恒定概率 $p_s$ 存活（由 τ 校准）；一旦被移除即从所有用户 feed 中删除。
  3.  **(c) 移除效果估计**：在广泛的 τ 取值上跑模拟，把移除效果度量为非法内容流行度/暴露相对**无移除基线**的相对减少。

- **输入输出**：
  - **输入**：DSA-TDB 的 SoRs 记录（含 `content date` 发布时间戳与 `application date` 审核时间戳）；政策报告中的评论比例数据。
  - **输出**：不同移除延迟下，非法内容流行度（prevalence）、覆盖范围（reach）、曝光量（impressions）相对无移除基线的**减少百分比**。

- **关键模块**：
  1.  **移除延迟估计 (τ)**：延迟定义为 `application date`（审核日期）与 `content date`（发布日期）之差 (p.4)。经验上延迟符合**指数生存曲线** $P(t)\approx e^{-t/\tau}$，τ 即拟合 DSA-TDB 得到的期望延迟/平均存活时间 (p.5–6)。Fig.2 给出五平台延迟的 CCDF（绿点经验数据 + 紫线指数拟合）(p.6)。
  2.  **非法内容概率估计 (p)**：用 *Future of Free Speech* 政策报告 (32) 数据——德/法/瑞典三国 Facebook、YouTube 2023 年 6–7 月两周评论数据。由 $\frac{illegal}{total}=\frac{disappear}{total}\times(1-\frac{legal}{disappear})$ 估出非法内容比例，得到 **0.00002–0.009** 的宽区间（Table 1）。该法把所有"消失评论"都当潜在移除，故是**保守上界**。模拟在该区间内取值（排除 p=0.00002 因需过大网络），最终主模拟用 **p=0.01**；系统级指标对 p 基本不敏感 (p.4–5)。
  3.  **基于代理的传播与移除模型 (SimSoM)**：
      - 平台建模为**有向网络**（节点=账号，边=关注关系，可不对称）。每步用户可发原创、转发 feed 中内容或不动作；转发时从 feed 采样，被转发的消息出现在其粉丝 feed 中，故曝光取决于作者粉丝数。模型刻画真实排序算法行为——倾向转发"有吸引力、较新、热门"的消息 (p.5)。
      - **非法内容扩散**：每条消息带一个二元属性标记是否非法。不同类型非法内容吸引力不同（CSAM 极少被转发，版权媒体则高度吸引）；因缺乏合法性与吸引力相关性的数据，**简化假设两者独立** (p.5)。
      - **用户活动异质性**：给每个用户一个活跃度 a，服从幂律 $P(a)\sim a^{\gamma}$，由 2023 年 1 月 9 天内 **81,633,118 条帖子、37,882,999 个账号**的日均 Twitter 活跃度拟合得 **γ=2.85**；a<1 时以概率 a 转发一条，否则转发 ⌊a⌋ 条 (p.5)。注：非法发帖概率的个体分布用**两组 beta 分布**建模（高风险/低风险两群），并验证对均匀/异质/两群三种假设均鲁棒 (p.5)。
      - **随机移除机制（生存过程）**：每步非法内容以概率 $p_s$ 存活、以 $1-p_s$ 被移除，则存活至少 t 步的概率 $P(t)\approx p_s^{\,t}$。为匹配经验指数生存曲线，令 **$p_s=e^{-1/\tau}$**，即每步以 $1-e^{-1/\tau}$ 概率移除；移除后内容从所有 feed 删除 (p.5)。

- **模块间连接**：τ、p 作为外部参数输入模型。τ 通过 $p_s=e^{-1/\tau}$ 转化为每步移除概率。

- **数学机制直观解释**：τ 是内容在平台上的**平均存活时间**。模拟中每步都是一次"被清除"的机会，τ 越小，每步移除概率 $1-e^{-1/\tau}$ 越大，内容越快被清除。

- **训练方式**：非机器学习训练。"校准"指用经验估计的 τ、p 设定模拟参数 (p.2)。

- **推理流程**：在给定网络上模拟内容产生、传播、移除多步，直到非法内容流行度的指数移动平均收敛到稳态（$\rho=0.9$，$\epsilon=0.0001$），再统计指标。每组参数跑 **70 次无移除基线 + 70 次有移除**，取均值；均从随机初始条件开始 (p.6)。

- **和已有方法的差异**：与以往主要研究错误信息/紧急事件、且多看"通知到行动"时间（notice-to-action）的工作不同，本文聚焦非法内容、审计了**完整的发布到移除生命周期**（publication-to-removal），并在常规时期进行，结论更具普遍性 (p.1, p.4)。

## 实验

- **使用的数据集**：
  1.  **主要数据 (DSA-TDB)**：2024 年 1 月 1 日至 12 月 31 日的 SoRs，用最严格过滤（平台明确标注 `DECISION GROUND ILLEGAL CONTENT`）。五平台计数：**Facebook 8,613，Instagram 3,005，YouTube 408,400，Snapchat 2,142，TikTok 90,409** (p.4)。排除 LinkedIn、Pinterest（缺乏相关 SoRs）和 Twitter/X（DSA 数据存在可疑模式）；另排除 2,949 条 `content date` 无效（2000-01-01）的 TikTok 记录 (p.4)。注：超过 99% 的审核被标为"违反条款"而非"非法"，非法内容可能被低报。
  2.  **辅助数据**：*Future of Free Speech* 政策报告，用于估计 p（Table 1）(p.4)。
  3.  **网络数据**：从 10% 公开推文随机样本构建的关注网络，原始 58,296 节点 / 10,632,023 边；经 **k-core 分解（k=94 core）取 N=10,006 节点**，再随机删边匹配原密度，得 **E=1,809,798 边，平均每节点约 180 个好友/粉丝** (p.6)。

- **对比方法**：主对比即**无任何内容移除的基线**（baseline），减少百分比相对此基线计算 (p.6)。

- **评价指标** (p.6)：
  1.  **流行度 (Illegal content prevalence)** $I_t=\frac{1}{N}\sum_i f_{i,t}$：t 时刻各用户 feed 中非法内容比例的平均。
  2.  **曝光量 (Impressions)**：非法内容被看到的总次数（同一用户可被同一帖多次曝光）。
  3.  **覆盖范围 (Reach)**：至少看到一次非法内容的**唯一用户数**。
  三者均算相对无移除基线的减少百分比，如流行度减少 $=(\langle\bar I_{baseline}\rangle-\bar I_{removal})/\langle\bar I_{baseline}\rangle$。

- **主实验结果**：
  - 平台间移除延迟差异巨大，从几天到几周，部分内容在线时间长达一年 (p.2, 摘要)。Table 2（按类型/平台）示例：YouTube 版权侵权 375,531 条、延迟 276（单位据原文为天/时间步，提取未给单位）；隐私侵权 YouTube 17,737 条延迟 2,362、TikTok 14,174 条延迟 8 (p.6, Table 2)。
  - 模拟显示**数小时内的快速移除**能显著降低非法内容流行度、覆盖与暴露；而审计观测到的实际延迟（通常超过两周）带来的减少**微乎其微** (p.2, 摘要)。
  - 延迟与传播呈**陡峭非线性关系**：延迟从数小时增到数天时传播急剧上升；超过约两周后曲线变平，移除效果已不明显 (p.2)。
  - **具体百分比（如"减少超过 80%"/"少于 5%"）在提取文本前 12 页中未给出**；这些数字应是论文结果章节（Takedown fails to curb… 节及其图表）所述，**(据原文后续页, 提取缓存未覆盖, 待核)**。

- **消融实验/鲁棒性检查**（据 p.14–16 章节线索 + p.5 正文，提取缓存未完整覆盖）：对不同 p 值（Fig.S1，τ=2.89 中位延迟）、不同高风险群体规模 $s_H$（Fig.S2）、个体非法发帖概率的不同分布（近均匀/异质/两群）、以及网络结构均做了鲁棒性检验，主结论稳定 (p.5；附录 Robustness)。

- **泛化实验**：按 p.16–17 线索，比较了不同类型非法内容的延迟、以及不同国家 YouTube 用户的延迟（如"八天延迟"情形，模拟两两差异 P≥0.13 不显著）**(据原文后续页, 提取缓存未覆盖, 待核)**。

- **速度/参数量/FLOPs 等效率信息**：非深度模型，无此类信息。模拟规模信息见上（10,006 节点 / ~1.81M 边，每组 70+70 次运行）。

## 局限

1.  **数据依赖性与偏差**：依赖 DSA-TDB；超过 99% 内容被标"违反条款"而非"非法"，非法内容可能被**低报**，平台报告口径也不一致 (p.4)。p 的估计法把所有"消失评论"当移除，是上界，可能高估真实非法内容比例 (p.4)。
2.  **建模简化**：移除被建为**瞬时且完全生效**（删除后从所有 feed 消失），忽略复制重传、跨平台再上传等；假设内容合法性与吸引力**独立**，现实未必成立 (p.5)。
3.  **实验范围**：模拟基于**单一 Twitter 子网络**，虽做了鲁棒性检验，但能否完全推广到 YouTube（视频）、TikTok（算法推荐）等不同平台生态仍待验证。
4.  **政策层面权衡**：论文指出快速移除的益处，也承认严格时限可能降低审核精度、误伤合法言论（过度审核），但对这一平衡的探讨偏定性 (p.1 提到 speed–accuracy trade-off)。

## 个人评论

这篇论文的核心价值在于把一个**政策性问题（监管移除速度的实际效果）转化为可量化、可模拟的计算问题**，给出一套"审计 + 建模"的方法论范式：

1.  **用监管强制公开的数据（DSA-TDB SoRs）做实证洞察**，绕开了"不能拿非法内容做实验"的伦理/隐私障碍，也填补了以往缺乏大规模非法内容审核数据的空白。
2.  **搭建经验观测与传播理论模型的桥梁**：用指数生存模型拟合延迟分布、再经 $p_s=e^{-1/\tau}$ 转成模拟参数，是干净利落的"经验→机制"转换，值得迁移到其他干预（降权、加标签）的效果评估。
3.  **用精确模拟取代模糊直觉**：明确给出"延迟超过约两周后移除几乎失效"这一关键阈值，为 DSA 是否需要更强执法条款的讨论提供了量化依据。

可改进/可追问之处：合法性与吸引力独立、移除瞬时完全生效这两个假设较强，可能系统性低估"高吸引力非法内容"（如版权媒体）在延迟期内的真实扩散；模拟只用了一个 Twitter 子网，跨平台外推需谨慎。对后续研究的启发：同一框架可扩展到错误信息、可比较软/硬干预组合的边际效益。

### 使用建议

- **如果快速了解**：读**摘要 + 引言末段 + 讨论**，即可掌握"快速移除有效、两周后失效"的核心结论与政策含义。
- **如果复现**：精读方法的 "Estimating takedown delay…"、"Modeling social media diffusion"、"Modeling illegal content diffusion and removal"、"Simulation framework and metrics" 四节，以及附录的非法内容概率建模与鲁棒性检验；需获取 DSA-TDB 与 Future of Free Speech 报告数据，并基于开源 SimSoM 实现 $p_s=e^{-1/\tau}$ 的移除机制。
- **如果借鉴创新点**：学习其**把监管透明度数据与基于代理的传播模型结合**的思路，以及**用指数生存模型拟合延迟并转成每步移除概率**的技术细节。
- **如果写 related work**：归入**社交媒体内容审核**、**在线有害/非法信息传播与干预建模**、**计算社会科学 / 平台治理政策模拟**类文献。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文位于**计算社会科学、内容审核与在线平台治理**的交叉方向（arXiv 类别 cs.SI 社会与信息网络）。它要解决的核心问题是：**社交媒体上非法内容（CSAM、版权侵权、煽动暴恐等）的移除延迟，对其流行度、覆盖范围与用户暴露到底有多大实际影响——此前没有经验数据可依**。作者把一个监管政策问题（移除"及时性"要求 vs 平台实际延迟）操作化为：先对欧盟 DSA 透明度数据库做跨平台延迟审计，再用校准过的基于代理模型量化"延迟→传播"的因果效应。在本库 taxonomy 中，它不属于任何具体 CV 主题，归入 `T_通用_NLP_其他`（社会计算 / 信息传播 / 内容治理）。

## 2. 一句话总结
通过审计欧盟 DSA 透明度数据库（五平台 2024 全年）并构建校准过的 SimSoM 传播模型，本文证明：只有**数小时内**的快速移除才能显著降低非法内容的流行度、覆盖与暴露；而平台实测的较长延迟（通常超两周）几乎无法遏制其传播——延迟与传播呈陡峭非线性关系，越过约两周阈值后移除"形同失效"。

## 3. 背景与问题
- **为什么要做**：非法内容危害严重需有效审核；监管框架（NetzDG/KoPl-G/Loi Avia 旧时限、DSA 新表述）都强调"及时/迅速"，但**移除速度对流行度/覆盖/暴露的影响没有经验数据**，政策难以设计和评估 (p.1–2)。
- **之前方法的问题**：已有移除速度研究多聚焦**错误信息**且集中在**紧急事件**（COVID 反疫苗、国会山骚乱），结论难推广到常规时期的非法内容；大规模实验又因伦理/隐私不可行 (p.1)。已有数据多是"通知到行动"时间，覆盖不到"发布到移除"的完整在线时长 (p.4)。
- **核心矛盾**：监管对"及时性"的要求 vs 平台实际的较长延迟；DSA 用"timely/expeditiously"取代了硬性时限，作者要量化这一松动的后果 (p.2)。

## 4. 核心贡献
1.  **首次跨平台审计非法内容移除延迟**：基于 DSA-TDB 案例级 SoRs，覆盖 Facebook/Instagram/YouTube/TikTok/Snapchat 五平台 2024 全年，量化延迟分布（数天到数周，部分达一年）(p.2, p.4)。
2.  **校准内容移除的传播模型**：扩展 SimSoM，纳入随机生存式移除机制，用经验 τ 与政策报告 p 校准 (p.2, p.5–6)。
3.  **量化延迟–传播的陡峭非线性关系与"两周失效"阈值**：超过约两周延迟后移除效果可忽略 (p.2)。
4.  **给出监管含义并讨论其局限**：支持更强执法条款，同时指出严格时限对审核质量/合法言论的风险，需平衡 (p.2)。

## 5. 方法详解
三步流水线（Fig.1, p.3）：**(a) 经验校准 → (b) SimSoM 模拟扩散与移除 → (c) 效果估计**。

- **τ（移除延迟）**：定义为 `application date` − `content date`（审核 − 发布）(p.4)。经验延迟符合指数生存曲线 $P(t)\approx e^{-t/\tau}$，τ 由拟合 DSA-TDB 得到，Fig.2 给五平台 CCDF（绿点 + 紫线指数拟合）(p.5–6)。
- **p（非法内容概率）**：用 Future of Free Speech 报告（德/法/瑞典，FB/YT，2023 年 6–7 月两周评论），$\frac{illegal}{total}=\frac{disappear}{total}(1-\frac{legal}{disappear})$，得 0.00002–0.009 区间（Table 1，保守上界）；主模拟用 p=0.01，系统指标对 p 基本不敏感 (p.4–5)。
- **SimSoM 扩展**：
  - 有向关注网络，节点=账号、边=关注；每步用户发原创/转发/不动作，转发从 feed 采样、出现在粉丝 feed，曝光取决于作者粉丝数；倾向转发"吸引、较新、热门"的消息 (p.5)。
  - 每条消息带"是否非法"二元属性；**简化假设合法性与吸引力独立** (p.5)。
  - 用户活跃度 a 服从幂律 $P(a)\sim a^\gamma$，由 2023 年 1 月 9 天 81.6M 帖 / 37.9M 账号拟合得 **γ=2.85**；a<1 以概率 a 转发一条，否则 ⌊a⌋ 条 (p.5)。
  - 个体非法发帖概率用**两组 beta 分布**（高/低风险），对三种分布假设鲁棒 (p.5)。
  - **生存式移除**：每步存活概率 $p_s$、移除概率 $1-p_s$，$P(t)\approx p_s^t$；令 $p_s=e^{-1/\tau}$ 以匹配经验指数曲线，即每步以 $1-e^{-1/\tau}$ 移除，移除即从所有 feed 删除 (p.5)。
- **仿真设置**：网络由 10% 公开推文样本的关注网（原 58,296 节点 / 10.63M 边）经 k-core（k=94）取 N=10,006 节点、随机删边后 E=1,809,798（平均 ~180 度）；流行度指数移动平均收敛（ρ=0.9, ϵ=0.0001）即停；每组参数跑 70 次无移除基线 + 70 次有移除取均值 (p.6)。

## 6. 实验与结果
- **数据**：DSA-TDB 2024 全年 SoRs（最严格"非法"过滤）：FB 8,613 / IG 3,005 / YT 408,400 / Snapchat 2,142 / TikTok 90,409；排除 LinkedIn、Pinterest、Twitter/X，及 2,949 条无效日期 TikTok 记录 (p.4)。辅助：Future of Free Speech 报告（Table 1）。网络：上述 Twitter 子网 (p.6)。
- **对比**：无移除基线 (p.6)。
- **指标**：流行度 $I_t=\frac1N\sum_i f_{i,t}$、曝光量 Impressions、覆盖 Reach，均算相对基线的减少百分比 (p.6)。
- **结果**：
  - 平台延迟差异巨大（数天到数周，部分达一年）；Table 2 示例 YouTube 版权侵权 375,531 条延迟 276、隐私侵权 YouTube 17,737 条延迟 2,362 / TikTok 14,174 条延迟 8 (p.6)。
  - 数小时内快速移除显著降低流行度/覆盖/暴露；实测的较长延迟（通常超两周）减少微乎其微 (p.2, 摘要)。
  - 延迟–传播陡峭非线性，约两周后曲线变平、移除几乎失效 (p.2)。
  - **具体减少百分比未在提取的前 12 页给出**；论文结果章节（Takedown fails to curb…）及其图表中的精确数值 **(据原文后续页, 提取缓存未覆盖, 待核)**。
- **鲁棒性**（p.5 + 附录 p.14–16 章节线索，缓存未完整覆盖）：对 p 值（Fig.S1，τ=2.89 中位）、高风险群体规模 $s_H$（Fig.S2）、个体概率分布、网络结构均稳定。
- **泛化**：比较不同非法内容类型与不同国家 YouTube 延迟（如"八天延迟"，两两差异 P≥0.13 不显著）**(据原文后续页, 提取缓存未覆盖, 待核)**。
- **效率信息**：非深度模型，无参数量/FLOPs；规模为 ~1 万节点 / ~1.81M 边、每组 140 次运行。

## 7. 这篇论文真正有价值的地方
- **把监管政策问题操作化为可模拟的计算问题**，用 DSA 强制公开的透明度数据绕过实验伦理障碍，是内容审核研究方法论上的一次推进。
- **干净的"经验→机制"转换**：指数生存模型拟合延迟 → $p_s=e^{-1/\tau}$ 转成每步移除概率，使模拟生存曲线与真实数据严格对齐。
- **用精确模拟给政策定锚**：明确"约两周后移除失效"的阈值，把模糊的"越快越好"直觉变成可引用的量化阈值，直接对接 DSA 是否需更强执法条款的争论。

## 8. 局限与问题
1.  **数据偏差**：>99% 内容被标"违反条款"而非"非法"，非法内容低报，平台口径不一致 (p.4)；p 估计是上界、可能高估 (p.4)。
2.  **建模简化**：移除瞬时且完全生效，忽略复制/再上传；合法性与吸引力独立的假设较强，可能低估高吸引力非法内容的扩散 (p.5)。
3.  **范围**：单一 Twitter 子网，跨平台外推（YouTube 视频、TikTok 推荐）待验证。
4.  **政策权衡偏定性**：承认严格时限的 speed–accuracy 取舍与过度审核风险，但量化不足 (p.1)。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言末段 + 讨论。
- **复现**：精读方法四节 + 附录建模/鲁棒性；获取 DSA-TDB 与 Future of Free Speech 数据，基于 SimSoM 实现 $p_s=e^{-1/\tau}$ 移除。
- **借鉴创新点**：监管透明度数据 + 基于代理传播模型的结合；指数生存拟合 → 移除概率的转换。
- **写 related work**：内容审核 / 在线非法信息传播与干预建模 / 计算社会科学 · 平台治理政策模拟。

## 10. 和其他论文的关系
- **传播模型基础**：扩展自 SimSoM（引用 33），并参考其排序/分享行为建模（34）。
- **移除速度的前序工作**：引言引用 24–27（错误信息/紧急事件中的移除速度，如 COVID 反疫苗、国会山骚乱），本文与之的区别是聚焦非法内容、常规时期、完整发布-移除生命周期 (p.1)。
- **DSA 数据可信度**：引用 29、30 指出 Twitter/X DSA 数据可疑、非法内容低报问题；附录引用 Daphne Keller (41) 对 DSA 平台数据库实验的评论 (p.13 线索)。
- **非法内容流行度的稀缺证据**：引用 Wagner et al. (31)。
（注：提取缓存未含完整参考文献列表，具体编号对应的论文标题待核。）

## 11. 关键词
非法内容, 移除延迟 (takedown delay), DSA 透明度数据库 (DSA-TDB), 理由声明 (SoRs), 基于代理模型 (SimSoM), 指数生存过程, 内容审核, 社交媒体治理, 信息传播, 监管政策, 计算社会科学, 跨平台审计

## 12. 可信度说明
本篇精读主要基于 PDF 提取缓存（覆盖 p.1–12 的文本，实际文本截断在约 25,000 字符 / 正文第 6–7 页 Table 2 处）。提取质量良好、文本连贯，足以支撑论文定位、问题背景、核心贡献与**完整方法框架及全部校准参数/数据集计数**的准确理解，这些均能在提取文本逐条核对。
**需注意的局限**：提取缓存**未覆盖结果章节（Takedown fails to curb… 及其图表）、讨论、结论与完整参考文献**。因此笔记中关于**精确减少百分比、各平台具体 τ 数值、附录鲁棒性图（Fig.S1–S5）的具体结论、参考文献编号对应的论文**等内容，部分依据原笔记"全文补读记录"中的 p.13–19 章节线索与摘录，已显式标注 **(据原文后续页, 提取缓存未覆盖, 待核)**，未从完整 PDF 验证。

---

> **可信度补充**: PDF 提取质量 = **high** (提取缓存覆盖 p.1–12, 约 2086 字符/页, 文本连贯); 来源缓存: `.paper-cache/extracts/2025_Audit_of_takedown_de.txt` (标注 12/19 页, 截断于约 25,000 字符 / Table 2); 原 AI 主体 12/19 + 原"全文补读记录"含 p.13–19 章节线索; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。本次重读据提取文本核对并修正了网络规模(58,296→k-core 10,006/1.81M 边)、幂律指数 γ=2.85、各平台 SoRs 精确计数、70+70 次模拟、p_s=e^{-1/τ} 等细节, 并标注了提取未覆盖的结果数值。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-19; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-19。
- **提取情况**: 缺失页 7 页, 其中 7 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: Appendix
- p.14: Alternative platform compliance data
- p.14: However, despite formal compliance, reporting practices differ significantly across platforms, preventing
- p.14: To overcome these limitations, we instead rely on the DSA Transparency Database (DSA-TDB), as
- p.14: Illegal content probability modeling
- p.14: As there is limited access to data on illegal content, it is difficult to determine how such individual probability
- p.14: First, we consider a nearly homogeneous scenario in which all users have similar propensities to post illegal
- p.14: Third, we explicitly model population heterogeneity by distinguishing betweenhigh-riskandlow-risk
- p.14: We explore whether the main outcome variable is sensitive to these different assumptions about illegal
- p.14: Robustness
- p.14: The results presented in the main text may depend on the distributions of individual-level illegal posting
- p.14: For the following analyses varying high-risk group size and illegal content probability, we need a large

### 缺失页关键摘录

- p.13: [41] Daphne Keller. Rushing to launch the EU’s platform database experiment. Stanford Center for Internet
- p.14: time between notification and removal of content. As a result, they omit the substantial period during which
- p.15: Illegal content probability distribution020406080Prevalence reduction (%)Figure S1: Robustness of results with respect to different distributions ofpforτ= 2.89 (median takedown
- p.15: We wish to explore how the main result is affected by the volume of illegal content, which varies across
- p.15: platforms and countries. We run simulations with the empirical estimates ofpreported in Table 1 (except for
- p.15: scaling relationship between ¯Iremoval and¯Ibaseline in Fig. S3a for differentpvalues from Table 1. We observe
- p.15: Table 1. We observe more noise for smallp, but none of the differences between the values in our main
- p.15: comparable in size and average degree to the network used in the main experiment. In particular, we initialize
- p.16: High-risk group relative size (%)020406080Prevalence reduction (%)Figure S2: Robustness of results with respect to different high-risk group sizess Hforτ= 2.89 (median
- p.16: We wish to examine the variation in takedown delays across types of illegal content (Table 2). Fig. S5 and
- p.17: YouTube users from Germany, France, and Sweden, derived from the data reported in Table 1. Estimates of
- p.17: delay of eight days, bottom). The result does not vary significantly (P≥0.13 across pairs of simulations
<!-- AI_READING_NOTE_END -->
