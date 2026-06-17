---
title: "Transforming medical imaging with Transformers? A comparative review of key properties, current progresses, and future perspectives"
authors:
  - "Jun Li"
  - "Junyu Chen"
  - "Yucheng Tang"
  - "Ce Wang"
  - "Bennett A. Landman"
  - "S. Kevin Zhou"
year: 2023
venue: "Medical Image Analysis (Elsevier)"
doi: 10.1016/j.media.2023.102762
pdf: [[Transforming-medical-imaging-with-Transformers--A-comparativ_2023_Medical-Im.pdf]]
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
extract_cache: .paper-cache/extracts/Transforming-medical-imaging-with-Transformers--A-comparativ_2023_Medical-Im.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/38 pages"
---
# Transforming medical imaging with Transformers? A comparative review of key properties, current progresses, and future perspectives

## 基本信息
- **PDF**: [[Transforming-medical-imaging-with-Transformers--A-comparativ_2023_Medical-Im.pdf]]
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`, `A2_医学图像_分类_配准_生成`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Transforming medical imaging with Transformers? A comparative review of key properties, current progresses, and future perspectives |
| **作者** | Jun Li; Junyu Chen; Yucheng Tang; Ce Wang; Bennett A. Landman; S. Kevin Zhou (前三位同等贡献) |
| **机构** | 中科院计算所智能信息处理重点实验室 / Johns Hopkins / Vanderbilt / 中国科学技术大学 MIRACLE |
| **发表时间** | 2023 (Available online 31 January 2023; 投稿 2022-06-02, 接收 2023-01-27) |
| **刊物/会议** | Medical Image Analysis 85 (2023) 102762, Elsevier — Survey paper |
| **DOI** | 10.1016/j.media.2023.102762 |

## 摘要

**英文原文 (据 PDF 提取文本整理, 已修复空格与连字符断裂)**:

> Transformer, one of the latest technological advances of deep learning, has gained prevalence in natural language processing or computer vision. Since medical imaging bears some resemblance to computer vision, it is natural to inquire about the status quo of Transformers in medical imaging and ask the question: can the Transformer models transform medical imaging? In this paper, we attempt to make a response to the inquiry. After a brief introduction of the fundamentals of Transformers, especially in comparison with convolutional neural networks (CNNs), and highlighting key defining properties that characterize the Transformers, we offer a comprehensive review of the state-of-the-art Transformer-based approaches for medical imaging and exhibit current research progresses made in the areas of medical image segmentation, recognition, detection, registration, reconstruction, enhancement, etc. In particular, what distinguishes our review lies in its organization based on the Transformer's key defining properties, which are mostly derived from comparing the Transformer and CNN, and its type of architecture, which specifies the manner in which the Transformer and CNN are combined, all helping the readers to best understand the rationale behind the reviewed approaches. We conclude with discussions of future perspectives.

**中文翻译**:

> Transformer 是深度学习近年的重要进展之一，已在自然语言处理和计算机视觉中广泛流行。由于医学影像与计算机视觉存在一定相似性，自然会追问 Transformer 在医学影像中的现状，并提出一个问题：Transformer 模型能否变革医学影像？本文尝试回应这一问题。我们首先简要介绍 Transformer 的基本原理，尤其是与卷积神经网络 (CNN) 的对比，并突出表征 Transformer 的关键定义属性；随后对面向医学影像的最新 Transformer 方法做全面综述，呈现其在医学图像分割、识别、检测、配准、重建、增强等领域的研究进展。本综述的独特之处在于：组织方式建立在 Transformer 的关键定义属性（多由 Transformer 与 CNN 的对比推导而来）及其架构类型（即 Transformer 与 CNN 的结合方式）之上，以帮助读者理解所综述方法背后的设计动机。最后讨论未来展望。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 据 EMC/IDC 报告，约 90% 的医疗数据是医学图像，是临床诊断与干预决策的关键证据来源。深度学习（尤其 CNN）已在医学图像分析中取得巨大成功——自 U-Net (Ronneberger et al., 2015) 赢得 2015 ISBI 细胞追踪挑战赛后，U-Net 及其变体一直是医学影像像素级任务的事实标准。但 CNN 存在固有局限。与此同时，Transformer (Vaswani et al., 2017) 在 NLP 中已蓬勃发展、在 CV 中正快速兴起，自然要追问：Vision Transformer 在医学影像中是否优于 CNN？Transformer 能否变革医学影像？
- **CNN 的核心局限**: CNN 普遍采用较小卷积核（如 3×3 或 5×5），其卷积操作的**局部性**使网络偏向学习局部空间结构，难以显式建模长距离依赖。已有大量扩大理论感受野 (RF) 的尝试：加深网络 (Simonyan & Zisserman, 2015)、引入循环/跳跃-残差连接 (He et al., 2016)、空洞卷积 (Yu & Koltun, 2016)、池化与上采样、级联或两阶段框架 (nnU-Net 等)。但 CNN 的浅层 RF 仍然有限，长距离依赖只能在深层隐式建模；且 Luo et al. (2016) 指出，随网络加深远处体素的影响迅速衰减，**有效感受野 (ERF) 实际远小于理论 RF**，即便理论 RF 已覆盖整幅图像。
- **核心矛盾**: 医学诊断不仅要关注病灶区域，还要考虑周围组织与器官（上下文）。CNN 的"局部性"偏置与医学图像理解所需的"全局性"上下文之间存在矛盾。Transformer 的自注意力天然擅长建模长距离依赖、拥有更大的有效感受野，有望弥合这一矛盾；但其计算量更大、数据需求更高，而医学影像常因患者隐私等因素导致资源/数据有限，构成新的现实挑战。
- **综述范围界定**: 本文明确将范围限定为 **Vision Transformer**；除非另行说明，文中"Transformer"/"Transformer-based"均指集成原始语言 Transformer 基本块、并应用于图像分析任务的 Vision Transformer。

## 关键贡献

1. **以"关键定义属性 + 架构类型"双视角组织综述**: 本文区别于其他综述之处在于——不是简单按任务罗列，而是根据 Transformer 的**关键定义属性**（多由与 CNN 的对比推导得出）以及**架构类型**（Transformer 与 CNN 的结合方式）来组织，帮助读者理解所综述方法背后的设计动机 (rationale)。
2. **全面的任务覆盖**: 系统回顾基于 Transformer 的 SOTA 方法在**医学图像分割、识别 / 分类、检测、配准、重建、增强**等多个任务上的研究进展。
3. **Transformer 与 CNN 的特性对比**: 详述自注意力与卷积的本质差异，涉及感受野、长距离依赖建模、可扩展性 (scalability)、对损坏的鲁棒性、归纳偏置等。
4. **未来方向探讨**: 讨论 Transformer 在医学影像中尚待解决的挑战与发展潜力（第 5 节）。

## 方法

本文是综述，其"方法"体现在**组织框架**与**所综述方法的关键原理**上。

- **整体框架**（论文第 1 节末明确给出）:
  - 第 2 节: CNN 在医学影像中的应用及其局限。
  - 第 3 节: Transformer 基础——一般原理、关键属性、与 CNN 的主要差异。
  - 第 4 节（主体）: 各任务的 SOTA Transformer 方法进展（分割、识别、分类、检测、配准、重建、增强）。
  - 第 5 节: 尚待解决的挑战与未来潜力。
- **自注意力机制 (Self-Attention, SA)**: 将输入 $X\in\mathbb{R}^{n\times c}$ 经三个可学习参数 $W_q, W_k, W_v\in\mathbb{R}^{c\times d}$ 线性映射为查询 $Q$、键 $K$、值 $V\in\mathbb{R}^{n\times d}$；注意力分布 $A=\mathrm{Softmax}(QK^\top/\sqrt{d})\in\mathbb{R}^{n\times n}$；输出 $Z=A\times V$。直觉上 $K$ 是"记忆"数据的嵌入矩阵、$Q$ 是查找向量，$A$ 连接所有元素，因而擅长建模 NLP/CV 中的长距离依赖。
- **多头自注意力 (MSA)**: 将 $Q,K,V$ 投影到多个子空间并行计算 SA，再拼接并经线性投影 $W_o\in\mathbb{R}^{hd\times c}$ 输出。注意：头数更多不必然带来更好性能 (Voita et al., 2019)。
- **Vision Transformer 流水线** (第 3.2 节):
  1. **非重叠分块**: 2D 图像 $X\in\mathbb{R}^{C\times H\times W}$ 切成 $N$ 个不重叠 patch；非重叠会部分破坏图像内部结构，但 MSA 跨 patch 整合信息可缓解，且无计算冗余。
  2. **块嵌入**: 每个 patch 向量化后线性投影成 token，嵌入维度 $D$。
  3. **位置编码**: Transformer 对位置不敏感，需加位置嵌入以保留 patch 相对全图的位置；位置嵌入同时是**人为引入的归纳偏置**。共三类——正弦 (sinusoidal)、可学习 (learnable)、相对 (relative)；前两者编码 1 到 patch 数的绝对位置，后者编码 patch 间的相对偏移。
  4. **Transformer 编码器**: $L$ 个基本块堆叠，每块含 MSA + MLP，配 LayerNorm 与残差连接：$Z'_l=\mathrm{MSA}(\mathrm{LN}(Z_{l-1}))+Z_{l-1}$，$Z_l=\mathrm{MLP}(\mathrm{LN}(Z'_l))+Z'_l$。
  5. **MLP**: 两层前馈网络中间夹激活（通常 GeLU），$\mathrm{MLP}(x)=\phi(xW_1+b_1)W_2+b_2$，权重维度通常设为 $D\times4D$ 与 $4D\times D$。由于作用在 token 上等价于 1×1 卷积，MLP 是高度局部且平移等变的，正好为缺乏归纳偏置的自注意力**注入归纳偏置**。
- **Transformer vs. CNN 的关键差异** (第 3.3 节):
  - **感受野**: CNN 感受野随深度逐步扩大，浅层与深层特征差异大、全局信息逐层注入；Transformer 自注意力在第一层即连接所有位置对，拥有更大的有效感受野。
  - **归纳偏置**: CNN 强归纳偏置（卷积的局部性、权重共享 = 强先验、平移等变）；Transformer 归纳偏置弱（仅 MLP 局部、位置编码人为注入），需依赖大模型 + 大数据发挥优势。
  - **可扩展性与鲁棒性**: Transformer 更易扩展到更大规模 (Liu et al., 2022e)，对图像损坏 (corruption) 更鲁棒 (Naseer et al., 2021)，弱归纳偏置使其在大规模模型与数据加持下可超越 CNN。
- **组织逻辑**: 第 4 节对各任务方法的回顾，并非简单按任务分类，而是**按这些方法如何利用/结合上述 Transformer 关键属性**来组织。

## 实验

本文作为综述论文，**本身不报告新的实验结果**，而是总结所综述文献的实验发现。

- **覆盖任务与典型数据集**: 文中按分割、识别 / 分类、检测、配准、重建、增强等任务综述方法。（据原文后续页 p.16-18，提取缓存未覆盖完整表格，待核）第 4.2 节"医学图像识别与分类"列出综述工作汇总表 (Table 2)，涉及架构、2D/3D、是否预训练、参数量、分类任务、模态、数据集等列；提及 IXI 数据集、组织病理 (histopathology) 分类数据集、SETMIL 处理全切片图像 (WSI)、i-ViT 用 171 张全切片中 1163 个 ROI 等。具体分割/检测/配准等任务的数值对比表格，提取文本（前 12 页）未覆盖，PDF 文本未明确给出统一数字对比。
- **对比基线与指标**: 各任务通常与当时 SOTA 的 CNN 方法（如 U-Net、nnU-Net 等）比较；指标随任务而异（分割常用 Dice、HD95 等）——此为领域常识性归纳，提取文本前 12 页未给出具体数字。
- **综述发现**: 现有研究表明 Transformer 在捕获长距离依赖、理解上下文方面展现潜力，在多种医学影像任务上取得有竞争力的性能；但在计算效率、数据需求方面仍有挑战。

## 局限

1. **时效性**: 论文 2022-06 投稿、2023-01 接收，文献截至 2023 年初；Transformer 医学影像领域发展极快，之后有大量新工作（如各类基础模型 / SAM 类方法）未被覆盖。
2. **方法深度的权衡**: 作为综述，对单个方法的介绍难以替代对原文的精读。
3. **挑战讨论的落地性**: 虽指出 Transformer 计算量大、数据需求高，但对小样本、隐私计算等实际医学场景下的具体应对，讨论可进一步深入（第 5 节细节超出提取文本覆盖范围，待核）。
4. **缺乏统一实验平台**: 综述无法在统一平台上对各方法做公平、全面的对比。

## 个人评论

这篇论文最大的价值在于其**系统性的梳理和深刻的对比视角**：它不止罗列方法，而是抓住 Transformer 与 CNN 最根本的两组差异——**全局建模 vs 局部建模**、**弱归纳偏置 vs 强归纳偏置**——并以此为线索组织文献。几个值得带走的启发：

1. **做研究 / 改模型**: 设计新模型时，先问"这个任务里 CNN 的瓶颈是不是来自局部性"。若答案是"需要跨区域关联的结构"，则 Transformer 的长距离建模能力才真正有用武之地；否则混合架构 (Hybrid CNN-Transformer) 往往是性能与效率的更优折中——本文把"Transformer 与 CNN 如何结合"单列为一条组织维度，正暗示纯 Transformer 在医学影像里很少是最优解。
2. **写论文 / Related Work**: 第 2-3 节对 CNN 局限（理论 RF vs 有效 RF、Luo et al. 2016 的体素影响衰减）与 Transformer 优势的论述清晰、引用扎实，是写动机段与综述段的极佳模板。
3. **做实验**: 它提醒评估 Transformer 时不能只看指标，还要看有效感受野的实际变化、对数据规模的依赖、以及计算开销——尤其在医学影像这种"数据少、隐私强"的场景里，弱归纳偏置可能反成劣势。
4. **一个保留意见**: 标题用了问号"can Transformers transform medical imaging?"，但提取到的前 12 页里作者的回答仍偏开放（"At the present stage, it is uncertain..."）。读者应把它当作"现状盘点 + 设计原理梳理"，而非"Transformer 必胜"的结论性背书。

### 使用建议

- **快速了解领域**: 读摘要、引言（第 1 节）、以及挑战与未来（第 5 节），快速把握全貌、动机与趋势。
- **复现 / 深入学习**: 想复现某类方法（如医学图像分割），重点读第 4 节对应任务小节 + 第 3 节 ViT 实现细节，再顺引用去精读目标论文。
- **借鉴创新点**: 学习第 3 节对关键属性的分析，以及第 4 节方法如何结合这些属性（如为医学图像特性设计位置编码、设计轻量注意力模块）。
- **写 Related Work**: 本文是该领域核心综述，可直接作为引用锚点并借鉴其论述逻辑。

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
综述论文 (Survey paper)，发表于医学图像分析顶刊《Medical Image Analysis》(2023, vol.85, 102762)，由中科院计算所、Johns Hopkins、Vanderbilt、中科大 MIRACLE 联合完成（前三位作者同等贡献，通讯作者 S. Kevin Zhou）。主题是**医学图像分析中 Vision Transformer 的应用与进展**，核心问句"Transformer 能否变革医学影像 (can the Transformer models transform medical imaging?)"。因为它本质是综述，主题归在 `R_综述_Survey`；又因覆盖医学图像分割/分类/配准/重建/增强等子任务，与 `A2_医学图像_分类_配准_生成` 强相关，故作为次要主题保留。

## 2. 一句话总结
这篇综述以"Transformer 与 CNN 的关键定义属性差异 + 二者结合的架构类型"双视角组织文献，系统回顾 Vision Transformer 在医学图像分割、识别/分类、检测、配准、重建、增强等任务上的进展，并展望未来挑战。

## 3. 背景与问题
- **为什么要做**: 约 90% 医疗数据为医学图像 (EMC/IDC)，深度学习尤其 CNN 已成主力（U-Net 自 2015 ISBI 挑战赛后成为像素级任务事实标准）。但 Transformer 在 NLP/CV 中崛起后，是否、以及如何优于 CNN 用于医学影像理解，尚不清楚。
- **CNN 的局限**: 小卷积核 (3×3/5×5) 带来局部性偏置，难以显式建模长距离依赖；尽管有加深网络、空洞卷积、池化、级联等扩大理论 RF 的手段，但浅层 RF 仍受限，深层 RF 只能隐式建模依赖，且 Luo et al.(2016) 表明远处体素影响随深度迅速衰减，**有效感受野远小于理论感受野**。
- **核心矛盾**: 医学诊断需兼顾病灶与周围组织/器官（全局上下文），与 CNN 局部性偏置冲突；Transformer 自注意力有更大有效感受野，但计算量大、数据需求高，而医学数据常因隐私受限——优势与现实约束并存。
- **范围**: 全文限定 Vision Transformer。

## 4. 核心贡献
1. **双视角组织框架**: 按"关键定义属性"（多由 Transformer vs CNN 对比导出）与"架构类型"（Transformer 与 CNN 结合方式）组织综述，凸显方法的设计动机，区别于按任务平铺的常规综述。
2. **任务覆盖广**: 分割、识别/分类、检测、配准、重建、增强全覆盖。
3. **特性对比清晰**: 系统对照感受野、归纳偏置、可扩展性、鲁棒性、长距离依赖建模等维度。
4. **未来展望**: 讨论挑战与发展潜力（第 5 节）。

## 5. 方法详解
（综述的"方法"= 组织框架 + 所综述方法的原理，下述公式与细节均来自第 3 节）
- **自注意力 SA**: $X\in\mathbb{R}^{n\times c}\to Q,K,V\in\mathbb{R}^{n\times d}$（经 $W_q,W_k,W_v\in\mathbb{R}^{c\times d}$）；$A=\mathrm{Softmax}(QK^\top/\sqrt d)\in\mathbb{R}^{n\times n}$；$Z=A\times V$。$A$ 连接所有元素 → 长距离依赖建模能力。
- **多头 MSA**: 多子空间并行 SA，拼接后经 $W_o\in\mathbb{R}^{hd\times c}$ 投影；头数越多≠越好 (Voita et al., 2019)。
- **ViT 流水线**: ① 非重叠分块（破坏部分内部结构但 MSA 可缓解、无计算冗余）；② patch 向量化 + 线性投影成 token（维度 $D$）；③ 位置编码（正弦/可学习/相对三类；既保留位置又作为人为注入的归纳偏置）；④ 编码器 $L$ 块堆叠，每块 MSA+MLP+LN+残差，公式 $Z'_l=\mathrm{MSA}(\mathrm{LN}(Z_{l-1}))+Z_{l-1}$、$Z_l=\mathrm{MLP}(\mathrm{LN}(Z'_l))+Z'_l$；⑤ MLP 两层前馈夹 GeLU，维度 $D\!\times\!4D$/$4D\!\times\!D$，作用于 token 等价 1×1 卷积，是局部+平移等变的，为自注意力**补足归纳偏置**。
- **Transformer vs CNN**（第 3.3 节）: CNN 感受野逐层扩大、强归纳偏置（局部性、权重共享、平移等变）；Transformer 第一层即全局连接、归纳偏置弱、更易扩展 (Liu et al., 2022e)、对损坏更鲁棒 (Naseer et al., 2021)，在大模型+大数据下可超越 CNN (Dosovitskiy et al., 2020; Zhai et al., 2022)。
- **第 4 节组织逻辑**: 按方法如何利用/结合上述属性归类，而非简单按任务平铺。

## 6. 实验与结果
综述本身**不含新实验**，总结文献发现。
- 第 4 节按任务综述方法；据原文后续页（p.16-18，提取缓存未覆盖完整内容，待核），4.2 节"识别与分类"含汇总表 Table 2（架构/2D-3D/预训练/参数量/分类任务/模态/数据集等列），提及 IXI 数据集、组织病理分类数据集、SETMIL 处理 WSI、i-ViT 用 171 张全切片中 1163 个 ROI 等。
- 分割等任务的具体数值对比（Dice、HD95 及与 U-Net/nnU-Net 的对照）属领域常识性归纳，提取文本（前 12 页）未给出具体数字，PDF 文本未明确统一对比表。
- 总体发现: Transformer 在长距离依赖与上下文理解上有潜力、性能有竞争力；计算效率与数据需求仍是挑战。

## 7. 这篇论文真正有价值的地方
价值在于**对比视角下的设计原理梳理**，而非方法清单。作者把"全局 vs 局部建模""弱 vs 强归纳偏置"提炼为组织主线，再叠加"Transformer 与 CNN 如何结合"的架构维度，使读者能从动机层面理解每类方法为何这样设计。对后续研究者的三点启发：(1) 先判断任务瓶颈是否真来自 CNN 局部性，再决定是否上 Transformer / 混合架构；(2) 第 2-3 节是写动机与 Related Work 的优质模板（理论 RF vs 有效 RF、体素影响衰减等论据扎实）；(3) 评估 Transformer 要看有效感受野、数据依赖、计算开销，而非只看指标。

## 8. 局限与问题
1. **时效性**: 投稿 2022-06、接收 2023-01，截至 2023 初；之后大量新工作（基础模型/SAM 类）未覆盖。
2. **深度权衡**: 综述难替代单篇精读。
3. **挑战落地性**: 对小样本、隐私计算等实际场景的具体应对讨论可更深入（第 5 节细节超出提取覆盖，待核）。
4. **无统一实验平台**: 无法对各方法做公平统一对比。
5. **结论开放**: 提取到的前 12 页中作者对"能否变革"仍持开放态度（"it is uncertain..."），应视作现状盘点而非结论性背书。

## 9. 我该怎么使用这篇论文
- **快速了解领域**: 读摘要 + 引言（第 1 节）+ 挑战与未来（第 5 节）。
- **复现/深入**: 精读第 4 节对应任务小节 + 第 3 节 ViT 细节，再顺引用查原始论文。
- **借鉴创新点**: 学第 3 节属性分析与第 4 节"属性结合"思路（如位置编码适配医学图像、轻量注意力模块）。
- **写 Related Work**: 作为领域核心综述引用并借鉴其论述逻辑。

## 10. 和其他论文的关系
- 作为综述，引用大量奠基/代表工作：基础模型 ViT (Dosovitskiy et al., 2020)、原始 Transformer (Vaswani et al., 2017)、BERT/GPT（语言侧）；CNN 侧 U-Net (Ronneberger et al., 2015)、nnU-Net (Isensee et al., 2021)、FCN (Long et al., 2015)、ResUNet+RNN (Alom et al., 2018)、Distance-LSTM (Gao et al., 2019a) 等。
- 与本库主题相关:
  - `[[R_综述_Survey]]`（本文为综述，主归类）。
  - `[[A2_医学图像_分类_配准_生成]]` 下的医学图像分割/分类/配准/重建 Transformer 方法（如 TransUNet、Swin-UNETR、nnFormer 等，若库内有对应笔记可建立链接）。
  - 注意力/混合架构方向的方法论文。

## 11. 关键词
Transformer, Vision Transformer, 医学图像分析, 综述/Survey, 自注意力, 多头自注意力, 卷积神经网络, 感受野/有效感受野, 长距离依赖, 归纳偏置, 位置编码, 混合架构

## 12. 可信度说明
本精读笔记主要基于 PDF 提取文本前 12 页（共 38 页；提取缓存截断于 25000 字符，覆盖至第 3.3 节 Transformer vs CNN）。该范围内文本质量好、连贯，含标题、摘要、引言、第 2 节 CNN 背景与局限、第 3 节 Transformer 基础原理（SA/MSA/ViT 流水线/位置编码/MLP/与 CNN 对比）等核心内容，相关描述准确可靠。第 4 节各任务方法综述与第 5 节结论的细节超出主提取范围；笔记中涉及 p.13-18 的少量信息（Table 2、IXI/组织病理数据集、SETMIL、i-ViT 等）来自原笔记"全文补读记录"摘录，已标注"据原文后续页，提取缓存未覆盖，待核"。全部内容严格依据文本，未编造数字或数据集。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/Transforming-medical-imaging-with-Transformers--A-comparativ_2023_Medical-Im.txt` (主提取 12/38 页, 截断于 25000 字符; 原 AI 主体 12/38 + 全文补读 13-38); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮 (2026-06-18) 重读优化基于提取文本前 12 页校核。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-38; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-38。
- **提取情况**: 缺失页 26 页, 其中 26 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Medical Image Analysis 85 (2023) 102762
- p.13: ViT in medical image segmentation, several works are proposed to
- p.15: The pre-training framework employs multi-task self-supervised learn-
- p.15: Segmentation Transformers for different imaging modalities: Medical
- p.15: 4.2. Medical image recognition and classification
- p.15: ViT is able to surpass convolutional inductive bias by learning the
- p.15: ViT over CNN with the aid of a large model size and pre-training
- p.15: These appealing properties have sparked an increasing interest in
- p.15: Hybrid model: The earliest use of ViTs for medical image classifi-
- p.15: The features extracted from multiple images of the same patient are
- p.15: SETMIL begins by embedding the large-sized whole slide image (WSI)
- p.15: Then, low-resolution embeddings are subjected to a Transformer-based

### 缺失页关键摘录

- p.13: supervised dataset, raw medical images without expert annotation are
- p.15: lenge dataset designed for general purpose segmentation tools, contains
- p.15: evaluation. Among a large number of methods, researchers attempt
- p.15: large-scale datasets. Indeed, as a result of their weaker inductive bias,
- p.15: Liu et al., 2021a; Bao et al., 2021). As a result of this discovery, many
- p.15: classification and also list the reviewed works in Table 2.
- p.15: dataset using the Probabilistic Class Activation Map (PCAM) pooling
- p.16: Reference Architecture 2D/3D Pre-training #Param Classification task Modality Dataset Highlights
- p.17: ahttps://brain-development.org/ixi-dataset/.
- p.18: several benchmark histopathology image classification datasets and
- p.18: the i-ViT using a dataset of 1163 ROIs/pictures taken from 171 whole
- p.18: of baseline methods in terms of classification accuracy. Likewise, Yu
<!-- AI_READING_NOTE_END -->
