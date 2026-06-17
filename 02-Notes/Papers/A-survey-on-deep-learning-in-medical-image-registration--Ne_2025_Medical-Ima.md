---
title: "A survey on deep learning in medical image registration: New technologies, uncertainty, evaluation metrics, and beyond"
authors:
  - "Junyu Chen"
  - "Yihao Liu"
  - "Shuwen Wei"
  - "Zhangxing Bian"
  - "Shalini Subramanian"
  - "Aaron Carass"
  - "Jerry L. Prince"
  - "Yong Du"
year: 2025
venue: Medical Image Analysis 100 (2025) 103385
doi: 10.1016/j.media.2024.103385
pdf: [[A-survey-on-deep-learning-in-medical-image-registration--Ne_2025_Medical-Ima.pdf]]
primary_topic: A2_医学图像_分类_配准_生成
topics:
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
extract_cache: .paper-cache/extracts/A-survey-on-deep-learning-in-medical-image-registration--Ne_2025_Medical-Ima.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/43 pages"
---
# A survey on deep learning in medical image registration

## 基本信息
- **PDF**: [[A-survey-on-deep-learning-in-medical-image-registration--Ne_2025_Medical-Ima.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A survey on deep learning in medical image registration: New technologies, uncertainty, evaluation metrics, and beyond |
| **作者** | Junyu Chen; Yihao Liu; Shuwen Wei; Zhangxing Bian; Shalini Subramanian; Aaron Carass; Jerry L. Prince; Yong Du (Johns Hopkins School of Medicine / Johns Hopkins University, MD, USA) |
| **发表时间** | 2025 (在线 2024-11-10; 收稿 2023-09-12, 修回 2024-10-27, 录用 2024-11-01) |
| **刊物/会议** | Medical Image Analysis 100 (2025) 103385 |
| **DOI** | 10.1016/j.media.2024.103385 |

## 摘要

> 来源: 据 PDF 提取文本整理。

**英文原摘要（已清理空格与连字符）**:

Deep learning technologies have dramatically reshaped the field of medical image registration over the past decade. The initial developments, such as regression-based and U-Net-based networks, established the foundation for deep learning in image registration. Subsequent progress has been made in various aspects of deep learning-based registration, including similarity measures, deformation regularizations, network architectures, and uncertainty estimation. These advancements have not only enriched the field of image registration but have also facilitated its application in a wide range of tasks, including atlas construction, multi-atlas segmentation, motion estimation, and 2D–3D registration. In this paper, we present a comprehensive overview of the most recent advancements in deep learning-based image registration. We begin with a concise introduction to the core concepts of deep learning-based image registration. Then, we delve into innovative network architectures, loss functions specific to registration, and methods for estimating registration uncertainty. Additionally, this paper explores appropriate evaluation metrics for assessing the performance of deep learning models in registration tasks. Finally, we highlight the practical applications of these novel techniques in medical imaging and discuss the future prospects of deep learning-based image registration.

**中文翻译**:

过去十年中，深度学习技术彻底重塑了医学图像配准领域。早期工作（如基于回归的网络与基于 U-Net 的网络）为图像配准的深度学习奠定了基础。此后，基于深度学习的配准在多个方面取得进展，包括相似性度量、形变正则化、网络架构与不确定性估计。这些进展不仅丰富了图像配准领域，还推动了其在多种任务中的应用，包括图谱构建（atlas construction）、多图谱分割（multi-atlas segmentation）、运动估计（motion estimation）以及 2D–3D 配准。本文对基于深度学习的图像配准的最新进展进行全面综述：先简要介绍核心概念，再深入探讨创新网络架构、配准专用的损失函数，以及估计配准不确定性的方法；此外探讨用于评估深度学习配准模型性能的恰当评价指标；最后强调这些新技术在医学影像中的实际应用，并讨论其未来前景。

## 研究背景与动机

*   **为什么要做**：深度学习在过去十年极大重塑了医学图像配准领域，新技术不断涌现（图 1 显示，本综述调研的 **250 余篇** 文章绝大多数发表于近五年）。已有的若干学习型配准综述（Fu et al. 2020a；Chen et al. 2021d；Xiao et al. 2021；Zou et al. 2022）受领域快速发展所限，可能未能完全跟进最新进展，因此需要一篇及时、全面的综述。
*   **配准任务定义**：图像配准的目标是估计最优空间变换，将一对固定图像（fixed）与运动图像（moving）中的感兴趣结构对齐。变换分两类：刚性/仿射（rigid/affine，所有坐标用同一变换矩阵），以及非刚性/可形变（non-rigid/deformable，对各局部区域用独立变换）。刚性配准用于刚体假设成立的场景（如将结构像 MRI/CT 与功能像 fMRI/PET 对齐做衰减校正或功能解读）；可形变配准（DIR）用于需要复杂、空间变化形变的场景（如构建可形变模板、将图谱配准到病人图像做多图谱分割）。
*   **之前方法（传统配准）的问题**：传统方法通过迭代求解优化问题完成配准（如 demons、LDDMM、SyN、DARTEL、Elastix），理论成熟但有两大局限：(1) **计算量大、速度慢**——每一对运动/固定图像都要独立求解一次优化，跨图像对存在大量冗余；(2) 关于变换参数（位移场或控制点）的目标函数通常**非线性**，构成**非凸优化困境**。已有的改进（目标函数线性化、凸化、离散化配准）往往以增加计算成本、或使问题失真为代价。
*   **核心矛盾与深度学习的三重优势**：深度学习通过在训练集上优化全局目标函数来训练通用网络，测试时固定权重对每个图像对直接前向推理。其相对传统方法的三重优势是：(1) 训练数据多样性充当**隐式正则化**，平滑损失面、抑制误导性梯度导致的次优局部极小；(2) 非凸优化对初值敏感，**预训练权重（迁移学习）+ 先进优化算法**提升了定位全局极小的能力；(3) 单次前向推理避免迭代优化，带来显著**速度优势**。本文同时要应对深度学习自身在模型设计、不确定性量化与评估上的新挑战。

## 关键贡献

依据提取文本（标题、摘要、完整目录与引言），本综述的核心贡献为：
1.  **系统性综述最新进展**：全面梳理基于深度学习的医学图像配准最新技术，涵盖创新网络架构、配准专用损失函数（相似性度量、形变正则化）以及不确定性估计方法。
2.  **形式化定义配准不确定性**：在学习型配准语境下正式探讨并定义不确定性，区分**偶然不确定性（aleatoric，§5.2.1）**与**认知不确定性（epistemic，§5.2.2）**，并讨论 Bayesian 深度学习与不确定性评估方法（§5）。
3.  **厘清被忽视的评估指标**：系统梳理评估学习型配准的恰当指标，分为**精度度量（accuracy measures，§6.1）**与**正则性度量（regularity measures，§6.2）**；作者指出这部分在以往综述中常被忽视。
4.  **关联实际应用**：探讨新技术在多种医学影像任务中的应用——图谱构建、多图谱分割、运动估计、2D-3D 配准（§8）。
5.  **指明挑战与未来方向**：总结当前挑战并展望前景（§9），含网络架构、损失函数、配准不确定性，以及两个新兴方向——**零样本配准（zero-shot registration）**与**变形/质变配准（metamorphic image registration，含时空配准、空间标准化）**。
6.  **整理开源代码索引**：将所综述论文的开源代码汇总成一份清单，公开于 `https://bit.ly/3QgFJ9z`。

## 方法

本文是**综述论文**，其"方法"在于对领域内已有工作的系统分类、梳理与评述，而非提出新框架。组织架构与关键内容（据完整目录）：

*   **整体框架（§2 基础 → §3 损失函数 → §4 网络架构 → §5 不确定性 → §6 评估指标 → §7 数据集 → §8 应用 → §9 挑战展望 → §10 结论）**：
    *   **§2 学习型配准基础**：监督 vs. 无监督（§2.1）、学习型配准范式（§2.2）、微分同胚配准（diffeomorphic，§2.3）。
    *   **§3 损失函数**（对应传统方法的目标函数）：监督学习损失（§3.1）、无监督与半监督学习（§3.2）、相似性度量（§3.3）、形变正则化器（§3.4）、辅助解剖信息（§3.5）。
    *   **§4 网络架构**（近年最活跃方向，共 10 个子类）：对抗学习（4.1）、对比学习（4.2）、Transformers（4.3）、扩散模型（4.4）、Neural ODEs（4.5）、隐式神经表示 INR（4.6）、超参数条件化（4.7）、解剖感知网络（4.8）、相关性层（4.9）、渐进式与金字塔配准（4.10）。
    *   **§5 配准不确定性**：Bayesian 深度学习（5.1）、DNN 配准不确定性估计（5.2，含 aleatoric 5.2.1 / epistemic 5.2.2）、不确定性评估（5.3）。
    *   **§6 评估指标**：精度度量（6.1）、正则性度量（6.2）。
    *   **§7-9**：公共基准数据集、应用、挑战与展望。
*   **配准的能量函数形式（式 1）**：`φ̂ = argmin_φ E(I_f, I_m∘φ) + λR(φ)`。其中 `I_f`、`I_m` 为固定/运动图像，`φ` 是把 `I_m` 映射到 `I_f` 的形变场，`R` 是关于 `φ` 的正则化泛函，`λ` 是权衡图像相似度与形变场正则性的超参数。第一项度量固定图像与变换后运动图像的相似度（差异），第二项对形变场施加正则（如空间平滑），用于 DIR 防止形变场出现"折叠"或体素重排等物理上不合理的行为（Rohlfing 2011）。
*   **输入输出**：学习型配准网络输入一对待配准图像（`I_f`、`I_m`）。无监督学习直接输出形变场 `φ`；监督学习输出与真值变换对齐的预测（刚性/仿射任务的真值通常是变换矩阵，可形变任务的真值是密集位移场）。
*   **架构演进（据引言）**：最初多为**编码器型网络**——或作特征提取器替代手工特征（Wu et al. 2013），或作回归器从局部图像块估计变换参数（Miao et al. 2016）。U-Net（Ronneberger et al. 2015）成功后，可形变配准开始采用**编码器-解码器架构**做监督学习（常需真值形变场）；**空间变换网络 STN**（Jaderberg et al. 2015）的出现推动了**无监督、端到端**的可形变配准，并已成为主流。刚性/仿射配准则继续采用仅编码器网络，输出刚性或仿射参数。
*   **训练范式**：分为**监督学习**（需真值形变场或变换矩阵作标签）与**无监督/半监督学习**（仅用图像对，通过可微的图像相似性度量作损失端到端训练）。无监督范式现已成为主导。
*   **推理流程**：固定训练好的权重，对新图像对单次前向传播即得形变场/变换参数，与传统方法的迭代优化形成鲜明对比。
*   **与传统方法的根本差异**：将"逐图像对优化"转化为"对全局数据集的学习"，由此获得快速推理、数据驱动的隐式正则化、以及预训练带来的优化鲁棒性。

## 实验

作为综述论文，本文不含作者独立实验，而是系统整理、对比、分析所综述 250 余篇论文中的实验。
*   **文献来源（图 1）**：左图为各年度论文数直方图，绝大多数集中在近五年；检索覆盖 Medical Image Analysis、IEEE TMI、Medical Physics、NeuroImage 等期刊，以及 MICCAI、IPMI、WBIR、CVPR、ECCV、ICCV、NeurIPS 等会议。
*   **基准数据集**：§7 专门枚举医学图像配准常用的公共基准数据集。**具体数据集清单在提取缓存（仅覆盖 p.1-12）中未涵盖**，需查阅原文 §7（p.23-25）。
*   **对比方法、指标与主结果**：本文不集中给出统一实验表，而在讨论各类方法时引用其原始论文的实验。原笔记记录的部分后续页线索（提取缓存未覆盖，待核）显示：Transformer 类方法报告在多个基准上 Dice 等指标提升（据原文后续页）；INR 类方法在 DIR-LAB 数据集上取得有前景结果（据原文后续页）；扩散类方法在公开 Cardiac MRI 数据集等上对比 ConvNet 方法（据原文后续页）。
*   **评价指标口径（§6）**：精度度量（如 Dice 等，§6.1）与形变场正则性度量（如折叠体素比例 / 雅可比行列式相关量，§6.2）——后者用于量化生成形变场的物理合理性，是本文强调的被忽视维度。
*   **效率信息**：引言明确强调深度学习在**推理速度**上的优势（单次前向 vs. 迭代优化）；具体 FLOPs/参数量等数字需查原始论文。

## 局限

1.  **覆盖面与时效性**：领域发展极快，综述发表时可能已遗漏最新（2024 年后期及之后）的突破。作者自身也指出已有学习型配准综述"may not be fully up-to-date"，本文同样受此约束。
2.  **深度与广度的权衡**：覆盖 250 余篇文章的广域综述，对每项具体技术的细节剖析必然受限；需复现某项技术仍要精读其原始论文（论文提供了开源代码索引以缓解此问题）。
3.  **实验分析的间接性**：本文价值在"整理"而非"实证"，所有实验结论依赖所引论文，可靠性取决于原始研究质量；本综述未做统一再评测。
4.  **预测的不确定性**：§9 对未来方向（如零样本配准、变形配准）的展望是基于当前趋势的推断，准确性有待时间验证。
5.  **本笔记的核查局限**：本仓库提取缓存仅覆盖 p.1-12（标题、摘要、完整目录、引言、§2 开头）。§3-§9 的技术细节（损失函数公式、各架构具体方法与数值、不确定性定义细节、数据集清单）在提取文本中**未直接给出**，本笔记中相关内容据目录、引言概述与原笔记后续页线索整理，标注"待核"，请以完整论文为准。

## 个人评论

1.  **领域全景地图**：作为来自 Johns Hopkins（VoxelMorph/TransMorph 等工作的同一脉络团队）的综述，它为初学者提供一幅可信的"全景地图"，快速理清深度学习配准的技术脉络、流派与演进，省去盲读零散论文的低效。
2.  **清晰且细粒度的分类框架**：§4 把网络架构拆成 10 个子类（对抗、对比、Transformer、扩散、Neural ODEs、INR、超参条件化、解剖感知、相关性层、渐进/金字塔），是本文最实用的资产，便于按技术方向快速定位与对照设计动机。
3.  **强调被忽视的维度**：把"不确定性估计"（区分 aleatoric/epistemic）与"评估指标"（精度 + 正则性）提到与架构同等地位，直指以往综述薄弱环节——尤其形变场正则性（折叠率/雅可比）对严谨评测至关重要。
4.  **理论与应用打通**：§8 专列图谱构建、多图谱分割、运动估计、2D-3D 配准等临床任务，使技术落地有迹可循。
5.  **明确的研究选题指引**：§9 的零样本配准与变形（metamorphic）配准是值得关注的前沿方向；附带的开源代码索引（bit.ly/3QgFJ9z）让本文兼具综述与"工具入口"双重价值。
6.  **可改进处**：受提取限制，本笔记未能逐一核对 §3-§9 的方法与数值；若要在本库内建立细粒度双链，建议据 §4 的 10 类架构去匹配库内具体方法论文。

### 使用建议

*   **快速了解领域**：读摘要、§1 引言（背景与全文结构）、§9 挑战与展望即可把握主脉络。
*   **复现具体技术**：本文不能直接复现；据其对某类方法的描述与引用找到原始论文及代码（开源索引见 bit.ly/3QgFJ9z）。
*   **借鉴创新点**：精读 §4 网络架构与 §3 损失函数，了解最前沿模块设计思路。
*   **撰写 Related Work**：本文是"医学图像配准"综述的优秀模板与索引，可参考其结构组织文献，并用其分类/引用快速定位相关工作。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇**综述论文**（Medical Image Analysis 2025，Johns Hopkins 团队），聚焦**深度学习在医学图像配准的最新进展**。它系统梳理近年（尤其近五年、250 余篇）该领域的新技术：网络架构、损失函数、不确定性估计与评估指标，并讨论应用与未来方向。核心问题是全面总结深度学习如何重塑医学图像配准，并填补以往综述在不确定性与评估指标上的缺口。归类于"医学图像配准 / 综述"主题（库内对应 `A2_医学图像_分类_配准_生成`）。

## 2. 一句话总结
本文全面综述了基于深度学习的医学图像配准最新进展，涵盖网络架构（10 类）、配准专用损失函数、不确定性估计（aleatoric/epistemic）与评估指标（精度/正则性），并梳理数据集、应用与未来方向。

## 3. 背景与问题
*   **为什么要做**：深度学习近十年极大重塑医学图像配准，新技术井喷（图 1：250 余篇多在近五年），已有综述受领域快速发展所限可能滞后，需一篇及时全面的综述。
*   **任务定义**：估计最优空间变换以对齐固定图像与运动图像；分刚性/仿射（同一矩阵）与非刚性/可形变（局部独立变换）。
*   **传统方法的问题**：迭代优化（demons、LDDMM、SyN、DARTEL、Elastix）理论成熟但 (1) 计算量大、速度慢（逐图像对独立求解、冗余）；(2) 目标函数非凸、对初值敏感。线性化/凸化/离散化等改进常增加成本或使问题失真。
*   **深度学习三重优势**：在训练集上学全局目标、测试时固定权重直接前向——(1) 数据多样性作隐式正则、平滑损失面；(2) 预训练 + 先进优化提升定位全局极小的能力；(3) 单次前向带来速度优势。

## 4. 核心贡献
1.  系统综述学习型配准最新技术（架构、损失、不确定性）。
2.  正式定义配准不确定性，区分偶然（aleatoric）与认知（epistemic），并讨论 Bayesian 深度学习与不确定性评估。
3.  厘清评估指标——精度度量与形变场正则性度量，补足以往综述忽视的维度。
4.  关联实际应用：图谱构建、多图谱分割、运动估计、2D-3D 配准。
5.  总结挑战与未来方向：网络架构、损失函数、配准不确定性、零样本配准、变形（metamorphic）配准。
6.  整理开源代码索引（bit.ly/3QgFJ9z）。

## 5. 方法详解
本文是综述，"方法"即对已有工作的系统分类与评述。组织：§2 基础（监督/无监督、范式、微分同胚）→ §3 损失（监督、无监督/半监督、相似性度量、形变正则、辅助解剖信息）→ §4 架构（对抗、对比、Transformer、扩散、Neural ODEs、INR、超参条件化、解剖感知、相关性层、渐进/金字塔，共 10 类）→ §5 不确定性（Bayesian、aleatoric/epistemic、评估）→ §6 指标（精度、正则性）→ §7 数据集 → §8 应用 → §9 挑战展望 → §10 结论。

配准能量函数（式 1）：`φ̂ = argmin_φ E(I_f, I_m∘φ) + λR(φ)`，第一项度量图像相似度，第二项正则化形变场（如空间平滑，防止折叠/体素重排），`λ` 权衡两者。

架构演进：编码器型（特征提取器 Wu 2013 / 参数回归器 Miao 2016）→ U-Net 编码器-解码器（监督，需真值形变场）→ STN（Jaderberg 2015）推动无监督端到端可形变配准（现为主流）；刚性/仿射仍用仅编码器网络输出变换参数。训练分监督（真值形变场/变换矩阵）与无监督/半监督（仅图像对 + 可微相似度损失）。推理：固定权重单次前向得形变场/参数。

## 6. 实验与结果
综述本身无独立实验，整理所引 250 余篇论文的实验。图 1 给出文献年度分布与来源（期刊 MedIA/TMI/Medical Physics/NeuroImage，会议 MICCAI/IPMI/WBIR/CVPR/ECCV/ICCV/NeurIPS）。§7 列公共基准数据集（具体清单提取缓存未覆盖，待核）。§6 评估口径：精度度量（Dice 等）+ 形变场正则性度量（折叠/雅可比相关）。效率方面引言强调推理速度优势（单次前向 vs. 迭代）。各架构的具体数值（如 Transformer 的 Dice 提升、INR 在 DIR-LAB 的结果、扩散在 Cardiac MRI 的对比）据原文后续页、提取缓存未覆盖，待核。

## 7. 这篇论文真正有价值的地方
1.  领域全景地图：快速理清深度学习配准的技术脉络、流派与演进。
2.  细粒度分类框架：§4 的 10 类架构便于按方向定位与理解设计动机。
3.  强调被忽视维度：把不确定性（aleatoric/epistemic）与评估指标（精度/正则性）提到与架构同等地位。
4.  打通理论与应用：§8 专列临床任务（图谱、多图谱分割、运动估计、2D-3D）。
5.  研究选题指引 + 工具入口：§9 前沿方向 + 开源代码索引。

## 8. 局限与问题
1.  时效性：领域快，发表时可能已遗漏最新突破（作者亦点出已有综述易滞后）。
2.  广度-深度权衡：覆盖面广导致单项技术细节有限，复现需读原文。
3.  间接性：结论依赖所引论文质量，无统一再评测。
4.  预测不确定：§9 展望基于趋势推断，待时间验证。
5.  本笔记核查局限：提取缓存仅 p.1-12，§3-§9 细节据目录/引言/原笔记线索整理并标"待核"。

## 9. 我该怎么使用这篇论文
*   快速了解领域：摘要 + §1 + §9。
*   复现具体技术：经本文索引找原始论文与代码（bit.ly/3QgFJ9z）。
*   借鉴创新点：精读 §4 架构与 §3 损失。
*   写 Related Work：以本文结构为模板、其分类/引用为索引。

## 10. 和其他论文的关系
*   依主题 `A2_医学图像_分类_配准_生成`，本文是"配准"方向的顶级综述。
*   与库中具体介绍某类配准技术（如基于 Transformer、扩散模型、INR 的配准）的论文构成 **"总-分"** 关系：本文总括，其余分述。
*   建议据本文 §4 的 10 类架构在库内匹配对应细分论文建立 `[[双链]]`。

## 11. 关键词
深度学习；医学图像配准；可形变图像配准（DIR）；网络架构（Transformer/扩散/Neural ODEs/INR）；损失函数；相似性度量；形变正则化；不确定性估计（aleatoric/epistemic）；评估指标（精度/正则性）；无监督学习；空间变换网络 STN；微分同胚配准；零样本配准

## 12. 可信度说明
本精读基于提取缓存 **p.1-12**（标题、作者、摘要、**完整目录**、§1 引言全文、§2 开头）。这部分提取质量好、文本连贯，**背景/动机、贡献、组织架构、能量函数、架构演进**等可直接据原文核实。涉及 **§3-§9** 的技术细节（损失函数具体公式、各架构方法与数值、不确定性定义细节、数据集清单）在提取文本中未直接出现，主要据**目录标题、引言概述及原笔记后续页线索**整理，已逐处标注"待核 / 据原文后续页"。需技术细节者请参考完整 43 页论文。

---

> **可信度补充**: PDF 提取质量 = **high** (提取缓存 p.1-12 连贯, ~2086 字符/页); 提取缓存覆盖 12/43 页 (标题/摘要/完整目录/§1/§2 开头), §3-§9 正文未覆盖, 相关内容据目录与引言整理并标"待核"; 来源缓存: `.paper-cache/extracts/A-survey-on-deep-learning-in-medical-image-registration--Ne_2025_Medical-Ima.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-43; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-43。
- **提取情况**: 缺失页 31 页, 其中 31 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 4.2. Contrastive learning
- p.13: The principle of contrastive learning enables DNNs to learn by
- p.13: For a comprehensive understanding of this concept and a detailed
- p.13: Siamese network to minimize the contrastive loss, which minimized the
- p.13: Their method used two independent U-Nets to learn the represen-
- p.13: This method demonstrated promising results in multi-modal brain MRI
- p.13: Until now, the methods based on contrastive learning have been
- p.13: However, it is important to note that the positive pair used in these two
- p.13: 4.3. Transformers
- p.13: One of the key factors in designing ConvNets is the size of the
- p.14: In contrast, Transformers are widely acknowledged for their superior
- p.14: For a comprehensive review of the current Transformer-based models

### 缺失页关键摘录

- p.14: on several benchmark datasets and demonstrated superior performance
- p.15: shows enhanced registration accuracy in terms of Dice coefficients and
- p.15: As a result, inference with these models, which requires the reverse
- p.16: a result, there is no need for time-consuming reverse diffusion steps
- p.16: ConvNet-based methods on a publicly available Cardiac MRI dataset
- p.16: and a human facial expression dataset. However, since their forward
- p.16: function. As a result, INRs provide a more compact representation
- p.17: proposed model showed promising results on the DIR-LAB dataset, sur-
- p.17: this dataset. Building on this foundation, Byra et al.(2023 ) further
- p.17: much like traditional approaches, suffer from a common limitation:
- p.17: from a larger dataset. As a result, these methods are unable to take
- p.17: dataset. In a parallel work, Mok and Chung (2021b ) proposed condi-
<!-- AI_READING_NOTE_END -->
