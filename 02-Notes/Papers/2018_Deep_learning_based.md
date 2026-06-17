---
title: Deep learning based cloud detection for medium and high resolution
authors:
  - "Zhiwei Li"
  - "Huanfeng Shen"
  - "Qing Cheng"
  - "Yuhao Liu"
  - "Shucheng You"
  - "Zongyi He"
year: 2018
venue: remote sensing images of different sensors
doi: 
pdf: [[2018_Deep_learning_based.pdf]]
primary_topic: R1_遥感_高光谱_变化检测
topics:
  - "R1_遥感_高光谱_变化检测"
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2018_Deep_learning_based.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/37 pages"
---
# Deep learning based cloud detection for medium and high resolution

## 基本信息
- **PDF**: [[2018_Deep_learning_based.pdf]]
- **primary_topic**: `R1_遥感_高光谱_变化检测`
- **topics**: `R1_遥感_高光谱_变化检测`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Deep learning based cloud detection for medium and high resolution remote sensing images of different sensors |
| **作者** | Zhiwei Li; Huanfeng Shen; Qing Cheng; Yuhao Liu; Shucheng You; Zongyi He（武汉大学等） |
| **发表时间** | 2018 |
| **刊物/会议** | remote sensing images of different sensors（venue 字段未明确，正文未给出期刊名；据数据集站点为 RSE 相关工作） |
| **DOI** | 未明确 |

## 摘要

**清理后的英文原摘要（据 PDF 提取文本整理，修复空格与连字符断裂）：**

> Cloud detection is an important preprocessing step for the precise application of optical satellite imagery. In this paper, we propose a deep learning based cloud detection method named multi-scale convolutional feature fusion (MSCFF) for remote sensing images of different sensors. In the network architecture of MSCFF, the symmetric encoder-decoder module, which provides both local and global context by densifying feature maps with trainable convolutional filter banks, is utilized to extract multi-scale and high-level spatial features. The feature maps of multiple scales are then up-sampled and concatenated, and a novel multi-scale feature fusion module is designed to fuse the features of different scales for the output. The two output feature maps of the network are cloud and cloud shadow maps, which are in turn fed to binary classifiers outside the model to obtain the final cloud and cloud shadow mask. The MSCFF method was validated on hundreds of globally distributed optical satellite images, with spatial resolutions ranging from 0.5 to 50 m, including Landsat-5/7/8, Gaofen-1/2/4, Sentinel-2, Ziyuan-3, CBERS-04, Huanjing-1, and collected high-resolution images exported from Google Earth. The experimental results show that MSCFF achieves a higher accuracy than the traditional rule-based cloud detection methods and the state-of-the-art deep learning models, especially in bright surface covered areas. The effectiveness of MSCFF means that it has great promise for the practical application of cloud detection for multiple types of medium and high-resolution remote sensing images. Our established global high-resolution cloud detection validation dataset has been made available online (http://sendimage.whu.edu.cn/en/mscff/).

**中文翻译：**

> 云检测是光学卫星影像精确应用的重要预处理步骤。本文提出一种基于深度学习的云检测方法——多尺度卷积特征融合（MSCFF），面向不同传感器的遥感影像。在 MSCFF 的网络架构中，使用对称的编码器-解码器模块，通过可训练的卷积滤波器组对特征图进行致密化，从而同时提供局部与全局上下文，用于提取多尺度、高层次的空间特征。随后将多个尺度的特征图上采样并拼接，并设计了一个新颖的多尺度特征融合模块，把不同尺度的特征融合后输出。网络的两张输出特征图分别为云图与云影图，再送入模型外部的二值分类器，得到最终的云与云影掩膜。MSCFF 在数百幅全球分布的光学卫星影像上得到验证，空间分辨率范围 0.5–50 m，覆盖 Landsat-5/7/8、Gaofen-1/2/4、Sentinel-2、Ziyuan-3、CBERS-04、Huanjing-1，以及从 Google Earth 导出的高分辨率影像。实验结果表明，MSCFF 的精度高于传统规则基云检测方法和当前最先进的深度学习模型，尤其在亮地表覆盖区域优势明显。MSCFF 的有效性意味着它在多类型中高分辨率遥感影像云检测的实际应用中具有很大潜力。作者构建的全球高分辨率云检测验证数据集已在线公开（http://sendimage.whu.edu.cn/en/mscff/）。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：云和云影是光学遥感影像中不可避免的干扰，限制了影像用于地表信息提取的潜力，影响卫星数据的可用性。云检测是影像精确应用前的必要预处理步骤（Introduction，p.3）。
- **之前方法的问题**：
    1.  **通用性差**：当前多数云检测属于**规则基分类**（基于云的物理属性做多阈值判断），通常只针对某一特定类型的卫星影像。Landsat 上最知名的是 Fmask（Zhu & Woodcock, 2012）。Table 1（p.3）列出 1998–2018 年间针对 ASTR/AVHRR/MERIS/MODIS/Landsat/SPOT/CBERS/HJ-1/Gaofen 等不同传感器各自开发的方法，说明**随着卫星影像来源增多，为每种影像分别开发方法效率低下**（p.4）。
    2.  **精度局限**：传统规则基方法常出现**亮的非云目标误检（bright non-cloud object commission）和薄云漏检（thin cloud omission）**，对光谱信息有限的影像尤甚（Li et al., 2017/2018，p.4）。这类方法多只用**低层光谱和空间特征**，仍有用更高层特征提升精度的空间（p.4）。
    3.  **定标依赖**：理想输入应是大气顶（TOA）反射率而非 DN 值，以减小不同影像的辐射差异；但辐射定标并非总能精确实现，尤其对缺乏星上定标能力的传感器，云检测更困难（p.4）。
- **已有机器学习/深度学习尝试**：SPARCS（Hughes & Hayes, 2014，训练神经网络识别 Landsat 云/云影）、Yuan & Hu (2015) 的词袋+SVM、Bai et al. (2016) 与 Ishida et al. (2018) 的 SVM 方案；深度学习方面有 Mateo-García et al. (2017，Proba-V 上的简单 CNN）、Xie et al. (2017，先分割再用 CNN 标注 patch）、Zhan et al. (2017，像素级区分云雪）。**但这些深度学习方法大多只在局部区域、单一类型影像上验证**（p.5）。
- **核心矛盾**：如何设计一个**既能适配多种传感器与分辨率影像（通用性/可扩展性）**、又能**利用深层语义特征克服传统方法在亮地表和薄云下的精度瓶颈**的云检测方法。

## 关键贡献

1.  **提出 MSCFF 全卷积网络**：专用于云和云影检测，核心由**对称编码器-解码器模块**和**多尺度卷积特征融合模块**构成，前者做多尺度特征提取，后者做特征融合（p.6，p.7）。
2.  **改进对称编解码模块**：编解码思想源自 SegNet（Badrinarayanan et al., 2017），通过引入**残差单元（He et al., 2016）和空洞卷积（Yu & Koltun, 2016; Chen et al., 2018）**改进，使网络更易训练、更有效，并在不增大模型深度/复杂度的前提下扩大感受野（p.8–p.10）。
3.  **设计多尺度特征融合模块**：把编解码器中**六个尺度**的特征图上采样到相同尺寸后拼接，再经卷积融合输出，充分利用不同尺度的卷积特征以进一步提升精度（p.6，p.9 Fig.2 说明）。
4.  **端到端像素级预测**：网络是 FCN，输出与输入同高宽的逐像素图；与 Mateo-García et al. (2017)、Xie et al. (2017) 用全连接层为整个 patch 输出单一类别标签不同（p.7–p.8）。两张输出特征图（云、云影，取值 0–1）送入**模型外部的二值分类器**得到最终掩膜。
5.  **构建全球高分辨率云检测验证数据集并公开**：覆盖全球不同区域、多种传感器、多种地表覆盖，含云与云影标签，已在线公开（http://sendimage.whu.edu.cn/en/mscff/，p.2）。（据原文后续页 p.14–15，数据集分四个子集、Table 2 给出明细，共 516 幅用于性能验证；提取缓存未覆盖，待核。）
6.  **验证通用性与优越性**：在多传感器全球数据集上，精度高于传统规则基方法和最先进深度学习模型，尤其在亮地表区域（p.2，p.5）。

## 方法

- **整体框架**：方法分**模型训练**和**模型测试**两个阶段（Fig.1，p.6）。实验数据被划分为训练/测试两部分。训练阶段：先预处理影像及其云/云影标签，再通过**最小化损失函数**（在模型预测与二值标签上计算）迭代优化参数到最优。测试阶段：用预训练 MSCFF 对每个像素预测云和云影，两张输出图送入外部二值分类器做逐像素二值化，最后合并为单张云/云影掩膜（p.6–p.7）。
- **输入输出**：
    - **训练样本**：大幅多光谱影像与掩膜均裁剪成 **256×256** 的成对样本，样本间**不重叠**；因 patch 已足够多，训练阶段**未使用数据增强**（p.7）。
    - **推理输入**：同样归一化后，整幅影像切成一系列等大 patch 逐块处理，**相邻 patch 部分重叠**以避免分块边界伪影；patch 尺寸可为 256×256、512×512、1024×1024 或更大（取决于设备显存），输入通道数取决于影像可用波段（p.7）。
    - **推理输出**：两张与输入同尺寸的概率图（云、云影，值在 0–1），经外部二值化合并为最终掩膜。
- **关键模块**：
    1.  **数据预处理**：把影像值归一化到 [0,1]，方式取决于能否精确定标——**能精确定标的（如 Landsat）用辐射定标归一化到 TOA 反射率**；否则用**最大值归一化**，既统一不同源影像的值域，又保留原始光谱信息。云/云影掩膜分别生成，云或云影像素标 1、其余标 0（p.7）。
    2.  **对称编码器-解码器模块**（2.2.1，p.7–p.11）：
        - **基本卷积层**：输入 m×n×c 特征图，k 个 r×r×c 滤波器，输出 m'×n'×k。每个卷积层（除最后一层）后做**批归一化（BN）**，再接 **ReLU `f(x)=max(0,x)`**；所有卷积核 **3×3**，边界**补零**以保持输出尺寸不变（p.8）。Fig.2 把含三个卷积层 + BN + ReLU + 残差单元的结构称为 **CBRR 块**。
        - **空洞卷积层**：用于在不增加模型深度/复杂度的前提下指数级扩大感受野。**编码器最后两个 CBRR 块和解码器前两个对应 CBRR 块**的 3×3 空洞卷积，膨胀率依次设为 **2、4、4、2**（p.10）。
        - **池化层**：仅在**前三个 CBRR 块之后**各接一个 **2×2、步长 2 的最大池化**下采样（共 3 个）；之所以前三块用池化、后两块改用空洞卷积，是因为二者结合能提供更强的多尺度特征并为解码器保留更多细节（p.10）。
        - **反卷积层（解码器）**：用反卷积（转置卷积/分数步长卷积）上采样、重建特征图，恢复编码阶段的初始特征图形状（p.10–p.11）。
        - **跳跃连接**：编码器与对应解码器中**等尺寸**的特征图通过跳跃连接做**逐元素相加（element-wise summed）**，以保留更多空间细节、得到更精细的边界（p.11）。
    3.  **多尺度卷积特征融合模块**：将编解码器中**六个尺度**的（上采样后的）特征图拼接并经卷积融合，输出云与云影两张图（p.6，Fig.2 说明 p.9）。
- **数学公式/机制**：
    - **卷积层**：`Y_i = W_i * X + b_i`（`*` 为离散卷积），核 3×3，补零保尺寸（p.8）。
    - **感受野**：以核 3×3、膨胀 2 像素为例，基本卷积感受野与层深 d **线性相关** `R=(2d+1)×(2d+1)`，而空洞卷积**指数相关** `R=(2^(d+1)−1)×(2^(d+1)−1)`（Zhang et al., 2018，p.10）。
    - **残差/恒等映射**：引入残差单元（He et al., 2016）使网络更易训练（p.8）。
- **训练方式**：最小化在模型预测与二值标签上计算的损失函数迭代优化参数（p.6）。**具体损失函数形式、优化器、学习率等超参数在提取文本（前 12 页）中未给出（PDF 文本未明确，应在 p.13+）。**
- **和已有方法的差异**：
    1.  **网络类型**：MSCFF 是 FCN、输出逐像素图；Mateo-García et al. (2017) 与 Xie et al. (2017) 用全连接层为整个 patch 输出单一类别标签（p.8）。
    2.  **多尺度显式融合**：显式提取并融合六个尺度的特征（多数早期方法未系统利用多尺度信息）。
    3.  **通用性**：模型设计与数据集构建都面向**多传感器、全球范围**，而多数现有方法针对特定影像类型与区域（p.4–p.5）。

## 实验

- **使用的数据集**：自建的**全球高分辨率云检测验证数据集**，含数百幅全球分布光学卫星影像，分辨率 0.5–50 m，传感器包括 Landsat-5/7/8、Gaofen-1/2/4、Sentinel-2、Ziyuan-3、CBERS-04、Huanjing-1，及从 Google Earth 导出的高分辨率影像（摘要 + p.5）。数据集已在线公开。（据原文后续页 p.14–15：数据集由四个子集构成、Table 2 给出明细，共 **516** 幅用于性能验证，含 Landsat-8 OLI/TIRS Level-1T 96 景及配套人工云标注；提取缓存未覆盖，待核。）
- **网络结构验证（2.2.3，标题见 p.13）**：论文设了对照实验验证网络有效性，除模型结构外其余训练/测试参数保持一致。（据原文后续页摘录：**残差单元有助于提升云检测精度**；含/不含编码器-解码器对应模块的两个模型间精度差异很小；**增加滤波器数量只带来轻微精度提升，却显著增加计算开销**——故在精度与计算效率间权衡。以上来自提取缓存外的 p.13–14，待核。）
- **对比方法**：(1) 传统规则基方法（如 Fmask 等）；(2) 最先进深度学习模型。**具体被比模型名称在前 12 页提取文本中未列出（PDF 文本未明确，应在第 4 章 p.13+）。**
- **评价指标**：摘要/引言提到对"accuracy"的评估，但**具体指标名称（总体精度/F1/IoU 等）及其计算值在前 12 页提取文本中未给出（PDF 文本未明确，应在第 4 章）。**
- **主实验结果**：结论性表述为 MSCFF 精度高于传统规则基方法和最先进深度学习模型，**尤其在亮地表覆盖区域**，并能生成更精细的云/云影掩膜（摘要，p.5）。**具体精度数字在提取文本中未找到。**
- **消融/网络结构实验**：从 p.13 标题"Network architecture validation"与后续页摘录可知论文做了网络结构对照（残差单元、编解码模块、滤波器数量的影响），**但完整定量结果在提取缓存（前 12 页）外，待核。**
- **泛化实验**：用覆盖多传感器、多地表类型的全球测试集评估泛化能力，结果显示方法有效（摘要，p.5）。
- **效率信息**：前 12 页未给推理速度/参数量/FLOPs；后续页提及"滤波器数增加显著增加计算开销"的定性结论（p.14，提取缓存外，待核），但无具体数值。

## 局限

1.  **难分类型**：从传统方法的问题描述（亮地表误检、薄云漏检，p.4）可推断，**超薄卷云、与雪/冰难区分的云**仍可能是挑战；前 12 页未给针对性失败分析。
2.  **定量证据受提取限制**：完整的定量比较表、被比模型清单、评价指标数值、网络结构消融的完整结果都在第 4 章（提取缓存仅覆盖前 12 页），笔记层面尚无法逐项核实。
3.  **数据集规模/平衡性**：摘要只说"数百幅、全球分布"；据后续页 Table 2 与"516 幅"线索可部分补足，但各类别样本平衡性、像素量等细节仍待核（提取缓存外）。
4.  **计算成本权衡**：多个空洞卷积 + 六尺度融合会增加计算量；论文后续页有"增加滤波器显著增加计算开销"的定性讨论（p.14，待核），但前 12 页无效率数值对比。
5.  **流程依赖**：方法仍依赖预处理（辐射/最大值归一化）和**模型外部的二值化后处理**，性能上限可能受这些步骤影响。
## 个人评论

1.  **"通用性"贯穿始终**：从问题定义（多源数据）、方法设计（按能否定标自适应选择归一化、输入通道数随波段自适应、FCN 可处理任意尺寸）到评估（多传感器全球数据集），全程围绕"一个模型适配多传感器"这一目标。对希望减少为每类数据定制模型成本的工作很有借鉴价值。
2.  **池化与空洞卷积的分工很实用**：前三块用最大池化快速降分辨率、后两块用空洞卷积在不丢分辨率的情况下扩感受野（膨胀率 2-4-4-2 的对称设计），这是在"感受野—分辨率—计算量"三者间做权衡的一个清晰范式，值得在自有分割网络中复用。
3.  **跳跃连接用相加而非拼接**：编解码同尺度特征**逐元素相加**（区别于 U-Net 的通道拼接），再叠加一个独立的六尺度融合模块，这种"先相加保边界、再拼接做融合"的双重多尺度策略在结构上有一定新意。
4.  **数据集是真正的长期价值**：公开的全球多源云检测基准（含云影标签）降低了后续研究门槛，是这篇工作影响力的重要来源；复现/对比时应优先去其数据集站点取数据。
5.  **可改进处**：损失函数、优化器、被比模型与具体指标在前 12 页缺失，复现需补读第 3–4 章；外部二值阈值的选取策略也值得关注，它直接影响最终掩膜质量。

### 使用建议

- **如果快速了解**：读 **Abstract** 和 **1. Introduction**，即可掌握问题、核心方法与主要结论。
- **如果复现**：精读 **2. Methodology**（尤其 2.2 与 Fig.2 网络结构），并补读第 3 章（实验数据）、第 4 章（精度/效率评估）；从公开数据集站点获取训练/测试数据。注意损失函数与超参数需到 p.13+ 查证。
- **如果借鉴创新点**：
    - 六尺度上采样拼接再卷积的**多尺度特征融合**实现。
    - **池化（前三块）+ 空洞卷积（后两块，膨胀 2-4-4-2）** 的配合策略（p.10）。
    - **按能否精确定标自适应选归一化方式**的多源统一预处理思路（p.7）。
- **如果写 Related Work**：可归入"基于深度学习的遥感影像云/云影检测"或"面向遥感影像语义分割的多尺度特征融合网络"。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R1_遥感_高光谱_变化检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**遥感图像处理 × 深度学习语义分割**交叉领域，具体解决**光学卫星影像的云与云影自动检测**问题。其核心是针对不同空间分辨率（0.5–50 m）、不同传感器来源的遥感影像，提出一个**通用、高精度**的全卷积深度学习检测方法 MSCFF。适合放在"遥感影像智能解译/预处理"主题下，本库归类为 `R1_遥感_高光谱_变化检测`（遥感方向，含语义分割/掩膜生成类工作）。

## 2. 一句话总结
本文提出多尺度卷积特征融合（MSCFF）网络：用引入残差单元与空洞卷积的对称编解码器提取多尺度特征，再经一个六尺度融合模块整合不同尺度信息，输出云与云影概率图（外部二值化得掩膜），在数百幅多传感器全球影像上实现通用且高精度的云/云影检测，尤其在亮地表区域优于传统规则基方法和当时最先进的深度学习模型。

## 3. 背景与问题
- **为什么做**：云与云影不可避免地限制光学遥感影像的可用性，云检测是影像精确应用前的必要预处理（p.3）。
- **之前方法的问题**：
    1.  **通用性差**：主流是规则基阈值方法，每种多只针对一类影像；最知名为 Landsat 上的 Fmask。Table 1（p.3）列出十余种针对不同传感器各自开发的方法，随影像来源增多而低效（p.4）。
    2.  **精度局限**：规则基方法常**亮非云目标误检、薄云漏检**，且多只用低层光谱/空间特征，仍有用高层特征提升的空间（p.4）。
    3.  **定标依赖**：理想输入是 TOA 反射率，但辐射定标并非总能精确实现，缺星上定标的传感器更难（p.4）。
    4.  **已有 ML/DL 尝试**：SPARCS、词袋+SVM、Mateo-García et al.(2017)/Xie et al.(2017)/Zhan et al.(2017) 的 CNN，但**大多只在局部、单一类型影像上验证**（p.5）。
- **核心矛盾**：兼顾**多传感器/多分辨率通用性**与**深层语义特征带来的精度**。

## 4. 核心贡献
1.  **MSCFF 全卷积网络**：对称编解码模块 + 多尺度特征融合模块（p.6–p.7）。
2.  **改进编解码**：在 SegNet 式编解码上引入**残差单元 + 空洞卷积**（p.8–p.10）。
3.  **六尺度特征融合模块**：六个尺度特征上采样、拼接、卷积融合（p.6，Fig.2）。
4.  **端到端逐像素预测**：FCN 输出云/云影概率图（0–1）+ 外部二值分类器；区别于用全连接层输出整 patch 单标签的早期 DL 方法（p.7–p.8）。
5.  **公开全球多源云检测验证数据集**（含云影标签，p.2）。（据后续页 p.14–15：四子集、共 516 幅用于验证、含 96 景 Landsat-8 Level-1T；提取缓存外，待核。）
6.  **通用性与优越性验证**：多传感器全球数据集上精度优于规则基与最先进 DL，尤以亮地表突出（p.2、p.5）。

## 5. 方法详解
- **两阶段**：训练（预处理→最小化损失迭代优化参数）/ 测试（预处理→逐像素预测→外部二值化→合并掩膜）（Fig.1，p.6–p.7）。
- **输入输出**：训练样本 256×256 成对、不重叠、无数据增强（p.7）；推理整幅切等大 patch（256/512/1024 或更大）、相邻 patch 部分重叠防边界伪影，输入通道随可用波段（p.7）；输出两张同尺寸概率图。
- **预处理**：归一化到 [0,1]——能精确定标的（如 Landsat）→ TOA 反射率；否则最大值归一化（统一值域且保留原始光谱）。掩膜云/云影标 1、其余标 0（p.7）。
- **编解码模块**（p.7–p.11）：
    - 基本卷积层：3×3 核、补零保尺寸；除最后一层外每层后接 **BN + ReLU**；Fig.2 称含 3 卷积+BN+ReLU+残差单元的结构为 **CBRR 块**（p.8–p.9）。
    - 空洞卷积：编码器最后两块、解码器前两对应块的 3×3 空洞卷积膨胀率 **2、4、4、2**，指数级扩感受野而不增深度/复杂度（p.10）。
    - 池化：仅前三 CBRR 块后各接 **2×2 步长 2 最大池化**（共 3 个）下采样（p.10）。
    - 反卷积：解码器用反卷积（转置卷积）上采样重建（p.10–p.11）。
    - 跳跃连接：编解码同尺寸特征**逐元素相加**，保边界（p.11）。
- **多尺度融合模块**：六尺度特征上采样→拼接→卷积融合→输出云/云影图（p.6，Fig.2 说明 p.9）。
- **公式/机制**：卷积 `Y_i=W_i*X+b_i`（p.8）；基本卷积感受野 `R=(2d+1)×(2d+1)` 线性、空洞卷积 `R=(2^(d+1)−1)×(2^(d+1)−1)` 指数（p.10）；残差单元便于训练（p.8）。
- **训练细节缺口**：损失函数具体形式、优化器、学习率等超参数在前 12 页提取文本中未给出（应在 p.13+，PDF 文本未明确）。
- **与已有方法差异**：FCN 逐像素 vs 全连接整 patch 单标签（p.8）；显式六尺度融合；面向多传感器/全球（p.4–p.5）。

## 6. 实验与结果
- **数据集**：自建全球高分辨率云检测验证集，数百幅、0.5–50 m，含 Landsat-5/7/8、Gaofen-1/2/4、Sentinel-2、Ziyuan-3、CBERS-04、Huanjing-1、Google Earth 导出影像（摘要、p.5），已公开。（据后续页 p.14–15：四子集、Table 2 明细、共 516 幅验证；提取缓存外，待核。）
- **网络结构验证（2.2.3，p.13 起）**：做了结构对照。据后续页摘录：**残差单元提升精度**；含/不含编解码对应模块两模型精度差异很小；**增滤波器数仅轻微提升精度却显著增计算开销**（p.13–14，提取缓存外，待核）。
- **对比方法**：传统规则基（Fmask 等）+ 最先进 DL 模型；**具体被比模型名称在前 12 页未列出（PDF 文本未明确，应在第 4 章）。**
- **评价指标**：摘要只提"accuracy"；**具体指标名与数值在前 12 页未给（PDF 文本未明确，应在第 4 章）。**
- **主结果**：MSCFF 精度高于传统规则基与最先进 DL，**尤以亮地表区域**，掩膜更精细（摘要、p.5）；**具体数字未在提取文本中找到。**
- **泛化**：多传感器/多地表全球测试集评估，结果有效（摘要、p.5）。
- **效率**：前 12 页无速度/参数量/FLOPs；后续页有"增滤波器显著增计算开销"定性结论（p.14，待核），无具体数值。

## 7. 这篇论文真正有价值的地方
1.  **"通用性"全链路设计**：问题（多源）→方法（自适应归一化、波段自适应、FCN）→评估（多传感器全球集）一以贯之，对降低逐类定制模型成本有启发。
2.  **多尺度处理范式**：编码器提取多尺度→跳跃连接（相加）保细节→六尺度融合模块整合，适合云这种形态/尺度多变的目标；空洞卷积在深层保分辨率是关键技巧。
3.  **池化+空洞卷积的工程权衡**：前三块池化、后两块空洞（2-4-4-2），在感受野、分辨率、计算量间取得平衡，可直接迁移到其他分割网络。
4.  **公开数据集**：全球多源云/云影基准是长期价值所在，降低社区门槛。

## 8. 局限与问题
1.  **难分类型**：超薄卷云、与雪/冰难区分的云仍可能是挑战；前 12 页无针对性失败分析。
2.  **定量证据受提取限制**：对比表、被比模型清单、指标数值、结构消融完整结果在第 4 章（提取缓存仅前 12 页），暂无法逐项核实。
3.  **数据集规模/平衡性**：摘要仅"数百幅"；后续页"516 幅 + Table 2"可部分补足，但平衡性等细节待核（提取缓存外）。
4.  **计算成本**：多空洞卷积+六尺度融合增计算；后续页有定性讨论（p.14，待核），但前 12 页无效率数值对比。
5.  **流程依赖**：依赖预处理与外部二值化后处理，性能上限受其影响。

## 9. 我该怎么使用这篇论文
- **快速了解**：读 Abstract + Introduction。
- **复现**：精读第 2 章与 Fig.2；务必补读第 3 章（数据）、第 4 章（指标/对比/效率）以及损失函数、超参数（p.13+）；从公开数据集站点取数据。
- **借鉴创新点**：六尺度融合实现；池化+空洞卷积（2-4-4-2）配合（p.10）；自适应归一化的多源统一预处理（p.7）。
- **写 Related Work**：归入"基于深度学习的遥感影像云/云影检测"或"遥感语义分割的多尺度特征融合网络"。

## 10. 和其他论文的关系
- **语义分割骨架**：FCN（Shelhamer et al., 2017）、SegNet（Badrinarayanan et al., 2017，编解码思想直接来源）、U-Net（同期编解码+跳跃连接代表，本文跳跃连接用相加而非拼接）。
- **基础组件来源**：残差网络（He et al., 2016）、空洞卷积（Yu & Koltun, 2016; Chen et al., 2018 DeepLab 系列）、BN（Ioffe & Szegedy, 2015）。
- **传统/规则基云检测对照**：Fmask（Zhu & Woodcock, 2012; Zhu et al., 2015）及其改进（Qiu et al., 2017 用 DEM；Frantz et al., 2018 云位移指数）、UDTCDA（Sun et al., 2016）、Zhai et al. (2018) 多/高光谱统一方法。
- **早期 DL 云检测对照**：SPARCS（Hughes & Hayes, 2014）、Mateo-García et al. (2017，Proba-V CNN）、Xie et al. (2017，分割+CNN）、Zhan et al. (2017，云雪区分）。
（以上均为论文正文显式引用的工作；本库内是否有对应笔记需另行检索，此处不臆造双链。）

## 11. 关键词
云检测, 云影, 卷积神经网络, 多尺度, 卷积特征融合, MSCFF, 全卷积网络, 编码器-解码器, 空洞卷积, 残差单元, 跳跃连接, 遥感影像, 语义分割, Landsat, Sentinel-2, Gaofen

## 12. 可信度说明
本笔记**主要基于 PDF 提取文本的前 12 页**（提取缓存上限 25000 字符 / 12 of 37 页），覆盖标题、作者、摘要、引言（含 Table 1 方法对照）与第 2 章方法论的大部分内容，故**论文定位、核心思想、背景问题、方法框架与细节（编解码结构、空洞卷积膨胀率 2-4-4-2、池化布置、跳跃连接相加、感受野公式、预处理策略）具有较高可信度**。
受提取截断影响，以下信息**前 12 页内无法确认**，已在正文用"（据原文后续页…提取缓存未覆盖，待核）"标注，来源为本笔记"全文补读记录"中保存的 p.13–16 摘录：
- 第 4 章实验：完整定量结果表、被比模型清单、评价指标名称与数值、效率数值。
- 第 3 章实验数据细节（Table 2、四子集、516 幅、96 景 Landsat-8 Level-1T 等为后续页线索，非前 12 页提取所得）。
- 第 5 章应用扩展与讨论、第 6 章结论。
- 损失函数具体形式、优化器、训练超参数。
总体而言，方法部分准确可靠，实验部分以定性结论 + 后续页线索为主、具体数值待核。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/2018_Deep_learning_based.txt` (前 12/37 页, 25000 字符上限; 原 AI 主体 12/37 + 全文补读 13-37 摘录); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro); 本轮: 据提取文本重写，分类由 T_通用_NLP_其他 修正为 R1_遥感_高光谱_变化检测。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-37; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-37。
- **提取情况**: 缺失页 25 页, 其中 25 页提取到可读文本。缺失页包含正文/附录内容, 其中约 5 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: 2.2.3 Network architecture validation
- p.13: In order to validate the effectiveness of the network, we trained and tested the performance
- p.14: 14 Except for the changes in the model structure, all the other parameter settings of MSCFF and
- p.14: In addition to the model structure, th e number of filters is a key factor affecting the model
- p.14: 3. Experiment al data
- p.14: The experiment al datasets consisted of multiple types of optical satellite remote sen sing
- p.14: Landsat -8 Operational Land Imager/ Thermal Infrared Sensor (OLI/TIRS ) (30 m), Gaofen -1
- p.14: Panchromatic and MultiSpectral Sensor (PMS ), Ziyuan -3 multispectral ( MUX ), Sentinel -2A
- p.14: Multispectral Instrument (MSI), CBERS -04 P10, Landsat -5 Thematic Mapper ( TM), and
- p.15: Name Source Resolution Total images Image size
- p.15: 96 Landsat -8 OLI/TIRS terrain -corrected (Level -1T) scenes with associated manual cloud
- p.16: In the procedure of delineating the cloud mask for high-resolution image ry, we fir st stretch ed

### 缺失页关键摘录

- p.13: Fig. 3. Accuracy curves over a validation subset of our established high -resolution dataset for MSCFF, MSCFF
- p.13: established high-resolution dataset , which is introduced in the following section . We compared
- p.14: the compared models were the same in the training and test ing stage s. The experiment al results
- p.14: the residual units in MSCFF can help to impro ve the cloud detection accuracy .
- p.14: encoder and the corresponding decoder module s. The experiment al resul ts indicate that there
- p.14: are only slight accuracy differences between the two models . Increasing the number of filters
- p.14: can only bring a slight improvement in accuracy to MSCFF , but it results in a signif icant
- p.14: model accuracy and computation al efficiency.
- p.14: The experiment al datasets consisted of multiple types of optical satellite remote sen sing
- p.14: Google Earth (Google Inc.). The details of the four datasets are given in Table 2. A total of 516
- p.14: were used for the model performance validation by visual evaluation , i.e., Gaofen -1/2/4
- p.14: the first time that such large and diverse dataset s have been used for the validatio n of a newly
<!-- AI_READING_NOTE_END -->
