---
title: "Rewrite the Stars"
authors:
  - "Xu Ma"
  - "Xiyang Dai"
  - "Yue Bai"
  - "Yizhou Wang"
  - "Yun Fu"
year: 2024
venue: "arXiv (arXiv:2403.19967)"
doi: 
pdf: [[StarBlocks.pdf]]
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
extract_cache: .paper-cache/extracts/StarBlocks.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# Rewrite the Stars

## 基本信息
- **PDF**: [[StarBlocks.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Rewrite the Stars |
| **作者** | Xu Ma; Xiyang Dai; Yue Bai; Yizhou Wang; Yun Fu (Northeastern University / Microsoft) |
| **发表时间** | 2024 (arXiv:2403.19967v1, 2024-03-29) |
| **刊物/会议** | arXiv (cs.CV); 后被 CVPR 2024 收录 (据原文 arXiv 标注, 提取缓存未明确会议名, 待核) |
| **DOI** | 未明确 |
| **代码** | https://github.com/ma-xu/Rewrite-the-Stars |

## 摘要

清理后的英文原摘要 (修复空格/连字符断裂, 剔除杂入的图表数字):

> Recent studies have drawn attention to the untapped potential of the "star operation" (element-wise multiplication) in network design. While intuitive explanations abound, the foundational rationale behind its application remains largely unexplored. Our study attempts to reveal the star operation's ability to map inputs into high-dimensional, non-linear feature spaces — akin to kernel tricks — without widening the network. We further introduce StarNet, a simple yet powerful prototype, demonstrating impressive performance and low latency under compact network structure and efficient budget. Like stars in the sky, the star operation appears unremarkable but holds a vast universe of potential. Our work encourages further exploration across tasks, with codes available at https://github.com/ma-xu/Rewrite-the-Stars.

中文翻译:

> 近期研究开始关注网络设计中"星操作"(逐元素乘法)尚未被充分挖掘的潜力。虽然直觉性的解释层出不穷, 但其应用背后的根本原理在很大程度上仍未被探究。本研究试图揭示星操作的一种能力: 在不加宽网络的前提下, 将输入映射到高维非线性特征空间——这与核技巧 (kernel tricks) 类似。我们进一步提出 StarNet, 一个简单却强大的原型网络, 在紧凑结构与高效预算下展现出优异性能与低延迟。正如夜空中的星辰, 星操作看似平平无奇, 却蕴藏着一个广阔的潜在宇宙。本工作鼓励在更多任务上进一步探索, 代码已开源。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 近年来一种新的学习范式逐渐受到关注——通过逐元素乘法 (作者统称为"星操作", star operation, 因乘号 `∗` 形似星星) 来融合不同子空间的特征。这一范式在 NLP (Monarch Mixer、Mamba、Hyena Hierarchy、GLU 等) 与计算机视觉 (FocalNet、HorNet、VAN 等) 中均表现出优异的性能与效率。但其成功的根本原理缺乏深入分析, 大多停留在直觉性解释: FocalNet 认为星操作起调制/门控作用; HorNet 归因于高阶特征; VAN 与 Monarch Mixer 归因于卷积注意力。这些解释缺乏严格分析与有力证据。
- **之前方法的问题**: 主流深度网络模块普遍由"线性投影 (卷积、线性层) + 非线性激活"构成; 自注意力虽强, 但通过点积构造注意力矩阵, 复杂度随 token 数二次增长, 效率不佳。基于星操作的现有方法虽经验有效, 却对"为什么有效"缺乏理论解释。
- **核心矛盾 / 关键观察**: 在一个抽象出的 demo block (两分支各做线性变换, 再用 `∗` 或求和聚合) 上, 保持其他条件不变, 逐元素乘法 (star) 始终优于求和 (sum), 且在网络宽度较窄时优势尤为明显 (图 1)。一个如此简单的操作为何能持续带来显著提升? 其表征能力来自何处?

## 关键贡献

1. **理论揭示**: 通过对星操作进行数学重写, 明确证明它能把输入映射到一个约 `(d√2)²`(即 `(d+2)(d+1)/2`) 维的隐式高维非线性特征空间, 类似多项式核函数, 且无需加宽网络 (增加通道数)。
2. **多层指数增长**: 进一步证明堆叠多层星操作时, 隐式维度以"指数的指数"方式增长——第 l 层达到 `R^((d√2)^(2^l))`, 仅需少量层即可近似无限维。
3. **实证验证**: 构建各向同性网络 DemoNet, 在 ImageNet-1k 上系统对比星操作与求和操作 (图 1、表 2、表 3), 证明星操作在不同宽度/深度下始终更优; 并通过 2D 决策边界可视化 (图 2) 直观展示其与多项式核 SVM 的相似性。
4. **提出 StarNet**: 基于理论洞察提出概念验证网络 StarNet, 设计极简、无需精细调参, 在 ImageNet-1K 上超越多种精心设计的高效模型 (MobileNetv3、EdgeViT、FasterNet 等), 兼具低延迟。
5. **开辟新范式**: 提出"通过隐式高维度提升网络效率"这一区别于现有所有高效网络范式 (深度可分离卷积、特征复用/重用、重参数化、NAS、混合架构等, 见表 1) 的新效率来源。

## 方法

- **整体定位**: 本文核心是理论分析而非提出复杂新框架。方法论是对星操作 `(W1^T X + B1) ∗ (W2^T X + B2)` 进行数学重写。作者抽象出一个 demo block (图 1 左): 两分支各做线性变换, 再用 `∗`(星) 或求和聚合; 由 stem 层 + 多个同构 demo block 堆叠成 DemoNet 用于实证。
- **单层重写 (Sec. 3.1)**: 把权重与偏置合并 (`W=[W; B]`, `X=[X; 1]`), 简化为 `(W1^T X) ∗ (W2^T X)`。在单输出通道、单特征点场景 (`w1, w2, x ∈ R^(d+1)`) 下展开 (公式 1-3):
  `w1^T x ∗ w2^T x = Σ_i Σ_j w1^i w2^j x_i x_j`, 可写成 `(d+2)(d+1)/2` 个不同项 `x_i x_j` 的加权和 (公式 4), 系数 `α(i,j)` 在 `i≠j` 时为 `w1^i w2^j + w1^j w2^i`(公式 5)。除含 `x_{d+1}`(即偏置项) 的项外, 每一项都与 x 呈非线性关系, 因此对应独立的隐式维度。于是: 计算在 d 维空间高效进行, 却隐式得到约 `(d+2)(d+1)/2 ≈ (d√2)²`(当 d≫2) 维的表征, 单层即可大幅放大特征维度且无额外计算开销。这与核函数 (尤其多项式核) 同源。
- **多层堆叠 (Sec. 3.2)**: 令 `O_l` 为第 l 层星操作输出 (公式 6-10), `O_l = W_{l,1}^T O_{l-1} ∗ W_{l,2}^T O_{l-1} ∈ R^((d√2)^(2^l))`。即隐式维度的指数随层数翻倍。例如宽度 d=128 的 10 层各向同性网络, 隐式维度约为 `901024`(原文写法), 可合理近似为无限维。
- **特殊案例 (Sec. 3.3)**: 并非所有星操作都让两分支都做变换。
  - Case I: W1/W2 含非线性激活 (如 Conv2Former、FocalNet)。只要保持通道间通信, 隐式维度数基本不变 (约 `d²/2`), 不影响 3.1 的分析, 故用线性变换演示即可。
  - Case II: `W1^T X ∗ X`(去掉 W2, 如 VAN、SENet 的恒等分支), 隐式维度从约 `d²/2` 降到 `2d`。
  - Case III: `X ∗ X`(GENet-θ⁻ 式无可学习变换), 把 `{x1,...,xd}` 映射到 `{x1·x1,...,xd·xd}`, 仍在 `R^d`。
  - 尽管 Case II/III 单层不显著增维, 但配合线性层 (通道通信) 与跳连, 多层可累积出高隐式维度。星操作常与空间交互 (池化/卷积) 结合 (如 VAN), 已有工作多强调感受野扩大, 却忽视了隐式高维带来的好处。
- **与已有方法的差异**:
  - 与**自注意力**相比: 星操作用隐式多项式核获得高维表征, 避免了 token 间显式点积的二次复杂度。
  - 与传统**线性投影+激活**模块相比: 后者靠显式增加宽度 (通道数) 升维, 星操作在低维计算中隐式升维。
  - 与现有**高效网络范式** (表 1) 相比: StarNet 的"隐式高维度"是一种全新效率来源。

## 实验

- **数据集**: 主要在 ImageNet-1K 上进行。
- **DemoNet 设计**: 各向同性网络, 先用一个卷积层把输入分辨率降为 1/16, 再接一串同构 demo block 提特征; 每个 block 内用星操作或求和聚合两分支特征。实现细节见补充材料 Algorithm 1。
- **对比方法**: (1) DemoNet 内"星操作 vs 求和操作"的受控对比; (2) StarNet 与其他高效网络 (MobileNetv3、EdgeViT、FasterNet 等; 表 1 还列举 ShuffleNet/ShuffleNetv2、GhostNet、EfficientNet/MnasNet、MobileOne/FasterViT、Mobile-Former 等代表各类范式)。
- **评价指标**: Top-1 分类准确率 (%); 延迟 (iPhone13、CPU、GPU)。
- **主实验结果**:
  1. **变宽度 (表 2, 深度固定 12, 步长 32)**: 星操作始终优于求和。宽度 96/128/160/192/224/256/288 下, sum 为 51.1/58.5/62.7/66.2/69.6/71.4/72.5, star 为 57.6/64.0/68.2/71.7/73.9/75.3/76.1, 差距为 6.5/5.5/5.5/5.5/4.3/3.9/3.6。随宽度增加, 增益逐渐缩小。
  2. **变深度 (表 3, 宽度固定 192, 步长 2)**: 深度 10/12/14/16/18/20/22 下, sum 为 63.8/66.3/68.2/68.8/69.9/69.6/70.6, star 为 70.3/71.8/72.9/72.9/73.9/75.4/75.4, 差距为 6.5/5.5/4.7/4.1/4.0/5.8/4.8。随深度增加增益未见类似宽度那样的稳定衰减。
  3. **两点推论**: 表 2 中增益随宽度衰减并非因模型变大 (否则表 3 变深度也应衰减); 这说明星操作本身就在内在地扩张网络维度, 从而削弱了"加宽网络"带来的边际收益。
  4. **StarNet 对比**: StarNet-S4 在 ImageNet-1K 验证集上比 EdgeViT-XS 高 **0.9%** Top-1, 同时在 iPhone13 与 CPU 上快 **3×**, 在 GPU 上快 **2×**。StarNet-S4 自身的绝对 Top-1 数值在提取文本 (前 12 页) 中未明确给出。
- **决策边界可视化 (图 2, 2D Noisy Moon 数据集)**: 相同配置下, 基于星操作的网络决策边界明显优于求和; 与 SVM 相比, 星操作的边界更接近多项式核 SVM, 而非高斯核 SVM——为"星操作 ≈ 多项式核"提供直观证据。
- **效率信息**: 论文强调低延迟优势; StarNet 各变体的具体 FLOPs/参数量在提取缓存覆盖的页面中未完整给出 (据原文后续页 Table 13/14、Figure 8 等含小型变体配置与 block 设计研究, 提取缓存未覆盖, 待核)。

## 局限

1. **理论简化**: 推导基于单输出通道、单特征点的简化场景, 其在完整复杂网络中的完全有效性需更多验证。作者推断星操作"天生更适合高效紧凑网络", 对大模型的提升未在本文探讨。
2. **任务范围**: 主要实验局限于图像分类, 星操作在检测/分割等其他视觉任务或跨模态任务上的有效性有待验证。
3. **非线性影响**: Case I 中作者认为激活函数 (使 W1/W2 非线性) "不改变隐式维度数, 不影响分析", 这一论断给出了直观说明但论证可更充分。
4. **复现细节**: 代码已开源, 但 StarNet 完整训练细节 (学习率、数据增强等) 在提取缓存覆盖的文本段落中未完全展开, 需参考原文补充材料或代码库。

## 个人评论

这篇论文最值得学习的地方在于: 它**从第一性原理出发, 为一种被广泛使用却缺乏深度解释的简单操作 (星操作) 给出了坚实的理论解释**。它把"逐元素乘法"与经典核技巧 (尤其多项式核) 联系起来, 打破了"简单操作没有深度"的刻板印象, 为网络设计提供了一个全新的理论视角——效率不一定来自更窄/更少, 也可以来自"低维计算、隐式高维表征"。

对后续研究者的启发:
1. **研究范式**: 面对反直觉的经验现象 (如"乘法为何稳赢加法"), 应深入数学本质做理论挖掘, 往往能带来更深的理解和新的设计范式。
2. **模型设计**: 设计高效网络时不必一味堆复杂模块 (轻量级注意力等), 一个被正确理解和运用的基础操作 (乘法) 也可能产出更强更简洁的模型。
3. **实验方法**: 用极简 DemoNet 做受控变量实验 + 2D 决策边界可视化, 是验证理论假设的优秀范例; 变宽度/变深度两组对照还被巧妙用来反证"增益并非来自模型变大"。

需要审慎之处: 隐式维度的计数 (如 `(d+2)(d+1)/2`、`901024`) 是组合学意义上的"独立项个数", 与网络实际"可用表达能力"并非等价——大量隐式维度之间高度相关, 真实有效自由度受权重秩约束, 这一层并未在理论中刻画。

### 使用建议

- **如果快速了解**: 重点读**摘要、引言**的贡献部分, 以及第 3 节 "Rewrite the Stars" 的 3.1、3.2 小节, 即可掌握核心理论。
- **如果复现**: 研究第 3 节的推导与第 3.4 节 (实证) 中 DemoNet 的构建方式 (补充材料 Algorithm 1), 以及 StarNet 架构 (图 3, 需结合描述; 详细配置在提取缓存未覆盖的后续页, 待核)。
- **如果借鉴创新点**: 学习其"把简单操作与核技巧类比"的思路, 设计新模块时多问一句"该操作隐式实现了什么表征变换"。星操作可作为即插即用的轻量特征聚合单元。
- **如果写 related work**: 可放在"高效网络设计 (Efficient Networks)"或"网络模块理论分析"类别下, 与 FocalNet、HorNet、VAN、Conv2Former 等并列讨论。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉与高效神经网络架构设计方向, 但落脚点是**对一种基础特征聚合算子 (星操作 / 逐元素乘法) 的理论剖析**。核心问题: 深度网络中"星操作"为何能持续提升性能? 作者把它重写成多项式核形式, 证明其能在低维计算中隐式获得高维非线性表征, 并据此设计极简高效网络 StarNet。归在"注意力算子模块 (B)"主题下是合适的——星操作正是 FocalNet/HorNet/VAN 等调制/门控类模块的数学公约数, 本文给出了它们共享的算子级解释。

## 2. 一句话总结
本文从理论上揭示: 星操作 (逐元素乘法) 能把输入隐式映射到约 `(d√2)²` 维、堆叠 l 层后达 `R^((d√2)^(2^l))` 的高维非线性空间 (类比多项式核), 从而在低维计算中获得高维表征能力, 并据此提出概念验证网络 StarNet。

## 3. 背景与问题
- **为什么要做**: 逐元素乘法 ("星操作") 这一范式在 NLP (Monarch Mixer、Mamba、Hyena、GLU) 与 CV (FocalNet、HorNet、VAN) 中均表现优异, 但成功原因停留在直觉解释 (调制/门控、高阶特征、卷积注意力), 缺乏严格分析与证据。
- **之前方法的问题**: 主流模块是"线性投影 + 非线性激活"; 自注意力靠点积构注意力矩阵, 复杂度随 token 数二次增长。基于星操作的方法虽有效, 却没人解释"为什么有效"。
- **核心矛盾**: 在受控 demo block 上, 逐元素乘法始终优于求和且窄网络时优势更大 (图 1)。如此简单的操作为何稳赢? 其表征能力来自何处?

## 4. 核心贡献
1. **理论揭示**: 重写星操作, 证明其单层隐式维度约 `(d+2)(d+1)/2 ≈ (d√2)²`, 类似多项式核, 无需加宽网络。
2. **多层指数增长**: 堆叠 l 层时隐式维度达 `R^((d√2)^(2^l))`(指数随层数翻倍), 少量层即近似无限维。
3. **实证验证**: DemoNet 在 ImageNet-1k 上证明星操作在各宽度/深度下均优于求和 (图 1、表 2、表 3), 决策边界可视化 (图 2) 佐证其与多项式核 SVM 相似。
4. **提出 StarNet**: 极简概念验证网络, 在 ImageNet-1K 上超越 MobileNetv3、EdgeViT、FasterNet 等并具低延迟。
5. **开辟新范式**: "隐式高维度"作为区别于深度可分离卷积、特征复用、重参数化、NAS、混合架构 (表 1) 的全新效率来源。

## 5. 方法详解
- **整体定位**: 核心是理论分析, 不是提复杂新框架。抽象出 demo block (两分支各线性变换→用 `∗` 或求和聚合), 堆叠成 DemoNet 做实证。
- **单层重写 (Sec. 3.1)**: 合并权重偏置后, `(W1^T X) ∗ (W2^T X)`。单输出通道/单特征点下 (公式 1-3) 展开为 `Σ_i Σ_j w1^i w2^j x_i x_j`, 即 `(d+2)(d+1)/2` 个不同二阶项 `x_i x_j` 的加权和 (公式 4), 系数 `α(i,j)` 在 `i≠j` 时为 `w1^i w2^j + w1^j w2^i`(公式 5)。除含偏置项 `x_{d+1}` 外, 每项都与 x 非线性, 对应独立隐式维度。⇒ 计算在 d 维进行, 表征却在约 `(d√2)²` 维, 单层无额外开销升维, 与多项式核同源。
- **多层堆叠 (Sec. 3.2)**: `O_l = W_{l,1}^T O_{l-1} ∗ W_{l,2}^T O_{l-1} ∈ R^((d√2)^(2^l))`(公式 6-10)。宽度 d=128、10 层时隐式维度约 `901024`, 近似无限维。
- **特殊案例 (Sec. 3.3)**: Case I (W1/W2 含激活, 保持通道通信, 隐式维度约 `d²/2` 不变, 不影响分析); Case II (`W1^T X ∗ X`, 维度由 `d²/2` 降到 `2d`); Case III (`X ∗ X`, `{x_i}→{x_i·x_i}`, 仍 `R^d`)。单层不显著增维的 II/III, 借线性层与跳连可多层累积高维。星操作常与空间交互 (池化/卷积) 结合 (如 VAN)。
- **差异**: vs 自注意力 (隐式核 vs 显式二次点积); vs 线性投影+激活 (隐式升维 vs 显式加宽通道); vs 高效网络范式 (隐式高维度是新效率源)。

## 6. 实验与结果
- **数据集**: ImageNet-1K。
- **DemoNet**: 卷积降分辨率到 1/16 + 同构 demo block 序列; 块内用星或求和聚合两分支 (实现见补充 Algorithm 1)。
- **变宽度 (表 2, 深度=12)**: 宽 96→288, sum 51.1/58.5/62.7/66.2/69.6/71.4/72.5, star 57.6/64.0/68.2/71.7/73.9/75.3/76.1, 差 6.5/5.5/5.5/5.5/4.3/3.9/3.6 (随宽度衰减)。
- **变深度 (表 3, 宽度=192)**: 深 10→22, sum 63.8/66.3/68.2/68.8/69.9/69.6/70.6, star 70.3/71.8/72.9/72.9/73.9/75.4/75.4, 差 6.5/5.5/4.7/4.1/4.0/5.8/4.8 (无类似宽度的稳定衰减)。
- **推论**: 增益随宽度衰减不是因模型变大 (否则变深度也应衰减), 说明星操作内在地扩张了网络维度, 从而削弱"加宽网络"的边际收益。
- **StarNet 对比**: StarNet-S4 比 EdgeViT-XS 高 0.9% Top-1, iPhone13/CPU 快 3×, GPU 快 2×; 其绝对 Top-1 数值在提取文本前 12 页未明确。
- **决策边界 (图 2, 2D Noisy Moon)**: 星操作边界优于求和, 且更贴近多项式核 SVM (而非高斯核 SVM)。

## 7. 这篇论文真正有价值的地方
最值得学习的是它**从第一性原理为一个广泛使用却缺乏解释的简单操作给出坚实理论**, 把逐元素乘法与多项式核技巧打通, 提出"低维计算、隐式高维表征"这一新效率视角。三点启发: (1) 对反直觉的经验现象深入数学本质做理论挖掘; (2) 高效网络不必堆复杂模块, 被正确理解的基础操作也能很强; (3) 用极简 DemoNet + 决策边界可视化做受控验证, 并用变宽/变深两组对照反证"增益非来自模型变大", 是优秀的实证范例。

## 8. 局限与问题
1. **理论简化**: 基于单输出通道/单特征点, 完整网络中的有效性需更多验证; 对大模型的效果未探讨。
2. **任务范围**: 实验局限分类, 检测/分割/跨模态待验证。
3. **非线性影响**: Case I 中"激活不改变隐式维度数"的论断可更充分论证。
4. **复现细节**: 训练超参/增强策略在提取缓存覆盖文本中未完全展开。
5. **维度计数的解读**: `(d√2)²`、`901024` 是组合意义上的独立二阶项个数, 与"实际有效表达能力"不等价 (隐式维度高度相关, 受权重秩约束), 论文未刻画这一点。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言贡献 + 第 3 节 3.1/3.2。
- **复现**: 第 3 节推导 + 3.4 节 DemoNet 构建 (补充 Algorithm 1) + StarNet 架构图 3 (详细配置在提取缓存未覆盖的后续页, 待核)。
- **借鉴创新点**: 学"简单操作 ↔ 核技巧"的类比思路; 把星操作当即插即用的轻量特征聚合单元。
- **写 related work**: 归入"高效网络设计"或"网络模块理论分析", 与 FocalNet/HorNet/VAN/Conv2Former 并列。

## 10. 和其他论文的关系
根据 PDF 中提及的工作, 本文与以下论文直接相关:
- `[[FocalNet]]`、`[[HorNet]]`、`[[VAN]]`、`[[Conv2Former]]`: 使用星操作的代表性视觉网络, 本文为其有效性提供理论解释 (并分别对应其调制/高阶/卷积注意力等直觉解释)。
- `[[MobileNetv3]]`、`[[EdgeViT]]`、`[[FasterNet]]`: StarNet 性能对比的主要高效网络基线。
- `[[ShuffleNet]]`、`[[GhostNet]]`、`[[EfficientNet]]`、`[[MobileOne]]`、`[[Mobile-Former]]`: 表 1 高效网络分类法中代表其他设计范式 (特征 shuffle / 复用 / NAS / 重参数化 / 混合架构)。
- `[[Self-Attention]]`、`[[Kernel Methods]]`(多项式核 / 高斯核): 本文理论对比与类比的重要参照。
- NLP 侧的 `[[Mamba]]`、`[[Monarch Mixer]]`、`[[Hyena Hierarchy]]`、`[[GLU]]`: 引言中作为星操作范式的跨领域例证。

## 11. 关键词
星操作 (star operation)、逐元素乘法、隐式高维特征空间、多项式核技巧、高效网络、StarNet、DemoNet、特征聚合、决策边界可视化、网络架构设计、模型效率。

## 12. 可信度说明
本篇精读笔记主要基于提取缓存覆盖的 PDF 前 12 页 (实际可读内容约到第 4 页正文, 含摘要、引言、相关工作、方法第 3 节全部 (3.1-3.4.2)、表 1-3 数据与图 1/图 2 描述)。表 2/表 3 的全部数值、StarNet-S4 相对 EdgeViT-XS 的 0.9%/3×/2× 结论、隐式维度公式与 901024 数值均直接来自提取文本。StarNet 各变体的绝对 Top-1、FLOPs/参数量、详细架构 (图 3) 及后续消融 (Table 13/14、Figure 5/6/8) 落在提取缓存未覆盖的后续页, 笔记中已逐处标注"未明确"或"提取缓存未覆盖, 待核", 未作编造。摘要原为 PDF 直提乱码 (混入图轴数字、断词), 已据提取文本重建并给出中译。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/StarBlocks.txt` (提取覆盖 12/15 页, 25000 字符截断, 实际可读至正文第 4 页; 原 AI 主体 12/15 + 全文补读 13-15 线索); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: We provide more analyses for the decision boundary visual-
- p.13: Next, our investigation extends to a more in-depth analy-
- p.13: Variant width depth expand Params FLOPs
- p.13: However, the change is not significant due to the intrin-
- p.13: In this section, we explore the performance of StarNet un-
- p.13: In this section, we delve into the performance of StarNet
- p.13: The results presented in Table 14 demonstrate that our
- p.13: StarNet-150 variant still outperforms in both top-1 accuracy
- p.14: ModelTop-1 Params FLOPs Latency (ms)
- p.14: Width 96 128 160 192 224 256 288
- p.14: In most cases, we observe slight performance drop when
- p.14: In our StarNet design, we adopt the ReLU6 activation func-

### 缺失页关键摘录

- p.13: sumstarTrain Acc. 84%Train Acc. 95%Figure 5. 4-run results of sum and star operations.
- p.13: Figure 6. More comprehensive analyses on decision boundary.
- p.13: initial run of the iOS benchmark consistently yields slightly
- p.13: times, and we report the latency of the final run. Although
- p.13: there are minor latency variations when testing on iPhone,
- p.13: Table 13. Configurations of very small StarNets . We vary the
- p.13: demonstrated in Figure 6. The visual results from this ex-
- p.13: small variants are presented in Table 13.
- p.13: very small StarNet variants are detailed in Table 13.
- p.13: The results presented in Table 14 demonstrate that our
- p.13: StarNet-150 variant still outperforms in both top-1 accuracy
- p.14: Figure 8. We provide more studies on the block design of StarNet. Block I is the default design used in our StarNet, and the standard star
<!-- AI_READING_NOTE_END -->
