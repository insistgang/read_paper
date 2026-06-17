---
title: "DexinDuan* PeilinLiu* BingweiHui† FeiWen*‡"
authors:
  - "Dexin Duan"
  - "Peilin Liu"
  - "Bingwei Hui"
  - "Fei Wen"
year: 2024
venue: BRAIN-INSPIRED ONLINE ADAPTATION FOR REMOTE SENSING
doi: 
pdf: [[2024_Brain-Inspired_Onlin.pdf]]
primary_topic: G_视觉基础模型_VLM_LLM
topics:
  - "G_视觉基础模型_VLM_LLM"
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
extract_cache: .paper-cache/extracts/2024_Brain-Inspired_Onlin.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/22 pages"
---
# DexinDuan* PeilinLiu* BingweiHui† FeiWen*‡

## 基本信息
- **PDF**: [[2024_Brain-Inspired_Onlin.pdf]]
- **primary_topic**: `G_视觉基础模型_VLM_LLM`
- **topics**: `G_视觉基础模型_VLM_LLM`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | DexinDuan* PeilinLiu* BingweiHui† FeiWen*‡ |
| **作者** | Dexin Duan; Peilin Liu; Bingwei Hui; Fei Wen |
| **发表时间** | 2024 |
| **刊物/会议** | BRAIN-INSPIRED ONLINE ADAPTATION FOR REMOTE SENSING |
| **DOI** | 未明确 |

## 摘要

> On-devicecomputing,oredgecomputing,isbecomingincreasinglyimportantforremotesensing, particularlyinapplicationslikedeepnetwork-basedperceptiononon-orbitsatellitesandunmanned aerialvehicles(UAVs). Inthesescenarios,twobrain-likecapabilitiesarecrucialforremotesensing models: (1) high energy efficiency, allowing the model to operate on edge devices with limited computingresources,and(2)onlineadaptation,enablingthemodeltoquicklyadapttoenvironmental variations,weatherchanges,andsensordrift. Thisworkaddressestheseneedsbyproposinganonline adaptationframeworkbasedonspikingneuralnetworks(SNNs)forremotesensing. Startingwith apretrainedSNNmodel,wedesignanefficient,unsupervisedonlineadaptationalgorithm,which adoptsanapproximationoftheBPTTalgorithmandonlyinvolvesforward-in-timecomputationthat significantlyreducesthecomputationalcomplexityofSNNadaptationlearning. Besides,wepropose anadaptiveactivationscalingschemetoboostonlineSNNadaptationperformance,particularlyin lowtime-steps. Furthermore,forthemor

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：深度学习模型在遥感领域表现优异，但模型日益庞大，在资源受限的边缘设备（如在轨卫星、UAV）上部署时面临巨大挑战。用户希望模型具备两种“类脑”能力：1) **高能效**，以适应有限的计算资源；2) **在线适应能力**，能快速适应多变的环境（如天气、传感器漂移）。SNN因其事件驱动的脉冲编码机制而具有高能效潜力，但其在线适应能力未被探索。
- **之前方法有什么问题**：现有深度网络的跨域适应方法（如对抗域适应、特征对齐）通常**严重依赖带标签样本**，或者需要**多轮训练/微调**，这在实际的边缘设备在线部署场景中不切实际。同时，传统深度神经网络（ANN）的高能耗问题依然是部署障碍。
- **作者想解决的核心矛盾**：如何**将SNN的高能效优势与快速在线适应能力结合起来**，设计出一个计算高效、无需标签数据的SNN在线适应框架，以满足边缘设备实时遥感感知的需求。
## 关键贡献

1.  **提出了首个SNN在线适应框架**：针对遥感任务，设计了一个从预训练SNN模型出发的高效、无监督在线适应算法。该算法通过**近似BPTT（时间反向传播）算法**，实现仅需前向时间计算的优化，显著降低了SNN适应学习的计算复杂度。
2.  **设计了自适应激活缩放方案**：提出了一个动态控制SNN模型激活范围的机制，该方案在适应学习过程中能有效提升SNN性能，**尤其是在较低的时间步（time-steps）下效果显著**。
3.  **设计了基于置信度的实例加权方案**：针对更具挑战性的遥感目标检测任务，提出了一个通过选择高置信度实例进行模型更新的加权策略，**显著提升了在检测任务上的适应性能**。
4.  **在多个基准上进行了全面评估**：在涵盖分类、分割和检测的**七个数据集**上（RSSCN, WHU-RS19, AID, DLRSD, WHDLD, RSOD, LEVIR）进行了实验，证明所提方法在不同天气条件下显著优于现有的域适应和域泛化方法。
## 方法

- **整体框架**：如图1所示。框架以一个预训练的SNN模型（主要通过ANN-SNN转换得到）为起点。在测试阶段，当输入数据（如带有天气干扰的遥感图像）与源域存在分布偏移时，模型利用**无监督损失**（如预测熵）对未标记的测试数据进行在线适应更新，以提升模型在目标域（测试场景）的性能。
- **输入输出**：输入是未标记的目标域测试数据（如不同天气下的遥感图像）。输出是适应后的SNN模型，以及模型在该测试数据上的预测结果。
- **关键模块**：
    1.  **脉冲神经元模型与BPTT**：论文采用IF（积分触发）神经元模型。标准的BPTT训练SNN需要存储所有时间步的计算图进行反向传播，计算和内存成本随时间步T线性增长，不利于边缘设备。
    2.  **ANN-SNN转换**：为了利用现有ANN模型，论文采用ANN-SNN转换方法（如ReLU到IF神经元的权重映射）作为预训练SNN的来源。
    3.  **自适应激活缩放**：这是解决SNN适应性能瓶颈的关键。观察发现，跨域适应时，SNN的脉冲发放率（firing rate）分布会向低值偏移并变得不均匀，损害模型表达能力。为此，论文为每一层引入一个可学习的**裁剪参数αl**，在前向传播时对神经元激活进行裁剪（`a_l = max(a_l, α_l)`）。优化α_l（通过包含L2正则化的联合损失）可以自适应地调整激活范围，使脉冲发放率分布更均匀（如图2d所示），从而提升适应效果，尤其在时间步较少时。
    4.  **基于置信度的实例加权**：针对检测任务，模型对不同实例的预测置信度不同。该方案赋予高置信度的预测结果更高的权重用于计算适应损失，从而抑制低质量或不确定预测对模型更新的干扰，提升检测任务的适应鲁棒性。
    5.  **无监督在线适应学习算法**：使用预测熵 `L_e(ŷ) = -∑ p(ŷ) log p(ŷ)` 作为无监督损失。核心创新在于提出了一种**前向时间优化算法**来近似BPTT。该算法解耦了时间梯度，使得梯度计算和参数更新可以在时间上前进时完成，无需存储和回溯整个时间计算图，**将计算复杂度从O(T)降低**，使其适合在线实时更新。
- **模块连接**：预训练SNN -> 接收未标记测试数据 -> 进行前向传播（使用自适应激活缩放） -> 计算基于熵的损失（对检测任务使用实例加权） -> 使用前向时间优化算法计算梯度 -> 更新模型参数（包括权重和缩放参数α） -> 输出适应后的模型。
- **训练方式**：在线、无监督、单次前向传播式更新。对于每个测试样本（或批次），模型立即计算损失并更新，而无需等待所有数据。
- **推理流程**：标准的SNN前向传播流程。输入数据被编码为脉冲序列，经过多层IF神经元处理，在多个时间步后累积输出膜电位，用于最终决策。
- **和已有方法的差异**：与传统ANN域适应方法（如对抗训练、特征对齐）相比，本方法**无需源数据、无需标签、无需多轮训练**，是面向SNN架构的轻量化在线方案。与标准SNN训练（BPTT）相比，本方法通过前向时间优化和自适应缩放，实现了计算高效且性能更优的在线适应。
## 实验

- **使用的数据集**：七个基准数据集，涵盖三大任务：
    - 分类：RSSCN, WHU-RS19, AID
    - 语义分割：DLRSD, WHDLD
    - 目标检测：RSOD, LEVIR
- **对比方法**：文中提到与“representative ANN adaptation methods”以及“existing domain adaptation and domain generalization approaches”进行对比。具体方法名称在提供的文本中未完整列出，但应包括如Tent等TTA方法及一些传统域适应方法。
- **评价指标**：分类任务使用准确率（Accuracy），分割任务使用平均交并比（mIoU），检测任务使用平均精度均值（mAP）。
- **主实验结果**：摘要中明确提到，在“varying weather conditions”下，所提方法“**significantly outperforms existing domain adaptation and domain generalization approaches**”。虽然提供的文本未包含完整的实验结果表格，但论文通过大量实验证明了其有效性。
- **消融实验**：论文进行了“ablation study”，用于验证自适应激活缩放、实例加权等各个模块的贡献。图2的分布图可视为对自适应激活缩放模块效果的定性消融分析。
- **泛化实验**：实验设置本身就是在评估模型从源域（如晴朗天气）泛化到不同目标域（如多云、雾天等）的能力。
- **效率信息**：论文核心贡献之一就是提升能效。通过前向时间优化，**显著降低了适应学习的计算复杂度**。第4节将进行“energy efficiency analysis”，但具体数据（如FLOPs、能耗对比）在提供的文本中未找到。
## 局限

- **任务覆盖与模型通用性**：论文主要实验基于通过ANN-SNN转换得到的SNN模型。虽然文中提及方法可直接用于训练好的SNN，但其在直接训练的、更复杂或更深的SNN模型上的效果有待进一步验证。
- **计算效率的实际表现**：论文强调了算法在复杂度上的优势，但提供的文本中缺少具体的能耗、运行时间或FLOPs对比数据，使得能效提升的量化程度不够清晰。
- **数据集与场景局限**：实验集中在遥感领域的特定数据集上，且主要应对天气变化。方法在更复杂的环境变化（如季节、光照、传感器类型剧变）或更复杂的任务（如实例分割、图像生成）上的泛化能力未知。
- **假设与依赖**：在线适应依赖于每个测试样本都能提供有效的梯度信息（通过熵损失）。如果测试数据噪声极大或熵损失无效，适应过程可能失效。此外，预训练SNN模型的质量是基础。
- **复现风险**：论文提出的优化算法（前向时间优化）是对BPTT的近似，其稳定性和最优性可能需要仔细调节超参数。自适应缩放参数的更新也与主网络权重更新耦合，优化过程可能需要精心设计。
## 个人评论

1.  **开创性研究方向**：这是**首次**系统性地研究SNN的在线适应问题，开辟了“高效在线神经形态感知”这一新的研究方向，对后续研究有奠基意义。
2.  **针对SNN特性的精巧设计**：论文深刻理解了SNN脉冲发放率分布对其性能的影响，并据此提出了**自适应激活缩放**这一简单而有效的机制。这个设计直接针对SNN的“量化”特性，是ANN域适应方法中没有的，体现了对问题本质的洞察。
3.  **实用性与部署友好**：整个框架的设计都围绕“边缘设备在线部署”这一实用目标。前向时间优化算法和无监督学习范式，使其非常适合在资源受限的平台上运行。这为将神经形态计算真正推向实际遥感应用提供了可行的技术路径。
4.  **对后续研究的启发**：SNN如何高效地进行无监督/自监督学习是一个广阔领域。本文的前向时间优化思路可以启发SNN在其他在线学习任务中的算法设计。自适应缩放的思想也可能推广到其他需要调整脉冲网络动态范围的场景。

### 使用建议

- **如果快速了解**：只读 **Abstract**、**1 Introduction**（尤其是最后贡献总结）、**2.3 Adaptive Activation Scaling** 和 **2.4 Unsupervised Online Adaptation Learning** 的前几段，以及 **Figure 1** 和 **Figure 2**。
- **如果复现**：重点阅读 **2 Methodology** 全部，特别是 **2.1** 的SNN基础、**2.3** 和 **2.4** 中具体的算法步骤和公式（如公式10, 11, 12）。需要关注自适应缩放参数α的初始化和优化细节，以及前向时间优化梯度计算的实现方式。
- **如果借鉴创新点**：应学习其 **“针对SNN动态特性设计专用机制”** 的研究思路（如自适应缩放）。其 **“将在线学习问题转化为前向传播优化”** 的算法设计思路也极具启发性。此外，**“基于置信度的加权”** 是解决任务特定问题的通用技巧。
- **如果写 related work**：可放在 **“神经形态计算/SNN在视觉任务中的应用”**、**“测试时域适应/在线无监督学习”**、**“遥感图像处理中的域适应与泛化”** 这几个子类下。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[G_视觉基础模型_VLM_LLM]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于神经形态计算（脑启发计算）与遥感图像处理的交叉领域。它主要解决边缘计算场景下（如在轨卫星、无人机）遥感感知模型面临的两个核心挑战：高能耗和缺乏快速在线适应能力。本文聚焦于利用脉冲神经网络（SNN）的低能耗特性，并为其设计首个在线适应框架，使其能快速适应环境变化、天气影响和传感器漂移。因此，该论文适合放在“G_视觉基础模型_VLM_LLM”主题下，具体涉及利用新型神经网络架构（SNN）进行视觉任务的在线学习和部署。

## 2. 一句话总结
本文提出了首个面向遥感应用的脉冲神经网络（SNN）在线无监督适应框架，通过设计前向时间优化算法、自适应激活缩放机制和基于置信度的实例加权方案，使SNN模型能在边缘设备上以高能效方式快速适应变化的环境和天气条件。

## 3. 背景与问题
- **这篇论文为什么要做**：深度学习模型在遥感领域表现优异，但模型日益庞大，在资源受限的边缘设备（如在轨卫星、UAV）上部署时面临巨大挑战。用户希望模型具备两种“类脑”能力：1) **高能效**，以适应有限的计算资源；2) **在线适应能力**，能快速适应多变的环境（如天气、传感器漂移）。SNN因其事件驱动的脉冲编码机制而具有高能效潜力，但其在线适应能力未被探索。
- **之前方法有什么问题**：现有深度网络的跨域适应方法（如对抗域适应、特征对齐）通常**严重依赖带标签样本**，或者需要**多轮训练/微调**，这在实际的边缘设备在线部署场景中不切实际。同时，传统深度神经网络（ANN）的高能耗问题依然是部署障碍。
- **作者想解决的核心矛盾**：如何**将SNN的高能效优势与快速在线适应能力结合起来**，设计出一个计算高效、无需标签数据的SNN在线适应框架，以满足边缘设备实时遥感感知的需求。

## 4. 核心贡献
1.  **提出了首个SNN在线适应框架**：针对遥感任务，设计了一个从预训练SNN模型出发的高效、无监督在线适应算法。该算法通过**近似BPTT（时间反向传播）算法**，实现仅需前向时间计算的优化，显著降低了SNN适应学习的计算复杂度。
2.  **设计了自适应激活缩放方案**：提出了一个动态控制SNN模型激活范围的机制，该方案在适应学习过程中能有效提升SNN性能，**尤其是在较低的时间步（time-steps）下效果显著**。
3.  **设计了基于置信度的实例加权方案**：针对更具挑战性的遥感目标检测任务，提出了一个通过选择高置信度实例进行模型更新的加权策略，**显著提升了在检测任务上的适应性能**。
4.  **在多个基准上进行了全面评估**：在涵盖分类、分割和检测的**七个数据集**上（RSSCN, WHU-RS19, AID, DLRSD, WHDLD, RSOD, LEVIR）进行了实验，证明所提方法在不同天气条件下显著优于现有的域适应和域泛化方法。

## 5. 方法详解
- **整体框架**：如图1所示。框架以一个预训练的SNN模型（主要通过ANN-SNN转换得到）为起点。在测试阶段，当输入数据（如带有天气干扰的遥感图像）与源域存在分布偏移时，模型利用**无监督损失**（如预测熵）对未标记的测试数据进行在线适应更新，以提升模型在目标域（测试场景）的性能。
- **输入输出**：输入是未标记的目标域测试数据（如不同天气下的遥感图像）。输出是适应后的SNN模型，以及模型在该测试数据上的预测结果。
- **关键模块**：
    1.  **脉冲神经元模型与BPTT**：论文采用IF（积分触发）神经元模型。标准的BPTT训练SNN需要存储所有时间步的计算图进行反向传播，计算和内存成本随时间步T线性增长，不利于边缘设备。
    2.  **ANN-SNN转换**：为了利用现有ANN模型，论文采用ANN-SNN转换方法（如ReLU到IF神经元的权重映射）作为预训练SNN的来源。
    3.  **自适应激活缩放**：这是解决SNN适应性能瓶颈的关键。观察发现，跨域适应时，SNN的脉冲发放率（firing rate）分布会向低值偏移并变得不均匀，损害模型表达能力。为此，论文为每一层引入一个可学习的**裁剪参数αl**，在前向传播时对神经元激活进行裁剪（`a_l = max(a_l, α_l)`）。优化α_l（通过包含L2正则化的联合损失）可以自适应地调整激活范围，使脉冲发放率分布更均匀（如图2d所示），从而提升适应效果，尤其在时间步较少时。
    4.  **基于置信度的实例加权**：针对检测任务，模型对不同实例的预测置信度不同。该方案赋予高置信度的预测结果更高的权重用于计算适应损失，从而抑制低质量或不确定预测对模型更新的干扰，提升检测任务的适应鲁棒性。
    5.  **无监督在线适应学习算法**：使用预测熵 `L_e(ŷ) = -∑ p(ŷ) log p(ŷ)` 作为无监督损失。核心创新在于提出了一种**前向时间优化算法**来近似BPTT。该算法解耦了时间梯度，使得梯度计算和参数更新可以在时间上前进时完成，无需存储和回溯整个时间计算图，**将计算复杂度从O(T)降低**，使其适合在线实时更新。
- **模块连接**：预训练SNN -> 接收未标记测试数据 -> 进行前向传播（使用自适应激活缩放） -> 计算基于熵的损失（对检测任务使用实例加权） -> 使用前向时间优化算法计算梯度 -> 更新模型参数（包括权重和缩放参数α） -> 输出适应后的模型。
- **训练方式**：在线、无监督、单次前向传播式更新。对于每个测试样本（或批次），模型立即计算损失并更新，而无需等待所有数据。
- **推理流程**：标准的SNN前向传播流程。输入数据被编码为脉冲序列，经过多层IF神经元处理，在多个时间步后累积输出膜电位，用于最终决策。
- **和已有方法的差异**：与传统ANN域适应方法（如对抗训练、特征对齐）相比，本方法**无需源数据、无需标签、无需多轮训练**，是面向SNN架构的轻量化在线方案。与标准SNN训练（BPTT）相比，本方法通过前向时间优化和自适应缩放，实现了计算高效且性能更优的在线适应。

## 6. 实验与结果
- **使用的数据集**：七个基准数据集，涵盖三大任务：
    - 分类：RSSCN, WHU-RS19, AID
    - 语义分割：DLRSD, WHDLD
    - 目标检测：RSOD, LEVIR
- **对比方法**：文中提到与“representative ANN adaptation methods”以及“existing domain adaptation and domain generalization approaches”进行对比。具体方法名称在提供的文本中未完整列出，但应包括如Tent等TTA方法及一些传统域适应方法。
- **评价指标**：分类任务使用准确率（Accuracy），分割任务使用平均交并比（mIoU），检测任务使用平均精度均值（mAP）。
- **主实验结果**：摘要中明确提到，在“varying weather conditions”下，所提方法“**significantly outperforms existing domain adaptation and domain generalization approaches**”。虽然提供的文本未包含完整的实验结果表格，但论文通过大量实验证明了其有效性。
- **消融实验**：论文进行了“ablation study”，用于验证自适应激活缩放、实例加权等各个模块的贡献。图2的分布图可视为对自适应激活缩放模块效果的定性消融分析。
- **泛化实验**：实验设置本身就是在评估模型从源域（如晴朗天气）泛化到不同目标域（如多云、雾天等）的能力。
- **效率信息**：论文核心贡献之一就是提升能效。通过前向时间优化，**显著降低了适应学习的计算复杂度**。第4节将进行“energy efficiency analysis”，但具体数据（如FLOPs、能耗对比）在提供的文本中未找到。

## 7. 这篇论文真正有价值的地方
1.  **开创性研究方向**：这是**首次**系统性地研究SNN的在线适应问题，开辟了“高效在线神经形态感知”这一新的研究方向，对后续研究有奠基意义。
2.  **针对SNN特性的精巧设计**：论文深刻理解了SNN脉冲发放率分布对其性能的影响，并据此提出了**自适应激活缩放**这一简单而有效的机制。这个设计直接针对SNN的“量化”特性，是ANN域适应方法中没有的，体现了对问题本质的洞察。
3.  **实用性与部署友好**：整个框架的设计都围绕“边缘设备在线部署”这一实用目标。前向时间优化算法和无监督学习范式，使其非常适合在资源受限的平台上运行。这为将神经形态计算真正推向实际遥感应用提供了可行的技术路径。
4.  **对后续研究的启发**：SNN如何高效地进行无监督/自监督学习是一个广阔领域。本文的前向时间优化思路可以启发SNN在其他在线学习任务中的算法设计。自适应缩放的思想也可能推广到其他需要调整脉冲网络动态范围的场景。

## 8. 局限与问题
- **任务覆盖与模型通用性**：论文主要实验基于通过ANN-SNN转换得到的SNN模型。虽然文中提及方法可直接用于训练好的SNN，但其在直接训练的、更复杂或更深的SNN模型上的效果有待进一步验证。
- **计算效率的实际表现**：论文强调了算法在复杂度上的优势，但提供的文本中缺少具体的能耗、运行时间或FLOPs对比数据，使得能效提升的量化程度不够清晰。
- **数据集与场景局限**：实验集中在遥感领域的特定数据集上，且主要应对天气变化。方法在更复杂的环境变化（如季节、光照、传感器类型剧变）或更复杂的任务（如实例分割、图像生成）上的泛化能力未知。
- **假设与依赖**：在线适应依赖于每个测试样本都能提供有效的梯度信息（通过熵损失）。如果测试数据噪声极大或熵损失无效，适应过程可能失效。此外，预训练SNN模型的质量是基础。
- **复现风险**：论文提出的优化算法（前向时间优化）是对BPTT的近似，其稳定性和最优性可能需要仔细调节超参数。自适应缩放参数的更新也与主网络权重更新耦合，优化过程可能需要精心设计。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读 **Abstract**、**1 Introduction**（尤其是最后贡献总结）、**2.3 Adaptive Activation Scaling** 和 **2.4 Unsupervised Online Adaptation Learning** 的前几段，以及 **Figure 1** 和 **Figure 2**。
- **如果复现**：重点阅读 **2 Methodology** 全部，特别是 **2.1** 的SNN基础、**2.3** 和 **2.4** 中具体的算法步骤和公式（如公式10, 11, 12）。需要关注自适应缩放参数α的初始化和优化细节，以及前向时间优化梯度计算的实现方式。
- **如果借鉴创新点**：应学习其 **“针对SNN动态特性设计专用机制”** 的研究思路（如自适应缩放）。其 **“将在线学习问题转化为前向传播优化”** 的算法设计思路也极具启发性。此外，**“基于置信度的加权”** 是解决任务特定问题的通用技巧。
- **如果写 related work**：可放在 **“神经形态计算/SNN在视觉任务中的应用”**、**“测试时域适应/在线无监督学习”**、**“遥感图像处理中的域适应与泛化”** 这几个子类下。

## 10. 和其他论文的关系
- 本文是“SNN”、“在线域适应”、“遥感感知”的交叉点。
- 与经典的SNN训练方法（如基于BPTT的监督学习）有继承和发展关系。
- 与ANN上的测试时适应方法（如Tent, TTT）属于同一问题域，但解决方案因SNN特性而完全不同。
- 与将SNN应用于遥感的其他工作（如论文中引用的Liu et al. [2022a], Pang et al. [2024]）相关，但本文专注于“在线适应”这一新维度。
- 由于主题是G_视觉基础模型_VLM_LLM，可能与 [[脉冲神经网络视觉处理]]、[[测试时域适应方法]] 等笔记存在关联。具体论文链接因信息不足无法建立。

## 11. 关键词
无监督域适应, 脑启发计算, 遥感图像处理, 神经形态计算, 脉冲神经网络 (SNN), 在线学习, 测试时适应, 能效优化, 边缘计算, ANN-SNN转换

## 12. 可信度说明
本精读笔记主要基于提供的PDF提取文本（前12页）生成，涵盖摘要、引言和方法论部分。方法框架、核心贡献、自适应缩放机制、在线优化算法等核心内容均有清晰文本依据。由于提供的文本不完整（仅12/22页），实验结果的具体数字、完整的对比方法列表、消融实验的详细表格、以及最终的结论部分缺失，因此笔记中这些部分只能根据已有文本进行概括性描述（如“显著优于”），无法提供具体数据。提取的文本质量尚可，关键公式和概念描述清晰，但实验结果和后续章节信息不全。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2024_Brain-Inspired_Onlin.txt` (22/22 页; 原 AI 主体 12/22 + 全文补读 13-22); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-22; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-22。
- **提取情况**: 缺失页 10 页, 其中 10 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Brain-Inspired Online Adaptation for Remote Sensing with Spiking Neural Network A P REPRINT
- p.13: Table 5: Results of the compared adaptation methods in the semantic segmentation task on the DLRSD and WHDLD
- p.13: Dataset Method Model type Source Target Loss Cloudy Foggy Smoke Rainy Mean mIoU
- p.13: Due to the increase of classes and the complexity of the image data, the source models drop more compared to their
- p.13: 4.3 Results on the Semantic Segmentation Task
- p.13: To demonstrate the broad applicability of the proposed method, we further conduct adaptation experiments on semantic
- p.13: experiments on two optical remote sensing datasets, WHDLD Shao et al. [2018, 2020] and DLRSDShao et al. [2018],
- p.13: It can be seen from TABLE 5 that, weather interference has a significant negative impact on the performance of
- p.13: The AdaptSegNet and ADVENT methods leverage adversarial training between the source and target domain data
- p.14: method.
- p.14: Datasets Method Model type Source Target Loss Cloudy Foggy Smoke Rainy Mean mAP
- p.14: The results show the impact of weather interference on the performance of the source model and demonstrate the

### 缺失页关键摘录

- p.13: Table 5: Results of the compared adaptation methods in the semantic segmentation task on the DLRSD and WHDLD
- p.13: datasets. Mean intersection-over-union (mIoU) (in %) is reported.
- p.13: Dataset Method Model type Source Target Loss Cloudy Foggy Smoke Rainy Mean mIoU
- p.13: achieves the best performance in terms of mean accuracy with both VGG16 and Resnet34 backbones, e.g., 70.03% and
- p.13: TABLE 3 shows the results on the WHU-RS19 dataset. On the WHU-RS19 dataset, the source models without
- p.13: adaptation also drop over 50% of accuracy from the oracle. The TTT method slightly outperforms ADA, while Tent
- p.13: slightly outperforms BN. The proposed method again achieves the best performance, e.g., 59.31% and 59.56% accuracy
- p.13: with the VGG16 and ResNet34 backbones, respectively. On the AID dataset, we observe a similar trend from TABLE 4.
- p.13: performance on the other two datasets. While the source models achieve over 91% accuracy on the source data, they
- p.13: only have an accuracy less than 20% on corruption data, indicating that the models fail in challenging scenarios when
- p.13: facing corruption. As shown in TABLE 4, with the VGG16 backbone, the TTT and ADA methods yield accuracy
- p.13: achieves an accuracy over 48% with both backbones. From the results, we can observe that the overall accuracy on
<!-- AI_READING_NOTE_END -->
