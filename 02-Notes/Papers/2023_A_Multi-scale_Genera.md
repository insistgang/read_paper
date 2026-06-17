---
title: A Multi-scale Generalized Shrinkage Threshold
authors:
  - "Yujie Feng"
  - "Yin Yang"
  - "Xiaohong Fan"
  - "Zhengpeng Zhang"
  - "Jianping Zhang"
year: 2023
venue: "IEEETRANSACTIONSONGEOSCIENCEANDREMOTESENSING,EARLYACCESS,NO.XX,FEB.2024,DOI:10.1109/TGRS.2024.3368760 1"
doi: 10.1109/TGRS.2024.3368760
pdf: [[2023_A_Multi-scale_Genera.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
extract_cache: .paper-cache/extracts/2023_A_Multi-scale_Genera.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/16 pages"
---
# A Multi-scale Generalized Shrinkage Threshold

## 基本信息
- **PDF**: [[2023_A_Multi-scale_Genera.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A Multi-scale Generalized Shrinkage Threshold Network for Image Blind Deblurring in Remote Sensing |
| **作者** | Yujie Feng; Yin Yang; Xiaohong Fan; Zhengpeng Zhang; Jianping Zhang（湘潭大学） |
| **发表时间** | 2023（arXiv:2309.07524v2，2024-02-21）|
| **刊物/会议** | IEEE Transactions on Geoscience and Remote Sensing (TGRS), Early Access |
| **DOI** | 10.1109/TGRS.2024.3368760 |

## 摘要

**清理后的英文原摘要**（据 PDF 提取文本整理，修复空格/连字符断裂）：

> Remote sensing images are essential for many applications of the earth's sciences, but their quality can usually be degraded due to limitations in sensor technology and complex imaging environments. To address this, various remote sensing image deblurring methods have been developed to restore sharp and high-quality images from degraded observational data. However, most traditional model-based deblurring methods usually require predefined hand-crafted prior assumptions, which are difficult to handle in complex applications. On the other hand, deep learning-based deblurring methods are often considered as black boxes, lacking transparency and interpretability. In this work, we propose a new blind deblurring learning framework that utilizes alternating iterations of shrinkage thresholds. This framework involves updating blurring kernels and images, with a theoretical foundation in network design. Additionally, we propose a learnable blur kernel proximal mapping module to improve the accuracy of the blur kernel reconstruction. Furthermore, we propose a deep proximal mapping module in the image domain, which combines a generalized shrinkage threshold with a multi-scale prior feature extraction block. This module also incorporates an attention mechanism to learn adaptively the importance of prior information, improving the flexibility and robustness of prior terms, and avoiding limitations similar to hand-crafted image prior terms. Consequently, we design a novel multi-scale generalized shrinkage threshold network (MGSTNet) that focuses specifically on learning deep geometric prior features to enhance image restoration. Experimental results on real and synthetic remote sensing image datasets demonstrate the superiority of our MGSTNet framework compared to existing deblurring methods.

**中文翻译**：

> 遥感图像对地球科学的诸多应用至关重要，但其质量常因传感器技术限制与复杂成像环境而退化。为此，已有多种遥感图像去模糊方法被提出，以从退化观测数据中恢复清晰、高质量的图像。然而，多数传统的基于模型的去模糊方法需要预先设定手工先验假设，在复杂应用中难以处理；而基于深度学习的去模糊方法又常被视为"黑盒"，缺乏透明度与可解释性。本文提出一种新的盲去模糊学习框架，利用收缩阈值的交替迭代来更新模糊核与图像，在网络设计上具有理论基础。此外，我们提出一个可学习的模糊核近端映射模块以提升模糊核重建精度；并在图像域提出一个深度近端映射模块，将广义收缩阈值与多尺度先验特征提取块相结合，同时引入注意力机制自适应学习先验信息的重要性，从而提升先验项的灵活性与鲁棒性，避免类似手工图像先验项的局限。由此设计出一个新颖的多尺度广义收缩阈值网络（MGSTNet），专注于学习深层几何先验特征以增强图像复原。在真实与合成遥感图像数据集上的实验表明，MGSTNet 相较已有去模糊方法具有优越性。

> **索引词**：盲去模糊、广义收缩阈值、多尺度特征空间、交替迭代算法、遥感图像、深度展开网络。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：遥感图像广泛用于目标检测、场景分割、遥感图像融合等任务，但成像硬件限制与复杂成像环境使图像质量退化，进而影响下游算法性能。相比升级设备，图像去模糊是"最经济"的提质手段，因此成为遥感与计算机视觉的热门课题。
- **问题定义**：经典退化模型为 `g = h * u + n`（公式1），其中 `g` 是退化观测图像、`u` 是清晰潜在图像、`h` 是模糊核、`n` 是加性高斯白噪声（AWGN），`*` 为二维卷积。**盲去模糊**需同时从 `g` 估计 `u` 和 `h`，是一个**病态（ill-posed）问题**——存在多组核/清晰图像对都满足公式1，解不唯一。
- **之前方法的问题**：
    1. **传统模型驱动方法**：从贝叶斯/MAP 视角求解，依赖手工几何先验（自相似先验、全变分 TV、梯度先验、稀疏编码先验、超拉普拉斯先验、暗通道先验等）。这些先验固定，难以准确刻画清晰图像与模糊核"特征复杂、几何多样"的本质；算法参数难选，求解计算复杂度高、耗时长。
    2. **纯数据驱动深度学习方法**：用端到端网络学习模糊/清晰图像映射（DeepDeblur、DeblurGAN、RDN、SFNet、MIMO-UNet 等），但端到端"黑盒"设计难以理解网络架构作用，缺乏透明度与可解释性；且多依赖加深/加宽模块来提升性能，框架设计缺乏理性指导。
    3. **扩散模型（Diffusion）**：生成质量与多样性好（DDPM、SR3、DiffIR、HI-Diff 等），但前向/反向多步过程产生时变中间量、破坏单步预条件框架，推理需多步采样，速度慢、计算开销大。
- **核心矛盾**：**恢复精度与可解释性/灵活性之间的权衡**。作者借助模型驱动的**深度展开（deep unfolding）**框架，把 MAP 优化迭代"展开"成网络，将传统优化中固定的变换 `Ψ(·)`、`Φ(·)` 替换为可学习非线性模块 `F(·)`、`G(·)`，既保留优化理论的可解释性，又获得数据驱动的灵活先验。

## 关键贡献

1. 提出基于 MAP 的**端到端可训练且可解释的深度展开框架 MGSTNet**，用于遥感图像盲去模糊；网络建立在模糊核与图像**交替近端梯度迭代（alternating proximal gradient iteration）**的数学优化方案之上。
2. 设计**可学习的模糊核近端映射模块 KPMM**，能学习并过滤模糊核的深层先验信息，显著提升模糊核估计/评估质量。
3. 创建**图像深度近端映射模块 IPMM**，将**广义收缩阈值算子（GST）** 与**多尺度先验特征提取块**结合，并引入**注意力机制**自适应学习先验信息的重要性，从而避免类似手工图像先验项的缺点。
4. 实验表明 MGSTNet 在**不同退化程度**的模糊图像上均能获得优于现有方法的恢复质量。

## 方法

- **整体框架**（Fig.1(a)）：MGSTNet 是基于交替图像/模糊核优化的**迭代式深度展开网络**，由 K 个重建阶段串联。每个阶段含两步：**模糊核重建**与**图像重建**。核心思想是用编码-解码模块与收缩阈值模块，学习图像空间（或核空间）与特征空间之间的表示映射。
- **优化起点**：由 MAP 估计（公式2-5）得到正则化优化问题（公式6）：
  `argmin_{u,h, ∥h∥₁=1} ∥h*u−g∥²₂ + λ₁∥Ψ(u)∥ₚᵖ + λ₂∥Φ(h)∥₁¹`，其中第一项为数据保真项，后两项分别为图像/核先验诱导的正则项，`λ₁=σ₁²/σ₂²`、`λ₂=σ₁²/σ₃²`。将 `Ψ/Φ` 替换为可学习模块 `F(·)/G(·)` 后，问题被拆为两个子问题（公式7 关于核 `h`、公式8 关于图像 `u`）。
- **输入输出**：输入退化模糊图像 `g`，输出恢复的清晰图像 `u` 和估计的模糊核 `h`。
- **关键模块**：
    1. **模糊核重建**（解公式7，两步更新）：
        - **核梯度下降模块 KGDM**（公式11，受 ISTA-Net+ 启发）：用可学习步长 `µ_k` 演化线性重建梯度流，`s_k = h_{k-1} − µ_k · u_{k-1}(−x,−y) * (u_{k-1}*h_{k-1} − g)`。
        - **核近端映射模块 KPMM**（公式12）：`h = s_k + G̃_k(Soft(G_k(s_k), θ₁,k))`。编码器 `G_k(·)` 用 3×3 卷积提取浅层核先验，再接**两个残差通道注意力块 RCAB**（Fig.1(f)）提取并平衡各通道深层核先验；中间用**可学习阈值 θ₁,k 的软阈值算子 Soft(·)**（公式13）稀疏化；解码器 `G̃_k(·)` 用对称结构映射回核空间，并带**长跳跃连接**（Fig.1(c)）。最后加**归一化层**保证物理约束 `h≥0, ∥h∥₁=1`（公式14）。
    2. **图像重建**（解公式8，两步更新）：
        - **图像梯度下降模块 IGDM**（公式17）：用可学习步长 `ρ_k`，`r_k = u_{k-1} − ρ_k · h_k(−x,−y) * (h_k*u_{k-1} − g)`。
        - **图像近端映射模块 IPMM**（公式18）：`u_k = r_k + F̃_k(GST_p(F_k(r_k), θ₂,k))`。`F_k(·)` 为**多尺度先验特征提取块**（融合通道注意力，自适应学习不同尺度特征的重要性），核心是**广义收缩阈值算子 GST_p（解 Lp 非凸正则）**，由此恢复丢失纹理细节、提升精细细节复原（论文同名算子）。
- **模块连接**：各阶段级联，前一阶段 `h_k`、`u_k` 作为下一阶段输入；每阶段内**先更新核 `h_k`，再用更新后的 `h_k` 更新图像 `u_k`**。
- **训练方式**：端到端反向传播训练，所有模块参数与可学习步长（`µ_k, ρ_k`）、阈值（`θ₁,k, θ₂,k`）联合优化；各阶段采用**不共享参数（unshared）** 设计。
- **与已有方法差异**：相比**传统模型方法**，先验为数据驱动而非手工，更灵活；相比**纯数据驱动深度学习**，架构由 MAP 优化迭代严格导出，可解释；相比其他**深度展开网络**（如 ISTA-Net 系列），本文在图像近端映射中额外引入**多尺度先验 + 注意力 + 广义收缩阈值**，更好捕捉图像多尺度几何结构。

## 实验

- **使用数据集**（据原文后续页 p.13-16，提取缓存未覆盖正文，待核）：合成遥感去模糊数据集（含 **AIRS 测试集，约 2000 张图像**），以及真实遥感图像 **Jilin-1（吉林一号）** 与 **Zhuhai-1（珠海一号）** 数据集。退化类型涵盖高斯、广义高斯、平台形（plateau-shaped）等多种模糊。
- **对比方法**（据原文后续页 Table IX / Fig.7 线索，待核）：**TransENet、MHAN、SFNet** 等，作者报告这些方法存在明显失真与伪影，而 MGSTNet 更优。
- **评价指标**：PSNR、SSIM 等图像质量指标（提取缓存内未直接给出指标行，据领域惯例与后续页平均定量评估描述，待核）。
- **主实验结果**：原文称 MGSTNet 相较现有去模糊方法在真实与合成数据上均更优；**具体 PSNR/SSIM 数值在提取缓存（p.1-12）中未覆盖**，落在 p.13-14 的定量表格中（待核）。
- **消融实验 / 效率信息**：提取缓存（p.1-12）未覆盖；据后续页线索存在不同去模糊模型对比表（Table IX），但**具体数值、参数量、FLOPs、推理速度 PDF 文本未明确**。

## 局限

- **空间不变假设**：基础退化模型（公式1）假设模糊为空间不变卷积。真实遥感中常见的**空间变化模糊**（如局部运动模糊）可能超出该模型表达能力。
- **病态性与解不唯一**：盲去模糊本质病态，框架靠学习先验缓解，但**对未见模糊类型/场景的泛化**仍可能下降（论文也将"扩充数据、纳入更多退化类型"列为未来工作）。
- **计算复杂度**：K 个迭代阶段、每阶段含 RCAB、多尺度块、不共享参数，**推理速度/显存开销 PDF 文本未明确**，可能不利于实时应用。
- **本笔记的证据缺口**：提取缓存仅覆盖 p.1-12（摘要、引言、相关工作、方法），**定量实验、消融、结论的具体数值未在提取文本中**，相关结论据后续页线索标注"待核"。

## 个人评论

1. **方法论上的融合范本**：本文系统展示了如何把一个**基于 MAP 的优化问题（公式6）** 经"拆分子问题 → 梯度下降 + 近端映射 → 可学习模块替换固定变换"逐步展开为深度网络（MGSTNet）。这条"优化即架构"的路线，对设计兼具可解释性与数据驱动能力的图像逆问题网络很有参考价值。
2. **模块设计的启发性**：
    - **近端算子的可学习化**：把传统优化中解 ℓ₁/ℓₚ 正则的近端算子用神经模块（KPMM、IPMM）替代，核空间用**软阈值**、图像空间用**广义收缩阈值 GST_p**，是连接优化理论与网络设计的关键桥梁。GST 对应非凸 Lp（0<p<1）正则，比软阈值更能保边、抑制过度收缩。
    - **多尺度 + 注意力**：图像先验模块用多尺度结构 + 通道注意力自适应加权，是融合多粒度信息、提升灵活性的有效设计。
    - **核重建单独建模 + 归一化约束**：把 `∥h∥₁=1, h≥0` 的物理约束显式编进网络，比单纯端到端回归更稳。
3. **可迁移性**：这套"交替迭代优化 + 深度先验学习"框架不限于去模糊，其思想可迁移到去噪、超分、压缩感知、MRI 重建等其他**图像逆问题**（论文相关工作也引用了 ISTA-Net、扩散类重建等同源工作）。

### 使用建议

- **如果快速了解**：读 Abstract + Introduction 末段（4 条贡献）+ Section III-B 框架描述 + Fig.1，即可把握核心思想。
- **如果复现**：精读 Section III（KGDM/KPMM/IGDM/IPMM 的公式9-18 与 Fig.1(c)(d)(f)）；注意 GST_p 算子定义、可学习阈值与步长、RCAB 结构、核归一化层。具体训练细节（损失、优化器、退化合成策略、AIRS/Jilin-1/Zhuhai-1 数据划分）在 p.13 起的实验节（提取缓存未覆盖，需查原文）。
- **如果借鉴创新点**：学习"从公式6到网络架构"的展开思路；借鉴编码器-解码器 + 可学习阈值算子的近端映射结构；借鉴图像先验模块"多尺度特征 + 注意力"的设计。
- **如果写 Related Work**：可归入 1) 遥感图像复原；2) 图像盲去模糊；3) 深度展开/展开网络（ISTA-Net 系列）；4) 基于先验学习的图像复原。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本论文属于**计算机视觉与图像处理 → 图像复原（image restoration）** 领域，具体任务为**遥感图像的盲去模糊（blind deblurring）**：从观测的模糊退化图像 `g` 中同时恢复清晰潜在图像 `u` 与模糊核 `h`。方法路线为**模型驱动的深度展开网络（deep unfolding network）**，把 MAP 优化迭代展开为网络。论文发表于 IEEE Transactions on Geoscience and Remote Sensing（TGRS, Early Access），有明确遥感应用背景。因主体是去模糊这一图像复原子任务，归入主题 **E_图像复原_超分_去噪_去雨去雾** 最贴切。

## 2. 一句话总结
本文提出 MGSTNet（多尺度广义收缩阈值网络）——一个由 MAP 优化交替近端梯度迭代展开而来的可解释深度网络，逐阶段交替更新模糊核与清晰图像，并在图像近端映射中用"多尺度先验 + 注意力 + 广义收缩阈值"学习深层几何先验，实现遥感图像高质量盲去模糊。

## 3. 背景与问题
- **为什么做**：遥感图像服务于目标检测、场景分割、图像融合等，但硬件与环境限制致其退化；去模糊是不换设备就能提质的最经济手段。退化模型 `g = h*u + n`（公式1），盲去模糊需同时估计 `u, h`，因解不唯一而病态。
- **之前方法的问题**：
    1. **传统模型方法**：手工几何先验（自相似/TV/梯度/稀疏编码/超拉普拉斯/暗通道）固定、难刻画几何多样性，参数难选、计算复杂度高。
    2. **纯数据驱动深度学习**：端到端黑盒、缺可解释性，靠加深加宽提升、缺理论指导。
    3. **扩散模型**：质量高但多步采样慢、开销大。
- **核心矛盾**：恢复精度 vs 可解释性/灵活性。作者用深度展开在二者间取平衡。

## 4. 核心贡献
1. 基于 MAP 的端到端可训练、可解释深度展开框架 **MGSTNet**（建立在模糊核与图像交替近端梯度迭代上）。
2. 可学习**模糊核近端映射模块 KPMM**，学习并过滤模糊核深层先验，显著提升核重建质量。
3. 图像深度近端映射模块 **IPMM**：广义收缩阈值算子 + 多尺度先验特征提取块 + 注意力机制，避免手工图像先验缺陷。
4. 实验证明在**不同退化程度**模糊图像上恢复质量优于现有方法。

## 5. 方法详解
- **整体框架**（Fig.1(a)）：K 个串联重建阶段，每阶段含"模糊核重建 + 图像重建"两步；用编码-解码 + 收缩阈值模块学习空间↔特征空间映射。
- **优化推导**：MAP（公式2-5）→ 正则优化（公式6）`argmin_{u,h,∥h∥₁=1} ∥h*u−g∥²₂ + λ₁∥Ψ(u)∥ₚᵖ + λ₂∥Φ(h)∥₁¹`；将固定变换 `Ψ/Φ` 替换为可学习模块 `F/G`，拆为核子问题（公式7）与图像子问题（公式8）。
- **模糊核重建**：
    - **KGDM**（公式11）：可学习步长 `µ_k` 的梯度下降，`s_k = h_{k-1} − µ_k·u_{k-1}(−x,−y)*(u_{k-1}*h_{k-1}−g)`。
    - **KPMM**（公式12）：`h = s_k + G̃_k(Soft(G_k(s_k), θ₁,k))`；`G_k` = 3×3 卷积 + 两个 RCAB（残差通道注意力块，Fig.1(f)）提取深层核先验；软阈值（公式13）用可学习阈值 `θ₁,k`；`G̃_k` 对称解码 + 长跳跃连接；末端归一化保证 `h≥0, ∥h∥₁=1`（公式14）。
- **图像重建**：
    - **IGDM**（公式17）：可学习步长 `ρ_k`，`r_k = u_{k-1} − ρ_k·h_k(−x,−y)*(h_k*u_{k-1}−g)`。
    - **IPMM**（公式18）：`u_k = r_k + F̃_k(GST_p(F_k(r_k), θ₂,k))`；`F_k` 为多尺度先验特征提取块（含通道注意力自适应加权），核心是**广义收缩阈值 GST_p**（解 Lp 非凸正则），恢复纹理与精细细节。
- **阶段衔接**：先更核后更图；各阶段不共享参数；端到端反向传播联合优化所有模块参数、步长与阈值。

## 6. 实验与结果
- **数据集**（据原文后续页 p.13-16，提取缓存未覆盖，待核）：合成遥感去模糊数据集（含 **AIRS 测试集 ~2000 张**）+ 真实遥感 **Jilin-1、Zhuhai-1**；退化含高斯、广义高斯、平台形等多种模糊。
- **对比方法**（据后续页 Table IX / Fig.7 线索，待核）：**TransENet、MHAN、SFNet** 等；论文称这些方法产生明显失真/伪影，MGSTNet 更优。
- **评价指标**：PSNR、SSIM 等（提取缓存 p.1-12 内未给出指标行，据后续页"平均定量评估"描述，待核）。
- **主实验/消融/效率**：原文称在真实与合成数据上全面优于对比方法；**具体 PSNR/SSIM 数值、消融、参数量/FLOPs/速度落在 p.13-14（提取缓存未覆盖），PDF 文本未明确具体数值，待核**。

## 7. 这篇论文真正有价值的地方
1. **"优化即架构"范本**：把 MAP 优化问题（公式6）系统展开为网络，给可解释图像逆问题网络设计提供清晰模板。
2. **近端算子可学习化**：核空间用软阈值、图像空间用广义收缩阈值 GST_p，是连接优化理论（ℓ₁/ℓₚ 正则）与网络设计的桥梁；GST 对应非凸 Lp，比软阈值更保边、抑过收缩。
3. **核 / 图像分别建模 + 物理约束**：核重建显式归一化 `∥h∥₁=1`，图像重建用多尺度 + 注意力，结构有针对性。
4. **可迁移**：框架思想可迁移到去噪、超分、压缩感知、MRI 重建等其他图像逆问题。

## 8. 局限与问题
- **空间不变假设**：公式1为空间不变卷积，难表达真实遥感的空间变化模糊。
- **泛化**：盲去模糊本质病态，对未见模糊类型/场景泛化可能下降（论文将扩充退化类型列为未来工作）。
- **复杂度**：多阶段 + RCAB + 多尺度 + 不共享参数，**速度/显存开销 PDF 文本未明确**。
- **本笔记证据缺口**：提取缓存仅 p.1-12，定量实验/消融/结论的具体数值落在后续页，相关结论标注"待核"。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Introduction 末段贡献 + Section III-B + Fig.1。
- **复现**：精读 Section III（公式9-18、Fig.1(c)(d)(f)）；关注 GST_p 算子、可学习阈值/步长、RCAB、核归一化；训练与数据细节查 p.13 起实验节（提取缓存未覆盖）。
- **借鉴创新点**：优化展开思路；编码器-解码器 + 可学习阈值的近端映射结构；图像先验"多尺度 + 注意力"设计。
- **写 Related Work**：归入 1) 遥感图像复原 2) 图像盲去模糊 3) 深度展开网络（ISTA-Net 系列）4) 先验学习图像复原。

## 10. 和其他论文的关系
- **ISTA-Net / ISTA-Net+ / ISTA-Net++**（Zhang & You [49][50]）：本文 KGDM 明确"受 ISTA-Net+ 启发"，同属基于 ISTA 收缩阈值算法的深度展开，近端映射用可学习模块。
- **RCAN / RCAB**（[64]）：核先验提取器用残差通道注意力块（RCAB）。
- **传统盲去模糊**：Chan(TV)、Krishnan(超拉普拉斯/归一化稀疏)、Zuo(广义迭代收缩)、Pan(暗通道) 等手工先验方法是其对照对象。
- **纯数据驱动**：DeepDeblur、DeblurGAN、RDN/RDB、SFNet、MIMO-UNet 等；**扩散类**：DDPM、SR3、DiffIR、HI-Diff 等。
- **同源展开工作**：Fan 等的几何增量学习、Cui 等的扩散学习 MRI 重建。

## 11. 关键词
- 盲去模糊（blind deblurring）
- 深度展开网络（deep unfolding network）
- 遥感图像复原
- 最大后验概率估计（MAP）
- 交替近端梯度迭代
- 近端映射模块（KPMM / IPMM）
- 广义收缩阈值（GST）/ 软阈值
- 多尺度特征 + 通道注意力（RCAB）
- 模糊核归一化约束 ∥h∥₁=1

## 12. 可信度说明
本精读笔记主体基于 PDF 提取文本的**前 12 页**（摘要、引言、相关工作、方法 Section III 的完整公式推导 1-18）。因此关于**问题背景、核心贡献、方法详解（KGDM/KPMM/IGDM/IPMM、公式6-18、RCAB、GST、核归一化）** 的内容证据充分、可靠。
**实验部分（数据集、对比方法、定量数值、消融、效率）落在 p.13-16，提取缓存（p.1-12）未覆盖**；笔记中 AIRS/Jilin-1/Zhuhai-1、TransENet/MHAN/SFNet、Table IX/Fig.7 等均据原笔记"全文补读记录"中的后续页线索标注"（据原文后续页，提取缓存未覆盖，待核）"，**未编造具体 PSNR/SSIM 数值**。总体：核心创新与方法设计准确可信，定量实验证据需查原文核实。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页); 提取缓存覆盖 p.1-12); 来源缓存: `.paper-cache/extracts/2023_A_Multi-scale_Genera.txt` (12/16 页可读; 实验定量数值在 p.13-16, 据原笔记后续页线索标注待核); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-16; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-16。
- **提取情况**: 缺失页 4 页, 其中 4 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: We skipped the second blur degradation with a probability of
- p.13: The proposed framework is trained using the training
- p.14: TABLE IX
- p.14: COMPARISON OF DIFFERENT DEBLURRING MODELS ON THE
- p.14: Method TransENet MHAN SFNet MGSTNet
- p.14: Gaussian, generalized Gaussian, and plateau-shaped blur, on
- p.14: SFNet all produce obvious distortions and artifacts, whereas
- p.14: Although our approach has achieved excellent performance
- p.14: In this paper, we propose a novel framework for image blind
- p.14: Our future plans involve expanding the capabilities of
- p.14: REFERENCES
- p.15: method for satellite super resolution,” IEEE Transactions on Computa-

### 缺失页关键摘录

- p.13: Fig. 7. Visual comparison of different methods on the Jilin-1 dataset and the Zhuhai-1 datasets.
- p.13: dataset, and its performance is evaluated on both the test
- p.13: dataset and real remote sensing images. The average quan-
- p.14: the AIRS test dataset (2000 images) is presented in Table
- p.14: the Jilin-1 dataset, and the fifth and sixth images come from
- p.14: the Zhuhai-1 dataset. We can see that TransENet, MHAN and
- p.14: evaluations on a synthetic remote sensing deblurred dataset
- p.14: tionally, we aim to augment the dataset by incorporating more
- p.16: scale dataset towards automatic mapping of buildings,” ISPRS journal
- p.16: “Aid: A benchmark data set for performance evaluation of aerial scene
<!-- AI_READING_NOTE_END -->
