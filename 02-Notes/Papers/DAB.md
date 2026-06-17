---
title: "DEFORMTIME: Capturing Variable Dependencies"
authors:
  - "Yuxuan Shu"
  - "Vasileios Lampos"
year: 2024
venue: "arXiv"
doi: 
pdf: [[DAB.pdf]]
primary_topic: B_注意力算子模块
topics:
  - "B_注意力算子模块"
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
extract_cache: .paper-cache/extracts/DAB.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/29 pages"
---
# DEFORMTIME: Capturing Variable Dependencies

## 基本信息
- **PDF**: [[DAB.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | DEFORMTIME: Capturing Variable Dependencies with Deformable Attention for Time Series Forecasting |
| **作者** | Yuxuan Shu, Vasileios Lampos (University College London) |
| **发表时间** | 2024 (arXiv:2406.07438v2, 18 Jun 2024) |
| **刊物/会议** | arXiv (cs.LG) |
| **DOI** | 未明确 |
| **代码** | github.com/ClaudiaShu/DeformTime |

## 摘要

> **清理后英文原文**：In multivariate time series (MTS) forecasting, existing state-of-the-art deep learning approaches tend to focus on autoregressive formulations and overlook the information within exogenous indicators. To address this limitation, we present DEFORMTIME, a neural network architecture that attempts to capture correlated temporal patterns from the input space, and hence, improve forecasting accuracy. It deploys two core operations performed by deformable attention blocks (DABs): learning dependencies across variables from different time steps (variable DAB), and preserving temporal dependencies in data from previous time steps (temporal DAB). Input data transformation is explicitly designed to enhance learning from the deformed series of information while passing through a DAB. We conduct extensive experiments on 6 MTS data sets, using previously established benchmarks as well as challenging infectious disease modelling tasks with more exogenous variables. The results demonstrate that DEFORMTIME improves accuracy against previous competitive methods across the vast majority of MTS forecasting tasks, reducing the mean absolute error by 10% on average. Notably, performance gains remain consistent across longer forecasting horizons.

> **中文翻译**：在多变量时间序列（MTS）预测中，现有最先进的深度学习方法往往聚焦于自回归形式，而忽视了外生指标中蕴含的信息。为解决这一局限，我们提出 DEFORMTIME——一种试图从输入空间捕捉相关时序模式、从而提升预测精度的神经网络架构。它部署了由"可变形注意力块（DAB）"完成的两项核心操作：学习不同时间步上跨变量的依赖关系（variable DAB / V-DAB），以及保持来自先前时间步的时序依赖（temporal DAB / T-DAB）。模型显式设计了输入数据变换，以增强在数据流经 DAB 时从"形变序列信息"中的学习能力。我们在 6 个 MTS 数据集上开展了大量实验，既包含已有的公开基准，也包含外生变量更多、更具挑战性的传染病建模任务。结果表明，DEFORMTIME 在绝大多数 MTS 预测任务上较此前的竞争方法提升了精度，平均将平均绝对误差（MAE）降低了 10%。值得注意的是，性能增益在更长的预测步长上保持稳定。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：在多变量时间序列预测任务中，当前 SOTA 模型偏好"多对多（many-to-many）序列架构"，但这种范式对于"存在一个明确目标（内生）变量 + 大量外生变量"的任务并不一定提供正确的学习机制。许多神经网络（如 [16,17,23,32,53]）并未设计用于纳入**变量间依赖**，而这正是传统预测器（如 [3,14,34]）的关键属性。
- **之前方法的问题**：
    1. 基于 RNN 的模型（[19,25]）能在一定程度上捕捉历史时间步信息，但建立**跨变量依赖**的能力有限。
    2. 尝试建模变量间依赖的模型（LightTS 用 MLP 先沿时间再沿变量建模；Crossformer 先做时序分块再用 router 模块跨变量聚合）后来被**不建立变量间依赖**的更新模型（[16,17,23,32,53]，如 DLinear、PatchTST）超越。后者论点是：不建模变量间依赖可使用更长回溯窗口而不显著增加复杂度（[11]）。
    3. 一个贯穿文献的普遍问题是**基准任务本身可能不恰当**（详见附录 A.5），使得上述结论的可靠性存疑。
    4. 近期工作（[56]）指出，要在利用变量间依赖的同时提升性能，需要在**时间上对齐输入时间序列**上投入更多努力——这启发本文引入对输入的"引导式重排"。
- **作者的核心思路**：把源自计算机视觉的**可变形（deformable）机制**（[5] 提出用于让 CNN 适应几何变换，与 Transformer 结合后在多任务取得 SOTA [4,48,60]）引入 MTS 预测，在 Transformer 编码器之上叠加可变形模块，使得"感受野（receptive field）"在不同变量与时间步上具有灵活性，从而更好地从内生尤其是**外生变量**的关键模式中学习。

## 关键贡献

1.  **提出 DEFORMTIME 模型**：一个新颖的 MTS 预测模型，可在不同时间粒度上更好地捕捉**变量间（inter-）与变量内（intra-）依赖**；核心是两个可变形注意力块 V-DAB（跨变量）与 T-DAB（跨时间）。
2.  **设计两个核心 DAB**：
    - **V-DAB（变量可变形注意力块）**：捕获**不同时间步上跨变量的依赖**。
    - **T-DAB（时间可变形注意力块）**：捕获**同一变量在不同时间周期的依赖**。
3.  **显式输入变换**：设计**邻域感知输入嵌入（NAE）**——按变量与目标的线性相关性重排并分组嵌入，使后续基于偏移采样的 CNN 能从"形变后的序列信息"中学习。
4.  **更全面的实验**：在 **3 个已有基准 + 3 个新的传染病流行率任务**上评估，每个任务覆盖 **4 个递增的预测步长**。作者论证疾病任务支持更彻底的评估，因为其外生变量多、跨越多年（其中 4 年作为独立的年度测试期）。
5.  **显著提升**：相比每次最强的竞争方法，**MAE 平均降低 10%**（基准任务平均降 7.4%，疾病预测任务平均降 12.6%），且增益随预测步长增大保持稳定。
6.  **附带发现**：尝试建立某种变量间依赖的模型，在更具挑战性的疾病预测任务上表现更好，凸显了需要更恰当的评估方法。

## 方法

**整体框架**：DEFORMTIME 是编码器-解码器结构。编码器的每一层包含两条并行分支，分别嵌入 **V-DAB（左）** 与 **T-DAB（右）**，分别捕捉跨变量与跨时间依赖；解码器是一个 **2 层 GRU**。

**任务定义与输入输出**（第 2 节）：
- 任务聚焦**单一目标变量**：可有多个输入、可选多个输出，但只关心一个输出变量的预测。采用滚动窗口、回溯窗口长度 `L`。
- 在时间步 `t`：`Q_t ∈ R^{L×C}` 是 `C` 个外生变量在 `L` 个时间步上的序列；`y_{t-δ} ∈ R^L` 是目标变量的 `L` 个自回归历史值，`δ∈N0` 是外生变量与目标变量之间的可选观测延迟（实时传染病预测中 ILI 率延迟 `δ=7` 或 `14` 天，见附录 A.2）。拼接得 `Z_t = [Q_t, y_{t-δ}] ∈ R^{L×(C+1)}`。
- **输出**：预测目标 `y_{t+H} ∈ R^H`（`H` 为预测步长）。部分基线采用多任务形式，让每个输入变量都成为预测目标（`Y_{t+H} ∈ R^{H×(C+1)}`）；但精度只在 `ŷ_{t+H} ∈ R` 最终估计上报告。

**关键模块与连接**：
1.  **多头注意力回顾（3.1）**：标准 Vaswani 注意力，`Q,K,V` 由 `Z` 经线性投影得到，分 `M` 头；`M=1` 即单头注意力。
2.  **邻域感知输入嵌入 NAE（3.2）**：
    - **操作**：先按各变量与目标变量的**时间对齐线性相关性**对 `Z` 的 `C+1` 个变量重排（附录 C.1）；再将变量分为 `G` 个邻域组，每组用全连接层独立嵌入到 `d/G` 维（变量数不能被 `G` 整除时零填充），拼接得 `E ∈ R^{L×d}`；加正弦位置编码 `P_n` 并层归一化，得 `Z_e = LN(E + P_n)`。`d` 和 `G` 都是可训练超参数。
    - **目的**：偏移采样 CNN 在捕捉相邻变量关系上有局限，NAE 通过把相关变量排在一起来缓解。
3.  **V-DAB（3.3）**：
    - 将 `Z_e` 沿时间维分割为重叠 patch：分段长 `ℓ`、步长 `s≤ℓ`，得 `n=⌊(L−ℓ)/s⌋+1` 个 patch `Z_p ∈ R^{ℓ×d}`。
    - patch 内每点记为 `(行,列)` 索引 `p=(i,j)`；对查询 `Q_p=Z_p W_Q` 经 **2D CNN `θ_off`**（一个 `k×k` 卷积捕捉邻域 + 一个 `1×1` 卷积投影）生成二维偏移 `Δp = α·tanh(θ_off(Q_p))`（`α∈R>0` 为可学习幅度，控制采样范围上界）。
    - 用 `Δp` 与**双线性插值** `ψ` 在 `p+Δp` 的 `2×2` 网格上采样得形变 patch `Z_d = ψ(Z_p; p+Δp)`（越界处用零插值）。`K_d=Z_d W_K`，`V_d=Z_d W_V + P_v`（`P_v` 为相对位置偏置，保留形变后的成对位置信息）。
    - **单头自注意力**：`A_i = softmax(Q_p K_d^T/√d) V_d W_i`，注意 Query 来自原始 patch、Key/Value 来自形变 patch。所有 patch 输出沿时间维拼接为 `A ∈ R^{(n·ℓ)×d}`，再经全连接 `Z_v = W_v^T A ∈ R^{L×d}`。
4.  **T-DAB（3.4）**：
    - 接收与 V-DAB 相同的输入 `Z_e`。先把每列 `z_e∈R^L` 重塑为 `z'_e ∈ R^{r×κ}`（`r` 为时间窗、`κ=L/r`），从而 `Z_e → Z'_e ∈ R^{r×κ×d}`，含 `r` 个 patch（`Z_r ∈ R^{κ×d}`）。`r` 可在不同编码器层取不同值以捕捉多种时间粒度（`r=1` 时 `Z_e` 不变）。
    - `Q_r = Z_r U_Q`；偏移在 `G` 个相关子组间**共享**（沿用 NAE 的分组）：每子组 `Q_g ∈ R^{κ×(d/G)}` 共享 `Δp(g) = α·tanh(η_off(Q_g))`，`η_off` 为 **1D CNN**（`k×1` 与 `1×1` 卷积），`α` 与 V-DAB 同。
    - 用**线性插值** `ϕ`（沿 2 个相邻点，区别于 V-DAB 的双线性）得形变序列 `Z_s^{(g)} = ϕ(z_r∈Z_r^{(g)}; p+Δp(g))`。`K_s=Z_s U_K`，`V_s=Z_s U_V + P_t`。
    - **多头注意力**：把 `K_s,V_s` 分为 `G` 组，`A_g = softmax(Q_g K_g^T/√(d/G)) V_g`，按列拼接并线性投影，得 `Z_t ∈ R^{L×d}`（重排回原时间结构，与 `Z_v` 对齐）。
5.  **编码器（3.5）**：2 个编码器层（与 [28,46] 一致）。每层两条 DAB 分支，残差连接内置层归一化；分支算子为 `Z_i = Drop(DAB(Z_e)) + Z_e`，`Z_c = Drop(MLP(LN(Z_i))) + Z_e`，其中 `Drop` 为**随机深度（stochastic depth, [12]）**且 drop 概率可学习，`MLP` 是带 ReLU、隐藏维 `d` 的 2 层感知机。两分支输出沿第二维拼接，过全连接得该层输出 `Z_j ∈ R^{L×d}`。
6.  **编码器-解码器结构（3.6）**：层间分层堆叠 `Z_j = Enc(Z_{j-1})`。最终编码输出送入 **2 层 GRU 解码器**（隐藏维 `d`），输出 `Z_out` 维度仍为 `L×d`；再经一个带 **LeakyReLU**、隐藏维 `d` 的 2 层感知机沿时间维投影到 `Z'_out ∈ R^{H×d}`，最后过全连接线性投影到 `ŷ ∈ R^H`。

**机制直观解释**：可变形注意力的核心是**偏移量生成** `Δp = α·tanh(θ_off(Q))`——模型据当前内容（Query）动态决定"去哪里采样"，从而在一个**由输入内容动态生成的不规则网格**上做注意力，而非固定规则网格，提供更大灵活性。

**训练方式**：损失函数与优化器在提取文本（前 12 页）中未明确，按惯例推断为标准时序预测损失端到端训练（PDF 文本未明确，具体在附录 C，提取缓存未完整覆盖）。

**和已有方法的差异**：
- **vs Crossformer**：Crossformer 用固定 patch 划分 + 学习的 router 跨变量聚合；DEFORMTIME 引入**连续可学习偏移**，通过形变直接调整采样位置，机制更灵活。
- **vs PatchTST / iTransformer**：这些模型为单变量或未显式建模变量间依赖；DEFORMTIME 通过 V-DAB **显式建模变量间依赖**。
- **vs LightTS**：LightTS 用 MLP 分别沿时间/变量建模；DEFORMTIME 用**基于注意力的形变模块**。

## 实验

- **数据集（6 个）**：
    - **3 个公开基准**：Weather、ETTh1、ETTh2。温度分辨率：weather 为 **10 分钟**、ETT 为 **1 小时**。目标变量：ETT 取**油温（oil temperature）**，weather 取**湿球温度（wet-bulb temperature）**，其余指标作外生变量。
    - **3 个疾病预测任务**：ILI-ENG（英格兰流感样病例率）、ILI-US2、ILI-US9（美国 HHS 第 2、9 区 ILI 率）。引入**网络搜索频率时间序列**作为外生预测变量；这些任务的外生变量明显多于 ETT/weather。
- **预测步长**：ETT/weather 取 `H∈{96,192,336,720}`（单一测试折）；ILI 取 `H∈{7,14,21,28}` 天，在 4 个连续流感季（2015/16–2018/19）上做 4 个独立测试折。
- **对比方法**：6 个 SOTA 竞争模型——LightTS、DLinear、Crossformer、PatchTST、iTransformer、TimeMixer，外加朴素持续性（naïve persistence）基线（附录 B）。ILI 任务对所有模型调参；基准任务上除 Crossformer、LightTS 外沿用官方仓库设置复现。
- **评价指标**：MAE 与 sMAPE（表中以 ϵ% 表示）。
- **主实验结果（Table 1，提取文本含完整数表）**：最优结果加粗、次优加下划线。
    - **平均提升**：相比每次最强竞争方法 MAE 平均降 **10%**（基准 7.4%、疾病 12.6%）。
    - **样例数值（MAE）**：ETTh1 H=96 → DEFORMTIME **0.1941** vs PatchTST 0.2017；ETTh2 H=720 → **0.3640** vs iTransformer 0.4565；Weather H=96 → **0.0244** vs Crossformer 0.0271 / DLinear 0.0251；ILI-ENG H=7 → **1.6417** vs Crossformer 1.8698；ILI-US2 H=7 → **0.4122** vs Crossformer 0.4400。
    - **长程稳定性**：随 `H` 增大优势保持稳定（如 ETTh1 H=720、ILI H=28 仍领先）。
    - 注：Weather H=720（0.0363）与 DLinear（0.0352）非常接近，DLinear 略优；个别基准长程点上 DEFORMTIME 为次优而非最优——总体仍是绝大多数任务领先。
- **消融与效率**：第 4 节开头声明"提供 ablation study 与 computational complexity / efficiency analysis"，但具体结果在提取的前 12 页之外（据原文后续页/附录，提取缓存未覆盖，待核）。

## 局限

1.  **额外计算开销**：每个 DAB 需 CNN 生成偏移并做插值采样，可能增加计算量与参数量；前 12 页提取文本未给出参数量/FLOPs/速度的具体对比（效率分析见后续页/附录，提取缓存未覆盖）。
2.  **对输入变换的依赖**：性能可能对 NAE 的相关性重排与分组数 `G` 敏感，增加预处理与调参负担。
3.  **基准数量有限且作者亦质疑基准恰当性**：仅 3 个公开基准；论文自身在附录 A.5 批评常用基准任务的不恰当性（如某些 ILI 基准存在 24/60 周的超长预测步长）。
4.  **可解释性**：偏移量虽给出"关注位置"线索，但 DAB 内部机制的可解释性论文未深入探讨。
5.  **复现复杂度**：涉及 NAE、V/T-DAB、随机深度、`G`/`r`/`ℓ`/`s` 等多个自定义模块与超参；完整复现需参照代码与附录（A、C、D 等，提取缓存未完整覆盖）。

## 个人评论

1.  **跨域迁移的范例**：把 CV 中成熟的**可变形（deformable）注意力/卷积**思想迁移到时序预测，把"感受野"从固定网格变为内容驱动的不规则采样，是一个干净且有解释力的切入点。
2.  **双维度解耦**：V-DAB（跨变量）与 T-DAB（跨时间）分别针对两个正交依赖维度，且二者在采样上有意区分（双线性 vs 线性插值、单头 vs 分组多头、2D vs 1D CNN 偏移），设计上自洽。
3.  **强调输入表示**：NAE 把"先按相关性重排再分组嵌入"前置，体现了"数据表示与模型模块同等重要"的工程观——这一点对改造其他时序模型有借鉴意义。
4.  **评估观值得学习**：作者不仅跑标准基准，还构造外生变量更丰富的疾病任务，并在论文中正面批评既有基准的不恰当性（附录 A.5）。这种"质疑评估口径"的自觉比单纯刷点更有价值。
5.  **可改进处**：偏移幅度 `α`、分组数 `G`、时间窗 `r` 等耦合超参较多，论文对其敏感性与最优配置的讨论需查附录；本笔记基于前 12 页，效率/消融结论待补读后续页核实。

### 使用建议

- **快速了解**：读摘要、引言与 Table 1，即可把握动机、方法骨架与主要数值。
- **复现**：精读第 3 节并对照 Figure 1 理解 Segment/Adapt 数据操作；务必查附录 A（数据与评估设置）、C（实现/超参/变量排序 C.1）、D（分季完整结果）。源代码：github.com/ClaudiaShu/DeformTime。
- **借鉴创新点**：学习 DAB 的偏移生成 `Δp=α·tanh(θ_off(Q))` 与形变插值机制，可尝试把 V-DAB/T-DAB 迁移到其他需建模动态序列依赖的任务。
- **写 related work**：可归入"基于 Transformer 的时序预测"（对比 PatchTST、Crossformer）、"显式建模变量间依赖的 MTS 模型"（对比 Crossformer、LightTS）、"可变形/动态注意力"（对比 CV 中的 Deformable DETR）。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**多变量时间序列（MTS）预测**方向，核心创新是一个**注意力算子模块**——可变形注意力块（DAB）。因此归入 **「B_注意力算子模块」** 主题：论文的主贡献不是某个具体应用任务，而是把"内容驱动的偏移采样 + 注意力"作为可复用算子引入时序建模（V-DAB 跨变量、T-DAB 跨时间）。taxonomy 中无独立时序类别，B 是最贴切的归类。

## 2. 一句话总结
DEFORMTIME 用两类**可变形注意力块**（V-DAB 跨变量、T-DAB 跨时间）对输入序列做内容驱动的偏移采样与插值形变，再做注意力计算，从而更好地捕捉 MTS 中跨变量与跨时间的动态依赖、充分利用外生变量，平均把 MAE 降低 10%。

## 3. 背景与问题
- **为什么要做**：SOTA MTS 模型偏好多对多序列架构，对"单一目标变量 + 大量外生变量"的任务并非最优；且多数模型未设计变量间依赖建模，而这是传统预测器的关键属性。
- **之前方法的问题**：
    1. RNN（[19,25]）能部分捕捉历史信息但建立跨变量依赖能力有限。
    2. 建模变量间依赖的 LightTS、Crossformer 反被不建模变量间依赖的 DLinear/PatchTST 等超越，后者靠更长回溯窗口取胜（[11]）。
    3. 文献中常用基准任务的"不恰当性"使上述结论存疑（附录 A.5）。
    4. [56] 指出利用变量间依赖需更好地时间对齐输入——启发本文的输入引导式重排（NAE）。
- **核心思路**：将 CV 的可变形机制（[5]）与 Transformer 结合，在编码器上叠加可变形模块，让感受野在变量与时间步上灵活，从外生变量关键模式中学习。

## 4. 核心贡献
1.  DEFORMTIME：在不同时间粒度捕捉变量间/变量内依赖，含 V-DAB（跨变量）与 T-DAB（跨时间）两个 DAB。
2.  NAE：按相关性重排 + 分组嵌入的显式输入变换，配合偏移采样。
3.  在 3 公开基准 + 3 传染病任务、各 4 个递增步长上评估；论证疾病任务因外生变量多、跨多年（4 年作独立测试折）更利于彻底评估。
4.  MAE 平均降 10%（基准 7.4%、疾病 12.6%），长程稳定。
5.  附带发现：建立变量间依赖的模型在更难的疾病任务上更优，呼吁更恰当的评估。

## 5. 方法详解
**框架**：编码器-解码器；编码器每层 = V-DAB 分支(左) + T-DAB 分支(右)并行，解码器为 2 层 GRU。

**任务定义（§2）**：滚动窗口、回溯 `L`。`Q_t∈R^{L×C}`（C 个外生变量）、`y_{t-δ}∈R^L`（目标历史，`δ` 为观测延迟，ILI 实时预测中 δ=7/14 天）。拼接 `Z_t=[Q_t,y_{t-δ}]∈R^{L×(C+1)}`，学函数 `f: Z_t → y_{t+H}`，精度只在最终估计 `ŷ_{t+H}∈R` 报告。

**NAE（§3.2）**：按与目标的时间对齐线性相关性重排 `C+1` 个变量 → 分 `G` 组各嵌入到 `d/G` 维 → 拼接得 `E∈R^{L×d}` → 加正弦位置编码并层归一化 `Z_e=LN(E+P_n)`。`d`、`G` 可训练。

**V-DAB（§3.3）**：`Z_e` 沿时间分割为 `n=⌊(L−ℓ)/s⌋+1` 个重叠 patch `Z_p∈R^{ℓ×d}`。偏移 `Δp=α·tanh(θ_off(Q_p))`（`θ_off` 为 2D CNN：`k×k` + `1×1`）；双线性插值 `Z_d=ψ(Z_p;p+Δp)`；`K_d=Z_d W_K`，`V_d=Z_d W_V+P_v`。**单头**自注意力 `A_i=softmax(Q_p K_d^T/√d)V_d W_i`（Q 来自原 patch、K/V 来自形变 patch），拼接过 FC 得 `Z_v∈R^{L×d}`。

**T-DAB（§3.4）**：每列 `z_e∈R^L` 重塑为 `r×κ`（`κ=L/r`，`r` 跨层可变以建多粒度，`r=1` 不变）。偏移在 `G` 组间共享 `Δp(g)=α·tanh(η_off(Q_g))`（`η_off` 为 1D CNN：`k×1`+`1×1`）；**线性插值** `Z_s^{(g)}=ϕ(...)`。`K_s=Z_s U_K`，`V_s=Z_s U_V+P_t`。**分组多头**注意力 `A_g=softmax(Q_g K_g^T/√(d/G))V_g`，重排回原结构得 `Z_t∈R^{L×d}`。

**编码器（§3.5）**：2 层。分支算子 `Z_i=Drop(DAB(Z_e))+Z_e`，`Z_c=Drop(MLP(LN(Z_i)))+Z_e`，`Drop` 为可学习概率的随机深度，`MLP` 为 ReLU 2 层。两分支输出拼接过 FC 得 `Z_j`。

**编码-解码（§3.6）**：层间堆叠 `Z_j=Enc(Z_{j-1})` → 2 层 GRU(隐藏维 d) → 带 LeakyReLU 的 2 层 MLP 沿时间维投影到 `Z'_out∈R^{H×d}` → FC → `ŷ∈R^H`。

**直观解释**：`Δp=α·tanh(θ_off(Q))` 让模型内容驱动地"决定去哪采样"，在动态生成的不规则网格上做注意力，区别于标准注意力的固定规则网格。

**和已有方法差异**：vs Crossformer（连续可学习偏移 vs 固定 patch + router）；vs PatchTST/iTransformer（显式建模变量间依赖）；vs LightTS（注意力形变 vs MLP）。

## 6. 实验与结果
- **数据集**：Weather(10min)、ETTh1/ETTh2(1h)，目标分别为湿球温度、油温；ILI-ENG/US2/US9（外生变量为网络搜索频率，外生变量数显著更多）。
- **步长**：ETT/weather `H∈{96,192,336,720}`（单折）；ILI `H∈{7,14,21,28}` 天（4 个流感季 2015/16–2018/19 作 4 折）。
- **对比**：LightTS、DLinear、Crossformer、PatchTST、iTransformer、TimeMixer + 朴素持续性。
- **指标**：MAE、sMAPE(ϵ%)。
- **结果（Table 1）**：MAE 平均降 10%（基准 7.4%、疾病 12.6%）。样例 MAE：ETTh1 H=96 0.1941(vs PatchTST 0.2017)；ETTh2 H=720 0.3640(vs iTransformer 0.4565)；Weather H=96 0.0244；ILI-ENG H=7 1.6417(vs Crossformer 1.8698)；ILI-US2 H=7 0.4122。长程稳定；个别长程点（如 Weather H=720 vs DLinear 0.0352）为次优。
- **消融/效率**：第 4 节声明提供，但细节在前 12 页之外（据后续页/附录，提取缓存未覆盖，待核）。

## 7. 这篇论文真正有价值的地方
1.  把 CV 可变形注意力迁移到时序，感受野从固定网格变为内容驱动采样。
2.  V-DAB/T-DAB 解耦两个依赖维度，且在插值方式、头数、CNN 维度上有意区分。
3.  强调输入表示（NAE 相关性重排+分组嵌入），可迁移到其他时序模型。
4.  评估上不仅刷基准，还自评基准恰当性、构造更难的疾病任务。

## 8. 局限与问题
1.  DAB 的偏移 CNN + 插值带来额外开销；前 12 页未给参数量/FLOPs/速度（在后续页/附录，提取缓存未覆盖，待核）。
2.  对 NAE 重排与 `G` 等超参可能敏感。
3.  公开基准仅 3 个；作者亦在 A.5 批评常用基准不恰当。
4.  DAB 内部可解释性未深入。
5.  复现需依赖代码与附录（多个自定义模块与超参）。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + Table 1。
- **复现**：精读 §3 + Figure 1（Segment/Adapt 操作），查附录 A/C/D 与源码。
- **借鉴创新点**：复用偏移生成 `Δp=α·tanh(θ_off(Q))` 与形变插值，迁移 V/T-DAB。
- **写 related work**：归入"Transformer 时序预测""显式变量间依赖 MTS""可变形/动态注意力（Deformable DETR）"。

## 10. 和其他论文的关系
- **直接对比/竞争**：PatchTST [[PatchTST]], iTransformer [[iTransformer]], Crossformer [[Crossformer]], DLinear [[DLinear]], TimeMixer [[TimeMixer]], LightTS [[LightTS]]。
- **方法启发来源**：Deformable DETR / 可变形卷积（CV 的可变形注意力 [5]），标准 Transformer [[Transformer]] [41]。
- **同一脉络**：MTS 预测 / 改进 Transformer 时序应用的工作（如 Autoformer [[Autoformer]], FEDformer [[FEDformer]]）。

## 11. 关键词
多变量时间序列预测、可变形注意力、V-DAB/T-DAB、变量间依赖、邻域感知输入嵌入(NAE)、偏移采样、外生变量、传染病(ILI)预测、基准恰当性、编码器-2层GRU解码器、自适应感受野。

## 12. 可信度说明
本精读基于 PDF 提取文本的**前 12 页**：覆盖摘要、引言、任务定义（§2）、方法全貌（§3.1–3.6，含全部核心公式）以及 Table 1 主结果数表（大部分数值可直接核对）。这部分文本清晰、逻辑连贯。**未覆盖**的内容包括：消融实验与效率分析（参数量/FLOPs/速度）的具体结果、附录 A（数据与评估设置）、C（实现/超参/变量排序）、D（分季完整结果）等——相关结论已在文中标注"据后续页/附录，提取缓存未覆盖，待核"。原笔记缺失第二作者 Vasileios Lampos、代码链接、目标变量（油温/湿球温度）与数据分辨率等细节，本次据提取文本补正。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/DAB.txt` (本次复核仅含前 12/29 页可读文本; 原 AI 主体 12/29 + 全文补读 13-29 记录见下); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。本次优化据前 12 页提取文本核对并补正第二作者、目标变量、分辨率、样例数值等。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-29; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-29。
- **提取情况**: 缺失页 17 页, 其中 17 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Supplementary Materials
- p.13: A Data sets for time series forecasting
- p.13: This section offers a detailed description of the data sets used in our experiments to assess the
- p.13: experiments to match the setup in related methods that we compare to). The temporal resolution
- p.13: England (in the United Kingdom) and two US HHS Regions, specifically Region 2 (states of New
- p.14: It should be noted that for RCGP, Monday determines the start of a week, while for CDC this is
- p.14: 2019. However, we note that not all search queries are used as exogenous variables in our forecasting
- p.14: Given that for the US, we can only obtain data at the state level (as opposed to regional), we use a
- p.15: Days020406080ILI rate (per 100K people)Test
- p.15: Train
- p.15: ValidationFigure A1: An example of how the training, validation, and test sets are constructed when the test influenza
- p.15: In this step, we compute the linear correlation between the remaining search queries and the target

### 缺失页关键摘录

- p.14: Training, validation, and test sets. We assess the accuracy of forecasters across the last 4influenza
- p.15: these time points are determined, they become the 30th point in a 60-day validation period. Figure A1
- p.15: A.5 Criticism of data sets used to benchmark forecasting methods
- p.16: forecasting. It captures a negligible portion of meteorological data and, as a result, derived forecasting
- p.16: Hence, using this data set for training and evaluating a forecasting model may, unfortunately, result
- p.16: hourly sampled data set has better accuracy compared to the quarter-hourly sampled data set even at
- p.16: generally provide good accuracy at approximately a 2weeks ahead forecasting horizon [ 31,33].
- p.16: that, in the aforementioned ILI rate benchmark, there were forecasting horizons of 24or60weeks
- p.16: ahead (i.e. even more than a year!). Of course, the accuracy of the forecasting models under these
- p.16: England or the US. The evaluation process is rigorous, i.e. across 4consecutive influenza seasons as
- p.17: each variable, leading to a sub-optimal performance in our empirical evaluation.
- p.18: Table D1: ILI rate forecasting accuracy results in England (ILI-ENG) using web search frequency time series as
<!-- AI_READING_NOTE_END -->
