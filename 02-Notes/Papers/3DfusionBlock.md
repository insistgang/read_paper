---
title: "Multi-Aperture Fusion of Transformer-Convolutional Network (MFTC-Net) for 3D Medical Image Segmentation and Visualization"
authors:
  - "Siyavash Shabani"
  - "Muhammad Sohaib"
  - "Sahar A. Mohammed"
  - "Bahram Parvin"
year: 2024
venue: "T4V@CVPR 2024 Workshop"
doi: 
pdf: [[3DfusionBlock.pdf]]
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
extract_cache: .paper-cache/extracts/3DfusionBlock.txt
---

# Multi-Aperture Fusion of Transformer-Convolutional Network (MFTC-Net) for 3D Medical Image Segmentation and Visualization

## 基本信息
- **PDF**: [[3DfusionBlock.pdf]]
- **primary_topic**: `A1_医学图像_分割`
- **topics**: `A1_医学图像_分割`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Multi-Aperture Fusion of Transformer-Convolutional Network (MFTC-Net) for 3D Medical Image Segmentation and Visualization |
| **作者** | Siyavash Shabani; Muhammad Sohaib; Sahar A. Mohammed; Bahram Parvin（University of Nevada, Reno） |
| **发表时间** | 2024 |
| **刊物/会议** | T4V@CVPR 2024 Workshop（Accepted as a Workshop Paper） |
| **DOI** | 未明确（代码: https://github.com/Siyavashshabani/MFTC-Net） |

## 摘要

> **清理后英文原摘要**（据 PDF 提取文本整理，修复了空格/连字符断裂）：
> Vision Transformers have shown superior performance to the traditional convolutional-based frameworks in many vision applications, including but not limited to the segmentation of 3D medical images. To further advance this area, this study introduces the Multi-Aperture Fusion of Transformer-Convolutional Network (MFTC-Net), which integrates the output of Swin Transformers and their corresponding convolutional blocks using 3D fusion blocks. The Multi-Aperture incorporates each image patch at its original resolutions with its pyramid representation to better preserve minute details. The proposed architecture has demonstrated a score of 89.73±0.04 and 7.31±0.02 for Dice and HD95, respectively, on the Synapse multi-organs dataset—an improvement over the published results. The improved performance also comes with the added benefits of the reduced complexity of approximately 40 million parameters. Our code is available at https://github.com/Siyavashshabani/MFTC-Net

> **中文翻译**：
> Vision Transformer 在众多视觉任务中已展现出优于传统卷积框架的性能，3D 医学图像分割也不例外。为推进这一方向，本文提出多孔径 Transformer-卷积融合网络（MFTC-Net），它用 3D 融合块整合 Swin Transformer 与其对应卷积块的输出。"多孔径"把每个图像 patch 以其原始分辨率连同金字塔表示一并纳入，从而更好地保留细微细节。该架构在 Synapse 多器官数据集上取得 Dice 89.73±0.04、HD95 7.31±0.02，优于已发表结果；性能提升的同时还带来了复杂度降低的额外收益——参数量约 4000 万。代码已开源。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：CNN（如 UNet）擅长提取局部特征，但难以建模长程依赖（全局特征及其关联）。Vision Transformer（ViT）通过自注意力捕捉长程依赖，在分类等任务上超过 ResNet 和 vanilla UNet，并被引入医学图像分割（如 Swin-UNet 用纯 Transformer 替代 UNet 框架）。因卷积块在保留局部信息上的价值，学界转向"融合 Transformer 与卷积表示"的混合架构（如 Swin UNETR 用 Swin 编码器 + 卷积解码器构成 U 形网络）。
- **之前方法的问题**：现有方法（Swin UNETR、nnFormer、UNETR++、3D TransUNet、MIST 等）多通过卷积下采样或金字塔实现"从粗到精"的多尺度表示。作者指出，这种降分辨率的多尺度表示会让相邻器官之间的表面被"扩散/模糊"（diffused），不利于精细表面刻画。
- **核心矛盾与假设**：如何在借助 Transformer 获取全局上下文的同时保留高分辨率局部细节。作者假设——改进的 3D 分割可受益于"多孔径表示"（multi-aperture representation）：对同一区域用多个**重叠的、各自保持原始分辨率**的尺度表示，避免下采样造成的表面扩散。

## 关键贡献

1. **四个并行 Swin Transformer 模块（多孔径）**：把金字塔表示与原始分辨率耦合——每个孔径（aperture）维持原始分辨率，从而在保留细节的同时构建多尺度上下文（原文贡献 i）。
2. **3D 融合块（含 SE + CBAM）**：用 squeeze-and-excitation（SE）块与卷积块注意力模块（CBAM）组合，整合每个 Transformer 及其对应卷积块的输出（原文贡献 ii）。
3. **融合距离变换的损失函数**：将 Dice 交叉熵损失与一个自定义的距离变换项结合，强化器官表面的形态一致性（morphometric consistency）（原文贡献 iii）。
4. **降低模型复杂度**：约 40M 参数，在 Synapse 多器官数据集上以更轻量的模型取得优于已发表结果的成绩。

## 方法

- **整体框架**（图 1）：编码器-解码器结构。编码器并行耦合四个不同孔径的 Swin Transformer（Swin T1–T4）与其对应卷积模块，逐级用 3D 融合块融合。每个 Swin Transformer 计算全局上下文关系，而 3D 卷积块从该表示中、在更高维映射上计算局部特征。**解码器细节在提取文本中未展开**（图 1 展示对称上采样结构，但正文未逐一描述）。
- **输入输出**：输入为从原始数据随机抽取的 3D patch `x ∈ R^{H×W×D}`（实现中 patch 大小为 `128×128×128`）。输出为分割掩膜。
- **多孔径 Swin 编码器（3.1）**：整块 `[H,W,D]` 送入第一个 Transformer（Swin T1）；随后**迭代地取上一个 block 输入的中心区域**作为下一个 block 的输入——第二个 block 的输入取自第一个 block 中心 `[H/2, W/2, D/2]`，第三个取第二个 block 中心 `[H/4, W/4, D/4]`，依此类推。每个孔径都保持原始分辨率。
- **3D 融合块（3.2）**：整合全局与局部空间特征。每个融合块**拼接（concatenate）三路输出**：
    1. Transformer 输出经 **SE 块**（强调通道维信息的重要性）；
    2. Transformer 输出与卷积输出的**逐元素相乘**（Hadamard 点积，调制特征重要性）；
    3. 卷积模块输出经 **CBAM**（加权空间相似性）。
    （注：图 1 caption 把融合块的"汇总模块"描述为 SE、max pooling、averaging blocks，与正文 3.2 的 SE/逐元素相乘/CBAM 表述略有出入；此处以正文 3.2 为准。）
- **损失函数（3.3）**：`Loss(G,P) = DiceCE + λ·(Σ Dᵢ·Sᵢ / Σ Dᵢ)`（式 1）。对每个类别 i，`Dᵢ` 为预测的有符号距离变换的绝对值（归一化到 0–1），`Sᵢ` 为表面点指示函数（表面处为 1、其余为 0），`λ` 为超参数。该距离变换项（DistLoss）惩罚预测表面与真实表面的偏差，提升形态一致性。
- **实现细节（3.4）**：硬件为 Linux 集群，**8× NVIDIA RTX 3080（每卡 12GB）**；所有图像重采样到 `1×1×1 mm` 物理分辨率，每个图像 stack 含 85–198 个切片；提取 `128×128×128` 随机 patch 并按文献 [2] 做增广。训练 **300 epoch**，patch 取自 18 张训练图像；在剩余 12 张图像上测试，保存 300 epoch 内最优模型；最终性能按 **5 折交叉验证**报告。优化器 **Adam，学习率 1e-4，权重衰减 5e-5**。
- **与已有方法的差异**：不同于 Swin UNETR 等用标准下采样/金字塔的"从粗到精"方案，本方法用"多孔径"在多尺度上**以原始分辨率**处理图像块，避免表面扩散；相比 3D TransUNet 等，本文显式设计融合块整合 Transformer 与卷积特征，并引入 DistLoss。

## 实验

- **数据集**：Synapse multi-organs dataset，30 个腹部 CT 扫描病例、8 个器官（脾 Spl、右肾 Kid(R)、左肾 Kid(L)、胆囊 Gal、肝 Liv、胃 Sto、主动脉 Aor、胰腺 Pan）。
- **对比方法**（Table 1）：MIST、Swin UNETR、nnFormer、UNETR++、MISSFormer、LeVit-UNet、3D TransUNet。
- **评价指标**：平均 Dice（↑）与 95% Hausdorff 距离 HD95（↓），并报告参数量（Par）。
- **主实验结果（Table 1）**：
    - MFTC-Net（无 DistLoss）：Avg Dice **89.17**，HD95 **07.47**，40M。
    - MFTC-Net + DistLoss：Avg Dice **89.73±0.04**，HD95 **7.31±0.02**，40M——**平均**优于 3D TransUNet（88.10，81M，HD95 未报告）与 UNETR++（87.22，42M，HD95 07.53）。其余基线平均 Dice：Swin UNETR 83.47（62M）、nnFormer 86.57（150M）、MIST 86.92、MISSFormer 81.96、LeVit-UNet 78.53。
    - **逐器官**：在 8 个器官中的 4 个上取得最高 Dice——脾(96.51)、右肾(93.35)、左肾(93.64)、主动脉(93.05)。另外 4 个器官的最优分属他法：胆囊与肝最高为 3D TransUNet（81.15 / 97.34），胃最高为 MIST（87.23），胰腺最高为 nnFormer（83.35）。**因此本文的优势是"平均 Dice/HD95 + 参数量"层面的综合最优，而非逐器官全面碾压**（原笔记"超过所有对比方法"的措辞略显夸大，已据 Table 1 修正）。
- **可视化对比（4.2，图 2）**：相比 Swin UNETR、nnFormer，本方法的杂散区域更少、器官内连续性更好；与 3D TransUNet 的差异"微小"（minute），只能借助约 50% 的复杂度降低（40M vs 81M）来评判。
- **消融实验**：
    - **损失函数（Table 2）**：`L_dice`=89.04 → `L_focal`=89.50 → `L_dice+L_ce`=89.17 → `L_dice+L_ce+DistLoss`=**89.73**，验证 DistLoss 有效。
    - **Transformer / 融合块数量（Table 3）**：T1=26M→86.12；T1+T2=30M→86.76；T1+T2+T3=34M→87.39；T1+T2+T3+T4=36M→88.75；再加融合块=40M→**89.73**。表明多孔径 Transformer 与融合块均有正向贡献（但作者也指出多孔径 Transformer 的性能提升是"modest level"，伴随参数量增长）。
- **效率信息**：仅强调参数量（40M）相对部分方法（3D TransUNet 81M、nnFormer 150M、Swin UNETR 62M）的下降；**未报告 FLOPs 或推理速度**。

## 局限

- **计算成本未充分比较**：并行四分支 Transformer + 融合块可能带来较高 FLOPs，但论文只报告参数量，未给 FLOPs / 训练或推理时间，效率对比不完整。
- **数据集单一**：仅在 Synapse 腹部 CT 上验证，未涉及其他模态（MRI）、其他部位（心、脑）或更大规模数据，泛化性待验证。
- **多孔径为固定中心裁剪**：孔径取"逐级中心区域"是固定策略，论文未与"自适应/可学习地选择信息量最高区域"作比较，其普适优势有待更多证据。
- **与最强基线差异微小**：作者自述与 3D TransUNet 的可视化差异"微小"，主要靠参数量评判；在该数据集上方法间性能或已接近瓶颈，绝对优势仍需在更具挑战性的场景检验。
- **图/文表述小幅不一致**：图 1 caption（SE/max pooling/averaging）与正文 3.2（SE/逐元素相乘/CBAM）对融合块汇总模块的描述不完全一致，纯文本无法消解。

## 个人评论

1. **"多孔径"的直观思想**：用"不同中心、原始分辨率、不同大小的孔径"替代下采样来获取多尺度上下文，是个清爽的视角。对需要精细边界保持的任务（医学分割、遥感细粒度解析）有启发；但也要注意它本质是"中心区域逐级聚焦"，对偏离中心的结构是否同样受益，论文未深究。
2. **融合块的"分而治之"**：3D 融合块不简单地相加/拼接，而是分别用 SE（通道）、逐元素相乘（特征调制）、CBAM（空间）从不同维度强调信息后再拼接，这种多机制组合比单一融合更灵活，值得借鉴。
3. **任务导向的损失设计**：把 Dice/CE 与基于距离变换的几何约束相结合，直接优化表面形态，是把"解剖先验"写进损失的好范例（消融中 DistLoss 带来约 +0.56 Dice）。
4. **效率-精度平衡**：40M 参数胜过 81M 的 3D TransUNet 与 150M 的 nnFormer（平均 Dice），展示了"靠架构巧思而非堆参数"提升的路径。不过需清醒看到：增益绝对值不大（89.73 vs 88.10），且逐器官并非全胜——这是一篇 workshop 论文（T4V@CVPR2024）量级的扎实改进，而非颠覆性突破。

### 使用建议

- **快速了解**：读 Abstract、Introduction（第 1 段 + 贡献列表）、Results（Table 1 与图 2）、Conclusion。重点看核心思想、平均 Dice/HD95、参数量对比。
- **复现**：精读 Section 3（3.1 Swin 编码器的中心裁剪输入选择、3.2 融合块结构与图 1、3.3 损失公式、3.4 实现细节），结合开源代码（GitHub: Siyavashshabani/MFTC-Net）理解图未尽之处。
- **借鉴创新点**：
    - 多孔径（Multi-Aperture）保持分辨率的多尺度上下文提取思路；
    - 3D 融合块把 SE/CBAM/逐元素操作组合的特征融合范式；
    - 在损失中融入距离变换几何先验的做法。
- **写 Related Work**：归入"结合 Transformer 与 CNN 的 3D 医学图像分割混合架构"，与 3D TransUNet、Swin UNETR、UNETR++、nnFormer、MIST、TransFuse 一并讨论。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A1_医学图像_分割]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇 **3D 医学图像分割** 论文（被 T4V@CVPR 2024 Workshop 接收），来自 University of Nevada, Reno。任务是对腹部 CT 体积做多器官分割，核心是设计一个把 Swin Transformer 全局表示与 3D 卷积局部表示融合的混合编码器。它处理的是规则的体素数据（CT volume）而非无序点云，因此本应归入 **`A1_医学图像_分割`**（原笔记误归入 `D_3D_点云_分类_分割_配准`，本次已修正——该论文与点云的分类/配准无关，只是同属"3D"这一宽泛标签）。

## 2. 一句话总结
MFTC-Net 用四个并行、各自保持原始分辨率的多孔径 Swin Transformer 与对应卷积模块，经 3D 融合块（SE+逐元素相乘+CBAM）集成，并辅以距离变换损失，在 Synapse 多器官 CT 分割上以约 40M 参数取得平均 Dice 89.73 / HD95 7.31。

## 3. 背景与问题
- **为什么做**：CNN 强于局部、弱于全局长程依赖；ViT 强于全局但易丢局部细节。学界因此发展 Transformer-CNN 混合架构（Swin-UNet、Swin UNETR、3D TransUNet、nnFormer、UNETR++、MIST 等），但它们普遍用下采样/金字塔做多尺度。
- **之前方法的问题**：下采样式多尺度表示会"扩散/模糊"（diffuse）相邻器官间的表面，损害精细边界。
- **核心假设**：用"多孔径"（同一区域的多个重叠、各自保持原始分辨率的尺度表示）替代下采样，可避免表面扩散，从而改善表面刻画。

## 4. 核心贡献
1. 四个并行多孔径 Swin Transformer，把金字塔表示与原始分辨率耦合（贡献 i）。
2. 含 SE 与 CBAM 的 3D 融合块，整合每个 Transformer 与其卷积块的输出（贡献 ii）。
3. 把 DiceCE 与自定义距离变换项结合的损失，强化形态一致性（贡献 iii）。
4. 仅约 40M 参数即超过已发表结果——精度与复杂度的双赢。

## 5. 方法详解
- **整体框架**（图 1）：编码器并行四个不同孔径的 Swin Transformer（T1–T4）+ 对应卷积模块，逐级经 3D 融合块融合；解码器对称上采样（提取文本未展开细节）。
- **输入**：随机抽取的 3D patch `x∈R^{H×W×D}`，实现中为 `128×128×128`。
- **多孔径机制（3.1）**：整块送入 T1；下一个 block 的输入是当前 block 输入的**中心区域**——T2 输入取自 T1 中心 `[H/2,W/2,D/2]`，T3 取自 T2 中心 `[H/4,W/4,D/4]`，依此类推；每个孔径都保持原始分辨率（"原始分辨率 + 逐级中心聚焦"，而非降采样）。
- **3D 融合块（3.2）**：拼接三路——(i) Transformer 输出经 SE（通道）；(ii) Transformer 与卷积输出逐元素相乘（特征调制）；(iii) 卷积输出经 CBAM（空间）。图 1 caption 另提到 SE/max pooling/averaging，与正文略异，以正文为准。
- **损失（3.3）**：`Loss(G,P)=DiceCE + λ·ΣDᵢSᵢ/ΣDᵢ`（式 1）。`Dᵢ`=有符号距离变换绝对值（归一化 0–1），`Sᵢ`=表面点指示函数，`λ` 为超参。
- **实现（3.4）**：8× RTX 3080（12GB）；重采样到 1×1×1 mm，stack 85–198 切片；300 epoch；18 训 / 12 测；5 折交叉验证；Adam，lr=1e-4，weight decay=5e-5。

## 6. 实验与结果
- **数据集**：Synapse 多器官 CT（30 例、8 器官）。
- **对比**：MIST、Swin UNETR、nnFormer、UNETR++、MISSFormer、LeVit-UNet、3D TransUNet。
- **指标**：平均 Dice↑、HD95↓、参数量。
- **主结果（Table 1）**：MFTC-Net 89.17/07.47/40M；+DistLoss 达 **89.73±0.04 / 7.31±0.02 / 40M**，平均优于 3D TransUNet（88.10，81M，HD95 未报告）和 UNETR++（87.22，42M）。逐器官在脾(96.51)、右肾(93.35)、左肾(93.64)、主动脉(93.05)上最高；胆囊/肝最高为 3D TransUNet、胃最高为 MIST、胰腺最高为 nnFormer——即"平均最优 + 4/8 器官最优"，并非逐器官全胜。
- **消融**：
    - 损失（Table 2）：dice 89.04 / focal 89.50 / dice+ce 89.17 / dice+ce+DistLoss **89.73**。
    - 模块（Table 3）：T1 26M/86.12 → +T2 30M/86.76 → +T3 34M/87.39 → +T4 36M/88.75 → +Fusion 40M/**89.73**。
- **可视化（图 2）**：杂散区域更少、器官内更连续；与 3D TransUNet 差异"微小"，靠约 50% 参数降低评判。
- **效率**：仅报告参数量，未给 FLOPs/速度。

## 7. 这篇论文真正有价值的地方
1. **多孔径 = 不下采样的多尺度**：以原始分辨率、逐级中心聚焦获取多尺度上下文，规避表面扩散，对边界敏感任务有迁移价值。
2. **多机制融合块**：SE（通道）+ 逐元素相乘（特征调制）+ CBAM（空间）三路拼接，比单一融合更有表达力。
3. **几何先验进损失**：距离变换项把"表面一致性"直接写进目标，消融显示约 +0.56 Dice。
4. **轻量取胜的范例**：40M 击败 81M/150M 基线的平均指标，体现架构巧思优先于参数堆叠。

## 8. 局限与问题
- 未报告 FLOPs/推理时间，"高效"主要落在参数量；并行四分支可能反而增加计算量。
- 仅 Synapse 腹部 CT 单数据集、单模态，泛化未验证。
- 多孔径为固定中心裁剪，未对比可学习的区域选择策略。
- 与最强基线（3D TransUNet）差异"微小"，绝对增益有限（89.73 vs 88.10），逐器官非全胜。
- 图 1 caption 与正文 3.2 对融合块汇总模块描述不完全一致。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Introduction（贡献列表）+ Table 1 + 图 2 + Conclusion。
- **复现**：精读 Section 3（3.1 中心裁剪输入选择、3.2 融合块、3.3 损失、3.4 实现），结合开源代码（GitHub: Siyavashshabani/MFTC-Net）。
- **借鉴**：多孔径多尺度提取 / 多注意力融合块 / 距离变换损失三点。
- **写 Related Work**：归入"Transformer-CNN 混合 3D 医学分割"，与 3D TransUNet、Swin UNETR、UNETR++、nnFormer、MIST、TransFuse 同列。

## 10. 和其他论文的关系
- `[[Swin UNETR]]`：基线兼思路来源（Swin 编码器 + 卷积解码器；本文沿用其增广 [2]）。
- `[[3D TransUNet]]`：主要对比对象、最强基线（88.10，81M）。
- `[[UNETR++]]`：高效混合架构对比方法（87.22，42M）。
- `[[nnFormer]]`、`[[MIST]]`、`[[MISSFormer]]`、`[[LeVit-UNet]]`：Table 1 中的其余对比方法。
- `[[TransFuse]]`：相关工作中提及的 BiFusion 融合思路前驱。
- `[[CBAM]]`、`[[SE-Net]]`（Squeeze-and-Excitation）：融合块中直接使用的注意力模块。
- 上游基础：ViT（Dosovitskiy）、Swin、UNet（Ronneberger）。

## 11. 关键词
MFTC-Net, 多孔径融合, Swin Transformer, 3D 融合块, 3D 医学图像分割, 腹部 CT 多器官分割, 距离变换损失 DistLoss, SE 模块, CBAM, Transformer-CNN 混合架构, Synapse 数据集, T4V@CVPR2024

## 12. 可信度说明
本精读严格基于 PDF 提取文本（6/6 页，约 3800 字符/页，含摘要、引言、相关工作、方法、实验、结论、参考文献）。所有数字（Table 1/2/3 的 Dice、HD95、参数量；训练超参；硬件）均逐项核对自提取文本。本次复核相对原笔记做了三处实质性修正：(1) 主题分类由 `D_3D_点云_分类_分割_配准` 改为更贴切的 `A1_医学图像_分割`（CT 体积分割，非点云）；(2) 补全题目（原缺 "3D Medical Image Segmentation and Visualization"）与会议（T4V@CVPR 2024 Workshop）；(3) 修正"超过所有对比方法"为"平均最优 + 4/8 器官最优"，并补出逐器官实际最优归属。残留不确定性：图 1 中融合块/解码器的精确连接需结合图与代码，纯文本无法完全还原；图 1 caption 与正文 3.2 的小幅措辞差异已标注。

---

> **可信度补充**: PDF 提取质量 = **high** (6/6 页, 约 3800 字符/页, 含完整正文与参考文献); 来源缓存: `.paper-cache/extracts/3DfusionBlock.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮据提取文本重新核校事实与分类。
<!-- AI_READING_NOTE_END -->
