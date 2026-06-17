---
title: "KAN: Kolmogorov–Arnold Networks"
authors:
  - "Ziming Liu"
  - "Yixuan Wang"
  - "Sachin Vaidya"
  - "Fabian Ruehle"
  - "James Halverson"
  - "Marin Soljacic"
  - "Thomas Y. Hou"
  - "Max Tegmark"
year: 2024
venue: accuracy and interpretability improvement over MLPs, at least on small-scale AI + Science tasks.
doi: 
pdf: [[kan.pdf]]
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
extract_cache: .paper-cache/extracts/kan.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/50 pages"
---
# KAN: Kolmogorov–Arnold Networks

## 基本信息
- **PDF**: [[kan.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | KAN: Kolmogorov–Arnold Networks |
| **作者** | Ziming Liu; Yixuan Wang; Sachin Vaidya; Fabian Ruehle; James Halverson; Marin Soljacic; Thomas Y. Hou; Max Tegmark |
| **发表时间** | 2024 |
| **刊物/会议** | accuracy and interpretability improvement over MLPs, at least on small-scale AI + Science tasks. |
| **DOI** | 未明确 |

## 摘要

> Inspired by the Kolmogorov-Arnold representation theorem, we propose Kolmogorov- Arnold Networks (KANs) as promising alternatives to Multi-Layer Perceptrons (MLPs). WhileMLPshavefixedactivationfunctionsonnodes(“neurons”),KANshavelearnable activation functions on edges (“weights”). KANs have no linear weights at all – every weightparameterisreplacedbyaunivariatefunctionparametrizedasaspline. Weshow that this seemingly simple change makes KANs outperform MLPs in terms of accuracy andinterpretability, onsmall-scaleAI+Sciencetasks. Foraccuracy, smallerKANscan achievecomparableorbetteraccuracythanlargerMLPsinfunctionfittingtasks. Theo- reticallyandempirically,KANspossessfasterneuralscalinglawsthanMLPs. Forinter- pretability, KANscanbeintuitivelyvisualizedandcaneasilyinteractwithhumanusers. Throughtwoexamplesinmathematicsandphysics,KANsareshowntobeuseful“collabo- rators”helpingscientists(re)discovermathematicalandphysicallaws.Insummary,KANs arepromisingalternativesforMLPs,openingopportunitie

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：多层感知机（MLP）是现代深度学习的基石，但存在显著缺点。在Transformer等架构中，MLP占据了绝大部分非嵌入参数（p.2），并且相对注意力层而言，其可解释性较差，通常需要事后分析工具（p.2）。
- **之前方法的问题**：MLP的灵感来源于通用逼近定理，其特点是节点上使用固定的激活函数。尽管强大，但MLP难以高效地优化低维单变量函数（内部自由度），并且其参数效率在某些任务上可能不是最优的。
- **核心矛盾**：作者想要解决的核心矛盾是：如何设计一种既具有强大表达能力（像MLP一样能学习组合结构），又能更高效地逼近函数（像样条一样能精确优化单变量函数），同时更易于人类理解和交互（可解释性）的神经网络模型。
## 关键贡献

1.  **提出KAN架构**：设计了一种基于Kolmogorov-Arnold表示定理的新型神经网络，其核心是将**可学习的激活函数（参数化为B样条）放置在边（权重）上**，而节点仅执行求和操作，彻底摒弃了线性权重矩阵（p.2, p.4）。
2.  **展示准确率优势**：通过实验证明，在小规模的科学任务上，更小的KAN可以达到与更大MLP相当或更好的精度，并且理论与实验表明KAN具有**更快的神经缩放律**（p.1, p.7-8）。
3.  **提升可解释性**：KAN的结构允许进行直观的可视化，并且易于与人类用户交互。论文通过数学（纽结理论）和物理（安德森局域化）的例子，展示了KAN如何作为“合作者”帮助科学家（重新）发现定律（p.1-2, p.10-11）。
4.  **提供理论保证**：定理2.1给出了KAN的逼近理论，表明如果目标函数存在平滑的Kolmogorov-Arnold表示，KAN能够以与维度无关的残差率进行逼近，从而**克服维度诅咒**（p.7）。
5.  **提出实用技术**：引入了**网格扩展技术**来逐步提高KAN的精度，以及网络**简化技术**来增强其可解释性（p.3, p.9-10）。
## 方法

- **整体框架**：KAN是一个全连接的前馈神经网络。其架构灵感来源于Kolmogorov-Arnold表示定理（公式2.1），该定理表明任何多元连续函数可以分解为有限个连续单变量函数与加法的组合（p.3-4）。
- **关键模块与数学机制**：
    - **KAN层**：一个具有`n_in`维输入和`n_out`维输出的KAN层，由一个`1D`函数的矩阵 `Φ = {ϕ_{q,p}}` 定义，其中每个`ϕ_{q,p}`是连接第`p`个输入神经元和第`q`个输出神经元的可学习单变量函数（p.5）。输出`x_{l+1}`是所有输入经对应函数处理后的求和：`x_{l+1, j} = Σ_i ϕ_{l, j, i}(x_{l, i})`（公式2.5）。
    - **激活函数参数化**：每条边上的函数`ϕ(x)`被实现为**残差形式**：`ϕ(x) = w_b * b(x) + w_s * spline(x)`（公式2.10）。其中`b(x)`通常取SiLU函数，`spline(x)`由可训练的B样条基函数的线性组合构成（p.6）。这种设计既保留了平滑的优化能力（通过样条），又包含了标准的非线性（通过基函数）。
    - **网络形状**：一个KAN由形状数组 `[n_0, n_1, ..., n_L]` 定义，表示各层的神经元数量（p.5）。原始Kolmogorov-Arnold表示对应一个形状为`[n, 2n+1, 1]`的两层KAN。
    - **与MLP的对比**：MLP将线性变换`W`和固定非线性`σ`分开处理：`MLP(x) = (W_{L-1} ∘ σ ∘ W_{L-2} ∘ σ ∘ ... ∘ W_0)x`（公式2.9）。而KAN将它们整合在一个函数矩阵`Φ`中：`KAN(x) = (Φ_{L-1} ∘ Φ_{L-2} ∘ ... ∘ Φ_0)x`（公式2.7）（p.6）。
- **训练方式**：由于所有操作可微，KAN可以通过**反向传播**进行训练（p.6）。参数初始化有特殊考虑，例如样条部分初始化为近似零（p.6）。在训练过程中，会动态更新样条网格以覆盖激活值的变化范围（p.6）。
- **推理流程**：给定输入`x_0`，依次通过各KAN层的函数矩阵进行变换和求和，最终得到输出（公式2.7）。
- **与已有方法的差异**：与MLP相比，KAN在边（而非节点）上学习非线性，没有传统的线性权重矩阵。与传统样条方法相比，KAN利用了多层结构来学习函数的组合特征，从而能在高维问题中克服维度诅咒（p.2）。
## 实验

- **使用的数据集**：PDF前12页提到了函数拟合任务（如`f(x,y)=exp(sin(x)+y^2)`，见图2.3）和泊松方程求解（p.10），但未提供完整的标准数据集列表。
- **对比方法**：主要与多层感知机（MLP）进行对比（p.1-2, p.8）。
- **评价指标**：主要使用**均方根误差（RMSE）** 作为准确率指标（p.8, 图2.3）。
- **主实验结果**：在提供的文本中，展示了KAN在函数拟合上的优势。例如，在图2.3中，随着网格大小`G`的增加，KAN的测试RMSE下降，并且遵循`~ G^{-4}`的缩放律，这与理论预测的`k+1=4`（对于三次样条）相符（p.8）。文中声称KAN能超越MLP达到更快的缩放律（p.8）。
- **消融/泛化实验**：文本提到了**网格扩展技术**的实验（图2.3），展示了通过增加样条网格点数`G`，KAN的精度可以阶梯式提升。理论部分（定理2.1）也给出了泛化误差的保证（p.7）。
- **效率信息**：参数量方面，一个深度L、宽度N、样条区间数G的KAN，参数量为`O(N^2 L G)`，而同等深度宽度的MLP为`O(N^2 L)`（p.7）。但论文指出KAN通常可以用更小的`N`来达到相同效果，从而节省参数并提高可解释性（p.7）。图2.3右下角显示了训练时间随网格大小`G`的增长情况。
## 局限

- **计算成本**：KAN的参数量是`O(N^2 L G)`，虽然可以通过更小的`N`弥补，但在需要极大网格`G`或网络非常宽/深时，其计算和内存开销可能仍高于MLP（p.7）。
- **假设依赖**：其理论优势（克服维度诅咒）依赖于目标函数存在平滑的Kolmogorov-Arnold表示这一假设（p.7）。对于不具备这种结构或函数极其不平滑的问题，KAN的优势可能无法体现。
- **实验规模**：从摘要和文中描述看，其优越性主要在“小规模AI + Science任务”上得到验证（p.1）。在更大规模、更通用的任务（如ImageNet分类、大规模语言建模）上的表现未知。
- **优化复杂性**：引入了样条参数化、网格动态更新等机制，可能使优化过程比标准MLP更复杂。
- **复现风险**：虽然提供了代码仓库，但样条相关操作的具体实现细节、超参数设置（如初始化方差σ、网格更新策略）对性能可能敏感。
## 个人评论

这篇论文最值得学习的点在于它**重新审视并成功应用了一个经典但曾被认为不实用的数学定理（Kolmogorov-Arnold定理）**，并将其转化为一个具有现代深度学习特性的实用框架。它提供了一种全新的建模视角：**在边（权重）上学习可解释的函数，而不是在节点上学习抽象的特征**。这启发我们思考神经网络架构设计的更多可能性，不一定要局限于“线性变换+固定激活”的范式。此外，论文将准确性、可解释性和理论保证结合起来的研究思路，对于希望推动可信AI和AI for Science的研究者具有重要参考价值。

### 使用建议

- **如果快速了解**：只读**摘要**、**引言**和**图0.1**，即可理解KAN的核心思想、动机和与MLP的关键区别。
- **如果复现**：重点阅读**第2.2节（KAN架构）**，特别是实现细节部分（残差激活函数、初始化、网格更新），并结合开源代码`https://github.com/KindXiaoming/pykan`。
- **如果借鉴创新点**：应学习其将**可学习函数置于边上的核心设计**，以及**网格扩展**这种逐步提升模型精度的技术。思考能否将这种“边激活”的思想应用到现有网络（如CNN、Transformer）的某个模块中。
- **如果写Related Work**：可放在“MLP替代架构”、“可解释神经网络”、“基于样条的神经网络”或“科学机器学习”类别中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于机器学习/深度学习基础模型架构研究方向。它旨在解决当前深度学习基石——多层感知机（MLP）存在的参数效率低、可解释性差等问题。论文提出了一种名为**Kolmogorov-Arnold Networks (KAN)** 的全新神经网络架构，作为MLP的一种有潜力的替代方案。该研究适合放在“神经网络架构创新”或“AI for Science”主题下，因为它不仅提出了新的模型，还强调了其在小规模科学任务（如函数拟合、偏微分方程求解、科学定律发现）中的优越性。

## 2. 一句话总结
该论文提出KAN，一种将可学习的单变量样条函数置于网络**边**上而非节点上的新型神经网络架构，旨在超越MLP在准确性和可解释性上的表现。

## 3. 背景与问题
- **为什么要做**：多层感知机（MLP）是现代深度学习的基石，但存在显著缺点。在Transformer等架构中，MLP占据了绝大部分非嵌入参数（p.2），并且相对注意力层而言，其可解释性较差，通常需要事后分析工具（p.2）。
- **之前方法的问题**：MLP的灵感来源于通用逼近定理，其特点是节点上使用固定的激活函数。尽管强大，但MLP难以高效地优化低维单变量函数（内部自由度），并且其参数效率在某些任务上可能不是最优的。
- **核心矛盾**：作者想要解决的核心矛盾是：如何设计一种既具有强大表达能力（像MLP一样能学习组合结构），又能更高效地逼近函数（像样条一样能精确优化单变量函数），同时更易于人类理解和交互（可解释性）的神经网络模型。

## 4. 核心贡献
1.  **提出KAN架构**：设计了一种基于Kolmogorov-Arnold表示定理的新型神经网络，其核心是将**可学习的激活函数（参数化为B样条）放置在边（权重）上**，而节点仅执行求和操作，彻底摒弃了线性权重矩阵（p.2, p.4）。
2.  **展示准确率优势**：通过实验证明，在小规模的科学任务上，更小的KAN可以达到与更大MLP相当或更好的精度，并且理论与实验表明KAN具有**更快的神经缩放律**（p.1, p.7-8）。
3.  **提升可解释性**：KAN的结构允许进行直观的可视化，并且易于与人类用户交互。论文通过数学（纽结理论）和物理（安德森局域化）的例子，展示了KAN如何作为“合作者”帮助科学家（重新）发现定律（p.1-2, p.10-11）。
4.  **提供理论保证**：定理2.1给出了KAN的逼近理论，表明如果目标函数存在平滑的Kolmogorov-Arnold表示，KAN能够以与维度无关的残差率进行逼近，从而**克服维度诅咒**（p.7）。
5.  **提出实用技术**：引入了**网格扩展技术**来逐步提高KAN的精度，以及网络**简化技术**来增强其可解释性（p.3, p.9-10）。

## 5. 方法详解
- **整体框架**：KAN是一个全连接的前馈神经网络。其架构灵感来源于Kolmogorov-Arnold表示定理（公式2.1），该定理表明任何多元连续函数可以分解为有限个连续单变量函数与加法的组合（p.3-4）。
- **关键模块与数学机制**：
    - **KAN层**：一个具有`n_in`维输入和`n_out`维输出的KAN层，由一个`1D`函数的矩阵 `Φ = {ϕ_{q,p}}` 定义，其中每个`ϕ_{q,p}`是连接第`p`个输入神经元和第`q`个输出神经元的可学习单变量函数（p.5）。输出`x_{l+1}`是所有输入经对应函数处理后的求和：`x_{l+1, j} = Σ_i ϕ_{l, j, i}(x_{l, i})`（公式2.5）。
    - **激活函数参数化**：每条边上的函数`ϕ(x)`被实现为**残差形式**：`ϕ(x) = w_b * b(x) + w_s * spline(x)`（公式2.10）。其中`b(x)`通常取SiLU函数，`spline(x)`由可训练的B样条基函数的线性组合构成（p.6）。这种设计既保留了平滑的优化能力（通过样条），又包含了标准的非线性（通过基函数）。
    - **网络形状**：一个KAN由形状数组 `[n_0, n_1, ..., n_L]` 定义，表示各层的神经元数量（p.5）。原始Kolmogorov-Arnold表示对应一个形状为`[n, 2n+1, 1]`的两层KAN。
    - **与MLP的对比**：MLP将线性变换`W`和固定非线性`σ`分开处理：`MLP(x) = (W_{L-1} ∘ σ ∘ W_{L-2} ∘ σ ∘ ... ∘ W_0)x`（公式2.9）。而KAN将它们整合在一个函数矩阵`Φ`中：`KAN(x) = (Φ_{L-1} ∘ Φ_{L-2} ∘ ... ∘ Φ_0)x`（公式2.7）（p.6）。
- **训练方式**：由于所有操作可微，KAN可以通过**反向传播**进行训练（p.6）。参数初始化有特殊考虑，例如样条部分初始化为近似零（p.6）。在训练过程中，会动态更新样条网格以覆盖激活值的变化范围（p.6）。
- **推理流程**：给定输入`x_0`，依次通过各KAN层的函数矩阵进行变换和求和，最终得到输出（公式2.7）。
- **与已有方法的差异**：与MLP相比，KAN在边（而非节点）上学习非线性，没有传统的线性权重矩阵。与传统样条方法相比，KAN利用了多层结构来学习函数的组合特征，从而能在高维问题中克服维度诅咒（p.2）。

## 6. 实验与结果
- **使用的数据集**：PDF前12页提到了函数拟合任务（如`f(x,y)=exp(sin(x)+y^2)`，见图2.3）和泊松方程求解（p.10），但未提供完整的标准数据集列表。
- **对比方法**：主要与多层感知机（MLP）进行对比（p.1-2, p.8）。
- **评价指标**：主要使用**均方根误差（RMSE）** 作为准确率指标（p.8, 图2.3）。
- **主实验结果**：在提供的文本中，展示了KAN在函数拟合上的优势。例如，在图2.3中，随着网格大小`G`的增加，KAN的测试RMSE下降，并且遵循`~ G^{-4}`的缩放律，这与理论预测的`k+1=4`（对于三次样条）相符（p.8）。文中声称KAN能超越MLP达到更快的缩放律（p.8）。
- **消融/泛化实验**：文本提到了**网格扩展技术**的实验（图2.3），展示了通过增加样条网格点数`G`，KAN的精度可以阶梯式提升。理论部分（定理2.1）也给出了泛化误差的保证（p.7）。
- **效率信息**：参数量方面，一个深度L、宽度N、样条区间数G的KAN，参数量为`O(N^2 L G)`，而同等深度宽度的MLP为`O(N^2 L)`（p.7）。但论文指出KAN通常可以用更小的`N`来达到相同效果，从而节省参数并提高可解释性（p.7）。图2.3右下角显示了训练时间随网格大小`G`的增长情况。

## 7. 这篇论文真正有价值的地方
这篇论文最值得学习的点在于它**重新审视并成功应用了一个经典但曾被认为不实用的数学定理（Kolmogorov-Arnold定理）**，并将其转化为一个具有现代深度学习特性的实用框架。它提供了一种全新的建模视角：**在边（权重）上学习可解释的函数，而不是在节点上学习抽象的特征**。这启发我们思考神经网络架构设计的更多可能性，不一定要局限于“线性变换+固定激活”的范式。此外，论文将准确性、可解释性和理论保证结合起来的研究思路，对于希望推动可信AI和AI for Science的研究者具有重要参考价值。

## 8. 局限与问题
- **计算成本**：KAN的参数量是`O(N^2 L G)`，虽然可以通过更小的`N`弥补，但在需要极大网格`G`或网络非常宽/深时，其计算和内存开销可能仍高于MLP（p.7）。
- **假设依赖**：其理论优势（克服维度诅咒）依赖于目标函数存在平滑的Kolmogorov-Arnold表示这一假设（p.7）。对于不具备这种结构或函数极其不平滑的问题，KAN的优势可能无法体现。
- **实验规模**：从摘要和文中描述看，其优越性主要在“小规模AI + Science任务”上得到验证（p.1）。在更大规模、更通用的任务（如ImageNet分类、大规模语言建模）上的表现未知。
- **优化复杂性**：引入了样条参数化、网格动态更新等机制，可能使优化过程比标准MLP更复杂。
- **复现风险**：虽然提供了代码仓库，但样条相关操作的具体实现细节、超参数设置（如初始化方差σ、网格更新策略）对性能可能敏感。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读**摘要**、**引言**和**图0.1**，即可理解KAN的核心思想、动机和与MLP的关键区别。
- **如果复现**：重点阅读**第2.2节（KAN架构）**，特别是实现细节部分（残差激活函数、初始化、网格更新），并结合开源代码`https://github.com/KindXiaoming/pykan`。
- **如果借鉴创新点**：应学习其将**可学习函数置于边上的核心设计**，以及**网格扩展**这种逐步提升模型精度的技术。思考能否将这种“边激活”的思想应用到现有网络（如CNN、Transformer）的某个模块中。
- **如果写Related Work**：可放在“MLP替代架构”、“可解释神经网络”、“基于样条的神经网络”或“科学机器学习”类别中。

## 10. 和其他论文的关系
- **[[多层感知机（MLP）]]**：KAN是作为MLP的直接替代品提出的。
- **[[样条理论]]**：KAN的核心是用B样条来参数化边上的激活函数。
- **[[Kolmogorov-Arnold表示定理]]**：KAN的理论基础。
- **[[通用逼近定理]]**：MLP的理论基础，与KAN的理论（定理2.1）形成对比。
- **[[Transformer]]**：文中提到MLP是Transformer中消耗参数的主要部分（p.2），KAN可能是一个潜在的替换选择。
- **[[科学发现]]**：KAN被展示用于帮助发现数学和物理定律（p.2）。

## 11. 关键词
KAN， Kolmogorov-Arnold Networks， Kolmogorov-Arnold表示定理， B样条， 可解释性， 神经缩放律， 替代MLP， AI for Science， 函数逼近， 维度诅咒， 网格扩展。

## 12. 可信度说明
本笔记主要基于提供的PDF文本前12页生成，涵盖了摘要、引言、核心方法（第2章前2节）和部分理论。提取质量良好，文本连贯。但需要注意，论文的完整实验部分（第3、4章）、相关工作（第5章）和结论（第6章）的详细信息在提供的文本中缺失，因此“实验与结果”一节内容基于已有的片段进行概括，可能不完整。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/kan.txt` (50/50 页; 原 AI 主体 12/50 + 全文补读 13-50); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-50; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-50。
- **提取情况**: 缺失页 38 页, 其中 38 页提取到可读文本。缺失页包含正文/附录内容, 其中约 7 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: In case the user has no domain knowledge or no idea which symbolic functions these activation
- p.13: In contrast, KANs do continuous search (with gradient descent) in function space, so their results
- p.13: 3 KANs are accurate
- p.13: In this section, we demonstrate that KANs are more effective at representing functions than MLPs
- p.14: Number of parameters107
- p.14: KAN (depth 2)
- p.14: MLP (depth 2)
- p.14: MLP (depth 3)
- p.14: MLP (depth 4)
- p.14: MLP (depth 5)
- p.14: Theory (KAN)
- p.14: Theory (ID)

### 缺失页关键摘录

- p.13: compare both their accuracy (loss) and their complexity (number of parameters). We will show that
- p.14: Theory (ID)Figure 3.1: Compare KANs to MLPs on five toy examples. KANs can almost saturate the fastest scaling law
- p.14: (3)f(x, y) =xy. We know from Figure 4.1 that it can be exactly represented by a [2,2,1]KAN.
- p.14: a function of the number of parameters for KANs and MLPs in Figure 3.1, showing that KANs have
- p.15: Pareto Frontiers than MLPs. The definitions of these special functions are in Table 1.
- p.15: We collect 15 special functions common in math and physics, summarized in Table 1. We choose
- p.15: For each dataset and each model family (KANs or MLPs), we plot the Pareto frontier5, in the
- p.15: (number of parameters, RMSE) plane, shown in Figure 3.2. KANs’ performance is shown to be
- p.15: discovered KANs for special functions in Table 1. On one hand, it is interesting to interpret what
- p.15: these compact representations mean mathematically (we include the KAN illustrations in Figure F.1
- p.15: breaking down a high-dimensional lookup table into several 1D lookup tables, which can potentially
- p.16: Given the structure of the dataset, we may construct KANs by hand, but we are not sure if they are
<!-- AI_READING_NOTE_END -->
