---
title: YMMNet_A_More_Accurate_and_Lightweight_Detector_of_Illegal_Buildings_for_Smart_Cities
authors:
  - "Wenjin Liu"
  - "Shudong Zhang"
  - "Lijuan Zhou"
  - "Ning Luo"
  - "Min Xu"
year: 2024
venue: "IEEE Transactions on Consumer Electronics"
doi: 10.1109/TCE.2024.3415673
pdf: [[YMMNet_A_More_Accurate_and_Lightweight_Detector_of_Illegal_Buildings_for_Smart_Cities.pdf]]
primary_topic: C2_目标检测_违建_车辆_船舶_行人
topics:
  - "C2_目标检测_违建_车辆_船舶_行人"
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
extract_cache: .paper-cache/extracts/YMMNet_A_More_Accurate_and_Lightweight_Detector_of_Illegal_Buildings_for_Smart_Cities.txt
---

# YMMNet_A_More_Accurate_and_Lightweight_Detector_of_Illegal_Buildings_for_Smart_Cities

## 基本信息
- **PDF**: [[YMMNet_A_More_Accurate_and_Lightweight_Detector_of_Illegal_Buildings_for_Smart_Cities.pdf]]
- **primary_topic**: `C2_目标检测_违建_车辆_船舶_行人`
- **topics**: `C2_目标检测_违建_车辆_船舶_行人`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-05

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | YMMNet: A More Accurate and Lightweight Detector of Illegal Buildings for Smart Cities |
| **作者** | Wenjin Liu; Shudong Zhang; Lijuan Zhou; Ning Luo; Min Xu (海南大学网络空间安全学院; Min Xu 为首都师范大学信息工程学院) |
| **发表时间** | 2024 (在线发表 2024-06-18; 当期 2024-12-11) |
| **刊物/会议** | IEEE Transactions on Consumer Electronics, Vol. 70, No. 3 |
| **DOI** | 10.1109/TCE.2024.3415673 |
| **代码** | https://github.com/QvQKing/YMMNet.git |

## 摘要

**清理后的英文原摘要**（据 PDF 提取文本整理，修复空格断裂、剔除杂入字符）：

> Illegal construction not only seriously affects economic consumption and urban infrastructure (including monitoring equipment, 5G infrastructure, 6G devices, and other consumer electronics) but also hinders the development of smart cities. However, current illegal building detection methods have low detection accuracy and high calculation costs. Therefore, a method for detecting illegal building activities by identifying illegal building-related objects is proposed. A lightweight and high-precision detector and a dataset including 14,038 images of 29 categories of illegal building objects are proposed. The proposed detector is an enhanced version of YOLOv4. MobileNetV3 is utilized as the backbone to extract features, which greatly improves the detection accuracy. Further, depthwise separable convolution (DSC) is introduced to optimize the model structure and lower calculation costs and parameters. Furthermore, Mish was utilized to enhance the identification precision, generalization, and robustness of the detector. Experimental results revealed that the mean average precision (mAP) value of the detector is 88.79% with the dataset. Compared to other state-of-the-art (SOTA) detectors, this detector exhibited superior performance in identifying illegal construction objects, which can detect and prevent illegal building activities accurately and timely, enhancing the development of smart cities. Our project is released at https://github.com/QvQKing/YMMNet.git.

**中文翻译**：

> 违法建设不仅严重影响经济消费和城市基础设施（包括监控设备、5G 基础设施、6G 设备及其他消费电子产品），还阻碍智慧城市的发展。然而，当前的违建检测方法检测精度低、计算成本高。为此，本文提出一种通过识别"违建相关物体"来检测违建活动的方法，并提出了一个轻量化、高精度检测器以及一个包含 14,038 张图像、涵盖 29 类违建物体的数据集。该检测器是 YOLOv4 的增强版本：采用 MobileNetV3 作为主干提取特征以大幅提升检测精度；引入深度可分离卷积（DSC）优化模型结构、降低计算成本与参数量；进一步使用 Mish 激活函数增强检测器的识别精度、泛化性和鲁棒性。实验结果表明该检测器在数据集上的平均精度均值（mAP）为 88.79%。与其他 SOTA 检测器相比，该检测器在识别违建物体方面表现更优，能够准确、及时地检测和预防违建活动，助力智慧城市发展。项目已开源于 https://github.com/QvQKing/YMMNet.git。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

*   **为什么要做**：违法建设阻碍经济发展和公共设施建设，引发法律与领土争议（[1]），甚至可能诱发潜在的犯罪活动（[2]），并危害消费电子类基础设施（监控设备、5G/6G 设施）。需要一种能够及时、低成本发现违建活动的方法以支撑智慧城市建设。
*   **之前方法的问题**（按论文 Related Work 三类梳理）：
    1.  **早期方法（人工/GIS/遥感）**：依赖人工采集建筑数据、更新地理数据库并与历史数据比对（如 Felice 两步勘测排名、Awrangjeb 的 GUI 建库、Zhu & Fan 借助 HPC 比对城市规划图、Yang 等结合 GPS+遥感+GIS）。受疲劳、恶劣天气等影响，效率低、易出错，人力成本高、检测周期长。
    2.  **传统图像处理 / 机器学习方法**：如改进 HOG-LBP、RGB→CIELUV + Otsu 阈值、多尺度滤波点划分 + 聚类生长、K-means 聚类识别像素变化与建筑轮廓等。多基于卫星图像，减少了人工干预与时间成本，但识别精度仍是显著瓶颈。
    3.  **现有深度学习方法**（Faster R-CNN、SSD、RetinaNet、YOLO 系列等）：精度有所提升但仍不令人满意，主要问题为：a) 检测精度仍不理想、计算成本高；b) **只能在违建建成后才检测，无法实现早期发现**；c) 多依赖遥感（检测周期长、实时性差）和无人机（城市内有安全隐患与隐私问题）；d) 现有违建数据集多局限于特定地区/国家，缺乏通用性，且缺少综合性数据集。
*   **核心矛盾**：需要一种能在违建**尚未完成时**就预警（通过检测施工相关物体，即"未完工的违建"）、**高精度**、且**轻量化**以适配城市区域实时部署的检测方法。

## 关键贡献

1.  **提出基于改进目标检测器的违建物体检测方法**：通过检测"疑似违建相关物体"来及时预防和发现违建活动，实现从"事后检测"到"早期发现未完工违建"的转变。
2.  **提出高精度轻量级检测器 YMMNet**：基于 YOLOv4，用 MobileNetV3 作主干、在主干外的颈部与头部把普通卷积替换为 DSC、并在主干外使用 Mish 激活，**显著降低计算成本与参数量并提升精度**。
3.  **构建了违建物体数据集**：包含 14,038 张图像、29 类违建相关物体，采集自多种真实场景、季节、天气、时段和光照条件，填补该领域专用数据集空白。
4.  **大量实验验证**：在该数据集上验证 YMMNet 的有效性，并测试多个流行 SOTA 检测器、构建了一个基准（benchmark）。

## 方法

*   **整体框架**（图1）：YMMNet 是单阶段检测器，沿用 YOLOv4 的"主干—颈部（SPP+PANet）—YOLO Head"结构，核心改动是把主干 CSPDarkNet53 换成更轻的 MobileNetV3，并对主干外的卷积与激活函数做轻量化/精度优化。
*   **输入输出**：原始 HD 相机图像为 `1080 x 1920` 像素，切割为多个 `416 x 416` 像素图像块用于训练/推理；输出为违建物体的边界框、类别与置信度。
*   **关键模块**：
    1.  **YOLOv4 基线**：主干 CSPDarkNet53（用 CSP 结构降算力、提速），输出 `13×13`、`26×26`、`52×52` 三个有效特征层；`13×13` 层进 SPP（含 `5×5`/`7×7`/`9×9` 三个最大池化），融合局部与全局特征并缓解尺度差异；SPP 输出与另两层一起进 PANet 做卷积、上/下采样与特征融合；最后三个增强特征层送入 YOLO Head 做分类与回归。
    2.  **主干 MobileNetV3（表I, 图2）**：融合 MobileNetV1 的 DSC、MobileNetV2 的线性瓶颈倒残差结构、以及基于 MnasNet 的 SE（squeeze-and-excitation）注意力。核心是 Bneck 块：先 `1×1` 卷积升维 → `3×3` 深度卷积提特征 → 全局平均池化 + 两层 FC + 两个非线性激活构成的 SE 模块做通道加权 → `1×1` 卷积调整通道用于 shortcut；shortcut 仅在 stride=1 且输入输出通道数相同时存在。用 **H-Swish 替代 ReLU6** 缓解信息损失严重的问题（公式 (1)(2)：`ReLU6[x]=min(max(x,0),6)`，`H-Swish[x]=x·ReLU6(x+3)/6`）。取 MobileNetV3 最后三层（高层语义丰富）送入 SPP/PANet：最精细的最终特征层接 SPP，其余两层用于 PANet。相比 CSPDarkNet53，MobileNetV3 因线性瓶颈倒残差、注意力与 DSC 能学到更具表达力的特征，同时显著降低参数量与算力。
    3.  **DSC 轻量化（图3, 公式(3)-(7)）**：把**主干外**颈部与头部中的 `3×3` 标准卷积改为深度可分离卷积，在 SPP 与 PANet 内以更少参数完成卷积/上下采样/特征融合。DSC 分两步：深度卷积（每通道独立卷积核提特征）+ 逐点卷积（`1×1` 卷积融合通道）。论文给出标准卷积算力 `S1 = GK·GK·M·N·GF·GF`、DSC 算力 `S2 = GK·GK·M·GF·GF + M·N·GF·GF`，二者之比 `S2/S1 = 1/N + 1/GK²`（GK 为核空间尺寸，M/N 为输入/输出通道数，GF 为输入特征图宽高），从而大幅降参降算。
    4.  **Mish 激活（公式(8)(9), 图4）**：YOLOv4 在主干外用 LeakyReLU（公式 (8)：`x≥0` 取 `x`，`x<0` 取 `ax`），其在不同区间表现不一致、难以稳定预测正负输入关系。YMMNet 在主干外改用 Mish（非单调、平滑、计算开销低，优于 ReLU/Swish）。论文公式 (9) 写作 `Mish = x·tanh(1+e^x)`（注：Mish 的规范定义应为 `x·tanh(ln(1+e^x))`，提取文本中 `ln` 疑似在版式中丢失，待核原文）。
*   **应用流程（图5, E 节）**：通过在多个区域部署高清摄像头采集图像，输入 YMMNet 实时推理，检测违建相关物体以及时发现并预防违建活动，同时降低人力与计算成本、提升检测精度与效率。
*   **训练方式**：PDF 提取文本（截止到 Section IV 数据集部分）**未给出**具体损失函数、优化器、学习率等训练细节；仅说明数据集被随机划分为三个子集（提取文本在"random"处截断，子集名称与比例据原文后续页，提取缓存未覆盖，待核）。
*   **与已有方法差异**：① 任务目标——检测"违建相关物体/未完工违建"以早期预警，而非检测已建成建筑；② 模型设计——在 YOLOv4 上换主干（MobileNetV3）、主干外卷积换 DSC、主干外激活换 Mish，平衡轻量化与精度；③ 应用场景——用地面高清摄像头做城市实时监控，避开遥感的实时性差与无人机的安全/隐私问题。

## 实验

*   **数据集**：自建违建物体数据集，14,038 张 `416×416` 图像，**29 类**违建物体。采集自中国**河北省**多个区域，用高清摄像头（型号 **DS-2TD6236-75C2L**）持续拍摄**两年以上**；覆盖城市/野外农田/郊区等场景，春夏秋冬四季，雨/雪/雾等天气，夜/晨/午等时段及明暗不同光照。标注用 **LabelImg** 人工完成，整理为类 **Pascal VOC** 格式；数据随机划分为三个子集。
*   **评价指标**：核心为平均精度均值 **mAP**。
*   **主结果**：YMMNet 在该数据集上 mAP = **88.79%**（见摘要），优于其他 SOTA 检测器。
*   **对比方法 / 消融 / 效率数值**：论文称测试了"多个流行 SOTA 检测器"并构建基准、做了消融验证各模块作用，但**提取缓存只覆盖到第 8 页（Section IV 数据集），未包含 Section V 实验**，因此具体对比检测器列表、消融数据表、参数量/FLOPs/FPS 等数值**提取文本未覆盖（据原文 Section V，待核）**。原始 PDF 共 50874 字符，提取仅取前 25000 字符。
*   **泛化实验**：提取文本未涉及（同上，待核 Section V）。

## 局限

1.  **数据集地域局限**：仅采自中国河北省，可能无法代表不同地区建筑风格与法规下的违建特征，存在域偏移风险。
2.  **"违法"判定的语义鸿沟**：检测到脚手架、建材等只说明存在施工活动，并不等于"违法"。模型本身无法区分合法/违法施工，论文未讨论如何结合城市规划规则做最终判定，潜在误报较多。
3.  **轻量化与精度权衡未充分剖析**：大量使用 DSC 通常会牺牲一定精度（尤其小目标/遮挡目标），论文（就提取部分而言）未分尺度分析检测性能；具体精度-效率折中数据在未覆盖的 Section V。
4.  **实时性/边缘部署验证缺口**：强调"及时检测"，但提取文本未提供在真实边缘设备上的 FPS/时延数据，实时部署能力的硬证据待核 Section V。
5.  **对采集条件的假设**：输入为固定 `416×416` 图像块且依赖高清摄像头，未讨论不同分辨率、视角、复杂背景下的鲁棒性。

## 个人评论

1.  **问题切入点新颖**："以物及事"——检测脚手架、建材等施工相关物体来对违建做**早期预警**（捕捉未完工违建），比检测已建成建筑更贴合城市管理"早发现、早制止"的实际需求。
2.  **务实的轻量化组合拳**：把成熟轻量化技术（MobileNetV3 主干、主干外 DSC）系统接入强检测框架（YOLOv4），并在激活函数上做针对性替换（主干内 H-Swish、主干外 Mish），在特定任务上追求精度-效率平衡。这套"换主干 + 换卷积 + 换激活"的改造范式对其他边缘检测任务有借鉴价值。
3.  **数据集贡献明确**：构建并开源大规模、多条件真实场景违建物体数据集（含 GitHub 链接），为该细分方向提供公共资源。
4.  **面向落地**：覆盖从数据采集（HD 摄像头）、模型设计（轻量化）到应用流程（实时预警）的完整链路，对智慧城市具体落地有直接参考意义。
5.  **保留判断**：这是发表在 IEEE TCE 的工程导向工作，方法上属"已有轻量化模块的组合应用"而非全新算法；其精度优势与"轻量"声明的硬数值（参数量/FLOPs/FPS、消融）落在提取未覆盖的实验章节，复核时应优先核对 Section V 的对比表与消融表。

### 使用建议

*   **快速了解**：读摘要、引言与（原文）实验结论即可把握问题、方法与贡献。
*   **复现**：重点看方法部分（Section III），结合图1（整体架构）、图2（Bneck）、图3（DSC 分解）和表I（MobileNetV3 结构），并参考开源代码复现数据集构建与训练流程。
*   **借鉴创新点**：① 学其"换主干 + 主干外换 DSC + 主干外换 Mish"的轻量化组合范式；② 借鉴"以物及事"的早期预警思路（检测关联物体/状态以预测复杂活动）；③ 参考其多条件数据采集与 LabelImg + Pascal VOC 格式的标注流程。
*   **写 related work**：可放入"基于深度学习的违建/建筑检测"或"轻量化目标检测网络"两个小节。

## 相关论文与链接

> - [[C2_目标检测_违建_车辆_船舶_行人]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的**目标检测应用**，具体是**面向智慧城市的违法建筑（违建）物体检测**。它发表于 IEEE Transactions on Consumer Electronics (Vol. 70, No. 3, 2024)，工程与落地导向明显。区别于遥感卫星/无人机的建成建筑提取，本文用**地面高清摄像头**采集近地面图像，检测与施工活动相关的物体（建材、脚手架等）以实现违建的**早期预警**。因此其最贴切的库内主题是 `C2_目标检测_违建_车辆_船舶_行人`（"违建"检测），而非遥感建筑检测——论文恰恰是为了规避遥感的实时性与无人机的隐私/安全问题。

## 2. 一句话总结
本文在 YOLOv4 上以 MobileNetV3 换主干、主干外用 DSC 降参、主干外用 Mish 提精度，得到轻量高精的违建物体检测器 YMMNet，并构建了 14,038 张、29 类的违建物体数据集，在该数据集上达到 88.79% mAP。

## 3. 背景与问题
*   **动机**：违建阻碍经济与公共设施建设、引发法律/领土争议乃至潜在犯罪，并危及监控设备、5G/6G 等消费电子基础设施，阻碍智慧城市发展。
*   **既有方法三类短板**：① 早期人工/GIS/遥感法——人力与周期成本高、易受疲劳与天气影响出错；② 传统图像处理/机器学习（HOG-LBP、Otsu、K-means 聚类等，多基于卫星图）——减少人工但精度仍是瓶颈；③ 深度学习法（Faster R-CNN/SSD/RetinaNet/YOLO 系列）——精度仍不满意、算力高，且**只能在建成后检测**，多依赖实时性差的遥感或有安全/隐私隐患的无人机，数据集又地域局限。
*   **核心矛盾**：要在违建**未完工时**就早期发现，同时兼顾**高精度**与**轻量化**以适配城市实时部署。

## 4. 核心贡献
1.  提出基于改进检测器、通过识别"疑似违建相关物体"来及时预防/发现违建活动的方法（检测未完工违建，实现早期预警）。
2.  提出高精度轻量检测器 YMMNet（MobileNetV3 主干 + 主干外 DSC + 主干外 Mish），降算力降参并提升精度。
3.  构建并开源 14,038 张 / 29 类违建物体数据集（多场景、多季节、多天气、多光照）。
4.  在该数据集上做大量实验验证有效性，并测试多个 SOTA 检测器、构建基准。

## 5. 方法详解
*   **框架（图1）**：单阶段，沿用 YOLOv4 的主干—颈部(SPP+PANet)—YOLO Head，主要改三处：主干换 MobileNetV3、主干外卷积换 DSC、主干外激活换 Mish。
*   **输入输出**：`1080×1920` HD 图像切成 `416×416` 块；输出边界框 + 类别 + 置信度。
*   **YOLOv4 基线**：CSPDarkNet53 出 `13×13/26×26/52×52` 三层；`13×13` 进 SPP（`5×5/7×7/9×9` 最大池化）融合局部+全局特征并缓解尺度差异；SPP 输出与另两层进 PANet 做卷积/上下采样/特征融合；三增强层送 YOLO Head。
*   **主干 MobileNetV3（表I, 图2）**：DSC（来自 V1）+ 线性瓶颈倒残差（来自 V2）+ SE 注意力（基于 MnasNet）。Bneck：`1×1` 升维 → `3×3` 深度卷积 → SE（GAP + 2 FC + 2 非线性）通道加权 → `1×1` 调通道用于 shortcut（仅 stride=1 且输入输出通道相同时存在）；H-Swish 替 ReLU6 缓解信息损失。公式 (1)(2)：`ReLU6[x]=min(max(x,0),6)`，`H-Swish[x]=x·ReLU6(x+3)/6`。取最后三层送 SPP/PANet（最精细层接 SPP）。相比 CSPDarkNet53，特征更具表达力且更省参省算。
*   **DSC（图3, 公式(3)-(7)）**：主干外颈/头的 `3×3` 标准卷积改为深度卷积 + `1×1` 逐点卷积两步。算力比 `S2/S1 = 1/N + 1/GK²`（N 输出通道、GK 核尺寸），大幅降参降算。
*   **Mish（公式(8)(9), 图4）**：主干外把 LeakyReLU（`x≥0→x`，`x<0→ax`）换成 Mish（非单调、平滑、低开销，优于 ReLU/Swish），提升识别精度、泛化与鲁棒性。论文公式 (9) 写作 `Mish=x·tanh(1+e^x)`（规范式应为 `x·tanh(ln(1+e^x))`，疑提取丢 `ln`，待核）。
*   **应用（图5）**：多区域部署 HD 摄像头采集 → YMMNet 实时推理 → 检出违建物体并触发预警，降低人力与算力、提升精度效率。
*   **训练细节**：提取文本截至数据集章节，未给损失/优化器/学习率；仅提到随机划分为三子集（具体比例据原文后续页，提取缓存未覆盖，待核）。

## 6. 实验与结果
*   **数据集**：14,038 张 `416×416`、29 类违建物体；河北省采集，HD 相机 DS-2TD6236-75C2L，拍摄逾两年；多场景/季节/天气/时段/光照；LabelImg 标注、类 Pascal VOC 格式、随机三子集划分。
*   **指标 & 主结果**：核心指标 mAP；YMMNet 达 **88.79% mAP**（见摘要），优于其他 SOTA 检测器。
*   **对比/消融/效率**：论文声称做了 SOTA 对比、构建基准、并以消融验证各模块——但**提取缓存只到第 8 页（Section IV），Section V 实验未覆盖**，故具体对比检测器名单、消融数据表、参数量/FLOPs/FPS 等数值**待核原文 Section V**。
*   **泛化实验**：提取文本未涉及（待核 Section V）。

## 7. 这篇论文真正有价值的地方
1.  **"以物及事"的早期预警视角**：检测施工相关物体而非建成建筑，捕捉"未完工违建"，更契合城市管理早发现早制止的需求。
2.  **可复用的轻量化改造范式**："换主干（MobileNetV3）+ 主干外换 DSC + 主干外换 Mish"，对其他边缘检测任务有迁移价值。
3.  **数据集贡献**：大规模、多条件真实场景违建物体数据集并开源，填补细分领域空白。
4.  **端到端落地链路**：从 HD 采集、轻量建模到实时预警流程完整，规避遥感实时性差与无人机隐私/安全问题。

## 8. 局限与问题
1.  **地域局限**：仅采自河北省，存在域偏移风险。
2.  **"违法"语义鸿沟**：检出施工物体≠违法，模型无法判定合法/违法，易误报；论文未讨论如何接入规划规则。
3.  **精度-效率折中分析不足**：DSC 轻量化可能牺牲小目标/遮挡目标精度，分尺度分析与折中硬数据落在未覆盖的 Section V。
4.  **实时/边缘部署证据缺口**：提取部分未见真实设备 FPS/时延（待核 Section V）。
5.  **采集条件假设强**：固定 `416×416` 块、依赖 HD 摄像头，鲁棒性未讨论。

## 9. 我该怎么使用这篇论文
*   **快速了解**：读摘要、引言与（原文）实验结论。
*   **复现**：看 Section III + 图1/2/3、表I，结合开源代码（https://github.com/QvQKing/YMMNet.git）复现数据与训练。
*   **借鉴创新点**：学轻量化组合范式；借"以物及事"早期预警思路；参考多条件采集 + LabelImg/Pascal VOC 标注流程。
*   **写 related work**：归入"基于深度学习的违建/建筑检测"或"轻量化目标检测网络"。

## 10. 和其他论文的关系
*   **直接改进对象**：YOLOv4（[10]，one-stage 检测，精度/速度折中），与 [[YOLOv4]] 系列直接相关。
*   **主干来源**：MobileNetV3（融合 V1 的 DSC、V2 的线性瓶颈倒残差、MnasNet 的 SE），与 [[MobileNetV3]]/[[MobileNetV2]]/[[MobileNetV1]] 强相关。
*   **对比/背景方法**：Faster R-CNN [4]、SSD [5]、RetinaNet [6]、YOLO 系列 [7][8][9][10]；违建/建筑检测相关如 Audebert 等 [38]（全卷积像素级标注）、Li 等 [40]（改进 Faster R-CNN 处理小目标）、An & Guo [26]（3D 点云分割识别违建）、Liu 等 [42]（双时相无人机变化检测 + PIC 法）。
*   **基础组件**：SPP [43]、PANet [44]、CSP 结构 [45]。

## 11. 关键词
智慧城市, 违建检测, 轻量化目标检测, YOLOv4, MobileNetV3, 深度可分离卷积(DSC), Mish, H-Swish, SE 注意力, 数据集构建, 早期预警, 地面高清摄像头, IEEE TCE

## 12. 可信度说明
本笔记基于 PDF 提取文本生成。**关键事实修正**：本文发表于 **IEEE Transactions on Consumer Electronics (Vol. 70, No. 3, 2024)**（原笔记误记为 "Electronics"），DOI 为 10.1109/TCE.2024.3415673，作者单位为海南大学网络空间安全学院（Min Xu 为首都师范大学），相应将 primary_topic 由 `T_遥感_建筑检测` 改为更贴切的 `C2_目标检测_违建_车辆_船舶_行人`。**覆盖范围限制**：提取缓存标注 12/12 页但实际字符在 25000 处截断（原文 50874 字符），内容仅覆盖到 **Section IV 数据集**，**Section V 全部实验（SOTA 对比表、消融表、参数量/FLOPs/FPS 等）未被提取**，相关数值已逐处标注"待核 Section V"。摘要、方法（YOLOv4/MobileNetV3/DSC/Mish）、数据集采集与标注细节、88.79% mAP 均可从提取文本直接核实；训练子集比例、Mish 公式中疑缺的 `ln` 需对照原文复核。

---

> **可信度补充**: PDF 提取质量 = **medium** (提取文本于 25000 字符处截断, 仅覆盖至 Section IV 数据集, Section V 实验未纳入); 来源缓存: `.paper-cache/extracts/YMMNet_A_More_Accurate_and_Lightweight_Detector_of_Illegal_Buildings_for_Smart_Cities.txt` (标注 12/12 页, 实际正文截断); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 复核优化日期: 2026-06-18.
<!-- AI_READING_NOTE_END -->
