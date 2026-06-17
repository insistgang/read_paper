---
title: "A Comprehensive Survey of Deep Learning in Remote Sensing: Theories, Tools and Challenges for the Community"
authors:
  - "John E. Ball"
  - "Derek T. Anderson"
  - "Chee Seng Chan"
year: 2017
venue: "arXiv:1709.00308 [cs.CV] (later published in Journal of Applied Remote Sensing)"
doi: 
pdf: [[2017_A_Comprehensive_Surv.pdf]]
primary_topic: R_综述_Survey
topics:
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2017_A_Comprehensive_Surv.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/64 pages"
---
# A Comprehensive Survey of Deep Learning in Remote Sensing: Theories, Tools and Challenges for the Community

## 基本信息
- **PDF**: [[2017_A_Comprehensive_Surv.pdf]]
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A Comprehensive Survey of Deep Learning in Remote Sensing: Theories, Tools and Challenges for the Community |
| **作者** | John E. Ball (Mississippi State University); Derek T. Anderson (Mississippi State University); Chee Seng Chan (University of Malaya) |
| **发表时间** | 2017 |
| **刊物/会议** | arXiv:1709.00308v2 [cs.CV] (2017-09-24), 后正式发表于 Journal of Applied Remote Sensing |
| **DOI** | 未明确 |

## 摘要

清理后的英文原摘要（据提取文本修复空格、连字符断裂）：

> In recent years, deep learning (DL), a re-branding of neural networks (NNs), has risen to the top in numerous areas, namely computer vision (CV), speech recognition, natural language processing, etc. Whereas remote sensing (RS) possesses a number of unique challenges, primarily related to sensors and applications, inevitably RS draws from many of the same theories as CV; e.g., statistics, fusion, and machine learning, to name a few. This means that the RS community should be aware of, if not at the leading edge of, of advancements like DL. Herein, we provide the most comprehensive survey of state-of-the-art RS DL research. We also review recent new developments in the DL field that can be used in DL for RS. Namely, we focus on theories, tools and challenges for the RS community. Specifically, we focus on unsolved challenges and opportunities as it relates to (i) inadequate data sets, (ii) human-understandable solutions for modelling physical phenomena, (iii) Big Data, (iv) non-traditional heterogeneous data sources, (v) DL architectures and learning algorithms for spectral, spatial and temporal data, (vi) transfer learning, (vii) an improved theoretical understanding of DL systems, (viii) high barriers to entry, and (ix) training and optimizing the DL.
>
> **关键词**：Remote Sensing, Deep Learning, Hyperspectral, Multispectral, Big Data, Computer Vision.

中文翻译：

> 近年来，深度学习（DL，本质上是神经网络 NN 的"再品牌化"）在计算机视觉（CV）、语音识别、自然语言处理等众多领域跃居前列。遥感（RS）虽然在传感器与应用上面临一系列独特挑战，但它不可避免地借鉴了与 CV 相同的诸多理论——例如统计学、信息融合与机器学习等。这意味着遥感社区即便不站在 DL 进展的最前沿，也理应对其有所了解。本文提供了迄今最全面的遥感深度学习（RS DL）前沿研究综述，同时回顾了 DL 领域可被遥感借鉴的最新进展，聚焦于面向遥感社区的理论、工具与挑战。具体而言，我们围绕九项尚未解决的挑战与机遇展开：(i) 数据集不足；(ii) 物理现象建模的可被人理解的解；(iii) 大数据；(iv) 非传统的异构数据源；(v) 面向光谱/空间/时间数据的 DL 架构与学习算法；(vi) 迁移学习；(vii) 对 DL 系统更深入的理论理解；(viii) 入门门槛过高；(ix) DL 的训练与优化。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：深度学习近年来在 CV、语音识别、NLP 等领域带来的是"跃迁式"而非渐进式的进步。论文点出一个反讽：DL 作为神经网络的代名词，本身是人工智能的"古老分支"，之所以复兴，得益于算法进步、高性能计算（GPU）和大数据三个因素。遥感本质上借鉴物理、统计、融合、机器学习等核心理论，与 CV 同源，因此遥感社区"理应了解、若非引领"DL 这样的进展。
- **遥感的范畴被扩展**：论文有意把 RS 的边界从传统卫星/航空成像，扩展到无人机（UAV）、众包数据（手机影像、推文等）、高级驾驶辅助系统（ADAS）等"非传统遥感"。这些新数据类型带来新的数据形态与处理需求，也给分析算法带来新挑战。
- **之前方法的问题**：传统 CV/RS 处理链是"浅层"的——通常先做图像去噪/增强，再做人工编码的特征提取（HOG、SIFT、颜色直方图等），然后特征优化，最后在特征上做处理；特征与输出之间一般只有 1–2 个处理层。浅层学习器（SVM、高斯混合模型、隐马尔可夫模型、条件随机场、逻辑回归、极限学习机等）长期是研究主力，但特征需人工设计、针对单一任务、表达复杂层次特征的能力有限。
- **核心矛盾**：DL 强大的自动、分层特征学习能力，与遥感数据的特异性（高维光谱、多源异构、时空序列）及应用对物理可解释性的要求之间存在张力。如何把通用 DL 技术适配到遥感这一特殊领域，是贯穿全文的核心问题。

## 关键贡献

论文在引言中明确列出 6 项贡献（据提取文本逐条核对）：

1.  **系统梳理 DL-RS 的挑战与开放问题**：提出九大未解决挑战与机遇——(i) 数据集不足，(ii) 物理现象建模的可理解解，(iii) 大数据，(iv) 非传统异构数据源，(v) 面向光谱/空间/时间数据的 DL 架构与学习算法，(vi) 迁移学习，(vii) 对 DL 系统更好的理论理解，(viii) 入门门槛高，(ix) DL 的训练与优化。这是全文主体，对应第 4 节。
2.  **全面的文献综述**：综述了 **207 篇遥感应用论文**与 **57 篇遥感及 DL 综述论文**，并引用大量相关 DL 论文；明确声称在覆盖面上扩展了此前的 DL 综述（文献 1–3）。同时把 DL 方法按应用领域聚类，在第 3 节给出代表性论文的详细讨论。
3.  **修改 DL 架构以解决遥感问题的详细讨论**：在第 4.5 节讨论遥感研究者实现的新架构、工具与 DL 组件。
4.  **DL 概述**：第 2 节为不熟悉 DL 的遥感研究者提供高层概述并列出大量参考文献。
5.  **DL 工具清单**：第 2.4.4 节回顾主流 DL 工具，列出若干工具的优缺点，并用表格（Table 2）汇总工具及其参考文献与链接。
6.  **在线数据集与论文汇总表**：提供两份在线表格——逐篇 DL-RS 论文的传感器模态/数据集/主要贡献/参考文献汇总，以及数据集汇总（名称、描述、URL、参考文献）。因体量过大无法放入正文，链接为 cs-chan.com 上的 Online_Dataset_Summary_Table.pdf 与 Online_Paper_Summary_Table.pdf。

## 方法

**重要说明**：本论文为综述，未提出单一新方法。本节概述论文（第 2 节）讨论的主流 DL 架构及其在遥感中的应用范式。

- **整体框架（论文组织）**：第 2 节对比深/浅学习并讨论 DL 架构与成功要素；第 3 节概述 DL 在遥感各领域的应用；第 4 节讨论 DL 应用于遥感的独特挑战与开放问题；第 5 节给出结论与建议。
- **深 vs 浅学习**：浅层学习器一般至多 1–2 层；DL 没有公认的层数界定，但典型网络"至少 4–5 层深"。DL 系统三大特征：(1) 直接从数据中学特征，而非人工设计；(2) 学到复杂度沿网络递增的分层特征；(3) 相比浅层网络更易泛化、更高效地编码模型（浅层系统需要指数级更多的神经元/参数和训练数据）。论文还引 Ba & Caruana 的模型压缩研究：用深网络（DNN）对无标签数据打分，再训练一个更浅的压缩模型去模仿大模型——压缩模型必须有足够复杂度才能复现复杂模型的输出。
- **五种主流架构**：
    1.  **自编码器 (AE)**：用于从无监督数据学有用特征，最早的应用之一是降维（遥感常需）。编码器 `f` 将输入 `x` 映射为潜在表示 `h=f(x)`，解码器 `g` 将 `h` 映射回重构 `x̂`；通过架构约束或稀疏约束（或两者）学到有用映射而非平凡的恒等映射；损失 `L` 度量 `x` 与 `x̂=g(f(x))` 的重构差距，可加正则项 Ω(h) 促进稀疏。其变体**去噪自编码器 (DAE)** 用于去噪：Chen 等给出可边缘化噪声、有闭式解的高效 DAE，训练时注入加性高斯噪声或二值掩蔽噪声。AE 的"哑铃/沙漏（diabolo）"形状即对应降维。
    2.  **卷积神经网络 (CNN)**：受人类视觉皮层"松散启发"。典型 CNN 由多组卷积掩码层后接池化层堆叠，再接全/部分连接层做分类或类别概率估计，部分还用数据归一化层。灰度图用 2D 卷积掩码，RGB 用 3D 掩码。浅层掩码学基础特征，越深特征越复杂、分层构建；池化层为非线性算子（通常取最大），赋予 CNN 非线性学习能力。论文给出 CNN 发展脉络：1990s LeNet（LeCun，读邮编）→ 2012 AlexNet（Krizhevsky，以显著优势赢得 ILSVRC 2012）→ 2013 ZFNet（Zeiler & Fergus，调参版 AlexNet）→ 2014 GoogLeNet（Szegedy，仅 **400 万参数**，远少于 AlexNet 的 **6000 万参数**）→ 2015 ResNet（He 等，使极深网络可训练）→ 2016 DenseNet（Huang 等，层间前馈全连接，消除梯度消失）。
    3.  **深度信念网络 (DBN)**：一种生成式概率图模型（PGM），即"深"的有向无环图（DAG）。Hinton 证明 DBN 可被视为受限玻尔曼机（RBM）/生成式 AE 的堆叠并以贪婪无监督方式逐层训练。论文措辞：迄今 CNN 在各 CV 基准上表现更好，但理论上 DBN "arguably 更优"，因为 CNN 带有更多"约束"；DBN vs CNN 之争随更好的 DBN 学习算法出现可能改变。
    4.  **循环神经网络 (RNN)**：连接构成有向环，主要用于分析语音、时间序列等非平稳过程；具有记忆/持久性（AE 与 CNN 没有），可展开为处理时序数据的一串互联网络。重大突破是 Hochreiter & Schmidhuber 的**长短期记忆 (LSTM)** 单元，可向 cell 写入/输出/存储信息，缓解极深网络的梯度消失/爆炸。
    5.  **反卷积神经网络 (DeconvNet)**：DL 社区的"相对新人"，用于回答"分类之外"的问题——滤波器到底在学什么、可迁移性如何、哪些滤波器最活跃、目标在图像何处（软/硬分割）。与 CNN 的池化相反，DeconvNet 用"反池化（unpooling）"，借助"开关变量（switch variables）"把第 l 层的激活放回 l−1 层原池化位置，得到放大但稀疏的激活图，再送入反卷积滤波器（学习得到或由 CNN 滤波器导出）。论文举例：把 VGG-16 去掉最后分类层后镜像复制（池化换成反池化），整网用于语义分割，得到的 DeconvNet 是 VGG CNN 的两倍大。论文也提醒局限：若 CNN 只学到物体的"部件"而非整体，反池化激活未必能拼出完整、高质量的整体分割；DeconvNet 很新，尚未被遥感社区广泛采用。
- **训练方式**：AE、CNN 等用反向传播（BP）与随机梯度下降（SGD）端到端训练；DBN 用逐层无监督预训练。GPU 与近期 DL 研究进展（Deng 等指出的两大成功原因）是 DL 落地的关键使能因素。
- **与已有方法的差异**：与依赖人工特征（HOG、SIFT、PCA、k-means、稀疏编码等）的浅层方法不同，DL 从原始数据自动学习多层、（通常）非线性、分层的特征表示，减少人工干预并可能更易泛化。

## 实验

- **使用的数据集**：作为综述，不做统一实验。论文称数据集的详细列表因体量过大放在线上汇总表（cs-chan.com）。据原文后续页（提取缓存未覆盖，待核），Table 5 汇总了数据集情况，指出"两大数据集问题"，并提到最常用数据集；不少工作用了未公开报告的自定义数据集。
- **对比方法**：综述层面对比浅层学习（SVM 等）与各类 DL 架构在不同遥感任务上的表现。
- **评价指标**：提取文本（前 12 页）未明确给出统一指标。据原文后续页（提取缓存未覆盖，待核），p.19 提到以 accuracy、F1 score、precision、AUC 衡量性能，Table 6 给出 HSI（高光谱）DL 论文的结果对比。
- **主实验结果**：提取文本未给出统一结果数字。论文主结论是 DL 在遥感多任务上取得显著进展，核心落点是第 4 节的九项挑战。据原文后续页（提取缓存未覆盖，待核），Table 4 给出代表性 DL-RS 工作概览，第 3 节按交通标志识别、迁移学习、分割、目标检测与跟踪、超分辨率、天气预报等子领域组织。
- **消融/泛化/效率信息**：作为综述无统一基准，相关信息分散在被回顾的各应用论文中。

## 局限

1.  **深度与广度的权衡**：作为全面综述，对每个具体算法/应用的讨论偏概览，深度有限。
2.  **时效性**：发表于 2017 年。其点名的若干挑战（小样本、可解释性）此后被大量工作推进；Transformer 等架构在当时尚未成为重点。论文自身亦坦言 DBN vs CNN 的结论会随算法演进而变。
3.  **核心资源的可复现性依赖外链**：最有价值的数据集/论文汇总表托管在 cs-chan.com 外链，依赖链接长期有效。
4.  **缺乏统一实证基准**：综述未对所有方法做统一横向实验对比（部分对比据原文后续页见于 Table 6，提取缓存未覆盖，待核）。

## 个人评论

> 以下为 AI 阅读视角的评论，非论文原文结论。

这篇综述的最大价值在于其**系统性与前瞻性**。

1.  **挑战框架（最值钱的部分）**：它不是简单罗列工作，而是把"DL 用于遥感"的难点提炼成九项具体、可对号入座的挑战（数据不足、物理可解释、大数据、异构数据、时空架构、迁移学习、理论理解、入门门槛、训练优化）。对后续研究者而言，这是一张清晰的"问题地图"。
2.  **全景视角**：把 DL 理论、工具与遥感应用三者串起来讲，帮助读者理解"技术从何而来、用什么工具、解决什么遥感问题"。
3.  **可被人理解的解（值得单独强调）**：论文把"physical-phenomena 的 human-understandable solution"列为一项独立挑战，这在 2017 年综述里相当超前——它预示了后来遥感可解释性、物理约束建模的研究热度。
4.  **实用资源**：在线的论文/数据集汇总表是"开箱即用"的文献调研工具，显著节省定位原始论文的时间。
5.  **入门指南**：第 2 节对 AE/CNN/DBN/RNN/DeconvNet 的高层梳理，是遥感背景研究者平滑过渡到 DL 的良好入口。

### 使用建议

- **快速了解**：读摘要、引言的六条贡献列表，以及第 4 节九项挑战，即可把握全貌。
- **复现**：综述本身无需复现；若要切入某具体方向，按在线汇总表回溯原始论文再精读。
- **借鉴创新点**：把自己的工作与九项挑战对号入座，是确立研究定位与意义的有效方法。
- **写 Related Work**：可作为"DL 在遥感"类综述的范式引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇计算机视觉与遥感交叉领域的**综述（Survey）**，系统梳理深度学习（DL）在遥感（RS）中的研究现状、理论基础、可用工具与领域特有挑战，定位于"为遥感研究者提供一份 DL 全面参考指南"。归入 **R_综述_Survey** 主题贴切。论文为 arXiv:1709.00308v2（2017-09-24），作者来自密西西比州立大学（Ball、Anderson）与马来亚大学（Chan），后正式发表于 Journal of Applied Remote Sensing。

## 2. 一句话总结
本文以"理论—工具—挑战"为主线，综述了 207 篇遥感应用 + 57 篇综述论文，提炼出 DL 应用于遥感的九项核心挑战，并配套在线数据集/论文汇总表，是 2017 年时该领域覆盖面最全的参考。

## 3. 背景与问题
- **为什么要做**：DL 在 CV/语音/NLP 带来跃迁式进步，靠的是算法进步 + 高性能计算（GPU）+ 大数据三因素的复兴。遥感与 CV 同源（物理、统计、融合、机器学习），理应紧跟 DL；论文还有意把遥感范畴从卫星/航空扩展到 UAV、众包、ADAS 等非传统数据源。
- **之前方法的问题**：传统处理链是"浅层"的（去噪/增强 → 人工特征 HOG/SIFT → 特征优化 → 处理），特征与输出间仅 1–2 层；SVM、GMM、HMM、CRF、ELM 等浅层学习器虽是研究主力，但需人工设计、针对单任务、层次特征表达能力有限。
- **核心矛盾**：DL 自动分层特征学习能力 vs 遥感数据特异性（高维光谱、多源异构、时空）与物理可解释性要求之间的张力。

## 4. 核心贡献
1.  **九项挑战与开放问题**（全文主体，第 4 节）：数据集不足 / 物理建模的可理解解 / 大数据 / 非传统异构数据源 / 光谱-空间-时间 DL 架构与算法 / 迁移学习 / DL 理论理解 / 高入门门槛 / 训练与优化。
2.  **全面文献综述**：207 篇 RS 应用论文 + 57 篇综述论文，按应用领域聚类，第 3 节给代表性论文详述；明确扩展此前 DL 综述（文献 1–3）。
3.  **修改 DL 架构以适配遥感**（第 4.5 节）：新架构、工具、DL 组件。
4.  **DL 概述**（第 2 节）：面向遥感读者的高层入门 + 参考文献。
5.  **DL 工具清单**（第 2.4.4 节，Table 2）：主流工具的优缺点与链接汇总。
6.  **在线汇总表**：论文级（传感器/数据集/贡献/引用）+ 数据集级（名称/描述/URL/引用），托管于 cs-chan.com。

## 5. 方法详解
**说明**：综述无单一新方法，此处梳理第 2 节的架构知识。

- **深 vs 浅**：浅层 ≤1–2 层；深层无公认层数界定但"典型 ≥4–5 层"。DL 三特征：直接从数据学特征、学复杂度递增的分层特征、相比浅层网络更易泛化且参数/数据需求更省（浅层需指数级更多神经元）。引 Ba & Caruana 的模型压缩：用 DNN 给无标签数据打分再训练浅模型去模仿。
- **AE**：`h=f(x)`、`x̂=g(h)`，靠架构约束或稀疏约束 Ω(h) 避免学到恒等映射，损失度量重构差距；DAE（Chen 等，注高斯/二值掩蔽噪声、闭式解）用于去噪与降维（diabolo 形状对应降维）。
- **CNN**：卷积掩码（灰度 2D/RGB 3D）+ 池化（多为 max，提供非线性）+ 全/部分连接分类层；浅层学基础特征、深层学复杂分层特征。发展史：LeNet（读邮编）→ AlexNet（ILSVRC 2012，6000 万参数）→ ZFNet（2013）→ GoogLeNet（2014，仅 400 万参数）→ ResNet（2015，极深）→ DenseNet（2016，层间全连接消梯度消失）。
- **DBN**：生成式 PGM = 深 DAG；Hinton 证明可作为 RBM/生成 AE 的堆叠贪婪逐层训练；当前 CNN 在基准上更好但 DBN 理论上"arguably 更优"（CNN 约束更多），结论可能随算法演进改变。
- **RNN**：有向环、有记忆，适合语音/时序等非平稳过程；LSTM（Hochreiter & Schmidhuber）以可写/读/存的 cell 缓解梯度消失/爆炸。
- **DeconvNet**：用反池化（switch variables 复原池化位置）+ 反卷积，回答"滤波器在学什么/目标在哪"；VGG-16 去分类层镜像复制 → 语义分割，体量为 VGG CNN 两倍；局限是若 CNN 只学到部件则难拼出完整分割，且尚未被遥感社区广泛采用。
- **训练**：AE/CNN 用 BP + SGD 端到端；DBN 逐层无监督预训练；GPU 与近期 DL 研究是关键使能因素。

## 6. 实验与结果
- **数据集**：综述不做统一实验；详细数据集列表在线（cs-chan.com）。据原文后续页（提取缓存未覆盖，待核）Table 5 汇总数据集并指出"两大数据集问题"、最常用数据集、以及大量未公开报告的自定义数据集。
- **指标/结果**：提取文本（前 12 页）未给统一指标与结果数字。据原文后续页（提取缓存未覆盖，待核）：p.19 提到 accuracy / F1 / precision / AUC；Table 4 概览代表性 DL-RS 工作；Table 6 对比高光谱（HSI）DL 论文结果；第 3 节按交通标志识别、迁移学习、分割、目标检测与跟踪、超分辨率、天气预报等子领域组织。
- **主结论**：DL 在遥感多任务上显著进步，核心落点是第 4 节九项挑战。

## 7. 这篇论文真正有价值的地方
1.  **挑战框架**：把领域难点提炼成九项可对号入座的挑战，是后续研究的"问题地图"。
2.  **全景视角**：DL 理论 + 工具 + 遥感应用三位一体，建立跨域知识连接。
3.  **超前的可解释性视角**：把"物理现象建模的可被人理解的解"单列为挑战，预示了后续遥感可解释性/物理约束建模热潮。
4.  **实用资源**：在线论文/数据集汇总表是开箱即用的调研工具。
5.  **入门路径**：第 2 节五大架构高层梳理，是遥感读者过渡到 DL 的良好入口。

## 8. 局限与问题
1.  **广度优先、深度有限**：每个算法/应用偏概览。
2.  **时效性**：2017 年视角，小样本/可解释性已被后续推进，Transformer 尚未进入视野；论文自承 DBN vs CNN 结论会变。
3.  **核心资源依赖外链**：汇总表托管 cs-chan.com，依赖链接长期有效。
4.  **无统一实证基准**：跨方法横向对比有限（部分对比据原文后续页见 Table 6，提取缓存未覆盖，待核）。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要 + 引言六条贡献 + 第 4 节九项挑战。
- **复现**：综述无需复现；切入具体方向时按在线汇总表回溯原始论文。
- **借鉴创新点**：把自己的研究与九项挑战对号入座以确立定位。
- **写 Related Work**：作为"DL 在遥感"类综述的范式引用。

## 10. 和其他论文的关系
本文明确声称扩展并深化此前的 DL 综述（提取文本中引为文献 1–3，含 Zhang et al. 给出的遥感四视角 DL 框架——图像处理/像素级分类/目标识别/场景理解，以及 Cheng et al. 对浅层与 DL 特征提取的讨论）。它与通用 DL 综述/教材（如 Schmidhuber 综述、Goodfellow 等的《Deep Learning》）是"领域应用"与"通用理论"的关系。

## 11. 关键词
遥感, 深度学习, 高光谱, 多光谱, 大数据, 计算机视觉, 综述, 九项挑战, AE/CNN/DBN/RNN/DeconvNet

## 12. 可信度说明
本笔记的"顶部各节"与精读第 1–5、7、9–11 节，依据提取文本前 12 页（标题、作者、机构、摘要、引言六条贡献、第 2 节 DL 概述：深浅对比 + AE/CNN/DBN/RNN/DeconvNet）逐条核对，事实支撑充分。涉及第 3 节应用子领域、第 4 节挑战详解、各 Table（4/5/6）的具体内容（实验/数据集/指标段落），提取缓存仅覆盖前 12 页未含，相关描述基于笔记"全文补读记录"中的页面线索给出并已逐处标注"（据原文后续页，提取缓存未覆盖，待核）"。全文未编造数字或数据集。

---

> **可信度补充**: PDF 提取质量 = **high** (提取缓存仅前 12/64 页, 约 2086 字符/页, 文本清晰可读); 核对依据: `.paper-cache/extracts/2017_A_Comprehensive_Surv.txt` (提取 12/64 页) + 笔记内"全文补读记录"页面线索 (覆盖 p.13-64); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。后续页具体数字/表格内容标注"待核"。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-64; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-64。
- **提取情况**: 缺失页 52 页, 其中 52 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: CPU handles preprocessing (data splitting and normalization), while the GPU performs convolu-
- p.14: 3.2 Transfer Learning
- p.14: Transfer learning utilizes training in one image (or domain) to enable better results in another
- p.14: results were tested on LiDAR data, CAD models, and RGB plus depth (RGBD) imagery. Finally,
- p.15: 3.4 Segmentation
- p.15: Segmentation means to process imagery and divide it into regions (segments) based on the con-
- p.15: FCN model was trained on huge and diverse ground truth data of the three cities, which achieved
- p.15: 3.5 Object Detection and tracking
- p.16: Two of the most interesting results were developed to handle incomplete training data, and
- p.16: 3.6 Super-resolution
- p.17: 3.7 Weather Forecasting
- p.17: Weather forecasting attempts to use physical laws combined with atmospheric measurements to

### 缺失页关键摘录

- p.13: Trafﬁc Sign Recognition: In the area of trafﬁc sign recognition, a nice result came from Cire-
- p.14: transfer learning across domains. They utilized a CNN pretrained on the ImageNet dataset, and
- p.14: used for classiﬁcation. The system was able to detect seals with high accuracy.
- p.14: Zelener et al.319labels missing 3D LiDAR points to enable the CNN to have higher accuracy. A
- p.15: agery, and a three-class SAR dataset is also provided. Deep networks of 2, 20, 50 and 100 layers
- p.19: performance in accuracy, F1 scores, precision and area under the curve.
- p.20: DL applied to RS has many challenges and open issues. Table 4 gives some representative DL
- p.20: There are two main issues with most current RS data sets. Table 5 provides a summary of the
- p.20: utilized custom datasets, and these are not reported. Table 5 shows that the most commonly used
- p.20: A very detailed online table (too large to put in this paper) is provided which lists each paper
- p.20: cited in Table 3. For each paper, a summary of the contributions is given, the datasets utilized
- p.20: rated. This is shown clearly in Table 6. Table 6 shows results for the HSI DL papers against the
<!-- AI_READING_NOTE_END -->
