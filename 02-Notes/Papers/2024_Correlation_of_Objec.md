---
title: Correlation of Object Detection Performance with Visual Saliency and Depth Estimation
authors:
  - "Matthias Bartolo"
  - "Dylan Seychell"
year: 2024
venue: "arXiv:2411.02844 (University of Malta)"
doi: 
pdf: [[2024_Correlation_of_Objec.pdf]]
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
extract_cache: .paper-cache/extracts/2024_Correlation_of_Objec.txt
---

# Correlation of Object Detection Performance with Visual Saliency and Depth Estimation

## 基本信息
- **PDF**: [[2024_Correlation_of_Objec.pdf]]
- **primary_topic**: `C_目标检测_通用与旋转框`
- **topics**: `C_目标检测_通用与旋转框`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Correlation of Object Detection Performance with Visual Saliency and Depth Estimation |
| **作者** | Matthias Bartolo; Dylan Seychell (University of Malta, Dept. of Artificial Intelligence) |
| **发表时间** | 2024 (arXiv:2411.02844v1, 2024-11-05, cs.CV) |
| **刊物/会议** | 预印本 (arXiv) |
| **DOI** | 未明确 (arXiv:2411.02844) |

## 摘要

> （清理后英文原文）As object detection techniques continue to evolve, understanding their relationships with complementary visual tasks becomes crucial for optimising model architectures and computational resources. This paper investigates the correlations between object detection accuracy and two fundamental visual tasks: depth prediction and visual saliency prediction. Through comprehensive experiments using state-of-the-art models (DeepGaze IIE, Depth Anything, DPT-Large, and Itti's model) on COCO and Pascal VOC datasets, we find that visual saliency shows consistently stronger correlations with object detection accuracy (mAρ up to 0.459 on Pascal VOC) compared to depth prediction (mAρ up to 0.283). Our analysis reveals significant variations in these correlations across object categories, with larger objects showing correlation values up to three times higher than smaller objects. These findings suggest incorporating visual saliency features into object detection architectures could be more beneficial than depth information, particularly for specific object categories. The observed category-specific variations also provide insights for targeted feature engineering and dataset design improvements, potentially leading to more efficient and accurate object detection systems.

> （中文翻译）随着目标检测技术不断演进，理解它与互补视觉任务之间的关系，对于优化模型架构与计算资源至关重要。本文研究目标检测精度与两项基础视觉任务——深度预测与视觉显著性预测——之间的相关性。通过在 COCO 与 Pascal VOC 数据集上使用一组最新模型（DeepGaze IIE、Depth Anything、DPT-Large 及 Itti 模型）进行系统实验，作者发现视觉显著性与目标检测精度的相关性始终更强（在 Pascal VOC 上 mAρ 最高达 0.459），高于深度预测（mAρ 最高 0.283）。分析揭示这些相关性在不同物体类别间差异显著：较大物体的相关值可达较小物体的约三倍。结论指出，将视觉显著性特征融入检测架构可能比深度信息更有益，尤其对特定物体类别；而观察到的类别差异为有针对性的特征工程与数据集设计提供了启示，有望带来更高效、更准确的检测系统。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：目标检测仍是计算机视觉的基础难题，尽管 YOLOv10 / YOLO11 / RT-DETR 等先进模型已达到可观精度，但在复杂场景下仍有局限。人类感知具有选择性注意（selective attention），机器同样依赖优先处理图像中特定区域的机制。理解深度估计、视觉显著性这类**互补视觉任务**与检测性能的关系，对优化模型架构、提升计算效率（论文还从可持续 AI 角度强调这一点）以及指导数据集设计都很关键。
- **之前方法的问题**：已有多任务学习研究（把检测与深度或显著性结合）通常只关注端到端性能，而**未分析这些任务之间底层的相关性**。因此无法判断哪类辅助信息对检测更有益，限制了更高效、更有针对性的模型设计。
- **核心问题**：在深度信息与视觉显著性信息中，哪一种与目标检测任务联系更紧密；这种联系又如何随物体类别、尺度与场景复杂度而变化。论文特别聚焦相关性在不同类别和尺度上的差异。
## 关键贡献

1.  **系统性相关性研究**：在 COCO 与 Pascal VOC 两个常用检测数据集上，系统量化目标检测真值与深度估计、视觉显著性预测两类任务的相关性（用皮尔逊相关系数）。
2.  **发现显著性相关性更强**：视觉显著性（DeepGaze IIE 在 Pascal VOC 上 mAρ 达 0.459）比深度预测（最高 0.283）与检测真值的相关性**始终更强**。
3.  **揭示尺度与类别的影响**：相关性强弱与物体尺度密切相关，**较大物体的相关值可达较小物体的约三倍**，且类别之间差异巨大（如长颈鹿 0.326 vs 电视 -0.034）。
4.  **提供实践见解**：结果为**特征工程**（在检测框架中引入显著性特征）和**数据集设计**（平衡物体尺度、类别与场景复杂度）提供经验证据。
## 方法

- **整体框架**：本文不提出新的检测网络，而是一个**实验性相关分析框架**。它测量现有预测模型（深度图 / 显著性图）的输出与物体分割掩码真值之间的相关性，以此推断哪类辅助任务与检测目标更"对齐"。
- **输入与输出**：
    - **输入**：检测数据集（COCO 2017 训练集、Pascal VOC 2012）的图像及其分割掩码标注，以及预训练的深度 / 显著性预测模型。
    - **输出**：每个物体类别上，预测图与该类别物体掩码真值之间的平均皮尔逊相关系数（mAρ）。
- **关键模块（4 个预测模型，深度 2 个 + 显著性 2 个）**：
    1.  **深度预测**：`Depth Anything`（鲁棒的单目深度预测基础模型）、`DPT-Large`（基于密集视觉 Transformer 的单目深度，含缓解特征粒度损失的技术）。
    2.  **视觉显著性预测**：`Itti 视觉注意力模型`（受早期灵长类视觉皮层行为/神经机理启发，基于强度/特征图、无需训练的经典模型）、`DeepGaze IIE`（基于深度学习、在显著性数据集上训练、可用多种 backbone 做注视点预测）。
- **数据集**：`COCO`（80 类、超过 200,000 张图、非标志性复杂场景，平均每图 3.5 类、7.7 个实例）和 `Pascal VOC`（20 类、超过 11,000 张图、物体相对更大）。两者都带分割掩码作为真值。
- **实验流程（算法 1）**：加载数据集标注并预处理 → 加载预测模型 → 对每张图像用模型推理出预测图 `p`，与掩码真值计算皮尔逊相关 `r`（公式 1）→ 对每个类别在所有图像上求相关性均值（公式 2），得到该类别相关性。
- **数学公式**：ρ = Cov(X,Y) / (σX·σY)（公式 1），衡量预测图与掩码真值的线性相关，与强度/尺度无关；mAρ 是对全部 C 个类别 ρ 求平均（公式 2），综合评价。
- **论文类型特化**：实验分析类论文，无新模块。价值在于用统一的相关性度量，量化"底层视觉任务 ↔ 检测目标"的统计关联，为后续多任务融合指明方向。
## 实验

- **数据集**：COCO 2017 训练集、Pascal VOC 2012。
- **被评估模型**：`Depth Anything`、`DPT-Large`（深度）、`Itti-Koch Model`、`DeepGaze IIE`（显著性）。
- **评价指标**：类别平均皮尔逊相关系数 mAρ；每图平均运行时间（秒）。硬件为 NVIDIA GeForce RTX 4070 GPU。
- **主实验结果（Table I，mAρ：Pascal VOC / COCO）**：
    | 模型 | 类型 | VOC mAρ | COCO mAρ | VOC 时间(s) | COCO 时间(s) |
    |---|---|---|---|---|---|
    | Depth Anything | 深度 | 0.273 | 0.125 | 0.020 | 0.029 |
    | DPT-Large | 深度 | 0.283 | 0.129 | 0.046 | 0.050 |
    | Itti-Koch | 显著性 | 0.280 | 0.130 | 0.030 | 0.065 |
    | DeepGaze IIE | 显著性 | **0.459** | **0.170** | 0.042 | 0.084 |
    | 平均 | — | 0.324 | 0.139 | 0.035 | 0.505* |
    - DeepGaze IIE（显著性）在两个数据集上 mAρ 都最高（VOC 0.459 / COCO 0.170）。
    - 深度模型中 `DPT-Large`（0.283/0.129）虽稍慢，却高于最快的 `Depth Anything`（0.273/0.125）。Itti-Koch（0.280/0.130）相对落后于深度学习显著性模型。
    - COCO 整体 mAρ 明显低于 Pascal VOC，作者归因于 COCO 的非标志性复杂场景（每图类别/实例多：COCO 仅 10% 图含单一类别，Pascal VOC 超过 60% 图含单一类别）。
    - *注：表中 COCO 平均时间 0.505 与各行（0.029~0.084）量级不一致，疑为原文排版/统计笔误（据提取文本，待核）。
- **类别细分结果（Table II，COCO 上 Depth Anything，整表 mAρ=0.125）**：相关性从高到低跨度极大——长颈鹿 0.326、飞机 0.310、停车计时器 0.304、大象 0.301、马 0.291……到底部 car -0.010、toaster -0.016、tv -0.034。较大物体（动物、车辆）得分明显高于小物体；常出现在背景中的物体（如电视）相关性最低，印证**物体尺度、位置与场景复杂度**对检测有效性的关键影响。
- **消融/跨域泛化**：未做专门的消融或跨域泛化实验；两数据集的对比本身充当了"数据集设计差异"的分析。
- **效率信息**：Table I 同时报告了各模型在两数据集上的每图平均推理时间。
## 局限

- **数据集范围有限**：仅 COCO 与 Pascal VOC，结论对其他领域（遥感、医学影像、特定自动驾驶场景）的适用性未验证。论文自身也将"数据集设计的重要性"列为讨论重点。
- **相关性是间接代理指标**：用"预测图 vs 掩码真值的皮尔逊相关"来代表辅助任务对检测的有用性，是间接度量；论文**未直接验证**把这些特征融入检测器后能否带来精度提升。
- **深度相关性偏低原因未深究**：只指出深度相关性较低，未区分是模型预测不准、任务本身关联弱，还是"与掩码求相关"这一评价方式本就不适合衡量深度对检测的贡献。论文同时承认深度仍有价值（区分大小物体、距离尺度，如 SODA 数据集场景）。
- **显著性模型的中心偏差**：论文明确指出 DeepGaze IIE 等显著性模型存在中心偏差（center bias），反映显著性估计的主观性，可能在 COCO 这类物体不居中的非标志性场景中影响评估公平性。
- **无下游任务验证**：结论停留在相关性层面，未把"更强的相关性"转化为"实际检测性能提升"，说服力受限。
## 个人评论

本文的价值在于提供了一个**轻量但具体的实证分析框架与一组量化基准**：在考虑用额外信息提升检测时，它给出了"显著性特征可能比深度信息更划算"的经验依据，尤其在复杂场景。其"类别/尺度相关性差异巨大"的发现很有启发性——意味着在模型设计或数据增广中，可针对检测难的类别（往往是小物体、常在背景中的物体）专门引入显著性先验，做**差异化特征工程**，这比笼统加一个深度分支更精准。

需要警惕的是方法学边界：相关性只是辅助任务与检测目标"对齐程度"的间接代理，不等于"加进去就能涨点"；而且显著性模型的中心偏差与 COCO 非标志性场景之间存在系统性张力，可能让 COCO 上的低 mAρ 部分来自评测偏置而非任务本身关联弱。作为引用，本文最适合作为"显著性 > 深度对检测更有益"这一动机的实证支撑，而不宜直接当作性能结论。

### 使用建议

- **快速了解**：读 Abstract 与 Conclusion（第 VI 节），最快把握核心发现。
- **复现或深入分析**：重点读 IV. Methodology（数据集、4 个模型、算法 1、公式 1/2）与 V. Evaluation（指标与 Table I / Table II）。Table I（模型对比）与 Table II（COCO 类别细分）是核心结果。
- **借鉴创新点**：
    - 学习其**系统性相关性分析**的实验设计，可迁移到其他视觉任务关系探索（分割↔检测、分类↔检测）。
    - 借鉴其**按类别/尺度细分**的诊断思路，定位自己模型的弱类别。
    - 将"**视觉显著性对检测有更强正相关**"作为引入显著性辅助模块的动机与引用依据。
- **写 Related Work**：可放入"目标检测与多任务学习"或"辅助任务（深度/显著性）与检测的关系"子部分，作为实证研究代表。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C_目标检测_通用与旋转框]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉 **目标检测** 方向，是一篇**实证相关性分析**论文（非新模型）。它量化目标检测真值与两类互补视觉任务——深度估计、视觉显著性预测——之间的统计相关性，为优化检测架构与计算资源分配提供经验指导。原笔记 frontmatter 主题为 "T_通用_NLP_其他"，与内容明显不符；本次已据正文改为 **C_目标检测_通用与旋转框**（通用目标检测）。

## 2. 一句话总结
通过在 COCO 与 Pascal VOC 上计算深度图/显著性图与物体掩码真值的皮尔逊相关，论文发现视觉显著性（DeepGaze IIE 在 VOC 上 mAρ=0.459）与检测目标的相关性始终强于深度预测（最高 0.283），且相关性随物体类别和尺度显著变化（大物体约为小物体的三倍）。

## 3. 背景与问题
- **为什么要做**：目标检测仍是 CV 基础难题，YOLOv10/YOLO11/RT-DETR 等已很强但在复杂场景受限。人类与机器都依赖选择性注意，理解深度、显著性这类互补任务与检测的关系，对优化架构、提升计算效率（含可持续 AI 视角）和数据集设计都重要。
- **之前方法的问题**：已有多任务学习把检测与深度/显著性结合，但只看端到端性能，**不分析任务间底层相关性**，因而无法判断哪类辅助信息对检测更有益。
- **核心问题**：深度 vs 显著性，哪一种与检测联系更紧；这种联系如何随物体类别、尺度、场景复杂度变化。

## 4. 核心贡献
1.  在 COCO 与 Pascal VOC 上系统量化检测真值与深度/显著性预测的相关性（皮尔逊相关）。
2.  发现显著性相关性始终更强：DeepGaze IIE 在 VOC 上 mAρ=0.459，高于深度最高的 DPT-Large（0.283）。
3.  揭示尺度/类别影响：大物体相关值约为小物体三倍；类别间差异巨大（长颈鹿 0.326 vs 电视 -0.034）。
4.  为特征工程（引入显著性特征）与数据集设计（平衡尺度/类别/复杂度）提供经验证据。

## 5. 方法详解
- **整体框架**：实验性相关分析框架，非新检测网络。度量预测图（深度/显著性）与物体分割掩码真值的皮尔逊相关，推断哪类任务与检测更"对齐"。
- **输入/输出**：输入为 COCO 2017 训练集 / Pascal VOC 2012 的图像与分割掩码标注、4 个预训练预测模型；输出为每类别的平均皮尔逊相关 mAρ。
- **4 个模型**：
    - 深度：`Depth Anything`（鲁棒单目深度基础模型）、`DPT-Large`（密集视觉 Transformer、缓解特征粒度损失）。
    - 显著性：`Itti 模型`（受灵长类视觉皮层启发、无需训练的经典模型）、`DeepGaze IIE`（深度学习、在显著性数据集上训练、可多 backbone 做注视点预测）。
- **数据集**：COCO（80 类、>200k 图、复杂非标志性场景，平均每图 3.5 类/7.7 实例）；Pascal VOC（20 类、>11k 图、物体更大）。均带分割掩码真值。
- **算法 1（流程）**：加载并预处理标注→加载模型→逐图推理出预测图 p，与真值算皮尔逊相关 r→每类在所有图上求均值→输出每类相关性。
- **公式**：ρ=Cov(X,Y)/(σXσY)（式 1，线性相关、与强度/尺度无关）；mAρ=(1/C)·Σ_c ρ_c（式 2，跨类别平均）。

## 6. 实验与结果
- **设置**：COCO 2017 训练集、Pascal VOC 2012；指标 mAρ + 每图运行时间；硬件 RTX 4070。
- **Table I（VOC / COCO 的 mAρ）**：Depth Anything 0.273/0.125；DPT-Large 0.283/0.129；Itti-Koch 0.280/0.130；DeepGaze IIE **0.459/0.170**；平均 0.324/0.139。
    - DeepGaze IIE（显著性）两数据集都最高；DPT-Large 虽稍慢但高于最快的 Depth Anything；Itti-Koch 落后于深度学习显著性模型。
    - COCO 整体远低于 VOC，作者归因于 COCO 复杂非标志性场景（COCO 仅 10% 图单类别，VOC >60% 单类别）。
- **Table II（COCO 上 Depth Anything 的逐类相关，整表 mAρ=0.125）**：长颈鹿 0.326、飞机 0.310、停车计时器 0.304、大象 0.301……至底部 car -0.010、toaster -0.016、tv -0.034。大物体（动物/车辆）显著高于小物体；常在背景的物体（如电视）最低。
- **效率**：Depth Anything 在 COCO 最快（0.029 s/图）。
- **消融/跨域**：未做专门消融或跨域泛化；以两数据集对比充当数据集差异分析。
- **注**：Table I 中 COCO 平均时间 0.505 与各行量级不符，疑为原文笔误（据提取文本，待核）。

## 7. 这篇论文真正有价值的地方
提供了一个轻量、可复现的**实证基准**：在用额外信息提升检测时，"显著性特征比深度信息更划算"有了量化依据，尤其在复杂场景。"类别/尺度相关性差异巨大"的发现指向**差异化特征工程**——对难检类别（小物体、背景物体）专门引入显著性先验，比笼统加深度分支更精准。

## 8. 局限与问题
- **数据集范围有限**：仅 COCO + Pascal VOC，对遥感/医学/特定自动驾驶等的适用性未验证。
- **相关性是间接代理**：未直接验证把特征融入检测器能否真正涨点。
- **深度低相关原因未深究**：未区分是模型不准、任务关联弱，还是"与掩码求相关"这一评价方式不适配；论文也承认深度对区分物体大小/距离仍有价值（如 SODA 场景）。
- **显著性中心偏差**：DeepGaze IIE 等存在 center bias，与 COCO 非标志性场景存在系统性张力，可能让 COCO 低 mAρ 部分来自评测偏置。
- **无下游验证**：结论停在相关性层面，未转化为实际检测提升。

## 9. 我该怎么使用这篇论文
- **快速了解**：读 Abstract + Conclusion（第 VI 节）。
- **复现/深入**：读 IV. Methodology（数据集、4 模型、算法 1、式 1/2）与 V. Evaluation（Table I 模型对比、Table II 类别细分）。
- **借鉴**：迁移其系统性相关分析设计到其他任务关系探索；借鉴按类别/尺度细分诊断弱点；把"显著性 > 深度对检测更有益"作为引入显著性模块的动机与引用依据。
- **写 Related Work**：放入"目标检测 + 多任务学习"或"辅助任务（深度/显著性）与检测关系"子部分，作为实证研究代表。

## 10. 和其他论文的关系
- 与**显著性引导/注意力机制的目标检测**相关（作者自引 arXiv:2408.06803，把显著性排序与强化学习结合用于增强检测）。
- 与**小目标检测**相关：本研究发现小物体与视觉任务相关性较弱，呼应小目标检测之难，并提示增强小目标显著性特征的改进方向（参考文献含 SODA、small object detection 等工作）。
- 引用了 YOLOv10 / YOLO11 / RT-DETR 等最新检测器作为背景，可与这些方法的笔记互链。

## 11. 关键词
目标检测，深度预测，视觉显著性，相关性分析，皮尔逊相关系数 (mAρ)，COCO，Pascal VOC，多任务学习，特征工程，数据集设计，物体尺度，中心偏差

## 12. 可信度说明
本精读笔记**完全基于 PDF 提取文本（6/6 页）生成**，覆盖摘要、引言、背景、相关工作、方法、评估、讨论与结论，以及 Table I、Table II 的完整数值。提取文本清晰完整（约 4173 字符/页），核心逻辑、实验设置与关键数字均可核验，可信度高。本次复核纠正了原笔记的标题截断、venue（误填为邮箱）与主题分类错误（T_通用_NLP_其他 → C_目标检测_通用与旋转框），并补全了 Table I 完整四模型数值、COCO/VOC 单类别占比、算法流程与公式细节。提取缓存仅到参考文献前段，完整参考文献列表未覆盖，但不影响对核心贡献的理解。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 4173 字符/页, 6/6 页); 来源缓存: `.paper-cache/extracts/2024_Correlation_of_Objec.txt`; 生成日期: 2026-06-04; 复核日期: 2026-06-18; 模式: LLM (mimo-v2.5-pro) + 人工对照提取文本复核。
<!-- AI_READING_NOTE_END -->
