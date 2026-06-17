---
title: Ren Y F Li Z Q and Zhang S H. 2024. Survey of visualization methods for multiscene visual cue information in immersive environments
authors:
  - "任洋甫"
  - "李志强"
  - "张松海"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.221147
pdf: [[cjig_计算机视觉_沉浸式环境和多场景中的视觉提示信息综述.pdf]]
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
extract_cache: .paper-cache/extracts/cjig_计算机视觉_沉浸式环境和多场景中的视觉提示信息综述.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/21 pages"
---
# 沉浸式环境中多场景视觉提示信息可视化方法综述

## 基本信息
- **PDF**: [[cjig_计算机视觉_沉浸式环境和多场景中的视觉提示信息综述.pdf]]
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 沉浸式环境中多场景视觉提示信息可视化方法综述 (Survey of visualization methods for multiscene visual cue information in immersive environments) |
| **作者** | 任洋甫¹·²; 李志强³*; 张松海¹·² |
| **单位** | 1. 青海大学计算机技术与应用系; 2. 清华大学计算机科学与技术系; 3. 国防大学联合作战学院 |
| **发表时间** | 2024 (29卷1期, pp.0001-0021; 收稿 2022-12-22) |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics) |
| **DOI** | 10.11834/jig.221147 |
| **基金** | 国家自然科学基金 (62132012); 清华-腾讯互联网创新技术联合实验室; 青海大学中青年科研基金 (2019-QGY-17) |

## 摘要

**英文原摘要（据 PDF 提取文本整理, 修复空格与连字符断裂、剔除杂入的版式数字）：**

> The immersive environment presents a near-real environment experience to users through technologies such as virtual reality (VR). Virtual reality is a simulated environment that generates the natural world through computers, providing users with a rich immersion experience, interactivity, and imagination. In virtual reality, the eyes are the window for viewing the scene and a meaningful way to interact with the virtual world. Virtual reality is a very convenient way for users to obtain information about the location through visual means. The interaction of the scene enhances the users' perception. Augmented reality (AR) places virtual information in a natural setting, and users can interact with the virtual information in the actual location. To understand the application research of visual cue information in different immersive scenarios such as virtual reality, combined with the relationship between visual information cue methods, this paper mainly distinguishes information according to the information display position, function use, and actual application field, and summarizes and discusses recent studies of information visualization methods for visual cues in immersive multiscene environments. First, the prompt information outside the field of view is analyzed. The methods for visual prompt information outside the field of view can be divided into overview+detail and focus+context, and are discussed separately for 2D and 3D scenarios. The situation within the field of view focuses on label placement around the model and label layout in the scene, aiming to reduce occlusion/overlap and lower users' cognitive load. Considering the use function of visual prompt information, fast visual information added in VR helps users know their position or scene information during roaming (e.g., map navigation, attention guidance). In practical applications, problems encountered in panoramic videos, as well as industrial and life scenarios (such as applying video barrage in panoramic videos), are discussed. Some challenges remain in six aspects: (1) adapting prompt methods to multi-size 2D screens; (2) better out-of-field prompting in different 3D scenes; (3) tag placement and layout in the scene; (4) map navigation and attention-guidance accuracy with low impact on immersion; (5) enhancing immersion and reducing dizziness when watching videos in VR; (6) good interaction with users in industrial production, education, and entertainment. This survey shows in more detail the research prospects and development directions of visual cue information in immersive environments and multiscenes.

**中文翻译：**

> 沉浸式环境通过虚拟现实 (VR) 等技术为用户呈现趋近真实的环境体验。VR 由计算机模拟现实世界，为用户提供丰富的沉浸感、交互性与想象力；在 VR 中，眼睛既是观看场景的窗口，也是与虚拟世界交互的重要途径，用户可便捷地通过视觉获取位置信息，场景交互增强用户感知。增强现实 (AR) 则将虚拟信息放置于真实场景中，用户可在真实位置与虚拟信息交互。为厘清视觉提示信息在 VR 等沉浸式场景中的研究并探究其本源，本文按**信息显示位置、使用功能、实际应用领域**进行区分，综述近年来沉浸式多场景环境下视觉提示信息的可视化方法。首先分析视野外提示信息，将其分为**概览+细节 (overview+detail)** 与**聚焦+上下文 (focus+context)** 两类，并分别针对二维与三维场景讨论；视野内则聚焦于模型周边标签放置与场景标签布局，目的是减少遮挡/重叠、降低认知负荷。在使用功能上，VR 中快速加入的视觉信息帮助用户在漫游中获知位置或场景信息（地图导航、注意力引导）。在实际应用中，讨论了全景视频、工业与生活场景遇到的问题及解法（如将视频弹幕用于全景视频）。最后总结六大挑战：(1) 适配多尺寸二维屏幕；(2) 改进不同三维场景下的视野外提示；(3) 场景中标签放置与布局；(4) 提升地图导航与注意力引导精度、降低对沉浸感的破坏；(5) 增强 VR 观影沉浸感、减少眩晕；(6) 工业/教育/娱乐中视觉提示与用户的良好交互。本文藉此更细致地展示视觉提示信息在沉浸式环境与多场景中的研究前景与发展方向。

> **来源**: 据 PDF 提取文本整理。

**关键词**：沉浸式环境；虚拟现实 (VR)；增强现实 (AR)；多场景；视觉提示信息；全景视频；注意力引导

## 研究背景与动机

- **为什么要做**：沉浸式环境（VR/AR）为用户创造趋近现实的体验，可应用于教育、医疗、工业、娱乐等行业。自 2014 年 Oculus Rift、HTC Vive 等消费级头戴显示器 (HMD) 商业化，VR 进入新时代。在 VR 中**眼睛既是观看窗口也是交互途径**，且用户通过视觉获取的信息占全部信息获取比例接近 **70%~80%**，因此视觉提示信息方法直接决定用户体验。
- **之前方法的问题**：
    1.  受**硬件视野 (field of view, FOV) 受限**，用户通过设备（HMD、CAVE、HoloLens/iPad/iPhone 等）观看场景时观察视角受限，视野外信息不可见。
    2.  二维场景的屏幕外提示方法（如 Halo、Wedge）迁移到三维 VR/AR 时需改进适配，且信息显示位置需从"视野四周"向"视野中央"调整。
    3.  视野内标签信息附着在被标注物体附近，容易产生**重叠、遮挡**，增加用户观察时的认知负荷。
    4.  全景视频/VR 电影 (CVR) 中用户自行决定观看方向，传统注意力引导方法（如固定字幕）不再适用，需新技术引导视线、避免错过重点。
- **核心矛盾**：如何在**保证或增强沉浸感**的前提下，**高效、舒适、准确**地传递视觉提示信息，辅助用户认知与交互（兼顾减少对沉浸感的破坏）。

## 关键贡献

> 本文是综述，"贡献"指其组织框架与系统梳理，非新算法。

1.  **三维度分类框架**：按**信息显示位置（视野外/视野内）、使用功能（地图导航/注意力引导）、实际应用领域（全景视频/工业生活）** 三个维度，对沉浸式多场景视觉提示信息研究进行系统分类（图 1 给出研究方向汇总）。
2.  **二维↔三维迁移分析**：详细分析视觉提示方法从二维平面显示设备迁移到三维 VR/AR 场景的继承、改进与异同（如显示位置由视野四周向视野中央调整、可增加颜色编码深度、可叠加声音/触觉多模态）。
3.  **系统梳理视野外提示方法**：区分**概览+细节**与**聚焦+上下文**两大范式，并以**表 1（二维 6 种方法）和表 2（三维 11 种方法）** 汇总形状、屏幕位置与文献来源，对比 Citylight、Halo、Wedge、Eyesee 360、3D Radar 等的原理与效果。
4.  **系统梳理视野内布局方法**：从**模型周边标签放置**与**场景信息标签布局管理**两个角度综述视图管理 (view management) 技术，覆盖几何约束、立体视差分离、图像驱动（显著性/边缘）、整数线性规划等思路。
5.  **整合功能与应用**：综述视觉提示信息在**地图导航、注意力引导**等功能，以及**全景视频/VR 电影 (CVR)、工业辅助、虚拟旅游**等应用中的进展（据原文后续页, 提取缓存仅覆盖到 p.12, 应用章节细节待核）。
6.  **明确六大挑战**：摘要明确列举六个未来研究方向（见"摘要"末段），为后续研究指明方向。

## 方法

这篇论文是**综述**，核心"方法"是分类框架与对已有研究的归纳，而非新算法。其梳理的技术体系如下：

- **整体框架（图 1）**：将视觉提示信息研究分为四条主线——**视野外信息显示、视野内信息显示、使用功能（导航/注意力引导）、实际应用**，每条主线下区分二维与三维场景讨论。

- **视野外信息提示方法（第 2 节）**：因 FOV 受限，需用代理元素提示视野外目标的位置、方向、数量、距离。两大范式：
    - **概览+细节 (overview+detail)**：将周围环境全部信息显示在用户面前（如视野中加缩略地图），便于获取周边信息，但显示信息量过多会影响观察。
    - **聚焦+上下文 (focus+context)**：通过鱼眼视图，用箭头、三角、圆形等符号在屏幕边缘提示视野外环境，识别效率高、占屏少，是二维场景主流方法。
    - **二维场景具体方法（表 1）**：
        - **Citylight**（Zellweger 等, 2003, UIST 2002）：沿窗口边界用**发光线条**提示屏幕外内容的位置与占内容多少，可配滚动条查看。
        - **Halo**（Baudisch 和 Rosenholtz, 2003, CHI 2003）：针对小手机屏，以视野外目标为圆心绘制**光圈/圆弧**，可见弧度提示方向与距离，叠加不产生遮挡。
        - **EdgeRadar**（Gustafson 和 Irani, 2007, CHI 2007）：用**屏幕四周边缘的代理信息（圆点）** 表示屏幕外移动目标，用代理的位置与数量判断真实信息的位置与数量。
        - **Wedge**（Gustafson 等, 2008, CHI 2008）：用**锐角等腰三角形**，尖端与屏幕外目标重合，另两角在屏幕上，两条边指向目标传达方向+距离；利用符号相互排斥避免视觉重叠（解决 Halo 信息多时易重叠的问题）。
        - **EdgeSplit**（Hossain 等, 2012, MobileHCI 2012）：受 EdgeRadar 启发，将屏幕四周代理区域以不同形状多边形区分，便于用户快速选择屏幕外对象。
        - **Personalized Compass / 个性化指南针**（Miau 和 Feiner, 2016, CHI 2016）：针对智能手表小屏，用**参考点+指针**传达到 POI 的方向与距离，提示位于**屏幕中央**（表 1 中唯一不在屏幕四周者），并支持点击放大等手动交互。
        - **对比研究**：Burigat 等 (2006) 比较 Halo/Arrows/Citylight 的空间认知任务有效性；Burigat 和 Chittaro (2011)、Burigat 等 (2012) 对比缩放 Arrows、Wedge、缩略图 (overview+detail)，发现缩略图整体效果较好但受屏幕大小与可提示信息数量限制。Ion 等 (2013) 提出折纸式 Canyon，在大屏优于 Wedge、可容纳更丰富上下文，但小屏占位过多。
    - **三维场景具体方法（表 2，11 种）**：相较二维可增加更多维度（颜色编码深度、声音/触觉多模态）。
        - **Eyesee 360**（Gruenefeld 等, 2017a, SUI 2017）：将用户水平 360°、垂直 180° 范围内物体以**彩色圆点**显示在**视野中央**方框周围，颜色编码目标与用户的距离，实验表明搜索效率更高。后续 Gruenefeld 等 (2018a) 针对小 FOV 改进（减少展示信息量、压缩外围显示）。
        - **AroundPlot**（Jo 等, 2011, Computers & Graphics 2011）：用二维正交鱼眼坐标将周围三维空间信息映射到视野矩形框外部（圆点, 视野四周）。
        - **sidebARs**（Siu 和 Herskovic, 2013, ChileCHI 2013）：圆点, 视野两侧。
        - **HaloVR/WedgeVR/HaloAR/WedgeAR**（Gruenefeld 等, 2018b, MobileHCI 2018）：将二维 Halo、Wedge 迁移到 VR/AR 设备（光圈、三角形, 视野四周）。
        - **FlyingARrow**（Gruenefeld 等, 2018d, PerDis 2018）：针对小 FOV 的 AR，用**绿色箭头**指向视野外信息，到达目标时发出提示声（箭头+声音, 视野中央）；认知负荷小于 Eyesee 360、减少屏幕杂乱，但搜索时间/方向误差较差，且一次只能指向单一对象。
        - **3D Radar**（Gruenefeld 等, 2019b, VR 2019）：三维雷达式圆点提示（视野中央）；Bork 等 (2018) 与 Gruenefeld 等 (2019b) 的实验均反馈其实用性较好。
        - **3D Wedge / 3D Minimap / 3D Arrow**（Yu 等, 2020, TVCG 2019）：三角形/圆点/箭头, 视野中央。
        - **CompassbAR**（Evangelista 等, 2022, ADM 2021）：类罗盘条置于界面顶端，颜色编码环境物体，按距离增减环形中心点大小（尺度条+彩色圆圈, 视野上方）。
        - **多模态/硬件外围扩展**：Marquardt 等 (2018/2019/2020) 在复杂或遮挡场景下加音频+触觉提升引导精度；Ghosh 等 (2018)、Binetti 等 (2021)、Trepkowski 等 (2022) 研究音/视/触多感官组合；**Radiallight**（Gruenefeld 等, 2018e）在 VR 中每只眼周布 18 个径向 LED，视野外有信息时对应方向 LED 发光、颜色为视觉线索（一次只提示一个对象）；Gruenefeld 等 (2018f) 在 HoloLens 单目设 12 个径向 LED 解决 FOV 受限。

- **视野内信息提示与标签布局（第 3 节）**：目的是减少标签放置/布局管理导致的遮挡与重叠，降低观察认知负荷。
    - **模型周边标签放置（3.1）**：
        - Hartmann 等 (2005)：从手工插图分析标签布局风格分类与功能/美学指标，确定**外部标签放置的 3 个主要约束**，实现三维模型上标签布局一致性。
        - Tatzgern 等 (2014)：AR 三维空间外部标签视图管理，提出**三维极点约束 + 平面约束**，避免相机运动时标签重叠。
        - Madsen 等 (2016)：对比"连续更新"与"离散时刻更新"布局，发现**3D 空间中静态放置标签的用户体验更好**。
        - **Zhou 等 (2021)**：针对标注对象外标签数多的复杂布局，对比字母序（易引导线交叉）、单圆（无法字母序）、**同心圆（可避免引导线交叉）**、预分类（把圆圈数减到 2 个）四种布局（图 5），提出用**同心圆**放置标签降低布局复杂度。
        - McNamara 等 (2019)：用**眼动追踪**作为注意力指示器，用户关注物体时显示相关信息，并讨论标签呈现位置与显示时间。
    - **场景信息标签布局管理（3.2）**：针对场景中多物体周围标签或主体信息补充。
        - **基于规则/几何约束**：Bell 等 (2001) 定义并实现 VR/AR 视图管理，约束下基于规则避免标签与物体遮挡（对后续视图管理很有启发）；Azuma 和 Furmanski (2003) 基于图像内容讨论视图管理。
        - **基于立体视差**：Peterson 等 (2008a/b, 2009, 2010) 系列——基于视差的视图管理、立体视差标签分离、深度/高度/平面三种静态分离技术；Peterson 等 (2010) 给出复杂 VR 中移动文本标签检测的速度阈值，实验反馈检测结果在 **5~28 arcmin/s** 之间，并据此优化标签管理算法。
        - **基于图像分析**：Makita 等 (2009)（可穿戴 AR 中移动/非刚性物体注释）；**Grasset 等 (2012)** 结合**视觉显著性 + 边缘检测**以图像驱动约束标签放置；**Orlosky 等 (2015)** 的 **Halo content** 结合人脸检测放射状放置标签避免遮挡人脸，实验发现**对用户讨论的干扰次数降低了 50% 之多**；Li 等 (2017/2018) 基于图像分析/边缘映射/显著性检测的标签放置系统。
        - **动态调整/认知负荷**：**Lindlbauer 等 (2019)** 用**基于规则的决策 + 整数线性规划**动态决定 AR 中虚拟元素的位置、时间与信息量，调控用户认知负荷。
        - **社交/通知场景**：Rzayev 等 (2020) 发现 AR 社交中**通知与对话用户对齐可降低干扰**，且对话用户右上角的通知紧迫感最强；Mathis 等 (2020) 发现头显观影时用户对屏幕下方消息更感兴趣；Luo 等 (2021) 研究物理环境对 AR 信息布局的影响。
        - **信息过滤**：Polys 等 (2005) 对比"对象空间/视窗空间"布局；Zhang 和 Sun (2005) 提出 VR/AR 动态标签管理，用"信息过滤"+视图驱动过滤减少渲染标签数。

- **功能与应用（第 1 节概述 + 后续章节, 提取缓存覆盖有限）**：
    - **导航/注意力引导**：先用箭头、雷达等显著形式，再发展为弱视觉/类生物信息提示以减少对沉浸感的破坏，并引入机器学习使提示智能化。Chittaro 和 Burigat (2004) 对比 3D 箭头/2D 箭头/雷达；Wallgrün 等 (2020) 在 360° 全景漫游对比**无指引、箭头、蝴蝶、雷达**四种引导方法。
    - **全景视频/VR 电影 (CVR)**：从画面加箭头，到画中画 (PIP) 呈现 ROI，再到将**视频弹幕**引入全景视频。Rothe 等 (2019) 对 VR 观影中 ROI 的注意力引导方法（箭头、PIP 等）做了分类并讨论优缺点。
    - **工业/旅游辅助**：Gutkowski 等 (2021) 讨论 AR 与旅游产业融合，用时间线/文档/虚拟导游展示人文历史信息，配合箭头、半透明盒子等增强交互。
    - **与已有工作的差异**：本综述将散布在 HCI、可视化、VR/AR 等不同会议/期刊的研究统一到"沉浸式环境视觉提示信息"主题下系统梳理与对比，而非提出单一新技术。

## 实验

本文为**综述**，不含作者自行设计执行的新实验，转述了所引研究的实验结论：

- **三维视野外方法对比**：Bork 等 (2018) 在混合现实场景对比 **3D Arrows、AroundPlot、Eyesee 360、sidebARs、3D Radar、Mirror Ball** 六种方法（其中作者主推 3D Radar 与 Mirror Ball），用户查找目标的反馈表明 **3D Radar 效果更好**（图 4）。
- **二维方法迁移 AR 对比**：Gruenefeld 等 (2017b) 将 Arrow、Halo、Wedge 等二维方法放入 AR，用户实验发现 **Halo 在客观体验、Wedge 在主观体验上分别表现较好**。
- **3D Radar vs Eyesee 360**：Gruenefeld 等 (2019b) 评估二者在可视化移动视野外物体上的性能，用户反馈 **3D Radar 实用性更好**；Gruenefeld 等 (2019a) 测试 3 种减少视觉辅助线的方法，发现视野里辅助线越少对用户影响越小。
- **注意力引导对比**：Wallgrün 等 (2020) 在 360° 全景漫游对比无指引/箭头/蝴蝶/雷达四种方法（据原文后续页 p.13 图 10 "Six guidance methods in VR scenes comparison, Lange et al., 2020"，提取缓存未覆盖正文, 待核）。
- **标签布局评估**：Orlosky 等 (2015) 的 Halo content 实验发现**对用户讨论的干扰次数降低 50% 之多**；Peterson 等 (2010) 给出移动文本标签检测速度阈值 **5~28 arcmin/s**；Madsen 等 (2016) 用户评估表明 3D 静态放置标签体验更好。
- **评价指标**：文本未提及统一基准数据集或指标体系。各研究的评估多基于**搜索时间、方向误差、用户满意度（主观评分）、任务完成度、对社交/讨论的干扰程度**等用户研究指标。

## 局限

1.  **提取缓存覆盖有限**：本笔记主要依据提取文本（p.1-12，至 3.2 节场景标签布局），**应用章节（全景视频细节、工业/虚拟旅游、总结展望）及参考文献在 p.13-21**，仅靠 AI 补读片段还原（见末尾补读记录），细节待核。
2.  **综述本身的批判深度**：作为分类性综述，对各方法优缺点、实验设计严谨性的批判性分析有限，更多是归纳与并置对比。
3.  **缺乏统一定量基准**：未提供统一实验环境/数据集直接定量对比所列方法，读者需自行查阅原文献横向比较。
4.  **时效性**：VR/AR 发展迅速，文中（收稿 2022 年底）未深入神经渲染 (NeRF)、大型视觉语言模型 (VLM/LLM) 等更新范式下的沉浸式信息提示。

## 个人评论

1.  **一张高质量的"研究地图"**：从位置（视野内/外）、场景（2D/3D）、功能（导航/引导）、应用（视频/工业）多坐标轴定位研究，配合表 1/表 2 把方法的"形状—屏幕位置—文献出处"列清楚，对入门者建立知识框架极其友好。
2.  **技术谱系清晰**：完整呈现了从二维（Citylight→Halo→EdgeRadar→Wedge→EdgeSplit→Personalized Compass）到三维（Eyesee 360→FlyingARrow→3D Radar→CompassbAR）的演进脉络，并点明"显示位置由视野四周向视野中央迁移"这一关键趋势。
3.  **问题导向**：始终围绕"沉浸感 vs 信息获取效率"这对核心矛盾串联技术，便于理解每种设计的初衷与取舍（如 FlyingARrow 认知负荷低却牺牲搜索精度）。
4.  **可直接落地的对照表**：表 1/表 2 + 多组用户实验结论（Halo/Wedge 客观/主观、3D Radar 较优、Halo content 降干扰 50%）对工程选型有直接参考价值。
5.  **可改进处**：评价口径不统一（各研究指标各异）使横向结论难以严格比较；中文表述存在少量 OCR/排版瑕疵（如个别人名拼写断裂），引用时建议回溯原文献。文中总结的六大挑战（多尺寸适配、三维沉浸感、标签布局、导航引导精度、观影眩晕、行业交互）是清晰的选题切入点。

### 使用建议

- **快速了解领域**：读摘要、第 0 节引言、第 1 节研究现状总览，及摘要末段六大挑战，即可把握全文脉络。
- **复现具体技术**：重点读第 2 节（视野外）与第 3 节（视野内），结合表 1/表 2 定位方法，按文中引用回溯原始论文获取算法/实验细节。
- **借鉴写综述**：学习其"位置×场景×功能×应用"分类框架，或针对六大挑战之一深入。
- **写 Related Work**：可直接套用其"视野外提示 / 视野内布局 / 功能应用"组织维度，并将本文作为该领域综述性引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇**综述**，处于**计算机视觉/信息可视化、虚拟现实 (VR)、增强现实 (AR) 与人机交互 (HCI)** 的交叉地带，主题为沉浸式环境中"视觉提示信息 (visual cue information)"的可视化方法。它系统梳理了在 VR/AR 等沉浸式环境中，如何通过视觉提示（符号、标签、导航/引导元素）克服 FOV 限制、获取视野外信息、优化视野内标签布局、引导注意力并降低认知负荷。适合归入"沉浸式环境信息可视化 / VR-AR 用户界面与交互"主题，归类为 `R_综述_Survey`。

## 2. 一句话总结
本文按"信息显示位置（视野外/视野内）、使用功能（导航/注意力引导）、实际应用领域（全景视频/工业生活）"三维度，系统梳理了 VR/AR 等沉浸式多场景中视觉提示信息的可视化方法，对比二维与三维的方法演进，并以两张方法汇总表（表 1/表 2）和多组用户实验结论支撑，总结出六大研究挑战。

## 3. 背景与问题
- **为什么要做**：沉浸式环境（VR/AR）应用于教育/医疗/工业/娱乐，自 2014 年消费级 HMD（Oculus Rift、HTC Vive）商业化进入新时代。VR 中眼睛兼具观看与交互双重角色，用户通过视觉获取的信息占比接近 **70%~80%**，视觉提示方法直接决定体验。
- **核心约束**：硬件 **FOV 受限**导致视野外信息不可见；视野内标签易遮挡/重叠；二维方法迁移三维需改进；全景视频中用户自主观看使传统引导失效。
- **核心矛盾**：在**保证/增强沉浸感**的前提下，**高效、舒适、准确**地传递视觉提示，且尽量减少对沉浸感的破坏。

## 4. 核心贡献
1.  **三维度分类框架**（信息显示位置/使用功能/实际应用领域，图 1）。
2.  **二维↔三维迁移分析**：明确显示位置"由视野四周向视野中央调整"、三维可加颜色编码深度与声音/触觉多模态等异同。
3.  **视野外方法系统梳理**：区分概览+细节 / 聚焦+上下文，以表 1（2D，6 种）和表 2（3D，11 种）汇总形状、屏幕位置、文献出处。
4.  **视野内布局系统梳理**：模型周边标签放置 + 场景标签布局管理两条线，覆盖几何约束、立体视差分离、图像驱动、整数线性规划等。
5.  **功能与应用整合**：地图导航、注意力引导，及全景视频/CVR、工业、虚拟旅游应用。
6.  **六大挑战**（见摘要末段）。

## 5. 方法详解
综述无新算法，核心是分类框架与技术归纳：

- **视野外（第 2 节）**——两大范式：
  - 概览+细节：把周边信息全显示（如缩略地图），便捷但信息量大。
  - 聚焦+上下文：鱼眼+边缘符号（箭头/三角/圆形），占屏少、识别快，二维主流。
  - **二维（表 1）**：Citylight（发光线条/屏幕四周, UIST 2002）、Halo（圆弧/屏幕四周, CHI 2003）、EdgeRadar（圆点/屏幕四周, CHI 2007）、Wedge（三角形/屏幕四周, CHI 2008）、EdgeSplit（圆点-多边形/屏幕四周, MobileHCI 2012）、Personalized Compass（圆形+指针/**屏幕中央**, CHI 2016）。对比研究见 Burigat 系列、Ion 等(2013, Canyon)。
  - **三维（表 2）**：AroundPlot（圆点/视野四周）、sidebARs（圆点/视野两侧）、Eyesee 360（圆点+颜色/视野中央, 搜索效率高）、Mirror Ball（Bork 等 2018）、FlyingARrow（绿色箭头+声音/视野中央, 认知负荷低但搜索精度差）、HaloVR/WedgeVR/HaloAR/WedgeAR（光圈/三角形/视野四周）、3D Radar（圆点/视野中央, 用户反馈较优）、3D Wedge/3D Minimap/3D Arrow（Yu 等 2020, 视野中央）、CompassbAR（尺度条+彩色圆圈/视野上方）。多模态：Marquardt/Ghosh/Binetti/Trepkowski 等音-视-触组合；硬件外围 Radiallight（每眼 18 个径向 LED）、HoloLens 12 个径向 LED。
- **视野内（第 3 节）**：
  - 模型周边（3.1）：Hartmann(2005, 3 约束)、Tatzgern(2014, 三维极点+平面约束)、Madsen(2016, 静态放置更优)、Zhou(2021, 同心圆布局, 图 5)、McNamara(2019, 眼动驱动)。
  - 场景布局管理（3.2）：Bell(2001, 规则化视图管理)、Azuma&Furmanski(2003)、Peterson 系列(视差/深度-高度-平面分离; 移动标签阈值 5~28 arcmin/s)、Makita(2009)、Grasset(2012, 显著性+边缘)、Orlosky(2015, Halo content, 降干扰 50%)、Li(2017/2018)、Lindlbauer(2019, 整数线性规划)、Rzayev(2020, 通知对齐降干扰)、Mathis(2020)、Luo(2021)、Polys(2005)、Zhang&Sun(2005, 信息过滤)。
- **功能与应用（第 1 节概述 + p.13 起, 提取缓存覆盖有限）**：导航/引导（Chittaro&Burigat 2004；Wallgrün 2020 无指引/箭头/蝴蝶/雷达）；全景视频/CVR（PIP、视频弹幕；Rothe 2019 ROI 引导分类）；工业/旅游（Gutkowski 2021 AR+旅游）。

## 6. 实验与结果
综述转述他人实验：
- Bork 等(2018) 六法对比，**3D Radar 反馈最好**（图 4）。
- Gruenefeld 等(2017b) 二维法入 AR，**Halo 客观、Wedge 主观分别较好**。
- Gruenefeld 等(2019b) 3D Radar vs Eyesee 360，**3D Radar 实用性更好**；(2019a) 视觉辅助线越少越好。
- Wallgrün 等(2020) 360° 全景四种引导对比（无指引/箭头/蝴蝶/雷达）。
- Orlosky 等(2015) Halo content **降讨论干扰 50%**；Peterson(2010) 移动标签阈值 **5~28 arcmin/s**；Madsen(2016) 静态标签更优。
- **指标**：无统一基准/数据集；多用搜索时间、方向误差、主观评分、任务完成度、社交/讨论干扰程度等用户研究指标。

## 7. 这篇论文真正有价值的地方
1.  **可检索的方法对照表（表 1/表 2）**：把每种方法的形状、屏幕位置、发表会议一列到底，工程选型与文献回溯都好用。
2.  **演进脉络清晰**：二维→三维的技术谱系，及"显示位置由四周向中央迁移"的趋势提炼。
3.  **问题导向**：始终以"沉浸感 vs 信息效率"统摄全部技术，便于理解取舍。
4.  **六大挑战可作选题**：多尺寸适配、三维沉浸感、标签布局、导航引导精度、观影眩晕、行业交互。
5.  **跨社区整合**：把分散在 HCI/可视化/VR-AR 的研究统一到一个主题下。

## 8. 局限与问题
1.  本笔记提取缓存仅覆盖 p.1-12（至 3.2 节），应用章节与参考文献在 p.13-21，靠 AI 补读片段还原，**应用细节待核**。
2.  综述批判深度有限，多为归纳/并置。
3.  无统一定量基准，横向比较需回溯原文献。
4.  时效性：未涉及 NeRF、VLM/LLM 等更新范式（收稿 2022 年底）。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 第 0/1 节 + 六大挑战。
- **复现技术**：第 2/3 节 + 表 1/表 2 定位方法，按引用回溯原文。
- **写综述**：套用"位置×场景×功能×应用"框架，或攻克某一挑战。
- **写 Related Work**：以"视野外提示 / 视野内布局 / 功能应用"组织，引用本文作综述性参考。

## 10. 和其他论文的关系
作为综述与大量工作相关，可建立双链的代表性主题/方法：
- [[Halo技术]]：Baudisch 和 Rosenholtz (2003) 经典二维视野外提示。
- [[Wedge技术]]：Gustafson 等 (2008) 改进方法（避免重叠）。
- [[Eyesee 360]]：Gruenefeld 等 (2017a) VR 视野外提示。
- [[3D Radar]]：Gruenefeld 等 (2019b)，多组实验中实用性较优。
- [[VR电影注意力引导]]：Rothe 等 (2019) ROI 引导分类。
- [[AR场景同心圆标签布局]]：Zhou 等 (2021)。
- [[多模态信息提示]]：Marquardt/Ghosh/Trepkowski 等音-视-触提示研究。

## 11. 关键词
沉浸式环境, 虚拟现实 (VR), 增强现实 (AR), 多场景, 视觉提示信息, 视野外可视化, 视图管理/标签布局, 注意力引导, 全景视频/CVR, 人机交互 (HCI), 信息可视化, 用户体验, 认知负荷

## 12. 可信度说明
本精读笔记主要基于 PDF 提取文本（共 21 页, 提取缓存覆盖 p.1-12，含标题/作者/摘要/引言/研究现状/视野外方法第 2 节/视野内方法第 3 节至 3.2 场景标签布局）。这部分信息密度高、可读，能可靠支撑"论文定位、核心贡献、视野外/视野内方法详解、表 1/表 2 方法清单、所引用户实验结论（Halo/Wedge 客观-主观、3D Radar 较优、Halo content 降干扰 50%、移动标签阈值 5~28 arcmin/s）"等内容。
**主要局限**：提取缓存未覆盖 p.13-21（使用功能完整章节、全景视频/工业/虚拟旅游应用、总结展望、参考文献），笔记中应用部分主要据第 1 节引言概述 + AI 补读片段还原（如 p.13 图 10 六种引导方法对比、p.15 全景视频弹幕研究），凡缓存未覆盖处已标注"待核"。因此本笔记在定位/贡献/视野外-视野内方法上可信度较高，在应用与总结全面性上仍有不足。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 2086 字符/页; 提取缓存覆盖 12/21 页); 来源缓存: `.paper-cache/extracts/cjig_计算机视觉_沉浸式环境和多场景中的视觉提示信息综述.txt`; 原 AI 主体 12/21 + 全文补读 13-21; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-21; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-21。
- **提取情况**: 缺失页 9 页, 其中 9 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.17: AR solutions for industrial maintenance//Proceedings of 2020 CHI
- p.17: Proceedings of 2020 IEEE Conference on Virtual Reality and 3D
- p.17: International Conference on Design Tools and Methods in Industrial
- p.17: Conference on Human -Computer Interaction with Mobile Devices
- p.18: 2021 IEEE International Symposium on Mixed and Augmented
- p.18: method in augmented reality//Proceedings of the 16th ACM
- p.18: SIGGRAPH International Conference on Virtual -Reality Continuum
- p.19: IEEE International Symposium on Mixed and Augmented Reality
- p.19: Information placement in virtual reality//Proceedings of 2019 IEEE
- p.20: Conference on Human Computer Interaction with Mobile Devices
- p.20: 2020 IEEE Conference on Virtual Reality and 3D User Interfaces
- p.21: Conference on Computer Aided Design and Computer Graphics

### 缺失页关键摘录

- p.13: Fig.10 Six guidance methods in VR scenes comparison （Lange et al .， 2020 ）
- p.15: Fig.11 Research on bullet comments for 360° video
- p.15: Fig.12 Wear AR glasses to play games in real scenes
- p.17: screen objects on mobile devices ： a comparative evaluation of three
- p.17: tual buildings ： a comparative evaluation of two approaches// 2006
- p.18: Harada Y and Ohyama J . 2022 . Quantitative evaluation of visual guid ⁃
- p.18: Hu S ， Malloch J and Reilly D . 2020 . A comparative evaluation of tech ⁃
- p.18: Li G， Liu Y and Wang Y T . 2017 . Evaluation of labelling layout methods
- p.18: Li G ， Liu Y and Wang Y T . 2018 . An empirical evaluation of labelling
- p.21: 2020 . Design and evaluation of visualization techniques of off -
<!-- AI_READING_NOTE_END -->
