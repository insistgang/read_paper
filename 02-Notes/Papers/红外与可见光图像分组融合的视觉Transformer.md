---
title: 红外与可见光图像分组融合的视觉Transformer
authors:
  - "孙旭辉"
  - "官铮"
  - "王学"
year: 2023
venue: "中国图象图形学报"
doi: 10.11834/jig.220515
pdf: [[红外与可见光图像分组融合的视觉Transformer.pdf]]
primary_topic: C3_目标检测_红外_可见光融合
topics:
  - "C3_目标检测_红外_可见光融合"
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
extract_cache: .paper-cache/extracts/红外与可见光图像分组融合的视觉Transformer.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/13 pages"
---
# 红外与可见光图像分组融合的视觉Transformer

## 基本信息
- **PDF**: [[红外与可见光图像分组融合的视觉Transformer.pdf]]
- **primary_topic**: `C3_目标检测_红外_可见光融合`
- **topics**: `C3_目标检测_红外_可见光融合`
- **状态**: ai-read（已提取 PDF 内容, 待人工复核）
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 红外与可见光图像分组融合的视觉Transformer（Vision transformer for fusing infrared and visible images in groups） |
| **作者** | 孙旭辉; 官铮（通信作者）; 王学 |
| **单位** | 云南大学信息学院（昆明 650500） |
| **发表时间** | 2023（第28卷 第1期，pp. 0166-0178） |
| **刊物/会议** | 中国图象图形学报（Journal of Image and Graphics） |
| **DOI** | 10.11834/jig.220515 |
| **基金** | 国家自然科学基金项目（61761045） |

## 摘要

**清理后的英文原摘要**（据 PDF 提取文本整理，修复连写并剔除杂入字符）：

> Current image fusion can be as one the key branches of information fusion. Infrared and visible image fusion (IVF) is developed for image fusion dramatically. A visible-light-sensor-derived image can capture light-reflected. It is rich in texture detail information and fit to the human eye observation pattern. The image-fused can integrate rich detail information and thermal radiation information. Therefore, it is essential for such applications like object tracking, video surveillance, and autonomous driving. To resolve the constraints of manual-designed feature extraction and feature fusion in traditional infrared and visible image fusion methods, as well as the problems that convolutional neural network based (CNN-based) methods cannot effectively extract global contextual information in images and inadequate fusion during feature fusion, we develop a visual-transformer-based end-to-end unsupervised fusion network via group-layered fusion strategies. First, a channel-attention-based transformer is designed, which enhances the features further through computing the self-attention in the channel dimension and using the channel attention in series as the feed-forward network of the transformer. After that, to extract features from the source image, the transformer module and CNN are used in parallel to form a local-global feature extraction module. In addition, to alleviate the loss of feature information, we design a newly layer-grouped fusion module to fuse the local-global features by grouping the features in the channel dimension, fusing the corresponding groups initially, and then fusing different groups via a hierarchical residual structure. Experiments on the publicly available datasets TNO and RoadScene compared with six popular methods (traditional and deep-learning-based) show that, on the TNO dataset, the proposed method achieves the best results in NMI, QNICE, AG and SD, improving by 30.90%, 0.58%, 11.72% and 11.82% over the second-best method; on the RoadScene dataset it achieves the best results as well.

**中文翻译**（亦可对照原文中文摘要）：

> **目的**：针对传统红外与可见光图像融合方法中人工设计特征提取与特征融合的局限性，以及基于卷积神经网络（CNN）的方法无法有效提取图像全局上下文信息、特征融合过程中融合不充分的问题，提出基于视觉 Transformer 和分组渐进式融合策略的端到端无监督图像融合网络。
> **方法**：首先，将在通道维度上计算自注意力的多头转置注意力（MDTA）模块与通道注意力（SE）模块组合成视觉 Transformer——MDTA 解决了自注意力计算量随像素大小呈平方增长的问题，SE 通道注意力则强化突出特征。其次，将 CNN 与该视觉 Transformer 并联组成局部—全局特征提取模块（LGFE），提取源图像中的局部细节与全局上下文信息，使特征兼具通用性与全局性。此外，为避免融合过程中信息丢失，通过将特征分组并构造渐进残差结构进行融合，最后解码得到融合图像。
> **结果**：在 TNO 与 RoadScene 数据集上与 6 种方法比较。主观上能有效融合互补信息得到优质融合图像；客观上，在 TNO 数据集上相比性能第 2 的方法，在归一化互信息（NMI）、非线性相关信息熵（QNICE）、平均梯度（AG）和标准差（SD）上分别提高 30.90%、0.58%、11.72%、11.82%；在 RoadScene 数据集上上述 4 个指标依然取得最佳。
> **结论**：本文方法在融合质量上取得显著提升，能有效突出红外显著目标、保留源图像背景与细节纹理，在对比度与清晰度上具有优越性。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：可见光图像由捕获反射光的可见光传感器产生，含丰富的颜色、对比度、纹理细节，更符合人眼观察模式，但在恶劣天气环境下成像质量受损；红外图像由热传感器获取，热辐射信息强、能在背景中突出目标，但缺少细节纹理。融合二者可获得既含红外热辐射目标信息、又含可见光丰富纹理细节的融合图像，已广泛应用于目标追踪、自动驾驶和视频监测等领域。
- **之前方法的问题**（论文将 IVF 方法分为传统方法与深度学习方法两类）：
    1.  **传统方法**：在空间域或变换域提取特征并按特定融合规则融合，典型有基于多尺度变换的方法（Pajares 和 de la Cruz，2004 等）和基于稀疏表示（SR）的方法（Li 等，2012）。缺陷：① 融合质量严重依赖人工设计的特征提取手段，特征不具广泛通用性；② 不同特征需采用不同的融合规则。
    2.  **深度学习方法**：基于 GAN 的方法（如 FusionGAN）在融合图像与源图像间构造对抗博弈，但网络结构与损失函数设计不当时会导致源图像信息丢失；基于 CNN 的方法提升了特征通用性，但受卷积局部感受野限制，**无法有效提取图像中的全局上下文信息**，导致特征信息不足、融合质量下降。此外，多数端到端网络仅简单地将特征图拼接，**融合不充分**。
- **核心矛盾**：如何同时有效地提取图像的局部细节信息与全局上下文信息，并设计一个能充分融合这些互补信息、减少信息丢失的机制。

## 关键贡献

1.  **设计了基于通道注意力的视觉Transformer模块**：将多头转置注意力（MDTA）模块与通道注意力（SE）模块串联组成视觉 Transformer，其中 SE 作为 Transformer 的前馈网络（替代全连接层）。MDTA **在通道维度而非空间维度计算自注意力**，将注意力矩阵从空间的 `R^{HW×HW}` 降为通道的 `R^{C×C}`，解决了自注意力计算量随像素分辨率呈平方增长的问题；MDTA 模块借鉴自 Restormer（Zamir 等，2022）。
2.  **构建了局部—全局特征提取模块（LGFE）**：将 CNN（类 DenseNet 的密集块）与所设计的视觉 Transformer **并联**。CNN 分支提取局部细节、保证特征通用性，Transformer 分支提取全局上下文、弥补卷积的全局建模不足，使最终特征兼具通用性与全局性。
3.  **提出了分组渐进式融合模块（GPF）**：受 Res2Net（Gao 等，2021）启发，将输入特征图沿通道维度分为 `s` 组（文中 s=4），先对同组特征初步融合，再通过分层渐进残差结构逐组融合，使融合过程体现多尺度性并减少信息丢失，比直接拼接更充分。
4.  **设计了端到端的无监督训练策略**：以结构相似性损失 `L_S`、均方误差损失 `L_M` 和感知损失 `L_P` 的组合作为总损失，从结构、像素强度、特征三个层面约束融合图像与源图像的一致性，无需标签与预训练分类网络。
5.  **在多个数据集上取得领先性能**：在 TNO 和 RoadScene 数据集上，本文方法在 NMI、QNICE、AG、SD 等指标上超越 6 种主流对比方法，定性结果显示其能更好地突出红外目标、保留细节纹理并提升对比度与清晰度。

## 方法

- **整体框架**（图1）：端到端结构，输入为配对红外图像与可见光图像，输出为融合图像。特征提取阶段采用两条结构相同但**不共享参数**的支路分别处理红外、可见光图像。每条支路先经两个卷积块提取浅层特征（卷积块 = 3×3 卷积 + BN + LeakyReLU），再经 **局部—全局特征提取模块（LGFE）** 提取局部—全局特征，然后将两支路特征送入 **分组渐进式融合模块（GPF）** 融合，最后由 3 个卷积块组成的解码器解码得到融合图像。
- **输入输出**：输入为原始红外、可见光图像对；输出为融合图像（提取文本未明确说明融合图像的通道数，通常为灰度）。
- **关键模块**：
    1.  **局部—全局特征提取模块（LGFE，图2(a)）**：含上、下两个分支。
        - **局部细节分支（上分支）**：结构类似 DenseNet（Huang 等，2017），由 4 层密集块组成，第 q 层输出 `X_q = F_q(cat(X_0, X_1, …, X_{q-1}))`，`F_q` 含 3×3 卷积和 LeakyReLU，`cat` 为前几层输出的通道拼接，使细节分支更好地学习原始浅层细节特征。
        - **全局结构信息分支（下分支）**：由 **MDTA 模块 + SE 模块** 组合成视觉 Transformer。
            - **MDTA（多头转置注意力，图2(b)）**：输入 `X∈R^{H×W×C}` 先层归一化，再经 1×1 卷积和 3×3 深度卷积生成 Q、K、V（`Q=W^Q_1(W^Q_2(X))` 等，`W_1` 为 1×1 卷积、`W_2` 为 3×3 深度卷积）。将 Q、K 维度转为 `R^{HW×C}` 和 `R^{C×HW}` 后矩阵相乘，生成 `R^{C×C}` 的转置注意力图 A（而空间自注意力会生成 `R^{HW×HW}`）。过程为 `X̂ = W_1(F_A(Q,K,V)) + X`，`F_A(Q,K,V) = V × F_sm(K×Q/α)`，`F_sm` 为 softmax，`α` 为可学习缩放参数（公式1）。
            - **SE（通道注意力，图2(c)）**：因 MDTA 输出已是通道维自注意力结果，故用 SE 替代前馈全连接层。`Y = F_S(COV_{3×3}(COV_{3×3}(F_AVG(X̂)))) · X̂`，`F_AVG` 为平均池化，`COV_{3×3}` 为 3×3 卷积 + LeakyReLU，`F_S` 为 sigmoid（公式2），进一步强化由 MDTA 获得的全局特征。
    2.  **分组渐进式融合模块（GPF，图3）**：
        - **输入**：两支路 LGFE 输出的红外特征图 `Y_I` 与可见光特征图 `Y_V`。
        - **过程**：① `Y_I`、`Y_V` 各经 1×1 卷积后沿通道维度分为 `s` 组（s=4），得到 `Y_I^i`、`Y_V^i`（`i∈{1,…,s}`）；② 同组拼接后经 3×3 卷积改变维度，得初步融合特征 `z_i = Conv_i(cat(Y_I^i, Y_V^i))`；③ 渐进融合：`Z_1 = z_1`；`i=2` 时 `Z_i = Conv_i^F(cat(z_i, z_{i-1}))`；`2<i≤s` 时 `Z_i = Conv_i^F(cat(z_i, Z_{i-1}))`；④ `M = cat(Z_1, Z_2, …, Z_i)`（公式3）。`Conv_i`、`Conv_i^F` 均为 3×3 卷积 + BN + LeakyReLU。
        - **直观解释**：每个 `Conv_i^F` 得到的融合特征潜在地包含了之前所有组的融合特征，使细节信息与全局信息更充分融合；且每次 `z_i` 经 3×3 卷积都会使 `Z_i` 获得更大感受野，逐组融合体现多尺度融合效果，比直接拼接更有效。
- **训练方式**：
    - **损失函数**：总损失 `L_T = L_S + λ1·L_M + λ2·L_P`（公式4，`λ1=10, λ2=1`），分别从结构相似性、像素强度、特征图差异约束融合图像与源图像。
        - `L_S`（结构相似性，公式5-6）：`L_S = f_SSIM(I_F, I_I) + f_SSIM(I_F, I_V)`，对融合图像 `I_F` 与红外 `I_I`、可见光 `I_V` 分别计算 SSIM。
        - `L_M`（均方误差，公式7）：因红外图像以像素强度为特征，为保留红外像素强度信息，**仅计算** `L_M = f_MSE(I_F, I_I)`。
        - `L_P`（感知损失，公式8）：用预训练 VGG-19 提取多层特征 `ψ_i`（m=4 层），计算 `I_F` 分别与 `I_I`、`I_V` 在特征空间的 MSE 之和（Johnson 等，2016）。
    - **训练数据**：TNO 数据集约 60 对图像，随机选 20 对，按步长 14 裁剪为 128×128 图像块，得 30360 对训练数据。
    - **优化器/超参**：Adam，初始学习率 0.0001，自适应学习率下降（忍耐系数 15 周期、调整系数 0.1），批大小 32，历元 50，PyTorch 实现，硬件为 RTX 3090 GPU + Intel i9-10900F CPU。
- **推理流程**：输入一对红外、可见光图像，前向传播直接得到融合图像，无需后处理。
- **与已有方法的差异**：
    1.  **特征提取**：相比纯 CNN 方法（如 DenseFuse）增加了全局建模能力；相比在像素/空间维度做自注意力的 Transformer 融合方法（CGTF、SwinFusion），本文在**通道维度**计算自注意力，计算量不随像素大小平方增长，且相比 CGTF **不用固定输入图像尺寸**，更灵活。
    2.  **特征融合**：摒弃简单拼接/加权平均，采用**分组渐进残差融合**（受 Res2Net 启发），融合更充分。
    3.  **训练范式**：端到端无监督，直接优化结构+像素+感知三项损失，无需预训练分类网络或手工融合规则。

## 实验

- **使用数据集**：
    - **训练集**：TNO 数据集（约 60 对，随机选 20 对，步长 14 裁剪为 128×128，得 30360 对，主要为军事场景）。
    - **测试集**：TNO（选 20 对）；RoadScene（Xu 等 2022 创建，含 221 对精确对齐的红外/可见光图像，源自 FLIR 视频，主要为含车辆、行人、建筑等的道路场景，选 40 对作测试）。
- **对比方法**：6 种——深度学习方法 DenseFuse（Li 和 Wu，2019）、DRF（Xu 等，2021）、DualFuse（Fu 和 Wu，2021）、FusionGAN（Ma 等，2019b）、GANMcC（Ma 等，2021）；传统方法 MDLatLRR（Li 等，2020）。
- **评价指标**：6 个——参考指标 NMI（归一化互信息）、QNICE（非线性相关信息熵，原文部分处写作 QNCIE）、QAB/F（基于边缘的相似性/梯度保留）、VIF（视觉信息保真度）；无参考指标 AG（平均梯度/清晰度）、SD（标准差/对比度）。
- **主实验结果**：
    - **定性**：本文方法能有效保留可见光纹理细节并突出红外热辐射目标，背景中云、路灯、帐篷、灌木、人物轮廓等细节保留更好，对比度与清晰度更优；DenseFuse/FusionGAN/MDLatLRR 红外目标不够突出且有伪影，DRF 会丢失背景云层。
    - **定量（表1，TNO 20 对均值）**：本文在 NMI(**0.5023**)、QNICE(**0.8108**，消融表中记 0.8107)、AG(**2.7593**)、SD(**46.5850**) 上最优，分别比第 2 名**提高 30.90%、0.58%、11.72%、11.82%**；QAB/F(0.4071) 第 2（次于 MDLatLRR 0.4541），VIF(0.8377) 第 2（次于 DRF 1.0067）。作者解释 QAB/F 略低于 MDLatLRR 是因全局分支弱化了部分梯度细节。
    - **定量（表2，RoadScene 40 对均值）**：本文在 NMI(**0.5323**)、QNICE(**0.8121**)、AG(**4.7032**)、SD(**54.4701**) 上同样最优；VIF(0.6982) 在 RoadScene 上反超 DRF（QAB/F 0.4652 仍次于 MDLatLRR 0.4708）。英文摘要给出 RoadScene 上 NMI/QNICE/AG/SD/VIF 相对第 2 名提升约 **32.74%、0.64%、24.53%、31.40%、31.73%**（据原文英文摘要数值，列举略多于 4 项，提取文本如此）。
- **消融实验（表3，TNO）**：去除 LGFE 中 Transformer 模块（仅留局部细节分支）或去除 GPF 模块（改为直接拼接）后，6 项指标整体下降——无 Transformer：NMI 0.4698 / SD 42.1901；无 GPF：NMI 0.4553 / SD 39.6536；完整模型 NMI 0.5023 / SD 46.5850，证明两个核心模块的有效性。
- **泛化实验**：仅在 TNO 训练、在 RoadScene 测试仍取得最优，证明泛化能力。
- **运行效率（表4，单位 s）**：本文 TNO 0.2817、RoadScene 0.1070，慢于最快深度学习方法（DualFuse 0.0860 / DenseFuse 0.0422，TNO 上与最优 DualFuse 差约 0.2s，RoadScene 上与最快 DenseFuse 差约 0.06s），但远快于传统方法 MDLatLRR（30.6983 / 11.2754）。作者认为自注意力带来的时间代价相对融合质量提升是值得的。

## 局限

1.  **任务范围局限**：结论明确指出本文工作**只限于红外与可见光图像融合，不适用于其他图像任务**（如医学、多光谱/多曝光融合），下一步方向是更多样化的融合任务。
2.  **运算效率**：引入自注意力机制带来比纯 CNN 方法更高的计算开销（表4），作者也将"提高模型运算效率、节省运算时间"列为后续工作。
3.  **训练数据规模有限**：训练数据仅从 TNO 的 20 对图像裁剪扩充而来，基础数据多样性与规模有限，可能影响泛化上限。
4.  **消融不够细致**：消融仅验证去除 Transformer 与 GPF 的影响，未对密集块层数、分组数 s、损失权重 λ1/λ2 做敏感性分析（提取文本未给出这些消融）。
5.  **定性评价依赖人工选图**：定性分析基于作者选定的 5 幅典型图像，可能存在选择性偏差。

## 个人评论

1.  **问题驱动、逻辑连贯**：清楚地把"CNN 缺全局建模 + 端到端网络融合不充分"两个痛点拆开，分别用 LGFE（并联 CNN/Transformer）与 GPF（分组渐进残差）对症下药，方法叙事与实验验证（两个消融分别对应两个模块）一一对应，说服力强。
2.  **模块设计的可迁移性**：
    - **通道维自注意力（MDTA）** 直接借鉴 Restormer，其价值在于把注意力复杂度从 `O(HW²)` 降到 `O(C²)` 并解除输入尺寸约束——这对高分辨率融合任务很实用，但也意味着核心算子的原创性有限。
    - **GPF 的"分组—渐进残差"** 借鉴 Res2Net，把"提取后直接拼接"改成结构化的逐组信息流动，思路可迁移到其他多源/多尺度融合问题；这是本文相对工程化但有效的亮点。
3.  **实验较扎实但可更强**：双数据集、6 对比方法、6 指标 + 消融 + 泛化 + 效率，覆盖面够；不足是定量优势集中在 NMI/AG/SD 等"信息量/清晰度/对比度"类指标，而在更贴近人眼感知的 QAB/F、VIF 上并非全场最优（QAB/F 始终次于 MDLatLRR），作者对此有诚实解释。
4.  **可信度注意**：英文摘要列出的 RoadScene 提升百分比（5 个数字对应 4 个标注指标名）排版混乱，引用这些具体提升比例时应回查原文表 2 核对。

### 使用建议

- **快速了解**：读中文摘要、引言后半段（提出问题处）、图1（总体结构）、图2（LGFE/MDTA/SE）、图3（GPF）和结论。
- **复现**：精读第 2 章（2.1 总体结构、2.2 LGFE、2.3 GPF、2.4 损失）与第 3.1 节实验设置；关键公式为 1（MDTA）、2（SE）、3（GPF）、4-8（损失）。注意密集块各层卷积通道数等细节正文未全部给出，需结合图示或代码。
- **借鉴创新点**：① CNN+Transformer 并联的局部—全局特征提取范式；② 分组渐进残差融合（Res2Net 思路用于多源融合）；③ 结构+像素强度（仅对红外）+感知 的无监督复合损失设计。
- **写 related work**：可归入"红外与可见光图像融合""视觉 Transformer 在图像融合中的应用""基于深度学习的多模态图像融合"。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C3_目标检测_红外_可见光融合]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的**多模态图像融合**方向，具体聚焦**红外与可见光图像融合**（Infrared and Visible Image Fusion, IVF）。它针对传统融合方法依赖人工设计特征、以及基于 CNN 的方法无法有效提取全局上下文信息且端到端网络"提取后直接拼接"导致融合不充分这两个痛点，提出基于视觉 Transformer 与分组渐进式融合策略的端到端无监督融合网络。归入 **"C3_目标检测_红外_可见光融合"** 主题贴切——它产出的高质量红外/可见光融合图像正是目标追踪、自动驾驶、视频监测等下游任务的输入。

## 2. 一句话总结
用"并联 CNN 与通道维自注意力 Transformer"的 LGFE 模块同时抓取局部细节与全局上下文，再用受 Res2Net 启发的"分组渐进残差"GPF 模块充分融合两模态特征，端到端无监督地生成兼顾红外热目标突出与可见光纹理保留的融合图像。

## 3. 背景与问题
- **为什么做**：可见光图像细节/纹理丰富、符合人眼，但恶劣天气下退化；红外图像热辐射强、能突出目标，但缺细节纹理。融合二者可互补，用于目标追踪、自动驾驶、视频监测。
- **之前方法的问题**：
    1.  **传统方法**（多尺度变换、稀疏表示）：融合质量严重依赖人工设计的特征提取手段，特征不通用，且不同特征需不同融合规则。
    2.  **深度学习方法**：基于 GAN 的方法（FusionGAN）在结构/损失设计不当时丢失源图像信息；基于 CNN 的方法受卷积局部感受野限制，**无法有效提取全局上下文**；且多数端到端网络仅**简单拼接特征**，融合不充分、信息丢失。
- **核心矛盾**：如何同时有效提取局部细节与全局上下文，并设计能充分融合互补信息、减少信息丢失的机制。

## 4. 核心贡献
1.  **通道注意力视觉 Transformer**：MDTA（多头转置注意力，借鉴 Restormer）+ SE（作前馈网络），在通道维度算自注意力，注意力矩阵从 `R^{HW×HW}` 降为 `R^{C×C}`，解决自注意力随像素分辨率平方增长的问题，且不限输入尺寸。
2.  **局部—全局特征提取模块 LGFE**：CNN（类 DenseNet 密集块）与视觉 Transformer **并联**，局部细节 + 全局上下文，使特征兼具通用性与全局性。
3.  **分组渐进式融合模块 GPF**：受 Res2Net 启发，通道维分 4 组，同组初步融合后经分层渐进残差结构逐组融合，体现多尺度性、减少信息丢失，优于直接拼接。
4.  **端到端无监督训练**：结构相似性 + 均方误差（仅对红外）+ 感知（VGG-19）三项复合损失，从结构、像素强度、特征三层面约束。
5.  **领先性能**：TNO/RoadScene 上 NMI、QNICE、AG、SD 等指标超越 6 种主流方法。

## 5. 方法详解
- **整体框架（图1）**：端到端。两条结构相同但**不共享参数**的支路分别处理红外、可见光图像；先经 2 个卷积块（3×3 卷积+BN+LeakyReLU）取浅层特征 → LGFE 取局部—全局特征 → GPF 融合 → 3 个卷积块组成的解码器输出融合图像。
- **输入输出**：原始红外/可见光图像对 → 融合图像（通道数提取文本未明确，通常为灰度）。
- **关键模块**：
    1.  **LGFE（图2(a)）**：
        - **局部细节分支**：类 DenseNet 的 4 层密集块，`X_q = F_q(cat(X_0,…,X_{q-1}))`，`F_q` = 3×3 卷积 + LeakyReLU，密集连接利于学习浅层细节。
        - **全局结构分支**：MDTA + SE 组成视觉 Transformer。
            - **MDTA（图2(b)，公式1）**：`X∈R^{H×W×C}` 经层归一化 → 1×1 卷积 + 3×3 深度卷积生成 Q/K/V；Q、K 转为 `R^{HW×C}` 与 `R^{C×HW}` 相乘得 `R^{C×C}` 转置注意力图 A；`X̂ = W_1(F_A(Q,K,V)) + X`，`F_A = V × softmax(K×Q/α)`，α 可学习缩放。
            - **SE（图2(c)，公式2）**：替代前馈全连接，`Y = sigmoid(COV_{3×3}(COV_{3×3}(AvgPool(X̂)))) · X̂`，强化通道维显著特征。
    2.  **GPF（图3，公式3）**：`Y_I, Y_V` 各经 1×1 卷积后通道维分 s=4 组；同组拼接经 3×3 卷积得 `z_i = Conv_i(cat(Y_I^i, Y_V^i))`；渐进残差：`Z_1=z_1`，`i=2` 时 `Z_2=Conv_2^F(cat(z_2,z_1))`，`2<i≤s` 时 `Z_i=Conv_i^F(cat(z_i,Z_{i-1}))`；`M=cat(Z_1,…,Z_s)`。每个 `Conv_i^F` 隐含前面所有组的融合结果，且逐次 3×3 卷积扩大感受野，体现多尺度融合。
- **损失（公式4-8）**：`L_T = L_S + 10·L_M + 1·L_P`。`L_S = SSIM(I_F,I_I)+SSIM(I_F,I_V)`；`L_M = MSE(I_F,I_I)`（仅红外，保像素强度）；`L_P = Σ MSE(ψ_i(I_F),ψ_i(I_I)) + Σ MSE(ψ_i(I_F),ψ_i(I_V))`（VGG-19，m=4 层）。
- **训练**：TNO 约 60 对中选 20 对，步长 14 裁 128×128 得 30360 对；Adam，lr=0.0001，自适应下降（忍耐 15、调整系数 0.1），batch 32，epoch 50，PyTorch，RTX 3090 + i9-10900F。
- **与已有差异**：vs 纯 CNN（DenseFuse）补全局建模；vs 空间维自注意力（CGTF/SwinFusion）改通道维、不限输入尺寸；vs 简单拼接改分组渐进残差融合；端到端无监督，无需预训练分类网或手工规则。

## 6. 实验与结果
- **数据集**：训练 TNO（20 对→30360 块）；测试 TNO（20 对）+ RoadScene（221 对中选 40 对）。
- **对比方法**：DenseFuse、DRF、DualFuse、FusionGAN、GANMcC（深度学习）+ MDLatLRR（传统）。
- **指标**：NMI、QNICE、QAB/F、VIF（参考）+ AG、SD（无参考）。
- **定量**：
    - **TNO（表1）**：本文 NMI **0.5023** / QNICE **0.8108** / AG **2.7593** / SD **46.5850** 最优，比第 2 名 +30.90% / +0.58% / +11.72% / +11.82%；QAB/F 0.4071（次于 MDLatLRR 0.4541）、VIF 0.8377（次于 DRF 1.0067）排第 2。
    - **RoadScene（表2）**：本文 NMI **0.5323** / QNICE **0.8121** / AG **4.7032** / SD **54.4701** 最优；VIF 0.6982 反超 DRF；QAB/F 0.4652 仍次于 MDLatLRR 0.4708。英文摘要另给 RoadScene 提升约 32.74%/0.64%/24.53%/31.40%/31.73%（原文数值，排版混乱，引用需回查表2）。
- **定性**：更好保留可见光纹理（路灯、帐篷、树叶）与红外热目标（人、车轮廓高亮），对比度/清晰度更优；对比方法存在红外目标不突出、伪影、背景云层丢失等问题。
- **消融（表3，TNO）**：无 Transformer → NMI 0.4698、SD 42.1901；无 GPF → NMI 0.4553、SD 39.6536；完整 → NMI 0.5023、SD 46.5850。两模块均有效。
- **效率（表4，s）**：本文 TNO 0.2817 / RoadScene 0.1070，慢于 DualFuse(0.0860)/DenseFuse(0.0422) 但远快于 MDLatLRR(30.6983/11.2754)。

## 7. 这篇论文真正有价值的地方
1.  **问题—方法—消融三者对齐**：两个痛点对应两个模块，两个消融分别拆掉这两个模块，论证闭环干净。
2.  **可迁移的工程思路**：通道维自注意力（降复杂度、解尺寸约束）+ 分组渐进残差融合（替代简单拼接）这两套机制都可迁移到其他多源/高分辨率融合任务。
3.  **诚实的指标分析**：对 QAB/F 始终次于 MDLatLRR 给出了"全局分支弱化梯度细节"的合理解释，而非回避。
4.  **完整的端到端无监督流程**：复合损失（结构+像素强度仅红外+感知）设计清晰，便于复现与借鉴。

## 8. 局限与问题
1.  **仅限 IVF**：结论自陈不适用于其他图像任务；未验证医学/多光谱/多曝光等其他融合。
2.  **效率非最优**：自注意力带来比纯 CNN 更高的开销，作者将提效列为后续工作。
3.  **训练数据规模小**：仅 20 对 TNO 图像裁剪扩充，基础多样性有限。
4.  **消融不够细**：未对密集块层数、分组数 s、损失权重 λ1/λ2 做敏感性分析。
5.  **核心算子原创性有限**：MDTA 源自 Restormer、GPF 源自 Res2Net，创新主要在"组合 + 应用于 IVF"层面。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言后半 + 图1/2/3 + 结论。
- **复现**：精读 2.1-2.4 与 3.1；核对公式 1-8 与训练超参（batch 32 / epoch 50 / step 14 / 128×128 / λ1=10,λ2=1）；部分卷积通道数正文未给，需看图或代码。
- **借鉴创新点**：CNN+Transformer 并联取局部—全局特征；分组渐进残差融合（Res2Net 思路）；无监督复合损失（SSIM + 仅红外 MSE + VGG-19 感知）。
- **写 related work**：归入红外可见光融合 / 视觉 Transformer 图像融合 / 深度学习多模态融合。

## 10. 和其他论文的关系
- [[Restormer]]（Zamir 等，2022）：本文 MDTA 模块的直接来源（通道维转置注意力），基础算子层面的相关工作。
- Res2Net（Gao 等，2021）：GPF 分组渐进残差结构的灵感来源。
- CGTF（Li 等，2022）：另一篇 CNN+视觉 Transformer 的红外可见光融合工作，本文在"通道维 vs 像素维自注意力、是否需固定输入尺寸"上与之对比。
- SwinFusion（Ma 等，2022）：基于 Swin Transformer 的通用图像融合，像素维自注意力，本文对比对象。
- [[DenseFuse]]、[[DRF]]、[[DualFuse]]、[[FusionGAN]]、[[GANMcC]]、MDLatLRR：本文 6 个定量对比 baseline。

## 11. 关键词
红外图像，可见光图像，图像融合，视觉 Transformer，卷积神经网络（CNN），局部—全局特征提取，多头转置注意力（MDTA），通道注意力（SE），分组渐进式融合，无监督学习

## 12. 可信度说明
本精读基于 PDF 提取缓存（标注 12/13 页，实际覆盖中文摘要、英文摘要、引言、相关工作、第 2 章方法全部公式 1-8、第 3 章实验设置/对比/消融/效率全部表 1-4 及结论）。关键事实——网络结构、MDTA/SE/GPF 公式、损失函数、训练超参（batch 32、epoch 50、step 14、s=4、λ1=10/λ2=1）、TNO/RoadScene 定量数值（表1-4）、6 对比方法、6 指标——均能在提取文本中直接核对，可信度 **high**。需注意两点：① 融合图像输出通道数、密集块各层精确通道数正文未明确，需依图示/代码；② 英文摘要中 RoadScene 提升百分比（5 个数对应 4 个标注指标名）排版混乱，引用具体百分比时建议回查原文表 2。提取缓存标注 p.13（参考文献末尾）未含正文内容，不影响方法与实验结论的完整性。

---

> **可信度补充**: PDF 提取质量 = **high** (提取覆盖 12/13 页, 含全部公式与表 1-4 数值, 1875 字符/页); 来源缓存: `.paper-cache/extracts/红外与可见光图像分组融合的视觉Transformer.txt` (12/13 页; p.13 为参考文献末尾, 缺失不影响正文); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-13。
- **提取情况**: 缺失页 1 页, 其中 1 页提取到可读文本。p.13 为参考文献列表末尾, 不含正文/实验内容。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: TransactionsonBiomedicalEngineering,59(12):3450-3459
- p.13: Objectiveassessmentofmultiresolutionimagefusionalgorithmsfor
- p.13: TransactionsonPatternAnalysisandMachineIntelligence,34(1):
- p.13: LiuZ,LinYT,CaoY,HuH,WeiYX,ZhangZ,LinSandGuoB
- p.13: Fusion:cross-domainlong-rangelearningforgeneralimagefusion
- p.13: VaswaniA,ShazeerN,ParmarN,UszkoreitJ,JonesL,GomezAN,
- p.13: NN:ageneralimagefusionframeworkbasedonconvolutionalneural

### 缺失页关键摘录

- p.13: 2020.Infraredandvisibleimagefusionviadetailpreservingadver- sariallearning.InformationFusion,54:85-98[DOI:10.1016/j.
<!-- AI_READING_NOTE_END -->
