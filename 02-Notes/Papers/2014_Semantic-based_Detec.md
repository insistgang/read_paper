---
title: Semantic-based Detection of Segment Outliers and Unusual
authors:
  - "Lianli Gao"
  - "Michael Bruenig"
  - "Jane Hunter"
year: 2014
venue: nature, variability and heterogeneity of sensors (the devices that detect or measure a physical property),
doi: 
pdf: [[2014_Semantic-based_Detec.pdf]]
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2014_Semantic-based_Detec.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/18 pages"
---
# Semantic-based Detection of Segment Outliers and Unusual

## 基本信息
- **PDF**: [[2014_Semantic-based_Detec.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Semantic-based Detection of Segment Outliers and Unusual |
| **作者** | Lianli Gao; Michael Bruenig; Jane Hunter |
| **发表时间** | 2014 |
| **刊物/会议** | nature, variability and heterogeneity of sensors (the devices that detect or measure a physical property), |
| **DOI** | 未明确 |

## 摘要

> : Environmental scientists have increasingly been deploying wireless sensor networks to capture valuable data that measures and records precise information about our environment. One of the major challenges associated with wireless sensor networks is the quality of the data – and more specifically the detection of segment outliers and unusual events. Most previous research has focused on detecting outliers that are errors that are caused by unreliable sensors and sensor nodes. However, there is an urgent need for the development of new tools capable of identifying, tagging and visualizing erroneous segment outliers and unusual events from sensor data streams. In this paper, we present a SOUE-Detector (Segment Outlier and Unusual Event-Detector) system for wireless sensor networks that combines statistical analyses using Dynamic Time Warping (DTW) with domain expert knowledge (captured via an ontology and semantic inferencing rules). The resulting Web portal enables scientist to efficie

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做这项研究**：环境科学家广泛使用无线传感器网络（WSN）收集环境数据，但低成本传感器和恶劣环境导致数据质量低下，存在噪声、故障、缺失等问题。从这些不可靠的数据流中准确识别有价值的真实异常事件（如微气候变化）是决策支持的关键。
- **之前方法有什么问题**：
    1.  **假设局限**：大多数现有研究默认所有离群点都是错误，没有尝试区分“错误离群点”和代表真实事件的“真实离群点”。
    2.  **数据维度**：多数方法假设传感器数据是单变量的，忽略了多变量数据间的关联。
    3.  **动态性处理不足**：对传感器、节点和网络配置的动态变化（如节点移动、传感器增删）考虑不足。
    4.  **知识依赖**：监督学习需要训练数据，而在异常检测场景中通常缺乏先验标签数据。
    5.  **知识忽略**：忽略了传感器属性之间的相关性（如温度与湿度的负相关），而这些相关性对检测真实事件至关重要。
- **作者想解决的核心矛盾**：如何**不依赖预先定义的异常规则或带标签的训练数据**，而是通过**整合动态的、多变量的传感器数据流本身的信息以及领域专家的关联性知识**，来可靠地将数据片段分类为“错误”或“真实异常事件”。
## 关键贡献

1.  **提出CESP本体**：通过扩展W3C的SSN本体，定义了“相关环境传感器属性本体”（CESP），形式化描述了传感器属性之间的多种相关性类型（强度、方向、形状、时空、构成），为推理提供了结构化知识基础。
2.  **设计语义增强的检测算法**：设计并实现了一种集成了统计分析（DTW）与语义Web技术的检测算法。该算法通过定义空间邻接矩阵、计算数据流相似度、并融合领域专家定义的关联规则，来区分错误和真实事件。
3.  **开发SOUE-Detector系统**：实现了一个完整的Web系统原型，包含数据存储、检测算法和可视化门户，使科学家能够搜索数据流并直观地查看被标记为“错误”或“异常事件”的片段。
4.  **解决领域知识整合问题**：提供了一个图形化用户界面，允许领域专家（如生态学家）直接输入和定义传感器属性之间的相关性规则（如“温度和湿度存在强负相关”），将隐性知识显性化用于检测。
5.  **提供端到端解决方案**：针对无线传感器网络数据质量的特定问题，提出了从数据存储、知识建模、算法设计到系统实现和评估的完整技术路线。
## 方法

- **整体框架**：系统分为五个主要步骤：1) 数据存储；2) 构建CESP本体；3) 设计与实现检测算法（核心）；4) 开发Web系统与可视化；5) 性能评估。
- **输入输出**：
    - **输入**：原始传感器数据流（包含节点ID、传感器ID、时间戳、观测值等元数据）、传感器网络配置信息、领域专家定义的相关性规则。
    - **输出**：对于给定时间窗口内的数据流片段，系统输出分类标签（“错误”或“真实异常事件”），并在Web地图和时间线上可视化。
- **关键模块**：
    1.  **空间邻接矩阵构建模块**：
        - 首先根据传感器节点间的地理距离（阈值定义）构建**传感器节点空间邻接矩阵**，确定节点间的邻居关系。
        - 然后结合网络配置（哪个传感器安装在哪个节点上），构建**传感器空间邻接矩阵**，用于后续计算同类型传感器数据流间的相似性。
    2.  **基于DTW的相似度计算模块**：
        - **机制**：对两个时间窗口（Δt）内的传感器数据流（观测值序列），将其转换为二维坐标系中的向量序列（时间差为x，观测值差为y）。使用**动态时间规整（DTW）** 计算两个序列的相似度。
        - **核心公式**：DTW的累积距离D(a,b)通过动态规划计算：`D(a,b) = min{ D(a-1,b-1), D(a-1,b), D(a,b-1) } + θ(v_a, v_b)`，其中θ是两个向量间的夹角（公式1），优于欧氏距离，能处理垂直平移。最终相似度由`sim = cos( D(u-1, u-1) / K )`计算（公式4），K是规整路径长度。
    3.  **可疑数据流检测模块**：对网络中每个传感器，计算其与其空间邻居（同类型传感器）数据流的DTW相似度。如果相似度低于预设阈值，则该传感器的数据流被标记为“可疑”。
    4.  **语义规则整合与事件判定模块**：
        - **领域知识输入**：专家通过GUI定义属性间的相关性规则（例如，`cesp:air_temperature cesp:hasNegativeCorrelation cesp:relative_humidity`）。
        - **推理流程**：结合“可疑”检测结果和专家规则。例如，如果一个温度传感器数据可疑，而其关联的湿度传感器数据在相同时间段也表现出符合已知相关性规则的异常模式（如温度异常升高时湿度异常降低），则更可能判定为**真实异常事件**；反之，如果异常是孤立的，则更可能判定为**传感器错误**。
- **与已有方法的差异**：
    1.  **范式差异**：从“所有离群点都是错误”的假设，转变为**显式区分“错误”与“真实异常事件”**。
    2.  **知识融合**：不是单纯依赖统计阈值或监督学习，而是**主动融入领域专家关于属性相关性的结构化知识**，通过语义推理增强判断。
    3.  **动态建模**：通过维护传感器和节点的元数据（包括配置变化历史），能够**适应传感器网络的动态变化**。
## 实验

- **使用的数据集**：Springbrook无线传感器网络数据集（澳大利亚昆士兰州春溪国家公园）。实验使用了从2010年1月至2012年6月共2.5年的数据，具体聚焦于由Vaisala WXT520气象传感器采集的**气温、相对湿度和气压**三种观测，采样频率为每10分钟一次。
- **对比方法**：PDF文本中**未明确说明**与哪些具体的基线方法进行了对比。
- **评价指标**：**精确率（Precision）** 和 **召回率（Recall）**。
- **主实验结果**：文本中声明“实验结果表明SOUE-Detector能够以高水平的精确率和召回率高效检测片段离群点和异常事件”（p.8），但**未提供具体的数值结果**。
- **消融实验**：PDF文本中**未找到**关于消融实验的描述。
- **泛化实验**：PDF文本中**未找到**在其他数据集上的泛化实验。
- **速度/参数量/效率**：PDF文本中**未找到**关于算法运行时间、参数量或计算复杂度（如FLOPs）的详细讨论。
## 局限

- **领域专家知识依赖**：方法的有效性很大程度上依赖于领域专家能否提供准确、全面的相关性规则。获取这些知识本身可能成本高昂或存在主观性。
- **数据与场景局限**：实验仅在一个特定的环境监测网络（Springbrook）和三种气象传感器上进行验证，其在不同领域（如工业物联网）、不同类型传感器或更复杂事件模式下的泛化能力尚未证明。
- **算法细节不完整**：提供的PDF文本（前12页）中，关于检测算法如何具体**结合规则与可疑结果进行最终决策**的流程描述不够清晰，属于“研究进行中”的状态。
- **评估缺乏基准**：未提供与现有离群点检测方法的详细定量对比，使得其宣称的“高精度”和“高召回率”缺乏参照。
- **计算成本未讨论**：DTW计算和可能的大规模规则匹配在面对海量传感器数据流时的计算效率如何，文本中未提及。
## 个人评论

1.  **问题定义的价值**：清晰地将问题定义为区分“错误离群点”和“真实异常事件”，这是一个比传统异常检测更精细、更具现实意义的设定，直接关系到科学发现的有效性。
2.  **方法论的启发**：展示了如何将**结构化的领域知识（通过本体建模）与数据驱动的统计方法（DTW）** 相结合。这种“语义增强”的范式可以迁移到其他需要利用领域知识提升数据分析质量的场景。
3.  **系统化的研究思路**：论文提供了一个完整的案例研究流程，从问题分析、数据收集、本体设计、算法提出、系统实现到实验评估，为进行类似跨学科（计算科学+领域科学）研究提供了可参考的模板。
4.  **工具化思想**：开发了一个可供领域科学家直接使用的Web门户和规则输入界面，强调了研究的可落地性和对最终用户的支持，这种“工具驱动研究”的思路值得借鉴。

### 使用建议

- **如果快速了解**：只读**摘要（Abstract）**、**第1节引言（INTRODUCTION）**、**第2节目标（OBJECTIVES）** 和**第8节结论（CONCLUSION）**，可以迅速掌握论文的动机、核心想法和主要贡献。
- **如果复现**：重点阅读**第5节检测算法（DETECTION ALGORITHMS）**，特别是关于符号定义、DTW计算公式（公式1-4）和空间邻接矩阵构建的部分。同时需要结合**第4节CESP本体**来理解知识建模，并参考系统描述（第6节）来设计实验流程。
- **如果借鉴创新点**：
    1.  学习其**将领域知识形式化为本体并用于数据质量分析**的思路，可以尝试将此模式应用于其他数据清洗或异常检测问题。
    2.  学习其**在时间序列分析中融合空间邻居信息和属性关联规则**的算法框架，可用于其他多变量时间序列异常检测。
- **如果写related work**：可放在以下类别：无线传感器网络数据质量、基于语义/本体的异常检测、时间序列离群点检测、环境监测数据分析。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**无线传感器网络（WSN）数据质量分析与语义Web技术相结合**的交叉研究方向。它旨在解决环境监测中无线传感器网络产生的数据流质量问题，特别是如何区分由传感器故障引起的“错误离群点”和由真实环境事件引起的“真实异常事件”。根据提供的主题标签 `T_通用_NLP_其他`，该论文可归类为**自然语言处理（NLP）和语义Web技术在非传统文本数据（传感器数据流）上的应用**，具体属于数据质量检测和事件识别范畴。

## 2. 一句话总结
本文提出了一个名为SOUE-Detector的系统，通过结合动态时间规整（DTW）统计分析和基于本体的领域专家知识语义推理规则，来自动检测无线传感器数据流中的“片段离群点”，并区分它们是传感器错误还是真实的环境异常事件。

## 3. 背景与问题
- **为什么要做这项研究**：环境科学家广泛使用无线传感器网络（WSN）收集环境数据，但低成本传感器和恶劣环境导致数据质量低下，存在噪声、故障、缺失等问题。从这些不可靠的数据流中准确识别有价值的真实异常事件（如微气候变化）是决策支持的关键。
- **之前方法有什么问题**：
    1.  **假设局限**：大多数现有研究默认所有离群点都是错误，没有尝试区分“错误离群点”和代表真实事件的“真实离群点”。
    2.  **数据维度**：多数方法假设传感器数据是单变量的，忽略了多变量数据间的关联。
    3.  **动态性处理不足**：对传感器、节点和网络配置的动态变化（如节点移动、传感器增删）考虑不足。
    4.  **知识依赖**：监督学习需要训练数据，而在异常检测场景中通常缺乏先验标签数据。
    5.  **知识忽略**：忽略了传感器属性之间的相关性（如温度与湿度的负相关），而这些相关性对检测真实事件至关重要。
- **作者想解决的核心矛盾**：如何**不依赖预先定义的异常规则或带标签的训练数据**，而是通过**整合动态的、多变量的传感器数据流本身的信息以及领域专家的关联性知识**，来可靠地将数据片段分类为“错误”或“真实异常事件”。

## 4. 核心贡献
1.  **提出CESP本体**：通过扩展W3C的SSN本体，定义了“相关环境传感器属性本体”（CESP），形式化描述了传感器属性之间的多种相关性类型（强度、方向、形状、时空、构成），为推理提供了结构化知识基础。
2.  **设计语义增强的检测算法**：设计并实现了一种集成了统计分析（DTW）与语义Web技术的检测算法。该算法通过定义空间邻接矩阵、计算数据流相似度、并融合领域专家定义的关联规则，来区分错误和真实事件。
3.  **开发SOUE-Detector系统**：实现了一个完整的Web系统原型，包含数据存储、检测算法和可视化门户，使科学家能够搜索数据流并直观地查看被标记为“错误”或“异常事件”的片段。
4.  **解决领域知识整合问题**：提供了一个图形化用户界面，允许领域专家（如生态学家）直接输入和定义传感器属性之间的相关性规则（如“温度和湿度存在强负相关”），将隐性知识显性化用于检测。
5.  **提供端到端解决方案**：针对无线传感器网络数据质量的特定问题，提出了从数据存储、知识建模、算法设计到系统实现和评估的完整技术路线。

## 5. 方法详解
- **整体框架**：系统分为五个主要步骤：1) 数据存储；2) 构建CESP本体；3) 设计与实现检测算法（核心）；4) 开发Web系统与可视化；5) 性能评估。
- **输入输出**：
    - **输入**：原始传感器数据流（包含节点ID、传感器ID、时间戳、观测值等元数据）、传感器网络配置信息、领域专家定义的相关性规则。
    - **输出**：对于给定时间窗口内的数据流片段，系统输出分类标签（“错误”或“真实异常事件”），并在Web地图和时间线上可视化。
- **关键模块**：
    1.  **空间邻接矩阵构建模块**：
        - 首先根据传感器节点间的地理距离（阈值定义）构建**传感器节点空间邻接矩阵**，确定节点间的邻居关系。
        - 然后结合网络配置（哪个传感器安装在哪个节点上），构建**传感器空间邻接矩阵**，用于后续计算同类型传感器数据流间的相似性。
    2.  **基于DTW的相似度计算模块**：
        - **机制**：对两个时间窗口（Δt）内的传感器数据流（观测值序列），将其转换为二维坐标系中的向量序列（时间差为x，观测值差为y）。使用**动态时间规整（DTW）** 计算两个序列的相似度。
        - **核心公式**：DTW的累积距离D(a,b)通过动态规划计算：`D(a,b) = min{ D(a-1,b-1), D(a-1,b), D(a,b-1) } + θ(v_a, v_b)`，其中θ是两个向量间的夹角（公式1），优于欧氏距离，能处理垂直平移。最终相似度由`sim = cos( D(u-1, u-1) / K )`计算（公式4），K是规整路径长度。
    3.  **可疑数据流检测模块**：对网络中每个传感器，计算其与其空间邻居（同类型传感器）数据流的DTW相似度。如果相似度低于预设阈值，则该传感器的数据流被标记为“可疑”。
    4.  **语义规则整合与事件判定模块**：
        - **领域知识输入**：专家通过GUI定义属性间的相关性规则（例如，`cesp:air_temperature cesp:hasNegativeCorrelation cesp:relative_humidity`）。
        - **推理流程**：结合“可疑”检测结果和专家规则。例如，如果一个温度传感器数据可疑，而其关联的湿度传感器数据在相同时间段也表现出符合已知相关性规则的异常模式（如温度异常升高时湿度异常降低），则更可能判定为**真实异常事件**；反之，如果异常是孤立的，则更可能判定为**传感器错误**。
- **与已有方法的差异**：
    1.  **范式差异**：从“所有离群点都是错误”的假设，转变为**显式区分“错误”与“真实异常事件”**。
    2.  **知识融合**：不是单纯依赖统计阈值或监督学习，而是**主动融入领域专家关于属性相关性的结构化知识**，通过语义推理增强判断。
    3.  **动态建模**：通过维护传感器和节点的元数据（包括配置变化历史），能够**适应传感器网络的动态变化**。

## 6. 实验与结果
- **使用的数据集**：Springbrook无线传感器网络数据集（澳大利亚昆士兰州春溪国家公园）。实验使用了从2010年1月至2012年6月共2.5年的数据，具体聚焦于由Vaisala WXT520气象传感器采集的**气温、相对湿度和气压**三种观测，采样频率为每10分钟一次。
- **对比方法**：PDF文本中**未明确说明**与哪些具体的基线方法进行了对比。
- **评价指标**：**精确率（Precision）** 和 **召回率（Recall）**。
- **主实验结果**：文本中声明“实验结果表明SOUE-Detector能够以高水平的精确率和召回率高效检测片段离群点和异常事件”（p.8），但**未提供具体的数值结果**。
- **消融实验**：PDF文本中**未找到**关于消融实验的描述。
- **泛化实验**：PDF文本中**未找到**在其他数据集上的泛化实验。
- **速度/参数量/效率**：PDF文本中**未找到**关于算法运行时间、参数量或计算复杂度（如FLOPs）的详细讨论。

## 7. 这篇论文真正有价值的地方
1.  **问题定义的价值**：清晰地将问题定义为区分“错误离群点”和“真实异常事件”，这是一个比传统异常检测更精细、更具现实意义的设定，直接关系到科学发现的有效性。
2.  **方法论的启发**：展示了如何将**结构化的领域知识（通过本体建模）与数据驱动的统计方法（DTW）** 相结合。这种“语义增强”的范式可以迁移到其他需要利用领域知识提升数据分析质量的场景。
3.  **系统化的研究思路**：论文提供了一个完整的案例研究流程，从问题分析、数据收集、本体设计、算法提出、系统实现到实验评估，为进行类似跨学科（计算科学+领域科学）研究提供了可参考的模板。
4.  **工具化思想**：开发了一个可供领域科学家直接使用的Web门户和规则输入界面，强调了研究的可落地性和对最终用户的支持，这种“工具驱动研究”的思路值得借鉴。

## 8. 局限与问题
- **领域专家知识依赖**：方法的有效性很大程度上依赖于领域专家能否提供准确、全面的相关性规则。获取这些知识本身可能成本高昂或存在主观性。
- **数据与场景局限**：实验仅在一个特定的环境监测网络（Springbrook）和三种气象传感器上进行验证，其在不同领域（如工业物联网）、不同类型传感器或更复杂事件模式下的泛化能力尚未证明。
- **算法细节不完整**：提供的PDF文本（前12页）中，关于检测算法如何具体**结合规则与可疑结果进行最终决策**的流程描述不够清晰，属于“研究进行中”的状态。
- **评估缺乏基准**：未提供与现有离群点检测方法的详细定量对比，使得其宣称的“高精度”和“高召回率”缺乏参照。
- **计算成本未讨论**：DTW计算和可能的大规模规则匹配在面对海量传感器数据流时的计算效率如何，文本中未提及。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读**摘要（Abstract）**、**第1节引言（INTRODUCTION）**、**第2节目标（OBJECTIVES）** 和**第8节结论（CONCLUSION）**，可以迅速掌握论文的动机、核心想法和主要贡献。
- **如果复现**：重点阅读**第5节检测算法（DETECTION ALGORITHMS）**，特别是关于符号定义、DTW计算公式（公式1-4）和空间邻接矩阵构建的部分。同时需要结合**第4节CESP本体**来理解知识建模，并参考系统描述（第6节）来设计实验流程。
- **如果借鉴创新点**：
    1.  学习其**将领域知识形式化为本体并用于数据质量分析**的思路，可以尝试将此模式应用于其他数据清洗或异常检测问题。
    2.  学习其**在时间序列分析中融合空间邻居信息和属性关联规则**的算法框架，可用于其他多变量时间序列异常检测。
- **如果写related work**：可放在以下类别：无线传感器网络数据质量、基于语义/本体的异常检测、时间序列离群点检测、环境监测数据分析。

## 10. 和其他论文的关系
根据论文主题“语义检测”和“无线传感器网络”，可能的相关论文包括：
- 基于语义Web的传感器网络描述框架相关工作，如Compton等人关于SSN本体的论文 `[[]]`。
- 使用动态时间规整（DTW）进行时间序列相似性计算和异常检测的相关研究。
- 其他针对无线传感器网络数据清洗和错误检测的统计或机器学习方法。
（由于缺乏完整的文献列表和具体细节，无法建立更精确的双链关联。）

## 11. 关键词
无线传感器网络 (WSN), 数据质量, 异常检测, 离群点检测, 动态时间规整 (DTW), 语义Web, 本体, 领域知识, 环境监测, Springbrook, 片段离群点, 异常事件

## 12. 可信度说明
本精读笔记**完全基于提供的PDF提取文本（论文的前12页，共18页）生成**。所有描述的方法细节、算法公式、贡献点和背景问题均严格从该文本中提取和归纳。对于文本中明确声明但未提供具体内容的部分（如具体的实验精确率/召回率数值、消融实验细节、与基线方法的对比），均已在笔记中明确标注“未提供”或“未找到”。笔记内容忠实反映了该研究进行中（Research-in-Progress）论文在引言、方法框架和初步系统设计阶段的工作，但无法包含可能存在于后续章节（第13-18页）的完整实验结果和结论部分。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2014_Semantic-based_Detec.txt` (18/18 页; 原 AI 主体 12/18 + 全文补读 13-18); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-18; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-18。
- **提取情况**: 缺失页 6 页, 其中 6 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Selecting rela tive humidity sensor 10 and air temperature sensor 10 (and their neighborhood sensors),
- p.13: These graphs show the following:
- p.13: These results indicate that the relative humidity and air temperature both changed simultaneously at
- p.14: 7. EV ALUATION
- p.14: 7.1 Evaluation Metrics
- p.14: To conduct our evaluations, we collected a real dataset from 36 sensor nodes deployed in the Springbroo k
- p.14: The first test dataset contains 155,520 relative humidity observations, 155,520 air temperature
- p.15: National Park
- p.15: Segment Outliers (
- p.15: Events with cesp:hasStrongCorrelation
- p.15: Events with cesp:hasPosi tiveCorrelation
- p.15: The remaining two test datasets are created by adding unusual events with two types of correlations,

### 缺失页关键摘录

- p.13:  Fig.4 (b-2) reveals that the pat tern for relative humidity sensor 10 is different from the patterns for its
- p.13:  Fig.4 (b-3) reveals that the pattern of air temperature sensor 10 is different from the patterns for its
- p.14: To conduct our evaluations, we collected a real dataset from 36 sensor nodes deployed in the Springbroo k
- p.14: real dataset s, we generated three test dataset s by adding segment outliers and unusual events to a cleaned
- p.14: The first test dataset is created by adding erroneous segment outliers to the cleaned dataset. The
- p.14: The first test dataset contains 155,520 relative humidity observations, 155,520 air temperature
- p.15: Fig.5: 36 sensor nodes deployed in the Springbrook
- p.15: including cesp:hasStrongCorrelation, and cesp:hasPosi tiveCorrelation , to the cleaned dataset.
- p.15: Specifically, to create each test dataset, we randomly selected 8 sensor nodes. For each sensor node, we
- p.15: steps 30 times. Finally , each test dataset contains 155 ,520 relative humidity observations, 155 ,520 air
- p.15: each test dataset contains one type of unusual even t.
- p.16: outliers and unusual events. Fig.6 shows the precision and recall for detecting erroneous segments from
<!-- AI_READING_NOTE_END -->
