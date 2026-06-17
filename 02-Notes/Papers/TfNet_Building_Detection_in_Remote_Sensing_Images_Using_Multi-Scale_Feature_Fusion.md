---
title: TfNet_Building_Detection_in_Remote_Sensing_Images_Using_Multi-Scale_Feature_Fusion
authors:
  - "Chunlei Han"
  - "Luyang Mei"
  - "Yao Lu"
  - "Zhongqian Jin"
  - "Wang Zhao"
  - "Shuang Wang"
  - "Siyu Cao"
  - "Rui Yang"
year: 2024
venue: "IGARSS 2024 (IEEE International Geoscience and Remote Sensing Symposium)"
doi: 10.1109/IGARSS53475.2024.10641463
pdf: [[TfNet_Building_Detection_in_Remote_Sensing_Images_Using_Multi-Scale_Feature_Fusion.pdf]]
primary_topic: T_遥感_建筑检测
topics:
  - "T_遥感_建筑检测"
status: ai-read
reading_stage: ai-complete
confidence: high
source_basis: pdf-text
date_added: 2026-06-05
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/TfNet_Building_Detection_in_Remote_Sensing_Images_Using_Multi-Scale_Feature_Fusion.txt
---

# TfNet_Building_Detection_in_Remote_Sensing_Images_Using_Multi-Scale_Feature_Fusion

## 基本信息
- **PDF**: [[TfNet_Building_Detection_in_Remote_Sensing_Images_Using_Multi-Scale_Feature_Fusion.pdf]]
- **primary_topic**: `T_遥感_建筑检测`
- **topics**: `T_遥感_建筑检测`
- **状态**: ai-read (已据 PDF 提取文本整理, 待人工复核)
- **date_added**: 2026-06-05

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | TFNet: Building Detection in Remote Sensing Images Using Multi-Scale Feature Fusion |
| **作者** | Chunlei Han; Luyang Mei; Yao Lu; Zhongqian Jin; Wang Zhao; Shuang Wang; Siyu Cao; Rui Yang（西安导航技术研究所 + 西安电子科技大学人工智能学院） |
| **发表时间** | 2024 |
| **刊物/会议** | IGARSS 2024（IEEE International Geoscience and Remote Sensing Symposium，4 页短文/会议论文） |
| **DOI** | 10.1109/IGARSS53475.2024.10641463 |

## 摘要

**英文原摘要（据提取文本清理）**：

> Building detection in remote sensing images is significant to urban land planning, battlefield environment perception, and illegal building monitoring. Existing methods excel in detecting small-scale building areas but struggle with remote sensing images with diverse and multi-scale characteristics. To solve this problem, this paper proposes a Two-stage Feature fusion Network (TFNet). Specifically, we propose a dense short connection module to enable internal interaction between features from different layers, achieving intra-stage feature fusion. Moreover, the holistically-nested edge detection (HED) network is used to integrate the effective information between different layers to achieve inter-stage feature fusion. In addition, an adaptive fusion weight is introduced to make the model adaptively select the weights of varying levels of features. Experimental results demonstrate the effectiveness of TFNet in improving the detection performance of multi-scale buildings in remote sensing images.
>
> Index Terms — building detection, remote sensing, feature fusion, multi-scale.

**中文翻译**：

> 遥感图像中的建筑物检测对城市土地规划、战场环境感知和违章建筑监测具有重要意义。现有方法在检测小尺度建筑区域上表现良好，但在面对多样化、多尺度特征的遥感图像时效果欠佳。为解决该问题，本文提出两阶段特征融合网络（TFNet）。具体而言：提出密集短连接模块（DSCM），使不同层特征之间产生内部交互，实现阶段内（intra-stage）特征融合；采用整体嵌套边缘检测（HED）网络整合不同层之间的有效信息，实现阶段间（inter-stage）特征融合；此外引入自适应融合权重（AFW），使模型能自适应地选择不同层级特征的权重。实验结果表明，TFNet 能有效提升遥感图像中多尺度建筑物的检测性能。
>
> 关键词：建筑检测、遥感、特征融合、多尺度。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：基于遥感图像的建筑物检测对城市变化监测、城市规划、地形图生产意义重大，并被作者明确关联到城市土地规划、战场环境感知、违章建筑监测等应用。早期方法主要依赖像素、边缘、纹理、阴影等手工特征，易受光照条件、环境因素、传感器质量和建筑风格影响，因此只适用于特定数据集，在更复杂多样的场景下难以取得理想效果。
- **之前方法的问题**：1）早期 CNN 方法沿用计算机视觉的图像识别范式，把遥感图像裁成 patch 逐块分类（是否为建筑），计算复杂度高且产生马赛克现象；2）语义分割（逐像素打标签）独立处理每个像素，可能遗漏小建筑或在大建筑内部产生空洞；3）实例分割尝试为每个建筑实例分配唯一标签。**核心矛盾**：随着网络加深，深层特征抽象/语义能力变强但图像细节信息丢失严重，难以应对小目标；浅层特征感受野有限、无法捕捉全局特征，检测大目标能力有限。
- **作者想解决的核心矛盾**：**单一层级特征不足以处理多尺度场景**——浅层善于捕捉小目标的细粒度细节与边缘，深层提供有助于大目标定位的高层语义；通过融合不同层级特征，增强模型对多尺度目标的感知与处理能力。

## 关键贡献

1.  提出 **TFNet** 框架——一种结合**阶段内(intra-stage)** 与**阶段间(inter-stage)** 特征融合的遥感图像建筑检测方法，专门应对多尺度问题。其中用密集短连接模块实现阶段内融合，用 HED 结构融合不同层级特征作为输出实现阶段间融合。
2.  提出**密集短连接模块(DSCM)**，以自上而下(top-down)的方式促进不同层特征间的交互，实现阶段内特征融合。
3.  考虑到不同层级特征对不同尺度目标检测的重要性差异，引入**自适应融合权重(AFW)**，使模型在训练过程中自适应学习各层特征的融合权重。
4.  在 **Massachusetts** 与 **WHU** 两个多尺度遥感数据集上实验，证明本方法优于若干典型 CNN 目标检测方法（U-Net、FCN、SegNet）。

## 方法

- **整体框架**：TFNet 基于 **HED（Holistically-nested Edge Detection）** 结构改进。HED 在传统串行结构上增加多条水平短连接，从不同层级获取多个特征并直接相加融合，得到输出（Fig. 2）。TFNet 在 HED 基础上构建**四个待融合的输出层**（Fig. 1），由于各输出层尺寸不同，用**反卷积**将各层放大到统一尺寸，缩放因子分别为 **2、4、8、16**，归一化尺寸后再通过四个输出层的加权相加得到预测结果。
- **输入输出**：输入为遥感图像，输出为建筑物的像素级预测结果图。
- **关键模块**：
    1.  **修改的密集卷积块(Modified Dense Block)**：用于提取建筑特征，同时保留 HED 结构。DenseNet 的特征图数量随深度线性增长，直接用于大规模遥感建筑检测时计算需求过高；为缓解该问题，本文用**单跳连接(single skip-connection)** 替换不同层之间的多跳连接，减少计算量（Fig. 3）。
    2.  **密集短连接模块(DSCM)**：实现阶段内特征融合的核心，自上而下融合。流程为：左侧密集卷积块的特征先经 **1×1 卷积将尺寸减半**；同时来自上层 DSCM 的特征经卷积或反卷积后，与左侧特征**拼接(concatenate)**；合并后的特征作为本层的输出特征图，并继续传递给下一层 DSCM（Fig. 4）。模型串联四个 DSCM（Fig. 1），实现多层级特征的自适应、选择性融合。
    3.  **自适应融合权重(AFW)**：针对阶段间融合的改进。处理不同分辨率数据集时，不同层级特征应被区别强调（例如较大建筑应更关注语义信息）。与 HED 直接相加各特征图不同，TFNet 采用加权相加：模型输出 `Y = Σ_{i=1..4} (α_i · F_i)`，其中 `Y` 为预测结果，`α_i` 为各待融合特征图的权重，`F_i` 为经过 DSCM 后得到的特征图（式(1)）。
- **模块连接与流程**：网络先用修改的密集卷积块提取特征 → 串联四个 DSCM 自上而下完成阶段内融合 → 每个 DSCM 输出经反卷积上采样到统一尺寸（缩放因子 2/4/8/16）→ 四个特征图通过自适应权重 `α_i` 加权相加得到最终预测 `Y`（Fig. 1）。
- **训练方式**：用**交叉熵损失(cross-entropy loss)** 由预测结果与真实标签(ground truth)计算并更新网络参数；训练中模型根据不同分辨率数据集自适应控制不同层级信息的融合比例。权重 `α_i` 与其他网络参数一同被学习更新。
- **训练超参数（据提取文本）**：优化器 **Adam**；学习率 **0.00001**；batch size **4**；训练 **30 epoch**；实现使用 Python 3.7（提取文本另写有 "Python 1.6.0"，疑为 PyTorch 1.6.0 的 OCR 误写）；在单卡 **RTX 2080Ti（12GB 显存）** 上训练。两个数据集统一了数据集比例与超参数设置以保证公平。
- **和已有方法的差异**：相比直接相加多层特征的 HED，TFNet 增加 **DSCM** 做更精细的阶段内自上而下融合，并引入**可学习的自适应权重 AFW**，使模型能依据不同数据集（不同分辨率/不同尺度目标）动态调整各层特征贡献度。

## 实验

- **数据集**：**Massachusetts** [10] 与 **WHU** [11]，均为多尺度遥感图像（建筑）数据集。
- **对比方法**：U-Net、FCN、SegNet。
- **评价指标**：**Precision(%)、Recall(%)、F1 score(%)**。
- **主实验结果（Table 1）**：
    - **Massachusetts**：TFNet（Ours）Precision 82.54 / Recall 67.38 / **F1 74.20**；U-Net 85.82/61.05/71.35；FCN 77.22/71.19/73.96；SegNet 69.82/75.21/72.08。相比 U-Net、FCN、SegNet，F1 分别提升 **2.85%、0.24%、2.12%**。
    - **WHU**：TFNet（Ours）Precision 92.62 / Recall 93.90 / **F1 93.25**；U-Net 92.49/92.82/92.65；FCN 91.25/92.56/91.89；SegNet 91.93/91.97/91.95。F1 在该数据集上也取得最优 93.25。
    - 观察：在 Massachusetts 上 U-Net 精确率最高(85.82)但召回率很低(61.05)，TFNet 通过提升召回(67.38)拿到最高 F1；说明改进点主要体现在 F1 的均衡性上，而非单项指标领先。
- **消融实验（Table 2，DSCM = 密集短连接模块+直接相加融合，AFW = 自适应融合权重）**：
    - **Massachusetts**：仅 DSCM（直接相加）Precision 88.00 / Recall 36.98 / F1 **52.07**；DSCM+AFW 后 82.54/67.38/**74.20**，F1 提升约 **22.13%**。可见仅直接相加时召回极低(36.98)，AFW 主要通过大幅拉高召回改善 F1。
    - **WHU**：仅 DSCM 94.39/92.09/F1 **93.23**；DSCM+AFW 92.62/93.90/F1 **93.25**，F1 仅提升 **0.02%**。说明 AFW 的增益在低分辨率/难度更高的 Massachusetts 上显著，在已较易、F1 已很高的 WHU 上几乎无差别。
- **泛化/鲁棒性**：作者据两数据集上均取得最优 F1，主张方法对多种建筑检测任务具有鲁棒性与更强的特征融合能力。
- **效率信息**：提取文本仅给出训练硬件(RTX 2080Ti 12GB)与超参数，**未报告**参数量、FLOPs、推理速度等效率指标。

## 局限

1.  **计算成本与效率未量化**：论文未报告参数量、FLOPs、推理速度。修改的密集卷积块 + 四个串联 DSCM + 多次反卷积可能带来不小开销，对大规模遥感影像实时处理可能构成挑战（提取文本未明确）。
2.  **数据集覆盖有限**：仅在 Massachusetts 和 WHU 两个数据集上评估，场景多样性有限；论文宣称的泛化性主要由"两数据集均最优"支撑，证据相对薄弱。
3.  **消融不够细**：消融仅对比"无 AFW vs 有 AFW"，未拆解 DSCM 内部各设计（单跳连接、自上而下连接、1×1 降维等）的单独贡献，也未与原始 HED/原始 DenseNet 做组件级对照。
4.  **改进幅度的代表性存疑**：在 WHU 上 TFNet 相对基线和 AFW 消融的 F1 增益都很小（93.25 vs 92.65 / 93.23），主要增益集中在 Massachusetts；说明方法收益对数据集依赖较强。
5.  **结构复杂、可读性受限于会议短文篇幅**：作为 4 页 IGARSS 短文，框架图(Fig.1/3/4)是理解关键，但文本对部分细节（如 DSCM 中卷积/反卷积的具体配置、各输出层通道数）描述不全，复现需依赖图示与合理推断。

## 个人评论

1.  **双阶段融合的拆分清晰**：把特征融合显式分为"阶段内(DSCM 融合同一骨干不同深度的特征)"与"阶段间(HED 融合不同输出层)"两层，是处理多尺度问题的一种"分而治之"思路，结构上比单纯堆 FPN 更有层次感。
2.  **务实的组件改造**：对 DenseNet（多跳→单跳降算量）和 HED（直加→加权）的改造都是针对遥感建筑检测实际约束的小而有效的修改，工程权衡明显，而非堆砌新模块。
3.  **AFW 是性价比高的设计，但要看清它的作用机制**：消融显示 AFW 在 Massachusetts 把 F1 从 52.07 拉到 74.20，关键在于它把召回从 36.98 提到 67.38——即直接相加时模型过度保守（高精确率、低召回），可学习权重让低层/细节特征获得更合理权重从而召回回升。这说明 AFW 的真正价值是缓解"多层直加导致的尺度偏置"，而非泛泛的"更灵活"。
4.  **谨慎看待"超越基线"**：在 WHU 上增益微乎其微，且 Ours 在 Massachusetts 上精确率(82.54)其实低于 U-Net(85.82)，优势仅来自 F1 均衡。把它当作"在难数据集上改善召回/F1 均衡"的方法来理解更准确。

### 使用建议

- **如果快速了解**：读摘要、引言末尾（贡献列表）、Table 1/Table 2 即可掌握核心思路与结论。
- **如果复现**：精读方法部分并对照 Fig. 1/3/4；超参照"Adam, lr=1e-5, batch=4, 30 epoch, RTX 2080Ti"，数据集用 Massachusetts [10] 与 WHU [11]。注意文本对通道数等细节未给全，需结合图示推断。
- **如果借鉴创新点**：重点是 DSCM（阶段内自上而下融合）与 AFW（把多层输出的固定相加换成可学习加权）。两者可作为即插即用组件迁移到其他多尺度分割/检测网络，尤其当基线存在"高精确率低召回"的尺度偏置时值得一试。
- **如果写 related work**：可归入"基于多层级特征融合的多尺度遥感建筑提取"，与借鉴 HED/DenseNet/FPN 的工作并列。

## 相关论文与链接

> - [[T_遥感_建筑检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**遥感图像分析**方向，聚焦**遥感图像中的建筑物检测**任务，发表于 **IGARSS 2024**（IEEE 国际地球科学与遥感大会，4 页会议短文）。核心目标是解决遥感影像中建筑物尺度差异大、多尺度并存导致的检测困难，提升模型在不同尺度目标上的检测均衡性。适合放在"**遥感建筑检测**"或"**多尺度特征融合**"主题下。

## 2. 一句话总结
TFNet 用密集短连接模块(DSCM)做阶段内特征融合、用 HED 结构做阶段间融合，并以自适应融合权重(AFW)把多层输出的固定相加改为可学习加权，从而提升遥感图像中多尺度建筑物的检测性能（在 Massachusetts/WHU 上 F1 优于 U-Net/FCN/SegNet）。

## 3. 背景与问题
- **为什么要做**：遥感建筑检测对城市变化监测、城市规划、地形图生产、违章建筑监测、战场环境感知意义重大。手工特征（像素/边缘/纹理/阴影）受光照、环境、传感器质量、建筑风格影响，泛化差。
- **之前方法的问题**：早期 CNN 用图像识别范式逐 patch 分类→计算量大且有马赛克现象；语义分割逐像素独立处理→易漏小建筑、在大建筑内部留空洞；实例分割为每个实例分配标签。共性瓶颈：普通 CNN 在多尺度目标上难以全尺度保持高精度。
- **作者想解决的核心矛盾**：网络加深→深层语义强但细节丢失（不利小目标）；浅层感受野小、缺全局语义（不利大目标）。**单层级特征不足以处理多尺度场景**，需综合多层级特征——浅层提供小目标细节/边缘，深层提供大目标语义。

## 4. 核心贡献
1.  **TFNet**：结合阶段内 + 阶段间特征融合的遥感建筑检测框架，针对多尺度问题；DSCM 负责阶段内融合，HED 结构融合不同层级输出负责阶段间融合。
2.  **DSCM（密集短连接模块）**：自上而下促进不同层特征交互，实现阶段内融合。
3.  **AFW（自适应融合权重）**：让模型在训练中自适应学习各层级特征的融合权重，替代 HED 的直接相加。
4.  在 **Massachusetts** 与 **WHU** 上验证优于典型 CNN 方法（U-Net/FCN/SegNet）。

## 5. 方法详解
- **整体框架**：在 HED（多条水平短连接、各层特征直接相加得输出）基础上，构建四个待融合输出层（Fig.1）；各层尺寸不同，用反卷积按缩放因子 **2/4/8/16** 放大到统一尺寸，再加权相加得预测。
- **修改的密集卷积块**：DenseNet 特征图数量随深度线性增长，直接用于大规模遥感检测算量过高；本文以**单跳连接替换多跳连接**降低计算量（Fig.3），同时保留 HED 结构。
- **DSCM**（Fig.4，阶段内、自上而下）：左侧密集卷积块特征经 **1×1 卷积尺寸减半**；上层 DSCM 特征经卷积/反卷积后与之**拼接(concat)**；合并特征作为本层输出并下传至下一 DSCM。模型串联**四个 DSCM**。
- **AFW**（阶段间）：`Y = Σ_{i=1}^{4} α_i · F_i`（式1），`α_i` 为可学习的逐层融合权重，`F_i` 为各 DSCM 输出特征图。训练中网络按不同分辨率数据集自适应控制各层信息的融合比例。
- **训练**：交叉熵损失（预测 vs ground truth），Adam，lr=1e-5，batch=4，30 epoch，单卡 RTX 2080Ti(12GB)；α_i 与网络参数联合学习。

## 6. 实验与结果
- **数据集**：Massachusetts [10]、WHU [11]（多尺度遥感影像），统一数据比例与超参。
- **对比**：U-Net、FCN、SegNet；**指标**：Precision/Recall/F1(%)。
- **Table 1 主结果**：
    - Massachusetts：Ours **74.20** F1（82.54/67.38）；U-Net 71.35、FCN 73.96、SegNet 72.08；相比三者 F1 提升 **2.85% / 0.24% / 2.12%**。
    - WHU：Ours **93.25** F1（92.62/93.90）；U-Net 92.65、FCN 91.89、SegNet 91.95。
    - 注意：Massachusetts 上 Ours 精确率(82.54)低于 U-Net(85.82)，优势来自更高召回带来的 F1 均衡。
- **Table 2 消融**（DSCM=含直接相加；AFW=自适应权重）：
    - Massachusetts：DSCM 52.07（88.00/36.98）→ +AFW 74.20（82.54/67.38），F1 **+22.13%**，主要靠召回从 36.98 提到 67.38。
    - WHU：DSCM 93.23（94.39/92.09）→ +AFW 93.25（92.62/93.90），F1 仅 **+0.02%**。
- **效率信息**：除训练硬件与超参外，**未报告**参数量/FLOPs/推理速度。

## 7. 这篇论文真正有价值的地方
1.  **"阶段内 vs 阶段间"的融合二分法**：DSCM 融合同一骨干不同深度、HED 融合不同输出层，层次清晰，是组织多尺度融合的一种可迁移思路。
2.  **务实的组件级改造**：多跳→单跳降算量、直加→加权融合，针对遥感建筑检测的真实约束做小改动，工程权衡清楚。
3.  **AFW 的机制洞察**：消融揭示其本质是修正"多层直加导致的尺度偏置"——把过度保守（高精确、极低召回）的模型召回拉回，从而显著改善难数据集上的 F1。这是比"更灵活"更具体的价值点。

## 8. 局限与问题
1.  **效率未量化**：无参数量/FLOPs/速度报告，DSCM 串联 + 反卷积的开销未知。
2.  **数据集仅两个**：泛化性证据较弱（仅"两集均最优"）。
3.  **消融粗**：只比 AFW 有无，未拆 DSCM 内部各设计的贡献，也无组件级对照原始 HED/DenseNet。
4.  **增益对数据集依赖强**：WHU 上提升微乎其微（F1 +0.02%），主要增益集中在 Massachusetts；且 Ours 在 Massachusetts 精确率反低于 U-Net。
5.  **会议短文细节不全**：通道数、DSCM 内卷积/反卷积具体配置等需依赖图示推断，复现门槛体现在此。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 贡献列表 + Table 1/2。
- **复现**：精读 Fig.1/3/4 与方法节；超参 Adam/lr=1e-5/batch=4/30 epoch，数据集 Massachusetts+WHU；细节缺失处结合图推断。
- **借鉴创新点**：DSCM（阶段内自上而下融合）与 AFW（多层输出可学习加权），可作即插即用组件，尤其用于纠正基线"高精确低召回"的尺度偏置。
- **写 related work**：归入"基于多层级特征融合的多尺度遥感建筑提取"，与借鉴 HED/DenseNet/FPN 的工作并列。

## 10. 和其他论文的关系
方法直接建立在 **HED**（[8]，Xie & Tu, ICCV 2015）与 **DenseNet**（[9]，Huang et al., CVPR 2017）之上；对比的基线 **U-Net**（[3]）、**FCN**（[4]）、**SegNet**（[5]）是语义分割里程碑。背景中还提及实例分割路线的建筑提取（[6][7]）。数据集来自 Mnih 的 Massachusetts [10] 与 Ji et al. 的 WHU [11]。在 [[T_遥感_建筑检测]] 主题下，它与所有使用多尺度/多层级特征融合（FPN 类、HED 类、DenseNet 改造类）的建筑检测工作相关。

## 11. 关键词
建筑检测, 遥感图像, 特征融合, 多尺度目标检测, DenseNet, HED, 密集短连接模块(DSCM), 自适应融合权重(AFW), TFNet, 语义分割, IGARSS

## 12. 可信度说明
本篇精读基于提取文本的**摘要、引言、方法（含式(1)与 Fig.1/3/4 文字描述）、实验（Table 1/Table 2 完整数值）、结论与参考文献**生成，提取覆盖全部 5/5 页且连续完整，关键表格数值与超参数均可逐条对照原文，因此信息基础**可靠**。需注意两点：venue 经核实为 **IGARSS 2024**（非"Remote Sensing"期刊），已据页脚 DOI 10.1109/IGARSS53475.2024.10641463 更正；提取文本中的 "Python 1.6.0" 疑为 PyTorch 1.6.0 的 OCR 误写，已在正文标注。其余未明确信息（参数量/FLOPs/推理速度、DSCM 通道配置）均如实标注为"未明确"。

---

> **可信度补充**: PDF 提取质量 = **high** (5/5 页, 全文连续, 表格数值与超参完整可核); 来源缓存: `.paper-cache/extracts/TfNet_Building_Detection_in_Remote_Sensing_Images_Using_Multi-Scale_Feature_Fusion.txt`; 生成日期: 2026-06-05; 复核整理: 2026-06-18 (据提取文本订正 venue/DOI 与超参细节); 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
