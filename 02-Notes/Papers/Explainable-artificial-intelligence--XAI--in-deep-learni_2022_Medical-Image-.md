---
title: "Explainable artificial intelligence (XAI) in deep learning-based medical image analysis"
authors:
  - "Bas H.M. van der Velden"
  - "Hugo J. Kuijf"
  - "Kenneth G.A. Gilhuijs"
  - "Max A. Viergever"
year: 2022
venue: Medical Image Analysis
doi: 10.1016/j.media.2022.102470
pdf: [[Explainable-artificial-intelligence--XAI--in-deep-learni_2022_Medical-Image-.pdf]]
primary_topic: R_综述_Survey
topics:
  - "R_综述_Survey"
  - "A2_医学图像_分类_配准_生成"
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
extract_cache: .paper-cache/extracts/Explainable-artificial-intelligence--XAI--in-deep-learni_2022_Medical-Image-.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/21 pages"
---
# Explainable artificial intelligence (XAI) in deep learning-based medical image analysis

## 基本信息
- **PDF**: [[Explainable-artificial-intelligence--XAI--in-deep-learni_2022_Medical-Image-.pdf]]
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`, `A2_医学图像_分类_配准_生成`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Explainable artificial intelligence (XAI) in deep learning-based medical image analysis |
| **作者** | Bas H.M. van der Velden; Hugo J. Kuijf; Kenneth G.A. Gilhuijs; Max A. Viergever（荷兰乌得勒支大学医学中心 Image Sciences Institute） |
| **发表时间** | 2022（Received 22 Jul 2021; Accepted 2 May 2022） |
| **刊物/会议** | Medical Image Analysis, vol. 79, art. 102470（open access, CC BY） |
| **DOI** | 10.1016/j.media.2022.102470 |

## 摘要

**清理后的英文原摘要（据 PDF 提取文本整理）**:

> With an increase in deep learning-based methods, the call for explainability of such methods grows, especially in high-stakes decision making areas such as medical image analysis. This survey presents an overview of explainable artificial intelligence (XAI) used in deep learning-based medical image analysis. A framework of XAI criteria is introduced to classify deep learning-based medical image analysis methods. Papers on XAI techniques in medical image analysis are then surveyed and categorized according to the framework and according to anatomical location. The paper concludes with an outlook of future opportunities for XAI in medical image analysis.

**中文翻译**:

> 随着基于深度学习的方法日益增多，对这类方法可解释性的呼声也在增长，尤其是在医学图像分析这种高风险（high-stakes）决策领域。本综述概述了基于深度学习的医学图像分析中所使用的可解释人工智能（XAI）。文中引入了一套 XAI 评判标准框架，用以对基于深度学习的医学图像分析方法进行分类。随后按该框架以及按解剖部位（anatomical location）对医学图像分析中的 XAI 技术论文进行了梳理和归类。论文最后给出了 XAI 在医学图像分析中未来机会的展望。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：深度学习是当前医学图像分析的 state-of-the-art（Litjens et al., 2017; Meijering, 2020; Shen et al., 2017），但神经网络由众多通过非线性关系交织的层构成，即使逐层检视也无法完全理解其决策过程，因而被视为"黑盒"。在医疗这类高风险决策领域，这种不可理解性可能掩盖模型的偏见（bias）并带来深远后果。
- **法规与社会驱动**：欧盟《通用数据保护条例》（GDPR，第 15 条）要求患者有权获得关于决策"如何做出"的有意义信息。文中还提到 DARPA（美国国防高级研究计划局）以及 ACM FAccT（公平性、问责制与透明性）会议等推动 XAI 的代表性举措。
- **术语**：文献中 "interpretable deep learning" 与 "explainable artificial intelligence (XAI)" 常被互换使用（Adadi and Berrada, 2018; Murdoch et al., 2019），本文统一采用 XAI 一词。"好的解释"被界定为：能让人洞察神经网络如何做出决策、和/或使决策变得可理解。
- **核心矛盾**：深度学习在医学图像分析中的高性能与其决策过程不可理解（黑盒）之间的矛盾。本综述只聚焦于**用深度学习做医学图像分析时所采用的 XAI**，意在为弥合这一矛盾提供技术地图与现状梳理。

## 关键贡献

1.  **提出 XAI 分类框架**：基于三组评判标准对深度学习医学图像分析方法分类——**model-based vs. post hoc（模型内 vs. 事后）**、**model-specific vs. model-agnostic（模型特定 vs. 模型无关）**、**global vs. local（全局 vs. 局部，即解释范围 scope）**。该框架改编自 Adadi and Berrada (2018) 与 Murdoch et al. (2019)，见 Section 2、Fig. 1。
2.  **系统性文献综述**：在 SCOPUS 用检索式 "(explainable deep learning OR interpretable deep learning OR XAI OR interpretable machine learning OR explainable machine learning) AND (medical imaging OR medical image analysis)" 检索，结合 ASReview 主动学习工具排序、与同行讨论以及滚雪球（snowballing）方式扩展，纳入截至 **2020 年 10 月** 的同行评审期刊与会议论文（Section 1）。
3.  **双维度归类**：将论文同时按 XAI 技术（视觉/文本/基于示例）和按解剖部位（脑、乳腺、心血管、胸部等）组织，集中呈现在 Table 1、Table 2（Section 3）。
4.  **强调"从计算机视觉到医学"的适配**：XAI 技术多源于计算机视觉，本文专门讨论这些技术如何通过引入医学影像领域知识（如解剖先验、多尺度信息）被改造（Section 1、3）。
5.  **与既有综述互补**：相比 Reyes et al. (2020)（侧重计算机视觉、未充分评估医学适配）和 Huff et al. (2021)（主要举例视觉解释），本文采取更全面（holistic）的视角，纳入非视觉解释、对 XAI 的批判（critiques）以及 XAI 的评估方法；并在 Section 4 讨论各技术优缺点、Section 5 总结现状与机会（Section 1）。

## 方法

本文为综述，其"方法"体现为它提出的分类框架与对现有技术的梳理。

- **三维分类框架**（Section 2, Fig. 1）：
    1.  **Model-based vs. Post hoc（模型内 vs. 事后）**：model-based 指模型本身简单到可被理解、又复杂到能拟合输入-输出关系（如线性回归、SVM；通过 sparsity 稀疏性或 simulatability 可模拟性实现，例 LASSO 强制许多系数为 0）。但深度网络有成千上万到数百万权重，既不稀疏也无法被人内部模拟，故 model-based 在深度学习中不可行；本文聚焦 **post hoc**——先训练网络再分析其学到的关系（如检视学到的特征、特征重要性、特征交互，以及用显著性图做视觉解释）。Murdoch et al. (2019) 提到的 model-based feature engineering（自动构造可解释特征）是一个例外接口。
    2.  **Model-specific vs. Model-agnostic（模型特定 vs. 模型无关）**：model-specific 方法局限于特定模型类别（如利用某类神经网络的特有属性），代价是限制了网络选择；其中一些 post hoc 显著性方法只适用于特定 CNN，但并非 model-based。model-agnostic 方法独立于网络类型，仅通过扰动输入、观察输出变化来解释（因而天然是 post hoc）。注意：model-based 一定 model-specific，但反之不成立。
    3.  **Scope：Global vs. Local（全局 vs. 局部）**：global（数据集级）描述网络在整个数据集上学到的普遍关系（如数据集级特征重要性分数、学到的滤波器可视化）；local 针对单个输入解释其预测（如指向 MRI 上脑肿瘤、解释分类器为何对该样本输出"tumor"的显著性图）。
- **三类解释技术**（Section 3）：
    - **视觉解释 / 显著性映射（Visual / saliency mapping）**：医学图像分析中最常见的 XAI 形式（Fig. 2）。
        - **反向传播类（Backpropagation-based, 3.1.1）**：(Guided) backpropagation（Springenberg et al., 2014）、deconvolution（Zeiler & Fergus, 2014）、partial-derivative 可视化（Simonyan et al., 2013）；**CAM**（Zhou et al., 2016，用全局平均池化替换 CNN 末端全连接层，类激活图为各空间位置视觉模式的加权线性和）；**Grad-CAM**（Selvaraju et al., 2017）；**LRP**（Bach et al., 2015）；**Deep SHAP**（Lundberg & Lee, 2017）；**Trainable attention**（Jetley et al., 2018）。这些通常是 local、model-specific（多数仅对 CNN）、post hoc。
        - **扰动类（Perturbation-based, 3.1.2）**：Occlusion sensitivity（Zeiler & Fergus, 2014）、**LIME**（Ribeiro et al., 2016）、Meaningful perturbation（Fong & Vedaldi, 2017）、Prediction difference analysis（Zintgraf et al., 2017）。这些通常是 model-agnostic、local、post hoc。
        - 另有少数方法基于多示例学习（multiple instance learning）。
    - **文本解释（Textual, 3.2）**：Image captioning（Vinyals et al., 2015）、Image captioning with visual explanation（Zhang et al., 2017a）、**TCAV**（Testing with Concept Activation Vectors，Kim et al., 2018，可做 global 解释）。
    - **基于示例的解释（Example-based, 3.3）**：Triplet networks（Hoffer & Ailon, 2015）、Influence functions（Koh & Liang, 2017）、Prototypes（Chen et al., 2019）。
- **医学特化**：由于医学图像常含多尺度信息，文中提到 multi-scale CAM 等改造（p.4）；并以早期采用者为例说明技术如何落地，如 de Vos et al. (2019) 用 deconvolution 在 CT 切片上定位冠脉钙化的决策来源；Jiang et al. (2019) 用 Inception-V3/ResNet-152/Inception-ResNet-V2 集成、加权组合 CAM 定位糖尿病视网膜病变；Lee et al. (2019b) 用 VGG-16/ResNet-50/Inception-V3/Inception-ResNet-V2 四网络集成的 CAM 检测急性颅内出血。模态覆盖 MRI、CT、X-ray、超声、组织学（Histology）、PET、OCT 等（Table 2）。

## 实验

本文为综述，未做自有实验，而是对现有研究做统计与归类。

- **文献规模与趋势**：Fig. 2 给出医学图像分析中三类 XAI 技术逐年发表论文数，**视觉解释占绝大多数**；2020 年的虚线为基于 2020-10-31 现状的外推。具体逐年论文数 PDF 提取文本未给出数值。
- **技术-框架对照（Table 1）**：将上述各技术按 Section 2 框架打标（model-based / post hoc / model-specific / model-agnostic / global / local）。例如 CAM、Grad-CAM、LRP 均为 post hoc + model-specific + local；LIME、Occlusion sensitivity 为 post hoc + model-agnostic + local；TCAV、Triplet networks 兼具 global 维度；Deep SHAP 因优化方法被标为 post hoc + model-specific（但一般 SHAP 也可 global + model-agnostic）。
- **技术-解剖部位分布（Table 2）**：按解剖部位（Bladder、Brain、Breast、Cardiovascular、Chest 等）列出大量论文的作者、模态与所用主要视觉解释技术。从提取覆盖的部分可见 **CAM/Grad-CAM 是最常用的视觉解释技术**，其次为 Guided backpropagation、LRP、Occlusion sensitivity、Trainable attention、Prediction difference analysis 等。脑部（Brain）以 MRI + CAM/Grad-CAM/LRP 为主，乳腺（Breast）跨 X-ray/MRI/超声/组织学多模态。
- **对比方法 / 评价指标**：作为综述不适用自有对比。值得注意的是，论文在 Section 5 讨论了 **XAI 解释本身的评估方法**（据原文后续页，提取缓存未覆盖，待核）：application-grounded、human-grounded、functionally-grounded 三类评估（与 Doshi-Velez & Kim 的分类一致），其中 application-grounded 用真实任务的人体实验直接测试解释目标，human-grounded 用更简化的人体实验、成本更低，functionally-grounded 不用人体实验、便于自动提取与扩展（线索见原笔记"全文补读记录" p.13-14）。
- **效率/计算成本**：Section 4.4 "Computational cost" 指出 XAI 计算成本在论文中很少被报告；反向传播类视觉解释通常只需一次（前向+反向）传播、成本低，扰动类则需大量扰动、成本高（据原文 p.13，提取缓存未覆盖，待核）。

## 局限

- **检索范围与时间截止**：仅用 SCOPUS 单一数据库、固定关键词检索，截至 2020 年 10 月，可能遗漏其他关键词/数据库的工作以及此后涌现的研究（Section 1）。
- **覆盖技术随快速演进而过时**：XAI 与医学深度学习发展迅速，2020 年后的新方法（如 Transformer/概念瓶颈类解释）不在覆盖范围内。
- **提取缓存仅覆盖前 12 页**：本仓库的 PDF 文本提取缓存只到 p.12（Table 2 的 Chest 部分），Section 4（各技术 pros/cons、计算成本、开源可用性）与 Section 5（讨论、评估方法、展望）的正文未进入缓存。涉及这些部分的结论在本笔记中均标注"据原文后续页，提取缓存未覆盖，待核"，未核证前不应直接引用其细节数字。
- **解释"好坏"的评估仍是难点**：论文虽在 Section 5 引入三类评估范式，但 XAI 解释忠实度（faithfulness）/稳定性/对临床信任与决策流程的真实影响，本身仍缺乏统一、客观的量化标准——这既是该领域的开放问题，也是本综述受限于一手文献而难以盖棺定论之处。

## 个人评论

1.  **框架是最大复用价值**：三维框架（model-based/post hoc × model-specific/model-agnostic × global/local）虽改编自 Adadi & Berrada、Murdoch 等通用 XAI 综述，但配上 Table 1 的逐技术打标，等于给医学影像研究者一张"选型决策表"——想要 model-agnostic 就看 LIME/扰动类，想要 global 就看 TCAV，写相关工作时可直接套用这套坐标系。
2.  **Table 2 是一张"按部位的寻宝图"**：按解剖位置（脑/乳腺/心血管/胸部……）× 模态 × 主要 XAI 技术列出大量一手文献，做特定部位（如脑 MRI）研究时能高效定位同类工作，节省文献调研时间。
3.  **诚实地指出 XAI 的软肋**：相较只罗列方法的综述，本文（Section 4-5）专门谈计算成本很少被报告、开源可用性、以及解释如何评估，提醒读者超越"画热力图"本身去追问解释的质量与可验证性。
4.  **需补读后半部分**：本笔记基于的提取缓存只到 p.12，框架与视觉解释部分扎实，但文本解释/示例解释的细节、各技术优缺点、评估范式与展望均依赖原文 p.13-21；若要严肃引用其评估结论，应回到 PDF 原文核对。

### 使用建议

- **快速了解领域**：读摘要、Introduction、Section 2（框架）+ Fig. 1、Table 1，再到 Section 5（展望）。Fig. 2 给趋势的宏观印象。
- **复现研究**：本文是综述无需复现；应顺着 Table 2 的引用去查具体方法（如 Grad-CAM 在某医学任务）的原始论文。
- **借鉴写作**：撰写"相关工作"时套用其"模型类型 × 解释范围 × 解释形式"的组织逻辑。
- **写相关工作引用**：涉及"医学图像分析可解释性""深度学习可视化""医疗 AI 的信任与问责"时，这是必引的权威综述。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R_综述_Survey]]
> - [[A2_医学图像_分类_配准_生成]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇综述（Survey）论文，发表于 Medical Image Analysis（2022, vol. 79, art. 102470），主题是**基于深度学习的医学图像分析中的可解释人工智能（XAI）**。它系统梳理 XAI 技术在医学影像中的应用现状、提出分类框架并展望未来。其定义性属性是"综述"，故归在 `R_综述_Survey`，因领域聚焦医学影像而辅以 `A2_医学图像_分类_配准_生成`。

## 2. 一句话总结
本文系统综述了深度学习医学图像分析中的 XAI 技术，提出 model-based/post hoc、model-specific/model-agnostic、global/local 三维分类框架，并按该框架与解剖部位归类了视觉、文本和基于示例三类解释方法的医学应用现状（截至 2020 年 10 月）。

## 3. 背景与问题
- **为什么要做**：深度学习是医学图像分析的 state-of-the-art，但神经网络多层非线性交织、无法被人完全理解，是"黑盒"，可能掩盖偏见且后果严重。
- **法规驱动**：GDPR 第 15 条要求患者有权获知决策"如何做出"的有意义信息；DARPA、ACM FAccT 等是 XAI 的代表性推动力。
- **核心矛盾**：医学影像深度学习的高性能 vs. 决策不可理解。论文聚焦"深度学习做医学影像时所用的 XAI"，旨在给出技术地图。术语上 interpretable deep learning 与 XAI 互换，本文统一用 XAI。

## 4. 核心贡献
1.  **XAI 分类框架**：三组标准 model-based vs. post hoc、model-specific vs. model-agnostic、global vs. local，改编自 Adadi & Berrada (2018) 与 Murdoch et al. (2019)（Section 2, Fig. 1）。
2.  **系统性文献综述**：SCOPUS 检索式 + ASReview 主动学习排序 + 同行讨论 + 滚雪球，纳入截至 2020 年 10 月的期刊/会议论文（Section 1）。
3.  **双维度归类**：按 XAI 技术（视觉/文本/示例）与按解剖部位（脑/乳腺/心血管/胸部……）双重组织（Table 1、Table 2）。
4.  **从 CV 到医学的适配**：专门讨论 XAI 技术如何通过引入医学领域知识（解剖先验、多尺度，如 multi-scale CAM）被改造。
5.  **与既有综述互补**：补 Reyes et al. (2020)、Huff et al. (2021) 之不足，纳入非视觉解释、对 XAI 的批判与评估方法（Section 1）；Section 4 谈优缺点、Section 5 谈现状与机会。

## 5. 方法详解
综述的"方法"= 分类框架 + 技术梳理。
- **三维框架**（Section 2, Fig. 1）：
    1.  **Model-based vs. Post hoc**：model-based 靠 sparsity（如 LASSO 强制系数为 0）或 simulatability 让模型本身可懂，但深度网络权重数百万、既不稀疏也不可内部模拟，故不可行；本文聚焦 post hoc——训练后再分析（特征检视、特征重要性、特征交互、显著性图）。例外接口：model-based feature engineering。
    2.  **Model-specific vs. Model-agnostic**：model-specific 局限于特定模型类别（如某类 CNN 的特有属性），代价是限制网络选择；model-agnostic 仅靠扰动输入观察输出，独立于网络类型、天然 post hoc。model-based 必 model-specific，反之不成立。
    3.  **Scope：Global vs. Local**：global（数据集级）给整体关系（数据集级特征重要性、滤波器可视化）；local 针对单一输入（如指向 MRI 脑肿瘤、解释该样本为何被判 "tumor" 的显著性图）。
- **三类技术**（Section 3）：
    - **视觉/显著性（3.1，最常见）**：反向传播类——(Guided) backprop、deconvolution、partial-derivative（Simonyan 2013）、**CAM**（Zhou 2016，GAP 替换全连接层）、**Grad-CAM**（Selvaraju 2017）、**LRP**（Bach 2015）、**Deep SHAP**（Lundberg & Lee 2017）、**Trainable attention**（Jetley 2018）；扰动类——Occlusion sensitivity、**LIME**（Ribeiro 2016）、Meaningful perturbation（Fong & Vedaldi 2017）、Prediction difference analysis（Zintgraf 2017）；另有 multiple instance learning。
    - **文本（3.2）**：Image captioning、Image captioning with visual explanation、**TCAV**（Kim 2018，可 global）。
    - **示例（3.3）**：Triplet networks、Influence functions、Prototypes（Chen 2019）。
- **医学特化实例**：de Vos et al. (2019) 用 deconvolution 在 CT 切片定位冠脉钙化；Jiang et al. (2019) 三网络集成加权 CAM 定位糖尿病视网膜病变；Lee et al. (2019b) 四网络集成 CAM 检测急性颅内出血；multi-scale CAM 应对多尺度医学信息。模态含 MRI/CT/X-ray/超声/组织学/PET/OCT。

## 6. 实验与结果
综述无自有实验，以统计与归类替代。
- **趋势（Fig. 2）**：三类 XAI 逐年发表数，视觉解释占绝大多数；2020 年为基于 2020-10-31 的外推（虚线）。具体年度数值 PDF 提取文本未给。
- **技术-框架对照（Table 1）**：CAM/Grad-CAM/LRP = post hoc + model-specific + local；LIME/Occlusion = post hoc + model-agnostic + local；TCAV/Triplet 含 global；Deep SHAP 因优化方法被标 post hoc + model-specific（一般 SHAP 也可 global + model-agnostic）。
- **技术-部位分布（Table 2）**：按 Bladder/Brain/Breast/Cardiovascular/Chest 等列作者、模态、主要视觉技术。提取覆盖部分显示 **CAM/Grad-CAM 最常用**，其后为 Guided backprop、LRP、Occlusion sensitivity、Trainable attention、Prediction difference analysis。
- **评估方法与计算成本**（据原文后续页 p.13-14，提取缓存未覆盖，待核）：Section 5 引入 application-grounded / human-grounded / functionally-grounded 三类评估；Section 4.4 指出计算成本很少被报告，反向传播类成本低、扰动类成本高（线索见原笔记"全文补读记录"）。
- **消融/泛化**：综述不含此类自有实验。

## 7. 这篇论文真正有价值的地方
1.  **可操作的选型框架**：三维框架 + Table 1 的逐技术打标，等于一张"想要某种解释属性该选哪个方法"的决策表。
2.  **领域适配视角**：不止介绍通用 XAI，还专门讲 CV 技术如何加入医学领域知识（解剖先验、多尺度），并给早期采用者实例。
3.  **按部位的文献地图（Table 2）**：解剖位置 × 模态 × 技术，便于特定部位研究快速定位同类工作。
4.  **直面 XAI 软肋**：谈计算成本少被报告、开源可用性、解释如何评估，推动读者思考解释的质量与可验证性而非止于热力图。

## 8. 局限与问题
- **检索范围**：单一 SCOPUS、固定关键词、截至 2020 年 10 月，可能遗漏其他来源与此后工作（Section 1）。
- **时效性**：2020 年后新方法（如 Transformer/概念瓶颈类解释）未覆盖。
- **本仓库提取缓存只到 p.12**：Section 4（pros/cons、计算成本、开源）与 Section 5（评估、展望）正文未入缓存，相关结论已标"据原文后续页，提取缓存未覆盖，待核"。
- **解释评估仍无金标准**：忠实度/稳定性/对临床信任与决策流程的真实影响缺乏统一量化标准，是开放问题。

## 9. 我该怎么使用这篇论文
- **快速了解领域**：摘要 + Introduction + Section 2（框架）+ Fig. 1 + Table 1 + Section 5（展望）；Fig. 2 看趋势。
- **复现研究**：本文是综述无需复现；顺 Table 2 引用查具体方法的原始论文（如 Grad-CAM 在某医学任务）。
- **借鉴写作**：套用其"模型类型 × 解释范围 × 解释形式"的组织逻辑写相关工作。
- **写相关工作引用**：涉及"医学图像分析可解释性""深度学习可视化""医疗 AI 的信任与问责"必引。

## 10. 和其他论文的关系
- 框架改编自通用 XAI 综述 Adadi and Berrada (2018) 与 Murdoch et al. (2019)，可与之互补阅读。
- 明确定位为对 Reyes et al. (2020)（偏 CV、未充分评估医学适配）与 Huff et al. (2021)（主要举例视觉解释）的补充与扩展，强调非视觉解释、批判与评估。
- 对做具体医学影像任务（脑肿瘤、乳腺癌分类等）的研究者，可经 Table 2 快速定位相关 XAI 工作。
- 主题上与 `R_综述_Survey` 下其他综述、以及 `A2_医学图像_分类_配准_生成` 下的医学影像方法论文相关；因 PDF 提取未含完整参考文献，未建立确定的 `[[双链]]`。

## 11. 关键词
可解释人工智能（XAI）, 可解释深度学习, 医学图像分析, 综述, 分类框架, model-based/post hoc, model-specific/model-agnostic, global/local, 显著性图, 类激活映射（CAM/Grad-CAM）, LRP, LIME, TCAV, 视觉/文本/示例解释, 高风险决策, GDPR

## 12. 可信度说明
本精读基于本仓库 PDF 提取缓存（覆盖 p.1-12：摘要、Introduction、Section 2 完整框架、Section 3 开头与视觉解释反向传播部分、Table 1 全表、Table 2 至 Chest 部分）。这些部分对论文动机、三维框架、视觉解释技术清单及技术-部位分布的呈现清晰可靠。涉及 Section 3.2/3.3 细节、Section 4（各技术优缺点、计算成本、开源可用性）、Section 5（讨论、application/human/functionally-grounded 三类评估、展望）的内容，提取缓存未覆盖，凡引用之处均标注"据原文后续页，提取缓存未覆盖，待核"，并以原笔记"全文补读记录"中的页面线索为辅助提示，未经 PDF 原文核对前不应直接当作定论引用。提取质量在已覆盖页面较好。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/Explainable-artificial-intelligence--XAI--in-deep-learni_2022_Medical-Image-.txt` (提取缓存覆盖 p.1-12/21; 原 AI 主体声称 12/21 + 全文补读 13-21 据页面线索); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-21; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-21。
- **提取情况**: 缺失页 9 页, 其中 9 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 4.4. Computational cost
- p.13: Computational cost of XAI is seldom reported in papers, but can
- p.13: Since model-based techniques embed the explanation in the
- p.13: For visual explanation techniques, there is a clear dis-
- p.13: Backpropagation-based techniques typically make a single
- p.13: Perturbation-based techniques require, however, extensive per-
- p.13: The computational costs of the post hoc textual explanation
- p.13: For visual explanation, most backpropagation techniques have a
- p.13: Perturbation-based visual explanation techniques often require
- p.13: 4.6. Open-source availability
- p.13: 5. Discussion
- p.13: 5.1. Overview

### 缺失页关键摘录

- p.13: was provided per case (e.g. per patient), rather than on a dataset-
- p.13: age analysis, such as accuracy, Dice coeﬃcient, or an ROC anal-
- p.13: uation of explainability, consisting of three evaluation methods:
- p.13: application-grounded evaluation, human-grounded evaluation, and
- p.13: Application-grounded evaluation uses human experiments
- p.13: application-grounded evaluation is that it directly tests the objec-
- p.13: Human-grounded evaluation uses simpler human experiments
- p.14: evaluation is that it is less costly, while still receiving general no-
- p.14: Functionally-grounded evaluation does not use human experi-
- p.14: gist. The advantages of functionally-grounded evaluation stated by
- p.14: evaluation of explanations are easily extracted, and can be auto-
- p.14: 5.2.4. Evaluation of XAI in medical image analysis
<!-- AI_READING_NOTE_END -->
