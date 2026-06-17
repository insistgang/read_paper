---
title: "Deep learning based synthesis of MRI, CT and PET: Review and analysis"
authors:
  - "Sanuwani Dayarathna"
  - "Kh Tohidul Islam"
  - "Sergio Uribe"
  - "Guang Yang"
  - "Munawar Hayat"
  - "Zhaolin Chen"
year: 2024
venue: "Medical Image Analysis 92 (2024) 103046"
doi: 10.1016/j.media.2023.103046
pdf: [[Deep-learning-based-synthesis-of-MRI--CT-and-PET--Revi_2024_Medical-Image-An.pdf]]
primary_topic: A2_医学图像_分类_配准_生成
topics:
  - "A2_医学图像_分类_配准_生成"
  - "R_综述_Survey"
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
extract_cache: .paper-cache/extracts/Deep-learning-based-synthesis-of-MRI--CT-and-PET--Revi_2024_Medical-Image-An.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/32 pages"
---
# Deep learning based synthesis of MRI, CT and PET: Review and analysis

## 基本信息
- **PDF**: [[Deep-learning-based-synthesis-of-MRI--CT-and-PET--Revi_2024_Medical-Image-An.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`, `R_综述_Survey`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Deep learning based synthesis of MRI, CT and PET: Review and analysis (Survey paper) |
| **作者** | Sanuwani Dayarathna; Kh Tohidul Islam; Sergio Uribe; Guang Yang; Munawar Hayat; Zhaolin Chen (Monash University; Imperial College London) |
| **发表时间** | 2024 (Received 5 Jun 2023; Accepted 29 Nov 2023; Online 1 Dec 2023) |
| **刊物/会议** | Medical Image Analysis, 92 (2024) 103046 (Elsevier, 开放获取 CC BY) |
| **DOI** | 10.1016/j.media.2023.103046 |

## 摘要

> **清理后英文原摘要**（据 PDF 提取文本修复空格/连字符）：
>
> Medical image synthesis represents a critical area of research in clinical decision-making, aiming to overcome the challenges associated with acquiring multiple image modalities for an accurate clinical workflow. This approach proves beneficial in estimating an image of a desired modality from a given source modality among the most common medical imaging contrasts, such as Computed Tomography (CT), Magnetic Resonance Imaging (MRI), and Positron Emission Tomography (PET). However, translating between two image modalities presents difficulties due to the complex and non-linear domain mappings. Deep learning-based generative modelling has exhibited superior performance in synthetic image contrast applications compared to conventional image synthesis methods. This survey comprehensively reviews deep learning-based medical imaging translation from 2018 to 2023 on pseudo-CT, synthetic MR, and synthetic PET. We provide an overview of synthetic contrasts in medical imaging and the most frequently employed deep learning networks for medical image synthesis. Additionally, we conduct a detailed analysis of each synthesis method, focusing on their diverse model designs based on input domains and network architectures. We also analyse novel network architectures, ranging from conventional CNNs to the recent Transformer and Diffusion models. This analysis includes comparing loss functions, available datasets and anatomical regions, and image quality assessments and performance in other downstream tasks. Finally, we discuss the challenges and identify solutions within the literature, suggesting possible future directions. We hope that the insights offered in this survey paper will serve as a valuable roadmap for researchers in the field of medical image synthesis.
>
> **中文翻译**：
>
> 医学图像合成是临床决策中的一个关键研究领域，目标是克服为了准确的临床工作流而需获取多种成像模态所带来的困难。该方法的价值在于：在 CT、MRI、PET 等最常用的医学成像对比之间，从一个给定的源模态估计出所需目标模态的图像。然而，由于模态间映射复杂且非线性，两个图像模态之间的转换并不容易。相比传统图像合成方法，基于深度学习的生成式建模在合成图像对比的应用中表现出更优的性能。本综述全面回顾了 2018 至 2023 年间基于深度学习的医学图像转换工作，涵盖伪 CT、合成 MR 和合成 PET。我们概述了医学成像中的各类合成对比及最常用的深度学习网络；进一步对每种合成方法进行详细分析，聚焦其基于输入域和网络架构的多样化模型设计；还分析了从传统 CNN 到近期 Transformer 与 Diffusion 模型的新型网络架构。分析内容包括损失函数、可用数据集与解剖区域、图像质量评估以及在其他下游任务中的表现。最后，我们讨论了相关挑战、归纳了文献中给出的解决方案，并指出可能的未来方向。希望本综述能为医学图像合成领域的研究者提供一份有价值的路线图。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

*   **为什么做：** MRI、CT、PET 各自提供独特的结构、功能与代谢信息，对临床诊断与治疗监测都很关键。但获取完整多模态图像存在三类现实障碍：① **辐射风险**（PET、CT 对儿童患者尤甚）；② **成本高 + 扫描时间长**，且长扫描时间会引入伪影；③ 某些场景下安全获取精确成像本身困难（如仅用 MRI 做放疗计划，即 MRI-only radiation therapy treatment planning）。医学图像合成通过"从源模态映射到目标模态"来缓解这些问题，可最大化已采集图像的利用率、缩短扫描时间、降低运营成本（如放射性示踪剂费用）。典型应用包括 MRI-only 放疗计划、PET/MRI 扫描、图像分割与超分辨率。
*   **之前方法的问题：** 早期的传统方法高度依赖由训练有素的专业人员**手工选择的特征**（handcrafted features），表征复杂图像细节的能力有限，会损害合成任务的性能，导致**可靠性与泛化性受限**。
*   **核心矛盾：** 模态间映射具有**高维、非线性、病态（ill-posed）**的特性（Nie et al., 2018），需要能自动学习复杂非线性关系的方法。深度学习（尤其生成式建模）已被证明能准确建模跨模态的域特性，并支持迁移知识（用一个任务的知识以最小改动提升相关任务）。但该领域发展迅速、方法分散，缺乏全面的分析与横向比较——这正是本综述的切入点。

## 关键贡献

> **校正说明**：原笔记把贡献扩成 5 条，但 PDF 提取文本中 "The main contributions of this survey paper are as follows" 下**只明确列出 2 条**（见下）。其余"更广的范围/纳入 Diffusion 与 Transformer/数据集补全/横向对比"等是论文在随后一段（与 Wang et al. 2020、Yi et al. 2019、Skandarani et al. 2023 等既有综述对比时）阐述的"独特性"，并非作者编号列出的 contribution。这里据实分列。

**作者明确编号的贡献（2 条）：**
1.  **全面综述跨模态合成方法**：对跨模态医学图像合成方法进行全面回顾，分析网络结构、损失函数、性能，并概述数据可用性。
2.  **识别挑战与未来方向**：识别当前方法的挑战与局限，讨论医学图像合成可能的未来方向。

**作者声明的与既有综述相比的独特之处（来自对比段，非编号 contribution）：**
- 不仅深入分析模型性能、比较数据集，还**纳入了最新的 Diffusion 与 Transformer 相关模型**（既有综述如 Yi et al. 2019、Skandarani et al. 2023 主要聚焦 GAN 与 U-Net）。
- 提供跨多种网络架构与合成任务的**横向对比分析**（被许多同期工作忽视的方面）。
- **揭示了被以往工作忽略的数据集**。

## 方法

**请注意**：本篇为**综述**，"方法"指其对现有技术的**分析与归类**框架，而非提出新模型。以下据 PDF 提取文本（前 12 页，覆盖第 1、2 节）整理。论文统一记号：生成器 `G`、判别器 `D`、源模态 `x`、目标模态 `y`、低维噪声向量 `z`。

*   **架构演进脉络（Section 2.1，Fig. 1 时间线）**：早期用 Autoencoder 与全卷积网络（FCN，如 Nie et al. 2016、Xiang et al. 2017）；随后 U-Net 与 GAN 成为主流（Nie et al. 2017）；近期 Vision Transformer 与 Diffusion 架构成为新一代生成网络（Khader et al. 2023、Kazerouni et al. 2022）。综述确认 **U-Net、GAN、Transformer、Diffusion** 四类架构主导该领域，因此重点剖析这四类。
*   **关键模块与机制：**
    1.  **U-Net（2.1.1）**：编码器（收缩路径）+ 瓶颈层 + 解码器（扩展路径）的 U 形对称结构（Ronneberger et al. 2015）。编码器由卷积层 + ReLU 组成，经 max-pooling 下采样并增加特征通道；瓶颈层为级联卷积；解码器用上卷积（up-convolution）并通过**跳跃连接**拼接来自编码器的高分辨率特征。常用损失为基于强度的逐像素损失 **L1（MAE）/ L2（MSE）**（Sikka et al. 2018）。
    2.  **GAN（2.1.2）**：生成器与判别器通过极大极小博弈对抗优化，目标函数为 `L_GAN = E_{x~p(x)}[log D(x)] + E_{z~p(z)}[log(1 - D(G(z)))]`（Eq. 1）。生成器把噪声 `z`（均匀/高斯）从低维映射到高维真实空间，判别器区分真假。变体：**DCGAN**（GAN + CNN，更适合图像生成，Radford et al. 2015）；**cGAN**（在目标函数加约束/条件——可为标签或图像，提升可控性；Fig. 5A：以 MRI 为条件由 G 生成 CT，D 区分真实/生成 CT）；**CycleGAN**（Zhu et al. 2017，用两组生成器-判别器实现 A↔B 非配对转换，引入**循环一致性损失** `L_cyc`，对真实与循环重建数据计算逐像素 L1 损失，Eq. 2-3；Fig. 5B：`G_CT` 由真实 MRI 生成 CT，`G_MR` 再由该 CT 重建 MRI，`D_MR`/`D_CT` 分别判别 MR/CT 的真假）。
    3.  **Vision Transformer（2.1.3）**：源自 NLP 的 Transformer（Vaswani et al. 2017），核心是擅长捕捉长程关系的**自注意力**。ViT 将图像表示为**非重叠图像块（patch）序列**，连同**位置信息**送入编码器；编码器由**多头自注意力（MHSA）、归一化、MLP** 层构成（Fig. 6），通过 MHSA 为图像 token 生成注意力图，使网络选择性关注最显著区域，从而把握**全局上下文**。
    4.  **DDPM 扩散模型（2.1.4）**：Ho et al. (2020) 提出的去噪扩散概率模型，是一条参数化马尔可夫链，学习从纯噪声映射到真实数据。**前向过程**（Eq. 4-5）按方差调度 `β_t` 在 T 步内向 `x_0` 逐步加高斯噪声得到 `x_T`，由马尔可夫性可由 `x_0` 直接得到任意 `x_t` 的边缘分布；**反向过程**（Eq. 6）`p_θ(x_{t-1}|x_t)` 从纯噪声逐步去噪，当 `β_t` 较小时该转移可近似为高斯。去噪网络 `p_θ` 通过最小化预测噪声与真实噪声的 L2 损失训练：`L_error = E_{t,x_0,ε}[‖ε - ε_θ(x_t)‖_2^2]`（Eq. 7）。论文指出 Diffusion 受**采样计算开销大**所限，近期工作（如 Rombach et al. 2021，即潜空间扩散）致力于提升其计算效率。
*   **背景小节（2.2）补充的合成应用动机**：医学图像合成还可用于真实模拟病理状态、避免高辐射重复扫描、为 CAD 系统做**数据增强**、获取正常人群数据（因公开数据多来自病患）、以及对比增强 MRI 等高风险场景成像。模态层面：MR 本身是多对比成像，可由已得对比合成缺失/损坏对比；低场（LF）MRI 便宜但信噪比低，可合成高场（HF）MR；MR 引导放疗（MRgRT）仍需 CT 做剂量计算，可由 MRI 生成**伪 CT** 勾画骨/肌边界；PET/MR 检查可由 MRI 合成 CT 用于**衰减校正（AC）**。

## 实验

**请注意**：本文是综述，**无独立实验**，而是对文献中的实验设置与结果做汇总分析。

*   **检索方法论**：用 **Scopus 与 PubMed** 检索 2018–2023 年 7 月的文献，检索式为 `("synth*" OR "pseudo" OR "translat*") AND "deep learning" AND ("medical imag*" OR "CT" OR "MRI" OR "MR" OR "PET" OR "low dose" OR "low count" OR "low field")`（标题/摘要/关键词字段）；另用 **Google Scholar** 查漏并排除综述类文章。先筛标题与摘要（纳入同行评审期刊/会议论文，排除超分、重建等不相关主题），全文复核与交叉引用后**最终纳入 173 篇**（Fig. 2 检索流程，Fig. 3 全文结构）。
*   **对比维度**：综述沿网络架构（CNN/U-Net、GAN 各变体、Transformer、Diffusion）× 合成任务（伪 CT、合成 MR、合成 PET）两个轴做横向比较，并比较损失函数、数据集与解剖区域、图像质量评估及下游任务表现。
*   **评价指标**：提取文本（前 12 页）**未列出具体指标名**；论文 Section 6 承诺给出各类评估方法与指标（综述此类通常含 MAE、PSNR、SSIM 等像素级与感知/任务级指标——**此为通用推断，非本文文本明示**）。
*   **后续章节的量化结果**：据原文后续页线索（提取缓存未覆盖，待核）——Section 3 按伪 CT / 合成 MR / 合成 PET 三类任务分述方法（如 p.13 提到 FD PET 合成、Transformer/Diffusion 近期方法、Table 3 概览合成 PET 工作），Section 4 分析网络模型（p.13："4. Analysis of networks"、"4.1 Network models"，指出 CycleGAN 在合成 MR/CT 中被最广泛使用），Section 5/6 给数据集与性能评估（p.18-19 提到 MAE/MSE 与多尺度结构相似性 MS-SSIM 用于改善边界，Table 4 涉及 T1/T2 加权图像）。**具体数值需查原文 p.13-32，前 12 页提取缓存不含。**
*   **效率信息**：前 12 页除提及 Diffusion 采样计算开销大外，未给速度/参数量/FLOPs 等量化效率数据。

## 局限

1.  **时间范围限制**：检索截止 2018–2023 年 7 月，无法覆盖此后进展（论文文本明示的检索区间所致）。
2.  **模态范围聚焦**：仅围绕 MRI、CT、PET 三种模态间的合成（论文标题与摘要明确界定），超声、X 光等其他模态涉及有限——此为范围界定，非缺陷。
3.  **范围排除项**：检索阶段主动排除了"为超分/重建做的图像转换"，故这类相邻任务不在覆盖内。
4.  **跨研究可比性**：作为综述汇总既有结果，不同文献在数据划分、预处理、评估口径上的差异会影响横向比较的严格性（综述固有局限，非本文文本逐句明示）。
5.  **本笔记的提取局限**：现有提取缓存仅覆盖 p.1-12（摘要、引言、第 2 节背景），第 3-8 节（各任务方法详析、数据集列表、性能数值、挑战与未来方向、结论）仅有"全文补读记录"中的零散行级线索，**完整技术细节与实验结论待据原文 p.13-32 核实**。

## 个人评论

1.  **一份可靠的入门路线图**：对想进入医学图像合成的研究者，本文给出清晰的"架构代际演进 + 任务分类"双轴框架（Fig. 1 时间线 + 伪 CT/合成 MR/合成 PET 三任务），能快速建立从 Autoencoder/FCN → U-Net/GAN → Transformer/Diffusion 的技术地图。
2.  **补齐了最新两代生成模型**：相比聚焦 GAN/U-Net 的既有综述，本文系统纳入 ViT 与 Diffusion，且第 2 节给出了四类架构的核心公式（GAN 目标、CycleGAN 循环一致性、DDPM 前向/反向与噪声预测损失），对快速对齐数学形式很有帮助。
3.  **务实地锚定临床痛点**：把技术综述与 MRI-only 放疗计划、PET/MR 衰减校正、低场→高场 MR、数据增强等真实场景绑定，便于读者评估方法的临床价值而非只看指标。
4.  **使用时的注意**：摘要承诺的"损失函数/数据集/指标横向对比"和具体数值都在第 3-6 节，本提取缓存不含；若要据本文做 related work 的量化对比或选型，务必回到原文 Table 3/4 及性能评估章节核对，不能仅凭前 12 页。

### 使用建议

*   **如果快速了解**：先读摘要、引言（第 1 节）与背景（第 2 节），即可掌握领域全貌、四类主流架构原理与三大合成任务。
*   **如果复现**：到第 3 节找对应任务（如伪 CT 生成）综述的具体模型（如某 CycleGAN 变体），再回查其**原始论文**获取实现细节——综述本身不含可复现配置。
*   **如果借鉴创新点**：学习其"架构 × 任务"的分析框架；可思考如何融合 Transformer 全局注意力与 Diffusion 生成能力，或设计更强的结构一致性损失（如文中提到的 MS-SSIM 方向）。
*   **如果写 related work**：可作为"医学图像生成/跨模态翻译"领域 2018–2023 的代表性综述引用，用于交代背景与技术演进；引用具体数据集/指标对比时需回原文核实。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇发表于 *Medical Image Analysis* 92 (2024) 的**综述（Survey paper）**，系统回顾 2018–2023 年（7 月止）基于深度学习的跨模态医学图像合成，覆盖三大目标任务：**伪 CT（pseudo-CT）、合成 MR、合成 PET**。它面向研究者提供路线图，分析主流深度学习架构（U-Net、GAN、Vision Transformer、Diffusion）、模型设计、损失函数、数据集与评估指标。属**医学图像分析**领域，核心问题是"如何用深度学习从一种成像模态生成另一种模态"。在本库 taxonomy 下，最贴切的是 **A2_医学图像_分类_配准_生成**（生成子主题），并打上 **R_综述_Survey** 副标签以体现其综述属性。

## 2. 一句话总结
本文全面综述 2018–2023 年用深度学习（U-Net、GAN 及其变体、ViT、Diffusion）做 MRI/CT/PET 跨模态合成（伪 CT、合成 MR、合成 PET）的研究，基于 Scopus+PubMed 检索纳入 173 篇文献，沿"网络架构 × 合成任务"双轴比较方法设计、损失函数、数据集与性能，并指出挑战与未来方向。

## 3. 背景与问题
*   **为什么做：** MRI/CT/PET 各提供结构、功能、代谢信息，但完整多模态获取面临辐射风险（PET/CT，儿童尤甚）、成本高、扫描时间长（引入伪影）等问题，部分场景（如 MRI-only 放疗计划）难以安全获取精确成像。图像合成可"从源模态映射到目标模态"，最大化已采集图像利用率、缩短扫描时间、降低成本。
*   **之前方法的问题：** 传统方法依赖专业人员**手工选择特征**，表征复杂细节能力有限，可靠性与泛化性差。
*   **核心矛盾：** 模态间映射**高维、非线性、病态**；需自动学习复杂非线性关系的方法。深度学习生成式建模被证明更优，但领域快速发展且分散，缺乏全面横向比较——本综述补此空白。

## 4. 核心贡献
作者在 "The main contributions of this survey paper are as follows" 下**明确编号列出 2 条**：
1.  **全面综述跨模态合成方法**，分析网络结构、损失函数、性能，并概述数据可用性。
2.  **识别当前方法的挑战与局限，讨论未来方向。**

随后在与既有综述（Wang et al. 2020；Yi et al. 2019；Skandarani et al. 2023）对比时，强调本文的**独特范围**（非编号 contribution）：纳入最新 Diffusion 与 Transformer 模型（既有综述多聚焦 GAN/U-Net）、给出跨架构与跨任务的横向对比、揭示被忽略的数据集。
> 原 AI 笔记把这些"独特性"误并为 5 条编号贡献，本次据原文校正为"2 条编号 + 独特性补充"。

## 5. 方法详解
本篇为综述，"方法"即其对现有技术的分析归类框架（Section 2）。统一记号：`G` 生成器、`D` 判别器、`x` 源模态、`y` 目标模态、`z` 噪声。

*   **演进脉络（Fig. 1）**：Autoencoder/FCN（Nie 2016、Xiang 2017）→ U-Net/GAN（Nie 2017）→ ViT/Diffusion（Khader 2023、Kazerouni 2022）。综述聚焦 U-Net、GAN、Transformer、Diffusion 四类主导架构。
*   **U-Net**：编码器（卷积+ReLU+max-pooling 下采样、增通道）+ 瓶颈（级联卷积）+ 解码器（up-conv + 跳跃连接拼接编码器高分辨率特征）。损失：逐像素 L1（MAE）/L2（MSE）。
*   **GAN**：极大极小博弈，目标 `L_GAN = E_x[log D(x)] + E_z[log(1−D(G(z)))]`（Eq.1）。变体：DCGAN（+CNN）、cGAN（加条件约束，可控；MRI→CT 见 Fig.5A）、CycleGAN（两组 G/D 做非配对 A↔B，循环一致性损失 `L_cyc` 为真实与循环重建的 L1，Eq.2-3；MRI→CT→MRI 见 Fig.5B，`G_CT`/`G_MR`、`D_CT`/`D_MR`）。
*   **ViT**：图像切成非重叠 patch 序列 + 位置编码，编码器含 MHSA+Norm+MLP（Fig.6），自注意力捕捉全局上下文、聚焦显著区域。
*   **DDPM**：参数化马尔可夫链。前向按 `β_t` 调度向 `x_0` 加高斯噪声得 `x_T`（Eq.4-5，可由 `x_0` 直接采样 `x_t`）；反向 `p_θ(x_{t-1}|x_t)` 逐步去噪（Eq.6，小 `β_t` 时近似高斯）；去噪网络 `p_θ` 最小化噪声预测 L2 损失 `E[‖ε−ε_θ(x_t)‖_2^2]`（Eq.7）。局限：采样计算开销大，Rombach et al. 2021（潜空间扩散）等改进效率。
*   **范式差异**：从手工特征 → 数据驱动深度学习；内部从像素相似度（U-Net）→ 对抗+结构一致性（GAN）→ 全局建模（Transformer）→ 强生成能力（Diffusion）。

## 6. 实验与结果
综述无独立实验，汇总文献。
*   **检索**：Scopus + PubMed（2018–2023.07），检索式见正文（synth*/pseudo/translat* AND deep learning AND CT/MRI/MR/PET/low dose/low count/low field 等）；Google Scholar 查漏并排除综述；筛选+交叉引用后**纳入 173 篇**（Fig.2 流程）。
*   **比较轴**：网络架构 × 合成任务（伪 CT/合成 MR/合成 PET），并比较损失函数、数据集与解剖区域、图像质量与下游任务。
*   **指标**：前 12 页提取文本**未列具体指标名**；Section 6 承诺给出（综述常见 MAE/PSNR/SSIM 等，属通用推断非文本明示）。
*   **后续页线索（提取缓存未覆盖，待核）**：p.13 提到 FD PET 合成、Table 3 概览合成 PET、"4. Analysis of networks / 4.1 Network models"、CycleGAN 在合成 MR/CT 中应用最广；p.18-19 提到 MAE/MSE 与 MS-SSIM 改善边界、Table 4 涉及 T1/T2 加权图像。具体数值需查原文 p.13-32。

## 7. 这篇论文真正有价值的地方
1.  **双轴知识地图**：架构代际（Fig.1）× 三大合成任务，帮助快速建立领域全景与技术关联。
2.  **补齐最新两代模型**：超越只看 GAN/U-Net 的旧综述，系统纳入 ViT 与 Diffusion，并给出四类架构核心公式（GAN/CycleGAN/DDPM），便于对齐数学形式。
3.  **结构化分析维度**：沿网络结构、损失函数、数据集、评估指标多维比较，对设计实验与撰写论文有参考价值（具体对比表在第 3-6 节）。
4.  **锚定临床痛点**：MRI-only 放疗、PET/MR 衰减校正、低场→高场 MR、数据增强等，把技术与真实需求绑定。

## 8. 局限与问题
1.  **时间窗**：检索止于 2023 年 7 月，无法覆盖之后进展。
2.  **模态聚焦**：仅 MRI/CT/PET 三模态间合成（范围界定），超声/X 光涉及有限。
3.  **主动排除**：检索阶段排除"为超分/重建做的转换"，相邻任务不覆盖。
4.  **跨研究可比性**：不同文献数据划分/预处理/评估口径差异影响横向比较严格性（综述固有局限）。
5.  **本笔记提取局限**：仅 p.1-12 提取可用，第 3-8 节细节与数值需据原文 p.13-32 核实。

## 9. 我该怎么使用这篇论文
*   **快速了解**：读摘要 + 第 1 节引言 + 第 2 节背景，掌握四类架构与三大任务。
*   **复现**：到第 3 节找对应任务的具体模型，再查其原始论文获取实现细节。
*   **借鉴创新**：学其"架构 × 任务"分析框架；可思考融合 Transformer 全局注意力与 Diffusion 生成能力，或设计更强结构一致性损失（如 MS-SSIM 方向）。
*   **写 related work**：作为 2018–2023 代表性综述引用；引用具体数据集/指标对比时回原文核实。

## 10. 和其他论文的关系
本文位于 **A2_医学图像_分类_配准_生成** 主题（生成子方向），兼具 **R_综述_Survey** 属性，可作为该方向的综述锚点：
*   下游关联**医学图像分割/配准**笔记——合成图像常作分割的数据增强，图像翻译与空间配准亦密切相关（文中多处提及 registration、segmentation 作为下游任务）。
*   关联本库中聚焦**单一生成模型（具体 GAN/Diffusion/Transformer 变体）在医学图像合成**的论文，本文可作其背景与横向对比综述。
*   关联同刊 *Medical Image Analysis* 的其他合成/生成工作。
*   （以下为占位主题词，非已存在笔记，待建链时替换为真实笔记名）`[[生成对抗网络在医学图像中的应用]]`、`[[扩散模型医学图像生成]]`、`[[医学图像跨模态翻译]]`。

## 11. 关键词
医学图像合成, 跨模态翻译, 伪CT(pseudo-CT), 合成MR, 合成PET, 深度学习, 生成式建模, U-Net, GAN, cGAN, CycleGAN, 循环一致性损失, Vision Transformer, 自注意力, DDPM/扩散模型, MAE/MSE, 综述, MRI-only放疗, 衰减校正

## 12. 可信度说明
本精读笔记**基于 PDF 提取缓存的前 12 页**（摘要、引言、第 2 节背景），这部分提取**质量良好、语句连贯**，作者信息、摘要、检索式、173 篇纳入数、四类架构描述与核心公式（Eq.1-7）均清晰可辨，据此整理的"背景/贡献/第 2 节方法/检索方法论"可信度高。本次复核相对原 AI 笔记做了三处实质校正：① 修复了摘要乱码、补全英文原文与中文译文；② 把"核心贡献"由臆增的 5 条改回原文明确编号的 **2 条 + 独特性补充**；③ 在 frontmatter/基本信息/相关链接补上 **R_综述_Survey** 副标签。**仍存信息缺口**：第 3-8 节（伪 CT/合成 MR/合成 PET 各任务方法详析、数据集完整列表、性能数值、挑战与未来方向、结论）仅有"全文补读记录"的行级线索，凡涉及这部分的具体数字均标注"据原文后续页，提取缓存未覆盖，待核"。因此本笔记对论文**总体框架与定位可靠**，对**深入技术细节与实验结论**存在信息缺失。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本连贯, ~2086 字符/页); 来源缓存: `.paper-cache/extracts/Deep-learning-based-synthesis-of-MRI--CT-and-PET--Revi_2024_Medical-Image-An.txt` (缓存仅含 p.1-12/32; 原 AI 主体 12/32 + 全文补读记录补 p.13-32 行级线索); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-32; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-32。
- **提取情况**: 缺失页 20 页, 其中 20 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Medical Image Analysis 92 (2024) 103046
- p.13: In the reviewed literature on FD PET synthesis, the majority of
- p.13: The weight ratio between primary and secondary task losses was set
- p.13: Recently, Transformer and Diffusion based methods have received
- p.13: method using spatial adaptive and Transformer-based fusion networks
- p.13: In the proposed method, the images are summarized and quantized into
- p.13: Transformer-based approaches have used in recent studies on FD
- p.13: Table 3 presents an overview of deep-learning-based synthetic PET
- p.13: 4. Analysis of networks
- p.13: 4.1. Network models
- p.13: Deep-learning-based architectures predominantly employed in med-
- p.13: CycleGANs have been most extensively utilized for synthetic MR and

### 缺失页关键摘录

- p.13: segmentation-guided strategy enhances the accuracy of image trans-
- p.13: Table 3 presents an overview of deep-learning-based synthetic PET
- p.16: employed to resolve the limitation with CNN to extract more contextual
- p.16: learned space to other relative features in the dataset using a single-
- p.17: process. As a result, many conditioning-based diffusion methods for
- p.18: (2022) have employed MAE or MSE. On the other hand, GAN-based ap-
- p.18: squared distances for generator loss functions often result in images
- p.18: accuracy at image boundaries, while Lei et al. (2019b) and Liu et al.
- p.18: the local structure. To solve this limitation, the multi-Scale Structural
- p.19: presented in Table 4. T1-weighted and T2-weighted images have been
- p.19: pacted training and evaluation processes, particularly at bone and air
- p.19: limited accuracy due to residual mismatches between scans, which can
<!-- AI_READING_NOTE_END -->
