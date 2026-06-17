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

## 基本信息
- **PDF**: [[2025_Audit_of_takedown_de.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Audit of takedown delays across social media reveals failure to |
| **作者** | Bao Tran Truong; Sangyeon Kim; Gianluca Nogara; Enrico Verdolotti; Erfan Samieyan Sahneh; Florian Saurwein; Natascha Just; Luca Luceri; Silvia Giordano; Filippo Menczer |
| **发表时间** | 2025 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Illegalcontentonsocialmediaposessignificantsocietalharmandnecessitatestimelyremoval. How- ever, the impact of the speed of content removal on prevalence, reach, and exposure to illegal content remainsunderexplored. Thisstudyexaminestherelationshipwithasystematicauditoftakedowndelays usingdatafromtheEUDigitalServicesActTransparencyDatabase,coveringfivemajorplatformsovera one-yearperiod. Wefindsubstantialvariationintakedowndelay,withsomecontentremainingonlinefor weeksorevenmonths. Toevaluatehowthesedelaysaffecttheprevalenceandreachofillegalcontentand exposure to it, we develop an agent-based model and calibrate it to empirical data. We simulate illegal content diffusion, revealing that rapid takedown (within hours) significantly reduces prevalence, reach, and exposure to illegal content, while the longer delays measured by the audit fail to reduce its spread. Though the link between delay and spread is intuitive, our simulations quantify exactly how takedown speed shapes exposure to ille

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：非法内容在社交媒体上造成严重危害，及时移除至关重要。监管机构和平台都强调“及时”移除，但实际操作中的延迟情况及其对内容传播的具体影响缺乏实证数据，这使得政策制定和评估缺乏依据 (p.1)。
- **之前方法有什么问题**：以往关于移除速度的研究主要集中在错误信息（如COVID-19相关虚假信息）或特定紧急事件期间，且多关注“通知-行动”时间，而非内容从发布到被移除的完整生命周期。这限制了研究结论对常规时期非法内容审核政策的指导意义 (p.1)。
- **作者想解决的核心矛盾**：**监管对移除“及时性”的要求**与**平台实际操作中存在较长延迟**之间的矛盾。作者旨在量化这种延迟，并精确评估其对非法内容传播造成的具体后果。
## 关键贡献

1.  **首次系统审计非法内容移除延迟**：基于欧盟《数字服务法》透明度数据库（DSA-TDB），对Facebook、Instagram、YouTube、TikTok和Snapchat五个主要平台在2024年一整年的非法内容移除记录进行了跨平台审计，量化了延迟分布（从数天到数周，甚至更长） (p.2, p.4)。
2.  **开发了校准于经验数据的传播模型**：扩展了`SimSoM`基于代理的模型，纳入内容移除机制，并利用DSA-TDB数据估计的平均移除延迟τ以及政策报告数据估计的非法内容概率p来校准模型参数 (p.2, p.5)。
3.  **量化了延迟与传播的非线性关系**：通过模拟揭示，非法内容的流行度、用户覆盖范围（Reach）和总曝光量（Impressions）随着移除延迟的增加而**非线性地急剧增长**，而当延迟超过约两周（这是数据中大多数平台的典型延迟）后，移除操作对遏制传播的效果**变得微乎其微** (p.2)。
4.  **指出了监管框架的潜在改进方向**：基于研究结果，指出更快的移除速度能有效遏制非法内容，但同时也讨论了严格移除截止日期的局限性，强调任何法律框架都需在移除及时性、审核质量以及平台运营现实之间取得平衡 (p.2, p.6)。
## 方法

本文的方法是一个三步流程，如图1所示 (p.3)。

- **整体框架**：
  1.  **经验数据校准**：从DSA-TDB中估计各平台的**平均移除延迟τ**；从外部政策报告中估计**非法内容概率p**。
  2.  **模拟传播与移除**：利用校准后的参数，在模拟的社交媒体网络中运行基于代理的模型，模拟非法内容的扩散和随机移除过程。
  3.  **评估移除效果**：对比有移除和无移除（基线）的模拟结果，计算非法内容流行度、覆盖范围等指标的减少百分比。

- **输入输出**：
  - **输入**：DSA-TDB中的“理由声明”（SoRs）记录（含内容发布和移除时间戳），以及政策报告中的内容比例数据。
  - **输出**：在不同移除延迟情景下，非法内容流行度、用户覆盖范围和总曝光量的**减少百分比**。

- **关键模块**：
  1.  **移除延迟估计模块 (τ)**：从DSA-TDB中，移除延迟定义为“审核日期”与“内容发布日期”之差 (p.4)。经验发现，延迟的累积分布函数（CCDF）符合指数分布 $P(t) \approx e^{-t/\tau}$，因此用指数分布拟合数据得到每个平台的平均延迟τ (p.5, p.6)。
  2.  **非法内容概率估计模块 (p)**：利用《未来言论自由》政策报告数据，通过“消失评论比例”和“其中合法评论比例”计算出非法内容的上界比例，在0.00002到0.009之间。最终模拟采用p=0.01 (p.4, p.5)。
  3.  **基于代理的传播与移除模型**：
      - 基于`SimSoM`模型，网络为有向图（用户为节点，关注关系为边）。用户发帖、转发或静默。信息通过新闻信息流传播 (p.5)。
      - **非法内容扩散**：每条消息标记是否非法。假设内容的合法性与其吸引力独立 (p.5)。
      - **用户活动异质性**：用户活跃度服从幂律分布，以模拟少量高活跃用户和大量低活跃用户的现实 (p.5)。
      - **随机移除机制**：为模拟延迟，在每个时间步，任何非法内容以概率 $1 - p_s$ 被移除。为使模拟的生存曲线与经验数据一致（指数分布），设定 $p_s = e^{-1/\tau}$。一旦内容被移除，将从所有用户的新闻信息流中删除 (p.5)。

- **模块间连接**：τ和p作为外部参数输入模型。τ通过 $p_s = e^{-1/\tau}$ 转化为模拟中的每一步移除概率。

- **数学机制直观解释**：参数τ代表了内容在平台上**平均**存活的时间。模拟中，每个时间步都像一次“开除”机会，τ越小，每一步的移除概率 $1 - e^{-1/\tau}$ 就越大，内容被快速清除的可能性越高。

- **训练方式**：这不是机器学习模型的训练。模型的“校准”是指使用从经验数据中估计出的参数（τ和p）来设定模拟的初始条件 (p.2)。

- **推理流程**：在给定的网络结构上，模型模拟多个时间步的内容产生、传播和移除过程，直到系统达到稳态（非法内容流行度稳定），然后统计相关指标 (p.6)。

- **和已有方法的差异**：与以往主要研究错误信息或紧急事件中“通知后响应”时间的研究不同，本文聚焦于非法内容，审计了**完整的发布-移除生命周期**，并在常规时期进行，结果更具普遍性 (p.1)。
## 实验

- **使用的数据集**：
  1.  **主要数据**：欧盟DSA透明度数据库（DSA-TDB）2024年1月1日至12月31日的“理由声明”记录。筛选了内容明确标记为非法的记录。最终数据集包括：Facebook 8,613条，Instagram 3,005条，YouTube 408,400条，TikTok 90,409条，Snapchat 2,142条 (p.4)。
  2.  **辅助数据**：《未来言论自由》政策报告，用于估计非法内容比例p (p.4, Table 1)。
  3.  **网络数据**：用于模拟的Twitter关注网络（约10,000个节点，180万条边）(p.6)。

- **对比方法**：主要对比基线，即在完全没有任何内容移除的情况下非法内容的传播水平 (p.6)。

- **评价指标**：
  1.  **非法内容流行度 (Illegal content prevalence)**：系统中非法内容的平均比例。
  2.  **曝光量 (Impressions)**：非法内容被用户看到的总次数。
  3.  **覆盖范围 (Reach)**：看到过非法内容的唯一用户数量。
  以上指标均计算相对于无移除基线的**减少百分比** (p.6)。

- **主实验结果**：
  - 平台间的移除延迟差异巨大，从几天到几周不等，部分内容在线时间可达一年 (p.2)。
  - 模拟显示，快速移除（延迟在几小时内）能显著降低非法内容的流行度、覆盖和曝光（减少超过80%）。然而，审计观测到的实际延迟（通常超过两周）带来的减少效果**微乎其微**（少于5%）(p.2)。
  - 移除延迟与内容传播之间存在**陡峭的非线性关系**：随着延迟从几小时增加到几天，非法内容的传播急剧增加；当延迟超过约两周后，曲线变得平缓，意味着移除操作的效果已不明显 (p.2)。

- **消融实验/鲁棒性检查**：文中提到对不同p值（非法内容概率）和不同用户风险分布假设进行了模拟，发现系统指标基本稳定，表明模型结果对这些假设是鲁棒的 (p.5, p.6)。

- **泛化实验**：PDF文本中未明确说明。

- **速度/参数量/FLOPs等效率信息**：PDF文本中未明确说明。
## 局限

1.  **数据依赖性与偏差**：依赖DSA-TDB数据，该数据可能存在偏差，例如平台可能倾向于报告更易处理的案例，或未完整报告所有非法内容审核 (p.4)。模型假设内容合法性与吸引力独立，这可能不总是成立 (p.5)。
2.  **模型简化**：基于代理的模型对现实世界进行了大量简化，例如移除是瞬间完成且完全生效，忽略了部分内容可被复制重新上传等情况。
3.  **实验范围**：模拟基于单一的Twitter子网络，尽管进行了鲁棒性检查，但结果能否完全推广至其他平台生态（如YouTube的视频分享、TikTok的算法推荐）有待进一步验证。
4.  **政策层面的复杂性**：论文指出了快速移除的好处，但也承认严格截止日期可能带来审核质量下降和误伤合法言论的风险，但对这一平衡的探讨更多是定性的。
## 个人评论

这篇论文最核心的价值在于它**将政策性问题（监管效果）转化为一个可量化、可模拟的技术研究问题**。它提供了一套方法论范式：
1.  **利用监管强制公开的数据（DSA-TDB）进行实证洞察**，解决了以往研究缺乏大规模非法内容审核数据的难题。
2.  **构建了连接经验观测与理论模型的桥梁**，通过参数校准使模拟能够反映真实平台的运营现状。
3.  **用精确的模拟结果取代了模糊的直觉**，明确指出了“延迟两周即失效”这一关键阈值，为政策讨论提供了强有力的量化依据。
对后续研究的启发是：可以借鉴这种“审计+建模”的方法来评估其他内容干预措施（如降权、标签）的效果；模型框架也可扩展用于研究不同类型内容（如错误信息）的审核策略。

### 使用建议

- **如果快速了解**：只读**摘要**和**结论/讨论**部分，即可掌握核心发现和观点。
- **如果复现**：重点阅读**方法**部分，特别是“Estimating takedown delay...”和“Modeling social media diffusion...”小节，以及附录（文中多次提及附录包含更多建模细节和鲁棒性检验）。需要获取DSA-TDB数据和政策报告数据。
- **如果借鉴创新点**：应学习其**如何将监管透明度数据与计算模型相结合**的研究思路，以及**用指数生存模型拟合延迟分布并转化为模拟参数**的技术细节。
- **如果写related work**：可放在**社交媒体内容审核**、**在线有害信息传播与控制**、**计算社会科学/政策模拟**等类别的文献综述中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**计算社会科学、内容审核和在线平台治理**的交叉研究方向。它旨在解决**社交媒体上非法内容（如CSAM、版权侵权等）移除延迟对内容传播和用户暴露的实际影响不明确**这一核心问题。论文结合对监管透明度数据的经验审计和基于代理的建模，为评估内容审核政策效果提供了新的量化工具。根据其研究内容（审计内容审核延迟、模拟信息传播），它可以被归类到主题 `T_通用_NLP_其他` 下，涉及网络信息传播、社会计算和内容审核等更广泛的领域。

## 2. 一句话总结
通过审计欧盟DSA透明度数据库和构建基于代理的模型，本文发现社交媒体平台对非法内容的移除延迟过长（通常为数天至数周），这种延迟未能有效减少非法内容的流行、覆盖范围和用户暴露，只有在数小时内移除才具有显著效果。

## 3. 背景与问题
- **这篇论文为什么要做**：非法内容在社交媒体上造成严重危害，及时移除至关重要。监管机构和平台都强调“及时”移除，但实际操作中的延迟情况及其对内容传播的具体影响缺乏实证数据，这使得政策制定和评估缺乏依据 (p.1)。
- **之前方法有什么问题**：以往关于移除速度的研究主要集中在错误信息（如COVID-19相关虚假信息）或特定紧急事件期间，且多关注“通知-行动”时间，而非内容从发布到被移除的完整生命周期。这限制了研究结论对常规时期非法内容审核政策的指导意义 (p.1)。
- **作者想解决的核心矛盾**：**监管对移除“及时性”的要求**与**平台实际操作中存在较长延迟**之间的矛盾。作者旨在量化这种延迟，并精确评估其对非法内容传播造成的具体后果。

## 4. 核心贡献
1.  **首次系统审计非法内容移除延迟**：基于欧盟《数字服务法》透明度数据库（DSA-TDB），对Facebook、Instagram、YouTube、TikTok和Snapchat五个主要平台在2024年一整年的非法内容移除记录进行了跨平台审计，量化了延迟分布（从数天到数周，甚至更长） (p.2, p.4)。
2.  **开发了校准于经验数据的传播模型**：扩展了`SimSoM`基于代理的模型，纳入内容移除机制，并利用DSA-TDB数据估计的平均移除延迟τ以及政策报告数据估计的非法内容概率p来校准模型参数 (p.2, p.5)。
3.  **量化了延迟与传播的非线性关系**：通过模拟揭示，非法内容的流行度、用户覆盖范围（Reach）和总曝光量（Impressions）随着移除延迟的增加而**非线性地急剧增长**，而当延迟超过约两周（这是数据中大多数平台的典型延迟）后，移除操作对遏制传播的效果**变得微乎其微** (p.2)。
4.  **指出了监管框架的潜在改进方向**：基于研究结果，指出更快的移除速度能有效遏制非法内容，但同时也讨论了严格移除截止日期的局限性，强调任何法律框架都需在移除及时性、审核质量以及平台运营现实之间取得平衡 (p.2, p.6)。

## 5. 方法详解
本文的方法是一个三步流程，如图1所示 (p.3)。

- **整体框架**：
  1.  **经验数据校准**：从DSA-TDB中估计各平台的**平均移除延迟τ**；从外部政策报告中估计**非法内容概率p**。
  2.  **模拟传播与移除**：利用校准后的参数，在模拟的社交媒体网络中运行基于代理的模型，模拟非法内容的扩散和随机移除过程。
  3.  **评估移除效果**：对比有移除和无移除（基线）的模拟结果，计算非法内容流行度、覆盖范围等指标的减少百分比。

- **输入输出**：
  - **输入**：DSA-TDB中的“理由声明”（SoRs）记录（含内容发布和移除时间戳），以及政策报告中的内容比例数据。
  - **输出**：在不同移除延迟情景下，非法内容流行度、用户覆盖范围和总曝光量的**减少百分比**。

- **关键模块**：
  1.  **移除延迟估计模块 (τ)**：从DSA-TDB中，移除延迟定义为“审核日期”与“内容发布日期”之差 (p.4)。经验发现，延迟的累积分布函数（CCDF）符合指数分布 $P(t) \approx e^{-t/\tau}$，因此用指数分布拟合数据得到每个平台的平均延迟τ (p.5, p.6)。
  2.  **非法内容概率估计模块 (p)**：利用《未来言论自由》政策报告数据，通过“消失评论比例”和“其中合法评论比例”计算出非法内容的上界比例，在0.00002到0.009之间。最终模拟采用p=0.01 (p.4, p.5)。
  3.  **基于代理的传播与移除模型**：
      - 基于`SimSoM`模型，网络为有向图（用户为节点，关注关系为边）。用户发帖、转发或静默。信息通过新闻信息流传播 (p.5)。
      - **非法内容扩散**：每条消息标记是否非法。假设内容的合法性与其吸引力独立 (p.5)。
      - **用户活动异质性**：用户活跃度服从幂律分布，以模拟少量高活跃用户和大量低活跃用户的现实 (p.5)。
      - **随机移除机制**：为模拟延迟，在每个时间步，任何非法内容以概率 $1 - p_s$ 被移除。为使模拟的生存曲线与经验数据一致（指数分布），设定 $p_s = e^{-1/\tau}$。一旦内容被移除，将从所有用户的新闻信息流中删除 (p.5)。

- **模块间连接**：τ和p作为外部参数输入模型。τ通过 $p_s = e^{-1/\tau}$ 转化为模拟中的每一步移除概率。

- **数学机制直观解释**：参数τ代表了内容在平台上**平均**存活的时间。模拟中，每个时间步都像一次“开除”机会，τ越小，每一步的移除概率 $1 - e^{-1/\tau}$ 就越大，内容被快速清除的可能性越高。

- **训练方式**：这不是机器学习模型的训练。模型的“校准”是指使用从经验数据中估计出的参数（τ和p）来设定模拟的初始条件 (p.2)。

- **推理流程**：在给定的网络结构上，模型模拟多个时间步的内容产生、传播和移除过程，直到系统达到稳态（非法内容流行度稳定），然后统计相关指标 (p.6)。

- **和已有方法的差异**：与以往主要研究错误信息或紧急事件中“通知后响应”时间的研究不同，本文聚焦于非法内容，审计了**完整的发布-移除生命周期**，并在常规时期进行，结果更具普遍性 (p.1)。

## 6. 实验与结果
- **使用的数据集**：
  1.  **主要数据**：欧盟DSA透明度数据库（DSA-TDB）2024年1月1日至12月31日的“理由声明”记录。筛选了内容明确标记为非法的记录。最终数据集包括：Facebook 8,613条，Instagram 3,005条，YouTube 408,400条，TikTok 90,409条，Snapchat 2,142条 (p.4)。
  2.  **辅助数据**：《未来言论自由》政策报告，用于估计非法内容比例p (p.4, Table 1)。
  3.  **网络数据**：用于模拟的Twitter关注网络（约10,000个节点，180万条边）(p.6)。

- **对比方法**：主要对比基线，即在完全没有任何内容移除的情况下非法内容的传播水平 (p.6)。

- **评价指标**：
  1.  **非法内容流行度 (Illegal content prevalence)**：系统中非法内容的平均比例。
  2.  **曝光量 (Impressions)**：非法内容被用户看到的总次数。
  3.  **覆盖范围 (Reach)**：看到过非法内容的唯一用户数量。
  以上指标均计算相对于无移除基线的**减少百分比** (p.6)。

- **主实验结果**：
  - 平台间的移除延迟差异巨大，从几天到几周不等，部分内容在线时间可达一年 (p.2)。
  - 模拟显示，快速移除（延迟在几小时内）能显著降低非法内容的流行度、覆盖和曝光（减少超过80%）。然而，审计观测到的实际延迟（通常超过两周）带来的减少效果**微乎其微**（少于5%）(p.2)。
  - 移除延迟与内容传播之间存在**陡峭的非线性关系**：随着延迟从几小时增加到几天，非法内容的传播急剧增加；当延迟超过约两周后，曲线变得平缓，意味着移除操作的效果已不明显 (p.2)。

- **消融实验/鲁棒性检查**：文中提到对不同p值（非法内容概率）和不同用户风险分布假设进行了模拟，发现系统指标基本稳定，表明模型结果对这些假设是鲁棒的 (p.5, p.6)。

- **泛化实验**：PDF文本中未明确说明。

- **速度/参数量/FLOPs等效率信息**：PDF文本中未明确说明。

## 7. 这篇论文真正有价值的地方
这篇论文最核心的价值在于它**将政策性问题（监管效果）转化为一个可量化、可模拟的技术研究问题**。它提供了一套方法论范式：
1.  **利用监管强制公开的数据（DSA-TDB）进行实证洞察**，解决了以往研究缺乏大规模非法内容审核数据的难题。
2.  **构建了连接经验观测与理论模型的桥梁**，通过参数校准使模拟能够反映真实平台的运营现状。
3.  **用精确的模拟结果取代了模糊的直觉**，明确指出了“延迟两周即失效”这一关键阈值，为政策讨论提供了强有力的量化依据。
对后续研究的启发是：可以借鉴这种“审计+建模”的方法来评估其他内容干预措施（如降权、标签）的效果；模型框架也可扩展用于研究不同类型内容（如错误信息）的审核策略。

## 8. 局限与问题
1.  **数据依赖性与偏差**：依赖DSA-TDB数据，该数据可能存在偏差，例如平台可能倾向于报告更易处理的案例，或未完整报告所有非法内容审核 (p.4)。模型假设内容合法性与吸引力独立，这可能不总是成立 (p.5)。
2.  **模型简化**：基于代理的模型对现实世界进行了大量简化，例如移除是瞬间完成且完全生效，忽略了部分内容可被复制重新上传等情况。
3.  **实验范围**：模拟基于单一的Twitter子网络，尽管进行了鲁棒性检查，但结果能否完全推广至其他平台生态（如YouTube的视频分享、TikTok的算法推荐）有待进一步验证。
4.  **政策层面的复杂性**：论文指出了快速移除的好处，但也承认严格截止日期可能带来审核质量下降和误伤合法言论的风险，但对这一平衡的探讨更多是定性的。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读**摘要**和**结论/讨论**部分，即可掌握核心发现和观点。
- **如果复现**：重点阅读**方法**部分，特别是“Estimating takedown delay...”和“Modeling social media diffusion...”小节，以及附录（文中多次提及附录包含更多建模细节和鲁棒性检验）。需要获取DSA-TDB数据和政策报告数据。
- **如果借鉴创新点**：应学习其**如何将监管透明度数据与计算模型相结合**的研究思路，以及**用指数生存模型拟合延迟分布并转化为模拟参数**的技术细节。
- **如果写related work**：可放在**社交媒体内容审核**、**在线有害信息传播与控制**、**计算社会科学/政策模拟**等类别的文献综述中。

## 10. 和其他论文的关系
根据提供的主题`T_通用_NLP_其他`和文件名，这篇论文可能与以下研究相关：
- 传播模型基础：论文扩展的`SimSoM`模型 [[SimSoM: A Simple Social Media Simulation Model]]。
- 内容审核研究：关于错误信息审核速度的研究 [[24, 25, 26, 27]]（引用在引言中，但具体论文未知）。
- DSA法规研究：其他对DSA实施效果或平台透明度进行分析的研究。
- 网络传播与干预：关于社交媒体网络中信息传播和干预措施建模的广泛文献。
（注：由于没有完整的引用列表，无法确定具体关联的论文，故使用一般性描述。）

## 11. 关键词
非法内容， 内容移除延迟， DSA透明度数据库， 基于代理的模型， 内容审核， 社交媒体治理， 信息传播， 监管政策， 计算社会科学， 模拟， 跨平台审计

## 12. 可信度说明
本篇精读笔记主要基于提供的PDF提取文本（前12页）生成，内容涵盖了论文的标题、作者信息、摘要、引言、方法部分的前半段以及图1和表1-2的数据。提取质量良好，文本连贯，能够支撑对论文定位、问题背景、核心贡献和方法框架的完整理解。
**需要注意的局限性**：由于提供的文本仅为论文的前部分，缺失了**完整的实验结果部分（包括所有结果图表）、讨论、结论以及参考文献列表**。因此，笔记中关于实验具体数字（如各平台精确的延迟τ值）、对结果的深度讨论以及与其他论文的详细关系等内容，是基于现有文本片段进行的合理推断或概括，未能从完整论文中获取并验证。后续部分的完整信息有待补充。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2025_Audit_of_takedown_de.txt` (19/19 页; 原 AI 主体 12/19 + 全文补读 13-19); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
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
