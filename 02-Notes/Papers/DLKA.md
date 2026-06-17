---
title: "Beyond Self-Attention: Deformable Large Kernel Attention for Medical Image"
authors:
  - "Reza Azad"
  - "Leon Niggemeier"
  - "Michael Hüttemann"
  - "Amirhossein Kazerouni"
  - "Ehsan Khodapanah Aghdam"
  - "Yury Velichko"
  - "Ulas Bagci"
  - "Dorit Merhof"
year: 2023
venue: "arXiv"
doi: 
pdf: [[DLKA.pdf]]
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
extract_cache: .paper-cache/extracts/DLKA.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# Beyond Self-Attention: Deformable Large Kernel Attention for Medical Image

## 基本信息
- **PDF**: [[DLKA.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Beyond Self-Attention: Deformable Large Kernel Attention for Medical Image Segmentation |
| **作者** | Reza Azad; Leon Niggemeier; Michael Hüttemann; Amirhossein Kazerouni; Ehsan Khodapanah Aghdam; Yury Velichko; Ulas Bagci; Dorit Merhof (通讯) |
| **机构** | RWTH Aachen University (德); Iran University of Science and Technology; Shahid Beheshti University; Northwestern University (美); University of Regensburg; Fraunhofer MEVIS |
| **发表时间** | 2023 (arXiv:2309.00121v1, 2023-08-31) |
| **刊物/会议** | arXiv (cs.CV) |
| **代码** | 公开于 GitHub (摘要末尾声明) |
| **DOI** | 未明确 |

## 摘要

> **英文原摘要 (据 PDF 提取文本整理, 已修复空格/连字符与混入字符)**:
> Medical image segmentation has seen significant improvements with transformer models, which excel in grasping far-reaching contexts and global contextual information. However, the increasing computational demands of these models, proportional to the squared token count, limit their depth and resolution capabilities. Most current methods process 3D volumetric image data slice-by-slice (called pseudo 3D), missing crucial inter-slice information and thus reducing the model's overall performance. To address these challenges, we introduce the concept of Deformable Large Kernel Attention (D-LKA Attention), a streamlined attention mechanism employing large convolution kernels to fully appreciate volumetric context. This mechanism operates within a receptive field akin to self-attention while sidestepping the computational overhead. Additionally, our proposed attention mechanism benefits from deformable convolutions to flexibly warp the sampling grid, enabling the model to adapt appropriately to diverse data patterns. We designed both 2D and 3D adaptations of the D-LKA Attention, with the latter excelling in cross-depth data understanding. Together, these components shape our novel hierarchical Vision Transformer architecture, the D-LKA Net. Evaluations of our model against leading methods on popular medical segmentation datasets (Synapse, NIH Pancreas, and Skin lesion) demonstrate its superior performance. Our code implementation is publicly available at GitHub.

> **中文翻译**:
> 借助善于把握远程上下文与全局上下文信息的 Transformer 模型, 医学图像分割已取得显著进步。然而这类模型的计算开销与 token 数量的平方成正比, 随之增长, 限制了网络的深度与分辨率。当前多数方法以"逐切片"(伪 3D)方式处理 3D 体数据, 丢失了关键的切片间信息, 从而损害整体性能。为应对这些挑战, 我们提出"可变形大核注意力"(Deformable Large Kernel Attention, D-LKA Attention)——一种精简的注意力机制, 利用大卷积核充分感知体数据上下文。该机制在与自注意力相当的感受野下工作, 同时规避了其计算开销。此外, 我们的注意力机制借助可变形卷积灵活地"扭曲"采样网格, 使模型能自适应多样的数据模式。我们为 D-LKA Attention 设计了 2D 与 3D 两个版本, 其中 3D 版本在跨切片(cross-depth)理解上表现尤佳。这些组件共同构成了我们新颖的层级式 Vision Transformer 架构——D-LKA Net。在多个常用医学分割数据集(Synapse、NIH Pancreas、皮肤病变)上与领先方法的对比表明其性能更优。代码已在 GitHub 公开。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

*   **为什么要做**：医学图像分割是计算机辅助诊断的关键环节, 可减少人工标注负担、降低对专家的依赖, 并支撑更快更准的诊断与影像引导手术。因此构建"快速且精确"的分割算法是本文的根本动机。
*   **之前方法的问题**：
    1.  **CNN 的局限**：CNN 擅长提取局部细节与低层信息, 但可检测目标的尺度与该层感受野紧密绑定——目标超出感受野会欠分割, 感受野过大又会让背景过度干扰预测; 难以建模长程依赖与全局上下文。
    2.  **ViT 的局限**：ViT 的注意力机制能跨整个输入序列聚合信息、突破 CNN 的有限感受野, 从而建模长程上下文; 但把图像切成 patch 序列后, 其对局部纹理/细节的表征不如卷积, 而局部纹理对诊断/预后任务至关重要。同时计算量随 token 数平方增长。
    3.  **CNN-ViT 混合方法的局限**：TransUNet 在 CNN 瓶颈中插入 Transformer 层, 但计算效率低; HiFormer 组合 Swin Transformer 与 CNN 编码器并用双层融合模块, 但重度依赖 CNN 骨干; UNETR/CoTr/TransBTS 等也存在效率或多尺度信息利用不足的问题。
    4.  **纯 Transformer 改进的局限**：Swin-UNet、MISSFormer、D-Former 重新设计自注意力(窗口注意力/高效 Transformer/双注意力等), 但仍存在计算低效、缺乏多尺度考虑等问题。
    5.  **处理 3D 数据的方式**：现有架构常逐切片处理 3D 体, 忽略相邻切片间的潜在关联, 损害定位精度与上下文整合。
    6.  **形变问题**：医学影像中病变/器官常呈现形状形变, 学习算法需具备捕获这些形变的能力, 同时还要保持计算高效以便处理 3D 体数据。
*   **核心矛盾**：如何在**保持计算高效**的同时, 既建模**长程依赖(全局上下文)**, 又自适应医学图像中器官/病变的**不规则形变(局部细节)**, 特别是面向 3D 体数据。
## 关键贡献

1.  **提出 Deformable-LKA 模块 (❶)**：作为网络的基本构建块, 显式设计来兼顾上下文信息与局部描述子, 并引入"基于数据动态调整感受野"的能力, 摆脱传统卷积固定滤波掩码的限制。其大核由深度可分离卷积、深度可分离扩张卷积、1×1 卷积组合构建, 以远低于自注意力的参数/计算获得相近感受野; 且**无需 Softmax/Sigmoid 归一化**(据文献其会抑制高频信息)。
2.  **引入可变形卷积**：用一个额外卷积层从特征自身学习偏移场, 使采样网格可整数偏移地自由形变, 自适应病变/器官形变, 增强对不规则边界的刻画。
3.  **设计 2D 与 3D 两套 D-LKA Net 架构 (❷❸)**：2D 与 3D 版本均为层级式编码器-解码器; 3D 版本将 D-LKA 机制适配到 3D 上下文, 实现跨切片(volumetric slices)的信息交换。
4.  **计算高效与高性能的统一**：网络仅依托 D-LKA 概念构建, 在多个分割基准上取得 SOTA。
## 方法

*   **整体框架**：D-LKA Net 是**层级式编码器-解码器(U 型)架构**, 2D/3D 两版本结构对称, 用于像素/体素级语义分割。
*   **输入输出**：输入 2D 医学图像或 3D 体数据, 输出同尺寸分割图。
*   **2.1 大核注意力 (LKA) 回顾**：一个 K×K 大核可由"深度可分离卷积 + 深度可分离扩张卷积(扩张率 d)+ 1×1 卷积"近似。两支卷积核尺寸为 `DW=(2d−1)×(2d−1)`(式1)、`DW-D=(K/d)×(K/d)`(式2)。参数量 `P(K,d)=C·((K/d)²+(2d−1)²+3+C)`(式3), FLOPs `F=P×H×W`(式4); FLOPs 随输入尺寸线性增长, 参数随通道数与核尺寸二次增长但通常都很小, 不构成瓶颈。对固定 K 求 P 对 d 的导数为零可得最优扩张率(式5); 例如 K=21 时 d≈3.37。3D 情形对应式(6)(7), 把 H×W 推广为 H×W×D。
*   **2.2 D-LKA 模块**：在 LKA 基础上引入可变形卷积。模块形式(式8):
    `Attention = Conv1×1(DDW-D-Conv(DDW-Conv(F')))`
    `Output = Conv1×1(Attention ⊗ F') + F`
    其中 `F∈R^{C×H×W}`, `F' = GELU(Conv(F))`, ⊗ 为逐元素乘, attention map 每个值表示对应特征的相对重要性。负责算偏移的卷积层与其对应卷积层共享核尺寸/扩张率, 非整数网格点用双线性插值取值。
    *   **2D 版本**：直接把(深度可分离)卷积层替换为**可变形卷积**, 以更好刻画不规则形状/尺寸的目标。
    *   **3D 版本的折中**：3D 中偏移生成层无法逐通道执行——输入通道是特征、输出通道需扩张到 `3·k×k×k`, 大核会使第三维通道数暴涨、参数与 FLOPs 剧增。故 3D 不把所有卷积变可变形, 而是**仅在深度可分离卷积之后引入单个可变形卷积层**。
*   **2.3 2D D-LKA Net**：卷积 stem 先把输入降到 H/4×W/4×C; 编码器用 **MaxViT** 块经四个阶段提取四级层级特征(每阶段后接下采样, 给出的图示为 ×2/×2/×5/×2 的 MaxViT 块配置); 解码器为四个阶段、每阶段 **2 个 D-LKA 块**, 用 Patch-Expanding 层上采样并缩减通道, 最后线性层输出。2D D-LKA 块: `x1 = D-LKA-Attn(LN(xin)) + xin`(式9), `xout = MLP(LN(x1)) + x1`(式10), 其中 `MLP = Conv1(GeLU(Convd(Conv1(x))))`(式11), Convd 为深度卷积, Conv1 为线性层。
*   **2.4 3D D-LKA Net**：patch embedding 先把输入从 (H×W×D) 降到 (H/4×W/4×D/2); 编码器三个阶段、每阶段 **3 个 D-LKA 块**, 每阶段后下采样(空间减半、通道翻倍); 瓶颈含 **2 个 D-LKA 块**; 解码器对称, 用转置卷积上采样、每阶段 3 个 D-LKA 块。跳跃连接基于简单加法融合各阶段特征, 并用卷积建立输入图与分割输出的直接连接。最终分割图由 3×3×3 与 1×1×1 卷积层产生。3D D-LKA 块: `x1 = DAttn(LN(xin)) + xin`(式12), `xout = Conv1(Conv3(x1)) + x1`(式13), Conv3 为含两层卷积+激活的前馈网络。
*   **数学直观**：大核分解用很少参数换大感受野; 可变形卷积通过学习偏移场让采样点随内容"扭曲", 更好覆盖不规则目标。
*   **训练方式**：均用 PyTorch、单张 RTX 3090 训练。
    *   2D: batch=20, SGD(base lr=0.05, momentum=0.9, weight decay=1e-4), 400 epochs; 损失 `L_total = 0.6·L_dice + 0.4·L_ce`(式14); 数据增强与 TransUNet[15] 一致。
    *   3D: batch=2, SGD(base lr=0.01, weight decay=3e-5), 1000 epochs, 每 epoch 用 250 个 patch, 输入 patch 尺寸 128×128×64; 数据增强与 nnFormer[64]、UNETR++[51] 一致。
*   **和已有方法的差异**：
    *   相较**传统自注意力**：复杂度从随 token 数平方增长降到与输入分辨率线性相关; 且无需归一化, 保留高频信息。
    *   相较**原始 LKA**：引入可变形卷积, 增强对不规则形变的适应。
    *   相较 **CNN-ViT 混合(TransUNet/HiFormer 等)**：避免计算冗余与对 CNN 骨干的重度依赖。
    *   相较**其他 3D 方法**：用完整 3D D-LKA 架构 + 3D 可变形策略, 避免伪 3D 的切片间信息丢失。
*   **论文类型特化(注意力类)**：
    *   **作用维度**：主要作用于**空间维度**, 用大核卷积在空间聚合信息, 近似全局+局部注意力。
    *   **可插入网络**：D-LKA 块为即插即用模块, 可作 Transformer/CNN 基本构建块。
    *   **计算量 vs 效果**：核心论点是 D-LKA 在更低计算成本下取得优于自注意力的分割效果; 参数/FLOPs 公式见式(3)-(7)。
## 实验

*   **实验设置**：PyTorch + 单张 RTX 3090; 2D/3D 超参见上方"训练方式"。
*   **使用的数据集**：
    1.  **Synapse 多器官分割**：30 个病例、共 3779 张腹部 CT 轴向切片(每个 CT 体 85～198 层、单层 512×512、体素分辨率约 [0.54~0.54]×[0.98~0.98]×[2.5~5.0] mm³), 评估 8 个腹部器官(脾、左右肾、胆囊、肝、胃、主动脉、胰腺); 2D/3D 评估均遵循 TransUNet[15]、UNETR++[51] 的设置。
    2.  **皮肤病变分割**：ISIC 2017(训练/验证/测试 = 2000/150/600 张皮肤镜图像)、ISIC 2018(沿用文献划分)、PH2(200 张, 含 160 痣 + 40 黑色素瘤)。
    3.  **NIH 胰腺分割**：82 个增强 3D 腹部 CT 体, 62 例训练、其余测试。
*   **对比方法**：ScaleFormer、DAEFormer、Swin-UNet、U-Net、HiFormer、MISSFormer、D-Former 等 SOTA。
*   **评价指标**：主要为 Dice 相似系数(DSC); 定性比较见 Figure 3。补充材料另含 HD 与显存(Memory)对比(据原文后续页线索)。
*   **主实验结果(关键数字)**：
    *   **Synapse(2D)**：D-LKA Net 平均 DSC 优于既有 SOTA——比 ScaleFormer 高 **1.41%**、比 DAEFormer 高 **1.64%**, 相对其他方法差距更大; 在右肾、左肾、胃、胰腺等区域提升显著; **胰腺**作为难点比第二名高出 **2.04%**(p.5)。定性上, 相比 DAEFormer 对胃的误分类更少, 相比 U-Net/Swin-UNet 减少了把远端组织误判为肝/胆囊/胃。
    *   **皮肤病变(ISIC 2017/2018/PH2)**：D-LKA Net 在各项指标上**一致性优于**竞争方法, 体现稳健的泛化能力(p.6)。
    *   (据原文后续页, 提取缓存未覆盖, 待核) 标准卷积 vs 分解卷积的参数对比见 Table 7(核尺寸 21×21); ScaleFormer 约 111.6M 参数, 引入可变形 LKA 确实带来额外参数/FLOPs; Figure 8 给出 Synapse 2D 上"性能 vs 显存/参数量"图; 另有 Synapse(Fig 9/10)与 ISIC 2018(Fig 12)的定性可视化及扩展消融。
*   **消融实验**：提取缓存(前 12 页)未含具体消融设置/结果; 据后续页线索(p.13/14)存在"扩展消融研究"用于验证鲁棒性, 数值待核。
*   **泛化实验**：在 Synapse(腹部 CT)与皮肤病变(皮肤镜图像)两种模态上均取得 SOTA, 体现跨模态泛化。
*   **效率信息**：正文给出参数/FLOPs 理论公式(式3-7), FLOPs 随输入尺寸线性增长; 提取覆盖范围内未给出运行时间/参数量/FLOPs 的实测对比表, 但补充材料(Table 7、Figure 8)含参数与显存对比(据原文后续页, 提取缓存未覆盖, 待核)。
## 局限

*   **3D 可变形卷积受限**：为控制 3D 计算量, 仅在深度可分离卷积后引入单个可变形卷积层, 而非像 2D 那样全面可变形, 可能限制对复杂 3D 形变的建模。
*   **额外参数/FLOPs 代价**：可变形 LKA 相比普通 LKA 确实引入额外参数与 FLOPs(据原文后续页 p.13 线索), 与"高效"卖点存在一定张力, 需结合补充材料的参数/显存图客观看待。
*   **机理分析待补**：提取覆盖范围内主要展示性能提升, 对"为何 D-LKA 有效"的可视化/消融在正文中分散于补充材料, 主文证据相对有限。
*   **数据集模态有限**：验证集中在腹部 CT 与皮肤镜图像, 对 MRI、超声等其他模态或更复杂边界任务的有效性未充分验证。
*   **2D 版依赖 MaxViT 编码器**：2D 性能与 MaxViT 自身能力有一定捆绑, 可能掩盖 D-LKA 模块在其他骨干下的普遍有效性。
## 个人评论

1.  **优雅的大核分解 + 可变形组合**：用"深度可分离卷积 + 深度可分离扩张卷积"高效构建大感受野, 再叠加可变形卷积自适应形变, 是替代标准自注意力的一条巧思路径, 为轻量化高效注意力模块提供了可借鉴范式。去掉 Softmax/Sigmoid 以保留高频信息这一点尤其值得在分割等密集预测任务中关注。
2.  **任务驱动的设计取向**：明确针对医学图像中器官/病变的不规则形变做模块改进, "把先验写进算子"而非堆数据, 思路上有启发性。
3.  **2D/3D 一体化方案**：不仅给出 2D 模块, 还系统设计了 3D 版本及其可变形折中策略, 直面伪 3D 的切片间信息丢失问题, 工程完整度高。
4.  **诚实的代价披露**：从后续页线索看, 作者并未回避可变形 LKA 带来的额外参数/FLOPs, 而是用参数/显存图正面比较; 不过把关键效率与消融证据放在补充材料, 削弱了主文对"高效"论点的支撑力, 复现时需连同附录一起读。

### 使用建议

*   **如果快速了解**：读摘要、引言"我们的贡献"部分与结论, 配合 Figure 1(网络架构)、Figure 2(D-LKA 模块)。
*   **如果复现**：重点看第 2 节, 尤其 2.2 节的式(8)与 2.3/2.4 节架构, 注意 2D/3D 在可变形位置上的差异; 第 3 节的优化器、损失(式14)、数据增强(对齐 TransUNet/nnFormer/UNETR++)与 patch 尺寸需照搬; 参数/显存细节见补充材料 Table 7 / Figure 8。
*   **如果借鉴创新点**：深入 2.2 节(大核分解 + 可变形)的构造, 思考迁移到分类/检测等其他视觉任务或其他骨干。
*   **如果写 related work**：可归入 1) 高效注意力/视觉 Transformer; 2) 医学分割中的上下文建模; 3) 大卷积核网络; 4) 可变形卷积在医学影像中的应用。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文处于计算机视觉与医学图像分析的交叉点, 任务为**医学图像分割**, 核心是**注意力算子模块**的改进: 提出可变形大核注意力(D-LKA), 用大核卷积在自注意力级别的感受野下高效聚合上下文, 并用可变形卷积自适应器官/病变形变。论文工作的主轴是"设计一个新算子并据其搭建网络", 因此归入"注意力算子模块"(B_注意力算子模块)主题最贴切——医学分割只是其落地场景。

## 2. 一句话总结
本文提出可变形大核注意力(D-LKA): 用"深度可分离卷积 + 深度可分离扩张卷积 + 1×1 卷积"分解出大核以低成本逼近自注意力感受野、去掉 Softmax/Sigmoid 归一化以保留高频信息, 再叠加可变形卷积自适应不规则形变, 并据此构建 2D/3D 一体的层级式 D-LKA Net, 在 Synapse、皮肤病变、NIH 胰腺等医学分割基准上取得 SOTA。

## 3. 背景与问题
*   **为什么要做**：医学分割支撑计算机辅助诊断与影像引导手术, 需要"又快又准"的算法。ViT 善于全局上下文但注意力随 token 数平方增长, 限制深度/分辨率, 且对局部纹理表征弱; CNN 善于局部却受感受野限制难建模长程依赖; 多数 3D 方法逐切片处理丢失切片间信息; 病变常有形变需被显式建模。
*   **之前方法的问题**：CNN 受感受野约束(目标过大欠分割、感受野过大背景干扰); ViT 局部纹理弱且开销大; CNN-ViT 混合(TransUNet 计算低效、HiFormer 重度依赖 CNN 骨干、UNETR/CoTr/TransBTS 多尺度利用不足); 纯 Transformer 改进(Swin-UNet/MISSFormer/D-Former)仍有低效或缺多尺度问题; 伪 3D 丢切片信息。
*   **核心矛盾**：在保持计算高效的前提下, 同时建模长程依赖(全局)与自适应不规则形变(局部), 尤其面向 3D 体数据。

## 4. 核心贡献
1.  **Deformable-LKA 模块**: 大核分解(深度可分离 + 深度可分离扩张 + 1×1)逼近自注意力感受野, 无需 Softmax/Sigmoid 归一化以保留高频信息; 引入"基于数据动态调整感受野"。
2.  **可变形卷积**: 从特征学习偏移场、整数偏移自由形变采样网格, 自适应病变/器官形变, 改善边界刻画。
3.  **2D/3D 两套 D-LKA Net 架构**: 层级式编码器-解码器; 3D 版适配 3D 上下文实现跨切片信息交换。
4.  **高效 + 高性能统一**: 仅依托 D-LKA 概念建网, 多基准 SOTA。

## 5. 方法详解
*   **框架**: 层级式编码器-解码器(U 型), 2D/3D 对称。
*   **LKA(2.1)**: K×K 大核 ≈ DW=(2d−1)² + DW-D=(K/d)²(扩张率 d) + 1×1; 参数 `P=C((K/d)²+(2d−1)²+3+C)`(式3), FLOPs=P×H×W(式4) 随输入线性增长; 式(5)给最优 d(K=21→d≈3.37); 3D 对应式(6)(7)。
*   **D-LKA 模块(2.2, 式8)**: `Attention=Conv1×1(DDW-D-Conv(DDW-Conv(F')))`, `Output=Conv1×1(Attention⊗F')+F`, `F'=GELU(Conv(F))`, ⊗ 逐元素乘; 偏移卷积与对应卷积共享核/扩张率, 非网格点双线性插值。2D: 卷积全替换为可变形; 3D: 因偏移层输出通道需扩到 3·k×k×k 致参数暴涨, 仅在深度可分离卷积后加单个可变形层。
*   **2D D-LKA Net(2.3)**: stem→H/4×W/4×C; MaxViT 编码器四阶段(图示块数 ×2/×2/×5/×2)各接下采样; 解码器四阶段、每阶段 2 个 D-LKA 块, Patch-Expanding 上采样缩通道, 线性层输出。块: 式(9)(10)(11), MLP=Conv1(GeLU(Convd(Conv1(x))))。
*   **3D D-LKA Net(2.4)**: patch embedding→H/4×W/4×D/2; 编码器三阶段各 3 块(段后下采样: 空间减半通道翻倍); 瓶颈 2 块; 解码器对称用转置卷积、每阶段 3 块; 跳跃连接加法融合 + 卷积直连输入到输出; 最终 3×3×3 + 1×1×1 卷积出图。块: 式(12)(13), Conv3 为两层卷积+激活的 FFN。
*   **训练**: PyTorch + 单 RTX 3090。2D: batch 20, SGD(lr 0.05, mom 0.9, wd 1e-4), 400 epochs, 损失 0.6·Dice+0.4·CE(式14), 增强同 TransUNet。3D: batch 2, SGD(lr 0.01, wd 3e-5), 1000 epochs/250 patch per epoch, patch 128×128×64, 增强同 nnFormer/UNETR++。
*   **与已有差异**: vs 自注意力(平方→线性、去归一化保高频); vs 原始 LKA(加可变形); vs CNN-ViT 混合(避免冗余/骨干依赖); vs 伪 3D(完整 3D 架构)。
*   **注意力类特化**: 作用于空间维; 即插即用块; 主打低成本高效果, 公式见式(3)-(7)。

## 6. 实验与结果
*   **数据集**: Synapse(30 例/3779 张腹部 CT 轴向切片, 每体 85~198 层、512×512, 8 器官); 皮肤病变 ISIC 2017(2000/150/600)、ISIC 2018、PH2(200 张=160 痣+40 黑色素瘤); NIH 胰腺(82 个 3D CT, 62 训练)。
*   **对比方法**: ScaleFormer、DAEFormer、Swin-UNet、U-Net、HiFormer、MISSFormer、D-Former 等。
*   **指标**: DSC 为主(补充材料另含 HD/Memory, 据后续页线索)。
*   **关键数字**: Synapse 2D 平均 DSC 比 ScaleFormer 高 1.41%、比 DAEFormer 高 1.64%, 胰腺难点比第二名高 2.04%(p.5); 皮肤病变三数据集各指标一致领先(p.6)。定性: 对胃误分类更少、减少把远端组织误判为肝/胆囊/胃。
*   **消融**: 提取缓存(前 12 页)未含具体设置; 据 p.13/14 线索有扩展消融, 数值待核。
*   **效率**: 参数/FLOPs 理论公式(式3-7)随输入线性增长; 实测参数/显存对比在补充材料 Table 7 / Figure 8(据原文后续页, 提取缓存未覆盖, 待核); 可变形 LKA 确带来额外参数/FLOPs。

## 7. 这篇论文真正有价值的地方
1.  **大核分解替代自注意力**: "深度可分离 + 深度可分离扩张 + 1×1" 用极少参数换大感受野, 给高效注意力模块提供范式。
2.  **去归一化保高频**: 不用 Softmax/Sigmoid 以避免抑制高频信息, 对密集预测/分割任务有针对性价值。
3.  **形变先验显式建模**: 可变形卷积 + 注意力结合, 把医学影像形变这一任务先验写进算子。
4.  **2D/3D 一体化**: 系统给出 3D 可变形的折中策略, 直面伪 3D 信息丢失。

## 8. 局限与问题
*   3D 仅单个可变形层, 对复杂 3D 形变建模能力受限。
*   可变形 LKA 引入额外参数/FLOPs(p.13 线索), 与"高效"卖点存在张力。
*   关键效率/消融证据多在补充材料, 主文机理论证相对有限。
*   验证模态集中在腹部 CT + 皮肤镜, 其他模态/复杂边界任务未充分验证。
*   2D 版性能与 MaxViT 编码器捆绑, 难分离 D-LKA 自身贡献。

## 9. 我该怎么使用这篇论文
*   **快速了解**: 摘要 + 引言贡献段 + 结论, 配 Figure 1/2。
*   **复现**: 第 2 节(尤其式8与 2.3/2.4 架构、2D/3D 可变形位置差异) + 第 3 节超参/损失(式14)/增强/patch 尺寸; 效率细节看补充材料。
*   **借鉴创新**: 吃透 2.2 节大核分解 + 可变形构造, 迁移到分类/检测或其他骨干。
*   **写 related work**: 高效注意力/ViT、医学分割上下文建模、大核网络、可变形卷积四类。

## 10. 和其他论文的关系
*   直接基于并扩展 Guo et al. 的 `[[LKA (Large Kernel Attention)]]` [23]。
*   采用 `[[Deformable Convolutional Networks]]` [20] 的可变形卷积思想。
*   2D 编码器使用 `[[MaxViT]]` [54]。
*   在医学分割上与 `[[TransUNet]]` [15]、`[[HiFormer]]` [29]、`[[UNETR]]` [26]、`[[Swin-UNet]]` [13]、MISSFormer[32]、D-Former[59]、ScaleFormer[31]、DAEFormer[4] 等对比。
*   3D 训练/评估设置对齐 `[[nnFormer]]` [64] 与 `[[UNETR++]]` [51]。

## 11. 关键词
Deformable Large Kernel Attention (D-LKA), 大核分解, 深度可分离扩张卷积, 可变形卷积, 去归一化注意力, 高频信息保留, 医学图像分割, 2D/3D 体数据, 层级式 Vision Transformer, Synapse, NIH 胰腺, 皮肤病变(ISIC/PH2)。

## 12. 可信度说明
本精读基于 PDF 提取文本的前 12 页(实际可读内容覆盖到第 5 页区域, 含摘要、引言、方法 2.1-2.4、实验设置/数据集、Synapse 2D 与皮肤病变结果; 提取在 25000 字符处截断, Table 1/2 的逐器官数值未进入可读文本)。论文核心思想、模块公式、网络架构、训练超参、数据集规模、以及 Synapse 的 1.41%/1.64%/2.04% 等关键数字均能在提取文本中找到明确依据。
无法据提取文本完全核实、依赖原笔记后续补读页线索的部分(已在正文标注"据原文后续页, 提取缓存未覆盖, 待核"):
1.  详细消融研究的具体设置与数值;
2.  参数/FLOPs/显存的实测对比表(Table 7、Figure 8);
3.  NIH 胰腺与各数据集的逐项数字、HD 指标;
4.  讨论/结论与补充材料定性图。
整体忠实于提取文本, 未编造。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页); 但缓存截断于 25000 字符, 实际可读内容止于约第 5 页, Table 数值未覆盖); 来源缓存: `.paper-cache/extracts/DLKA.txt` (标注 12/17 页; 原 AI 主体 12/17 + 全文补读 13-17 页线索); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Supplementary Material
- p.13: The additional materials provided encompass an ex-
- p.13: A comparison of the number of parameters for normal
- p.13: It is worth noting that the introduction of the deformable
- p.13: LKA does indeed introduce additional parameters and
- p.13: method, the ScaleFormer [31], which used 111.6M param-
- p.14: To further visualize our model capability, we provide a
- p.14: To gain a better understanding of the limitations associ-
- p.14: Figure 12 shows a qualitative visualization of ISIC 2018
- p.14: Since this is also present in the training data, this could hin-
- p.14: In line with the ablation study presented in the main pa-
- p.15: Spl RKid LKid Gal Liv Sto Aor Pan

### 缺失页关键摘录

- p.13: tended ablation study, which serves to demonstrate the ro-
- p.13: floating-point operations per second (FLOPS) to the model.
- p.13: visualize the performances on the Synapse 2D dataset, re-
- p.13: on the number of parameters in Figure 8. The D-LKA Net
- p.13: Figure 8. Performance vs memory chart to compare the perfor-
- p.13: posed 2D D-LKA Net on Synapse dataset. DSC, HD, and Memory
- p.14: Table 7. The number of parameters for standard convolution and decomposed convolution. The kernel size is 21×21. Adapted from [23].
- p.14: C. Qualitative results on the Synapse dataset
- p.14: Synapse dataset in Figure 9 and Figure 10. We neglect the
- p.14: spective into the 3D domain. As illustrated in Figure 11, we
- p.14: Figure 12 shows a qualitative visualization of ISIC 2018
- p.14: In line with the ablation study presented in the main pa-
<!-- AI_READING_NOTE_END -->
