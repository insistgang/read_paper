---
title: Semantic Segmentation by Semantic Proportions
authors:
  - "Halil Ibrahim Aysel"
  - "Xiaohao Cai"
  - "Adam Prugel-Bennett"
year: 2023
venue: arXiv:2305.15608 (preprint, cs.CV)
doi: 
pdf: [[语义比例分割 Semantic Proportions.pdf]]
primary_topic: F_图像分割_语义_实例_全景
topics:
  - "F_图像分割_语义_实例_全景"
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
extract_cache: .paper-cache/extracts/语义比例分割 Semantic Proportions.txt
---

# Semantic Segmentation by Semantic Proportions

## 基本信息
- **PDF**: [[语义比例分割 Semantic Proportions.pdf]]
- **primary_topic**: `F_图像分割_语义_实例_全景`
- **topics**: `F_图像分割_语义_实例_全景`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Semantic Segmentation by Semantic Proportions |
| **作者** | Halil Ibrahim Aysel; Xiaohao Cai; Adam Prugel-Bennett（University of Southampton） |
| **发表时间** | 2023（arXiv 首发）；提取文本含 v2，2024-11-15 修订 |
| **刊物/会议** | arXiv:2305.15608（预印本，cs.CV） |
| **DOI** | 未明确（代码：github.com/Halilibrahimaysel/SemanticSegmentationbySemanticProportions） |

## 摘要

清理后英文原摘要（据 PDF 提取文本修复空格/连字符、剔除杂入文字）：

> Semantic segmentation is a critical task in computer vision aiming to identify and classify individual pixels in an image, with numerous applications in for example autonomous driving and medical image analysis. However, semantic segmentation can be highly challenging particularly due to the need for large amounts of annotated data. Annotating images is a time-consuming and costly process, often requiring expert knowledge and significant effort; moreover, saving the annotated images could dramatically increase the storage space. In this paper, we propose a novel approach for semantic segmentation, requiring the rough information of individual semantic class proportions, shortened as semantic proportions, rather than the necessity of ground-truth segmentation maps. This greatly simplifies the data annotation process and thus will significantly reduce the annotation time, cost and storage space, opening up new possibilities for semantic segmentation tasks where obtaining the full ground-truth segmentation maps may not be feasible or practical. Our proposed method of utilising semantic proportions can (i) further be utilised as a booster in the presence of ground-truth segmentation maps to gain performance without extra data and model complexity, and (ii) also be seen as a parameter-free plug-and-play module, which can be attached to existing deep neural networks designed for semantic segmentation. Extensive experimental results demonstrate the good performance of our method compared to benchmark methods that rely on ground-truth segmentation maps. Utilising semantic proportions suggested in this work offers a promising direction for future semantic segmentation research.

中文翻译：

> 语义分割是计算机视觉中的一项关键任务，目标是识别并分类图像中的每个像素，在自动驾驶、医学影像分析等领域有大量应用。然而语义分割极具挑战性，尤其是因为它需要大量带标注的数据。图像标注耗时且成本高，往往需要专业知识和大量投入；此外，保存标注后的图像还会显著增加存储空间。本文提出一种新的语义分割方法，只需各语义类别比例的粗略信息（简称"语义比例"，semantic proportions），而无需真值分割图。这极大简化了数据标注流程，从而显著降低标注时间、成本与存储空间，为那些难以或不便获取完整真值分割图的任务开辟了新可能。所提方法（i）在已有真值分割图时可作为"增强器（booster）"使用，在不增加额外数据与模型复杂度的情况下提升性能；（ii）也可视为一个无参数、即插即用的模块，附加到现有为语义分割设计的深度神经网络上。大量实验结果表明，相较依赖真值分割图的基准方法，本方法性能良好。利用语义比例为未来语义分割研究提供了一个有前景的方向。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：语义分割是计算机视觉的基础任务，应用广泛（自动驾驶、医学影像、增强现实、机器人）。深度网络的进步很大程度上依赖大规模像素级标注数据集，而像素级标注每个物体需 54–79 秒，含多个物体的图像往往要花几分钟；3D/体素标注更昂贵；存储标注数据本身也耗费大量空间。
- **之前方法的问题**：已有弱监督思路用图像级标签、涂鸦（scribbles）、眼动轨迹、点监督等更便宜的监督形式降低标注成本，但始终存在"标注成本 vs 模型性能"的权衡——监督越弱，性能通常越差。其他降本路线还包括主动学习（按不确定性挑信息量最大的样本标注）和合成数据增强。
- **核心思路**：本文改用图像中各语义类别的"比例/百分比"（semantic proportions, SP）作为监督信号。作者称这是首次将 SP 用于语义分割——它比图像级标签、边界框、涂鸦更粗、更易获取（如图 1：building 68%、water 4%、vegetation 7%），却能训出与全监督相当甚至更好的分割模型。

## 关键贡献

1.  **提出新范式与 SPSS 架构**：首次提出利用图像级"语义比例（SP）"进行语义分割，设计了对应的 SPSS（SP-based Semantic Segmentation）架构，仅需类别比例向量即可训练。
2.  **提出即插即用增强模块 SPSS+**：当存在真值分割掩码时，SP 损失可作为无参数、即插即用模块加到现有分割网络上，在不增加额外数据或模型复杂度的前提下"近乎免费"地提升性能。
3.  **跨领域实验验证**：在 4 个来自不同领域（卫星遥感、皮肤镜、电子显微、脑 MRI）的代表性基准数据集上做了大量实验，验证有效性与鲁棒性。
4.  **开辟新方向**：为利用弱标注数据进行语义分割给出了富有启发的讨论与未来方向。

## 方法

- **整体框架**：两个核心架构。
    1.  **SPSS**：仅用语义比例 ρ\* 训练（图 2）。
    2.  **SPSS+**：联合用语义比例 ρ\* 与像素级掩码 Y\* 训练，作为性能增强器（图 3）。
- **记号与输入输出**：图像 X_i∈R^{M×H}，每图至多含 C 个语义类。真值掩码 Y\*_i 是把各类二值掩码 {Y\*_ij} 堆叠成的张量（第 j 通道对应第 j 类）；SP 标注 ρ\*_i=(ρ\*_i1,…,ρ\*_iC)，每个 ρ\*_ij∈[0,1] 且 Σ_j ρ\*_ij=1。SPSS 训练只需 ρ\*；SPSS+ 额外需要 Y\*。输出为预测分割图 Y_i。
- **关键模块**：
    1.  **CNN 特征提取器**：用标准 CNN（U-Net / FPN，骨干 VGG16 或 ResNet34）从输入提取特征 Y_i。为输出 SP，在网络末端加 1×1 卷积（n 个滤波器以匹配 C 个类）；Aerial Dubai 取 n=6，医学影像二分类取 n=1（无需设 n=2），相应输出特征图尺寸 288×288×6 与 288×288×1。
    2.  **全局平均池化（GAP）层**：对特征 Y_i 做 GAP，得到 n 个浮点数即预测语义比例 ρ_i。
- **核心机制**：训练时只用 GAP 后的 ρ_i 与真值 ρ\*_i 算损失；但训练完成后，GAP **之前**的逐通道特征图本身"出乎意料地"就是各类分割掩码的预测——测试阶段提取 GAP 前的特征图、按类可视化即得分割结果。即全局比例这一统计约束，反向诱导网络学到了空间上判别性的逐类响应图。
- **损失函数**：
    - **L_sp（MSE）**：L_sp = (1/|Ω_T|) Σ_i ‖ρ\*_i − ρ_i‖²，约束预测比例逼近真值比例。(Eq. 1)
    - **L_sm（BCE）**：L_sm = (1/|Ω_T|) Σ_i Σ_j −(Y\*_ij·log Y_ij + (1−Y\*_ij)·log(1−Y_ij))，预测分割图与真值掩码的二元交叉熵。(Eq. 2)
    - **SPSS+ 总损失**：L_total = α·L_sp + (1−α)·L_sm，α 为权衡权重。(Eq. 3)
- **训练设置**：80/20 训练/测试划分；Adam，学习率 10⁻³，批大小 16；100 轮、基于验证损失早停（patience=10）。Aerial Dubai 用 U-Net/FPN×{VGG16,ResNet34}，其余医学数据集与全部消融统一用 U-Net+VGG16。
- **推理流程**：取 GAP 层之前的特征图，逐类可视化/阈值化即为最终分割。
- **与已有方法差异**：相比全监督无需像素级掩码；相比图像级标签/边界框/涂鸦等弱监督，SP 监督更粗、更易由人或算法估计，是更弱的监督形式。

## 实验

- **使用数据集**（4 个，跨领域）：
    1.  **Aerial Dubai**（卫星遥感，Kaggle）：8 个 tile，每 tile 9 张，6 类（building, land, road, vegetation, water, unlabeled）；切成 224×224 patch，共 1,647 张。
    2.  **ISIC**（皮肤镜图像）：2,594 训练 / 100 验证 / 1,000 测试，高分辨率皮肤病变图。
    3.  **Electron Microscopy**（电子显微，识别线粒体 mitochondria）：165 张 768×1024 切片，切成 256×256 patch 后共 1,980 张，类别严重不平衡（目标极小）。
    4.  **LGG Brain MRI**（TCGA/TCIA，Buda 等版本）：约 4,000 张脑 MRI（110 名患者，含 FLAIR）；256×256 中心裁剪到 144×144。
    - 预处理后**所有数据集（含 ISIC）统一 resize 到 288×288**，以保证尺寸一致。
- **对比方法**：全监督基准（用像素级掩码端到端训练）——U-Net 与 FPN，骨干 VGG16/ResNet34；与本文用 SP 的方法用相同训练图像做公平对比。
- **评价指标**：平均交并比（Mean IoU）与 F1。误差由随机初始化训练 3 次估计。
- **主实验结果**：
    - **Aerial Dubai（Table I）**：以 U-Net+VGG16 为例，Benchmark 71.3 mIoU / 88.3 F1，SPSS 64.2 / 83.7（仅用比例已接近），SPSS+ 71.6 / 88.7（超过基准）。除 FPN+VGG16 外，SPSS+ 在所有配置上均优于基准。
    - **医学影像（Table II，U-Net+VGG16）**：ISIC Benchmark 78.4 → SPSS 73.2 → SPSS+ 79.1；Mitochondria（电镜）Benchmark 83.7 → SPSS 76.5 → SPSS+ 84.3；Brain MRI Benchmark 72.3 → SPSS 69.5 → SPSS+ 72.8。三个数据集上 SPSS+ 均超基准。
    - **定性（Fig. 6/7）**：作者称本方法逐类分割图在二值化清晰度上"反而明显优于"全监督基准；在电镜难例上能分出基准漏掉的小线粒体。
- **消融实验**：提取文本（前 10 页）止于 Table II 与定性对比，正文提到 SP 经聚类退化（Section V-B2）等消融，但具体内容超出提取缓存范围，未覆盖。
- **泛化实验**：跨 4 个不同领域数据集验证，体现一定泛化能力。
- **效率信息**：硬件为个人笔记本（i7-8750H + GTX 1060 + 16GB RAM）；SPSS / SPSS+ 训练分别约 30 / 40 分钟。

## 局限

1.  **缺乏精细边界约束**：SP 是纯全局、粗粒度统计量，对物体边缘/形状无直接约束，这可能是 SPSS（仅用比例）略低于全监督的原因；对要求极精细边界的任务可能受限。
2.  **比例估计噪声未评估**：方法假设 SP 已给定，但实际由人或算法估计的比例可能有误差，提取文本（前 10 页）未讨论比例噪声对鲁棒性的影响（正文 V-B2 提到聚类退化方案，超出提取范围）。
3.  **极端类别不平衡的处理**：电子显微数据集类别严重不平衡（线粒体极小），小类别比例对损失贡献弱；论文虽展示该数据集上 SPSS+ 仍超基准，但针对不平衡的专门策略在提取文本中未深入说明。
4.  **未在大规模通用基准验证**：覆盖了 4 个领域，但规模中等，未在 Cityscapes、ADE20K 等大规模通用分割基准上验证。

## 个人评论

1.  **极低成本的全新监督信号**：语义比例比图像级标签、边界框更易获取，甚至可由非专业人员粗略目测估计（图 1 那种"building 68%、water 4%"式标注），为大规模廉价标注提供了新可能。
2.  **"比例约束"的引导能力出人意料**：仅靠 1×1 卷积 + GAP + MSE 这一极简结构，全局比例约束就能反向逼出空间上判别性的逐类特征图——训练只监督全局统计量，推理却拿到了像素级分割，机制优雅。
3.  **SPSS+ 接近"免费的午餐"**：对任何已有全监督分割网络，训练时加一项 SP 损失即可（无额外数据、无参数、无模型复杂度增加），表 I/II 显示几乎都能小幅提升，实践价值高。
4.  **对"信息量"的再认识**：即使是各类面积占比这种极粗的图像级统计，也蕴含足以训出优秀分割模型的信息，启发我们重估物体数量、相对大小等其他廉价信号的潜力。
5.  **需谨慎之处**：定性结论（"本方法二值化反而优于全监督"）颇强，需结合 mIoU/F1 综合看；且实验仅在 4 个中等规模数据集、最多 6 类的设定上验证，多类别复杂场景（如 Cityscapes 19 类）下比例约束是否仍足够判别，尚待检验。

### 使用建议

- **快速了解**：读 Abstract、Introduction（第 I 节）、图 1（与基准标注方式的对比）、图 2/图 3（SPSS / SPSS+ 架构），以及 Table I/II 与图 6/7 的定性对比。
- **复现**：精读第 III 节公式（Eq. 1–3）与架构，第 IV 节实验配置；注意网络改造（末端加 1×1 卷积匹配类数 + GAP 输出比例）、各数据集预处理与统一 resize 到 288×288、测试时取 GAP 前特征图作分割。
- **借鉴创新点**：
    1.  **SP 标注思想**：在自己领域（尤其标注成本高的医学/遥感）尝试用类别比例替代像素级掩码。
    2.  **SPSS+ 模块**：在已有全监督分割训练中加入 SP 损失，验证能否获得"免费"性能提升。
    3.  **设计新的全局约束损失**：思考其他全局统计量（长宽比分布、纹理分布、物体数量等）能否同样约束特征学习。
- **写 Related Work**：归入"弱监督语义分割 / 基于图像级信息的语义分割"，与图像级分类标签、涂鸦、边界框、点监督等弱监督方法对比，并指出 SP 是比上述更弱（更粗）的监督形式。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[F_图像分割_语义_实例_全景]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的语义分割，具体聚焦**弱监督语义分割**，并提出了一种比图像级标签/边界框/涂鸦更弱（更粗）的监督形式——图像级"语义比例（SP）"。核心要解决的是像素级标注成本高、存储大的问题。归入"F_图像分割_语义_实例_全景"主题下的弱监督子方向最贴切。

## 2. 一句话总结
本文提出"语义比例分割（SPSS）"：仅用图像中各类别的粗略面积占比（而非像素级真值掩码）经 MSE 损失训练 CNN，训练后 GAP 层之前的逐类特征图即成为分割预测；并给出即插即用的增强版 SPSS+，在有真值掩码时近乎免费地提升性能。

## 3. 背景与问题
- **为什么要做**：语义分割依赖大规模像素级标注，每物体标注耗时 54–79 秒，含多物体的图像要几分钟；3D/体素更贵；存储标注本身也昂贵。医学影像还需专家知识，全监督常不现实。
- **之前方法的问题**：图像级标签、涂鸦、眼动、点监督等弱监督能降本，但有"成本 vs 性能"的固有权衡；主动学习、合成数据是另两条降本路线。
- **核心思路**：改用各类比例（SP，如 building 68%/water 4%/vegetation 7%）作监督——比已有弱监督更粗更省，且作者称这是首次将 SP 用于语义分割。

## 4. 核心贡献
1.  **新方法 + 即插即用模块**：提出基于 SP 标注的 SPSS 架构与可附加到现有网络的无参数 SP 损失模块。
2.  **跨领域实验**：在卫星遥感、皮肤镜、电子显微、脑 MRI 4 个代表性数据集上充分验证有效性与鲁棒性。
3.  **有启发的讨论**：就弱标注数据下的语义分割与未来方向展开讨论。

## 5. 方法详解
- **两个架构**：SPSS（仅用 SP，图 2）；SPSS+（SP + 像素掩码联合，图 3，作增强器）。
- **记号**：图像 X_i∈R^{M×H}，至多 C 类；真值掩码 Y\*_i 为各类二值掩码堆叠的张量；SP 标注 ρ\*_i=(ρ\*_i1,…,ρ\*_iC)，ρ\*_ij∈[0,1]、Σ_j ρ\*_ij=1。
- **网络**：CNN（U-Net/FPN，骨干 VGG16/ResNet34）提特征 Y_i；末端加 1×1 卷积（n 滤波器匹配 C 类，Aerial n=6、医学二分类 n=1，输出 288×288×6 / 288×288×1）；再加 GAP 得 n 维预测比例 ρ_i。
- **损失**：L_sp=(1/|Ω_T|)Σ‖ρ\*_i−ρ_i‖²（MSE, Eq.1）；L_sm 为预测图与真值掩码的 BCE（Eq.2）；L_total=αL_sp+(1−α)L_sm（Eq.3，SPSS+）。
- **核心机制**：训练只监督 GAP 后的全局比例，但训练完成后 **GAP 之前**的逐类特征图本身就是分割预测——测试时提取 GAP 前特征图按类可视化即得分割。全局统计约束反向诱导出空间判别特征，是本文最反直觉、最关键之处。
- **训练**：80/20 划分，Adam lr=10⁻³，batch=16，100 轮、早停 patience=10；除 Aerial 用多骨干外，医学与全部消融统一 U-Net+VGG16。

## 6. 实验与结果
- **数据集**：Aerial Dubai（6 类，224×224 patch，1,647 张）；ISIC（2,594/100/1,000）；Electron Microscopy（165 张 768×1024 → 256×256 patch，共 1,980 张，识别线粒体，严重不平衡）；LGG Brain MRI（约 4,000 张，256×256 中心裁 144×144）。全部统一 resize 到 288×288。
- **基准**：全监督 U-Net / FPN（VGG16/ResNet34），同样训练图像公平对比。
- **指标**：Mean IoU、F1；随机初始化训练 3 次估计误差。
- **结果**：
    - Aerial（Table I, U-Net+VGG16）：Benchmark 71.3 mIoU → SPSS 64.2 → SPSS+ 71.6；除 FPN+VGG16 外 SPSS+ 全面超基准。
    - 医学（Table II, U-Net+VGG16）：ISIC 78.4→73.2→79.1；Mitochondria 83.7→76.5→84.3；Brain MRI 72.3→69.5→72.8。三者 SPSS+ 均超基准。
    - 定性（Fig.6/7）：作者称逐类分割图二值化清晰度反而优于全监督；电镜难例能分出基准漏检的小线粒体。
- **效率**：i7-8750H + GTX 1060 + 16GB；SPSS/SPSS+ 训练约 30/40 分钟。
- **消融/聚类退化（V-B2）等内容超出提取缓存（前 10 页），未覆盖。**

## 7. 这篇论文真正有价值的地方
1.  **极低成本监督信号**：SP 比图像级标签/边界框更易获取，可粗略目测估计，为廉价大规模标注开新路。
2.  **"比例约束"反向引导空间分割**：仅 1×1 卷积 + GAP + MSE，全局比例就能逼出逐类判别特征图，机制优雅且反直觉。
3.  **SPSS+ 近乎免费的提升**：对已有全监督网络只加一项 SP 损失，无额外数据/参数/复杂度，表 I/II 几乎都小幅提升。
4.  **重估廉价信息的潜力**：粗糙的面积占比即蕴含足够训练信息，启发利用数量、相对大小等其他廉价统计量。

## 8. 局限与问题
1.  **无精细边界约束**：SP 纯全局粗粒度，缺边缘/形状监督，可能是 SPSS 略低于全监督的原因，对极精细边界任务受限。
2.  **比例噪声未评估**：假设 SP 已给定，估计误差对鲁棒性的影响在提取文本（前 10 页）未讨论。
3.  **极端不平衡处理**：电镜小目标比例对损失贡献弱；专门策略在提取文本中未深入说明。
4.  **未在大规模通用基准验证**：4 个数据集规模中等、类别少（≤6），未在 Cityscapes/ADE20K 等验证。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract、第 I 节、图 1/2/3、Table I/II、图 6/7。
- **复现**：第 III 节公式（Eq.1–3）与架构，第 IV 节配置；注意 1×1 卷积匹配类数 + GAP 输出比例、各数据集预处理与统一 288×288、测试取 GAP 前特征图。
- **借鉴**：把 SP 范式用于自己领域；在已有全监督训练中加 SP 损失验证免费增益；探索其他全局统计量作约束。
- **写 Related Work**：归入弱监督语义分割，与图像级标签、涂鸦、边界框、点监督对比，强调 SP 是更弱的监督。

## 10. 和其他论文的关系
基于主题"F_图像分割_语义_实例_全景"与论文引用：
- 弱监督语义分割（图像级标签 [11]、边界框 [15,16]、涂鸦 [12,17]、点监督 [8,14]）——本文对照的同类更强监督。
- DNN 分割骨架：FCN [21]、SegNet [22]、DeepLab [23]、本文采用的 U-Net [[U-Net: Convolutional Networks for Biomedical Image Segmentation]] [24] 与 FPN [32]。
- 主动学习 [18,19] 与合成数据 [20] 是论文提到的其他降本路线，与 SP 思路互补。

## 11. 关键词
语义分割, 语义比例(SP), 弱监督学习, SPSS/SPSS+, 全局平均池化, 即插即用模块, MSE/BCE 损失, 医学图像分割, 卫星遥感分割

## 12. 可信度说明
本笔记基于 PDF 提取文本（前 10 页 / 共约 51,225 字符，提取覆盖 25,000 字符）生成，已涵盖摘要、引言、相关工作、方法（含 Eq.1–3 与 SPSS/SPSS+ 架构）、数据与设置、Table I/II 主结果及定性对比。受提取截断限制，正文后续的消融（含 SP 聚类退化 V-B2）、更详细讨论与结论部分未覆盖；相关处已在文中标注"超出提取范围"。原笔记中"水占 4%"被误系于电镜不平衡——经核实该例来自 Aerial Dubai 图 1（building 68%/water 4%/vegetation 7%），本次已更正；并补全电镜 patch 数（1,980）、统一 resize 288×288、Mitochondria 表数等细节。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2504 字符/页)); 来源缓存: `.paper-cache/extracts/语义比例分割 Semantic Proportions.txt` (10/10 页, 提取覆盖前 25000/51225 字符); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮据提取文本复核更正。
<!-- AI_READING_NOTE_END -->
