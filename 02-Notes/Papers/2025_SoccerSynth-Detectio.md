---
title: "SoccerSynth-Detection: A Synthetic Dataset for Soccer Player Detection"
authors:
  - "Haobin Qin"
  - "Calvin Yeung"
  - "Rikuhei Umemoto"
  - "Keisuke Fujii"
year: 2025
venue: "arXiv:2501.09281v2 [cs.CV] (2025-10-03)"
doi: 10.48550/arXiv.2501.09281
pdf: [[2025_SoccerSynth-Detectio.pdf]]
primary_topic: L_数据集_Benchmark
topics:
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/2025_SoccerSynth-Detectio.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/14 pages"
---
# SoccerSynth-Detection: A Synthetic Dataset for Soccer Player Detection

## 基本信息
- **PDF**: [[2025_SoccerSynth-Detectio.pdf]]
- **primary_topic**: `L_数据集_Benchmark`
- **topics**: `L_数据集_Benchmark`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | SoccerSynth-Detection: A Synthetic Dataset for Soccer Player Detection |
| **作者** | Haobin Qin; Calvin Yeung; Rikuhei Umemoto; Keisuke Fujii (名古屋大学信息学研究科 / RIKEN AIP / JST PRESTO) |
| **发表时间** | 2025 (arXiv v2, 2025-10-03) |
| **刊物/会议** | arXiv:2501.09281v2 [cs.CV]（预印本） |
| **DOI** | 10.48550/arXiv.2501.09281 |
| **代码/数据** | https://github.com/open-starlab/SoccerSynth-Detection |

## 摘要

**英文原文（据提取文本整理，修复断词与空格）**:

> In soccer video analysis, player detection is essential for identifying key events and reconstructing tactical positions. The presence of numerous players and frequent occlusions, combined with copyright restrictions, severely restricts the availability of datasets, leaving limited options such as SoccerNet-Tracking and SportsMOT. These datasets suffer from a lack of diversity, which hinders algorithms from adapting effectively to varied soccer video contexts. To address these challenges, we developed SoccerSynth-Detection, the first synthetic dataset designed for the detection of synthetic soccer players. It includes a broad range of random lighting and textures, as well as simulated camera motion blur. We validated its efficacy using the object detection model (Yolov8n) against real-world datasets (SoccerNet-Tracking and SportsMoT). In transfer tests, it matched the performance of real datasets and significantly outperformed them in images with motion blur; in pre-training tests, it demonstrated its efficacy as a pre-training dataset, significantly enhancing the algorithm's overall performance. Our work demonstrates the potential of synthetic datasets to replace real datasets for algorithm training in the field of soccer video analysis. The dataset is available at https://github.com/open-starlab/SoccerSynth-Detection.

**中文翻译**:

> 在足球视频分析中，球员检测是识别关键事件、重建战术位置的基础。球员数量众多、遮挡频繁，加上版权限制，严重制约了可用数据集的获取，能用的选择有限（如 SoccerNet-Tracking 与 SportsMOT），且这些数据集多样性不足，使算法难以适应多变的足球视频场景。为应对这些挑战，我们开发了 SoccerSynth-Detection——首个面向合成足球球员检测的合成数据集。它包含大范围随机化的光照与纹理，以及模拟的摄像机运动模糊。我们用目标检测模型（YOLOv8n）在真实数据集（SoccerNet-Tracking 与 SportsMoT）上验证了其有效性。在迁移测试中，它达到了真实数据集的性能水平，并在含运动模糊的图像上显著超越后者；在预训练测试中，它作为预训练数据集展现出有效性，显著提升了算法的整体性能。我们的工作证明了合成数据集在足球视频分析领域替代真实数据集进行算法训练的潜力。数据集已开源。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：球员检测是体育（尤其足球）视频处理的基础任务，直接影响下游的跟踪、动作识别（action recognition）、动作预测（action prediction）和比赛状态重建（game state reconstruction）。然而在体育场景下标注数据集困难重重——频繁遮挡、动态背景、光照变化、运动引起的模糊以及版权限制。足球因球员数量多，遮挡和跟踪尤为困难。
- **之前方法的问题**：现有真实球员检测/跟踪数据集（SoccerNet-Tracking 直播录像、SoccerTrack/TeamTrack 鱼眼+无人机、SoccerDB 电视转播、3x3 篮球数据集、SportsMOT 多运动跟踪等）总量仍有限、多样性不足。用模拟器生成合成数据已在行人检测、自动驾驶、室内场景理解等领域被广泛采用；足球领域虽有若干合成数据尝试（SoccerNet-Depth 用 NVIDIA Nsight 从 eFootball 抽深度图；RADepthNet 用 RenderDoc 生成 FIFADataset 深度图；基于网页工具的关键点提取场地数据集；Kaneko 等用 Google Research Football 模拟器训练传球预测；Qin 等用足球摄像机模拟器+强化学习），但这些工具/游戏并非为计算机视觉研究设计，缺乏生成检测标注的功能，**始终没有专门用于足球球员检测的合成数据集**。
- **核心矛盾**：检测算法对大规模、多样化标注数据的需求，与真实足球数据集获取成本高、多样性低之间的矛盾。

## 关键贡献

> 论文 1 Introduction 末尾明确列出 3 条贡献：

1. **发布首个专用数据集**：发布 `SoccerSynth-Detection`，第一个专门为足球球员检测设计的合成数据集。
2. **增强模拟器以生成检测数据**：在前作模拟器（Qin et al. [39]）基础上扩展——增强摄像头特性以适配检测，并引入随机光照和纹理，使其能生成足球检测数据集。
3. **实证合成数据可替代/补充真实数据**：证明 `SoccerSynth-Detection` 可以替代并补充真实数据集用于训练检测模型。

## 方法

- **整体框架**：基于 `Unreal Engine` 的足球场模拟器，通过引擎插件在渲染时捕获帧并自动生成 YOLO 格式的球员/足球检测边界框标注；通过领域随机化（domain randomization）缩小合成—真实之间的域差距。
- **输入/输出**：
    - **输入**：模拟器构建的虚拟足球场环境。
    - **输出**：带像素级精确边界框标注（两类：0=球员 player，1=足球 soccer ball）的图像，分为清晰图（1920×1080）和运动模糊图（800×600），均按训练/验证子集划分。
- **关键模块与连接**：
    1.  **模拟器构建（2.1 Simulator Construction）**：
        - 因现有足球模拟器不支持边界框生成，在前作模拟器 [39] 上新建一个中心摄像头，其位置、角度、焦距参考 SoccerNet-Tracking 和 SportsMoT 配置（图 1 给出 (a) 无人机视角 / (b) 角点摄像头视角 / (c) 中心摄像头视角对比）。
        - 集成从 Unreal Engine Marketplace 购买的动态观众模型、球员角色模型与动画，用 `Behavior Tree` 和 `AI Controller` 实现球员移动逻辑，并用物理引擎模拟传球、带球、射门、接球，实现连续自主的比赛。
        - **行为规则**（论文逐条列出）：持球权归最后触球方所在球队；持球时门将传给前锋、后卫传给中场、中场传给前锋，前锋被包夹则回传、否则带球突入禁区向球门内随机选定点射门；丢球时最近球员上抢、门将在禁区内回抢、其他球员做战术无球跑动；无球移动遵循"持球方压上、无球方退防（门将除外）"；重置规则采用 4-4-2 阵型、无越位、球出界或时间结束即重置；足球运动由物理引擎模拟（带球时周期性向前踢球），传球先短暂停球→计算抛物线轨迹→施加所需力，接球时瞬时停球以模拟控球。
    2.  **数据生成与随机化（2.2 Data Generation）**：先在渲染中对光照、纹理做大范围随机化并加随机摄像机旋转，再用插件捕帧并生成边界框；具体随机化项：
        - **运动模糊**：通过拍摄时引入随机摄像机抖动来还原（图 2a）。
        - **场地特征随机化**：组合 10 种黄绿草色 + 5 种不同草纹理，增加背景视觉复杂度（图 2b）。
        - **光照条件随机化**：设计可调亮度与色温的梯度阳光系统，模拟一天不同时段日出日落（图 2c）。
        - **球员服饰随机化**：从大量预制图案库随机组合发型、球衣、短裤、球鞋纹理，覆盖真实球员的多样外观。
        - **摄像头参数随机化**：随机化角度与焦距，但基于真实比赛录像优化范围以保证视角真实可用。
        - **球员动作与场景再现**：用行为树组件模拟跑动、射门、传球等复杂动态比赛场景。
    3.  **标注生成模块**：使用从 Unreal Engine Marketplace 购买的 `"2D Bounding Box for Deep Learning Image Detection"` 插件，在渲染过程中直接为每个球员和足球生成像素级精确的边界框，标注存为 YOLO 格式（场上所有个体均标为 player）。
- **训练流程（2.3 Validation）**：所有实验用 `YOLOv8n` 并加载预训练参数 `yolov8n.pt`（以参数量小著称）。图像统一 640×640，学习率 0.01，最多 300 epoch，IoU 阈值 0.7，启用数据增强。为与真实标注习惯一致，将检测框水平宽度手动扩展 2 像素。
- **与已有方法的差异**：现有足球合成数据集（SoccerNet-Depth、RADepthNet 的 FIFADataset 等）主要从游戏（eFootball、FIFA）抽取深度图或做关键点，**并非为生成检测标注而设计**，且缺乏本文强调的大规模视觉随机化。本文是首个专注球员检测的合成数据集，系统集成了运动模糊与多种领域随机化。

## 实验

- **使用数据集**：
    - 合成数据集 `SoccerSynth-Detection`：用模拟器生成 **37,621 张清晰图 + 17,052 张运动模糊图**，按 **4:1** 划分训练/验证。
    - 真实对比数据集：`SoccerNet-Tracking`、`SportsMoT`（所有 person 相关标签统一为 "player"）。
- **对比方法**：在不同数据集上独立训练的 `YOLOv8n` 模型。
- **评价指标**：`AP50`（IoU=0.5 时的 AP，反映基础检测能力）与 `AP50:5:95`（IoU 0.5→0.95 步长 0.05 的平均 AP，反映定位严格性）。
- **主实验结果**：
    1.  **迁移学习实验（synth-to-real 对照，表 1）**——独立训练后在未见过的真实数据集上测试：
        | 训练数据 | 测试数据 | AP50 | AP50:5:95 |
        |---|---|---|---|
        | SoccerNet-Tracking | SportsMoT | 90.3 | 62.3 |
        | **SoccerSynth-Detection** | SportsMoT | 88.1 | **63.3** |
        | SportsMoT | SoccerNet-Tracking | 82.8 | 43.9 |
        | **SoccerSynth-Detection** | SoccerNet-Tracking | **89.4** | **48.4** |
        - 测 SportsMoT：合成数据 AP50 下降 2.2pp（88.1 vs 90.3），但 AP50:5:95 提升 1.0pp（63.3 vs 62.3）。
        - 测 SoccerNet-Tracking：合成数据相对 SportsMoT 训练显著提升 **AP50 +6.6pp（89.4 vs 82.8）、AP50:5:95 +4.5pp（48.4 vs 43.9）**。
    2.  **预训练实验（表 2）**——对 SoccerNet-Tracking、SportsMoT 按 1/2、1/4、1/8 子采样，比较是否用 SoccerSynth-Detection 预训练：
        - 以 SoccerNet-Tracking 为真实数据时，预训练带来 AP50/AP50:5:95 约 **0.1–1.5pp** 提升，有效缓解数据量减少的不利影响。
        - **最显著提升**：SportsMoT 子采样 1/8 时，预训练后 AP50 达到 **95.3%**（不预训练为 92.6%，提升 2.7pp，为表中最高 AP50）。
        - 注意并非全部场景都提升：如 SportsMoT 1/2 时 AP50 反而 93.6→92.6（提升不一致，整体在稀疏数据场景收益最明显）。
- **定性分析（4 Discussion，图 3/4）**：可视化显示 SoccerNet-Tracking 训练的 YOLOv8n 在 SportsMoT 图上产生大量重叠且偏移的框，SoccerSynth 训练的模型识别更准；反向亦然（SportsMoT 训练者在 SoccerNet 上检测失败）。SoccerSynth 之所以在 AP50:5:95 占优，归因于其接触了更多样、更大量的运动模糊图像，检测轮廓能更精确贴合球员外形。图 3c 揭示 SoccerSynth 训练的模型会漏检球员头部，源于合成数据中球员头部模型多样性不足，这正是其在 SportsMoT 上 AP50 偏低的原因（作者计划未来引入更多头部纹理贴图）。
- **消融实验**：提取文本未明确提及针对各随机化技术的独立消融实验。
- **速度/参数量/FLOPs**：提取文本未给出推理速度、参数量、FLOPs 等效率数据（仅提到 YOLOv8n 参数量小）。

## 局限

> 论文 Discussion 明确两条主要局限，其余为可推断的工程局限：

1.  **视角单一**：数据集仅由中心摄像头生成，缺乏真实转播中的多种机位（角点、无人机、底线等），可能限制对多视角场景的泛化（作者计划引入多机位）。
2.  **帧间不连续**：为增加多样性，相邻帧之间是不连续的，难以直接用于需要时序连续性的视频任务（如跟踪）；作者计划引入球员区分与编号标签以在一定时段内保证帧连续性。
3.  **头部模型多样性不足**：合成球员头部模型种类少，导致在 SportsMoT 上漏检头部、AP50 偏低。
4.  **未报告生成成本**：论文未讨论生成数万张图所需的算力与时间，复现成本不明（数据将在论文发表后释放）。
5.  **任务范围有限**：仅标注球员与足球两类，未含球门、裁判等其他物体，也无球员 ID、姿态等细粒度标注。

## 个人评论

1.  **数据生成范式**：提供了完整可复现的范式——用现代游戏引擎（Unreal Engine）+ 领域随机化，低成本生成大规模、像素级精确标注的检测数据。这对任何面临数据稀缺的视觉领域（体育、自动驾驶、机器人）都有借鉴价值，本文也明确把方法谱系挂靠到行人检测/自动驾驶的合成数据研究上。
2.  **领域随机化的具体清单**：论文把足球场景下实施的随机化逐项列清（运动模糊、10 草色×5 草纹理、梯度阳光、服饰库、机位/焦距），这种"配方级"细节可直接迁移到其他合成数据项目，比泛泛而谈的 domain randomization 更可操作。
3.  **评估设计有模板价值**：不止做迁移学习，还设计了"预训练+不同子采样率微调"的范式，分别验证合成数据的两类价值——增强鲁棒性（尤其运动模糊）与缓解数据稀缺。值得注意的是实验也诚实暴露了反例（SportsMoT 1/2 预训练反降、AP50 在某测试集略弱），没有粉饰，这反而提升了结论可信度。
4.  **可商榷处**：所有实验只用 YOLOv8n 单一轻量模型，缺乏跨检测器（如 Faster R-CNN、RT-DETR）的验证，合成数据增益是否对更大/更新模型同样成立尚不确定；且仅以 AP 衡量、未做统计显著性或多次随机种子，部分 0.1–0.3pp 量级的"提升"解释需谨慎。

### 使用建议

- **如果快速了解**：读 **摘要**、**1 Introduction** 末尾的 3 条贡献、**2.2 Data Generation** 的随机化清单、**3 Results** 的表 1 与表 2。
- **如果复现**：精读 **2.1 Simulator Construction**（含行为规则）和 **2.2 Data Generation**，注意其依赖的 Unreal Engine 付费插件/资产（观众模型、角色模型、"2D Bounding Box for Deep Learning Image Detection" 插件）。训练超参见 **2.3 Validation**。
- **如果借鉴创新点**：学习其领域随机化配方，以及"游戏引擎插件生成像素级检测标注"的工程路径；"迁移学习+预训练"的评估框架可直接套用。
- **如果写 related work**：可归入"合成数据集与领域随机化"或"体育视频分析与数据集"，作为首个足球球员检测合成数据集引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[L_数据集_Benchmark]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
计算机视觉目标检测领域，应用于足球视频分析中的球员检测。论文的核心交付物是一个**合成数据集**及其生成器（基于 Unreal Engine + 领域随机化），用以缓解真实足球检测数据集稀缺、多样性不足的问题。因核心成果是数据集/Benchmark，最贴切的主题是 `L_数据集_Benchmark`。预印本 arXiv:2501.09281v2 [cs.CV]（2025-10-03），代码与数据在 open-starlab/SoccerSynth-Detection。

## 2. 一句话总结
提出 SoccerSynth-Detection——首个面向足球球员检测的合成数据集，通过在 Unreal Engine 模拟器中引入大范围随机光照/纹理/运动模糊（领域随机化），用 YOLOv8n 在真实数据集上验证：合成数据训练可媲美真实数据、在运动模糊场景更优，且作为预训练数据能在低数据量场景显著提升性能。

## 3. 背景与问题
- **为什么要做**：球员检测是足球视频处理的基础任务，支撑跟踪、动作识别/预测、比赛状态重建。但体育数据标注受制于频繁遮挡、动态背景、光照变化、运动模糊和版权限制，足球因球员多而尤甚。
- **之前方法的问题**：真实数据集（SoccerNet-Tracking、SoccerTrack、TeamTrack、SoccerDB、SportsMOT 等）总量有限、多样性不足；已有足球合成数据（SoccerNet-Depth、FIFADataset、关键点场地数据、Google Research Football 等）面向深度/关键点/策略，**非为检测标注设计**，因为这些模拟器/游戏不是为 CV 研究做的、缺乏生成标注的功能。
- **核心矛盾**：检测算法对大规模多样化标注数据的需求 vs 真实足球数据获取成本高、多样性低。

## 4. 核心贡献
1. 发布首个专为足球球员检测设计的合成数据集 SoccerSynth-Detection。
2. 在前作模拟器 [39] 上扩展——增强摄像头特性以适配检测、引入随机光照与纹理，使其能生成检测数据集（含生成器开源）。
3. 实证 SoccerSynth-Detection 可替代并补充真实数据集训练检测模型，尤其在运动模糊场景与低数据预训练场景。

## 5. 方法详解
- **整体框架**：Unreal Engine 足球场模拟器 → 渲染时大范围随机化光照/纹理 + 随机摄像机旋转 → 用 "2D Bounding Box for Deep Learning Image Detection" 插件捕帧并生成像素级边界框 → 输出 YOLO 格式标注。两类：0=球员、1=足球。
- **模拟器构建（2.1）**：在前作 [39] 上新建中心摄像头，位置/角度/焦距参考 SoccerNet-Tracking 与 SportsMoT；集成 Marketplace 购买的动态观众与角色模型/动画，用 Behavior Tree + AI Controller 驱动球员逻辑，物理引擎模拟传/带/射/接球，实现连续自主比赛。行为规则覆盖持球权归属、各位置传球策略、丢球上抢、无球跑动、4-4-2 无越位的重置规则、踢球/传球（抛物线轨迹+施力）/接球（瞬时停球）机制。
- **数据生成与随机化（2.2）**：运动模糊（随机摄像机抖动）、场地（10 草色×5 草纹理）、光照（可调亮度色温的梯度阳光，模拟日出日落）、服饰（发型/球衣/短裤/球鞋随机组合）、机位（角度焦距随机但基于真实录像优化）、动作场景（行为树驱动跑/射/传）。动机是用领域随机化缩小合成—真实域差距。
- **输出规格**：清晰图 1920×1080、运动模糊图 800×600，训练/验证子集划分。
- **训练（2.3）**：YOLOv8n 载入 yolov8n.pt；img 640×640、lr 0.01、≤300 epoch、IoU 0.7、数据增强；检测框水平宽度手动+2 像素以匹配真实标注习惯。

## 6. 实验与结果
- **数据**：SoccerSynth-Detection 共 37,621 清晰 + 17,052 运动模糊图，4:1 训/验；真实对比 SoccerNet-Tracking、SportsMoT（person 标签统一为 player）。
- **指标**：AP50、AP50:5:95。
- **迁移学习（表 1）**：
    - SoccerNet-Tracking→SportsMoT 90.3/62.3；**SoccerSynth→SportsMoT 88.1/63.3**（AP50 −2.2pp，AP50:5:95 +1.0pp）。
    - SportsMoT→SoccerNet 82.8/43.9；**SoccerSynth→SoccerNet 89.4/48.4**（AP50 +6.6pp，AP50:5:95 +4.5pp）。
- **预训练（表 2）**：对 1/2、1/4、1/8 子采样比较是否用 SoccerSynth 预训练。
    - 以 SoccerNet-Tracking 为真实数据，预训练带来约 0.1–1.5pp 提升。
    - **SportsMoT 1/8 时预训练后 AP50 达 95.3%（vs 92.6%，+2.7pp，全表最高）**；但并非全场景提升（如 SportsMoT 1/2 的 AP50 93.6→92.6 反降）。
- **定性（图 3/4）**：合成数据训练者在跨域图上框更准、轮廓贴合更好（解释其 AP50:5:95 优势源于丰富运动模糊曝光）；但会漏检头部（头部模型多样性不足 → SportsMoT 上 AP50 偏低）；预训练有助减少误检、提升检测框置信度。
- **消融**：提取文本未见独立随机化消融。
- **效率指标**：提取文本未给出速度/参数量/FLOPs（仅称 YOLOv8n 参数量小）。

## 7. 这篇论文真正有价值的地方
1.  **可复现的数据生成范式**：游戏引擎 + 领域随机化低成本造大规模像素级精确检测标注，对数据稀缺的视觉领域普遍适用。
2.  **配方级的随机化清单**：把足球场景的随机化项逐一列清（草色/纹理数量、梯度阳光、服饰库、运动模糊实现），可操作性强、易迁移。
3.  **评估框架有模板价值**：迁移学习 + "预训练×子采样率微调"两条线，分别验证鲁棒性增益与数据稀缺缓解，并诚实呈现反例，便于他人套用与判读合成数据价值。

## 8. 局限与问题
1.  视角单一（仅中心摄像头），缺多机位，限制多视角泛化（作者计划补多机位）。
2.  帧间不连续，难直接用于时序/跟踪任务（作者计划加球员编号以保证一定时段帧连续）。
3.  头部模型多样性不足 → SportsMoT 上漏检头部、AP50 偏低。
4.  未报告生成所需算力/时间，复现成本不明；数据待论文发表后释放。
5.  任务范围窄：仅球员+足球两类，无球门/裁判，无 ID/姿态等细粒度标注。
6.  （评审补充）仅验证 YOLOv8n 单一轻量检测器、仅用 AP 衡量、未做多种子/显著性检验，部分小幅"提升"的稳健性待确认。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 3 条贡献 + 2.2 随机化清单 + 表 1/表 2。
- **复现**：精读 2.1（含行为规则）、2.2，注意付费插件/资产依赖；超参见 2.3。
- **借鉴创新**：领域随机化配方 + 引擎插件生成检测标注的工程路径 + 迁移+预训练评估框架。
- **写 related work**：归入"合成数据集与领域随机化"或"体育视频分析与数据集"，作为首个足球球员检测合成数据集引用。

## 10. 和其他论文的关系
主题 `L_数据集_Benchmark`。本文设计参考并对比的真实数据集：
- `[[SoccerNet-Tracking]]`（来自足球直播录像的跟踪数据集，[23]）
- `[[SportsMOT]]`（多运动球员跟踪数据集，[27]）
- `[[SoccerTrack]]`（鱼眼+无人机足球数据集，[2]）；另提及 TeamTrack、SoccerDB、3x3 篮球数据集。
相关足球合成数据：SoccerNet-Depth [34]、RADepthNet/FIFADataset [35]、Google Research Football [38]。模拟器构建基于作者团队前作 Qin et al. [39]，整体方法谱系受行人检测/自动驾驶/室内场景理解的合成数据研究启发（[28–33]）。

## 11. 关键词
论文自带关键词：synthetic datasets, object detection, soccer。
扩展关键词：合成数据集、领域随机化、运动模糊、YOLOv8n、迁移学习、预训练、球员检测、Unreal Engine、体育视频分析、像素级边界框标注。

## 12. 可信度说明
本精读基于 PDF 提取文本（提取缓存覆盖前 12/14 页，已含摘要、引言、方法、结果、讨论、结论全部正文，仅缺参考文献页）。所有事实性描述、数字（数据集规模 37,621/17,052、表 1/表 2 的 AP 数值、超参 640×640/lr0.01/300epoch/IoU0.7、+2 像素框扩展、95.3% 最高 AP50 等）均直接源自提取文本。提取文本未涵盖的细节（独立消融、效率指标）已标注"未明确"。无据可查处一律标注，未编造。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2025_SoccerSynth-Detectio.txt` (提取缓存覆盖 12/14 页正文; 缺第 13-14 页参考文献, 由原 AI 全文补读补足); 生成日期: 2026-06-05; 本次重读核对日期: 2026-06-18; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-14; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-14。
- **提取情况**: 缺失页 2 页, 其中 2 页提取到可读文本。缺失页主要为参考文献或文献列表, 对方法和实验正文影响较小。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- 未从缺失页稳定识别到章节标题

### 缺失页关键摘录

- p.13: F., Yu, F.: Shift: a synthetic driving dataset for continuous multi-task domain
- p.13: N., Webb, R., Susskind, J.M.: Hypersim: A photorealistic synthetic dataset for
- p.13: photo-realistic dataset for structured 3d modeling. In: Computer Vision–ECCV
- p.13: M.: Soccernet-depth: a scalable dataset for monocular depth estimation in
<!-- AI_READING_NOTE_END -->
