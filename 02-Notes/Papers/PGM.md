---
title: "PromptIR: Prompting for All-in-One Blind Image"
authors:
  - "Restoration"
  - "VaishnavPotlapalli⋆"
  - "SyedWaqasZamir"
  - "SalmanKhan⋆"
  - "FahadShahbazKhan⋆"
  - "⋆MohamedbinZayedUniversityofAI"
  - "InceptionInstituteofAI"
year: 2023
venue: about D. While the model is initially "blind" to the nature of degradation, its performance in
doi: 
pdf: [[PGM.pdf]]
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
extract_cache: .paper-cache/extracts/PGM.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/18 pages"
---
# PromptIR: Prompting for All-in-One Blind Image

## 基本信息
- **PDF**: [[PGM.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | PromptIR: Prompting for All-in-One Blind Image |
| **作者** | Restoration; VaishnavPotlapalli⋆; SyedWaqasZamir; SalmanKhan⋆; FahadShahbazKhan⋆; ⋆MohamedbinZayedUniversityofAI; InceptionInstituteofAI |
| **发表时间** | 2023 |
| **刊物/会议** | about D. While the model is initially "blind" to the nature of degradation, its performance in |
| **DOI** | 未明确 |

## 摘要

> Imagerestorationinvolvesrecoveringahigh-qualitycleanimagefromitsdegraded version. Deeplearning-basedmethodshavesignificantlyimprovedimagerestora- tionperformance, however, theyhavelimitedgeneralizationabilitytodifferent degradation types and levels. This restricts their real-world application sinceit requirestrainingindividualmodelsforeachspecificdegradationandknowingthe inputdegradationtypetoapplytherelevantmodel. Wepresentaprompt-based learningapproach,PromptIR,forAll-In-Oneimagerestorationthatcaneffectively restore images from various types and levels of degradation. In particular, our methodusespromptstoencodedegradation-specificinformation,whichisthen used to dynamically guide the restoration network. This allows our method to generalizetodifferentdegradationtypesandlevels,whilestillachievingstate-of- the-artresultsonimagedenoising,deraining,anddehazing. Overall,PromptIR offersagenericandefficientpluginmodulewithfewlightweightpromptsthatcan beusedtorestoreimagesofvarioustypesandle

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：现实中的图像退化（如噪声、雨滴、雾霾）多种多样。现有的深度学习恢复方法针对每种退化类型/水平需要训练单独的模型，且测试时需要知道退化类型才能选择对应模型，这在实际应用中（如资源受限的移动设备）非常不便且不切实际。
- **之前方法的问题**：1）单一任务方法缺乏泛化能力；2）多任务/全能方法如AirNet（[29]）虽然尝试统一处理，但需要额外的对比学习编码器，导致两阶段训练负担重，并且难以完全解耦不同退化的表示。
- **核心矛盾**：需要一种既能用**单一模型**处理**多种未知退化**，又能**避免复杂训练流程**（如对比学习、多阶段训练），且能**动态适应**输入图像具体退化内容的图像恢复方法。
## 关键贡献

1.  提出了一个**基于提示学习的全能型盲恢复框架PromptIR**。它仅依赖输入图像即可恢复干净图像，无需关于退化的先验知识（p. 2）。
2.  设计了一个**即插即用的提示模块**。该模块由**提示生成模块**和**提示交互模块**构成。PGM动态生成输入条件的提示，PIM通过Transformer块将这些富含退化上下文的提示与输入特征进行交互，从而引导网络进行恢复（p. 2, 4）。
3.  通过**综合性实验**验证了PromptIR的动态适应行为，在图像去噪、去雨、去雾等多个任务上，仅使用一个统一的PromptIR模型即达到了 state-of-the-art 的性能（p. 3）。
## 方法

**整体框架**：采用4级的UNet式编码器-解码器结构，编码器和解码器各级使用Transformer块。核心创新是在解码器的每两个相邻层级之间插入一个**提示模块**（共3个），用于在特征上采样过程中动态注入退化信息（p. 3, Fig. 3）。

**输入输出**：输入是退化图像 ˜I ∈ R^{H×W×3}，输出是恢复后的高质量图像。

**关键模块——提示模块**：
- **组成部分**：每个提示模块包含两个子模块：**提示生成模块**和**提示交互模块**。
- **PGM（提示生成模块）**：
    - **输入**：可学习的提示组件 P_c ∈ R^{N×ˆH×ˆW×ˆC} 和解码器某一层的输入特征 F_l。
    - **功能**：不是直接使用静态提示，而是**动态地**根据输入特征生成加权提示。它通过全局平均池化和通道下采样卷积提取输入特征的上下文，生成一个权重向量 w ∈ R^N（通过Softmax归一化）。然后用这些权重对可学习的提示组件进行加权求和，再通过一个3×3卷积，生成**输入条件的提示 P**。公式为：P = Conv3x3(Σ w_i * P_c)，其中 w_i = Softmax(Conv1x1(GAP(F_l)))。为了处理不同分辨率的输入，提示组件会通过双线性插值上采样到与特征 F_l 相同的空间尺寸（p. 4-5）。
- **PIM（提示交互模块）**：
    - **输入**：PGM生成的提示 P 和输入特征 F_l。
    - **功能**：将提示与特征进行融合，引导特征变换。具体做法是将提示 P 与特征 F_l 在通道维度上进行拼接，然后送入一个**Transformer块**。该Transformer块包含两个子模块：1）**多头深度卷积转置注意力**：在通道维度（而非空间维度）上计算自注意力，具有线性复杂度；2）**门控深度卷积前馈网络**：通过门控机制抑制无用特征，传播有用特征。最终输出增强后的特征 ˆF_l = Conv3x3(GDFN(MDTA[F_l; P]))。这个过程实现了提示对特征的**通道和空间注意力引导**（p. 5）。

**模块连接方式**：提示模块作为“插件”插入到解码器的每两个层级之间。解码器的低分辨率潜在特征 F_l 流入PGM，与可学习提示组件交互生成任务特定提示，然后该提示与特征一同流入PIM进行融合变换，得到增强了退化上下文的特征 ˆF_l，再继续上采样和解码过程（p. 3, Fig. 3）。

**训练方式**：端到端训练。使用L1损失函数，Adam优化器（β1=0.9, β2=0.999），学习率2e-4，训练200个epochs。训练图像裁剪为128x128，并进行随机翻转增强。在全能设置下，批大小为32；在单任务设置下，批大小为8（p. 6）。

**推理流程**：输入一张退化图像，通过网络编码、解码。在解码阶段，PGM会根据输入图像的特征自动计算出相应的提示权重，动态生成提示，并通过PIM引导特征恢复。整个过程无需用户提供退化类型信息。

**与已有方法的差异**：相较于AirNet [29]，PromptIR**不需要额外的对比学习编码器**，避免了复杂的正负样本对选择和两阶段训练，训练流程更简单、直接。提示模块作为一个轻量化的“适配器”插入现有网络（如Restormer），架构无关，即插即用。
## 实验

- **使用的数据集**：
    - **去噪**：训练集：BSD400 + WED（共5144张图像），噪声水平σ ∈ {15, 25, 50}；测试集：BSD68, Urban100。
    - **去雨**：训练/测试集：Rain100L（200/100对）。
    - **去雾**：训练/测试集：SOTS（72,135/500张）。
    - **全能设置**：合并以上所有训练集训练一个模型（p. 6）。
- **对比方法**：包括通用图像恢复方法（BRDNet, LPNet, FDGAN, MPRNet, DL）和专门的全能方法（AirNet [29]），以及基线Restormer [67]（p. 6, Tables 1-4）。
- **评价指标**：主要采用**PSNR**和**SSIM**（p. 6）。
- **主实验结果**：
    - **全能设置**（Table 1）：PromptIR在三个任务的平均PSNR上比AirNet高出**0.86 dB**。具体地，在去雾任务上提升高达**2.64 dB**（从27.94到30.58），在去雨任务上提升**1.47 dB**。
    - **单任务设置**（Tables 2-4）：PromptIR同样表现优异。在SOTS去雾上，比AirNet提升**8.13 dB**（从23.18到31.31）；在Rain100L去雨上提升**2.13 dB**（从34.90到37.04）；在Urban100去噪（σ=50）上提升**0.51 dB**（从28.88到29.39）。
- **消融实验**：提供的文本中未找到详细的消融实验部分。
- **泛化实验**：实验本身就在测试模型对多种退化的泛化能力（全能设置），结果表明其泛化性优于对比方法。
- **速度/参数量/FLOPs等效率信息**：提供的文本中未明确说明PromptIR模型的具体参数量、计算量或运行速度。
## 局限

- **方法局限性**：提示模块的插入位置和结构（基于Restormer的Transformer块）可能与特定网络架构绑定。其有效性是否适用于完全基于CNN或其他架构的网络尚不明确。
- **实验充分性**：提供的文本中未包含详细的消融实验（如提示数量、位置、PGM/PIM组件的必要性分析），也未与其他基于提示学习的视觉方法进行对比。效率方面（计算开销、参数量增加）缺乏讨论。
- **数据集与任务**：实验仅覆盖了去噪、去雨、去雾三种退化。对于更复杂的退化（如混合退化、真实世界退化、模糊等）的泛化能力未知。
- **计算成本与复现**：虽然作者提供了代码，但提示模块引入的额外计算（特别是PGM中的注意力权重计算和PIM中的Transformer块）对整体推理速度的影响未被分析。复现风险较低，因为代码开源。
## 个人评论

1.  **将提示学习引入低层视觉任务的范式**：它成功地将NLP和高级视觉中流行的提示学习思想，创新性地应用于图像恢复这一低级视觉任务，并设计了一个具体、有效的模块实现。这启发我们思考如何在其他低级任务（如超分辨率、修复）中利用类似“轻量、可学习的上下文注入”机制。
2.  **设计了一种简洁、高效的即插即用模块**：提示模块（PGM+PIM）设计得非常巧妙，通过动态加权和通道拼接+Transformer的方式，将任务上下文信息注入网络，而无需修改主干网络结构。这种“插件”思想对于为已有模型增加多任务或自适应能力很有参考价值。
3.  **为多任务统一建模提供了新方案**：与需要显式解耦或对比学习的方法不同，PromptIR通过隐式的、由输入特征触发的提示生成机制来隐式地适应不同任务。这提供了一种更简单、更直接的统一多任务学习思路。

### 使用建议

- **如果快速了解**：阅读**摘要**、**引言**（第1节）和**结论**（第6节，虽未提供但可推断），以及**图1和图3**，即可掌握核心思想和框架。
- **如果复现**：重点精读**第3节方法**，特别是3.1节关于提示模块的公式（1）、（2）、（3）和**第4节实验**中的实现细节（网络结构参数、训练超参、数据集准备）。结合提供的代码仓库复现。
- **如果借鉴创新点**：应重点学习**提示模块的设计思想**（如何动态生成提示、如何注入网络）以及**即插即用的模块化设计思路**。可以尝试将其迁移到其他图像处理网络（如Uformer）或其他任务中。
- **如果写related work**：可以放在以下几个类别：1）图像恢复/增强；2）提示学习/适配器在视觉中的应用；3）多任务/全能型恢复；4）基于Transformer的图像处理。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中的**图像恢复**方向，具体聚焦于 **“全能型”盲图像恢复**。它旨在解决用一个统一模型处理多种未知类型与水平的图像退化问题。适合放在 **“B_注意力算子模块”** 这个主题下，因为其核心的“提示模块”是一种创新的、用于引导网络动态适应退化类型的注意力机制模块，本质上是通过通道与空间注意力（在Transformer块中实现）来动态注入退化上下文信息。

## 2. 一句话总结
这篇论文提出了一种名为 **PromptIR** 的基于提示学习的方法，通过一个即插即用的“提示模块”（包含PGM和PIM），动态生成并注入退化特定信息到恢复网络中，从而用一个统一模型实现了对去噪、去雨、去雾等多种退化的高效盲恢复，无需预先知道退化类型。

## 3. 背景与问题
- **为什么要做**：现实中的图像退化（如噪声、雨滴、雾霾）多种多样。现有的深度学习恢复方法针对每种退化类型/水平需要训练单独的模型，且测试时需要知道退化类型才能选择对应模型，这在实际应用中（如资源受限的移动设备）非常不便且不切实际。
- **之前方法的问题**：1）单一任务方法缺乏泛化能力；2）多任务/全能方法如AirNet（[29]）虽然尝试统一处理，但需要额外的对比学习编码器，导致两阶段训练负担重，并且难以完全解耦不同退化的表示。
- **核心矛盾**：需要一种既能用**单一模型**处理**多种未知退化**，又能**避免复杂训练流程**（如对比学习、多阶段训练），且能**动态适应**输入图像具体退化内容的图像恢复方法。

## 4. 核心贡献
1.  提出了一个**基于提示学习的全能型盲恢复框架PromptIR**。它仅依赖输入图像即可恢复干净图像，无需关于退化的先验知识（p. 2）。
2.  设计了一个**即插即用的提示模块**。该模块由**提示生成模块**和**提示交互模块**构成。PGM动态生成输入条件的提示，PIM通过Transformer块将这些富含退化上下文的提示与输入特征进行交互，从而引导网络进行恢复（p. 2, 4）。
3.  通过**综合性实验**验证了PromptIR的动态适应行为，在图像去噪、去雨、去雾等多个任务上，仅使用一个统一的PromptIR模型即达到了 state-of-the-art 的性能（p. 3）。

## 5. 方法详解
**整体框架**：采用4级的UNet式编码器-解码器结构，编码器和解码器各级使用Transformer块。核心创新是在解码器的每两个相邻层级之间插入一个**提示模块**（共3个），用于在特征上采样过程中动态注入退化信息（p. 3, Fig. 3）。

**输入输出**：输入是退化图像 ˜I ∈ R^{H×W×3}，输出是恢复后的高质量图像。

**关键模块——提示模块**：
- **组成部分**：每个提示模块包含两个子模块：**提示生成模块**和**提示交互模块**。
- **PGM（提示生成模块）**：
    - **输入**：可学习的提示组件 P_c ∈ R^{N×ˆH×ˆW×ˆC} 和解码器某一层的输入特征 F_l。
    - **功能**：不是直接使用静态提示，而是**动态地**根据输入特征生成加权提示。它通过全局平均池化和通道下采样卷积提取输入特征的上下文，生成一个权重向量 w ∈ R^N（通过Softmax归一化）。然后用这些权重对可学习的提示组件进行加权求和，再通过一个3×3卷积，生成**输入条件的提示 P**。公式为：P = Conv3x3(Σ w_i * P_c)，其中 w_i = Softmax(Conv1x1(GAP(F_l)))。为了处理不同分辨率的输入，提示组件会通过双线性插值上采样到与特征 F_l 相同的空间尺寸（p. 4-5）。
- **PIM（提示交互模块）**：
    - **输入**：PGM生成的提示 P 和输入特征 F_l。
    - **功能**：将提示与特征进行融合，引导特征变换。具体做法是将提示 P 与特征 F_l 在通道维度上进行拼接，然后送入一个**Transformer块**。该Transformer块包含两个子模块：1）**多头深度卷积转置注意力**：在通道维度（而非空间维度）上计算自注意力，具有线性复杂度；2）**门控深度卷积前馈网络**：通过门控机制抑制无用特征，传播有用特征。最终输出增强后的特征 ˆF_l = Conv3x3(GDFN(MDTA[F_l; P]))。这个过程实现了提示对特征的**通道和空间注意力引导**（p. 5）。

**模块连接方式**：提示模块作为“插件”插入到解码器的每两个层级之间。解码器的低分辨率潜在特征 F_l 流入PGM，与可学习提示组件交互生成任务特定提示，然后该提示与特征一同流入PIM进行融合变换，得到增强了退化上下文的特征 ˆF_l，再继续上采样和解码过程（p. 3, Fig. 3）。

**训练方式**：端到端训练。使用L1损失函数，Adam优化器（β1=0.9, β2=0.999），学习率2e-4，训练200个epochs。训练图像裁剪为128x128，并进行随机翻转增强。在全能设置下，批大小为32；在单任务设置下，批大小为8（p. 6）。

**推理流程**：输入一张退化图像，通过网络编码、解码。在解码阶段，PGM会根据输入图像的特征自动计算出相应的提示权重，动态生成提示，并通过PIM引导特征恢复。整个过程无需用户提供退化类型信息。

**与已有方法的差异**：相较于AirNet [29]，PromptIR**不需要额外的对比学习编码器**，避免了复杂的正负样本对选择和两阶段训练，训练流程更简单、直接。提示模块作为一个轻量化的“适配器”插入现有网络（如Restormer），架构无关，即插即用。

## 6. 实验与结果
- **使用的数据集**：
    - **去噪**：训练集：BSD400 + WED（共5144张图像），噪声水平σ ∈ {15, 25, 50}；测试集：BSD68, Urban100。
    - **去雨**：训练/测试集：Rain100L（200/100对）。
    - **去雾**：训练/测试集：SOTS（72,135/500张）。
    - **全能设置**：合并以上所有训练集训练一个模型（p. 6）。
- **对比方法**：包括通用图像恢复方法（BRDNet, LPNet, FDGAN, MPRNet, DL）和专门的全能方法（AirNet [29]），以及基线Restormer [67]（p. 6, Tables 1-4）。
- **评价指标**：主要采用**PSNR**和**SSIM**（p. 6）。
- **主实验结果**：
    - **全能设置**（Table 1）：PromptIR在三个任务的平均PSNR上比AirNet高出**0.86 dB**。具体地，在去雾任务上提升高达**2.64 dB**（从27.94到30.58），在去雨任务上提升**1.47 dB**。
    - **单任务设置**（Tables 2-4）：PromptIR同样表现优异。在SOTS去雾上，比AirNet提升**8.13 dB**（从23.18到31.31）；在Rain100L去雨上提升**2.13 dB**（从34.90到37.04）；在Urban100去噪（σ=50）上提升**0.51 dB**（从28.88到29.39）。
- **消融实验**：提供的文本中未找到详细的消融实验部分。
- **泛化实验**：实验本身就在测试模型对多种退化的泛化能力（全能设置），结果表明其泛化性优于对比方法。
- **速度/参数量/FLOPs等效率信息**：提供的文本中未明确说明PromptIR模型的具体参数量、计算量或运行速度。

## 7. 这篇论文真正有价值的地方
1.  **将提示学习引入低层视觉任务的范式**：它成功地将NLP和高级视觉中流行的提示学习思想，创新性地应用于图像恢复这一低级视觉任务，并设计了一个具体、有效的模块实现。这启发我们思考如何在其他低级任务（如超分辨率、修复）中利用类似“轻量、可学习的上下文注入”机制。
2.  **设计了一种简洁、高效的即插即用模块**：提示模块（PGM+PIM）设计得非常巧妙，通过动态加权和通道拼接+Transformer的方式，将任务上下文信息注入网络，而无需修改主干网络结构。这种“插件”思想对于为已有模型增加多任务或自适应能力很有参考价值。
3.  **为多任务统一建模提供了新方案**：与需要显式解耦或对比学习的方法不同，PromptIR通过隐式的、由输入特征触发的提示生成机制来隐式地适应不同任务。这提供了一种更简单、更直接的统一多任务学习思路。

## 8. 局限与问题
- **方法局限性**：提示模块的插入位置和结构（基于Restormer的Transformer块）可能与特定网络架构绑定。其有效性是否适用于完全基于CNN或其他架构的网络尚不明确。
- **实验充分性**：提供的文本中未包含详细的消融实验（如提示数量、位置、PGM/PIM组件的必要性分析），也未与其他基于提示学习的视觉方法进行对比。效率方面（计算开销、参数量增加）缺乏讨论。
- **数据集与任务**：实验仅覆盖了去噪、去雨、去雾三种退化。对于更复杂的退化（如混合退化、真实世界退化、模糊等）的泛化能力未知。
- **计算成本与复现**：虽然作者提供了代码，但提示模块引入的额外计算（特别是PGM中的注意力权重计算和PIM中的Transformer块）对整体推理速度的影响未被分析。复现风险较低，因为代码开源。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：阅读**摘要**、**引言**（第1节）和**结论**（第6节，虽未提供但可推断），以及**图1和图3**，即可掌握核心思想和框架。
- **如果复现**：重点精读**第3节方法**，特别是3.1节关于提示模块的公式（1）、（2）、（3）和**第4节实验**中的实现细节（网络结构参数、训练超参、数据集准备）。结合提供的代码仓库复现。
- **如果借鉴创新点**：应重点学习**提示模块的设计思想**（如何动态生成提示、如何注入网络）以及**即插即用的模块化设计思路**。可以尝试将其迁移到其他图像处理网络（如Uformer）或其他任务中。
- **如果写related work**：可以放在以下几个类别：1）图像恢复/增强；2）提示学习/适配器在视觉中的应用；3）多任务/全能型恢复；4）基于Transformer的图像处理。

## 10. 和其他论文的关系
根据主题“B_注意力算子模块”，本文的核心贡献是设计了一种用于动态引导恢复的注意力模块。它可能与以下论文相关（但需根据实际阅读判断）：
- [[Restormer]]：PromptIR的主干网络，其高效的通道注意力（MDTA）被直接用于提示交互模块（PIM）中。
- [[SwinIR]]：另一个强大的基于Transformer的图像恢复网络，论文提到PromptIR的插件思想理论上也可用于此类架构。
- [[AirNet]]：本文的主要对比方法，采用对比学习解决全能恢复问题。PromptIR旨在用更简单的提示学习方案超越它。
- [[Visual Prompting]]：更广泛的将提示学习用于视觉任务的相关工作，PromptIR是其在低级视觉领域的具体应用。

## 11. 关键词
图像恢复， 提示学习， 全能型恢复， 盲恢复， 提示模块， 提示生成模块， 提示交互模块， 动态适应， 即插即用， UNet， Transformer， 多任务学习

## 12. 可信度说明
本精读笔记主要基于提供的PDF提取文本的前12页生成。这些部分涵盖了论文的**摘要、引言、相关工作、方法概述（含详细公式和图示）、以及部分实验设置和结果（Tables 1-4, Figs. 4-6）**。笔记中的所有方法描述、公式、实验数据均严格来源于该文本，并注明了对应页码(p.X)。然而，由于提供的文本不完整（缺少第7-18页），笔记中关于**消融实验、更多定量/定性结果、完整结论以及附录**的信息标注为“未找到”或“未明确说明”。因此，本笔记完整呈现了论文的核心思想、方法和关键实验结果，但可能遗漏了一些后续的深入分析和补充实验。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/PGM.txt` (18/18 页; 原 AI 主体 12/18 + 全文补读 13-18); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-18; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-18。
- **提取情况**: 缺失页 6 页, 其中 6 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: Appendix
- p.14: A Additional Ablation Studies
- p.14: We conduct further ablation studies to illustrate the effectiveness of various design choices of the
- p.14: PGM module with embeddings extracted from the Contrastive- learning based Degradation Encoder
- p.14: Method Dehazing Deraining Denoising on BSD68 dataset [41]) Average
- p.14: We study the importance of decoder-only prompting by evaluating the usage of prompt blocks on
- p.14: B Transformer Block in PromptIR Framework
- p.16: C Qualitative results:
- p.16: We present more qualitative results from single-task models to further elucidate the effectiveness of

### 缺失页关键摘录

- p.14: We conduct further ablation studies to illustrate the effectiveness of various design choices of the
- p.14: Table A.1: Comparisons under all-in-one setting: between the usage of degradation embedding
- p.14: Method Dehazing Deraining Denoising on BSD68 dataset [41]) Average
- p.14: Table A.2: Comparisons under the all-in-one setting: between the usage of the Prompt-block on both
- p.15: Figure B.1: Overview of the Transformer block used in the PromptIR framework. The Transformer
- p.16: Figure C.1: Image deraining comparisons under single task setting on images from the SOTS
- p.16: dataset [31]. Our method effectively removes haze to produce visually better images.
- p.17: Figure C.2: Image deraining comparisons under single task setting on images from the Rain100L
- p.17: dataset [16]. Our method effectively removes rain streaks to generate rain-free images.
- p.18: Figure C.3: Image deraining comparisons under single task setting on images from the URBAN100
- p.18: dataset [ 22] with σ= 50 . Our method produces visually better images as compared to previous
<!-- AI_READING_NOTE_END -->
