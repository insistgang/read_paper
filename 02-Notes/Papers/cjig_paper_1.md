---
title: Hu B Xie G Q Li L D Li J Yang J C Lu W and Gao X B. 2024. Progress of image retargeting quality evaluation a survey. Journal
authors:
  - "胡波"
  - "谢国庆"
  - "李雷达"
  - "李静"
  - "杨嘉琛"
  - "路文"
  - "高新波"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.220722
pdf: [[cjig_paper_1.pdf]]
primary_topic: R_综述_Survey
topics:
  - "R_综述_Survey"
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
extract_cache: .paper-cache/extracts/cjig_paper_1.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/23 pages"
---
# Hu B Xie G Q Li L D Li J Yang J C Lu W and Gao X B. 2024. Progress of image retargeting quality evaluation a survey. Journal

## 基本信息
- **PDF**: [[cjig_paper_1.pdf]]
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 图像重定向质量评价的研究进展 (Progress of image retargeting quality evaluation: a survey) |
| **作者** | 胡波; 谢国庆; 李雷达; 李静; 杨嘉琛; 路文; 高新波 |
| **发表时间** | 2024 年 1 月 |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics), 第 29 卷第 1 期, 0022-0044 |
| **DOI** | 10.11834/jig.220722 |
| **单位** | 重庆邮电大学图像认知重庆市重点实验室 / 广阳湾实验室重庆脑与智能科学中心 / 西安电子科技大学人工智能学院与电子工程学院 / 阿里巴巴集团 / 天津大学电气自动化与信息工程学院 |

## 摘要

**英文原摘要 (据提取文本清理, 修复空格与连字符):**

> With the popularization of the Internet, intelligent technology, and various sensing devices, images and videos are playing an increasingly important role in video surveillance, health care, and distance education. All kinds of information can be obtained through images or videos using different terminal devices (such as mobile phones, laptops, and tablets) anytime and anywhere. Because different terminal devices have dissimilar sizes and resolutions, how to display the same image with high visual quality on these devices has become a common concern of the academic and industrial community. To solve this problem, image retargeting technology has emerged and become a popular, cutting-edge research direction in the field of computer vision and image processing. Image retargeting technology aims to adjust the image resolution without destroying the visual content to adapt to the information acquisition of various terminals. According to different technologies, content-based image retargeting algorithms can be divided into four categories: discrete methods, continuous methods, multioperator methods, and deep learning methods. Although great progress has been made in this field, no algorithm can be guaranteed to meet the requirements of multiple display devices without reducing the visual quality. Distortions are inevitably introduced in image retargeting. Therefore, how to evaluate the quality of retargeted images objectively and accurately is very important for the selection, optimization, and development of image retargeting algorithms. Image quality assessment (IQA) is a basic problem in image processing and computer vision. In general, it can be divided into subjective assessment and objective assessment. According to whether a reference image is used or not, it can be further divided into full-reference, reduced-reference, and no-reference quality metrics. In recent years, a massive effort has been made in objective image retargeting quality assessment (IRQA); thus, encouraging research progress has been achieved. However, up to now, no review paper has studied image retargeting quality evaluation, which could hinder further development of this field. To this end, this review paper analyzes the challenges facing the field, reviews and summarizes the existing methods, examines their advantages and disadvantages, and states the possible development directions of the field. Two types of representative IRQA models, namely, the traditional feature similarity-based IRQA model and the image registration-based IRQA model, are introduced and summarized in detail. The performances of representative IRQA metrics are compared and analyzed on three public datasets in terms of prediction accuracy and monotonicity. Experimental results show the current models are only partially consistent with human perception and can still be improved. More energy and efforts are needed in this field.

**中文翻译/摘要 (据原文中文摘要整理):**

> 随着移动显示设备的普及, 人们可以使用不同的终端设备获取图像信息。为适配不同尺寸的设备, 图像重定向技术应运而生并成为研究热点。尽管该技术近年取得长足进步, 但没有算法能够保证在不降低视觉内容质量的前提下满足多种显示设备的要求 —— 重定向过程中不可避免地会引入失真, 降低用户视觉体验。因此如何客观、准确地评价重定向图像质量, 对重定向算法的选择、优化及发展至关重要。当前已有一系列 IRQA 研究但尚缺综述, 本文对该领域研究进展进行较为全面的回顾与总结: 先简单介绍图像重定向及传统图像质量评价; 再分别介绍 IRQA 的数据集和客观评价方法, 将现有客观方法分为**基于传统特征相似性**和**基于图像配准**两类并分析其优缺点; 接着在 3 个数据集上对代表性算法的性能进行对比分析; 最后总结领域面临的问题与挑战, 指明未来发展方向。
> 关键词: 图像质量评价 (IQA); 图像重定向; 图像配准; 内容损失; 几何失真

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 不同终端设备 (手机、平板、笔记本等) 尺寸与分辨率各异, 如何在这些设备上完整显示同一图像并保持较高视觉质量, 是学术界与工业界共同关心的问题。图像重定向 (image retargeting) 旨在尽量不破坏图像内容的前提下调整分辨率以适配多终端 (应用于图像摘要、图像合成、照片拼接、自动裁剪、缩略图/视频封面生成等)。但该过程不可避免引入失真 (如像素重复删除/添加导致锯齿边缘、伪影; 内容挤压扭曲导致拉伸或丢失), 降低观感。因此客观、准确地评价重定向图像质量, 对算法的选择、优化与发展具有重要指导意义。
- **之前方法的问题**: 传统 IQA 方法 (全参考 FR、半参考 RR、无参考 NR) 主要针对**相同分辨率**自然图像的常见失真 (模糊、压缩、噪声) 设计, 无法直接用于重定向图像。原因有二: (1) 重定向图像的失真是**算法失真**, 主要为内容失真与几何结构失真, 与传统模糊/噪声失真本质不同; (2) 参考图像与失真 (重定向) 图像**分辨率不一致**, 而 FR/RR 方法通常应用于同分辨率图像, 分辨率不匹配是又一限制因素。
- **核心矛盾**: 如何针对重定向图像特有的失真特性 (分辨率变化、几何结构扭曲、内容损失), 设计与人类视觉感知 (HVS) 高度一致的客观质量评价模型。
- **综述定位**: 王志明 (2015)、方玉明等 (2021)、鄢杰斌等 (2022)、程茹秋等 (2022) 等已发表多篇 IQA 综述, 但均未专门涉及 IRQA 领域。本文是 (据其自述) 首篇专门针对图像重定向质量评价的综述。

## 关键贡献

1. **首篇 IRQA 专门综述**: 据论文自述, 截至成文尚无专门针对图像重定向质量评价的综述, 本文填补该空白, 帮助研究者快速掌握领域基本情况。
2. **分类框架**: 将现有客观 IRQA 方法清晰划分为两大类 —— **基于传统特征相似性的方法**与**基于图像配准的方法**, 详细分析每类的基本思想、代表性工作、优点与缺点 (第 3 节, 优缺点汇总于 Table 3, 据原文 p.13, 提取缓存未覆盖)。同时对重定向算法本身也分了 4 类 (离散/连续/多算子/深度学习, Table 1)。
3. **数据集整理**: 总结 IRQA 领域 3 个基准主观数据集 (MIT RetargetMe、CUHK、NRID), 从原始图像数、重定向算子、缩放比例、主观评价方法等维度比较其构建方式 (Table 2)。
4. **性能对比分析**: 在 3 个公开数据集上, 从预测精度与单调性两个角度对代表性 IRQA 算法进行性能比较 (Table 4 MIT、Table 5 CUHK、Table 6 NRID, 据原文 p.16-17, 提取缓存未覆盖, 具体数值待核)。
5. **挑战与展望**: 总结当前问题与挑战 (现有模型仅与人类感知部分一致, 数据集规模小、内容不丰富、缩放比例固定), 指明未来研究方向。

## 方法

本文是综述, 未提出新方法。以下为其梳理的技术体系。

### 重定向算法分类 (第 1.1 节, Table 1)
内容感知重定向算法普遍采用**两阶段框架**: 第 1 阶段计算输入图像的重要性图 (为每个像素分配重要性权值, 权重越高越应保留); 第 2 阶段在满足几何约束下执行尺寸调整, 尽量保留重要内容。据不同技术分为 4 类:
- **离散方法**: 直接决定像素的保留/去除。又分基于简单裁剪 (Suh 2003、Chen 2003、Santella 2006) 与基于细缝裁剪 (seam carving, SC; Avidan & Shamir 2007 用梯度作能量+动态规划; Rubinstein 2008; Guo 2015) 及移位图 (Pritch 2009)。优势: 速度快、易实现、适用主体小/缩放比例小的图像; 劣势: 丢失部分信息、可能局部结构失真。
- **连续方法**: 设定约束能量项保留关键物体, 本质为非均匀缩放 (基于内容感知缩放: Shi 2008、Liang 2012、Du 2013; 基于 warping: Liu & Gleicher 2005、Wang 2008、Zhang 2009、Kim 2018 结构感知网格变形、Lau 2018 Beltrami 表示)。优势: 较好保留重要区域、适合复杂结构图像; 劣势: 计算复杂度较高、重要/背景边界易失真。
- **多算子方法**: 组合多种算子 (Fang 2017 组合 CR/WARP/SCL/SC; Wang 2016 组合 WARP/CR/SCL; Shafieyan 2017)。优势: 综合多算子、效果较好; 劣势: 计算复杂度高、效率低、依赖算子操作策略 (比例与顺序)。
- **深度学习方法**: 利用神经网络提取符合 HVS 的语义特征 (Cho 2017 首次用 DNN 生成重定向图像; Guo 2018b CNN+级联回归自动裁剪; Tan 2020 循环重定向网络, 无监督+循环感知一致性损失; Shocher 2019 InGAN; Ahmadi 2021; Naderi 2022 修复+超分+PSO 融合)。优势: 可拓展性好、视觉效果更符合 HVS; 劣势: 计算复杂度高、效率低、不适合实时、对硬件依赖高。

### 传统 IQA 体系 (第 1.2 节, 作为背景)
按是否需参考图像分为 FR-IQA / RR-IQA / NR-IQA 三类。FR-IQA 分手工特征 (SSIM 等 Wang 2004) 与深度学习; RR-IQA 分空域与变换域; NR-IQA 早期基于自然场景统计 NSS (BRISQUE、NIQE、BLIINDS、NFERM), 后期大量基于 CNN (Kang 2014 首次引入)。结论: FR/RR 因需同分辨率参考、NR 因主要面向模糊/噪声失真, 都难以直接用于重定向图像。

### IRQA 整体框架 (图 6)
输入**参考图像**与对应**重定向图像**, 输出预测**质量分数**, 整体流程为特征提取 → 特征比较/匹配 → 质量分数映射。两类模型:

**(a) 基于传统特征相似性的 IRQA 模型 (第 3.1 节):**
- **核心思想**: 分别从参考图像和重定向图像提取感知敏感特征 (梯度、颜色、结构等), 通过计算特征相似度/分布距离量化失真程度。
- **早期 6 种指标**: EH (edge histogram)、CL (color layout)、BDS (bidirectional similarity)、BDW (bidirectional warping)、EMD (earth-mover's distance)、SIFT-flow。其中 EH/CL 用低层特征视图像为整体; BDS/BDW 搜索中级语义对应; EMD/SIFT-flow 通过对齐图像捕捉结构特性, 比前 4 种更有效。Rubinstein (2010) 在 MIT RetargetMe 上评估 6 种指标, 发现与主观结果存在明显差异。
- **显著性加权**: 因人更关注显著区域, 显著区域失真对整体质量影响更大, 故引入**显著性图 (Saliency Map)** 加权 (Wei 2021 基于 EMD 的 RR-IRQA; Chen 2017a 从显著区域/伪影/全局结构/美学/对称性多方面描述特征并用 GRNN 建模、输出相对分数转全局排名; Chen 2017b 用 NSS+显著全局结构失真+双向显著信息损失; Liang 2017; Liu 2020 基于 Chen 2017a 的学习式方法)。
- **质量回归**: 常用支持向量回归 (SVR) 或通用回归神经网络 (GRNN, Specht 1991)。
- **不足 (原文明列 3 点)**: 1) 高度依赖手工设计特征的有效性; 2) 通常不符合 HVS 感知特性; 3) 部分方法性能受显著性算法性能制约。

**(b) 基于图像配准的 IRQA 模型 (第 3.2 节):**
- **核心思想**: 由于参考与重定向图像尺寸不同, 直接提特征效果受限。此类方法在特征提取前先做**稀疏或密集图像配准**, 建立两图对应关系再提特征评价。
- **代表工作**: Zhang & Kuo (2014) 先做特征点匹配, 再以全局结构失真、局部区域失真、显著信息损失为指导获取特征; Liu (2015) 在空域获取形状失真/局部与全局内容失真, 并考虑频域几何与内容失真, 最后用 SVR 回归。(Lin 等人的方法在提取文本 p.12 末被截断, 据原文后续页, 待核。)
- **与特征相似性类的差异**: 通过显式配准建立空间对应关系, 能更细致度量几何失真 (形状扭曲) 与内容失真 (丢失/重复)。
- **训练/推理**: 多为传统机器学习流程 (手工特征 + SVR/GRNN 回归)。

## 实验

- **数据集 (Table 2, 已据提取文本核实)**:
  - **MIT RetargetMe** (MIT, 2010): 80 幅原始图像 (主观实验选其中 37 幅), 8 种重定向算子 (CR、SCL、WARP、SC、SNS、MULTIOP、SM、SV), 缩放比例 0.5/0.75, 共 296 幅重定向图像; 主观评价采用**成对比较法** (用户选两幅中质量更好者, 由投票数决定质量)。
  - **CUHK** (香港中文大学, 2012): 57 幅原始图像, 10 种算子 (MIT 的 8 种 + SCSC + ENER) 中随机选 3 种生成, 缩放比例 0.5/0.75, 共 171 幅重定向图像; 采用**双刺激法** (论文表 2; 正文另述用 MOS 平均意见分数衡量, MOS 越大质量越好)。
  - **NRID** (NTHU retargeting image dataset, 2014): 35 幅原始图像, 5 种算子 (SC、SM、SCL、WARP、MULTIOP), 长或宽为原图的 0.75, 共 175 幅重定向图像; 主观评价与 MIT 一致, 采用**成对比较法**。
  - 3 个数据集均仅从水平或垂直一个方向压缩, 普遍存在规模小、内容不够丰富、缩放比例较固定的缺点。
- **评价指标**: 以主观分数 (成对比较投票数 / MOS) 为真值, 客观算法用**预测精度** (如 PLCC 皮尔逊线性相关系数) 与**单调性** (如 SRCC 斯皮尔曼秩相关系数) 衡量与主观感知的一致性。
- **对比方法**: 早期 6 指标 (EH、CL、BDS、BDW、EMD、SIFT-flow); 特征相似性类 (Ma 2016 GIST+排名、Chen 2017a GRNN、Chen 2017b、Liang 2017、Wei 2021、Liu 2020); 图像配准类 (Zhang & Kuo 2014、Liu 2015)。提取缓存末页 (p.16-17) 标题线索显示性能表还含 SIFT-flow、IR-SSIM、PGDIL、Karimi、RN-IRQA、INSEM、TRASIM 等方法名 (据原文后续页, 提取缓存未覆盖, 待核)。
- **主实验结果**: 性能对比表为 Table 4 (MIT RetargetMe)、Table 5 (CUHK)、Table 6 (NRID), 据原文 p.16-17, **提取缓存仅覆盖前 12 页, 具体 PLCC/SRCC 数值未覆盖, 待核**。论文摘要明确给出总体结论: "*实验结果表明当前模型仅与人类感知部分一致 (only partially consistent with human perception), 仍有改进空间, 该领域需要更多投入。*"
- **消融/泛化/效率**: 综述性质, 提取文本 (前 12 页) 中未含此类信息。

## 局限

1. **综述本身的局限**: 核心价值在总结而非创新, 不提出新评价模型。
2. **数据集局限 (原文明确指出)**: 3 个基准数据集规模小、图像内容不够丰富、缩放比例较为固定 (仅 0.5/0.75)、仅单方向压缩, 限制了对算法的全面、鲁棒评估。
3. **现有方法与 HVS 不完全一致**: 论文结论明确 "当前模型仅与人类感知部分一致", 大多数算法用回归方法获得分数, 与人眼感知过程一致性不高。
4. **本笔记的覆盖局限**: 提取缓存仅含 PDF 前 12 页 (止于第 3.2 节开头、Lin 等人方法被截断)。论文后续的两类方法优缺点汇总表 (Table 3, p.13)、深度学习 IRQA 方法详评、3 个数据集上的具体性能数值 (Table 4-6, p.16-17)、以及总结与展望部分的完整内容, **均据原文后续页, 提取缓存未覆盖, 待核**。

## 个人评论

1. **入门地图**: 对刚进入图像重定向或质量评价领域的研究者, 这篇综述提供清晰的"地图" —— 核心问题 (分辨率不匹配 + 特有失真)、关键资源 (三大数据集)、两大技术路径、现存瓶颈, 一文打通。其作为"首篇 IRQA 综述"的定位 (论文自述) 使它有较高的引用价值。
2. **分类清晰、优缺点明确**: 把纷杂方法归纳为特征相似性 vs 图像配准两大类, 并对重定向算法本身也做了 4 类划分, 优缺点对比 (Table 1/Table 3) 有助于研究者快速定位不同路径的理论基础与固有局限。值得注意的是, 论文对"为何配准能帮上忙"给出了清晰动因 (尺寸不匹配下显式建立空间对应), 这一思想对其他跨分辨率图像比较任务也有借鉴。
3. **指明方向**: 论文揭示的痛点 (数据集规模小且缩放比例固定、现有模型与 HVS 仅部分一致、深度学习在 IRQA 而非重定向中的应用仍不充分) 直接指向值得投入的研究方向。一个自然的延伸是: 将"图像配准"思想与深度特征提取器结合, 并设计更贴合 HVS 的损失/注意力机制。
4. **可改进之处 (评论方角度)**: 综述偏重传统与配准方法, 深度学习 IRQA 评价方法的覆盖相对单薄 (本提取文本范围内仅见重定向生成侧的深度方法, 评价侧着墨少); 三大数据集十余年未有大规模更新, 也是制约整个领域的结构性瓶颈。

### 使用建议

- **快速了解**: 读摘要、引言 (0)、相关工作 1.1/1.2、第 2 节数据集, 10-15 分钟掌握领域全貌、核心问题与关键文献。
- **复现**: 综述本身不含可复现算法, 应顺着它定位到具体方法原文 (如 Chen 2017a、Liu 2015、Zhang & Kuo 2014) 再精读。
- **借鉴创新**: 重点看第 3 节两类方法优缺点分析。可思考: 如何把图像配准与深度特征结合? 如何设计更符合 HVS 的损失/注意力来改进评价? 现有数据集缺点正是构建新数据集的动机。
- **写 Related Work**: 是撰写"图像质量评价/图像重定向"相关工作的素材库, 可按其分类框架引用关键文献。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页:
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇**综述论文 (Survey)**, 属于**图像质量评价 (Image Quality Assessment, IQA)** 方向, 聚焦其细分领域 **图像重定向质量评价 (Image Retargeting Quality Assessment, IRQA)**。发表于《中国图象图形学报》2024 年第 29 卷第 1 期 (0022-0044, DOI 10.11834/jig.220722), 由重庆邮电大学、西安电子科技大学、天津大学、阿里巴巴等单位合作完成, 通信作者高新波。论文系统回顾该领域研究进展: 背景 (图像重定向 + 传统 IQA)、基准数据集、客观评价方法两大分类及优缺点、性能比较, 并指出挑战与未来方向。在本知识库中归于 **R_综述_Survey** 主题最贴切。

## 2. 一句话总结
这篇综述系统梳理了图像重定向质量评价 (IRQA) 的研究进展, 重点介绍 3 个基准数据集 (MIT RetargetMe、CUHK、NRID) 和两类主流客观评价方法 (基于传统特征相似性 / 基于图像配准), 分析其优缺点, 并指出当前模型仅与人类感知部分一致、数据集规模偏小等挑战与未来方向。

## 3. 背景与问题
- **驱动力**: 终端设备尺寸/分辨率各异, 同图高质量显示成为学界工业界共同关切。图像重定向旨在不破坏内容前提下调整分辨率, 应用于图像摘要、合成、拼接、自动裁剪、缩略图/封面等场景。
- **失真根源**: 传统简单操作 (缩放、裁剪) 严重破坏显著区域; 内容感知算法虽改进, 但受限于图像处理技术与对 HVS 理解的不足, 仍不可避免引入**内容失真**与**几何结构失真** (锯齿边缘、伪影、过度拉伸、内容丢失)。
- **核心矛盾**: 传统 IQA (FR/RR/NR) 无法直接用于重定向图像 —— (1) 重定向失真是算法失真 (内容+几何), 不同于模糊/噪声; (2) 参考图与失真图**分辨率不一致**, FR/RR 要求同分辨率。故需针对重定向失真特性专门设计客观评价模型。
- **综述空白**: 既有 IQA 综述 (王志明 2015、方玉明 2021、鄢杰斌 2022、程茹秋 2022) 均未专门覆盖 IRQA, 本文填补此空白。

## 4. 核心贡献
1. 据论文自述, 首篇专门针对 IRQA 的综述, 帮助研究者快速掌握领域基本情况。
2. 提出客观 IRQA 方法的两类划分 (特征相似性 / 图像配准), 详析每类思想、代表作、优缺点 (Table 3, 据原文 p.13, 提取缓存未覆盖); 同时对重定向算法本身做 4 类划分 (离散/连续/多算子/深度学习, Table 1)。
3. 整理 3 个基准数据集 (MIT RetargetMe / CUHK / NRID), 多维比较构建方式 (Table 2)。
4. 在 3 个公开数据集上从预测精度与单调性比较代表性算法 (Table 4-6, 据原文 p.16-17, 提取缓存未覆盖)。
5. 总结挑战 (模型与 HVS 仅部分一致、数据集规模小且缩放比例固定) 并指明未来方向。

## 5. 方法详解
本文为综述, 无新方法; 梳理的技术体系如下。

**重定向算法 (1.1 节, 两阶段框架: 算重要性图 → 满足几何约束下调整尺寸), 4 类:**
- **离散** (简单裁剪 Suh/Chen/Santella; 细缝裁剪 SC: Avidan & Shamir 2007 梯度能量+动态规划, Rubinstein 2008, Guo 2015; 移位图 Pritch 2009)。优: 快、易实现; 劣: 丢信息、局部结构失真。
- **连续** (内容感知缩放 Shi 2008/Liang 2012/Du 2013; warping: Liu & Gleicher 2005、Wang 2008、Zhang 2009、Kim 2018、Lau 2018 Beltrami)。优: 保留重要区域; 劣: 复杂度较高、边界失真。
- **多算子** (Fang 2017 / Wang 2016 / Shafieyan 2017)。优: 效果较好; 劣: 复杂度高、依赖操作策略。
- **深度学习** (Cho 2017 首个 DNN 生成; Guo 2018b CNN+级联回归; Tan 2020 循环网络无监督; Shocher 2019 InGAN; Naderi 2022 修复+超分+PSO)。优: 可拓展、符合 HVS; 劣: 复杂度高、不适实时、依赖硬件。

**传统 IQA (1.2 节, 背景)**: FR (手工特征 SSIM/深度学习) / RR (空域/变换域) / NR (NSS: BRISQUE、NIQE、BLIINDS、NFERM; CNN: Kang 2014 起)。结论: FR/RR 需同分辨率参考、NR 主要面向模糊噪声, 均难直接用于重定向。

**IRQA 整体框架 (图 6)**: 输入参考图+重定向图 → 特征提取 → 比较/匹配 → 质量分数。
- **(a) 特征相似性类 (3.1)**: 提感知敏感特征 (梯度/颜色/结构) 算相似度。早期 6 指标 EH/CL/BDS/BDW/EMD/SIFT-flow (Rubinstein 2010 在 MIT 上评估发现与主观差异明显); 引入**显著性图**加权 (Chen 2017a 多维特征+GRNN→全局排名, Chen 2017b NSS+显著结构+双向信息损失, Liang 2017, Wei 2021 EMD-based RR, Liu 2020 学习式); 回归用 SVR/GRNN。**不足 (原文 3 点)**: 依赖手工特征、不符 HVS、受显著性算法性能制约。
- **(b) 图像配准类 (3.2)**: 先稀疏/密集配准建立对应关系再提特征。Zhang & Kuo 2014 (特征点匹配 + 全局/局部/显著信息损失); Liu 2015 (空域形状/内容失真 + 频域几何/内容失真 + SVR)。优势: 显式空间对应, 更细致度量几何与内容失真。(Lin 等方法在提取文本 p.12 末截断, 待核。)

## 6. 实验与结果
- **数据集 (Table 2, 已核实)**: MIT RetargetMe (2010, 80 原图/选 37, 8 算子 CR·SCL·WARP·SC·SNS·MULTIOP·SM·SV, 比例 0.5/0.75, 296 重定向图, 成对比较); CUHK (2012, 57 原图, 10 算子选 3, 比例 0.5/0.75, 171 图, 双刺激法/MOS); NRID (2014, 35 原图, 5 算子 SC·SM·SCL·WARP·MULTIOP, 比例 0.75, 175 图, 成对比较)。三者均单方向压缩, 规模偏小。
- **指标**: 主观分数 (投票/MOS) 为真值, 客观用预测精度 (PLCC) 与单调性 (SRCC) 衡量一致性。
- **对比方法**: 早期 6 指标 + 特征相似性类 (Ma 2016 GIST, Chen 2017a/b, Liang 2017, Wei 2021, Liu 2020) + 配准类 (Zhang & Kuo 2014, Liu 2015); p.16-17 表标题线索另含 IR-SSIM、PGDIL、RN-IRQA、INSEM、TRASIM 等 (据原文后续页, 提取缓存未覆盖, 待核)。
- **主结果**: Table 4 (MIT) / Table 5 (CUHK) / Table 6 (NRID), 据原文 p.16-17, **提取缓存仅前 12 页, 具体 PLCC/SRCC 数值未覆盖, 待核**。论文结论 (见摘要): 当前模型仅与人类感知部分一致, 仍有改进空间。
- **消融/效率**: 综述性质, 前 12 页未含。

## 7. 这篇论文真正有价值的地方
1. **领域地图**: 一文打通核心问题 (分辨率不匹配+特有失真)、关键资源 (三大数据集)、两条技术路径与瓶颈; 作为自述"首篇 IRQA 综述", 引用价值高。
2. **双层清晰分类**: 既对重定向算法分 4 类 (Table 1), 又对评价方法分 2 类 (Table 3), 优缺点对照便于定位。
3. **指向研究空白**: 数据集规模小/缩放比例固定、模型与 HVS 仅部分一致、深度学习 IRQA 评价方法仍不充分 —— 都是可投入方向。
4. **配准思想的可迁移性**: 显式建立跨分辨率空间对应关系的思路, 对其他跨分辨率图像比较任务亦有借鉴。

## 8. 局限与问题
1. 综述不提出新模型, 价值在总结。
2. 数据集局限 (原文明确): 3 个基准规模小、内容不丰富、缩放比例固定 (0.5/0.75)、仅单方向压缩。
3. 现有方法与 HVS 仅部分一致, 多数用回归获分, 与人眼感知一致性不高。
4. **本笔记覆盖局限**: 提取缓存仅前 12 页 (止于 3.2 节 Lin 等方法截断处)。两类方法优缺点汇总 (Table 3, p.13)、深度学习 IRQA 详评、性能数值 (Table 4-6, p.16-17)、总结展望部分, 均据原文后续页, 提取缓存未覆盖, 待核。

## 9. 我该怎么使用这篇论文
- **快速了解**: 读摘要、引言、1.1/1.2、第 2 节数据集 (10-15 分钟掌握全貌)。
- **复现**: 顺综述定位具体方法原文 (Chen 2017a、Liu 2015、Zhang & Kuo 2014) 再精读。
- **借鉴创新**: 看第 3 节两类方法优缺点; 思考配准+深度特征结合、设计更贴合 HVS 的损失/注意力; 数据集缺点即新数据集动机。
- **写 Related Work**: 按其分类框架引用关键文献, 是 IQA/重定向相关工作素材库。

## 10. 和其他论文的关系
- **核心数据集**:
    - [[Rubinstein et al., 2010]] (MIT RetargetMe)
    - [[Ma et al., 2012]] (CUHK)
    - [[Hsu et al., 2014]] (NRID)
- **特征相似性类代表方法**:
    - [[Ma et al., 2016]] (GIST 特征 + 排名学习)
    - [[Chen et al., 2017a]] (多维特征 + GRNN → 全局排名)
    - [[Chen et al., 2017b]] (NSS + 显著全局结构失真 + 双向显著信息损失)
    - [[Liang et al., 2017]] (多维度特征融合)
    - [[Liu et al., 2020]] (基于 Chen 2017a 的学习式 IRQA)
- **图像配准类代表方法**:
    - [[Zhang and Kuo, 2014]] (特征点匹配 + 全局/局部/显著信息损失)
    - [[Liu et al., 2015]] (空域+频域失真 + SVR)
- **基础重定向算法**:
    - [[Avidan and Shamir, 2007]] (Seam Carving)
    - [[Pritch et al., 2009]] (Shift Maps)
    - [[Tan et al., 2020]] (循环重定向网络)
- **传统 IQA 基础**:
    - [[Wang et al., 2004]] (SSIM)
    - [[Mittal et al., 2012]] (BRISQUE)

## 11. 关键词
图像质量评价 (IQA)、图像重定向 (image retargeting)、图像配准 (image registration)、内容损失 (content loss)、几何失真 (geometric distortion)、综述 (survey)、主观/客观评价、显著性图、特征相似性、细缝裁剪 (seam carving)、PLCC/SRCC、数据集

## 12. 可信度说明
本精读笔记基于 PDF 提取缓存 (覆盖论文前 12 页, p.1-12, 止于第 3.2 节 Lin 等人方法被截断处) 生成。该范围内提取质量良好, 涵盖标题、作者、中英文摘要、引言、相关工作 (重定向算法 4 类 + 传统 IQA 三类)、数据集 (Table 2, 含 MIT/CUHK/NRID 全部构建参数) 以及客观评价两类模型的思想与代表作。所有事实性陈述 (数据集数量/算子/比例、6 早期指标、方法不足 3 点等) 均可在提取文本核实。**论文后续的两类方法优缺点汇总 (Table 3, p.13)、深度学习 IRQA 详评、3 数据集上的具体 PLCC/SRCC 性能数值 (Table 4-6, p.16-17)、总结与展望完整内容, 据原文后续页, 提取缓存未覆盖, 已逐处标注"待核"。**

---

> **可信度补充**: PDF 提取质量 = **high** (前 12 页提取质量好, 约 2086 字符/页; 但提取缓存实际仅覆盖 12/23 页, 后 11 页含 Table 3-6 等关键内容未进入缓存); 来源缓存: `.paper-cache/extracts/cjig_paper_1.txt` (头部声明 pages_extracted: 12/23); 原 AI 主体覆盖 p.1-12, 补读记录据 p.13-23 线索但具体数值仍待核; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-23; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-23。
- **提取情况**: 提取缓存文件头声明 pages_extracted: 12/23, 即正式文本提取仅前 12 页; p.13-23 仅有页面章节/表标题线索 (见下), 表内具体数值未进入缓存, 故相关数字均标"待核"。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核; `human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Table 3 Summary of main ideas, advantages and shortcomings of image retargeting quality evaluation methods
- p.16: Table 4 Performance comparison results on the MIT RetargetMe dataset
- p.16: SIFT-flow / IR-SSIM / PGDIL / Karimi / RN-IRQA / INSEM (方法名线索)
- p.17: Table 5 Performance comparison results on the CUHK dataset
- p.17: Table 6 Performance comparison results on the NRID dataset
- p.17: TRASIM (PLCC, 方法名线索)
- p.18: Proceedings of 2017 IEEE International Conference on Computer (参考文献)
- p.21: Transformation-aware similarity measurement for image retargeting (参考文献)

### 缺失页关键摘录

- p.13: Table 3 Summary of main ideas, advantages and shortcomings of image retargeting quality evaluation methods
- p.16: Table 4 Performance comparison results on the MIT RetargetMe dataset
- p.17: Table 5 / Table 6 Performance comparison results on CUHK / NRID datasets
- p.19: Li L D, Li Y X, Wu J J, Ma L and Fang Y M. 2021. Quality evaluation ... (参考文献)
- p.21: bi-directional evaluation-based approach for image retargeting quality ... (参考文献)
- p.21: Sheikh H R, Sabir M F and Bovik A C. 2006. A statistical evaluation of ... (参考文献)
- p.23: progress in objective quality evaluation of virtual reality images. Journal ... (参考文献)
<!-- AI_READING_NOTE_END -->
