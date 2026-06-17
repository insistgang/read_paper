---
title: Gong J Y Lou Y J Liu F Q Zhang Z W Chen H M Zhang Z Z Tan X Xie Y and Ma L Z. 2023. Scene point cloud understanding
authors:
  - "龚靖渝"
  - "楼雨京"
  - "柳奉奇"
  - "张志伟"
  - "陈豪明"
  - "张志忠"
  - "谭鑫"
  - "谢源"
  - "马利庄"
year: 2023
venue: "中国图象图形学报"
doi: 10.11834/jig.230004
pdf: [[cjig_计算机图形学_三维场景点云理解与重建技术.pdf]]
primary_topic: D_3D_点云_分类_分割_配准
topics:
  - "D_3D_点云_分类_分割_配准"
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
extract_cache: .paper-cache/extracts/cjig_计算机图形学_三维场景点云理解与重建技术.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/26 pages"
---
# Gong J Y Lou Y J Liu F Q Zhang Z W Chen H M Zhang Z Z Tan X Xie Y and Ma L Z. 2023. Scene point cloud understanding

## 基本信息
- **PDF**: [[cjig_计算机图形学_三维场景点云理解与重建技术.pdf]]
- **primary_topic**: `D_3D_点云_分类_分割_配准`
- **topics**: `D_3D_点云_分类_分割_配准`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 三维场景点云理解与重建技术 (Scene point cloud understanding and reconstruction technologies in 3D space) |
| **作者** | 龚靖渝; 楼雨京; 柳奉奇; 张志伟; 陈豪明; 张志忠; 谭鑫; 谢源; 马利庄 |
| **单位** | 上海交通大学计算机科学与工程系; 华东师范大学计算机科学与技术学院 |
| **发表时间** | 2023 (28卷6期, pp.1741-1766) |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics) |
| **DOI** | 10.11834/jig.230004 |

## 摘要

**英文原摘要 (据 PDF 提取文本整理, 修复断字与空格)：**

> 3D scene understanding and reconstruction are essential for machine vision and intelligence, which aim to reconstruct completed models of real scenes from multiple scene scans and understand the semantic meanings of each functional component in the scene. This technique is indispensable for real-world digitalization and simulation, which can be widely used in related domains like robots, navigation system and virtual tourism. Its key challenges are required to be resolved on three aspects: 1) to recognize the same area in multiple real scans and fuse all the scans into an integrated scene point cloud; 2) to make sense of the whole scene and recognize the semantics of multiple functional components; 3) to complete the missing region in the original point cloud caused by occlusion during scanning. It is necessary to extract point cloud features (invariant to scanning position and rotation) in order to fuse multiple real scene scans into an integrated point cloud. Intrinsic geometry features like point distance and singular values in the neighborhood covariance matrix are often involved in rotation-invariant feature design, and a contrastive learning scheme is usually taken to pull features from the same area close while pushing features from different areas away. For whole-scene parsing, an effective and efficient network with an appropriate 3D convolution operation is required to parse the entire point-based scene hierarchically. For object point cloud completion, it is crucial to learn a compact latent code space to represent all complete shapes and to design a versatile decoder; a cross-domain learning scheme is used to apply completion knowledge to real object scans. We analyze the current situation of scene understanding and reconstruction (point cloud fusion, 3D convolution operation, entire scene segmentation, and fine-grained object completion), survey the frontier technologies, and predict promising future research trends, pointing to more open space with further challenges on computing efficiency, handling out-of-domain knowledge, and human-scene interaction.

**中文翻译 (论文给出的中文摘要原文)：**

> 三维场景理解与重建技术能够使计算机对真实场景进行高精度复现并引导机器以三维空间的思维理解整个真实世界，从而使机器拥有足够智能参与到真实世界的生产与建设，并能通过场景的模拟为人类的决策和生活提供服务。该技术主要包含场景点云特征提取、扫描点云配准与融合、场景理解与语义分割、扫描物体点云补全与细粒度重建等；在处理真实扫描场景时，受到扫描设备、角度、距离以及场景复杂程度的影响，对技术的精准度和稳定性提出了更高要求，相关技术也十分具有挑战性。其中，原始扫描点云特征提取与配准融合旨在将同场景下多个扫描区域进行特征匹配从而融合得到完整场景点云，是理解与重建技术的基石；场景点云的理解与语义分割旨在对场景模型进行整体感知并按语义划分为功能性物体甚至部件级别的点云，是整套技术的核心组成部分；后续物体点云细粒度补全主要研究扫描物体的结构恢复与残缺部分补全，是场景物体点云细粒度重建的关键技术。本文围绕上述系列技术详细分析了相关应用领域和研究方向，归纳总结了国内外前沿进展与研究成果，并对未来研究方向和技术发展进行了展望。
>
> **关键词**：三维场景；点云融合；场景分割；物体形状补全；深度学习

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：三维场景模型是真实世界在计算机中数字化后的具体表征，研究它不仅能让机器以三维空间思维理解周围环境，更能让机器以智能体方式参与真实三维世界的工业生产、城市与交通规划，以及与人体的交互 (p.1742)。点云作为采集设备通用的三维数据形式，常被主流工作用于表征三维场景。场景点云可通过 RGB-D 相机、激光雷达扫描获得；室内场景也可借助 SLAM (Hosseinzadeh 等, 2019) 由相邻帧图像估计相机运动并恢复空间结构得到。但扫描得到的原始点云往往不完整，需后续处理 (p.1742)。
- **之前方法的问题 / 三大技术挑战**：
  1. **特征提取与配准融合**：扫描设备、角度、距离存在差异，同时受离群噪声点影响，同一区域的点云表现不同，大幅提升特征提取与匹配难度；核心难点是探索局部点云几何特征的平移旋转不变性，找到不同扫描数据中的匹配区域 (p.1742-1743)。点云配准是从扫描三维数据到完整点云场景模型的核心模块 (李建微和占家旺, 2022)。
  2. **场景语义分割**：三维点云的结构不规则性、不同扫描设备及距离角度导致的不均匀性，使鲁棒的三维特征提取困难；对不同三维场景进行精准的语义甚至实例分割极具挑战 (龙霄潇 等, 2021) (p.1742)。
  3. **物体点云补全与细粒度重建**：遮挡导致点云残缺，需利用大型完整点云数据库学习先验知识修复；重点研究点云编解码方式与跨域跨数据集的统一特征学习。由于点云的非结构化表征，仍缺乏细粒度点云解码与重建方法；仅凭合成完整模型数据集很难补全无完整真值的真实扫描数据 (p.1742)。
- **核心矛盾**：**真实世界扫描数据的复杂性、不完整性、不规则性**与**对高精度、强鲁棒性三维理解与重建技术的需求**之间的矛盾。

## 关键贡献

本文是一篇综述，核心贡献在于系统性梳理、分析与展望：
1.  **三环节技术框架**：将三维场景点云理解与重建清晰划分为"点云特征提取与配准融合"→"场景点云语义分割"→"物体点云形状补全与细粒度重建"三个相互关联的环节，并阐明其内在联系 (p.1741-1742)。
2.  **特征提取技术演进综述**：系统梳理点云特征提取的发展，从**传统几何算子**(空间分布统计类: SI、3DSC、USC、RoPS；几何属性统计类: LSP、Thrift、PFH、FPFH、SHOT、PPF)，到**深度学习先驱** PointNet / PointNet++，再到**点云卷积**(PointCNN、SpiderCNN、DGCNN、RSCNN、KPConv)、**稀疏卷积**(子流形稀疏卷积、Minkowski Engine、PVC/SPVConv) 与**点云 Transformer**(PCT、Point Transformer、PTv2)，并专设一节讨论**旋转不变特征提取**(RIConv、ClusterNet、SGMNet、PR-invNet、RI-GCN、AECNN) (第 1 节)。
3.  **场景分割方法全面总结**：按**室内/室外场景**不同表征方式组织 (室内: 点特征 / 图网络 / 注意力；室外: 环视图 / 稀疏卷积 / 鸟瞰图 / 神经辐射场)，总结**全监督**分割方法，以及面向标注难题的**半监督与弱监督**分割方法，并涉及多模态融合与实例分割 (第 2 节)。
4.  **物体补全与未来展望**：综述物体点云补全 (隐式编码空间 + 解码器 + 跨域学习)，并指出未来研究方向——更开放复杂的场景、计算效率、跨域 (out-of-domain) 知识、人机交互场景建模 (p.1742)。

## 方法

作为综述，本文不提出单一新方法，而是给出一条贯穿全文的技术主线并对各环节系列方法归纳分析。
- **整体框架 / 逻辑主线**：**原始扫描输入 → 特征提取与配准融合 → 场景语义分割 → 物体补全与细粒度重建**。即: 1) 对原始扫描点云做点级几何特征提取，并据特征配准融合成完整场景点云；2) 对完整场景点云做语义/实例分割，识别功能性物体甚至部件；3) 对分割出的残缺物体点云补全并细粒度重建 (p.1741-1742)。
- **输入输出**：输入是 RGB-D 相机、激光雷达扫描或 SLAM 恢复得到的原始 (不完整) 扫描点云；输出是语义清晰、结构完整的三维场景模型或物体模型。
- **关键模块与连接**：
    1.  **点云特征提取模块** (1.1-1.6 节)：从原始点云提取具区分性、平移旋转不变性的局部/全局特征。传统几何算子编码局部几何信息 (要求可描述性、紧密性、鲁棒性)；PointNet 用对称函数 max-pooling 直接处理无序点；PointNet++ 用最远点采样 (FPS) + 分层球形邻域获取多尺度局部特征；点云卷积 (PointCNN 的 χ-卷积、KPConv 的核点卷积) 解决邻域点排序与权重对应；稀疏卷积仅在非空体素处计算以省资源；点云 Transformer 用 (向量) 自注意力建模点间关系。
    2.  **点云配准与融合模块** (1.7 节)：提取两块点云特征后，用对比学习拉近对应区域、推远不同区域，建立对应关系并求解扫描帧间变换矩阵，将多块局部点云拼接成完整场景点云。代表工作 3DMatch、3DSmoothNet、FCGF、D3Feat、SpinNet 及端到端从粗到细匹配。
    3.  **场景语义分割模块** (第 2 节)：对融合后的场景点云做点级语义预测；核心是设计合适的三维卷积/注意力操作以分层解析大规模不规则点云，并按室内/室外特点选择表征 (点 / 图 / 注意力 / 环视图 / 稀疏体素 / 鸟瞰图 / NeRF) 与监督策略 (全监督 / 半监督 / 弱监督)。
    4.  **物体形状补全模块**：针对残缺物体点云，学习一个能表示所有完整形状的**紧凑隐式编码空间** (需大规模合成模型数据集训练以保证泛化)，编码器识别原始结构并保存到隐编码，解码器据已有局部几何提示恢复整体骨架与细粒度细节；**跨域学习**将补全知识从合成模型迁移到真实扫描物体 (p.1742)。
- **与已有方法的关系**：本文是对 PointNet、PointNet++、PointCNN、KPConv、DGCNN、稀疏卷积/Transformer 系列，以及 3DMatch、FCGF 等匹配工作、S3DIS/ScanNet/SemanticKITTI 等数据集上方法的系统归纳与对比，而非提出并列新方法。

## 实验

本文是**综述论文**，主要工作是总结分析现有研究，不提出新方法并做实验。因此**没有**作者自己的统一实验、对比方法或量化指标数值——提取文本中未给出任何 mIoU/精度/速度的具体数字。
- **综述中梳理的代表数据集** (据提取文本):
    - **室内分割**：NYUv2 (Silberman 等, 2012)、SUN RGB-D (Song 等, 2015)、S3DIS (Armeni 等, 2016)、ScanNet (Dai 等, 2017) (p.1748-1749)。
    - **室外静态 LiDAR**：Semantic 3D (Hackel 等, 2017) (p.1749)。
    - **室外自动驾驶 LiDAR**：SemanticKITTI (Behley 等, 2019)、nuScenes (Caesar 等, 2020)、Waymo Open Dataset (Sun 等, 2020)、Lyft L5 (Houston 等, 2020)；其中 nuScenes 与 Waymo 还提供毫米波雷达数据，支持雨/雪/雾等极端天气下的探测 (p.1749)。
    - **点云匹配**：3DMatch (Zeng 等, 2017) (p.1747)。
- **指标与效率**：提取文本提及语义分割任务采用逐点语义分类，但**未列出任何具体数值**；在稀疏卷积 (1.4 节)、环视图与鸟瞰图等讨论中定性指出"减少计算量、满足实时性"的优势，但**无具体速度/参数量/FLOPs 对比数据** (PDF 文本未明确)。

## 局限

- **纯综述, 无统一基准复现**：未在统一基准上对所述方法做实验比较，无法给出各方法优劣的绝对量化结论。
- **聚焦理解与重建主链, 旁支覆盖有限**：主线为"特征提取-配准-分割-补全"，对三维目标检测、位姿估计、独立的点云生成等分支着墨较少 (但分割章节已涉及实例分割与多模态融合)。
- **时效性受截稿时间限制**：收稿 2023-01-03，对其后 (如点云大模型、3D 生成与重建结合等) 的最新突破难以覆盖。
- **方法本身的固有难点**：如旋转不变特征在将坐标转为底层几何量时会丢失重要几何信息、导致结果下降 (1.6 节)；向量注意力网络参数量随深度激增、易过拟合 (1.5 节)；环视图分割将 2D 结果传回 3D 时有精度损失、鸟瞰图对悬吊物体预测差 (2.1.2 节)——这些是综述指出的、而非本文造成的局限。

## 个人评论

1.  **一张高质量的技术演进地图**：对初入三维点云的研究者，这篇综述把特征提取 (传统算子 → PointNet 系 → 点云卷积 → 稀疏卷积 → Transformer → 旋转不变)、配准、分割、补全的脉络铺得很清楚，且每类方法都点到代表工作与其解决的具体问题 (如 PointCNN 解决排序、KPConv 解决核定义、稀疏卷积解决空体素浪费)，比单纯罗列文献更有结构。
2.  **对"为什么难"的洞察扎实**：点云的不规则/无序/稀疏/不均匀，旋转不变性需求，大规模场景的算力与显存瓶颈，标注稀缺 (半/弱监督的动机)，合成-真实域差异 (补全的跨域学习)——这些贯穿全文的痛点，正是选题与定义问题的好抓手。
3.  **室内/室外分治的组织视角值得借鉴**：把分割按室内 (稠密、几何规整) 与室外 (稀疏、长尾、天气光照) 分开讨论，并对应到不同表征 (点/图/注意力 vs 环视图/稀疏卷积/BEV/NeRF)，这种"按数据特性组织方法"的写法，对写自己论文的相关工作很有参考价值。
4.  **可改进处**：作为综述缺少统一基准的横向定量对比，读者需自行查阅原论文的数值；且本文作者团队 (Gong 等, 2021a/b) 的若干工作在分割章节被引用，阅读时可留意其立场。

### 使用建议

- **快速了解领域**：先读中英文摘要与引言 (第 0 节)，再读各章节开头与小结，建立整体认知。
- **复现具体技术**：把本综述当**索引**，顺着引用去精读 PointNet、KPConv、FCGF、PTv2 等原论文并找开源代码与实验设置。
- **借鉴组织思路**：写"相关工作"时可参考其按"任务环节 + 数据特性"的分类与叙述逻辑，并以其未来展望 (计算效率、跨域知识、人机交互) 为选题切入口。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[D_3D_点云_分类_分割_配准]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文是**三维场景点云理解与重建**领域的**中文综述** (中国图象图形学报, 2023, 28(6):1741-1766)。它围绕"如何从多角度、不完整的扫描点云恢复出语义清晰、结构完整的三维场景模型"这一核心问题，把技术体系拆为三个相互衔接的环节——点云特征提取与配准融合、场景语义分割、物体点云补全与细粒度重建，并逐环节梳理国内外代表工作与未来挑战。因此它非常适合放在 `D_3D_点云_分类_分割_配准` 主题下，作为了解该领域脉络与前沿的入门与参考文献。

## 2. 一句话总结
本文系统综述了基于三维点云的场景理解与重建技术，沿"特征提取与配准融合 → 场景语义分割 → 物体形状细粒度补全"主线梳理了从传统几何算子到深度学习 (PointNet 系、点云卷积、稀疏卷积、Transformer、旋转不变方法) 的关键技术、室内外分割方法与数据集，并展望了计算效率、跨域知识、人机交互等方向。

## 3. 背景与问题
- **为什么要做**：三维场景模型是真实世界在计算机中的数字化表征，研究它能让机器以三维空间思维理解环境并参与工业生产、城市与交通规划及人机交互 (p.1742)。点云是采集设备通用的三维数据形式；可由 RGB-D 相机、激光雷达扫描，或室内场景借助 SLAM (Hosseinzadeh 等, 2019) 估计相机运动恢复结构得到，但原始扫描点云往往不完整需后续处理。
- **之前方法的三大挑战**：1) **特征提取与配准**——设备/角度/距离差异与离群噪声使同一区域点云表现不同，难点是局部几何的平移旋转不变性与跨扫描匹配 (p.1742-1743)；2) **场景语义分割**——点云不规则、不均匀使鲁棒三维特征提取与精准语义/实例分割困难 (龙霄潇 等, 2021)；3) **物体补全**——遮挡致残缺，需从大型完整数据库学先验、跨域跨数据集统一特征学习，且缺乏细粒度解码重建方法 (p.1742)。
- **核心矛盾**：真实扫描数据的复杂、不完整、不规则 vs. 对高精度强鲁棒三维理解与重建的需求。

## 4. 核心贡献
1.  **三环节系统框架**：特征提取与配准融合 → 场景语义分割 → 物体形状补全与细粒度重建，并阐明三者内在联系 (p.1741-1742)。
2.  **特征提取演进综述**：传统几何算子 (空间分布统计 SI/3DSC/USC/RoPS；几何属性统计 LSP/Thrift/PFH/FPFH/SHOT/PPF) → PointNet/PointNet++ → 点云卷积 (PointCNN/SpiderCNN/DGCNN/RSCNN/KPConv) → 稀疏卷积 (子流形稀疏卷积/Minkowski/PVC/SPVConv) → 点云 Transformer (PCT/Point Transformer/PTv2)，并专节讨论旋转不变特征 (第 1 节)。
3.  **分割方法全面总结**：按室内 (点/图/注意力) 与室外 (环视图/稀疏卷积/BEV/NeRF) 表征组织，覆盖全监督、半监督、弱监督方法及多模态融合与实例分割，并整理室内外代表数据集 (第 2 节)。
4.  **补全与未来展望**：物体补全的隐式编码空间 + 解码器 + 跨域学习范式；未来方向为更开放复杂场景、计算效率、跨域知识、人机交互场景建模 (p.1742)。

## 5. 方法详解
作为综述，"方法"体现在一条贯穿全文的技术主线与各环节梳理框架上。
- **逻辑主线**：原始扫描输入 → 特征提取与配准融合 → 场景语义分割 → 物体补全与细粒度重建 (p.1741-1742)。
- **特征提取 (1.1-1.6)**：
    - *传统算子 (1.1)*：好算子需可描述性、紧密性、鲁棒性。空间分布统计类——SI (Johnson & Hebert, 1999) 用关键点+法向量建局部参考轴并记录点到切平面内外距离；3DSC (Frome 等, 2004) 用三维球形网格统计点数；USC (Tombari 等, 2010) 锁定绕轴旋转自由度消歧；RoPS (Guo 等, 2013) 绕轴多角度旋转投影统计。几何属性统计类——LSP (Chen & Bhanu, 2007)、Thrift (Flint 等, 2007)、PFH (Rusu 等, 2008, 基于 Darboux 参考系)、FPFH (Rusu 等, 2009, 降低 PFH 复杂度)、SHOT (Salti 等, 2014, 按半径/方位角/仰角分球形网格)、PPF (Drost 等, 2010, 点对四维特征)。
    - *PointNet 系 (1.2)*：PointNet (Qi 等, 2017a) 直接以点坐标为输入，用对称函数 max-pooling 保证排列不变性并聚成全局描述子，配 STN 空间变换网络标准化输入；PointNet++ (Qi 等, 2017b) 用 FPS 划分重叠球形邻域、分层多尺度提取局部几何，弥补 PointNet 无法捕获局部结构的缺陷。
    - *点云卷积 (1.3)*：PointCNN (Li 等, 2018b) 用 χ-卷积学习变换矩阵对邻域点排序以对应权重；SpiderCNN、Hua 等 (2018) 逐点卷积、DGCNN (Wang 等, 2019)、RSCNN (Liu 等, 2019b) 用相对位置生成权重；KPConv (Thomas 等, 2019) 定义固定/可形变核点，邻域核点数不定、不受密度变化影响，可构建很深网络。亦可在图结构上做谱域或空间域卷积。
    - *稀疏卷积 (1.4)*：Graham 等 (2018) 提出子流形稀疏卷积；Choy 等 (2019a) 的 Minkowski Engine 用稀疏张量 + 核映射只对非空体素卷积；PVC/PVCNN (Liu 等, 2019c) 点-体素双分支，SPVConv (Tang 等, 2020) 在体素分支引入稀疏卷积改善小目标 (如行人) 识别。
    - *点云 Transformer (1.5)*：Guo 等 (2021) 的 PCT 用全局自注意力 (受内存限制只适合小物体/小场景)；Zhao 等 (2020/2021) 用向量注意力关注局部 (参数量随深度激增易过拟合)；PTv2 (Wu 等, 2022) 用分组向量注意力降参并设计三维专用位置编码。
    - *旋转不变 (1.6)*：三类思路——旋转不变几何特征作输入 (RIConv/ClusterNet/SGMNet)、构建局部参考系 (RI-GCN/AECNN)、估计姿态归一化 (PR-invNet 及 Li 等, 2021a, 用 PCA 选轴, 因 PCA 歧义而以姿态空间+姿态选择器处理)。
- **配准融合 (1.7)**：对比学习拉近对应、推远不同区域以学匹配特征。3DMatch (Zeng 等, 2017) 提供匹配数据集并用三维卷积提特征；3DSmoothNet (Gojcic 等, 2019) 引入旋转不变局部参考系；FCGF (Choy 等, 2019b) 稀疏卷积 + 最困难样本对比学习；D3Feat (Bai 等, 2020) 稠密检测+描述；SpinNet (Ao 等, 2021) 柱形卷积。另有端到端从粗到细匹配 (Yu 等, 2021a；Qin 等, 2022；Yew & Lee, 2022)。
- **场景分割 (第 2 节)**：核心是设计合适三维卷积/注意力分层解析大规模不规则点云；按室内/室外表征与全/半/弱监督策略组织 (详见第 6 节)。
- **物体补全**：学紧凑隐式编码空间表示完整形状 (需大规模合成数据集), 编码器存结构到隐编码、解码器据局部几何提示恢复骨架与细节, 跨域学习迁移到真实扫描 (p.1742)。

## 6. 实验与结果
本文是**综述**，不含作者自做的统一实验，因此**没有任何精度/速度的具体数值** (PDF 文本未明确)。其价值在于把领域内的数据集与方法体系整理清楚:
- **室内分割数据集**：NYUv2 (Silberman 等, 2012)、SUN RGB-D (Song 等, 2015)、S3DIS (Armeni 等, 2016)、ScanNet (Dai 等, 2017) (p.1748-1749)。
- **室外 LiDAR 数据集**：静态 Semantic 3D (Hackel 等, 2017)；自动驾驶 SemanticKITTI (Behley 等, 2019)、nuScenes (Caesar 等, 2020)、Waymo Open Dataset (Sun 等, 2020)、Lyft L5 (Houston 等, 2020)；nuScenes 与 Waymo 含毫米波雷达数据, 支持极端天气探测 (p.1749)。
- **匹配数据集**：3DMatch (Zeng 等, 2017) (p.1747)。
- **室内分割代表方法**：PointWeb (Zhao 等, 2019, 自适应特征调整)、PointConv (Wu 等, 2019b)、谱图卷积 (Wang 等, 2018a)、RGCNN (Te 等, 2018, 平滑性正则)、DGCNN、基于注意力/Transformer 的 Feng 等 (2020)、Park 等 (2022, 快速点云 Transformer)、Yu 等 (2022, 掩码 Transformer 预训练)、Zhang 等 (2022, 块注意力)。
- **室外分割表征方法**：环视图 (Milioto 等, 2019；Cortinhal 等, 2020)、稀疏卷积 (Graham 等, 2018；Zhu 等, 2021 扇形卷积)、鸟瞰图 (PolarNet, Zhang 等, 2020c；概念源于 2020 年特斯拉 FSD 纯视觉方案)、神经辐射场 (Kundu 等, 2022)。
- **全监督分割**：边缘感知 (Gong 等, 2021b 边缘预测+边缘几何编码)、极角正则数据增强 (Chen 等, 2022)、时序融合 (Schutt 等, 2022)、多表征融合 (Xu 等, 2021b 环视图-点-体素；Ye 等, 2021 点-体素交替转换；Gong 等, 2021a 层次化感受野因果推理；Li 等, 2022b 点-网格融合)。
- **有限标注分割**：半监督——室内伪标签置信度 (Li 等, 2021b 判别网络)、室外 LaserMix (Kong 等, 2022 环形混合增强)；弱监督——Xu & Lee (2020) 首次 (如每帧仅随机标注 1% 点)。
> 注: 弱监督具体方法、物体形状补全的细节方法清单位于 PDF 后续页 (p.1749 以后), 提取缓存仅覆盖至 p.1749, 相关具体方法名待核。

## 7. 这篇论文真正有价值的地方
1.  **结构化的技术演进图谱**：每个子方向都点出代表工作及其"解决了什么具体问题" (PointCNN 解排序、KPConv 解核定义、稀疏卷积省空体素算力、PTv2 解 Transformer 参数膨胀)，比纯文献堆叠更易把握脉络。
2.  **对核心难点的系统洞察**：不规则/无序/稀疏/不均匀、旋转不变、算力与显存、标注稀缺、合成-真实域差异——为选题与问题定义提供抓手。
3.  **室内/室外分治的方法组织**：按数据特性 (室内稠密规整 vs. 室外稀疏长尾天气敏感) 对应不同表征与策略，组织视角清晰，便于借鉴到自己论文的相关工作写作。

## 8. 局限与问题
- **缺乏统一基准的横向定量对比**：纯综述不复现, 无法给出各方法优劣的绝对量化结论, 读者需回到原论文查数值。
- **聚焦主链, 旁支有限**：以特征-配准-分割-补全为主线, 对三维目标检测、位姿估计、独立点云生成涉及较少。
- **时效性受截稿时间限制**：收稿 2023-01-03, 难覆盖其后的点云大模型、3D 生成与重建结合等突破。
- **综述转述的固有方法局限**：旋转不变特征转底层几何量会丢信息 (1.6)、向量注意力参数随深度激增易过拟合 (1.5)、环视图传回 3D 有精度损失且鸟瞰图对悬吊物体差 (2.1.2)——是被综述方法的局限, 非本文造成。

## 9. 我该怎么使用这篇论文
- **快速了解领域**：先读中英文摘要与引言 (第 0 节), 再读各章节开头/小结, 建立整体认知。
- **复现具体技术**：把它当**索引**, 顺引用去精读 PointNet、KPConv、FCGF、PTv2 等原论文并找开源代码与实验设置。
- **借鉴组织思路**：写"相关工作"时参考其"任务环节 + 数据特性"的分类逻辑, 并以未来展望 (计算效率、跨域知识、人机交互) 为选题切入口。

## 10. 和其他论文的关系
在 `D_3D_点云_分类_分割_配准` 主题下, 本综述与该主题下的大量具体工作是**总览与细分**的关系, 是众多经典工作的背景介绍与对比框架:
- 特征提取：PointNet / PointNet++ / PointCNN / KPConv / DGCNN / Point Transformer (PTv2)。
- 配准匹配：3DMatch / 3DSmoothNet / FCGF / D3Feat / SpinNet。
- 分割：S3DIS / ScanNet / SemanticKITTI / nuScenes / Waymo 等数据集上的具体网络 (PointWeb / PolarNet / LaserMix 等)。
- （注：上述工作均为提取文本中明确出现的引用；是否在本知识库中已有同名笔记需另行核对, 故此处暂未建立确定的双链。）

## 11. 关键词
三维场景, 点云融合, 场景分割, 物体形状补全, 深度学习, 点云特征提取, 点云配准, 语义分割, 稀疏卷积, 点云 Transformer, 旋转不变, 室内外场景, 半监督/弱监督分割

## 12. 可信度说明
本篇精读主体基于提取缓存 (覆盖至期刊页 p.1749, 即引言 + 第 1 章全部 + 第 2 章场景表征/数据集/全监督分割/有限标注分割开头)。该范围内文本结构完整, 算子名、网络名、数据集名、引用年份均可逐条核对, 据此撰写的第 1-6 节与第 0 节背景可信度高。
**提取质量**：良好 (约 2086 字符/页), 公式与参考文献得以保留。
**局限性**：弱监督分割的具体方法清单、**物体点云形状补全**的详细技术 (隐式编码/解码器/跨域具体网络) 位于 p.1749 之后的页面, 提取缓存未覆盖, 笔记中相关具体方法名为"据原文后续页, 提取缓存未覆盖, 待核"。所有未在提取文本中出现的方法名/数字均未编造。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/cjig_计算机图形学_三维场景点云理解与重建技术.txt` (覆盖至期刊页 p.1749, 约前 8 个期刊版面页; 缓存头标注 12/26 PDF 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮据提取文本重核并补充技术细节, human_reviewed 仍为 false。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-26; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-26。
- **提取情况**: 缺失页 14 页, 其中 14 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.19: Learning a structured latent space for unsupervised point cloud
- p.19: 2010 IEEE Computer Society Conference on Computer Vision and
- p.20: Boundary -aware geometric encoding for semantic segmentation of
- p.20: Proceedings of 2022 IEEE/CVF Conference on Computer Vision
- p.21: method . Journal of Image and Graphics ， 27（2） ： 349-367 （李 建
- p.22: 2008 IEEE/RSJ International Conference on Intelligent Robots and
- p.22: Image -to-lidar self -supervised distillation for autonomous driving
- p.23: Shape inpainting using 3D generative adversarial network and
- p.24: LiDAR point cloud segmentation//Proceedings of 2021 IEEE/CVF
- p.24: Proceedings of the 35th Advances in Neural Information Processing
- p.25: Learning rotation -invariant representations of point clouds using
- p.25: GAN inversion//Proceedings of 2021 IEEE/CVF Conference on

### 缺失页关键摘录

- p.15: Fig.1 Boundary prediction results for scenes in ScanNet （Gong et al .， 2021 b）1755
- p.16: Fig.2 Framework of hybrid contrastive regularization （Li et al .， 2022 a）1756
- p.19: and Gall J . 2019 . SemanticKITTI ： a dataset for semantic scene
- p.19: modal dataset for autonomous driving//Proceedings of 2020 IEEE/
- p.20: driving ？ The KITTI vision benchmark suite//Proceedings of 2012
- p.20: fication benchmark ［EB/OL ］. ［2023 -01-03］.
- p.20: hours ： self -driving motion prediction dataset//Proceedings of the
- p.22: scene understanding benchmark suite//Proceedings of 2015 IEEE
- p.22: ity in perception for autonomous driving ： waymo open dataset//Pro ⁃
- p.23: Night -time scene parsing with a large real dataset . IEEE Transac ⁃
<!-- AI_READING_NOTE_END -->
