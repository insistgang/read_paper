---
title: 深度学习实时语义分割综述 (Deep learning-based real-time semantic segmentation: a survey)
authors:
  - "高常鑫"
  - "徐正泽"
  - "吴东岳"
  - "余昌黔"
  - "桑农"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.230659
pdf: [[cjig_图像识别_深度学习实时语义分割综述_完整版.pdf]]
primary_topic: F_图像分割_语义_实例_全景
topics:
  - "F_图像分割_语义_实例_全景"
  - "R_综述_Survey"
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
extract_cache: .paper-cache/extracts/cjig_图像识别_深度学习实时语义分割综述_完整版.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/27 pages"
---
# 深度学习实时语义分割综述 (Deep learning-based real-time semantic segmentation: a survey)

## 基本信息
- **PDF**: [[cjig_图像识别_深度学习实时语义分割综述_完整版.pdf]]
- **primary_topic**: `F_图像分割_语义_实例_全景`
- **topics**: `F_图像分割_语义_实例_全景`, `R_综述_Survey`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 深度学习实时语义分割综述 (Deep learning-based real-time semantic segmentation: a survey) |
| **作者** | 高常鑫; 徐正泽; 吴东岳; 余昌黔; 桑农 (华中科技大学人工智能与自动化学院 / 类脑智能系统湖北省重点实验室 / 北京三快科技(美团)) |
| **发表时间** | 2024 (中国图象图形学报 29(05): 1119-1145) |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics) |
| **DOI** | 10.11834/jig.230659 |
| **代码/资源** | https://github.com/xzz777/Awesome-Real-time-Semantic-Segmentation |

## 摘要

**英文原摘要（据 PDF 提取文本整理，已修复空格/连字符断裂并剔除杂入的版式数字）：**

> Semantic segmentation is a fundamental task in the field of computer vision, which aims to assign a category label to each pixel in the input image. Many semantic segmentation networks have complex structures, high computational costs, and massive parameters. As a result, they introduce considerable latency when performing pixel-level scene understanding on high-resolution images. These limitations greatly restrict the applicability of these methods in resource-constrained scenarios, such as autonomous driving, medical applications, and mobile devices. Therefore, real-time semantic segmentation methods, which produce high-precision segmentation masks with fast inference speeds, receive widespread attention. This study provides a systematic and critical review of real-time semantic segmentation algorithms based on deep learning techniques. It covers three key aspects: real-time semantic segmentation networks, mainstream datasets, and common evaluation indicators. In accordance with the characteristics of the overall network structure, existing works are categorized into five categories: single-branch, two-branch, multibranch, U-shaped, and neural architecture search networks, covering CNN-based, Transformer-based, and hybrid-architecture-based segmentation networks. To avoid the interference of different devices, this study compares the performance of advanced methods of each category with the same devices and configuration, establishing a fair and integral evaluation system. Finally, current challenges are discussed, and possible future directions are envisioned (e.g., utilization of Transformers, applications on edge devices, knowledge transfer of visual foundation models, diversity of evaluation indicators, variety of datasets, utilization of multimodal data and weakly supervised methods, combination with incremental learning).

**中文翻译（即论文中文摘要原文）：**

> 语义分割是计算机视觉领域的一项像素级别的感知任务，目的是为图像中的每个像素分配相应类别标签，具有广泛应用。许多语义分割网络结构复杂，计算量和参数量较大，在对高分辨率图像进行像素层次的理解时具有较大的延迟，这极大限制了其在资源受限环境下的应用，如自动驾驶、辅助医疗和移动设备等。因此，实时推理的语义分割网络得到了广泛关注。本文对深度学习中实时语义分割算法进行了全面论述和分析：1) 介绍了语义分割和实时语义分割任务的基本概念、应用场景和面临问题；2) 详细介绍了实时语义分割算法中常用的技术和设计，包括模型压缩技术、高效 CNN 模块和高效 Transformer 模块；3) 全面整理和归纳了现阶段的实时语义分割算法，包括单分支网络、双分支网络、多分支网络、U 型网络和神经架构搜索网络 5 种类别，涵盖基于 CNN、基于 Transformer 和基于混合框架的分割网络，并分析了各类算法的特点和局限性；4) 提供了完整的实时语义分割评价体系，包括相关数据集和评价指标、现有方法性能汇总以及领域主流方法的同设备比较，为后续研究者提供统一的比较标准；5) 给出结论并分析了领域仍存在的挑战，对未来可能的研究方向提出了相应见解。
>
> **关键词**：实时语义分割；模型轻量化；高效模块设计；计算机视觉；深度学习

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：语义分割是计算机视觉中长期存在的像素级感知任务，广泛应用于医学图像处理、机器人视觉、遥感图像分类、增强现实、图像压缩与传送、自动驾驶视觉、智能视频分析等。FCN (Long 等, 2015) 之后 CNN 成为分割新范式，VGG/GoogLeNet/ResNet/HRNet 等更强主干，以及 U-Net/PSPNet/RefineNet、各类注意力模块、乃至视觉 Transformer (ViT, SETR, PVT, SegFormer, Swin) 不断刷新精度上限。但这些方法在高分辨率图像上推理延迟显著，难以满足实时需求。
- **之前方法的问题**：高精度网络的高延迟源于两方面——1) 为捕获丰富空间细节需保留**高分辨率底层特征图**，极大增加计算代价；2) 为捕获多尺度上下文与长距离依赖需设计**复杂模块与交互**，增加推理延迟。尤其自注意力机制虽具全局建模能力，但与图像分辨率呈**平方复杂度**，显著放大延迟。
- **实时定义**：论文明确给出——实时语义分割网络指在指定设备上推理帧率达到 **30 帧/s 及以上**（人眼对视频流畅的最低帧率要求）的语义分割网络。在实际场景（移动端、自动驾驶、人机交互）中，繁重网络往往产生不可接受的秒级延迟。
- **核心矛盾**：如何以**更少的计算代价**，同时**保留更丰富的空间信息**并**捕获更有效的多尺度上下文**，以得到更好的模型**速度—精度平衡**。此外在资源受限的移动/边缘设备上，模型的**大小和内存占用量**也是关键挑战。

## 关键贡献

1.  **系统梳理前置技术**：归纳实时语义分割常用的四类模型压缩技术（网络剪枝、神经架构搜索 NAS、知识蒸馏、量化）、高效 CNN 模块（ShuffleNet、MobileNet、EfficientNet 系列）和高效 Transformer 模块（外部注意力 EA、SeaFormer、MobileViT 等）。
2.  **提出五类分类框架**：按网络整体结构特点将现有方法系统归纳为五大类——**单分支网络、双分支网络、多分支网络、U 型网络、神经架构搜索网络**，涵盖 CNN/Transformer/混合架构，并分析各类的特点和局限。另从网络框架类型、应用场景类型加以分类。
3.  **建立评价体系**：整理相关数据集（分为自动驾驶场景与通用场景）、评价指标（精度指标 + 效率描述符），汇总现有方法性能，并提出在**相同设备与配置下做公平比较**，为后续研究提供统一标准。
4.  **开源研究资源**：将论文提及的算法、数据集、评估指标汇总于公开仓库 `https://github.com/xzz777/Awesome-Real-time-Semantic-Segmentation`。

## 方法

本篇为综述论文，其"方法"在于**系统性地介绍和分类归纳**现有实时语义分割技术，而非提出单一新模型。论文结构（图 1）分 5 部分：引言、前置知识、方法分类、评价体系、结语。

- **前置知识（第 1 节）**：
    - **模型压缩**：网络剪枝（训练大网络→评估参数重要性→去掉不重要参数→微调恢复精度）；NAS（在搜索空间内用搜索策略得到最优网络，可加入准确率/推理延迟等指标）；知识蒸馏（大教师监督小学生）；量化（降低数字精度以压缩模型、加速推理）。
    - **高效 CNN 模块**：
        - **ShuffleNet**：分组卷积 (Krizhevsky 等, 2012) 减少计算量但阻碍组间信息流，故引入**通道洗牌 (channel shuffle)** 实现组间信息交互。ShuffleNetV2 用通道划分替代分组卷积、调整洗牌位置，以通道拼接+洗牌代替像素级相加，效率更高。
        - **MobileNet**：核心是**深度可分离卷积**（深度卷积 + 点卷积）。**MobileNetV2** 提出**倒置残差模块**（升维点卷积-深度卷积-降维点卷积+残差）和**线性瓶颈**（降维点卷积后不加激活，因 ReLU 作用于低维特征损失大），并使用 ReLU6 提升低比特量化鲁棒性。**MobileNetV3** 在倒置残差块中加入 **SE 模块**、引入 **h-swish** 激活并用网络搜索进一步提效。
        - **EfficientNet**：分析深度/宽度/分辨率缩放影响，基于 MobileNetV2 模块用网络搜索做**复合缩放**得到一系列高效模型。EfficientNetV2 改进 MobileNetV3 模块、采用非均匀缩放与渐进式输入。
    - **高效 Transformer 模块**：
        - **外部注意力 (EA, Guo 等, 2023)**：Query 保留原始特征图，Key/Value 替换为与图像无关的可学习参数 Mk、Mv（Mk, Mv ∈ R^{B×M×C}），用**双重归一化 DoubleNorm**（维度 N 上 softmax、维度 M 上 L1）。将注意力计算复杂度从 **O(H²W²) 降至 O(HW)**，仅由两个额外线性层实现，延迟低。
        - **SeaFormer (Wan 等, 2023)**：提出**轴向压缩增强注意力 (squeeze-enhance axial attention)**，将 Key、Value（以及进一步 Query）在图像宽、高方向分别压缩；为弥补压缩造成的局部信息丢失，对原始 Q/K/V 用深度可分离卷积获得特征图，并以轴向压缩增强注意力的输出作为权重增强该特征图。
        - 此外还提及 **MobileViT**（混合 Transformer-CNN）、**MobileFormer**（Transformer 提全局、与卷积分支反复跨注意力交互）、**EdgeViT**（局部卷积 + 稀疏注意力），但在实时分割中应用较少，不详述。
- **方法分类（第 2 节）** — 五类网络结构（表 1 归纳特点）：
    - **单分支网络**：编码器为单支层级式主干，解码器轻量。细分 3 种：① **单尺度轻量解码器**（仅用编码器最后输出，如 **ENet**——最早探索实时性、早期下采样 + 轻量解码器、编解码不对称）；② **多尺度轻量解码器**（融合编码器多阶段特征后简单拼接映射，如 **SegFormer**——首个用于实时分割的 Transformer，Key/Value 下采样使复杂度 O(N²)→O(N²/R)，MLP 解码器；以及 **SegNext**——只用阶段 2-4 特征拼接，用多尺度卷积注意力 MSCA 模拟自注意力，性能超 SegFormer）；③ **无解码器**（直接用分类头，下采样仅至 1/8，如 **DABNet**——DAB 模块用 3×3 卷积+3×1/1×3 条纹卷积+条纹空洞卷积扩大感受野；**AFFormer**——用自适应频率滤波器 AFF 替换自注意力，PL/PD 双支建模上下文与局部细节）。
    - **双分支网络**：解耦空间细节与语义上下文。细分 2 种：① **解耦双分支**（从输入即分两路，如 **BiSeNet**——空间路径 + 上下文路径 + 特征融合模块 FFM；**BiSeNetV2**——Stem 模块、聚合拓展模块、上下文表征模块 + 双向引导聚合；**STDC**——STDC 模块调整卷积核深度/个数获多感受野特征，空间路径仅用 stage3 + 细节头边缘监督，推理时不计算细节头，大幅削减额外计算）；② **特征共享双分支**（早期共享、深层分支，如 **Fast-SCNN**——学习下采样共享早期层；**DDRNet**——浅层 1/8 前共享、深层高/低分辨率双支，每阶段双边融合 + DAPPM 深度聚合金字塔扩大感受野；**RTFormer**——沿用 DDRNet 结构，深层用双分辨率 RTFormer 模块，低分辨率分支自注意力、高分辨率分支跨注意力，GPU 友好注意力 + 逐步融合；**SeaFormer**——混合 Transformer-CNN，DDRNet 类框架但用单边融合，上下文分支用 SeaFormer 层 + 大量 MobileNetV2 模块，移动端速度-精度平衡最佳）。
    - **多分支网络**：编码器多独立分支或多子网，捕获不同层次/分辨率信息（表 2 归纳）：**ICNet**（首个多分支，多分辨率 1/4-1/2-原图级联，级联特征融合单元 CCF + 多分辨率真值监督）、**ESPNet**（高效空间金字塔 ESP：1×1 降维 + 不同空洞率卷积，分层特征融合 HFF 避免网格效应，子网共享浅层参数故参数量小）、**DFANet**（额外子网精炼多尺度特征）、**PIDNet (Xu 等, 2023)**（浅层共享、深层独立的多分支结构，输入多尺度特征图）。
    - **U 型网络 / 神经架构搜索网络**：详细内容位于提取缓存未覆盖的后续页（见下方"全文补读记录"，含 U 型网络示意图 Fig.8、NAS 网络表 Table 3：DF-Seg、FasterSeg、RT-Seg 等）。
- **与已有方法的差异**：作为综述，差异在于**系统性**与**时效性**——既覆盖经典 CNN 方法（ENet、BiSeNet），又纳入最新 Transformer（SegFormer、SeaFormer、AFFormer）与混合架构，并首次从网络结构角度给出清晰、全面的五类分类体系。

## 实验

- **使用的数据集**：论文将数据集分为**自动驾驶场景**与**通用场景**两类。提取文本（前 12 页）确认 **Cityscapes**（据 p.16 摘录，含 5000 幅精细标注图像；据原文后续页，提取缓存未覆盖，待核），完整数据集汇总见 p.17 的 Table 5（提取缓存未覆盖）。原笔记推测的 CamVid、ADE20K 等未在提取文本明确出现，"PDF 文本未明确"。
- **对比方法**：覆盖单分支、双分支、多分支、U 型、NAS 五类，涵盖 CNN/Transformer/混合架构。完整方法清单见 p.16 的 Table 4 "Overview of real-time semantic segmentation methods"（按 Desktop/Mobile GPU、Mobile CPU 等设备分类；提取缓存未覆盖）。
- **评价指标**：分为**精度指标**与**效率描述符**。精度指标主要为 **mIoU**（平均交并比）；效率描述符包括推理速度（FPS）、参数量 (Params)、计算量 (FLOPs, floating point operations)。指标汇总见 p.18 Fig.11（提取缓存未覆盖）。
- **主实验结果**：论文提供"现有方法性能汇总"与"同设备公平比较"（p.19 Table 6 "Comparison of the performance on Cityscapes dataset"）。具体数字位于提取缓存未覆盖的后续页：据原文 p.18 摘录，有方法在 Cityscapes 测试集达 **80.6% mIoU**、验证/其他达 **80.9% mIoU**，**RTFormer-B 达 82.5% mIoU、RTFormer-S** 亦给出数值（据原文后续页，提取缓存未覆盖，待核）。提取文本（前 12 页）本身未含性能表格。
- **消融/泛化实验**：作为综述不做消融，但系统总结并分析各方法的模块设计效果。
- **效率信息**：论文强调在统一设备与配置下做**速度、参数量、FLOPs** 的公平比较以建立评价体系，具体数据在提取缓存（前 12 页）中未出现。

## 局限

- **提取覆盖局限（笔记层面）**：本笔记主体基于 PDF 提取文本前 12 页，U 型网络与 NAS 网络的详细方法、完整实验结果表（Table 4/5/6）、指标图（Fig.11）、结论与未来展望等位于提取缓存未覆盖的后续页，相关数字均标注为"待核"。
- **时效性（论文层面）**：收稿 2023-09，内容截止 2023 年左右，2024 年及之后的最新工作可能未涵盖。
- **分类边界主观性**：论文自述"个别方法可能由多种类别衍生，按其最重要的贡献归到一类"，分类标准存在一定主观性（如 SeaFormer 既是高效 Transformer 模块又是特征共享双分支网络）。
- **深度与广度权衡**：综述对每个具体方法解读深度有限，不能替代对原始论文的精读。

## 个人评论

1.  **分类框架抓住结构本质**："单分支 / 双分支 / 多分支 / U 型 / NAS"五类划分直接对应"如何分配空间细节与上下文建模的计算预算"这一核心设计抉择，是建立领域知识图谱的极佳路线图。尤其"解耦双分支 → 特征共享双分支"的演化主线（BiSeNet → Fast-SCNN → DDRNet → RTFormer → SeaFormer）讲清了实时分割近年最重要的一条技术脉络。
2.  **从算子到架构的完整视角**：把模型压缩（剪枝/NAS/蒸馏/量化）与高效模块（ShuffleNet/MobileNet/EfficientNet、EA/SeaFormer）作为前置知识先讲，再讲架构，使读者理解"高效网络 = 高效算子 × 合理架构"的完整设计逻辑，而非只看顶层结构。
3.  **直击公平比较痛点**：实时分割领域 FPS 严重依赖硬件/分辨率/精度 (FP16/INT8)/是否含后处理，跨论文数字常不可比。本文坚持"同设备同配置"比较，对推动标准化价值很大，也是综述少有的实证贡献。
4.  **可改进处**：作为读者最希望看到的"速度-精度散点图 + 帕累托前沿"在正文图表（Fig.11/Table 6）中，但提取缓存未覆盖，无法在此核对；混合架构（CNN+Transformer）的部署友好性结论（如 SeaFormer 移动端最优）依赖具体设备，迁移到新硬件时需重新验证。

### 使用建议

- **快速了解**：读摘要、引言、表 1（五类结构归纳）以及每节开头/总结，可快速掌握全貌。
- **复现**：查 GitHub 仓库代码集合，以及论文图 2-7（ShuffleNet/MobileNet/SeaFormer/单分支/双分支结构图），这些是搭网络的积木。
- **借鉴创新点**：
    - **设计新网络**：学习**双分支解耦**与**特征共享**思想，以及如何平衡"轻量解码器 + 强编码器"（单分支）vs"双路解耦 + 高效融合"（双分支）。
    - **写论文**：用本文五类框架组织 related work，引用其"同设备公平比较"理念与评价体系。
- **写 related work**：归入"实时语义分割综述 / 高效语义分割网络设计"类引用，是该领域全面且较新的中文综述参考。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[F_图像分割_语义_实例_全景]]
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
计算机视觉领域的**实时语义分割综述**。系统梳理并归纳基于深度学习的实时语义分割算法，解决在资源受限场景（自动驾驶、辅助医疗、移动/边缘设备）下如何实现快速且准确的像素级场景理解。作者来自华中科技大学（桑农团队）与美团，发表于《中国图象图形学报》2024 年第 29 卷第 5 期 (pp.1119-1145)。主题归于 **F_图像分割_语义_实例_全景**（专注语义分割的实时化），兼具 **R_综述_Survey** 属性。

## 2. 一句话总结
本文从模型压缩与高效模块两大前置技术出发，将现有实时语义分割方法按网络结构归纳为单分支、双分支、多分支、U 型、NAS 五大类（涵盖 CNN / Transformer / 混合架构），并建立"同设备公平比较"的数据集 + 指标评价体系，为平衡分割精度与推理速度提供统一的研究路线图。

## 3. 背景与问题
- **为什么要做**：FCN 之后 CNN 成为分割主范式，ViT/SETR/PVT/SegFormer/Swin 等进一步刷新精度，但高分辨率下延迟显著；尤其自注意力与图像分辨率呈**平方复杂度**，难以满足移动端、自动驾驶、人机交互的实时（≥30 帧/s）需求。
- **之前方法的问题**：高精度的两大代价——保留高分辨率底层特征图（空间细节）极大增加计算量；设计复杂模块捕获多尺度上下文与长距离依赖增加推理延迟。
- **核心矛盾**：以更少计算代价、同时保留更丰富空间信息并捕获更有效多尺度上下文，得到更好的速度—精度平衡；移动/边缘设备上还需兼顾模型大小与内存占用。

## 4. 核心贡献
1.  **系统梳理前置技术**：四类模型压缩（剪枝、NAS、知识蒸馏、量化）+ 高效 CNN 模块（ShuffleNet、MobileNet、EfficientNet）+ 高效 Transformer 模块（外部注意力 EA、SeaFormer、MobileViT）。
2.  **五类分类框架**：单分支 / 双分支 / 多分支 / U 型 / NAS，涵盖 CNN/Transformer/混合架构，分析各类特点与局限，并按框架类型、应用场景类型再分类。
3.  **统一评价体系**：数据集分自动驾驶/通用两类，指标分精度指标 + 效率描述符（mIoU、FPS、Params、FLOPs），主张同设备同配置公平比较。
4.  **开源资源库**：`github.com/xzz777/Awesome-Real-time-Semantic-Segmentation`。

## 5. 方法详解
本篇为综述，"方法"在于系统性介绍与分类归纳。整体结构（图 1）：引言 → 前置知识 → 方法分类 → 评价体系 → 结语。

**前置知识**
- **模型压缩**：剪枝（训大网络→评估参数重要性→剪枝→微调）；NAS（搜索空间 + 搜索策略，可纳入精度/延迟指标）；知识蒸馏（教师监督学生）；量化（降数字精度加速）。
- **高效 CNN 模块**：ShuffleNet（分组卷积 + 通道洗牌；V2 用通道划分替代分组卷积）；MobileNet（深度可分离卷积；V2 倒置残差 + 线性瓶颈 + ReLU6；V3 加 SE + h-swish + 网络搜索）；EfficientNet（深度/宽度/分辨率复合缩放；V2 改进 V3 模块 + 非均匀缩放 + 渐进式输入）。
- **高效 Transformer 模块**：外部注意力 EA（Key/Value → 可学习外部参数 Mk/Mv，DoubleNorm 归一化，复杂度 O(H²W²)→O(HW)）；SeaFormer（轴向压缩增强注意力，宽高方向压缩 Q/K/V，深度可分离卷积补偿局部信息）；另提 MobileViT/MobileFormer/EdgeViT（实时分割应用较少）。

**方法分类（五类）**
- **单分支**（单支层级编码器 + 轻量解码器）：① 单尺度轻量解码器 = ENet（最早实时网络，早期下采样 + 轻量非对称解码器，借鉴 SegNet 保存池化索引）；② 多尺度轻量解码器 = SegFormer（首个实时 Transformer，K/V 下采样降复杂度 O(N²)→O(N²/R)，MLP 解码器）、SegNext（仅用阶段 2-4 特征，MSCA 多尺度卷积注意力模拟自注意力，性能超 SegFormer）；③ 无解码器 = DABNet（DAB 模块：3×3 + 条纹卷积 + 条纹空洞卷积，最小分辨率 1/8）、AFFormer（自适应频率滤波器 AFF 替换自注意力，PL/PD 双支，分辨率 1/8）。
- **双分支**（解耦空间细节 + 语义上下文）：① 解耦双分支 = BiSeNet（空间路径 + 上下文路径 + FFM 融合）、BiSeNetV2（Stem/聚合拓展/上下文表征模块 + 双向引导聚合）、STDC（STDC 模块多感受野，空间路径仅 stage3 + 细节头边缘监督、推理时不计算）；② 特征共享双分支 = Fast-SCNN（学习下采样共享早期层）、DDRNet（浅层共享、深层高低分辨率双支，逐阶段双边融合 + DAPPM）、RTFormer（DDRNet 框架 + 双分辨率 RTFormer 模块，低分辨率自注意力 / 高分辨率跨注意力，GPU 友好注意力 + 逐步融合）、SeaFormer（混合 Transformer-CNN，单边融合 + 大量 MobileNetV2，移动端速度-精度最优）。
- **多分支**（多独立分支/多子网/多分辨率输入，表 2）：ICNet（首个多分支，多分辨率级联 + CCF + 多分辨率真值监督）、ESPNet（ESP 空间金字塔 + HFF 分层融合，子网共享浅层故参数量小）、DFANet（额外子网精炼多尺度特征）、PIDNet（浅层共享、深层独立）。
- **U 型 / NAS**：详见提取缓存未覆盖的 p.13-14（U 型网络示意图 Fig.8；NAS 表 Table 3 含 DF-Seg、FasterSeg、RT-Seg）。

**差异点**：系统性 + 时效性，首次从网络结构角度统一组织 CNN/Transformer/混合方法。

## 6. 实验与结果
- **数据集**：分自动驾驶场景 / 通用场景两类。提取文本确认 Cityscapes（含约 5000 幅精细标注图像——据原文后续页 p.16，提取缓存未覆盖，待核）；完整汇总见 p.17 Table 5（未覆盖）。CamVid/ADE20K 等"PDF 文本未明确"。
- **对比方法**：五类共数十种方法，完整清单见 p.16 Table 4（按 Desktop/Mobile GPU、Mobile CPU 分设备；未覆盖）。
- **评价指标**：精度指标 = mIoU；效率描述符 = FPS、Params、FLOPs。汇总见 p.18 Fig.11（未覆盖）。
- **主实验结果**：同设备公平比较见 p.19 Table 6 (Cityscapes)。据原文 p.18 摘录，有方法在 Cityscapes 测试集达 80.6% mIoU、并出现 80.9% mIoU；RTFormer-B 达 82.5% mIoU、RTFormer-S 亦给出数值（据原文后续页，提取缓存未覆盖，待核）。提取文本（前 12 页）本身不含性能表。
- **消融**：综述不做消融，转为模块设计效果的归纳分析。
- **效率信息**：强调同设备同配置比较速度/Params/FLOPs；具体数据在提取缓存（前 12 页）未出现。

## 7. 这篇论文真正有价值的地方
1.  **结构化分类抓住设计本质**：五类划分对应"空间细节 vs 上下文 vs 计算预算"的核心抉择，"解耦双分支 → 特征共享双分支"演化主线（BiSeNet→Fast-SCNN→DDRNet→RTFormer→SeaFormer）尤为清晰。
2.  **算子—架构双层视角**：先讲模型压缩与高效模块，再讲架构，呈现"高效算子 × 合理架构"的完整逻辑。
3.  **同设备公平比较**：直击 FPS 因硬件/分辨率/精度/后处理而不可比的痛点，是综述少见的实证贡献。
4.  **面向未来**：展望 Transformer 利用、边缘部署、视觉基础模型知识迁移、评价指标多样化、数据集多样化、多模态/弱监督、增量学习等方向 + 开源资源库。

## 8. 局限与问题
- **提取覆盖局限（笔记层面）**：U 型/NAS 详细方法、完整实验表 (Table 4/5/6)、指标图 (Fig.11)、结论展望位于提取缓存未覆盖页，数字均标"待核"。
- **时效性（论文层面）**：收稿 2023-09，截止 2023 年左右，2024 年后工作可能未涵盖。
- **分类边界主观**：论文自述"按最重要贡献归类"，如 SeaFormer 横跨高效 Transformer 模块与特征共享双分支两类。
- **深度有限**：综述不能替代原文精读。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + 表 1 + 各节开头/总结。
- **复现**：GitHub 仓库 + 图 2-7 结构图。
- **借鉴**：设计新网络时学双分支解耦/特征共享思想与"轻量解码器 + 强编码器"权衡；写论文用五类框架组织 related work、引用同设备公平比较理念。
- **related work**：归入"实时语义分割综述 / 高效语义分割网络设计"引用。

## 10. 和其他论文的关系
- **覆盖的代表方法**：
    - **BiSeNet / BiSeNetV2**：解耦双分支开山与改进。
    - **STDC**：双分支计算成本优化（细节头边缘监督）。
    - **Fast-SCNN / DDRNet / RTFormer**：特征共享双分支演化，RTFormer 引入 GPU 友好注意力。
    - **SeaFormer**：混合 Transformer-CNN 双分支，移动端代表。
    - **SegFormer / SegNext**：单分支多尺度轻量解码器（SegFormer 为首个实时 Transformer）。
    - **ENet / DABNet / AFFormer**：单分支（单尺度解码器 / 无解码器）代表。
    - **ICNet / ESPNet / DFANet / PIDNet**：多分支代表。
    - **MobileNet 系列 / ShuffleNet / EfficientNet**：高效 CNN 模块基础积木。
- **互补/对比**：可与专注子领域（Transformer 分割、知识蒸馏分割）的综述互补；其五类框架可用于定位与对比新发表的实时分割方法。

## 11. 关键词
实时语义分割, 模型轻量化, 高效模块设计, 计算机视觉, 深度学习, 网络结构分类, 单分支网络, 双分支网络, 多分支网络, U 型网络, 神经架构搜索, 速度-精度平衡, 模型压缩, CNN, Transformer, 综述

## 12. 可信度说明
本精读主要基于 **PDF 提取文本（前 12 页，约 2086 字符/页，质量良好）**，覆盖摘要、引言、前置知识（模型压缩 + 高效 CNN/Transformer 模块）以及方法分类中**单分支、双分支、多分支**三类的大部分内容；对这些部分的总结忠实于原文。

**受提取覆盖所限**，以下内容来自原文后续页（提取缓存未覆盖），笔记中已逐处标注"待核"或"PDF 文本未明确"：
1.  U 型网络、神经架构搜索网络的详细方法（p.13-14，Fig.8 / Table 3）。
2.  完整实验结果（数据集 Table 5、方法汇总 Table 4、Cityscapes 性能 Table 6、指标图 Fig.11，以及 80.6%/80.9%/82.5% mIoU 等具体数字）。
3.  结论与未来展望的具体细节（英文摘要已概述方向）。

---

> **可信度补充**: PDF 提取质量 = **high** (前 12 页, 约 2086 字符/页); 来源缓存: `.paper-cache/extracts/cjig_图像识别_深度学习实时语义分割综述_完整版.txt` (提取 12/27 页; 全文补读记录补足 p.13-27 线索); 摘要已据提取文本重建 (英文清理 + 中文原文); 分类核对: F_图像分割_语义_实例_全景 (+ R_综述_Survey) 维持; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-27; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-27。
- **提取情况**: 缺失页 15 页, 其中 15 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: Table 3 Overview of neural architecture search networks in real -time segmentation
- p.14: DF-Seg
- p.14: Faster Seg
- p.14: RT-Seg
- p.16: Table 4 Overview of real -time semantic segmentation methods
- p.16: Transformer
- p.16: Hybrid
- p.16: Desk/Mobile GPU
- p.16: Desk GPU
- p.16: Mobile CPU
- p.16: Mobile GPU
- p.16: Arxiv

### 缺失页关键摘录

- p.13: Fig.8 Schematic diagram of the U -shape real -time semantic segmentation network1131
- p.14: operations per second ， FLOPs ）评价实时模型的轻量
- p.14: Table 3 Overview of neural architecture search networks in real -time segmentation
- p.15: Fig.10 Overview of different frameworks of real -time
- p.16: cityscapes -dataset .com/） 。Cityscapes 有5 000幅精细
- p.16: Table 4 Overview of real -time semantic segmentation methods
- p.17: Table 5 Summary of the datasets in real -time semantic segmentation
- p.18: 算数（floating point operations ，FLOPs ） ，但由于浮点
- p.18: 80.9% mIoU ，在Cityscape 测 试 集 上 达 到 了 80.6%
- p.18: RTFormer -B达到了 82.5% mIoU ，RTFormer -S达到了
- p.18: Fig.11 Summary of the metrics of real -time segmentation1136
- p.19: Table 6 Comparison of the performance on Cityscapes dataset
<!-- AI_READING_NOTE_END -->
