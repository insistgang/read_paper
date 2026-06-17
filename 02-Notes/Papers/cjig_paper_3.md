---
title: Wang L A Miao P H Su W Li X Ji N Y and Jiang Y B. 2023. Multimodal referring expression comprehension based on image and
authors:
  - "王丽安"
  - "缪佩翰"
  - "苏伟"
  - "李玺"
  - "吉娜烨"
  - "姜燕冰"
year: 2023
venue: "中国图象图形学报"
doi: 10.11834/jig.221024
pdf: [[cjig_paper_3.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
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
extract_cache: .paper-cache/extracts/cjig_paper_3.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/18 pages"
---
# Wang L A Miao P H Su W Li X Ji N Y and Jiang Y B. 2023. Multimodal referring expression comprehension based on image and

## 基本信息
- **PDF**: [[cjig_paper_3.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 图像—文本多模态指代表达理解研究综述 (Multimodal referring expression comprehension based on image and text: a review) |
| **作者** | 王丽安¹; 缪佩翰¹; 苏伟²; 李玺²; 吉娜烨³; 姜燕冰³* |
| **单位** | 1. 浙江大学软件学院(宁波); 2. 浙江大学计算机科学与技术学院(杭州); 3. 浙江传媒学院媒体工程学院(杭州) |
| **发表时间** | 2023, 第 28 卷第 5 期, 页码 1308-1325 |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics) |
| **DOI** | 10.11834/jig.221024 |

## 摘要

**清理后的英文原摘要 (Abstract):**

> As a subtask of visual grounding (VG), referring expression comprehension (REC) is focused on locating the object defined by the input referring expression in a given image. To optimize multimodal-data-based artificial intelligence (AI) tasks, REC is used to facilitate interaction ability between humans, machines, and the physical world. REC can be used in domains like navigation, autonomous driving, robotics, and early education, in terms of visual understanding systems and dialogue systems. Additionally, it is beneficial for other related studies, including (1) image retrieval, (2) image captioning, and (3) visual question answering. In the past two decades, computer-vision-oriented object detection has been developing dramatically, which can locate all predefined, fixed-category objects. To obtain the object defined by a referring expression, REC must solve the challenging problem of reasoning over multiple related objects. The general process of REC can be divided into three modules: linguistic feature extraction, visual feature extraction, and visual-linguistic fusion. The most important of the three is visual-linguistic fusion, which realizes the interaction and screening between linguistic and visual features. This survey segments existing REC methods into three categories according to visual representation granularity: (1) regional convolution granularity (five sub-categories by fusion module: early, attention-mechanism fusion, expression-decomposition fusion, graph-network fusion, and Transformer-based fusion); (2) grid convolution granularity (two sub-categories: filtering-based fusion and Transformer-based fusion); and (3) image-patch granularity. It then introduces four popular datasets and evaluation methods, and finally identifies three challenges to be resolved — the model's reasoning speed, interpretability, and reasoning ability over expressions — and predicts future research directions in the video and 3D domains.

**中文翻译 / 原文摘要要点:**

> 指代表达理解(REC)作为视觉—语言相结合的多模态任务，旨在理解输入指代表达式的内容并在图像中定位其所描述的目标对象，受到计算机视觉和自然语言处理两个领域的关注。REC 建立了人类语言与物理世界视觉内容之间的桥梁，可广泛应用于视觉理解系统和对话系统等人工智能设备。解决该任务的关键在于：先对复杂的指代表达式进行充分的语义理解，再利用语义信息对包含多个对象的图像进行关系推理与对象筛选，最终在图像中唯一地定位目标对象。本文从计算机视觉视角出发综述 REC：首先介绍通用处理流程；然后按视觉数据表征粒度将现有方法划分为基于区域卷积粒度、网格卷积粒度、图像块粒度三类，并进一步按视觉—文本特征融合模块的建模方式细分；此外介绍主流数据集与评估指标；最后从模型推理速度、可解释性、对表达式的推理能力三个方面揭示现有方法面临的挑战，并对 REC 的发展进行全面展望。
>
> **关键词**: 视觉定位(VG); 指代表达理解(REC); 视觉与语言; 视觉表征粒度; 多模态特征融合

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：REC 要求根据一个完整的描述性句子(指代表达式)在图像中**唯一地**定位目标对象，成功构建起人类语言、机器与现实场景之间的沟通桥梁。它在新一代智能设备的视觉理解系统和对话系统中应用前景广泛，例如导航、自动驾驶、视频监控、机器人和早期教育。随着大规模多模态数据的产生，与 REC 类似的视觉—语义理解任务(VG、图像/视频描述生成、VQA、视觉文本检索)吸引了大量关注。
- **与相邻任务的区别**：REC 与**短语定位(phrase localization)**同为视觉定位的两个子任务——短语定位需定位查询语句中提及的**所有**对象(查询可为词、短语、从句乃至整句)，而 REC 的查询是描述**特定对象**的表达式，需根据对象的类别、属性及与其他对象的关系**唯一**定位目标。另一相似任务是**指代表达分割(RES)**，目标是分割(而非框出)表达式描述的对象。
- **与目标检测的区别**：目标检测在预定义固定类别上定位对象(在 COCO 上 mAP 已达 63.2%，Zhang 等 2022)，而 REC 的目标对象**没有固定类别，完全由输入表达式决定**，因此更具挑战性：既要理解表达式的语义(属性、关系)，又要对含多个对象的图像进行推理。论文用图 1 举例：同一句不同表述("man on middle horse wearing black and red" vs "man on horse red top")指向同一对象；而表述虽共享 "man""horse" 等词却可能指向不同对象。
- **之前方法的问题**：综述类论文多关注视觉—语言多模态任务的总体概述；针对 REC 仅有 1 篇 2021 年英文综述(Qiao 等，2021)，它对当时方法与数据集做了全面总结，但**没有对 REC 任务进行深入分析**，且未充分涵盖近两年流行的基于 Transformer 的方法。
- **核心矛盾**：视觉数据比文本含更丰富信息的同时也存在更多冗余干扰，提取出完整且有效的视觉特征是后续定位成功的基础——因此视觉特征提取模块被视为 REC 模型的"基础模块"，而视觉—文本融合是"最核心模块"。如何在保证定位精度的同时提升推理速度、可解释性和对长难表达式的推理能力，是核心挑战。

## 关键贡献

1.  **提出两级分类框架**：第 1 级以**视觉特征提取模块的视觉表征粒度**为标准(区域卷积、网格卷积、图像块三类)，第 2 级以**视觉—文本特征融合模块的建模方式**为标准。论文明确指出此分类不同于以往按"是否预生成对象候选框"划分为一阶段/二阶段方法(Qiao 等 2021)的二分法。
2.  **系统梳理 REC 处理流程**：将通用流程划分为文本特征提取、视觉特征提取、视觉—文本特征融合推理三个模块(图 2)，并分析各模块的功能与演进。
3.  **全面总结基于 Transformer 的 REC 方法**：归纳将 Transformer 用于多模态融合的三种注意力机制——**相加融合、拼接融合、交叉融合**(图 9)，并在表 2 中列出 8 个代表方法各自的视觉输入粒度与注意力类别。
4.  **介绍主流数据集与评估指标**：基于四个流行数据集介绍任务(RefCOCO、RefCOCO+、RefCOCOg 等，划分细节见原文 3.1 节)，评估指标为定位准确率(%)。
5.  **揭示三大挑战并展望未来**：从模型推理速度、可解释性、对表达式的推理能力三方面总结挑战，并从模型设计与领域发展两个方面对 REC 在视频、3D 领域的发展进行展望。

## 方法

**整体框架与分类**：本文不提出新模型，而是提出一个分析框架(图 4)。先按**视觉特征提取模块的输出粒度**将方法分三大类，每类内部再按**视觉—文本融合模块的设计**细分。

- **输入输出**：输入一张图像和一个文本指代表达式；输出目标对象在图像中的边界框坐标。

- **关键模块详解**：
  1.  **文本特征提取模块**：早期普遍用单个 LSTM(Donahue 等 2015)直接编码整个表达式，处理简单但忽略各部分重要程度差异、对长表达式无法提取关键特征；之后出现将表达式分解为三元组或用外部解析器分解的方法；随预训练发展，大量方法改用预训练 **BERT**(Devlin 等 2019)提取文本特征。
  2.  **视觉特征提取模块(分类核心，图 3 给出三种粒度对比)**：
      - **区域卷积粒度**：将图像输入预训练目标检测网络(如 Faster R-CNN)得到对象边界框，筛选出对象提议(proposal)，用其卷积特征作视觉表征(图 3a)。优点是能有效避免背景干扰，利于目标选择；缺点是需预先生成提议、计算开销大、推理速度慢，且性能受提议质量制约。
      - **网格卷积粒度**：借鉴一阶段检测器思想，直接将整层卷积特征划分为 S×S 网格(如用 ResNet 输出，图 3b)，无需生成提议，在获得相近准确率的同时显著提升推理速度(论文称至少加速 10 倍)。
      - **图像块粒度**：借鉴 ViT(Dosovitskiy 等 2021)思想，将图像在空间维度直接划分为图像块(patch)、线性映射成 1 维序列作为 Transformer 视觉输入(图 3c)，无需卷积网络或检测器，实现更轻量、更快的特征提取。
  3.  **视觉—文本特征融合推理模块(第二级分类依据，REC 最核心模块)**：
      - **基于区域卷积粒度(5 个子类)**：
          - *早期方法*：CNN-LSTM 框架直接计算各对象区域提议与整个表达式的匹配得分(MMI，Mao 等 2016，用最大互信息思想设计损失；后续 Visdif 加同类提议差值、MIL 用多实例学习、SCRC 聚合空间信息)。在 RefCOCO 上准确率约 73.33%。
          - *基于注意力机制的融合*：用文本信息逐步修改区域提议的注意力权重，使定位"渐进化"且可解释(PLAN 用图像级+区域级两级注意力；A-ATT 累积注意力机制可显示高注意力区域与关键单词)。
          - *基于表达式分解的融合*：将表达式解析为语法结构做细粒度匹配(CMNs 用 3 个软注意拆解主语/关系/宾语三元组；GroundNet 用外部解析器+语法树；NMTree 在依赖解析树上自下而上累积区域置信度)。
          - *基于图网络的融合*：用图建模对象间关系，节点表对象、边表关系，文本特征用于计算节点/边注意力得分修正图(LGRAN 语言引导图注意；DGA 动态图注意做多步迭代推理；SGMN 场景图引导；SeMBI 三分支隐式/显式关系图+视觉属性图)。
          - *基于 Transformer 的融合*：将区域提议特征线性映射为视觉 Token 与文本 Token 融合(ViLBERT 双流+交叉注意力；VL-BERT 单流+拼接融合)。
      - **基于网格卷积粒度(2 个子类)**：
          - *基于滤波的融合*：用文本特征生成滤波核对视觉特征做相关滤波(FAOA 用 Darknet 多级卷积特征+1×1 卷积核滤波，推理速度达区域卷积方法的 10 倍；RCCF 将 REC 重定义为跨模态模板匹配，先滤波定位中心点再回归大小/偏移)。
          - *基于 Transformer 的融合*：将网格卷积特征划块映射为 Token 与文本 Token 做 Transformer 融合(TransVG 双流+拼接融合，引入 REG token 回归框；VGTR 文本指导的视觉编码器、交叉注意力;MDETR、OFA 大规模 VLP 预训练)。
      - **基于图像块粒度**：视觉与文本融合模块**都用 Transformer**，并趋向将特征提取与融合更紧密结合(QRNet 的查询感知动态注意模块实现文本指导的视觉特征细化；TransVG++ 删除独立融合模块、将视觉 Transformer 最后一层改为语言指导的视觉编码器，设计 language prompter 与 language adapter 两种注意力方案)。

- **训练与推理**：多数方法端到端训练；定位头输出边界框坐标，损失依方法不同(如 MMI 用最大互信息思想设计损失)。提取文本未统一给出各方法的损失函数公式细节。

- **与已有方法差异**：本文分类法不同于以往"一阶段/二阶段"的简单二分(Qiao 等 2021)。它从**视觉表征这一基础环节**切入，并深入到**融合模块的设计哲学**，更能反映技术演进的内在逻辑(从依赖外部检测器到摆脱依赖，从模块化到端到端)。

## 实验

> 本文为综述，"实验"即对已有方法的横向性能/速度汇总(表 1、表 3)，非作者自做实验。

- **使用数据集**：主流为 **RefCOCO、RefCOCO+、RefCOCOg**，基于 COCO 图像，具不同表达式风格与划分(val/testA/testB；RefCOCOg 另有 val*/val/test)。评估指标为定位准确率(%)。
- **主实验结果(表 1，加粗为当前最优值，"-" 表示文献无数据)**：
    - 早期方法 MMI 在 RefCOCO testA 仅 64.90%、testB 54.51%；Visdif testA 62.50%。
    - 基于注意力的 **CM-Att-Erase** 在 RefCOCO testA 达 **83.14%**(val 78.35%、testB 71.32%)，相比早期最优方法 VaruContext 提升近 10 个百分点。
    - 基于图网络/分解：NMTree RefCOCO testA 81.21%、MAttNet testA 81.14%、DGA testA 78.42%。
    - **OFA**(网格卷积粒度+大规模 VLP 预训练)在 RefCOCO val 达 **90.05%**、testA 92.93%，为当前最优；在 RefCOCO+/RefCOCOg 上也整体领先。
    - 基于图像块粒度：**TransVG++** RefCOCO val **86.28%**、testA 88.37%；QRNet val 84.01%、testA 85.85%。
    - 论文据表 1 指出：区域提议粒度方法通过加注意力/解析器/图网络后性能提升近 20%；网格卷积方法在 Transformer 建模下相比 ViLBERT、VL-BERT 提升超 10%。
- **效率信息(表 3，准确率为 RefCOCO val 评估)**：
    - **VaruContext 383ms、DGA 330ms、MAttNet 320ms**(均区域卷积粒度)。
    - **FAOA 23ms、RCCF 25ms、VGTR 40ms**(网格卷积粒度)。RCCF 在单个 Titan Xp 上约 40 帧/s，约为区域卷积特征方法的 12～16 倍；论文称 FAOA、RCCF 是 VaruContext 等区域卷积方法的 10 倍以上。
- **消融实验**：综述层面提及 QRNet 查询感知动态注意模块、TransVG++ 的 language prompter vs language adapter 等设计，但提取文本中未给出具体消融对比数字。

## 局限

- **综述性质**：核心价值是梳理而非提出新方法，追求最新突破的读者需结合具体原始论文阅读。
- **实验数据完整性**：表 1、表 3 存在大量"-"(文献无相关数据)，部分方法无法全面横向比较。
- **视频/3D 讨论深度**：虽展望了这些方向，但提取覆盖的文本(前 12 页)未展开具体讨论，内容相对概略(原文后续页可能有更多展望，提取缓存未覆盖，待核)。
- **复现的间接性**：不提供模型代码或训练细节，复现需查阅其引用的每一篇原始论文。

## 个人评论

这篇综述最大的价值在于其**分类框架的系统性与前瞻性**。它不仅告诉读者"有哪些方法"，更揭示了"为什么这样分类"以及"技术如何演进"。对研究者而言：

1.  **提供了清晰的研究地图**：以"视觉表征粒度"为主轴，把 REC 演进串成一条逻辑链——早期匹配 → 注意力 → 表达式分解 → 图网络 → Transformer，并在每个粒度下对应到具体融合范式，一目了然。这条主轴比"一阶段/二阶段"二分更能解释**速度为何提升**(摆脱区域提议)与**精度为何提升**(融合模块的演进)。
2.  **揭示了关键技术权衡**：区域卷积粒度精度高但速度慢(表 3 中 320～383ms)，网格卷积粒度速度快(23～40ms、约 10 倍以上加速)且精度相近，图像块粒度与 Transformer 天然契合且最轻量。这为选择或设计新方法提供了根本依据。
3.  **指明了未来趋势**：强调大规模多模态预训练(OFA 在 RefCOCO val 达 90.05%)的潜力，以及将视觉特征提取与融合模块深度融合(QRNet、TransVG++)的必要性。
4.  **可改进之处**：表格大量"-"削弱了横向可比性；不同方法的视觉骨干(VGG16 / ResNet-101 / DarkNet-53 / Swin / ViT)差异大，单看准确率难以剥离"骨干红利"与"方法红利"，论文未对此做受控对比，读者需自行警惕。

### 使用建议

- **如果快速了解**：读摘要、引言、第 1 节(处理流程)、图 4(分类图)、第 4 节(挑战与展望)，即可掌握 REC 核心概念、分类框架与发展方向。
- **如果复现**：本文是索引。确定感兴趣的方法类别后，重点查其引用的原始论文(如 TransVG、OFA、QRNet 等)及对应开源代码。
- **如果借鉴创新点**：学习其两级分类思路(可迁移到 VQA、图像描述等多模态任务)；关注其提出的三大挑战(速度、可解释性、推理能力)作为切入点；研究图 9 的三种 Transformer 融合注意力(相加/拼接/交叉)这一主流融合范式。
- **如果写 related work**：可将本文作为 REC / 视觉定位任务的中文经典综述引用，说明该领域分类体系与发展概况。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是计算机视觉与自然语言处理交叉的**图像—文本多模态指代表达理解(Referring Expression Comprehension, REC)综述**，发表于《中国图象图形学报》2023 年第 28 卷第 5 期(页 1308-1325)。REC 旨在根据一个完整的描述性句子(指代表达式)，在含多个对象的图像中**唯一地**定位目标对象。它与短语定位同为视觉定位(VG)的子任务，与指代表达分割(RES)互为"框 vs 分割"的姊妹任务。由于该任务横跨 CV 与 NLP、且本身是综述，在本库 taxonomy 中归入视觉—语言交叉的通用类 `T_通用_NLP_其他` 较为合适。

## 2. 一句话总结
本文从计算机视觉视角出发，以**视觉表征粒度**(区域卷积/网格卷积/图像块)为第 1 级、以**视觉—文本融合模块建模方式**为第 2 级，提出 REC 方法的**两级分类框架**，并系统汇总了代表方法、四个数据集、性能/速度表格与三大未来挑战。

## 3. 背景与问题
- **为什么要做**：REC 在导航、自动驾驶、视频监控、机器人、早期教育等智能设备的视觉理解/对话系统中应用前景广泛；多模态数据爆发使该任务受 CV 与 NLP 双重关注。
- **与相邻任务区别**：相比目标检测在固定类别上定位(COCO mAP 已达 63.2%)，REC 目标对象无固定类别、完全由表达式决定，更具挑战；相比短语定位(定位句中所有对象)，REC 只唯一定位表达式描述的特定对象；RES 则是分割版本。
- **之前综述的不足**：针对 REC 仅有 1 篇 2021 年英文综述(Qiao 等)，全面但分析不深、未覆盖近两年 Transformer 方法。
- **核心矛盾**：视觉数据信息丰富但冗余干扰多，有效视觉特征是定位基础；既要充分理解表达式语义(属性、关系)，又要对多对象图像做关系推理，并兼顾速度、可解释性与对长难表达式的推理能力。

## 4. 核心贡献
1.  **两级分类框架**：第 1 级=视觉表征粒度(区域卷积/网格卷积/图像块)，第 2 级=视觉—文本融合建模方式；明确区别于 Qiao 等(2021)的一阶段/二阶段二分法。
2.  **梳理三模块处理流程**：文本特征提取、视觉特征提取、视觉—文本融合推理(图 2)，并分析各模块演进。
3.  **总结 Transformer 融合**：归纳相加/拼接/交叉三种多模态注意力(图 9)，并在表 2 中给出 8 个代表方法(ViLBERT、VL-BERT、TransVG、VGTR、MDETR、OFA、QRNet、TransVG++)各自的视觉输入粒度与注意力类别。
4.  **数据集与指标**：基于 4 个流行数据集(RefCOCO/RefCOCO+/RefCOCOg 等)介绍任务，指标为定位准确率(%)。
5.  **三大挑战与展望**：推理速度、可解释性、对表达式的推理能力；并从模型设计与领域发展两方面展望视频、3D 方向。

## 5. 方法详解
**框架**：不提新模型，而提分析框架(图 4)。先按视觉特征提取的输出粒度分三类，再按融合模块设计细分。

- **输入输出**：图像 + 文本表达式 → 目标对象边界框坐标。
- **文本特征提取**：LSTM(早期)→ 表达式分解(三元组/外部解析器)→ 预训练 BERT。
- **视觉特征提取(分类核心，图 3)**：
  - 区域卷积粒度(图 3a)：Faster R-CNN 等检测器生成对象提议、取其卷积特征——能避背景干扰，但需预生成提议、慢、受提议质量制约。
  - 网格卷积粒度(图 3b)：直接用 ResNet 整层卷积特征划成 S×S 网格——无需提议、速度提升(≥10 倍)、精度相近。
  - 图像块粒度(图 3c)：仿 ViT 把图像切块线性映射成 1 维序列直送 Transformer——无需 CNN/检测器、最轻量。
- **视觉—文本融合(第二级分类，REC 最核心模块)**：
  - 区域卷积下 5 子类：早期匹配(MMI/Visdif/MIL/SCRC) → 注意力(PLAN/A-ATT) → 表达式分解(CMNs/GroundNet/NMTree) → 图网络(LGRAN/DGA/SGMN/SeMBI) → Transformer(ViLBERT 双流交叉/VL-BERT 单流拼接)。
  - 网格卷积下 2 子类：滤波(FAOA 用 1×1 卷积核滤波；RCCF 跨模态模板匹配) → Transformer(TransVG 拼接+REG token；VGTR 交叉注意力；MDETR、OFA 大规模 VLP 预训练)。
  - 图像块下：融合模块全用 Transformer，趋向特征提取与融合一体化(QRNet 查询感知动态注意；TransVG++ language prompter / language adapter)。
- **与已有差异**：从视觉表征基础环节切入并深入融合模块设计哲学，比一阶段/二阶段二分更能反映"从依赖检测器到摆脱依赖、从模块化到端到端"的演进逻辑。

## 6. 实验与结果
- **数据集/指标**：RefCOCO、RefCOCO+、RefCOCOg(基于 COCO，含 val/testA/testB 等划分)，指标为定位准确率(%)。
- **表 1 关键数字(加粗=当前最优)**：
  - 早期方法弱(MMI RefCOCO testA 64.90%、testB 54.51%)。
  - 注意力 CM-Att-Erase RefCOCO testA **83.14%**(较早期最优 VaruContext 提升近 10 点)。
  - 分解/图网络 NMTree testA 81.21%、MAttNet testA 81.14%、DGA testA 78.42%。
  - **OFA**(网格卷积+VLP)RefCOCO val **90.05%**、testA 92.93%，当前最优。
  - 图像块 **TransVG++** val **86.28%**、testA 88.37%；QRNet val 84.01%。
  - 论文据表 1 总结：区域卷积方法加注意力/解析/图网络后提升近 20%；网格卷积 Transformer 法相比 ViLBERT/VL-BERT 提升超 10%。
- **表 3 速度(RefCOCO val 准确率)**：区域卷积 VaruContext 383ms / DGA 330ms / MAttNet 320ms；网格卷积 FAOA 23ms / RCCF 25ms(约 40 帧/s，约区域卷积法 12～16 倍)/ VGTR 40ms。FAOA、RCCF 整体为 VaruContext 等的 10 倍以上。
- **消融**：综述层面提及 QRNet 动态注意、TransVG++ 两种融合方案，但提取文本无具体消融数字。

## 7. 这篇论文真正有价值的地方
1.  **清晰的研究地图**：用"视觉表征粒度"主轴串起 REC 演进(匹配→注意力→分解→图网络→Transformer)，每个粒度对应具体融合范式，比一阶段/二阶段二分更解释力强。
2.  **关键技术权衡量化**：区域卷积精度高但慢(320～383ms)，网格卷积快(23～40ms、≥10 倍加速)且精度相近，图像块与 Transformer 天然契合且最轻量。
3.  **指明趋势**：大规模 VLP 预训练(OFA val 90.05%)+ 视觉提取与融合一体化(QRNet、TransVG++)是两大方向。
4.  **批判视角的留白**：各方法骨干差异大(VGG16/ResNet-101/DarkNet-53/Swin/ViT)，纯比准确率难剥离骨干红利，论文未做受控对比——这一点读者需自行警惕。

## 8. 局限与问题
- 综述性质，重梳理轻创新，需结合原始论文。
- 表 1、表 3 大量"-"，横向比较受限。
- 视频/3D 展望在提取覆盖的前 12 页未展开(原文后续页或有更多，提取缓存未覆盖，待核)。
- 不提供代码/训练细节，复现需逐篇查引文。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + 第 1 节 + 图 4 + 第 4 节。
- **复现**：作索引，按方法类别查 TransVG、OFA、QRNet 等原始论文与开源代码。
- **借鉴创新**：迁移两级分类思路到 VQA/图像描述；以三大挑战为切入点；研究图 9 三种 Transformer 融合注意力。
- **写 related work**：作为 REC/视觉定位的中文经典综述引用，说明分类体系与发展概况。

## 10. 和其他论文的关系
本文是视觉—语言交叉的 REC 综述(`T_通用_NLP_其他`)，与以下方向密切相关：
- **视觉定位/短语定位(Visual Grounding / Phrase Localization)**：REC 的母任务与姊妹子任务。
- **指代表达分割(RES)**：分割版指代任务(Hu 等 2016；Li 等 2018)。
- **多模态预训练模型**：ViLBERT、VL-BERT、MDETR、OFA。
- **Transformer 视觉应用**：ViT、TransVG/TransVG++、QRNet(Swin)。
- **目标检测基石**：Faster R-CNN、一阶段检测器(为区域/网格卷积粒度提供视觉骨干)。

## 11. 关键词
指代表达理解(REC)，视觉定位(VG)，视觉与语言，视觉表征粒度，多模态特征融合，Transformer，注意力机制，图网络，预训练模型，综述

## 12. 可信度说明
本精读基于提供的 PDF 提取文本生成。提取缓存标注 12/18 页(约 25000 字符)，完整覆盖了**标题、中英文摘要、引言(第 0 节)、处理流程(第 1 节，含 1.1-1.3)、方法分类(第 2 节 2.1-2.3，含各子类代表方法)、表 1(性能比较)、表 2(Transformer 融合方法)、表 3(推理速度)**。笔记中的具体数字(CM-Att-Erase 83.14%、OFA 90.05%、TransVG++ 86.28%、RCCF 25ms/40fps、VaruContext 383ms、COCO mAP 63.2% 等)均可在提取文本中逐一核对。由于提取仅含前 12 页(共 18 页)，**第 3 节数据集详细划分、第 4 节挑战与展望的展开、参考文献列表**等后续内容在本次提取中缺失，相关描述已标注"提取缓存未覆盖/未明确"。整体忠于所给文本，未编造。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页); 提取缓存标注 12/18 页, 已覆盖摘要/引言/处理流程/方法分类/表 1-3); 来源缓存: `.paper-cache/extracts/cjig_paper_3.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。已据提取文本重建英文摘要、核对全部性能/速度数字。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-18; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-18。
- **提取情况**: 缺失页 6 页, 其中 6 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.15: Referring image segmentation via recurrent refinement networks//
- p.15: Proceedings of 2018 IEEE/CVF Conference on Computer Vision
- p.17: Proceedings of 2022 IEEE/CVF Conference on Computer Vision

### 缺失页关键摘录

- p.14: new dataset and task on compositional referring expression compre ⁃
- p.15: The segmented and annotated IAPR TC -12 benchmark . Computer
- p.15: TC12 benchmark ： a new evaluation resource for visual information
<!-- AI_READING_NOTE_END -->
