---
title: Xie B Xu Y Wang G C Yang S M and Li Y W. 2024. Adaptive decolorization method based on tSNE maximization. Journal of
authors:
  - "谢斌"
  - "徐燕"
  - "王冠超"
  - "杨舒敏"
  - "李燕伟"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.230392
pdf: [[cjig_图像处理_基于t-SNE最大化的彩色图像灰度化.pdf]]
primary_topic: T_图像处理_其他
topics:
  - "T_图像处理_其他"
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
extract_cache: .paper-cache/extracts/cjig_图像处理_基于t-SNE最大化的彩色图像灰度化.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/17 pages"
---
# Xie B Xu Y Wang G C Yang S M and Li Y W. 2024. Adaptive decolorization method based on tSNE maximization. Journal of

## 基本信息
- **PDF**: [[cjig_图像处理_基于t-SNE最大化的彩色图像灰度化.pdf]]
- **primary_topic**: `T_图像处理_其他`
- **topics**: `T_图像处理_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | t-SNE最大化的自适应彩色图像灰度化方法 (Adaptive decolorization method based on t-SNE maximization) |
| **作者** | 谢斌; 徐燕(通信); 王冠超; 杨舒敏; 李燕伟 (江西理工大学信息工程学院, 赣州 341000) |
| **发表时间** | 2024, 中国图象图形学报 29(08): 2333-2349 |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics) |
| **DOI** | 10.11834/jig.230392 |

## 摘要

**清理后的英文原摘要 (据 PDF 提取文本整理, 修复连字符与空格、剔除杂入的页脚/基金/图表数字):**

> **Objective** Image decolorization converts a color image into a grayscale one. It aims to maintain important features of the original color image as much as possible. It is normally used in the preprocessing stage of pattern recognition and image processing systems, such as extracting fingerprint features, face recognition, and medical imaging. Given that image decolorization maps color images in three dimensions into grayscale images in one dimension, it is a dimensionality reduction process essentially. Thus, the loss of information is inevitable. Accordingly, the major task for researchers can be expressed as preserving important features such as contrast, detail information, and hierarchy of the original color image as much as possible. Existing color-to-gray conversion methods generally fall into two main categories: local mapping methods and global mapping methods. Local mapping methods keep part of the structure and local contrast but tend to lose the overall information and may produce halo and noise enhancement; global mapping methods use one mapping function for the whole image, but many of them focus excessively on pixels with large amplitude values, which tend to produce visual overfitting and cause difficulty in retaining information in small-contrast areas. A novel image decolorization method is proposed, in combination with t-distributed stochastic neighbor embedding (t-SNE), to address the problems of insufficient contrast maintenance, blurred details, and lack of hierarchy. **Method** We introduce the idea of t-SNE dimensionality reduction into color-to-gray conversion and design a new model based on t-SNE maximization. The similarity between pixels in the original color image is represented by a joint Gaussian probability, while the similarity between pixels in the grayscale image is represented by a t-distribution joint probability; the energy function is maximized so that low-contrast areas of the original image can be appropriately enlarged or maintained after graying. An adaptive contrast-retention strategy defines a contrast-retention coefficient that adaptively adjusts the graying intensity of different regions based on color-contrast information. Because the maximization model is highly nonlinear (so gradient descent / iterative solvers are complex and slow), an efficient discrete search strategy turns the continuous parameter optimization into a discrete parameter-space search. **Result** On three datasets (Cadik, CSDD, Color 250), for the color contrast preserving ratio (CCPR) metric with contrast thresholds from 1 to 15, the average CCPR values of the proposed method are 0.874, 0.862, and 0.864, higher than the conventional methods; on the same hardware it has the shortest running time (real-time speed) on a 396×386 image; volunteer preference and accuracy experiments also favored the proposed results. **Conclusion** The proposed adaptive t-SNE-maximization decolorization method better maintains contrast, detail, and hierarchy, and performs better in both subjective and objective evaluations.

**中文翻译 / 原文中文摘要要点 (据 PDF 中文摘要整理):**

> **目的** 彩色图像灰度化是计算机视觉领域的研究热点。针对传统方法所得灰度图像存在对比度保持不足、细节模糊及层次感欠缺等问题，本文结合 t 分布随机邻域嵌入 (t-SNE) 提出一种更简单、高效的灰度化新方法。**方法** 首先将 t-SNE 降维思想引入灰度化过程，设计基于 t-SNE 最大化的新模型，通过最大化能量函数使原始彩色图像中对比度较小的区域在灰度化后对比度能适当变大或保持，让灰度图像更好地保持原图的对比度特征与层次感；其次设计一种自适应对比度保持策略，根据颜色对比度信息自适应调节不同区域的灰度化力度，更好地保留细节与对比度信息；最后采用一种高效的离散搜索方法快速求解所提模型。**结果** 在 Cadik、CSDD (complex scene decolorization dataset) 和 Color 250 数据集上的大量实验表明，本文方法在 CCPR 指标上的平均值在三个数据集上最高，分别为 0.874、0.862 和 0.864；相同硬件上运行时间最短。**结论** 相较传统方法，本文方法不仅能更好地保持原图的对比度、细节特征和层次感，在主客观评价上也均有更好表现。
>
> **关键词**: 彩色图像灰度化; t 分布随机邻域嵌入 (t-SNE); 对比度保持; 离散搜索; 细节保持

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：彩色图像灰度化常用于模式识别和图像处理系统的预处理阶段（提取指纹特征、人脸识别、医学成像等），在广告制作、文献印刷、目标跟踪和非真实感渲染中也有广泛应用。其本质是把三维空间的彩色图像映射为一维空间的灰度图像（Jin 和 Ng, 2015），降维过程不可避免地产生信息损失，因此如何较好地保留原图的对比度、细节信息和层次感是核心问题。
- **之前方法的问题**：论文将现有方法分为**局部映射**和**全局映射**两类，逐一点评：
    - **局部映射方法**：映射函数随空间位置变化，能保留部分结构与局部对比度，但容易丢失整体信息并产生光晕(halo)、噪声增强等问题。代表工作及其缺陷——Bala 和 Eschbach(2004) 将色度高频信息加入亮度通道，颜色丰富时易细节丢失与伪影；Neumann 等(2007) 假设颜色与亮度对比度梯度相同后二维积分，计算复杂度高且会出现"同色异灰"；Smith 等(2008) 基于 H-K 效应+多尺度非锐化掩蔽，易产生伪影；Ancuti 等(2010) 在其上加多尺度对比度约束有所改善，但 H-K 效应被证明不完全符合颜色顺序保留原则(Lu 等, 2012a)；Ancuti 等(2011) 基于显著性融合亮度与色度，但忽略非显著区域，常致视觉对比度不足；Zhou 等(2014) 用视觉对比度模型求显著性后最小化显著度差异，需先分割区域、复杂度高。
    - **全局映射方法**：整幅图用同一映射函数，灰度值只与颜色有关。Gooch 等(2005) 用 L2 范数构造最小二乘目标函数，效率低且复杂结构下效果欠佳；Kim 等(2009) 引入三角多项式做快速非线性映射，但严格定义颜色顺序，难以有效保持对比度；Lu 等(2012a) 基于双峰高斯模型用九色基线性加权，弱化颜色顺序约束但数值求解复杂、耗时；Lu 等(2012b) 将九色基简化为三色基并用离散搜索加速，但双峰高斯目标函数高度非线性只能求近似解，且**过分关注幅值较大的像素点，易产生视觉过拟合**；Liu 等(2015) 基于梯度相关相似性测度从离散候选中选最大梯度相关值的图像，但不同通道细节各异易致边缘模糊、对比度缺失；Yu 等(2021) 用拉普拉斯分布与归一化 L1 范数度量通道与灰度对比度距离，但拉普拉斯拟合在零轴附近误差较大，难以保持较小的对比度特征。
- **核心矛盾**：在信息不可避免损失的降维过程中，如何设计一种既简单高效、又能自适应平衡和保持图像中大小不同对比度区域特征的灰度化模型。论文受 Liu 等(2017a) 启发——"灰度化时若过分惩罚幅值较大像素而忽略较小像素则易产生过拟合视觉效果"，主张让小对比度区域灰度化后对比度适当变大、大对比度区域适当变小但仍保持显著视觉差异。

## 关键贡献

1.  **提出基于 t-SNE 最大化的灰度化新模型 (MAX-tSNE)**：将 t-SNE 降维思想引入彩色图像灰度化。论文先按 t-SNE 标准目标推出一个**最小化**能量函数 (式7, 记作 MIN-tSNE)，并通过图1说明直接最小化会丢失细节；继而提出**最大化** `A(δ_mn)·log(p_mn/q_mn)` 之和的新能量函数 (式8)，使原图中对比度较小的区域在灰度化后对比度能适当变大或保持，从而更好地保留对比度层次。
2.  **设计自适应对比度保持策略**：在能量函数中引入由颜色对比度 `δ_mn` 决定的**自适应系数 `A(δ_mn) = exp(-α||δ_mn||²)`** (式9)，按区域颜色对比度大小自动调节灰度化力度：增强小对比度区域、对大对比度区域适度收敛但保持显著差异，从而更好保留细节。
3.  **采用高效离散搜索求解方法**：所提模型高度非线性，梯度下降/迭代法复杂耗时；论文将连续权重优化转化为在离散参数空间的搜索 (66 种组合)，快速求得灰度图像，大幅提升效率。
4.  **多数据集主客观验证**：在 Cadik、CSDD、Color 250 三个数据集上，用主观视觉比较和客观指标 (CCPR, E-score, C2G-SSIM) 评估，并辅以志愿者偏好/准确性实验，证明 MAX-tSNE 在对比度保持、细节保留与运算速度上优于 SVD、CorrC2G、PrD、Wang 等(2018)、Yu 等(2021) 等方法。

## 方法

**整体框架与输入输出**：
- **输入**：一幅 RGB 彩色图像 `I`，任意像素 `m` 的值为 `I_m = (I_R,m, I_G,m, I_B,m)^T`。
- **输出**：对应灰度图像 `g`，像素 `m` 的灰度值为 `g_m`。
- **核心思想**：把彩色图像 `I` 看作高维空间数据点集合、灰度图像 `g` 看作低维空间数据点集合，借 t-SNE 用概率分布刻画像素对相似性，并通过优化映射权重 `w` 让灰度图保持原图的相对对比度关系。

**关键模块与连接**：
1.  **MAX-tSNE 能量函数模型**：
    - **相似性表示** (与 t-SNE 一致)：
        - 彩色图像像素 `m, n` 的相似性 `p_mn` 由**高斯联合概率**表示 (式4)，依赖颜色对比度 `δ_mn = sqrt((I_R,m-I_R,n)² + (I_G,m-I_G,n)² + (I_B,m-I_B,n)²)` (式5)，含方差 `σ`。
        - 灰度图像像素 `m, n` 的相似性 `q_mn` 由 **t 分布联合概率**表示 (式6)，依赖灰度差 `g_m - g_n`。（注：t 分布拖尾比高斯更长，可缓解低维空间的"拥挤问题"。论文英文摘要在此处将 q 误写为 Gaussian，正文式(6) 明确为 t 分布，应以公式为准。）
    - **从 MIN 到 MAX**：式(7) 是按 t-SNE 标准 KL 散度推出的**最小化**能量函数 (MIN-tSNE)；图1 显示直接最小化会使落日余晖、红花绿草、花瓣花蕾等细节/对比度在灰度图中几乎丢失。据此论文提出式(8) 的**最大化**能量函数 `max_g E = Σ_{(m,n)∈U} A(δ_mn) log(p_mn/q_mn)`，其中 `U` 是包含局部与非局部候选集的像素对集合。**直观解释**：最大化该式使原图中对比度较小的区域在灰度化后对比度被适当拉大、对比度较大的区域适当缩小但仍显著，从而避免对幅值大的像素过拟合、兼顾小对比度细节。（原笔记"让 q 尽可能不同于 p"的表述不准确，已据正文修正为上述机制。）
    - **映射函数**：`g = Σ_c w_c I_c`，约束 `Σ_c w_c = 1`、`w_c ≥ 0`，`c ∈ {R, G, B}`。

2.  **自适应对比度保持系数 `A(δ_mn)`** (2.2 节, 式9)：
    - **定义**：`A(δ_mn) = exp(-α||δ_mn||²)`，`α > 0` 为调节参数，是颜色对比度 `δ_mn` 的函数。
    - **作用机制**：`A(δ_mn)` 乘在 `log(p_mn/q_mn)` 前面。
        - 颜色对比度 `δ_mn` **小**（细节区域）→ `A(δ_mn)` **大** → `log(p_mn/q_mn)` 变化的"动能"较大 → 灰度对比度 `g_m - g_n` 的变化力度加大 → 更好保持细节。
        - 颜色对比度 `δ_mn` **大**（显著区域）→ `A(δ_mn)` **小** → 变化力度适当减小；但该区域原本对比度大，灰度图中仍能保持较显著的视觉对比度。
    - **图2 验证**：`A(δ_mn)=1` (无自适应) 时，球体颜色差异丢失、有明显伪影、绿白对比度不足；改用 `A(δ_mn)=exp(-α||δ_mn||²)` 后这些问题显著改善。

3.  **离散搜索求解器** (2.3 节, 图3)：
    - **流程**：在 [0,1] 内以步长 0.1 把 `w_R, w_G, w_B` 各分 10 等份 (每个权重 11 个取值)，在和为 1 的约束下得到 **66 种**权重组合；逐一代入映射函数得 66 个候选灰度图，再代入能量函数，取使能量函数**最大**的候选图为最终结果，对应 `(w_R, w_G, w_B)` 即最优权重。
    - **效率优化**：考虑图像冗余，将高分辨率原图下采样至 **64×64** 像素以加速；式(8) 中获取**局部候选集**时再下采样至 **32×32** 像素。

**数学/机制直观解释**：本方法是一个**带自适应感知权重的、基于概率分布关系的优化过程**。它不追求灰度图与彩色图像素级梯度绝对匹配，而是借 t-SNE 的高斯/t 分布相似性形式，最大化加权能量函数以拉开小对比度区域、保留大对比度区域，并由 `A(δ_mn)` 赋予小差异区域更高优化优先级。

## 实验

- **使用的数据集**：
    1.  **Cadik** (Ĉadík, 2008)：彩色图像灰度化经典数据集之一，颜色数量较少、结构相对简单。
    2.  **CSDD** (complex scene decolorization dataset, Du 等 2015)：颜色丰富、结构复杂的场景数据集。
    3.  **Color 250** (Lu 等, 2014)：包含 250 幅图像 (自然图像、合成图像、数字图表、地图等) 的大数据集。
- **对比方法**：SVD (Sowmya 等, 2017)、CorrC2G (Nafchi 等, 2017)、PrD (Xiong 等, 2018)、Wang 等(2018)、Yu 等(2021)。
- **实现环境**：MATLAB R2021a；Intel(R) Core(TM) i5-1135G7、2.4 GHz 主频、Windows10。参数 `α=3.6`、`σ=0.3` (一般设置, 详见 3.5 节参数敏感度分析)。
- **评价指标**：
    1.  **颜色对比度保持率 (CCPR)** (Lu 等, 2012a)：当两像素颜色对比度 `δ` 小于阈值 `τ` 时人眼几乎察觉不出差异；CCPR (式10) 是原图中 `δ_{x,y}≥τ` 的像素对里、灰度化后人眼仍可感知差异的比例。取值 0~1，**越接近 1 越好**。
    2.  **E-score** (Lu 等, 2014, 式11)：`E-score = 2·CCPR·CCFR/(CCPR+CCFR)`，其中 CCFR 为颜色对比度保真率 (式12)，衡量灰度图中不必要伪影的情况。综合 CCPR 与 CCFR，更符合人眼感知，**越接近 1 越好**。
    3.  **C2G-SSIM** (Ma 等, 2015)：color-to-gray 结构相似性。（具体数值结果在提取缓存未覆盖的页 p.13 Fig.9, 据原文后续页, 待核。）
- **主实验结果**：
    - **CCPR (表1-表3, τ=1~15)**：MAX-tSNE 的 CCPR 值普遍高于其他 5 种方法，**平均 CCPR 最高**——Cadik **0.874**、CSDD **0.862**、Color 250 **0.864**。对照次优方法 Yu 等(2021) 的平均值 (Cadik 0.869、CSDD 0.860、Color 250 0.859)，本文均略高。图7 给出 τ=1~40 的 CCPR 曲线，本文方法整体高于其他 5 种，且随 τ 增大优势愈发明显。
    - **E-score (图8, τ=1~40)**：MAX-tSNE 在三个数据集上的 E-score 曲线均高于其他方法，在 Cadik 和 Color 250 上尤为明显，说明其在对比度保持与内容保真方面更优。
    - **主观评价 (图4-6)**：在 Cadik/CSDD/Color 250 大量示例上，本文方法在保持颜色顺序、区域对比度、细节纹理 (蓝绿区分、红绿叶差异、芒果/梨、青提表面、蝴蝶翅膀红色渐变、条形图/扇形图配色等) 方面通常优于 SVD、CorrC2G、PrD、Wang 等(2018)、Yu 等(2021)。
    - **志愿者实验**：随机邀请志愿者完成偏好实验 (preference) 和准确性实验 (accuracy)，结果显示志愿者更偏好本文方法所得灰度图，表明其更符合人眼视觉感知。
- **运行效率**：相同硬件上处理 **396×386** 像素图像时，本文方法运行时间最短，达到实时速度。（不同方法运行时间对比见 Table 4, 位于提取缓存未覆盖的 p.15，据原文后续页, 待核。）
- **消融/参数实验**：图2 为 `A(δ_mn)` 取不同值的对比 (无自适应 vs 自适应)，证明自适应系数的作用；`α`、`σ` 的参数敏感度分析在 3.5 节 (据原文后续页 Fig.11/Fig.12, 提取缓存未覆盖, 待核)。

## 局限

- **离散搜索的精度限制**：权重以 0.1 为步长、仅 66 种组合，可能无法找到全局最优，精度上存在理论天花板。
- **参数依赖**：模型需预设 `α=3.6`、`σ=0.3`，虽做了敏感度分析，但这些值是否对所有图像类型最优仍需验证。
- **计算效率的权衡**：虽相对最快，但仍需生成并评估 66 个候选图；为提速对原图下采样至 64×64 / 32×32，超高分辨率或对下采样敏感的细节场景下其代价与影响文中未深入展开。
- **数据集覆盖**：实验集中在三个特定数据集，虽具代表性，但未覆盖低光照、水下、医学影像等图像类型，泛化边界未知。
- **对极端情况的鲁棒性**：颜色极单一或对比度极复杂时自适应机制是否依然有效，文中未深入讨论。

## 个人评论

1.  **创新性的降维思想迁移**：把 t-SNE 从数据可视化迁移到图像灰度化，并将标准的"最小化 KL"改为"最大化加权能量"，这一反转是论文最有辨识度的点——本质上是把"忠实保留高维结构"重新诠释为"在一维灰度上主动拉开易丢失的小对比度"。这种"先按标准范式推出 MIN-tSNE、用反例(图1)证明其不足、再提出 MAX-tSNE"的论证链条值得借鉴。
2.  **优雅的自适应机制设计**：`A(δ_mn)=exp(-α||δ_mn||²)` 简洁有效，把全局优化转化为基于局部颜色对比度的加权优化，让模型自动聚焦细节区域。这种"以小放大、对大区域收敛"的思想，正好对症全局映射方法"过分关注大幅值像素导致过拟合"的通病。
3.  **工程与理论的良好结合**：面对高度非线性模型，作者不强求梯度下降，而用 66 组合的离散搜索 + 64×64/32×32 下采样，把方法拉到实时速度。这提醒：模型设计与高效求解同样重要，有时降维/离散化反而更实用。
4.  **可改进与启发**：
    - 离散步长 0.1 限制了精度，可考虑由粗到细的多级搜索或在 66 组合附近做局部细化。
    - 可探索把其他嵌入/降维算法 (如 UMAP) 引入灰度化或更广的图像处理任务。
    - "在能量/损失函数中引入任务感知、基于数据本身特性 (此处为颜色对比度) 的权重" 是提升模型关注重点的通用手段。
    - CCPR / E-score / C2G-SSIM 这套面向灰度化任务的指标体系，可直接复用于同类任务的严谨评估。

### 使用建议

- **快速了解**：读摘要、引言(0节)最后一段、方法 2.1 节 (式7→式8 的 MIN→MAX 转换及图1反例)、3.2 节客观结果与表1-3 平均 CCPR。
- **复现**：精读第2节，尤其式(4)-(9) 的定义与含义、离散搜索流程 (2.3 节 + 图3)；注意 `α=3.6`、`σ=0.3`，以及 64×64 (全局) / 32×32 (局部候选集) 的下采样策略与 66 种权重组合。
- **借鉴创新点**：
    - **思路借鉴**：如何把成熟算法 (t-SNE) 的核心思想跨领域迁移并重新形式化 (最小化↔最大化)。
    - **模块借鉴**：自适应系数 `A(δ_mn)` 如何按任务关键特征 (颜色对比度) 动态调整优化权重。
    - **写作借鉴**：清晰地阐述问题→逐一分析两类方法不足→提出并论证模型→主客观系统实验。
- **写 Related Work**：可关联 1) 基于全局优化的灰度化方法 (Gooch 2005、Lu 2012a/b)；2) 基于视觉感知/对比度保持的灰度化 (H-K 效应、显著性、Liu 2015/2017)；3) 利用机器学习/降维技术做图像处理的研究。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_图像处理_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**计算机视觉 / 图像处理**领域，具体方向是**图像增强**中的**彩色图像灰度化 (color-to-gray conversion / decolorization)**。它要解决传统灰度化方法把三维彩色映射为一维灰度时普遍存在的**对比度保持不足、细节模糊、层次感欠缺**问题。核心技术点是把降维算法 **t-SNE** 的相似性建模思想引入灰度化，并把标准的最小化目标反转为**最大化加权能量函数**。因此本笔记将主题归为 **`T_图像处理_其他`**（不属于分割/去噪等更具体的子类，是灰度化/对比度保持这一图像处理任务）。原归类 `R2_控制_生物启发_其他跨学科` 不贴切，已更正。

## 2. 一句话总结
本文提出 **MAX-tSNE** 自适应彩色图像灰度化方法：用 t-SNE 的高斯/t 分布相似性刻画彩色图(高维)与灰度图(低维)像素对关系，**最大化**一个由自适应对比度系数 `A(δ_mn)` 加权的能量函数，并以离散搜索 (66 组 RGB 权重) 高效求解，使灰度图更好地保持原图的对比度、细节与层次感。

## 3. 背景与问题
- **为什么要做**：灰度化是模式识别/图像处理系统的预处理 (指纹、人脸、医学成像) 及广告印刷、目标跟踪、非真实感渲染的常用步骤，本质是三维→一维降维 (Jin 和 Ng, 2015)，信息损失不可避免，保留对比度/细节/层次感是核心难题。
- **之前方法的两类缺陷**：
    - **局部映射**（Bala-Eschbach 2004、Neumann 2007、Smith 2008、Ancuti 2010/2011、Zhou 2014）：映射随空间位置变化，能保结构与局部对比度，但丢整体信息、易光晕/噪声增强；H-K 效应类被证不完全符合颜色顺序保留 (Lu 2012a)，显著性类忽略非显著区域致对比度不足，显著度类需先分割、复杂度高。
    - **全局映射**（Gooch 2005、Kim 2009、Lu 2012a/b、Liu 2015、Yu 2021）：整幅同一映射函数；L2 范数类效率低、复杂结构差，三角多项式类严格定义颜色顺序难保对比度，双峰高斯类求解复杂且**过分关注大幅值像素→视觉过拟合** (Liu 2015)，梯度相关类各通道细节不一致致边缘模糊，拉普拉斯-L1 类零轴附近误差大难保小对比度。
- **核心矛盾**：在不可避免的信息损失下，设计既简单高效、又能自适应平衡大小对比度区域的灰度化模型。论文受 Liu 等(2017a) 启发——好的灰度化应让小对比度区域灰度化后对比度适当变大、大对比度区域适当变小但仍显著。

## 4. 核心贡献
1.  **MAX-tSNE 新模型**：先按 t-SNE 标准推出最小化能量函数 (式7, MIN-tSNE)，用图1 证明直接最小化丢细节，再提出**最大化** `Σ A(δ_mn)·log(p_mn/q_mn)` 的能量函数 (式8)，使小对比度区域在灰度化后被适当放大、保留层次。
2.  **自适应对比度保持策略**：引入 `A(δ_mn)=exp(-α||δ_mn||²)` (式9)，按区域颜色对比度自动调节灰度化力度 (小对比度增强、大对比度收敛但保持显著)。
3.  **高效离散搜索求解**：把连续权重优化转为 66 种离散权重组合的搜索，避免高度非线性模型的梯度/迭代求解，速度快。
4.  **三数据集主客观验证**：Cadik/CSDD/Color 250 上用 CCPR、E-score、C2G-SSIM 及志愿者实验，优于 SVD/CorrC2G/PrD/Wang(2018)/Yu(2021)。

## 5. 方法详解
**输入输出**：输入 RGB 图 `I` (像素 `I_m=(I_R,m,I_G,m,I_B,m)^T`)，输出灰度图 `g` (像素 `g_m`)。把 `I` 看作高维点集、`g` 看作低维点集。

**模块一：MAX-tSNE 能量函数**
- 彩色相似性 `p_mn` = 高斯联合概率 (式4)，依赖颜色对比度 `δ_mn = sqrt(Σ_c (I_c,m - I_c,n)²)` (式5, 含方差 σ)。
- 灰度相似性 `q_mn` = t 分布联合概率 (式6)，依赖灰度差 `g_m - g_n`；t 分布长拖尾缓解低维"拥挤问题"。（英文摘要把 q 误写为 Gaussian；以正文式(6) 为准——q 是 t 分布。）
- 标准 t-SNE 给出最小化 KL 的式(7) (MIN-tSNE)；图1 显示直接最小化会丢落日余晖、红花绿草、花瓣花蕾等细节。论文改为最大化式(8)：`max_g E = Σ_{(m,n)∈U} A(δ_mn) log(p_mn/q_mn)`，`U` 含局部+非局部候选像素对集合。**机制**：最大化此式拉大小对比度区域、收敛大对比度区域(但保持显著)，从而既避免对大幅值像素过拟合、又保住细节。映射约束 `g=Σ_c w_c I_c`，`Σ w_c=1`，`w_c≥0`。

**模块二：自适应系数 `A(δ_mn)` (式9)**
- `A(δ_mn)=exp(-α||δ_mn||²)`，`α>0`。`δ_mn` 小→A 大→`log(p/q)` 变化动能大→灰度对比度变化力度大→保细节；`δ_mn` 大→A 小→力度减小，但原对比度大故灰度图仍显著。图2 (无自适应 vs 自适应) 验证：自适应后球体颜色差异、伪影、绿白对比度均改善。

**模块三：离散搜索求解 (图3)**
- `w_R,w_G,w_B` 在 [0,1] 以 0.1 步长各分 10 等份 (各 11 取值)，和为 1 约束下得 **66 种**组合；逐一映射得 66 个候选灰度图，代入能量函数取最大者为结果，对应权重即最优解。
- 提速：原图下采样至 **64×64**；获取局部候选集时再下采样至 **32×32**。

## 6. 实验与结果
- **数据集**：Cadik (Ĉadík 2008, 颜色少结构简单)、CSDD (Du 2015, 颜色丰富结构复杂)、Color 250 (Lu 2014, 250 幅含自然/合成/图表/地图)。
- **对比方法**：SVD(Sowmya 2017)、CorrC2G(Nafchi 2017)、PrD(Xiong 2018)、Wang(2018)、Yu(2021)。
- **环境/参数**：MATLAB R2021a，i5-1135G7 @2.4GHz，Windows10；`α=3.6`、`σ=0.3`。
- **指标**：CCPR (式10, 0~1 越大越好)、E-score (式11，=2·CCPR·CCFR/(CCPR+CCFR)，结合 CCFR 式12，越接近 1 越好)、C2G-SSIM (Ma 2015)。
- **CCPR (表1-3, τ=1~15)**：平均值最高——Cadik **0.874**、CSDD **0.862**、Color 250 **0.864**；次优 Yu(2021) 为 0.869/0.860/0.859。图7 (τ=1~40) 显示本文曲线整体最高，τ 越大优势越明显。
- **E-score (图8, τ=1~40)**：本文曲线在三数据集均最高，Cadik/Color 250 尤为明显。
- **主观 (图4-6)**：在颜色顺序、区域对比度、细节纹理上普遍优于对比方法。
- **志愿者实验**：偏好实验 + 准确性实验，志愿者更偏好本文结果，更合人眼感知。
- **效率**：396×386 图像上本文运行时间最短，实时速度 (各方法运行时间对比见 Table 4，p.15，提取缓存未覆盖，据原文后续页待核)。
- **C2G-SSIM 数值结果**：在 p.13 Fig.9，提取缓存未覆盖，据原文后续页待核。

## 7. 这篇论文真正有价值的地方
1.  **最小化→最大化的反转**：把 t-SNE "忠实保结构"的最小化目标，反转为"在一维灰度上主动拉开易丢失的小对比度"的最大化目标，并用 MIN-tSNE 反例 (图1) 论证其必要性——思路新颖且论证扎实。
2.  **自适应加权的对症设计**：`A(δ_mn)` 直接针对全局方法"过分关注大幅值像素→过拟合"的通病，用一个指数衰减系数把优化重心移向小对比度细节，简洁有效。
3.  **理论与工程结合**：高度非线性模型不强求梯度下降，而以 66 组合离散搜索 + 多级下采样达到实时速度，实用性强。
4.  **启发**：可探索 UMAP 等其他嵌入用于图像处理；在能量/损失中引入数据自身特性的任务感知权重是通用手段；CCPR/E-score/C2G-SSIM 指标体系可复用。

## 8. 局限与问题
- 离散步长 0.1、仅 66 组合，可能错过全局最优，精度有天花板 (可考虑由粗到细多级搜索)。
- 依赖预设 `α=3.6`、`σ=0.3`，对所有图像类型是否最优待验证。
- 仍需生成评估 66 个候选图并下采样 (64×64 / 32×32)，对超高分辨率或对下采样敏感的细节场景代价/影响未深入。
- 数据集未覆盖低光照、水下、医学影像等，泛化边界未知。
- 颜色极单一或对比度极复杂的极端情况鲁棒性未讨论。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要、引言最后一段、2.1 节 (式7→式8 + 图1)、3.2 节表1-3 平均 CCPR。
- **复现**：精读第2节，式(4)-(9) 与离散搜索 (2.3 节 + 图3)；注意 `α=3.6`、`σ=0.3`、64×64/32×32 下采样、66 组合。
- **借鉴**：t-SNE 跨领域迁移并反转目标的思路；`A(δ_mn)` 的任务感知加权设计；问题→现状不足→模型→主客观实验的写作结构。
- **写 Related Work**：关联全局优化灰度化 (Gooch/Lu)、视觉感知/对比度保持灰度化 (H-K/显著性/Liu)、降维技术用于图像处理三条线。

## 10. 和其他论文的关系
- 直接对比的灰度化方法：SVD (Sowmya 2017)、CorrC2G (Nafchi 2017)、PrD (Xiong 2018)、Wang 等(2018)、[[基于拉普拉斯分布和L1范数的彩色图像灰度化方法]] (Yu 等 2021)。
- 引言中讨论的相关工作：Gooch(2005) L2 范数全局法、Lu(2012a/b) 双峰高斯/离散搜索、[[基于梯度相关相似性测度的灰度化方法]] (Liu 等 2015)、Bala-Eschbach(2004)、Smith(2008)/Ancuti H-K 效应类。
- 理论基础：van der Maaten 和 Hinton (2008) 的 t-SNE 原始论文。
- 评价指标来源：CCPR (Lu 2012a)、E-score (Lu 2014)、C2G-SSIM (Ma 2015)。
（库内是否实际存在上述同名笔记需核实，链接仅为合理推断。）

## 11. 关键词
彩色图像灰度化 (color-to-gray conversion), t 分布随机邻域嵌入 (t-SNE), 对比度保持 (CCPR), 细节保持, 自适应对比度系数 A(δ_mn), 离散搜索, 能量函数最大化 (MAX-tSNE), 图像增强, 降维, E-score, C2G-SSIM

## 12. 可信度说明
本精读笔记主要基于 PDF 提取文本 (提取缓存 12/17 页, 覆盖摘要、引言、t-SNE 理论 (第1节)、方法 (第2节, 式1-9)、主观评价 (3.1) 与客观评价中 CCPR/E-score 定义及表1-3) 生成。所引方法描述、公式、实验设置与平均 CCPR 值 (0.874/0.862/0.864)、对比方法、硬件、参数 (α=3.6、σ=0.3)、下采样尺寸 (64×64/32×32)、66 种权重组合、志愿者实验等均能在提取文本中找到支撑。**提取缓存未覆盖**的内容已逐一标注"据原文后续页待核"：C2G-SSIM 数值 (p.13 Fig.9)、各方法运行时间表 (Table 4, p.15)、参数敏感度图 (Fig.11/Fig.12, p.14)。英文摘要将灰度相似性 q 误写为 Gaussian，已据正文式(6) 更正为 t 分布。原笔记"最大化让 q 不同于 p"的解释不准确，已据 2.1 节机制 (拉大小对比度、收敛大对比度) 修正。原分类 `R2_控制_生物启发_其他跨学科` 与论文实际主题不符，已更正为 `T_图像处理_其他`。

---

> **可信度补充**: PDF 提取质量 = **high** (提取缓存 12/17 页, 约 2074 字符/页, 覆盖核心方法与主结果); 来源缓存: `.paper-cache/extracts/cjig_图像处理_基于t-SNE最大化的彩色图像灰度化.txt` (12/17 页; 缺 p.13-17, 含 C2G-SSIM 数值/运行时间表/参数敏感度图/参考文献); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-17; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-17。
- **提取情况**: 缺失页 5 页, 其中 5 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 3.2.3 C2G-SSIM
- p.15: Table 4 Comparison of runtime of different methods
- p.15: CorrC 2G
- p.16: method for efficient contrast -preserving decolorization . Multimedia

### 缺失页关键摘录

- p.13: Fig.9 C2G-SSIM values of different grayscale methods
- p.13: Fig.8 E-score value curves of different grayscale methods based on three datasets
- p.13: （ （a） Cadik dataset ； （b） CSDD dataset ； （c） Color 250 dataset ）2345
- p.14: Fig.12 Comparison of CCPR values based on three datasets under different σ values
- p.14: （ （a） Cadik dataset ； （b） CSDD dataset ； （c） Color 250 dataset ）2346
- p.15: Ĉadík M . 2008 . Perceptual evaluation of color -to-grayscale image conver ­
- p.15: Table 4 Comparison of runtime of different methods
<!-- AI_READING_NOTE_END -->
