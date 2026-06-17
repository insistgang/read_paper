---
title: Improving the Detection of Small Oriented Objects in Aerial Images
authors:
  - "Chandler Timm C. Doloriel"
  - "Rhandley D. Cajote"
year: 2024
venue: "Electronics"
doi: 
pdf: [[2024_Improving_the_Detect.pdf]]
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
extract_cache: .paper-cache/extracts/2024_Improving_the_Detect.txt
---

# Improving the Detection of Small Oriented Objects in Aerial Images

## 基本信息
- **PDF**: [[2024_Improving_the_Detect.pdf]]
- **primary_topic**: `C_目标检测_通用与旋转框`
- **topics**: `C_目标检测_通用与旋转框`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Improving the Detection of Small Oriented Objects in Aerial Images |
| **作者** | Chandler Timm C. Doloriel; Rhandley D. Cajote（University of the Philippines, Diliman） |
| **发表时间** | 2024（arXiv:2401.06503v1，2024-01-12） |
| **刊物/会议** | Electronics |
| **DOI** | 未明确 |
| **代码** | https://github.com/chandlerbing65nm/APDetection |

## 摘要

> **英文原摘要（据 PDF 提取文本整理，已修复空格/连字符断裂）**：
> Small oriented objects that represent tiny pixel-area in large-scale aerial images are difficult to detect due to their size and orientation. Existing oriented aerial detectors have shown promising results but are mainly focused on orientation modeling with less regard to the size of the objects. In this work, we proposed a method to accurately detect small oriented objects in aerial images by enhancing the classification and regression tasks of the oriented object detection model. We designed the Attention-Points Network consisting of two losses: Guided-Attention Loss (GALoss) and Box-Points Loss (BPLoss). GALoss uses an instance segmentation mask as ground-truth to learn the attention features needed to improve the detection of small objects. These attention features are then used to predict box points for BPLoss, which determines the points' position relative to the target oriented bounding box. Experimental results show the effectiveness of our Attention-Points Network on a standard oriented aerial dataset with small object instances (DOTA-v1.5) and on a maritime-related dataset (HRSC2016). The code is publicly available.

> **中文翻译**：在大尺度航空图像中，仅占极少像素面积的小型旋转目标因其尺寸与方向而难以检测。现有旋转航空检测器虽已取得不错结果，但主要聚焦方向建模，对目标尺寸关注不足。本文提出一种方法，通过增强旋转目标检测模型的**分类**与**回归**两项任务，来精确检测航空图像中的小型旋转目标。我们设计了**注意力-点网络（Attention-Points Network）**，包含两个损失：**引导注意力损失（GALoss）** 与 **框点损失（BPLoss）**。GALoss 以实例分割掩码作为真值，学习有助于提升小目标检测的注意力特征；这些注意力特征再被用于为 BPLoss 预测框点，BPLoss 据框点相对于目标旋转框（OBB）的位置进行评分。实验在含小目标实例的标准旋转航空数据集 DOTA-v1.5 与海事数据集 HRSC2016 上验证了 Attention-Points Network 的有效性。代码已开源。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：航空图像目标尺寸小、方向任意。水平边界框（HBB）检测旋转航空目标"非常无效"——目标无法被精确定位，会框入更多噪声与背景，导致漏检/误检；因此需要能输出旋转边界框（OBB）的检测器 (Introduction, p.1)。HBB 检测在车辆跟踪、人脸识别、海事检测等场景常见，但不适用于旋转航空目标。
- **之前方法的问题**：现有旋转检测方法从特征精炼、提议生成、方向对齐、回归损失设计等方向改进，对旋转目标"很有效"，但**对小型旋转目标的检测仍需更多研究** (p.1)。同时，常用基准 **DOTA-v1.0 并不以包含小而复杂实例著称**；为了在含小旋转目标的数据集上恰当评测，本文改用 **DOTA-v1.5** (p.1)。
- **核心思路（动机）**：用**注意力机制**汇聚目标的重要特征，提升模型对"小且复杂"这类难识别目标的感知；进而把注意力特征用于设计的**回归损失**，预测框点并依据其相对 OBB 的位置打分 (p.1)。

## 关键贡献

1.  提出 **注意力-点网络（Attention-Points Network, APN）**，用于提升航空图像中小型旋转目标的检测。该网络包含两个损失：**引导注意力损失（GALoss）** 与 **框点损失（BPLoss）**。GALoss 用注意力特征改善小目标检测，BPLoss 依据预测框点相对目标 OBB 的位置进行打分 (Contributions, p.2)。
2.  将本方法与其它 OBB 检测器对比，在含小目标实例的标准旋转航空数据集 **DOTA-v1.5** 与海事数据集 **HRSC2016** 上验证了有效性 (p.2)。
3.  进行**消融实验**评估所设计的两个损失 GALoss 与 BPLoss，并与基线架构对比；结果表明**每个损失都对整体性能有贡献，且不落后于基线** (p.2)。

> 注：原笔记把"76.20% mAP50""DOTA-v1.5 含 403,318 实例"等数字写进贡献条目，这些是实验/数据集事实而非论文自列的贡献。本节据论文"Contributions"原文校正为 3 条。

## 方法

- **整体框架**：基于两阶段旋转检测器 **Oriented RCNN [34]** 改进，将 APN 置于 **rotated RoIAlign 之后**（架构见 Fig. 1）。第一阶段做特征提取，第二阶段做预测。骨干为 **ResNet（R-50）[14]**，产生五个层级特征送入 **FPN [17]** 精炼；特征送入 **RPN** 生成多尺度多比例提议；提议经 **rotated RoIAlign** 抽取并变换为特征，作为自注意力的输入 RoI (p.3)。
- **输入**：每个 RoI 使用 **7×7** 特征尺寸作为自注意力的输入，并用 GALoss 精炼；注意力特征用于预测框点，再由 BPLoss 依其相对目标 OBB 的位置打分 (p.3)。
- **关键模块**：
    1.  **引导注意力损失（GALoss）**（§3.1, Fig. 2, Algorithm 1）：
        - **机制**：RoI 先经**自注意力**得到富含全局上下文的注意力特征 `x`；掩码 `y` 由**边界框转换得到的实例分割掩码**给出。论文指出航空目标形状不规则、实例分割掩码难以标注，故改用**仅需边界框坐标即可标注的粗粒度掩码（coarse-level masks）** (p.2, §3.1)。该思路借鉴 [23]，但用**自注意力**替代 CNN 来获取目标的全局上下文。
        - **损失计算**：用**二元交叉熵**比较注意力特征 `x` 与掩码 `y`：`GALoss = -1/(N·P) · Σ_j [ y_j·log(x_j) + (1-y_j)·log(1-x_j) ]` (Algorithm 1)。训练中 `x` 逐渐学到目标掩码、聚焦前景，使特征比原始 RoI 信息更丰富，从而改善小目标检测。
        - **自注意力**：遵循标准 Q/K/V 形式 `Attention(Q,K,V)=softmax(QKᵀ/√d_k)·V` (Eq. 3)。论文相关工作还提到可借鉴"高效自注意力"（如交换 Q、V 位置 [46]）降低计算量 (§2.3.1)。
    2.  **框点损失（BPLoss）**（§3.2, Fig. 3）：
        - **机制**：用注意力特征预测一组**框点（box-points）**，每个框点位于 `(i, j)`。
        - **相对位置判据**：连接 OBB 四条边与框点 `(i,j)` 形成四个三角形 T1–T4；若四个三角形面积之和 ≤ OBB 面积，则框点在 OBB 内部 `δ=1`，否则 `δ=0` (Eq. 4)。
        - **可微近似**：Eq. 4 不可导，故设计 sigmoid 派生的核函数近似：`δ(BP_{i,j}|OBB) = 2 / (1 + e^{ k·(Σ_n Area_{Tn} − Area_{OBB})/Area_{OBB} })` (Eq. 5)。
        - **损失计算**：`BPLoss = 1 − (1/N)·Σ_{n=1}^{N} δ(BP_n|OBB)` (Eq. 6)，鼓励框点落入目标 OBB 内。
- **与已有回归损失的差异**（§2.2.1, §3.2）：
    - 论文综述了旋转 IoU 类损失的三条路线：① 多边形距离 + smooth L1（梯度仍由 smooth L1 主导，度量不一致）[39]；② 转 2-D 高斯分布并用 Wasserstein [38] / KL 散度 [40] 计算（复杂、开销大）；③ **PIoU Loss [6]**，直接累加重叠像素的贡献（简单，但每个像素注意力相同，难以表达目标重要性）。
    - **BPLoss vs. PIoU Loss [6]**：PIoU 计算像素到 OBB 中心的距离、且同时用目标与预测的 OBB；**BPLoss 只用目标 OBB 的顶点**，无需转中心格式，且**用三角形面积之差**而非像素的**欧氏距离**来度量。
- **评测指标（§3.3）**：用 mAP；按 IoU 阈值划分 TP/FP（IoU>阈值为 TP），先算各类 AP 再对类别取平均 `mAP = (1/N)·Σ_i AP_i` (Eq. 7)。默认 **IoU=0.5 + PASCAL VOC07** 评测，另用 VOC12 及 IoU=0.7、IoU=0.5:0.95 等阈值。
- **训练**：两个新损失与检测主损失一同端到端训练；GALoss/BPLoss 在推理时不参与计算（推理流程与标准两阶段检测器一致：特征→提议→rotated RoIAlign→APN→分类/回归）。

> 说明：原笔记给出的"总损失 = 检测损失 + λ1·GALoss + λ2·BPLoss"中的权重系数 λ1、λ2 在提取缓存（前 ~25000 字符）中未出现，属合理推断但**具体取值 PDF 提取文本未明确**。

## 实验

- **数据集**（§4.1）：
    1.  **DOTA-v1.5 [33]**：航空图像旋转框检测最大数据集，**2806 张大尺寸图像**（约 1/2 train、1/6 val、1/3 test），**403,318 个实例**、**16 个类别**（PL/BD/BR/GTF/SV/LV/SH/TC/BC/ST/SBF/RA/HA/SP/HC/CC）；含**小于 10 像素的极小实例**，尺度/方向/长宽比变化大。
    2.  **HRSC2016 [20]**：海事船舶数据集，**1061 张图像**（300×300 至 1500×900 像素）。提取缓存在"We combined the train and val sets for tra…"处截断，该数据集的 train/val/test 张数（提取文本片段为 436/181/444）及其后续实验数字未完整覆盖。
- **基线 / 骨干**：基线为 **Oriented RCNN（ORCNN）[34]**，骨干 **R-50-FPN [14]**。
- **对比方法**（Table 1）：
    - 单阶段：RetinaNet、FCOS、RSDet++、DCL、GWD、BCD、KLD、KFIoU、R2CNN（结果取自 AlphaRotate 库，标 α）。
    - 多阶段：MR、CMR、HTC、FR、RT、ORCNN（标 β，结果取自 AerialDetection 库）。
- **主实验结果（DOTA-v1.5，Table 1，mAP50）**：
    - **trainval/test** 划分：基线 ORCNN = **0.7619**，本文 OURS = **0.7620**（基本持平，仅 +0.01%）。OURS 在若干类别上更高（如 PL 0.8620 vs 0.8098、GTF 0.8015 vs 0.7960、HC 0.7536 vs 0.7354）。
    - **train/test\*** 划分（更难，训练数据更少）：基线 ORCNN\* = **0.6672**，本文 OURS\* = **0.7172**，**相对提升 +7.49%**。这是论文主要增益所在。
- **不同 IoU 阈值（Table 2）**：
    - trainval/test：Baseline 0.7619/0.5089/0.4795（mAP50/75/50:95）→ Ours 0.7620(+0.01%)/0.5204(+2.24%)/0.4824(+0.59%)。
    - train/test\*：Baseline\* 0.6672/0.3886/0.3800 → Ours\* 0.7172(+7.49%)/0.4425(+13.87%)/0.4260(+12.11%)。**越严格的 IoU 下相对增益越大**，说明方法主要改善了定位精度。
- **HRSC2016 结果**：原笔记记 OURS = 88.77% mAP50 vs 基线 86.83%。该数字位于提取缓存截断点之后**（据原文后续页，提取缓存未覆盖，待核）**。
- **消融实验**：论文（Contributions §3）声明对 GALoss、BPLoss 做了消融并与基线对比，"每个损失都有贡献且不落后基线"。原笔记给出的"仅 BPLoss→70.39%、仅 GALoss→68.80%、二者结合→71.72%"中，**71.72% 与 Table 2 一致；但 70.39%、68.80% 这两个单损失消融数字未出现在提取缓存的 Table 1/Table 2 中**，应来自后续页的消融表 **（据原文后续页，提取缓存未覆盖，待核）**。
- **效率信息**：提取文本未提供推理速度、参数量或 FLOPs 等效率对比；论文相关工作多次提到自注意力"计算开销大"，但**正文是否给出本方法的开销数据，提取缓存未覆盖**。

## 局限

1.  **GALoss 依赖掩码监督**：需实例分割掩码作为真值。论文已用"仅需边界框坐标"的粗粒度掩码缓解标注成本，但相对纯框标注仍多一步，且粗掩码对不规则航空目标是近似。
2.  **trainval/test 上几乎无增益**：在完整数据划分（trainval/test）上 OURS 仅比基线高 0.01%（76.20% vs 76.19%）；显著增益集中在数据更少的 train/test\* 划分。方法在数据充足时的边际收益有限。
3.  **效率分析缺失（就提取文本而言）**：自注意力会引入额外计算/显存开销，提取缓存中未见对应的速度/参数/FLOPs 报告。
4.  **实验广度**：主要在 DOTA-v1.5 与 HRSC2016 上验证，未见在 VisDrone 等其它小目标数据集上的泛化结果。
5.  **对比时效**：Table 1 中部分对比方法（KLD、KFIoU、GWD 等）年份偏早，与 2023–2024 最新旋转检测 SOTA 的对比在提取文本中未体现。

## 个人评论

1.  **问题切口明确**：抓住"现有旋转检测器重方向、轻尺寸"的空白，把目标对准更难的小型旋转目标，并据此把基准从 DOTA-v1.0 换成含 <10px 实例的 DOTA-v1.5，问题与评测设置自洽。
2.  **两个损失互补**：GALoss 用弱监督（框生成的粗掩码）把自注意力"拉"向前景，是一种轻量的注意力对齐范式；BPLoss 则把"点是否落在目标框内"这一几何判据做成可微核函数，思路清晰。两者一个改分类感知、一个改回归定位，呼应摘要"增强分类与回归两项任务"。
3.  **增益的可信度**：最亮眼的 +7.49%/+13.87%/+12.11% 都来自 train/test\* 这一数据更少的设定，而 trainval/test 上几乎打平。这更像"在低数据/难设定下注意力与几何先验帮助更大"，读者引用时应区分两种划分，不宜笼统说"大幅提升"。
4.  **与 PIoU 的关系**：BPLoss 在 PIoU 思想上做了简化（只用目标 OBB 顶点、面积差代替像素欧氏距离），创新是"减负而非加难"，工程上更易实现，但论文对"为何面积核优于直接坐标回归"的机理论证可更深入。

### 使用建议

- **快速了解**：读 Abstract、Introduction 的贡献小结、§3（方法）标题与 Fig. 1/2/3、以及 Table 1/2。
- **复现**：精读 §3，重点 Algorithm 1 与 Eq. (4)(5)(6)；需弄清如何从边界框生成"粗粒度实例分割掩码"、自注意力如何接在 rotated RoIAlign（7×7）之后、以及框点如何预测与打分。代码已开源（GitHub: chandlerbing65nm/APDetection）。
- **借鉴创新点**：
    - **GALoss**：任何"想让模型注意特定区域"的任务，都可把注意力特征与（可弱监督生成的）空间掩码对齐。
    - **BPLoss**：把"预测点与目标框的几何关系"做成可微损失的思路，可迁移到其它需要空间关系监督的回归任务。
- **写 related work**：可归入"**旋转目标检测**（改进回归损失 / 注意力机制）"或"**小目标检测**（航空/遥感场景）"。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C_目标检测_通用与旋转框]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
计算机视觉 **目标检测** 方向，聚焦 **航空图像中小型旋转目标（oriented/旋转框）检测**。航空目标尺度小、方向任意，水平框（HBB）会框入大量背景导致误检；现有旋转框（OBB）检测器又"重方向、轻尺寸"，对小目标不足。论文用 DOTA-v1.5（含 <10px 极小实例）作为针对性基准，归属"**旋转目标检测**"与"**小目标检测**"。对应库内主题 `C_目标检测_通用与旋转框`。

## 2. 一句话总结
提出 **注意力-点网络（Attention-Points Network, APN）**，用 **引导注意力损失（GALoss）** 让自注意力特征对齐目标掩码、用 **框点损失（BPLoss）** 以可微面积核约束预测框点落入目标 OBB，从而同时增强旋转检测的分类与回归，提升航空小目标检测精度。

## 3. 背景与问题
- **为什么要做**：HBB 检测旋转航空目标"非常无效"，需输出 OBB 的检测器；但现有 OBB 方法对小型旋转目标仍有不足 (Intro, p.1)。
- **基准问题**：DOTA-v1.0 不以含小而复杂实例著称，故改用含 <10px 实例的 **DOTA-v1.5** 评测 (p.1)。
- **核心思路**：用注意力汇聚小目标关键特征，再把注意力特征喂给基于框点相对位置的回归损失 (p.1)。

## 4. 核心贡献（据论文 Contributions 原文，3 条）
1.  提出 **APN**，含 **GALoss**（用注意力特征改善小目标检测）与 **BPLoss**（按预测框点相对目标 OBB 的位置打分）。
2.  与其它 OBB 检测器对比，在 **DOTA-v1.5**（含小实例）与 **HRSC2016**（海事）上验证有效性。
3.  对 GALoss、BPLoss 做**消融**并与基线对比，证明每个损失都有贡献且不落后基线。

## 5. 方法详解
- **框架**：基于 **Oriented RCNN [34]**，将 APN 置于 **rotated RoIAlign 之后**（Fig. 1）。骨干 ResNet（R-50）+ FPN，RPN 出提议，rotated RoIAlign 抽取 **7×7** RoI 特征送入自注意力。
- **GALoss（§3.1, Fig. 2, Algo. 1）**：RoI 经自注意力得特征 `x`；掩码 `y` 由**边界框转换的粗粒度实例分割掩码**给出（航空目标形状不规则、精细掩码难标，故用只需框坐标的 coarse mask）。用 BCE 比较 `x` 与 `y`：`GALoss = -1/(N·P)·Σ_j[y_j log x_j + (1-y_j) log(1-x_j)]`。自注意力为标准 `softmax(QKᵀ/√d_k)V`（Eq. 3）。思路借鉴 [23]，但以自注意力替代 CNN 获取全局上下文。
- **BPLoss（§3.2, Fig. 3）**：预测框点 `(i,j)`；连 OBB 四边与框点成四三角形 T1–T4，`ΣArea_Tn ≤ Area_OBB` 则点在框内 `δ=1`（Eq. 4，不可导）；用 sigmoid 核近似 `δ = 2/(1+e^{ k·(ΣArea_Tn − Area_OBB)/Area_OBB })`（Eq. 5）；`BPLoss = 1 − (1/N)Σ_n δ(BP_n|OBB)`（Eq. 6）。
- **与回归损失谱系的关系（§2.2.1）**：综述了多边形+smooth L1 [39]、2-D 高斯+Wasserstein/KL [38,40]、PIoU [6] 三类。**BPLoss vs PIoU**：只用目标 OBB 顶点（不转中心格式）、用三角形面积差替代像素欧氏距离，更轻量。
- **评测（§3.3）**：mAP（Eq. 7），默认 IoU=0.5 + VOC07，另用 VOC12、IoU=0.7、IoU=0.5:0.95。
- **训练/推理**：两损失与主检测损失端到端联合训练（加权系数 λ1、λ2 提取文本未明确）；推理不计算 GALoss/BPLoss。

## 6. 实验与结果
- **数据集**：DOTA-v1.5（2806 图、403,318 实例、16 类、含 <10px 实例）；HRSC2016（1061 图，300×300–1500×900）。基线 ORCNN [34]，骨干 R-50-FPN。
- **DOTA-v1.5 主结果（Table 1, mAP50）**：
    - trainval/test：ORCNN **0.7619** → OURS **0.7620**（几乎持平）。
    - train/test\*：ORCNN\* **0.6672** → OURS\* **0.7172**（**+7.49%**，主要增益）。
- **不同 IoU（Table 2）**：
    - trainval/test：0.7619/0.5089/0.4795 → 0.7620(+0.01%)/0.5204(+2.24%)/0.4824(+0.59%)。
    - train/test\*：0.6672/0.3886/0.3800 → 0.7172(+7.49%)/0.4425(+13.87%)/0.4260(+12.11%)。越严格 IoU 增益越大 → 主要改善定位精度。
- **HRSC2016**：原笔记记 88.77% vs 86.83%——**据原文后续页，提取缓存未覆盖，待核**。
- **消融单项数字**：原笔记"仅 BPLoss 70.39%、仅 GALoss 68.80%"——**据原文后续页消融表，提取缓存未覆盖，待核**；组合 71.72% 与 Table 2 一致。
- **效率**：提取文本未给推理速度/参数/FLOPs。

## 7. 这篇论文真正有价值的地方
1.  **问题与评测自洽**：把"重方向轻尺寸"的空白说清楚，并据此换用含 <10px 实例的 DOTA-v1.5。
2.  **GALoss 的弱监督注意力对齐**：用框生成的粗掩码引导自注意力聚焦前景，是低成本、可迁移的范式。
3.  **BPLoss 的可微几何约束**：把"框点是否落入目标 OBB"做成 sigmoid 面积核，比 PIoU 更轻（只需目标顶点、面积差代替欧氏距离）。
4.  **增益分布的诚实呈现**：在低数据 train/test\* 设定下增益明显，且严格 IoU 下更大，指向"定位精度"这一可解释的改进维度。

## 8. 局限与问题
1.  **掩码监督依赖**：GALoss 需（粗粒度）实例分割掩码，比纯框标注多一步，且粗掩码对不规则目标是近似。
2.  **充足数据下增益微弱**：trainval/test 上仅 +0.01%，显著增益集中于数据更少的 train/test\*。
3.  **效率未报（就提取文本）**：自注意力开销未见量化。
4.  **泛化范围**：仅 DOTA-v1.5 + HRSC2016，未见 VisDrone 等其它小目标基准。
5.  **对比时效**：部分对比方法偏早，缺少与最新 SOTA 的对照（就提取文本）。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Intro 贡献小结 + §3 标题/Fig.1-3 + Table 1/2。
- **复现**：精读 §3，重点 Algorithm 1 与 Eq.(4)(5)(6)；弄清粗掩码生成、自注意力接 7×7 RoI、框点预测与打分。代码：github.com/chandlerbing65nm/APDetection。
- **借鉴**：GALoss（注意力特征↔弱监督空间掩码对齐）；BPLoss（预测点↔目标框几何关系做成可微损失）。
- **写 related work**：归入"旋转目标检测（回归损失/注意力）"或"小目标检测（航空/遥感）"。

## 10. 和其他论文的关系
- 直接建立在 **Oriented RCNN [34]** 之上，作为基线与架构起点。
- 回归损失设计上对照 **PIoU Loss [6]**（像素距离）、**GWD [38] / KLD [40]**（高斯+Wasserstein/KL）、多边形距离+smooth L1 [39]。
- 注意力部分沿用 **自注意力 / ViT [45]** 的 Q/K/V 思想，并讨论了高效自注意力（交换 Q、V）以降开销 [46]。
- GALoss 的"掩码引导注意力"思路借鉴 [23]（原用 CNN 高亮被遮挡目标）。
（以上链接为据论文正文识别的相关工作，入库建链时以实际笔记为准。）

## 11. 关键词
旋转目标检测, OBB, 小目标检测, 航空/遥感图像, 自注意力, 引导注意力损失 GALoss, 框点损失 BPLoss, 实例分割掩码引导, 可微 IoU 损失, Oriented RCNN, DOTA-v1.5, HRSC2016, PIoU

## 12. 可信度说明
本精读基于提取缓存（前 ~25000 字符，约覆盖原文 42984 字符的前 ~58%，含 Abstract、Introduction、Related Work、§3 方法全部、§3.3 评测、§4.1 数据集、Table 1、Table 2）。**截断发生在 HRSC2016 数据集描述中段（"…combined the train and val sets for tra"）**，故 HRSC2016 的最终 mAP（88.77%/86.83%）、损失单项消融数字（70.39%/68.80%）、以及损失加权系数 λ1/λ2、效率开销等，均在提取缓存之外，已逐处标注"待核"。方法公式（Eq. 3–7）、DOTA-v1.5 主结果与 Table 1/2 数值均可在提取文本逐一核对。

---

> **可信度补充**: PDF 提取质量 = **medium**（提取缓存仅覆盖原文前 ~25000/42984 字符 ≈ 58%，HRSC2016 结果与单项消融数字未覆盖，已标"待核"）; 来源缓存: `.paper-cache/extracts/2024_Improving_the_Detect.txt`（标称 10/10 页，但字符级截断于 25000）; 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro); 复核重写: 2026-06-18（对照提取文本校正分类、摘要、数字归属）。
<!-- AI_READING_NOTE_END -->
