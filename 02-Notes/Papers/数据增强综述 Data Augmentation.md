---
title: "Data Augmentation in Classification and Segmentation: A Survey and New Strategies"
authors:
  - "Khaled Alomar"
  - "Halil Ibrahim Aysel"
  - "Xiaohao Cai"
year: 2023
venue: "Journal of Imaging (J. Imaging)"
doi: 10.3390/jimaging9020046
pdf: [[数据增强综述 Data Augmentation.pdf]]
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
extract_cache: .paper-cache/extracts/数据增强综述 Data Augmentation.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/26 pages"
---
# Data Augmentation in Classification and Segmentation: A Survey and New Strategies

## 基本信息
- **PDF**: [[数据增强综述 Data Augmentation.pdf]]
- **primary_topic**: `R_综述_Survey`
- **topics**: `R_综述_Survey`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Data Augmentation in Classification and Segmentation: A Survey and New Strategies |
| **作者** | Khaled Alomar, Halil Ibrahim Aysel, Xiaohao Cai（University of Southampton, School of Electronics and Computer Science, UK） |
| **发表时间** | 2023（Received 16 Dec 2022, Accepted 10 Feb 2023, Published 17 Feb 2023） |
| **刊物/会议** | Journal of Imaging (J. Imaging), 2023, 9, 46（MDPI 开放获取） |
| **DOI** | 10.3390/jimaging9020046 |

> 说明: 原笔记 frontmatter 把刊物写成 "Electronics", 与 PDF 不符。据提取文本第 1 页引用块, 正确刊物为 *Journal of Imaging*（J. Imaging 2023, 9, 46），已更正。

## 摘要

**英文原摘要（据 PDF 提取文本整理，修复空格与连字符）：**

> In the past decade, deep neural networks, particularly convolutional neural networks, have revolutionised computer vision. However, all deep learning models may require a large amount of data so as to achieve satisfying results. Unfortunately, the availability of sufficient amounts of data for real-world problems is not always possible, and it is well recognised that a paucity of data easily results in overfitting. This issue may be addressed through several approaches, one of which is data augmentation. In this paper, we survey the existing data augmentation techniques in computer vision tasks, including segmentation and classification, and suggest new strategies. In particular, we introduce a way of implementing data augmentation by using local information in images. We propose a parameter-free and easy to implement strategy, the random local rotation strategy, which involves randomly selecting the location and size of circular regions in the image and rotating them with random angles. It can be used as an alternative to the traditional rotation strategy, which generally suffers from irregular image boundaries. It can also complement other techniques in data augmentation. Extensive experimental results and comparisons demonstrated that the new strategy consistently outperformed its traditional counterparts in, for example, image classification.

**中文翻译：**

> 在过去十年中，深度神经网络（尤其是卷积神经网络）彻底改变了计算机视觉。然而，所有深度学习模型为取得令人满意的结果，往往都需要大量数据。遗憾的是，现实问题中并非总能获得足量数据，而数据匮乏极易导致过拟合，这已是公认事实。缓解这一问题可走多条路径，其中之一便是数据增强。本文综述了计算机视觉任务（含分割与分类）中现有的数据增强技术，并提出了新策略。具体而言，我们引入了一种利用图像中"局部信息"实现数据增强的方式：提出一种无参数、易实现的随机局部旋转（random local rotation, RLR）策略——随机选取图像中圆形区域的位置与大小，并以随机角度对其旋转。该策略可作为传统旋转的替代方案（传统旋转通常因不规则图像边界而受损），也可与其他增强技术互补。大量实验与对比表明，新策略在诸如图像分类等任务上一致优于其传统对应方法。
>
> **关键词**: data augmentation; deep learning; convolutional neural networks; image processing; segmentation; classification

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**: 以 CNN 为代表的深度网络在动作识别、目标检测与定位、人脸识别、图像表征等视觉任务上全面超越传统方法（提取文本引言段落 [1–7]）。但其短板——大规模数据需求、训练时间长、过拟合、数据稀缺时性能骤降——会阻碍泛化与有效性 [8,9]。
- **过拟合的成因与已有缓解手段**: 追求更高精度通常靠堆叠更复杂的架构（VGG-16、ResNet、Inception-V3、DenseNet 等），而模型复杂度（可训练参数、层数、每层神经元/滤波器数）与所需数据复杂度成正比；数据不足时，复杂模型易"记忆"训练样本而非泛化（Figure 1 给出过拟合损失曲线示意）。文中明确的缓解策略分两条线（Figure 2）：① 模型架构层面的正则化——dropout、岭回归（ℓ2）、Lasso（ℓ1），以及 batch normalisation、迁移学习等副产物；② **数据层面**——获取更多数据，而数据增强正是在数据层面"人工创造多样且类别均衡的样本"的方法。
- **数据增强的两类划分**: 文中指出可按 ① 目的（扩大训练集规模 / 提升多样性）或 ② 所针对的问题来划分。后者例子：随机擦除针对遮挡问题 [8]；旋转与翻转部分解决视角问题 [27–29]；亮度调整应对光照变化 [30]；裁剪与缩放应对尺度与背景问题。最流行的划分（Figure 3 taxonomy）是把数据增强分为**深度学习式**与**传统式**，后者再细分为几何（geometric）、光度（photometric）、噪声（noise）三类。
- **核心矛盾 / 切入点**: 一方面是"数据需求 vs 数据匮乏"的根本矛盾；另一方面，作者特别指出最常用的几何增强之一——**传统旋转**——本身有缺陷：把方形图像沿圆形轨迹旋转会在边界产生黑色斑块（black patches），既不反映原始数据又可能损害增强效果（Figure 4、Figure 5）。常见补救是用 wrap、constant、reflection、nearest 等方式填充黑块，但都是后处理。作者据此提出"利用图像局部信息、在局部随机做旋转"的 RLR。

## 关键贡献

1. **系统综述**: 聚焦图像分类与分割中使用数据增强的近期文献，梳理传统（几何/光度/核滤波/噪声/随机擦除）与深度学习式两大类技术。作者强调"据我们所知，分类与分割领域的数据增强综述尚少"。
2. **提出新几何增强方法 RLR**: 无参数、易实现的随机局部旋转——随机选取图像内部圆形区域的位置、面积与角度并旋转之，可补充现有增强策略。
3. **解决传统旋转的边界黑块问题**: 旋转在局部进行，避免在图像边界形成黑色区域，从而不丢失边界像素信息。
4. **提升数据多样性**: 不仅扩量，还能通过随机化区域/大小/角度改善多样性。
5. **实验验证**: 大量实验与对比表明 RLR 在图像分类等任务上一致优于传统旋转（提取文本未给出具体准确率数字；据原文后续页, 提取缓存未覆盖, 待核）。

## 方法

核心创新是**随机局部旋转（RLR）**，属几何数据增强。

- **整体定位**: 作为训练前/数据加载时的预处理增强，与模型结构解耦，模型无关（model-agnostic）。
- **输入 / 输出**: 输入一张原始图像（论文示例取自 CIFAR-10）；输出在某个内部圆形区域被随机旋转后的增强图像。
- **关键步骤**（据提取文本引言对 RLR 的定义："RLR rotates an image's internal circular region by selecting random location, area and angle"）:
    1. **随机定位与定面积**: 在图像内部随机选取圆形区域的位置（中心）与面积（半径）。
    2. **随机角度旋转**: 对该圆形区域施加一个随机角度旋转。
    3. **区域外保持不变**: 圆外像素不动。
- **与传统旋转的对照（Figure 4、Figure 5）**: 传统旋转（TR，即 "constant" 填充）在边界产生黑块；其变体 RNR（random nearest neighbor rotation，重复最近像素填充）、RRR（random reflect rotation，镜像填充）、RWR（random wrap rotation，周期边界填充）是对黑块的不同后处理。RLR 的不同之处在于**根本不产生黑块**——因为旋转发生在图像内部圆形区域，边界保持完整。
- **直观理解**: 可视为一个局部仿射/旋转变换。设原图 \(I\)、圆形区域掩码 \(M\)、旋转矩阵 \(R_\theta\)，增强图 \(I'\) 在 \(M\) 内由 \(R_\theta(I)\) 填充、在 \(M\) 外保持 \(I\)。核心是"变换局部而非全局"。（公式为笔记对文字描述的形式化整理，提取文本未给出该式。）
- **推理阶段**: 与一般增强相同，测试时不施加增强（提取文本未对此明述，属常规约定）。

> 注: 提取缓存仅覆盖到 p.12（第 5 节"Proposed Strategy"恰在 p.15 开始，据补读线索）。RLR 完整算法、掩码生成细节、区域大小/角度的取值范围等，位于提取缓存未覆盖的 p.15 之后，待核。

## 实验

- **本文方法的实验设置**: RLR 的完整实验（数据集、模型、超参、对比与数值结果）位于第 6 节，在提取缓存未覆盖的 p.15 之后。提取文本（p.1–12）仅给出结论性陈述："Extensive experimental results and comparisons demonstrated that the new strategy consistently outperformed its traditional counterparts in, for example, image classification."（据原文后续页, 提取缓存未覆盖, 具体准确率数字待核）。
- **综述部分常用的评测数据集**: 文中列出 MNIST、CIFAR-10、CIFAR-100、ImageNet 为四个常用数据集 [10,33–35]；并指出 ImageNet 等属"大数据"（>1400 万张），通常不需再增强，许多实验会**截取大数据集的小子集**来模拟数据稀缺。
- **综述中引用的代表性实验结论（可据提取文本核实的具体数字）**:
    - **Mash et al. [39]**: 用 10 类细粒度数据集做飞机分类，测试裁剪、旋转、缩放、多边形遮挡及其组合；**裁剪 + 遮挡组合**取得最大提升，相对基线提升 **9%**；该研究未考察光度增强。
    - **据补读线索（p.13–14，提取缓存未覆盖正文，仅有片段摘录，待核）**: 某分割工作（"…net" [93]）达 **99.5% mean accuracy / 97.3% mean IoU**；某工作报告**分割精度可提升 5–20%**；BraTS 数据集上训练标准 **3D U-Net [98]**；Ma et al. [90] 构建小规模开源绵羊分割数据集 **SSG**（数百张图）。这些数字来自补读片段，原始上下文不完整，需核。
- **对比方法**: RLR 主要与传统旋转 TR 及其填充变体 RNR / RRR / RWR 对比（据提取文本对 Figure 5 的描述）。
- **消融 / 泛化 / 效率**: 提取缓存未覆盖第 6 节，未见 RLR 的消融、跨任务泛化与效率（参数量/FLOPs/速度）数据；因 RLR 不改模型结构，预期不增加模型参数，但文中是否量化分析待核。

## 局限

> 以下局限部分基于提取文本（p.1–12）对方法的描述与综述自身边界，部分为对方法性质的合理推断（已标注）。

1. **方向敏感任务可能受损（合理推断）**: RLR 引入局部随机旋转，对方向/位置极敏感的任务（如字符/数字识别、车牌、关键点定位）可能产生不合理变换。文中虽未直接评估 RLR 在此类任务的效果，但在讨论翻转与随机擦除时确实提到"label safety"——对不对称/方向敏感数据（字母、数字）翻转会导致错误甚至相反标签，随机擦除不宜用于车牌/字母等敏感分类，RLR 同源问题值得警惕。
2. **本笔记可核实的实验证据有限**: 因提取缓存只覆盖前 12 页，RLR 的具体数据集、模型、超参、对比明细与数值结果（第 6 节）无法据提取文本核实，结论的可复现性在本笔记层面打折（这是提取覆盖问题，非论文本身缺陷）。
3. **综述任务覆盖**: 综述聚焦分类与分割，对更复杂场景（细粒度、实例分割、医学影像中的增强权衡）的系统比较，需读 p.13–26 才能判断深度。
4. **设计参数的"随机性"边界（合理推断）**: 虽号称"无参数"，但圆形区域的大小/位置分布、角度范围仍需合理设定，否则可能过度扭曲语义；其设计原则的讨论位于提取缓存未覆盖的第 5 节，待核。

## 个人评论

> 本节为 AI 阅读时的评论，非论文原文。

1. **问题意识值得学**: 论文没有把"旋转"当成完美工具，而是直指其边界黑块缺陷——这种"对常用手段保持怀疑"的视角，对设计/选用增强很有启发。
2. **"局部化全局操作"是可迁移的设计哲学**: RLR 的本质是把"全局旋转"降维为"局部随机旋转"以规避边界副作用。同样思路可延伸到局部缩放、局部平移、局部弹性形变，是一个有生产力的元方法。
3. **即插即用、模型无关**: 无参数、不改网络结构，适合资源有限或追求快速增益的场景，落地成本低。
4. **作为综述的入门价值**: Figure 3 的 taxonomy（深度学习式 vs 传统式 → 几何/光度/噪声）给了清晰的入门地图，且每类都配了直观示例图（翻转 Fig.6、裁剪 Fig.7、颜色抖动 Fig.8、核/滤波 Fig.9、噪声 Fig.10、随机擦除 Fig.11、纹理迁移 Fig.12）。
5. **需要注意的取舍**: 文中诚实地点出各增强的"反例"——裁剪可能裁掉主体导致错标（Fig.7 的狗）、光度变换内存/算力开销大且可能丢失辨别性颜色特征、随机擦除可能整体抹掉待分类对象。读这类综述时，这些"何时不该用"往往比"怎么用"更有价值。

### 使用建议

- **快速了解**: 读摘要、引言、Figure 3（taxonomy）、第 7 节结论，即可掌握全貌与主要创新点。
- **复现 RLR**: 重点读第 5 节（方法，p.15 起）+ 第 6 节（实验），并对照 Figure 4、Figure 5 理解传统旋转问题与四种填充变体（TR/RNR/RRR/RWR）。提取缓存未覆盖这两节，需查原 PDF。
- **借鉴创新点**: 学其"用局部随机操作规避全局操作缺陷"的设计哲学，可迁移到其他几何/弹性变换。
- **写 related work**: 可作为"分类与分割中数据增强"的系统性综述引用；RLR 作为"几何增强 / 旋转增强变体"的一个具体案例讨论。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R_综述_Survey]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
计算机视觉中**数据增强**方向的"综述 + 新方法"论文（J. Imaging 2023, 9, 46, MDPI 开放获取）。它系统梳理用于**图像分类与分割**的数据增强技术，并提出一种新的几何增强策略 RLR。适合作为"数据增强方法综述"或"提升 CNN 泛化能力的训练策略"主题下的入门级参考与方法引用。归类 `R_综述_Survey` 准确。

## 2. 一句话总结
本文综述了图像分类与分割中的数据增强技术（传统几何/光度/噪声 + 深度学习式），并提出无参数、易实现的随机局部旋转（RLR）——在图像内部圆形区域做随机定位、定面积、定角度的旋转，以规避传统旋转在边界产生黑块、丢失像素信息的问题。

## 3. 背景与问题
- **为什么做**: CNN 在视觉任务上超越传统方法，但依赖大规模高质量数据；数据不足 → 过拟合（Figure 1 损失曲线：训练/验证损失先同降，过拟合点后验证损失回升）。
- **已有缓解手段两条线（Figure 2）**: ① 模型层面正则化（dropout、ℓ2 岭回归、ℓ1 Lasso、BN、迁移学习）；② 数据层面——获取/人工创造更多样本，即数据增强。
- **数据增强的划分**: 按目的（扩量/增多样性）或按所针对问题划分；最流行的是"深度学习式 vs 传统式（→几何/光度/噪声）"，见 Figure 3 taxonomy。常用评测集 MNIST/CIFAR-10/CIFAR-100/ImageNet，常用大数据集的小子集模拟数据稀缺。
- **切入的具体缺陷**: 传统旋转把方形图沿圆形轨迹旋转 → 边界黑块（black patches）+ 像素信息丢失（Figure 4、5），常见补救是 wrap/constant/reflection/nearest 填充（后处理）。RLR 从根上规避。

## 4. 核心贡献
1. 系统综述分类与分割中数据增强（传统 + 深度学习式两大类）。
2. 提出无参数、易实现的几何增强 RLR。
3. RLR 在局部旋转、避免边界黑块与信息丢失。
4. 同时扩量与增多样性。
5. 大量实验显示 RLR 在图像分类等任务一致优于传统旋转（具体数字在第 6 节，提取缓存未覆盖，待核）。

## 5. 方法详解
- **定位**: 训练前/加载时的预处理增强，与模型解耦，模型无关，属几何增强。
- **三步**（据引言对 RLR 的定义）: ① 随机选圆形区域的位置与面积；② 对该区域施随机角度旋转；③ 区域外像素保持不变。
- **与四种旋转的对照**: TR（constant 填充，产生黑块）/ RNR（最近邻填充）/ RRR（镜像反射填充）/ RWR（周期 wrap 填充）都是对黑块的后处理；RLR 因旋转发生在内部圆区、边界完整，**根本不产生黑块**。
- **形式化（笔记整理，非原文公式）**: \(I'=R_\theta(I)\) 于掩码 \(M\) 内、\(I\) 于 \(M\) 外。
- **细节缺口**: 圆区大小/角度的取值范围、掩码与重采样实现等在第 5 节（p.15 起），提取缓存未覆盖，待核。

## 6. 实验与结果
- **RLR 自身实验**: 第 6 节，提取缓存（p.1–12）未覆盖。提取文本仅有结论句"consistently outperformed its traditional counterparts ... in image classification"；具体准确率数字待核（据原文后续页, 提取缓存未覆盖）。
- **综述中可核实的代表数字**:
    - Mash et al. [39] 飞机分类（10 类细粒度）: 裁剪+遮挡组合相对基线提升 **9%**（最佳）。
    - 据 p.13–14 补读片段（上下文不完整，待核）: 某分割工作达 **99.5% mean accuracy / 97.3% mean IoU**；分割精度可提升 **5–20%**；BraTS 上训练 **3D U-Net**；Ma et al. [90] 建小规模开源绵羊分割集 **SSG**（数百张）。
- **对比方法**: 主要对比传统旋转 TR 及其填充变体 RNR/RRR/RWR。
- **消融/泛化/效率**: 提取缓存未覆盖第 6 节，无法核实；RLR 不改模型结构，预期不增加参数。

## 7. 这篇论文真正有价值的地方
1. **诚实的"反例清单"**: 几乎每种增强都点出"何时会出错"——裁剪裁掉主体导致错标（Fig.7）、翻转破坏方向敏感标签（label safety）、随机擦除抹掉待分类对象、光度变换丢失辨别性颜色特征。这种取舍清单比"怎么用"更有参考价值。
2. **清晰 taxonomy（Figure 3）**: 给数据增强一张干净的分类地图，配齐示例图，入门友好。
3. **可迁移的设计哲学**: "把全局操作降为局部随机操作以规避副作用"——RLR 是该思路在旋转上的实例，可推广。
4. **低落地成本**: 无参数、模型无关、即插即用。

## 8. 局限与问题
1. 方向/位置敏感任务（字符、车牌、关键点）可能受 RLR 损害——文中以 label safety 讨论翻转/随机擦除的同类风险（合理推断）。
2. 本笔记可核实证据受限于提取覆盖（仅前 12 页），第 6 节数值结果待核。
3. RLR 设计参数（圆区大小/位置/角度分布）虽称"无参数"，仍需合理设定，原则讨论在第 5 节，待核。
4. 综述对复杂任务（细粒度、实例分割、医学影像增强权衡）的深度需读 p.13–26 判断。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言 + Figure 3 + 第 7 节结论。
- **复现**: 第 5 节（方法）+ 第 6 节（实验），对照 Figure 4/5；提取缓存未覆盖，需查原 PDF。
- **借鉴**: 学"局部随机化全局操作"的设计哲学。
- **写 related work**: 作为分类/分割数据增强综述引用；RLR 作几何/旋转增强变体案例。

## 10. 和其他论文的关系
- 与数据增强领域其他综述并列/承继（如 [[Data Augmentation Strategies]]）。
- 引用并讨论了多项具体增强技术，作为综述基础：
    - 随机擦除：[[Random Erasing Data Augmentation]]（[8]，针对遮挡）。
    - 颜色抖动：[[数据增强中的颜色抖动策略]]（[42] 随机 / [43] 预设调整）。
    - 几何增强：[[传统几何变换在数据增强中的应用]]（翻转/裁剪/旋转 [27–30,37–39]）。
- RLR 可与所有旋转增强方法（TR/RNR/RRR/RWR）直接对比。
- 综述还涉及纹理迁移（texture transfer [55,56]，深度学习式增强的起点，Figure 12）等。

## 11. 关键词
data augmentation；deep learning；convolutional neural networks；image processing；segmentation；classification。（中文补充：过拟合、几何/光度/噪声增强、随机局部旋转 RLR、随机擦除、纹理迁移、泛化能力）

## 12. 可信度说明
本笔记主要基于 PDF 提取文本（p.1–12，提取缓存截断于 25000 字符）。该范围包含**完整摘要、引言、第 2 节全部传统增强（几何/光度/核滤波/噪声/随机擦除）以及第 3.1 节纹理迁移开头**，可据此可靠重建论文定位、背景、taxonomy、传统增强细节与 RLR 的引言级描述。
- **可直接核实**: 标题/作者/刊物（J. Imaging，已更正原 frontmatter 的 "Electronics" 错误）、摘要与关键词、Figure 1–11 的语义、Mash et al. [39] 的 9% 提升、四种旋转 TR/RNR/RRR/RWR 的定义。
- **信息缺口（提取缓存未覆盖 p.13–26）**: 第 3 节深度学习式增强其余部分、第 4 节近期研究综述全表、第 5 节 RLR 完整算法与参数、第 6 节实验设置/结果表/消融、第 7 节结论。笔记中标"待核"的数字（99.5%/97.3% mean IoU、5–20%、SSG、BraTS+3D U-Net 等）来自补读片段，上下文不完整。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 提取缓存覆盖 = 12/26 页 (截断于 25000 字符)，p.13–26 仅有补读片段摘录; 来源缓存: `.paper-cache/extracts/数据增强综述 Data Augmentation.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-26; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-26。
- **提取情况**: 缺失页 14 页, 其中 14 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Resurs datasetsRandom chromatic
- p.13: ResNet34 as
- p.13: CRAG datasetObject-level augmentation
- p.13: method.MobileNet based
- p.13: Experimental results on their acquired cattle dataset showed that this data augmentation
- p.14: To overcome the small data size challenge, data augmentation techniques, such as rotation,
- p.14: In light of this, an automatic learning-based data augmentation technique was developed
- p.14: experiments on both normal and medical image datasets demonstrated that the ObjectAug
- p.14: results illustrated the superior performance of the proposed segmentation methods for the
- p.15: 5. Proposed Strategy for Data Augmentation
- p.15: In this section, we propose a new data augmentation technique, belonging to the
- p.15: Mask 1

### 缺失页关键摘录

- p.13: Papers Dataset Aug. Techniques Model Task Findings
- p.13: and segmentation accuracy can be increased
- p.13: accuracy and mean intersection over union
- p.13: strate the beneﬁts of applying data augmentation. Ma et al. [ 90] created the SSG dataset,
- p.13: i.e., a small-scale and open-source sheep segmentation dataset containing hundreds of
- p.13: images. To ﬁnd the best technique for this small semantic segmentation dataset, they
- p.13: Experimental results on their acquired cattle dataset showed that this data augmentation
- p.14: net” [ 93], achieved 99.5 percent mean accuracy and 97.3 percent mean intersection of unions.
- p.14: transformations to increase the size and diversity of the training dataset. Their ﬁndings
- p.14: transformations, and that the segmentation accuracy could be improved by 5 to 20 percent
- p.14: learning process when training a standard 3D U-Net [ 98] on the BraTS dataset [ 85,103,104].
- p.14: terms of accuracy and mean intersection over union.
<!-- AI_READING_NOTE_END -->
