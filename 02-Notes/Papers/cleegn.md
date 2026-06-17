---
title: "CLEEGN: A Convolutional Neural Network for Plug-and-Play Automatic EEG Reconstruction"
authors:
  - "Pin-Hua Lai"
  - "Bo-Shan Wang"
  - "Wei-Chun Yang"
  - "Hsiang-Chieh Tsou"
  - "Chun-Shu Wei"
year: 2024
venue: "arXiv (eess.SP)"
doi: 
pdf: [[cleegn.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
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
extract_cache: .paper-cache/extracts/cleegn.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/14 pages"
---
# CLEEGN: A Convolutional Neural Network for Plug-and-Play Automatic EEG Reconstruction

## 基本信息
- **PDF**: [[cleegn.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | CLEEGN: A Convolutional Neural Network for Plug-and-Play Automatic EEG Reconstruction |
| **作者** | Pin-Hua Lai; Bo-Shan Wang; Wei-Chun Yang; Hsiang-Chieh Tsou; Chun-Shu Wei (National Yang Ming Chiao Tung University, NYCU, Taiwan) |
| **发表时间** | 2024 (arXiv:2210.05988v2, 21 Feb 2024) |
| **刊物/会议** | arXiv (eess.SP); 排版为 IEEE 期刊模板 |
| **DOI** | 未明确 (arXiv:2210.05988) |

## 摘要

清理后的英文原摘要 (修复空格与连字符断裂, 剔除杂入文字):

> Human electroencephalography (EEG) is a brain monitoring modality that senses cortical neuroelectrophysiological activity at high temporal resolution. One of the greatest challenges posed in applications of EEG is the unstable signal quality that is susceptible to inevitable artifacts during recordings. To date, most existing techniques for EEG artifact removal and reconstruction are applicable to offline analysis solely, or require individualized training data to facilitate online reconstruction. We have proposed CLEEGN, a novel light-weighted convolutional neural network for plug-and-play automatic EEG reconstruction. CLEEGN is based on a subject-independent pre-trained model using existing data and can operate on a new user without any further calibration. The performance of CLEEGN was validated using multiple evaluations including waveform observation, reconstruction error assessment, and decoding accuracy on well-studied labeled datasets. The results of simulated online validation suggest that, even without any calibration, CLEEGN can largely preserve inherent brain activity and outperforms leading artifact removal methods in the decoding accuracy of reconstructed EEG data. In addition, visualization of latent features reveals the model's behavior and the intriguing process of artifact removal in EEG data. We foresee pervasive applications of CLEEGN in prospective works of online plug-and-play EEG decoding and analysis.

中文翻译:

> 人类脑电图 (EEG) 是一种以高时间分辨率监测大脑皮层神经电生理活动的脑监测手段。EEG 应用中最大的挑战之一, 是其信号质量不稳定, 在记录过程中极易混入不可避免的伪影。迄今为止, 多数现有的 EEG 伪影去除与重建技术要么仅适用于离线分析, 要么需要个体化训练数据才能实现在线重建。我们提出了 CLEEGN——一种用于即插即用 (plug-and-play)、自动 EEG 重建的轻量级卷积神经网络。CLEEGN 基于利用已有数据训练的"被试无关"预训练模型, 可在新用户身上直接运行而无需任何额外标定。CLEEGN 的性能通过多种评估方式得到验证, 包括波形观察、重建误差评估, 以及在公认标注数据集上的解码准确率。模拟在线验证的结果表明, 即使没有任何标定, CLEEGN 也能在很大程度上保留固有的大脑活动, 并在重建 EEG 数据的解码准确率上超越领先的伪影去除方法。此外, 对潜在特征的可视化揭示了模型的行为以及其在 EEG 中去除伪影的有趣过程。我们预期 CLEEGN 将在在线即插即用 EEG 解码与分析的后续工作中获得广泛应用。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: EEG 信号即便在受控实验室、训练有素且尽量保持身体静止放松的被试身上, 也会被不可避免的行为与生理伪影污染——眼动 (eye blinks)、反射性肌肉运动 (muscle)、眼电 (ocular)、心电 (cardiac) 等。这些伪影来源多样且非平稳, 难以完全识别和追踪, 噪声消除与伪影去除一直是 EEG 信号处理与解码的主要难题, 直接影响下游分析 (如 BCI 解码) 的准确性。
- **之前方法的问题** (论文按 filter-based / domain-based / NN-based 三类组织):
    1.  **滤波器类 (filter-based)**: 数字滤波器、自适应滤波。低计算成本、可解释, 但无法处理 EEG 与伪影的频谱重叠; 自适应滤波还需额外 EOG/EMG/ECG 辅助电极, 不方便。
    2.  **域分解类 (domain-based)**: EMD、小波 (WT)、CCA、ICA、ASR 等, 把信号变换到分量域分离伪影。比滤波器更主流, 但性能高度依赖用户设定的超参数与判据 (如小波母函数、EMD 停止准则、CCA 自相关阈值、ASR 截断参数 k), 且 ICA/EMD 常需人工逐分量判断是脑活动还是伪影; 多数仅适用于离线, 在线表现不佳。混合方法 (w-ICA、EEMD-ICA、EEMD-CCA 等) 性能更好但需更复杂的人工调参。
    3.  **神经网络类 (NN-based)**: 近年方法 (深度卷积自编码器 [28]、Bayesian DL+ICA [31]、1D-ResCNN [29]、IC-U-Net [33] 等) 能自动去伪影且性能更好, 但多数**在合成数据上验证** (将预设"干净"EEG 与噪声手工混合), 与真实场景有差距; 且很少同时满足真实数据有效性与支持实时处理的**计算高效性**这两条现实部署标准。
- **核心矛盾**: 在线实时 EEG 分析/解码迫切需要**自动化、零标定、高泛化**的去噪方法, 而现有方法或依赖人工干预、或需要个体化训练、或仅在合成数据上有效。论文明确指出: 此前没有工作同时满足"真实世界 EEG 重建"的双重标准 (有效性 + 计算高效性)。

## 关键贡献

论文原文明确写明贡献为 **three-fold (三点)**:

1.  **提出 CLEEGN 架构**: 一个轻量级编码器-解码器卷积神经网络, 能实现全自动、端到端的 EEG 重建。
2.  **优越性能**: 在增强 EEG 信号质量上优于领先的在线与离线方法, 以**提升的解码准确率**为证据。
3.  **被试无关训练框架**: 引入利用**离线参考去噪方法**生成训练数据的框架, 实现被试无关训练, 达成**零标定、即插即用**的 EEG 重建。

> 注: 原笔记列出的第 4 点"模型行为分析 (潜在特征可视化)"出自摘要 ("visualization of latent features reveals the model's behavior"), 是论文的一项内容, 但**并未**被作者列入正式的三点贡献清单, 此处不再算作独立贡献。

## 方法

- **整体框架**: CLEEGN 是**编码器-解码器**卷积网络 (见图 1 与表 I), 把多通道含噪 EEG `X` 映射到潜在空间再重建为去噪 EEG。训练目标是让输出逼近由传统离线方法生成的参考信号 `Ỹr` (公式 (1): `arg min_ϕ E{‖Ỹr − CLEEGN_ϕ(X)‖²₂}`, 即最小化 MSE)。编码器设计受一个已有 EEG 识别 CNN 模型 [25] 启发 (即 EEGNet 风格的时空卷积块)。
- **网络结构 (表 I, 提取文本可核)**:
    - **输入**: `(B, 1, C, T)`; `B` 批大小, `C` 通道数, `T` 时间窗采样点数。
    - **编码器**: ①Conv2D, `C` 个 `(C,1)` 空间滤波器 → 输出 `(B, C, 1, T)`, 提取通道间空间相关性; ②Permute (交换前两维) → `(B, 1, C, T)`; ③BatchNorm; ④Conv2D, `NF` 个 `(1, ⌊fs×0.1⌋)` = `(1, ⌊fs/10⌋)` 时间滤波器 → `(B, NF, C, T)`, `fs` 为采样率; ⑤BatchNorm。
    - **解码器** (与编码器近似对称, 三个卷积块): ①Conv2D, `NF` 个 `(1, ⌊fs/10⌋)` 时间核 + BN; ②Conv2D, `C` 个 `(C,1)` 空间核重建空间信息 + BN; ③Conv2D, 1 个 `(C,1)` 核映射回时域 → `(B, 1, C, T)`。
    - 除编码器第一层外, 所有卷积层用**零填充**保持输入输出尺寸一致, 每个卷积层后接**批归一化**以稳定梯度。
- **参考去噪方法的选择 (B 节)**: 噪声-干净训练对有两类生成方式: (1) 用干净 EEG + 生理噪声**合成** [28]–[30], 量大但存在"无法完美标注干净段""不同生理噪声与脑活动交互未知"两大隐患, 难直接迁移到真实数据; (2) 用**传统去噪方法处理真实记录** [31]–[33]。本文采用第二种, 因其更贴近真实应用场景。具体用的传统方法是 **ICA (配 ICLabel 自动标注 7 类成分: brain/eye/heart/muscle/line noise/channel noise/other)** 与 **ASR (基于 PCA, 用截断参数 k 剔除高方差伪影成分)**。ICA+ICLabel 与不同 k 的 ASR 都能自动生成训练对, **以解码性能最好者作为最终参考方法**。
- **训练 (C 节)**:
    - `X = Y + N` (观测 = 真信号 + 噪声); 因无法完美分离, 用离线伪影去除方法产出 `Ỹr` 近似 `Y`。
    - 因实验时长达数分钟, 不直接用整段训练; 用**滑动窗口**切成 `(C, T)` 的 epoch, 窗长 `T`、步长 `0.5T` (即 50% 重叠)。
    - 切分前对每个通道独立做**自适应 z-归一化** (均值/标准差由 noiseless 段计算)。
    - **被试无关 (留一被试) 训练**: 把数据按被试分成 `k` 个不相交集合, 每次留出 1 个集合做测试, 该测试集被试数据不参与训练与验证; 单个数据集会得到 `k` 个模型, 用留出集评估去伪影性能。
- **推理**: 训练好后, 新用户原始 EEG 直接输入即可输出去噪信号, 无需对该用户再训练或调参 (即插即用、零标定)。

## 实验

- **数据集**:
    1.  **合成多元时间序列**: 8 个时域源 `s1(t)..s8(t)`, 每个时长 100 s、采样率 1000 Hz (`s1` 随机大幅噪声, `s2`/`s3` 为 8 Hz / 25 Hz 正弦, `s4` 均匀分布随机, `s5`/`s6` 复合周期函数, `s7`/`s8` 两种密度方波)。随机混合矩阵 `A ∈ R^{8×8}, A~U(0,1)`, 观测 `X = AS + ϵ` (`ϵ` 为 `N(0, 0.01)` 微扰)。设 3 种"期望源/伪影源"划分场景 (scenario-1/2/3), 参考信号由仅投影期望源得到。用于初步理解模型行为。
    2.  **BCI-Challenge (ERN)**: Kaggle inria-BCI-Challenge 数据集, 共 26 名被试 (16 标注 + 10 未标注), 本文**使用 16 名标注被试**; P300 拼写任务, ERN 在错误反馈后约 350 ms 出现大负波、约 500 ms 出现正波。原始采样率 200 Hz、56 个 passive Ag/AgCl 电极。预处理: 降采样到 **128 Hz**、CAR 共平均参考、FIR 带通 **1–40 Hz**; 解码时取 [0, 1.25] s epoch 区分正确/错误反馈。
    3.  **MAMEM-SSVEP-II (SSVEP)**: 11 名被试, 5 个刺激频率 (6.66 / 7.50 / 8.57 / 10.00 / 12.00 Hz), 每人 5 个 session、每 session 25 trials; 采集设备为 256 通道 HydroCel Geodesic Sensor Net、采样率 250 Hz。本文跨被试选取**公共 20 通道**训练, 降采样到 **125 Hz**、CAR、带通 1–40 Hz, 取 [1, 5] s epoch。用于检验泛化能力。
- **解码评估模型**: 据 p.14 提取线索, 下游解码用 **EEGNet** ("E. Decoding Performance Evaluation Model: EEGNet")。
- **对比方法 / 基线**: 独立的 ICA、ASR 及其变体 (不同 k 的 ASR)——它们既是生成参考数据的来源, 也是被对比的基线 (在线 + 离线方法)。
- **评价指标**: ①波形观察 (目视保真度); ②重建误差 (MSE); ③**下游解码准确率** (ERN/SSVEP 分类), 这是衡量去噪是否保留有用脑活动信息的最关键指标。
- **主结果**: 合成数据上模型能有效分离"脑活动"源与噪声源; 真实数据上模拟在线验证显示, **零标定的 CLEEGN 在解码准确率上优于用来生成其训练数据的传统方法 (ICA/ASR) 本身**, 在 BCI-Challenge (ERN) 与 MAMEM (SSVEP) 上均有提升。
- **具体数值**: 提取缓存只覆盖到第 5 页 (截断于 MAMEM 预处理), **未含结果表/图的具体准确率数字**; 据原文后续页应有 ERN/SSVEP 的定量对比与 SSVEP 分类实验结论 (p.14 线索 "for the SSVEP classification, an experimental result showed ..."), **提取缓存未覆盖, 待核**。
- **消融**: 提取文本未明确给出针对网络深度/卷积核大小的系统消融。
- **效率**: 论文反复强调"light-weighted", 但提取文本**未明确**给出参数量、FLOPs 或处理速度等数字。

## 局限

1.  **对参考方法质量的依赖**: 性能上限受限于生成 `Ỹr` 的传统去噪方法 (ICA/ASR) 质量; 参考方法失效的场景, 模型也可能学不到正确映射。论文 B 节自陈"目前没有方法能完美标注干净 EEG 段", 这一不确定性被继承进训练标签。
2.  **伪标签假设的简化**: 训练隐含假设传统方法能提供足够好的"伪标签"; 模型能超越参考方法, 但仍依赖参考方法至少提供部分正确信息。
3.  **数据集规模与多样性**: 主要在 BCI-Challenge、MAMEM 两个常见公开数据集上验证, 在更复杂、噪声更丰富的真实场景 (如移动 BCI) 中的效果有待验证。
4.  **实时性未量化**: 虽声称轻量、适合在线, 但提取文本未提供明确的延迟/计算效率数据, 实时部署可行性需自行验证。

## 个人评论

1.  **训练数据生成策略最具启发**: 它不纠结于获取"绝对干净"的 EEG, 而是把**现有但不完美的离线去噪方法 (ICA/ASR) 的输出当作训练目标**——并配合"以解码性能最好的参考方法为目标"这一选择策略。这种"站在巨人肩膀上"的弱监督思路, 既复用了传统方法的知识, 又让网络学到更优映射, 最终在解码准确率上反超教师方法, 很有工程智慧。
2.  **零标定的实现路径清晰**: 用被试无关 (留一被试) 预训练克服新用户标定难题, 为需要快速部署的 BCI 系统提供了可落地方案。
3.  **评估范式抓住本质**: 不只用信号 MSE, 更以**下游 EEGNet 解码准确率**为核心指标——去噪的目的不是让信号"看起来"干净, 而是保留对任务有用的脑活动信息。这一评估取向值得其他信号去噪任务借鉴。
4.  **可改进处**: 论文对"为何 CLEEGN 能超越其教师 (ICA/ASR)"的机理解释偏定性 (依赖潜在特征可视化); 若能给出更可量化的归因, 说服力会更强。

### 使用建议

- **如果快速了解**: 读摘要、引言末尾的三点贡献、实验主结果总结即可掌握核心。
- **如果复现**: 重点读 III. Materials and Methods——A. Model Architecture (表 I 给出精确结构) 与 C. Model Training (z-归一化、50% 重叠滑窗、留一被试)。注意参考方法 (ICA+ICLabel、ASR 的 k) 的具体实现, 以及用 EEGNet 做解码评估。
- **如果借鉴创新点**: ①用传统算法输出作为深度学习训练标签的弱监督思路; ②面向即插即用的被试无关预训练框架; ③以任务性能 (解码准确率) 为核心的评估体系。
- **如果写 Related Work**: 放在"基于深度学习的 EEG 伪影去除"小节, 对比"合成数据训练"与"需个体化训练"两类方法, 强调其"零标定"与"基于真实数据+参考方法"的特性 (与 IC-U-Net [33] 同属用 ICA 离线对训练、但 CLEEGN 更强调轻量与即插即用)。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页:
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇**脑机接口 (BCI) / 生物信号处理**方向的论文, 核心是 **EEG 信号的伪影去除与重建**。目标是用一个轻量级 CNN 实现自动、在线的 EEG 去噪, 且对新用户**无需任何标定或再训练**。注意: 它本质上不属于计算机视觉的任何具体子方向, 也**不涉及注意力机制**——原笔记 frontmatter 把它归入 `B_注意力算子模块` 是错误的串台 (论文从头到尾是标准时空卷积的编码器-解码器, 见表 I, 无任何 attention 算子)。在本库 taxonomy 下, 它最贴近"非 CV 通用"类, 故改归 `T_通用_NLP_其他`。

## 2. 一句话总结
本文提出 CLEEGN, 一个轻量级卷积编码器-解码器, 通过在通用数据集上以**传统离线去噪方法 (ICA/ASR) 的输出为参考信号做被试无关 (留一被试) 预训练**, 实现对新用户 EEG 的**零标定、即插即用、自动伪影去除与重建**, 并在 EEGNet 下游解码准确率上超越其参考方法本身。

## 3. 背景与问题
- **为什么要做**: EEG 即便在受控环境也会被眼动、肌电、眼电、心电等非平稳伪影污染, 难以完全识别追踪, 直接拉低 BCI 解码准确率。传统方法 (ICA/ASR/小波/EMD/CCA) 依赖人工调参或逐分量判断, 多为离线, 不满足实时自动化需求。
- **之前方法的问题**:
    1.  **合成数据训练的 DL 方法**: 用手工合成的"干净+噪声"对训练, 与真实噪声特性有差距, 泛化到真实 EEG 时性能可能下降。
    2.  **缺乏实用性**: 很少同时满足真实数据有效性与计算高效性这两条现实部署标准。
    3.  **需个体化训练**: 多数方法需为目标用户准备个体化数据, 不利于快速部署。
- **核心矛盾**: 在线实时 EEG 解码需要自动化、零标定、高泛化的去噪, 而现有方法或依赖人工干预、或需个体化训练、或仅在合成数据上有效。论文明确: 此前无工作同时满足"有效性 + 计算高效性"的双重标准。

## 4. 核心贡献 (原文 three-fold)
1.  **CLEEGN 架构**: 轻量级编码器-解码器 CNN, 全自动端到端 EEG 重建。
2.  **优越性能**: 以提升的下游解码准确率为证据, 优于领先的在线/离线伪影去除方法。
3.  **被试无关训练框架**: 利用离线参考去噪方法 (ICA/ASR) 生成训练数据, 实现零标定、即插即用。
> (摘要另提"潜在特征可视化揭示模型行为", 是论文内容但未列入正式三点贡献。)

## 5. 方法详解
- **目标函数**: 公式 (1), `arg min_ϕ E{‖Ỹr − CLEEGN_ϕ(X)‖²₂}`, 即输出与参考信号 `Ỹr` 的 MSE 最小化。`X=Y+N`, 因无法完美分离, 用离线方法的输出 `Ỹr` 近似真信号 `Y`。
- **网络 (表 I)**:
    - 输入 `(B,1,C,T)`。
    - 编码器: Conv2D `C×(C,1)` 空间滤波 → `(B,C,1,T)` → Permute → `(B,1,C,T)` → BN → Conv2D `NF×(1,⌊fs/10⌋)` 时间滤波 → `(B,NF,C,T)` → BN。
    - 解码器: Conv2D `NF×(1,⌊fs/10⌋)` + BN → Conv2D `C×(C,1)` 空间重建 + BN → Conv2D `1×(C,1)` 映射回时域 → `(B,1,C,T)`。
    - 除编码器首层外全部零填充保持尺寸; 每层后接 BN。编码器设计借鉴已有 EEG 识别 CNN ([25], EEGNet 风格)。
- **参考方法选择**: 用真实记录经传统方法 (ICA+ICLabel, ASR 不同 k) 自动生成噪声-干净对, **取解码性能最优者**为最终参考。ICLabel 把成分分 7 类 (brain/eye/heart/muscle/line/channel/other); ASR 用 PCA + 截断参数 k 剔除高方差伪影成分。
- **数据准备**: 滑动窗口切 `(C,T)` epoch, 窗长 `T`、步长 `0.5T` (50% 重叠); 切分前对每通道独立做自适应 z-归一化 (统计量来自 noiseless 段)。
- **被试无关训练**: 按被试分 `k` 个不相交集合, 留一集测试 (不进训练/验证), 得 `k` 个模型, 用留出集评估。
- **推理**: 新用户原始 EEG 直接前向即得去噪结果, 零标定、无再训练。

## 6. 实验与结果
- **数据集**: ①合成 8 源 (100 s, 1000 Hz; `X=AS+ϵ`, `A~U(0,1)`, `ϵ~N(0,0.01)`; 3 种期望/伪影源场景)。②BCI-Challenge ERN: 26 被试 (用 16 标注), P300 speller, 200 Hz/56 通道 → 降采样 128 Hz、CAR、带通 1–40 Hz, epoch [0,1.25] s。③MAMEM-SSVEP-II: 11 被试, 5 频率 (6.66/7.50/8.57/10.00/12.00 Hz), 256 通道 HCGSN/250 Hz → 选 20 通道、降采样 125 Hz、CAR、带通 1–40 Hz, epoch [1,5] s。
- **解码模型**: EEGNet (据 p.14 提取线索)。
- **对比/基线**: ICA、ASR 及其变体 (既是参考来源也是基线)。
- **指标**: 波形观察、重建 MSE、下游解码准确率 (最关键)。
- **结果**: 合成数据上能分离脑活动与噪声; 真实数据模拟在线验证下, **零标定 CLEEGN 的解码准确率超越其参考方法 ICA/ASR**, ERN 与 SSVEP 任务均有提升。
- **数值缺口**: 提取缓存截断于第 5 页, 未含结果表的具体准确率数字; 据原文后续页 (p.14 "for the SSVEP classification, an experimental result showed ...") 应有定量结论, **提取缓存未覆盖, 待核**。
- **消融/效率**: 提取文本未明确给出系统消融, 也未给参数量/FLOPs/速度数字 (尽管标榜 light-weighted)。

## 7. 这篇论文真正有价值的地方
1.  **弱监督的训练对生成策略**: 把不完美的离线方法输出当训练目标, 并以"解码性能最优的参考方法"为锚, 既复用传统知识又让网络学到更优映射, 最终反超教师方法——很有工程价值, 可迁移到其他信号去噪任务。
2.  **零标定路径**: 被试无关 (留一被试) 预训练直接解决新用户标定难题, 适合快速部署的 BCI。
3.  **以任务性能为核心的评估范式**: 用下游 EEGNet 解码准确率而非仅 MSE 评判去噪, 抓住了 EEG 去噪的真正目的——保留有用脑活动信息。

## 8. 局限与问题
1.  **依赖参考方法质量**: 性能上限受 ICA/ASR 质量约束; 参考方法失效场景模型也学不好。论文自陈"无法完美标注干净 EEG 段"。
2.  **伪标签假设简化**: 隐含假设传统方法提供足够好的伪标签; 反超依赖其至少部分正确。
3.  **数据多样性有限**: 主要在 BCI-Challenge、MAMEM 验证, 移动 BCI 等复杂场景待验证。
4.  **实时性未量化**: 声称轻量在线, 但提取文本无明确延迟/效率数字, 实时部署需自行验证。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 三点贡献 + 实验主结果。
- **复现**: 精读 III 章——表 I (精确结构)、C 节 (z-归一化、50% 重叠滑窗、留一被试)、B 节 (ICA+ICLabel/ASR 的 k 选择)、用 EEGNet 做解码评估。
- **借鉴创新点**: ①传统算法输出作弱监督标签; ②即插即用的被试无关预训练框架; ③以解码准确率为核心的评估体系。
- **写 Related Work**: 归入"基于深度学习的 EEG 伪影去除", 对比合成数据训练与个体化训练两类, 强调零标定 + 真实数据/参考方法特性; 与 IC-U-Net [33] (同用 ICA 离线对) 形成最直接对照。

## 10. 和其他论文的关系
CLEEGN 是标准时空卷积的编码器-解码器, **不采用注意力机制**, 故与"注意力模块设计"类论文无直接技术承袭——这也是把它移出 `B_注意力算子模块` 的依据。它与生物信号/EEG 去噪谱系关系更近: 与合成数据训练的深度自编码器 [28]、1D-ResCNN [29] 对照其"真实数据训练"取向; 与 IC-U-Net [33] 同属"用离线 ICA 制备训练对"路线, 但更强调轻量化与零标定即插即用。在本库中宜与其他生物信号处理 / BCI / 弱监督学习笔记互链。

## 11. 关键词
EEG, 伪影去除, 脑机接口 (BCI), 卷积神经网络, 编码器-解码器, 即插即用, 零标定, 被试无关训练, 信号重建, ICA, ICLabel, ASR, EEGNet, 弱监督, 跨被试泛化

## 12. 可信度说明
本精读**严格基于 PDF 提取文本** (12/14 页, 且因 25000 字符上限截断于第 5 页中段)。模型架构 (表 I)、训练目标 (公式 1)、参考方法选择 (B 节)、训练流程 (C 节)、数据集设置 (合成/BCI-Challenge/MAMEM 的被试数、通道、采样率、预处理) 均有明确文本依据。三点贡献按原文 "three-fold" 校正 (原笔记多列的第 4 点已降级说明)。BCI-Challenge"使用 16 标注被试"、MAMEM"256 通道设备选 20 通道""降采样 128/125 Hz、带通 1–40 Hz"等细节均来自提取文本。具体解码准确率数字因提取缓存截断而缺失, 仅作定性描述并标注"待核"; 解码模型为 EEGNet 来自 p.14 提取线索。计算效率 (参数量/FLOPs) 文本未给, 已说明。

---

> **可信度补充**: PDF 提取质量 = **high** (2086 字符/页), 但提取缓存因 25000 字符上限截断于第 5 页中段, 实验结果数值未覆盖; 来源缓存: `.paper-cache/extracts/cleegn.txt` (标注 12/14 页; 原 AI 主体 12/14 + 全文补读 13-14); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。本轮 (2026-06-18) 据提取文本重核并修正分类 (B_注意力算子模块 → T_通用_NLP_其他)、补题、订正贡献条数与数据集细节。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-14; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-14。
- **提取情况**: 缺失页 2 页, 其中 2 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核; `human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: CLEEGN, even without calibration, predominantly preserves
- p.13: EEG trials from different subjects demonstrate model behav-
- p.13: EEG reconstruction from existing techniques and surpasses
- p.13: We anticipate widespread applications of CLEEGN in future
- p.13: REFERENCES
- p.13: EMBS Conference on Biomedical Engineering and Sciences (IECBES) ,
- p.13: Artifact suppression with wavelet enhanced independent component
- p.13: A u-net-based denoising autoencoder using mixtures of independent
- p.14: COCOSDA held jointly with 2013 Conference on Asian Spoken
- p.14: 2012 IEEE International Symposium on Circuits and Systems (ISCAS) ,
- p.14: S136466130001545X
- p.14: APPENDIX A

### 缺失页关键摘录

- p.13: [12] M. Alam and B. Samanta, "Performance evaluation of empirical mode
- p.13: noisenet: A benchmark dataset for end-to-end deep learning solutions
- p.14: dataset, and website," NeuroImage , vol. 198, pp. 181–197, 2019.
- p.14: Language Research and Evaluation (O-COCOSDA/CASLRE) , 2013, pp.
- p.14: batch is fixed. Under our experiment, the result showed that the
- p.14: E. Decoding Performance Evaluation Model: EEGNet
- p.14: for the SSVEP classification, an experimental result showed
<!-- AI_READING_NOTE_END -->
