---
title: "CasDyF-Net: Image Dehazing via Cascaded Dynamic Filters"
authors:
  - "Yinglong Wang"
  - "Bin He"
year: 2024
venue: "arXiv"
doi: 
pdf: [[CasDyFBlock&RMB&LFB.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
extract_cache: .paper-cache/extracts/CasDyFBlock&RMB&LFB.txt
---

# CasDyF-Net: Image Dehazing via Cascaded Dynamic Filters

## 基本信息
- **PDF**: [[CasDyFBlock&RMB&LFB.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | CasDyF-Net: Image Dehazing via Cascaded Dynamic Filters |
| **作者** | Yinglong Wang; Bin He（西南交通大学 计算与人工智能学院） |
| **发表时间** | 2024（arXiv:2409.08510v1, 2024-09-13） |
| **刊物/会议** | arXiv (cs.CV) |
| **代码** | https://github.com/dauing/CasDyF-Net |
| **DOI** | 未明确 |

## 摘要

**英文原文（据 PDF 提取文本整理，修复断词与空格）：**

> Image dehazing aims to restore image clarity and visual quality by reducing atmospheric scattering and absorption effects. While deep learning has made significant strides in this area, more and more methods are constrained by network depth. Consequently, lots of approaches have adopted parallel branching strategies. However, they often prioritize aspects such as resolution, receptive field, or frequency domain segmentation without dynamically partitioning branches based on the distribution of input features. Inspired by dynamic filtering, we propose using cascaded dynamic filters to create a multi-branch network by dynamically generating filter kernels based on feature map distribution. To better handle branch features, we propose a residual multiscale block (RMB), combining different receptive fields. Furthermore, we also introduce a dynamic convolution-based local fusion method to merge features from adjacent branches. Experiments on RESIDE, Haze4K, and O-Haze datasets validate our method's effectiveness, with our model achieving a PSNR of 43.21dB on the RESIDE-Indoor dataset. The code is available at https://github.com/dauing/CasDyF-Net.

**中文翻译：**

> 图像去雾旨在通过减弱大气散射与吸收效应来恢复图像的清晰度与视觉质量。尽管深度学习在该领域已取得显著进展，越来越多的方法却受限于网络深度。为此，许多方法采用了并行分支策略；然而它们往往侧重于分辨率、感受野或频域分割等方面，而没有根据输入特征的分布来动态地划分分支。受动态滤波（dynamic filtering）启发，我们提出使用级联动态滤波器（cascaded dynamic filters），根据特征图分布动态生成滤波器核，从而构建多分支网络。为更好地处理各分支特征，我们提出了结合不同感受野的残差多尺度模块（RMB）。此外，我们还引入了一种基于动态卷积的局部融合方法，用于融合相邻分支的特征。在 RESIDE、Haze4K 与 O-Haze 数据集上的实验验证了方法的有效性，模型在 RESIDE-Indoor（SOTS-Indoor）数据集上达到 43.21dB 的 PSNR。代码已开源。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：图像去雾是计算机视觉的重要前置任务——雾霾（水汽、烟、尘等粒子造成的大气散射）会降低图像质量，进而影响目标检测、语义分割、自动驾驶等下游任务。传统先验方法（如暗通道先验 DCP）依赖人工设计特征，在不同光照与雾浓度下泛化性差，且常有计算不准确的问题。
- **之前方法的问题**：深层 CNN 面临梯度消失与精度退化（diminishing returns）。多分支并行网络是一种缓解方案，但现有分支创建策略是**静态的**：基于分辨率的方法会丢失高频细节；基于固定感受野的方法可能忽略语义、产生冗余特征；基于频域的方法无法随图像内容自适应。这些策略都**没有根据输入特征的分布动态划分分支**。
- **核心矛盾 / 思路**：受动态滤波核启发，作者主张用**级联动态滤波**构建多分支结构——每个滤波器隔离特定频带并动态调整，从而在不同层级提取更丰富的特征，自适应地应对复杂雾霾场景。

## 关键贡献

论文在引言末明确列出 5 条贡献：

1.  **新的去雾架构**：利用动态滤波核创建**可自适应的特征分支**（级联动态滤波 DFS），根据输入特征图分布动态生成卷积核来分割特征。
2.  **残差多尺度模块（RMB）**：使用三个不同**膨胀率（dilation rate）**的 3×3 卷积核提取从精细到粗略的多尺度感受野特征，再用 1×1 卷积融合，增强多尺度信息利用与表征能力（论文将其与 RB/MB/DB/RDB 等经典残差块对比，见 Fig.2）。
3.  **基于动态卷积的局部融合模块（LFB）**：用 1×1 动态卷积融合相邻频带/分支，以较小计算代价提升融合连续性并保留各频带特性。
4.  **渐进式融合策略**：将 LFB 的局部融合与全局注意力（采用文献中的 Enhanced Parallel Attention, EPA）结合，由局部到全局逐步整合分支特征，兼顾清晰度与自然度。
5.  **多数据集全面测试**：在多个公开数据集验证有效性，性能与效率均优于当时 SOTA。

> 量化亮点（据引言/实验）：相比同样用动态滤波的 CNN 方法 FSNet，CasDyF-Net 仅用其约 36.5% 的参数与约 46.8%~46.9% 的 FLOPs，在 ITS 上 +0.76dB、在 Haze4K 上 +1.61dB；相比 Transformer 方法 MB-TaylorFormer-L，用其约 84% 参数、约 47% FLOPs，在 ITS 上 +0.57dB。

## 方法

- **整体框架**：CasDyF-Net 采用经典 U 形编码器-解码器结构（Fig.3(a)），编/解码器核心组件是本文的 **CasDyF-Block**。该 Block 含三个过程：动态分割（Dynamic Segmentation）、局部融合（Local Fusion）、全局融合（Global Fusion），其中动态分割包含动态滤波（DFS）与 RMB（Fig.3(b)）。
- **输入输出与跳连**：输入三通道带雾图像 H×W×3；首个卷积层将通道数升到 C（H×W×C）。网络含多个跳连——前两个编码器的信息作为残差加到后两个解码器之前。仿照 FSNet（文献[45]），额外输入两张低分辨率图像辅助学习低层特征；后两个解码器后接两个卷积层重建低分辨率图像，引导网络逐级恢复清晰图像。
- **关键模块**：
    1.  **动态特征分割 DFS**（Fig.3(c)，公式(1)-(6)）：动态滤波器将特征图分解为**两个**频率成分。对第 i 级输入 `Xi`，先经全局平均池化 GAP → 卷积 `Wi` → 批归一化 BN → Softmax `S` 生成滤波核 `Ki=S(BN(Wi(GAP(Xi))))`（公式(1)），再与 `Xi` 卷积得滤波结果 `Yi=Ki∗Xi`（公式(2)）。`Yi` 作为一个独立分支，经 1×1 卷积降通道（`Wout_i`）与 RMB 细化得分支特征 `Fi=RMB_i(Wout_i(ReLU(BN(Yi))))`（公式(3)）；最后一级 `Fn=Xn`（公式(4)）。为不丢信息，下一级输入用**互补特征** `Xi+1=Wnext_i(Xi−Yi)`（公式(5)，借鉴频率选择思想）。共 `n−1` 个级联 DFS 单元，整体分割流程见公式(6)。
    2.  **残差多尺度模块 RMB**（Fig.3(e)）：用于细化分割后的频带特征。并行使用三个**膨胀率不同**的 3×3 卷积核（感受野由细到粗，对不同频带敏感），其输出再通过**两个 1×1 卷积层**融合。设计动机：大核卷积有效但缺乏灵活性且增大模型；用膨胀卷积可在不增计算的前提下扩大感受野（受 LKD-Net[21] 启发）。论文用 Fig.2 将 RMB 与 SRResNet 的 RB、MemNet 的 MB、SRDenseNet 的 DB、RDN 的 RDB 对比。
    3.  **渐进式注意力融合**（Progressive Attention Fusion）：
        - **局部融合 LFB**（Fig.3(d)，公式(7)）：为每个分支动态生成独立的 1×1 卷积参数（动态 1×1 卷积），对相邻三个分支加权融合，并对当前分支加残差连接。边界处理：`i=1` 融合 `(Fi,Fi+1,Fi+2)`；`i=2..n-1` 融合 `(Fi-1,Fi,Fi+1)`；`i=n` 融合 `(Fi-2,Fi-1,Fi)`。
        - **全局融合**：采用文献[22]（MixDehazeNet）的 **Enhanced Parallel Attention (EPA)**，结合多个 1×1 卷积，作为全局注意力融合模块，整合全部分支。
- **模块间连接**：级联 DFS 产生 n 个分支 → 各分支经 RMB 细化 → 各分支经 LFB 与相邻分支初步融合 → 全部送入 EPA 全局融合。
- **损失函数**（公式(8)）：三个尺度输出损失之和，每个尺度同时含**空间域 L1 损失**与**频域 L1 损失**（对预测与 GT 做 FFT 后取 L1），频域损失系数 `λ=0.1`（沿用文献[45]）。
- **训练**：NVIDIA A800 GPU，余弦退火学习率（衰减到 1e-6）。ITS/Haze4K：patch 256×256、batch 8、初始 lr 4e-4、1000 epochs；Dense-Haze/O-HAZE：patch 600×800、batch 2、初始 lr 2e-4、5000 epochs。
- **与已有方法差异**：相比同用动态滤波的 FSNet，本文用级联 DFS 实现多级精细分割、用 RMB 增强多尺度表征、用动态 1×1 卷积 LFB 实现灵活局部融合，并以"局部→全局"渐进融合替代直接全局融合。

## 实验

- **数据集**：
    - 合成：RESIDE 的 ITS（13,990 训练 / SOTS-Indoor 500 测试）与 OTS（313,740 训练 / SOTS-Outdoor 500 测试）；Haze4K（3000 训练 / 1000 测试）。
    - 真实：Dense-Haze（55 对）、O-HAZE（45 对），各取最后 5 张作测试，其余训练。
- **对比方法**：GridDehazeNet、FFA-Net、MAXIM、PMNet、DehazeFormer-L、OKNet、DSANet、FSNet、MixDehazeNet-L、MB-TaylorFormer-L、ConvIR-B/L、MSBDN、DeHamer、SGID-PFF、DehazeNet、AOD-Net、DMT-Net 等。
- **评价指标**：PSNR(dB)、SSIM、参数量 Params(M)、FLOPs(G)。
- **主实验结果**：
    - **SOTS-Indoor（Table I）**：CasDyF-Net **43.21 dB / 0.997**，为表中最佳（次优 ConvIR-B 42.72、MB-TaylorFormer-L 42.64、MixDehazeNet-L 42.62、FSNet 42.45）；参数 6.23M、FLOPs 40.55G。
    - **SOTS-Outdoor（Table I）**：CasDyF-Net 38.86 / 0.995，**并非最佳**（FSNet 40.40、ConvIR-B 39.42 更高），论文未在文中强调室外结果。
    - **Haze4K（Table II）**：CasDyF-Net **35.73 dB / 0.99**，为表中最佳（次优 ConvIR-L 34.50、FSNet 34.12）；参数 6.23M、FLOPs 40.55G。
    - **真实数据集（Table III）**：Dense-Haze **17.56 / 0.658**、O-HAZE **25.44 / 0.936**，均为表中最佳。Dense-Haze 领先约 0.7dB；O-HAZE 仅领先 0.08dB，但 SSIM 领先 0.156（作者解释为 SSIM 受单样本影响小、模型更稳定）。
    - 注：Table III 中"我方"行标注为 **"DFLS-Net (ours)"**，与正文 CasDyF-Net 不一致，疑为论文笔误/早期命名残留（据原文，待核）。
- **消融实验**（Haze4K，1000 epochs）：
    - **各模块有效性（Table IV）**：(a) 基线 31.58 dB / 3.96M / 27.02G；(b) +local 33.80（+2.22dB，仅 +1GFLOPs）；(c) 仅 global(EPA) 30.61（**反而低于基线**，作者归因于缺残差致分支差异过大，全局注意力难整合）；(d) local+global 34.16（较基线 +2.58dB，验证渐进融合）；(e) local+global+RMB 35.73（再 +1.57dB，仅多 0.35M 参数 / 3.3GFLOPs）。
    - **RMB 数量（Table V）**：0/1/2/3 个 RMB 对应 34.16 / 35.39 / 35.73 / 35.59 dB；超过 2 个性能下降（疑过拟合），故最终用 **2 个 RMB**。
    - 此外还做了 RMB 与其他先进模块的替换对比（Table VI，提取文本截断处未给全），以及用 FFT 对 RMB 频域特性的定性分析。
- **效率**：参数 **6.23M**、FLOPs **40.55G**，显著低于 FSNet（13.28M / 111G）、MB-TaylorFormer-L（7.41M / 86.3G）、MAXIM（14.1M / 216G）、FFA-Net（4.456M / 287.8G）等。

## 局限

1.  **室外/部分真实场景优势不明显**：SOTS-Outdoor 上 PSNR(38.86) 低于 FSNet(40.40)、ConvIR-B(39.42)，论文回避了室外对比；O-HAZE 上 PSNR 仅领先 0.08dB（靠 SSIM 优势支撑结论）。
2.  **计算成本**：虽比多数对比方法高效，但 40.55G FLOPs 对移动端/实时应用仍偏高，仍有轻量化空间。
3.  **结构复杂、可复现性**：DFS、RMB、LFB、EPA 多模块叠加，分支数 n、各分支膨胀率等超参在提取文本中未完全给出，复现细节有缺口。
4.  **真实数据规模极小**：Dense-Haze 55 对、O-HAZE 45 对，且各仅 5 张测试，结论的统计可靠性有限，更广泛真实场景泛化性待检验。
5.  **命名/表格不一致**：Table III "DFLS-Net (ours)" 与正文方法名不符，影响严谨性（据原文，待核）。

## 个人评论

1.  **动态划分特征分支的思想有迁移价值**：不固定分支结构，而让网络依据输入特征分布动态生成滤波核来"决定"如何分频/分支。这种自适应思路对去雨、去模糊、低光增强等低级视觉任务同样有启发；本质是把"频带分解"做成可学习、可级联的算子。
2.  **"局部→全局"渐进融合是本文最有说服力的设计**：消融显示单独用全局注意力(EPA)甚至低于基线（30.61 vs 31.58），而先用 LFB 做相邻分支局部融合再上全局注意力则大幅提升。这说明在多分支差异较大时，先做局部对齐/平滑再全局整合，比直接全局融合更稳定——是一个可复用的工程经验。
3.  **效率-性能平衡务实**：大量使用 1×1 卷积与膨胀卷积，在 6.23M/40.55G 下达到 SOTS-Indoor 43.21dB，对实际部署有参考意义。
4.  **保留批判**：室外结果不占优却未充分讨论、真实集规模过小、以及 Table III 命名笔误，都削弱了"全面 SOTA"的说服力。读者引用其数字时应区分"室内显著领先"与"室外/真实场景仅小幅或不领先"。

### 使用建议

- **快速了解**：读摘要 + 引言，看 **Fig.3**（整体架构与 DFS/LFB 模块图）即可掌握核心。
- **复现**：精读第 III 节 A–E（各模块公式(1)-(8)）与第 IV 节 A 实验设置（GPU、patch、batch、lr、epochs、数据集划分）。注意分支数 n 与膨胀率等超参需结合开源代码确认。
- **借鉴创新点**：重点学 **DFS（动态生成滤波核做频带分割）** 与 **RMB（多膨胀率 + 1×1 融合）**，思考"动态卷积核 + 互补残差 `Xi−Yi` 级联"能否迁移到超分、去雨、分割等任务。
- **写 related work**：可放在**多分支网络**或**动态卷积/动态滤波**脉络下，与 FSNet、ConvIR、MB-TaylorFormer、MixDehazeNet 对比。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉**底层视觉 / 图像复原**领域，具体任务是**单幅图像去雾（single image dehazing）**。在本知识库 taxonomy 中归入 `E_图像复原_超分_去噪_去雨去雾`（去雾属图像复原范畴）。论文确实大量使用注意力（LFB 局部融合 + EPA 全局注意力），但其本质是一个完整的去雾网络架构，而非一个独立的注意力算子模块，因此 primary_topic 由原 `B_注意力算子模块` 修正为 `E`。发表于 arXiv（2024-09-13, 2409.08510v1），作者来自西南交通大学，代码开源。

## 2. 一句话总结
CasDyF-Net 用**级联动态滤波器**根据特征图分布动态生成滤波核，把特征自适应地分割成多个频带分支，再以**残差多尺度模块 RMB**细化、以**动态 1×1 卷积局部融合 LFB + 全局并行注意力 EPA**做"局部→全局"渐进融合，在 6.23M/40.55G 的低开销下实现高质量去雾（SOTS-Indoor 43.21dB）。

## 3. 背景与问题
- **任务价值**：去雾是检测、分割、自动驾驶等任务的前置，雾霾由水汽/烟/尘等粒子的大气散射造成。
- **传统方法局限**：DCP 等先验方法依赖人工特征，跨光照/雾浓度泛化差。
- **深度方法瓶颈**：深层 CNN 有梯度消失与精度退化；多分支网络虽能缓解，但分支创建是**静态的**（分辨率/固定感受野/预设频域），无法随输入特征分布自适应——基于分辨率的丢高频、基于频域的不适配内容。
- **本文主张**：用级联动态滤波动态分频建多分支，每个滤波器隔离特定频带并自适应调整。

## 4. 核心贡献
对应引言 5 条：(1) 动态滤波核创建自适应分支的去雾架构（DFS）；(2) 多膨胀率 3×3 + 1×1 融合的残差多尺度块 RMB；(3) 基于动态 1×1 卷积、低成本的局部融合 LFB；(4) 局部+全局注意力的渐进融合策略；(5) 多公开数据集验证。量化卖点：相比 FSNet 用 ~36.5% 参数 / ~46.8% FLOPs 取得 ITS +0.76dB、Haze4K +1.61dB；相比 MB-TaylorFormer-L 用 ~84% 参数 / ~47% FLOPs 取得 ITS +0.57dB。

## 5. 方法详解
- **架构**：U 形编解码（Fig.3(a)），核心是 CasDyF-Block（动态分割 + 局部融合 + 全局融合）。含编→解码器的残差跳连；仿 FSNet 额外输入 2 张低分图、解码端重建低分图以多尺度监督。
- **DFS（公式1-6）**：`Ki=S(BN(Wi(GAP(Xi))))` → `Yi=Ki∗Xi`（把特征分解为两个频率成分）；`Fi=RMB_i(Wout_i(ReLU(BN(Yi))))`，`Fn=Xn`；下一级输入用互补残差 `Xi+1=Wnext_i(Xi−Yi)`。共 n−1 个级联单元。
- **RMB**：三个不同膨胀率 3×3 卷积（细→粗感受野，对不同频带敏感）+ 两个 1×1 卷积融合；动机是用膨胀卷积替代大核以低成本扩感受野（受 LKD-Net 启发），并在 Fig.2 与 RB/MB/DB/RDB 对比。最终每分支用 2 个 RMB。
- **渐进融合**：LFB（公式7）用动态 1×1 卷积加权融合相邻三分支并加残差，边界分支调整取邻；全局用 EPA（来自 MixDehazeNet[22]）+ 多个 1×1 卷积。
- **损失（公式8）**：三尺度，每尺度 = 空间 L1 + 频域(FFT) L1，λ=0.1。
- **训练**：A800；ITS/Haze4K patch256 batch8 lr4e-4 1000ep；Dense/O-HAZE patch600×800 batch2 lr2e-4 5000ep；余弦退火→1e-6。

## 6. 实验与结果
- **数据**：ITS(13990训/SOTS-Indoor 500测)、OTS(313740训/SOTS-Outdoor 500测)、Haze4K(3000/1000)、Dense-Haze(55对)、O-HAZE(45对，各末5张测)。
- **SOTS-Indoor（Table I）**：43.21/0.997 最佳，6.23M/40.55G；次优 ConvIR-B 42.72。
- **SOTS-Outdoor（Table I）**：38.86/0.995，逊于 FSNet 40.40、ConvIR-B 39.42（非最佳，论文未强调）。
- **Haze4K（Table II）**：35.73/0.99 最佳，次优 ConvIR-L 34.50。
- **真实（Table III）**：Dense-Haze 17.56/0.658、O-HAZE 25.44/0.936，均最佳；O-HAZE PSNR 仅 +0.08dB 但 SSIM +0.156。该行表头误标"DFLS-Net (ours)"（据原文，待核）。
- **消融（Haze4K, Table IV）**：基线 31.58 → +local 33.80 → 仅 global(EPA) 30.61（低于基线）→ local+global 34.16 → +RMB 35.73。
- **RMB 数量（Table V）**：0/1/2/3 → 34.16/35.39/35.73/35.59，取 2 个。
- 另有 RMB 替换对比（Table VI，提取文本于此截断未给全）与 FFT 频域定性分析。
- **效率**：6.23M/40.55G，远低于 FSNet 13.28M/111G、MB-TaylorFormer-L 7.41M/86.3G。

## 7. 这篇论文真正有价值的地方
1.  **动态分频建分支**：用可学习滤波核 + 互补残差 `Xi−Yi` 级联，把"频带分解"做成自适应、可堆叠的算子，对多种低级视觉任务有迁移性。
2.  **渐进式融合的强证据**：消融显示单独全局注意力反而掉点（30.61<31.58），先局部后全局才有效——一个可复用的多分支融合经验。
3.  **效率优先**：1×1 + 膨胀卷积组合，在 6.23M/40.55G 达 43.21dB，部署友好。

## 8. 局限与问题
1.  室外（SOTS-Outdoor）PSNR 不占优却被回避，"全面 SOTA"表述偏乐观。
2.  40.55G FLOPs 对实时/移动端仍偏高。
3.  多模块叠加、分支数与膨胀率等超参未在提取文本中完整给出，复现有缺口。
4.  真实集规模极小（55/45 对、各 5 张测），统计可靠性弱。
5.  Table III 命名笔误（DFLS-Net）削弱严谨性（据原文，待核）。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + Fig.3。
- **复现**：第 III 节 A–E（公式1-8）+ 第 IV.A 实验设置；分支数/膨胀率参照开源代码。
- **借鉴**：DFS（动态核 + 互补残差级联）与 RMB（多膨胀率 + 1×1 融合）；考虑迁移到超分/去雨/分割。
- **写 related work**：归入多分支网络 / 动态滤波脉络，对照 FSNet、ConvIR、MB-TaylorFormer、MixDehazeNet。

## 10. 和其他论文的关系
本文紧密对照并改进了 **FSNet**（同用动态滤波，文献[45]，本文多处沿用其设计：互补残差、低分图监督、λ=0.1）。全局融合直接复用 **MixDehazeNet** 的 **Enhanced Parallel Attention (EPA)**（文献[22]）。RMB 受 **LKD-Net** 膨胀卷积思想启发（文献[21]），并在 Fig.2 与 **SRResNet(RB)/MemNet(MB)/SRDenseNet(DB)/RDN(RDB)** 等残差块谱系对比。性能上与 **ConvIR、MB-TaylorFormer-L、DehazeFormer、FFA-Net、PMNet** 等去雾 SOTA 比较。提取文本未给出可直接双链的库内笔记 ID，故此处仅按方法脉络关联，不创建不确定链接。

## 11. 关键词
图像去雾, 动态滤波, 级联动态滤波器, 多分支网络, 频带分割, 残差多尺度块(RMB), 膨胀卷积, 动态卷积, 局部融合(LFB), 全局注意力(EPA), 渐进式融合, 频域损失, U型网络, 图像复原, 计算机视觉

## 12. 可信度说明
本精读基于 PDF 提取文本（9/9 页，约 2782 字符/页，质量良好）生成。标题、作者、单位、arXiv 号、摘要、引言、相关工作、方法全部公式(1)-(8)、实验设置、Table I/II/III/IV/V 的关键数值、消融结论均可在提取文本中直接核对，置信度高。需注意：(a) 提取文本在 25000 字符处截断，Table VI（RMB 与其他模块替换对比）的具体数值与后续 FFT 定性分析未覆盖，本笔记已标注"截断/待核"；(b) Fig.4-7 为可视化对比，纯文本仅有图题，无法核其视觉内容，但对应定量结果已在表格给出；(c) Table III 的方法名 "DFLS-Net (ours)" 与正文 CasDyF-Net 不一致，按原文如实记录并标注待核。本笔记对技术核心、实验框架与主要结论的总结准确、有据。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本 9/9 页, ~2782 字符/页, 结构完整; 第 25000 字符后截断, Table VI 及 FFT 分析未覆盖); 来源缓存: `.paper-cache/extracts/CasDyFBlock&RMB&LFB.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
