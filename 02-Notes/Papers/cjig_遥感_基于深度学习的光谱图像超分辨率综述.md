---
title: Zhang T Wang B F Fu Y Liu S R Ye J C Shan P H and Yan C G. 2024. Deep learningbased spectral image superresolution a
authors:
  - "张涛"
  - "王彬沣"
  - "付莹"
  - "刘松荣"
  - "叶吉超"
  - "单培红"
  - "颜成钢"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.230747
pdf: [[cjig_遥感_基于深度学习的光谱图像超分辨率综述.pdf]]
primary_topic: R_综述_Survey
topics:
  - "R_综述_Survey"
  - "E_图像复原_超分_去噪_去雨去雾"
  - "R1_遥感_高光谱_变化检测"
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
extract_cache: .paper-cache/extracts/cjig_遥感_基于深度学习的光谱图像超分辨率综述.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/24 pages"
---
# 基于深度学习的光谱图像超分辨率综述 (Deep learning-based spectral image super-resolution: a survey)

## 基本信息
- **PDF**: [[cjig_遥感_基于深度学习的光谱图像超分辨率综述.pdf]]
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`, `E_图像复原_超分_去噪_去雨去雾`, `R1_遥感_高光谱_变化检测`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Deep learning-based spectral image super-resolution: a survey (基于深度学习的光谱图像超分辨率综述) |
| **作者** | 张涛; 王彬沣; 付莹(通信作者); 刘松荣; 叶吉超; 单培红; 颜成钢 |
| **单位** | 杭州电子科技大学; 北京理工大学; 浙江交投; 国网浙江; 浙江公众信息 |
| **发表时间** | 2024, Vol.29 No.8, pp.2113-2136 |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics) |
| **DOI** | 10.11834/jig.230747 |
| **代码/资源** | https://github.com/ColinTaoZhang/DL-based-spectral-super-resolution |
| **基金** | 国家自然科学基金 (62171038, 62331006) |

## 摘要

> **英文原文 (据 PDF 提取文本整理, 已修复空格与连字符断裂、剔除混入的图表与版式数字):**
>
> The goal of spectral image super-resolution technology is to recover images with high spatial resolution and spectral resolution from images with low spatial resolution and spectral resolution. Images of high spatial and spectral resolution are widely used in remote sensing fields such as vegetation survey, geological exploration, environmental protection, anomaly detection, and target tracking. With the rise of deep learning, spectral image super-resolution algorithms based on deep learning have emerged. In particular, the emergence of technologies such as end-to-end neural networks, generative adversarial networks, and deep unfolding networks has made a qualitative leap in spectral image super-resolution performance. This study comprehensively discusses and analyzes cutting-edge deep learning algorithms under different spectral image super-resolution task scenarios. First, we introduce the basic concepts of spectral image super-resolution and the definitions of different super-resolution scenarios. Focusing on the two major scenarios of single-image super-resolution and fusion super-resolution, the basic concepts of various methods are elaborated from multiple perspectives such as super-resolution dimensions, data types, basic frameworks, and supervision methods. Second, this study summarizes the limitations of various algorithms and proposes directions for further improvement. Furthermore, the commonly used datasets in different fusion scenarios are briefly introduced, and the specific definitions of various evaluation indicators are clarified. For each super-resolution task, this study comprehensively compares the performance of representative algorithms from qualitative and quantitative perspectives. Finally, this study summarizes the research results and discusses some serious challenges faced in the field, while also looking forward to possible future research directions. The methods and datasets mentioned are linked at the GitHub repository above.

> **中文翻译 (对应原刊中文摘要):**
>
> 光谱图像超分辨率技术的目的是从低空间分辨率和低光谱分辨率的图像中恢复出高空间分辨率和高光谱分辨率的图像，在植被调查、地质勘探、环境保护、异常检测和目标追踪等遥感领域有着广泛应用。随着深度学习的兴起，基于深度学习的光谱图像超分辨率算法如雨后春笋般涌现，特别是卷积神经网络、Transformer、生成对抗网络以及深度展开网络等技术的出现，使图像融合性能产生了质的飞跃。本文全面探讨和分析了不同光谱图像超分辨率任务场景下的前沿深度学习算法。首先，介绍了光谱图像超分辨率的基本概念以及不同超分辨率场景的定义。针对单图超分辨率和融合超分辨率两大场景，从超分辨率维度、数据类型、基本框架和监督方式等多个角度详细阐述了各类方法的基本思想和特点。其次，总结了各类算法存在的局限性，并提出了进一步改进的方向。然后，简要介绍了不同融合场景中常用的数据集，并明确了各种评估指标的具体定义。对于每种超分辨率任务，从定性评估、定量评估等多个角度全面比较了代表性算法的性能。最后，总结研究结果，探讨了该领域面临的严峻挑战，并对未来可能的研究方向进行了展望。

> **关键词**: 深度学习; 超分辨率; 光谱图像; 单图超分辨率; 融合超分辨率
>
> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：光谱图像由数十至数百个连续光谱波段组成，能解决彩色图像无法区分的"同色异谱"问题，在植被调查、地质勘探、环境保护、异常检测、目标追踪等遥感领域应用广泛。但受信噪比和成像时间限制，传感器必须在空间分辨率与光谱分辨率之间权衡：高光谱图像光谱分辨率高、空间分辨率低（导致空间混叠、地物混合于同一像素而信息丢失）；多光谱/全色图像空间分辨率高、光谱分辨率低（难以区分形状相似的目标）。直接提升光学器件与传感器精度成本极高，因此用计算方法（超分辨率）提升分辨率是降低成本的有效途径。
- **之前方法的问题**：在深度学习普及前，光谱超分已被深入研究——最基础是相邻像素非线性插值（双线性、双三次，Li 和 Orchard, 2001），但易导致边缘模糊和振铃效应；传统方法则通过挖掘高维数据相关性/冗余性、引入手工先验（**稀疏性**：Dian 等 2017、Li 等 2018 等；**低秩性**：Wang 等 2017、Fu 等 2018a 等）构建优化模型。这类方法存在两大痛点：1) 需求解目标函数，**恢复速度很慢**；2) 稀疏性、低秩性等**手工先验难以完整表达现实世界复杂的光谱数据**。
- **核心矛盾**：如何在高效计算的同时，更完整、更自适应地学习并表达光谱图像中复杂的空间—光谱关联性，以实现高质量的超分辨率重建。深度学习凭借强大的数据特征表达能力（已在图像分类、目标检测、语义分割、图像增强等任务取得成功）被引入该领域，主要学习低分辨率与高分辨率图像之间的非线性映射关系。

## 关键贡献

1.  **系统性分类框架**：提出清晰的光谱图像超分辨率任务分类体系。按输入分为**光谱单图超分辨率（SSISR）**与**光谱融合超分辨率（FSISR）**；SSISR 按超分方向再分为空间（SpaSR）、光谱（SpeSR）和空间—光谱（SSSR）超分辨率；FSISR 按融合模态分为全色光谱融合（PS, pansharpening）和多光谱高光谱融合（MHF）。
2.  **方法论综述**：按网络架构（端到端网络 E2EN、生成对抗网络 GAN、深度展开网络 DUN）和监督范式（有监督、无监督）两个维度，全面介绍各场景下代表性深度学习方法的基本思想与特点。
3.  **光谱超分与自然图像超分的区别辨析**：明确指出二者三点核心差异——数据类型更广（高光谱/多光谱/彩色/灰度 vs 彩色/灰度）、超分维度更多（同时关注空间、光谱、空间—光谱 vs 仅空间）、融合输入模态差异更大（不同模态 vs 同模态同分辨率）。
4.  **局限性与方向总结**：明确总结现有算法局限性并提出改进方向。
5.  **评估体系介绍**：介绍不同任务常用数据集，并给出全参考指标（PSNR、SSIM、SAM、ERGAS）和无参考指标的具体定义。
6.  **性能全面比较与未来展望**：对每种超分任务从定性、定量多角度全面比较代表性算法，并探讨严峻挑战与未来方向（高质量数据集、模型驱动与深度学习结合、实时超分、全面评估指标）。

## 方法

本文是综述论文，未提出新方法，但系统梳理了现有方法。以下按其分类框架详解（其中 SSISR 全部子方向已在提取文本中完整覆盖；FSISR 在 1.2.2 节末被提取缓存截断）。

- **整体三维分类框架**：
    - **任务维度**：SSISR（单图） vs. FSISR（融合）。
    - **网络架构维度**：E2EN-based（端到端，按基本计算单元再分 CNN-based / Transformer-based，也有 Du 等 2023 将二者结合）、GAN-based（生成器与判别器博弈）、DUN-based（将传统优化迭代步骤展开为网络，由线性计算单元对应数据保真项、非线性计算单元对应先验项，先验项一般用 CNN/Transformer 实现）。
    - **监督范式维度**：有监督（最小化超分结果与真值之间的距离） vs. 无监督（通过超分与输入图像的相似性、或生成器—判别器博弈设计损失）。

- **单图超分辨率（SSISR）详解**：
    - **空间超分辨率 (SpaSR, 1.1.1)**：将低空间分辨率输入转为高空间分辨率输出，不涉及光谱信息增加；分为 E2EN-based 与 GAN-based 两类。核心挑战是**保留光谱特征**——直接迁移自然图像 SR 会产生严重光谱失真。代表技术：3D 卷积同时挖掘空间与波段相关性以减轻失真（Mei 等 2017，即 3D-FCNN）；空间约束+深度谱差 CNN（Li 等 2017b, SDCNN）；多尺度小波 3D-CNN 预测小波系数（Yang 等 2019）；2D/3D 混合卷积与可分离卷积降算量（Li 等 2020c, MCNet）；隐式神经表示 INR 连续映射空间坐标到光谱值（Zhang 等 2023b）；引入光谱注意力并结合空间残差（Jiang 等 2020, SSPSR）、协方差统计构造的光谱注意力（Liu 等 2021）；从序列角度用循环网络建模全局光谱相关性（Fu 等 2021, Bi3DQRNN; Wang 等 2022, RFSR）；双注意力 Transformer 分别建模长距空间与全局光谱相关性（Long 等 2023, DSSTSR）、光谱相关系数构建高效 Transformer（Zhang 等 2023c, ESSAformer）；GAN 路线则结合 3D 卷积与注意力保留光谱（Dou 等 2020, 3DASRGAN）、局部+全局注意力 GAN（Li 等 2022b, SRAGAN）、以及把光谱图像视为潜在空间高维流形、用潜在编码器耦合 GAN 缓解模式崩溃（Shi 等 2022, LE-GAN）。
    - **光谱超分辨率 (SpeSR, 1.1.2)**：从高分辨率 RGB/多光谱图像重建高光谱图像，主流是端到端 CNN。代表技术：先光谱维插值上采样再 CNN 增强（Xiong 等 2017, HSCNN）；利用**相机光谱响应先验**构建自适应权重注意力（Li 等 2020b, AWAN）；像素感知深度函数混合网络（Zhang 等 2020a, PDFN）；引入**图像语义信息作为先验**且无监督训练（Zhu 等 2021c, SEN），并在此基础上加注意力与二阶先验（Wu 等 2023, HPRN）；光谱维度多头自注意力的多阶段 Transformer（Cai 等 2022, MST++）、双光谱维自注意力+掩膜引导通道增强（Li 等 2023b, MFormer）；DUN 路线提升可解释性：受梯度下降启发、单次训练适配不同相机光谱响应（Zhu 等 2021b, DAGDN）、基于半二次分裂法+跨维通道注意力（He 等 2022, PoNet）；GAN 路线用条件 GAN（Lore 等 2019, GANSSR）与空谱特征注意力+光谱角映射损失（Liu 等 2023, SSFAN）。
    - **空间—光谱超分辨率 (SSSR, 1.1.3)**：同时提升空间与光谱分辨率。Mei 等（2020, SSJSR）**首次**用 CNN 联合改进二者，并讨论了"同时联合"与"顺序分离"两种空谱超分策略的影响；后续工作常将空间 SR 与光谱 SR 设计为相互促进的辅助任务（Ma 等 2022b, SSFIN；Ma 等 2021, US3RN 用交替乘子法 ADMM 封闭求解两个子问题；Zhang 等 2023a, INRJSR 将 INR 用于空谱超分）。

- **融合超分辨率（FSISR）详解**：
    - **全色光谱融合 (PS / pansharpening, 1.2.1)**：融合全色图像（高空间、低光谱）与多光谱图像（低空间、高光谱）。深度学习首次引入是 Masi 等（2016）用 3 层卷积融合。代表技术：在**高频域**而非图像域训练以保留空谱特征（Yang 等 2017）；多尺度卷积+残差（Yuan 等 2018）；用**深度光谱先验**上采样（Zheng 等 2020）；模态感知特征空间互信息最小化以鼓励互补信息（Zhou 等 2022c）；探索**空间—频率域交互**的空频信息集成网络（Zhou 等 2022d, 2022b）；上下文感知引导注意力的交叉反馈密集网络（Dong 等 2022a）；Transformer 路线（Meng 等 2022 通道拼接后输入 Transformer；Xu 等 2022 分别提特征再拼接；Bandara 和 Patel 2022 / Zhou 等 2022a 用查询—键机制跨模态转移纹理）；DUN 路线融合模型驱动与数据驱动（Xu 等 2021 迭代求解；Cao 等 2022a/b 用卷积稀疏编码+近端梯度展开；Yang 等 2022 去噪先验+非局部自回归变分模型；Qu 等 2023 把半二次分裂迭代展开为生成双对抗网络，含空间与光谱双判别器）；无监督/弱监督 GAN（Ma 等 2020 无监督、生成器分别与光谱判别器和空间判别器博弈；Xu 等 2023 先生成均值差分图像再由粗到精）。
    - **多光谱高光谱融合 (MHF, 1.2.2)**：融合高空间分辨率多光谱图像与高光谱分辨率高光谱图像。有监督方法注重精细融合网络：渐进式零中心残差网络（Zhu 等 2021a）、外部+内部联合注意力（Guo 等 2022）、高分辨率引导的通用 CNN 框架（Ran 等 2023）、**首次将 Transformer 用于 MHF**（Hu 等 2022a）、金字塔置乱—复原 Transformer PSRT（Deng 等 2023）；可解释性 DUN（Xie 等 2019b/2022 近端梯度展开+光谱低秩；Dong 等 2021/2022b 深度去噪先验/双优化模型驱动；Wang 等 2019 盲融合迭代优化观测模型）。**无监督方法是该场景重点**（难获完美配对高低分辨率图像）：无监督编码器—解码器（Qu 等 2018 首次）、用额外构造的低分辨率多光谱图像辅助学习映射（Fu 等 2019；Zhang 等 2021；Li 等 2022a）、自动编码器框架联合优化（Wang 等 2020）、交叉注意力耦合解混网络（Yao 等 2020）、非负矩阵分解（Liu 等 2022）、**外部—内部学习框架**迁移通用先验再泛化到特定图像（Zhang 等 2019；Fu 等 2022a；Zhang 等 2020b 无监督自适应学习）。
      > 注: 提取缓存在 1.2.2 节末（Li 等 2023a 处）被截断，本节后半及其余 FSISR/实验内容据原文 p.13-24，提取缓存未覆盖，待核。

- **训练/推理范式**：E2EN 直接由 LR 经卷积/Transformer 块输出 HR；GAN 由判别器迫使生成器输出在概率分布上逼近高分辨率目标；DUN 将 ADMM/梯度下降/半二次分裂等迭代步骤展开为网络层（也有方法把预训练网络插入优化算法迭代，如 Lai 等 2022）。有监督用成对 LR-HR 最小化像素级损失（L1/L2）；无监督设计自监督损失（如光谱角约束）或对抗损失。

- **与已有方法的差异**：本文的核心差异不在于提出新方法，而在于**系统性的分类、梳理与比较**——将光谱图像超分辨率作为一个整体研究领域，从任务、数据类型、网络架构、监督方式多维度剖析，并配套开源汇总仓库。

## 实验

- **使用的数据集**：分为单图超分辨率数据集与融合超分辨率数据集。具体数据集名称在提取缓存（前 12 页）中未列出；据原文后续页（Table 3 / Fig.5，提取缓存未覆盖，待核），涉及 **Harvard、Botswana、Chikusei、Pavia University、QuickBird、HypSen** 等。
- **对比方法**：表 1（单图超分研究归纳，提取文本已完整给出）汇总了 40 余个方法，含 SpaSR（3D-FCNN、SDCNN、1D2DCNN、IDN、MW-3D-CNN、DFMF、RIFN、3DASRGAN、MCNet、SSPSR、SFCSR、MMCA、Bi3DQRNN、INR、RFSR、DualSR、SRAGAN、LE-GAN、DSSTSR、ESSAformer）、SpeSR（HSCNN、GANSSR、AWAN、PDFN、SSRAN、DAGDN、SEN、HSACS、SSRN-IPH、SSN、DRCRNet、PoNet、MST++、MFormer、HPRN、CTJN、SSFAN）、SSSR（SSJSR、US3RN、SSFIN、INRJSR），并标注了各方法的场景、基础框架（CNN/GAN/Transformer/DUN）、监督范式与发表期刊/会议。
- **评价指标**：全参考指标包括**峰值信噪比 PSNR**、**结构相似性 SSIM**、**光谱角映射器 SAM**、**相对无量纲全局合成误差 ERGAS**；另介绍了无参考指标。指标定义在原文第 13 页起展开（提取缓存覆盖到 p.13 的 PSNR 定义起始）。
- **主实验结果**：原文"从定性、定量多角度全面比较了代表性算法性能"。具体数字在提取缓存（前 12 页）中未给出；据原文后续页（提取缓存未覆盖，待核）：单图超分结果见 Table 4 / Fig.6（涉及 MCNet、SFCSR、SSPSR 等）；MHF 融合定量结果见 Table 5，**UAL 在除 PSNR 外的其他指标上取得最好**（据 p.16 摘录）；全色锐化定量比较见 Table 6 / Fig.8。
- **消融/泛化/效率实验**：提取缓存中未明确说明；综述类论文通常不做统一消融。

## 局限

1.  **实验深度的局限**：作为综述，价值在于梳理而非实验创新。文中性能比较是"综述"式的，可能未在统一基准数据集、统一实验设置（数据划分、降质核）下对所有方法严格对比。
2.  **数据集覆盖**：作者也将"高质量光谱图像超分辨率数据集"列为未来挑战之一，说明现有数据集在规模、真实退化场景覆盖上仍有不足。
3.  **算法筛选主观性**：代表算法的选择与分类标准带有作者主观性，边缘或交叉方法可能未被充分涵盖。
4.  **前沿进展滞后**：受论文发表周期所限（收稿 2023-10，修回 2024-03），更新进展（如扩散模型在光谱超分中的应用）可能未纳入。

## 个人评论

1.  **清晰的"领域地图"**：为初入该领域者提供完整导航。三维分类体系（SSISR/FSISR → SpaSR/SpeSR/SSSR/PS/MHF → E2EN/GAN/DUN → 有监督/无监督）逻辑严密，便于快速建立宏观认知，且配套 GitHub 汇总仓库可直接索引方法与数据集。
2.  **方法论精髓提炼**：不堆砌算法，而是提炼每类任务、每种框架下解决**核心挑战**（光谱失真、空谱关联建模、可解释性、无监督训练）的关键技术思路（3D 卷积、光谱注意力、循环建模、INR、深度展开、自构造监督信号）。
3.  **区别辨析有价值**：明确点出光谱超分与自然图像超分在数据、维度、模态上的三点差异，这是很多入门者容易混淆之处，也解释了"为什么不能直接套用自然图像 SR 网络"。
4.  **指明研究缺口**：通过总结局限与四大未来挑战（高质量数据集、模型驱动+深度学习结合、实时超分、全面评估指标），为后续研究者指明方向。
5.  **可改进之处**：该笔记的实验/数据集细节因提取缓存仅覆盖前 12 页而存在缺口，定量结论（如 UAL、各 Table 数字）需回原文 p.13-24 核对。综述本身的局限在于未给出统一基准的实证对比，读者仍需自行复现关键方法。

### 使用建议

- **快速了解领域**：重点阅读摘要、引言（第 0 节）和结构框架图（图 4），以及各章开头概述段，可快速掌握全貌。
- **深入学习方法**：按兴趣精读第 1 章对应任务（如 1.1.1 空间超分），并对照表 1 追溯具体方法原文。
- **复现研究**：复现价值在于其梳理的具体算法（如 MST++、SSPSR、LE-GAN 等），需找原始论文。
- **借鉴创新点**：学习其分类框架组织自己的相关工作；关注其总结的局限与改进方向（数据集、实时性、可解释性、评估指标）寻找课题。
- **撰写 Related Work**：若涉及光谱图像超分，此综述是极佳的撰写指南，可借鉴其分类方式并引用关键文献。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R_综述_Survey]]
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[R1_遥感_高光谱_变化检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇**综述论文**（发表于《中国图象图形学报》2024, 29(8):2113-2136），系统梳理基于深度学习的**光谱图像超分辨率**算法。它横跨**综述（Survey）**、**图像复原/超分辨率**与**遥感/高光谱**三个维度，但其本质是一篇 survey，故 primary_topic 定为 `R_综述_Survey`。涵盖单图超分辨率（SSISR）和融合超分辨率（FSISR）两大场景，并按网络架构（E2EN/GAN/DUN）与监督范式（有监督/无监督）组织全部方法。

## 2. 一句话总结
本文从超分维度、数据类型、网络架构（端到端/GAN/深度展开）和监督方式四个角度，系统梳理了深度学习提升光谱图像空间和/或光谱分辨率的代表方法、数据集、评估指标、局限与未来挑战。

## 3. 背景与问题
- **为什么做**：光谱图像（数十至数百连续波段）能解决"同色异谱"，广泛用于遥感；但受信噪比与成像时间限制，传感器须在空间分辨率与光谱分辨率间权衡——高光谱图像光谱高/空间低（空间混叠、地物混于一像素），多光谱/全色图像空间高/光谱低（难区分相似目标）。提升硬件成本高昂，故用计算超分降本。
- **之前方法的问题**：传统方法靠手工先验（稀疏性、低秩性）构建优化模型，存在两大痛点——求解目标函数导致**恢复慢**；手工先验**难以完整表达复杂现实光谱数据**。深度学习以强表达能力学习 LR→HR 非线性映射来突破。
- **核心矛盾**：在高效计算的同时，更完整、自适应地建模并表达光谱图像复杂的空间—光谱关联性。

## 4. 核心贡献
1.  **三维分类框架**：SSISR vs FSISR；SSISR 再分 SpaSR/SpeSR/SSSR，FSISR 再分 PS/MHF；正交叠加网络架构（E2EN/GAN/DUN）与监督范式（有监督/无监督）。
2.  **方法论综述**：逐场景介绍代表性方法的基本思想与特点。
3.  **光谱超分 vs 自然图像超分的三点差异辨析**：数据类型更广、超分维度更多、融合输入模态差异更大。
4.  **局限性与改进方向总结**。
5.  **评估体系**：数据集分类 + 全参考（PSNR/SSIM/SAM/ERGAS）与无参考指标定义。
6.  **性能比较与四大未来挑战**：高质量数据集、模型驱动+深度学习结合、实时超分、全面评估指标。

## 5. 方法详解
（综述未提新方法，下按其分类框架梳理；SSISR 三子方向在提取文本中完整覆盖，FSISR 1.2.2 节末被提取缓存截断。）

- **E2EN（端到端）**：按基本计算单元分 CNN-based 与 Transformer-based，也有二者结合（Du 等 2023）。直接学习 LR→HR 非线性映射。
- **GAN**：生成器—判别器博弈，迫使超分结果在概率分布上逼近高分辨率目标；易遇模式崩溃（Shi 等 2022 用潜在空间流形视角+耦合潜在编码器缓解）。
- **DUN（深度展开）**：将传统优化（梯度下降/ADMM/半二次分裂）迭代步骤展开为网络，线性单元对应数据保真项、非线性单元（CNN/Transformer）对应先验项，兼具可解释性与学习能力。

**SSISR**：
- *SpaSR（空间超分，1.1.1）*：核心挑战是保留光谱特征（直接套自然图像 SR 会光谱失真）。技术线：3D 卷积（Mei 2017, 3D-FCNN）、空间约束+谱差 CNN（Li 2017b, SDCNN）、小波 3D-CNN（Yang 2019）、2D/3D 混合卷积降算量（Li 2020c, MCNet）、INR（Zhang 2023b）、光谱注意力+空间残差（Jiang 2020, SSPSR）、循环网络建模序列光谱相关性（Fu 2021, Bi3DQRNN; Wang 2022, RFSR）、双注意力 Transformer（Long 2023, DSSTSR）、光谱相关系数高效 Transformer（Zhang 2023c, ESSAformer）、GAN（Dou 2020, 3DASRGAN; Li 2022b, SRAGAN; Shi 2022, LE-GAN）。
- *SpeSR（光谱超分，1.1.2）*：从 RGB/多光谱重建高光谱，主流 CNN。技术线：光谱插值+CNN 增强（Xiong 2017, HSCNN）、相机光谱响应先验注意力（Li 2020b, AWAN）、函数混合网络（Zhang 2020a, PDFN）、语义先验无监督（Zhu 2021c, SEN; Wu 2023, HPRN）、光谱维 Transformer（Cai 2022, MST++; Li 2023b, MFormer）、DUN（Zhu 2021b, DAGDN; He 2022, PoNet）、GAN（Lore 2019, GANSSR; Liu 2023, SSFAN）。
- *SSSR（空间—光谱超分，1.1.3）*：同时提升空间与光谱。Mei 2020（SSJSR）首次提出，讨论"联合 vs 分离"策略；后续把空间/光谱 SR 设为互助辅助任务（Ma 2022b, SSFIN; Ma 2021, US3RN 用 ADMM 封闭求解; Zhang 2023a, INRJSR）。

**FSISR**：
- *PS（全色光谱融合，1.2.1）*：融合全色（高空间）+多光谱（高光谱）。技术线：高频域训练保特征（Yang 2017）、深度光谱先验上采样（Zheng 2020）、空—频域交互（Zhou 2022d/2022b）、Transformer 查询—键跨模态转移（Bandara & Patel 2022; Zhou 2022a）、DUN（Cao 2022; Yang 2022; Qu 2023 展开为双判别器生成对抗网络）、无监督 GAN（Ma 2020）。
- *MHF（多光谱高光谱融合，1.2.2）*：有监督重精细网络（Guo 2022 外+内注意力；Hu 2022a 首用 Transformer；Deng 2023, PSRT）；**无监督为重点**（难获配对数据）：自构造低分辨率多光谱辅助学习（Fu 2019; Zhang 2021）、自动编码器联合优化（Wang 2020）、外部—内部学习迁移通用先验（Zhang 2019; Fu 2022a）。
  > 注: 提取缓存在 1.2.2 节末截断，此后内容据原文 p.13-24，提取缓存未覆盖，待核。

## 6. 实验与结果
- **数据集**：分单图与融合两类；具体名称提取缓存（前 12 页）未列。据原文后续页（提取缓存未覆盖，待核）涉及 Harvard、Botswana、Chikusei、Pavia University、QuickBird、HypSen 等。
- **对比方法**：表 1 完整汇总 40+ 单图超分方法（含场景、基础框架 CNN/GAN/Transformer/DUN、监督范式、发表期刊会议），代表如 3D-FCNN、SSPSR、MST++、ESSAformer、PoNet、SSJSR 等。
- **评价指标**：全参考 PSNR、SSIM、SAM、ERGAS + 无参考指标；定义在原文第 13 页起展开（提取覆盖到 p.13 PSNR 定义起始）。
- **主结果**：原文从定性、定量多角度比较。具体数字提取缓存未给出；据原文后续页（提取缓存未覆盖，待核）单图结果见 Table 4/Fig.6，MHF 定量结果见 Table 5（UAL 在除 PSNR 外指标最好），全色锐化见 Table 6/Fig.8。
- **消融/泛化/效率**：提取缓存未明确；综述类一般不做统一消融。

## 7. 这篇论文真正有价值的地方
1.  **清晰的领域地图**：三维分类体系逻辑严密，配套 GitHub 汇总仓库可直接索引方法与数据集。
2.  **方法论精髓提炼**：聚焦每类任务/框架解决核心挑战（光谱失真、空谱建模、可解释性、无监督训练）的关键技术思路。
3.  **差异辨析**：明确光谱超分 vs 自然图像超分的三点差异，解释"为何不能直接套用自然图像 SR"。
4.  **指明研究缺口**：四大未来挑战（高质量数据集、模型驱动+DL 结合、实时超分、全面评估指标）。

## 8. 局限与问题
1.  **实验深度局限**：综述式比较，未必在统一基准/设置下严格对比所有方法。
2.  **数据集不足**：作者亦将"高质量数据集"列为未来挑战。
3.  **筛选主观性**：代表算法选择与分类标准带主观性。
4.  **进展滞后**：收稿 2023-10/修回 2024-03，更新进展（如扩散模型）可能未纳入。

## 9. 我该怎么使用这篇论文
- **快速了解领域**：读摘要、引言、图 4 框架及各章概述段。
- **深入学习方法**：按任务精读第 1 章并对照表 1 追溯原文。
- **复现研究**：复现其梳理的具体算法（MST++、SSPSR、LE-GAN 等）。
- **借鉴创新点**：学其分类框架组织自己的相关工作；从其局限找课题。
- **撰写 Related Work**：作为光谱图像超分的撰写指南，借鉴分类方式与关键文献。

## 10. 和其他论文的关系
本文是 survey，横跨超分（E）、遥感高光谱（R1）两个具体方向：
- [[E_图像复原_超分_去噪_去雨去雾]]：光谱超分方法常借鉴自然图像超分网络设计，但需额外处理光谱维度与光谱失真问题。
- [[R1_遥感_高光谱_变化检测]]：本文核心数据对象是遥感高光谱/多光谱图像，与高光谱分类、解混、变化检测等下游任务密切相关。
- 涉及 Transformer 在光谱长程依赖建模中的应用（DSSTSR、MST++、PSRT 等）。
- DUN（深度展开网络）是连接传统优化与深度学习的桥梁，在本文中作为三大框架之一被综述。

## 11. 关键词
深度学习, 超分辨率, 光谱图像, 高光谱图像, 多光谱图像, 单图超分辨率(SSISR), 融合超分辨率(FSISR), 全色锐化(pansharpening), 多光谱高光谱融合(MHF), 生成对抗网络(GAN), Transformer, 深度展开网络(DUN), 遥感图像处理

## 12. 可信度说明
本精读笔记**基于 PDF 提取文本（前 12 页/共 24 页）生成**。该文本完整包含**摘要、引言（第 0 节）、第 1 章"方法"的 SSISR 全部子方向（1.1.1-1.1.3）、FSISR 的 PS（1.2.1）及 MHF（1.2.2）前半**，并完整给出了表 1（单图超分研究归纳）。文本提取质量良好、结构清晰。对于提取缓存未覆盖的内容（具体数据集名称、各 Table 实验数字、评估指标完整定义），笔记中均标注"提取缓存未覆盖, 待核"或"PDF 文本中未明确"，未进行任何编造；其中数据集名称、UAL/Table 编号等线索来自原 AI 全文补读记录（p.13-24），保留并标注待核。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本 2086 字符/页, 结构清晰); 来源缓存: `.paper-cache/extracts/cjig_遥感_基于深度学习的光谱图像超分辨率综述.txt` (提取覆盖 12/24 页; 原 AI 主体 12/24 + 全文补读 13-24); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。注: 本次优化重建了摘要(原为乱码直提)、修正了作者列表(补全付莹/刘松荣/叶吉超)、按提取文本核实并丰富了方法细节、修正 primary_topic 为 R_综述_Survey。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-24; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-24。
- **提取情况**: 缺失页 12 页, 其中 12 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: CCS(xi, yi)
- p.14: Table 3 Overview of spectral image super -resolution datasets
- p.14: Harvard
- p.14: Botswana
- p.14: Chikusei
- p.14: Pavia University
- p.14: QuickBird
- p.14: HypSen
- p.15: Table 4 Results of single image super -resolution
- p.15: MCNet
- p.15: SFCSR
- p.15: SSPSR

### 缺失页关键摘录

- p.13: 2）峰值信噪比 （peak signal -to-noise ratio ，PSNR ）
- p.14: Table 3 Overview of spectral image super -resolution datasets
- p.14: Fig.5 Samples of spectral image dataset2126
- p.15: Table 4 Results of single image super -resolution
- p.15: Fig.6 Results of single image super -resolution visualization2127
- p.16: （Zhou 等，2023 ）进行验证 ，采用 PSNR 、SSIM 、SAM 和
- p.16: 多光谱高光谱融合超分辨率实验的定量结果见表5，UAL 在除 PSNR 外的其他指标上都取得了最好
- p.16: Table 5 Results of multispectral and hyperspectral fusion
- p.16: Fig.7 Visualization results of multispectral and hyperspectral fusion super -resolution 2128
- p.17: Fig.8 Visualization results of pansharpening
- p.17: Table 6 Results of panshapening quantitative comparison
<!-- AI_READING_NOTE_END -->
