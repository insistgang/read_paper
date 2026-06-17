---
title: machines-12-00557
authors:
  - "Qinghui Zhou"
  - "Diyi Zhang"
  - "Haoshi Liu"
  - "Yuping He"
year: 2024
venue: "Machines"
doi: 10.3390/machines12080557
pdf: [[machines-12-00557.pdf]]
primary_topic: C2_目标检测_违建_车辆_船舶_行人
topics:
  - "C2_目标检测_违建_车辆_船舶_行人"
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
extract_cache: .paper-cache/extracts/machines-12-00557.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# machines-12-00557

## 基本信息
- **PDF**: [[machines-12-00557.pdf]]
- **primary_topic**: `C2_目标检测_违建_车辆_船舶_行人`
- **topics**: `C2_目标检测_违建_车辆_船舶_行人`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-05

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | KCS-YOLO: An Improved Algorithm for Traffic Light Detection under Low Visibility Conditions |
| **作者** | Qinghui Zhou; Diyi Zhang; Haoshi Liu (北京建筑大学 机电与车辆工程学院); Yuping He (安大略理工大学) |
| **发表时间** | 2024 (Received 30 Jun, Accepted 14 Aug, Published 15 Aug 2024) |
| **刊物/会议** | Machines (MDPI), 2024, 12(8), 557 |
| **DOI** | 10.3390/machines12080557 |

## 摘要

> 来源: 据 PDF 提取文本整理。

**英文原文（清理后）**：

Autonomous vehicles face challenges in small-target detection and, in particular, in accurately identifying traffic lights under low visibility conditions, e.g., fog, rain, and blurred night-time lighting. To address these issues, this paper proposes an improved algorithm, namely KCS-YOLO (you only look once), to increase the accuracy of detecting and recognizing traffic lights under low visibility conditions. First, a comparison was made to assess different YOLO algorithms. The benchmark indicates that the YOLOv5n algorithm achieves the highest mean average precision (mAP) with fewer parameters. To enhance the capability for detecting small targets, the algorithm built upon YOLOv5n, namely KCS-YOLO, was developed using the K-means++ algorithm for clustering marked multi-dimensional target frames, embedding the convolutional block attention module (CBAM) attention mechanism, and constructing a small-target detection layer. Second, an image dataset of traffic lights was generated, which was preprocessed using the dark channel prior dehazing algorithm to enhance the proposed algorithm's recognition capability and robustness. Finally, KCS-YOLO was evaluated through comparison and ablation experiments. The experimental results showed that the mAP of KCS-YOLO reaches 98.87%, an increase of 5.03% over its counterpart of YOLOv5n. This indicates that KCS-YOLO features high accuracy in object detection and recognition, thereby enhancing the capability of traffic light detection and recognition for autonomous vehicles in low visibility conditions.

**中文翻译**：

自动驾驶车辆在小目标检测上面临挑战，尤其是在低能见度条件（如雾、雨、夜间模糊灯光）下准确识别交通灯。为解决这些问题，本文提出改进算法 KCS-YOLO，以提升低能见度条件下交通灯检测与识别的准确性。首先，对不同 YOLO 算法进行了对比评估，基准测试表明 YOLOv5n 以更少的参数取得了最高的平均精度均值（mAP）。为增强小目标检测能力，本文在 YOLOv5n 基础上构建 KCS-YOLO：用 K-means++ 算法对标注的多维目标框进行聚类、嵌入 CBAM 卷积块注意力机制、并构建小目标检测层。其次，生成了一个交通灯图像数据集，并用暗通道先验去雾算法对其预处理，以增强算法的识别能力和鲁棒性。最后，通过对比实验与消融实验对 KCS-YOLO 进行评估。实验结果表明，KCS-YOLO 的 mAP 达到 98.87%，比其对照模型 YOLOv5n 提升了 5.03%。这说明 KCS-YOLO 在目标检测与识别上具有高精度，从而增强了自动驾驶车辆在低能见度条件下对交通灯的检测与识别能力。

**关键词**：object detection and recognition; YOLOv5n; KCS-YOLO (an improved algorithm); low visibility; autonomous vehicles。

## 研究背景与动机

- **为什么要做**：交通灯检测与识别对自动驾驶车辆的安全运行至关重要，而低能见度是引发交通事故的主要因素之一。提取文本给出能见度的定义——在复杂气象条件下能辨识前方物体的距离，并明确"能见度低于 300 m 即视为低能见度"，对自动驾驶系统构成挑战。
- **影响能见度的两个因素**：论文明确归纳为 (1) 光照差异（自然光与人工光，照度与能见度成正比）和 (2) 大气透明度（大雨、雪、雾、沙尘使大气浑浊，透明度与能见度成正比）。交通灯与车辆距离远时目标小、与背景亮度对比度低，更难被检测。
- **之前方法的问题**：传统交通灯检测多从颜色特征出发结合机器学习/图像处理，精度低、易漏检误检。深度学习方法虽被广泛应用，但仍存在不足：Tian & Kim 用暗通道先验预处理 + Faster-RCNN 做车辆检测，精度和实时性仍待提升；YOLOv3 系（Possatti 融合先验地图、Du 上采样多特征融合）检测精度仍偏低；Mao 等优化 YOLOv7（引入注意力 + SIOU 损失）但未考虑复杂天气；Appiah & Mensah 用 YOLOv7+ESRGAN 应对恶劣天气但未专门针对小目标；Li 等基于改进 YOLOv4 但早于 YOLOv5 系，精度欠佳。
- **核心矛盾**：在低能见度、复杂天气下，如何同时保证对交通灯这类**远距离小目标**的高检测精度与算法实用性。作者旨在弥补现有 YOLO 算法在低能见度场景下检测能力的不足。

## 关键贡献

1.  **基准选型确定基线**：对不同版本 YOLO 算法做性能对比（表 1，涵盖 AP/mAP/Params/F1/FLOPs），结论是 **YOLOv5n 以更少的参数取得最高 mAP**，故选其为改进基线。
2.  **提出 KCS-YOLO 架构**（名字 KCS 取自三项改进的首字母 K-means++、CBAM、Small-target layer）：
    - **K-means++ 聚类**：对标注的多维边界框做聚类，得到更贴合本数据集尺寸分布的先验锚框，提升定位精度。
    - **CBAM 注意力机制**：嵌入卷积块注意力模块，自适应聚焦更关键的特征，增强低能见度下的特征表达。
    - **小目标检测层**：新增专门面向小目标的检测层，提升对远距离、小尺寸交通灯的检测能力。
3.  **数据集生成与去雾预处理**：自建包含 **3053 个低能见度交通灯样本**的数据集，并用**暗通道先验去雾算法**预处理图像以增强清晰度与对比度后再输入网络。
4.  **实验验证**：通过与 YOLOv5n、其变体及 Faster-RCNN 的对比实验和消融实验，验证有效性。**KCS-YOLO 的 mAP 达 98.87%，比 YOLOv5n 提升 5.03%**。

## 方法

- **整体框架**：流程分为**数据预处理**和**模型检测**两阶段。感知系统直接采集原始图像 → 暗通道先验去雾算法预处理 → 处理后图像输入 **KCS-YOLO** 做交通灯检测与识别。
- **输入输出**：
    - **输入**：低能见度（雾、雨等）条件下采集的原始 RGB 图像。
    - **输出**：图像中交通灯的位置（边界框）与颜色/状态类别（red / yellow / green / off 四类）。
- **关键模块**：
    1.  **暗通道先验去雾预处理（3.2 节）**：
        - **去雾成像模型**（式 1）：`I(x) = J(x)t(x) + A(1 − t(x))`，其中 `I(x)` 为有雾图像、`J(x)` 为待恢复无雾图像、`A` 为全局大气光、`t(x)` 为光的透射率。求 `J(x)` 的关键在于估计 `t(x)` 与 `A`。
        - **暗通道先验（3.2.1，引 He et al. [17]）**：绝大多数非天空局部区域中，RGB 至少一个通道强度趋近于零，即 `J_dark → 0`。定义（式 2）`J_dark(x) = min_{c∈{r,g,b}} ( min_{y∈Ω(x)} J^c(y) )`，Ω(x) 为以 x 为中心的局部区域。有雾时散射增强、对比度下降，暗通道值不再趋零，可近似度量雾的浓度。
        - **透射率估计（3.2.2，式 3）**：引入缓冲因子 `ω`（通常取 0.95）做校正：`t(x) = 1 − ω · min_{c} ( min_{y∈Ω(x)} I^c(y)/A^c )`。
        - **图像复原（3.2.3，式 4）**：为防 `t(x)` 过小导致 `J(x)` 过曝，设透射率下界 `t_0 = 0.1`（保留少量薄雾）：`J(x) = (I(x) − A) / max[t(x), t_0] + A`。该去雾算法同样可用于雨天图像，去除雨滴散射、增强对比度并保持原色。
    2.  **KCS-YOLO 模型（基于 YOLOv5n 改进，3.3 节及后续）**：
        - **K-means++ 聚类**：替代普通 K-means 对标注边界框尺寸聚类，生成更适配本数据集交通灯尺寸分布的锚框，改善初始定位。（聚类簇数 K 等具体取值在提取缓存覆盖范围内未给出。）
        - **CBAM 注意力机制**：轻量通用模块，依次在通道维度与空间维度做注意力——先学习各通道重要性（通道注意力），再学习关键空间位置（空间注意力），引导网络关注交通灯特征、抑制背景。（CBAM 在网络中的具体嵌入位置在提取缓存覆盖范围内未给出。）
        - **小目标检测层**：在 YOLOv5n 原检测头基础上新增一层面向小目标的检测层（通常对应更大特征图、保留更多细节），提升远距离小尺寸交通灯的召回。（新增层的具体尺度/通道在提取缓存覆盖范围内未给出。）
- **YOLO 评价指标定义（3.3 节，式 5–11）**：P = TP/(TP+FP)（式 5）；R = TP/(TP+FN)（式 6）；AP = ∫₀¹ P·R dR（式 7）；mAP = (1/N)·Σ AP_i（式 8）；F1 = 2PR/(P+R)（式 9）；FLOPs = 2HW(C_in K² − 1)C_out（式 10）；Params = C_in C_out K²（式 11）。
- **数据集划分**：训练/验证/测试 = **80% / 10% / 10%**。具体训练超参数（学习率、优化器、epoch、输入分辨率等）在提取缓存覆盖范围内未明确。
- **与已有方法的差异**：相较直接套用 YOLOv5n 或其他 YOLO 变体，本方法在四个维度做针对性改造——锚框匹配（K-means++）、特征质量（CBAM）、小目标（专用检测层）、输入图像质量（模型外的去雾预处理），构成完整流水线，且专门面向"低能见度 + 小目标"双重难点（这正是 Mao [13]、Appiah [14] 等前作各自只覆盖其一的不足）。

## 实验

- **使用的数据集**：作者自建的低能见度交通灯数据集，**共 3053 个样本**。覆盖不同时间段、雨天条件，以及红/黄/绿不同强度灯光，对应直行、左转、右转等运行场景。经翻转、平移、旋转、裁剪、缩放、加噪、随机遮挡等增强提升多样性，用 **LabelImg** 标注，仅含交通灯颜色标签四类（red / yellow / green / off）。划分为 80%/10%/10%。
- **对比方法**：基线 **YOLOv5n** 及其变体；经典两阶段检测器 **Faster-RCNN**。（相关工作中还提及 YOLOv3、YOLOv7、ESRGAN 等作为背景，非本文对比实验对象。）
- **评价指标**：AP、mAP、Params/M、F1、FLOPs/G，以及精确率 P、召回率 R（式 5–11 定义）。
- **主实验结果**：**KCS-YOLO 的 mAP 达 0.9887（98.87%），比 YOLOv5n 提升 5.03 个百分点**；据原文后续页，Faster-RCNN 的 mAP 仅 0.2431（提取缓存未覆盖，待核）。论文结论称 KCS-YOLO 在 AP、mAP 与 F1 上综合表现最优，且 Params 与 FLOPs 仍具可比性（即在精度大幅提升的同时未显著牺牲效率）。
- **消融实验**：论文摘要与引言明确进行了消融实验（验证 K-means++、CBAM、小目标层各自贡献），但**消融结果表格落在提取缓存未覆盖的页（约 p.7 起及 Table 3 区域），本笔记无法据提取文本列出各组件单独增益**。
- **基准/对比实验**：据原文后续页，Table 4 给出三种算法（KCS-YOLO / YOLOv5n / Faster-RCNN）在四种灯色（Red/Green/Yellow/Off）上的 AP 与综合指标，结论与 Table 3 高度一致；KCS-YOLO 综合最优（据原文 p.13，提取缓存未覆盖，待核）。
- **泛化实验**：提取缓存覆盖范围内未见在其它公开数据集/场景上的泛化测试。
- **效率信息**：表 1 在背景对比中给出各 YOLO 算法的 Params 与 FLOPs，但 **KCS-YOLO 自身的 Params/FLOPs/推理速度的具体数值落在提取缓存未覆盖页**，本笔记无法据提取文本给出；结论仅定性称其与对照模型 Params/FLOPs"可比"。

## 局限

1.  **数据集规模与场景偏窄**：仅 3053 个样本且专注低能见度，算法在常态（好天气）及更复杂灯光干扰场景下的泛化能力未做验证。数据集为自建、未公开（仅声明 Data Availability，据 p.14，提取缓存未覆盖），复现门槛高。
2.  **去雾预处理的计算开销**：暗通道先验去雾是模型外的额外步骤，会增加流水线延迟与算力成本，对自动驾驶实时性可能不利；论文未量化该步骤耗时。
3.  **关键实验数据落在缓存未覆盖页**：消融实验逐项增益、KCS-YOLO 自身 Params/FLOPs/推理速度、Table 3/4 完整数值均在提取缓存（前 25000 字符，约前 6 页）之外，无法据提取文本核验，对方法有效性的独立判断受限。
4.  **去雾假设依赖**：去雾效果依赖暗通道先验，在极端或不符合该先验（如大面积天空/亮背景）的场景下可能失效；t_0=0.1 仅是经验下界。
5.  **复现风险**：训练超参数、网络改造的具体配置（CBAM 插入位置、新增检测层尺度、K-means++ 簇数）在提取缓存覆盖范围内缺失，精确复现需查阅原文后续页或源码。

## 个人评论

1.  **"四点改造 + 去雾流水线"的系统工程思路清晰**：论文路径为"基准选型（YOLOv5n）→ 多模块针对性集成（K-means++ 锚框 / CBAM 特征 / 小目标层）→ 输入侧去雾增强"，每一步都对应低能见度小目标检测的一个具体瓶颈，工程上可借鉴、可拆解。
2.  **把领域去雾与通用检测器解耦是合理工程取舍**：去雾放在模型外作为独立预处理，便于替换与单独评估，但也带来串行延迟——这与自动驾驶实时性存在张力，论文未给耗时数据是明显短板。
3.  **98.87% mAP 需谨慎看待**：数据集自建、四类目标、规模仅 3053，且与之对比的 Faster-RCNN mAP 仅 0.2431（差距异常大），更像是数据集相对简单/同分布所致，而非方法相对其他强检测器的绝对优势；跨数据集泛化未验证，宜把该数字理解为"本数据集上的相对提升"而非通用 SOTA。
4.  **可迁移价值**：CBAM + 小目标检测层 + 先验锚框聚类的组合，以及"恶劣环境用领域预处理提升输入质量"的思路，可迁移到其它小目标/恶劣天气视觉任务（车牌、路标、远距离行人等）。

### 使用建议

- **快速了解**：读摘要 + 第 5 节结论即可掌握核心思想（KCS 三改进 + 去雾）与主结果（98.87% mAP，+5.03%）。
- **复现**：精读第 3 节"Traffic Light Dataset and Proposed KCS-YOLO Algorithm"——3.1 数据集生成、3.2 去雾（式 1–4）、3.3 起的网络改造与指标定义（式 5–11）；CBAM 嵌入位置、小目标层尺度、K-means++ 簇数、训练超参需查原文后续页或作者源码。
- **借鉴创新点**：学习"通用检测器 + 领域预处理（去雾）+ 小目标专用层 + 注意力"的组合范式，可迁移到其它恶劣环境/小目标检测任务。
- **写 related work**：归入"基于 YOLO 改进的交通信号/小目标检测"或"自动驾驶恶劣天气感知"类，与 Mao [13]（YOLOv7+注意力+SIOU）、Appiah [14]（YOLOv7+ESRGAN）并列，KCS-YOLO 的卖点是同时覆盖"低能见度去雾 + 小目标"两难点。

## 相关论文与链接

> - [[C2_目标检测_违建_车辆_船舶_行人]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
计算机视觉**目标检测**方向，落在**自动驾驶感知**的应用子域——**低能见度（雾/雨/夜间模糊）条件下的交通灯检测与识别**，本质是"恶劣天气 + 远距离小目标"双约束下的检测器改进。主题归类：`C2_目标检测_违建_车辆_船舶_行人`（交通场景应用型目标检测）。发表于 MDPI *Machines* 2024, 12(8), 557（DOI: 10.3390/machines12080557）。

## 2. 一句话总结
本文提出 KCS-YOLO：在 YOLOv5n 上用 K-means++ 重聚类锚框、嵌入 CBAM 注意力、新增小目标检测层，并在模型外用暗通道先验去雾预处理低能见度图像，使自建交通灯数据集上的 mAP 达 98.87%（较 YOLOv5n +5.03%）。

## 3. 背景与问题
- **为什么要做**：交通灯检测关乎自动驾驶安全，而低能见度（论文定义为能见度 < 300 m）是事故主因之一。论文把能见度归因于两点：光照差异（照度与能见度成正比）和大气透明度（雨雪雾沙尘使大气浑浊、透明度降低）。远距离交通灯目标小、与背景对比度低，更难检测。
- **之前方法的问题**：传统颜色特征+机器学习精度低、漏检误检；深度学习方法各有短板——Tian & Kim（暗通道+Faster-RCNN）实时性不足；YOLOv3 系（Possatti 先验地图、Du 多特征融合）精度仍低；Mao（YOLOv7+注意力+SIOU）未顾及复杂天气；Appiah & Mensah（YOLOv7+ESRGAN）顾天气未顾小目标；Li（改进 YOLOv4）早于 YOLOv5 系精度欠佳。
- **核心矛盾**：低能见度复杂天气下，如何兼顾远距离小目标的高精度与算法实用性。论文目标是"低能见度去雾 + 小目标增强"一起解决。

## 4. 核心贡献
1.  **基准选型**：对比多版本 YOLO（表 1：AP/mAP/Params/F1/FLOPs），确定 YOLOv5n"少参数、高 mAP"为基线。
2.  **KCS-YOLO 三改进**：K-means++ 锚框聚类（K）+ CBAM 注意力（C）+ 小目标检测层（S）。
3.  **自建数据集 + 去雾预处理**：3053 个低能见度交通灯样本，暗通道先验去雾增强输入。
4.  **对比 + 消融验证**：vs YOLOv5n/变体/Faster-RCNN，mAP 98.87%、较 YOLOv5n +5.03%。

## 5. 方法详解
- **两阶段流水线**：原始 RGB 图像 → 暗通道先验去雾预处理 → KCS-YOLO 检测 → 输出边界框 + 四类颜色（red/yellow/green/off）。
- **去雾（3.2，式 1–4）**：
    - 成像模型（式 1）`I(x)=J(x)t(x)+A(1−t(x))`，求无雾 `J(x)` 关键在估计透射率 `t(x)` 与大气光 `A`。
    - 暗通道（式 2，He et al.[17]）`J_dark(x)=min_c min_{y∈Ω(x)} J^c(y)`，非天空区某通道强度趋零；有雾时暗通道值升高，可度量雾浓度。
    - 透射率（式 3）`t(x)=1−ω·min_c min_{y∈Ω(x)} I^c(y)/A^c`，缓冲因子 ω≈0.95。
    - 复原（式 4）`J(x)=(I(x)−A)/max[t(x),t_0]+A`，下界 t_0=0.1 防过曝、留薄雾；该法亦可去雨滴散射、保原色。
- **网络改造（基于 YOLOv5n）**：
    - **K-means++**：对标注边界框尺寸聚类，得贴合数据集的先验锚框。
    - **CBAM**：通道注意力→空间注意力，聚焦交通灯特征、抑背景。
    - **小目标检测层**：在原检测头外新增一层提升远距小目标召回。
    - 三者具体配置（锚框簇数、CBAM 插入位置、新增层尺度）落在提取缓存未覆盖页，本笔记不臆测。
- **指标定义（3.3，式 5–11）**：P、R、AP=∫₀¹P·R dR、mAP=(1/N)ΣAP_i、F1=2PR/(P+R)、FLOPs=2HW(C_in K²−1)C_out、Params=C_in C_out K²。
- **数据划分**：80%/10%/10%。训练超参数提取缓存内未给出。

## 6. 实验与结果
- **数据集**：自建 3053 样本，覆盖多时段/雨天/三色灯/直行左右转，LabelImg 标注四类（red/yellow/green/off），含翻转/旋转/加噪/随机遮挡等增强。
- **对比方法**：YOLOv5n（基线）及其变体、Faster-RCNN。
- **指标**：AP、mAP、Params/M、F1、FLOPs/G、P、R。
- **主结果**：KCS-YOLO mAP = 0.9887（98.87%），较 YOLOv5n +5.03 个百分点；据原文后续页 Faster-RCNN mAP 仅 0.2431（提取缓存未覆盖，待核）。结论称其 AP/mAP/F1 综合最优且 Params/FLOPs 可比。
- **消融实验**：论文明确做了消融（拆 K-means++/CBAM/小目标层），但结果表落在提取缓存未覆盖页，本笔记无法据提取文本列出逐项增益。
- **Table 4 基准实验**：据原文 p.13，给出三算法在四色灯上的 AP，与 Table 3 一致，KCS-YOLO 综合最优（提取缓存未覆盖，待核）。
- **效率/泛化**：KCS-YOLO 自身 Params/FLOPs/速度具体值、跨数据集泛化均在提取缓存覆盖范围外或未提及。

## 7. 这篇论文真正有价值的地方
1.  **针对"低能见度 + 小目标"双难点的完整流水线**：把领域去雾（暗通道先验）与通用检测器改进（K/C/S）拼成端到端方案，正好补上前作各自只覆盖其一的缺口。
2.  **改进点与瓶颈一一对应、可拆解迁移**：锚框（K-means++）、特征（CBAM）、小目标（专用层）、输入质量（去雾）四个改造各打一个痛点，方法论上干净，组件可迁移到其它恶劣天气/小目标任务。
3.  **指标体系完整**：同时报告 AP/mAP/F1 与 Params/FLOPs，兼顾精度与效率口径（尽管 KCS-YOLO 自身效率数值落在缓存外）。

## 8. 局限与问题
1.  **数据集小且自建未公开**：3053 样本、专注低能见度，常态天气与跨场景泛化未验证；数据集复现门槛高。
2.  **去雾串行开销未量化**：模型外去雾增加延迟，与自动驾驶实时性冲突，论文未给耗时。
3.  **关键数据落在缓存未覆盖页**：消融逐项增益、KCS-YOLO 自身 Params/FLOPs/速度、Table 3/4 完整数值无法据提取文本核验。
4.  **98.87% vs Faster-RCNN 0.2431 差距异常大**：更可能反映数据集相对简单/同分布，而非方法的绝对通用优势，宜按"本数据集上相对提升"理解。
5.  **去雾假设依赖**：暗通道先验在大面积天空/亮背景等不符场景可能失效。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 第 5 节结论。
- **复现**：精读第 3 节（3.1 数据集、3.2 去雾式 1–4、3.3 网络改造与指标式 5–11）；CBAM 位置、小目标层尺度、K-means++ 簇数、训练超参需查原文后续页/源码。
- **借鉴创新点**：复用"通用检测器 + 领域去雾预处理 + 小目标专用层 + CBAM"的组合范式。
- **写 related work**：归入"YOLO 改进的交通信号/小目标检测""自动驾驶恶劣天气感知"，与 Mao[13]、Appiah[14] 并列，卖点是同时覆盖去雾与小目标。

## 10. 和其他论文的关系
- **YOLOv7 + 注意力/损失改进**：Mao et al. [13]（注意力 + SIOU 损失）。
- **检测 + 超分增强应对天气**：Appiah & Mensah [14]（YOLOv7 + ESRGAN）。
- **暗通道先验源头**：He et al. [17]（dark channel prior 去雾）。
- **早期 YOLO 系交通灯检测**：Possatti [8]、Du [9]（YOLOv3）、Li [12]（YOLOv5 小目标）、Li [15]（YOLOv4 多传感器）。
- [[KCS-YOLO]] 本质是 [[YOLOv5n]] 的领域改进变体；完整参考文献的双链关系受提取范围所限未尽列。

## 11. 关键词
- 目标检测 / 交通灯检测与识别
- 低能见度（能见度 < 300 m）
- YOLOv5n / KCS-YOLO
- CBAM 注意力机制
- K-means++ 锚框聚类
- 小目标检测层
- 暗通道先验去雾（dark channel prior）
- 自动驾驶感知

## 12. 可信度说明
本精读基于 **PDF 提取缓存（前 25000 字符，约覆盖论文前 6 页正文 + 摘要/引言/相关工作/3.1–3.3 去雾与指标定义）** 生成；缓存 header 标注 `pages_extracted: 12/15`，但因 25000 字符截断，实际可读正文约止于式 11（第 6 页）。
- **可据提取文本核实**：标题/作者/单位/DOI/期刊卷号、摘要全文与关键词、能见度定义与两因素、相关工作脉络、数据集（3053 样本/四类/80-10-10/LabelImg/增强）、去雾式 1–4 与 ω=0.95/t_0=0.1、YOLO 指标式 5–11、mAP 98.87%、+5.03%、对比对象（YOLOv5n/变体/Faster-RCNN）。
- **据原文后续页、提取缓存未覆盖、待核**：Faster-RCNN mAP 0.2431、Table 3/4 逐项 AP、消融逐组件增益、KCS-YOLO 自身 Params/FLOPs/推理速度、第 5 节结论原文、Data Availability（p.13–15）。这些来自原笔记"全文补读记录"中对 p.13–15 的摘录，本次保留并明确标注未经提取缓存独立核验。
- **提取质量**：总体清晰（约 2086 字符/页），少量乱码（如"tra ﬃc light""o ﬀ"连字符/合字断裂）已据上下文修正；摘要乱码已用提取文本重建为干净英文 + 中文。

---

> **可信度补充**: PDF 提取质量 = **medium**（提取清晰但因 25000 字符上限截断, 实际仅覆盖约前 6 页正文; 后续页关键实验数据未进缓存, 部分声明依赖原笔记 p.13–15 摘录待核）; 来源缓存: `.paper-cache/extracts/machines-12-00557.txt` (header 标注 12/15 页, 实读约 6 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Machines 2024 ,12, 557 13 of 15
- p.13: Table 4 lists the performance measures for all the three algorithms derived from the
- p.13: Figure 9 and Table 4 discloses the following facts: (1) even though KCS-YOLO performs
- p.13: AlgorithmsAP
- p.13: Red Green Yellow Off Red Green Yellow Off
- p.13: The associated research findings reported in the literature may well explain the second
- p.13: 5. Conclusions
- p.13: In low visibility conditions, traffic light detection and recognition becomes more
- p.13: Experimental results demonstrate that compared with YOLOv5n and its variants,
- p.13: KCS-YOLO exhibits the best overall performance in AP , mAP and F1 with the comparable
- p.14: Machines 2024 ,12, 557 14 of 15
- p.14: Data Availability Statement: The original contributions presented in the study are included in the

### 缺失页关键摘录

- p.13: Table 4 lists the performance measures for all the three algorithms derived from the
- p.13: benchmark experiments. KCS-YOLO achieves the mAP value of 0.9887, an increase of 5.03%
- p.13: of 0.2431 for Faster-RCNN. The results shown in Table 4 achieve excellent agreement with
- p.13: those listed in Table 3. It is demonstrated that KCS-YOLO exhibits superior performance
- p.13: Figure 9 and Table 4 discloses the following facts: (1) even though KCS-YOLO performs
- p.13: Table 4. The results of benchmark experiments.
- p.13: data augmentation techniques, which prevents it from achieving high accuracy under low
- p.13: challenging. To improve the traffic light detection accuracy, this paper proposes and
- p.13: image dataset generated with the dark channel prior dehazing algorithm to eliminate
- p.13: KCS-YOLO exhibits the best overall performance in AP , mAP and F1 with the comparable
- p.13: measures of Params and FLOPs. In particular, KCS-YOLO achieves the mAP value of
- p.13: low-speed mobile robot. The trade-off between the accuracy and computational efficiency
<!-- AI_READING_NOTE_END -->
