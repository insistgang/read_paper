---
title: "Deep Learning in Remote Sensing: A Review"
authors:
  - "Xiao Xiang Zhu"
  - "Devis Tuia"
  - "Lichao Mou"
  - "Gui-Song Xia"
  - "Liangpei Zhang"
  - "Friedrich Fraundorfer"
year: 2017
venue: "Deep Learning in Remote Sensing: A Review"
doi: 
pdf: [[2017_Deep_learning_in_rem.pdf]]
primary_topic: R1_遥感_高光谱_变化检测
topics:
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
- **primary_topic**: `R1_遥感_高光谱_变化检测`
- **topics**: `R1_遥感_高光谱_变化检测`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Deep Learning in Remote Sensing: A Review |
| **作者** | Xiao Xiang Zhu; Devis Tuia; Lichao Mou; Gui-Song Xia; Liangpei Zhang; Friedrich Fraundorfer |
| **发表时间** | 2017 |
| **刊物/会议** | Deep Learning in Remote Sensing: A Review |
| **DOI** | 未明确 |

## 摘要

> This is the pre-acceptance version, to read the final version please go to IEEE Geoscience and Remote Sensing Magazine on IEEE XPlore. Standing at the paradigm shift towards data-intensive science, machine learning techniques are becoming increasingly important. In particular, as a major breakthrough in the field, deep learning has proven as an extremely powerful tool in many fields. Shall we embrace deep learning as the key to all? Or, should we resist a “black-box” solution? There are controversial opinions in the remote sensing community. In this article, we analyze the challenges of using deep learning for remote sensing data analysis, review the recent advances, and provide resources to make deep learning in remote sensing ridiculously simple to start with. More importantly, we advocate remote sensing scientists to bring their expertise into deep learning, and use it as an implicit general model to tackle unprecedented large-scale influential challenges, such as climate change and

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：深度学习在计算机视觉等领域取得了巨大成功，正向各个领域渗透。遥感领域也开始拥抱深度学习，但由于遥感数据的独特性，其应用面临新的科学问题，亟需一篇系统性的综述来梳理现状、挑战和方向。
- **之前方法有什么问题**：传统的遥感数据分析依赖手工设计特征和浅层机器学习模型，这些模型在面对日益增长的、复杂的、多模态的遥感大数据时，其特征提取和泛化能力有限。
- **作者想解决的核心矛盾是什么**：核心矛盾在于，深度学习这一“数据驱动”的“黑盒”模型，与遥感科学作为一门“物理驱动”的、需要定量反演和置信度估计的测量科学之间，如何有效结合。作者希望通过综述推动社区思考如何将领域知识（如物理模型）作为先验重新引入深度学习框架，而不仅仅是追求全自动化的数据驱动。
## 关键贡献

基于提供的PDF文本，本文的具体贡献如下：
1.  **系统性地分析了将深度学习应用于遥感数据分析时面临的六大独特挑战**：数据多模态、数据地理定位、数据为测地学测量、时间变量的重要性、大数据挑战、以及需要反演物理/生化参数（而非仅分类检测）。
2.  **全面综述了深度学习在多个遥感应用方向的研究进展**，包括：高光谱图像分析（分类与异常检测）、合成孔径雷达（SAR）图像解译、高分辨率图像解译、多模态数据融合、以及三维重建（在提供的文本中，后几部分仅提及但未展开）。
3.  **提供了深度学习在遥感中应用的“入门工具箱”**，包括开源代码和数据仓库的资源链接（在Section IV，但提供的文本未包含具体内容）。
4.  **明确提出并倡导了一种研究理念**：遥感科学家应发挥自身专业优势，将深度学习视为一种“隐式通用模型”，用以应对气候变化、城市化等大规模挑战，并强调将物理模型等专家知识作为先验重新引入深度学习概念中。
## 方法

本文作为综述，并未提出单一的新模型，而是系统梳理并解释了深度学习中关键模型的结构和原理，并讨论了它们在遥感领域的适配与应用。以下根据提供的文本进行总结：

- **整体框架**：论文结构为“挑战分析 -> 基础模型回顾 -> 遥感应用综述 -> 工具与展望”。
- **核心基础模型详解**：
    1.  **自编码器及其变体**：介绍了自编码器（AE）、堆叠自编码器（SAE）、稀疏自编码器和受限玻尔兹曼机（RBM）/深度置信网络（DBN）。这些是早期用于无监督特征学习的深度模型。例如，AE通过编码-解码结构学习数据的压缩表示，其目标是最小化输入与重建输出之间的欧氏距离（第4-5页）。稀疏自编码器通过在损失函数中加入KL散度约束来鼓励隐藏层激活的稀疏性（第5页）。DBN通过堆叠RBM并逐层贪婪训练来构建深层生成模型（第6页）。
    2.  **卷积神经网络**：这是文本中讨论的重点。回顾了计算机视觉中的经典CNN架构：
        - **AlexNet**：使用ReLU激活函数、Dropout层、数据增强，并利用GPU训练，在ImageNet上取得突破（第7页）。
        - **VGG Net**：强调“更深的网络使用更小的卷积核（3x3）”，以增加网络深度并提升特征层次化表达能力（第7-8页）。
        - **ResNet**：通过引入“残差连接”（快捷连接）解决深层网络训练退化问题，使训练极深的网络（如152层）成为可能（第8页）。
        - **FCN**：全卷积网络，用于语义分割。其核心是使用卷积层替代全连接层，从而支持任意尺寸输入；通过编码器-解码器结构和跳跃连接实现端到端的像素级预测（第8-9页）。
- **应用于遥感的方法论**：在具体应用部分（如III-A 高光谱图像分析），综述了如何将上述基础模型适配到遥感任务中。例如：
    - **输入输出**：对于高光谱分类，输入可以是光谱向量（1D）、空间-光谱数据块（2D或3D）。输出是像素级的类别标签。
    - **关键模块与连接**：对于高光谱分类，研究尝试了1D CNN（处理光谱）、2D CNN（处理空间）和3D CNN（同时处理空间和光谱）。3D CNN通过三维卷积操作能更好地联合建模空间-光谱信息（第11-12页，图5）。
    - **与已有方法的差异**：相比传统浅层模型（如SVM），CNN等深度模型能够自动学习层次化、抽象的特征，理论上对数据的非线性建模能力更强，更鲁棒（第10-11页）。
## 实验

- **使用的数据集**：PDF文本中未明确说明本文作为综述所对比分析的具体实验数据集。但提到了一些高光谱数据集在相关研究中的应用，以及Sentinel卫星产生大量数据（如25 PB）作为大数据挑战的例证（第4页）。
- **对比方法**：本文未进行自己的实验，因此没有直接的对比方法。但在综述各类研究时，会提及传统方法（如SVM）作为对比基准。
- **评价指标**：PDF文本中未明确说明。
- **主实验结果**：本文的核心“结果”是统计发现。**图4**显示了自2014年以来，关于“遥感中深度学习”的论文数量呈指数增长（第9页）。此外，在介绍具体模型时，会引用相关研究的结果，例如AlexNet在ImageNet上取得15.4%的top-5错误率（第7页），ResNet在ILSVRC 2015取得3.6%的错误率（第8页）。
- **消融实验**：PDF文本中未明确说明。
- **泛化实验**：PDF文本中未明确说明。
- **速度/参数量/FLOPs**：未提供具体数字，但指出深度学习需要大量计算资源和大数据，GPU训练是关键（第7页）。
## 局限

- **方法深度有限**：作为一篇综述，本文对各项研究的介绍是概括性的，无法深入探讨某一具体方法的细节和局限性。
- **覆盖范围与前沿性**：提供的文本仅覆盖了论文的前12页，关于SAR、高分辨率图像、数据融合和3D重建等重要部分的详细内容未能看到。此外，本文发表于2017年，深度学习领域发展极快，文中综述的一些模型和观点可能已不是最新前沿。
- **缺乏定量对比**：本文没有提供一个统一的基准来定量对比不同深度学习方法在遥感任务上的性能，这使得读者难以判断各方法的相对优劣。
- **“倡导”的实践性**：将物理模型与深度学习深度融合是一个极具挑战性的方向，本文更多是提出理念，具体的、普适的技术路径仍需探索。
## 个人评论

这篇综述的最大价值在于其 **“格局”和“指引性”**。它超越了单纯的技术回顾，深刻剖析了遥感学科与深度学习方法论之间的契合点与矛盾点。对后续研究的启发在于：
1.  **问题导向而非技术堆砌**：它提醒研究者，应用深度学习于遥感时，不能盲目套用计算机视觉模型，必须首先思考遥感数据的独特性（多模态、时序、地理参考等）所带来的新挑战。
2.  **倡导“领域知识+深度学习”的融合范式**：提出了将物理模型、传感器专业知识等作为先验融入深度学习框架的思想（如“模拟器”概念），这对设计更可信、可解释的遥感AI模型具有重要指导意义。
3.  **提供了领域全景图和入门路径**：对于刚进入该领域的研究者，本文清晰地描绘了主要子方向（高光谱、SAR、高分等）的研究脉络，并提供了资源索引，是极佳的“开题地图”。

### 使用建议

- **如果快速了解**：重点阅读**摘要**、**Section I Motivation**（理解挑战和动机）、**Section III Remote Sensing Meets Deep Learning** 的开头部分（了解应用领域分类），以及**Section V Conclusion**（展望）。可以快速把握论文核心思想和领域概况。
- **如果复现**：本文作为综述，不包含可直接复现的单一方法。应将其作为**索引**，根据文中引用的参考文献（如[19], [21], [25]等）去查找具体的研究论文进行复现。
- **如果借鉴创新点**：应重点学习其**提出问题的视角**（Section I）和**融合领域知识的思想**。在设计自己的遥感深度学习模型时，思考如何将数据特性（如光谱维、时间序列）或物理约束融入网络设计。
- **如果写Related Work**：本文可放在**“遥感与深度学习综述”** 这一类别的经典参考文献列表中，用于引出领域背景和挑战。如果论文涉及高光谱分类，可以引用本文III-A节的内容作为背景支撑。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R1_遥感_高光谱_变化检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文是一篇综述性文章，其核心方向是探讨深度学习技术在遥感科学中的应用现状、挑战与未来。它系统性地回顾了深度学习模型（特别是CNN）在遥感多个子领域（如高光谱图像分析、合成孔径雷达图像解译、高分辨率图像处理等）的研究进展。该论文旨在为遥感领域的研究人员提供一个全面的入门指南和资源索引，同时倡导将遥感专业知识与深度学习相结合。根据文件名“2017_遥感高光谱变化检测_Deep_Learning_遥感_综述_深度_学习_感知.pdf”及提供的主题“R1_遥感_高光谱_变化检测”，本文特别适合作为“遥感与深度学习”这一交叉领域的宏观背景和基础综述文献。

## 2. 一句话总结
这篇综述分析了深度学习在遥感领域面临的数据多模态、地理定位、时间序列、大数据及物理模型融合等独特挑战，回顾了其在多个遥感应用子方向的研究进展，并提供了学习资源，倡导将领域专家知识作为先验融入深度学习框架。

## 3. 背景与问题
- **这篇论文为什么要做**：深度学习在计算机视觉等领域取得了巨大成功，正向各个领域渗透。遥感领域也开始拥抱深度学习，但由于遥感数据的独特性，其应用面临新的科学问题，亟需一篇系统性的综述来梳理现状、挑战和方向。
- **之前方法有什么问题**：传统的遥感数据分析依赖手工设计特征和浅层机器学习模型，这些模型在面对日益增长的、复杂的、多模态的遥感大数据时，其特征提取和泛化能力有限。
- **作者想解决的核心矛盾是什么**：核心矛盾在于，深度学习这一“数据驱动”的“黑盒”模型，与遥感科学作为一门“物理驱动”的、需要定量反演和置信度估计的测量科学之间，如何有效结合。作者希望通过综述推动社区思考如何将领域知识（如物理模型）作为先验重新引入深度学习框架，而不仅仅是追求全自动化的数据驱动。

## 4. 核心贡献
基于提供的PDF文本，本文的具体贡献如下：
1.  **系统性地分析了将深度学习应用于遥感数据分析时面临的六大独特挑战**：数据多模态、数据地理定位、数据为测地学测量、时间变量的重要性、大数据挑战、以及需要反演物理/生化参数（而非仅分类检测）。
2.  **全面综述了深度学习在多个遥感应用方向的研究进展**，包括：高光谱图像分析（分类与异常检测）、合成孔径雷达（SAR）图像解译、高分辨率图像解译、多模态数据融合、以及三维重建（在提供的文本中，后几部分仅提及但未展开）。
3.  **提供了深度学习在遥感中应用的“入门工具箱”**，包括开源代码和数据仓库的资源链接（在Section IV，但提供的文本未包含具体内容）。
4.  **明确提出并倡导了一种研究理念**：遥感科学家应发挥自身专业优势，将深度学习视为一种“隐式通用模型”，用以应对气候变化、城市化等大规模挑战，并强调将物理模型等专家知识作为先验重新引入深度学习概念中。

## 5. 方法详解
本文作为综述，并未提出单一的新模型，而是系统梳理并解释了深度学习中关键模型的结构和原理，并讨论了它们在遥感领域的适配与应用。以下根据提供的文本进行总结：

- **整体框架**：论文结构为“挑战分析 -> 基础模型回顾 -> 遥感应用综述 -> 工具与展望”。
- **核心基础模型详解**：
    1.  **自编码器及其变体**：介绍了自编码器（AE）、堆叠自编码器（SAE）、稀疏自编码器和受限玻尔兹曼机（RBM）/深度置信网络（DBN）。这些是早期用于无监督特征学习的深度模型。例如，AE通过编码-解码结构学习数据的压缩表示，其目标是最小化输入与重建输出之间的欧氏距离（第4-5页）。稀疏自编码器通过在损失函数中加入KL散度约束来鼓励隐藏层激活的稀疏性（第5页）。DBN通过堆叠RBM并逐层贪婪训练来构建深层生成模型（第6页）。
    2.  **卷积神经网络**：这是文本中讨论的重点。回顾了计算机视觉中的经典CNN架构：
        - **AlexNet**：使用ReLU激活函数、Dropout层、数据增强，并利用GPU训练，在ImageNet上取得突破（第7页）。
        - **VGG Net**：强调“更深的网络使用更小的卷积核（3x3）”，以增加网络深度并提升特征层次化表达能力（第7-8页）。
        - **ResNet**：通过引入“残差连接”（快捷连接）解决深层网络训练退化问题，使训练极深的网络（如152层）成为可能（第8页）。
        - **FCN**：全卷积网络，用于语义分割。其核心是使用卷积层替代全连接层，从而支持任意尺寸输入；通过编码器-解码器结构和跳跃连接实现端到端的像素级预测（第8-9页）。
- **应用于遥感的方法论**：在具体应用部分（如III-A 高光谱图像分析），综述了如何将上述基础模型适配到遥感任务中。例如：
    - **输入输出**：对于高光谱分类，输入可以是光谱向量（1D）、空间-光谱数据块（2D或3D）。输出是像素级的类别标签。
    - **关键模块与连接**：对于高光谱分类，研究尝试了1D CNN（处理光谱）、2D CNN（处理空间）和3D CNN（同时处理空间和光谱）。3D CNN通过三维卷积操作能更好地联合建模空间-光谱信息（第11-12页，图5）。
    - **与已有方法的差异**：相比传统浅层模型（如SVM），CNN等深度模型能够自动学习层次化、抽象的特征，理论上对数据的非线性建模能力更强，更鲁棒（第10-11页）。

## 6. 实验与结果
- **使用的数据集**：PDF文本中未明确说明本文作为综述所对比分析的具体实验数据集。但提到了一些高光谱数据集在相关研究中的应用，以及Sentinel卫星产生大量数据（如25 PB）作为大数据挑战的例证（第4页）。
- **对比方法**：本文未进行自己的实验，因此没有直接的对比方法。但在综述各类研究时，会提及传统方法（如SVM）作为对比基准。
- **评价指标**：PDF文本中未明确说明。
- **主实验结果**：本文的核心“结果”是统计发现。**图4**显示了自2014年以来，关于“遥感中深度学习”的论文数量呈指数增长（第9页）。此外，在介绍具体模型时，会引用相关研究的结果，例如AlexNet在ImageNet上取得15.4%的top-5错误率（第7页），ResNet在ILSVRC 2015取得3.6%的错误率（第8页）。
- **消融实验**：PDF文本中未明确说明。
- **泛化实验**：PDF文本中未明确说明。
- **速度/参数量/FLOPs**：未提供具体数字，但指出深度学习需要大量计算资源和大数据，GPU训练是关键（第7页）。

## 7. 这篇论文真正有价值的地方
这篇综述的最大价值在于其 **“格局”和“指引性”**。它超越了单纯的技术回顾，深刻剖析了遥感学科与深度学习方法论之间的契合点与矛盾点。对后续研究的启发在于：
1.  **问题导向而非技术堆砌**：它提醒研究者，应用深度学习于遥感时，不能盲目套用计算机视觉模型，必须首先思考遥感数据的独特性（多模态、时序、地理参考等）所带来的新挑战。
2.  **倡导“领域知识+深度学习”的融合范式**：提出了将物理模型、传感器专业知识等作为先验融入深度学习框架的思想（如“模拟器”概念），这对设计更可信、可解释的遥感AI模型具有重要指导意义。
3.  **提供了领域全景图和入门路径**：对于刚进入该领域的研究者，本文清晰地描绘了主要子方向（高光谱、SAR、高分等）的研究脉络，并提供了资源索引，是极佳的“开题地图”。

## 8. 局限与问题
- **方法深度有限**：作为一篇综述，本文对各项研究的介绍是概括性的，无法深入探讨某一具体方法的细节和局限性。
- **覆盖范围与前沿性**：提供的文本仅覆盖了论文的前12页，关于SAR、高分辨率图像、数据融合和3D重建等重要部分的详细内容未能看到。此外，本文发表于2017年，深度学习领域发展极快，文中综述的一些模型和观点可能已不是最新前沿。
- **缺乏定量对比**：本文没有提供一个统一的基准来定量对比不同深度学习方法在遥感任务上的性能，这使得读者难以判断各方法的相对优劣。
- **“倡导”的实践性**：将物理模型与深度学习深度融合是一个极具挑战性的方向，本文更多是提出理念，具体的、普适的技术路径仍需探索。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：重点阅读**摘要**、**Section I Motivation**（理解挑战和动机）、**Section III Remote Sensing Meets Deep Learning** 的开头部分（了解应用领域分类），以及**Section V Conclusion**（展望）。可以快速把握论文核心思想和领域概况。
- **如果复现**：本文作为综述，不包含可直接复现的单一方法。应将其作为**索引**，根据文中引用的参考文献（如[19], [21], [25]等）去查找具体的研究论文进行复现。
- **如果借鉴创新点**：应重点学习其**提出问题的视角**（Section I）和**融合领域知识的思想**。在设计自己的遥感深度学习模型时，思考如何将数据特性（如光谱维、时间序列）或物理约束融入网络设计。
- **如果写Related Work**：本文可放在**“遥感与深度学习综述”** 这一类别的经典参考文献列表中，用于引出领域背景和挑战。如果论文涉及高光谱分类，可以引用本文III-A节的内容作为背景支撑。

## 10. 和其他论文的关系
根据提供的文件名和主题“R1_遥感_高光谱_变化检测”，本文作为2017年的权威综述，很可能被该主题下的后续研究论文引用为背景文献。例如，一篇具体研究高光谱变化检测的论文，可能会在Related Work中引用本文来说明“深度学习在高光谱分析中的兴起”（III-A节）。但由于未看到其他具体论文信息，无法建立确切的双链关系。

## 11. 关键词
深度学习， 遥感， 机器学习， 大数据， 地球观测， 卷积神经网络， 高光谱图像分析， 综述， 多模态数据， 物理模型， 时间序列分析， 挑战与展望

## 12. 可信度说明
本笔记主要基于提供的PDF文本前12页内容生成，该部分包含了论文的**标题、作者、摘要、索引词、第一章“动机”、第二章“从感知机到深度学习”的大部分内容（模型基础）、以及第三章“遥感遇见深度学习”的A部分“高光谱图像分析”**。笔记中所有对模型原理、挑战和贡献的总结均直接来源于这些文本。需要注意的是，由于只提供了部分内容，关于论文后半部分（如SAR、高分辨率图像解译、数据融合、工具资源、结论）的详细综述内容无法覆盖。提取的文本整体连贯，关键图表（如网络结构图）描述清晰，但部分公式和引用标记可能因提取工具而略显零乱。因此，本笔记对**论文前半部分**的概括是可靠且基于原文的。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2017_Deep_learning_in_rem.txt` (60/60 页; 原 AI 主体 12/60 + 全文补读 13-60); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
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
