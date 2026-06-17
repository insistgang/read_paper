---
title: "A prior knowledge-guided distributionally robust optimization-based adversarial training strategy for medical image classification"
authors:
  - "Shancheng Jiang"
  - "Zehui Wu"
  - "Haiqiong Yang"
  - "Kun Xiang"
  - "Weiping Ding"
  - "Zhen-Song Chen"
year: 2024
venue: Information Sciences
doi: 10.1016/j.ins.2024.120705
pdf: [[A-prior-knowledge-guided-distributionally-robust-optimization_2024_Informati.pdf]]
primary_topic: A2_医学图像_分类_配准_生成
topics:
  - "A2_医学图像_分类_配准_生成"
  - "O_物理对抗_安全_鲁棒"
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
extract_cache: .paper-cache/extracts/A-prior-knowledge-guided-distributionally-robust-optimization_2024_Informati.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/16 pages"
---
# A prior knowledge-guided distributionally robust optimization-based adversarial training strategy for medical image classification

## 基本信息
- **PDF**: [[A-prior-knowledge-guided-distributionally-robust-optimization_2024_Informati.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`, `O_物理对抗_安全_鲁棒`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A prior knowledge-guided distributionally robust optimization-based adversarial training strategy for medical image classification |
| **作者** | Shancheng Jiang; Zehui Wu; Haiqiong Yang; Kun Xiang; Weiping Ding; Zhen-Song Chen |
| **发表时间** | 2024（Available online 7 May 2024） |
| **刊物/会议** | Information Sciences 673 (2024) 120705 |
| **DOI** | 10.1016/j.ins.2024.120705 |
| **代码** | https://github.com/sysu19351146/MMK-DRO |

## 摘要

> 来源: 据 PDF 提取文本整理。

**英文原文（清理后）**：

> Medical image classification plays a vital role in computer vision applications within the field of healthcare and medicine, and deep neural network-based classifiers are continuously achieving new breakthroughs and demonstrating tremendous potential in medical imaging analysis. However, the lack of robustness in deep learning techniques makes it risky to apply these classifiers to the domain of healthcare. In addition, the existing adversarial training strategies and domain generation methods are difficult to generalize into the medical imaging field challenged by complex medical texture features. To address this issue, we propose a medical morphological knowledge-guided adversarial training strategy, by jointly considering the robustness against medical data distribution shifts and adversarial attacks from the view of distributionally robust optimization. First, we train a surrogate model with the augmented dataset by guided filtering for capturing model attention on medical morphological information. Next, we design a gradient normalization-based prior knowledge injection module to transfer the attention information learned by surrogate model to the main classifier. Finally, we design a distributionally robust optimization-based training strategy to induce the main classifier to learn key diagnostic clues as well as enhance the robustness against adversarial attacks. To evaluate the effectiveness of the proposed methods, we perform experiments on two types of in-domain and out-of-domain medical image sets, which contain lung CT scan datasets and dermatoscopic image datasets. Comparative results show that the proposed training strategy achieves higher adversarial attack accuracy than all involved state-of-the-art adversarial training methods and domain generation methods. The code is available at https://github.com/sysu19351146/MMK-DRO.

**中文翻译**：

> 医学图像分类在医疗健康领域的计算机视觉应用中起着至关重要的作用，基于深度神经网络的分类器不断取得新突破，在医学影像分析中展现出巨大潜力。然而，深度学习技术鲁棒性的缺失，使得将这类分类器应用于医疗领域存在风险。此外，现有的对抗训练策略和域生成（domain generation）方法难以泛化到具有复杂医学纹理特征的医学影像领域。为解决该问题，本文提出一种医学形态知识引导的对抗训练策略，从分布鲁棒优化（distributionally robust optimization, DRO）的视角，联合考虑模型对医学数据分布偏移与对抗攻击的鲁棒性。首先，用引导滤波（guided filtering）增强后的数据集训练一个代理模型（surrogate model），以捕获模型对医学形态信息的注意力；接着，设计一个基于梯度归一化（gradient normalization）的先验知识注入模块，将代理模型学到的注意力信息迁移到主分类器；最后，设计一种基于分布鲁棒优化的训练策略，引导主分类器学习关键诊断线索并增强其对对抗攻击的鲁棒性。为评估方法有效性，在两类含域内（in-domain）与域外（out-of-domain）的医学图像集（肺部 CT 扫描数据集与皮肤镜图像数据集）上进行实验。对比结果表明，所提训练策略相比所有参与对比的最先进对抗训练方法和域生成方法，取得了更高的对抗攻击准确率。代码已开源。

## 研究背景与动机

- **为什么要做**：医学影像（X 光、MRI、CT 等）配合计算机辅助诊断（CAD）系统已成为变革性技术，深度学习（尤其卷积网络自 ILSVRC2012 起）显著提升了 CAD 性能。但提取文本明确指出，即便是最先进的深度模型也**缺乏鲁棒性**——对数据分布偏移（distribution shift）和对抗攻击（adversarial attack）都很脆弱 [9,10]。在医疗场景，模型出错可能造成误诊、错误治疗方案，乃至**医疗报销欺诈（medical reimbursement fraud）**等严重甚至危及生命的后果 [14,16]。
- **之前方法的问题**（据提取文本归纳）：
    1. 现有对抗训练策略与域生成方法主要面向自然图像，**难以泛化到具有复杂医学纹理特征的医学影像领域**（医学任务高度专门化、依赖领域特定的上下文信息）；
    2. 大多数对抗训练方法只考虑**单个数据样本的扰动**（individually altering each data point），忽略了训练数据周围的潜在分布信息；
    3. 不同采样设备、后处理方法、患者种族等导致的分布差异会带来严重性能退化。
- **核心矛盾**：如何在**不破坏关键医学诊断线索（纹理/形态）**的前提下，同时增强模型对**数据分布偏移**和**对抗攻击**两类鲁棒性威胁的抵抗力。
- **领域脉络（提取文本 Section 2 相关工作）**：模型鲁棒性研究分三支——域适应（domain adaptation，测试域与源域相似）、域生成（domain generation，测试分布在训练时未知）、对抗鲁棒（对抗攻击分白盒/灰盒/黑盒，对抗训练是最有效防御之一）。本文是首个**联合考虑医学数据分布偏移特性与模型对抗鲁棒性**的工作。

## 关键贡献

> 据提取文本 Section 1 末尾的三点贡献整理：

1. 设计了一种新颖的模型训练策略，目标是同时增强模型对**医学数据分布偏移**与**一般对抗攻击**的鲁棒性。通过把从**代理模型**获得的先验知识注入**主分类器**，在数据增强过程中**最大限度保留**原始医学图像中的形态特征，从而引导主分类器更高效地学习关键诊断线索。
2. 从**训练数据周围分布**的视角联合考虑医学数据分布偏移特性与对抗鲁棒性，设计了基于 **Wasserstein 距离**的分布鲁棒优化对抗训练策略，并配合一种基于**自引导滤波（self-guided filtering）的注意力参数正则化技术**，提升主分类器对分布偏移与对抗攻击的双重鲁棒性。
3. 在案例研究中模拟真实世界医学影像分析场景：从**多个医疗系统**收集相似图像样本，构建了**两类域外（OoD）医学数据集**评估模型对目标医疗系统未见图像的鲁棒性。结果显示本方法在域内、域外数据集上均优于现有方法，并从**模型可解释性**角度验证了有效性。

## 方法

- **整体框架（Fig. 1）**：方法包含三个核心部分——1）基于引导滤波增强训练的**代理模型**（捕获形态注意力）；2）基于**梯度归一化**的**先验知识注入模块**；3）基于**分布鲁棒优化**的**主分类器训练策略**。提取文本明确指出该策略适用于**基于 vision transformer 的医学图像分类器**（"available to general vision transformer-based medical image classifiers"）——这是原笔记遗漏的关键骨干信息。
- **问题设定（Section 3.1）**：典型分类任务，从输入 `x` 预测标签 `y`，`x` 服从数据空间分布 `D`。记 `√x` 为增强样本，`xʹ` 为对抗样本，`f(x;θ)` 为分类器输出（θ 为参数）。文中说明 transformer 类模型在多数识别数据集上优于 CNN，图像经 embedding 后送入多层预训练 transformer。
- **关键模块**：
    1. **代理模型与引导滤波（Section 3.2）**：受引导滤波 [38]"增强边缘、平滑细节"特性启发，对医学图像采用基于引导滤波的局部线性变换，滤波窗口 `w_k` 核大小 `s×s`、像素中心为 `k`。增强图像计算为（提取文本式 (1)(2)，OCR 有损，按引导滤波标准形式还原）：
        - `√x_i = a_k · x_i + b_k, ∀i ∈ w_k`（式 1）
        - `a_k = σ²_k / (σ²_k + t)` 形式的线性系数，`b_k = (1 − a_k)·μ_k`（式 2），其中 `μ_k`、`σ²_k` 为窗口 `w_k` 内像素均值与方差，`t` 为控制平滑程度的**温度参数（temperature parameter）**。
        - **机理**：滤波保留边缘但平滑小波动，**移除病灶区域内大部分纹理特征**——而这些纹理可能恰是某些疾病的关键诊断线索。以阳性肺部 CT 为例，增强后病灶区被移除、仅留轮廓，按理预测标签会变为阴性。基于这一点，引入一个**与主分类器同结构的代理模型**，并设计相应学习策略，**驱使代理模型把注意力聚焦到被移除的纹理特征信息上**，从而捕获医学形态先验。
    2. **先验知识注入模块（Section 3.3）**：基于**梯度归一化**，将代理模型学到的注意力信息迁移到主分类器，以增强主分类器对多样医学数据分布偏移的鲁棒性。（注入模块的逐步公式位于 p.12 之后，提取缓存未覆盖；此处据 Section 1/Abstract 的概述描述。）
    3. **分布鲁棒优化（DRO）训练策略（Section 3.4）**：主分类器采用基于 **Wasserstein 距离**的分布鲁棒优化进行对抗训练，不仅考虑单个对抗样本 `xʹ`，而是在训练数据周围由 Wasserstein 距离定义的**分布集合**上寻找最坏情况分布。其中嵌入一个**自适应惩罚系数生成策略（adaptive penalty coefficient generation strategy）**，用于平衡鲁棒性与准确率。（该节具体公式位于提取缓存未覆盖页，据原文后续页，待核。）
- **训练方式**：多阶段——1）用引导滤波增强数据训练代理模型；2）经知识注入模块指导主分类器；3）用 DRO 策略对主分类器做对抗训练。
- **推理流程**：提取文本未明确说明推理阶段流程；通常推理时直接使用训练好的主分类器（代理模型与注入仅用于训练）。
- **与已有方法的差异**：**首次**联合考虑医学数据分布偏移特性与对抗鲁棒性；不同于仅扰动单样本的传统对抗训练，从数据分布视角优化；不同于简单数据增强/域适应，通过知识注入保留关键诊断特征。
- **论文类型特化（医学类）**：
    - **任务类型**：医学图像**分类**（二分类/诊断阳性-阴性，以肺部 CT 为例）。
    - **图像模态**：肺部 CT 扫描、皮肤镜（dermatoscopic）图像。
    - **骨干**：vision transformer 类分类器。
    - **数据集**：作者自建域内 + 域外（OoD）医学数据集（含 COVID-19 CT 与皮肤病变两类，见参考文献 [40][41]）。
    - **临床意义**：提高 CAD 系统在设备差异、患者群体变化及恶意攻击下的可靠性，降低误诊与医疗报销欺诈风险。

## 实验

> 注意：提取缓存仅覆盖 p.1-12（含 Abstract / 引言 / 相关工作 / 方法 3.1-3.2 局部），**实验主体（Section 4）与结论（Section 5）的定量结果不在提取缓存内**。以下结论性描述来自摘要、引言贡献，以及笔记"全文补读记录"中 p.13-14 的关键摘录（据原文后续页，提取缓存未覆盖，待核）。

- **使用的数据集**：两类医学图像集，每类各含**域内**与作者自建的**域外（OoD）**子集——1）肺部 CT 扫描数据集；2）皮肤镜图像数据集。参考文献提示其底层数据可能来自 COVID-19 患者 CT 大数据集 [40] 与 HAM10000 多源皮肤镜数据集 [41]（据原文参考文献页，待核）。
- **对比方法**：摘要称与"所有参与的最先进对抗训练方法与域生成方法"对比。p.13 摘录明确提到 **TRADES** 作为对比基线之一（"TRADES does not concentrate on the lesion area which indicates that the result of TRADES is lack of interpretability"），参考文献 [21] 为 TRADES（Zhang et al., ICML 2019）。其余对比方法名称在提取缓存未覆盖页中（待核）。
- **评价指标**：摘要与 p.13 摘录指明核心指标为**对抗攻击准确率（adversarial attack accuracy）/ 对抗鲁棒性**，并在不同**扰动预算（perturbation budgets）**下测试；同时关注**自然准确率（natural accuracy）**的平衡（p.14："our model achieves better adversarial robustness while balancing natural accuracy"）。具体数值表格在提取缓存未覆盖页（待核）。
- **主实验结果**：MMK-DRO 在域内与域外数据集上均取得**高于所有对比的最先进对抗训练与域生成方法**的对抗攻击准确率（摘要 + p.13 摘录证实）。具体数字提取缓存未覆盖（待核）。
- **消融实验**：p.13 摘录明确指出做了消融研究，且证明**先验知识注入模块**与**分布鲁棒优化**两者**均有正向作用**（"ablation study demonstrate the positive effectiveness of both the prior knowledge injection module and the distributionally robust ..."）——这一点纠正了原笔记"未明确是否进行消融"的说法。具体数值在提取缓存未覆盖页（待核）。
- **可解释性/定性分析**：p.13 摘录显示作者用注意力可视化对比，指出 TRADES 未聚焦病灶区、可解释性不足，反衬本方法注意力更贴合病灶（据原文后续页，待核）。
- **泛化实验**：通过自建**域外（OoD）数据集**评估对未见医疗系统图像的泛化/鲁棒性，是实验设计的关键部分。
- **效率信息**：提取文本未提及速度、参数量、FLOPs 等效率信息。

## 局限

> p.14 标题"The advantages and limitations of this work are summarized as follows"提示原文有专门的优劣讨论，但该页正文不在提取缓存内。以下为据可见文本的合理评估（标注未覆盖项）。

1. **方法步骤多、复现成本**：含代理模型训练、知识注入、Wasserstein DRO 三段式流程，复现与调参复杂度较高；计算开销文中未在提取缓存内给出量化分析（待核）。
2. **模态与任务泛化性**：实验仅覆盖肺部 CT 与皮肤镜两种模态的**分类**任务，对 MRI、超声等其他模态或分割/检测等其他任务的有效性未验证。
3. **假设依赖**：方法依赖"引导滤波能有效分离形态轮廓与病灶纹理"这一假设；对于纹理本身即关键诊断线索且无法被轮廓替代的疾病，"移除纹理迫使代理模型关注纹理"的设计动机可能受限。
4. **骨干局限**：策略表述为面向 vision transformer 类分类器，对纯 CNN 骨干的适配性提取文本未明确（待核）。
5. **定量证据缺口（本笔记角度）**：提取缓存未覆盖实验定量表格，故笔记中实验数值均为待核状态，理解方法优势的量化程度受限。

## 个人评论

1. **问题定义的现实性与前瞻性**：把"数据分布偏移"和"对抗攻击"两类鲁棒性威胁统一到 DRO 框架下，并锚定医疗场景的高代价后果（误诊、报销欺诈），问题切口扎实且有临床现实感。
2. **方法设计的巧妙融合**：用引导滤波"故意移除纹理"再用代理模型"被迫关注被移除纹理"来显式建模形态先验，是一个反直觉但自洽的设计；再通过梯度归一化把这种注意力注入主分类器，比单纯数据增强更有针对性。
3. **优化视角的提升**：从单点扰动的传统对抗训练提升到 Wasserstein DRO 的最坏情况分布，理论上对"训练时未知的测试分布"更有保障，与域生成设定天然契合。
4. **实验设置的严谨性**：自建跨医疗系统的 OoD 数据集，配合 TRADES 等强基线和可解释性可视化，论证链条比较完整（以可见摘录判断）。
5. **对后续研究的启发**："代理模型捕获先验 → 梯度归一化注入 → 分布鲁棒训练"这一范式可迁移到其他需要领域先验（解剖约束、放射组学特征、不确定性图）的鲁棒学习任务。
6. **可改进处**：温度参数 `t`、惩罚系数自适应策略、注入强度三者的相互作用缺少在可见文本中的敏感性讨论，是阅读时最想看到却受提取截断影响而存疑的部分。

### 使用建议

- **如果快速了解**：读摘要、引言最后三点贡献、以及 **Fig. 1（方法概述图）**。
- **如果复现**：精读第 3 节，尤其 3.2（代理模型与引导滤波）、3.3（梯度归一化知识注入）、3.4（Wasserstein DRO 训练 + 自适应惩罚系数），并结合开源代码 `https://github.com/sysu19351146/MMK-DRO`。
- **如果借鉴创新点**：
    - 学习"代理模型—梯度归一化知识注入"范式，用于注入解剖约束、不确定性图等其他先验；
    - 学习把 **Wasserstein DRO** 落地到特定领域（医学影像）对抗训练的做法；
    - 借鉴**自建跨机构 OoD 评估集**严格测试泛化性的实验设计。
- **如果写 related work**：可置于"医学图像对抗攻击与防御"、"面向医疗的域泛化/域生成"或"基于先验知识的鲁棒深度学习"等小节。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[O_物理对抗_安全_鲁棒]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**医学图像分类**与**深度学习鲁棒性**的交叉研究，发表于 Information Sciences 673 (2024) 120705。它聚焦深度神经网络（尤其 vision transformer 类分类器）在医学图像分类中对**对抗攻击**与**数据分布偏移**的双重脆弱性，从**分布鲁棒优化（DRO）**视角提出一套以**医学形态先验**为引导的对抗训练策略（MMK-DRO）。从知识库分类看，它最贴合 A2（医学图像分类）并与 O（对抗/安全/鲁棒）强相关，而非原标注的 A3（配准/切片/张量/数学）——本文不涉及配准或张量数学。

## 2. 一句话总结
MMK-DRO：用引导滤波"剥离纹理 + 代理模型回捞纹理注意力"显式建模医学形态先验，经梯度归一化注入主分类器，再以 Wasserstein 距离的分布鲁棒优化做对抗训练，从而同时抵御医学数据分布偏移与对抗攻击。

## 3. 背景与问题
- **为什么要做**：CAD 系统中深度模型潜力巨大，但缺乏鲁棒性——对分布偏移（设备/后处理/患者种族差异）与对抗攻击都脆弱，在医疗场景可致误诊、错误治疗、医疗报销欺诈等高代价后果。
- **之前方法的问题**：1）对抗训练/域生成主要面向自然图像，难泛化到复杂医学纹理；2）多数对抗训练只扰动单个样本，忽略训练数据周围的分布信息；3）数据增强可能破坏纹理这一关键诊断线索。
- **核心矛盾**：在**不损失关键诊断线索**的前提下，同时增强对分布偏移与对抗攻击的鲁棒性。
- **领域定位**：相关工作（Section 2）把鲁棒性研究分为域适应、域生成、对抗鲁棒三支，并指出医学影像方向研究仍处早期；本文自述为首个联合考虑"医学分布偏移特性 + 对抗鲁棒"的工作。

## 4. 核心贡献
1. 新颖训练策略：从代理模型向主分类器注入先验知识，在数据增强中最大限度保留医学形态特征，引导主分类器更高效学习诊断线索。
2. 基于 **Wasserstein 距离**的分布鲁棒优化对抗训练 + 基于**自引导滤波的注意力参数正则化**，提升对分布偏移与对抗攻击的双重鲁棒性。
3. 模拟真实场景，从多个医疗系统收集样本构建**两类 OoD 医学数据集**（肺 CT、皮肤镜）评估鲁棒性；域内域外均优于现有方法，并以可解释性佐证。

## 5. 方法详解
- **整体框架（Fig. 1）**：三段式——引导滤波增强训练的代理模型 → 梯度归一化先验知识注入 → Wasserstein DRO 主分类器训练。策略面向 **vision transformer 类医学分类器**。
- **问题设定**：从 `x` 预测 `y`，`x ~ D`；`√x` 为增强样本、`xʹ` 为对抗样本、`f(x;θ)` 为分类器输出。
- **关键模块**：
    1. **引导滤波 + 代理模型（3.2）**：核大小 `s×s` 的窗口 `w_k` 内做局部线性变换 `√x_i = a_k·x_i + b_k`，系数由窗口均值 `μ_k`、方差 `σ²_k` 与温度参数 `t` 决定（`t` 控平滑程度）。滤波保边缘、平滑细节 ⇒ **移除病灶纹理**，仅留轮廓。设计与主分类器同结构的代理模型，用专门学习策略迫使其**关注被移除的纹理信息**，从而捕获形态先验（动机：阳性 CT 去纹理后理应被判阴性，模型若真关注病灶就会对此敏感）。
    2. **梯度归一化知识注入（3.3）**：将代理模型注意力经梯度归一化迁移到主分类器，增强其对分布偏移的鲁棒性。（公式在提取缓存未覆盖页，待核。）
    3. **Wasserstein DRO 训练（3.4）**：在训练数据周围由 Wasserstein 距离定义的分布集合上寻找最坏情况分布做对抗训练，嵌入**自适应惩罚系数生成策略**平衡鲁棒性与准确率。（公式在提取缓存未覆盖页，待核。）
- **训练/推理**：训练分代理模型→注入→DRO 对抗训练三阶段；推理直接用主分类器（提取文本未显式描述推理流程）。
- **差异点**：首次联合医学分布偏移与对抗鲁棒；从分布视角而非单点扰动优化；通过知识注入保留诊断特征，区别于纯增强/域适应。

## 6. 实验与结果
> 提取缓存仅到 p.12，实验定量表格（Section 4）与结论（Section 5）不在缓存内；以下据摘要 + p.13-14 摘录，标"待核"者来自原文后续页。
- **数据集**：肺 CT、皮肤镜两类，各含域内 + 自建 OoD 子集（疑似底层数据 [40] COVID-19 CT、[41] HAM10000，待核）。
- **对比方法**：与所有最先进对抗训练 + 域生成方法对比；可见基线含 **TRADES**（[21], ICML 2019），其余名称待核。
- **指标**：对抗攻击准确率/对抗鲁棒性（多个**扰动预算**下），同时平衡自然准确率。
- **主结果**：MMK-DRO 在域内域外均取得高于所有对比方法的对抗攻击准确率（摘要 + p.13 摘录证实）；具体数字待核。
- **消融**：p.13 摘录明确做了消融，证明**知识注入模块**与 **DRO** 两者均有正向贡献（纠正原笔记"未明确"的说法）；数值待核。
- **可解释性**：注意力可视化显示 TRADES 未聚焦病灶、可解释性差，本方法更贴合病灶区（p.13 摘录，待核）。
- **泛化**：以自建 OoD 集评估对未见医疗系统图像的鲁棒性。
- **效率**：提取文本未提及速度/参数量/FLOPs。

## 7. 这篇论文真正有价值的地方
1. **统一两类鲁棒性威胁**：把分布偏移与对抗攻击纳入同一 DRO 框架，问题定义有深度与临床现实感。
2. **形态先验的显式建模**：引导滤波"剥纹理"+ 代理模型"回捞纹理注意力"是反直觉而自洽的巧思，超越普通数据增强。
3. **优化视角升级**：单点对抗 → Wasserstein 最坏情况分布，与"测试分布未知"的域生成设定天然契合。
4. **严谨的 OoD 评估**：自建跨医疗系统数据集 + 强基线（TRADES）+ 可解释性可视化，论证较完整。
5. **可迁移范式**："先验捕获→梯度归一化注入→分布鲁棒训练"可推广到其他领域先验注入的鲁棒学习任务。

## 8. 局限与问题
1. **流程复杂**：三段式训练（代理/注入/DRO）复现与调参成本高；计算开销在缓存未覆盖页（待核）。
2. **模态/任务窄**：仅 CT、皮肤镜两模态的分类，未及 MRI/超声或分割/检测。
3. **假设依赖**：依赖"引导滤波能分离轮廓与纹理"；纹理即关键且不可由轮廓替代的疾病可能失效。
4. **骨干局限**：表述面向 vision transformer，对 CNN 适配性未明确（待核）。
5. **定量缺口（笔记角度）**：实验表格不在提取缓存，方法增益的量化理解受限。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 三点贡献 + Fig. 1。
- **复现**：精读 3.2/3.3/3.4，结合开源代码 `https://github.com/sysu19351146/MMK-DRO`。
- **借鉴**：代理模型—梯度归一化注入范式；领域化 Wasserstein DRO 对抗训练；自建 OoD 评估集设计。
- **写 related work**：归入"医学图像对抗攻防""面向医疗的域泛化/域生成""基于先验的鲁棒深度学习"。

## 10. 和其他论文的关系
按修正后的主题 `A2_医学图像_分类_配准_生成` 与 `O_物理对抗_安全_鲁棒`，本文是"医学图像分类鲁棒性/对抗防御"方向。可关联：
- 使用**分布鲁棒优化 / Wasserstein 距离**训练的论文；
- 研究**医学图像对抗攻击与对抗训练**（如 TRADES、PGD、FGSM/BIM/C&W 系列）的论文；
- 使用**引导滤波/图像先验**做医学预处理或增强的论文；
- **域生成 / 域适应**用于医学影像的论文。
（提取信息有限，此处不强行建立逐篇 `[[双链]]`。）

## 11. 关键词
医学图像分类、对抗训练、分布鲁棒优化（DRO）、Wasserstein 距离、域生成、引导滤波、代理模型、梯度归一化、先验知识注入、对抗攻击、数据分布偏移、vision transformer、可解释性

## 12. 可信度说明
本笔记主体基于提取缓存的 **p.1-12**（标题、作者、摘要、引言、相关工作、方法 3.1 与 3.2 局部），并结合笔记"全文补读记录"中 p.13-16 的关键摘录。
- **提取质量**：可见文本脉络清晰（约 2086 字符/页），公式区因 OCR 有损（式 1/2 系数已按引导滤波标准形式还原并标注）。
- **信息缺口**：方法 3.3/3.4 的具体公式、实验 Section 4 的**定量结果表格**、对比方法完整列表、消融数值、效率分析均在提取缓存未覆盖页，笔记中相关结论已逐条标注"待核"。所有对抗攻击准确率等数字均未被提取缓存证实，严格未编造具体数值。
- **本轮修订要点**：（1）修正主题分类 A3→A2 + O；（2）用提取文本重建摘要并补中文译；（3）补足"面向 vision transformer""TRADES 基线""消融两模块均有效""OoD 底层数据 [40][41]"等可见证据；（4）将原"未做消融"等不确定表述按 p.13 摘录修正。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页), 但提取缓存仅 12/16 页, 实验定量结果未覆盖); 来源缓存: `.paper-cache/extracts/A-prior-knowledge-guided-distributionally-robust-optimization_2024_Informati.txt` (缓存 12/16 页, 文本截断于 25000/57094 字符; p.13-16 关键摘录见下方补读记录); 生成日期: 2026-06-05; 本轮优化: 2026-06-18; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-16; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-16。
- **提取情况**: 缺失页 4 页, 其中 4 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Information Sciences 673 (2024) 120705
- p.14: The advantages and limitations of this work are summarized as follows:
- p.15: CRediT authorship contribution statement
- p.15: Declaration of competing interest
- p.15: Data availability
- p.15: Acknowledgments
- p.15: References

### 缺失页关键摘录

- p.13: TRADES does not concentrate on the lesion area which indicates that the result of TRADES is lack of interpretability. Besides, from
- p.13: testing. In numeric experimental analysis, we conduct the model evaluation by simulating the medical image analysis scenarios in real-
- p.13: MMK-DRO achieves higher adversarial attack accuracy than all involved state-of-the-art adversarial training methods and domain
- p.13: testing with different perturbation budgets, and MMK-DRO achieves better adversarial robustness while balancing natural accuracy.
- p.13: ablation study demonstrate the positive effectiveness of both the prior knowledge injection module and the distributionally robust
- p.13: dataset by guided filtering and a customized loss function. Without directly training the main classifier with hybrid image samples, the
- p.14: world to conduct model evaluation, which shows that our model promises to have better performance in practical medical imaging
- p.14: adversarial attacks. (2) Adversarial training strategies often sacrifice natural accuracy while increasing adversarial accuracy, our
- p.14: model achieves better adversarial robustness while balancing natural accuracy. (3) Most related researches only focus on robustness
- p.15: [21] Zhang, H., Y. Yu, J. Jiao, et al. Theoretically principled trade-off between robustness and accuracy. in International conference on machine learning. 2019. PMLR.
- p.16: [40] E. Soares, P. Angelov, A large dataset of real patients CT scans for COVID-19 identification , Harv. Dataverse 1 (2020) 1–8.
- p.16: [41] P. Tschandl, C. Rosendahl, H. Kittler, The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions , Scientific
<!-- AI_READING_NOTE_END -->
