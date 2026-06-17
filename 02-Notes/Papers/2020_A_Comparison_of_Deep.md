---
title: A Comparison of Deep Learning Object Detection
authors:
  - "Austen Groener Gary Chern Mark Pritt"
  - "King of Prussia"
  - "Pennsylvania Palo Alto"
  - "California Gaithersburg"
  - "Maryland"
year: 2020
venue: science. As the volume of data increases rapidly, so too
doi: 
pdf: [[2020_A_Comparison_of_Deep.pdf]]
primary_topic: R_综述_Survey
topics:
  - "R_综述_Survey"
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
extract_cache: .paper-cache/extracts/2020_A_Comparison_of_Deep.txt
---

# A Comparison of Deep Learning Object Detection

## 基本信息
- **PDF**: [[2020_A_Comparison_of_Deep.pdf]]
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A Comparison of Deep Learning Object Detection Models for Satellite Imagery |
| **作者** | Austen Groener, Gary Chern, Mark Pritt（均属 Lockheed Martin Space） |
| **发表时间** | 2020（arXiv:2009.04857v1, 2020-09-10） |
| **刊物/会议** | PDF 文本未明确正式发表刊物（提取文本显示为 arXiv 预印本, cs.CV） |
| **DOI** | PDF 文本未明确（arXiv ID: 2009.04857） |

## 摘要

清理后的英文原摘要（据 PDF 提取文本整理, 修复空格/连字符断裂）：

> In this work, we compare the detection accuracy and speed of several state-of-the-art models for the task of detecting oil and gas fracking wells and small cars in commercial electro-optical satellite imagery. Several models are studied from the single-stage, two-stage, and multi-stage object detection families of techniques. For the detection of fracking well pads (50m–250m), we find single-stage detectors provide superior prediction speed while also matching detection performance of their two- and multi-stage counterparts. However, for detecting small cars, two-stage and multi-stage models provide substantially higher accuracies at the cost of some speed. We also measure timing results of the sliding window object detection algorithm to provide a baseline for comparison. Some of these models have been incorporated into the Lockheed Martin Globally-Scalable Automated Target Recognition (GATR) framework.

中文翻译：

> 本文比较了若干先进模型在商业电子光学（EO）卫星图像中检测油气压裂井（fracking wells）和小型汽车两类目标时的检测精度与速度。研究涵盖单阶段、两阶段和多阶段三大目标检测技术族。对于压裂井平台（50–250 米）的检测，单阶段检测器在提供更优预测速度的同时，检测性能可与两阶段、多阶段模型相匹配；但对于小型汽车检测，两阶段和多阶段模型以牺牲部分速度为代价获得了显著更高的精度。本文还测量了滑动窗口目标检测算法的耗时结果作为比较基准。部分模型已被整合进洛克希德·马丁公司的全球可扩展自动目标识别（GATR）框架。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：图像分析师与地球科学家面临从多光谱、俯视传感器采集的海量数据中提取情报的严峻挑战。自动目标识别（ATR，亦即目标检测）在广域搜索、持续站点监测、建设工地发现与跟踪、土地管理分析、人道救援与灾害响应、以及油气压裂井监测等任务中扮演核心角色，其输出（目标类别 + 边界框坐标）被送入大量下游应用（p.1）。
- **之前方法的问题**：因实现简单，文献中常用滑动窗口算法替代更现代的方法，但滑动窗口在速度与定位精度之间存在根本性权衡（p.1, [4]）。历史上最高精度模型几乎总采用两阶段方案（Stage 1 候选目标检测 + Stage 2 用 CNN 做分类与位置精修）；单阶段模型则一次性同时回归边界框参数和分类。近来若干单阶段模型已证明能在匹配两阶段性能的同时显著提速（p.1, [5][6]）。
- **核心矛盾**：卫星图像与自动驾驶场景差异显著——目标多从正上方俯视（含离天底角偏差）、单幅图像极大（WorldView-3 单幅全色影像常 >10 Gigapixel，该星每天可采集多达 680,000 km² 的 31cm 全色影像）、目标物理尺度跨度极大（从数米/几像素到数百米/数百像素）、常被云雾遮挡并受温湿度、霾、太阳角影响，极端情况下目标仅数像素且密集排列。作者要探究：哪种先进架构（单/两/多阶段）能在该独特领域最好地平衡精度与速度（p.2）。

## 关键贡献

1.  **系统的比较研究**：在卫星图像领域对六种前沿目标检测模型（RetinaNet, GHM, Faster R-CNN, Grid R-CNN, Double-Head R-CNN, Cascade R-CNN）× 三种骨干网络（ResNet-50, ResNet-101, ResNeXt-101）进行精度与速度基准测试（见 Table I 的模型-骨干组合矩阵）。这些模型均非为俯视图像（EO/IR/SAR）专门设计（p.5）。
2.  **大目标量化发现**：对于大尺度目标（压裂井平台，50–250m），单阶段检测器（RetinaNet、GHM）同时给出最高检测性能与最佳面积覆盖率；最高精度为 **RetinaNet + ResNeXt-101，AP=0.92**（p.7）。
3.  **小目标量化发现**：对于小尺度、密集目标（小汽车），两阶段与多阶段模型 AP 均接近 0.70、max F1 约 0.75，显著优于单阶段（单阶段 AP 从 RetinaNet 的 0.661 降到 GHM 的 0.583）；最佳模型为 Grid R-CNN（ResNet-101/ResNeXt-101 骨干）（p.7-8）。
4.  **基线对比**：测量滑动窗口算法的耗时，揭示其为达到与现代模型相当的面积覆盖率，需选用 100–250 像素的极大步长，严重损害定位精度（p.5, p.8, Figure 7）。
5.  **工程实践整合**：部分模型已被整合进洛克希德·马丁公司的全球可扩展自动目标识别（GATR）框架（p.1-2, [13]）。注：论文指出 GATR 框架中的压裂井模型使用更低的 IoU 阈值，性能高于本文所报（p.7 脚注）。

## 方法

- **整体框架**：采用“模型-骨干”组合的对比框架，统一使用开源工具箱 **MMDetection**（基于 PyTorch，提供 200+ 高性能检测模型的预训练权重与定义）做模型定义、训练与测试，保证比较公平（p.5）。MMDetection 将单/两/多阶段模型抽象为共用的功能组件（如所有模型共享 backbone 特征提取器）。
- **输入输出**：输入为卫星图像切片（chips）；输出为每个目标的类别概率与边界框坐标。压裂井：从 5000×5000 像素切片下采样到 1250×1250（1.24m GSD，配 ResNet-50/101）与 1050×1050（1.48m GSD，配 ResNeXt-101）。小汽车：保留原生 30cm 分辨率，切成 600×600 后上采样到 1200×1200（ResNet-50/101）与 1000×1000（ResNeXt-101）。选择上采样而非降低 IoU 阈值，是为了能沿用默认模型配置（小汽车标注约 10×16 像素，不足 Faster R-CNN 最小锚框 32×32 的一半）（p.4）。
- **关键模块与模型类别**：
    1.  **单阶段**：RetinaNet（引入 **Focal Loss**，通过修改交叉熵聚焦难样本，解决严重的前景-背景类别不平衡）；GHM（梯度调和机制，修改分类损失 GHM-C 与回归损失 GHM-R，缓解易/难、正/负样本的梯度不均衡）。
    2.  **两阶段**：Faster R-CNN（用 RPN 网络替代 selective search 做区域提议）；Grid R-CNN（用**网格点引导的定位机制**替代全连接回归框，在 COCO 上尤其在收紧定位约束时表现 SOTA）；Double-Head R-CNN（分类用全连接头、边界框回归用卷积头）。
    3.  **多阶段**：Cascade R-CNN（级联一串对定位要求逐级更严的检测器，逐阶段联合训练，前一检测器输出作为后一检测器的良好训练分布，以抑制接近的假正例）。
    4.  **基准方法**：滑动窗口——单 CNN 分类器在预定义窗口上分类，再在两维方向滑动以覆盖全图（Figure 3）。压裂井的滑窗用独立训练的 ResNet-50/ResNet-101 分类器，在 1.24m GSD 下的 250×250 切片上区分“井 vs. clutter（非井杂物）”；窗口取能完全覆盖所有真值框的最小尺寸；因 ResNet-50/101 验证精度已很高，未训练更复杂的 ResNeXt-101（p.6）。
- **骨干网络**：所有模型共享 ResNet-50、ResNet-101、ResNeXt-101 三种 CNN 骨干（p.2, p.5）。
- **训练方式**：以 MMDetection 默认配置文件 + ImageNet 预训练权重为起点，除学习率外多数超参保持默认；统一用带动量、学习率衰减与调度的 SGD 优化器；数据增强仅用随机水平/垂直翻转。压裂井训练 12–25 epoch、汽车 6–12 epoch（按模型复杂度调整）。滑窗 CNN 用目标切片（而非整景）作为独立分类器训练，增强与优化设置与上述模型基本一致（学习率与 epoch 数除外）（p.6）。
- **评估指标**：
    1.  **平均精度 AP**：P-R 曲线下面积（式 4）；多类时取各类 AP 均值（mAP）。压裂井报告 AP@IoU=0.50，小汽车因目标极小报告 AP@IoU=0.25（p.7）。IoU/Jaccard 指数、P=TP/(TP+FP)、R=TP/(TP+FN) 均给出公式（式 1-3）。
    2.  **max F1**：P-R 曲线上 P 与 R 调和平均最大的点（最接近完美分类器 P=R=1）（式 5）。
    3.  **面积覆盖率（area coverage rate）**：单位 km²/sec，衡量模型处理数据的吞吐量。
- **与已有方法的差异**：原有检测研究多面向自动驾驶（按高分辨率视频逐帧、毫秒级避撞需求设计）；本文将每个 chip 视作独立输入，专门评估卫星图像的俯视、超大图、多尺度挑战，并引入更贴合对地观测的“面积覆盖率”速度指标（p.2-3）。

## 实验

- **使用的数据集**：
    1.  **WorldView-3 压裂井**：作者从全球手动整理了 **超过 12,000 个**各运营阶段的压裂井（0.31m GSD pansharpened 影像）以构建全球可扩展模型；**本文聚焦其中新墨西哥州子集——2,802 个压裂井，分布于 568 张 5000×5000 像素的 WorldView-3 切片**，再下采样到 1250×1250（1.24m GSD）与 1050×1050（1.48m GSD）（p.4）。
    2.  **xView 小汽车**：取自公开 xView 数据集（DIUx 与 NGA 组织的 2018 检测挑战赛，60 类手标真值框）的 small car 类（class #18）。共 **210,938 个小汽车**实例（约 35% 的图含至少一辆车），原生 30cm GSD 下小汽车约 7 像素/边（中位 14 像素/边），切成 600×600 后上采样到 1200×1200 / 1000×1000（p.4-5）。
- **对比方法**：六种深度学习模型 × 三种骨干，加滑动窗口基线（Table I）。
- **评价指标**：AP、max F1、面积覆盖率（km²/sec）。
- **测速设置**：单块 NVIDIA TITAN Xp GPU；面积覆盖率由非重叠定面积图像上的 FPS 换算得到；每张压裂井 WorldView-3 图固定为 **2.4025 km²**、每张 xView 小汽车图为 **0.0324 km²**。滑窗的计时使用重叠窗口（这正是其更慢的原因）。训练用多 GPU 加速，但有意未探索预测时的并行（p.7）。
- **主实验结果**：
    - **压裂井**：单阶段 RetinaNet、GHM 同时拿下最高性能与最佳面积覆盖率。追求最高精度选 **RetinaNet + ResNeXt-101（AP=0.92）**；纯追求面积覆盖率选 **RetinaNet + ResNet-50**；联合优化性能与速度则 GHM(ResNet-50/101) 与 RetinaNet(ResNet-101) 占据理想权衡区（p.7, Figure 4 / Table II / Figure 8 的 P-R 曲线）。
    - **小汽车**：两阶段与多阶段 AP 均略低于 0.70、max F1 约 0.75；单阶段落后，AP 从 RetinaNet 的 **0.661** 降到 GHM 的 **0.583**。最高性能为 **Grid R-CNN（ResNet-101/ResNeXt-101 骨干）**，但多个模型-骨干组合非常接近；最快为 RetinaNet/GHM/Faster R-CNN 配 ResNet-50；**速度与精度最佳折中为 Faster R-CNN + ResNet-50**（p.7-8, Figure 5 / Table III / Figure 9）。论文指出 xView 车辆指标偏低属正常（尺寸小且拥挤）（p.8, [22]）。
    - **滑动窗口**：要达到与现代检测器相当的面积覆盖率，需 100–250 像素的极大步长，严重损害边界框定位精度（p.8, Figure 7）。
- **消融实验**：PDF 文本未明确说明系统消融，但通过对同一模型比较 ResNet-50/101/ResNeXt-101 三种骨干，展示了骨干复杂度与精度/速度的权衡。
- **泛化实验**：PDF 文本未明确说明跨域泛化实验。
- **效率信息**：速度以面积覆盖率（km²/sec）报告，硬件为单块 NVIDIA TITAN Xp；论文明确未探索预测时多 GPU 并行（p.7）。

## 局限

1.  **场景局限性**：实验仅针对两类目标（压裂井、小汽车）来代表“大尺度”与“小尺度”两端，可能无法覆盖中等尺度或形状不规则的目标。
2.  **数据集局限**：压裂井实验仅用新墨西哥州 2,802 个样本子集（虽源自 12,000+ 全球库），地理多样性受限；xView 小汽车存在固有的小目标、密集场景挑战，指标天然偏低。
3.  **计算成本**：所有计时在单 GPU 上，论文有意未探索预测时并行；未讨论边缘/集群部署效率（对实时卫星处理可能重要）。
4.  **方法假设**：为沿用默认配置而对小汽车图像 2× 上采样，简化了实验但可能非最优且增加计算量；亦可改为降低 IoU 阈值，作者未对两种方案做对比。
5.  **复现风险**：压裂井使用商业 WorldView-3 影像与作者自标注子集，完全复现需访问相同数据；论文也指出 GATR 框架内的井模型用更低 IoU 阈值，性能与本文所报不同。

## 个人评论

这篇论文最大的价值在于为**卫星图像目标检测提供了一份实证的、可直接落地的模型选择指南**。它超越单纯的性能报告，把“**目标物理尺度**”识别为决定架构选择的关键因素：大目标（建筑、大型设施、压裂井）优先单阶段以换取高吞吐；小目标（车辆、小型装备）优先两/多阶段以换取定位精度。这个“按尺度选架构”的结论简单但工程上很有指导意义。

方法学上有两点值得借鉴：其一，用 **MMDetection 统一框架 + 共享骨干**做横向对比，把架构差异从工程差异中剥离出来，比较更可信；其二，用 **面积覆盖率（km²/sec）替代 FPS** 作为速度指标，更贴合对地观测“处理多大区域”的实际需求。需注意：这是一篇 2020 年的预印本，所测模型（RetinaNet 至 Cascade R-CNN）属于当时一代，结论的“相对趋势”比“绝对数值”更具长期价值；且压裂井数据为商业影像+自标注，绝对 AP（如 0.92）与该特定数据/IoU 设置强绑定，不宜直接外推。

### 使用建议

- **快速了解**：读摘要、结论（VI 节）与结果（V 节）的总结及 Figure 4 / Figure 5 的权衡图。
- **如果复现**：重点读方法（IV 节）与数据集（III 节），尤其是预处理（下采样/上采样及对应 GSD）、训练超参与 IoU/AP 定义；注意需获取 WorldView-3 与 xView 数据。
- **如果借鉴创新点**：学习其系统对比框架（模型×骨干矩阵）、针对卫星图像调整的实验设置（IoU 阈值、2× 上采样）以及面积覆盖率指标。
- **如果写 related work**：可归为“卫星/遥感图像中深度学习目标检测的架构比较/基准研究”。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉的目标检测方向，应用场景为商业电子光学（EO）卫星/遥感图像分析。它本质是一篇**架构横向比较 / 基准评测**研究：把面向自动驾驶设计的现代检测器（单/两/多阶段）迁移到俯视卫星图像，系统比较其在两类不同物理尺度目标（50–250m 的油气压裂井 vs. 仅几像素的小汽车）上的检测精度与推理速度，给出工程模型选择指南。归在“R_综述_Survey”（比较/基准类）下合适。

## 2. 一句话总结
在统一的 MMDetection 框架与共享骨干下比较六种检测器 × 三种骨干，发现：大目标（压裂井）单阶段即可在更快速度下匹配甚至超越两/多阶段（RetinaNet+ResNeXt-101 AP=0.92），而小目标（小汽车）必须用两/多阶段才能拿到约 0.70 的 AP——模型选择应由目标尺度与精度-速度权衡共同决定。

## 3. 背景与问题
- **为什么要做**：对地观测数据量爆炸（WorldView-3 单星每天可采集多达 680,000 km² 的 31cm 全色影像，单幅常 >10 Gigapixel），广域搜索、站点监测、压裂井监测等任务亟需自动目标识别（ATR）。现有检测研究多面向自动驾驶（地面视角、毫秒级避撞），与卫星场景差异大。
- **之前方法的问题**：滑动窗口实现简单但在速度与定位精度间存在根本权衡，且目标尺度差异大时需多套模型；历史最高精度依赖两阶段（候选+精修），单阶段虽快此前性能落后。
- **核心矛盾**：卫星图像俯视、超大图、目标物理尺度跨数米到数百米、易被云雾遮挡甚至仅数像素且密集——在此独特领域，哪类架构能最好地平衡精度与速度尚无系统答案。

## 4. 核心贡献
1.  在卫星图像领域系统比较 RetinaNet / GHM / Faster R-CNN / Grid R-CNN / Double-Head R-CNN / Cascade R-CNN × ResNet-50 / ResNet-101 / ResNeXt-101（Table I 矩阵），所有模型均非为俯视图像专门设计。
2.  大目标结论：单阶段（RetinaNet、GHM）同时给出最高性能与最佳面积覆盖率，最高 AP=0.92（RetinaNet+ResNeXt-101）。
3.  小目标结论：两/多阶段 AP≈0.70、max F1≈0.75，单阶段落后（AP 0.661→0.583），最佳为 Grid R-CNN。
4.  以滑动窗口为基线，量化其“为提速需 100–250 像素大步长、严重损害定位”的固有缺陷。
5.  部分模型已落地洛克希德·马丁 GATR 框架（GATR 内井模型用更低 IoU 阈值，性能高于本文所报）。

## 5. 方法详解
- **统一框架**：MMDetection（PyTorch，200+ 模型与 ImageNet 预训练权重），把单/两/多阶段抽象为共用组件（共享 backbone），保证横向比较公平。
- **预处理**：压裂井 5000×5000 切片下采样到 1250×1250（1.24m GSD，ResNet-50/101）/ 1050×1050（1.48m GSD，ResNeXt-101）；小汽车保留 30cm 原生分辨率、切 600×600 后上采样到 1200×1200 / 1000×1000。小汽车标注约 10×16 像素，不足 Faster R-CNN 最小锚框 32×32 的一半，故选择 2× 上采样而非降低 IoU 阈值，以便沿用默认配置。
- **模型要点**：RetinaNet=Anchor+FPN+Focal Loss（治前景背景类不平衡）；GHM=梯度调和（GHM-C/GHM-R）；Faster R-CNN=RPN 替代 selective search；Grid R-CNN=网格点引导定位替代 FC 回归；Double-Head R-CNN=FC 头分类 + 卷积头回归；Cascade R-CNN=逐级收紧 IoU 的级联检测器、逐阶段联合训练。滑窗=单 CNN 分类器（ResNet-50/101，在 250×250、1.24m GSD 切片上区分井/clutter，窗口取覆盖所有真值框的最小尺寸；验证精度高故未训 ResNeXt-101）。
- **训练**：MMDetection 默认配置 + ImageNet 权重，除学习率外多数超参默认；带动量/衰减/调度的 SGD；增强仅随机水平+垂直翻转；井 12–25 epoch、车 6–12 epoch。
- **指标**：AP（井 @IoU=0.50、车 @IoU=0.25）、max F1（P-R 曲线调和均值最大点）、面积覆盖率 km²/sec；给出 IoU、P、R、AP、F1 的全部公式。

## 6. 实验与结果
- **数据集**：压裂井——全球手标 12,000+，本文用新墨西哥子集 2,802 个 / 568 张 5000×5000 切片；小汽车——xView class #18，210,938 个实例，原生 30cm 约 7px/边（中位 14px）。每张井图 2.4025 km²、每张车图 0.0324 km²。
- **硬件/计时**：单块 NVIDIA TITAN Xp，面积覆盖率由非重叠定面积图的 FPS 换算；滑窗用重叠窗口计时（更慢的原因）；训练用多 GPU，预测时未并行。
- **压裂井**：单阶段 RetinaNet/GHM 性能与速度双优。最高 AP=0.92（RetinaNet+ResNeXt-101）；纯速度选 RetinaNet+ResNet-50；联合权衡区由 GHM(R50/R101)+RetinaNet(R101) 填充（Figure 4 / Table II / Figure 8）。
- **小汽车**：两/多阶段 AP 略低于 0.70、max F1≈0.75；单阶段 AP 0.661(RetinaNet)→0.583(GHM)。最佳 Grid R-CNN(R101/ResNeXt-101)，多组合接近；最快 RetinaNet/GHM/Faster R-CNN+R50；速度-精度最佳折中 Faster R-CNN+R50（Figure 5 / Table III / Figure 9）。xView 车辆指标偏低属正常（小且拥挤）。
- **滑动窗口**：为达现代检测器的面积覆盖率需 100–250px 极大步长，严重损害定位（Figure 7）。
- **消融/泛化**：未做系统消融与跨域泛化；仅以三种骨干的横向比较呈现复杂度-性能权衡。

## 7. 这篇论文真正有价值的地方
价值在于把抽象的“架构 vs. 场景”问题转成一条可操作的工程经验：**目标物理尺度是选架构的第一性变量**——大目标用单阶段（更快、精度不输），小目标用两/多阶段（精度显著更高、可接受降速）。方法学上的两个可借鉴点：用 MMDetection+共享骨干把架构差异与实现差异解耦；用面积覆盖率（km²/sec）代替 FPS，更贴合对地观测“处理多大区域”的真实诉求。

## 8. 局限与问题
1.  仅用压裂井、小汽车代表大/小两端尺度，未覆盖中等尺度或不规则目标。
2.  压裂井实验仅新墨西哥子集（2,802），地理多样性受限；xView 小汽车小且密集，指标天然偏低。
3.  计时在单 GPU、有意未做预测时并行；未讨论边缘/集群部署。
4.  为沿用默认配置对小汽车 2× 上采样，可能非最优且增计算量，未与“降低 IoU 阈值”方案对比。
5.  商业 WorldView-3 影像 + 自标注子集复现门槛高；GATR 内井模型用更低 IoU 阈值，性能与本文所报不一致。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要、结论（VI）、结果（V）总结及 Figure 4/5 权衡图。
- **如果复现**：方法（IV）+ 数据集（III），尤其预处理（下采样/上采样及对应 GSD）、训练超参、IoU/AP 定义；注意需获取 WorldView-3 与 xView 数据。
- **如果借鉴创新点**：模型×骨干对比框架、针对卫星图像的实验设置（IoU 阈值、2× 上采样）、面积覆盖率指标。
- **如果写 related work**：归为“卫星/遥感图像中深度学习目标检测的架构比较/基准研究”。

## 10. 和其他论文的关系
作为比较研究，本文主要**引用并评测**其对比的各原始模型（RetinaNet [5]、GHM [6]、Faster R-CNN [7]、Grid R-CNN [8]、Double-Head R-CNN [9]、Cascade R-CNN [10]），骨干引用 ResNet [11]、ResNeXt [12]；数据/工具引用 xView [15]、MMDetection [16]、COCO [21]。它本身是这些模型在卫星图像这一特定域上的应用效果评估报告。由于知识库主题中未列出这些模型的独立笔记，此处不作不确定的内部链接关联。

## 11. 关键词
自动目标识别(ATR), 目标检测, 深度学习, 卫星/遥感图像, 油气压裂井检测, 小汽车检测, 模型比较/基准, 单阶段检测器, 两阶段检测器, 多阶段检测器, 面积覆盖率, MMDetection, 滑动窗口, GATR

## 12. 可信度说明
本精读完全基于 PDF 提取文本（10/10 页，覆盖摘要、引言、Problem、Dataset、Methods 全部与 Results 主体至结论 VI 节开头）。提取质量良好、文字清晰，关键数值（2,802 / 568 / 210,938 / AP=0.92 / 0.661 / 0.583 / 2.4025 km² / 0.0324 km²、各 GSD、IoU 阈值）与论述逻辑均可在提取文本中逐条核对。主要限制：无法读取 Table II/III 的逐行数值与 Figure 4/5/7/8/9 的精确曲线，以及原文 25000 字符后被截断的结论段尾与参考文献（提取缓存显示原文 34751 字符，仅展示前 25000）。结论 VI 节最后关于“小汽车性能偏低原因”的完整解释位于截断处，本笔记据已有正文与摘要一致复述。

---

> **可信度补充**: PDF 提取质量 = **high** (10/10 页, 文字清晰, 关键数值可逐条核对; 正文约 25000/34751 字符, 结论段尾与参考文献被截断); 来源缓存: `.paper-cache/extracts/2020_A_Comparison_of_Deep.txt`; 生成日期: 2026-06-04; 复核优化: 2026-06-18; 模式: LLM (mimo-v2.5-pro) + 人工对照提取文本校订事实.
<!-- AI_READING_NOTE_END -->
