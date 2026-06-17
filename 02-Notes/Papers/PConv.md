---
title: "Run, Don’t Walk: Chasing Higher FLOPS for Faster Neural Networks"
authors:
  - "Jierun Chen"
  - "Shiu-hong Kao"
  - "Hao He"
  - "Weipeng Zhuo"
  - "Song Wen"
  - "Chul-Ho Lee"
  - "S.-H. Gary Chan"
year: 2023
venue: "CVPR 2023 (arXiv:2303.03667)"
doi: 
pdf: [[PConv.pdf]]
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
extract_cache: .paper-cache/extracts/PConv.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# Run, Don’t Walk: Chasing Higher FLOPS for Faster Neural Networks

## 基本信息
- **PDF**: [[PConv.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Run, Don’t Walk: Chasing Higher FLOPS for Faster Neural Networks |
| **作者** | Jierun Chen; Shiu-hong Kao; Hao He; Weipeng Zhuo; Song Wen; Chul-Ho Lee; S.-H. Gary Chan |
| **单位** | HKUST(港科大); Rutgers University; Texas State University |
| **发表时间** | 2023 |
| **刊物/会议** | CVPR 2023（提取文本含 arXiv:2303.03667v3 [cs.CV] 21 May 2023）|
| **代码** | https://github.com/JierunChen/FasterNet |
| **DOI** | 未明确 |

## 摘要

**清理后的英文原摘要（据 PDF 提取文本整理，修复断词与空格）：**

> To design fast neural networks, many works have been focusing on reducing the number of floating-point operations (FLOPs). We observe that such reduction in FLOPs, however, does not necessarily lead to a similar level of reduction in latency. This mainly stems from inefficiently low floating-point operations per second (FLOPS). To achieve faster networks, we revisit popular operators and demonstrate that such low FLOPS is mainly due to frequent memory access of the operators, especially the depthwise convolution. We hence propose a novel partial convolution (PConv) that extracts spatial features more efficiently, by cutting down redundant computation and memory access simultaneously. Building upon our PConv, we further propose FasterNet, a new family of neural networks, which attains substantially higher running speed than others on a wide range of devices, without compromising on accuracy for various vision tasks. For example, on ImageNet-1k, our tiny FasterNet-T0 is 2.8×, 3.3×, and 2.4× faster than MobileViT-XXS on GPU, CPU, and ARM processors, respectively, while being 2.9% more accurate. Our large FasterNet-L achieves impressive 83.5% top-1 accuracy, on par with the emerging Swin-B, while having 36% higher inference throughput on GPU, as well as saving 37% compute time on CPU. Code is available at https://github.com/JierunChen/FasterNet.

**中文翻译：**

> 为设计快速神经网络，大量工作聚焦于降低浮点运算次数（FLOPs）。但我们观察到，FLOPs 的降低不一定带来同等程度的延迟下降——其根源在于「每秒浮点运算数（FLOPS，有效计算速度）」过低。为获得更快的网络，我们重新审视常用算子，证明这种低 FLOPS 主要源于算子频繁的内存访问，尤以深度卷积（DWConv）为甚。为此我们提出一种新的部分卷积（PConv），通过同时削减冗余计算与内存访问，更高效地提取空间特征。在 PConv 之上，我们进一步提出 FasterNet 这一全新网络家族，在多种设备上获得远高于同类的运行速度，且在各类视觉任务上不损失精度。例如在 ImageNet-1k 上，轻量级的 FasterNet-T0 在 GPU/CPU/ARM 上分别比 MobileViT-XXS 快 2.8×、3.3×、2.4×，同时精度高 2.9%；大型 FasterNet-L 取得 83.5% 的 top-1 精度，与新兴的 Swin-B 相当，但 GPU 推理吞吐高 36%、CPU 计算时间节省 37%。代码已开源。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **这篇论文为什么要做**：低延迟、高吞吐的快速神经网络对实时应用（即时响应、安全等）至关重要。主流做法用 FLOPs 衡量复杂度并努力降低它，但作者发现 FLOPs 下降并不必然换来延迟下降。
- **核心观察**：论文把延迟拆解为 `Latency = FLOPs / FLOPS`（式 1），其中 FLOPS（每秒浮点运算数）是有效计算速度。多数工作只降 FLOPs（分子）却忽视 FLOPS（分母），导致延迟改善有限。作者在 Intel CPU 上测得（图 2）：许多「快速」网络的 FLOPS 甚至低于经典 ResNet50。典型反例——**CycleMLP-B1 的 FLOPs 只有 ResNet50 的一半，实测却更慢（116.1ms vs 73.0ms）**。
- **之前方法有什么问题**：MobileNets、ShuffleNets、GhostNet 等用深度卷积（DWConv）/分组卷积（GConv）降 FLOPs，但伴随**内存访问激增**；MicroNet 进一步稀疏化把 FLOPs 压到极低，却带来碎片化的低效计算；这些网络还常引入拼接、shuffle、池化等额外数据操作，对小模型而言耗时占比可观。ViT/MLP 类（MobileViT、MobileFormer 等）仍依赖 DWConv 与改进注意力，既有 DWConv 的老问题，又需专用硬件支持，且高级归一化/激活层也拖慢速度。
- **作者想解决的核心矛盾**：**FLOPs 降低与延迟降低之间的脱节**。目标是设计一个简单、快速且有效的算子，在减少 FLOPs 的同时维持高 FLOPS，从而真正实现低延迟。作者指出该脱节的根因是**频繁的内存访问**。

## 关键贡献

1.  **指出追求高 FLOPS 的重要性**：明确「仅降 FLOPs 不够，必须同时提高 FLOPS」才能造就真正更快的网络。
2.  **提出部分卷积（PConv）**：一种简单、快速、有效的算子，仅对输入特征图的一部分（典型 1/4）通道做常规卷积、其余通道原样保留，同时削减计算冗余与内存访问，有潜力替代当前主流的 DWConv。
3.  **提出 FasterNet 网络家族**：以 PConv + 逐点卷积（PWConv）为主要构件，在 GPU/CPU/ARM 上普遍快速，并在分类、检测、分割上取得 SOTA 级速度-精度权衡。
4.  **广泛实验验证**：在多设备、多任务上验证 PConv 与 FasterNet 的高速度与有效性。

## 方法

- **整体框架（图 4）**：FasterNet 为分层 CNN，含四个阶段。每个阶段前置一个**嵌入层（Embedding，常规 Conv 4×4 / stride 4）**或**合并层（Merging，常规 Conv 2×2 / stride 2）**做空间下采样与通道扩张，随后堆叠若干 FasterNet 块。作者观察到后两个阶段的块内存访问更少、FLOPS 更高（Tab.1 佐证），故把更多块与算力分配到后两个阶段。末端用「全局平均池化 + Conv 1×1 + 全连接层」做特征变换与分类。
- **输入输出**：输入为图像；输出为分类标签或下游任务特征图。
- **关键模块**：
    1.  **部分卷积（PConv）**：核心算子。对输入 `I ∈ R^(c×h×w)`，取**前（或后）连续 `c_p` 个通道**作为整图代表做一次常规 `k×k` 卷积（如 3×3），其余 `(c−c_p)` 个通道**保持不变**（而非删除——保留它们是为了后续 PWConv 让信息流过所有通道）。其 FLOPs 为 `h×w×k²×c_p²`（式 4），内存访问约 `h×w×2c_p`（式 5）。取典型部分比 `r = c_p/c = 1/4` 时，**PConv 的 FLOPs 仅为常规 Conv 的 1/16，内存访问仅为其 1/4**。
    2.  **逐点卷积（PWConv，即 Conv 1×1）**：紧跟 PConv。两者的等效感受野在输入特征图上形如 **T 形卷积**（图 5），相比均匀处理整个 patch 的常规 Conv 更关注中心位置。作者用 position-wise Frobenius 范数在预训练 ResNet18 上统计各位置显著性（图 6），发现**中心位置（3×3 的位置 5）最常成为显著位置**，与 T 形计算聚焦中心相吻合。
    3.  **FasterNet 块**：每块为「一层 PConv + 两层 PWConv（Conv 1×1）」，整体呈倒残差结构（中间层通道扩张），并用 shortcut 复用输入特征。**与常用设计的关键区别**：归一化与激活层**只放在中间 PWConv 之后**（不在网络中处处堆叠），以保留特征多样性并降低延迟；归一化选用 **BN**（推理时可融合进相邻 Conv 加速），激活层在小变体用 **GELU**、大变体用 **ReLU**。
- **DWConv 的内存访问瓶颈（3.1 推导）**：DWConv FLOPs 为 `h×w×k²×c`（常规 Conv 为 `h×w×k²×c²`），虽低但单独替换常规 Conv 会严重掉精度，故实践中把通道数从 `c` 扩到 `c′`（如倒残差中扩 6 倍）来补偿，导致内存访问升至 `≈ h×w×2c′`（式 2），高于常规 Conv 的 `≈ h×w×2c`（式 3），在 I/O 受限设备上造成可观延迟。
- **T 形卷积的分解证明（3.3）**：对同样输入/输出，T 形 Conv 的 FLOPs 为 `h×w×(k²·c_p·c + c·(c−c_p))`（式 6），高于「PConv + PWConv」的 `h×w×(k²·c_p² + c²)`（式 7）——当 `(k²−1)c > k²·c_p`（如 `c_p = c/4, k = 3` 时成立）。故把 T 形 Conv 分解成 PConv+PWConv 既利用了滤波器间冗余、又进一步省 FLOPs，且可直接复用现成常规 Conv 实现。
- **训练/推理**：使用标准分类/检测/分割流程；推理时 BN 融合进相邻层加速。
- **和已有方法的差异**：
    - **与 DWConv/GConv 相比**：它们利用**滤波器冗余**做低秩近似，并常需加宽网络补偿精度从而增内存访问；PConv 利用**特征图通道间冗余**，同时降 FLOPs 与内存访问，FLOPS 更高。
    - **与常规 Conv 相比**：PConv 的 FLOPs 与内存访问均大幅降低。
    - **与注意力机制相比**：PConv 是纯卷积，简单易部署、不依赖专用硬件；作者也论证注意力相对卷积的优势尚有争议且通常更慢。
- **变体**：提供 FasterNet-T0/T1/T2、-S、-M、-L 六种，结构相似、深度与宽度不同；详细规格表见附录（提取文本未覆盖）。

## 实验

- **使用的数据集**：ImageNet-1k（分类，约 1.3M 训练图、50k 验证图、1k 类）；COCO（检测）；ADE20K（分割）。**注：检测/分割的具体数值在提取文本（前 12 页）中未覆盖，据原文后续页，提取缓存未覆盖，待核。**
- **测试硬件**：GPU = 2080Ti；CPU = Intel i9-9900X（单线程）；ARM = Cortex-A72（单线程）。延迟用 batch=1、吞吐用 batch=32，推理时 BN 融合。
- **对比方法**：MobileViT-XXS、MobileNetV3、EfficientNet、Swin-B、CycleMLP-B1、ResNet50 等。
- **评价指标**：Top-1 准确率、延迟（Latency）、吞吐量（Throughput）、FLOPs、FLOPS、参数量。
- **PConv 算子效率（Tab.1, §4.1）**：堆叠 10 层纯算子、用典型尺寸特征图测速。PConv FLOPs 仅为常规 Conv 的 1/16，且在 GPU/CPU/ARM 上分别取得**比 DWConv 高 10.5×、6.2×、22.8× 的 FLOPS**。常规 Conv 的 FLOPS 最高（多年优化所致）但总 FLOPs 与延迟过高难以负担；GConv/DWConv 虽降 FLOPs 却 FLOPS 骤降，且需加宽通道补偿精度反增延迟。
- **PConv+PWConv 有效性（Tab.2, §4.2）**：用预训练 ResNet50 在四个阶段第一个 Conv 3×3 前后抽特征图建四个数据集（train 70%/val 10%/test 20%），训练「PConv+PWConv / DWConv+PWConv / GConv+PWConv」三种小网络拟合（MSE 损失）。**PConv+PWConv 平均测试损失最低（0.0123，DWConv 为 0.0148、GConv 为 0.0133）**，说明仅用一部分特征图就足以高效近似常规 Conv 的特征变换。
- **分类（ImageNet-1k, §4.3 起）**：FasterNet-T0 在 GPU/CPU/ARM 上分别比 MobileViT-XXS 快 2.8×/3.3×/2.4×、精度高 2.9%；FasterNet-L 达 **83.5% top-1**，与 Swin-B 相当，但 GPU 吞吐高 36%、CPU 计算时间省 37%。（更细的逐变体表格据原文后续页，提取缓存未覆盖，待核。）
- **泛化**：跨 GPU/CPU/ARM 三类设备与分类/检测/分割三类任务验证通用性。
- **消融**：见 §4 末「brief ablation study」（具体内容据原文后续页，提取缓存未覆盖，待核）。

## 局限

1.  **冗余假设依赖**：PConv 的有效性建立在「特征图通道间存在足够冗余」之上；在极低算力预算或任务特殊时，DWConv 或更激进的稀疏化方法可能仍更优。
2.  **实验范围**：提取文本可见的实验集中于主流视觉任务与标准数据集，视频、多模态、域自适应等更复杂场景未涉及。
3.  **理论深度**：除 T 形感受野直观解释与 Frobenius 范数位置统计外，对「为何部分通道卷积足以提取空间特征」缺乏更深入的理论刻画。
4.  **复现风险**：代码已开源，但延迟绝对数值随硬件/软件环境而异（相对趋势应一致）。
5.  **覆盖说明**：本笔记顶部各节主要依据 PDF 前 12 页提取文本；检测/分割具体指标、逐变体规格表与完整消融数据未在提取缓存中，标注为「待核」。

## 个人评论

1.  **问题切口本质**：把「快」从 FLOPs 这一单一代理指标，拆回 `Latency = FLOPs/FLOPS` 的双因子视角，并锁定**内存访问**为低 FLOPS 的根因——这是比「再砍几个 FLOPs」更本质的一步，也解释了为何很多「轻量」网络名不副实。
2.  **算子设计极简而有效**：PConv 的核心思想朴素到几乎「显然」——只卷一部分通道——却同时命中计算量与内存访问两个痛点，且保留其余通道留给 PWConv，避免退化成「窄的常规 Conv」。这种「用最小改动换最大收益」的工程美感很强。
3.  **理论小推导支撑设计选择**：T 形 Conv 分解成 PConv+PWConv 更省 FLOPs（式 6 vs 7）、中心位置 Frobenius 范数最大（图 6）这两处分析，使「为何这样设计」有据可依，而非纯经验堆叠。
4.  **可落地性强**：PConv 直接复用现成常规 Conv 实现、BN 可融合、归一化/激活只放中间层，整套设计对部署极友好，也使其后被 YOLO 等检测框架的轻量化版本广泛借用。
5.  **可深挖方向**：特征图通道冗余度本身随层/任务变化，固定 `r=1/4` 是否最优、能否自适应选通道，是值得继续探索的点。

### 使用建议

- **如果快速了解**：读**摘要**与**引言**，看**图 1、图 4** 理解 PConv 与 FasterNet，浏览 **Tab.1（算子 FLOPS）、Tab.2（拟合损失）** 与图 2（FLOPS-FLOPs 关系）。
- **如果复现**：重点看 **§3.2（PConv）、§3.3（PConv+PWConv 与 T 形分解）、§3.4（FasterNet 架构）**，并查附录的逐变体规格表；代码仓库 JierunChen/FasterNet 是关键参考。
- **如果借鉴创新点**：
    - 把「部分卷积」思想用到自己模型替代 DWConv；
    - 借鉴「归一化/激活只放必要位置」的极简化设计哲学；
    - 在设计算子时同时盯住 FLOPS 与内存访问，而不仅是 FLOPs。
- **如果写 related work**：放在「高效卷积算子设计」（对比 DWConv/GConv）或「轻量级网络架构」（对比 MobileNet/ShuffleNet/GhostNet）一节。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**高效神经网络设计 / 高效卷积算子**方向，核心解决「**FLOPs 与延迟脱节**」问题：现有轻量网络（MobileNet/ShuffleNet/GhostNet 等）一味降 FLOPs，却因频繁内存访问导致有效计算速度（FLOPS）低、实测延迟改善有限。论文从算子层面给出替代方案 PConv，并据此搭建 FasterNet 骨干。在本知识库 taxonomy 中无「高效骨干」专类，归入最贴近的**「B_注意力算子模块」（基础算子/模块设计）**；需注意 PConv 是纯卷积算子而非注意力，此归类是「就近原则」而非语义精确匹配。

## 2. 一句话总结
提出**部分卷积（PConv）**——只对一部分输入通道做常规卷积、其余原样保留——在把 FLOPs 降到常规 Conv 1/16、内存访问降到 1/4 的同时维持高 FLOPS，并以「PConv+两层 PWConv」为块搭建 **FasterNet**，在 GPU/CPU/ARM 上获得显著更快的速度而不损精度。

## 3. 背景与问题
- **动机**：实时应用要求低延迟高吞吐；但延迟由 `Latency = FLOPs/FLOPS`（式 1）共同决定，业界只优化分子 FLOPs、忽视分母 FLOPS。
- **证据**：Intel CPU 上多数「快速」网络的 FLOPS 低于 ResNet50（图 2）；CycleMLP-B1 FLOPs 是 ResNet50 一半却更慢（116.1ms vs 73.0ms）。
- **根因诊断**：低 FLOPS 主要来自**频繁内存访问**，尤以 DWConv 为甚——为补偿精度而加宽通道（如倒残差扩 6 倍）使内存访问升至 `≈h×w×2c′`（式 2），高于常规 Conv 的 `≈h×w×2c`（式 3）。
- **目标**：设计简单、快、有效、能维持高 FLOPS 的算子，消除 FLOPs-延迟脱节。

## 4. 核心贡献
1.  提出「降 FLOPs 之外更要提 FLOPS」的观点；
2.  提出 PConv 算子，有潜力替代主流 DWConv；
3.  提出在 GPU/CPU/ARM 上普遍快速的 FasterNet 家族；
4.  在多任务多设备上做广泛实验验证。

## 5. 方法详解
- **DWConv 问题回顾（§3.1）**：DWConv FLOPs `h×w×k²×c`，虽低但替换常规 Conv 会掉精度，需加宽到 `c′` 补偿，内存访问反升（式 2 vs 3），在 I/O 受限设备上拖慢。
- **PConv（§3.2）**：利用特征图**通道间高冗余**（图 3 在 ResNet50 中间层可见）。取前/后连续 `c_p` 个通道做常规 `k×k` 卷积、其余不动。FLOPs `h×w×k²×c_p²`（式 4），内存访问 `≈h×w×2c_p`（式 5）；`r=c_p/c=1/4` 时 FLOPs 为常规 Conv 的 1/16、内存访问为 1/4。**不删除其余通道**，因为它们要供后续 PWConv 让信息流过全通道。
- **PConv+PWConv 与 T 形感受野（§3.3）**：两者等效感受野形如 T 形 Conv（图 5），聚焦中心；用 ResNet18 上 position-wise Frobenius 范数统计证明中心位置（3×3 的位置 5）最显著（图 6）。进一步证明把 T 形 Conv **分解**为 PConv+PWConv 更省 FLOPs：式 6 `h×w×(k²·c_p·c+c·(c−c_p))` > 式 7 `h×w×(k²·c_p²+c²)`，条件 `(k²−1)c>k²·c_p`（`c_p=c/4,k=3` 时成立）。
- **FasterNet（§3.4）**：四阶段分层，前置 Embedding（Conv 4×4/s4）或 Merging（Conv 2×2/s2）；块 = PConv + 2×PWConv 的倒残差结构 + shortcut；归一化/激活**只放中间 PWConv 后**（保特征多样性、降延迟），归一化用 BN（推理可融合），激活小变体 GELU、大变体 ReLU；末端 全局池化+Conv 1×1+FC。后两阶段分配更多块/算力（因其 FLOPS 更高）。变体 T0/T1/T2/S/M/L。

## 6. 实验与结果
- **数据集**：ImageNet-1k（1k 类、约 1.3M 训练/50k 验证）、COCO、ADE20K（后两者具体数值据原文后续页，提取缓存未覆盖，待核）。
- **硬件**：GPU 2080Ti、CPU i9-9900X 单线程、ARM Cortex-A72 单线程；延迟 batch=1、吞吐 batch=32。
- **算子效率（Tab.1）**：PConv FLOPs 为常规 Conv 1/16；FLOPS 在 GPU/CPU/ARM 上比 DWConv 高 **10.5×/6.2×/22.8×**。常规 Conv FLOPS 最高但总 FLOPs/延迟过高；GConv、DWConv 降 FLOPs 但 FLOPS 骤降。
- **拟合有效性（Tab.2）**：用 ResNet50 各阶段 Conv 3×3 前后特征图建数据集，PConv+PWConv 平均测试损失最低（**0.0123** vs DWConv 0.0148、GConv 0.0133）。
- **分类（ImageNet-1k）**：FasterNet-T0 在三设备上比 MobileViT-XXS 快 2.8×/3.3×/2.4× 且精度高 2.9%；FasterNet-L 达 83.5% top-1，与 Swin-B 相当但 GPU 吞吐高 36%、CPU 省 37% 计算时间。
- **检测/分割 + 完整消融**：提取文本（前 12 页）止于 §4.3 开头，相关具体数值据原文后续页，提取缓存未覆盖，待核。

## 7. 这篇论文真正有价值的地方
1.  把「快」从单一 FLOPs 代理还原为 FLOPs/FLOPS 双因子，并锁定内存访问为根因——视角更本质。
2.  PConv 设计极简却同时打中计算量与内存访问，且保留其余通道避免退化。
3.  T 形分解（式 6/7）与中心显著性（图 6）让设计选择有理论/统计支撑。
4.  工程友好（复用常规 Conv、BN 可融合、极简归一化/激活布置），易部署易复现，后续被检测框架轻量化版本广泛借用。

## 8. 局限与问题
1.  依赖「通道冗余充足」假设，极低预算或特殊任务下未必最优。
2.  提取可见实验集中于主流视觉任务，视频/多模态/域自适应未涉及。
3.  理论刻画偏直观（T 形 + 位置统计），缺更深机理分析。
4.  延迟绝对值随软硬件环境变化，需以相对趋势为准。
5.  本笔记顶部各节据前 12 页提取，检测/分割数值、逐变体规格、完整消融未覆盖（已标「待核」）。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + 图 1/图 4 + Tab.1/Tab.2 + 图 2。
- **复现**：§3.2/§3.3/§3.4 + 附录规格表 + JierunChen/FasterNet 仓库。
- **借鉴创新点**：用部分卷积替代 DWConv；借鉴「归一化/激活只放必要位置」；设计算子时同时盯 FLOPS 与内存访问。
- **写 related work**：归入「高效卷积算子设计」或「轻量级网络架构」一节。

## 10. 和其他论文的关系
- 与轻量卷积网络相关：`[[MobileNet系列]]`、`[[ShuffleNet]]`、`[[GhostNet]]`、`[[EfficientNet]]`（提取文本均作为对比/背景被引）。
- 与高效 Transformer/MLP 相关：`[[MobileViT]]`、`[[MobileFormer]]`、`[[CycleMLP]]`、`[[Swin Transformer]]`（Swin-B 为精度对标对象）。
- 与计算瓶颈分析相关：本文把内存访问而非 FLOPs 视为关键瓶颈，可与分析 I/O / 算子效率的工作互参。
（注：本知识库主题文件名为「B_注意力算子模块」，而本文核心是卷积算子，语义并非严格匹配；上述链接多为论文中明确出现的对比对象，未在文中出现者不臆造。）

## 11. 关键词
Partial Convolution (PConv), FLOPS, Efficient Neural Networks, Low-Latency Inference, Memory Access, FasterNet, Depthwise Convolution (DWConv), T-shaped Convolution, Pointwise Convolution (PWConv), Hardware-Friendly Design, ImageNet-1k.

## 12. 可信度说明
本篇精读笔记主要基于 PDF 提取文本（前 12 页，止于 §4.3 ImageNet 实验开头）。该范围覆盖了摘要、引言、相关工作、核心方法（§3 PConv 与 FasterNet 全部设计与公式）、以及算子效率（Tab.1）与拟合有效性（Tab.2）两组关键实验，文本质量良好，核心思想、关键公式、Tab.1/Tab.2 数值均严格引自原文。**检测/分割的具体指标、逐变体（T0–L）规格表、完整消融数据未在提取缓存中**，相关处已标注「据原文后续页，提取缓存未覆盖，待核」，未编造任何数字。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/PConv.txt` (提取 12/15 页, 25000 字符上限; 原 AI 主体 12/15 + 全文补读 13-15); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本次重读据提取文本核对并补全 Tab.1/Tab.2 数值、Eq.2–7 公式、硬件型号与架构细节, 检测/分割等未覆盖项已标「待核」。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Accelerating deep network training by reducing internal co-
- p.13: Imagenet classification with deep convolutional neural net-
- p.13: Mengchen Liu, Lu Yuan, Zicheng Liu, Lei Zhang, and Nuno
- p.13: Fitsum A Reda, Karan Sapra, Zhiding Yu, Xiaodong Yang,
- p.13: Proceedings of the IEEE/CVF Conference on Computer Vi-
- p.13: Proceedings of the IEEE/CVF International Conference on
- p.13: Hang Xu, Weiguo Gao, Chunjing Xu, Tao Xiang, and Li
- p.13: Shufflenet v2: Practical guidelines for efficient cnn architec-
- p.13: Cholakkal, Salman Khan, Syed Waqas Zamir, Rao Muham-
- p.13: Dudziak, Hongsheng Li, Georgios Tzimiropoulos, and Brais
- p.14: IEEE conference on computer vision and pattern recogni-
- p.14: Conference on Computer Vision and Pattern Recognition ,

### 缺失页关键摘录

- p.13: extremely low flops. In Proceedings of the IEEE/CVF In-
<!-- AI_READING_NOTE_END -->
