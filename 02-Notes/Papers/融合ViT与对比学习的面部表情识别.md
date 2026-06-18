---
title: 融合ViT与对比学习的面部表情识别 (Combining ViT with contrastive learning for facial expression recognition)
authors:
  - "崔鑫宇"
  - "何翀"
  - "赵宏珂"
  - "王美丽"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.230043
pdf: [[融合ViT与对比学习的面部表情识别.pdf]]
primary_topic: J_人脸_表情_伪造_情感
topics:
  - "J_人脸_表情_伪造_情感"
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/融合ViT与对比学习的面部表情识别.txt
---

# 融合ViT与对比学习的面部表情识别 (Combining ViT with contrastive learning for facial expression recognition)

## 基本信息
- **PDF**: [[融合ViT与对比学习的面部表情识别.pdf]]
- **primary_topic**: `J_人脸_表情_伪造_情感`
- **topics**: `J_人脸_表情_伪造_情感`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 融合 ViT 与对比学习的面部表情识别 (Combining ViT with contrastive learning for facial expression recognition) |
| **作者** | 崔鑫宇; 何翀; 赵宏珂; 王美丽 (西北农林科技大学信息工程学院) |
| **发表时间** | 2024, 第 29 卷第 1 期, 0123-0133 |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics) |
| **DOI** | 10.11834/jig.230043 |

## 摘要

**英文原摘要 (清理后)**:

> **Objective** Facial expression is one of the important factors in human communication to help understand the intentions of others. The task of facial expression recognition is to output the category of facial expression corresponding to a given face picture. Facial expression has broad applications in areas such as security monitoring, education, and human-computer interaction. Currently, facial expression recognition under uncontrolled conditions suffers from low accuracy due to factors such as pose variations, occlusions, and lighting differences. Self-supervised learning leverages a large amount of unlabeled data and extracts the prior knowledge distribution of the images themselves to improve the performance of downstream tasks. Contrastive learning belongs to self-supervised learning, which can further learn the intrinsic consistent feature information between similar images under the change of posture and light by increasing the difficulty of the task. This paper proposes an unsupervised contrastive learning-based facial expression classification method to address the problem of low accuracy caused by occlusion, pose variation, and lighting changes.
> **Method** The method consists of two stages: contrastive learning pretraining and model fine-tuning. In the pretraining stage, an unsupervised contrastive loss is introduced to reduce the distance between images of the same type and increase the distance between images of different classes. The method adds positive sample pairs for contrastive learning between the original images and occlusion-augmented images, enhancing the robustness of the model to image occlusion and illumination changes. Additionally, a dictionary mechanism is applied to MoCo v3 to overcome the issue of insufficient memory during training. The recognition model is pretrained on the ImageNet dataset, then fine-tuned on the facial expression recognition dataset. The Transformer-based vision Transformer (ViT) network is employed as the backbone network to enhance the model's feature extraction capability.
> **Result** Experiments were conducted on four datasets and compared with the latest 13 methods. On RAF-DB, compared with Face2Exp, the recognition accuracy increased by 0.48%; on FERPlus, compared with KTN, accuracy increased by 0.35%; on AffectNet-8, compared with SCN, accuracy increased by 0.40%; on AffectNet-7, compared with DACL, accuracy was slightly lower by 0.26%, which proves the effectiveness of the method.
> **Conclusion** The proposed model combines the advantages of contrastive learning and the ViT model, improving the robustness of facial expression recognition under occlusion and other conditions, and making the recognition results more accurate.

**中文翻译**:

> **目的** 面部表情识别是计算机视觉领域中的重要任务之一，而真实环境下面部表情识别的准确度较低。针对面部表情识别中存在的遮挡、姿态变化和光照变化等问题导致识别准确度较低的问题，提出一种基于自监督对比学习的面部表情识别方法，可以提高遮挡等变化条件下面部表情识别的准确度。
> **方法** 该方法包含对比学习预训练和模型微调两个阶段。在对比学习预训练阶段，改进对比学习的数据增强方式及正负样本对对比次数，选取基于 Transformer 的视觉 Transformer (ViT) 网络作为骨干网络，并在 ImageNet 数据集上训练模型，提高模型的特征提取能力；同时将字典机制应用到 MoCo v3 以缓解训练显存不足。模型微调阶段，采用训练好的预训练模型，用面部表情识别目标数据集微调模型获得识别结果。
> **结果** 实验在 4 类数据集上与 13 种方法进行了比较：在 RAF-DB 数据集中相比 Face2Exp 模型识别准确度提高 0.48%；在 FERPlus 数据集中相比 KTN 模型提高 0.35%；在 AffectNet-8 数据集中相比 SCN 模型提高 0.40%；在 AffectNet-7 数据集中相比 DACL 模型识别准确度略低 0.26%，表明了本文方法的有效性。
> **结论** 本文所提出的人脸表情识别模型，综合了对比学习模型和 ViT 模型的优点，提高了面部表情识别模型在遮挡等条件下的鲁棒性，使识别结果更加准确。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

*   **为什么要做**：面部表情识别在安全监控、教育教学、人机交互等领域应用广泛。表情类型最早由 Ekman 和 Friesen (1971) 定义为快乐、悲伤、愤怒、恐惧、惊讶、厌恶等基本情绪。但在非受控（自然条件）环境下构建的数据集（如 RAF-DB、AffectNet、FERPlus）虽更接近真实场景，却因姿态变换、遮挡、光照差异等与表情无关的干扰因素，使现有深度识别模型准确率下降 (p.123-124)。
*   **之前方法的问题**：现有工作主要分两类：1) 改进损失函数（Separate Loss, DDA loss, DACL, Ad-Corre 等）来引导模型学习更具判别性的特征，但并未聚焦于特征提取与学习本身；2) 引入注意力机制（ACNN, RAN, SPWFA-SE, FER-VT, EAC 等）关注未遮挡、信息丰富的区域，但忽略了数据本身的特征分布 (p.125)。
*   **本文思路（核心矛盾）**：对比学习属于自监督学习，可通过增加任务难度，进一步学习姿态/光照变化下同类图像间的内在一致特征。作者认为**基于负例的对比学习**能够缓解现实条件下遮挡、姿态和光线变化对表情识别的影响，并用 ViT 强大的特征提取能力来增强对比学习在非受控条件下的表征能力 (p.124)。

## 关键贡献

1.  **针对遮挡的对比方式改进**：在 MoCo 框架的随机数据增强（水平翻转、颜色抖动、随机裁剪、灰度转换、模糊、曝光等）基础上，**增加一组正样本对比**——将原图做遮挡增强，再令原图与遮挡增强图构成正样本对，以减少遮挡和数据不确定性对识别的影响 (p.127)。
2.  **字典机制融入 MoCo v3**：MoCo v3 预训练需大批次、显存开销大而难以广泛使用；本文将 MoCo v1/v2 采用的**字典（队列）机制**引入 MoCo v3，使其在显存资源缺乏的情况下仍能训练 (p.126-127)。
3.  **ViT 作为对比学习骨干**：采用基于 Transformer 的 **ViT-small** 作为特征提取骨干网络（替代标准 CNN），结合对比学习预训练，增强特征表征能力 (p.124, p.128)。
4.  **两阶段流程**：先在 ImageNet 上做无监督对比学习**预训练**，再在表情数据集上**微调**，充分利用大量无标签、含噪声/遮挡的数据学习表情数据分布特征 (p.123, p.124)。
5.  **多基准验证**：在 RAF-DB、FERPlus、AffectNet-7、AffectNet-8 四个公开数据集上与 13 种方法比较，取得 89.02%、90.84%、64.94%、60.63% 的准确率，在 RAF-DB、FERPlus、AffectNet-8 上取得最优、在 AffectNet-7 上次优 (p.124, p.129, 表1)。

## 方法

*   **整体框架**（图1）：分两阶段。
    *   **阶段一 — 对比学习预训练**：在 ImageNet 上用无标签数据做自监督对比学习，训练含 ViT 骨干的特征提取器。
    *   **阶段二 — 模型微调**：用训练好的预训练模型，在面部表情数据集上微调获得识别结果。
*   **输入输出**：输入一幅人脸图像，输出该图像对应的表情类别。
*   **关键模块**（p.126）：
    1.  **编码器网络 fq**：包含 1 个 ViT 骨干 + 1 个投影头 + 1 个预测头。投影头是 3 层 MLP，预测头是 2 层 MLP。
    2.  **动量编码器网络 fk**：包含 1 个 ViT 骨干 + 1 个投影头，**没有预测头**；fk 通过 fq 的滑动（移动）平均更新，预测头不更新。
    3.  **字典机制（队列）**：来自 MoCo v1/v2，样本队列以字典形式存储历史负样本特征，使对比时可用的负样本数 K 远大于当前批量，缓解显存压力 (p.126-127)。
*   **数据增强与正样本对**（2.1 节，图2）：以原图 X 为基准，X0 为加入随机遮挡后的图像，X1 为水平翻转图像，X2 为随机裁剪图像。X、X1、X2 经编码器 fq 得到特征 q、q1、q2；X0、X1、X2 经动量编码器 fk 得到特征 k、k1、k2（维度为 n、特征向量长度为 c）。三路分别做矩阵相乘得到 3 个 (n,n) 矩阵，相加后其对角线元素代表正样本对相似度，整个矩阵越接近单位矩阵越好 (p.127-128)。
*   **损失函数 InfoNCE**（p.127, 式(1)）：

    `Loss = -log [ exp(q·k₊/t) / (Σᵢ₌₀ᴷ exp(q·kᵢ⁻/t)) ]`

    *   按原文记法：`k₊` 是 q 的同一幅图像经编码器 fq 的输出，作为 q 的正样本；`k⁻` 表示其他图像经动量编码器 fk 的处理输出，作为 q 的负样本；`t` 是归一化 q、k 的温度超参数；`K` 代表字典中的样本数量。
    *   直观解释：分子为正例间相似度、分母为正例与负例间相似度；相同类别样本相似度越大、不同类别越小，损失越小。
*   **ViT 编码器细节**（2.2 节，图3，p.128）：使用 **ViT-small**，输入图像尺寸 **224×224**，patch 大小 **16×16**，嵌入维度 **384**。前向流程：图像分块 → 块嵌入并加入可学习的分类编码 Xs 与位置编码（式(2)）→ 经 L 层 Transformer 编码器（含 LN + 多头自注意力 MSA + MLP，残差连接，式(3)(4)）→ 层归一化输出面部特征 y（式(5)）。
*   **推理流程**：微调后用编码器骨干提取特征，经分类头输出表情类别。
*   **与已有方法的差异**：
    *   相对 **MoCo v3**：引入字典机制以降低显存需求，并改进数据增强（针对遮挡的增强 + 新增一组正样本对）。
    *   相对**注意力类 FER 方法**（ACNN, RAN 等）：不依赖显式注意力模块定位区域，而是通过对比学习隐式学习对遮挡等变化鲁棒的特征分布。
    *   相对**损失函数改进类方法**（DACL 等）：更侧重通过自监督预训练提升骨干特征表示能力，而非仅优化分类边界。
*   **论文类型特化**：本文属于**自监督/对比学习**与**图像分类**的结合，核心创新在训练框架（字典机制 + ViT 骨干）和任务特化的数据增强（遮挡增强 + 正样本对）。不涉及目标检测、医学影像或 3D 数据。

## 实验

*   **数据集**（第3节, p.129）：
    *   **预训练**：ImageNet。
    *   **RAF-DB**：29 672 幅网络采集真实人脸图像，含单/多标签子集；本文用单标签子集（快乐、中性、惊讶、愤怒、悲伤、恐惧、厌恶 7 类），12 271 训练 + 3 068 测试。
    *   **FERPlus**：28 709 训练 + 3 589 验证 + 3 589 测试，从谷歌搜索引擎收集，除 7 种基本情绪外还含"蔑视"类（共 8 类）。
    *   **AffectNet**：超过 1 000 000 幅面部图像；实验中分别用 8 类（AffectNet-8）和去除蔑视的 7 类（AffectNet-7）。
*   **训练设置**（第4节, p.129）：硬件 Intel i7-6700 CPU 3.40GHz + 16GB 内存 + RTX 1080 Ti GPU，Ubuntu 20.04；损失函数 InfoNCE，骨干 ViT-small，优化器 **Adam**，批量大小 **128**，迭代轮次 **200**，学习率初始 **0.0003**，采用**余弦退火**衰减，衰减周期 **30**；训练/验证集按官网默认划分。
*   **对比方法**（表1, 共13种）：ACNN, SPWFA-SE, RAN, SCN, DACL, KTN, FER-VT, EfficientFace, Separate loss, DDA loss, Ad-Corre, EAC, Face2Exp。
*   **评价指标**：识别准确率 (Accuracy, %)。
*   **主实验结果**（表1, p.129-130）：
    *   **RAF-DB**：本文 **89.02%**，比 Face2Exp (88.54%) 高 **0.48%**（该列最优）。
    *   **FERPlus**：本文 **90.84%**，比 KTN (90.49%) 高 **0.35%**（该列最优）。
    *   **AffectNet-8**：本文 **60.63%**，比 SCN (60.23%) 高 **0.40%**（该列最优）。
    *   **AffectNet-7**：本文 **64.94%**，略低于 DACL (65.20%) **0.26%**（次优，DACL 最优）。
*   **混淆矩阵分析**（图5-图8, p.129-131）：快乐、惊讶、中性表情识别准确度较高；蔑视、恐惧、厌恶等准确度较低，与面部变化不明显、训练集类别不平衡（高兴样本最多、厌恶/蔑视样本少）有关。
*   **消融实验**：PDF 文本未明确给出（未分项验证字典机制 / 遮挡增强 / ViT 骨干各自贡献）。
*   **速度/参数量/FLOPs**：PDF 文本未报告，仅给出硬件配置 (p.129)。

## 局限

1.  **负面表情识别率较低**：作者在结论中明确指出，蔑视、恐惧、厌恶等负面表情准确率有待提高，原因是数据集中负面表情样本数量有限、网络未学到更多负面表情特征 (p.131)。
2.  **类别不平衡敏感**：混淆矩阵显示样本多的类别（高兴）识别效果好，不平衡度高会使网络偏向大样本类，影响分类器性能 (p.129)。
3.  **缺乏消融实验**：未分别验证"字典机制""遮挡增强""ViT 骨干"三项改进各自的贡献，难以判断哪项最关键（PDF 文本未涉及消融）。
4.  **计算成本未讨论**：虽用字典机制缓解显存，但 ImageNet 预训练的整体算力/时间开销论文未报告。
5.  **依赖 2D 数据**：方法基于 2D 人脸表情数据集；作者指出未来将探索 3D 人脸数据下的表情识别 (p.131)。

## 个人评论

1.  **任务驱动的自监督定制化**：论文把通用对比学习框架（MoCo）针对下游任务（表情识别）的具体痛点（遮挡）做定制——把"遮挡增强图与原图构成正样本对"，让模型在预训练阶段就学习对遮挡的不变性。这比在微调阶段依赖有限的带标签遮挡样本更有效，是值得借鉴的"先分析数据特性再设计预训练任务"的思路。
2.  **"预训练-微调"范式的价值**：表情数据集规模小且标签有主观噪声，直接训练受限；先在 ImageNet 上自监督预训练再迁移，强调了大规模无标签数据学习通用表征对小样本、高噪声下游任务的重要性。
3.  **实用的工程取舍**：将字典机制引入 MoCo v3 缓解显存瓶颈，降低了在有限算力下的复现门槛，提升了方法实用性——这是相对原始 MoCo v3 的主要工程贡献。
4.  **改进幅度偏小是隐忧**：四个基准上相对此前最优方法的提升均在 0.48% 以内（且 AffectNet-7 上还落后 DACL 0.26%），缺乏消融与显著性分析的情况下，难以判断收益究竟来自 ViT 骨干、字典机制还是遮挡增强中的哪一项，这也是后续改进的切入点。

### 使用建议

*   **快速了解**：读摘要 + 引言最后一段（工作贡献）+ 结论，即可把握核心思想、方法与主要结果。
*   **复现**：精读第 2 节（2.1 数据增强与正负样本对、2.2 ViT 编码器细节）与第 4 节实验设置（Adam、lr=3e-4、batch=128、200 epoch、余弦退火周期 30）。
*   **借鉴创新点**：1) 如何把下游痛点（遮挡）转化为自监督预训练任务（遮挡增强 + 正样本对比）；2) 融合字典机制以降低显存；3) ViT 骨干 + 对比学习的范式。
*   **写 related work**：可归入"对比/自监督学习视觉表征""基于 Transformer 的面部表情识别""遮挡/姿态鲁棒的 FER"三个子领域。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[J_人脸_表情_伪造_情感]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的**人脸表情识别 (FER)** 方向，针对真实非受控环境下因遮挡、姿态变化、光照差异导致识别准确率低的问题，提出一种结合**自监督对比学习**（基于 MoCo 系列、负例对比）与**视觉 Transformer (ViT)** 的方法。归类于 `J_人脸_表情_伪造_情感` 主题。

## 2. 一句话总结
在 MoCo 对比学习框架上融合 ViT-small 骨干、把字典机制引入 MoCo v3 缓解显存，并新增"原图—遮挡增强图"正样本对；先在 ImageNet 自监督预训练再到表情数据集微调，从而提升遮挡等复杂条件下的表情识别准确率。

## 3. 背景与问题
*   **为什么要做**：FER 在安全监控、教育、人机交互等领域应用广，但非受控环境下遮挡/姿态/光照干扰使深度模型准确率下降；非受控数据集（RAF-DB、AffectNet、FERPlus）更接近真实场景因而更具研究意义 (p.123-124)。
*   **之前方法的问题**：损失函数改进类（Separate Loss/DDA/DACL/Ad-Corre）未聚焦特征提取本身；注意力类（ACNN/RAN/SPWFA-SE/FER-VT/EAC）忽略了数据本身的特征分布 (p.125)。
*   **核心思路**：对比学习可通过增加任务难度学习姿态/光照变化下同类图像的内在一致特征，作者用基于负例的对比学习 + ViT 来解决遮挡等问题 (p.124)。

## 4. 核心贡献
1.  在 MoCo 随机增强（翻转/颜色抖动/裁剪/灰度/模糊/曝光）基础上，**新增一组正样本对比**：原图做遮挡增强后与原图构成正样本对，提升对遮挡的鲁棒性 (p.127)。
2.  将 MoCo v1/v2 的**字典（队列）机制引入 MoCo v3**，解决其大批次训练显存不足问题 (p.126-127)。
3.  采用 **ViT-small** 作为对比学习骨干替代 CNN，增强特征表征 (p.124, p.128)。
4.  **两阶段**：ImageNet 自监督预训练 + 表情数据集微调 (p.123-124)。
5.  四基准（RAF-DB/FERPlus/AffectNet-7/-8）与 13 种方法比较，取得 89.02%/90.84%/64.94%/60.63%，三个数据集最优、AffectNet-7 次优 (p.124, p.129, 表1)。

## 5. 方法详解
*   **整体框架**（图1）：阶段一在 ImageNet 上自监督对比学习预训练（含 ViT 骨干）；阶段二在表情数据集上微调。
*   **输入输出**：输入一幅人脸图像，输出表情类别。
*   **关键模块**（p.126）：
    1.  **编码器 fq** = ViT 骨干 + 3 层 MLP 投影头 + 2 层 MLP 预测头。
    2.  **动量编码器 fk** = ViT 骨干 + 投影头（无预测头），由 fq 滑动平均更新，预测头不更新。
    3.  **字典/队列机制**：存储历史负样本，使可用负样本数 K 远大于批量 (p.126-127)。
*   **正样本对设计**（2.1 节，图2）：X 原图、X0 随机遮挡图、X1 水平翻转图、X2 随机裁剪图；X/X1/X2 经 fq 得 q/q1/q2，X0/X1/X2 经 fk 得 k/k1/k2；三路矩阵相乘相加，对角线（正样本对相似度）越大、整体越接近单位矩阵越好 (p.127-128)。
*   **损失 InfoNCE**（式(1), p.127）：
    `Loss = -log [ exp(q·k₊/t) / (Σᵢ₌₀ᴷ exp(q·kᵢ⁻/t)) ]`
    *   原文记法：`k₊` 为 q 同一图像经 fq 的输出（正样本）；`k⁻` 为其他图像经动量编码器 fk 的输出（负样本）；`t` 温度超参；`K` 字典样本数。分子=正例相似度，分母=正例与负例相似度。
*   **ViT 编码器**（2.2 节，图3，p.128）：ViT-small，输入 224×224，patch 16×16，嵌入维度 384；流程为分块 → 块嵌入 + 分类编码 Xs + 位置编码（式(2)）→ L 层 Transformer（LN + MSA + MLP + 残差，式(3)(4)）→ LN 输出面部特征 y（式(5)）。
*   **推理**：微调后用骨干提取特征经分类头输出类别。
*   **与已有方法差异**：相对 MoCo v3（字典机制降显存 + 遮挡增强/新增正样本对）；相对注意力类 FER（隐式学习鲁棒特征分布而非显式定位）；相对损失改进类（提升骨干表征而非仅优化分类边界）。
*   **类型特化**：自监督/对比学习 + 图像分类，不涉及检测/医学/3D。

## 6. 实验与结果
*   **数据集**（p.129）：预训练 ImageNet；RAF-DB（29672 总，单标签 7 类 12271 训练 + 3068 测试）；FERPlus（28709 训练 + 3589 验证 + 3589 测试，8 类含蔑视）；AffectNet（>1M 图像，8 类 / 去蔑视 7 类）。
*   **训练设置**（p.129）：Adam，batch=128，200 epoch，lr=3e-4，余弦退火（周期 30）；硬件 i7-6700 + 16GB + RTX 1080 Ti。
*   **对比方法**（表1）：13 种 — ACNN, SPWFA-SE, RAN, SCN, DACL, KTN, FER-VT, EfficientFace, Separate loss, DDA loss, Ad-Corre, EAC, Face2Exp。
*   **评价指标**：准确率 (%)。
*   **主结果**（表1, p.129-130）：RAF-DB 89.02%（+0.48% vs Face2Exp，最优）；FERPlus 90.84%（+0.35% vs KTN，最优）；AffectNet-8 60.63%（+0.40% vs SCN，最优）；AffectNet-7 64.94%（-0.26% vs DACL，次优）。
*   **混淆矩阵**（图5-8）：快乐/惊讶/中性高、蔑视/恐惧/厌恶低，受类别不平衡影响 (p.129)。
*   **消融实验**：PDF 文本未明确给出。
*   **速度/参数量/FLOPs**：PDF 文本未报告，仅硬件配置 (p.129)。

## 7. 这篇论文真正有价值的地方
1.  **任务驱动的自监督定制**：把通用 MoCo 框架针对表情识别的遮挡痛点定制——"遮挡增强图—原图"正样本对，让预训练阶段就学到遮挡不变性，比微调阶段靠有限带标签遮挡样本更有效。
2.  **"预训练-微调"对小/噪数据的价值**：表情数据集小且标签主观有噪，先在 ImageNet 自监督预训练再微调，凸显大规模无标签数据学通用表征的重要性。
3.  **工程实用性**：字典机制引入 MoCo v3 缓解显存瓶颈，降低有限算力下的复现门槛——这是相对 MoCo v3 的主要工程贡献。

## 8. 局限与问题
1.  **负面表情识别率低**：结论明确指出蔑视/恐惧/厌恶等准确率有待提高，与负面样本数量有限、特征学习不足有关 (p.131)。
2.  **类别不平衡敏感**：混淆矩阵显示模型偏向高兴等大样本类 (p.129)。
3.  **缺消融**：未分项验证字典机制/遮挡增强/ViT 骨干各自贡献（PDF 文本未涉及）。
4.  **计算成本未讨论**：ImageNet 预训练整体算力/时间未报告。
5.  **依赖 2D 数据**：作者指出未来探索 3D 人脸数据下的表情识别 (p.131)。
6.  **改进幅度偏小**：四基准提升均 ≤0.48%（AffectNet-7 还落后 0.26%），缺消融与显著性分析。

## 9. 我该怎么使用这篇论文
*   **快速了解**：读摘要 + 引言最后一段（贡献）+ 结论。
*   **复现**：精读 2.1（数据增强与正负样本对）、2.2（ViT 编码器细节）与第 4 节超参（Adam, lr=3e-4, batch=128, 200 epoch, 余弦退火周期 30）。
*   **借鉴创新点**：1) 把下游痛点转化为自监督预训练任务（遮挡增强 + 正样本对比）；2) 字典机制降显存；3) ViT 骨干 + 对比学习范式。
*   **写 related work**：归入"对比/自监督视觉表征""基于 Transformer 的 FER""遮挡/姿态鲁棒 FER"。

## 10. 和其他论文的关系
*   [[MoCo]] / MoCo v1/v2/v3：本文框架的直接基础与改进对象（字典机制取自 v1/v2，骨干与预测头取自 v3）(p.126)。
*   [[ViT]] (Dosovitskiy 等, 2021)：本文采用的骨干网络 (p.124)。
*   [[Face2Exp]] (Zeng 等, 2022)：RAF-DB 上的主要对比方法，用元优化框架消除数据偏差 (表1)。
*   [[SCN]] (Self-Cure Network, Wang 等, 2020a)：AffectNet-8 上主要对比方法，抑制标签不确定性 (p.125, 表1)。
*   [[KTN]] (Knowledgeable Teacher Network, Li 等, 2021)：FERPlus 上主要对比方法，知识蒸馏 + AdaReg 损失 + 粗-细标签策略 (p.126, 表1)。
*   [[DACL]] (Deep Attentive Center Loss, Farzaneh & Qi, 2021)：AffectNet-7 上最优方法，注意力中心损失 (p.125, 表1)。
*   对比学习同类工作：SimCLR、BYOL、SwAV、Barlow Twins（1.2 节背景对比）(p.125-126)。

## 11. 关键词
面部表情识别 (FER)，对比学习，自监督学习，视觉 Transformer (ViT-small)，MoCo，字典/队列机制，遮挡增强，正负样本对，InfoNCE，鲁棒性，预训练-微调。

## 12. 可信度说明
本笔记基于覆盖全文 11 页的 PDF 提取文本（含摘要、引言、相关工作、方法、数据集、实验与结果、结论），提取质量高（约 2276 字符/页）。方法（2.1/2.2 节公式与超参）、数据集划分、表1 全部数值、训练设置均能在提取文本中逐项核实。**消融实验、模型效率（参数量/FLOPs/时间）** 论文本身未给出，已如实标注"PDF 文本未明确"。所有引用数字均严格来源于提取文本。

---

> **可信度补充**: PDF 提取质量 = **high** (覆盖 11/11 页, 约 2276 字符/页); 来源缓存: `.paper-cache/extracts/融合ViT与对比学习的面部表情识别.txt`; 生成日期: 2026-06-05; 复核整理日期: 2026-06-18; 模式: LLM (mimo-v2.5-pro) + 人工对照提取文本校订。
<!-- AI_READING_NOTE_END -->
