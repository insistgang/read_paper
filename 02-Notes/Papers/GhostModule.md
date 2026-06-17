---
title: "GhostNet: More Features from Cheap Operations"
authors:
  - "Kai Han"
  - "Yunhe Wang"
  - "Qi Tian"
  - "Jianyuan Guo"
  - "Chunjing Xu"
  - "Chang Xu"
year: 2020
venue: "arXiv (CVPR 2020)"
doi: 
pdf: [[GhostModule.pdf]]
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
extract_cache: .paper-cache/extracts/GhostModule.txt
---

# GhostNet: More Features from Cheap Operations

## 基本信息
- **PDF**: [[GhostModule.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | GhostNet: More Features from Cheap Operations |
| **作者** | Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu |
| **单位** | 华为诺亚方舟实验室 (Noah's Ark Lab, Huawei) · 北京大学 · 悉尼大学 |
| **发表时间** | arXiv:1911.11907v2, 2020-03-13 (CVPR 2020) |
| **刊物/会议** | arXiv (CVPR 2020) |
| **代码** | https://github.com/huawei-noah/ghostnet |
| **DOI** | 未明确 |

## 摘要

**英文原摘要 (据 PDF 提取文本整理, 已修复空格与连字符):**

> Deploying convolutional neural networks (CNNs) on embedded devices is difficult due to the limited memory and computation resources. The redundancy in feature maps is an important characteristic of those successful CNNs, but has rarely been investigated in neural architecture design. This paper proposes a novel Ghost module to generate more feature maps from cheap operations. Based on a set of intrinsic feature maps, we apply a series of linear transformations with cheap cost to generate many ghost feature maps that could fully reveal information underlying intrinsic features. The proposed Ghost module can be taken as a plug-and-play component to upgrade existing convolutional neural networks. Ghost bottlenecks are designed to stack Ghost modules, and then the lightweight GhostNet can be easily established. Experiments conducted on benchmarks demonstrate that the proposed Ghost module is an impressive alternative of convolution layers in baseline models, and our GhostNet can achieve higher recognition performance (e.g. 75.7% top-1 accuracy) than MobileNetV3 with similar computational cost on the ImageNet ILSVRC-2012 classification dataset. Code is available at https://github.com/huawei-noah/ghostnet.

**中文翻译:**

> 在嵌入式设备上部署卷积神经网络 (CNN) 因内存和算力受限而困难。特征图中的冗余是成功 CNN 的一个重要特性, 却很少在网络架构设计中被研究。本文提出一种新颖的 Ghost 模块, 用廉价操作生成更多特征图: 基于一组本征特征图 (intrinsic feature maps), 施加一系列低成本的线性变换, 生成大量能充分揭示本征特征内在信息的 "幽灵 (ghost)" 特征图。该 Ghost 模块是即插即用组件, 可升级现有 CNN。通过堆叠 Ghost 模块设计出 Ghost bottleneck, 进而轻松搭建出轻量级网络 GhostNet。基准实验表明 Ghost 模块是基线模型卷积层的一个出色替代; 在 ImageNet ILSVRC-2012 分类数据集上, GhostNet 在相近算力下取得比 MobileNetV3 更高的识别性能 (如 75.7% top-1 精度)。代码已开源。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 将 CNN 部署到手机、自动驾驶汽车等嵌入式设备时, 面临内存和算力严重受限的挑战。传统 CNN 参数量与计算量巨大, 难以直接部署 (论文给出量化例子: ResNet-50 约 25.6M 参数, 处理一张 224×224 图像需约 4.1B FLOPs)。
- **之前方法的问题**: 1) **模型压缩**方法 (剪枝、低比特量化、张量分解、知识蒸馏) 的性能通常被预训练基线模型 "上界" 所限制 (performance upper bounded by pre-trained baselines)。2) **紧凑模型设计**方法 (Xception/MobileNet 系列用深度可分离卷积、ShuffleNet 用通道混洗) 虽以极少 FLOPs 取得很好性能, 但论文明确指出: 特征图之间的相关性与冗余性 "从未被充分利用 (has never been well exploited)"。
- **核心观察与矛盾**: 训练好的网络中, 特征图存在大量丰富甚至冗余的信息, 这往往保证了对输入的全面理解 (Figure 1 展示 ResNet-50 第一残差组的特征图存在多对相似图, 彼此像 "幽灵", 可通过廉价变换由另一张近似得到)。论文的立场不是 "避免冗余", 而是 **主动拥抱冗余, 但以一种成本高效的方式生成它** (embrace them, but in a cost-efficient way)。

## 关键贡献

1. **提出 Ghost 模块**: 将一个普通卷积层拆为两部分——(a) 用受严格控制数量的普通卷积生成少量 "本征特征图"; (b) 对本征特征图施加一系列廉价线性变换 (实现上用深度卷积) 生成更多 "幽灵特征图", 并行一个恒等映射保留本征特征。在不改变输出特征图尺寸的前提下降低参数量与计算量。
2. **设计 Ghost Bottleneck (G-bneck)**: 专为小型 CNN 设计、由两个 Ghost 模块堆叠的残差瓶颈结构 (类似 ResNet basic block), 可堆叠构建高效网络。
3. **构建 GhostNet**: 基本沿用 MobileNetV3 架构, 将其瓶颈块替换为 Ghost bottleneck; 与 MobileNetV3 不同的是因延迟过大而**不使用 hard-swish**。
4. **提出宽度乘子 (Width Multiplier) α**: 在每层通道数上统一乘以因子 α (记为 GhostNet-α), 模型大小与计算量随约 α² 二次变化, 灵活权衡精度/速度/体积。
5. **实验验证**: 在 CIFAR-10 (模块分析)、ImageNet ILSVRC 2012 (分类)、MS COCO (检测) 上验证 Ghost 模块与 GhostNet 的有效性与相对 MobileNetV3 等 SOTA 轻量模型的优越性。

## 方法

- **整体框架**: GhostNet 由首层标准卷积 (16 个 33 滤波器, stride=2) + 一系列通道逐渐增大的 Ghost bottleneck (按输入特征图尺寸分组为不同 stage, 每个 stage 最后一个 G-bneck 用 stride=2) + 末端的 11 卷积 (960)、全局平均池化 (77)、11 卷积升到 1280 维、FC (1000 类) 构成, 完整结构见论文 Table 1。
  - 注: 论文正文在引述整体架构表与 SE 模块时多次写成 "Table 7", 应为 Table 1 的笔误 (提取文本可见此处行文不一致)。
- **输入输出**: 对 Ghost 模块, 输入 `X ∈ R^(c×h×w)` (c 输入通道, h、w 高宽), 输出 `n` 张特征图 `Y ∈ R^(h'×w'×n)`。
- **关键模块**:
    1. **Ghost 模块** (Figure 2(b)):
        - **主卷积 (Primary Convolution)**: 用 `f0 ∈ R^(c×k×k×m)`、`m ≤ n` 个滤波器对 `X` 卷积, 得 `m` 张本征特征图 `Y' = X * f0` (Eq.2, 略去偏置)。滤波器大小、步长、填充与原卷积 (Eq.1) 一致, 以保持输出空间尺寸 `h'×w'`。
        - **廉价线性操作 (Cheap Linear Operations)**: 对每张本征图 `y'_i` 施加 `s` 个线性操作 `Φ_{i,j}` 生成幽灵图 `y_ij` (Eq.3); 其中第 `s` 个 (最后一个) 为恒等映射, 用于保留本征特征。最终 `n = m × s` 张特征图拼接为输出。线性操作逐通道作用, 成本远低于普通卷积; 实现上用固定核大小 `d×d` 的深度卷积 (论文建议同一模块内用同尺寸核, 如 33 或 55, 以利 CPU/GPU 效率)。
    2. **Ghost Bottleneck (G-bneck)** (Figure 3): 由两个堆叠 Ghost 模块构成的残差块。
        - 第一个 Ghost 模块作为**扩展层 (expansion layer)**, 按扩展比 (expansion ratio) 增加通道数; 第二个 Ghost 模块**减少通道数**以匹配 shortcut。
        - shortcut 连接两个 Ghost 模块的输入与输出。每层后接 BN+ReLU, 但**第二个 Ghost 模块后不加 ReLU** (沿用 MobileNetV2 的做法)。
        - **stride=1** 时为标准残差; **stride=2** 时 shortcut 走下采样层, 并在两个 Ghost 模块之间插入一个 stride=2 的深度卷积 (DWConv) 做下采样; 此时 Ghost 模块内的主卷积用 11 逐点卷积以提效。
- **数学公式直观解释**:
    - Eq.1: 标准卷积 `Y = X * f + b`, FLOPs ≈ `n·h'·w'·c·k·k`, 因 `n`、`c` 常达 256/512 而非常大。
    - Eq.2 & Eq.3: 先用 `m` 个滤波器得 "精简版" 本征图, 再对每张做廉价空间变换 `Φ` 克隆出幽灵副本, 以约 `1/s` 的成本得到 `n` 倍特征图。
    - Eq.4 (加速比) & Eq.5 (压缩比): 在 `d×d` 与 `k×k` 量级相近、`s ≪ c` 的假设下, 加速比 `r_s ≈ (s·c)/(s+c-1) ≈ s`, 压缩比 `r_c` 与之相等, 即理论加速与压缩都近似等于 `s`。
- **训练方式**: CIFAR-10 实验明确 "训练策略紧密遵循 ResNet [16] 的设置, 包括动量、学习率等"; 具体学习率、轮数等数值在提取文本中**未明确给出**。
- **和已有方法的差异** (3.1 节 "Difference from Existing Methods"):
    1. 相比 MobileNet/ShuffleNet 广泛使用的 11 逐点卷积, Ghost 主卷积**核大小可自定义**。
    2. 已有方法先用逐点卷积跨通道、再用深度卷积处理空间; Ghost **流程相反**: 先用普通卷积生成少量本征特征, 再用廉价线性操作扩充通道。
    3. 处理单张特征图的操作**不限于**深度卷积或移位 (shift), 线性操作可有更大多样性。
    4. 用并行**恒等映射显式保留本征特征图**。

## 实验

- **使用数据集**: CIFAR-10 (60,000 张 3232 彩图 / 10 类, 50K 训练 + 10K 测试, 用于模块属性分析)、ImageNet ILSVRC 2012 (>1.2M 训练 + 50K 验证 / 1000 类, 主分类基准)、MS COCO (检测; trainval35k 训练, minival 5K 评测)。
- **对比方法**: VGG-16、ResNet-56 (作替换基线)、MobileNet/ShuffleNet 系列、MobileNetV3 等。
- **评价指标**: Top-1 准确率、参数量 (Weights, M)、FLOPs (M)、推理延迟、MSE 重建误差 (Toy 实验)。
- **Toy 实验 (重建误差, Table 2)**: 取 Figure 1 的红/绿/蓝三对相似特征图, 用 ResNet-50 第一残差块特征, 以一个小深度卷积学习一张到另一张的映射。核大小 `d` 从 1 到 7, MSE (×10⁻³) 均极小 (如红对 d=1 为 4.0, d=7 为 3.2; 绿对约 24~25; 蓝对约 11~12), 证明特征图间存在强相关、冗余图可由少量本征图生成。
- **消融实验 (CIFAR-10, VGG-16)**:
    - **线性操作核大小 d** (固定 s=2, Table 3): VGG-16 基线 15.0M/313M/93.6%。d=1→7.6M/157M/93.5%; **d=3→7.7M/158M/93.7%** (最佳); d=5→7.7M/160M/93.4%; d=7→7.7M/163M/93.1%。d=1 无法引入空间信息, d=5/7 过拟合且算力上升, 故后续采用 **d=3**。
    - **扩展因子 s** (固定 d=3, Table 4): **s=2→7.7M/158M/93.7%** (略超原模型); s=3→5.2M/107M/93.4%; s=4→4.0M/80M/93.0%; s=5→3.3M/65M/92.9%。s 越大压缩/加速越多但精度渐降, 印证 Eq.4/Eq.5; s=2 即把 VGG-16 压缩约 2 倍且精度反超原模型。
- **CIFAR-10 替换实验**: 把 VGG-16、ResNet-56 所有卷积层替换为 Ghost 模块 (记 Ghost-VGG-16、Ghost-ResNet-56), VGG-16 变体用文献 [60] 的常用版本。
- **ImageNet 分类**: GhostNet 在相近算力下取得 **75.7% top-1**, 优于 MobileNetV3 (摘要与引言明确)。
- **MS COCO 检测**: 论文称将 GhostNet 作为 backbone 用于检测基准; **具体数字所在表格落在提取缓存截断之后, 提取文本未覆盖** (原文 45453 字符, 仅前 25000 被缓存)。
- **效率信息**: Ghost-VGG-16 (s=2, d=3) 参数 7.7M (原 15.0M)、FLOPs 158M (原 313M), 压缩与加速约 2 倍, 同时精度 93.7% > 93.6% (Table 3/4)。

## 局限

1. **假设依赖**: 方法有效性建立在 "特征图间存在可被简单线性变换 (深度卷积) 建模的强相关" 这一观察上 (Toy 实验在 ResNet-50 上验证); 在相关性较弱的任务/数据域中, 这种冗余模式可能不同。
2. **实现折中带来的非最优**: 理论上每个线性操作可有不同形状与参数, 但为利于 CPU/GPU 在线推理效率, 论文限制同模块内核同尺寸、`d` 取固定值并统一用深度卷积; 这是工程效率与表达灵活性之间的折中, 实际硬件加速比可能与理论 `s` 有差距 (论文亦指出不规则模块会降低计算单元效率)。
3. **实验设置未尽**: 提取文本未给出完整训练超参 (学习率、轮数等), COCO 检测的详细结果表格落在提取缓存截断之后; 完全复现需查阅原文后续页与开源代码。
4. **适用场景**: 验证集中在图像分类与目标检测, 在语义/实例分割、生成模型等任务上的效果需进一步验证。

## 个人评论

1. **思想的简洁与穿透力**: "特征图冗余是有用的, 但可以廉价生成" 这一命题非常凝练。它把效率优化的视角从 "滤波器/权重层面" 移到 "特征图生成过程" 本身, 并且不是去消除冗余, 而是承认冗余有用、再用低成本造出来——这种 "顺势而为" 的设计哲学比单纯压缩更有启发性。
2. **即插即用 + 完整落地**: Ghost 模块只用普通卷积 + 深度卷积实现, 替换标准卷积层即可, 复现门槛低; 论文还不止于模块, 而是给出 Ghost bottleneck、完整 GhostNet 架构 (Table 1) 与宽度乘子, 形成可直接部署/微调的工程栈。
3. **理论与实验自洽**: Eq.4/Eq.5 推出加速比与压缩比都近似等于 `s`, 而 Table 4 中 s 增大时 FLOPs 单调下降、精度渐降的趋势与理论吻合; Table 2 的 MSE 又为 "可廉价重建" 的前提提供了直接证据。论证链条 (观察→假设→公式→消融) 比较完整。
4. **对后续研究的启示**: 鼓励把网络中间表征的内在结构 (冗余、相关、低秩) 当作架构设计的可利用资源, 而不仅是事后压缩的对象。其 "生成少量本征 + 廉价扩充" 的范式后来也被迁移到注意力、Transformer token 生成等场景。

### 使用建议

- **如果快速了解**: 读 Abstract、Figure 1/Figure 2 (直观理解 Ghost 思想)、Table 1 (整体架构), 以及 4.1 节开头与消融结论 (Table 2/3/4)。
- **如果复现**: 精读 3.1 (Ghost Module, Eq.2/Eq.3) 与 3.2 (Ghost Bottleneck & GhostNet, Figure 3), 按 Table 1 搭网络, 配合官方代码 https://github.com/huawei-noah/ghostnet 验证。注意 d=3、s=2 是论文推荐起点。
- **如果借鉴创新点**: 学习 "把卷积分解为生成本征特征 + 廉价扩充" 的范式, 思考迁移到注意力机制或 Transformer token 生成; Ghost bottleneck (两个 Ghost 模块 + 可选 SE + 残差) 也是优秀可复用结构。
- **如果写 related work**: 归入 "轻量级/高效网络设计"、"模型压缩与加速"、"移动端 CNN 架构", 与 MobileNet 系列、ShuffleNet、Xception、EfficientNet 等并列讨论。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**轻量级/高效卷积神经网络设计**方向 (CVPR 2020, 华为诺亚方舟实验室)。核心是解决算力/内存受限的嵌入式设备上高效部署 CNN 的问题, 提出基础算子 **Ghost 模块** 替代标准卷积层, 以更低参数与 FLOPs 生成同等数量特征图。本库归类标签为 "B_注意力算子模块"——严格说 Ghost 模块不是通过学习权重来加权强调的传统注意力, 而是一种**高效特征生成算子**; 之所以仍归入 B, 是因为该桶涵盖 "算子/模块" 类即插即用结构, Ghost 与 SE 等模块的设计目标 (提升模型效率) 一致, 且 GhostNet 架构本身也在部分 bottleneck 中集成了 SE 模块 (Table 1)。

## 2. 一句话总结
Ghost 模块先用普通卷积生成少量 "本征特征图", 再对每张施加廉价线性变换 (深度卷积) 克隆出 "幽灵特征图" 并保留恒等映射, 以约 1/s 的成本得到 n 倍特征图; 据此堆叠出 Ghost bottleneck 与轻量网络 GhostNet, 在 ImageNet 上以相近算力取得 75.7% top-1, 优于 MobileNetV3。

## 3. 背景与问题
- **为什么要做**: 嵌入式部署 (手机、自动驾驶) 算力内存受限; 传统 CNN 太重 (ResNet-50 约 25.6M 参数、4.1B FLOPs)。
- **之前方法的问题**: 1) 模型压缩 (剪枝/量化/张量分解/蒸馏) 性能被预训练基线上界限制。2) 紧凑模型设计 (MobileNet/ShuffleNet/Xception) 虽 FLOPs 极低, 但特征图间的相关性与冗余 "从未被充分利用"。
- **核心立场**: 成功网络的特征图冗余有用 (Figure 1 中存在多对 "幽灵般" 相似特征图); 不回避冗余而是**以成本高效的方式主动生成它**。

## 4. 核心贡献
1. **Ghost 模块**: 普通卷积拆为 "少量本征卷积 + 廉价线性变换 + 恒等映射", 不改输出尺寸而降参降算。
2. **Ghost Bottleneck**: 两个 Ghost 模块堆叠的残差瓶颈 (扩展层 + 降维层 + shortcut)。
3. **GhostNet**: 沿用 MobileNetV3 架构、替换其瓶颈块、去掉 hard-swish。
4. **宽度乘子 α**: 统一缩放各层通道, 模型大小/算力随约 α² 变化。
5. **多基准验证**: CIFAR-10 / ImageNet / COCO。

## 5. 方法详解
- **整体框架**: 首层 33 标准卷积 (16 滤波器, stride=2) → 通道渐增的 Ghost bottleneck 堆叠 (分 stage, 每 stage 末 stride=2) → 11 卷积 (960) → 77 全局平均池化 → 11 卷积升 1280 维 → FC(1000)。完整结构见 Table 1 (注: 原文多处将该表与 SE 配置误引为 "Table 7", 应为 Table 1 笔误)。
- **Ghost 模块** (Figure 2(b)):
    - 主卷积 Eq.2: `Y' = X * f0`, `f0 ∈ R^(c×k×k×m)`, `m ≤ n`, 超参 (核/步长/填充) 同原卷积以保尺寸。
    - 廉价线性操作 Eq.3: 对每张本征图 `y'_i` 施加 `s` 个操作 `Φ_{i,j}` (第 s 个为恒等映射), 得 `n = m×s` 张; 逐通道、用固定 `d×d` 深度卷积实现。
- **Ghost Bottleneck** (Figure 3): 两 Ghost 模块堆叠; 第一个按 expansion ratio 升维、第二个降维匹配 shortcut; 每层后 BN+ReLU, 第二个 Ghost 后不加 ReLU (循 MobileNetV2)。stride=2 时 shortcut 走下采样, 两 Ghost 间插 stride=2 深度卷积, 主卷积用 11 逐点卷积。
- **复杂度** (Eq.4/Eq.5): 含 1 个恒等 + `n/s·(s-1)` 个 `d×d` 线性操作; 在 `d×d ≈ k×k`、`s ≪ c` 下, 加速比 `r_s ≈ s·c/(s+c-1) ≈ s`, 压缩比 `r_c` 与之相等。
- **与已有方法差异** (3.1 节): ① 主卷积核可自定义 (非必 11); ② 流程相反 (先生本征再扩充通道); ③ 线性操作不限于深度卷积/移位; ④ 并行恒等映射保留本征特征。
- **训练**: CIFAR-10 紧随 ResNet [16] 设置 (动量、学习率等); 具体数值提取文本未明确。

## 6. 实验与结果
- **数据集**: CIFAR-10 (10 类, 50K/10K)、ImageNet ILSVRC 2012 (>1.2M/50K, 1000 类)、MS COCO (trainval35k/minival 5K)。
- **Toy 实验 (Table 2)**: 三对相似特征图用小深度卷积学映射, MSE (×10⁻³) 均极小 (红 3.2~4.0、绿 23.9~25.0、蓝 11.0~12.1), 证明强相关、可廉价重建。
- **消融 d (Table 3, s=2, VGG-16)**: 基线 15.0M/313M/93.6%; d=1 93.5%、**d=3 7.7M/158M/93.7% (采用)**、d=5 93.4%、d=7 93.1%。
- **消融 s (Table 4, d=3)**: **s=2 7.7M/158M/93.7%**、s=3 5.2M/107M/93.4%、s=4 4.0M/80M/93.0%、s=5 3.3M/65M/92.9%; 印证 s 越大压缩越多、精度渐降。
- **ImageNet**: GhostNet 相近算力 **75.7% top-1**, 优于 MobileNetV3。
- **CIFAR-10 替换**: Ghost-VGG-16 / Ghost-ResNet-56 (替换全部卷积层); s=2 时 VGG-16 压缩约 2 倍且精度反超 (93.7% vs 93.6%)。
- **COCO 检测**: 原文有检测实验, 但**具体数字表格落在提取缓存截断之后 (前 25000 字符/共 45453), 提取文本未覆盖, 待核**。

## 7. 这篇论文真正有价值的地方
1. **思想穿透力**: 把效率优化从权重层面移到特征图生成层面, 且 "拥抱冗余 + 廉价生成" 而非消除冗余, 视角独特。
2. **简洁普适**: 仅普通卷积 + 深度卷积实现, 即插即用替换标准卷积, 复现门槛低。
3. **理论-实验自洽**: Eq.4/5 的加速压缩比 ≈ s 与 Table 4 趋势吻合, Table 2 的低 MSE 为前提提供直接证据。
4. **完整工程栈**: 不止模块, 还有 bottleneck、完整 GhostNet、宽度乘子, 可直接部署/微调。

## 8. 局限与问题
1. **假设依赖**: 依赖特征图间可被简单线性变换建模的强相关; 弱相关域可能失效。
2. **实现折中**: 为推理效率限制核同尺寸、`d` 固定、统一深度卷积, 牺牲了线性操作的潜在多样性, 实测加速比可能低于理论 `s`。
3. **细节缺口**: 提取文本无完整训练超参; COCO 详细结果落在缓存截断之后。
4. **任务范围**: 集中分类/检测, 分割与生成等待验证。

## 9. 我该怎么使用这篇论文
- **快速了解**: Abstract + Figure 1/2 + Table 1 + 4.1 节消融结论 (Table 2/3/4)。
- **复现**: 精读 3.1 (Eq.2/3)、3.2 (Figure 3), 按 Table 1 搭网络, 配合官方代码; 起点 d=3、s=2。
- **借鉴创新点**: 迁移 "生成本征 + 廉价扩充" 范式到注意力/Transformer token; 复用 Ghost bottleneck (Ghost×2 + 可选 SE + 残差)。
- **写 related work**: 归 "高效网络设计/模型压缩加速/移动端 CNN", 与 MobileNet、ShuffleNet、Xception、EfficientNet 并列。

## 10. 和其他论文的关系
- `[[MobileNetV3]]`: GhostNet 直接沿用其架构并替换瓶颈块、去 hard-swish; 是主要对比与递进对象 (75.7% > MobileNetV3)。
- `[[ShuffleNet]]` / ShuffleNetV2: 同为轻量网络; GhostNet 的动机部分源于对 ShuffleNet/MobileNet "未充分利用特征冗余" 的观察。
- `[[Squeeze-and-Excitation Networks]]` (SE): 被集成进 GhostNet 部分 bottleneck (Table 1) 做通道注意力, 与 Ghost 模块是互补关系。
- MobileNetV2: Ghost bottleneck 的 "第二个 Ghost 后不加 ReLU" 借鉴自 MobileNetV2 的线性瓶颈做法。

## 11. 关键词
Ghost Module, GhostNet, 轻量级神经网络, 特征图冗余, 本征特征图, 幽灵特征图, 深度可分离卷积, 移动端部署, 模型压缩, MobileNetV3, 宽度乘子, 即插即用算子

## 12. 可信度说明
本精读笔记基于 PDF 提取文本 (10/10 页, 但原文 45453 字符仅前 25000 被缓存, 覆盖到摘要、引言、相关工作、方法 (3.1/3.2 含 Eq.1~5、Table 1~2)、实验设置与 CIFAR-10 消融 (Table 3/4) 直到 4.1.2 节中段)。摘要、ResNet-50 参数量 (25.6M/4.1B)、ImageNet 75.7%、所有 Table 2/3/4 数字、Eq.1~5、Table 1 架构、与已有方法差异等均严格据提取文本核对。**COCO 检测的具体数值、ImageNet 详细对比表、完整训练超参落在提取缓存截断之后, 已标注 "待核"。** 笔记修正了原版三处事实错误: 年份 (原 2012 → 实为 arXiv 2020-03-13 / CVPR 2020)、作者 (原为乱码机构串 → Kai Han 等 6 人)、摘要乱码 (已据提取文本重建)。未编造任何提取文本之外的数字。

---

> **可信度补充**: PDF 提取质量 = **high** (提取清晰, 但原文 45453 字符仅前 25000 入缓存, 后续页未覆盖); 来源缓存: `.paper-cache/extracts/GhostModule.txt` (10/10 页, 文本截断于前 25000 字符); 生成日期: 2026-06-05; 复核优化: 2026-06-18; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
