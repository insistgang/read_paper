---
title: "MambaIR: A Simple Baseline for Image Restoration with State-Space Model"
authors:
  - "Hang Guo"
  - "Jinmin Li"
  - "Tao Dai"
  - "Zhihao Ouyang"
  - "Xudong Ren"
  - "Shu-Tao Xia"
year: 2024
venue: "arXiv (ECCV 2024)"
doi: 
pdf: [[RSSG.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
# MambaIR: A Simple Baseline for Image Restoration with State-Space Model

## 基本信息
- **PDF**: [[RSSG.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`, `B_注意力算子模块`
- **状态**: ai-read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | MambaIR: A Simple Baseline for Image Restoration with State-Space Model |
| **作者** | Hang Guo; Jinmin Li; Tao Dai; Zhihao Ouyang; Xudong Ren; Shu-Tao Xia（清华深研院、深圳大学、字节跳动、鹏城实验室）|
| **发表时间** | 2024（arXiv:2402.15648v2, 25 Mar 2024；后被 ECCV 2024 收录）|
| **刊物/会议** | arXiv（cs.CV）|
| **代码** | https://github.com/csguoh/MambaIR |
| **DOI** | 未明确 |

## 摘要

**英文原文（据 PDF 提取文本整理，已修复断字与空格）**：

> Recent years have seen significant advancements in image restoration, largely attributed to the development of modern deep neural networks, such as CNNs and Transformers. However, existing restoration backbones often face the dilemma between global receptive fields and efficient computation, hindering their application in practice. Recently, the Selective Structured State Space Model, especially the improved version Mamba, has shown great potential for long-range dependency modeling with linear complexity, which offers a way to resolve the above dilemma. However, the standard Mamba still faces certain challenges in low-level vision such as local pixel forgetting and channel redundancy. In this work, we introduce a simple but effective baseline, named MambaIR, which introduces both local enhancement and channel attention to improve the vanilla Mamba. In this way, our MambaIR takes advantage of the local pixel similarity and reduces the channel redundancy. Extensive experiments demonstrate the superiority of our method, for example, MambaIR outperforms SwinIR by up to 0.45dB on image SR, using similar computational cost but with a global receptive field. Code is available at https://github.com/csguoh/MambaIR.

**中文翻译**：

> 近年来图像恢复取得了显著进展，这在很大程度上归功于 CNN、Transformer 等现代深度神经网络的发展。然而，现有的恢复骨干网络常常陷入"全局感受野"与"高效计算"之间的两难，限制了实际应用。最近，选择性结构化状态空间模型——尤其是改进版 Mamba——展现出以线性复杂度建模长程依赖的巨大潜力，为化解上述两难提供了思路。但标准 Mamba 在低级视觉中仍面临特有挑战，如局部像素遗忘（local pixel forgetting）和通道冗余（channel redundancy）。本文提出一个简单而有效的基准模型 MambaIR，通过引入局部增强（local enhancement）和通道注意力（channel attention）来改进原始 Mamba，从而利用局部像素相似性并减少通道冗余。大量实验证明了本方法的优越性：例如在图像超分辨率上，MambaIR 在计算成本相近、但具备全局感受野的情况下，比 SwinIR 高出最多 0.45dB。代码已开源。

> **关键词**: Image Restoration · State Space Model · Mamba
> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：图像恢复（super-resolution、denoising、JPEG 压缩伪影去除等）旨在从低质量输入重建高质量图像。论文指出，深度恢复模型性能的提升很大程度上来自**网络感受野的扩大**——更大的感受野让网络能参考更广区域的像素、提取更高级的结构信息，对去噪等结构保持任务尤为关键；近期工作（HAT）也指出"激活更多像素"通常带来更好的恢复结果。
- **之前方法的两难**：当前恢复骨干在**全局感受野与高效计算之间存在固有的选择困境**。
    - **CNN 方法**（如 EDSR, RCAN）：卷积并行操作效率高、适合资源受限设备部署，但**有效感受野有限**（p.2, Fig. 1(a)）。
    - **Transformer 方法**（如 IPT, SwinIR, HAT）：token 数通常设为图像分辨率，标准自注意力带来**不可接受的二次方计算复杂度**；采用移位窗口注意力（shifted window attention）等高效注意力虽降本，却**以牺牲全局有效感受野为代价**（p.2, Fig. 1(b)），未从本质上跳出权衡。
- **为何选 Mamba**：结构化状态空间序列模型（S4）尤其是改进版 Mamba，离散化状态空间方程可写成**递归形式**，能建模超长程依赖（激活更多像素）；同时**并行扫描算法**让其能在 GPU 上高效并行训练，享有线性复杂度。这恰好同时满足"全局感受野 + 高效计算"。
- **标准 Mamba 直接用于图像的两个缺陷**：Mamba 原为 NLP 的 1D 序列设计，迁移到图像时：(1) 将 2D 图像展平为 1D 序列递归处理，导致**空间相邻像素在序列中相距甚远 → 局部像素遗忘**；(2) 为记忆长程依赖通常需要大量隐藏状态，导致**通道冗余**，妨碍关键通道表示的学习。
- **核心矛盾**：如何设计一个同时拥有**全局有效感受野**与**线性计算复杂度**的图像恢复骨干，并针对性弥补 Mamba 在低级视觉中的两个缺陷。

## 关键贡献

1.  **首次将状态空间模型适配到低级图像恢复**：通过大量实验提出 MambaIR，作为 CNN 与 Transformer 方法的一个简单而有效的替代骨干。
2.  **提出残差状态空间块（Residual State-Space Block, RSSB）**：以**局部卷积增强**（local enhancement）缓解局部像素遗忘、以**通道注意力**减少通道冗余，从而提升标准 Mamba 的能力；并用**可学习缩放因子**控制块内残差连接。
3.  **实验验证优越性**：在多种图像恢复任务（经典/轻量/真实超分、高斯彩色去噪、真实去噪）上超越多个强基线（如经典 SR 上比 SwinIR 高最多 0.45dB；真实去噪 SIDD 上比 Uformer 高 0.12dB PSNR，据 p.14 摘录），为图像恢复提供有力且有前景的骨干方案。

## 方法

- **整体框架（三阶段，p.5-6, Fig. 2）**：
    1.  **浅层特征提取（Shallow Feature Extraction）**：用一个 3×3 卷积层从低质量输入 `I_LQ ∈ R^{H×W×3}` 提取浅层特征 `F_S ∈ R^{H×W×C}`。
    2.  **深层特征提取（Deep Feature Extraction）**：由多个**残差状态空间组（RSSG）**堆叠；每个 RSSG 含若干**残差状态空间块（RSSB）**，并在组末尾加一个卷积层细化特征。得到第 l 层深层特征 `F^l_D ∈ R^{H×W×C}`。
    3.  **高质量图像重建（High-Quality Reconstruction）**：用逐元素求和聚合深浅特征 `F_R = F^L_D + F_S`，再经重建模块生成高质量输出 `I_HQ`。
- **预备知识（3.1）**：S4 源自连续 LTI 系统的 ODE `h'(t)=Ah(t)+Bx(t), y(t)=Ch(t)+Dx(t)`（公式 1），用**零阶保持（ZOH）**离散化为 `A=exp(ΔA)`、`B=(ΔA)^{-1}(exp(A)-I)·ΔB`（公式 2），得到 RNN 形式（公式 3）`h_k=A h_{k-1}+B x_k, y_k=C h_k+D x_k`，亦可等价转为 CNN 形式（公式 4）的结构化卷积核 K。Mamba 进一步把 B、C、Δ 设为**输入相关**（input-dependent / 选择性机制），实现动态特征表示。
- **关键模块详解**：
    - **残差状态空间块 RSSB（3.3, Fig. 2(a)）**：核心设计。
        - **动机**：以往 Transformer 恢复网络多遵循 Norm→Attention→Norm→MLP 流程；作者发现 Attention 与 SSM 虽都能建模全局依赖，但**行为不同**，简单地把 Attention 换成 SSM 只能得到次优结果，故需为 Mamba 定制全新块结构。
        - **第一步（VSSM + 残差）**：`Z_l = VSSM(LN(F^l_D)) + s·F^l_D`（公式 5），其中 `s ∈ R^C` 是可学习缩放因子，控制跳连信息。
        - **解决局部像素遗忘**：四方向展开下每个锚点像素仅有四个最近邻可用（Fig. 3(a)），故在 VSSM 后引入**局部卷积**恢复邻域相似性；先 LayerNorm 再卷积，卷积采用**瓶颈结构**（通道先按因子 γ 压缩到 C/γ，再扩张回 C）以保持效率。
        - **解决通道冗余**：用 ReLU + 全局平均池化可视化 VSSM 末层输出的通道激活，发现**多数通道未被激活**（Fig. 3(b)），故引入**通道注意力（CA）**选择关键通道。
        - **公式**：`F^{l+1}_D = CA(Conv(LN(Z_l))) + s'·Z_l`（公式 6），`s' ∈ R^C` 为另一可学习缩放因子。
    - **视觉状态空间模块 VSSM（3.4, Fig. 2(b)）**：双分支结构（沿用 VMamba [38] 设计）。输入 `X ∈ R^{H×W×C}`：
        - 分支一：Linear（通道扩张到 λC，λ 为预设扩张因子）→ 深度卷积 DWConv → SiLU → 2D-SSM → LayerNorm；
        - 分支二：Linear（同样扩张到 λC）→ SiLU；
        - 两分支以**哈达玛积（⊙）**聚合，再用 Linear 把通道投影回 C。
        - **公式（7）**：`X1=LN(2D-SSM(SiLU(DWConv(Linear(X)))))`，`X2=SiLU(Linear(X))`，`X_out=Linear(X1 ⊙ X2)`。
    - **2D 选择性扫描模块 2D-SSM（3.5, Fig. 2(c)）**：标准 Mamba 因果处理仅能捕获已扫描部分，不适合图像这类非因果数据。故将 2D 特征图沿**四个方向**（左上→右下、右下→左上、右上→左下、左下→右上）展平成四条 1D 序列，分别用离散状态空间方程建模长程依赖，最后**求和并 reshape** 恢复 2D 结构。
- **损失函数（3.6）**：
    - 图像 SR 用 **L1 损失** `L=||I_HQ − I_LQ||_1`（公式 8）；
    - 图像去噪用 **Charbonnier 损失** `L=sqrt(||I_HQ − I_LQ||^2 + ε^2)`，`ε=10^{-3}`（公式 9）。
- **训练细节（4.1）**：数据增强为水平翻转 + 随机旋转（90°/180°/270°）；SR 裁 64×64 patch、去噪裁 128×128 patch；SR 用 ×2 预训练权重初始化 ×3/×4 并减半学习率与迭代数；batch size = 32（SR）/16（去噪）；优化器 Adam（β1=0.9, β2=0.999），初始学习率 2×10^{-4} 在里程碑处减半；训练用 **8 张 NVIDIA V100 GPU**。
- **推理**：测试时用自集成（self-ensemble）策略，模型记为 **MambaIR+**。
- **和已有方法的差异**：相比 CNN，拥有全局有效感受野且能更好建模长程依赖；相比 Transformer，同有全局感受野但复杂度为线性（得益于并行扫描）。关键是**并非简单替换 Attention 为 SSM**，而是因二者行为不同而定制了 RSSB。

## 实验

- **任务范围**：图像超分辨率（经典 SR、轻量 SR、真实 SR）+ 图像去噪（高斯彩色去噪、真实去噪），另含 JPEG 压缩伪影去除（详见补充材料）。
- **使用的数据集**：
    - **经典 SR**：训练 DIV2K + Flickr2K；**轻量 SR** 仅用 DIV2K 训练。测试集：Set5, Set14, B100, Urban100, Manga109。
    - **高斯彩色去噪**：训练 DIV2K, Flickr2K, BSD500, WED；测试 BSD68, Kodak24, McMaster, Urban100。
    - **真实去噪**：训练 SIDD 的 320 张高分辨率图像；测试 SIDD 测试集 + DND。
- **评价指标**：在 YCbCr 颜色空间的 **Y 通道**上计算 **PSNR 与 SSIM**。
- **主实验结果**：
    - **经典 SR**：MambaIR 在计算成本相近、但具备全局感受野的情况下，**比 SwinIR 高出最多 0.45dB**（摘要 / p.1）。
    - **真实去噪**：据 p.14 摘录，"比 Uformer 等方法在 SIDD 上高 0.12dB PSNR"。完整对比表 Table 6（高斯去噪）、Table 7（真实去噪）位于 p.14，**提取缓存只覆盖 p.1-12，具体数值表格未在提取文本中给出（据原文后续页，提取缓存未覆盖，待核）**。
    - **轻量 SR**：对比表 Table 5 位于 p.13（含 ESRGAN/Real-ESRGAN/BSRGAN/SwinIR 等对比，据原文后续页，提取缓存未覆盖，待核）。
    - **可视化**：在 Urban100（×4，img_004/059/073）上与 CNN/Transformer 方法定性比较（p.10, Fig. 4）。
- **消融实验**（提取文本明确给出数值）：
    1.  **RSSB 设计消融（Table 1, p.9）**，指标为各测试集 PSNR：

        | settings | #param | MACs | Set5 | Set14 | B100 | Urban100 | Manga109 |
        |---|---|---|---|---|---|---|---|
        | (0) baseline（完整 RSSB） | 16.7M | 439G | 38.57 | 34.67 | 32.58 | 34.15 | 40.28 |
        | (1) +w/o Conv（去局部卷积） | 11.9M | 316G | 38.48 | 34.54 | 32.56 | 34.04 | 40.20 |
        | (2) +w/o Conv+CA（去卷积+通道注意力） | 11.8M | 315G | 38.55 | 34.64 | 32.57 | 34.06 | 40.14 |
        | (3) +replace with MLP（换成 MLP，近似 Transformer） | 14.3M | 379G | 38.55 | 34.68 | 32.59 | 34.22 | 40.13 |

        结论：去局部卷积会引发局部像素遗忘、性能下降；直接用现成 Mamba（去卷积+CA）只得次优结果；用 MLP 替换（结构近 Transformer）同样不理想——说明 SSM 与 Attention 虽都能全局建模但**行为不同**，需定制块结构。
    2.  **扫描模式消融（Table 2, p.9-10）**，参数量与 MACs 均为 16.7M / 439G：

        | scan mode | Set5 | Set14 | B100 | Urban100 | Manga109 |
        |---|---|---|---|---|---|
        | one-direction | 38.53 | 34.63 | 32.58 | 34.06 | 40.31 |
        | two-direction | 38.56 | 34.60 | 32.56 | 33.96 | 40.14 |
        | baseline（four-direction） | 38.57 | 34.67 | 32.58 | 34.15 | 40.28 |

        四方向扫描在多数测试集（Set5/Set14/Urban100）取得最佳，验证展开策略的重要性。（提取文本在 "using four directions of sca…" 处截断。）
- **速度/参数量/FLOPs**：消融表给出参数量与 MACs（baseline 16.7M / 439G）。正文（提取范围内）未提供与其他方法的统一速度/FLOPs 对比表格。

## 局限

- **2D 局部性建模仍间接**：方法本质是将 2D 图像展平为 1D 序列递归处理，靠四方向扫描 + 局部卷积补偿邻域信息；对具有复杂非局部空间结构依赖的图像模式，是否一定优于基于 2D 窗口的 Transformer，论文未深入论证。
- **计算成本绝对值偏高**：虽为线性复杂度，但 baseline MACs 达 439G（消融表），实际推理效率仍需在统一基准上验证；提取范围内未见与其他方法的速度/FLOPs 对比表。
- **部分结果在缓存外**：去噪与轻量 SR 的完整定量表（Table 5/6/7）及 JPEG 伪影去除结果分布在 p.13-14 与补充材料，提取缓存（p.1-12）未覆盖，难以独立核对其声明的全部增益。
- **领域泛化未知**：实验集中于学术标准数据集，对极端退化、特定领域（医学、遥感等）图像的表现未涉及。
- **复现依赖设计细节**：性能依赖 RSSB 结构、瓶颈压缩因子 γ、通道扩张因子 λ、可学习缩放因子等超参，调参可能需要经验（论文正文未给出 γ、λ 的具体取值，提取范围内未明确）。

## 个人评论

1.  **开辟新骨干方向**：首次系统性地把状态空间模型（Mamba）引入低级视觉恢复，给出了 CNN / Transformer 之外的第三种可行骨干，且以"线性复杂度 + 全局有效感受野"直击图像恢复长期的权衡痛点，ERF 可视化（Fig. 1）是有说服力的论据。
2.  **问题-分析-解决闭环清晰**：没有直接套用 Mamba，而是用通道激活可视化与四邻域展开图示，把"局部像素遗忘""通道冗余"两个抽象缺陷落到可观察的现象上，再分别用瓶颈卷积与通道注意力对症下药——这种实证驱动的模块设计思路很有借鉴价值。
3.  **"SSM ≠ Attention"是关键洞察**：消融 (3)（用 MLP 替换、结构近 Transformer）反而变差，说明不能机械地把 Attention 位置替换为 SSM，需要为序列模型补回 2D 局部归纳偏置与通道自适应。这是本文超出"把 Mamba 搬进视觉"层面的真正贡献。
4.  **强可复现基准**：代码开源、模块简单（RSSB 即"VSSM + 瓶颈卷积 + CA + 两个可学习残差因子"），为后续 SSM 视觉工作提供了坚实起点。
5.  **可改进处**：消融中各配置 PSNR 差距其实较小（Set5 上 baseline 38.57 vs 替换 MLP 38.55），单看 SR 难以完全凸显各组件必要性，更有力的证据其实在去噪/真实退化场景（在缓存外）；论文若能在正文给出统一的速度/显存对比，对"高效"主张会更有说服力。

### 使用建议

- **快速了解**：读摘要 + 引言（第 1 节）即可掌握动机（感受野 vs 效率两难）、方法（Mamba + RSSB）与主要结论（比 SwinIR 高最多 0.45dB）。
- **复现**：精读第 3 节，尤其 RSSB（3.3）、VSSM（3.4）、2D-SSM（3.5）的公式 5-7 与 Fig. 2；注意瓶颈卷积的压缩因子 γ、通道扩张因子 λ 需对照开源代码确认。
- **借鉴创新点**：学习其"用可视化定位缺陷 → 针对性补模块"的分析框架；学习把**局部归纳偏置（卷积）+ 通道自适应（CA）**注入序列模型的做法；参考其消融设计逐组件验证有效性。
- **写 Related Work**：可归入"**基于状态空间模型 / Mamba 的视觉任务**"或"**高效全局建模骨干**"综述。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉的**低级视觉 / 图像恢复**方向，核心解决超分辨率、去噪等任务的骨干网络设计问题。论文提出基准模型 MambaIR，基于选择性结构化状态空间模型（Mamba），目标是化解现有 CNN/Transformer 恢复骨干在**全局感受野与高效计算之间的两难**。从主题归类看，论文的**应用域是图像恢复**，故主主题定为 `E_图像复原_超分_去噪_去雨去雾`；同时其核心技术贡献是一个新的特征提取块（RSSB = 状态空间算子 + 瓶颈卷积 + 通道注意力 + 可学习残差），因此并列保留 `B_注意力算子模块` 作为次主题。

## 2. 一句话总结
MambaIR 通过为原始 Mamba 补上局部卷积增强与通道注意力（即 RSSB），在保持线性复杂度与全局感受野的前提下，构建了一个简单有效的图像恢复骨干，在经典 SR 上以相近算力比 SwinIR 高出最多 0.45dB。

## 3. 背景与问题
- **为什么要做**：恢复模型性能很大程度上来自感受野扩大（参考更多像素、提取更高级结构）。但当前骨干在全局感受野与高效计算间存在固有两难。
- **之前方法的问题**：
    - **CNN（EDSR, RCAN）**：效率高、适合部署，但有效感受野有限（Fig. 1(a)）。
    - **Transformer（IPT, SwinIR, HAT）**：token 数 = 图像分辨率，标准自注意力二次方复杂度不可接受；移位窗口等高效注意力又以牺牲全局有效感受野为代价（Fig. 1(b)），未本质解决权衡。
- **为何用 Mamba**：离散状态空间方程可写成递归形式建模超长依赖（激活更多像素），并行扫描算法支持 GPU 高效训练，天然兼顾"全局 + 线性"。
- **Mamba 直接用于图像的缺陷**：(1) 展平为 1D 递归 → 局部像素遗忘；(2) 隐藏状态多 → 通道冗余。
- **核心矛盾**：设计兼具全局有效感受野与线性复杂度、并修补上述两缺陷的恢复骨干。

## 4. 核心贡献
1.  首次将状态空间模型适配低级图像恢复，提出 MambaIR，作为 CNN/Transformer 的简单有效替代。
2.  提出残差状态空间块 RSSB：局部卷积增强缓解局部像素遗忘，通道注意力减少通道冗余，可学习因子控制残差。
3.  在经典/轻量/真实 SR 与高斯/真实去噪上超越多个强基线（经典 SR 比 SwinIR 最多高 0.45dB；真实去噪 SIDD 比 Uformer 高 0.12dB，据 p.14 摘录，缓存未覆盖完整表）。

## 5. 方法详解
- **三阶段框架（Fig. 2）**：浅层提取（3×3 卷积得 `F_S`）→ 深层提取（多个 RSSG，每组含多个 RSSB + 组末卷积）→ 重建（`F_R=F^L_D+F_S` 经重建模块得 `I_HQ`）。
- **预备（3.1）**：S4 源自 LTI 系统 ODE（公式 1），ZOH 离散化（公式 2）得 RNN 形式（公式 3）/ CNN 形式（公式 4）；Mamba 令 B、C、Δ 输入相关，实现选择性动态表示。
- **RSSB（3.3, Fig. 2(a)）**：
    - 动机：Attention 与 SSM 行为不同，简单替换得次优，需定制块。
    - `Z_l = VSSM(LN(F^l_D)) + s·F^l_D`（公式 5，s 为可学习缩放因子）。
    - 局部像素遗忘：四方向展开下锚点仅四最近邻（Fig. 3(a)），故 VSSM 后加**瓶颈卷积**（通道按 γ 压缩到 C/γ 再扩张）恢复邻域相似性。
    - 通道冗余：ReLU+GAP 可视化通道激活，多数通道未激活（Fig. 3(b)），引入**通道注意力**选关键通道。
    - `F^{l+1}_D = CA(Conv(LN(Z_l))) + s'·Z_l`（公式 6，s' 为另一可学习因子）。
- **VSSM（3.4, Fig. 2(b)）**：双分支（沿用 VMamba）。分支一 Linear(λC)→DWConv→SiLU→2D-SSM→LN；分支二 Linear(λC)→SiLU；哈达玛积聚合后 Linear 投回 C。公式 7：`X_out=Linear(LN(2D-SSM(SiLU(DWConv(Linear(X))))) ⊙ SiLU(Linear(X)))`。
- **2D-SSM（3.5, Fig. 2(c)）**：沿四方向（左上→右下、右下→左上、右上→左下、左下→右上）展平为四条 1D 序列，各自用状态空间方程建模，求和后 reshape 回 2D。
- **损失（3.6）**：SR 用 L1（公式 8）；去噪用 Charbonnier，ε=10^{-3}（公式 9）。
- **训练**：增强=水平翻转+90/180/270°旋转；SR 64×64 patch、去噪 128×128 patch；×2 权重初始化 ×3/×4；batch 32（SR）/16（去噪）；Adam(0.9,0.999)，lr=2×10^{-4} 里程碑减半；8×V100。测试自集成记为 MambaIR+。

## 6. 实验与结果
- **任务**：经典/轻量/真实 SR + 高斯彩色去噪 + 真实去噪（另含 JPEG 伪影去除，在补充材料）。
- **数据集**：经典 SR 训 DIV2K+Flickr2K、轻量 SR 仅 DIV2K；SR 测 Set5/Set14/B100/Urban100/Manga109。高斯去噪训 DIV2K+Flickr2K+BSD500+WED，测 BSD68/Kodak24/McMaster/Urban100。真实去噪训 SIDD 320 张，测 SIDD+DND。
- **指标**：YCbCr 的 Y 通道 PSNR / SSIM。
- **主结果**：经典 SR 比 SwinIR 最多高 0.45dB（相近算力 + 全局感受野）；真实去噪 SIDD 比 Uformer 高 0.12dB PSNR（p.14 摘录）。完整定量表 Table 5（轻量, p.13）/Table 6（高斯, p.14）/Table 7（真实, p.14）**在提取缓存（p.1-12）之外，据原文后续页、待核**。
- **消融 1（Table 1, RSSB 设计, p.9）**：baseline 16.7M/439G，Set5 38.57；去 Conv 降到 38.48、去 Conv+CA 38.55、换 MLP 38.55 / Urban100 上 baseline 34.15 vs 去 Conv 34.04——验证局部卷积与通道注意力的必要性，且 SSM≠Attention。
- **消融 2（Table 2, 扫描模式, p.9-10）**：one-/two-/four-direction 均 16.7M/439G，四方向在 Set5(38.57)/Urban100(34.15) 等多数集最佳。
- **算力**：消融给出 #param 与 MACs；正文（缓存范围内）无统一速度/FLOPs 对比表。

## 7. 这篇论文真正有价值的地方
1.  **第三种恢复骨干**：把 Mamba 引入低级视觉，用 ERF 可视化直观证明只有 MambaIR 达到显著的全局有效感受野，正面回应"全局 vs 效率"两难。
2.  **实证驱动的缺陷诊断**：用四邻域示意（局部像素遗忘）与通道激活可视化（通道冗余）把问题可观测化，再瓶颈卷积 + 通道注意力对症下药。
3.  **SSM≠Attention 的洞察与验证**：换 MLP（近 Transformer）反而更差，说明需为 SSM 定制块结构，而非机械替换注意力。
4.  **简单可复现**：RSSB 模块结构清晰、代码开源，为后续 SSM 视觉研究提供强基准。

## 8. 局限与问题
- 2D 局部性仍靠"四方向扫描 + 卷积"间接补偿，对复杂非局部结构是否优于 2D 窗口 Transformer 未充分论证。
- baseline MACs 439G 绝对值偏高，缓存范围内无统一速度/FLOPs 对比，"高效"主张缺正文量化支撑。
- 去噪/轻量 SR 完整表与 JPEG 结果在 p.13-14 与补充材料（缓存 p.1-12 之外），难以独立核对全部增益。
- 未涉及极端退化、医学/遥感等特定域；γ、λ 等关键超参正文（提取范围内）未给具体值，复现依赖代码。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言即可掌握动机/方法/结论。
- **复现**：精读 3.3-3.5 公式 5-7 与 Fig. 2，对照开源代码确认 γ、λ。
- **借鉴**：学习"可视化定位缺陷→针对性补模块"框架；把局部归纳偏置（卷积）+ 通道自适应（CA）注入序列模型；参考逐组件消融设计。
- **写综述**：归入"基于 Mamba/SSM 的视觉任务"或"高效全局建模骨干"。

## 10. 和其他论文的关系
- **直接对比基线**：[[SwinIR]]、[[HAT]]、[[IPT]]、[[SRFormer]]（Transformer 恢复方法）；[[EDSR]]、[[RCAN]]、[[RDN]]（CNN 方法）；去噪侧 [[Restormer]]、[[Uformer]]、[[MPRNet]] 等。
- **基础技术来源**：[[Mamba]]（核心基础模型）、[[VMamba]]（VSSM 与四方向 2D 扫描的直接来源 [38]）、[[S4]]。
- **同期视觉 Mamba 工作**：[[Vision Mamba (Vim)]]、[[VMamba]] 等，扫描策略可能不同。
- **主题相关**：其他关注"全局建模 vs 效率平衡"的骨干网络（CNN / Transformer / 新架构）。

## 11. 关键词
图像恢复, 状态空间模型, Mamba, 超分辨率, 图像去噪, 残差状态空间块 (RSSB), 视觉状态空间模块 (VSSM), 2D 选择性扫描, 全局感受野, 线性复杂度, 局部像素遗忘, 通道冗余, 通道注意力, 基准骨干

## 12. 可信度说明
本精读笔记主要基于 PDF 提取文本（缓存覆盖 p.1-12，含摘要、引言、相关工作、完整方法论第 3 节公式 1-9、实验设置与两组消融的完整数值表）。摘要、研究背景、方法、消融数值（38.57/34.15/16.7M/439G 等）、损失函数、训练超参均可在提取文本逐条核对，支撑度高。涉及去噪/轻量 SR 完整定量表（Table 5/6/7, p.13-14）与"比 Uformer 高 0.12dB"等结论来自原 AI 全文补读对 p.13-14 的章节线索与摘录，**提取缓存（p.1-12）未覆盖完整表格，相应数字已标注"据原文后续页、待核"**。γ、λ 等超参具体取值在提取范围内未给出。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/RSSG.txt` (提取覆盖 12/19 页; 原 AI 主体 12/19 + 全文补读 13-19 章节线索); 生成日期: 2026-06-05; 复核优化: 2026-06-18; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-19；原 AI 主体覆盖 p.1-12，本记录补足到 p.1-19。
- **提取情况**: 缺失页 7 页，其中 7 页提取到可读文本。缺失页包含正文/附录内容，其中约 1 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读，不是人工精读复核；`human_reviewed` 仍应保持 `false`。

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
