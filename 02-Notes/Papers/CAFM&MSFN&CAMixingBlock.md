---
title: "Hybrid Convolutional and Attention Network for Hyperspectral Image Denoising"
authors:
  - "Shuai Hu"
  - "Feng Gao"
  - "Xiaowei Zhou"
  - "Junyu Dong"
  - "Qian Du"
year: 2024
venue: "IEEE GRSL (arXiv:2403.10067)"
doi: 
pdf: [[CAFM&MSFN&CAMixingBlock.pdf]]
primary_topic: B_注意力算子模块
topics:
  - "B_注意力算子模块"
status: ai-read
reading_stage: ai-complete
confidence: high
source_basis: pdf-text
date_added: 2026-06-03
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/CAFM&MSFN&CAMixingBlock.txt
---

# Hybrid Convolutional and Attention Network for Hyperspectral Image Denoising

## 基本信息
- **PDF**: [[CAFM&MSFN&CAMixingBlock.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Hybrid Convolutional and Attention Network for Hyperspectral Image Denoising |
| **作者** | Shuai Hu; Feng Gao; Xiaowei Zhou; Junyu Dong; Qian Du（中国海洋大学 / 密西西比州立大学） |
| **发表时间** | 2024（arXiv 2403.10067, 提交于 2024-03-15, eess.IV）|
| **刊物/会议** | IEEE Geoscience and Remote Sensing Letters (letter)，预印本见 arXiv |
| **代码** | https://github.com/summitgao/HCANet |

## 摘要

**清理后英文原摘要（据 PDF 提取文本整理）**:

> Hyperspectral image (HSI) denoising is critical for the effective analysis and interpretation of hyperspectral data. However, simultaneously modeling global and local features is rarely explored to enhance HSI denoising. In this letter, we propose a hybrid convolution and attention network (HCANet), which leverages both the strengths of convolution neural networks (CNNs) and Transformers. To enhance the modeling of both global and local features, we have devised a convolution and attention fusion module aimed at capturing long-range dependencies and neighborhood spectral correlations. Furthermore, to improve multi-scale information aggregation, we design a multi-scale feed-forward network to enhance denoising performance by extracting features at different scales. Experimental results on mainstream HSI datasets demonstrate the rationality and effectiveness of the proposed HCANet. The proposed model is effective in removing various types of complex noise. Our codes are available at https://github.com/summitgao/HCANet.

**中文翻译**:

> 高光谱图像（HSI）去噪对高光谱数据的有效分析与解译至关重要。然而，为提升 HSI 去噪而同时建模全局与局部特征的工作鲜有探索。本文提出一种混合卷积与注意力网络（HCANet），同时发挥卷积神经网络（CNN）与 Transformer 的优势。为增强对全局与局部特征的建模，我们设计了一个卷积与注意力融合模块（CAFM），用于捕获长程依赖与邻域光谱相关性；此外，为改进多尺度信息聚合，我们设计了一个多尺度前馈网络（MSFN），通过提取不同尺度的特征来提升去噪性能。在主流 HSI 数据集上的实验验证了所提 HCANet 的合理性与有效性，该模型能有效去除多种复杂噪声。代码已开源。

> 来源: 据 PDF 提取文本整理。（原自动提取摘要混入了引言第二段 [6]–[9] 的文字，此处已剔除并复原原始摘要。）

## 研究背景与动机

- **为什么要做**：高光谱成像可获取丰富的细粒度光谱信息，广泛用于解混、地物分类等遥感任务。但成像传感器因曝光时间不足、反射能量不够会引入不可避免的混合噪声，降低图像质量、影响后续分析。因此去噪是众多遥感应用预处理阶段不可或缺的关键技术。
- **之前方法的问题**：
    1.  **传统/模型驱动方法**（如低秩 LRMR、全变分、非局部相似性、空间-光谱相关性等）利用先验做优化求解，性能依赖手工先验与真实噪声模型的匹配程度。
    2.  **基于 CNN 的方法**（Maffei 等以噪声水平图为输入、Wang 等基于八度卷积+注意力、Pan 等渐进多尺度聚合 MAFNet）用卷积核建模局部特征，难以捕捉长距离信息交互。
    3.  **基于 Transformer 的方法**借注意力建模全局上下文已取得成功，但若能有效利用局部特征，去噪性能仍可进一步提升。
- **作者点明的两大挑战**（原文 Introduction）：
    1.  局部与全局特征建模的最优混合架构仍是开放问题——卷积捕获局部却丢失长距离交互，卷积+注意力的结合是可行方案。
    2.  Transformer 中前馈网络（FFN）的单尺度特征聚合受限——隐层通道数大时，单尺度 token 聚合难以充分利用丰富的通道表示。
- **核心矛盾**：如何在统一框架内**同时高效建模局部与全局特征**，并用**多尺度信息**增强 FFN，以应对多种复杂混合噪声。

## 关键贡献

> 原文正式列出的贡献为三条：探索 HSI 去噪的全局-局部建模并首次结合卷积与注意力、提出 MSFN、大量实验+开源代码。CAFM 在摘要与方法中被作为核心模块提出，下面据此整理。

1.  **首次结合卷积与注意力机制做 HSI 去噪**：作者称据其所知，这是首个为 HSI 去噪任务结合卷积与注意力机制的工作，显式探索全局与局部特征联合建模这一有挑战的问题。
2.  **卷积注意力融合模块（CAFM）**：并行的局部分支（1×1 卷积 + 通道混洗 + 3×3×3 卷积）与全局分支（通道维自注意力），分别捕获邻域光谱相关性与长程依赖，再逐元素相加融合。
3.  **多尺度前馈网络（MSFN）**：用三条不同步长/膨胀率的并行卷积替代传统单尺度 FFN，无缝提取多尺度特征、抑制多尺度噪声。
4.  **充分实验 + 开源**：在两个基准数据集（ICVL 训练、Pavia 测试）上、单一高斯噪声与五类复杂噪声下与 5 个 SOTA 对比，并开源代码。

## 方法

- **整体框架**（图1）：HCANet 是 **U 型网络**，由若干 **卷积注意力混合块（CAMixing block）** 与跳跃连接、通道拼接（C）、逐元素相加、矩阵乘法等连接构成。每个 CAMixing block 含两部分：CAFM 与 MSFN，且各自前置 LayerNorm。考虑到 3D 卷积虽能综合捕获空间+光谱特征但参数量大，作者用 2D 卷积做通道调整以控制复杂度。
- **输入与输出**：
    - **输入**：带噪高光谱图像 \( I \in \mathbb{R}^{H \times W \times B} \)，先用一个 3×3×3 卷积提取低层特征。
    - **输出**：经 U 型网络得到与输入同形的噪声残差图 \( I_N \in \mathbb{R}^{H \times W \times B} \)，重建干净图像 \( \hat{I} = I + I_N \)。
- **关键模块与连接**：
    1.  **卷积注意力融合模块（CAFM）**（图2）：
        - **局部分支**：1×1 卷积调整通道 → **通道混洗（Channel Shuffle）**（沿通道分组，组内用深度可分离卷积诱导混洗，再沿通道拼接）→ 3×3×3 卷积提取特征。公式 \( F_{conv} = W_{3\times3\times3}(CS(W_{1\times1}(Y))) \)（式1）。
        - **全局分支**：用 1×1 卷积 + 3×3 深度卷积生成 Q、K、V（形状均为 \( \hat{H}\times\hat{W}\times\hat{C} \)）；将 Q 重塑为 \( \hat{Q} \in \mathbb{R}^{\hat{H}\hat{W} \times \hat{C}} \)、K 重塑为 \( \hat{K} \in \mathbb{R}^{\hat{C} \times \hat{H}\hat{W}} \)，计算 **通道维注意力图** \( A \in \mathbb{R}^{\hat{C} \times \hat{C}} \)，从而避免计算 \( \hat{H}\hat{W}\times\hat{H}\hat{W} \) 的巨大常规注意力图、降低计算负担。输出 \( F_{att} = W_{1\times1}\,Attention(\hat{Q},\hat{K},\hat{V}) + Y \)（式2），其中 \( Attention(\hat{Q},\hat{K},\hat{V}) = \hat{V}\,Softmax(\hat{K}\hat{Q}/\alpha) \)（式3），α 为可学习缩放参数，控制 softmax 前矩阵乘的幅度。
        - **融合**：\( F_{out} = F_{att} + F_{conv} \)（式4），两分支逐元素相加。
    2.  **多尺度前馈网络（MSFN）**（图3）：
        - **结构**：两个 1×1 卷积以扩展率 γ=2 扩展通道；输入分两条并行路径，引入门控机制（两路特征逐元素相乘）增强非线性变换。**下路径**用深度卷积/3×3×3 卷积做特征提取；**上路径**用两个膨胀率分别为 2 与 3 的 3×3 膨胀卷积做多尺度特征提取。
        - **公式**：\( Gating(X) = \phi(W_{3\times3\times3}W_{1\times1}(X)) \odot (W^2_{3\times3}W_{1\times1}(X) + W^3_{3\times3}W_{1\times1}(X)) \)（式5），\( X_{out} = W_{1\times1}\,Gating(X) \)（式6）。⊙ 为逐元素相乘，φ 为 GELU 非线性，\( W^2_{3\times3} \)/\( W^3_{3\times3} \) 分别为膨胀率 2/3 的 3×3 膨胀卷积。
        - 注：引言提到 MSFN 用「三条不同步长的并行膨胀卷积」，与图3/式5中「一条 3×3×3 普通卷积 + 两条膨胀卷积」的并行结构对应。MSFN 角色与 CAFM 不同，专注于用上下文信息丰富特征。
- **机制直观解释**：
    - CAFM 并行局部（卷积）与全局（注意力）分支，让模型**同时关注邻域光谱相关性与长程空间-光谱依赖**；通道混洗促进跨通道信息交流。
    - 在**通道维**而非空间维计算注意力（\( \hat{C}\times\hat{C} \) vs \( HW\times HW \)），计算更高效，适合高光谱大通道数场景。
    - MSFN 通过门控将单尺度与多尺度特征非线性融合，利用不同感受野抑制多尺度噪声。
- **训练方式（损失函数）**：
    - 重建损失（L1）：\( L_{rec} = \|\hat{I} - I\|_1 \)（式7）。
    - 全局梯度正则化：\( L_{grad} = \|\nabla_h \hat{I} - \nabla_h I\|_2^2 + \|\nabla_v \hat{I} - \nabla_v I\|_2^2 + \|\nabla_s \hat{I} - \nabla_s I\|_2^2 \)（式8），分别约束水平、垂直、光谱方向梯度，以提升去噪质量并抑制冗余。
    - 总损失 \( L = L_{rec} + \lambda L_{grad} \)（式9），按经验取 λ=0.01。
    - 优化：Adam，初始学习率 \( 10^{-4} \)（随训练逐步衰减），高斯噪声训练 100 epoch、复杂噪声 150 epoch。PyTorch 实现，单卡 NVIDIA GTX 2080Ti（Intel Xeon E5 / 32GB RAM）。
- **推理流程**：带噪 HSI → HCANet → 噪声残差图 \( I_N \) → 与输入相加得 \( \hat{I} \)。
- **和已有方法的差异**：
    - 相比纯 CNN 方法（如 MAFNet），CAFM 引入全局上下文建模。
    - 相比纯 Transformer 方法（如 Restormer），CAFM 的局部分支 + MSFN 的多尺度膨胀卷积显式强化局部特征与多尺度聚合。
    - 相比简单 CNN+Transformer 拼接，并行分支 + 门控融合实现更高效的特征交互。
- **论文类型特化（注意力类）**：
    - **注意力作用维度**：在**通道维**计算注意力图，结合空间卷积（3×3×3），实现空间到通道的交互。
    - **可插入性**：CAFM、MSFN 为模块化设计，可作即插即用组件考虑迁移到其他网络。
    - **计算量 vs 效果**：用通道注意力替代全局空间注意力，在 4.75M 参数 / 11.5 GFLOPS 的中等开销下取得 SOTA 去噪效果。

## 实验

- **数据集**：训练用 **ICVL**（31 个光谱波段，分辨率 1392×1300；随机裁剪为 128×128×31 立方体，旋转+缩放增强后约 20,000 个样本）；测试用 **Pavia** 数据集（真实遥感图像，评估泛化）。
- **噪声设置**：
    - 设置一：高斯噪声 σ=30、50、70 及盲噪声（随机幅度）。
    - 设置二：五类复杂噪声——Case1 各波段随机 σ∈[30,70] 高斯；Case2 高斯+条带（5%~15% 列）；Case3 高斯+死线（1/3 波段，5%~15% 列）；Case4 高斯+脉冲（约 1/3 波段，30%~70% 强度）；Case5 混合噪声（每波段 non-i.i.d 高斯 + 随机叠加其余三类）。
- **对比方法**：模型驱动 BM4D、LRMR、LRTV；深度学习 Restormer、MAFNet（共 5 个 SOTA）。效率表与定性图中还出现 MemNet、HSID-CNN。
- **评价指标**：PSNR（越大越好）、SSIM（越大越好）、SAM（越小越好）。
- **主实验结果**：
    - **单一高斯噪声**（Table I）：HCANet 在 σ=30/50/70/盲 四档下各指标均最优。例：σ=30 PSNR 45.51（MAFNet 43.95、Restormer 42.19）；σ=50 PSNR 44.54（MAFNet 42.13、Restormer 41.51）；σ=70 PSNR 43.27；盲噪声 PSNR 43.97。
    - **五类复杂噪声**（Table II）：HCANet 在所有 case 取得最佳。例：Case5（最难混合噪声）PSNR 40.57，显著高于 MAFNet 37.27、Restormer 36.15；Case4 PSNR 39.99（MAFNet 37.71）。注：个别项 SSIM 上 MAFNet 略高（如 Case5 SSIM MAFNet 0.978 vs Ours 0.963），但 PSNR/SAM 仍以 HCANet 领先。
    - **定性比较**（图4 高斯 σ=50 / 图5 Pavia 真实噪声，波段 17/20/30 假彩色）：传统方法难应对复杂噪声，MAFNet 易过平滑丢细节，Restormer 在复杂噪声下表现差；HCANet 在去噪同时更好保留局部细节与结构。
- **消融实验**（Table III，ICVL，σ=30，epoch=50）：
    - Base model：PSNR 39.94 / SSIM 0.965 / SAM 0.045。
    - +Local branch：42→ PSNR 40.58 / SSIM 0.967 / SAM 0.039。
    - +3D Conv：PSNR 42.23 / SSIM 0.975 / SAM 0.037。
    - +MSFN（全组件）：PSNR 42.68 / SSIM 0.976 / SAM 0.035。逐项验证局部分支、3D 卷积、MSFN 各自有效。
- **效率分析**（Table IV，盲高斯噪声，epoch=50）：HCANet **4.75M 参数 / 11.5 GFLOPS / PSNR 41.21**。对比：MemNet 1.98M/32.41/35.60，HSID-CNN 0.63M/40.80/36.72，MAFNet 20.17M/20.15/40.51，Restormer 14.88M/9.55/40.27。即 HCANet 参数远少于 MAFNet/Restormer，GFLOPS 略高于 Restormer（9.55）但远低于 MAFNet（20.15），且 PSNR 最高，达到精度-效率的良好平衡。

## 局限

- **方法适用场景**：聚焦 HSI 去噪，对超分、去模糊等其他复原任务或其他模态的迁移性未验证。
- **数据集覆盖**：仅 ICVL（训练）与 Pavia（测试）两个数据集，在更多样真实 HSI 上的表现待考察；未讨论对极端方差或特定分布噪声的鲁棒性。
- **计算成本**：3D 卷积与注意力仍有一定开销，资源受限设备部署可能需进一步优化（虽 4.75M 参数已属中等偏低）。
- **假设依赖**：以残差学习方式预测噪声，对与信号高度相关的噪声此假设可能需检验。
- **复现细节**：通道混洗、MSFN 中下路径卷积（深度卷积 / 3×3×3）等描述较概括，下路径在正文（深度卷积）与公式（\(W_{3\times3\times3}\)）/图3（3X3X3Conv）间表述略有出入，复现需仔细参照开源代码。

## 个人评论

1.  **清晰的局部-全局融合范式**：CAFM 用并行「局部卷积分支 + 全局注意力分支」并显式相加，是结合 CNN 与 Transformer 优点的直观、可复用设计；把注意力放在通道维（借鉴 Restormer 的转置注意力思路）以适配高光谱大通道数，是合理工程取舍。
2.  **增强 FFN 的实用做法**：MSFN 用门控（逐元素相乘）将单尺度卷积与膨胀卷积多尺度特征非线性融合，对「FFN 单尺度聚合受限」这一痛点给出轻量解法，可迁移到其他复原任务。
3.  **精度-效率权衡突出**：4.75M 参数、11.5 GFLOPS 即超过 20M 级的 MAFNet 与 14M 级的 Restormer，效率论证（Table IV）是本文较有说服力的一面。
4.  **作为 letter 的局限**：篇幅所限，消融只在 σ=30/单数据集做，注意力维度选择、α 的作用、MSFN 三分支各自贡献等缺少更细的剖析；与同源 MAFNet（同课题组 Pan 等）的关系也值得读者结合代码进一步辨析。

### 使用建议

- **快速了解**：读摘要、引言最后两段（两大挑战 + 提出的方法）、图1（框架）、图2（CAFM），以及 Table I/II 的 Ours 列。
- **复现**：精读第 II 节（CAFM/MSFN 公式与图2/图3）、第 III-A 节（数据准备、五类噪声定义、训练细节），最终以开源代码 https://github.com/summitgao/HCANet 为准。
- **借鉴创新点**：
    - 局部-全局融合：学 CAFM 的并行分支 + 相加融合。
    - 增强 FFN：借鉴 MSFN 的膨胀卷积多尺度聚合 + 门控。
    - 高效注意力：学其重塑 Q/K 在通道维计算注意力以降复杂度。
- **写 related work**：可放在「HSI 去噪的深度学习方法」「CNN 与 Transformer 混合架构」「注意力机制在图像复原中的应用」等小节。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**高光谱图像（HSI）去噪**任务，方法上是**CNN 与 Transformer 混合架构**。其核心创新是两个可复用算子模块：卷积注意力融合模块（CAFM）与多尺度前馈网络（MSFN）。由于本文价值主要在「注意力/卷积融合算子的设计」而非某个具体复原 pipeline，归类于 **B_注意力算子模块** 主题是合理的（任务层面同时与图像复原-去噪强相关）。发表为 IEEE GRSL letter，预印本 arXiv:2403.10067（2024-03）。

## 2. 一句话总结
HCANet 用并行「卷积 + 通道维注意力」融合模块（CAFM）同时建模局部光谱相关性与长程依赖，再用多尺度前馈网络（MSFN）以门控膨胀卷积聚合多尺度特征，在 4.75M 参数的轻量代价下实现 SOTA 高光谱去噪。

## 3. 背景与问题
- **为什么要做**：高光谱成像因曝光不足、反射能量不够会引入混合噪声，损害解混、地物分类等下游任务；去噪是遥感预处理的关键环节。
- **之前方法的问题**：
    1.  传统先验法（低秩、全变分、非局部相似性）性能依赖手工先验与真实噪声的匹配度。
    2.  CNN 法用卷积核建模局部，丢失长距离信息交互。
    3.  Transformer 法擅长全局上下文，但未充分利用局部特征。
- **两大挑战（原文）**：① 局部-全局建模的最优混合架构仍是开放问题；② FFN 的单尺度特征聚合在隐层通道数大时难以充分利用通道表示。
- **核心矛盾**：统一框架内**同时高效建模局部与全局特征**并引入**多尺度信息**，以应对多种复杂混合噪声。

## 4. 核心贡献
1.  据作者所知，**首个为 HSI 去噪结合卷积与注意力机制**的工作，显式探索全局-局部联合建模。
2.  提出 **MSFN**，无缝提取多尺度特征、从多个尺度抑制噪声（原文正式列出的贡献之一）。
3.  在两个基准数据集上做大量实验验证合理性与有效性，并**开源代码**。
4.  （方法核心模块）提出 **CAFM**：并行局部卷积分支 + 全局通道注意力分支，相加融合，兼顾邻域光谱相关性与长程依赖。

## 5. 方法详解
- **整体框架（图1）**：U 型网络 + 若干 CAMixing block + 跳跃连接。先用 3×3×3 卷积取低层特征，经 U 型网络输出与输入同形的噪声残差图 \( I_N \)，重建 \( \hat{I}=I+I_N \)。每个 CAMixing block = LayerNorm→CAFM + LayerNorm→MSFN。为控复杂度，通道调整用 2D 卷积。
- **输入/输出**：输入 \( I \in \mathbb{R}^{H\times W\times B} \)；输出残差 \( I_N \)，最终 \( \hat{I}=I+I_N \)。
- **CAFM（图2，式1–4）**：
    - 局部分支：\( F_{conv}=W_{3\times3\times3}(CS(W_{1\times1}(Y))) \)。通道混洗 = 沿通道分组、组内深度可分离卷积、再沿通道拼接，促进跨通道信息整合。
    - 全局分支：1×1 + 3×3 深度卷积生成 Q/K/V（形状 \( \hat{H}\times\hat{W}\times\hat{C} \)）；重塑 \( \hat{Q}\in\mathbb{R}^{\hat{H}\hat{W}\times\hat{C}} \)、\( \hat{K}\in\mathbb{R}^{\hat{C}\times\hat{H}\hat{W}} \)，得通道维注意力图 \( A\in\mathbb{R}^{\hat{C}\times\hat{C}} \)，避免 \( \hat{H}\hat{W}\times\hat{H}\hat{W} \) 的巨大注意力图。\( F_{att}=W_{1\times1}Attention(\hat{Q},\hat{K},\hat{V})+Y \)，\( Attention=\hat{V}Softmax(\hat{K}\hat{Q}/\alpha) \)，α 可学习缩放。
    - 融合：\( F_{out}=F_{att}+F_{conv} \)。
- **MSFN（图3，式5–6）**：两个 1×1 卷积以 γ=2 扩通道；双并行路径 + 门控（逐元素相乘）。下路径深度/3×3×3 卷积；上路径两条膨胀率 2、3 的 3×3 膨胀卷积。\( Gating(X)=\phi(W_{3\times3\times3}W_{1\times1}(X))\odot(W^2_{3\times3}W_{1\times1}(X)+W^3_{3\times3}W_{1\times1}(X)) \)，\( X_{out}=W_{1\times1}Gating(X) \)，φ=GELU。
- **损失（式7–9）**：\( L_{rec}=\|\hat{I}-I\|_1 \)；\( L_{grad} \) 约束水平/垂直/光谱三方向梯度的 L2；\( L=L_{rec}+\lambda L_{grad} \)，λ=0.01。
- **训练**：Adam，lr=\( 10^{-4} \) 衰减，高斯 100 epoch / 复杂噪声 150 epoch；PyTorch + 单卡 GTX 2080Ti。
- **直观机制**：通道维注意力降复杂度且适配大通道高光谱；局部分支补邻域光谱相关性；MSFN 门控融合不同感受野抑制多尺度噪声。
- **与已有差异**：相比 MAFNet（纯 CNN）补全局；相比 Restormer（纯 Transformer）补局部+多尺度；相比简单拼接，并行分支+门控更高效。
- **注意力类特化**：作用于通道维，结合空间 3×3×3 卷积；模块化可插拔；以通道注意力换取计算效率。

## 6. 实验与结果
- **数据集**：ICVL 训练（31 波段，1392×1300；裁 128×128×31，旋转+缩放增强 ~20,000 样本）；Pavia 测试（真实遥感）。
- **噪声**：高斯 σ=30/50/70/盲；五类复杂噪声 Case1（随机 σ 高斯）/Case2（+条带）/Case3（+死线）/Case4（+脉冲）/Case5（混合）。
- **对比**：BM4D、LRMR、LRTV（模型驱动）+ Restormer、MAFNet（深度学习），共 5 个 SOTA；效率表/图5 另含 MemNet、HSID-CNN。
- **指标**：PSNR↑、SSIM↑、SAM↓。
- **Table I（单高斯）**：HCANet 各档全优。σ=30 PSNR 45.51 / σ=50 44.54 / σ=70 43.27 / 盲 43.97，对应 SSIM 最高 0.981/0.978/0.968/0.978，SAM 最低 0.028/0.033/0.037/0.034。
- **Table II（复杂噪声）**：HCANet 全 case PSNR 最佳，Case1 44.11 / Case2 43.58 / Case3 41.79 / Case4 39.99 / Case5 40.57，普遍领先 MAFNet 与 Restormer（Case5 高出 MAFNet 3.3 dB、Restormer 4.4 dB）；个别 SSIM（Case5）MAFNet 略高。
- **定性（图4/图5）**：传统法难应对复杂噪声，MAFNet 过平滑丢细节，Restormer 复杂噪声差；HCANet 去噪同时保留细节。
- **消融（Table III，σ=30/epoch50）**：Base 39.94 → +Local 40.58 → +3D Conv 42.23 → +MSFN 42.68，逐项有效。
- **效率（Table IV，盲噪声/epoch50）**：HCANet 4.75M / 11.5 GFLOPS / PSNR 41.21；MAFNet 20.17M/20.15/40.51；Restormer 14.88M/9.55/40.27。参数与精度-效率平衡占优。

## 7. 这篇论文真正有价值的地方
1.  **局部-全局融合范式（CAFM）**：并行卷积+通道注意力分支、显式相加，是结合 CNN/Transformer 的直观可复用模板。
2.  **通道维注意力降复杂度**：以 \( \hat{C}\times\hat{C} \) 替代 \( HW\times HW \) 注意力图，特别契合高光谱大通道数场景。
3.  **MSFN 增强 FFN**：门控 + 膨胀卷积多尺度聚合，针对「FFN 单尺度受限」给出轻量解法。
4.  **精度-效率证据扎实**：4.75M 参数即超过 20M/14M 级对手，Table IV 是较有说服力的论证。

## 8. 局限与问题
- **任务/模态单一**：仅验证 HSI 去噪，未涉超分、去模糊等其他复原任务。
- **数据覆盖有限**：仅 ICVL+Pavia，缺更多真实 HSI 与极端噪声的鲁棒性讨论。
- **计算开销**：3D 卷积+注意力在受限设备仍需优化。
- **残差假设**：对与信号强相关的噪声，残差学习假设需检验。
- **描述概括**：通道混洗、MSFN 下路径卷积在正文/公式/图之间表述略有出入，复现宜对照代码。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言末两段 + 图1/图2 + Table I/II 的 Ours 列。
- **复现**：精读第 II 节公式与图2/图3、第 III-A 节实验设置，最终以开源代码为准。
- **借鉴创新点**：局部-全局并行+相加融合（CAFM）；门控膨胀卷积增强 FFN（MSFN）；重塑 Q/K 在通道维算注意力降复杂度。
- **写 related work**：放入「HSI 去噪深度学习方法」「CNN+Transformer 混合架构」「注意力在图像复原中的应用」。

## 10. 和其他论文的关系
- **转置/通道注意力**：CAFM 全局分支的通道维注意力思路与 [[Restormer]] 的转置注意力同源，本文将其用于高光谱去噪。
- **同课题组 HSI 去噪**：[[MAFNet]]（Pan 等，参考[10]，同含 Gao/Dong/Du）是本文主要深度学习对比与多尺度灵感来源。
- **CNN+Transformer 混合**：与 ConvNeXt、CoAtNet 等混合架构思路相通，本文为 HSI 去噪场景的具体设计。
- **传统/低秩去噪**：LRMR、BM4D、LRTV 为本文模型驱动对比基线。

## 11. 关键词
高光谱图像去噪, 混合卷积与注意力网络 HCANet, 卷积注意力融合模块 CAFM, 多尺度前馈网络 MSFN, 通道维注意力, 通道混洗, 膨胀卷积, 门控机制, 残差学习, 图像复原

## 12. 可信度说明
本精读基于 PDF 提取文本（5/5 页，约 25,000 字符，覆盖摘要、引言、方法全部公式、实验设置、Table I–IV、结论与部分参考文献）。
- **提取质量**：高。关键方法公式、五张表格数值、五类噪声定义均完整保留并已逐项核对。
- **已修正项**：原摘要混入引言 [6]–[9] 文字已剔除复原；标题补全为完整题名；对比方法订正为 5 个 SOTA（主定量表为 BM4D/LRMR/LRTV/Restormer/MAFNet，效率表另含 MemNet/HSID-CNN）；补充各档 PSNR、Table IV 全部数值、五类噪声定义、硬件与发表信息（GRSL/arXiv）。
- **存疑项**：MSFN 下路径卷积类型在正文（深度卷积）/公式（\(W_{3\times3\times3}\)）/图3（3X3X3Conv）间表述略异，已如实标注；参考文献列表在提取文本中被截断（原文 25515 字符，仅展示前 25000），不影响正文事实。

---

> **可信度补充**: PDF 提取质量 = **high** (5/5 页, ~5000 字符/页, 文本清晰)；据提取文本逐项核对五张表格与全部公式后修订；来源缓存: `.paper-cache/extracts/CAFM&MSFN&CAMixingBlock.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
