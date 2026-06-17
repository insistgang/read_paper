---
title: "MPSN: Motion-aware Pseudo-Siamese Network for Indoor Video"
authors:
  - "Kailai Sun"
  - "Xiaoteng Ma"
  - "Peng Liu"
  - "Qianchuan Zhao"
year: 2021
venue: "arXiv"
doi: 
pdf: [[2021_MPSN_Motion-aware_P.pdf]]
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
extract_cache: .paper-cache/extracts/2021_MPSN_Motion-aware_P.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/13 pages"
---
# MPSN: Motion-aware Pseudo-Siamese Network for Indoor Video

## 基本信息
- **PDF**: [[2021_MPSN_Motion-aware_P.pdf]]
- **primary_topic**: `C2_目标检测_违建_车辆_船舶_行人`
- **topics**: `C2_目标检测_违建_车辆_船舶_行人`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | MPSN: Motion-aware Pseudo-Siamese Network for Indoor Video Head Detection in Buildings |
| **作者** | Kailai Sun; Xiaoteng Ma; Peng Liu; Qianchuan Zhao（清华大学自动化系，CINS / BNRist） |
| **发表时间** | 2021 (arXiv:2110.03302；提取文本所在版本 v5, 2022-12-12，标注 "Preprint submitted to Elsevier") |
| **刊物/会议** | arXiv 预印本（投往 Elsevier 期刊） |
| **DOI** | 未明确（arXiv:2110.03302） |
| **代码** | https://github.com/pl-share/MPSN |

## 摘要

清理后的英文原摘要（据 PDF 提取文本整理，修复空格/连字符断裂）：

> Indoor video head detection is an essential component of building occupancy detection. While deep learning models have achieved remarkable progress in general object detection, their performance is limited in complex indoor scenes. Indoor surveillance videos often contain cluttered background objects, among which heads have small scales and diverse poses. In this paper, we propose Motion-aware Pseudo-Siamese Network (MPSN), an end-to-end approach that leverages head motion information to guide deep learning models to extract effective head features in indoor scenarios. By taking the pixel-wise difference between adjacent frames as the auxiliary input, MPSN effectively enhances human head motion information and removes irrelevant background objects. Compared with existing methods, MPSN achieves superior performance on two indoor video datasets. It successfully suppresses static background objects and highlights the moving instances, especially human heads in indoor videos. Different methods to capture head motion also were compared. MPSN demonstrates simplicity and flexibility compared to other methods. We validate its robustness through adversarial experiments with a mathematical solution of small perturbations for robust model selection. To confirm its potential in building control systems, we apply MPSN to occupancy counting. The code is available at https://github.com/pl-share/MPSN.

中文翻译：

> 室内视频人头检测是建筑占用检测的关键组成部分。尽管深度学习模型在通用目标检测上已取得显著进展，但在复杂室内场景下性能受限：室内监控视频常含杂乱的背景物体，而人头尺度小、姿态多样。本文提出**运动感知伪孪生网络（MPSN）**，一种利用人头运动信息引导深度模型在室内场景中提取有效人头特征的端到端方法。MPSN 把**相邻帧的逐像素差分**作为辅助输入，从而增强人头运动信息、剔除无关背景物体。相比现有方法，MPSN 在两个室内视频数据集上取得了更优性能，能成功抑制静态背景物体、凸显运动实例（尤其是室内视频中的人头）。本文还对比了不同的人头运动捕获方式，MPSN 在简洁性与灵活性上更具优势。我们通过对抗实验验证其鲁棒性，并给出小扰动的数学解用于鲁棒模型选择。为验证其在建筑控制系统中的潜力，我们将 MPSN 应用于占用计数。代码见 https://github.com/pl-share/MPSN。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：人员维度信息对建筑节能与室内舒适至关重要。论文引用的研究指出，基于占用信息的控制策略可节约建筑能耗约 20%~45%、提升热舒适约 29.1%（Pang et al., 2020），并为 HVAC 与照明系统提供闭环反馈控制。基于视觉的占用检测因此成为热点。
- **为何选人头检测**：视觉占用检测分为身体（body）、人脸（face）、人头（head）三类。身体检测受类间/类内遮挡影响；人脸检测在目标不正对摄像头时失效；人头在复杂室内场景中可见且可靠，适用范围更广，故成为首选。
- **之前方法的问题**：
    1. 身体检测、人脸检测分别受严重遮挡与朝向限制。
    2. 通用检测器直接用于室内人头检测时：背景物体（黑包、球、花等）在尺寸/颜色/纹理上与人头相似，导致高误报率（FPR）；人头尺度小，拥挤场景中难以高置信度检出，导致高漏检率（FNR）；运动人头还带来尺度、姿态、纹理、光照的剧烈变化。
    3. 多数现有研究面向**静态图像**人头检测，不适用于室内视频。
    4. 已有视频人头检测多依赖**检测框级**后处理（设计追踪器、相邻帧手工规则），只依赖单帧检测器、未联合优化；当目标外观剧变、被遮挡或帧间隔大时不准确。
- **核心观察 / 矛盾**：人头通常在运动，而背景物体几乎总是静止。由此提出关键问题——**能否利用人头运动来增强特征、同时抑制背景信息**，即在特征/像素层面区分并增强人头，而非只做检测框级后处理。

## 关键贡献

论文原文（INTRODUCTION 结尾）列出 5 条贡献：

1. **像素级运动感知伪孪生网络**：提出在像素层面学习更鲁棒人头特征的 pseudo-siamese 网络；据作者所述，MPSN 是**首个把当前帧与像素级运动信息联合训练进端到端 CNN** 的人头检测工作。
2. **更有效的运动特征 + 实测优越且低显存**：在 crowd Brainwash 数据集与 Restaurant 数据集上展示了更优性能与较低的内存需求。
3. **作为通用人头检测框架的灵活性**：可适配不同骨干网络（VGGNet16、MobileNetv2、ResNet18）。
4. **鲁棒性评估**：对 MPSN 施加对抗样本，并给出**小扰动的数学解**以选择更鲁棒的模型。
5. **应用潜力**：将 MPSN 用于占用计数（occupancy counting），验证其在实际建筑控制系统中的潜力。

> 注：原笔记把"特征聚合（SFA/DFA）"单列为一条贡献，但论文官方贡献清单是上述 5 条；SFA/DFA 属于第 1 条网络设计的内部组件，本节按原文订正。

## 方法

- **整体形式化**：给定图像，特征提取网络记 `N_feat`、检测网络记 `N_det`，输出为 `N_det(h)`，其中 `h = N_feat(I)`。核心思想是用运动信息在**像素层面**抑制静态背景、聚焦人头实例。
- **推理流水线（图2，4 个模块）**：
    1. **运动估计模块**：估计人头运动信息，喂给伪孪生网络。
    2. **特征聚合模块**：提取鲁棒的人头运动特征（SFA + DFA）。
    3. **梯度反传模块**：解释 MPSN 的梯度原理，**详见附录**（提取文本未含附录正文）。
    4. **检测网络模块**：把聚合特征解码为人头框。
- **输入输出**：输入为当前帧 `I_f` 与前一帧 `I_{f-1}`；输出为当前帧人头框及类别。
- **运动估计（3.1）**：
    - 帧差算子（公式1）：`I_df = |I_f − I_{f-1}|`，对 RGB 三通道分别计算。该算子对运动像素敏感、含空间位置信息，且对帧间隔的大变化较鲁棒。
    - 另定义基于光流的运动场（公式2）：`I_df = F(I_f, I_{f-1})`，F 为光流估计算法（引用 RAFT / FlowNet / Lucas-Kanade）。
- **伪孪生特征提取（3.2）**：原始帧 `I_f` 与帧差图 `I_df` 并行送入 `N_feat`。由于 `I_df` 与 `I_f` 位于**不同流形**，权重共享的标准孪生网络不适用；故设计**伪孪生网络**——两支子网络结构相同、**权重独立学习**，保证同层尺寸与通道完全一致。网络拆为四支：前向 FN/FDN、后向 BN/BDN，即 `N_feat = {N_FN, N_FDN, N_BN, N_BDN}`，且 `h_fn = N_FN(I_f)`，`h_fdn = N_FDN(I_df)`（公式3，二者形状相同）。
- **特征聚合（3.2）**：
    - **浅层特征聚合 SFA（公式4）**：在低层、激活函数之后直接相加 —— `h_fn = h_fdn + h_fn`，把运动区域叠加到原始特征上以保留更多时序信息。SFA 能增强小而运动的像素，但当存在相似背景物体时不够准确（难保证人头激活值高于背景）。
    - **深层特征聚合 DFA（公式5）**：在高层 position-sensitive score map 上做 —— 先 `h_bn = N_BN(h_fn)`、`h_bdn = N_BDN(h_fdn)`；逐通道用 sigmoid 把 `h_bdn` 压到 (0,1) 当作**稠密可学习掩码** `σ(h_bdn)`，与 `h_bn` 做逐元素（Hadamard）相乘，再加回 `h_bdn`：
      `h_agg = h_bn ⊙ σ(h_bdn) + h_bdn`。
      该掩码不同于图像处理中的普通掩码，是稠密且可学习的；运动实例被部分保留、静态实例被抑制。末尾再加 `h_bdn` 是为补偿——因 `h_bn` 在激活前经过归一化（BN/IN/LN）、`σ(h_bdn)∈(0,1)` 会衰减激活后的人头特征，故加回 `h_bdn` 以补偿损失并增强运动人头区域。
      （订正：原笔记写成 `α·h_bn⊙σ(h_bdn)+β·h_bdn` 的带权形式，但提取文本公式5中**没有 α、β 系数**，此处按原文去除。）
- **检测网络（3.3）**：聚合特征 `h_agg` 送入检测器，`(c, t) = N_det(h_agg)`。`t = (t_x, t_y, t_w, t_h)` 为锚框参数化坐标，`c` 为类别概率。沿用 RPN 思路：每图预测 **5700 个锚框（50×38×3）**，选 **16×16、32×32、64×64 三种锚框尺寸**覆盖多数人头；每锚预测 4 个回归坐标 + 2 个概率分数，故 `t` 维度 5700×4、`c` 维度 5700×2。GT 框 `G=(G_x,G_y,G_w,G_h)` 经公式7 转为参数化坐标 `t`（中心偏移 + log 宽高比），分类 GT 由"锚是否含人头（1/0）"直接生成。
- **损失与训练**：多任务损失（公式8）`L(c,t) = (1/N_s) Σ_i [L_cla(c_i, ĉ_i) + L_box(t_i, t̂_i)]`，`L_cla` 为交叉熵、`L_box` 为 smooth L1；按正样本数 `N_s` 归一化，且仅用正样本计算。正样本定义三策略：(1) 与 GT 的 IoU ≥ 0.7；(2) 取与每个 GT 最大 IoU 的锚；(3) 每图正样本数限制 ≤ 16。骨干与检测器**端到端联合训练**，训练超参在附录（提取文本未含）。
- **与已有方法的差异**：框级后处理（追踪器）只依赖单帧检测器、不联合优化；MPSN 在**像素级 + 特征级**（前处理）工作，把运动先验融入特征学习，是该领域少见的特征/像素级人头检测方案。

## 实验

- **数据集（4.1）**：
    1. **Brainwash**（Stewart et al., 2016）：11917 张图、91146 个标注人头，测试集 484 张。
    2. **Restaurant**（El Ahmar et al., 2020）：采集自餐厅 4 个不同室内位置，1610 张图，测试集 123 张；图像从视频中以**大时间间隔**抽取，多样性/差异性大；摄像头稳定，故所提运动估计方法适用。
- **评价指标**：标准平均精度 **AP50**。
- **对比方法（表1）**：ReInspect、SSD、DETR、FCHD、CrowdDet、Iter-E2EDET（Brainwash）；YOLOX、HTC++、SSD、FCHD、CrowdDet、Iter-E2EDET（Restaurant）。
- **主结果（表1，AP50，据 PDF 提取文本核对）**：

    | 数据集 | 方法 | 骨干 | AP50 |
    |---|---|---|---|
    | Brainwash | ReInspect | GoogLeNet | 0.78 |
    | Brainwash | SSD | ResNet101 | 0.80 |
    | Brainwash | DETR | ResNet18 | 0.53 |
    | Brainwash | FCHD | VGGNet16 | 0.70 |
    | Brainwash | CrowdDet | ResNet50 | 0.67 |
    | Brainwash | Iter-E2EDET | ResNet50 | 0.52 |
    | **Brainwash** | **MPSN** | **MobileNetv2** | **0.90** |
    | **Brainwash** | **MPSN** | **VGGNet16** | **0.91** |
    | Restaurant | YOLOX | CSPNet | 0.83 |
    | Restaurant | HTC++ | Swin-B | 0.68 |
    | Restaurant | SSD | ResNet18 | 0.51 |
    | Restaurant | FCHD | VGGNet16 | 0.75 |
    | Restaurant | CrowdDet | ResNet50 | 0.61 |
    | Restaurant | Iter-E2EDET | ResNet50 | 0.61 |
    | **Restaurant** | **MPSN** | **MobileNetv2** | **0.84** |
    | **Restaurant** | **MPSN** | **VGGNet16** | **0.86** |

    MPSN(VGGNet16) 在两数据集上均最高（0.91 / 0.86），显著超过基线 FCHD(0.70 / 0.75)。
- **后续实验（按 4 开头规划，据原文 §4 概述，提取缓存未覆盖正文，待核）**：§4.2~4.4 围绕灵活性与对比（SFA/DFA 可嵌入多数 CNN，多骨干/多检测器）；§4.5 选最优模型做室内占用计数、平衡低算力与高精度；§4.6 用对抗样本评估鲁棒性，并给小扰动数学解选鲁棒模型。这些章节的**具体数值/消融表**在提取文本中未出现（PDF 文本未明确）。

## 局限

1. **场景假设依赖**：方法建立在"人头不会长时间静止"与"摄像头稳定"两个前提上（§4.1 明确"camera was stable 故运动估计适用"）。摄像头移动、或人头长时间静止（如熟睡）时，帧差信号弱，方法可能失效。
2. **运动捕获方式的敏感度**：帧差对运动像素敏感但依赖帧间差异；过大或过小的运动、不同帧间隔可能影响表现（论文专门对比了不同运动捕获方式，但提取文本未给该对比的数值）。
3. **实验证据的可见性**：提取缓存仅覆盖到 §4.2 开头，SFA/DFA 各自贡献的消融、对抗鲁棒性、占用计数、算力/速度等对比数值在已提取文本中不可见（PDF 文本未明确）。
4. **数据集覆盖**：仅在 Brainwash（人群/办公场景）与 Restaurant（餐厅）两个室内数据集上验证，对商场、走廊、医院等更广室内场景的泛化未在可见文本中给出。

## 个人评论

> 本节为 AI 生成的评述。

这篇论文最值得学习的核心思想是：**把视频中的运动信息当作强先验，从"检测框级后处理"提升到"特征级联合学习"**。几点启发：
1. **简单操作 + 精心结构 = 显著增益**：逐像素帧差是最朴素的背景建模，但经伪孪生 + SFA/DFA 后，在 Brainwash 上把 FCHD 的 0.70 提到 0.91，说明"信号来源简单"不等于"价值低"，关键在如何把它注入特征学习。
2. **条件特征增强范式**：DFA 用一支辅助流（运动）生成稠密可学习掩码 `σ(h_bdn)` 去调制主流特征 `h_bn`，并加回辅助特征补偿激活衰减——这是一种可迁移的"用辅助模态门控主干特征"思路，深度图、热力图、光流都能套用。注意它特意区分了"标准孪生（共享权重）不适用，因两输入在不同流形上"——把这一点想清楚是该设计成立的前提。
3. **问题定义先于模型选择**：先抓住"人头动、背景静"这一领域先验，再设计抑制静态/增强运动的结构，比直接把通用检测器搬到室内更有效。
4. **工程闭环意识**：论文不止刷点，还接了对抗鲁棒性 + 小扰动数学解 + 占用计数落地，体现了"面向建筑控制系统部署"的完整链路，值得在写应用型论文时借鉴。

### 使用建议

- **快速了解**：读摘要、图1（FCHD vs MPSN 的 CAM 热图对比）、图2（框架）、表1。可在几分钟内抓住问题、思路与效果。
- **复现**：精读 §3 与公式1-8；注意网络架构细节、训练超参、梯度反传模块均在**附录**（提取文本未含），需查原文附录与官方代码 https://github.com/pl-share/MPSN。
- **借鉴创新点**：聚焦 §3.2 的 SFA/DFA，尤其 DFA 用运动特征生成掩码调制原始特征的设计，可迁移到光流/深度/文本等辅助信息引导主干的任务。
- **写 Related Work**：可归入 1) 基于深度学习的室内人头/行人检测；2) 视频目标检测中的运动信息利用；3) 建筑占用感知的视觉方法。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C2_目标检测_违建_车辆_船舶_行人]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**计算机视觉 / 目标检测**方向，具体任务是**室内视频中的人头检测（indoor video head detection）**，服务于**建筑占用检测（building occupancy detection）**这一应用目标。它要解决的是：复杂室内场景下，如何利用视频相邻帧的运动信息提升人头检测的准确率（同时降低误报 FPR 与漏检 FNR）。在本库 taxonomy 中归入 **C2_目标检测_违建_车辆_船舶_行人**（人头/人员检测属于行人/人员目标检测一类）；亦与"视频目标检测""智能建筑占用感知"主题相关。

## 2. 一句话总结
本文提出运动感知伪孪生网络 MPSN，把相邻帧逐像素差分作为辅助输入并入端到端 CNN，通过浅层相加（SFA）与深层掩码调制（DFA）增强运动人头、抑制静态背景，在 Brainwash 与 Restaurant 两个室内数据集上以 AP50 0.91 / 0.86 显著超过 FCHD 等基线。

## 3. 背景与问题
- **为什么要做**：占用信息驱动的控制可节约建筑能耗约 20%~45%、提升热舒适约 29.1%（论文引用 Pang et al., 2020），是 HVAC/照明闭环控制的基础；视觉占用检测因此成为热点。
- **为何用人头**：身体检测受遮挡、人脸检测受朝向限制；人头在复杂室内场景中可见可靠，适用范围更广。
- **之前方法的问题**：
    1. 通用检测器直接用于室内人头检测时，背景物体（黑包、球、花）与人头在尺寸/颜色/纹理上相似 → 高 FPR；人头尺度小、拥挤 → 高 FNR；运动还带来尺度/姿态/纹理/光照剧变。
    2. 多数研究面向**静态图像**，不适配视频。
    3. 已有视频方法多为**检测框级**后处理（追踪器 + 手工帧间规则），只依赖单帧检测器、不联合优化，目标外观剧变或帧间隔大时失效。
- **核心观察**：人头常运动、背景几乎总静止 → 用运动增强特征、抑制背景，可同时降低 FPR 与 FNR。

## 4. 核心贡献
论文官方列出 5 条：
1. 提出像素级运动感知伪孪生网络以学习更鲁棒人头特征；声称是首个将当前帧与像素级运动信息联合训练进端到端 CNN 的人头检测工作。
2. 借更有效的运动特征，在 Brainwash 与 Restaurant 上取得优越性能且内存需求低。
3. 作为通用人头检测框架，展示对不同骨干（VGGNet16 / MobileNetv2 / ResNet18）的灵活性。
4. 用对抗样本评估鲁棒性，并给出小扰动数学解以选择更鲁棒模型。
5. 应用于占用计数，验证在建筑控制系统中的潜力。
（SFA/DFA 是第 1 条网络设计的内部组件，非独立贡献项。）

## 5. 方法详解
- **形式化**：`h = N_feat(I)`，输出 `N_det(h)`；核心是用运动信息在像素层面抑制静态背景、聚焦人头。
- **流水线（图2 四模块）**：运动估计 → 特征聚合（SFA/DFA）→ 梯度反传模块（附录，未提取）→ 检测网络。
- **运动估计（3.1）**：帧差 `I_df=|I_f−I_{f-1}|`（公式1，RGB 逐通道，对运动像素敏感、含空间位置、对帧间隔变化鲁棒）；或光流 `I_df=F(I_f,I_{f-1})`（公式2）。
- **伪孪生（3.2）**：`I_f` 与 `I_df` 位于不同流形，故弃用权重共享的标准孪生，改用**结构相同、权重独立**的伪孪生；四支子网络 `{N_FN,N_FDN,N_BN,N_BDN}`，`h_fn=N_FN(I_f)`、`h_fdn=N_FDN(I_df)`，同层形状一致（公式3）。
- **SFA（公式4）**：`h_fn = h_fdn + h_fn`，低层激活后直接相加，保留时序信息、增强运动小像素；相似背景存在时不够准确。
- **DFA（公式5）**：`h_bn=N_BN(h_fn)`、`h_bdn=N_BDN(h_fdn)`；`h_agg = h_bn ⊙ σ(h_bdn) + h_bdn`。`σ(h_bdn)∈(0,1)` 是逐通道、稠密、可学习的掩码，与 `h_bn` 做 Hadamard 积以激活原始特征图的局部区域；末尾加回 `h_bdn` 补偿（因 `h_bn` 归一化 + sigmoid 压缩导致人头激活衰减）。**公式中无 α/β 系数**（订正原笔记）。
- **检测网络（3.3）**：`(c,t)=N_det(h_agg)`；每图预测 5700（=50×38×3）个锚框，锚框尺寸 16/32/64 三种，每锚 4 回归 + 2 分类 → `t`:5700×4、`c`:5700×2；GT 经公式7 参数化为中心偏移 + log 宽高比。
- **损失（公式8）**：`L=(1/N_s)Σ[L_cla+L_box]`，交叉熵 + smooth L1，仅用正样本、按 N_s 归一；正样本三策略：IoU≥0.7、每 GT 最大 IoU、每图 ≤16。端到端联合训练，超参在附录（未提取）。

## 6. 实验与结果
- **数据集**：Brainwash 11917 图 / 91146 人头 / 测试 484；Restaurant 4 地点 1610 图 / 测试 123，大时间间隔抽帧、摄像头稳定。
- **指标**：AP50。
- **表1 主结果（已据提取文本逐行核对）**：Brainwash 上 MPSN MobileNetv2/VGGNet16 = 0.90 / 0.91，超 FCHD 0.70、SSD 0.80、DETR 0.53、CrowdDet 0.67、Iter-E2EDET 0.52、ReInspect 0.78；Restaurant 上 MPSN = 0.84 / 0.86，超 FCHD 0.75、YOLOX 0.83、HTC++ 0.68、SSD 0.51、CrowdDet/Iter-E2EDET 0.61。
- **未覆盖部分**：§4.2~4.6 的灵活性对比、运动捕获方式对比、占用计数、对抗鲁棒性、算力/速度等具体数值在提取缓存中不可见（PDF 文本未明确）。

## 7. 这篇论文真正有价值的地方
核心是把视频运动信息从"检测框级后处理"上升为"特征级联合学习"。可学之处：
1. **简单操作 + 精心结构的杠杆效应**：逐像素帧差 + 伪孪生/特征聚合，把 FCHD 的 0.70 提到 0.91。
2. **条件特征增强范式**：DFA 用辅助（运动）流生成稠密可学习掩码门控主干特征，并加回辅助特征补偿激活衰减——可迁移到深度/热力/光流等辅助模态。
3. **流形差异的工程判断**：明确论证"两输入不同流形 → 标准孪生不适用 → 改伪孪生"，是该设计的关键前提。
4. **领域先验先于模型**：抓住"人头动、背景静"再设计结构，比直接套通用检测器更有效。

## 8. 局限与问题
1. **强场景假设**：依赖"人头不长时间静止"+"摄像头稳定"；摄像头移动或人头静止时帧差信号弱，可能失效。
2. **运动捕获敏感度**：帧差依赖帧间差异，过大/过小运动或不同帧间隔可能影响性能。
3. **可见证据有限**：提取缓存仅到 §4.2 开头，消融（SFA/DFA 各自贡献）、鲁棒性、占用计数、效率等数值不可见。
4. **数据集覆盖窄**：仅两个室内数据集，更广室内场景泛化未在可见文本中给出。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 图1（CAM 对比）+ 图2（框架）+ 表1。
- **复现**：精读 §3 与公式1-8；架构/超参/梯度反传在附录（未提取），结合官方代码 https://github.com/pl-share/MPSN。
- **借鉴创新点**：深读 §3.2 的 SFA/DFA，迁移 DFA 的"辅助流生成掩码调制主干"思想。
- **写 Related Work**：归入室内人头/行人检测、视频检测中的运动利用、建筑占用视觉感知三类。

## 10. 和其他论文的关系
- **[[FCHD (Meng et al., 2020)]]**：核心基线（图1 直接对比 CAM，表1 中 VGGNet16 骨干 0.70/0.75）。
- **[[Brainwash (Stewart et al., 2016)]]**：主评测数据集来源。
- **Restaurant (El Ahmar et al., 2020)**：第二评测数据集。
- **[[DETR]]**、**[[SSD]]**、**[[YOLOX]]**、**CrowdDet**、**Iter-E2EDET**、**HTC++**、**ReInspect**：表1 对比方法。
- **RPN (Ren et al., 2015)**：检测头基础。
- **光流估计（Teed & Deng 2020 / Ilg et al. 2017 / Lucas-Kanade 1981）**：公式2 运动场所引方法。
- **CAM (Zhou et al., 2016)**：图1 热图可视化方法。

## 11. 关键词
室内人头检测、建筑占用检测、运动估计（帧差/光流）、伪孪生网络、浅层/深层特征聚合（SFA/DFA）、稠密可学习掩码、RPN、多任务损失、对抗鲁棒性、小扰动数学解、占用计数

## 12. 可信度说明
本精读主要基于 PDF 提取文本（覆盖标题、作者、摘要、§1 引言、§2 相关工作、§3 方法全部公式1-8、§4.1 数据集与表1 完整结果，并延伸到 §4.2 开头）。
- **可靠部分**：论文定位、背景动机、5 条贡献、方法细节（公式1-8、伪孪生/SFA/DFA、检测网络与锚框配置）、表1 全部 AP50 数值——均可在提取文本逐条核对。
- **本轮订正**：DFA 公式（公式5）按原文去除 α/β 系数；贡献清单按原文 5 条重排；摘要由乱码直提重建为清理后英文 + 中文译文；primary_topic 由 `T_通用_NLP_其他` 改为 `C2_目标检测_违建_车辆_船舶_行人`。
- **信息缺失部分**：§4.2~4.6 的消融、灵活性/运动捕获对比、对抗鲁棒性、占用计数、算力/速度，以及附录（网络架构细节、训练超参、梯度反传模块）在提取缓存中不可见，对应论断已标注"PDF 文本未明确"。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本约 2086 字符/页, 覆盖 §1-§4.1 + 表1 完整); 来源缓存: `.paper-cache/extracts/2021_MPSN_Motion-aware_P.txt` (提取头标 12/13 页, 缓存按 25000 字符截断, 后续 §4.2 之后内容未入缓存); 生成日期: 2026-06-04; 本轮重读订正日期: 2026-06-18; 模式: LLM (mimo-v2.5-pro) + 本轮据提取文本人工对照重写。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-13。
- **提取情况**: 缺失页 1 页, 其中 1 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: MPSN: Motion-aware Pseudo-Siamese Network for Indoor Video Head Detection in Buildings

### 缺失页关键摘录

- p.13: Kailai Sun et al.: Preprint submitted to Elsevier Page 13 of 13
<!-- AI_READING_NOTE_END -->
