---
title: Three things everyone should know
authors:
  - "Hugo Touvron"
  - "Matthieu Cord"
  - "Alaaeldin El-Nouby"
  - "Jakob Verbeek"
  - "Hervé Jégou"
year: 2022
venue: "ECCV"
doi: 
pdf: [[Parallel ViT.pdf]]
primary_topic: B_注意力算子模块
topics:
  - "B_注意力算子模块"
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
extract_cache: .paper-cache/extracts/Parallel ViT.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/22 pages"
---
# Three things everyone should know

## 基本信息
- **PDF**: [[Parallel ViT.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Three things everyone should know |
| **作者** | Hugo Touvron; Matthieu Cord; Alaaeldin El-Nouby; Jakob Verbeek; Hervé Jégou |
| **发表时间** | 2022 |
| **刊物/会议** | ECCV |
| **DOI** | 未明确 |

## 摘要

> After their initial success in natural language processing, transformer ar- chitectures have rapidly gained traction in computer vision, providing state- of-the-art results for tasks such as image classification, detection, segmenta- tion, and video analysis. We offer three insights based on simple and easy to implement variants of vision transformers. (1) The residual layers of vi- sion transformers, which are usually processed sequentially, can to some ex- tentbeprocessedefficientlyinparallelwithoutnoticeablyaffectingtheaccu- racy. (2) Fine-tuning the weights of the attention layers is sufficient to adapt visiontransformerstoahigherresolutionandtootherclassificationtasks.This saves compute, reduces the peak memory consumption at fine-tuning time, andallowssharingthemajorityofweightsacrosstasks.(3)AddingMLP-based patchpre-processinglayersimprovesBert-likeself-supervisedtrainingbased on patchmasking. We evaluatethe impact of these designchoices usingthe ImageNet-1k dataset, and confirm

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：Vision Transformer (ViT) 在计算机视觉任务中取得了巨大成功，但其设计和训练程序的优化探索相对有限。作者认为存在一些简单但未被充分探索的改进方向。
- **之前方法的问题**：
  1.  标准ViT采用顺序层结构，在网络较深时可能面临优化困难。
  2.  在进行分辨率调整或下游任务微调时，通常需要对整个网络进行全参数微调，计算成本和内存峰值高，且不同任务无法共享大部分参数。
  3.  基于patch掩码的自监督学习（如BEiT）需要与patch预处理（如卷积主干）结合，但标准的卷积操作会在patch间传播信息，破坏自监督学习任务所需的独立性。
- **核心矛盾**：如何在**不显著损害模型性能**的前提下，**提升ViT的推理效率（如通过并行化）、降低微调和适配的成本（计算与内存）、并增强其与基于patch的自监督学习方法的兼容性**。
## 关键贡献

本文的核心贡献是提出了三个具体的、易于实现的见解：
1.  **并行Vision Transformer**：提出了一种简单的并行化ViT层结构的方法。将原本顺序执行的MHSA和FFN残差块进行配对并行处理，在保持相同参数量和计算量的同时，使网络变得更“浅”更“宽”，以降低延迟、简化优化。
2.  **微调注意力足矣**：发现在适应更高分辨率或迁移到其他分类任务时，**仅微调多头自注意力层（MHSA）的权重，同时冻结前馈网络层（FFN）** 的策略，其精度与全网络微调无显著差异。这能节省计算、降低峰值内存，并允许参数占主导的FFN层在不同任务间共享。
3.  **用于自监督学习的Patch预处理**：提出了一种分层MLP（hMLP）主干，用于在基于掩码的自监督学习（如BEiT）之前预处理图像块。该主干通过交替的MLP层和patch聚合操作实现，严格禁止patch间通信，从而与自监督训练兼容，并能在有监督设置下取得与最佳卷积主干相当的效果。
## 方法

### 整体框架
本文并未提出一个单一的全新网络框架，而是在标准的ViT架构基础上，提出了三种独立的、可组合的改进策略。核心是围绕ViT中的基本构建块——**多头自注意力层**和**前馈网络层**——进行重组和选择性训练。

### 关键模块与机制
#### 1. 并行ViT (Parallel ViT)
- **机制**：将原本顺序的两个Transformer块（`MHSA_l` -> `FFN_l` -> `MHSA_{l+1}` -> `FFN_{l+1}`）重组为并行结构。
- **输入输出**：输入 `x_l` 经过并行处理后得到输出 `x_{l+2}`。
- **数学公式与直观解释**：
  - 顺序处理：`x'_{l+1} = x_l + MHSA_l(x_l)`， `x_{l+1} = x'_{l+1} + FFN_l(x'_{l+1})`；`x'_{l+2} = x_{l+1} + MHSA_{l+1}(x_{l+1})`， `x_{l+2} = x'_{l+2} + FFN_{l+1}(x'_{l+2})`。
  - 并行处理：`x_{l+1} = x_l + MHSA_{l,1}(x_l) + MHSA_{l,2}(x_l)`；`x_{l+2} = x_{l+1} + FFN_{l,1}(x_{l+1}) + FFN_{l,2}(x_{l+1})`。
  - **直观解释**：随着网络变深，每个残差块对整体函数的贡献越来越小，因此可以用近似 `r'(x + r(x)) ≈ r'(x)` 来理解。这使得并行处理多个块成为可能，从而减少顺序计算步骤。
- **与已有方法的差异**：不同于直接增加工作维度（width）来增加模型容量（会导致参数和计算量二次增长），并行化在保持参数和FLOPs不变的情况下，增加了模型的宽度（并行处理能力）。

#### 2. 选择性微调策略
- **输入输出**：微调时，输入是预训练好的ViT模型和新的目标数据集；输出是适配后的模型。
- **关键机制**：仅更新MHSA层的权重，而FFN层的权重保持冻结（来自预训练模型）。
- **直观解释**：MHSA层负责捕捉数据间的依赖关系和全局上下文，这部分在分辨率改变或任务改变时需要调整。而FFN层可以视为对每个token进行独立的非线性变换，其功能在预训练后相对稳定，可以跨任务复用。

#### 3. hMLP Patch预处理主干
- **整体框架**：在将图像输入标准ViT之前，先通过一个分层的MLP主干进行处理。
- **模块与连接**：该主干由多个MLP层和patch聚合操作交替组成。聚合操作（如使用步长大于1的卷积或池化）减少序列长度（即降低分辨率），而MLP层对每个token进行独立变换。**关键设计**是禁止任何跨patch的通信，确保每个输出token只依赖于原始图像的一个局部区域，从而与基于patch掩码的自监督学习（掩码是在patch级别进行的）兼容。
- **训练方式**：在自监督学习（如BEiT）中，图像先通过hMLP stem得到patch序列，然后再对序列进行随机掩码，输入Transformer进行重建训练。
- **推理流程**：与标准ViT相同，图像经过hMLP stem处理后，序列输入Transformer进行分类或其他任务。
## 实验

### 数据集
- 主要数据集：**ImageNet-1k** (用于训练和验证)。
- 辅助测试集：**ImageNet-V2** (matched frequency) 提供独立测试视角。
- 迁移学习数据集：**六个较小的数据集**（文中未列出具体名称，但指出在这些数据集上测量了转移性能）。
- 自监督学习评估数据集：主要也在ImageNet-1k上进行。

### 对比方法
- **基线模型**：标准的顺序ViT（ViT-Ti, ViT-S, ViT-B, ViT-L）以及它们的变种（不同深度、是否使用LayerScale）。
- **对比架构**：与**增加工作维度**（更宽）的ViT模型进行参数和FLOPs近似的公平对比。
- **自监督学习对比**：与使用卷积主干（Conv-Stem）的BEiT方法进行对比。

### 评价指标
- **分类精度**：ImageNet-1k验证集和ImageNet-V2测试集的Top-1准确率。
- **效率指标**：模型参数量（params）、计算量（FLOPs）、推理速度（images/s）、峰值内存（MB）。

### 主实验结果
- **并行ViT效果**：在具有足够深度的模型上（如36或60个块），**并行两个分支的模型（如ViT-B18×2）性能与顺序模型相当甚至更优**。例如，ViT-B36顺序模型在400 epochs+LS下为84.1%，而并行版本ViT-B18×2在相同训练设置下达到84.1%（表2）。对于较浅的小模型（如ViT-Ti, ViT-S 24层），顺序版本通常更好（图2）。
- **选择性微调结果**：将预训练于224×224的ViT模型微调至384×384分辨率时，**仅微调MHSA层**的精度与全参数微调的精度差异在标准差（±0.1）之内（表5）。例如，ViT-S仅微调MHSA层在ImageNet-val上达到84.4%，与全微调的84.3%相当。
- **hMLP stem效果**：在BEiT自监督预训练框架下，提出的hMLP stem效果优于传统的卷积主干（Conv-Stem）。在有监督设置下，其精度与对比中最佳的卷积主干持平。
- **效率信息**：
  - **并行化**：主要优势在小批量（batch size）推理时，可获得显著速度提升（表4）。例如，ViT-B18×2在batch size=1时，并行实现比顺序实现快45%。
  - **选择性微调**：仅微调MHSA层，FFN参数量（约占模型主体参数2/3）被冻结，大幅减少可训练参数、计算量和训练内存峰值。
  - **参数/计算对比**：并行化模型与同等深度的顺序模型具有完全相同的参数量和FLOPs（表3）。与增加宽度的模型相比，在参数和FLOPs近似时，并行/顺序模型通常精度更高（表3）。

### 消融与泛化实验
- **消融**：研究了并行分支数量（1,2,3,4）对精度的影响，发现两个并行分支是最优平衡点（图1）。
- **泛化**：将仅微调MHSA层的策略应用于六个较小数据集的迁移学习任务，发现对于大模型（ViT-L），精度损失有限。
## 局限

1.  **方法适用场景**：并行ViT的优势主要在**深层、高容量模型**上显现。对于中小模型，标准顺序结构可能更优且易于优化。
2.  **实验局限性**：
    - 迁移学习仅测试了**分类任务**，未涉及检测、分割等更复杂的下游任务。
    - 自监督学习实验主要围绕**BEiT**，未验证与MAE等其他主流方法的兼容性。
    - 速度提升依赖于**特定实现和硬件**。论文指出，简单的实现下，小批量推理有增益，但批量较大时增益消失甚至可能下降，提示需要定制化的CUDA内核才能充分发挥硬件并行性。
3.  **数据集限制**：核心实验基于ImageNet-1k及其变体，虽然验证了泛化性，但领域的广泛性有待在更丰富的数据（如医学、遥感）上验证。
4.  **理论分析较浅**：并行化有效性的解释基于直觉（残差块贡献变小）和实验，缺乏更深入的理论分析。
## 个人评论

这篇论文的价值在于其**简洁性和实用性**。它没有提出复杂的新架构，而是揭示了几个基于标准ViT的、易于实现的改进洞察，对后续研究和工程实践有直接启发：
1.  **对研究的启发**：并行化思路提供了一种在不增加计算复杂度下改变网络“形状”（更宽更浅）的视角，这可能启发对Transformer深度与宽度平衡的新探索。
2.  **对模型改写的启发**：**选择性微调**是一个极其高效的策略。在资源受限或需要快速适配多个下游任务时，可以优先考虑只调参少的注意力层，这比微调整个模型或使用参数高效的适配器更简单直接。
3.  **对实验设计的启发**：论文强调了在比较不同架构时，需要仔细控制变量（如保持参数量和FLOPs一致），否则比较可能不公平（如对比并行化和增加宽度）。
4.  **对自监督学习的启发**：hMLP stem的设计理念（禁止patch间通信）为将卷积式的归纳偏置引入Transformer而不破坏其全局序列建模能力，提供了一个清晰的范式。

### 使用建议

- **快速了解**：重点阅读**摘要、引言、第3/4/5节的开头总结段落以及结论**。可以迅速把握三个核心贡献。
- **复现实验**：需要仔细阅读**第2.2节实验设置**和**第3.3、4、5节的具体实验细节**。特别注意训练超参数（学习率、随机深度率、LayerScale）和评估协议，这是复现结果的关键。
- **借鉴创新点**：
    - 若想改进模型效率：学习**并行化思路**（第3节），尝试在自己的ViT变体中应用。
    - 若想减少微调成本：借鉴**选择性微调**（第4节），在跨分辨率或跨任务适配中只训练注意力层。
    - 若做自监督学习：研究**hMLP stem的设计**（第5节），思考如何设计与预训练任务兼容的预处理模块。
- **写Related Work**：可以放在以下几个类别中：视觉Transformer架构优化、高效Transformer、Transformer的迁移学习与微调、自监督视觉Transformer。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉领域的神经网络架构设计与优化方向，具体聚焦于**视觉Transformer (Vision Transformer, ViT)** 的架构改进和训练策略。它旨在解决ViT在效率、微调成本和自监督学习兼容性方面的优化问题。根据文件名“Parallel ViT.pdf”和给定主题“B_注意力算子模块”，这篇论文的核心内容（并行化注意力/FFN层、选择性微调注意力层）与注意力模块的计算和优化直接相关，非常适合放在“B_注意力算子模块”主题下，作为研究Transformer注意力机制效率与实用性的重要参考。

## 2. 一句话总结
本文通过提出并行化ViT层结构、仅微调注意力层以及设计MLP-based的patch预处理层，揭示了简单易行的改进视觉Transformer设计和训练的三种有效方法。

## 3. 背景与问题
- **为什么要做**：Vision Transformer (ViT) 在计算机视觉任务中取得了巨大成功，但其设计和训练程序的优化探索相对有限。作者认为存在一些简单但未被充分探索的改进方向。
- **之前方法的问题**：
  1.  标准ViT采用顺序层结构，在网络较深时可能面临优化困难。
  2.  在进行分辨率调整或下游任务微调时，通常需要对整个网络进行全参数微调，计算成本和内存峰值高，且不同任务无法共享大部分参数。
  3.  基于patch掩码的自监督学习（如BEiT）需要与patch预处理（如卷积主干）结合，但标准的卷积操作会在patch间传播信息，破坏自监督学习任务所需的独立性。
- **核心矛盾**：如何在**不显著损害模型性能**的前提下，**提升ViT的推理效率（如通过并行化）、降低微调和适配的成本（计算与内存）、并增强其与基于patch的自监督学习方法的兼容性**。

## 4. 核心贡献
本文的核心贡献是提出了三个具体的、易于实现的见解：
1.  **并行Vision Transformer**：提出了一种简单的并行化ViT层结构的方法。将原本顺序执行的MHSA和FFN残差块进行配对并行处理，在保持相同参数量和计算量的同时，使网络变得更“浅”更“宽”，以降低延迟、简化优化。
2.  **微调注意力足矣**：发现在适应更高分辨率或迁移到其他分类任务时，**仅微调多头自注意力层（MHSA）的权重，同时冻结前馈网络层（FFN）** 的策略，其精度与全网络微调无显著差异。这能节省计算、降低峰值内存，并允许参数占主导的FFN层在不同任务间共享。
3.  **用于自监督学习的Patch预处理**：提出了一种分层MLP（hMLP）主干，用于在基于掩码的自监督学习（如BEiT）之前预处理图像块。该主干通过交替的MLP层和patch聚合操作实现，严格禁止patch间通信，从而与自监督训练兼容，并能在有监督设置下取得与最佳卷积主干相当的效果。

## 5. 方法详解
### 整体框架
本文并未提出一个单一的全新网络框架，而是在标准的ViT架构基础上，提出了三种独立的、可组合的改进策略。核心是围绕ViT中的基本构建块——**多头自注意力层**和**前馈网络层**——进行重组和选择性训练。

### 关键模块与机制
#### 1. 并行ViT (Parallel ViT)
- **机制**：将原本顺序的两个Transformer块（`MHSA_l` -> `FFN_l` -> `MHSA_{l+1}` -> `FFN_{l+1}`）重组为并行结构。
- **输入输出**：输入 `x_l` 经过并行处理后得到输出 `x_{l+2}`。
- **数学公式与直观解释**：
  - 顺序处理：`x'_{l+1} = x_l + MHSA_l(x_l)`， `x_{l+1} = x'_{l+1} + FFN_l(x'_{l+1})`；`x'_{l+2} = x_{l+1} + MHSA_{l+1}(x_{l+1})`， `x_{l+2} = x'_{l+2} + FFN_{l+1}(x'_{l+2})`。
  - 并行处理：`x_{l+1} = x_l + MHSA_{l,1}(x_l) + MHSA_{l,2}(x_l)`；`x_{l+2} = x_{l+1} + FFN_{l,1}(x_{l+1}) + FFN_{l,2}(x_{l+1})`。
  - **直观解释**：随着网络变深，每个残差块对整体函数的贡献越来越小，因此可以用近似 `r'(x + r(x)) ≈ r'(x)` 来理解。这使得并行处理多个块成为可能，从而减少顺序计算步骤。
- **与已有方法的差异**：不同于直接增加工作维度（width）来增加模型容量（会导致参数和计算量二次增长），并行化在保持参数和FLOPs不变的情况下，增加了模型的宽度（并行处理能力）。

#### 2. 选择性微调策略
- **输入输出**：微调时，输入是预训练好的ViT模型和新的目标数据集；输出是适配后的模型。
- **关键机制**：仅更新MHSA层的权重，而FFN层的权重保持冻结（来自预训练模型）。
- **直观解释**：MHSA层负责捕捉数据间的依赖关系和全局上下文，这部分在分辨率改变或任务改变时需要调整。而FFN层可以视为对每个token进行独立的非线性变换，其功能在预训练后相对稳定，可以跨任务复用。

#### 3. hMLP Patch预处理主干
- **整体框架**：在将图像输入标准ViT之前，先通过一个分层的MLP主干进行处理。
- **模块与连接**：该主干由多个MLP层和patch聚合操作交替组成。聚合操作（如使用步长大于1的卷积或池化）减少序列长度（即降低分辨率），而MLP层对每个token进行独立变换。**关键设计**是禁止任何跨patch的通信，确保每个输出token只依赖于原始图像的一个局部区域，从而与基于patch掩码的自监督学习（掩码是在patch级别进行的）兼容。
- **训练方式**：在自监督学习（如BEiT）中，图像先通过hMLP stem得到patch序列，然后再对序列进行随机掩码，输入Transformer进行重建训练。
- **推理流程**：与标准ViT相同，图像经过hMLP stem处理后，序列输入Transformer进行分类或其他任务。

## 6. 实验与结果
### 数据集
- 主要数据集：**ImageNet-1k** (用于训练和验证)。
- 辅助测试集：**ImageNet-V2** (matched frequency) 提供独立测试视角。
- 迁移学习数据集：**六个较小的数据集**（文中未列出具体名称，但指出在这些数据集上测量了转移性能）。
- 自监督学习评估数据集：主要也在ImageNet-1k上进行。

### 对比方法
- **基线模型**：标准的顺序ViT（ViT-Ti, ViT-S, ViT-B, ViT-L）以及它们的变种（不同深度、是否使用LayerScale）。
- **对比架构**：与**增加工作维度**（更宽）的ViT模型进行参数和FLOPs近似的公平对比。
- **自监督学习对比**：与使用卷积主干（Conv-Stem）的BEiT方法进行对比。

### 评价指标
- **分类精度**：ImageNet-1k验证集和ImageNet-V2测试集的Top-1准确率。
- **效率指标**：模型参数量（params）、计算量（FLOPs）、推理速度（images/s）、峰值内存（MB）。

### 主实验结果
- **并行ViT效果**：在具有足够深度的模型上（如36或60个块），**并行两个分支的模型（如ViT-B18×2）性能与顺序模型相当甚至更优**。例如，ViT-B36顺序模型在400 epochs+LS下为84.1%，而并行版本ViT-B18×2在相同训练设置下达到84.1%（表2）。对于较浅的小模型（如ViT-Ti, ViT-S 24层），顺序版本通常更好（图2）。
- **选择性微调结果**：将预训练于224×224的ViT模型微调至384×384分辨率时，**仅微调MHSA层**的精度与全参数微调的精度差异在标准差（±0.1）之内（表5）。例如，ViT-S仅微调MHSA层在ImageNet-val上达到84.4%，与全微调的84.3%相当。
- **hMLP stem效果**：在BEiT自监督预训练框架下，提出的hMLP stem效果优于传统的卷积主干（Conv-Stem）。在有监督设置下，其精度与对比中最佳的卷积主干持平。
- **效率信息**：
  - **并行化**：主要优势在小批量（batch size）推理时，可获得显著速度提升（表4）。例如，ViT-B18×2在batch size=1时，并行实现比顺序实现快45%。
  - **选择性微调**：仅微调MHSA层，FFN参数量（约占模型主体参数2/3）被冻结，大幅减少可训练参数、计算量和训练内存峰值。
  - **参数/计算对比**：并行化模型与同等深度的顺序模型具有完全相同的参数量和FLOPs（表3）。与增加宽度的模型相比，在参数和FLOPs近似时，并行/顺序模型通常精度更高（表3）。

### 消融与泛化实验
- **消融**：研究了并行分支数量（1,2,3,4）对精度的影响，发现两个并行分支是最优平衡点（图1）。
- **泛化**：将仅微调MHSA层的策略应用于六个较小数据集的迁移学习任务，发现对于大模型（ViT-L），精度损失有限。

## 7. 这篇论文真正有价值的地方
这篇论文的价值在于其**简洁性和实用性**。它没有提出复杂的新架构，而是揭示了几个基于标准ViT的、易于实现的改进洞察，对后续研究和工程实践有直接启发：
1.  **对研究的启发**：并行化思路提供了一种在不增加计算复杂度下改变网络“形状”（更宽更浅）的视角，这可能启发对Transformer深度与宽度平衡的新探索。
2.  **对模型改写的启发**：**选择性微调**是一个极其高效的策略。在资源受限或需要快速适配多个下游任务时，可以优先考虑只调参少的注意力层，这比微调整个模型或使用参数高效的适配器更简单直接。
3.  **对实验设计的启发**：论文强调了在比较不同架构时，需要仔细控制变量（如保持参数量和FLOPs一致），否则比较可能不公平（如对比并行化和增加宽度）。
4.  **对自监督学习的启发**：hMLP stem的设计理念（禁止patch间通信）为将卷积式的归纳偏置引入Transformer而不破坏其全局序列建模能力，提供了一个清晰的范式。

## 8. 局限与问题
1.  **方法适用场景**：并行ViT的优势主要在**深层、高容量模型**上显现。对于中小模型，标准顺序结构可能更优且易于优化。
2.  **实验局限性**：
    - 迁移学习仅测试了**分类任务**，未涉及检测、分割等更复杂的下游任务。
    - 自监督学习实验主要围绕**BEiT**，未验证与MAE等其他主流方法的兼容性。
    - 速度提升依赖于**特定实现和硬件**。论文指出，简单的实现下，小批量推理有增益，但批量较大时增益消失甚至可能下降，提示需要定制化的CUDA内核才能充分发挥硬件并行性。
3.  **数据集限制**：核心实验基于ImageNet-1k及其变体，虽然验证了泛化性，但领域的广泛性有待在更丰富的数据（如医学、遥感）上验证。
4.  **理论分析较浅**：并行化有效性的解释基于直觉（残差块贡献变小）和实验，缺乏更深入的理论分析。

## 9. 我该怎么使用这篇论文
- **快速了解**：重点阅读**摘要、引言、第3/4/5节的开头总结段落以及结论**。可以迅速把握三个核心贡献。
- **复现实验**：需要仔细阅读**第2.2节实验设置**和**第3.3、4、5节的具体实验细节**。特别注意训练超参数（学习率、随机深度率、LayerScale）和评估协议，这是复现结果的关键。
- **借鉴创新点**：
    - 若想改进模型效率：学习**并行化思路**（第3节），尝试在自己的ViT变体中应用。
    - 若想减少微调成本：借鉴**选择性微调**（第4节），在跨分辨率或跨任务适配中只训练注意力层。
    - 若做自监督学习：研究**hMLP stem的设计**（第5节），思考如何设计与预训练任务兼容的预处理模块。
- **写Related Work**：可以放在以下几个类别中：视觉Transformer架构优化、高效Transformer、Transformer的迁移学习与微调、自监督视觉Transformer。

## 10. 和其他论文的关系
本文与以下工作密切相关：
- [[ViT (Dosovitskiy et al., 2020)]]：本文的基线模型。
- [[DeiT (Touvron et al., 2021)]]：作者先前工作，本文部分训练策略（如LayerScale）在此基础上发展。
- [[BEiT (Bao et al., 2021)]]：本文第3点贡献（hMLP stem）所针对和改进的自监督学习框架。
- [[MAE (He et al., 2022)]]：另一种主流的基于掩码的自监督学习方法，本文思路可能也相关。
- [[Wightman et al. (2021) 的A2训练程序]]：本文采用的基线训练流程。
- [[LayerScale (Touvron et al., 2021)]]：本文用于稳定大模型训练的关键技术之一。

## 11. 关键词
视觉Transformer (ViT), 并行网络, 选择性微调, 注意力层, 前馈网络层, 自监督学习, patch预处理, hMLP主干, 计算效率, 参数共享, ImageNet, 迁移学习

## 12. 可信度说明
本笔记内容**严格基于用户提供的PDF前12页文本**，主要包括了摘要、引言、第2节背景、第3节并行ViT的完整内容、第4节选择性微调的前半部分，以及部分图表描述。所有引用的数字（如准确率、参数量、速度）均直接摘录自文本。
提取的文本质量良好，覆盖了论文的核心方法、实验设置和主要结果。但由于文本仅包含前12页（共22页），**第4节微调的完整实验细节、第5节自监督学习的完整实验与结果、以及后续的讨论、结论和完整参考文献未能获取**。因此，本笔记在涉及这些部分的总结时，主要依据文本中已给出的概述性描述。对于未能明确看到的信息（如六个迁移学习数据集的具体名称、部分消融实验的完整数据），已在文中明确标注。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/Parallel ViT.txt` (22/22 页; 原 AI 主体 12/22 + 全文补读 13-22); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-22; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-22。
- **提取情况**: 缺失页 10 页, 其中 10 页提取到可读文本。缺失页包含正文/附录内容, 其中约 6 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Figure 6: Performance of patch pre-processing in the
- p.13: Results with BeiT training. We report the results with BeiT, fine-tuned on ImageNet-
- p.14: 6 Conclusion
- p.14: First, we investigated a simple but effective way to parallelize them, showing a
- p.14: Last, we introduced a simple patch pre-processing stem, which processes patches
- p.15: References
- p.15: Conference on Computer Vision (2019)
- p.15: Computer Vision (2020)
- p.15: ConViT: Improving vision transformers with soft convolutional inductive bi-
- p.15: Recognition (2021)
- p.16: International Conference on Learning Representations (2021)
- p.17: Computer Vision and Pattern Recognition (2019)

### 缺失页关键摘录

- p.13: Table 7: Patch pre-processing: Performance in top1 accuracy with for a ViT-B12. All models are (1)
- p.13: when used with BeiT. We report the result of a ViT-B13 to provide the performance of a vanilla trans-
- p.13: former with more FLOPS. We measure the standard deviation for the two linear stem baselines and our
- p.13: Figure 6: Performance of patch pre-processing in the
- p.13: plexity (+0.8% FLOPS compared to the ViT-B12 in
- p.13: lar number of FLOPS. Our hMLP stem obtains a comparable performance but with
- p.13: val, in the right-most column of Table 7. We use the code of BeiT [3] with their
- p.13: effective and provides an improvement of +0.3/+0.4 top1 accuracy compared to
- p.13: est of hMLP in the context of masked self-supervised learning is clear in Figure 6,
- p.14: tuning large models or/and transferring to a dataset with few training images.
- p.16: P ., Belongie, S.J.: The inaturalist challenge 2017 dataset. arXiv preprint
- p.21: Table 8: Comparison our baseline with previous training procedures. We only include results that
<!-- AI_READING_NOTE_END -->
