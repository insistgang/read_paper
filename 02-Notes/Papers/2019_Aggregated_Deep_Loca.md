---
title: Aggregated Deep Local Features for Remote Sensing
authors:
  - "Raffaele Imbriaco"
  - "Clint Sebastian"
  - "Egor Bondarev"
  - "Peter H.N. de With"
year: 2019
venue: remote sensing
doi: 10.3390/rs11050493
pdf: [[2019_Aggregated_Deep_Loca.pdf]]
primary_topic: R1_遥感_高光谱_变化检测
topics:
  - "R1_遥感_高光谱_变化检测"
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2019_Aggregated_Deep_Loca.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/24 pages"
---
# Aggregated Deep Local Features for Remote Sensing

## 基本信息
- **PDF**: [[2019_Aggregated_Deep_Loca.pdf]]
- **primary_topic**: `R1_遥感_高光谱_变化检测`
- **topics**: `R1_遥感_高光谱_变化检测`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Aggregated Deep Local Features for Remote Sensing Image Retrieval |
| **作者** | Raffaele Imbriaco; Clint Sebastian; Egor Bondarev; Peter H.N. de With |
| **机构** | Eindhoven University of Technology (Video Coding and Architectures Group) |
| **发表时间** | 2019 (收稿 2018-12-27, 录用 2019-02-24, 发表 2019-02-28) |
| **刊物/会议** | Remote Sensing (MDPI), 2019, vol. 11 |
| **DOI / arXiv** | 10.3390/rs11050493 / arXiv:1903.09469v1 |

## 摘要

**英文原摘要 (据 PDF 提取文本清理)**:

> Remote Sensing Image Retrieval remains a challenging topic due to the special nature of Remote Sensing imagery. Such images contain various different semantic objects, which clearly complicates the retrieval task. In this paper, we present an image retrieval pipeline that uses attentive, local convolutional features and aggregates them using the Vector of Locally Aggregated Descriptors (VLAD) to produce a global descriptor. We study various system parameters such as the multiplicative and additive attention mechanisms and descriptor dimensionality. We propose a query expansion method that requires no external inputs. Experiments demonstrate that even without training, the local convolutional features and global representation outperform other systems. After system tuning, we can achieve state-of-the-art or competitive results. Furthermore, we observe that our query expansion method increases overall system performance by about 3%, using only the top-three retrieved images. Finally, we show how dimensionality reduction produces compact descriptors with increased retrieval performance and fast retrieval computation times, e.g. 50% faster than the current systems.

**中文翻译**:

> 由于遥感影像的特殊性, 遥感图像检索 (RSIR) 仍是一个具有挑战性的课题。这类影像包含多种不同的语义目标, 明显加大了检索难度。本文提出一条图像检索流水线: 它使用注意力引导的局部卷积特征, 并用局部聚合描述子向量 (VLAD) 将其聚合为一个全局描述子。我们考察了多个系统参数, 例如乘性与加性两种注意力机制以及描述子维度。我们提出一种无需任何外部输入的查询扩展方法。实验表明, 即使不经训练, 这些局部卷积特征与全局表示也能优于其他系统; 经过系统调优后, 可以取得最优或有竞争力的结果。此外, 我们观察到该查询扩展方法仅利用检索结果中前三张图像, 就能将整体系统性能提升约 3%。最后, 我们展示了降维如何在提升检索性能的同时产生紧凑的描述子, 并带来更快的检索计算时间, 例如比当前系统快 50%。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 随着遥感影像空间分辨率提升、图像库规模增大, 如何基于视觉内容高效检索遥感图像 (RSIR) 成为现实需求。遥感影像覆盖大范围地理区域, 单幅图内常包含多种不同尺度的语义目标 (如建筑、道路、车辆、植被); 且同一语义类别的图像在不同地理区域采集时外观差异极大。这要求描述子既要有足够的判别力, 又要支持快速数据库检索。
- **之前方法的问题**:
    1. 文献把描述子分为三层: 低层 (颜色、光谱、纹理)、中层 (局部不变特征经 BoW 聚合的全局表示)、以及由 CNN 提取的高层语义特征。前两层不编码语义信息, 难以跨越"语义鸿沟"。
    2. 现有 RSIR 中使用卷积特征的代表性方法 (文献 [12]) 需要先把图像切分成 patch, 逐块提取卷积描述子, 再用 BoW 聚合; 流程繁琐, 且 BoW 聚合性能不如 VLAD。
    3. 作者声称: 在 RSIR 领域, 未见有系统直接为图像中"最显著/最具代表性的区域"生成局部卷积描述子。
- **核心矛盾**: 如何在不切块的前提下, 自动定位遥感图像中语义相关、跨尺度的局部区域, 提取卷积描述子, 并高效聚合成既紧凑又有判别力的全局描述子, 实现快速、准确的检索。

## 关键贡献

1. **新颖的 RSIR 流水线**: 提取注意力引导的、多尺度卷积描述子 (基于 DELF), 在多个 RSIR 数据集上取得最优或有竞争力的结果。这些描述子自动捕获不同尺度上的显著语义特征。
2. **泛化能力**: 展示了为地标检索 (landmark retrieval) 学到的特征可直接复用于 RSIR, 即使不微调也有竞争力。
3. **不同注意力机制的对比**: 实验比较了乘性注意力与加性注意力, 评估局部卷积特征的"上下文"信息对 RSIR 任务是否有用。
4. **无需用户输入的查询扩展**: 提出一种低复杂度查询扩展方法, 仅用 top-3 检索结果, 平均带来约 3% 的性能提升。
5. **低维描述子评估**: 用 PCA 降维后, 检索性能反而更好, 且匹配时间显著下降 (摘要给出"比当前系统快 50%"的量级)。

## 方法

- **整体框架** (图 2): 三阶段流水线——特征提取 (Feature extraction) → 特征聚合 (Feature aggregation) → 图像匹配 (Image matching)。输入查询图像, 输出排序后的检索结果列表。
- **特征提取模块 (DELF [4])**:
    - **骨干网络**: 预训练 **ResNet50**, 从**第三个卷积块 (third convolutional block)** 提取稠密特征。每个 DELF 局部描述子是 **1024 维向量**, 并附带其在图像中的位置、注意力分数和所在尺度。
    - **注意力机制**: 稠密特征不直接使用, 而是经一个独立的小 CNN (注意力模块) 为每个特征向量 $f_n$ 学习一个打分函数 $a(f_n; Q)$ ($Q$ 为该函数参数, $n=1,\dots,N$, $f_n\in\mathbb{R}^d$)。注意力模块用 softplus 激活 (避免学到负权重)。
    - **乘性注意力 (Multiplicative attention)**: $y = W\left(\sum_n a(f_n; Q) f_n\right)$ (式 1), $W\in\mathbb{R}^{M\times d}$ 为 $M$ 类的最终预测层权重。直接用注意力分数加权特征, 会**完全抑制**网络认为不相关的特征。
    - **加性注意力 (Additive attention)**: $y = W\left(\sum_n (1 + a(f_n; Q)) f_n\right)$ (式 2)。在增强显著特征的同时**保留**其他特征 (上下文)。作者认为, 对遥感影像而言乘性注意力可能丢掉有用的语义上下文, 故提出加性注意力。
    - **多尺度**: 训练后, 去掉最后两层卷积层; 把输入图像缩放到 **7 个尺度** (从 0.25 到 2.0, 间隔因子 $\sqrt{2}$) 各前向一次, 单次流程即可生成多尺度特征, 无需手动分块。
    - **关键点选择**: 跨全部 7 个尺度按注意力分数排序, 每幅图保留**注意力最高的 300 个特征**; 据原文, 这约占所有非零注意力描述子的 21%。注意特征在各尺度上分布不均 (UCMerced 上 53% 的特征……此处提取缓存截断, 待核)。
- **特征聚合模块 (VLAD [6])**:
    - **作用**: 把每幅图的局部描述子聚合为单一、紧凑的全局描述子。
    - **与 BoW 区别**: BoW/VLAD/FK 都先用聚类构造码本 (VLAD、BoW 用 k-means, FK 用高斯混合); BoW 只生成视觉词频率直方图, 而 VLAD 编码局部描述子相对聚类中心的残差统计量, 性能优于 BoW (原文据 [6])。
- **图像匹配与查询扩展**:
    - **匹配**: 用全局描述子间的向量距离 (如欧氏距离/余弦相似度) 排序候选图像。
    - **查询扩展**: 仅用全局表示、无需用户输入。提取文本未给出聚合方式的完整公式细节 (具体平均/加权方式据原文后续页, 提取缓存未覆盖, 待核); 摘要明确"仅用 top-3 检索图像, 平均提升约 3%"。
- **训练方式**:
    1. **两阶段、分开训练** (沿用 DELF [4] 做法, 作者称分开训练检索性能更好): 先训特征提取网络, 再固定其权重、单独训注意力网络。
    2. **特征提取网络**: 作为分类器训练, 损失为交叉熵; 图像缩放到 **224×224**; 此阶段**不做随机裁剪** (目的是学更好的特征, 而非特征定位/显著性)。
    3. **注意力模块**: 半监督方式; 输入图像**随机裁剪**后缩放到 224×224, 仍用交叉熵 (仅用原图像级标签, 无需额外标注), 迫使网络学到"哪些区域/特征对特定类别更相关"。
- **和已有方法的差异**: 不切 patch (注意力自动聚焦显著区域) + 用 VLAD 而非 BoW 聚合 + 端到端基于特征显著性 + 可单次多尺度提取。

## 实验

> 说明: PDF 提取缓存只覆盖前 12 页 (止于 3.1 特征提取节中段), 实验章节的完整数值表格在第 13-24 页, 提取缓存未覆盖。以下数据集与对比方法据笔记后续页线索与缺失页摘录, 标注"待核"。

- **使用的数据集** (据缺失页表头线索 p.13/p.15): **UCM (UCMerced Land-Use)、SATREM、SIRI、NWPU (NWPU-RESISC45)**。(注: 原笔记曾写"AID", 提取文本/缺失页线索均未出现 AID, 已删除; 出现的是 SATREM 与 SIRI。)
- **对比方法** (据缺失页线索 p.13/p.15): **DBOW、ResNet-50、BoCF、D-CNN**, 以及本文的 Multiplicative Attention / Additive Attention 两种配置。引言/相关工作中提及的传统基线包括 fc 层全局特征 (Babenko 等 [2]) 与 SIFT+BoW 类方法。
- **评价指标**: 平均精度 (Average Precision / mAP)。缺失页表 4-8 为各数据集的检索精度对比 (待核具体数值)。
- **主要结论 (来自摘要, 可信)**:
    - **未训练时**, 局部卷积特征 + 全局表示即可优于其他系统;
    - **系统调优后**, 取得最优或有竞争力的结果;
    - **查询扩展** 仅用 top-3 平均提升约 3%;
    - **降维** 在提升检索性能的同时使检索更快 (约快 50%)。
- **消融 / 分析 (缺失页线索)**:
    - 注意力机制对比 (乘性 vs 加性): 缺失页提到二者结果"几乎相同, 仅 top-one precision 例外" (p.17 摘录), 提示加性注意力优势有限。原笔记给出的"加性比乘性高约 0.6%"在提取文本中未找到支撑, **待核**。
    - 查询扩展稳定性: p.17 提到对不同大小检索集做实验 (图 6), VLAD 用 300 个最具注意力的特征构建。
    - 描述子数量影响 (表 9): 用更多特征构建字典/VLAD 时, UCM、SIRI 数据集上性能反而可能下降。
    - 原笔记给出的"4096 维 VLAD 降到 256 维""NWPU 从 78.12% 提升到 80.59%"等具体数字在提取文本中无法核实, **据原文后续页, 提取缓存未覆盖, 待核**。
- **泛化实验**: 用为地标检索 (Google Landmarks/DELF) 学到的模型直接做 RSIR, 不微调即有竞争力 (摘要与引言可证方向, 具体数值待核)。

## 局限

- **场景级检索为主**: 所用数据集 (UCM、SATREM、SIRI、NWPU) 本质偏场景分类, "相似"更接近类别相似; 对需检索特定小目标 (飞机、船舶) 的应用, 适用性未知。
- **计算成本**: 特征提取要跑 7 个尺度的前向传播并额外运行注意力网络, 开销高于单次前向的全局特征方法; 论文未在提取文本中给出特征提取时间对比 (匹配时间有对比, 提取时间待核)。
- **加性注意力收益存疑**: 缺失页线索显示乘性/加性结果"几乎相同", 该创新点的实际增益可能很小。
- **对注意力可靠性的依赖**: 复杂、密集遥感场景中, 注意力可能分散或聚焦于干扰物。
- **复现风险**: 论文未提供代码 (据原笔记判断, 提取文本未明确); VLAD 码本大小 (聚类中心数 k)、随机裁剪比例、查询扩展聚合细节等超参在提取文本中缺失, 复现需调参。

## 个人评论

1. **注意力用于"选择+加权"局部特征, 而非压缩特征图**: 这比简单 pooling 更贴合检索任务, 让模型自动学"哪些区域对检索重要", 免去手工分块。这是把 DELF 思路迁移到遥感域的合理工程化。
2. **VLAD 与深度局部特征的结合是务实选择**: 在 2019 年这是经典聚合方法 + 深度特征的成熟范式, 性能优于 BoW, 也比端到端可学聚合 (如 NetVLAD) 更易落地。
3. **"简单后处理拿增益"的工程智慧**: 无监督查询扩展 (仅 top-3 平均) 与 PCA 降维都很轻量, 却带来约 3% 提升和约 50% 提速——提醒研究者经典后处理与深度特征结合常有性价比。
4. **加性注意力的价值需谨慎看待**: 缺失页线索显示它与乘性注意力结果几乎相同, 这个"创新点"在本文证据下说服力有限, 引用时不宜夸大。
5. **对后续研究的启发**: 可探索自注意力/图注意力 + 可学聚合 (NetVLAD/GeM) 的替代; 也可把该框架当作强特征提取器, 迁移到遥感细粒度分类、变化检测等任务。

### 使用建议

- **如果快速了解**: 读摘要、引言贡献点、图 2 流水线、第 4 节主要表格。
- **如果复现**: 精读第 3 节 (ResNet50 第三卷积块、7 尺度 √2、注意力网络结构 (图 3) 与半监督随机裁剪训练、VLAD/PCA 实现); 实验设置看第 4 节。注意码本大小 k 与查询扩展聚合细节需自行确定。
- **如果借鉴创新点**: 学"注意力选择 + VLAD 聚合"范式; 借鉴无监督查询扩展; 思考"降维反而提升性能"的现象 (可能去噪/缓解过拟合)。
- **如果写 Related Work**: 可归入 (1) 基于深度学习的图像检索; (2) 注意力机制在视觉识别中的应用; (3) 特征聚合技术 (VLAD/FK) 的现代应用; (4) 遥感图像检索专门方法。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页:
> - [[R1_遥感_高光谱_变化检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
计算机视觉 (图像检索) 与遥感影像处理的交叉工作。解决**遥感图像检索 (RSIR)**: 给定一张查询遥感图像, 从大规模库中按视觉内容找出相似图像。方法学根属于"基于内容的图像检索 (CBIR)"在遥感场景的实现, 核心是把地标检索里的注意力深度局部特征 (DELF) 迁移到遥感, 配 VLAD 聚合与查询扩展。在本库 taxonomy 中归为遥感方向 (R1)。

## 2. 一句话总结
本文用基于注意力的深度局部特征 (DELF, ResNet50 第三卷积块, 1024 维, 7 尺度) 提取遥感图像的显著局部描述子, 用 VLAD 聚合为全局描述子, 再辅以无需用户输入的查询扩展 (top-3, +约 3%) 和 PCA 降维 (提速约 50% 且不降精度), 在多个 RSIR 数据集上取得最优或有竞争力的结果。

## 3. 背景与问题
- **为什么要做**: 遥感影像分辨率与库规模上升, 单幅图含多尺度、多类别语义目标, 同类跨地域外观差异大, 直接套用普通图像检索效果有限。
- **之前方法的问题**:
    1. 低层 (颜色/光谱/纹理) 与中层 (BoW 直方图) 特征不编码语义, 存在语义鸿沟。
    2. 用卷积特征的代表 RSIR 方法 [12] 需切 patch 逐块提取再 BoW 聚合, 流程繁琐且 BoW 弱于 VLAD。
    3. 作者称 RSIR 中未见"直接为最显著区域生成局部卷积描述子"的系统。
- **核心矛盾**: 不切块地自动定位跨尺度显著区域、提取卷积描述子, 并聚合成紧凑且判别力强的全局描述子。

## 4. 核心贡献
1. 注意力引导、多尺度卷积描述子的 RSIR 流水线 (DELF + VLAD), 多数据集 SOTA/有竞争力。
2. 泛化: 地标检索学到的特征可直接复用于 RSIR, 不微调也有竞争力。
3. 对比乘性与加性两种注意力, 评估"上下文"对 RSIR 的作用。
4. 无需用户输入的查询扩展 (top-3, 平均 +约 3%, 低复杂度)。
5. 低维描述子评估: PCA 降维既提性能又显著降匹配时间 (摘要: 约快 50%)。

## 5. 方法详解
- **流水线 (图 2)**: 特征提取 → 特征聚合 → 图像匹配。
- **特征提取 (DELF)**:
    - ResNet50, 第三卷积块, 局部描述子 **1024 维**, 每个描述子带位置、注意力分数、尺度。
    - 注意力: 独立小 CNN 学打分 $a(f_n; Q)$, softplus 激活避免负权重。
    - 乘性注意力 (式 1): $y=W(\sum_n a(f_n;Q) f_n)$, 完全抑制不相关特征。
    - 加性注意力 (式 2): $y=W(\sum_n (1+a(f_n;Q)) f_n)$, 增强显著特征同时保留上下文。
    - 多尺度: 7 个尺度 (0.25→2.0, 间隔 √2), 单次流程; 训练后去掉最后两卷积层。
    - 每图保留注意力最高的 300 个特征 (约占非零注意力描述子的 21%)。
- **聚合 (VLAD)**: k-means 码本, 编码相对聚类中心的残差统计, 优于 BoW。
- **匹配 + 查询扩展**: 全局描述子向量距离排序; 查询扩展只用全局表示、无用户输入 (具体聚合细节据后续页, 待核), top-3 平均 +约 3%。
- **训练**: 两阶段分开训练; 特征网络分类训练 (交叉熵, 224×224, 不随机裁剪); 注意力模块半监督 (随机裁剪 + 224×224 + 交叉熵, 仅用图像级标签)。

## 6. 实验与结果
- **数据集** (缺失页线索): UCM、SATREM、SIRI、NWPU。(原笔记"AID"系误, 已订正。)
- **对比方法** (缺失页线索): DBOW、ResNet-50、BoCF、D-CNN, 加本文乘性/加性注意力配置。
- **指标**: Average Precision / mAP; 缺失页表 4-8 给各数据集检索精度 (数值待核)。
- **可信结论 (摘要)**: 未训练即优于他法; 调优后 SOTA/有竞争力; 查询扩展 top-3 +约 3%; 降维提性能且约快 50%。
- **分析线索 (p.13-18)**: 乘性 vs 加性"结果几乎相同, 仅 top-one precision 例外" (故加性增益有限); 表 9 显示用更多特征构建字典/VLAD 时 UCM、SIRI 反而可能下降。原笔记"+0.6%""4096→256 维""NWPU 78.12%→80.59%"等具体数字提取文本无法核实, **待核**。
- **泛化**: 地标检索预训练模型直接用于 RSIR 不微调即有竞争力 (方向可证, 数值待核)。

## 7. 这篇论文真正有价值的地方
1. 把注意力用于"选择/加权"局部特征而非压缩特征图, 更贴合检索, 免去手工分块。
2. 证明经典 VLAD 与深度局部特征结合的成熟范式在遥感域可行且有效。
3. 极轻量的无监督查询扩展 (top-3) 与 PCA 降维带来"提质 + 提速"的双赢, 是务实的工程智慧。
4. 给出跨域复用 (地标→遥感) 的正面证据, 提示 DELF 特征的可迁移性。

## 8. 局限与问题
- 评测以场景级检索为主, 小目标检索 (飞机/船舶) 适用性未知。
- 7 尺度前向 + 额外注意力网络, 特征提取成本高于单次前向全局法; 提取时间无对比 (待核)。
- 加性注意力相对乘性的实际增益很小 (缺失页线索"几乎相同")。
- 性能依赖注意力可靠性; 复杂密集场景可能聚焦干扰物。
- 无代码 (据原笔记); 码本大小 k、查询扩展聚合、随机裁剪比例等超参在提取文本缺失, 复现需调参。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言贡献点 + 图 2 + 第 4 节主表。
- **复现**: 精读第 3 节 (ResNet50 第三卷积块、7 尺度 √2、图 3 注意力结构、半监督随机裁剪训练、VLAD/PCA); 自定 k 与查询扩展聚合细节。
- **借鉴**: 注意力选择 + VLAD 聚合范式; 无监督查询扩展; "降维提性能"现象。
- **写 Related Work**: 归入深度学习图像检索 / 注意力机制 / 特征聚合 (VLAD/FK) / 遥感图像检索四类。

## 10. 和其他论文的关系
本文是 RSIR (遥感图像检索) 工作, 直接相关的基础工作:
- **DELF (Deep Local Features, Noh et al. [4])**: 本文特征提取模块的来源, 这是其在遥感域的迁移与扩展。
- **VLAD (Vector of Locally Aggregated Descriptors [6])**: 本文采用的聚合方法, 优于 BoW。
- **文献 [12] (patch + 卷积描述子 + BoW, 无监督自编码器)**: 本文的主要对照 RSIR 方法之一。
- 同库可关联: 遥感方向 [[R1_遥感_高光谱_变化检测]] 主题下的其他检索/特征工作。

## 11. 关键词
图像检索、卷积描述子、查询扩展、描述子聚合、卷积神经网络、注意力机制、VLAD、遥感图像检索 (RSIR)、深度局部特征 (DELF)、主成分分析 (PCA)。

## 12. 可信度说明
本笔记的"摘要、研究背景、方法 (第 3 节: 架构、特征提取、注意力机制式 1/式 2、多尺度、300 特征、两阶段训练)"严格基于 PDF 提取文本前 12 页, 文本质量良好, 可逐句核对。**实验数值部分受限**: 提取缓存只覆盖 12/24 页 (止于 3.1 节中段), 实验表 4-9、消融完整数值、结论在第 13-24 页, 不在提取文本内; 这部分依据缺失页章节线索与摘录, 并对原笔记中无法核实的具体数字 (如 +0.6%、4096→256 维、NWPU 78.12%→80.59%、AID 数据集) 做了订正或标注"待核"。原笔记"AID"数据集已删除 (缺失页线索显示实际为 SATREM、SIRI)。

---

> **可信度补充**: PDF 提取质量 = **high** (前 12 页提取质量好, 约 2086 字符/页); 但提取缓存仅覆盖 12/24 页, 实验数值章节 (p.13-24) 未进入提取文本, 相关数字标注"待核"。来源缓存: `.paper-cache/extracts/2019_Aggregated_Deep_Loca.txt` (12/24 页); 本轮校订: 订正数据集 (删 AID, 补 SATREM/SIRI)、修正 primary_topic (T_通用_NLP_其他 → R1_遥感_高光谱_变化检测)、重建摘要、标注无法核实的实验数字; 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-24; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-24。
- **提取情况**: 缺失页 12 页, 其中 12 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核; `human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Method UCM SATREM SIRI NWPU
- p.13: DBOW ResNet-50 BoCF DCNN Multiplicative Attention Additive Attention
- p.15: DBOW ResNet-50 BoCF D-CNN Multiplicative Attention Additive Attention
- p.17: A further aspect for evaluation is the query expansion stability by experimenting with different
- p.17: results. Furthermore, their results are almost identical, with the exception of top-one precision. We also
- p.18: While the proposed system provides state-of-the-art results in the RSIR task, the above described
- p.18: experiments deploy descriptors that are 4 times larger than the largest descriptor used in previous
- p.18: SATREM
- p.18: V-DELF
- p.18: QE-IAverage Precision for Retrieval Sets of Different Sizes
- p.18: Retrieval Set SizePrecision
- p.18: Query

### 缺失页关键摘录

- p.13: Table 4. Average precision comparison between various RSIR methods using convolutional features.
- p.13: Table 5. Retrieval precision for the UCM dataset after training the DELF network. Bold values indicate
- p.14: Table 6. Retrieval precision for the SATREM dataset after training the DELF network. Bold values
- p.14: Table 7. Retrieval precision for the SIRI dataset after training the DELF network. Bold values indicate
- p.15: Table 8. Retrieval precision for the NWPU dataset after training the DELF network. Bold values
- p.16: Figure 5. The 10 most attentive features per scale are depicted for different semantic classes of
- p.17: A further aspect for evaluation is the query expansion stability by experimenting with different
- p.17: performance. In Figure 6, the average precision for various sizes of the retrieval set is depicted. It
- p.17: this experiment, VLAD descriptors are constructed with the 300 most attentive features and the number
- p.17: study are found in Table 9. The ﬁrst experiment reveals that using more features for generation of the
- p.17: performance may decrease, as is the case for the UCM and SIRI datsets. From the second experiment,
- p.17: Table 9. Impact of the number of descriptors used for visual dictionary and VLAD construction on
<!-- AI_READING_NOTE_END -->
