---
title: A_New_High-Precision_and_Lightweight_Detection_Model_for_Illegal_Construction_Objects_Based_on_Deep_Learning
authors:
  - "Wenjin Liu"
  - "Lijuan Zhou"
  - "Shudong Zhang"
  - "Ning Luo"
  - "Min Xu"
year: 2024
venue: "Tsinghua Science and Technology"
doi: 10.26599/TST.2023.9010090
pdf: [[A_New_High-Precision_and_Lightweight_Detection_Model_for_Illegal_Construction_Objects_Based_on_Deep_Learning.pdf]]
primary_topic: C2_目标检测_违建_车辆_船舶_行人
topics:
  - "C2_目标检测_违建_车辆_船舶_行人"
status: ai-read
reading_stage: ai-fulltext
confidence: high
source_basis: pdf-text
date_added: 2026-06-05
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/A_New_High-Precision_and_Lightweight_Detection_Model_for_Illegal_Construction_Objects_Based_on_Deep_Learning.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/21 pages"
---
# A_New_High-Precision_and_Lightweight_Detection_Model_for_Illegal_Construction_Objects_Based_on_Deep_Learning

## 基本信息
- **PDF**: [[A_New_High-Precision_and_Lightweight_Detection_Model_for_Illegal_Construction_Objects_Based_on_Deep_Learning.pdf]]
- **primary_topic**: `C2_目标检测_违建_车辆_船舶_行人`
- **topics**: `C2_目标检测_违建_车辆_船舶_行人`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-05

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | A New High-Precision and Lightweight Detection Model for Illegal Construction Objects Based on Deep Learning |
| **作者** | Wenjin Liu; Lijuan Zhou; Shudong Zhang; Ning Luo; Min Xu (海南大学网络空间安全学院 / 首都师范大学信息工程学院) |
| **发表时间** | 2024 (收稿 2023-06-21, 录用 2023-08-27) |
| **刊物/会议** | Tsinghua Science and Technology, Vol. 29, No. 4, pp. 1002–1022 |
| **DOI** | 10.26599/TST.2023.9010090 (ISSN 1007-0214) |

## 摘要

> 来源: 据 PDF 提取文本整理。

**清理后的英文原摘要**：

Illegal construction has caused serious harm around the world. However, current methods are difficult to detect illegal construction activities in time, and the calculation complexity and the parameters of them are large. To solve these challenges, a new and unique detection method is proposed, which detects objects related to illegal buildings in time to discover illegal construction activities. Meanwhile, a new dataset and a high-precision and lightweight detector are proposed. The proposed detector is based on the algorithm You Only Look Once (YOLOv4). The use of DenseNet as the backbone of YDHNet enables better feature transfer and reuse, improves detection accuracy, and reduces computational costs. Meanwhile, depthwise separable convolution is employed to lightweight the neck and head to further reduce computational costs. Furthermore, H-Swish is utilized to enhance non-linear feature extraction and improve detection accuracy. Experimental results illustrate that YDHNet realizes a mean average precision of 89.60% on the proposed dataset, which is 3.78% higher than YOLOv4. The computational cost and parameter count of YDHNet are 26.22 GFLOPs and 16.18 MB, respectively. Compared to YOLOv4 and other detectors, YDHNet not only has lower computational costs and higher detection accuracy, but also timely identifies illegal construction objects and automatically detects illegal construction activities.

**中文翻译**：

违法建设在全球造成了严重危害。然而现有方法难以及时发现违法施工活动，且计算复杂度与参数量都很大。为解决这些问题，本文提出一种新颖独特的检测方法——通过及时检测与违法建筑相关的物体来发现违法施工活动；同时提出了一个新数据集和一个高精度、轻量化的检测器。该检测器基于 YOLOv4 算法：以 DenseNet 作为骨干网络（YDHNet），实现更好的特征传递与复用、提升检测精度并降低计算成本；采用深度可分离卷积对颈部（neck）和头部（head）进行轻量化，进一步减少计算量；并用 H-Swish 激活函数增强非线性特征提取、提升检测精度。实验表明，YDHNet 在所提数据集上取得 89.60% 的 mAP，比 YOLOv4 高 3.78%；其计算成本和参数量分别为 26.22 GFLOPs 与 16.18 MB。相比 YOLOv4 及其他检测器，YDHNet 不仅计算成本更低、检测精度更高，还能及时识别违法建设物体、自动检测违法施工活动。

**关键词**：illegal buildings; object detection; illegal construction objects; high-precision; lightweight。

## 研究背景与动机

- **为什么做**：违法建设（illegal construction / illegal building）是全球性难题，威胁城市规划、资源保护、公共安全、经济与社会稳定，还会造成环境污染（空气、土壤、水）和税收减少。论文引述了中国、中国香港（屋顶违建）、阿根廷、保加利亚（破坏生态系统与生物多样性）、希腊（部分城区违建占比高达 25%）、英国/新西兰/美国等地的案例。因此自动、高精度的违建检测技术尤为重要。
- **之前方法的问题**：
  1. **早期方法**（GIS + GPS 结合遥感、多时相高分辨率卫星影像）依赖人工统计地籍数据、检测周期长、成本高、难以自动化。
  2. **图像处理 + 经典机器学习**（建筑图像分割、Hough 变换、K-Means、HOG-LBP、阴影信息等）减少了人工，但需手工提取特征、检测精度不足。
  3. **基于深度学习 CNN 的方法**（GoogLeNet、AlexNet、UNet、CGAN、Faster R-CNN 等）显著提升精度，但仍有两个根本缺陷：(a) **计算复杂度高、参数量大、对硬件要求高**，不适合移动/智能设备部署；(b) **只能检测"已建成"的违建，无法及时预防或制止违建活动**。此外既有数据集多依赖卫星/无人机影像、仅适用特定区域、缺乏通用性。
- **核心矛盾 / 切入点**：把检测对象从"已建成的违法建筑"前移到"违法建设相关物体"（施工车辆、建材、工具等），从而在施工早期就能预警；同时在保证高精度的前提下大幅压缩计算量与参数量，使模型可在移动/智能设备实时部署。

## 关键贡献

1.  **新的违建检测范式**：不同于以往检测已建成建筑，本文用端到端深度学习检测器识别"违法施工相关物体"，实现违建活动的更快检测与早期预防（real-time detection and early prevention）。
2.  **构建新的违法建设物体数据集**：31 个类别、共 14,046 张图像；由架设在约 60 m 高塔架上的高清相机拍摄，涵盖城市与郊区等多种场景，以及雨、雪、雾等多种自然条件，并包含遮挡与重叠情形，以提升通用性（可跨国家/地区使用）。
3.  **以 DenseNet121 为骨干**：替换 YOLOv4 原骨干 CSPDarkNet53，增强特征提取、复用与传递，提升精度的同时显著降低计算成本与参数量。
4.  **颈部与头部用 DSC 轻量化**：把 neck 和 head 中的 3×3 标准卷积改为深度可分离卷积（DSC），进一步降低计算量与参数，达到性能-资源的较优平衡。
5.  **采用 H-Swish 激活函数**：替换 YOLOv4 中主用的 Leaky ReLU，增强非线性特征学习能力，提升检测精度。
6.  **与 18 个 SOTA 检测器的综合评测**：YDHNet 在自建数据集上 mAP 达 **89.60%**，超过 SSD、RetinaNet、Faster R-CNN、YOLOv3/v4/v5/v7、YOLOX、EfficientDet 等；比 YOLOv4 高 **3.78%**。论文摘要/引言称 YDHNet 与 YOLOv4 相比，参数量与计算量分别仅为 **22.10%** 与 **25.24%**。

## 方法

- **整体框架**：YDHNet 基于 YOLOv4，由**输入模块、骨干网络（Backbone）、颈部（Neck：SPP + PANet）、预测头（YOLO Head）** 组成。
- **输入输出**：输入图像经马赛克（Mosaic）数据增强后统一缩放到 **416×416**；骨干输出三个尺度有效特征图（52×52、26×26、13×13）；最终输出 31 类违建物体的边界框、置信度与类别。
- **关键模块与连接**：
    1.  **输入模块（Mosaic 增强）**：随机裁剪、移动、拼接 4 张原图生成新图，丰富检测背景、缓解数据集尺度过于单一的问题，并避免训练时 BN 计算对大 batch size 的依赖。
    2.  **骨干网络 DenseNet121**（移除分类用全连接层，仅保留 head 的 3×3 卷积、池化层与 dense block 结构）。论文 Table 1 给出完整结构：7×7 conv(stride 2) → 3×3 max pool → Dense block_1(6×) → Transition_1 → Dense block_2(12×) → Transition_2 → Dense block_3(24×) → Transition_3 → Dense block_4(16×)。
        - **Dense Block**：每层在通道维与前面所有层相连并作为后一层输入；连接总数 C = L(L+1)/2（L 为层数）。密集连接实现特征复用、强化梯度流、以更少参数获得更丰富特征。本文 dense block 中堆叠 BN + H-Swish + 卷积层。
        - **Transition Layer**：BN + 1×1 卷积 + 2×2（平均）池化，在 dense block 之间下采样、压缩模型。
    3.  **颈部（Neck = SPP + PANet，标准卷积改 DSC）**：SPP 对 13×13 特征图做 5×5/9×9/13×13 三级最大池化，融合多尺度上下文、缓解裁剪缩放带来的目标残缺与形变；PANet 经卷积、上/下采样、特征融合输出三个改进特征图。论文 Fig.4 显示 neck 中以 "Conv ×n + DSC ×n" 的形式把 3×3 标准卷积替换为 DSC。
    4.  **预测头（YOLO Head，标准卷积改 DSC）**：由 3×3 卷积（特征整合）与 1×1 卷积（通道调整、得到预测结果）组成；判断目标是否可识别、类别是否符合三组先验框，再经 NMS 与先验框调整得到最终预测框。
    5.  **深度可分离卷积（DSC）**：将标准 3×3 卷积拆为 3×3 depthwise + 1×1 pointwise（论文 Eq.2–6 给出输出与计算量公式，及 DSC/标准卷积计算量之比约为 1/N + 1/G_K²），大幅降低参数与计算量。
    6.  **激活函数 H-Swish**：H-Swish(x) = x·ReLU6(x+3)/6，替换 backbone 外原用的 Leaky ReLU。论文列举其优点：无上界（防梯度饱和、加速训练）、有下界（强正则、防过拟合）、非单调（保留少量负值、梯度流稳定）、处处连续可微、泛化与优化能力强；且比 Swish 计算更高效、减少内存访问。
- **损失函数**：YDHNet 总损失 Loss = 位置损失 L_l + 分类损失 L_c + 置信度损失 L_cf（Eq.9）。其中位置损失采用 **CIoU** 形式：L_l = 1 − IoU + ρ²(b_p,b_t)/c² + βν（含中心点欧氏距离项与长宽比一致性项 ν，Eq.10–13）；分类损失与置信度损失为逐网格、逐预测框的交叉熵（Eq.14–15，置信度损失含无目标项权重 λ_no）。
- **训练设置**：先在 Pascal VOC 上预训练再在违建物体数据集上微调；Adam 优化器，共 100 epoch；前 50 epoch 冻结 DenseNet121 骨干仅训非骨干部分（lr=0.001, batch=16），后 50 epoch 解冻全网训练（lr=0.0001, batch=8）。数据集划分 train/val/test = 11,376 / 1,265 / 1,405。
- **与已有方法的差异**：系统性而非单点改进——骨干换 DenseNet121 提升特征效率、neck/head 全面引入 DSC 做轻量化、激活函数换 H-Swish，三者协同在违建物体这一具体任务上平衡精度与效率。

## 实验

- **数据集**：自建违法建设物体数据集，31 类、14,046 张图。相机型号 DS-2TD6236-75C2L（云台型号 Hikvision iDS-2DY9437IX-A/SP，水平 360°、垂直 −20°~90°、工作温度 −40~70℃、防护 IP67）；原图 1080×1920，统一裁切为 416×416，用 LabelImg 标注，转为 Pascal VOC 格式。类别覆盖施工车辆（混凝土搅拌车、推土机、挖掘机、塔吊等）、建材（砖、土堆、木堆等）、施工工具（混凝土搅拌机等）。各类样本数量不均衡（Fig.8/9）。
- **实验环境**：NVIDIA GeForce GTX Titan X（12 GB）、Intel Xeon E5-2667 v4 @3.20 GHz、Ubuntu 18.04。
- **评价指标**：mAP、AP、precision、recall、F1-score、参数量（MB）、计算量（GFLOPs）。
- **5.1 与 YOLOv4 对比（Table 5）**：
    - YDHNet 的 precision/recall/F1 = **90.08% / 86.06% / 87.80%**；YOLOv4 = **85.03% / 82.76% / 83.56%**；YDHNet 分别高出 **5.05% / 3.30% / 4.24%**。
    - mAP：YDHNet **89.60%** vs YOLOv4 **85.82%**，高 **3.78%**。
    - YDHNet 在 31 类中 **25 类优于 YOLOv4**，仅 6 类略差（blue enclosure、earth vehicles、grave mound、green cover、scaffold、woodpile），论文归因于这些类在数据集中样本不均衡或目标特征不清晰、背景复杂。论文还指出将 grave mound 与 piece deposits 单独标注以减少混淆。
- **5.2 与 18 个 SOTA 检测器对比（Table 6）**：YDHNet mAP 89.60% 最高；其后依次 YOLOv3 86.37%、SSD 86.19%、YOLOv4 85.82%、RetinaNet 85.22%、YOLOX-M 83.70%、…、YOLOv7 81.54%（F1 79.75%）。**参数量/计算量**：YDHNet 仅 **16.18 MB / 26.22 GFLOPs**，低于 SSD(27.62 MB/63.74)、YOLOv4(64.10 MB/60.17)、YOLOv3(61.69 MB/65.82)、RetinaNet(36.95 MB/154.74)、Faster R-CNN(137.30 MB/370.46) 等，适合移动/智能设备实时部署。
- **5.3 消融实验（Table 7，以 YOLOv4 为基线 85.82%）**：
    - 单项：YD（仅换 DenseNet121）→ 88.60%（+2.78%）；YM（仅加 DSC）→ 86.46%（+0.64%）；YA（仅换 H-Swish）→ 87.09%（+1.27%）。
    - 双项：YDM（DenseNet+DSC）→ 88.93%（+3.11%）；YDA（DenseNet+H-Swish）→ 89.02%（+3.20%）；YMA（DSC+H-Swish）→ 87.45%（+1.63%）。
    - 全部：YDHNet → 89.60%（+3.78%）。可见 DenseNet 骨干贡献最大，DSC 单独提升精度有限（主要作用是降参降算），H-Swish 居中。
- **效率结论**：YDHNet 在精度提升的同时，参数量与计算量相比 YOLOv4 及多数重型检测器显著下降，达到较好的精度-效率平衡。

## 局限

1.  **检测目标的间接性**：通过检测施工车辆、建材、工具等"相关物体"来推断违法施工，是一种间接信号；其有效性依赖于类别定义的代表性，在隐蔽或非典型施工场景下可能误判/漏判。
2.  **类别不均衡与困难类**：6 类（blue enclosure、green cover、woodpile 等）AP 偏低，论文自承与样本不均衡、目标特征不清晰、背景复杂有关，针对长尾类别缺乏专门处理。
3.  **数据集泛化性待验证**：作者宣称数据集可跨国家/地区通用，但全部图像来自同一套塔架高清相机（约 60 m 高、固定型号），实际采集地点未明确；对其它来源（卫星/无人机/手机）影像的迁移能力未做实验验证。
4.  **缺少推理速度/部署实测**：虽强调"轻量、可移动端部署"，但只报告参数量与 GFLOPs，未给出实际帧率（FPS）或在嵌入式/移动端硬件上的推理延迟测试。26.22 GFLOPs 对低端边缘设备可能仍偏高。
5.  **对"遮挡/密集"问题缺乏针对性验证**：引言指出现有方法在密集遮挡建筑上不足，数据集也声称含遮挡与重叠，但方法部分没有专门设计、实验也未单独评估遮挡/密集场景下的表现。

## 个人评论

1.  **问题定义的创新**：把检测目标从"已建成违法建筑"前移到"违法建设相关物体"，为**施工早期干预**提供了技术可行性，比"事后拆除"更贴近监管的真实需求，是本文最有价值的角度。
2.  **系统性的轻量化思路**：不是单点替换，而是从**骨干特征效率（DenseNet）** 与**网络结构计算效率（DSC）** 两个层面协同，加上激活函数（H-Swish）微调，给出了一条清晰的轻量化检测器设计范式。消融表也佐证了"骨干换 DenseNet 贡献精度、DSC 主要降算降参"的分工。
3.  **数据集构建的启示**：直面既有数据集"区域特定、依赖卫星/无人机"的局限，示范了如何用固定塔架高清相机构建面向具体任务（施工物体）、覆盖多场景多天气的专用数据集，并给出 31 类的明确定义表，对后续同类研究有参考价值。
4.  **工程组合的实用性**：把 DenseNet、DSC、H-Swish 等成熟模块组合进 YOLOv4 并取得成效，是"精选+组合高效模块改进主流检测器"的实用样板；但学术新颖性偏弱，核心组件均为已有技术。
5.  **可改进处**：对比公平性（不同检测器是否同等调参/同输入尺寸）、长尾类别处理、真实推理速度与边缘部署可行性，都是值得补强的环节。

### 使用建议

- **快速了解**：读 Abstract、Introduction 的贡献列表（5 条）、Section 5.1–5.3（与 YOLOv4 对比 / 与 SOTA 对比 / 消融），即可掌握核心问题、方法亮点与主要结论。
- **复现**：精读 Section 3（方法）——DenseNet121 如何接入 YOLOv4（Table 1 结构 + Fig.6 网络图）、DSC 替换了 neck/head 哪些 3×3 卷积（Fig.4）、H-Swish 集成位置、损失函数（Eq.9–15，CIoU 位置损失）；以及 Section 4.1–4.2 的数据集构建与训练设置（VOC 预训练 + 微调、冻结/解冻两阶段、Adam、lr 与 batch 调度）。
- **借鉴创新点**：
    - 学习其**问题重新定义**（检测施工物体而非建筑）。
    - 学习其**系统性轻量化设计**：骨干选型 + 各阶段（Neck/Head）轻量算子（DSC）+ 激活函数。
    - 把**密集连接**或**深度可分离卷积**模块迁移到自己的检测器改进中。
- **写 Related Work**：可归入"基于深度学习 CNN 的违建/施工物体检测"，尤其是**轻量化与效率提升**方向。

## 相关论文与链接

> - [[C2_目标检测_违建_车辆_船舶_行人]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**目标检测**应用论文，落在"违法建设（违建）物体检测 + 轻量化检测器设计"的交叉点，发表于 *Tsinghua Science and Technology* (Vol. 29, No. 4, 2024)。它要解决的核心问题是：如何用计算机视觉**及时**发现违法施工活动。与多数"检测已建成违法建筑"的工作不同，本文把检测对象定义为**违法建设相关物体**（施工车辆、建材、工具等），从而在施工早期就能预警。检测数据并非卫星/无人机遥感影像，而是**约 60 m 高塔架高清相机**的地面斜视图像。因此在分类上更契合"目标检测—违建/车辆/船舶/行人"主题（C2），而非纯遥感建筑检测。

## 2. 一句话总结
本文提出轻量化检测器 YDHNet（YOLOv4 改进版：DenseNet121 骨干 + neck/head 深度可分离卷积 + H-Swish 激活），并自建 31 类、14,046 张违法建设物体数据集，在该数据集上取得 89.60% mAP（较 YOLOv4 +3.78%），同时参数量与计算量仅为 16.18 MB / 26.22 GFLOPs。

## 3. 背景与问题
- **为什么做**：违建是全球性难题（论文列举中国、香港、阿根廷、保加利亚、希腊≤25%城区违建、英美新等案例），危害城市规划、公共安全、经济社会稳定与生态环境。自动、高精度检测因此十分重要。
- **既有方法三代局限**：(1) 早期 GIS/GPS+遥感——人工密集、周期长、难自动化；(2) 图像处理+经典机器学习（Hough、K-Means、HOG-LBP 等）——需手工特征、精度不足；(3) 深度学习 CNN（GoogLeNet、UNet、Faster R-CNN 等）——精度高但**计算量大、参数多、硬件门槛高**，且**只能检测已建成违建、无法及时预防**；数据集多依赖卫星/无人机、区域特定、缺通用性。
- **核心矛盾**：在"自动 + 高精度"与"低计算量 + 低参数（可移动端部署）+ 早期可预防"之间取得平衡。

## 4. 核心贡献
1.  **新检测范式**：用端到端检测器识别"违建相关物体"，实现违建活动的实时检测与早期预防。
2.  **新数据集**：31 类、14,046 张，塔架高清相机采集，含城市/郊区、雨雪雾、遮挡重叠，强调通用性。
3.  **DenseNet121 骨干**：替换 CSPDarkNet53，增强特征提取/复用/传递，降参降算。
4.  **DSC 轻量化 neck/head**：3×3 标准卷积改深度可分离卷积。
5.  **H-Swish 激活**：替换 Leaky ReLU，提升非线性特征学习与精度。
6.  **18 个 SOTA 检测器综合评测**：mAP 89.60% 居首，较 YOLOv4 +3.78%；参数/计算量约为 YOLOv4 的 22.10%/25.24%。

## 5. 方法详解
- **框架**：基于 YOLOv4 = 输入模块 + Backbone + Neck(SPP+PANet) + YOLO Head；输入经 Mosaic 增强后缩放 416×416；骨干输出 52×52/26×26/13×13 三尺度特征。
- **骨干 DenseNet121**（去分类 FC，保留 head 3×3 conv / 池化 / dense block）：Table 1 给出 7×7conv(s2)→3×3maxpool→DB1(6×)→T1→DB2(12×)→T2→DB3(24×)→T3→DB4(16×)。Dense block 内堆叠 BN+H-Swish+卷积，层间通道维全连接（连接数 C=L(L+1)/2），实现特征复用、强化梯度流、以更少参数获更丰富特征；Transition layer = BN+1×1conv+2×2池化，负责下采样与压缩。
- **Neck**：SPP 对 13×13 做 5×5/9×9/13×13 最大池化融合多尺度上下文；PANet 经卷积/上下采样/特征融合输出三特征图；其中 3×3 标准卷积改为 DSC（Fig.4）。
- **Head**：3×3 conv（特征整合）+1×1 conv（通道调整/预测），3×3 改为 DSC；经 NMS 与先验框调整出最终框。
- **DSC**：3×3 depthwise + 1×1 pointwise（Eq.2–6），计算量约为标准卷积的 1/N + 1/G_K²，显著降参降算。
- **H-Swish**：x·ReLU6(x+3)/6（Eq.8），替换 backbone 外的 Leaky ReLU（Eq.7）；无上界/有下界/非单调/处处可微，泛化优、比 Swish 高效。
- **损失**：Loss = L_l(CIoU 位置) + L_c(分类交叉熵) + L_cf(置信度交叉熵)（Eq.9–15）。
- **训练**：VOC 预训练→违建数据集微调；Adam，100 epoch；前 50 冻结骨干(lr 0.001,bs 16)，后 50 解冻(lr 0.0001,bs 8)；train/val/test=11376/1265/1405。

## 6. 实验与结果
- **数据集**：31 类、14,046 张；相机 DS-2TD6236-75C2L（云台 Hikvision iDS-2DY9437IX-A/SP，360°/IP67）；原图 1080×1920→裁 416×416，LabelImg 标注，VOC 格式；类别样本不均衡。
- **环境**：GTX Titan X (12GB)、Xeon E5-2667 v4、Ubuntu 18.04。
- **指标**：mAP、AP、precision、recall、F1、参数量(MB)、GFLOPs。
- **5.1 vs YOLOv4（Table 5）**：YDHNet P/R/F1 = 90.08/86.06/87.80，YOLOv4 = 85.03/82.76/83.56（分别 +5.05/+3.30/+4.24）；mAP 89.60 vs 85.82（+3.78）；31 类中 25 类胜出、6 类略差（blue enclosure/earth vehicles/grave mound/green cover/scaffold/woodpile）。
- **5.2 vs 18 个 SOTA（Table 6）**：YDHNet mAP 89.60 居首；YOLOv3 86.37、SSD 86.19、YOLOv4 85.82、RetinaNet 85.22、YOLOv7 81.54 等其后。YDHNet 16.18 MB/26.22 GFLOPs，低于 SSD/YOLOv4(64.10/60.17)/YOLOv3/RetinaNet/Faster R-CNN(137.30/370.46) 等。
- **5.3 消融（Table 7，基线 YOLOv4 85.82）**：YD 88.60(+2.78)、YM 86.46(+0.64)、YA 87.09(+1.27)、YDM 88.93、YDA 89.02、YMA 87.45、YDHNet 89.60(+3.78)。DenseNet 骨干贡献最大；DSC 主要降参降算、精度增益小；H-Swish 居中。

## 7. 这篇论文真正有价值的地方
1.  **问题定义前移**：检测"施工物体"而非"已建成建筑"，使**早期干预**成为可能，更贴近监管实际。
2.  **系统性轻量化范式**：骨干（DenseNet 特征效率）+ 结构（DSC 计算效率）+ 激活（H-Swish）三层协同，消融表清晰量化各组件分工。
3.  **专用数据集**：31 类明确定义、多场景多天气、固定塔架采集，弥补既有数据集"区域特定/依赖遥感"的不足。
4.  **工程可复用**：成熟模块组合改进主流检测器的实用样板（虽学术新颖性有限）。

## 8. 局限与问题
1.  **间接检测**：靠"相关物体"推断违建，依赖类别代表性，隐蔽场景易误判漏判。
2.  **长尾类别**：6 个困难类 AP 偏低，缺乏针对性处理。
3.  **泛化性存疑**：全部图像来自同套塔架相机，跨来源（卫星/无人机/手机）迁移未验证。
4.  **缺速度/部署实测**：只报 GFLOPs/参数，无 FPS 或嵌入式实测；26.22 GFLOPs 对低端边缘仍偏高。
5.  **遮挡/密集未单独评估**：方法无专门设计、实验无专项指标。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + 贡献列表 + Section 5（5.1/5.2/5.3）。
- **复现**：Section 3（DenseNet 接入 Fig.6/Table 1、DSC 替换 Fig.4、H-Swish、损失 Eq.9–15）+ Section 4.1/4.2（数据集与两阶段训练）。
- **借鉴**：问题重定义、系统性轻量化设计、把密集连接/DSC 迁移到自有检测器。
- **写 Related Work**：归入"深度学习 CNN 违建/施工物体检测"中"轻量化与效率提升"方向。

## 10. 和其他论文的关系
- **直接基础**：[[YOLOv4: Optimal Speed and Accuracy of Object Detection]]（Bochkovskiy 等, 2020, 文献[40]）——本文改进对象。
- **骨干来源**：[[Densely Connected Convolutional Networks]]（Huang 等, CVPR 2017, 文献[45]）。
- **轻量算子**：MobileNets / MobileNetV3（文献[73][74]）——DSC 与 H-Swish 的出处。
- **对比检测器**：SSD、RetinaNet、Faster R-CNN、YOLOv3/v5/v7、YOLOX、EfficientDet（文献[33][34][36][46][47][70][75] 等）。
- **同作者团队相关违建工作**：CRMNet（anchor-free 违建物体检测, 文献[25]）、复杂场景违建图像高精度检测（文献[23]）。

## 11. 关键词
违法建设, 违建物体检测, 目标检测, 高精度, 轻量化, YOLOv4, DenseNet121, 深度可分离卷积(DSC), H-Swish, CIoU 损失, 施工活动早期预警。

## 12. 可信度说明
本次精读已覆盖全文（PDF 全 21 页，含方法 Section 3 的完整细节、数据集 Section 4、实验 Section 5 的三张主表 Table 5/6/7 及消融分析、结论 Section 6）。所有关键数字（mAP 89.60%、+3.78%、P/R/F1、16.18 MB / 26.22 GFLOPs、消融各项、train/val/test 划分、训练超参）均直接来自 PDF 提取文本，可信度高。需注意：原笔记中"YOLOv4 ≈64.36 MB / 103.92 GFLOPs"为误记，论文 Table 6 实为 YOLOv4 = **64.10 MB / 60.17 GFLOPs**，已据原文订正；"22.10% / 25.24%"是论文摘要/引言对 YDHNet 相对 YOLOv4 参数量/计算量比例的表述。原笔记 frontmatter 的 venue/year（"Remote Sensing / 2023"）亦为误记，实为 *Tsinghua Science and Technology*, Vol.29 No.4, 2024，已据 PDF 页眉与版权页订正。

---

> **可信度补充**: PDF 提取质量 = **high**; 提取缓存仅含前 12/21 页 (`.paper-cache/extracts/...txt`, 截至 §3.2)，本次复核已用 pdfplumber 通读全 21 页（含 Table 1/3/5/6/7、Eq.1–20、Section 4–6）补全后续页事实；生成日期: 2026-06-05；模式: LLM (mimo-v2.5-pro) + 全文人工对照修订（仍为 AI 阅读稿, human_reviewed=false）。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-21; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-21。
- **提取情况**: 缺失页 9 页, 其中 9 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Woodpile
- p.13: Vehicle
- p.13: Tower
- p.13: Small truck
- p.13: Simple house
- p.13: Scaffold
- p.13: Piece deposits
- p.13: Mixer
- p.13: Grey enclosure
- p.13: Greenhouse
- p.13: Green cover
- p.13: Grave mound

### 缺失页关键摘录

- p.13: Fig. 7 Samples images of the illegal construction objects dataset.
- p.13: Fig. 8 Number of images for each category of illegal construction object in the dataset. 1014 Tsinghua Science and Technology, August 2024 , 29(4): 1002 −1022
- p.14: using a dataset of illegal construction objects, which
- p.14: was proposed in this research. Table 5 presents the
- p.14: on the proposed dataset. The precision, recall, and F1-
- p.14: respectively. In terms of the most important evaluation
- p.14: detection accuracy of most classes of illegal
- p.14: construction objects, with lower AP values observed
- p.14: imbalanced distribution of these classes in the dataset,
- p.14: During the experiment, the majority of the models
- p.14: annotated dataset, leading to improved detection
- p.14: accuracy. Furthermore, Fig. 10 demonstrates the
<!-- AI_READING_NOTE_END -->
