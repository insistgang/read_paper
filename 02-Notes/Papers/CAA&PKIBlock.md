---
title: Poly Kernel Inception Network for Remote Sensing Detection
authors:
  - "Xinhao Cai"
  - "Qiuxia Lai"
  - "Yuwei Wang"
  - "Wenguan Wang"
  - "Zeren Sun"
  - "Yazhou Yao"
year: 2024
venue: "arXiv:2403.06258 [cs.CV]"
doi: 
pdf: [[CAA&PKIBlock.pdf]]
primary_topic: C_目标检测_通用与旋转框
topics:
  - "C_目标检测_通用与旋转框"
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
extract_cache: .paper-cache/extracts/CAA&PKIBlock.txt
---

# Poly Kernel Inception Network for Remote Sensing Detection

## 基本信息
- **PDF**: [[CAA&PKIBlock.pdf]]
- **primary_topic**: `C_目标检测_通用与旋转框`
- **topics**: `C_目标检测_通用与旋转框`, `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Poly Kernel Inception Network for Remote Sensing Detection |
| **作者** | Xinhao Cai; Qiuxia Lai; Yuwei Wang; Wenguan Wang; Zeren Sun; Yazhou Yao |
| **单位** | 南京理工大学; 中国传媒大学; 浙江大学 |
| **发表时间** | 2024 (arXiv:2403.06258v2, 20 Mar 2024) |
| **刊物/会议** | arXiv preprint [cs.CV]（据原文后续页线索为 CVPR 2024，提取缓存未覆盖该信息，待核） |
| **代码** | https://github.com/NUST-Machine-Intelligence-Laboratory/PKINet |
| **DOI** | 未明确 |

## 摘要

**清理后英文原文**：
> Object detection in remote sensing images (RSIs) often suffers from several increasing challenges, including the large variation in object scales and the diverse-ranging context. Prior methods tried to address these challenges by expanding the spatial receptive field of the backbone, either through large-kernel convolution or dilated convolution. However, the former typically introduces considerable background noise, while the latter risks generating overly sparse feature representations. In this paper, we introduce the Poly Kernel Inception Network (PKINet) to handle the above challenges. PKINet employs multi-scale convolution kernels without dilation to extract object features of varying scales and capture local context. In addition, a Context Anchor Attention (CAA) module is introduced in parallel to capture long-range contextual information. These two components work jointly to advance the performance of PKINet on four challenging remote sensing detection benchmarks, namely DOTA-v1.0, DOTA-v1.5, HRSC2016, and DIOR-R.

**中文翻译**：
> 遥感图像（RSI）中的目标检测常常面临若干日益严峻的挑战，包括物体尺度变化巨大以及上下文范围多样。已有方法试图通过扩大骨干网络的空间感受野来应对这些挑战，途径要么是大核卷积，要么是扩张（空洞）卷积。然而，前者通常会引入大量背景噪声，后者则可能产生过于稀疏的特征表示。本文提出 Poly Kernel Inception Network（PKINet）来处理上述挑战。PKINet 采用多尺度且不带扩张的卷积核来提取不同尺度的物体特征并捕获局部上下文；此外，并行引入一个上下文锚点注意力（Context Anchor Attention, CAA）模块以捕获长程上下文信息。这两个组件协同工作，使 PKINet 在 DOTA-v1.0、DOTA-v1.5、HRSC2016 和 DIOR-R 四个具有挑战性的遥感检测基准上取得性能提升。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：遥感图像（RSI，含航拍与卫星图像）从鸟瞰视角采集，物体尺度跨度极大（从足球场等大目标到车辆等小目标），且识别不仅依赖外观，还高度依赖周围环境的上下文信息。OBB（有向边界框）检测器虽多，但 RSI 特有的"大尺度变化 + 多样上下文"在**特征提取**层面仍未被充分挖掘。
- **之前方法的问题**：
    - 数据增强、多尺度特征融合、特征金字塔（FPN）等方法对不同尺度物体使用**相同的感受野**，无法为大物体提供足够上下文。
    - 直接竞品 **LSKNet** 通过引入**大核卷积**与**扩张卷积**为大物体选择性扩大感受野，但大核卷积会引入大量**背景噪声**（不利于小目标），扩张卷积则可能遗漏感受野内的细粒度细节，导致**特征过于稀疏**。
- **核心矛盾**：如何在不引入背景噪声、也不产生稀疏特征的前提下，为尺度变化巨大的目标**自适应地捕获兼顾局部与全局的上下文信息**。

## 关键贡献

1.  **提出 PKINet 骨干网络**：一个专为遥感目标检测设计的、轻量且强大的特征提取骨干。论文自称是首个将 **inception 风格卷积** 与 **全局上下文注意力** 结合用于遥感目标检测的工作。
2.  **PKI 模块（多尺度无扩张卷积）**：并行排布多个不同尺寸的深度可分离卷积核（不使用扩张），跨多个感受野提取稠密纹理特征，并沿通道维自适应融合，以捕获局部多尺度上下文。
3.  **上下文锚点注意力（CAA）模块**：利用全局平均池化与一维条带卷积建模远距离像素间的依赖关系，增强中心区域特征，从而捕获长程上下文。
4.  **轻量化设计**：策略性地使用深度可分离卷积与 1D（条带）卷积，在保持强特征提取能力的同时显著控制参数量与计算量。
5.  **多基准验证**：在 DOTA-v1.0、DOTA-v1.5、HRSC2016、DIOR-R 四个主流遥感检测基准上验证有效性。
## 方法

- **整体框架**：PKINet 是类似 VGG/ResNet 的**四阶段**特征提取骨干（Fig. 2a）。每个 Stage 采用**跨阶段部分（CSP）结构**：stage 输入经初始处理后沿通道维**对半切分**为两路——一路过简单**前馈网络（FFN）**，另一路过 `N_l` 个串联的 **PKI Block**；两路输出拼接后经 1×1 卷积融合，得到该 stage 输出。PKINet 可接入各种有向检测器（如 Oriented RCNN）产出最终检测结果。
- **输入输出**：输入为遥感图像，输出四个尺度的特征图 `F_l ∈ R^(C_l × H_l × W_l)`；论文设 `H_l = H/2^(l+1)`、`W_l = W/2^(l+1)`（`l=0,…,4`）。Stem 由三个 stride 为 (2,1,1) 的 3×3 卷积构成。
- **关键模块**：
    - **PKI 模块（§3.2）**：inception 风格模块。先用一个 `ks×ks` 小核卷积（`ks=3`）提取局部特征 `L`；再并行用 4 个深度可分离卷积 `DWConv_{k(m)×k(m)}` 提取多尺度上下文特征 `Z^(m)`，核尺寸 `k(m)=(m+1)×2+1`（即 **5,7,9,11**），`m=1,…,4`。**不使用扩张卷积**，避免稀疏特征。
    - **CAA 模块（§3.3）**：先对输入做平均池化 + 1×1 卷积得局部区域特征 `F_pool`；再用两个连续的深度可分离**条带卷积** `DWConv_{1×kb}` 和 `DWConv_{kb×1}` 近似一个大核 2D 深度卷积。选用条带卷积的两点理由：① 轻量——相比 `kb×kb` 2D 深度卷积，一对 1D 核可达近似效果而参数减少约 `kb/2` 倍；② 利于识别桥梁等**细长形物体**。核尺寸随阶段加深而增大：`kb = 11 + 2×l`。
- **模块连接（PKI Block 内部）**：输入 `X` 经 PKI 模块得 `P`；同一输入经 CAA 得注意力图 `A = Sigmoid(Conv1×1(F_h))`，将 `A` 用于增强 `P`；该 Block 输出再经 1×1 卷积得到 `X^(2)_{l,n}`。论文图 2(c) 显示 CAA 与 PKI 在 Block 内并行/串接协同（注意：CAA 输入取自 Block 输入 `X^(2)`，与 PKI 共享同一输入）。
- **数学公式/机制直观解释**：
    - PKI 模块通道融合：`P_{l-1,n} = Conv1×1( L_{l-1,n} + Σ_{m=1..4} Z^(m)_{l-1,n} )`（Eq. 4）。直观上：小核看细节，多个不同尺寸大核看不同范围"视野"，1×1 卷积做通道融合，把多感受野信息整合而不破坏局部纹理完整性。
    - CAA 增强：`F_attn = (A ⊙ P) ⊕ P`（Eq. 7），`⊙` 为逐元素乘、`⊕` 为逐元素加。直观上：`A` 是"关注度地图"，告诉网络 `P` 上哪些空间位置更重要，通过"乘 + 残差加"对重点区域增强。
- **训练方式**：两阶段。① 在 **ImageNet-1K** 上预训练 **300 epoch**（MMPretrain 工具箱），优化器 **AdamW**（动量 0.9、权重衰减 0.05），余弦学习率调度 + warm-up，**8 GPU、batch size 1024**。② 将预训练骨干接入具体检测器（如 Oriented RCNN）在遥感数据集上微调（检测器训练用 MMRotate，原文后续句被提取截断）。
- **和已有方法的差异**：与直接竞品 **LSKNet** 相比，两点核心区别——① PKINet 用 inception 风格**无扩张**深度卷积扩大感受野，避免稀疏特征；② PKINet 显式引入 **CAA** 建模长程上下文，而 LSKNet 主要依赖大核卷积。
## 实验

- **使用数据集**：
    1.  **DOTA-v1.0**：大规模遥感检测基准，15 类、2806 张图像、188,282 个实例；train/val/test 划分为 1,411 / 458 / 937 张。
    2.  **DOTA-v1.5**：DOTA-v1.0 的更难版本（DOAI Challenge 2019），新增"集装箱起重机（Container Crane, CC）"类别，并大量增加小于 10 像素的微小实例，共 **403,318** 个实例。
    3.  **HRSC2016**：舰船检测数据集，1061 张航拍图像（尺寸 300×300 至 1500×900），train/val/test = 436/181/444。
    4.  **DIOR-R**：基于 DIOR 的旋转框标注版本，**23,463** 张 800×800 图像，192,518 个标注。
- **对比方法**（DOTA-v1.0，表 2）：DETR 系（AO2-DETR, O2-DETR, ARS-DETR）、单阶段（SASM, R3Det-GWD/KLD, O-RepPoints, Rotated FCOS, S2ANet）、双阶段（SCRDet, Gliding Vertex, CenterMap, ReDet, Roi Trans, Rotated Faster R-CNN, O-RCNN）；并与 ResNet、ARC-R50、LSKNet-S 等骨干对比。
- **评价指标**：mAP、参数量（#P / #Params）、浮点运算次数（FLOPs）。
- **主实验结果（DOTA-v1.0，表 2，PKINet-S 作骨干替换 ResNet-50）**：
    - **O-RCNN**：ResNet-50 75.87 → LSKNet-S 77.49 → **PKINet-S 78.39**（最优；图 1 标注 +2.52）。
    - **S2ANet**：ResNet-50 74.12 → **PKINet-S 77.83**（+3.71）。
    - **Rotated FCOS**：ResNet-50 72.45 → **PKINet-S 74.86**（图 1 标注 +2.41）。
    - **R3Det**：ResNet-50 69.70 → **PKINet-S 75.89**（图 1 标注 +6.19）。
    - **Roi Trans**：ResNet-50 74.05 → **PKINet-S 77.17**（图 1 标注 +3.12）。
    - **Rotated Faster R-CNN**：ResNet-50 73.17 → **PKINet-S 76.45**。
    - 总体趋势：PKINet-S 在多种检测器上以**更少或相当的参数量**带来稳定增益。
- **骨干对比（表 3，均接 Oriented RCNN、ImageNet-1K 预训练 300 epoch）**：
    - **PKINet-T**：4.1M / 22.7G FLOPs，mAP **77.87**，优于 ResNet-18（11.2M / 38.1G，74.20）。
    - **PKINet-S**：13.7M / 70.2G FLOPs，mAP **78.39**，优于 ResNet-50（23.3M / 86.1G，75.87）。
    - 即参数量与 FLOPs 更低，mAP 反而更高。
- **网络配置（表 1）**：PKINet-T 各 stage Block 数 (4,14,22,4)、Embed Dim (32,64,128,256)、4.13M / 22.70G；PKINet-S 各 stage Block 数 (4,12,20,4)、Embed Dim (64,128,256,512)、13.69M / 70.20G。两者 PKI Block 核尺寸均 3×3 至 11×11。
- **消融实验**：提取文本仅含主表（表 2、表 3）与图 1 顶部"+gain"标注；针对 CAA / PKI 各组件的独立消融表在提取覆盖的前 11 页**未出现**（待核）。
- **泛化实验**：DOTA-v1.5、HRSC2016、DIOR-R 三个数据集的具体数值结果**未在提取文本中出现**（据原文后续页，提取缓存未覆盖，待核），文中仅声明 "Extensive experiments … demonstrate the effectiveness"。
- **效率信息**：参数量 / FLOPs 见上（表 1、表 3）；**推理速度（FPS）未在提取文本中明确**。
## 局限

1.  **计算成本绝对值仍偏高**：PKINet-S 的 70.2G FLOPs 虽低于 ResNet-50，但对资源严格受限的边缘设备部署仍有挑战。
2.  **对极小目标的专门分析缺失**：DOTA-v1.5 含大量 <10 像素实例，但该尺度段的细分检测效果在提取文本中未单列分析（待核）。
3.  **CAA 贡献度的定量消融**：去掉 CAA 后掉多少点等定量消融未在提取覆盖页出现（提取缓存未覆盖，待核）。
4.  **领域泛化**：方法验证集中于遥感有向检测，多尺度无扩张卷积 + CAA 在自然图像或分割/分类等其他任务上的有效性未被探索。
5.  **复现细节**：虽有 GitHub 链接，但 CSP 中 FFN 的具体构成、检测器训练阶段超参（提取在 "MMRo…" 处截断）、数据增强策略等未在提取文本中完整给出。
## 个人评论

1.  **解决矛盾的设计思路清晰**：把"大核卷积→噪声 / 扩张卷积→稀疏"这对矛盾讲得很透，并以"无扩张多尺度卷积 + 专用长程注意力"协同破局，动机—方法—模块的对应关系干净利落。
2.  **两个模块的可借鉴性强**：
    - **PKI 模块**示范了如何用并行多尺寸**常规**深度卷积高效拿到多尺度信息——通用、可插拔，可直接迁移到其他检测/分割骨干。
    - **CAA 模块**用一对 1D 条带卷积近似大核 2D 卷积（参数省约 `kb/2`），既轻量又天然契合桥梁等细长目标，是轻量长程注意力的一个实用范式。
3.  **"巧设计"优于"堆算力"**：大量深度可分离 + 1D 卷积让 PKINet-T/S 在 mAP 反超更重模型的同时显著降参降算力，符合轻量骨干的工程取向。
4.  **实验面铺得足**：在 6+ 种下游检测器上以骨干替换验证通用性，说服力强；若提取后续页含三数据集数值与组件消融，证据链会更完整。
5.  **可疑/可深挖处**：CAA 与 PKI 在 Block 内究竟是"并行"还是"先 PKI 再 CAA 增强"——摘要说 "in parallel"，但 Eq.(7) 显示 CAA 的注意力 `A` 作用于 PKI 输出 `P`，二者输入共享而增强串接，建议结合 Fig.2(c)/代码核实数据流。

### 使用建议

- **如果快速了解**：读 Abstract、Introduction、Fig.1、Fig.2，以及 Table 2、Table 3，约 10 分钟掌握核心思想、结构与主结果。
- **如果复现**：精读 §3（尤其 3.2 PKI 模块、3.3 CAA）与 §3.4 实现细节，对照 Table 1 网络配置与 GitHub 代码；§4.1 的预训练/检测器训练超参（AdamW、cosine、300 epoch、batch 1024）是关键。
- **如果借鉴创新点**：重点学 PKI 模块（多尺度并行无扩张卷积）与 CAA 模块（条带卷积近似大核的轻量长程注意力），思考如何嵌入自己的多尺度特征建模管线。
- **如果写 related work**：可归入"**为遥感检测设计的特征提取骨干**"与"**轻量级/多尺度注意力机制**"两类。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C_目标检测_通用与旋转框]]
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**遥感图像有向（旋转框 OBB）目标检测**方向，核心是为该任务设计**特征提取骨干网络**（PKINet）及其内置的**上下文锚点注意力 CAA 模块**。因此最贴切的主主题是 **"C_目标检测_通用与旋转框"**（旋转框检测），并与 **"B_注意力算子模块"**（CAA 是一种可插拔注意力算子）交叉。它要解决遥感图像中**目标尺度变化巨大**与**上下文多样**两大难题。

## 2. 一句话总结
本文提出多尺度**无扩张**卷积骨干 **PKINet** 及核心组件**上下文锚点注意力（CAA）**：用并行多尺度深度卷积捕获局部多尺度上下文、用条带卷积构成的 CAA 捕获长程上下文，二者协同，在 DOTA/HRSC/DIOR-R 等遥感检测基准上以更少参数取得更高 mAP。

## 3. 背景与问题
- **为什么要做**：遥感图像鸟瞰采集，物体尺度跨度极大（足球场↔车辆），识别强依赖周围环境上下文。OBB 检测器虽多，但 RSI 特有的尺度/上下文挑战在**特征提取骨干**层面仍待深挖。
- **之前方法的问题**：
    - 多尺度融合 / FPN 等对不同尺度物体使用**相同感受野**，无法为大物体提供足够上下文。
    - 竞品 LSKNet 用**大核卷积**（→ 引入背景噪声，害小目标）和**扩张卷积**（→ 遗漏细节、特征稀疏）扩大感受野。
- **核心矛盾**：不引入背景噪声、也不产生稀疏特征的前提下，为尺度差异巨大的目标自适应捕获**局部 + 全局**上下文。

## 4. 核心贡献
1.  **PKINet 骨干**：专为遥感检测设计的轻量强骨干；自称首个把 inception 风格卷积 + 全局上下文注意力用于遥感检测。
2.  **PKI 模块**：并行多尺度（5/7/9/11）深度可分离卷积、无扩张，提取稠密多尺度纹理并通道融合，捕获局部上下文。
3.  **CAA 模块**：全局平均池化 + 1D 条带卷积（`1×kb` 接 `kb×1`）近似大核 2D 卷积，建模远距离像素依赖、增强中心特征。
4.  **轻量范式**：深度可分离 + 1D 卷积大幅降参降算。
5.  **四基准验证**：DOTA-v1.0/v1.5、HRSC2016、DIOR-R。

## 5. 方法详解
- **整体框架**：四阶段骨干，每阶段为 CSP 结构——输入沿通道对半切分，一路过 FFN，一路过 `N_l` 个 PKI Block，两路拼接后 1×1 卷积融合（Eq.1–2）。可接 Oriented RCNN 等检测器。Stem 为三个 stride (2,1,1) 的 3×3 卷积。
- **PKI 模块（Eq.3–4）**：`L = Conv_{3×3}(X)`；`Z^(m) = DWConv_{k(m)×k(m)}(L)`，`k(m)=(m+1)×2+1 ∈ {5,7,9,11}`；`P = Conv_{1×1}(L + Σ Z^(m))`。无扩张卷积，避免稀疏特征；1×1 卷积做多感受野通道融合。
- **CAA 模块（Eq.5–8）**：`F_pool = Conv_{1×1}(AvgPool(X))`；`F_w = DWConv_{1×kb}(F_pool)`，`F_h = DWConv_{kb×1}(F_w)`；`A = Sigmoid(Conv_{1×1}(F_h))`；`F_attn = (A ⊙ P) ⊕ P`；Block 输出 `X^(2)_{l,n} = Conv_{1×1}(F_attn)`。`kb = 11 + 2×l`（随阶段加深增大）。条带卷积理由：轻量（省约 `kb/2` 参数）+ 利于细长目标（桥梁等）。
- **机制直观**：PKI 小核看细节、多大核看不同视野、1×1 融合；CAA 产出"关注度地图" `A`，以"乘 + 残差加"增强 `P` 的重点区域。
- **训练**：ImageNet-1K 预训练 300 epoch（AdamW，动量 0.9，权重衰减 0.05，cosine + warm-up，8 GPU，batch 1024）；再接检测器在遥感集上微调（检测器训练用 MMRotate，提取截断）。
- **vs LSKNet**：① 无扩张 inception 卷积 vs 大核+扩张；② 显式 CAA 长程注意力 vs 主要靠大核。

## 6. 实验与结果
- **数据集**：DOTA-v1.0（15 类 / 2806 图 / 188,282 实例，1411/458/937 划分）；DOTA-v1.5（新增 Container Crane，<10px 微小实例剧增，403,318 实例）；HRSC2016（舰船，1061 图，436/181/444）；DIOR-R（23,463 张 800×800，192,518 标注）。
- **指标**：mAP / #Params / FLOPs。
- **DOTA-v1.0 主表（表 2，PKINet-S 替换 ResNet-50）**：O-RCNN 75.87→**78.39**（>LSKNet-S 77.49）；S2ANet 74.12→**77.83**；Rotated FCOS 72.45→**74.86**；R3Det 69.70→**75.89**；Roi Trans 74.05→**77.17**；Rotated Faster R-CNN 73.17→**76.45**。
- **骨干对比（表 3，接 O-RCNN）**：PKINet-T 4.1M/22.7G → mAP **77.87**（>ResNet-18 74.20）；PKINet-S 13.7M/70.2G → mAP **78.39**（>ResNet-50 75.87）。参数与算力更低，mAP 更高。
- **配置（表 1）**：T 各 stage Block (4,14,22,4)、Dim(32,64,128,256)、4.13M/22.70G；S 各 stage Block (4,12,20,4)、Dim(64,128,256,512)、13.69M/70.20G。
- **消融 / 三数据集数值**：未在提取覆盖的前 11 页出现（提取缓存未覆盖，待核）；推理速度未明确。

## 7. 这篇论文真正有价值的地方
1.  **矛盾拆解干净**：把"大核噪声 vs 扩张稀疏"讲透并用"无扩张多尺度 + 专用长程注意力"协同破局，动机—方法对应清晰。
2.  **两个可插拔模块**：PKI（并行多尺寸常规深度卷积拿多尺度信息）与 CAA（一对 1D 条带卷积近似大核、省约 `kb/2` 参数、利于细长目标），都是可迁移的轻量设计。
3.  **巧设计优于堆算力**：深度可分离 + 1D 卷积让 T/S 在 mAP 反超更重模型的同时降参降算。
4.  **实验通用性**：在 6+ 种下游检测器上以骨干替换验证，说服力强。

## 8. 局限与问题
1.  PKINet-S 70.2G FLOPs 绝对值仍偏高，边缘部署有挑战。
2.  <10px 极小目标的细分效果在提取文本中无单列分析（待核）。
3.  CAA 的定量消融在提取覆盖页缺失（提取缓存未覆盖，待核）。
4.  仅验证遥感有向检测，跨任务/跨域有效性未探索。
5.  复现细节（FFN 构成、检测器训练超参、数据增强）在提取文本中不完整。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Intro + Fig.1/2 + Table 2/3，约 10 分钟。
- **复现**：精读 §3.2/§3.3/§3.4 + Table 1 + GitHub；预训练/检测器超参是关键。
- **借鉴创新点**：迁移 PKI（多尺度并行无扩张卷积）与 CAA（条带卷积近似大核的轻量长程注意力）。
- **写 related work**：归入"遥感检测特征提取骨干"与"轻量级/多尺度注意力机制"。

## 10. 和其他论文的关系
- **直接对比 baseline**：[[LSKNet]]（大核 + 扩张的遥感骨干，本文逐点对比并改进）。
- **注意力机制对照**：[[CBAM]]、[[SENet]]，对照 CAA 的空间锚点 + 条带卷积思路差异。
- **多尺度/inception 渊源**：[[InceptionNet]]、[[Res2Net]]，PKI 模块的并行多核与之同源。
- **轻量卷积**：[[MobileNet系列]]，本文大量使用深度可分离与 1D 条带卷积。
- **下游检测器**：Oriented RCNN、S2ANet、Roi Trans 等旋转框检测器是本文骨干的承载框架。

## 11. 关键词
- 遥感目标检测
- 有向边界框（OBB）/ 旋转框检测
- 多尺度卷积 / inception 风格卷积
- 上下文锚点注意力（CAA）
- 无扩张（non-dilated）卷积
- 条带卷积（strip convolution）
- 特征提取骨干网络
- 轻量级网络 / 深度可分离卷积
- DOTA / HRSC2016 / DIOR-R 数据集

## 12. 可信度说明
本篇精读主要基于 PDF 提取文本的**前 11 页（11/11，提取脚本上限）**，覆盖摘要、引言、相关工作、方法论（§3 全部公式 Eq.1–8）、实现细节（§3.4）、Table 1 配置、Table 2（DOTA-v1.0 主表）、Table 3（ResNet 对比）及 §4.1 数据集/训练设置。提取质量良好、结构清晰，模块设计、数学公式、主要数值均可逐条核对。**未覆盖**部分：DOTA-v1.5/HRSC2016/DIOR-R 的具体数值、组件消融表、推理速度、检测器训练阶段超参（提取在 "MMRo…" 处截断）；这些已明确标注"提取缓存未覆盖，待核"。年份已据 arXiv 标识由原 2016 更正为 2024；venue 由重复标题改为 arXiv 标识（CVPR 2024 线索待核）；primary_topic 由 B 调整为 C（旋转框检测为论文主体，B 作为 CAA 注意力交叉主题保留）。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 2276 字符/页); 来源缓存: `.paper-cache/extracts/CAA&PKIBlock.txt` (11/11 页, 提取脚本上限, 原文约 55828 字符); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮深度重读据提取文本核对并修订年份/venue/分类。
<!-- AI_READING_NOTE_END -->
