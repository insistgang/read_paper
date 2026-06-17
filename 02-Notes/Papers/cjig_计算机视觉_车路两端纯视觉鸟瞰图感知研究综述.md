---
title: 微表情峰值帧定位引导的分类算法 (Apex frame spotting and recognition of micro-expression by optical flow)
authors:
  - "李博凯"
  - "吴从中"
  - "项柏杨"
  - "臧怀娟"
  - "任永生"
  - "詹曙"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.230537
pdf: [[cjig_计算机视觉_车路两端纯视觉鸟瞰图感知研究综述.pdf]]
primary_topic: J_人脸_表情_伪造_情感
topics:
  - "J_人脸_表情_伪造_情感"
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
extract_cache: .paper-cache/extracts/cjig_计算机视觉_车路两端纯视觉鸟瞰图感知研究综述.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/13 pages"
---
# 微表情峰值帧定位引导的分类算法 (Apex frame spotting and recognition of micro-expression by optical flow)

> **注意**: 本笔记文件名词干 `cjig_计算机视觉_车路两端纯视觉鸟瞰图感知研究综述` 与论文实际内容**不符**。据 PDF 提取文本, 本文真实题目为「微表情峰值帧定位引导的分类算法」(英文: Apex frame spotting and recognition of micro-expression by optical flow), 与「鸟瞰图/车路感知」无关。文件名为历史命名错误, 笔记内容以 PDF 实际内容为准。

## 基本信息
- **PDF**: [[cjig_计算机视觉_车路两端纯视觉鸟瞰图感知研究综述.pdf]]
- **primary_topic**: `J_人脸_表情_伪造_情感`
- **topics**: `J_人脸_表情_伪造_情感`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 微表情峰值帧定位引导的分类算法 / Apex frame spotting and recognition of micro-expression by optical flow |
| **作者** | 李博凯; 吴从中; 项柏杨; 臧怀娟; 任永生; 詹曙 |
| **发表时间** | 2024 (Vol.29, No.5, May 2024, pp.1447-1459) |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics) |
| **DOI** | 10.11834/jig.230537 |
| **基金** | 国家自然科学基金 (52104303); 安徽省教育厅安徽高校协同创新项目 (GXXT-2022-041) |

## 摘要

清理后的英文原摘要 (据 PDF 提取文本整理, 修复空格/连字符断裂、剔除杂入的版式与图轴数字):

> **Objective** Micro-expressions are unconscious facial actions made by people under external information and stimulation. These expressions are crucial proofs to judge people's emotions and thoughts. Micro-expressions are widely used in the fields of social security, business negotiation, and psychological counseling. This type of expression is different from the general macro-expression and demonstrates characteristics of short duration, low expression intensity, and fast change speed. Therefore, compared with macro-expressions, micro-expressions are more difficult to recognize and locate. Before the emergence of deep learning, researchers mostly used the traditional hand-crafted method, which utilizes artificially designed micro-expression extractors and complex parameter adjustment to extract features (e.g., LBP-TOP, MDMO). However, these algorithms mostly only extract shallow features, and improving their accuracy is difficult. This paper proposes a dual-branch optical flow spotting network (DFSN) based on an optical flow window. **Method** First, the size of the optical flow window is selected in accordance with the number of video frames, and three frames at both ends of the window are taken to stabilize the optical flow intensity. The Dlib library is used to detect faces, and the Farneback method is used to extract facial optical flow features; the image size is finally converted into 224×224 pixels. The dual-branch network is then used for two classifications: presence/absence of a micro-expression, and the rising/falling state of the micro-expression. The same network backbone is shared, and two branches process the features in different directions. Combining two loss functions can suppress overfitting. By sliding the window, the micro-expression intensity curve is drawn, and the highest point among multiple windows is taken as the apex frame. In the classification network, Euler motion magnification (EMM) is used to amplify facial motion (it is not used in the positioning network because it destroys some optical-flow features); the apex frame of the positioning network is taken as the center, and the five surrounding positions are selected as the input of a simple classification network. **Result** Using leave-one-subject-out cross-validation on CASME II and CASME, the lowest NMAE of 0.1017 is obtained on CASME II (9% lower than the current best spotting method), and an NMAE of 0.1378 (second-lowest) on CASME. With the spotting network's apex frame, the classification network achieved 89.79% accuracy (3 classes) on CASME II and 66.06% (4 classes) on CASME; using the dataset-annotated apex frame, it achieved 91.83% and 76.96%, respectively. **Conclusion** The proposed spotting network effectively locates the apex frame, and supplying an effective frame such as the apex frame significantly helps subsequent classification.

中文翻译:

> **目的** 微表情是人在外界信息和刺激下做出的无意识面部动作, 是判断受试人情绪和想法的重要佐证, 在社会安全、商业谈判和心理辅导等领域应用广泛。微表情不同于一般的宏表情, 具有持续时间短、表情强度低、变化速度快的特点, 因此比宏表情更难识别和定位。深度学习出现前多用手工特征 (如 LBP-TOP、MDMO), 但这类方法只能提取浅层特征, 精度难以提高。本文提出一种基于光流窗口的双分支微表情定位网络 (DFSN)。**方法** 先根据视频帧数选择光流窗口大小, 在窗口两端各取 3 帧以稳定光流强度; 用 Dlib 检测人脸、Farneback 提取面部光流, 图像统一缩放为 224×224。随后输入双分支网络进行两次分类: 判断有无微表情, 以及在有微表情前提下判断处于上升还是下降阶段; 共享主干、两分支侧重不同方向, 结合两个损失函数抑制过拟合。滑动窗口绘制微表情强度曲线, 取多个窗口中的最高点作为峰值帧。分类网络中用欧拉运动放大 (EMM) 放大面部运动 (因其会破坏部分光流特征, 故不用于定位网络); 以峰值帧为中心取周围 5 帧输入一个结构简单的分类网络。**结果** 在 CASME II 和 CASME 上用留一被试交叉验证, CASME II 上取得最低 NMAE 0.1017 (比当前最好定位方法低 9%), CASME 上 NMAE 为 0.1378 (次优); 用定位网络峰值帧分类, CASME II 上 89.79% (3 类)、CASME 上 66.06% (4 类); 若用数据集标注峰值帧, 则分别为 91.83% 与 76.96%。**结论** 所提定位网络能有效定位峰值帧, 而提供峰值帧这类有效信息能显著帮助后续分类。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 微表情是个体受到有效刺激并试图隐藏真实情绪时出现的无意识面部动作 (Ekman, 2008), 持续时间大约在 `0.04 s` 到 `0.5 s` 之间, 具有变化速度快、动作幅度小、持续时间短的特点, 是判断真实情绪的重要线索, 但未经专业训练者很难察觉和分类。
- **之前方法的问题**: 1) 传统手工特征 (如 `LBP-TOP`、`MDMO`、`STCLQP`、`Bi-WOOF`) 只能提取浅层且不稳定的特征, 难以识别面部肌肉的细微变化, 后续改进也很困难。2) 深度学习方法虽成为主流, 但微表情视频中存在大量冗余帧, 会对分类性能产生负面影响 (Liong 等, 2018)。3) 现有研究大多集中在微表情**分类**, 对微表情**定位** (尤其是峰值帧定位) 研究较少; 多数研究又只针对自己的分类方法过滤冗余信息, 缺乏通用的定位方案。
- **核心矛盾**: 如何从含大量冗余信息的微表情视频中, 自动、准确地定位到信息最丰富的峰值帧, 并以此为基础设计有效的分类方法。

## 关键贡献

1. **提出基于光流窗口的双分支微表情定位网络 (`DFSN`)**: 依照表情产生的内在逻辑 (非微表情 / 上升 / 下降三阶段) 建立并行分支网络和新的损失函数。`L1` 分支判断有无微表情, `R1` 分支在有微表情前提下判断处于上升还是下降阶段, 共享 `MobileNetV2` 主干, 利用窗口光流信息确定微表情阶段并绘制强度曲线, 通过曲线峰值定位峰值帧。
2. **设计结合 `L1` 与 `R1` 损失的新损失函数**: `loss = lossL1 + lossR1`, 二者均用交叉熵。由于一个 batch (sbatch) 内只有部分样本会进入 `R1` 分支, `lossR1` 先对通过 `R1` 的样本求平均损失再乘以 sbatch 大小 (`lossR1 = (∑lossᵢ / num) × sbatch`), 以消除 `R1` 分支样本数较少的影响、缓解数据集不平衡导致的过拟合。
3. **提出基于定位峰值帧的微表情分类网络**: 以定位网络输出的峰值帧为中心选取 5 帧, 用 `EMM` 放大面部运动后提取光流, 输入一个结构简单 (`MobileNetV2` + 一层 `ECA-Net` 通道注意力) 的分类网络, 在 `CASME`/`CASME II` 上证明准确定位对分类的关键作用。
4. **充分实验验证**: 在 `CASME II` 和 `CASME` 上用留一被试交叉验证 (`LOSO`) 评估。定位网络在 `CASME II` 上取得目前最低的 `NMAE` 值 `0.1017`; 分类网络在 `CASME II` 上用定位峰值帧取得 `89.79%`、用标注峰值帧取得 `91.83%` 的准确率。

## 方法

本文提出一个两阶段的微表情识别框架 (图1): 先用微表情定位部分 (图1(a)) 定位峰值帧, 再基于定位结果用微表情分类部分 (图1(b)) 对视频分类。

**整体框架**:
- **阶段一 (定位)**: 输入微表情视频, 经 dlib 人脸对齐、Farneback 光流计算与方向信息提取后, 输入 `DFSN` 网络, 输出微表情强度曲线, 曲线最高点对应峰值帧位置。
- **阶段二 (分类)**: 以定位到的峰值帧为中心截取 5 帧, 用 `EMM` 放大运动, 提取光流后输入分类网络, 输出微表情类别。

**关键模块与连接**:
1. **光流特征提取 (2.1.1)**:
    - 用 `dlib` 库检测人脸特征点、对齐人脸, 排除背景干扰; 用 `Farneback` 密集光流算法提取面部光流 (作者据 Zhao 等 2022 指出 Farneback 简单有效, 比 TV-L1 更快、细节更丰富)。
    - **多光流窗口机制**: 为适应不同持续时间的微表情和不同帧率, 用多个不同长度窗口检测。`200 fps` 视频 (CASME II) 用 `5/10/20` 帧 3 个窗口; `60 fps` 视频 (CASME) 用 `3/5` 帧 2 个窗口。设窗口长度为 `τ`, 起止位置为 `Vi`/`Vj` 帧; 为稳定光流, 在窗口每端各取 3 帧 (`Vi-1,Vi,Vi+1` 与 `Vj-1,Vj,Vj+1`), 将 3 个光流矩阵相加后判断 `Vi→Vj` 的微表情阶段。
    - 将光流 (2 通道) 从直角坐标转为极坐标获得方向信息, 与原光流组合成三通道, 图像统一缩放为 `224×224` 后输入网络。
2. **微表情定位网络 (`DFSN`, 2.1.2)**:
    - **骨干网络**: 沿用 `MobileNetV2` 的 Bottleneck 层与 Conv 层; `Conv 1×1` 层将通道数由 `320` 提到 `1280` 以获得更丰富特征; `BN` 用 BatchNorm2d, `Avgpool` 用 AdaptiveAvgPool2d。
    - **双分支结构**: 样本经主干提特征后, 先进 `L1` 分支判断是否存在微表情 (利用方向 + 幅度信息); 若存在再进 `R1` 分支判断上升还是下降 (主要靠方向信息, 此时幅度信息为干扰项)。两分支用各自的 `1×1` 卷积层扩大通道数、侧重不同方向。
    - **损失函数**: `loss = lossL1 + lossR1` (式1), `lossR1 = ∑ᵢⁿ lossᵢ / num × sbatch` (式2), 其中 n 为同一 sbatch 内最后一个通过 R1 的样本编号, num 为通过 R1 的样本总数。
    - **强度曲线绘制 (2.1.3)**: 设窗口长 `τ`, 当处于上升阶段且前端窗口帧强度 ≤ 后端帧强度时, 将窗口内除前端帧外所有帧强度加 `1/(τ-1)`; 下降阶段且前端强度 > 后端强度则减 `1/(τ-1)`; 无微表情阶段不处理。该法消除窗口大小差异、统一最高值、稳定曲线。取多条 (不同窗口长度) 曲线的最高点为峰值帧; 若峰值不止一帧, 取峰值的中心点。
3. **微表情分类网络 (2.2)**:
    - **峰值帧窗口**: 以定位峰值帧为中心取 5 帧。光流窗口前端选视频第 `2` 帧 (因 EMM 会极大增强第 1 帧噪声), 后端选微表情帧。
    - **欧拉运动放大 (`EMM`, 2.2.1)**: 放大倍数 `α` 越大形变与噪声越大 (Lei 等 2020), 本文取 `α=3` 平衡放大效果与图像失真; 因 EMM 会破坏部分光流, 故不用于定位网络。
    - **网络结构 (2.2.2)**: 同样用 `MobileNetV2`, 仅在 `FC` 层前加一层通道注意力 `ECA-Net` (Wang 等 2020) 增强跨通道交互、捕捉面部关键运动区域。
    - **分类策略**: 对 5 帧分别分类, 取 5 次分类中数量最多的类别作为视频类别 (多数投票)。

**训练方式 (3.1)**:
- **验证方法**: 均采用留一被试交叉验证 (`LOSO`): 设 K 个被试, 每次留 1 人作测试集、其余 K-1 人作训练集, 共 K 次, 保证测试样本纯净。
- **定位网络**: 迭代 `50` 轮, 初始学习率 `0.02`, 最小学习率 `10⁻⁴`。
- **分类网络**: 迭代 `30` 轮, 初始学习率 `0.01`, 最小学习率 `10⁻⁵`。

**与已有方法的差异**:
- **解耦定位与分类**: 先聚焦找到信息最丰富的峰值帧, 再分类; 不同于端到端分类。
- **自动定位 vs 标注峰值帧**: 探索自动定位可行性, 并与使用数据集标注峰值帧的分类结果对比。
- **针对双分支不平衡的自定义加权损失**: 不同于单一损失函数。

## 实验

**使用的数据集 (3.1)**:
- `CASME II`: `26` 名受试者, `255` 个视频样本, `200 fps`, LED 灯照明、`640×480` 像素记录, 标注起始/峰值/结束帧; 原始 7 类 (happiness 32, surprise 25, disgust 63, repression 27, sadness 7, fear 2, others 99)。
- `CASME`: `19` 人共 `193` 个微表情片段, `60 fps`, 含 A、B 两部分 (A 部分自然光 `1280×720`, B 部分 LED `640×480`), 标注起始/峰值/结束帧; 原始 8 类 (happiness 10, disgust 42, sadness 5, surprise 19, fear 2, tense 71, repression 43, contempt 1)。
- 分类实验中合并为大类: `CASME II` → 3 类 (积极 = happiness, 消极 = disgust+repression, 惊讶 = surprise); `CASME` → 4 类 (厌恶 disgust, 紧张 tense, 压抑 repression, 惊讶 surprise); 样本过少的类别合并/舍弃。定位实验在全部样本上进行。

**对比方法**:
- **定位** (表1): `LBP+differences measure` (Yan 等 2014b)、`OS-ROIs+binary search` (Liong 等 2015)、`RHOOF+differences measure` (Ma 等 2017)、`3DF-N+frequencies comparison` (Li 等 2021b)、`Optical flow+UPC` (Zhao 等 2022)。
- **分类** (表2/表3): `CASME II` 上对比 `OFF-ApexNet`、`AU-GACN`、`MER-GCN`、`TSGACN`、`MER-Supcon`、`STCP-Net`; `CASME` 上对比 `FDM`、`VGGMag`、`FHOFO`、`LTOGP`、`TSCNN-II`、`STRCN-G`、`LGCcon`。

**评价指标**:
- **定位**: 归一化平均绝对误差 `NMAE` (Li 等 2021b), `NMAE = (1/N)∑ eᵢ'`, `eᵢ' = |eᵢ|/l` (eᵢ 为定位峰值帧与正确峰值帧的帧差, l 为样本平均长度, N 为样本数), 值越小越准。
- **分类**: 准确率 (Accuracy)。

**主实验结果**:
- **定位** (表1, NMAE):
    - `CASME II`: DFSN **0.1017** (最优), 较 `Optical flow+UPC` (0.1119) 降低 0.0102、提高 9%; 较 `3DF-N+frequencies comparison` (0.1471) 降低 0.0454、提高 31%。其余对比: LBP 0.2037, OS-ROIs 0.1964, RHOOF 0.1656。
    - `CASME`: DFSN **0.1378** (次优), 仅次于 `3DF-N+frequencies comparison` 的 0.1023; 较 `RHOOF+differences measure` (0.1644) 提高 16%, 较 `OS-ROIs+binary search` (0.1824) 提高 24%。`Optical flow+UPC` 在 CASME 上无数据 (N/A)。CASME 表现较弱主因是帧率低 (60 fps) 导致可训练微表情部分更少、噪声更大、干扰光流。
- **分类** (表2/表3, 准确率):
    - `CASME II`: 用定位峰值帧 **89.79%**, 用标注峰值帧 **91.83%**。较 `STCP-Net` (91.46%) 上升 0.37%, 较 `MER-Supcon` (89.65%) 上升 2.18%; 其余对比含 OFF-ApexNet 88.28%、TSGACN 89.66%、AU-GACN 71.20%、MER-GCN 54.40%。(注: STCP-Net 91.46% 略高于本文定位峰值帧 89.79%; 文中"上升 0.37%"的口径据原文后续页表述, 应是与本文标注峰值帧 91.83% 相比。)
    - `CASME`: 用定位峰值帧 **66.06%**, 用标注峰值帧 **76.96%**。较 `LGCcon` (60.82%) 上升 16.14% (注: 文中此口径疑指与标注峰值帧 76.96% 相比), 较 `TSCNN-II` (73.88%) 上升 3.08%; 其余对比含 FDM 56.14、VGGMag 60.23、FHOFO 65.99、LTOGP 61.07、STRCN-G 59.65。
    - **混淆矩阵 (图6/图7)**: CASME II 上"消极"识别率高、"积极"偏低; CASME 上"紧张"识别率高、其他偏低。主因数据集不平衡, 网络倾向预测训练样本多的类别。

**消融实验** (均在 `CASME` 数据集上):
1. **定位网络消融 (表4, NMAE)**:
    - `光流峰值` (取光流强度峰值位置, 比较起始帧与选定帧的光流强度): `0.3529` (最差, 易受眨眼干扰——眨眼幅度比微表情更剧烈)。
    - `单分支 DFSN` (仅保留 L1 分支, FC 层直接三分类区分微表情阶段, 同用交叉熵): `0.1982` (较 DFSN 下降约 43%, 因单分支用相同高维特征难以区分上升/下降, 幅度信息成干扰项)。
    - `DFSN` (完整方法): **0.1378**。证明双分支结构与特定损失函数设计的关键性。
2. **分类网络消融 (表5, 准确率)**:
    - `分类网络 + 单分支定位峰值帧`: `53.33%`。
    - `分类网络 + DFSN 定位峰值帧`: `60.61%`。
    - `分类网络 + DFSN 定位峰值帧 + EMM` (完整方法): **66.06%**。
    - `分类网络 + 标注峰值帧`: `71.51%`。
    - `分类网络 + 标注峰值帧 + EMM`: **76.96%**。
    - 结论: 1) 峰值帧定位精度直接影响分类性能 (定位帧 vs 标注帧); 2) 峰值帧相同时, `EMM` 能稳定提升分类准确率 (DFSN 峰值帧与标注峰值帧两种情况下, EMM 均带来 5.45% 的提升)。

**泛化实验、速度/参数量/FLOPs 等**: PDF 文本未明确报告模型参数量、FLOPs 或推理速度。

## 局限

1. **对视频帧率敏感**: 定位网络在低帧率 (`60 fps` 的 CASME) 上明显下降, 低帧率下可训练微表情部分更少、噪声更大、表情强度变化更剧烈, 对定位准确度要求更高、对光流计算的噪声更敏感。
2. **分类网络鲁棒性不足**: 数据集类别不平衡时 (如 CASME II 中"消极"远多于"积极"), 网络倾向预测多数类, 少数类识别率偏低 (混淆矩阵图6、图7 与作者分析均印证)。
3. **两阶段设计的误差累积**: 分类严重依赖第一阶段定位精度。据原文, 使用定位峰值帧 vs 标注峰值帧, CASME 上准确率下降 `10.9%`、CASME II 上下降 `2.04%`, 定位误差会传递放大到分类。
4. **计算效率未知**: 论文未报告参数量、FLOPs 或推理速度, 难以评估实际部署可行性。
5. **`EMM` 的副作用**: 虽提升分类, 但会破坏部分光流信息 (故不用于定位), 放大倍数 `α` 需手动权衡, 引入也可能增加预处理时间。
6. **超参/窗口靠经验设定**: 窗口长度 (5/10/20 或 3/5)、α=3、5 帧分类窗口等多为经验设定, 文中未给系统的敏感性分析。

## 个人评论

1. **"定位引导分类"的范式**: 论文清晰论证了在微表情识别中先自动定位信息最丰富的"峰值帧"再分类是有效且符合直觉的思路, 消融实验 (定位帧 53–66% vs 标注帧 71–77%) 直接量化了定位精度对分类的决定性影响。这一范式可迁移到其他时序关键点定位任务 (如视频精彩瞬间提取、行为识别中的关键动作定位)。
2. **按任务内在逻辑设计网络**: `DFSN` 的双分支并非简单并行, 而是模拟人类判断微表情的逻辑 (先判"有无"再判"上升/下降"阶段), 并据"R1 阶段只靠方向、幅度成干扰"这一物理直觉拆分分支。这种基于领域知识的结构设计, 消融中比单分支三分类 NMAE 好约 43%。
3. **针对样本不平衡的损失设计**: `lossR1` 先对通过 R1 的样本求平均再乘 sbatch, 巧妙处理了 R1 分支仅在部分样本上激活导致的梯度/过拟合问题, 思路在多任务学习中有普适性。
4. **对"放大"技术的辩证使用**: EMM 能放大微小运动助分类, 但会破坏光流, 故只用于分类、不用于需要精确光流的定位阶段。这体现了对技术特性的务实理解。
5. **基准对比较严谨但口径需注意**: 用标准 `LOSO`、在两个主流数据集上与多种方法比较, 并给出定位/分类两组消融。但需注意: 表2 中 STCP-Net (91.46%) 实际高于本文定位峰值帧 (89.79%), 文中"上升 0.37%/16.14%"等口径多是与本文**标注峰值帧**结果相比, 读者引用时应区分"定位峰值帧"与"标注峰值帧"两栏。

### 使用建议

- **如果快速了解**: 读摘要、引言最后一段 (本文贡献)、表1/表2/表3 与结论。
- **如果复现**: 重点读第 2 节 (本文方法), 尤其 2.1 (定位) 与 2.2 (分类): 网络结构图 (图3、图5)、光流窗口机制 (图2)、强度曲线绘制规则 (2.1.3)、损失函数 (式1、式2)、`EMM` 参数 (α=3)、以及 3.1 的训练设置 (定位 50 轮/lr 0.02→1e-4, 分类 30 轮/lr 0.01→1e-5)。注意窗口长度按帧率取 5/10/20 (200fps) 或 3/5 (60fps)。
- **如果借鉴创新点**:
    - **"定位引导分类"思路**: 可用于其他视频识别任务的关键帧/关键动作定位。
    - **双分支设计**: 需区分层次化状态 (有无/程度/方向) 的任务可设计共享骨干的并行分支。
    - **损失函数设计**: 子任务样本量不平衡时可参考 `lossR1` 的加权方式。
- **如果写 `related work`**: 可将本文放在微表情识别 (定位 + 分类)、光流特征应用、关键帧/峰值帧定位、情感计算这几条线下。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页:
> - [[J_人脸_表情_伪造_情感]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉与情感计算方向中的**微表情识别**子领域 (taxonomy: `J_人脸_表情_伪造_情感`)。它聚焦两大挑战: 微表情视频中**关键信息 (峰值帧) 的自动定位**, 以及**基于该关键帧的准确分类**, 核心是一个"先定位、后分类"的两阶段框架 (定位网络 DFSN + 分类网络)。注: 本笔记文件名词干含"车路/鸟瞰图感知综述", 与论文真实内容 (微表情) 完全不符, 系历史命名错误, 内容以 PDF 为准。

## 2. 一句话总结
本文提出基于光流窗口的双分支网络 (`DFSN`) 准确定位微表情峰值帧, 再用欧拉运动放大 (`EMM`) 放大峰值帧附近运动信息, 结合一个简单的 `MobileNetV2`+`ECA-Net` 分类网络实现微表情视频分类, 在 `CASME II`/`CASME` 上验证有效。

## 3. 背景与问题
- **为什么要做**: 微表情持续约 `0.04–0.5 s`、动作幅度小、变化速度快 (个体试图隐藏真实情绪时出现, Ekman 2008), 是判断真实情绪的重要线索, 但难察觉、难分类。
- **之前方法的问题**: 1) 手工特征 (`LBP-TOP`/`MDMO`/`STCLQP`/`Bi-WOOF`) 只提取浅层、不稳定特征, 改进困难。2) 深度学习虽成主流, 但视频中冗余帧会干扰分类 (Liong 等 2018)。3) 研究多集中在分类、对峰值帧定位研究少, 且多数研究只针对自身方法过滤冗余信息, 缺乏通用定位方案。
- **核心矛盾**: 如何从冗余信息中自动、准确定位信息最丰富的峰值帧, 并据此有效分类。

## 4. 核心贡献
1. **基于光流窗口的双分支定位网络 `DFSN`**: 依表情产生逻辑 (非微表情/上升/下降三阶段) 建并行分支 (`L1` 判有无、`R1` 判上升/下降) 与新损失函数, 用窗口光流绘制强度曲线并定位峰值帧。
2. **新损失函数**: `loss = lossL1 + lossR1` (式1), 对 `R1` 分支用 `∑lossᵢ/num × sbatch` (式2) 加权, 消除 R1 样本少的影响、缓解过拟合。
3. **基于定位峰值帧的分类网络**: 以峰值帧为中心取 5 帧, 用 `EMM` (α=3) 放大运动后提光流, 输入 `MobileNetV2`+`ECA-Net` 的简单网络, 多数投票出类别。
4. **充分实验**: `LOSO` 验证, 定位网络在 `CASME II` 取最低 NMAE `0.1017`; 分类在 `CASME II` 用定位/标注峰值帧分别取 `89.79%`/`91.83%`。

## 5. 方法详解
两阶段框架 (图1): 定位 (图1a) 找峰值帧 → 分类 (图1b) 出类别。

**定位 (2.1)**:
- **光流提取 (2.1.1)**: dlib 人脸对齐 + Farneback 密集光流 (比 TV-L1 更快、细节更多, 据 Zhao 等 2022); 多窗口检测 (200fps 用 5/10/20 帧, 60fps 用 3/5 帧), 设窗口长 τ、起止 Vi/Vj, 每端各取 3 帧光流相加判阶段; 直角→极坐标得方向信息, 组成三通道、缩放 224×224 输入。
- **定位网络 DFSN (2.1.2)**: 主干为 `MobileNetV2` (Bottleneck/Conv 层), `Conv 1×1` 把通道 320→1280, 含 BatchNorm2d、AdaptiveAvgPool2d。`L1` 分支判有无微表情 (用方向+幅度), `R1` 分支判上升/下降 (主要靠方向, 幅度为干扰)。两分支各用 1×1 卷积扩通道。损失见式1/式2。
- **强度曲线 (2.1.3)**: 上升且前端强度 ≤ 后端时, 窗口内除前端帧外各帧 +`1/(τ-1)`; 下降且前端 > 后端则 -`1/(τ-1)`; 无微表情不变。取多条曲线最高点为峰值帧, 多峰时取中心点。

**分类 (2.2)**:
- **峰值帧窗口**: 以峰值帧为中心取 5 帧, 窗口前端取视频第 2 帧 (避 EMM 放大首帧噪声), 后端取微表情帧。
- **EMM (2.2.1)**: α=3 (Lei 等 2020), 平衡放大与失真; 因破坏光流故不用于定位。
- **分类网络 (2.2.2)**: `MobileNetV2` + FC 前加 `ECA-Net` 通道注意力 (Wang 等 2020); 对 5 帧分类取多数票。

**训练 (3.1)**: 全程 `LOSO`。定位 50 轮 / lr 0.02→1e-4; 分类 30 轮 / lr 0.01→1e-5。

## 6. 实验与结果
**数据集 (3.1)**:
- `CASME II`: 26 人, 255 个样本, 200fps, 640×480 LED, 标注起始/峰值/结束帧, 原始 7 类 → 合并为积极/消极/惊讶 3 类。
- `CASME`: 19 人, 193 片段, 60fps, A 部分自然光 1280×720 / B 部分 LED 640×480, 标注三帧, 原始 8 类 → 合并为厌恶/紧张/压抑/惊讶 4 类。

**对比方法**: 定位见表1 (LBP / OS-ROIs / RHOOF / 3DF-N / Optical flow+UPC); 分类见表2 (CASME II) 与表3 (CASME)。

**评价指标**: 定位用 NMAE (越小越准), 分类用准确率。

**主结果**:
- 定位 (NMAE): CASME II DFSN **0.1017** (最优, 比 Optical flow+UPC 0.1119 提高 9%, 比 3DF-N 0.1471 提高 31%); CASME DFSN **0.1378** (次优, 3DF-N 0.1023 更优; 比 RHOOF 0.1644 提高 16%, 比 OS-ROIs 0.1824 提高 24%; Optical flow+UPC 在 CASME 无数据)。CASME 较弱主因帧率低 (60fps)。
- 分类 (准确率): CASME II 定位峰值帧 **89.79%** / 标注峰值帧 **91.83%**; CASME 定位峰值帧 **66.06%** / 标注峰值帧 **76.96%**。注意表2 中 STCP-Net 91.46% 高于本文定位峰值帧 89.79%, 文中"上升 0.37%"等口径多是与本文标注峰值帧相比。混淆矩阵 (图6/图7) 显示类别不平衡导致少数类识别率低。

**消融** (CASME):
- 定位 (表4, NMAE): 光流峰值 0.3529 → 单分支 DFSN 0.1982 → DFSN **0.1378** (单分支比 DFSN 差约 43%; 光流峰值易受眨眼干扰)。
- 分类 (表5, 准确率): 单分支定位帧 53.33 → DFSN 定位帧 60.61 → DFSN 定位帧+EMM **66.06** → 标注帧 71.51 → 标注帧+EMM **76.96**。结论: 定位精度直接影响分类; 峰值帧相同时 EMM 稳定 +5.45%。

**速度/参数量/FLOPs**: PDF 未报告。

## 7. 这篇论文真正有价值的地方
1. **"定位引导分类"范式**: 消融定量证明定位精度决定分类上限 (定位帧 vs 标注帧差距明显), 可迁移到其他时序关键点定位任务。
2. **按任务内在逻辑设计网络**: 双分支模拟"先判有无、再判上升/下降"的人类逻辑, 并据"R1 只靠方向、幅度成干扰"拆分, 比单分支三分类好约 43% NMAE。
3. **针对样本不平衡的损失**: `lossR1` 加权处理 R1 分支样本少导致的梯度/过拟合, 多任务学习中可借鉴。
4. **对放大技术的辩证使用**: EMM 助分类但破坏光流, 故只用于分类、不用于定位。
5. **较系统的基准与消融**: LOSO + 两数据集 + 两组消融, 但分类提升口径需区分"定位/标注峰值帧"两栏。

## 8. 局限与问题
1. **对帧率敏感**: 低帧率 (60fps CASME) 定位明显下降, 对光流噪声敏感。
2. **分类鲁棒性不足**: 类别不平衡时倾向多数类, 少数类识别率低 (图6/图7)。
3. **两阶段误差累积**: 据原文, 定位帧 vs 标注帧, CASME 准确率降 10.9%、CASME II 降 2.04%。
4. **效率未知**: 未报告参数量/FLOPs/速度。
5. **EMM 副作用**: 破坏光流、α 需手调、增加预处理。
6. **超参靠经验**: 窗口长度、α、5 帧窗口等多为经验设定, 无系统敏感性分析。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言末段 + 表1/2/3 + 结论。
- **复现**: 第 2 节 (图2/3/5、式1/2、强度曲线规则、α=3) + 3.1 训练设置 (定位 50 轮 lr 0.02→1e-4, 分类 30 轮 lr 0.01→1e-5); 窗口长度按帧率取 5/10/20 (200fps) 或 3/5 (60fps)。
- **借鉴**: 定位引导分类思路 / 共享骨干双分支 / 样本不平衡的 lossR1 加权。
- **写 related work**: 微表情定位、微表情分类、光流特征、峰值帧定位、情感计算。

## 10. 和其他论文的关系
- 本文与在 `CASME`/`CASME II` 上发表的微表情工作构成基准对比关系, 如文中对比的 `STCP-Net`、`MER-Supcon`、`TSGACN`、`OFF-ApexNet` (CASME II) 与 `TSCNN-II`、`LGCcon`、`FHOFO`、`STRCN-G` (CASME)。
- 方法上借鉴/引用了 `Farneback` 光流 (Farnebäck 2003)、`EMM` (Wu 等 2012)、`ECA-Net` (Wang 等 2020)、`MobileNetV2` 主干。
- 提取文本未提供完整参考文献列表 (截断于第 12 页), 故不对库内其他笔记建立不确定的双链。

## 11. 关键词
微表情定位, 峰值帧, 微表情分类, 双分支网络 (DFSN), 光流, Farneback, 欧拉运动放大 (EMM), MobileNetV2, ECA-Net, 留一被试交叉验证 (LOSO), 强度曲线, 情感计算, CASME / CASME II, NMAE

## 12. 可信度说明
本精读笔记基于 PDF 提取文本的**摘要 (中英文)、引言、相关工作、方法、实验结果与分析、结论**等核心部分生成, 数字结果严格从文本摘录, 未编造。需注意:
1. 提取缓存为 12/13 页, **参考文献页 (p.13) 在主提取中截断**, 后续补读仅补到零散文献条目, 故无法对相关工作做更全面溯源。
2. 图表 (图1–7、表1–5) 的视觉细节无法从文本完全复现, 但表1–5 的数值已在正文中给出并被本笔记采用。
3. 分类提升的部分口径 (如"上升 0.37%/16.14%") 与表2/表3 的"本文 (基于定位网络峰值帧)"一栏对照存在差异, 本笔记已标注应区分"定位峰值帧"与"标注峰值帧"两栏。
总体而言, 笔记准确反映了论文的核心思想、方法框架与实验结论, 可信度较高。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 提取缓存 12/13 页 (参考文献页 p.13 在主提取中截断, 后续补读补到零散条目); 来源缓存: `.paper-cache/extracts/cjig_计算机视觉_车路两端纯视觉鸟瞰图感知研究综述.txt`; 生成日期: 2026-06-05; 本轮优化: 据提取文本重建摘要、核对全部数值、修正主题分类 (L_数据集_Benchmark → J_人脸_表情_伪造_情感) 并标注文件名串台; 模式: LLM。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-13。
- **提取情况**: 缺失页 1 页 (参考文献页), 其中提取到部分可读文献条目。已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核; `human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13 为参考文献 (References) 页, 未含正文章节。

### 缺失页关键摘录

- p.13: database and the baseline evaluation . PLoS One ， 9（1） ： #86041 (CASME II 数据集文献, Yan 等 2014a)
- p.13: base： a dataset of spontaneous micro-expressions collected from (CASME 数据集文献, Yan 等 2013)
<!-- AI_READING_NOTE_END -->
