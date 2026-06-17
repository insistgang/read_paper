---
title: "HiFi-Mamba: Dual-Stream w-Laplacian Enhanced Mamba for High-Fidelity MRI Reconstruction"
authors:
  - "Hongli Chen"
  - "Pengcheng Fang"
  - "Yuxia Chen"
  - "Yingxuan Ren"
  - "Jing Hao"
  - "Fangfang Tang"
  - "Xiaohao Cai"
  - "Shanshan Shan"
  - "Feng Liu"
year: 2026
venue: AAAI 2026
doi: 
pdf: [[HiFi-Mamba MRI重建 HiFi-Mamba MRI Reconstruction.pdf]]
primary_topic: A2_医学图像_分类_配准_生成
topics:
  - "A2_医学图像_分类_配准_生成"
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
extract_cache: .paper-cache/extracts/HiFi-Mamba MRI重建 HiFi-Mamba MRI Reconstruction.txt
---

# HiFi-Mamba: Dual-Stream w-Laplacian Enhanced Mamba for High-Fidelity MRI Reconstruction

## 基本信息
- **PDF**: [[HiFi-Mamba MRI重建 HiFi-Mamba MRI Reconstruction.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | HiFi-Mamba: Dual-Stream w-Laplacian Enhanced Mamba for High-Fidelity MRI Reconstruction |
| **作者** | Hongli Chen; Pengcheng Fang; Yuxia Chen; Yingxuan Ren; Jing Hao; Fangfang Tang; Xiaohao Cai; Shanshan Shan; Feng Liu |
| **单位** | 昆士兰大学、南安普顿大学、苏州大学、成都交子金控、新加坡国立大学、香港大学（按作者署名顺序） |
| **发表时间** | 2026 (AAAI 2026; arXiv:2508.09179v2, 2026-01-13) |
| **刊物/会议** | AAAI 2026 (Copyright © 2026, AAAI) |
| **代码** | https://github.com/HongliChen-Ali/HiFi-Mamba.git |
| **DOI** | 未明确 |

## 摘要

> **英文原摘要（据 PDF 提取文本整理，已修复断字与连字符）**
>
> Reconstructing high-fidelity MR images from undersampled k-space data remains a challenging problem in MRI. While Mamba variants for vision tasks offer promising long-range modeling capabilities with linear-time complexity, their direct application to MRI reconstruction inherits two key limitations: (1) insensitivity to high-frequency anatomical details; and (2) reliance on redundant multi-directional scanning. To address these limitations, we introduce High-Fidelity Mamba (HiFi-Mamba), a novel dual-stream Mamba-based architecture comprising stacked w-Laplacian (WL) and HiFi-Mamba blocks. Specifically, the WL block performs fidelity-preserving spectral decoupling, producing complementary low- and high-frequency streams. This separation enables the HiFi-Mamba block to focus on low-frequency structures, enhancing global feature modeling. Concurrently, the HiFi-Mamba block selectively integrates high-frequency features through adaptive state-space modulation, preserving comprehensive spectral details. To eliminate the scanning redundancy, the HiFi-Mamba block adopts a streamlined unidirectional traversal strategy that preserves long-range modeling capability with improved computational efficiency. Extensive experiments on standard MRI reconstruction benchmarks demonstrate that HiFi-Mamba consistently outperforms state-of-the-art CNN-based, Transformer-based, and other Mamba-based models in reconstruction accuracy while maintaining a compact and efficient model design.

> **中文翻译**
>
> 从欠采样 k 空间数据重建高保真 MR 图像仍是 MRI 中的难题。视觉任务上的 Mamba 变体凭借线性时间复杂度具备良好的长程建模能力，但将其直接用于 MRI 重建会继承两项关键局限：(1) 对高频解剖细节不敏感；(2) 依赖冗余的多方向扫描。为此，作者提出 High-Fidelity Mamba（HiFi-Mamba）——一种由堆叠的 w-Laplacian（WL）块与 HiFi-Mamba 块构成的双流 Mamba 架构。具体而言，WL 块执行保真度保持的频谱解耦，产出互补的低频流与高频流；这种分离使 HiFi-Mamba 块得以专注于低频结构、增强全局特征建模。与此同时，HiFi-Mamba 块通过自适应状态空间调制选择性地融合高频特征，从而保留完整的频谱细节。为消除扫描冗余，HiFi-Mamba 块采用精简的单向遍历策略，在提升计算效率的同时保持长程建模能力。在标准 MRI 重建基准上的大量实验表明，HiFi-Mamba 在重建精度上一致优于当前最先进的 CNN、Transformer 与其他 Mamba 模型，同时保持紧凑高效的模型设计。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：MRI 因无创、软组织对比度高而成为临床不可或缺的成像方式，但其主要短板是采集时间长（易引起患者不适、增加运动伪影风险）。为加速扫描，现代协议普遍在频率域（k 空间）做欠采样，这虽缩短了扫描时间，却违反奈奎斯特–香农采样定理，导致混叠伪影与图像质量下降。因此需要先进的重建算法从不完整的 k 空间数据中恢复高保真图像。
- **之前方法的问题**：
    1.  **传统压缩感知（CS）方法**（如 Lustig 等 2007）：利用变换域（如小波）稀疏先验，但需大量超参数调优，对采样模式与噪声变化缺乏鲁棒性。
    2.  **基于 CNN 的方法**：通过建模层次化、局部化的解剖特征表现强劲；模型驱动的 CNN 还会融入 MRI 前向模型并强制数据一致性。但 CNN 固有的局部性限制了对**长程依赖**的捕捉，而长程依赖对恢复全局解剖结构（尤其在高欠采样下）至关重要。
    3.  **基于 Transformer 的方法**：通过自注意力计算全部空间 token 间的两两相关来建模全局依赖，在 MRI 重建中有前景；但标准 Transformer 复杂度为**二次方**，难以应对高分辨率 MRI。其高效变体（如 Swin Transformer 的分层、移位窗口注意力）虽降低开销，却把计算限制在局部邻域，重新陷入“计算效率 vs 全局建模”的根本权衡。
    4.  **直接将 Mamba 应用于 MRI 重建**：作者在引言中指出三个根本性局限：a) 现有视觉 Mamba（如 vMamba）用**多方向空间扫描**提升覆盖，却引入显著**计算冗余**（见 Figure 1(a)）；b) 其状态空间参数对每个空间 token **独立、局部地**生成，**缺乏空间邻域上下文**，忽略了对建模连贯解剖结构很关键的邻域信息；c) 现有 Mamba 变体**对高频成分不敏感**，而高频对保留精细解剖细节至关重要。
- **核心矛盾**：如何在保持**线性复杂度（计算效率）**的同时，有效捕捉**全局上下文依赖**，并特别保留对图像质量至关重要的**高频细节**。
- **注意**：摘要把上述归纳为“两项关键局限”（高频不敏感 + 多方向扫描冗余），引言进一步细化为“三个根本局限”（多了“局部参数化、缺乏空间感知”一项）。两处口径侧重不同但不矛盾。

## 关键贡献

1.  **提出新颖的 HiFi-Mamba 块**：采用高效的双流架构，使用**单向扫描**提升效率，并引入**跨流指导（cross-stream guidance）机制**，以同时化解 Mamba 固有的局部性与高频不敏感问题。
2.  **设计轻量级 w-Laplacian 块**：将特征解耦为**高频流**与**低频流**两个互补流，使 HiFi-Mamba 实现频率感知的双流处理。
3.  **取得 SOTA 结果**：在公开 MRI 基准上，HiFi-Mamba 一致优于领先的 CNN、Transformer 与其他 Mamba 基线，并在**重建保真度与计算效率之间建立更优的权衡**。

## 方法

**整体框架（Overall Pipeline）**：HiFi-Mamba 遵循**展开优化（unrolled optimization）框架**——求解 MRI 重建这类逆问题的强范式。网络骨干由 **K=8 个级联的 HiFi-Mamba 组（Group）** 构成；每个组含**两个连续的 Mamba 单元（Unit）** 做特征精炼，后接一个**数据一致性（DC）块**，把原始采集的 k 空间测量值强制融入重建。

> 注：训练细节一节又写道“模型为 **6×2 的 HiFi-Mamba 单元堆叠配置**”，与 Overall Pipeline 的“K=8 组、每组 2 单元”在组数上不完全一致；此处按原文如实并列记录两种表述，具体以代码为准。

**输入输出**：
- **输入**：欠采样图像 `I_in ∈ R^{H×W×2}`，两通道张量，分别表示复值 MR 数据的实部与虚部。
- **输出**：重建图像 `I_out ∈ R^{H×W×2}`。
- **补丁嵌入**：`F_in = P(I_in) ∈ R^{(H/P)×(W/P)×C}`，`P(·)` 为补丁嵌入操作。

**关键模块与连接（Mamba 单元，非对称双流）**：
1.  **流准备（频率解耦）**：输入特征图 `F_in` 沿通道拆为 `F1, F2 ∈ R^{H×W×(C/2)}`。`F1` 经 **w-Laplacian (WL) 块** 得低频分量 `F_low` 与残余高频分量 `F'_high`（式2）。`F2` 与 `F'_high` 逐元素相加，形成最终高频流 `F_high = F2 + F'_high`（式3）。
2.  **非对称并行处理**：
    - **高频流**：`F_high` 先经一个**条件精炼模块（CRM，Condition Refinement Module）** 提取解剖引导特征 `G = CRM(F_high)`（式4），`G` 捕捉空间高频结构、作为调制低频流的引导先验；再经第二个 CRM 精炼得 `F̃_high = CRM(G)`（式5）。CRM 负责**跨分辨率特征变换**。
    - **低频流**：`F_low` 在 **HiFi-Mamba 块** `H(·)` 中处理，**在引导图 `G` 的显式指导下**做长程依赖建模，`F̃_low = H(F_low | G)`（式6）。此**跨流指导**把高频线索注入全局上下文建模。
3.  **双流融合（DSFA）**：`F̃_low` 与 `F̃_high` 拼接后由**双流融合注意力（DSFA，Dual-Stream Fusion Attention）** 自适应加权融合为 `F_fused`（式7）。单元最终输出经残差连接 `F_out = F_fused + F_in`（式8）。

**w-Laplacian 块（WL）**：执行保真度保持的频谱解耦，目的：(1) 为 Mamba 流提供专门的低频输入；(2) 把高频特征抽到并行流做细节增强。设计动机：传统拉普拉斯金字塔是**面向分辨率**而非**面向频率**的，其低频分量只是模糊下采样近似、缺乏明确频谱语义；故改用**小波（wavelet）公式**实现结构化、可逆的频率分离。流程：
- 先用 CRM 精炼 `F1` 得 `F'1 = CRM(F1)`（式9）；
- 对 `F'1` 做逐通道 2D 离散小波变换（DWT），得 `{LL, LH, HL, HH}` 四个子带（式10）；
- 为避免直接用高频子带带来的信息损失与基依赖，先对 `LL` 子带上采样得到平滑低频基 `F_low = Upsample(LL)`（式11）；
- 高频残差定义为精炼图与该低频基之差 `F_high = F'1 − F_low`（式12）。

**HiFi-Mamba 块**：处理低频特征 `F_low` 并受解剖引导图 `G` 调制，针对标准 Mamba 引入两项关键改造（跨频率指导 + 空间感知参数精炼）：
1.  **初始参数生成**：先做投影并拆分得主特征 `F_c` 与残差 `Z`：`F_c, Z = Split(Linear(Norm(F_low)))`（式13）；`F_c` 经 2D 卷积 + SiLU 得上下文感知图 `F_conv = SiLU(Conv2D(F_c))`（式14）；将 `F_conv` 重排为序列 `F_s` 后线性投影并拆分，生成初始状态投影矩阵 `B, C` 与时间步参数 `Δ`：`[Δ, B, C] = Split(Linear(F_s))`（式15）。此阶段已含卷积带来的局部上下文，但**尚未**被高频流告知。
2.  **跨频率指导（Cross-Frequency Guidance）**：从引导图 `G` 投影出预条件张量 `B'_h, C'_h`，再各经一个独立门控：`B'_{h,1}, B'_{h,2} = Split(Linear(B'_h))`，`B_h = GELU(B'_{h,1}) ⊙ B'_{h,2}`（式16，`C_h` 同理但权重独立）；随后逐元素相加注入参数 `B = B + B_h`，`C = C + C_h`（式17）。门控作为动态滤波器，从 `G` 中蒸馏显著高频信息（如解剖边缘、混叠伪影）：`B_h` 调制 SSM 的**输入投影** `B`（条件化输入 `x(t)` 对状态 `h(t)` 的影响），`C_h` 调制**输出投影** `C`（确保高频细节被准确渲染到重建中）。对应状态/输出方程 `h'(t)=Ah(t)+Bx(t)`，`y(t)=Ch(t)`（式18）。
3.  **空间感知精炼（Spatially-Aware Refinement）**：对条件化后的 `B, C` 及时间步 `Δ` 各应用一个**核大小 k=7 的一维深度可分卷积**，使每个 token 的参数受空间邻居影响、注入局部上下文；对 `Δ` 卷积还能让状态转移动态在空间序列上平滑演化——以此弥补标准 Mamba“参数严格局部生成”的缺陷。
4.  **输出生成**：用精炼后的 `(Δ, B, C)` 执行选择性扫描（Selective Scan）得 `F_ssm`，最终 `F̃_low = Linear_out(F_ssm ⊙ SiLU(Z))`（式19），通过门控调制把 `F_ssm` 的长程上下文与 `Z` 的局部特征结合后再线性投影。

**数据一致性（DC）块**：每个组之后、以及反补丁化后的图像域最终输出前都施加 DC，确保重建与原始 k 空间一致。

**训练方式**：AdamW 优化器，初始学习率 `1×10⁻³`，余弦退火 + 5 epoch 预热，共训练 100 epoch，批大小 4，采用 ℓ1 损失。硬件：训练于 2 块 NVIDIA H100；FLOPs 在单块 A100 上测量；实现基于 PyTorch。

**推理流程**：欠采样图像 → 补丁嵌入 → 经 8 个级联组（每组 2 个 Mamba 单元 + DC 块） → 反补丁化恢复到 `R^{H×W×2}` → 图像域最终 DC 块 → 输出重建图像。

**和已有方法的差异**：
- 相比多方向扫描的 Mamba（vMamba 四方向、MambaMIR、LMO），改用**单向遍历**避免重复访问、减少冗余计算。
- 相比直接套用 Mamba，引入**频率解耦（WL 块）** 与**跨流指导**，显式处理高/低频、增强高频敏感性。
- 通过 **k=7 深度卷积的空间感知精炼**弥补 Mamba 参数生成过于局部的缺陷。

## 实验

- **使用的数据集**：
    1.  **fastMRI (knee)**：1,172 例复值单线圈冠状面膝关节扫描，PD 加权，每例约 35 个冠状切片，矩阵 320×320；仅用 **PDFS（质子密度脂肪抑制）** 子集做训练与评估，遵循官方划分；丢弃首尾各 5 个切片。
    2.  **CC359 (brain)**：临床扫描仪（GE Discovery MR750）采集的原始脑部 MR 数据，矩阵 256×256；官方划分 **25 例训练 / 10 例测试**；丢弃首尾各 15 个切片。
- **欠采样**：等间距 1D 笛卡尔欠采样掩模（来自 fastMRI 挑战赛）。AF=4 时中心 8% 的 k 空间线全采样；AF=8 时降至 4%。
- **预处理**：采用**统一、透明的预处理策略**（统一归一化方案）以避免强度分布不一致带来的不公平比较，细节（归一化、k 空间欠采样）见附录（提取缓存未覆盖）。
- **对比方法**：Zero-Filling（零填充基线）；CNN：UNet、ISTA-Net；Transformer：ReconFormer、FPSFormer；Mamba：LMO。
- **评价指标**：PSNR (↑)、SSIM (↑)、NMSE (↓)。
- **主实验结果（Table 1，AF=4×/8×）**：
    - **HiFi-Mamba (P2，补丁大小=2)** 在大多数场景一致优于现有方法，AF=8 提升尤为明显：fastMRI PSNR 31.38 dB（LMO 31.10）、CC359 PSNR 28.08 dB（LMO 27.99）；SSIM 也全面领先（fastMRI 8× 0.758 vs LMO 0.744；CC359 8× 0.802 vs 0.787）。
    - **HiFi-Mamba (P1，补丁大小=1)** 性能更优：fastMRI 4× 34.85 / 8× 31.81 dB；CC359 4× **36.93** dB（LMO 35.35）、8× 28.49 dB；NMSE 也最低。
    - 关键对照数字（PSNR，fastMRI 4×/8× | CC359 4×/8×）：Zero-Filling 29.25/25.95 | 24.79/21.27；UNet 31.66/28.60 | 28.27/24.28；ISTA 33.27/29.44 | 32.03/25.44；ReconFormer 33.75/30.42 | 32.46/26.47；FPSFormer 33.74/30.63 | 32.35/26.65；LMO 34.49/31.10 | 35.35/27.99。注：fastMRI 4× 上 P2(34.47) 略低于 LMO(34.49)，P1(34.85) 才超过——这是“across most evaluation scenarios（多数场景）”而非全部的来由。
- **效率信息（Table 2，提取缓存仅截到表头与前三行）**：ReconFormer 270.60G FLOPs（注意力扫描）、FPSFormer 200.45G（注意力）、LMO 484.98G（4 方向扫描）。**HiFi-Mamba 自身的 FLOPs 数值在提取缓存中被截断（表格行止于 “HiFi”），PDF 文本未覆盖**；文中以 LMO 的 484.98G 佐证多方向扫描开销大，并强调 HiFi-Mamba 保持“紧凑高效”的设计。模型参数量未在提取文本中给出。
- **消融实验**：提取缓存（前 25000 字符 / 共 40458 字符）未包含消融表格或段落，无法据此核实各模块（跨流指导、空间感知精炼、单向扫描）的单独贡献。

## 局限

1.  **效率对比不完整（提取层面）**：提取缓存未覆盖 Table 2 中 HiFi-Mamba 自身的 FLOPs，也未覆盖任何消融实验，故“高效”与各创新点的量化有效性在本笔记证据范围内无法完全核实（数值可能存在于原文后续页）。
2.  **数据集与场景有限**：仅在两个**单线圈** MRI 数据集（膝、脑）上评估，未验证多线圈 MRI 或其他模态（CT、超声）/更复杂解剖结构上的泛化性。
3.  **采样模式单一**：仅用等间距 1D 笛卡尔欠采样掩模；在非笛卡尔、可学习或更复杂采样模式下的稳健性未考察。
4.  **内部口径不一致**：Overall Pipeline 写 K=8 组、训练细节写 6×2 单元配置，组/单元数表述不统一，需结合代码确认实际深度。
5.  **复杂度与可复现性**：方法叠加多个新模块（WL、带指导的 HiFi-Mamba 块、CRM、DSFA），框架较复杂；虽提供代码链接，完整复现/调参仍有门槛。

## 个人评论

1.  **针对任务谱特性的架构设计**：把 MRI“低频载结构、高频载细节”的频谱先验显式编码为“频率解耦 + 双流异步处理 + 跨流指导”范式——让 Mamba 只啃低频长程结构、让 CRM/高频流补细节，思路清晰，对超分、去噪、去模糊等同样需兼顾全局结构与精细纹理的复原任务有迁移价值。
2.  **对 SSM 的“诊断式”改造**：不直接套 Mamba，而是逐条对应其三大短板给出模块化解法（多方向冗余→单向扫描；局部参数化→k=7 深度卷积空间感知精炼；高频不敏感→跨频率门控指导调制 B/C）。这种“先定位缺陷、再对症下药”的方式值得借鉴。
3.  **把高频信息注入 SSM 参数而非特征**：用引导项 `B_h/C_h` 直接调制 SSM 的输入/输出投影矩阵（而非简单做特征相加），是一个相对新颖的切入点——在状态空间层面而非纯特征层面引入条件，理论上更贴近 Mamba 的选择性机制。
4.  **公平比较意识**：强调统一透明的预处理以消除强度分布混淆，并把细节放附录，体现了对 MRI 重建领域“预处理不一致导致结果不可比”这一痛点的自觉。
5.  **可挑剔处**：fastMRI 4× 上 P2 并未超过 LMO，须靠更重的 P1 才领先；摘要“两局限”与引言“三局限”口径切换、以及 K=8 与 6×2 的不一致，都提示论文在表述精确性上仍有打磨空间。

### 使用建议

- **如果快速了解**：读 Abstract、Introduction（前两页引出三大局限的部分）、Experiments 的 Table 1 与结论段，即可抓住核心思想与主结果。
- **如果复现**：精读 Method 的 Overall Pipeline 与 Mamba Unit（式 1–8），结合 Figure 2 理解数据流；重点研读 w-Laplacian Block（式 9–12）与 HiFi-Mamba Block（式 13–19，尤其跨频率指导式 16–17 与 k=7 空间精炼），并核对附录预处理/超参；注意 K=8 与 6×2 的口径差异，以代码为准。
- **如果借鉴创新点**：
    - 频率解耦双流：可迁到去模糊、超分等需区分高低频的任务。
    - 跨流/跨模态指导：把一支特征（如边缘图/引导图）作为先验调制另一支主干，甚至像本文一样去调制 SSM 参数而非仅特征。
    - 单向扫描：思考视觉 Mamba 中如何简化扫描方向以省算力而不损长程建模。
- **如果写 Related Work**：可归入 1) 基于深度学习/展开优化的 MRI 重建；2) 状态空间模型（Mamba）在视觉的应用；3) 频率感知/小波驱动的神经网络设计。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**医学图像重建**方向，具体是**磁共振成像（MRI）加速重建**：从欠采样的 k 空间（频率域）数据重建高保真 MR 图像，是一项临床关键的逆问题。范式上属于“展开优化 + 深度学习先验”。它不是分割任务，而是图像重建/生成类问题。本知识库 taxonomy 中无独立的“重建”桶，重建在性质上最接近“生成”，故归入 **A2_医学图像_分类_配准_生成**（原归 `A1_医学图像_分割` 与正文不符，已纠正）。

## 2. 一句话总结
HiFi-Mamba 是一个面向 MRI 重建的双流状态空间（Mamba）架构：用 w-Laplacian 块做小波频谱解耦分出高/低频，让 Mamba 专注低频长程结构、用高频引导跨流调制其 SSM 参数，并以单向扫描替代多方向扫描，从而在 fastMRI/CC359 上以更高效率取得优于 CNN/Transformer/Mamba 基线的重建精度。

## 3. 背景与问题
- **为什么要做**：MRI 无创、软组织对比好但采集慢；为加速而在 k 空间欠采样会违反奈奎斯特准则，产生混叠伪影、降质，需要强重建算法恢复高保真图像。
- **之前方法的问题**：
    1.  **压缩感知（CS）**：依赖稀疏先验，超参多、对采样/噪声变化不鲁棒。
    2.  **CNN**：层次化局部特征强，但感受野受限、难捕长程依赖（高欠采样下尤甚）；模型驱动 CNN 虽加 DC 仍受局部性约束。
    3.  **Transformer**：全局自注意力强但复杂度二次方；Swin 类窗口注意力省算力却又限制感受野，回到“效率 vs 全局”的权衡。
    4.  **直接用 Mamba**：引言列三大根本局限——a) 多方向扫描带来计算冗余；b) 状态空间参数按 token 局部独立生成、缺空间邻域上下文；c) 对高频解剖细节不敏感。
- **核心矛盾**：在保持线性复杂度的同时兼顾全局上下文与高频细节。（摘要把局限收敛为“高频不敏感 + 多方向冗余”两条，引言细化为三条。）

## 4. 核心贡献
1.  **HiFi-Mamba 块**：高效双流，单向扫描提效 + 跨流指导，化解 Mamba 的局部性与高频不敏感。
2.  **轻量 w-Laplacian 块**：小波驱动的频谱解耦，分出互补的高/低频流，支撑频率感知双流处理。
3.  **SOTA + 更优权衡**：在公开 MRI 基准上一致超越 CNN/Transformer/Mamba 基线，并在保真度与算力间取得更优平衡。

## 5. 方法详解
**整体框架**：展开优化框架；骨干为 K=8 个级联 HiFi-Mamba 组，每组含 2 个 Mamba 单元 + 1 个 DC 块（训练细节处另述为 6×2 单元配置，组数口径不一，待以代码核实）。输入欠采样图 `I_in∈R^{H×W×2}`（实/虚两通道），先补丁嵌入 `F_in=P(I_in)`，顺序过 K 组，每组末 DC 块强制 k 空间一致；末组后反补丁化回 `R^{H×W×2}`，再过图像域 DC 输出 `I_out`。

**Mamba 单元（非对称双流，式 1–8）**：
- 频率解耦：`F_in` 拆成 `F1,F2`；`F1` 过 WL 得 `F_low, F'_high`（式2）；`F_high=F2+F'_high`（式3）。
- 高频流：`G=CRM(F_high)`（式4，解剖引导先验），`F̃_high=CRM(G)`（式5）。
- 低频流：`F̃_low=H(F_low|G)`（式6），在 `G` 指导下由 HiFi-Mamba 块做长程建模。
- 融合：`F_fused=DSFA(concat[F̃_low,F̃_high])`（式7），残差 `F_out=F_fused+F_in`（式8）。

**w-Laplacian 块（式 9–12）**：用小波替代分辨率导向的拉普拉斯金字塔以获得结构化、可逆的频率分离。`F'1=CRM(F1)`（式9）→ 逐通道 2D DWT 得 `{LL,LH,HL,HH}`（式10）→ `F_low=Upsample(LL)`（式11，先取平滑低频基以避免直接用高频子带的信息损失/基依赖）→ `F_high=F'1−F_low`（式12，高频残差）。

**HiFi-Mamba 块（式 13–19）**：处理 `F_low`、受 `G` 调制。
- 初始参数：`F_c,Z=Split(Linear(Norm(F_low)))`（式13）；`F_conv=SiLU(Conv2D(F_c))`（式14）；重排为序列后 `[Δ,B,C]=Split(Linear(F_s))`（式15）。
- 跨频率指导（式 16–18）：由 `G` 投影出 `B'_h,C'_h`，经门控 `B_h=GELU(B'_{h,1})⊙B'_{h,2}`（`C_h` 同构、独立权重），再相加 `B=B+B_h, C=C+C_h`；`B_h` 调制输入投影 `B`、`C_h` 调制输出投影 `C`（对应 SSM 方程式18），把从 `G` 蒸馏的高频（边缘、混叠伪影）注入 SSM。
- 空间感知精炼：对 `Δ,B,C` 各做 k=7 一维深度卷积，注入邻域上下文、使 `Δ` 的状态转移空间平滑。
- 输出：选择性扫描得 `F_ssm`，`F̃_low=Linear_out(F_ssm⊙SiLU(Z))`（式19）。

**训练**：AdamW，lr=1e-3，余弦退火 +5 epoch 预热，100 epoch，batch=4，ℓ1 损失；2×H100 训练、A100 测 FLOPs、PyTorch 实现。

## 6. 实验与结果
- **数据集**：fastMRI knee（1,172 例单线圈 PD 冠状、约 35 切片/例、320×320、仅 PDFS 子集、官方划分、丢首尾 5 切片）；CC359 brain（GE Discovery MR750、256×256、25 训/10 测、丢首尾 15 切片）。
- **欠采样**：等间距 1D 笛卡尔；AF=4 中心 8% 全采样，AF=8 为 4%。
- **对比**：Zero-Filling；UNet、ISTA-Net；ReconFormer、FPSFormer；LMO。指标 PSNR↑/SSIM↑/NMSE↓。
- **主结果（Table 1）**：P2 在多数场景领先，AF=8 提升明显（fastMRI 31.38 vs LMO 31.10；CC359 28.08 vs 27.99）；P1 更强（CC359 4× 36.93 vs LMO 35.35；fastMRI 4×/8× 34.85/31.81）。唯 fastMRI 4× P2(34.47) 略逊 LMO(34.49)，需 P1 方超越。
- **效率（Table 2，提取被截断）**：ReconFormer 270.60G、FPSFormer 200.45G、LMO 484.98G（4 方向）；**HiFi-Mamba 自身 FLOPs 被截断未给（据原文后续页，提取缓存未覆盖，待核）**；参数量未在提取文本出现。
- **消融**：提取缓存未覆盖消融表/段（待核）。

## 7. 这篇论文真正有价值的地方
1.  **频率解耦 + 双流异步 + 跨流指导**的范式，对 MRI“低频结构/高频细节”谱特性高度对齐，可迁到超分、去噪、去模糊。
2.  **诊断式改造 SSM**：逐条对应 Mamba 三短板给模块化解法（单向扫描 / k=7 空间精炼 / 跨频率门控），方法论值得学习。
3.  **在 SSM 参数层做条件注入**：用 `B_h/C_h` 调制输入/输出投影矩阵而非仅做特征融合，切入点贴近 Mamba 选择性机制。
4.  **统一透明预处理**以保障 MRI 重建的可比性，体现实验严谨。

## 8. 局限与问题
1.  提取缓存未覆盖 HiFi-Mamba 自身 FLOPs 与消融，核心效率/创新点贡献在本笔记证据范围内无法量化核实（数值或在原文后续页，待核）。
2.  仅两个单线圈 MRI 数据集（膝、脑），未验证多线圈/其他模态/复杂解剖的泛化。
3.  仅等间距 1D 笛卡尔欠采样，非笛卡尔/可学习采样下稳健性未知。
4.  K=8 组 与 6×2 单元配置表述不一致，需以代码确认实际深度。
5.  框架叠加多模块（WL/HiFi-Mamba/CRM/DSFA）相对复杂，复现门槛存在。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Introduction（三大局限）+ Table 1 + 结论。
- **复现**：精读 Overall Pipeline 与 Mamba Unit（式 1–8），结合 Figure 2；细读 WL（式 9–12）与 HiFi-Mamba Block（式 13–19，重点跨频率指导与 k=7 精炼）；核对附录预处理/超参；留意 K=8 与 6×2 差异。
- **借鉴创新点**：频率解耦双流可迁去模糊/超分；跨流指导可推广为“一支特征调制另一支（甚至调制 SSM 参数）”；单向扫描思路用于精简视觉 Mamba 扫描。
- **写 Related Work**：1) 深度学习/展开优化 MRI 重建；2) Mamba/SSM 在视觉的应用；3) 频率感知/小波神经网络。

## 10. 和其他论文的关系
- **MRI 重建中的 Mamba 工作**：文中明确对比/引用的 `LMO`（Li et al. 2025，4 方向扫描）与 `MambaMIR`（Huang et al. 2025），本文针对它们的多方向冗余与高频不敏感做改进。
- **视觉 Mamba 基座**：`vMamba`（Liu et al. 2024，四方向扫描）是本文要简化的扫描范式来源。
- **展开优化/数据一致性范式**：`ISTA-Net`、`DeepCascade`、`KIKI-Net`、`DuDoRNet` 等同属展开优化路线，本文把骨干换成 Mamba。
- **Transformer MRI 重建对照**：`ReconFormer`、`FPSFormer`、`SwinMR` 等为本文实验/相关工作中的 Transformer 对照。

（注：以上为文中明确出现的引用对象，本知识库内是否已有对应笔记需另行核对，故未加 `[[]]` 双链。）

## 11. 关键词
MRI 重建, Mamba, 状态空间模型(SSM), 频率解耦, 小波/DWT, w-Laplacian, 跨流指导, 高频敏感性, 单向扫描, 双流架构, 展开优化, 数据一致性, 计算效率

## 12. 可信度说明
本精读**基于提供的 PDF 提取文本**（前 25000 字符 / 原文 40458 字符，标称 9/9 页但实际被字符上限截断）。
- **信息来源**：方法（式 1–19）、数据集设置、Table 1 全部数字、训练/硬件细节均直接来自提取文本，已逐项核对。
- **提取不完整处（据原文后续页推断，提取缓存未覆盖，待核）**：
    1.  Table 2 效率对比仅截到表头与前三行，**HiFi-Mamba 自身 FLOPs 缺失**。
    2.  **消融实验**表格/段落未出现。
    3.  **模型参数量**、**附录预处理细节**未出现。
- 对上述未覆盖内容，笔记已显式标注“待核 / 提取缓存未覆盖”，未编造任何数值。
- 一处需读者留意的原文内部不一致：Overall Pipeline 的 K=8 组 与 训练细节的 6×2 单元配置。

---

> **可信度补充**: PDF 提取质量 = **medium-high** (单页字符密度好，但 25000 字符上限截断了 Table 2 后续行、消融与附录，约占全文 38% 内容未进缓存); 来源缓存: `.paper-cache/extracts/HiFi-Mamba MRI重建 HiFi-Mamba MRI Reconstruction.txt` (标称 9/9 页，实际前 25000/40458 字符); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
