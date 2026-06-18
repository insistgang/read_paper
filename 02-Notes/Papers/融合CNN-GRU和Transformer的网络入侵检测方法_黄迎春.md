---
title: 融合CNN-GRU和Transformer的网络入侵检测方法
authors:
  - "黄迎春"
  - "邢秀祺"
year: 2025
venue: "火力与指挥控制"
doi: 10.3969/j.issn.1002-0640.2025.06.003
pdf: [[融合CNN-GRU和Transformer的网络入侵检测方法_黄迎春.pdf]]
primary_topic: T_安全_入侵检测
topics:
  - "T_安全_入侵检测"
status: ai-read
reading_stage: ai-complete
confidence: high
source_basis: pdf-text
date_added: 2026-06-05
rating: 
tags:
  - "paper"
ai_generated: true
human_reviewed: false
ai_generated_at: 2026-06-05
extract_cache: .paper-cache/extracts/融合CNN-GRU和Transformer的网络入侵检测方法_黄迎春.txt
---

# 融合CNN-GRU和Transformer的网络入侵检测方法

## 基本信息
- **PDF**: [[融合CNN-GRU和Transformer的网络入侵检测方法_黄迎春.pdf]]
- **primary_topic**: `T_安全_入侵检测`
- **topics**: `T_安全_入侵检测`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-05

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 融合CNN-GRU和Transformer的网络入侵检测方法 |
| **作者** | 黄迎春, 邢秀祺（通信作者）；沈阳理工大学信息科学与工程学院 |
| **发表时间** | 2025（收稿 2024-06-08，发表于《火力与指挥控制》2025, 50(6): 21-27） |
| **刊物/会议** | 火力与指挥控制（Fire Control & Command Control） |
| **DOI** | 10.3969/j.issn.1002-0640.2025.06.003 |
| **基金** | 国家自然科学基金（61971291） |

## 摘要

**清理后的英文原摘要**（据 PDF 提取文本整理，已修复空格与连字符断裂）：
> With the rapid development of network technology and its wide application in the military field, IDS is very important to the security of the system. To address the issue of class imbalance in traditional intrusion detection datasets, a network intrusion detection method called CNN-GRU Transformer (CGT) is proposed, which combines convolutional gated recurrent units (CNN-GRU) and a neural network model based on self-attention mechanism (Transformer). This method optimizes intrusion detection technology by addressing the drawbacks of bidirectional long short-term memory (LSTM) networks, which only consider temporal features while neglecting spatial features and have a large number of parameters. Additionally, the dataset is balanced using the NBW model (Neighbourhood-cleaning-rule Borderline-SMOTE WGAN), which combines over- and under-sampling with Wasserstein generative adversarial networks. The experimental results demonstrate that the proposed method exhibits promising performance on the NSL-KDD dataset, effectively enhancing intrusion detection performance.

**中文翻译**：
> 随着网络技术的快速发展及其在军事领域的广泛应用，入侵检测系统（IDS）对系统安全起着重要作用。针对传统入侵检测数据集的类别不平衡问题，本文提出一种融合卷积门控循环单元（CNN-GRU）与基于自注意力机制的神经网络（Transformer）的网络入侵检测方法 CGT（CNN-GRU Transformer）。该方法针对双向长短期记忆网络（BiLSTM）只考虑时序特征、忽略空间特征且参数量大的缺点进行优化；同时采用融合过采样-欠采样与 Wasserstein 生成对抗网络（WGAN）的数据平衡处理模型 NBW（Neighbourhood-cleaning-rule Borderline-SMOTE WGAN）对数据集进行平衡处理。实验结果表明，所提方法在 NSL-KDD 数据集上表现良好，有效提升了入侵检测性能。
>
> 关键词：入侵检测；卷积门控循环单元；数据平衡处理；邻域清理规则；神经网络
>
> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：网络技术快速发展并在军事领域、物联网（IoT）中广泛应用，网络攻击越来越频繁、复杂，新型攻击不断涌现。入侵检测系统（IDS）通过主动防御检测入侵并及时响应，是保护网络安全亟待解决的问题。IDS 分为网络入侵检测系统（NIDS，监视网络流量）与主机入侵检测系统（HIDS，监视单机活动）。传统基于机器学习（贝叶斯、SVM 等）的 NIDS 在提取深层特征上能力有限，深度学习（DL）因强大的特征提取能力被引入 IDS。
- **核心痛点——类别不平衡**：基于 DL 的 NIDS 仍存在较高假阳率，重要原因是数据集类别不平衡。现实网络中正常流量占多数、异常流量较少，分类模型更关注多数类，忽略少数类攻击；但对 NIDS 而言，正确检测少数类攻击同样至关重要（如 NSL-KDD 中 U2R 训练样本仅 52 个）。
- **之前方法的问题**：
    - 文献[12]结合随机欠采样与 SMOTE 过采样预处理 CICIDS2017，但采样不稳定可能丢失多数类重要信息；
    - 文献[13]用 Nearmiss-1 欠采样 + SMOTE 过采样，但未考虑 SMOTE 易产生边缘分布问题的缺陷；
    - BiLSTM 主要依赖 LSTM 的记忆能力捕捉序列长期依赖，但忽略空间特征、对短期依赖敏感性较低；相比之下 CNN 擅长提取局部特征，GRU 相较 LSTM 减少约 40% 参数、提升计算效率。
- **核心矛盾**：需要一种既能有效平衡少数类与多数类数据（避免信息丢失和边缘分布问题），又能同时高效提取空间特征与时序特征、并捕获特征间全局关联的入侵检测方法。

## 关键贡献

1.  **提出 NBW（Neighbourhood-cleaning-rule Borderline-SMOTE WGAN）数据平衡模型**：融合 NCR 欠采样、Borderline-SMOTE 过采样与 WGAN，能自动学习少数类分布、避免生成数据造成边缘分布问题，生成更合理、多样的攻击类样本。
2.  **设计 CNN-GRU 特征提取模块**：将 CNN 与 GRU 并行结合——CNN 通过两个卷积层（各接 BatchNorm + ReLU）提取局部空间特征，两层 GRU 捕捉时序依赖，同步提取空间与时序信息；GRU 相比 LSTM 减少约 40% 参数。
3.  **改进 Transformer 模块并融合**：仅使用 Transformer 的编码部分，修改部分参数以适应一维信号数据；前馈网络隐藏层神经元数设为输入层两倍并采用 GELU 激活，通过多头注意力建立不同特征间的全局联系。
4.  **构建 CGT（CNN-GRU Transformer）端到端入侵检测模型**：将 NBW 数据平衡、CNN-GRU 特征提取、改进 Transformer 编码器与 MLP+Softmax 分类器整合，在 NSL-KDD 上验证。
5.  **实验验证有效性**：在二分类与五分类任务上，NBW+CGT 在准确率、召回率、F1 等指标上均优于未平衡数据训练的模型及 LR/KNN/DT/AB/RF/SVM 等经典模型。

## 方法

- **整体框架**（图1）：分为 **NBW 数据平衡处理** 与 **CGT 模型训练与推理** 两部分。原始训练集先经 NBW 生成平衡数据集，再输入 CGT 训练；测试集（KDDTest+）输入训练好的 CGT 推理。
- **输入输出**：
    - **输入**：网络流量样本的一维向量 X，每个样本由 **43 种特征** 构成（据原文 2.1 节，"每个样本由43种特征构成"）。
    - **输出**：二分类（正常/异常）或五分类（Normal, DOS, Probing, R2L, U2R）结果。
- **关键模块与连接**：
    1.  **NBW 数据平衡模块**（1.1 节）：
        - **流程**：原始数据 `(X, Y)` → **NCR 欠采样**（消除干扰分类的异常值/噪声）→ **Borderline-SMOTE 过采样**（仅对边缘的少数类样本即 Danger 区域合成新样本）→ 得到 `(X_{n,s}, Y)`。Borderline-SMOTE 将少数类样本划分为 Safe / Danger / Noise 三区，只对 Danger 合成。
        - **WGAN 增强**：从 `(X_{n,s}, Y)` 取真实少数类样本 `(X_r, Y_m)`，与随机噪声 `X_N` 一起对抗训练；噪声经生成器 Generator 生成伪数据 `X_fake`，用 `(X_r, Y_m)` 与 `X_fake` 迭代训练判别器与生成器；训练完成后生成器输出合成少数类样本 `(X_g, Y)`。
        - **损失函数**：WGAN 用 Earth Mover's Distance（EMD）替代传统 GAN 的 JS/KL 散度，减轻模式崩溃与梯度消失。判别器/生成器损失（式1、2）：
          `Loss(c) = (1/m)Σ f_w(x_i) − (1/m)Σ f_w(g_θ(z_i))`，`Loss(g) = (1/m)Σ f_w(g_θ(z_i))`，其中 g_θ 为生成器、f_w 为判别器，x_i 为真实数据、z_i 为噪声、m 为批大小。
        - **输出**：合并 `(X_{n,s}, Y)` 与 `(X_g, Y)` 得到平衡训练集 `Data`。
    2.  **CGT 特征提取与分类模块**：
        - **CNN-GRU 模块**（1.2 节）：一个包含两个卷积层的卷积块（每个卷积层后接 BatchNorm + ReLU）和两个相同 GRU 层并行。样本向量 X 一路经卷积块二次卷积提取**空间特征**；另一路在**时间维度转置**后输入 GRU 提取**时序特征**。两路输出特征图各自**降维后拼接（concat）**，送入 Transformer 模块。
        - **改进的 Transformer 编码器模块**（1.3 节）：仅用编码部分，含一个多头注意力机制与一个前馈网络。点积注意力：`Attention(Q,K,V) = softmax(QK^T / √d_K) V`（式3，d_K 为 Key 维度）；多头注意力 `MultiHead(Q,K,V) = concat(head_1,…,head_n) W^O`，各头 `head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)`（式4）。前馈网络隐藏层神经元数设为输入层两倍，激活函数为 GELU（式5）。
        - **MLP 分类模块**（1.4 节）：由两个全连接层和 1 个 Dropout 层组成；第 1 个全连接层用 ReLU 激活引入非线性，Dropout 置于全连接层之后防止过拟合、提升泛化；最后经 Softmax 回归输出各类别概率。
- **训练与推理**：
    - **实验环境**：AMD Ryzen 9 7945HX CPU、NVIDIA GeForce RTX 4060 GPU、Windows 11、PyCharm 2023，Python 3.6，PyTorch 1.8.1。
    - **超参数**（表4）：batch_size=64，learning_rate=0.001，Dropout=0.5，Input_dim=32，Attention_head=16，FeedForward_hidden_size=64，GRU_layer=2，CNN_kernel_size=3。使用 Adam 优化器（自动调节学习率）更新参数。
- **与已有方法的差异**：
    - 相比仅用 LSTM/BiLSTM 的模型，CGT 通过 CNN 显式提取空间特征，且 GRU 比 LSTM 少约 40% 参数；
    - 相比仅用 CNN 或仅用 Transformer 的模型，CGT 结合 GRU 的时序建模与 Transformer 的全局关系建模；
    - 相比传统 SMOTE 过采样，NBW 结合 WGAN 生成更真实、多样的少数类样本。
- **论文类型特化**：本文属**检测/分类类**方法。**backbone** 为 CNN-GRU 与 Transformer 编码器组合，**head** 为 MLP+Softmax。核心创新在于融合处理不平衡数据的预处理模块（NBW）与同时具备空间-时序-全局注意力特征提取能力的混合主干（CGT），解决入侵检测中**数据类别不平衡**与**多类型特征提取**两个关键问题。

## 实验

- **数据集**：**NSL-KDD**，含 KDDTrain+、KDDTest+、KDDTest-21、KDDTrain+_20Percent 四个子集。训练集用 **KDDTrain+_20Percent**（KDDTrain+ 的 20%，便于快速实验调试并保留代表性），测试集用 **KDDTest+（22,544 条）**；标签分 5 类。
    - **原始训练集分布（表1）**：Normal 13448(38.00%)、DOS 9234(26.10%)、Probing 11656(32.94%)、R2L 995(2.81%)、U2R **52(0.15%)**——严重不平衡。
    - **NBW 平衡后训练集（表2）**：Normal 13255(29.9%)、DOS 9062(20.44%)、Probing 11513(25.97%)、R2L 7000(15.79%)、U2R **3500(7.90%)**，总计 44330。少数类 R2L/U2R 被显著上采样。
- **对比方法**：经典模型 LR, KNN, DT, AB, RF, SVM，分别在**原始数据**与 **NBW 平衡数据**上训练，与 CGT、NBW+CGT 对比（黑体为最佳）。
- **评价指标**：准确率 Acc、查准率 Pre、召回率 Rec、F1（式6–9）；入侵类样本定义为正样本。
- **主实验结果**（表5）：
    - **数据平衡的有效性**：经 NBW 平衡后各模型性能普遍提升。例如 LR 二分类 Acc 72.8%→84.7%（提升约 12%），五分类 Acc 也提升约 3.2%。
    - **模型有效性**：NBW+CGT 表现最佳：
        - **二分类**：Acc **93.4%**，Rec **96.8%**，Pre 92.0%，F1 **94.3%**。次优 NBW+LR 的 F1 为 86.5%，提升约 7.8 个百分点。
        - **五分类**：Acc **82.5%**，Rec **65.5%**，Pre **79.1%**，F1 **69.1%**。次优 NBW+RF 的 F1 为 53.7%，提升约 15.4 个百分点。
        - 文中另举例：相对 SVM，CGT 的 Acc 与 F1 分别提高约 12.3% 和 12.8%（兼顾了 Acc 与 Rec 两个相互矛盾的指标）。
    - 值得注意：未加 NBW 的 CGT 单独跑五分类 Acc 已达 79.6%、Rec 78.8%（高于 NBW+CGT 的 Rec 65.5%），但其五分类 F1 仅 46.5%、Pre 56.8%；NBW 主要提升了 Pre 与整体 F1。
- **混淆矩阵分析（图3、图4）**：多数样本聚集对角线，性能较好。但图4显示 **U2R 类仅 41 个样本被正确检测，120 个 U2R 样本被误判为 Normal**——模型难以捕捉 U2R 攻击的特征模式；原因是 U2R 现实样本严重不足，NBW 生成的 U2R 仿真数据缺乏多样性，导致识别精度不足。
- **消融实验**：通过对比"未用 NBW 的 CGT"与"NBW+CGT"以及各经典模型在原始/平衡数据上的差异，间接证明 NBW 与 CGT 两个组件的有效性。**未提供移除单个子模块（去掉 GRU / Transformer / WGAN）的细粒度消融**。
- **泛化实验**：**仅在 NSL-KDD 上验证**，未在 CICIDS2017、UNSW-NB15 等其他数据集做泛化实验。
- **效率信息**：给出硬件环境与超参数，但**未提供参数量、FLOPs、训练/推理时间的定量比较**。

## 局限

1.  **U2R 类检测难题未根本解决**：即便用 NBW，多分类中 U2R 仍最差（图4：仅 41 正确、120 误判为 Normal）。对极稀缺（原始 52 样本）且特征复杂的攻击，单纯数据增强不足，生成样本缺乏多样性，仍需结合代价敏感学习、异常检测等策略。
2.  **实验不够全面**：仅在 NSL-KDD（源自 1999 年 KDD'99，相对老旧）上验证，未在更接近现代真实流量的数据集（CICIDS2017、UNSW-NB15）上验证泛化能力。
3.  **计算成本未探讨**：模型融合 CNN、GRU、Transformer、WGAN，结构相对复杂，但未讨论参数量、训练时间、是否适合实时检测等效率问题。
4.  **特征工程缺失**：结论明确"实验并未对样本的特征进行提取选择"，直接使用原始特征可能含冗余/不相关信息；作者将"设计轻量级模型挖掘特征以提升检测效率"列为下一步重点。
5.  **复现风险**：给出了部分超参数，但 WGAN 训练细节、NCR 与 Borderline-SMOTE 的具体阈值等关键实现细节不完整，精确复现有难度。

## 个人评论

1.  **"数据+模型"协同的系统性方案**：论文不只关注架构或只关注数据，而是把**数据平衡（NBW）**与**特征提取（CGT）**有机结合，针对类别不平衡入侵检测给出端到端方案，这种协同优化思路值得借鉴。
2.  **NBW 的分阶段融合逻辑清晰**：先用 NCR + Borderline-SMOTE 做"粗处理"提升数据质量并初步平衡，再用 WGAN 做"精生成"创造高质量、多样化的少数类样本；用 EMD 替代 JS/KL 散度缓解模式崩溃，为不平衡学习提供了具体范例。不过表2显示 U2R 仅扩到 3500，相对 Normal 的 13255 仍偏少，这也部分解释了 U2R 检测仍差。
3.  **混合特征架构的启示**：CNN-GRU 并行提取空间+时序特征、再用 Transformer 建模全局关系，充分利用不同网络优势，适合既有局部相关性又有序列依赖的网络流量数据，启发打破单一网络限制做模块组合。
4.  **指标解读需谨慎**：NBW+CGT 在 F1 上大幅领先，但表5也显示裸 CGT 的五分类 Rec（78.8%）高于 NBW+CGT（65.5%），说明 NBW 是以牺牲部分召回换取精确率与综合 F1；在"宁可误报不可漏报"的安全场景，这种权衡是否合适值得进一步分析——但论文未就此展开。

### 使用建议

- **快速了解**：读**摘要**、**图1（整体框架）**、**2.4 结果分析**与表5，即可掌握核心思想、方法与主要结论。
- **如果复现**：精读**第1章（1.1–1.4 各模块）**与**第2章**的参数设置（表4）和数据集描述（表1、表2）；NCR、Borderline-SMOTE、WGAN 的精确算法细节需查参考文献[14][15]等原文。
- **如果借鉴创新点**：
    - **数据平衡**：学习 NBW 如何融合传统采样与生成模型处理不平衡数据，可迁移到其他不平衡分类任务。
    - **模型架构**：CNN-GRU 并行提取时空特征 + Transformer 建模全局关系，可用于语音、传感器等时序任务。
- **写 related work**：可归入——基于深度学习的网络入侵检测；应对类别不平衡的入侵检测技术；Transformer 在安全领域的应用；CNN 与 RNN 的混合模型。

## 相关论文与链接

> - [[T_安全_入侵检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属网络安全领域的网络入侵检测（NID）方向，聚焦用深度学习解决传统 IDS 在数据类别不平衡下性能下降的问题。核心是提出融合"数据平衡处理（NBW）"与"混合特征提取（CGT = CNN-GRU + 改进 Transformer）"的端到端模型。论文发表于《火力与指挥控制》2025 年 50(6)（军工/指挥控制方向期刊，呼应摘要中"军事领域应用"），适合放在"网络安全-入侵检测"主题下，具体属"不平衡数据下的深度学习入侵检测方法"。

## 2. 一句话总结
本文提出 CGT（CNN-GRU Transformer）网络入侵检测方法：先用融合邻域清理规则、Borderline-SMOTE 与 WGAN 的 NBW 模型平衡不平衡数据集，再用 CNN-GRU 并行提取空间与时序特征、用改进 Transformer 编码器建模特征间全局关系，在 NSL-KDD 上显著提升了入侵检测性能。

## 3. 背景与问题
- **为什么要做**：网络技术在军事、IoT 中广泛应用，攻击日益频繁复杂；IDS 是主动防御关键。基于 DL 的 NIDS 仍有较高假阳率，重要原因是数据集类别不平衡——正常流量占多数、攻击流量少，模型偏向多数类、忽略少数类攻击（如 U2R），而少数类检测同样关键。
- **之前方法的问题**：随机欠采样 + SMOTE（文献[12]）采样不稳定易丢失多数类信息；Nearmiss-1 + SMOTE（文献[13]）未解决 SMOTE 的边缘分布缺陷；BiLSTM 只关注时序、忽略空间特征且参数多，CNN 擅长局部特征、GRU 比 LSTM 少约 40% 参数。
- **核心矛盾**：需同时做到（a）有效平衡数据且不引入信息丢失/边缘分布噪声，（b）同步提取空间+时序特征并捕获特征间全局关联。

## 4. 核心贡献
1.  **NBW 数据平衡模型**：NCR 欠采样 + Borderline-SMOTE 过采样 + WGAN 生成，自动学习少数类分布、避免边缘分布问题。
2.  **CNN-GRU 模块**：CNN（两卷积层 + BN + ReLU）提空间特征、两层 GRU 提时序特征，并行后降维拼接。
3.  **改进 Transformer**：仅用编码器，调参适配一维数据；前馈隐藏层为输入两倍、GELU 激活；多头注意力建全局关系。
4.  **CGT 端到端模型**：NBW + CNN-GRU + 改进 Transformer + MLP/Softmax 整合，NSL-KDD 验证。
5.  **实验有效性**：二/五分类上 NBW+CGT 在 Acc/Rec/F1 等指标优于未平衡数据训练的模型及经典 ML/DL 模型。

## 5. 方法详解
- **整体框架（图1）**：NBW 数据平衡处理 + CGT 训练/推理两部分。原始训练集经 NBW 平衡后输入 CGT 训练；KDDTest+ 输入训练好的 CGT 推理。
- **输入输出**：输入为一维向量 X（每样本 43 种特征，据原文 2.1 节）；输出二分类（正常/异常）或五分类（Normal, DOS, Probing, R2L, U2R）。
- **NBW 数据平衡模块（1.1 节）**：
    - `(X, Y)` → NCR 去噪/去异常 → Borderline-SMOTE 仅对 Danger 区少数类合成 → `(X_{n,s}, Y)`；Borderline-SMOTE 把少数类分 Safe/Danger/Noise 三区，只对 Danger 合成。
    - WGAN：真实少数类 `(X_r, Y_m)` 与噪声 `X_N`→Generator 生成 `X_fake`，用 `(X_r,Y_m)` 与 `X_fake` 迭代训练判别器与生成器；训练后生成 `(X_g, Y)`。
    - WGAN 用 EMD（Earth Mover's Distance）替代 JS/KL 散度，缓解模式崩溃与梯度消失；损失式(1)(2)：`Loss(c)=(1/m)Σf_w(x_i)−(1/m)Σf_w(g_θ(z_i))`，`Loss(g)=(1/m)Σf_w(g_θ(z_i))`。
    - 合并 `(X_{n,s},Y)` 与 `(X_g,Y)` → 平衡训练集 `Data`。
- **CNN-GRU 模块（1.2 节）**：卷积块（2 卷积层，各接 BatchNorm + ReLU）与 2 个相同 GRU 层并行。X 经卷积块二次卷积提空间特征；X 时间维转置后入 GRU 提时序特征；两路输出降维后拼接送入 Transformer。
- **改进 Transformer 编码器（1.3 节）**：仅编码部分（多头注意力 + 前馈网络）。点积注意力 `Attention(Q,K,V)=softmax(QK^T/√d_K)V`（式3）；多头 `MultiHead=concat(head_1,…,head_n)W^O`（式4）。前馈隐藏层为输入两倍、GELU 激活（式5）以增强非线性。
- **MLP 模块（1.4 节）**：2 全连接层 + 1 Dropout（置于全连接后），第 1 层 ReLU；Softmax 输出概率。
- **训练**：环境 AMD Ryzen 9 7945HX + RTX 4060 + Win11，Python 3.6 / PyTorch 1.8.1；Adam 优化器。超参数（表4）：batch_size=64、lr=0.001、Dropout=0.5、Input_dim=32、Attention_head=16、FeedForward_hidden_size=64、GRU_layer=2、CNN_kernel_size=3。
- **与已有方法差异**：比 LSTM/BiLSTM 多空间特征且 GRU 省参；比单 CNN/单 Transformer 多结合 GRU 时序与 Transformer 全局；比传统 SMOTE 多 WGAN 生成更真实样本。
- **类型特化**：检测/分类类；backbone = CNN-GRU + Transformer 编码器，head = MLP+Softmax；创新在 NBW 预处理 + 混合主干，解决类别不平衡与多类型特征提取。

## 6. 实验与结果
- **数据集**：NSL-KDD（四子集）。训练集 KDDTrain+_20Percent，测试集 KDDTest+（22,544 条），5 类标签。
    - 原始训练集（表1）：Normal 13448 / DOS 9234 / Probing 11656 / R2L 995 / U2R **52**（0.15%），严重不平衡。
    - NBW 平衡后（表2）：Normal 13255 / DOS 9062 / Probing 11513 / R2L 7000 / U2R **3500**，总 44330。
- **对比方法**：LR, KNN, DT, AB, RF, SVM，分别在原始/平衡数据上训练，对比 CGT、NBW+CGT。
- **指标**：Acc, Pre, Rec, F1（式6–9）；入侵样本为正样本。
- **主结果（表5）**：
    - 平衡有效性：LR 二分类 Acc 72.8%→84.7%（约 +12%），五分类约 +3.2%。
    - NBW+CGT 最佳：二分类 Acc **93.4%** / Rec **96.8%** / Pre 92.0% / F1 **94.3%**（次优 NBW+LR F1 86.5%，+7.8pt）；五分类 Acc **82.5%** / Rec **65.5%** / Pre **79.1%** / F1 **69.1%**（次优 NBW+RF F1 53.7%，+15.4pt）。相对 SVM，CGT 的 Acc/F1 约 +12.3%/+12.8%。
    - 细节：裸 CGT 五分类 Rec 78.8% 高于 NBW+CGT 的 65.5%，但其 F1 仅 46.5%、Pre 56.8%——NBW 以牺牲部分召回换取 Pre 与综合 F1。
- **混淆矩阵（图3/4）**：多数样本在对角线；但 U2R 仅 41 正确、120 误判为 Normal，模型难捕捉 U2R 特征（U2R 现实样本太少 + 生成样本缺多样性）。
- **消融**：仅"有/无 NBW"对比，**无去 GRU/Transformer/WGAN 的细粒度消融**。
- **泛化**：仅 NSL-KDD，未做跨数据集泛化。
- **效率**：给硬件与超参，**无参数量/FLOPs/速度定量比较**。

## 7. 这篇论文真正有价值的地方
1.  **"数据+模型"协同**：把 NBW 数据平衡与 CGT 特征提取有机结合，给出针对类别不平衡入侵检测的系统性端到端方案。
2.  **NBW 分阶段融合**：NCR + Borderline-SMOTE "粗处理"提质并初平衡，WGAN（EMD 损失）"精生成"高质量多样样本，是不平衡学习的具体范例。
3.  **混合特征架构**：CNN-GRU 并行提空间+时序、Transformer 建全局关系，适合兼具局部相关性与序列依赖的网络流量；启发跨网络类型的模块组合。

## 8. 局限与问题
1.  **U2R 仍最差**：图4 显示 41 正确/120 误判为 Normal；表2 中 U2R 仅扩到 3500，生成样本缺多样性，单靠数据增强不够。
2.  **实验不全面**：仅 NSL-KDD（源自 1999 KDD'99，相对老旧），未验证 CICIDS2017/UNSW-NB15 等现代数据集。
3.  **计算成本未探讨**：CNN+GRU+Transformer+WGAN 结构复杂，未讨论参数量、训练时间、实时性。
4.  **特征工程缺失**：结论自承"未对样本特征进行提取选择"，下一步拟设计轻量级模型挖掘特征。
5.  **复现风险**：WGAN 训练细节、NCR/Borderline-SMOTE 阈值等关键实现不完整。

## 9. 我该怎么使用这篇论文
- **快速了解**：读摘要、图1、2.4 结果分析与表5。
- **复现**：精读第1章（1.1–1.4）与第2章参数设置（表4）、数据集（表1/表2）；NCR/Borderline-SMOTE/WGAN 细节查参考文献[14][15]。
- **借鉴创新点**：数据平衡（NBW 融合采样+生成，迁移到其他不平衡分类）；模型架构（CNN-GRU + Transformer 用于语音/传感器等时序任务）。
- **写 related work**：归入"基于深度学习的入侵检测""应对类别不平衡的入侵检测""Transformer 在安全领域应用""CNN+RNN 混合模型"。

## 10. 和其他论文的关系
- 用 GAN/WGAN 做入侵检测数据增强的工作（文中文献[5] CWVAE-GAN+1D-CNN、[11] VAE-CWGAN、[12] 过-欠采样+GAN 直接相关）。
- 用 Transformer/自注意力做序列建模与分类的工作（文献[19] 联邦学习+自注意力工业 IoT 入侵检测）。
- CNN 与 RNN（LSTM/GRU）混合用于时序数据分类的工作（文献[16] Conv-LSTM）。
- 不平衡数据处理（文献[14] SMOTE+Tomek、[15] Borderline-SMOTE 原文）。
`[[数据平衡处理中的生成对抗网络应用]]`
`[[Transformer在时序数据分类中的应用]]`
`[[CNN-RNN混合架构在序列建模中的应用]]`
`[[不平衡数据下的网络入侵检测方法综述]]`

## 11. 关键词
入侵检测，CNN-GRU，Transformer，数据平衡处理，NBW 模型，Wasserstein 生成对抗网络（WGAN），Borderline-SMOTE，邻域清理规则（NCR），Earth Mover's Distance，多头注意力，NSL-KDD，深度学习

## 12. 可信度说明
本精读基于 PDF 提取文本（7/7 页，覆盖摘要、引言、第1章方法、第2章实验与结果、第3章结论及参考文献）生成，文本完整。所有具体数字（表1/表2 数据分布、表4 超参数、表5 各指标、U2R 41/120 检测数、22544 测试条数、43 种特征）均严格来自提取文本。原始笔记将发表年份记为 2024（实为收稿年），已据引用格式更正为 2025；将作者补全为黄迎春、邢秀祺；DOI、基金、实验环境、EMD 损失、平衡后分布等据提取文本补充。提取文本为公式 OCR 文字，部分数学符号（如下标）可能有轻微转写误差。

---

> **可信度补充**: PDF 提取质量 = **high** (7/7 页全覆盖，约 2254 字符/页，含全部表格数字)；据本轮复核，原笔记年份(2024→2025)、作者(补邢秀祺)、DOI、实验环境、损失函数、平衡后分布、U2R 检测细节均已据提取文本核实更正；来源缓存: `.paper-cache/extracts/融合CNN-GRU和Transformer的网络入侵检测方法_黄迎春.txt` (7/7 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
