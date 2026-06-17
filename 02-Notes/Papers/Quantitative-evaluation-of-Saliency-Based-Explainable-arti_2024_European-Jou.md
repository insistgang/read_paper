---
title: EuropeanJournalofRadiology173(2024)111356
authors:
  - "Esma Cerekci"
  - "Deniz Alis"
  - "Nurper Denizoglu"
  - "Ozden Camurdan"
  - "Mustafa Ege Seker"
  - "Caner Ozer"
  - "Muhammed Yusuf Hansu"
  - "Toygar Tanyel"
  - "Ilkay Oksuz"
  - "Ercan Karaarslan"
year: 2024
venue: "journal homepage: www.elsevier.com/locate/ejrad"
doi: 10.1016/j.ejrad.2024.111356
pdf: [[Quantitative-evaluation-of-Saliency-Based-Explainable-arti_2024_European-Jou.pdf]]
primary_topic: A2_医学图像_分类_配准_生成
topics:
  - "A2_医学图像_分类_配准_生成"
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/Quantitative-evaluation-of-Saliency-Based-Explainable-arti_2024_European-Jou.txt
---

# EuropeanJournalofRadiology173(2024)111356

## 基本信息
- **PDF**: [[Quantitative-evaluation-of-Saliency-Based-Explainable-arti_2024_European-Jou.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Quantitative evaluation of Saliency-Based Explainable artificial intelligence (XAI) methods in Deep Learning-Based mammogram analysis |
| **作者** | Esma Cerekci; Deniz Alis; Nurper Denizoglu; Ozden Camurdan; Mustafa Ege Seker; Caner Ozer; Muhammed Yusuf Hansu; Toygar Tanyel; Ilkay Oksuz; Ercan Karaarslan |
| **发表时间** | 2024 |
| **刊物/会议** | European Journal of Radiology 173 (2024) 111356 |
| **DOI** | 10.1016/j.ejrad.2024.111356 |

## 摘要

**英文原摘要（据 PDF 提取文本清理）**：

> **Background:** Explainable Artificial Intelligence (XAI) is prominent in the diagnostics of opaque deep learning (DL) models, especially in medical imaging. Saliency methods are commonly used, yet there's a lack of quantitative evidence regarding their performance.
> **Objectives:** To quantitatively evaluate the performance of widely utilized saliency XAI methods in the task of breast cancer detection on mammograms.
> **Methods:** Three radiologists drew ground-truth boxes on a balanced mammogram dataset of women (n = 1496 cancer-positive and negative scans) from three centers. A modified, pre-trained DL model was employed for breast cancer detection, using MLO and CC images. Saliency XAI methods, including Gradient-weighted Class Activation Mapping (Grad-CAM), Grad-CAM++, and Eigen-CAM, were evaluated. We utilized the Pointing Game to assess these methods, determining if the maximum value of a saliency map aligned with the bounding boxes, representing the ratio of correctly identified lesions among all cancer patients, with a value ranging from 0 to 1.
> **Results:** The development sample included 2,244 women (75%), with the remaining 748 women (25%) in the testing set for unbiased XAI evaluation. The model's recall, precision, accuracy, and F1-Score in identifying cancer in the testing set were 69%, 88%, 80%, and 0.77, respectively. The Pointing Game Scores for Grad-CAM, Grad-CAM++, and Eigen-CAM were 0.41, 0.30, and 0.35 in women with cancer and marginally increased to 0.41, 0.31, and 0.36 when considering only true-positive samples.
> **Conclusions:** While saliency-based methods provide some degree of explainability, they frequently fall short in delineating how DL models arrive at decisions in a considerable number of instances.

**中文翻译**：

> **背景**：可解释人工智能（XAI）在解读不透明的深度学习（DL）模型时占据重要地位，在医学影像领域尤为突出。基于显著性（saliency）的方法被广泛使用，但关于其性能的定量证据仍然缺乏。
> **目标**：定量评估广泛使用的显著性 XAI 方法在乳腺 X 光（mammogram）乳腺癌检测任务上的性能。
> **方法**：三位放射科医生在来自三个中心的平衡乳腺 X 光数据集（n = 1496 例癌症阳性与等量阴性）上绘制了地面真值边界框。采用一个经过改造的预训练 DL 模型进行乳腺癌检测，输入 MLO 与 CC 两个视图。评估的显著性 XAI 方法包括梯度加权类激活映射（Grad-CAM）、Grad-CAM++ 和 Eigen-CAM。使用 Pointing Game 评估这些方法，判断显著性图的最大值是否落在边界框内，得到在所有癌症患者中被正确定位病灶的比例，取值范围 0 到 1。
> **结果**：开发集包含 2244 名女性（75%），其余 748 名（25%）作为测试集用于无偏的 XAI 评估。模型在测试集上识别乳腺癌的召回率、精确率、准确率和 F1 分数分别为 69%、88%、80% 和 0.77。在乳腺癌女性中，Grad-CAM、Grad-CAM++ 和 Eigen-CAM 的 Pointing Game 分数分别为 0.41、0.30 和 0.35；仅考虑真阳性样本时，分数小幅提升至 0.41、0.31 和 0.36。
> **结论**：虽然基于显著性的方法提供了一定程度的可解释性，但在相当数量的实例中，它们往往无法刻画 DL 模型究竟是如何得出决策的。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：乳腺 X 光是乳腺癌检测的首选手段（普及、性价比高、灵敏度可靠），但日益增长的阅片需求给放射科医生带来沉重负担，可能导致报告延迟、漏检和诊断错误增多。深度学习（DL）在乳腺癌检测上已被多项研究证明可媲美甚至超越放射科医生，但其包含数百万乃至数十亿参数的"黑盒/不透明"特性，在乳腺癌检测这类高风险任务中引发了信任和安全担忧。
- **之前方法的问题**：一篇近期关于医学影像 XAI 的系统综述指出，约三分之一的研究采用了某种 XAI 方法，其中可视化或基于显著性的技术最为常用；但绝大多数研究只对 XAI 做**定性**评价，且常常只挑选（cherry-pick）有利的示例展示，缺乏系统、客观的定量性能评估。只有极少数研究（文中引用 [17–19]）对 XAI 方法做过定量考察。
- **作者想解决的核心矛盾**：XAI（尤其显著性图方法）在医学影像中应用日益普遍，但其**解释的定位准确性**究竟有多可靠尚无定量证据。本文旨在用客观指标（Pointing Game Score）量化常用显著性 XAI 方法在乳腺癌检测中的定位表现，揭示"广泛使用"与"实际可靠性"之间的差距。

## 关键贡献

1.  **构建了平衡的乳腺癌数据集并配专家标注**：从三所大学医院（2016.01–2020.01）初筛 28324 名女性，排除有乳腺手术/放化疗史者（n=124），最终纳入 1496 例病理证实的乳腺癌，并通过分层欠采样匹配出 1496 例非乳腺癌（BI-RADS 1/2 或病理证实良性），构成平衡数据集（共 2992 例），由三位资深乳腺放射科医生共识绘制边界框作为地面真值。
2.  **改造的多视图深度学习模型**：采用 ImageNet 预训练的 ResNet50，关键改造为（a）双输入通道，同时输入同一乳房的 MLO 与 CC 视图以融合互补信息；（b）将最后的全连接层替换为线性层 + Sigmoid，做二分类并输出概率。
3.  **系统定量评估三种主流显著性 XAI 方法**：对 Grad-CAM、Grad-CAM++、Eigen-CAM 在同一乳腺癌检测任务上做横向定量比较。
4.  **以 Pointing Game 作为客观定位指标**：把"XAI 是否解释正确"转化为可计算的客观问题——显著性图的最大激活点是否落在专家边界框内（含偏移量 τ=15）。
5.  **给出冷静的性能基准**：即使只看模型预测正确（真阳性）的样本，三种方法的 Pointing Game 分数也仅 0.31–0.41，统计上彼此无显著差异，说明显著性图解释能力有限，为该方向提供了重要的定量参照。

## 方法

- **整体框架**：流程分为数据准备与标注、DL 模型训练、XAI 方法应用、XAI 性能定量评估四个阶段（图 1 给出 DL pipeline）。
- **输入与输出**：
    - **输入**：同一乳房的 MLO（中外侧斜位）与 CC（头尾位）两张乳腺 X 光，经裁剪、填充、重采样为 512×512、形成 2 通道输入。
    - **模型输出**：0 到 1 之间的概率，表示该乳房患癌可能性。
    - **XAI 输出**：针对输入生成的显著性热力图（saliency map）。
- **关键模块与连接**：
    1.  **图像预处理**：用自研的基于 patch 的算法找出能包住乳房的最大矩形，裁掉乳腺组织周围的空白区域（不损失乳房关键信息），再填充/重采样到统一的 512×512；入模前由放射科医生确认裁剪有效、信息完整。
    2.  **深度学习模型**：基于 PyTorch 1.7.1，采用 ImageNet 预训练 **ResNet50** 改造为**多视图分类网络**——双通道分别喂入 MLO/CC（文献 [26] 证明多视图优于单视图）；末层全连接换成**线性变换 + Sigmoid**，做二分类并输出概率。
    3.  **三种 XAI 方法（均为事后、无需改模型结构）**：
        - **Grad-CAM**：利用流入**最终卷积层**的梯度信息理解每个神经元对目标决策的贡献，生成高亮输入中影响网络输出区域的热力图。
        - **Grad-CAM++**：Grad-CAM 的扩展，考虑**多层、多节点信息**（不像 Grad-CAM 只聚焦最后卷积层），能捕获特征图中的多模态行为（而非仅峰值），对存在多个感兴趣区域时解释更细致。
        - **Eigen-CAM**：对最终卷积层特征图的**空间维度做特征分解（eigen-decomposition）**，结合特征值与特征向量生成类激活图；与 Grad-CAM/Grad-CAM++ 不同，它能处理特征图中的**负值**，更适合含 BatchNorm 或 ReLU 层的模型。
    4.  **评估模块（Pointing Game）**：核心是判断显著性图的最大激活点是否落在专家边界框内，并允许一个偏移量 **τ=15**（该值由乳腺癌专家给出，是模型关注区与临床病灶位置关系的现实近似）。本研究采用**图像级（image-level）分析、按每个视图独立评估**——因为乳腺病灶可能在某一视图（MLO 或 CC）更明显甚至仅在单视图可见，故病灶在一个视图被高亮、另一视图未被高亮时，两视图分开评分。
- **训练方式**：
    - 损失函数：交叉熵（Cross-Entropy）损失。
    - 优化器：Adam。
    - 学习率策略：StepLR 调度器，初始学习率 0.0001，每 20 个 epoch 衰减为原来的 0.5 倍。
    - 训练周期：100 个 epoch；批大小：16。
    - 数据增强（on-the-fly）：转置、垂直/水平翻转、随机平移、缩放、旋转。
- **推理与评估流程**：输入一对 MLO/CC 图像，模型输出癌症概率。Pointing Game 分数**只对癌症患者计算**（阴性/良性 BI-RADS 1–2 作为负样本，无边界框）。对每张显著性图取最大激活像素，判断是否在专家框内（含 τ=15），准确记为 T、不准确记为 F，分数 = T/(T+F)。
- **和已有方法的差异**：与大量只做定性展示 XAI 热力图、并挑选有利示例的研究不同，本文核心差异是**系统性地使用客观定量指标（Pointing Game Score）+ 专家边界框地面真值**来评估 XAI 的定位准确性。

## 实验

- **数据集**：三中心回顾性数据，初筛 28324 例、排除 124 例，最终 2992 名女性（中位年龄 49 岁，IQR 8）；1496 名（50%）病理证实乳腺癌、1496 名（50%）阴性。每位患者仅纳入一次乳腺 X 光检查。按 75%/25% 分层划分为开发集（2244 人）与测试集（748 人，用于无偏 XAI 评估）。
- **对比方法**：本文比较的是三种显著性 XAI 方法（Grad-CAM、Grad-CAM++、Eigen-CAM）之间的表现，并与专家边界框地面真值对齐评估；未与 LIME、SHAP 等其他 XAI 方法做对比。
- **评价指标**：
    - 模型性能：召回率、精确率、准确率、F1 分数（准确率/召回率/精确率均给出 95% 置信区间）。
    - XAI 性能：**Pointing Game Score = T/(T+F)**，T 为最大激活点落在边界框内的准确实例数，F 为不准确实例数。
- **主实验结果**：
    - DL 模型测试集性能：**召回率 69%（95%CI 0.621–0.759），精确率 88%（95%CI 0.828–0.932），准确率 80%（95%CI 0.735–0.865），F1 = 0.77**。
    - 全体癌症患者的 Pointing Game Score：**Grad-CAM 0.41，Grad-CAM++ 0.30，Eigen-CAM 0.35**。
    - 仅真阳性样本时小幅提升：**Grad-CAM 0.41，Grad-CAM++ 0.31，Eigen-CAM 0.36**。
    - Grad-CAM 在三者中表现最高；三种方法间无统计学显著差异。
    - 统计检验存在表述不一致：方法部分（2.6）说用 **Wilcoxon 检验**（p<0.05 为显著）比较三种方法，结果部分（3.）却写"按 **Kruskal-Wallis** 检验无显著差异"。两处检验名称不一致，疑为原文笔误，以原文为准记录。
    - 图 3–5 展示了测试集上 XAI 方法的代表性示例（提取文本未给出图内具体数值）。
- **消融实验**：PDF 文本未明确说明针对模型结构或 XAI 方法的消融实验。
- **泛化实验**：PDF 文本未提及在其他数据集或任务上的泛化实验（讨论中仅与 Arun et al. 在气胸/肺炎胸片上的结果做定性对照）。
- **速度/参数量/FLOPs 等效率信息**：PDF 文本未明确说明（仅提到为兼顾计算效率与训练时间将 batch size 设为 16）。

## 局限

- **方法适用场景**：基于显著性的 XAI 在精确定位上能力有限（最高分仅约 0.41），对微钙化等微小病灶或边界模糊病灶可能尤其不可靠；本研究结果直接印证了这一点。
- **实验充分性**：评估仅用 Pointing Game 这一种指标，难以全面反映 XAI 的其他属性（稳定性、可重复性、对比类敏感性等）；模型召回率仅 69%，本身不算高，可能限制 XAI 评估的上限。
- **数据集**：虽做了平衡，但数据来自同一大学医院系统（虽含三个中心），且对非癌组做了欠采样（作者承认可能引入偏倚，已用分层随机采样缓解）；约 3000 例规模在当前 DL 标准下不算大。
- **标注/评估假设**：严重依赖三位放射科医生共识绘制的边界框作为"黄金标准"，且**未做独立标注、未评估评分者间一致性**（作者明确说不在本研究范围内），病灶精确边界本身存在主观性；Pointing Game 的偏移量 τ=15 为人为设定。
- **统计口径**：方法与结果部分对所用检验的命名不一致（Wilcoxon vs Kruskal-Wallis），需查原文确认。
- **复现风险**：专家标注耗时且需专业知识，复现成本高；图像预处理自研算法的细节未完全公开。

## 个人评论

这篇论文最有价值的地方在于它对常用 XAI 方法在真实临床任务中的性能做了**冷静、定量的祛魅**，而非一味宣扬 XAI 的好处。它揭示了一个让人不太舒服但很重要的事实：即使在模型预测正确（真阳性）的情况下，依赖显著性热力图去"理解"模型决策也高度不可靠——最高分仅 0.41 左右，意味着即便放宽到 τ=15 的偏移，仍有过半样本的峰值落在病灶框外。

1.  **研究启发**：它用一个朴素却有力的指标（Pointing Game）戳破了"热力图大致对上病灶 = XAI 有效"的直觉，推动领域从"挑图展示"走向严谨定量评估。
2.  **实践启发**：临床上不能把 AI 给出的"解释热力图"当作可信的定位依据；高分类性能（精确率 88%）与低解释定位（0.41）可以并存，二者必须分开评估。
3.  **实验设计启发**：其"专家共识边界框 + Pointing Game + 多视图独立评分"的框架，可作为其他医学影像 XAI 研究可复用的评估范式。
4.  **需要审视之处**：结论的强度受制于较低的模型召回率（69%）和单一指标；若模型本身更强、或叠加忠实度（faithfulness）/稳定性等多指标，结论是否依然成立值得后续验证。此外原文方法与结果对统计检验的命名不一致，提醒读者引用其数值时留意。

### 使用建议

- **如果快速了解**：读**摘要**与**讨论（Discussion）**即可掌握动机、方法与主要结论。
- **如果复现**：重点看方法部分的 2.2 Ground truthing、2.3 DL model、2.4 XAI methods、2.5/2.6 评估与统计，弄清标注流程、ResNet50 多视图改造、三种 XAI 选择及 Pointing Game（τ=15、图像级、按视图评分）的具体设置。
- **如果借鉴创新点**：学习其"为 XAI 设计客观定量评估"的思路——构建带专家标注的平衡数据集、选择 Pointing Game 这类可计算指标，以及"多视图输入融合 + 按视图独立评分"的做法。
- **如果写 related work**：可归入"**医学影像 XAI 的定量评估**"类别，与 Arun et al. [18]（胸片气胸/肺炎）并列，作为显著性方法定位可靠性偏低的代表性证据之一。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于医学图像分析中的**可解释人工智能（XAI）定量评估**方向，落点在乳腺 X 光（mammogram）乳腺癌检测这一具体临床任务上。它不提出新模型，而是回答一个具体问题：常用的基于显著性的 XAI 方法（Grad-CAM、Grad-CAM++、Eigen-CAM）在解释乳腺癌分类模型时到底有多"准"？因其底层任务是乳腺 X 光的二分类（患癌 vs 非患癌）、并评估该分类模型决策的可解释性，归入主题 `A2_医学图像_分类_配准_生成`（医学图像分类）是恰当的。

## 2. 一句话总结
本文用 Pointing Game Score 在一个三中心、专家标注的平衡乳腺 X 光数据集上定量评估了 Grad-CAM、Grad-CAM++、Eigen-CAM 三种显著性 XAI 方法的定位准确性，发现即使在模型预测正确时它们的分数也仅 0.31–0.41，常常无法解释 DL 模型究竟如何做出决策。

## 3. 背景与问题
- **为什么要做**：乳腺 X 光是乳腺癌检测首选手段，但阅片负担重；DL 已能媲美/超越放射科医生，却因"黑盒"特性在高风险诊断中引发信任担忧。XAI（尤其显著性图）被用来打开黑盒。
- **之前方法的问题**：近期 XAI 系统综述指出约 1/3 研究用了 XAI，可视化/显著性方法最常用，但绝大多数只做**定性**评价、挑选有利示例展示，仅极少数（[17–19]）做过定量考察。
- **核心矛盾**：显著性 XAI 在医学影像中广泛使用，但其定位是否可靠缺乏定量证据。本文用客观指标量化这一差距。

## 4. 核心贡献
1.  **三中心平衡数据集 + 专家边界框**：从 28324 初筛、排除 124，得 1496 癌 + 1496 非癌（欠采样分层匹配）共 2992 例，三位资深乳腺放射科医生共识标注病灶框为地面真值。
2.  **改造的多视图 ResNet50**：ImageNet 预训练 ResNet50，双通道输入 MLO/CC，末层换线性 + Sigmoid 做二分类输出概率。
3.  **三种显著性 XAI 的横向定量比较**：Grad-CAM、Grad-CAM++、Eigen-CAM 在同一任务上对比。
4.  **Pointing Game 客观指标**：显著性图最大激活点是否落在专家框内（含 τ=15 偏移），把"解释对不对"变成可计算量。
5.  **冷静的性能基准**：真阳性样本上三方法分数仅 0.31–0.41，统计上无显著差异，给出该方向重要的定量参照。

## 5. 方法详解
- **整体框架**：数据准备与标注 → DL 模型训练 → 应用 XAI → Pointing Game 定量评估（图 1 给出 DL pipeline）。
- **输入/输出**：输入同一乳房的 MLO + CC（裁剪/填充/重采样为 512×512、2 通道）；模型输出 0–1 患癌概率；XAI 输出显著性热力图。
- **关键模块**：
    1.  **预处理**：基于 patch 的自研算法找包住乳房的最大矩形裁掉空白，再填充/重采样到 512×512，入模前放射科医生复核裁剪有效性。
    2.  **DL 模型（PyTorch 1.7.1）**：ImageNet 预训练 ResNet50 → 多视图分类网络（双通道 MLO/CC，文献 [26] 证明优于单视图）；末层全连接换线性 + Sigmoid。
    3.  **三种 XAI（事后、不改结构）**：Grad-CAM（最终卷积层梯度，高亮影响输出的区域）；Grad-CAM++（多层多节点信息，捕获多模态行为，多 ROI 时更细致）；Eigen-CAM（对最终卷积层特征图空间维做特征分解，能处理负值，适合含 BatchNorm/ReLU 的模型）。
    4.  **Pointing Game**：判断显著性图峰值是否落在专家框内（τ=15，由乳腺癌专家给定）；采用图像级、按视图独立评分（病灶可能仅在 MLO 或 CC 可见）。
- **训练**：交叉熵损失、Adam；StepLR（初始 lr 0.0001，每 20 epoch ×0.5）；100 epoch；batch 16；增强含转置/翻转/平移/缩放/旋转（on-the-fly）。
- **评估口径**：Pointing Game 仅对癌症患者算（阴性/良性无框）；分数 = T/(T+F)，T 准确、F 不准确。
- **与已有差异**：用客观定量指标 + 专家框评估 XAI 定位，而非定性挑图。

## 6. 实验与结果
- **数据集**：2992 名女性（中位年龄 49，IQR 8），1496 癌 + 1496 非癌；每人一次检查；75%/25% 分层划分 → 开发集 2244、测试集 748。
- **对比**：三种 XAI 互比并与专家框对齐；未与 LIME/SHAP 比较。
- **指标**：模型用召回/精确/准确/F1（前三者带 95%CI）；XAI 用 Pointing Game Score = T/(T+F)。
- **主结果**：
    - 模型测试集：召回 **69%**（95%CI 0.621–0.759）、精确 **88%**（0.828–0.932）、准确 **80%**（0.735–0.865）、F1 **0.77**。
    - 全体癌症患者 Pointing Game：Grad-CAM **0.41**、Grad-CAM++ **0.30**、Eigen-CAM **0.35**。
    - 仅真阳性：Grad-CAM **0.41**、Grad-CAM++ **0.31**、Eigen-CAM **0.36**。
    - Grad-CAM 表现最高；三者间无统计显著差异。
    - **统计检验表述不一致**：方法 2.6 写用 Wilcoxon 检验，结果 3. 写按 Kruskal-Wallis 检验无显著差异（疑原文笔误，照原文记录）。
    - 图 3–5 为代表性示例（提取文本未含图内数值）。
- **消融/泛化/效率**：PDF 文本均未明确说明（仅提 batch=16 出于计算效率考虑）。

## 7. 这篇论文真正有价值的地方
价值在于它对常用 XAI 方法做了**冷静、定量的祛魅**而非吹捧。核心发现：即使模型预测正确，依赖显著性热力图"理解"决策也很不可靠（最高仅约 0.41，意味放宽到 τ=15 仍过半样本峰值在框外）。启示：
1.  **研究**：用朴素却有力的 Pointing Game 戳破"热力图大致对上病灶 = XAI 有效"的直觉，推动从挑图展示走向严谨定量评估。
2.  **实践**：高分类性能（精确率 88%）与低解释定位（0.41）可并存，临床不可把热力图当作可信定位依据。
3.  **实验设计**："专家共识框 + Pointing Game + 多视图独立评分"是可复用的评估范式。

## 8. 局限与问题
- **方法适用场景**：显著性 XAI 定位能力有限，对微钙化等微小/边界模糊病灶尤其不可靠。
- **实验充分性**：仅用 Pointing Game 单指标，未覆盖稳定性/可重复性/对比类敏感性；模型召回 69% 偏低，可能限制评估上限。
- **数据集**：来自同一大学医院系统（含三中心），对非癌组欠采样（作者承认或引入偏倚，已用分层随机采样缓解）；约 3000 例规模不算大。
- **标注假设**：依赖三位医生共识框为金标准，未做独立标注、未评估评分者间一致性（明确不在范围内）；τ=15 为人为设定。
- **统计口径**：Wilcoxon 与 Kruskal-Wallis 命名不一致，需查原文。
- **复现风险**：专家标注成本高；预处理算法细节未完全公开。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要 + 讨论即可。
- **复现**：精读 2.2–2.6（标注、ResNet50 多视图改造、三种 XAI、Pointing Game τ=15/图像级/按视图评分、统计）。
- **借鉴创新点**：学习"为 XAI 设计客观定量评估"的思路——带专家标注的平衡数据集 + Pointing Game + 多视图独立评分。
- **写 related work**：归入"医学影像 XAI 的定量评估"，与 Arun et al. [18]（胸片气胸/肺炎）并列。

## 10. 和其他论文的关系
根据文中引用，相关工作包括：
- **医学影像 XAI 系统综述**：文中提及的近期综述 [15]，指出约 1/3 研究用 XAI、显著性方法最常用且多为定性评价。
- **其他 XAI 定量评估研究**：Arun et al. [18] 在公开数据集上评估显著性方法检测气胸/肺炎，但用 precision-recall 曲线下面积衡量定位、跨不同模态，故与本文结果无法直接比较（本文据此做定性对照，结论一致）。
- **乳腺癌检测的 DL 研究**：文中引用 [11,12] 等大量用 DL 检测乳腺癌的工作，本文为这一方向提供 XAI 层面的补充评估。
由于提取文本未给出完整参考文献列表，且不确定其他论文确切标题，此处不做猜测性 `[[双链]]`。

## 11. 关键词
Breast Cancer, Deep Learning, Mammogram, Explainable Artificial Intelligence (XAI), Grad-CAM, Grad-CAM++, Eigen-CAM, Pointing Game, Quantitative Evaluation, Saliency Maps, Medical Image Analysis

## 12. 可信度说明
本精读笔记基于 PDF 提取文本（缓存标注 8/8 页，但文本在 25000 字符处截断，原文约 41407 字符——讨论后半段、结论及参考文献列表未完整覆盖）。笔记中的样本量、模型性能（69%/88%/80%/0.77 及置信区间）、Pointing Game 分数（0.41/0.30/0.35 与 0.41/0.31/0.36）、τ=15、训练超参等关键数据均直接引自提取文本可见部分。已主动标注两处需注意点：(a) 原文方法与结果对统计检验的命名不一致（Wilcoxon vs Kruskal-Wallis）；(b) 图 3–5 内具体数值、讨论后半段及参考文献因截断未覆盖。缺失信息已在相应章节注明"PDF 文本未明确"。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (3130 字符/页)); 但提取缓存正文在 25000 字符处截断 (原文约 41407 字符, 讨论后半段/结论/参考文献未完整覆盖); 提取文本对统计检验有 Wilcoxon vs Kruskal-Wallis 两种不一致表述, 已照原文标注待核; 来源缓存: `.paper-cache/extracts/Quantitative-evaluation-of-Saliency-Based-Explainable-arti_2024_European-Jou.txt` (8/8 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
