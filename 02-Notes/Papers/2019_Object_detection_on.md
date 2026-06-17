---
title: Object detection on aerial imagery using CenterNet
authors:
  - "DheerajReddyPailla"
  - "InternationalInstituteofInformationTechnology"
  - "Hyderabad"
  - "VargheseKollerathu"
  - "SiemensTechnologyandServicesPrivateLimited"
  - "Bengaluru"
  - "SaiSakethChennamsetty"
year: 2019
venue: "arXiv"
doi: 
pdf: [[2019_Object_detection_on.pdf]]
primary_topic: C_目标检测_通用与旋转框
topics:
  - "C_目标检测_通用与旋转框"
status: ai-read
reading_stage: ai-complete
confidence: high
source_basis: pdf-text
date_added: 2026-06-03
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2019_Object_detection_on.txt
---

# Object detection on aerial imagery using CenterNet

## 基本信息
- **PDF**: [[2019_Object_detection_on.pdf]]
- **primary_topic**: `C_目标检测_通用与旋转框`
- **topics**: `C_目标检测_通用与旋转框`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Object detection on aerial imagery using CenterNet |
| **作者** | Dheeraj Reddy Pailla (IIIT Hyderabad); Varghese Kollerathu (Siemens Technology and Services, Bengaluru); Sai Saketh Chennamsetty (Siemens Technology and Services, Bengaluru) |
| **发表时间** | 2019 (arXiv:1908.08244v1, 22 Aug 2019) |
| **刊物/会议** | arXiv (VisDrone2019 挑战赛技术报告) |
| **DOI** | 未明确 |

## 摘要

**英文原文（据 PDF 提取文本整理）**：

> Detection and classification of objects in aerial imagery have several applications like urban planning, crop surveillance, and traffic surveillance. However, due to the lower resolution of the objects and the effect of noise in aerial images, extracting distinguishing features for the objects is a challenge. We evaluate CenterNet, a state of the art method for real-time 2D object detection, on the VisDrone2019 dataset. We evaluate the performance of the model with different backbone networks in conjunction with varying resolutions during training and testing.

**中文翻译**：

> 航空图像中目标的检测与分类有诸多应用，如城市规划、作物监测和交通监控。然而，由于航空图像中目标分辨率较低且受噪声影响，提取目标的判别性特征是一个挑战。本文在 VisDrone2019 数据集上评估了 CenterNet——一种用于实时 2D 目标检测的先进方法。我们评估了在训练和测试中采用不同骨干网络、并配合不同分辨率时该模型的性能。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：航空（无人机）图像在城市规划、作物监测、交通监控等领域有重要应用，但其与常规图像（如 MSCOCO 数据集中常见物体在一般场景下拍摄的图像）有显著不同：存在异常的长宽比、不规则的视角、以及目标判别细节缺失。MSCOCO 中前景与背景通常分离良好、分辨率与质量高，而这些有助于识别的目标特性在无人机图像中缺失（Fig. 1）。此外无人机画面中目标尺寸小、且目标聚集密度高（p.1, Sec. 1）。
- **之前方法的问题**：基于 CNN 的检测器分为两阶段与一阶段两类。两阶段检测器（R-CNN/Fast R-CNN/Faster R-CNN）先用预训练 CNN 提特征，再用 RPN（预定义约 k=2000 个候选区域）判断区域是前景还是背景，泛化与性能好，但**推理时间长**（p.1-2, Sec. 2/2.1）。一阶段检测器（SSD、YOLOv3）用固定数量的密集候选框规避 RPN，但因候选框固定采样，**前景/背景样本严重不平衡**；RetinaNet 用 focal loss 缓解该不平衡，但仍无法消除大量背景候选框带来的冗余计算（p.2, Sec. 2.2）。
- **核心矛盾**：如何在**分辨率低、目标小且密集**的无人机图像中实现**快速且准确**的检测。作者据此引入 CenterNet——用关键点估计网络寻找潜在目标，显著降低推理时间（p.2 末）。

## 关键贡献

> 注：本文是一篇评估/调优性质的挑战赛技术报告，"贡献"更多是系统评估与经验结论，而非新方法。

1.  **将 CenterNet 应用并系统评估于 VisDrone2019 航空数据集**：验证这一基于关键点估计的实时检测器在无人机小目标检测上的有效性。
2.  **骨干网络性能对比**：在验证集（n=548）上定量比较 ResNet-18、DLA-34、Hourglass-104 三种骨干，并与 YOLOv3(416×416) 对比，结论是 Hourglass-104 最优（Table 1）。
3.  **测试时增强（TTA）策略分析**：研究**水平翻转**与**多尺度测试**的独立及组合影响，并揭示输入分辨率与缩放尺度的耦合关系，给出最优配置（Table 2, Table 3）。
4.  **在 VisDrone2019 挑战赛两个赛道验证**：图像检测（Track 1，第 7 名，mAP 27.83%）与视频检测（Track 2，第 5 名，mAP 21.58%），其中 Track 1 在 AR500 指标上取得所有参赛方最佳值（Table 4, Table 5）。Track 2 模型未做任何重训练或微调，直接复用 Track 1 模型。

## 方法

- **整体框架**：采用 **CenterNet（Objects as Points, Zhou et al. 2019, 文献[9]）**作为检测模型。它摒弃锚框，将每个物体建模为其边界框的**中心点**，用关键点估计找中心点，再回归尺寸、3D 位置、朝向乃至姿态等属性。该过程端到端可微，相比基于边界框枚举的检测器更简单、更快、更准（p.3, Sec. 3.2）。
- **骨干网络**：实验了 ResNet-18、DLA-34、Hourglass-104；最终采用 **Hourglass-104**（文献[9]）作为主干（p.3, Table 1）。
- **预处理（训练/验证，Sec. 3.2.1）**：图像统一缩放到 **1024×1024**，并用 ImageNet 统计量归一化。
  - 注：在"骨干网络对比"实验（Sec. 4.2）中，输入实际缩放到 **512×512** 后再喂入各网络——预处理小节的 1024×1024 与该消融的 512×512 是两处不同设置，原笔记曾混为一谈，此处已分开标注。
- **训练（Sec. 3.2.2）**：
    - **初始化**：使用 COCO 数据集上的预训练权重。
    - **学习率**：初始 **2.5e-4**，在第 90 与第 120 个 epoch 末各降为 1/10。
    - **优化器**：ADAM（文献[3]）。
- **测试 / 推理（Sec. 3.2.3）**：图像缩放到 **2048×2048**、ImageNet 归一化；使用 2 种 TTA：i) 水平翻转，ii) 多尺度测试，尺度为 **0.5, 0.75, 1, 1.25, 1.5** 倍输入分辨率。
- **与已有方法的差异**：
    - **vs 锚框检测器（SSD/YOLOv3）**：无需枚举近乎穷尽的候选位置，避免前景/背景极端不平衡，省去额外后处理，更高效。
    - **vs 角点关键点方法（如 CornerNet）**：CenterNet 只估计中心点这一个关键点，结构更简单（提取文本未直接对比 CornerNet，此为对 CenterNet 设计的常识性补充）。
- **损失函数**：提取文本未明确给出 CenterNet 的中心点热力图/尺寸回归损失公式（仅引用 Objects as Points 原文[9]），具体损失细节需查原始 CenterNet 论文。

## 实验

- **数据集**：VisDrone2019 **DET**（图像检测）与 **VID**（视频检测），均由天津大学机器学习与数据挖掘实验室 AISKYEYE 团队制作（Sec. 3.1）。
  - 验证集 n=548 张图像（Table 1/2 标注）。注：Fig. 2 标题处标注的是 n=528，与表格不一致，疑为原文笔误。
  - Track 1 测试集 3,190 张图像；Track 2 测试集 33 个序列、共 12,968 张图像。
- **对比方法**：与 YOLOv3(416×416) 对比（Table 1）；挑战赛中与 DPNet-ensemble、RRNet、ACM-OD、S+D、BetterFPN、HRDet（Track 1）及 DBAI-Det、AFSRNet、HRDet+、VCL-CRCNN（Track 2）等参赛算法对比（Table 4, 5）。
- **评价指标**：AP 在 IoU 阈值 [0.5:0.05:0.95] 下计算；AR 在每图最大检测数 1/10/100/500 下计算（Sec. 4.1）。
- **主实验结果**：
    - **骨干网络（Table 1，验证集 n=548）**：Hourglass-104 mAP=**31.97%** > DLA-34 **24.18%** > ResNet-18 **13.36%** > YOLOv3(416×416) **8%**。
    - **TTA-水平翻转（Table 2，Hourglass-104）**：No flip 31.97% → Horizontal flip **32.99%**，约 +1%。
    - **输入分辨率 × 缩放尺度（Table 3，每档尺度步长 0.25 并叠加水平翻转）**：
      | 输入分辨率 | 缩放尺度 | mAP |
      |---|---|---|
      | 512 | 0.5-1.5 | 43.17 |
      | 512 | 1-2.5 | 49.10 |
      | 2048 | 0.5-1.5 | **58.03** |
      | 2048 | 1-2 | 51.99 |
      | 2048 (no-flip) | 0.5-1.5 | 56.88 |
      结论：低输入分辨率(512)宜用较高尺度(1-2.x)，高输入分辨率(2048)宜用较低尺度(0.5-1.5)；超过 2048（如 4096，scale=2）不再提升。在 2048+0.5-1.5 上去掉水平翻转（58.03→56.88），原文称下降"约 2%"（实测约 1.15 个百分点）。最终配置定为输入 2048、尺度 0.5/0.75/1/1.25/1.5。
    - **挑战赛 Track 1（Table 4，n=3190）**：CN-DhVaSa(ours) AP=**27.83%**、AP50=50.73、AP75=26.77、**AR500=46.81（全场最佳）**，排名第 **7**（榜首 DPNet-ensemble 29.62%）。注：本方法 AR1=0、AR10=0.18、AR100=7.78，低召回端表现很差，靠 AR500 取胜。
    - **挑战赛 Track 2（Table 5，n=33 序列）**：CN-DhVaSa(ours) AP=**21.58%**、AP50=48.09、AP75=16.76，排名第 **5**（榜首 DBAI-Det 29.22%）；Track 2 直接复用 Track 1 模型，未重训练/微调。
    - **类别级表现（Table 6）**：Track 1(Image) 上 car=51.92 最高，bus=40.94、van=38.33；people=12.99、bicycle=9.08 最低。Track 2(Video) 上 truck=40.55 最高；motor=6.59、people=6.59 偏低。整体显示大目标（car/bus/truck）远好于小目标（people/bicycle/motor），印证小目标检测的难点。
- **效率信息**：提取文本**未明确给出**推理速度（FPS）、参数量或 FLOPs；论文仅在动机中称 CenterNet "实时"且推理时间短，但未提供本任务下的具体效率数据。

## 局限

1.  **场景与数据限制**：实验仅在 VisDrone2019 上进行，未覆盖更高分辨率、不同光照/天气等其它航空场景。
2.  **方法无创新**：本文为评估/调优工作，未针对航空图像特性改造 CenterNet 架构（如注意力、面向小目标的特征金字塔）。
3.  **效率分析缺失**：未报告推理速度/参数量/FLOPs，而这些对无人机边缘部署关键。
4.  **召回结构性偏弱**：Track 1 在 AR1/AR10/AR100 上接近 0（0 / 0.18 / 7.78），仅 AR500 突出，说明模型每图需要极多检测框才能召回，置信度排序质量差（据 Table 4，为提取文本支撑的客观短板，非原文自述）。
5.  **TTA 手段简单**：仅测水平翻转与朴素多尺度，未比较 Mosaic、自适应缩放等更复杂方案（为评注，非原文）。

## 个人评论

> 以下为 AI 评注，非论文原文观点。

这篇论文的核心价值在于提供了一个**在困难场景（无人机小目标检测）下应用并系统调优一个先进检测框架（CenterNet）的实用案例**，可读为一份扎实的挑战赛工程报告。值得记下的几点：

1.  **系统性消融范式**：通过控制变量（骨干网络 → 翻转 → 输入分辨率×尺度）逐级优化，是值得复制的研究/打榜流程。
2.  **分辨率与缩放尺度的耦合是真知识**：Table 3 清楚地表明"低输入分辨率配大尺度、高输入分辨率配小尺度"，并且盲目放大到 4096 无收益——这类经验对实际部署很有指导价值，比"多尺度有用"这种泛论更扎实。
3.  **指标要看分布而非单点**：本方法靠 AR500 拿到全场最佳召回，却在 AR1/AR10/AR100 几近为 0，是一个很好的反面教材——高 AR500 不等于实用，密集小目标场景下"每图允许多少检测框"会极大改变排名解读。
4.  **直接迁移到视频**：Track 2 不重训练直接复用图像模型仍排第 5，说明 CenterNet 在跨图像/视频检测上的泛化尚可，也暴露其未利用时序信息的潜在改进空间。

### 使用建议

- **快速了解**：读 Abstract、Sec. 1 Introduction、Sec. 5 Conclusion，即可掌握问题、方法与主要结论。
- **复现**：重点读 Sec. 3 (Materials and Methods)，尤其 3.2 的预处理/训练/测试参数；Table 1/2/3 给出关键超参与设置。注意区分预处理 1024×1024 与骨干对比 512×512、测试 2048×2048 三处分辨率。
- **借鉴创新点**：学习其系统性消融设计，特别是骨干选择与"输入分辨率 × 多尺度尺度"的联合调参思路。
- **写 related work**：可归入"无人机/航空图像目标检测"或"小目标检测的评估与调优"类工作引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C_目标检测_通用与旋转框]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉**目标检测**方向，聚焦**航空/无人机（UAV）图像**中的检测任务，是 **VisDrone2019 挑战赛**的一份参赛技术报告（队名 CN-DhVaSa）。它要解决无人机图像分辨率低、视角不规则、目标小且密集导致常规检测器失效的问题，做法是把基于关键点估计的 CenterNet 迁移到 VisDrone2019 并做系统调优。归类于"**目标检测_通用与旋转框**"主题：处理的是通用多类目标（行人、车辆、自行车等），用水平框而非旋转框，无人机/遥感是该主题下的重要应用子领域。

## 2. 一句话总结
本文在 VisDrone2019 无人机数据集上系统评估了基于关键点估计的实时检测器 CenterNet，通过比较 ResNet-18/DLA-34/Hourglass-104 三种骨干及水平翻转、多尺度测试两种 TTA，给出航空小目标检测的最优配置（Hourglass-104 + 输入 2048 + 0.5~1.5 多尺度 + 水平翻转），并在挑战赛 Track 1/2 分获第 7/第 5。

## 3. 背景与问题
- **为什么要做**：航空图像用于城市规划、作物监测、交通监控等，但与 MSCOCO 这类常规数据集相比，无人机图像长宽比异常、视角不规则、目标判别细节缺失，且目标小、聚集密度高（Fig. 1, Sec. 1）。
- **之前方法的问题**：两阶段检测器（Faster R-CNN 等）借 RPN（约 k=2000 候选）获得好性能但推理慢；一阶段检测器（SSD、YOLOv3）用固定密集候选框，前景/背景严重不平衡，RetinaNet 的 focal loss 缓解不平衡但仍要算大量背景候选框（Sec. 2）。
- **核心矛盾**：在低分辨率、小而密集目标的无人机图像上同时要快与准。作者引入 CenterNet（关键点估计找目标）以降低推理时间。

## 4. 核心贡献
1.  将 CenterNet 系统性地评估于 VisDrone2019 DET/VID（验证集 n=548）。
2.  骨干网络对比：Hourglass-104(31.97) > DLA-34(24.18) > ResNet-18(13.36) > YOLOv3(8)（Table 1）。
3.  TTA 分析：水平翻转 +1%（Table 2）；揭示输入分辨率与缩放尺度的耦合并给最优配置（Table 3）。
4.  挑战赛验证：Track 1 第 7（mAP 27.83%，AR500 全场最佳 46.81）、Track 2 第 5（mAP 21.58%，模型直接复用未微调）。

## 5. 方法详解
- **整体框架**：CenterNet（Objects as Points，[9]）以边界框中心点为单一关键点建模物体，用关键点估计定位中心、再回归尺寸等属性，端到端可微，比枚举锚框的检测器更简单/快/准。主干用 Hourglass-104。
- **输入/输出**：输入无人机图像；输出每个目标的中心点、类别及边界框宽高。
- **预处理**：训练/验证图像缩放 1024×1024、ImageNet 归一化（Sec. 3.2.1）；但骨干对比消融实际用 512×512 输入（Sec. 4.2）——两处分辨率不同，须区分。
- **训练**：COCO 预训练初始化；LR 初始 2.5e-4，在第 90、120 epoch 末各降 10×；优化器 ADAM（Sec. 3.2.2）。
- **测试**：缩放 2048×2048、ImageNet 归一化；2 种 TTA = 水平翻转 + 多尺度（0.5/0.75/1/1.25/1.5）（Sec. 3.2.3）。
- **与他法差异**：相对 SSD/YOLOv3 免去近乎穷尽的候选枚举与前景/背景不平衡及额外后处理；损失函数细节提取文本未给出，参见 CenterNet 原文[9]。

## 6. 实验与结果
- **数据集**：VisDrone2019 DET（图像）/VID（视频），AISKYEYE@天津大学制作；验证 n=548；Track 1 测试 3190 图；Track 2 测试 33 序列/12968 图。
- **指标**：AP@IoU[0.5:0.05:0.95]；AR@maxDet 1/10/100/500（Sec. 4.1）。
- **骨干（Table 1，n=548）**：Hourglass-104 **31.97** / DLA-34 24.18 / ResNet-18 13.36 / YOLOv3(416) 8。
- **水平翻转（Table 2）**：31.97 → **32.99**（+1%）。
- **分辨率×尺度（Table 3，步长 0.25，含水平翻转）**：512/0.5-1.5=43.17，512/1-2.5=49.10，2048/0.5-1.5=**58.03**，2048/1-2=51.99，2048(no-flip)/0.5-1.5=56.88。结论：低分辨率配大尺度、高分辨率配小尺度；>2048 无增益；去翻转降"约 2%"（实测约 1.15 点）。
- **Track 1（Table 4，n=3190）**：ours AP=27.83、AP50=50.73、AP75=26.77、AR500=**46.81（全场最高）**，第 7 名；但 AR1=0、AR10=0.18、AR100=7.78，低召回端极弱。
- **Track 2（Table 5，n=33）**：ours AP=21.58、AP50=48.09、AP75=16.76，第 5 名，复用 Track 1 模型未重训。
- **类别级（Table 6）**：大目标（car 51.92 / bus 40.94 / van 38.33）远好于小目标（people 12.99 / bicycle 9.08 / motor 20.35）；视频侧 truck 40.55 最高，motor/people 仅 ~6.6。
- **效率**：推理速度/参数量/FLOPs 提取文本均未给出。

## 7. 这篇论文真正有价值的地方
1.  **可复制的系统消融流程**：骨干 → 翻转 → 分辨率×尺度逐级调参，是打榜/部署调优的好范式。
2.  **分辨率-尺度耦合的实证**：低输入分辨率用大尺度、高输入分辨率用小尺度，且 4096 无收益——比"多尺度有用"更具体可操作。
3.  **指标分布的警示价值**：本方法靠 AR500 夺得全场最佳召回，却在 AR1/10/100 近乎为 0，提醒读者评估密集小目标检测时必须看不同 maxDet 下的召回分布，而非单一 mAP。
4.  **图像模型零成本迁移视频**：Track 2 不微调仍第 5，显示 CenterNet 的跨域泛化，也指出未用时序的改进空间。

## 8. 局限与问题
1.  仅在 VisDrone2019 上评估，泛化到其它航空场景未验证。
2.  纯评估/调优，未对 CenterNet 架构做面向航空小目标的改造。
3.  无效率（速度/参数/FLOPs）分析，不利于边缘部署评估。
4.  召回结构性偏弱：AR1/AR10/AR100 近 0，仅 AR500 突出，置信度排序质量差（据 Table 4）。
5.  TTA 仅水平翻转 + 朴素多尺度，未比更复杂增强（评注）。

## 9. 我该怎么使用这篇论文
- **快速了解**：读 Abstract、Sec. 1、Sec. 5。
- **复现**：读 Sec. 3，注意三处分辨率（预处理 1024、骨干对比 512、测试 2048）与 Table 1/2/3 的超参。
- **借鉴**：学其系统消融与"分辨率×多尺度"联合调参思路。
- **写 related work**：归入"无人机/航空图像目标检测"或"小目标检测评估与调优"。

## 10. 和其他论文的关系
- [[Objects as Points (CenterNet)]]（Zhou et al. 2019，文献[9]，本文方法核心来源）
- [[YOLOv3: An Incremental Improvement]]（文献[7]，主要对比基线）
- [[SSD: Single Shot MultiBox Detector]]（文献[6]，一阶段检测器代表）
- [[Focal Loss for Dense Object Detection]]（RetinaNet，文献[4]，讨论的一阶段改进）
- [[Faster R-CNN]]（文献[8]，两阶段检测器代表）
- [[VisDrone2019 挑战赛及参赛方法]]（DPNet-ensemble、RRNet、DBAI-Det 等，提供数据集与基准）

## 11. 关键词
CenterNet, Objects as Points, 航空/无人机图像目标检测, VisDrone2019, DET/VID, 骨干网络评估, 测试时增强 (TTA), 水平翻转, 多尺度测试, 分辨率-尺度耦合, 关键点估计, 小目标检测, Hourglass-104, AR500

## 12. 可信度说明
本精读笔记基于 PDF 提取文本（6/6 页，含 Abstract、Introduction、Related work、Methods、Results、Conclusion、References 及 Table 1-6 与 Fig 1-2 标题）生成。表格 1-3 与 4-6 的具体 mAP/AP/AR 数值均直接摘自提取文本对应表格行。少量为评注或对 CenterNet 的常识性补充（已在正文标注"评注/常识性补充"），损失函数公式与效率数据原文未给出。验证集规模 548 与 Fig. 2 标注的 528 不一致，疑为原文笔误，已标注。所有事实分析严格限定在提取文本范围内。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 6/6 页全覆盖); 来源缓存: `.paper-cache/extracts/2019_Object_detection_on.txt` (6/6 页); 生成日期: 2026-06-04; 复核优化: 2026-06-18; 模式: LLM (mimo-v2.5-pro) + 提取文本逐条核对.
<!-- AI_READING_NOTE_END -->
</content>
</invoke>
