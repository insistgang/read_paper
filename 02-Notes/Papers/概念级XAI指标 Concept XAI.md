---
title: "Concept-Based Explainable Artificial Intelligence: Metrics and Benchmarks"
authors:
  - "Halil Ibrahim Aysel"
  - "Xiaohao Cai"
  - "Adam Prugel-Bennett"
year: 2025
venue: "arXiv"
doi: 
pdf: [[概念级XAI指标 Concept XAI.pdf]]
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
extract_cache: .paper-cache/extracts/概念级XAI指标 Concept XAI.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# Concept-Based Explainable Artificial Intelligence: Metrics and Benchmarks

## 基本信息
- **PDF**: [[概念级XAI指标 Concept XAI.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Concept-Based Explainable Artificial Intelligence: Metrics and Benchmarks |
| **作者** | Halil Ibrahim Aysel; Xiaohao Cai; Adam Prugel-Bennett (University of Southampton) |
| **发表时间** | 2025 (arXiv:2501.19271v1, 31 Jan 2025) |
| **刊物/会议** | arXiv (cs.AI) |
| **DOI / arXiv** | arXiv:2501.19271 |

## 摘要

清理后的英文原摘要(据 PDF 提取文本整理, 修复空格/连字符、剔除杂入的图轴字符):

> Concept-based explanation methods, such as concept bottleneck models (CBMs), aim to improve the interpretability of machine learning models by linking their decisions to human-understandable concepts, under the critical assumption that such concepts can be accurately attributed to the network's feature space. However, this foundational assumption has not been rigorously validated, mainly because the field lacks standardised metrics and benchmarks to assess the existence and spatial alignment of such concepts. To address this, we propose three metrics: the concept global importance metric, the concept existence metric, and the concept location metric, including a technique for visualising concept activations, i.e., concept activation mapping. We benchmark post-hoc CBMs to illustrate their capabilities and challenges. Through qualitative and quantitative experiments, we demonstrate that, in many cases, even the most important concepts determined by post-hoc CBMs are not present in input images; moreover, when they are present, their saliency maps fail to align with the expected regions by either activating across an entire object or misidentifying relevant concept-specific regions. We analyse the root causes of these limitations, such as the natural correlation of concepts. Our findings underscore the need for more careful application of concept-based explanation techniques especially in settings where spatial interpretability is critical.

中文翻译:

> 基于概念的解释方法(如概念瓶颈模型 CBMs)通过把模型决策与人类可理解的概念关联起来来提升可解释性, 其前提是一个关键假设: 这些概念能被准确地归因到网络的特征空间。然而这一根本假设从未被严格验证, 主要原因是该领域缺乏标准化的指标与基准来评估这些概念的"存在性"与"空间对齐性"。为此, 我们提出三个指标——概念全局重要性指标(CGIM)、概念存在性指标(CEM)、概念位置指标(CLM), 并配套一种可视化概念激活的技术, 即概念激活映射(CoAM)。我们以后验概念瓶颈模型(post-hoc CBMs)为基准对象来展示其能力与挑战。通过定性与定量实验, 我们证明: 在许多情况下, 即便是后验 CBMs 判定为最重要的概念, 也并不存在于输入图像中; 而即使概念确实存在, 其显著性图也往往无法对齐预期区域——要么在整个物体上弥散激活, 要么错误识别出概念专属区域。我们进一步分析了这些缺陷的根源, 例如概念之间的自然相关性。我们的发现强调: 在空间可解释性至关重要的场景下, 应用基于概念的解释技术需要更加谨慎。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 基于概念的 XAI 方法(以概念瓶颈模型 CBMs 为代表)旨在把模型决策与人类可理解的概念绑定, 从而提升可解释性。这类方法隐含一个关键假设——这些概念能被准确地归因到网络的特征空间。
- **之前方法的问题**: 这个关键假设从未被严格验证, 根本原因是该领域缺乏标准化的指标与基准, 无法系统评估"被判为重要的概念到底是否存在于图像中"以及"模型关注的区域是否对应该概念的真实位置"。
- **核心矛盾**: 概念解释方法承诺给出人类可理解的解释, 但人们无法判断这些"解释性概念"是否真在输入图像里, 也无法判断激活区域是否落在正确位置。论文用提出的指标实测后发现, 这种对齐"出乎意料地差"(surprisingly poor), 这正是引入新指标的必要性所在。

## 关键贡献

(据引言末尾明确列出的三条贡献, 并补充论文实际给出的发现)

1. 提出**概念激活映射 (CoAM)** 框架: 用对应概念向量 (CAV) 对**预-GAP 特征图**做加权, 可视化输入图像中与某概念对应的激活区域。
2. 提出**三个定量指标**:
   - **CGIM (概念全局重要性指标)**: 检验 XAI 方法给出的全局概念重要性是否对齐真值。
   - **CEM (概念存在性指标)**: 检验被判为重要的概念是否真的存在于该图像中。
   - **CLM (概念位置指标)**: 检验被判为重要的概念在空间上是否与人类标注的概念位置对齐。
3. 以 **CUB-200-2011** 鸟类细粒度分类数据集构建基准, 用上述指标系统评估 **post-hoc CBMs (Yuksekgonul et al., 2023)**, 并讨论其优势与局限。
4. (实验发现) 后验 CBMs 即使在被认为最重要的概念上, 也经常**无法在输入图像中找到该概念**; 即使概念存在, 显著性图也常常**无法正确对齐**——要么在整个物体上弥散激活, 要么错误识别区域。
5. 分析这些缺陷的根本原因, 例如**概念之间的自然相关性** (natural correlation of concepts)。

## 方法

- **整体框架**: 评估流程分"全局评估"与"局部评估"两部分(图 1 下半部分)。先用 CoAM 生成概念激活图, 在此基础上计算三个指标。图 1 上半部分给出了 CAVs、传统 CBMs、post-hoc CBMs 的统一刻画: 特征提取器 a⃝ + 分类头 e⃝ 是传统(无瓶颈)分类模型; a⃝+b⃝+d⃝+e⃝ 是传统 CBMs; a⃝+c⃝+d⃝+e⃝ 是 post-hoc CBMs; 本文提出的 CoAM 是 f⃝。
- **形式化设定 (Preliminary)**: 训练集 `S = {(X_i, u_i, y_i, Λ_i, P_i)}`, 其中 `u_i ∈ {0,1}^L` 是 L 维概念标签向量, `y_i` 是 K 类的 one-hot, `Λ_i` 是图像 `X_i` 中被激活概念的索引集合, `P_i = {p_i1,…,p_iL}` 是各概念中心像素坐标。`f: X → R^d` 是任意已训练 DNN(如 ResNet/VGG)。`f(X_i)` 是**后-GAP**特征(GAP 层之后); `E_i ∈ R^{H×W×d}` 是**预-GAP**特征图(GAP 层之前, 保留空间信息)。
- **CAVs 构建**: 对每个概念 j, 取含该概念的正样本嵌入集 `N_pos_j` 与随机选取的负样本嵌入集 `N_neg_j`, 训练 SVM, 取分离超平面的法向量为该概念的 CAV `c_j ∈ R^d`; L 个 CAV 堆成概念库 `C = (c_1,…,c_L)^⊤ ∈ R^{L×d}`。post-hoc CBMs 的概念值由投影 `ˆu_i = C f(X_i) ∈ R^L` 直接得到(无需概念标签)。
- **传统 vs post-hoc CBMs (关键差异)**: 传统 CBMs 有概念真值标签 `u_i`, 用二元交叉熵损失 `L_g = Σ_i L_g(ˆu_i, u_i)` 训练概念预测块 g; post-hoc CBMs 没有 `u_i`, 直接令 `g(f(X_i)) = C f(X_i)`。两者最终都接一个单层分类器 `h(ˆu_i) = θ^⊤ ˆu_i + b` (`θ ∈ R^{L×K}`), 用类别交叉熵 `L_h` 训练。
- **关键模块**:
  1. **CoAM (公式 2)**: 第 j 个概念的激活图 `F_ij = (1/d) Σ_{k=1}^d c_jk · E_i(:,:,k) ∈ R^{H×W}`, 即用第 j 个 CAV 对预-GAP 特征图逐通道加权求和。再上采样回原图尺寸 `¯F_ij` 并叠加到 `X_i` 上做可视化与定位评估(伪代码见附录 Algorithm 1/2)。
  2. **CGIM (公式 3-8)**: 全局重要性分 `θ_jk` 是分类器把概念 j 映射到类 k 的权重; 真值是标注者给的概念-类别矩阵 `V ∈ R^{L×K}` (取值 0~1)。因 θ 与 V 量纲不同, 不直接比对单元素, 而是用**余弦相似度** ϕ 比较整行向量。三个变体: CGIM1 比 `θ(j,:)` 与 `V(j,:)`; CGIM2 比平均概念矩阵 `ˆU*(j,:)` 与 `V(j,:)`; CGIM3 比 `ˆU*_θ = θ ⊙ ˆU*` (逐点相乘) 与 `V(j,:)`。可按概念(逐 j)或按类别(逐 k, 公式 6-8)计算。理想情况下分数接近 1。
  3. **CEM (公式 9-10)**: 先定义**局部重要性分** `θ_jk · ˆu_ij` (论文明确指出: 不能仅凭瓶颈层概念值 `ˆu_ij` 的大小判断重要性, 因为 θ 会放大/缩小其影响)。据此对 L 个概念降序排名得 `q_i`, CEM `ρ_CEM_l = (1/l) Σ_{j=1}^l 1_{Λ_i}(q_ij)` 检查前 l 个重要概念中有多少真在 `Λ_i` 里, 是 0~1 的准确率。
  4. **CLM (公式 11)**: 在 CEM 之后, 对前 l 个重要概念检查其 CoAM 热图(上采样后用阈值 τ 二值化得区域 `Ω_ij`)是否**包含该概念的真值中心像素 `p_ij`**: `ρ_CLM_l = (1/l) Σ_{j=1}^l 1_{Ω_ij}(p_ij)`。论文说明: 严格做法应用每概念分割掩码算 IoU, 但缺乏分割真值, 故退而用中心像素坐标这一更易获得的标签。
- **训练与推理**: 本文**不训练新模型**, 是一个**事后评估框架**。它复用: 已训练的特征提取器 (ResNet-18), SVM 训练得到的概念库 C, 单层分类器 h(提供权重 θ)。推理时对每张测试图依次算 CGIM(全局)、CEM(局部存在)、CoAM+CLM(局部位置)。
- **与已有方法差异**: 本文不提新解释模型, 而是提出**系统性的评估方法学**, 填补概念解释领域缺乏定量评估工具的空白。

## 实验

- **使用数据集**: **Caltech-UCSD Birds (CUB-200-2011)**, 200 个类、112 个二元概念标签(如翅膀颜色、喙形状、羽毛图案), 约 11,800 张图像; 另提供 **12 个身体部位**的中心像素坐标, 用于 CLM 的概念定位评估。
- **被评估方法 / 复现设置**: 主要评估 **post-hoc CBMs (Yuksekgonul et al., 2023)**。按其设置用在 CUB 上训练的 **ResNet-18** 作特征提取器 f; 每个概念取约 **m≈100** 张正负样本图像训练 SVM 得 CAV; 训练单层分类器 h, 权重 `θ ∈ R^{112×200}`。复现细节在附录。
- **评价指标**: 本文提出的 CGIM、CEM、CLM(及其多个变体)。这是"被评估模型 × 评估指标"的关系, 而非不同模型横向对比。
- **主实验结果**:
  - **全局评估 (CGIM)**: 图 2 给出 CGIM 分数的直方图(分别按类别和按概念), 总体分数偏低、分布分散, 表明 post-hoc CBMs 的全局概念重要性与真值对齐很差。逐概念完整分数见 Table 6, 逐类别见 Table 7/8(附录)。
  - **局部评估 (CEM)**: 提取缓存在第 4.2 节中段截断, **CEM 的具体数值结果不在提取文本中**。原笔记给出的"前 3 概念平均 0.06~0.40"为(据原文后续页, 提取缓存未覆盖, 待核); 定性结论(被判最重要的概念常根本不在图像中)与摘要陈述一致。
  - **局部评估 (CLM)**: 同样, **CLM 的具体数值不在提取文本中**。原笔记给出的"0.15~0.51"为(据原文后续页, 提取缓存未覆盖, 待核); 定性结论(即使概念存在, 热图也常无法定位)与摘要一致。
- **消融 / 超参**: 提取文本未给出针对指标本身的消融。论文复现 post-hoc CBMs 时尝试了多种超参组合(如计算 CAV 的正负样本数 m), 但具体结果在截断之后, PDF 文本未明确。
- **泛化实验**: 提取文本未提到其他数据集, 实验集中于 CUB。
- **效率信息**: 提取文本未提及计算量/参数量/速度等效率指标; 评估重点是概念对齐质量。
- **概念-部位映射(据原文后续页 p.13-14, 提取缓存未覆盖, 据补读线索)**: 112 个概念按类型(颜色/图案/形状)归到身体部位, 例如 Beak 9 个、Wing 12 个、Tail 14 个等(Table 4/5)。

## 局限

1. **CLM 真值的简化**: CLM 用概念**中心像素点**作真值, 是一种简化。更严格的评估需要逐概念的像素级分割掩码(算 IoU), 但这类真值获取成本高、CUB 上不可得。阈值 τ 的取法也会影响 Ω_ij 进而影响 CLM。
2. **数据集单一**: 仅在 CUB 鸟类数据集上验证。该数据集的部件(喙、翅、尾)和颜色概念视觉上较局部、定义清晰; 对于更抽象(如"快乐")、更全局(如"风景")或定义模糊的概念, 方法的适用性有待验证。
3. **计算成本未讨论**: 需为每张图的每个概念生成热图, 但论文(就提取文本所见)未系统讨论该评估框架的计算开销。
4. **被评估对象有限**: 系统评估只覆盖 post-hoc CBMs, 未对传统 CBMs 或其他概念解释方法(如 TCAV)做同等系统的评估, 尽管指标本身是通用的。

## 个人评论

1. **补上了一块急需的拼图**: 概念解释方法这几年很热, 但"如何检验解释本身是否可靠"长期缺位。本文把这个问题拆成全局重要性、局部存在性、局部位置三个可量化维度, 是很务实的工具, 提醒研究者不能只看解释的"形式", 还要验证其"内容"是否成立。
2. **结论有分量也有反直觉性**: 用实验证据指出当前流行的 post-hoc CBMs 在概念对齐上有根本缺陷(连最重要的概念都常常不在图里), 这直接动摇了其可解释性的根基, 对推动更可靠的下一代方法有警示价值。
3. **抓住了空间可解释性**: CLM 把"解释要落在正确位置"这一在视觉任务里至关重要、却常被忽视的维度显式量化, 而不只给一个抽象标签。
4. **方法学定位清晰**: 它不卷新模型, 而是提供评估标尺, 这类工作长期看更可能成为领域基础设施。CoAM 这种"把 CAV 反投影回预-GAP 特征图"的可视化思路也简单可迁移。
5. **可改进处**: post-hoc CBMs 这一被评对象本身的复现质量(SVM 样本选择、阈值 τ)会显著影响结论, 若把"指标揭示的缺陷"全部归因于方法本身可能略激进; 更稳的叙事是"在该复现设置下对齐很差"。

### 使用建议

- **如果快速了解**: 读摘要 + 第 1 节引言(三个指标的直觉用"犀牛-角"的例子讲得很清楚) + 第 4.2 节及之后的实验小结。
- **如果复现**: 重点看第 3 节, 尤其 CoAM 公式 (2)、CEM 公式 (9)、CLM 公式 (11), 以及第 4 节/附录里 post-hoc CBMs 的复现设置(ResNet-18、CAV 的 SVM 训练、θ∈R^{112×200})。
- **如果借鉴创新点**: 学其评估思路——从"全局重要性 / 局部存在性 / 局部位置"三维构建评估体系; 以及 CoAM 这种用 CAV 加权预-GAP 特征图的可视化技术。
- **如果写 related work**: 归入"XAI 评估方法"或"概念可解释性(concept-based XAI)"综述, 作为提出评估指标/基准的代表作之一。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于可解释人工智能 (XAI) 方向, 聚焦**概念可解释性 (concept-based XAI) 的评估方法学**。核心问题: 如何系统地检验基于概念的解释方法(以概念瓶颈模型 CBMs / post-hoc CBMs 为代表)所判定的重要概念, 是否真实存在于输入图像中, 且其空间位置是否与人类预期一致。论文不提新解释模型, 而是提出三个指标 + 一种可视化技术, 并在 CUB 数据集上建基准。它本质是通用的 XAI 评估论文(arXiv 2025, Southampton 团队), 虽用鸟类数据做实验, 但与医学图像无关——因此真实主题应归在 `T_通用_NLP_其他`(无更贴切的具体 CV 主题), 而非原先误置的 `A2_医学图像_分类_配准_生成`。

## 2. 一句话总结
本文提出三个定量指标(概念全局重要性 CGIM、概念存在性 CEM、概念位置 CLM)和一个概念激活映射 (CoAM) 可视化框架, 用于评估基于概念的解释方法, 并在 CUB 上证明 post-hoc CBMs 在概念对齐上存在严重缺陷——最重要的概念常根本不在图里, 即使在也难以正确定位。

## 3. 背景与问题
- **为什么要做**: 概念解释方法把决策绑到人类可理解的概念上, 隐含"概念能被准确归因到特征空间"这一关键假设。
- **之前方法的问题**: 该假设从未被严格验证, 因为缺乏标准化指标与基准来评估概念的存在性与空间对齐性。
- **核心矛盾**: 解释方法承诺人类可理解的解释, 但无法判断这些概念是否真在图里、激活区域是否正确。论文实测后发现对齐"出乎意料地差", 这正是引入新指标的动机。

## 4. 核心贡献
1. 提出 **CoAM**: 用 CAV 加权预-GAP 特征图, 可视化概念激活区域。
2. 提出**三个定量指标**: CGIM(全局对齐)、CEM(概念是否存在)、CLM(空间是否对齐)。
3. 用 **CUB-200-2011** 建基准, 系统评估 **post-hoc CBMs (Yuksekgonul et al., 2023)**, 讨论其优劣。
4. (发现) post-hoc CBMs 即便在最重要概念上也常找不到该概念; 即使存在, 显著性图也常弥散或错位。
5. 分析根因, 如**概念之间的自然相关性**。

## 5. 方法详解
- **整体框架**: 评估分全局 / 局部两部分(图 1)。图 1 同时统一刻画了 CAVs、传统 CBMs、post-hoc CBMs: a⃝(特征提取)+e⃝(分类头)是无瓶颈模型; a⃝+b⃝+d⃝+e⃝ 是传统 CBMs; a⃝+c⃝(CAVs)+d⃝+e⃝ 是 post-hoc CBMs; CoAM 是 f⃝。
- **形式化**: `S = {(X_i, u_i, y_i, Λ_i, P_i)}`; `u_i ∈ {0,1}^L` 概念标签, `Λ_i` 激活概念索引集, `P_i` 各概念中心像素坐标。`f(X_i)` 是后-GAP 特征, `E_i ∈ R^{H×W×d}` 是预-GAP 特征图(含空间信息)。
- **CAVs**: 每概念用约 m≈100 张正负样本图训练 SVM, 取超平面法向量为 CAV `c_j`; 概念库 `C ∈ R^{L×d}`。post-hoc 的概念值直接由 `ˆu_i = C f(X_i)` 投影得到。
- **传统 vs post-hoc**: 传统 CBMs 有概念真值, 用 BCE 损失 `L_g = Σ_i L_g(ˆu_i, u_i)` 训练概念预测块; post-hoc 无真值, 直接令 `g(f(X_i)) = C f(X_i)`。两者都接单层分类器 `h(ˆu_i) = θ^⊤ ˆu_i + b` (`θ ∈ R^{L×K}`), 用类别交叉熵训练。
- **CoAM (公式 2)**: `F_ij = (1/d) Σ_k c_jk · E_i(:,:,k)`, 即用第 j 个 CAV 逐通道加权预-GAP 特征图; 上采样到原图尺寸 `¯F_ij` 后叠加可视化。
- **CGIM (公式 3-8)**: θ 与真值矩阵 `V ∈ R^{L×K}`(0~1) 量纲不同, 故用**余弦相似度**比整行向量。三变体: CGIM1 比 `θ(j,:)` vs `V(j,:)`; CGIM2 用平均概念矩阵 `ˆU*`; CGIM3 用 `ˆU*_θ = θ ⊙ ˆU*`。可按概念或按类别计算。
- **CEM (公式 9)**: 局部重要性分 `θ_jk · ˆu_ij`(论文强调不能只看瓶颈层概念值 `ˆu_ij`, 因 θ 会改变其影响); 排名后检查前 l 个是否真在 `Λ_i` 中, 得 0~1 准确率。
- **CLM (公式 11)**: 对前 l 个重要概念, 检查 CoAM 热图阈值化得到的区域 `Ω_ij` 是否包含真值中心像素 `p_ij`。理想做法是用分割掩码算 IoU, 但缺真值, 故用中心点近似; 阈值 τ 决定 Ω_ij。
- **训练与推理**: 框架本身不训练新模型, 是事后评估, 复用已训特征提取器、SVM 概念库、单层分类器。
- **与已有差异**: 提供系统性的评估方法学, 而非新解释模型。

## 6. 实验与结果
- **数据集**: CUB-200-2011, 200 类、112 二元概念、约 11,800 图, 含 12 个身体部位中心像素坐标供 CLM 使用。
- **被评估对象 / 复现**: post-hoc CBMs (Yuksekgonul et al., 2023); ResNet-18 作 f, CAV 的 SVM 用约 m≈100 正负样本, 分类器权重 `θ ∈ R^{112×200}`。
- **评价指标**: 本文的 CGIM / CEM / CLM(及变体)。无横向模型对比。
- **结果**:
  - CGIM: 图 2 直方图显示分数普遍偏低、分布分散; 逐概念完整分数 Table 6, 逐类别 Table 7/8(均在附录)。
  - CEM / CLM: 提取缓存在 4.2 节中段截断, **具体数值不在提取文本中**。原笔记给出的 CEM≈0.06~0.40、CLM≈0.15~0.51 为(据原文后续页, 提取缓存未覆盖, 待核); 定性结论(最重要概念常不存在; 即使存在也难定位)与摘要一致。
- **消融 / 泛化 / 效率**: 提取文本未明确(均在截断之后或未涉及)。

## 7. 这篇论文真正有价值的地方
1. **补上评估缺位**: 在概念解释研究火热但评估缺失时, 提供了可量化的三维评估工具与基准, 提醒人们验证解释的"内容"而非仅"形式"。
2. **结论有冲击力**: 用证据指出 post-hoc CBMs 在概念对齐上有根本缺陷, 动摇其可解释性根基, 对推动更可靠方法有警示价值。
3. **凸显空间可解释性**: CLM 把"解释要落在正确位置"这一视觉任务关键维度显式量化。
4. **指明方向**: 后续应开发能**保证概念存在性与空间一致性**的方法, 而非仅用概念分类。

## 8. 局限与问题
1. **CLM 真值简化**: 用中心像素点而非分割掩码(IoU 不可得), 阈值 τ 也影响结果。
2. **数据集单一**: 仅 CUB; 概念较局部、定义清晰, 对抽象/全局/模糊概念适用性待验证。
3. **计算成本未讨论**: 逐图逐概念生成热图的开销, 提取文本未系统讨论。
4. **被评对象有限**: 只系统评估 post-hoc CBMs, 未覆盖传统 CBMs / TCAV 等, 尽管指标通用。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言(犀牛-角的例子讲清三个指标直觉) + 4.2 节及之后实验小结。
- **复现**: 第 3 节公式 (2)(9)(11) + 第 4 节/附录的 post-hoc CBMs 复现设置(ResNet-18、CAV 的 SVM、θ∈R^{112×200})。
- **借鉴创新点**: 三维评估体系 + CoAM 反投影可视化。
- **写 related work**: 归入"XAI 评估方法 / 概念可解释性", 作为提评估指标的代表作。

## 10. 和其他论文的关系
本文不是医学图像论文, 属于通用 XAI 评估方法学(故主题改为 `T_通用_NLP_其他`)。直接相关:
- [[Concept Bottleneck Models]] (Koh et al., 2020): 传统 CBMs, 本文刻画与评估的基础范式之一。
- [[TCAV / Concept Activation Vectors]] (Kim et al., 2018): CAV 的原始提出者, 本文的概念库与 CoAM 基于此。
- [[Post-hoc Concept Bottleneck Models]] (Yuksekgonul et al., 2023): 本文直接复现并系统评估的具体对象。
- Aysel et al. (2023): 第一作者前作(用类级而非图像级标注学概念), 引言中引用。
- 在医学影像等领域应用概念解释的工作: 可受益于本文的评估框架。

## 11. 关键词
可解释人工智能 (XAI), 概念可解释性, 概念瓶颈模型 (CBMs / post-hoc CBMs), 概念激活向量 (CAV), 评估指标, 概念激活映射 (CoAM), 概念存在性, 概念定位, 显著性对齐, CUB 数据集

## 12. 可信度说明
本精读基于 **PDF 提取文本(前 12 页, 截断于第 4.2 节中段)** 生成。提取文本清晰, 完整覆盖了摘要、引言、Preliminary、第 3 节方法(CoAM/CGIM/CEM/CLM 全部公式)与第 4 节实验设置。
**需注意的局限**: 提取文本在 **4.2 节中段截断**, 因此 CGIM 的逐概念/逐类别完整表(Table 6/7/8)、CEM 与 CLM 的具体数值、后续讨论与结论**未包含在提取文本中**。原笔记中涉及的具体数字(CEM≈0.06~0.40、CLM≈0.15~0.51)无法据提取文本核实, 已就地标注"(据原文后续页, 提取缓存未覆盖, 待核)"。另外, **frontmatter 原 year=2017 有误**——PDF 明确为 arXiv:2501.19271v1, 31 Jan 2025, 已据真值改为 2025。**原 primary_topic=A2_医学图像** 与论文内容串台, 已改为 `T_通用_NLP_其他`。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 2086 字符/页); 来源缓存: `.paper-cache/extracts/概念级XAI指标 Concept XAI.txt` (提取 12/17 页, 4.2 节中段截断; 全文补读线索覆盖 p.13-17 章节标题与表名); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。本轮重读修正: 摘要重建(原为乱码直提)、year 2017→2025、primary_topic A2_医学图像→T_通用_NLP_其他、CEM/CLM 数字标注为"提取缓存未覆盖待核"、补足方法形式化细节。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Concept-Based Explainable Artificial Intelligence: Metrics and Benchmarks
- p.13: Input Concept-wise maps Class maps
- p.13: PartTypeColor Pattern Shape Total
- p.13: Beak 3 2 4 9
- p.13: Wing 6 4 2 12
- p.13: Tail 10 3 1 14
- p.13: Total 82 18 12 112
- p.14: PartTypeColor Pattern (length for beak) Shape
- p.14: Beak grey, black, buff same-as-head, shorter-than-head dagger, hooked-seabird, all-purpose, cone
- p.14: Wing brown, grey, yellow, black, white, buff solid, spotted, striped, multi-coloured rounded, pointed
- p.14: Tail brown, grey, black, white, buff solid, striped, multi-colored notched
- p.14: Algorithm 2 Feature Visualisation in CoAM

### 缺失页关键摘录

- p.13: D. Concept Localisation Evaluation – Figures and Tables
- p.13: Figure 4 presents some examples of class and concept visualisation by using our CoAM. The matching between the concept
- p.13: groups and the body parts for the CUB dataset is given in Tables 4 and 5.
- p.13: Figure 4. Class and concept visualisation with our CoAM. All images (on the left) are correctly classified and their class-wise saliency
- p.13: Table 4. The number of concepts, grouped based on their types, and mapped to the body parts (see Table 5 for more details).
- p.14: Table 5. Details of the concepts and the body parts they are mapped to.
- p.14: Figure 2 presents the histograms of the CGIM scores. The full list of CGIM scores for every concept and every class is
- p.14: presented below in Table 6 and in Tables 7 and 8, respectively.
- p.15: Table 6. Full list of CGIM scores for concepts in CUB dataset (Wah et al., 2011) with reproduced post-hoc CBMs (Yuksekgonul et al.,
- p.16: Table 7. Full list of CGIM scores for classes in CUB dataset (Wah et al., 2011) with reproduced post-hoc CBMs (Yuksekgonul et al., 2023).
- p.17: Table 8. Full list of CGIM scores for classes in CUB dataset (Wah et al., 2011) with reproduced post-hoc CBMs (Yuksekgonul et al., 2023)
<!-- AI_READING_NOTE_END -->
