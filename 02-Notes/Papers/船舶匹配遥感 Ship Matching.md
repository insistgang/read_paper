---
title: Remote Sensing Image Ship Matching Utilising Line Features
authors:
  - "Leyang Li"
  - "Guixing Cao"
  - "Jun Liu"
  - "Xiaohao Cai"
year: 2023
venue: Remote Sensing Image Ship Matching Utilising Line Features
doi: 10.3390/s23239479
pdf: [[船舶匹配遥感 Ship Matching.pdf]]
primary_topic: C2_目标检测_违建_车辆_船舶_行人
topics:
  - "C2_目标检测_违建_车辆_船舶_行人"
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
extract_cache: .paper-cache/extracts/船舶匹配遥感 Ship Matching.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/16 pages"
---
# Remote Sensing Image Ship Matching Utilising Line Features

## 基本信息
- **PDF**: [[船舶匹配遥感 Ship Matching.pdf]]
- **primary_topic**: `C2_目标检测_违建_车辆_船舶_行人`
- **topics**: `C2_目标检测_违建_车辆_船舶_行人`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Remote Sensing Image Ship Matching Utilising Line Features |
| **作者** | Leyang Li; Guixing Cao; Jun Liu; Xiaohao Cai |
| **发表时间** | 2023 |
| **刊物/会议** | Remote Sensing Image Ship Matching Utilising Line Features |
| **DOI** | 10.3390/s23239479 |

## 摘要

> :Theexistingimagematchingmethodsforremotesensingscenesareusuallybasedonlocal features.ThemostcommonlocalfeatureslikeSIFTcanbeusedtoextractpointfeatures.However, thiskindofmethodsmayextracttoomanykeypointsonthebackground,resultinginlowattention tothemainobjectinasingleimage,increasingresourceconsumptionandlimitingtheirperformance. Toaddressthisissue,weproposeamethodthatcouldbeimplementedwellonresource-limited satellitesforremotesensingimagesshipmatchingbyleveraginglinefeatures.Akeypointextraction strategycalledlinefeaturebasedkeypointdetection(LFKD)isdesignedusinglinefeaturestochoose and filter keypoints. It can strengthen the features at corners and edges of objects and also can significantlyreducethenumberofkeypointsthatcausefalsematches.Wealsopresentanend-to-end matchingprocessdependentonanewcroppatchingfunction,whichhelpstoreducecomplexity.The matchingaccuracyachievedbytheproposedmethodreaches0.972withonly313Mmemoryand 138mstestingtime.Comparedtothestate-of-the-artmethodsinremotesen

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：现有基于天基信息系统的图像处理流程通常需要将数据传回地面处理，再发回卫星，耗时较长。这是因为卫星自身的计算能力、功耗和散热受到严格限制，无法运行大型算法。因此，需要开发能在卫星上运行的高效、有效的遥感图像匹配算法。船舶是遥感中的重要目标，对其匹配有应用需求。
- **之前方法的问题**：现有的基于局部特征（如SIFT）的匹配方法，容易在背景区域提取过多关键点，导致对图像中主要目标（船舶）的关注度降低，增加了计算资源消耗和误匹配率，不适用于资源受限的卫星平台。
- **核心矛盾**：如何在**有限的计算资源（内存、功耗）** 约束下，**同时提升遥感船舶图像匹配的准确性和效率**。现有方法难以兼顾高精度与低消耗。
## 关键贡献

1.  **提出LFKD关键点提取策略**：设计了一种基于线特征的关键点检测方法（LFKD），通过LSD线段检测器生成线特征掩膜，并与图像分割掩膜结合，用于筛选SIFT生成的关键点。该方法能显著减少关键点数量，同时保留船舶边缘与角落的关键点，提升匹配质量。
2.  **设计端到端匹配流程**：引入一个新颖的裁剪补丁函数（warpAffine），实现从原始图像对到匹配结果的端到端处理，降低了流程复杂性。
3.  **创建新的遥感船舶数据集**：构建了一个包含三种船舶（航空母舰、货船、潜艇）的遥感图像数据集，图像在光照、角度和尺寸上有变化，专门用于测试遥感目标匹配方法。
4.  **验证方法的高效性与普适性**：实验证明，所提方法在自建数据集和公开数据集上，能在匹配准确率达到0.972的同时，仅占用313 M内存和138毫秒测试时间，相比现有先进方法速度提升约50%，内存节省约30%。
5.  **增强算法兼容性**：所提关键点提取方法可以与所有能获取描述子的现有CNN模型结合使用，并能提升其匹配准确率。
## 方法

**整体框架**：该方法是一个端到端的图像匹配流程，主要包括**关键点提取**和**匹配过程**两大模块（如图4所示）。输入是一对遥感图像，输出是它们之间的匹配点集。

**关键模块与流程**：
1.  **关键点提取（LFKD策略）**：
    - **输入**：单张遥感图像 I。
    - **步骤**：
        a. 使用SIFT检测器提取初始关键点集 `S_SIFT`。
        b. 使用LSD线段检测器提取线特征，得到所有线段端点集合 `S_LSD`。
        c. 生成两个掩膜矩阵：
            - `A_s`：通过图像分割模型（在遥感数据集上训练）得到的船舶等感兴趣区域掩膜。
            - `A_l`：基于 `S_LSD` 生成的线特征掩膜（将关键点位置设为1，再进行膨胀操作）。
        d. 通过逐元素相乘得到融合掩膜 `A = A_s ⊙ A_l`（公式1），该掩膜同时强调了线特征区域和船舶区域。
        e. 利用掩膜 `A` 筛选出新的关键点集 `S_LSD^A`。
        f. 最终的关键点集 `S` 为SIFT关键点与 `S_LSD^A` 的交集，即 `S = S_SIFT ∩ S_LSD^A`（公式2）。这一步过滤掉了大量背景关键点。
    - **输出**：筛选后的、更关注船舶结构的关键点集 `S`。

2.  **匹配过程**：
    - **输入**：图像对及其筛选后的关键点集。
    - **步骤**：
        a. **裁剪补丁**：对于图像 `I_i` 中的每个关键点 `k`，使用 `warpAffine` 函数以其为中心裁剪一个 **32×32** 大小的图像补丁 `I_i^k`（如图6）。
        b. **生成描述子**：使用预训练的轻量CNN模型 **HardNet**（基于L2-Net骨干）处理每个补丁，生成特征描述子 `d_i^k = f(I_i^k)`（公式3）。所有描述子构成描述子集 `D_i`。
        c. **最近邻匹配**：对于图像 `I_i` 和 `I_j` 的描述子集 `D_i` 和 `D_j`，使用 **BFMatcher** 进行最近邻搜索，寻找匹配对 `(p, q)`，满足双向最近邻条件（公式4）。
    - **输出**：匹配点集 `M_ij`。

**与已有方法的差异**：
- **传统SIFT/SURF**：直接使用点特征，关键点多且在背景区域密集，计算量大。本文通过LFKD策略大幅减少了关键点数量，并使其更聚焦于目标。
- **基于深度学习的匹配方法**：通常计算成本高，不适合资源受限平台。本文采用轻量CNN（HardNet）描述子，并通过LFKD减少了需要描述的补丁数量，实现了高效。
## 实验

- **使用的数据集**：
    1.  **自建船舶数据集**：包含12张图像，涵盖航空母舰、货船、潜艇三种类别，考虑了光照、尺寸、角度变化及多目标情况。
    2.  **NWPU VHR-10**：公开的遥感目标检测数据集，本文从中选取了包含船舶的图像进行测试。
    3.  **HRSC**：包含1680张港口船舶图像的公开数据集，船舶类型多样。
- **对比方法**：论文中对比了基于SIFT、SURF、ORB、Harris等传统点特征的方法以及一些CNN模型。具体对比方法名称在提供的PDF文本中未明确列出。
- **评价指标**：匹配准确率（Accuracy）。
- **主实验结果**：所提方法（LFKD）在自建数据集上达到了**0.972**的匹配准确率。
- **效率结果**：
    - **内存占用**：**313 M**。
    - **测试时间**：**138 ms**（每对图像）。
    - **性能提升**：相比现有先进方法（SOTA），实现了**约50%的测试速度提升**和**约30%的内存节省**。
- **消融实验**：PDF文本中提到了进行了详细的消融实验（“detailed ablation study”），但具体的消融实验结果和分析在提供的文本（前12页）中未展开。
- **泛化实验**：方法在自建数据集和两个公开数据集（NWPU VHR-10, HRSC）上均进行了实验，展示了其有效性。
- **关键点数量影响**：实验表明，对于船舶匹配任务，并非关键点越多越好。利用本文方法筛选后的稀疏关键点足以计算出准确的图像基础矩阵（仅需8个点），过多的密集关键点反而是不必要的。
## 局限

- **对分割模型的依赖**：方法的性能部分依赖于图像分割模型（用于生成掩膜`A_s`）的准确性。如果分割失败，可能会影响关键点筛选的效果。
- **数据集规模与多样性有限**：自建数据集仅12张图像，虽然进行了公开数据集验证，但自建数据集的规模较小，可能无法全面评估方法在各种复杂情况下的鲁棒性。
- **对线特征明显的场景更优**：LFD策略依赖于目标（船舶）具有清晰的线结构。对于结构模糊或纹理丰富但边缘不明显的物体，效果可能打折扣。
- **实验细节部分缺失**：提供的PDF文本未展示完整的实验对比表格、消融实验具体数据、以及在不同数据集上的详细精度-召回曲线等，这使得对方法优势的定量评估不够直观。
- **仅关注船舶**：方法是针对船舶匹配设计的，其对于其他类型遥感目标（如车辆、飞机、建筑物）的匹配效果如何，文中未探讨，泛化性有待验证。
## 个人评论

1.  **问题导向明确**：紧紧抓住了“资源受限卫星”这一特定应用场景的痛点（功耗、内存、计算时间），所有设计都围绕“高效”和“低消耗”展开，非常具有工程实践价值。
2.  **“筛选”优于“生成”的思路**：没有设计一个全新的、复杂的特征检测器，而是提出了一个聪明的**后处理筛选策略（LFKD）**。它利用线特征（对结构敏感）和分割信息（对目标敏感）来“修剪”已有的SIFT关键点，思路简洁且有效，易于与现有方法结合。
3.  **模块化与可插拔性**：LFKD策略可以作为一个独立的预处理模块，与任何能够输出描述子的CNN模型（如HardNet, SuperPoint）结合，提升了整个方法的通用性和升级潜力。
4.  **提供了面向任务的数据集**：创建了专注于船舶匹配的数据集，考虑了影响匹配的实际因素（光照、角度、尺度），为后续研究提供了便利。

### 使用建议

- **快速了解**：只需阅读**摘要（Abstract）**、**引言（Introduction）** 的后半部分（贡献点）、**图4（框架图）** 和**实验部分（Section 4）的开头与结论**。
- **复现**：重点看**3.1节（关键点提取）** 和**3.2节（匹配过程）**，理解LFKD策略和补丁裁剪、描述子生成的完整流程。需要关注使用的具体工具（LSD， HardNet， BFMatcher）及其参数。
- **借鉴创新点**：
    1.  学习 **“利用先验信息（线特征、分割）筛选现有特征点”** 的思路，可应用于其他目标（如车辆、建筑物）的匹配任务。
    2.  学习其 **“端到端轻量流程”** 的设计思想，在资源受限场景下如何平衡精度与效率。
    3.  参考其创建面向任务的评估数据集的方法。
- **写Related Work**：可将其归类为 **“基于线特征的图像匹配”**、**“面向资源受限平台的轻量化视觉算法”** 以及 **“遥感图像目标匹配”** 等相关工作类别下。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C2_目标检测_违建_车辆_船舶_行人]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**遥感图像处理与计算机视觉**方向，具体聚焦于**遥感图像中的船舶目标匹配**任务。其核心是为资源受限的卫星平台设计一种高效、高精度的船舶图像匹配方法。该研究适用于`C2_目标检测_违建_车辆_船舶_行人`主题，特别是其中的船舶目标检测与匹配子领域。

## 2. 一句话总结
本文提出了一种利用线特征（LFKD）来筛选和优化关键点，并结合轻量CNN描述子与裁剪补丁函数的端到端方法，以实现资源受限卫星上遥感船舶图像的高效、高精度匹配。

## 3. 背景与问题
- **为什么要做**：现有基于天基信息系统的图像处理流程通常需要将数据传回地面处理，再发回卫星，耗时较长。这是因为卫星自身的计算能力、功耗和散热受到严格限制，无法运行大型算法。因此，需要开发能在卫星上运行的高效、有效的遥感图像匹配算法。船舶是遥感中的重要目标，对其匹配有应用需求。
- **之前方法的问题**：现有的基于局部特征（如SIFT）的匹配方法，容易在背景区域提取过多关键点，导致对图像中主要目标（船舶）的关注度降低，增加了计算资源消耗和误匹配率，不适用于资源受限的卫星平台。
- **核心矛盾**：如何在**有限的计算资源（内存、功耗）** 约束下，**同时提升遥感船舶图像匹配的准确性和效率**。现有方法难以兼顾高精度与低消耗。

## 4. 核心贡献
1.  **提出LFKD关键点提取策略**：设计了一种基于线特征的关键点检测方法（LFKD），通过LSD线段检测器生成线特征掩膜，并与图像分割掩膜结合，用于筛选SIFT生成的关键点。该方法能显著减少关键点数量，同时保留船舶边缘与角落的关键点，提升匹配质量。
2.  **设计端到端匹配流程**：引入一个新颖的裁剪补丁函数（warpAffine），实现从原始图像对到匹配结果的端到端处理，降低了流程复杂性。
3.  **创建新的遥感船舶数据集**：构建了一个包含三种船舶（航空母舰、货船、潜艇）的遥感图像数据集，图像在光照、角度和尺寸上有变化，专门用于测试遥感目标匹配方法。
4.  **验证方法的高效性与普适性**：实验证明，所提方法在自建数据集和公开数据集上，能在匹配准确率达到0.972的同时，仅占用313 M内存和138毫秒测试时间，相比现有先进方法速度提升约50%，内存节省约30%。
5.  **增强算法兼容性**：所提关键点提取方法可以与所有能获取描述子的现有CNN模型结合使用，并能提升其匹配准确率。

## 5. 方法详解
**整体框架**：该方法是一个端到端的图像匹配流程，主要包括**关键点提取**和**匹配过程**两大模块（如图4所示）。输入是一对遥感图像，输出是它们之间的匹配点集。

**关键模块与流程**：
1.  **关键点提取（LFKD策略）**：
    - **输入**：单张遥感图像 I。
    - **步骤**：
        a. 使用SIFT检测器提取初始关键点集 `S_SIFT`。
        b. 使用LSD线段检测器提取线特征，得到所有线段端点集合 `S_LSD`。
        c. 生成两个掩膜矩阵：
            - `A_s`：通过图像分割模型（在遥感数据集上训练）得到的船舶等感兴趣区域掩膜。
            - `A_l`：基于 `S_LSD` 生成的线特征掩膜（将关键点位置设为1，再进行膨胀操作）。
        d. 通过逐元素相乘得到融合掩膜 `A = A_s ⊙ A_l`（公式1），该掩膜同时强调了线特征区域和船舶区域。
        e. 利用掩膜 `A` 筛选出新的关键点集 `S_LSD^A`。
        f. 最终的关键点集 `S` 为SIFT关键点与 `S_LSD^A` 的交集，即 `S = S_SIFT ∩ S_LSD^A`（公式2）。这一步过滤掉了大量背景关键点。
    - **输出**：筛选后的、更关注船舶结构的关键点集 `S`。

2.  **匹配过程**：
    - **输入**：图像对及其筛选后的关键点集。
    - **步骤**：
        a. **裁剪补丁**：对于图像 `I_i` 中的每个关键点 `k`，使用 `warpAffine` 函数以其为中心裁剪一个 **32×32** 大小的图像补丁 `I_i^k`（如图6）。
        b. **生成描述子**：使用预训练的轻量CNN模型 **HardNet**（基于L2-Net骨干）处理每个补丁，生成特征描述子 `d_i^k = f(I_i^k)`（公式3）。所有描述子构成描述子集 `D_i`。
        c. **最近邻匹配**：对于图像 `I_i` 和 `I_j` 的描述子集 `D_i` 和 `D_j`，使用 **BFMatcher** 进行最近邻搜索，寻找匹配对 `(p, q)`，满足双向最近邻条件（公式4）。
    - **输出**：匹配点集 `M_ij`。

**与已有方法的差异**：
- **传统SIFT/SURF**：直接使用点特征，关键点多且在背景区域密集，计算量大。本文通过LFKD策略大幅减少了关键点数量，并使其更聚焦于目标。
- **基于深度学习的匹配方法**：通常计算成本高，不适合资源受限平台。本文采用轻量CNN（HardNet）描述子，并通过LFKD减少了需要描述的补丁数量，实现了高效。

## 6. 实验与结果
- **使用的数据集**：
    1.  **自建船舶数据集**：包含12张图像，涵盖航空母舰、货船、潜艇三种类别，考虑了光照、尺寸、角度变化及多目标情况。
    2.  **NWPU VHR-10**：公开的遥感目标检测数据集，本文从中选取了包含船舶的图像进行测试。
    3.  **HRSC**：包含1680张港口船舶图像的公开数据集，船舶类型多样。
- **对比方法**：论文中对比了基于SIFT、SURF、ORB、Harris等传统点特征的方法以及一些CNN模型。具体对比方法名称在提供的PDF文本中未明确列出。
- **评价指标**：匹配准确率（Accuracy）。
- **主实验结果**：所提方法（LFKD）在自建数据集上达到了**0.972**的匹配准确率。
- **效率结果**：
    - **内存占用**：**313 M**。
    - **测试时间**：**138 ms**（每对图像）。
    - **性能提升**：相比现有先进方法（SOTA），实现了**约50%的测试速度提升**和**约30%的内存节省**。
- **消融实验**：PDF文本中提到了进行了详细的消融实验（“detailed ablation study”），但具体的消融实验结果和分析在提供的文本（前12页）中未展开。
- **泛化实验**：方法在自建数据集和两个公开数据集（NWPU VHR-10, HRSC）上均进行了实验，展示了其有效性。
- **关键点数量影响**：实验表明，对于船舶匹配任务，并非关键点越多越好。利用本文方法筛选后的稀疏关键点足以计算出准确的图像基础矩阵（仅需8个点），过多的密集关键点反而是不必要的。

## 7. 这篇论文真正有价值的地方
1.  **问题导向明确**：紧紧抓住了“资源受限卫星”这一特定应用场景的痛点（功耗、内存、计算时间），所有设计都围绕“高效”和“低消耗”展开，非常具有工程实践价值。
2.  **“筛选”优于“生成”的思路**：没有设计一个全新的、复杂的特征检测器，而是提出了一个聪明的**后处理筛选策略（LFKD）**。它利用线特征（对结构敏感）和分割信息（对目标敏感）来“修剪”已有的SIFT关键点，思路简洁且有效，易于与现有方法结合。
3.  **模块化与可插拔性**：LFKD策略可以作为一个独立的预处理模块，与任何能够输出描述子的CNN模型（如HardNet, SuperPoint）结合，提升了整个方法的通用性和升级潜力。
4.  **提供了面向任务的数据集**：创建了专注于船舶匹配的数据集，考虑了影响匹配的实际因素（光照、角度、尺度），为后续研究提供了便利。

## 8. 局限与问题
- **对分割模型的依赖**：方法的性能部分依赖于图像分割模型（用于生成掩膜`A_s`）的准确性。如果分割失败，可能会影响关键点筛选的效果。
- **数据集规模与多样性有限**：自建数据集仅12张图像，虽然进行了公开数据集验证，但自建数据集的规模较小，可能无法全面评估方法在各种复杂情况下的鲁棒性。
- **对线特征明显的场景更优**：LFD策略依赖于目标（船舶）具有清晰的线结构。对于结构模糊或纹理丰富但边缘不明显的物体，效果可能打折扣。
- **实验细节部分缺失**：提供的PDF文本未展示完整的实验对比表格、消融实验具体数据、以及在不同数据集上的详细精度-召回曲线等，这使得对方法优势的定量评估不够直观。
- **仅关注船舶**：方法是针对船舶匹配设计的，其对于其他类型遥感目标（如车辆、飞机、建筑物）的匹配效果如何，文中未探讨，泛化性有待验证。

## 9. 我该怎么使用这篇论文
- **快速了解**：只需阅读**摘要（Abstract）**、**引言（Introduction）** 的后半部分（贡献点）、**图4（框架图）** 和**实验部分（Section 4）的开头与结论**。
- **复现**：重点看**3.1节（关键点提取）** 和**3.2节（匹配过程）**，理解LFKD策略和补丁裁剪、描述子生成的完整流程。需要关注使用的具体工具（LSD， HardNet， BFMatcher）及其参数。
- **借鉴创新点**：
    1.  学习 **“利用先验信息（线特征、分割）筛选现有特征点”** 的思路，可应用于其他目标（如车辆、建筑物）的匹配任务。
    2.  学习其 **“端到端轻量流程”** 的设计思想，在资源受限场景下如何平衡精度与效率。
    3.  参考其创建面向任务的评估数据集的方法。
- **写Related Work**：可将其归类为 **“基于线特征的图像匹配”**、**“面向资源受限平台的轻量化视觉算法”** 以及 **“遥感图像目标匹配”** 等相关工作类别下。

## 10. 和其他论文的关系
根据给定的主题`C2_目标检测_违建_车辆_船舶_行人`，本文是其中船舶目标方向的一个具体应用。可能相关的论文主题包括：
- 遥感图像中的`目标检测`方法。
- 图像匹配与配准技术，特别是面向轻量化或移动平台的算法。
- 其他基于局部特征（点、线、区域）的传统或深度学习匹配方法。
- 其他利用船舶结构信息（如线特征、轮廓）进行识别或检测的工作。

## 11. 关键词
遥感，图像匹配，线特征，船舶，卫星，资源受限，关键点检测，SIFT，LSD，轻量化

## 12. 可信度说明
本笔记主要基于提供的**PDF提取文本的前12页**内容生成，涵盖了论文的标题、作者信息、摘要、引言、方法描述、部分实验设置与结果。内容严格遵循“只基于提供文本”的原则，未编造任何信息。例如，具体的匹配准确率（0.972）、内存（313 M）和测试时间（138 ms）均直接摘自文本。对于文本中未明确说明的信息（如具体对比方法名称、完整消融实验结果），已标注“PDF文本中未明确说明”。总体提取质量良好，核心思想和关键方法描述完整，但实验细节和结论部分由于文本截断而不完整。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/船舶匹配遥感 Ship Matching.txt` (16/16 页; 原 AI 主体 12/16 + 全文补读 13-16); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-16; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-16。
- **提取情况**: 缺失页 4 页, 其中 4 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Sensors 2023 ,23, 9479 13 of 16
- p.13: Method Precision ( r) Memory Cost ( T) Testing Time ( M)
- p.13: 4.5. Discussion
- p.13: Our method can achieve good performance by combining line features and CNN at
- p.13: 5. Conclusions and Future Work
- p.13: In this paper, we created a new remote sensing dataset for ship matching and proposed
- p.13: experiments including ablation study demonstrated that the proposed method can obtain
- p.14: Sensors 2023 ,23, 9479 14 of 16
- p.14: Funding: This work is supported in part by the National Natural Science Foundation of China under
- p.14: Abbreviations
- p.14: The following abbreviations are used in this manuscript:
- p.14: DCSS Deformed Contour Segment Similarity

### 缺失页关键摘录

- p.13: Table 7. Comparison between our method with other keypoint extraction methods in image matching
- p.13: ment in running time and memory saving with great matching accuracy by combining
- p.13: is consistent with the conclusion of some existing research. In addition, we found that
- p.13: the precision achieved by methods compared on our dataset is higher than that from the
- p.13: publicly available datasets (see Tables 2 and 4). This is because our dataset owns obvious
- p.13: special structures like attention model to improve the matching accuracy. Compared with
- p.13: In this paper, we created a new remote sensing dataset for ship matching and proposed
- p.13: experiments including ablation study demonstrated that the proposed method can obtain
- p.13: better performance such as matching accuracy (i.e., 0.972 in our dataset, 0.954 and 0.889 in
- p.15: 36. Wang, A.; Pruksachatkun, Y.; Nangia, N.; Singh, A.; Michael, J.; Hill, F.; Levy, O.; Bowman, S.R. SuperGLUE: A Stickier Benchmark
- p.16: 51. Liu, Z.; Yuan, L.; Weng, L.; Yang, Y. A High Resolution Optical Satellite Image Dataset for Ship Recognition and Some New
<!-- AI_READING_NOTE_END -->
