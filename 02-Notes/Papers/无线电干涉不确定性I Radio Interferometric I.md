---
title: MNRAS000,1–16(2017) Preprint12September2018 CompiledusingMNRASLATEXstylefilev3.0
authors:
  - "Xiaohao Cai"
  - "Marcelo Pereyra"
  - "Jason D. McEwen"
year: 2017
venue: "arXiv"
doi: 
pdf: [[无线电干涉不确定性I Radio Interferometric I.pdf]]
primary_topic: N_雷达_无线电_张量_数学
topics:
  - "N_雷达_无线电_张量_数学"
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
extract_cache: .paper-cache/extracts/无线电干涉不确定性I Radio Interferometric I.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/16 pages"
---
# MNRAS000,1–16(2017) Preprint12September2018 CompiledusingMNRASLATEXstylefilev3.0

## 基本信息
- **PDF**: [[无线电干涉不确定性I Radio Interferometric I.pdf]]
- **primary_topic**: `N_雷达_无线电_张量_数学`
- **topics**: `N_雷达_无线电_张量_数学`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | MNRAS000,1–16(2017) Preprint12September2018 CompiledusingMNRASLATEXstylefilev3.0 |
| **作者** | Xiaohao Cai; Marcelo Pereyra; Jason D. McEwen |
| **发表时间** | 2017 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Uncertainty quantification is a critical missing component in radio interferometric imaging that will only become increasingly important as the big-data era of radio interferometry emerges. Since radio interferometric imaging requires solving a high-dimensional, ill-posed inverseproblem,uncertaintyquantificationisdifficultbutalsocriticaltotheaccuratescientific interpretationofradioobservations.StatisticalsamplingapproachestoperformBayesianin- ference,likeMarkovChainMonteCarlo(MCMC)sampling,caninprinciplerecoverthefull posteriordistributionoftheimage,fromwhichuncertaintiescanthenbequantified.However, traditional high-dimensional sampling methods are generally limited to smooth (e.g. Gaus- sian) priors and cannot be used with sparsity-promoting priors. Sparse priors, motivated by thetheoryofcompressivesensing,havebeenshowntobehighlyeffectiveforradiointerfer- ometricimaging.InthisarticleproximalMCMCmethodsaredevelopedforradiointerfero- metricimaging,leveragingproximalcalculustosupportnon-

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：无线电干涉成像是一个**高维、病态的线性逆问题**。从科学解释和决策制定的角度看，对重建图像提供误差估计等不确定性信息至关重要，但现有所有实用成像技术（如CLEAN、MEM、基于压缩感知的方法）都无法提供这种不确定性。
- **之前方法的问题**：
    1.  **传统成像方法**：CLEAN、最大熵法(MEM)等经典方法不提供不确定性信息。
    2.  **现有贝叶斯方法**：一些贝叶斯MCMC采样方法（如Gibbs采样、HMC、MALA）原则上可以从后验分布中提取不确定性。但它们要求先验分布必须是**光滑的（如高斯先验）**，因此**无法与已被证明非常有效的非光滑稀疏先验（如L1范数先验）结合使用**。其他贝叶斯方法（如信息场理论）计算成本过高，且只支持限制性的先验（如对数正态）。
- **核心矛盾**：**高效的图像重建**需要稀疏先验，而**有效的不确定性量化**需要贝叶斯后验采样，但传统贝叶斯采样技术无法处理非光滑的稀疏先验。作者要解决的正是这个“鱼与熊掌”的矛盾。
## 关键贡献

1.  **提出近端MCMC算法**：首次将近端微积分引入无线电干涉成像的贝叶斯推理中，提出了**Px-MALA（近端Metropolis-adjusted Langevin算法）**和**MYULA（Moreau-Yosida ULA）**两种算法。这两种算法是ULA和MALA的直接扩展，能够对包含非光滑稀疏先验的高维后验分布进行采样。
2.  **构建不确定性量化框架**：基于恢复的后验分布，开发了三种具体的不确定性量化策略：
    - **(i) 局部（逐像素）可信区间**：为每个像素提供误差范围。
    - **(ii) 最高后验密度(HPD)可信区域**：标识出图像中高概率包含真实信号的区域。
    - **(iii) 基于HPD区域的图像结构假设检验**：对图像中特定结构（如源的存在）进行统计检验。
3.  **比较分析模型与合成模型**：在贝叶斯框架下，系统地比较了采用分析先验（直接对图像施加先验）和合成先验（对表示系数施加先验）两种建模方式在成像和不确定性量化中的性能。
4.  **算法特性分析**：明确指出Px-MALA通过引入Metropolis-Hastings接受-拒绝步骤来保证采样准确性（无偏），但计算开销大；而MYULA通过引入可控的近似消除了该步骤，计算开销更低，但引入了有偏性（偏差可被控制得任意小）。
## 方法

**整体框架**：论文提出的方法是一个完整的**贝叶斯后验推理流程**，包括建模、采样和不确定性评估三步。
1.  **建模（输入输出）**：
    - **输入**：测量的可见度数据 `y ∈ ℂ^M`，线性测量算子 `Φ`，噪声标准差 `σ`。
    - **输出**：未知的天空图像 `x ∈ ℝ^N`，以及关于 `x` 的不确定性信息。
    - **核心公式**：构建后验分布。以**分析模型**为例，其未归一化后验为：
      `p(x|y) ∝ exp{ - ( λ∥Ψ†x∥₁ + ∥y - Φx∥²₂ / (2σ²)) }`
      其中，第一项是L1范数先验，鼓励图像在字典 `Ψ†` 下稀疏；第二项是高斯似然项。合成模型类似，但先验施加在系数 `a` 上。
2.  **关键模块：近端MCMC采样器**：
    - **Px-MALA**：这是标准MALA算法的推广。它在朗之万动力学的梯度步中，引入了**近端算子**来处理后验分布中的非光滑L1项。近端算子在每一步对非光滑部分进行“软阈值”或“收缩”操作，从而允许算法探索由稀疏先验定义的非光滑空间。为了保证收敛到正确的目标后验，它包含了Metropolis-Hastings接受-拒绝步骤。
    - **MYULA**：这是标准ULA算法的推广。它使用**Moreau-Yosida包络**对非光滑的先验项进行一个光滑近似，从而可以直接应用梯度信息。它省去了Px-MALA中的MH步骤，因此每迭代一步的计算量更小，但引入了一个可控的近似误差。
    - **直观解释**：想象一个崎岖不平（非光滑，有L1尖峰）的能量地形图。传统MCMC（如HMC）只能在一个光滑的近似地形上探索。Px-MALA和MYULA则装备了“近端导航仪”，能够更精确地在原始的崎岖地形上行走和采样。
3.  **模块连接与流程**：
    - 首先，选择分析或合成模型，并确定稀疏字典 `Ψ` 和正则化参数 `λ`。
    - 然后，使用Px-MALA或MYULA算法，从初始点出发，通过迭代更新图像 `x`（或系数 `a`），生成一个马尔可夫链。链上的样本被认为近似来自目标后验分布。
    - 最后，**推理流程**：当马尔可夫链收敛后（经过“老化”期），从链中收集大量样本，用这些样本来估计后验均值（点估计）和计算各种不确定性度量（如逐像素方差、HPD区域）。
4.  **与已有方法的差异**：
    - **与传统MAP估计（如基于L1的优化）**：MAP只给出一个最优点估计，而本文方法给出一个样本集合，包含了完整的不确定性信息。
    - **与传统光滑先验的MCMC（如高斯先验的HMC）**：本文方法**能够处理非光滑的L1稀疏先验**，而后者不能。
    - **与CLEAN/MEM**：本文提供严格的统计不确定性框架，而CLEAN/MEM不提供。
## 实验

PDF文本中**仅包含论文的前12页，未包含第6节“数值结果”的具体内容**。
- **使用数据集**：PDF文本中未明确说明。
- **对比方法**：PDF文本中未明确说明。
- **评价指标**：PDF文本中未明确说明。
- **主实验结果**：PDF文本中未明确说明。
- **消融实验**：PDF文本中未明确说明。
- **泛化实验**：PDF文本中未明确说明。
- **速度/参数量/FLOPs等效率信息**：在方法描述中，作者定性指出Px-MALA计算开销高于MYULA，但未提供具体数值。
## 局限

1.  **计算成本**：尽管MYULA降低了开销，但MCMC采样本质上仍然非常耗时，尤其对于高分辨率成像。论文提到其扩展性将在 companion article 中讨论，但本文本身未解决大数据规模下的效率问题。
2.  **近似与偏差**：MYULA方法引入了有偏近似，虽然偏差可被控制，但相比Px-MALA的无偏性，这可能在某些对精度要求极高的科学分析中是一个顾虑。
3.  **模型假设**：采用了高斯噪声和线性测量模型的简化假设。真实观测中可能存在非高斯噪声、校准误差等，方法的鲁棒性有待进一步验证。
4.  **先验选择**：论文聚焦于L1范数稀疏先验。虽然这是主流，但其他类型的先验（如全变分先验）是否也能便捷地整合到该近端框架中，未在本文中展开。
## 个人评论

1.  **思想启发**：论文最核心的贡献是展示了如何将**优化领域的“近端算子”技巧**成功引入到**贝叶斯统计的MCMC采样**中，以解决非光滑先验下的采样难题。这是一个非常漂亮且具有启发性的跨领域融合思路，可以推广到其他需要处理非光滑先验或约束的贝叶斯推理问题中。
2.  **框架完整性**：论文不仅提出了新的采样算法，还系统性地构建了从采样结果中提取实用不确定性信息（误差棒、可信区域、假设检验）的框架，使得统计理论真正落地到具体的成像应用中。
3.  **问题选择精准**：准确地指出了当前无线电干涉成像领域从“追求高质量重建”走向“可信定量分析”所面临的核心瓶颈——不确定性量化缺失，并给出了一个理论上严谨、方法上可行的解决方案。

### 使用建议

- **如果快速了解**：只阅读 **摘要（Abstract）**、**引言（Introduction）的前两段和最后两段**，以及**结论（Conclusion）**。可以快速把握问题背景、核心矛盾和主要贡献。
- **如果复现**：重点精读 **第3节（贝叶斯推理的近端MCMC）** 和 **第4节（用于RI成像的近端MCMC）**。需要仔细推导算法中近端算子的具体形式以及MH接受率的计算，并理解分析模型与合成模型在代码实现上的区别。
- **如果借鉴创新点**：应该学习 **近端MCMC的整体框架**（第3节），理解如何将一个非光滑的目标分布通过Moreau-Yosida包络或近端步骤转化为可采样的形式。不确定性量化策略的构建思路（第5节）也值得借鉴。
- **如果写related work**：可将其放在 **“贝叶斯成像与不确定性量化”** 或 **“非光滑优化在统计计算中的应用”** 相关部分，与使用光滑先验的MCMC方法、其他贝叶斯成像算法（如信息场理论）以及压缩感知理论进行对比引用。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[N_雷达_无线电_张量_数学]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**无线电天文成像与贝叶斯统计计算交叉领域**的研究。它旨在解决无线电干涉(RI)成像中一个长期缺失的关键问题：如何对重建图像进行可靠的**不确定性量化**。具体而言，论文针对传统贝叶斯MCMC采样方法无法处理在RI成像中非常有效的非光滑（如L1范数）稀疏先验这一局限，提出了新的近端MCMC采样算法。因此，本研究适合放在“**贝叶斯成像与不确定性量化**”或“**天文信号处理中的先进统计方法**”主题下。

## 2. 一句话总结
本文提出了**近端MCMC方法（Px-MALA和MYULA）**，首次在支持非光滑稀疏先验的贝叶斯框架下，实现了无线电干涉成像的完整后验分布采样，并基于此开发了多种实用的不确定性量化策略。

## 3. 背景与问题
- **为什么要做**：无线电干涉成像是一个**高维、病态的线性逆问题**。从科学解释和决策制定的角度看，对重建图像提供误差估计等不确定性信息至关重要，但现有所有实用成像技术（如CLEAN、MEM、基于压缩感知的方法）都无法提供这种不确定性。
- **之前方法的问题**：
    1.  **传统成像方法**：CLEAN、最大熵法(MEM)等经典方法不提供不确定性信息。
    2.  **现有贝叶斯方法**：一些贝叶斯MCMC采样方法（如Gibbs采样、HMC、MALA）原则上可以从后验分布中提取不确定性。但它们要求先验分布必须是**光滑的（如高斯先验）**，因此**无法与已被证明非常有效的非光滑稀疏先验（如L1范数先验）结合使用**。其他贝叶斯方法（如信息场理论）计算成本过高，且只支持限制性的先验（如对数正态）。
- **核心矛盾**：**高效的图像重建**需要稀疏先验，而**有效的不确定性量化**需要贝叶斯后验采样，但传统贝叶斯采样技术无法处理非光滑的稀疏先验。作者要解决的正是这个“鱼与熊掌”的矛盾。

## 4. 核心贡献
1.  **提出近端MCMC算法**：首次将近端微积分引入无线电干涉成像的贝叶斯推理中，提出了**Px-MALA（近端Metropolis-adjusted Langevin算法）**和**MYULA（Moreau-Yosida ULA）**两种算法。这两种算法是ULA和MALA的直接扩展，能够对包含非光滑稀疏先验的高维后验分布进行采样。
2.  **构建不确定性量化框架**：基于恢复的后验分布，开发了三种具体的不确定性量化策略：
    - **(i) 局部（逐像素）可信区间**：为每个像素提供误差范围。
    - **(ii) 最高后验密度(HPD)可信区域**：标识出图像中高概率包含真实信号的区域。
    - **(iii) 基于HPD区域的图像结构假设检验**：对图像中特定结构（如源的存在）进行统计检验。
3.  **比较分析模型与合成模型**：在贝叶斯框架下，系统地比较了采用分析先验（直接对图像施加先验）和合成先验（对表示系数施加先验）两种建模方式在成像和不确定性量化中的性能。
4.  **算法特性分析**：明确指出Px-MALA通过引入Metropolis-Hastings接受-拒绝步骤来保证采样准确性（无偏），但计算开销大；而MYULA通过引入可控的近似消除了该步骤，计算开销更低，但引入了有偏性（偏差可被控制得任意小）。

## 5. 方法详解
**整体框架**：论文提出的方法是一个完整的**贝叶斯后验推理流程**，包括建模、采样和不确定性评估三步。
1.  **建模（输入输出）**：
    - **输入**：测量的可见度数据 `y ∈ ℂ^M`，线性测量算子 `Φ`，噪声标准差 `σ`。
    - **输出**：未知的天空图像 `x ∈ ℝ^N`，以及关于 `x` 的不确定性信息。
    - **核心公式**：构建后验分布。以**分析模型**为例，其未归一化后验为：
      `p(x|y) ∝ exp{ - ( λ∥Ψ†x∥₁ + ∥y - Φx∥²₂ / (2σ²)) }`
      其中，第一项是L1范数先验，鼓励图像在字典 `Ψ†` 下稀疏；第二项是高斯似然项。合成模型类似，但先验施加在系数 `a` 上。
2.  **关键模块：近端MCMC采样器**：
    - **Px-MALA**：这是标准MALA算法的推广。它在朗之万动力学的梯度步中，引入了**近端算子**来处理后验分布中的非光滑L1项。近端算子在每一步对非光滑部分进行“软阈值”或“收缩”操作，从而允许算法探索由稀疏先验定义的非光滑空间。为了保证收敛到正确的目标后验，它包含了Metropolis-Hastings接受-拒绝步骤。
    - **MYULA**：这是标准ULA算法的推广。它使用**Moreau-Yosida包络**对非光滑的先验项进行一个光滑近似，从而可以直接应用梯度信息。它省去了Px-MALA中的MH步骤，因此每迭代一步的计算量更小，但引入了一个可控的近似误差。
    - **直观解释**：想象一个崎岖不平（非光滑，有L1尖峰）的能量地形图。传统MCMC（如HMC）只能在一个光滑的近似地形上探索。Px-MALA和MYULA则装备了“近端导航仪”，能够更精确地在原始的崎岖地形上行走和采样。
3.  **模块连接与流程**：
    - 首先，选择分析或合成模型，并确定稀疏字典 `Ψ` 和正则化参数 `λ`。
    - 然后，使用Px-MALA或MYULA算法，从初始点出发，通过迭代更新图像 `x`（或系数 `a`），生成一个马尔可夫链。链上的样本被认为近似来自目标后验分布。
    - 最后，**推理流程**：当马尔可夫链收敛后（经过“老化”期），从链中收集大量样本，用这些样本来估计后验均值（点估计）和计算各种不确定性度量（如逐像素方差、HPD区域）。
4.  **与已有方法的差异**：
    - **与传统MAP估计（如基于L1的优化）**：MAP只给出一个最优点估计，而本文方法给出一个样本集合，包含了完整的不确定性信息。
    - **与传统光滑先验的MCMC（如高斯先验的HMC）**：本文方法**能够处理非光滑的L1稀疏先验**，而后者不能。
    - **与CLEAN/MEM**：本文提供严格的统计不确定性框架，而CLEAN/MEM不提供。

## 6. 实验与结果
PDF文本中**仅包含论文的前12页，未包含第6节“数值结果”的具体内容**。
- **使用数据集**：PDF文本中未明确说明。
- **对比方法**：PDF文本中未明确说明。
- **评价指标**：PDF文本中未明确说明。
- **主实验结果**：PDF文本中未明确说明。
- **消融实验**：PDF文本中未明确说明。
- **泛化实验**：PDF文本中未明确说明。
- **速度/参数量/FLOPs等效率信息**：在方法描述中，作者定性指出Px-MALA计算开销高于MYULA，但未提供具体数值。

## 7. 这篇论文真正有价值的地方
1.  **思想启发**：论文最核心的贡献是展示了如何将**优化领域的“近端算子”技巧**成功引入到**贝叶斯统计的MCMC采样**中，以解决非光滑先验下的采样难题。这是一个非常漂亮且具有启发性的跨领域融合思路，可以推广到其他需要处理非光滑先验或约束的贝叶斯推理问题中。
2.  **框架完整性**：论文不仅提出了新的采样算法，还系统性地构建了从采样结果中提取实用不确定性信息（误差棒、可信区域、假设检验）的框架，使得统计理论真正落地到具体的成像应用中。
3.  **问题选择精准**：准确地指出了当前无线电干涉成像领域从“追求高质量重建”走向“可信定量分析”所面临的核心瓶颈——不确定性量化缺失，并给出了一个理论上严谨、方法上可行的解决方案。

## 8. 局限与问题
1.  **计算成本**：尽管MYULA降低了开销，但MCMC采样本质上仍然非常耗时，尤其对于高分辨率成像。论文提到其扩展性将在 companion article 中讨论，但本文本身未解决大数据规模下的效率问题。
2.  **近似与偏差**：MYULA方法引入了有偏近似，虽然偏差可被控制，但相比Px-MALA的无偏性，这可能在某些对精度要求极高的科学分析中是一个顾虑。
3.  **模型假设**：采用了高斯噪声和线性测量模型的简化假设。真实观测中可能存在非高斯噪声、校准误差等，方法的鲁棒性有待进一步验证。
4.  **先验选择**：论文聚焦于L1范数稀疏先验。虽然这是主流，但其他类型的先验（如全变分先验）是否也能便捷地整合到该近端框架中，未在本文中展开。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只阅读 **摘要（Abstract）**、**引言（Introduction）的前两段和最后两段**，以及**结论（Conclusion）**。可以快速把握问题背景、核心矛盾和主要贡献。
- **如果复现**：重点精读 **第3节（贝叶斯推理的近端MCMC）** 和 **第4节（用于RI成像的近端MCMC）**。需要仔细推导算法中近端算子的具体形式以及MH接受率的计算，并理解分析模型与合成模型在代码实现上的区别。
- **如果借鉴创新点**：应该学习 **近端MCMC的整体框架**（第3节），理解如何将一个非光滑的目标分布通过Moreau-Yosida包络或近端步骤转化为可采样的形式。不确定性量化策略的构建思路（第5节）也值得借鉴。
- **如果写related work**：可将其放在 **“贝叶斯成像与不确定性量化”** 或 **“非光滑优化在统计计算中的应用”** 相关部分，与使用光滑先验的MCMC方法、其他贝叶斯成像算法（如信息场理论）以及压缩感知理论进行对比引用。

## 10. 和其他论文的关系
根据主题 `N_雷达_无线电_张量_数学`，本文可能与以下方向的研究相关：
- [[无线电干涉成像中的其他贝叶斯方法]]， 如使用信息场理论或高斯过程先验的工作。
- [[稀疏信号恢复的压缩感知理论]]， 作为稀疏先验的理论基础。
- [[近端算法与MCMC采样]]， 如Pereyra等其他关于近端MCMC的理论工作。
- [[大规模天文数据处理方法]]， 如文中提及的SKA大数据挑战。

## 11. 关键词
不确定性量化, 无线电干涉成像, 贝叶斯推理, MCMC采样, 近端算法, 稀疏先验, L1正则化, 后验分布, 可信区间, 最高后验密度, 假设检验

## 12. 可信度说明
本精读笔记**主要基于提供的PDF文本前12页内容生成**，重点涵盖了摘要、引言、方法（第2、3、4节）和部分实验设定描述。由于**第6节“数值结果”及后续章节未包含在提供的提取文本中**，因此关于具体实验设置、数据集、对比方法和量化结果的部分（第6节）标注为“PDF文本中未明确说明”。提取的文本质量良好，逻辑清晰，足以支撑对论文动机、核心思想和方法论框架的理解。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/无线电干涉不确定性I Radio Interferometric I.txt` (16/16 页; 原 AI 主体 12/16 + 全文补读 13-16); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-16; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-16。
- **提取情况**: 缺失页 4 页, 其中 4 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Cygnus A
- p.13: This is due to the fact that the posterior median is closer to the
- p.13: result. Therefore, we recommend using the median sample for test-
- p.13: MCMC sampling by MYULA, provides a powerful framework to
- p.13: To conclude, we emphasise again that the standard methods
- p.13: RI imaging that will only become increasingly important as the
- p.13: We formulate the RI imaging problem in a Bayesian frame-
- p.14: 14 Cai, Pereyra and McEwen
- p.14: Px-MALA 2:44 2:34 2:43 2:34 3
- p.14: Px-MALA 1:17 1:26 1:18 1:27 7
- p.14: Px-MALA 3:38 1:84 3:37 1:85 3
- p.14: Px-MALA 3:27 2:02 3:25 2:01 3

### 缺失页关键摘录

- p.13: Figure 5. Length of pixel-wise credible intervals (95% credible level). First to fourth rows are results for the images M31, Cygnus A, W28, and 3C288,
- p.13: to those recovered by Px-MALA. See further discussion in main text.
- p.13: physical. The only difference between Table 2 and Table 3 is the re-
- p.13: result. Therefore, we recommend using the median sample for test-
- p.14: Figure 6. HPD credible region isocontour levels
- p.14: Table 2. Hypothesis test results for test structures shown in Figure 7 for M31, Cygnus A, W28, and 3C288. Note that
- p.14: Table 3. Same as Table 2 but based on the sample median instead of the sample mean (the mean is considered for Table 2). This table shows that hypothesis
- p.15: Figure 7. Hypothesis testing for M31, Cygnus A, W28, and 3C288. The
- p.15: Results of these hypothesis tests are speciﬁed in Table 2 and Table 3. Note
- p.15: be computed and uncertainty information regarding the accuracy
<!-- AI_READING_NOTE_END -->
