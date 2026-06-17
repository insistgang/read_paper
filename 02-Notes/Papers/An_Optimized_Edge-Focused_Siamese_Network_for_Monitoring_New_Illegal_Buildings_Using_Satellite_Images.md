---
title: An_Optimized_Edge-Focused_Siamese_Network_for_Monitoring_New_Illegal_Buildings_Using_Satellite_Images
authors:
  - "Haode Du"
  - "Zhou Huang"
  - "Yi Zhang"
year: 2024
venue: "IEEE Transactions on Geoscience and Remote Sensing (TGRS)"
doi: 10.1109/TGRS.2024.3379567
pdf: [[An_Optimized_Edge-Focused_Siamese_Network_for_Monitoring_New_Illegal_Buildings_Using_Satellite_Images.pdf]]
primary_topic: T_遥感_建筑检测
topics:
  - "T_遥感_建筑检测"
status: ai-read
reading_stage: ai-fulltext
confidence: high
source_basis: pdf-text
date_added: 2026-06-05
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/An_Optimized_Edge-Focused_Siamese_Network_for_Monitoring_New_Illegal_Buildings_Using_Satellite_Images.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# An_Optimized_Edge-Focused_Siamese_Network_for_Monitoring_New_Illegal_Buildings_Using_Satellite_Images

## 基本信息
- **PDF**: [[An_Optimized_Edge-Focused_Siamese_Network_for_Monitoring_New_Illegal_Buildings_Using_Satellite_Images.pdf]]
- **primary_topic**: `T_遥感_建筑检测`
- **topics**: `T_遥感_建筑检测`
- **状态**: ai-read (已 AI 全文提取阅读, 待人工复核)
- **date_added**: 2026-06-05

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | An Optimized Edge-Focused Siamese Network for Monitoring New Illegal Buildings Using Satellite Images |
| **作者** | Haode Du; Zhou Huang; Yi Zhang（北京大学地球与空间科学学院遥感与地理信息系统研究所） |
| **发表时间** | 2024（在线发表 2024-03-20） |
| **刊物/会议** | IEEE Transactions on Geoscience and Remote Sensing (TGRS), Vol. 62, 2024, Art. 4703115 |
| **DOI** | 10.1109/TGRS.2024.3379567 |

## 摘要

**英文原摘要（据 PDF 提取文本整理，已修复空格/连字符断裂、剔除杂入的版式字符）**：

> Illegal construction is a common problem often encountered by cities with rapid development, which is hard to deal with for multiple reasons. Although these illegal buildings are primarily defined by laws and regulations, they still have physical characteristics in common that makes them identifiable. In this study, we propose an illegal building monitoring method based on satellite images and deep learning techniques, named illegal building monitoring network (IBMNet), to improve the data collection capacity for monitoring new illegal buildings. IBMNet is an end-to-end pixelwise segmentation network with two flows: the Segment Flow, which includes a Siamese encoder and an attention fusion module (AFM), and the Edge Flow, which uses Gated Convolutional Layers to extract edge information. We implement and evaluate our model in China, a country with fast development and struggling with illegal buildings. In addition to the conventional metrics, we propose a set of specialized metrics to evaluate the model's ability to discriminate illegal buildings and legal buildings (OA_B, F1_B, and IoU_B). The model achieves great results on the illegal building monitoring dataset (IBMD) with an F1 score of 0.7990 and IoU_B of 0.7449, showing its great ability in detecting illegal buildings in various scenarios and distinguishing them from legal buildings. Compared to the existing methods based on urban database, IBMNet has a higher time resolution and a larger space coverage, making it more accessible in data and cost-effective for governments. The proposed method is also promising in other cities and countries with similar problems.
>
> Index Terms — Change detection, edge focus, illegal building monitoring, Siamese network.

**中文翻译**：

> 违章建筑是快速发展城市常遇到的普遍问题，因多重原因难以治理。尽管违章建筑主要由法律法规界定，但它们仍具有可识别的共同物理特征。本研究提出一种基于卫星影像与深度学习的违章建筑监测方法——违章建筑监测网络（IBMNet），以提升新建违章建筑监测的数据采集能力。IBMNet 是一个端到端的逐像素分割网络，含两条流：分割流（Segment Flow，含 Siamese 编码器与注意力融合模块 AFM）和边缘流（Edge Flow，用门控卷积层提取边缘信息）。我们在中国——一个快速发展且深受违章建筑困扰的国家——实现并评估了模型。除常规指标外，本文提出一组专门指标来评估模型在不掌握合法建筑信息时区分违章建筑与合法建筑的能力（OA_B、F1_B、IoU_B）。模型在违章建筑监测数据集（IBMD）上取得优异结果，F1 达 0.7990、IoU_B 达 0.7449，表明其在多种场景下检测违章建筑并将其与合法建筑区分的强大能力。与现有基于城市数据库的方法相比，IBMNet 具有更高的时间分辨率与更大的空间覆盖范围，数据获取更便捷、对政府更具成本效益。该方法在有相似问题的其他城市和国家也颇具前景。
>
> 关键词：变化检测、边缘聚焦、违章建筑监测、Siamese 网络。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

*   **为什么要做**：快速城市化进程中，违章建筑（illegal construction）是普遍且难以治理的问题。提取文本明确列举了监管的多重困难：(1) 违章建筑分布零散、跨城区/郊区/农村，且建造极快——可"一夜建成"、每天加盖 2–3 层；(2) 相关立法不统一、不完善，存在大量"灰色地带"；(3) 政府缺乏可靠的技术-行政手段在大尺度上获取准确数据，且中央政策与地方实践、政治团体间的不一致进一步阻碍信息获取与执法；(4) 拆除长期存在的违建以及对住户的补偿/安置成本高昂。
*   **遥感+深度学习的机会**：作者指出，超高分辨率（VHR）卫星影像 + 深度学习已被广泛用于城市问题求解。违章建筑虽由法规界定，但常共享相同物理特征（形状、纹理、颜色），尤其表现为**较低的高度与均质的屋顶颜色**，使神经网络有可能从复杂背景中提取其深层语义特征。变化检测（change detection）能用高时间分辨率影像及时识别**新建**违建，并将其与厂房/农场里早已存在的相似建筑（如仓库、温室）区分开，从而缩小排查范围。
*   **之前方法的问题**：已有用 VHR 影像检测违建的工作**仍需城市数据库支撑**（[18][19]）。这些方法受数据库质量与更新频率限制——数据库依赖政府部门间沟通、受上述层级不一致影响；面对违建的快速建造，基于数据库的变化检测在时间分辨率上不足；数据库还限制了空间覆盖（统计不完善的郊区难以覆盖）。
*   **核心矛盾**：违章建筑**快速出现** vs. 现有监测手段**低时间分辨率、受限于数据库更新与覆盖**。作者据此提出：以卫星影像为**唯一数据源**，将违建监测与城市数据库解耦，实现更灵活、更频繁、可覆盖郊区的主动监测。

## 关键贡献

论文 Introduction 末尾明确列出 4 条贡献：

1.  **提出双流变化检测网络 IBMNet**：基于 Siamese 网络与门控卷积层（GCL）为违建监测设计。Edge Flow 用于细化分割边界、从复杂背景中提取小型违建；并引入 AFM 融合双时相特征。论文自称是**首个将前沿边缘聚焦（edge-focusing）方法应用于违建监测**的工作，在提升精度的同时降低数据需求。
2.  **仅依赖卫星影像、规避城市数据库局限**：与按行政层级分级构建的城市数据库不同，本方法直接从卫星影像生成统一结果；借助遥感影像的高时间分辨率，显著提升检测频率，使政府能在违建早期主动监管、抑制，降低监管成本；并能覆盖数据库常忽略的郊区。
3.  **提出领域专用评估指标**：为评估模型在**不显式学习合法建筑特征**的前提下区分违建与合建的能力，引入一组专门指标（OA_B、F1_B、IoU_B），通过衡量模型对违建/合建的二值分割能力来评估其判别力。
4.  **初步验证可行性**：初步验证了"仅依靠遥感影像监测违建"的可行性，向高效、大范围的违建监管与数据采集迈出渐进一步。

## 方法

*   **整体框架（据 Section III-A）**：IBMNet 是一个 Siamese 神经网络，输入两张 RGB 影像、输出二值变化图。由三部分构成：**Segment Flow、Edge Flow、Fusion Block**。
*   **输入输出**：输入双时相 RGB 卫星影像对；输出与输入同尺寸的二值图，标识新出现的违章建筑。
*   **关键模块与连接**：
    1.  **Segment Flow（分割流）**：
        *   **Siamese 编码器**：两个**权重共享**、改自 ResNet101 的深度编码器，从双时相影像提取层次化语义特征。编码器在**5 个不同深度**输出特征，供 Edge Flow 的边缘特征提取与 Fusion Block 的多尺度融合使用。采用**不同膨胀率（dilated rate）的卷积**以避免下采样造成的细节损失；随着特征图变小，膨胀率增大以从更大空间范围提取信息（见原文 Fig. 3）。
        *   **注意力融合模块（AFM）**：用于比较并融合编码器两支输出的层次化特征。论文指出常规的通道拼接 / 逐元素相减在表达语义信息上较差，故提出 AFM——**同时关注空间与通道信息**，并可按下游任务适配不同的典型融合算子。流程（Fig. 4）：对同层级特征 F1、F2，先按用途做**通道拼接或逐元素相减**，再过 1×1 卷积得到形如 C×H×W 的初步整合特征 Fi；随后由空间分支与通道分支分别生成空间/通道注意力权重。
            *   **空间注意力分支**：特征经两层逐点（1×1）卷积，并配合 BN 与 ReLU，得到空间注意力权重 Ws（见下方公式）。
            *   **通道注意力分支**：（提取缓存在描述 AFM 通道分支时被截断，r 为通道压缩因子；通道分支的完整算式 PDF 提取文本未覆盖，待核。）
    2.  **Edge Flow（边缘流）**：用**门控卷积层（GCL）** 处理来自层次语义特征的边缘信息以生成清晰边界；通过**局部监督（local supervision）** 强制其只关注边缘相关信息。
    3.  **Fusion Block（融合块）**：整合 Segment Flow 的深层语义特征与 Edge Flow 的边缘特征生成最终二值图。内部用**面向边缘特征的空洞空间金字塔池化（Edge-ASPP）** 整合深层语义与边缘特征生成多尺度特征；最后由 final fusion module 将多尺度特征融合为带精细边界的违建分割结果。
*   **数学公式/机制直观解释**：AFM 空间注意力权重 `Ws = BN(Conv1(ReLU(BN(Conv1(Fi)))))`（Eq. 1，其中 Conv1 为 1×1 逐点卷积、BN 为 BatchNorm）。直观上：对整合特征 Fi 做两轮"1×1 卷积 + BN + ReLU"非线性变换，学习出一张空间权重图，决定哪些空间位置更重要。
*   **训练方式**：端到端监督。网络由**逐像素的边缘标签与分割标签共同监督**（Fig. 2）：L_seg 监督变化图，L_edge 监督边缘提取。（两者的具体函数形式 / 加权方式在提取缓存中未覆盖，待核。）
*   **推理流程**：输入一对卫星影像 → 共享权重 Siamese 编码器提多尺度特征 → Segment Flow 经 AFM 做时相间融合、Edge Flow 经 GCL 提边缘 → Fusion Block（含 Edge-ASPP）融合两路 → 输出违建二值图。
*   **与已有方法的差异**：
    *   **vs. 依赖城市数据库的方法**：IBMNet 摒弃对城市数据库的依赖，直接从影像端到端生成统一结果，解决数据库更新慢、覆盖不全（尤其郊区）的限制。
    *   **vs. 其他深度学习变化检测模型**：专门设计 **Edge Flow** 强化边缘与小目标检测（违建常为小型、不规则结构）；**AFM** 是专为双时相特征融合设计的模块，比通用拼接/相减更具针对性。
    *   **（论文类型特化分析 - 变化检测/语义分割类）**：本任务是一种**新建违建的变化检测（逐像素二值分割）**。Backbone 为改自 ResNet101 的 Siamese 编码器，处理双时相输入；无典型 Anchor/Query 机制，而是靠双流（语义流+边缘流）+ 特征融合提升复杂场景中小目标的检测与分割精度。

## 实验

*   **使用的数据集**：**违章建筑监测数据集（IBMD）**，用**北京市政府**提供的数据构建，含 **5230 对**卫星影像。
*   **实现与评估范围**：在**中国**实现并评估（论文强调中国近四十年快速城镇化但仍受违建困扰）。
*   **对比方法**：论文称在 IBMD 上做了**对比实验与消融实验**（Section IV 报告对比、Section V 报告消融）。提取缓存（前 12 页）未列出具体对比方法清单；相关工作部分提及的同类深度学习变化检测方法包括 U-Net、DBN、GAN、RNN/LSTM、纯 Transformer 与 CNN-Transformer 混合等流派（用作背景，非必为对比基线）。具体基线名称待核。
*   **评价指标**：
    *   常规指标：F1、总体精度 OA、（mIoU 等）。
    *   **专门指标**：为衡量违建/合建判别力提出 **OA_B、F1_B、IoU_B**。
*   **主实验结果**：摘要明确给出关键数字——**F1 = 0.7990，IoU_B = 0.7449**，表明模型在多场景下检测违建并与合建区分的能力强。
*   **消融实验**：Section V 报告消融以验证各组件（Edge Flow、AFM 等）有效性；具体数值在提取缓存中未覆盖，待核。
*   **泛化展望**：摘要与结论部分表示方法在有相似问题的其他城市/国家也有前景；据原文后续页（提取缓存未覆盖，待核），作者在 p.13 提到"将在其他城市和国家开展更多实验以进一步评估"，并提及对三种不同高分辨率卫星影像的性能评估。是否已做跨城市独立测试，提取缓存未明确。
*   **效率信息**：提取缓存未提供参数量、FLOPs、推理速度等数据。

## 局限

*   **数据局限性**：IBMD 仅基于北京数据构建。违建特征因城市规划、地理环境、建筑风格而异，模型在其他城市/国家的泛化能力有待进一步验证（作者亦在 p.13 将"更多城市/国家实验"列为未来工作）。
*   **假设依赖**：方法假设违建共享可被深度学习捕捉的共同物理特征（如较低高度、均质屋顶颜色）。现实中违建形式多样，可能存在视觉特征不显著或与周围环境极相似的情况。
*   **计算成本未明**：ResNet101 Backbone + 额外 Edge Flow + 复杂 Fusion（Edge-ASPP）计算成本可能较高，论文（提取缓存范围内）未提供效率分析；对实际部署是需考虑的因素。
*   **边界条件**：影像分辨率、光照、阴影、云遮挡等会影响检测精度，提取缓存范围内未深入探讨其鲁棒性影响。
*   **定义依赖（论文亦自陈）**：模型检测的本质是**基于物理特征变化的"新增可疑建筑"**，新增建筑是否违章最终仍需法规与许可文件界定。论文输出的是**可疑目标**，是数据采集与缩小排查范围的工具，不能替代法律判断。

## 个人评论

1.  **问题驱动的网络架构设计**：双流（语义流+边缘流）紧贴违建监测特点——既要宏观语义识别，又要精细边界以提取小型/不规则目标。这种"先定义问题、再设计网络"的思路值得借鉴。
2.  **AFM 的针对性**：AFM 并非 SE/CBAM 式通用注意力，而是把空间+通道注意力与"拼接/相减"两种融合算子结合、面向双时相特征融合，体现了模块设计随下游任务自适应的灵活性。
3.  **范式转变的价值**：核心贡献是**完全不依赖城市数据库、仅靠遥感影像**的监测范式，提升了时效性、覆盖面与可用性，对突破"数据壁垒"类现实问题有启发。但需清醒：它把"违章判定"前移为"可疑新增建筑检测"，法律判定仍在闭环之外。
4.  **领域专用指标**：意识到通用分割指标不足以反映"区分违建/合建"这一任务本质，提出 OA_B/F1_B/IoU_B，体现严谨的实验设计。
5.  **可改进处（基于提取范围内的信息）**：单一城市数据集 + 缺少效率分析 + 缺少跨域验证，使"对其他城市/国家有前景"目前更像展望而非实证；若能补上参数量/速度与至少一个跨城市测试，论文的"可部署性"说服力会更强。

### 使用建议

*   **如果快速了解**：读**摘要、引言、结论**即可掌握动机、核心方法、贡献与结论。
*   **如果复现**：重点读 **III-A（网络架构）**，结合 **Fig. 2（整体）、Fig. 3（编码器膨胀率 Backbone）、Fig. 4（AFM）**；并关注损失函数（L_seg / L_edge）与 IBMD 数据集构建方式（这两部分细节在提取缓存中未覆盖，需查原文 III-B/III-C）。
*   **如果借鉴创新点**：
    *   双流（语义+边缘）思路 → 迁移到其他需精细边界的分割任务。
    *   AFM 设计 → 处理多时相 / 多模态特征融合。
    *   "去数据库化"范式 → 迁移到其他存在数据壁垒的遥感应用（如监测特定设施）。
*   **如果写 Related Work**：归入"**基于深度学习的变化检测**"与"**违章/非法建筑遥感监测**"两类，作为结合 Siamese + 注意力融合 + 边缘聚焦的代表性方法。

## 相关论文与链接

> - [[T_遥感_建筑检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本论文位于**遥感 + 计算机视觉（深度学习）交叉领域**，聚焦**城市违章建筑监测**这一应用。它把"新建违建识别"建模为**双时相 VHR 卫星影像的变化检测（逐像素二值分割）**问题，用深度学习自动识别新出现的违建。发表于 **IEEE TGRS 2024（Vol. 62, Art. 4703115）**，作者来自北京大学。归入主题"遥感_建筑检测"，与"变化检测""深度学习遥感"密切相关。

## 2. 一句话总结
本文提出 IBMNet——一个边缘聚焦的 Siamese 双流网络（分割流 + 边缘流，含 AFM 与门控卷积），仅以双时相卫星影像为唯一数据源、不依赖城市数据库地监测新建违章建筑，在自建 IBMD 数据集上取得 F1=0.7990、IoU_B=0.7449。

## 3. 背景与问题
*   **为什么要做**：快速城市化中违建普遍且难治理。监管难点包括：分布零散、建造极快（可一夜建成、每天 2–3 层）；立法不统一存在灰色地带；政府缺乏大尺度准确数据获取的技术-行政手段，且央地政策不一致阻碍信息获取与执法；长期违建拆除与住户补偿成本高。
*   **之前方法的问题**：已有用 VHR 影像监测违建的工作仍需城市数据库（地籍图、施工许可、城市规划）支撑——数据库更新慢、覆盖不全（尤其郊区）、受政府部门间沟通与层级不一致影响，难以匹配违建的快速建造。
*   **核心矛盾**：违建快速出现 vs. 现有手段低时间分辨率、受限于数据库更新与空间覆盖。解法是以卫星影像为唯一数据源、把违建监测与城市数据库解耦。

## 4. 核心贡献
1.  **双流变化检测网络 IBMNet**：基于 Siamese + GCL；Edge Flow 细化边界并提取小型违建；AFM 融合双时相特征。自称首个将边缘聚焦方法引入违建监测，提升精度同时降低数据需求。
2.  **仅靠卫星影像、规避数据库局限**：从影像生成统一结果，提升检测频率、支持早期主动监管、覆盖郊区、降低成本。
3.  **领域专用指标**：OA_B、F1_B、IoU_B，衡量在不显式学习合法建筑特征下区分违建/合建的能力。
4.  **可行性初步验证**：验证"仅靠遥感影像监测违建"可行，迈向高效、大范围的违建监管与数据采集。

## 5. 方法详解
*   **整体框架**：Siamese 网络，输入两张 RGB 影像、输出二值变化图；三部分 = Segment Flow + Edge Flow + Fusion Block。
*   **Segment Flow**：
    *   **Siamese 编码器**：两个权重共享、改自 ResNet101 的编码器，在 5 个深度输出层次特征；用不同膨胀率卷积避免下采样的细节损失，特征图越小膨胀率越大以扩大感受野（Fig. 3）。
    *   **AFM**：对同层级 F1、F2 先按用途做"通道拼接 / 逐元素相减 + 1×1 卷积"得整合特征 Fi（C×H×W），再经空间分支与通道分支生成注意力权重。空间分支：两层 1×1 卷积 + BN + ReLU，`Ws = BN(Conv1(ReLU(BN(Conv1(Fi)))))`（Eq.1）。论文强调 AFM 同时关注空间与通道、可适配不同融合算子，优于简单拼接/相减。（通道分支完整算式因提取缓存在 Fig.4 描述处截断，待核。）
*   **Edge Flow**：门控卷积层（GCL）处理层次语义特征、生成清晰边界；用局部监督强制其只关注边缘信息。
*   **Fusion Block**：用 Edge-ASPP 整合深层语义 + 边缘特征生成多尺度特征，再由 final fusion module 融合为带精细边界的违建分割结果。
*   **训练**：端到端监督，逐像素边缘标签 + 分割标签共同监督（L_edge 监督边缘、L_seg 监督变化图）；损失的具体形式与权重提取缓存未覆盖，待核。
*   **vs. 已有**：摒弃城市数据库依赖；专设 Edge Flow 强化小目标边界；AFM 针对双时相融合优于通用算子。

## 6. 实验与结果
*   **数据集**：IBMD，北京市政府数据构建，5230 对卫星影像；在中国实现评估。
*   **对比/消融**：Section IV 报告对比实验、Section V 报告消融。提取缓存（前 12 页）未列出具体对比基线名单与消融数值，待核。相关工作中提及的同类方法流派含 U-Net、DBN、GAN、RNN/LSTM、Transformer / CNN-Transformer 混合等（背景，非必为基线）。
*   **指标**：常规 F1 / OA（及 mIoU 等）+ 专门 OA_B / F1_B / IoU_B。
*   **主结果**：F1 = 0.7990，IoU_B = 0.7449（摘要明确给出）。
*   **效率**：参数量 / FLOPs / 速度，提取缓存未提供。
*   **泛化**：据原文后续页（p.13，提取缓存未覆盖，待核）提到将在其他城市/国家做更多实验、并对三种高分辨率卫星影像评估；是否已完成跨城市独立测试，提取缓存未明确。

## 7. 这篇论文真正有价值的地方
1.  **问题驱动的架构**：双流贴合"宏观语义 + 精细边界"的违建监测需求。
2.  **AFM 的任务自适应**：把空间+通道注意力与"拼接/相减"算子结合，专为双时相融合设计。
3.  **范式转变**：完全不依赖城市数据库、仅靠遥感影像，提升时效与覆盖面，对突破数据壁垒有启发。
4.  **领域专用指标**：OA_B/F1_B/IoU_B 抓住"区分违建/合建"的任务本质，而非套用通用分割指标。

## 8. 局限与问题
*   **数据单一**：IBMD 仅北京，跨城市/国家泛化待验证（作者亦列为未来工作）。
*   **假设依赖**：假设违建共享可学共同物理特征（低矮、均质屋顶色），但违建形式多样、可能视觉不显著。
*   **效率未报**：ResNet101 + Edge Flow + Edge-ASPP 成本或较高，提取缓存范围内无效率分析。
*   **干扰因素**：分辨率/光照/阴影/云遮挡对鲁棒性的影响未深入。
*   **法律边界**：输出是"可疑新增建筑"而非法律意义上的"违章"判定，仍需法规/许可闭环。

## 9. 我该怎么使用这篇论文
*   **快速了解**：读摘要、引言、结论。
*   **复现**：重点 III-A，结合 Fig. 2/3/4；关注 III-B 损失函数与 III-C IBMD 构建（这两部分在提取缓存外）。
*   **借鉴**：双流"语义+边缘"思路、AFM 双时相融合、"去数据库化"范式。
*   **写 Related Work**：归入"深度学习变化检测"与"违建/非法建筑遥感监测"，作为 Siamese + 注意力融合 + 边缘聚焦的代表。

## 10. 和其他论文的关系
主题为 `T_遥感_建筑检测`。可能相关方向：
*   基于深度学习的**建筑物提取 / 变化检测**论文（如 FC-Siam 系列、DSIFN、BiT 等 Siamese / Transformer 变化检测）。
*   **边缘检测在语义分割**中的应用（GCL / Gated-SCNN 思路、ASPP/DeepLab 系列）。
*   其他**城市环境监测**（目标识别、变化检测）论文。
本笔记不臆造库内具体双链；如需建立，应按库中实际存在的同主题笔记 stem 补 `[[...]]`。

## 11. 关键词
违章建筑监测、变化检测、深度学习、Siamese 网络、边缘聚焦、门控卷积（GCL）、注意力融合模块（AFM）、Edge-ASPP、卫星影像、遥感、逐像素语义分割、IBMNet、IBMD、OA_B/F1_B/IoU_B。

## 12. 可信度说明
本精读笔记**基于 PDF 提取缓存（前 12/15 页，约 25000 字符上限，文本在 Fig.4 AFM 描述处截断）** 与原笔记的少量后续页线索生成，未编造信息。可据提取文本确证的内容包括：发表信息（IEEE TGRS 2024, Vol.62, Art.4703115, DOI 10.1109/TGRS.2024.3379567，北京大学）、研究动机、四条贡献、网络三部分结构（Siamese 编码器 / AFM / Edge Flow / Fusion Block / Edge-ASPP）、AFM 空间注意力公式 Eq.1、数据集（IBMD, 北京, 5230 对）、主结果（F1=0.7990, IoU_B=0.7449）、专用指标定义。**因提取截断而未能据原文核实、标注为"待核"的**包括：AFM 通道注意力分支完整算式、L_seg/L_edge 的具体函数形式与权重、对比实验的基线清单与数值、消融实验数值、效率数据、跨城市泛化是否已实测。涉及 p.13 的泛化/未来工作描述来自原笔记后续页线索，标注为"据原文后续页，提取缓存未覆盖，待核"。总体可信度：高（核心事实与关键数字均有提取文本直接支撑）。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 2086 字符/页; 但提取缓存仅前 12/15 页且在 25000 字符上限处于 Fig.4 描述截断); 来源缓存: `.paper-cache/extracts/An_Optimized_Edge-Focused_Siamese_Network_for_Monitoring_New_Illegal_Buildings_Using_Satellite_Images.txt` (12/15 页; 原 AI 主体 12/15 + 后续页线索 13-15); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 复核优化: 2026-06-18 (修正 venue 为 IEEE TGRS、补 DOI、重建英文摘要与中译、标注待核项)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本（线索级，非全文）。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: In summary, we conducted a preliminary verification of
- p.13: In areas where illegal structures resemble those found in
- p.13: Beijing, primarily consisting of simple or colored steel build-
- p.13: In future work, we will continue to conduct more experi-
- p.13: ACKNOWLEDGMENT
- p.13: The authors also appreciate the detailed comments from the
- p.13: REFERENCES
- p.14: Markov random field and hopfield-type neural networks for unsupervised
- p.14: method based on multiscale graph convolutional network and metric
- p.15: The impact of urban form on commuting patterns on the city fringe
- p.15: University, Beijing, China, in 2022, where he is
- p.15: His research interests include remote sensing

### 缺失页关键摘录

- p.13: ments in other cities and other countries for further evaluation
- p.13: mance evaluation of three different high resolution satellite images
- p.15: a new dataset for remote sensing image change detection,” Remote
<!-- AI_READING_NOTE_END -->
