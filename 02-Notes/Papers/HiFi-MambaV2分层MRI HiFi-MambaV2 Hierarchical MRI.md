---
title: "HiFi-MambaV2: Hierarchical Shared-Routed MoE for High-Fidelity MRI Reconstruction"
authors:
  - "Pengcheng Fang"
  - "Hongli Chen"
  - "Guangzhen Yao"
  - "Jian Shi"
  - "Fangfang Tang"
  - "Xiaohao Cai"
  - "Shanshan Shan"
  - "Feng Liu"
year: 2025
venue: "arXiv preprint (arXiv:2511.18534v1 [cs.CV], 23 Nov 2025)"
doi: 
pdf: [[HiFi-MambaV2分层MRI HiFi-MambaV2 Hierarchical MRI.pdf]]
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
extract_cache: .paper-cache/extracts/HiFi-MambaV2分层MRI HiFi-MambaV2 Hierarchical MRI.txt
---

# HiFi-MambaV2: Hierarchical Shared-Routed MoE for High-Fidelity MRI Reconstruction

## 基本信息
- **PDF**: [[HiFi-MambaV2分层MRI HiFi-MambaV2 Hierarchical MRI.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

> 分类说明: 本文是**MRI 加速重建**（从欠采样 k 空间恢复全采样图像）论文, 属于医学图像的逆问题求解/图像生成范畴, 不是分割任务。原 `A1_医学图像_分割` 与正文不符, 已改为 `A2_医学图像_分类_配准_生成`（taxonomy 中最贴近"医学图像生成/重建"的一项）。

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | HiFi-MambaV2: Hierarchical Shared-Routed MoE for High-Fidelity MRI Reconstruction |
| **作者** | Pengcheng Fang*; Hongli Chen*; Guangzhen Yao; Jian Shi; Fangfang Tang; Xiaohao Cai; Shanshan Shan†; Feng Liu (*共同一作, †通讯) |
| **发表时间** | 2025 (arXiv 提交日 2025-11-23) |
| **刊物/会议** | arXiv preprint (arXiv:2511.18534v1 [cs.CV]); 排版用 IEEE 期刊模板, 推测投稿 IEEE 期刊 |
| **DOI** | 未明确 |

> 注: frontmatter 原 `year: 2021` 来自 LaTeX 模板页眉 "JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021"（模板年份, 非论文年份）。论文 arXiv 提交日为 2025-11-23, 故实际年份为 2025。

## 摘要

**英文原文（据提取文本整理, 已修复空格/连字符断裂、剔除杂入图表标签）**:

> Reconstructing high-fidelity MR images from undersampled k-space data requires recovering high-frequency details while maintaining anatomical coherence. We present HiFi-MambaV2, a hierarchical shared-routed Mixture-of-Experts (MoE) Mamba architecture that couples frequency decomposition with content-adaptive computation. The model comprises two core components: (i) a separable frequency-consistent Laplacian pyramid (SF-Lap) that delivers alias-resistant, stable low- and high-frequency streams; and (ii) a hierarchical shared-routed MoE that performs per-pixel top-1 sparse dispatch to shared experts and local routers, enabling effective specialization with stable cross-depth behavior. A lightweight global context path is fused into an unrolled, data-consistency-regularized backbone to reinforce long-range reasoning and preserve anatomical coherence. Evaluated on fastMRI, CC359, ACDC, M4Raw, and Prostate158, HiFi-MambaV2 consistently outperforms CNN-, Transformer-, and prior Mamba-based baselines in PSNR, SSIM, and NMSE across single- and multi-coil settings and multiple acceleration factors, with consistent improvements in high-frequency detail and overall structural fidelity. These results demonstrate that HiFi-MambaV2 enables reliable and robust MRI reconstruction.

**中文翻译**:

> 从欠采样 k 空间数据重建高保真 MR 图像, 需要在保持解剖结构一致性的同时恢复高频细节。我们提出 HiFi-MambaV2, 一种层次化共享-路由混合专家（MoE）Mamba 架构, 它将频率分解与内容自适应计算相耦合。模型包含两个核心组件:（i）可分离频率一致拉普拉斯金字塔（SF-Lap）, 提供抗混叠、稳定的低频与高频特征流;（ii）层次化共享-路由 MoE, 对每个像素执行 top-1 稀疏分派, 将其分发给共享专家与局部路由器, 在保持跨深度稳定行为的同时实现有效的专业化分工。此外, 一条轻量级全局上下文路径被融合进一个展开式、数据一致性正则化的骨干网络, 以强化长程推理并保持解剖结构一致性。在 fastMRI、CC359、ACDC、M4Raw 与 Prostate158 五个数据集上, HiFi-MambaV2 在单/多线圈设置和多种加速因子下的 PSNR、SSIM、NMSE 指标上持续超越 CNN、Transformer 与此前的 Mamba 基线方法, 在高频细节和整体结构保真度上均有稳定提升。结果表明 HiFi-MambaV2 能够实现可靠且鲁棒的 MRI 重建。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: MRI 因非侵入性和优异的软组织对比度在临床上不可或缺, 但采集时间长, 增加患者不适并限制临床吞吐量。从欠采样 k 空间重建是一种加速策略, 但欠采样会引入混叠伪影, 因此需要既能恢复精细高频解剖细节、又能保持全局解剖结构一致性的重建方法。
- **之前方法的问题**:
    1.  **CNNs**: 感受野有限, 难以建模对保持全局解剖一致性至关重要的长程依赖。
    2.  **Vision Transformers**（如 SwinMR、ReconFormer、FpsFormer）: 能建模长程依赖, 但自注意力的二次方计算/内存复杂度阻碍了其向高分辨率临床输入和大视野（FOV）的扩展; 高分辨率下的 patch 级注意力还可能破坏多尺度上下文一致性。
    3.  **先前的 Mamba 方法**（如 MambaMIR、LMO, 基于 VMamba 等视觉骨干）: 直接应用于 MRI 时存在三类问题——（i）冗余的多方向扫描;（ii）局部状态参数化削弱解剖结构一致性;（iii）缺乏显式的频率控制。
    4.  作者之前的 **HiFi-Mamba（V1）**: 采用单向扫描的双流频率解耦设计, 虽有效, 但严格解耦减少了跨频率交互和全局聚合; 且采用静态路由 + 固定的 w-Laplacian 变换, 频率自适应性有限。
- **频域分析动机（图 1）**: 作者可视化了 Conv / Pure Mamba / HiFi-Mamba 三类块前后中间特征的逐通道 2D 对数频谱（14×14 缩略图）。观察到: **Conv 块**保留显著的十字形高频响应（对局部边缘/纹理敏感）; **Pure Mamba**抑制中高频、能量集中在 DC 附近（低通、偏全局上下文行为）; **HiFi-Mamba 块**产生平衡频谱——低频主导（全局一致性）同时保留适度高频能量（局部细节）。这一频域互补性正是后续设计的动机。
- **核心矛盾**: 如何在重建过程中统一并平衡**全局解剖一致性（低频）** 与**局部精细纹理恢复（高频）**, 尤其针对空间上变化的组织复杂度和混叠模式, 实现自适应的计算分配。

## 关键贡献

论文引言（第 2 页）明确列出**三个核心组件**, 笔记按此整理:

1.  **层次化共享-路由 MoE（SR-MoE）**: 对每个像素执行 top-1 稀疏路由, 分发给共享专家与局部专家, 在保持跨深度稳定的同时实现自适应专业化。来自不同分辨率/频率流的多级特征先拼接再送入该模块, 以同时捕获全局与局部频率模式。
2.  **可分离频率一致拉普拉斯金字塔（SF-Lap）**: 采用深度可分离二项式滤波 + 对称扩展, 实现能量保持、抗混叠的多尺度分解, 产生稳定的低频与高频特征流, 替代 V1 中固定的 w-Laplacian 变换。
3.  **轻量级 SE 引导残差路径（LSGP）**: 在频率分解之前注入整体全局上下文, 作为展开式、数据一致性正则化重建骨干中的辅助增强分支。

此外（贡献的工程/实验维度）:
4.  **完整的展开式重建框架**: 将上述模块集成进数据一致性正则化的展开优化框架（**8 个 HiFi-Mamba 组级联**）。
5.  **五数据集全面评估 + 消融**: 在 fastMRI、CC359、ACDC、M4Raw、Prostate158 上, 多加速因子、多采样模式、单/多线圈设置下, 在 PSNR/SSIM/NMSE 上持续达到最优或次优, 并通过消融验证各组件（"validates each component through ablations"）。

## 方法

- **整体框架**: HiFi-MambaV2 是展开式、数据一致性正则化的迭代重建框架, 求解多线圈逆问题。整体由**8 个 HiFi-Mamba 组**级联构成, 每组对应一次展开迭代, 含**2 个 HiFi-Mamba 单元（Mamba Unit ×2）+ 1 个数据一致性（DC）块**（图 2c）。每个组在图像域特征精炼与 k 空间物理一致性之间交替。
- **前向模型与重建更新**:
    - 多线圈前向模型: `y_c = F_u(S_c x) + n_c`（公式 1）, 其中 `x∈C^{H×W}` 为全采样图像, `y_c∈C^M` 为第 c 个线圈的欠采样 k 空间测量, `S_c` 为线圈灵敏度图, `F_u` 为欠采样算子, `n_c` 为噪声。
    - 迭代更新: `x^(t+1) = D_θ( x^(t) − λ Σ_c S_c^H F_u^H (F_u(S_c x^(t)) − y_c) )`（公式 2）, `D_θ` 为可学习特征精炼模块（即 HiFi-Mamba 单元）。
- **关键模块与连接**（图 2）:
    1.  **轻量级 SE 引导全局上下文路径 LSGP**（图 2e, 公式 5-7）: 对输入 `x∈R^{B×H×W×C}` 做全局平均池化 `z=GAP(x)`（公式 5）; 经两层门控网络 `s=Sigmoid(W_2 ReLU(W_1 z))` 生成逐通道调制权重（公式 6, `W_1∈R^{C×(C/r)}`, `W_2∈R^{(C/r)×C}`, r 为缩减比）; 残差式调制 `x' = x⊙s + x`（公式 7）。与主骨干并行运行, **在 SF-Lap 之前**注入全局解剖上下文, 开销可忽略。
    2.  **可分离频率拉普拉斯分解 SF-Lap**（图 2g, 公式 3-4）: 把经典 Gauss-Laplacian 操作重写成单级、深度可分离分解。使用归一化 **5-tap 二项式核 k=[1,4,6,4,1]/16**（近似 σ≈1 的高斯, 各向同性平滑）, 以深度可分离方式水平/垂直应用、采用反射 padding, 把 2D 卷积代价从 O(k²) 降到 O(2k)。低通约简（公式 3）: 先水平 stride=1 平滑, 再垂直 stride=2 联合低通 + 2× 下采样得到低频 `L`。高频提取（公式 4）: `L̃ = U_×2(L)`（2× 双线性上采样）, `H = x − L̃`; 双线性插值相比零插值扩展能避免棋盘伪影。
    3.  **层次化共享-路由 MoE（SR-MoE）**（图 2 路由 K=4 路, 公式 8-12）: 将**全局上下文流 + 高频流 H + 低频流 L 拼接**成融合特征 `x∈R^{B×H×W×C}`。含两组专家——**共享专家**（对所有 token 始终激活）和**路由专家**（由轻量逐像素路由器自适应选择）; 每个专家实现为在空间位置上独立操作的轻量**逐通道 MLP**。共享输出 `y_shared = Σ_{i=1..N_s} E_i^{(sh)}(x)`（公式 8）。路由器经 1×1 线性投影 `W_r` 生成 logits, `G=Softmax(W_r x)∈R^{B×H×W×N_r}`（公式 9）; 逐像素 **top-1** 选择得路由掩码 `M`（公式 10）; 路由输出 `y_routed = Σ_{e=1..N_r} M_{:,:,:,e}⊙E_e^{(rt)}(x)`（公式 11）; 最终 `y = y_shared + y_routed`（公式 12）。该模块置于 SF-Lap 与 LSGP 之后。
    4.  **频率感知 HiFi-Mamba 块**（图 2f）: 在 MoE 之前, 高/低频流分别经基于 Mamba 的 token 混合块（含 Patchify / Linear / DConv1D / S6 等, 见图 2f）做序列建模, 提供线性时间复杂度的长程依赖建模。
    5.  **双频空间注意力 DFSA**（图 2h, 文中称 Dual-Frequency Spatial Attention）: 通过自适应加权融合路由专家的输出, 形成最终特征表示。
    6.  **CRM（Condition Refinement Module, 图 2d）**: 执行跨分辨率特征变换。
    7.  **数据一致性 DC 块**（图 2b）: 每个组之后施加, 用采集到的 k 空间数据约束重建结果的物理保真。
- **训练方式**: AdamW 优化器, 初始学习率 **8×10⁻⁴**, 余弦退火 + **5 epoch 预热**, 共训练 **100 epoch**。损失为 **重建 L1 损失 + 负载均衡正则项**: `L = (1/B)Σ_b ‖x̂_b − x_b^{gt}‖_1 + λ_bal · L_bal`（公式 15）, 其中 `L_bal = N_r Σ_{e=1..N_r} p_e²`（公式 14, `p_e` 为专家 e 的平均路由概率, 公式 13）, 当各专家均匀利用 `p_e=1/N_r` 时取最小, 用于避免专家坍塌。
- **硬件**: 训练在 2× NVIDIA H100 GPU 上进行; FLOPs 在 NVIDIA A100 上测量。
- **与已有方法的差异**: 区别于纯 CNN（局部性）、Transformer（高计算成本）、基础 Mamba（缺乏频率控制和自适应性）。HiFi-MambaV2 的独特之处: **1) 在 Mamba 骨干中引入内容自适应 MoE 路由**（动态分配计算）; **2) 显式、抗混叠的频率分解 SF-Lap**; **3) 全局上下文路径 LSGP**。即"频率感知"与"自适应计算"相结合。
- **论文类型特化（医学类）**:
    - **任务**: MRI 图像重建（欠采样 k 空间 → 全采样图像域）, 属逆问题求解。
    - **模态/部位**: MRI, 涵盖膝盖（fastMRI）、大脑（CC359、M4Raw）、心脏（ACDC）、前列腺（Prostate158）。
    - **流程**: 基于深度学习的展开优化, 集成数据一致性与学习先验（Mamba+MoE）。
    - **临床意义**: 缩短扫描时间、提高患者舒适度与临床吞吐量, 同时保留诊断细节。

## 实验

- **使用的数据集**（共 5 个, 第 4 页 V.A 给出规模）:
    - **fastMRI（膝盖）**: 1,172 例单线圈冠状膝关节扫描, PDFS 加权, 遵循官方划分; 丢弃每个体积首尾各 5 个切片。
    - **CC359（大脑）**: 原始脑 MR 体积, 25 例训练 / 10 例测试; 丢弃每个体积首尾各 15 个切片。
    - **ACDC（心脏）**: 150 例 Cine 心脏 MR, 官方划分 100 训练 / 50 测试。
    - **M4Raw（多线圈大脑）**: 183 名志愿者在 0.3T 四通道线圈下采集, 多对比/多重复/多通道 k 空间; 1,024 / 240 体积分别用于训练/验证。
    - **Prostate158（前列腺）**: 158 名志愿者, 139 训练 / 19 测试。
- **对比方法**: Zero-Filling、UNet（MICCAI 2015）、ISTA-Net（CVPR 2018）、ReconFormer（TMI 2023）、FpsFormer（AAAI 2025）、LMO（CVPR 2025）、HiFi-MambaV1（P1/P2, AAAI 2026）。
- **评价指标**: PSNR↑、SSIM↑、NMSE↓。
- **主实验结果**:
    - **表 I（fastMRI / CC359, 等间距采样, 4×/8×)**: HiFi-MambaV2(P1) 在两数据集多数指标上达最优。
        - fastMRI 4×: PSNR 34.86 / SSIM 0.855 / NMSE 0.010; 8×: PSNR 31.89 / SSIM 0.764 / NMSE 0.019。
        - CC359 4×: PSNR 37.21 / SSIM 0.957 / NMSE 0.003; 8×: PSNR 29.05 / SSIM 0.849 / NMSE 0.020。
        - 相较 V1(P1)（fastMRI 8× 为 31.81 / 0.762 / 0.020; CC359 4× 为 36.93 / 0.942 / 0.004）和 LMO（CVPR 2025）等基线均有提升, 在 SSIM 与高频结构保真上提升尤为明显。
    - **表 II（Prostate158, 单线圈, 随机掩码, 4×/8×)**: HiFi-MambaV2(P1) 最佳。
        - 4×: PSNR 29.04 / SSIM 0.837 / NMSE 0.012（V1(P1) 为 28.85 / 0.833 / 0.013）。
        - 8×: PSNR 23.91 / SSIM 0.662 / NMSE 0.039（V1(P1) 为 23.22 / 0.654 / 0.046）。
    - 论文称 Tables I–IV 给出跨多数据集/采样/加速因子的全面对比, HiFi-MambaV2 在所有设置下达最优或次优; 但**表 III、IV（含 ACDC、M4Raw 等及多线圈结果）落在提取缓存截断之后**（提取仅到 V.B 开头、Table I/II), 具体数字提取文本未覆盖。
- **消融实验**: 引言与 V.B 提及"validates each component through ablations", 但**消融的具体表格与数字落在提取截断之后, 提取文本未覆盖**。
- **泛化实验**: 通过 5 个部位、单/多线圈、等间距/随机两类采样模式、多加速因子的测试展示泛化能力。
- **速度/参数量/FLOPs**: 文中说明 FLOPs 在 A100 上测量, 但**具体 FLOPs/参数量数值落在提取截断之后, 提取文本未给出**。

## 局限

1.  **多线圈/ACDC/M4Raw 与消融数字缺位（就本提取而言）**: 提取缓存只覆盖前 9 页至 Table I/II, 表 III/IV、消融表、FLOPs/参数量等关键定量结论未包含, 无法在本笔记中核对其强度。
2.  **依赖多方向扫描的开放问题**: 背景指出 Mamba 视觉模型常用多方向扫描建模 2D 空间关系, 引入冗余计算且扫描顺序最优性是开放问题; 本文以频率分解 + MoE 路由缓解, 但未在方法部分详述自身的扫描方向设计。
3.  **模态单一**: 实验局限于 MRI 单模态, 在 CT、超声等其他成像模态或更广视觉任务上的有效性未验证。
4.  **假设依赖**: 方法假设低/高频可由 SF-Lap（二项式拉普拉斯）有效分离, 且共享专家能提供有效"通用"先验; 在极端欠采样或复杂病变区域, 这种分离与先验的有效性有待进一步检验。
5.  **复现细节**: 提取文本未给出专家数量 N_s/N_r 的具体取值、缩减比 r、负载均衡系数 λ_bal 的数值, 以及 SF-Lap padding 的全部细节; 论文将数据预处理/介绍放在附录 A.1/A.2（提取未覆盖附录）, 精确复现需查原文与附录。

## 个人评论

1.  **MoE 思想成功引入医学图像重建的 Mamba 骨干**: "共享-路由"双轨设计兼顾稳定通用先验（共享专家）与内容自适应专精（路由专家 top-1）, 对处理 MRI 中空间变化的纹理/混叠复杂度很对症; 逐像素路由比固定双流路由更细粒度。
2.  **"频域分析→架构设计"的闭环很扎实**: 图 1 用逐通道 2D 频谱量化了 Conv（偏高频）与 Pure Mamba（偏低频）的频率偏好, 据此设计 SF-Lap 显式平衡频率。这种"先观测频率行为、再针对性补偿"的思路, 比单纯堆模块更有说服力, 也方便迁移到其他频率敏感的复原任务。
3.  **稳定性是这版的隐性卖点**: 8 组展开 × 每组 2 单元意味着路由要在很深的展开链上保持一致; 文中用负载均衡正则 `L_bal=N_r Σ p_e²` 和"跨深度稳定路由"来防专家坍塌, 这是把 MoE 用进展开重建的关键工程点, 不容易但做对了价值很大。
4.  **模块化、可迁移**: LSGP（全局上下文）、SF-Lap（频率分解）、SR-MoE（自适应计算）三者相对解耦, 有即插即用潜力, 可借鉴到其他基于 Mamba 或需频率/自适应计算控制的视觉复原任务。
5.  **审慎处**: 增益主要来自 SSIM 与高频细节, PSNR 在 fastMRI 上相对 V1 提升较小（4× 34.85→34.86）; 真正的提升幅度（CC359、Prostate158 上更明显）以及参数/FLOPs 代价需结合截断后的表 III/IV 与消融才能完整评估。

### 使用建议

- **如果快速了解**: 读**摘要**与**引言最后几段**（含三组件列表）+ **图 1** 频域可视化, 即可掌握问题、核心思想（层次化共享-路由 MoE-Mamba 做频率自适应重建）与主要结论。
- **如果复现**: 精读**第 IV 节 Method**（SF-Lap 公式 3-4、LSGP 公式 5-7、SR-MoE 公式 8-12、损失公式 13-15）, 结合**图 2** 理解模块连接; 数据集预处理/介绍见**附录 A.1/A.2**, 超参见 V.A（lr 8e-4, 100 epoch, 5 epoch warmup, 2×H100）。专家数量、r、λ_bal 等需查原文。
- **如果借鉴创新点**:
    1.  **SR-MoE**: 共享 + 路由专家的逐像素 top-1 路由 + 负载均衡, 用于自适应计算。
    2.  **SF-Lap**: 深度可分离 5-tap 二项式滤波 + 双线性上采样实现抗混叠频率分解。
    3.  **频域可视化分析法**: 通过逐通道 2D 对数频谱论证模块的频率行为。
- **如果写 related work**, 可归入: ①基于深度学习/展开优化的 MRI 重建; ②Mamba 在视觉/医学影像中的应用; ③MoE 在视觉任务中的应用; ④频率感知的图像复原/重建模型。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页:
> - [[A2_医学图像_分类_配准_生成]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**医学图像重建**方向, 具体是**基于深度学习的高保真 MRI 加速重建**（从欠采样 k 空间数据恢复全采样图像）。核心创新是把**状态空间模型（Mamba）**与**混合专家（MoE）**结合, 在频率域显式分解的基础上做内容自适应计算。任务本质是医学图像的逆问题求解/图像生成, **不是分割**; 因此 taxonomy 中归入 `A2_医学图像_分类_配准_生成`（"生成/重建"维度）比原 `A1_医学图像_分割` 更准确。文件名"分层MRI HiFi-MambaV2 Hierarchical MRI"与正文一致, 无串台。

## 2. 一句话总结
HiFi-MambaV2 是一种层次化共享-路由 MoE-Mamba 架构, 通过耦合频率一致的拉普拉斯金字塔分解（SF-Lap）与逐像素 top-1 的内容自适应专家计算（SR-MoE）, 并辅以 SE 引导的全局上下文路径, 在数据一致性正则化的展开框架内实现高保真、解剖一致的 MRI 重建。

## 3. 背景与问题
- **为什么要做**: MRI 非侵入、软组织对比好但采集慢; 从欠采样 k 空间重建可加速, 但会引入混叠伪影, 需要既恢复高频细节又保持全局解剖一致性的重建方法。
- **之前方法的问题**:
    1.  **CNN**: 感受野有限, 难建长程依赖。
    2.  **ViT**（SwinMR/ReconFormer/FpsFormer）: 自注意力二次复杂度难扩展到高分辨率/大 FOV; 高分辨率 patch 注意力还会侵蚀多尺度上下文。
    3.  **基础 Mamba**（MambaMIR/LMO, 基于 VMamba）: 冗余多方向扫描、局部状态参数化削弱解剖一致性、缺乏频率控制。
    4.  **HiFi-Mamba V1**: 单向扫描双流频率解耦, 但严格解耦减少跨频交互与全局聚合; 静态路由 + 固定 w-Laplacian 频率自适应性有限。
- **频域观测（图 1）**: Conv 偏高频、Pure Mamba 偏低频（能量集中 DC）、HiFi-Mamba 块平衡两者——这是设计动机。
- **核心矛盾**: 在空间变化的组织复杂度/混叠模式下, 自适应平衡全局一致性（低频）与局部细节（高频）。

## 4. 核心贡献
论文明确列出**三个核心组件**:
1.  **SR-MoE（层次化共享-路由 MoE）**: 逐像素 top-1 稀疏路由到共享专家 + 局部专家, 多分辨率特征拼接后输入, 跨深度稳定。
2.  **SF-Lap（可分离频率一致拉普拉斯金字塔）**: 深度可分离二项式滤波 + 对称扩展, 能量保持、抗混叠的多尺度分解。
3.  **LSGP（轻量级 SE 引导残差路径）**: 频率分解前注入全局上下文, 作为展开骨干内的辅助增强分支。
工程/实验维度: 8 组展开式数据一致性重建框架; 5 数据集 + 消融的全面评估。

## 5. 方法详解
- **整体框架**: 展开式、数据一致性正则化迭代重建; **8 个 HiFi-Mamba 组**级联, 每组 = 2 个 Mamba 单元 + 1 个 DC 块（图 2c）, 图像域精炼与 k 空间一致性交替。
- **前向模型与更新**: `y_c=F_u(S_c x)+n_c`（公式 1）; `x^(t+1)=D_θ( x^(t) − λ Σ_c S_c^H F_u^H (F_u(S_c x^(t)) − y_c) )`（公式 2）, `D_θ` 为可学习 HiFi-Mamba 单元。
- **LSGP（公式 5-7）**: GAP→两层门控 Sigmoid(W_2 ReLU(W_1 z))→残差通道调制 `x'=x⊙s+x`; 与主干并行, SF-Lap 之前注入全局上下文, 开销可忽略。
- **SF-Lap（公式 3-4）**: 5-tap 二项式核 [1,4,6,4,1]/16（近似 σ≈1 高斯）, 深度可分离水平/垂直滤波 + 反射 padding, O(k²)→O(2k); 低通约简先水平 s=1 再垂直 s=2（含 2× 下采样）得 L; 高频 `H=x−U_×2(L)`, 双线性上采样避免棋盘伪影。
- **SR-MoE（公式 8-12）**: 拼接全局/高频 H/低频 L 成融合特征; 共享专家始终激活 `y_shared=Σ E_i^{(sh)}(x)`（公式 8）; 路由器 `G=Softmax(W_r x)`（1×1 投影, 公式 9）逐像素 top-1 得掩码 M（公式 10）, `y_routed=Σ_e M⊙E_e^{(rt)}(x)`（公式 11）; `y=y_shared+y_routed`（公式 12）; 每个专家是轻量逐通道 MLP, top-1 故开销可忽略。
- **其他模块**: 频率感知 HiFi-Mamba 块（图 2f, Mamba token 混合, 线性复杂度）; DFSA 双频空间注意力（图 2h, 自适应加权融合路由输出）; CRM 跨分辨率变换（图 2d）; DC 块（图 2b）。
- **训练**: AdamW, lr 8×10⁻⁴, 余弦退火 + 5 epoch warmup, 100 epoch; 损失 = L1 重建 + λ_bal·L_bal, `L_bal=N_r Σ p_e²`（公式 13-15, 防专家坍塌）; 2×H100 训练, FLOPs 在 A100 测。

## 6. 实验与结果
- **数据集**: fastMRI 膝（1,172 单线圈, 弃首尾 5 切片）、CC359 脑（25/10, 弃首尾 15 切片）、ACDC 心（100/50）、M4Raw 多线圈脑（0.3T 四通道, 1,024/240）、Prostate158 前列腺（139/19）。
- **对比方法**: Zero-Filling、UNet、ISTA-Net、ReconFormer、FpsFormer、LMO、HiFi-MambaV1(P1/P2)。
- **指标**: PSNR↑/SSIM↑/NMSE↓。
- **主结果（提取覆盖到表 I/II）**:
    - 表 I fastMRI: V2(P1) 4×=34.86/0.855/0.010, 8×=31.89/0.764/0.019; CC359: 4×=37.21/0.957/0.003, 8×=29.05/0.849/0.020 — 多数指标超 V1(P1) 与 LMO。
    - 表 II Prostate158（随机掩码）: V2(P1) 4×=29.04/0.837/0.012, 8×=23.91/0.662/0.039 — 均优于 V1(P1)。
    - 论文称 Tables I–IV 全面对比, V2 全设置最优/次优; **表 III/IV（含 ACDC、M4Raw、多线圈）与消融、FLOPs 落在提取截断之后, 提取文本未覆盖**。
- **泛化**: 5 部位 + 单/多线圈 + 等间距/随机采样 + 多加速因子。

## 7. 这篇论文真正有价值的地方
1.  **MoE 进入 MRI 重建的 Mamba 骨干**: 共享 + 路由专家的逐像素 top-1 自适应计算, 契合 MRI 空间变化的复杂度。
2.  **频域分析与设计动机紧密结合**: 图 1 频谱量化 Conv/Mamba 频率偏好, 据此设计 SF-Lap 显式平衡频率, "分析→设计"闭环可借鉴。
3.  **层次化 + 稳定性**: 多级特征拼接送共享 MoE + 负载均衡正则, 在 8×2 的深展开链上保持路由稳定、防专家坍塌。
4.  **模块化即插即用**: LSGP / SF-Lap / SR-MoE 相对独立, 可迁移到其他 Mamba/频率敏感复原任务。

## 8. 局限与问题
1.  **关键定量结论缺位（就本提取）**: 表 III/IV、消融、FLOPs/参数量落在提取截断后, 无法核对其强度。
2.  **多方向扫描的开放问题**: Mamba 视觉模型常用多方向扫描, 冗余计算且顺序最优性未解; 本文未在方法部分详述自身扫描设计。
3.  **模态单一**: 仅 MRI, 未验证 CT/超声等模态或更广视觉任务。
4.  **假设依赖**: 假设二项式拉普拉斯能有效分离高/低频、共享专家提供有效通用先验; 极端欠采样/复杂病变下有待检验。
5.  **复现细节**: N_s/N_r、缩减比 r、λ_bal 等数值与附录预处理细节提取未覆盖, 精确复现需查原文 + 附录。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言末尾三组件列表 + 图 1 频域图。
- **复现**: 精读第 IV 节公式（3-4 SF-Lap、5-7 LSGP、8-12 SR-MoE、13-15 损失）+ 图 2; 超参见 V.A; 数据集细节见附录 A.1/A.2。
- **借鉴创新点**: SR-MoE 路由设计、SF-Lap 抗混叠分解、频域可视化分析法。
- **写 related work**: ①展开式 MRI 重建; ②Mamba 在视觉/医学影像; ③MoE 在视觉; ④频率感知图像复原。

## 10. 和其他论文的关系
- **[[HiFi-Mamba]]**: 本文直接前身（V1）。V2 针对 V1 的静态路由 + 固定 w-Laplacian + 双流严格解耦做改进（引入自适应 MoE 路由、可学习抗混叠 SF-Lap、全局上下文路径）。
- **[[MambaMIR]]**、**[[LMO]]**: 近期将 Mamba 用于 MRI 重建的代表工作, 是本文主要对比基线（LMO 为 CVPR 2025）。
- **[[VMamba]]**: 将 Mamba 引入视觉骨干的代表工作, 提供基础架构参考。
- **[[SwinMR]]**、**[[ReconFormer]]**、**[[FpsFormer]]**: 基于 Transformer 的 MRI 重建方法, 本文对比基线（ReconFormer TMI 2023, FpsFormer AAAI 2025）。
- **[[ADMM-Net]]**、**[[DuDoRNet]]**、**[[ISTA-Net]]**: 经典模型展开式 MRI 重建, 体现数据一致性集成思想。

## 11. 关键词
MRI 重建, 加速 MRI, 欠采样 k 空间, Mamba, 状态空间模型, 混合专家 MoE, 共享-路由专家, 逐像素 top-1 路由, 频率分解, 拉普拉斯金字塔, SF-Lap, 自适应计算, SE 全局上下文, 展开优化, 数据一致性, 高频细节恢复, 负载均衡

## 12. 可信度说明
本精读基于提取缓存的**前 9 页文本**（提取在 25,000 字符处截断, 原文约 45,281 字符, 覆盖到第 5 页 Section V.B 开头 / Table I、II）。标题、作者、摘要、引言、相关工作、动机、Method（公式 1-15）、实验设置（数据集/指标/训练）、Table I（fastMRI/CC359）与 Table II（Prostate158）的数字均直接来自提取文本, 可核对。**Table III、IV、消融实验、FLOPs/参数量、附录 A.1/A.2 落在截断之后, 未包含**, 相关处已逐条标注"提取文本未覆盖"。年份据 arXiv 提交日 2025-11-23 校正（frontmatter 原 2021 系 LaTeX 模板页眉年份）; primary_topic 由 A1_分割 改为 A2_分类_配准_生成（本文为重建/生成任务）。

---

> **可信度补充**: PDF 提取质量 = **high** (前 9 页提取清晰, 约 2782 字符/页); 但**提取在 25,000 字符处截断**(原文约 45,281 字符), 表 III/IV、消融、FLOPs 与附录未覆盖, 相关结论待核原文。来源缓存: `.paper-cache/extracts/HiFi-MambaV2分层MRI HiFi-MambaV2 Hierarchical MRI.txt` (标注 9/9 页, 但字符截断); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
