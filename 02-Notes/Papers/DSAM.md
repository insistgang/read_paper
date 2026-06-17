---
title: Dual-domain strip attention for image restoration
authors:
  - "Yuning Cui"
  - "Alois Knoll"
year: 2024
venue: "Neural Networks 171 (2024) 429–439"
doi: 10.1016/j.neunet.2023.12.003
pdf: [[DSAM.pdf]]
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
extract_cache: .paper-cache/extracts/DSAM.txt
---

# Dual-domain strip attention for image restoration

## 基本信息
- **PDF**: [[DSAM.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 文本, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Dual-domain strip attention for image restoration（双域条状注意力图像复原） |
| **作者** | Yuning Cui; Alois Knoll（慕尼黑工业大学 计算、信息与技术学院） |
| **发表时间** | 2024（Received 2023-09-18; Accepted 2023-12-01） |
| **刊物/会议** | Neural Networks 171 (2024) 429–439（Elsevier） |
| **DOI** | 10.1016/j.neunet.2023.12.003 |
| **代码** | https://github.com/c-yn/DSANet |

## 摘要

> 来源: 据 PDF 提取文本整理。

**英文原文（清理后）**：
Image restoration aims to reconstruct a latent high-quality image from a degraded observation. Recently, the usage of Transformer has significantly advanced the state-of-the-art performance of various image restoration tasks due to its powerful ability to model long-range dependencies. However, the quadratic complexity of self-attention hinders practical applications. Moreover, sufficiently leveraging the huge spectral disparity between clean and degraded image pairs can also be conducive to image restoration. In this paper, we develop a dual-domain strip attention mechanism for image restoration by enhancing representation learning, which consists of spatial and frequency strip attention units. Specifically, the spatial strip attention unit harvests the contextual information for each pixel from its adjacent locations in the same row or column under the guidance of the learned weights via a simple convolutional branch. In addition, the frequency strip attention unit refines features in the spectral domain via frequency separation and modulation, which is implemented by simple pooling techniques. Furthermore, we apply different strip sizes for enhancing multi-scale learning, which is beneficial for handling degradations of various sizes. By employing the dual-domain attention units in different directions, each pixel can implicitly perceive information from an expanded region. Taken together, the proposed dual-domain strip attention network (DSANet) achieves state-of-the-art performance on 12 different datasets for four image restoration tasks, including image dehazing, image desnowing, image denoising, and image defocus deblurring. The code and models are available at https://github.com/c-yn/DSANet.

**中文翻译**：
图像复原旨在从退化的观测中重建潜在的高质量图像。近来，Transformer 凭借强大的长程依赖建模能力，显著推进了多种图像复原任务的最优性能；然而自注意力的二次方复杂度阻碍了其实际应用。此外，充分利用干净图像与退化图像之间巨大的频谱差异，同样有助于图像复原。本文提出一种用于图像复原的**双域条状注意力机制**，通过增强表征学习来提升性能，它由**空间条状注意力单元**和**频率条状注意力单元**组成。具体而言，空间条状注意力单元在一个简单卷积分支学得的权重引导下，为每个像素从同一行或同一列的相邻位置汇聚上下文信息；频率条状注意力单元则通过频率分离与调制在频谱域细化特征，且由简单的池化操作实现。进一步地，我们对不同尺寸的条状施加多尺度学习，以更好地应对各种尺度的退化。通过在不同方向部署双域注意力单元，每个像素可隐式感知一个被扩展区域的信息。综合而言，所提出的**双域条状注意力网络（DSANet）** 在去雾、去雪、去噪、去焦模糊**四类图像复原任务的 12 个数据集**上取得了最优性能。代码与模型见 https://github.com/c-yn/DSANet。

## 研究背景与动机

- **论文为什么要做**：图像复原是病态问题，传统手工先验在复杂真实场景下难以泛化；CNN 的两个固有缺陷与复原任务不匹配——i) 静态卷积核不随输入特征自适应，难以处理空间变化的模糊；ii) 有限感受野无法建模大尺度退化所需的长程像素交互。
- **之前方法的问题**：Transformer 的自注意力能建模长程依赖，但其复杂度对相关维度呈二次方，难以处理高分辨率图像。已有的降本方案均未打破二次方本质：1）局部窗口自注意力（Liang 等，SwinIR）把注意力限制在小窗口内，复杂度仍对窗口尺寸二次方；2）通道自注意力（Zamir 等，Restormer）把注意力从空间维转到通道维，复杂度仍对通道二次方；3）条状自注意力（Tsai 等，Stripformer）在条状区域内算自注意力，复杂度仍对条状尺寸二次方。
- **作者想解决的核心矛盾**：如何在**高效聚合长程上下文**与**控制计算成本**之间取得平衡，同时**充分利用干净/退化图像对在频谱域的巨大差异**来提升复原。作者的取舍是：不再改进自注意力本身，而是回到 CNN，并借入自注意力的"内容自适应"特性来做廉价的信息聚合。

## 关键贡献

1.  **提出空间条状注意力单元（SSA）**：用极轻量旁路分支（GAP → 1×1 卷积 → Sigmoid）直接生成长度为 K 的注意力权重，再以卷积式加权求和在水平/垂直方向聚合上下文信息，复杂度由自注意力的 O((HW)²C) 降到 O(HWCK)，实现**线性复杂度**的高效整合。
2.  **提出频率条状注意力单元（FSA）**：仅用条状平均池化把特征分离为高/低频分量，再用**逐通道可学习参数**（无任何卷积层）对各频率分量做调制，在频谱域轻量地细化特征。
3.  **提出双域条状注意力机制（DSAM）**：组织多尺度 FSA 与不同条状尺寸的 SSA，**在频率域与空间域同时执行双方向、多尺度**的注意力，高效增强表征学习。
4.  **提出双域条状注意力网络（DSANet）**：将 DSAM 集成进编码器-解码器架构，在**去雾、去雪、去噪、去焦模糊四类任务的 12 个基准数据集**上取得当时最优性能。
5.  **会议版扩展**：本文是会议工作（Cui, Tao, Jing & Knoll, 2023）的期刊扩展。三项主要改进：a) 新增频谱（FSA）单元，在三类任务上一致提升——在 SOTS-Outdoor 上**+0.38 dB PSNR，仅增加 0.05M 参数与 0.46 GFLOPs**；b) 方法扩展到图像去噪任务，并在 7 个额外数据集（4 个真实去雾、1 个夜间去雾、2 个去雪）上评估；c) 补充更多消融实验验证新频谱注意力的有效性。

## 方法

**整体框架**（图1a）：基于 CNN 的 DSANet 采用编码器-解码器架构，分三个尺度。编/解码器各含 3 个 ResGroup；每个 ResGroup 由 N 个残差块 + 1 个定制残差块组成，定制残差块把 DSAM 夹在两个 3×3 卷积之间。
- 输入退化图像 I ∈ R^{3×H×W}，先经单个 3×3 卷积提取浅层特征（C×H×W）。
- 编码器逐级扩大通道数、把空间分辨率渐进降到 H/4 × W/4；下采样用步长卷积实现。
- 解码器用转置卷积上采样；解码特征与编码特征拼接后接 1×1 卷积把通道减半。
- 最后用 3×3 卷积输出残差图像 R ∈ R^{3×H×W}，复原图像 Î = I + R。

**关键模块详解**：

1.  **空间条状注意力单元（SSA）**（图2a，图3）：
    - **复杂度分析（动机）**：自注意力 Attention(Q,K,V)=Softmax(QKᵀ)V 的复杂度来自三处——生成 Q/K/V 为 3HWC²，注意力图 QKᵀ 为 (HW)²C，加权求和为 (HW)²C；后两项对空间尺寸二次方。SSA 针对这三步降本。
    - **权重生成（去掉 Q/K/V）**：A = σ(W₁ₓ₁(GAP(X))) ∈ R^K（公式2），即对输入做全局平均池化、1×1 卷积、Sigmoid，得到长度为 K（K≪W）的权重向量；A **在空间与通道维度上共享**以进一步省算。
    - **卷积式聚合**：̂X_{c,h,w} = Σ_{k=0}^{K-1} A_k · X_{c,h,w-⌊K/2⌋+k}（公式3），复杂度 O(HWCK)，远低于 (HW)²C。
    - **双向构成**：X^{SSA}_K = SSA_K(X) = S^V_K(S^H_K(X))（公式5），即顺序执行水平再垂直算子。图3 推导：先水平得 B=w_AB·A+w_BB·B+w_CB·C，再垂直使中心像素 D = w_BD·B + w_DD·D 展开后隐式感知 K×K 区域，从而把感受野从 K 隐式扩展到 K×K。
    - **多尺度**：DSAM 中用 K=7 与 K=11 两种尺寸。

2.  **频率条状注意力单元（FSA）**（图2b）：
    - **频率分离**：用条状平均池化（均值滤波）对以 X_{c,h,w} 为中心、长度 K 的条状区域 S 取低频分量 X^l = AP(S)（公式7）；高频分量 X^h = X − X^l（公式8，即输入减低频）。
    - **频率调制**：̂X = W¹_l·X^l + W¹_h·X^h（公式9），其中 W_l、W_h ∈ R^C 是**逐通道可学习注意力参数**，由反向传播直接更新，**全程不使用任何卷积层**（区别于 Guo 2023、Zou 2021 等先前频率方法）。
    - **双向构成**：X^{FSA}_K = FSA_K(X) = V_K(H_K(X))（公式10），水平、垂直算子各有自己的一组参数（W¹ 与 W²）。

3.  **双域条状注意力机制（DSAM）**（图1c，公式11-13）：
    - X′ = W₁ₓ₁( FSA_{K=7}(X) + FSA_{K=11}(X) + FSA_{global}(X) )：输入先并行通过三种尺度（K=7、K=11、global，global 指水平/垂直算子中 K=W/H）的 FSA，三支相加后由 1×1 卷积融合。
    - X₁, X₂ = Split(X′)：把融合特征沿通道维均分两半。
    - ̂X = [ SSA_{K=7}(X₁), SSA_{K=11}(X₂) ]：两半分别送入 K=7 与 K=11 的 SSA，再沿通道拼接为 DSAM 输出。
    - **设计逻辑**：先多尺度频率域调制，再分组多尺度空间域聚合，实现双域、多尺度的联合增强。

**损失函数**：采用双域 L1 损失。空间域损失 L_s = (1/E)·‖Î−G‖₁（公式14）；频域损失 L_f = (1/E)·‖F(Î)−F(G)‖₁（公式15，F 为快速傅里叶变换，E 为归一化元素总数）。总损失 L_total = L_s + λ·L_f，λ 经验设为 **0.1**。

**实现细节**：用 Adam 优化器，初始学习率 2e−4 并逐步衰减（提取文本在 4.1 节此处被截断，后续衰减策略/迭代数等未覆盖）。

**和已有方法的差异**：
- 与**条状自注意力**（Tsai/Stripformer、Dong、Li 等）不同：它们在条状区域内做自注意力、对条状尺寸二次方；本文 SSA 用旁路网络生成权重 + 廉价卷积式聚合，线性复杂度。
- 与**频率网络**（基于 FFT 的 Guo 2023、Huang 2022、Mao 2021；基于小波/OctConv/DCT 的方法）不同：本文 FSA 仅用条状池化做频率分离、用逐通道参数做调制，不依赖 FFT/卷积，更轻量。
- 与一般通道/像素/空间注意力（Qin、Zamir、Chen 等）不同：那些方法只对特征施加权重而不聚合上下文；本文在施权重的同时完成上下文聚合，并兼顾双域与多尺度。

## 实验

- **任务与数据集**：在**4 类任务的 12 个基准数据集**上评估——图像去雾、去雪、去焦模糊、去噪。提取文本（截断于 4.1 节）明确点名的具体数据集为 **SOTS-Outdoor**（去雾，用于报告 +0.38 dB 提升）；其余各任务的逐数据集名单与对比数字表位于第 4 节后半部分，**提取缓存未覆盖（待核）**。
- **评测协议**：表格中最优结果加粗、次优结果加下划线（best/second-best in bold/underlined）。常用指标按领域惯例为 PSNR/SSIM（提取文本未直接列出指标公式，待核）。
- **会议版→期刊版关键增益（已核）**：新增 FSA 频谱单元在 **SOTS-Outdoor 上带来 +0.38 dB PSNR，仅增加 0.05M 参数与 0.46 GFLOPs**——这是 FSA 单元相对会议版的净贡献，并非整网相对所有基线的差距。
- **泛化评估（已核）**：模型在 **4 个真实世界去雾数据集、1 个夜间去雾数据集、2 个去雪数据集**（共 7 个额外数据集）上进一步评估。
- **消融实验（已核）**：作者声称做了更多消融以证明新设计的频谱注意力（FSA）的有效性；具体消融数字表提取缓存未覆盖（待核）。
- **效率**：强调线性复杂度注意力带来的高效计算；整网逐项参数量/FLOPs/速度对比表提取缓存未覆盖（待核）。

> 提取文本仅覆盖前 11 页（至 4.1 节学习率一句被截断）。第 4 节后半的全部对比数字表、逐数据集 SOTA 结果、详细消融表均在缓存之外，本节凡涉及具体数值已标注"待核"。

## 局限

> 以下为基于方法与实验范围的合理推断，非论文明确自陈（论文未设独立"局限"小节，提取文本亦未覆盖结论部分）。

- **静态单图设定**：方法面向单幅静态图像复原，对视频序列的时序/时空建模能力未涉及。
- **退化分布依赖**：训练多依赖合成退化，对极端或未知真实退化的鲁棒性需进一步验证（论文已在真实去雾/去雪数据上做了泛化测试以部分缓解此点）。
- **频率假设**：FSA 假设退化信息可被条状高/低频分量有效解耦，对不符合该假设的退化类型可能受限。
- **超参依赖**：性能可能依赖条状尺寸组合（K=7/11/global）、残差块数 N、损失权重 λ=0.1 等设置，迁移到新任务可能需重调。
- **整体开销**：虽单元线性，但 DSAM 串/并联多个 FSA+SSA，超大图或实时场景下整网开销仍需实测（具体 FLOPs 表提取缓存未覆盖）。

## 个人评论

1.  **解耦"注意力生成"与"特征聚合"是核心范式**：SSA 把自注意力里最贵的 Q/K/V 与 (HW)² 点积全部砍掉，改用 GAP→1×1→Sigmoid 生成一个**跨空间与通道共享**的小权重向量，再以卷积式滑窗聚合。这等价于"内容自适应的可分离条状卷积"，是把自注意力的自适应性蒸馏进卷积成本里的干净做法，值得迁移到检测/分割骨干。
2.  **FSA 的极简主义**：不做 FFT、不加卷积，仅用条状池化分高低频 + 两个逐通道标量调制，几乎零成本（+0.05M/+0.46 GFLOPs）却能稳定提升，说明"频率分离+逐通道再加权"这一最朴素操作已能吃到频谱差异红利，工程性价比极高。
3.  **两方向顺序 = K×K 隐式感受野**：用水平后接垂直、把 O(K) 的两次一维操作组合出 O(K²) 的二维感受野，是低成本扩感受野的经典技巧，DSAM 再叠多尺度（7/11/global）补足尺度覆盖。
4.  **需要警惕之处**：论文主张的"线性 vs 二次方"优势在模块层面成立，但整网堆叠多个双域单元后的真实墙钟时间/显存并未在提取文本中给出；其相对 Restormer/SwinIR 的端到端效率优势需看完整表后再下结论。0.38 dB 也只是 FSA 这一增量的贡献，不应误读为整网相对所有基线的领先幅度。

### 使用建议

- **快速了解**：读摘要 + 引言后两段 + 图1/图2，即可抓住"旁路生成权重 + 条状卷积聚合 + 频率池化调制"三件套。
- **如果复现**：精读 3.2–3.4 节与公式 2–13，重点是 A 的共享方式、公式3 的滑窗下标、FSA 高频=输入−低频、DSAM 的 Split/Concat 通道分配；实现细节看 4.1 节（注意提取缓存在此处截断，需回原文补全衰减策略与各任务超参）。
- **如果借鉴创新点**：把 SSA 当"可分离条状自适应卷积"、FSA 当"零卷积频率门控"，评估能否嵌入其他视觉任务的特征增强位。
- **如果写 Related Work**：可归入 1) 高效注意力；2) 频率/双域图像处理；3) 条状/窗口注意力；4) 图像复原通用架构。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于低层视觉的**图像复原**方向，但其核心技术贡献是设计一个**高效的注意力算子/模块**（双域条状注意力 DSAM），并以此搭建复原网络 DSANet。因贡献落点在通用、可移植的注意力模块，归类于 **B_注意力算子模块** 主题最贴切（而非按某一具体复原子任务归类）。发表于 Neural Networks 171 (2024)，是同作者会议工作的期刊扩展版。

## 2. 一句话总结
DSANet 用"旁路网络生成共享权重 + 条状卷积式聚合"的空间单元（SSA）和"条状池化分频 + 逐通道参数调制"的频率单元（FSA），在空间域与频率域、多尺度、双方向上做线性复杂度的注意力增强，在 4 类复原任务 12 个数据集上达到最优。

## 3. 背景与问题
- **为什么做**：复原是病态问题；CNN 静态核不自适应、感受野有限；Transformer 自注意力虽建模长程依赖却对相关维度二次方复杂度，难处理高分辨率图。
- **前法缺陷**：窗口注意力（SwinIR）、通道注意力（Restormer）、条状自注意力（Stripformer）都只是把二次方转移到窗口/通道/条状尺寸，**未打破二次方本质**；且多数注意力只对特征施权重、不聚合上下文。
- **核心矛盾**：长程上下文聚合 vs 计算成本；同时想吃到干净/退化图像对的**频谱差异**红利。作者选择回到 CNN、借入自注意力的内容自适应性来做廉价聚合。

## 4. 核心贡献
1. **SSA**：A=σ(W₁ₓ₁(GAP(X)))∈R^K 生成跨空间/通道共享权重，卷积式滑窗聚合，复杂度 O(HWCK)（vs 自注意力 (HW)²C），水平+垂直顺序得 K×K 隐式感受野。
2. **FSA**：条状均值池化取低频、输入减低频得高频、逐通道可学习参数 W_l/W_h 调制，**零卷积**，极轻量。
3. **DSAM**：三尺度 FSA（7/11/global）相加→1×1 融合→通道二分→分送 K=7/11 的 SSA→拼接，双域多尺度联合。
4. **DSANet**：编解码架构集成 DSAM，12 数据集/4 任务 SOTA。
5. **会议版扩展**：新增 FSA（SOTS-Outdoor +0.38 dB / +0.05M / +0.46 GFLOPs）、扩展到去噪、新增 7 数据集泛化与更多消融。

## 5. 方法详解
**框架**（图1a）：三尺度编解码；ResGroup = N 个残差块 + 1 个把 DSAM 夹在两 3×3 卷积间的定制块。I∈R^{3×H×W}→3×3 卷积出浅层特征→编码器扩通道、降分辨率至 H/4×W/4（步长卷积下采样）→解码器转置卷积上采样、与编码特征拼接后 1×1 减半通道→3×3 卷积出残差 R，Î=I+R。

**SSA**（公式2-5，图2a/图3）：先做自注意力复杂度分析指出 (HW)²C 二次方瓶颈→去掉 Q/K/V，用 GAP+1×1+Sigmoid 生成长度 K（K≪W）的共享权重 A→̂X_{c,h,w}=Σ A_k·X_{c,h,w−⌊K/2⌋+k}（O(HWCK)）→水平后接垂直 S^V_K(S^H_K(X))，图3 推导中心像素隐式感知 K×K。DSAM 内 K∈{7,11}。

**FSA**（公式7-10，图2b）：X^l=AP(S)（条状均值池化低频）→X^h=X−X^l（高频）→̂X=W¹_l·X^l+W¹_h·X^h（逐通道参数，无卷积）→水平后接垂直 V_K(H_K(X))，两方向各一组参数。

**DSAM**（公式11-13，图1c）：X′=W₁ₓ₁(FSA₇+FSA₁₁+FSA_global)→Split 成 X₁,X₂→[SSA₇(X₁),SSA₁₁(X₂)] 拼接。global 指 K=W/H。

**损失**（公式14-15）：L_s=(1/E)‖Î−G‖₁，L_f=(1/E)‖F(Î)−F(G)‖₁（F=FFT），L_total=L_s+0.1·L_f。Adam，初始 lr=2e−4 渐减（4.1 节后续被截断）。

## 6. 实验与结果
- **范围**：4 任务（去雾/去雪/去焦模糊/去噪）× 12 基准数据集；表格 best 加粗、second-best 下划线。
- **已核数值**：FSA 相对会议版在 **SOTS-Outdoor +0.38 dB PSNR，+0.05M 参数，+0.46 GFLOPs**。
- **泛化**：4 真实去雾 + 1 夜间去雾 + 2 去雪共 7 个额外数据集评估。
- **消融**：声称做了更多消融验证 FSA 有效性。
- **待核**：各任务逐数据集 SOTA 对比表、消融数字表、整网参数/FLOPs/速度表均在**提取缓存（前11页，截断于4.1节）之外**，PDF 文本未覆盖，本笔记不臆造具体数字。

## 7. 这篇论文真正有价值的地方
1. **解耦注意力生成与聚合**：把自注意力最贵的部分换成"小旁路网络生成共享权重 + 卷积式聚合"，等价于内容自适应的可分离条状卷积，是把自注意力红利蒸馏进卷积成本的干净范式。
2. **FSA 极简频率门控**：无 FFT、无卷积，仅池化分频 + 两个逐通道标量，几乎零成本却稳定提升，验证"频率分离+逐通道再加权"已足够吃频谱差异红利。
3. **低成本扩感受野**：两个一维方向顺序组合出 K×K 二维感受野，再叠多尺度（7/11/global）补尺度。
4. **工程性价比**：简单池化/卷积/乘加堆出强模块，落地友好。

## 8. 局限与问题
（论文无独立局限节、提取未覆盖结论，以下为推断）静态单图设定、对极端/未知真实退化的鲁棒性待验、FSA 的频率可分离假设对某些退化可能不成立、超参（K 组合/N/λ）依赖、整网真实墙钟开销与显存提取文本未给出。0.38 dB 仅是 FSA 增量、非整网相对所有基线的领先。

## 9. 我该怎么使用这篇论文
快速了解读摘要+引言尾两段+图1/2；复现精读 3.2-3.4 与公式 2-13（注意 A 的共享、公式3 滑窗下标、高频=输入−低频、DSAM 的 Split/Concat），实现细节回原文补全（4.1 在缓存中截断）；借鉴时把 SSA 当可分离条状自适应卷积、FSA 当零卷积频率门控，评估能否嵌入检测/分割特征增强位；写 Related Work 归入高效注意力/频率双域/条状窗口注意力/复原通用架构。

## 10. 和其他论文的关系
- [[SwinIR]]（Liang 等，窗口自注意力）、[[Restormer]]（Zamir 等，通道自注意力）：作为高效自注意力的代表基线与对比对象，本文以"仍二次方"区别于它们。
- [[Stripformer]]（Tsai 等，条状自注意力去模糊）：**最直接相关**，本文 SSA 以"线性 vs 对条状尺寸二次方"与之区分。
- FFA-Net（Qin 等，通道+像素注意力去雾）：被归为"只施权重不聚合上下文"的注意力，作为背景引用。
- 频率类工作（Guo 2023 窗口频率通道注意力、Huang 2022 相位/幅度、Mao 2021 频域卷积、小波/OctConv/DCT 系）：FSA 以"无 FFT/无卷积、仅池化+逐通道参数"与之区分。
- 同作者会议版（Cui, Tao, Jing & Knoll, 2023）：本文的前身，期刊版主要增量即 FSA。

## 11. 关键词
图像复原，双域学习，高效网络（注意力），条状注意力，空间注意力，频率注意力，多尺度表征，编码器-解码器，去雾/去雪/去噪/去焦模糊。（原文 Keywords：Image restoration, Dual-domain learning, Efficient network）

## 12. 可信度说明
本笔记基于提取缓存的**前 11 页**（含摘要、引言、相关工作 2.1-2.3、方法 3.1-3.5 全部公式、实验 4.1 开头）。**方法与公式部分提取质量高、可逐式核对**，背景/贡献/会议版增量（含 +0.38 dB / +0.05M / +0.46 GFLOPs、12 数据集/4 任务、7 个泛化数据集）均有原文支撑。**第 4 节后半的全部对比数字表、逐数据集 SOTA、消融表、效率表在缓存之外**，凡涉及具体数值已标注"待核/PDF 文本未覆盖"，未臆造。局限节为合理推断（论文未独立列出）。

---

> **可信度补充**: PDF 提取质量 = **high** (方法/公式可逐式核对; 实验数字表在前11页之外, 缺第4节后半数据); 来源缓存: `.paper-cache/extracts/DSAM.txt` (11/11 页, 截断于 4.1 节); 生成日期: 2026-06-05; 复核重写: 2026-06-18; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
