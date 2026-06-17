---
title: "Vision-Language Models in Remote Sensing: Current Progress and Future Trends"
authors:
  - "Xiang Li"
  - "Congcong Wen"
  - "Yuan Hu"
  - "Zhenghang Yuan"
  - "Xiao Xiang Zhu"
year: 2023
venue: "arXiv:2305.05726 (cs.CV)"
doi: 
pdf: [[2023_Vision-Language_Mode.pdf]]
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
extract_cache: .paper-cache/extracts/2023_Vision-Language_Mode.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/29 pages"
---
# Vision-Language Models in Remote Sensing: Current Progress and Future Trends

## 基本信息
- **PDF**: [[2023_Vision-Language_Mode.pdf]]
- **primary_topic**: `G_视觉基础模型_VLM_LLM`
- **topics**: `G_视觉基础模型_VLM_LLM`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Vision-Language Models in Remote Sensing: Current Progress and Future Trends |
| **作者** | Xiang Li†,∗; Congcong Wen†; Yuan Hu†; Zhenghang Yuan; Xiao Xiang Zhu (†共同一作, ∗通讯作者) |
| **机构** | KAUST; NYU Abu Dhabi; 北京大学; 慕尼黑工业大学 (TUM) |
| **发表时间** | 2023 (arXiv v1, 2305.05726); v2 修订 2024-04-02 |
| **刊物/会议** | arXiv preprint (cs.CV) |
| **DOI** | 未明确; arXiv:2305.05726 |

## 摘要

> **清理后英文原文**: The remarkable achievements of ChatGPT and GPT-4 have sparked a wave of interest and research in the field of large language models for Artificial General Intelligence (AGI). These models provide intelligent solutions close to human thinking, enabling us to use general artificial intelligence to solve problems in various applications. However, in remote sensing (RS), the scientific literature on the implementation of AGI remains relatively scant. Existing AI-related research in remote sensing primarily focuses on visual understanding tasks while neglecting the semantic understanding of the objects and their relationships. This is where vision-language models excel, as they enable reasoning about images and their associated textual descriptions, allowing for a deeper understanding of the underlying semantics. Vision-language models can go beyond visual recognition of RS images, model semantic relationships, and generate natural language descriptions of the image. This makes them better suited for tasks requiring visual and textual understanding, such as image captioning and visual question answering. This paper provides a comprehensive review of the research on vision-language models in remote sensing, summarizing the latest progress, highlighting challenges, and identifying potential research opportunities. Specifically, we review the application of vision-language models in mainstream remote sensing tasks, including image captioning, text-based image generation, text-based image retrieval, visual question answering, scene classification, semantic segmentation, and object detection. For each task, we analyze representative works and discuss research progress. We also summarize the commonly used remote sensing vision-language datasets, codebases, and online accessible resources. Finally, we delineate the limitations of current studies and suggest potential avenues for future advancements.

> **中文翻译**: ChatGPT 和 GPT-4 的卓越成就在面向通用人工智能（AGI）的大语言模型领域掀起了研究热潮。这些模型提供了接近人类思维的智能解决方案，使我们能用通用人工智能解决各类应用中的问题。然而在遥感（RS）领域，关于 AGI 落地的科学文献仍相对稀少。现有遥感 AI 研究主要聚焦于视觉理解任务，却忽视了对物体及其相互关系的语义理解。这正是视觉-语言模型（VLM）的长处所在——它们能对图像及其关联文本描述进行推理，从而更深入地理解底层语义。VLM 能够超越对遥感图像的视觉识别，建模语义关系，并生成图像的自然语言描述，因此更适合需要同时进行视觉与文本理解的任务，如图像描述（image captioning）与视觉问答（VQA）。本文全面综述遥感领域 VLM 的研究，总结最新进展、指出挑战并识别潜在研究机会。具体而言，本文回顾了 VLM 在主流遥感任务中的应用：图像描述、基于文本的图像生成、基于文本的图像检索、视觉问答、场景分类、语义分割和物体检测；对每个任务分析代表性工作并讨论研究进展；同时汇总常用的遥感视觉-语言数据集、代码库及在线资源；最后阐明当前研究的局限并给出未来发展方向的建议。
>
> **关键词（Index Terms）**: Remote Sensing, Vision-Language Model, AGI, GPT, Transformer

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **这篇论文为什么要做**：ChatGPT 等大语言模型（LLM）的成功在 AGI 领域掀起研究热潮，但在遥感领域 AGI 落地的文献仍相对稀少。早期遥感深度学习主要用 CNN 提取视觉特征来做物体检测、语义分割、变化检测等任务（注意力机制也被引入以聚焦关键区域），这些方法在多种遥感任务上达到 SOTA，**但只关注视觉理解，忽视了对物体及其关系的语义理解**。
- **之前方法有什么问题**：纯视觉模型（vision-only）主要依赖监督学习，在面对**分布外（out-of-distribution）数据**时表现受限。它们缺乏人类的世界知识与推理能力。原文给出的典型例子：做地物分类时，纯视觉模型可能把一个**建筑屋顶像素误分为高速公路像素**，仅因二者在视觉上相似——模型不知道"高速公路不可能修在建筑屋顶上"这一常识。
- **作者想解决的核心矛盾**：**视觉识别能力与语义理解、推理能力之间的鸿沟**。VLM 之所以是答案，是因为它能将世界知识与推理引入视觉分析：例如它"知道船舶更可能出现在水域而非陆地上"，因此基于 VLM 的检测器会倾向于不在陆地上误检船舶。VLM 还带来**零样本/开放词汇理解**（对训练时未见类别有更好泛化）和**人机自然语言交互**（如让非遥感专家用日常语言分析遥感数据的 chatbot）——原文提到的 [138] 即基于 Visual ChatGPT 构建遥感图像处理 chatbot，用 ChatGPT 作为 prompt manager 把用户意图映射到合适的工具/算法。

## 关键贡献

1.  **演进脉络综述**：系统回顾了遥感模型"从视觉中心 → 语言（LLM）→ 视觉-语言（VLM）"的演进路径，并对遥感 VLM 的最新进展做了系统性回顾。
2.  **任务归类分析**：逐一分析 VLM 在七类主流遥感任务中的应用并讨论各任务的代表性工作与研究进展——图像描述、基于文本的图像生成、基于文本的图像检索、视觉问答、场景分类、语义分割、物体检测。
3.  **资源汇总**：总结了常用的遥感视觉-语言数据集、代码库及在线可访问资源。
4.  **挑战与机遇**：明确指出当前研究的局限，并为未来潜在研究方向提供了建议，以激励该领域后续研究。

## 方法

本文是综述（Survey），未提出新模型，但系统介绍了 VLM 的基础架构谱系（对应原文第 II 章 "From Vision-Centric to Vision-Language Models"）。

- **整体框架演进（三阶段）**：
    1.  **视觉中心模型（Vision-Centric）**：
        - **CNN 谱系**（按原文时间线）：LeNet-5（1998, MNIST）→ AlexNet（2012, ImageNet）→ VGG（2014, 更少参数同等性能）→ GoogLeNet/Inception（2015, 多尺度并行卷积）→ ResNet（2016, 残差连接, 152 层）→ DenseNet（2016, 密集连接, 特征复用）→ ResNeXt（2017, cardinality 提升容量）→ EfficientNet（2019, 复合缩放 + NAS）。
        - **视觉 Transformer 谱系**：以自注意力为核心，原文给出公式 (1) `Attention(Q,K,V) = Softmax(QKᵀ/√d_k)·V`；代表有 ViT（首个用于图像分类的 Transformer）及其变体 DeiT（蒸馏）、TNT、PVT（金字塔）、Swin（移位窗口）、Twins（空间可分自注意力）、ViL（局部嵌入替代单 class token）、VOLO（outlook attention）。
    2.  **大型语言模型（LLM）**：
        - **GPT 系**：GPT 通过最大化序列似然训练（公式 2，k 为上下文窗口长度）；GPT-2（15 亿参数）→ GPT-3（验证预训练 LLM 可做零样本/上下文学习）→ InstructGPT（ChatGPT 关键技术之一，用自然语言指令引导生成）→ GPT-4。
        - **BERT 系**：双向预训练，含两个无监督任务——掩码语言建模（公式 3, M 为随机掩码位置）和下一句预测（NSP）；变体有 RoBERTa（更多迭代 + 动态掩码）、ALBERT（参数分解 + 跨层共享 + 句序预测）、MacBERT（用同义词替换 [MASK]）。
        - **其他**：T5（统一 text-to-text 架构）、CoT（思维链提示，启用中间推理）。
    3.  **视觉-语言模型（VLM）**：按架构分两类：
        - **融合编码器（Fusion-Encoder）**：用多层跨模态 Transformer 联合编码图文对并融合表征。**单流**代表 VisualBERT——用 BERT 编码文本 + 预训练 Faster-RCNN 生成物体候选框，将文本与图像区域特征作为无序 token 一起喂入多层 Transformer，通过自注意力隐式对齐图文（Uniter、OSCAR、InterBert 同此范式）。**双流**代表 ViLBERT——分别处理图文，再用协同注意力 Transformer 块（Co-TRM）在两模态间交换信息（LXMERT、Visual Parsing、ALBEF、WenLan 也采用 cross-attention 解耦模态内/跨模态交互）；另有 VisualGPT 用自复活编码器-解码器注意力将预训练语言模型适配到少量域内图文数据。
        - **双编码器（Dual-Encoder）**：用两个独立编码器分别编码图像和文本，投影到共享语义空间后用点积/MLP 算相似度；因预计算并存储嵌入、不需复杂 cross-attention，**交互建模更高效**。典型代表 **CLIP**（对比语言-图像预训练），用文本编码器和图像编码器联合匹配 (image, text) 样本对。
- **关键输入输出**：输入为遥感图像及关联文本（标题、问题、指令）；输出按任务而定——文本描述、生成图像、分类标签、分割图、检测框或问答答案。
- **VLM 相对纯视觉方法的优势**：① 语义推理（建立视觉概念间联系 + 利用世界知识）；② 分布外数据上性能显著提升，进而支持零样本/开放词汇理解；③ 支持需图文协同理解的新任务（图像描述、VQA、语言引导编辑）；④ 自然语言人机交互（VLM chatbot）。

## 实验

本文是综述，**主体未提供作者自身方法的统一实验对比**。提取缓存仅覆盖 p.1-12（摘要 + 引言 + 第 II 章至 CLIP 介绍处），各任务的具体性能表（如原文 TABLE IV/V）位于未覆盖页。

- **使用/汇总的数据集与模型**（据已覆盖文本 + 缺失页线索）：
    - **RS5M**：通过从公开数据集筛选遥感相关图像构建的大规模遥感图像描述数据集，并用 **BLIP-2** 自动生成图像描述。
    - **RSGPT**：先驱工作，构建了高质量人工标注的遥感图像描述数据集 **RSICap**，并提出一个基于 GPT 的遥感图像描述与 VQA 模型。
    - **图像描述基准**（据原文后续页线索, 提取缓存未覆盖, 待核）：RSICD、RSITMD、UCM、Sydney 等数据集，对应原文 TABLE IV。
    - **VQA 数据集**（据原文后续页线索, 提取缓存未覆盖, 待核）：RSVQA（首个遥感 VQA 基准, 含低/高分辨率集）；RSIVQA（约 37k 图文对, 某方法在其上总体准确率 77%）；VQA-TextRS（含 2,144 个遥感样本）；另有方法在 RSVQA 低分辨率集达约 84% 总体准确率、某双模态融合方法达 84.01% 准确率（对应原文 TABLE V）。
- **分析的具体任务**：图像描述、基于文本的图像生成、基于文本的图像检索、视觉问答、场景分类、语义分割、物体检测。
- **评价指标**：综述未在前 12 页统一列出；各任务沿用标准指标（图像描述常用 BLEU/CIDEr，分割常用 mIoU，VQA 用 overall accuracy）。
- **主实验/消融/效率**：作为综述本文无自身方法实验，故 PDF 文本未提供主实验、消融、效率（速度/参数量/FLOPs）等数据。

## 局限

> 说明：以下"局限"主要从综述读者角度归纳；原文作者明确撰写的 limitations/future trends 章节位于未覆盖页（p.13-29），其具体论点 **提取缓存未覆盖, 待核**。

1.  **时效性**：本综述初版为 2023 年（v2 修订于 2024-04），遥感 VLM 领域更新极快，最新成果可能未被覆盖。
2.  **缺乏统一基准横评**：各任务工作使用不同数据集与设置，前 12 页未给出统一的横向性能对比；读者难以直接判断各方法相对优劣（具体性能表见后续页 TABLE IV/V）。
3.  **底层技术细节深度**：为保广度，对每种 VLM 架构（CLIP、VisualBERT 等）的训练技巧、实现细节着墨有限。
4.  **遥感特殊性探讨可加深**：对如何针对遥感图像的特殊性（多时相、多模态、高分辨率、地理坐标等）定制/改进通用 VLM，可进一步深入。

## 个人评论

1.  **清晰的演进定位**：本文最大价值是为研究者（尤其新入门者）提供了"视觉中心 → LLM → VLM"的清晰技术脉络，并把 VLM 精准定位为破解遥感"语义理解缺失"难题的关键路径。
2.  **架构二分法实用**：将 VLM 干净地切成"融合编码器 vs 双编码器"，并点出双编码器（CLIP 式）因可预计算嵌入而更高效——这条工程权衡对选型很有指导意义。
3.  **任务地图 + 资源指南**：系统绘制了 VLM 在七类遥感任务上的应用地图，并汇总数据集/代码/在线资源，显著降低后续研究的检索与入门成本。
4.  **范式转变的启发**：反复强调从"视觉识别"到"结合世界知识的语义理解与推理"的范式转变（船在水里、路不在屋顶上等例子很有说服力），提示选题应关注模型的知识整合与推理能力，而非只在固定类别上刷精度。
5.  **阅读提醒**：本笔记顶部各节与精读块基于提取缓存 p.1-12，七类任务的具体进展与性能数字主要在 p.13-29，引用其数据前应回原文核对。

### 使用建议

- **如果快速了解**：读**摘要 + 引言（第 I 章）**即可掌握 VLM 在遥感中的动机、核心价值与全文框架；第 II 章给出架构谱系。
- **如果复现**：本文是综述，**无可直接复现的自身方法**；应循其"资源汇总"指向的具体工作（RSGPT/RSICap、RS5M/BLIP-2 等）及其代码库复现。
- **如果借鉴创新点**：学习其**"融合编码器 / 双编码器"二分法**，以及**把 VLM 能力（语义推理、零样本）与具体遥感任务（分类/检测/VQA）对接的思考范式**。
- **如果写 Related Work**：作为"VLM 在遥感应用"子方向的综合性背景文献引用，或借其任务分类组织相关工作。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[G_视觉基础模型_VLM_LLM]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇**综述（Survey）**，主题为**遥感（Remote Sensing）领域的视觉-语言模型（Vision-Language Models, VLM）的当前进展与未来趋势**（arXiv:2305.05726, cs.CV, v2 于 2024-04-02 修订）。作者来自 KAUST、NYU Abu Dhabi、北京大学和慕尼黑工业大学（Xiang Li 等，前三位共同一作）。论文位于**计算机视觉与自然语言处理交叉、并落地到地球观测/遥感应用**的位置，核心命题是：传统纯视觉模型在遥感任务中缺乏语义理解与推理能力，而 VLM 通过引入语言与世界知识来弥补这一缺口。归类于 **G_视觉基础模型_VLM_LLM** 准确。

## 2. 一句话总结
本文系统综述了视觉-语言模型如何把视觉特征与语言/世界知识结合，突破纯视觉遥感分析"只识别不理解"的局限，并梳理了 VLM 沿"视觉中心→LLM→VLM"的架构演进及其在图像描述、文生图、图文检索、VQA、场景分类、语义分割、物体检测七类遥感任务上的应用、数据资源与未来方向。

## 3. 背景与问题
- **为什么要做**：ChatGPT/GPT-4 引爆 AGI 研究，但遥感领域 AGI 落地文献稀少。早期遥感深度学习用 CNN（及注意力机制）提取视觉特征做检测/分割/变化检测，达到 SOTA，**却只做视觉理解、忽视语义理解**。
- **纯视觉方法的问题**：依赖监督学习，面对分布外数据吃力；缺乏世界知识与推理。原文经典反例——把"建筑屋顶像素"误判为"高速公路像素"，只因视觉相似而模型不懂"高速公路不会修在屋顶上"。
- **核心矛盾**：视觉识别能力 vs. 语义理解与推理能力之间的鸿沟。VLM 通过引入世界知识缓解之（"船在水里、不在陆上"），并解锁零样本/开放词汇理解与自然语言人机交互（如基于 Visual ChatGPT 的遥感处理 chatbot，用 ChatGPT 作 prompt manager 调度工具）。

## 4. 核心贡献
1.  **演进脉络综述**：系统梳理遥感模型从视觉中心→语言→视觉-语言的演进，并综述遥感 VLM 最新进展。
2.  **任务归类分析**：逐一分析七类主流遥感任务（图像描述、文本生成图像、文本检索图像、视觉问答、场景分类、语义分割、物体检测）的代表工作与进展。
3.  **资源汇总**：汇总常用遥感视觉-语言数据集、代码库与在线资源。
4.  **挑战与机遇**：指出当前局限并给出未来方向建议。

## 5. 方法详解
综述无新方法，核心是第 II 章的架构谱系（详见正文"方法"节）：
- **视觉中心**：CNN 时间线 LeNet-5→AlexNet→VGG→GoogLeNet→ResNet→DenseNet→ResNeXt→EfficientNet；ViT 系（自注意力公式 1）DeiT/TNT/PVT/Swin/Twins/ViL/VOLO。
- **LLM**：GPT 系（似然公式 2；GPT-2 15 亿参数、GPT-3 零样本、InstructGPT 指令、GPT-4）；BERT 系（双向预训练 = 掩码 LM 公式 3 + NSP；RoBERTa/ALBERT/MacBERT）；T5、CoT。
- **VLM**：① 融合编码器——单流 VisualBERT（BERT + Faster-RCNN，自注意力隐式对齐图文；Uniter/OSCAR/InterBert 同范式），双流 ViLBERT（Co-TRM 协同注意力；LXMERT/Visual Parsing/ALBEF/WenLan），及 VisualGPT；② 双编码器——CLIP（对比预训练、可预计算嵌入、更高效）。
- **优势**：语义推理、分布外鲁棒/零样本开放词汇、图文协同新任务、自然语言交互。

## 6. 实验与结果
综述主体不含作者自身实验。提取缓存仅覆盖 p.1-12，七类任务的性能表（原文 TABLE IV/V 等）在未覆盖页。
- **已确认数据资源**：RS5M（筛选公开图像 + BLIP-2 自动生成描述的大规模遥感图像描述集）；RSGPT（构建人工标注数据集 RSICap，并提出基于 GPT 的遥感图像描述/VQA 模型）。
- **缺失页线索（据原文后续页, 提取缓存未覆盖, 待核）**：图像描述基准 RSICD/RSITMD/UCM/Sydney（TABLE IV）；VQA 数据集 RSVQA、RSIVQA（约 37k，某方法 77% 准确率）、VQA-TextRS（2,144 样本）；某方法在 RSVQA 低分辨率集约 84% 准确率，某融合方法 84.01% 准确率（TABLE V）。
- **指标**：图像描述 BLEU/CIDEr、分割 mIoU、VQA overall accuracy 等（前 12 页未统一列出）。

## 7. 这篇论文真正有价值的地方
1.  **演进脉络清晰**：给出"视觉中心→LLM→VLM"的完整技术地图，对入门者尤为友好。
2.  **架构二分法 + 工程直觉**：融合编码器 vs 双编码器的划分干净，并点明双编码器因可预计算嵌入而更高效，对模型选型有实操价值。
3.  **任务地图 + 资源指南**：七任务应用地图 + 数据集/代码汇总，显著降低后续研究的检索成本。
4.  **范式转变叙事**：用"船在水里、路不在屋顶上"等直观例子强调从"视觉识别"到"语义理解与推理"的转变，对选题方向有启发。

## 8. 局限与问题
（注：原文 limitations/future trends 章节在未覆盖页 p.13-29，下列以读者视角归纳，**作者原话待核**。）
1.  **时效性**：2023 年初版（v2 2024-04），更新极快领域可能漏掉最新成果。
2.  **缺乏统一横评**：各工作数据集/设置不一，前 12 页未给统一性能对比表。
3.  **技术细节深度**：为保广度，对各 VLM 架构的训练技巧着墨有限。
4.  **遥感特殊性**：对针对多时相/多模态/高分辨率/地理坐标定制 VLM 的探讨可加深。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要 + 引言（第 I 章）掌握动机与框架，第 II 章看架构谱系。
- **复现**：综述无自身方法，循其资源汇总指向的具体工作（RSGPT/RSICap、RS5M/BLIP-2 等）复现。
- **借鉴**：学其融合/双编码器二分法，及"VLM 能力 × 遥感任务"的对接范式。
- **写 Related Work**：作为"VLM 在遥感"子方向综合背景文献引用。

## 10. 和其他论文的关系
- 同主题 `G_视觉基础模型_VLM_LLM` 下，本综述与以下通用 VLM/LLM 工作密切相关（均为原文引用）：
    - `[[CLIP]]`：双编码器代表，对比预训练做图文匹配。
    - `[[VisualBERT]]`、`[[ViLBERT]]`：融合编码器（单流/双流）代表。
    - `[[GPT]]`、`[[BERT]]`：作为 VLM 基础组件的 LLM。
    - `[[BLIP-2]]`：被 RS5M 用于自动生成遥感图像描述。
- 文件名 `2023_Vision-Language_Mode.pdf` 对应本综述本身；它与遥感专用 VLM 工作（RSGPT、RS5M 等）构成"综述 ↔ 具体工作"关系，后者细节多在本笔记未覆盖的 p.13-29。

## 11. 关键词
遥感, 视觉-语言模型 (VLM), 大型语言模型 (LLM), AGI, GPT, BERT, CLIP, Transformer, 图像描述, 文本生成图像, 图文检索, 视觉问答 (VQA), 场景分类, 语义分割, 物体检测, 零样本/开放词汇学习, 融合编码器, 双编码器

## 12. 可信度说明
本精读笔记基于提取缓存 **p.1-12**（摘要 + 引言第 I 章 + 第 II 章 "From Vision-Centric to Vision-Language Models" 至 CLIP 介绍开始处）。该段文本连贯、质量良好，关于架构定义、模型谱系、任务范围与 VLM 优势的论述均直接来自文本，可信度高。**七类任务的具体研究进展、性能表（TABLE IV/V）、数据集细节及作者撰写的局限/未来趋势章节位于 p.13-29，不在提取缓存内**；笔记中相关数字（RSIVQA 37k/77%、VQA-TextRS 2,144、84.01% 等）来自笔记原"全文补读记录"的缺失页摘录线索，已统一标注"据原文后续页, 提取缓存未覆盖, 待核"。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2023_Vision-Language_Mode.txt` (提取覆盖 12/29 页; 原 AI 主体 p.1-12 + 缺失页线索 p.13-29 据补读记录); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-29; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-29。
- **提取情况**: 缺失页 17 页, 其中 17 页提取到可读文本。缺失页包含正文/附录内容, 其中约 7 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: ApproachRSICD dataset RSITMD dataset
- p.13: ApproachUCM dataset Sydney dataset
- p.13: TABLE IV
- p.13: method.
- p.13: Furthermore, we provide a summary of the performance
- p.13: Visual question answering (VQA) is a task that seeks to pro-
- p.13: OpenStreetMap, with human-generated questions and answers
- p.13: method that uses Convolutional neural networks (CNNs) for
- p.13: Unlike previous methods that mainly focus on solving
- p.14: While existing RSVQA methods have demonstrated promis-
- p.14: Method Presence Comparison Average Accuracy
- p.14: TABLE V

### 缺失页关键摘录

- p.13: Sydney datasets in Table IV. In the table presented, we disclose
- p.13: VQA benchmark dataset for RS images, called RSVQA. Both
- p.13: resolution set. In [122], the authors provided a benchmark
- p.13: answering dataset called RSIVQA that contains around 37k
- p.13: The proposed method achieved an overall accuracy of 77% on
- p.13: their RSIVQA dataset. Chappuis et al. [19] proposed to use
- p.13: neural networks. This method obtained an overall accuracy
- p.13: close to 84% on the low-resolution set of the RSVQA dataset.
- p.13: of the RSVQA dataset and improved the robustness of the
- p.13: introduced a novel dataset, VQA-TextRS, with 2,144 RS
- p.13: mechanism to integrate the two modalities. As a result, the
- p.13: proposed method achieved an accuracy of 84.01% in relation
<!-- AI_READING_NOTE_END -->
