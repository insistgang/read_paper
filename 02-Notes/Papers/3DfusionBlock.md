---
title: Multi-Aperture Fusion of Transformer-Convolutional Network (MFTC-Net) for
authors:
  - "Siyavash Shabani"
  - "Muhammad Sohaib"
  - "Sahar A. Mohammed"
  - "Bahram Parvin"
year: 2024
venue: "arXiv"
doi: 
pdf: [[3DfusionBlock.pdf]]
primary_topic: D_3D_点云_分类_分割_配准
topics:
  - "D_3D_点云_分类_分割_配准"
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
extract_cache: .paper-cache/extracts/3DfusionBlock.txt
---

# Multi-Aperture Fusion of Transformer-Convolutional Network (MFTC-Net) for

## 基本信息
- **PDF**: [[3DfusionBlock.pdf]]
- **primary_topic**: `D_3D_点云_分类_分割_配准`
- **topics**: `D_3D_点云_分类_分割_配准`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Multi-Aperture Fusion of Transformer-Convolutional Network (MFTC-Net) for |
| **作者** | Siyavash Shabani; Muhammad Sohaib; Sahar A. Mohammed; Bahram Parvin |
| **发表时间** | 2024 |
| **刊物/会议** | arXiv |
| **DOI** | 未明确 |

## 摘要

> which is then reconstructed by the decoder block. Vision Transformers have shown superior performance to Additionally, the skip connections, at each stage of the the traditional convolutional-based frameworks in many dimensionality reduction, map the output of the encoder to vision applications, including but not limited to the the decoder blocks to improve medical image segmentation segmentation of 3D medical images. To further advance [18]. These blocks excel in extracting local image features, this area, this study introduces the Multi-Aperture Fusion but they are challenged to extract global features and their of Transformer-Convolutional Network (MFTC-Net), associations. Some studies have incorporated the attention which integrates the output of Swin Transformers and their mechanism [19-21] to enhance performance by improving corresponding convolutional blocks using 3D fusion the extraction of global features. blocks. The Multi-Aperture incorporates each image patch at its origina

> **来源**: PDF 自动提取，需人工复核。

## 研究背景与动机

- **为什么做**：传统的CNN（如UNet）在提取局部特征方面表现出色，但在捕捉长程依赖（全局特征）方面存在局限。Vision Transformers (ViT) 虽然擅长建模全局关系，但可能忽略重要的局部细节。现有的混合架构（如Swin UNETR）尝试结合二者，但在处理多尺度特征、特别是精细的物体表面细节方面仍有提升空间。
- **之前方法的问题**：文中提到Swin UNETR等模型使用标准的下采样和多尺度表示，这种“从粗到精”的表示方式在降低分辨率的同时，可能导致相邻器官间的表面细节被模糊或扩散（diffused）。
- **核心矛盾**：作者希望解决在利用Transformer获取全局上下文的同时，如何更好地保持高分辨率下的局部细节和表面清晰度这一矛盾。作者假设，改进的3D分割可以从“多孔径表示”中受益，即以原始分辨率保持重叠的多尺度区域表示，从而避免表面细节的丢失。
## 关键贡献

1.  **提出多孔径Swin Transformer模块**：设计了四个并行的Swin Transformer模块，每个模块处理不同“孔径”（即不同中心裁剪区域）但保持原始分辨率的图像块，从而在保留细节的同时构建多尺度上下文。
2.  **提出3D融合块（3D Fusion Block）**：设计了一个新颖的融合模块，用于整合每个Swin Transformer及其对应卷积模块的输出。该模块内部集成了挤压激励（SE）模块、元素乘法以及卷积块注意力模块（CBAM），分别从通道、特征和空间维度强调重要信息。
3.  **提出结合距离变换的损失函数**：在标准的Dice交叉熵损失基础上，引入了一种自定义的基于距离变换的损失项（DistLoss），以增强对器官表面形态一致性的约束。
4.  **实现更优的性能与模型效率**：在Synapse多器官数据集上取得了优于先前研究的平均Dice分数和HD95值，同时将模型参数量控制在约40M，相较于某些SOTA方法（如81M参数的3D TransUNet）更为轻量。
## 方法

- **整体框架**：模型采用编码器-解码器结构。编码器由四个并行的、具有不同“孔径”的Swin Transformer分支和与之对应的卷积分支组成，通过3D融合块在每一级进行特征融合。解码器部分在文中未详细描述，但图1显示了一个对称的逐步上采样结构。
- **输入输出**：输入是从3D CT体积中随机裁剪的 `128x128x128` 的3D图像块。输出是对应的分割掩膜。
- **关键模块与连接**：
    1.  **多孔径Swin Transformer**：输入的3D块首先送入第一个Swin Transformer (Swin T1)，其输入是完整块。第二个Transformer (Swin T2) 的输入则取自第一个块的中心区域（尺寸为 `H/2, W/2, D/2`），依此类推，T3和T4的输入中心区域尺寸更小。每个Transformer都处理保持原始分辨率的局部区域。
    2.  **卷积模块**：每个Swin Transformer分支都有一个对应的3D卷积分支，用于从Transformer的表示中提取更高级的局部特征。
    3.  **3D融合块**：对于第i个分支，融合块将三部分特征进行拼接：
        - **路径一**：Swin Transformer的输出经过一个**SE块**（强调通道重要性）。
        - **路径二**：Swin Transformer输出与卷积输出进行**元素乘法**（Hadamard乘积，调制特征重要性）。
        - **路径三**：卷积模块的输出经过一个**CBAM**模块（强调空间和通道注意力）。
        拼接后的特征作为该分支融合后的输出，传递给后续的解码器。
    4.  **损失函数**：总损失 `Loss(G, P) = DiceCE + λ * Σ(Di * Si) / Σ(Di)`。其中 `DiceCE` 是Dice交叉熵损失。`Di` 是预测值的有符号距离变换图的绝对值（归一化到0-1），`Si` 是表面点指示函数。这项DistLoss惩罚预测表面与真实表面的距离，提升形态一致性。
- **训练与推理**：训练使用Adam优化器，学习率10^-4，共300个epoch。在18个训练图像上随机提取patch进行训练，在12个图像上测试。最终结果基于5折交叉验证报告。
- **与已有方法的差异**：与Swin UNETR等使用标准金字塔下采样不同，本方法通过“多孔径”策略在多个尺度上以**原始分辨率**处理图像块，旨在更好地保留表面细节。与3D TransUNet等方法相比，本文显式地设计了融合块来整合Transformer和卷积特征，并引入了DistLoss。
## 实验

- **数据集**：Synapse multi-organs dataset，包含30个腹部CT扫描病例，标注了8个器官（脾、右肾、左肾、胆囊、肝、胃、主动脉、胰腺）。
- **对比方法**：MIST, Swin UNETR, nnFormer, UNETR++, MISSFormer, LeVit-UNet, 3D TransUNet。
- **评价指标**：平均Dice相似系数（Dice↑）和95%豪斯多夫距离（HD95↓）。同时报告了模型参数量（Par）。
- **主实验结果**：提出的MFTC-Net + DistLoss模型取得了**平均Dice 89.73**和**平均HD95 7.31**的最佳成绩，超过了所有对比方法。在八个器官中的四个（脾、右肾、左肾、主动脉）上取得了最高的Dice分数。模型参数量为**40M**，低于3D TransUNet (81M) 和 nnFormer (150M)，与UNETR++ (42M) 相当。
- **消融实验**：
    - **损失函数**：仅使用Dice损失得89.04；加入focal Dice得89.50；Dice+交叉熵得89.17；加入本文提出的DistLoss后提升至89.73，证明了DistLoss的有效性。
    - **Transformer与融合块数量**：仅使用T1（26M参数）得86.12；依次增加T2、T3、T4，参数增至36M，Dice提升至88.75；最后加上融合块（40M参数），Dice达到最佳89.73，表明多孔径策略和融合块均有贡献。
- **效率信息**：论文主要强调了参数量（40M）相较于某些方法的减少，但未报告FLOPs或推理速度。
## 局限

- **计算成本未明确比较**：虽然参数量减少了，但并行的四个Transformer分支和融合块可能带来较高的计算复杂度（FLOPs），论文未报告计算成本或训练/推理时间，与Swin UNETR等方法的效率对比不完整。
- **数据集相对单一**：所有实验仅在Synapse腹部CT数据集上进行，未在其他模态（如MRI）、其他部位（如心脏、脑部）或更大规模数据集上验证其泛化能力。
- **多孔径策略的深层分析不足**：“多孔径”避免了下采样带来的细节丢失，但论文未深入分析这种固定中心裁剪的策略与学习如何选择最有信息量区域的自适应策略相比有何优劣，其优势是否具有普适性有待更多验证。
- **可视化对比的细微差异**：在可视化对比（图2）中，作者承认MFTC-Net与3D TransUNet的分割结果差异“微小”，只能通过参数量来评判，这说明在该数据集上，不同方法的性能可能已接近瓶颈，本文方法的绝对优势仍需在更富挑战性的场景中检验。
## 个人评论

1.  **“多孔径”的直观思想**：提出了一个新颖的特征提取视角——不是通过下采样获得多尺度特征，而是通过在不同中心位置、以原始分辨率裁剪不同大小的区域（孔径）来获取多尺度上下文。这个思想对于需要精细边界保持的任务（如医学图像分割、遥感图像分析）具有很好的启发性。
2.  **系统的融合设计**：3D融合块的设计思路值得借鉴。它并非简单地拼接或相加Transformer和CNN的特征，而是通过SE、CBAM、元素乘积等多种注意力/调制机制，从多个角度（通道、空间、特征交互）进行智能融合，这种“分而治之”的融合策略比单一方法更灵活有效。
3.  **任务导向的损失函数设计**：将标准的Dice损失与基于距离变换的几何约束项相结合，直接优化表面形态，这种针对解剖结构先验知识的损失函数设计思路，对医学图像分析任务具有普适的参考价值。
4.  **高效实现的范例**：在性能超越部分SOTA的同时，显著降低了模型复杂度，展示了如何在Transformer时代通过巧妙的架构设计实现精度与效率的平衡。

### 使用建议

- **快速了解**：阅读 **Abstract, Introduction（第1段和贡献列表）, Results（Table 1和可视化部分）, Conclusion**。重点看其核心思想、结果数字和可视化对比。
- **复现**：重点精读 **Section 3: Method**，特别是3.1（Swin Encoders的具体输入选择机制）、3.2（Fusion Block的结构和图1）、3.3（损失函数公式）以及 **Section 4: Implementation details**。代码已开源，需结合代码理解细节。
- **借鉴创新点**：
    - 学习 **多孔径（Multi-Aperture）** 的思想，思考如何在自己的任务中设计保持分辨率的多尺度上下文提取模块。
    - 学习 **3D融合块** 的组合设计，将多种注意力机制（SE, CBAM）与元素操作结合进行特征融合。
    - 学习 **损失函数** 中融入几何先验（距离变换）的设计思路。
- **写Related Work**：可将本文归入“**结合Transformer与CNN的医学图像分割方法**”或“**用于3D体积分割的混合架构**”这一类别，与3D TransUNet, Swin UNETR, UNETR++, TransFuse等放在一起讨论。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[D_3D_点云_分类_分割_配准]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这篇论文属于**医学图像分析**与**三维（3D）计算机视觉**的交叉领域，具体聚焦于**3D医学图像分割**任务。它旨在解决现有基于Transformer和CNN的混合架构在分割3D医学图像（如腹部CT）时，对物体表面细节和相邻器官边界保持能力不足的问题。该论文最适合归入主题 `D_3D_点云_分类_分割_配准` 下，尽管其处理的是规则体数据（CT体积）而非点云，但其核心任务是3D分割，并大量涉及3D卷积和Transformer的融合架构设计。

## 2. 一句话总结
本文提出了一个名为MFTC-Net的新框架，通过并行的多孔径（Multi-Aperture）Swin Transformer与对应的卷积模块，并经由3D融合块进行集成，旨在更精确地分割3D医学图像中的器官表面和边界。

## 3. 背景与问题
- **为什么做**：传统的CNN（如UNet）在提取局部特征方面表现出色，但在捕捉长程依赖（全局特征）方面存在局限。Vision Transformers (ViT) 虽然擅长建模全局关系，但可能忽略重要的局部细节。现有的混合架构（如Swin UNETR）尝试结合二者，但在处理多尺度特征、特别是精细的物体表面细节方面仍有提升空间。
- **之前方法的问题**：文中提到Swin UNETR等模型使用标准的下采样和多尺度表示，这种“从粗到精”的表示方式在降低分辨率的同时，可能导致相邻器官间的表面细节被模糊或扩散（diffused）。
- **核心矛盾**：作者希望解决在利用Transformer获取全局上下文的同时，如何更好地保持高分辨率下的局部细节和表面清晰度这一矛盾。作者假设，改进的3D分割可以从“多孔径表示”中受益，即以原始分辨率保持重叠的多尺度区域表示，从而避免表面细节的丢失。

## 4. 核心贡献
1.  **提出多孔径Swin Transformer模块**：设计了四个并行的Swin Transformer模块，每个模块处理不同“孔径”（即不同中心裁剪区域）但保持原始分辨率的图像块，从而在保留细节的同时构建多尺度上下文。
2.  **提出3D融合块（3D Fusion Block）**：设计了一个新颖的融合模块，用于整合每个Swin Transformer及其对应卷积模块的输出。该模块内部集成了挤压激励（SE）模块、元素乘法以及卷积块注意力模块（CBAM），分别从通道、特征和空间维度强调重要信息。
3.  **提出结合距离变换的损失函数**：在标准的Dice交叉熵损失基础上，引入了一种自定义的基于距离变换的损失项（DistLoss），以增强对器官表面形态一致性的约束。
4.  **实现更优的性能与模型效率**：在Synapse多器官数据集上取得了优于先前研究的平均Dice分数和HD95值，同时将模型参数量控制在约40M，相较于某些SOTA方法（如81M参数的3D TransUNet）更为轻量。

## 5. 方法详解
- **整体框架**：模型采用编码器-解码器结构。编码器由四个并行的、具有不同“孔径”的Swin Transformer分支和与之对应的卷积分支组成，通过3D融合块在每一级进行特征融合。解码器部分在文中未详细描述，但图1显示了一个对称的逐步上采样结构。
- **输入输出**：输入是从3D CT体积中随机裁剪的 `128x128x128` 的3D图像块。输出是对应的分割掩膜。
- **关键模块与连接**：
    1.  **多孔径Swin Transformer**：输入的3D块首先送入第一个Swin Transformer (Swin T1)，其输入是完整块。第二个Transformer (Swin T2) 的输入则取自第一个块的中心区域（尺寸为 `H/2, W/2, D/2`），依此类推，T3和T4的输入中心区域尺寸更小。每个Transformer都处理保持原始分辨率的局部区域。
    2.  **卷积模块**：每个Swin Transformer分支都有一个对应的3D卷积分支，用于从Transformer的表示中提取更高级的局部特征。
    3.  **3D融合块**：对于第i个分支，融合块将三部分特征进行拼接：
        - **路径一**：Swin Transformer的输出经过一个**SE块**（强调通道重要性）。
        - **路径二**：Swin Transformer输出与卷积输出进行**元素乘法**（Hadamard乘积，调制特征重要性）。
        - **路径三**：卷积模块的输出经过一个**CBAM**模块（强调空间和通道注意力）。
        拼接后的特征作为该分支融合后的输出，传递给后续的解码器。
    4.  **损失函数**：总损失 `Loss(G, P) = DiceCE + λ * Σ(Di * Si) / Σ(Di)`。其中 `DiceCE` 是Dice交叉熵损失。`Di` 是预测值的有符号距离变换图的绝对值（归一化到0-1），`Si` 是表面点指示函数。这项DistLoss惩罚预测表面与真实表面的距离，提升形态一致性。
- **训练与推理**：训练使用Adam优化器，学习率10^-4，共300个epoch。在18个训练图像上随机提取patch进行训练，在12个图像上测试。最终结果基于5折交叉验证报告。
- **与已有方法的差异**：与Swin UNETR等使用标准金字塔下采样不同，本方法通过“多孔径”策略在多个尺度上以**原始分辨率**处理图像块，旨在更好地保留表面细节。与3D TransUNet等方法相比，本文显式地设计了融合块来整合Transformer和卷积特征，并引入了DistLoss。

## 6. 实验与结果
- **数据集**：Synapse multi-organs dataset，包含30个腹部CT扫描病例，标注了8个器官（脾、右肾、左肾、胆囊、肝、胃、主动脉、胰腺）。
- **对比方法**：MIST, Swin UNETR, nnFormer, UNETR++, MISSFormer, LeVit-UNet, 3D TransUNet。
- **评价指标**：平均Dice相似系数（Dice↑）和95%豪斯多夫距离（HD95↓）。同时报告了模型参数量（Par）。
- **主实验结果**：提出的MFTC-Net + DistLoss模型取得了**平均Dice 89.73**和**平均HD95 7.31**的最佳成绩，超过了所有对比方法。在八个器官中的四个（脾、右肾、左肾、主动脉）上取得了最高的Dice分数。模型参数量为**40M**，低于3D TransUNet (81M) 和 nnFormer (150M)，与UNETR++ (42M) 相当。
- **消融实验**：
    - **损失函数**：仅使用Dice损失得89.04；加入focal Dice得89.50；Dice+交叉熵得89.17；加入本文提出的DistLoss后提升至89.73，证明了DistLoss的有效性。
    - **Transformer与融合块数量**：仅使用T1（26M参数）得86.12；依次增加T2、T3、T4，参数增至36M，Dice提升至88.75；最后加上融合块（40M参数），Dice达到最佳89.73，表明多孔径策略和融合块均有贡献。
- **效率信息**：论文主要强调了参数量（40M）相较于某些方法的减少，但未报告FLOPs或推理速度。

## 7. 这篇论文真正有价值的地方
1.  **“多孔径”的直观思想**：提出了一个新颖的特征提取视角——不是通过下采样获得多尺度特征，而是通过在不同中心位置、以原始分辨率裁剪不同大小的区域（孔径）来获取多尺度上下文。这个思想对于需要精细边界保持的任务（如医学图像分割、遥感图像分析）具有很好的启发性。
2.  **系统的融合设计**：3D融合块的设计思路值得借鉴。它并非简单地拼接或相加Transformer和CNN的特征，而是通过SE、CBAM、元素乘积等多种注意力/调制机制，从多个角度（通道、空间、特征交互）进行智能融合，这种“分而治之”的融合策略比单一方法更灵活有效。
3.  **任务导向的损失函数设计**：将标准的Dice损失与基于距离变换的几何约束项相结合，直接优化表面形态，这种针对解剖结构先验知识的损失函数设计思路，对医学图像分析任务具有普适的参考价值。
4.  **高效实现的范例**：在性能超越部分SOTA的同时，显著降低了模型复杂度，展示了如何在Transformer时代通过巧妙的架构设计实现精度与效率的平衡。

## 8. 局限与问题
- **计算成本未明确比较**：虽然参数量减少了，但并行的四个Transformer分支和融合块可能带来较高的计算复杂度（FLOPs），论文未报告计算成本或训练/推理时间，与Swin UNETR等方法的效率对比不完整。
- **数据集相对单一**：所有实验仅在Synapse腹部CT数据集上进行，未在其他模态（如MRI）、其他部位（如心脏、脑部）或更大规模数据集上验证其泛化能力。
- **多孔径策略的深层分析不足**：“多孔径”避免了下采样带来的细节丢失，但论文未深入分析这种固定中心裁剪的策略与学习如何选择最有信息量区域的自适应策略相比有何优劣，其优势是否具有普适性有待更多验证。
- **可视化对比的细微差异**：在可视化对比（图2）中，作者承认MFTC-Net与3D TransUNet的分割结果差异“微小”，只能通过参数量来评判，这说明在该数据集上，不同方法的性能可能已接近瓶颈，本文方法的绝对优势仍需在更富挑战性的场景中检验。

## 9. 我该怎么使用这篇论文
- **快速了解**：阅读 **Abstract, Introduction（第1段和贡献列表）, Results（Table 1和可视化部分）, Conclusion**。重点看其核心思想、结果数字和可视化对比。
- **复现**：重点精读 **Section 3: Method**，特别是3.1（Swin Encoders的具体输入选择机制）、3.2（Fusion Block的结构和图1）、3.3（损失函数公式）以及 **Section 4: Implementation details**。代码已开源，需结合代码理解细节。
- **借鉴创新点**：
    - 学习 **多孔径（Multi-Aperture）** 的思想，思考如何在自己的任务中设计保持分辨率的多尺度上下文提取模块。
    - 学习 **3D融合块** 的组合设计，将多种注意力机制（SE, CBAM）与元素操作结合进行特征融合。
    - 学习 **损失函数** 中融入几何先验（距离变换）的设计思路。
- **写Related Work**：可将本文归入“**结合Transformer与CNN的医学图像分割方法**”或“**用于3D体积分割的混合架构**”这一类别，与3D TransUNet, Swin UNETR, UNETR++, TransFuse等放在一起讨论。

## 10. 和其他论文的关系
基于提供的主题 `D_3D_点云_分类_分割_配准` 和论文内容，本文很可能与以下方向或论文存在联系（使用`[[双链]]`表示）：
- `[[Swin UNETR]]`：本文直接对比并改进的基线方法之一，同样基于Swin Transformer。
- `[[3D TransUNet]]`：本文的主要对比方法，也是将Transformer用于3D医学分割的代表性工作。
- `[[UNETR++]]`：本文的对比方法，代表了另一种高效的Transformer-CNN混合设计。
- `[[TransFuse]]`：本文在相关工作中提及，代表了早期Transformer与CNN融合的思路。
- `[[CBAM]]` 和 `[[SE-Net]]`：本文融合块中直接使用的关键注意力模块。
- 由于主题是3D分割，也可能与 `[[点云分割]]` 领域的 `[[Point Transformer]]` 等方法在“处理三维数据的Transformer架构”这一高层理念上有交叉。

## 11. 关键词
MFTC-Net, 多孔径融合, Swin Transformer, 3D融合块, 医学图像分割, CT腹部器官分割, 距离变换损失, SE模块, CBAM, 混合架构, Synapse数据集

## 12. 可信度说明
本精读笔记的内容**严格基于提供的PDF提取文本生成**（共6页）。提取文本包含了论文的摘要、引言、相关工作、方法、实验结果、结论和参考文献，信息相对完整。主要的局限性在于：1）部分图表细节（如图1中融合块的精确连接方式）依赖于文字描述和图示说明，纯文本可能无法完全还原视觉信息；2）参考文献部分仅包含引用，未提供正文细节。因此，所有具体数字、方法描述和结论均来自文本，未进行任何编造或基于外部知识的补充。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (3800 字符/页)); 来源缓存: `.paper-cache/extracts/3DfusionBlock.txt` (6/6 页); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro).
<!-- AI_READING_NOTE_END -->
