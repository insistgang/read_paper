---
title: "Deep Learning in Remote Sensing: A Review"
authors:
  - "Xiao Xiang Zhu"
  - "Devis Tuia"
  - "Lichao Mou"
  - "Gui-Song Xia"
  - "Liangpei Zhang"
  - "Feng Xu"
  - "Friedrich Fraundorfer"
year: 2017
venue: "IEEE Geoscience and Remote Sensing Magazine"
doi: 
pdf: [[2017_Deep_learning_in_rem.pdf]]
primary_topic: R_综述_Survey
topics:
  - "R_综述_Survey"
  - "R1_遥感_高光谱_变化检测"
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
extract_cache: .paper-cache/extracts/2017_Deep_learning_in_rem.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/60 pages"
---
# Deep Learning in Remote Sensing: A Review

## 基本信息
- **PDF**: [[2017_Deep_learning_in_rem.pdf]]
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`, `R1_遥感_高光谱_变化检测`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Deep Learning in Remote Sensing: A Review |
| **作者** | Xiao Xiang Zhu; Devis Tuia; Lichao Mou; Gui-Song Xia; Liangpei Zhang; Feng Xu; Friedrich Fraundorfer |
| **发表时间** | 2017 (arXiv:1710.03959v1, 11 Oct 2017) |
| **刊物/会议** | IEEE Geoscience and Remote Sensing Magazine (in press) |
| **DOI** | 未明确 (预印本 arXiv:1710.03959) |
| **索引词** | Deep learning, remote sensing, machine learning, big data, Earth observation |

## 摘要

清理后的英文原摘要（修复空格与连字符断裂）：

> This is the pre-acceptance version, to read the final version please go to IEEE Geoscience and Remote Sensing Magazine on IEEE Xplore. Standing at the paradigm shift towards data-intensive science, machine learning techniques are becoming increasingly important. In particular, as a major breakthrough in the field, deep learning has proven as an extremely powerful tool in many fields. Shall we embrace deep learning as the key to all? Or, should we resist a "black-box" solution? There are controversial opinions in the remote sensing community. In this article, we analyze the challenges of using deep learning for remote sensing data analysis, review the recent advances, and provide resources to make deep learning in remote sensing ridiculously simple to start with. More importantly, we advocate remote sensing scientists to bring their expertise into deep learning, and use it as an implicit general model to tackle unprecedented large-scale influential challenges, such as climate change and urbanization.

中文翻译：

> 站在迈向"数据密集型科学"的范式转变节点上，机器学习技术正变得日益重要。作为该领域的一项重大突破，深度学习已在诸多领域证明是一种极其强大的工具。我们是否应当把深度学习奉为解决一切问题的钥匙？还是应当抵制这种"黑盒"方案？遥感社区对此存在争议。本文分析了将深度学习用于遥感数据分析时面临的挑战，综述了近期进展，并提供了能让"在遥感中上手深度学习"变得极为简单的资源。更重要的是，我们倡导遥感科学家把自身专业知识带入深度学习，并将其作为一种隐式的通用模型，用以应对气候变化、城市化等前所未有的大规模重大挑战。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **这篇论文为什么要做**：深度学习是大数据分析中增长最快的趋势，并被列为 2013 年十大突破技术之一[1]。它在计算机视觉等领域（图像索引、分割、目标检测，乃至 AlphaGo 对弈李世石）取得突破后正向各领域渗透。随着数据与算力的增加，遥感领域也终于开始拥抱深度学习，但遥感卫星图像分析带来一系列独特的新科学问题，亟需一篇系统综述来梳理现状、挑战与方向。
- **之前方法有什么问题**：传统遥感分析依赖基于领域知识手工设计的特征（hand-crafted features）和浅层（shallow）机器学习模型；与之相对，深度学习（通常多于两层的神经网络）完全从数据中学习特征表示。面对日益增长的多模态遥感大数据，手工特征的提取与泛化能力有限。
- **作者想解决的核心矛盾是什么**：核心矛盾在于，深度学习这一"数据驱动"的"黑盒"模型，与遥感作为一门"受控质量的测地学测量科学"（geodetic measurements with controlled quality，需要带置信度地反演地球物理/生化参数）之间如何有效结合。作者明确质疑"专家无关、全自动化深度学习"这一教条在遥感中的适用性，倡导把物理模型作为先验重新引入深度学习概念（例如 emulator 模拟器思路[12]）。

## 关键贡献

基于 PDF 提取文本（前 12 页）与原文后续页线索，本文的贡献如下：

1. **系统分析了深度学习应用于遥感时的六大独特挑战**（原文 Section I 逐条列出）：
   ① 数据多模态（光学多/高光谱与 SAR 成像几何和内容完全不同，需要新架构做跨视角/跨模态匹配与融合）；
   ② 数据地理定位（每个像素对应空间坐标，便于与 GIS 图层、地理标记图像等融合，催生定位、基于位置服务等新应用）；
   ③ 数据是受控质量的测地学测量（可带置信度反演地球参数，传感器适配性与数据质量的先验知识更关键，如单航过 SAR 干涉图优于重复航过）；
   ④ 时间变量日益重要（Copernicus 计划保障数十年连续观测，Sentinel-1 每六天覆盖全球一次，推动从单幅图像分析转向时间序列处理）；
   ⑤ 大数据挑战（Sentinel 卫星 2014 年发射至今已获取约 25 PB 数据，算法须足够快且可迁移以应用于全球）；
   ⑥ 很多场景目标是反演地球物理/生化量（地表形变速率、土壤矿物成分、水体成分、大气微量气体浓度、地形高程/生物量）而非分类检测——这里已有过程模型和专家知识作先验。
2. **综述了深度学习在五大遥感方向的进展**：高光谱图像分析（Section III-A，含分类与异常检测）、SAR 图像解译（III-B）、甚高分辨率图像解译（III-C）、多模态数据融合（III-D）、三维重建（III-E）。提取文本仅完整覆盖到 III-A，其余方向据原文后续页线索补读（见文末"全文补读记录"）。
3. **提供"上手工具箱"**（Section IV）：开源代码与数据仓库资源，含 UC-Merced[90]、RSSCN7[80]、WHU-RS19[91] 等场景分类数据集（据原文后续页线索）。
4. **明确提出研究理念**：遥感科学家应发挥专业优势，把深度学习当作"隐式通用模型"应对气候变化、城市化等大规模挑战，并把物理模型等专家知识作为先验重新引入深度学习框架。

## 方法

本文是综述，不提出单一新模型，而是系统讲解深度学习关键模型的结构与原理，并讨论其在遥感的适配。结构为"挑战分析(I) → 从感知机到深度学习的模型基础(II) → 遥感应用综述(III) → 工具(IV) → 展望(V)"。

- **自编码器家族（Section II-A）**：
  1. 自编码器（AE）[14] 与堆叠自编码器（SAE）：AE 将输入 x∈R^D 经非线性映射编码为隐表示 h，再反向映射重建出 y；重建误差定义为 x 与 y 的欧氏距离（约束 ‖x−y‖₂²→0），一般用 SGD 优化（第 4-5 页, 式(1)(2)）。SAE 是多层 AE 串联、前一层输出接后一层输入。
  2. 稀疏自编码器[15]：当隐层维度 M>D 时，通过在损失中加入稀疏约束发现有趣结构；损失为重建误差项 J 加上隐单元的 KL 散度惩罚 KL(ρ‖ρ̂_j)（式(3)(4)），ρ 是期望平均激活、β 控制稀疏惩罚权重（第 5 页）。
  3. RBM 与 DBN[16]：RBM 是含可见层与隐层、层间对称连接、层内无连接的随机无向图模型，能量函数式(5)、联合分布式(6)（第 5-6 页, 图 1）。单个 RBM 表达能力有限，堆叠多个 RBM 构成 DBN；Hinton 等[16]提出逐层贪婪训练 RBM 以高效训练整个 DBN。
- **卷积神经网络（Section II-B，文本重点）**：回顾计算机视觉经典 CNN：
  - **AlexNet**[2]：2012 年 Krizhevsky 等提出，赢得 2012 ILSVRC，首次用 CNN 取得 top-5 错误率 15.4%。三大贡献——用 ReLU 替代 tanh（训练快数倍）、用 Dropout 防过拟合、用数据增强（水平/垂直平移与翻转）；关键之一是在 GPU 上训练（第 7 页, 图 2）。
  - **VGG Net**[3]：2014 年 Simonyan 与 Zisserman 提出，理念是"简洁与深度"——严格使用 3×3 卷积核（stride 与 padding 均为 1）配 2×2 步长为 2 的最大池化；用更小感受野的 3×3 替代 5×5/7×7，同一 block 内特征图尺寸与卷积核数相同，每经一次池化特征数约翻倍，并用 scale jittering 做数据增强。它强化了"更深 CNN 能促进层次化特征表示从而提升分类精度"的认识；缺点是从头训练需巨大算力与大规模标注集（第 7-8 页）。
  - **ResNet**[4]：He 等提出 152 层网络，以 3.6% 错误率赢得 ILSVRC 2015，在分类/检测/定位上以单一架构创下新纪录。论文深入分析了"退化问题"（朴素增层反而带来更高训练/测试误差），并主张优化残差映射比优化原始无参照映射更容易；核心是加入跳过两层及以上卷积、做恒等映射的 shortcut 连接，与堆叠卷积输出相加（第 8 页）。
  - **FCN**[7]：语义分割（给每个像素分配语义标签）最重要的工作，输出须与输入同像素尺寸。核心思想——经编码/解码结构端到端学习上采样（先下采样激活尺寸再上采样）；全卷积结构（末端无全连接层）使网络可接受任意尺寸输入；引入 skip connection 融合网络不同深度的信息做多尺度推断（第 8-9 页, 图 3）。
- **遥感应用方法论（Section III-A 高光谱图像分析）**：高光谱传感器有数百个窄波段，极高光谱分辨率可借光谱学分析识别像素内材料；EnMAP（计划 2020）、DESIS（计划 2017）等高质量高光谱卫星数据正在到来（第 9-10 页）。综述的两类应用为土地覆被/利用分类（III-A1）与异常检测（III-A2）。在分类中：
    - **为何用深度学习**：大气散射、复杂光散射机制、类间相似与类内差异使高光谱成像过程本质上是非线性的；相比浅层模型（决策树、随机森林、SVM[20]），深度架构能提取高层、层次化、抽象的特征，对非线性输入更鲁棒（第 10-11 页）。
    - **自编码器路线**：SAE 在光谱域提取层次特征[22]；DBM[23]；Tao 等用稀疏堆叠 AE 从无标签数据学特征再喂入线性 SVM[24]（第 11 页）。
    - **监督 CNN 路线**：5 层 1D CNN 直接在光谱域分类[25]；2D CNN 编码空谱信息后接 MLP 分类[26]；用 1D/2D CNN 分类作物类型、结论是 2D 优于 1D 但小目标会被平滑误分[27]；空谱特征框架联合局部判别嵌入降维与 2D CNN 防过拟合[28]；自改进 CNN 把 2D CNN 与分数阶达尔文粒子群优化结合迭代选最优波段[21]；端到端波段自适应空谱特征学习网络应对维度灾难[29]；像素对（pixel-pair）CNN 显著扩增训练样本[30]（第 11-12 页）。
    - **3D CNN**：3D 卷积同时在空间-光谱维操作（2D CNN 仅空间维），故能更好建模光谱信息；[19] 提出有监督、ℓ₂ 正则的 3D CNN 模型（图 5），[32] 沿类似思路做空谱分类（第 11-12 页）。

## 实验

- **使用的数据集**：本文是综述，无自有实验数据集。文中作为例证/背景提及：Sentinel 卫星至今约 25 PB 数据（大数据挑战, 第 3 页）；高光谱卫星 EnMAP（2020）、DESIS（2017, 第 9-10 页）；据原文后续页线索还涉及 SAR 的 MSTAR ATR 数据集、PolSAR 的 Flevoland 数据集、场景分类的 UC-Merced/RSSCN7/WHU-RS19（见文末"全文补读记录"，提取缓存未覆盖, 待核）。
- **对比方法**：本文不做自有实验，但在综述各研究时反复以传统浅层模型（决策树、随机森林、SVM[20]）作为对比基准。
- **评价指标**：提取文本（前 12 页）未给出统一指标。据原文后续页线索，SAR ATR 任务报告了 MSTAR 标准操作条件下 99.1% 的精度（[40] 等, 待核）。
- **主实验结果**：本文核心"结果"是文献计量统计——**图 4** 显示自 2014 年以来"遥感中深度学习"论文数量呈指数增长（来源 ISI Web of Science, 状态 2017 年 9 月, 第 8-10 页）。引用的代表性结果：AlexNet top-5 错误率 15.4%（2012 ILSVRC, 第 7 页）、ResNet 152 层错误率 3.6%（ILSVRC 2015, 第 8 页）。
- **消融实验**：综述无自有消融。PDF 文本未明确。
- **泛化实验**：综述无自有泛化实验。PDF 文本未明确。
- **速度/参数量/FLOPs**：未给具体数字，但强调深度学习依赖大数据与大算力，GPU 训练是关键（AlexNet 段, 第 7 页）。

## 局限

- **方法深度有限**：作为综述，对各研究是概括性介绍，难以深入某一具体方法的细节与局限。
- **覆盖范围与时效**：本提取缓存仅完整覆盖前 12 页（即标题/摘要/索引词/第 I 章动机/第 II 章模型基础/第 III-A 高光谱分类），SAR、甚高分、数据融合、3D 重建、工具资源、结论等后续内容靠补读线索补足、尚需核对。本文发表于 2017 年，深度学习发展极快，文中所述前沿可能已被超越。
- **缺乏统一定量对比**：未提供统一基准定量比较不同方法在遥感任务上的性能，读者难判相对优劣。
- **"倡导"的实践性**：物理模型与深度学习深度融合极具挑战，本文更多提出理念，普适技术路径仍待探索。

## 个人评论

这篇综述的最大价值在于其 **"格局"与"指引性"**。它超越单纯技术回顾，剖析了遥感学科与深度学习方法论之间的契合点与矛盾点。对后续研究的启发：
1. **问题导向而非技术堆砌**：把六大遥感独特性（多模态、地理定位、测地学测量、时序、大数据、参数反演）讲清楚，提醒研究者不能盲目套用 CV 模型，须先思考遥感数据特性带来的新挑战。
2. **倡导"领域知识+深度学习"的融合范式**：把物理模型、传感器专业知识作为先验融入网络（如 emulator 模拟器思路），对设计更可信、可解释的遥感 AI 有指导意义。
3. **提供领域全景图与入门路径**：清晰描绘高光谱、SAR、甚高分等子方向的脉络并给出资源索引，是极佳的"开题地图"。

值得注意的是，它本质是一篇横跨多子领域的综述（primary_topic 因此定为 `R_综述_Survey`），高光谱只是其中 III-A 一节；若只把它当高光谱/变化检测文献会低估其覆盖面。

### 使用建议

- **如果快速了解**：读**摘要**、**Section I Motivation**（六大挑战与动机）、**Section III 开头**（应用领域分类）与 **Section V Conclusion**（展望），即可把握核心思想与领域概况。
- **如果复现**：本文不含可直接复现的单一方法，应作为**索引**，按文中引用（如 [19]、[21]、[25] 等）查找具体研究复现。
- **如果借鉴创新点**：重点学其**提出问题的视角**（Section I）与**融合领域知识的思想**，思考如何把光谱维、时间序列或物理约束融入网络设计。
- **如果写 Related Work**：可放在**"遥感与深度学习综述"** 经典参考文献列表，用于引出领域背景与挑战；涉及高光谱分类时可引 III-A 节作背景支撑。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R_综述_Survey]]
> - [[R1_遥感_高光谱_变化检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇权威综述（IEEE Geoscience and Remote Sensing Magazine，预印本 arXiv:1710.03959, 2017），由 DLR/TUM、Wuhan University、Fudan、TU Graz 等机构的遥感与计算机视觉团队合著。核心方向是系统探讨深度学习在遥感中的应用现状、挑战与未来：先讲六大独特挑战（Section I），再回顾深度学习模型基础（Section II，重点 CNN），然后综述高光谱、SAR、甚高分、数据融合、3D 重建五个子方向（Section III），最后给工具资源（IV）与展望（V）。它适合作为"遥感×深度学习"交叉领域的宏观背景与基础综述文献。需要说明：本仓库文件名虽含"高光谱变化检测"字样，但该字样只对应论文 III-A 一节，论文真实定位是覆盖多子领域的综述（故 primary_topic 已修正为 `R_综述_Survey`，`R1_遥感_高光谱_变化检测` 作为次要主题保留）。

## 2. 一句话总结
本综述提炼了深度学习用于遥感的六大独特挑战（多模态、地理定位、测地学测量、时间序列、大数据、地球物理/生化参数反演），系统讲解了自编码器家族与 CNN（AlexNet/VGG/ResNet/FCN）模型基础并综述其在高光谱等遥感子方向的进展，倡导把遥感专家知识与物理模型作为先验融入深度学习框架。

## 3. 背景与问题
- **为什么要做**：深度学习是大数据分析增长最快的趋势（2013 十大突破技术之一[1]），在 CV、围棋等领域取得突破后正全面渗透；随着数据与算力增加，遥感也开始拥抱它，但卫星图像分析提出一系列独特的新科学问题，需要一篇综述来梳理。
- **之前方法的问题**：传统遥感依赖基于领域知识手工设计的特征与浅层模型；深度学习则完全从数据中学特征表示。面对多模态遥感大数据，手工特征的提取与泛化能力受限。
- **核心矛盾**：纯数据驱动的"黑盒"深度学习 vs. 遥感作为"受控质量的测地学测量科学"（需带置信度反演地球参数、已有物理过程模型作先验）。作者明确质疑"专家无关、全自动化深度学习"教条对遥感的适用性，主张把物理模型重新引入（emulator 思路[12]）。

## 4. 核心贡献
1. **逐条厘清六大遥感独特挑战**（Section I）：多模态/跨模态匹配融合、地理定位、受控质量测地学测量、时间序列（Sentinel-1 每 6 天覆盖全球）、大数据（Sentinel 已积累约 25 PB）、地球物理/生化参数反演（而非仅分类检测）。
2. **综述五大子方向**：高光谱（III-A，分类+异常检测）、SAR（III-B）、甚高分（III-C）、数据融合（III-D）、3D 重建（III-E）。
3. **提供上手工具箱**（Section IV）：开源代码与数据仓库（含 UC-Merced/RSSCN7/WHU-RS19 等场景分类集，据后续页线索）。
4. **提出研究理念**：把深度学习当"隐式通用模型"应对气候变化、城市化等大规模挑战，并把物理模型/专家知识作为先验重新引入。

## 5. 方法详解
本文不提新模型，而是讲解关键模型并讨论其遥感适配。
- **自编码器家族（II-A）**：AE[14]（编码-解码，重建误差为欧氏距离 ‖x−y‖₂²→0，SGD 优化，式 1-2）→ SAE（多层 AE 串联）；稀疏自编码器[15]（M>D 时加 KL 散度稀疏惩罚，式 3-4，ρ 为期望激活、β 控权重）；RBM[16]（可见层+隐层、层间对称连接、层内无连接的随机无向图，能量函数式 5、联合分布式 6）→ 堆叠成 DBN，Hinton 等逐层贪婪训练[16]。
- **CNN（II-B，重点）**：AlexNet[2]（2012 ILSVRC 冠军，top-5 错误率 15.4%；ReLU+Dropout+数据增强+GPU 训练）；VGG[3]（3×3 卷积 stride/padding=1 + 2×2 stride-2 池化，深而简洁，scale jittering）；ResNet[4]（152 层，ILSVRC 2015 错误率 3.6%，shortcut 恒等映射缓解退化问题）；FCN[7]（语义分割，编码/解码端到端学上采样，全卷积接受任意尺寸，skip connection 做多尺度融合）。
- **遥感适配（III-A 高光谱分类）**：因大气散射/光散射机制/类间相似类内差异致成像过程非线性，深度模型比 SVM 等浅层模型能提取更鲁棒的高层特征。路线含：SAE[22]/DBM[23]/稀疏堆叠 AE+线性 SVM[24]；监督 CNN——5 层 1D CNN[25]、2D CNN+MLP[26]、1D vs 2D 作物分类[27]、LDE 降维+2D CNN[28]、2D CNN+分数阶达尔文 PSO 选波段[21]、波段自适应空谱网络[29]、像素对 CNN 扩样[30]；3D CNN[19,32]（空谱联合卷积，ℓ₂ 正则，图 5）。

## 6. 实验与结果
- **数据集**：综述无自有数据集；例证性提及 Sentinel（约 25 PB）、高光谱卫星 EnMAP(2020)/DESIS(2017)；据后续页线索涉及 MSTAR、Flevoland PolSAR、UC-Merced/RSSCN7/WHU-RS19（提取缓存未覆盖, 待核）。
- **对比方法**：以决策树/随机森林/SVM[20] 等浅层模型为常用对比基准。
- **评价指标**：前 12 页未给统一指标；后续页线索称 SAR ATR 在 MSTAR 标准操作条件下达 99.1%（待核）。
- **主结果**：图 4 文献计量——自 2014 年起遥感深度学习论文指数增长（ISI Web of Science，2017 年 9 月）。引用结果：AlexNet 15.4%、ResNet 3.6%。
- **消融/泛化/复杂度**：综述无自有实验；强调依赖大数据与 GPU 算力。

## 7. 这篇论文真正有价值的地方
1. **问题导向**：把六大遥感独特性讲透，提醒不要盲目照搬 CV 模型。
2. **融合范式**：倡导把物理模型/传感器知识作为先验融入网络（emulator），指向更可信、可解释的遥感 AI。
3. **领域全景图**：清晰梳理高光谱/SAR/甚高分等脉络并给资源索引，是优秀"开题地图"。

## 8. 局限与问题
- 综述粒度粗，难深入单一方法细节。
- 本提取缓存仅完整覆盖前 12 页，后续子方向靠补读线索、尚需核对；2017 年发表，部分前沿已被超越。
- 无统一定量基准对比不同方法。
- 物理模型与深度学习融合更多停留在理念，缺普适技术路径。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + Section I（六大挑战）+ Section III 开头 + Section V。
- **复现**：当作索引，按引用（[19][21][25] 等）查具体研究。
- **借鉴创新**：学其提出问题的视角与融合领域知识的思想，把光谱维/时序/物理约束融入网络设计。
- **写 Related Work**：放入"遥感×深度学习综述"经典文献，引出背景与挑战；高光谱分类可引 III-A。

## 10. 和其他论文的关系
本文是 2017 年的领域综述，自然会被遥感深度学习的后续研究引为背景。其 II-B 节回顾的 AlexNet[2]/VGG[3]/ResNet[4]/FCN[7] 是 CV 基础工作，III-A 节梳理的 1D/2D/3D CNN 高光谱分类[19][25][26] 等是具体研究的源头。在本知识库中可与 `R_综述_Survey`、`R1_遥感_高光谱_变化检测` 主题下的论文建立背景关联。

## 11. 关键词
深度学习, 遥感, 机器学习, 大数据, 地球观测; 卷积神经网络, 自编码器, RBM/DBN, FCN; 高光谱图像分析, SAR, 甚高分, 数据融合, 3D 重建; 多模态, 时间序列, 物理模型先验, 综述

## 12. 可信度说明
本笔记中关于标题、作者（含原笔记此前遗漏的 Feng Xu）、刊物（IEEE Geoscience and Remote Sensing Magazine）、摘要、索引词、Section I 六大挑战、Section II 模型基础（AE/SAE/稀疏 AE/RBM/DBN、AlexNet/VGG/ResNet/FCN 及对应数字 15.4%、3.6%、152 层、3×3、2×2 等）、Section III-A 高光谱分类（各引用 [19]-[32] 路线）的所有声明，均能在 PDF 提取文本（前 12 页）中逐条找到支撑。涉及 SAR(III-B)/甚高分(III-C)/数据融合(III-D)/3D 重建(III-E)、工具资源(IV)、结论(V) 的内容（如 MSTAR 99.1%、UC-Merced 等）来自原文后续页补读线索、提取缓存未覆盖，已逐处标注"待核"。整体而言，本笔记对论文前半部分的概括可靠且基于原文。

---

> **可信度补充**: PDF 提取质量 = **high** (前 12 页约 2086 字符/页, 空格与连字符断裂已在摘要等处人工修复); 来源缓存: `.paper-cache/extracts/2017_Deep_learning_in_rem.txt` (提取 12/60 页, 文末补读线索覆盖至 p.60); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-60; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-60。
- **提取情况**: 缺失页 48 页, 其中 48 页提取到可读文本。缺失页包含正文/附录内容, 其中约 16 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: In summary, deep learning has been widely applied to the multi/hyper-spectral image clas-
- p.13: Over the past few years, there have been many publications in deep learning-related studies for
- p.13: October 12, 2017 DRAFT
- p.16: Deep learning provides such a tool for automatically extract features that represent spatial patterns
- p.16: One large stream of studies will employ at least one type of unsupervised generative graphical
- p.17: The so-called convolutional-wavelet neural network is then used in conjunction with superpixels
- p.18: The deep arhitectures discussed in Section II-B have been applied to the problem of scene
- p.19: The reason may lies in the fact that the large-scale networks usually contain millions of
- p.19: CNN model is transferred to extract high-level features of objects and the negative bootstrapping
- p.22: Of course, when data are big and relations to be unveiled are complex, one would favour
- p.22: In this respect, training data are abundant, which is in line with the requirements of modern
- p.24: Parallel research considered spatial structures in the network, by training architectures predict-

### 缺失页关键摘录

- p.14: Chen et al. [40] introduce CNN into SAR ATR and tested on the standard ATR dataset
- p.14: the MSTAR dataset (i.e., a state-of-the-art accuracy of 99.1% on standard operating condition
- p.14: Many authors applied CNN to SAR ATR and tested on MSTAR dataset, e.g., [43–46], etc.
- p.15: Fig. 9. Flevoland dataset. Left: Pauli RGB of the PolSAR dataset; Right: classiﬁcation result from [53].
- p.17: can produce a more detailed result then operational products.
- p.18: - Using pre-trained networks. The pre-trained deep CNN on the natural image dataset, e.g.,
- p.18: - Making a pre-trained model adapt to the speciﬁc conditions observed in a dataset under
- p.18: study, one can decide to ﬁne-tune it on a smaller labeled dataset of satellite images. For
- p.18: the UC-Merced dataset [90] (see Section IV-C), obtaining better results than directly using
- p.18: characteristic of satellite images. Nonetheless, compared with the natural image dataset that
- p.18: (i.e., UC-Merced dataset [90], RSSCN7 dataset [80], WHU-RS19 [91] are fairly small –
- p.19: satellite image dataset, which suffers a drop in classiﬁcation accuracy compared with using
<!-- AI_READING_NOTE_END -->
