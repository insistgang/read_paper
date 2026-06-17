---
title: "Attention Neural Network for Trash Detection on Water Channels"
authors:
  - "Mohbat Tharani"
  - "Abdul Wahab Amin"
  - "Mohammad Maaz"
  - "Murtaza Taj"
year: 2020
venue: "arXiv (arXiv:2007.04639)"
doi: 
pdf: [[2020_Attention_Neural_Net.pdf]]
primary_topic: B_注意力算子模块
topics:
  - "B_注意力算子模块"
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
extract_cache: .paper-cache/extracts/2020_Attention_Neural_Net.txt
---

# Attention Neural Network for Trash Detection on Water Channels

## 基本信息
- **PDF**: [[2020_Attention_Neural_Net.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Attention Neural Network for Trash Detection on Water Channels |
| **作者** | Mohbat Tharani; Abdul Wahab Amin; Mohammad Maaz; Murtaza Taj |
| **单位** | Computer Vision and Graphics Lab, Lahore University of Management Sciences, 巴基斯坦拉合尔 |
| **发表时间** | 2020 |
| **刊物/会议** | arXiv preprint (arXiv:2007.04639v1, 2020-07-09, cs.CV) |
| **DOI** | 未明确 |

## 摘要

> **英文原文（据 PDF 提取整理）**: Rivers and canals flowing through cities are often used illegally for dumping trash. This contaminates fresh water channels as well as causes blockage in sewerage resulting urban flooding. When this contaminated water reaches agricultural fields, it results in degradation of soil and poses critical environmental as well as economic threats. The dumped trash is often found floating on the water surface. The trash could be disfigured, partially submerged, decomposed into smaller pieces, clumped together with other objects which obscures its shape and creates a challenging detection problem. This paper proposes a method for detection of visible trash floating on the water surface of the canals in urban areas. We also provide a large dataset, first of its kind, *trash in water channels* that contains object level annotations. A novel attention layer is proposed that improves the detection of smaller objects. Towards the end of this paper, we provide a detailed comparison of our method with state-of-the-art object detectors and show that our method significantly improves the detection of smaller objects. The dataset will be made publicly available.

> **中文翻译**: 流经城市的河流与运河常被非法用于倾倒垃圾。这既污染了淡水水道，又造成下水道堵塞、引发城市内涝。当这些污染水体流入农田时，会导致土壤退化，带来严重的环境与经济威胁。被倾倒的垃圾往往漂浮在水面，可能已变形、部分淹没、分解成更小的碎片，或与其他物体纠缠在一起，从而遮蔽其形状，构成一个极具挑战性的检测问题。本文提出一种用于检测城市运河水面可见漂浮垃圾的方法。我们还提供了首个此类大规模数据集 *trash in water channels*，包含物体级标注。论文提出一种新颖的注意力层，可改善对小物体的检测。文末我们将所提方法与当前最先进的目标检测器进行了详尽对比，结果表明本方法显著提升了对小物体的检测能力。该数据集将公开发布。

> **关键词（Index Terms）**: Object Detection, Smaller Objects, Attention, Water Quality, Urban Trash。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：城市河流和运河被非法倾倒垃圾，污染淡水、堵塞下水道引发城市内涝，污水流入农田后会退化土壤、降低肥力、危害作物。论文引用数据指出，发展中国家 90% 的污水和 70% 的工业废弃物未经处理直接排入当地水道（[1]），联合国世界水资源发展报告（[2]）称每年约 350 万人（多为儿童）死于水相关感染。要量化水体污染、通知规划部门采取行动，检测水面可见漂浮垃圾是关键的第一步。
- **之前方法的问题**：现有基于视觉的垃圾检测可分为三类：1) 受控环境（回收厂）中的垃圾分类（[3,4]）；2) 城市中非法倾倒的成堆垃圾检测（[5,6]）；3) 街道垃圾或海洋垃圾等稀疏垃圾检测（[7-10]）。本文提出**第四类**——检测排水/淡水运河水面上的漂浮垃圾，**此前没有任何针对该问题的研究和数据集**。此外，主流深度目标检测器（SSD、YOLO、Faster R-CNN）是为监控、自动驾驶等通用城市场景设计的，在 MS-COCO、Pascal-VOC 上表现良好，但在水道这种**物体形状随水流变化、尺寸跨度极大**的场景下表现不佳。
- **核心矛盾**：物体尺寸变化大、小目标占比高，是该任务的主要瓶颈。论文指出已有应对尺寸变化的手段（图像金字塔 [18]、特征融合网络 [19,20]、Thinned U-shape Modules（TUM）[21]、注意力机制 [22,23]）仍不足以处理水面小垃圾，需要一种**隐式聚焦于小物体**的方法。
## 关键贡献

1.  **提出新的检测类别**：首次将"城市运河水面漂浮可见垃圾"的检测定义为一个独立的（第四类）问题类别。
2.  **发布首个数据集**：贡献了首个该场景的人工采集与标注数据集（trash in water channels）。共 **13,500 张图像**、**48,898 个物体级标注**（边界框，VOC 格式，用 LabelImg 标注），物体面积约从 256 px² 到 300,000 px² 不等。数据采集自巴基斯坦拉合尔商业区、贫民区、工业区附近共 **5 个关键站点**，录制了 30 段最长 60 分钟的视频，按固定间隔抽帧标注。
3.  **设计新颖的对数注意力层**：提出一种基于对数（log）激活的注意力层，利用对数对偏态数据"压缩大值、放大小值"的特性，**隐式增强特征图中小物体的低响应**，以缓解小目标检测难题。
4.  **系统实证对比**：在 SSD、YOLO-v3-Tiny、YOLO-v3、PeleeNet、RetinaNet（含 ResNet50 变体）等多个 SOTA 检测器上集成该注意力层，并在自建数据集（按小/中/大三类尺寸）上对比验证其对小物体检测精度的提升。
## 方法

- **整体框架**：基于现成目标检测器（YOLO-v3、PeleeNet、RetinaNet 等），核心改动是在检测器的**骨干网络（backbone）** 中插入自定义的**对数注意力层**（见原文图 4：左侧 backbone 被修改以引入注意力层，右侧为检测头）。
- **输入输出**：输入为水道场景 RGB 图像；输出为漂浮垃圾的边界框及置信度。
- **关键模块：对数注意力层（公式 1）**
    - **公式**：`f_{i+1} = f_i · log(ReLU(f_i) + 1)`，其中 `f_i` 是第 i 层输出，i = 0,…,N，N 为层数。`ReLU` 丢弃激活中的负值，偏置 `+1` 将其上移一个尺度以保证可取对数。原文还给出了该层的导数（公式 2）：当 `f_i ≥ 0` 时为 `log(f_i+1) + f_i/(f_i+1)`，否则为 1。
    - **直观解释**：传统注意力用 Sigmoid 或 Softmax 预测特征的 objectness 概率，擅长分割物体边界附近的像素；但本文需要的是隐式聚焦小物体的激活函数。对数尺度用于**克服数据偏态**——当少数值远大或远小于其余值时，对数可把大范围压成小范围，从而**降低特征方差、放大较小的值**，进而强调小物体。
    - **作用位置**：该层施加于**多分辨率（multi-resolution）特征**上。由于 backbone 学到的特征决定了检测器的上限，放大 backbone 中小物体的低激活值能驱动整体检测性能提升；更新后的特征还被前传回 backbone 的前一层，以逐步改进特征学习（原文图 5 的激活可视化显示对小物体特征学习有明显改善）。论文称该层引入了"数值稳定性"，对因物体尺寸差异巨大造成的特征不均匀做出响应。
- **训练方式**：所有网络用各自**默认超参数与 API**，并以 **Pascal VOC 预训练权重**初始化。12,500 张训练-验证图像按 **80%/20%** 随机划分（训练/验证），划分对所有模型固定。**测试集来自与训练-验证不同的站点**，共 1000 张，再分为 Easy / Hard 各 500 张。
- **与已有方法的差异**：不同于使用 Sigmoid/Softmax 的通用注意力，本文用对数变换直接针对"特征值分布偏态、小物体激活值过低"的问题设计。
## 实验

- **使用的数据集**：自建 trash in water channels（13,500 张标注图像）。测试集分 **Easy Test Set**（500 张，不同天气与水面纹理，部分采于雨天；训练集中无雨天样本）和 **Hard Test Set**（500 张，多样视角、天气、水色与气泡）。
- **对比方法**：SSD、YOLO-v3-Tiny、YOLO-v3、PeleeNet、RetinaNet、RetinaNet-resnet50（各有 +Attn 变体）。
- **评价指标**：平均精度（Average Precision, AP）与交并比（Intersection over Union, IoU），口径同 MS-COCO。
- **主实验结果**（Table 2，AP / IoU）：
    - **Easy Test Set 最高 AP** 为 **RetinaNet-resnet50+Attn = 52.6**，其次 **RetinaNet+Attn = 51.8**；YOLO-v3+Attn = 48.1（高于 vanilla YOLO-v3 的 43.8）。原文文字强调"在 Easy 集上 YOLO-v3+Attn 超过其余模型、AP 达 48.1%"，但其表 2 数据里 RetinaNet 系的 +Attn 实际更高，叙述与表存在不一致（以表为准）。
    - **Hard Test Set 最高 AP** 为 **RetinaNet+Attn = 43.9** 与 **RetinaNet-resnet50+Attn = 43.9** 并列；vanilla RetinaNet-resnet50 = 48.5（注：这是无注意力版，是 Hard 集整体最高，但加注意力后反而降到 43.9）。YOLO-v3+Attn 在 Hard 集上（31.2）与 vanilla YOLO-v3（31.5）基本持平。
    - SSD 与 YOLO-v3-Tiny 学习失败、AP 很低（YOLO-v3-Tiny Hard 仅 11.6，为最低）。各模型 IoU 接近（约 64%–74%）。
- **小物体检测分析**（Table 3，按 S/M/L 分尺寸 AP）：
    - 所有模型在小物体（S，面积 < 32² px²）上的 AP 远低于中、大物体。
    - **Easy 集小物体**：RetinaNet+Attn = **6.3**、PeleeNet+Attn = **6.2**，均高于各自原版（RetinaNet 5.0、PeleeNet 5.5）；YOLO-v3+Attn = 5.4（高于 vanilla 4.5）。
    - **Hard 集小物体**：**PeleeNet+Attn = 9.0**（全表小物体最高，远超 vanilla PeleeNet 的 1.9）；RetinaNet+Attn = 4.1（高于 vanilla 4.0）。
    - 论文解释：大物体仅 4692 个（约为小物体数量的一半）却仍能被检出，是因为模型在 Pascal VOC 上预训练保留了对大物体的"objectness"先验。
- **消融/效率实验**：PDF 文本未提供参数量、FLOPs 或运行速度的对比信息（PDF 文本未明确）。
## 局限

1.  **场景局限**：仅检测**水面漂浮**垃圾。论文明确**不标注**微颗粒、树叶、树枝、非漂浮（沉没）垃圾和气泡；宽高均小于 7 像素的物体也不标注。微颗粒会被建议用纹理分析而非目标检测处理，故被排除。完全沉没/贴岸/已分解为微粒的垃圾不在方法覆盖范围内。
2.  **数据集规模与地域**：13,500 张相对 MS-COCO 等仍偏小，且全部来自拉合尔的 5 个站点，地理与场景多样性有限，泛化能力存疑。
3.  **方法验证深度不足**：未对对数注意力层的各组件（ReLU、+1、log）做消融，也未分析其计算开销。注意力对部分模型在 Hard 集上甚至带来性能下降（如 RetinaNet-resnet50 由 48.5 降到 43.9），论文未深入解释这种不稳定性。
4.  **性能瓶颈仍存**：即便加注意力，小物体 AP 仍极低（Easy 集最高 6.3、Hard 集最高 9.0），表明这仍是开放难题，提升幅度有限。
5.  **表述与数据不一致**：正文对"哪个模型最佳"的叙述与 Table 2 的数值存在出入（见实验小节），削弱了主结论的清晰度。
## 个人评论

1.  **问题定义的价值**：敏锐识别并定义了一个有现实意义却被忽视的 CV 应用场景（城市水道垃圾检测），开辟了"第四类垃圾检测"这一新方向。
2.  **数据集贡献**：从零构建并承诺公开首个该场景数据集，覆盖反光、气泡、形变等特有挑战，可作为后续基准。
3.  **简洁的算子级创新**：对数注意力层从函数性质（压缩大值、放大小值、降低方差）出发解决"小目标激活过低"这一具体痛点，几乎零额外结构、易于实现。"用简单算子针对特定数据分布问题"的思路值得借鉴——这也是本文归入 `B_注意力算子模块` 的核心理由。
4.  **诊断式实验设计的启示**：除整体 AP 外，论文按物体尺寸（S/M/L）分层评估，有助于定位模型瓶颈，是模型诊断的良好范式。
5.  **批判性看待**：注意力层并非对所有 backbone 都有正收益（RetinaNet-resnet50 在 Hard 集上反而下降），加上正文与表格的数值出入，说明该算子的有效性带有数据/模型依赖性，并非普适增益。

### 使用建议

- **如果快速了解**：读摘要与结论，浏览图 2（挑战场景）、图 3（注意力层与激活函数）、表 2/3（整体与分尺寸 AP）。
- **如果复现**：精读第 2 节（数据集采集/标注/划分：5 站点、30 视频、13,500 图、48,898 框、80/20 划分、测试集异站点）与第 3 节方法（公式 1/2、图 4 集成方式）。需自行获取 YOLO-v3、PeleeNet、RetinaNet 等实现。
- **如果借鉴创新点**：把"针对偏态特征用对数算子放大小值"迁移到其他存在特征分布不均的检测任务；同时注意其对不同 backbone 收益不稳定，需自做消融。
- **如果写 related work**：可置于"特定场景（水环境）垃圾/物体检测"与"面向小目标检测的注意力机制"两个子类别下。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉的**目标检测（Object Detection）**方向，核心方法贡献是一个**算子级的注意力模块（对数注意力层）**，并附带一个全新的应用场景与数据集——**城市运河水面漂浮垃圾检测**。论文将该任务定义为继"回收厂垃圾分类 / 城市垃圾堆检测 / 街道与海洋稀疏垃圾检测"之后的**第四类**垃圾检测问题。鉴于论文标题即"Attention Neural Network"、其最可迁移的创新是对数注意力算子本身，本笔记将主题由原先的 `T_通用_NLP_其他`（明显误归，该论文与 NLP 无关）修正为 `B_注意力算子模块`。

## 2. 一句话总结
本文提出一个对数（log）注意力层，通过"压缩大值、放大小值"的对数变换隐式增强特征图中小物体的低响应，并配套发布首个城市运河漂浮垃圾检测数据集（13,500 图 / 48,898 框），在多种 SOTA 检测器上验证了其对小物体检测的提升。

## 3. 背景与问题
- **动机**：城市水道非法倾倒垃圾导致水污染、下水道堵塞、城市内涝和农田土壤退化。论文援引：发展中国家 90% 污水、70% 工业废弃物未处理直排水道；每年约 350 万人（多为儿童）死于水相关感染。量化水体垃圾、通知规划部门，第一步就是检测水面可见漂浮垃圾。
- **空白**：此前没有任何针对淡水/废水运河漂浮垃圾的研究与数据集；该问题不同于海洋垃圾（水色、反光、气泡、城市建筑/飞鸟倒影等都更复杂）。
- **技术难点**：物体随水流变形、无固定几何形状、尺寸跨度极大且小目标占比高。已有的图像金字塔、特征融合（FPN）、TUM、注意力等手段仍不能很好处理水面小垃圾，需要一个**隐式聚焦小物体**的机制。

## 4. 核心贡献
1.  **新问题类别**：定义"运河水面漂浮可见垃圾检测"为第四类垃圾检测问题。
2.  **首个数据集**：trash in water channels，13,500 图、48,898 框（VOC 格式，LabelImg 标注），面积 256–300,000 px²；采自拉合尔 5 个站点、30 段（≤60 min）视频；按 MS-COCO 标准分小（<32²）/中（32²–96²）/大（>96²）三类，小+中占比超 90%（小 11090、中 33116、大 4692）。
3.  **对数注意力层**：`f_{i+1} = f_i · log(ReLU(f_i)+1)`，零额外可学习结构，针对偏态特征放大小值、降方差。
4.  **系统对比**：在 SSD / YOLO-v3-Tiny / YOLO-v3 / PeleeNet / RetinaNet(+resnet50) 上集成并按尺寸分层评测。

## 5. 方法详解
- **框架**：在检测器 backbone 中插入对数注意力层（图 4：左 backbone 改造、右检测头）。
- **公式（式 1）**：`f_{i+1} = f_i · log(ReLU(f_i) + 1)`，ReLU 去负值、`+1` 保证对数可计算且整体上移一个尺度。导数（式 2）：`f_i ≥ 0` 时为 `log(f_i+1) + f_i/(f_i+1)`，否则为 1。
- **为何用对数**：Sigmoid/Softmax 注意力擅长物体边界分割，但本文要隐式聚焦小物体。对数把宽分布压成窄分布、降低特征方差、放大小值，恰好抬升小物体的低激活，并带来数值稳定性。
- **施加位置**：作用于**多分辨率特征**；放大 backbone 中小激活以驱动检测头；更新特征前传回 backbone 前一层逐步精炼（图 5 激活可视化显示小物体特征学习改善）。
- **训练**：默认超参/API，Pascal VOC 预训练初始化；12,500 图按 80/20 划分训练/验证，划分对所有模型固定；测试集取自不同站点的 1000 图（Easy/Hard 各 500）。

## 6. 实验与结果
- **数据/指标**：自建数据集；AP 与 IoU（MS-COCO 口径）。
- **整体 AP（Table 2）**：
    - Easy 集最高 = RetinaNet-resnet50+Attn **52.6**，次高 RetinaNet+Attn **51.8**，YOLO-v3+Attn 48.1（vanilla 43.8）。原文文字称 YOLO-v3+Attn 在 Easy 集最佳（48.1），与表中 RetinaNet 系更高的数值不一致——**以表为准**。
    - Hard 集：RetinaNet+Attn 与 RetinaNet-resnet50+Attn 并列 **43.9**；vanilla RetinaNet-resnet50 = 48.5（Hard 集整体最高，但加注意力后下降）；YOLO-v3+Attn 31.2 ≈ vanilla 31.5。
    - SSD、YOLO-v3-Tiny 学习失败（YOLO-v3-Tiny Hard AP 仅 11.6，最低）；各模型 IoU 接近（约 64–74%）。
- **分尺寸 AP（Table 3）**：所有模型小物体 AP 远低于中/大。
    - Easy 小物体：RetinaNet+Attn **6.3**、PeleeNet+Attn **6.2**（均高于原版 5.0、5.5）。
    - Hard 小物体：PeleeNet+Attn **9.0**（全表小物体最高）、RetinaNet+Attn 4.1（vanilla 4.0）。
    - 大物体虽只有 4692 个仍能被检出，归因于 Pascal VOC 预训练保留的大物体 objectness 先验。
- **效率/消融**：PDF 文本未给出参数量/FLOPs/速度，也无组件级消融（PDF 文本未明确）。

## 7. 这篇论文真正有价值的地方
1.  **问题定义**：识别并定义了被忽视的现实 CV 场景（运河漂浮垃圾），开辟"第四类垃圾检测"。
2.  **数据集**：首个该场景数据集，覆盖反光、气泡、倒影、形变等特有挑战，可作基准。
3.  **算子创新**：对数注意力层以极低成本针对"小物体激活过低"的具体痛点，思路简洁可迁移。
4.  **诊断式评测**：按物体尺寸分层评估，暴露小目标瓶颈，是良好的模型诊断范式。

## 8. 局限与问题
1.  **覆盖范围**：仅检测水面漂浮垃圾；明确不标注微颗粒、树叶树枝、非漂浮/沉没垃圾、气泡，以及宽高均 <7 px 的物体；沉没/微粒垃圾不在范围内。
2.  **规模与地域**：13,500 图偏小且全来自拉合尔 5 站点，泛化性存疑。
3.  **收益不稳**：注意力对部分 backbone 反而降分（RetinaNet-resnet50 Hard 48.5→43.9），且无组件消融、无开销分析。
4.  **瓶颈仍在**：小物体 AP 仍极低（Easy 最高 6.3、Hard 最高 9.0）。
5.  **正文与表格不一致**：对"最佳模型"的叙述与 Table 2 数值出入，削弱主结论清晰度。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要+结论，看图 2/3、表 2/3。
- **复现**：精读第 2 节（5 站点、30 视频、13,500 图、48,898 框、80/20 划分、异站点测试集）与第 3 节（式 1/2、图 4 集成方式）；需自备检测器实现。
- **借鉴**：把"对偏态特征用对数算子放大小值"迁移到其他特征分布不均的检测任务，并自做消融验证其稳定性。
- **写 related work**：归入"水环境垃圾/物体检测"与"面向小目标的注意力机制"。

## 10. 和其他论文的关系
本文与库内主题最直接相关的是 [[B_注意力算子模块]]（其核心是一个注意力算子）。延伸关联方向：
- 通用目标检测器改进（SSD [11]、YOLO-v3 [12,14]、Faster R-CNN [13]、RetinaNet/Focal Loss [20]、PeleeNet [15]）。
- 应对尺寸变化的结构：图像金字塔 [18]、FPN [19]、TUM/M2Det [21]。
- 注意力机制：Attention Augmented Conv [22]、Attention Is All You Need [23]——本文与之的差异在于用对数激活替代 Sigmoid/Softmax，目标是放大小物体而非分割边界。

## 11. 关键词
对数注意力, 注意力算子, 小目标检测, 目标检测, 水道垃圾, 环境监测, 城市水质, 数据集, 深度学习, YOLO/RetinaNet/PeleeNet

## 12. 可信度说明
本精读基于 PDF 提取文本（6/6 页，提取完整：含摘要、引言、数据集、方法、结果、结论、参考文献）。所有方法公式（式 1/2）、数据集统计（13,500 图、48,898 框、小/中/大 = 11090/33116/4692）、AP/IoU 数值均直接来自 Table 1/2/3 文本。本轮重读修正了原笔记的两处关键错误：(a) Easy 集最高 AP 实为 RetinaNet-resnet50+Attn 52.6 而非 YOLO-v3+Attn 48.1；(b) Hard 集小物体最高 AP 为 PeleeNet+Attn 9.0（原笔记遗漏），并指出正文叙述与 Table 2 存在不一致。未在文本中出现的信息（参数量/FLOPs/速度/组件消融）已标注为"PDF 文本未明确"。主题由 `T_通用_NLP_其他` 修正为 `B_注意力算子模块`。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 6/6 页完整, 含全部表格数值); 来源缓存: `.paper-cache/extracts/2020_Attention_Neural_Net.txt` (6/6 页); 生成日期: 2026-06-04; 本轮重读: 2026-06-18 (修正 Table 2/3 数值与主题分类); 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
