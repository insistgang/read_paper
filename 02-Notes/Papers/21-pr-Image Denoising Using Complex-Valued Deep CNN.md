---
title: 21-pr-Image Denoising Using Complex-Valued Deep CNN
authors:
  - "Yuhui Quan"
  - "Yixin Chen"
  - "Yizhen Shao"
  - "Huan Teng"
  - "Yong Xu"
  - "Hui Ji"
year: 2024
venue: "Pattern Recognition"
doi: 
pdf: [[21-pr-Image Denoising Using Complex-Valued Deep CNN.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
status: ai-read
reading_stage: ai-fulltext
confidence: high
source_basis: pdf-text
date_added: 2026-06-05
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/21-pr-Image Denoising Using Complex-Valued Deep CNN.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/32 pages"
---
# 21-pr-Image Denoising Using Complex-Valued Deep CNN

## 基本信息
- **PDF**: [[21-pr-Image Denoising Using Complex-Valued Deep CNN.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-05

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Image Denoising Using Complex-Valued Deep CNN |
| **作者** | Yuhui Quan; Yixin Chen; Yizhen Shao; Huan Teng; Yong Xu; Hui Ji |
| **单位** | 华南理工大学计算机科学与工程学院 (Quan/Chen/Shao/Teng/Xu); 新加坡国立大学数学系 (Ji) |
| **发表时间** | 2024 (Preprint submitted to Pattern Recognition, July 25, 2024) |
| **刊物/会议** | Pattern Recognition |
| **DOI** | 未明确 |

## 摘要

**英文原摘要 (据 PDF 提取文本整理, 修复断字与空格)**:
> While complex-valued transforms have been widely used in image processing and have their deep connections to biological vision systems, complex-valued convolutional neural networks (CNNs) have not seen their applications in image recovery. This paper aims at investigating the potentials of complex-valued CNNs for image denoising. A CNN is developed for image denoising with its key mathematical operations defined in the complex number field to exploit the merits of complex-valued operations, including the compactness of convolution given by the tensor product of 1D complex-valued filters, the nonlinear activation on phase, and the noise robustness of residual blocks. The experimental results show that, the proposed complex-valued denoising CNN performs competitively against existing state-of-the-art real-valued denoising CNNs, with better robustness to possible inconsistencies of noise models between training samples and test images. The results also suggest that complex-valued CNNs provide another promising deep-learning-based approach to image denoising and other image recovery tasks.
>
> **Keywords**: Complex-Valued Operations; Convolutional Neural Network; Image Denoising; Deep Learning

**中文翻译**:
> 复数值变换在图像处理中已被广泛使用, 并与生物视觉系统有深刻联系, 但复数值卷积神经网络 (CNN) 尚未被应用于图像复原。本文旨在探究复数值 CNN 在图像去噪中的潜力。我们将网络的关键数学运算定义在复数域上, 以发挥复数值运算的优势, 包括: 由 1D 复数值滤波器张量积带来的卷积紧凑性、相位上的非线性激活、以及残差块的噪声鲁棒性。实验结果表明, 所提复数值去噪 CNN 在与最先进实数值去噪 CNN 的对比中具有竞争力, 并且在训练样本与测试图像间可能存在的噪声模型不一致时表现出更好的鲁棒性。结果还表明, 复数值 CNN 为图像去噪及其他图像复原任务提供了另一条有前景的深度学习路线。
>
> **关键词**: 复数值运算; 卷积神经网络; 图像去噪; 深度学习

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 图像去噪是从输入图像中去除测量噪声的任务。在移动设备摄影普及的背景下它具有实用价值, 同时也是大多数图像复原任务的关键组成部分。受深度学习在计算机视觉中巨大成功的启发, 近年来出现了大量基于深度学习 (尤其是 CNN) 的去噪方法。但提取文本明确指出: **所有已有的基于 CNN 的去噪方法都建立在实数值 CNN 之上**, 而复数值变换 (离散傅里叶变换、Gabor 变换、双树复小波变换) 在图像处理中广泛使用, 复数值 NN 在图像复原中的潜力却未被探索, 这与复数值变换在图像处理中的广泛采用相矛盾。
- **生物视觉依据**: 论文强调复数表示与生物视觉的深刻联系——灵长类初级视皮层 V1 区以复杂细胞 (complex cells) 为主, 这些细胞对方向和频率具有选择性 (其感受野常用 Gabor 小波建模); V4 区多数细胞也更接近 V1 的复杂细胞而非简单细胞。复数表示引入的**相位 (phase) 主导了对视觉场景的感知**: 已知仅用图像傅里叶变换的相位即可恢复图像的大部分信息 (形状、边缘、方向)。一个信号在复数变换下可分解为幅度 |F(f)| 和相位 ϕ(f): F(f) = |F(f)|·e^{iϕ(f)}。
- **之前方法的问题**: 现有 CNN 去噪方法的性能高度依赖训练样本与测试数据在**图像内容和噪声特性**两方面的匹配程度。当噪声分布复杂或空间变化时, 干净图像虽充足, 但其带噪版本可能不足, 难以训练出泛化能力好的 CNN。
- **核心矛盾**: 如何利用复数值表示在数学上的优势 (更紧凑的滤波器表示、对相位的非线性处理、残差块的噪声鲁棒性) 来提升 CNN 的去噪性能, 尤其是在训练与测试噪声模型不一致的实际场景下的鲁棒性。

## 关键贡献

提取文本中作者明确将贡献归纳为三点:
1.  **首个研究复数值 CNN 用于图像去噪的工作**: 在以往实数值 CNN 主导图像复原网络设计的背景下, 本文首次研究复数值 CNN 在底层视觉任务 (图像去噪) 中的潜力, 并表明复数值 CNN 对图像去噪确有其优势。
2.  **去噪 CNN 中关键数学运算的复数值新设计**: 在复数域定义若干基本运算以发挥相对实数版本的潜在优势——(i) 通过 1D 复数值滤波器张量积得到 2D 滤波器的紧凑表示, 有助于避免过拟合; (ii) 相位上的非线性激活, 有助于提升去噪性能; (iii) 对实际中常见的噪声模型不一致具有更好鲁棒性的残差块。
3.  **一个实用且具竞争力的去噪 CNN**: 在标准数据集上的实验表明, 所提复数值 CNN (CDNet) 在训练与测试噪声模型完全匹配时性能与最先进实数值去噪 CNN 相当; 而在噪声模型不一致的多种场景下 (测试图像噪声水平未知、噪声标准差在像素间变化、噪声为多种类型混合) 展现出优于其他方法的鲁棒性。

## 方法

### 整体框架
所提网络称为 **CDNet (Complex-valued Denoising Network)**, 将带噪图像 Y 映射到无噪图像 X: CDNet: Y∈R^{M1×M2} → X∈R^{M1×M2} (公式 4)。整体由 **24 个顺序连接的卷积单元** 组成 (图 3)。除第一个单元外, 每个卷积单元含一个复数值卷积层, 后接复数值批归一化和复数值 ReLU。**所有卷积层使用 64 个卷积核**。中间 18 个卷积单元实现为 **9 个残差块**。

### 复数值卷积层 (3.2)
- 卷积核为复数值张量 {K_i ∈ C^{L×L×D1}}, 沿输入深度 D1 延展; 实际设置 **L=3** (所有卷积层)。前向卷积见公式 (6), 输出复数值特征立方体 (公式 5)。
- **张量积紧凑性**: 两个 1D 复数值滤波器 (a1+ib1, a2+ib2) 的张量积关于实部/虚部不可分 (公式 2), 可模拟不同方向的 2D 不可分滤波器 (如图 1 的 1D Gabor 滤波器)。提取文本给出精确数量关系: 用复数表示只需 **4L 个自由度** 即可生成两个定义在 R^{L×L} 上的 2D 不可分滤波器, 而实数表示需要 **2L² 个自由度**——因此复数卷积更紧凑, 有助于避免过拟合。
- **1D 分解**: 在所有残差块中, 2D 卷积用两个连续的 1D 卷积实现 (公式 7), k1_i∈C^{L×1×D}, k2_i∈C^{1×L×D}, 将每层参数量从 **DL² 降到 2DL** (D 为通道数)。
- **四实卷积实现**: 复数卷积可写成四个实卷积 (公式 8: A∗K = (ℜ(A)∗ℜ(K) − ℑ(A)∗ℑ(K)) + i·(ℜ(A)∗ℑ(K) + ℑ(A)∗ℜ(K))), 从而可用现有实数深度学习框架。论文指出这"类似于双宽度 (double-width) CNN", 但区别在于复数卷积引入了实部与虚部间的额外交互, 而实数网络不会在没有复数动机的情况下自发建立这种连接。
- 反向传播 (公式 10-12): 复数核的梯度按复分析链式法则计算, ∂f/∂K = (∂f/∂B)∗A, 其实部/虚部同样由四个实卷积组合得到。

### CReLU 激活函数 (3.3)
- 采用 **CReLU** (公式 15): CReLU(z) = ReLU(ℜ(z)) + i·ReLU(ℑ(z)), 即分别对实部和虚部做标准 ReLU。它在幅度上与实数 ReLU 机制相同, 但在**相位上产生复杂的非线性激活**——图 2 显示其在相位环上有 4 种不同模式 (z=0、z=ℜz、z=ℑz、z=z), 使网络能在幅度域和相位域同时定义噪声图像到无噪图像的映射。
- 论文还讨论了两种对比激活: **ModReLU** (公式 16, 文本原文误写为 "MoeReLU", 有可训练偏置 b, 保持相位不变) 和 **zReLU** (公式 17-18, 仅当实部与虚部均为正即相位∈[0,π/2] 时激活)。实验将表明 CReLU 优于 ModReLU 与 zReLU。

### 复数值批归一化 (3.4)
用于改善泛化和加速收敛 (公式 19)。提取文本在此处截断 (定义到公式 19 后即止), 具体复数 BN 公式未覆盖; 据缺失页线索, 论文将 BN 适配到复数域是"分别对实部/虚部做 batch normalization"。

### 复数值残差块 (3.5, 据原文后续页, 提取缓存未覆盖, 待核)
利用 [6] 中复数表示在联想记忆机制上的噪声鲁棒检索性质——残差块与记忆单元架构相似 (残差被计算并插入由恒等连接提供的"记忆"), 因此复数值残差块对**噪声模型不一致**应有更好鲁棒性 (图 4)。

### 模块连接与网络流程
- 输入图像先经第一个卷积单元。
- 第一个残差块前用一个步长 2 的复数值卷积下采样, 接复数 BN 和 CReLU; 最后一个残差块后用步长 2 的复数值转置/反卷积上采样, 同样接复数 BN 和 CReLU——用以扩大感受野并提升计算效率。
- 中部为 9 个复数值残差块 (即 18 个卷积单元)。
- 末端 **合并层 (merging layer)** 将复数特征转换为实数输出图像。据缺失页摘录, 合并方式是"只取复数值特征的幅度 (amplitude)"。
- 使用 **跳跃连接** 将第一个残差块的输入与最后一个残差块的输出相连, 以保留图像细节。

### 训练方式 (3.7, 据原文后续页, 提取缓存未覆盖, 待核)
提取文本止于 3.4, 未覆盖 3.7 训练细节。原笔记称损失为 L1, 但提取文本未提及损失公式; 此处不予断言 (PDF 提取文本未明确, 损失函数/优化器/学习率均待查原文)。

### 和已有方法的差异
- **本质区别**: 已有去噪 CNN (如 DnCNN [36]) 的所有操作 (卷积、激活、归一化) 都在实数域; CDNet 的关键运算均定义在复数域。
- **动机差异**: 实数 CNN 主要从数据驱动角度设计; CDNet 的动机部分来自复数变换在图像处理中的传统优势与生物视觉启发 (相位的重要性)。
- **优势侧重**: 本文特别论证复数 CNN 在**训练-测试噪声模型不一致时的鲁棒性**优势, 是对实数 CNN 的补充。

## 实验

**说明**: PDF 提取缓存仅覆盖前 12 页 (止于 3.4 节), 第 4 节实验的正文不在提取文本内。以下数据集与表格信息来自原笔记的"全文补读记录" (据 PDF p.13-32 缺失页线索, 提取缓存未覆盖, 待核)。
- **使用的数据集**: 据缺失页线索, 测试集为两个广泛使用的基准数据集 **Set12 与 BSD68** (p.15: "two widely-used benchmark datasets"; p.16-17 表 1-4 标题明确为 Set12 和 BSD68)。模型规模设置为"与标准基准方法规模相近" (p.15)。
- **评价指标**: **PSNR (dB)** 与 **SSIM** (p.15 明确; 表 1/2 给 PSNR, 表 3/4 给 SSIM)。
- **任务设置**: 据 p.14-15 线索, 论文在多种设置下评估 CDNet, 包括 4.1 节"非盲去除 AWGN (non-blind removal of AWGN)"。
- **主实验结论**: 在训练样本噪声模型与测试图像完全匹配时, 所提复数值 CNN 与最先进实数值去噪 CNN **具有竞争力 (performs competitively)** (摘要与贡献处定性声明; p.16 摘录"our CDNet performs..." 印证)。
- **消融实验**: 论文比较了 CReLU / ModReLU / zReLU 三种激活, 表明在相位上做非线性的 **CReLU 效果更好** (作者在 3.3 节预告"将在实验中表明")。
- **泛化/鲁棒性实验 (核心亮点)**: 重点展示噪声模型不一致场景下的优势——(1) 测试图像噪声水平未知; (2) 噪声标准差在像素间变化 (空间变化噪声); (3) 噪声为多种类型混合。这三种设置与摘要、贡献中的鲁棒性主张对应。
- **效率信息**: 提取文本未给出运行时间/FLOPs。论文从设计层面指出 1D 张量积分解使参数量从 DL² 降到 2DL, 暗示潜在效率优势, 但缺乏直接量化对比。

## 局限

1.  **计算实现开销**: 每个复数卷积需四个实卷积实现 (公式 8), 尽管 1D 分解降低了参数量, 实际计算时间/内存仍可能高于等价实数网络; 提取文本未提供与实数方法的运行时间/FLOPs 对比。
2.  **噪声模型范围**: 提取覆盖部分与缺失页线索均围绕**加性高斯白噪声 (AWGN)** 及其混合/空间变化变体; 对真实传感器噪声、泊松噪声等更复杂模型的能力在可见文本中未验证。
3.  **复数表示的必要性存疑**: 论文自承实现"类似于双宽度 CNN", 复数卷积的额外收益主要来自实部-虚部交互。这种交互理论上可在实数网络中以额外连接实现, 复数表示相对精心设计的宽实数网络究竟有多大不可替代性, 需更细致的消融来厘清。
4.  **提取覆盖局限**: 本笔记顶层小节中实验数字部分依赖缺失页线索而非完整正文, 具体 PSNR/SSIM 数值、对比方法完整列表、训练超参数 (3.7) 与结论 (第 5 节) 均待核原文。

## 个人评论

1.  **开创了一个研究方向**: 论文清晰地把"复数值表示是图像处理传统工具"这一既有事实, 延伸为"复数值也可作为深度网络中的有效内部表示", 为底层视觉网络设计提供了新视角。动机链条 (傅里叶/Gabor 相位 → 生物视觉复杂细胞 → 复数 NN) 讲得很完整, 是写研究动机的范本。
2.  **动机驱动的模块设计**: 它没有把实数网络机械替换为复数版本, 而是分别为卷积 (张量积紧凑性/避免过拟合)、激活 (相位非线性)、残差 (噪声鲁棒记忆) 三个环节各自找到一条数学/生物学依据。这种"每个模块都有出处"的设计思路比单纯堆 trick 更有说服力。
3.  **价值在鲁棒性而非 SOTA 刷点**: 匹配条件下只是"competitive"而非大幅领先, 论文把卖点放在训练-测试噪声不一致下的稳健性。这其实是更贴近真实部署的评估维度, 也提醒读者评测时别只看理想条件下的 PSNR。
4.  **可深挖的反问**: 论文自己点出"类似双宽度 CNN", 那么复数表示相对一个加了实部-虚部交叉连接的实数双分支网络, 增益究竟有多少, 是这条线最值得后续工作补做的对照实验。

### 使用建议

- **快速了解**: 读摘要、1.1 (动机)、1.2 (复数表示优点)、1.3 (贡献), 配合图 1 (Gabor 张量积)、图 2 (CReLU 相位激活)、图 3 (CDNet 框架)。
- **复现**: 精读第 3 节全部细节, 重点 3.2 (复数卷积及梯度公式 8-12)、3.3 (CReLU 与 ModReLU/zReLU 对比公式 15-18)、3.4 (复数 BN)、3.5 (复数残差块)、3.6 (合并层=取幅度) 与 3.7 (训练)。已知关键超参: L=3, 64 通道, 24 卷积单元 (9 残差块), 步长 2 下/上采样, 跳跃连接。训练优化器/学习率/迭代次数需查原文 3.7。
- **借鉴创新点**: 学习如何从数学特性 (张量积分解、相位操作) 出发设计模块; 借鉴构建鲁棒残差块的思路并迁移到超分/去模糊等任务。
- **写 related work**: 可归入 (1) 基于深度学习的图像去噪 (BM3D/WNNM/TWSC 等非局部法、EPLL 等先验学习法、DnCNN 系列); (2) 复数值神经网络及其应用; (3) 提升深度模型鲁棒性的方法。

## 相关论文与链接

> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**计算机视觉/底层视觉 (low-level vision)** 中的**图像去噪**方向, 核心是首次将**复数值深度卷积神经网络 (Complex-Valued Deep CNN)** 系统地引入图像去噪。它要解决的实际痛点是: 当训练样本与测试图像的噪声模型不一致时, 现有实数值去噪 CNN 鲁棒性不足。适合放在"图像复原/底层视觉"与"非实数域 (复数) 网络架构创新"的交叉主题下。

## 2. 一句话总结
本文首次系统研究并构建了用于图像去噪的复数值深度 CNN (CDNet), 通过复数值卷积 (1D 张量积紧凑表示)、相位非线性激活 (CReLU) 和噪声鲁棒的复数残差块, 在噪声匹配时与 SOTA 实数 CNN 竞争力相当, 在噪声模型不一致时鲁棒性更优。

## 3. 背景与问题
- **为什么要做**: 图像去噪既有实用价值 (移动摄影), 又是大多数图像复原任务的关键模块。深度学习去噪近年发展迅猛, 但**几乎全部基于实数值 CNN**。与此同时, 离散傅里叶、Gabor、双树复小波等复数值变换在图像处理中广泛使用, 且与生物视觉 (V1/V4 复杂细胞、相位主导感知) 深刻关联; 复数值 NN 在图像复原中的潜力却是空白。
- **之前方法的问题**: 实数 CNN 性能强依赖训练样本对测试数据在图像内容与噪声特性上的匹配。噪声分布复杂或空间变化时, 干净图充足而带噪样本不足, 泛化困难。
- **核心矛盾**: 如何用复数值表示的数学优势 (滤波器更紧凑、相位可非线性处理、残差块更鲁棒) 提升去噪性能, 尤其是训练-测试噪声不一致下的鲁棒性。

## 4. 核心贡献
1.  **首个复数值 CNN 去噪工作**: 打破图像复原网络仅用实数 CNN 的局面, 证明复数 CNN 对去噪有其优势。
2.  **复数值基本运算的新设计**: (i) 1D 复数滤波器张量积给出 2D 不可分滤波器的紧凑表示 (4L 自由度生成两个 R^{L×L} 滤波器, 实数需 2L²; 1D 分解使参数 DL²→2DL), 抑制过拟合; (ii) 相位非线性激活 CReLU 提升去噪; (iii) 噪声鲁棒的复数残差块。
3.  **实用网络 CDNet**: 噪声匹配时与 SOTA 实数 CNN 竞争力相当; 噪声不一致 (未知水平/空间变化/混合噪声) 时鲁棒性更优。

## 5. 方法详解
### 整体框架
CDNet 映射 Y∈R^{M1×M2}→X∈R^{M1×M2} (公式 4)。24 个顺序卷积单元 (图 3); 除首单元外每单元 = 复数卷积 + 复数 BN + 复数 ReLU; **所有卷积层 64 核**; 中部 18 单元 = 9 个复数残差块。首残差块前/末残差块后各用一个步长 2 的复数卷积/反卷积做下/上采样以扩大感受野; 末端合并层把复数特征转为实数图; 跳跃连接连首残差块输入与末残差块输出以保细节。五类基本块: 复数卷积层、复数 ReLU、复数 BN、复数残差块、合并层。

### 复数值卷积层 (3.2)
- 核 K_i∈C^{L×L×D1}, **L=3**; 前向公式 (6), 输出复数特征立方体 (公式 5)。
- 紧凑性 (公式 2): 两 1D 复数滤波器张量积关于实/虚部不可分, 模拟不同方向 2D 不可分滤波器 (图 1, 1D Gabor)。**4L 自由度生成两个 R^{L×L} 的 2D 滤波器, 实数需 2L²**, 故更紧凑、抗过拟合。
- 1D 分解 (公式 7): 残差块内 2D 卷积 = 两个连续 1D 卷积 (k1∈C^{L×1×D}, k2∈C^{1×L×D}), 参数 **DL²→2DL**。
- 四实卷积实现 (公式 8): 用现有实数框架; "类似双宽度 CNN", 但复数引入实部-虚部额外交互, 实数网络不会自发建立此连接。
- 反传 (公式 10-12): 复分析链式法则, ∂f/∂K=(∂f/∂B)∗A, 实/虚部各由四实卷积组合。

### CReLU (3.3)
CReLU(z)=ReLU(ℜz)+i·ReLU(ℑz) (公式 15): 实/虚部各做 ReLU; 幅度上同实 ReLU, 相位上有 4 种激活模式 (图 2: z=0/ℜz/ℑz/z), 实现相位域复杂非线性。对比: **ModReLU** (公式 16, 原文误拼 MoeReLU, 可训练偏置 b, 保相位) 与 **zReLU** (公式 17-18, 仅相位∈[0,π/2] 即实虚部皆正时激活)。作者预告实验中 CReLU 优于二者。

### 复数 BN (3.4)
改善泛化与收敛 (公式 19); 提取文本在此截断, 据缺失页线索为"分别对实/虚部做 batch normalization" (据原文后续页, 提取缓存未覆盖, 待核)。

### 复数残差块 (3.5) / 合并层 (3.6) / 训练 (3.7) — 据原文后续页, 提取缓存未覆盖, 待核
残差块借 [6] 复数联想记忆的噪声鲁棒检索性质 (残差块结构与记忆单元相似), 推断对噪声不一致更鲁棒 (图 4)。合并层据缺失页摘录"只取复数特征的幅度"转实数图。训练细节 (损失/优化器/超参) 提取文本未覆盖, 原笔记的"L1 损失"无提取文本支撑, 此处不予断言。

## 6. 实验与结果
**说明**: 提取缓存止于 3.4 节, 第 4 节实验正文不在提取文本内; 以下据缺失页线索 (据原文后续页, 提取缓存未覆盖, 待核)。
- **数据集**: 测试用 **Set12 与 BSD68** 两个常用基准 (p.15-17 线索), 模型规模设为与标准基准方法相近。
- **指标**: **PSNR(dB)** 与 **SSIM** (表 1/2 给 PSNR, 表 3/4 给 SSIM)。
- **设置**: 含 4.1 节非盲 AWGN 去除等多种设置。
- **主结论**: 噪声匹配时与 SOTA 实数去噪 CNN **竞争力相当 (competitively)**。
- **消融**: CReLU vs ModReLU vs zReLU, **CReLU 更优** (3.3 节预告)。
- **鲁棒性 (核心亮点)**: 噪声水平未知 / 空间变化噪声 / 混合噪声三种不一致场景下优于对比方法。
- **效率**: 无运行时间/FLOPs 直接对比; 1D 分解 (DL²→2DL) 暗示参数效率优势。

## 7. 这篇论文真正有价值的地方
1.  **开了一个方向**: 把复数表示从"图像处理传统工具"推进到"深度网络内部表示", 为底层视觉网络设计提供新思路。
2.  **动机驱动的系统性模块创新**: 卷积 (紧凑性/抗过拟合)、激活 (相位非线性)、残差 (噪声鲁棒记忆) 三处各有数学/生物学依据, 而非机械复数化。
3.  **关注鲁棒性而非绝对 SOTA**: 匹配条件下"相当", 价值在非理想/不匹配条件下的稳健性, 更贴近真实部署评估。
4.  **理论-实践闭环**: 从复数变换数学性质、生物视觉启示, 到网络实现与实验验证, 故事完整, 是写动机的范本。

## 8. 局限与问题
1.  **实现开销**: 每个复数卷积需四个实卷积 (公式 8), 1D 分解虽减参数, 实际时间/内存仍可能偏高; 无运行时间/FLOPs 对比。
2.  **噪声范围**: 围绕 AWGN 及其混合/空间变化变体; 真实传感器噪声、泊松噪声等在可见文本中未验证。
3.  **复数表示必要性**: 自承"类似双宽度 CNN", 收益主要来自实-虚部交互, 而该交互理论上可在实数网络以额外连接实现; 相对精心设计的宽实数网络的不可替代性需更细致消融。
4.  **覆盖局限**: 实验数字依赖缺失页线索, 具体 PSNR/SSIM、对比方法全列表、训练超参与结论待核原文。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 1.1/1.2/1.3 + 图 1/2/3。
- **复现**: 精读第 3 节, 重点 3.2 (卷积+梯度 8-12)、3.3 (CReLU 与对比 15-18)、3.4 (复数 BN)、3.5 (残差块)、3.6 (合并层=取幅度)、3.7 (训练)。已知超参: L=3, 64 通道, 24 单元/9 残差块, 步长 2 下上采样, 跳跃连接; 优化器/学习率待查 3.7。
- **借鉴创新点**: 从数学特性 (张量积分解、相位操作) 出发设计模块; 把复数/代数结构引入超分、去模糊等任务的鲁棒残差块设计。
- **写 related work**: (1) 深度学习去噪 (BM3D/WNNM/TWSC、EPLL、DnCNN 系列); (2) 复数值神经网络及应用; (3) 模型鲁棒性方法。

## 10. 和其他论文的关系
- **复数值 NN 基础**: 关联讨论复数 NN 表示能力 [3]、易优化 [4]、泛化 [5]、噪声鲁棒记忆 [6] 的工作; 以及可学习复数 CNN 构建技术 [3, 12]、scale/rotation 不变复数 CNN [43, 44, 45] (这些均面向识别任务)。
- **经典去噪 CNN**: 与 **DnCNN** [36] 等奠基性实数去噪 CNN 形成直接对比与延伸 (DnCNN 学噪声残差, 已成 CNN 去噪基准); [37] 处理空间变化噪声; [38] 用 GAN 合成噪声样本; [39] 插入非局部滤波层。
- **传统/非局部去噪**: BM3D [20]、WNNM [24]、TWSC [25]、EPLL [28]、稀疏/字典 [15-19] 等。
- **复数图像复原**: 与傅里叶、Gabor、双树复小波等复数域变换的传统图像复原方法关联。

## 11. 关键词
复数值卷积神经网络, 图像去噪, CDNet, 复数值运算, CReLU 相位激活, 张量积紧凑卷积, 1D 因子分解卷积, 复数残差块, 噪声鲁棒性, 底层视觉, 生物视觉/复杂细胞启发, 相位

## 12. 可信度说明
本篇精读笔记的**顶层小节与精读块 1-5 节主要基于 PDF 提取文本的前 12 页** (摘要、引言 1.1-1.4 动机/复数优点/贡献、第 2 节相关工作、第 3 节 3.1-3.4 框架/复数卷积/CReLU/复数 BN 开头), 这部分信息清晰、有公式与具体数量关系 (L=3、64 通道、4L vs 2L²、DL²→2DL、24 单元/9 残差块), 可信度高。
**主要缺失部分**: 提取缓存在 3.4 节公式 19 后截断, 因此**复数残差块 (3.5)、合并层 (3.6)、训练 (3.7) 与第 4 节实验的正文不在提取文本内**。笔记中关于数据集 (Set12/BSD68)、PSNR/SSIM、消融与鲁棒性实验的描述, 来自原笔记"全文补读记录"中 p.13-32 的缺失页线索/摘录, 已统一标注"据原文后续页, 提取缓存未覆盖, 待核"; 具体实验数值与训练超参仍需查阅完整论文。原笔记中"损失为 L1"的说法在提取文本无支撑, 已在方法节改为不予断言。

---

> **可信度补充**: PDF 提取质量 = **high** (前 12 页提取清晰, 约 1952 字符/页), 但提取缓存仅覆盖 12/32 页 (止于 3.4 节公式 19), 第 4 节实验正文未进入提取文本; 实验相关内容来自原笔记全文补读的缺失页线索, 待核原文。来源缓存: `.paper-cache/extracts/21-pr-Image Denoising Using Complex-Valued Deep CNN.txt`; 全文补读覆盖标注 32/32 页 (原 AI 主体 12/32 + 补读 13-32); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-32; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-32。
- **提取情况**: 缺失页 20 页, 其中 20 页提取到可读文本。缺失页包含正文/附录内容, 其中约 5 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Complex Conv
- p.13: Complex BN
- p.13: Complex ReLU
- p.13: We adapt batch normalization to the complex number field by separately running batch
- p.13: 3.5. Complex-valued residual block265
- p.13: 3.6. Merging layer
- p.13: The merging layer transforms the complex-valued feature maps into the output real-
- p.14: In other words, the conversion is done by only taking the amplitude of a complex-
- p.14: 3.7. Training285
- p.14: 4. Experiments
- p.14: We applied the CDNet to image denoising under different settings, including non-
- p.15: 4.1. Non-blind removal of AWGN

### 缺失页关键摘录

- p.13: Complex ReLU.Figure 4: Diagram of complex-valued residual block. Abbreviations: Conv for Convolution, RB for Residual
- p.13: blocks to the complex number field is straightforward. See Figure 4 for an illustration
- p.15: such that the resulting model has similar size with the standard benchmark methods,
- p.15: each noise level. For test, we select two widely-used benchmark datasets including
- p.15: noisy images. The peak signal-to-noise ratio (PSNR) and structural similarity (SSIM)
- p.16: Table 1 and Table 2 show the PSNR values of all the compared methods with dif-
- p.16: SSIM values are given in Table 3 and Table 4. It can be seen that our CDNet performs
- p.16: some denoising results in Figure 5 and Figure 6 for visual comparison.
- p.16: Table 1: Average PSNR(dB) of denoised images by different methods on Set12 in non-blind AWGN removal.
- p.17: Table 2: Average PSNR(dB) of denoised images by different methods on BSD68 in non-blind AWGN re-
- p.17: Table 3: Average SSIM of denoised images by different methods on Set12 in non-blind AWGN removal.
- p.17: Table 4: Average SSIM of denoised images by different methods on BSD68 in non-blind AWGN removal.
<!-- AI_READING_NOTE_END -->
