---
title: "FreezeAsGuard: Mitigating Illegal Adaptation of Diffusion Models via Selective Tensor Freezing"
authors:
  - "Kai Huang"
  - "Haoming Wang"
  - "Wei Gao"
year: 2024
venue: "arXiv (2405.17472v2)"
doi: 
pdf: [[2024_FreezeAsGuard_Mitig.pdf]]
primary_topic: G_视觉基础模型_VLM_LLM
topics:
  - "G_视觉基础模型_VLM_LLM"
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2024_FreezeAsGuard_Mitig.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/28 pages"
---
# FreezeAsGuard: Mitigating Illegal Adaptation of Diffusion Models via Selective Tensor Freezing

## 基本信息
- **PDF**: [[2024_FreezeAsGuard_Mitig.pdf]]
- **primary_topic**: `G_视觉基础模型_VLM_LLM`
- **topics**: `G_视觉基础模型_VLM_LLM`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | FreezeAsGuard: Mitigating Illegal Adaptation of Diffusion Models via Selective Tensor Freezing |
| **作者** | Kai Huang, Haoming Wang, Wei Gao (University of Pittsburgh) |
| **发表时间** | 2024 (arXiv:2405.17472v2, 27 Nov 2024, Preprint / Under review) |
| **刊物/会议** | arXiv |
| **代码** | https://github.com/pittisl/FreezeAsGuard |
| **DOI** | 未明确 |

## 摘要

清理后的英文原摘要（修复连写/连字符断裂、剔除图轴杂入文字）：

> Text-to-image diffusion models can be fine-tuned in custom domains to adapt to specific user preferences, but such adaptability has also been utilized for illegal purposes, such as forging public figures' portraits, duplicating copyrighted artworks and generating explicit contents. Existing work focused on detecting the illegally generated contents, but cannot prevent or mitigate illegal adaptations of diffusion models. Other schemes of model unlearning and reinitialization, similarly, cannot prevent users from relearning the knowledge of illegal model adaptation with custom data. In this paper, we present FreezeAsGuard, a new technique that addresses these limitations and enables irreversible mitigation of illegal adaptations of diffusion models. Our approach is that the model publisher selectively freezes tensors in pre-trained diffusion models that are critical to illegal model adaptations, to mitigate the fine-tuned model's representation power in illegal adaptations, but minimize the impact on other legal adaptations. Experiment results in multiple text-to-image application domains show that FreezeAsGuard provides 37% stronger power in mitigating illegal model adaptations compared to competitive baselines, while incurring less than 5% impact on legal model adaptations. The source code is available at: https://github.com/pittisl/FreezeAsGuard.

中文翻译：

> 文本到图像扩散模型可以在自定义领域上微调以适配特定用户偏好，但这种适配能力也被用于非法目的，例如伪造公众人物肖像、复制受版权保护的艺术品以及生成不雅内容。现有工作聚焦于检测非法生成的内容，但无法预防或缓解扩散模型本身的非法适配。其他的模型遗忘（unlearning）与重初始化方案同样无法阻止用户用自定义数据重新学习这些非法适配知识。本文提出 FreezeAsGuard，一种新技术，解决了上述局限，能够对扩散模型的非法适配实现**不可逆的缓解**。核心思路是：模型发布者选择性地冻结预训练扩散模型中对非法适配至关重要的张量，从而削弱微调后模型在非法适配上的表征能力，同时最小化对其他合法适配的影响。在多个文本到图像应用领域的实验表明，与有竞争力的基线相比，FreezeAsGuard 在缓解非法模型适配上的能力强 37%，而对合法模型适配的影响小于 5%。源码已开源。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：开源文本到图像扩散模型（如 Stable Diffusion）可被用户用自定义数据方便地微调（如卡通数据集合成游戏头像、风景照生成壁纸），但这种"适配能力的民主化"带来非法滥用风险——伪造公众人物肖像、复制版权艺术品、生成不雅内容(p.1)。
- **之前方法的问题**（论文 Introduction 逐一列举）：
    1.  **版权检测/水印**（copyright detection，向训练数据和生成图像嵌入不可见水印）：只能检测训练数据的滥用，无法缓解用户的非法适配能力；用户用自采集的无水印数据（如自拍的公众人物照片）即可绕过(p.1)。
    2.  **内容过滤**：过滤用户提示词可通过微调使"无害提示"对齐非法图像内容来绕过；过滤生成图像往往误报率高(p.1)。
    3.  **数据投毒**：向训练数据注入不可见扰动避免误报，但当使用公共网络数据或用户私有数据微调时无法应用(p.1)。
    4.  **模型遗忘（Unlearning）**：通过修改模型权重移除非法适配所需知识，但无法阻止通过微调重新学习该知识(p.1)。
- **核心矛盾**：上述方法的关键局限在于它们都聚焦于修改**训练数据或模型权重**，而这种修改可被用户用自己的数据通过微调**逆转**。同时，由于合法类（如用户自己的肖像）与非法类（如公众人物肖像）之间存在高度模糊性和可能的重叠，这种修改无法把缓解能力**仅约束在非法类**而不影响合法类适配(p.1)。
- **技术难点**：如何评估张量在微调中的"重要性"。基于归因（attribution-based）的剪枝重要性度量适用于固定权重值，但无法反映微调中权重变化的影响；由于微调迭代中权重更新的随机性与相互依赖，这种影响无法压缩成单一重要性度量(p.2)。论文据此转向"把冻结张量的选择形式化为一个可训练的二元掩码"。

## 关键贡献

1.  提出 **FreezeAsGuard** 新范式：通过在微调时**约束扩散模型张量的可训练性（selective tensor freezing）**，实现对非法适配的**不可逆**缓解。不同于修改权重的遗忘方案，被冻结的张量从根本上无法被重新学习(p.1, p.2)。
2.  将"在所有非法类中选择需冻结张量"形式化为**一个可训练的二元掩码**，通过**双层优化（bilevel optimization）** 把掩码学习的迭代过程与模型微调的迭代过程结合，使掩码能及时学到微调中权重变化对训练损失的影响(p.2)。
3.  在双层优化中**同时纳入合法类训练样本**，为冻结张量的选择提供"抑制信号"，使学到的掩码跳过对合法类微调重要的张量，从而最小化对合法适配的影响(p.2)。
4.  提出**高效双层优化**策略：内层微调不等待收敛、只跑前几次迭代即反馈给外层；并通过维护 `θ(m)` 与 `θ_d = θ_pre − θ_ft` 两版权重（而非 `θ(m)`、`θ_pre`、`θ_ft` 三版）降低显存(p.5, p.6, Algorithm 1)。
5.  在伪造公众人物肖像、复制版权艺术品、生成不雅内容**三个领域**验证：缓解非法适配的能力比有竞争力的基线（模型遗忘）**强最多 37%**，对合法适配影响**小于 5%**，同时相比全微调节省**最多 48% GPU 显存和 21% 墙钟时间**(p.2)。

## 方法

- **整体框架（图 5）**：FreezeAsGuard 是一个**双层优化**。
    - **外层（Mask Learning Loop，由模型发布者执行）**：学习二元掩码 `m`，决定哪些张量在用户微调时被冻结，目标是削弱模型在非法类上的表征能力、同时不影响合法类。
    - **内层（Simulated User Loop）**：模拟用户对被掩码部分冻结的模型进行微调，最小化非法类与合法类上的扩散损失之和。
- **扩散微调目标（Eq.1）**：给定文本 `y` 与图像 `x`，最小化重构损失 `L_θ = E[‖ε − ε_θ(E(x_t), t, τ(y))‖²₂]`，其中 `E(·)` 是预训练 VAE 编码器，`τ(·)` 是预训练文本编码器，`ε_θ(·)` 是去噪模型（多数扩散模型用 UNet 架构）(p.3)。
- **输入输出**：
    - **输入**：预训练权重 `θ_pre`、（在两类数据上）全微调后的权重 `θ_ft`、非法类数据 `x_illegal`、合法类数据 `x_legal`、指定的冻结张量比例 `ρ`。
    - **输出**：优化后的二元掩码 `m*`，随模型一起发布。
- **关键模块与机制**：
    1.  **张量级冻结掩码 `m`**：在**张量级别**（tensor-level）施加冻结，保证足够粒度且不引入额外计算开销（论文注：多数扩散模型参数量 1B–3.5B，UNet 去噪器至少含 686 个张量）。被掩码的权重表示为 `θ(m) = m ⊙ θ_pre + (1−m) ⊙ θ_ft`（Eq.4）——`m_i=1` 的张量取预训练值（即冻结，等价于不被微调更新），`m_i=0` 的张量取微调值(p.4)。
    2.  **掩码的连续松弛**：`m` 离散不可导，采用连续形式 `m(w) = σ(w/T)`，对可训练张量 `w` 施加 sigmoid；优化结束后将 `m*` 取整为二元值以确保所选张量被完全冻结(p.4-5)。
    3.  **上层（掩码学习，Eq.2/5）**：用线性标量化把多目标转为单目标 `L_upper = −λ₁·L_θ*(m)(x_illegal) + λ₂·L_θ*(m)(x_legal) + L_sparsity`。负号使非法类损失被**最大化**（削弱表征），合法类损失被**最小化**；`(λ₁,λ₂)` 按两类样本数量比例设置以避免数量不均带来的梯度偏置(p.5)。
    4.  **稀疏性约束（Eq.6）**：`L_sparsity = ‖1ᵀm/N − ρ‖²₂`，`N` 为张量数，`1ᵀm/N` 为冻结张量比例；最小化它使实际冻结比例逼近指定的 `ρ`(p.5)。
    5.  **下层（模型微调，Eq.3/7）**：`L_lower = L_θ(m)(x_illegal) + L_θ(m)(x_legal)`，模拟用户在部分冻结下对两类数据微调(p.5)。
    6.  **高效双层优化（图 6 Right）**：朴素做法是每次更新掩码后都把模型微调到收敛再更新掩码（图 6 Left），开销极大。论文观察到微调损失通常在前几次迭代快速下降、之后剧烈波动，因此内层**只跑前几次迭代**即把模型权重与损失反馈给外层，并把微调后的权重继承到下一轮，从而整个优化只需一次微调过程(p.5)。
    7.  **显存优化（Eq.8-10，Appendix A）**：只维护 `θ(m)` 与 `θ_d = θ_pre − θ_ft` 两版权重，通过链式法则把 `θ_pre`、`θ_ft` 从梯度计算中消去。上层掩码更新 `w_i ← w_i − η₁ · ∂L_upper/∂θ(m)_i · θ_d^(i) · (1/T)·σ(w_i/T)·σ(1−w_i/T)`（Eq.8）；下层更新 `θ_d^(i) ← θ_d^(i) + η₂·∂L_lower/∂θ(m)_i·(1−m_i)`（Eq.9）、`θ(m)_i ← θ(m)_i − η₂·∂L_lower/∂θ(m)_i·(1−m_i)²`（Eq.10）(p.5-6)。
- **训练流程（Algorithm 1）**：初始化 `θ_d = θ_pre − θ_ft`、`m = 0`、`θ(m) = θ_ft`；外层 `k=1..K`、内层 `l=1..L` 交替执行：采样 `(x_illegal, x_legal)` → 反向传播得 `∂L_lower/∂θ(m)` → 按 Eq.9/10 更新 `(θ_d, θ(m))`；内层结束后再做上层掩码更新。掩码初始化为全零、`θ(m)` 初始为全微调模型，以缓解过激冻结；论文还给 `w` 设随机负值使连续掩码初始接近零(p.6)。
- **与已有方法的差异**：
    - **vs 模型遗忘（UCE, IMMA）**：遗忘是修改权重"删知识"，可被重新学习；FreezeAsGuard 是**直接限制权重可更新性**，被冻结的张量无法被重学，因此不可逆(p.1, p.2 图1/图2)。
    - **vs 简单分层冻结**：只冻结固定层/组件无效，因为浅层提供主要图像特征、深层提供领域语义，两者对合法类性能都重要；且即便冻结相同数量（如随机 50%），具体分布不同也会影响质量。这种异质性促使论文**在全局张量级别**搜最优冻结组合，把所有组件一并纳入双层优化(p.3-4 表1/图4)。

## 实验

- **数据集**：在三个非法适配领域评估——1) 伪造公众人物肖像；2) 复制版权艺术品；3) 生成不雅内容。每个领域用开源或自采集数据，随机选不同数据类作为非法类与合法类(p.5)。
    - 肖像领域可见的人物：Donald Trump、Elizabeth Warren、Emma Watson、Halle Berry（图2 提示词与训练样本）(p.1-2)。
    - 消融用 captioned pokemon 数据集（表1/图4）(p.3)。
    - （据原文后续页线索，提取缓存未覆盖正文，待核）p.13-14 提到 **FF25 数据集**（以 **FN-L 分数** 度量肖像缓解能力）与 **Artwork 数据集**（以 **CSD 分数** 度量艺术品缓解能力），以及 modern-logo-v4、pokemon 等 HuggingFace 数据集。
- **对比方法（基线）**：有竞争力的**模型遗忘**方案 **UCE** 与 **IMMA**(p.1, p.2 图2)。
- **评价指标**：
    - **图像质量/缓解能力**：CLIP（↑）、TOPIQ（↑）、FID（↓）三项质量指标，以及目标对象的可识别性（视觉对比，图2）(p.3 表1)。（据原文后续页线索，提取缓存未覆盖：肖像用 FN-L、艺术品用 CSD 等专用度量，待核）
    - **对合法适配的影响**：同样的质量指标，对比合法类上全微调与 FreezeAsGuard 微调。
    - **计算效率**：GPU 显存占用与墙钟时间的节省比例(p.2)。
- **主实验结果（来自 Abstract / Introduction 总结性数字）**：
    - **缓解能力**：相比基线（遗忘方案），把微调后模型在非法类上生成图像的质量**进一步降低最多 37%**，并确保生成图像无法被识别为非法类目标对象(p.2)。
    - **合法性影响**：在合法类上与常规全微调相比，质量差异**最多 5%**，基本持平(p.2)。
    - **可视化（图2）**：FreezeAsGuard-30%/70%（FG-30%/FG-70%）处理后的模型即使被非法数据微调也无法生成可识别肖像/艺术品；而 IMMA、UCE 遗忘方案微调后仍能重学并生成(p.2)。
    - **效率**：相比全微调节省**最多 48% GPU 显存和 21% 墙钟计算时间**(p.2)。
- **动机性消融（表1 + 图4，pokemon 数据集，提示词 "a pikachu with a pink dress and a pink bow"）**：冻结不同组件对生成质量的影响——
    | 被冻结组件 | CLIP (↑) | TOPIQ (↑) | FID (↓) |
    |---|---|---|---|
    | 不冻结 | 31.93 | 0.054 | 202.18 |
    | 注意力投影层 (Attention projectors) | 31.60 | 0.051 | 208.40 |
    | 卷积层 (Conv. layers) | 31.54 | 0.047 | 206.58 |
    | 时间嵌入 (Time embeddings) | 31.46 | 0.045 | 212.79 |
    | 随机 50% 权重 (seed 1) | 32.25 | 0.054 | 206.53 |
    | 随机 50% 权重 (seed 2) | 32.62 | 0.051 | 216.12 |
    冻结关键组件（注意力投影、时间嵌入）使质量明显下降；即使随机冻结相同数量（50%），不同 seed 下 FID 差异也很大（206.53 vs 216.12），证明需要"学习获得全局最优冻结掩码"而非固定分层冻结(p.3)。
- **完整定量实验**：（提取缓存仅覆盖 p.1-12，主结果表格、不同非法类数量/不同扩散模型的鲁棒性表、计算成本表均在 p.13 之后，提取未覆盖，待核。据原文后续页线索：Table 5 在 FF25 用 FN-L 衡量不同非法类数量下的缓解能力；Table 6 在 Artwork 用 CSD；Table 7 在 FF25 衡量不同扩散模型；Table 8 在 SD v1.5、NVidia A6000 GPU 上的计算成本。）

## 局限

1.  **行为假设依赖**：方法有效性建立在"大多数非法用户非专业、会遵循模型发布者提供的微调指南从而采用张量冻结"这一假设上(p.2)。论文也以"冻结降低可训练参数、减少计算成本，用户有动机采用"作为采用激励，但若恶意用户故意改代码绕过冻结约束，方法将失效。
2.  **类别需预定义**：需要预先界定并划分"非法类"与"合法类"。现实中非法用途可能多变、难以穷举，且合法/非法类共享知识基（论文以"green beetle = hornet + emerald"为例说明知识可组合共享），增加了精确约束缓解能力的难度(p.3)。
3.  **发布者侧计算成本**：尽管提出了高效双层优化（一次微调过程、两版权重显存优化），双层优化的训练开销仍由模型发布者在发布前承担，高于标准微调或遗忘方法。
4.  **提取覆盖不全**：本笔记的提取缓存仅含 PDF p.1-12（方法与动机完整、定量主结果不完整）。生成不雅内容领域的具体数据集与结果、完整消融、跨非法类数量/跨扩散模型的泛化鲁棒性、与更多 SOTA 的对比，需依据全文（p.13-28）核实(p.5 起)。
5.  **威胁模型范围**：论文主要针对"直接微调攻击"。对更复杂攻击（如反演攻击、提示工程、绕过冻结的工程化手段）的鲁棒性，提取覆盖范围内未给出定量结论，待核。

## 个人评论

> （本节为 AI 评述，非原文结论）

1.  **范式转换**：从"事后检测/可逆的权重修改"转向**"事前预防性、不可逆的可训练性约束"**。把防御点从"权重值"挪到"权重能否被更新"，这是相对遗忘类方法的根本区别，也是"不可逆"宣称的来源——冻结张量在用户侧根本不进入梯度更新，所以无从重学。
2.  **建模优雅**：把"哪些张量在微调中重要"这一难以用单一归因度量刻画的问题，转化为与微调过程动态耦合的双层优化中的可学习二元掩码，绕开了静态重要性度量在微调场景失效的问题，思路扎实。
3.  **兼顾合法/非法**：在外层目标里显式以负号最大化非法类损失、正号最小化合法类损失，并用 `(λ₁,λ₂)` 平衡样本数量——直面"合法与非法类共享知识"这一根本挑战，是方法可用性的关键。
4.  **工程性强**：图6 的"只跑前几次迭代"观察、Eq.8-10 把三版权重压成两版的显存技巧，是让双层优化在 1B-3.5B 扩散模型上跑得动的务实设计，对复现者尤其重要。
5.  **对下游的启发**：
    - **可控生成与安全**：为"选择性削弱/移除特定能力"提供了一条不依赖修改权重值的技术路径。
    - **安全驱动的 PEFT**：选择性冻结本身是一种参数高效微调，本文为它找到了"安全/防滥用"这一新优化目标。
    - **模型发布协议**：提出发布者可在发布前预置防御掩码的新治理模式，对开源模型生态规范有启示。
    - **可质疑处**：防御强度高度依赖"用户遵循冻结指南"的行为假设，威胁模型偏弱；一个能改训练脚本的对手即可解冻，所以更像"提高滥用门槛"而非"密码学意义上的不可逆"。

### 使用建议

- **快速了解**：读 Abstract + Introduction（图1/图2）即可掌握问题、核心思想、三条主结论数字。
- **复现**：精读 Section 3（Eq.2-10）与 Algorithm 1，重点是掩码连续松弛 `m(w)=σ(w/T)`、`θ(m)=m⊙θ_pre+(1−m)⊙θ_ft`、图6 Right 的短周期交替、以及 Eq.8-10 / Appendix A 的两版权重显存优化；代码见 https://github.com/pittisl/FreezeAsGuard 。
- **借鉴创新点**：约束可训练性来防御滥用的范式；用双层优化联合处理"防御目标 + 合法兼容目标"；张量掩码的松弛-离散化与稀疏约束 `L_sparsity`；基于 `θ_d` 的显存技巧。
- **写 Related Work**：可归入 Diffusion Model Safety、Machine Unlearning（作对比基线）、Efficient / Selective Fine-Tuning、Adversarial Robustness 等类。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[G_视觉基础模型_VLM_LLM]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**生成式视觉基础模型（文本到图像扩散模型）的安全与可控性**方向，主题归于 `G_视觉基础模型_VLM_LLM`。它解决的是"如何**预防**扩散模型被非法微调适配"（伪造公众人物肖像、复制版权艺术品、生成不雅内容），而非事后检测或事后遗忘。作者来自 University of Pittsburgh（Kai Huang, Haoming Wang, Wei Gao），论文为 arXiv:2405.17472v2（2024-11-27，Under review），代码开源于 github.com/pittisl/FreezeAsGuard。

## 2. 一句话总结
FreezeAsGuard 让模型发布者在发布前用**双层优化学得一个二元张量掩码**，选择性冻结对非法微调至关重要的张量，使用户即便用非法数据微调也无法重建该能力（不可逆），同时通过把合法类样本纳入优化把对合法适配的影响控制在 5% 以内。

## 3. 背景与问题
- **动机**：开源扩散模型（Stable Diffusion 等）的低门槛微调被滥用，构成社会风险(p.1)。
- **既有方法及其缺陷**：版权水印只测数据滥用、可用无水印自采数据绕过；提示/图像内容过滤可被绕过或误报高；数据投毒对公共/私有数据微调无效；模型遗忘改权重但可被微调重学(p.1)。
- **根本局限**：上述都改"数据或权重值"，可被用户微调**逆转**；且合法与非法类高度重叠，难以只在非法类上施加缓解而不伤合法类(p.1)。
- **技术难点**：基于归因的静态重要性度量无法刻画微调中权重变化的影响（随机性、相互依赖），故论文把冻结张量选择转为可训练掩码 + 双层优化(p.2)。

## 4. 核心贡献
1.  选择性张量冻结约束可训练性 → 对非法适配的**不可逆**缓解(p.1-2)。
2.  把冻结张量选择形式化为**可训练二元掩码**，用双层优化耦合掩码学习与模型微调(p.2)。
3.  把**合法类样本纳入双层优化**作为抑制信号，掩码学会跳过对合法微调重要的张量(p.2)。
4.  **高效双层优化**：内层只跑前几次迭代、权重继承、两版权重（`θ(m)`、`θ_d`）显存优化(p.5-6)。
5.  三领域实验：比基线强 37%，合法影响 <5%，省 ≤48% 显存、≤21% 时间(p.2)。

## 5. 方法详解
- **框架（图5）**：外层 Mask Learning Loop（发布者学掩码 `m`）+ 内层 Simulated User Loop（模拟用户微调）。
- **扩散损失（Eq.1）**：`L_θ = E‖ε − ε_θ(E(x_t), t, τ(y))‖²₂`，UNet 去噪器 + 预训练 VAE 编码器 `E` + 文本编码器 `τ`(p.3)。
- **掩码权重（Eq.4）**：`θ(m) = m ⊙ θ_pre + (1−m) ⊙ θ_ft`；`m_i=1`→冻结取预训练值，`m_i=0`→取微调值；张量级冻结，UNet 至少 686 张量(p.4)。
- **掩码连续松弛**：`m(w) = σ(w/T)`，优化后取整为二元(p.4-5)。
- **上层目标（Eq.2/5/6）**：`L_upper = −λ₁L_θ*(m)(x_illegal) + λ₂L_θ*(m)(x_legal) + L_sparsity`，`L_sparsity = ‖1ᵀm/N − ρ‖²₂`，`(λ₁,λ₂)` 按样本量比例设(p.5)。
- **下层目标（Eq.3/7）**：`L_lower = L_θ(m)(x_illegal) + L_θ(m)(x_legal)`(p.5)。
- **高效优化（图6 Right）**：内层只跑前几次迭代即反馈、微调权重继承到下一轮，整个过程只需一次微调(p.5)。
- **显存优化（Eq.8-10, Appendix A）**：只维护 `θ(m)` 与 `θ_d = θ_pre − θ_ft` 两版，用链式法则消去 `θ_pre/θ_ft`(p.5-6)。
- **算法1**：初始 `θ_d=θ_pre−θ_ft`、`m=0`、`θ(m)=θ_ft`；外层 K 轮、内层 L 步交替更新；`w` 设随机负值使连续掩码近零(p.6)。
- **与遗忘/分层冻结的区别**：遗忘改权重可重学；FreezeAsGuard 限制可更新性不可逆。固定分层冻结无效（浅层=主要特征、深层=领域语义都重要；随机 50% 不同分布质量差异大），故需全局张量级最优冻结(p.3-4 表1/图4)。

## 6. 实验与结果
- **数据集**：三领域——伪造肖像（Trump/Warren/Watson/Berry，图2）、复制艺术品、生成不雅内容；消融用 captioned pokemon。每域随机划分非法/合法类(p.1-3, p.5)。据后续页线索（提取未覆盖，待核）：肖像 FF25 数据集（FN-L 度量）、Artwork 数据集（CSD 度量）。
- **基线**：模型遗忘 UCE、IMMA(p.1-2)。
- **指标**：CLIP↑、TOPIQ↑、FID↓ + 目标对象可识别性（图2）+ 显存/墙钟时间节省(p.2-3)。
- **主结果**（Abstract/Intro 数字）：缓解能力比基线强、把非法类图像质量再降 ≤37%；合法类质量差异 ≤5%；省 ≤48% 显存、≤21% 时间(p.2)。可视化（图2）：FG-30%/FG-70% 微调后仍不可识别，UCE/IMMA 可重学(p.2)。
- **动机消融（表1，pokemon）**：不冻结 CLIP 31.93/TOPIQ 0.054/FID 202.18；冻注意力投影 31.60/0.051/208.40；冻卷积 31.54/0.047/206.58；冻时间嵌入 31.46/0.045/212.79；随机 50% seed1 32.25/0.054/206.53，seed2 32.62/0.051/216.12。结论：冻关键组件质量降，随机同量不同分布差异大 → 需学全局最优掩码(p.3)。
- **完整定量主结果**：在 p.13+，提取未覆盖，待核（据线索：Table 5/6 不同非法类数量、Table 7 不同扩散模型、Table 8 SD v1.5 @A6000 计算成本）。

## 7. 这篇论文真正有价值的地方
1.  **范式转换**：从"事后检测/可逆权重修改"转向"事前、不可逆的可训练性约束"，把防御点从权重值挪到权重能否被更新。
2.  **双层优化建模优雅**：用与微调动态耦合的可学习掩码替代失效的静态重要性度量。
3.  **合法/非法兼容设计**：外层目标显式平衡两类损失，直面共享知识挑战。
4.  **务实工程**：短周期交替（图6）+ 两版权重显存技巧（Eq.8-10）让方法在 1B-3.5B 模型上可行。
5.  **下游启发**：可控生成/能力删除、安全驱动 PEFT、模型发布预置防御的治理新模式。

## 8. 局限与问题
1.  **行为假设强**：依赖"用户遵循冻结指南"，能改训练脚本的对手可解冻——更像提高门槛而非密码学不可逆(p.2)。
2.  **类别需预定义**且合法/非法共享知识，难以穷举与精确约束(p.3)。
3.  **发布者侧训练成本**：双层优化开销仍高于标准微调/遗忘，由发布者承担。
4.  **提取覆盖不全**：缓存仅 p.1-12；生成不雅内容结果、完整消融、跨非法类数量/跨模型泛化、更多 SOTA 对比待全文（p.13-28）核实。
5.  **威胁模型偏窄**：主要针对直接微调攻击，更复杂攻击鲁棒性在覆盖范围内未给定量结论。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Introduction（图1/图2）。
- **复现**：Section 3（Eq.2-10）+ Algorithm 1 + 图6 Right + Appendix A；代码 github.com/pittisl/FreezeAsGuard。
- **借鉴**：约束可训练性防滥用的范式；双层优化联合防御+兼容目标；掩码松弛-离散化 + `L_sparsity`；`θ_d` 显存技巧。
- **写 Related Work**：Diffusion Model Safety、Machine Unlearning（对比基线）、Selective/Efficient Fine-Tuning、Adversarial Robustness。

## 10. 和其他论文的关系
- 主题 `G_视觉基础模型_VLM_LLM`，与扩散模型安全/可控生成工作相关。
- 与**模型遗忘** UCE、IMMA 是直接对比关系(p.1-2)。
- 可关联方向：扩散模型概念擦除/遗忘、文本引导可控生成中的内容安全、参数高效微调（LoRA/Adapter 等选择性训练）。具体库内链接需按实际标题判断，此处为方向性推测。

## 11. 关键词
扩散模型, 文本到图像生成, 非法适配缓解, 模型安全, 选择性张量冻结, 二元掩码, 双层优化, 模型遗忘, 不可逆缓解, 知识产权保护, Stable Diffusion, UCE, IMMA

## 12. 可信度说明
本精读笔记**严格基于 PDF 提取文本**生成；提取缓存覆盖 PDF p.1-12（含 Abstract、Section 1 Introduction、Section 2 Background & Motivation、Section 3 Method 直至 Algorithm 1 上半与 Eq.1-10）。方法动机、双层优化公式、Algorithm 1、表1 消融数值、三条主结论数字（37% / <5% / 48%+21%）、CLIP/TOPIQ/FID 指标、UCE/IMMA 基线、GitHub 链接均**直接来自提取文本**。完整定量主结果表（不同非法类数量/不同扩散模型/计算成本）、生成不雅内容领域细节、FF25/Artwork 数据集与 FN-L/CSD 度量等在 p.13-28，提取**未覆盖**，相关处已标注"据原文后续页线索, 提取缓存未覆盖, 待核"。"## 个人评论"为 AI 评述。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本约 2086 字符/页, 无明显乱码; 方法与公式可逐条核对); 来源缓存: `.paper-cache/extracts/2024_FreezeAsGuard_Mitig.txt` (提取覆盖 p.1-12; 原 AI 主体 12/28 + 全文补读线索 13-28); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-28; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-28。
- **提取情况**: 缺失页 16 页, 其中 16 页提取到可读文本。缺失页包含正文/附录内容, 其中约 4 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Method2 classes 5 classes 10 classes
- p.13: Table 5: Mitigation power in the FF25 dataset, measured by the FN-L score, with different numbers of
- p.13: Method1 class 2 classes 3 classes
- p.13: Table 6: Mitigation power in the Artwork dataset, measured by the CSD score, with different numbers
- p.13: References
- p.13: Class 1
- p.13: Class 2Tensor index
- p.14: Table 7: Mitigation power in the FF25 dataset, measured by the FN-L score, with different diffusion
- p.17: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pages
- p.18: A Vectorizing the Gradient Calculations in Bilevel Optimization
- p.18: PyTorch) maintain model tensors in either list or dictionary-like structures, and hence the gradient
- p.18: In addition, computing gradients over large diffusion models is expensive when using automatic

### 缺失页关键摘录

- p.13: Table 5: Mitigation power in the FF25 dataset, measured by the FN-L score, with different numbers of
- p.13: Table 6: Mitigation power in the Artwork dataset, measured by the CSD score, with different numbers
- p.13: [5]modern-logo-v4 dataset. https://huggingface.co/datasets/logo-wizard/
- p.13: [6]pokemon dataset. https://huggingface.co/datasets/lambdalabs/
- p.13: Figure 12: The frozen tensors for illegal classes on the FF-25 dataset, with ρ=30%
- p.14: Table 7: Mitigation power in the FF25 dataset, measured by the FN-L score, with different diffusion
- p.14: Table 8: Computing cost with FreezeAsGuard- ρon SD v1.5 model, using an NVidia A6000 GPU
- p.14: Figure 13: The frozen tensors for illegal classes on the Artwork dataset, with ρ=70%
- p.15: [27] J. Hessel, A. Holtzman, M. Forbes, R. L. Bras, and Y . Choi. Clipscore: A reference-free evaluation
- p.15: fid: Towards a better evaluation metric for image generation. In Proceedings of the IEEE/CVF
- p.15: quality assessment dataset for perceptual image restoration. In Computer Vision–ECCV 2020:
- p.16: A. Katta, C. Mullis, M. Wortsman, et al. Laion-5b: An open large-scale dataset for training
<!-- AI_READING_NOTE_END -->
