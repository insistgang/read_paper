---
title: A comprehensive survey on deep active learning in medical image analysis
authors:
  - "Haoran Wang"
  - "Qiuye Jin"
  - "Shiman Li"
  - "Siyu Liu"
  - "Manning Wang"
  - "Zhijian Song"
year: 2024
venue: "Medical Image Analysis 95 (2024) 103201"
doi: 10.1016/j.media.2024.103201
pdf: [[A-comprehensive-survey-on-deep-active-learning-in-medi_2024_Medical-Image-An.pdf]]
primary_topic: A1b_医学图像_小样本_综述
topics:
  - "A1b_医学图像_小样本_综述"
  - "R_综述_Survey"
  - "Q_自监督_对比学习_主动学习"
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
extract_cache: .paper-cache/extracts/A-comprehensive-survey-on-deep-active-learning-in-medi_2024_Medical-Image-An.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/34 pages"
---
# A comprehensive survey on deep active learning in medical image analysis

## 基本信息
- **PDF**: [[A-comprehensive-survey-on-deep-active-learning-in-medi_2024_Medical-Image-An.pdf]]
- **primary_topic**: `A1b_医学图像_小样本_综述`
- **topics**: `A1b_医学图像_小样本_综述`, `R_综述_Survey`, `Q_自监督_对比学习_主动学习`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A comprehensive survey on deep active learning in medical image analysis |
| **作者** | Haoran Wang; Qiuye Jin; Shiman Li; Siyu Liu; Manning Wang; Zhijian Song |
| **发表时间** | 2024 (Available online 13 May 2024) |
| **刊物/会议** | Medical Image Analysis 95 (2024) 103201 (Elsevier) |
| **DOI** | 10.1016/j.media.2024.103201 |
| **单位** | 复旦大学基础医学院数字医学研究中心 / 上海市医学图像处理与计算机辅助介入重点实验室; KAUST CBRC |
| **代码与论文列表** | https://github.com/LightersWang/Awesome-Active-Learning-for-Medical-Image-Analysis |

## 摘要

**英文原文（据 PDF 提取文本整理，已修复断词与空格）**：

> Deep learning has achieved widespread success in medical image analysis, leading to an increasing demand for large-scale expert-annotated medical image datasets. Yet, the high cost of annotating medical images severely hampers the development of deep learning in this field. To reduce annotation costs, active learning aims to select the most informative samples for annotation and train high-performance models with as few labeled samples as possible. In this survey, we review the core methods of active learning, including the evaluation of informativeness and sampling strategy. For the first time, we provide a detailed summary of the integration of active learning with other label-efficient techniques, such as semi-supervised, self-supervised learning, and so on. We also summarize active learning works that are specifically tailored to medical image analysis. Additionally, we conduct a thorough comparative analysis of the performance of different AL methods in medical image analysis with experiments. In the end, we offer our perspectives on the future trends and challenges of active learning and its applications in medical image analysis. An accompanying paper list and code for the comparative analysis is available at https://github.com/LightersWang/Awesome-Active-Learning-for-Medical-Image-Analysis.

**中文翻译**：

> 深度学习在医学图像分析中取得了广泛成功，由此带来了对大规模专家标注医学影像数据集的不断增长的需求。然而，医学图像标注的高昂成本严重制约了深度学习在该领域的发展。为降低标注成本，主动学习旨在挑选信息量最大的样本进行标注，并用尽可能少的有标签样本训练出高性能模型。本综述系统回顾了主动学习的核心方法，包括信息性评估与采样策略。我们首次详细总结了主动学习与其他标签高效技术（如半监督学习、自监督学习等）的结合。我们还梳理了专门针对医学图像分析定制的主动学习工作。此外，我们通过实验对不同主动学习方法在医学图像分析中的性能进行了全面的对比分析。最后，我们对主动学习及其在医学图像分析中应用的未来趋势与挑战给出了我们的看法。配套的论文列表与对比实验代码已开源于上述 GitHub 仓库。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：深度学习在医学影像分析中已逼近临床专家水平（文中举例：皮肤癌分类 Esteva 2017、CT 肺癌筛查 Ardila 2019、结肠镜息肉检测 Wang 2018、全切片图像前列腺癌检测 Tolkach 2020），但深度模型的成功高度依赖大规模人工标注数据。医学图像数据集虽在扩张（如脑肿瘤分割数据集 BraTS 从 2013 年的 65 名患者扩到 2021 年的 1200+ 名，后者等价于 70 万+ 张标注 2D 图像；脚注：BraTS 2021 含 1251 名患者，每例 4 个 MRI 序列、每序列 155 张轴位切片，共 1251×4×155=775,620 张切片），但仍远小于自然图像数据集（如 ImageNet 千万级）。瓶颈在于**标注成本极高**，文中归纳为两方面：
  1. **精细标注耗时费力**：分割模型需像素级标注，极其繁琐；数字病理学中病理学家需在高倍显微镜下反复调焦检查组织切片，检视单张切片通常需 15–30 分钟（Qu 2022）。
  2. **标注门槛高导致成本高**：CV 中众包平台可低成本获取检测/分割标注，但医学图像标注需要医学知识与临床专长，复杂病例甚至需多名资深专家会诊；众包工人质量低于专业标注者（Rädsch 2023），且涉及隐私问题。改用临床医生标注则更贵——放射科医生为单个患者多序列 MRI 手动分割脑肿瘤约需 60 分钟（Menze 2014），美国放射科医生时薪中位数约 \$221；为降低个体偏倚，常需同一病例多次/多人标注，引入标注者内/间差异，进一步抬高成本。
- **之前方法的问题**：已有 AL 综述（Settles 2009 机器学习时代综述；Ren 2021 综述深度 AL 在 CV/NLP；Liu 2022 总结模型驱动/数据驱动样本选择器；Zhan 2022 公平复现高影响力深度 AL 工作；Takezoe 2023 综述 CV 与工业应用；以及医学侧 Budd 2021、Tajbakhsh 2020、Jin 2023a）存在四点局限：1) 深度 AL 发展迅速，需更全面覆盖最新进展；2) "AL + 其他标签高效技术"的结合是新趋势却缺乏系统总结；3) 极少有综述在医学影像数据集上系统评估不同 AL 方法的性能；4) 高标注成本凸显 AL 在医学影像中的重要性，但相关综述在这一领域仍不够全面。
- **作者想解决的核心矛盾**：**有限标注预算与训练高性能深度模型所需大量标注数据之间的矛盾**。主动学习智能挑选信息量最大的样本送标注，从而以尽量少的标注成本逼近全监督性能。

## 关键贡献

文中明确列出四点贡献（Section 1 末尾）：

1. **全面综述与新颖分类法**：通过详尽文献检索（在 Google Scholar 与 arXiv 上以 "Active Learning" 检索并沿引用扩展），为 AL（尤其面向医学图像分析者）提供全面综述与新分类框架。文中统计本综述涉及近 **164 篇相关 AL 工作、234 篇参考文献**，多发表于 TPAMI、MedIA、TMI、TBME、JBHI 等顶刊与 MICCAI、ISBI、MIDL、CVPR、ICCV、ECCV、ICML、ICLR、NeurIPS 等顶会。
2. **系统总结采样策略**：以往综述主要关注"信息性评估"，本文进一步总结深度 AL 中的不同**采样策略**（如多样性、类别平衡策略），为未来方法改进提供参考。
3. **首次详细综述技术融合**：本文是**第一篇**详细综述 AL 与其他标签高效技术融合的工作，涵盖**半监督学习、自监督学习、基于区域的主动学习、生成模型、域自适应**。
4. **公开对比实验分析**：为促进研究并回馈社区，本文在多个医学影像数据集上评估了若干主流 AL 方法的性能，并公开代码以增强可复现性。

## 方法

本文是综述，其"方法"即对现有 AL 方法的**系统梳理、分类与阐述框架**（总体框架见 Fig. 2）。组织结构（提取文本 Section 1 末尾明确给出）：第 2 节问题设定与数学公式化 → 第 3 节核心方法（信息性评估 3.1/3.2 + 采样策略 3.3）→ 第 4 节 AL 与其他标签高效技术的融合 → 第 5 节面向医学影像定制的 AL 工作 → 第 6 节实验设置/结果/分析 → 第 7 节挑战与未来方向 → 第 8 节结论。

- **AL 的三种问题设定**（Section 2，依据 Settles 2009）：
  1. **成员查询合成（membership query synthesis）**：可对输入空间任意样本（含生成模型合成样本）查询标注，本文也称之为"生成式主动学习"；适合低维输入，但高维（如图像）时生成样本可能让人类标注者无法识别——与 AL 的结合在 4.4 节讨论。
  2. **流式选择性采样（stream-based selective sampling）**：样本逐个到达，需即时决定是否请求标注（Cohn 1994）；适合内存受限场景（如边缘计算），但忽略样本间相关性。
  3. **基于池的主动学习（pool-based AL）**：从大规模无标签池中抽样并请求 oracle（如医生）标注，是绝大多数 AL 工作采用的设定；若一次选多个样本则进一步称"批模式（batch-mode）"。深度 AL 默认即批模式池式（逐样本重训不现实，且单个样本未必带来显著提升）。**本综述除非特别说明，均默认批模式、基于池的 AL。**
- **核心数学公式化**（Section 2，设共 T 轮标注）：
  1. **样本选择**：第 t 轮用信息性函数 I 评估无标签池 D_u^t 中每个样本的信息量，再用采样策略 S 选出查询批次 D_q^t = S( I_{x∈D_u^t}(x, f_{θ_{t-1}}), b )（式 1），其中 f_{θ_{t-1}} 为上一轮模型，标注预算 b=|D_q^t|≪|D_u^t|。
  2. **专家标注**：D_q^t 送 oracle（如医生）标注，加入有标签集 D_l^t = D_l^{t-1} ∪ {(x,y)|x∈D_q^t}（式 2），并从无标签集移除 D_u^t = D_u^{t-1} \ {x|x∈D_q^t}（式 3）。
  3. **模型训练**：用本轮有标签集以全监督方式训练 θ_t = argmin_θ E_{(x,y)∈D_l^t}[ℓ(f_θ(x),y)]（式 4）。
  4. **重复**步骤 1–3，直至达到标注预算或预期性能。文中指出部分工作采用"一次性（one-shot）"选样，不分多轮（详见 5.2.2）。
  5. **初始化**：随机初始化的 f_{θ_0} 只能给出无意义的信息性，故多数工作随机选一批样本作初始有标签集 D_l^0 训练 f_{θ_0}；用预训练模型做更好初始化见 4.2 节。
  6. 文中还提到当前部分工作把 AL 与**交互式分割**结合：模型在交互中辅助专家标注以降低标注难度（详见 5.2.4）。
- **采样单元的灵活性**：医学影像 AL 多数时候按"图像级"（2D 或 3D）选样（本综述默认采样单元为图像）；但随发展也采用**区域级**（region-wise，4.3 / 4.5.2 节）或**切片级**（slice-wise，从 3D 体数据选关键切片，5.2.1 节）标注，以进一步减负。
- **核心方法分类**（Section 3）：把"信息性评估"与"采样策略"并列为 AL 的两大核心方法。
  1. **信息性评估（informativeness）**：定义每个样本被标注的价值，高信息性优先送标。两大典型指标：
     - **不确定性（uncertainty, 3.1）**：衡量模型预测的不确定程度；高不确定样本被视为"硬样本"、更易被当前模型误判，标注它们有助模型学新模式。文中按来源把不确定性分为偶然不确定性（AU，数据噪声如 MRI 运动伪影/CT 金属伪影，增数据不可减）与认知不确定性（EU，模型尚未掌握的知识，增数据可减）；但多数 AL 工作不区分二者，统一用"预测不确定性"（AU+EU 的复合），因显式分离通常困难且对 AL 实践收益有限（Kahl 2024）。基于单次前向预测概率的经典指标见 Table 1：**最小置信度** max_i p_i（↓越小越不确定）、**熵** -Σ p_i log p_i（↑）、**间隔 Margin**（最大与次大概率之差，↓）、**均值方差 Mean variance**（↑）。但深度网络存在臭名昭著的**过自信（over-confidence）**问题——对错分样本也给出极高置信（如 0.99），扭曲不确定性估计。为缓解过自信，3.1 把基于不确定性的 AL 进一步分为五类（taxonomy 见 Fig. 3）：
        - **多次推理（multiple inference, 3.1.1）**：在扰动下多次跑模型（如 MC Dropout、深度集成），两种用法——用多次推理的平均概率算经典指标，或取不同预测结果间的"分歧（disagreement）"，以降低架构/训练数据引入的偏差。
        - **基于梯度（gradient-based）**：用模型对输入/参数的梯度估计不确定性。
        - **性能估计（performance estimation, 3.1.3）**：直接估计在某样本上训练后预期的模型性能（用替代指标 surrogate metric，如预测 Dice / 损失），并可训练辅助网络做"可学习的性能估计"（据原文 p.13 线索，提取缓存未覆盖，待核）。
        - **不确定性感知模型（uncertainty-aware model, 3.1.4）**：设计能显式输出不确定性的网络（如证据深度学习 evidential deep learning 用证据分布替换 Softmax；据原文 p.13 线索，提取缓存未覆盖，待核）。
        - **对抗性方法（adversarial-based）**：通过对抗扰动寻找模型最不稳定的样本。
     - **代表性（representativeness, 3.2）**：衡量样本能否代表整个无标签数据分布，避免所选样本偏离总体分布、避免冗余，常基于特征空间聚类/覆盖（如 core-set 用若干"球"覆盖整个数据集、max cover 等；据原文 p.14–15 线索，提取缓存未覆盖，待核）。
  2. **采样策略（sampling strategy, 3.3）**：本文明确强调的**独特贡献**——首次显式把采样策略定义为 AL 的核心方法。仅按信息性分数排序取 top-k（贪婪选样）会因信息性分数本身有缺陷而导致**冗余或类别不平衡**。因此需要更高级的策略：
     - **多样性策略**：保证所选样本在特征空间彼此相异，避免信息冗余。
     - **类别平衡策略**：保证所选样本类别分布均衡。
     - **批次构建**：如何把信息性、多样性、平衡性等准则结合，构建高质量查询批次。

## 实验

提取缓存仅覆盖 PDF 前 12 页（约 25000/63603 字符），实验部分对应论文第 6 节（约 p.20+），**未被提取缓存覆盖**。提取文本仅说明：作者在多个医学影像数据集上评估若干主流 AL 方法性能并公开代码（Awesome-Active-Learning-for-Medical-Image-Analysis 仓库）。因此**具体数据集名称、对比方法清单、评价指标与数值结果无法从当前提取文本中核实**——需在完整论文第 6 节（含实验设置、结果、消融/泛化/效率分析）中查找，提取缓存未覆盖，待核。

## 局限

- **作为综述的固有局限**：本文不提出新 AL 算法，价值在梳理与总结；对比实验（据描述）未必涵盖所有最新方法。文中亦自陈"由于 AL 发展迅速，许多相关工作未能覆盖"，并提供持续更新的网站。
- **实验完整性待核**：提取缓存未覆盖第 6 节，无法据提取文本评估其对比实验是否充分（数据集多样性、方法覆盖面、是否含最新 SOTA）。
- **方法适用性边界**：AL 假设存在可查询的"专家标注者（oracle）"，在医疗领域即需医生资源；其效用取决于标注成本与性能增益的权衡，在标注成本已很低或数据需求极大的任务中优势可能不明显。
- **技术发展速度**：深度 AL 迭代很快，综述易很快出现未覆盖的新工作（文中已明确指出并给出持续更新链接）。

## 个人评论

1. **体系化的知识图谱**：本文给出深度 AL 在医学影像领域应用的完整框架——核心方法（信息性评估 vs. 采样策略）、技术融合趋势、特定应用场景，是快速进入该领域、把握全貌的优秀路线图。
2. **把"采样策略"提升为一等公民**：以往研究多在"不确定性/代表性"指标上做文章，本文首次把"如何基于这些指标设计批次采样策略"提升到与信息性评估同等的核心地位，并指明 top-k 贪婪选样会导致冗余与类别不平衡——这对方法设计有直接启发。
3. **技术融合的全景视野**：系统梳理 AL 与半监督、自监督、区域级 AL、生成模型、域自适应的结合，反映"组合拳"是解决实际标签稀缺问题的重要方向，为设计混合范式算法提供思路。
4. **扎实的成本论证**：用 BraTS 切片数、放射科医生 60 分钟/例、时薪 \$221、病理切片 15–30 分钟等具体数字把"标注昂贵"量化，比泛泛而谈更有说服力。
5. **社区贡献**：公开代码仓库与持续更新的论文列表（Awesome-Active-Learning-for-Medical-Image-Analysis）方便复现、对比与跟进，学术贡献精神良好。

### 使用建议

- **快速了解**：读摘要 + 引言 + 第 2 节（问题设定与公式化）+ 第 3.1 节（不确定性）开头，即可掌握主旨、核心矛盾与方法分类。
- **复现/对比**：重点看第 6 节（实验设置、数据集、实现细节、结果表）与作者 GitHub 仓库。
- **借鉴创新点**：学习其"信息性评估 vs. 采样策略"的分类框架，以及第 4 节技术融合的综述结构。
- **写 related work**：可作为"医学图像中的主动学习""标签高效学习""降低标注成本的深度学习"等分类下的全面基准综述引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A1b_医学图像_小样本_综述]]
> - [[R_综述_Survey]]
> - [[Q_自监督_对比学习_主动学习]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇关于**深度主动学习（deep active learning, deep AL）在医学图像分析中应用**的综述（Elsevier《Medical Image Analysis》2024，文章号 103201，标题页明确标为 "Survey paper"）。它系统梳理、分类并实验评估了用于降低医学图像标注成本的深度 AL 方法。论文属于"医学影像 × 标签高效学习"交叉领域，核心瓶颈是医学影像大规模高质量标注的高成本。综合其性质——医学影像 + 综述 + 小样本/标签高效——最贴切的主题是 **A1b_医学图像_小样本_综述**，并跨 **R_综述_Survey** 与 **Q_自监督_对比学习_主动学习**。（原笔记归在 A2_医学图像_分类_配准_生成 不准确：本文并非分类/配准/生成方法论文，而是 AL 综述。）

## 2. 一句话总结
本文首次系统综述了深度主动学习在医学图像分析中的核心方法（信息性评估 + 采样策略）、与其他标签高效技术（半监督/自监督/区域级 AL/生成模型/域自适应）的融合、以及面向医学影像定制的 AL 工作，并在多个医学影像数据集上做了公开可复现的对比实验。

## 3. 背景与问题
- **为什么做**：深度学习在医学影像分析中已逼近临床专家（皮肤癌分类、CT 肺癌筛查、息肉检测、WSI 前列腺癌检测等），但高度依赖大规模标注；而医学影像标注**高成本、高门槛**：① 像素级/病理切片标注耗时（病理切片检视 15–30 分钟/张，放射科医生分割脑肿瘤约 60 分钟/例，时薪中位数约 \$221）；② 需医学专业知识、难以众包、涉隐私，且多人多轮标注引入标注者内/间差异、再抬成本。数据规模虽增（BraTS 从 65→1200+ 患者，等价 70 万+ 张 2D 切片）仍小于自然图像。
- **之前方法的问题**：已有 AL 综述（Settles 2009、Ren 2021、Liu 2022、Zhan 2022、Takezoe 2023、Budd 2021、Tajbakhsh 2020、Jin 2023a）在四方面不足：覆盖最新进展不够、缺"AL+其他标签高效技术"融合的总结、极少在医学影像数据集上系统评估、对高标注成本的医学影像领域不够全面。
- **核心矛盾**：有限标注预算 vs. 高性能深度模型所需的大量标注数据。AL 以智能选样逼近全监督性能。

## 4. 核心贡献
1. **全面综述 + 新分类法**：详尽检索（Google Scholar/arXiv，沿引用扩展），涉及近 164 篇 AL 工作、234 篇参考文献，多来自顶刊顶会。
2. **系统总结采样策略**：突破以往只重"信息性评估"，总结多样性、类别平衡等采样策略。
3. **首次详述技术融合**：第一篇详细综述 AL 与半监督、自监督、区域级 AL、生成模型、域自适应的融合。
4. **公开对比实验**：多个医学影像数据集上评估主流 AL 方法并开源代码。

## 5. 方法详解
作为综述，其"方法"是对现有 AL 的梳理框架（Fig. 2 总体框架）：
- **三种 AL 设定**（Settles 2009）：成员查询合成（≈生成式 AL，高维图像下合成样本可能不可识别）、流式选择性采样（适合边缘/内存受限，忽略样本相关性）、基于池的 AL（主流，多样本一次选即"批模式"）。**本综述默认批模式池式 AL。**
- **数学公式化**（共 T 轮）：① 样本选择 D_q^t = S(I(·), b)，b=|D_q^t|≪|D_u^t|（式 1）；② oracle 标注、更新 D_l^t / D_u^t（式 2、3）；③ 全监督训练 θ_t=argmin E[ℓ]（式 4）；④ 重复至预算/性能达标；部分工作用一次性选样（5.2.2），需合理初始化 f_{θ_0}（4.2 用预训练模型）。
- **采样单元**：默认图像级（2D/3D），也可区域级（4.3/4.5.2）、切片级（5.2.1）；部分工作结合交互式分割（5.2.4）。
- **核心方法两分支**（Section 3）：
  - **信息性评估** = 不确定性（3.1）+ 代表性（3.2）。不确定性分 AU（数据噪声，不可减）/EU（模型未掌握，可减），多数工作不分离、统一用预测不确定性；单次前向的经典指标（Table 1）：最小置信度、熵、Margin、均值方差，但深度网络**过自信**会扭曲估计。缓解过自信的五类（Fig. 3）：多次推理（MC Dropout/集成，取平均概率或预测分歧，3.1.1）、基于梯度、性能估计（surrogate metric / 可学习性能估计，3.1.3）、不确定性感知模型（如证据深度学习替换 Softmax，3.1.4）、对抗性方法。代表性（3.2）基于特征空间覆盖（core-set/max cover 等）。
  - **采样策略**（3.3，本文独特贡献）：仅 top-k 贪婪选样会导致冗余/类别不平衡，故需多样性策略、类别平衡策略、批次构建（融合信息性+多样性+平衡性）。
- 第 4 节进一步综述 AL 与半监督、自监督、区域级 AL、生成模型、域自适应的融合；第 5 节综述医学影像定制工作（切片级、一次性、交互式分割等）。

## 6. 实验与结果
提取缓存仅覆盖 PDF 前 12 页（约 25000/63603 字符），第 6 节实验**未被覆盖**。仅知作者在多个医学影像数据集上评估若干主流 AL 方法并公开代码。**具体数据集、对比方法、指标与数值无法据提取文本核实**——需查完整论文第 6 节（提取缓存未覆盖，待核）。

## 7. 这篇论文真正有价值的地方
1. **体系化知识图谱**：完整框架（核心方法 + 技术融合 + 特定应用），适合入门与建立全局观。
2. **把"采样策略"提升为核心方法**：从"造更好的不确定性/代表性指标"转向"设计更优批次采样策略"，并点明 top-k 的冗余/类别不平衡缺陷——对方法设计有直接启发。
3. **技术融合全景**：系统总结 AL 与多种标签高效技术的"组合拳"，指向混合范式算法。
4. **成本量化与社区贡献**：用具体数字论证标注昂贵；开源代码 + 持续更新论文列表便于复现跟进。

## 8. 局限与问题
- 综述不提新算法，对比实验未必涵盖所有最新方法（文中自陈许多工作未覆盖、提供更新网站）。
- 提取缓存未覆盖第 6 节，对比实验是否充分待核。
- AL 依赖可查询的 oracle（医生资源），效用取决于标注成本与性能增益的权衡。
- 领域迭代快，综述易很快出现未覆盖工作。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + 第 2 节（设定/公式化）+ 第 3.1 节（不确定性）开头。
- **复现/对比**：第 6 节 + 作者 GitHub 仓库（Awesome-Active-Learning-for-Medical-Image-Analysis）。
- **借鉴创新点**："信息性评估 vs. 采样策略"分类框架 + 第 4 节技术融合结构。
- **写 related work**：作为"医学图像中的主动学习""标签高效学习""降低标注成本的深度学习"等分类下的基准综述引用。

## 10. 和其他论文的关系
本文综述自身关联到大量子方向，可与库内同主题论文互链（以下为基于主题的推测，需确认库内是否存在对应笔记）：
- `[[A1b_医学图像_小样本_综述]]`（同主题首页：医学图像小样本/综述）
- `[[Q_自监督_对比学习_主动学习]]`（本文核心技术：主动学习 / 与自监督、对比学习的融合）
- `[[R_综述_Survey]]`（综述类聚合）
- 文中重点综述的融合技术（半监督、自监督学习）方向的医学影像论文。

*注：上述 `[[双链]]` 仅为基于主题的示意，实际引用需确认库内对应笔记是否存在。*

## 11. 关键词
主动学习, 深度主动学习, 医学图像分析, 标签高效学习, 标注成本, 信息性评估, 不确定性, 代表性, 采样策略, 半监督, 自监督, 综述

## 12. 可信度说明
本笔记主要依据 PDF 提取文本（缓存覆盖前 12 页 / 约 25000 字符，原文共约 63603 字符）。该文本完整涵盖标题、作者单位、摘要、引言（含标注成本论证与已有综述局限）、第 2 节问题设定与数学公式化（式 1–4）、第 3 节核心方法导引、第 3.1 节不确定性（含 Table 1 经典指标与过自信问题、AU/EU 区分、3.1.1 多次推理开头）。**第 3.1.3 性能估计、3.1.4 不确定性感知模型、3.2 代表性的细节**仅据原笔记"全文补读记录"中的 p.13–15 页线索补充并已标注"提取缓存未覆盖, 待核"；**第 4 节技术融合细节、第 5 节医学影像定制、第 6 节实验、第 7–8 节讨论与结论**均未被提取缓存覆盖，本笔记未编造其具体内容。分类已据正文性质从 A2_医学图像_分类_配准_生成 更正为 A1b_医学图像_小样本_综述（医学影像 + 综述 + 标签高效/小样本）。结构保持 12 个 H2 章节，内容均来自提取文本或明确标注的待核来源，无编造。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本 2086 字符/页, 清晰可读); 提取缓存覆盖 = 12/34 页 (约 25000/63603 字符); 关键数字/公式/分类均可在提取文本核实, 第 4–8 节及实验数据未被缓存覆盖、已标注待核; 来源缓存: `.paper-cache/extracts/A-comprehensive-survey-on-deep-active-learning-in-medi_2024_Medical-Image-An.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-34; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-34。
- **提取情况**: 缺失页 22 页, 其中 22 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Medical Image Analysis 95 (2024) 103201
- p.13: 3.1.3. Performance estimation
- p.13: In this section, uncertainty metrics are estimations of the current
- p.13: Surrogate metrics are widely used in active learning of medical image
- p.13: They found a linear correlation between this average Dice and the real
- p.13: Learnable performance estimation: We can train auxiliary neural
- p.13: method also outperformed several AL baselines. In lung nodule detec-
- p.13: AL focuses only on uncertainty ranking of the unlabeled samples, Kim
- p.13: Thus, they replaced the loss regressor in LLAL with the ranker in
- p.13: 3.1.4. Uncertainty-aware model
- p.13: In the above sections, uncertainty is derived based on the commonly
- p.13: Evidential deep learning replaces the Softmax distribution with a

### 缺失页关键摘录

- p.13: or task-specific evaluation metrics. These metrics reflect the level of
- p.13: loss or task-specific evaluation metrics. In breast cancer segmentation
- p.13: correlation with the evaluation metrics with post-hoc validation.
- p.14: 3.2. Evaluation of informativeness: Representativeness
- p.14: the overall data distribution. This discrepancy introduces dataset bias
- p.14: samples that can represent the entire dataset. Specifically, representa-
- p.14: query result and try to keep the original data distribution as much
- p.14: of a dataset. Besides, the uniqueness of medical images may require
- p.15: entire dataset, which is analogous to using several spheres to cover all
- p.15: the dataset. To achieve this goal, the radius of its covering spheres may
- p.15: The goal of max cover is to cover as much of the entire dataset as
- p.15: tation of unlabeled samples with the labeled dataset. Enhanced feature
<!-- AI_READING_NOTE_END -->
