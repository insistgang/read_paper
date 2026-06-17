---
title: "MambaIR: A Simple Baseline for Image"
authors:
  - "Hang Guo"
  - "Jinmin Li"
  - "Tao Dai"
  - "Zhihao Ouyang"
  - "Xudong Ren"
  - "Shu-Tao Xia"
year: 2024
venue: "arXiv"
doi: 
pdf: [[RSSG.pdf]]
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
extract_cache: .paper-cache/extracts/RSSG.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/19 pages"
---
# MambaIR: A Simple Baseline for Image

## 基本信息
- **PDF**: [[RSSG.pdf]]
- **primary_topic**: `B_注意力算子模块`
- **topics**: `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | MambaIR: A Simple Baseline for Image |
| **作者** | Hang Guo; Jinmin Li; Tao Dai; Zhihao Ouyang; Xudong Ren; Shu-Tao Xia |
| **发表时间** | 2024 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> Recent years have seen significant advancements in image restoration,largelyattributedtothedevelopmentofmoderndeepneural networks,suchasCNNsandTransformers.However,existingrestoration backbonesoftenfacethedilemmabetweenglobalreceptivefieldsandef- ficientcomputation,hinderingtheirapplicationinpractice.Recently,the SelectiveStructuredStateSpaceModel,especiallytheimprovedversion Mamba, has shown great potential for long-range dependency modeling withlinearcomplexity,whichoffersawaytoresolvetheabovedilemma. However, the standard Mamba still faces certain challenges in low-level vision such as local pixel forgetting and channel redundancy. In this work, we introduce a simple but effective baseline, named MambaIR, which introduces both local enhancement and channel attention to im- provethevanillaMamba.Inthisway,ourMambaIRtakesadvantageof thelocalpixelsimilarityandreducesthechannelredundancy.Extensive experiments demonstrate the superiority of our method, for example, MambaIRoutperformsSwinI

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么要做**：图像恢复的性能提升很大程度上依赖于网络感受野的扩大。然而，当前主流的CNN和Transformer骨干网络在**全局感受野与高效计算**之间面临固有的两难选择。
- **之前方法的问题**：
    - **CNN方法**（如EDSR, RCAN）：计算效率高，适合部署，但**有效感受野有限**（p.2, Fig. 1(a)）。
    - **Transformer方法**（如SwinIR, HAT）：具有全局感受野，但标准自注意力的计算复杂度是图像分辨率的平方，难以承受。采用滑动窗口等高效注意力技术会**牺牲全局有效感受野**（p.2, Fig. 1(b)），本质上未解决权衡问题。
- **作者想解决的核心矛盾**：如何设计一个既能拥有**全局有效感受野**，又能保持**线性计算复杂度**，从而高效、高性能地进行图像恢复的骨干网络。
## 关键贡献

1.  **首次将状态空间模型适配到低级视觉任务**：通过大量实验，提出了MambaIR，作为CNN和Transformer方法的一个简单有效的替代方案。
2.  **提出了残差状态空间块**：针对原始Mamba在图像恢复中的两个缺陷（局部像素遗忘和通道冗余），提出了RSSB，它通过**局部卷积增强**来缓解局部像素遗忘，并通过**通道注意力**来减少通道冗余，从而提升标准Mamba的效能。
3.  **实验验证了MambaIR的优越性**：在多种图像恢复任务（超分辨率、去噪）上，MambaIR超越了其他强大的基线方法，证明了其作为图像恢复骨干的潜力和前景。
## 方法

- **整体框架**：MambaIR采用典型的三分段结构（p.5-6, Fig. 2）：
    1.  **浅层特征提取**：使用一个3×3卷积层从低质量输入图像`I_LQ`中提取浅层特征`F_S`。
    2.  **深层特征提取**：由多个**残差状态空间组**堆叠而成。每个RSSG包含多个**残差状态空间块**，并在组末尾使用卷积层细化特征。最终深层特征`F_L_D`与浅层特征`F_S`进行逐元素求和，得到重建输入`F_R`。
    3.  **高质量图像重建**：使用`F_R`通过重建模块生成高质量输出图像`I_HQ`。
- **输入输出**：输入为低质量图像`I_LQ ∈ R^{H×W×3}`，输出为高质量重建图像`I_HQ`。
- **关键模块详解**：
    - **残差状态空间块**：这是适配Mamba的核心设计（p.6-7, Fig. 2(a)）。
        - **结构**：输入特征`F_l_D`先经过LayerNorm，然后通过**视觉状态空间模块**捕获空间长程依赖，其输出与原始输入通过一个**可学习的缩放因子`s`** 进行残差连接。
        - **解决局部像素遗忘**：由于VSSM将2D特征图展平为1D序列处理，会导致空间相邻像素在序列中距离遥远（p.7, Fig. 3(a)）。因此，在VSSM后引入一个**瓶颈结构的卷积层**（通道先压缩后扩张）来恢复局部邻域相似性。
        - **解决通道冗余**：SSM为记忆长程依赖通常需要大量隐藏状态，导致通道冗余（p.7, Fig. 3(b)）。因此，在卷积层后引入**通道注意力**模块，以选择关键通道，减少冗余。最终输出再与Z_l通过另一个可学习因子`s'`进行残差连接。
        - **公式**：整个RSSB过程可形式化为：`F_{l+1}_D = CA(Conv(LN(Z_l))) + s' * Z_l` (公式 6)。
    - **视觉状态空间模块**：用于捕获长程依赖的模块（p.7-8, Fig. 2(b)）。
        - **双分支结构**：输入特征X分别经过两个分支。第一个分支为：Linear -> 深度可分离卷积(DWConv) -> SiLU激活 -> 2D-SSM -> LayerNorm。第二个分支为：Linear -> SiLU激活。两个分支的特征通过**哈达玛积**聚合，最后通过一个Linear层将通道数投影回原始维度C。
        - **公式**：`X_out = Linear( LN(2D-SSM(SiLU(DWConv(Linear(X))))) ⊙ SiLU(Linear(X)) )` (公式 7)。
    - **2D选择性扫描模块**：为适应2D图像的空间结构（p.8, Fig. 2(c)）。它将2D特征图**沿四个方向**（左上到右下、右下到左上、右上到左下、左下到右上）展平成四个1D序列，分别用状态空间方程建模长程依赖，最后将四个序列的结果**求和并恢复**为2D形状。
- **训练方式**：
    - **损失函数**：图像超分辨率使用L1损失；图像去噪使用Charbonnier损失（ε=10^{-3}）。
    - **优化器**：Adam (β1=0.9, β2=0.999)，初始学习率2×10^{-4}，并在特定训练轮次减半。
    - **训练硬件**：8张NVIDIA V100 GPU。
- **推理流程**：测试时可采用自集成策略进一步提升性能，此时模型记为MambaIR+。
- **和已有方法的差异**：
    - 与**CNN方法**相比：拥有全局有效感受野和线性复杂度，能更好地建模长程依赖。
    - 与**Transformer方法**相比：同样拥有全局感受野，但计算复杂度是线性的（得益于Mamba的并行扫描算法），更高效。它并非简单替换Transformer中的注意力为SSM，而是设计了新的RSSB模块结构，因为作者发现SSM和Attention行为不同，简单替换效果不佳。
## 实验

- **使用的数据集**：
    - **图像超分辨率**：训练集为DIV2K和Flickr2K；测试集包括Set5, Set14, B100, Urban100, Manga109。
    - **图像去噪**：高斯彩色图像去噪训练集为DIV2K, Flickr2K, BSD500, WED；测试集为BSD68, Kodak24, McMaster, Urban100。真实图像去噪训练集为SIDD的320张高分辨率图像，测试集为SIDD和DND。
- **对比方法**：主要与CNN方法（EDSR, RCAN, RDN）和Transformer方法（IPT, SwinIR, HAT, SRFormer）进行比较。
- **评价指标**：在YCbCr颜色空间的Y通道上计算PSNR和SSIM。
- **主实验结果**：
    - **图像超分辨率**：论文声称MambaIR在经典图像超分辨率任务上，使用**相似的计算成本但具备全局感受野**的情况下，**比SwinIR高出高达0.45dB** (p.1)。
    - **图像去噪**：在高斯彩色图像去噪和真实图像去噪任务上也进行了实验，但PDF前12页未提供具体对比数字表格。
    - **可视化结果**：在Urban100数据集上进行了定性比较（p.10, Fig. 4），展示了MambaIR在恢复纹理和结构细节上的优势。
- **消融实验**：
    1.  **RSSB设计消融**（Tab. 1）：
        - (0) baseline: 标准VSSM。
        - (1) 去掉局部卷积：性能下降，证明局部增强对缓解像素遗忘有效。
        - (2) 去掉局部卷积和通道注意力：性能进一步下降，证明二者结合效果最好。
        - (3) 用MLP替换卷积+通道注意力（结构类似Transformer）：性能不如RSSB，证明SSM和Attention行为不同，需要定制化设计。
    2.  **扫描模式消融**（Tab. 2）：
        - 对比了单方向、双方向和四方向扫描。**四方向扫描**在多数测试集上取得了最佳性能（如Set5上38.57dB）。
- **泛化实验**：论文提及在JPEG压缩伪影减少等任务上也有实验，但详细结果在补充材料中（p.9）。
- **速度/参数量/FLOPs**：
    - 消融实验中提供了参数量（#param）和乘加操作数（MACs）。例如，RSSB的baseline配置参数量为16.7M，MACs为439G（p.9, Tab. 1）。
    - 论文未在正文中提供与其他方法的详细速度或FLOPs对比表格。
## 局限

- **方法场景局限性**：MambaIR基于将2D图像展平为1D序列处理，尽管使用了四方向扫描，但对于具有**复杂、非局部空间结构依赖**的图像模式，其建模能力是否优于基于2D窗口的Transformer（如SwinIR）尚不明确。
- **实验完整性**：PDF文本（前12页）未提供与其他先进方法的详细计算效率（如推理速度、FLOPs）对比，也未充分讨论模型在**移动端部署**的潜力。
- **计算成本**：虽然理论上是线性复杂度，但消融实验显示其MACs（439G）相对较高，实际运行效率需要进一步验证。
- **数据集依赖**：实验主要基于学术界标准数据集，在**极端退化条件**或**特定领域图像**（如医学影像、遥感影像）上的表现未知。
- **复现风险**：虽然代码开源，但论文的性能高度依赖于精心设计的RSSB结构和扫描模式，调参可能是一个需要经验的过程。
## 个人评论

1.  **开辟了新方向**：首次系统性地将强大的状态空间模型（Mamba）引入低级视觉恢复任务，证明了其作为CNN和Transformer之外一种可行骨干的潜力。
2.  **提供了深入的问题分析与有效的工程设计**：论文没有直接套用Mamba，而是清晰分析了其应用于图像恢复时的两个具体缺陷（局部像素遗忘、通道冗余），并给出了**局部卷积+通道注意力**的针对性解决方案。这种“发现问题-分析问题-解决问题”的思路极具启发性。
3.  **提供了可复现的强基准**：MambaIR作为一个“简单但有效”的基准模型，代码开源，为后续研究者探索状态空间模型在视觉任务中的应用提供了一个坚实的起点。
4.  **模块设计的启示**：RSSB的设计表明，不能简单地将用于序列建模的SSM模块替换Transformer的Attention，需要根据任务特性（如图像的2D局部性）进行**适配和改进**。

### 使用建议

- **快速了解**：只读**摘要**和**引言**（第1节），就能掌握论文的核心动机、方法和主要结论。
- **复现**：重点仔细阅读**第3节方法论**，特别是RSSB（3.3）、VSSM（3.4）和2D-SSM（3.5）的详细描述和图示（Fig. 2）。结合开源代码理解实现细节。
- **借鉴创新点**：
    - **学习其分析框架**：学习它如何发现并分析现有技术（Mamba）在新场景（图像恢复）中的问题（局部像素遗忘、通道冗余）。
    - **学习其模块设计思路**：学习它如何将**局部归纳偏置**（通过卷积）和**通道自适应**（通过通道注意力）引入序列模型以提升性能。
    - **实验设计**：参考其消融实验的设计，验证自己模块中各个组件的有效性。
- **写Related Work**：可将其放在“**基于状态空间模型的视觉任务**”或“**高效全局建模骨干网络**”的相关工作综述中。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于计算机视觉中的**低级视觉**方向，核心解决**图像恢复**问题（如图像超分辨率、去噪）。论文提出了一种名为MambaIR的基准模型，它基于选择性结构状态空间模型（Mamba），旨在解决现有CNN和Transformer方法在恢复过程中**全局感受野与高效计算之间的权衡难题**。根据提供的PDF文本，本文适合放在“**B_注意力算子模块**”主题下，因为其核心贡献是设计了一个结合了状态空间模型（可视为一种长序列注意力机制）和通道注意力的新型特征提取模块。

## 2. 一句话总结
本文提出了MambaIR，一个通过引入局部卷积增强和通道注意力来适配原始Mamba模型的简单有效的图像恢复基准模型，它利用状态空间模型的线性复杂度全局建模能力，在计算成本相近的情况下，取得了优于SwinIR等强大基线的性能。

## 3. 背景与问题
- **为什么要做**：图像恢复的性能提升很大程度上依赖于网络感受野的扩大。然而，当前主流的CNN和Transformer骨干网络在**全局感受野与高效计算**之间面临固有的两难选择。
- **之前方法的问题**：
    - **CNN方法**（如EDSR, RCAN）：计算效率高，适合部署，但**有效感受野有限**（p.2, Fig. 1(a)）。
    - **Transformer方法**（如SwinIR, HAT）：具有全局感受野，但标准自注意力的计算复杂度是图像分辨率的平方，难以承受。采用滑动窗口等高效注意力技术会**牺牲全局有效感受野**（p.2, Fig. 1(b)），本质上未解决权衡问题。
- **作者想解决的核心矛盾**：如何设计一个既能拥有**全局有效感受野**，又能保持**线性计算复杂度**，从而高效、高性能地进行图像恢复的骨干网络。

## 4. 核心贡献
1.  **首次将状态空间模型适配到低级视觉任务**：通过大量实验，提出了MambaIR，作为CNN和Transformer方法的一个简单有效的替代方案。
2.  **提出了残差状态空间块**：针对原始Mamba在图像恢复中的两个缺陷（局部像素遗忘和通道冗余），提出了RSSB，它通过**局部卷积增强**来缓解局部像素遗忘，并通过**通道注意力**来减少通道冗余，从而提升标准Mamba的效能。
3.  **实验验证了MambaIR的优越性**：在多种图像恢复任务（超分辨率、去噪）上，MambaIR超越了其他强大的基线方法，证明了其作为图像恢复骨干的潜力和前景。

## 5. 方法详解
- **整体框架**：MambaIR采用典型的三分段结构（p.5-6, Fig. 2）：
    1.  **浅层特征提取**：使用一个3×3卷积层从低质量输入图像`I_LQ`中提取浅层特征`F_S`。
    2.  **深层特征提取**：由多个**残差状态空间组**堆叠而成。每个RSSG包含多个**残差状态空间块**，并在组末尾使用卷积层细化特征。最终深层特征`F_L_D`与浅层特征`F_S`进行逐元素求和，得到重建输入`F_R`。
    3.  **高质量图像重建**：使用`F_R`通过重建模块生成高质量输出图像`I_HQ`。
- **输入输出**：输入为低质量图像`I_LQ ∈ R^{H×W×3}`，输出为高质量重建图像`I_HQ`。
- **关键模块详解**：
    - **残差状态空间块**：这是适配Mamba的核心设计（p.6-7, Fig. 2(a)）。
        - **结构**：输入特征`F_l_D`先经过LayerNorm，然后通过**视觉状态空间模块**捕获空间长程依赖，其输出与原始输入通过一个**可学习的缩放因子`s`** 进行残差连接。
        - **解决局部像素遗忘**：由于VSSM将2D特征图展平为1D序列处理，会导致空间相邻像素在序列中距离遥远（p.7, Fig. 3(a)）。因此，在VSSM后引入一个**瓶颈结构的卷积层**（通道先压缩后扩张）来恢复局部邻域相似性。
        - **解决通道冗余**：SSM为记忆长程依赖通常需要大量隐藏状态，导致通道冗余（p.7, Fig. 3(b)）。因此，在卷积层后引入**通道注意力**模块，以选择关键通道，减少冗余。最终输出再与Z_l通过另一个可学习因子`s'`进行残差连接。
        - **公式**：整个RSSB过程可形式化为：`F_{l+1}_D = CA(Conv(LN(Z_l))) + s' * Z_l` (公式 6)。
    - **视觉状态空间模块**：用于捕获长程依赖的模块（p.7-8, Fig. 2(b)）。
        - **双分支结构**：输入特征X分别经过两个分支。第一个分支为：Linear -> 深度可分离卷积(DWConv) -> SiLU激活 -> 2D-SSM -> LayerNorm。第二个分支为：Linear -> SiLU激活。两个分支的特征通过**哈达玛积**聚合，最后通过一个Linear层将通道数投影回原始维度C。
        - **公式**：`X_out = Linear( LN(2D-SSM(SiLU(DWConv(Linear(X))))) ⊙ SiLU(Linear(X)) )` (公式 7)。
    - **2D选择性扫描模块**：为适应2D图像的空间结构（p.8, Fig. 2(c)）。它将2D特征图**沿四个方向**（左上到右下、右下到左上、右上到左下、左下到右上）展平成四个1D序列，分别用状态空间方程建模长程依赖，最后将四个序列的结果**求和并恢复**为2D形状。
- **训练方式**：
    - **损失函数**：图像超分辨率使用L1损失；图像去噪使用Charbonnier损失（ε=10^{-3}）。
    - **优化器**：Adam (β1=0.9, β2=0.999)，初始学习率2×10^{-4}，并在特定训练轮次减半。
    - **训练硬件**：8张NVIDIA V100 GPU。
- **推理流程**：测试时可采用自集成策略进一步提升性能，此时模型记为MambaIR+。
- **和已有方法的差异**：
    - 与**CNN方法**相比：拥有全局有效感受野和线性复杂度，能更好地建模长程依赖。
    - 与**Transformer方法**相比：同样拥有全局感受野，但计算复杂度是线性的（得益于Mamba的并行扫描算法），更高效。它并非简单替换Transformer中的注意力为SSM，而是设计了新的RSSB模块结构，因为作者发现SSM和Attention行为不同，简单替换效果不佳。

## 6. 实验与结果
- **使用的数据集**：
    - **图像超分辨率**：训练集为DIV2K和Flickr2K；测试集包括Set5, Set14, B100, Urban100, Manga109。
    - **图像去噪**：高斯彩色图像去噪训练集为DIV2K, Flickr2K, BSD500, WED；测试集为BSD68, Kodak24, McMaster, Urban100。真实图像去噪训练集为SIDD的320张高分辨率图像，测试集为SIDD和DND。
- **对比方法**：主要与CNN方法（EDSR, RCAN, RDN）和Transformer方法（IPT, SwinIR, HAT, SRFormer）进行比较。
- **评价指标**：在YCbCr颜色空间的Y通道上计算PSNR和SSIM。
- **主实验结果**：
    - **图像超分辨率**：论文声称MambaIR在经典图像超分辨率任务上，使用**相似的计算成本但具备全局感受野**的情况下，**比SwinIR高出高达0.45dB** (p.1)。
    - **图像去噪**：在高斯彩色图像去噪和真实图像去噪任务上也进行了实验，但PDF前12页未提供具体对比数字表格。
    - **可视化结果**：在Urban100数据集上进行了定性比较（p.10, Fig. 4），展示了MambaIR在恢复纹理和结构细节上的优势。
- **消融实验**：
    1.  **RSSB设计消融**（Tab. 1）：
        - (0) baseline: 标准VSSM。
        - (1) 去掉局部卷积：性能下降，证明局部增强对缓解像素遗忘有效。
        - (2) 去掉局部卷积和通道注意力：性能进一步下降，证明二者结合效果最好。
        - (3) 用MLP替换卷积+通道注意力（结构类似Transformer）：性能不如RSSB，证明SSM和Attention行为不同，需要定制化设计。
    2.  **扫描模式消融**（Tab. 2）：
        - 对比了单方向、双方向和四方向扫描。**四方向扫描**在多数测试集上取得了最佳性能（如Set5上38.57dB）。
- **泛化实验**：论文提及在JPEG压缩伪影减少等任务上也有实验，但详细结果在补充材料中（p.9）。
- **速度/参数量/FLOPs**：
    - 消融实验中提供了参数量（#param）和乘加操作数（MACs）。例如，RSSB的baseline配置参数量为16.7M，MACs为439G（p.9, Tab. 1）。
    - 论文未在正文中提供与其他方法的详细速度或FLOPs对比表格。

## 7. 这篇论文真正有价值的地方
1.  **开辟了新方向**：首次系统性地将强大的状态空间模型（Mamba）引入低级视觉恢复任务，证明了其作为CNN和Transformer之外一种可行骨干的潜力。
2.  **提供了深入的问题分析与有效的工程设计**：论文没有直接套用Mamba，而是清晰分析了其应用于图像恢复时的两个具体缺陷（局部像素遗忘、通道冗余），并给出了**局部卷积+通道注意力**的针对性解决方案。这种“发现问题-分析问题-解决问题”的思路极具启发性。
3.  **提供了可复现的强基准**：MambaIR作为一个“简单但有效”的基准模型，代码开源，为后续研究者探索状态空间模型在视觉任务中的应用提供了一个坚实的起点。
4.  **模块设计的启示**：RSSB的设计表明，不能简单地将用于序列建模的SSM模块替换Transformer的Attention，需要根据任务特性（如图像的2D局部性）进行**适配和改进**。

## 8. 局限与问题
- **方法场景局限性**：MambaIR基于将2D图像展平为1D序列处理，尽管使用了四方向扫描，但对于具有**复杂、非局部空间结构依赖**的图像模式，其建模能力是否优于基于2D窗口的Transformer（如SwinIR）尚不明确。
- **实验完整性**：PDF文本（前12页）未提供与其他先进方法的详细计算效率（如推理速度、FLOPs）对比，也未充分讨论模型在**移动端部署**的潜力。
- **计算成本**：虽然理论上是线性复杂度，但消融实验显示其MACs（439G）相对较高，实际运行效率需要进一步验证。
- **数据集依赖**：实验主要基于学术界标准数据集，在**极端退化条件**或**特定领域图像**（如医学影像、遥感影像）上的表现未知。
- **复现风险**：虽然代码开源，但论文的性能高度依赖于精心设计的RSSB结构和扫描模式，调参可能是一个需要经验的过程。

## 9. 我该怎么使用这篇论文
- **快速了解**：只读**摘要**和**引言**（第1节），就能掌握论文的核心动机、方法和主要结论。
- **复现**：重点仔细阅读**第3节方法论**，特别是RSSB（3.3）、VSSM（3.4）和2D-SSM（3.5）的详细描述和图示（Fig. 2）。结合开源代码理解实现细节。
- **借鉴创新点**：
    - **学习其分析框架**：学习它如何发现并分析现有技术（Mamba）在新场景（图像恢复）中的问题（局部像素遗忘、通道冗余）。
    - **学习其模块设计思路**：学习它如何将**局部归纳偏置**（通过卷积）和**通道自适应**（通过通道注意力）引入序列模型以提升性能。
    - **实验设计**：参考其消融实验的设计，验证自己模块中各个组件的有效性。
- **写Related Work**：可将其放在“**基于状态空间模型的视觉任务**”或“**高效全局建模骨干网络**”的相关工作综述中。

## 10. 和其他论文的关系
- **强对比/继承关系**：[[SwinIR]]，[[HAT]]：作为Transformer基线进行直接性能对比的论文。
- **基础技术来源**：[[Mamba]]：本文的核心基础模型，论文旨在适配它用于图像恢复。
- **同系列/同期工作**：[[Vision Mamba (Vim)]] 或 [[VMamba]] 等其他将Mamba用于视觉任务的工作，它们可能采用不同的2D扫描策略。
- **主题相关**：其他关注“**全局建模与效率平衡**”的骨干网络论文，无论基于CNN、Transformer还是新架构。

## 11. 关键词
图像恢复， 状态空间模型， Mamba， 超分辨率， 图像去噪， 残差状态空间块， 全局感受野， 线性复杂度， 局部像素遗忘， 通道冗余， 通道注意力， 基准模型

## 12. 可信度说明
本精读笔记**完全基于用户提供的PDF提取文本（前12页）** 生成。笔记中的所有信息、描述和数字（如0.45dB, 16.7M, 439G）均直接来源于所提供的文本段落。对于实验部分未在提供的文本中详细展示的结果（如主实验对比表格、具体去噪PSNR/SSIM数值、速度对比），已在相应章节明确标注“PDF文本中未提供”或“PDF文本中未明确说明”。提取的文本覆盖了论文的摘要、引言、相关工作、完整方法论以及部分实验设置与消融分析，信息质量足以支撑对论文核心思想、技术细节和主要贡献的准确理解。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/RSSG.txt` (19/19 页; 原 AI 主体 12/19 + 全文补读 13-19); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-19; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-19。
- **提取情况**: 缺失页 7 页, 其中 7 页提取到可读文本。缺失页包含正文/附录内容, 其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: MambaIR 13
- p.13: Table 5: Quantitative comparison on lightweight image super-resolution with
- p.13: ESRGAN Real-ESRGAN BSRGAN SwinIR Ours RealSR LR
- p.13: 4.4 Comparison on Image Denoising
- p.13: Thanks to the global receptive field, our MambaIR can achieve better structure
- p.14: Table 6: Quantitative comparison on gaussian color image denoising with state-
- p.14: MethodBSD68 Kodak24 McMaster Urban100
- p.14: SwinIR IPT Restormer Ours GT Noisy
- p.14: Table 7: Quantitative comparison on real image denosing with state-of-the-art
- p.14: results, shown in Tab. 7, suggest that our method achieves comparable per-
- p.14: 5 Conclusion
- p.14: In this work, we explore for the first time the power of the recent advanced state

### 缺失页关键摘录

- p.13: Table 5: Quantitative comparison on lightweight image super-resolution with
- p.13: Set5 Set14 BSDS100 Urban100 Manga109Method scale#param MACsPSNR SSIM PSNR SSIM PSNR SSIM PSNR SSIM PSNR SSIM
- p.13: with σ=50 on the Urban100 dataset. We also give a visual comparison in Fig. 7.
- p.14: Table 6: Quantitative comparison on gaussian color image denoising with state-
- p.14: Table 7: Quantitative comparison on real image denosing with state-of-the-art
- p.14: DeamNet [53] MPRNet [64] DAGL [49] Uformer [61] Restormer [63] OursDatasetPSNR SSIM PSNR SSIM PSNR SSIM PSNR SSIM PSNR SSIM PSNR SSIM
- p.14: other methods such as Uformer [61] by 0.12dB PSNR on SIDD dataset. The
- p.15: 1. Abdelhamed, A., Lin, S., Brown, M.S.: A high-quality denoising dataset for smart-
- p.17: K.: Sketch-based manga retrieval using manga109 dataset. Multimedia Tools and
<!-- AI_READING_NOTE_END -->
