---
title: "SmoothNet: A Plug-and-Play Network for"
authors:
  - "Ailing Zeng"
  - "Lei Yang"
  - "Xuan Ju"
  - "Jiefeng Li"
  - "Jianyi Wang"
  - "Qiang Xu"
year: 2021
venue: highly-unbalanced nature of the jitters in the estimated poses, resulting in un-
doi: 
pdf: [[SmoothNet.pdf]]
primary_topic: R2_控制_生物启发_其他跨学科
topics:
  - "R2_控制_生物启发_其他跨学科"
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/SmoothNet.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/34 pages"
---
# SmoothNet: A Plug-and-Play Network for

## 基本信息
- **PDF**: [[SmoothNet.pdf]]
- **primary_topic**: `R2_控制_生物启发_其他跨学科`
- **topics**: `R2_控制_生物启发_其他跨学科`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SmoothNet: A Plug-and-Play Network for |
| **作者** | Ailing Zeng; Lei Yang; Xuan Ju; Jiefeng Li; Jianyi Wang; Qiang Xu |
| **发表时间** | 2021 |
| **刊物/会议** | highly-unbalanced nature of the jitters in the estimated poses, resulting in un- |
| **DOI** | 未明确 |

## 摘要

> When analyzing human motion videos, the output jitters fromexistingposeestimatorsarehighly-unbalancedwithvariedestima- tion errors across frames. Most frames in a video are relatively easy to estimateandonlysufferfromslightjitters.Incontrast,forrarelyseenor occludedactions,theestimatedpositionsofmultiplejointslargelydevi- ate from the ground truth values for a consecutive sequence of frames, rendering significant jitters on them. To tackle this problem, we propose to attach a dedicated temporal- only refinement network to existing pose estimators for jitter mitiga- tion, named SmoothNet. Unlike existing learning-based solutions that employ spatio-temporal models to co-optimize per-frame precision and temporal smoothness at all the joints, SmoothNet models the natu- ral smoothness characteristics in body movements by learning the long- range temporal relations of every joint without considering the noisy correlationsamongjoints.Withasimpleyeteffectivemotion-awarefully- connected network

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**: 人体姿态估计在动作分析、人机交互等领域有广泛应用。然而，将基于图像的姿态估计器直接应用于视频时，输出的关节轨迹会产生严重抖动，尤其是在包含罕见动作或遮挡的连续帧上，导致感知不可靠 (p.1)。
- **之前方法的问题**: 现有的学习方法（端到端网络或精炼网络）通常采用时空模型联合优化单帧精度和所有关节的时间平滑性。这是一个高难度任务，因为在抖动帧中提取的时空特征本身不可靠，且同时优化抖动误差(J)和偏差误差(S)存在“时空优化瓶颈”(p.5)。而传统的低通滤波器（如移动平均、高斯滤波）虽然简单，但会在平滑性和滞后性之间权衡，导致长时抖动场景下精度损失严重 (p.5)。
- **核心矛盾**: 优化单帧位置精度（MPJPE）与优化序列平滑性（Accel）之间的内在矛盾。时空模型试图同时优化两者，但常常顾此失彼；固定滤波器无法根据数据动态调整，导致过度平滑或滞后。
## 关键贡献

1.  **发现抖动的不平衡性**: 系统性地分析了抖动问题，指出严重抖动通常只出现在连续的、由图像质量差、遮挡或罕见姿态构成的“挑战帧”上 (p.2)。
2.  **提出首个数据驱动的纯时间精炼方案**: 据作者所知，这是第一个用于缓解人体运动抖动的、数据驱动的、仅依赖时间信息的精炼解决方案 (p.2)。
3.  **设计简单有效的FCN网络架构**: 设计了基于具有长感受野的残差全连接网络（FCN）的SmoothNet，学习每个关节的时间关系进行平滑，实验证明其优于TCN和Transformer (p.2, p.6)。
4.  **提出运动感知（Motion-aware）变体**: 显式地将速度（一阶运动信息）和加速度（二阶运动信息）注入网络，利用物理先验加速学习收敛并获得更好效果 (p.7)。
5.  **验证了强大的即插即用与跨域泛化能力**: 作为纯时间模型，SmoothNet在11种不同骨干网络、3种任务模态（2D/3D位姿、SMPL参数）和5个数据集上验证了其有效性和可迁移性 (p.2, p.8)。
## 方法

- **整体框架**: SmoothNet是一个插件式（Plug-and-Play）模块，附加在任何现有的2D/3D人体姿态估计器之后。其输入是原始估计器输出的带有抖动的关节坐标序列 `Ŷ ∈ R^{L×C}`，输出是平滑和精炼后的关节坐标序列 `Ĝ ∈ R^{L×C}` (p.3, p.6)。
- **关键模块 (Basic SmoothNet)**: 核心是多个残差连接的全连接（FC）层块，沿时间轴处理输入。每一层的计算如公式(1)所示：`Ŷ_{i,t}^{l+1} = σ(Σ_t w_t^l * Ŷ_{i,t}^l + b^l)`，其中权重 `w_t` 和偏置 `b` 在不同的关节轴 `i` 间共享，激活函数σ默认使用LeakyReLU。这种FCN结构在每个层都具有全局感受野，能更好地容忍长时抖动 (p.6)。
- **运动感知版本 (Motion-aware SmoothNet)**: 在Basic SmoothNet的基础上，增加了对速度和加速度的显式建模。给定输入序列 `Ŷ`，首先计算一阶速度 `V` 和二阶加速度 `A`（如公式2）。网络包含三个并行的FCN分支，分别处理位置、速度和加速度序列。最后，将三个分支顶部的特征拼接，通过一个线性融合层得到最终平滑结果 `Ĝ` (p.7)。
- **输入输出与滑动窗口**: 采用类似滤波器的滑动窗口方案处理长序列。从输入序列中提取一个长度为 `T` 的窗口（论文中T=32），进行精炼，然后以步长 `s`（s≤T，论文中s=1）滑动到下一个窗口，防止丢失末尾帧 (p.7)。
- **训练方式**: 训练损失是位置损失 `L_pose` 和加速度损失 `L_acc` 的简单相加。`L_pose` 衡量预测位姿与真值间的L1误差，`L_acc` 衡量预测加速度（由预测位姿计算）与真值加速度间的L1误差 (p.8)。
- **推理流程**: 训练好的SmoothNet模型接收前端估计器的输出序列，通过滑动窗口方式进行推理，并额外使用滑动窗口平均算法基于精炼结果来避免帧丢失和减少尖峰 (p.9)。
- **与已有方法的差异**:
    1.  **与时空模型相比**: 完全摒弃空间信息，只处理单个关节的时间序列，避免了在抖动帧中引入不可靠的空间关节关联。
    2.  **与Transformer相比**: 虽然两者都有全局感受野，但作者认为FCN更适合此问题，因为姿态平滑更关注运动连续性而非点间语义关联，且FCN更易训练 (p.6)。
    3.  **与低通滤波器相比**: 是数据驱动的方法，能够学习运动分布，自适应地进行平滑，而不是使用固定的滤波核。
## 实验

- **数据集**: Human3.6M, 3DPW, MPI-INF-3DHP, AIST++, MuPoTS-3D (p.9)。
- **对比方法**: 包括三类：1) 滤波器：One-Euro滤波器、Savitzky-Golay滤波器、高斯滤波器；2) 其他时空精炼模型；3) 十一种骨干网络（如Hourglass, CPN, HRNet, RLE, FCN, VIBE等）的原始输出 (p.9)。
- **评价指标**: 用于衡量平滑性的**平均关节加速度误差 (Accel)**，单位为mm/frame²或pixel/frame²；用于衡量单帧精度的**平均关节位置误差 (MPJPE)** 和经过普氏分析校正后的**PA-MPJPE** (p.9)。
- **主实验结果**: 在AIST++数据集上，以VIBE为骨干，SmoothNet将**Accel从31.64降至4.15**（降低约86.88%），同时**MPJPE从106.90降至97.47**（降低约8.82%），显著优于所有滤波器方法 (p.9, Table 1)。在Human3.6M上，对多种2D/3D估计器应用SmoothNet后，**Accel普遍降低超过88%**，同时MPJPE仅有轻微下降甚至提升 (p.11, Table 2)。
- **消融实验**: PDF文本中未展示详细的消融实验表格，但文中指出Basic SmoothNet与Motion-aware SmoothNet是两种变体设计，并通过不同骨干网络和任务验证了架构的有效性。
- **泛化实验**: SmoothNet在训练时仅使用FCN (H3.6M), SPIN (3DPW), VIBE (AIST++)的输出，但在测试时泛化到未见过的骨干网络（如HRNet, RLE）和数据集（如MuPoTS-3D），表现出强大的可迁移性 (p.9)。
- **效率信息**: SmoothNet参数量为**0.33M**，在CPU上的平均推理速度**低于1.3k FPS**，在A100 GPU上可达**46.8k FPS**，远快于多数滤波器（p.9）。
## 局限

- **依赖前端估计器**: SmoothNet的效果受限于前端姿态估计器的质量。如果原始估计在挑战帧上产生极大的位置错误（而不仅仅是抖动），SmoothNet可能无法有效校正，甚至可能被误导。
- **极端错误场景**: 论文主要关注“连续帧”上的抖动。对于完全丢失或估计完全错误的单帧或极短序列，其基于时间平滑假设的方法可能失效。
- **超参数选择**: 滑动窗口大小 `T` 和步长 `s` 是关键超参数。虽然论文给出了设置（T=32, s=1），但未深入探讨其敏感性以及对不同运动速度场景的适应性。
- **计算开销**: 虽然推理速度快，但作为后处理步骤，它为整个处理流程增加了额外的计算阶段。在实时性要求极高的应用中，仍需权衡。
- **假设依赖**: 其核心假设是“人体运动在时间上是连续平滑的”。这一假设在大多数情况下成立，但在发生快速、不连续的突变动作时，平滑处理可能会带来负面效果。
## 个人评论

这篇论文最值得学习的核心价值在于它对问题本质的深刻洞察和解决方案的简洁性。
1.  **问题洞察**: 它没有盲目地增加模型复杂度，而是首先深入分析了抖动问题的“不平衡性”本质，即严重问题只出现在特定连续帧上。这启发我们在研究中要先做细致的错误分析。
2.  **模块化思想**: 它将“精度优化”和“平滑优化”解耦，通过一个独立的、即插即用的模块专门解决平滑问题。这种模块化设计易于集成、评估和迭代，比设计一个端到端解决所有问题的庞大系统更灵活、更有效。
3.  **简约设计**: 在发现单关节时间序列建模是关键后，没有追逐最复杂的时序模型（如Transformer），而是选择了简单有效的全连接网络，并通过长感受野和残差连接实现强大性能。这证明了“简单方法 + 深刻理解”往往能带来惊喜。
4.  **跨领域泛化启发**: 其纯时间处理的设计使其天然具备跨不同数据集、不同估计器和不同任务模态的泛化能力，为设计具有强泛化性的预处理/后处理模块提供了范例。

### 使用建议

- **如果快速了解**: 阅读 **Abstract**, **Introduction** (特别是Fig.1, Fig.2和贡献列表), 以及 **Experiments** 中的 **5.2 Comparison with Existing Solutions** 和 **Table 1, Table 2** 的关键数字。这些部分足以掌握论文的核心思想、动机和主要成果。
- **如果复现**: 重点精读 **4. Method** 部分，特别是 **4.1 Basic SmoothNet**, **4.2 Motion-aware SmoothNet** 的结构图（Fig.5, Fig.6）和公式。结合 **5.1 Experimental Settings** 中的实现细节（网络层数、窗口大小、训练数据准备方式）以及提供的代码链接进行复现。
- **如果借鉴创新点**: 应学习其 **问题定义方式**（将误差分解为J和S）、**模块化设计哲学**（即插即用的时间精炼器）、以及 **如何利用物理先验（运动方程）来指导网络设计**（Motion-aware分支）。这些思想可以迁移到其他时间序列平滑任务中。
- **如果写 related work**: 可将SmoothNet放在 **人体姿态估计的时间序列精炼** 或 **视频理解中的时序建模** 相关工作中。它代表了一种不同于时空融合模型和传统滤波器的“纯数据驱动时序精炼”流派。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R2_控制_生物启发_其他跨学科]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉与人体运动分析的交叉领域，具体方向是视频中的人体姿态估计与时间序列优化。它解决的核心问题是现有姿态估计器在视频分析中输出的轨迹存在严重抖动（Jitter），特别是对于罕见或被遮挡的姿态。该论文通过设计一个即插即用的、仅依赖时间信息的精炼网络来平滑输出。它适合放在用户指定的 `R2_控制_生物启发_其他跨学科` 主题下，因为其研究动机（改善感知以支持下游控制/交互）和其借鉴人体运动自然平滑特性的方法论，具有生物启发和跨学科特性。

## 2. 一句话总结
论文提出了一个名为SmoothNet的即插即用、仅使用时间信息的全连接网络，通过学习人体运动的长期时间关系来显著平滑视频中的人体姿态估计，并意外地提升了困难帧的精度。

## 3. 背景与问题
- **为什么要做**: 人体姿态估计在动作分析、人机交互等领域有广泛应用。然而，将基于图像的姿态估计器直接应用于视频时，输出的关节轨迹会产生严重抖动，尤其是在包含罕见动作或遮挡的连续帧上，导致感知不可靠 (p.1)。
- **之前方法的问题**: 现有的学习方法（端到端网络或精炼网络）通常采用时空模型联合优化单帧精度和所有关节的时间平滑性。这是一个高难度任务，因为在抖动帧中提取的时空特征本身不可靠，且同时优化抖动误差(J)和偏差误差(S)存在“时空优化瓶颈”(p.5)。而传统的低通滤波器（如移动平均、高斯滤波）虽然简单，但会在平滑性和滞后性之间权衡，导致长时抖动场景下精度损失严重 (p.5)。
- **核心矛盾**: 优化单帧位置精度（MPJPE）与优化序列平滑性（Accel）之间的内在矛盾。时空模型试图同时优化两者，但常常顾此失彼；固定滤波器无法根据数据动态调整，导致过度平滑或滞后。

## 4. 核心贡献
1.  **发现抖动的不平衡性**: 系统性地分析了抖动问题，指出严重抖动通常只出现在连续的、由图像质量差、遮挡或罕见姿态构成的“挑战帧”上 (p.2)。
2.  **提出首个数据驱动的纯时间精炼方案**: 据作者所知，这是第一个用于缓解人体运动抖动的、数据驱动的、仅依赖时间信息的精炼解决方案 (p.2)。
3.  **设计简单有效的FCN网络架构**: 设计了基于具有长感受野的残差全连接网络（FCN）的SmoothNet，学习每个关节的时间关系进行平滑，实验证明其优于TCN和Transformer (p.2, p.6)。
4.  **提出运动感知（Motion-aware）变体**: 显式地将速度（一阶运动信息）和加速度（二阶运动信息）注入网络，利用物理先验加速学习收敛并获得更好效果 (p.7)。
5.  **验证了强大的即插即用与跨域泛化能力**: 作为纯时间模型，SmoothNet在11种不同骨干网络、3种任务模态（2D/3D位姿、SMPL参数）和5个数据集上验证了其有效性和可迁移性 (p.2, p.8)。

## 5. 方法详解
- **整体框架**: SmoothNet是一个插件式（Plug-and-Play）模块，附加在任何现有的2D/3D人体姿态估计器之后。其输入是原始估计器输出的带有抖动的关节坐标序列 `Ŷ ∈ R^{L×C}`，输出是平滑和精炼后的关节坐标序列 `Ĝ ∈ R^{L×C}` (p.3, p.6)。
- **关键模块 (Basic SmoothNet)**: 核心是多个残差连接的全连接（FC）层块，沿时间轴处理输入。每一层的计算如公式(1)所示：`Ŷ_{i,t}^{l+1} = σ(Σ_t w_t^l * Ŷ_{i,t}^l + b^l)`，其中权重 `w_t` 和偏置 `b` 在不同的关节轴 `i` 间共享，激活函数σ默认使用LeakyReLU。这种FCN结构在每个层都具有全局感受野，能更好地容忍长时抖动 (p.6)。
- **运动感知版本 (Motion-aware SmoothNet)**: 在Basic SmoothNet的基础上，增加了对速度和加速度的显式建模。给定输入序列 `Ŷ`，首先计算一阶速度 `V` 和二阶加速度 `A`（如公式2）。网络包含三个并行的FCN分支，分别处理位置、速度和加速度序列。最后，将三个分支顶部的特征拼接，通过一个线性融合层得到最终平滑结果 `Ĝ` (p.7)。
- **输入输出与滑动窗口**: 采用类似滤波器的滑动窗口方案处理长序列。从输入序列中提取一个长度为 `T` 的窗口（论文中T=32），进行精炼，然后以步长 `s`（s≤T，论文中s=1）滑动到下一个窗口，防止丢失末尾帧 (p.7)。
- **训练方式**: 训练损失是位置损失 `L_pose` 和加速度损失 `L_acc` 的简单相加。`L_pose` 衡量预测位姿与真值间的L1误差，`L_acc` 衡量预测加速度（由预测位姿计算）与真值加速度间的L1误差 (p.8)。
- **推理流程**: 训练好的SmoothNet模型接收前端估计器的输出序列，通过滑动窗口方式进行推理，并额外使用滑动窗口平均算法基于精炼结果来避免帧丢失和减少尖峰 (p.9)。
- **与已有方法的差异**:
    1.  **与时空模型相比**: 完全摒弃空间信息，只处理单个关节的时间序列，避免了在抖动帧中引入不可靠的空间关节关联。
    2.  **与Transformer相比**: 虽然两者都有全局感受野，但作者认为FCN更适合此问题，因为姿态平滑更关注运动连续性而非点间语义关联，且FCN更易训练 (p.6)。
    3.  **与低通滤波器相比**: 是数据驱动的方法，能够学习运动分布，自适应地进行平滑，而不是使用固定的滤波核。

## 6. 实验与结果
- **数据集**: Human3.6M, 3DPW, MPI-INF-3DHP, AIST++, MuPoTS-3D (p.9)。
- **对比方法**: 包括三类：1) 滤波器：One-Euro滤波器、Savitzky-Golay滤波器、高斯滤波器；2) 其他时空精炼模型；3) 十一种骨干网络（如Hourglass, CPN, HRNet, RLE, FCN, VIBE等）的原始输出 (p.9)。
- **评价指标**: 用于衡量平滑性的**平均关节加速度误差 (Accel)**，单位为mm/frame²或pixel/frame²；用于衡量单帧精度的**平均关节位置误差 (MPJPE)** 和经过普氏分析校正后的**PA-MPJPE** (p.9)。
- **主实验结果**: 在AIST++数据集上，以VIBE为骨干，SmoothNet将**Accel从31.64降至4.15**（降低约86.88%），同时**MPJPE从106.90降至97.47**（降低约8.82%），显著优于所有滤波器方法 (p.9, Table 1)。在Human3.6M上，对多种2D/3D估计器应用SmoothNet后，**Accel普遍降低超过88%**，同时MPJPE仅有轻微下降甚至提升 (p.11, Table 2)。
- **消融实验**: PDF文本中未展示详细的消融实验表格，但文中指出Basic SmoothNet与Motion-aware SmoothNet是两种变体设计，并通过不同骨干网络和任务验证了架构的有效性。
- **泛化实验**: SmoothNet在训练时仅使用FCN (H3.6M), SPIN (3DPW), VIBE (AIST++)的输出，但在测试时泛化到未见过的骨干网络（如HRNet, RLE）和数据集（如MuPoTS-3D），表现出强大的可迁移性 (p.9)。
- **效率信息**: SmoothNet参数量为**0.33M**，在CPU上的平均推理速度**低于1.3k FPS**，在A100 GPU上可达**46.8k FPS**，远快于多数滤波器（p.9）。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的核心价值在于它对问题本质的深刻洞察和解决方案的简洁性。
1.  **问题洞察**: 它没有盲目地增加模型复杂度，而是首先深入分析了抖动问题的“不平衡性”本质，即严重问题只出现在特定连续帧上。这启发我们在研究中要先做细致的错误分析。
2.  **模块化思想**: 它将“精度优化”和“平滑优化”解耦，通过一个独立的、即插即用的模块专门解决平滑问题。这种模块化设计易于集成、评估和迭代，比设计一个端到端解决所有问题的庞大系统更灵活、更有效。
3.  **简约设计**: 在发现单关节时间序列建模是关键后，没有追逐最复杂的时序模型（如Transformer），而是选择了简单有效的全连接网络，并通过长感受野和残差连接实现强大性能。这证明了“简单方法 + 深刻理解”往往能带来惊喜。
4.  **跨领域泛化启发**: 其纯时间处理的设计使其天然具备跨不同数据集、不同估计器和不同任务模态的泛化能力，为设计具有强泛化性的预处理/后处理模块提供了范例。

## 8. 局限与问题
- **依赖前端估计器**: SmoothNet的效果受限于前端姿态估计器的质量。如果原始估计在挑战帧上产生极大的位置错误（而不仅仅是抖动），SmoothNet可能无法有效校正，甚至可能被误导。
- **极端错误场景**: 论文主要关注“连续帧”上的抖动。对于完全丢失或估计完全错误的单帧或极短序列，其基于时间平滑假设的方法可能失效。
- **超参数选择**: 滑动窗口大小 `T` 和步长 `s` 是关键超参数。虽然论文给出了设置（T=32, s=1），但未深入探讨其敏感性以及对不同运动速度场景的适应性。
- **计算开销**: 虽然推理速度快，但作为后处理步骤，它为整个处理流程增加了额外的计算阶段。在实时性要求极高的应用中，仍需权衡。
- **假设依赖**: 其核心假设是“人体运动在时间上是连续平滑的”。这一假设在大多数情况下成立，但在发生快速、不连续的突变动作时，平滑处理可能会带来负面效果。

## 9. 我该怎么使用这篇论文
- **如果快速了解**: 阅读 **Abstract**, **Introduction** (特别是Fig.1, Fig.2和贡献列表), 以及 **Experiments** 中的 **5.2 Comparison with Existing Solutions** 和 **Table 1, Table 2** 的关键数字。这些部分足以掌握论文的核心思想、动机和主要成果。
- **如果复现**: 重点精读 **4. Method** 部分，特别是 **4.1 Basic SmoothNet**, **4.2 Motion-aware SmoothNet** 的结构图（Fig.5, Fig.6）和公式。结合 **5.1 Experimental Settings** 中的实现细节（网络层数、窗口大小、训练数据准备方式）以及提供的代码链接进行复现。
- **如果借鉴创新点**: 应学习其 **问题定义方式**（将误差分解为J和S）、**模块化设计哲学**（即插即用的时间精炼器）、以及 **如何利用物理先验（运动方程）来指导网络设计**（Motion-aware分支）。这些思想可以迁移到其他时间序列平滑任务中。
- **如果写 related work**: 可将SmoothNet放在 **人体姿态估计的时间序列精炼** 或 **视频理解中的时序建模** 相关工作中。它代表了一种不同于时空融合模型和传统滤波器的“纯数据驱动时序精炼”流派。

## 10. 和其他论文的关系
根据论文主题和内容，可能相关的论文包括：
- 它直接改进的前端估计器: `[[VIBE]]`, `[[RLE]]`, `[[HRNet]]`, `[[SPIN]]` 等，这些论文构成了其应用基础和对比基线。
- 它探讨和对比的时序模型: `[[TCN (Temporal Convolutional Network)]]`, `[[Transformer]]`，作为其架构设计的对比参照。
- 同属姿态估计精炼或时序优化范畴: 可能相关一些基于图卷积或注意力机制的时空姿态估计模型，但SmoothNet强调与它们的差异（纯时间，无空间）。

## 11. 关键词
人体姿态估计, 抖动缓解, 时间序列模型, 即插即用网络, 全连接网络, 运动平滑, 加速度误差, 人体运动分析, 计算机视觉, 后处理精炼

## 12. 可信度说明
本篇精读笔记主要基于提供的PDF文本的前12页生成，涵盖了论文的摘要、引言、方法、实验设置和部分实验结果。提取质量良好，文本连贯。笔记中引用的所有具体概念、数字（如Accel降低86.88%， 参数量0.33M）、公式和图表说明均严格来自提供的文本。由于提供的文本仅包含前12页（论文共34页），后续更详细的消融实验、可视化分析、在更多数据集上的结果等可能未被涵盖，因此笔记中“消融实验”部分指出信息不完整。总体而言，基于已提供内容，本笔记准确、客观地反映了论文的核心思想和主要成果。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/SmoothNet.txt` (34/34 页; 原 AI 主体 12/34 + 全文补读 13-34); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-34; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-34。
- **提取情况**: 缺失页 22 页, 其中 22 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: SmoothNet 13
- p.13: Method Gaussian1d TCN(27) TCN(81) TCN(81) ×TCN(243) Trans. ×Ours⋆Ours×
- p.13: Epoch50100150MPJPE
- p.13: Basic-Train
- p.13: Ours-Train
- p.13: Basic-Test
- p.13: Ours-Test
- p.13: Results are shown in Table 4, which indicates (i). the performance of TCN
- p.14: MPJPE initially decrease, then begin to increase slightly, indicating that when
- p.14: W VIBE 2 8 16 32 64 128 256
- p.14: 6 Conclusion
- p.14: BroaderImpact: SmoothNet isatemporal-onlymodeltargetingatremoving

### 缺失页关键摘录

- p.13: Table 4:Comparison results with diﬀerent temporal models on VIBE-
- p.13: Fig.8: Impact of model designs from the training and testing precision curves.
- p.13: Results are shown in Table 4, which indicates (i). the performance of TCN
- p.13: aware temporal network as the SmoothNet in Sec. 4.2. Figure 8 illustrates the
- p.14: eﬀects on diﬀerent window sizes from 2to256frames in Table 5. As the window
- p.14: Table 5:Impact of window size Won VIBE-AIST++ [25].
- p.15: New benchmark and state of the art analysis. In: Proceedings of the IEEE Con-
- p.15: 2. Bai, S., Kolter, J.Z., Koltun, V.: An empirical evaluation of generic convolutional
- p.19: about dataset descriptions, implementation details in Sec. 1. In Sec. 2, we show
- p.19: conduct more ablation studies on the eﬀect of the loss function, motion modali-
- p.19: space limitation. Lastly, in Sec. 3, we visualize qualitative results to verify the
- p.19: –3DPW [28] an in-the-wild dataset consisting of more than 51 ,000 frames’
<!-- AI_READING_NOTE_END -->
