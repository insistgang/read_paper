---
title: "R. Duan et al. SODA: Site Object Detection dAtaset for Deep Learning in Construction 2022"
authors:
  - "Rui Duan"
  - "Hui Deng"
  - "Mao Tian"
  - "Yichuan Deng"
  - "Jiarui Lin"
year: 2022
venue: 未明确
doi: 
pdf: [[2022_SODA_Site_Object_De.pdf]]
primary_topic: L_数据集_Benchmark
topics:
  - "L_数据集_Benchmark"
  - "C_目标检测_通用与旋转框"
status: ai-read
reading_stage: ai-complete
confidence: medium
source_basis: pdf-text
date_added: 2026-06-03
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-10
extract_cache: .paper-cache/extracts/2022_SODA_Site_Object_De.txt
full_text_covered: true
full_text_completed_at: 2026-06-10
full_text_completion_basis: full-document chunked LLM synthesis
extraction_complete: true
extracted_pages: 23
total_pages: 23
content_coverage: full
extraction_engine: pymupdf
metadata_verified: false
---

# R. Duan et al. SODA: Site Object Detection dAtaset for Deep Learning in Construction 2022

> PDF: [[2022_SODA_Site_Object_De.pdf]] | 本页为 AI 全文精读，尚未人工复核。

## 基本信息
- **PDF**: [[2022_SODA_Site_Object_De.pdf]]
- **primary_topic**: `L_数据集_Benchmark`
- **topics**: `L_数据集_Benchmark`, `C_目标检测_通用与旋转框`
- **状态**: ai-read (AI 全文精读, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SODA: Site Object Detection dAtaset for Deep Learning in Construction |
| **作者** | Rui Duan; Hui Deng; Mao Tian; Yichuan Deng (通讯); Jiarui Lin |
| **单位** | 华南理工大学土木与交通学院、南加州大学、清华大学土木系等 |
| **发表时间** | 2022 |
| **刊物/会议** | 未明确（提取文本未给出期刊名；数据下载链接托管于华南理工 OSS） |
| **DOI** | 未明确 |

## 摘要

**英文原摘要（据 PDF 提取文本整理，修复断词与空格）**：

> Computer vision-based deep learning object detection algorithms have been developed sufficiently powerful to support the ability to recognize various objects. Although there are currently general datasets for object detection, there is still a lack of large-scale, open-source dataset for the construction industry, which limits the developments of object detection algorithms as they tend to be data-hungry. Therefore, this paper develops a new large-scale image dataset specifically collected and annotated for the construction site, called Site Object Detection dAtaset (SODA), which contains 15 kinds of object classes categorized by workers, materials, machines, and layout. Firstly, more than 20,000 images were collected from multiple construction sites in different site conditions, weather conditions, and construction phases, which covered different angles and perspectives. After careful screening and processing, 19,846 images including 286,201 objects were then obtained and annotated with labels in accordance with predefined categories. Statistical analysis shows that the developed dataset is advantageous in terms of diversity and volume. Further evaluation with two widely-adopted object detection algorithms based on deep learning (YOLO v3 / YOLO v4) also illustrates the feasibility of the dataset for typical construction scenarios, achieving a maximum mAP of 81.47%. In this manner, this research contributes a large-scale image dataset for the development of deep learning-based object detection methods in the construction industry and sets up a performance benchmark for further evaluation of corresponding algorithms in this area.
>
> **Keywords**: Dataset; Object Detection; Construction site; Deep Learning; Computer Vision

**中文翻译**：

> 基于计算机视觉的深度学习目标检测算法已发展得足够强大，能够支持对各类物体的识别。尽管当前已有通用目标检测数据集，但建筑行业仍缺乏大规模、开源的数据集，而深度学习算法对数据高度依赖，这一空缺限制了相关检测算法的发展。为此，本文构建了一个专门为建筑工地采集与标注的大规模图像数据集——Site Object Detection dAtaset（SODA），它包含按工人、材料、机械、布局四大类组织的 15 类目标。首先，在不同工地条件、天气条件与施工阶段下，从多个工地采集了 2 万余张涵盖不同角度和视角的图像；经过仔细筛查与处理后，得到并按预定义类别标注了 19,846 张图像、共 286,201 个目标。统计分析表明该数据集在多样性与规模上具有优势。进一步用两种广泛采用的深度学习检测算法（YOLO v3 / YOLO v4）评估，验证了数据集对典型建筑场景的可行性，最高达到 81.47% 的 mAP。由此，本研究为建筑行业基于深度学习的目标检测方法提供了一个大规模图像数据集，并为该领域相应算法的评测建立了性能基准。
>
> **关键词**：数据集；目标检测；建筑工地；深度学习；计算机视觉

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 建筑业仍是劳动密集型行业，现场管理多依赖人工判断，效率低且困难；计算机视觉与深度学习检测算法已成熟（在合适场景下识别准确率可达 98% 甚至更高），但深度学习"嗜数据"，将其落地到工地必须有建筑领域专用的图像数据集。(p.1, p.2)
- **之前方法的问题**:
    1.  通用图像数据集（MNIST 7 万张、PASCAL VOC 1.1 万张 20 类、COCO 16 万张 91 类、ImageNet 1400 万+张 2 万+类）缺乏建筑工地特有的类别。(p.2, p.4)
    2.  现有建筑行业数据集（Tajeen 等的施工机械集、Kolar 等的护栏集 6000 张、Li 等的安全帽集 3261 张、MOCS 40000+张 13 类、CHV 1330 张、ACID 10000 张 10 类）规模较小、类别较少，且集中在工人、个人防护装备（PPE）和部分机械上，**缺乏对建筑材料与场地布局的覆盖**。(p.4, p.5)
    3.  工地图像采集本身困难：因安全原因工地通常不对外开放、在线资源稀少且重复率高；固定式单目相机难以获取多视角图像，易致模型过拟合；工地环境杂乱、标注需专业知识、成本高。(p.2)
- **核心矛盾**: 工地智能化、自动化监控的迫切需求与可用的大规模、多要素（尤其覆盖材料/布局）开源数据集极度匮乏之间的矛盾。

## 关键贡献

1.  **构建并开源首个大规模建筑工地目标检测数据集 SODA**：含 19,846 张图像、286,201 个标注对象、15 个具体类别，VOC 格式，面向建筑业公开免费下载。(p.1, p.3, p.20)
2.  **首次实现四要素全覆盖**：SODA 是首个同时检测**工人、材料、机械、布局**四大要素的开源数据集；并首次引入塔吊吊钩可视化（hook visualization）设备采集的图像，这是以往研究忽视的部分。(p.3, p.14, p.20)
3.  **提供数据集构建方法论与经验**：详细记录类别选择、多源采集（无人机/手持单目相机/工地监控-吊钩可视化）、四目标数据清洗、标准化标注的完整流程与"避坑"经验（含隐私处理、标注标准、标注错误类型统计）。(p.6–p.12)
4.  **建立性能基准**：在 YOLO v3 与 YOLO v4 两个单阶段检测器上给出基准结果（最高 mAP 81.47%），为后续算法在该数据集上的评测提供参照。(p.15–p.19)

## 方法

- **论文类型与整体框架**: 本文核心是**数据集构建（dataset paper）**，而非提出新检测模型。构建流程（Fig. 2）分四步：①类别选择 → ②图像数据采集 → ③图像数据清洗 → ④图像标注。(p.6)
- **输入输出**:
    - **输入**: 来自广州多个工地、覆盖从基坑阶段到装修阶段、不同角度与时间段的原始图像（手持单目相机、无人机、工地监控/吊钩可视化）。(p.6, p.8)
    - **输出**: VOC 标准的 XML 标注文件，含存储路径、图像名、边界框坐标与类别标签。(p.11, p.12)
- **关键模块**:
    1.  **类别选择**（§3.1）：四大类细分为 15 类——工人类：person、helmet、vest；材料类：board、wood、rebar、brick、scaffold；机械类：handcart、cutter、ebox（电箱）、hopper、hook；布局类：fence、slogan。(p.6, Table 1/2)
    2.  **数据采集**（§3.2）：放弃网络爬虫（图像不符要求），全部实地采集；三种方式——无人机、手持单目相机、工地监控视频（吊钩可视化）；统一转 JPG。共采集 **21,863** 张。经验教训：机械/布局目标数量少需多角度补拍；单一拍摄方式难取正样本需多设备融合；最高点相机可拍全景与塔吊等大机械，但画面太模糊难标注小目标。(p.8, p.9)
    3.  **数据清洗**（§3.3）：四个目标——去重、去模糊、去无目标、隐私保护。隐私处理（公司 LOGO 与人脸模糊化）耗时巨大，**每人约 200 工时、占清洗 2/3**；清洗中删除 **2017** 张无效图像；一轮隐私处理与作者/专家联合检查后，学生仍有 **1307 处遗漏（人均 37 处）**。清洗整体约 **300 工时**（正文 p.10 称占总时间 25%，但 p.12 的细分表给出占比 16.4%，两处口径不一致）。(p.10, p.12)
    4.  **数据标注**（§3.4）：35 名土木专业学生（人均约 600 张）用 **LabelImg** 标注，生成 XML。四条标注标准：①框必须框住且不与目标相交、②尽量减少无关背景、③相邻相似目标用"单目标多框"而非"一框多目标"、④部分遮挡或不便标注的目标省略（Fig. 6 蓝框 vs 红框）。先培训并制作教程，作者定期检查进度，学生标注由研究生+作者联合复检。复检发现的错误集中在：标签拼写错误（如 scaffold→seaffold、hopper→hooper、helmet→helemt、board→borad/boadrd 等，Table 3 列出）、复数错误、未知标签（含 48 个 'w'、2 个 'wwww'，因快捷键为 w 误触），均在正式发布版中修正。(p.11, p.12)
- **训练方式**: SODA 按 9:1 随机划分为训练集 **17,861** 张 / 测试集 **1,985** 张；用 PyTorch 实现，硬件为 NVIDIA RTX 2060 + i7-10750H。训练 100 个 epoch，分两阶段：前 50 epoch **冻结**主干、提高学习率以跳出局部最优；后 50 epoch **解冻**主干、降低学习率精调。(p.15, p.16)
- **总工时统计**: 清洗+标注+检查共约 1832 工时——清洗约 300 工时（16.4%）、标注 1246 工时（68%）、检查 286 工时（15.6%），断续耗时近一个月。(p.12)
- **推理流程**: 训练好的模型在实际复杂工地图像上做了可行性验证（Fig.15–17），未详述端到端部署流程。(p.17)
- **与已有方法的差异**: 相比已有小型建筑数据集，SODA 在**对象总数（286,201，居各对比集之首）**、**类别多样性（首覆盖四要素）**、**视角多样性（多设备、多角度，含吊钩可视化）**上均显著提升。(p.14, Table 4)

## 实验

- **使用的数据集**: SODA（训练 17,861 张 / 测试 1,985 张，9:1）。(p.16)
- **统计层面对比**: 与建筑业现有开源集做**规模/覆盖的定性对比**（Table 4，非同模型同指标的检测性能横向对比）——SODA 19846 图/286201 对象/15 类（1920×1080 等）；MOCS 41668 图/222861 对象/13 类；ACID 10000 图/15767 对象/10 类；CHV 1330 图/9209 对象。SODA 对象数与类别覆盖最优，并首用吊钩可视化数据。(p.14)
- **评价指标**: IoU=0.5 下的 **mAP**（由各类 AP 平均，AP 为 P-R 曲线下面积）；速度用 **FPS**；另给出 log-average miss rate（Fig.16）。(p.15)
- **主实验结果**:
    - **整体 mAP**: YOLO v3 = **71.22%**，YOLO v4 = **81.47%**。(p.16, p.19, Table 5)
    - **速度**: YOLO v4 = **31.94 FPS** > YOLO v3 = **25.06 FPS**。(p.17)
    - **类间规律**: 两模型上**材料类 mAP 普遍较高、工人类较低**。(p.17)
    - **最佳/最差类别 AP**: 正文（p.17）称最高 AP 为 hook（YOLO v3 中 92.81%）与 hopper（YOLO v4 中 95.18%），最低为 fence（YOLO v3 中 50.99%）与 helmet（YOLO v4 中 55.62%）。**注意自相矛盾**：Table 5 数值显示 v3 的 hook=91.76、v4 的 hook=92.81，即 92.81% 实际属于 v4 而非正文所述的 v3，正文与表格存在归属错误（fence 50.99%/helmet 55.62% 两值正文与表格一致）。(p.17, p.19)
- **定性验证**: 简单场景下 v3、v4 识别相近；复杂场景下 v4 能识别更多类别、准确率更高。(p.17)
- **消融实验**: 提取文本中未明确说明针对四要素子集或模型配置的消融实验。
- **泛化实验**: 未做跨数据集/跨场景的定量泛化测试（仅在真实工地图像上做定性可行性展示）。
- **效率信息**: 报告 FPS；未提供参数量（Parameters）与计算量（FLOPs）。

## 局限

1.  **数据集规模与类别仍有限**：尽管类别数与图像数大于同行业其它数据集，但相比深度学习社区的通用大集仍偏小，类别也无法覆盖工地全部要素，后续需扩充。(p.20)
2.  **标注粒度受限**：仅做目标级（边界框）标注，非像素级，因此只能训练检测算法，无法支撑实例/语义分割等更精细任务；像素级标注是未来重要工作。(p.20)
3.  **算法探索深度不足**：研究重心在数据集构建，仅训练了 YOLO v3/v4 两个经典单阶段模型，未引入更先进检测器（如两阶段或 Transformer 类）挖掘潜力。(p.20)
4.  **标注与采集仍依赖人工、成本高**：标注者为工程管理专业学生，未来可探索众包标注与自动标注；实地采集耗时费力（清洗约 300 工时、隐私处理每人约 200 工时），且工地监控视频常被定时删除或难以获取，计划借助行业主管部门权限扩充。(p.10, p.12, p.20)

## 个人评论

1.  **填补"材料+布局"空白的即用型基准**：以往工地数据集几乎都聚焦工人/PPE/机械，SODA 首次把建筑材料（板材、木方、钢筋、砖、脚手架）与场地布局（围栏、标语）纳入统一标注体系，类别定义贴合工程实际，直接降低了相关研究门槛。
2.  **难得的工程化"避坑指南"**：论文罕见地公开了构建过程的真实代价与坑点——隐私处理占清洗 2/3、删除 2017 张无效图、人均 37 处遗漏、48 个误触的 'w' 标签等，这种过程透明度对后续行业数据集建设的参考价值甚至高于数据本身。
3.  **结果暴露场景特异难点**：fence、helmet 等小目标/复杂背景类别 AP 偏低（50–56%），而 hopper、scaffold 等规则大目标 AP 高（90%+），直观指明了密集小目标与杂乱背景是工地检测的主攻方向。
4.  **可信度提醒**：正文与 Table 5 对"最高 AP 归属哪个模型"的表述自相矛盾（hook 92.81% 应属 v4 而非正文所写的 v3）；且清洗时间占比一处写 25%、一处写 16.4%。引用其具体数字时应以表格/细分表为准并交叉核对。

### 使用建议

- **如果快速了解**：读摘要(p.1)、引言问题阐述(p.1–3)、结论与未来工作(p.20)、以及 Table 4 的数据集对比。
- **如果复现/用数据**：精读 §3 方法论(p.6–12)，尤其数据清洗四目标与四条标注标准；下载链接见 p.20（华南理工 OSS，VOCv1.zip）。
- **如果借鉴创新点**：学习其多源采集（含吊钩可视化）、严格质量控制与隐私处理流程，以及把工程领域知识转化为 15 类检测体系的做法。
- **如果写 related work**：可归入"**特定行业（建筑/施工）目标检测数据集**"或"**工业视觉检测 benchmark**"，用于说明该领域数据集现状与缺口。

## 相关论文与链接

- 主题归类：[[L_数据集_Benchmark]]、[[C_目标检测_通用与旋转框]]
- **同领域数据集（论文中对比/引用）**：MOCS（An 等，工地移动目标 13 类）、ACID（Xiao 等，10 类施工机械）、CHV（Wang 等，PPE 多类）、Kolar 等护栏集、Li 等安全帽集。
- **基准算法**：YOLO v3 / v4（单阶段）；论文亦综述了 R-CNN、Fast/Faster R-CNN（两阶段）作为背景。
- **可能的后续方向**：与更先进检测器（DETR、后续 YOLO 系列）结合探索性能上限；引入数据增强/域自适应解决跨工地泛化；扩展为像素级标注以支持分割；作为评测小目标/密集/复杂背景检测算法的标准基线。

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是计算机视觉**目标检测领域的数据集/基准（dataset & benchmark）论文**，应用场景为**建筑工地**。核心问题不是提出新模型，而是构建一个大规模、多要素、高质量的开源工地图像数据集 SODA，以缓解"深度学习嗜数据、而建筑业缺开源数据"的矛盾。最贴切的归类是 `L_数据集_Benchmark`（数据集/基准），应用域为目标检测（`C_目标检测_通用与旋转框`）。

## 2. 一句话总结
本研究构建并开源了首个同时覆盖工人/材料/机械/布局四大要素的大规模建筑工地目标检测数据集 SODA（19,846 张图像、286,201 个目标、15 类，VOC 格式），并在 YOLO v3/v4 上给出基准（最高 mAP 81.47%）。

## 3. 背景与问题
- **为什么要做**: 建筑业现场管理依赖人工、效率低；CV+深度学习检测已成熟（合适场景识别率可达 98%+），但算法嗜数据，落地工地必须有建筑领域专用数据集。(p.1, p.2)
- **之前方法的问题**:
    1.  通用集（MNIST/VOC/COCO/ImageNet）缺工地类别。(p.2, p.4)
    2.  现有建筑集（MOCS、ACID、CHV、护栏集、安全帽集等）规模小、类别少，集中于工人/PPE/部分机械，**缺材料与布局**。(p.4, p.5)
    3.  工地图像采集难（安全不开放、在线资源少且重复、单目相机视角单一易过拟合、环境杂乱标注需专业知识成本高）。(p.2)
- **核心矛盾**: 工地智能化监控的迫切需求 vs. 多要素大规模开源数据集的极度匮乏。

## 4. 核心贡献
1.  构建并开源首个大规模工地检测集 SODA：19,846 图 / 286,201 对象 / 15 类 / VOC 格式。(p.1, p.3, p.20)
2.  首次四要素（工人/材料/机械/布局）全覆盖，并首用吊钩可视化设备采集图像。(p.3, p.14, p.20)
3.  公开完整构建方法论与经验（采集/清洗/标注流程、隐私处理、标注错误统计）。(p.6–12)
4.  在 YOLO v3/v4 上建立性能基准（最高 mAP 81.47%）。(p.15–19)

## 5. 方法详解
- **整体框架**: 数据集构建四步（Fig. 2）：类别选择 → 数据采集 → 数据清洗 → 图像标注。(p.6)
- **输入输出**: 输入为广州多工地、多阶段、多角度的实地图像（无人机/手持/监控-吊钩）；输出为 VOC 的 XML（路径、图名、坐标、类别）。(p.6, p.8, p.11)
- **类别（15 类/4 大类）**: 工人 person/helmet/vest；材料 board/wood/rebar/brick/scaffold；机械 handcart/cutter/ebox/hopper/hook；布局 fence/slogan。(Table 1/2)
- **采集**: 放弃爬虫、全实地；三方式（无人机/手持单目/监控-吊钩可视化）；共采 21,863 张。经验：稀有目标多角度补拍、多设备融合取正样本、最高点相机拍全景但小目标模糊。(p.8, p.9)
- **清洗**: 去重/去模糊/去无目标/隐私保护四目标；隐私处理每人约 200 工时占清洗 2/3；删 2017 张无效图；联合检查后仍 1307 处遗漏（人均 37）。清洗约 300 工时（正文称 25%，细分表称 16.4%，口径不一）。(p.10, p.12)
- **标注**: 35 名土木学生（人均约 600 张）用 LabelImg 出 XML；四条标注标准（框住不相交/减背景/单目标多框/省略遮挡）；先培训后联合复检；错误集中于拼写/复数/未知标签（含 48 个'w'、2 个'wwww'），均在发布版修正。(p.11, p.12)
- **训练**: 9:1 划分（17,861/1,985）；PyTorch，RTX 2060+i7-10750H；100 epoch，前 50 冻结主干提高 lr、后 50 解冻主干降 lr。(p.15, p.16)
- **总工时**: ≈1832 工时（清洗 300/16.4%、标注 1246/68%、检查 286/15.6%），断续近一月。(p.12)
- **差异**: 对象总数、类别多样性、视角多样性（含吊钩可视化）均优于同行业小集。(p.14)

## 6. 实验与结果
- **数据**: SODA 训练 17,861 / 测试 1,985。(p.16)
- **对比**: 与 MOCS/ACID/CHV 在规模与覆盖上定性对比（Table 4），非同模型同指标横向比较。MOCS 41668/222861/13 类；ACID 10000/15767/10 类；CHV 1330/9209。(p.14)
- **指标**: IoU=0.5 下 mAP（各类 AP 平均，AP=P-R 曲线下面积）；FPS；log-average miss rate。(p.15)
- **结果**:
    - 整体 mAP：YOLO v3 = 71.22%，YOLO v4 = 81.47%。(p.16, p.19)
    - 速度：v4 31.94 FPS > v3 25.06 FPS。(p.17)
    - 规律：材料类 mAP 普遍高、工人类低。(p.17)
    - 最佳/最差 AP：正文称最高 hook 92.81%（标注为 v3）、hopper 95.18%（v4）；最低 fence 50.99%（v3）、helmet 55.62%（v4）。**矛盾**：Table 5 中 v3 hook=91.76、v4 hook=92.81，故 92.81% 实属 v4，正文归属有误。(p.17, p.19)
    - 定性：复杂场景 v4 优于 v3。(p.17)
- **消融**: 提取文本未明确说明。
- **泛化**: 无定量跨域测试，仅真实工地图像定性验证。(p.17)
- **效率**: 报告 FPS；未给 Params/FLOPs。

## 7. 这篇论文真正有价值的地方
1.  **即用型多要素基准**：首次把材料与布局纳入工地检测体系，类别定义贴合工程，直接降低研究门槛。
2.  **工程化避坑指南**：公开真实代价（隐私占清洗 2/3、删 2017 张、人均 37 处遗漏、'w' 误标等），过程透明度参考价值高。
3.  **暴露场景难点**：fence/helmet 等小目标/复杂背景类别 AP 仅 50–56%，而规则大目标（hopper/scaffold）90%+，指明密集小目标与杂乱背景为主攻方向。

## 8. 局限与问题
1.  规模与类别相对深度学习通用大集仍偏小，需扩充。(p.20)
2.  仅边界框（目标级）标注，无像素级，不能训练分割。(p.20)
3.  算法探索浅，仅 YOLO v3/v4，未用更先进检测器。(p.20)
4.  采集/标注重度依赖人工、成本高，监控视频常被删难获取；未来可众包/自动标注、借行业权限扩充。(p.10, p.12, p.20)
5.  **内部一致性问题**：正文与 Table 5 对最高 AP 的模型归属自相矛盾；清洗时间占比两处不一（25% vs 16.4%）。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要(p.1)、引言(p.1–3)、结论(p.20)、Table 4。
- **复现/用数据**：精读 §3(p.6–12) 清洗四目标与四条标注标准；下载见 p.20（华南理工 OSS，VOCv1.zip）。
- **借鉴创新**：多源采集（含吊钩可视化）、质量控制与隐私处理流程、行业知识→15 类体系。
- **写 related work**：归入"特定行业（建筑/施工）目标检测数据集"或"工业视觉 benchmark"。

## 10. 和其他论文的关系
- 直接对比/引用的数据集：MOCS（An 等）、ACID（Xiao 等）、CHV（Wang 等）、Kolar 等护栏集、Li 等安全帽集。
- 基准算法：YOLO v3/v4（单阶段）；背景综述 R-CNN/Fast/Faster R-CNN（两阶段）。
- 可能后续：接更先进检测器探索上限、数据增强/域自适应解决跨工地泛化、扩展为像素级标注支持分割、作为小目标/密集/复杂背景检测的标准基线。

## 11. 关键词
SODA, 建筑工地, 目标检测数据集, Benchmark, 四要素(工人/材料/机械/布局), 15 类, YOLO v3/v4, VOC 格式, 数据清洗, 隐私处理, 吊钩可视化, 安全监控

## 12. 可信度说明
本精读基于覆盖全 23 页的 PDF 提取文本（缓存完整，full coverage）。摘要已据提取文本重建（修复断词与杂入符号）。所有具体数字（19,846 张图像、286,201 对象、21,863 采集、17,861/1,985 划分、71.22%/81.47% mAP、25.06/31.94 FPS、2017 张无效图、1307 处遗漏、1246/300/286 工时等）均直接来自提取文本。对论文自身存在的两处内部矛盾（最高 AP 模型归属：正文 vs Table 5；清洗时间占比 25% vs 16.4%）已显式标注，引用时建议以表格/细分表为准并交叉核对。提取文本未明确给出本文的发表期刊名与 DOI，故 venue/doi 保留"未明确"；消融实验与跨域泛化定量测试在提取文本中未见。

---

> **可信度补充**: PDF 提取质量 = **medium** (PDF 文本可读 (2449 字符/页), 尚未人工核验); 来源缓存: `.paper-cache/extracts/2022_SODA_Site_Object_De.txt` (23/23 页); 提取引擎: pymupdf; 内容覆盖: full; 生成日期: 2026-06-10; 模式: LLM (mimo-v2.5-pro)。本轮据全文提取文本重核：重建英文摘要+中译、补全对比数据集数值/硬件/工时/清洗细节、标注论文内部两处自相矛盾、primary_topic 由 C 调整为 L_数据集_Benchmark。
<!-- AI_READING_NOTE_END -->
