---
title: Scaling Laws for Neural Language Models
authors:
  - "Jared Kaplan"
  - "Sam McCandlish"
  - "Tom Henighan"
  - "Tom B. Brown"
  - "Benjamin Chess"
  - "Rewon Child"
  - "Scott Gray"
  - "Alec Radford"
  - "Jeffrey Wu"
  - "Dario Amodei"
year: 2020
venue: "arXiv"
doi: 
pdf: [[Scaling_Laws_for_Neural_Language_Models.pdf]]
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
extract_cache: .paper-cache/extracts/Scaling_Laws_for_Neural_Language_Models.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/30 pages"
---
# Scaling Laws for Neural Language Models

## 基本信息
- **PDF**: [[Scaling_Laws_for_Neural_Language_Models.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Scaling Laws for Neural Language Models |
| **作者** | Jared Kaplan, Sam McCandlish (共同一作); Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei |
| **单位** | Johns Hopkins University (Kaplan), OpenAI (其余) |
| **发表时间** | 2020 (arXiv:2001.08361v1, 2020-01-23) |
| **刊物/会议** | arXiv (预印本) |
| **DOI** | arXiv:2001.08361 |

## 摘要

清理后的英文原摘要（据 PDF 提取文本修复空格/连字符、剔除杂入字符）：

> We study empirical scaling laws for language model performance on the cross-entropy loss. The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. Other architectural details such as network width or depth have minimal effects within a wide range. Simple equations govern the dependence of overfitting on model/dataset size and the dependence of training speed on model size. These relationships allow us to determine the optimal allocation of a fixed compute budget. Larger models are significantly more sample-efficient, such that optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence.

中文翻译：

> 我们研究语言模型在交叉熵损失上的经验性缩放定律。损失随模型规模、数据集规模和训练所用计算量呈幂律变化，其中部分趋势跨越了七个以上数量级。网络宽度、深度等其他架构细节在很宽的范围内影响甚微。简洁的方程刻画了过拟合对模型/数据集规模的依赖关系，以及训练速度对模型规模的依赖关系。基于这些关系，我们可以确定固定计算预算下的最优分配方式。更大的模型样本效率显著更高，因此计算最优的训练应当是：训练一个非常大的模型，只用相对适量的数据，并在远未收敛之前就停止。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **这篇论文为什么要做**：深度学习在语言建模上进展迅速，当时最先进模型（如 GPT-2 [RWC+19] 等）已能生成连贯的多段文本。但人们一直缺乏对"性能如何依赖模型架构、模型规模、计算量与数据量"的系统定量理解，研究者多凭经验或直觉来设计模型、分配资源。
- **作者的切入点**：语言任务"性能上限高、下限低"的特点，使得可以在超过七个数量级的尺度范围上观察趋势。作者聚焦 Transformer 架构 [VSP+17]，系统地把损失（交叉熵）写成训练时间、上下文长度、数据集规模、模型规模、计算预算的函数，去寻找其中的精确幂律。
- **作者想解决的核心矛盾是**：在计算预算 C 固定的前提下，如何在模型大小 N 与训练数据量 D 之间分配，以达到最低测试损失 L —— 即同样的算力，是该花在"造更大的模型"还是"喂更多的数据/训更久"上？
## 关键贡献

1.  **性能与规模的幂律关系**：当不被其它两个因素瓶颈时，测试损失 L 分别与非嵌入参数量 N、数据集大小 D、最优分配计算预算 C_min 呈幂律关系（式 1.1-1.3）：`L(N)=(N_c/N)^{α_N}`，α_N≈0.076，N_c≈8.8×10^13；`L(D)=(D_c/D)^{α_D}`，α_D≈0.095，D_c≈5.4×10^13 tokens；`L(C_min)=(C_c^min/C_min)^{α_C^min}`，α_C^min≈0.050，C_c^min≈3.1×10^8 PF-days。趋势分别跨越约 6（N）、2（D）、8（C_min）个数量级。
2.  **性能强依赖规模、弱依赖形状**：在固定非嵌入参数量 N 时，深度/宽度、注意力头数 n_heads、前馈维度 d_ff 等架构超参对损失影响仅几个百分点（§3，图 5）。例如纵横比 d_model/n_layer 可变化 40 倍而损失几乎不变；(n_layer,d_model)=(6,4288) 与 GPT-2 用的 (48,1600) 损失相差在 3% 以内。
3.  **过拟合的普遍规律**：N 与 D 须协同扩展；性能惩罚可预测地取决于比值 N^{0.74}/D。即模型规模每放大 8 倍，数据量只需放大约 5 倍即可避免惩罚。联合公式 `L(N,D)=[(N_c/N)^{α_N/α_D}+D_c/D]^{α_D}`（式 1.5，§4，图 4 左）。
4.  **训练曲线的普遍性**：不同规模模型在初始瞬态之后，学习曲线都能用同一族幂律拟合，参数大致与模型大小无关（式 1.6：`L(N,S)=(N_c/N)^{α_N}+(S_c/S_min(S))^{α_S}`，S_c≈2.1×10^3，α_S≈0.76）；借此可由训练早期外推最终损失（§5，图 4 右）。
5.  **最优计算分配策略**：固定预算 C 下，大部分算力应投向更大的模型。N∝C_min^{α_C^min/α_N}、B∝C_min^{α_C^min/α_B}、S∝C_min^{α_C^min/α_S}（式 1.7-1.8），经验拟合为 N∝C_min^{0.73}、B∝C_min^{0.24}、S∝C_min^{0.03}（§6，图 3）。数据需求随训练算力增长很慢，D∝C^{0.27}。结论：大模型本质上更样本高效。
## 方法

- **整体框架**：实证研究。训练大量不同配置的 Transformer 语言模型，控制变量逐一改变某个因素（模型大小、数据量、模型形状、批大小、上下文长度等），记录测试损失，再拟合经验幂律。
- **输入输出**：自回归语言建模，上下文长度 n_ctx=1024 token（除特别说明外），目标是对每个 token 预测下一个 token；主性能指标是在 1024-token 上下文上平均的交叉熵损失（nats）。
- **架构**：主要是 decoder-only Transformer [VSP+17, LSP+18]；另训练 LSTM 与 Universal Transformers（循环 Transformer）[DGV+18] 作对比。Transformer 由 n_layer、d_model（残差流维度）、d_ff（前馈中间维度）、d_attn（注意力输出维度）、n_heads 参数化。
- **关键定义与公式**：
    - 模型规模 N 定义为**非嵌入参数量**：`N≈12·n_layer·d_model^2`（取标准 d_attn=d_ff/4=d_model，式 2.1）；嵌入矩阵 n_vocab·d_model 与位置嵌入 n_ctx·d_model 不计入 N（作者指出排除嵌入参数能得到明显更干净的缩放定律，图 6）。
    - 前向计算量 `C_forward≈2N+2·n_layer·n_ctx·d_model`（式 2.2）；计入约为前向 2 倍的反向传播后，每 token 非嵌入训练算量 `C≈6N`。
    - 总训练算量 `C≈6·N·B·S`（B 批大小、S 训练步数），以 PF-days 计量，1 PF-day = 10^15·24·3600 = 8.64×10^19 FLOPs。
    - 临界批大小 B_crit(L)≈B_*/L^{1/α_B}（式 1.4，B_*≈2×10^8 tokens，α_B≈0.21），由梯度噪声尺度 [MKAT18] 测定；最大模型收敛时约 1-2 百万 tokens。
- **训练方式**：除特别说明外用 Adam [KB14]，固定 2.5×10^5 步，批大小 512 个长 1024 的序列；因显存约束，最大模型（>1B 参数）改用 Adafactor [SS18]。学习率用 3000 步线性预热后余弦衰减到 0；作者发现收敛结果对学习率调度大体不敏感。
- **和已有方法的差异**：不提出新模型，而是首次大规模、系统化地把现有主流架构（Transformer）的性能与 N/D/C 之间的关系量化为可预测的简洁公式，将模糊的"规模直觉"变成可外推的数学定律。
## 实验

- **使用的数据集**：训练与主测试集为 **WebText2**——WebText [RWC+19] 的扩展版。原 WebText 是 2017 年 12 月前 Reddit 上 ≥3 karma 外链的网页抓取；WebText2 又加入 2018 年 1-10 月、同样 ≥3 karma 的外链，用 Newspaper3k 抽取正文。共 20.3M 文档、96 GB 文本、1.62×10^10 词（wc 计），经 BPE（n_vocab=50257）tokenize 后得 2.29×10^10 tokens，其中 6.6×10^8 tokens 留作测试集。泛化测试集：Books Corpus、Common Crawl、English Wikipedia、公开互联网图书。
- **变量范围**：模型规模 768 ~ 1.5B 非嵌入参数；数据量 22M ~ 23B tokens；形状（深度/宽度/头数/前馈维度）；上下文长度（多数 1024，也试更短）；批大小（多数 2^19，也调节以测临界批大小）。
- **对比方法**：不同规模 Transformer 之间对比；Transformer vs LSTM；Transformer vs 循环 Transformer（Universal Transformers）[DGV+18]（在附录图 17）。
- **评价指标**：WebText2 测试集上的交叉熵损失（nats）。
- **主实验结果**：
    - **幂律验证**：L 对 N、D、C 各自呈清晰幂律，趋势跨越六个以上数量级，且高端未见偏离趋势的迹象（损失最终必在到达零损失前趋平）（§3，图 1）。
    - **形状不敏感**：固定 N 时改变形状，损失仅变化几个百分点（图 5）；含嵌入参数时性能"看似"强依赖层数，排除嵌入参数后不同深度模型收敛到同一趋势（图 6）。
    - **过拟合规律**：联合公式 L(N,D)（式 1.5）拟合良好（图 4 左）。
    - **训练曲线规律**：式 1.6 拟合所有规模学习曲线（图 4 右）。
    - **LSTM 对比**：LSTM 在上下文前部 token 上与 Transformer 相当，但 <100 个 token 后趋于平台，无法利用长上下文，后部 token 性能显著落后（图 7）。
    - **泛化（迁移）**：在 WebText2 上训练的模型在其它数据分布上的损失也随 N 平滑改善，与 in-distribution 验证损失强相关，且对训练时长/是否接近收敛几乎不依赖；迁移到不同分布只带来一个大致恒定的损失偏移（§3.2.2，图 8）。
- **消融实验**：文中未用"ablation"一词，但通过严格控制变量逐一研究 N、D、形状、批大小等因素，本质上构成了对各维度的系统消融。
- **速度/参数量/FLOPs**：见"方法"中 N≈12·n_layer·d_model^2、C≈6NBS、PF-day 定义；论文论证计算最优训练应在收敛前很早停止，故远比"小模型训到收敛"样本高效。
## 局限

- **架构依赖性**：结论基于 decoder-only Transformer。文中虽对比了 LSTM 与循环 Transformer，但对编码器-解码器、混合专家等其它架构是否成立未做系统验证。
- **常数无根本意义**：幂律的具体常数（N_c、D_c、C_c^min）依赖词表大小与 tokenization，论文明言"因此没有根本意义"，跨数据集/分词方案不可直接迁移。
- **外推风险**：虽趋势跨多个数量级且高端未见偏离，作者仍承认损失"最终必在到达零损失前趋平"；把关系外推到远超本研究范围的规模，其有效性未经验证。
- **计算成本高昂**：需训练大量不同规模模型才能拟合出这些公式，门槛很高。
- **假设依赖**：最优分配（式 1.7-1.8）依赖可自由调批大小等假设；最优批大小约为损失的幂函数（式 1.4），需借梯度噪声尺度估计。
- **(说明)** 提取缓存仅覆盖前 12 页（截至 §3.3 中段），§4-§8、附录及参考文献未在提取文本内；下文凡涉及 p.13 以后页码的数字均据原文后续页/原笔记，提取缓存未覆盖，待核。
## 个人评论

（以下为 AI 阅读阶段的评论，非人工精读结论。）

这篇论文最核心的价值在于，它**把大模型训练从一门"手艺"向"工程科学"推进了关键一步**。它给出的几条幂律就像一个"水晶球"：在真正花费昂贵算力之前，就能**预测**不同资源配置下的模型损失。

- **对后续研究的启发**：它确立了"规模即性能、且可预测"的实证基础，直接指导了后续 GPT-3 等更大模型的研发路线（"训非常大的模型、提前停止"）。值得注意的是，两年后 Chinchilla（DeepMind, 2022）修正了本文关于 N 与 D 分配比例的结论——指出当时这类工作普遍把模型造得过大、数据喂得过少，N 与 D 应近似等比例扩展。因此本文的最优分配指数（N∝C^0.73）应理解为该实验设置下的经验值，而非最终定论。
- **对改模型/做实验的启发**：提升性能最有效的途径是同时扩 N 与 D，但（按本文）N 增长应快于 D；资源有限时优先训一个远大于"收敛所需"规模的模型、用较少数据、提前停止。这与"小模型在大数据上训到收敛"的传统直觉相反。
- **对写论文的启发**：是"如何做大规模系统性实证、并从噪声数据中提炼出简洁公式"的范本——从观测现象→拟合公式→推论→应用，逻辑链完整。

### 使用建议

- **快速了解**：读摘要、§1.1 Summary、§1.2 Summary of Scaling Laws，即可掌握全部核心发现与公式（式 1.1-1.8）。
- **复现**：读 §2 Background and Methods（模型/算量定义、训练过程、WebText2 构建）及附录 D 的具体设置。
- **借鉴创新点**：读 §3-§6，学习如何设计控制变量实验隔离 N、D 的单独影响，以及如何拟合幂律。
- **写 related work**：归入"大语言模型的缩放定律 / Transformer 训练动力学 / 计算效率与样本效率"，它是该方向的奠基工作；与 Chinchilla 对照阅读尤佳。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
机器学习/自然语言处理领域，属于**神经网络缩放定律（Scaling Laws）**研究。论文通过大规模实证，系统量化了 Transformer 语言模型的交叉熵损失如何随非嵌入参数量 N、训练数据量 D、计算预算 C 变化，目标是为大模型训练提供可预测的公式与资源分配指导。这是一篇纯 NLP/LLM 论文（无视觉成分），故归入 `T_通用_NLP_其他` 主题。

## 2. 一句话总结
Transformer 语言模型的损失与模型大小、数据量、计算量之间存在跨越多个数量级的平滑幂律关系；据此，固定算力下最优做法是"训一个非常大的模型、用适量数据、远在收敛前停止"，因为大模型样本效率本质更高。

## 3. 背景与问题
- **动机**：深度学习语言建模进展快，但"性能 vs 架构/规模/算力/数据"缺乏定量理解，资源分配靠直觉。
- **空白**：缺乏把损失写成各因素函数的普适、可外推的定量关系。
- **核心矛盾**：固定计算预算 C 下，如何在模型大小 N 与数据量 D 间分配以最小化损失 L —— 把算力花在更大的模型上，还是更多的数据/更长的训练上？

## 4. 核心贡献
1.  **三大幂律**：`L(N)=(N_c/N)^{0.076}`、`L(D)=(D_c/D)^{0.095}`、`L(C_min)=(C_c^min/C_min)^{0.050}`（式 1.1-1.3），常数 N_c≈8.8×10^13、D_c≈5.4×10^13 tokens、C_c^min≈3.1×10^8 PF-days；趋势跨越 6（N）/2（D）/8（C_min）个数量级。例：参数翻倍损失约乘 2^{-0.076}≈0.95。
2.  **强依赖规模、弱依赖形状**：固定 N 时深度/宽度/头数/前馈维度等仅影响损失几个百分点（图 5）。
3.  **过拟合普遍规律**：惩罚取决于 N^{0.74}/D；N 放大 8 倍只需 D 放大约 5 倍。联合式 1.5：`L(N,D)=[(N_c/N)^{α_N/α_D}+D_c/D]^{α_D}`。
4.  **训练曲线普遍性**：式 1.6 `L(N,S)=(N_c/N)^{α_N}+(S_c/S_min)^{α_S}`，S_c≈2.1×10^3、α_S≈0.76，参数近似与模型大小无关，可由早期外推最终损失。
5.  **最优计算分配**：经验拟合 N∝C_min^{0.73}、B∝C_min^{0.24}、S∝C_min^{0.03}（式 1.7-1.8）；数据需求 D∝C^{0.27} 增长很慢。大部分增量算力应投向模型规模。

## 5. 方法详解
- **整体框架**：实证 + 控制变量 + 幂律拟合。逐一改变单一因素、固定其余，记录测试损失，拟合经验公式。
- **输入输出**：自回归语言建模，n_ctx=1024，主指标为 1024-token 平均交叉熵损失（nats）。
- **架构**：主体 decoder-only Transformer，另有 LSTM、Universal Transformers 作对比。
- **关键定义**：
    - 规模 N = **非嵌入参数量** ≈ 12·n_layer·d_model^2（式 2.1，取 d_attn=d_ff/4=d_model）；嵌入/位置嵌入参数不计入 N（排除后缩放定律明显更干净，图 6）。
    - 前向算量 C_forward≈2N+2·n_layer·n_ctx·d_model（式 2.2）；含反向后每 token C≈6N；总算量 C≈6NBS；1 PF-day=8.64×10^19 FLOPs。
    - 临界批大小 B_crit(L)≈B_*/L^{1/α_B}（B_*≈2×10^8 tokens、α_B≈0.21），由梯度噪声尺度 [MKAT18] 测定，最大模型收敛时约 1-2M tokens。
- **训练**：Adam，固定 2.5×10^5 步，批 512 序列×1024 token；最大模型（>1B）用 Adafactor；3000 步线性预热 + 余弦衰减到 0；结果对学习率调度大体不敏感。
- **差异**：不创新架构，而是把 Transformer 性能与 N/D/C 的关系量化为可外推的简洁定律。

## 6. 实验与结果
- **数据集**：WebText2（20.3M 文档 / 96GB / 1.62×10^10 词 / BPE 后 2.29×10^10 tokens，6.6×10^8 留作测试；vocab 50257）；泛化测试用 Books Corpus、Common Crawl、English Wikipedia、互联网图书。
- **变量范围**：N 768~1.5B；D 22M~23B tokens；形状/上下文长度/批大小亦扫。
- **对比**：不同规模 Transformer；Transformer vs LSTM；Transformer vs 循环 Transformer。
- **指标**：WebText2 测试交叉熵损失（nats）。
- **主结果**：
    - 幂律对 N/D/C 均成立，跨六个以上数量级，高端无偏离迹象（图 1）。
    - 固定 N 改形状损失仅变几个百分点；排除嵌入参数后不同深度收敛到同一趋势（图 5、6）。
    - L(N,D)（式 1.5）与学习曲线（式 1.6）拟合良好（图 4）。
    - LSTM 在 <100 token 后趋平台，长上下文不及 Transformer（图 7）。
    - 泛化：他域损失随 N 平滑改善、与 in-distribution 验证损失强相关，仅带恒定偏移；不依赖训练时长（图 8）。
- **算量分析**：计算最优训练远在收敛前停止，故比"小模型训到收敛"样本高效得多。

## 7. 这篇论文真正有价值的地方
把大模型训练从"手艺"推向"工程科学"：用几条幂律即可在花费算力前预测不同配置的损失，并给出"固定算力下如何分配 N/D/S"的明确处方。它确立了"规模即性能、且可预测"的实证基础，深刻影响了后续 GPT-3 乃至整个大模型路线；同时也是大规模系统性实证研究的方法论范本。需与 Chinchilla（2022）对读：后者修正了本文 N/D 分配比例，指出本文设定下模型偏大、数据偏少。

## 8. 局限与问题
- 结论基于 decoder-only Transformer，对其它架构的普适性未系统验证。
- 幂律常数依赖词表与分词，"没有根本意义"，跨设置不可直接迁移。
- 外推到远超本研究规模的有效性未验证；损失终将在到达零之前趋平。
- 拟合需训练大量模型，门槛高。
- 最优分配依赖"可自由调批大小"等假设。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + §1.1 + §1.2（式 1.1-1.8）。
- **复现**：§2（模型/算量定义、训练过程、WebText2）+ 附录 D。
- **借鉴创新点**：§3-§6，学习控制变量隔离 N/D 影响与幂律拟合方法。
- **写 related work**：归入"LLM 缩放定律 / Transformer 训练动力学 / 计算与样本效率"，与 Chinchilla 对照。

## 10. 和其他论文的关系
- 直接影响 **GPT-3**（训练受本文缩放定律指导）；后由 **Chinchilla**（2022）修正 N/D 分配关系。
- 对比了 **LSTM** 与 **Universal Transformers / 循环 Transformer** [DGV+18]。
- 依赖/引用：Transformer [VSP+17]、Adam [KB14]、梯度噪声尺度与临界批大小 [MKAT18]、WebText/GPT-2 数据 [RWC+19]、BPE [SHB15]、Adafactor [SS18]、decoder-only [LSP+18, RNSS18]。
- *注：提取缓存仅含前 12 页，完整参考文献列表与 §7 Related Work 未覆盖，关联可能不全。*

## 11. 关键词
缩放定律, 幂律, Transformer, 语言模型, 交叉熵损失, 计算效率, 样本效率, 模型规模, 数据集规模, 最优计算分配, 过拟合, 训练动力学, 临界批大小, 梯度噪声尺度。

## 12. 可信度说明
本精读笔记**主要基于提供的 PDF 提取文本（前 12 页，含摘要、目录、§1 引言与总结、§2 背景与方法、§3 部分实证结果，且第 12 页处文本在约 25000 字符被截断、止于 §3.3 中段）**。其中的关键公式、数字与结论（式 1.1-1.8、§2 各定义、WebText2 统计、形状不敏感、LSTM 对比、泛化等）均可在提取文本中直接核到。
**§4-§8、所有附录及完整参考文献未在提取文本内**；涉及最优分配的完整推导、训练曲线拟合更多细节、临界批大小图 10 / 早停下界 §5.3 等仅据原文后续页（p.13-16）与原笔记保留，提取缓存未覆盖，待核。这些处已尽量标注页码与不确定性。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本约 2086 字符/页, 前 12 页可读性好; 但提取缓存仅 12/30 页且第 12 页处被字符上限截断); 来源缓存: `.paper-cache/extracts/Scaling_Laws_for_Neural_Language_Models.txt`; 全文补读记录覆盖 p.13-30 (AI 补读, 非人工复核); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-30; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-30。
- **提取情况**: 缺失页 18 页, 其中 18 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Bcritminimizes the number of training steps, while B
- p.13: Bcritminimizes
- p.13: In Figure 10 we have plotted the critical batch size and gradient noise scale5as a function of training loss for
- p.13: We have chosen this parameterization for Bcrit(L)because as the loss approaches its minimum value Lmin,
- p.13: We will use Bcrit(L)to estimate the relation between the number of training steps Swhile training at batch
- p.14: Parameters (non-embedding)2345678Test LossPerformance vs Compute Budget
- p.14: PF-dayss
- p.14: Parameter
- p.14: SNcSc
- p.14: 5.3 Lower Bound on Early Stopping Step
- p.14: 6 Optimal Allocation of the Compute Budget
- p.14: We displayed the empirical trend of performance as a function of the computation used during training in

### 缺失页关键摘录

- p.13: We demonstrate the relation (5.1) for Transformers in Figure 18 in the appendix. This relation deﬁnes the
- p.13: In Figure 10 we have plotted the critical batch size and gradient noise scale5as a function of training loss for
- p.14: With these parameters, we obtain the learning curve ﬁts in Figure 4. Though the ﬁts are imperfect, we believe
- p.14: The data and ﬁts can be visualized in a different and more interesting way, as shown in Figure 11. There we
- p.14: parison to the empirical data is displayed in Figure 16 in the appendix. In that ﬁgure, the values of Sstop
- p.14: the top-right of Figure 1. However, this result involved training at a ﬁxed batch size B, whereas we know
- p.15: Figure 12 Left: Given a ﬁxed compute budget, a particular model size is optimal, though somewhat larger
- p.15: Figure 13 When adjusting performance to simulate training far below the critical batch size, we ﬁnd a
- p.15: Let us ﬁrst study the loss as a function of the optimally allocated compute from Equation (5.5). The result is
- p.15: plotted in Figure 13, along with a power-law ﬁt. We see that as compared to the compute plot of Figure 1, the
- p.15: given quantity of training compute. The optimal model size is shown in Figure 14. We observe that N(Cmin)
- p.16: S (fixed-batch)Figure 14 Left: Each value of the compute budget Cminhas an associated optimal model size N. Optimal
<!-- AI_READING_NOTE_END -->
