---
title: JyotiKini RohitGupta MubarakShah
authors:
  - "TION IN AERIAL IMAGERY"
  - "JyotiKini RohitGupta MubarakShah"
  - "CenterforResearchinComputerVision"
  - "UniversityofCentralFlorida"
  - "Orlando"
  - "Florida"
year: 2025
venue: "arXiv"
doi: 
pdf: [[2025_Cross-View_Open-Voca.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
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
extract_cache: .paper-cache/extracts/2025_Cross-View_Open-Voca.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# JyotiKini RohitGupta MubarakShah

## 基本信息
- **PDF**: [[2025_Cross-View_Open-Voca.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | JyotiKini RohitGupta MubarakShah |
| **作者** | TION IN AERIAL IMAGERY; JyotiKini RohitGupta MubarakShah; CenterforResearchinComputerVision; UniversityofCentralFlorida; Orlando; Florida |
| **发表时间** | 2025 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Traditionalobjectdetectionmodelsaretypicallytrainedonafixedsetofclasses, limitingtheirflexibilityandmakingitcostlytoincorporatenewcategories.Open- vocabularyobjectdetectionaddressesthislimitationbyenablingmodelstoiden- tify unseen classes without explicit training. Leveraging pretrained models con- trastively trained on abundantly available ground-view image-text classification pairsprovidesastrongfoundationforopen-vocabularyobjectdetectioninaerial imagery.Domainshifts,viewpointvariations,andextremescaledifferencesmake directknowledgetransferacrossdomainsineffective,requiringspecializedadap- tationstrategies. Inthispaper,weproposeanovelframeworkforadaptingopen- vocabularyrepresentationsfromground-viewimagestosolveobjectdetectionin aerialimagerythroughstructureddomainalignment. Themethodintroducescon- trastive image-to-image alignment to enhance the similarity between aerial and ground-viewembeddingsandemploysmulti-instancevocabularyassociationsto align aerial images with text embedding

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：传统目标检测模型在固定类别上训练，缺乏灵活性且难以纳入新类别。开放词汇目标检测能识别训练时未见过的类别，而利用大量地面视角图像-文本对预训练的视觉-语言模型（VLM）为此提供了强大基础。然而，由于**领域偏移、视角差异和极端尺度变化**，直接将这些模型应用于航拍图像效果不佳。
- **之前方法的问题**：
    1.  **直接迁移无效**：地面视角模型直接在航拍图像上零样本检测性能很差。
    2.  **依赖航拍数据**：现有的跨域适应方法（如生成模型、对抗训练）和开放词汇航拍检测方法（如CastDet, SS-OWFormer）通常需要依赖大规模、带标签的航拍数据集进行微调、伪标签生成或特征对齐，而这类数据在实际中往往稀缺或不可用。
    3.  **灾难性遗忘**：对特定航拍数据集进行简单微调会导致模型忘记之前在地面视角学到的知识（如图2所示）。
- **核心矛盾**：如何利用丰富易得的地面视角知识，无需大量标注的航拍数据，就能让模型在航拍视角下实现强大的开放词汇检测能力，同时不丢失原有的地面视角知识。
## 关键贡献

1.  **跨视角图像对齐 (Contrastive Image-to-Image Alignment)**：提出一种新颖的对比学习策略，通过构建航空-地面图像对，显式地增强航拍视角嵌入与地面视角嵌入之间的语义一致性，从而将地面预训练VLM的特征空间有效映射到航拍域。
2.  **多实例词汇关联 (Multi-Instance Vocabulary Association)**：提出一种多实例对比学习技术，将每个航拍图像与一组语义相关的文本描述（文本包）进行对齐，而非严格的一对一匹配，这增强了模型对同一物体不同命名方式的鲁棒性。
3.  **数据生成管线**：设计了一套构建跨视角对齐数据和扩展文本词汇的管线，包括通过直接对应和推理对应建立航空-地面物体检测对应关系（Algorithm 1），以及使用ChatGPT生成类别名称变体以扩展词汇（Algorithm 2，Table 1）。
4.  **广泛的基准评估**：在xView、DOTAv2、VisDrone、DIOR和HRRSD五个航拍数据集上进行了大量实验，证明了方法在零样本设置下的有效性。
## 方法

- **整体框架**：模型构建在预训练的视觉-语言模型（VLMs）之上，包含一个视觉编码器 `f_θ` 和一个文本编码器 `h_ϕ`。框架的核心是在标准检测损失（边界框回归和分类）之外，引入两个新的对比学习损失：**跨视角图像对齐损失**和**航空-文本多实例关联损失**，共同优化，将航空、地面、文本表示置于一个统一的嵌入空间中（Figure 3）。
- **输入输出**：输入是航拍图像 `I_A` 和文本查询 `Y`。输出是检测到的物体类别和位置。训练时还需要地面视角参考图像 `I_G` 及其对应的文本。
- **关键模块与连接**：
    1.  **视觉与文本编码**：航拍图像 `I_A` 通过视觉编码器得到嵌入 `f_θ(I_A)`；文本查询 `Y` 通过文本编码器得到嵌入 `h_ϕ(Y)`。两者在共享的 `d` 维嵌入空间中。
    2.  **跨视角图像对齐 (Sec. 3.1)**：计算航拍图像 `I_A` 与配对的地面图像 `I_G` 之间的对比损失 `L_{Image A – Image G}`（公式1）。该损失拉近正确配对（正对）的相似度，推远与批次内其他地面图像（负对）的相似度。**训练时只更新视觉编码器 `f_θ` 的航空部分，地面图像编码保持固定**。
    3.  **多实例文本关联 (Sec. 3.2)**：计算航拍图像 `I_A` 与一个“文本包”（包含多个语义相关文本描述）之间的对比损失 `L_{Image A – Text}`（公式2，扩展自MIL-NCE）。文本包中的文本被视为该图像的多个正例。
    4.  **数据生成管线 (Sec. 3.3 & 3.4)**：为上述两个损失提供训练数据。
        - *航空-地面对应数据* (D_aligned)：对于共有类别，直接使用标注匹配；对于航空独有类别，使用OWLv2模型在地面图像上生成检测框作为伪匹配（Figure 4, Algorithm 1）。
        - *文本词汇扩展* (D_text)：使用ChatGPT为航空数据集的每个类别生成同义词、变体描述，形成“文本包”（Table 1, Algorithm 2）。
- **数学公式直观解释**：公式1是标准的InfoNCE损失，强制航空-地面正对的嵌入相似。公式2是MIL-NCE损失，允许一个图像与多个文本正例匹配，解决了物体命名歧义问题。
- **训练方式**：联合优化传统的检测损失（边界框回归和分类）与本文提出的两个对比损失。使用生成的 `D_aligned` 和 `D_text` 数据进行训练。
- **推理流程**：PDF文本中未明确说明推理流程，但根据常规开放词汇检测推断：给定一张航拍图像和一个文本查询列表（可包含未见过的类别），模型通过计算视觉嵌入与文本嵌入的相似度来检测和分类物体。
- **和已有方法的差异**：
    1.  **与简单微调相比**：避免了灾难性遗忘（Figure 2），能同时保持地面和航拍性能。
    2.  **与依赖航拍监督的方法（如CastDet）相比**：不依赖于大规模带标签的航拍数据或复杂的伪标签生成流程，而是利用生成的跨视角对应数据进行对齐。
    3.  **与标准VLM对齐方法相比**：显式地建模了跨视角（地面->航拍）的域偏移，而不仅仅是图像-文本对齐。
## 实验

- **使用的数据集**：
    - **训练/对齐**：xView (航拍)， LVIS / CC12M (地面)。
    - **评估（零样本）**：xView, DOTAv2, VisDrone, DIOR, HRRSD。
- **对比方法**：
    - 基线：OWLv2 (零样本)， OWLv2 (在xView上微调)。
    - 其他开放词汇检测器：CastDet, SS-OWFormer等。
- **评价指标**：mAP（平均精度均值）。
- **主实验结果**：
    - 在零样本设置下，本文模型在DOTAv2上比微调的闭集模型性能**提升 +6.32 mAP**，在VisDrone (Images) 上**提升 +4.16 mAP**，在HRRSD上**提升 +3.46 mAP**。
    - 图2显示，在xView上微调的OWLv2导致LVIS（地面）性能下降（-11.1 mAP），而本文方法在xView上提升（+23.6 mAP）的同时，在LVIS上也有提升（+2.2 mAP）。
- **消融实验**：PDF中提到了进行了消融实验以评估设计决策（如编码器patch size，损失贡献），但未提供具体消融数据。
- **泛化实验**：通过在五个不同数据集上的零样本评估，验证了方法的泛化能力。
- **速度/参数量/FLOPs**：PDF文本中未明确说明。
## 局限

1.  **对生成数据质量的依赖**：方法的效果高度依赖于生成的航空-地面对应数据的质量。对于推理对应部分（使用OWLv2生成伪标签），如果OWLv2本身性能不佳或类别在地面数据中罕见，可能会引入噪声。
2.  **对文本编码器的依赖**：整个框架建立在强大的预训练文本编码器（如CLIP的文本编码器）之上，其对自然语言的理解能力直接影响性能。
3.  **计算成本**：PDF中未提及，但构建大规模跨视角对应数据集（31万对）和运行ChatGPT生成词汇需要一定的前期计算和人力成本。
4.  **实验范围**：主要在常见航拍物体类别（车辆、飞机、建筑等）上验证，对于更小众或更复杂的物体类别效果未知。消融实验的具体数据未在提供的文本中展示。
## 个人评论

1.  **问题定义的洞察力**：清晰地指出了现有开放词汇模型从地面到航拍迁移的核心障碍，并提出了一个不依赖目标域大量标注数据的优雅解决方案。
2.  **方法设计的优雅性**：通过两个精心设计的对比损失（图像-图像和图像-文本包）进行结构化对齐，思路清晰，直指跨域对齐和开放词汇识别两个核心。**利用ChatGPT进行词汇扩展**是一个简单却有效的工程技巧，显著提升了文本空间的覆盖度。
3.  **完整的数据构建流程**：提供了从数据生成（跨视角对应、词汇扩展）到模型训练的完整管线，具有很好的可复现性和可借鉴性。
4.  **对后续研究的启发**：
    - **研究思路**：证明了利用对比学习进行跨域特征空间对齐是解决领域自适应问题的有效范式。
    - **改模型**：可以借鉴其多实例文本关联的思想来处理其他存在命名歧义或描述多样性的任务。
    - **做实验**：其零样本评估协议和跨多个数据集测试的做法值得学习，能更全面地衡量模型的泛化能力。

### 使用建议

- **如果快速了解**：只读 **Abstract** 和 **Section 1 (Introduction)** 的后半部分，可以抓住核心问题、方法和主要结果。
- **如果复现**：重点看 **Section 3 (Approach)** 的完整内容，特别是 **Algorithm 1 & 2** 和损失函数公式（公式1， 2）。同时需要关注其依赖的预训练模型（OWLv2, ChatGPT）和训练数据细节（第4节开头）。
- **如果借鉴创新点**：
    - 学习其**跨视角对比对齐**的损失设计（公式1），可用于任何需要将知识从源域迁移到目标域的视觉任务。
    - 学习其**多实例文本关联**（MIL-NCE变体，公式2）和**文本词汇扩展**的思路，适用于处理标签模糊或描述多样的多模态任务。
- **如果写related work**：可放在“开放词汇目标检测（OVD）”和“跨域/跨视角适应”这两个小节中，作为利用对比学习进行跨域VLM知识迁移的代表工作之一。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉领域中的**目标检测**方向，具体聚焦于**开放词汇目标检测**和**跨域适应**。它旨在解决如何将在大规模地面视角图像-文本对上预训练好的开放词汇检测模型，有效迁移到航拍视角这一挑战性领域的问题。该论文适合放在“开放词汇检测”、“跨域适应”或“遥感图像分析”等主题下。

## 2. 一句话总结
本文提出一个新颖框架，通过**跨视角对比图像对齐**和**多实例文本词汇关联**两种机制，将地面视角预训练的视觉-语言模型知识结构化地迁移到航拍图像，以实现无需特定数据集微调的开放词汇目标检测。

## 3. 背景与问题
- **为什么要做**：传统目标检测模型在固定类别上训练，缺乏灵活性且难以纳入新类别。开放词汇目标检测能识别训练时未见过的类别，而利用大量地面视角图像-文本对预训练的视觉-语言模型（VLM）为此提供了强大基础。然而，由于**领域偏移、视角差异和极端尺度变化**，直接将这些模型应用于航拍图像效果不佳。
- **之前方法的问题**：
    1.  **直接迁移无效**：地面视角模型直接在航拍图像上零样本检测性能很差。
    2.  **依赖航拍数据**：现有的跨域适应方法（如生成模型、对抗训练）和开放词汇航拍检测方法（如CastDet, SS-OWFormer）通常需要依赖大规模、带标签的航拍数据集进行微调、伪标签生成或特征对齐，而这类数据在实际中往往稀缺或不可用。
    3.  **灾难性遗忘**：对特定航拍数据集进行简单微调会导致模型忘记之前在地面视角学到的知识（如图2所示）。
- **核心矛盾**：如何利用丰富易得的地面视角知识，无需大量标注的航拍数据，就能让模型在航拍视角下实现强大的开放词汇检测能力，同时不丢失原有的地面视角知识。

## 4. 核心贡献
1.  **跨视角图像对齐 (Contrastive Image-to-Image Alignment)**：提出一种新颖的对比学习策略，通过构建航空-地面图像对，显式地增强航拍视角嵌入与地面视角嵌入之间的语义一致性，从而将地面预训练VLM的特征空间有效映射到航拍域。
2.  **多实例词汇关联 (Multi-Instance Vocabulary Association)**：提出一种多实例对比学习技术，将每个航拍图像与一组语义相关的文本描述（文本包）进行对齐，而非严格的一对一匹配，这增强了模型对同一物体不同命名方式的鲁棒性。
3.  **数据生成管线**：设计了一套构建跨视角对齐数据和扩展文本词汇的管线，包括通过直接对应和推理对应建立航空-地面物体检测对应关系（Algorithm 1），以及使用ChatGPT生成类别名称变体以扩展词汇（Algorithm 2，Table 1）。
4.  **广泛的基准评估**：在xView、DOTAv2、VisDrone、DIOR和HRRSD五个航拍数据集上进行了大量实验，证明了方法在零样本设置下的有效性。

## 5. 方法详解
- **整体框架**：模型构建在预训练的视觉-语言模型（VLMs）之上，包含一个视觉编码器 `f_θ` 和一个文本编码器 `h_ϕ`。框架的核心是在标准检测损失（边界框回归和分类）之外，引入两个新的对比学习损失：**跨视角图像对齐损失**和**航空-文本多实例关联损失**，共同优化，将航空、地面、文本表示置于一个统一的嵌入空间中（Figure 3）。
- **输入输出**：输入是航拍图像 `I_A` 和文本查询 `Y`。输出是检测到的物体类别和位置。训练时还需要地面视角参考图像 `I_G` 及其对应的文本。
- **关键模块与连接**：
    1.  **视觉与文本编码**：航拍图像 `I_A` 通过视觉编码器得到嵌入 `f_θ(I_A)`；文本查询 `Y` 通过文本编码器得到嵌入 `h_ϕ(Y)`。两者在共享的 `d` 维嵌入空间中。
    2.  **跨视角图像对齐 (Sec. 3.1)**：计算航拍图像 `I_A` 与配对的地面图像 `I_G` 之间的对比损失 `L_{Image A – Image G}`（公式1）。该损失拉近正确配对（正对）的相似度，推远与批次内其他地面图像（负对）的相似度。**训练时只更新视觉编码器 `f_θ` 的航空部分，地面图像编码保持固定**。
    3.  **多实例文本关联 (Sec. 3.2)**：计算航拍图像 `I_A` 与一个“文本包”（包含多个语义相关文本描述）之间的对比损失 `L_{Image A – Text}`（公式2，扩展自MIL-NCE）。文本包中的文本被视为该图像的多个正例。
    4.  **数据生成管线 (Sec. 3.3 & 3.4)**：为上述两个损失提供训练数据。
        - *航空-地面对应数据* (D_aligned)：对于共有类别，直接使用标注匹配；对于航空独有类别，使用OWLv2模型在地面图像上生成检测框作为伪匹配（Figure 4, Algorithm 1）。
        - *文本词汇扩展* (D_text)：使用ChatGPT为航空数据集的每个类别生成同义词、变体描述，形成“文本包”（Table 1, Algorithm 2）。
- **数学公式直观解释**：公式1是标准的InfoNCE损失，强制航空-地面正对的嵌入相似。公式2是MIL-NCE损失，允许一个图像与多个文本正例匹配，解决了物体命名歧义问题。
- **训练方式**：联合优化传统的检测损失（边界框回归和分类）与本文提出的两个对比损失。使用生成的 `D_aligned` 和 `D_text` 数据进行训练。
- **推理流程**：PDF文本中未明确说明推理流程，但根据常规开放词汇检测推断：给定一张航拍图像和一个文本查询列表（可包含未见过的类别），模型通过计算视觉嵌入与文本嵌入的相似度来检测和分类物体。
- **和已有方法的差异**：
    1.  **与简单微调相比**：避免了灾难性遗忘（Figure 2），能同时保持地面和航拍性能。
    2.  **与依赖航拍监督的方法（如CastDet）相比**：不依赖于大规模带标签的航拍数据或复杂的伪标签生成流程，而是利用生成的跨视角对应数据进行对齐。
    3.  **与标准VLM对齐方法相比**：显式地建模了跨视角（地面->航拍）的域偏移，而不仅仅是图像-文本对齐。

## 6. 实验与结果
- **使用的数据集**：
    - **训练/对齐**：xView (航拍)， LVIS / CC12M (地面)。
    - **评估（零样本）**：xView, DOTAv2, VisDrone, DIOR, HRRSD。
- **对比方法**：
    - 基线：OWLv2 (零样本)， OWLv2 (在xView上微调)。
    - 其他开放词汇检测器：CastDet, SS-OWFormer等。
- **评价指标**：mAP（平均精度均值）。
- **主实验结果**：
    - 在零样本设置下，本文模型在DOTAv2上比微调的闭集模型性能**提升 +6.32 mAP**，在VisDrone (Images) 上**提升 +4.16 mAP**，在HRRSD上**提升 +3.46 mAP**。
    - 图2显示，在xView上微调的OWLv2导致LVIS（地面）性能下降（-11.1 mAP），而本文方法在xView上提升（+23.6 mAP）的同时，在LVIS上也有提升（+2.2 mAP）。
- **消融实验**：PDF中提到了进行了消融实验以评估设计决策（如编码器patch size，损失贡献），但未提供具体消融数据。
- **泛化实验**：通过在五个不同数据集上的零样本评估，验证了方法的泛化能力。
- **速度/参数量/FLOPs**：PDF文本中未明确说明。

## 7. 这篇论文真正有价值的地方
1.  **问题定义的洞察力**：清晰地指出了现有开放词汇模型从地面到航拍迁移的核心障碍，并提出了一个不依赖目标域大量标注数据的优雅解决方案。
2.  **方法设计的优雅性**：通过两个精心设计的对比损失（图像-图像和图像-文本包）进行结构化对齐，思路清晰，直指跨域对齐和开放词汇识别两个核心。**利用ChatGPT进行词汇扩展**是一个简单却有效的工程技巧，显著提升了文本空间的覆盖度。
3.  **完整的数据构建流程**：提供了从数据生成（跨视角对应、词汇扩展）到模型训练的完整管线，具有很好的可复现性和可借鉴性。
4.  **对后续研究的启发**：
    - **研究思路**：证明了利用对比学习进行跨域特征空间对齐是解决领域自适应问题的有效范式。
    - **改模型**：可以借鉴其多实例文本关联的思想来处理其他存在命名歧义或描述多样性的任务。
    - **做实验**：其零样本评估协议和跨多个数据集测试的做法值得学习，能更全面地衡量模型的泛化能力。

## 8. 局限与问题
1.  **对生成数据质量的依赖**：方法的效果高度依赖于生成的航空-地面对应数据的质量。对于推理对应部分（使用OWLv2生成伪标签），如果OWLv2本身性能不佳或类别在地面数据中罕见，可能会引入噪声。
2.  **对文本编码器的依赖**：整个框架建立在强大的预训练文本编码器（如CLIP的文本编码器）之上，其对自然语言的理解能力直接影响性能。
3.  **计算成本**：PDF中未提及，但构建大规模跨视角对应数据集（31万对）和运行ChatGPT生成词汇需要一定的前期计算和人力成本。
4.  **实验范围**：主要在常见航拍物体类别（车辆、飞机、建筑等）上验证，对于更小众或更复杂的物体类别效果未知。消融实验的具体数据未在提供的文本中展示。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读 **Abstract** 和 **Section 1 (Introduction)** 的后半部分，可以抓住核心问题、方法和主要结果。
- **如果复现**：重点看 **Section 3 (Approach)** 的完整内容，特别是 **Algorithm 1 & 2** 和损失函数公式（公式1， 2）。同时需要关注其依赖的预训练模型（OWLv2, ChatGPT）和训练数据细节（第4节开头）。
- **如果借鉴创新点**：
    - 学习其**跨视角对比对齐**的损失设计（公式1），可用于任何需要将知识从源域迁移到目标域的视觉任务。
    - 学习其**多实例文本关联**（MIL-NCE变体，公式2）和**文本词汇扩展**的思路，适用于处理标签模糊或描述多样的多模态任务。
- **如果写related work**：可放在“开放词汇目标检测（OVD）”和“跨域/跨视角适应”这两个小节中，作为利用对比学习进行跨域VLM知识迁移的代表工作之一。

## 10. 和其他论文的关系
基于提供的主题和文件名，这篇论文可能与以下工作相关：
- **[[OWLv2]]**：本文的关键基线模型和用于生成推理对应数据的模型。
- **[[CastDet]]** 和 **[[SS-OWFormer]]**：同一任务（开放词汇航拍检测）的前期工作，作为对比方法。
- **[[CLIP]]** / **[[ALIGN]]**：其框架所依赖的视觉-语言预训练范式。
- **[[MIL-NCE]]**：本文多实例关联损失（公式2）的思想来源。
（注：由于提供的论文库信息有限，无法确认更多具体关联。）

## 11. 关键词
开放词汇目标检测、航拍图像、跨视角适应、对比学习、视觉-语言模型、领域自适应、知识迁移、零样本检测、多实例学习、词汇扩展

## 12. 可信度说明
本精读笔记**完全基于用户提供的PDF提取文本（前12页）**生成。文本提取质量良好，涵盖了摘要、引言、相关工作、方法、实验设置和部分结果等核心章节。笔记中的所有具体信息（如贡献、方法细节、数字结果）均有文本依据。由于提供的文本不包含完整的实验表格、部分附录以及最终结论章节，因此关于某些实验细节（如完整的消融表格）和可能的局限性讨论，笔记中明确标注为“PDF文本中未明确说明”或基于现有内容进行合理推断。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2025_Cross-View_Open-Voca.txt` (15/15 页; 原 AI 主体 12/15 + 全文补读 13-15); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Unsupervised domain adaptation for remote sensing semantic segmentation with the 2d discrete
- p.13: Yiwu Zhong, Jianwei Yang, Pengchuan Zhang, Chunyuan Li, Noel Codella, Liunian Harold Li,
- p.14: A APPENDIX
- p.14: Experimental results on the VisDrone dataset demonstrate the model-agnostic nature of our frame-
- p.14: Model Finetuned OursmAP

### 缺失页关键摘录

- p.14: Experimental results on the VisDrone dataset demonstrate the model-agnostic nature of our frame-
- p.14: Table 7: Model-agnostic results on the VisDrone dataset.
- p.14: Figure 8: Qualitative results on xView Lam et al. (2018)
- p.14: Figure 9: Qualitative results on DOTAv2 Ding et al. (2021)
- p.15: Figure 10: Qualitative results on VisDrone Cao et al. (2021)
<!-- AI_READING_NOTE_END -->
