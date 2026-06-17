---
title: Yu L and Wu X Q. 2024. Survey of texture optimization algorithms for 3D reconstructed scenes. Journal of Image and Graphics
authors:
  - "于柳"
  - "吴晓群"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.230478
pdf: [[cjig_计算机图形学_三维重建场景纹理优化算法综述.pdf]]
primary_topic: D2_3D_重建_神经辐射场_SLAM
topics:
  - "D2_3D_重建_神经辐射场_SLAM"
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
extract_cache: .paper-cache/extracts/cjig_计算机图形学_三维重建场景纹理优化算法综述.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/16 pages"
---
# Yu L and Wu X Q. 2024. Survey of texture optimization algorithms for 3D reconstructed scenes. Journal of Image and Graphics

## 基本信息
- **PDF**: [[cjig_计算机图形学_三维重建场景纹理优化算法综述.pdf]]
- **primary_topic**: `D2_3D_重建_神经辐射场_SLAM`
- **topics**: `D2_3D_重建_神经辐射场_SLAM`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 三维重建场景的纹理优化算法综述 / Survey of texture optimization algorithms for 3D reconstructed scenes |
| **作者** | 于柳; 吴晓群 (北京工商大学 计算机与人工智能学院; 食品安全大数据技术北京市重点实验室) |
| **发表时间** | 2024 (收稿 2023-07-20, 修回 2023-10-18) |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics), 29(08): 2303–2318 |
| **DOI** | 10.11834/jig.230478 |
| **基金** | 国家自然科学基金 (62272014) |

## 摘要

**英文原摘要（据 PDF 提取文本整理, 已修复空格与连字符）**：

> Texture optimization is an important task in the field of computer graphics and computer vision, and it plays an essential role in creating realistic 3D reconstructed scenes, which aims to enhance the quality of texture mapping for 3D reconstructed scenes. It has various applications in digital entertainment, heritage restoration, smart cities, virtual/augmented reality, and other fields. To achieve complete texture mapping, a single image is often insufficient, and multiple-angle color images are required. By combining these images and projecting them onto the 3D scene, high-quality texture mapping can be achieved, ideally with consistent luminosity across all images. However, the accuracy of 3D reconstruction can be impacted by errors in camera pose estimation and geometry, which result in misaligned projected images. This limitation restricts the use of 3D scenes in various fields, which makes 3D scene texture optimization a crucial task. Texture optimization algorithms have two main types: traditional and deep learning-based optimization algorithms. Traditional optimization algorithms typically aim to reduce the accumulated error of camera pose and the impact of reconstruction geometry accuracy on texture mapping quality, often involving image fusion, image stitching, and joint texture and geometry optimization. Deep learning-based optimization algorithms use neural networks to optimize 3D scene textures, and can be further classified into convolutional neural network-based, GAN-based, neural textures, and text-driven diffusion model optimization algorithms. The future trend of texture optimization is likely to be deep learning-based optimization algorithms, which can effectively reduce computational costs and enhance visual realism.

**中文翻译**：

> 三维重建场景的纹理优化是计算机图形学与计算机视觉领域的基础任务之一，对生成逼真的三维重建场景至关重要，其目的是提升三维重建场景纹理映射的质量。它在数字娱乐、遗产修复、智慧城市、虚拟/增强现实等领域有广泛应用。要实现完整的纹理映射，单幅图像往往不够，需要多角度的彩色图像；将这些图像组合并投影到三维场景上，理想情况下可得到光度一致、质量较高的纹理映射。然而，相机姿态估计与几何重建的误差会影响三维重建的精度，导致投影图像错位，限制了三维场景的应用，使三维场景纹理优化成为一项关键任务。纹理优化算法主要分两类：传统算法与基于深度学习的算法。传统算法通常旨在减小相机姿态累积误差及重建几何精度对纹理映射质量的影响，主要包括基于图像融合、基于图像拼接以及纹理与几何联合优化三类；基于深度学习的算法利用神经网络优化三维场景纹理，可进一步分为基于卷积神经网络、基于 GAN、神经表示（神经纹理）和文本驱动的扩散模型四类。纹理优化未来的发展趋势很可能是基于深度学习的算法，它能有效降低计算成本并增强视觉真实感。

> **关键词**: 场景重建; 纹理优化; 图像融合; 图像拼接; 联合优化

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：三维场景重建以图形/图像为输入，重构场景的三维几何信息与物理属性，已深入应用于工业、军事、医学、教育、文化等行业。但受采集设备限制与人为因素影响，输入数据常存在噪声、模糊、缺失；重建算法本身也会引入几何误差、特征模糊与纹理失真，使重建场景无法直接用于相关领域。因此优化纹理、提升细节表现尤为重要。
- **之前方法的问题**：当前主流采集设备包括激光测距仪、单目相机、立体相机和 RGB-D 相机。单目/多目立体方案依赖环境光获取 RGB 并预测深度图，但场景结构变化、对象遮挡使精确深度估计困难，实际无法保证几何精度。基于 RGB-D 的重建（图像预处理→配准→曲面融合）大多采用截断符号距离函数（TSDF, Curless & Levoy 1996）作为深度集成的隐式表示，其移动加权平均策略虽能降噪，却会导致几何过度平滑、缺少锐利细节，并进一步引起颜色纹理的模糊与伪影；加之测量/量化误差和相机姿态累积误差，重建几何与纹理细节往往不能满足实际应用要求。
- **作者想解决的核心矛盾**：如何在有限的相机姿态精度和几何重建精度下，通过纹理优化算法（传统优化与深度学习方法）减小三维几何体与纹理图像之间的对齐误差，恢复场景细节，提升纹理的视觉逼真度与一致性。

## 关键贡献

1.  **系统分类框架**：将现有纹理优化算法划分为传统算法（基于图像融合、基于图像拼接、纹理与几何联合优化）和基于深度学习的算法（CNN、GAN、神经表示/神经纹理、扩散模型）两大类并细分子类。
2.  **文献综述与对比**：选取 38 篇高质量代表性文献详细分析，用图 1 统计文献年份分布、图 2 统计各类算法文献数量，并用表 2/3/4/6 汇总各算法年份、主要思想与优缺点。
3.  **数据集与评价指标汇总**：系统梳理 10 个常用数据集（TUM、ICL-NUIM、Sun 3D、Fountain、ShapeNet、Matterport 3D、ScanNet、SceneNet、BundleFusion、Replica，附下载链接，见表 1），并明确纹理优化指标（MSE、PSNR、SSIM）与几何优化指标（IoU、HD、MD）的含义与方向。
4.  **定性与定量分析**：在 Fountain 与 ScanNet 上对 4 种传统算法做定量比较（表 5），并在 ScanNet/Fountain/BundleFusion 上给出定性对比（图 4、7、8）。
5.  **挑战与趋势**：总结当前纹理优化面临的挑战，指出基于深度学习的算法因能结合先验知识、降低计算成本、增强视觉真实感，是未来主要发展方向。

## 方法

本文是综述，"方法"部分梳理其介绍的各类算法核心思想与流程。

**整体框架**：纹理优化被视为后处理过程，输入是粗略三维几何模型 + 多视角彩色图像（可伴深度信息），输出是视觉质量提升的带纹理三维模型。简单做法是组合多角度彩色图像直接投影到三维场景，但相机姿态累积误差会导致投影图像错位、几何不准确会导致纹理失真，故直接投影通常伴随模糊与伪影。算法目标是减小投影误差、消除接缝、保持颜色一致性与几何细节。

**传统纹理优化算法**（输入为重建三维几何体 + 全局配准的多幅彩色图像，输出为纹理三维模型）：
- **基于图像融合**（侧重三维模型与小规模场景）：在用混合权重函数对多幅纹理图像的颜色样本加权平均前，通过优化相机姿态、对图像添加变形函数等减少模糊伪影。Zhou & Koltun (2014) 优化相机姿态以最大化光度一致性并为每幅图加变形函数，但局部变形无法纠正较大几何错位，且需细分网格导致数据量增大；Jeon et al. (2016) 改为全局纹理图渲染，利用顶点-环邻域局部信息并行优化纹理坐标，几十秒生成全局纹理图，较 Zhou & Koltun 提速近 100 倍；翟昌杰和秦学英 (2017) 求解漫反射分量并综合成像质量/遮挡/光照设计混合权重；Bi et al. (2017) 用双向相似性 (BDS, Simakov 2008) 基于块重新生成配准图像；Li et al. (2019b) 用多重网格扭曲修复未对齐并做全局多视图颜色校正；Lee et al. (2020) 与 Kim et al. (2022) 采用基于体素的实时纹理融合（Lee 用正交投影 + 透视贴图、Kim 在重建中建立并更新全局纹理图谱），但多视角光照不一致时仍产生模糊伪影。
- **基于图像拼接**（侧重大规模场景，在视觉质量与数值效率间权衡）：按视角位置、图像分辨率等构造能量函数，为每个三角面片选最佳图像，重点是解决相邻面片用不同图像产生的接缝。Lempitsky & Ivanov (2007) 首次将接缝最小化建模为网格上的马尔可夫随机场 (MRF) 能量函数 E(l)=Σ E_data + Σ E_smooth，用三角面片法线与相机视角夹角作选图标准并引入校平函数；Allene et al. (2008) 改用投影面积、Gal et al. (2010) 改用梯度指标改进数据项；Waechter et al. (2014) 综合视角选择标准改进数据项，并在优化顶点颜色基础上同时优化顶点邻接边颜色以消除边界不连续；姜翰青等 (2015) 分块映射并修复不可见区域纹理；刘彬等 (2015) 加权生成贴片像素 + 多分辨率分解融合消缝；Li et al. (2019a) 移动纹理坐标减少对齐误差，较 Gal et al. (2010) 平均提速约 50%；Fu et al. (2018) 用颜色/几何一致性调整每块相机姿态并引入变换矩阵细化边界纹理坐标；Li et al. (2020) 引入平面先验作 MRF 平滑项约束；Fu et al. (2023) 在选图时对纹理细节加权并用 Bi et al. (2017) 重合成边界，结果比 Fu et al. (2018) 更清晰；Sheng et al. (2021) 将空间连续最大流扩展到三维网格不规则图，较 Waechter et al. (2014) 大规模室外效率大幅提升。
- **纹理与几何联合优化**：认为残余的顶点颜色/投影颜色不一致源于几何误差，故同时优化相机姿态、纹理颜色与几何顶点位置。Maier et al. (2017) 用空间可变照明模型处理光照变化，但易导致纹理复制；室内场景方法（Huang et al. 2017; Wang & Guo 2018, 2019）在曼哈顿世界假设下用平面基元优化几何与纹理——Huang 引入纹理锐化与跨帧颜色校正、生成清晰高保真纹理但耗时，Wang & Guo (2018) 简化网格提速但纹理不及 Huang 清晰且不能填补 RGB-D 孔洞，Wang & Guo (2019) 结合线特征约束与平面先验、更好处理边界过平滑并保持边界颜色一致；Fu et al. (2020) 结合光度/几何一致性同时优化相机姿态与顶点坐标并用法线约束增强细节，较 Fu et al. (2018) 有效消除接缝。

**基于深度学习的纹理优化算法**：
- **基于卷积神经网络 (CNN)**：高明慧等 (2019) 在 CNN 基础上加批量归一化 (BN) 层提速并减少过拟合（VGGNet 改进）；Liu et al. (2021) 用级联全卷积网络以渐进自适应方式细化噪声模型的体积表示、降低计算成本，但无法恢复大面积遮挡缺失；Zhi et al. (2020) 基于光度一致性重建时空一致网格与高分辨率反照率纹理；Dai et al. (2021) 用 2D 视图引导、自监督联合修复缺失几何与颜色；Wei et al. (2021) 用 3D 自先验 + 2D 自先验 CNN 联合预测纹理贴图与顶点位置；赵明华等 (2022) 重构亮度分量恢复逆光区颜色、缓解曝光过度；都双丽等 (2023) 用暗通道先验提亮、解决色彩失真。
- **基于生成对抗网络 (GAN)**：生成器生成优化纹理、判别器辨别真伪并迭代。Huang et al. (2020) 每次迭代随机取两幅不同姿态图像输入、用鉴别器辨别渲染纹理与真实纹理；Zhang et al. (2023) 将场景渲染为多视图、比较渲染图与输入图一致性并通过可微渲染器反传，同时更新相机参数、顶点位置与纹理颜色；Siddiqui et al. (2022) 将 GAN 与编码器-解码器结合（用 Karras et al. 2020 网络编码特征向量），用两个鉴别器评判真实视图与渲染视图差异，无需二维-三维对应即可生成完整纹理。
- **基于神经表示（神经纹理）**：Thies et al. (2019) 首次提出神经纹理 (neural texture)，据光源与相机姿态重算每像素颜色，可在复杂场景合成高质量纹理，但训练成本高且受数据集限制；后续工作将神经辐射场 (NeRF) 与其他架构结合——Baatz et al. (2022) 将表面属性表示为随空间位置变化的连续函数并用 MLP 预测各视角密度进而算颜色，Sun et al. (2023) 将几何与纹理信息转为低维特征向量、解码为高质量三维纹理并结合法向/深度由渲染器映射回模型。NeRF 无需显式几何即可高质量渲染，但训练复杂度高，与其他架构结合可提升纹理逼真度。
- **基于扩散模型**：扩散模型 (diffusion) 具良好可扩展性与泛化能力。Song et al. (2023) 基于 2D 扩散文本生成高保真三维场景纹理，用单目深度预测作伪监督对齐场景平滑区域（提取文本在此处截断，后续内容据原文后续页未覆盖；表 6 另列 Richardson et al. 2023 文本引导扩散，主要思想"无缝、高保真"）。

**与已有方法的差异**：传统方法依赖物理模型与几何约束、计算过程明确但复杂耗时、对几何精度敏感；深度学习方法利用大数据学习强先验、自动优化纹理，但训练成本高、可解释性弱、依赖训练数据。
## 实验

- **使用的数据集**（表 1，10 个）：TUM benchmark (Sturm 2012, 39 序列, Kinect 室内)、ICL-NUIM (Handa 2014, 8 序列, 合成室内)、Sun 3D (Xiao 2013, 415 序列, 大规模室内)、Fountain (Zhou & Koltun 2014, 手持 RGB-D, 物体)、ShapeNet (Chang 2015, 51 300 模型/55 类, 物体, 训练/验证/测试 70%/20%/10%)、Matterport 3D (Chang 2017, 90, 大规模)、ScanNet (Dai 2017a, 1 513 场景, 训练/测试 80%/20%)、SceneNet (Handa 2016, 57, 室内, 合成)、BundleFusion (Dai 2017b, 8, 室内)、Replica (Straub 2019, 18 室内场景)。表 1 同时给出年份、数据量、类别、彩色/深度/相机姿态/三维模型/真值的有无、场景规模与获取方式。
- **评价指标**：纹理质量用 MSE（越小越好）、PSNR（越高越好）、SSIM（[-1,1]，越大越相似）；几何质量用 IoU（重建结果与真值交并比）、Hausdorff 距离 HD（越小越相似）、平均距离 MD（顶点到几何体 M 的距离除以网格 M0 面积的表面积分）。
- **对比方法**：定量比较（表 5）对比 Zhou & Koltun (2014)、Lee et al. (2020)、Kim et al. (2022)、Fu et al. (2018) 四种传统算法。
- **主实验结果**（表 5，加粗为各列最优）：
    - **Fountain**：Zhou & Koltun (2014) PSNR=19.410 dB / SSIM=0.382（最优）；Kim PSNR=18.428/SSIM=0.295；Lee PSNR=18.186/SSIM=0.358；Fu(2018) PSNR=18.060/SSIM=0.318。
    - **ScanNet Scene 0000_00**：Zhou & Koltun PSNR=17.714/SSIM=0.719（PSNR、SSIM 均最优）；Kim PSNR=17.466/SSIM=0.711；Fu(2018) PSNR=15.399/SSIM=0.572；Lee PSNR=14.810/SSIM=0.638。
    - **ScanNet Scene 0261_02**：Kim PSNR=22.294（最优）/SSIM=0.761；Zhou & Koltun PSNR=22.028/SSIM=0.783（SSIM 最优）；Fu(2018) PSNR=16.424/SSIM=0.633；Lee PSNR=15.394/SSIM=0.685。
    - 注：表 5 表头将 ScanNet 两场景标注为 Dai 等 2017b（与正文 ScanNet=Dai 2017a 略有出入，按原文记录）。
- **定性结果**：图 4 比较 Lee (2020) 与 Kim (2022) 在 ScanNet 两场景；图 7 比较 Waechter (2014)、Fu (2018)、Fu (2023) 在 Fountain，Fu(2023) 明显优于另两者，Waechter 因未优化相机姿态而含明显错位与接缝；图 8 比较 Huang (2017)、Wang & Guo (2018, 2019) 在 BundleFusion，Huang 纹理清晰度更优、另两者更侧重整体效果。
- **消融/泛化实验**：作为综述本文不含自身方法的消融或泛化实验。
- **效率信息**：Jeon et al. (2016) 较 Zhou & Koltun (2014) 提速近 100 倍；Li et al. (2019a) 较 Gal et al. (2010) 平均提速约 50%；Sheng et al. (2021) 大规模室外效率大幅提升；联合优化与神经纹理训练计算成本高。论文未提供统一的 FLOPs/运行时间表。
## 局限

1.  **深度学习方法缺乏统一定量比较**：表 5 的定量对比只覆盖 4 种传统算法（Fountain + ScanNet），对 CNN/GAN/神经表示/扩散模型主要做定性综述（表 6 列优缺点），不同深度学习范式之间的性能差距不够明确。
2.  **时效性与覆盖范围**：作为投稿于 2023、刊于 2024 的综述，可能未涵盖最新的 3D 生成扩散与高斯泼溅等突破；对 NeRF 及其变体在纹理优化中的应用介绍相对简略。
3.  **侧重分类、深度有限**：为求全面覆盖，对单个算法的原理细节讲解偏总结性。
4.  **挑战讨论较泛**：对复杂场景、特殊材质、计算成本等挑战的讨论较宏观，缺乏针对性的深入分析或解决方案。
## 个人评论

1.  **清晰的领域入门地图**：对初入纹理优化方向的研究者，本文给出从问题定义、采集设备、TSDF 平滑/伪影成因，到"传统（融合/拼接/联合）→深度学习（CNN/GAN/神经表示/扩散）"的完整脉络与代表作，便于快速建立全局认知。
2.  **可迁移的对比框架**：表 2/3/4/6 的"主要思想 + 优缺点"逐条对照，是定位自身工作类别、寻找改进点的现成模板；其按"小规模物体 vs 大规模室外/室内"划分算法适用范围的视角尤其实用。
3.  **实用的资源汇总**：表 1 的 10 个数据集（含下载链接、是否含深度/姿态/真值/三维模型）与 MSE/PSNR/SSIM/IoU/HD/MD 指标说明，可直接用于实验设计与论文写作，省去从头搜集。
4.  **趋势判断明确但留白**：作者押注深度学习方向并强调其"结合先验、降本、增真"的优势，但本文成稿时间偏早，3D 高斯泼溅 (3DGS)、更强的文本/图像扩散纹理生成等近年主线着墨不足，读者宜把它当作"2023 年前的快照"并自行补充最新工作。

### 使用建议

- **如果快速了解**：精读摘要、引言、第 2 章开头（分类框架）与第 2 章每小节首段（概述），再浏览图 1、2、表 5、6，即可把握领域全貌。
- **如果复现**：本文是综述、不含新方法，但可依表 1 的链接获取基准数据，依表 2-4 和表 6 找到目标算法原始论文（如 Zhou & Koltun 2014、Waechter 2014、Fu 2018/2020/2023、Thies 2019、Baatz 2022）。
- **如果借鉴创新点**：重点学习其分类体系与问题定义，思考自身工作所属类别及跨类别结合（如用深度网络预测传统融合的权重函数、在神经渲染中引入平面/线几何约束、用扩散先验补全大面积缺失纹理）；表 2-4/6 的"缺点"列是改进点提示。
- **如果写 Related Work**：可将本文作为"三维重建纹理优化"主题的综述性引用支撑背景与重要性，再按自身方法所属子类（如基于神经辐射场的纹理优化）引用其介绍的相关工作。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[D2_3D_重建_神经辐射场_SLAM]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是一篇综述，系统梳理三维重建场景中纹理优化算法的进展，属计算机图形学与计算机视觉的交叉领域，聚焦三维场景重建的后处理阶段，旨在解决重建模型纹理模糊、失真与接缝问题以提升视觉质量。可作为"3D 重建""纹理优化""深度学习在三维视觉中的应用"等主题下的文献综述参考。刊于《中国图象图形学报》29(08):2303-2318，国家自然科学基金 (62272014) 资助。

## 2. 一句话总结
本文从传统算法（基于图像融合、图像拼接、纹理与几何联合优化）和基于深度学习的算法（CNN、GAN、神经表示/神经纹理、扩散模型）两大类、共 38 篇代表性文献综述三维重建场景纹理优化，汇总 10 个数据集与 MSE/PSNR/SSIM/IoU/HD/MD 指标，并在 Fountain、ScanNet 上对 4 种传统算法做定量比较。

## 3. 背景与问题
- **为什么要做**：三维重建广泛应用于工业、军事、医学、教育、文化等行业，但采集设备限制、噪声/模糊/缺失数据以及重建算法引入的几何误差、特征模糊、纹理失真，使重建场景无法直接应用，纹理优化因此至关重要。
- **之前方法的问题**：单目/立体方案受结构变化与遮挡影响、难保证几何精度；RGB-D 重建普遍用 TSDF 隐式表示，其移动加权平均会使几何过度平滑、缺少锐利细节，并引起颜色纹理模糊与伪影；加上测量/量化与相机姿态累积误差，几何与纹理细节常不达标。
- **核心矛盾**：在有限的相机姿态与几何精度下，如何通过纹理优化算法减小三维几何体与纹理图像间的对齐误差、恢复细节、提升逼真度与一致性。

## 4. 核心贡献
1.  **系统分类框架**：传统算法（图像融合、图像拼接、纹理与几何联合优化）+ 深度学习算法（CNN、GAN、神经表示、扩散模型）两大类并细分子类。
2.  **文献综述与对比**：选 38 篇高质量文献，图 1 统计年份分布、图 2 统计各类算法数量，表 2/3/4/6 汇总主要思想与优缺点。
3.  **数据集与指标汇总**：10 个数据集（表 1，含下载链接）；纹理指标 MSE/PSNR/SSIM、几何指标 IoU/HD/MD 的含义与方向。
4.  **定性与定量分析**：表 5 在 Fountain、ScanNet 上定量对比 4 种传统算法；图 4/7/8 给出定性比较。
5.  **挑战与趋势**：指出深度学习方法因结合先验、降本、增真而成为未来主要方向。

## 5. 方法详解
本文是综述，"方法详解"梳理各类算法核心思想与流程。

**整体框架**：纹理优化是后处理，输入为粗略三维几何 + 多视角彩色图像（可含深度），输出为视觉质量提升的带纹理模型。直接投影因姿态累积误差错位、几何不准失真而伴随模糊伪影；目标是减小投影误差、消除接缝、保持颜色一致与几何细节。

**传统纹理优化算法**：
- **基于图像融合**（小规模/物体）：加权平均前先优化姿态/加变形函数。Zhou & Koltun (2014) 优化姿态 + 图像变形（需细分网格、数据量增大，局部变形难纠正大错位）；Jeon et al. (2016) 并行优化纹理坐标、全局纹理图渲染、提速近 100 倍；翟昌杰和秦学英 (2017) 求漫反射 + 混合权重；Bi et al. (2017) 双向相似性 (BDS) 基于块重配准；Li et al. (2019b) 多重网格扭曲 + 全局多视图颜色校正；Lee et al. (2020)、Kim et al. (2022) 实时体素纹理融合（Lee 正交投影 + 透视贴图、Kim 全局纹理图谱）。
- **基于图像拼接**（大规模，质量/效率权衡）：为每个三角面片选最佳图像、再消接缝。Lempitsky & Ivanov (2007) 首次建模为 MRF 能量函数（法线-视角夹角 + 校平函数）；Allene et al. (2008) 投影面积、Gal et al. (2010) 梯度改进数据项；Waechter et al. (2014) 综合视角标准 + 同时优化顶点与邻接边颜色；姜翰青等 (2015) 分块映射 + 不可见纹理修复；刘彬等 (2015) 多分辨率分解融合消缝；Li et al. (2019a) 移动纹理坐标、较 Gal 提速约 50%；Fu et al. (2018) 颜色/几何一致性调姿态 + 变换矩阵细化边界；Li et al. (2020) 平面先验作 MRF 平滑约束；Fu et al. (2023) 纹理细节加权 + Bi 重合成边界（优于 Fu 2018）；Sheng et al. (2021) 空间连续最大流扩展到三维网格、大规模室外提效。
- **纹理与几何联合优化**：同时优化相机姿态、纹理颜色、几何顶点。Maier et al. (2017) 空间可变照明模型（易纹理复制）；Huang et al. (2017)、Wang & Guo (2018, 2019) 曼哈顿世界假设下用平面基元（Huang 清晰高保真但耗时、Wang&Guo 2018 提速但不及清晰且不补孔洞、Wang&Guo 2019 线特征 + 平面先验、边界更好）；Fu et al. (2020) 光度/几何一致性 + 法线约束，较 Fu 2018 消除接缝。

**基于深度学习的纹理优化算法**：
- **CNN**：高明慧等 (2019) 加 BN 层提速（VGGNet 改进）；Liu et al. (2021) 级联全卷积渐进细化体积表示、降本（无法恢复大遮挡）；Zhi et al. (2020) 光度一致性重建时空一致网格 + 高分反照率；Dai et al. (2021) 2D 视图引导自监督联合修复几何与颜色；Wei et al. (2021) 3D+2D 自先验联合预测纹理与顶点；赵明华等 (2022) 重构亮度恢复逆光区；都双丽等 (2023) 暗通道先验提亮去色失真。
- **GAN**：Huang et al. (2020) 随机两姿态图像 + 鉴别器辨真伪；Zhang et al. (2023) 多视图渲染 + 可微渲染器反传、联合更新相机/顶点/纹理；Siddiqui et al. (2022) GAN + 编解码（Karras 2020 网络）、双鉴别器、无需二三维对应。
- **神经表示**：Thies et al. (2019) 首提神经纹理（据光源/姿态重算像素颜色，训练成本高）；Baatz et al. (2022) 表面属性为连续函数 + MLP 预测各视角密度；Sun et al. (2023) 低维特征向量解码为三维纹理 + 法向/深度映射回模型。NeRF 无需显式几何即可高质量渲染，但训练复杂度高。
- **扩散模型**：Song et al. (2023) 2D 扩散文本生成高保真三维场景纹理 + 单目深度伪监督对齐（提取文本此处截断，后续据原文后续页未覆盖；表 6 另含 Richardson et al. 2023 文本引导扩散）。

**与已有方法差异**：传统方法依赖物理/几何约束、明确但耗时、对几何敏感；深度学习方法学强先验、自动优化，但训练成本高、可解释性弱、依赖数据。

## 6. 实验与结果
- **数据集**（表 1）：TUM、ICL-NUIM、Sun 3D、Fountain、ShapeNet、Matterport 3D、ScanNet、SceneNet、BundleFusion、Replica，附数据量/类别/数据类型/场景规模/获取方式。
- **指标**：纹理 MSE（小好）/PSNR（高好）/SSIM（大好，[-1,1]）；几何 IoU/HD（小好）/MD。
- **对比方法**（表 5）：Zhou & Koltun (2014)、Lee et al. (2020)、Kim et al. (2022)、Fu et al. (2018)。
- **主结果**（表 5，加粗最优）：
    - Fountain：Zhou & Koltun PSNR=19.410/SSIM=0.382（均最优）。
    - ScanNet Scene 0000_00：Zhou & Koltun PSNR=17.714/SSIM=0.719（均最优），Kim PSNR=17.466/SSIM=0.711。
    - ScanNet Scene 0261_02：Kim PSNR=22.294（最优），Zhou & Koltun SSIM=0.783（最优），二者互有胜负。
- **定性**：图 4（ScanNet, Lee/Kim）、图 7（Fountain, Waechter/Fu2018/Fu2023，Fu2023 最优）、图 8（BundleFusion, Huang/Wang&Guo2018/2019，Huang 最清晰）。
- **消融/泛化**：综述不含自身方法实验。
- **效率**：Jeon 较 Zhou&Koltun 提速近 100 倍；Li(2019a) 较 Gal 提速约 50%；Sheng 大规模室外提效；无统一 FLOPs/时间表。

## 7. 这篇论文真正有价值的地方
1.  **领域入门地图**：从问题成因（TSDF 平滑/伪影）到"传统→深度学习"脉络与代表作一应俱全，快速建立全局认知。
2.  **可迁移的对比框架**：表 2/3/4/6 的"主要思想 + 优缺点"逐条对照，便于定位自身工作并寻找改进点；按场景规模划分适用范围尤为实用。
3.  **实用资源汇总**：10 个数据集（含链接、含/不含深度/姿态/真值/三维模型）与 6 类指标说明，可直接用于实验设计与写作。
4.  **明确的趋势指引**：押注深度学习方向，并点出复杂场景、特殊材质、计算效率等挑战，为选题提供方向。

## 8. 局限与问题
1.  **深度学习缺统一定量比较**：表 5 仅覆盖 4 种传统算法，深度学习部分主要定性，范式间性能差距不明确。
2.  **时效性**：成稿偏早，3DGS、更强扩散纹理生成等近年主线着墨不足；NeRF 变体介绍偏简略。
3.  **侧重分类、深度有限**：单算法原理讲解偏总结性。
4.  **挑战讨论较泛**：对复杂场景/特殊材质/计算成本的讨论宏观，缺针对性方案。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要、引言、第 2 章开头与各小节首段 + 图 1/2、表 5/6。
- **复现**：依表 1 链接取数据，依表 2-4/6 找目标算法原文（如 Zhou&Koltun 2014、Waechter 2014、Fu 2018/2020/2023、Thies 2019、Baatz 2022）。
- **借鉴创新点**：学其分类体系与问题定义，思考跨类别结合（深度网络预测融合权重、神经渲染加几何约束、扩散先验补全缺失纹理）；表 2-4/6 的"缺点"列是改进提示。
- **写 Related Work**：作为"三维重建纹理优化"主题综述性引用，再按自身子类引用其介绍的相关工作。

## 10. 和其他论文的关系
基于主题 `D2_3D_重建_神经辐射场_SLAM`，可能相关的论文包括：
- `[[NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis]]`：本文 2.2.3 节神经表示算法（Baatz 2022、Sun 2023）的基础。
- `[[BundleFusion: Real-time Globally Consistent 3D Reconstruction using Online Surface Re-integration]]`：本文 1.1 节 BundleFusion 数据集 (Dai 2017b) 来源，也是图 8 联合优化定性分析所用数据集。
- 表内被反复引用的奠基工作：Zhou & Koltun (2014) 提出 Fountain 数据集并贯穿表 5；Waechter et al. (2014, MVS-Texturing) 是大规模拼接代表；Thies et al. (2019) 首提神经纹理。
- 提取文本未直接出现 NICE-SLAM、TextureNet、Diffusion-based Texture Generation 等条目，原笔记中的这些链接为主题外推，已删去以免误导。

## 11. 关键词
场景重建; 纹理优化; 纹理映射; 图像融合; 图像拼接; 联合优化; 深度学习; 卷积神经网络; 生成对抗网络; 神经辐射场; 神经纹理; 扩散模型; 综述

## 12. 可信度说明
本笔记基于 PDF 提取文本（前 12 页，覆盖摘要、引言、数据集与评价标准、传统算法全部三小节及深度学习算法 2.2.1-2.2.4 开头）生成。算法分类、各算法核心思想、数据集与指标列表、表 5 定量结果（PSNR/SSIM）均严格据提取文本核对（表 5 表头将 ScanNet 标为 Dai 2017b、与正文 Dai 2017a 略有出入，已按原文记录）。扩散模型小节在 Song et al. (2023) 处提取文本截断，后续内容据原文后续页未覆盖、已标注待核。深度学习方法缺乏统一基准结果，原文如此。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/cjig_计算机图形学_三维重建场景纹理优化算法综述.txt` (提取 12/16 页, 全文 16 页; 原 AI 主体 12/16 + 全文补读 13-16); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮据提取文本重核摘要与表 5 数值、补足各算法细节、清理无据外推链接。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-16; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-16。
- **提取情况**: 缺失页 4 页, 其中 4 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: Proceedings of 2021 IEEE/CVF Conference on Computer Vision
- p.16: Large -scale texturing of 3D reconstructions//Proceedings of the 13th
- p.16: RGB -D video//Proceedings of the 16th European Conference on

### 缺失页关键摘录

- p.14: Handa A ， Whelan T ， McDonald J and Davison A J . 2014 . A benchmark
- p.16: combe R . 2019 . The Replica dataset ： a digital replica of indoor
- p.16: benchmark for the evaluation of RGB -D SLAM systems//Proceed ­
<!-- AI_READING_NOTE_END -->
