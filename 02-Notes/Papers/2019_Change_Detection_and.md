---
title: "Change Detection and Notification of Web Pages: A Survey"
authors:
  - "Vijini Mallawaarachchi"
  - "Lakmal Meegahapola"
  - "Roshan Madhushanka"
  - "Eranga Heshan"
  - "Dulani Meedeniya"
  - "Sampath Jayarathna"
year: 2019
venue: "ACM Computing Surveys (ACM Comput. Surv., Vol. 53, No. 1, Article 15)"
doi: 10.1145/xxxxxxx
pdf: [[2019_Change_Detection_and.pdf]]
primary_topic: S_变化检测_ChangeDetection
topics:
  - "S_变化检测_ChangeDetection"
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
extract_cache: .paper-cache/extracts/2019_Change_Detection_and.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/35 pages"
---
# Change Detection and Notification of Web Pages: A Survey

## 基本信息
- **PDF**: [[2019_Change_Detection_and.pdf]]
- **primary_topic**: `S_变化检测_ChangeDetection`
- **topics**: `S_变化检测_ChangeDetection`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Change Detection and Notification of Web Pages: A Survey |
| **作者** | Vijini Mallawaarachchi; Lakmal Meegahapola; Roshan Madhushanka; Eranga Heshan; Dulani Meedeniya; Sampath Jayarathna |
| **机构** | The Australian National University (澳); Idiap Research Institute & EPFL (瑞士); University of Moratuwa (斯里兰卡); Old Dominion University (美) |
| **发表时间** | 2019 (December) |
| **刊物/会议** | ACM Computing Surveys, Vol. 53, No. 1, Article 15（35 页）；arXiv:1901.02660v4 [cs.IR] |
| **DOI** | 10.1145/xxxxxxx |

## 摘要

> **英文原摘要（据 PDF 提取文本整理）**：The majority of currently available webpages are dynamic in nature and are changing frequently. New content gets added to webpages, and existing content gets updated or deleted. Hence, people find it useful to be alert for changes in webpages that contain information that is of value to them. In the current context, keeping track of these webpages and getting alerts about different changes have become significantly challenging. Change Detection and Notification (CDN) systems were introduced to automate this monitoring process, and to notify users when changes occur in webpages. This survey classifies and analyzes different aspects of CDN systems and different techniques used for each aspect. Furthermore, the survey highlights the current challenges and areas of improvement present within the field of research.

> **中文翻译**：当前绝大多数网页本质上是动态的、内容频繁变化——新内容被添加、已有内容被更新或删除。因此，对包含自己关心信息的网页保持"变化警觉"对人们很有用。但在当下，持续追踪这些网页并获得各类变化的提醒已变得相当困难。变化检测与通知（Change Detection and Notification, CDN）系统正是为自动化这一监控过程、并在网页发生变化时通知用户而提出的。本综述对 CDN 系统的各个方面以及每个方面所用的不同技术进行了分类与分析，并进一步指出了该研究领域当前面临的挑战和可改进之处。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：万维网快速演进，网站日益动态化、内容持续变化，用户希望追踪自己关心网页（新闻、预订、维基、博客等）的创建/更新/删除。早年（1990s）人们靠 RSS 订阅追踪更新，2005 年起 Atom 取代 RSS，当前大多数用户改用浏览器书签——但这两类传统手段都已难以胜任高效监控 (p.1-2)。
- **之前方法的问题**：
    1.  **RSS/Atom**：一项对 web 联合（syndication）行为与内容的研究表明，RSS 的 XML 规范字段利用率低，导致信息缺失、错误和"未分类的 feed"；加之微博/社交媒体兴起、格式从 XML 转向 JSON、市场力量推崇专有接口而弱化互操作性，RSS 走向衰落（如 Google Reader 已停服）(p.2)。
    2.  **搜索引擎**：理论上多数搜索引擎底层也有变化检测机制，但其目的是决定爬哪些站点、维持搜索结果新鲜度，而非直接向用户提供变更通知；搜索引擎为"搜索网页"而生，CDN 为"监控网页变化"而生 (p.2)。
- **核心矛盾**：网页内容日益动态多样，与用户需要**便捷、高效、可定制**的监控通知手段之间存在矛盾。CDN 系统（如 Google Alerts、Follow That Page、Visualping）虽已广泛使用，但缺乏对其各方面特性的全面、统一评估 (p.2)。

## 关键贡献

1.  **CDN 领域综合性综述框架**：作者指出此前针对网页 CDN 的综述很少（仅 Oita et al.、Shobhna & Chaudhary 等），且难以找到覆盖多方面的综合评估。本文按 Figure 1 的结构系统梳理 CDN 的各个方面——网页动态性、架构、变化检测技术（爬取/检测/调度/变化频率估计）、通知技术、变化可视化、现有系统对比、趋势与未来方向 (p.3-4)。
2.  **三大研究目标**：①给出 CDN 系统不同特性的全面概览；②研究现有 CDN 系统并评估其特性与各项性能；③评估 CDN 的不同方面、考察新趋势、指出待改进领域 (p.3)。
3.  **总结网页动态性的大规模实证研究**：汇总 Cho & Garcia-Molina、Fetterly、Olston & Pandey、Adar、Elsas & Dumais、Saad & Gançarski 等多项大规模长期爬取研究（见 Table 1），为 CDN 设计提供数据基础 (p.7)。
4.  **梳理现有商用 CDN 系统能力**：归纳 Wachete、VisualPing 等系统的监控选项（监控范围、内容类型、变化阈值、监控频率、通知频率）(p.2)。

> 说明：贡献 2、3 在提取文本（p.1-8）有直接依据；对架构/检测算法/调度的逐项对比（Table 3-6）位于 p.13 及以后，提取缓存未覆盖，见下方"全文补读记录"。

## 方法

本文是综述，不提出新技术，而是剖析、分类 CDN 系统的通用方法（提取文本覆盖到 p.8 的"网页动态性"，架构与检测技术的细节在 p.9 以后，下文据原文后续页标注）。

- **CDN 系统定义与定位**：CDN 系统自动检测网页变化并通知关心的用户，使用户无需反复刷新即可获知变更，从而减少浏览时间 (p.2)。
- **典型工作流**：CDN 系统通过**爬取**获取网页各版本→将数据以"带标签的文档"（非结构化）形式存入**版本库**→把版本数据转成类 XML 结构（元素对应 HTML 开/闭标签，如 `<h>...</h>`）→用**相似度计算**比较旧版本与最新版本→若变化超过用户设定的**阈值**则触发通知 (p.2-3)。
- **两类架构（按部署位置）**：①**服务端变化检测**：服务器轮询网页、跟踪变化并通知用户；②**客户端变化检测**：由客户端基础设施自行轮询网页、跟踪变化 (p.2-3)。
- **现有系统的监控选项**（以 Wachete、VisualPing 为例，p.2）：
    1. 监控范围：网页的多个部分 / 整张网页 / 多个网页 / 整个网站；
    2. 监控内容：文本、图片、链接、文档（PDF、DOC、DOCX）；
    3. 变化阈值：网页发生变化的百分比；
    4. 监控频率：每小时 / 每天 / 每周 / 每月 / 按需；
    5. 通知频率：每天两次 / 每天一次 / 每周一次 / 一有变化就通知。
- **调度的关键问题**：多数系统按用户或系统预设的固定计划爬取，但网页更新频率差异很大；因此 CDN 需要**变化频率估计**机制来生成高效的检查计划，减少"无变化的空检查"、提升资源利用率 (p.3)。
- **变化可视化（通用做法）**：文本变化常用绿色高亮新增、红色（常带删除线）标注删除 (p.3)。
- **与 RSS/Atom 的差异**：CDN 不依赖内容方发布标准化更新源，而是主动监控任意网页，监控对象与频率更灵活 (p.2)。

## 实验

本文为综述，**未做新实验**，但系统总结了"网页动态性"的关键实证研究（Section 2.2 与 Table 1，p.7-8 提取文本完整覆盖）：

- **Cho & Garcia-Molina (2000)**：爬取来自 270 个网站的 **720,000** 个网页，连续每天爬取 **4 个月**；发现每次访问时 >20% 网页有变化、**40%** 网页在一周内变化，但 >50% 的 `.com`/`.edu` 网页在整个实验期内未变 (p.7)。
- **Fetterly et al. (2003)**：扩展上述研究，用约 **1.5 亿**网页、跨 **11 周**；约 **65%** 页面零变化；`.org`/`.gov` 比 `.edu` 更不易变，含垃圾内容（spam）的页面变化更频繁 (p.7)。
- **Olston & Pandey**：分别从 Yahoo 爬取集合与 Open Directory 各取 **10,000** 个 URL；Open Directory 动态内容中约三分之一表现出 "scroll" 行为 (p.7)。
- **Adar et al. (2009)**：爬取并分析约 **55,000** 个被用户回访的网页；**34%** 无任何变化，其余页面平均每 **123 小时**至少变化一次；**流行网页（体育、新闻、个人页）变化最频繁**，政府/教育域名网页变化不频繁 (p.7)。
- **Elsas & Dumais (2010)**：构建约 **200 万** HTML 页面，每周爬取共 **10 周**；>**62%** 页面无实质差异；高相关文档比一般文档更易变、变化幅度更大；最终提出面向动态文档的、按时间维度差异化加权的排序检索模型 (p.7)。
- **Saad & Gançarski (2012)**：监控法国电视台（FranceTV）档案 **100** 个网页，每小时爬取、每天获 **3000+** 版本；档案根层（如首页）显著变化，最深层页面几乎不变 (p.8)。
- **总体结论**：网页变化行为与网站类型、顶级域名性质高度相关——流行/新闻类站点更新快，政府/教育类站点变化少 (p.8)。
- **关于具体 CDN 系统的定量对比**（准确率/召回率、系统横向 benchmark）位于第 7 节等后续页（p.13+），提取缓存未覆盖，本节无法据提取文本给出 (据原文目录第 7 节，提取缓存未覆盖，待核)。

## 局限

1.  **提取覆盖有限带来的笔记盲区**：本笔记主体所依据的提取缓存仅含 p.1-8（摘要、引言、第 2 节"网页动态性"），关于架构（第 3 节）、爬取/检测/调度算法（第 4 节，含 X-Diff、Table 3-6）、通知（第 5 节）、可视化（第 6 节）、系统对比（第 7 节）、趋势与未来方向（第 8-9 节）的具体内容未在提取文本中，相关结论待核。
2.  **综述固有的深度限制**：对每个技术点（相似度公式、调度算法、树匹配算法等）多为概括性介绍，难以深入实现细节。
3.  **实证数据的时效性**：所汇总的网页动态性研究多为 2000-2012 年的历史爬取，互联网形态已演变，结论的现今适用性需谨慎对待。
4.  **系统评估偏定性**：在已提取部分看不到对商用/开源 CDN 系统的统一基准定量评测（该部分位于第 7 节，未覆盖）。

## 个人评论

> 以下为 AI 阅读时的评论，非论文原文观点。

1.  **一张清晰的领域地图**：本文把"网页变化检测"这一看似零散的领域解构为爬取/存储/检测/调度/通知/可视化等子问题，并配 Figure 1 的组织结构图，对初学者快速建立全局认知非常有用。
2.  **实证数据是调度设计的地基**：Table 1 汇总的"哪类网页变得快、变多少"的实证结论，直接支撑任何高效 CDN 调度/变化频率估计算法的设计——这是本文最具复用价值的部分。
3.  **问题导向、利于找创新点**：作者反复强调现有系统的不足（调度不够智能、缺乏统一评估），天然指向研究机会：自适应/学习型调度、变化"重要性/语义"评估、统一 benchmark。
4.  **跨域迁移的提示**：本文的"变化检测"是 Web/文档语境，与遥感影像变化检测（同名不同域）共享"版本比对+变化定位+变化可视化"的思想骨架，可作类比阅读，但勿混淆数据形态与方法。

### 使用建议

- **快速了解**：读**摘要**、**第 1 节引言**与 **1.1-1.2 节**，即可掌握 CDN 的定义、与搜索引擎的区别、服务端/客户端两类架构与核心监控选项。
- **复现/深入**：精读**第 3 节（架构）**与**第 4 节（变化检测技术、爬取与调度）**——这两节细节在本笔记提取范围之外，需回到原 PDF。
- **借鉴框架**：直接套用其 Figure 1 的问题分解结构来组织自己的相关工作综述。
- **写 Related Work**：可归入 "Web Change Detection / Web Monitoring Systems / Information Freshness" 类引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[S_变化检测_ChangeDetection]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇**综述（ACM Computing Surveys, 2019）**，方向为**网页变化检测与通知（Change Detection and Notification, CDN）**。它把"如何自动监控网页变化并在变化时通知用户"这一问题，系统拆解为网页动态性、系统架构、变化检测技术（爬取/检测/调度/变化频率估计）、通知、可视化、现有系统评估、趋势与未来方向等维度（Figure 1）。适合作为"网页/文档变化检测""网络监控""信息新鲜度"主题下的入门与框架性文献。注意：这是 **Web 网页**变化检测，与遥感影像变化检测属同名不同域。

## 2. 一句话总结
本文以 Figure 1 的结构系统综述了 CDN 系统的网页动态性、架构、检测技术、调度、通知与可视化，并汇总大规模网页动态性实证研究，为理解、评估与改进 CDN 系统提供统一框架。

## 3. 背景与问题
- **为什么要做**：Web 快速演进、网页持续动态变化（创建/更新/删除），用户希望被动获知关心网页的变化。RSS（源自 RDF）→2005 年被 Atom 取代→现多用浏览器书签，但这些传统方式都难以高效监控 (p.1-2)。
- **之前方法的问题**：
    1.  **RSS/Atom**：XML 规范字段利用率低 → 信息缺失/错误/未分类 feed；社交媒体兴起、XML→JSON、专有接口等因素致其衰落（Google Reader 停服）(p.2)。
    2.  **搜索引擎**：底层虽有变化检测，但服务于"维持索引新鲜度"，而非向用户直接通知；搜索引擎为搜索而生，CDN 为监控变化而生 (p.2)。
- **核心矛盾**：网页动态多样 vs. 用户需要便捷、高效、可定制的监控通知；已有 CDN 系统（Google Alerts、Follow That Page、Visualping 等）缺乏对其多方面特性的统一全面评估 (p.2-3)。

## 4. 核心贡献
1.  **综合性 CDN 综述框架**：弥补此前综述（Oita et al.、Shobhna & Chaudhary）覆盖面不足，按 Figure 1 系统覆盖动态性/架构/检测/通知/可视化/系统对比/趋势 (p.3-4)。
2.  **明确三大目标**：全面概览 CDN 特性、评估现有系统的特性与性能、考察新趋势并指出改进方向 (p.3)。
3.  **汇总网页动态性实证研究**：Table 1 归纳六项大规模长期爬取研究，量化"哪类网页变得快/慢" (p.7-8)。
4.  **梳理商用系统能力**：归纳 Wachete、VisualPing 的监控范围/内容/阈值/频率/通知频率等选项 (p.2)。

## 5. 方法详解
本文为综述，不提新方法，剖析 CDN 通用机制（提取文本覆盖 p.1-8；架构与检测算法细节在 p.9+，下文据原文目录标注）。
- **CDN 工作流**：爬取网页各版本 → 以带标签文档（非结构化）存入版本库 → 转为类 XML 元素树（元素 = HTML 开/闭标签）→ 用相似度计算比较旧/新版本 → 变化超用户阈值则通知 (p.2-3)。
- **网页与变化模型（Section 2.1）**：网页分**静态**（开发者保存后不变、对所有访客相同、加载快但需另加动态功能）与**动态**（由程序按请求即时生成、可按用户/上下文定制、用 CGI + PHP/ASP.NET/JSP，借 CMS 如 WordPress/Drupal 普及）。三类变化事件：**创建（Creations）**（新页需被已有页链接才公开，故创建至少触发一次"加链接"的更新）、**更新（Updates，分 minor/major）**、**删除（Deletions，含断链 broken link）** (p.5-6)。
- **两类架构**：服务端检测（服务器轮询+跟踪+通知）、客户端检测（客户端自行轮询跟踪）(p.2-3, 第 3 节)。
- **监控选项（Wachete/VisualPing）**：监控范围（部分/整页/多页/整站）、内容（文本/图片/链接/PDF·DOC·DOCX）、变化阈值（百分比）、监控频率（小时/天/周/月/按需）、通知频率（日两次/日一次/周一次/即时）(p.2)。
- **调度与变化频率估计**：固定计划易产生"空检查"；CDN 需估计每页变化频率以生成高效检查计划，提升资源利用率 (p.3)。
- **可视化通用做法**：新增文本绿色、删除文本红色（常带删除线）(p.3)。

## 6. 实验与结果
综述未做新实验，核心是 Section 2.2 + Table 1 对网页动态性的实证总结（提取文本 p.7-8 完整覆盖）：
- **Cho & Garcia-Molina (2000)**：720,000 网页 / 270 站，每天爬 4 个月；>20% 每访问即变、**40% 一周内变**，>50% 的 .com/.edu 全程未变 (p.7)。
- **Fetterly et al. (2003)**：约 1.5 亿网页 / 11 周；约 **65% 零变化**；.org/.gov 比 .edu 更稳定，spam 页变化更频繁 (p.7)。
- **Olston & Pandey**：Yahoo 集合 + Open Directory 各 10,000 URL；Open Directory 动态内容约 1/3 有 "scroll" 行为 (p.7)。
- **Adar et al. (2009)**：约 55,000 回访网页；34% 无变化，其余平均每 **123 小时**至少变一次；流行页（体育/新闻/个人）变最频繁，政府/教育页不频繁 (p.7)。
- **Elsas & Dumais (2010)**：约 200 万 HTML 页，每周爬 10 周；>62% 无实质差异；高相关文档更易变、变化幅度更大；提出按时间维度差异化加权的排序检索模型 (p.7)。
- **Saad & Gançarski (2012)**：FranceTV 档案 100 页，每小时爬、日获 3000+ 版本；根层显著变、最深层不变 (p.8)。
- **结论**：网页变化与站点类型/域名强相关——流行/新闻站更新快、政府/教育站变化少 (p.8)。
- **系统级定量对比**（准确率/召回率、跨系统 benchmark）在第 7 节等后续页 (据原文目录，提取缓存未覆盖, 待核)。

## 7. 这篇论文真正有价值的地方
1.  **一张可复用的领域地图**：Figure 1 的问题分解（动态性/架构/检测/调度/通知/可视化/评估）让零散主题成体系。
2.  **实证数据奠基调度设计**：Table 1 的"哪类网页变得快/慢"是设计变化频率估计与自适应调度的直接依据。
3.  **问题导向利于选题**：持续点名现有系统不足（调度不智能、缺统一评估），指向自适应调度、变化重要性评估、统一 benchmark 等创新方向。

## 8. 局限与问题
1.  **笔记提取盲区**：本笔记主体仅覆盖 p.1-8；架构（§3）、检测/爬取/调度算法（§4，含 X-Diff、Table 3-6）、通知（§5）、可视化（§6）、系统对比（§7）、趋势/未来（§8-9）未在提取文本中，相关内容待核。
2.  **综述深度有限**：对相似度公式、调度/树匹配算法多为概括介绍。
3.  **实证数据时效性**：所引研究多为 2000-2012 历史爬取，现今适用性需谨慎。
4.  **评估偏定性**：已提取部分未见统一基准定量评测。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要 + §1 引言 + §1.1-1.2（定义、与搜索引擎区别、服务端/客户端架构、监控选项）。
- **复现/深入**：精读 §3（架构）、§4（检测/爬取/调度）——细节在本笔记提取范围外，需回原 PDF。
- **借鉴框架**：套用 Figure 1 的问题分解结构组织自己的综述。
- **写 Related Work**：归入 Web Change Detection / Web Monitoring Systems / Information Freshness。

## 10. 和其他论文的关系
属"S_变化检测_ChangeDetection"主题下的 **Web 网页**变化检测综述（区别于遥感影像变化检测）。可关联：
- 具体网页/文档变化检测算法（哈希、DOM/XML 树匹配如 X-Diff，原文 Table 6）。
- 网页存档与时间快照、信息新鲜度研究。
- 网络爬虫调度与变化频率估计策略。
（注：提取资料有限，具体论文链接未定，故以主题双链标注。）

## 11. 关键词
变化检测, 网页通知 (CDN), 网页监控, 动态网页, 网络爬虫, 调度, 相似度计算, 变化频率估计, 变化可视化, 信息新鲜度, 综述

## 12. 可信度说明
本精读笔记的**主体依据是 PDF 提取缓存的 p.1-8**（摘要、引言 §1 含背景/问题/贡献/结构概述、第 2 节"网页动态性"全部，含 Table 1 六项实证研究），这部分提取质量良好、逻辑连贯、数字清晰可辨，相关声明可逐条对应原文。**论文 p.9 及以后**的架构细节（§3）、检测/爬取/调度算法（§4，含 X-Diff、Table 3-6）、通知（§5）、可视化（§6）、系统对比（§7）、趋势与未来方向（§8-9）**不在提取缓存中**，凡涉及这些章节之处均按"据原文目录/后续页，提取缓存未覆盖，待核"标注，未编造数字与结论。分类 `S_变化检测_ChangeDetection` 正确（变化检测主题，Web 子域）。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本 p.1-8 清晰, 约 2086 字符/页); 提取缓存覆盖 12/35 页且本次实读为前 8 页正文(p.9+ 截断); 来源缓存: `.paper-cache/extracts/2019_Change_Detection_and.txt`; 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。本轮优化重建了乱码摘要、订正实证数据、补充静态/动态网页与变化事件模型，并对所有提取未覆盖章节加注"待核"。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-35; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-35。
- **提取情况**: 缺失页 23 页, 其中 23 页提取到可读文本。缺失页包含正文/附录内容, 其中约 6 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。
- **与上方笔记的关系**: 本次优化所用的提取缓存仅含 p.1-8 正文; 下列 p.13+ 线索来自补读记录, 未并入上方各节的事实性结论, 仅作章节索引, 内容待核。

### 缺失页章节线索

- p.13: Change Detection and Notification of Web Pages: A Survey 15:13
- p.13: Crawling
- p.13: TechniqueCrawling
- p.13: PatternPrioritize
- p.13: General
- p.13: Focused
- p.13: Distributed
- p.13: Another aspect that has drawn the attention of researchers is the efficient partitioning mecha-
- p.14: Efficient crawling of Rich Internet Applications (RIA) is an open problem as RIAs consist of
- p.14: Crawler Distributed Advantage Disadvantage
- p.14: Dist-RIA crawler
- p.14: Applications in parallelLack of adaptive load-

### 缺失页关键摘录

- p.13: Figure 7 denotes the general arrangement of components in a distributed crawling system. The
- p.13: the Web grows. Table 3 summarizes the three main crawling techniques with their advantages,
- p.13: Table 3. A summary of the main crawling techniques.
- p.14: Table 4. A summary of various crawling solutions presented in the literature.
- p.15: in processing times over doing I/O operations and processing in a central processing unit. Table 4
- p.15: Table 5. A summary of various scheduling solutions.
- p.16: where computational resources are used inefficiently. Table 5 compares the various scheduling
- p.16: the different changes occurring on webpages. Elaborated in Table 6 are a few popular algorithms
- p.17: algorithm. The authors have tested the X-Diff algorithm for its accuracy and efficiency of change
- p.18: order between nodes is crucial, and this order directly contributes to the result of change detection;
- p.18: nodes, and the tree is constructed for the webpage as illustrated in Figure 8, while maintaining
- p.19: Table 6. A summary of existing change detection algorithms.
<!-- AI_READING_NOTE_END -->
