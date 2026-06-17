---
title: Xu K Liu X P Wang H Y Wan J W and Guo Y L. 2024. Infraredvisible image object detection algorithm using feature dynamic
authors:
  - "许可"
  - "刘心溥"
  - "汪汉云"
  - "万建伟"
  - "郭裕兰"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.230495
pdf: [[cjig_图像识别_红外与可见光图像特征动态选择的目标检测网络.pdf]]
primary_topic: C3_目标检测_红外_可见光融合
topics:
  - "C3_目标检测_红外_可见光融合"
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
extract_cache: .paper-cache/extracts/cjig_图像识别_红外与可见光图像特征动态选择的目标检测网络.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/14 pages"
---
# Xu K Liu X P Wang H Y Wan J W and Guo Y L. 2024. Infraredvisible image object detection algorithm using feature dynamic

## 基本信息
- **PDF**: [[cjig_图像识别_红外与可见光图像特征动态选择的目标检测网络.pdf]]
- **primary_topic**: `C3_目标检测_红外_可见光融合`
- **topics**: `C3_目标检测_红外_可见光融合`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 红外与可见光图像特征动态选择的目标检测网络 (Infrared-visible image object detection algorithm using feature dynamic selection) |
| **作者** | 许可; 刘心溥(通信); 汪汉云; 万建伟; 郭裕兰 |
| **单位** | 国防科技大学电子科学学院; 信息工程大学地理空间信息学院 |
| **发表时间** | 2024 (第29卷第8期, pp.2350-2363) |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics) |
| **DOI** | 10.11834/jig.230495 |

## 摘要

清理后的英文原摘要(据 PDF 提取文本修复空格、连字符断裂, 剔除杂入的页码/编号):

> **Objective** In recent years, considerable attention has been given to the object detection algorithm that utilizes the fusion of visible and infrared dual-modal images. This algorithm serves as an effective approach for addressing object detection tasks in complex scenes. The process of object detection algorithms can be roughly divided into three stages. The first stage is feature extraction, which aims to extract geometric features from the input data. Next, the extracted features are fed into the neck network for multi-scale feature fusion. Finally, the fused features are input into the detection network to output object detection results. However, the feature fusion process of existing dual-modal detection algorithms faces two major issues. First, the feature fusion methods employed are relatively simple, which involves the addition or parallel operation of individual feature elements, yielding unsatisfactory fusion effects. Second, the algorithm structure solely focuses on the feature fusion process, which neglects the crucial feature selection process. **Method** We introduce a visible and infrared image fusion object detection algorithm that employs dynamic feature selection. We propose enhancements to the conventional YOLOv5 detector, selecting CSPDarkNet53 as the backbone with an identical structure for the visible and infrared image branches. The algorithm incorporates two innovative modules: a dynamic fusion layer (embedded in the backbone, using a Transformer structure for multiple feature fusions in multi-source feature maps) and a dynamic selection layer (in the neck network, using three attention mechanisms — scale, space, and channel, implemented with SENet and deformable convolutions — to improve multi-scale feature maps and screen useful features). The loss function is the combined sum of bounding box regression loss (GIoU), classification loss (cross entropy), and confidence loss (squared error). **Result** We validate our algorithm on three public datasets: FLIR, LLVIP (visible-infrared paired dataset for low-light vision), and VEDAI (vehicle detection in aerial imagery). Compared with the baseline that adds features individually, our algorithm achieves improvements of 1.3%, 0.6%, and 3.9% in mAP50, 4.6%, 2.6%, and 7.5% in mAP75, and 3.2%, 2.1%, and 3.1% in mAP on the respective datasets. Ablation experiments on the two innovative modules confirm their effectiveness. **Conclusion** The proposed algorithm effectively integrates feature information from visible and infrared modalities and enhances detection performance. However, it has slightly increased computational complexity and requires pre-registration of the input images, which limits some application scenarios; lightweight fusion modules and processing of unregistered dual-light images are future work.

中文翻译(综合 PDF 中的中文摘要原文):

> **目的** 基于可见光和红外双模态图像融合的目标检测算法是解决复杂场景下目标检测任务的有效手段。然而现有双光检测算法中的特征融合过程存在两大问题: 一是特征融合方式较为简单, 逐特征元素相加或并联操作导致融合效果不佳; 二是算法结构中仅有特征融合过程, 缺少特征选择过程, 导致有用特征无法得到高效利用。为此提出一种基于动态特征选择的可见光红外图像融合目标检测算法。**方法** 本文算法包含动态融合层和动态选择层两个创新模块: 动态融合层嵌入骨干网络, 利用 Transformer 结构多次对多源图像特征图进行融合以丰富特征表达; 动态选择层嵌入颈部网络, 利用 3 种注意力机制(尺度、空间、通道, 由 SENet 与可变形卷积实现)对多尺度特征图进行特征增强以筛选有用特征。**结果** 在 FLIR、LLVIP、VEDAI 3 个公开数据集上验证, 相比基线模型, mAP50 分别提升 1.3%、0.6%、3.9%; mAP75 分别提升 4.6%、2.6%、7.5%; mAP 分别提升 3.2%、2.1%、3.1%。消融实验验证了所提算法的有效性。**结论** 所提算法可有效融合两种模态特征信息, 提升检测性能; 但计算复杂度略有增加且依赖输入图像预配准, 未来将研究轻量融合模块与处理未配准双光图像的算法。
>
> 关键词: 红外图像; 目标检测; 注意力机制; 特征融合; 深度神经网络

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 实际二维目标检测场景往往复杂(雨、雾、遮挡、光照不良、低分辨率)。仅用可见光相机在低光照、强光干扰下检测性能差; 红外图像在低光照下成像优异, 但易受热源干扰出现热噪声(红外"鬼影", 易造成虚警), 且纹理细节不足。两种模态互补(可见光纹理利于分类定位, 红外利于暗光成像), 融合双光是提升检测准确性、可靠性、稳健性的有效途径(图1 给出四种典型对比)。
- **之前方法的问题**: 现有双光检测算法的特征融合过程存在两大问题:
    1. **融合方式简单**: 逐特征元素相加(Addition)或并联(Concatenation), 且通常仅在颈部网络融合特征, 导致融合不充分、效果不佳。
    2. **缺乏选择过程**: 算法结构中只有融合没有选择, 导致有用特征无法被高效利用。
- **为何用 Transformer**: 大部分多源融合机制(He 2016、Ren 2017、Li 2018、Zhang 2019/2021、邱德粉 2023 等)基于 CNN, 但 CNN 卷积感受野非全局、特征交互在局部完成, 不利于多源特征充分融合。Transformer(Vaswani 2017)自注意力具有全局感受野, 能建模特征长距离依赖与相关性强弱, 更适合双光融合任务(Fu 等 2023 已将 Swin-Transformer 引入双光检测)。
- **核心矛盾**: 既要通过深层、交互式融合充分利用两种模态互补信息, 又要在融合后智能筛选对检测最有用的特征, 避免噪声和冗余干扰。

## 关键贡献

1.  **提出基于动态特征选择的双模态检测算法框架**: 将多源特征图按"先融合后选择"的范式进行特征增强, 有效利用双光信息, 提升检测性能。
2.  **设计了动态融合层(DyFu)与动态选择层(DySe)两个模块**: DyFu 嵌入骨干网络, 利用 Transformer 机制多次对多源特征图融合, 丰富特征表达("动态"意为不断更新双光图像特征矩阵); DySe 嵌入颈部网络, 利用 3 种注意力机制(尺度、空间、通道)对多尺度特征图增强以筛选有用特征。
3.  **在 3 个公开数据集上验证有效性**: 在 FLIR、LLVIP、VEDAI 上, 相比基线模型(逐元素相加), mAP50 分别提升 1.3%、0.6%、3.9%; mAP75 分别提升 4.6%、2.6%、7.5%; mAP 分别提升 3.2%、2.1%、3.1%(论文原文贡献中强调 mAP75, 称"性能达到领域领先水平")。并设计消融实验与注意力权重可视化验证模块价值。

## 方法

**整体框架**(图2, p.2353):
基于 YOLOv5(you only look once v5)检测器改进, 由骨干网络、颈部网络、检测头三部分组成。骨干选用 **CSPDarkNet53**, 可见光与红外两条支路结构相同。在两条支路中间嵌入 **3 个动态融合层(DyFu)**, 对两种图像的特征图进行交互式融合更新; 后 3 层的特征图分别相加为融合特征图 P1、P2、P3 送入颈部网络。颈部采用带 FPN(Lin 2017)的 PAN(Liu 2018)结构生成多尺度特征图 FU1、FU2、FU3, 再输入 DySe 生成增强特征图 F'U1、F'U2、F'U3, 最后送入 YOLOv5 检测头输出结果。整体流程由公式 (1)(2)(3) 概括。

**输入输出**:
- 输入: 已预先完成配准的可见光图像和红外图像。
- 输出: 目标的边界框、类别、置信度。

**关键模块**:
1.  **动态融合层(DyFu)** (图3, p.2354):
    - **目的**: 在骨干网络多次对可见光和红外特征图融合, 丰富特征表达。
    - **机制**(受 CFT, Fang 等 2022 启发):
        - 将 `F_RGB` 与 `F_IR` 分别展平后并联拼接得到 `I_FU`(公式4)。
        - 经 3 个独立 MLP 生成 Q、K、V 矩阵, 输入多头注意力(MHA), 计算交互特征向量 `I_mid = MHA(Q,K,V) = αV = softmax(QKᵀ/√d_k)·V`(公式5-6)。
        - **关键点**: 先拼接后计算注意力权重, 使权重矩阵 α(图4, p.2355)同时包含 4 个相关运算区域: 可见光自相关、可见光/红外互相关、红外/可见光互相关、红外自相关, 从而量化两模态间相关性。
        - `I_mid` 经归一化、MLP 后与前面变量构成残差连接, 再按模态分离: `F'_RGB, F'_IR = fSplit(I_mid + I_FU + MLP(BN(I_mid)))`(公式7)。
        - **重要细节**: 模型中多头注意力模块**重复了 8 次**(p.2355)。
2.  **动态选择层(DySe)** (图5, p.2356):
    - **目的**: 在颈部网络利用注意力对多尺度特征图增强以筛选有用特征。
    - **机制**:
        - FU1、FU2、FU3 经 MLP 降维统一为 128 通道; FU2、FU3 双线性插值上采样后与 FU1 并联, 得多尺度聚合特征 `F_U`(维度 3×80×80×128, 公式8; 其中 3 代表 3 个尺度, 80×80 为特征图尺寸, 128 为通道数)。
        - 依次施加**尺度、空间、通道注意力**: `F'_U = Cha(Spa(Sca(F_U)))`(公式9)。
        - 按尺度维度切片解耦, 再下采样得到 `F'_U1`, `F'_U2`, `F'_U3`(公式10)。
    - **三种注意力实现**:
        - **尺度注意力**与**通道注意力**: 采用改进的 **SENet**(Hu 2018)结构(公式11)。将 (N,C) 特征用全局平均池化压缩到通道描述符(N 可代表多个特征维度), 经瓶颈 MLP 学习注意力权重, 再与原特征点积(哈达玛积 ⊙)加权: `F_CHA = Cha(F) = F⊙FC(∑F(i,j)/N)`。
        - **空间注意力**: 采用**可变形卷积(DCN)**(Zhu 2019)。DCN 根据图像特征学习一组卷积偏移量作用于可变形卷积核, 动态提取卷积核周围局部区域特征, 起到像素空间注意力效果。

**损失函数**(第4节, p.2356): 整体损失由三部分组成, 与 CFT(Fang 2022)保持一致: 边界框回归损失 L_box 采用 GIoU; 分类损失 L_cls 采用交叉熵; 置信度损失 L_conf 采用均方误差。

**训练设置**(第5.1节, p.2356):
- 预训练: 在 COCO(Lin 2014)上的 YOLOv5 预训练模型初始化。**VEDAI 用 YOLOv5s, FLIR 与 LLVIP 用 YOLOv5l**。
- 优化器: SGD, 动量 0.937, 衰减率 0.0005, 初始学习率 0.01。
- batchsize=16; LLVIP 训练 100 轮, FLIR 与 VEDAI 训练 300 轮。
- 所有模型设 3 个 DyFu 层和 6 个 DySe 层; 采用马赛克增强与标签平滑等正则化。

**与已有方法的差异**:
- 与**基线模型(逐元素相加)**相比: DyFu 进行更深入、交互式的特征融合, 且 DySe 进行特征选择。
- 与 **CFT、YOLOFusion** 等其他融合方法相比: 不仅改进融合方式, 还在双光检测中引入独立的动态特征选择模块(DySe), 形成"融合+选择"的双重增强范式。

## 实验

- **数据集**(表1, p.2356):
    - **FLIR**(Saga 2022): 偏自动驾驶, 场景多样, 3 类{person, car, bicycle}, 4129 训练/1013 测试。
    - **LLVIP**(Jia 2021): 行人检测, 仅 1 类{person}, 夜晚样本较多, 体量较大, 12025 训练/3463 测试。
    - **VEDAI**(Razakarivony & Jurie 2016): 无人机俯瞰视角车辆检测, 目标较小, 9 类{car, truck, pickup, tractor, camping car, boat, plane, van, other}, 1089 训练/121 测试。
    - 三个数据集的可见光与红外图像均已预先完成配准。
- **评价指标**: mAP50, mAP75, mAP。
- **对比方法**(表2, p.2357): 单模态 YOLOv5(RGB / IR)、前融合(双光初始图像通道拼接)、后融合(检测结果取并集后 NMS)、基线模型(特征图逐元素相加)、YOLOFusion(Fang & Wang 2022)、CFT(Fang 2022)。表中结果均为作者实际复现。
- **主实验结果**(表2):
    - 本文算法(DyFu+DySe)在三个数据集上均优于所有对比方法, mAP75 提升最显著(FLIR ↑4.6%, LLVIP ↑2.6%, VEDAI ↑7.5%; mAP 分别 ↑3.2%、↑2.1%、↑3.1%; mAP50 分别 ↑1.3%、↑0.6%、↑3.9%, 均相对基线)。关键数值: FLIR ours mAP50/75/mAP = 77.5/36.5/40.6; LLVIP = 97.4/74.6/65.0; VEDAI = 80.7/67.6/51.7。
    - **四点实验规律**: (1)低光照场景较多的数据集上, 红外单模态性能远超可见光单模态(FLIR、LLVIP 上红外约高 10%), 甚至接近融合基线; (2)有些融合方法性能甚至低于红外单模态(如 FLIR 上红外单模态超过基线与 CFT), 但本文算法均优于单模态, 说明其融合有效; (3)相比 mAP50, 本文在 mAP75/mAP 提升更明显, 即检测率相近时定位精度更高, 归功于 DySe 中的可变形卷积对物体边界的更准确提取; (4)类别越多的数据集提升越多(VEDAI 9 类提升最明显)。
    - P-R 曲线与混淆矩阵对比见图6(FLIR)、图7(VEDAI)。
- **可视化检测结果**(图8-10, p.2358-2361): 相比 CFT, 本文算法虚警率与漏检率更低, 能检出数据集标注中漏标的物体, 定位更精准(如 FLIR 场景中 CFT 误检舰船/快艇为小汽车、漏检边缘行人; LLVIP 中本文克服强光反射准确识别漏标行人; VEDAI 小目标中 CFT 误识皮卡为小汽车、漏检黑色小汽车)。
- **消融实验**(表3, p.2361): 每个数据集 4 个对照组(DyFu/DySe 添加与否的 4 种组合)。三个数据集上完整模型(DyFu+DySe)均最优, 单独添加任一模块也均有提升。注意: 表3 中 VEDAI 完整模型 mAP50 标为 80.4(↑3.6), 与表2/摘要的 ↑3.9 存在论文内部小差异(据原文如实记录)。
- **效率信息**(表4, p.2361, FLIR 数据集): 参数量 基线 73.72M / CFT 206.03M / 本文 216.16M; 计算量 190.14 / 224.40 / 236.95 GFlop/s; 帧速率 15.9 / 7.7 / 7.1 帧/s。即相比 CFT 参数与计算量小幅增加, 换来较大性能提升; 但相比基线帧率明显下降。
- **注意力权重可视化**(图11, p.2361): 随 DyFu 层数加深, 骨干网络高关注区由背景逐渐转向真实目标, 并能识别红外"鬼影"区域并逐渐给予较低关注度以防虚警。

## 局限

1.  **计算成本增加**: Transformer + 额外注意力使参数量、计算量增加, 帧率明显下降(基线 15.9 → 本文 7.1 帧/s, 表4)。作者在结论中明确将"轻量融合模块"列为未来工作, 这限制其在实时/边缘设备上的应用。
2.  **依赖预配准输入**: 算法要求输入双光图像已预先配准。作者在结论中承认处理未配准双光图像是未来研究方向; 实际应用中实时配准是挑战。
3.  **数据集场景偏向**: 实验集中在自动驾驶(FLIR)、低光行人(LLVIP)、航拍车辆(VEDAI)三类, 其他通用场景(室内、复杂工业)的泛化能力 PDF 文本未明确验证。
4.  **模块数量固定**: 固定使用 3 个 DyFu 层与 6 个 DySe 层, PDF 文本未给出对模块数量/位置的敏感性消融, 可能存在优化空间。

## 个人评论

1.  **"先融合后选择"的范式思想**: 论文把"融合"与"选择"明确拆成两个独立且互补的步骤(DyFu 负责深度交互融合, DySe 负责增强筛选), 而不是只改进单一融合模块。这种分阶段、有侧重的特征处理思路对多模态任务以及其他需要精细特征处理的场景(医学多模态、小目标检测)有启发。
2.  **Transformer 跨模态融合的具体设计**: DyFu 先拼接双模态特征再算联合注意力, 使权重矩阵同时蕴含模态内自相关与模态间互相关四个区域, 比"分别提特征再拼接"更深入。MHA 重复 8 次也提示其融合是反复迭代的, 这是计算开销大的直接来源。
3.  **可变形卷积(DCN)作为空间注意力**: 将 DCN 用于空间注意力使感受野随图像内容动态调整, 论文将 mAP75 的显著提升归因于此(定位精度对 IoU 阈值更敏感)。提示在需要精确空间定位的任务中可考虑用 DCN 替代/增强传统空间注意力。
4.  **实验诚实度**: 论文如实给出了帧率从 15.9 降到 7.1 的代价, 并主动把轻量化与未配准处理列为未来工作; 同时表3 与表2 在 VEDAI mAP50 上的 3.6/3.9 小差异未被掩盖, 整体可复现性较好。
5.  **可改进处**: 缺少对 DyFu/DySe 层数与位置的消融, 也未给出不同 backbone(YOLOv5s vs l 混用)对结论的影响分析, 这两点是后续工作可补强的地方。

### 使用建议

- **如果快速了解**: 读摘要、引言(第0节)、结论(第6节)与图2 整体框架图。
- **如果复现**: 精读方法(第1-4节), 重点公式 (4)-(11)、图3/图5; 实验设置(第5.1节)注意 VEDAI 用 YOLOv5s 而 FLIR/LLVIP 用 YOLOv5l、batchsize=16、LLVIP 100 轮 / FLIR&VEDAI 300 轮、马赛克增强+标签平滑、MHA 重复 8 次。
- **如果借鉴创新点**: 改进融合学 DyFu 的跨模态联合注意力(公式4-7); 改进选择/增强学 DySe 的多尺度注意力(公式8-11), 尤其 SENet 用于尺度/通道、DCN 用于空间; 提升定位精度借鉴 DCN 增强边界敏感性。
- **如果写 related work**: 可归入"基于注意力机制的多模态(红外+可见光)融合检测"或"Transformer 在视觉检测中的应用", 与 CFT、YOLOFusion、Fu 等(Swin-Transformer 双光)对比讨论。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页:
> - [[C3_目标检测_红外_可见光融合]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**计算机视觉**领域的**红外与可见光双模态目标检测**方向, 对应主题"C3_目标检测_红外_可见光融合"。它旨在解决复杂场景(低光照、强光干扰、热噪声"鬼影")下, 利用红外与可见光图像互补信息进行鲁棒目标检测的问题。论文通过改进 YOLOv5 的特征融合与选择机制, 提升双模态检测精度, 适合对多源信息融合、注意力机制、Transformer 跨模态交互以及改进经典检测器感兴趣的研究者。

## 2. 一句话总结
本文提出一种基于动态特征选择的红外与可见光图像融合目标检测算法, 在 YOLOv5/CSPDarkNet53 骨干中嵌入 3 个基于 Transformer 的动态融合层(DyFu), 在颈部 PAN 后嵌入 6 个基于尺度/空间/通道三注意力(SENet+DCN)的动态选择层(DySe), 实现"先融合后选择"的特征增强, 在 FLIR/LLVIP/VEDAI 上 mAP75 相比基线分别提升 4.6%/2.6%/7.5%。

## 3. 背景与问题
- **为什么要做**: 雨、雾、遮挡、光照不良、低分辨率等复杂场景下, 仅用可见光相机难以高精度检测; 红外在暗光下成像优异但易受热源干扰出现"鬼影"造成虚警、纹理不足。可见光(纹理/细节, 利于分类定位)与红外(暗光成像)互补, 融合双光是提升准确性、可靠性、稳健性的有效途径(图1)。
- **之前方法的问题**:
    1. **融合方式简单**: 逐元素相加或并联, 且常仅在颈部融合, 导致融合不充分、效果不佳。
    2. **缺乏选择过程**: 只有融合没有选择, 有用特征无法高效利用。
    3. **CNN 局限**: 既有多源融合多基于 CNN, 但 CNN 感受野非全局、交互在局部完成, 不利于多源特征充分融合; Transformer 自注意力全局感受野更适合双光融合。
- **核心矛盾**: 既要深层交互式融合充分利用互补信息, 又要在融合后筛选最有用特征, 避免噪声/冗余干扰。

## 4. 核心贡献
1.  **基于动态特征选择的双模态检测框架**: 按"先融合后选择"范式增强多源特征, 有效利用双光信息。
2.  **动态融合层 DyFu**: 嵌入骨干, 基于 Transformer 多次对多源特征图融合("动态"指不断更新双光特征矩阵)。
3.  **动态选择层 DySe**: 嵌入颈部, 用尺度/空间/通道三种注意力增强多尺度特征以筛选有用特征。
4.  **三数据集验证**: FLIR/LLVIP/VEDAI 上相比基线 mAP50 ↑1.3%/0.6%/3.9%、mAP75 ↑4.6%/2.6%/7.5%、mAP ↑3.2%/2.1%/3.1%, 并以消融与注意力可视化佐证。

## 5. 方法详解
**整体框架**(图2, p.2353): 基于 YOLOv5 改进(骨干+颈部+检测头)。骨干为 CSPDarkNet53, 可见光/红外两支路结构相同, 中间嵌入 3 个 DyFu 更新特征(公式1); 后 3 层特征图相加为 P1/P2/P3 送入颈部。颈部 FPN+PAN 生成 FU1/FU2/FU3(公式2), 经 DySe 得 F'U1/F'U2/F'U3(公式3)送入检测头。

**输入输出**: 输入预配准的可见光与红外图像; 输出边界框、类别、置信度。

**关键模块**:
1.  **DyFu**(图3, 受 CFT/Fang 2022 启发):
    - `I_FU = Concat(flatten(F_RGB), flatten(F_IR))`(公式4)。
    - 3 个 MLP 生成 Q/K/V → 多头注意力 `I_mid = MHA(Q,K,V) = αV = softmax(QKᵀ/√d_k)V`(公式5-6); 先拼接后算注意力, 权重矩阵 α(图4)含 4 区域(可见光自相关、可见光/红外互相关、红外/可见光互相关、红外自相关)。
    - 残差+归一化+MLP 后按模态分离: `F'_RGB, F'_IR = Split(I_mid + I_FU + MLP(BN(I_mid)))`(公式7)。
    - **MHA 重复 8 次**(p.2355)。
2.  **DySe**(图5):
    - FU1/2/3 经 MLP 降维至 128 通道, FU2/FU3 双线性上采样后与 FU1 并联得 `F_U`(3×80×80×128, 公式8)。
    - `F'_U = Cha(Spa(Sca(F_U)))`(公式9), 按尺度切片解耦+下采样得 F'U1/2/3(公式10)。
    - 尺度/通道注意力: 改进 SENet(公式11, 全局平均池化压缩→瓶颈 MLP→点积加权 `F_CHA=F⊙FC(∑F(i,j)/N)`); 空间注意力: DCN(Zhu 2019)学卷积偏移量动态提取局部特征。

**损失函数**(第4节): 与 CFT 一致, L_box(GIoU)+L_cls(交叉熵)+L_conf(均方误差)。

**训练设置**(第5.1节): COCO 预训练 YOLOv5 初始化(VEDAI 用 YOLOv5s, FLIR/LLVIP 用 YOLOv5l); SGD(动量0.937, 衰减0.0005, lr0.01); batchsize=16; LLVIP 100 轮, FLIR/VEDAI 300 轮; 3 DyFu+6 DySe; 马赛克增强+标签平滑。

**与已有方法差异**: 相比基线(相加)更深入交互融合且增加选择; 相比 CFT/YOLOFusion 首次引入独立特征选择模块 DySe, 形成"融合+选择"双重增强。

## 6. 实验与结果
- **数据集**(表1): FLIR(自动驾驶, 3类, 4129/1013); LLVIP(夜视行人, 1类, 12025/3463); VEDAI(航拍车辆, 9类小目标, 1089/121); 均已预配准。
- **对比方法**(表2): 单模态 YOLOv5(RGB/IR)、前融合(通道拼接)、后融合(并集后 NMS)、基线(相加)、YOLOFusion、CFT; 结果均为作者复现。
- **指标**: mAP50/mAP75/mAP。
- **主结果**(表2): 本文(DyFu+DySe)三数据集均最优。相比基线 mAP75 ↑4.6%/2.6%/7.5%, mAP ↑3.2%/2.1%/3.1%, mAP50 ↑1.3%/0.6%/3.9%。关键值: FLIR 77.5/36.5/40.6; LLVIP 97.4/74.6/65.0; VEDAI 80.7/67.6/51.7。四点规律: 暗光数据集红外单模态远超可见光(约+10%); 部分融合法甚至低于红外单模态而本文均优于单模态; mAP75/mAP 提升大于 mAP50(定位精度高, 归功 DCN); 类别越多提升越多(VEDAI)。P-R/混淆矩阵见图6-7。
- **可视化**(图8-10): 相比 CFT 虚警/漏检更低, 能检出漏标目标, 定位更准。
- **消融**(表3): 完整模型三数据集均最优, 单模块也提升。注: VEDAI 完整 mAP50 标 80.4(↑3.6), 与表2 的 ↑3.9 有论文内部小差异。
- **效率**(表4, FLIR): 参数 73.72/206.03/216.16 M; 计算 190.14/224.40/236.95 GFlop/s; 帧率 15.9/7.7/7.1 帧/s。相比 CFT 小幅增参换较大性能提升, 但相比基线帧率明显下降。
- **注意力可视化**(图11): 随 DyFu 加深, 高关注区由背景转向目标, 并对红外"鬼影"逐渐降低关注度防虚警。

## 7. 这篇论文真正有价值的地方
1.  **"先融合后选择"范式**: 把融合与选择拆为两个独立互补步骤, 对多模态及精细特征处理任务有启发。
2.  **Transformer 跨模态联合注意力**: 先拼接再算注意力, 权重矩阵同含模态内自相关与模态间互相关四区域, 比分别提特征再拼接更深入; MHA 重复 8 次体现迭代融合。
3.  **DCN 作为空间注意力**: 感受野随内容动态调整, 论文将 mAP75 大幅提升归因于此, 提示精确定位任务可用 DCN 增强空间注意力。
4.  **模块化与诚实实验**: DyFu/DySe 可插拔、消融清晰; 如实报告帧率代价与表内小差异, 可复现性好。

## 8. 局限与问题
1.  **计算成本增加**: 帧率 15.9→7.1 帧/s(表4), 限制实时/边缘部署; 作者已将轻量融合列为未来工作。
2.  **依赖预配准**: 要求输入双光图像已配准; 处理未配准图像是作者明确的未来方向。
3.  **数据集偏向**: 集中于自动驾驶/夜视行人/航拍车辆三类, 通用场景泛化 PDF 文本未明确。
4.  **模块数量固定**: 3 DyFu+6 DySe, PDF 文本未给层数/位置敏感性消融。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要+引言(第0节)+结论(第6节)+图2。
- **复现**: 方法(第1-4节)公式(4)-(11)与图3/5; 实验设置(第5.1节)注意 backbone 混用(YOLOv5s/l)、batchsize=16、轮数差异、马赛克+标签平滑、MHA 重复 8 次。
- **借鉴**: 融合学 DyFu 跨模态注意力(公式4-7); 选择学 DySe 多尺度注意力(公式8-11, SENet+DCN); 定位精度借鉴 DCN 空间注意力。
- **写 related work**: 归入"基于注意力的红外+可见光融合检测"或"Transformer 视觉检测", 与 CFT、YOLOFusion、Fu(Swin 双光)对比。

## 10. 和其他论文的关系
- 基于 **YOLOv5**(检测器)与 **CSPDarkNet53**(骨干)改进。
- DyFu 受 **CFT**(Cross Modality Fusion Transformer, Fang 2022)启发, 损失函数也与 CFT 一致。
- DySe 使用 **SENet**(Hu 2018, 尺度/通道注意力)与 **DCN**(Zhu 2019, 可变形卷积, 空间注意力); FPN(Lin 2017)+PAN(Liu 2018)构成颈部。
- 与 **YOLOFusion**(Fang & Wang 2022)、**Fu 等 2023**(Swin-Transformer 双光)等双光检测方法是同类竞争/对比关系。

## 11. 关键词
红外图像, 目标检测, 注意力机制, 特征融合, 深度神经网络, 动态特征选择, Transformer, 可变形卷积(DCN), SENet, YOLOv5, 双模态检测

## 12. 可信度说明
本精读笔记基于 PDF 提取文本(12/14 页, 覆盖摘要、引言、方法、损失、实验、消融、效率与结论核心内容)生成, 关键数值(三数据集 mAP50/75/mAP 提升、表2/表3/表4 具体数字、训练超参、MHA 重复 8 次、backbone 混用)均能在提取文本逐条核对。提取文本未覆盖的页(p.13-14, 主要为图11 后续与参考文献)不含影响结论的新数据。笔记如实记录了论文内部表2 与表3 在 VEDAI mAP50 上 3.9/3.6 的小差异, 未做编造或外部补充。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 1780 字符/页, 正文清晰); 来源缓存: `.paper-cache/extracts/cjig_图像识别_红外与可见光图像特征动态选择的目标检测网络.txt` (提取覆盖 12/14 页, 含完整摘要/方法/实验/结论; 缺失 p.13-14 主要为图11 后续与参考文献); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本次重读已对照提取文本逐条核对数值并修正分类。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-14; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-14。
- **提取情况**: 缺失页 2 页, 其中 2 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.14: 2021 IEEE/CVF International Conference on Computer Vision

### 缺失页关键摘录

- p.13: Fig.11 Qualitative comparison of attention weight matrix in different dynamic fusion layers2362
- p.14: visible -infrared paired dataset for low -light vision//Proceedings of
- p.14: small target detection benchmark . Journal of Visual Communication
- p.14: 39（6） ： 1137 -1149 ［DOI： 10.1109 /TPAMI .2016 .2577031 ］Saga F ’s team . Free FLIR thermal dataset for algorithm training ［DB/
- p.14: https ：//www .flir.com/oem/adas/adas -dataset -form/
<!-- AI_READING_NOTE_END -->
