---
title: "A2-Nets: Double Attention Networks"
authors:
  - "Yunpeng Chen"
  - "Yannis Kalantidis"
  - "Jianshu Li"
  - "Shuicheng Yan"
  - "Jiashi Feng"
year: 2018
venue: "NeurIPS (NIPS) 2018 / arXiv:1810.11579"
doi: 
pdf: [[DA.pdf]]
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
extract_cache: .paper-cache/extracts/DA.txt
---

# A2-Nets: Double Attention Networks

## 基本信息
- **PDF**: [[DA.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A2-Nets: Double Attention Networks |
| **作者** | Yunpeng Chen (NUS); Yannis Kalantidis (Facebook Research); Jianshu Li (NUS); Shuicheng Yan (Qihoo 360 AI Institute / NUS); Jiashi Feng (NUS) |
| **发表时间** | 2018 (arXiv:1810.11579v1, 2018-10-27) |
| **刊物/会议** | NeurIPS / NIPS 2018 (32nd Conference on Neural Information Processing Systems, Montréal) |
| **DOI** | 未明确 (arXiv:1810.11579) |

## 摘要

> **英文原摘要 (据 PDF 提取文本清理)**:
> Learning to capture long-range relations is fundamental to image/video recognition. Existing CNN models generally rely on increasing depth to model such relations which is highly inefficient. In this work, we propose the "double attention block", a novel component that aggregates and propagates informative global features from the entire spatio-temporal space of input images/videos, enabling subsequent convolution layers to access features from the entire space efficiently. The component is designed with a double attention mechanism in two steps, where the first step gathers features from the entire space into a compact set through second-order attention pooling and the second step adaptively selects and distributes features to each location via another attention. The proposed double attention block is easy to adopt and can be plugged into existing deep neural networks conveniently. We conduct extensive ablation studies and experiments on both image and video recognition tasks for evaluating its performance. On the image recognition task, a ResNet-50 equipped with our double attention blocks outperforms a much larger ResNet-152 architecture on ImageNet-1k dataset with over 40% less the number of parameters and less FLOPs. On the action recognition task, our proposed model achieves the state-of-the-art results on the Kinetics and UCF-101 datasets with significantly higher efficiency than recent works.

> **中文翻译**:
> 捕捉长程关系是图像/视频识别的根本性问题。现有 CNN 模型通常依赖增加深度来建模此类关系，效率极低。本文提出"双重注意力块"（double attention block），一种新型组件，它从输入图像/视频的整个时空空间中聚合并传播富含信息的全局特征，使后续卷积层能够高效地访问整个空间的特征。该组件由分两步的双重注意力机制构成：第一步通过**二阶注意力池化**（second-order attention pooling）将整个空间的特征汇聚成一个紧凑集合；第二步通过另一个注意力机制**自适应地选择并将特征分配**到每个位置。该模块易于采用，可方便地嵌入现有深度神经网络。我们在图像与视频识别任务上做了大量消融实验。在图像识别任务上，配备双重注意力块的 ResNet-50 在 ImageNet-1k 上超过了体量大得多的 ResNet-152，且参数量减少 40% 以上、FLOPs 更低。在动作识别任务上，所提模型在 Kinetics 与 UCF-101 数据集上取得了当时的 SOTA 结果，效率显著高于近期工作。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：CNN 受其卷积算子的固有限制——卷积算子专注于捕捉局部特征与关系（例如 7×7 邻域），在建模**长程相互依赖**（long-range interdependencies）方面效率低下。理解全局上下文是图像/视频识别的根本需求。
- **堆叠卷积的弊端**：堆叠多个卷积算子虽能扩大感受野，但实践中带来三个问题——1) 模型不必要地变深变大，计算和内存成本升高、过拟合风险增加；2) 远处特征要穿过一叠层才能影响某位置，前向/反向传播路径都长，优化困难；3) 远距离位置看到的是来自后几层的"延迟"特征，推理低效。
- **近期工作的不足（论文明确指出）**：近期工作 [11, 25] 只能部分缓解上述问题，要么**不够灵活**（[11] 即 SENet，对所有位置分配相同的全局特征），要么**计算开销大**（[25] 即 Non-local Net）。
- **核心目标**：引入一种新组件，使一个卷积层能**立即**感知其相邻层提供的整个时空空间——先从整个空间汇聚关键特征到一个紧凑集合，再自适应地分配到各位置，从而即便没有大感受野，后续卷积层也能感知全局。
## 关键贡献

论文在引言末尾明确列出三点贡献：

1.  **通用公式框架**：提出一个通过通用的"聚合"（gathering）与"分配"（distribution）函数来捕捉长程特征相互依赖的通用公式 `z_i = F_distr(G_gather(X); v_i)`（式 (1)）。
2.  **双重注意力块（A2-block）**：基于该公式实现的高效架构，捕捉**二阶特征统计量**并做**自适应特征分配**。它能以低计算和内存开销建模长程依赖，同时显著提升图像/视频识别性能。
3.  **广泛实验验证**：在 ImageNet-1k、Kinetics、UCF-101 三个公开基准上，通过大量消融实验与 SOTA 对比验证其优越性。图像识别中，配 A2-block 的 ResNet-50 以减少 40% 以上参数量、更少 FLOPs 超越更深的 ResNet-152。
## 方法

- **整体框架**：双重注意力块（A2-block）是一个可插入现有深度网络（如 ResNet）的即插即用组件，核心思想是**先聚合（gather），后分配（distribute）**。图 2 给出其在深度网络中的计算图，所有卷积核大小均为 1×1×1。
- **输入与输出**：
    - **输入**：时空特征张量 `X ∈ R^{c×d×h×w}`，`c` 为通道数，`d` 为时间维度（2D 图像时 `d=1`），`h, w` 为空间维度。每个时空位置 `i = 1,...,dhw` 有局部特征 `v_i`。
    - **输出**：增强后的特征 `Z`；末端额外加一层卷积**扩展通道数**，使 `Z` 可通过逐元素相加（element-wise addition）残差式地编码回输入 `X`。
- **第一步——特征聚合（二阶注意力池化）**：
    - 论文先回顾双线性池化 `G_bilinear(A,B) = A B^T = Σ_i a_i b_i^T`（式 (2)），并重写为 `g_i = A b_i^T = Σ_j b_ij a_j`（式 (3)）——揭示双线性池化的输出 `G` 实际是一**袋视觉基元（bag of visual primitives）**，每个基元 `g_i` 由 `b_i` 加权汇聚局部特征得到。
    - 对 `B` 施加 softmax 使 `Σ_j b_ij = 1`（合法注意力权重），得到**二阶注意力池化**：`g_i = A · softmax(b_i)^T`（式 (4)）。实现上 `A = φ(X; W_φ)`、`B = softmax(θ(X; W_θ))`，二者由两个不同卷积层从 `X` 变换而来。
    - **直观解释**：当 `b_i` 在所有位置密集激活时，`g_i` 捕捉全局特征（如纹理、光照）；当 `b_i` 仅在特定区域稀疏激活时，`g_i` 捕捉特定语义（如物体、部件）。论文不施加任何低秩约束（区别于 [7] 的 rank-1 近似）。
- **第二步——特征分配（自适应软注意力）**：
    - 区别于 SENet 把同一份汇聚后的全局特征分给所有位置，A2 按每个位置 `v_i` 的需求**自适应分配一袋视觉基元**：`z_i = Σ_j v_ij g_j = G_gather(X) · v_i`，其中 `Σ_j v_ij = 1`（式 (5)）。实现上对 `v_i` 做 softmax 归一化（实验发现收敛更好），`V = softmax(ρ(X; W_ρ))`。
- **完整双重注意力（式 (6)，左结合）**：将式 (4)(5) 代入式 (1)：
  `Z = [φ(X; W_φ) · softmax(θ(X; W_θ))^T] · softmax(ρ(X; W_ρ))`。
  特征 `A, B, V` 由三个不同卷积层从 `X` 生成（必要时接 softmax），`Z` 经两次带 reshape/转置的矩阵乘得到。
- **左结合 vs 右结合（关键效率分析，式 (7)）**：两种结合**数学上等价**但成本不同。左结合第二次矩乘复杂度 `O(mn·dhw)`，右结合为 `O(m·(dhw)^2)`；中间结果内存分别为 `mn` 与 `(dhw)^2`。论文举例：`32×28×28` 帧、512 通道的输入在右结合下可轻易耗费 >2GB，而左结合仅约 1MB（论文给出 mn 约 218MB / (dhw)^2 约 218MB 的对照量级，并指出常见情况 `(dhw)^2 > nm` 时应用左结合）。
- **训练方式**：未提特殊策略；训练时损失梯度可由自动微分（auto-gradient）按链式法则轻松计算，随主干端到端训练。
- **和已有方法的差异**：
    - **vs SENet [11]**：A2 受 SENet "聚合-分配"思想启发，但式 (1) 是更一般的形式。SENet 用一阶全局平均池化聚合、把**单个**全局特征分给所有位置（忽略各位置不同需求）；A2 用二阶注意力池化聚合、为每位置**自适应分配不同子集**。
    - **vs Non-local Net [25] / Transformer [24]**：右结合形式可由 NL-Net 解释——第一次乘法捕捉局部特征间成对关系，输出 `dhw×dhw` 关系矩阵。差异在成对关系函数：A2 用 `softmax(θ(X))^T · softmax(ρ(X))`，而非 NL-Net 的 Embedded Gaussian。论文指出 Embedded Gaussian NL-Net 在数学上等价于 [24] 的 self-attention，故对 NL-Net 的结论可外推到 Transformer。
## 实验

- **数据集**：图像识别 ImageNet-1k；视频动作识别 Kinetics、UCF-101。
- **主干网络（表 1）**：视频任务用三种残差网络——ResNet-26（7.043M 参数, 8.3G FLOPs）、ResNet-29（7.620M, 9.2G）、ResNet-50（33.4M, 31.3G）。消融全部用 ResNet-26，ResNet-29 作为基线之一；ResNet-50 几乎是 ResNet-26 的约 2 倍深宽，仅在与 SOTA 对比时使用。图像任务用同款 ResNet-50（去掉时间维）。
- **训练设置**：图像分类用 MXNet、报告单模型单 224×224 center-crop 验证精度；视频分类用 PyTorch、同时报告单 clip 精度与 video 精度。分布式 K80 GPU 集群、同步 SGD。消融在 Kinetics 上用 32 GPU、总 batch 512、从头训练、输入 16 帧 112×112；base lr=0.2，在 20k/30k 迭代各乘 0.1，37k 迭代终止。三个卷积层 φ/θ/ρ 的输出通道设为输入通道的 **1/4**；为公平对比所有方法均不用 sub-sampling 技巧。
- **消融——单个块（表 2，Kinetics）**：块置于某 stage 第二个残差单元之后。基线 ResNet-26 Clip@1=50.4% / Video@1=60.7%；ResNet-29 为 50.8% / 61.6%。A2-block 在 Conv2/Conv3/Conv4 分别得 Clip@1 = 51.2% / 51.9% / **52.3%**（+0.8 / +1.5 / +1.9），额外 FLOPs 仅 463M。对比 NL-block：@Conv3=51.5%(+1.1, +5.45G)、@Conv4=51.7%(+1.3, +1.04G)，且 @Conv2 因复杂度在底层二次膨胀（+40.69G FLOPs）**训练无法完成**。论文发现 A2 置于**高层**收益更大（高层语义更抽象，利于提取全局视觉基元）。
- **消融——多个块（表 3，Kinetics）**：A2 随块数（1/2/4）单调提升——1@Conv4=52.3%、2@Conv4=52.5%、4@Conv3&4=**53.0%**（Video@1 至 63.5%），4 块仅 +1.85G FLOPs。对应 NL-Net 4@Conv3&4=52.4%（+12.97G FLOPs）。分散到不同 stage 比集中同一 stage 收益更大。同等设置下 A2（如 4 块 10.1G FLOPs）以更低成本胜过 NL（4 块 21.3G FLOPs）。
- **图像识别与完整 SOTA 对比**：提取缓存在 Section 3.3 "Experiments on ImageNet" 处截断（原文约 34838 字符，缓存仅前 25000 字符 / 含表 1-3）。摘要明确给出结论：ResNet-50 + A2-block 在 ImageNet-1k 上超越 ResNet-152，参数减少 40%+、FLOPs 更低；Kinetics/UCF-101 上达 SOTA。**具体 ImageNet/UCF-101 数值表据原文后续页，提取缓存未覆盖，待核。**
## 局限

1.  **实验范围**：实验集中于分类任务（图像识别 + 视频动作识别）。对密集预测任务（检测、分割）的直接效果，提取文本未涉及。
2.  **紧凑描述符的表征上限**：核心假设是"一组 `n` 个紧凑全局描述符足以表征整个空间"（φ/θ/ρ 通道压到输入 1/4）。在极复杂或高度动态场景中，这组描述符的容量可能成为瓶颈，论文未探讨 `n` 的敏感性。
3.  **底层使用受限**：虽整体高效，但与 NL 同理，若把模块用于空间分辨率很高的底层（如 Conv2），中间矩乘成本仍偏高（论文 @Conv2 收益分析也提到高层更划算）。
4.  **复现细节依赖代码/附录**：主公式与 1/4 通道比例已给出，但部分集成细节、ImageNet 训练超参与完整对比表在提取缓存截断处之后，需参考原文后续页或开源代码。
## 个人评论

> 以下为 AI 阅读评论，非论文原文结论。

1.  **"先聚合再分配"是优雅的线性复杂度范式**：用一个 `m×n` 的紧凑中间表示（视觉基元袋）承载全局信息，把成本从 NL/self-attention 的 `O((dhw)^2)` 降到 `O(mn·dhw)`。左/右结合等价但成本差 3 个数量级（1MB vs 2GB）的分析，是本文最有工程价值的洞察之一。
2.  **把双线性池化重解读为注意力池化**：式 (3)→(4) 的推导（在 `B` 上加 softmax）把二阶统计量重新诠释为"加权汇聚视觉基元"，既提升性能也加深了对高阶特征统计的理解，这一视角可独立借鉴。
3.  **统一视角的价值**：式 (1) 把 SENet、Non-local、Transformer self-attention 纳入同一"聚合-分配"框架，并指出 NL 的 Embedded Gaussian 等价于 self-attention——这种"用一个公式串起多个注意力模块"的叙事，本身就是高质量架构论文的范本。

### 使用建议

- **快速了解**：读 Abstract、Introduction 动机段、图 1 与图 2、以及 Section 3.2 的表 2/表 3。
- **复现**：精读 Section 2，重点式 (4)(5)(6)(7) 与图 2 计算图；注意 φ/θ/ρ 通道设为输入 1/4、矩阵乘采用左结合（式 6）更省内存与算力。
- **借鉴创新点**：可直接把 A2-block 插入主干高层；或沿用"聚合-分配"抽象范式替换聚合/分配算子；二阶注意力池化式 (4) 可作独立聚合模块。
- **写 Related Work**：放在"长程依赖与全局上下文建模"或"注意力机制"小节，与 SENet、Non-local、Transformer、双线性/协方差池化并列，突出其"线性复杂度"与"自适应分配"。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉**网络架构设计**与**注意力机制**方向（NeurIPS 2018），核心是设计一个高效、可即插即用的全局注意力算子——**双重注意力块（A2-block）**，用于增强图像/视频识别。它聚焦"如何高效建模长程依赖"这一算子级问题，故归入 `B_注意力算子模块` 最贴切。

## 2. 一句话总结
本文提出"双重注意力块"：先用**二阶注意力池化**把整个时空空间的特征汇聚成一袋紧凑的全局视觉基元，再用第二个注意力按每个位置的需求**自适应分配**回去，以线性复杂度（而非 self-attention 的二次复杂度）高效捕捉长程依赖。

## 3. 背景与问题
- **痛点**：卷积算子只看局部邻域（如 7×7），靠堆深来建模长程依赖，导致模型臃肿、优化路径长、远处特征"延迟"——三重低效。
- **近期工作不足**：SENet [11] 把同一全局特征分给所有位置（不够灵活）；Non-local Net [25] 计算所有位置对的关系矩阵（`dhw×dhw`，开销大）。
- **目标**：让一层卷积能立即感知整个时空空间——先汇聚关键特征到紧凑集合，再自适应分配，无需大感受野。

## 4. 核心贡献
1.  **通用公式** `z_i = F_distr(G_gather(X); v_i)`（式 1），用"聚合 + 分配"统一描述长程依赖建模。
2.  **双重注意力块**：二阶注意力池化聚合 + 自适应注意力分配，低算力/低内存建模长程依赖并显著提升性能。
3.  **三基准验证**：ImageNet-1k、Kinetics、UCF-101 上大量消融与 SOTA 对比；ResNet-50+A2 以减 40%+ 参数超越 ResNet-152。

## 5. 方法详解
- **结构**：可插入 ResNet 的即插即用块，所有卷积核 1×1×1（图 2）。输入 `X ∈ R^{c×d×h×w}`（图像 `d=1`），输出 `Z` 经末端扩通道卷积后逐元素相加回 `X`（残差）。
- **第一步 聚合（式 2→3→4）**：从双线性池化 `A B^T` 出发，重解读为"一袋视觉基元"，对 `B` 加 softmax 得**二阶注意力池化** `g_i = A·softmax(b_i)^T`；`A=φ(X)`、`B=softmax(θ(X))`。`b_i` 密集→捕捉纹理/光照等全局属性，`b_i` 稀疏→捕捉物体/部件等语义。不加低秩约束（区别于 [7] 的 rank-1）。
- **第二步 分配（式 5）**：`z_i = G_gather(X)·v_i`，`Σ_j v_ij=1`，`V=softmax(ρ(X))`；每个位置按 `v_i` 自适应挑选互补的全局基元（区别于 SENet 的统一分配）。
- **合一（式 6 左结合）**：`Z = [φ(X)·softmax(θ(X))^T]·softmax(ρ(X))`，两次带 reshape/转置的矩乘。
- **左 vs 右结合（式 6 vs 7）**：等价但成本不同。左结合第二次矩乘 `O(mn·dhw)`、右结合 `O(m·(dhw)^2)`；论文举例 `32×28×28×512` 输入右结合 >2GB、左结合约 1MB，故 `(dhw)^2>nm` 时用左结合。
- **训练**：随主干端到端，梯度由自动微分按链式法则计算（未提特殊技巧）。

## 6. 实验与结果
- **数据集/主干**：ImageNet-1k（图像）、Kinetics+UCF-101（视频）；ResNet-26（7.043M/8.3G）、ResNet-29（7.620M/9.2G）、ResNet-50（33.4M/31.3G），消融用 ResNet-26（表 1）。
- **设置**：消融在 Kinetics，32 GPU、batch 512、16 帧 112×112、base lr=0.2（20k/30k×0.1，37k 止）；φ/θ/ρ 输出通道 = 输入 1/4；不用 sub-sampling。
- **单块（表 2）**：基线 ResNet-26 Clip@1=50.4%/Video@1=60.7%，ResNet-29=50.8%/61.6%。A2@Conv2/3/4 = 51.2/51.9/**52.3**%（+0.8/+1.5/+1.9），额外仅 463M FLOPs；NL@Conv3=51.5%(+5.45G)、@Conv4=51.7%(+1.04G)，@Conv2 因二次膨胀(+40.69G) 训练无法完成。高层放置收益更大。
- **多块（表 3）**：A2 1/2/4 块 = 52.3/52.5/**53.0**% Clip@1（Video@1 至 63.5%），4 块仅 +1.85G FLOPs；NL 4 块 52.4%（+12.97G）。分散到不同 stage 优于集中同一 stage。
- **图像识别 SOTA**：摘要明确 ResNet-50+A2 在 ImageNet-1k 超 ResNet-152（参数 −40%+、FLOPs 更低）；Kinetics/UCF-101 达 SOTA。**具体 ImageNet/UCF-101 数值表据原文后续页，提取缓存（前 25000 字符）未覆盖，待核。**

## 7. 这篇论文真正有价值的地方
1.  **线性复杂度的全局建模范式**：用 `m×n` 紧凑视觉基元袋替代 `(dhw)^2` 关系矩阵，把全局上下文成本从二次降到线性；左/右结合的内存对照（1MB vs 2GB）是直接可落地的工程洞察。
2.  **双线性池化 → 注意力池化的重诠释**：式 (3)→(4) 把二阶统计量解释成"加权汇聚视觉基元"，加 softmax 即得注意力池化，既提性能又给出新理解视角。
3.  **统一注意力家族**：式 (1) 将 SENet / Non-local / Transformer self-attention 纳入同一框架，并证明 NL 的 Embedded Gaussian 等价于 self-attention，叙事极具启发性。

## 8. 局限与问题
1.  **任务范围**：仅验证分类（图像 + 动作识别），未涉及检测/分割等密集预测（提取文本范围内）。
2.  **紧凑描述符容量**：假设 `n` 个（通道压到 1/4）基元足以表征全空间，复杂动态场景下可能成瓶颈，未做 `n` 的敏感性分析。
3.  **底层使用成本**：与 NL 同理，模块用于高分辨率底层（Conv2）时中间矩乘成本仍偏高，论文亦建议放高层。
4.  **复现依赖后续页/代码**：ImageNet 训练超参与完整 SOTA 对比表在提取缓存截断处之后。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Introduction 动机段 + 图 1/图 2 + 表 2/表 3。
- **复现**：精读 Section 2 与式 (4)(5)(6)(7)、图 2；注意 φ/θ/ρ 通道=输入 1/4、用左结合（式 6）。
- **借鉴**：把 A2-block 插主干高层；沿用"聚合-分配"范式替换算子（如 QKV）；二阶注意力池化式 (4) 可作独立聚合模块。
- **写 Related Work**：放"长程依赖/全局上下文"或"注意力机制"小节，与 SENet、Non-local、Transformer、双线性/协方差池化并列，突出"线性复杂度 + 自适应分配"。

## 10. 和其他论文的关系
依据主题 `B_注意力算子模块`，与下列工作密切相关（论文正文均有引用）：
- **Squeeze-and-Excitation Networks (SENet)** [11]：A2 受其"聚合-分配"启发，但式 (1) 更一般——用二阶注意力池化替代一阶平均池化、用自适应分配替代统一通道缩放。
- **Non-local Neural Networks (NL-Net)** [25]：与 A2 解决同一长程依赖问题；A2 右结合形式可被 NL 解释，区别在成对关系函数（A2 用 `softmax(θ)^T·softmax(ρ)` 而非 Embedded Gaussian），且 A2 更高效。
- **Transformer / Self-Attention** [24]：论文指出 Embedded Gaussian NL-Net 数学等价于 self-attention，故对 NL 的对比/结论外推到 Transformer。
- **Bilinear / Covariance Pooling** [14, 15]：A2 的特征聚合直接源于对双线性池化（式 2/3）的重解读。

## 11. 关键词
- 双重注意力网络 (A2-Nets / A2-block)
- 二阶注意力池化 (second-order attention pooling)
- 特征聚合与分配 (gather & distribute)
- 长程依赖建模 / 全局上下文
- 视觉基元袋 (bag of visual primitives)
- 线性复杂度注意力 / 即插即用模块
- 图像识别 / 视频动作识别 (Kinetics, UCF-101, ImageNet-1k)

## 12. 可信度说明
本笔记基于 PDF 提取文本生成。提取缓存标注 10/10 页，但实际文本在 25000 字符处被截断（原文约 34838 字符），结束于 Section 3.3 "Experiments on ImageNet" 开头。因此覆盖良好的部分包括：摘要、引言、完整方法（式 1-7、图 1/图 2、左右结合分析）、表 1（主干）、表 2/表 3（Kinetics 单块/多块消融，含具体 Clip@1/Video@1/FLOPs 数值）。未覆盖部分：ImageNet 完整结果表、UCF-101 数值、与 SOTA 的完整对比、结论（Section 4）。摘要中"ResNet-50 超越 ResNet-152、参数 −40%+"为论文原文明确结论，但其支撑数值表在缓存截断之后，已标注"待核"。除明确标注外，本笔记所有数值均可在提取文本表 2/表 3 中逐一核对。

---

> **可信度补充**: PDF 提取质量 = **high** (排版清晰、公式与表格可读); 来源缓存: `.paper-cache/extracts/DA.txt` (标注 10/10 页, 实际文本 25000 字符处截断, 约覆盖原文前 72%, 止于 Section 3.3); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
