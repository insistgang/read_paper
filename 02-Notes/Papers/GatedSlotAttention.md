---
title: Gated Slot Attention for Efficient Linear-Time Sequence Modeling
authors:
  - "Yu Zhang"
  - "Songlin Yang"
  - "Ruijie Zhu"
  - "Yue Zhang"
  - "Leyang Cui"
  - "Yiqiao Wang"
  - "Bolun Wang"
  - "Freda Shi"
  - "Bailin Wang"
  - "Wei Bi"
  - "Peng Zhou"
  - "Guohong Fu"
year: 2024
venue: "arXiv (NeurIPS 2024)"
doi: 
pdf: [[GatedSlotAttention.pdf]]
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
extract_cache: .paper-cache/extracts/GatedSlotAttention.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/21 pages"
---
# Gated Slot Attention for Efficient Linear-Time Sequence Modeling

## 基本信息
- **PDF**: [[GatedSlotAttention.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Gated Slot Attention for Efficient Linear-Time Sequence Modeling |
| **作者** | Yu Zhang*; Songlin Yang*; Ruijie Zhu; Yue Zhang; Leyang Cui; Yiqiao Wang; Bolun Wang; Freda Shi; Bailin Wang; Wei Bi; Peng Zhou†; Guohong Fu† (*共同一作, †通讯; 苏州大学 / MIT / UCSC / 腾讯AI Lab / LuxiTech / 滑铁卢大学) |
| **发表时间** | 2024 (arXiv:2409.07146, 2024-09-11; 后被 NeurIPS 2024 接收) |
| **刊物/会议** | arXiv preprint (Under review 时提交) |
| **DOI** | 未明确 (arXiv:2409.07146) |
| **代码** | github.com/sustcsonglin/flash-linear-attention; 模型见 huggingface.co/fla-hub |

## 摘要

**清理后英文原文** (据 PDF 提取文本整理, 修复连写空格与连字符):

> Linear attention Transformers and their gated variants, celebrated for enabling parallel training and efficient recurrent inference, still fall short in recall-intensive tasks compared to traditional Transformers and demand significant resources for training from scratch. This paper introduces Gated Slot Attention (GSA), which enhances Attention with Bounded-memory-Control (ABC) by incorporating a gating mechanism inspired by Gated Linear Attention (GLA). Essentially, GSA comprises a two-layer GLA linked via softmax, utilizing context-aware memory reading and adaptive forgetting to improve memory capacity while maintaining compact recurrent state size. This design greatly enhances both training and inference efficiency through GLA's hardware-efficient training algorithm and reduced state size. Additionally, retaining the softmax operation is particularly beneficial in "finetuning pretrained Transformers to RNNs" (T2R) settings, reducing the need for extensive training from scratch. Extensive experiments confirm GSA's superior performance in scenarios requiring in-context recall and in T2R settings.

**中文翻译**:

> 线性注意力 Transformer 及其门控变体以支持并行训练和高效循环推理著称, 但在召回密集型 (recall-intensive) 任务上仍逊于传统 Transformer, 且从头训练需要大量资源。本文提出门控槽注意力 (Gated Slot Attention, GSA): 它在"有界内存控制注意力" (Attention with Bounded-memory-Control, ABC) 的基础上, 引入受门控线性注意力 (GLA) 启发的门控机制。本质上, GSA 由两层经 softmax 连接的 GLA 构成, 借助上下文感知的内存读取 (context-aware memory reading) 与自适应遗忘 (adaptive forgetting), 在保持紧凑循环状态尺寸的同时提升内存容量。该设计借助 GLA 的硬件高效训练算法和更小的状态尺寸, 大幅提升训练与推理效率。此外, 保留 softmax 操作在"将预训练 Transformer 微调为 RNN" (T2R) 设置中尤为有益, 减少了从头训练的需求。大量实验证实 GSA 在需要上下文召回的场景以及 T2R 设置下均表现优越。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 标准 Transformer 的 softmax 注意力 (SA) 强大但有二次复杂度, 对视频理解、生物序列等长序列建模构成瓶颈; 在语言建模 (序列长度适中) 中, 训练效率不是首要问题, 但**推理**时 KV cache 随生成长度线性增长, 带来显存负担和 I/O 吞吐瓶颈。
- **线性注意力的两大遗留问题** (原文 Introduction 明确列出): (i) **性能**: 近期研究表明线性循环模型在需要上下文检索/学习的任务上仍吃力, 且存在根本性的"召回-内存权衡" (recall-memory trade-off)——所有推理期常数内存的模型都受此约束; (ii) **训练效率**: 虽然线性注意力支持 FLA 实现的硬件高效分块训练, 但在万亿 token 上从头训练仍代价高昂。
- **T2R 范式与其缺陷**: "将预训练 Transformer 微调为 RNN" (T2R) 只需几十亿 token 微调 (约为从头训练总成本的 1–3%), 但线性注意力用的核函数与 softmax 不同, 把预训练的 softmax 注意力模型微调成线性注意力会产生性能落差。
- **为何回到 ABC**: 作者重新审视 ABC 模型, 因为它**保留了 softmax 操作**, 减小了标准注意力与线性注意力间的训练-微调差异, 天然适合 T2R; 且 ABC 状态利用更高效, 用更小状态即可达到相近性能, 有望扩展召回-内存权衡的帕累托前沿。ABC 此前未受重视, 原因是其语言建模性能平庸且训练慢。
- **核心矛盾**: 如何在保持/提升训练与推理效率 (线性复杂度、小状态) 的前提下, 大幅提升上下文召回能力, 并能有效复用已有的预训练 Transformer 权重。

## 关键贡献

1. **把 ABC 重写为"经 softmax 连接的两阶段线性注意力"**, 从而可直接套用 FLA 的硬件高效分块并行实现来加速训练 (解决 ABC 训练慢的问题)。
2. **提出 GSA 模型**: 识别 ABC 更新规则的两个缺陷, 引入受 GLA 启发的**数据相关标量门控** $\alpha_i$ (每个槽独立) 系统性解决, 即 ABC 的门控版本。
3. **诊断并修复 ABC 两大缺陷**: (i) 无遗忘机制 → 信息一旦写入内存槽便无限期保留, 阻碍槽位复用; (ii) 累积 softmax 写入规则给句首 token 过高写入强度 (首 token $\phi_1 = \mathbf{1}$, 写满所有槽), 与自然语言的近因偏置相悖。
4. **召回任务性能优越**: 在 MQAR 合成任务与多个真实世界召回/问答任务上, GSA 以远小于 RetNet/GLA 的状态尺寸, 显著超越所有线性基线。
5. **验证 T2R 中"保留 softmax"的重要性**: 将 Mistral-7B 微调为 GSA, 不仅超越 RWKV6-7B、Mamba-7B 等大循环模型, 也优于把 Mistral 微调成 RetNet/GLA 以及 SUPRA 等其他 T2R 方法。
6. **效率平衡**: GSA 训练吞吐与 GLA 相当, 又因状态更小获得推理加速。

## 方法

- **整体框架**: GSA 是即插即用的 token mixing 层, 替换标准 Transformer 的自注意力层。骨干沿用 Llama 架构, 堆叠 $L$ 个 GSA 块, 每块 = 一个 GSA token mixing 层 + 一个 GLU channel mixing 层 (图 2)。
- **多头与投影**: 对每个头 $h$, $q_i^h, k_i^h, v_i^h = \phi(W_q^h x_i), \phi(W_k^h x_i), \phi(W_v^h x_i)$, 其中 $\phi$ 为 Swish 激活。遗忘门 $\alpha_i^h = \sigma(W_\alpha^h x_i)^{1/\tau}$ (sigmoid + 阻尼因子 $\tau$, 实践取 $\tau=8$), 阻尼因子把门值往 1 靠, 对长程依赖建模关键。输出经 RMSNorm、Swish、Concat 后投影 $y_i = W_o(\cdot)$。
- **状态与更新规则 (公式 6)**: 维护键状态 $\widetilde{K}_t \in \mathbb{R}^{m\times d}$ 和值状态 $\widetilde{V}_t \in \mathbb{R}^{m\times d}$, $m$ 为槽位数 ($m \ll T$):
    $\widetilde{K}_t = \mathrm{Diag}(\alpha_t)\widetilde{K}_{t-1} + (1-\alpha_t)\otimes k_t$
    $\widetilde{V}_t = \mathrm{Diag}(\alpha_t)\widetilde{V}_{t-1} + (1-\alpha_t)\otimes v_t$
    $o_t = \widetilde{V}_t^{\top}\,\mathrm{softmax}(\widetilde{K}_t^{\top} q_t)$
    其中 $\alpha_t \in [0,1]^m$ 是数据相关遗忘门 (每槽一个标量), $(1-\alpha_t)$ 为写入门——两门通过 $k_t=1-\alpha_t$ 耦合, 与 HGRN2 同一思路。
- **两阶段 GLA 视角 (公式 7)**: GSA 可写成两次经 softmax 连接的 GLA:
    1. $\{o'_t\} = \mathrm{GLA}(q_t, k_t, 1-\alpha_t, \alpha_t, 1)$——第一阶段聚合历史键, 得到上下文感知的查询 $o'_t \in \mathbb{R}^m$;
    2. $\{o_t\} = \mathrm{GLA}(\mathrm{softmax}(o'_t), 1-\alpha_t, v_t, 1, \alpha_t)$——第二阶段用 softmax 增强的查询从值状态读取。
    据此可复用 GLA 的分块并行算法训练 (详细推导在原文 §A、§B)。
- **直观解释**: (i) 遗忘门 $\alpha$ 让模型主动清除过时信息、复用槽位 → 修复 ABC 缺陷一; 耦合写入门 $1-\alpha$ 引入近因偏置 → 修复缺陷二。(ii) 第一阶段线性注意力提供全局上下文查询, 使第二阶段 softmax 读取更精准。(iii) 第二阶段保留 softmax 缓解"注意力稀释" (attention dilution); 从 Hopfield 网络视角, softmax 可指数级放大有效记忆容量——故 ABC/GSA 即便实际状态小也可能隐含较大记忆容量。
- **参数预算**: $W_q,W_k,W_v,W_o$ 合计 $4d^2$, 与单个标准 softmax 注意力层相同; $W_\alpha$ 参数量 $dHm$, 通过设 $m=64$、$H=4$ 使 $Hm \ll d$, 总参数约 $4.125d^2$ (1.3B 模型 $d=2048$, 仅引入 $0.125d^2$ 额外开销)。
- **训练**: 采用 GLA 的分块并行算法; 反向传播时**重计算**循环状态 (recomputation, 同 FLA / Mamba2) 以降显存峰值, 代价是吞吐略降。
- **推理**: 展开为标准 RNN, 每步仅维护 $\widetilde{K}_t, \widetilde{V}_t$, 状态大小 $O(md)$, 与序列长度无关, 实现恒定内存/计算。
- **与已有方法对比**: 对 ABC——用数据相关门控替代累积 softmax 写入规则; 对 GLA——底层是两层 GLA 但中间经 softmax 连接, 保留检索能力 (标准 GLA 单阶段无 softmax); 对 RetNet——RetNet 用**数据无关**固定衰减 $\gamma$, GSA 的 $\alpha$ 是**数据相关**、选择性更强; 对标准 Transformer——状态从 $O(Td)$ 降到 $O(md)$, 复杂度从二次降为线性。

## 实验

- **语言建模设置**: 在 **Slimpajama** 语料子集上训练 **1.3B 与 2.7B** 两档模型, 各 **100B tokens** (1.3B: L=24, d=2048; 2.7B: L=32, d=2560)。对比 Xfmr++ (Llama 风格), Mamba, RetNet, GLA, HGRN2。指标: 困惑度 (PPL)、零样本准确率。
- **状态尺寸对比** (越小推理越快): GSA 与 HGRN2 同为 128×Ld, GLA 256×Ld, RetNet 512×Ld, Mamba 64×Ld。GSA 用一半于 GLA、四分之一于 RetNet 的状态。
- **常识推理 (表 1)**: 在 1.3B 与 2.7B 上, GSA 与最强线性模型 HGRN2 (同状态尺寸) 相当, 并在更小状态下优于 GLA 和 RetNet。例: 1.3B Lambada PPL——GSA 12.6 / HGRN2 11.8 / GLA 15.4 / RetNet 15.4 / Mamba 16.5 / Xfmr++ 15.3; 平均准确率 GSA 51.7、HGRN2 51.9、GLA 50.4、RetNet 50.6、Xfmr++ 50.5。注: 这些任务序列短、不真正考察上下文检索能力。
- **上下文召回——MQAR (图 3a/表 3a)**: 采用最难设置 (序列长 512、64 个 KV 对)。GSA 准确率随模型维度增加稳步提升, 显著优于其他线性模型; Xfmr++ 标准注意力近乎满分故省略。
- **上下文召回——真实任务 (表 3b)**: 信息检索 FDA、SWDE (从 HTML/PDF 抓取的段落) + 问答 SQuAD、NQ、TriviaQA、Drop, 输入截断到 2K token。
    - 1.3B 平均分: Xfmr++ **36.9** (最佳, 符合预期) > GSA **31.8** > GLA 31.4 > RetNet 28.4 > Mamba 27.7 > HGRN2 25.9。GSA 在所有线性基线中平均最优。
    - 2.7B 平均分: Xfmr++ 41.7 > GSA **36.5** > GLA 34.3 > RetNet 31.0 > Mamba 30.5 > HGRN2 29.5。
    - 优势归因: GSA 的上下文感知读取 + 遗忘 (门控) 机制, 使其更有效地操纵有限大小的内存。
- **消融 (表 2, 340M 模型 / 10B Slimpajama tokens, PPL↓)**:
    1. **门控机制**: GSA (64 槽) 13.51 → 去掉衰减退化回 ABC 升到 **16.94**; 改用数据无关衰减为 15.83 → 数据相关门控贡献最大。
    2. **非线性 (第一阶段后)**: 去掉 softmax 升到 14.03; 换 Swish 13.71 / ReLU 13.69 / ReLU² 13.95——softmax 优于其他非线性。
    3. **槽位数**: 32 槽 13.74 / 64 槽 13.51 / 128 槽 13.46。128 槽 PPL 略低, 但因吞吐显著下降, 最终选 64 槽作性能-效率平衡点。
- **效率 (图 4, 1.3B, 单卡 H800)**:
    - **训练吞吐 (图 4a)**: 固定每 batch 16K tokens 时, GSA (开重计算) 吞吐与 GLA 相当, 略低于 Xfmr++; 槽数 32/64/128 对应 46.7K / 44.1K / 37.1K tokens/s。尽管走两次 GLA, 凭更小状态 GSA 仍能维持与 GLA 相当的吞吐。
    - **显存 (图 4b)**: GSA 37.4 GiB (开重计算后 35.9), 低于 Mamba 38.0、Xfmr++ 41.4, 但**略高于** GLA 36.2 (注: 原笔记称"低于 GLA"有误, 已据图 4b 数值更正)。
    - **推理延迟 (图 4c)**: 推理为内存受限, 速度与状态尺寸强相关; GSA 状态比 RetNet/GLA 小, 推理更快 (具体延迟数值在提取文本中仅有定性描述)。
- **T2R 实验 (§4.2)**: 把预训练 Mistral-7B 微调成 GSA, 超越 RWKV6-7B、Mamba-7B 等大循环模型, 也优于微调成 RetNet/GLA 及 SUPRA, 印证保留 softmax 的价值。(该节完整数值表落在提取缓存未完整覆盖的后续页, 待核。)

## 局限

1. **极长序列未验证**: 实验序列长度最长约 16K (训练吞吐基准) / 召回任务截断到 2K; 百万级 token 下固定槽位能否承载信息尚未可知。
2. **固定槽位假设**: 槽位数 $m$ 固定, 可能限制其在"信息量随序列长度线性增长"任务中的表现。
3. **因果建模**: GSA 为因果 (自回归) 设计, 不直接适用于需要双向上下文的非因果任务 (如 BERT 式编码)。
4. **从头训练优势有限**: GSA 优势在 T2R 设置最突出; 从零训练时在常识推理任务上与 HGRN2 等接近, 区分度不大 (论文亦坦承这些短任务不充分反映检索能力)。
5. **两阶段计算开销**: 虽是线性复杂度, 但走两次 GLA, 实际计算量可能高于单阶段 GLA 或 Mamba (论文用更小状态弥补吞吐)。
6. **强依赖 FLA 库**: 高效训练依赖作者的 FlashLinearAttention 库; 代码已开源但引入外部依赖。

## 个人评论

1. **核心洞察**: 为受限记忆模型 (ABC) 引入**数据相关门控**, 是平衡效率 (小状态) 与能力 (强召回) 的关键。这个"给固定容量内存加遗忘门"的思路可推广到其他状态空间/循环模型。
2. **设计哲学**: 把复杂操作分解为已知、硬件高效的原语 (GLA) 的组合, 再用形式化分析 (两阶段 GLA) 指导设计——既复用现成 kernel 拿到工程红利, 又让创新点可解释。这种"站在 FLA 肩膀上"的做法很实用。
3. **T2R 实践指南**: 明确验证微调预训练 Transformer 为 RNN 时**保留 softmax**能大幅减少性能损失。给后续 T2R 方法的启示是: 应尽量保持与 softmax 注意力结构的相似性, 而非彻底换核。
4. **"小状态, 大能力"范式**: GSA 用一半于 GLA、四分之一于 RetNet 的状态在召回任务上更好, 对内存受限部署 (长上下文推理) 很有吸引力。需注意其优势主要体现在**推理延迟**而非训练显存 (显存上 GSA 略高于 GLA)。
5. **一个值得追问的点**: 召回任务上 GSA (31.8) 与 GLA (31.4) 在 1.3B 上差距其实不大, 真正拉开是与 Mamba/HGRN2; 与 softmax 的 Xfmr++ (36.9) 仍有明显鸿沟——召回-内存权衡的根本限制并未被打破, 只是帕累托前沿被推进了一步。

### 使用建议

- **快速了解**: 读 Abstract、Introduction (§1)、Method (§3.1-3.3) 和 Experiments (§4.1.2 召回 / §4.1.3 消融) 的结论。
- **复现**: 重点读 Method (§3.2、§3.3) 与附录 §A、§B (算法伪代码 Algorithm 1 "Hardware-Efficient GSA"、超参数), 必须结合 FlashLinearAttention (FLA) 库代码理解分块并行训练。
- **借鉴创新点**:
    - 为线性注意力引入数据相关门控以增强选择性记忆 (GLA → GSA)。
    - 把复杂模块形式化为已知高效算子的组合 ("两阶段 GLA"视角)。
    - T2R 中"保留 softmax"的迁移思想。
- **写 related work**: 可放入——高效/线性注意力 (与 [[GLA]]、[[RetNet]]、[[ABC]] 并列)、循环状态空间模型 (与 [[Mamba]]、[[RWKV]] 对比)、预训练模型高效适配 (与 [[T2R]]、[[SUPRA]] 相关)。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**序列建模与高效注意力机制**方向, 核心解决两个痛点: (1) 线性注意力 (及其门控变体) 在需要强上下文召回 (recall) 的任务上表现不佳; (2) 从头训练此类模型成本过高。它的独特切口是回到一个被低估的模型 ABC——因为 ABC 保留了 softmax, 特别适合"将预训练 Transformer 微调为 RNN" (T2R) 范式。因此归入"B_注意力算子模块"主题恰当, 具体聚焦于"改进受限内存的线性注意力算子"。

## 2. 一句话总结
GSA = 给 ABC 的每个内存槽加一个数据相关遗忘门 (受 GLA 启发), 把它重写成两层经 softmax 连接的 GLA; 在保持小状态、高训练/推理效率的同时, 显著提升上下文召回能力, 并因保留 softmax 成为 T2R 的理想选择。

## 3. 背景与问题
- **为什么要做**: softmax 注意力强大但二次复杂度 + KV cache 随生成长度线性增长, 推理时显存/吞吐受限。线性注意力线性复杂度、可重写为 RNN 高效推理, 但在上下文检索任务上落后, 且从头训练昂贵。
- **线性模型的两大遗留问题** (原文明列): (i) 性能——存在根本性"召回-内存权衡", 所有推理期常数内存模型都受限; (ii) 训练——万亿 token 从头训练仍太贵, 故 T2R (只用 1-3% 成本微调) 兴起, 但软/线性核不同导致迁移落差。
- **ABC 两大缺陷** (本文诊断): ① 无遗忘机制, 信息写入即永久保留, 槽位无法复用; ② 累积 softmax 写入给句首 token 过高写入强度 ($\phi_1=\mathbf{1}$ 写满所有槽), 违背近因偏置, 长上下文下不稳。
- **核心矛盾**: 在不牺牲 (反而提升) 训练/推理效率的前提下大幅增强上下文召回, 并能复用预训练权重。

## 4. 核心贡献
1. **把 ABC 重写为两阶段 (经 softmax 连接的) 线性注意力**, 直接套用 FLA 分块并行实现加速训练。
2. **提出 GSA**: 引入受 GLA 启发的数据相关标量门控 $\alpha_i$ (每槽独立), 即 ABC 的门控版本。
3. **诊断并系统修复 ABC 两大缺陷** (无遗忘 / 首 token 偏见) ——遗忘门修复其一, 耦合写入门 $1-\alpha$ 引入近因偏置修复其二。
4. **召回任务全面领先线性基线**: MQAR + 6 个真实召回/问答任务, 用更小状态超越所有 subquadratic 基线。
5. **验证 T2R 中保留 softmax 的重要性**: Mistral-7B → GSA 超越 RWKV6-7B/Mamba-7B 及 RetNet/GLA/SUPRA 等。
6. **效率平衡**: 训练吞吐与 GLA 相当, 推理因状态更小而更快。

## 5. 方法详解
- **骨干**: Llama 风格, 堆 $L$ 个块 = GSA token mixing + GLU channel mixing (图 2)。多头 $H=4$, 槽数 $m=64$。
- **投影与门**: $q,k,v = \mathrm{Swish}(Wx)$; 遗忘门 $\alpha_i = \sigma(W_\alpha x_i)^{1/\tau}$, 阻尼 $\tau=8$ 把门值往 1 推, 利于长程依赖。
- **更新规则 (公式 6)**: 两状态 $\widetilde{K}_t,\widetilde{V}_t \in \mathbb{R}^{m\times d}$:
    $\widetilde{K}_t = \mathrm{Diag}(\alpha_t)\widetilde{K}_{t-1} + (1-\alpha_t)\otimes k_t$
    $\widetilde{V}_t = \mathrm{Diag}(\alpha_t)\widetilde{V}_{t-1} + (1-\alpha_t)\otimes v_t$
    $o_t = \widetilde{V}_t^{\top}\,\mathrm{softmax}(\widetilde{K}_t^{\top} q_t)$
    $\alpha_t\in[0,1]^m$ 数据相关遗忘门, 写入门 $1-\alpha_t$ 与之耦合 (同 HGRN2)。
- **两阶段 GLA (公式 7)**:
    1. $\{o'_t\}=\mathrm{GLA}(q_t,k_t,1-\alpha_t,\alpha_t,1)$, 聚合历史键得上下文感知查询 $o'_t\in\mathbb{R}^m$;
    2. $\{o_t\}=\mathrm{GLA}(\mathrm{softmax}(o'_t),1-\alpha_t,v_t,1,\alpha_t)$, 用 softmax 增强查询读值。
    → 可复用 GLA 分块并行训练 (推导见 §A/§B)。
- **三点直观机制**: 遗忘门→清旧复用槽; 第一阶段线性注意力→全局上下文查询使 softmax 读取更准; 第二阶段 softmax→缓解注意力稀释, 且 (Hopfield 视角) 指数放大有效记忆容量, 同时结构更贴近预训练 softmax 注意力, 利于 T2R。
- **参数预算**: $W_{q,k,v,o}$ 合计 $4d^2$ 与标准注意力同; $W_\alpha$ 为 $dHm$, 设 $Hm\ll d$ 使总量约 $4.125d^2$。
- **训练/推理**: 训练用分块并行 + 反向重计算循环状态降显存; 推理展开为 RNN, 状态 $O(md)$ 与序列长度无关。
- **对比定位**: vs ABC (门控替代累积 softmax 写入); vs GLA (两层 GLA + 中间 softmax, 标准 GLA 单阶段无 softmax); vs RetNet (数据相关门 vs 数据无关固定衰减 $\gamma$); vs Transformer (状态 $O(Td)\to O(md)$, 复杂度二次→线性)。

## 6. 实验与结果
- **语言建模**: Slimpajama, 1.3B (L=24,d=2048) 与 2.7B (L=32,d=2560), 各 100B tokens。基线: Xfmr++、Mamba、RetNet、GLA、HGRN2。状态尺寸 GSA=HGRN2=128×Ld < GLA 256×Ld < RetNet 512×Ld; Mamba 64×Ld。
- **常识推理 (表 1)**: GSA 与 HGRN2 (同状态) 相当, 小状态下优于 GLA/RetNet。1.3B 平均准确率 GSA 51.7 / HGRN2 51.9 / GLA 50.4 / RetNet 50.6 / Mamba 49.8 / Xfmr++ 50.5。论文明示这些短任务不充分考察检索能力。
- **MQAR 召回 (图 3a)**: 最难设置 (len 512, 64 KV 对), GSA 准确率随维度稳升, 显著优于其他线性模型; Xfmr++ 近满分故省略。
- **真实召回 (表 3b, 输入截断 2K)** ——FDA/SWDE/SQuAD/NQ/TriviaQA/Drop:
    - 1.3B 平均: Xfmr++ 36.9 > **GSA 31.8** > GLA 31.4 > RetNet 28.4 > Mamba 27.7 > HGRN2 25.9。
    - 2.7B 平均: Xfmr++ 41.7 > **GSA 36.5** > GLA 34.3 > RetNet 31.0 > Mamba 30.5 > HGRN2 29.5。
    - GSA 在所有线性基线中平均最优, 但与 softmax 的 Xfmr++ 仍有约 5 分差距。
- **消融 (表 2, 340M / 10B tokens, PPL↓)**: GSA-64槽 13.51; 去衰减(=ABC) 16.94, 数据无关衰减 15.83 (门控最关键); 去 softmax 14.03 (>Swish 13.71/ReLU 13.69, softmax 最优); 槽数 32→13.74 / 64→13.51 / 128→13.46 (128 略好但慢, 选 64)。
- **效率 (图 4, 1.3B, H800)**: 训练吞吐 GSA≈GLA<Xfmr++ (槽 32/64/128 = 46.7K/44.1K/37.1K tok/s); 显存 GSA 37.4 GiB (重计算后 35.9) < Mamba 38.0 < Xfmr++ 41.4, 但略高于 GLA 36.2; 推理内存受限, 状态更小的 GSA 比 RetNet/GLA 推理更快 (图 4c 仅定性, 精确延迟数值提取未覆盖)。
- **T2R (§4.2)**: Mistral-7B→GSA 超大循环模型与其他 T2R 方法 (完整数值表在提取缓存未覆盖的后续页, 待核)。

## 7. 这篇论文真正有价值的地方
1. **数据相关门控 + 受限记忆**: 给固定容量内存槽装"遗忘门", 是平衡小状态与强召回的关键招式, 可推广到其他循环/SSM 模型。
2. **形式化复用红利**: 把新算子写成两次已有高效算子 (GLA) 的组合, 直接吃 FLA 的 kernel 红利, 同时让设计可解释——这是高效模型研究的实用范式。
3. **T2R 的可操作结论**: "保留 softmax 减少迁移损失"是一条明确、可迁移的工程指南。
4. **推进 (而非打破) 召回-内存帕累托前沿**: 用更小状态在召回上更好, 但与 softmax 的差距仍在——诚实地界定了贡献边界。

## 8. 局限与问题
1. **极长序列未验证**: 序列最长 ~16K (吞吐基准), 召回任务截断 2K; 百万级 token 下固定槽位能否够用未知。
2. **固定槽位**: $m$ 固定, 可能限制"信息量随长度线性增长"任务。
3. **仅因果建模**: 不直接适用双向/非因果任务。
4. **从头训练优势有限**: 优势集中在 T2R; 从零训练时短任务上与 HGRN2 接近。
5. **两阶段计算开销**: 走两次 GLA, 实际 FLOPs 可能高于单阶段 GLA/Mamba (靠更小状态弥补吞吐)。
6. **依赖 FLA 库**: 高效训练强绑定作者的 FlashLinearAttention。

## 9. 我该怎么使用这篇论文
- **快速了解**: Abstract + §1 + §3.1-3.3 + §4.1.2/§4.1.3 结论。
- **复现**: §3.2/§3.3 + 附录 §A/§B (Algorithm 1、超参数), 结合 FLA 库代码。
- **借鉴创新点**: 数据相关门控增强选择性记忆 (GLA→GSA); 复杂模块=高效算子组合 (两阶段 GLA); T2R 保留 softmax。
- **写 related work**: 高效/线性注意力 ([[GLA]]/[[RetNet]]/[[ABC]])、循环 SSM ([[Mamba]]/[[RWKV]])、预训练适配 ([[T2R]]/[[SUPRA]])。

## 10. 和其他论文的关系
- [[GLA]] (Gated Linear Attention): GSA 的门控机制与训练算法直接来源, GSA 可视为 GLA 的两阶段/深度扩展。
- [[ABC]] (Attention with Bounded-memory Control): GSA 是 ABC 的门控改进版, 修复其无遗忘与首 token 偏见两大缺陷。
- [[HGRN2]]: 写入/遗忘门耦合 ($k_t=1-\alpha_t$) 的参数化与之一致; GSA 额外含读取 softmax 与两阶段设计。
- [[RetNet]]: 主要对比基线, 同求高效推理, 但 RetNet 用数据无关固定衰减 $\gamma$, GSA 用数据相关门控。
- [[Mamba]]: 同属高效序列模型, 召回与效率上对比。
- [[FlashLinearAttention]] (FLA): GSA 高效训练的基础库 (即论文开源仓库)。
- [[T2R]]/[[SUPRA]]: GSA 在 T2R 范式中验证保留 softmax 的重要性, 优于 SUPRA。

## 11. 关键词
门控槽注意力, 线性注意力, 有界内存控制 (ABC), 门控线性注意力 (GLA), 上下文召回, Transformer 到 RNN 微调 (T2R), 数据相关遗忘门, 两阶段 GLA, 分块并行训练, 高效推理, softmax 检索

## 12. 可信度说明
本笔记主要基于 PDF 文本**前 12 页** (提取缓存标注 12/21 页, 且原文 43955 字符截断至前 25000 字符) 生成。该部分完整覆盖**摘要、引言、背景 (§2)、方法 (§3 核心) 及主要实验** (常识推理表 1、召回表 3a/3b、消融表 2、效率图 4a/4b)。关键数值 (状态尺寸、召回平均分、消融 PPL、吞吐 46.7K/44.1K/37.1K tok/s、显存 GiB) 均可在提取文本核到。**未完整覆盖**的部分: §4.2 T2R 的完整数值表、图 4c 推理延迟的精确数值、完整相关工作、附录算法伪代码与超参数 (落在 p.13-21, 据全文补读记录其中多页偏参考文献)。本轮修正了原笔记三处事实问题: (a) 作者列表 (补回 Yu Zhang/Songlin Yang/Ruijie Zhu/Peng Zhou/Guohong Fu, 非"Yue Zhang"领衔); (b) 显存对比 (GSA 37.4 GiB **略高于**而非低于 GLA 36.2); (c) 召回表补全 RetNet 数值。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/GatedSlotAttention.txt` (21/21 页; 原 AI 主体 12/21 + 全文补读 13-21); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮据提取文本重核摘要并修正作者/显存/RetNet 数值。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-21; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-21。
- **提取情况**: 缺失页 9 页, 其中 9 页提取到可读文本。缺失页包含正文/附录内容, 其中约 5 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.18: A Linear Attention and its Chunkwise Form
- p.18: By reserving bounded mmemory slots only, the overall computation complexity is reduced from
- p.18: During inference, LA enjoys the merits of RNNs, which only need to maintain O(md)hidden
- p.19: Hardward considerations Modern GPU architectures, such as the NVIDIA A100, offer highly
- p.19: B Algorithm Details for GSA
- p.19: Figure 5: Diagrams of the recurrence and updating rules in
- p.19: Gated Slot Attention ( GSA ) in Algo-
- p.19: In the preprocessing step, we pre-
- p.19: Ointer
- p.19: Ointra
- p.20: Algorithm 1 Hardware-Efficient Gated Slot Attention
- p.20: Define FORWARD PASS(Q,K,V,I,A)

### 缺失页关键摘录

- p.13: challenge dataset for reading comprehension. In R. Barzilay and M.-Y . Kan, editors, Proceed-
- p.13: J. Uszkoreit, Q. Le, and S. Petrov. Natural questions: A benchmark for question answering
- p.14: G. Boleda, and R. Fernández. The lambada dataset, 2016.
- p.14: E. Almazrouei, and J. Launay. The RefinedWeb dataset for Falcon LLM: outperforming
- p.17: Y . Liu, X. Qiu, and D. Radev. QMSum: A new benchmark for query-based multi-domain
- p.19: FLOPs greatly. Also, the chunk recurrent updating conducts the query and hidden states reduction
- p.19: significantly reduce the memory/IO overheads. While LA enjoys much lower overall running FLOPs
- p.19: Figure 5: Diagrams of the recurrence and updating rules in
- p.20: only the output of the first GLA pass, which significantly reduces memory consumption (Figure 4b).
- p.21: We utilize a subset of 100B tokens picked from the Slimpajama dataset [ 79]. The input tokens are
<!-- AI_READING_NOTE_END -->
