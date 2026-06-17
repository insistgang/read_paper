---
title: Simple Baselines for Image Restoration
authors:
  - "Liangyu Chen"
  - "Xiaojie Chu"
  - "Xiangyu Zhang"
  - "Jian Sun"
year: 2022
venue: "arXiv"
doi: 
pdf: [[NAF.pdf]]
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
extract_cache: .paper-cache/extracts/NAF.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/21 pages"
---
# Simple Baselines for Image Restoration

## 基本信息
- **PDF**: [[NAF.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Simple Baselines for Image Restoration |
| **作者** | Liangyu Chen; Xiaojie Chu; Xiangyu Zhang; Jian Sun |
| **发表时间** | 2022 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Althoughtherehavebeensignificantadvancesinthefieldof imagerestorationrecently,thesystemcomplexityofthestate-of-the-art (SOTA)methodsisincreasingaswell,whichmayhindertheconvenient analysis and comparison of methods. In this paper, we propose a sim- ple baseline that exceeds the SOTA methods and is computationally efficient. To further simplify the baseline, we reveal that the nonlinear activation functions, e.g. Sigmoid, ReLU, GELU, Softmax, etc. are not necessary:theycouldbereplacedbymultiplicationorremoved.Thus,we derive a Nonlinear Activation Free Network, namely NAFNet, from the baseline.SOTAresultsareachievedonvariouschallengingbenchmarks, e.g.33.69dBPSNRonGoPro(forimagedeblurring),exceedingthepre- vious SOTA 0.38 dB with only 8.4% of its computational costs; 40.30 dBPSNRonSIDD(forimagedenoising),exceedingthepreviousSOTA 0.28dBwithlessthanhalfofitscomputationalcosts.Thecodeandthe pre-trainedmodelsarereleasedatgithub.com/megvii-research/NAFNet.

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：尽管深度学习在图像恢复领域取得了显著成功，但最先进方法的系统复杂性（包括块间复杂性和块内复杂性）也在不断增加，这阻碍了对方法的便捷分析和比较。(p.1, p.2)
- **之前方法的问题**：SOTA方法通常采用复杂的网络架构（如多阶段网络、多尺度特征融合）和复杂的内部模块（如Restormer中的转置注意力、门控卷积前馈网络），导致系统复杂度高，不便于快速验证新想法。(p.1, p.2)
- **核心矛盾**：作者希望探究一个根本问题：是否一个具有**低块间复杂度**（采用简单的单阶段UNet）和**低块内复杂度**（使用简单组件）的网络，也能达到SOTA性能？(p.1)
## 关键贡献

1.  **构建了一个简单高效的基线网络**：通过系统性的消融实验，从最基础的PlainNet块出发，逐步验证并添加必要的组件（Layer Normalization, GELU, 通道注意力），形成了一个超越当时SOTA方法且计算成本更低的基线网络（Baseline）。(p.2, p.5, p.7)
2.  **提出了NAFNet**：通过揭示GELU与门控线性单元（GLU）的联系，以及通道注意力与GLU的形式相似性，进一步用**简单乘法操作（SimpleGate）** 替换GELU，用**简化通道注意力（Simplified Channel Attention）** 替换标准通道注意力，从而去除了网络中所有非线性激活函数，得到了NAFNet。(p.2, p.7, p.8, p.9)
3.  **证明了非线性激活函数的可替代性**：首次在计算机视觉的SOTA任务中实证表明，非线性激活函数可能不是必要的，它们可以被简单的逐元素乘法操作替代或去除而不损失性能，甚至有所提升。这扩展了网络设计的思路。(p.2, p.9)
4.  **提出了两个具体的简化算子**：**SimpleGate**（将特征图在通道维度分成两半并逐元素相乘）和**简化通道注意力（SCA）**（对池化后的特征仅用一个线性层计算通道权重）。(p.8, p.9)
## 方法

### 整体框架
- 采用经典的**单阶段UNet架构**，以降低块间复杂度。(p.4, p.5)
- **输入**：退化的图像（如模糊、含噪图像）。
- **输出**：恢复后的清晰图像。

### 关键模块与连接（从PlainNet到NAFNet的演进）
1.  **PlainNet块**（图3b）：包含最基本的**卷积**、**ReLU**激活函数和**残差连接**。这是研究的起点。(p.5)
2.  **基线块**（图3c）：在PlainNet块基础上：
    - 添加了**层归一化（Layer Normalization）**，以稳定训练，允许使用更大的学习率。(p.5)
    - 将ReLU替换为**GELU**激活函数。(p.6)
    - 在末尾加入了**通道注意力（Channel Attention, CA）**模块，用于聚合全局信息。(p.6)
    - 组件连接顺序大致为：层归一化 -> 卷积 -> GELU -> 卷积 -> 通道注意力 -> 残差连接。
3.  **NAFNet块**（图3d）：对基线块进行终极简化：
    - **用SimpleGate替换GELU**：SimpleGate公式为`SimpleGate(X, Y) = X ⊙ Y`，其中X和Y是将输入特征图在通道维度平分得到的两部分。它用一次逐元素乘法实现了非线性。(p.8)
    - **用简化通道注意力（SCA）替换标准CA**：SCA公式为`SCA(X) = X * Wpool(X)`，其中`pool`是全局平均池化，`W`是一个全连接层。它去掉了原CA中的ReLU和Sigmoid，只保留了聚合全局信息（池化）和通道交互（线性变换）的核心功能。(p.9)
    - 组件连接顺序大致为：层归一化 -> 卷积 -> SimpleGate -> 卷积 -> 简化通道注意力 -> 残差连接。
    - **关键点**：此时，网络中已**不存在任何非线性激活函数**（如ReLU, GELU, Sigmoid）。(p.9)

### 数学公式与机制的直观解释
- **GELU作为GLU的特例**：GELU公式为`GELU(x) = xΦ(x)`，其中Φ是正态分布的累积分布函数。这与GLU公式`Gate(X) = f(X) ⊙ σ(g(X))`形式相似，可视为f和g是恒等映射，σ是Φ的特例。(p.8)
- **核心洞察**：GLU结构`f(X) ⊙ g(X)`本身（即使没有σ）就通过两个线性变换的乘积引入了非线性。因此，网络中的非线性可以来自这种结构，而非传统的激活函数。(p.8)

### 训练方式
- 使用Adam优化器（β1=0.9, β2=0.9，权重衰减为0）。(p.10)
- 训练200K次迭代，初始学习率为1e-3，采用余弦退火策略降至1e-6。(p.10)
- 训练图像块大小为256×256，批大小为32。(p.10)
- 采用了**TLC**（Test-time Local Converter）策略来解决分块训练和整图测试带来的性能下降问题。(p.10)
- 采用了**skip-init**来稳定训练。(p.10)

### 推理流程
论文未在提供文本中详细描述推理流程，但提到测试时使用完整图像，并应用TLC策略。

### 和已有方法的差异
- **与Restormer等相比**：Restormer等方法使用复杂的自注意力机制（如转置注意力）和带有非线性激活的前馈网络。NAFNet则使用更简单的深度卷积和通道交互，且完全去除了非线性激活函数，结构更简单，计算更高效。(p.5, p.7)
- **与传统CNN相比**：传统CNN依赖ReLU等非线性激活。NAFNet用SimpleGate（乘法）和线性变换的组合来产生非线性，提供了一种新的网络设计范式。(p.8)
## 实验

### 使用的数据集
- **图像去噪**：SIDD数据集。(p.4)
- **图像去模糊**：GoPro数据集。(p.4)

### 对比方法
包括HINet, Restormer, MPRNet, UFormer, NBNet, MIMO-UNet, DeepRFT等当时多个SOTA方法。(p.2, p.10)

### 评价指标
- 主要指标：**PSNR**（峰值信噪比）和**SSIM**（结构相似性）。(p.10)
- 效率指标：计算复杂度（MACs，乘加运算次数）。(p.2, p.4)

### 主实验结果
- **NAFNet在GoPro数据集**（图像去模糊）上达到**33.69 dB PSNR**，超过当时SOTA方法0.38 dB，且**计算成本仅为该方法的8.4%**。(p.1, p.2)
- **NAFNet在SIDD数据集**（图像去噪）上达到**40.30 dB PSNR**，超过当时SOTA方法0.28 dB，**计算成本不到其一半**。(p.1, p.2)
- 作者构建的简单基线网络也已超越SOTA（GoPro 33.40 dB， SIDD 40.28 dB）。(p.2)

### 消融实验
- **从PlainNet到基线**：引入Layer Normalization (LN)使训练稳定且允许大学习率，在SIDD和GoPro上分别带来0.44 dB和3.39 dB的巨大提升。将ReLU换成GELU在GoPro上带来0.21 dB提升。加入通道注意力在SIDD和GoPro上分别带来0.14 dB和0.24 dB提升。(p.5, p.6, p.7, Tab.1)
- **从基线到NAFNet**：将基线中的GELU替换为SimpleGate，在SIDD和GoPro上分别提升0.08 dB和0.41 dB。将通道注意力替换为简化通道注意力，进一步带来0.03 dB和0.09 dB的提升。(p.8, p.9, Tab.2)

### 泛化实验
论文还将NAFNet应用于**raw图像去噪**和**带JPEG伪影的图像去模糊**任务，但具体结果未在提供的文本段落中详述。(p.9)

### 速度/参数量/FLOPs
- 主要以**MACs**（乘加运算次数）衡量计算成本。实验在输入尺寸为256×256的条件下进行。(p.10)
- NAFNet的MACs在**10到1000G**的范围内，具体取决于模型宽度和块数，图1展示了其在精度-计算量帕累托前沿的优势。(p.2)
## 局限

- **适用场景的假设**：论文实验主要集中在图像去噪和去模糊上，其结论（非线性激活不必要）是否适用于更复杂或数据分布不同的任务（如超分辨率、图像生成）尚待验证。
- **实验范围的局限**：尽管在SIDD和GoPro上取得了SOTA，但这两个数据集不能代表所有图像恢复场景。在更广泛的基准上验证其泛化能力是必要的。
- **未讨论参数量与速度**：论文主要关注计算复杂度（MACs），但未在提供文本中详细讨论模型参数量和实际推理速度（FPS），这对部署很重要。
- **对设计深度的依赖**：方法的成功在一定程度上依赖于特定的超参数选择（如默认宽度32，块数36），文中虽有消融，但最优配置的获取过程未完全展开。
- **复现细节**：虽然提供了训练设置，但TLC、skip-init等技术的具体实现细节对完全复现很重要，可能需要参考其代码。
## 个人评论

1.  **“做减法”的研究范式**：本文最值得学习的是其研究思路——不盲目堆砌SOTA组件，而是从最简单的基线出发，通过系统性的消融实验，**严格验证每个组件的必要性**，最终甚至能大胆去除“不可或缺”的非线性激活函数。这为设计高效模型提供了清晰的方法论。
2.  **对非线性激活的深刻理解**：揭示了GELU与GLU的内在联系，以及乘法操作本身可以提供足够的非线性。这一发现将设计空间从“选择哪种激活函数”扩展到“如何产生非线性”，启发了更多创新的可能。
3.  **工程实践的直接启发**：SimpleGate和简化通道注意力是极其简洁、易于实现的算子，但能带来显著的性能提升。这为其他研究者在自己的网络中快速替换或插入高效模块提供了直接可用的方案。
4.  **效率与性能的平衡典范**：论文明确给出了在达到或超越SOTA性能的同时，将计算成本降低一个数量级的具体方案，展示了简单设计在效率上的巨大潜力。

### 使用建议

- **如果快速了解**：只读**摘要**、**引言**（第1节）和**结论/贡献**部分，即可掌握论文核心思想、动机和主要成果。
- **如果复现**：重点精读**第3节（构建基线）**、**第4节（NAFNet详解）** 和**第5.1节（消融实验）**，结合其公开代码和模型配置，关注训练细节（优化器、学习率、TLC、skip-init）。
- **如果借鉴创新点**：
    - 学习**SimpleGate**和**简化通道注意力（SCA）** 的具体实现，考虑将它们作为轻量化、高效的模块插入自己的网络。
    - 学习其**从简单基线开始做系统消融**的研究方法，用于评估自己设计的模块是否真的必要。
- **如果写related work**：可放在以下几个类别：
    - `[[图像恢复/去噪/去模糊]]` 领域的最新工作。
    - `[[注意力机制/通道注意力]]` 的简化与应用。
    - `[[轻量化网络设计]]` 或 `[[高效网络架构]]`。
    - `[[激活函数/非线性]]` 研究的延伸。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中的底层图像处理方向，具体是**图像恢复**领域，核心解决的是**图像去噪**与**图像去模糊**任务。论文提出了一种计算高效、结构简单的基线网络NAFNet，旨在以更低的复杂度达到或超越当时的最优性能。根据文件名和主题标注“B_注意力算子模块”，虽然论文整体是网络架构设计，但其核心贡献之一是提出了一个简化的注意力算子（简化通道注意力，Simplified Channel Attention），因此适合放在“注意力算子模块”这一主题下。

## 2. 一句话总结
本文通过构建并逐步简化一个通用图像恢复基线网络，揭示并证明了非线性激活函数（如Sigmoid, ReLU, GELU）在高性能网络中并非必要，最终提出了无需非线性激活函数的NAFNet，在多个基准测试上实现了SOTA性能与高计算效率。

## 3. 背景与问题
- **为什么要做**：尽管深度学习在图像恢复领域取得了显著成功，但最先进方法的系统复杂性（包括块间复杂性和块内复杂性）也在不断增加，这阻碍了对方法的便捷分析和比较。(p.1, p.2)
- **之前方法的问题**：SOTA方法通常采用复杂的网络架构（如多阶段网络、多尺度特征融合）和复杂的内部模块（如Restormer中的转置注意力、门控卷积前馈网络），导致系统复杂度高，不便于快速验证新想法。(p.1, p.2)
- **核心矛盾**：作者希望探究一个根本问题：是否一个具有**低块间复杂度**（采用简单的单阶段UNet）和**低块内复杂度**（使用简单组件）的网络，也能达到SOTA性能？(p.1)

## 4. 核心贡献
1.  **构建了一个简单高效的基线网络**：通过系统性的消融实验，从最基础的PlainNet块出发，逐步验证并添加必要的组件（Layer Normalization, GELU, 通道注意力），形成了一个超越当时SOTA方法且计算成本更低的基线网络（Baseline）。(p.2, p.5, p.7)
2.  **提出了NAFNet**：通过揭示GELU与门控线性单元（GLU）的联系，以及通道注意力与GLU的形式相似性，进一步用**简单乘法操作（SimpleGate）** 替换GELU，用**简化通道注意力（Simplified Channel Attention）** 替换标准通道注意力，从而去除了网络中所有非线性激活函数，得到了NAFNet。(p.2, p.7, p.8, p.9)
3.  **证明了非线性激活函数的可替代性**：首次在计算机视觉的SOTA任务中实证表明，非线性激活函数可能不是必要的，它们可以被简单的逐元素乘法操作替代或去除而不损失性能，甚至有所提升。这扩展了网络设计的思路。(p.2, p.9)
4.  **提出了两个具体的简化算子**：**SimpleGate**（将特征图在通道维度分成两半并逐元素相乘）和**简化通道注意力（SCA）**（对池化后的特征仅用一个线性层计算通道权重）。(p.8, p.9)

## 5. 方法详解
### 整体框架
- 采用经典的**单阶段UNet架构**，以降低块间复杂度。(p.4, p.5)
- **输入**：退化的图像（如模糊、含噪图像）。
- **输出**：恢复后的清晰图像。

### 关键模块与连接（从PlainNet到NAFNet的演进）
1.  **PlainNet块**（图3b）：包含最基本的**卷积**、**ReLU**激活函数和**残差连接**。这是研究的起点。(p.5)
2.  **基线块**（图3c）：在PlainNet块基础上：
    - 添加了**层归一化（Layer Normalization）**，以稳定训练，允许使用更大的学习率。(p.5)
    - 将ReLU替换为**GELU**激活函数。(p.6)
    - 在末尾加入了**通道注意力（Channel Attention, CA）**模块，用于聚合全局信息。(p.6)
    - 组件连接顺序大致为：层归一化 -> 卷积 -> GELU -> 卷积 -> 通道注意力 -> 残差连接。
3.  **NAFNet块**（图3d）：对基线块进行终极简化：
    - **用SimpleGate替换GELU**：SimpleGate公式为`SimpleGate(X, Y) = X ⊙ Y`，其中X和Y是将输入特征图在通道维度平分得到的两部分。它用一次逐元素乘法实现了非线性。(p.8)
    - **用简化通道注意力（SCA）替换标准CA**：SCA公式为`SCA(X) = X * Wpool(X)`，其中`pool`是全局平均池化，`W`是一个全连接层。它去掉了原CA中的ReLU和Sigmoid，只保留了聚合全局信息（池化）和通道交互（线性变换）的核心功能。(p.9)
    - 组件连接顺序大致为：层归一化 -> 卷积 -> SimpleGate -> 卷积 -> 简化通道注意力 -> 残差连接。
    - **关键点**：此时，网络中已**不存在任何非线性激活函数**（如ReLU, GELU, Sigmoid）。(p.9)

### 数学公式与机制的直观解释
- **GELU作为GLU的特例**：GELU公式为`GELU(x) = xΦ(x)`，其中Φ是正态分布的累积分布函数。这与GLU公式`Gate(X) = f(X) ⊙ σ(g(X))`形式相似，可视为f和g是恒等映射，σ是Φ的特例。(p.8)
- **核心洞察**：GLU结构`f(X) ⊙ g(X)`本身（即使没有σ）就通过两个线性变换的乘积引入了非线性。因此，网络中的非线性可以来自这种结构，而非传统的激活函数。(p.8)

### 训练方式
- 使用Adam优化器（β1=0.9, β2=0.9，权重衰减为0）。(p.10)
- 训练200K次迭代，初始学习率为1e-3，采用余弦退火策略降至1e-6。(p.10)
- 训练图像块大小为256×256，批大小为32。(p.10)
- 采用了**TLC**（Test-time Local Converter）策略来解决分块训练和整图测试带来的性能下降问题。(p.10)
- 采用了**skip-init**来稳定训练。(p.10)

### 推理流程
论文未在提供文本中详细描述推理流程，但提到测试时使用完整图像，并应用TLC策略。

### 和已有方法的差异
- **与Restormer等相比**：Restormer等方法使用复杂的自注意力机制（如转置注意力）和带有非线性激活的前馈网络。NAFNet则使用更简单的深度卷积和通道交互，且完全去除了非线性激活函数，结构更简单，计算更高效。(p.5, p.7)
- **与传统CNN相比**：传统CNN依赖ReLU等非线性激活。NAFNet用SimpleGate（乘法）和线性变换的组合来产生非线性，提供了一种新的网络设计范式。(p.8)

## 6. 实验与结果
### 使用的数据集
- **图像去噪**：SIDD数据集。(p.4)
- **图像去模糊**：GoPro数据集。(p.4)

### 对比方法
包括HINet, Restormer, MPRNet, UFormer, NBNet, MIMO-UNet, DeepRFT等当时多个SOTA方法。(p.2, p.10)

### 评价指标
- 主要指标：**PSNR**（峰值信噪比）和**SSIM**（结构相似性）。(p.10)
- 效率指标：计算复杂度（MACs，乘加运算次数）。(p.2, p.4)

### 主实验结果
- **NAFNet在GoPro数据集**（图像去模糊）上达到**33.69 dB PSNR**，超过当时SOTA方法0.38 dB，且**计算成本仅为该方法的8.4%**。(p.1, p.2)
- **NAFNet在SIDD数据集**（图像去噪）上达到**40.30 dB PSNR**，超过当时SOTA方法0.28 dB，**计算成本不到其一半**。(p.1, p.2)
- 作者构建的简单基线网络也已超越SOTA（GoPro 33.40 dB， SIDD 40.28 dB）。(p.2)

### 消融实验
- **从PlainNet到基线**：引入Layer Normalization (LN)使训练稳定且允许大学习率，在SIDD和GoPro上分别带来0.44 dB和3.39 dB的巨大提升。将ReLU换成GELU在GoPro上带来0.21 dB提升。加入通道注意力在SIDD和GoPro上分别带来0.14 dB和0.24 dB提升。(p.5, p.6, p.7, Tab.1)
- **从基线到NAFNet**：将基线中的GELU替换为SimpleGate，在SIDD和GoPro上分别提升0.08 dB和0.41 dB。将通道注意力替换为简化通道注意力，进一步带来0.03 dB和0.09 dB的提升。(p.8, p.9, Tab.2)

### 泛化实验
论文还将NAFNet应用于**raw图像去噪**和**带JPEG伪影的图像去模糊**任务，但具体结果未在提供的文本段落中详述。(p.9)

### 速度/参数量/FLOPs
- 主要以**MACs**（乘加运算次数）衡量计算成本。实验在输入尺寸为256×256的条件下进行。(p.10)
- NAFNet的MACs在**10到1000G**的范围内，具体取决于模型宽度和块数，图1展示了其在精度-计算量帕累托前沿的优势。(p.2)

## 7. 这篇论文真正有价值的地方
1.  **“做减法”的研究范式**：本文最值得学习的是其研究思路——不盲目堆砌SOTA组件，而是从最简单的基线出发，通过系统性的消融实验，**严格验证每个组件的必要性**，最终甚至能大胆去除“不可或缺”的非线性激活函数。这为设计高效模型提供了清晰的方法论。
2.  **对非线性激活的深刻理解**：揭示了GELU与GLU的内在联系，以及乘法操作本身可以提供足够的非线性。这一发现将设计空间从“选择哪种激活函数”扩展到“如何产生非线性”，启发了更多创新的可能。
3.  **工程实践的直接启发**：SimpleGate和简化通道注意力是极其简洁、易于实现的算子，但能带来显著的性能提升。这为其他研究者在自己的网络中快速替换或插入高效模块提供了直接可用的方案。
4.  **效率与性能的平衡典范**：论文明确给出了在达到或超越SOTA性能的同时，将计算成本降低一个数量级的具体方案，展示了简单设计在效率上的巨大潜力。

## 8. 局限与问题
- **适用场景的假设**：论文实验主要集中在图像去噪和去模糊上，其结论（非线性激活不必要）是否适用于更复杂或数据分布不同的任务（如超分辨率、图像生成）尚待验证。
- **实验范围的局限**：尽管在SIDD和GoPro上取得了SOTA，但这两个数据集不能代表所有图像恢复场景。在更广泛的基准上验证其泛化能力是必要的。
- **未讨论参数量与速度**：论文主要关注计算复杂度（MACs），但未在提供文本中详细讨论模型参数量和实际推理速度（FPS），这对部署很重要。
- **对设计深度的依赖**：方法的成功在一定程度上依赖于特定的超参数选择（如默认宽度32，块数36），文中虽有消融，但最优配置的获取过程未完全展开。
- **复现细节**：虽然提供了训练设置，但TLC、skip-init等技术的具体实现细节对完全复现很重要，可能需要参考其代码。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读**摘要**、**引言**（第1节）和**结论/贡献**部分，即可掌握论文核心思想、动机和主要成果。
- **如果复现**：重点精读**第3节（构建基线）**、**第4节（NAFNet详解）** 和**第5.1节（消融实验）**，结合其公开代码和模型配置，关注训练细节（优化器、学习率、TLC、skip-init）。
- **如果借鉴创新点**：
    - 学习**SimpleGate**和**简化通道注意力（SCA）** 的具体实现，考虑将它们作为轻量化、高效的模块插入自己的网络。
    - 学习其**从简单基线开始做系统消融**的研究方法，用于评估自己设计的模块是否真的必要。
- **如果写related work**：可放在以下几个类别：
    - `[[图像恢复/去噪/去模糊]]` 领域的最新工作。
    - `[[注意力机制/通道注意力]]` 的简化与应用。
    - `[[轻量化网络设计]]` 或 `[[高效网络架构]]`。
    - `[[激活函数/非线性]]` 研究的延伸。

## 10. 和其他论文的关系
根据主题和内容，本文与以下方向的论文强相关：
- **图像恢复网络**：如文中反复对比的 `[[Restormer]]` (p.3, p.5, p.7)、`[[HINet]]` (p.10)、`[[MPRNet]]` (p.2, p.10)、`[[UFormer]]` (p.2)。
- **门控线性单元**：其理论基础来源于 `[[Gated Linear Units (GLU)]]` (p.3, p.7)，并对此进行了计算机视觉领域的应用和简化。
- **通道注意力**：标准实现参考了 `[[Squeeze-and-Excitation (SE)]]` 中的通道注意力 (p.6, p.8)，并对其进行了简化。
- **UNet架构**：采用了通用的 `[[UNet]]` 作为基础架构 (p.4)。

## 11. 关键词
图像恢复, 图像去噪, 图像去模糊, NAFNet, 简单基线, 非线性激活自由, 通道注意力, 简化通道注意力, SimpleGate, GELU, Layer Normalization, 计算效率

## 12. 可信度说明
本笔记主要基于提供的PDF文本的前12页生成，这部分内容涵盖了摘要、引言、相关工作、方法核心描述（第3、4节）以及部分实验结果（第5节开头）。提取文本质量良好，清晰记录了论文的核心动机、方法演进、关键公式和主要的定量结果。关于更详细的实验（如raw去噪）、完整的消融表格、以及与更多方法的视觉对比，可能在未提供的后续页面中，因此笔记中仅做了概括性描述。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/NAF.txt` (21/21 页; 原 AI 主体 12/21 + 全文补读 13-21); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-21; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-21。
- **提取情况**: 缺失页 9 页, 其中 9 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Nonlinear Activation Free Network 13
- p.13: MethodMPRNet MIRNet NBNet UFormer MAXIM HINet Restormer Baseline NAFNet
- p.13: MethodMIMO-UNet HINet MAXIM Restormer UFormer DeepRFT MPRNet Baseline NAFNet
- p.14: Noisy Image
- p.14: Reference, PSNR
- p.14: Table 8: Raw image denoising results
- p.14: Method PSNR SSIM MACs(G)
- p.14: 6 Conclusions
- p.14: By decomposing the SOTA methods, we extract the essential components and
- p.14: Acknowledgements: This research was supported by National Key R&D Pro-
- p.15: Appendix
- p.15: A Other Details

### 缺失页关键摘录

- p.13: PSNR MPRNet [37] MPRNet-local [8] NAFNet( ours )
- p.13: Table 6: Image Denoising Results on SIDD[1]
- p.13: PSNR 39.71 39.72 39.75 39.89 39.96 39.99 40.02 40.30 40.30
- p.13: set as 4Scenes (as the dataset contains 39 raw images of 4 different scenes in
- p.13: shown in Table 8 and Figure 7 demonstrate NAFNet can surpass PMRID quan-
- p.13: titatively and qualitatively. In addition, this experiment indicates our NAFNet
- p.13: dataset, the training setting follows [5,32], and we evaluate the result on 300 im-
- p.13: in Table 9, our method outperforms other competing methods, including the
- p.13: Table 7: Image Deblurring Results on GoPro[26]
- p.13: PSNR 32.68 32.71 32.86 32.92 32.97 33.23 33.31 33.40 33.69
- p.14: previous winning solution (HINet) on the REDS dataset of NTIRE 2021 Image
- p.15: We first discuss the setting of the ablation studies. In the baseline, the channel
<!-- AI_READING_NOTE_END -->
