---
title: "TSLANet: Rethinking Transformers for Time Series Representation Learning"
authors:
  - "Emadeldeen Eldele"
  - "Mohamed Ragab"
  - "Zhenghua Chen"
  - "Min Wu"
  - "Xiaoli Li"
year: 2023
venue: "arXiv"
doi: 
pdf: [[TSLANet(ICB&ASB).pdf]]
primary_topic: B_注意力算子模块
topics:
  - "B_注意力算子模块"
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
extract_cache: .paper-cache/extracts/TSLANet(ICB&ASB).txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/20 pages"
---
# TSLANet: Rethinking Transformers for Time Series Representation Learning

## 基本信息
- **PDF**: [[TSLANet(ICB&ASB).pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | TSLANet: Rethinking Transformers for Time Series Representation Learning |
| **作者** | Emadeldeen Eldele; Mohamed Ragab; Zhenghua Chen; Min Wu; Xiaoli Li |
| **发表时间** | 2023 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> CNN PatchTST Autoformer 0.7 FEDformer Crossformer Time series data, characterized by its intrin- sic long and short-range dependencies, poses a 0.6 unique challenge across analytical applications. While Transformer-based models excel at cap- 0.5 turinglong-rangedependencies,theyfacelimita- 0.4 tionsinnoisesensitivity,computationalefficiency, andoverfittingwithsmallerdatasets. Inresponse, 0.3 we introduce a novel Time Series Lightweight Adaptive Network (TSLANet), as a universal 0.2 convolutionalmodelfordiversetimeseriestasks. Specifically, we propose an Adaptive Spectral 0.1 Classifcation Accuracy Forecasting MSE (Weather) Forecasting MSE (ETTh1) Block, harnessing Fourier analysis to enhance Figure 1: A comparison between CNN and Transformer- feature representation and tocapture bothlong- basedarchitecturesforclassificationandforecastingtasks. term and short-term interactions while mitigat- Classificationresultsaretheaverageover10UEAdatasets ingnoiseviaadaptivethresholding. Additionall

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **这篇论文为什么要做**：虽然Transformer因其捕捉长程依赖的能力在时间序列预测等任务中取得初步成功，但其固有的**排列不变性**可能损失时序信息，且在**小数据集、噪声环境**下存在过拟合和计算效率低的问题。近期研究甚至发现简单的线性层在某些情况下能超越复杂的Transformer。
- **之前方法有什么问题**：
    1. **Transformer**：计算复杂度高（O(N²)），参数量大易过拟合，注意力机制对噪声和冗余数据敏感，且其排列不变性可能不适用于强时序任务。
    2. **CNN**：擅长通过局部感受野捕捉短期模式（因此在分类任务中表现好），但**难以建模长程依赖**，导致在需要理解长期趋势的预测和异常检测任务中效果受限。
- **作者想解决的核心矛盾**：如何设计一个模型，既能像CNN一样高效、擅长捕捉局部模式，又能像Transformer一样有效地捕捉长程依赖和全局上下文，同时具备对噪声的鲁棒性和参数效率。
## 关键贡献

1. 提出了一个**通用的轻量级卷积骨干网络TSLANet**，它借鉴了Transformer的模块化设计（多层堆叠），但用高效的卷积操作替代了自注意力，适用于分类、预测和异常检测等多种任务。
2. 提出了**自适应频谱块（ASB）**。该模块利用FFT将数据转换到频域，通过一个**可学习的阈值θ**自适应地滤除代表噪声的高频分量，同时应用全局和局部滤波器（等效于循环卷积）来同时学习长短期特征。
3. 提出了**交互卷积块（ICB）**。该模块使用两个不同核大小的并行卷积层（分别捕获局部和较长范围特征），并通过逐元素相乘让它们的特征相互调制，以增强对复杂时间模式的建模能力。
4. 结合**基于掩码自编码器范式的自监督预训练**，提升模型在不同数据集上的表征能力和鲁棒性。
5. 通过全面实验（分类、预测、异常检测）证明了TSLANet优于多种先进模型。
## 方法

- **整体框架**：如图2所示，TSLANet整体架构分为三个部分：嵌入层、多个堆叠的TSLANet层（每层包含ASB和ICB）、以及一个任务特定的最终线性层。
- **输入输出**：输入是多通道时间序列信号S∈RC×L（C通道，L长度）。输出根据任务而定，例如分类任务的输出类别概率。
- **关键模块**：
    1. **自适应频谱块（ASB）**：
        - **FFT与自适应滤波**：首先对输入进行快速傅里叶变换（FFT）得到频域表示F。然后计算功率谱P=|F|²，并通过一个**可学习阈值θ**生成二值掩码(P>θ)，与F逐元素相乘，从而自适应地滤除低功率的高频噪声。
        - **可学习滤波器**：对原始频域数据F和滤波后的数据F_filtered分别应用**全局滤波器W_G**和**局部滤波器W_L**（均为可学习参数）。这两个操作等价于循环卷卷积，能覆盖整个序列，捕捉周期模式。
        - **IFFT重构**：将两个滤波结果相加后，通过逆快速傅里叶变换（IFFT）转换回时域，得到增强后的特征S′。ASB的核心思想是在频域进行操作，利用频域的特性实现高效、自适应的全局与局部特征融合及降噪。
    2. **交互卷积块（ICB）**：
        - 接收ASB输出的S′。
        - 使用两个1D卷积层（Conv1， Conv2）和GELU激活函数。关键设计是**交互调制**：Conv1的激活输出与Conv2的输出逐元素相乘得到A1，反之Conv2的激活输出与Conv1的输出相乘得到A2。这鼓励了不同尺度特征的相互影响。
        - 最后将A1与A2相加，再通过一个卷积层Conv3得到ICB的最终输出O_ICB。
- **模块之间怎么连接**：输入经过Patch分割和添加可学习位置编码后，进入TSLANet层。在每一层中，数据先流经ASB进行频域特征增强和降噪，其输出再流入ICB进行多尺度特征交互和提炼。层与层之间可以堆叠。
- **数学公式或机制的直观解释**：ASB的公式(4) `F_filtered = F ⊙ (P > θ)` 直观展示了如何用一个自学习的“筛子”在频域筛掉噪声。ICB的公式(8)(9) `A1 = φ(Conv1(S′)) ⊙ Conv2(S′)` 则形象地表示，一种尺度的特征被另一种尺度的特征所“调制”或“门控”，实现特征交互。
- **训练方式**：采用两阶段训练。第一阶段是**自监督预训练**，采用掩码自编码器范式：随机掩盖输入序列的某些patch，训练模型去重建这些被掩盖的部分，损失函数为MSE。第二阶段是在下游任务数据上进行**监督微调**。
- **推理流程**：PDF文本中未明确说明详细的推理流程，但通常与监督微调阶段前向传播流程一致，即输入时间序列经过分块、嵌入、通过堆叠的ASB和ICB层，最后由任务头输出结果。
- **和已有方法的差异**：如表1所示，与CNN（擅长局部，不擅长长程）和Transformer（擅长长程，不擅长局部且参数不高效）相比，TSLANet通过ASB和ICB的设计，旨在**同时高效地捕捉长程和局部依赖**，并保持参数效率。ASB作为注意力机制在**频域**的替代品，计算复杂度为O(N log N)，优于自注意力的O(N²)。
## 实验

- **使用的数据集**：
    - **分类**：UCR Archive (85个数据集), UEA Archive (26个数据集), 2个生物医学信号数据集, 3个人类活动识别数据集。
    - **预测**：ECL, ETT (ETTh1, ETTh2, ETTm1, ETTm2), Exchange, Traffic, Weather。
- **对比方法**：GPT4TS, TimesNet, ROCKET, Crossformer, PatchTST, MLP, TS-TCC, TS2VEC, Time-LLM, iTransformer, FEDformer, Autoformer, RLinear, DLinear, SCINet等。
- **评价指标**：分类使用**准确率**；预测使用**均方误差（MSE）** 和**平均绝对误差（MAE）**。
- **主实验结果**：
    - **分类**：在4个子集的平均准确率上，TSLANet达到**85.90%**，优于所有对比方法（次优的ROCKET为83.46%）。在UCR和UEA数据集上均取得最佳结果。
    - **多变量预测**：在多个基准数据集上，TSLANet整体表现优异。例如，在ECL数据集上，TSLANet的MSE为**0.165**，与最佳模型Time-LLM（0.158）接近且显著优于其他Transformer模型；在Weather数据集上，TSLANet的MSE为**0.228**，仅次于Time-LLM（0.225）。
- **消融实验**：PDF提供的文本中未找到关于消融实验的详细描述或结果。
- **泛化实验**：实验本身在多个任务（分类、预测）和多个数据集上进行，证明了其作为通用模型的**跨任务和跨数据集泛化能力**。
- **速度/参数量/FLOPs等效率信息**：论文在引言中提到TSLANet享有FFT的O(N log N)复杂度，比自注意力高效（见5.4节）。但**提供的PDF文本中未包含具体的参数量、FLOPs或推理速度对比数据**。
## 局限

1. **频域操作的假设与局限**：ASB的核心是基于频域滤波。这对于具有明显周期性或平稳特性的信号可能非常有效，但对于**高度非平稳、缺乏明确频谱特征的时间序列**，其自适应滤波和全局滤波器的效果可能需要进一步验证。
2. **阈值θ的学习**：可学习阈值θ是一个全局标量。论文未说明其初始化方式以及学习到的θ值是否具有可解释性（例如，是否对应数据中的特定噪声水平）。其学习可能对数据特性和损失函数敏感。
3. **自监督预训练的依赖**：论文提到自监督预训练能增强模型能力，尤其在大数据集上。这暗示其性能提升可能**依赖于额外的预训练阶段和未标注数据**，增加了应用成本和流程复杂度。
4. **实验细节缺失**：提供的文本中**缺少关键的消融实验**（如验证ASB中各组件、ICB中交互机制、自监督预训练各自贡献），以及详细的**计算效率对比**（参数量、FLOPs、推理时间），这使得对模型效率优势的评估不够完整。
5. **与最新方法的对比**：在预测任务中，虽与众多方法对比，但缺少与一些最新的、专注于高效长序列预测的MLP类模型（如N-BEATS, N-HiTS等）的对比。
## 个人评论

1. **创新的设计思路**：将**频域分析**（FFT）与**自适应信号处理思想**（可学习阈值滤波）引入深度学习网络设计，作为自注意力机制的替代，这为设计高效、物理可解释的时序模型提供了新视角。
2. **模块化与平衡性**：通过ASB（全局/长程）和ICB（局部/多尺度）的明确分工与协同，优雅地解决了CNN和Transformer在建模能力上的“偏科”问题。这种“频域-时域”、“全局-局部”的模块化设计思想非常值得借鉴。
3. **方法的有效性验证**：论文在差异巨大的三种任务（分类、预测、异常检测）上都取得了竞争力强的结果，证明了该框架的**通用性和鲁棒性**，增加了其作为基础骨干网络的参考价值。
4. **对自监督预训练的应用**：展示了简单的掩码自编码器预训练策略能有效提升该卷积骨干网络在多种下游任务上的性能，尤其对大模型和大数据场景有启发。

### 使用建议

- **如果快速了解**：只读 **Abstract（摘要）** 和 **Introduction（引言）** 的前两页，以及 **Fig. 2** 和 **Table 1**，就能快速抓住其动机、核心思想、方法框架和与现有方法的差异。
- **如果复现**：重点精读 **Section 3. Method**，特别是3.4（ASB）和3.5（ICB）的公式与算法描述，并仔细研究 **Fig. 2** 的结构图。同时需要参考附录（如有）中的算法细节和超参数设置。
- **如果借鉴创新点**：
    - **频域自适应处理**：学习ASB中“FFT → 功率谱计算 → 可学习阈值滤波 → 可学习滤波器乘法 → IFFT”这一流程，可思考如何将其应用于自己的模型中进行特征增强或去噪。
    - **特征交互机制**：学习ICB中通过逐元素乘法实现不同尺度卷积特征相互调制的设计，可用于其他需要多尺度融合的模块中。
    - **自监督预训练策略**：了解其基于patch的掩码自编码器范式，可直接应用于其他时序表征学习框架。
- **如果写related work**：可将其放在**时间序列表示学习**、**轻量级或高效Transformer替代模型**、**时域/频域混合模型**这几个类别下进行综述。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**时间序列表示学习**方向，具体聚焦于**时间序列分析的通用骨干网络设计**。它旨在解决Transformer模型在处理时间序列数据时面临的**噪声敏感、计算效率低和小数据集过拟合**等问题。论文的核心创新在于提出了一种基于卷积的轻量级架构（TSLANet），通过在频域进行自适应操作来替代计算开销大的自注意力机制。因此，这篇论文适合放在“B_注意力算子模块”主题下，因为它提出的“自适应频谱块（ASB）”是作为Transformer中自注意力模块的一种高效替代品。

## 2. 一句话总结
本文提出了一个名为TSLANet的轻量级自适应卷积网络，通过自适应频谱块（ASB）在频域进行特征学习和降噪，并结合交互卷积块（ICB）捕捉多尺度特征，以取代Transformer的自注意力机制，从而高效、鲁棒地处理多种时间序列任务。

## 3. 背景与问题
- **这篇论文为什么要做**：虽然Transformer因其捕捉长程依赖的能力在时间序列预测等任务中取得初步成功，但其固有的**排列不变性**可能损失时序信息，且在**小数据集、噪声环境**下存在过拟合和计算效率低的问题。近期研究甚至发现简单的线性层在某些情况下能超越复杂的Transformer。
- **之前方法有什么问题**：
    1. **Transformer**：计算复杂度高（O(N²)），参数量大易过拟合，注意力机制对噪声和冗余数据敏感，且其排列不变性可能不适用于强时序任务。
    2. **CNN**：擅长通过局部感受野捕捉短期模式（因此在分类任务中表现好），但**难以建模长程依赖**，导致在需要理解长期趋势的预测和异常检测任务中效果受限。
- **作者想解决的核心矛盾**：如何设计一个模型，既能像CNN一样高效、擅长捕捉局部模式，又能像Transformer一样有效地捕捉长程依赖和全局上下文，同时具备对噪声的鲁棒性和参数效率。

## 4. 核心贡献
1. 提出了一个**通用的轻量级卷积骨干网络TSLANet**，它借鉴了Transformer的模块化设计（多层堆叠），但用高效的卷积操作替代了自注意力，适用于分类、预测和异常检测等多种任务。
2. 提出了**自适应频谱块（ASB）**。该模块利用FFT将数据转换到频域，通过一个**可学习的阈值θ**自适应地滤除代表噪声的高频分量，同时应用全局和局部滤波器（等效于循环卷积）来同时学习长短期特征。
3. 提出了**交互卷积块（ICB）**。该模块使用两个不同核大小的并行卷积层（分别捕获局部和较长范围特征），并通过逐元素相乘让它们的特征相互调制，以增强对复杂时间模式的建模能力。
4. 结合**基于掩码自编码器范式的自监督预训练**，提升模型在不同数据集上的表征能力和鲁棒性。
5. 通过全面实验（分类、预测、异常检测）证明了TSLANet优于多种先进模型。

## 5. 方法详解
- **整体框架**：如图2所示，TSLANet整体架构分为三个部分：嵌入层、多个堆叠的TSLANet层（每层包含ASB和ICB）、以及一个任务特定的最终线性层。
- **输入输出**：输入是多通道时间序列信号S∈RC×L（C通道，L长度）。输出根据任务而定，例如分类任务的输出类别概率。
- **关键模块**：
    1. **自适应频谱块（ASB）**：
        - **FFT与自适应滤波**：首先对输入进行快速傅里叶变换（FFT）得到频域表示F。然后计算功率谱P=|F|²，并通过一个**可学习阈值θ**生成二值掩码(P>θ)，与F逐元素相乘，从而自适应地滤除低功率的高频噪声。
        - **可学习滤波器**：对原始频域数据F和滤波后的数据F_filtered分别应用**全局滤波器W_G**和**局部滤波器W_L**（均为可学习参数）。这两个操作等价于循环卷卷积，能覆盖整个序列，捕捉周期模式。
        - **IFFT重构**：将两个滤波结果相加后，通过逆快速傅里叶变换（IFFT）转换回时域，得到增强后的特征S′。ASB的核心思想是在频域进行操作，利用频域的特性实现高效、自适应的全局与局部特征融合及降噪。
    2. **交互卷积块（ICB）**：
        - 接收ASB输出的S′。
        - 使用两个1D卷积层（Conv1， Conv2）和GELU激活函数。关键设计是**交互调制**：Conv1的激活输出与Conv2的输出逐元素相乘得到A1，反之Conv2的激活输出与Conv1的输出相乘得到A2。这鼓励了不同尺度特征的相互影响。
        - 最后将A1与A2相加，再通过一个卷积层Conv3得到ICB的最终输出O_ICB。
- **模块之间怎么连接**：输入经过Patch分割和添加可学习位置编码后，进入TSLANet层。在每一层中，数据先流经ASB进行频域特征增强和降噪，其输出再流入ICB进行多尺度特征交互和提炼。层与层之间可以堆叠。
- **数学公式或机制的直观解释**：ASB的公式(4) `F_filtered = F ⊙ (P > θ)` 直观展示了如何用一个自学习的“筛子”在频域筛掉噪声。ICB的公式(8)(9) `A1 = φ(Conv1(S′)) ⊙ Conv2(S′)` 则形象地表示，一种尺度的特征被另一种尺度的特征所“调制”或“门控”，实现特征交互。
- **训练方式**：采用两阶段训练。第一阶段是**自监督预训练**，采用掩码自编码器范式：随机掩盖输入序列的某些patch，训练模型去重建这些被掩盖的部分，损失函数为MSE。第二阶段是在下游任务数据上进行**监督微调**。
- **推理流程**：PDF文本中未明确说明详细的推理流程，但通常与监督微调阶段前向传播流程一致，即输入时间序列经过分块、嵌入、通过堆叠的ASB和ICB层，最后由任务头输出结果。
- **和已有方法的差异**：如表1所示，与CNN（擅长局部，不擅长长程）和Transformer（擅长长程，不擅长局部且参数不高效）相比，TSLANet通过ASB和ICB的设计，旨在**同时高效地捕捉长程和局部依赖**，并保持参数效率。ASB作为注意力机制在**频域**的替代品，计算复杂度为O(N log N)，优于自注意力的O(N²)。

## 6. 实验与结果
- **使用的数据集**：
    - **分类**：UCR Archive (85个数据集), UEA Archive (26个数据集), 2个生物医学信号数据集, 3个人类活动识别数据集。
    - **预测**：ECL, ETT (ETTh1, ETTh2, ETTm1, ETTm2), Exchange, Traffic, Weather。
- **对比方法**：GPT4TS, TimesNet, ROCKET, Crossformer, PatchTST, MLP, TS-TCC, TS2VEC, Time-LLM, iTransformer, FEDformer, Autoformer, RLinear, DLinear, SCINet等。
- **评价指标**：分类使用**准确率**；预测使用**均方误差（MSE）** 和**平均绝对误差（MAE）**。
- **主实验结果**：
    - **分类**：在4个子集的平均准确率上，TSLANet达到**85.90%**，优于所有对比方法（次优的ROCKET为83.46%）。在UCR和UEA数据集上均取得最佳结果。
    - **多变量预测**：在多个基准数据集上，TSLANet整体表现优异。例如，在ECL数据集上，TSLANet的MSE为**0.165**，与最佳模型Time-LLM（0.158）接近且显著优于其他Transformer模型；在Weather数据集上，TSLANet的MSE为**0.228**，仅次于Time-LLM（0.225）。
- **消融实验**：PDF提供的文本中未找到关于消融实验的详细描述或结果。
- **泛化实验**：实验本身在多个任务（分类、预测）和多个数据集上进行，证明了其作为通用模型的**跨任务和跨数据集泛化能力**。
- **速度/参数量/FLOPs等效率信息**：论文在引言中提到TSLANet享有FFT的O(N log N)复杂度，比自注意力高效（见5.4节）。但**提供的PDF文本中未包含具体的参数量、FLOPs或推理速度对比数据**。

## 7. 这篇论文真正有价值的地方
1. **创新的设计思路**：将**频域分析**（FFT）与**自适应信号处理思想**（可学习阈值滤波）引入深度学习网络设计，作为自注意力机制的替代，这为设计高效、物理可解释的时序模型提供了新视角。
2. **模块化与平衡性**：通过ASB（全局/长程）和ICB（局部/多尺度）的明确分工与协同，优雅地解决了CNN和Transformer在建模能力上的“偏科”问题。这种“频域-时域”、“全局-局部”的模块化设计思想非常值得借鉴。
3. **方法的有效性验证**：论文在差异巨大的三种任务（分类、预测、异常检测）上都取得了竞争力强的结果，证明了该框架的**通用性和鲁棒性**，增加了其作为基础骨干网络的参考价值。
4. **对自监督预训练的应用**：展示了简单的掩码自编码器预训练策略能有效提升该卷积骨干网络在多种下游任务上的性能，尤其对大模型和大数据场景有启发。

## 8. 局限与问题
1. **频域操作的假设与局限**：ASB的核心是基于频域滤波。这对于具有明显周期性或平稳特性的信号可能非常有效，但对于**高度非平稳、缺乏明确频谱特征的时间序列**，其自适应滤波和全局滤波器的效果可能需要进一步验证。
2. **阈值θ的学习**：可学习阈值θ是一个全局标量。论文未说明其初始化方式以及学习到的θ值是否具有可解释性（例如，是否对应数据中的特定噪声水平）。其学习可能对数据特性和损失函数敏感。
3. **自监督预训练的依赖**：论文提到自监督预训练能增强模型能力，尤其在大数据集上。这暗示其性能提升可能**依赖于额外的预训练阶段和未标注数据**，增加了应用成本和流程复杂度。
4. **实验细节缺失**：提供的文本中**缺少关键的消融实验**（如验证ASB中各组件、ICB中交互机制、自监督预训练各自贡献），以及详细的**计算效率对比**（参数量、FLOPs、推理时间），这使得对模型效率优势的评估不够完整。
5. **与最新方法的对比**：在预测任务中，虽与众多方法对比，但缺少与一些最新的、专注于高效长序列预测的MLP类模型（如N-BEATS, N-HiTS等）的对比。

## 9. 我该怎么使用这篇论文
- **如果快速了解**：只读 **Abstract（摘要）** 和 **Introduction（引言）** 的前两页，以及 **Fig. 2** 和 **Table 1**，就能快速抓住其动机、核心思想、方法框架和与现有方法的差异。
- **如果复现**：重点精读 **Section 3. Method**，特别是3.4（ASB）和3.5（ICB）的公式与算法描述，并仔细研究 **Fig. 2** 的结构图。同时需要参考附录（如有）中的算法细节和超参数设置。
- **如果借鉴创新点**：
    - **频域自适应处理**：学习ASB中“FFT → 功率谱计算 → 可学习阈值滤波 → 可学习滤波器乘法 → IFFT”这一流程，可思考如何将其应用于自己的模型中进行特征增强或去噪。
    - **特征交互机制**：学习ICB中通过逐元素乘法实现不同尺度卷积特征相互调制的设计，可用于其他需要多尺度融合的模块中。
    - **自监督预训练策略**：了解其基于patch的掩码自编码器范式，可直接应用于其他时序表征学习框架。
- **如果写related work**：可将其放在**时间序列表示学习**、**轻量级或高效Transformer替代模型**、**时域/频域混合模型**这几个类别下进行综述。

## 10. 和其他论文的关系
根据论文主题（注意力算子模块）和提及的方法，可能相关的论文包括：
- `[[TimesNet]]`: 同为基于CNN的时序通用模型，但利用周期性和2D卷积，TSLANet则利用频谱分析和1D卷积。
- `[[PatchTST]]`: 基于Transformer的预测模型，采用了类似的分块（patching）思想，可作为TSLANet的一个关键对比对象。
- `[[TS-TCC]]` / `[[TS2VEC]]`: 专注于时间序列表示学习的自监督方法，TSLANet借鉴了其自监督预训练范式。
- `[[FEDformer]]` / `[[Autoformer]]`: 在Transformer中引入了频率增强模块，可视为在频域增强的另一种思路，与TSLANet的ASB有可比性。

## 11. 关键词
时间序列表示学习， 自适应频谱块， 交互卷积块， 卷积神经网络， 快速傅里叶变换， 长短期依赖， 噪声鲁棒性， 自监督预训练， 轻量级网络， 时间序列分类， 时间序列预测

## 12. 可信度说明
本篇精读笔记**主要基于提供的PDF提取文本的前12页内容**生成，涵盖了摘要、引言、相关工作、方法部分的全部内容，以及实验部分的结果表格和部分文本。提取文本质量良好，公式、图表描述和关键数据均清晰可辨。但需注意，**实验部分的详细设置、消融实验结果、完整的实验图表以及结论部分未包含在提供的文本中**，因此笔记中关于这些方面的描述相对简略或基于已提供内容的推断。所有数字和核心描述均严格来自提供的文本。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/TSLANet(ICB&ASB).txt` (20/20 页; 原 AI 主体 12/20 + 全文补读 13-20); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-20; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-20。
- **提取情况**: 缺失页 8 页, 其中 8 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: TSLANet: Rethinking Transformers for Time Series Representation Learning
- p.13: Through this process, H(f)learns to emphasize the frequency components that are most relevant for predicting the target,
- p.13: This signal now encapsulates the learned dependencies, ready for further processing or as an input to subsequent model
- p.13: To train the classification experiments, we optimized TSLANet using AdamW with a learning rate of 1e-3 and a weight
- p.13: In forecasting and anomaly detection, we use the Mean Squared Error (MSE) to measure discrepancies between predicted
- p.14: results on the validation sets across each collection of datasets, i.e., UCR and UEA. For biomedical and human activity
- p.14: In our evaluation, we extensively utilize four categories of datasets:
- p.14: It is part of the PhysioNet database and includes polysomnographic sleep recordings that have been widely used
- p.15: It provides a diverse set of user-generated activity data, making it suitable for testing the robustness of HAR
- p.15: Sleep EEG 25,612 8,910 3,000 2 5
- p.15: Arrhythmia ECG 70,043 21,892 187 1 2
- p.15: UCIHAR 7,352 2,947 128 9 6

### 缺失页关键摘录

- p.13: For all experiments, the stride was set to half of the patch size to ensure overlapping windows. Each experiment was repeated
- p.14: Model performance was evaluated using standard metrics appropriate to each task. For classification, we reported accuracy;
- p.14: from each dataset in the training set with a ratio of 80/20. The selection of the hyperparameters was based on the average
- p.14: For the self-supervised task, we deploy the unlabeled version of the training set in each dataset for pretraining, then use the
- p.14: In our evaluation, we extensively utilize four categories of datasets:
- p.14: this context, we utilized two pivotal datasets for our evaluation: the Sleep-EDF dataset and the MIT-BIH Arrhythmia
- p.14: –Sleep-EDF Dataset: This dataset consists of polysomnography recordings intended for sleep stage classification.
- p.14: –MIT-BIH Arrhythmia Dataset: Another significant dataset from PhysioNet, the MIT-BIH Arrhythmia Dataset, is
- p.14: A summary of the characteristics of these two datasets is presented in Table 6.
- p.15: –UCI Human Activity Recognition Using Smartphones (UCIHAR): This dataset is collected from experiments
- p.15: –Wireless Sensor Data Mining (WISDM): The WISDM dataset includes time series data from smartphone
- p.15: –Heterogeneity Human Activity Recognition (HHAR): HHAR dataset stands out due to its collection from
<!-- AI_READING_NOTE_END -->
