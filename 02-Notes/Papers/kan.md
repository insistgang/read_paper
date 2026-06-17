---
title: "KAN: Kolmogorov–Arnold Networks"
authors:
  - "Ziming Liu"
  - "Yixuan Wang"
  - "Sachin Vaidya"
  - "Fabian Ruehle"
  - "James Halverson"
  - "Marin Soljacic"
  - "Thomas Y. Hou"
  - "Max Tegmark"
year: 2024
venue: "arXiv preprint (arXiv:2404.19756, Preprint. Under review)"
doi: 
pdf: [[kan.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
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
extract_cache: .paper-cache/extracts/kan.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/50 pages"
---
# KAN: Kolmogorov–Arnold Networks

## 基本信息
- **PDF**: [[kan.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | KAN: Kolmogorov–Arnold Networks |
| **作者** | Ziming Liu; Yixuan Wang; Sachin Vaidya; Fabian Ruehle; James Halverson; Marin Soljačić; Thomas Y. Hou; Max Tegmark |
| **机构** | MIT; Caltech; Northeastern University; NSF AI Institute (IAIFI) |
| **发表时间** | 2024 (arXiv v4, 16 Jun 2024) |
| **刊物/会议** | arXiv:2404.19756 (Preprint, Under review) |
| **DOI** | 未明确 (arXiv:2404.19756) |
| **代码** | https://github.com/KindXiaoming/pykan (`pip install pykan`) |

## 摘要

清理后的英文原摘要（修复了 PDF 提取造成的空格丢失与断词）：

> Inspired by the Kolmogorov-Arnold representation theorem, we propose Kolmogorov-Arnold Networks (KANs) as promising alternatives to Multi-Layer Perceptrons (MLPs). While MLPs have fixed activation functions on nodes ("neurons"), KANs have learnable activation functions on edges ("weights"). KANs have no linear weights at all — every weight parameter is replaced by a univariate function parametrized as a spline. We show that this seemingly simple change makes KANs outperform MLPs in terms of accuracy and interpretability, on small-scale AI + Science tasks. For accuracy, smaller KANs can achieve comparable or better accuracy than larger MLPs in function fitting tasks. Theoretically and empirically, KANs possess faster neural scaling laws than MLPs. For interpretability, KANs can be intuitively visualized and can easily interact with human users. Through two examples in mathematics and physics, KANs are shown to be useful "collaborators" helping scientists (re)discover mathematical and physical laws. In summary, KANs are promising alternatives for MLPs, opening opportunities for further improving today's deep learning models which rely heavily on MLPs.

中文翻译：

> 受 Kolmogorov-Arnold 表示定理启发，我们提出 Kolmogorov-Arnold 网络（KAN）作为多层感知机（MLP）的有潜力替代方案。MLP 在节点（"神经元"）上使用固定的激活函数，而 KAN 在边（"权重"）上使用可学习的激活函数。KAN 完全没有线性权重——每个权重参数都被替换为一个参数化为样条的单变量函数。我们证明，这一看似简单的改动使 KAN 在小规模 AI + 科学任务上，于准确率和可解释性两方面都超越 MLP。在准确率方面，更小的 KAN 在函数拟合任务上即可达到与更大 MLP 相当或更好的精度。理论与经验都表明，KAN 拥有比 MLP 更快的神经缩放律。在可解释性方面，KAN 可以被直观地可视化，并易于与人类用户交互。通过数学（纽结理论）和物理（安德森局域化）两个例子，KAN 被证明可作为有用的"合作者"，帮助科学家（重新）发现数学与物理定律。总之，KAN 是 MLP 的有潜力替代方案，为进一步改进当今高度依赖 MLP 的深度学习模型提供了机会。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：多层感知机（MLP，即全连接前馈网络）是当今深度学习模型的基础构件，因通用逼近定理保证其表达能力而成为逼近非线性函数的默认模型（p.2）。但作者质问："MLP 真是我们能构建的最好的非线性回归器吗？" MLP 有两个显著缺点：在 Transformer 等架构中，MLP 消耗了几乎全部非嵌入参数；且相对注意力层而言可解释性更差，通常需要事后分析工具（p.2）。
- **之前方法的问题**：作者将 KAN 定位为"样条 + MLP"的结合体，扬长避短（p.2）。样条在低维函数上精确、易于局部调整、可在不同分辨率间切换，但有严重的维度诅咒（COD）——因为无法利用组合结构；MLP 凭借特征学习较少受 COD 影响，但因无法很好地优化单变量函数，在低维上不如样条精确。换言之，要准确学习一个函数，模型既要学到组合结构（外部自由度），又要逼近好单变量函数（内部自由度）。
- **历史包袱**：用 Kolmogorov-Arnold 表示定理建神经网络早有人尝试（文献 [9]-[16]），但多数停留在原始的"深度 2、宽度 2n+1"表示，且未能用上反向传播等现代技术（p.2）。Kolmogorov-Arnold 定理本身曾被认为"理论上成立但实际无用"，因为其分解出的 1D 函数可能非光滑甚至分形、难以学习，几乎被机器学习界判了"死刑"（p.4，引 [19][20]）。
- **核心矛盾与作者立场**：作者持更乐观态度，理由有二——(1) 不必拘泥于原始两层表示，可推广到任意宽度和深度；(2) 科学与日常中的多数函数往往光滑且具稀疏组合结构，可能存在光滑的 Kolmogorov-Arnold 表示（这与物理学家"更关心典型情形而非最坏情形"的思路一致，p.4）。

## 关键贡献

1.  **将 Kolmogorov-Arnold 表示推广为深层网络**：原始定理对应"深度 2、宽度 2n+1"的浅层表示，作者通过定义"KAN 层"（1D 函数矩阵）并堆叠，将其推广到**任意宽度和深度**，在现代深度学习语境下复活了这一经典定理（p.2，p.5）。
2.  **提出 KAN 架构**：核心是把**可学习的激活函数（参数化为 B 样条）放在边（权重）上**，节点只做求和，完全没有线性权重矩阵（p.2-6）。每个权重参数被一个可学习的 1D 函数替代。
3.  **展示准确率优势与更快的缩放律**：更小的 KAN 在函数拟合上即可达到与更大 MLP 相当或更好的精度；理论上 KAN 的缩放指数为 α=k+1（三次样条 k=3 时 α=4），是文中对比各理论里最大的，且经验上能在图 2.3 中接近饱和此速率（p.8）。
4.  **提供逼近理论保证（定理 2.1，KAT）**：若目标函数存在各 Φ 都 (k+1) 次连续可微的 KAN 表示，则存在 k 阶 B 样条使逼近误差以 G^(−k−1+m) 的速率收敛，**残差率与维度无关，从而克服维度诅咒**（p.7-8）。
5.  **提出两项实用技术**：**网格扩展（grid extension）** 逐步细化样条网格以提升精度（第 2.4 节，图 2.3 的"阶梯式"loss 下降）；**简化技术（simplification）** 使 KAN 可解释（第 2.5 节）。
6.  **AI + Science 实证**：用数学（纽结理论）和物理（安德森局域化）两个例子展示 KAN 作为科学发现"合作者"的潜力（p.2，第 4 节；相关章节在提取缓存中被截断，据原文目录）。

## 方法

- **整体框架**：KAN 是全连接前馈网络，灵感来自 Kolmogorov-Arnold 表示定理（公式 2.1）：对有界域上的光滑函数 f:[0,1]ⁿ→R，有 `f(x) = Σ_{q=1}^{2n+1} Φ_q( Σ_{p=1}^{n} ϕ_{q,p}(x_p) )`，其中 `ϕ_{q,p}:[0,1]→R`、`Φ_q:R→R` 都是单变量函数（p.3-4）。"唯一真正的多元函数是加法"。
- **从浅层定理到深层网络的关键洞见**：原始定理只对应两层 KAN，没有现成的"深层版定理"。作者借助 MLP 与 KAN 的类比——MLP 定义一层（线性变换+非线性）后即可堆叠，于是先回答"什么是 KAN 层？"：一个 `n_in→n_out` 的 KAN 层就是 1D 函数矩阵 `Φ={ϕ_{q,p}}`（公式 2.2）。Kolmogorov-Arnold 表示恰是内层 `[n→2n+1]` 与外层 `[2n+1→1]` 两个 KAN 层的复合；"更深的表示"就是堆叠更多 KAN 层（p.5）。
- **关键模块与数学机制**：
    - **KAN 层与前向传播**：网络形状记为整数数组 `[n_0, n_1, ..., n_L]`（公式 2.3）。连接 (l,i) 与 (l+1,j) 的激活函数记为 `ϕ_{l,j,i}`；后激活 `x̃_{l,j,i}=ϕ_{l,j,i}(x_{l,i})`；下一层神经元值是所有入边后激活之和：`x_{l+1,j} = Σ_{i=1}^{n_l} ϕ_{l,j,i}(x_{l,i})`（公式 2.5）。矩阵形式 `x_{l+1}=Φ_l x_l`（公式 2.6）。整网是 `KAN(x) = (Φ_{L-1}∘...∘Φ_1∘Φ_0)x`（公式 2.7）。
    - **激活函数参数化（残差形式）**：每条边的函数 `ϕ(x) = w_b·b(x) + w_s·spline(x)`（公式 2.10），其中基函数 `b(x)=silu(x)=x/(1+e^{-x})`（公式 2.11），`spline(x)=Σ_i c_i B_i(x)` 是 B 样条基的线性组合、系数 `c_i` 可训练（公式 2.12）。`w_b, w_s` 原则上冗余（可被吸收进 b、spline），但仍保留为可训练量以控制激活函数整体幅度（p.6）。
    - **初始化**：每个激活函数初始化为 `w_s=1` 且 `spline(x)≈0`（通过 `c_i∼N(0,σ²)`、小 σ，文中典型 σ=0.1）；`w_b` 用 Xavier 初始化（p.6，脚注 2）。
    - **样条网格在线更新**：样条定义在有界区间上，而训练中激活值可能跑出固定区间，故按输入激活值动态更新每个网格（p.6，脚注 3 还提到两种备选：网格可学习、或对输入做归一化——作者试过归一化但效果更差）。
    - **参数量**：深度 L、各层等宽 N、k 阶样条（通常 k=3）在 G 个区间（G+1 个网格点）上，总参数量 `O(N²L(G+k)) ~ O(N²LG)`；同深宽 MLP 仅需 `O(N²L)`，看似 MLP 更省（p.6-7）。但 KAN 通常用更小的 N 即可，反而省参数、泛化更好、更易解释。1D 问题取 N=L=1 时，KAN 退化为纯样条逼近。
    - **与 MLP 对比**：`MLP(x)=(W_{L-1}∘σ∘...∘W_0)x`（公式 2.9）把线性变换 W 与固定非线性 σ 分开；KAN 把二者统一进函数矩阵 Φ（公式 2.7）。
- **训练方式**：所有操作可微，KAN 用**反向传播**端到端训练（p.6）。
- **逼近理论与缩放律**：定理 2.1（KAT）给出与维度无关的逼近误差界 `‖f − (Φ^G_{L-1}∘...∘Φ^G_0)x‖_{C^m} ≤ C·G^{-k-1+m}`（公式 2.15），其中 C^m 范数度量到 m 阶导数（p.7）。m=0 时恢复 L∞ 精度并给出 RMSE 的缩放指数 k+1。作者将自己的缩放律 α=k+1 与他人理论对比（p.8）：Sharma & Kaplan 给 α=(k+1)/d（受 COD 影响）；Michaud 等给 α=(k+1)/2（二元运算最大 arity d*=2）；Poggio 等给 α=m/2。KAN 取 k=3 得 α=4，是其中最大者，且能经验达到，而既有工作报告 MLP 甚至难以饱和更慢的界（如 α=1）就早早 plateau。

## 实验

> 注：提取缓存仅覆盖到 p.8（截断于第 8 页泛化误差讨论处）。以下"数据集/对比/结果"主要据 p.1-8 可见内容；涉及第 3-4 章完整实验（15 个特殊函数、Pareto frontier、PDE、纽结理论、安德森局域化）的部分据原文后续页线索，提取缓存未覆盖，待核。

- **使用的数据/任务**：
    - **玩具函数拟合**：核心示例 `f(x,y)=exp(sin(x)+y²)`（图 2.3）。引言还给出高维示例 `f(x_1,...,x_N)=exp((1/N)Σ sin²(x_i))`（公式 1.1）用以说明样条因 COD 失败、MLP 逼近 exp/sin 低效、而 KAN 两者兼得（p.2）。
    - **据原文后续页（提取缓存未覆盖，待核）**：第 3 章在五个玩具例子（图 3.1）上比较 KAN 与不同深度 MLP；收集 **15 个数学物理中常见的特殊函数**（Table 1），在 (参数量, RMSE) 平面画 Pareto frontier（图 3.2），并求解泊松方程示例（PDE）。
- **对比方法**：主要与 MLP（不同深度，图 3.1 含 depth 2-5）对比（p.2，p.8）。
- **评价指标**：测试 **RMSE**（图 2.3 纵轴），以及参数量（复杂度）。
- **主实验结果（图 2.3，p.8 可见）**：拟合 `f(x,y)=exp(sin(x)+y²)`，对 [2,5,1] 和 [2,1,1] 两个 KAN 做网格扩展。训练动态呈"**阶梯状**"——每次网格扩展（grid=3,5,10,20,50,100,200,500,1000）后 loss 骤降然后 plateau；测试 RMSE 随网格 G 的缩放接近 `~ G^{-4}`（对照线给出 G^{-2}、G^{-3}、G^{-4}），与三次样条理论 k+1=4 相符；训练时间随 G 增长温和（图 2.3 右下）。文中存在"插值阈值（interpolation threshold）"——当网格点数接近训练样本数时行为转变。
- **缩放律对比（p.8）**：KAN 经验上能接近饱和 α=4 的最快缩放律，而既有工作报告 MLP 难以饱和更慢的界且很快 plateau。
- **效率信息**：参数量 KAN `O(N²LG)` vs MLP `O(N²L)`，但 KAN 常以更小 N 取胜（p.6-7）。

## 局限

- **计算成本**：每个 MLP 权重在 KAN 中变成一条样条函数，参数量带额外的网格因子 G（`O(N²LG)`）。虽常可用更小 N 弥补，但当需要极大网格或网络很宽/深时，开销可能仍高于 MLP；作者亦坦言 KAN 训练比 MLP 慢（p.6-7）。
- **假设依赖**：理论优势（克服 COD）建立在"目标函数存在足够光滑的 Kolmogorov-Arnold 表示、各 Φ 至少 (k+1) 次连续可微"之上（定理 2.1 前提，p.7）。原始两层表示的 1D 函数可能非光滑甚至分形（p.4），此时需靠加深/加宽换取光滑表示，并非自动成立；常数 C 仍依赖维度（p.8，作者将其留作未来工作）。
- **实验规模**：优越性主要在"小规模 AI + Science 任务"上验证（摘要，p.2）。在大规模、通用任务（如 ImageNet、大规模语言建模）上的表现未在本文涉及。
- **优化复杂性**：样条参数化、残差激活、网格在线更新、初始化方差 σ 等机制使优化比标准 MLP 更繁琐；k 取太高会过度振荡导致优化困难（p.8）。
- **复现敏感性**：σ（默认 0.1）、网格更新策略、w_b/w_s 等超参对性能可能敏感；好在已开源 pykan。

## 个人评论

> （以下为 AI 阅读判断，非论文原文）

这篇论文最值得学习的，是它把一个**曾被判"死刑"的经典数学定理**（Kolmogorov-Arnold 表示定理）重新激活，并转化为带现代深度学习特性（任意宽深、反向传播、残差激活、网格自适应）的实用框架。它提供了一个干净的"对偶视角"：MLP 是"外层 MLP + 固定激活"，KAN 是"外层 MLP + 内层样条"——把外部自由度（组合结构）和内部自由度（单变量函数逼近）分别交给最擅长的工具。这种"在边上学函数、在节点上只求和"的设计，提示我们神经网络架构未必要局限于"线性变换 + 固定激活"的范式。

更有方法论价值的是它的论证闭环：先用对偶视角讲清楚 KAN 为何兼具样条与 MLP 的长处，再给逼近定理（与维度无关的残差率）+ 缩放律推导（α=k+1=4），最后用 `f=exp(sin(x)+y²)` 的阶梯式 loss 曲线把理论指数 G^{-4} 落到实证。把"准确率 + 可解释性 + 理论保证"三者捏在一起的研究范式，对做可信 AI / AI for Science 的研究者很有参考意义。

需要保持的清醒：KAN 的优势强绑定于"存在光滑稀疏组合结构"这一前提，在缺乏此结构或大规模视觉/语言任务上是否仍成立，本文未给答案；工程上它比 MLP 更慢、超参更敏感。它更像是一把"在小规模科学回归/符号回归上锋利"的专用刀，而非 MLP 的即插即用通用替代品。

### 使用建议

- **如果快速了解**：读**摘要 + 引言 + 图 0.1**，即可抓住 KAN 的核心思想（边上可学激活、节点求和）、动机和与 MLP 的关键区别。
- **如果复现**：精读**第 2.2 节**实现细节（残差激活公式 2.10-2.12、`w_s=1`/`spline≈0`/Xavier 初始化、网格在线更新），结合开源代码 `https://github.com/KindXiaoming/pykan`（`pip install pykan`）。
- **如果借鉴创新点**：学习"把可学习函数放到边上"的核心设计与"网格扩展"逐步提精度的思路；思考能否将"边激活"嵌入 CNN/Transformer 的某个模块。
- **如果写 Related Work**：可归入"MLP 替代架构""可解释神经网络""基于样条的神经网络""科学机器学习 / AI for Science"。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于机器学习/深度学习的**基础网络架构**研究，不是某个具体视觉任务或注意力模块的工作。它要解决的是当今深度学习基石——多层感知机（MLP）的两个痛点：在 Transformer 等架构中 MLP 占据几乎全部非嵌入参数、且相对注意力层可解释性差（p.2）。论文提出 **Kolmogorov-Arnold Networks (KAN)** 作为 MLP 的有潜力替代架构，核心创新是把可学习的单变量样条函数放到网络的**边**上而非节点上。该研究最贴切的主题是"通用/其他"而非任何具体 CV 主题，因为它是一篇通用架构论文，实证场景集中在小规模 AI + Science（函数拟合、PDE 求解、纽结理论、安德森局域化）。

## 2. 一句话总结
KAN 把网络的每个线性权重替换为一个参数化为 B 样条的可学习单变量函数（激活放在"边"上、节点只求和），由此在小规模 AI + Science 任务上以更小的模型获得比 MLP 更高的精度、更快的缩放律和更好的可解释性。

## 3. 背景与问题
- **为什么要做**：MLP 是逼近非线性函数的默认模型，其表达能力由通用逼近定理保证（p.2）。但作者质疑"MLP 是否是最好的非线性回归器"，并指出两个缺点：Transformer 中 MLP 消耗几乎全部非嵌入参数；相对注意力层可解释性差、需事后分析工具（p.2）。
- **之前方法的问题**：样条在低维精确、易局部调整、可切换分辨率，但有严重 COD（无法利用组合结构）；MLP 靠特征学习较少受 COD 影响，但低维上不如样条精确（无法优化单变量函数）。准确学习一个函数需同时学好组合结构（外部自由度）与单变量函数（内部自由度），二者此前由不同模型分别擅长（p.2）。此外，用 Kolmogorov-Arnold 定理建网早有尝试，但多停在两层 2n+1 表示、未用反向传播，且该定理因 1D 子函数可能非光滑/分形被认为"实用无用"（p.2,4）。
- **核心矛盾**：如何设计一个既能像 MLP 那样学组合结构、又能像样条那样精确优化单变量函数、同时更易可视化与人机交互的网络。作者的乐观立场：(1) 推广到任意宽深；(2) 现实函数多光滑且有稀疏组合结构，可能存在光滑的 KA 表示（p.4）。

## 4. 核心贡献
1.  **推广 KA 表示为深层 KAN**：定义"KAN 层"（1D 函数矩阵），把原始两层表示堆叠成任意宽深的网络（p.5）。
2.  **KAN 架构**：边上放可学习 B 样条激活、节点只求和、无线性权重矩阵（公式 2.5-2.7）。
3.  **准确率与更快缩放律**：更小 KAN ≥ 更大 MLP 的精度；缩放指数 α=k+1（k=3 时 α=4），文中对比里最大（p.8）。
4.  **逼近理论（定理 2.1, KAT）**：存在光滑 KA 表示时，逼近误差以 G^{−k−1+m} 收敛、残差率与维度无关，克服维度诅咒（p.7）。
5.  **两项实用技术**：网格扩展（提精度）、简化（提可解释性）（第 2.4-2.5 节）。
6.  **AI + Science 实证**：纽结理论 + 安德森局域化两例展示 KAN 作为科学发现"合作者"（p.2，第 4 章；提取缓存未覆盖，待核）。

## 5. 方法详解
- **理论基础**：Kolmogorov-Arnold 表示定理（公式 2.1）：`f(x)=Σ_{q=1}^{2n+1} Φ_q(Σ_{p=1}^{n} ϕ_{q,p}(x_p))`，把多元连续函数分解为有限个单变量函数与加法的复合（p.3-4）。
- **KAN 层与前向**：形状 `[n_0,...,n_L]`（公式 2.3）；下一层神经元 = 所有入边后激活之和 `x_{l+1,j}=Σ_i ϕ_{l,j,i}(x_{l,i})`（公式 2.5）；整网 `KAN(x)=(Φ_{L-1}∘...∘Φ_0)x`（公式 2.7）。原始 KA 表示 = 形状 `[n,2n+1,1]` 的两层 KAN。
- **激活参数化（残差形式）**：`ϕ(x)=w_b·b(x)+w_s·spline(x)`（公式 2.10），`b(x)=silu(x)`（公式 2.11），`spline(x)=Σ_i c_i B_i(x)` 系数可训练（公式 2.12）；`w_b,w_s` 控制幅度。
- **训练细节**：可微 → 反向传播；初始化 `w_s=1`、`spline≈0`（`c_i∼N(0,σ²)`，σ≈0.1）、`w_b` 用 Xavier；样条网格按输入激活在线更新（p.6，脚注 2-3）。
- **参数量**：KAN `O(N²LG)` vs MLP `O(N²L)`，但 KAN 常用更小 N（p.6-7）；1D 时 N=L=1 退化为纯样条。
- **逼近与缩放**：定理 2.1 给 `‖f−(Φ^G_{L-1}∘...∘Φ^G_0)x‖_{C^m}≤C·G^{-k-1+m}`（公式 2.15）；α=k+1，与 Sharma-Kaplan `(k+1)/d`、Michaud `(k+1)/2`、Poggio `m/2` 对比，KAN 的 α 最大（p.7-8）。KAT 与 UAT 的区别在于 KAN 利用了函数的内在低维表示而 MLP 不能（p.8）。

## 6. 实验与结果
> 提取缓存覆盖到 p.8（截断于第 8 页泛化误差讨论）。第 3-4 章完整实验据原文后续页线索补充，标注"待核"。
- **任务/数据**：玩具函数拟合 `f(x,y)=exp(sin(x)+y²)`（图 2.3）；引言高维示例 `exp((1/N)Σsin²(x_i))`（公式 1.1）。**据原文后续页（缓存未覆盖，待核）**：图 3.1 五个玩具例子对比不同深度 MLP；Table 1 收集 15 个数学物理特殊函数、画 (参数量, RMSE) Pareto frontier（图 3.2）；泊松方程 PDE 示例。
- **对比方法**：不同深度 MLP（depth 2-5，图 3.1）。
- **指标**：测试 RMSE、参数量。
- **主结果（图 2.3, p.8）**：网格扩展使 loss 呈阶梯式骤降；测试 RMSE 随网格 `~ G^{-4}`，符合三次样条理论 k+1=4；训练时间随 G 增长温和。KAN 经验上接近饱和 α=4 最快缩放律，而 MLP 难以饱和更慢的界即 plateau（p.8）。
- **效率**：参数量带 G 因子，但 KAN 以更小 N 取胜并改善泛化（p.6-7）。

## 7. 这篇论文真正有价值的地方
价值在于把"理论上成立但被认为实用无用"的 Kolmogorov-Arnold 定理，通过推广到任意宽深 + 反向传播 + 残差样条激活 + 网格自适应，落地为可训练的现代架构。它给出一个干净的对偶视角：MLP 把"线性变换 + 固定激活"分开，KAN 把二者统一进函数矩阵 Φ，且"外层像 MLP（学组合结构）、内层像样条（优化单变量函数）"。这种"边上学可解释函数、节点只求和"的设计，加上"逼近定理 + 缩放律 + 实证阶梯曲线"三层论证闭环，对架构创新与 AI for Science 都有启发。

## 8. 局限与问题
- **计算成本/速度**：参数量含 G 因子（`O(N²LG)`），KAN 训练比 MLP 慢；极大网格或宽深网络时开销可能高于 MLP（p.6-7）。
- **假设依赖**：克服 COD 依赖"存在足够光滑（各 Φ 至少 k+1 次可微）的 KA 表示"，原始两层表示的子函数可能非光滑/分形（p.4,7）；常数 C 仍依赖维度（留作未来工作，p.8）。
- **实验规模**：仅小规模 AI + Science 验证，大规模/通用任务（ImageNet、大模型）未涉及（摘要）。
- **优化复杂性**：样条 + 残差激活 + 网格更新 + σ 等机制使优化更繁琐；k 太高会过度振荡（p.8）。
- **复现敏感性**：σ、网格更新策略等超参敏感（已开源 pykan）。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + 图 0.1，抓住"边激活 + 节点求和"与对 MLP 的对偶。
- **复现**：精读第 2.2 节实现细节（公式 2.10-2.12、初始化、网格更新）+ pykan 代码。
- **借鉴创新点**：把可学习函数放边上的设计 + 网格扩展；思考嵌入 CNN/Transformer 模块的可能。
- **写 Related Work**：归入 MLP 替代架构 / 可解释神经网络 / 样条神经网络 / AI for Science。

## 10. 和其他论文的关系
- **[[多层感知机（MLP）]]**：KAN 作为其直接替代品提出，二者通过 UAT vs KAT、`W,σ` 分离 vs `Φ` 统一形成对照。
- **[[Kolmogorov-Arnold表示定理]]**：KAN 的理论基础（公式 2.1）。
- **[[样条理论]]**：B 样条参数化边上激活，逼近界引经典 1D B 样条理论（文献 [23]）。
- **[[通用逼近定理]]**：MLP 的理论基础，本文专门对比 KAT 与 UAT（p.8）。
- **[[神经缩放律]]**：本文将 α=k+1 与 Sharma-Kaplan、Michaud、Poggio 等理论对比（p.8）。
- **[[Transformer]]**：MLP 是 Transformer 中消耗参数的主要部分，KAN 是潜在替换方向（p.2）。
- **[[AI for Science]]**：KAN 被用于（重新）发现数学（纽结理论）与物理（安德森局域化）定律（p.2）。

## 11. 关键词
KAN, Kolmogorov-Arnold Networks, Kolmogorov-Arnold 表示定理, B 样条, 边上激活, 残差激活函数, SiLU, 网格扩展, 神经缩放律 (α=k+1), 逼近定理 KAT, 维度诅咒, 可解释性, MLP 替代, AI for Science。

## 12. 可信度说明
本笔记基于 PDF 提取缓存（覆盖 p.1-8 的实质内容：摘要、引言、第 2.1-2.3 节架构与逼近理论、图 2.3 缩放律，截断于第 8 页泛化误差讨论）。摘要、动机、KAN 架构、残差激活公式（2.10-2.12）、参数量、定理 2.1 与缩放律对比均有原文直接支撑，可信度高。涉及第 3 章完整缩放实验（15 个特殊函数、Pareto frontier、五例对比）、第 4 章可解释性与科学发现（纽结理论、安德森局域化）、第 5-6 章相关工作与结论的细节，提取缓存未覆盖，已据原文目录/后续页线索标注"待核"，未编造具体数值。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 2086 字符/页); 来源缓存: `.paper-cache/extracts/kan.txt` (缓存仅含 12/50 页, 截断于 p.8 实质内容; 原 AI 主体 12/50 + 全文补读线索 13-50); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-50; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-50。
- **提取情况**: 缺失页 38 页, 其中 38 页提取到可读文本。缺失页包含正文/附录内容, 其中约 7 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: In case the user has no domain knowledge or no idea which symbolic functions these activation
- p.13: In contrast, KANs do continuous search (with gradient descent) in function space, so their results
- p.13: 3 KANs are accurate
- p.13: In this section, we demonstrate that KANs are more effective at representing functions than MLPs
- p.14: Number of parameters107
- p.14: KAN (depth 2)
- p.14: MLP (depth 2)
- p.14: MLP (depth 3)
- p.14: MLP (depth 4)
- p.14: MLP (depth 5)
- p.14: Theory (KAN)
- p.14: Theory (ID)

### 缺失页关键摘录

- p.13: compare both their accuracy (loss) and their complexity (number of parameters). We will show that
- p.14: Theory (ID)Figure 3.1: Compare KANs to MLPs on five toy examples. KANs can almost saturate the fastest scaling law
- p.14: (3)f(x, y) =xy. We know from Figure 4.1 that it can be exactly represented by a [2,2,1]KAN.
- p.14: a function of the number of parameters for KANs and MLPs in Figure 3.1, showing that KANs have
- p.15: Pareto Frontiers than MLPs. The definitions of these special functions are in Table 1.
- p.15: We collect 15 special functions common in math and physics, summarized in Table 1. We choose
- p.15: For each dataset and each model family (KANs or MLPs), we plot the Pareto frontier5, in the
- p.15: (number of parameters, RMSE) plane, shown in Figure 3.2. KANs’ performance is shown to be
- p.15: discovered KANs for special functions in Table 1. On one hand, it is interesting to interpret what
- p.15: these compact representations mean mathematically (we include the KAN illustrations in Figure F.1
- p.15: breaking down a high-dimensional lookup table into several 1D lookup tables, which can potentially
- p.16: Given the structure of the dataset, we may construct KANs by hand, but we are not sure if they are
<!-- AI_READING_NOTE_END -->
