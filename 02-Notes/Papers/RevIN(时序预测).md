---
title: "Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift"
authors:
  - "Taesung Kim"
  - "Jinhee Kim"
  - "Yunwon Tae"
  - "Cheonbok Park"
  - "Jang-Ho Choi"
  - "Jaegul Choo"
year: 2022
venue: "ICLR"
doi: 
pdf: [[RevIN(时序预测).pdf]]
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
extract_cache: .paper-cache/extracts/RevIN(时序预测).txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/25 pages"
---
# Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift

## 基本信息
- **PDF**: [[RevIN(时序预测).pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift |
| **作者** | Taesung Kim; Jinhee Kim; Yunwon Tae; Cheonbok Park; Jang-Ho Choi; Jaegul Choo (KAIST AI / VUNO / NAVER / ETRI) |
| **发表时间** | 2022 |
| **刊物/会议** | ICLR 2022 |
| **DOI** | 未明确 |

## 摘要

清理后的英文原摘要(修复空格/连字符断裂):

> Statistical properties such as mean and variance often change over time in time series, i.e., time-series data suffer from a distribution shift problem. This change in temporal distribution is one of the main challenges that prevent accurate time-series forecasting. To address this issue, we propose a simple yet effective normalization method called reversible instance normalization (RevIN), a generally-applicable normalization-and-denormalization method with learnable affine transformation. The proposed method is symmetrically structured to remove and restore the statistical information of a time-series instance, leading to significant performance improvements in time-series forecasting, as shown in Fig. 1. We demonstrate the effectiveness of RevIN via extensive quantitative and qualitative analyses on various real-world datasets, addressing the distribution shift problem.

中文翻译:

> 时间序列中的统计特性(如均值与方差)常随时间变化, 即时序数据存在**分布偏移**问题。这种时间维度上的分布变化, 是阻碍准确时序预测的主要挑战之一。为解决该问题, 我们提出一种简单而有效的归一化方法——**可逆实例归一化(RevIN)**, 它是一种带可学习仿射变换、可通用应用的"归一化-反归一化"方法。该方法采用对称结构, 在一处**移除**时序实例的统计信息、在另一处**恢复**之, 从而显著提升时序预测性能(见图1)。我们在多种真实世界数据集上通过广泛的定量与定性分析, 验证了 RevIN 对分布偏移问题的有效性。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：时间序列数据的统计特性(如均值、方差)常随时间变化, 即存在**分布偏移**问题。预测任务中, 训练集与测试集通常是按某个时间点切分的, 两者往往几乎不重叠, 这是模型性能退化的常见原因; 此外, 输入到模型的**不同输入序列之间**也可能具有不同的底层分布, 同样会显著拉低性能 (p.1)。
- **之前方法的问题**：
    1. 近期基于深度学习的时序预测模型(如 Informer, N-BEATS, SCINet)**忽视了归一化的重要性**, 仅对模型输入做简单的全局预处理, 而期望端到端模型自行替代归一化的作用, 缺乏进一步探索 (p.2)。
    2. 若直接对输入做实例归一化(去均值/方差), 虽能减小不同序列间的分布差异, 但同时**移除了对预测未来值可能很重要的非平稳信息(原始分布)**; 模型只能从归一化后的输入中重建原始分布, 因这一固有局限而损失预测性能 (p.1-2)。
    3. 领域适应(domain adaptation)与领域泛化(domain generalization)是缓解分布偏移的常见手段, 但二者都需要定义明确的"领域"; 而非平稳时序中数据分布随时间漂移, "领域"的定义并不直观。Adaptive RNNs (Du et al., 2021)虽针对该问题, 但**计算代价高** (p.2 Related Work)。
- **核心矛盾与洞察**：需要**归一化**输入以消除分布差异、降低预测难度, 但归一化又会**丢失**对预测重要的非平稳统计信息。作者的关键洞察是: 若把输入归一化时移除的信息**在输出层显式地还回去**(对输出做反归一化), 模型就既保留了归一化输入的好处, 又无需自行重建原始分布 (p.1-2)。

## 关键贡献

> 据 p.2 "In summary, our contributions are as follows" 三条贡献。

1. **提出 RevIN 方法**: 一种简单而有效的、对称结构的"归一化-反归一化"方法, 在一处移除、另一处恢复时序实例的统计信息; 可通用应用于任意深度神经网络, 且代价可忽略(negligible cost) (p.2)。
2. **达到 SOTA**: 将 RevIN 加到基线模型后, 在**七个大规模真实世界数据集**上以显著优势取得当时的最佳性能 (p.2)。
3. **充分的实验验证**: 通过定量分析与定性可视化, 验证 RevIN 在缓解分布偏移问题上的有效性 (p.2)。

(补充) 论文反复强调 RevIN 是**灵活、端到端可训练的层**, 可加在任意层、甚至中间层(p.5 提到附录 A.4 Table 7 验证了加在中间层的效果), 但最有效的位置是编码器-解码器结构的对称位置, 实践中即输入层与输出层。

## 方法

- **整体框架**: RevIN 由对称的归一化层与反归一化层组成, 实践中分别加在模型**输入层与输出层**(图2)。流程为: 输入序列 → RevIN 归一化 → 主模型预测 → RevIN 反归一化 → 最终预测。
- **输入输出与符号**: 输入序列 `x(i) ∈ R^{K×Tx}`, K 是变量数, Tx 是输入长度; 目标 `y(i) ∈ R^{K×Ty}`, Ty 是预测长度。因归一化/反归一化是在**时间维度**上做的, 故 Tx 与 Ty 可以不同 (p.3-4)。
- **关键模块**:
    1. **统计量(公式1)**: 对每个实例 `x(i)_k ∈ R^{Tx}` 沿时间维计算均值与方差:
        ```
        E_t[x_kt^(i)] = (1/Tx) Σ_{j=1..Tx} x_kj^(i)
        Var[x_kt^(i)] = (1/Tx) Σ_{j=1..Tx} ( x_kj^(i) − E_t[x_kt^(i)] )^2
        ```
    2. **实例归一化(公式2)**: 用上述统计量标准化, 并引入**可学习仿射参数向量** `γ, β ∈ R^K`:
        ```
        x̂_kt^(i) = γ_k * ( (x_kt^(i) − E_t[x_kt^(i)]) / sqrt(Var[x_kt^(i)] + ε) ) + β_k
        ```
        归一化后序列的均值/方差更一致, 非平稳信息被削弱, 模型在分布一致的输入下能更准确地预测序列内的局部动态 (p.4)。
    3. **反归一化(公式3)**: 对模型输出 `ỹ(i)` 施加公式2 的**逆变换**, 使用**完全相同的统计量与仿射参数**:
        ```
        ŷ_kt^(i) = sqrt(Var[x_kt^(i)] + ε) * ( (ỹ_kt^(i) − β_k) / γ_k ) + E_t[x_kt^(i)]
        ```
        其中 μ、σ 来自**输入序列**的统计量, γ、β 是与归一化层共享的可学习参数。最终预测是 `ŷ(i)` 而非 `ỹ(i)` (p.4)。
- **3.2 节直观解释(图3)**: 论文用 ETT/ECL 数据集 + SCINet 基线, 逐步可视化分布: (a) 原始输入中训练/测试分布几乎不重叠、且呈多峰(说明序列间分布差异大); (b) 归一化后变成均值居中、训练/测试分布重叠的单峰分布, 证实多峰来源于序列间分布差异; (c) 模型在对齐分布下输出; (d) 反归一化把输出还原回原始分布作为最终预测。作者将整个过程概括为"**先把问题变简单, 再还原回原始状态**", 而非直接在分布偏移下硬解难题 (p.5)。
- **训练方式**: 端到端。`γ, β` 与主模型参数一起反向传播更新 (p.2 提到仿射变换"widely accepted in recent deep-learning-based normalization work, Ulyanov et al., 2016")。
- **与已有方法差异**:
    1. 与传统全局预处理不同, RevIN 是**实例级**的, 每个序列用自身统计量。
    2. 与单纯实例归一化不同, RevIN 含**对称的反归一化步骤**, 显式恢复原始非平稳信息。
    3. 相比 Adaptive RNNs (Du et al., 2021), RevIN **更简单、代价低、模型无关**, 可轻易嵌入任何深度网络 (p.2)。
- **论文类型特化**: 本文是**时序预测方法论**研究。核心创新是一个通用的归一化/反归一化模块, 不修改注意力机制或网络架构, 因此可挂载到任何深度预测骨干上。

## 实验

- **数据集**: 主实验用**4 个**大规模真实数据集——ETTh1, ETTh2, ETTm1(电力变压器温度, 七维特征, 中国两地两年数据; ETTh 为小时级、ETTm1 为 15 分钟级), ECL(电力消耗, 321 个客户、小时级多变量) (p.6)。附录 A.1 另在 3 个数据集上给结果: air quality、Nasdaq(均取自 UCI)与 M4 竞赛数据集——合计 7 个数据集 (p.6, p.13 据全文补读)。
- **数据切分**: ETT 按前 12 个月/中间 4 个月/最后 4 个月做训练/验证/测试; ECL 用 15/3/4 个月 (p.6)。
- **预测长度**: 小时级数据集(ETTh1/ETTh2/ECL)设为 1d/2d/7d/14d/30d/40d; ETTm1 设为 6h/12h/3d/7d/14d。表中以步数计, 从 24 增到 960(ETT 系列最长 1344) (p.6, Table 1)。
- **对比方法**: 三个 SOTA 非自回归预测模型作基线——**Informer, N-BEATS, SCINet**; RevIN 作为模型无关模块叠加其上 (p.6)。
- **评价指标**: **MSE 与 MAE**, 均在 z-score 归一化数据上计算(沿用 Informer 的评测协议, 使不同变量同尺度) (p.6)。
- **主实验结果(Table 1, p.6)**: 对全部三个基线, 加 RevIN 后 MSE/MAE 在绝大多数设置上大幅下降。摘录(MSE):
    - ETTh1, 24 步: Informer 0.550→0.504; N-BEATS 0.478→0.330; SCINet 0.338→0.308。
    - ETTh2, 168 步: Informer 8.157→**0.859**; N-BEATS 7.174→**0.410**; SCINet 0.559→0.337(长预测下基线误差爆炸, RevIN 把误差压低数倍乃至一个数量级)。
    - ETTm1, 1344 步: N-BEATS 14.613→**0.631**(同样数量级修正)。
    - ECL, 24 步: Informer 0.250→0.148; N-BEATS 0.279→0.176; SCINet 0.138→0.112。
    - 结果为 5 次运行的平均误差; 完整结果(含标准差与基线原报告值)在附录 A.14 (p.6)。
- **长序列实验(Table 2)**: 论文还在固定输入长度、预测长度从 48 增到 960 的设定下分析长序列预测性能(具体数值在提取缓存截断处之后, 提取缓存未覆盖, 待核) (p.6)。
- **跨域实验(Table 5, 据原文 p.14, 提取缓存未覆盖, 待核)**: 用 ETT 不同子集互为源域/目标域做 cross-domain 评测, 显示即便分布差异大, RevIN 仍表现出色, 印证其缓解训练-测试分布差异的能力。
- **消融/中间层实验**: 论文称在附录 A.4 Table 7 验证了把 RevIN 加到**中间层**的效果 (p.5)。
- **超参敏感性 / 输入长度影响**: 据原文 p.14(图7、超参分析)讨论了输入序列长度对 RevIN 与基线的影响(提取缓存未覆盖, 待核)。
- **效率信息**: 文中称开销可"忽略不计"(negligible cost, p.2), 但提取文本未给出运行时间/参数量/FLOPs 的具体数值。

## 局限

- **统计代表性假设**: RevIN 用单个输入实例(每变量的整段序列)估计均值/方差, 隐含该序列统计量有意义。对**极短序列**或几乎无统计规律的序列, 估计可能不稳, 效果存疑(提取文本未直接讨论, 系据方法推断)。
- **输入/输出共享统计量假设**: 反归一化沿用输入序列的 μ、σ。若预测窗口内分布相对输入窗口发生根本性漂移(强非平稳), 这一"输入统计量也适用于输出"的假设可能不成立(提取文本未直接讨论, 系据公式3 推断)。
- **效率指标缺位**: 称代价可忽略, 但提取文本未给出具体速度/参数量/FLOPs 对比, 无法精确评估。
- **训练细节未在正文给出**: 仿射参数 γ、β 的初始化、与主模型训练的协调、超参等放在附录 A.11/A.12, 不在提取缓存覆盖范围内, 复现时需查附录。
- **复现风险**: 方法本身极简、复现门槛低; 主要不确定性来自附录中的训练/超参细节(提取缓存未覆盖)。

## 个人评论

> 以下为 AI 阅读后的评述。

这篇论文最值得学习的是其**问题抽象与解法的优雅**:
1. **问题抽象准确**: 把"预测不准"的一个关键来源精准地抽象为分布偏移, 并点出"归一化降难度"与"归一化丢信息"之间的核心矛盾, 为解法指明方向。
2. **解法优雅简洁**: 不去堆复杂网络模块, 而是从输入/输出变换的视角, 用一个**对称、可学习、即插即用**的层解决问题。这提示我们: 一个设计精巧的"外围"模块, 有时比改动核心网络更通用、更有效。RevIN 后续被时序预测社区广泛沿用, 正印证了这一点。
3. **方法论启发**: "**先把问题变简单, 再还原回原始状态**"具有普适性——遇到难题时, 先想能否通过输入输出变换把它转成模型更易处理的形式。
4. **论证严谨**: 在三种异构基线 × 多数据集上一致提升, 再配合分布可视化(图3)直观地说明"为什么有效", 这种"数值 + 机理可视化"双线论证值得借鉴。

一个值得追问的点: 论文把 γ、β 设为可学习, 但消融中"可学习仿射 vs 纯标准化(γ=1,β=0)"的增益拆分在正文未展开(可能在附录), 这是判断仿射项贡献度的关键。

### 使用建议

- **快速了解**: 读摘要、第1节引言、图2/图3、Table 1 即可掌握动机、方法与显著效果。
- **复现**: 精读第3节(公式1、2、3), 并查附录 A.11(训练细节/超参)与 A.12(基线复现细节)。
- **借鉴创新点**:
    1. 学习"对称归一化/反归一化"的模块思路, 迁移到其他有分布偏移的任务(如跨域分类、风格迁移)。
    2. 学习"可插拔层为整模型带来稳定提升"的设计哲学。
    3. 学习用分布可视化直观证明方法有效性。
- **写 related work**: 可归入(1)时序归一化方法;(2)处理分布偏移的深度学习方法(与领域适应/泛化并列);(3)时序预测的通用即插即用组件。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**时间序列预测**领域(ICLR 2022), 专注解决时序数据中普遍存在的**分布偏移(distribution shift)**问题。它提出**可逆实例归一化(RevIN)**——一个模型无关、即插即用的归一化层, 提升深度学习模型在非平稳时序上的预测准确性。原笔记将其归在 "R2_控制_生物启发_其他跨学科" 并不贴切: 本文与控制/生物启发无关, 是时序预测/分布适应方向的机器学习方法论。本仓库 taxonomy 无专门的时序条目, 故归入 **T_通用_NLP_其他**(通用序列/非 CV 的机器学习方法)。

## 2. 一句话总结
本文提出对称结构的"归一化-反归一化"层 RevIN: 在输入层用实例自身的均值/方差(配可学习仿射参数 γ、β)移除非平稳信息, 在输出层用相同统计量显式还原, 从而缓解训练/测试及序列间的分布偏移, 显著提升 Informer、N-BEATS、SCINet 等多种时序预测模型的精度。

## 3. 背景与问题
- **为什么要做**: 时序数据的均值/方差随时间变化, 训练集与测试集按时间点切分后几乎不重叠, 且不同输入序列底层分布也各异; 这种分布偏移是模型退化的主因之一 (p.1)。
- **之前方法的问题**:
    1. 现代深度预测模型(Informer/N-BEATS/SCINet)只做简单全局预处理, 忽视归一化, 指望端到端学习自行补偿, 探索不足 (p.2)。
    2. 直接做实例归一化会连带移除对预测重要的非平稳信息, 逼模型从归一化输入里重建原始分布, 反而损性能 (p.1-2)。
    3. 领域适应/泛化需明确"领域", 在分布随时间漂移的非平稳时序里不易定义; Adaptive RNNs 虽针对此但代价高 (p.2)。
- **核心矛盾与洞察**: 归一化降难度却丢信息——把丢掉的信息在输出层显式还回去(反归一化), 即可两全 (p.1-2)。

## 4. 核心贡献
1. 提出 RevIN——对称的"归一化-反归一化"层, 移除并恢复实例统计信息, 通用且代价可忽略 (p.2)。
2. 叠加到基线后, 在**七个**大规模真实数据集上以显著优势达到 SOTA (p.2)。
3. 用定量分析 + 定性可视化充分验证其对分布偏移的缓解作用 (p.2)。
4. (论文强调)RevIN 是端到端可训练的灵活层, 可加在任意/中间层(附录 A.4 Table 7), 但最优位置是编码器-解码器的对称端, 即输入/输出层 (p.5)。

## 5. 方法详解
- **整体框架**: 对称归一化层 + 反归一化层, 实践中挂在输入/输出层。流程: 输入 → 归一化 → 主模型 → 反归一化 → 最终预测 (p.4, 图2)。
- **符号**: `x(i) ∈ R^{K×Tx}`(K 变量数, Tx 输入长度), `y(i) ∈ R^{K×Ty}`; 因沿时间维归一/反归一, Tx 与 Ty 可不同 (p.3-4)。
- **统计量(公式1)**: 每个实例 `x_k^{(i)}` 沿时间求均值 `E_t[·]` 与方差 `Var[·]` (p.4)。
- **归一化(公式2)**: `x̂_kt = γ_k * (x_kt − μ_k)/sqrt(σ²_k + ε) + β_k`, γ、β ∈ R^K 为可学习仿射向量, ε 防除零 (p.4)。
- **反归一化(公式3)**: `ŷ_kt = sqrt(σ²_k + ε) * (ỹ_kt − β_k)/γ_k + μ_k`, 用与归一化**完全相同**的 μ、σ、γ、β; 最终预测取 `ŷ` 而非 `ỹ` (p.4)。
- **机理(3.2 节, 图3)**: 在 ETT/ECL + SCINet 上逐步可视化: 原始输入训练/测试分布不重叠且多峰 → 归一化后均值居中、重叠、单峰(证实多峰源于序列间差异) → 模型在对齐分布下输出 → 反归一化还原。一言以蔽之"先简化、再还原" (p.5)。
- **训练**: 端到端, γ、β 随主模型一起反向传播; 仿射变换沿用 Ulyanov et al. 2016 的实例归一化思路 (p.2)。
- **与他法差异**: 实例级(非全局); 含对称反归一化(非单纯实例归一化); 比 Adaptive RNNs 更简单、模型无关 (p.2)。

## 6. 实验与结果
- **数据集**: 主实验 4 个——ETTh1/ETTh2/ETTm1(电力变压器温度)、ECL(电力消耗, 321 客户); 附录 A.1 另加 air quality、Nasdaq、M4, 共 7 个 (p.6; Nasdaq/M4 据全文补读 p.13)。
- **切分**: ETT 12/4/4 月, ECL 15/3/4 月 (p.6)。
- **预测长度**: 小时级 1d~40d, ETTm1 6h~14d; 表中步数 24→960(ETT 最长 1344) (p.6)。
- **基线**: Informer、N-BEATS、SCINet(非自回归 SOTA), RevIN 叠加其上 (p.6)。
- **指标**: MSE、MAE(z-score 归一化数据上计算) (p.6)。
- **主结果(Table 1, p.6, 5 次平均, MSE 摘录)**:
    - ETTh1@24: Informer 0.550→0.504, N-BEATS 0.478→0.330, SCINet 0.338→0.308。
    - ETTh2@168: Informer 8.157→0.859, N-BEATS 7.174→0.410, SCINet 0.559→0.337。
    - ETTm1@1344: N-BEATS 14.613→0.631。
    - ECL@24: Informer 0.250→0.148, N-BEATS 0.279→0.176, SCINet 0.138→0.112。
    - 完整结果(标准差 + 基线原报告值)在附录 A.14。
    - 规律: 预测越长, 基线误差越易爆炸, RevIN 的相对修正越大(长预测下可达数倍至一个数量级)。
- **长序列(Table 2)**: 固定输入、预测 48→960(具体数值在提取缓存截断处之后, 待核) (p.6)。
- **跨域(Table 5)**: ETT 子集互为源/目标域, RevIN 在分布差异大时仍出色(据原文 p.14, 提取缓存未覆盖, 待核)。
- **消融/中间层**: 附录 A.4 Table 7 验证加在中间层有效 (p.5)。
- **效率**: 称 negligible cost, 但提取文本无具体数值 (p.2)。

## 7. 这篇论文真正有价值的地方
1. **问题抽象准确**: 把预测误差的一大来源精准定位到分布偏移, 并揭示"归一化降难度 vs 丢信息"的核心矛盾。
2. **解法优雅**: 用对称、可学习、即插即用的层, 而非复杂网络改造解决问题; 后被社区广泛沿用。
3. **方法论可迁移**: "先简化问题, 再恢复复杂性"——通过输入输出变换把难题转成易解形式。
4. **论证扎实**: 三异构基线 × 多数据集一致提升 + 分布可视化(图3)双线证明"有效且为何有效"。

## 8. 局限与问题
- **统计代表性假设**: 用单实例估均值/方差, 对极短/无规律序列可能不稳(系据方法推断, 提取文本未直接讨论)。
- **输入/输出共享统计量**: 反归一化沿用输入统计量, 强非平稳时该假设或失效(据公式3 推断)。
- **效率指标缺位**: 称代价可忽略, 但提取文本无 runtime/参数量/FLOPs 数据。
- **训练细节在附录**: γ、β 初始化、超参、基线复现细节在 A.11/A.12, 提取缓存未覆盖。
- **复现风险**: 方法极简、门槛低; 不确定性主要在附录细节。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言 + 图2/图3 + Table 1。
- **复现**: 精读第3节公式1/2/3 + 附录 A.11/A.12。
- **借鉴**: 对称归一化/反归一化思路迁移到跨域分类、风格迁移等分布偏移任务; 学其可插拔层设计与分布可视化论证。
- **写 related work**: 归入时序归一化 / 处理分布偏移的深度学习方法 / 时序预测通用组件。

## 10. 和其他论文的关系
- **基线模型**: [[Informer]]、[[N-BEATS]]、[[SCINet]](文中作为叠加 RevIN 的三个 SOTA 骨干)。
- **分布偏移相关**: 领域适应/泛化(Tzeng 2017、Ganin 2016 DANN 等)、Adaptive RNNs (Du et al., 2021, 文中对比)。
- **归一化谱系**: 实例归一化 (Ulyanov et al., 2016, RevIN 的仿射变换来源)。
（知识库未提供具体论文列表, 上述双链按概念给出, 可能为占位。）

## 11. 关键词
可逆实例归一化(RevIN), 时间序列预测, 分布偏移, 归一化与反归一化, 可学习仿射变换, 模型无关, 即插即用层, 非平稳时序, ETT 数据集, ECL 数据集, Informer, N-BEATS, SCINet, MSE, MAE

## 12. 可信度说明
本笔记的顶部各节与精读 1-6 节主要基于 PDF 提取文本 p.1-12(摘要、引言、相关工作、方法详述含公式1-3、实验设置、主结果 Table 1)生成, 这部分**完整可靠**。提取缓存头标注 `pages_extracted: 12/25` 且按 25000 字符截断, 故:
- **方法与主结果**(原理、公式、框架、Table 1 数值)描述完整准确。
- **核心动机、贡献、实验设置**准确。
- **信息缺口**: Table 2 长序列具体数值、Table 5 跨域、图6/图7、超参敏感性、附录(A.1/A.4/A.11/A.12/A.14)等位于提取缓存截断之后, 文中相关条目均已标注"据原文 p.13-14 / 提取缓存未覆盖, 待核"。效率(速度/参数量/FLOPs)文本未给出具体数值。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本 p.1-12, 约 2086 字符/页, 无明显乱码); 来源缓存: `.paper-cache/extracts/RevIN(时序预测).txt` (头标 12/25 页, 按 25000 字符截断; 原 AI 主体 12/25 + 全文补读记录引用了 p.13-25 线索); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。本轮重读已据提取文本重建摘要(原为乱码直提)、修正分类(R2→T_通用_NLP_其他)、补足实验数值并标注提取缓存未覆盖处。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-25; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-25。
- **提取情况**: 缺失页 13 页, 其中 13 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Published as a conference paper at ICLR 2022
- p.13: M45competition dataset consists of six different hourly, daily, weekly, monthly, quarterly, and
- p.13: Additionally, we conduct a qualitative analysis on the Nasdaq dataset to verify the effectiveness
- p.14: Train ETTh 1 ETTh 2 ETTm 1
- p.14: Test ETTh 2 ETTm 1 ETTh 1 ETTm 1 ETTh 1 ETTh 2
- p.14: Prediction length 336 960 336 960 336 960 336 960 288 1344 288 1344
- p.14: As RevIN can alleviate the distribution discrepancy between the training and test data, we investigate
- p.14: ETTh 2datasets are collected from different locations, and the ETTh and ETTm 1datasets have dif-
- p.14: In Table 5, despite the difference in the data distributions, RevIN shows remarkable performance in
- p.14: results demonstrate that RevIN successfully solves the distribution shift problem by alleviating data
- p.14: We analyze the hyperparameter sensitivity of the proposed method compared with the baseline mod-
- p.14: MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE

### 缺失页关键摘录

- p.13: Figure 6: Prediction results on the Nasdaq dataset. The results on three variables in the data,
- p.13: M45competition dataset consists of six different hourly, daily, weekly, monthly, quarterly, and
- p.13: competition (Makridakis et al., 2020). For evaluation, we measure the micro-averaged mean ab-
- p.13: As shown in Table 4, RevIN signiﬁcantly improves the forecasting performance of the baselines on
- p.13: all three datasets. Notably, RevIN shows outstanding performance on the Nasdaq dataset, reducing
- p.13: Additionally, we conduct a qualitative analysis on the Nasdaq dataset to verify the effectiveness
- p.13: distribution. As a result, even existing state-of-the-art models often cannot predict the future values
- p.14: Table 5: Cross-domain time-series forecasting results. We conduct a cross-domain evaluation on
- p.14: the data is collected. We use the ETT datasets for the experiment since they have the same feature
- p.14: ferent measurement time intervals. Thus, we alternately use each ETT dataset as a source domain
- p.14: In Table 5, despite the difference in the data distributions, RevIN shows remarkable performance in
- p.14: Figure 7: Impacts of the input sequence length on RevIN compared with the baselines. We
<!-- AI_READING_NOTE_END -->
