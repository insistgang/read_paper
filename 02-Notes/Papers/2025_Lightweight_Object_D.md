---
title: Lightweight Object Detection Using Quantized YOLOv4-Tiny for Emergency Response in Aerial Imagery
authors:
  - "Sindhu Boddu"
  - "Arindam Mukherjee"
year: 2025
venue: "arXiv"
doi: 
pdf: [[2025_Lightweight_Object_D.pdf]]
primary_topic: C2_目标检测_违建_车辆_船舶_行人
topics:
  - "C2_目标检测_违建_车辆_船舶_行人"
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
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/2025_Lightweight_Object_D.txt
---

# Lightweight Object Detection Using Quantized YOLOv4-Tiny for Emergency Response in Aerial Imagery

## 基本信息
- **PDF**: [[2025_Lightweight_Object_D.pdf]]
- **primary_topic**: `C2_目标检测_违建_车辆_船舶_行人`
- **topics**: `C2_目标检测_违建_车辆_船舶_行人`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Lightweight Object Detection Using Quantized YOLOv4-Tiny for Emergency Response in Aerial Imagery |
| **作者** | Sindhu Boddu; Dr. Arindam Mukherjee（UNC Charlotte，电气与计算机工程系，美国北卡夏洛特） |
| **发表时间** | 2025 |
| **刊物/会议** | arXiv（预印本） |
| **DOI** | 未明确 |

## 摘要

**清理后英文原摘要：**

> This paper presents a lightweight and energy-efficient object detection solution for aerial imagery captured during emergency response situations. We focus on deploying the YOLOv4-Tiny model, a compact convolutional neural network, optimized through post-training quantization to INT8 precision. The model is trained on a custom-curated aerial emergency dataset, consisting of 10,820 annotated images covering critical emergency scenarios. Unlike prior works that rely on publicly available datasets, we created this dataset ourselves due to the lack of publicly available drone-view emergency imagery, making the dataset itself a key contribution of this work. The quantized model is evaluated against YOLOv5-small across multiple metrics, including mean Average Precision (mAP), F1 score, inference time, and model size. Experimental results demonstrate that the quantized YOLOv4-Tiny achieves comparable detection performance while reducing the model size from 22.5 MB to 6.4 MB and improving inference speed by 44%. With a 71% reduction in model size and a 44% increase in inference speed, the quantized YOLOv4-Tiny model proves highly suitable for real-time emergency detection on low-power edge devices.

**中文翻译：**

> 本文针对应急响应场景下采集的空中图像，提出一套轻量、节能的目标检测方案。核心是部署 YOLOv4-Tiny 这一紧凑型卷积神经网络，并通过后训练量化（post-training quantization）将其精度压缩到 INT8。模型在作者自建的空中应急数据集上训练，该数据集含 10,820 张标注图像，覆盖关键应急场景。与依赖公开数据集的前人工作不同，由于缺乏公开的无人机视角应急图像，作者从零构建了该数据集，使数据集本身成为本文的一项关键贡献。量化后的模型与 YOLOv5-small 在多项指标上对比，包括平均精度均值（mAP）、F1 分数、推理时间和模型大小。实验表明，量化后的 YOLOv4-Tiny 在保持相当检测性能的同时，将模型大小从 22.5 MB 降至 6.4 MB，推理速度提升 44%。凭借 71% 的模型体积缩减和 44% 的推理速度提升，量化后的 YOLOv4-Tiny 非常适合在低功耗边缘设备上进行实时应急检测。

> **说明**：摘要中"从 22.5 MB 降至 6.4 MB（71% 缩减）"与正文 Table I 存在内部口径不一致——Table I 显示 YOLOv4-Tiny（FP32）本身为 14.5 MB，22.5 MB 实为对比模型 YOLOv5-small 的体积。论文在摘要与方法 D 节均写"22.5 MB→6.4 MB"。此处忠实保留论文原文数字，并提示该处口径需复核。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：人工智能与嵌入式系统结合，革新了实时监控应用，尤其在应急响应与灾害管理等关键场景。搭载机载相机和轻量检测算法的无人机越来越多地用于从空中视角采集信息，可探测并定位交通事故、翻车、火灾、以及救护车/警车等应急服务对象。然而，在树莓派（Raspberry Pi）这类资源受限边缘设备上实现准确且快速的检测仍是难题。
- **之前方法的问题**：Faster R-CNN、SSD 等传统框架准确但延迟高、算力需求大，不适合低功耗设备部署；YOLOv3、YOLOv5-small 等现代实时检测器虽高效，但面向电池供电的嵌入式平台时，仍可借助量化等模型压缩技术进一步优化。
- **核心矛盾**：在严格的实时推理、能效与小内存占用约束下，需在**检测准确性**与**计算效率（推理速度、模型大小、功耗）**之间取得平衡。论文给出的具体目标是：评估量化后的 YOLOv4-Tiny 能否作为在树莓派 5 上进行实时空中应急检测的可靠、节能替代方案。
## 关键贡献

1.  **构建领域专用数据集**：因缺乏公开的无人机视角应急图像，作者从零自建并标注了一个含 10,820 张空中应急图像、覆盖 7 类应急目标的数据集，并将数据集本身视为本文一项关键贡献。
2.  **系统比较两种轻量模型**：在同一数据集上以相同配置训练并对比 YOLOv4-Tiny 与 YOLOv5-small，不仅看精度指标（mAP、Precision、Recall、F1），更强调系统级指标（推理时间、FPS、模型大小、功耗）。
3.  **验证后训练量化的有效性**：用 ONNX Runtime 静态量化把 YOLOv4-Tiny 从 FP32 压到 INT8，模型大小降至 6.4 MB（论文称从 22.5 MB 降 71%，注意上文口径说明），推理速度提升约 44%，检测性能基本无损。
4.  **给出类别级检测结果与基准框架**：展示了 7 类应急车辆/事件的检测结果（定性图 1–3），并建立了一个面向时间敏感、算力受限场景的可复现轻量检测模型选型基准框架。

> 注：原笔记列的"在树莓派 5 上用 USB 功率计实测功耗"属于实验内容（Table II 确有），但方法 D 节明确写"硬件部署与功耗评估的细节将在第二篇论文中讨论（will be addressed in the second paper）"，本文正文中 Table II 给出了 FP32/INT8 在树莓派 5 上的推理时间与功耗对比，属本文已含结果。
## 方法

- **整体框架**：数据集准备 → 模型选择与训练（YOLOv4-Tiny 与 YOLOv5-small）→ 评估对比 → 选定 YOLOv4-Tiny → 后训练量化 → 在边缘设备（树莓派 5）上评估推理时间与功耗。
- **输入输出**：
    - **输入**：统一缩放到 416×416 像素的 RGB 空中图像。
    - **输出**：目标类别、边界框坐标和置信度分数。
- **关键模块与架构**：
    - **YOLOv4-Tiny**（主模型）：YOLOv4 的精简版，参数远少于全尺寸版本，适合低功耗边缘设备。
        - **骨干（Backbone）**：CSPDarknet53-tiny，提取层次化特征。
        - **颈部（Neck）**：PANet（路径聚合网络），做特征融合。
        - **检测头（Head）**：在两个不同尺度上预测边界框和类别概率。
    - **YOLOv5-small**（对比模型）：基于 PyTorch，部署便捷、精度略高，但模型尺寸与算力需求相对更大。
- **训练配置**（两模型相同，保证公平对比）：
    - 训练硬件：**NVIDIA GTX 1080 Ti GPU**。
    - 图像尺寸 416×416；批大小 16；**Epochs 100**；学习率 0.001（带余弦衰减）；优化器 **SGD（带动量）**。
    - **损失函数**：目标性（objectness）与分类用二元交叉熵（BCE），边界框回归用均方误差（MSE）。
    - 数据增强：水平翻转、旋转、亮度/对比度调整、缩放、裁剪、颜色抖动。
    - 用早停（early stopping）和基于验证损失的检查点防过拟合，按验证集最佳表现选最终模型。
- **后训练量化**：
    - 工具：**ONNX Runtime 静态量化**。
    - 步骤：1) 把 PyTorch 模型转 ONNX；2) 用 100 张代表性图像生成校准数据，计算缩放因子（scale）与零点（zero-point）；3) 调 ONNX Runtime API 做静态量化；4) 保存为 INT8 ONNX 文件。
    - 机制：把 32 位浮点权重和激活值转为 8 位整数（INT8），大幅降低内存占用并加速推理。
- **与已有方法差异**：相较依赖通用公开数据集的前人工作，本文自建针对性更强的应急数据集；评估不止比精度，更系统地考察 FPS、功耗等边缘部署关键指标，并在真实嵌入式硬件上验证。
## 实验

- **数据集**：自建空中应急响应数据集，10,820 张标注图像，**7 类**目标：救护车（Ambulance）、警车（Police）、消防车（Fire Engine）、着火车（Car on Fire）、车祸（Car Crash）、拖车（Tow Truck）、翻倒车（Car Upside Down）。来源含无人机视频、在线航空数据集、合成增强图像；标注为 YOLO 格式；按训练 80% / 验证 10% / 测试 10% 划分。
- **对比方法**：YOLOv5-small。
- **评价指标**：mAP@0.5、Precision、Recall、F1、推理时间、FPS、模型大小、平均功耗（W）。
- **主实验结果**：
    - **模型对比（Table I，GPU 端）**：

        | 指标 | YOLOv4-Tiny | YOLOv5-small |
        |------|------|------|
        | mAP@0.5 | 85.6% | 87.1% |
        | Precision | 0.86 | 0.89 |
        | Recall | 0.82 | 0.88 |
        | F1 Score | 0.84 | 0.88 |
        | 推理时间 | 39 ms | 43 ms |
        | FPS | 25.6 | 15.8 |
        | 模型大小 | 14.5 MB | 22.5 MB |
        | 平均功耗 | 33.8 W | 46.3 W |

        结论：YOLOv5-small 精度略高（mAP、F1），但 YOLOv4-Tiny 在推理速度、FPS、模型大小和功耗上明显占优（平均功耗约低 12.5 W），故选 YOLOv4-Tiny 做后续量化与部署。
    - **量化结果（Table II，YOLOv4-Tiny 在树莓派 5 上，FP32 vs INT8）**：

        | 指标 | FP32 | INT8 |
        |------|------|------|
        | 推理时间 | 25.5 ms | 28.2 ms |
        | 平均功耗 | 33.67 W | 13.85 W |
        | 最大功耗 | 63.43 W | 22.34 W |
        | 最小功耗 | 8.24 W | 8.14 W |
        | RMS 功耗 | 41.06 W | 14.92 W |

        结论：量化后推理时间仅微增 2.7 ms，但平均功耗降超 59%、最大功耗降近 65%、RMS 功耗从 41.06 W 降至 14.92 W，最小功耗也略降。模型大小从 22.5 MB 降至 6.4 MB（论文口径，见摘要说明）。
    - **定性结果（图 1–3）**：量化模型成功检出车祸（置信度 0.69、0.80）、翻倒消防车（0.74）、多辆警车（0.86、0.89）等，表明量化未损害实际部署中的检测质量。提取文本仅有图注文字，无图像像素信息。
- **消融/泛化实验**：提取文本未明确说明做了标准消融或跨数据集泛化实验；论文将类别不平衡处理、跨域迁移、Grad-CAM 可解释性等列入未来工作。
- **效率信息**：论文核心即效率，明确给出 FPS、推理时间、模型大小、GPU 与树莓派端实测功耗等对比数据。
## 局限

1.  **数据集局限**：数据集为自建、未公开，规模/多样性/可访问性有限，影响可复现性与广泛认可；论文自承存在类别不平衡（如"着火车"样本少）。
2.  **量化精度数据缺失**：论文给出 INT8 后的推理时间与功耗，但**未给出量化后具体 mAP/F1**，仅以定性图和"comparable performance"佐证精度无损，量化对精度的定量影响无法核实。
3.  **评估硬件单一**：边缘端评估仅在树莓派 5 上进行，未覆盖 Jetson Nano 等其他平台；论文将扩展到更多边缘硬件列为未来工作。
4.  **量化方法单一**：仅用 ONNX Runtime 静态后训练量化，未探索量化感知训练（QAT）或与剪枝、知识蒸馏结合（这些被列为未来方向）。
5.  **内部口径不一致**：摘要/方法称量化"22.5 MB→6.4 MB"，与 Table I 中 YOLOv4-Tiny 的 14.5 MB 相矛盾，论文未澄清；功耗量级（GPU 端 33–46 W 与树莓派端的标注）也需对照原图核实。
6.  **图表信息缺失**：图 1–3 的视觉内容无法从提取文本评估，定性质量需看原 PDF。
## 个人评论

1.  **系统级评估的思维值得借鉴**：论文反复强调，为嵌入式场景选模型时，FPS、功耗、模型大小等系统级指标与精度同等重要——本文里 YOLOv5-small 精度仅高约 1.5 个百分点，却在功耗上贵了约 12.5 W，这种"用 1.5% mAP 换可观能效"的取舍框架对落地很实用。
2.  **工程价值清晰，但科学新意有限**：后训练量化、YOLOv4-Tiny、ONNX Runtime 都是成熟技术，本文贡献更多在"把已知方法在特定应急/无人机场景做了一次干净的工程验证 + 自建数据集"，方法层面没有新模块或新损失，定位为应用/基准论文更准确。
3.  **数据集贡献是真亮点**：指出无人机视角应急图像缺公开集，自建 10,820 张 7 类数据集填补空白；若能公开，对该细分方向价值会更大（目前未公开是减分项）。
4.  **数字口径需谨慎引用**：22.5 MB/14.5 MB 的不一致、量化后缺 mAP、以及 33–46 W 这种偏高的"功耗"标注，提示读者引用本文具体数值时务必回查原表，不要直接转述摘要里的"71% 缩减"。

### 使用建议

- **快速了解**：读摘要、引言（I）、贡献与未来工作（V）、结论（VI）即可掌握核心思想、取舍结论。
- **复现研究**：重点看 III. METHODOLOGY（数据集准备、训练配置 416×416/bs16/100ep/SGD、ONNX 静态量化四步）和 IV. RESULTS AND DISCUSSION（Table I、Table II）；需自行构建类似数据集并配训练/量化环境。
- **借鉴创新点**：
    - 借鉴其系统级指标评估框架（尤其 USB 功率计实测功耗方法）。
    - 学习把 ONNX Runtime 后训练静态量化套到自定义 YOLO 模型上的完整四步流程。
    - 参考其构建领域专用小规模数据集的思路。
- **写 Related Work**：可放入"轻量化目标检测在边缘设备部署"或"模型量化在计算机视觉中的应用"的综述段落。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[C2_目标检测_违建_车辆_船舶_行人]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属计算机视觉**目标检测**子领域，聚焦**轻量级模型部署与模型压缩（量化）**在无人机/空中视角应急场景的应用。检测对象全部是车辆与交通事故类目标（救护车、警车、消防车、车祸、翻车等 7 类），从无人机航拍视角采集，部署目标是树莓派 5 这类资源受限边缘设备。由于检测目标专一为车辆/事件类，本文归入 `C2_目标检测_违建_车辆_船舶_行人` 比泛化的通用检测更贴切。性质上是一篇**应用/基准论文**，而非提出新检测算法。

## 2. 一句话总结
通过 ONNX Runtime 后训练静态量化把 YOLOv4-Tiny 压到 INT8，在树莓派 5 上以约 2.7 ms 的微小延迟代价换来超 59% 的平均功耗下降和 71% 的模型体积缩减，实现低功耗实时空中应急车辆检测；并在自建 10,820 张 7 类应急数据集上系统对比 YOLOv4-Tiny 与 YOLOv5-small，论证前者更适合边缘部署。

## 3. 背景与问题
- **为什么要做**：无人机搭载轻量检测算法可从空中快速定位交通事故、翻车、火灾、救护车/警车等应急事件，对应急响应价值大；但在树莓派等边缘设备上做到准确又快速很难。
- **之前方法的问题**：Faster R-CNN/SSD 准但慢、算力重；YOLOv3/YOLOv5-small 高效但面向电池供电平台仍可用量化进一步优化。公开的无人机视角应急图像数据集稀缺。
- **核心矛盾**：在实时推理、能效、小内存三重约束下平衡精度与效率。具体研究问题是：量化后的 YOLOv4-Tiny 能否作为树莓派 5 上实时空中应急检测的可靠、节能方案。

## 4. 核心贡献
1.  从零自建并标注 10,820 张、7 类的无人机视角应急数据集，填补该方向公开数据缺口，数据集本身即一项贡献。
2.  同配置训练并系统对比 YOLOv4-Tiny 与 YOLOv5-small，覆盖 mAP/Precision/Recall/F1 与 FPS/推理时间/模型大小/功耗两类指标。
3.  用 ONNX Runtime 静态后训练量化把 YOLOv4-Tiny 压到 INT8，模型降至 6.4 MB、推理提速约 44%、能效大幅提升，性能基本无损。
4.  给出 7 类应急目标的类别级检测结果，验证两模型在高变异空中场景的泛化与鲁棒性。
5.  建立面向时间敏感、算力受限环境的可复现轻量检测模型选型基准框架。

## 5. 方法详解
- **流程**：数据准备 → 训练 YOLOv4-Tiny 与 YOLOv5-small → 评估对比 → 选 YOLOv4-Tiny → 后训练量化 → 树莓派 5 评估推理时间与功耗。
- **输入输出**：输入 416×416 RGB 空中图；输出类别 + 边界框 + 置信度。
- **YOLOv4-Tiny 架构**：骨干 CSPDarknet53-tiny；颈部 PANet 特征融合；检测头在两个尺度预测框与类别。对比模型 YOLOv5-small（PyTorch，精度略高但更大）。
- **训练配置**：GTX 1080 Ti；416×416；batch 16；100 epochs；lr 0.001 + 余弦衰减；SGD（带动量）；损失 = objectness/分类 BCE + 边框回归 MSE；早停 + 验证损失检查点；增强含翻转/旋转/亮度对比度/缩放/裁剪/颜色抖动。
- **量化**：ONNX Runtime 静态量化；100 张校准图计算 scale 与 zero-point；四步 = PyTorch→ONNX、生成校准数据、ONNX Runtime API 静态量化、存 INT8 ONNX；FP32→INT8 降内存并加速。
- **差异**：自建针对性数据集 + 系统级指标评估 + 真实嵌入式硬件验证。注意方法 D 节自述"硬件部署与功耗细节将在第二篇论文展开"，但本文 Table II 已含树莓派 FP32/INT8 对比。

## 6. 实验与结果
- **数据集**：自建 10,820 张、7 类（救护车/警车/消防车/着火车/车祸/拖车/翻倒车），YOLO 格式标注，80/10/10 划分。
- **GPU 端对比（Table I）**：YOLOv4-Tiny mAP@0.5 85.6%、P 0.86、R 0.82、F1 0.84、39 ms、25.6 FPS、14.5 MB、33.8 W；YOLOv5-small mAP@0.5 87.1%、P 0.89、R 0.88、F1 0.88、43 ms、15.8 FPS、22.5 MB、46.3 W。结论：YOLOv5-small 精度略高，YOLOv4-Tiny 速度/体积/功耗占优。
- **量化对比（Table II，树莓派 5，FP32 vs INT8）**：推理 25.5→28.2 ms（+2.7 ms）；平均功耗 33.67→13.85 W（降超 59%）；最大功耗 63.43→22.34 W（降近 65%）；最小功耗 8.24→8.14 W；RMS 功耗 41.06→14.92 W。模型大小 22.5→6.4 MB（论文口径，与 Table I 的 14.5 MB 存在不一致）。
- **定性（图 1–3）**：检出车祸（0.69/0.80）、翻倒消防车（0.74）、多警车（0.86/0.89），量化未损实际检测质量。
- **量化后精度数据缺失**：论文未列 INT8 的 mAP/F1，精度无损仅靠定性图与文字佐证。
- **消融/泛化**：提取文本未见标准消融或跨集泛化实验。

## 7. 这篇论文真正有价值的地方
1.  **系统级评估框架**：用真实 USB 功率计在树莓派上量功耗，把 FPS、功耗、体积摆到与精度同等位置，给边缘选型提供实用视角与数据。
2.  **量化的工程收益直观**：以约 2.7 ms 延迟换 59%+ 功耗下降和 71% 体积缩减，定量展示后训练量化在低功耗实时部署的价值。
3.  **填补数据空白**：针对无人机应急这一缺公开集的细分方向自建数据集，推动该方向落地。
4.  **可复现基准**：完整给出训练超参与量化四步，便于他人复现与对照。

## 8. 局限与问题
1.  数据集自建未公开，规模/多样性有限，存在类别不平衡，影响可复现与认可度。
2.  **未给出量化后 mAP/F1**，量化对精度的定量影响无法核实，"性能无损"主要靠定性证据。
3.  边缘评估仅限树莓派 5，缺 Jetson 等其他平台对比。
4.  仅静态后训练量化一种压缩方法，未试 QAT、剪枝、蒸馏（均列入未来工作）。
5.  数字口径不一致（22.5 MB vs 14.5 MB）与偏高的功耗标注（GPU 端 33–46 W）需回查原表，引用须谨慎。
6.  图 1–3 视觉内容无法从提取文本核实。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要、引言（I）、贡献/未来工作（V）、结论（VI）。
- **复现**：重点看 III. METHODOLOGY（数据集、416×416/bs16/100ep/SGD、ONNX 静态量化四步）与 IV. RESULTS（Table I、II），需自建类似数据集并配训练/量化环境。
- **借鉴**：系统级指标评估框架（尤其 USB 功率计功耗测法）；ONNX Runtime 后训练静态量化套用到自定义 YOLO 的四步流程；构建领域专用小规模数据集的思路。
- **写 Related Work**：放入"轻量化检测的边缘部署"或"模型量化在 CV 中的应用"综述段落。

## 10. 和其他论文的关系
- **YOLO 系列**：直接基于 YOLOv4-Tiny（YOLOv4 精简版，CSPDarknet53-tiny + PANet）评估，并与 YOLOv5-small（Ultralytics）对比；引用了 YOLO[1]、YOLOv4[2]、Ultralytics[3]、SSD[5]、Faster R-CNN[6]、RetinaNet[7] 等检测基线。
- **模型压缩**：引用 Han 等[4] 的模型压缩综述（论证 INT8 后训练量化可大幅减小体积/推理时间且精度损失小）与 Hinton 等[9] 的知识蒸馏，属后训练量化/边缘计算主题。
- **应用领域**：属无人机/空中视角应急车辆检测的细分应用研究，与遥感/交通事件检测、智能交通、便携安防监控等场景相关。

## 11. 关键词
YOLOv4-Tiny、量化、INT8、后训练静态量化、ONNX Runtime、空中图像、无人机、应急响应、轻量化检测、边缘设备、树莓派 5、功耗优化、车辆检测

## 12. 可信度说明
本精读笔记基于提供的 PDF 提取文本（6/6 页）生成。
- **信息来源**：模型架构、训练超参、量化四步、Table I/II 的全部数值、7 类目标、数据集规模与划分等均严格摘录或转述自提取文本。
- **提取质量**：文本完整覆盖摘要、引言、相关工作、方法、结果与讨论、贡献与未来工作、结论；参考文献在第 25000 字符处被截断（仅到"REFEREN"），未做引文细节分析。
- **存疑处（已在正文标注）**：(a) 模型大小"22.5 MB→6.4 MB"与 Table I 中 YOLOv4-Tiny 的 14.5 MB 不一致，系论文内部口径问题；(b) 量化后缺 mAP/F1；(c) GPU 端"功耗 33–46 W"量级偏高，需对照原图核实；(d) 图 1–3 仅有图注、无像素信息。除标注处外，未添加外部知识或推测。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 4173 字符/页, 6/6 页); 提取在 ~25000 字符处于参考文献(REFERENCES)起始处截断, 不影响正文; 来源缓存: `.paper-cache/extracts/2025_Lightweight_Object_D.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
