---
title: Building-Road Collaborative Extraction from Remote Sensing Images via Cross-Task and Cross-Scale Interaction
authors:
  - "Haonan Guo"
  - "Xin Su"
  - "Chen Wu"
  - "Bo Du"
  - "Liangpei Zhang"
year: 2023
venue: IEEE Transactions on Geoscience and Remote Sensing (TGRS)
doi: 10.1109/TGRS.2024.3383057
pdf: [[2023_Building-road_Collab.pdf]]
primary_topic: T_遥感_建筑检测
topics:
  - "T_遥感_建筑检测"
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
extract_cache: .paper-cache/extracts/2023_Building-road_Collab.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# Building-Road Collaborative Extraction from Remote Sensing Images via Cross-Task and Cross-Scale Interaction

## 基本信息
- **PDF**: [[2023_Building-road_Collab.pdf]]
- **primary_topic**: `T_遥感_建筑检测`
- **topics**: `T_遥感_建筑检测`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Building-Road Collaborative Extraction from Remote Sensing Images via Cross-Task and Cross-Scale Interaction |
| **作者** | Haonan Guo; Xin Su (通讯); Chen Wu; Bo Du; Liangpei Zhang（武汉大学） |
| **发表时间** | 2023（IEEE 接收版；DOI 标注 2024，© 2024 IEEE） |
| **刊物/会议** | IEEE Transactions on Geoscience and Remote Sensing (TGRS) |
| **DOI** | 10.1109/TGRS.2024.3383057 |

## 摘要

**清理后的英文原摘要**（据 PDF 提取文本修复空格/连字符、剔除杂入字符后）：

> Buildings and roads are the two most basic man-made environments that carry and interconnect human society. Building and road information has important application value in the frontier fields of regional coordinated development, disaster prevention, auto-driving, etc. Mapping buildings and roads from very high-resolution (VHR) remote sensing images has become a hot research topic. However, the existing methods often extract buildings and roads with separate models, ignoring their strong spatial correlation. To fully utilize their complementary relation, we propose a method that simultaneously extracts buildings and roads from remote sensing images. The accuracy of both tasks can be improved using our proposed multi-task feature interaction and cross-scale feature interaction modules. To be specific, a multi-task interaction module is proposed to interact information across building extraction and road extraction tasks while preserving the unique information of each task. Furthermore, a cross-scale interaction module is designed to automatically learn the optimal reception field for buildings and roads under varied appearances and structures. Compared with existing methods that train individual models for each task separately, the proposed collaborative extraction method can utilize the complementary advantages between buildings and roads and reduce the inference time by half using a single model. Experiments on a wide range of urban and rural scenarios show that the proposed algorithm can achieve building-road extraction with outstanding performance and efficiency.

**中文翻译**：

> 建筑物与道路是承载并连接人类社会的两类最基本的人造环境。建筑物与道路信息在区域协调发展、灾害防控、自动驾驶等前沿领域具有重要应用价值，从甚高分辨率（VHR）遥感影像中绘制建筑物与道路已成为研究热点。然而，现有方法往往用相互独立的模型分别提取建筑物和道路，忽略了二者之间强烈的空间相关性。为充分利用其互补关系，本文提出一种从遥感影像中同时提取建筑物与道路的方法。借助所提出的多任务特征交互模块与跨尺度特征交互模块，两项任务的精度均可得到提升。具体而言，本文提出多任务交互模块，在建筑提取与道路提取任务之间交互信息，同时保留各任务的独有信息；进一步设计跨尺度交互模块，针对外观与结构各异的建筑物与道路自动学习最优感受野（reception field）。相比为每个任务分别训练独立模型的已有方法，本文的协同提取方法能够利用建筑物与道路之间的互补优势，并以单一模型将推理时间减半。在涵盖大量城市与乡村场景的数据上的实验表明，所提算法能够以出色的性能与效率实现建筑-道路提取。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：建筑物和道路是承载人类社会的两类最基本人造元素——建筑物是社会生产与人类生活的基本载体，道路则连接起承载货物与信息流通的社会网络。二者的地理数据对理解人类活动、支撑可持续发展目标（SDG，如区域协调发展、可持续城市规划、公共卫生、灾害风险削减）以及智慧城市等前沿应用不可或缺。VHR 遥感影像为大范围绘制建筑物和道路提供了丰富的数据源；传统人工目视判读/测绘虽精度高但费时，难以满足自动驾驶等应用对最新数据库的需求，故催生了自动提取方法的研究。
- **之前方法的问题**：
    1.  **孤立提取**：主流方法大多孤立地提取建筑物或道路（[23][24]），忽略二者间强烈的空间相关性。论文用 U-Net 分别在建筑、道路任务上训练，可视化特征后（Fig.1）发现一个经验现象：仅用建筑标签训练的模型，其部分特征已学会定位道路区域；反之道路分割模型也在无建筑监督的情况下自动学到了建筑信息——这说明两任务可协同互助。
    2.  **统一结构但分别训练**：一些方法虽设计了统一网络结构（Fig.2a），但仍在两个任务上分别训练，无法利用互补关系，且需图像两次过模型、计算量翻倍。
    3.  **简单多分类器多任务的缺陷**：直观方案是为两任务各加一个分类器、改成多任务（Fig.2b，[26][27][28]），但这类简单设计引发 **"跷跷板现象"（seesaw phenomenon，[29]）**——一个任务的精度往往以损害另一个任务为代价（论文实验中也得到验证）。
    4.  **感受野统一**：上述方法对建筑、道路任务采用统一的模型感受野（reception field），忽略了不同任务对感受野的不同需求，进一步劣化多任务特征表示。
- **核心矛盾**：如何用单一模型实现建筑与道路的**协同提取**、利用其**特征互补性**，同时**避免任务间性能冲突（跷跷板现象）**，并**自适应地为不同任务/特征空间选择最优感受野**。

## 关键贡献

1.  **单模型协同提取网络**：提出一个在单一模型中同时提升建筑与道路两项任务精度的提取网络（CRIN）。其中的**多任务交互模块**利用建筑-道路空间相关的互补性，在共享特征空间内实现跨任务交互，同时通过内任务（inner-task）交互设计保留各任务独有特征，缓解已有方法孤立学习或不平衡学习的问题。
2.  **跨尺度交互（感知）模块**：由于建筑、道路的任务特定特征对感受野的依赖不同，设计了跨尺度交互模块，通过反向传播自适应地为**任务特定特征空间**和**任务共享特征空间**确定最优感受野，从而改善二者的特征表示。
3.  **广泛实验验证**：在涵盖城市与乡村的大量场景上的实验证明方法有效，在建筑与道路提取任务上均达到最高精度；相比分别训练的结构、以及会引发"跷跷板现象"的多任务结构，CRIN 能利用建筑-道路互补优势，取得最佳的性能与效率（单次推理、推理时间减半）。

## 方法

- **整体框架（CRIN）**：CRoss-INteraction（CRIN）网络（Fig.3），编码器-解码器结构，权重共享编码器。输入 VHR 遥感影像，**同时**输出建筑掩膜图与道路掩膜图，通过任务间信息共享提升学习效率。输入先经编码器做层级特征提取；提取的特征被复制并传给解码器以恢复分辨率、生成预测。最终用建筑与道路真值（ground truths）联合监督优化。
- **多任务交互模块（MTI / MFI）**：位于解码器每一阶段（Fig.4），是缓解"跷跷板现象"的核心。注：原文同时使用 "MTI"（multi-task interaction module）与 "MFI" 两个缩写指代该模块，PDF 文本未对二者作区分。
    - **输入**：上一解码阶段的深层特征（语义上下文丰富，但因空间分辨率低、边缘细节不足）与编码器传来的浅层特征（含全图丰富边缘细节，但非仅限目标）。
    - **内任务融合阶段（inner-task / fusion stage）**：常规解码器做法是把多个特征拼接后用单一卷积融合，但在多任务下直接拼接卷积成统一表示会引发跷跷板现象。本文改为分别融合建筑特征与道路特征：把输入特征**分成两组**、**交替拼接（concatenate in alternation）**，再用**组卷积（group size = 2）**生成各含丰富语义与空间细节的建筑特征、道路特征，引导模型为不同任务关注输入特征的不同细节。Fig.4 的真实样例显示，各任务的融合结果相比输入特征能更好地定位建筑/道路区域。
    - **跨任务交互阶段（cross-task / interaction stage）**：将融合特征进一步投影到三个空间——**建筑特定特征空间**、**道路特定特征空间**（任务特定空间，学习各自任务的最优表示）与**任务共享特征空间**（使两任务特征相互交互、利用互补性）。（PDF 提取文本在交互阶段细节处截断于该句，更细粒度的投影/交互公式未在缓存文本中给出。）
- **跨尺度交互模块（CSI）**：集成在 MFI 之后，为每个任务/特征空间选择最优特征尺度。因不同目标对感受野依赖不同，CSI 通过反向传播自动学习并选择任务特定空间与任务共享空间各自的最优感受野，从而为每个具体任务挖掘最优特征表示。
- **训练与推理**：端到端，用建筑+道路真值联合监督；推理时单次前向即同时得到两类预测，相比分别跑两个独立模型推理时间减半。
- **与已有方法的差异**：相比 Fig.2(a) 分别训练的统一结构（计算量翻倍、不利用相关性）与 Fig.2(b) 简单多分类器多任务（易引发跷跷板现象），CRIN（Fig.2c）显式分离任务特定/共享特征空间并配合 CSI 自适应感受野，兼顾任务独有性与互补共享。

## 实验

> 说明：本仓库的 PDF 提取缓存仅覆盖前 12 页（约前 25000 字符），止于"方法"的跨任务交互阶段；实验章节正文未进入缓存。以下数据集等信息来自笔记末"全文补读记录"对 p.13-17 的零散摘录，定量结果仍不可考。

- **数据集**：补读线索显示至少使用了 **Massachusetts 数据集** 与 **AIOI 数据集** 两套数据（p.13 提到 "Massachusetts dataset is approximately 3 times lower than the AIOI dataset" 的空间分辨率比较，并据此推断各任务最优感受野）。论文摘要/引言强调覆盖"大量城市与乡村场景"。其余数据集划分、影像分辨率/数量等细节**PDF 提取文本未明确**。
- **对比方法**：对比对象在结构层面明确——分别训练的 separate models（Fig.2a）与会引发跷跷板现象的多任务模型（Fig.2b）。相关工作中点名的相关方法包括 U-Net、D-LinkNet、Res-U-Net（Ayala 等）、非局部特征搜索网络（Ding 等）等，但**具体对比算法名单与配置 PDF 提取文本未明确**。
- **评价指标**：缓存文本反复使用 "accuracy / highest accuracy / better accuracy"，但**未给出具体指标定义（IoU/F1/OA 等）**——PDF 提取文本未明确。
- **主实验结果**：论文声称在建筑与道路提取上均"达到最高精度"、性能与效率最佳；**具体定量数值 PDF 提取文本未明确**。
- **消融实验**：p.13 补读片段提及"through the proposed cross-task and ..."、"recognition accuracy"等，暗示存在对跨任务/跨尺度模块的分析；**具体消融数字 PDF 提取文本未明确**。
- **效率**：明确——单模型、单次推理，相比分别运行两个独立模型**推理时间减半**。参数量、FLOPs **PDF 提取文本未明确**。
- **局限与展望（来自 p.13 补读片段）**：作者自陈方法仍有改进空间，方向包括：真值标签常与影像不严格对齐（"ground truth labels are usually not strictly aligned"），可探索**噪声标签学习（noisy label learning）**以实现更鲁棒的建筑提取；以及生成细粒度、最新的建筑与道路地图、面向大规模制图（"great potential in large-scale mapping"）。

## 局限

1.  **缓存文本不完整导致的可评估性局限**：本仓库的 PDF 提取缓存仅前 12 页，实验章节正文缺失，无法核验数据集划分、对比基线、定量指标与消融数字，对方法实证强度的判断只能依赖补读片段。
2.  **核心假设依赖互补性**：方法收益建立在"建筑与道路在特征空间存在强互补性"之上（Fig.1 经验观察）。在道路被密集建筑完全遮挡、或路面材质与建筑材质高度相近的极端场景，互补性可能减弱，优势或不明显。
3.  **标签对齐问题（作者自陈）**：补读片段显示真值标注与影像常不严格对齐，作者将其列为待改进点并建议引入噪声标签学习——说明当前结果一定程度受标注噪声影响。
4.  **效率细节缺失**：虽明确"推理时间减半"，但缓存文本未给出参数量/FLOPs，难以量化其作为多任务模型的轻量化程度。

## 个人评论

1.  **"协同 > 孤立"的可迁移范式**：本文最有价值的并非某个具体卷积，而是把"两类强空间相关地物"从孤立提取改为协同学习的思路。Fig.1 那个"只用建筑标签训练的模型自发学到道路"的经验观察很有说服力，足以启发其他成对地物（建筑-阴影、水体-岸线、车辆-道路、地块-边界）的协同设计。
2.  **对"跷跷板现象"的工程化拆解**：把统一特征空间显式拆为任务特定 + 任务共享空间，再用"分组交替拼接 + 组卷积（group=2）"做内任务融合，是一种简单、可解释、易复用的多任务特征处理范式，比单纯堆多个分类器更有针对性。
3.  **自适应感受野值得单独关注**：CSI 用反向传播自动为不同特征空间选感受野，呼应了"道路是条带状、需大感受野/长程依赖，建筑更局部"的领域常识，把这一先验交给模型学习而非手工设定，是多任务遥感分割里一个干净的设计点。
4.  **需谨慎之处**：论文中 "MTI" 与 "MFI" 缩写混用、跨任务交互的精确算子在缓存文本中未完整呈现；真正复现需回到原文 Fig.3/Fig.4 与公式，并补齐实验设置。本笔记对实验定量部分保持"未明确"的克制结论。

### 使用建议

- **如果快速了解**：读 Abstract 与 Introduction 后半段（问题提出 + 三点贡献），配合 Fig.1（互补性经验观察）、Fig.2（三种架构对比）、Fig.3（CRIN 总框架）。
- **如果复现**：精读 III. METHODOLOGY，重点是 Fig.3（整体流程）与 Fig.4（MFI/MTI 内任务融合的分组交替拼接 + 组卷积、跨任务三空间投影），以及 CSI 的反向传播选感受野机制；实验设置（数据集划分、指标、基线）需回原文 p.13 之后补齐。
- **如果借鉴创新点**：学习"任务特定/共享特征空间显式分离"与"自适应尺度选择"，并思考迁移到其他成对/双任务（如语义分割中的"物体 vs 边界"、变化检测中的"建筑 vs 背景上下文"）。
- **如果写 related work**：归入"遥感建筑/道路提取"的"多任务/协同提取"子类，作为利用地物空间相关性提升提取精度的代表工作引用，并可对比其与单任务 U-Net/D-LinkNet 系方法的差异。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_遥感_建筑检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**遥感影像理解 / 语义分割**领域，研究**从甚高分辨率（VHR）遥感影像中同时（协同）提取建筑物与道路**。它针对的痛点是：现有方法把建筑、道路当作两个孤立任务用独立模型提取，忽略二者强空间相关性，既无法利用互补性提升精度，又因图像两次过模型而效率低下；简单的多分类器多任务又会引发"跷跷板现象"。按其技术本质（多任务遥感语义分割 + 特征交互）与对象（建筑、道路），应归入 **T_遥感_建筑检测**（遥感建筑/地物提取）主题，而非"目标检测（违建/车辆/船舶/行人）"——本文做的是像素级建筑与道路提取，不是边界框检测，原 `C2` 分类不准确。

## 2. 一句话总结
本文提出 CRIN（CRoss-INteraction）网络，在编码器-解码器结构上用**多任务交互模块（MTI/MFI）**显式分离任务特定与任务共享特征空间、并用**跨尺度交互模块（CSI）**自适应选择感受野，在单一模型中同时提取建筑物与道路，借助二者特征互补缓解"跷跷板现象"，在提升两任务精度的同时把推理时间减半。

## 3. 背景与问题
- **为什么要做**：建筑与道路是社会最基本的两类人造元素，其地理数据支撑 SDG、智慧城市、自动驾驶等；VHR 遥感提供大范围数据源，人工判读费时、难更新，需自动提取。
- **之前方法的问题**：
    1.  **孤立提取**：主流方法孤立提取建筑或道路，忽略强空间相关性；Fig.1 经验显示，仅用单类标签训练的 U-Net 已自发学到另一类地物，证明两任务可协同。
    2.  **统一结构但分别训练**（Fig.2a）：计算量翻倍，且不利用相关性。
    3.  **简单多分类器多任务**（Fig.2b）：引发"跷跷板现象"，一个任务以损害另一个为代价提升。
    4.  **感受野统一**：忽略建筑/道路对感受野的不同需求，劣化多任务表示。
- **核心矛盾**：单模型协同提取 + 利用互补性 + 避免跷跷板 + 自适应感受野，四者如何兼得。

## 4. 核心贡献
1.  **单模型协同提取网络（CRIN）**：在共享特征空间内做跨任务交互、以内任务交互保留各任务独有特征，缓解孤立/不平衡学习；单次推理、推理时间减半。
2.  **跨尺度交互（感知）模块（CSI）**：通过反向传播自适应为任务特定空间、任务共享空间确定最优感受野，改善二者特征表示。
3.  **广泛实验**：在大量城市与乡村场景上，建筑与道路提取均达最高精度，性能与效率优于分别训练结构与会引发跷跷板的多任务结构。

## 5. 方法详解
- **整体框架**：CRIN，权重共享编码器 + 解码器（Fig.3）。输入 VHR 影像，同时输出建筑、道路掩膜；编码器层级提特征→复制传给解码器恢复分辨率→每个解码阶段插入 MFI/MTI→其后接 CSI；最终用建筑+道路真值联合端到端监督。
- **MTI / MFI（多任务交互模块，Fig.4）**：原文 "MTI" 与 "MFI" 混用指同一模块。
    - 输入：上一解码阶段深层特征（语义强、边缘弱）+ 编码器浅层特征（边缘细节丰富）。
    - **内任务融合阶段**：不同于常规"拼接 + 单卷积"（会引发跷跷板），改为把输入特征**分两组、交替拼接**，再用**组卷积（group size = 2）**分别生成建筑特征与道路特征，引导各任务关注输入的不同细节；Fig.4 样例显示融合结果比输入更准地定位建筑/道路。
    - **跨任务交互阶段**：把融合特征投影到**建筑特定空间、道路特定空间、任务共享空间**三者；任务特定空间学各自最优表示，任务共享空间让两任务特征交互、利用互补。（缓存文本恰在此阶段细节处截断，更细的投影/交互算子未进入缓存。）
- **CSI（跨尺度交互模块）**：接在 MFI 后，因不同目标对感受野依赖不同，CSI 用反向传播自动为任务特定/共享空间各选最优感受野与特征尺度。
- **数学公式**：PDF 提取文本（前 12 页）未给出完整公式，机制层面可理解为"分治（分离特征空间）+ 交互（共享空间）+ 自适应多尺度选择（CSI）"。
- **推理**：单次前向同时出两类预测，较两独立模型推理时间减半。

## 6. 实验与结果
- **数据集**：补读线索（p.13）显示使用 **Massachusetts** 与 **AIOI** 两套数据，Massachusetts 空间分辨率约为 AIOI 的 1/3（论文据此讨论不同数据集的最优感受野差异）。覆盖城市与乡村场景。具体划分/数量 **PDF 提取文本未明确**。
- **对比方法**：结构层面对比 separate models（Fig.2a）与多任务模型（Fig.2b）；相关工作点名 U-Net、D-LinkNet、Res-U-Net、非局部特征搜索网络等，但**具体对比算法清单 PDF 提取文本未明确**。
- **评价指标**：缓存文本只出现 "accuracy"，**具体指标（IoU/F1/OA）未明确**。
- **主实验结果**：声称建筑、道路均"最高精度"，**定量数值未明确**。
- **消融实验**：p.13 片段暗示有跨任务/跨尺度模块分析，**具体数字未明确**。
- **效率**：单模型单次推理，**推理时间减半**；参数量/FLOPs 未明确。

## 7. 这篇论文真正有价值的地方
1.  **"协同优于孤立"的可迁移范式**：把两类强空间相关地物从分别提取改为协同学习，Fig.1 的经验观察（单类标签模型自发学到另一类）提供了有力动机，可迁移到建筑-阴影、水体-岸线、车辆-道路等成对地物。
2.  **对跷跷板现象的工程化解法**：显式分离任务特定/共享空间 + "分组交替拼接 + 组卷积"内任务融合，简单可解释、易复用。
3.  **自适应感受野（CSI）**：把"道路需大感受野、建筑更局部"的先验交给反向传播学习，而非手工统一设定，是多任务遥感分割的干净设计点。
4.  **效率收益实在**：单模型把两任务推理时间减半，对大规模制图有现实意义。

## 8. 局限与问题
1.  **缓存文本不完整**：本仓库提取缓存仅前 12 页，实验正文缺失，数据集划分/指标/消融/对比基线无法核验，实证强度判断受限。
2.  **互补性假设**：在道路被密集建筑遮挡、或路面与建筑材质相近的极端场景，互补性可能减弱。
3.  **标签对齐（作者自陈）**：真值与影像常不严格对齐，作者建议引入噪声标签学习以增强鲁棒性，说明结果受标注噪声影响。
4.  **效率细节缺失**：报告了推理时间减半，但参数量/FLOPs 未给出。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Introduction 后半段 + Fig.1/2/3。
- **复现**：精读 III. METHODOLOGY，Fig.3（总流程）+ Fig.4（MFI 内任务融合的分组交替拼接、组卷积、三空间投影）+ CSI 反向传播选感受野；实验设置需回原文 p.13 之后补齐。
- **借鉴创新点**：学习任务特定/共享空间分离 + 自适应尺度选择，迁移到其他双任务（物体 vs 边界、地物 vs 上下文）。
- **写 related work**：归入"遥感建筑/道路提取"的"多任务/协同提取"子类，作为利用地物空间相关性提升精度的代表工作引用。

## 10. 和其他论文的关系
本文应归于 **T_遥感_建筑检测** 主题（遥感建筑/地物提取），与库内其他建筑提取/检测工作相关：
- 同主题的遥感建筑检测/提取工作（如 [[2017_Building_Detection_f]]、[[TfNet_Building_Detection_in_Remote_Sensing_Images_Using_Multi-Scale_Feature_Fusion]] 等多尺度特征融合建筑提取方法），可对比单任务 vs 协同多任务的差异。
- 道路提取方向（D-LinkNet 等扩张卷积/长程依赖方法）与本文 CSI 自适应感受野思想相关。
- 多任务学习中针对"跷跷板现象"的通用方法，可与本文的特征空间分离方案互为参照。

## 11. 关键词
建筑物提取, 道路分割, 多任务学习, 协同提取, 跨任务交互, 跨尺度交互, 自适应感受野, 跷跷板现象, 高分辨率遥感, 编码器-解码器, 语义分割

## 12. 可信度说明
本精读基于 PDF 提取缓存的**前 12 页**（约前 25000 字符），完整覆盖**标题、摘要、引言、相关工作（建筑/道路/建筑-道路提取）、方法概述、MFI/MTI 内任务融合与跨任务交互的开头**；缓存恰在跨任务交互阶段细节处截断。**实验章节正文（数据集划分、指标定义、定量结果、消融、对比基线）未进入缓存**，相关结论多为定性或基于论文声明，定量数据缺失。实验/局限部分的数据集名称（Massachusetts、AIOI）、标签对齐与噪声标签展望等来自笔记末"全文补读记录"对 p.13-17 的零散摘录，属片段级线索而非完整正文。已修正原笔记两处问题：题目/作者/刊物的乱码与缺失（补全 Xin Su、Bo Du、Liangpei Zhang，刊物为 IEEE TGRS）；主题分类由 `C2_目标检测_违建_车辆_船舶_行人` 修正为 `T_遥感_建筑检测`（本文为像素级建筑/道路提取，非边界框目标检测）。

---

> **可信度补充**: PDF 提取质量 = **high** (前 12 页提取质量好, 约 2086 字符/页); 来源缓存: `.paper-cache/extracts/2023_Building-road_Collab.txt` (缓存覆盖 12/17 页, 截断于方法的跨任务交互阶段; 笔记末"全文补读记录"另含 p.13-17 零散摘录); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro); 本轮 2026-06-18 据提取文本重读优化(摘要重建、作者/刊物补全、方法核对、分类修正)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Massachusetts dataset is approximately 3 ti mes lower than the
- p.13: AIOI dataset, we suppose that the optimal reception field of
- p.13: Although our proposed method achieves better accuracy than
- p.13: The ground truth labels are usua lly not strictly aligned with the
- p.13: Explor ing noisy label learning to achieve more robust building -
- p.13: Moreover, generating fine-grained and up -to-date building and
- p.13: Buildings are the basic carrier of social production and
- p.13: The geodata of buildings and roads are valuable for various
- p.13: Furthermore, a cross -scale interaction module is proposed to
- p.13: REFERENCES
- p.13: Aligned Representations With Multimodel Transformers
- p.13: Networks (CNNs) for fused airborne lidar and image data

### 缺失页关键摘录

- p.13: dataset. Considering that the spatial resolution of the
- p.13: Massachusetts dataset is approximately 3 ti mes lower than the
- p.13: AIOI dataset, we suppose that the optimal reception field of
- p.13: Although our proposed method achieves better accuracy than
- p.13: limitation s and can be further improved from the following
- p.13: the “seesaw phenomenon” where the accuracy of one task is
- p.13: recognition accuracy through the proposed cross -task and
- p.13: accuracy, showing great pot ential in large -scale mapping.
- p.16: dataset for building and road detection, and building
<!-- AI_READING_NOTE_END -->
