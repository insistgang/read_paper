---
title: Predicting Illegal Fishing on the Patagonia Shelf from Oceanographic Seascapes
authors:
  - "A. John Woodill"
  - "Maria Kavanaugh"
  - "Michael Harte"
  - "James R. Watson"
year: 2020
venue: "arXiv"
doi: 
pdf: [[2020_Predicting_Illegal_F.pdf]]
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
extract_cache: .paper-cache/extracts/2020_Predicting_Illegal_F.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/27 pages"
---
# Predicting Illegal Fishing on the Patagonia Shelf from Oceanographic Seascapes

## 基本信息
- **PDF**: [[2020_Predicting_Illegal_F.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Predicting Illegal Fishing on the Patagonia Shelf from Oceanographic Seascapes |
| **作者** | A. John Woodill; Maria Kavanaugh; Michael Harte; James R. Watson |
| **发表时间** | 2020 (arXiv:2007.05470v1, cs.LG, 2020-07-10) |
| **刊物/会议** | arXiv (preprint) |
| **DOI** | 未明确 (arXiv:2007.05470) |

## 摘要

> **英文原文 (据 PDF 提取文本整理)**：Many of the world's most important fisheries are experiencing increases in illegal fishing, undermining efforts to sustainably conserve and manage fish stocks. A major challenge to ending illegal, unreported, and unregulated (IUU) fishing is improving our ability to identify whether a vessel is fishing illegally and where illegal fishing is likely to occur in the ocean. However, monitoring the oceans is costly, time-consuming, and logistically challenging for maritime authorities to patrol. To address this problem, we use vessel tracking data and machine learning to predict illegal fishing on the Patagonian Shelf, one of the world's most productive regions for fisheries. Specifically, we focus on Chinese fishing vessels, which have consistently fished illegally in this region. We combine vessel location data with oceanographic seascapes – classes of oceanic areas based on oceanographic variables – as well as other remotely sensed oceanographic variables to train a series of machine learning models of varying levels of complexity. These models are able to predict whether a Chinese vessel is operating illegally with 69-96% confidence, depending on the year and predictor variables used. These results offer a promising step towards preempting illegal activities, rather than reacting to them forensically.

> **中文翻译**：全球许多重要渔场的非法捕鱼正在增加，破坏了可持续养护与管理鱼类种群的努力。终结非法、不报告、不管制（IUU）捕鱼的一大挑战，是提升我们识别"某船只是否在非法捕鱼"以及"海洋中何处可能发生非法捕鱼"的能力。然而，海洋监测成本高、耗时长，且海事执法部门在巡逻上面临巨大的后勤困难。为解决这一问题，本文利用船舶追踪数据和机器学习来预测巴塔哥尼亚大陆架（全球最高产渔区之一）上的非法捕鱼。我们特别聚焦于在该区域长期非法捕鱼的中国渔船。我们将船舶位置数据与"海洋景观（seascapes）"——基于海洋学变量对海域进行分类的方法——以及其他遥感海洋学变量相结合，训练了一系列复杂程度不一的机器学习模型。这些模型能够以 69%–96% 的置信度预测某艘中国渔船是否在非法作业，具体取决于年份和所用的预测变量。这些结果朝着"事先预防而非事后取证式应对"非法活动迈出了有希望的一步。

> **关键词**：geospatial intelligence; illegal, unreported, and unregulated fishing; IUU; machine learning; prediction; seascapes; sustainable fisheries.

> **来源**：据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：非法捕鱼损害海洋健康，是实现海洋可持续利用的长期挑战。近期估计显示非法捕鱼可达全球渔获量的 20%，每年价值约 364 亿美元（$36.4 billion，p.2）。它通过削弱官方渔获和资源量估计的准确性，使总捕捞努力量超过最大可持续水平，进而造成鱼类种群负增长，并削弱对海洋保护区的监测能力（p.2）。
- **案例区域**：巴塔哥尼亚大陆架位于阿根廷外海，是全球最高产的渔区之一，盛产阿根廷滑柔鱼（每年捕获量可达约 100 万吨）以及无须鳕、长尾鳕、岩鳕、南方蓝鳕等鱼类（p.2-3）。但该区过度捕捞严重：UNFAO 2015 年报告指出，西南大西洋 42% 的资源处于不可持续水平，在 15 个主要统计区中排名倒数第三（p.3）。前阿根廷渔业副国务卿 Cesar Lerena 称该国每年损失高达约 50 亿美元和数千个就业岗位（p.3）。
- **空间博弈结构**：最高产的渔区之一恰好紧邻 EEZ 边界，渔船可以选择在 EEZ 外合法作业，也可越界进入阿根廷 EEZ 非法捕鱼且多半不被发现。中国渔船利用这一空间特征，常在 EEZ 边界附近大量聚集以捕捞滑柔鱼（p.3-4）。中国拥有全球最大的远洋渔船队，且无权在阿根廷 EEZ 内捕鱼（p.3-4）。
- **之前方法的问题**：传统监测（巡逻）成本高、耗时、后勤困难；船只还会关闭 GPS 应答器或伪造位置（"spoofing"），构成全球"暗船队"（dark fleet）。已有研究多聚焦于通过 AIS 数据检测 spoofing 来"检测"非法船只（Ford 2018、Miller 2018、Petrossian 2018），但检测只能提供过去事件的信息（p.2）。Watson and Woodill (2019) 通过识别船队对邻近非法活动的异常空间响应来"预测"，能给出早期预警信号，但其前兆指标无法判定某艘具体船只是合法还是非法（p.2）。
- **核心矛盾 / 本文目标**：能否仅基于某位置的海洋条件，近实时地预测某艘渔船当前是否在非法作业，从而把"事后取证"升级为"事前预防"，并具备"针对单艘船只"的判别能力（p.2）。

## 关键贡献

1.  **将"海洋景观（Seascapes）"引入非法捕鱼预测特征**：海洋景观是 Kavanaugh 等提出的、按生物/化学/地质/物理过程将海域聚类为不同类别的方法，能在保留底层数据分布（即使非线性）的前提下概括海洋条件的多维变异性。本文用它与 SST、CHL 一起作为预测变量（p.4-5）。
2.  **构建随机森林二分类器预测单船合法性**：以"操作合法（y=0）/非法（y=1）"为二分类目标，输入海洋学变量、地理变量与月份哑变量，能针对单艘船只判别其是否非法、以及非法活动可能发生的时间和地点（p.5-6）。
3.  **用按年份的块状交叉验证抑制时空自相关导致的过度乐观**：以单一年份为测试集、其余四年为训练集，做五折验证，确保训练/测试集时空结构独立，避免因空间自相关而高估模型性能（p.6）。
4.  **变量重要性筛选 + 精简模型反超"全变量"模型**：随机森林给出最重要的 5 个变量——经度、纬度、SST、CHL、是否在 EEZ 内（I-EEZ）；仅用这 5 个变量的精简模型 F-1 反而略优于"kitchen sink"全变量模型（p.7-8）。
5.  **从模型可解释性导出行为洞察**：最强的海洋景观预测因子是 Seascape 14 "Temperate Bloom Upwelling（温带藻华上升流）"；当该上升流景观（可用渔场）收缩时，更多渔船倾向进入 EEZ 非法作业，揭示了船只随海洋条件变化调整风险偏好的机制（p.8-9）。

## 方法

- **整体框架**：数据准备（AIS + 遥感海洋学变量，最近邻匹配）→ 随机森林分类与块状交叉验证 → 变量重要性筛选 + 精简/纯海洋模型 → 行为与空间分布解读。
- **非法/合法的标签定义（p.4-5）**：将"非法作业船只"定义为同时满足三条件——(1) 中国籍渔船（按 flag 判定）、(2) 位于阿根廷 EEZ 内、(3) 捕鱼努力量为正（GFW 数据中非零捕鱼小时数）。作者承认该定义偏严格（无法获知具体哪艘中国船持有合法许可证），但据其判断持证比例极小（若有），故是保守的。
- **输入变量（Table 2，p.4-5）**：
    - 海洋学：海表温度 SST、叶绿素 CHL、海洋景观分类 SEA；
    - 地理：纬度 LAT、经度 LON、是否在 EEZ 内 I-EEZ；
    - 时间：月份（哑变量，因区域捕鱼有季节性——多数非法捕鱼发生在 2 月和 3 月，p.4）。
- **数据匹配**：对每个船舶位置点，用最近邻插值匹配 SST、CHL、SEA（p.4-5）。因云层覆盖，部分海面位置无观测，记为 "not available"（p.5）。
- **建模思路（p.5-6）**：核心假设是"船只在海洋条件有利于捕鱼之处作业"，当条件变化激励它向不允许作业的区域（EEZ 内）移动时，越界可获益但承担被执法抓获的风险。建模思路类似物种分布模型（将捕鱼努力量与环境变量关联），但本文转为二分类器以直接判别单船是否非法。
- **随机森林为何适用**：通过对数据 bagging 到不同子集、跨树降低相关性，从而降低方差、提升预测；天然处理多重共线性与非线性；并能输出变量重要性。这种"kitchen sink"思路既提供预测工具，又增进对非法捕鱼驱动因素的理解（p.6）。
- **三档模型规格（p.7）**：
    1. 全变量"kitchen sink"模型（所有预测变量）；
    2. 精简模型：仅 Top-5 重要变量（SST, CHL, I-EEZ, LAT, LON）；
    3. 纯海洋模型：仅 SST, CHL, SEA + 月份，模拟只有实时遥感数据、缺船位数据的场景。
- **训练与验证（p.6）**：块状交叉验证（block cross-validation），单年为测试集、其余四年训练，五折；目的是防止空间自相关导致的过拟合与过度自信。
- **与已有方法的差异**：区别于仅检测 spoofing 或识别船队异常空间行为的方法，本方法聚焦"单艘船只合法性"判别，并以"位置 + 海洋条件"作为预测依据，从而具备针对个体的预警能力（p.2, 5-6）。

> 说明：这是一篇基于表格特征（AIS 轨迹 + 遥感海洋学变量）的机器学习行为预测论文，不涉及图像目标检测、检测框或卷积网络。

## 实验

- **数据集（p.4）**：
    - **船舶数据**：来自 Global Fish Watch (GFW) 的网格化 AIS 数据，覆盖 2012–2016 年巴塔哥尼亚大陆架，空间分辨率为 1/10 度；提供每日渔船位置、捕鱼努力量（小时）及唯一 AIS 标识（MMSI），并含 flag（国籍）与 gear type（渔具）等船只特征。子集共 **114,103 个观测点**，其中合法作业的唯一船只 **781 艘**、非法作业的唯一船只 **186 艘**。非法样本仅占总观测的 **1.5%**（类别极度不平衡）。非法中国船只中滑柔鱼钓船占 81%、拖网船占 15%（p.4）。
    - **海洋数据**：SST、CHL 来自 NASA Ocean Color，SEA（海洋景观）来自 NOAA ERDDAP，均为 8 天合成（8-day increments）。因云层覆盖部分缺失（p.5）。
- **评价指标（p.6-7）**：针对类别不平衡，关注对非法类（y=1）的预测。共 5 项指标：(1) Precision 与 Recall；(2) F-Score；(3) AUC；(4) Average Precision (AP)；(5) Average Recall (AR)。以 **F-1 分数为主指标**（不平衡分类的精度-召回调和平均，越接近 100% 越准）。
- **主结果（p.7-8）**：
    - **全变量模型**：F-1 在 **69–89%**（随年份不同）；AP 0.79–0.96，AR 0.69–0.99，AUC 0.79–0.96（详细指标见 Table S1）。
    - **精简模型（Top-5 变量）**：F-1 **69–96%**，AP 0.75–0.99，AR 0.76–0.97，AUC 0.75–0.99；略优于全变量模型（"反直觉地"更准）。
    - **纯海洋模型（SST, CHL, SEA + 月份）**：F-1 **71–89%**，AP 0.67–0.85，AR 0.79–0.97，AUC 0.71–0.88；虽不及前两者，但可在无船位数据时提示"何时海洋条件适于非法捕鱼"。
- **变量重要性（Figure 4，p.7-8）**：Top-5 = 经度、纬度、SST、CHL、I-EEZ（重要性已缩放到 1）。
- **行为分析（p.8-9）**：最强海洋景观预测因子是 Seascape 14 "Temperate Bloom Upwelling"。追踪船只从合法转非法的当日景观变化：共 **83 艘**中国渔船在观察到有利条件后进入 EEZ 开始非法作业；次重要为 "Temperate Transition" 景观（**80 艘**转入，该带温度 11–15°C、盐度 >34 psu、低中营养 chl-a 0.2–0.5 mg/m³）。空间对比（Figure 6）显示：高非法活动日（n=76）温带藻华上升流景观覆盖面积小于低非法活动日（n=3），暗示上升流/藻华景观收缩→可用渔场受限→船只更可能越界进入 EEZ。
- **消融 / 泛化**：通过精简模型与纯海洋模型构成变量消融；块状交叉验证在样本外年份上的表现说明了跨年份泛化能力。
- **效率信息**：PDF 文本未明确说明随机森林的树数量、训练时间、参数量等计算效率信息。

## 局限

- **数据依赖与"暗船队"盲区**：方法依赖 AIS。但非法船常 spoofing 或关闭应答器，构成完全缺失数据的"暗船队"，模型可能恰恰难以覆盖最顽固的非法活动（p.2）。
- **"非法"定义偏严**：将"所有中国船只在阿根廷 EEZ 内作业"一律视为非法。作者承认无法获知哪些船持有许可证，但据判断持证比例极小，故称此假设虽严格却保守（p.5）。
- **时空分辨率聚合**：AIS 为 1/10 度网格，海洋数据为 8 天合成，且云层导致缺失（记为 not available）。这种聚合可能掩盖更精细尺度的船只行为与环境变化。
- **泛化范围**：聚焦中国渔船 + 巴塔哥尼亚大陆架 + 进入 EEZ 这一类非法行为。能否推广到其他国籍、其他渔场或其他非法类型（如禁用渔具）需进一步验证。
- **实时部署挑战**：纯海洋模型为实时应用提供思路，但精度低于含船位的模型；实际部署中如何高效、实时获取并融合多源数据是工程挑战（作者称构建精简/纯海洋模型正是为可操作化的实时数据流做准备，p.7）。
- **证据性质**：部分行为结论（如 Figure 6 的上升流收缩→越界）是定性/相关性证据，并非因果证明（p.9）。

## 个人评论

1.  **把执法预测问题干净地表述为不平衡二分类**：标签由"国籍 + EEZ 内 + 正捕鱼努力量"三条件硬编码，简单透明、可复现；"数据定义—特征工程—建模—评估—解释"的完整链条对其他异常行为预测任务有借鉴价值。
2.  **领域知识特征化（Seascapes）值得学习**：把高维、非结构化的海洋状态压缩为有意义的离散景观类别，再证明其对下游预测有效，比直接堆原始变量更贴合领域知识，也更利于行为解读。
3.  **可解释性反哺机理发现**："kitchen sink → 变量重要性 → 精简模型"不只为提分，更用于回答"什么在驱动非法行为"；并由 Seascape 14 收缩引出"风险权衡"行为假说，体现了"模型驱动发现"的范式。
4.  **评估方法的严谨性**：按年份块状交叉验证显式对抗时空自相关，是空间数据建模中容易被忽视、却很值得效仿的实践。
5.  **可改进之处**：分类阈值、随机森林超参（树数、深度）、以及"暗船队"缺失数据的偏差校正在本文文本中均未充分展开；F-1 区间较宽（如全变量 69–89%）也提示年际稳定性仍有提升空间。

### 使用建议

- **如果快速了解**：读 Abstract、Introduction 首末段、以及 Results（第 3 节）即可把握动机、方法与主要结论。
- **如果复现**：重点读 2. Materials and Methods 的 Data 与 Predicting Illegal Fishing 小节，明确数据来源（GFW 公开 AIS + NASA Ocean Color + NOAA ERDDAP）、最近邻匹配、三条件标签定义、随机森林与块状交叉验证；指标以 F-1 为主，辅以 AP/AR/AUC。
- **如果借鉴创新点**：(1) 领域知识→ML 特征（Seascapes）；(2) 变量重要性反推驱动因素并构建精简模型；(3) 针对时空数据 + 类别不平衡的评估（块状交叉验证、F-1）。
- **如果写 Related Work**：可归入——IUU 捕鱼监测与预测、船舶 AIS 轨迹分析、遥感海洋环境应用、机器学习在生态/环境监测中的应用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇**地理空间情报 / 机器学习应用于海洋资源执法**的论文（arXiv:2007.05470, cs.LG），主题是"从海洋学条件预测 IUU（非法、不报告、不管制）捕鱼"。它**不属于计算机视觉目标检测**：没有图像、检测框或卷积网络，而是用 AIS 船舶轨迹 + 遥感海洋学变量（SST/CHL/海洋景观）构成的表格特征，训练随机森林二分类器判别单艘中国渔船在阿根廷 EEZ 内是否非法作业。因此本笔记将主题由原先的"C2_目标检测_违建_车辆_船舶_行人"修正为 `T_通用_NLP_其他`。

## 2. 一句话总结
本文将船舶 AIS 轨迹与海洋环境数据（尤其是"海洋景观"分类）融合为随机森林二分类特征，预测中国渔船在阿根廷 EEZ 内的非法捕鱼，F-1 准确率随年份与变量组合在 69%–96% 之间，并借模型可解释性揭示船只随上升流景观收缩而越界的风险权衡行为。

## 3. 背景与问题
- **为什么要做**：非法捕鱼可达全球渔获量约 20%、每年约 364 亿美元（p.2），削弱资源量估计、推高总捕捞努力量、危害海洋保护区。巴塔哥尼亚大陆架高产却过度捕捞（西南大西洋 42% 资源不可持续，p.3），阿根廷每年因非法捕鱼损失约 50 亿美元（p.3）。最高产渔区紧邻 EEZ 边界，中国渔船常在边界聚集、择机越界（p.3-4）。
- **之前方法的问题**：传统巡逻成本高；非法船 spoofing 形成"暗船队"。已有研究多检测 spoofing（事后），Watson & Woodill (2019) 能预测但无法判定单艘船的合法性（p.2）。
- **核心矛盾**：能否仅凭某位置的海洋条件，近实时、针对单船地预测其是否非法，把"事后取证"变为"事前预防"（p.2）。

## 4. 核心贡献
1.  引入"海洋景观（Seascapes）"作为预测特征，概括海洋条件的多维变异（p.4-5）。
2.  构建随机森林二分类器，以"国籍 + EEZ 内 + 正捕鱼努力量"三条件定义非法标签，针对单船预测（p.5-6）。
3.  用按年份块状交叉验证抑制空间自相关导致的过度乐观评估（p.6）。
4.  变量重要性给出 Top-5（LON, LAT, SST, CHL, I-EEZ），精简模型反超全变量模型（p.7-8）。
5.  由 Seascape 14（温带藻华上升流）收缩 → 越界增多，导出风险权衡行为洞察（p.8-9）。

## 5. 方法详解
- **数据匹配**：对每个 AIS 位置点用最近邻插值匹配 SST、CHL、SEA（8 天合成；云层缺失记为 not available）（p.4-5）。
- **标签**：y=1 当且仅当（中国籍 ∧ EEZ 内 ∧ 捕鱼努力量>0），否则 y=0；作者承认严格但保守（无法获知许可证，持证比例极小）（p.5）。
- **特征**：SST, CHL, SEA, LAT, LON, I-EEZ, 月份哑变量（季节性，多数非法发生在 2、3 月）（p.4-5）。
- **模型**：随机森林——bagging + 跨树降相关以降方差，处理多重共线性/非线性，输出变量重要性；"kitchen sink"既预测又解释（p.6）。
- **三档规格**：全变量 / Top-5 精简 / 纯海洋（SST,CHL,SEA+月份，模拟无船位的实时场景）（p.7）。
- **验证**：块状交叉验证，单年测试、其余四年训练，五折，对抗空间自相关（p.6）。
- **与已有方法差异**：聚焦单船合法性判别，以位置+海洋条件为依据，具个体级预警能力（p.2, 5-6）。

## 6. 实验与结果
- **数据集**：GFW 网格化 AIS（2012–2016，1/10 度），114,103 观测点，合法船 781 艘、非法船 186 艘，非法样本占 1.5%；非法中国船 81% 为滑柔鱼钓船、15% 为拖网船（p.4）。海洋数据来自 NASA Ocean Color（SST/CHL）与 NOAA ERDDAP（SEA），8 天合成（p.5）。
- **指标**：Precision/Recall、F-Score、AUC、AP、AR；以 **F-1 为主**（不平衡分类）（p.6-7）。
- **结果**：
    - 全变量：F-1 **69–89%**；AP 0.79–0.96，AR 0.69–0.99，AUC 0.79–0.96（p.7-8）。
    - 精简（Top-5）：F-1 **69–96%**；AP 0.75–0.99，AR 0.76–0.97，AUC 0.75–0.99；略优于全变量（p.8）。
    - 纯海洋：F-1 **71–89%**；AP 0.67–0.85，AR 0.79–0.97，AUC 0.71–0.88（p.8-9）。
- **变量重要性**：LON, LAT, SST, CHL, I-EEZ（Figure 4，p.7-8）。
- **行为分析**：83 艘船在 Seascape 14 有利条件下越界；80 艘转入 Temperate Transition（11–15°C, >34 psu, chl-a 0.2–0.5 mg/m³）；高非法日上升流景观覆盖面积小于低非法日（Figure 6），暗示渔场收缩驱动越界（p.8-9）。
- **效率**：PDF 文本未明确树数量、训练时间、参数量等。

## 7. 这篇论文真正有价值的地方
1.  把执法预测干净地建模为不平衡二分类，标签可复现、链条完整。
2.  领域知识特征化（Seascapes）：高维海洋状态 → 离散景观类别 → 有效预测特征。
3.  可解释性反哺机理：变量重要性 + Seascape 行为假说 → "模型驱动发现"。
4.  块状交叉验证显式对抗时空自相关，评估更贴近真实部署。

## 8. 局限与问题
- 依赖 AIS，无法覆盖 spoofing 的"暗船队"（p.2）。
- "非法"定义偏严（所有中国船在 EEZ 内即视为非法），作者称保守（p.5）。
- 时空聚合（1/10 度、8 天合成、云层缺失）掩盖精细行为（p.4-5）。
- 泛化范围限于中国船 + 巴塔哥尼亚 + 越界一类行为（p.9）。
- 纯海洋模型精度较低，实时多源数据融合是工程挑战（p.7）。
- Figure 6 的上升流收缩→越界为定性/相关性证据，非因果（p.9）。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Introduction 首末段 + Results。
- **复现**：读 Methods 的 Data 与 Predicting Illegal Fishing（GFW 公开 AIS + NASA/NOAA 遥感；三条件标签；随机森林；块状交叉验证；F-1 主指标）。
- **借鉴创新点**：领域知识→ML 特征（Seascapes）；变量重要性反推驱动因素；时空数据+不平衡的评估方法。
- **写 Related Work**：IUU 捕鱼监测与预测 / 船舶 AIS 轨迹分析 / 遥感海洋环境应用 / ML 在生态环境监测中的应用。

## 10. 和其他论文的关系
本文是**地理空间情报 + 机器学习**在海洋执法上的应用（非 CV 目标检测），现归入 `T_通用_NLP_其他`。相关方向：
- 基于 AIS 的船舶行为分析（港口交通、异常轨迹检测）。
- 物种分布建模（本文方法论上由其改造而来，p.5-6）。
- 其他非法活动（IUU、走私）的预测研究，以及作者团队前作 Watson & Woodill (2019)。
（库内暂无对应笔记，无法建立具体 `[[双链]]`。）

## 11. 关键词
非法捕鱼, IUU, 随机森林, 海洋景观 (Seascapes), AIS 轨迹, 单船合法性预测, 巴塔哥尼亚大陆架, 阿根廷 EEZ, 块状交叉验证, F-1 分数, 类别不平衡, 变量重要性, 温带藻华上升流, 地理空间情报

## 12. 可信度说明
本精读笔记基于 PDF 提取文本（覆盖前 12 页正文，含 Abstract→Discussion 开头，约 25000 字符），所有数字（114,103 观测、781/186 艘、1.5%、69–96% F-1、AP/AR/AUC 区间、83/80 艘转移、364 亿美元等）均直接来自该文本并标注页码。提取文本未呈现完整 Discussion 末段、Acknowledgements、Data Availability、References 及附录表/图（p.13-27，见全文补读记录）。文本未明确的内容（如随机森林超参、训练时间、参数量）已标"PDF 文本未明确"。分类已由原 C2（CV 目标检测）修正为 T_通用_NLP_其他。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2020_Predicting_Illegal_F.txt` (27/27 页; 原 AI 主体 12/27 + 全文补读 13-27); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro); 本轮深读已对照前 12 页提取文本重核全部数值并修正主题分类。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-27; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-27。
- **提取情况**: 缺失页 15 页, 其中 15 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 6 ACKNOWLEDGEMENTS
- p.13: 7 DATA AVAILABILITY
- p.14: References
- p.15: Aloha from the edge: Reconciling three decades of in situ eulerian observations and geographic
- p.15: Hierarchicalanddynamicseascapes: Aquantitativeframeworkforscalingpelagicbiogeochemistry
- p.18: Class Name Description
- p.18: 1 North Atlantic Spring,
- p.18: ACC TransitionCold (4-7 C), low dynamic topography,
- p.18: 2 Subpolar-Subtropical
- p.18: TransitionVariable SST (12-21C), Oligotrophic to
- p.18: 7 Temperate Transition Temperatures ranging from 11-15 C,
- p.18: 12 Subpolar Cool (6-9 C), mesotrophic, low CDOM

### 缺失页关键摘录

- p.13: a Chinese ﬁshing vessel is operating illegally with 69-96% accuracy in the Patagonian Shelf region
- p.18: Table 1: Summary of Patagonian Shelf Seascapes
- p.18: Table provides a list of the most prevalent seascapes in the Patagonian Shelf region.
- p.19: Table 2: Summary of Random Forest Variables
- p.19: Table provides a list of variables, abbreviations, a brief description and the source of the data used in
- p.20: Table provides results from our analysis across diﬀerent model speciﬁcations shown in column: (1)
- p.20: sensitivity analysis of vessels distance to EEZ being inside 2km, 5km, and 10km. Table provides
- p.20: an F-1 Score to evaluate model performance for each predicted year 2012-2016. See Table S1 for
- p.21: The table provides results from our analysis across diﬀerent model speciﬁcations shown in column: (1) using
- p.21: analysis of vessels distance to EEZ being inside 2km, 5km, and 10km. The table provides Average-Precision,
- p.21: Average-Recall, and Area-Under-Curve accuracy metrics to evaluate model performance for each predicted
- p.22: Figure 1: Map of Patagonian Shelf with Seascapes and Illegal/Legal Fishing Vessels
<!-- AI_READING_NOTE_END -->
