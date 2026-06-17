---
title: "InfoNorm: Mutual Information Shaping of Normals for Sparse-View Reconstruction"
authors:
  - "Xulong Wang"
  - "Siyan Dong"
  - "Youyi Zheng"
  - "Yanchao Yang"
year: 2024
venue: "ECCV 2024 (arXiv:2407.12661)"
doi: 
pdf: [[InfoNorm.pdf]]
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
extract_cache: .paper-cache/extracts/InfoNorm.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/24 pages"
---
# InfoNorm: Mutual Information Shaping of Normals for Sparse-View Reconstruction

## 基本信息
- **PDF**: [[InfoNorm.pdf]]
- **primary_topic**: `D2_3D_重建_神经辐射场_SLAM`
- **topics**: `D2_3D_重建_神经辐射场_SLAM`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | InfoNorm: Mutual Information Shaping of Normals for Sparse-View Reconstruction |
| **作者** | Xulong Wang, Siyan Dong, Youyi Zheng, Yanchao Yang（浙江大学 CAD&CG 国家重点实验室 / Chohotech / 香港大学）|
| **发表时间** | 2024（arXiv 提交于 2024-07-17）|
| **刊物/会议** | ECCV 2024（arXiv:2407.12661v1, cs.CV）|
| **代码** | https://github.com/Muliphein/InfoNorm |
| **DOI** | 未明确 |

## 摘要

> **英文原文（据提取文本整理，已修复断词与空格）**：
> 3D surface reconstruction from multi-view images is essential for scene understanding and interaction. However, complex indoor scenes pose challenges such as ambiguity due to limited observations. Recent implicit surface representations, such as Neural Radiance Fields (NeRFs) and signed distance functions (SDFs), employ various geometric priors to resolve the lack of observed information. Nevertheless, their performance heavily depends on the quality of the pre-trained geometry estimation models. To ease such dependence, we propose regularizing the geometric modeling by explicitly encouraging the mutual information among surface normals of highly correlated scene points. In this way, the geometry learning process is modulated by the second-order correlations from noisy (first-order) geometric priors, thus eliminating the bias due to poor generalization. Additionally, we introduce a simple yet effective scheme that utilizes semantic and geometric features to identify correlated points, enhancing their mutual information accordingly. The proposed technique can serve as a plugin for SDF-based neural surface representations. Our experiments demonstrate the effectiveness of the proposed in improving the surface reconstruction quality of major states of the arts.

> **中文翻译**：
> 从多视图图像重建三维表面是场景理解与交互的基础任务。然而，复杂室内场景由于观测有限而存在歧义等挑战。近期的隐式表面表示（如神经辐射场 NeRF 与符号距离函数 SDF）借助各种几何先验来弥补观测信息的不足，但其性能严重依赖于预训练几何估计模型的质量。为缓解这种依赖，本文提出对几何建模施加正则化：显式地鼓励**高相关场景点的表面法线之间的互信息**。这样一来，几何学习过程被来自含噪（一阶）几何先验的**二阶相关性**所调制，从而消除因泛化能力差而引入的偏差。此外，本文引入一个简单有效的方案，利用语义特征与几何特征来识别相关点，并相应地增强它们之间的互信息。所提技术可作为**插件**应用于基于 SDF 的神经表面表示。实验证明该方法能够提升当前主流方法的表面重建质量。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：从多视图图像重建三维表面是计算机视觉与图形学的基础任务，应用包括 VR 内容创建与机器人-场景交互。但室内场景规模大、结构复杂，且通常只有稀疏视点，伴随遮挡与歧义。传统多视图立体（MVS）方法要求图像间有大量重叠，在稀疏视图下难以给出满意结果。
- **之前方法的问题**：结合 SDF 的 NeRF 方法（如 NeuS、VolSDF）在视图充足的简单场景上能产生高质量重建，但在大而复杂的稀疏视图场景下性能下降。后续工作（NeuRIS、MonoSDF）引入单目几何先验（法线、深度）作为额外监督来引导学习，但这些先验来自预训练估计模块，**不可避免地包含错误和噪声**，方法性能因此**高度依赖先验质量**。
- **核心矛盾 / 本文切入点**：稀疏视图下需要几何先验来补足观测，但先验是含噪、不可靠的（一阶信息）。本文从**二阶视角**切入：认为不仅几何本身重要，**场景区域之间几何的相关性**同样关键。该相关性被表述为网络权重受随机扰动时不同场景实体之间的**互信息**——即便一阶先验有噪，约束其二阶相关性仍能稳定地引导几何学习，从而消除因泛化差带来的偏差。
## 关键贡献

1.  **提出二阶几何相关性正则化（互信息形式）**：将**表面法线之间的互信息（Mutual Information）** 作为正则项引入基于 SDF 的 NeRF 表面重建。与直接把一阶几何先验当监督信号不同，这里约束的是二阶相关性，对噪声更鲁棒。
2.  **设计高效的法线互信息计算流水线**：通过度量法线关于扰动网络权重 θ_D 的梯度之间的**余弦相似度（取绝对值）** 来近似互信息（推导沿用 JacobiNeRF），并以 InfoNCE 形式实现对比损失 L_M。
3.  **提出多模态相关区域识别策略**：结合预训练**语义特征（DINO）** 与**几何特征（单目法线估计）**，通过**取交集**的方式筛选既语义相似又法线一致的像素对作为正样本，避免单一特征造成的误关联。
4.  **验证为即插即用插件**：将方法应用于 NeuS、VolSDF、GeoNeuS、I2-SDF、NeuRIS、MonoSDF、Neuralangelo 等多种基线，证明它能作为易用插件一致提升稀疏视图下的表面重建质量。
## 方法

- **整体框架**（图 2）：场景由一个 NeRF 骨干 + 一个 SDF 头 `f(x;θ)` + 一个颜色头 `c(x,v;θ)` 表示，两个头部分共享参数 θ。密度与颜色分别由经典的 eikonal 损失 L_E 与光度重建损失 L_C 监督。核心创新是只对 **SDF 分支 `f` 的一个参数子集 θ_D** 施加几何感知的**互信息损失 L_M**，使密度场学习朝着更好的表面质量收敛，而颜色分支 `c` 保持不变。
- **输入输出**：输入为一组带位姿的稀疏多视图图像；输出为场景的 SDF，最终通过提取 SDF 的零等值面得到三维网格表面。
- **关键模块**：
    1.  **SDF-based NeRF 骨干（Sec. 3.1 预备知识）**：沿相机射线采样 3D 点，MLP 预测密度 σ 与颜色 c，离散体渲染得到像素颜色（式 1）。SDF 通过函数 Φ（如 Laplace CDF）转换为体密度（式 3），并用 eikonal 损失 L_E（式 4）保持 SDF 的单位梯度特性。
    2.  **NeRF 中的互信息（Sec. 3.1）**：在网络权重子集 θ_D 上施加幅度 γ≪1 的随机扰动（噪声 n 采样自球面 S^{D-1} 上的均匀分布），对扰动后的像素做一阶泰勒展开。沿用 JacobiNeRF 的推导，两个扰动像素的互信息 ∝ |cos β|（式 5），β 为两者关于 θ_D 的梯度 ∂F_i/∂θ_D、∂F_j/∂θ_D 之间的夹角。结论：若两像素高相关，则其关于扰动参数的梯度应同向或反向。
    3.  **法线互信息度量与聚合（Sec. 3.2）**：表面法线 N(x;θ)=∂f(x;θ)/∂x（式 6）。选择对**法线**而非 SDF 值施加约束的两点理由：① 法线的计算涉及 f 的全部参数，正则更全局；② 直接约束 SDF 值可能扭曲密度，而约束 ∂f/∂x 给 SDF 值留出更多空间应对重建。法线对 θ_D 的梯度按 x/y/z 三分量拼接为 ∂N（式 7–8），再沿视角射线按体渲染权重 ω 聚合到像素 N(p_i)（式 9）。两法线像素间互信息 ∝ |N(p_i)·N(p_j)/(|N(p_i)||N(p_j)|)|（式 10），与梯度余弦相似度正相关。
    4.  **相关区域提取模块（Sec. 3.2）**：用现成视觉特征确定哪些像素对应被约束为高互信息——**语义特征 DINO**（高层场景理解）与**单目法线估计器**（低层几何感知）。对邻近图像的像素分别用余弦相似度 + 两个阈值 β_S（语义）和 β_G（几何）筛选 top 相似像素，**取交集**作为正样本对；其余随机像素作为负样本。图 3 给出动机：仅语义会把不相连区域（如墙柜与天花板）关联，仅（含噪）几何无法区分平行但不相连的平面，二者交集才能选出空间相连且法线一致的区域。
- **模块连接**：输入图像同时送入骨干与特征提取器（DINO、单目法线）；骨干负责体渲染与 L_C、L_E；特征模块在线采样正负像素对，送入互信息损失模块与 SDF 分支的法线梯度结合计算 L_M。三个损失加权求和端到端优化 θ。
- **损失函数**：互信息以**定制 InfoNCE 损失**实现（式 11）：分子为锚点 i 与正样本 i+ 法线梯度余弦相似度（取绝对值）的指数，分母对负样本 j 求和。总损失（式 12）：`L = L_C + λ_E·L_E + λ_M·L_M`，全部参数 θ 端到端训练。
- **数学公式直观解释**：
    - 式 6、9：把 3D 点法线梯度沿射线聚合到 2D 像素，建立"像素—法线梯度"关联。
    - 式 5、10：要让两个相关像素互信息高，就要让它们关于扰动参数 θ_D 的法线梯度向量尽量平行或反向（|cos| 大），即网络受扰动时相关区域几何变化应一致。
    - 式 11：InfoNCE 是实现该约束的对比工具，拉近锚点—正样本、推远锚点—负样本的法线梯度方向。
- **推理流程**：与标准 SDF-based NeRF 相同；训练完成后从 SDF 网络提取零等值面得到网格。
- **和已有方法的差异**：
    - **对比 NeuRIS / MonoSDF**：它们把单目法线/深度作为**一阶直接监督**，易受先验噪声影响；本文把法线先验仅用于**筛选相关区域**，正则目标是**二阶相关性（互信息）**，对噪声更鲁棒。
    - **对比 JacobiNeRF**：JacobiNeRF 同样用互信息，但塑造的是**颜色梯度**的互信息，用于语义标签传播；本文塑造的是**几何（法线）梯度**的互信息，用于**表面重建**正则，约束对象与任务不同（本文式 5 的互信息推导即引用 JacobiNeRF）。
    - **对比 ManhattanSDF**：后者依赖曼哈顿世界假设、主要面向平面场景；本文在含噪相关信息下可用于一般场景。
## 实验

- **使用的数据集**：**ScanNet++**（选 8 个代表性场景）与 **Replica**（选 4 个代表性场景），均为真实室内场景（办公室、卧室等）。聚焦稀疏视图，每个场景从官方扫描序列（Replica 取自 Semantic-NeRF）均匀采样 **50–85 张**图像作为输入。
- **对比方法（基线）**：作为插件应用于 **NeuS、VolSDF、GeoNeuS、I2-SDF、NeuRIS、MonoSDF、Neuralangelo**，与各自原版对比，增强版记作 NeuS+ / VolSDF+ / GeoNeuS+ 等。
- **评价指标**：**L2 Chamfer 距离**（重建与真值点集差异）与 **F-score**（综合精确率与召回率）。
- **关键实现细节（Sec. 4.2）**：对 I2-SDF 丢弃其法线与深度损失项；NeuRIS 用单目法线监督并通过多视图 patch 丢弃低置信度法线；MonoSDF 在 30k 迭代时对法线与深度损失衰减以防退化；Neuralangelo 用多分辨率 hash grid + 数值梯度，hash 编码字典大小设为 20、编码维度设为 4。
- **主实验结果（数值）**：提取缓存仅到 p.12（Sec. 4.3 开头"We can observe t…"即截断），**ScanNet++ 的 Tab.1 与 Replica 的 Tab.2 具体数值未被提取覆盖**。据原文后续页线索（提取缓存未覆盖，待核）：Replica 数值见 Tab.2，结论与 ScanNet++ 一致，即各基线加入 InfoNorm 后重建质量普遍提升。
- **消融实验（Sec. 4.4）**：据原文后续页线索（提取缓存未覆盖，待核），Tab.3 在三个场景上做消融以验证各组件必要性；并报告训练时间(h)与显存(GB)开销（p.14 出现 "Training Time (h) VRAM (GB)"）。具体数值待核。
- **效率/开销**：方法需计算法线关于网络参数的梯度（高阶导数），原文后续页（p.14）含训练时间与显存表，提取缓存未覆盖其数值，待核。
- **泛化性**：通过在 7 个不同基线上一致生效来体现作为插件的泛化能力；据原文 p.14 自陈，部分提升"有的边际、有的显著"，并将提升幅度的不一致视为一项局限。
## 局限

1.  **提升幅度不均**：作者在结论附近（p.14，提取缓存未覆盖，待核）自述部分场景/基线的提升是边际的、部分是显著的，并将这种不一致明确列为局限。
2.  **计算成本**：需计算法线关于网络参数子集 θ_D 的梯度（式 7、8）这类高阶导数，并在每步采样正负像素对，训练开销与显存增加（原文 p.14 给出训练时间/显存表，数值待核）。
3.  **对相关性定义的依赖**：效果依赖正样本选取质量。语义/几何阈值 β_S、β_G 与交集操作若过严会导致有效正样本不足，过松会引入错误关联；极端情况下（语义模糊、单目法线完全失真）可能失效。
4.  **先验依赖未完全消除**：仍需 DINO 与单目法线估计器作为输入。虽仅用于区域选择而非直接监督，但若这些特征在特定场景表现很差，仍会影响相关区域识别质量。
5.  **场景范围**：实验集中于**室内场景**。室外大场景、无纹理表面或动态物体的适用性未讨论。
## 个人评论

1.  **范式价值**：核心思想是从"利用一阶几何先验"转向"约束二阶几何相关性"。面对含噪监督，不直接信任信号值，而是约束信号之间的关系——这是处理不可靠先验的一种通用且优雅的思路。
2.  **工程实用性**：被设计为即插即用模块，且在 7 个差异较大的基线上都接入并见效，这种"插件"式工作更容易被社区采用。
3.  **多模态相关性定义有启发**：用 DINO（全局语义）∩ 单目法线（局部几何）来定义"相关"，图 3 的反例（墙柜 vs 天花板、座椅 vs 地板）把"为何需要交集"讲得很清楚，提示设计约束时可融合不同层次/模态信息来更准确地圈定约束对象。
4.  **对后续研究的启发**：互信息正则框架可拓展到其它几何属性（如曲率）、其它任务（点云）或其它模态（RGB-D）；它展示了在神经渲染框架内做更精细、更结构化几何约束的一条路径。不过"提升幅度不均"也提醒：二阶正则的收益与场景相关性结构强弱有关，何时显著、何时边际值得进一步分析。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[D2_3D_重建_神经辐射场_SLAM]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**计算机视觉与图形学**中的**多视图三维表面重建**方向（ECCV 2024，arXiv:2407.12661）。要解决的核心问题是：在**稀疏视图**输入下，对**大而复杂的室内场景**做高质量三维表面重建。先前基于 NeRF + SDF 的方法（NeuRIS、MonoSDF 等）依赖预训练单目几何估计模型（法线/深度），其噪声与泛化误差会损害重建质量。本文提出一种**二阶几何正则化**技术（互信息塑造），可作为插件接入各类 SDF-based NeRF。因此应归类到 **"3D 重建—神经辐射场 / SLAM"（D2_3D_重建_神经辐射场_SLAM）** 主题，而非注意力算子模块。

## 2. 一句话总结
InfoNorm 通过对**高相关场景点表面法线之间的互信息**做对比式正则（InfoNCE），用二阶相关性约束替代对含噪一阶几何先验的直接监督，从而提升稀疏视图下 SDF-based NeRF 的表面重建质量。

## 3. 背景与问题
- **为什么要做**：稀疏多视图三维重建是 VR 内容创建、机器人交互的基础，但室内场景规模大、遮挡多、观测稀疏。传统 MVS 需要大量图像重叠，在此场景失效。
- **之前方法的问题**：NeuS、VolSDF 等 SDF-based NeRF 在充足视图下表现好，稀疏视图下下降；NeuRIS、MonoSDF 引入单目法线/深度作一阶监督，但先验含噪、不可靠，性能高度依赖先验质量。
- **核心矛盾**：稀疏视图需几何先验补足观测，但先验不可靠。本文主张：除几何本身外，**场景区域之间几何的相关性**（表述为网络权重受扰动时的互信息）同样重要——约束这种二阶相关性，对一阶先验噪声更鲁棒。

## 4. 核心贡献
1.  **二阶几何相关性正则**：以法线之间的互信息形式正则化 SDF-based NeRF 表面重建，而非直接用一阶先验作监督。
2.  **高效互信息计算流水线**：用法线关于扰动权重 θ_D 的梯度余弦相似度（取绝对值）近似互信息（沿用 JacobiNeRF 推导），以 InfoNCE 实现。
3.  **多模态相关区域识别**：DINO 语义特征 ∩ 单目法线几何特征筛选正样本对，兼顾语义相似与法线一致。
4.  **即插即用插件**：在 NeuS、VolSDF、GeoNeuS、I2-SDF、NeuRIS、MonoSDF、Neuralangelo 上验证有效。

## 5. 方法详解
- **整体框架（图 2）**：NeRF 骨干 + SDF 头 f(x;θ) + 颜色头 c(x,v;θ)，部分共享参数 θ。密度/颜色由 eikonal 损失 L_E 与光度损失 L_C 监督；仅对 SDF 分支参数子集 θ_D 施加互信息损失 L_M，颜色分支不变。
- **输入输出**：输入带位姿稀疏多视图图像；输出 SDF，提取零等值面得网格。
- **预备知识（Sec. 3.1）**：体渲染（式 1）+ 光度损失（式 2）；SDF→密度的转换函数 Φ（式 3，如 Laplace CDF）+ eikonal 损失（式 4）；NeRF 互信息——对权重子集 θ_D 加球面均匀分布的小扰动 γn，泰勒展开后两扰动像素互信息 ∝ |cos β|（式 5），β 为两梯度夹角。
- **法线互信息（Sec. 3.2）**：法线 N(x;θ)=∂f/∂x（式 6）。约束法线而非 SDF 值的理由：① 法线计算涉及 f 全部参数，正则更全局；② 约束 ∂f/∂x 比约束 SDF 值更不易扭曲密度。法线对 θ_D 的梯度按 xyz 拼接为 ∂N（式 7–8），沿射线按 ω 聚合到像素 N(p_i)（式 9）；两像素法线互信息 ∝ |余弦相似度|（式 10）。
- **相关区域提取**：DINO（语义）+ 单目法线（几何）各用余弦相似度 + 阈值 β_S、β_G 选 top 相似像素，**取交集**为正样本对，其余随机像素为负样本。图 3 反例：单语义会关联墙柜与天花板，单（含噪）几何无法区分平行不相连平面，交集才正确。
- **损失（式 11、12）**：定制 InfoNCE 损失 L_M（分子=锚点与正样本法线梯度 |cos| 的 exp，分母对负样本求和）；总损失 L = L_C + λ_E·L_E + λ_M·L_M，端到端训练。
- **和已有方法的差异**：vs NeuRIS/MonoSDF（一阶监督 → 本文二阶相关性，先验仅用于选区域）；vs JacobiNeRF（颜色梯度互信息做语义传播 → 本文法线梯度互信息做表面重建，互信息推导引自 JacobiNeRF）；vs ManhattanSDF（曼哈顿假设、平面场景 → 本文一般场景）。

## 6. 实验与结果
- **数据集**：ScanNet++（8 场景）、Replica（4 场景，取自 Semantic-NeRF），每场景均匀采样 50–85 张图像。
- **基线**：NeuS、VolSDF、GeoNeuS、I2-SDF、NeuRIS、MonoSDF、Neuralangelo，对比各自原版（+ 版本为加入 InfoNorm）。
- **指标**：L2 Chamfer 距离、F-score。
- **实现细节（Sec. 4.2）**：I2-SDF 丢弃法线/深度损失；NeuRIS 多视图 patch 丢弃低置信度法线；MonoSDF 在 30k 迭代衰减法线/深度损失防退化；Neuralangelo hash 字典大小 20、编码维度 4。
- **主结果**：提取缓存仅到 p.12（Sec. 4.3 开头即截断），ScanNet++ Tab.1 / Fig.4 与 Replica Tab.2 的**具体数值未被提取覆盖**。据原文后续页线索（提取缓存未覆盖，待核）：各基线 + InfoNorm 后重建质量普遍提升，Replica 结论与 ScanNet++ 一致。
- **消融（Sec. 4.4）**：据原文 p.13–14 线索（待核），Tab.3 在三个场景做组件消融；p.14 含训练时间(h)/显存(GB)开销表。具体数值待核。
- **效率**：高阶导数 + 在线正负样本采样带来额外开销，原文 p.14 给出训练时间/显存表，数值待核。

## 7. 这篇论文真正有价值的地方
1.  **范式转换**：从"利用一阶几何先验"到"约束二阶几何相关性"，为处理含噪监督提供"约束关系而非信号值"的通用思路。
2.  **工程实用**：即插即用，跨 7 个差异较大基线一致见效。
3.  **多模态相关性定义**：DINO（全局语义）∩ 单目法线（局部几何），图 3 的反例把交集的必要性论证得清楚。
4.  **可迁移框架**：互信息正则可推广到曲率等其它几何属性、点云等其它任务、RGB-D 等其它模态。

## 8. 局限与问题
1.  **提升幅度不均**：作者自陈部分提升边际、部分显著，并将此不一致列为局限（p.14，提取缓存未覆盖，待核）。
2.  **计算成本**：法线对参数的高阶导数（式 7、8）+ 在线采样像素对，训练时间与显存增加（p.14 有表，数值待核）。
3.  **依赖相关性定义**：β_S、β_G 阈值与交集操作过严/过松都会影响正样本质量；极端先验失真下可能失效。
4.  **先验依赖未完全消除**：仍需 DINO 与单目法线估计器，特征质量差时影响区域选择。
5.  **场景范围**：仅室内；室外、无纹理、动态场景未讨论。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要、第 1 节引言（后半 + 贡献列表）、图 2/图 3、第 3.2 节损失设计、第 4.1 数据集与第 4.2 实现细节。
- **复现**：精读第 3 节全部公式（式 6–12），关注 4.2 节各基线的超参调整（MonoSDF 30k 衰减、Neuralangelo hash 字典 20 / 维度 4 等），并参考官方代码 https://github.com/Muliphein/InfoNorm 与补充材料中正负样本选取与互信息推导细节。
- **借鉴创新点**：学习其二阶正则思想与"语义 ∩ 几何"定义相关性的策略，思考"约束关系而非约束值"如何迁移到自己的问题。
- **写 Related Work**：可放入 1) 基于 NeRF/SDF 的三维重建；2) 几何先验在 NeRF 中的应用；3) 基于对比学习/互信息的网络正则化。

## 10. 和其他论文的关系
- **核心基线与对比**：
    - `[[NeuS]]` / `[[VolSDF]]`：SDF-based NeRF 的两个奠基基线，本文主要插件对象。
    - `[[GeoNeuS]]`, `[[I2-SDF]]`, `[[NeuRIS]]`, `[[MonoSDF]]`, `[[Neuralangelo]]`：本文进一步做增强实验的先进基线。
    - `[[JacobiNeRF]]`：互信息推导的直接来源（颜色梯度互信息做语义传播），本文将其迁移到几何法线。
- **技术组件来源**：
    - `[[DINO]]`：语义特征提取器。
    - `[[InfoNCE]]`：互信息对比损失形式。
- **同主题对照方法**：
    - `[[ManhattanSDF]]`：基于曼哈顿世界假设的另一类先验方法，面向平面场景。

## 11. 关键词
3D 表面重建, 稀疏视图, 神经辐射场 (NeRF), 符号距离函数 (SDF), 互信息, 二阶相关性, 法线正则化, InfoNCE, 几何先验, DINO 语义特征, 单目法线, 室内场景, 即插即用插件。

## 12. 可信度说明
本精读笔记的方法部分（Sec. 1–3 与 Sec. 4.1/4.2）**严格基于提取缓存中可读的 p.1–12 文本**，涵盖摘要、引言、相关工作、完整方法（含式 1–12）与数据集 / 实现细节，可信度高。
**信息缺失**：提取缓存在 Sec. 4.3（"We can observe t…"）处截断，**Tab.1（ScanNet++）、Tab.2（Replica）、Tab.3（消融）、Fig.4 的具体数值，以及训练时间 / 显存（p.14）、附录数据集统计（Tab.5）等均未被提取覆盖**。笔记中这些数值已统一标注"（据原文后续页，提取缓存未覆盖，待核）"，未编造任何数字。分类已从误标的"B_注意力算子模块"修正为"D2_3D_重建_神经辐射场_SLAM"。

---

> **可信度补充**: PDF 提取质量 = **high** (提取覆盖 p.1–12, 2086 字符/页, 含完整方法与全部公式); 缺失数值集中于 p.13–24 的结果/消融/效率表与附录, 已逐项标注"待核"; 来源缓存: `.paper-cache/extracts/InfoNorm.txt` (提取 12/24 页; 原 AI 主体 p.1–12 + 全文补读线索 p.13–24); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-24; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-24。
- **提取情况**: 缺失页 12 页, 其中 12 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: InfoNorm 13
- p.13: Last but not least, the experiments on Neuralangelo demonstrate the poten-
- p.13: Results on the Replica dataset. In Tab. 2 we report the numerical results on
- p.13: 4.4 Analyses
- p.13: Table 3: Ablation studies on three scenes from
- p.13: The results are reported
- p.14: Training Time (h) VRAM (GB)
- p.14: method provides benefits for 3D re-
- p.14: 5 Conclusion
- p.14: We explore the usage of the second-order geometric correlations as a regulariza-
- p.14: In return, we can observe a boost in the geometric quality of the reconstructed
- p.14: Extensiveevaluationsonvariousbaselinesanddatasetsshowtheeffectiveness

### 缺失页关键摘录

- p.13: Results on the Replica dataset. In Tab. 2 we report the numerical results on
- p.13: the Replica dataset, with respect to NeuS [30], VolSDF [37], GeoNeuS [8], I2-
- p.13: incorporated into these baselines, aligning with the conclusion drawn from the
- p.13: Table 3: Ablation studies on three scenes from
- p.14: e.g., some are marginal, and some are significant, which we deem as a limitation
- p.17: 7 More Information on Datasets and Evaluation Metrics
- p.17: Datasets. We report the statistics of the scenes in our evaluation in Tab. 5.
- p.17: Evaluation metrics. We use the L2 Chamfer distance and F-score to evaluate the
- p.18: Table 5: Statistics of the scenes in our evaluation on ScanNet++ and Replica.
- p.18: To ensure a fair evaluation, we remove all parts of the geometry that are not
- p.18: visible from the training views, as shown in Figure 6.
- p.18: The numbers reported in Table 4 in the main paper were measured on an
<!-- AI_READING_NOTE_END -->
