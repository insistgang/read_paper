---
title: "CondConv: Conditionally Parameterized Convolutions for Efficient Inference"
authors:
  - "Brandon Yang"
  - "Gabriel Bender"
  - "Quoc V. Le"
  - "Jiquan Ngiam"
year: 2019
venue: "NeurIPS 2019"
doi: 
pdf: [[CondConv.pdf]]
primary_topic: B_注意力算子模块
topics:
  - "B_注意力算子模块"
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
extract_cache: .paper-cache/extracts/CondConv.txt
---

# CondConv: Conditionally Parameterized Convolutions for Efficient Inference

## 基本信息
- **PDF**: [[CondConv.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | CondConv: Conditionally Parameterized Convolutions for Efficient Inference |
| **作者** | Brandon Yang; Gabriel Bender; Quoc V. Le; Jiquan Ngiam (均为 Google Brain) |
| **发表时间** | 2019 (NeurIPS 2019; arXiv:1904.04971v3, 2020-09-04) |
| **刊物/会议** | NeurIPS 2019 (第 33 届, Vancouver) |
| **DOI** | 未明确 |

## 摘要

> **英文原摘要(清理后)**：Convolutional layers are one of the basic building blocks of modern deep neural networks. One fundamental assumption is that convolutional kernels should be shared for all examples in a dataset. We propose conditionally parameterized convolutions (CondConv), which learn specialized convolutional kernels for each example. Replacing normal convolutions with CondConv enables us to increase the size and capacity of a network, while maintaining efficient inference. We demonstrate that scaling networks with CondConv improves the performance and inference cost trade-off of several existing convolutional neural network architectures on both classification and detection tasks. On ImageNet classification, our CondConv approach applied to EfficientNet-B0 achieves state-of-the-art performance of 78.3% accuracy with only 413M multiply-adds. Code and checkpoints for the CondConv Tensorflow layer and CondConv-EfficientNet models are available at: https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet/condconv.

> **中文翻译**：卷积层是现代深度神经网络最基本的构件之一。其中一个根本性假设是：同一份卷积核应当被数据集中所有样本共享。本文提出条件参数化卷积(CondConv)，为每个样本学习专门定制的卷积核。用 CondConv 替换普通卷积，使我们能够在保持高效推理的同时增大网络的规模与容量。我们证明：用 CondConv 对网络进行缩放，能改善多个现有卷积神经网络架构在分类与检测两类任务上的"性能-推理成本"权衡。在 ImageNet 分类上，将 CondConv 应用于 EfficientNet-B0 取得了 78.3% 准确率的 SOTA 表现，而乘加运算仅为 413M。CondConv 的 TensorFlow 层与 CondConv-EfficientNet 模型的代码及检查点已开源(github.com/tensorflow/tpu，efficientnet/condconv 目录)。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：深度 CNN 的性能提升主要来自扩大模型规模与容量(加深/加宽)以适配越来越大的数据集，但当前提升容量的做法计算代价高昂。常规增容(加大核高/宽、增减输入/输出通道)的额外计算量与卷积输入(特征图)的尺寸成正比，开销很大；部署最好的模型推理会消耗大量数据中心算力，对延迟敏感的应用往往不可行。
- **之前方法的问题**：受"移动端部署 + 参数量受限"导向的影响，当前的高效模型(MobileNet 等)参数极少。但存在一类增长中的视觉应用——它们并不受参数量约束，却对推理延迟有严格要求(如实时服务端视频处理、自动驾驶感知)。现有高效模型并不能很好地服务这类场景。
- **核心矛盾**：如何在**不显著增加推理计算成本(尤其是乘加 MADDs)**的前提下，**有效提升模型容量与性能**。论文动机即为这类"参数不受限、延迟受限"的应用设计模型。

## 关键贡献

1. **提出 CondConv 层**：一种条件参数化卷积，卷积核是输入样本的函数，参数化为 `n` 个专家核的线性组合 `(α₁W₁+...+αₙWₙ) * x`，其中 `αᵢ = rᵢ(x)` 由路由函数依输入经梯度下降学得。增容方式从"加大核"改为"增加专家数 n"——每多一个参数仅多 1 次乘加，而非与像素数成正比。
2. **设计高效路由函数**：`r(x) = Sigmoid(GlobalAveragePool(x) · R)`，三步(全局平均池化→全连接矩阵 R→Sigmoid)把全局上下文映射到 `n` 个专家权重，让局部卷积运算能借助全局信息做自适应。
3. **即插即用、广泛验证**：CondConv 可直接替换任意卷积层(含深度可分离卷积、全连接层)。在 MobileNetV1/V2、ResNet-50、MnasNet-A1、EfficientNet-B0 上，统一用 8 个专家，于 ImageNet 分类(<10% MADDs 增幅)和 COCO 检测(<5% MADDs 增幅)上均带来稳定提升。
4. **揭示数学等价性与高效训练策略**：证明 CondConv 在数学上等价于更昂贵的"线性混合专家(每个专家是一次静态卷积)"，但推理只需 1 次卷积。训练时按专家数选实现：专家数 ≤4 用线性混合专家式(大批量分支卷积，利于当前加速器)，专家数 >4 用 batch size=1 的直接条件卷积更高效。
5. **分析路由机制特性**：消融研究路由结构(单次/部分共享/隐藏层/层级/Sigmoid vs Softmax)与 CondConv 所在深度；可视化显示路由权重随网络变深更具类别特异性，且各专家学到语义明确的模式(专家1=轮式车辆、专家2=矩形结构、专家3=圆柱形家居物、专家4=棕黑色犬种)。

## 方法

- **整体框架**：CondConv 层直接替换 CNN 中的卷积层。对每个样本先把 `n` 个专家核线性组合成一份"该样本专属"的卷积核，再做 1 次卷积。关键直觉：卷积核会被应用在输入的许多空间位置上，而专家核每个样本只需合并一次——因此增加 n 带来容量增长，但推理成本只小幅上升。
- **输入输出**：输入特征图 `x`；输出为经条件卷积与激活后的特征图。
- **核心公式**：`Output(x) = σ((α₁W₁+...+αₙWₙ) * x)`，每个 `Wᵢ` 与原卷积核同维，`αᵢ` 是样本依赖的标量，`σ` 为激活函数。
- **路由函数**：`r(x) = Sigmoid(GlobalAveragePool(x) · R)`，`R` 是把池化后向量映射到 `n` 个专家权重的可学习矩阵。论文设计目标是路由既要高效、能有意义地区分样本、又可解释。注意：若路由对所有样本恒定，CondConv 就退化为静态卷积，因此"逐样本路由"是其性能关键。
- **数学等价性**：`σ((α₁W₁+...+αₙWₙ) * x) = σ(α₁(W₁*x)+...+αₙ(Wₙ*x))`。右侧是线性混合专家，需 n 次卷积；CondConv 先合核再卷积，仅 1 次卷积即可获得同等容量，故高效。
- **两种等价训练实现**：
    1. **直接条件卷积式**(Fig.1a)：先为每个样本算核，再以 batch size=1 卷积。专家数 >4 时更高效。
    2. **线性混合专家式**(Fig.1b)：对每个专家分支做大批量卷积再加权求和。当前加速器擅长大批量卷积、难以利用小批量，故专家数 ≤4 时此式训练更高效；推理仍切回高效的 CondConv 形式。
- **块内路由共享**：在一个 block(残差块/倒残差块/可分离卷积块)内共享路由权重；部分模型还把最终全连接分类层换成 1×1 CondConv 层。具体架构见 Appendix A(提取文本未覆盖)。
- **正则化**：对大容量模型使用 Dropout(logits 前 FC 输入处，keep 概率 0.6~1.0)、AutoAugment(ImageNet 策略)、Mixup(α=0.2)；为缓解大 ResNet 的过拟合，提出基于 Shake-Shake 的"训练时随机丢弃专家"的新数据增强。
- **与已有方法的差异**：
    - vs **条件计算/MoE**：传统条件计算需对样本做离散路由(常借助 RL/进化/聚类)，难训练；CondConv 无需离散路由，可直接用梯度下降优化。
    - vs **权重生成网络**(HyperNetwork、Platanios 等)：那些方法对数据集所有样本(或每个语言对内)生成相同权重；CondConv 让每个样本用不同权重。
    - vs **多分支网络**(Inception/ResNeXt)：CondConv 数学等价于"每分支一次卷积、加权求和"的多分支层，但只需 1 次卷积。
    - vs **激活缩放**(SENet 缩放每层激活、GaterNet 选二值滤波器掩码、注意力方法缩放输入)：这些都只调制基础网络的激活；CondConv 直接动态生成卷积核权重。
    - **注意力视角**：CondConv 可视为在**卷积核维度**上、由全局上下文驱动的输入依赖注意力——用全局平均池化得到的全局信息动态生成核参数。

## 实验

- **数据集**：ImageNet 2012(128 万训练图、5 万验证图、1000 类，输入 224×224，单 crop top-1)；COCO 目标检测(SSD300，输入 300×300，在排除 8000 张 minival 后的 train+val 上训练，于 minival 评测)。
- **对比方法**：作者用相同超参与正则搜索空间重训的静态卷积基线(MobileNetV1/V2、ResNet-50、MnasNet-A1、EfficientNet-B0)。所有 CondConv 模型每层 8 个专家。
- **评价指标**：ImageNet top-1 准确率、COCO minival mAP(AP@IoU=0.50:0.05:0.95)，计算成本以乘加数 MADDs 衡量。
- **主实验(Table 1, ImageNet, 单位 10⁶ MADDs)**：
    - MobileNetV1(1.0x): 71.9%/567 → **73.7%/600**
    - MobileNetV2(1.0x): 71.6%/301 → **74.6%/329**
    - MnasNet-A1: 74.9%/312 → **76.2%/325**
    - ResNet-50: 77.7%/4093 → **78.6%/4213**
    - EfficientNet-B0: 77.2%/391 → **78.3%/413**(对照 MixNet frontier 为当时 SOTA)
    - 所有架构推理成本增幅 <10%。另：CondConv-EfficientNet-B0-depth(深度乘子 1.1x)达 **79.5%/614M**，优于同条件重训的 EfficientNet-B1(79.2%/700M)——说明在该区间 CondConv 缩放优于复合系数静态缩放。
- **COCO 检测(Table 2, CondConv-MobileNetV1 SSD300, 8 专家, 单位 10⁶ MADDs)**：
    - 0.5x: 14.4/352 → **18.0/363**
    - 0.75x: 18.2/730 → **21.0/755**
    - 1.0x: 20.3/1230 → **22.4/1280**
    - 推理成本增幅 <5%；CondConv-MobileNetV1(1.0x) 比基线提升 2.1 mAP，且 0.75x CondConv 以 60% 推理成本就超过 1.0x 基线 0.7 mAP。
- **消融——路由结构(Table 3, CC-MobileNetV1 0.25x, 32 专家, 基线 62.0%/55.7M)**：
    - **Single**(只在第 7 个可分离卷积块算一次路由、后续层复用)显著最差(56.5%)；逐层路由(基线)与 **Partially-shared**(隔层共享)都远超 Single → 在多个深度做路由能提质；Partially-shared(62.5%)略优于基线，说明邻近层共享路由略有益。
    - **隐藏层**：在池化后加 ReLU 隐藏层；Hidden(medium)(62.2%)略提升，Hidden(small)(57.7%)、Hidden(large)(54.1%)较差——隐藏层过大易过拟合。
    - **Hierarchical**(把上一层路由权重拼接到本层池化输出)也易过拟合(60.3%)。
    - **Softmax**(60.5%) 显著差于 Sigmoid(62.0%)——表明单个样本常需同时激活多个专家，Sigmoid 允许多专家并激活。
- **消融——CondConv 所在深度(Table 4, CC-MobileNetV1 0.25x)**：纯 MobileNetV1(0.25x) 基线为 50.0%/41.2M。从第 1 层起全用 CondConv 最佳(62.5%/56.3M)；从第 7 层起开始用与从第 1/5 层起几乎持平(62.0%)，即在第 7 层之前再加 CondConv 对性能影响很小。仅在最终 FC 层用 CondConv(Layer 15, FC Only) 也能从 50.0% 提到 54.2%，但收益不如全网使用；去掉 FC 层的 CondConv(7 No FC)略降到 60.2% 但更省算力——FC 层的 CondConv 占了 0.25x 模型相当一部分额外推理成本。
- **可视化分析(Sec.5, 提取文本止于此节开头)**：Fig.3 显示路由权重随深度更具类别特异性；Fig.4 末层路由权重呈双峰分布；Fig.6 显示 4 个专家分别特化到轮式车辆/矩形结构/圆柱形家居物/棕黑色犬种。

## 局限

- **延迟与参数量未充分报告**：论文以 MADDs 衡量成本，但 CondConv 显著增加参数量(专家核+路由参数)，而真实硬件上的实际推理延迟、以及核合并/路由本身的开销在提取文本中未给出系统评估。
- **训练复杂度上升**：两套等价实现需按专家数切换，加上额外参数，可能增加调参与训练稳定性的负担。
- **大容量模型易过拟合**：大 ResNet 必须额外引入"专家 Dropout(Shake-Shake 变体)"才能控制过拟合；消融中大隐藏层、Hierarchical 路由也都观察到过拟合——说明容量大幅上升后过拟合风险升高。
- **任务范围**：实验集中在 ImageNet 分类与 COCO 检测(SSD)，对语义/实例分割等其他密集预测任务的效果在提取文本中未涉及。
- **细节未在提取文本中给出**：路由矩阵 R 的具体维度、专家核初始化方式、完整架构表(Appendix A)、Section 5 分析的完整内容(提取缓存止于该节开头)。

## 个人评论

1. **把"增容成本"从空间维迁到一次性核合成**：传统增容(加大核/通道)的成本与特征图像素数成正比，而 CondConv 把额外参数的代价压到"每参数仅 1 次乘加"。这条"参数不受限、延迟受限"的设计思路，对服务端实时视频、自驾感知等场景很有启发。
2. **数学等价性带来工程价值**：CondConv 与线性混合专家严格等价的洞见，既解释了它为何"有 n 倍容量却只 1 次卷积"，又落地成"按专家数选训练实现"的实用技巧——这是把理论等价转化为训练效率的范例。
3. **可解释性是亮点**：专家特化到语义类别(车辆/建筑/家居物/犬种)、路由权重的双峰分布与随深度增强的类别特异性，给"动态网络如何工作"提供了少见的直观证据。
4. **对后续研究的催化**：本文(NeurIPS 2019)催生了一系列动态卷积/条件参数化工作(Dynamic Convolution、DyNet、ODConv 等)，说明"在卷积核上做条件化"是简单而富有成效的设计空间。
5. **可商榷处**：以 MADDs 而非真实延迟作为主成本指标，可能高估实际部署收益(动态核合并、按样本路由在加速器上未必廉价)；参数量大幅膨胀对显存/存储也有代价。这些在论文中讨论不足。

### 使用建议

- **快速了解**：读 Abstract、Section 1 Introduction，以及 4.1 中 Table 1，即可掌握核心思想与主要结果。
- **复现**：重点读 Section 3(数学形式与路由)与 Section 4(实验设置、训练细节、两种实现选择、架构替换策略)，并参考 Appendix A(提取文本未覆盖)与开源代码。
- **借鉴创新点**：核心是"输入依赖的动态卷积核"；路由 `GlobalAvgPool→FC→Sigmoid` 是简洁有效的基线(注意 Sigmoid 优于 Softmax)；训练时按专家数切换实现、用专家 Dropout 抑制过拟合也值得借鉴。
- **写 related work**：可归入条件计算/动态计算、输入依赖卷积、高效神经网络架构、混合专家(MoE)四类。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉中的**高效神经网络设计**方向，更具体落在**动态神经网络 / 条件计算**子方向。它要解决深度 CNN 的"模型容量 vs 推理效率"矛盾。放在"**注意力算子模块**"主题下是恰当的：CondConv 本质是依输入动态计算卷积核权重的机制，可看作作用于**卷积核维度**、由全局上下文驱动的输入依赖注意力(与 SENet 那种作用于通道激活的注意力相对)。发表于 NeurIPS 2019(arXiv:1904.04971)。

## 2. 一句话总结
CondConv 把卷积核参数化为输入的条件函数(n 个专家核的样本依赖加权组合)，在数学上等价于 n 专家的线性混合专家、却只需 1 次卷积，从而以 <10% 的推理成本增幅显著提升多种 CNN 的容量与性能。

## 3. 背景与问题
- **为什么要做**：CNN 性能提升主要靠扩容(加深/加宽)，但常规增容的额外计算量与卷积输入特征图尺寸成正比，开销大、对延迟敏感的部署不友好。
- **之前方法的问题**：受移动端导向影响，高效模型参数极少；但一类"参数不受限、推理延迟受限"的应用(实时服务端视频、自驾感知)缺乏合适模型。
- **核心矛盾**：在不显著增加推理成本(尤其 MADDs)的前提下有效提升模型容量与性能。

## 4. 核心贡献
1. **CondConv 层**：卷积核 = `(α₁W₁+...+αₙWₙ)`，`αᵢ=rᵢ(x)` 为样本依赖标量；增容靠加专家数 n，每参数仅 +1 次乘加。
2. **高效路由**：`r(x)=Sigmoid(GlobalAvgPool(x)·R)`，用全局上下文调制局部卷积。
3. **即插即用 + 广验证**：替换 MobileNetV1/V2、ResNet-50、MnasNet-A1、EfficientNet-B0 的卷积层(统一 8 专家)，ImageNet(<10% MADDs)、COCO(<5% MADDs)均稳定提升。
4. **数学等价 + 高效训练**：等价于线性混合专家但推理仅 1 次卷积；专家数 ≤4 用混合专家式训练、>4 用 batch=1 直接条件卷积。
5. **机制分析**：消融路由结构与所在深度；可视化显示专家语义特化、路由权重随深度更类别特异、末层呈双峰分布。

## 5. 方法详解
- **整体框架**：每样本先把 n 个专家核线性组合成一份专属核，再做 1 次卷积；关键在于核被复用于许多空间位置，而专家合并每样本只做一次，故增 n 容量增、成本只小升。
- **核心公式**：`Output(x)=σ((α₁W₁+...+αₙWₙ)*x)`，`Wᵢ` 与原核同维。
- **路由**：`r(x)=Sigmoid(GlobalAvgPool(x)·R)`，`R` 把池化向量映射到 n 个权重。若路由恒定则退化为静态卷积，故逐样本路由是性能关键。
- **数学等价**：`σ((ΣαᵢWᵢ)*x)=σ(Σαᵢ(Wᵢ*x))`，右侧需 n 次卷积，CondConv 先合核仅 1 次卷积。
- **两种等价训练实现**：(a) 直接条件卷积(batch=1)，专家 >4 更高效；(b) 线性混合专家(大批量分支卷积+加权求和)，专家 ≤4 更高效；推理统一切回高效形式。
- **工程细节**：block 内共享路由权重；部分模型把 FC 分类层换成 1×1 CondConv；正则用 Dropout(keep 0.6~1.0)、AutoAugment、Mixup(α=0.2)，大 ResNet 额外用基于 Shake-Shake 的专家 Dropout。
- **与已有方法差异**：vs 条件计算/MoE(无需离散路由，梯度可优化)；vs 权重生成网络(它们对所有样本同权重)；vs 多分支(等价但仅 1 次卷积)；vs 激活缩放/SENet/GaterNet/注意力(它们只调制激活，CondConv 生成核权重)。

## 6. 实验与结果
- **数据集**：ImageNet 2012(128 万训练/5 万验证/1000 类，224×224，单 crop top-1)；COCO(SSD300，300×300，排除 8000 minival 后训练并在 minival 评测)。
- **指标**：top-1 acc / mAP(AP@0.50:0.05:0.95) / MADDs。CondConv 均用 8 专家。
- **Table 1(ImageNet, 10⁶ MADDs)**：MobileNetV1 1.0x 71.9/567→73.7/600；MobileNetV2 1.0x 71.6/301→74.6/329；MnasNet-A1 74.9/312→76.2/325；ResNet-50 77.7/4093→78.6/4213；EfficientNet-B0 77.2/391→78.3/413(SOTA vs MixNet)。CondConv-EfficientNet-B0-depth(1.1x 深度)79.5/614，胜过 EfficientNet-B1(79.2/700)。增幅 <10%。
- **Table 2(COCO, CondConv-MobileNetV1 SSD300, 8 专家)**：0.5x 14.4/352→18.0/363；0.75x 18.2/730→21.0/755；1.0x 20.3/1230→22.4/1280。增幅 <5%；1.0x 提升 2.1 mAP，0.75x CondConv 以 60% 成本超 1.0x 基线 0.7 mAP。
- **Table 3 路由消融(0.25x, 32 专家, 基线 62.0/55.7M)**：Single 56.5(最差)；Partially-shared 62.5(略优于基线)；Hidden(medium) 62.2、(small) 57.7、(large) 54.1；Hierarchical 60.3；Softmax 60.5(显著差于 Sigmoid 62.0)→单样本常需多专家并激活。
- **Table 4 深度消融(0.25x)**：纯 MobileNetV1 0.25x 为 50.0/41.2M；从第 1 层起全用 62.5/56.3M(最佳)，第 5/7 层起 ~62.0，第 7 层前再加 CondConv 影响很小；仅 FC 层(Layer 15)54.2；7 No FC 60.2(略降但更省)。
- **可视化(Sec.5, 提取止于此节开头)**：Fig.3 类别特异性随深度增强、Fig.4 末层双峰分布、Fig.6 专家特化(车辆/矩形结构/圆柱形家居物/棕黑犬种)。

## 7. 这篇论文真正有价值的地方
1. **高效扩容范式**：把"与像素数成正比"的卷积成本，转为"每样本仅合并一次"的核合成成本，给大容量低延迟模型一条更高效的扩展路径。
2. **数学等价性的洞见与落地**：与线性混合专家严格等价，既解释了高效性，又转化为"按专家数选训练实现"的实用技巧。
3. **可解释性证据**：专家语义特化、路由权重双峰分布与随深度的类别特异性，是理解动态网络如何工作的难得直观案例。
4. **催化后续研究**：激励了 Dynamic Convolution、ODConv 等一系列动态/条件卷积工作。

## 8. 局限与问题
- 以 MADDs 而非真实延迟为主成本指标，未系统评估实际推理延迟、参数量膨胀以及核合并/路由开销。
- 两套等价实现需按专家数切换，叠加额外参数，增加训练/调参负担。
- 大容量模型(大 ResNet、大隐藏层路由、Hierarchical 路由)易过拟合，需专家 Dropout 等额外正则。
- 任务范围限于分类与检测(SSD)，对分割等密集预测未涉及(提取文本内)。
- R 维度、专家核初始化、Appendix A 架构表、Section 5 完整分析在提取文本中未给出(提取缓存止于 Sec.5 开头)。

## 9. 我该怎么使用这篇论文
- **快速了解**：Abstract + Section 1 + Table 1。
- **复现**：Section 3(数学/路由) + Section 4(实验设置、两种实现选择、架构替换) + Appendix A(提取未覆盖) + 开源代码。
- **借鉴创新点**：输入依赖动态核；路由 `GlobalAvgPool→FC→Sigmoid`(Sigmoid 优于 Softmax)；按专家数切换训练实现；专家 Dropout 抗过拟合。
- **写 related work**：条件计算/动态计算、输入依赖卷积、高效网络架构、混合专家。

## 10. 和其他论文的关系
- [[SENet]]：同样用全局信息(GAP)做调制，但 SENet 缩放通道激活，CondConv 生成卷积核权重——两者是"激活注意力 vs 核注意力"的对照(论文 Related Work 明确以 SENet 作对比)。
- [[EfficientNet]]：CondConv 在 EfficientNet-B0 上取得 78.3% SOTA，并与其复合缩放系数做了直接比较(CondConv-B0-depth 胜过 B1)。
- [[MixNet]]：作为 frontier 参照系；MixNet 混合卷积核尺寸，CondConv 混合卷积核参数。
- [[MnasNet]]：作为 NAS 高效基线，CondConv 是可叠加的模块化提升组件。
- 与 MoE / HyperNetwork / 多分支网络(Inception、ResNeXt)/ GaterNet / SplineNets 等在 Related Work 中均有定位对比。

## 11. 关键词
条件卷积, 动态卷积, 混合专家(MoE), 高效推理, 条件计算, 路由函数, 模型容量, ImageNet 分类, COCO 检测, 参数化卷积, 输入依赖, 核注意力

## 12. 可信度说明
本精读基于 PDF 提取文本(12/12 页，约 2086 字符/页，提取质量良好)生成，覆盖了摘要、引言、相关工作、方法(Section 3)、全部主实验与消融(Table 1-4)及图 1-6 的描述性文字。Table 1/2/3/4 的全部数值、专家特化结论(Fig.6)、训练实现切换阈值(≤4 vs >4 专家)均逐条核对自原文。**需注意**：提取文本止于 Section 5 "Analysis" 的开头(原文 41942 字符，缓存仅展示前 25000 字符)，故 Section 5 后续分析与 Appendix A 完整架构表未被覆盖，相关细节(R 维度、专家核初始化等)已标注"提取文本未明确"。相对原始骨架，本次修正了:作者/会议(NeurIPS 2019 而非泛指 arXiv)、补全了 MnasNet-A1 与 ResNet-50 的 Table 1 数值、修正了 Table 4 深度消融的解读(最佳为从第 1 层起、第 7 层前增益很小，而非"第 7 层及之后最佳")、补全了路由消融各项具体数值。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/CondConv.txt` (12/12 页, 文本止于 Sec.5 开头, 约 25000/41942 字符); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
