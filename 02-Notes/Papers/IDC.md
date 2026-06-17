---
title: "InceptionNeXt: When Inception Meets ConvNeXt"
authors:
  - "Weihao Yu"
  - "Pan Zhou"
  - "Shuicheng Yan"
  - "Xinchao Wang"
year: 2023
venue: "arXiv"
doi: 
pdf: [[IDC.pdf]]
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
extract_cache: .paper-cache/extracts/IDC.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/14 pages"
---
# InceptionNeXt: When Inception Meets ConvNeXt

## 基本信息
- **PDF**: [[IDC.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | InceptionNeXt: When Inception Meets ConvNeXt |
| **作者** | Weihao Yu; Pan Zhou; Shuicheng Yan; Xinchao Wang (NUS & Sea AI Lab) |
| **发表时间** | 2023 (arXiv:2303.16900v1, 29 Mar 2023) |
| **刊物/会议** | arXiv |
| **代码** | https://github.com/sail-sg/inceptionnext |
| **DOI** | 未明确 |

## 摘要

清理后的英文原摘要（修复空格/连字符、剔除杂入的图表坐标数字）：

> Inspired by the long-range modeling ability of ViTs, large-kernel convolutions are widely studied and adopted recently to enlarge the receptive field and improve model performance, like the remarkable work ConvNeXt which employs 7×7 depthwise convolution. Although such depthwise operator only consumes a few FLOPs, it largely harms the model efficiency on powerful computing devices due to the high memory access costs. For example, ConvNeXt-T has similar FLOPs with ResNet-50 but only achieves 60% throughputs when trained on A100 GPUs with full precision. Although reducing the kernel size of ConvNeXt can improve speed, it results in significant performance degradation. It is still unclear how to speed up large-kernel-based CNN models while preserving their performance. To tackle this issue, inspired by Inceptions, we propose to decompose large-kernel depthwise convolution into four parallel branches along channel dimension, i.e. small square kernel, two orthogonal band kernels, and an identity mapping. With this new Inception depthwise convolution, we build a series of networks, namely IncepitonNeXt, which not only enjoy high throughputs but also maintain competitive performance. For instance, InceptionNeXt-T achieves 1.6× higher training throughputs than ConvNeXt-T, as well as attains 0.2% top-1 accuracy improvement on ImageNet-1K. We anticipate InceptionNeXt can serve as an economical baseline for future architecture design to reduce carbon footprint.

中文翻译：

> 受 ViT 长距离建模能力的启发，大核卷积近年被广泛研究和采用，用以扩大感受野、提升模型性能，例如采用 7×7 深度卷积的代表性工作 ConvNeXt。尽管这种深度卷积算子本身只消耗少量 FLOPs，但由于内存访问成本高，它在强算力设备上严重损害模型效率。例如 ConvNeXt-T 与 ResNet-50 的 FLOPs 相近，但在 A100 GPU 上全精度训练时吞吐量只有 60%。虽然减小 ConvNeXt 的核尺寸可以提速，但会带来显著的性能下降。如何在保持性能的同时加速基于大核的 CNN 仍不清楚。为解决该问题，受 Inception 启发，我们提出沿通道维度将大核深度卷积分解为四个并行分支：小方核、两个正交带状核，以及一个恒等映射。基于这一全新的 Inception 深度卷积，我们构建了一系列网络 InceptionNeXt，既享有高吞吐又保持有竞争力的性能。例如 InceptionNeXt-T 的训练吞吐量比 ConvNeXt-T 高 1.6 倍，同时在 ImageNet-1K 上 top-1 精度提升 0.2%。我们期望 InceptionNeXt 能作为未来架构设计的经济基线，以减少碳足迹。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：受视觉 Transformer（ViT）长距离建模能力的启发，大核卷积（如 ConvNeXt 中的 7×7 深度卷积）被广泛采用以扩大感受野、提升 CNN 性能。然而大核深度卷积虽 FLOPs 小，却是一个"昂贵"算子——它带来高内存访问成本，在 GPU 等强算力设备上成为瓶颈（论文引 ShuffleNetV2 [40] 的观察）。
- **之前方法的问题**：以 ConvNeXt-T 为例，其 FLOPs 与 ResNet-50 相近，但在 A100 上全精度训练吞吐量只有 60%。论文进一步给出 Figure 1 的对比：默认 7×7 核的 ConvNeXt-T 比 3×3 核版本慢 **1.4×**，比 ResNet-50 慢 **1.8×**（三者 FLOPs 相近）。而直接缩小核尺寸虽能提速，却会降性能——ConvNeXt-T/k3 相对 ConvNeXt-T/k7 在 ImageNet-1K 上 top-1 下降 **0.6%**。
- **核心矛盾**：如何在保持大核带来的大感受野与高性能的同时解决其低效问题，即在精度-速度权衡上做得更好。论文明确不追求把核做得更大（区别于 RepLKNet 31×31、VAN 21×21），而是面向效率把大核以速度友好的方式分解。

## 关键贡献

论文原文自述贡献是 **two-fold（两点）**：

1.  **提出 Inception 深度卷积（Inception Depthwise Convolution）**：将昂贵的大核深度卷积分解为**三个小核卷积分支**（3×3 小方核、1×k 带状核、k×1 带状核）加**一个恒等映射分支**，沿通道维度并行。
2.  **大量实验验证**：在图像分类与语义分割上的实验表明，所构建的 InceptionNeXt 相比 ConvNeXt 取得更好的速度-精度权衡；期望它能作为加速架构设计研究的新 CNN 基线。

笔记补充（属本笔记归纳，非原文逐条列出）：论文还据预实验（Appendix A / Table 10）实证"并非所有通道都需做昂贵深度卷积"，由此引入恒等映射分支（思想源自 ShuffleNetV2 的部分通道处理）；并基于该算子构建了 InceptionNeXt-T/S/B 系列，沿用类 MetaNeXt 的简洁模块设计。

## 方法

- **整体框架**：InceptionNeXt 采用与 ResNet、ConvNeXt 类似的 **4 阶段金字塔**结构。各 stage 的 block 数为 S 尺寸 `[3, 3, 9, 3]`、B 尺寸 `[3, 3, 27, 3]`（Table 2）。下采样用 4×4 stride-4（stem）与 2×2 stride-2。论文采用 **Batch Normalization**（强调速度），并在 stage 4 把 MLP ratio 从 4 降到 3、把省下的参数移给分类器，base 尺寸可省约 3% FLOPs。
- **MetaNeXt 抽象（3.1）**：论文沿用 MetaFormer 的 "token mixer" 视角，把 ConvNeXt 块抽象为 MetaNeXt 块。关键区别：MetaFormer 块有**两个**残差捷径（token mixer 一个、MLP 一个），MetaNeXt 把两个残差子块合并为**一个**捷径，因此更快、更简——但代价是其 token mixer 不能太复杂（如自注意力会训练不收敛，见 Table 3）。把 token mixer 指定为深度卷积即得 ConvNeXt 块，指定为 Inception 深度卷积即得 InceptionNeXt 块。
  - 块公式：`X' = TokenMixer(X)` → `Y = Norm(X')` → `Y = Conv_{1×1}^{rC→C}{σ[Conv_{1×1}^{C→rC}(Y)]} + X`（残差只加一次，MLP 即两层 1×1 卷积夹一个激活）。
- **Inception 深度卷积机制（3.2）**：输入 `X ∈ R^{B×C×H×W}`，沿通道分为四组（Eq. 5）：`X_hw, X_w, X_h, X_id = X_{:,:g}, X_{:,g:2g}, X_{:,2g:3g}, X_{:,3g:}`，其中 `g = r_g·C` 为每个卷积分支的通道数，分支比例 `r_g` 默认 **1/8**（Table 2 "Conv. group ratio 1/8"）。四分支并行（Eq. 6）：
    - `X_hw` → 3×3 深度卷积（`k_s = 3`，小方核）。
    - `X_w` → 1×k_b 深度卷积（带状核，`k_b = 11`）。
    - `X_h` → k_b×1 深度卷积（带状核，`k_b = 11`）。
    - `X_id` → 恒等映射（不变）。
    - 最后沿通道拼接 `X' = Concat(X'_hw, X'_w, X'_h, X'_id)`（Eq. 7）。
- **关于 "1/3" 与 "1/8" 的辨析**：引言里说"对**处理通道**，1/3 用 3×3、1/3 用 1×k、1/3 用 k×1"，指的是被处理（非恒等）的那部分通道再三等分；而 1/8 是每个卷积分支占**总通道** C 的比例（即三个卷积分支共占 3/8，剩下 5/8 走恒等映射）。Algorithm 1 中恒等分支通道数为 `in_channels − 3·gc`。
- **复杂度（Table 1）**：常规卷积 Params=`k²C²`、FLOPs=`2k²C²HW`；深度卷积 Params=`k²C`、FLOPs=`2k²CHW`（对核尺寸 k 平方）；**Inception 深度卷积 Params=`(2k+9)C/8`、FLOPs=`(2k+9)CHW/4`**，对 k 是**线性**关系，故 k 越大节约越显著（Figure 3）。
- **与已有方法的差异**：
    - 与**标准深度卷积**（ConvNeXt）相比：FLOPs/参数随核尺寸线性而非平方增长，更高效。
    - 与 **Inception v3** 的 1×k / k×1 分解相比：Inception v3 是**顺序堆叠**，本文是**并行分支**（更并行友好）；本文还刻意避开大方核（如 5×5）因其实测慢。
    - 与 **SLaK**（把 k×k 分解为 k×s 和 s×k, s<k）相比：本文不追求放大核，且额外引入恒等分支与 3×3 小方核分支。
- **训练设置（4.1）**：ImageNet-1K，主要沿用 DeiT 超参（不蒸馏），AdamW 优化器，学习率 `lr = 0.001×batchsize/1024`（论文用 batchsize=4096，即 lr=4e-3，与 ConvNeXt 一致）；数据增强含 random resized crop、horizontal flip、RandAugment、Mixup、CutMix、Random Erasing 等。

## 实验

- **数据集**：ImageNet-1K（分类，约 130 万训练 / 5 万验证），ADE20K（语义分割）。
- **对比方法**：DeiT-S/B、T2T-ViT、TNT、Swin-T/S/B、Focal-T/S/B、PVT、ResNet-50/101/152(及 RSB 版)、RegNetY、FocalNet-T/S/B、RepLKNet-31B、ConvNeXt-T/S/B 等。
- **评价指标**：ImageNet top-1 (%)、训练/推理吞吐量 (img/s，A100、batch 128、FP32、PyTorch 1.13/CUDA 11.7)、参数量 (M)、MACs (G)、mIoU (%)。
- **主实验结果**：
    - **ImageNet-1K 分类（Table 4）**：InceptionNeXt 全面优于同级 ConvNeXt。
        - T：**82.3% vs 82.1%**（+0.2），训练吞吐 901 vs 575（**+57%**），推理 2900 vs 2413（**+20%**）；参数 28M/4.2G。其训练吞吐接近 ResNet-50（969 img/s）而精度远高（vs 78.4%）。
        - S：**83.5% vs 83.1%**（+0.4），训练 521 vs 361（**+44%**），推理 1750 vs 1535（**+14%**）；49M/8.4G。
        - B：**84.0% vs 83.8%**（+0.2），训练 375 vs 267（**+40%**），推理 1244 vs 1122（**+11%**）；87M/14.9G。
        - B@384：**85.2% vs 85.1%**（+0.1），训练 139 vs 95（**+46%**），推理 428 vs 393（+9%）。
    - **同构（isotropic）模型对比（Table 3）**：22M 档 InceptionNeXt-S(iso.) 79.7% 与 ConvNeXt-S(iso.) 79.7%、DeiT-S 79.8% 持平；87M 档 InceptionNeXt-S(iso.) **82.1%** 略高于 ConvNeXt-S(iso.) 82.0%、DeiT-B 81.8%。**MetaNeXt-Attn**（token mixer 换成自注意力）只有 **3.9%**——印证 MetaNeXt 单残差结构下复杂 token mixer 不收敛。
    - **ADE20K 语义分割（两套头）**：
        - **UperNet（Table 5）**：InceptionNeXt 全面优于 Swin/ConvNeXt 且参数/MACs 更少。T mIoU **47.9 vs ConvNeXt-T 46.7 / Swin-T 45.8**；S 50.0 vs 49.6 / 49.5；B 50.6 vs 49.9 / 49.7。
        - **Semantic FPN（Table 6）**：InceptionNeXt-T 43.1（vs PoolFormer-S24 40.3、PVT-Small 39.8、ResNet-50 36.7）；-S 45.6；-B 46.4，均优于同档对手。
- **效率分析**：Table 1 与 Figure 3 从理论给出线性 vs 平方复杂度；Table 4 给出 A100 上 FP32 的实测训练/推理吞吐，强调"小 FLOPs ≠ 高速度"。
- **消融/预实验**：恒等分支的依据来自 Appendix A（Table 10）的部分通道处理预实验。**(据原文后续页, 提取缓存仅覆盖前 12/14 页, Appendix A 的具体数字未在提取文本中, 待核)**

## 局限

1.  **场景/硬件依赖**：速度收益建立在特定软硬件栈（PyTorch 1.13、CUDA 11.7、A100 GPU、FP32、Channel First/Last 取优）上；论文自己也指出在其环境下 ConvNeXt 吞吐都比原论文高，说明吞吐数高度依赖实现与硬件，边缘设备/其他框架上的优势需另测。
2.  **任务范围**：实验集中在图像分类与语义分割（ADE20K），目标检测、视频理解等任务未验证。
3.  **超参为经验设定**：分支核尺寸（3、11）与通道比例（1/8）来自经验/调参，论文未给最优化或理论依据。
4.  **不追求更大核的取舍**：本文方法明确不放大核，与 RepLKNet(31×31)、VAN(21×21)、FocalNet 等"超大核/复杂分解"路线的精度上界对比是有限的（Table 4 列了部分，但论文核心对照系是 ConvNeXt）。

## 个人评论

1.  **"取 Transformer 之长、回归 CNN 之效"的范例**：用大核模拟注意力的全局感受野，但用算子分解换回 CNN 的高吞吐，思路干净、落地性强。
2.  **即插即用算子**：Inception 深度卷积可直接替换 ConvNeXt 类模型中的大核深度卷积 token mixer，Algorithm 1 仅十余行 PyTorch，复现/迁移成本极低。
3.  **强调"吞吐量"而非只看 FLOPs**：在 A100 上以实测 img/s 公平对比，提醒社区 FLOPs 是误导性指标——这是本文最有现实意义的方法论贡献。
4.  **侧面验证 MetaNeXt 单残差设计**：Table 3 中自注意力 token mixer 崩到 3.9%，说明简化块结构对 token mixer 复杂度有约束，是个值得注意的工程边界。

### 使用建议

- **快速了解**：读摘要、引言、Figure 1（精度-吞吐权衡）和 Figure 2（四种 block 对比）。
- **复现**：看 3.2 节（Eq. 5-7）+ Algorithm 1（PyTorch 代码）+ Table 2（各尺寸配置）。
- **借鉴创新点**：把大核分解为"小方核 + 两个正交带状核 + 恒等"的并行结构，可调分支核大小与通道比例。
- **写 Related Work**：归入"高效 CNN 架构 / 大核卷积设计 / CNN 现代化"，与 ConvNeXt、RepLKNet、SLaK、VAN、FocalNet 并列。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的**高效网络架构 / 卷积算子模块设计**方向。它以 ConvNeXt 为基线，针对现代大核 CNN 骨干的**计算效率瓶颈**（大核深度卷积内存访问成本高、GPU 上慢），提出一个新的空间混合算子（Inception 深度卷积）来替换 ConvNeXt 块中的 token mixer，从而在精度-吞吐权衡上取得更优解。本库主题标签为 `B_注意力算子模块`；严格说本文不是注意力，而是把"token mixer 算子模块"做高效化——论文正是借 MetaFormer 的 token-mixer 抽象来组织全文，因此放入"算子/模块"主题是合适的（其更精确的归类是"高效 CNN 算子模块"）。

## 2. 一句话总结
把大核深度卷积沿通道分解为四个并行分支（3×3 小方核、1×11 与 11×1 两个正交带状核、一个恒等映射），构建 InceptionNeXt 系列，在 ImageNet-1K 上相对 ConvNeXt 同精度甚至更高的同时，训练吞吐提升 40%-57%、推理提升 9%-20%。

## 3. 背景与问题
- **为什么做**：大核深度卷积（ConvNeXt 7×7）虽 FLOPs 小，但内存访问成本高，在 A100 上 ConvNeXt-T 吞吐只有 ResNet-50 的 60%；Figure 1 显示 7×7 比 3×3 慢 1.4×、比 ResNet-50 慢 1.8×（FLOPs 相近）。
- **之前方法的问题**：缩小核能提速但掉精度（ConvNeXt-T/k3 比 /k7 掉 0.6% top-1）；RepLKNet/VAN/FocalNet/SLaK 等只追求更大核或更强性能，忽视效率，速度都不如 ConvNeXt，而 ConvNeXt 相对 ResNet 本身也不算高效。
- **核心矛盾**：如何在保留大感受野（高性能）的同时，以速度友好的方式分解大核，回到 CNN 应有的效率优势。

## 4. 核心贡献
论文自述为**两点**：
1.  **Inception 深度卷积**：把昂贵的大核深度卷积分解为三个小核卷积分支（3×3、1×k、k×1）加一个恒等映射分支，沿通道并行。
2.  **大量实验**：分类 + 分割实验表明 InceptionNeXt 相对 ConvNeXt 有更好的速度-精度权衡，可作为加速架构研究的新 CNN 基线。
（本笔记补充的"部分通道处理预实验依据""InceptionNeXt-T/S/B 系列"是对正文的归纳，非原文逐条贡献。）

## 5. 方法详解
- **整体框架**：4 阶段金字塔；block 数 S=[3,3,9,3]、B=[3,3,27,3]；采用 BatchNorm（重速度）；stage 4 的 MLP ratio 由 4 降到 3 并把参数移给分类器（base 省约 3% FLOPs）。
- **MetaNeXt 抽象**：MetaFormer 有两个残差（token mixer 一个、MLP 一个），MetaNeXt 合并为一个残差 → 更快更简，但 token mixer 不能太复杂（自注意力会不收敛，Table 3 中崩到 3.9%）。token mixer = 深度卷积 → ConvNeXt 块；= Inception 深度卷积 → InceptionNeXt 块。块流程：TokenMixer → Norm → 两层 1×1 卷积 MLP（夹激活）+ 单残差。
- **Inception 深度卷积（Eq. 5-7）**：沿通道分四组 `X_hw, X_w, X_h, X_id`，每个卷积分支通道数 `g = r_g·C`，`r_g` 默认 1/8（三个卷积分支共占 3/8，恒等占 5/8）。`X_hw`→3×3（k_s=3）；`X_w`→1×11（k_b=11）；`X_h`→11×1；`X_id` 恒等；末尾通道拼接。引言里"处理通道 1/3 / 1/3 / 1/3"指的是被处理那部分再三等分，与 1/8 的总通道比例口径不同。
- **复杂度（Table 1）**：常规卷积 Params=k²C²、FLOPs=2k²C²HW；深度卷积 Params=k²C、FLOPs=2k²CHW（对 k 平方）；Inception 深度卷积 Params=(2k+9)C/8、FLOPs=(2k+9)CHW/4（对 k 线性，Figure 3 印证）。
- **与已有差异**：vs ConvNeXt 标准深度卷积更高效；vs Inception v3 顺序 1×k/k×1 用并行分支且避开大方核；vs SLaK（k×s + s×k）不放大核、加恒等与 3×3 分支。
- **训练**：DeiT 超参（不蒸馏），AdamW，lr=0.001×bs/1024（bs=4096 → 4e-3），含 RandAugment/Mixup/CutMix/Random Erasing 等。

## 6. 实验与结果
- **数据集**：ImageNet-1K（分类）、ADE20K（分割，UperNet 与 Semantic FPN 两套头）。
- **对比**：DeiT、Swin、Focal/FocalNet、T2T-ViT、TNT、PVT、ResNet(-RSB)、RegNetY、RepLKNet-31B、ConvNeXt 等。
- **指标**：top-1 (%)、A100/FP32/batch128 训练与推理吞吐 (img/s)、参数 (M)、MACs (G)、mIoU (%)。
- **ImageNet-1K（Table 4）**：
    - T 82.3 vs ConvNeXt-T 82.1（+0.2），训练 901 vs 575（+57%），推理 2900 vs 2413（+20%）；28M/4.2G。
    - S 83.5 vs 83.1（+0.4），训练 521 vs 361（+44%），推理 1750 vs 1535（+14%）；49M/8.4G。
    - B 84.0 vs 83.8（+0.2），训练 375 vs 267（+40%），推理 1244 vs 1122（+11%）；87M/14.9G。
    - B@384 85.2 vs 85.1（+0.1），训练 139 vs 95（+46%）。
- **isotropic（Table 3）**：87M 档 InceptionNeXt-S(iso.) 82.1 略高于 ConvNeXt-S(iso.) 82.0、DeiT-B 81.8；MetaNeXt-Attn 仅 3.9（自注意力 token mixer 不收敛）。
- **ADE20K UperNet（Table 5）**：T 47.9 vs ConvNeXt-T 46.7 / Swin-T 45.8；S 50.0 vs 49.6 / 49.5；B 50.6 vs 49.9 / 49.7（且参数/MACs 更少）。
- **ADE20K Semantic FPN（Table 6）**：T 43.1 / S 45.6 / B 46.4，均优于 PoolFormer、PVT、ResNet 等同档。
- **效率**：Table 1 + Figure 3 理论复杂度；Table 4 实测吞吐，主张以吞吐而非 FLOPs 评效率。

## 7. 这篇论文真正有价值的地方
1.  **"取 Transformer 之长、回归 CNN 之效"** 的清晰范例：大核换全局感受野，分解换回高吞吐。
2.  **即插即用高效算子**：十余行 PyTorch（Algorithm 1）可替换 ConvNeXt 大核 token mixer，迁移成本极低。
3.  **强调实测吞吐而非 FLOPs**：A100/FP32 公平对比，纠正"小 FLOPs = 快"的误区。
4.  **侧证简洁块的边界**：MetaNeXt 单残差结构下复杂 token mixer 会崩，给后续 block 设计划了条警戒线。

## 8. 局限与问题
1.  **硬件/实现依赖**：吞吐高度依赖 PyTorch/CUDA/A100/FP32 与内存布局取优，边缘设备与其他框架上的收益需另测（论文自承其环境下 ConvNeXt 吞吐都高于原论文）。
2.  **任务范围窄**：仅分类与分割，检测/视频未验证。
3.  **超参经验化**：核 3/11、比例 1/8 无理论/最优化依据。
4.  **不放大核的取舍**：与 RepLKNet/VAN/FocalNet 等超大核或复杂分解路线的精度上界对比有限。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + Figure 1（权衡）+ Figure 2（block 对比）。
- **复现**：3.2 节 Eq. 5-7 + Algorithm 1 + Table 2 配置。
- **借鉴创新点**：把大核拆成"小方核 + 两个正交带状核 + 恒等"的并行结构，可调分支核与通道比例。
- **写 Related Work**：归入高效 CNN / 大核卷积 / CNN 现代化，与 ConvNeXt、RepLKNet、SLaK、VAN、FocalNet 并列。

## 10. 和其他论文的关系
- **ConvNeXt [[ConvNeXt]]**：直接基线与改进对象（token mixer 被替换）。
- **Inception Nets [[Inception Net]]**：3×3/带状核并行分支的思想来源（Inception v1/v3）。
- **MetaFormer [[MetaFormer]]**：本文 MetaNeXt 抽象（token mixer 视角）的来源。
- **Swin Transformer [[Swin Transformer]]**：主要对照的 ViT 变体（模型配置也对齐 Swin/ConvNeXt）。
- **RepLKNet [[RepLKNet]]、SLaK [[SLaK]]、VAN、FocalNet**：同属大核卷积效率/设计的相关工作（本文不放大核，方向不同）。
- **ShuffleNetV2 [[ShuffleNetV2]]**：启发"部分通道处理"（恒等映射分支）。

## 11. 关键词
Inception 深度卷积, 高效 CNN, 大核卷积分解, 带状核, 恒等映射, token mixer, MetaNeXt, 吞吐量, ConvNeXt, ImageNet 分类, ADE20K 分割

## 12. 可信度说明
本精读基于 PDF 提取文本（前 12/14 页）。该文本完整覆盖了摘要、引言、相关工作、方法（3.1 MetaNeXt、3.2 Inception 深度卷积 + Algorithm 1 + Table 1 复杂度）、以及实验主表（Table 2 配置、Table 3 isotropic、Table 4 ImageNet、Table 5/6 ADE20K）。笔记中所有具体数字（精度、吞吐百分比、mIoU、复杂度公式、超参）均可在提取文本逐项核对。**未覆盖部分**：Appendix A / Table 10 的部分通道处理预实验具体数字、p.13-14（主要为参考文献），笔记中相应处已标注"待核"。本轮相对原笔记修正了两点关键事实：(a) 论文自述贡献是 two-fold 而非 4 点（原笔记把归纳当成原文贡献）；(b) Inception 深度卷积的 FLOPs 应为 (2k+9)CHW/4（原笔记只给了 Params 的 (2k+9)C/8 并写成"复杂度"），并补全了 Semantic FPN(Table 6)、Figure 1 的 1.4×/1.8× 倍数、训练超参与 BN 等细节。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/IDC.txt` (提取覆盖 12/14 页; 方法与主实验表均完整, Appendix A 数字与 p.13-14 未覆盖); 生成日期: 2026-06-05; 本轮重读优化: 2026-06-18; 模式: LLM (mimo-v2.5-pro) + 人对照提取文本核改.
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-14; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-14。
- **提取情况**: 缺失页 2 页, 其中 2 页提取到可读文本。缺失页主要为参考文献, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Grad-cam: Visual explanations from deep networks via
- p.13: Yoshua Bengio and Yann LeCun, editors, 3rd International
- p.13: Conference on Learning Representations, ICLR 2015, San
- p.13: Diego, CA, USA, May 7-9, 2015, Conference Track Proceed-
- p.13: Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent
- p.13: Pyramid vision transformer: A versatile backbone for dense
- p.13: IEEE/CVF international conference on computer vision ,
- p.13: IEEE conference on computer vision and pattern recogni-
- p.13: Zi-Hang Jiang, Francis EH Tay, Jiashi Feng, and Shuicheng
- p.14: Moya Chen, Shuohui Chen, Christopher Dewan, Mona Diab,
- p.14: Shufflenet: An extremely efficient convolutional neural net-

### 缺失页关键摘录

- p.14: ade20k dataset. In Proceedings of the IEEE conference on
<!-- AI_READING_NOTE_END -->
