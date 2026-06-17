---
title: "LMFLoss: A Hybrid Loss for Imbalanced Medical Image Classification"
authors:
  - "Abu Adnan Sadi"
  - "Labib Chowdhury"
  - "Nusrat Jahan"
  - "Mohammad Newaz Sharif Rafi"
  - "Radeya Chowdhury"
  - "Faisal Ahamed Khan"
  - "Nabeel Mohammed"
year: 2022
venue: "arXiv"
doi: 
pdf: [[LMFLoss.pdf]]
primary_topic: A2_医学图像_分类_配准_生成
topics:
  - "A2_医学图像_分类_配准_生成"
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
extract_cache: .paper-cache/extracts/LMFLoss.txt
---

# LMFLoss: A Hybrid Loss for Imbalanced Medical Image Classification

## 基本信息
- **PDF**: [[LMFLoss.pdf]]
- **primary_topic**: `A2_医学图像_分类_配准_生成`
- **topics**: `A2_医学图像_分类_配准_生成`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | LMFLoss: A Hybrid Loss for Imbalanced Medical Image Classification |
| **作者** | Abu Adnan Sadi; Labib Chowdhury; Nusrat Jahan; Mohammad Newaz Sharif Rafi; Radeya Chowdhury; Faisal Ahamed Khan; Nabeel Mohammed |
| **单位** | North South University; Giga Tech Limited; City Hospital（均位于孟加拉国达卡） |
| **发表时间** | 2022（arXiv:2212.12741v1, 2022-12-24） |
| **刊物/会议** | arXiv（预印本，注：作者标注代码"待录用后开放"，提示其投稿目标可能为会议） |
| **DOI** | 未明确（arXiv ID: 2212.12741） |

## 摘要

**英文原摘要（据 PDF 提取文本整理）**：

> Automatic medical image classification is a very important field where the use of AI has the potential to have a real social impact. However, there are still many challenges that act as obstacles to making practically effective solutions. One of those is the fact that most of the medical imaging datasets have a class imbalance problem. This leads to the fact that existing AI techniques, particularly neural network-based deep-learning methodologies, often perform poorly in such scenarios. Thus this makes this area an interesting and active research focus for researchers. In this study, we propose a novel loss function to train neural network models to mitigate this critical issue in this important field. Through rigorous experiments on three independently collected datasets of three different medical imaging domains, we empirically show that our proposed loss function consistently performs well with an improvement between 2%–10% macro f1 when compared to the baseline models. We hope that our work will precipitate new research toward a more generalized approach to medical image classification.
>
> **Index Terms** — Imbalanced Classification, Medical Imaging, Loss Function, Minority Class

**中文翻译**：

> 自动医学图像分类是一个非常重要的领域，AI 在其中有望产生真实的社会影响。然而，要做出实际有效的解决方案仍面临诸多障碍，其中之一便是大多数医学影像数据集存在类别不平衡问题。这导致现有 AI 技术——尤其是基于神经网络的深度学习方法——在此类场景下往往表现不佳，因而该问题成为研究者关注的活跃焦点。本研究提出了一种新颖的损失函数来训练神经网络模型，以缓解这一关键问题。通过在三个独立采集、来自三种不同医学影像领域的数据集上进行严格实验，我们实证表明，相比基线模型，所提损失函数能稳定带来 2%–10% 的宏 F1 提升。我们希望本工作能推动针对医学图像分类更具普适性方法的新研究。
>
> **关键词** — 不平衡分类、医学影像、损失函数、少数类

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：基于神经网络的计算机视觉方法已使自动智能诊断工具具备接近人类水平的潜力（[1]），但这类系统多用于诊断常见病，应用面受限。医学影像数据集中罕见病样本数量显著少于常见病，造成类别不平衡，使神经网络模型产生偏置、在少数类上表现很差，阻碍其作为医生辅助工具落地（p.1）。本研究即针对此类别不平衡挑战。
- **之前方法有什么问题**（论文把缓解类别不平衡的工作分为数据中心与算法两大类）：
  - **数据中心策略**（过采样/欠采样）：过采样为少数类生成人造样本，欠采样剔除多数类样本；但包括 [3, 4] 在内的多项研究表明，这些方法并非总是可行（p.1）。
  - **算法层面策略**（深度学习领域主要做法是设计损失函数，而非操纵数据）：
    - **类别加权交叉熵**：为各类设置类别系数权重，使少数类误分类受到更重惩罚（[5]）；但权重固定，无法按样本难度动态调整。
    - **焦点损失（Focal Loss，[6]）**：自适应地为每个训练样本设权重，使难样本获得更高权重；通过聚焦参数 $\gamma$ 下调易分类（多数类）样本的损失，引导模型关注难样本。论文未把"类别先验分布"作为其显式考量。
    - **标签分布感知边缘损失（LDAM Loss，[9]）**：依据类别样本数为少数类设定更大的分类边缘，对少数类施加更强正则以降低其泛化误差。其按类别分布判定权重，但本身不显式按样本难度动态加权。
- **核心矛盾（作者的假设）**：Focal Loss 侧重关注**难分类样本**，LDAM 侧重依据**类别分布**判定权重；作者假设**同时**利用两种特性可比单独使用任一种更有效（p.2，"We hypothesize that leveraging both features simultaneously..."）。

## 关键贡献

> 论文 Introduction 末尾明确列出三条贡献：

1. 提出一种新颖的**混合损失函数**——大边缘感知焦点损失（Large Margin aware Focal, LMF Loss），将 Focal Loss 与 LDAM Loss 线性组合（公式 3），在单一框架内联合优化"对难样本的关注"与"对类别分布的考量"，缓解医学影像的类别不平衡问题。
2. 在三个流行的医学影像数据集（ODIR-5K、HAM-10K、ISIC-2019）上进行了大量实验，在所有数据集上取得 **2%–10%** 的宏 F1 性能提升。
3. 在 HAM 数据集的一个具体类别上，使用**少于 90 个训练样本**即达到 **80% 的 F1**，相比其他方法提升约 **9%**（对应 DF 类，训练样本 81 个，LMF 80.00 vs 交叉熵 71.43，详见 Table 2）。

## 方法

- **整体框架**：方法完全集中在损失函数设计上，不修改网络结构。将两种针对类别不平衡的损失（Focal Loss、LDAM Loss）线性组合为一个复合损失 LMF Loss，用于训练分类网络（迁移学习骨干为 ResNet50、EfficientNetV2）。
- **输入输出**：损失输入是模型对样本的预测（Focal 用正确类概率 $p_t$，LDAM 用各类 logits $z_j$）与真实标签；输出为标量损失，用于反向传播。
- **关键模块与数学公式**：
  1. **焦点损失（FL）**：$FL(p_t) = -(1-p_t)^\gamma \log(p_t)$（公式 1）。$p_t$ 为模型对正确类别的预测概率，$\gamma$ 为可调聚焦参数；$\gamma$ 越大、易样本的损失被压得越低，使模型注意力转向难样本；$\gamma=0$ 时退化为标准交叉熵。本研究取 **$\gamma=1.5$**（论文称该值"produces better results"）。
  2. **标签分布感知边缘损失（LDAM）**：按类别样本数 $n_j$ 给出类别相关边缘 $\Delta_j = C / n_j^{1/4}$（$C$ 为常数），少数类边缘更大。设 $u = e^{z_y - \Delta_y}$，损失定义为 $L_{LDAM}((x,y); f) = -\log \dfrac{u}{u + \sum_{j \neq y} e^{z_j}}$（公式 2）。（注：提取文本中分母指数项 OCR 略有变形，此处按 LDAM 标准形式 $\sum_{j\neq y}e^{z_j}$ 给出。）
  3. **提出的大边缘感知焦点损失（LMF）**：$L_{LMF} = \alpha\, L_{LDAM} + \beta\, L_{FL}$（公式 3）。$\alpha$、$\beta$ 为可调超参数；论文称通过试错（trial and error）发现**两者取相同权重**即可取得良好效果。
- **训练方式**：数据集按 **70:15:15** 划分训练/验证/测试，并保证每个子集的逐类分布与整体一致；所有图像缩放至 **224×224**；用 ImageNet 预训练的 **ResNet50** 与 **EfficientNetV2** 做迁移学习。（PDF 文本未明确学习率、优化器、训练轮数、批大小等。）
- **推理流程**：与常规分类一致，前向传播得到预测类别（损失仅作用于训练阶段）。
- **和已有方法的差异**：单用 Focal 只关注难样本、单用 LDAM 只看类别分布；LMF 旨在**同时**兼具二者——既像 Focal 一样动态关注难样本，又像 LDAM 一样按类别分布为少数类施加更强的边缘正则。

## 实验

- **使用的数据集**（均含类别不平衡）：
  - **ODIR-5K**：真实眼科患者数据，**8 个类别**，总样本 **6392**。
  - **HAM-10K**：皮肤镜图像，**7 个类别**，总样本 **10015**。
  - **ISIC-2019**：皮肤病变图像，**8 个类别**，总样本 **25331**。
- **对比方法**：交叉熵（Cross-Entropy）、Focal Loss、LDAM Loss。
- **评价指标**：准确率、精确率、召回率、**宏 F1（macro F1）**。宏 F1 为逐类 F1 的算术平均，更适合评估类别不平衡数据（[10]），是主要指标。
- **主实验结果（Table 1，宏 F1）**：
  - **ODIR-5K**：EfficientNetV2 上 LMF 达 **62.94**（交叉熵 60.34，+2.6），ResNet50 上 **57.73**（交叉熵 55.79，+1.94）；论文表述为"超过 2.5% 的提升"。
  - **HAM-10K**：EfficientNetV2 上 LMF 达 **84.61**（交叉熵 81.85），ResNet50 上 **82.43**（交叉熵 79.95）；论文表述为"近 3% 的提升"。
  - **ISIC-2019**：提升最显著。EfficientNetV2 上 LMF 达 **80.15**（论文表述"近 5% 提升"；vs Focal 71.73 即 +8.4，vs 交叉熵 75.46 即 +4.7，vs LDAM 78.50 即 +1.65）；ResNet50 上 LMF 达 **77.68**，论文称"相比其他方法近 10% 提升"——该 10% 是对照交叉熵 68.42（+9.26）/ Focal 70.60（+7.08）得出，对照最强基线 LDAM 75.64 时为 +2.04。
  - 其他指标（准确率/精确率/召回率）上 LMF 几乎在所有情形取得最佳（Table 1）。
- **类级别分析（Table 2，EfficientNetV2，针对训练样本 <200 的类）**：
  - ODIR：类 H 训练样本仅 **90**，LMF 宏 F1 **28.57**（交叉熵 8.33 / Focal 13.33 / LDAM 13.79，显著领先）；类 M 训练样本 **162**，LMF **91.89**（提升超 5%）。
  - HAM：最少类 DF 训练样本 **81**，LMF **80.00**（交叉熵 71.43，约 +9%）。
  - ISIC：最少类 DF 训练样本 **167**，LMF **78.26**，最强基线 LDAM 仅 73.85。
- **可解释性可视化**：用 **Grad-CAM（[11]）** 对 HAM-10K 单样本生成注意力图（Fig. 2），LMF 训练的模型注意力区域更大更相关，并在该 AKIEC 样本上唯一预测正确（Focal/LDAM 误判为 BKL）。
- **消融实验**：PDF 文本未给出针对 $\alpha$、$\beta$ 超参数的系统消融（仅说"trial and error 取相同权重"）。
- **泛化实验**：在眼科（ODIR）与皮肤科（HAM、ISIC）两类、三套独立数据集上均一致提升，作为泛化能力的证据。
- **速度/参数量/FLOPs**：PDF 文本未提及 LMF 引入的额外计算开销或参数/速度变化。

## 局限

1. **超参数缺乏系统分析**：$\alpha$、$\beta$（及 Focal 的 $\gamma$、LDAM 的 $C$）均为需调超参；论文仅凭试错取等权，无系统调参曲线或指导，复现与迁移存在不确定性。
2. **任务范围有限**：实验仅覆盖三个医学**图像分类**数据集；对分割、检测等其他医学任务（作者在结论中将其列为未来工作）或自然图像不平衡是否同样有效尚待验证。
3. **机制解释偏浅**：给出了线性组合公式，但对"为何"这两种损失线性叠加有效、二者在训练动态中如何相互作用，缺乏理论推导或量化分析（Grad-CAM 仅为单样本定性展示）。
4. **计算开销未讨论**：混合损失相对单一损失是否增加成本，论文未提。
5. **个别结果非单调**：从 Table 2 可见 LMF 并非在每个类都最优（如 ODIR 类 A、VASC 在 EfficientNetV2 上 LMF 低于部分基线），整体提升与逐类提升存在权衡，论文未深入讨论这一点。

## 个人评论

1. **设计范式的启发**：把两种针对不同维度（样本难度 vs. 类别分布）的损失做简单线性组合即可产生协同、超越单一方法，是一条低成本但有效的思路，启发后续探索更多损失的组合或自适应加权。
2. **聚焦真实痛点**：直面医学影像的类别不平衡，而非在理想平衡集上做研究，具备明确的临床辅助诊断落地价值。
3. **实验较为扎实**：三套独立、领域不同的公开数据集 + 两个骨干（ResNet50 / EfficientNetV2），结论一致，并辅以逐类分析与 Grad-CAM 可视化，说服力较强。
4. **对极少数类的价值突出**：专门分析 <200 样本的类，ODIR 类 H（90 样本）从 8.33 跃升到 28.57、HAM DF（81 样本）达 80.00，这类极端少数类的提升对识别罕见病最有意义。
5. **保留的疑问**：等权组合是否最优、$C$/$\gamma$ 的取值敏感性、相对单损失的训练成本，以及为何 ISIC 上 ResNet50 提升远大于 EfficientNetV2，论文都未给出解释，是后续值得补的实验。

### 使用建议

- **如果快速了解**：读**摘要**、**引言末尾的贡献列表**与**结论**即可。
- **如果复现**：重点看**方法 2.1/2.2/2.3 的三条公式**与**实验设置 3.1/3.2**（数据集划分 70:15:15、224×224、ImageNet 预训练的 ResNet50/EfficientNetV2）；$\gamma=1.5$、$\alpha=\beta$ 为关键设定。
- **如果借鉴创新点**：学习其"**混合损失**"范式（公式 3），思考把针对长尾、噪声标签等其他问题的损失与现有损失组合，或设计自适应加权而非固定等权。
- **如果写 related work**：归入"**处理类别不平衡的损失函数设计**"，与 Focal Loss、LDAM Loss、类平衡损失等并列。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[A2_医学图像_分类_配准_生成]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**医学图像分析中的类别不平衡分类**方向，核心是一个新的训练损失函数（不改网络结构）。任务面是医学影像的多类分类（眼科 ODIR、皮肤科 HAM/ISIC），方法面是损失函数设计。因此最贴切的主题是 **A2_医学图像_分类_配准_生成**（医学图像分类）。原归类的"B_注意力算子模块"并不准确：论文未提出任何注意力算子/模块，仅在结果中用 Grad-CAM 做了一次事后注意力图可视化，把"损失引导模型关注难样本"类比为注意力是过度引申，故本次将主题改正为 A2。

## 2. 一句话总结
本文提出大边缘感知焦点损失（LMF Loss），将 Focal Loss 与 LDAM Loss 线性等权组合（$L_{LMF}=\alpha L_{LDAM}+\beta L_{FL}$），在训练中同时按样本难度与类别分布加权，从而在三个不平衡医学影像数据集上较交叉熵/Focal/LDAM 基线取得 2%–10% 的宏 F1 提升。

## 3. 背景与问题
- **为什么要做**：医学影像数据集普遍类别不平衡（罕见病样本远少于常见病），使神经网络偏向多数类、少数类表现差，限制其作为辅助诊断工具落地。
- **之前方法的不足**：
  - **数据中心**（过采样/欠采样）：[3,4] 指出并非总可行。
  - **加权交叉熵**（[5]）：类别权重固定，不随样本难度调整。
  - **Focal Loss**（[6]）：按样本难度动态加权、关注难样本，但不显式建模类别先验分布。
  - **LDAM Loss**（[9]）：按类别样本数给少数类更大边缘做正则，但不显式按单样本难度加权。
- **核心矛盾/假设**：难样本关注（Focal）与类别分布正则（LDAM）是两条互补但此前未被联合的路线，作者假设二者同时使用更有效。

## 4. 核心贡献
1. 提出混合损失 LMF（公式 3），单框架内联合"难样本关注"与"类别分布正则"。
2. 在 ODIR-5K、HAM-10K、ISIC-2019 三个数据集上做大量实验，宏 F1 提升 2%–10%。
3. HAM 上某类（DF，81 训练样本）以 <90 样本达 80% F1，较其他方法约 +9%。

## 5. 方法详解
- **整体框架**：纯损失函数方法。ResNet50 / EfficientNetV2（ImageNet 预训练）做分类骨干，仅替换训练损失为 LMF。
- **输入输出**：Focal 分支用正确类概率 $p_t$，LDAM 分支用各类 logits $z_j$ 与类别样本数 $n_j$；输出标量损失。
- **三条公式**：
  1. Focal：$FL(p_t)=-(1-p_t)^\gamma\log(p_t)$（公式 1），$\gamma=1.5$；$\gamma=0$ 退化为交叉熵。
  2. LDAM：类别相关边缘 $\Delta_j=C/n_j^{1/4}$，$u=e^{z_y-\Delta_y}$，$L_{LDAM}=-\log\frac{u}{u+\sum_{j\neq y}e^{z_j}}$（公式 2）。
  3. LMF：$L_{LMF}=\alpha L_{LDAM}+\beta L_{FL}$（公式 3），等权（$\alpha=\beta$）。
- **训练**：70:15:15 划分且保持逐类分布一致；图像 224×224；迁移学习。其余优化细节 PDF 未明确。
- **与已有差异**：Focal 只看难度、LDAM 只看分布，LMF 同时利用两者。

## 6. 实验与结果
- **数据集**：ODIR-5K（8 类，6392）、HAM-10K（7 类，10015）、ISIC-2019（8 类，25331）。
- **基线**：交叉熵、Focal、LDAM。指标：准确率/精确率/召回率/宏 F1（主指标）。
- **整体（Table 1，宏 F1）**：
  - ODIR：EffNetV2 62.94 / ResNet50 57.73（vs 交叉熵 60.34 / 55.79）。
  - HAM：EffNetV2 84.61 / ResNet50 82.43（vs 交叉熵 81.85 / 79.95，约 +3%）。
  - ISIC：EffNetV2 80.15（论文"近 5%"）/ ResNet50 77.68（论文"近 10%"——该 10% 系对照交叉熵 68.42、Focal 70.60 得出；对照最强基线 LDAM 75.64 为 +2.04）。
  - 准确率/精确率/召回率上 LMF 几乎全场最优。
- **类级别（Table 2，EffNetV2，<200 样本类）**：ODIR 类 H（90）8.33→28.57、类 M（162）→91.89；HAM DF（81）→80.00（vs 交叉熵 71.43）；ISIC DF（167）→78.26（vs 最强基线 LDAM 73.85）。
- **可解释性**：Grad-CAM（[11]）单样本注意力图（Fig. 2），LMF 注意力更聚焦且唯一预测正确（AKIEC，基线误判为 BKL）。
- **消融**：未做 $\alpha/\beta$ 系统消融。**开销**：未报告 FLOPs/参数/速度。

## 7. 这篇论文真正有价值的地方
1. 以最低工程成本（换损失、不改结构）取得跨数据集一致提升，组合范式可迁移。
2. 直击医学影像类别不平衡这一真实临床痛点。
3. 三数据集 + 双骨干 + 逐类分析 + Grad-CAM，验证较完整。
4. 对极端少数类（<100 样本）有显著拉升，对罕见病识别价值大。

## 8. 局限与问题
1. $\alpha/\beta/\gamma/C$ 均靠试错，无系统调参分析。
2. 仅验证图像分类，未及分割/检测或自然图像（分割被列为未来工作）。
3. 机制解释偏浅，Grad-CAM 仅单样本定性。
4. 计算开销未讨论。
5. 逐类结果非全优（部分类 LMF 低于基线），整体与逐类的权衡未深入。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 贡献列表 + 结论。
- **复现**：方法三公式 + 实验设置（70:15:15、224×224、ResNet50/EfficientNetV2、$\gamma=1.5$、$\alpha=\beta$）。
- **借鉴**：学其"混合损失"范式，尝试自适应加权或与处理长尾/噪声标签的损失组合。
- **写 related work**：归入"类别不平衡损失函数设计"，与 Focal/LDAM/类平衡损失并列。

## 10. 和其他论文的关系
- **直接相关（本文的两个组成基石）**：
  - `[[Focal Loss for Dense Object Detection]]`（[6]，公式 1 来源）。
  - `[[Learning Imbalanced Datasets with Label-Distribution-Aware Margin Loss]]`（[9]，公式 2 来源）。
- **同主题相关**：A2_医学图像_分类_配准_生成 下其他医学图像分类工作；处理数据不平衡的其他路线（重采样、数据增强、两阶段训练、代价敏感学习 [5] 等）。
- **工具相关**：Grad-CAM（[11]）用于可解释性可视化。

## 11. 关键词
类别不平衡, 医学图像分类, 损失函数, Focal Loss, LDAM Loss, LMF Loss, 混合损失, 宏 F1, 少数类, 难样本加权, 边缘正则, ODIR/HAM/ISIC

## 12. 可信度说明
本笔记基于 PDF 提取文本（4/4 页，含摘要、引言、方法、实验设置、结果与讨论、结论、Table 1/2 及参考文献）撰写，关键公式、数据集规模、宏 F1 数值与逐类样本数均能在提取文本中核对。已修正原笔记的若干事实错误：(a) 题目由误取的作者行（"AbuAdnanSadi2..."）改为真实题目 "LMFLoss: A Hybrid Loss for Imbalanced Medical Image Classification"；(b) 年份由 2019 改为 2022（arXiv:2212.12741v1, 2022-12-24）；(c) 补全单位信息；(d) 主题由 B_注意力算子模块 改正为 A2_医学图像_分类_配准_生成。公式 2 分母指数项因提取文本 OCR 变形，按 LDAM 标准形式给出并已标注。论文未明确的信息（优化器/学习率/训练轮数、$\alpha/\beta$ 消融、计算开销）均已注明"PDF 文本未明确"。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 4/4 页全覆盖); 来源缓存: `.paper-cache/extracts/LMFLoss.txt` (4/4 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro); 本轮人工优化复读已据提取文本核对并修正题目/年份/单位/主题等事实。
<!-- AI_READING_NOTE_END -->
