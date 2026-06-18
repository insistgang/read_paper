---
title: Medical image classification by incorporating clinical variables and learned features
authors:
  - "Jiahui Liu"
  - "Xiaohao Cai"
  - "Mahesan Niranjan"
year: 2025
venue: Royal Society Open Science
doi: 10.1098/rsos.241222
pdf: [[医学图像分类 Medical Classification.pdf]]
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
extract_cache: .paper-cache/extracts/医学图像分类 Medical Classification.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# Medical image classification by incorporating clinical variables and learned features

## 基本信息
- **PDF**: [[医学图像分类 Medical Classification.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Medical image classification by incorporating clinical variables and learned features |
| **作者** | Jiahui Liu; Xiaohao Cai; Mahesan Niranjan（英国南安普顿大学 School of Electronics and Computer Science） |
| **发表时间** | 2025（Received 19 Jul 2024, Accepted 15 Dec 2024） |
| **刊物/会议** | Royal Society Open Science, 12: 241222 |
| **DOI** | 10.1098/rsos.241222 |
| **代码** | https://gitfront.io/r/Rachel/mGKvf81UJVr9/Incorporating-Clinical-Variables |

## 摘要

**英文原摘要（据 PDF 提取文本整理，已修复断词与空格）**：

> Medical image classification plays an important role in medical imaging. In this work, we present a novel approach to enhance deep learning models in medical image classification by incorporating clinical variables without overwhelming the information. Unlike most existing deep neural network models that only consider single-pixel information, our method captures a more comprehensive view. Our method contains two main steps and is effective in tackling the extra challenge raised by the scarcity of medical data. Firstly, we employ a pre-trained deep neural network served as a feature extractor to capture meaningful image features. Then, an exquisite discriminant analysis is applied to reduce the dimensionality of these features, ensuring that the low number of features remains optimized for the classification task and striking a balance with the clinical variables information. We also develop a way of obtaining class activation maps for our approach in visualizing models' focus on specific regions within the low-dimensional feature space. Thorough experimental results demonstrate improvements of our proposed method over state-of-the-art methods for tuberculosis and dermatology issues for example. Furthermore, a comprehensive comparison with a popular dimensionality reduction technique (principal component analysis) is also conducted.

**中文翻译**：

> 医学图像分类在医学影像中扮演重要角色。本文提出一种新方法，在不让信息被"淹没"的前提下，把临床变量引入深度学习模型以增强医学图像分类。与多数仅考虑单一像素信息的深度网络不同，本方法获取了更全面的视角。方法包含两个主要步骤，能有效应对医学数据稀缺带来的额外挑战：第一步，用一个预训练深度网络作为特征提取器来获取有意义的图像特征；第二步，用一种精巧的判别分析（DA）对这些特征降维，使少量特征仍然对分类任务保持最优，并与临床变量信息取得平衡。我们还为本方法开发了一种获取类激活图（CAM）的方式，用于可视化模型在低维特征空间中对特定区域的关注。充分的实验结果表明，本方法在如肺结核、皮肤病等不同疾病分类上优于现有先进（SOTA）方法；此外还与常用降维技术主成分分析（PCA）做了全面对比。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：临床实践中放射科医生工作负荷极高——文中称放射科医生平均需在 3–4 秒内解读一张影像、每天工作 8 小时，疲劳会显著抬升错误率。同时影像解读高度依赖临床上下文：一项面向放射科医生的调查中，压倒性多数（87%，文中引用 [8]）表示临床信息在其解读过程中起重要作用。X 光等影像征象本身往往是**非特异性的**（同样的胸片表现，配合发热+白细胞升高可能提示肺炎，缺少这些支撑则可能是肺不张、肺水肿甚至肺癌），需要结合临床/化验数据才能准确诊断。
- **之前方法的问题**：早期医学图像分析的深度模型多把任务当作**单像素模态**问题，未纳入临床信息，限制了临床转化（文中引用 [11–13]）。已有的融合工作方法较简单：Kharazmi 等 [21] 用稀疏自编码器提取特征、再经池化层降维后与患者资料（病灶位置、大小、隆起、年龄、性别）拼接送 softmax，但未训练的特征 + 仅靠池化降维（无标签信息、无损失更新）效果不佳且可能丢信息；Yap 等 [22] 把图像送入去掉最后一层的 ResNet50，得到 **1024 维**特征后直接与元数据（年龄、性别、身体部位）拼接，由于图像特征维度本就很高，少量元数据被"淹没"，**提升不足 1% 且不稳定**；Spasov 等 [25] 在阿尔茨海默病分类上用 CNN 融合 3D 结构 MRI 与临床评估，思路类似。
- **核心矛盾**：医学数据稀缺（采集成本高、标注费力、涉及隐私），可用样本数 N 常常**与甚至小于**预训练特征维度 M（典型 1024/2048），直接在高维特征上拼接少量临床变量会带来维度灾难、过拟合和信息失衡，临床变量的作用被掩盖。本文主张：先对高维特征做**保留判别性的降维**，为临床变量"腾出空间"。

## 关键贡献

1.  **两步式融合框架**：预训练深度网络（如 ResNet18、ViT）提取图像特征 + 判别分析（DA）降维，使临床变量得以在平衡的维度上融入，专门应对医学数据稀缺场景。
2.  **用判别分析（DA）替代 PCA 做降维**：DA 是**有监督**降维，最小化类内散度、最大化类间散度（Fisher 准则），在低维表示中保留判别信息；文中采用 Foley & Sammon [19] 的方法，通过向量正交性递归求出**多个**最优判别方向，克服了传统二分类判别只能得到一个投影方向（受类间散度矩阵秩限制）的局限。
3.  **为降维特征量身开发的类激活图（CAM）**：标准 CAM 流水线无法直接可视化降维后的特征，本文针对预训练 CNN、用一个全连接层 ϕ\* 作为分类器来求权重，给出可在低维特征空间上生成 CAM 的方法（文中称这是此前未被探索的贡献）。
4.  **在真实医学任务上验证并与 PCA 系统对比**：以肺结核、皮肤病等分类为例证明优于 SOTA，并与常用降维方法 PCA [20] 做了全面对比。

## 方法

- **整体框架**（图 1）：从左到右为 `预训练网络提取特征 → DA 降维得到子空间表示 → 与临床变量融合（临床变量也可先嵌入到另一空间）→ 分类器（SVM 或全连接层）输出预测`。
- **输入输出**：输入医学图像 `I_i` 及其对应的 `L_cv` 维临床变量向量 `v_i`；输出疾病类别预测。
- **关键模块**：
    1.  **预训练特征提取器 ϕ**：使用在 ImageNet 上预训练的网络（ResNet18 / VGGNet / ViT），**不微调**。图像被映射到倒数第二个全连接层维度 M 的特征空间，`y_i = ϕ(I_i)`。文中指出常见架构该层维度为 **1024 或 2048**；图 1 图注另举例特征维度为 512 / 4096（依模型而定）。由于数据稀缺，N 常与 M 相当甚至更小，必须降维。
    2.  **判别分析（DA）降维**：用投影矩阵 `P = (d_1, …, d_L)^T ∈ ℝ^{L×M}, L≪M`（式 3.1）把 `y_i` 投到低维，`ȳ_i = P y_i ∈ ℝ^L`（式 3.2）。二分类下记 `S_B = s_b s_b^T`、`S_W = β S_{W1} + (1−β) S_{W2}`，其中 `s_b = ȳ_1 − ȳ_2`、`β = (N_2−1)/(N_1+N_2−2)`（式 2.1）。Fisher 准则 `R(d) = d^T S_B d / d^T S_W d`（式 2.2），首个方向 `d_1 = α_1 S_W^{-1} s_b`（式 2.3），第二个方向在与 d_1 正交约束下用拉格朗日乘子求得（式 2.4–2.5），并可递归推广到第 n 个方向（式 2.6–2.7），从而得到不受 S_B 秩限制的一组判别方向 `{d_k}`。
    3.  **特征融合（两种策略）**：
        - **策略一（直接拼接）**：`z_i = (ȳ_i^T, v_i^T)^T ∈ ℝ^{L+L_cv}`（式 3.3）。
        - **策略二（先嵌入再降维）**：先用 BERT [27] 等基础模型把临床变量文本编码为嵌入，对嵌入再做 DA 降维得到 `v̄_i`，然后 `z_i = (ȳ_i^T, v̄_i^T)^T`（式 3.4）。文中明确：本数据集的临床变量文本（如性别、肤色）重复且缺乏多样性，BERT 可能不会显著提升性能；只有当文本信息更丰富多样时，策略二才被假设能带来收益。
    4.  **分类器**：融合特征 `z_i` 送入 SVM 或全连接层做最终预测。
- **降维特征上的 CAM**：传统 CAM 把全局平均池化输入与分类层权重相乘生成各类注意力图，无法直接用于降维特征。本文针对预训练 CNN，用全连接层 ϕ\*（代替 SVM）作分类器来获取权重；设最后一个卷积层输出特征图 `F ∈ ℝ^{M×H×W}`（如 ResNet18 为 512×7×7），将通道维特征图展平为 `ℝ^{M×(H·W)}` 后据此构造可叠加到原图的低维特征 CAM。（CAM 完整推导位于提取缓存截断处之后，据原文后续页，提取缓存未覆盖，待核。）
- **训练方式**：预训练网络**冻结**，仅在训练集上学习 DA 投影矩阵 `P` 和分类器（SVM / 全连接层）。
- **与已有方法的差异**：核心区别是用**有监督的 DA** 取代池化 [21,23,24] 或 PCA [18] 这类无监督/无标签的降维——DA 利用类别标签让低维子空间对分类最优，同时把维度压到 L≪M，避免临床变量被高维特征淹没。

## 实验

> 注：提取缓存仅覆盖到方法/CAM 章节（约前 12 页），实验（§4）、讨论与结论（§5）多数内容未进入提取文本，以下结合摘要、引言陈述与全文补读线索整理。

- **任务与数据集**：以**肺结核（tuberculosis）** 和**皮肤病（dermatology）** 分类为例。补读线索显示用到 **ChestX-ray8** 数据集（图 3 在其上展示带边界框信息的 CAM 可视化）以及皮肤病数据集 **PAD-UFES-20**（Pacheco 等 2020，参考文献 [33]，由智能手机采集的皮损图像 + 患者数据）。具体规模、划分、临床变量项清单在提取文本中未给出（据原文后续页/表格，提取缓存未覆盖，待核）。
- **对比方法**：核心对比是 **DA vs PCA** [20] 的全面比较；引言亦将本方法对标只用图像特征或简单拼接临床变量的已有融合方法（[21,22] 等）。
- **评价指标**：摘要称 "thorough experimental results"，但提取文本未列出具体指标（准确率/AUC 等）与数值（PDF 文本未明确，据原文后续页，提取缓存未覆盖，待核）。
- **主结果**：摘要与引言反复声明本方法在肺结核、皮肤病分类上"优于 SOTA"，并通过与 PCA 对比"进一步印证其优越性能"；具体提升幅度在提取文本中未找到（待核）。
- **消融/泛化**：在两个不同疾病领域上验证体现一定泛化性；是否有系统消融实验在提取文本中未明确（PDF 文本未明确）。
- **可解释性结果**：补读线索（p.13–14）显示，CAM 可视化用于验证模型确实关注与疾病/边界框对齐的区域；文中讨论强调目标不是单纯刷基准精度，而是优先考虑临床诊断中的实用性。
- **效率信息**：速度、参数量、FLOPs 等在提取文本中未找到。

## 局限

1.  **实验细节缺口（受限于提取覆盖）**：提取缓存未含完整 §4，因此具体指标数值、消融设置、各数据集临床变量清单无法从提取文本量化核实；需对照原文后续页与开源代码确认。
2.  **CAM 不直接反映临床变量影响**：补读线索（p.13）明确提到 "CAMs in our current approach do not directly visualize the influence of the clinical variables"——即可视化仍主要解释图像通路，临床变量这一支的贡献未被 CAM 直接呈现，是方法可解释性上的已知短板。
3.  **对临床变量性质的依赖**：方法收益依赖临床变量与图像特征在 DA 子空间中能互补。文中自陈当前数据集临床变量文本重复、缺乏多样性，导致策略二（BERT 嵌入）难以显效；若临床变量噪声大或与图像强相关，收益亦可能有限。
4.  **特征提取器全程冻结、不做领域自适应**：以 ImageNet 预训练网络直接提取特征、不微调，虽降低过拟合与算力开销，但可能无法捕捉医学图像特有的细微模式，是进一步提升的瓶颈。

## 个人评论

1.  **抓住"维度失衡"这一真实痛点**：在 N≈M 甚至 N<M 的医学小数据场景里，"先有监督降维再融合元数据"比"高维直接拼接"更合理，论文把这一直觉做成了可操作的 DA 框架，对任何"高维深度特征 + 低维结构化辅助信息"的融合任务都有迁移价值。
2.  **DA 替代 PCA 的选择有原理支撑**：用 Foley & Sammon 的正交递归判别方向，既解决了二分类判别只能得一个方向的老问题，又保留了类别可分性，比无监督 PCA 在分类目标上更对口；论文用系统对比而非单点结果来支撑这一选择，说服力较强。
3.  **务实大于刷榜**：冻结预训练网络、只训练轻量 DA + 分类器，是数据稀缺约束下降低过拟合与成本的现实策略；文中也明确把"临床可用性"置于"基准精度"之上，这种取向在医疗 AI 中值得肯定。
4.  **可解释性诚实但未闭环**：开发降维特征上的 CAM 是亮点，但作者自己点明 CAM 不直接可视化临床变量的影响——多模态融合模型"解释了哪一支"这个问题仍然开放，是后续值得补的工作。

### 使用建议

- **如果快速了解**：读**摘要** + **引言最后两段**（阐明方法）+ **图 1**，即可掌握"预训练特征 → DA 降维 → 融合临床变量 → 分类"的核心范式。
- **如果复现**：重点读 **§3 Proposed method** 框架描述 + **§2.2 判别分析公式（式 2.1–2.7）** 与**两种融合策略（式 3.3、3.4）**，并结合开源代码确认数据预处理、临床变量项与 DA 超参（这些在提取文本中未给全）。
- **如果借鉴创新点**：
    - 直接复用 **"预训练特征提取 + 判别分析降维 + 元数据融合"** 范式到其他"图像 + 结构化元数据"的分类任务；
    - 借鉴**为降维/新特征空间设计 CAM** 的思路增强可解释性；
    - 学习其**与 PCA 等基线做系统性对比**的实验设计。
- **如果写 related work**：可放入"**医学图像多模态融合（图像 + 临床/元数据）**"或"**深度特征降维与可解释性**"小节。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于医学图像分析与机器学习的交叉方向，解决**医学图像分类**中如何把临床上下文（患者信息、病史、既往诊断、化验值等）与从图像提取的深度特征**有效且平衡地**融合的问题。核心思路：预训练深度网络作固定特征提取器 → 用判别分析（DA）对高维特征做**有监督降维** → 再与临床变量融合 → 用 SVM 或全连接层分类。属于主题 `A2_医学图像_分类_配准_生成` 下的医学图像分类子方向。

## 2. 一句话总结
用预训练网络提特征、判别分析（DA）有监督降维、再与临床变量融合的两步框架，在医学小数据下避免高维图像特征"淹没"临床信息，并配套低维特征 CAM 可视化；在肺结核、皮肤病分类上优于 SOTA 且系统性优于 PCA。

## 3. 背景与问题
- **为什么做**：放射科医生需在 3–4 秒内读一张影像、每天 8 小时，疲劳推高错误率；且影像征象本身**非特异**，准确诊断高度依赖临床/化验上下文（调查中 87% 放射科医生认为临床信息对解读重要，[8]）。早期深度模型多只用像素单模态，限制临床转化。
- **之前方法的问题**：已有融合工作方法简单——池化降维后拼接（Kharazmi [21]，无标签、无损失更新易丢信息）、ResNet50 取 1024 维后直接拼元数据（Yap [22]，提升 <1% 且不稳定）、CNN 融合 MRI + 临床评估（Spasov [25] 阿尔茨海默）。这些做法让少量临床变量被高维图像特征淹没。
- **核心矛盾**：医学数据稀缺使样本数 N 与特征维度 M（1024/2048）相当甚至更小 → 高维直接融合会过拟合、信息失衡。本文主张先做保留判别性的降维。

## 4. 核心贡献
1.  **两步框架**：预训练网络（ResNet18/ViT 等）特征提取 + DA 降维，为临床变量融入创造平衡条件，专门应对数据稀缺。
2.  **DA 取代 PCA 做有监督降维**：最小化类内散度、最大化类间散度（Fisher 准则）；用 Foley & Sammon [19] 的正交递归法求多个判别方向，突破传统二分类只得一个方向的秩限制。
3.  **降维特征上的 CAM**：标准 CAM 无法直接用于降维特征，本文针对预训练 CNN、以全连接层 ϕ\* 作分类器求权重，给出可在低维特征空间生成 CAM 的方法（自称为此前未探索的贡献）。
4.  **真实任务验证 + 与 PCA 全面对比**：以肺结核、皮肤病为例优于 SOTA，并系统对比 PCA [20]。代码开源。

## 5. 方法详解
- **整体框架（图 1）**：`图像 → 冻结预训练网络 ϕ → 高维特征 y_i → DA 投影 P → 低维 ȳ_i → 与临床变量 v_i 融合 → z_i → SVM/全连接层 → 预测`。
- **特征提取**：`y_i = ϕ(I_i)`，ϕ 为 ImageNet 预训练网络（ResNet18/VGGNet/ViT），**不微调**；M 为倒数第二个全连接层维度（常见 1024/2048，图 1 图注举例 512/4096）。
- **DA 降维（§2.2 公式）**：`P = (d_1,…,d_L)^T ∈ ℝ^{L×M}, L≪M`（式 3.1），`ȳ_i = P y_i`（式 3.2）。二分类下 `S_B = s_b s_b^T`、`S_W = β S_{W1}+(1−β)S_{W2}`，`s_b = ȳ_1−ȳ_2`、`β=(N_2−1)/(N_1+N_2−2)`（式 2.1）；Fisher 准则 `R(d)=d^T S_B d / d^T S_W d`（式 2.2）；`d_1 = α_1 S_W^{-1} s_b`（式 2.3），d_2 在与 d_1 正交下经拉格朗日乘子求解（式 2.4–2.5），递归至第 n 个方向（式 2.6–2.7），得到不受 S_B 秩约束的 `{d_k}`。
- **两种融合策略**：策略一直接拼接 `z_i=(ȳ_i^T, v_i^T)^T ∈ ℝ^{L+L_cv}`（式 3.3）；策略二先用 BERT [27] 把临床文本嵌入再 DA 降维得 v̄_i，拼成 `z_i=(ȳ_i^T, v̄_i^T)^T`（式 3.4）。作者指出本数据集临床文本（性别、肤色）重复、缺多样性，BERT 难显效，仅假设文本更丰富时策略二有益。
- **降维特征 CAM（§3.2）**：以全连接层 ϕ\* 作分类器求权重；最后卷积层特征图 `F ∈ ℝ^{M×H×W}`（ResNet18 为 512×7×7），展平为 `ℝ^{M×(H·W)}` 后构造可叠加原图的 CAM（完整推导在提取缓存截断处之后，据原文后续页待核）。
- **训练**：预训练网络冻结，仅训练 DA 投影 P 与分类器（SVM/FC）。

## 6. 实验与结果
> 提取缓存覆盖至 §3（CAM）即截断，§4 实验、§5 结论多数未进入提取文本；以下据摘要/引言陈述 + 全文补读线索，数值待核。
- **数据集**：肺结核、皮肤病分类；补读线索显示用到 **ChestX-ray8**（图 3 带边界框 CAM）与皮肤病数据集 **PAD-UFES-20**（[33]）。规模/划分/临床变量清单提取文本未给（据原文后续页待核）。
- **对比方法**：核心是 **DA vs PCA** [20] 全面比较；并对标只用图像或简单拼接的已有融合方法。
- **指标与数值**：摘要称 "thorough experimental results" 并声明优于 SOTA，但提取文本未列具体指标（准确率/AUC）与提升幅度（PDF 文本未明确，待核）。
- **可解释性结果**：补读线索（p.13–14）显示 CAM 验证模型关注与疾病/边界框对齐的区域；讨论强调优先临床实用性而非单纯刷基准精度。
- **消融/效率**：是否系统消融、速度/参数量/FLOPs 在提取文本中均未明确。

## 7. 这篇论文真正有价值的地方
1.  **"先有监督降维、再融合元数据"** 是对多模态维度失衡痛点的优雅解法，可迁移到任何"高维深度特征 + 低维辅助信息"的融合任务。
2.  **DA 的选择有原理支撑**：正交递归判别方向既破除二分类只得一个方向的限制，又在分类目标上比无监督 PCA 更对口，并用系统对比而非单点结果佐证。
3.  **务实导向**：冻结预训练网络、只训练轻量 DA + 分类器，契合医学小数据约束；明确把临床可用性置于基准精度之上。
4.  **可解释性尝试但诚实**：为降维特征开发 CAM 是亮点，作者也坦承 CAM 不直接可视化临床变量影响，留下了"多模态解释哪一支"的开放问题。

## 8. 局限与问题
1.  **实验细节缺口**：受提取覆盖所限，指标数值、消融、各数据集临床变量清单无法据提取文本量化核实，需对照原文后续页与代码。
2.  **CAM 不直接反映临床变量影响**（p.13 补读线索明确指出），是已知可解释性短板。
3.  **依赖临床变量性质**：当前数据集临床文本重复、缺多样性致策略二难显效；变量噪声大或与图像强相关时收益受限。
4.  **特征提取器全程冻结**：不做领域自适应/微调，可能漏掉医学图像细微模式，是进一步提升的瓶颈。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言末两段 + 图 1。
- **复现**：§3 框架 + §2.2 判别分析公式（式 2.1–2.7）+ 融合策略（式 3.3/3.4），结合开源代码补齐预处理/超参/临床变量项。
- **借鉴创新点**：复用"预训练特征 + DA 降维 + 元数据融合"范式；借鉴为新特征空间设计 CAM 的思路；学习与 PCA 系统对比的实验设计。
- **写 related work**：归入"医学图像多模态融合（图像 + 临床/元数据）"或"深度特征降维与可解释性"。

## 10. 和其他论文的关系
- 直接对标的融合工作：Kharazmi 等 [21]（稀疏自编码器 + 池化 + 患者资料）、Yap 等 [22]（ResNet50 + 元数据，<1% 提升）、Spasov 等 [25]（MRI + 临床评估，阿尔茨海默）。
- 降维路线对照：以 PCA 做降维的工作 [18,20] 是本文主要对比对象（无监督 vs 本文有监督 DA）。
- 数学基础：Foley & Sammon [19] 的正交判别向量法。
- 本库相关主题：[[A2_医学图像_分类_配准_生成]]。

## 11. 关键词
医学图像分类，判别分析（DA），临床变量融合，多模态融合，特征降维，预训练网络（ResNet18/ViT），类激活图（CAM），可解释性，肺结核诊断，皮肤病分类，PCA 对比

## 12. 可信度说明
本精读主体严格基于 PDF 提取文本，覆盖范围约为前 12 页（标题/摘要/引言/相关工作含 DA 公式/方法框架/两种融合策略/CAM 方法的开端），提取在 §3.2 CAM 推导处截断（缓存 25406 字符，原文约 44790 字符，仅展示前 25000）。方法、公式（式 2.1–2.7、3.1–3.4）、引言事实（87%、3–4 秒、Yap<1%、维度 1024/2048、512/4096）均可在提取文本中逐条核对。实验章节（§4）的**具体指标、数值、消融、数据集规模**未进入提取文本；数据集名 ChestX-ray8 与 PAD-UFES-20 来自笔记原有"全文补读记录"对 p.13–15 的线索摘录，已标注"据原文后续页/补读线索，提取缓存未覆盖，待核"。全程未编造缺失页的数字。

---

> **可信度补充**: PDF 提取质量 = **high** (2086 字符/页, 提取在 §3.2 CAM 处截断，约覆盖 12/15 页); 来源缓存: `.paper-cache/extracts/医学图像分类 Medical Classification.txt` (提取 12/15 页; 原 AI 主体 12/15 + 全文补读 13-15 线索); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本次重读据提取文本逐条核对方法与引言事实, 实验数值标注待核。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 4.5. Discussion and limitation
- p.13: We used pretrained deep neural networks in combination with DA for dimensionality reduction,
- p.13: We remark that CAMs in our current approach do not directly visualize the influence of the clinical
- p.13: 5. Conclusion
- p.13: In this paper, we proposed a method for medical image classification by using the integration of
- p.14: CAMs further validates that our proposed method indeed focuses on regions aligned with that of the
- p.14: All authors gave final approval for publication and agreed to be held accountable for the work performed
- p.14: References

### 缺失页关键摘录

- p.13: ments in benchmark accuracy but to prioritize practical applicability in clinical diagnosis. While some
- p.13: approaches that use more complex neural network models may report higher accuracy, they often
- p.13: decision-making and accuracy in a way that aligns with real-world diagnostic scenarios.
- p.13: Figure 3. Visualization examples of CAMs on the ChestX-ray8 dataset with the inclusion of bounding box information regarding the
- p.14: 1. Banerjee I et al . 2019 Development and performance of the pulmonary embolism result forecast model (PERFORM) for computed tomography
- p.15: 33. Pacheco AGC et al . 2020 PAD-UFES-20: a skin lesion dataset composed of patient data and clinical images collected from smartphones. Data
<!-- AI_READING_NOTE_END -->
