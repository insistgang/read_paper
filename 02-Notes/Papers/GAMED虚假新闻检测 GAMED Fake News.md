---
title: "GAMED: Knowledge Adaptive Multi-Experts Decoupling for Multimodal Fake News Detection"
authors:
  - "Lingzhi Shen"
  - "Yunfei Long"
  - "Xiaohao Cai"
  - "Imran Razzak"
  - "Guanming Chen"
  - "Kang Liu"
  - "Shoaib Jameel"
year: 2025
venue: "WSDM '25 (ACM International Conference on Web Search and Data Mining)"
doi: 10.1145/3701551.3703541
pdf: [[GAMED虚假新闻检测 GAMED Fake News.pdf]]
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
extract_cache: .paper-cache/extracts/GAMED虚假新闻检测 GAMED Fake News.txt
---

# GAMED: Knowledge Adaptive Multi-Experts Decoupling for Multimodal Fake News Detection

## 基本信息
- **PDF**: [[GAMED虚假新闻检测 GAMED Fake News.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | GAMED: Knowledge Adaptive Multi-Experts Decoupling for Multimodal Fake News Detection |
| **作者** | Lingzhi Shen (Southampton), Yunfei Long (Essex), Xiaohao Cai (Southampton), Imran Razzak (MBZUAI / UNSW), Guanming Chen (Southampton), Kang Liu (Southampton), Shoaib Jameel\* (Southampton, 通讯作者) |
| **发表时间** | 2025 (WSDM '25, 2025-03-10 至 14, 德国汉诺威) |
| **刊物/会议** | ACM WSDM '25 — 第十八届 Web 搜索与数据挖掘国际会议 |
| **DOI** | 10.1145/3701551.3703541 |
| **arXiv** | 2412.12164v2 (2025-03-02) |
| **代码** | https://github.com/slz0925/GAMED |

## 摘要

> **清理后英文原摘要**（据 PDF 提取文本整理，修复空格与连字符）:
> Multimodal fake news detection often involves modelling heterogeneous data sources, such as vision and language. Existing detection methods typically rely on fusion effectiveness and cross-modal consistency to model the content, complicating understanding how each modality affects prediction accuracy. Additionally, these methods are primarily based on static feature modelling, making it difficult to adapt to the dynamic changes and relationships between different data modalities. This paper develops a significantly novel approach, GAMED, for multimodal modelling, which focuses on generating distinctive and discriminative features through modal decoupling to enhance cross-modal synergies, thereby optimizing overall performance in the detection process. GAMED leverages multiple parallel expert networks to refine features and pre-embed semantic knowledge to improve the experts' ability in information selection and viewpoint sharing. Subsequently, the feature distribution of each modality is adaptively adjusted based on the respective experts' opinions. GAMED also introduces a novel classification technique to dynamically manage contributions from different modalities, while improving the explainability of decisions. Experimental results on the Fakeddit and Yang datasets demonstrate that GAMED performs better than recently developed state-of-the-art models. The source code can be accessed at https://github.com/slz0925/GAMED.

> **中文翻译**:
> 多模态虚假新闻检测通常需要对视觉与语言等异质数据源进行建模。现有检测方法一般依赖融合的有效性以及跨模态一致性来建模内容，这使得人们难以理解每个模态究竟如何影响预测精度。此外，这些方法主要基于静态特征建模，难以适应不同数据模态之间的动态变化与关系。本文提出了一种全新的多模态建模方法 GAMED，其核心是通过**模态解耦**生成独特且具判别性的特征，以增强跨模态协同，从而优化整个检测过程的整体性能。GAMED 利用多个并行专家网络来精炼特征，并预先嵌入语义知识，以提升专家在信息筛选与观点共享方面的能力；随后根据各专家的意见自适应地调整每个模态的特征分布。GAMED 还引入一种新的分类技术，用于动态管理各模态的贡献，同时提升决策的可解释性。在 Fakeddit 与 Yang 两个数据集上的实验表明，GAMED 优于近期提出的最先进模型。源代码见 https://github.com/slz0925/GAMED。

> **关键词**（论文原列）: Fake News Detection; Multimodal Learning; Pattern Recognition; Mixture of Experts; Explainable AI。
> **CCS 分类**: 计算方法学 → 自然语言处理 (Natural language processing); 计算机视觉 (Computer vision)。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

*   **为什么要做：** 社交媒体时代"人人都是编辑、人人都能发布新闻"，多模态虚假新闻（文本 + 图像协同）成为操纵公众舆论、侵蚀信息信任的强力武器。论文引用 [74] 的定义：假新闻是"刻意编造的、煽情的、情绪化的、误导或虚构的信息，且模仿主流新闻的形式"。
*   **之前方法的问题（引言明确列举）：**
    1.  **基础融合 + 特征抑制：** 传统多模态检测依赖基础融合技术，难以捕捉文本与视觉间的细微互动；许多融合技术存在**特征抑制（feature suppression）** 问题，妨碍模型把握单条内容中文图元素间的"微妙共舞"。
    2.  **过度依赖预训练模型且无精炼步骤：** 流水线中直接使用预训练模型的固有能力、缺少额外的特征表示精炼步骤，容易丢失对分类至关重要的信息。
    3.  **过度依赖一致性：** 现有方法只关注模态间一致性，未把判别性特征作为补充；而现实中造假者已学会绕过"以一致性为中心"的检测模型。
    4.  **黑盒、缺乏可解释性：** 决策过程黑盒，各模态的视角与贡献不透明，损害可解释性与用户信任。
*   **作为靶子的两个近期工作：**
    *   **BMR [69]**：促进深入多模态分析与更优特征提取，但在整合多模态数据、动态加权不同模态方面有困难；多视图表示的自举（bootstrapping）过程损害可解释性；且无法在模型困惑时调用真实世界事实知识作参考。
    *   **LEMMA [65]**（Xuan 等）：结合视觉语言模型与外部知识，但缺乏特征精炼策略，可能引入额外噪声。
*   **核心矛盾：** 如何突破静态特征建模与单一一致性检测的局限，动态、可解释地利用每个模态自身的判别性特征与跨模态协同，以提升检测的鲁棒性与准确性。

## 关键贡献

1.  **模态解耦建模范式：** 基于 modal-decoupling 建模，挖掘跨模态协同潜力来提升检测性能，区别于现有基于一致性学习或纯融合策略 [20,33,54] 的方法。
2.  **专家网络 + AdaIN 的渐进式特征精炼：** 结合专家网络与 AdaIN [26] 的特性进行 progressive feature refinement，得到更具判别性、更独特的特征表示，为多模态数据的动态筛选与优化提供新范式。
3.  **外部语义知识增强：** 论文论证预训练语言模型 [13] 中编码的语义知识图谱信息有助于模型理解假新闻中的复杂关系与上下文，并把这种来自文本的影响扩展到其他模态。
4.  **新型决策方法（否决投票）：** 引入有助于提升决策过程透明度与可解释性的新决策方法。
5.  **实验有效性：** 在公开的 Fakeddit 与 Yang [68] 数据集上取得更好的检测性能。
> 注：原笔记此处还列了"MMoE-Pro 引入 token 注意力 / 放松 softmax 约束"作为独立贡献条；这一点在引言贡献段并未单列，但在方法第 3 节确实描述（见"方法"）。

## 方法

*   **整体框架（图1）：** GAMED 是面向文本与视觉模态的模态解耦设计，流程为：① 从文本和图像提取特征 → ② 用 **MMoE-Pro** 网络模拟"专家评审与意见"以精炼特征表示 → ③ 由 **AdaIN** 自适应机制引导的"分布调整"阶段，动态微调各模态影响、优先处理最相关可靠的数据 → ④ 决策阶段引入结合"共识"与"置信度"两类评估的**否决投票（veto voting）** 系统。整个流程还受益于预训练语言模型编码的语义信息（KE，对结构化如知识图谱与非结构化文本均编码）。Algorithm 1 给出 PyTorch 风格伪代码。
*   **输入与输出：** 输入新闻数据 `N = [I, T] ∈ D`（图像 `I`、文本 `T`、数据集 `D`）；输出真/假二分类。
*   **关键模块：**
    1.  **特征提取：**
        *   **图像模式特征 `f_ip`（IP）**：Inception-ResNet-v2 (IRNv2) [57] 作为提取器，并加入 **BayarConv [7]** 作为早期层，捕捉图像被篡改时留下的细微伪造痕迹（artefacts、光照、纹理），这些痕迹传统卷积不易检测。
        *   **图像语义特征 `f_is`（IS）**：ViT + 掩码自编码器 (MAE) [19,36] 组合，提取图像全局与局部细节；辅以**数据增强 (DA)**（旋转、翻转、缩放）以更好泛化假图像中常见的不一致、增强鲁棒性与数据多样性。
        *   **文本特征 `f_t`（T）**：ERNIE 2.0 [56] 提取。其优势在于建模句子级关系（而不仅是词级）、以及存储于知识图谱中的大规模语义知识，能更好评估文本与图像视觉信息的一致性、分析文本中的事实与实体关系；其结构化知识有助于增强整个架构在跨模态全局协同上的推理能力。
    2.  **专家评审与意见模块 MMoE-Pro（图2左）：** 在传统 MMoE [45] 基础上升级，主要靠两点：
        *   **Token 注意力：** 设输入 `f`（来自 IS、T 或融合 MM 模块）由多个 token 组成，用共享权重 MLP `A` 计算每个 token 的重要性分数 `α_i = A(token_i)`，归一化 `β_i = α_i / Σ_j α_j`，聚合得统一表示 `f̃ = Σ_i β_i · token_i`，从而动态评估不同输入特征的重要性、优化多任务学习中的特征共享。
        *   **放松门控约束：** 解除 softmax 强加的严格非负与归一化约束，专家权重 `w_{t,i}(f)` 直接由原始分数导出，**允许为负或大于 1**（论文认为没有必要强制专家贡献为正）。最终输出
            `MMoE-Pro_t(f) = Σ_{i=1}^{N} w_{t,i}(f̃) · E_i(f)`，其中 `E_i(f)` 为第 i 个专家的输出。
        *   产出的精炼表示 `r` 含 `(r0_is, r1_is)`、`(r0_t, r1_t)`、`(r0_mm, r1_mm)`；其中 `r1_is` 与 `r1_t` 作为融合模块 `f_mm` 的初始特征及该模块专家网络的输入。
        *   **粗预测：** 用 MLP 分类器接收 MMoE-Pro 精炼表示与投影 `f_ip`，对每个 `r` 做 64 维特征降维后输出分类，记 `O = MLP(r)`（粗预测输出）。
    3.  **分布调整 AdaIN（图2右）：** 把粗预测结果转为 AdaIN 可接受的均值/标准差输入，自适应调整特征分布、优先保留最相关可靠的信息。
        *   与标准 AdaIN 不同，`μ` 与 `σ` 由 MLP 生成而非直接从风格特征提取：`μ = MLP_μ(sigmoid(O))`，`σ = MLP_σ(sigmoid(O))`。
        *   调整公式：`e = σ · (r − μ_r)/σ_r + μ`，其中 `μ_r, σ_r` 是输入特征 `r` 的均值与标准差，`e` 为调整后特征；可简记 `e = AdaIN(r, μ, σ)`。
        *   **核心创新（利用"不相关性"）：** 对来自一致性学习的预测输出 `O`，用 `(1 − sigmoid(O))` 反转，从而调整"不相关表示 `r_x → e_x`"的分布。直觉是：煽情语言、冗长背景介绍、复杂修辞等"不相关信息"本身也可作为检测假新闻的线索；因此论文把相关性与一致性学习**解耦**，把不相关性当作协同补充。融合表示 `r_mm` 则直接作为融合模块的调整表示 `e_mm`。
    4.  **否决投票（图3）：** 投票触发前，先把各模态经 AdaIN 的增强表示拼接为 `e_mix`，再经 MMoE-Pro 同样精炼得到 `r_mix` 与 `O_mix`；随后把这个拼接预测输出与各模态先前的粗预测输出一起送入投票阶段。机制结合阈值与置信度，动态管理各模态预测的贡献与冲突。定义高/低置信阈值 `θ_high, θ_low`；对每个模块输出 `O_i` 取 `P_i = sigmoid(O_i)`，拼接输出置信度初始化为 `P_mix = sigmoid(O_mix)`。规则（论文原文）：
        *   **规则1（初始化）：** `P_mix = sigmoid(O_mix)`。
        *   **规则2（替换）：** 若 `P_i > θ_high` 且 `P_i > P_mix`，则用模块 i 的输出替换拼接输出，`P_mix = P_i`。
        *   **规则3（忽略并重考虑）：** 若 `P_i < θ_low` 且模块 i 属于多数类，则忽略多数类的所有输出，并重新考虑所有模块的最大输出，`P_mix = ½(P_mix + max P_i)`。
        *   **规则4（保持）：** 若 `θ_low ≤ P_i ≤ θ_high`，保持 `P_mix` 不变。
*   **训练方式（Algorithm 1）：** 损失 `L_BCE`（二元交叉熵），优化器 AdamW；前向：提取 `f = t, is, ip` → `r = experts(...)`、`r_mm = experts(mm = t + is)` → `O = class(reduc(r0…rn))` → `μ,σ = comp(O, 1−O)` → `e = AdaIN(r,μ,σ)` → `f_mix = concat(e0…en)` → `r_mix = experts(f_mix)` → `O_mix = class(reduc(r_mix))` → `ŷ = veto(O0…On)`；损失 `L = ComputeLoss(O0,O1,…,On)` 基于各模块粗预测计算（伪代码第17行），端到端反向传播。
*   **与已有方法的差异：** 区别于一致性学习/纯融合方法（如 EANN、BMR、LEMMA，及 [20,33,54]）侧重模态解耦与判别性特征增强；相比传统 MMoE 增加 token 注意力并放松门控；创造性把 AdaIN 用于按粗预测动态调整分布、并设计利用"不相关"特征的反向机制；否决投票相比简单平均/求和提供更动态、可解释的决策逻辑。

## 实验

*   **数据集：**
    *   **Fakeddit：** 超过 100 万条带标签样本，平衡划分（628,501 假，527,049 真），来自 22 个 subreddit，领域主题多样；提供细粒度类别，但本文只用 2-way（二分类）标签。划分：训练 563,612 / 验证 58,798 / 测试 59,271。
    *   **Yang：** 20,015 条新闻（11,941 假，8,074 真），假新闻来自 240 多个网站，真新闻来自纽约时报、华盛顿邮报等权威媒体。划分：训练 4,655 / 验证 582 / 测试 583。每条文本配一张图像。
    *   **不可用基准：** Ying 等 [69] 的数据集因 Twitter/Weibo 图像 API 严格限制而不可公开获取，作者联系原作者未果。
*   **实现细节（Settings）：** 图像用两个预训练模型——`mae-pretrain-vit-base`（语义分析）与 `pytorch-InceptionResNetV2`（模式识别）；文本用 `ernie-2.0-base-en`。MAE-ViT 与 ERNIE 隐藏维度均为 768，**参数冻结（frozen）**。图像统一缩放至 224×224；文本与图像数据最大 tokenization 长度均设为 197。所有 MLP 含一个隐藏层 + SiLU 激活。AdamW，学习率 1×10⁻⁴。模型一般在 Fakeddit 上 9–10 epoch、Yang 上 5–7 epoch 达到峰值精度。
*   **评价指标：** 准确率 Acc、召回率 R、精确率 P、F1。
*   **对比方法：** 基线见 Table 1；Fakeddit 上与近期稳健模型对比，文中明确点名 **EANN [62]**（结合 Text-CNN 与 VGG-19，过滤事件特定特征）。**（其余基线列表与全部结果数值：提取缓存在第 25000 字符处截断，未覆盖，待核）**
*   **主实验结果 / 消融 / 定性分析：** 论文第 4 节声明将评估 GAMED 是否优于近期稳健模型、并通过消融研究评估各组件贡献、用定性分析展示决策过程透明度；摘要与引言均称 GAMED 在两数据集上优于近期 SOTA。**（具体的 Table 1 结果数字、消融设置与数据、定性分析图表：提取缓存截断未覆盖，据原文后续页应存在，待核）**
*   **效率信息：** **PDF 提取文本（前 25000 字符）未明确给出 GAMED 的参数量、FLOPs 或推理速度；** 仅知收敛所需 epoch 数（如上）。

## 局限

1.  **模态限制：** 主要处理**文本–图像**双模态，未涉及视频、音频等；对更复杂多模态场景的适用性有待验证（相关工作也明确提到 deepfake 等新形态是该领域开放挑战）。
2.  **计算成本：** 使用多个大型预训练模型（ERNIE 2.0、MAE-ViT、IRNv2）与多个并行专家网络，开销可能较高；不过预训练骨干参数冻结、只训练上层，实际可训练参数量与效率对比在提取文本中未给出。
3.  **数据可获取性：** 部分基准（Ying 等 [69]）因 API 限制不可用，限制了更全面的对比。
4.  **"不相关性"假设的脆弱性：** 把"不相关信息"（煽情语言、复杂修辞等）当作检测线索是核心直觉之一；该假设普适到何种程度、是否可能引入噪声，提取文本未见专门验证（消融可能涉及，但提取缓存截断未覆盖）。
5.  **否决投票机制复杂：** 引入多个超参数（`θ_high, θ_low`）与条件规则，最优设置需调优，边缘情形下规则逻辑的稳健性存疑。
6.  **本笔记证据完整性：** 受提取缓存截断（前 25000/61725 字符）所限，**定量结果表格、消融具体数据、定性分析**均未进入本笔记，无法直接核验"优于 SOTA"的具体幅度与各组件精确贡献。

## 个人评论

1.  **模态解耦范式给出新视角：** 不依赖模态融合、而靠解耦与独立精炼来利用各模态自身判别信息，正面回应了"融合导致特征抑制 / 信息丢失"的痛点，思路对多模态检测有借鉴价值。
2.  **MMoE-Pro 的两点改动很务实：** token 级注意力做特征选择 + 放松 softmax 约束允许负权重，二者结合让专家门控更灵活；"允许负贡献"在直觉上对应"某专家对该任务起抑制/否决作用"，可迁移到其他多专家或多任务筛选场景。
3.  **AdaIN 的迁移用法有巧思：** 把风格迁移里的 AdaIN 改造为"按粗预测动态调整特征分布"，尤其用 `(1−sigmoid(O))` 反转来放大"不相关"线索，是跨领域技术嫁接的范例——但这也是全文最需要消融数据支撑的假设。
4.  **可解释性是真做而非口号：** 显式解耦模态、模拟专家投票、用置信度+阈值规则化决策，确实在透明度上有切实设计；不过四条规则的超参敏感性与失败模式值得在复现时重点关注。
5.  **知识增强落到实处：** 用 ERNIE 2.0 中编码的结构化知识（知识图谱）辅助跨模态推理，对需要事实核查的假新闻任务方向正确。
6.  **阅读提醒：** 本篇关于性能的核心论断目前在本笔记中缺乏数字支撑（提取截断），引用其"优于 SOTA"前应回到原文 Table 1 / 消融表核对。

### 使用建议

*   **快速了解：** 读 Abstract 与 Introduction，即可抓住问题、动机与四阶段框架（解耦特征提取 → MMoE-Pro 专家评审 → AdaIN 分布调整 → 否决投票）。
*   **复现：** 精读 Section 3 "Our Novel GAMED Model"，配合图1（整体框架）、图2（MMoE-Pro 与 AdaIN 细节）、图3（否决投票）与 Algorithm 1。注意 4.1 节实现细节：骨干冻结、224×224、token 长度 197、SiLU、AdamW lr=1e-4。代码已开源（github.com/slz0925/GAMED）。
*   **借鉴创新点：**
    *   多任务学习 / 特征选择：学习 MMoE-Pro 的 token 注意力 + 放松门控（允许负权重）设计。
    *   特征增强 / 分布调整：借鉴 AdaIN 与粗预测结合、以及"不相关性"反向放大思路。
    *   可解释性：参考模态解耦 + 否决投票的决策逻辑。
    *   知识增强 AI：参考把 ERNIE 2.0 语义知识融入多模态流程的方式。
*   **写 Related Work：** 可归入"基于深度学习的多模态假新闻检测""混合专家网络在 NLP/CV 中的应用""自适应特征归一化（AdaIN）在模型改进中的应用""可解释的虚假信息检测"。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**多模态虚假新闻检测**（NLP × CV 交叉，且以 Mixture-of-Experts 为骨架），发表于数据挖掘顶会 **WSDM '25**。它要解决的核心问题是：在融合易导致特征抑制、过度依赖一致性、决策黑盒的现状下，如何**解耦各模态、动态精炼并可解释地决策**。论文 CCS 自我归类为"自然语言处理 + 计算机视觉"，属于多模态 NLP 应用类工作。因此在本知识库的 taxonomy 中，最贴切的是 **T_通用_NLP_其他**（NLP/多模态，非某一具体 CV 主题）。原归类 `B_注意力算子模块` 虽然能对应 MMoE-Pro 的 token 注意力，但那只是子模块，会让本篇与"纯 CV 注意力算子"论文串台，故已改正。

## 2. 一句话总结
GAMED 通过**知识自适应的多专家解耦**：用并行专家网络（MMoE-Pro，含 token 注意力 + 放松门控）对文本/图像/融合特征做渐进精炼，用 AdaIN 按粗预测自适应调整（并反向利用"不相关"线索）特征分布，再用带否决权的投票机制做可解释决策，从而在 Fakeddit 与 Yang 上超过近期 SOTA。

## 3. 背景与问题
*   **为什么要做：** 社媒时代多模态假新闻泛滥，"人人都是编辑"；假新闻定义引自 [74]——刻意编造、煽情、模仿主流新闻形式的误导信息。
*   **之前方法四大问题（引言）：** ① 基础融合存在特征抑制，捕捉不到文图细微互动；② 过度依赖预训练模型固有能力、缺特征精炼步骤，易丢分类关键信息；③ 只看一致性、不用判别特征，而造假者已学会绕过一致性中心模型；④ 决策黑盒、可解释性差、损害用户信任。
*   **靶子工作：** BMR [69]（动态加权与可解释性差、不调用事实知识）、LEMMA [65]（缺特征精炼、可能引噪声）。
*   **核心矛盾：** 突破静态建模与单一一致性，动态且可解释地利用各模态判别特征与跨模态协同。

## 4. 核心贡献
1.  **模态解耦建模范式**，区别于一致性学习/纯融合 [20,33,54]。
2.  **专家网络 + AdaIN 渐进式特征精炼**，得到更具判别性的表示，提供动态筛选与优化的新范式。
3.  **外部语义知识增强**：论证预训练 LM 编码的知识图谱信息有益于理解假新闻复杂关系，并把文本影响扩展到其他模态。
4.  **新型可解释决策方法**（否决投票），提升透明度。
5.  **实验有效性**：Fakeddit 与 Yang 上优于近期 SOTA。
（方法层面另含 MMoE-Pro 的 token 注意力 + 放松 softmax 约束这一技术细节，见第 5 节。）

## 5. 方法详解
四阶段端到端（图1、Algorithm 1）：
*   **① 特征提取：** 图像模式 `f_ip` = IRNv2 [57] + 早期层 **BayarConv [7]**（捕篡改痕迹）；图像语义 `f_is` = ViT+MAE [19,36] + 数据增强（旋/翻/缩）；文本 `f_t` = **ERNIE 2.0 [56]**（句子级关系 + 知识图谱语义）。多模态数据记 `N=[I,T]∈D`。
*   **② 专家评审 MMoE-Pro（图2左）：** token 注意力——`α_i=A(token_i)`、`β_i=α_i/Σα_j`、`f̃=Σ β_i·token_i`；放松门控——权重 `w_{t,i}` 直接由原始分数得到，允许为负或 >1；输出 `MMoE-Pro_t(f)=Σ_{i=1}^N w_{t,i}(f̃)·E_i(f)`（式1）。精炼表示 `r` 含 IS/T/MM 各两份；`r1_is, r1_t` 喂入融合模块 `f_mm`。粗预测 `O=MLP(r)`（先 64 维降维），输入含 MMoE-Pro 表示与投影 `f_ip`。
*   **③ 分布调整 AdaIN（图2右）：** `μ=MLP_μ(sigmoid(O))`、`σ=MLP_σ(sigmoid(O))`（由 MLP 生成而非取自风格特征）；`e=σ(r−μ_r)/σ_r+μ`（式2，`μ_r,σ_r` 为 `r` 的统计量）。对一致性学习输出用 `(1−sigmoid(O))` 反转，调整"不相关表示 `r_x→e_x`"——把煽情/冗长背景/复杂修辞等不相关信息当线索，解耦相关性与一致性。融合表示 `r_mm` 直接作 `e_mm`。
*   **④ 否决投票（图3）：** 拼接增强表示 `e_mix`→ MMoE-Pro 精炼 → `r_mix, O_mix`；与各模态粗预测一起投票。`P_i=sigmoid(O_i)`，`P_mix=sigmoid(O_mix)` 起步。规则1 初始化；规则2 若 `P_i>θ_high` 且 `P_i>P_mix` 则 `P_mix=P_i`；规则3 若 `P_i<θ_low` 且属多数类，则忽略多数类输出、`P_mix=½(P_mix+max P_i)`；规则4 阈值之间则保持。
*   **训练：** `L_BCE` + AdamW，损失 `L=ComputeLoss(O0…On)` 基于各模块粗预测（伪代码17行），端到端。

## 6. 实验与结果
*   **数据集：** Fakeddit（>100 万；628,501 假 / 527,049 真；22 个 subreddit；用 2-way 标签；训/验/测 = 563,612 / 58,798 / 59,271）；Yang（20,015；11,941 假 / 8,074 真；假源自 >240 网站，真源自 NYT、WaPo 等；训/验/测 = 4,655 / 582 / 583）。Ying 等 [69] 数据集因 API 限制不可用。
*   **实现：** mae-pretrain-vit-base + pytorch-InceptionResNetV2 + ernie-2.0-base-en；隐藏维 768、骨干冻结；图像 224×224；token 长度 197；MLP 单隐层 + SiLU；AdamW lr=1e-4；Fakeddit 9–10 epoch、Yang 5–7 epoch 收敛。
*   **指标：** Acc, R, P, F1。
*   **对比方法：** Table 1 给出基线，文中点名 EANN [62]（Text-CNN + VGG-19）。
*   **结果 / 消融 / 定性：** 第 4 节声明含主实验对比、消融评估各组件贡献、定性分析展示决策透明度；摘要与引言称优于近期 SOTA。**具体数字与表格因提取缓存在第 25000 字符截断而未覆盖（原文 61725 字符，据后续页应有，待核）。**
*   **效率：** 提取文本未给出参数量/FLOPs/速度。

## 7. 这篇论文真正有价值的地方
1.  **模态解耦**替代融合，规避特征抑制与信息丢失。
2.  **MMoE-Pro** 的 token 注意力 + 允许负权重门控，是灵活的特征选择/多任务方案。
3.  **AdaIN 反向利用"不相关性"** 作为假新闻线索，是有想象力的跨领域嫁接。
4.  **否决投票** 把可解释性落到规则化、可追踪的决策流程上。
5.  **知识增强**（ERNIE 2.0 知识图谱）支撑跨模态事实推理。

## 8. 局限与问题
1.  仅文本–图像双模态，未及视频/音频/deepfake。
2.  多个大模型 + 并行专家，成本可能高（骨干冻结缓解部分训练成本，但无效率对比）。
3.  部分基准（Ying 等）不可获取，限制全面对比。
4.  "不相关性即线索"假设的普适性与噪声风险，提取文本未见专门验证。
5.  否决投票超参（θ_high, θ_low）与规则的稳健性需调优。
6.  本笔记受提取截断所限，缺定量结果与消融数据，无法核验"优于 SOTA"的幅度。

## 9. 我该怎么使用这篇论文
*   **快速了解：** Abstract + Introduction → 抓住四阶段框架。
*   **复现：** Section 3 + 图1/2/3 + Algorithm 1 + 4.1 实现细节（冻结骨干、224×224、token 197、SiLU、AdamW 1e-4），代码 github.com/slz0925/GAMED。
*   **借鉴：** 多任务/特征选择看 MMoE-Pro；特征增强看 AdaIN 与"不相关性"；可解释性看解耦 + 否决投票；知识增强看 ERNIE 2.0 融入方式。
*   **写 Related Work：** 多模态假新闻检测 / MoE 在 NLP·CV / AdaIN 类自适应归一化 / 可解释虚假信息检测。

## 10. 和其他论文的关系
*   **MMoE (Multi-gate Mixture-of-Experts) [45]：** MMoE-Pro 的直接前身，本文增 token 注意力并放松门控。
*   **AdaIN [26]：** 风格迁移技术，本文改造用于按粗预测调整特征分布。
*   **ERNIE 2.0 [56]：** 文本编码器，代表预训练 LM 知识增强方向；亦呼应 BERT [12]、RoBERTa、GPT-3 [5] 等文本骨干谱系。
*   **VisualBERT [32]、ViLBERT [17]、LXMERT [58]：** 相关工作提到的多模态融合代表，GAMED 用解耦克服其融合丢失判别信息的问题。
*   **BMR [69]、LEMMA [65]、EANN [62]：** 直接对照/批评或对比的多模态假新闻方法。
*   **IRNv2 [57]、ViT+MAE [19,36,28]、BayarConv [7]：** 视觉侧骨干与篡改检测组件。

## 11. 关键词
多模态虚假新闻检测, 混合专家网络 (MoE/MMoE-Pro), 模态解耦, 自适应实例归一化 (AdaIN), token 注意力, 放松门控, 知识增强 (ERNIE 2.0), 否决投票, 可解释 AI, 跨模态协同

## 12. 可信度说明
本精读基于 PDF 提取文本（标注 10/10 页，但 `max_chars=25000`，**实际只覆盖前 25000/61725 字符**，止于第 4.1 节对 EANN 的描述）。
*   **可靠的部分：** 标题/作者/会议/DOI/arXiv/代码、摘要、引言、相关工作、**完整的方法第 3 节（特征提取、MMoE-Pro 全部公式、AdaIN、否决投票四条规则、Algorithm 1）**、以及 4.1 节实验设置（数据集统计、划分、实现超参）——这些均能在提取文本中逐条核到。
*   **未覆盖（截断）：** Table 1 完整基线列表与全部结果数字、消融实验数据、定性分析图表、结论、参考文献。涉及具体性能数字的论断（"优于 SOTA"的幅度、各组件贡献）在本笔记中标注为"据后续页、提取缓存未覆盖、待核"，未编造任何数值。
*   **修正记录：** 本轮把 frontmatter 中被乱码污染的 title/authors/year(原误为2005)/venue 还原为正确值；摘要由乱码直提重建为"清理英文原文 + 中文翻译"；primary_topic 由 `B_注意力算子模块` 改为 `T_通用_NLP_其他`（本质是多模态 NLP 工作，原归类把子模块当主题，易与纯 CV 注意力论文串台）。

---

> **可信度补充**: PDF 提取覆盖 = **partial**（缓存标 10/10 页但受 `max_chars=25000` 截断，仅前 25000/61725 字符；方法第3节与实验设置4.1完整，实验结果表格/消融/结论未覆盖）; 来源缓存: `.paper-cache/extracts/GAMED虚假新闻检测 GAMED Fake News.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮重读修正了 frontmatter 元数据乱码、重建摘要、并改正 primary_topic。
<!-- AI_READING_NOTE_END -->
