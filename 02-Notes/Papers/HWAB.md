---
title: "Half Wavelet Attention on M-Net+ for Low-Light Image Enhancement"
authors:
  - "Chi-Mao Fan"
  - "Tsung-Jung Liu"
  - "Kuan-Hsien Liu"
year: 2022
venue: "arXiv (eess.IV)"
doi: 
pdf: [[HWAB.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
extract_cache: .paper-cache/extracts/HWAB.txt
---

# Half Wavelet Attention on M-Net+ for Low-Light Image Enhancement

## 基本信息
- **PDF**: [[HWAB.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Half Wavelet Attention on M-Net+ for Low-Light Image Enhancement |
| **作者** | Chi-Mao Fan; Tsung-Jung Liu (National Chung Hsing University); Kuan-Hsien Liu (National Taichung University of Science and Technology), Taiwan |
| **发表时间** | 2022 (arXiv:2203.01296v1, 2 Mar 2022) |
| **刊物/会议** | arXiv (eess.IV) |
| **DOI** | 未明确 (arXiv:2203.01296) |
| **代码** | https://github.com/FanChiMao/HWMNet |

## 摘要

> Low-Light Image Enhancement is a computer vision task which intensifies the dark images to appropriate brightness. It can also be seen as an ill-posed problem in the image restoration domain. With the success of deep neural networks, the convolutional neural networks surpass the traditional algorithm-based methods and become the mainstream in the computer vision area. To advance the performance of enhancement algorithms, we propose an image enhancement network (HWMNet) based on an improved hierarchical model: M-Net+. Specifically, we use a half wavelet attention block on M-Net+ to enrich the features from the wavelet domain. Furthermore, our HWMNet has competitive performance results on two image enhancement datasets in terms of quantitative metrics and visual quality. The source code and pretrained model are available at https://github.com/FanChiMao/HWMNet.

**中文翻译**：低光图像增强是一项将暗图像增强到合适亮度的计算机视觉任务，也可视为图像恢复领域的一个病态（ill-posed）问题。随着深度神经网络的成功，卷积神经网络已超越传统的基于算法的方法，成为计算机视觉领域的主流。为提升增强算法的性能，本文基于一个改进的层次化模型 M-Net+ 提出图像增强网络 HWMNet。具体而言，我们在 M-Net+ 上使用半小波注意力模块（half wavelet attention block）来丰富小波域中的特征。在两个图像增强数据集上，HWMNet 在定量指标和视觉质量上均取得了有竞争力的结果。源码与预训练模型已开源。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：图像增强是一项低级（low-level）视觉任务，也是图像分类、目标检测等高级视觉任务的重要前处理步骤。论文把低光增强归入图像恢复框架，用退化模型 `Y = D(X) + n` 描述（X 为高质量/无噪图像，D 为退化函数，n 为加性噪声）。增强方法分两类：基于算法（algorithm-based，又称基于先验/模型）与基于学习（learning-based）。前者又可归为三类主流：直方图均衡化、Retinex、去雾。
- **之前方法的问题**：传统基于先验的方法效果可接受，但常有颜色失真或过度增强问题。近年基于 CNN 的学习方法在推理速度与增强效果上均已超越传统方法。作者进一步分析了医学/指纹任务中常用的层次化网络 **M-Net**，认为它没有成为图像恢复主流骨干有两个原因：1）编码器在 gatepost 和 U-Net 两条路径上都用 **max-pooling 下采样**，而恢复是像素级任务，下采样会造成严重的空间信息丢失；2）解码器因额外增加了 gatepost 特征路径，重建时需要融合的特征过多，加重了网络负担、参数量与计算复杂度。
- **核心矛盾**：如何既利用层次化结构（如 M-Net 的 gatepost 多尺度路径）获取多分辨率上下文信息，又减小下采样带来的空间信息损失、并高效融合多尺度特征，从而在低复杂度下实现高质量低光增强。

## 关键贡献

1.  提出改进的层次化架构 **M-Net+**，作为低光图像增强的网络骨干，能提供更多样、更丰富的多尺度级联（cascading）特征。
2.  提出高效的特征提取模块 **半小波注意力模块（HWAB）**，能在另一个域（小波域）获取更多样化的特征，同时仅对一半特征施加注意力以降低计算复杂度。
3.  在两个低光增强数据集（LOL、MIT-Adobe FiveK）上实验，证明 HWMNet 在定量与视觉质量上达到 state-of-the-art，且计算复杂度更低。

## 方法

- **整体框架（HWMNet）**：端到端图像增强模型，骨干为改进的 M-Net+（图 1），是类 U-Net 的层次化结构，共 **4 层**。每个分辨率上先用 3×3 **权值共享卷积**处理由原图双线性下采样得到的多分辨率低光输入；每层都嵌入一个 HWAB 提取充分且丰富的语义信息。各分辨率初始通道数设为 96（经 3×3 卷积后）。
- **输入输出**：输入低光图像（及其双线性下采样得到的多分辨率版本），输出增强后的正常亮度图像。
- **关键模块**：
    1.  **HWAB（半小波注意力模块，图 2）**：改造自双注意力单元 **DAU**（来自 MIRNet [1] 与 CycleISP [15]，DAU 同时用通道注意力 [SE, 16] 与空间注意力并融合）。流程：输入特征 `f_in ∈ R^{C×H×W}` 沿通道分两半 `f_identity` 与 `f_t`（各 `∈ R^{(C/2)×H×W}`）。`f_identity` 保留原域特征（思想参考 HINet [17] 的半实例归一化）；`f_t` 做离散小波变换（DWT）得小波域特征 `f_w ∈ R^{2C×(H/2)×(W/2)}`（通道变 4 倍后这里写为 2C 配合分半，空间各减半）。`f_w` 经 DAU 加权得 `\hat{f}_w`，再经逆小波变换（IWT）还原为 `\hat{f}_t ∈ R^{(C/2)×H×W}`。将 `\hat{f}_t` 与 `f_identity` 拼接，经 3×3 卷积与 PReLU 得残差特征 `f_r`；最后把经 1×1 卷积的 shortcut 加到 `f_r`，输出 `f_out ∈ R^{C×H×W}`，携带小波注意力信息。**分半的目的是降低计算复杂度并保留上下文信息。**
    2.  **M-Net+（针对原 M-Net 两大问题改进）**：① 更多样丰富的多尺度级联特征——在 U-Net 路径用 **pixel unshuffle 下采样**（[14]，置于每层 HWAB 末端的 trunk 路径），在 gatepost 路径用 **双线性下采样**，两条路径不同的下采样方式使级联特征更具多样性，gatepost 路径本身也缓解空间信息丢失；② 解码器改用 **选择性核特征融合（SKFF [1]）** 替代简单 concatenation 来汇总信息，解决原 M-Net 高维级联特征导致的参数多、复杂度高问题。
- **损失函数**：Charbonnier 损失（L1 的变体），`L_char = sqrt(||\hat{X} - X||² + ε²)`（公式 2），其中 `\hat{X}, X ∈ R^{N×C×H×W}` 为低光图像与真值，ε 经验设为 `10^-3`。
- **训练方式**：PyTorch 1.8.0，单卡 NVIDIA GTX 1080Ti，从头训练；在 256×256 patch 上训练，batch size = 2，迭代 `1×10^5` 次；数据增强为随机水平/垂直翻转；Adam 优化器，初始学习率 `1×10^-4`，余弦退火衰减至 `1×10^-6`。
- **推理流程**：低光图像输入 → M-Net+ 骨干（内含多个 HWAB）处理 → 直接输出增强图像。
- **和已有方法的差异**：相较 DAU 直接在空域/通道域操作，HWAB 把注意力搬到小波（频）域加权；相较原 M-Net，M-Net+ 用差异化下采样 + SKFF 融合在保多尺度优势的同时提升效率与效果。
- **论文类型特化（注意力类）**：HWAB 是可插拔模块，嵌入 M-Net+ 每一层；其注意力经 DAU 作用于 **通道域 + 空间域**，并通过 DWT/IWT 在 **小波域** 进行加权。"半分"策略（只对一半特征做小波变换+注意力，另一半走 identity）在引入频域表达增益的同时控制计算量。

## 实验

- **使用的数据集**：
    1.  **LOL** [24]：485 对训练 / 15 对测试，图像尺寸 600×400，每对含一张低光图与对应正常亮度真值。训练时每图随机裁出 10 个 256×256 patch；验证用每张测试图的中心裁剪 256×256 patch。
    2.  **MIT-Adobe FiveK** [26]：5000 张室内外图像（单反相机不同光照），以专家 C（A~E 之一）的调整结果为真值，前 4500 训练 / 后 500 测试。两数据集分别训练独立模型。
- **对比方法**：传统方法 MSR [4]，及学习方法 Zero-DCE、LIME、Retinex-Net、EnlightenGAN、RUAS、GLAD、DRBN、KinD、KinD++、MIRNet、LLFlow（LOL 表）；HDRNet、W-Box、DR、DPE、DeepUPE、MIRNet（FiveK 表）。
- **评价指标**：PSNR（越高越好）、SSIM（越高越好）、LPIPS [18]（越低越接近人眼感知）。
- **主实验结果**：
    - **LOL（表 1）**：HWMNet 取得 PSNR **24.24** dB / SSIM **0.85** / LPIPS **0.12**。论文明确表述为"对所有指标均取得 runner-up（第二名）"——即三项都是次优：PSNR 仅次于 LLFlow（25.19）、亦高于 MIRNet（24.14）；SSIM 仅次于 LLFlow（0.93）；LPIPS（0.12）仅次于 LLFlow（0.11）、优于 MIRNet（0.13）。作者据此称增强结果"在感知上更保真"。（注：原笔记曾误称 LPIPS 排第一，已据表 1 与正文订正为第二。）
    - **MIT-Adobe FiveK（表 2）**：HWMNet 取得 **最佳 PSNR 24.44** dB（次于它的 MIRNet 23.73、DeepUPE 23.04），SSIM **0.914**（次于 MIRNet 0.925，为第二）。论文称在 PSNR 与 SSIM 上达到 state-of-the-art。
- **效率信息（关键卖点）**：在 400×592 彩色图上测得 FLOPs——MIRNet **2.84T**、LLFlow **1.05T**、HWMNet **0.92T**（T=10^12），HWMNet 是三个顶级模型中复杂度最低的。作者归因于 HWAB 的"半特征过注意力"设计（参 HINet [17]）以及小波注意力带来的语义/细节增益。
- **消融实验**：PDF 文本未给出针对 HWAB 或 M-Net+ 各组件（DWT/IWT、DAU、分半、下采样策略、SKFF）的独立消融结果。
- **泛化实验**：两数据集各训独立模型，未做跨数据集泛化测试。

## 局限

1.  **任务单一**：仅在低光增强上验证；去噪、去模糊等其他恢复任务仅列为未来工作（结论提及）。
2.  **数据集有限**：仅 LOL、MIT-FiveK 两个数据集评估，难以覆盖各类复杂低光场景。
3.  **缺消融**：未定量分析 M-Net+ 各改进点（差异化下采样、SKFF）与 HWAB 各组件（DWT/IWT、DAU、分半）各自贡献。
4.  **复现依赖代码**：SKFF、DAU 等具体结构/配置需参照 GitHub 源码，纯读论文复现不够友好。
5.  **绝对精度仍有差距**：在 LOL 上 PSNR/SSIM 均不及 LLFlow，方法卖点是"性能接近 SOTA + 复杂度更低"，而非单纯刷新精度。

## 个人评论

这篇论文最值得学习的是 **HWAB 的工程权衡设计**。它不是简单地在空间或通道上叠注意力，而是沿通道把特征一分为二：一半走 identity 保住基础信息流（借鉴 HINet 的半实例归一化思路），另一半经 DWT 进小波域做注意力加权再 IWT 还原，最后拼接融合。这种"半分（Half）"策略很巧妙——只对一半特征做较贵的小波变换 + 注意力，在引入频域特征表达增益的同时把额外算力压住，最终在 LOL 上 FLOPs 仅 0.92T（约 MIRNet 的 1/3）却拿到接近 SOTA 的精度。对后续研究的启发：可在不同变换域（小波/傅里叶/其他）设计轻量注意力，并用"分路 + 残差"结构平衡效果与效率。需要客观看待的是，论文缺乏消融，"分半"和"小波域"各自贡献多少其实没被定量拆开；且在 LOL 上 LLFlow 仍全面占优，所以本文真正的价值在"性价比"而非绝对精度。

### 使用建议

- **如果快速了解**：读摘要、引言贡献列表、图 1（整体架构）、图 2（HWAB 结构）与第 4.3 节（表 1/表 2 + FLOPs 对比）。
- **如果复现**：重点读第 3 节（3.1 整体、3.2 M-Net+、3.3 HWAB）及图表；第 4.1 节给了完整训练超参（256×256 patch、bs=2、1e5 iter、Adam 1e-4→1e-6 余弦退火）。务必结合 GitHub 源码核对 SKFF/DAU 细节。
- **如果借鉴创新点**：深入 HWAB（3.3），抓"分路—频域注意力—再融合—残差"主线；同时关注 M-Net+（3.2）用差异化下采样 + SKFF 替代 concat 的融合改进。
- **如果写 Related Work**：可归入"基于深度学习的低光增强""小波变换在图像恢复中的应用""注意力机制 + 频域"三类，作为结合小波变换与注意力的轻量化代表。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属计算机视觉 **低光图像增强（Low-Light Image Enhancement）** 方向，将其纳入图像恢复（image restoration）框架处理（退化模型 `Y = D(X) + n`）。核心是用改进的层次化网络 M-Net+ 搭配一个结合小波变换的注意力模块 HWAB 来增强暗图像。由于论文的任务本体是图像恢复/增强（而非单纯提出一个通用算子），更贴切的主题是"E_图像复原_超分_去噪_去雨去雾"；其方法层面的亮点（HWAB）才落在注意力模块范畴。（原笔记归入"B_注意力算子模块"，已据论文任务订正为 E。）

## 2. 一句话总结
HWMNet 用改进的层次化骨干 M-Net+（pixel-unshuffle + 双线性双路下采样、SKFF 融合）配合半小波注意力模块 HWAB（半特征走 DWT→DAU→IWT 的频域注意力），在 LOL 与 MIT-FiveK 低光增强上达到接近 SOTA 的精度，同时把 FLOPs 压到三大顶级模型中最低（0.92T）。

## 3. 背景与问题
- **为什么要做**：低光增强是低级视觉任务，也是分类/检测等高级任务的前处理；可视为 `Y=D(X)+n` 的病态恢复问题。传统基于先验的方法（直方图均衡、Retinex、去雾）效果可接受但常有颜色失真/过增强；CNN 学习方法已在速度与效果上超越传统方法。
- **之前方法的问题**：医学/指纹领域常用的层次化网络 M-Net 不适合做恢复骨干，原因有二——① 编码器两路（gatepost + U-Net）都用 max-pooling 下采样，对像素级恢复任务造成严重空间信息丢失；② 解码器因额外 gatepost 路径，重建时待融合特征过多，参数量与计算复杂度高。
- **核心矛盾**：既要保留层次化结构的多尺度上下文优势，又要减小下采样损失、降低融合负担，实现"高质量 + 低复杂度"的增强。

## 4. 核心贡献
1.  改进层次化架构 **M-Net+**，提供更多样丰富的多尺度级联特征。
2.  高效特征提取模块 **HWAB**，在另一域（小波域）获取更多样化特征，且仅对一半特征做注意力以省算力。
3.  在 LOL 与 MIT-Adobe FiveK 上验证，在更低计算复杂度下取得（接近）SOTA 的定量与视觉质量。

## 5. 方法详解
- **整体框架**：端到端，骨干 M-Net+（图 1），类 U-Net 层次化共 4 层，每分辨率初始通道 96；多分辨率低光输入由原图双线性下采样得到，先过 3×3 权值共享卷积，每层嵌 HWAB。
- **HWAB（图 2，改自 DAU [1,15]）**：`f_in ∈ R^{C×H×W}` 沿通道分 `f_identity` 与 `f_t`（各 `∈ R^{(C/2)×H×W}`）。`f_identity` 保留原域特征（参 HINet [17]）；`f_t` 做 DWT 得 `f_w ∈ R^{2C×(H/2)×(W/2)}`，经 DAU（通道注意力 SE [16] + 空间注意力）加权得 `\hat{f}_w`，再 IWT 还原为 `\hat{f}_t ∈ R^{(C/2)×H×W}`；拼接 `\hat{f}_t` 与 `f_identity` → 3×3 卷积 + PReLU 得残差 `f_r`；加上 1×1 卷积的 shortcut，输出 `f_out ∈ R^{C×H×W}`。分半的目的：降复杂度 + 保上下文。
- **M-Net+ 两项改进**：① U-Net 路径用 pixel unshuffle 下采样 [14]、gatepost 路径用双线性下采样，差异化使级联特征更多样、gatepost 缓解空间损失；② 解码器用 SKFF [1] 替代 concatenation 融合，解决原 M-Net 高维级联导致的参数多/复杂度高。
- **损失**：Charbonnier `L_char = sqrt(||\hat{X}-X||² + ε²)`，ε=`10^-3`。
- **训练**：PyTorch 1.8.0 / 单卡 GTX 1080Ti；256×256 patch，bs=2，1×10^5 iter；随机水平/垂直翻转；Adam，lr 1e-4→1e-6 余弦退火。

## 6. 实验与结果
- **数据集**：LOL [24]（485/15，600×400，训练每图裁 10 个 256² patch，验证中心裁 256²）；MIT-Adobe FiveK [26]（5000 张，专家 C 为真值，4500/500）；两集分别训独立模型。
- **指标**：PSNR↑、SSIM↑、LPIPS↓ [18]。
- **LOL（表 1）**：HWMNet **24.24 / 0.85 / 0.12**，论文称三项指标均为 runner-up（第二名）——PSNR 次于 LLFlow 25.19（>MIRNet 24.14）；SSIM 次于 LLFlow 0.93；LPIPS 0.12 次于 LLFlow 0.11（<MIRNet 0.13）。**订正：原笔记称 LPIPS 第一有误，实为第二。**
- **MIT-FiveK（表 2）**：HWMNet PSNR **24.44（最佳）**、SSIM **0.914（次于 MIRNet 0.925）**；称 PSNR/SSIM 达 SOTA。
- **效率**：400×592 彩图上 FLOPs，MIRNet 2.84T / LLFlow 1.05T / HWMNet **0.92T**，三者中最低；归因于 HWAB 半特征过注意力 [17] + 小波注意力的语义增益。
- **消融/泛化**：PDF 文本未给独立消融；无跨数据集泛化测试。

## 7. 这篇论文真正有价值的地方
价值在 **HWAB 的"半分 + 频域"工程权衡**：一半特征走 identity 保信息流，另一半进小波域做注意力再融合，用 1/3 于 MIRNet 的 FLOPs（0.92T）拿到接近 SOTA 的精度。它示范了"换个变换域 + 分路轻量化"是注意力设计中兼顾效果与效率的可行路线。需保留批判：缺消融，"分半"与"小波域"各自的增益未被拆开量化。

## 8. 局限与问题
1.  仅验证低光增强一种任务，去噪/去模糊仅列未来工作。
2.  仅两数据集（LOL、MIT-FiveK），覆盖场景有限。
3.  无消融，各改进点贡献不明。
4.  SKFF/DAU 细节需查源码，纯论文复现不友好。
5.  LOL 上 PSNR/SSIM 仍不及 LLFlow，卖点是性价比而非绝对精度。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言贡献 + 图 1 + 图 2 + 4.3 节表格/FLOPs。
- **复现**：第 3 节（3.1/3.2/3.3）+ 图表；4.1 节超参；结合 GitHub 源码核对 SKFF/DAU。
- **借鉴创新**：吃透 HWAB（3.3）的"分路—频域注意力—再融合—残差"，并看 M-Net+（3.2）的 SKFF 融合改进。
- **写 Related Work**：归入"深度学习低光增强 / 小波变换在恢复中的应用 / 频域注意力"。

## 10. 和其他论文的关系
- **MIRNet** [1]（ECCV 2020，"Learning enriched features…"）：本文最重要的基线与思想来源，HWAB 直接改自其 DAU、SKFF 也来自它；HWMNet 精度接近 MIRNet 但 FLOPs 仅约 1/3。
- **CycleISP** [15]（CVPR 2020）：DAU 的另一来源。
- **HINet** [17]（CVPR 2021，半实例归一化）：HWAB 保留一半原域特征的"分半"设计受其启发。
- **SE-Net** [16]（CVPR 2018）：DAU 中通道注意力的来源。
- **RDN** [14]：pixel unshuffle 下采样的出处。
- **LLFlow** [10]、**KinD++** [8]、**KinD** [7]、**DRBN** [23] 等：主要对比对象；LLFlow 在 LOL 上 PSNR/SSIM/LPIPS 全面占优。

## 11. 关键词
低光图像增强, 图像恢复, 半小波注意力 HWAB, 小波变换 DWT/IWT, 双注意力单元 DAU, M-Net+, SKFF, pixel unshuffle, Charbonnier 损失, LOL, MIT-Adobe FiveK, FLOPs, 注意力机制

## 12. 可信度说明
本精读基于完整 6/6 页的高质量 PDF 提取（提取缓存覆盖全文，含摘要、引言、相关工作、方法第 3 节、实验第 4 节、结论与参考文献）。关键数字（LOL 24.24/0.85/0.12、FiveK 24.44/0.914、FLOPs 0.92T/1.05T/2.84T、ε=1e-3、bs=2、1e5 iter、4 层、初始通道 96）与模块描述均直接取自提取文本对应表格/正文。对原笔记一处明显错误（LOL 的 LPIPS 名次）依表 1 与正文"runner-up for all metrics"订正为第二。文中未提供的消融实验已明确标注"PDF 文本未给出"。提取质量好，覆盖完整，本笔记可信度高。

---

> **可信度补充**: PDF 提取质量 = **high** (6/6 页完整, 提取覆盖全文含表 1/表 2 数值); 来源缓存: `.paper-cache/extracts/HWAB.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮重读已据提取文本校正标题/作者/摘要、LOL LPIPS 名次, 并将 primary_topic 由 B 改为 E。
<!-- AI_READING_NOTE_END -->
