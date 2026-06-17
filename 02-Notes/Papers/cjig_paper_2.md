---
title: Wang Z Huo G L Lan H Hu J M and Wei X. 2024. Fundus image enhancement algorithm based on convolutional dictionary diffu­
authors:
  - "王珍"
  - "霍光磊"
  - "兰海"
  - "胡建民"
  - "魏宪"
year: 2024
venue: 中国图象图形学报 (Journal of Image and Graphics) 29(8):2426-2438
doi: 10.11834/jig.230595
pdf: [[cjig_paper_2.pdf]]
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/cjig_paper_2.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/13 pages"
---
# Wang Z Huo G L Lan H Hu J M and Wei X. 2024. Fundus image enhancement algorithm based on convolutional dictionary diffu­

## 基本信息
- **PDF**: [[cjig_paper_2.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 基于卷积字典扩散模型的眼底图像增强算法 (Fundus image enhancement algorithm based on convolutional dictionary diffusion model) |
| **作者** | 王珍; 霍光磊(通信); 兰海; 胡建民; 魏宪 |
| **单位** | 福建农林大学机电工程学院; 中科院福建物质结构研究所; 泉州通维科技; 福建医科大学; 华东师范大学软件工程学院 |
| **发表时间** | 2024 年 8 月 |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics) 29(8):2426-2438 |
| **DOI** | 10.11834/jig.230595 |
| **基金** | 泉州市科技项目 (2023C009R, 2022C004L) |

## 摘要

**清理后英文原摘要 (Abstract)**：

> Objective: Retinal fundus images have important clinical applications in ophthalmology. These images can be used to screen and diagnose various ophthalmic diseases, such as diabetic retinopathy, macular degeneration, and glaucoma. However, the acquisition of these images is often affected by various factors in real scenarios, including lens defocus, poor ambient light conditions, patient eye movements, and camera performance. These issues often lead to quality problems such as blurriness, unclear details, and inevitable noise in fundus images. Existing enhancement methods for fundus images have progressed in improving image quality; however, some problems still exist, such as image blurring, artifacts, missing high-frequency information, and increased noise. Therefore, in this study, we propose a convolutional dictionary diffusion model, which combines convolutional dictionary learning with a conditional diffusion model.
>
> Method: The algorithm consists of two parts: simulation of a diffusion process and an inverse denoising process. First, random noise is gradually added to the input image to obtain a purely noisy image; then a neural network is trained to gradually remove the noise until a clear image is obtained. This study takes the blurred fundus image as the conditional information to better preserve the fine-grained structure of the image. Because blurred–clear fundus image pairs are difficult to collect, a Gaussian filtering algorithm is designed to simulate defocus-blur images. The convolutional network implements convolutional dictionary learning to obtain the sparse representation of the image; a self-attention mechanism is added to the convolutional dictionary learning module to capture non-local similarity and long-range dependency and improve reconstruction quality. The model minimizes the negative log-likelihood loss.
>
> Result: The proposed method was trained on the EyePACS dataset and evaluated on synthetic datasets DRIVE, CHASEDB1, ROC and realistic datasets RF, HRF. Compared with the original diffusion model (Led, learning enhancement from degradation), PSNR and LPIPS are improved on average by 1.9929 dB and 0.0289, respectively. Used as a preprocessing module for the downstream retinal-vessel-segmentation task on DRIVE, the AUC, accuracy (Acc) and sensitivity (Sen) are improved by 0.0314, 0.0030 and 0.0738 on average, respectively.
>
> Conclusion: The proposed method can remove blur while preserving real fundus features and recovering richer details, which benefits the analysis and application of clinical images.

**中文翻译**：

> 目的：视网膜眼底图像广泛用于临床筛查和诊断眼科疾病（糖尿病视网膜病变、黄斑变性、青光眼等），但散焦、光线不佳、患者眼动、相机性能等因素常导致图像模糊、细节不清和噪声，且现有增强方法恢复的图像仍存在模糊、伪影、高频信息缺失和噪点增多的问题。为此本文提出一个卷积字典扩散模型，将卷积字典学习与条件扩散模型相结合。
> 方法：算法包含扩散过程与反向去噪过程两部分。先逐步向输入图像加噪得到纯噪声图像，再训练神经网络逐步去噪还原清晰图像；以模糊眼底图像作为条件信息以更好保留图像细粒度结构。由于清晰-模糊配对图像难以采集，本文用高斯滤波模拟散焦模糊合成训练数据；用卷积网络实现卷积字典学习获取稀疏表示，并在该模块中加入自注意力以捕捉非局部相似性与长程依赖、提升重建质量；模型最小化负对数似然损失。
> 结果：模型在 EyePACS 上训练，在合成数据集 DRIVE、CHASEDB1、ROC 与真实数据集 RF、HRF 上测试。与原始扩散模型 Led 相比，PSNR、LPIPS 平均分别提升 1.9929 dB 和 0.0289。作为下游任务前处理，在 DRIVE 视网膜血管分割上 AUC、Acc、Sen 较 Led 平均分别提升 0.0314、0.0030、0.0738。
> 结论：所提方法能在去除模糊的同时保留真实眼底特征并恢复更丰富的细节，有利于临床图像分析与应用。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：视网膜眼底图像是眼科疾病诊断和监测的重要工具，但成像设备限制、镜头散焦、光线条件、患者配合度等因素常导致图像模糊、低对比度、不均匀照明和噪声。一项基于 UK BioBank (MacGillivray 等, 2015) 的研究表明：68 544 名参与视网膜成像的参与者中，约 **30%** 的眼底图像因质量不足而无法被眼科医生识别，其中不可处理图像约 **80%** 完全或大部分模糊。
- **之前方法的问题**：
  - CNN 类方法（如 Gaudio 等的像素颜色放大、Zamir 等的多尺度残差特征融合、Zhu 等的信息一致性机制）在高分辨率重建上有局限，无法恢复细微结构，对噪声和伪影鲁棒性弱，结果常模糊或产生伪结构。
  - 扩散模型 (DDPM) 鲁棒性更好、生成更可控，但通常结合 U-Net，下采样会逐渐降低空间分辨率、丢失或模糊细小特征；眼底图像比自然图像细节更丰富，故 U-Net 扩散模型不能直接套用。
- **核心思路与矛盾**：卷积字典学习能自适应学习字典、更好捕捉数据特征与结构，稀疏表示能有效过滤噪声。因此本文将**卷积字典学习模块嵌入 U-Net 下采样后的中间层**，核心矛盾是如何在去模糊增强的同时**保留眼底真实细微结构（血管、视盘等）、避免高频信息缺失和噪点增多**，并提升跨数据集泛化与鲁棒性。

## 关键贡献

1. **首次将卷积字典学习与条件扩散模型结合用于眼底图像增强**：把卷积字典学习模块作为 U-Net 下采样后的中间层，融合稀疏表示的去噪优势与条件扩散模型的生成灵活性，缓解重建图像高频信息缺失和噪点增多问题。
2. **以模糊眼底图像作为条件先验**：将模糊图 `xb` 与噪声图 `xt` 在通道维拼接后输入网络，缓解去噪过程的不确定性，引导模型更精确恢复结构（区别于无条件 DDPM 从纯噪声"无中生有"）。
3. **设计基于高斯滤波的散焦模糊退化模型**：合成清晰-模糊配对训练数据，参数为 `σB = 15 + 10×random`、`rB ∈ [σB/3, σB/2]` (random∈[0,1])。
4. **在卷积字典学习模块中引入自注意力**：捕捉非局部自相似性和长程依赖，提升重建质量。
5. **采用分层抽样加速去噪**：将反向去噪迭代从原始 1k~2k 次减少到 **100 次**。
6. **充分的实验验证**：在 6 个数据集上 PSNR/LPIPS 均最优，并验证作为前处理能提升 DRIVE 视网膜血管分割精度。

## 方法

- **整体框架**：模型为**条件去噪扩散概率模型 (CDDPM)**，网络基于 U-Net，含三部分：下采样模块、卷积字典学习模块（中间层）、上采样模块（图 3）。核心是正向扩散过程与反向去噪过程。
- **理论基础**：
  - **卷积字典学习**：用一组线性滤波器 {dj} 代替非结构化字典 D，优化目标为重构误差 + L1 稀疏正则（式 1，约束 ‖dj‖₂≤1 避免尺度模糊）；稀疏编码用迭代阈值收缩算法 **ISTA** (Gregor 和 LeCun, 2010) 求解（式 2），软阈值函数 ST(x,θ)=sign(x)·max(|x|−θ,0)（式 3）。
  - **DDPM**：正向过程为马尔可夫加噪 `q(xt|xt-1)=N(xt; √(1-βt)xt-1, βtI)`（式 4），任意时刻 `xt=√α̅t·x0+√(1-α̅t)·z̃t`（式 6，αt=1-βt, α̅t=∏αt）；反向去噪过程预测噪声 `zθ`，迭代式（式 11）。
- **输入与输出**：
    - **输入**：条件信息——模糊眼底图像 `xb`，加随机噪声图 `xt`，两者通道维拼接。
    - **输出**：反向去噪迭代后的清晰眼底图像 `x0`。
- **关键模块**：
    1. **下采样模块**：不断缩小图像尺寸提取抽象特征，降低稀疏表示计算的时空复杂度。采用 Dhariwal 和 Nichol (2021) 基于 **Wide-Resnet** (Zagoruyko 和 Komodakis, 2017) 的"减小深度、增大宽度"结构，避免层数增加导致训练困难和参数量剧增。
    2. **卷积字典学习模块（核心创新）**：将 ISTA 求解过程**展开为递归卷积神经网络**，用卷积算子代替矩阵乘法、卷积滤波器当字典（式 12）：迭代 `z^{k+1}=ST(z^k + C1^{kT}∗(x − C2^k∗z^k), v^k)`，K 步后得 `z_ISTA`，再 `x̂=D∗z_ISTA`。可学习参数集 `O={[C1^{kT}, C2^k, v^k], D}`；目标函数为重构损失 `L=½‖x−x̂‖₂²`（式 13）。
    3. **自注意力机制**：加在卷积字典学习模块中，`Attention(Q,K,V)=softmax(QKᵀ/√dk)V`（式 14），Q/K/V 由特征图 X 与 WQ/WK/WV 相乘得到。
    4. **上采样模块**：用反卷积层将特征还原到原图尺寸，并与下采样特征拼接融合，输出 `xt-1`（图 3c）。
- **时间步嵌入与方差调度**：扩散时间 T 通过 **Transformer** 在每个残差块做位置嵌入（正弦/余弦位置编码，式 15），**T=3000**；采用 Nichol 和 Dhariwal (2021) 的**余弦方差调度**（式 16，s=0.008）。
- **分层抽样加速**：不直接把 t 输入模型，而是借鉴离散抽样策略 (Chen 等, 2020)，定义 T=100 的噪声调度，在分割片段 (α̅_{t-1}, α̅_t) 中均匀采样噪声水平 α̅ 作为输入，仅 **100 次迭代**完成去噪。
- **退化模型**：参考 Shen 等 (2021)，`x_blur = x∗GB(rB+σB) + n`（式 17），GB 为高斯滤波器，rB 为模糊半径，σB 为空间常数，n 为噪声；`σB=15+10×random`，`rB∈[σB/3, σB/2]`。
- **损失函数**：将模糊图作为先验代入反向式（式 18）`xt-1 = (1/√αt)(xt − βt/√(1-α̅t)·zθ(xb,xt,α̅)) + σt·z`；损失最小化 μθ 与 μ̃t 差异（式 19），并按 Ho 等 (2020) 去除系数得简化目标（式 20）`Lθ = E[‖zt − zθ(√α̅t·x0 + √(1-α̅t)·zt, xb, α̅)‖²]`，即让预测噪声 zθ 逼近真实噪声 zt。
- **训练配置**：图像统一 512×512；Adam 优化器，学习率 `3×10⁻⁶`，迭代 **2M** 次；因显存大、批大小小，**用组归一化 (GroupNorm) 代替批归一化**。实验环境：CentOS 7、i7-6700、Python 3.6.9、PyTorch 1.9.0、CUDA 11.1、RTX 3090（表 1）。

## 实验

- **数据集**：
    - **训练集**：EyePACS (Cuadros 和 Bresnick, 2009) 中选 **8400** 幅高质量眼底图，用退化模型合成 8400 幅模糊图组成配对训练集；另取 50 幅及其合成模糊图作测试。
    - **泛化测试集**：合成数据集 **DRIVE**(40 幅, 768×584，含血管分割标签)、**CHASEDB1**(28 幅, 999×960，含分割标签)、**ROC**(100 幅)；真实数据集 **RF**(120 组 2560×2560 清晰/低质对)、**HRF**(佳能 CR-1 相机, 18 名受试者 18 对清晰/失焦图)。
- **评价指标**：图像质量——**PSNR**(越高越好，式略)、**LPIPS** (Zhang 等, 2018，越低越好，式 21)；并对各数据集 PSNR/LPIPS 计算**方差** σ²(P)/σ²(L) 衡量鲁棒性（表 3）；分割精度——**AUC**、**Acc**、**Sen**(越高越好)。
- **对比方法**（6 种）：CLAHE(传统直方图均衡)、Cofe-Net(CNN)、Arc-Net(CNN+域自适应)、Cycle-GAN、T-Cycle-GAN(Transformer+GAN)、**Led** (Cheng 等, 2023，基于 DDPM 的退化学习增强，即基准扩散模型)。
- **主实验——图像去模糊（表 2）**：
    - 本文算法 6 数据集平均 **PSNR=29.6710 dB、LPIPS=0.1015**，均为最优；相比 Led(平均 PSNR=27.6781, LPIPS=0.1304) 提升 **1.9929 dB / −0.0289**。
    - 次优为 T-Cycle-GAN(平均 PSNR=29.1168, LPIPS=0.1063)；最差为 CLAHE(平均 PSNR=20.9200, LPIPS=0.2951)。
    - 各数据集本文 PSNR：EyePACS 31.8023、DRIVE 30.1533、CHASEDB1 32.3744、RF 26.3791、HRF 27.2084、ROC 30.1083。本文仅在 RF 上 PSNR 略逊 Cycle-GAN(26.7853)，其余 5 个数据集 PSNR/LPIPS 均最优。
    - **鲁棒性（表 3）**：本文仅在 CHASEDB1 的 σ²(P) 略高于 Led，整体平均方差最优，且所有数据集 σ²(L) 均最小。
- **视网膜血管分割（表 4）**：用 Liu 等 (2022) 的分割方法，在 DRIVE 上以增强后图像分割：本文 **AUC=0.8352、Acc=0.9080、Sen=0.3801** 三项均最优；相比 Led(AUC=0.8038, Acc=0.9050, Sen=0.3063) 平均提升 **0.0314 / 0.0030 / 0.0738**。Cycle-GAN 易产生伪结构、分割出不存在的血管；Led 因用 U-Net 对视神经头部血管恢复不完整。
- **消融实验（表 5，EyePACS 测试集）**：逐组件验证（√=用，×=不用）：

| 扩散模型 | 卷积字典学习 | 自注意力 | PSNR/dB | LPIPS |
|:---:|:---:|:---:|:---:|:---:|
| × | √ | √ | 23.3765 | 0.2059 |
| √ | × | × | 26.4645 | 0.1217 |
| √ | × | √ | 28.1617 | 0.1101 |
| √ | √ | × | 30.8972 | 0.0962 |
| √ | √ | √ | **31.8023** | **0.0827** |

  解读：仅扩散模型 PSNR=26.4645；加自注意力→28.1617；加卷积字典学习→30.8972；三者全用→31.8023。去掉扩散模型(第 1 行)指标大幅下降，三个组件均有正向贡献，卷积字典学习贡献最大。
- **采样模块数量实验（图 10）**：分别设 3/5/6/7 个采样模块，记录每轮训练时间与前 30 轮增强效果；综合性能、计算资源和运行时间，**模块数=5 时效率最佳**。
- **效率信息**：PDF 文本未明确 FLOPs 或参数量；通过分层抽样将推理迭代从原始 1k~2k 次减少到 100 次以提速。

## 局限

1. **模型复杂度与速度**：作者在结论中明确指出，算法模型复杂度相对较高、计算速度无明显优势，限制了实际应用可行性；未来方向是轻量化架构、模型剪枝等。
2. **退化模型的局限**：训练依赖高斯滤波模拟的散焦模糊（式 17），可能无法覆盖真实临床中所有复杂退化类型（如运动模糊等），可能影响极端情况的泛化。
3. **下游任务验证单一**：仅在视网膜血管分割上验证临床价值，未在病灶检测、视杯视盘分割等更多任务上验证。
4. **依赖合成数据**：训练用合成模糊图，尽管在真实数据集 (RF/HRF) 上测试，合成与真实退化间的 domain gap 仍是此类方法的普遍挑战。

## 个人评论

1. **跨领域技术融合**：将信号处理的经典方法（卷积字典学习/稀疏表示，及其 ISTA 求解器）与现代深度生成模型（扩散模型）创新融合。其"把 ISTA 展开为递归卷积网络"的做法值得借鉴——为解决 U-Net 下采样丢细节的固有缺陷，回头把传统算法网络化，是很有启发的工程思路。
2. **条件扩散引入结构先验**：把模糊图作为强条件输入而非从纯噪声生成，大大约束了生成空间，更好保留原图结构，避免伪影。这种"强条件引导"在医学图像增强中尤为重要（伪结构会误导诊断）。
3. **完整的评估链条**：不仅评图像质量指标 (PSNR/LPIPS)，还加方差衡量鲁棒性，并通过下游血管分割验证临床实用性——从"图像质量"到"任务性能"的完整闭环值得学习。
4. **可改进处**：作者自承速度无优势是真痛点（递归 ISTA 展开 + 自注意力 + 扩散迭代叠加）；分层抽样把迭代降到 100 步是务实的折中，但与一次性采样的加速方法相比仍有空间。

### 使用建议

- **快速了解**：读摘要、引言（背景与问题）、第 2 节（模型框架）、3.4.1（去模糊结果）、第 4 节（结论）。
- **如果复现**：重点看第 2 节、式(12)（卷积字典学习的递归展开）、式(17)（退化模型参数）、第 3.1 节（实验环境与数据集），需实现 Wide-Resnet 风格结构和卷积字典学习模块。
- **如果借鉴创新点**：学习其将 ISTA 展开为可微递归网络、以及在生成模型中引入强条件输入（原模糊图）的策略，对去噪、超分等图像复原任务有启发。
- **写 related work**：可放在 (1) 眼底图像增强；(2) 基于扩散模型的图像增强/复原；(3) 字典学习/稀疏表示与深度学习结合 三类中讨论。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**医学图像复原/增强**方向（眼底图像去模糊），是计算机视觉中图像复原 (image restoration) 的一个垂直应用。解决的核心问题是：临床筛查中因散焦、光线不佳、患者眼动、相机性能等导致的低质量（模糊）视网膜眼底图像，影响医生准确诊断。从任务性质看（去模糊、去噪、恢复高频细节），归入 `E_图像复原_超分_去噪_去雨去雾` 主题，而非原先误归的 `T_通用_NLP_其他`。

## 2. 一句话总结
本文提出**卷积字典扩散模型 (CDDPM)**，把卷积字典学习（ISTA 展开为递归卷积网络）的稀疏去噪能力嵌入条件扩散模型的 U-Net 中间层，并以模糊图为条件、加自注意力，实现模糊眼底图像增强，在恢复细节的同时抑制高频信息缺失和噪点。

## 3. 背景与问题
- **为什么做**：眼底图像是眼科诊断与监测的重要工具，但成像设备、散焦、光线、患者配合度等导致模糊、低对比度、不均匀照明和噪声。UK BioBank 研究 (MacGillivray 等, 2015) 显示 68 544 名参与者中约 30% 眼底图像因质量不足无法识别，其中约 80% 完全/大部分模糊。
- **之前方法的问题**：CNN 类方法在高分辨率重建上无法恢复细微结构、对噪声伪影鲁棒性弱；扩散模型虽鲁棒可控，但 U-Net 下采样会丢失/模糊细小特征，而眼底图比自然图细节更丰富，不能直接套用。
- **核心矛盾**：在去模糊增强的同时保留真实细微结构（血管、视盘），避免高频缺失/噪点，并提升跨数据集泛化与鲁棒性。

## 4. 核心贡献
1. **首次结合卷积字典学习与条件扩散模型**用于眼底增强，把卷积字典学习模块作为 U-Net 下采样后的中间层，融合稀疏去噪与扩散生成。
2. **模糊图作为条件先验**（与噪声图通道拼接），缓解去噪不确定性，引导精确恢复结构。
3. **基于高斯滤波的散焦模糊退化模型**合成配对数据 (σB=15+10×random, rB∈[σB/3,σB/2])。
4. **卷积字典学习模块中加自注意力**，捕捉非局部相似性与长程依赖。
5. **分层抽样加速**，反向去噪迭代由 1k~2k 次降到 100 次。
6. **完整实验**：6 数据集 PSNR/LPIPS 最优 + 下游血管分割提升。

## 5. 方法详解
- **整体框架**：CDDPM，基于 U-Net，含下采样模块、卷积字典学习中间层、上采样模块（图 3）。
- **输入/输出**：输入为模糊图 `xb`（条件）与噪声图 `xt` 通道拼接；输出为反向去噪后的清晰图 `x0`。
- **理论基础**：
  - 卷积字典学习：式(1) 重构误差+L1 正则（‖dj‖₂≤1）；ISTA 迭代式(2)；软阈值 ST 式(3)。
  - DDPM：正向加噪式(4)、闭式式(6) `xt=√α̅t·x0+√(1-α̅t)·z̃t`；反向预测噪声 zθ，迭代式(11)。
- **关键模块**：
    1. **下采样**：缩小尺寸提取抽象特征、降低稀疏表示计算复杂度；用 Dhariwal & Nichol(2021) 的 Wide-Resnet（浅而宽）结构。
    2. **卷积字典学习（核心）**：把 ISTA 展开为 K 步递归卷积网络（式 12），卷积算子代替矩阵乘法、滤波器当字典：`z^{k+1}=ST(z^k+C1^{kT}∗(x−C2^k∗z^k), v^k)`，得 `z_ISTA`，`x̂=D∗z_ISTA`；目标 `L=½‖x−x̂‖₂²`（式 13）。
    3. **自注意力**：式(14) `softmax(QKᵀ/√dk)V`，加在字典学习模块中提升重建质量。
    4. **上采样**：反卷积还原尺寸 + 特征拼接融合，输出 `xt-1`。
- **时间嵌入/调度**：Transformer 位置嵌入（式 15），T=3000；余弦方差调度（式 16，s=0.008）。
- **分层抽样**：定义 T=100 噪声调度，在 (α̅_{t-1},α̅_t) 均匀采样 α̅，100 次迭代完成去噪 (Chen 等, 2020)。
- **退化模型**：式(17) `x_blur=x∗GB(rB+σB)+n` (Shen 等, 2021)。
- **损失**：式(18) 把模糊图代入反向式；式(19) 最小化 μθ 与 μ̃t 差异；式(20) 去系数简化目标 `Lθ=E[‖zt−zθ(√α̅t·x0+√(1-α̅t)·zt, xb, α̅)‖²]`。
- **训练**：512×512、Adam、lr=3×10⁻⁶、2M 迭代、GroupNorm 替代 BatchNorm；环境 RTX 3090 / PyTorch 1.9.0 / CUDA 11.1（表 1）。

## 6. 实验与结果
- **数据集**：训练 EyePACS 8400 幅+合成 8400 模糊 (另 50 幅测试)；泛化测试 DRIVE/CHASEDB1/ROC（合成）、RF/HRF（真实）。DRIVE、CHASEDB1 含血管分割标签。
- **对比方法**：CLAHE、Cofe-Net、Arc-Net、Cycle-GAN、T-Cycle-GAN、Led（基准扩散模型）。
- **指标**：PSNR↑、LPIPS↓（式 21）、方差 σ²(P)/σ²(L)（鲁棒性）；分割 AUC/Acc/Sen↑。
- **图像增强（表 2）**：本文平均 PSNR=29.6710 dB、LPIPS=0.1015，均最优；相比 Led(27.6781/0.1304) 提升 1.9929 dB/−0.0289。次优 T-Cycle-GAN(29.1168/0.1063)；本文仅 RF 的 PSNR 略逊 Cycle-GAN，其余 5 数据集全最优。各数据集本文 PSNR：EyePACS 31.8023 / DRIVE 30.1533 / CHASEDB1 32.3744 / RF 26.3791 / HRF 27.2084 / ROC 30.1083。
- **鲁棒性（表 3）**：本文整体平均方差最优，所有数据集 σ²(L) 最小（仅 CHASEDB1 的 σ²(P) 略高于 Led）。
- **血管分割（表 4，DRIVE）**：本文 AUC=0.8352 / Acc=0.9080 / Sen=0.3801 三项最优；相比 Led(0.8038/0.9050/0.3063) 平均提升 0.0314/0.0030/0.0738。
- **消融（表 5，EyePACS）**：仅扩散 26.4645→+自注意力 28.1617→+卷积字典学习 30.8972→全用 31.8023（LPIPS 0.1217→0.1101→0.0962→0.0827）；去掉扩散模型(第 1 行 23.3765)指标最差。卷积字典学习贡献最大，三组件均正向。
- **采样模块数（图 10）**：3/5/6/7 对比，模块数=5 效率最佳。
- **效率**：FLOPs/参数量 PDF 文本未明确；分层抽样把迭代由 1k~2k 降到 100 次。

## 7. 这篇论文真正有价值的地方
1. **把传统算法网络化**：将 ISTA/卷积字典学习展开为可微递归卷积网络嵌入扩散 U-Net，针对性弥补"下采样丢细节"，是经典优化算法与深度生成模型融合的好范例。
2. **强条件引导**：以模糊图为条件约束生成空间，比无条件 DDPM 更能保结构、抑伪影——这一点在医学增强中关乎诊断安全（伪结构会误导）。
3. **完整评估链条**：图像质量 + 方差鲁棒性 + 下游分割任务三层验证，把"画质好"落到"任务有用"。

## 8. 局限与问题
1. **复杂度/速度**：作者结论明确承认模型复杂度高、速度无优势，限制落地；未来转向轻量化与剪枝。
2. **退化模型单一**：仅高斯散焦模糊（式 17），难覆盖真实复杂退化（运动模糊等）。
3. **下游验证单一**：仅血管分割，未覆盖病灶检测、视杯视盘分割等。
4. **依赖合成数据**：合成-真实 domain gap 仍是普遍挑战。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要、引言、第 2 节（模型框架）、3.4.1（去模糊结果）、第 4 节（结论）。
- **如果复现**：第 2 节、式(12)（卷积字典学习递归展开）、式(17)（退化模型参数）、第 3.1 节（环境与数据集）；需实现 Wide-Resnet 结构与卷积字典学习模块。
- **如果借鉴创新点**：学习 ISTA→可微递归网络 的展开手法，以及生成模型中的强条件输入策略，可迁移到去噪/超分等复原任务。
- **写 related work**：归入 (1) 眼底图像增强；(2) 扩散模型图像增强/复原；(3) 字典学习/稀疏表示+深度学习 三类。

## 10. 和其他论文的关系
本文属图像复原方向（眼底去模糊），与之相关：
- **扩散模型基础**：[[DDPM]] (Ho 等, 2020)、Sohl-Dickstein 等(2015)、改进调度 (Nichol & Dhariwal, 2021)、Wide-Resnet 上采样 (Dhariwal & Nichol, 2021)。
- **眼底增强对比方法**：[[Led]] (Cheng 等, 2023, 基准扩散模型)、Cofe-Net (Shen 等, 2021)、Arc-Net (Li 等, 2022)、Cycle-GAN (Wan 等, 2022)、T-Cycle-GAN (Alimanov & Islam, 2022)、CLAHE。
- **字典学习/稀疏表示**：[[ISTA]] (Gregor 和 LeCun, 2010) 的可学习展开是本文核心借鉴。
- **退化合成**：Shen 等 (2021) 的散焦模糊退化模型。

## 11. 关键词
眼底图像增强, 卷积字典学习, 稀疏表示, 扩散模型, 条件扩散模型, 自注意力, ISTA, 视网膜血管分割, 图像去模糊, 图像复原

## 12. 可信度说明
本篇精读基于 PDF 提取文本（12/13 页，含标题、摘要、引言、理论基础、模型框架、退化模型、损失函数、完整实验环境/数据集、对比表 2/3/4、消融表 5、结论）。这些内容信息充分，关键公式、数字（PSNR/LPIPS/AUC/Acc/Sen 各表数值）和结论均清晰可辨，已据原文逐一核对修正。提取缓存仅缺第 13 页（参考文献），不影响对方法与实验的理解。本笔记为 AI 阅读稿，`human_reviewed` 保持 `false`。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/cjig_paper_2.txt` (提取 12/13 页, 缺第 13 页参考文献); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮已据提取文本逐表核对数值并修正分类 (E_图像复原)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-13。
- **提取情况**: 缺失页 1 页, 其中 1 页提取到可读文本。第 13 页为参考文献 (References), 不含正文/实验/讨论新内容。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Color retinal image enhancement using CLAHE//Proceedings of
- p.13: Deep unsupervised learning using nonequilibrium thermodynamic
- p.13: Medical image fusion using double dictionary learning and adaptive
- p.13: Proceedings of 2018 IEEE/CVF Conference on Computer Vision

### 缺失页关键摘录

- p.13: 2024 Roux C ， Karray F ， Garcia M ， Fujita H and Abramoff M D .
<!-- AI_READING_NOTE_END -->
