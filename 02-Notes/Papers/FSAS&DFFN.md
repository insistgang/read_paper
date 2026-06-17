---
title: Efficient Frequency Domain-based Transformers
authors:
  - "Lingshun Kong"
  - "Jiangxin Dong"
  - "Jianjun Ge"
  - "Mingqiang Li"
  - "Jinshan Pan"
year: 2023
venue: "CVPR"
doi: 
pdf: [[FSAS&DFFN.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
extract_cache: .paper-cache/extracts/FSAS&DFFN.txt
---

# Efficient Frequency Domain-based Transformers

## 基本信息
- **PDF**: [[FSAS&DFFN.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`, `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Efficient Frequency Domain-based Transformers for High-Quality Image Deblurring |
| **作者** | Lingshun Kong; Jiangxin Dong; Jianjun Ge; Mingqiang Li; Jinshan Pan |
| **单位** | 南京理工大学计算机科学与工程学院; 中国电子科技集团信息科学研究院 |
| **发表时间** | 2023 |
| **刊物/会议** | CVPR |
| **代码** | https://github.com/kkkls/FFTformer |
| **DOI** | 未明确 |

## 摘要

> We present an effective and efficient method that explores the properties of Transformers in the frequency domain for high-quality image deblurring. Our method is motivated by the convolution theorem that the correlation or convolution of two signals in the spatial domain is equivalent to an element-wise product of them in the frequency domain. This inspires us to develop an efficient frequency domain-based self-attention solver (FSAS) to estimate the scaled dot-product attention by an element-wise product operation instead of the matrix multiplication in the spatial domain. In addition, we note that simply using the naive feed-forward network (FFN) in Transformers does not generate good deblurred results. To overcome this problem, we propose a simple yet effective discriminative frequency domain-based FFN (DFFN), where we introduce a gated mechanism in the FFN based on the Joint Photographic Experts Group (JPEG) compression algorithm to discriminatively determine which low- and high-frequency information of the features should be preserved for latent clear image restoration. We formulate the proposed FSAS and DFFN into an asymmetrical network based on an encoder and decoder architecture, where the FSAS is only used in the decoder module for better image deblurring. Experimental results show that the proposed method performs favorably against the state-of-the-art approaches.

> **中文翻译**: 我们提出了一种有效且高效的方法，在频域中挖掘 Transformer 的特性，用于高质量图像去模糊。本方法的动机来自卷积定理：两个信号在空间域的相关或卷积运算，等价于它们在频域中的逐元素乘积。受此启发，我们设计了一个高效的频域自注意力求解器（FSAS），用频域的逐元素乘积运算来估计缩放点积注意力，从而取代空间域中的矩阵乘法。此外，我们注意到，直接使用 Transformer 中朴素的前馈网络（FFN）无法生成良好的去模糊结果。为解决该问题，我们提出了一个简单而有效的判别性频域前馈网络（DFFN）：在 FFN 中引入一个基于 JPEG 压缩算法的门控机制，以判别性地决定特征中哪些低频与高频信息应被保留，用于潜在清晰图像的复原。我们将 FSAS 与 DFFN 组织进一个基于编码器-解码器架构的非对称网络，其中 FSAS 仅用于解码器模块以获得更好的去模糊效果。实验结果表明，本方法相较当前最先进方法表现优异。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：图像去模糊（image deblurring）旨在从模糊图像恢复高质量清晰图像，是一项重要的底层视觉任务。基于 CNN 的方法虽借助多尺度、多阶段、GAN、物理模型启发结构等取得显著进展，但卷积是**空间不变的局部操作**，无法建模图像内容的空间变化特性与全局上下文；论文还指出（引 [17,33]）单纯增大模型容量并不总能带来性能提升。
- **之前方法的问题**：
    1.  **CNN 的局限性**：卷积只建模局部连接，不能有效建模全局上下文。
    2.  **标准 Transformer 的局限性**：缩放点积注意力关于 token 数 N 具有**二次方**的空间与时间复杂度（QK^T 为 O(N²)、O(N²C)），处理高分辨率图像代价过高。
    3.  **已有降本策略的不足**：用更小/更少 token 或下采样降低空间分辨率会造成信息损失、产生伪影；而在特征深度（通道）维计算注意力的方法（如 Restormer [30]）虽降低了开销，却**未充分挖掘空间信息**，而空间信息对图像复原至关重要。
- **作者想解决的核心矛盾**：如何在享受 Transformer 全局建模能力的同时**克服其二次方复杂度瓶颈**，并设计更适合图像复原（保留有用频率信息、恢复清晰细节）的前馈模块。

## 关键贡献

论文的具体贡献如下：
1.  **高效频域自注意力求解器 FSAS**：基于卷积定理（空间域相关/卷积 = 频域逐元素乘积），用 FFT 在频域以逐元素乘积估计缩放点积注意力，取代空间域矩阵乘法，将每个特征通道的空间/时间复杂度由 O(N²) 降到 **O(N log N)**（N 为像素数）。
2.  **判别性频域前馈网络 DFFN**：受 JPEG 压缩启发，在 FFN 中引入**可学习量化矩阵 W**（以 JPEG 压缩的逆向方式学习），以门控机制判别性地决定保留哪些低/高频信息，用于潜在清晰图像复原。
3.  **非对称编码器-解码器架构**：观察到浅层（编码器）特征仍含模糊、模糊会改变相似 patch 间的相似度从而使注意力估计失准，而深层（解码器）特征更清晰；因此将 FSAS **仅置于解码器**，形成非对称结构以获得更好去模糊。
4.  **系统分析频域 Transformer 对去模糊的促进作用**：从分析与实验上论证，在频域挖掘 Transformer 特性能有效促进模糊去除，并在精度与效率上优于 SOTA（图 1）。

## 方法

- **整体框架**（图 2a）：端到端可训练的非对称编码器-解码器网络。**编码器**模块仅含 DFFN；**解码器**模块同时含 FSAS 与 DFFN（即 FSAS+DFFN 组合）。编/解码器跨层用 Concatenation 跳跃连接（图中 C），各级通道数依次为 48 / 96 / 192。最终经全局残差连接输出：`I = N(B) + B`（式 8），其中 B 为模糊图像、I 为复原图像、N 为该非对称网络。
- **关键模块一：频域自注意力求解器 FSAS**（图 2b）
    1.  **特征生成**：对输入特征 X 用 1×1 点卷积 + 3×3 深度卷积得到 Fq、Fk、Fv（不再走传统的 unfold/reshape 得到 Q/K/V）。
    2.  **核心机制**：论文先指出 QK^T 的每个元素是 patch 内积 `⟨q_i, k_j⟩`（式 3），重排 token 后可写成卷积 `q̃_i ⊛ K̃`；再据卷积定理把空间域相关转为频域逐元素乘积。对 Fq、Fk 做 FFT，在频域计算注意力图：`A = F⁻¹( F(Fq) ⊙ F(Fk)* )`（式 4），其中 F(·) 为 FFT、F⁻¹(·) 为逆 FFT、F(·)* 为共轭（原文称 conjugate transpose）。
    3.  **聚合与输出**：对 A 做 LayerNorm 后与 Value 特征 Fv 逐元素相乘得 V_att（式 5），再经 1×1 卷积并与输入相加：`X_att = X + Conv1×1(V_att)`（式 6）。计算自注意力(式4)时同样采用 8×8 的 patch 大小。
    4.  **优势**：避免空间域的 QK^T 矩阵乘法，复杂度降至 O(N log N)/通道。
- **关键模块二：判别性频域前馈网络 DFFN**（图 2c）
    1.  **输入**：FSAS 输出 X_att。
    2.  **核心机制（式 7）**：`X1 = Conv1×1(L(X_att))`；按 JPEG 的 patch unfolding `P(·)` 分块后做 FFT 得频域特征 `Xf1 = F(P(X1))`；用**可学习量化矩阵 W** 与之逐元素相乘并逆变换 `X2 = F⁻¹(W ⊙ Xf1)`；再经 patch folding `P⁻¹(·)`、GEGLU 激活 G（引 [19]）并残差相加 `X_out = G(P⁻¹(X2)) + X_att`。
    3.  **与标准 FFN 的差异**：标准 FFN（GeLU/ReLU）不区分频率；DFFN 借 JPEG「量化」思想显式、判别性地对不同频率分量加权，只保留对复原有用的频率信息。
- **训练设置**：损失函数沿用 [4]；Adam 优化器（默认参数）；初始学习率 10⁻³，**经 600,000 次迭代后**按余弦退火更新，最小学习率 10⁻⁷；patch 大小 256×256，batch size 16；数据增强沿用 [30]。量化矩阵的 patch 取 8×8（依 JPEG），张量形状为 `[batch_size, channel_num, 8, 8]`，与其余参数联合训练。
- **推理流程**：将整幅模糊图像送入训练好的网络直接输出清晰图像。
- **与已有方法的差异**：
    1.  与 **CNN 方法**（如 MIMO-Unet+ [4]）相比，引入全局注意力（FSAS）建模长程依赖。
    2.  与 **空间域 Transformer**（如 Restormer [30] 在通道维算注意力、Stripformer [24] 用条状 token、Uformer [27] 用非重叠窗口注意力）相比，本文把相关计算移到频域，避免昂贵矩阵乘法，且用 DFFN 替代标准 FFN，更充分利用空间信息。
    3.  **网络结构**上采用非对称设计，将开销较大的 FSAS 仅用于解码器，是其特色。

## 实验

- **数据集**：GoPro [16]、HIDE [20]、RealBlur [18]（RealBlur-R / RealBlur-J）；遵循各数据集既有协议公平比较。
- **对比方法**：CNN 方法（DeblurGAN-v2、SRN、DMPHN、SAPHN、MIMO-Unet+、MPRNet、NAFNet、以及 *-local 变体）与 Transformer/频域方法（IPT、DeepRFT+、Restormer、Restormer-local、Uformer-B、Stripformer、BANet）。
- **评价指标**：PSNR、SSIM、参数量（M）、平均推理时间（256×256 图像）；图 1 另含 FLOPs。
- **GoPro（Table 1）**：本文 **PSNR 34.21 dB / SSIM 0.9692**，均为表中最高。相较 CNN 的 SOTA NAFNet（33.71 dB / 67.9M），PSNR **至少高 0.5 dB**，而参数量 **16.6M 仅约为 NAFNet 的 1/4**；相较 Restormer（32.92 dB / 26.1M）、Uformer-B（33.06 / 50.9M）、Stripformer（33.08 / 19.7M）、DeepRFT+（33.23 / 23.0M）、Restormer-local（33.57 / 26.1M）均更优。
- **RealBlur（Table 2）**：RealBlur-R **40.11 dB / 0.9732**、RealBlur-J **32.62 dB / 0.9326**，PSNR 均优于对比方法（如 Stripformer 39.84/0.9737、32.48/0.9290；DeepRFT+ 39.84/0.9721、32.19/0.9305）。
- **HIDE（Table 3）**：用 GoPro 上训练的模型做泛化测试，参数量 16.6M；具体 PSNR/SSIM 数值在提取文本中被截断未覆盖（据原文后续页，提取缓存未覆盖，待核）。
- **效率分析**：参数量 16.6M 处于对比方法中较低水平；图 1 显示在 PSNR 领先的同时 FLOPs 处于中等偏下，精度-效率平衡良好。作者明确指出 **PyTorch 的 FFT 实现未充分优化**，故平均推理时间 **0.13s**（256×256），慢于高度优化的 CNN（MIMO-Unet+ 0.02s），但仍与 SOTA 有竞争力，且**比基于原始自注意力的 IPT（0.50s）至少快 4 倍**。
- **可视化（图 3、图 4）**：在 GoPro 与 RealBlur 上，CNN（NAFNet、MIMO-Unet+）与空间域 Transformer（Restormer、Stripformer、Restormer-local）的去模糊结果在字符、椅子等主结构上仍残留模糊或恢复不佳，本文结果字符与结构更清晰。
- **消融实验**：提取文本未包含详细消融表/分析；作者注明因篇幅限制更多结果置于补充材料（据原文，提取缓存未覆盖，待核）。

## 局限

- **运行时受 FFT 实现制约**：PyTorch 的 FFT 未优化，导致 0.13s 的推理时间未能完全体现频域方法的理论效率优势，依赖底层框架对 FFT 算子的支持。
- **消融证据缺失（在提取文本范围内）**：FSAS、DFFN、非对称设计各自贡献的拆解放在补充材料，提取缓存未覆盖，无法据正文直接核验各模块独立增益。
- **频域操作对高频敏感**：频域加权对噪声/纹理等高频成分敏感；虽 DFFN 做频率选择，但在极端模糊或复杂退化下的鲁棒性需进一步验证（推断，PDF 文本未就此做专门讨论）。
- **任务/退化范围**：仅在合成（GoPro）与真实运动模糊（RealBlur/HIDE）上验证，对散焦、复合退化等其他类型的泛化性待考察。
- **复现细节多**：FFT/IFFT 的正确使用、DFFN 中 JPEG patch unfold/fold 与量化矩阵 W 的初始化与学习、8×8 patch 设置等需参照作者公开代码（FFTformer）。

## 个人评论

1.  **跨域知识融合**：把信号处理的**卷积定理**与 Transformer 的**注意力**结合，用频域逐元素乘积替代 QK^T 矩阵乘法，为降低注意力复杂度提供了理论依据扎实的新视角，可启发立体匹配、光流等需要计算相关性的任务。
2.  **任务驱动的模块设计**：DFFN 不是凭空设计，而是从 **JPEG 压缩**中提取「频率选择/量化」这一对图像重建至关重要的概念，把它转化为可学习的量化矩阵 W，是「领域知识 → 网络模块」的范例。
3.  **非对称架构的实践洞见**：从「浅层模糊特征会破坏 patch 相似度、不利于注意力估计」的观察出发，提出 FSAS 只放解码器的非对称结构，打破「编/解码器对称」的默认范式，提示按特征清晰度差异化配置模块。
4.  **效率-性能的强平衡**：以 1/4 于 NAFNet 的参数量取得 +0.5 dB 的 GoPro PSNR，对部署友好；唯运行时受 FFT 实现拖累，是工程层面而非方法层面的短板。

### 使用建议

- **快速了解**：读摘要 + 图 2（架构）+ 图 1 与 Table 1，即可把握核心思想与性能优势。
- **复现**：精读第 3 节（3.1 FSAS 式 3-6、3.2 DFFN 式 7、3.3 非对称结构式 8）配合图 2(b)(c)，并落实 4.1 节全部训练细节（学习率 10⁻³→10⁻⁷ 余弦退火、600k 迭代、patch 256×256、batch 16、量化矩阵 8×8）；参照官方代码 FFTformer。
- **借鉴创新点**：FSAS 的频域相关计算可迁移到其他需相似度/相关性的视觉任务以降本；DFFN 的「源于经典算法的门控/选择」思路可移植到其他 FFN 设计；非对称设计思想可用于按编/解码器特征状态（分辨率/噪声/清晰度）差异化放置模块。
- **写 related work**：可归入「高效图像复原 Transformer」「频域在深度学习中的应用（如 DeepRFT）」「图像去模糊的深度学习方法」三类。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉**图像复原**方向，具体任务为**图像去模糊（image deblurring）**：从模糊图像恢复高质量清晰图像。核心创新是把 Transformer 的注意力计算从空间域搬到**频域**（FSAS），并以受 JPEG 压缩启发的判别性前馈网络（DFFN）替代标准 FFN，二者构成非对称编码器-解码器网络（FFTformer）。因方法本体是一个新型注意力/前馈算子，且落点在图像复原，故主题归入「**E_图像复原_超分_去噪_去雨去雾**」，并以「**B_注意力算子模块**」作为次主题（FSAS 是可迁移的注意力算子）。

## 2. 一句话总结
本文提出在频域用逐元素乘积估计缩放点积注意力的高效求解器 FSAS（复杂度 O(N²)→O(N log N)/通道），并设计受 JPEG 启发、含可学习量化矩阵的判别性前馈网络 DFFN，将二者组织为「编码器只含 DFFN、解码器含 FSAS+DFFN」的非对称网络，实现高质量、高效率的图像去模糊。

## 3. 背景与问题
- **为什么要做**：去模糊是重要底层视觉任务；CNN 方法的卷积是空间不变的局部操作，无法建模空间变化与全局上下文，且单纯增大容量未必更好（[17,33]）。Transformer 能建模全局上下文，在去模糊上已优于 CNN，但缩放点积注意力对 token 数 N 是二次方复杂度。
- **之前方法的问题**：
    1.  **CNN**：局部操作，缺全局建模。
    2.  **标准 Transformer**：QK^T 复杂度 O(N²)/O(N²C)，高分辨率不可承受；用更少 token / 下采样会信息损失、产生伪影。
    3.  **通道维注意力**（Restormer [30]）：降本但未充分利用对复原至关重要的空间信息。
- **核心矛盾**：在保留 Transformer 全局建模力的同时打掉二次方复杂度，并设计更利于复原的前馈模块。

## 4. 核心贡献
1.  **FSAS**：据卷积定理用 FFT 在频域以逐元素乘积估计缩放点积注意力，复杂度降到 O(N log N)/通道，更高效有效。
2.  **DFFN**：受 JPEG 压缩启发，引入可学习量化矩阵、以门控判别性地保留有用低/高频信息。
3.  **非对称编/解码器**：FSAS 仅用于解码器（浅层模糊特征会使注意力相似度估计失准）。
4.  **分析与验证**：论证频域挖掘 Transformer 特性可促进模糊去除，并在精度/效率上优于 SOTA（图 1）。

## 5. 方法详解
- **整体框架（图 2a）**：端到端非对称编码器-解码器。编码器模块仅 DFFN；解码器模块为 FSAS+DFFN；通道数 48/96/192，跨层 Concatenation 跳连，输出 `I = N(B) + B`（式 8）。
- **FSAS（图 2b，式 3-6）**：
    1.  Fq、Fk、Fv 由 1×1 点卷积 + 3×3 深度卷积得到。
    2.  推导：QK^T 元素为 patch 内积 `⟨q_i,k_j⟩`（式 3），重排后等价卷积 `q̃_i ⊛ K̃`，据卷积定理转为频域逐元素乘积。
    3.  注意力图 `A = F⁻¹( F(Fq) ⊙ F(Fk)* )`（式 4，F(·)* 为共轭/conjugate transpose）。
    4.  `V_att = L(A) ⊙ Fv`（式 5，L 为 LayerNorm）；`X_att = X + Conv1×1(V_att)`（式 6）。计算式(4)时 patch 取 8×8。
- **DFFN（图 2c，式 7）**：`X1=Conv1×1(L(X_att))` → `Xf1=F(P(X1))`（P 为 JPEG patch unfolding）→ `X2=F⁻¹(W⊙Xf1)`（W 可学习量化矩阵）→ `X_out=G(P⁻¹(X2))+X_att`（P⁻¹ 为 patch folding，G 为 GEGLU [19]）。W 以 JPEG 压缩的逆向方式学习，判别性地决定保留哪些频率。
- **非对称设计（3.3）**：多数方法编/解码器对称；但编码器浅层特征含模糊，模糊会改变相似 patch 的相似度，使 FSAS 在编码器估计相似度失准，故 FSAS 只嵌解码器。
- **训练**：损失沿用 [4]；Adam（默认参数）；学习率 10⁻³，经 600,000 次迭代后余弦退火至 10⁻⁷；patch 256×256、batch 16；数据增强同 [30]；量化矩阵 patch 8×8、张量形状 `[batch_size, channel_num, 8, 8]`，联合训练。代码：FFTformer。

## 6. 实验与结果
- **数据集**：GoPro [16]、HIDE [20]、RealBlur [18]。
- **对比方法**：DeblurGAN-v2、SRN、DMPHN、SAPHN、MIMO-Unet+、MPRNet、IPT、DeepRFT+、Restormer(+local)、Uformer-B、Stripformer、NAFNet、BANet 等。
- **指标**：PSNR、SSIM、参数量、平均推理时间（256×256），图 1 含 FLOPs。
- **GoPro（Table 1）**：**Ours 34.21 / 0.9692（最高）**，参数 16.6M。NAFNet 33.71/0.9668/67.9M（Ours PSNR 至少高 0.5 dB、参数约 1/4）；Restormer 32.92/0.9611/26.1M；Restormer-local 33.57/0.9656；Stripformer 33.08/0.9624/19.7M；Uformer-B 33.06/0.9670/50.9M；DeepRFT+ 33.23/0.9632。
- **RealBlur（Table 2）**：RealBlur-R **40.11/0.9732**、RealBlur-J **32.62/0.9326**，PSNR 均最优。
- **HIDE（Table 3）**：GoPro 训练模型迁移测试，参数 16.6M；具体 PSNR/SSIM 数值在提取缓存中被截断（据原文后续页，待核）。
- **效率**：作者指出 PyTorch FFT 未优化，**Ours 0.13s**（256×256），慢于 MIMO-Unet+（0.02s），但**比 IPT（0.50s）至少快 4 倍**；图 1 显示精度领先、FLOPs 中等偏下。
- **可视化（图 3/4）**：对比方法在字符、椅子等主结构上残留模糊或恢复不佳，本文结果更清晰。
- **消融**：因篇幅置于补充材料，提取缓存未覆盖（待核）。

## 7. 这篇论文真正有价值的地方
1.  **卷积定理 × 注意力**：用频域逐元素乘积替代 QK^T，理论依据扎实、复杂度从 O(N²) 降到 O(N log N)，为高效注意力提供新范式。
2.  **JPEG → DFFN**：把图像压缩里的「频率量化/选择」转成可学习量化矩阵，是领域知识注入网络的范例。
3.  **非对称结构的实证洞见**：基于「模糊破坏 patch 相似度」的观察决定 FSAS 只放解码器，打破对称设计惯性。
4.  **强效率-性能平衡**：1/4 参数取得 +0.5 dB GoPro PSNR，对部署有价值。

## 8. 局限与问题
- **运行时受 FFT 实现拖累**：PyTorch FFT 未优化，0.13s 未完全体现频域理论效率。
- **消融证据在提取范围外**：各模块独立贡献置于补充材料，提取缓存未覆盖，无法据正文核验（待核）。
- **频域对高频敏感**：噪声/纹理等高频在极端模糊/复杂退化下的鲁棒性需进一步验证（推断，PDF 文本未专门讨论）。
- **退化范围**：仅运动模糊（合成 GoPro + 真实 RealBlur/HIDE），散焦/复合退化泛化性待考察。
- **复现门槛**：FFT/IFFT、JPEG patch unfold/fold、量化矩阵初始化与学习、8×8 设置等细节多，需对照官方代码。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 图 2 + 图 1/Table 1。
- **复现**：精读 3.1-3.3（式 3-8）配图 2(b)(c)，落实 4.1 全部训练细节（10⁻³→10⁻⁷ 余弦退火、600k 迭代、256×256/batch16、量化矩阵 8×8），参照官方代码 FFTformer。
- **借鉴创新点**：FSAS 频域相关计算可迁移到立体匹配/光流等；DFFN 的经典算法门控思路可移植到其他 FFN；非对称设计可按编/解码器特征状态差异化放模块。
- **写 related work**：归入「高效图像复原 Transformer」「频域在深度学习中的应用（DeepRFT 等）」「图像去模糊深度学习方法」。

## 10. 和其他论文的关系
- **频域方法**：`[[DeepRFT]]`（文中 DeepRFT+ 为对比项），同探频域信息，但本文聚焦把频域思想用于注意力计算与判别性 FFN。
- **高效图像复原 Transformer**：`[[Restormer]]`（主要对比，通道维注意力）、`[[Stripformer]]`（条状 token 注意力）、`[[Uformer]]`（非重叠窗口注意力）；本文提供基于频域的高效替代。
- **图像去模糊方法**：CNN 类 `[[MIMO-Unet+]]`、`[[MPRNet]]`、`[[NAFNet]]`，Transformer 类 `[[IPT]]` 等，均为实验对比对象。

## 11. 关键词
图像去模糊, Transformer, 频域, 注意力机制, 快速傅里叶变换 (FFT), 卷积定理, 前馈网络 (FFN), JPEG 压缩, 可学习量化矩阵, 非对称编码器-解码器, 高效计算, 底层视觉, 自注意力

## 12. 可信度说明
本精读主要基于提取文本的以下部分：
- **摘要**：核心思想、动机、贡献、结论。
- **引言**：研究背景、现有方法问题、动机与四点贡献。
- **相关工作**：CNN 与 Transformer 去模糊方法的定位（含 Restormer/Stripformer/Uformer 的注意力策略对比）。
- **方法（第 3 节）**：FSAS（式 3-6）、DFFN（式 7）、非对称网络（式 8）的原理与公式，是方法详解的主要依据。
- **实验（4.1-4.2）**：数据集、参数设置（学习率/迭代/patch/batch/量化矩阵 8×8）、GoPro Table 1、RealBlur Table 2 的定量结果与效率分析。
提取缓存覆盖 10/10 页、约 25000/41176 字符，**HIDE 的 Table 3 具体 PSNR/SSIM、消融实验与更多可视化在后续页被截断**，相应处已标注「待核」。除明确标注的 1-2 处推断外，笔记其余声明均可在提取文本中找到支撑，无编造。

---

> **可信度补充**: PDF 提取质量 = **high** (2504 字符/页, 10/10 页), 但提取缓存仅含前 25000/41176 字符, HIDE Table 3 数值/消融/部分可视化未覆盖; 来源缓存: `.paper-cache/extracts/FSAS&DFFN.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 2026-06-18 据提取文本复核优化 (重建摘要、补 600k 迭代/8×8 自注意力/RealBlur SSIM 等细节, 主题改判 E_图像复原)。
<!-- AI_READING_NOTE_END -->
