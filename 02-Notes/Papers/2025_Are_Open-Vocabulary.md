---
title: Are Open-Vocabulary Models Ready for Detection of MEP
authors:
  - "Abdalwhab Abdalwhab"
  - "Ali Imran"
  - "Sina Heydarian"
  - "Ivanka Iordanova"
  - "David St-Onge"
year: 2025
venue: "Sensors"
doi: 
pdf: [[2025_Are_Open-Vocabulary.pdf]]
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/2025_Are_Open-Vocabulary.txt
---

# Are Open-Vocabulary Models Ready for Detection of MEP

## 基本信息
- **PDF**: [[2025_Are_Open-Vocabulary.pdf]]
- **primary_topic**: `C_目标检测_通用与旋转框`
- **topics**: `C_目标检测_通用与旋转框`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Are Open-Vocabulary Models Ready for Detection of MEP Elements on Construction Sites |
| **作者** | Abdalwhab Abdalwhab; Ali Imran; Sina Heydarian; Ivanka Iordanova; David St-Onge |
| **发表时间** | 2025 (arXiv:2501.09267v2, 2025-04-12) |
| **刊物/会议** | Sensors |
| **机构** | ETS Montreal（Lab INIT Robots / GRIDD），加拿大 |
| **DOI** | 未明确 |

## 摘要

> The construction industry has long explored robotics and computer vision, yet their deployment on construction sites remains very limited. These technologies have the potential to revolutionize traditional workflows by enhancing accuracy, efficiency, and safety in construction management. Ground robots equipped with advanced vision systems could automate tasks such as monitoring mechanical, electrical, and plumbing (MEP) systems. The present research evaluates the applicability of open-vocabulary vision-language models compared to fine-tuned, lightweight, closed-set object detectors for detecting MEP components using a mobile ground robotic platform. A dataset collected with cameras mounted on a ground robot was manually annotated and analyzed to compare model performance. The results demonstrate that, despite the versatility of vision-language models, fine-tuned lightweight models still largely outperform them in specialized environments and for domain-specific tasks.

> **中文翻译**：建筑行业长期探索机器人与计算机视觉技术，但其在工地现场的部署仍非常有限。这些技术有潜力通过提升建筑管理的准确性、效率与安全性来变革传统工作流程。配备先进视觉系统的地面机器人可以自动化诸如监测机械、电气与管道（MEP）系统等任务。本研究评估开放词汇视觉-语言模型与微调过的、轻量级的闭集目标检测器在用移动地面机器人平台检测 MEP 组件这一任务上的适用性对比。研究用安装在地面机器人上的相机采集了一个数据集，对其进行人工标注与分析以比较模型性能。结果表明：尽管视觉-语言模型具有通用性，微调过的轻量级模型在专业环境与领域特定任务中仍大幅胜出。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：移动机器人在建筑业的应用日益增长，被视为缓解劳动力短缺、改善安全的手段（引言引文 [1]）。但工地现场的"场地巡查（site survey）"——监测进度、支撑决策的关键环节——目前仍主要靠人工完成（[3]）。MEP（机械/电气/管道）系统的安装与功能监测尤为重要：能尽早发现问题、避免昂贵返工与工期延误（[4]）。因此作者想用机器人视觉自动化 MEP 检测，但 MEP 检测在动态、非结构化的工地环境中本身就是难点。
- **之前方法的问题**：以 CNN 为代表的监督学习目标检测（如 YOLO）在受控条件下成功，但在遮挡、光照变化、出现训练中未见过的新物体等工地常见情形下表现受限（[5,6,7]）。开放词汇目标检测是另一条路线，能跨多样数据集泛化、识别训练时未见过的物体（[8]），并把大语言模型（LLM）与视觉结合，已在生成检查报告、监测工地等任务上展现潜力（[9]）。其中 Omni-Scan2BIM（[10]）用开放词汇模型识别/分割 MEP 组件以自动生成竣工 BIM，但其只聚焦管道、风管等特定类别，难以推广到更广义的 MEP 监测。
- **核心矛盾**：通用性强的开放词汇模型，是否已经"准备好"在 MEP 这种专业、动态的工地检测任务上，取代需要按特定类别微调的专用轻量级模型？（标题中的 "Are ... Ready" 即此问。）

## 关键贡献

1.  **构建了一个真实工地 MEP 数据集**：用配备多相机+LiDAR 的移动机器人（Journeybot）在一个活跃工地（由产业合作方提供）采集，人工标注 10 类 MEP 组件，共 **8885 张图像、14064 个实例**，并已在线公开。
2.  **系统对比评估**：将在本数据集上微调的轻量闭集检测器 **YOLO11 Nano**，与三个有代表性的预训练开放词汇模型 **Grounded SAM2、Grounding DINO、DETIC**（均不微调）在同一 MEP 测试集上比较。
3.  **量化了性能差距**：YOLO11 在精确率（0.87 vs 开放词汇模型最高仅 0.02）、召回率（0.901 vs 最高 0.084）、F1（0.89 vs 最高 0.032）上全面、大幅领先；相对最佳开放词汇模型（GDINO）的提升超过 85%（精确率）、82%（召回率）、86%（F1）。
4.  **评估实际部署可行性**：从模型参数量与推理速度两个维度评估。YOLO11 Nano 仅 **2.6M 参数**，可在 NVIDIA Jetson Orin Nano 上达 **23.36 FPS** 满足实时；而最小的开放词汇模型（DETIC，164M）参数量也是它的 63 倍。
5.  **指出未来方向**：建议在专业数据集上微调开放词汇模型（结合其适应性与监督模型的精度），或设计建筑相关的提示词（prompt）来适配开放词汇检测器。

## 方法

本文是一篇**比较实验 / 基准（Benchmark）** 论文，"方法"核心在于严谨的实验设置，而非提出新网络模块。

- **整体框架**：数据收集 → 数据集构建（抽帧+滤除冗余/模糊帧+人工标注）→ 模型训练（仅 YOLO11）/直接加载（开放词汇模型）→ 在同一测试集评估 → 结果分析。
- **机器人平台 Journeybot**：四轮无人地面车（UGV），混合视觉+激光传感系统。含 4 个 Intel RealSense D435i 立体相机（覆盖四周，其中一个朝上）、1 个前向 Intel RealSense T265 跟踪相机（增强定位）、Velodyne Puck 32MR LiDAR 与 Ouster LiDAR（两个 LiDAR 本工作未用）。轮式编码器、IMU 与检测传感器由 NVIDIA Jetson 同步。数据采集时为安全起见由人手动遥操作。
- **输入输出**：输入是机器人相机拍摄的工地 RGB 图像；输出是 MEP 组件的类别标签与边界框。
- **对比模型**：
    - **闭集检测器**：YOLO11 Nano，COCO 预训练权重基础上在本数据集微调 200 epoch；取验证集上最佳权重用于测试。需针对特定类别训练。
    - **开放词汇模型**：Grounded SAM2 (GSAM2)、Grounding DINO (GDINO)、DETIC，均用预训练权重，**不做任何微调**直接评估。
- **数据划分**：70% 训练 / 20% 验证 / 10% 测试。
- **评估协议**：所有模型在同一测试集、IoU=0.5 下计算 precision / recall / F1。
- **与已有工作差异**：Omni-Scan2BIM 等[10]用开放词汇模型做特定任务（如 BIM 生成），但未系统比较其与专用检测器在通用 MEP 检测上的表现；本文填补该对比评估空白。

## 实验

- **数据集（Table 1）**：自建 MEP 数据集，10 类，共 8885 图 / 14064 实例。各类图像(实例)数：1 Boiler 768(769)、2 Cable Tray fitting 252(317)、3 Electrical Panel 658(1022)、4 Fire Alarm Detector 872(877)、5 Pipe Fitting 3625(5014)、6 Valve 610(906)、7 Electrical Outlet 786(1023)、8 Generator 124(124)、9 Light 1992(2168)、10 Pump 1536(1844)。可见类别高度不均衡（Pipe Fitting 最多，Generator 仅 124 张）。图像从 rosbag 以 10 Hz 抽帧后滤除冗余/模糊。
- **对比方法**：YOLO11 Nano（微调闭集）、GSAM2、GDINO、DETIC（三者开放词汇、零样本）。
- **评价指标**：Precision、Recall、F1，均在测试集 IoU=0.5 计算。
- **整体结果**：
    - Precision：YOLO11 **0.87** vs GSAM2 0.018 / GDINO 0.02 / DETIC 0.015。
    - Recall：YOLO11 **0.901** vs GSAM2 0.042 / GDINO 0.084 / DETIC 0.018。
    - F1（total）：YOLO11 **0.89** vs GSAM2 0.018 / GDINO 0.032 / DETIC 0.014。
    - 相对最佳开放词汇模型 GDINO，YOLO11 在 precision/recall/F1 上分别提升超过 85% / 82% / 86%。
- **逐类 F1（Table 2，YOLO11）**：1→0.94、2→0.86、3→0.90、4→0.94、5→0.86、6→0.87、7→0.82、8→0.92、9→0.81、10→0.93（范围 0.81–0.94，全类稳健）。开放词汇模型多类彻底失效（F1=0）：Cable Tray fitting（类 2）无任何开放词汇模型检测出；DETIC 在 10 类中有 5 类失败（表现最差），GSAM2 与 GDINO 各在 2 类失败。
- **不均衡处理**：混淆矩阵（Figure 2）显示 YOLO11 即使对样本极少的 Generator（仅 124 张）也达 91% 检测准确率，说明其能较好处理领域内的类别不均衡。
- **定性观察（Figure 3）**：部分情形下 YOLO11 甚至优于人工标注（识别出被漏标的阀门）；对模糊图像能避免误检、与标注者的局限一致；但偶有误检，尤其反光表面会被误判成"光源（Light）"类。
- **效率分析（Real-world Applicability）**：
    - 参数量：GSAM2 910M（YOLO11 的 350 倍） > GDINO（67 倍 ≈ 174M，注：174M 由 67×2.6M 推算，原文只给"67 倍"） > DETIC 164M（63 倍） ≫ YOLO11 Nano 2.6M。
    - 推理速度：YOLO11 Nano 在 NVIDIA Jetson Orin Nano 上 **23.36 FPS**，满足实时；文中未给出开放词汇模型的具体速度，但指出其算力需求大、不适合资源受限平台。
- **消融实验**：无传统意义上的消融；泛化/鲁棒性通过逐类与不均衡类别（如 Generator）的稳定表现间接体现。

## 局限

1.  **任务与场景局限**：仅评估静态图像的 2D 目标检测，未涉及视频流、时序信息、三维重建或更复杂语义理解；而工地是高度动态的。
2.  **数据集局限**：虽来自真实工地，但仅 10 类 MEP 组件、来自单一工地（一个产业合作方），多样性可能不足以评估更广建筑场景下的泛化。
3.  **模型选择有限**：只对比少数几个开放词汇模型；该领域迭代快（如引文 [8] 的 YOLO-World），结论可能有时效性。
4.  **未探索范式融合**：直接对比"微调 vs 零样本"两种范式，未尝试结合（如用开放词汇模型生成伪标签、或用其区域建议能力）；而作者自己也把"在专业数据集上微调开放词汇模型"列为未来方向。
5.  **评估指标单一**：主要基于 IoU=0.5，未报告更严格阈值（如 0.75）或 mAP / 定位精度等细节。

## 个人评论

1.  **结论清晰可落地**：对建筑机器人感知研究者，结论很直接——在资源受限、需高精度的实时 MEP 检测场景下，应优先对 YOLO 这类轻量模型做**领域数据微调**，而非直接套用庞大的开放词汇模型。其 0.89 vs 0.032 的 F1 量级差距非常醒目。
2.  **揭示了数据表征鸿沟**：性能瓶颈的根因被点明——开放词汇模型依赖 COCO/LVIS 这类通用数据集，缺乏对 MEP 专用组件（如电缆桥架配件）的表征，所以"开放"不等于在任何领域都"好用"。这是对当前 VLM 热潮一个有价值的冷思考。
3.  **值得商榷的公平性**：开放词汇模型完全零样本、且未做任何提示词工程，与微调 200 epoch 的 YOLO 对比，本身就不是同一起跑线；F1≈0.02 之低也提示提示词/类别名映射可能未优化。作者把"设计建筑相关 prompt"列为未来工作，恰恰说明这次对比可能低估了开放词汇模型的上限。读者宜把本文当作"现成开箱即用条件下"的结论，而非"开放词汇范式不行"的定论。
4.  **可复现性强**：贡献了公开数据集，并较完整地交代了平台、训练细节与评估协议，为后续工作提供了可靠基准。

### 使用建议

- **如果快速了解**：读**摘要**、**结论**与 **Table 2**（逐类 F1）即可掌握核心发现。
- **如果复现**：重点看 **第2节 Experimental Setup**——数据集构建（ROS、rosbag、10 Hz 抽帧、滤冗余/模糊）、YOLO11 Nano 微调（COCO 预训练 + 200 epoch、取验证集最佳权重）与评估协议（IoU=0.5）。数据集已公开。
- **如果借鉴创新点**：学习其在特定领域内构建公平基准、并从**准确性 / 效率 / 部署可行性**多维度评估不同范式的思路。
- **如果写 related work**：可归入"建筑工地自动化检测""机器人视觉感知"或"开放词汇检测的领域应用评估"。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C_目标检测_通用与旋转框]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**机器人学 × 计算机视觉 × 建筑自动化**的交叉领域，本质是一篇**目标检测基准/对比评估**论文。它聚焦一个具体而实用的问题：在用移动机器人检测建筑工地 MEP（机械/电气/管道）组件这一任务上，预训练的开放词汇视觉-语言模型，是否能与按特定类别微调的轻量级闭集检测器相抗衡。论文不提出新网络，而是用自建数据集做严谨的横向比较，回答"开放词汇模型是否已经准备好"。适合放在"目标检测""开放词汇检测的领域应用评估"或"建筑工地自动化"主题下。

## 2. 一句话总结
作者用机器人在真实工地采集并标注了一个 10 类、8885 张图的 MEP 数据集，发现微调后的 YOLO11 Nano 在精确率/召回率/F1 和推理效率上都以数量级优势碾压零样本的 Grounded SAM2、Grounding DINO、DETIC，说明当前开放词汇模型在这类专业领域任务上尚未"准备好"取代微调的轻量专用模型。

## 3. 背景与问题
- **为什么要做**：移动机器人正被引入建筑业以缓解用工短缺、提升安全（[1]），但工地巡查这一关键环节仍主要靠人工（[3]）。MEP 系统的安装/功能监测能尽早发现问题、避免返工与延误（[4]），是自动化的高价值靶点；但 MEP 检测在动态非结构化工地中本身就难。
- **之前方法的问题**：CNN/YOLO 类监督检测在受控条件下成功，但遇遮挡、光照变化、训练未见过的新物体时受限（[5,6,7]）。开放词汇检测能跨数据集泛化、识别未见类（[8]），并已在工地报告生成、监测等任务展现潜力（[9]，如 Omni-Scan2BIM [10] 做 MEP→BIM），但后者只覆盖少数特定类别，难推广。
- **核心矛盾**：通用性强的开放词汇模型，能否在专业、动态的工地 MEP 检测上取代需按类别微调的专用轻量模型？

## 4. 核心贡献
1.  自建并公开真实工地 MEP 数据集：10 类、8885 图 / 14064 实例，由 Journeybot 机器人遥操作采集、人工标注。
2.  首次在同一 MEP 数据集上系统对比微调的 YOLO11 Nano 与三个零样本开放词汇模型（GSAM2、GDINO、DETIC）。
3.  量化性能差距：YOLO11 全面领先（P 0.87、R 0.901、F1 0.89），较最佳开放词汇模型 GDINO 提升 >85%/82%/86%。
4.  评估部署可行性：YOLO11 Nano 2.6M 参数、Jetson Orin Nano 上 23.36 FPS；开放词汇模型参数量为其 63–350 倍。
5.  指出未来方向：在专业数据集上微调开放词汇模型，或设计建筑相关 prompt。

## 5. 方法详解
这是一篇 Benchmark 论文，核心在实验设置而非新模块。
- **流程**：数据收集 → 抽帧滤帧 → 人工标注 10 类 → 仅训练 YOLO11（加载其余三模型）→ 同一测试集 IoU=0.5 评估 → 分析。
- **平台 Journeybot**：四轮 UGV，4× RealSense D435i 立体相机（含一朝上）、前向 T265 跟踪相机、Velodyne Puck 32MR + Ouster LiDAR（两 LiDAR 本工作未用），轮编码器/IMU 由 NVIDIA Jetson 同步；采集时人工遥操作。
- **对比模型**：YOLO11 Nano（COCO 预训练 + 本集微调 200 epoch，取验证集最佳权重）；GSAM2 / GDINO / DETIC（预训练权重、零样本、不微调）。
- **数据划分**：70/20/10（训练/验证/测试）。
- **评估**：统一 IoU=0.5，指标 P/R/F1。
- **与已有工作差异**：Omni-Scan2BIM[10] 等用开放词汇模型做特定任务但未与专用检测器系统对比，本文填补此空白。

## 6. 实验与结果
- **数据集（Table 1）**：10 类、8885 图 / 14064 实例，高度不均衡（Pipe Fitting 3625 图最多，Generator 124 图最少）。
- **整体指标（IoU=0.5）**：
    - Precision：YOLO11 0.87 | GSAM2 0.018 | GDINO 0.02 | DETIC 0.015。
    - Recall：YOLO11 0.901 | GSAM2 0.042 | GDINO 0.084 | DETIC 0.018。
    - F1：YOLO11 0.89 | GSAM2 0.018 | GDINO 0.032 | DETIC 0.014。
    - 相对最佳开放词汇模型 GDINO 提升 >85%(P)/82%(R)/86%(F1)。
- **逐类 F1（Table 2，YOLO11）**：0.81–0.94 全类稳健（类 9 Light 最低 0.81；类 1、4 最高 0.94）。开放词汇模型：Cable Tray fitting（类 2）无一检出；DETIC 5/10 类失败（最差），GSAM2、GDINO 各 2 类失败。失败主因是其依赖 COCO/LVIS 等通用数据，缺 MEP 专用组件表征。
- **不均衡鲁棒性**：混淆矩阵（Fig.2）显示 YOLO11 对样本极少的 Generator 仍达 91% 准确率。
- **定性（Fig.3）**：YOLO11 偶尔优于人工标注（找出漏标阀门）；模糊图能避免误检；但反光表面易误判为 Light 类。
- **效率**：参数量 GSAM2 910M(350×) / GDINO 67× / DETIC 164M(63×) vs YOLO11 2.6M；YOLO11 在 Jetson Orin Nano 23.36 FPS（开放词汇模型速度未报告）。
- **消融**：无传统消融；以逐类与不均衡类表现间接体现泛化。

## 7. 这篇论文真正有价值的地方
1.  **给出可直接落地的工程结论**：资源受限的实时 MEP 检测，优先微调 YOLO 类轻量模型而非套用开放词汇大模型；性能差距是数量级的（F1 0.89 vs 0.032）。
2.  **点明数据表征鸿沟**：开放词汇模型在专业领域失效的根因是通用预训练数据缺乏专用组件表征——"开放"≠在任何领域都好用。
3.  **可复现**：公开数据集 + 明确的平台/训练/评估协议，构成可靠基准。
4.  **指明融合路径**：在专业数据上微调开放词汇模型、或设计建筑 prompt，可能催生兼具通用性与专业精度的下一代检测器。

## 8. 局限与问题
1.  仅静态图像 2D 检测，未用视频/时序/3D，而工地高度动态。
2.  数据来自单一工地、仅 10 类，多样性与跨场景泛化未充分验证。
3.  只对比少数开放词汇模型，领域迭代快（如 YOLO-World [8]），结论或有时效。
4.  未尝试两种范式融合（伪标签、区域建议复用等）。
5.  **公平性存疑**：开放词汇模型零样本且未做提示词工程，与微调 200 epoch 的 YOLO 对比起跑线不同；F1≈0.02 之低也提示其上限可能被低估——作者自己把"设计建筑 prompt"列为未来工作即旁证。
6.  指标仅 IoU=0.5，未报告更严阈值或 mAP/定位精度。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要、结论与 Table 2 即可。
- **复现**：看第2节 Experimental Setup（ROS/rosbag/10Hz 抽帧、YOLO11 微调 200 epoch、IoU=0.5），数据集已公开。
- **借鉴创新点**：学习其在特定领域构建公平基准、从准确性/效率/部署可行性多维评估的思路。
- **写 related work**：归入"建筑工地自动化检测""机器人视觉感知"或"开放词汇检测的领域应用评估"。

## 10. 和其他论文的关系
基于真实主题 `C_目标检测_通用与旋转框`（这是一篇 MEP 目标检测的基准/对比论文，并非 NLP），相关方向包括：
- 开放词汇检测：`[[YOLO-World: 实时开放词汇目标检测]]`（引文[8]）、`[[Grounding DINO: 开放集目标检测]]`（引文[14]）、`[[Grounded SAM: 组装开放世界模型]]`（引文[13]）、`[[DETIC: 用图像级监督检测两万类]]`（引文[15]）。
- 闭集轻量检测：`[[YOLOv11 架构增强综述]]`（引文[12]）。
- 建筑机器人与 MEP/BIM：`[[机器人在建筑工地部署的安全与生产力考量]]`（引文[2]）、`[[Omni-Scan2BIM: 基于视觉基础模型的 MEP 场景 BIM 生成]]`（引文[10]）、`[[工地小目标与遮挡工人检测]]`（引文[5]）。
- 通用检测数据集：`[[COCO]]`（引文[16]）、`[[LVIS]]`（引文[17]）。

## 11. 关键词
机器人学, MEP检测, 开放词汇模型, 目标检测, 建筑自动化, 计算机视觉, 对比评估/基准, YOLO11 Nano, Grounding DINO, Grounded SAM2, DETIC, 移动机器人, 数据集, 微调, 实时部署

## 12. 可信度说明
本精读笔记**完全基于** PDF 提取文本（共 4 页，提取完整）生成，关键数字均逐项核对：
- **定位、贡献、结论、动机**：基于 Abstract、Introduction、Conclusion。
- **实验设置**：基于第2节 Experimental Setup（Journeybot 平台、数据集 Table 1、YOLO11 微调、评估协议）。
- **结果与数字**：基于第3节 Results and Discussion 正文 + Table 1（逐类图/实例数）+ Table 2（逐类 F1）；整体 P/R/F1 与逐类 F1 已逐一对齐原文。
- **效率**：参数量 350×/67×/63× 与 23.36 FPS 出自 Real-world Applicability 段；其中 GDINO 的 "≈174M" 为按 67×2.6M 推算（原文只给倍数），已标注。
- **图信息缺失**：Figure 1（平台）、2（混淆矩阵，含 Generator 91%）、3（定性示例）的视觉内容缺失，但其文字描述已在正文中，足以理解。

---

> **可信度补充**: PDF 提取质量 = **high** (4 页完整提取, 约 4279 字符/页, 数字清晰); 已对照提取文本逐项核对 Table 1/Table 2 与整体 P/R/F1; 主题由 `T_通用_NLP_其他` 修正为 `C_目标检测_通用与旋转框`（本文为 MEP 目标检测基准/对比, 与 NLP 无关）; 来源缓存: `.paper-cache/extracts/2025_Are_Open-Vocabulary.txt` (4/4 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
