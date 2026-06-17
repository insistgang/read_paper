---
title: "‘Project & Excite’ Modules for Segmentation of Volumetric Medical Scans"
authors:
  - "Anne-Marie Rickmann"
  - "Abhijit Guha Roy"
  - "Ignacio Sarasua"
  - "Nassir Navab"
  - "Christian Wachinger"
year: 2019
venue: "arXiv"
doi: 
pdf: [[PE3d.pdf]]
primary_topic: A1_医学图像_分割
topics:
  - "A1_医学图像_分割"
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
extract_cache: .paper-cache/extracts/PE3d.txt
---

# ‘Project & Excite’ Modules for Segmentation of Volumetric Medical Scans

## 基本信息
- **PDF**: [[PE3d.pdf]]
- **primary_topic**: `A1_医学图像_分割`
- **topics**: `A1_医学图像_分割`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | ‘Project & Excite’ Modules for Segmentation of Volumetric Medical Scans |
| **作者** | Anne-Marie Rickmann; Abhijit Guha Roy; Ignacio Sarasua; Nassir Navab; Christian Wachinger |
| **发表时间** | 2019（arXiv:1906.04649v2, 12 Jun 2019; eess.IV） |
| **刊物/会议** | arXiv（MICCAI 2019 接收稿） |
| **DOI** | 未明确（arXiv:1906.04649） |

## 摘要

> **英文原文（据 PDF 提取文本整理）**：Fully Convolutional Neural Networks (F-CNNs) achieve state-of-the-art performance for image segmentation in medical imaging. Recently, squeeze and excitation (SE) modules and variations thereof have been introduced to recalibrate feature maps channel- and spatial-wise, which can boost performance while only minimally increasing model complexity. So far, the development of SE has focused on 2D images. In this paper, we propose ‘Project & Excite’ (PE) modules that base upon the ideas of SE and extend them to operating on 3D volumetric images. ‘Project & Excite’ does not perform global average pooling, but squeezes feature maps along different slices of a tensor separately to retain more spatial information that is subsequently used in the excitation step. We demonstrate that PE modules can be easily integrated in 3D U-Net, boosting performance by 5% Dice points, while only increasing the model complexity by 2%. We evaluate the PE module on two challenging tasks, whole-brain segmentation of MRI scans and whole-body segmentation of CT scans. Code: https://github.com/ai-med/squeeze_and_excitation

> **中文翻译**：全卷积神经网络（F-CNN）在医学图像分割中已达到当前最优性能。近期出现的 squeeze-and-excitation（SE）模块及其变体可在通道维与空间维上重校准特征图，在仅极小幅度增加模型复杂度的同时提升性能。但目前 SE 的发展主要集中于二维图像。本文提出 ‘Project & Excite’（PE）模块，它沿用 SE 的思想并将其扩展到三维体数据。PE 不做全局平均池化，而是分别沿张量的不同切片方向压缩特征图，从而保留更多空间信息，供后续激励步骤使用。实验表明，PE 模块可轻松集成进 3D U-Net，在仅增加约 2% 模型复杂度的情况下将性能提升约 5% Dice 点。我们在两个具有挑战性的任务——MRI 全脑分割与 CT 全身分割上进行了评估。代码：https://github.com/ai-med/squeeze_and_excitation

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **这篇论文为什么要做**：全卷积神经网络（F-CNN）在计算机视觉与医学影像的语义分割中被广泛采用，但大多数架构创新面向 2D 自然图像，难以直接迁移到 CT/MRI/PET 这类体数据。早期做法是用 2D F-CNN 逐切片分割三维扫描，但相邻切片间的上下文信息未被利用，对小目标类别尤其容易产生不完整的分割。自然的选择是使用 3D F-CNN，但 3D F-CNN 有两个实际难题：(i) 训练时占用大量 GPU 显存；(ii) 权重参数远多于 2D 版本，在医学领域典型只有约 15–20 个标注扫描的有限数据下极易过拟合。
- **之前方法有什么问题**：为缓解过拟合，研究者通常通过减少卷积层数或减少每层通道数来精心压低 3D F-CNN 的模型复杂度，但这会限制网络的探索能力。SE（Squeeze and Excite）模块通过建模通道间依赖、对特定通道施加注意力，可在几乎不增加复杂度的前提下提升性能，并已被扩展到医学图像分割（2D）与 3D F-CNN（Zhu 等的 AnatomyNet）。但 3D cSE 的扩展方式是对整个 4D 张量在所有空间维度上做平均池化，生成一个逐通道的标量描述符——这会**移除全部空间信息**。作者假设：对于需要精确定位解剖结构的分割任务，丢弃空间信息会损失相关信息，尤其影响小目标。
- **作者想解决的核心矛盾**：如何在**有限训练数据**与**有限计算资源**下提升三维分割性能，特别是对**小目标结构的定位精度**，同时**不引入额外模型复杂度或 FLOP 开销**。作者的思路来自传统张量切片：沿张量三个主轴分别平均，在保留空间信息的同时为网络在每个阶段提供全局感受野。
## 关键贡献

论文在引言末尾明确列出三点贡献：

1. 提出一种新的计算模块 **`Project & Excite`（PE）**，专门用于重校准 3D F-CNN 的特征图；它用沿三个主轴的"投影"（average pooling）替代 SE 的全局平均池化，以保留更多空间信息。
2. 证明 PE 模块可**轻松集成进任意 F-CNN**，提升分割性能，**对小目标类别提升尤为显著**。
3. 证明 PE 模块相比"增加更多卷积层"只**极小幅度增加模型复杂度**，却能带来**更高的分割精度**，从实证上支撑其重校准的有效性。
## 方法

- **整体框架**：基于编码器-解码器架构（3D U-Net）。SE/PE 模块通常放在每个编码器、解码器块之后；作者实验确认放在**所有编码器、瓶颈、解码器块之后**（配置 P6）效果最佳。
- **输入输出**：输入是 4D 特征图张量 `U ∈ R^{H×W×D×C}`（高 H、宽 W、深 D、通道 C）。输出 `Û` 维度与输入相同，是经过重校准的特征图。
- **3D cSE 模块（对比基线，来自 Zhu 等）**：
  - 挤压 `Fsq`：全局平均池化把每个通道的空间内容压成一个标量，得 `z ∈ R^C`，即 `z_c = (1/HWD)·ΣΣΣ u_c(i,j,k)`（公式 1）。
  - 激励 `Fex`：用两个全连接层学习通道间依赖，`ẑ = σ(W2·δ(W1·z))`（公式 2），其中 δ 为 ReLU、σ 为 Sigmoid，`W1 ∈ R^{(C/r)×C}`、`W2 ∈ R^{C×(C/r)}`，`r` 为通道压缩因子。输出对 `U` 做逐通道乘法。
- **3D PE 模块（本文方法）**：
  1. **投影操作 `Fpr`**：不做全局池化，而拆成三个沿不同空间维的平均池化（公式 3–5），分别得到三个投影向量：
     - `z_h ∈ R^{C×H}`：对 W、D 两维平均，`z_hc(i) = (1/WD)·ΣΣ u_c(i,j,k)`，i∈{1..H}
     - `z_w ∈ R^{C×W}`：对 H、D 两维平均，j∈{1..W}
     - `z_d ∈ R^{C×D}`：对 H、W 两维平均，k∈{1..D}
     直观含义：三个向量分别给出"沿三个主轴的切片重要性"；某个空间位置只有当其对应的三个切片估值都较高时才被认为重要。
  2. **激励操作 `Fex`**：把三个投影向量分别"平铺"（tile）回 `H×W×D×C` 形状并**相加**得到 `Z`；再对 `Z` 过两个 **1×1×1 卷积层**（而非 cSE 的全连接层）+ ReLU + Sigmoid。第一层把通道压缩 `r` 倍，第二层恢复原通道数。`V1 ∈ R^{1×1×1×(C/r)}`、`V2 ∈ R^{1×1×1×C}`。
  3. **重校准**：`Û = ẑ ⊙ U = Fex(Z) ⊙ U = σ(V2 ⋆ δ(V1 ⋆ Z)) ⊙ U`（公式 6），⋆ 为卷积、⊙ 为逐元素乘法。这样既建模了通道依赖，又隐含保留了空间结构，兼顾通道与空间上下文。
- **和 cSE 的关键差异**：cSE 把每个通道的空间信息压成一个标量（在网络首/尾层空间尺度很大时损失尤为严重）；PE 用投影保留沿三个主轴的空间摘要，且不增加额外 FLOP/复杂度。
- **训练设置**：采用 3D U-Net，用**整幅 3D 扫描**而非子体训练，并对架构做了改动以保证可训练性：3 个编码器 + 3 个解码器块，仅前两个编码器做下采样、后两个解码器做上采样；每块含 2 个 3×3×3 卷积层；通道数减半（如编码器 1 的两个卷积通道为 {16,32} 而非 {32,64}）以压低复杂度。因输入尺寸大且可变，batch size = 1（占满 TITAN Xp 的 2×12 GB 显存）；小 batch 下用 **Instance Normalization**（替代对 batch 敏感的 BatchNorm）。优化器 SGD，动量 0.9，初始学习率 0.1，验证损失平台期时按 10 倍衰减。在线数据增强用弹性形变与随机旋转。损失为 **Cross Entropy + Dice 组合损失**，CE 项用**中位数频率平衡**加权以应对严重类别不平衡。
## 实验

- **使用的数据集**：
  1. **MALC**（Multi-Atlas Labelling Challenge）：脑部 T1 MRI，30 个体积，分割 32 个皮层与皮层下结构。划分：15 训练 / 3 验证 / 12 测试。标注由 Neuromorphometrics, Inc. 提供。
  2. **Visceral**：增强 CT 全身扫描，gold corpus 含 20 个标注扫描，分割胸腹部 14 个器官。采用 5 折交叉验证，每折从测试折中留一个扫描作验证集。
  两个数据集的共同挑战：训练扫描量有限、目标类别间严重不平衡。
- **对比方法**：3D U-Net（基线）、3D cSE（Zhu 等把 2D SE 直接扩到 3D 的通道 SE 版本，放置位置与 PE 一致）。
- **评价指标**：平均 Dice 系数（Mean Dice score，附标准差）。
- **主实验结果（Table 3）**：
  - **MALC（脑）**：3D U-Net **0.802±0.171** → 3D cSE **0.825±0.119** → PE **0.843±0.079**（相对基线 +4% Dice 点；论文表述 cSE +2%、PE +4%）。
  - **Visceral（全身）**：3D U-Net **0.810±0.137** → 3D cSE **0.797±0.168**（下降约 1%）→ PE **0.846±0.095**（相对基线 +3.5% Dice 点）。
  - **大目标提升很小**：白质/灰质（脑）、肝/右肺（全身）上 cSE 与 PE 的增益都在约 1% 以内，与基线相当。
  - **小目标提升巨大**：在小且难分的结构上 PE 增益约 **3–36% Dice 点**；而 cSE 在某些结构（气管 trachea、胸骨 sternum）反而下降。
    - MALC：下侧脑室 Inf. Lat. Vent. 0.242 → cSE 0.403 → PE **0.604**；杏仁核 Amygdala 0.761 → 0.761 → **0.789**；伏隔核 Accumbens 0.483 → cSE 0.704 → PE **0.735**。
    - Visceral：右肾 R. Kidney 0.907 → **0.929**；气管 Trachea 0.815 → cSE 0.491(↓) → PE **0.845**；胸骨 Sternum 0.438 → cSE 0.427(↓) → PE **0.699**。
  - 定性结果（Fig. 3）：3D U-Net 与 cSE 都漏掉了很小的左下侧脑室，PE 能分割出来；气管分叉处 U-Net 过分割右肺、cSE 完全漏掉气管，PE 正确分割。
- **消融——PE 模块放置位置（Table 1, MALC）**：测试 6 种组合：P1 仅编码器后（0.828）、P2 仅解码器后（0.796）、P3 仅瓶颈后（0.822）、P4 编码器+解码器后（0.819）、P5 编码器+瓶颈后（0.818）、P6 全部位置（**0.843**，最佳）。结论：PE 在编码器与瓶颈位置最有效；仅放解码器后几乎不提升性能。后续实验统一用 P6。
- **模型复杂度（Table 2, MALC）**：3D U-Net 基础参数 **5.57×10^6**。+3D cSE 与 +PE 都仅增加 **1.97%** 复杂度，但 PE 在同等开销下多带来约 2% 性能提升。对照实验：增加一个额外编码器-解码器块 → 复杂度 +39.7%、Dice 反而降到 **0.779**（过拟合）；只加两个卷积层 → 复杂度 +3.97%、Dice 0.826（与 cSE 相当但仍低于 PE）。证明 PE 的提升源于有效重校准而非单纯加参数。
- **速度/FLOPs**：论文未报告具体 FPS 或 FLOPs，但强调 PE 不引入额外 FLOP 开销、参数仅增约 2%。
## 局限

- **投影假设的适用性**：PE 假设沿三个主轴的平均池化足以捕捉关键空间上下文。对形状复杂、各向异性极强或高度不规则的目标，这种主轴投影可能不充分（论文未就此做实验，属于笔记的合理推测）。
- **实验范围有限**：仅在两个相对标准化的多结构分割任务（脑结构、胸腹器官）上评估，未覆盖肿瘤、病变等形态变化大、边界模糊的任务。
- **计算成本未量化**：参数增量很小，但投影、平铺、相加会带来额外计算步骤与内存访问；论文未报告推理时间或 FLOPs 增量。
- **训练数据极少**：MALC 15、Visceral 20 个标注扫描，样本量小且结构相对固定，在更大规模/更复杂任务中 PE 相对其他方法的优势是否保持需进一步验证。
- **放置位置敏感**：消融显示位置对性能影响明显（P6 最佳，P2 最差且几乎无提升），实际使用需按架构调优。
## 个人评论

> 以下为 AI 阅读评论，非论文原文。

这篇论文最值得学习的点在于**问题定位的精准**与**解决方案的"以巧补缺"**。
1. **洞察清晰**：作者把矛头直接对准 SE/cSE 的全局平均池化——"在 3D 体数据、尤其是空间尺度很大的首尾层，把整通道压成一个标量会损失定位信息"。这个对小目标的判断既符合直觉，又被实验（大目标增益小、小目标增益大）有力印证。
2. **方案精巧且省力**：投影操作借鉴传统张量切片，用三个方向的平均池化这种几乎零成本的操作换来结构化的空间摘要，比完全压缩更合理，又比真正的三维注意力轻得多，且不增加 FLOP。这种"用结构化先验弥补有限算力"的范式对资源受限场景很有启发。
3. **实验设计的反例最有说服力**：与"加一个 enc/dec 块（+39.7% 却掉点）"和"加两层卷积（+3.97% 仍不及 PE）"的对照，干净地证明了收益来自重校准机制而非参数量。这是消融写作的好范例。
4. **工程实用**：即插即用、代码开源，对想快速提升 3D 分割模型的人很实用。需要注意的是放置位置敏感（P6 最佳，仅解码器位置几乎无效），并非完全无脑可用。

### 使用建议

- **快速了解**：读摘要、引言末尾的三点贡献、结论，以及 Table 1/2/3。能快速掌握核心思想、创新点与主要结果。
- **复现**：重点看第 2 节（Methods）公式 3–6 的投影与激励，以及第 3 节训练设置（架构改动、Instance Norm、batch=1、SGD+动量 0.9、lr 0.1、CE+Dice 组合损失+中位数频率平衡）。参考开源仓库 `https://github.com/ai-med/squeeze_and_excitation`。
- **借鉴创新点**：学习"投影-激励"范式——先用有几何意义的操作（沿轴池化）得到结构化中间表示，再在其上做全局依赖建模（通道激励）。可迁移到点云、视频等任务。
- **写 related work**：可归入 1) 3D 医学图像分割，2) 注意力/特征重校准模块，3) 轻量级网络设计，4) 小目标分割。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A1_医学图像_分割]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**医学图像分析**中的**三维体数据语义分割**方向（注意：不是点云的 3D 分类/分割，目标是体素级分割 CT/MRI 体数据）。它解决用 3D F-CNN 分割医学扫描时，如何在有限训练数据下提升精度、尤其是小目标结构精度的问题。核心产出是一个即插即用的特征重校准模块，可集成进现有 3D F-CNN。因此最贴切的主题是"**3D 医学图像分割**（A1_医学图像_分割）"，相关主题为"**注意力机制/特征重校准**"。

## 2. 一句话总结
本文提出轻量级模块 **Project & Excite（PE）**，用沿三维三个主轴的"投影"（平均池化）替代 SE 的全局平均池化以保留空间信息，再在投影上做通道激励，从而在仅增加约 2% 复杂度的前提下显著提升 3D 全卷积网络对医学体数据（尤其是小目标结构）的分割精度。

## 3. 背景与问题
- **为什么要做**：3D F-CNN 是分割体数据的自然选择，但显存占用大、参数多、在医学领域典型的 15–20 个标注扫描下易过拟合。为压复杂度而减层/减通道又会限制网络能力，因此需要"在不增复杂度下最大化利用参数"的机制。
- **之前方法的问题**：SE/cSE 通过全局平均池化把每通道空间内容压成一个标量来做重校准——会**移除全部空间信息**。作者假设：在需要精确定位的分割任务（尤其首尾层空间尺度大时），这会损失相关信息，伤害小目标。
- **核心矛盾**：有限数据 + 有限算力下提升 3D 分割精度（特别是小目标定位），同时**不增加额外模型复杂度或 FLOP**。

## 4. 核心贡献
1. 提出 PE 模块——为重校准 3D F-CNN 量身定制，用沿三主轴投影替代全局池化以保留空间信息。
2. PE 可轻松集成进任意 F-CNN，提升分割性能，**对小目标类别尤其显著**。
3. 与"增加卷积层"相比，PE 极小幅度增加复杂度却带来更高精度，实证其重校准有效性。

## 5. 方法详解
- **整体框架**：编码器-解码器（3D U-Net），PE 放在每个编码器、瓶颈、解码器块后（P6 最佳）。
- **输入输出**：`U ∈ R^{H×W×D×C}` → `Û`，同维。
- **cSE 基线**：`z_c = (1/HWD)ΣΣΣ u_c(i,j,k)`（全局平均池化，公式 1）；`ẑ = σ(W2 δ(W1 z))`（两 FC 层，公式 2）；逐通道乘 `U`。
- **PE 模块**：
  1. **投影（公式 3–5）**：三路平均池化 → `z_h∈R^{C×H}`（池 W,D）、`z_w∈R^{C×W}`（池 H,D）、`z_d∈R^{C×D}`（池 H,W）。一个空间位置当且仅当其三个对应切片估值都高时才重要。
  2. **激励（公式 6）**：三向量 tile 回 `H×W×D×C` 后相加得 `Z`；过两个 **1×1×1 卷积**（先压 r 倍再还原）+ ReLU + Sigmoid，得通道-空间注意力 `ẑ`；`Û = ẑ ⊙ U = σ(V2 ⋆ δ(V1 ⋆ Z)) ⊙ U`。
- **与 cSE 差异**：cSE 用 FC + 全局池化丢空间；PE 用 1×1×1 卷积 + 三轴投影保空间，且不增 FLOP，并在每个阶段提供全局感受野。

## 6. 实验与结果
- **数据集**：MALC（脑 T1 MRI，30 卷，32 结构，15/3/12）；Visceral（增强 CT，20 标注卷，14 器官，5 折交叉验证，每折留一卷作验证）。共同挑战：数据少、类别严重不平衡。
- **对比**：3D U-Net 基线、3D cSE。**指标**：Mean Dice（±std）。
- **主结果（Table 3）**：
  - MALC：0.802 → cSE 0.825 → **PE 0.843**（+4%）。
  - Visceral：0.810 → cSE 0.797（−1%）→ **PE 0.846**（+3.5%）。
  - 大目标（WM/GM、肝/右肺）增益约 1% 以内；小目标增益约 3–36%（cSE 在气管、胸骨上反而掉点）。例：Inf. Lat. Vent. 0.242→0.604；Accumbens 0.483→0.735；Trachea 0.815→0.845（cSE 0.491↓）；Sternum 0.438→0.699（cSE 0.427↓）。
- **消融——位置（Table 1, MALC）**：P1 0.828 / P2 0.796 / P3 0.822 / P4 0.819 / P5 0.818 / **P6 0.843**。结论：编码器+瓶颈位置最有效，仅解码器几乎无效。
- **复杂度（Table 2）**：基线 5.57M。+cSE/+PE 均 +1.97%；+enc/dec 块 +39.7% 却降到 0.779（过拟合）；+2 卷积层 +3.97% 得 0.826（仍不及 PE）。证明收益来自重校准而非加参数。
- **速度/FLOPs**：未报告，但强调不增 FLOP、参数仅 +约 2%。

## 7. 这篇论文真正有价值的地方
1. **问题定位准**：把矛头对准全局池化丢空间，并用"大目标增益小、小目标增益大"的实验佐证假设。
2. **方案巧而省**：三轴投影是几乎零成本的结构化空间摘要，介于"完全压缩"与"完整三维注意力"之间，且不增 FLOP。
3. **对照消融硬核**：用"加 enc/dec 块掉点""加卷积层仍不及"两组对照，证明收益源于机制而非参数。
4. **工程实用**：即插即用、代码开源；但放置位置敏感，需调优。

## 8. 局限与问题
- 投影假设对复杂/各向异性目标可能不充分（论文未实验，属推测）。
- 评估仅两个标准化多结构任务，未覆盖肿瘤/病变。
- 未量化推理时间或 FLOPs 增量。
- 训练样本极少（15、20），泛化到更大/更复杂任务待验证。
- 放置位置敏感（P6 最佳、P2 最差），需按架构调优。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言末尾三点贡献 + 结论 + Table 1/2/3。
- **复现**：第 2 节公式 3–6（投影/激励）+ 第 3 节训练设置（3 enc/3 dec、通道减半、Instance Norm、batch=1、SGD 动量 0.9、lr 0.1、CE+Dice+中位数频率平衡）+ 开源仓库 `https://github.com/ai-med/squeeze_and_excitation`。
- **借鉴创新点**：学习"投影-激励"范式——先用有几何意义的操作得结构化中间表示，再做全局依赖建模；可迁移到点云、视频。
- **写 related work**：归入 1) 3D 医学图像分割，2) 注意力/特征重校准，3) 轻量级网络，4) 小目标分割。

## 10. 和其他论文的关系
依据正文引用：
- `[[3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation]]`（Çiçek 等, 参考[1]）：本文实验用的基础架构。
- `[[Squeeze-and-Excitation Networks]]`（Hu 等, CVPR 2018, 参考[2]）：PE 思想的 2D 起点。
- `[[AnatomyNet: Deep learning for fast and fully automated whole-volume segmentation of head and neck anatomy]]`（Zhu 等, 参考[10]）：本文对比的 3D cSE 即来自此文。
- `[[U-Net: Convolutional Networks for Biomedical Image Segmentation]]`（Ronneberger 等, 参考[5]）：相关工作基石。
- `[[Recalibrating Fully Convolutional Networks with Spatial and Channel Squeeze and Excitation Blocks]]`（Roy 等, IEEE TMI 2019, 参考[7]）：同团队在医学图像上用 SE 的前作。

## 11. 关键词
3D 医学图像分割, 体数据分割, 注意力机制, Project & Excite, Squeeze and Excitation, 特征重校准, 全卷积网络, 3D U-Net, MRI 全脑分割, CT 全身分割, 小目标分割, 轻量级模块

## 12. 可信度说明
本篇精读完全基于提供的 PDF 提取文本（9/9 页，含摘要、引言、方法公式 1–6、实验设置、Table 1–3 数值、结论与参考文献）。方法细节、数据集划分、Dice 数值（0.802/0.825/0.843、0.810/0.797/0.846 等）、复杂度（5.57M、+1.97%/+39.7%/+3.97%）均直接来自该文本。提取质量较好、结构清晰。文中未提供的内容（具体 FPS/FLOPs、更广的消融）已明确标注"未报告/属推测"。原笔记把 primary_topic 误标为"D_3D_点云"，本次据正文（体素级医学分割，非点云）改正为 A1_医学图像_分割；并修复了被截断的标题与乱码摘要。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2386 字符/页)); 来源缓存: `.paper-cache/extracts/PE3d.txt` (9/9 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本次复读校正: 分类 D_3D_点云→A1_医学图像_分割、标题补全、摘要重建、Visceral 增益 3.6%→3.5%、补全训练/小目标细节。
<!-- AI_READING_NOTE_END -->
