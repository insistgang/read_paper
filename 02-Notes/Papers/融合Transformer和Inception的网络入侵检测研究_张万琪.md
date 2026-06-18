---
title: 融合Transformer和Inception的网络入侵检测研究
authors:
  - "张万琪"
  - "王家兴"
  - "宋振峰"
year: 2025
venue: "电信科学"
doi: 
pdf: [[融合Transformer和Inception的网络入侵检测研究_张万琪.pdf]]
primary_topic: T_安全_入侵检测
topics:
  - "T_安全_入侵检测"
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
extract_cache: .paper-cache/extracts/融合Transformer和Inception的网络入侵检测研究_张万琪.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/20 pages"
---
# 融合Transformer和Inception的网络入侵检测研究

## 基本信息
- **PDF**: [[融合Transformer和Inception的网络入侵检测研究_张万琪.pdf]]
- **primary_topic**: `T_安全_入侵检测`
- **topics**: `T_安全_入侵检测`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-05

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 融合Transformer和Inception的网络入侵检测研究 |
| **作者** | 张万琪, 王家兴, 宋振峰 |
| **机构** | 中国人民公安大学信息网络安全学院, 北京 100038 |
| **发表时间** | 2025 (网络首发 2025-08-25, 收稿 2025-07-14) |
| **刊物/会议** | 电信科学 (中图分类号 TP393) |
| **基金** | 中央高校基本科研业务费专项资金项目 (2023JKF01ZK07) |
| **DOI/链接** | https://link.cnki.net/urlid/11.2103.tn.20250825.1048.002 |

## 摘要

**英文原文(据 PDF 提取文本整理, 修复断字与空格)**:

> At present, the problem of network security in the world is getting more and more attention. As an important part of network security, intrusion detection technology needs to be further developed and improved. Aiming at the lack of traffic feature extraction information ability and low detection efficiency of intrusion detection model, an intrusion detection method combining feature pre-extraction module (Feature pre-extraction module-RAM, FRAM), residual attention module and Transformer-DSC-Inception-Pyramid Squeeze Attention (T-DIPSA-FRAM) is proposed. In order to improve the detection performance in complex network traffic environment, adaptive synthetic oversampling (ADASYN), undersampling (RENN) and local outlier algorithm (LOF) are used to balance the data set. Firstly, the adaptive hybrid sampling and outlier detection algorithm (AR-LOF) is used to balance the data set. The feature pre-extraction module including the residual attention module is designed to extract the key features in the network traffic preliminarily and efficiently, and improve the learning stability of the high-dimensional features. Finally, the local feature enhanced attention module (DIPSA) is designed. The Transformer encoder structure captures the long-distance dependence, and the feed-forward network integrating DIPSA focuses on multi-scale local spatial features to enhance the sensitivity of the model to dynamic and non-uniformly distributed traffic. The experimental results show that the F1 scores are 93.58% and 95.35% and the weighted F1 scores are 88.26% and 91.03% in the binary classification and multi-classification detection tasks of the data sets UNSW-NB15 and ToN-IoT, respectively. It is proved that the proposed method can effectively improve the reliability of network intrusion detection.

**中文翻译**:

> 当前世界网络安全问题日益受到重视, 入侵检测技术作为网络安全的重要组成部分亟待进一步发展完善。针对入侵检测模型流量特征提取信息能力不足、检测效率低的问题, 本文提出一种结合特征预提取模块 (FRAM, 含残差注意力模块 RAM)、残差注意力机制与 Transformer-DSC-Inception-金字塔挤压注意力 (T-DIPSA-FRAM) 的入侵检测方法。为提升复杂网络流量环境下的检测性能, 采用自适应合成过采样 (ADASYN)、欠采样 (RENN) 和局部离群算法 (LOF) 平衡数据集。首先, 使用自适应混合采样与离群点检测算法 (AR-LOF) 平衡数据集; 设计含残差注意力模块的特征预提取模块以初步、高效地提取网络流量关键特征, 改善高维特征的学习稳定性; 最后, 设计局部特征增强注意力模块 (DIPSA), Transformer 编码器结构在捕捉长距离依赖的同时, 由融合 DIPSA 的前馈网络聚焦多尺度局部空间特征, 增强模型对动态、非均匀分布流量的敏感性。实验结果表明, 在 UNSW-NB15 与 ToN-IoT 数据集的二分类与多分类检测任务中, 分别取得 F1 分数 93.58%、95.35% 和加权 F1 分数 88.26%、91.03%, 证明所提方法能有效提升网络入侵检测的可靠性。

> 关键词: 入侵检测; 自适应混合采样与离群点检测算法 (AR-LOF); 残差注意力; 多尺度卷积。

> 来源: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 随着云技术大规模应用、网络设备规模庞大, 复杂网络环境极易受各类攻击威胁。入侵检测系统 (IDS) 通过监测分析网络流量或系统行为, 及时发现并报警 DDoS、恶意软件、SQL 注入等潜在恶意行为, 是网络安全的重要工具, 亟需发展完善。
- **之前方法的问题** (引言对 16 篇相关工作做了逐条点评):
    1.  **特征降维方法不足**: 基于方差选特征 (Rashid Mamunur 等) 过于简单, 只考虑单个特征、忽略特征间复杂关联; 基尼不纯度+随机森林 (Disha Raisa Abedin 等) 计算开销大、可解释性差、对冗余特征处理不足; Dropout 堆叠自编码器 (YanFang Fu 等) 可能训练不稳定、降低收敛速度。归纳为: 传统降维依赖统计特性, 导致重要信息丢失且无法充分考虑特征间非线性关联。
    2.  **数据类别不平衡处理不佳**: GAN+DNN 数据增强 (孙佳佳 等)、去噪自编码器+WGAN (Mohammad Arafah 等, 但生成样本可能与真实数据有差异)、SMOTE (Murad Ali Khan 等, 可能过采样易分样本、忽视难分样本)、Borderline-SMOTE (Yong Sun 等)、ADASYN+CNN (Taher Al-Shehari 等, 优先生成难分样本但未考虑原始噪声)。归纳为: 类别不平衡且无有效剔除噪声点。
    3.  **多尺度特征提取效率低**: CNN+LSTM (Asmaa Halbouni 等, LSTM 对长序列依赖建模有限)、Transformer 取长距离依赖 (Zihan Wu 等, 但未聚焦局部细粒度)、金字塔深度可分离卷积 (He J 等, 计算复杂度高)、Inception V4 (KMK Raghunath 等)、CNN+Inception 多尺度 (谢金鑫等, 但通道特征权重无区分性)。归纳为: 多尺度提取时通道权重缺乏动态调整, 无法充分融合全局上下文与局部细粒度特征, 检测效率低下。
- **核心矛盾**: 现有入侵检测模型无法**同时高效、准确地捕捉网络流量数据中的长距离 (全局) 依赖关系与多尺度 (局部) 细粒度特征**, 且受数据不平衡和噪声干扰严重, 限制了检测性能。

## 关键贡献

1.  **自适应混合采样与离群点检测算法 (AR-LOF)**: 结合 ADASYN 自适应过采样、RENN 欠采样和 LOF 局部离群检测, 平衡数据集并剔除 `lof(p)>1` 的噪声样本, 兼顾不平衡、噪声与特征差异问题。
2.  **特征预提取模块 (FRAM)**: 含卷积核逐级递减 (7-5-5-3) 的四层 1D 卷积和残差注意力模块 (RAM), 初步高效提取流量关键特征、降低特征维度、改善高维特征学习稳定性。
3.  **改进的 Transformer 编码器**: 仅用编码器部分, 在前馈网络中插入 DSC-Inception-PSA 结构 (即 DIPSA 局部特征增强注意力模块), 使自注意力捕捉全局依赖的同时聚焦多尺度局部空间特征, 增强对动态、非均匀流量的敏感性。
4.  **引入并适配金字塔挤压注意力 (PSA)**: 将其从图像领域转换为适合流量数据的实现, 通过 SPC 通道划分 (s 段) + 不同尺度卷积核 + SEWeight + Softmax 校准, 对多尺度特征做注意力加权。
5.  **完整框架 T-DIPSA-FRAM**: 将数据平衡、特征预提取与改进 Transformer 编码器串成端到端入侵检测流程, 在 UNSW-NB15、ToN-IoT 上验证对少数类的检测效果。

## 方法

- **整体框架** (图1, T-DIPSA-FRAM): 三阶段流水线 **数据集预处理与平衡 → 特征预提取 → 模型训练 (改进的 Transformer 编码器)**。
    - **数据预处理**: 缺失值填补 → 非数值型数据数值化 → Min-Max 归一化消除量纲差异 → ADASYN-RENN-LOF (AR-LOF) 平衡数据。
    - **输入**: 原始网络流量序列 (UNSW-NB15 共 49 维特征, ToN-IoT Network 子集 43 维特征)。
    - **输出**: 二分类 (正常/攻击) 或多分类 (10 类: 9 攻击 + 1 正常) 结果。
- **关键模块详解**:
    1.  **数据平衡模块 (AR-LOF, 算法1)**:
        - **ADASYN 过采样**: 计算全局合成基数 `G=β(R-A)` (式1); 对每个少数类样本计算其邻域中多数类比例 `r_i` (式2); 按 `g_i=G·r_i` (式3) 动态分配合成数量, 实现分布自适应; 在 k 邻域随机选少数类样本插值生成新样本 `z_i=x_i+(x_zi-x_i)·λ` (式4)。
        - **RENN 欠采样**: 对每个多数类样本统计其 K2 近邻中的少数类数量, 超过阈值则剔除该样本 (算法1中阈值取 0.1)。
        - **LOF 离群检测**: 对剩余样本经欧氏距离求可达距离 (式6)、局部可达密度 LRD (式7)、局部离群因子 `lof(p)` (式8); `lof(p)>1` 即判为离群点剔除, 直至数据集稳定无离群样本, 得 `D_new`。
    2.  **特征预提取模块 (FRAM, 图2)**:
        - **结构**: 卷积核大小从左至右依次为 7、5、5、3 的四个 1D 卷积层堆叠 (递减卷积核为后续卷积提供广阔感受野); 激活函数 ReLU 与 LeakyReLU (负斜率 α=0.2) 交替设置, 利于收敛和稳健; 卷积层间插入残差注意力模块 (RAM); 配最大池化 + Dropout 减小复杂度、防过拟合。
        - **残差注意力模块 (RAM, 图4, 受深度收缩网络启发)**: 先以 1×1、3×3、5×5 并行卷积提特征并做输入-输出跳跃连接相加 (缓解梯度消失); 输出后全局平均池化得每个特征图均值 `a`, 经 BN + Sigmoid 放缩为 [0,1] 系数, 阈值取 `τ=α·a`; 以软阈值函数 (式9, 曲线见图3) 处理特征 `p`: 将落在 `[-τ, τ]` 内的特征置零 (滤除小幅冗余), 区间外特征收缩 (`p-τ` 或 `p+τ`), 再与原始输入相加, 实现自适应去噪与冗余抑制。
    3.  **改进的 Transformer 编码器 (图5)**:
        - **基本结构**: 仅采用编码器 (入侵检测是分类/异常检测、不涉及生成), 含多头自注意力 + 前馈网络, 经残差连接和层归一化相连; 嵌入层加入正余弦位置编码 (式12、13, 偶数维用 sin、奇数维用 cos)。
        - **自注意力**: `Attention(Q,K,V)=Softmax(QK^T/√d_k)V` (式10, `√d_k` 为缩放因子); 多头即拼接多个头输出再过权重矩阵 (式11)。
        - **创新点**: 将标准前馈网络 (两层线性 + ReLU, 难以提取重要特征) 替换为 **DSC-Inception-PSA 模块 (图8)**, 进一步提取序列关键信息; 配批归一化加速稳定训练、末端全局平均池化降维。
    4.  **DSC-Inception 结构 (图6, 受 GoogLeNet Inception 启发)**: 3 个并行分支, 各分支先用 1×1 卷积降维再扩感受野, 分别以 1×1、3×3、5×5 的深度可分离卷积 (DSC, 比原始卷积轻便) 提取不同尺度特征, 末端拼接聚合, 输出 `F_k=PW(DW(X2)), k∈{1,3,5}` (PW 逐点卷积, DW 逐通道卷积)。
    5.  **金字塔挤压注意力 (PSA, 图7)**: 将输入张量 `m=(b,h,c)` (批次/序列长度/通道) 经 SPC 操作均分为 s 个片段 (每段通道 c/s), 各片段用核大小 `k=2(i+1)+1`、分组大小 `G=2^((k-1)/2)` 的独立卷积得多尺度特征图 `f_i`; 经 SEWeight 计算各段权重并拼接, 再用 Softmax 跨通道校准, 最后与原始输入逐元素相乘融合: `PSA(concat F)=σ(f(concat F))⊗F` (σ 为 sigmoid, f 为卷积)。s 越大引入大核卷积、增大感受野, G 越大强化 SEWeight 效果; 本文 PSA 参数见表4。
    6.  **DSC-Inception-PSA 模块 (图8, 即 DIPSA)**: 堆叠两个改进 Transformer 编码器; 前馈网络层先归一化 + 两个标准卷积初步增强 (`X1→X2`), 经 DSC-Inception 多分支提多尺度局部特征, 再经 PSA 加权聚焦关键攻击特征, 末端 LayerNorm + Dropout + 平均池化提升训练稳定性与泛化。
- **与已有方法的差异**: 区别于单纯 Transformer 或 CNN/Inception, 本工作系统整合 ① 前端 FRAM+RAM 的初步特征清洗与提取; ② AR-LOF 数据平衡 (过采样+欠采样+离群剔除一体); ③ 后端把 Transformer 全局建模与深度可分离卷积 Inception 多尺度局部提取, 通过 PSA 注意力在前馈网络内深度融合, 而非简单串/并联。
- **训练与推理**: 预处理+平衡后的样本先经 FRAM 提取降维, 再输入改进 Transformer 编码器; 输出维度 (43/49,1)→Transformer (提升至 64/128)→DSC-Inception-PSA→Flatten (二分类约 1312/1504, 多分类约 2324/3008) → Dense/Softmax 分类。

## 实验

- **使用数据集** (第4.1节, 类别计数见表1、表2):
    1.  **UNSW-NB15** (新南威尔士大学): 49 个特征, 9 种攻击 + 1 正常共 10 类。多分类标签 0-9 对应 Analysis、Backdoor、DoS、Exploits、Fuzzers、Generic、Normal、Reconnaissance、Shellcode、Worms。表1给出各类训练/测试样本数 (如 Normal 56000/37000, Generic 40000/18871, Exploit 33393/11132, Worms 130/44, Shellcode 1133/378 等), 类别极不平衡。
    2.  **ToN-IoT** (新南威尔士大学堪培拉校区物联网实验室, 选 Network 子集): 43 个特征, 9 种攻击 + 1 正常共 10 类。多分类标签 0-9 对应 Password、Injection、Backdoor、Scanning、Mitm、Normal、Ransomware、DoS、Ddos、Xss。表2各类样本数多为 20000 (Normal 50000, Xss 200, Mitm 1043)。
- **对比方法**: 提取文本 (前 12 页) 未给出与基线方法的对比表格 (据原文后续页 p.18 章节线索 "Comparative evaluation of data imbalance"、p.20 参考含 CIC-IoT-2023, 提取缓存未覆盖具体数值, 待核)。
- **评价指标** (第4.2节, 均由混淆矩阵 TP/TN/FP/FN 计算):
    - 正文 4.2 节列出 **准确率 Accuracy (式14)、召回率 Recall (式16)、F1 分数 (式17)**; 精确率 Precision 在式15中定义并用于 F1 计算 (原笔记把 Precision 单列为评价指标, 提取文本 4.2 句中未单独列出, 仅作为 F1 的中间量)。
    - **多分类**: 改用加权 F1 分数 (Weighted F1-score, 式18), 按各类样本数加权综合各类 F1。
- **主实验结果** (摘要明确给出):
    - **UNSW-NB15**: 二分类 F1 = **93.58%**, 多分类加权 F1 = **88.26%**。
    - **ToN-IoT**: 二分类 F1 = **95.35%**, 多分类加权 F1 = **91.03%**。
- **关键参数设置** (第4.3节):
    - **Transformer 编码器 (表3)**: 多头注意力头数 4; 特征隐藏维度 64/128 (二分类/多分类); 前馈中间层维度 512; 编码器堆叠层数 2; 层归一化率 0.00001。
    - **PSA 模块 (表4)**: 通道分组数 s=4; 各片段 (分组大小 / 核大小) = (1/3)、(4/5)、(8/7)、(16/9)。
- **模型计算复杂度分析** (第4.4节, 理论推导):
    - **FRAM**: 时间复杂度 `O(L·d_in·d_max), d_max=64/128`, 空间复杂度 `O(d_out²)+O(L·d_out)`。
    - **Transformer 编码器**: 多头注意力 `O(L²·d_model + L·d_model²)` (d_model=64/128, L=43/49, 故主要取决于 d_model, 头数取 4 平衡效率); 前馈 `O(L·d_model·d_ff)`, d_ff=512; 整体时间 `O(L²·d_model + L·d_ff·d_model)`。
    - **DSC-Inception-PSA**: DSC-Inception `O(L·d_max·m)` (m 为各分支通道之和); PSA `O(L·d_max·S² + d_max/S)`; 通过分组卷积+轻量注意力控制参数量、节约开销。
- **消融实验 / 泛化实验**: 提取文本 (前 12 页) 未覆盖具体设计与结果 (据原文后续页 p.13-20, 提取缓存未覆盖, 待核)。
- **实验环境与训练细节**: Windows 11, 32GB 内存, Intel Core i7-14650HX, NVIDIA RTX 4060, Python 3.12.0, TensorFlow 2.18.0, CUDA 11.8; 总训练轮数 80, 批次大小 32, 每轮训练约 50 秒。

## 局限

1.  **场景适用性 / 计算开销**: 结构相对复杂 (AR-LOF + FRAM + 改进 Transformer + DSC-Inception-PSA), 对极低延迟或资源受限的实时在线检测场景部署可能有挑战。论文虽给出理论复杂度分析, 但未提供 FLOPs、参数量等绝对量化对比 (提取文本仅含"平均单个样本检测用时"这一句的开头, 数值在缓存未覆盖页, 待核)。
2.  **实验充分性 (受提取范围限制)**: 提取缓存仅覆盖前 12 页, 与主流基线 (其他 Transformer 变体、CNN-LSTM、GAN-based 等) 的详细对比表、消融实验、训练曲线均在 p.13-20, 缓存未覆盖, 无法在本笔记核实其相对优势。
3.  **数据集局限性**: 仅用两个公开数据集 (UNSW-NB15、ToN-IoT Network)。两者虽具代表性, 但与真实动态网络环境仍有差距; 对更新颖攻击类型的泛化能力有待验证。后续页参考文献提及 CIC-IoT-2023 (p.20), 是否做了第三数据集验证待核。
4.  **超参数敏感性**: AR-LOF 效果依赖 ADASYN 的 β、RENN 邻居阈值 (算法1取 0.1)、LOF 的 k 值等超参; PSA 的 s、G 设置 (表4) 也需调参。论文未讨论这些参数的敏感性分析。
5.  **复现风险**: 含多个自定义模块 (RAM 软阈值、DSC-Inception-PSA), 且数据平衡流程 (算法1) 步骤多、依赖中间阈值, 完全复现需仔细对照式1-9 与图2-8 的全部细节。

## 个人评论

> (以下为 AI 阅读判断, 非作者原文)

这篇论文最值得学习的地方在于其**系统性的方法融合与模块化创新思路**:
1.  **数据层面的扎实处理**: 没有忽视数据质量, 把 ADASYN 过采样、RENN 欠采样、LOF 离群剔除串成一条完整的 AR-LOF 流水线 (算法1), 既解决类别不平衡又清洗噪声, 对实际场景中的脏数据与不平衡问题有参考价值。值得留意的是它对"难分类样本优先合成"(ADASYN 的 r_i 加权) 与"边界/噪声剔除"两个目标的兼顾。
2.  **特征提取的渐进式设计**: FRAM 卷积核逐级递减 (7→5→5→3)、ReLU/LeakyReLU 交替、嵌入软阈值残差注意力的设计, 体现了对 1D 流量时序信号特征提取的思考, "先精炼再喂主模型"的定位为后端减负。软阈值借鉴深度收缩网络, 把"自适应阈值去噪"用到流量特征上是一个轻巧的迁移。
3.  **架构的有机融合**: 把 Transformer 的全局上下文建模与 Inception 的多尺度局部提取, 通过在前馈网络内部插入 DSC-Inception-PSA (而非简单串/并联) 结合, 这种"全局-局部"协同范式对既需理解长程依赖 (攻击序列模式) 又需关注局部细节 (特定攻击载荷) 的时序任务 (入侵检测、日志分析) 有启发。
4.  **对注意力机制的精细设计**: FRAM 的软阈值残差注意力与 PSA 的多尺度通道注意力, 都在"特征选择"与"特征增强"上做文章, 而非直接套现成模块; 把图像领域的 PSA 适配到 1D 流量是一个可借鉴的跨域迁移点。

需要保留的批判视角: 本笔记基于前 12 页, 论文的核心说服力 (与基线对比、消融) 在后续页, 缓存未覆盖, 因此对"是否真的优于 SOTA"应持保留态度; 同时多模块叠加带来的复杂度收益是否值得, 缺少绝对效率数据支撑。

### 使用建议

- **快速了解**: 读摘要、引言 (问题与动机) + 第2章 (图1 整体框架) + 实验主结果 (4 个 F1 数值)。
- **复现**: 精读第3章, 重点是算法1 (AR-LOF, 式1-8)、图2/图4 (FRAM/RAM, 式9)、图5 (改进 Transformer)、图6-8 (DSC-Inception / PSA / DIPSA), 以及第4.3节参数 (表3 Transformer、表4 PSA)。
- **借鉴创新点**:
    - 数据平衡: AR-LOF (ADASYN+RENN+LOF) 的组合思路可迁移到自己的不平衡数据。
    - 特征提取: FRAM 卷积核递减 + 激活交替 + 软阈值注意力, 适用于其他 1D 时序特征提取。
    - 架构融合: 把多尺度卷积 (Inception 类) 置于 Transformer 前馈网络内部, 是增强局部建模能力的一种可试方案。
- **写 Related Work**: 可归入 ① 基于深度学习的网络入侵检测综述; ② Transformer 在入侵检测的应用; ③ 注意力机制在时序数据分类的应用; ④ 数据不平衡处理方法。

## 相关论文与链接

> - [[T_安全_入侵检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**网络安全与人工智能交叉领域**, 具体方向为**网络入侵检测 (NIDS)**。作者来自中国人民公安大学信息网络安全学院, 发表于《电信科学》(网络首发 2025-08-25, 中图分类 TP393)。针对入侵检测模型"流量特征提取能力不足、检测效率低"的痛点, 提出深度学习模型 T-DIPSA-FRAM。归入 **`[[T_安全_入侵检测]]`** 主题, 是深度学习 (Transformer + Inception + 注意力 + 重采样) 在网络威胁识别中的一次工程化整合创新。

## 2. 一句话总结
T-DIPSA-FRAM 用 AR-LOF (ADASYN+RENN+LOF) 平衡数据、用含残差软阈值注意力的特征预提取模块 (FRAM) 初步精炼特征, 再把 DSC-Inception-PSA 多尺度模块插入 Transformer 编码器前馈网络, 实现全局依赖与多尺度局部特征的协同建模, 在 UNSW-NB15、ToN-IoT 上二分类 F1 达 93.58%/95.35%、多分类加权 F1 达 88.26%/91.03%。

## 3. 背景与问题
- **为什么要做**: 云技术普及、设备规模庞大使复杂网络环境易受 DDoS、恶意软件、SQL 注入等攻击, IDS 作为监测分析流量/行为的安全工具亟需发展。现有深度学习 IDS 仍有不足。
- **之前方法的三类问题** (引言点评 16 篇工作后归纳):
    1.  **传统特征降维依赖统计特性** (方差选特征、基尼+随机森林、Dropout 自编码器), 导致重要信息丢失且无法充分考虑特征间非线性关联。
    2.  **数据类别不平衡且无有效剔噪** (GAN/WGAN 生成样本与真实有差异、SMOTE 过采样易分样本忽视难分样本、ADASYN 未考虑原始噪声)。
    3.  **多尺度提取时通道权重缺乏动态调整** (CNN+LSTM 长依赖有限、纯 Transformer 不聚焦局部、CNN+Inception 通道权重无区分性), 无法充分融合全局上下文与局部细粒度特征。
- **核心矛盾**: 现有模型无法**同时高效准确地捕捉流量的长距离全局依赖与多尺度局部细粒度特征**, 且受不平衡与噪声干扰。

## 4. 核心贡献
1.  **AR-LOF 数据平衡算法 (算法1)**: ADASYN 过采样 + RENN 欠采样 + LOF 离群剔除 (`lof(p)>1` 剔除), 一体化处理不平衡、噪声与特征差异。
2.  **FRAM 特征预提取模块**: 卷积核 7-5-5-3 递减的四层 1D 卷积 + ReLU/LeakyReLU(0.2) 交替 + 残差软阈值注意力 RAM, 初步高效提取关键特征、降维、稳定高维特征学习。
3.  **改进 Transformer 编码器**: 仅编码器, 在前馈网络插入 DSC-Inception-PSA (DIPSA), 自注意力捕全局依赖的同时聚焦多尺度局部空间特征。
4.  **PSA 跨域适配**: 将图像领域金字塔挤压注意力转为流量 1D 实现 (SPC 分段 + 多核卷积 + SEWeight + Softmax 校准 + 逐元素融合)。
5.  **端到端框架 T-DIPSA-FRAM**: 预处理→平衡→预提取→改进 Transformer 串成完整 NIDS 流程, 验证对少数类的检测效果。

## 5. 方法详解
- **整体流水线 (图1)**: 缺失值填补 → 数值化 → Min-Max 归一化 → AR-LOF 平衡 → FRAM 预提取 (Conv1D/池化 + RAM) → 改进 Transformer 编码器 (多头注意力 + 含 DSC-Inception-PSA 前馈) → 10 类 (二分类/多分类) 输出。
- **AR-LOF (算法1, 式1-8)**:
    - 合成基数 `G=β(R-A)`, β∈[0,1] (式1); 若 G≤0 返回原集。
    - 每个少数类样本邻域多数类比例 `r_i` (式2), 合成数 `g_i=G·r_i` (式3) 自适应分配; k 邻域插值生成 `z_i=x_i+(x_zi-x_i)·λ`, λ∈[0,1] (式4)。
    - RENN: 对多数类样本统计 K2 近邻中少数类数, 超阈值 (0.1) 剔除, 直至 R_new 稳定。
    - LOF: 求可达距离 (式6)、局部可达密度 LRD (式7)、局部离群因子 lof (式8); lof>1 剔除, 直至 D_new 无离群点。
- **FRAM (图2) + RAM (图4)**:
    - FRAM: 四层 1D 卷积 (核 7/5/5/3, 递减扩感受野) + ReLU/LeakyReLU(α=0.2) 交替 + 层间 RAM + 最大池化 + Dropout。
    - RAM (受深度收缩网络启发): 1×1/3×3/5×5 并行卷积 + 跳跃连接; 输出 GAP 得 `a`, 经 BN+Sigmoid 得系数, 阈值 `τ=α·a`; 软阈值 (式9): `[-τ,τ]` 内置零、区间外收缩 (p∓τ), 再与原输入相加去冗余降噪。
- **改进 Transformer 编码器 (图5)**: 仅编码器 + 正余弦位置编码 (式12/13); 自注意力 `Softmax(QK^T/√d_k)V` (式10), 多头拼接 (式11); 前馈网络由标准 (两层线性+ReLU) 替换为 DSC-Inception-PSA, 配 BN + 全局平均池化。
- **DSC-Inception (图6)**: 3 并行分支, 各分支 1×1 降维 + 1×1/3×3/5×5 深度可分离卷积, `F_k=PW(DW(X2))`, 末端拼接。
- **PSA (图7)**: 张量 `(b,h,c)` 经 SPC 分 s 段 (通道 c/s), 各段核 `k=2(i+1)+1`、分组 `G=2^((k-1)/2)`; SEWeight 求权重 + Softmax 校准 + 逐元素相乘融合, `PSA=σ(f(concat F))⊗F`。
- **DSC-Inception-PSA (图8, DIPSA)**: 堆叠两个改进编码器; 前馈层归一化 + 两标准卷积 → DSC-Inception 多尺度 → PSA 加权 → LayerNorm+Dropout+平均池化。

## 6. 实验与结果
- **数据集**:
    1.  **UNSW-NB15**: 49 特征, 10 类 (Analysis/Backdoor/DoS/Exploits/Fuzzers/Generic/Normal/Reconnaissance/Shellcode/Worms), 极不平衡 (Normal 56000 训练 vs Worms 130 训练, 表1)。
    2.  **ToN-IoT** (Network 子集): 43 特征, 10 类 (Password/Injection/Backdoor/Scanning/Mitm/Normal/Ransomware/DoS/Ddos/Xss), 多数类约 20000 (Xss 仅 200, 表2)。
- **评价指标 (4.2)**: 二分类用 Accuracy (式14)、Recall (式16)、F1 (式17), Precision (式15) 作为 F1 中间量; 多分类用加权 F1 (式18)。
- **主结果**: UNSW-NB15 二分类 F1 **93.58%**、多分类加权 F1 **88.26%**; ToN-IoT 二分类 F1 **95.35%**、多分类加权 F1 **91.03%**。
- **参数 (4.3)**: Transformer 表3 (头数 4, 隐藏维 64/128, 前馈中间维 512, 堆叠层 2, 层归一化率 1e-5); PSA 表4 (s=4, 分组/核 = 1/3、4/5、8/7、16/9)。
- **复杂度 (4.4)**: FRAM `O(L·d_in·d_max)`; Transformer `O(L²·d_model + L·d_ff·d_model)` (d_model=64/128, d_ff=512); DSC-Inception-PSA 用分组卷积+轻量注意力控参数量。
- **环境/训练**: Win11, 32GB, i7-14650HX, RTX 4060, Python 3.12.0, TF 2.18.0, CUDA 11.8; 80 epoch, batch 32, ~50s/epoch。
- **对比/消融**: 提取缓存仅前 12 页, 基线对比表与消融在 p.13-20 (后续页线索: p.18 "Comparative evaluation of data imbalance"), 缓存未覆盖具体数值, 待核。

## 7. 这篇论文真正有价值的地方
1.  **数据层面扎实**: AR-LOF 把过采样 (难分样本优先)、欠采样 (剔边界模糊)、离群剔除 (清噪声) 串成一条完整流水线, 对实际脏数据/不平衡问题有参考价值。
2.  **特征提取渐进式**: FRAM 卷积核递减 + 激活交替 + 软阈值残差注意力, 体现对 1D 流量时序提取的思考, "先精炼后入主模型"为后端减负; 软阈值是对深度收缩网络的轻巧迁移。
3.  **架构有机融合**: 把 Transformer 全局建模与 Inception 多尺度局部提取在前馈网络内部 (而非简单串/并联) 结合, "全局-局部"协同范式对入侵检测、日志分析等时序任务有启发。
4.  **注意力精细化**: 软阈值残差注意力 + PSA 多尺度通道注意力, 都聚焦"特征选择/增强"; 把图像 PSA 适配到 1D 流量是可借鉴的跨域迁移。

## 8. 局限与问题
1.  **计算开销 / 部署**: 模块叠加多, 实时低延迟场景部署有挑战; 缺 FLOPs、参数量等绝对效率数据 (理论复杂度有, 实测单样本检测用时在缓存未覆盖页, 待核)。
2.  **实验完整性 (受缓存范围限制)**: 与基线对比、消融、训练曲线在 p.13-20, 提取缓存仅前 12 页, 无法在本笔记核实相对优势。
3.  **数据集局限**: 仅两个公开数据集, 与真实动态网络有差距; 后续页提及 CIC-IoT-2023 (p.20), 是否做第三数据集验证待核。
4.  **超参敏感性**: AR-LOF 的 β/RENN 阈值 (0.1)/LOF k 值、PSA 的 s/G 均需调参, 论文未做敏感性分析。
5.  **复现风险**: RAM 软阈值、DSC-Inception-PSA 与算法1 步骤多, 完全复现需对照式1-9、图2-8 全部细节。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言 + 图1 + 4 个 F1 数值。
- **复现**: 精读算法1 (式1-8)、图2/图4 (式9 软阈值)、图5、图6-8, 及表3/表4 参数。
- **借鉴**: AR-LOF 组合采样思路; FRAM 卷积递减+激活交替+软阈值注意力; 把多尺度卷积置于 Transformer 前馈网络内部。
- **写 Related Work**: 深度学习 NIDS 综述 / Transformer 在入侵检测 / 注意力机制在时序分类 / 数据不平衡处理。

## 10. 和其他论文的关系
主题 `[[T_安全_入侵检测]]`。引言引用了 16 篇相关工作, 可据此建立关系:
- **特征降维/选择**: Rashid Mamunur (方差+树堆叠集成)、Disha Raisa Abedin (基尼+随机森林)、YanFang Fu (Dropout 堆叠自编码器)。
- **数据不平衡处理**: 孙佳佳 (GAN+DNN)、Mohammad Arafah (去噪自编码器+WGAN)、Murad Ali Khan (SMOTE)、Yong Sun (Borderline-SMOTE)、Taher Al-Shehari (ADASYN+CNN, 内部威胁检测)。
- **深度学习 IDS 架构**: Asmaa Halbouni (CNN+LSTM)、Zihan Wu (Transformer)、He J (变分高斯+金字塔深度可分离卷积)、KMK Raghunath (Inception V4)、谢金鑫 (CNN+Inception)、Hamad Naeem (深度 CNN 堆叠集成, 恶意软件多尺度)。
- 本文相当于把上述"数据平衡 + 多尺度卷积 + Transformer + 注意力"四条线整合到一个框架。(参考文献编号 [1]-[25] 可见, 但提取缓存未覆盖完整参考文献表, 无法逐条建立双链。)

## 11. 关键词
网络入侵检测, Transformer, Inception, DSC-Inception-PSA, 金字塔挤压注意力 (PSA), 残差注意力 (RAM), 软阈值, 多尺度卷积, 深度可分离卷积 (DSC), 数据平衡, ADASYN, RENN, 局部离群因子 (LOF), AR-LOF, UNSW-NB15, ToN-IoT。

## 12. 可信度说明
本篇精读主要基于 PDF 提取缓存 (前 12 页, 25000 字符上限截断), 覆盖摘要、引言、第2章方法、第3章模块技术 (算法1、FRAM/RAM、Transformer、DSC-Inception、PSA、DIPSA, 含式1-18)、第4.1-4.4节 (数据集、指标、参数表3/表4、复杂度分析、实验环境)。所有问题、方法、模块机制、参数、4 个 F1 主结果均直接来源于提取文本。**与基线方法的详细对比表、消融实验、训练曲线、单样本推理时间在 p.13-20, 提取缓存未覆盖, 凡涉及处均标注"待核"。** 英文摘要按提取文本修复断字后整理, 公式编号与参数取自原文。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本约 1612 字符/页, 公式/参数/类别表清晰); 提取覆盖 = 12/20 页 (摘要-引言-方法-模块技术-4.1~4.4); 后续 p.13-20 (对比/消融/参考文献) 缓存未覆盖, 相关结论标注"待核"。来源缓存: `.paper-cache/extracts/融合Transformer和Inception的网络入侵检测研究_张万琪.txt`; 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-20; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-20。
- **提取情况**: 缺失页 8 页, 其中 8 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Feature pre -extraction
- p.13: Transformer(43/49,128)
- p.13: DSC -
- p.13: Inception -PSAMaxpooling(21/24,64)
- p.13: Average
- p.13: Pooling (41/47,64)
- p.13: Flatten(2324/3008)
- p.13: Dense(1)Softmax
- p.13: Transformer(43/49,64)
- p.13: Maxpooling(21/24,32)
- p.13: Pooling (41/47,32)
- p.13: Flatten(1312/1504)

### 缺失页关键摘录

- p.18: Comparative evaluation of data imbalance
- p.20: IoT networks using CIC -IoT-2023 dataset[J].
<!-- AI_READING_NOTE_END -->
