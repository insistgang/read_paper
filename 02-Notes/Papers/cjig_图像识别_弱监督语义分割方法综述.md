---
title: Xiang W K Zhou Q Cui J C Mo Z Y Wu X F Ou W H Wang J D and Liu W Y. 2024. Weakly supervised semantic segmentation
authors:
  - "项伟康"
  - "周全"
  - "崔景程"
  - "莫智懿"
  - "吴晓富"
  - "欧卫华"
  - "王井东"
  - "刘文予"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.230628
pdf: [[cjig_图像识别_弱监督语义分割方法综述.pdf]]
primary_topic: F_图像分割_语义_实例_全景
topics:
  - "F_图像分割_语义_实例_全景"
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
extract_cache: .paper-cache/extracts/cjig_图像识别_弱监督语义分割方法综述.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/23 pages"
---
# Xiang W K Zhou Q Cui J C Mo Z Y Wu X F Ou W H Wang J D and Liu W Y. 2024. Weakly supervised semantic segmentation

## 基本信息
- **PDF**: [[cjig_图像识别_弱监督语义分割方法综述.pdf]]
- **primary_topic**: `F_图像分割_语义_实例_全景`
- **topics**: `F_图像分割_语义_实例_全景`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 基于深度学习的弱监督语义分割方法综述 (Weakly supervised semantic segmentation based on deep learning) |
| **作者** | 项伟康; 周全; 崔景程; 莫智懿; 吴晓富; 欧卫华; 王井东; 刘文予 |
| **发表时间** | 2024 |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics), 29(05): 1146-1168 |
| **DOI** | 10.11834/jig.230628 |

## 摘要

**英文原摘要（据 PDF 提取文本整理，已修复空格与连字符断裂）**

> Semantic segmentation is an important and fundamental task in the field of computer vision. Its goal is to assign a semantic category label to each pixel in an image, achieving pixel-level understanding. It has wide applications in areas such as autonomous driving, virtual reality, and medical image analysis. Given the development of deep learning in recent years, remarkable progress has been achieved in fully supervised semantic segmentation, which requires a large amount of training data with pixel-level annotations. However, accurate pixel-level annotations are difficult to provide because it sacrifices substantial time, money, and human-label resources, thus limiting their widespread application in reality. To reduce the cost of annotating data and further expand the application scenarios of semantic segmentation, researchers are paying increasing attention to weakly supervised semantic segmentation (WSSS) based on deep learning. The goal is to develop a semantic segmentation model that utilizes weak annotations information instead of dense pixel-level annotations to predict pixel-level segmentation accurately. Weak annotations mainly include image-level, bounding-box, scribble, and point annotations. The key problem in WSSS lies in how to find a way to utilize the limited annotation information, incorporate appropriate training strategies, and design powerful models to bridge the gap between weak supervision and pixel-level annotations. This study aims to classify and summarize WSSS methods based on deep learning, analyze the challenges and problems encountered by recent methods, and provide insights into future research directions. First, we introduce WSSS as a solution to the limitations of fully supervised semantic segmentation. Second, we introduce the related datasets and evaluation metrics. Third, we review and discuss the research progress of WSSS from three categories: image-level annotations, other weak annotations, and assistance from large-scale models, where the second category includes bounding-box, scribble, and point annotations. ... This paper also reports the quantitative segmentation results on the PASCAL VOC 2012 dataset to evaluate the performance of different WSSS methods. Finally, four challenges and potential future research directions are provided.

**中文翻译**

> 语义分割是计算机视觉领域的一项重要的基础任务，目标是为图像中的每个像素分配语义类别标签，实现像素级理解，在自动驾驶、虚拟现实和医学图像分析等领域有广泛应用。得益于深度学习近年来的发展，全监督语义分割取得了显著进展，但它需要大量带有像素级标注的训练数据；而精确的像素级标注难以提供，因为它要耗费大量时间、资金和人力标注资源，从而限制了其实际应用。为降低标注成本并拓宽语义分割的应用场景，研究者越来越关注基于深度学习的弱监督语义分割（WSSS）：其目标是用弱标注信息代替稠密的像素级标注来准确预测像素级分割。弱标注主要包括图像级、最小包围盒、线（涂鸦）和点标注。WSSS 的关键问题在于：如何利用有限的标注信息、结合恰当的训练策略、设计强大的模型，以弥合弱监督与像素级标注之间的鸿沟。本文旨在对基于深度学习的 WSSS 方法进行分类与总结，分析近期方法面临的挑战与问题，并对未来研究方向给出洞见。文中依次：(1) 引出 WSSS 作为全监督局限的解决方案；(2) 介绍相关数据集与评估指标；(3) 从图像级标注、其他弱标注、大模型辅助三个类别回顾并讨论 WSSS 研究进展（其中第二类包含包围盒、线、点标注）。本文在 PASCAL VOC 2012 数据集上报告了不同 WSSS 方法的定量分割结果，最后给出四项挑战与潜在的未来研究方向。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：全监督语义分割依赖大量精细的像素级标注，其标注过程耗费大量人力、时间和资金，对医学图像、遥感图像理解等专业领域，人工标注的准确性也难以保证。论文引用 Lin 等人（2014）的结论给出量化对比——对一幅图像做像素级标注的时间成本约为最小包围盒标注的 **15 倍**、图像级标注的 **60 倍**，直接说明了弱标注的成本优势。
- **之前方法的问题**：全监督方法面临**标注成本高昂**的根本困境；传统图像分割（LBP、HOG、SIFT 特征 + 阈值/区域生长/GrabCut 等）虽计算效率高、可解释性强，但依赖手工特征、表示能力与鲁棒性差，无法处理复杂场景。深度学习方法（自 2015 年 FCN 起）虽性能强，但仍以全监督为主。
- **核心矛盾**：**弱监督信息的有限性与像素级分割任务的精确性之间的矛盾**。论文将关键问题明确表述为：如何利用有限的弱标注信息、结合有效训练策略与模型设计，来缩小弱监督与全监督之间的性能差距（gap between weak supervision and pixel-level annotations）。
- **本文区别于传统综述之处**：作者不采用传统按弱标注类型（4 类：图像级 / 包围盒 / 线 / 点）简单划分的做法，而是**按标注类型和受关注程度**重组为三个类别——图像级标注、其他弱标注（含包围盒、线、点）、大模型辅助，把新兴的大模型辅助方向单列。
## 关键贡献

1.  **系统性的分类框架**：按**标注类型与受关注程度**将 WSSS 分为三大类——基于图像级标注、基于其他弱标注（最小包围盒、线、点）、基于大模型辅助，并把"大模型辅助 WSSS"单独成类，区别于传统的四类划分（任冬伟等，2022）。
2.  **对图像级标注方法的深度剖析**：依据第 2 阶段训练中像素级伪标签是否更新，将图像级方法细分为**伪标签离线生成**（两阶段独立，伪标签固定）与**伪标签在线更新**（端到端联合优化）两类，并把离线生成方法系统归纳为**六类优化策略**：CAM 集成、图像擦除、共现关系解耦、亲和性传播、额外监督信息、自监督学习。
3.  **全面的研究进展回顾**：覆盖从早期 CAM 优化到最新端到端方法，并紧跟前沿单独讨论预训练大模型如何辅助 WSSS（生成更准确的像素级伪标签）。
4.  **统一的性能评估**：在 **PASCAL VOC 2012** 数据集上（表 1/2/3 分别对应图像级、其他弱标注、大模型辅助）报告多种代表性方法的 mIoU 定量结果，为方法对比提供基准。
5.  **明确的挑战与展望**：总结四大挑战——与全监督的性能差距、对未知（训练中未出现）类别的适应能力、模型规模与推理速度（部署效率）、高质量 WSSS 数据集匮乏，并提出相应未来方向。
## 方法

本文作为综述，其核心"方法"是**分类、梳理和总结**现有研究的方法论。因此本节阐述其分类框架下的各类技术路径。

- **整体框架**（图 2 组织结构）：第 1 节介绍相关数据集与评估指标；第 2 节回顾基于图像级标注的 WSSS；第 3 节介绍基于其他弱标注的 WSSS；第 4 节介绍基于大模型的 WSSS；第 5 节总结问题、挑战与未来方向。
- **输入输出**：综述的输入是现有各类 WSSS 论文，输出是对这些方法的系统性分类、对比、总结与展望。
- **关键模块（技术路径分类）**：
    1.  **基于图像级标注的方法**（第 2 节，最具挑战性，仅提供图像所含物体类别、缺位置信息）：
        - **两阶段流程**（图 3，引自 Shen 等，2023）：第 1 阶段用类激活图（CAM，Zhou 等，2016）获得初始种子区域以初步定位，再优化为高质量像素级伪标签；第 2 阶段用伪标签作为监督训练语义分割模型。
        - **CAM 生成机制**（图 4，引自 Zhou 等，2016）：取分类骨干网最后一层卷积特征图，用分类器关于类别 c 的权重参数 W1…Wn 加权求和，得到关于类别 c 的 CAM（反映各位置属于类别 c 的概率），筛选高置信区域得到种子。
        - **伪标签优化——离线方法六类策略**（2.1 节）：
            - **CAM 集成（2.1.1）**：缓解**欠激活**。Wei 等（2018）用不同空洞率的空洞卷积生成并集成多个 CAM；Lee 等（2019）的 FickleNet 随机隐藏特征位置后集成；Jiang 等（2019）的 OAA 在训练中在线累积各阶段 CAM，Jiang 等（2022a）再加注意力丢弃层。
            - **图像擦除（2.1.2）**：擦除已识别的辨别性区域，迫使模型发现新区域再合并。代表：Kim 等（2017）两阶段擦除、Kweon 等（2021）类特定对抗擦除、Wei 等（2017）PSL、Hou 等（2018）自擦除网络、Sun 等（2021）Ecs-Net。
            - **共现关系解耦（2.1.3）**：缓解**过激活**（如"马-人""地板-沙发"共现误导）。Zhang 等（2020b）CONTA（因果推理）、Su 等（2021）CDA（复制粘贴数据增强）、Chen 等（2022b）C-CAM（双因果链，面向医学图像）。
            - **亲和性传播（2.1.4）**：用像素/patch 间相似度把标签从高置信区传播到相似区。低级特征：Kolesnikov & Lampert（2016）边界损失、Huang 等（2018）DSRG 种子区域生长；高级语义：Ahn & Kwak（2018）AffinityNet（随机游走）、Xu 等（2022）MCTformer（多类别 token Transformer）；跨图像/数据集级：Sun 等（2020）协同+对比注意力、Wu 等（2021）CMA、Li 等（2021）图神经网络、Zhou 等（2022）RCA（记忆库 + K-Means 原型）。
            - **额外监督信息（2.1.5）**：①物体边界——Chen 等（2020）BENet、Li 等（2022a）SANCE（轮廓+分割双分支）、Rong 等（2023）边界增强；②显著性图——Joon Oh 等（2017）、Yu 等（2019）SSNet、Lee 等（2021c）EPS、Chen 等（2023c）I2CRC。
            - **自监督学习（2.1.6）**：孪生网络（Wang 等 2020 SEAM 跨视图一致性正则化、Jo & Yu 2021 Puzzle-CAM、Zhang 等 2021b CPN、Jiang 等 2022b L2G、Peng 等 2023）；对比学习/损失设计（Du 等 2022 像素到原型对比、Xie 等 2022b C2AM）；正则化项（Zhang 2020c、Chang 2020 子类别探索、Lee 2021a AdvCAM、Chen 2022a SIPE）。
        - **伪标签在线更新——在线方法**（2.2 节）：端到端联合优化伪标签生成与分割训练。Araslanov & Roth（2020）提出三准则：**局部一致性、语义准确性、完整性**。代表：Zhang 等（2020a）RRM 双分支（分类分支选可靠区域监督分割分支）及（2021c）自适应亲和性损失/标签重分配损失；Ru 等（2022）AFA（从 Transformer MHSA 学全局语义亲和性 + 像素自适应细化）；Ru 等（2023）ToCo（PTC + CTC 模块缓解 ViT 过度平滑）；Chen 等（2023b）MDBA（由显著性图直接生成伪标签 + 多粒度去噪 + 双向对齐）。
    2.  **基于其他弱标注的方法**（第 3 节，监督信号比图像级更强）：
        - **包围盒标注**：盒外视为背景，盒内同时含前景与背景；关键是准确区分盒内前景与背景以生成更准确的伪标签。
        - **线（涂鸦）/点标注**：除类别外还提供局部位置信息；线标注通过从已标注涂鸦推断未标注区域类别生成更完整伪标签；点标注通过标签传播、距离度量学习、损失函数优化将语义扩展到全图。
        - *（注：第 3 节正文在提取缓存中未覆盖，以上要点来自摘要对该类的概述。）*
    3.  **基于大模型辅助的方法**（第 4 节）：利用大规模预训练模型的通用知识理解图像、生成更准确的像素级伪标签，从而提升最终分割性能，是新兴方向。*（第 4 节正文未覆盖。）*
- **评估指标公式**：式(1) mIoU = (1/(k+1)) Σ_{i=0}^{k} (X∩Y)/(X∪Y)，X 为真实结果、Y 为预测结果、k 为总类别数。
- **训练方式 / 推理**：涵盖两阶段独立训练与端到端联合训练；最终分割模型推理与全监督一致，输入图像、输出逐像素类别预测图。
## 实验

- **使用的数据集**（1.1 节，含精确规模）：
    - **PASCAL VOC 2012**：1 464 训练 / 1 449 验证 / 1 456 测试，20 类（人、动物、车辆、日用品等）；最常用，后续性能对比主要基于此。
    - **PASCAL Context**：基于 VOC 2010 构建，共 540 类，常用最高频 59 类、其余归为背景；10 103 幅（4 998 训练 / 5 105 验证）。
    - **MS COCO 2014**：80 类；83 K 训练 / 40 K 验证 / 41 K 测试。
    - **Cityscapes**：城市街景，30 类；5 000 幅精细标注（2 975 训练 / 500 验证 / 1 525 测试）。
    - **Mapillary Vistas**：大规模街景，65 类；25 K 高分辨率图像（18 K 训练 / 2 K 验证 / 5 K 测试）。
- **评价指标**（1.2 节）：**mIoU**（平均交并比，式 1）为主要准确性指标；执行时间、内存占用亦为重要指标，但论文明确指出**大多数 WSSS 论文未给出执行时间结果**（受硬件配置影响而无可比性），**几乎没有论文报告内存占用**。
- **对比方法**：综述提及并对比了大量代表性方法，如 CAM、FickleNet、OAA、PSL、Ecs-Net、CONTA、CDA、C-CAM、AffinityNet、MCTformer、DSRG、RCA、BENet、SANCE、EPS、SEAM、Puzzle-CAM、AdvCAM、SIPE、RRM、AFA、ToCo、MDBA 等。
- **主实验结果**（2.3 节讨论，PASCAL VOC 2012）：早期仅依赖图像级标注的离线方法性能提升有限，例如 Lee 等（2019）FickleNet 仅获 **65.3% mIoU**；近年引入额外监督或自监督后提升显著，例如 Du 等（2022）方法取得 **73.6% mIoU**。论文同时指出 CAM 种子区域在处理小目标、中间镂空物体和复杂形状物体时仍可能很不准确。
- **量化对比表**：表 1（图像级方法）、表 2（其他弱标注方法）、表 3（大模型辅助方法）均在 PASCAL VOC 2012 上对比 mIoU。*（表 1 数值仅 FickleNet 65.3%/Du 等 73.6% 在 2.3 节正文出现；表 2、表 3 完整数值据原文 p.15-16，提取缓存未覆盖，待核。）*
- **消融实验**：作为综述本身无消融实验，仅总结被综述论文中的关键设计及效果。
- **速度/参数量/FLOPs**：论文明确指出大多数 WSSS 论文未给出此类结果，本综述也未提供统一效率对比。
## 局限

1.  **作为综述的固有局限**：本文总结已有工作，自身不提出新方法或新实验。
2.  **内容深度与广度的权衡**：覆盖图像级、其他弱标注、大模型三大类，对某些具体技术的剖析深度可能不如专门算法论文。
3.  **实验对比的局限性**：定量对比集中于 PASCAL VOC 2012，论文虽介绍了 COCO、Cityscapes 等数据集，但未在其上做统一横向对比。
4.  **论文自承的领域挑战**：作者在结论中明确四大未决问题——弱监督与全监督的性能差距、对未知类别的适应能力、模型规模与推理速度（部署）、高质量大规模 WSSS 数据集匮乏。
5.  **本笔记的覆盖局限**：提取缓存仅覆盖 PDF 前 12 页（至 2.3 节讨论开头），第 3 节（其他弱标注详解）、第 4 节（大模型辅助详解）、第 5 节（完整总结与展望）及表 2/3 的具体数值未被提取文本覆盖，相关内容据摘要概述与原文后续页线索标注"待核"。
## 个人评论

1.  **为初学者绘制了清晰的技术地图**：系统梳理了图像级 WSSS 的演进——从 CAM 优化六大策略到端到端在线更新，并把核心难题归纳为三类可直接对应的失败模式：**欠激活**（CAM 覆盖不全→CAM 集成/擦除）、**过激活**（共现误导→共现解耦）、**边界模糊**（→亲和性传播/额外监督）。这种"问题—对策"映射使读者能快速定位每类方法解决的痛点。
2.  **揭示了方法设计的深层逻辑**：以"伪标签是否在线更新"作为切分图像级方法的主轴，比按标注类型切分更有洞察力——它点出了该领域从"分阶段独立优化"向"端到端联合优化"的趋势，并阐明 Transformer 全局感受野（AFA 从 MHSA 学亲和性）与自监督/对比学习是提升弱监督性能的两大杠杆。
3.  **提供了实用的研究起点**：结论中的四项挑战（性能差距、未知类别适应、部署效率、数据集匮乏）直接点明未决难题，其中"模型规模与推理速度"被作者指出是当前研究普遍忽视的方向，对追求落地的研究者尤具选题价值。
4.  **凸显了"额外监督"的杠杆作用**：综述用 65.3%→73.6% mIoU 的对比清楚说明，单纯依赖图像级标注自身信息的提升空间有限，引入显著性图、物体边界等额外监督或自监督是打破瓶颈的有效途径。
5.  **将"大模型辅助"单列的前瞻性**：在 2023 年成稿背景下把预训练大模型辅助 WSSS 独立成类，体现了对 SAM/CLIP 类基础模型冲击该领域的预判，是本综述区别于早期同类综述的关键之处（惜该部分正文未在本笔记覆盖范围内）。

### 使用建议

- **如果快速了解领域**：重点读**摘要、引言（第 0 节）、第 1 节（数据集与指标）、第 2 节开头与 2.3 节讨论**，可快速掌握"是什么、为何重要、方法分类与当前水平"。
- **如果复现某个具体方法**：本文不能直接用于复现；应循文中引用顺着原始论文（如 SEAM、AFA、ToCo 等）去找实现。本综述的价值是帮你定位"哪篇论文解决了你关心的哪个子问题"。
- **如果借鉴创新点**：重点学 **2.1 节六类离线优化策略**的核心思想与 **2.2 节端到端联合优化**的设计理念，尤其亲和性传播、自监督/对比学习、Transformer 全局亲和性如何提升伪标签质量。
- **如果写 Related Work**：可作为弱监督语义分割领域的**权威中文综述**引用，用于引出研究背景、主要技术流派（离线 vs 在线、三大标注类别）与四大挑战。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[F_图像分割_语义_实例_全景]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇**综述论文**，发表于《中国图象图形学报》（Journal of Image and Graphics）2024 年第 29 卷第 5 期（1146-1168），属于计算机视觉领域**图像分割**方向，聚焦**弱监督语义分割（WSSS）**。它系统梳理并总结基于深度学习的 WSSS 方法，核心问题是：如何利用比像素级标注更易获取的弱标注（图像级、最小包围盒、线/涂鸦、点），训练出性能接近全监督的语义分割模型，从而降低标注成本、拓宽应用场景。适合作为图像分割主题下**语义分割**子方向中关于**弱监督学习**的入门与参考文献。

## 2. 一句话总结
本文按"标注类型与受关注程度"将 WSSS 分为图像级标注、其他弱标注、大模型辅助三大类进行系统综述，对图像级方法又按伪标签是否在线更新细分为离线（六类优化策略）与在线（端到端联合优化）两类，并在 PASCAL VOC 2012 上做定量对比、提出四大挑战与展望。

## 3. 背景与问题
- **为什么做**：全监督语义分割依赖海量精细像素级标注，标注耗费大量人力、时间和资金，且在医学、遥感等专业领域准确性难保证。论文引 Lin 等（2014）量化：像素级标注成本约为最小包围盒标注的 15 倍、图像级标注的 60 倍，凸显弱标注的成本优势。
- **之前方法的问题**：全监督面临**标注成本高昂**的根本困境；传统手工特征方法（LBP/HOG/SIFT + GrabCut 等）鲁棒性差、难处理复杂场景；自 2015 年 FCN 起的深度方法虽强但以全监督为主。
- **核心矛盾**：**弱监督信息有限性与像素级分割精确性之间的矛盾**。论文将关键问题表述为：如何利用有限标注信息、结合有效训练策略与模型设计，弥合弱监督与像素级标注之间的鸿沟。

## 4. 核心贡献
1.  **系统性分类框架**：按标注类型与受关注程度分三大类（图像级 / 其他弱标注 / 大模型辅助），把"大模型辅助"单列，区别于传统四类划分（任冬伟等，2022）。
2.  **图像级方法深度细分**：按第 2 阶段伪标签是否更新分为离线生成与在线更新；离线方法归纳为六类策略——CAM 集成、图像擦除、共现关系解耦、亲和性传播、额外监督信息、自监督学习。
3.  **全面进展回顾**：覆盖从 CAM 优化到端到端，并单独讨论预训练大模型辅助 WSSS 的新思路。
4.  **统一性能评估**：在 PASCAL VOC 2012 上以表 1/2/3 对三类方法报告 mIoU。
5.  **挑战与展望**：四大挑战——性能差距、未知类别适应、模型规模与推理速度（部署效率）、高质量数据集匮乏。

## 5. 方法详解
本文核心"方法"是**分类、梳理与总结**现有研究。

- **整体框架**（图 2）：第 1 节数据集与指标 → 第 2 节图像级 → 第 3 节其他弱标注 → 第 4 节大模型 → 第 5 节问题/挑战/展望。
- **图像级两阶段流程**（图 3，Shen 等 2023）：第 1 阶段用 CAM（Zhou 等 2016）获得初始种子并优化为伪标签；第 2 阶段以伪标签监督训练分割模型。CAM 生成（图 4）：取分类骨干末层卷积特征图，用类别 c 的分类权重 W1…Wn 加权求和得到 CAM，筛高置信区为种子。
- **离线六类策略**：
    - **CAM 集成**（欠激活）：Wei 2018（空洞率集成）、Lee 2019 FickleNet（随机隐藏）、Jiang 2019 OAA（在线累积）+ 2022a 注意力丢弃层。
    - **图像擦除**：Kim 2017、Kweon 2021（类特定对抗擦除）、Wei 2017 PSL、Hou 2018 自擦除、Sun 2021 Ecs-Net。
    - **共现关系解耦**（过激活）：Zhang 2020b CONTA（因果推理）、Su 2021 CDA（复制粘贴增强）、Chen 2022b C-CAM（双因果链，医学）。
    - **亲和性传播**：低级——Kolesnikov & Lampert 2016 边界损失、Huang 2018 DSRG；高级——Ahn & Kwak 2018 AffinityNet（随机游走）、Xu 2022 MCTformer（多类别 token Transformer）；跨图像/数据集——Sun 2020、Wu 2021 CMA、Li 2021（图神经网络）、Zhou 2022 RCA（记忆库 + K-Means 原型）。
    - **额外监督信息**：边界——Chen 2020 BENet、Li 2022a SANCE、Rong 2023；显著性图——Joon Oh 2017、Yu 2019 SSNet、Lee 2021c EPS、Chen 2023c I2CRC。
    - **自监督学习**：孪生网络——Wang 2020 SEAM、Jo & Yu 2021 Puzzle-CAM、Zhang 2021b CPN、Jiang 2022b L2G、Peng 2023；对比/损失——Du 2022（像素到原型对比，73.6% mIoU）、Xie 2022b C2AM；正则化——Zhang 2020c、Chang 2020、Lee 2021a AdvCAM、Chen 2022a SIPE。
- **在线方法**（2.2 节）：端到端联合优化。Araslanov & Roth 2020 三准则（局部一致性、语义准确性、完整性）；Zhang 2020a RRM 双分支 + 2021c 自适应亲和性损失/标签重分配损失；Ru 2022 AFA（从 MHSA 学全局亲和性 + 像素自适应细化）；Ru 2023 ToCo（PTC + CTC 缓解 ViT 过度平滑）；Chen 2023b MDBA（显著性图直接生成伪标签 + 多粒度去噪 + 双向对齐）。
- **其他弱标注（第 3 节，正文未覆盖，据摘要）**：包围盒——区分盒内前景/背景；线（涂鸦）——从已标注涂鸦推断未标注区域；点——通过标签传播、距离度量学习、损失优化扩展到全图。
- **大模型辅助（第 4 节，正文未覆盖，据摘要）**：用预训练大模型的通用知识生成更准确伪标签。
- **指标公式**：式(1) mIoU = (1/(k+1)) Σ (X∩Y)/(X∪Y)。

## 6. 实验与结果
- **数据集**（含精确规模）：PASCAL VOC 2012（1464/1449/1456，20 类）；PASCAL Context（540 类用 59，10103 幅，4998/5105）；MS COCO 2014（80 类，83K/40K/41K）；Cityscapes（30 类，5000 幅，2975/500/1525）；Mapillary Vistas（65 类，25K，18K/2K/5K）。后续对比主要基于 PASCAL VOC 2012。
- **评价指标**：mIoU 为主（式 1）；执行时间、内存占用虽重要但论文指出大多数 WSSS 论文未报告（执行时间受硬件影响无可比性，内存占用几无人报告）。
- **主结果**（2.3 节）：FickleNet（Lee 2019）65.3% mIoU；Du 等（2022）73.6% mIoU，体现引入额外监督/自监督后的显著提升；同时指出 CAM 在小目标、镂空、复杂形状物体上仍不准确。
- **对比表**：表 1（图像级）/表 2（其他弱标注）/表 3（大模型辅助）均在 PASCAL VOC 2012 上比 mIoU。*（表 2/3 完整数值据原文 p.15-16，提取缓存未覆盖，待核。）*
- **消融/效率**：综述自身无消融；未提供统一速度/参数量/FLOPs 对比（因多数原论文未报告）。

## 7. 这篇论文真正有价值的地方
1.  **清晰的技术地图**：把图像级 WSSS 的演进与三类核心失败模式（欠激活、过激活、边界模糊）一一对应，便于定位每类方法的痛点。
2.  **揭示设计深层逻辑**：以"伪标签是否在线更新"为主轴切分，点出从分阶段优化到端到端联合优化的趋势，并指明 Transformer 全局亲和性与自监督/对比学习是两大性能杠杆。
3.  **实用研究起点**：四项挑战（性能差距、未知类别适应、部署效率、数据集匮乏）直接给出选题方向，其中"模型规模与推理速度"被指为被忽视的方向。
4.  **量化凸显"额外监督"价值**：用 65.3%→73.6% mIoU 说明纯图像级标注提升有限，额外监督/自监督是打破瓶颈的关键。

## 8. 局限与问题
1.  **综述固有局限**：总结已有工作，自身不提出新方法/新实验。
2.  **深广权衡**：覆盖三大类，单技术剖析深度可能不及专门论文。
3.  **对比局限**：定量对比集中于 PASCAL VOC 2012，未在 COCO/Cityscapes 等做统一横向对比。
4.  **领域未决挑战**（作者自承）：性能差距、未知类别适应、部署效率、高质量大规模数据集匮乏。
5.  **本笔记覆盖局限**：提取缓存仅覆盖前 12 页（至 2.3 节开头），第 3/4/5 节正文与表 2/3 数值据摘要概述与原文后续页标注"待核"。

## 9. 我该怎么使用这篇论文
- **快速了解领域**：读摘要、引言、第 1 节、第 2 节开头与 2.3 节讨论。
- **复现具体方法**：本文不能直接复现；顺引用找原始论文（SEAM/AFA/ToCo 等）。
- **借鉴创新点**：学 2.1 节六类离线策略与 2.2 节端到端联合优化，尤其亲和性传播、自监督/对比学习、Transformer 全局亲和性。
- **写 Related Work**：作为弱监督语义分割权威中文综述引用，引出背景、技术流派（离线 vs 在线 / 三大标注类别）与四大挑战。

## 10. 和其他论文的关系
- 基于主题 `F_图像分割_语义_实例_全景`，本综述与所有具体 WSSS 方法论文相关：文中详述的 CAM（Zhou 等 2016）、FickleNet、OAA、CONTA、CDA、AffinityNet、MCTformer、SEAM、AdvCAM、SIPE、RRM、AFA、ToCo、MDBA 等。
- 与更广的 `[[F_图像分割_语义_实例_全景]]`（语义分割）主题、FCN/DeepLab 等全监督分割工作互为背景。
- "大模型辅助 WSSS"是该综述提出的新兴交叉方向，关联预训练基础模型（SAM/CLIP 类）研究。

## 11. 关键词
语义分割；深度学习；弱监督语义分割（WSSS）；图像级标注；最小包围盒标注；线标注；点标注；大模型；类激活图（CAM）；伪标签；离线生成；在线更新；亲和性传播；自监督学习；PASCAL VOC 2012；mIoU

## 12. 可信度说明
本精读笔记主要基于 PDF 提取文本的**前 12 页**（涵盖中英文摘要、关键词、引言第 0 节、第 1 节数据集与评估指标、第 2 节基于图像级标注方法的 2.1 离线六类策略与 2.2 在线方法、2.3 讨论开头）。提取质量良好、逻辑连贯、图表（图 1-4）说明清晰，故**背景、问题定义、图像级方法分类与详解、数据集规模、2.3 节给出的 65.3%/73.6% mIoU 与四大挑战**等内容可信度高。但**第 3 节（其他弱标注详解）、第 4 节（大模型辅助详解）、第 5 节（完整总结与展望）以及表 1/2/3 的完整 mIoU 数值**未在提取缓存覆盖范围内，相关内容据摘要概述与原文后续页线索标注"待核"，请以原文 p.13-23 为准。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本质量好, 12/23 页, 约 2086 字符/页); 来源缓存: `.paper-cache/extracts/cjig_图像识别_弱监督语义分割方法综述.txt` (提取 12/23 页; 第 3/4/5 节与表 2/3 数值据原文后续页, 提取缓存未覆盖, 待核); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-23; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-23。
- **提取情况**: 缺失页 11 页, 其中 11 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.15: Table 2 Performance comparison of weakly supervised semantic segmentation methods based on
- p.15: ICCV 2015
- p.15: CVPR 2017
- p.15: CVPR 2019
- p.15: CVPR 2021
- p.15: ECCV 2020
- p.15: CVPR 2016
- p.15: CVPR 2018
- p.15: ICCV 2021
- p.15: ECCV 2018
- p.15: IJCAI 2019
- p.15: ECCV 2016

### 缺失页关键摘录

- p.13: Fig.6 The mainstream pipeline for WSSS with
- p.14: Fig.7 The mainstream pipeline for WSSS with
- p.15: Table 2 Performance comparison of weakly supervised semantic segmentation methods based on
- p.15: other weak annotations on PASCAL VOC 2012 dataset
- p.16: Table 3 Performance comparison of weakly supervised semantic segmentation methods based on
- p.16: large -scale models on PASCAL VOC 2012 dataset
- p.19: Franke U ， Roth S and Schiele B . 2016 . The cityscapes dataset for
- p.21: Mapillary vistas dataset for semantic understanding of street
- p.21: Ojala T ， Pietikainen M and Harwood D . 1994 . Performance evaluation
- p.22: learning -a comprehensive evaluation of the good ， the bad and the
<!-- AI_READING_NOTE_END -->
