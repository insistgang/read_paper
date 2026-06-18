---
title: "Less but Better: Parameter-Efficient Fine-Tuning of Large Language Models for Personality Detection"
authors:
  - "Lingzhi Shen"
  - "Yunfei Long"
  - "Xiaohao Cai"
  - "Guanming Chen"
  - "Imran Razzak"
  - "Shoaib Jameel"
year: 2025
venue: "arXiv"
doi: 
pdf: [[高效PEFT微调 Less but Better PEFT.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
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
extract_cache: .paper-cache/extracts/高效PEFT微调 Less but Better PEFT.txt
---

# Less but Better: Parameter-Efficient Fine-Tuning of Large Language Models for Personality Detection

## 基本信息
- **PDF**: [[高效PEFT微调 Less but Better PEFT.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Less but Better: Parameter-Efficient Fine-Tuning of Large Language Models for Personality Detection |
| **作者** | Lingzhi Shen, Yunfei Long, Xiaohao Cai, Guanming Chen, Imran Razzak, Shoaib Jameel（University of Southampton / Queen Mary University of London / MBZUAI） |
| **发表时间** | 2025（arXiv:2504.05411v1, cs.CL, 2025-04-07） |
| **刊物/会议** | arXiv preprint |
| **DOI** | arXiv:2504.05411 |

## 摘要

**英文原文（据 PDF 提取文本整理，修复断词与空格）**:

> Personality detection automatically identifies an individual's personality from various data sources, such as social media texts. However, as the parameter scale of language models continues to grow, the computational cost becomes increasingly difficult to manage. Fine-tuning also grows more complex, making it harder to justify the effort and reliably predict outcomes. We introduce a novel parameter-efficient fine-tuning framework, PersLLM, to address these challenges. In PersLLM, a large language model (LLM) extracts high-dimensional representations from raw data and stores them in a dynamic memory layer. PersLLM then updates the downstream layers with a replaceable output network, enabling flexible adaptation to various personality detection scenarios. By storing the features in the memory layer, we eliminate the need for repeated complex computations by the LLM. Meanwhile, the lightweight output network serves as a proxy for evaluating the overall effectiveness of the framework, improving the predictability of results. Experimental results on key benchmark datasets like Kaggle and Pandora show that PersLLM significantly reduces computational cost while maintaining competitive performance and strong adaptability.

**中文翻译**:

> 人格检测旨在从社交媒体文本等多种数据源中自动识别个体的人格。然而，随着语言模型参数规模持续增长，计算成本越来越难以控制，微调也越来越复杂，使得"投入是否值得、结果是否可靠"变得难以判断。为此我们提出一种新颖的参数高效微调（PEFT）框架 PersLLM。在 PersLLM 中，大语言模型（LLM）从原始数据中提取高维表征并存入一个**动态记忆层**；随后用一个**可替换的输出网络**更新下游各层，以灵活适配不同的人格检测场景。通过把特征存入记忆层，避免了 LLM 反复进行复杂计算；同时这个轻量输出网络可作为评估整体框架效果的代理，提升了结果的可预测性。在 Kaggle 与 Pandora 两个基准数据集上的实验表明，PersLLM 在显著降低计算成本的同时，仍保持有竞争力的性能与很强的适应性。

> 关键词（Index Terms）: Personality Detection（人格检测）, Large Language Models（大语言模型）, Parameter-Efficient Fine-Tuning（参数高效微调）, Text Classification（文本分类）

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：MBTI 人格检测在个性化营销、心理健康评估、员工招聘等领域有广泛应用价值。语言模型捕捉复杂语言模式与上下文依赖的能力对从文本理解人格至关重要；但当模型扩展到数十亿乃至上万亿参数时，全参数微调面临巨大的计算资源需求、更长的训练时长和更高的内存消耗，严重影响对 LLM 在特定任务上表现的全面评估，且无法在开发阶段快速得到反馈与验证改进。
- **之前方法的问题**：
    1.  **经典模型**：SVM、XGBoost 及深度网络（如带注意力的 BiLSTM），以及图方法（D-DGCN、Semi-PerGCN）在社交媒体人格分类上有表现，但多数难以捕捉非结构化文本中更深层、更具上下文的关系。
    2.  **语言模型微调**：BERT、RoBERTa 已被微调用于人格识别（如结合情感词典做多标签检测、用混合策略预测连续人格值），但随着模型规模增大，微调日益复杂。
    3.  **LLM 应用方法**：PsyCoT 用心理问卷作为思维链（CoT）步骤、TAE 用文本增强从 LLM 蒸馏知识。但因微调成本高，研究者更偏向基于提示的方法以降低训练成本，**直接对 LLM 做微调用于人格检测的工作非常稀少**，可能因此错过该任务的最优方案。
- **核心矛盾**：在传统端到端模型中，每来一个新输入，LLM 都要重复特征提取、前向传播、反向传播等密集矩阵运算（self-attention、梯度计算），都需访问 LLM 的海量参数，计算开销极大。**需要利用 LLM 强大的语义表征能力，又要避免对相同/相似输入反复进行昂贵的 LLM 计算。**

## 关键贡献

1.  **提出 PersLLM 框架**：首个面向人格检测任务、用 LLM 做 PEFT 的框架，将"特征提取（LLM）—特征存储（记忆层）—任务训练（输出网络）"解耦，为微调 LLM 提供一种新策略。
2.  **动态记忆层（核心技术贡献）**：在特征提取之后引入由**索引、查询、缓存更新**三机制组成的动态记忆层，用局部敏感哈希（LSH）做高效检索，存储并复用提取的特征，消除每次推理都要调用 LLM 的开销。
3.  **可替换输出网络**：用参数少、计算轻的神经网络（以 GRU 为示例）做下游训练，仅学习基于记忆层特征的任务专属关系，训练快；网络可替换，从而无需重训 LLM 即可适配不同场景，其性能可作为评估整体框架的代理。
4.  **验证有效性**：在 Kaggle 与 Pandora 两个基准上，PersLLM 在全部四个维度及整体平均上均超越当前 SOTA（含基于提示与微调的方法），刷新性能标准。

## 方法

- **整体框架**：原始文本 → **LLM 特征提取** → **动态记忆层（缓存/检索）** → **可替换输出网络聚合** → **分类头预测**。核心思想是"一次提取、多次复用"，把 LLM 当作一次性的特征生成器，后续训练与推理交给轻量输出网络。
- **输入与输出**：
    - **输入**：单个用户的多条社交媒体帖子（按批次处理）。用户 `u_i` 的帖子集合 `P_i={p_i1,...,p_im}`，分批 `P_ib⊆P_i` 顺序处理。
    - **输出**：同时做两类预测——四个 MBTI 维度（E/I、S/N、T/F、J/P）的二分类，以及完整人格类型的 16 类分类。
- **关键模块**：
    1.  **特征提取层（III-A）**：用 **Llama 3.1**（实现细节为 Llama-3.1-8B-Instruct）逐批提取嵌入。Llama 用**分组查询注意力（GQA）**降低开销：将查询头数按因子 `g` 缩减，得 `Q'∈R^{s×(d_k/g)}`，键值矩阵 `K,V∈R^{s×d_k}` 保持不变，注意力为 `softmax(Q'K^T/√(d_k/g))·V`，在保持长程依赖建模能力的同时降低计算量。每批经多层 GQA + 前馈后得高维表征 `H_ib=GQA(E_ib)`，整体得序列 `H_i={H_i1,...,H_iB}`（B 为该用户批次数）。
    2.  **动态记忆层（III-B）**：
        - **索引**：对每个特征批 `H_ib` 做 LSH 投影到低维并保持相似性，`h_hash=sign(W_LSH·H_ib)`，`W_LSH` 为随机投影矩阵，得到二值向量作索引键。
        - **查询**：在记忆库 `M` 中按距离 `H*=argmin_{H_j∈M} d(H_ib,H_j)` 检索最近的已存批；相似度用余弦相似度 `S(H_ib,H_j)=H_ib·H_j/(‖H_ib‖‖H_j‖)`。
        - **缓存更新**：设相似度阈值 `θ`；若 `S(H_ib,H*)≥θ` 则直接复用已存表征，否则让 Llama 重算该批并存入。容量有限时采用**自适应 LRU 策略**：未满则并入 `M∪{H_ib}`，已满则淘汰最久未访问的 `H_oldest` 后并入。
    3.  **可替换输出层（III-C）**：记忆层在**批级**存取嵌入；输出网络把检索得到的批级特征 `{H_i1,...,H_iB}` 高效聚合为**用户级**紧凑表征。以 GRU 为示例：每步 `t` 用当前批嵌入 `H_it` 和前态 `h_{t-1}` 迭代刷新内部状态，处理完所有批得最终表征 `h_final`。该层刻意做得轻量，可无显著开销地替换为 Transformer 编码器或卷积网络等。
    4.  **分类（III-D）**：以 `h_final` 为输入；因输出网络可替换，分类过程与其具体结构解耦。四维各作独立二分类 `ŷ=(ŷ_E,ŷ_N,ŷ_T,ŷ_J)`；16 类则在全部 16 种 MBTI 类型上输出概率分布取最大者。
- **训练方式**：LLM 在初始特征提取后被冻结，不参与后续训练；仅输出网络与分类头用**交叉熵损失**、**Adam 优化器（学习率 1×10⁻³）**训练，可训练参数量大幅减少。
- **实现细节**：Llama 提取的特征向量长度与输出网络输入长度均统一为 **4096**；GRU 默认 **3 个隐层**、dropout 概率 **0.2**、每步输出隐维 **512**；为防标签泄漏，预处理时移除直接匹配人格标签的词；数据集按 **60%/20%/20%** 划分训练/验证/测试，报告结果为 **10 次运行的平均值**。
- **与已有方法的差异**：与 Adapter、LoRA、prefix/prompt tuning 等通用 PEFT 不同，PersLLM **不修改 LLM 内部结构**，而是通过外挂的记忆层 + 独立下游网络实现高效适配；与纯提示工程或知识蒸馏相比，它通过有限微调（仅输出网络）更充分利用了 LLM 的表征能力。

## 实验

- **数据集**（Table I）：
    - **Kaggle**：来自 PersonalityCafe 论坛，**8,675** 个用户，平均每人约 **45–50** 帖；帖文 train/val/test 为 246794/82642/82152。
    - **Pandora**：来自 Reddit 的更大语料，含 **9,084** 个带 MBTI 标签的用户，每人帖数从几十到几百不等，话题更广；帖文 train/val/test 为 523534/173005/174080。
    - 两数据集均为大规模输入、用户级聚合，且**类别不平衡显著**（尤其 S/N 与 E/I 维度）。
- **对比方法（Baselines）**：微调 BERT、RoBERTa；先进 LLM 的 GPT-4 Turbo 与 DeepSeek-V3（各含 Zero-shot 与 CoT 两种提示变体）；复杂架构 Transformer-MD（记忆增强的 Transformer-XL + 维度专属注意力）、PQ-Net（文本 + 心理问卷双流交叉注意力）；以及 LLM 人格检测专用方法 PsyCoT、TAE。
- **评价指标**：主指标为**宏平均 F1（Macro-F1）**，新增场景下辅以准确率（ACC）、精确率（P）、召回率（R）。
- **主实验结果（Table II，Macro-F1 %）**：
    - PersLLM 在 Kaggle 与 Pandora 的**全部四个维度及整体平均**上均最佳。
    - **Kaggle**：PersLLM 各维度 E/I 76.71、S/N 75.55、T/F 85.11、J/P 75.96，平均 **78.33%**；次优为 TAE 72.07%，领先 **6.26 个百分点**。
    - **Pandora**：PersLLM 各维度 E/I 68.89、S/N 66.72、T/F 73.70、J/P 68.55，平均 **69.47%**；次优为 TAE 63.05%，领先 **6.42 个百分点**。
    - 在类别严重不平衡的维度上提升明显，**缩小了 T/F 与其余三维之间的性能差距**。
    - 一个有意思的发现：CoT 逐步推理的结果甚至略差于 zero-shot，作者认为模型容量受限，且 CoT 的复杂分解会引入幻觉与噪声（提取文本在此处截断）。
- **消融/效率信息**：提取缓存覆盖前 8 页（截断于 IV-B"Overall Results"开头），**未包含**详细消融实验或参数量/FLOPs/推理速度的量化对比。论文以"输出网络轻量、可作整体效果代理"来论证可预测性与适应性，但具体效率数字在提取文本中**未明确**。

## 局限

1.  **依赖局部性假设**：动态记忆层基于"相似输入可复用特征"。对需要对每个输入做独立、精微理解的场景，按阈值 `θ` 复用缓存可能损失个性化信息。
2.  **记忆容量与超参敏感**：采用 LRU 淘汰，但提取文本未讨论记忆容量 `M`、相似度阈值 `θ` 的最优设置如何影响性能——过小导致频繁重算，过大可能存入低价值特征。
3.  **实验深度（受提取截断所限）**：提取缓存未覆盖消融实验，无法得知记忆层与输出网络各自的贡献度；与全参数微调相比实际节省的时间/内存等量化效率数据，在提取文本中**未明确**。
4.  **任务特异性**：方法专为人格检测（分类）设计，能否直接推广到生成式或更复杂 NLP 任务尚不明确。
5.  **复现风险**：依赖 Llama-3.1-8B-Instruct 及其 GQA；LSH 投影矩阵、缓存工程实现等细节可能影响复现。

## 个人评论

1.  **"计算缓存"思路清晰可落地**：把 LLM 从"每次都深度参与的处理器"变成"一次性特征生成器"，后续基于缓存特征训练/推理。这一思路对处理重复或高度相似输入（如同一用户的大量帖子）的 LLM 应用很有启发，本质上是把 KV/特征缓存的思想搬到了 PEFT 的系统层。
2.  **模块化与可替换性**：特征提取、特征存储、任务适配三段解耦，"可替换输出网络"让同一份 LLM 特征库快速适配不同任务/算力预算，灵活性与工程实用性都好。
3.  **拓宽 PEFT 设计空间**：证明 PEFT 不必侵入式改 LLM（加 Adapter/LoRA），外挂式架构（记忆层 + 轻量网络）也能在特定任务上取得 SOTA，给"无侵入 PEFT"提供了范例。
4.  **可改进处**：论文叙事强调"少即是好"，但提取文本中缺少消融与效率量化，记忆层在真实分布漂移下的命中率、阈值 `θ` 的鲁棒性是读者最想看到的证据；这是后续核对全文时需重点关注的部分。

### 使用建议

- **快速了解**：读摘要、引言贡献列表、以及 Table II 的对比结果，即可把握核心思想与成效。
- **如果复现**：精读方法论 III-A/B/C/D 与实验设置 IV-A（Llama-3.1-8B-Instruct、特征长 4096、GRU 3 层/dropout 0.2/隐维 512、Adam lr 1e-3、交叉熵、60/20/20 划分、10 次平均）。
- **如果借鉴创新点**：重点学动态记忆层（LSH 索引 + 余弦相似度查询 + 阈值复用 + 自适应 LRU）与可替换输出层的设计哲学。
- **如果写 Related Work**：归入"面向特定 NLP 任务（人格检测/情感分析）的 LLM PEFT"，与 LoRA、Adapter、prefix/prompt tuning 等通用方法，以及 PsyCoT、TAE 等任务专用方法对比。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**自然语言处理（NLP）**下的**文本分类 / 人格检测**子方向，聚焦**大语言模型（LLM）的参数高效微调（PEFT）**。它解决的问题是：在不做全参数微调、不修改 LLM 内部结构的前提下，如何用 LLM 高效完成 MBTI 人格类型检测，同时降低计算成本、提升结果可预测性。这是一篇纯 NLP/LLM 论文（任务为文本分类，无任何视觉模态），归类应为 `T_通用_NLP_其他`（原 `G_视觉基础模型_VLM_LLM` 不匹配，因为本文不涉及视觉或多模态）。

## 2. 一句话总结
PersLLM 把冻结的 LLM 当作一次性特征提取器，用 LSH 索引的动态记忆层缓存/复用批级特征，再接一个轻量可替换的输出网络（如 GRU）做下游训练，从而在大幅降低人格检测计算成本的同时，于 Kaggle/Pandora 上全面超越 SOTA。

## 3. 背景与问题
- **应用价值**：MBTI 人格检测用于个性化营销、心理健康评估、员工招聘等。
- **痛点**：LLM 参数达数十亿至上万亿，全参数微调计算/内存开销巨大、训练慢、难以在开发期快速验证；而传统端到端模型对每个输入都要重复特征提取与前向/反向传播，密集访问 LLM 海量参数。
- **现状空白**：BERT/RoBERTa 已被微调用于人格识别，PsyCoT/TAE 用提示或蒸馏方式应用 LLM，但**直接微调 LLM 做人格检测的工作极少**，可能错过最优方案。
- **核心矛盾**：要用 LLM 的强语义表征，又要避免对相似/重复输入反复进行昂贵的 LLM 计算。

## 4. 核心贡献
1.  **PersLLM 框架**：首个面向人格检测的 LLM-PEFT 框架，解耦"提取—存储—训练"。
2.  **动态记忆层**：索引 + 查询 + 缓存更新三机制，LSH 高效检索，复用特征以省去重复 LLM 计算（关键技术贡献）。
3.  **可替换输出网络**：轻量、训练快、可替换，性能可作整体框架的评估代理，无需重训 LLM 即可适配新场景。
4.  **SOTA 验证**：Kaggle/Pandora 四维 + 平均全面领先。

## 5. 方法详解
- **流程**：文本 → Llama 3.1 提取批级特征 → LSH 索引的动态记忆层缓存/检索 → GRU 等输出网络聚合为用户级表征 → 二分类（四维）+ 16 类分类。
- **特征提取（III-A）**：Llama-3.1-8B-Instruct 按批处理用户帖子；GQA 把查询头按 `g` 缩减，`Q'∈R^{s×(d_k/g)}`，K/V 不变，`Attention=softmax(Q'K^T/√(d_k/g))V`，降开销又保长程依赖；输出批级 `H_i={H_i1,...,H_iB}`。
- **动态记忆层（III-B）**：`h_hash=sign(W_LSH·H_ib)` 做索引；`H*=argmin_{H_j∈M} d(H_ib,H_j)`，余弦相似度查询；阈值复用 `S(H_ib,H*)≥θ` 则用缓存、否则重算并存；满则自适应 LRU 淘汰 `H_oldest`。
- **可替换输出层（III-C）**：批级 → 用户级聚合；GRU 每步用 `H_it` 与 `h_{t-1}` 更新得 `h_final`；可换成 Transformer 编码器/卷积网络。
- **分类（III-D）**：四维独立二分类 `ŷ=(ŷ_E,ŷ_N,ŷ_T,ŷ_J)`；16 类在全部类型上取最大概率。
- **训练**：LLM 冻结；仅输出网络 + 分类头用交叉熵 + Adam（lr 1e-3）训练。特征/输入维统一 4096；GRU 3 层、dropout 0.2、隐维 512；移除标签泄漏词；60/20/20 划分；结果取 10 次均值。

## 6. 实验与结果
- **数据集**：Kaggle（PersonalityCafe，8,675 用户，约 45–50 帖/人）；Pandora（Reddit，9,084 用户，几十至几百帖/人）。两者类别不平衡显著（S/N、E/I）。
- **基线**：BERT、RoBERTa、Transformer-MD、PQ-Net、GPT-4 Turbo（Zero-shot/CoT）、DeepSeek-V3（Zero-shot/CoT）、PsyCoT、TAE。
- **指标**：Macro-F1 为主，辅以 ACC/P/R。
- **结果（Table II）**：
    - Kaggle 平均 **78.33%**，次优 TAE 72.07%，领先 **6.26pp**（PersLLM 维度：E/I 76.71、S/N 75.55、T/F 85.11、J/P 75.96）。
    - Pandora 平均 **69.47%**，次优 TAE 63.05%，领先 **6.42pp**（维度：E/I 68.89、S/N 66.72、T/F 73.70、J/P 68.55）。
    - 在类别不平衡维度提升明显，缩小 T/F 与其余维度的差距。
    - CoT 反而略逊 zero-shot：作者归因于模型容量受限 + CoT 分解引入幻觉/噪声（此处提取截断）。
- **效率/消融**：提取缓存未覆盖，参数量/FLOPs/速度等量化数据在提取文本中未明确。

## 7. 这篇论文真正有价值的地方
1.  **"计算缓存"思想**：LLM 由"处理器"变"一次性特征生成器"，为降 LLM 推理成本提供清晰可落地的架构。
2.  **模块化可替换**：提取/存储/适配三段解耦，同一特征库快速适配多任务/多算力预算。
3.  **无侵入 PEFT 范例**：不改 LLM 结构、靠外挂记忆层 + 轻量网络也能拿到任务 SOTA，拓宽 PEFT 设计空间。

## 8. 局限与问题
1.  **局部性假设**：阈值 `θ` 复用缓存在需精微独立理解的场景可能丢失个性化信息。
2.  **超参敏感**：记忆容量 `M`、阈值 `θ` 的最优设置与影响在提取文本中未讨论。
3.  **缺消融与效率量化**：提取截断，记忆层/输出网络各自贡献、与全参数微调的实际节省均未在提取文本中体现。
4.  **任务特异**：能否推广到生成式/更复杂 NLP 任务未知。
5.  **复现风险**：依赖特定 Llama 版本与 GQA；LSH/缓存工程细节影响复现。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言贡献 + Table II。
- **复现**：精读 III-A/B/C/D 与 IV-A 实现细节（模型、4096 维、GRU 3 层/dropout 0.2/隐维 512、Adam lr 1e-3、交叉熵、60/20/20、10 次平均）。
- **借鉴创新**：动态记忆层（LSH + 余弦查询 + 阈值复用 + 自适应 LRU）与可替换输出层。
- **写 Related Work**：归入"特定 NLP 任务的 LLM-PEFT"，对比 LoRA/Adapter/prefix-prompt tuning 及 PsyCoT/TAE。

## 10. 和其他论文的关系
- 同属 PEFT 大方向，与 `[[LoRA]]`、`[[Adapter]]`、`[[Prefix-Tuning]]`、`[[Prompt-Tuning]]` 技术路径不同（本文不改 LLM 结构，走外挂记忆层）。
- 提及 `[[AdapterHub]]`（将多种 adapter 方法统一为"adapter method"抽象）作为 PEFT 模块化背景。
- 人格检测任务上直接对比 `[[BERT]]`、`[[RoBERTa]]`、`[[GPT-4]]`、`[[DeepSeek-V3]]`、`[[PsyCoT]]`、`[[TAE]]`，以及 Transformer-MD、PQ-Net。
- 动态记忆层与 Transformer-MD 所基于的 Transformer-XL 记忆/片段递归机制有相通之处（扩展可访问上下文、减少重复计算）。

## 11. 关键词
人格检测, MBTI, 大语言模型, 参数高效微调（PEFT）, 动态记忆层, 局部敏感哈希（LSH）, 自适应 LRU, 可替换输出网络, GRU, 分组查询注意力（GQA）, Llama-3.1-8B-Instruct, 文本分类, 计算效率

## 12. 可信度说明
本精读笔记基于 PDF 提取缓存的**前 8 页**（截断于第 25000 字符、IV-B "Overall Results" 开头；原文约 43183 字符）。覆盖了摘要、引言、相关工作、方法论（III-A 至 III-D 完整）、实验设置（IV-A，含 Table I 数据统计与全部实现细节）与主结果（Table II 完整数据）。**结论、详细消融分析、效率量化、附录**等内容在提取文本中缺失，相关结论已逐处标注"提取文本未明确/受截断所限"。
提取质量良好，方法公式、数据集统计与对比数值清晰；所有数字（78.33%、69.47%、+6.26pp、+6.42pp 及各维度值、4096、GRU 3 层/0.2/512、Adam 1e-3、60/20/20、10 次平均、8675/9084 用户等）均可在提取文本逐一核对。笔记严格依据提取文本，未引入外部知识或推测。

---

> **可信度补充**: PDF 提取质量 = **high** (前 8 页提取清晰, 关键公式/表格数值完整; 提取缓存截断于第 25000 字符, 未覆盖结论与消融, 已逐处标注); 来源缓存: `.paper-cache/extracts/高效PEFT微调 Less but Better PEFT.txt` (8/8 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
