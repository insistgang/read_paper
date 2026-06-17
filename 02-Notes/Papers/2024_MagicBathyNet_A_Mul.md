---
title: "MagicBathyNet: A Multimodal Remote Sensing Dataset for Bathymetry Prediction and Pixel-Based Classification in Shallow Waters"
authors:
  - "Panagiotis Agrafiotis"
  - "Łukasz Janowski"
  - "Dimitrios Skarlatos"
  - "Begüm Demir"
year: 2024
venue: "arXiv (2405.15477, cs.CV)"
doi: 
pdf: [[2024_MagicBathyNet_A_Mul.pdf]]
primary_topic: L_数据集_Benchmark
topics:
  - "L_数据集_Benchmark"
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
extract_cache: .paper-cache/extracts/2024_MagicBathyNet_A_Mul.txt
---

# MagicBathyNet: A Multimodal Remote Sensing Dataset for Bathymetry Prediction and Pixel-Based Classification in Shallow Waters

## 基本信息
- **PDF**: [[2024_MagicBathyNet_A_Mul.pdf]]
- **primary_topic**: `L_数据集_Benchmark`
- **topics**: `L_数据集_Benchmark`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | MagicBathyNet: A Multimodal Remote Sensing Dataset for Bathymetry Prediction and Pixel-Based Classification in Shallow Waters |
| **作者** | Panagiotis Agrafiotis; Łukasz Janowski; Dimitrios Skarlatos; Begüm Demir |
| **机构** | BIFOLD / TU Berlin (德国); Gdynia Maritime University (波兰); Cyprus University of Technology (塞浦路斯) |
| **发表时间** | 2024 |
| **刊物/会议** | arXiv:2405.15477v2 (cs.CV, 2024-06-04); 具体收录会议提取文本未明确 |
| **项目主页** | www.magicbathy.eu/magicbathynet.html (数据集、预训练权重、代码公开) |
| **DOI** | 未明确 |

## 摘要

> **英文原摘要（据 PDF 提取文本修复空格与断字）**:
> Accurate, detailed, and regularly updated bathymetry, coupled with complex semantic content, is crucial for the under-mapped shallow water areas facing intense climatological and anthropogenic pressures. Current methods exploiting remote sensing imagery to derive bathymetry or pixel-based seabed classes mainly exploit non-open data. This lack of openly accessible benchmark archives prevents the wider use of deep learning methods in such applications. To address this issue, in this paper we present the MagicBathyNet, which is a benchmark dataset made up of image patches of Sentinel-2, SPOT-6 and aerial imagery, bathymetry in raster format and annotations of seabed classes. MagicBathyNet is then exploited to benchmark state-of-the-art methods in learning-based bathymetry and pixel-based classification. Dataset, pre-trained weights, and code are publicly available at www.magicbathy.eu/magicbathynet.html.
>
> **中文翻译**: 精确、细致、定期更新的水深数据，加上复杂的语义内容，对那些正承受强烈气候与人类活动压力、却尚未被充分测绘的浅水区域至关重要。当前利用遥感影像推导水深或像素级海底类别的方法大多依赖非公开数据，这种公开基准数据的缺失阻碍了深度学习方法在该领域的更广泛应用。为解决此问题，本文提出 MagicBathyNet——一个由 Sentinel-2、SPOT-6 与航拍影像图像块、栅格格式水深以及海底类别标注构成的基准数据集，并基于它对学习型水深反演与像素级分类的前沿方法进行了基准测试。数据集、预训练权重与代码公开于 www.magicbathy.eu/magicbathynet.html。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：地球约 71% 表面被水覆盖，但仅有极小部分被直接观测测绘。受栖息地破坏、污染、自然灾害、航行等需求驱动，海底测绘的重要性近年显著上升。浅水沿海区域承受强烈气候与人类活动压力，急需精确、细致、高频的水深和海底语义信息。声学方法在浅水区低效，易受波浪、礁石影响并因多径误差失败；LiDAR 昂贵，二者都缺乏视觉信息。因此航空与卫星影像被广泛使用——光谱推导水深（SDB，基于辐亮度随深度和波长的衰减）可在大范围浅水上提供深度，深度学习方法相比物理/简单回归模型（随机森林、SVM）能更好处理光与水面、水柱、水底的复杂交互。
- **之前方法的问题**：现有的 SDB 与像素分类方法大多基于非公开数据集；海底像素分类工作又主要集中在珊瑚礁或海草床制图，多用全卷积网络（FCN）。公开基准档案的缺失阻碍了深度学习方法的更广泛应用，也使已开发方法之间难以可靠比较。
- **核心矛盾**：浅水测绘任务的重要性日益增长、深度学习展现潜力，但**缺乏一个公开、高质量、多模态的基准数据集来公平评估并推动算法发展**。本文正是为填补这一空白。

## 关键贡献

1.  **提出首个公开的多模态浅水测绘基准数据集 MagicBathyNet**：包含 Sentinel-2(S2)、SPOT-6、航拍影像三种模态的配准图像块，并附带栅格水深与海底类别标注（作者称据其所知是该任务的首个公开多模态数据集）。
2.  **地理分布良好的两个差异巨大的区域**：地中海的塞浦路斯阿依纳帕（Agia Napa，代表典型地中海水体与海底）与波罗的海的波兰帕克泻湖（Puck Lagoon，代表波罗的海水体与海底）。
3.  **大规模配准数据**：3355 组 S2/SPOT-6/航拍三模态配准三元组、1244 组 S2–SPOT-6 配对、3354 个航拍 DSM 块、3396 个 S2/SPOT-6 DSM 块；533 个图像块带海底类别标注（共 1451 个标注样本）。每个图像块覆盖 180×180 m。
4.  **基准测试现有方法**：用改进的 U-Net 做水深反演，用 U-Net 与 SegFormer(B5) 做像素分类，给出跨模态、跨区域的性能对比，建立基线。
5.  **数据集、预训练权重、代码全部公开**，并显式保留大量未标注块以支持自监督预训练。

## 方法

**论文核心是构建数据集，并非提出新模型架构。其"方法"主要指数据集构建流程与基准测试设置。**

- **整体框架**：数据收集 → 预处理与校正 → 配准与裁剪 → 标注。
- **输入/输出（基准任务）**：
    - **输入**：三模态 RGB 图像块，物理覆盖 180×180 m；分辨率为 S2 = 18×18 像素、SPOT-6 = 30×30 像素、航拍 = 720×720 像素。
    - **输出**：连续水深预测图（回归）或像素级海底类别图（5 类分类）。
- **关键模块与构建流程**：
    1.  **影像数据收集**（2.1 节）：阿依纳帕 S2 摄于 2016-01-10、SPOT-6 摄于 2016-01-29、航拍为 2015-02-16 至 03-16；帕克泻湖 S2 摄于 2021-04-20、SPOT-6 摄于 2021-04-19、航拍为 2022-02-27 至 03-02。S2 Level2A 来自 Copernicus Hub，ORTHO SPOT-6 经 ESA TPM 计划从 Airbus Hub 下载，卫星影像均做辐射、几何、大气校正。航拍：阿依纳帕用固定翼无人机 + Canon IXUS 220HS（焦距 4.3 mm，像元 1.55 µm，4000×3000），383 张、平均航高 209 m、GSD 6.3 cm，40 个陆上控制点，XYZ 方向 RMSE 分别 5.03/4.74/7.36 cm；帕克泻湖用 Phase One iXM-100（焦距 35 mm，像元 3.7 µm，11664×8750），4384 张、平均航高 676 m、GSD 6.8 cm，22 个控制点，XYZ RMSE 1.15/0.71/0.69 cm。
    2.  **折射校正**：用 SfM-MVS 生成 DSM，并对 DSM 与航拍正射影像施加文献 [1,2,12]（Agrafiotis 等 2019/2020/2021）提出的前沿折射校正方法，将空气中获取的几何校正到水下真实位置——这是获得准确水深的关键。
    3.  **配准与裁剪**：正射影像按各模态裁成非重叠 180×180 m 块；用 SPOT-6 近红外波段生成水体掩膜，仅保留含水图像块并剔除边界块。
    4.  **水深与标注收集**（2.2 节）：阿依纳帕海底最深 −30.29 m，用 Leica HawkEye III 测深 LiDAR；帕克泻湖最深 −10.57 m，用 Riegl VQ-880-GII LiDAR 与 Teledyne Reson T50/T20 多波束测深仪。标注采用"保守但精确"策略：仅标注在 S2/SPOT-6/航拍三模态中类别一致的像素，得到稀疏但高置信、各模态一致的标注；每个区域每个模态约人工标注 700 个像素样本，覆盖 5 类：i) 海草（Posidonia oceanica）；ii) 大型藻类（丝状/草皮藻）；iii) 鳗草/眼子菜（Zostera marina, Stuckenia pectinata, Potamogeton perfoliatus）；iv) 沙；v) 岩石。水深和标注都转栅格（像元等于各模态分辨率）再裁成 180×180 m 块，并经人工目视检查。大量未标注块一并发布以支持无监督预训练。
- **训练方式（基准测试）**：
    - **水深预测**：改进 U-Net——除首尾卷积外含 4 个下采样层（ReLU 激活、max pooling）和 4 个上采样层（转置卷积），保留跳连，解码末端 1×1 卷积输出水深图。损失为屏蔽无深度区的 RMSE loss，优化器 Adam，初始学习率 SPOT-6/S2 为 1e-4、航拍为 1e-5，训练 10 epoch；S2 与航拍在第 9 epoch 后学习率降为 1/10。
    - **像素分类**：U-Net 与 SegFormer(B5-sized，分层 Transformer 编码器 + 全 MLP 解码头)。指标用总准确率与 F1；优化器 SGD，阿依纳帕 U-Net 学习率 1e-5、SegFormer 1e-4，帕克泻湖 U-Net 对 SPOT-6/S2 用 1e-5、航拍 1e-6，SegFormer 对 SPOT-6/S2 用 1e-4、航拍 1e-5；统一训练 100 epoch，损失为交叉熵。
    - **公共设置**：S2 与 SPOT-6 数据（两任务）统一 resize 到 256×256 裁剪，在不引入新信息的前提下显著提升性能；PyTorch 实现，单张 NVIDIA RTX A5000 24 GB GPU；随机 80%/20% 划分，分类与水深各自定制以保证可复现。
- **和已有方法的差异**：差异不在模型创新，而在**数据集创新**——首次提供公开、多模态、带高质量水深与类别真值的浅水基准，使深度学习方法的系统性评估成为可能。

## 实验

- **使用的数据集**：MagicBathyNet 本身。3355 三模态配准三元组、1244 S2–SPOT-6 配对、3354+3396 个 DSM 块；533 个标注块（阿依纳帕 35 块、帕克泻湖 498 块），共 1451 个标注样本（阿依纳帕 697、帕克泻湖 754）。按类别（Table 1）：海草 118（仅阿依纳帕）、大型藻类 82（仅阿依纳帕）、鳗草等 428（仅帕克泻湖）、沙 572（246+326）、岩石 251（仅阿依纳帕）。
- **对比方法**：
    - **水深预测**：仅评估改进 U-Net 在三模态、两区域的表现，未与其他模型对比。
    - **像素分类**：U-Net vs SegFormer(B5)。
- **评价指标**：水深用 RMSE/MAE/标准差(Std.)；分类用各类 F1 与总准确率。
- **主实验结果**：
    - **水深预测**（Table 2，单位米）：**航拍最佳**。阿依纳帕 aerial RMSE 0.616 / MAE 0.420 / Std. 0.598，SPOT-6 RMSE 0.718，S2 RMSE 1.068；帕克泻湖 aerial RMSE 0.298（MAE 0.187 / Std. 0.297），SPOT-6 RMSE 0.817，S2 RMSE 0.907。阿依纳帕航拍 RMSE 明显高于帕克泻湖，原因是该区航拍深度标签稀疏；阿依纳帕整体更难（海底覆盖多变、深度突变大、水更深）。
    - **像素分类**（Tables 3/4/5，F1 与总准确率，%）：
        - **阿依纳帕（Table 3、5）**：海草 U-Net/SegFormer 航拍均 97.37；大型藻类 U-Net 航拍 94.73、SPOT-6 仅 13.33、S2 25.00（SegFormer 航拍 87.50、SPOT-6 46.15、S2 50.00）；沙、岩石普遍较高。总准确率（Table 5）：航拍 U-Net=SegFormer=94.67，SPOT-6 U-Net 76.00 / SegFormer 77.33，S2 U-Net 78.76 / SegFormer 75.51。
        - **帕克泻湖（Table 4、5）**：鳗草等与沙 F1 均较高（如鳗草 SegFormer 航拍 97.47、U-Net 95.36）。总准确率航拍 SegFormer 97.33 vs U-Net 95.33，SPOT-6 85.33/86.66，S2 78.52/82.55——SegFormer 明显占优。
        - **总体趋势**：航拍 > SPOT-6 > S2。SegFormer 在 F1 上整体优于 U-Net，例外是阿依纳帕 SPOT-6/S2 的海草与沙、以及航拍的大型藻类；作者归因于 SegFormer 在样本极少时表现下降，而 U-Net 更适合小数据。卫星影像上大型藻类差，是因该类海底覆盖面积常小于卫星 GSD。目视检查显示 SegFormer 能更好捕捉长程依赖与全局上下文，在未标注区域预测更准（如 U-Net 把仅有岩石处误判为大型藻类/沙、把沙误判为鳗草）。
- **消融/泛化实验**：未做传统消融。"泛化"体现为在两个差异巨大的地理区域上测试。
- **速度/参数量**：提取文本未给出参数量、FLOPs 或训练/推理耗时；仅说明用单张 NVIDIA RTX A5000 24 GB GPU、PyTorch 实现。

## 局限

- **地理与类型覆盖有限**：仅两个区域（地中海、波罗的海）；作者在结论中也将"扩展到更多地理区域、覆盖更多水体与海底类型"列为未来工作。
- **类别不平衡与稀疏**：标注本就"稀疏但精确"，且类别极不均衡——海草/大型藻类/岩石仅出现在阿依纳帕，鳗草仅出现在帕克泻湖；大型藻类在卫星影像上样本与覆盖都极小，F1 低至 13.33%。这限制了模型在复杂场景的能力。
- **基准模型有限**：仅 U-Net 与 SegFormer 两种相对标准的模型，未探索多模态融合、对比/自监督等更前沿策略（作者把多模态学习与自监督预训练列为未来方向）。
- **固定随机划分**：随机 80/20 划分，未考虑时相、空间自相关，可能影响对泛化能力的评估。（此为笔者评述，原文仅强调划分以保证可复现。）
- **计算成本未量化**：未给出训练时间/成本与模型规模等细节。

## 个人评论

1.  **填补关键资源缺口**：最大价值是提供一个急需、设计良好的公开基准。高质量公开数据集往往能催生一系列新方法，MagicBathyNet 为浅水测绘提供了标准"竞技场"，且作者明确把未标注块定位为自监督预训练资源，扩展了它作为基础数据集的用途。
2.  **多模态构建方法论的启示**：从多源异构数据（不同分辨率、不同平台、不同时相）到对齐配准样本的完整流程，尤其是基于作者自家前序工作的**折射校正**，对构建类似水下/水体数据集很有参考价值。
3.  **评估框架的参考**：覆盖水深回归 + 像素分类两个相关任务、CNN vs Transformer 两类代表模型、两个差异巨大的区域，这种评估框架全面且有说服力，可作为后续工作评估新方法的模板。
4.  **CNN vs Transformer 的小数据洞察**：论文给出一个实用结论——样本极少时 U-Net 反而可能优于 SegFormer，提醒该领域研究者在数据稀缺场景谨慎选择大模型。
5.  **紧扣现实需求**：将遥感、深度学习与海洋测绘、海草/海底生境监测等实际需求结合，应用价值突出。

### 使用建议

- **如果快速了解**：读摘要、引言首尾段与结论，即可掌握数据集的核心价值、构成与主要结论。
- **如果复现**：精读第 2 节（DESCRIPTION OF MAGICBATHYNET）的数据构成（数量、尺寸、来源、传感器）与第 3 节（EXPERIMENTAL RESULTS）的训练超参（各模态学习率、epoch、损失、优化器、256×256 resize），并下载其公开代码与数据。
- **如果借鉴创新点**：学习其数据集构建方法论——多源遥感整合、精确配准与折射校正、高置信跨模态一致标注策略。
- **如果写 related work**：可放入"多模态遥感数据集""浅水测绘基准""海底分类数据集""SDB 方法评估"等讨论中。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[L_数据集_Benchmark]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**遥感 + 水深测量（Bathymetry）+ 海底分类 + 深度学习数据集**的交叉方向。它解决的核心问题是：**浅水区域的水深反演和海底像素分类任务缺乏公开、标准化的多模态基准数据集**，这阻碍了深度学习方法的应用与算法间的公平比较。论文主体是数据集构建与基准测试，因此最适合放在"L_数据集_Benchmark"主题下。

## 2. 一句话总结
本文提出首个公开多模态（Sentinel-2 / SPOT-6 / 航拍）浅水遥感基准数据集 MagicBathyNet，包含栅格水深真值与 5 类海底标注，并用改进 U-Net 做水深回归、U-Net 与 SegFormer 做像素分类建立基线，覆盖地中海阿依纳帕与波罗的海帕克泻湖两个差异巨大的区域。

## 3. 背景与问题
- **为什么要做**：地球约 71% 表面是水但仅极小部分被直接测绘；浅水沿海区承受气候与人类活动压力，急需高精度高频水深与海底语义。声学方法在浅水低效（受波浪、礁石、多径误差影响），LiDAR 昂贵，二者均缺视觉信息。遥感影像的 SDB（基于辐亮度随深度/波长衰减）与像素分类是有效补充，深度学习相比物理/简单回归模型能更好处理光-水交互。
- **之前方法的问题**：SDB 与海底像素分类大多基于非公开数据，且分类工作多局限于珊瑚礁/海草床、多用 FCN；公开基准的缺失阻碍方法推广与可靠对比。
- **核心矛盾**：任务重要性上升、深度学习有潜力，但缺一个公开、高质量、多模态、带真值的基准来公平评估。

## 4. 核心贡献
1.  首个公开多模态浅水测绘基准 MagicBathyNet（S2/SPOT-6/航拍 + 栅格水深 + 海底类别标注）。
2.  地理分布良好的两个差异巨大区域：阿依纳帕（地中海）与帕克泻湖（波罗的海）。
3.  规模：3355 三模态三元组、1244 S2–SPOT-6 配对、3354+3396 DSM 块、533 标注块（1451 样本），每块 180×180 m。
4.  用改进 U-Net 做水深、U-Net 与 SegFormer 做分类的跨模态/跨区域基准。
5.  数据、预训练权重、代码全部公开，并保留大量未标注块以支持自监督预训练。

## 5. 方法详解
**核心是构建数据集，非新模型。** 流程：数据收集 → 预处理校正 → 配准裁剪 → 标注。
- **输入/输出**：输入三模态 RGB 块（物理 180×180 m；S2 18×18、SPOT-6 30×30、航拍 720×720 像素）；输出连续水深图或 5 类像素分类图。
- **关键步骤**：① 收集两区三类影像与水深测量；② 卫星影像辐射/几何/大气校正，航拍用 SfM-MVS 生成 DSM 并施加文献 [1,2,12] 的折射校正，把空气中几何还原到水下真实位置；③ 按各模态裁非重叠 180×180 m 块，用 SPOT-6 近红外做水体掩膜剔除陆地与边界块；④ 水深来自 LiDAR（Leica HawkEye III / Riegl VQ-880-GII）与多波束（Teledyne Reson T50/T20），阿依纳帕最深 −30.29 m、帕克泻湖最深 −10.57 m；标注仅取三模态类别一致的像素（稀疏但高置信、各模态一致），每区每模态约 700 像素，5 类：海草/大型藻类/鳗草等/沙/岩石。
- **训练**：水深用改进 U-Net（4 下 4 上采样、ReLU、max pooling、转置卷积、跳连、1×1 输出），损失为屏蔽无深度区的 RMSE loss，Adam，10 epoch；分类用 U-Net 与 SegFormer(B5)，SGD，交叉熵，100 epoch；各模态学习率不同（详见正文上方"方法"节）；S2/SPOT-6 统一 resize 256×256；单张 RTX A5000，随机 80/20 划分。
- **差异**：贡献在数据集而非模型。

## 6. 实验与结果
- **数据集**：MagicBathyNet 本身（标注块阿依纳帕 35、帕克泻湖 498，共 533；样本 697+754=1451）。
- **对比**：水深仅评估改进 U-Net；分类 U-Net vs SegFormer。
- **指标**：水深 RMSE/MAE/Std.；分类 F1 + 总准确率。
- **结果**：
    - 水深（Table 2，米）：航拍最佳——阿依纳帕 aerial RMSE 0.616、SPOT-6 0.718、S2 1.068；帕克泻湖 aerial 0.298、SPOT-6 0.817、S2 0.907。阿依纳帕航拍 RMSE 偏高因深度标签稀疏；阿依纳帕整体更难。
    - 分类（Tables 3/4/5）：海草、鳗草、沙 F1 普遍高（海草航拍 97.37）；大型藻类在卫星影像上差（U-Net SPOT-6 仅 13.33%），因其海底覆盖常小于卫星 GSD。总准确率：阿依纳帕航拍 94.67（两模型相同），帕克泻湖航拍 SegFormer 97.33 > U-Net 95.33。整体航拍 > SPOT-6 > S2，SegFormer 多数情况优于 U-Net，但样本极少时 U-Net 反而更稳。目视检查显示 SegFormer 在未标注区预测更准（捕捉长程依赖/全局上下文）。
- **消融/泛化**：无传统消融；泛化体现为两个差异巨大区域。
- **速度/参数量**：提取文本未给出参数量/FLOPs/耗时，仅说明单张 RTX A5000 24 GB。

## 7. 这篇论文真正有价值的地方
1.  **填补关键资源缺口**：提供急需、设计良好的公开基准，并显式把大量未标注块定位为自监督预训练资源。
2.  **多模态构建方法论**：多源异构数据到对齐配准样本的完整流程，尤其折射校正，对类似数据集建设参考价值高。
3.  **评估框架**：水深回归 + 像素分类两任务、CNN vs Transformer 两模型、两区域，框架全面有说服力。
4.  **小数据下 CNN vs Transformer 的实用洞察**：样本极少时 U-Net 可能优于 SegFormer，提醒数据稀缺场景慎用大模型。

## 8. 局限与问题
- **覆盖有限**：仅两区域，作者也将扩展更多地理区域列为未来工作。
- **类别不平衡且稀疏**：多数类别只在单一区域出现，大型藻类在卫星影像上 F1 低至 13.33%。
- **基准模型有限**：仅 U-Net/SegFormer，未探索多模态融合、自监督等（均列为未来方向）。
- **固定随机 80/20 划分**：未控时相/空间自相关（笔者评述）。
- **计算成本未量化**。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言首尾段 + 结论。
- **复现**：精读第 2 节（数据构成、传感器、来源、尺寸）与第 3 节（各模态学习率、epoch、损失、优化器、256×256 resize），下载公开代码与数据。
- **借鉴创新点**：学其数据集构建方法论——多源整合、配准与折射校正、高置信跨模态一致标注。
- **写 related work**：放入多模态遥感数据集 / 浅水测绘基准 / 海底分类数据集 / SDB 方法评估的讨论。

## 10. 和其他论文的关系
该数据集旨在被用于评估水深反演与海底分类算法。基准用到的基础工具包括 U-Net [[U-Net]]（Ronneberger 等 2015）、SegFormer [[SegFormer]]（Xie 等 2021）、Adam [[Adam]]（Kingma & Ba 2014）。数据集构建关键技术来自作者自家折射校正系列 [[Agrafiotis等2019]] [[Agrafiotis等2020]]（及 [12] Agrafiotis 等 2021 合成数据增强折射校正），以及帕克泻湖遥感/水深数据集 [13][14]（Janowski 等 2023/2024）。它与各类 SDB/海底制图工作（如 BathyNet、CNN/LSTM 水深反演 [4–9]、珊瑚礁/海草制图 [10,11]）形成评估关系。

## 11. 关键词
多模态数据集, 水深预测, 像素级分类, 深度学习, 遥感, 浅水测绘, 基准, Sentinel-2, SPOT-6, 航拍影像, 海底制图, 折射校正, SDB

## 12. 可信度说明
本精读笔记基于完整的 PDF 提取文本（5/5 页，含摘要到参考文献的全部章节）生成。所有具体数字（3355 三元组、1244 配对、3354/3396 DSM、533 标注块、1451 样本、各类样本数、Table 2 的 RMSE/MAE/Std.、Tables 3–5 的 F1 与总准确率、各模态学习率与 epoch、传感器型号、深度 −30.29/−10.57 m、采集日期）均逐项核对自提取文本。提取质量良好、内容连贯。提取文本未提供的信息（模型参数量、FLOPs、训练耗时、具体收录会议）已明确标注"未明确"。venue 据 arXiv 标识（2405.15477v2, cs.CV, 2024-06-04）填写，具体会议未知。

---

> **可信度补充**: PDF 提取质量 = **high** (5/5 页完整, 含全部章节, 内容连贯); 来源缓存: `.paper-cache/extracts/2024_MagicBathyNet_A_Mul.txt`; 生成日期: 2026-06-04; 复核优化日期: 2026-06-18; 模式: LLM (mimo-v2.5-pro) + 据提取文本逐项核对。
<!-- AI_READING_NOTE_END -->
