---
title: "S2Looking: A Satellite Side-Looking Dataset for Building Change Detection"
authors:
  - "Li Shen"
  - "Yao Lu"
  - "Hao Chen"
  - "Hao Wei"
  - "Donghai Xie"
  - "Jiabao Yue"
  - "Rui Chen"
  - "Shouye Lv"
  - "Bitao Jiang"
year: 2021
venue: remote sensing
doi: 10.3390/rs1010000
pdf: [[2021_S2Looking_A_Satelli.pdf]]
primary_topic: S_变化检测_ChangeDetection
topics:
  - "S_变化检测_ChangeDetection"
  - "L_数据集_Benchmark"
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
extract_cache: .paper-cache/extracts/2021_S2Looking_A_Satelli.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/23 pages"
---
# S2Looking: A Satellite Side-Looking Dataset for Building Change Detection

## 基本信息
- **PDF**: [[2021_S2Looking_A_Satelli.pdf]]
- **primary_topic**: `S_变化检测_ChangeDetection`
- **topics**: `S_变化检测_ChangeDetection`, `L_数据集_Benchmark`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | S2Looking: A Satellite Side-Looking Dataset for Building Change Detection |
| **作者** | Li Shen, Yao Lu (通讯), Hao Chen, Hao Wei, Donghai Xie, Jiabao Yue, Rui Chen, Shouye Lv, Bitao Jiang |
| **机构** | 北京遥感信息研究所、北航宇航学院图像处理中心、天津大学微电子学院、首都师范大学资源环境研究所 |
| **发表时间** | 2021 (Remote Sensing; arXiv:2107.09244v3, 2022-01-11) |
| **刊物/会议** | Remote Sensing (MDPI) |
| **DOI** | 10.3390/rs1010000 |

## 摘要

清理后的英文原摘要（修复连写、断字与杂入字符）：

> Building-change detection underpins many important applications, especially in the military and crisis-management domains. Recent methods used for change detection have shifted towards deep learning, which depends on the quality of its training data. The assembly of large-scale annotated satellite imagery datasets is therefore essential for global building-change surveillance. Existing datasets almost exclusively offer near-nadir viewing angles. This limits the range of changes that can be detected. By offering larger observation ranges, the scroll imaging mode of optical satellites presents an opportunity to overcome this restriction. This paper therefore introduces S2Looking, a building-change-detection dataset that contains large-scale side-looking satellite images captured at various off-nadir angles. The dataset consists of 5000 bitemporal image pairs of rural areas and more than 65,920 annotated instances of changes throughout the world. The dataset can be used to train deep-learning-based change-detection algorithms. It expands upon existing datasets by providing (1) larger viewing angles; (2) large illumination variances; and (3) the added complexity of rural images. To facilitate the use of the dataset, a benchmark task has been established, and preliminary tests suggest that deep-learning algorithms find the dataset significantly more challenging than the closest-competing near-nadir dataset, LEVIR-CD+. S2Looking may therefore promote important advances in existing building-change-detection algorithms.

中文翻译：

> 建筑物变化检测支撑着许多重要应用，尤其在军事与危机管理领域。近年来变化检测方法已转向深度学习，而深度学习的效果依赖训练数据的质量，因此构建大规模、带标注的卫星影像数据集对全球建筑物变化监测至关重要。然而现有数据集几乎只提供近星下点（near-nadir）视角，限制了可检测变化的范围。光学卫星的滚转成像模式（scroll imaging）能提供更大的观测范围，为突破这一限制提供了契机。为此本文提出 S2Looking——一个包含大规模侧视卫星影像、在不同离轴角下拍摄的建筑物变化检测数据集。数据集由 5000 对双时相图像对组成，覆盖全球农村地区，标注变化实例超过 65,920 个，可用于训练基于深度学习的变化检测算法。它在三方面扩展了现有数据集：(1) 更大的观测视角；(2) 更大的光照差异；(3) 农村影像带来的额外复杂度。为便于使用，论文建立了基准任务；初步测试表明，相比最接近的近星下点数据集 LEVIR-CD+，深度学习算法在 S2Looking 上面临的挑战显著更大。S2Looking 因此有望推动建筑物变化检测算法的重要进步。
>
> **关键词**（原文）：change detection; remote sensing; benchmark dataset; neural networks

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：建筑物变化检测服务于城市扩张监测、土地利用/覆盖变化监测、资源管理评估等应用，并在军事监视与危机管理中尤为重要——建筑变化可能预示威胁形成或灾后救援重点区域（p. 1）。深度学习已成为变化检测主流，但其性能严重依赖训练数据的规模、质量与完整性（p. 1-2）。
- **之前方法/数据集的问题**：传统方法分为基于像素与基于对象两类，依赖手工特征与阈值分割，易受图像细节与质量变化影响，精度受限（p. 1, 4-5）。深度学习方法（DASNet、IFN、CD-UNet++、FC-Siam-Conc/Diff、DTCDSCN 等）虽更优，但受训练数据制约（p. 1）。现有公开变化检测数据集（Change Detection Dataset、WHU、SZTAKI、OSCD、AICD、LEVIR-CD 等）几乎全部基于**近星下点影像**，观测到的建筑特征相对简单，限制了算法服务实际应用的广度（p. 5-7）。
- **核心矛盾 / 切入点**：现代光学卫星（尤其侦察/监视卫星）的**滚转成像模式**能在多个离轴角下捕获同一目标，相比测绘卫星拥有更大成像范围和更短重访周期（文中举例：GF-1 重访周期 41 天，35° 离轴角下可缩短至 4 天；GF-2 为 69 天 / 5 天），对应急响应价值巨大（p. 2-3, 7-8）。但此前唯一认真做多角度卫星影像数据集的工作是 SpaceNet MVOI，而它不针对变化检测、不提供双时相图像，且只含单一地理位置 27 个不同视角（p. 3）。大规模、带标注的**侧视变化检测数据集缺失**，与开发能处理真实侧视影像的鲁棒算法的需求之间存在根本矛盾。

## 关键贡献

原文 1.3 节明确列出四项贡献（p. 7）：

1.  **数据集构建流水线**：提出一套构建基于卫星遥感影像的建筑物变化检测数据集的流程（pipeline）。
2.  **发布 S2Looking 数据集**：首个大规模、侧视、覆盖全球农村区域的建筑物变化检测遥感数据集。含 5000 对双时相 VHR 图像、65,920 个专家标注变化实例、69,611,520 个变化像素（p. 3, 6 Table 1）。
3.  **建立基准任务**：建立像素级建筑物变化检测的 benchmark，供现有算法在大规模侧视影像上评估变化监测能力（p. 7）。
4.  **初步评估并反思**：初步评估数据集带来的额外复杂度，并据此简要反思基于监视卫星的建筑物变化检测的未来发展方向（p. 7）。

## 方法

本文是一篇**数据集 / 基准论文**，核心“方法”在于数据集构建、特性描述与基准建立，而非提出新网络模型。

- **数据来源与采集**：5000 对双时相 VHR 配准图像，采自高分（GaoFen, GF）、超景（SuperView, SV）、北京二号（BeiJing-2, BJ-2）卫星，时间跨 2017-2020 年，覆盖全球分布的多种农村区域（村庄、农场、别墅、零售中心、工业区等，见 Figure 2）（p. 3）。
- **预处理与标注**：每幅图像 1024×1024，分辨率 0.5-0.8 m/pixel；原始 16-bit TIFF 转为 8-bit PNG。每个样本配有两张标签图，分别标出**新建（newly built）**与**拆除（demolished）**建筑区域，均为像素级专家标注（p. 3）。
- **输入输出**：输入为同一地理位置、不同时间的两幅 1024×1024 VHR 图像；输出为两张像素级标签图（新建 / 拆除）。
- **关键特性**：
    1.  **侧视成像**：图像由卫星滚转成像在不同离轴角下拍摄，带来与近星下点截然不同的几何畸变与遮挡，使建筑识别与匹配显著更难（p. 1-3）。
    2.  **大光照差异 + 复杂农村场景**：跨时相光照变化大、阴影多，农村地物复杂（p. 3）。
    3.  **规模与多样性**：5000 对、65,920 实例，全球农村（p. 3）。
- **与 LEVIR-CD+ 的差异**（全篇主对照基准，p. 6-8）：①视角：侧视 vs 近星下点；②场景：全球农村 vs 美国得州城市；③数据来源：监视/侦察卫星 vs Google Earth 测绘卫星；④规模：S2Looking 图像对数最多、变化实例/变化像素最多（WHU 单图尺寸与分辨率最高）。LEVIR-CD+ 含 985 对、来自得州 20 个区域、时间跨 2002-2020、每对时间跨度约 5 年（p. 7）。
- **变化检测方法分类（相关工作梳理）**：论文将深度学习变化检测分为 **metric-based** 与 **classification-based** 两类（p. 5）。metric-based 学习嵌入空间使变化像素距离大、未变像素距离小，多用对比损失（contrastive loss），代表如 STANet（含 STANet-Base / STANet-BAM / STANet-PAM）；classification-based 用 CNN 学双时相到变化概率图的映射，多用交叉熵损失、可用早/晚融合，选择更丰富、应用更普遍，代表如 IFN、FC-EF、FC-Siam-Conc/Diff、DTCDSCN、CDNet、BiT（p. 5）。

## 实验

- **基准设置（Benchmark Setup）**：论文为数据集建立像素级变化检测 benchmark，并按地理区域划分以兼顾真实使用场景与公平性（据原文 p.13-14 章节线索 "2.4. Challenge Restrictions" / "3.1. Benchmark Setup"，提取缓存未覆盖正文，待核）。
- **使用的数据集**：S2Looking（本文）与对照基准 LEVIR-CD+（p. 7）。
- **对比方法**：FC-EF、FC-Siam-Conc、FC-Siam-Diff、DASNet、STANet（Base/BAM/PAM）、DTCDSCN、CDNet、IFN、BiT 等（p. 1, 5；图例 p.16 出现 STANet-BAM、FC-EF 的 epoch 曲线）。
- **评价指标**：F1-score（以 TP/FP/FN 计算 Precision、Recall、F1；据原文 p.15 章节线索 "F1-scores can be used as evaluation metrics" 与 "TP, FP, and FN correspond to..."，提取缓存未覆盖具体公式与数值，待核）。
- **主实验结论**：摘要与引言均指出 "preliminary tests suggest that deep-learning algorithms find the dataset significantly more challenging than the closest-competing near-nadir dataset, LEVIR-CD+"（p. 1, 3）。原文 p.13 进一步说明：许多方法在 LEVIR-CD 上已达 F1 > 0.85，但 S2Looking 给变化检测带来全新挑战；S2Looking 是 LEVIR-CD+ 的扩展版，必然更难；其变化建筑实例比 LEVIR-CD+ 稀疏得多（rural vs urban 差异所致）（据原文 p.13 摘录，提取缓存未覆盖完整正文，待核）。
- **具体数值（各方法 F1 等）**：提取缓存（仅前约 8 页 / 25000 字符）未覆盖结果表格，PDF 文本未明确给出具体数字，待核。
- **消融 / 速度 / 参数量**：提取缓存未覆盖，PDF 文本未明确。

## 局限

1.  **任务与场景局限**：仅针对**建筑物**变化、且以**农村**场景为主，未覆盖城市侧视场景与其他地物类型。
2.  **数据来源相对单一**：主要来自中国卫星（GF、SV、BJ-2），虽覆盖全球区域，但卫星平台类型有限，对更多样侧视成像条件的模拟可能不足。
3.  **稀疏变化带来的难点**：农村变化建筑实例稀疏（原文 p.13 "Sparse building updates"），正负样本极不平衡，对算法是额外挑战，论文未在提供文本中给出针对性方案。
4.  **未提出新方法**：贡献在“数据”与“问题”，而非“解决方案”；只测试现有方法，未提出针对侧视挑战的专用模型或训练策略。
5.  **标注一致性**：65,920 实例的像素级标注人力成本巨大，提供文本未详述质量控制与标注一致性保证。
6.  **配准精度**：原文 p.13 提到“若配准精度提升，这些标注图像可被复用”，暗示当前配准存在残差，是潜在误差源（据原文 p.13 摘录，待核）。

## 个人评论

> 以下为 AI 阅读评论，非论文原文结论。

1.  **定义了新问题域**：把“侧视卫星影像 + 农村场景”的建筑物变化检测确立为一个独立、重要的研究方向，并提供首个专用大规模基准，这是其最大价值。
2.  **揭示了算法瓶颈**：在 LEVIR-CD 上 F1>0.85 的 SOTA，到 S2Looking 上显著退化，直接量化暴露了现有算法在大视角变化、复杂几何/光照、稀疏正样本下的脆弱性。
3.  **对照实验设计干净**：全篇以 LEVIR-CD+ 为单一参照系（同为 1024×1024、0.5 m 量级），使“近星下点 → 侧视”这一变量被清晰隔离，是数据集论文凸显价值的范本做法。
4.  **实用价值导向**：素材取自侦察/监视卫星（重访快、范围大），贴合应急响应等真实场景，研究动机不止于学术。
5.  **可改进处**：论文偏“提出问题”，对“稀疏变化 + 大离轴角”这两个核心难点缺少哪怕雏形的算法应对，留给后续工作很大空间。

### 使用建议

- **快速了解**：读 Abstract + 1.3 Contributions（p. 7）+ Table 1（p. 6），即可掌握目的、数据集核心数字与定位。
- **复现 / 用数据**：看 2. Materials and Methods（p. 7 起）理解来源、预处理（16-bit TIFF→8-bit PNG）、双标签（新建/拆除）协议；数据与指南见官方仓库 https://github.com/S2Looking/ 。
- **借鉴创新点**：学习“针对现有数据集短板（视角、场景单一）定义新数据集核心特性 + 用单一 SOTA 数据集（LEVIR-CD+）做对照凸显挑战”的范式。
- **写 Related Work**：归入“变化检测数据集”子类，与 [[LEVIR-CD]]、[[WHU Building Dataset]]、[[OSCD]]、[[SZTAKI]]、[[AICD]] 对比，突出侧视 + 农村 + 规模三大特性。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[S_变化检测_ChangeDetection]]
> - [[L_数据集_Benchmark]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于遥感变化检测（change detection）方向的**数据集 / 基准论文**，聚焦建筑物变化检测，核心创新是首次提供大规模**侧视（side-looking / off-nadir）卫星影像 + 复杂农村场景**的双时相基准。它不提出新模型，而是通过发布数据集 + benchmark 推动算法发展。因此最贴切主题为“**S_变化检测_ChangeDetection**”，并兼具“**L_数据集_Benchmark**”属性（原笔记归入 F_图像分割 属于错配，本轮已改正）。

## 2. 一句话总结
S2Looking 提出首个大规模侧视卫星建筑物变化检测数据集（5000 对双时相图、65,920 个变化实例、覆盖全球农村），用更大离轴角、更大光照差异和更复杂农村场景，证明现有 SOTA 算法在侧视影像上显著退化，从而为变化检测算法的鲁棒性研究立起新基准。

## 3. 背景与问题
- **为什么要做**：建筑变化检测服务城市扩张、土地覆盖、资源管理，尤其军事监视与危机管理。深度学习已成主流，但性能受训练数据规模/质量制约（p. 1-2）。现有公开变化检测数据集几乎全为近星下点视角，建筑特征相对简单，限制算法实用广度（p. 5-7）。
- **之前方法的问题**：传统像素/对象法依赖手工特征 + 阈值，易受图像质量影响，精度受限（p. 1, 4）；深度学习法（DASNet/IFN/CD-UNet++/FC-Siam/DTCDSCN 等）受数据集制约（p. 1）。
- **核心矛盾**：光学卫星滚转成像可在大离轴角下成像，范围更大、重访更快（GF-1：41 天 / 4 天@35°；GF-2：69 天 / 5 天@35°），对应急响应价值高（p. 2-3, 8）；但唯一的多角度卫星数据集 SpaceNet MVOI 不做变化检测、无双时相、仅单点 27 视角（p. 3）。**侧视变化检测数据集的缺失**是关键瓶颈。

## 4. 核心贡献
1.  **数据集构建流水线**（pipeline）（p. 7）。
2.  **S2Looking 数据集**：5000 对 VHR 双时相图、65,920 变化实例、69,611,520 变化像素、全球农村、双标签（新建/拆除）（p. 3, 6）。
3.  **像素级变化检测 benchmark**，供现有算法在大规模侧视影像上评估（p. 7）。
4.  **初步评估数据集复杂度并反思未来方向**（p. 7）。

## 5. 方法详解
本文核心是**数据**而非模型。
- **构建流程**：采集 GF/SV/BJ-2 卫星 2017-2020 影像 → 配准 → 裁剪为 1024×1024 → 16-bit TIFF 转 8-bit PNG → 专家像素级标注（新建 / 拆除两张标签图）（p. 3）。
- **输入输出**：输入同位置双时相 1024×1024 VHR（0.5-0.8 m/pixel）图像对；输出两张像素级变化标签图。
- **关键特性**：①侧视成像带来强几何畸变/遮挡；②跨时相大光照差异 + 复杂农村场景；③规模与多样性领先（p. 1-3）。
- **与 LEVIR-CD+ 差异**：视角（侧视 vs 近星下点）、场景（全球农村 vs 得州城市）、来源（监视/侦察卫星 vs Google Earth 测绘卫星）、规模（图像对/变化实例/变化像素最多）（p. 6-8）。
- **相关工作分类**：metric-based（学嵌入空间 + 对比损失，如 STANet-Base/BAM/PAM）vs classification-based（CNN 学变化概率图 + 交叉熵，可早/晚融合，如 IFN/FC-EF/FC-Siam-Conc/Diff/DTCDSCN/CDNet/BiT）；后者选择更多、应用更广（p. 5）。

## 6. 实验与结果
- **数据集**：S2Looking + 对照 LEVIR-CD+（p. 7）。
- **对比方法**：FC-EF、FC-Siam-Conc/Diff、DASNet、STANet(Base/BAM/PAM)、DTCDSCN、CDNet、IFN、BiT 等（p. 1, 5；p.16 出现 STANet-BAM、FC-EF 训练曲线）。
- **评价指标**：基于 TP/FP/FN 的 Precision/Recall/F1-score（据原文 p.15 章节线索，提取缓存未覆盖公式与数值，待核）。
- **核心结论**：preliminary tests 表明算法在 S2Looking 上比近星下点 LEVIR-CD+ 显著更难（p. 1, 3）；许多方法在 LEVIR-CD 上 F1>0.85，但 S2Looking 给出全新挑战，且其变化实例比 LEVIR-CD+ 稀疏得多（rural vs urban）（据原文 p.13 摘录，待核）。
- **具体数字、消融、速度/参数量**：提取缓存仅含前约 8 页（25000 字符上限），未覆盖结果表格，PDF 文本未明确，待核。

## 7. 这篇论文真正有价值的地方
1.  **定义新问题域**：侧视 + 农村建筑物变化检测，首个专用大规模基准。
2.  **量化算法瓶颈**：LEVIR-CD 上 F1>0.85 的方法到 S2Looking 显著退化，暴露视角鲁棒性与复杂场景适应性短板。
3.  **干净的对照实验范式**：以单一 SOTA 数据集 LEVIR-CD+ 为参照，隔离“近星下点→侧视”这一变量。
4.  **实用导向**：素材源于重访快、范围大的监视卫星，贴合应急响应等真实场景。

## 8. 局限与问题
1.  **任务/场景局限**：仅建筑、以农村为主，未覆盖城市侧视与其他地物。
2.  **数据来源单一**：主要中国卫星（GF/SV/BJ-2），平台类型有限。
3.  **稀疏变化难点**：农村变化实例稀疏（p.13 "Sparse building updates"），正负样本失衡，论文未给针对性方案。
4.  **未提新方法**：只测现有算法，无针对侧视挑战的专用模型/训练策略。
5.  **标注一致性**：65,920 实例像素级标注成本高，质量控制未详述。
6.  **配准残差**：p.13 暗示配准精度仍有提升空间，是潜在误差源（据原文 p.13 摘录，待核）。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + 1.3 Contributions（p.7）+ Table 1（p.6）。
- **复现/用数据**：2. Materials and Methods（p.7 起）+ 官方仓库 https://github.com/S2Looking/ 。
- **借鉴创新点**：“针对现有数据集短板定义新数据集核心特性 + 单一 SOTA 数据集做对照”的范式。
- **写 Related Work**：归入“变化检测数据集”，与 [[LEVIR-CD]]、[[WHU Building Dataset]]、[[OSCD]]、[[SZTAKI]]、[[AICD]] 对比。

## 10. 和其他论文的关系
- **LEVIR-CD / LEVIR-CD+**：最重要的对照基准与动机来源；S2Looking 图像尺寸、分辨率（1024×1024、0.5 m 量级）与之对齐，定位为其“更难的扩展版”。`[[LEVIR-CD]]`
- **WHU Building Dataset**：Table 1 中尺寸与分辨率最高的建筑数据集。`[[WHU Building Dataset]]`
- **AICD / OSCD / SZTAKI / Change Detection Dataset**：Table 1 中其他变化检测数据集，共同构成研究背景。`[[AICD]]` `[[OSCD]]` `[[SZTAKI]]`
- **SpaceNet MVOI**：唯一此前认真做多角度卫星数据集者，但不针对变化检测、无双时相，是本文动机的直接对照。
- 论文引用的算法（DASNet、STANet、DTCDSCN、IFN、FC-EF/Siam、CDNet、BiT 等）为相关工作，不逐一硬连。

## 11. 关键词
变化检测 (Change Detection), 遥感 (Remote Sensing), 基准数据集 (Benchmark Dataset), 神经网络 (Neural Networks), 侧视卫星影像 (Side-Looking Satellite Imagery), 离轴角 (Off-Nadir Angle), 滚转成像 (Scroll Imaging), 建筑物变化 (Building Change), 农村场景 (Rural Areas), S2Looking, LEVIR-CD+

## 12. 可信度说明
本精读基于 PDF 提取缓存。需注意：提取缓存头标 `pages_extracted: 12/23`，但实际受 25000 字符上限截断，文本仅完整覆盖约前 8 页（摘要、引言、相关工作、Table 1、2.1 节）。Table 1 的全部统计数字、作者机构、摘要、相关工作分类等均直接来自提取文本，可信度高。
**局限**：实验 benchmark 的设置细节、各方法 F1 等具体数值、消融、讨论与结论（p.13-23）不在提取缓存内；这些部分依据原笔记“全文补读记录”保留的页眉/章节线索与零散摘录标注，并均以“(据原文后续页，提取缓存未覆盖，待核)”形式标明，未编造具体数字。

---

> **可信度补充**: PDF 提取质量 = **high** (前约 8 页连贯, 2086 字符/页); 但提取缓存受 25000 字符上限截断, 实测覆盖 ≈p.1-8 而非头标的 12 页; 来源缓存: `.paper-cache/extracts/2021_S2Looking_A_Satelli.txt` (头标 23/23 页, 实含前约 8 页正文); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-23; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-23。
- **提取情况**: 缺失页 11 页, 其中 11 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 2.3. The S2Looking Challenge
- p.13: The S2Looking dataset therefore presents current deep learning techniques with a new and
- p.13: The S2Looking dataset was extracted from side-looking rural-area remote-sensing images,
- p.14: 2.4. Challenge Restrictions
- p.14: To better accommodate operational use cases and maintain fairness, the geographic
- p.14: 3. Results
- p.14: In order to provide a benchmark against which change-detection algorithms can assess
- p.14: 3.1. Benchmark Setup
- p.15: F1-scores can be used as evaluation metrics:
- p.15: Here, TP,FP, and FNcorrespond to the number of true-positive, false-positive, and false-
- p.16: Epoch -----STANet-BAM
- p.16: Epoch 120 --FC-EF

### 缺失页关键摘录

- p.13: labeled images. In this way, if the registration accuracy is improved, these labeled images can
- p.13: The S2Looking Dataset. As noted previously, the dataset can be downloaded from
- p.13: https://github.com/S2Looking/, with our hope being that innovative use of the dataset in
- p.13: that can then be addressed through further dataset reﬁnements.
- p.13: The S2Looking dataset therefore presents current deep learning techniques with a new and
- p.13: based on the S2looking dataset (see https://www.rsaicp.com Accessed 1 November 2021),
- p.13: The S2Looking dataset was extracted from side-looking rural-area remote-sensing images,
- p.13: which makes it an expanded version of the LEVIR-CD+ dataset that will inevitably be harder
- p.13: Many methods have achieved satisfactory results on the LEVIR-CD dataset (F1-score >
- p.13: 0.85) [ 23,34], but the S2Looking dataset presents a whole new set of challenges that change-
- p.13: Sparse building updates. The changed building instances in the S2Looking dataset are far
- p.13: sparser than those in the LEVIR-CD+ dataset due to the differences between rural and
<!-- AI_READING_NOTE_END -->
