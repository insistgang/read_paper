---
title: 结合密集连接的轻量级高分辨率人体姿态估计
authors:
  - "高坤"
  - "李汪根"
  - "束阳"
  - "葛英奎"
  - "王志格"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.230228
pdf: [[cjig_图像识别_融合密度和精细分数的行人检测.pdf]]
primary_topic: K_跟踪_视频_动作
topics:
  - "K_跟踪_视频_动作"
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
extract_cache: .paper-cache/extracts/cjig_图像识别_融合密度和精细分数的行人检测.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/13 pages"
---
# 结合密集连接的轻量级高分辨率人体姿态估计

## 基本信息
- **PDF**: [[cjig_图像识别_融合密度和精细分数的行人检测.pdf]]
- **primary_topic**: `K_跟踪_视频_动作`
- **topics**: `K_跟踪_视频_动作`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

> **题目/分类说明**: 本笔记文件名（stem）"图像识别_融合密度和精细分数的行人检测"与论文真实内容不符——这是 PDF 自动提取产生的乱码/张冠李戴文件名。论文真实标题为《结合密集连接的轻量级高分辨率人体姿态估计》（Lightweight high-resolution human pose estimation combined with densely connected network, LDHNet），主题是**2D 人体姿态估计的轻量化网络设计**，并非行人检测。据此已将 primary_topic 由 `C2_目标检测_违建_车辆_船舶_行人` 改为更贴切的 `K_跟踪_视频_动作`（人体关键点 / 动作相关 CV 任务；现有 taxonomy 无独立的"姿态估计"主题）。

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 结合密集连接的轻量级高分辨率人体姿态估计 |
| **英文题目** | Lightweight high-resolution human pose estimation combined with densely connected network |
| **作者** | 高坤; 李汪根*(通信作者); 束阳; 葛英奎; 王志格（安徽师范大学计算机与信息学院） |
| **发表时间** | 2024（收稿 2023-05-31，修回 2023-07-31） |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics)，29(05): 1408-1420 |
| **DOI** | 10.11834/jig.230228 |
| **基金** | 国家自然科学基金 (61976006) |

## 摘要

清理后的英文原摘要（修复了空格、连字符断裂，剔除杂入的版式数字）：

> **Objective**: Human pose estimation is a technology that can be widely used in life. In recent years, many excellent high-precision methods have been proposed, but they are often accompanied by a very large model scale, which encounters the problem of a computing power bottleneck in application. Whether for model training or deployment, large models require considerable computing power as the basis. For scenes in daily life, the equipment needs further applicability and detection speed of the model, which is difficult to achieve with large models. Given such requirements, lightweight human pose estimation has become a hot research field. The main problem is how to achieve high detection accuracy and fast detection speed under an extremely limited number of resources. **Method**: Based on a high-resolution network (HRNet), a lightweight high-resolution human pose estimation network combined with a dense connection network (LDHNet) is proposed. Dense connection and multi-scale feature extraction are integrated to construct a lightweight and efficient feature extraction unit by redesigning the stage branch structure in HRNet; dilated convolutions of three scales obtain a wide range of feature information, and concatenating the output feature maps reuses features. The cross-branch feature fusion is replaced by depthwise separable convolution, the data preprocessing (stem) module uses a double-branch form to better preserve original image information, and coordinate attention is used to reinforce spatial location information. **Result**: The model size is greatly reduced to less than one-tenth of the original HRNet. On the MPII test set, LDHNet improves the average prediction accuracy by 1.5% over LiteHRNet and by 0.9% over DiteHRNet; on the COCO validation set, the average detection accuracy improves by 3.4% over LiteHRNet and 2.3% over DiteHRNet; it reaches detection performance similar to the Transformer-based HRFormer at smaller scale. In the actual scene, LDHNet has stable performance, and its inference speed is higher than the baseline HRNet and LiteHRNet. **Conclusion**: LDHNet effectively achieves the lightweight design goal while maintaining detection performance; a remaining problem is that the speed-up does not match the degree of lightweighting.

中文翻译：

> **目的**：为了更好地实现轻量化的人体姿态估计，在轻量级模型极为有限的资源下实现更高的检测性能。**方法**：基于高分辨率网络 HRNet，提出结合密集连接网络的轻量级高分辨率人体姿态估计网络 LDHNet——重新设计 HRNet 的阶段分支结构、提出新的轻量级特征提取模块（融合密集连接与多尺度膨胀卷积）构建高效特征提取单元，对多分支间的特征融合做轻量化改进（深度可分离卷积），用双分支 Stem 模块更充分保留原始图像信息，并用坐标注意力强化空间位置信息，从而大幅降低参数量与计算量。**结果**：模型规模降至原 HRNet 的不足 1/10；在 MPII 测试集上较 LiteHRNet 平均预测准确度提升 1.5%、较 DiteHRNet 提升 0.9%；在 COCO 验证集上较 LiteHRNet 提升 3.4%、较 DiteHRNet 提升 2.3%；在更小规模下与融合 Transformer 的 HRFormer 检测性能相近；实际场景表现稳定，同环境下推理速度高于 HRNet 与 LiteHRNet。**结论**：LDHNet 有效实现了轻量化并保证了预测性能；不足是推理速度的提升未达到与轻量化程度相匹配的水平。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：2D 人体姿态估计是计算机视觉的重要方向，目标是从场景中提取人体关节点坐标，广泛用于动作识别、人机交互、虚拟现实等。随着精度提升，模型规模（动辄上千万参数）不断膨胀，无论训练还是部署都成本高昂，与现实中常见的低算力设备（移动端、嵌入式）"高适用性 + 轻量快速"的需求相悖，因此轻量化人体姿态估计成为重要研究方向。
- **方法路线选择**：姿态估计分自顶向下（top-down，先检测单个人体目标再对该区域做姿态估计）与自底向上（bottom-up，先检测所有关节点再组装）两类；得益于把多人估计转化为单人估计，自顶向下方法性能更好、鲁棒性更强，本文采用自顶向下路线。
- **之前方法的问题**：
    - 高精度模型（HRNet、ViTPose 等）性能优异，但模型规模大、计算开销高；ViTPose 用单分支 Vision Transformer 即远超 HRNet，但同样不轻量。
    - 既有轻量级模型——LPN（简化 SBL + 深度可分离卷积）、Lite-HRNet（在 HRNet 上大幅压缩参数/计算量）、HRFormer（轻量化高分辨率 Transformer）——虽显著压缩了模型，但轻量级模型在特征信息利用上往往不充分，精度仍存在损失。
- **核心矛盾**：如何在极其有限的模型资源（参数量、计算量）下尽可能提升检测精度，实现轻量化与高性能之间更好的平衡。

## 关键贡献

1.  **提出 LDHNet 架构**：以 HRNet 为基线，系统性重新设计各阶段结构，融入密集连接与多尺度特征提取，充分利用网络各阶段的特征图、避免信息浪费，同时简化占资源较大的特征融合部分，模型规模降至原 HRNet 不足 1/10。
2.  **轻量级多尺度特征提取模块 GMConv**：在 GSConv（通道压缩 + 深度卷积 + ECA 注意力）基础上结合 ESPNet 思想，先把通道压缩至 1/4，再用膨胀率 1/3/5 的 3 组膨胀卷积级联相加获取多尺度信息，最后拼接 + 通道洗牌恰好还原原通道数，无需额外 1×1 卷积。
3.  **密集连接模块 GWblock**：借鉴 DenseNet→VoVNet 思路，仅保留所有中间层到最后一层的密集连接，在复用特征、加强梯度反传的同时几乎不增加复杂度。
4.  **轻量化特征融合**：将 HRNet 跨分支（高→低分辨率）传递信息时的普通 3×3 卷积替换为 3×3 深度可分离卷积，并加入坐标注意力（Coordinate Attention, Hou 等 2021）强化空间位置信息。
5.  **双分支 Stem 模块**：受 PeleeNet 启发，把 HRNet Stem 中第 2 个 3×3 卷积替换为"卷积 + 池化"双分支下采样、拼接后用 1×1 卷积还原，在不增加参数量/计算量的前提下保留更多原始图像信息。
6.  **多数据集验证**：在 MPII、COCO val、COCO test-dev 上验证，并在 CPU 环境下做推理速度对比。

## 方法

- **整体框架**：LDHNet 延续 HRNet 多分支并行结构，预处理后共 4 个阶段。第 1 阶段仅 1 个最高分辨率分支；后续 3 个阶段在每阶段初始由当前阶段内最低分辨率分支下采样生成一个新分支，并在多分支阶段内反复进行跨分支特征交互；第 4 阶段结束后仅输出最高分辨率分支特征图用于预测关键点（图1，表1）。新分支特征图尺寸为最小分辨率分支的 1/4，通道数翻倍。各阶段配置（表1）：
    - 阶段1：GMCneck，堆叠 1，分支 1，通道 64，多尺度输出；
    - 阶段2：GWblock+Fuse，堆叠 1，分支 2，通道 32/64，多尺度输出；
    - 阶段3：GWblock+Fuse，堆叠 4，分支 3，通道 32/64/128，多尺度输出；
    - 阶段4：GWblock+Fuse，堆叠 3，分支 4，通道 32/64/128/256，无多尺度输出。
- **输入输出**：输入为以人体髋部为中心裁剪的人体图像（COCO 裁 256×192 或 384×288，MPII 裁 256×256）并经数据增强；输出为人体关键点坐标。
- **关键模块**：
    1.  **Stem 模块**（图2）：把原 HRNet Stem 的第 2 个 3×3 卷积换成卷积/池化双分支下采样，输出在通道维拼接后用 1×1 卷积还原尺寸；不增加参数量/计算量却提升了检测性能。
    2.  **GSConv 模块**（图3）：先把通道压缩为原本 1/2，再用深度卷积（Sandler 等 2018）+ ECA 注意力（Wang 等 2020）提取特征，最后拼接还原尺寸。3 组 GSConv 串联构成 GMCneck（用于第 1 阶段）。
    3.  **GMConv 模块**（图4，公式1-3）：核心特征提取单元。① 用 GSConv 方式把通道压缩至 1/4（XT=φ(X)，公式1）；② 用 3 组膨胀率分别为 1/3/5 的膨胀卷积，把较小膨胀率的输出与下一组输出级联相加（XT(i)=Di(XT)+XT(i-1)，i=1,2,3，公式2）；③ 把压缩特征图与 3 个膨胀输出共 4 组在通道维拼接并做通道洗牌（公式3），因压缩 4 倍拼接后恰好还原原通道数，无需 1×1 卷积。
    4.  **GWblock 模块**（图5，公式4-6）：由 2 组 GMConv 作为密集单元加最后拼接后的 1×1 卷积构成。第 1 个 GMConv 同时负责把输入通道数变换到输出通道数（Y1=φ(xin)），后续 GMConv 不再改通道（Yi=φ(Yi-1)）；最后把 xin 与所有中间输出拼接后过 1×1 卷积还原到与 xin 相同通道（xout=φ(Concat[x,Y1,Y2,Y3])，公式6）。仅保留中间层到最后一层的密集连接，故相比直接串联 GMConv，新增连接带来的参数量/计算量增加有限。
    5.  **特征融合**（图6）：HRNet 跨分支交互中，高→低分辨率用步长 2 的 3×3 卷积下采样、低→高用系数 2 邻近上采样、同分辨率直接映射，跨度>1 则多次上/下采样后相加。本文把高→低的普通 3×3 卷积换为 3×3 深度可分离卷积并加入坐标注意力机制，强化空间位置信息、大幅削减模型规模。
- **训练设置**：实验平台 Ubuntu 20.04 LTS，CPU i5-10400F，GPU RTX 3060（12 GB），PyTorch 1.10.1 / Python 3.9。Adam 优化器，训练 210 轮（与 HRNet 一致），初始学习率 0.001，在第 170、200 轮各衰减 10 倍。数据增强与 HRNet/LiteHRNet/DiteHRNet 一致：±45° 旋转、±35% 缩放。
- **和已有方法的差异**：
    - 相比 HRNet：参数量不足 1/10、计算量约 1/5（MPII 输入 256×256 下），用 GMConv/GWblock 在轻量化前提下尽量保持精度。
    - 相比 LiteHRNet/DiteHRNet：在相近轻量级规模下，通过密集连接 + 多尺度膨胀卷积获得显著精度提升。
    - 相比 HRFormer：在参数量、计算量都更低时取得接近性能，说明 CNN 轻量化路线仍具竞争力。

## 实验

- **数据集**：
    - **COCO 2017**（Lin 等 2014）：约 330K 幅图像、超 200K 幅带标注；人体姿态估计用含关键点标注的图像，约 250K 个人体目标（训练约 57K 幅、验证约 5K 幅、测试 20K 幅）。指标基于 OKS（公式7）：AP（OKS=0.5…0.95 共 10 个位置的均值）、AP50、AP75、APM、APL、AR。
    - **MPII**（Andriluka 等 2014）：约 25K 幅图像、超 40K 个人体目标，每个目标标注 **16 个关键点**；评估指标 PCKh@0.5，评估的关键点为头部、肩膀、手肘、腕部、髋部、膝盖、脚踝共 **7 类**（注：是 7 类评估部位，而非仅标注 7 个关键点）。
- **对比方法**：大型网络 SHN、CPN、SBL-50/152、HRNet、HigherHRNet、HRFormer-S；轻量级网络 LPN-50/101、MobileNetV2、ShuffleNetV2、Small HRNet、LiteHRNet、DiteHRNet、HRFormer-T（表2/3/4）。
- **主实验结果**：
    - **COCO 验证集**（256×192，表2）：LDHNet 参数量 2.2M、GFlops 1.4、AP=**70.6%**。较 LiteHRNet（67.2%）提升 3.4%（正文 2.3 节叙述为 3.5%，摘要口径为 3.4%，差异源于不同取整），较 DiteHRNet（68.3%）提升 2.3%（正文叙述 2.4%）。AP50=**90.5%** 为全表（含 HRNet 89.5%）最高；较 LPN-101（70.4%）提升 0.2%；较基线 HRNet（73.4%）AP 略降，但 AP50 反而更高。
    - **COCO test-dev**（384×288，表3）：LDHNet 参数量 2.2M、GFlops **3.3**、AP=**70.5%**，较 LiteHRNet（69.7%）提升 0.8%；AP50=90.6%、AR=76.6%。
    - **MPII 验证集**（256×256，PCKh@0.5，表4）：LDHNet 参数量 **2.5M**、GFlops **1.8**、Mean=**88.5%**。较 LiteHRNet（87.0%）提升 1.5%，较 DiteHRNet（87.6%）提升 0.9%，较 LPN-50（86.6%）提升 2.5%；较 HRNet（90.3%）用不足 1/10 参数与约 1/5 计算量达到相近水准。各部位：头 96.8 / 肩 95.3 / 肘 88.8 / 腕 83.4 / 髋 88.3 / 膝 83.7 / 踝 79.5。
- **效率信息**：参数量随输入/数据集不同——COCO 256×192 为 2.2M/1.4 GFlops；COCO test-dev 384×288 为 2.2M/3.3 GFlops；MPII 256×256 为 2.5M/1.8 GFlops。HRNet 对应约 28.5M / 7.1~16.0 GFlops。
- **消融实验**（均在 MPII，表5-8）：
    - **Stem 模块**（表5）：参数量/计算量不变（2.5M/1.8），Mean 由 87.7% 升至 88.5%。
    - **主要模块**（表6）：GMCneck 与 GWConv 对照原 HRNet 残差模块。GMCneck 对轻量化贡献不大但对精度提升重要；GWConv 把参数量降低一个数量级（去掉 GWConv 时升到 14.7M/5.5 GFlops），是轻量化的关键。两者同时使用为 2.5M/1.8/88.5%。
    - **多尺度特征提取**（表7）：用 GMConv 的多尺度膨胀卷积相比普通 3×3 逐通道卷积，Mean 由 87.7% 升至 88.5%（参数量/计算量同为 2.5M/1.8）。
    - **密集连接**（表8）：用 GWblock 密集连接（2.5M/1.8）相比直接串行（1.2M/1.7），参数量增加但 Mean 由 82.9% 大幅升至 88.5%。
- **推理速度（图7）**：仅在 **CPU（i5-10400F）** 环境下测试（强调资源受限场景），取一段时间内帧率范围；LDHNet 推理速度高于基线 HRNet，相比 LiteHRNet 也有较大优势；圆形大小表示模型规模。相比 MobileNetV2/ShuffleNetV2 的"高速低精度"，LDHNet 在速度与精度间更平衡。
- **可视化（图8）**：在低光照、模糊、部分遮挡及多人复杂场景下，LDHNet 仍能保持良好稳定性能。

## 局限

1.  **推理速度提升未达预期**：作者在结论中自述，模型推理速度的提升没有达到与其轻量化程度（参数量大幅减少）相匹配的水平，可能受复杂模块连接与密集计算影响实际运行效率；后续工作拟分离训练与推理、融合重参数化思想进一步提速。
2.  **速度测试条件单一**：推理速度仅在 CPU（i5-10400F）下测试（结论段亦提及 GPU 加速下相比 HRNet 提升明显，但正文 2.5 节明确测试环境仅用 CPU），缺乏不同硬件、不同 batch、嵌入式真机的系统评测。
3.  **依赖自顶向下框架**：本文属自顶向下姿态估计，性能依赖前端人体检测器，检测器漏检/误检会直接拖累姿态估计；文中未讨论与检测器的联合优化或对检测误差的鲁棒性。
4.  **数据集局限**：仅在 MPII 与 COCO 上验证；未针对极度拥挤、严重遮挡、非标准姿态等极端场景做专门的定量分析。
5.  **复现细节**：坐标注意力的精确集成位置、通道洗牌的具体实现、图1/图7 的精确数值等需查阅原图或代码方可完全复现（提取文本含表格但图细节有限）。

## 个人评论

1.  **清晰的"基线→模块替换"轻量化范式**：论文从强基线 HRNet 出发，按可解释的步骤逐块替换（普通卷积→深度可分离卷积、残差块→GMConv/GWblock、单 Stem→双分支 Stem），并配套消融逐项验证每个改动的收益，逻辑链完整、可复现性较好，比单纯堆砌轻量组件更有说服力。
2.  **GMConv 的"压缩—多尺度—拼接还原"设计**：先压 1/4 再用膨胀率 1/3/5 的膨胀卷积级联相加，最后拼接恰好还原通道、省掉收尾 1×1 卷积，是一个在算量受限下扩大感受野的紧凑技巧，值得迁移到其他轻量骨干。
3.  **GWblock 对密集连接的轻量化裁剪**：只保留中间层到最后一层的连接（VoVNet 式），表8 显示它把 Mean 从 82.9% 拉到 88.5%（代价是 1.2M→2.5M），印证了"特征复用"在轻量级网络中是高性价比的性能来源。
4.  **诚实的不足陈述**：作者明确指出"参数量大降但速度提升不成比例"，这正是轻量化研究中 FLOPs/参数量与实际延迟脱节的经典问题——对读者比单纯报喜更有价值。
5.  **需要注意的取整不一致**：摘要与正文对同一对比（如 vs LiteHRNet/DiteHRNet 在 COCO val 上的提升）给出 3.4%/3.5%、2.3%/2.4% 两套数字，引用时应以表2 原始值（70.6 vs 67.2/68.3）自行核算。

### 使用建议

- **快速了解**：读摘要、引言（问题与三类背景工作）、1.1 节 LDHNet 概述（图1、表1）、2.3 节主结果表（表2、表4）与结论。
- **如果复现**：精读第 1 节全部子模块（1.1-1.6）、公式(1)-(6)、图2-6，以及 2.1 数据集 / 2.2 实验环境的全部超参（210 轮、lr 0.001 在 170/200 轮各 ×0.1、±45° 旋转、±35% 缩放、髋部为中心裁剪）。注意区分三套规模数字（COCO 256×192：2.2M/1.4；test-dev 384×288：2.2M/3.3；MPII 256×256：2.5M/1.8）。
- **如果借鉴创新点**：可迁移 GMConv 的多尺度轻量化思路、GWblock 的选择性密集连接、坐标注意力强化空间信息、双分支 Stem 保信息等设计到其他轻量化任务。
- **如果写 related work**：归入"轻量化人体姿态估计 / 基于 HRNet 的改进"，与 LiteHRNet、DiteHRNet、HRFormer、LPN 并列引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[K_跟踪_视频_动作]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的 **2D 人体姿态估计（human pose estimation）** 方向，具体聚焦 **轻量化高分辨率网络设计**，目标是在移动端 / 嵌入式等资源受限设备上实现高精度且较快的人体关键点检测。注意：本笔记文件名"图像识别_融合密度和精细分数的行人检测"是 PDF 自动提取的错误文件名，与论文真实内容（LDHNet 姿态估计）无关——论文既不做行人检测，也不涉及"密度图 + 精细分数"。现有 taxonomy 无独立的"姿态估计"主题，姿态估计是动作识别等视频/动作任务的关键上游，故归入 `K_跟踪_视频_动作` 最为贴切（原 `C2_目标检测_违建_车辆_船舶_行人` 属误归类）。

## 2. 一句话总结
本文以 HRNet 为基线，融合 DenseNet/VoVNet 式密集连接与多尺度膨胀卷积，重新设计特征提取单元（GMConv/GWblock）、Stem 与跨分支特征融合，提出轻量级人体姿态估计网络 LDHNet——把模型规模压到原 HRNet 不足 1/10，同时在 MPII / COCO 上较 LiteHRNet、DiteHRNet 等轻量模型取得更高精度、与 HRFormer 相近性能。

## 3. 背景与问题
- **为什么要做**：2D 姿态估计精度提升伴随模型规模膨胀（上千万参数），训练与部署成本高，与低算力设备的轻量快速需求相悖，轻量化姿态估计成为重要方向。
- **路线**：自顶向下（先检测人体目标再估计单人姿态）性能与鲁棒性更优，本文采用之。
- **之前方法的问题**：
    - 高精度模型（HRNet、ViTPose）规模大、算量高。
    - 轻量级模型（LPN、Lite-HRNet、HRFormer）虽压缩了模型，但轻量网络对特征信息利用不充分，精度仍有损失，提升遇瓶颈。
- **核心矛盾**：如何在极有限的参数量/计算量下尽可能提升检测精度，实现轻量化与高性能的平衡。

## 4. 核心贡献
1.  **LDHNet 架构**：以 HRNet 为基线重设计 4 阶段结构，融入密集连接与多尺度提取并简化特征融合，规模降至原 HRNet 不足 1/10。
2.  **GMConv 多尺度轻量模块**：通道压缩至 1/4 → 膨胀率 1/3/5 三组膨胀卷积级联相加 → 拼接 + 通道洗牌恰好还原通道（无需 1×1 收尾）。
3.  **GWblock 密集连接模块**：VoVNet 式仅保留中间层到最后一层的密集连接，复用特征、加强梯度反传，几乎不增复杂度。
4.  **轻量化特征融合**：高→低分辨率传递改用 3×3 深度可分离卷积并加坐标注意力强化空间信息。
5.  **双分支 Stem**：受 PeleeNet 启发用卷积/池化双分支，无额外参数量/计算量地保留更多原始信息。
6.  **多基准验证**：MPII、COCO val、COCO test-dev 精度对比 + CPU 推理速度对比。

## 5. 方法详解
- **整体框架**：HRNet 式多分支并行，预处理后 4 阶段；阶段 1 仅最高分辨率分支，阶段 2-4 在初始由当前最低分辨率分支下采样生成新分支（尺寸 1/4、通道翻倍），阶段内反复跨分支交互，末端仅输出最高分辨率分支预测关键点（图1，表1）。表1 配置：阶段1 GMCneck（堆叠1/分支1/通道64）、阶段2 GWblock+Fuse（1/2/32,64）、阶段3（4/3/32,64,128）、阶段4（3/4/32,64,128,256，不再多尺度输出）。
- **输入输出**：以髋部为中心裁剪的人体图（COCO 256×192 或 384×288、MPII 256×256）+ 数据增强 → 关键点坐标。
- **关键模块**：
    1.  **Stem**（图2）：第 2 个 3×3 卷积换为卷积/池化双分支下采样，拼接后 1×1 还原；不增参数量却提精度。
    2.  **GSConv**（图3）：通道压缩 1/2 → 深度卷积 + ECA → 拼接还原；3 组串联成 GMCneck（阶段1）。
    3.  **GMConv**（图4，式1-3）：压缩 1/4（式1）→ 膨胀率 1/3/5 级联相加（式2，XT(i)=Di(XT)+XT(i-1)）→ 4 组拼接 + 通道洗牌还原（式3）。
    4.  **GWblock**（图5，式4-6）：2 组 GMConv 密集单元 + 末端 1×1 卷积；第 1 个 GMConv 兼做通道变换（Y1=φ(xin)），末端 xout=φ(Concat[x,Y1,Y2,Y3]) 还原到 xin 通道；仅中间层→最后一层连接，复杂度增量有限。
    5.  **特征融合**（图6）：高→低分辨率的 3×3 卷积换深度可分离卷积 + 坐标注意力（Hou 等 2021），低→高用邻近上采样、同分辨率直接映射、跨度>1 多次采样后相加。
- **训练**：Ubuntu 20.04 / i5-10400F / RTX 3060 12GB / PyTorch 1.10.1 / Python 3.9；Adam，210 轮，lr 0.001 在 170/200 轮各 ×0.1；±45° 旋转、±35% 缩放。
- **差异**：vs HRNet 参数不足 1/10、算量约 1/5；vs LiteHRNet/DiteHRNet 同规模下精度更高；vs HRFormer 更小规模下性能相近。

## 6. 实验与结果
- **数据集**：COCO 2017（约 330K 图、>200K 带标注、约 250K 人体目标；OKS → AP/AP50/AP75/APM/APL/AR，式7）；MPII（约 25K 图、>40K 人体目标、每目标 16 关键点；PCKh@0.5，评估头/肩/肘/腕/髋/膝/踝 7 类部位）。
- **主结果**：
    - **COCO val 256×192**（表2）：LDHNet 2.2M/1.4 GFlops，AP **70.6%**，AP50 **90.5%**（全表最高，>HRNet 89.5%），较 LiteHRNet 67.2 提升 3.4%（正文 3.5%）、较 DiteHRNet 68.3 提升 2.3%（正文 2.4%）、较 LPN-101 70.4 提升 0.2%；较基线 HRNet 73.4 的 AP 略降但 AP50 更高。
    - **COCO test-dev 384×288**（表3）：LDHNet 2.2M/**3.3** GFlops，AP **70.5%**，较 LiteHRNet 69.7 提升 0.8%，AP50 90.6 / AR 76.6。
    - **MPII 256×256**（表4，PCKh@0.5）：LDHNet **2.5M / 1.8** GFlops，Mean **88.5%**；较 LiteHRNet 87.0 提升 1.5%、DiteHRNet 87.6 提升 0.9%、LPN-50 86.6 提升 2.5%；较 HRNet 90.3 用不足 1/10 参数、约 1/5 算量达近似水准。部位：头96.8/肩95.3/肘88.8/腕83.4/髋88.3/膝83.7/踝79.5。
- **消融（MPII，表5-8）**：Stem 使 87.7→88.5（规模不变，表5）；GWConv 把参数量降一个数量级（去掉后 14.7M/5.5）、GMCneck 主要贡献精度（表6）；多尺度膨胀卷积 87.7→88.5（表7）；密集连接 GWblock 82.9→88.5（1.2M→2.5M，表8）。
- **推理速度（图7）**：仅 CPU（i5-10400F）测试，LDHNet 帧率高于 HRNet、优于 LiteHRNet；相比 MobileNetV2/ShuffleNetV2 的高速低精度更平衡。
- **可视化（图8）**：低光、模糊、遮挡、多人场景下表现稳定。

## 7. 这篇论文真正有价值的地方
1.  **可复现的轻量化设计流程**：基线→逐模块替换→逐项消融，方法论清晰，比堆砌组件更有逻辑性。
2.  **GMConv 的紧凑多尺度设计**："压缩 1/4 → 膨胀 1/3/5 级联 → 拼接还原免 1×1"是算量受限下扩感受野的实用技巧。
3.  **GWblock 的选择性密集连接**：表8 证明特征复用是轻量网络高性价比的性能来源（82.9→88.5）。
4.  **对"资源受限下精度天花板"的实证**：在 2~2.5M 参数量级给出了一个有竞争力的精度基准。
5.  **诚实暴露速度瓶颈**：点明 FLOPs/参数量与实际延迟脱节，对工程落地有参考价值。

## 8. 局限与问题
1.  **速度提升未达预期**：参数量大降但推理提速不成比例（结论自述），拟用训练/推理分离 + 重参数化改进。
2.  **速度评测单一**：正文 2.5 节明确仅 CPU 测试（结论另提 GPU 加速对比，口径略不一致），缺多硬件 / 嵌入式真机评测。
3.  **依赖自顶向下框架**：性能受前端人体检测器制约，未讨论联合优化与鲁棒性。
4.  **数据集局限**：仅 MPII/COCO，未对极端拥挤、严重遮挡、非标准姿态做专门定量分析。
5.  **复现细节缺口**：坐标注意力集成位置、通道洗牌实现、图1/图7 精确数值需查图或代码。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + 1.1（图1/表1）+ 表2/表4 + 结论。
- **如果复现**：精读 1.1-1.6 全部模块、式(1)-(6)、图2-6、2.1/2.2 全部超参；区分三套规模（256×192:2.2M/1.4、test-dev 384×288:2.2M/3.3、MPII 256×256:2.5M/1.8）。
- **如果借鉴**：迁移 GMConv 多尺度轻量提取、GWblock 选择性密集连接、坐标注意力、双分支 Stem。
- **如果写 related work**：归入"轻量化人体姿态估计 / HRNet 改进"，与 LiteHRNet、DiteHRNet、HRFormer、LPN 并列。

## 10. 和其他论文的关系
- **基线**：HRNet（Sun 等 2019）。
- **主要轻量级对比 / 同类改进**：Lite-HRNet（Yu 等 2021）、DiteHRNet（Li 等 2022）、LPN（Zhang 等 2020）、Small HRNet（Wang 等 2021）。
- **Transformer 路线对比**：HRFormer（Yuan 等 2021）、ViTPose（Xu 等 2022）。
- **经典姿态估计**：SHN（Newell 等 2016）、CPN（Chen 等 2018）、SBL（Xiao 等 2018）。
- **被借鉴的模块来源**：DenseNet（Huang 等 2017）、VoVNet（Lee 等 2019）、ESPNet（Mehta 等 2019）、MobileNet/深度卷积（Howard/Sandler）、ShuffleNet（Ma 等 2018）、ECA-Net（Wang 等 2020）、坐标注意力（Hou 等 2021）、PeleeNet（Wang 等 2018）。
- **下游关系**：作为人体关键点检测器，LDHNet 可作动作识别、步态分析、人机交互等下游任务的上游组件（属 `K_跟踪_视频_动作` 主题）。

## 11. 关键词
人体姿态估计，轻量级网络，密集连接网络，高分辨率网络，多分支结构，多尺度特征提取（膨胀卷积），坐标注意力，深度可分离卷积，HRNet，模型轻量化。

## 12. 可信度说明
本篇精读完全基于 PDF 提取文本（13/13 页；主体 12/13 + 全文补读 13）生成，未引入外部信息。提取文本覆盖摘要（中英）、引言、第 1 节方法（含公式1-6、表1）、第 2 节实验（含表2-8 的可读数字、OKS/PCKh 定义、超参）与结论。本轮核实并修正了原笔记若干事实偏差：① 文件名/标题/分类纠偏（行人检测→人体姿态估计，C2→K）；② 摘要由乱码直提改为清理后的中英对照；③ MPII 关键点数 16（评估 7 类部位）而非"7 个关键点"；④ 区分三套规模数字（COCO 256×192:2.2M/1.4、test-dev 384×288:2.2M/3.3、MPII 256×256:2.5M/1.8），修正原"COCO test 1.4 GFlops"等错置；⑤ 推理速度正文为 CPU 测试（结论另提 GPU，口径标注差异）；⑥ 补全作者"束阳"。图内精确坐标（图1/图7/图8）受提取限制无法逐一核验，已标注。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (约 2086 字符/页)); 来源缓存: `.paper-cache/extracts/cjig_图像识别_融合密度和精细分数的行人检测.txt` (13/13 页; 原 AI 主体 12/13 + 全文补读 13-13); 生成日期: 2026-06-05; 本轮深度复核与纠偏: 2026-06-18; 模式: LLM (mimo-v2.5-pro) + 人工提示下的 AI 复核。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-13。
- **提取情况**: 缺失页 1 页, 其中 1 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- 未从缺失页稳定识别到章节标题（p.13 为参考文献延续）

### 缺失页关键摘录

- p.13: ECA-Net: Efficient channel attention for deep convolutional neural networks // Proceedings of 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)（参考文献条目）。
<!-- AI_READING_NOTE_END -->
