---
title: "Waste detection in Pomerania: non-profit project for detecting waste in environment"
authors:
  - "Sylwia Majchrowska"
  - "Agnieszka Mikołajczyk"
  - "Maria Ferlin"
  - "Zuzanna Klawikowska"
  - "Marta A. Plantykow"
  - "Arkadiusz Kwasigroch"
  - "Karol Majek"
year: 2021
venue: "arXiv"
doi: 
pdf: [[2021_Waste_detection_in_P.pdf]]
primary_topic: C2_目标检测_违建_车辆_船舶_行人
topics:
  - "C2_目标检测_违建_车辆_船舶_行人"
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
extract_cache: .paper-cache/extracts/2021_Waste_detection_in_P.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/19 pages"
---
# Waste detection in Pomerania: non-profit project for detecting waste in environment

## 基本信息
- **PDF**: [[2021_Waste_detection_in_P.pdf]]
- **primary_topic**: `C2_目标检测_违建_车辆_船舶_行人`
- **topics**: `C2_目标检测_违建_车辆_船舶_行人`
- **状态**: ai-read (已 AI 全文覆盖, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Waste detection in Pomerania: non-profit project for detecting waste in environment |
| **作者** | Sylwia Majchrowska (Wrocław University of Science and Technology); Agnieszka Mikołajczyk, Maria Ferlin, Zuzanna Klawikowska, Arkadiusz Kwasigroch (Gdańsk University of Technology); Marta A. Plantykow (Intel); Karol Majek (Cufix) |
| **发表时间** | 2021-05 (arXiv:2105.06808v1, [cs.CV]) |
| **刊物/会议** | arXiv preprint |
| **DOI** | 未明确 (arXiv:2105.06808) |
| **代码** | https://github.com/wimlds-trojmiasto/detect-waste |

## 摘要

> Waste pollution is one of the most significant environmental issues in the modern world. The importance of recycling is well known, either for economic or ecological reasons, and the industry demands high efficiency. Our team conducted comprehensive research on Artificial Intelligence usage in waste detection and classification to fight the world's waste pollution problem. As a result, an open-source framework that enables the detection and classification of litter was developed. The final pipeline consists of two neural networks: one that detects litter and a second responsible for litter classification. Waste is classified into seven categories: bio, glass, metal and plastic, non-recyclable, other, paper and unknown. Our approach achieves up to 70% of average precision in waste detection and around 75% of classification accuracy on the test dataset. The code used in the studies is publicly available online.

> **中文翻译**：废物污染是现代世界最重大的环境问题之一。回收的重要性人尽皆知（无论出于经济还是生态原因），且产业界对其效率有很高要求。我们的团队就"用人工智能进行废物检测与分类来对抗全球废物污染"开展了系统性研究，最终开发出一个能够检测并分类垃圾的开源框架。最终的处理流程由两个神经网络组成：一个负责检测垃圾，另一个负责对垃圾进行分类。废物被划分为七个类别：bio（生物可降解）、glass（玻璃）、metal and plastic（金属与塑料）、non-recyclable（不可回收）、other（其他）、paper（纸）和 unknown（未知）。本方法在测试集上的废物检测平均精度（AP）最高可达 70%，分类准确率约为 75%。研究所用代码已公开。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：废物污染是全球性环境问题，一次性商品的大量生产使年垃圾产量呈指数增长，达到约每年 20 亿吨（提取文本引用 [1]）；据估计人类每年摄入多达 250 克微塑料，其中近 90% 来自瓶装水和自来水；当前每年生产超过 3 亿吨塑料，按此趋势仅需约 30 年海洋中垃圾的数量就将超过海洋生物的数量。提高回收效率是关键，但由于能耗大、成本高，许多分拣线上的塑料废物分离仍靠人工完成，深度学习为自动化分拣提供了可能。
- **之前方法的问题**：
    1.  **场景受限**：现有基于机器学习的分拣系统多为自分拣"智能垃圾桶"（self-sorting smart bins），一次只能对置于清晰单一背景上的单个物体进行分类（相机通常架在容器顶部），无法处理野外（in the wild）复杂、形变、多样自然场景下的垃圾。
    2.  **定义模糊**：同一物体是否算"垃圾"取决于上下文，因此必须明确定义"在什么时候/什么条件下"应将被定位的物体视为垃圾（litter）。
    3.  **分拣规则不统一 + 数据集分散**：废物分类（segregation）规则复杂且不统一；现有公开废物数据集在类别、场景多样性或标注级别（分类/检测/分割）上各有不足，缺乏面向可回收物、统一定义的标注与综述。
- **核心矛盾**：在复杂多变的真实自然场景中，如何对形态各异、背景干扰多样的废物进行有效且可归类的"检测 + 分类"，以支持实际的自动化分拣流程。

## 关键贡献

1.  **混合公开数据集 + 七类废物分类标准**：将多个不同环境下的公开废物数据集混合，并提出七类"定义良好"的分拣类别——`bio`、`glass`、`metal and plastic`、`non-recyclable`、`paper`、`other`、`unknown`，其选择灵感来自波兰格但斯克（Gdańsk）的分类规则。
2.  **两阶段 DL 检测框架（开源）**：实现了一个由"检测器（detector）+ 分类器（classifier）"两个独立神经网络组成的两阶段框架，自由开源，可用于多种用途（如研究自然界中常见废物类型）。作者声称这是首个支持如此"通用"垃圾检测与分类的实验。
3.  **首个废物数据集综合评述**：提供了首个面向"垃圾检测"视角的现有废物数据集综合综述，对十余个数据集（TrashNet、Open Litter Map、Waste Pictures、TACO、Wade-AI、UAVVaste、TrashCan、Trash-ICRA19 等）的关键统计（图像数、标注类型等）进行了汇总（论文表 1）。
4.  **扩展标注 TACO 数据集**：对 TACO 约 3000 张未标注图像在"检测级别"提供了标注，累计得到超过 14000 个实例，并公开。
5.  **系统回顾检测/分类架构**：在相关工作中梳理了从 AlexNet/VGG/ResNet/Inception/DenseNet/ResNeXt/EfficientNet(v2) 到 ViT/DeiT/PVT/CvT 的分类骨干，以及从 R-CNN 系列、SSD、YOLO 系列、DETR/Deformable DETR、EfficientDet、Mask R-CNN 的检测/分割发展脉络。

## 方法

- **整体框架**：两阶段（two-stage）流程。第一阶段用一个**检测器**在输入图像中定位所有可能的废物目标（生成类别无关的边界框）；第二阶段用一个**分类器**对检测到的废物区域进行七类精细分类。
- **输入输出**：
    - 输入：单张包含废物的自然场景图像。
    - 输出：每个废物实例的边界框 + 对应的七类废物标签。
- **关键模块（据 p.13-19 提取摘录补充）**：
    1.  **检测器**：论文比较了多个检测架构，包含 **EfficientDet-D2（骨干 EfficientNet-B2）**、**Mask R-CNN（骨干 ResNet-50）** 与 **DETR（骨干 ResNet-50）**（对应论文 Table 4）。作者得出结论：**EfficientNet 网络家族是处理废物图像的优选**（EfficientDet 在其实验中表现更好）。
    2.  **分类器**：使用 **EfficientNet-B2** 作为分类网络（对应混淆矩阵 Fig 8 / Table 8 与分类器对比 Table 7）。
    3.  **半监督伪标签（pseudo-labeling）**：引入伪标签半监督学习技术（流程见论文 Figure 7），实验显示"每个 batch 更新一次伪标签"可略微提升准确率；并比较了不同的采样器（sampler，含 random / weighted sampler）。
- **模块连接**：检测器输出的废物区域候选框送入分类器，分类器对裁剪后的区域独立分类。
- **训练方式**：检测与分类分阶段训练；分类阶段引入伪标签半监督与不同采样策略（具体优化器/学习率等超参在提供文本中未完整列出）。
- **推理流程**：图像 → 检测器生成候选废物框 → 裁剪 → EfficientNet-B2 分类器分类 → 输出"框 + 七类标签"。
- **与已有方法的差异**：不同于只处理受控单一背景的智能垃圾桶方案，本方法面向野外图像；相比端到端检测分类，采用两阶段解耦设计，便于分别优化检测与分类，并便于复用伪标签等半监督技巧扩充训练数据。

## 实验

- **使用的数据集**：混合多个公开废物数据集训练/测试。明确提到为 TACO 的 3000+ 未标注图像补充检测级标注，累计超过 14000 个实例。综述部分给出的各数据集检测 mAP 区间参考：从 TACO+Mask R-CNN 的 15.9%，到 Trash-ICRA19+Faster R-CNN 的 81%（提取文本明确，作为领域对比基准）。
- **对比方法**：检测端对比 EfficientDet-D2(EfficientNet-B2) vs Mask R-CNN(ResNet-50) vs DETR(ResNet-50)（Table 4）；分类端在 Table 7 对比"所选分类器的准确率"（含不同 #classes、Accuracy、Sampler、Pseudo-labeling type 几列）。
- **评价指标**：检测用平均精度（Average Precision / mAP）；分类用准确率（Accuracy），并报告了 per-class 的 Precision / Recall / F1-score（Table 8 / Fig 8 混淆矩阵）。
- **主实验结果（摘要口径 + p.13-15 提取摘录）**：
    - 废物检测：测试集上**平均精度最高约 70%**。
    - 废物分类：摘要口径**约 75%**；提取摘录给出更细的数字——最佳准确率 **74.6%（random sampler）**；另有一处报告测试准确率 **73%**（训练集 86.7%，测试集约占 25%）；某一类别召回率达 **82%**、F1 达 **83%**（class balance 较好）。
    - 作者在结论中称这相比此前对部分数据集单独报告的结果是"优秀的"（an excellent result）。
- **消融/分析**：包含分类器对比（Table 7）、检测器对比（Table 4）、伪标签更新频率与采样器的对比；混淆矩阵分析（Fig 8 / Table 8）。完整数值表格在提供文本中未全部提取。
- **泛化实验**：未在提供文本中找到专门的跨域/跨数据集泛化实验。
- **效率信息（速度/参数量/FLOPs）**：提供文本未给出具体推理速度/参数量/FLOPs 数字（仅在相关工作中讨论 EfficientDet/EfficientNet 的效率动机）。

## 局限

1.  **超参细节不完整**：提供文本（p.1-12 完整 + p.13-19 摘录）未完整列出检测/分类的训练超参（优化器、学习率、数据增强配置等），完整复现需结合开源代码。
2.  **分类依赖检测**：两阶段框架的瓶颈在第一阶段——检测器漏检或定位不准会级联影响分类，错误传播无法在第二阶段挽回。
3.  **数据集偏置与跨域泛化**：混合数据集中 TACO 等存在众包带来的标签偏差（"是否算垃圾"依赖上下文）；废物场景在不同地域、文化下差异巨大，论文未报告系统的跨数据集泛化实验。
4.  **未评估实时性**：面向实际自动化分拣，推理速度关键，但提供文本未报告运行速度或计算成本（论文展望提到未来可结合机械臂用于废物管理）。
5.  **类别定义的地域性**：七类划分基于格但斯克的分拣规则，可能不完全适用于其他城市/国家。
6.  **绝对性能仍有限**：检测 AP 约 70%、分类约 73-75%，离落地可靠分拣仍有差距，且野外小目标（如 UAVVaste 中中位数 76×68px 的小垃圾）对检测仍是挑战。

## 个人评论

1.  **务实的工程导向与开源精神**：这是一个非营利项目（WiMLDS Trójmiasto 社区驱动），价值不在某个新算法，而在端到端打通"野外垃圾检测+七类分类"并完整开源，为后续研究提供可复现基线。
2.  **标准化分类定义有落地价值**：七类（尤其区分可回收/不可回收）直接对应市政分拣规则，比 TrashNet 的材质六类更贴近"实际怎么扔"。
3.  **数据集综述 + TACO 扩标是真实社区贡献**：对十余个废物数据集的统一统计（表 1）对新入坑者极有参考价值；为 TACO 补检测标注并公开，是可被他人直接复用的数据贡献。
4.  **方法选择有据**："EfficientNet 家族是处理废物图像的优选"这一结论由 EfficientDet vs Mask R-CNN vs DETR 的对比支撑，而非凭空选型；伪标签半监督的引入也针对"标注稀缺"这一现实痛点。
5.  **可改进处**：缺乏推理效率报告与跨域泛化评估，使"能否真正上分拣线"难以判断；绝对精度（检测约 70%）也说明野外垃圾检测远未解决。

### 使用建议

- **如果快速了解**：读摘要 + 引言最后一段（"This paper addresses..."）即可掌握七类定义、两阶段框架、综述与 TACO 扩标四个要点。
- **如果复现**：方法/结果细节在论文 Section 3 与 Table 4/7/8，但提供文本仅部分提取，务必结合开源仓库 `https://github.com/wimlds-trojmiasto/detect-waste`；起点配置可参考"EfficientDet-D2 + EfficientNet-B2 检测、EfficientNet-B2 分类、伪标签 + 采样器"。
- **如果借鉴创新点**：两阶段解耦设计、面向市政规则的类别定义方法论、混合 + 扩标（TACO 检测标注）+ 伪标签半监督扩充数据的组合策略。
- **如果写 Related Work**：可作为"野外废物/垃圾检测与分类"的代表性工作引用；其 Section 2 的分类/检测架构与废物数据集综述本身就是一份很好的资料库。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C2_目标检测_违建_车辆_船舶_行人]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中"目标检测 + 图像分类"的应用方向，聚焦自然环境中的废物（litter/waste）检测与分类。它是一个非营利社区项目（WiMLDS Trójmiasto），目标是从野外图像中自动定位并按市政可回收规则分类垃圾，以支撑更高效的回收与环境治理。归入"C2_目标检测_违建_车辆_船舶_行人"主题下的"特定物体（废物）检测"子类——废物与车辆/行人/船舶一样，是真实场景中需定位并归类的具体物体类别。

## 2. 一句话总结
本文构建并开源了一个"检测器（EfficientDet-D2/Mask R-CNN/DETR）+ EfficientNet-B2 分类器"的两阶段废物检测分类框架，配合伪标签半监督训练，在混合公开数据集上实现约 70% 检测 AP、约 73-75% 分类准确率，并贡献了首个废物数据集综述与对 TACO 的检测级扩标（14000+ 实例）。

## 3. 背景与问题
- **为什么要做**：年垃圾产量约 20 亿吨且指数增长，塑料污染严峻（每年人均摄入约 250 克微塑料，约 90% 来自饮用水）；分拣高度依赖人工，自动化分拣是刚需，深度学习提供了路径。
- **之前方法的问题**：
    1.  **场景受限**：智能垃圾桶只能在清晰单一背景下逐个分类，无法处理野外形变、多样背景的垃圾。
    2.  **定义模糊**：物体是否算"垃圾"取决于上下文，需明确判定边界。
    3.  **规则与数据分散**：分拣规则不统一；公开废物数据集在类别/场景/标注级别上各有缺口，缺乏面向可回收物的统一综述与标注。
- **核心矛盾**：野外复杂场景中如何同时做好"有效检测"与"可归类分类"，以支持落地分拣。

## 4. 核心贡献
1.  混合公开数据集并提出七类（bio/glass/metal and plastic/non-recyclable/paper/other/unknown）分拣标准，灵感来自格但斯克规则。
2.  开源两阶段框架（detector + classifier），作者称为首个支持通用垃圾检测+分类的实验。
3.  首个面向检测视角的废物数据集综合综述（十余个数据集，表 1）。
4.  对 TACO 约 3000 张未标注图像提供检测级标注，累计 14000+ 实例并公开。
5.  系统回顾分类骨干（AlexNet→EfficientNetv2、ViT/DeiT/PVT/CvT）与检测/分割架构（R-CNN 系列、SSD、YOLO 系列、DETR/Deformable DETR、EfficientDet、Mask R-CNN）。

## 5. 方法详解
- **整体框架**：两阶段。检测器先出类别无关候选框，分类器再做七类细分。
- **输入输出**：输入单张自然场景图；输出每个废物实例的框 + 七类标签。
- **检测器（Table 4 / p.13 摘录）**：对比 EfficientDet-D2(EfficientNet-B2)、Mask R-CNN(ResNet-50)、DETR(ResNet-50)，结论是 EfficientNet 家族（EfficientDet）更适合废物图像。
- **分类器**：EfficientNet-B2（混淆矩阵见 Fig 8 / Table 8，分类器对比见 Table 7）。
- **半监督**：伪标签（pseudo-labeling，Fig 7）+ 不同采样器（random / weighted）；每 batch 更新伪标签可略升准确率。
- **连接与推理**：检测框 → 裁剪 → EfficientNet-B2 分类 → 输出框+标签。
- **训练**：检测与分类分阶段训练；完整超参在提供文本中未全部给出，需查代码。
- **与已有方法差异**：面向野外（非受控背景），两阶段解耦便于分别优化并叠加半监督扩数据。

## 6. 实验与结果
- **数据集**：混合多个公开废物集；为 TACO 补检测标注得 14000+ 实例。综述给出领域 mAP 区间参考：TACO+Mask R-CNN 15.9% ~ Trash-ICRA19+Faster R-CNN 81%。
- **对比方法**：检测 Table 4（三种检测器）；分类 Table 7（不同 #classes/采样器/伪标签类型）。
- **指标**：检测 AP/mAP；分类 Accuracy + per-class Precision/Recall/F1（Table 8）。
- **主结果**：检测 AP 最高约 70%；分类摘要约 75%，提取摘录细化为最佳 74.6%（random sampler）、另一处测试 73%（训练 86.7%）、某类 recall 82% / F1 83%。作者称相比此前对部分数据集单独报告的结果是"优秀的"。
- **消融/分析**：检测器对比、分类器对比、伪标签更新频率与采样器对比、混淆矩阵分析。
- **泛化/效率**：提供文本未见系统跨域泛化实验，也未报告推理速度/参数量/FLOPs 的具体数字。

## 7. 这篇论文真正有价值的地方
1.  **端到端打通 + 开源基线**：野外垃圾"检测+七类分类"完整流程开源，复现门槛低。
2.  **面向市政规则的类别定义**：七类（区分可回收/不可回收）比材质六类更贴近实际分拣。
3.  **数据集综述 + TACO 扩标**：统一统计十余个数据集、为 TACO 补检测标注（14000+ 实例）是可直接复用的社区贡献。
4.  **有据的选型与半监督**：用 EfficientDet/Mask R-CNN/DETR 对比支撑"EfficientNet 家族更优"的结论；伪标签针对标注稀缺痛点。

## 8. 局限与问题
1.  训练超参细节在提供文本中不完整，完整复现需结合开源代码。
2.  两阶段瓶颈在检测，漏检/定位不准会级联影响分类。
3.  众包数据（TACO）存在标签偏差；缺系统跨数据集泛化实验。
4.  未报告推理速度/计算成本，落地实时性未知。
5.  七类基于格但斯克规则，地域适配性有限。
6.  绝对性能（检测约 70%、分类约 73-75%）距可靠分拣仍有差距，野外小目标仍难。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言最后一段。
- **复现**：方法/结果在 Section 3 与 Table 4/7/8，结合代码仓库 `https://github.com/wimlds-trojmiasto/detect-waste`；起点配置 = EfficientDet-D2(EfficientNet-B2) 检测 + EfficientNet-B2 分类 + 伪标签/采样器。
- **借鉴创新点**：两阶段解耦、面向规则的类别定义、混合+扩标+伪标签的数据策略。
- **写 Related Work**：作为野外废物检测分类代表作引用；Section 2 综述可直接当资料库。

## 10. 和其他论文的关系
本文核心技术（EfficientDet、Mask R-CNN、DETR、YOLO 系列、Faster R-CNN 等）与主题 `C2_目标检测_违建_车辆_船舶_行人` 下其他检测论文共享技术基础；区别在于检测目标是"废物"这一具体物体类别，与违建/车辆/船舶/行人属平行的"特定类别检测"应用。可视为通用目标检测 + 分类技术在环保/回收领域的特化落地，并额外贡献了数据集综述与 TACO 扩标。

## 11. 关键词
废物检测, 垃圾检测, litter detection, 目标检测, 两阶段框架, EfficientDet, EfficientNet, DETR, Mask R-CNN, 伪标签半监督, 废物分类, TACO, 数据集综述, 开源, 环境监测

## 12. 可信度说明
本笔记基于 PDF 提取文本：p.1-12 为完整提取（摘要、引言、相关工作——分类/检测/数据集三小节均完整），p.13-19 为补读阶段的关键摘录（含方法对比 Table 4、分类器对比 Table 7、混淆矩阵 Table 8/Fig 8、伪标签流程 Fig 7，以及结论/展望片段）。因此"方法详解""实验与结果"中的架构选型（EfficientDet-D2/EfficientNet-B2、Mask R-CNN/DETR + ResNet-50）、伪标签与采样器、74.6%/73%/82%/83% 等数字均有提取文本支撑；但完整结果表格的全部数值、训练超参、跨域泛化与效率指标在提供文本中不完整，相应处已标注"未明确/未找到"。本笔记为 AI 全文覆盖稿，非人工精读复核。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2021_Waste_detection_in_P.txt` (19/19 页; 原 AI 主体 12/19 + 全文补读 13-19); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。本次优化据 p.1-12 完整提取 + p.13-19 补读摘录重写，修复了乱码摘要与作者/题目字段，并据 Table 4/7/8 摘录补足了架构选型与分类指标。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-19; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-19。
- **提取情况**: 缺失页 7 页, 其中 7 页提取到可读文本。缺失页包含正文/附录内容, 其中约 4 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: APREPRINT - M AY17, 2021
- p.13: 3.3.2 Results
- p.15: Class name Precision Recall F 1-score
- p.15: 4 Conclusions and Future Work
- p.15: This is an excellent result comparing to other recent reports, that were presented for some of used datasets separately
- p.15: In the future with the assistance of DL models, it would be possible to mount robotic arms in waste management
- p.15: Additionally, the high precision of litter localization in a large variety of the environments, shows the possibility of
- p.15: 5 Acknowledgements
- p.16: References
- p.16: In Yoshua Bengio and Yann LeCun, editors, 3rd International Conference on Learning Representations, ICLR
- p.17: Kamalika Chaudhuri and Ruslan Salakhutdinov, editors, Proceedings of the 36th International Conference on

### 缺失页关键摘录

- p.13: Figure 7: Flowchart for pseudo-labeling semi-supervised learning technique.
- p.13: A comparison of the performance of two different neural networks is presented in Table 7. One of them is EfﬁcientNet-
- p.13: backbones are EfﬁcientNet-B2 for EfﬁcientDet-D2 and ResNet-50 for Mask RCNN or DETR (see Table 4). It leads
- p.13: to the conclusion, that the EfﬁcientNet networks family is a preferred choice to deal with waste images.
- p.13: The experiments showed that updating pseudo-labels every batch can slightly raise accuracy. Although the best-
- p.13: achieved accuracy was 74.6%, it was performed for a random sampler. While analyzing the confusion matrices of each
- p.13: we have achieved an accuracy of 73% (and 86.7% on the training set), while almost 25% of our dataset were test
- p.13: Although the confusion matrix clearly shows that most of the predictions are accurate (see Fig. 8, and Table 8), it
- p.14: recall value - 82%. The F 1-score metric for this class achieved the utmost result - 83%, which shows the balance
- p.14: Table 7: Comparison of accuracy of selected classiﬁers.
- p.14: Model # classes Accuracy Sampler Pseudo-labeling type
- p.14: Figure 8: Evaluation of the accuracy of a classiﬁcation in form of confusion matrix for EfﬁcientNet-B2, Weighted
<!-- AI_READING_NOTE_END -->
