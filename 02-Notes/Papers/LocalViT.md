---
title: "LocalViT: Bringing Locality to Vision Transformers"
authors:
  - "Yawei Li"
  - "Kai Zhang"
  - "Jiezhang Cao"
  - "Radu Timofte"
  - "Luc Van Gool"
year: 2021
venue: "arXiv"
doi: 
pdf: [[LocalViT.pdf]]
primary_topic: B_注意力算子模块
topics:
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
extract_cache: .paper-cache/extracts/LocalViT.txt
---

# LocalViT: Bringing Locality to Vision Transformers

## 基本信息
- **PDF**: [[LocalViT.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | LocalViT: Bringing Locality to Vision Transformers |
| **作者** | Yawei Li; Kai Zhang; Jiezhang Cao; Radu Timofte; Luc Van Gool (ETH Zurich / KU Leuven) |
| **发表时间** | 2021 (arXiv:2104.05707v1, 2021-04-12) |
| **刊物/会议** | arXiv preprint |
| **DOI** | 未明确 (arXiv: 2104.05707) |
| **代码** | https://github.com/ofsoundof/LocalViT |

## 摘要

> **清理后英文原摘要**（据 PDF 提取文本修复空格/连字符、剔除杂入的图注）：
>
> We study how to introduce locality mechanisms into vision transformers. The transformer network originates from machine translation and is particularly good at modelling long-range dependencies within a long sequence. Although the global interaction between the token embeddings could be well modelled by the self-attention mechanism of transformers, what is lacking is a locality mechanism for information exchange within a local region. Yet, locality is essential for images since it pertains to structures like lines, edges, shapes, and even objects. We add locality to vision transformers by introducing depth-wise convolution into the feed-forward network. This seemingly simple solution is inspired by the comparison between feed-forward networks and inverted residual blocks. The importance of locality mechanisms is validated in two ways: 1) A wide range of design choices (activation function, layer placement, expansion ratio) are available for incorporating locality mechanisms and all proper choices can lead to a performance gain over the baseline, and 2) The same locality mechanism is successfully applied to 4 vision transformers, which shows the generalization of the locality concept. In particular, for ImageNet2012 classification, the locality-enhanced transformers outperform the baselines DeiT-T and PVT-T by 2.6% and 3.1% with a negligible increase in the number of parameters and computational effort.

> **中文翻译**：
>
> 我们研究如何为视觉 Transformer 引入局部性机制。Transformer 网络源自机器翻译，特别擅长建模长序列中的长程依赖。尽管 token 嵌入之间的全局交互能被自注意力机制很好地建模，但它缺乏一个在局部区域内交换信息的局部性机制。而局部性对图像而言至关重要，因为它关系到线条、边缘、形状乃至物体等结构。我们通过在前馈网络（FFN）中引入深度卷积（depth-wise convolution）来为视觉 Transformer 添加局部性。这个看似简单的方案，源自对前馈网络与倒残差块（inverted residual block）的对比。局部性机制的重要性通过两方面验证：1) 引入局部性时存在大量设计选择（激活函数、层放置位置、扩展比率），所有合适的选择都能在基线之上带来性能增益；2) 同一局部性机制被成功应用于 4 种视觉 Transformer，体现了该局部性概念的可泛化性。具体地，在 ImageNet-2012 分类上，局部性增强后的 Transformer 在参数量和计算量几乎不增加的情况下，分别比基线 DeiT-T 和 PVT-T 高出 2.6% 和 3.1%。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：CNN 凭借卷积滤波器只感受输入局部区域（感受野），并通过堆叠多层逐步扩大有效感受野，天然具备局部性，能学到层次化特征；同时局部、重复的连接相比全连接层节省了大量参数。但 CNN 扩大感受野只能靠叠层。另一条并行路线是用自注意力把全局连通性引入网络——即源自机器翻译的 Transformer，它擅长建模序列中的长程依赖，在视觉任务上已能与 CNN 竞争。处理 2D 图像时，图像先被切成对应 patch 的 token 序列，单层自注意力即可把有效感受野扩展到整张图。
- **之前方法有什么问题**：视觉 Transformer 的问题在于"全局连通性与卷积思想相矛盾"——单纯的全局注意力缺少对邻近像素间局部依赖的建模。已有为 Transformer 补局部性的工作（如 T2T-ViT、改进 tokenization/自注意力的方法）主要聚焦于改进 **tokenization 与自注意力**部分；另一些工作做 CNN 与 Transformer 的混合架构。作者明确指出：**几乎没有工作关注视觉 Transformer 的前馈网络（FFN）**——而标准 FFN 是逐位置（position-wise）变换，token 之间没有信息交互。
- **作者想解决的核心矛盾**：能否在**不增加模型复杂度**的前提下，高效结合 CNN 的局部性与视觉 Transformer 的全局连通性，从而提升性能。

## 关键贡献

论文自述贡献为三点（提取文本 line 116-130）：

1.  **把局部性机制带入视觉 Transformer**：通过在 FFN 中引入深度卷积，得到一个同时含"自注意力做全局关系建模 + 局部性机制做局部信息聚合"的新 Transformer 架构。
2.  **系统分析局部性机制的基本性质**：孤立分析每个组成部分（深度卷积、非线性激活函数、层放置位置、隐藏层维度扩展比率）的影响。
3.  **验证普适性**：把该思想应用到 DeiT、T2T-ViT、PVT、TNT 四种视觉 Transformer，实验表明这一简单技术能很好地泛化到各种 Transformer 架构。
（笔记补充：作者强调实现极简、参数/计算量增加可忽略，但这是上述贡献的属性，原文并未单列为第 4 条贡献。）

## 方法

- **整体框架**：图像分类只用 Transformer 的 encoder。每个 encoder 层含两部分：把一个 token 关联到所有 token 的**自注意力**，以及对每个 token 应用的**前馈网络（FFN）**。LocalViT 不改自注意力、不改位置编码，**只改 FFN**。
- **输入解释（两种等价视角）**：
    - *序列视角*：输入图像 X∈R^{C×H×W} 切成 N = HW/p² 个 token，嵌入维度 d = C·p²，聚合成矩阵 X̂∈R^{N×d}。
    - *格点（lattice）视角*：因 FFN 是逐位置作用于 token 序列 Z∈R^{N×d}，可等价地用 `Seq2Img` 把序列重排回 2D 特征图 Zr∈R^{h×w×d}（h=H/p, w=W/p），恢复 token 间的邻近关系——这正是引入局部性的机会。此时两个全连接层等价于两个 1×1 卷积。
- **关键模块——带局部性的 FFN**：
    - *标准 FFN*（式 2）：`Y = f(Z·W1)·W2`，隐藏维通常按比率 γ=4 扩展；逐位置操作，token 间无交互。
    - *LocalViT 的 FFN*（式 6）：`Yr = f( f(Zr ⊛ Wr1) ⊛ Wd ) ⊛ Wr2`。即结构为 **1×1 Conv → 激活 → k×k 深度卷积(DW, k>1) → 激活 → 1×1 Conv**，再 `Img2Seq` 回序列。深度卷积逐通道地把 k×k 核内特征聚合，提供 FFN 缺失的"相邻像素局部信息聚合"，且在参数与计算上都高效。
    - *灵感来源*：FFN 的"升维-降维"结构与 MobileNetV2 的倒残差块（1×1 → DW → 1×1，中间隐藏维扩展）高度相似，二者**唯一差别就是倒残差块里那一层深度卷积**（图 3）。作者据此"把深度卷积重新引回 FFN"。
- **类 token（class token）处理（3.3 节）**：引入深度卷积需要把序列重排成 2D 特征图，但多出来的 class token 使精确重排不可能。解决办法：每一层都先 `Split` 出 class token，只让 N 个图像 token 过带 DW 的 FFN 得到 Y，class token **不过 FFN**，直接 `Concat(Zcls, Y)` 拼回。论文论证：因为信息交换与聚合只在自注意力部分完成，FFN 仅做逐 token 变换，所以 class token 旁路不会损害整体性能。
- **激活/注意力增强**：DW 之后的非线性"对网络容量很关键，尤其对高效网络"。作者尝试了 **ReLU6、h-swish、SE（squeeze-and-excitation）模块、ECA（efficient channel attention）模块及其组合**。
- **训练方式**：实现基于倒残差块；2D 卷积后接 BatchNorm；移除 FFN 前的 LayerNorm；移除 FFN 后的 path drop。对 T2T-ViT 的 T2T 模块同样改造；TNT 的内层 Transformer FFN 不改；PVT 因 class token 只在金字塔最后阶段引入，故 split/concat 也只在最后阶段做。
- **与已有方法的差异**：不同于"在 Transformer 前加卷积 stem"的混合架构、也不同于"把自注意力改成局部注意力"的做法——LocalViT **保留全局自注意力**，只在 Transformer block 内部的 FFN 里加局部操作，结构更简洁。

## 实验

- **数据集**：ImageNet-2012，1000 类，1.28M 训练图、50K 验证图。
- **训练协议**（与 DeiT 一致）：输入随机裁剪 224×224；交叉熵损失 + label smoothing；weight decay = 0.05；AdamW（momentum 0.9）；训练 300 epoch；batch size = 1024；学习率从 1×10⁻³ 余弦衰减到 1×10⁻⁵；验证用 center crop。
- **评价指标**：Top-1 准确率（%）、参数量 Params（M）、计算量 FLOPs（G）。
- **主实验——局部性的作用（表 1，基于 DeiT-T）**：
    - 扩展比率 γ=4：DeiT-T 72.2 → LocalViT-T（仅改 FFN 操作、**无 DW**）72.5（+0.3，参数/计算量不变）→ LocalViT-T*（**加 DW**, ReLU6）73.7（+1.5，Params 5.7M→5.8M, FLOPs 1.3G 不变）。
    - 扩展比率 γ=6：DeiT-T 73.1 → LocalViT-T（无 DW）74.3（+1.2）→ LocalViT-T*（加 DW）76.1（+3.0，Params 7.5M→7.7M, FLOPs 1.6G）。
    - 结论：仅改 FFN 操作（无 DW、无额外参数/计算）就能小幅涨点（0.3%~1.2%）；引入局部性（DW）后显著涨点（1.5%~3.0%），代价是参数仅微增、计算量近乎不变。
- **消融实验**：
    1.  **激活函数（表 2，基于 LocalViT-T）**：DeiT-T 72.2 为基线。ReLU6 73.7（+1.5）；h-swish 74.4（+2.2）；h-swish+ECA 74.5（+2.3）；h-swish+SE-192 74.8（+2.6）；SE-96 74.8（+2.6）；SE-48 75.0（+2.8）；**SE-4 75.8（+3.6）**（"SE-**" 中的数字是 SE 模块的 reduction ratio；SE-4 准确率最高但 Params 升到 9.4M）。
    2.  **局部性放置位置（表 3，基于 LocalViT-T，参数/计算量几乎相同）**：High(层9-12) 69.1 < Mid(层5-8) 72.1 < Low(层1-4) 73.1 < Low(层1-8) 74.0 < All(全部12层) 74.8。结论：**只放高层反而掉点（69.1 低于基线72.2）；局部性对低层更重要**；放全部层最好（74.8）。
    3.  **隐藏层扩展比率 γ**：γ=6 相比 γ=4 容量更大、精度更高（表 1 中 γ=6 各项均高于 γ=4，但参数与 FLOPs 同步增加）。
- **四项基本结论**（提取文本 line 106-113）：i. 仅深度卷积本身就能提升基线；ii. DW 之后用更好的激活函数能带来显著增益；iii. 局部性机制对**较低层**更重要；iv. 扩展 FFN 隐藏维能增大模型容量、提高分类精度。
- **泛化实验**：摘要明确 LocalViT 在 DeiT-T、PVT-T 上分别 +2.6%、+3.1%（line 33-34）；并将同一机制成功用于 DeiT、T2T-ViT、PVT、TNT 四种架构。T2T-ViT-7/PVT-T/TNT-S 的逐项准确率与 CNN 对比表位于原文 4.4/4.5 节，**(据原文后续页, 提取缓存仅含前 ~25000 字符, 未覆盖, 待核)**。
- **效率信息**：DW 带来的参数增量很小（γ=4 时 5.7M→5.8M；放置消融中 5.78M~5.91M），FLOPs 基本不变（1.3G；放置消融 1.26G~1.28G）；唯一明显增参的是 SE-4（9.4M）。

## 局限

- **任务局限**：提取文本中所有实验均为 **ImageNet 图像分类**；论文虽在 related work 提到 Transformer 已用于检测/分割等，但 LocalViT 本身在检测/分割上的有效性，提取文本未给出实验（**PDF 提取文本未明确**）。
- **数据集单一**：仅在 ImageNet-1k 上验证，跨域（如医学影像等分布差异大的数据）是否同样有效未涉及。
- **对 FFN 结构的强假设**：方法依赖 FFN"先升维再降维"的结构（才能类比倒残差块插入 DW），对 FFN 设计不同的变体可能不直接适用。
- **额外结构开销**：虽称计算增加"可忽略"，但 DW + Seq2Img/Img2Seq 的来回重排，以及最优精度配置 SE-4 把参数从 5.8M 抬到 9.4M，在极端追求效率/移动端的场景仍需权衡。
- **类 token 旁路**：class token 不过 FFN（仅靠自注意力聚合信息），作者实验称"不影响性能"，但这是一项设计取舍，提取文本仅给出经验性论证。

## 个人评论

1.  **思想的启发性**：论文最漂亮的一点是把"FFN ≈ 缺了一层深度卷积的倒残差块"这一观察讲透——一个看似不起眼的等价视角（lattice perspective + Seq2Img），就把 CNN 高效的局部聚合无痛塞进了 Transformer，为"改造 Transformer 而非推倒重来"提供了范式。
2.  **工程实用性高**：只动 FFN、不碰自注意力与位置编码，即插即用，参数/FLOPs 增量在大多数配置下可忽略，却能稳定涨点（DeiT-T +2.6%、PVT-T +3.1%），落地与复现成本都很低。
3.  **研究严谨**：表 1/2/3 把深度卷积、激活函数、放置位置三个变量逐一孤立，结论具体可复现（"无 DW 也能小涨""h-swish/SE 更好""高层单独放反而掉到 69.1，低层更重要"），是后续工作可直接引用的可靠基线认知。
4.  **可商榷处**：SE-4 虽达 75.8% 但参数翻到 9.4M，"精度-效率"的真实代价被主线叙事弱化；class token 旁路的理论依据偏经验。这些是读者复现时值得留意的细节。

### 使用建议

- **如果快速了解**：读 Abstract + Introduction + 图 1/图 3，即可抓住"在 FFN 里加深度卷积引入局部性"的核心思想、动机与结论。
- **如果复现**：重点读 Methodology（第 3 节，尤其式 6 与 class token 的 split/concat）和 4.1 实现细节（BN 替换、移除 LN 与 path drop、训练协议）以及表 1/2/3 的设置。
- **如果借鉴创新点**：核心是"FFN→倒残差块"的等价改造思路；技术细节可参考激活函数（h-swish/SE）选择与"局部性放低层"的结论。
- **如果写 Related Work**：归入"视觉 Transformer 的局部性增强 / CNN 与 Transformer 混合"一类，与 Swin（窗口注意力）、CoAtNet、Conformer 等并列。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的**视觉 Transformer 网络架构设计/算子模块**方向，核心是为视觉 Transformer 补上其缺失的**局部性（locality）机制**：把 CNN 高效的深度卷积（depth-wise convolution）重新引入 Transformer 的前馈网络（FFN）。它提出的是一个**即插即用的算子模块**（locality-enhanced FFN），不改自注意力，可替换 DeiT/T2T-ViT/PVT/TNT 等多种 Transformer 的原始 FFN，因此归类为「注意力算子模块」（B 类）。论文实验全部围绕 ImageNet 图像分类，**未涉及医学图像或分割任务**（此前笔记误归入 `A1_医学图像_分割`，已据正文纠正）。

## 2. 一句话总结
LocalViT 通过在视觉 Transformer 的前馈网络中插入一层深度卷积（类比 MobileNetV2 倒残差块），以几乎不增加参数和计算量的代价为模型引入局部性，在 DeiT/T2T-ViT/PVT/TNT 上稳定涨点（DeiT-T +2.6%、PVT-T +3.1%）。

## 3. 背景与问题
- **为什么要做**：CNN 靠卷积的局部感受野 + 叠层获得层次化特征，天然有局部性但需叠层才能扩大感受野；Transformer 靠自注意力一层就把感受野扩到全图、擅长长程依赖，却缺少对邻近像素局部依赖的建模。"全局连通性与卷积思想相矛盾"，一个自然问题是能否在不增加复杂度的前提下兼得二者。
- **之前方法有什么问题**：已有为 Transformer 补局部性的工作主要改 tokenization 与自注意力，或做 CNN-Transformer 混合架构；**几乎没人动 FFN**。而标准 FFN 是逐位置变换，token 之间零交互。
- **核心矛盾**：在**不显著增加模型复杂度**的前提下，把 CNN 的局部性高效地注入全局建模的视觉 Transformer。

## 4. 核心贡献
1.  **把局部性带入视觉 Transformer**：在 FFN 中引入深度卷积，得到"自注意力（全局）+ 深度卷积（局部）"的新架构。
2.  **孤立分析局部性机制各组件**：深度卷积、非线性激活函数、层放置位置、隐藏维扩展比率的影响逐一单列。
3.  **验证普适性**：同一机制成功应用于 DeiT、T2T-ViT、PVT、TNT 四种视觉 Transformer，泛化性良好。
（实现极简、参数/计算量增加可忽略，是上述贡献的属性，原文未单列为独立第 4 条。）

## 5. 方法详解
- **整体框架**：图像分类只用 encoder，每层 = 自注意力 + FFN。LocalViT **只改 FFN**，自注意力、位置编码不动。
- **两种等价输入视角**：序列视角（token 矩阵 X̂∈R^{N×d}，N=HW/p²，d=C·p²）；格点视角（用 `Seq2Img` 把序列重排为 2D 特征图 Zr∈R^{h×w×d}，恢复 token 邻近关系，全连接层等价于 1×1 卷积）。
- **核心改造（式 6）**：标准 FFN `Y=f(Z·W1)·W2`（隐藏维按 γ=4 扩展，逐位置、无交互）→ LocalViT FFN `Yr=f( f(Zr⊛Wr1) ⊛ Wd ) ⊛ Wr2`，即 **1×1 Conv → 激活 → k×k 深度卷积 → 激活 → 1×1 Conv**，再 `Img2Seq` 回序列。深度卷积逐通道聚合 k×k 邻域，提供 FFN 缺失的局部信息聚合，且参数/计算高效。
- **灵感**：FFN 的"升维-降维"与 MobileNetV2 倒残差块（1×1 → DW → 1×1）几乎一样，**唯一差别就是中间那层深度卷积**（图 3）。
- **class token**：DW 需要 2D 重排，但 class token 多出的维度让精确重排不可能；解决办法是每层 `Split` 出 class token，只让图像 token 过带 DW 的 FFN，class token **旁路**后再 `Concat` 回。论证依据：信息聚合只发生在自注意力，FFN 仅做逐 token 变换，故旁路不损性能。
- **激活/注意力增强**：尝试 ReLU6、h-swish、SE、ECA 及组合；DW 后的非线性对高效网络的容量很关键。
- **实现细节**：基于倒残差块；2D 卷积后加 BN；移除 FFN 前 LayerNorm；移除 FFN 后 path drop；T2T 模块同样改造；TNT 内层 FFN 不改；PVT 仅在金字塔最后阶段做 split/concat。

## 6. 实验与结果
- **数据集 / 协议**：ImageNet-2012（1.28M 训练、50K 验证、1000 类）；DeiT 同款协议（224×224 随机裁剪、交叉熵 + label smoothing、weight decay 0.05、AdamW、300 epoch、batch 1024、lr 1e-3→1e-5 余弦）。
- **指标**：Top-1 acc(%)、Params(M)、FLOPs(G)。
- **表 1（局部性作用，基于 DeiT-T）**：
    - γ=4：DeiT-T 72.2 → 仅改 FFN(无DW) 72.5(+0.3) → 加 DW(ReLU6) 73.7(+1.5)，Params 5.7→5.8M、FLOPs 1.3G 不变。
    - γ=6：DeiT-T 73.1 → 无 DW 74.3(+1.2) → 加 DW 76.1(+3.0)，Params 7.5→7.7M、FLOPs 1.6G。
- **表 2（激活函数，基于 LocalViT-T；基线 72.2）**：ReLU6 73.7(+1.5)；h-swish 74.4(+2.2)；+ECA 74.5(+2.3)；+SE-192 74.8(+2.6)；+SE-96 74.8(+2.6)；+SE-48 75.0(+2.8)；**+SE-4 75.8(+3.6)**（SE-* 为 reduction ratio；SE-4 最高但参数 9.4M）。
- **表 3（放置位置，基于 LocalViT-T）**：High(9-12) 69.1 < Mid(5-8) 72.1 < Low(1-4) 73.1 < Low(1-8) 74.0 < All(全12层) 74.8；参数/FLOPs 几乎不变（5.78-5.91M / 1.26-1.28G）。**只放高层会掉到基线之下，局部性对低层更重要，放全部层最佳。**
- **四点结论**：i. 仅 DW 就能提升基线；ii. DW 后更好的激活带来显著增益；iii. 局部性对低层更重要；iv. 扩展隐藏维提升容量与精度。
- **泛化**：摘要确认 DeiT-T +2.6%、PVT-T +3.1%，并应用于 DeiT/T2T-ViT/PVT/TNT 四种架构；T2T-ViT-7/PVT-T/TNT-S 逐项数字及与 CNN 的对比 **(据原文后续页, 提取缓存仅含前 ~25000 字符, 未覆盖, 待核)**。
- **效率**：DW 参数增量极小（5.7→5.8M）、FLOPs 基本不变；仅 SE-4 把参数抬到 9.4M。

## 7. 这篇论文真正有价值的地方
1.  **"FFN = 缺一层深度卷积的倒残差块"这一洞见**，把 CNN 局部性无痛迁入 Transformer，思路简洁优雅。
2.  **工程极实用**：只改 FFN、即插即用、参数/计算近乎免费，却稳定涨点，复现/落地成本低。
3.  **消融严谨**：DW / 激活函数 / 放置位置三变量逐一孤立，结论具体可复现（含"高层单独放反而掉到 69.1"这种反直觉但有数据支撑的发现），是可靠的基线认知。

## 8. 局限与问题
- **任务局限**：提取文本中实验全在 ImageNet 分类；检测/分割上的有效性 **PDF 提取文本未明确**。
- **数据集单一**：仅 ImageNet-1k，跨域有效性未验证。
- **FFN 结构强假设**：依赖"升维-降维"结构才能类比倒残差块插 DW。
- **效率代价被弱化**：最优精度配置 SE-4 参数 5.8M→9.4M；Seq2Img/Img2Seq 来回重排有额外开销，移动端需权衡。
- **class token 旁路**：仅经验性论证"不影响性能"，是设计取舍。

## 9. 我该怎么使用这篇论文
- **快速了解**：读 Abstract + Introduction + 图 1/图 3。
- **复现**：精读第 3 节（式 6、class token split/concat）与 4.1 实现细节、表 1/2/3 设置。
- **借鉴创新点**：核心是"FFN→倒残差块"的等价改造；细节参考 h-swish/SE 激活与"局部性放低层"的结论。
- **写 Related Work**：归入"视觉 Transformer 局部性增强 / CNN-Transformer 混合"，与 Swin、CoAtNet、Conformer 并列。

## 10. 和其他论文的关系
- **直接基线**：`[[DeiT]]`、`[[PVT]]`、`[[T2T-ViT]]`、`[[TNT]]`（四个被增强的视觉 Transformer）。
- **思想来源**：`[[MobileNetV2]]`（倒残差块、深度卷积）、`[[MobileNetV3]]`（h-swish）、SE / ECA 通道注意力模块。
- **同领域相关**：`[[Swin Transformer]]`（局部窗口注意力）、`[[CoAtNet]]`、`[[Conformer]]`（CNN 与注意力结合）。

## 11. 关键词
视觉 Transformer, 局部性, 深度卷积, 倒残差块, 前馈网络(FFN), 即插即用算子, h-swish, SE/ECA, 图像分类, ImageNet, 消融实验

## 12. 可信度说明
本精读基于 PDF 提取文本（标称 10/10 页，但**缓存被字符截断**：full PDF 44769 字符，缓存仅含前 ~25298 字符，止于 4.3 激活函数节）。已覆盖摘要、引言、相关工作、方法论（含式 1-9 与 class token 处理）、4.1 实现细节、4.2 局部性作用（表 1）、4.3 激活函数（表 2）、表 3 放置位置等内容；所有引用数字（Top-1、Params、FLOPs、各表增益）均直接来自提取文本。**未被缓存覆盖**的部分（T2T-ViT/PVT/TNT 逐项泛化表、与 CNN 的系统对比、结论节）已标注"(据原文后续页, 提取缓存未覆盖, 待核)"。原笔记年份 2012、主题 A1_医学图像_分割 均为明显错误，已据正文更正为 2021、B_注意力算子模块。

---

> **可信度补充**: PDF 提取质量 = **medium** (标称 10/10 页, 但字符截断, 仅前 ~25298/44769 字符进入缓存, 4.4 节起未覆盖); 来源缓存: `.paper-cache/extracts/LocalViT.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
