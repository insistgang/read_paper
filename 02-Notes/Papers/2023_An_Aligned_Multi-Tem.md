---
title: An Aligned Multi-Temporal Multi-Resolution Satellite Image Dataset for Change Detection Research
authors:
  - "Rahul Deshmukh"
  - "Constantine J. Roros"
  - "Amith Kashyap"
  - "Avinash C. Kak"
year: 2023
venue: "arXiv"
doi: 
pdf: [[2023_An_Aligned_Multi-Tem.pdf]]
primary_topic: S_变化检测_ChangeDetection
topics:
  - "S_变化检测_ChangeDetection"
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2023_An_Aligned_Multi-Tem.txt
---

# An Aligned Multi-Temporal Multi-Resolution Satellite Image Dataset for Change Detection Research

## 基本信息
- **PDF**: [[2023_An_Aligned_Multi-Tem.pdf]]
- **primary_topic**: `S_变化检测_ChangeDetection`
- **topics**: `S_变化检测_ChangeDetection`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | An Aligned Multi-Temporal Multi-Resolution Satellite Image Dataset for Change Detection Research |
| **作者** | Rahul Deshmukh; Constantine J. Roros; Amith Kashyap; Avinash C. Kak（Purdue University） |
| **发表时间** | 2023（arXiv:2302.12301v2，2023-02-27，cs.CV） |
| **刊物/会议** | arXiv |
| **DOI** | 未明确（arXiv 标识：2302.12301v2） |

## 摘要

**英文原摘要（据 PDF 提取文本整理，已修复空格/连字符断裂、剔除杂入的版面字符）：**

> This paper presents an aligned multi-temporal and multi-resolution satellite image dataset for research in change detection. We expect our dataset to be useful to researchers who want to fuse information from multiple satellites for detecting changes on the surface of the earth that may not be fully visible in any single satellite. The dataset we present was created by augmenting the SpaceNet-7 dataset [22] with temporally parallel stacks of Landsat and Sentinel images. The SpaceNet-7 dataset consists of time-sequenced Planet images recorded over 101 AOIs (Areas-of-Interest). In our dataset, for each of the 60 AOIs that are meant for training, we augment the Planet datacube with temporally parallel datacubes of Landsat and Sentinel images. The temporal alignments between the high-res Planet images, on the one hand, and the Landsat and Sentinel images, on the other, are approximate since the temporal resolution for the Planet images is one month — each image being a mosaic of the best data collected over a month. Whenever we have a choice regarding which Landsat and Sentinel images to pair up with the Planet images, we have chosen those that had the least cloud cover. A particularly important feature of our dataset is that the high-res and the low-res images are spatially aligned together with our MuRA framework presented in this paper. Foundational to the alignment calculation is the modeling of inter-satellite misalignment errors with polynomials as in NASA's AROP [8] algorithm. We have named our dataset MuRA-T for the MuRA framework that is used for aligning the cross-satellite images and "T" for the temporal dimension in the dataset.

**中文翻译：**

> 本文提出一个用于变化检测研究的、时间与分辨率均经过对齐的多卫星图像数据集。我们期望该数据集对那些希望融合多颗卫星信息、以检测单一卫星无法完整观测到的地表变化的研究者有所帮助。该数据集通过为 SpaceNet-7 数据集补充时间上平行的 Landsat 与 Sentinel 影像栈构建而成。SpaceNet-7 由覆盖 101 个 AOI（兴趣区域）的时序 Planet 影像组成；在我们的数据集中，对其中用于训练的 60 个 AOI，我们为 Planet 数据立方体补充了时间平行的 Landsat 与 Sentinel 数据立方体。由于 Planet 影像的时间分辨率为一个月（每幅图像是该月内最佳数据的镶嵌合成），高分辨率 Planet 影像与 Landsat/Sentinel 影像之间的时间对齐是近似的。在可以选择与 Planet 影像配对的 Landsat、Sentinel 影像时，我们优先选取云量最少者。本数据集的一个重要特征在于：高分辨率与低分辨率影像通过本文提出的 MuRA 框架在空间上完成了对齐。对齐计算的基础，是仿照 NASA 的 AROP 算法、用多项式对卫星间误配准误差建模。我们将数据集命名为 MuRA-T——"MuRA"取自用于跨卫星图像对齐的 MuRA 框架，"T"指数据集的时间（temporal）维度。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：卫星是识别和追踪地表显著变化的丰富数据源，相关需求覆盖科学家、城市规划者、灾害评估与减灾规划人员等。检测变化至少需要事件前后两幅图像；若要理解变化的时间演化，则需要同一地理区域的时序图像。Planet 数据使得在中等分辨率（约 4m）下构建这种时序成为可能，SpaceNet-7 已证明该分辨率足以识别和追踪城市建筑物层面的变化。
- **作者独特的研究兴趣**：作者不仅关心建筑物本身，更关心建筑物所处的**地理上下文**——即建筑周边陆地（landmasses）发生的变化与纯城市场景中的建筑变化同等重要。要捕捉这种更宏观的上下文变化，需要 Landsat、Sentinel 这类更低分辨率卫星提供的多尺度信息。
- **之前方法/数据集的问题**：现有数据集要么是时间静态的（SpaceNet 各挑战、DeepGlobe、off-nadir WorldView-2 等，多用于建筑/道路提取），要么虽含时序但只来自单一卫星（如 EarthNet 2021 只含 Sentinel-2，xBD 只给灾前灾后两期），缺少一个**多卫星、多分辨率、且时间与空间都对齐**的数据集。
- **核心矛盾**：要融合不同卫星的互补信息（高分辨率细节 + 低分辨率宏观上下文）做更全面的变化检测，但不同卫星影像在空间分辨率和时间戳上存在固有差异；变化检测对哪怕极细微的配准误差都很敏感，因此需要一个经过精心时空对齐的基准数据集。

## 关键贡献

1.  **提出 MuRA-T 数据集**：据作者所知，这是**首个**可用于变化检测研究的、时间与空间均对齐的多卫星数据集。它在 SpaceNet-7 的 60 个训练 AOI 上，为每个 Planet 时间步补充了时间平行的 Landsat-8 与 Sentinel-2 数据立方体。
2.  **提出 MuRA（Multi-Resolution Alignment）对齐框架**：用于对齐不同分辨率卫星图像的算法框架，包含下采样、（超分/图到图翻译）上采样、混合三条处理路径，采用即插即用（plug-n-play）设计便于替换特征提取/匹配方法。
3.  **多项式误配准建模 + 鲁棒估计**：仿照 NASA AROP，用多项式对跨卫星误配准误差建模；通过捆集调整（bundle adjustment）估计多项式系数，并以 RANSAC 迭代剔除外点、寻找最大内点集，最终（据论文第 7 节）达到**亚像素级**对齐精度。
4.  **完整的数据获取与时间配对流程**：用 F-MASK 做云检测，按"同月内云量最少"原则为每幅 Planet 影像配对最佳 Landsat 与 Sentinel 影像；Landsat 经 AWS Open Data 注册表（WRS2 path/row）获取，Sentinel-2 经 Google Cloud Platform + BigQuery API 获取，均通过自定义 Python 脚本自动化。

> 注：原笔记列出的"5 条贡献"中第 1、5 条均强调"首个时空对齐多源数据集"，本质重复，此处已合并，与提取文本的表述（"to the best of what we know, MuRA-T is the first..."）一致。

## 方法

- **整体框架**：方法可分两部分——（A）**时间配对**（构建时间平行的 Landsat/Sentinel 数据立方体，第 5 节）；（B）**空间对齐**（MuRA 框架，第 6 节）。
- **输入输出**：
    - **输入**：SpaceNet-7 中的 Planet 时序数据立方体（RGB，约 4m，每月一幅、跨约 24 个月、月份不一定连续）；以及与每幅 Planet 影像时间大致对应的 Landsat-8、Sentinel-2 影像。
    - **输出**：时间平行、空间对齐的 Planet / Landsat-8 / Sentinel-2 三个数据立方体（如论文 Fig.1 所示三个并列立方体）。
- **时间配对（第 5 节）**：
    1.  用每个 AOI 的经纬度 (Lat/Long) 角点坐标，与 NASA 提供的 WRS2 path/row shapefile 比对，定位对应的 Landsat 瓦片（自定义 Python 脚本自动化）；再通过 AWS Open Data 注册表的元数据列表拿到 URL，用 AWS CLI 下载。由于 AOI 远小于 Landsat 瓦片，下载的 Landsat 图像被**裁剪**到 AOI 范围。
    2.  Sentinel-2 以类似方式经 Google Cloud Platform + BigQuery API 检索与 AOI 日期/位置匹配的影像并下载。
    3.  用 **F-MASK 算法**做云检测，在与某 Planet 月份匹配的候选中选取**云量最少**者完成配对。
- **空间对齐（MuRA 框架，第 6 节）**：
    1.  **确定工作分辨率**：先把高分辨率图像**下采样**到输入中最低的分辨率（即"最小公分母"路径）。例：对齐 4m Planet 与 15m Landsat 时，先把 Planet 下采样到 15m。MuRA 框架另有两条路径——用超分/图到图翻译网络把低分上采样到高分；或上采样+下采样混合（用于分辨率差异过大的情形）——但**当前发布版 MuRA-T 只用了第一条（下采样）路径**。
    2.  **特征提取与匹配（得到 tie-points）**：在重采样后的图像上用 **FAST+VGG** 或 **SuperPoint+SuperGlue** 提取并匹配特征点；框架的即插即用设计便于替换匹配方法，作者选这两种是因为效果最好（细节在第 6.3 节，提取缓存未覆盖）。
    3.  **误配准建模与系数估计**：用**多项式模型**表示两幅图像间的几何变换误差（多项式次数可按所需精度调整），通过**捆集调整**估计多项式系数（多项式模型的具体形式在第 6.2 节，提取缓存未覆盖）。
    4.  **鲁棒估计**：捆集调整中集成 **RANSAC** 迭代剔除外点，寻找最大内点 tie-point 集。
    5.  **图像重采样**：用估计出的多项式模型把待配准的低分辨率图像重采样为对齐图像。
- **与已有方法的关系（第 2.2 节）**：处理跨视角图像时常用 RPC（有理多项式系数）相机模型 + 捆集调整；RPC 有 78 个多项式系数，但 Grodecki & Dial 证明仅估计 RPC 的偏置校正项即可纠正卫星图像误配准。而当待对齐图像都是**正下视（nadir）**——如 Planet 与低分 Landsat/Sentinel——时，误配准更易用仿射变换/多项式扭曲（即 NASA AROP 思路）建模；本文采用后者。
- **论文类型（数据集 + 框架类）小结**：
    - **任务**：为变化检测构建多源、多分辨率、时空对齐数据集。
    - **数据模态**：多光谱卫星图像（Planet RGB ~4m；Landsat-8 多波段；Sentinel-2 多波段）。
    - **对齐度量**：以最大内点集上的**重投影误差**作为相对对齐精度度量。

## 实验

- **数据集**：MuRA-T，即 SpaceNet-7 的 60 个训练 AOI 增强而成（SpaceNet-7 共 101 个 AOI，60 训练、其余测试/验证；当前 MuRA-T 仅用训练这 60 个）。每个时间栈平均跨约 24 个月，Planet 为 RGB 正下视、约 4m。SpaceNet-7 每幅图含 1 万~2 万个建筑标注及 footprint mask、"unusable data mask"。
- **分辨率事实（论文 Tab.1/Tab.2，在提取文本内）**：
    - **Landsat-8**：多数波段 30m；全色（Panchromatic）波段最高为 **15m**；TIRS 热红外 1/2 为 100m。
    - **Sentinel-2**：RGB（蓝/绿/红）最高为 **10m**；VNIR 多波段 20m；超蓝、SWIR(1373.5/945.1nm) 等为 60m。
- **评价指标**：**重投影误差（reprojection error）**，定义为两幅待对齐图像最大内点 tie-point 集上对应点的距离；属于"相对精度"度量（仅相对于彼此，而非相对于地面真实地物）。
- **主结果**：论文（第 7 节）声称所有基于重投影误差的对齐精度均达到**亚像素级（sub-pixel level）**。**具体的重投影误差数值在第 7 节，提取缓存（前约 25000 字符）未覆盖该节，待核。**
- **定性展示**：Fig.3 给出 Meridian, Idaho AOI 的前 10/24 幅 Planet 影像及其对齐后的 Landsat、Sentinel 影像（图细节超出提取文本范围）。
- **对比方法 / 消融 / 泛化 / 速度参数量**：提取文本中未见相应内容（这是一篇数据集论文，正文主体为构建流程与对齐方法）。

## 局限

1.  **仅覆盖训练子集**：当前 MuRA-T 只基于 SpaceNet-7 的 60 个训练 AOI，测试/验证 AOI 的增强尚未提供。
2.  **只有相对对齐精度，缺绝对地理定位精度**：当前只用重投影误差（相对精度）；论文明确指出未来版本将结合**地面控制点（GCP）**给出绝对精度。作者解释暂未纳入 USGS Landsat GCP 的原因：那些 GCP 是针对旧的 30m Landsat-7 数据的邻域描述，能否超分到 Landsat-8 的 15m 仍是开放问题。
3.  **只实现了下采样这一条对齐路径**：MuRA 框架虽支持上采样（超分/图到图翻译）和混合策略，但发布版数据集只用了"把 Planet 下采样到低分辨率"这一路径，可能损失高分辨率信息。
4.  **依赖上游数据**：质量受 SpaceNet-7、以及 Landsat/Sentinel 公开数据的可用性与质量制约；时间对齐本身是"近似"的（Planet 为一个月镶嵌）。
5.  **WorldView 暂未纳入**：作者已用 MuRA 把 Landsat/Sentinel 与高分 WorldView 对齐，但 WorldView 尚不属于 MuRA-T。
6.  **复现细节**：第 6.2（多项式模型形式）、6.3（特征匹配细节）、7（对齐结果数值）等关键工程参数在提取缓存中未覆盖，复现需查阅原文这些章节及补充材料。

## 个人评论

1.  **填补真实空白的数据资源**：多源、多分辨率、时空双对齐的变化检测基准此前确实缺位。MuRA-T 把繁琐的多卫星数据获取、时间配对、跨分辨率配准都做好，让研究者能直接专注于"多源融合变化检测"这一更难的算法问题。
2.  **问题视角的拓展有价值**：把变化检测从"单一高分建筑变化"扩展到"建筑 + 周边陆地的多尺度地表变化"，是一个能催生更复杂问题表述的方向，数据集为此提供了实证基础。
3.  **方法上是经典与现代的务实结合**：多项式 + 捆集调整 + RANSAC 是成熟的几何配准范式，论文将其与深度特征匹配（SuperPoint+SuperGlue）以即插即用方式拼装，工程上可借鉴性强，但方法本身的新颖性有限——其主要贡献在"数据集"而非"对齐算法"。
4.  **当前版本完成度偏初步**：只有训练 60 个 AOI、只走下采样路径、对齐精度只有相对值且第 7 节数值未在可见文本中给出，更像是一个"v2 预印本阶段"的数据集发布，后续版本（绝对精度、上采样路径、WorldView、测试集）才是其价值能否充分兑现的关键。

### 使用建议

- **如果快速了解**：读**摘要**、**引言（第 1 节）**、以及第 2 节相关数据集对比，把握"为什么需要多源时空对齐数据集"与 MuRA-T 的定位（论文无独立结论段）。
- **如果复现/使用数据集**：精读第 5 节（数据获取：AWS/WRS2、GCP/BigQuery、F-MASK 配对）与第 6 节（MuRA 对齐：下采样→特征匹配→多项式建模→RANSAC→重采样），并查阅第 6.2/6.3/7 节及 SpaceNet-7 原文。
- **如果借鉴创新点**：学习其"时间配对 + 跨分辨率空间对齐"的完整数据集构建流水线，以及把深度特征匹配嵌入经典多项式几何模型的即插即用框架设计。
- **如果写 related work**：可归入"多源遥感数据集"或"卫星图像配准/对齐"，突出其在跨卫星、跨分辨率、时空双对齐上的独特性（区别于单源时序的 EarthNet 2021、仅两期的 xBD、时间静态的 SpaceNet 系列）。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[S_变化检测_ChangeDetection]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇**遥感变化检测方向的数据集（dataset）+ 对齐框架（framework）论文**，作者来自 Purdue University（arXiv:2302.12301v2, 2023-02-27, cs.CV）。核心工作：构建并发布 **MuRA-T**——首个时间平行、空间对齐的多卫星（Planet / Landsat-8 / Sentinel-2）、多分辨率变化检测数据集，并配套提出 **MuRA（Multi-Resolution Alignment）** 跨卫星跨分辨率对齐框架。它适合放在 **S_变化检测_ChangeDetection** 主题下，子方向是"多源数据融合 + 变化检测数据集"。

## 2. 一句话总结
本文通过为 SpaceNet-7 的 60 个训练 AOI 补充时间平行的 Landsat-8、Sentinel-2 数据立方体、并用 MuRA 框架（多项式 + 捆集调整 + RANSAC）把它们与 Planet 影像做亚像素空间对齐，构建出首个时空双对齐的多源多分辨率变化检测数据集 MuRA-T。

## 3. 背景与问题
- **数据基础已成熟，但视角受限**：Planet 数据让中分辨率（约 4m）时序成为可能，SpaceNet-7 证明该分辨率足以追踪城市建筑变化（每 AOI 每月一幅、跨约 24 月）。但作者的兴趣超出建筑本身，延伸到建筑周边陆地的多尺度地表变化，这需要 Landsat（多数 30m、全色 15m）、Sentinel-2（RGB 10m、VNIR 20m）的宏观上下文。
- **现有数据集的缺口**：SpaceNet 系列、DeepGlobe、off-nadir WorldView-2 多为时间静态、用于建筑/道路提取；EarthNet 2021 虽时序但只含 Sentinel-2 单源；xBD 只给灾前灾后两期。没有一个数据集同时满足"多卫星 + 多分辨率 + 时间对齐 + 空间对齐"。
- **核心矛盾**：变化检测对配准误差极敏感，而多卫星影像分辨率与时间戳天然不一致，需要精心对齐的统一基准——这正是 MuRA-T 要填补的空白。

## 4. 核心贡献
1.  **MuRA-T 数据集**：据作者所知，首个可用于变化检测研究的时空双对齐多卫星数据集；在 SpaceNet-7 的 60 个训练 AOI 上为每个 Planet 时间步补充时间平行的 Landsat-8、Sentinel-2 数据立方体（Fig.1 的三个并列立方体）。
2.  **MuRA 对齐框架**：含下采样 / 上采样（超分、图到图翻译）/ 混合三条路径，即插即用设计；当前 MuRA-T 仅用下采样路径。
3.  **多项式误配准建模 + 鲁棒估计**：仿 NASA AROP 用多项式建模跨卫星误配准，捆集调整估系数、RANSAC 剔外点，达亚像素精度（第 7 节）。
4.  **可复现的数据获取与时间配对流水线**：AWS Open Data + WRS2（Landsat）、GCP + BigQuery（Sentinel-2）、F-MASK 云检测 + "同月最少云量"配对，均经 Python 脚本自动化。

## 5. 方法详解
- **两阶段**：时间配对（第 5 节）→ 空间对齐（第 6 节 MuRA）。
- **时间配对**：用 AOI 经纬度角点比对 NASA WRS2 path/row shapefile 定位 Landsat 瓦片，经 AWS Open Data 元数据拿 URL、AWS CLI 下载，并按 AOI **裁剪**（AOI 远小于 Landsat 瓦片）；Sentinel-2 经 GCP + BigQuery 检索下载；F-MASK 云检测后选同月云量最少者配对。Planet 的时间分辨率为月（每幅是该月最佳数据的镶嵌），故时间对齐是"近似"的。
- **空间对齐（MuRA-T 所用路径，Fig.2）**：
    1.  下采样高分图像到工作分辨率（输入中最低分辨率，如把 4m Planet 降到 15m Landsat）；
    2.  在重采样图像上用 **FAST+VGG** 或 **SuperPoint+SuperGlue** 提取并匹配特征点得 tie-points；
    3.  对 tie-points 做**捆集调整**，估计**多项式模型**系数（多项式次数随精度需求可调）；
    4.  捆集调整内嵌 **RANSAC** 迭代剔外点、求最大内点集；
    5.  用估出的多项式把低分图像**重采样**为对齐图像。
- **几何模型选择依据（第 2.2 节）**：跨视角对齐常用 RPC（78 系数）+ 捆集调整，但 Grodecki & Dial 表明只估 RPC 偏置项即可纠偏；而本文图像皆为正下视（nadir），误配准更适合用仿射/多项式扭曲（AROP 思路）建模，故采用之。
- **提取缓存未覆盖**：多项式模型的具体形式（第 6.2 节）、特征匹配实现细节（第 6.3 节）超出提取文本范围，待核。

## 6. 实验与结果
- **数据集规模**：SpaceNet-7 共 101 AOI（60 训练 / 其余测试验证），MuRA-T 当前仅基于 60 训练 AOI；每栈约 24 月、Planet RGB 正下视约 4m；SpaceNet-7 每幅含 1 万~2 万建筑标注、footprint mask、unusable data mask。
- **分辨率（Tab.1/Tab.2，在提取文本内）**：Landsat-8 多数 30m、全色 15m、TIRS 100m；Sentinel-2 RGB 10m、VNIR 20m、部分 60m。
- **评价指标**：重投影误差（最大内点集上对应点距离），属相对精度。
- **主结果**：论文第 7 节声称所有重投影误差均达**亚像素级**。**具体数值在第 7 节，提取缓存（前 ~25000 字符）未覆盖该节，待核（据原文后续页，提取缓存未覆盖）。**
- **对比 / 消融 / 泛化 / 效率**：提取文本中未见——本文为数据集论文，主体是构建流程与对齐方法描述。

## 7. 这篇论文真正有价值的地方
1.  **填补真实空白**：时空双对齐的多源多分辨率变化检测基准此前不存在；省去研究者大量数据获取与预处理负担。
2.  **拓展问题边界**：把变化检测从"单源高分建筑变化"推向"多源多尺度地表变化（建筑 + 周边陆地）"。
3.  **可复用的工程流水线**：AWS/WRS2、GCP/BigQuery、F-MASK 配对、即插即用对齐框架，对其他多源遥感配准任务有直接参考价值。
4.  **经典 + 现代的务实组合**：多项式几何模型嵌入深度特征匹配（SuperPoint+SuperGlue），展示现代遥感处理中经典稳健配准范式的延续。

## 8. 局限与问题
1.  仅覆盖 SpaceNet-7 的 60 个训练 AOI，测试/验证 AOI 增强未提供。
2.  仅有相对精度（重投影误差），缺基于 GCP 的绝对地理定位精度；作者说明 USGS GCP 是旧 30m Landsat-7 邻域描述，能否超分到 15m 是开放问题。
3.  只实现下采样这一条对齐路径，上采样/混合路径未用于发布版，可能损失高分信息。
4.  时间对齐本质是近似（Planet 为月镶嵌）；质量受上游 SpaceNet-7、Landsat/Sentinel 数据制约。
5.  WorldView 已用 MuRA 对齐但尚未纳入 MuRA-T。
6.  第 6.2/6.3/7 节关键细节与数值在提取缓存中缺失，复现需查原文。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要、第 1 节引言、第 2 节数据集对比，把握定位与动机。
- **复现/用数据**：精读第 5 节（数据获取）与第 6 节（MuRA 对齐），并补读第 6.2/6.3/7 节与 SpaceNet-7 原文。
- **借鉴创新**：学习"时间配对 + 跨分辨率空间对齐"完整流水线，以及深度特征匹配 + 多项式几何模型的即插即用框架。
- **写 related work**：归入"多源遥感数据集"或"卫星图像配准/对齐"，强调其相对 EarthNet 2021（单源时序）、xBD（两期）、SpaceNet 系列（时间静态）的独特之处。

## 10. 和其他论文的关系
基于提取文本中明确引用/比较的工作：
- **SpaceNet-7 [22]**：MuRA-T 的**基底数据集**，全部增强都基于它。
- **NASA AROP [8]**：跨卫星误配准多项式建模的**思路来源**。
- **SuperPoint [5] + SuperGlue [17]、FAST+VGG [15,19]**：MuRA 中使用的特征提取/匹配方法。
- **RANSAC [7]、bundle adjustment [20]**：鲁棒估计与系数优化的核心算法；RPC 模型相关工作（Grodecki & Dial [9]）作为对照。
- **F-MASK [24]**：云检测算法。
- 作为相关/对照数据集被讨论：**SpaceNet 系列 [6]、DeepGlobe [4]、off-nadir WorldView-2 [23]、SpaceNet-6（光学+SAR）[18]、xBD [10]、EarthNet 2021 [14]**。

## 11. 关键词
变化检测，多时相，多分辨率，多源卫星融合，数据集，MuRA / MuRA-T，SpaceNet-7，Planet，Landsat-8，Sentinel-2，图像对齐 / 配准，多项式模型，AROP，捆集调整，RANSAC，SuperPoint+SuperGlue，F-MASK，重投影误差，亚像素精度。

## 12. 可信度说明
本精读笔记**主要基于 PDF 提取文本**，覆盖摘要、第 1 节引言、第 2 节文献综述、第 3 节 SpaceNet-7、第 4 节 Landsat/Sentinel 波段属性（含 Tab.1/Tab.2）、第 5 节数据获取、第 6.1 节 MuRA 路径。
- **提取覆盖范围**：提取缓存为原文前约 25000 / 41319 字符（约前 6~7 页内容，止于第 6.1 节末 / Fig.3 题注），**第 6.2 节（多项式模型形式）、第 6.3 节（特征匹配细节）、第 7 节（对齐结果数值）未被覆盖**。因此"亚像素精度"为论文自述（引言已声明，第 7 节细化），但**具体重投影误差数值在提取文本中无法核实，已标注待核**。
- **图表**：Fig.1（三立方体）、Fig.2（MuRA 计算路径）、Fig.3（Idaho AOI 定性展示）依文本题注还原，未见图内细节。
- **零编造校验**：所有数字（101/60 AOI、约 4m、24 月、15m/30m/100m Landsat、10m/20m/60m Sentinel、1 万~2 万建筑标注、78 RPC 系数等）均直接出自提取文本 Tab/正文。

---

> **可信度补充**: PDF 提取质量 = **high (覆盖不全)** — 单页字符密度高、文本清晰，但 max_chars=25000 截断，仅覆盖原文约前 6~7 页（含至第 6.1 节），第 6.2/6.3/7 节及具体对齐误差数值未进入提取缓存，相关条目已标注"待核"; 来源缓存: `.paper-cache/extracts/2023_An_Aligned_Multi-Tem.txt` (标注 9/9 页, 实际 25260 字符 / 原文 41319 字符); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
