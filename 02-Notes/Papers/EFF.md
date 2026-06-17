---
title: "SUnet: A multi-organ segmentation network based on multiple attention"
authors:
  - "Xiaosen Li"
  - "Xiao Qin"
  - "Chengliang Huang"
  - "Yuer Lu"
  - "Jinyan Cheng"
  - "Liansheng Wang"
  - "Ou Liu"
  - "Jianwei Shuai"
  - "Chang-an Yuan"
year: 2023
venue: Computers in Biology and Medicine
doi: 10.1016/j.compbiomed.2023.107596
pdf: [[EFF.pdf]]
primary_topic: A1_医学图像_分割
topics:
  - "A1_医学图像_分割"
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/EFF.txt
---

# SUnet: A multi-organ segmentation network based on multiple attention

## 基本信息
- **PDF**: [[EFF.pdf]]
- **primary_topic**: `A1_医学图像_分割`
- **topics**: `A1_医学图像_分割`, `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SUnet: A multi-organ segmentation network based on multiple attention |
| **作者** | Xiaosen Li; Xiao Qin; Chengliang Huang; Yuer Lu; Jinyan Cheng; Liansheng Wang; Ou Liu; Jianwei Shuai; Chang-an Yuan |
| **发表时间** | 2023 (收稿 2023-07-20, 录用 2023-10-17, 在线 2023-10-18) |
| **刊物/会议** | Computers in Biology and Medicine, vol. 167, art. 107596 |
| **DOI** | 10.1016/j.compbiomed.2023.107596 |

## 摘要

**英文原文（据 PDF 提取文本整理，已修复空格与连字符断裂）**：

> Organ segmentation in abdominal or thoracic computed tomography (CT) images plays a crucial role in medical diagnosis as it enables doctors to locate and evaluate organ abnormalities quickly, thereby guiding surgical planning, and aiding treatment decision-making. This paper proposes a novel and efficient medical image segmentation method called SUnet for multi-organ segmentation in the abdomen and thorax. SUnet is a fully attention-based neural network. Firstly, an efficient spatial reduction attention (ESRA) module is introduced not only to extract image features better, but also to reduce overall model parameters, and to alleviate overfitting. Secondly, SUnet's multiple attention-based feature fusion module enables effective cross-scale feature integration. Additionally, an enhanced attention gate (EAG) module is considered by using grouped convolution and residual connections, providing richer semantic features. We evaluate the performance of the proposed model on synapse multiple organ segmentation dataset and automated cardiac diagnostic challenge dataset. SUnet achieves an average Dice of 84.29% and 92.25% on these two datasets, respectively, outperforming other models of similar complexity and size, and achieving state-of-the-art results.

**中文翻译**：

> 腹部或胸部 CT 图像中的器官分割在医学诊断中至关重要，它使医生能够快速定位并评估器官异常，从而指导手术规划、辅助治疗决策。本文提出一种新颖且高效的医学图像分割方法 SUnet，用于腹部与胸部的多器官分割。SUnet 是一个完全基于注意力的神经网络。首先，引入高效空间压缩注意力（ESRA）模块，不仅能更好地提取图像特征，还能降低整体模型参数量并缓解过拟合。其次，SUnet 的多注意力特征融合模块实现了有效的跨尺度特征整合。此外，本文还设计了一个增强型注意力门控（EAG）模块，利用分组卷积与残差连接提供更丰富的语义特征。我们在 Synapse 多器官分割数据集与自动心脏诊断挑战（ACDC）数据集上评估所提模型，SUnet 在这两个数据集上分别取得 84.29% 和 92.25% 的平均 Dice，在相近复杂度与体量的模型中表现最佳，达到 state-of-the-art 水平。

> 来源: 据 PDF 提取文本整理。
## 研究背景与动机

- **为什么要做**：腹部和胸部集中了人体大部分器官，也易发各类疾病；从 CT 扫描中分割器官对诊断与治疗至关重要，但人工分割耗时且易出错（论文引言原话 "laborious and error-prone"）。临床上迫切需要自动分割方法。分割困难来自周围组织干扰、器官形变/位移、以及图像对比度低导致的边界模糊。
- **之前方法的问题**：
    1. **基于 CNN 的方法**（Unet 及其变体 Unet++/Unet3+/ResUnet 等）：受卷积操作固有约束，难以有效建立长距离依赖，限制了性能上限。
    2. **基于 Transformer 的方法**（ViT → TransUnet（CNN-Transformer 混合编码器）→ Swin-Unet（纯 Transformer 编解码））：能有效捕捉长距离依赖，但参数量与计算需求显著高于 CNN 方案，对计算资源有限的从业者构成挑战；且在有限数据下易过拟合。
- **核心矛盾**：如何在保留 Transformer 全局建模能力的同时，降低其参数量与计算开销，并缓解小数据下的过拟合。论文的解法受**金字塔视觉 Transformer（PVT）**启发——PVT 通过卷积压缩 MHSA 的 Key/Value 来削减参数与计算量。
## 关键贡献

论文引言明确列出 4 条贡献：

1. **提出 SUnet**：一个纯 Transformer 的 U 型医学图像分割网络，整合了高效空间压缩注意力与多注意力特征融合。
2. **高效空间压缩注意力（ESRA）**：在保持较少参数的同时让模型表现更好，并缓解 Transformer 模型常见的过拟合。
3. **增强型注意力门控（EAG）**：基于分组卷积与残差连接，降低计算复杂度与数据依赖性，提取更多任务相关特征。
4. **基于多注意力的高效特征融合（EFF）模块**：在 U 型网络中实现跳跃连接特征与解码器特征更好的融合。
## 方法

**整体框架（图 1a）**：SUnet 沿用 Unet 的编码器-解码器结构与跳跃连接。四个阶段的通道数定义为 C1=64、C2=128、C3=320、C4=512。每个阶段堆叠两个 ESRA Transformer 块作为特征提取模块。**重叠 patch 嵌入**用 7×7 卷积、步长 3；**重叠 patch 合并**用 3×3 卷积。重叠特性有助于缓解传统 patch 嵌入造成的信息损失。

**关键模块**：

1. **ESRA Transformer 块（图 1b，对比图 2）**：
    - **作用**：主干特征提取器，替代标准卷积/标准 Transformer 块。
    - **空间压缩（SR）**：用卷积核与步长均为 R_i 的 2D 卷积压缩 MHSA 的 Key 与 Value（公式 4 `SR(x)=Norm(Conv2d_Ri(x))`），由此降低参数。论文给出原始 MHSA 与 ESRA 的参数量表达式（公式 1、2），并指出当 R_i ≥ 2 时 MHSA 参数量大于 ESRA。R_i 是第 i 阶段的压缩比，决定卷积核大小与步长。
    - **DropKey 正则化（公式 5）**：为缓解 Transformer 过拟合，在注意力上施加 DropKey——以 Bernoulli 分布对注意力权重做隐式自适应掩码，惩罚过高注意力值，促使注意力更平滑、关注更多任务相关区域，捕获更鲁棒的全局特征。ESRA 整体表达见公式 3（在 `Softmax[DropKey(Q·SR(K)^T)/√dim_head] · SR(V)` 形式上）。
    - **前馈网络 Mix-FFN（图 1c）**：在两个线性层之间插入深度可分离卷积，引入局部上下文。
    - **与 PVT 差异**：思路源自 PVT 的 K/V 压缩，但本文面向分割任务，并额外整合 DropKey 等正则化。

2. **高效特征融合模块（EFF，图 1d）**：由三个子模块构成——EAG、ECA、SA。
    - **EAG（图 1e，公式 6–8）**：改进自 Attention Unet 的 AG 模块。原 AG 计算复杂度高且对两路输入相关性依赖强，当相关性弱时无法捕获关键特征。EAG 的改进：① 用**分组卷积（32 组）**替代常规卷积做组内特征融合，降低计算量（公式 7、8：`Wg=ReLU(BN(GroupConv32(g)))`、`Wx=ReLU(BN(GroupConv32(x)))`，其中 g 为上采样得到的高级语义特征、x 为跳跃连接传来的低级语义特征）；② 卷积后加 ReLU；③ 对低级特征 x 做**残差连接**——当两路相关性弱时减弱高级特征对低级特征的干扰，避免性能退化。输出 `EAG = x × Sigmoid(Conv1×1(ReLU(Wg+Wx)))`（公式 6）。
    - **拼接 + 多注意力串联**：两路经 EAG 增强的特征在通道维拼接（通道数翻倍）；为避免直接操作丢失信息，再依次经 **ECA（高效通道注意力）与 SA（空间注意力）串联**（图 3，用 GAP 全局平均池化、GMP 全局最大池化），从通道与空间两维度强调任务相关特征，实现多注意力融合。
    - **特例**：最底层的 ECA&SA 模块只有单路输入，故仅用 ECA 与 SA 做特征强调，不经 EAG。

**训练方式（4.2）**：PyTorch 1.8.0；AdamW 优化器，学习率与权重衰减均为 1e-4。损失为 Dice 损失与交叉熵损失的加权和（公式 9：`LOSS = λ1·DICE + λ2·CE`，λ1=0.6、λ2=0.4）。数据增强为随机翻转与旋转。
- Synapse：18 例训练 / 12 例测试，batch=24，最多 150 epoch，输入 224×224、patch 16。
- ACDC：70 例训练 / 10 例验证 / 20 例测试，batch=12，150 epoch，patch 16。

**医学任务特化**：
- **任务类型**：多器官语义分割。
- **图像模态**：CT（Synapse 腹部）与 MRI（ACDC 心脏）。
- **临床意义**：辅助医生快速定位、评估器官异常，指导手术规划与治疗决策。
## 实验

- **数据集**：
    1. **Synapse 多器官分割数据集**：来自 MICCAI 2015 Multi-Atlas Abdominal Labeling Challenge，30 例标注腹部 CT 扫描、3779 张增强腹部图像；每例含 85–198 张切片、分辨率 512×512。分割 8 个器官（论文列举为 aorta、gallbladder、spleen、left kidney、right kidney、liver、pancreas、spleen、stomach——原文 spleen 重复列出，按"8 个器官"口径应为 spleen 计一次、外加 stomach）。
    2. **ACDC（自动心脏诊断挑战）数据集**：100 名患者的心脏 MRI，每例含 3 个标签——左心室（LV）、右心室（RV）、心肌（Myo）。
- **对比方法**：选取 10 个有代表性、性能良好的 2D 医学图像分割模型在 Synapse 上做对比，含 Unet（U 型奠基者）、TransUnet（首个 Transformer+Unet 结合）、Swin-Unet（首个纯 Transformer U 型网络）等。
- **评价指标**：Dice 相似系数（DSC，越高越好）、Hausdorff 距离（HD，越低越好）。
- **主实验结果（来自摘要）**：Synapse 平均 Dice **84.29%**，ACDC 平均 Dice **92.25%**；论文声称在相近复杂度与体量的模型中达到 state-of-the-art。
- **消融实验**：论文 4 节明确做了"structure ablation experiments"分析架构，但**提取缓存只覆盖到第 5 页 Table 1 表头即截断**，消融的具体数值未在缓存中出现。
- **效率信息**：模型参数量 **28.27 M**、计算量 **11.89 G FLOPs**（据原文后续页 Table 1，提取缓存未覆盖，待核）。实验环境：Ubuntu 18.04、CPU i7-12700K、NVIDIA RTX 3090、1 TB SSD，PyTorch 1.8.0。
## 局限

1. **2D 处理的局限**：SUnet 是 2D 模型，对 3D 的 CT/MRI 体数据逐切片处理，可能丢失切片间上下文，影响连续结构的分割一致性。
2. **对正则化/数据的依赖**：需借助 DropKey、残差连接等手段抑制过拟合，间接说明小数据下模型易过拟合；实验数据集规模偏小（Synapse 30 例、ACDC 100 例），在大规模、多样性临床数据上的泛化能力有待验证。
3. **实验完整性（受缓存限制的判断）**：提取缓存截断于 Table 1 表头，逐器官 DSC、完整对比表、消融具体数值与定性可视化结果均未在缓存中呈现，难据缓存独立核验每个模块（ESRA/EAG/EFF）的贡献，需回原文后续页核对。
4. **推理速度未见于缓存**：参数/FLOPs 之外的实测推理速度（FPS、latency）在已覆盖文本中未提及，对实时临床场景而言是缺口（待核原文）。
## 个人评论

1. **"压缩 + 正则化"的瘦身范式**：ESRA 把 PVT 的 K/V 卷积压缩与 DropKey 隐式正则化组合在一起，是一个把视觉 Transformer 系统性"瘦身"的清晰范例——压缩降参、DropKey 稳训练。该思路可迁移到其他 ViT/混合网络。
2. **务实的分层融合**：EFF 不用复杂交叉注意力，而是"先用改进的 AG（EAG）做对齐增强、再用经典 ECA/SA 串联做通道-空间强调"。这种模块化、可插拔的融合范式实现门槛低、易调试，值得借鉴到跳跃连接特征融合场景。
3. **针对真实痛点**：所有创新都围绕"Transformer 性能好但参数大、易过拟合"展开，对计算资源有限却追求高性能的研究者有参考价值。
4. **一处需谨慎之处**：论文器官列表把 spleen 写了两次，与"8 个器官"口径不符，复现时应以官方 Synapse 标签为准；本笔记的部分数字（28.27M/11.89G、逐器官 DSC、消融）依赖原文后续页，提取缓存未覆盖，引用前建议回查原表。

### 使用建议

- **快速了解**：读摘要、引言（动机与 4 条贡献）、图 1（整体框架与各子模块）、第 4 节实验设置。
- **复现**：精读第 3 节方法，重点是 ESRA（公式 1–5）、EAG（公式 6–8）、损失（公式 9，λ1=0.6/λ2=0.4），以及 4.2 实现细节（AdamW、lr=wd=1e-4、Synapse batch24/ACDC batch12、150 epoch、输入 224×224）。
- **借鉴创新点**：① ESRA 的空间压缩 + DropKey；② EAG 的分组卷积 + 残差；③ EFF 的"EAG + ECA/SA 串联"融合范式。
- **写 Related Work**：可归入 1) 基于 Transformer 的医学图像分割；2) 高效视觉 Transformer 设计；3) U 型网络中的注意力机制。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A1_医学图像_分割]]
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
计算机视觉与医学图像分析的交叉工作，任务是腹部/胸部 CT 与心脏 MRI 的多器官语义分割。发表于医学工程期刊 Computers in Biology and Medicine（2023）。论文本质是一篇**高效 Transformer 医学图像分割**工作：以分割任务为目标、以注意力算子（ESRA、EAG、ECA/SA）的设计为手段。因此主题定为 `A1_医学图像_分割`，并保留 `B_注意力算子模块` 作为次主题（其核心贡献确为注意力模块创新）。

## 2. 一句话总结
SUnet 是一个纯注意力的 U 型医学分割网络：用 ESRA（卷积压缩 K/V + DropKey 正则）做高效全局特征提取，用 EFF（EAG + ECA/SA 串联）做跳跃连接与解码器特征的融合，在 Synapse/ACDC 上分别取得 84.29%/92.25% 平均 Dice，并以相近体量胜过同类模型。

## 3. 背景与问题
- CNN 类（Unet、Unet++、Unet3+、ResUnet…）受卷积约束，长距离依赖建模弱。
- Transformer 类（ViT→TransUnet→Swin-Unet）长依赖强，但参数/计算大、小数据易过拟合。
- 矛盾：在保留全局建模能力的同时降参降算、抑过拟合。解法受 PVT 的 K/V 卷积压缩启发。

## 4. 核心贡献
对应引言 4 条：① 纯 Transformer U 型网络 SUnet；② ESRA（少参数、缓解过拟合）；③ EAG（分组卷积 + 残差，降复杂度与数据依赖）；④ 多注意力 EFF 融合模块。

## 5. 方法详解
- **骨架**：Unet 编解码 + 跳跃连接；通道 C1–C4 = 64/128/320/512；每阶段 2 个 ESRA 块；重叠 patch 嵌入 7×7/步长3，重叠 patch 合并 3×3。
- **ESRA**：公式 4 用核=步长=R_i 的 2D 卷积压缩 K/V；公式 1、2 给出 MHSA 与 ESRA 参数量，R_i≥2 时 ESRA 更省参；公式 5 DropKey 以 Bernoulli 掩码隐式正则化注意力；公式 3 给出 ESRA 整体；Mix-FFN（图 1c）两线性层间插深度可分离卷积引入局部上下文。
- **EAG（公式 6–8）**：改进 Attention Unet 的 AG——分组卷积（32 组）替常规卷积、卷积后加 ReLU、对低级特征 x 加残差；`EAG = x × Sigmoid(Conv1×1(ReLU(Wg+Wx)))`，g 为上采样高级特征、x 为跳跃低级特征。残差在两路相关性弱时保护低级特征。
- **EFF（图 1d）**：两路经 EAG 增强后通道拼接（通道翻倍），再串联 ECA→SA（图 3，含 GAP/GMP）做通道与空间强调；最底层单输入分支只用 ECA/SA。
- **训练**：AdamW，lr=wd=1e-4；损失 = 0.6·Dice + 0.4·CE（公式 9）；随机翻转/旋转增强。Synapse：18/12 划分、batch24、150 epoch、输入 224×224、patch16；ACDC：70/10/20 划分、batch12、150 epoch。

## 6. 实验与结果
- **Synapse**：MICCAI 2015 多图谱腹部标注挑战，30 例 CT、3779 张增强图、每例 85–198 切片、512×512；8 器官（aorta/gallbladder/spleen/left kidney/right kidney/liver/pancreas/stomach；原文 spleen 误列两次）。
- **ACDC**：100 例心脏 MRI，标签 LV/RV/Myo。
- **对比**：10 个代表性 2D 分割模型（Unet、TransUnet、Swin-Unet 等）。指标 DSC↑、HD↓。
- **结果（据摘要）**：Synapse 84.29%、ACDC 92.25% 平均 Dice，声称同体量 SOTA。
- **效率**：参数 28.27 M、11.89 G FLOPs（据原文后续页 Table 1，提取缓存未覆盖，待核）；环境 Ubuntu18.04 + i7-12700K + RTX 3090 + PyTorch1.8.0。
- **消融**：论文称做了 structure ablation，但提取缓存截断于 Table 1 表头，具体数值未覆盖。

## 7. 这篇论文真正有价值的地方
1. ESRA 给出"卷积压缩 K/V + DropKey 正则"的可迁移瘦身范式。
2. EFF 用"EAG 对齐增强 + ECA/SA 串联强调"的分层、可插拔融合方案，实现简单。
3. 全篇围绕"Transformer 降参提效抗过拟合"这一真实痛点，对资源受限场景实用。

## 8. 局限与问题
1. 2D 逐切片，丢失 3D 切片间上下文。
2. 依赖 DropKey/残差抑过拟合，数据集偏小（30/100 例），泛化待验证。
3. 受提取缓存截断限制，逐器官 DSC、完整对比表、消融数值与可视化未能据缓存核验，需回原文后续页。
4. 推理速度（FPS/latency）在已覆盖文本中未提及。

## 9. 我该怎么使用这篇论文
- 快速了解：摘要 + 引言 + 图 1 + 第 4 节设置。
- 复现：第 3 节方法（公式 1–9）+ 4.2 超参（AdamW、lr=wd=1e-4、batch/epoch/输入尺寸）。
- 借鉴：ESRA 压缩+DropKey、EAG 分组卷积+残差、EFF 的 EAG+ECA/SA 串联融合。

## 10. 和其他论文的关系
SUnet 是对 Unet 的 Transformer 化与效率改造。提取文本明确引用的相关工作可锚定为：
- **改造对象**：`[[Unet]]`（Ronneberger 2015）、`[[Attention Unet]]`（Oktay 2018，AG 模块的来源）。
- **灵感来源**：`[[PVT (Pyramid Vision Transformer)]]`（K/V 卷积压缩思想）。
- **同类对比/前驱**：`[[TransUNet]]`（首个 Transformer+Unet）、`[[Swin-UNet]]`（首个纯 Transformer U 型网络）。
- **借用的注意力算子**：`[[ECA-Net]]`（Wang 等，高效通道注意力）、`[[SENet]]`、`[[CBAM]]`（多维注意力）。
（以上均为提取文本中明确点名的工作；笔记内 `[[]]` 链接是否已建对应笔记需另行核对。）

## 11. 关键词
医学图像分割、Transformer、注意力机制、网络架构、计算机断层扫描（CT）；本文新模块：ESRA（高效空间压缩注意力）、EAG（增强型注意力门控）、EFF（高效特征融合）。（前五项为论文 Keywords 原列。）

## 12. 可信度说明
本笔记基于 `.paper-cache/extracts/EFF.txt`。该缓存头标注 10/10 页，但实际文本受 25000 字符上限截断于**第 5 页 Table 1 表头**，覆盖了标题、摘要、引言、相关工作、完整方法（含全部公式 1–9）与实验设置（4.1 数据集、4.2 实现细节）。**结果部分的具体数值——逐器官 DSC、完整对比 Table 1、参数/FLOPs（28.27M/11.89G）、消融数据——未在缓存中出现**：平均 Dice 84.29%/92.25% 来自摘要可核；28.27M/11.89G 沿用原笔记、标注"据原文后续页待核"，未编造。原 frontmatter 标题为期刊页眉乱码（"ComputersinBiologyandMedicine167(2023)107596"），本次已据提取文本更正为真实论文标题。

---

> **可信度补充**: PDF 提取质量 = **medium**（缓存头标 10/10 页，但实际文本在 25000 字符处截断于 Table 1 表头，结果区数值未覆盖）; 来源缓存: `.paper-cache/extracts/EFF.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本次重读优化日期: 2026-06-18。
<!-- AI_READING_NOTE_END -->
