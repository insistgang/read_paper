---
title: "FFA-Net: Feature Fusion Attention Network for Single Image Dehazing"
authors:
  - "Xu Qin"
  - "Zhilin Wang"
  - "Yuanchao Bai"
  - "Xiaodong Xie"
  - "Huizhu Jia"
year: 2020
venue: "AAAI 2020"
doi: 
pdf: [[FFA.pdf]]
primary_topic: E_图像复原_超分_去噪_去雨去雾
topics:
  - "E_图像复原_超分_去噪_去雨去雾"
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
extract_cache: .paper-cache/extracts/FFA.txt
---

# FFA-Net: Feature Fusion Attention Network for Single Image Dehazing

## 基本信息
- **PDF**: [[FFA.pdf]]
- **primary_topic**: `E_图像复原_超分_去噪_去雨去雾`
- **topics**: `E_图像复原_超分_去噪_去雨去雾`, `B_注意力算子模块`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | FFA-Net: Feature Fusion Attention Network for Single Image Dehazing |
| **作者** | Xu Qin¹*; Zhilin Wang²*; Yuanchao Bai¹; Xiaodong Xie¹†; Huizhu Jia¹ (¹北京大学电子工程与计算机科学学院; ²北京航空航天大学计算机学院; *前两位作者贡献相同; †通讯作者) |
| **发表时间** | 2020 (AAAI 2020; arXiv 预印本 1911.07559v2, 2019-12-05) |
| **刊物/会议** | AAAI 2020 (Association for the Advancement of Artificial Intelligence) |
| **DOI** | 未明确 (代码已开源, 见原文 GitHub) |

## 摘要

> In this paper, we propose an end-to-end feature fusion attention network (FFA-Net) to directly restore the haze-free image. The FFA-Net architecture consists of three key components: 1) A novel Feature Attention (FA) module combines Channel Attention with Pixel Attention mechanism, considering that different channel-wise features contain totally different weighted information and haze distribution is uneven on the different image pixels. FA treats different features and pixels unequally, which provides additional flexibility in dealing with different types of information, expanding the representational ability of CNNs. 2) A basic block structure consists of Local Residual Learning and Feature Attention; Local Residual Learning allowing the less important information such as thin haze region or low-frequency to be bypassed through multiple local residual connections, lets main network architecture focus on more effective information. 3) An Attention-based different levels Feature Fusion (FFA) structure, the feature weights are adaptively learned from the Feature Attention (FA) module, giving more weight to important features. This structure can also retain the information of shallow layers and pass it into deep layers. The experimental results demonstrate that our proposed FFA-Net surpasses previous state-of-the-art single image dehazing methods by a very large margin both quantitatively and qualitatively, boosting the best published PSNR metric from 30.23 dB to 36.39 dB on the SOTS indoor test dataset.

> **中文翻译**: 本文提出一个端到端的特征融合注意力网络 (FFA-Net), 直接复原无雾图像。FFA-Net 由三个关键组件构成: 1) 一个新颖的特征注意力 (FA) 模块, 将通道注意力与像素注意力机制相结合——考虑到不同通道的特征蕴含的加权信息完全不同, 且雾在不同图像像素上分布不均匀。FA 对不同特征和像素区别对待, 为处理不同类型信息提供了额外灵活性, 扩展了 CNN 的表征能力。2) 一个由局部残差学习 (Local Residual Learning) 与特征注意力构成的基础块结构; 局部残差学习让薄雾区域或低频等次要信息可经由多条局部残差连接被旁路, 使主干网络聚焦于更有效的信息。3) 一个基于注意力的多层级特征融合 (FFA) 结构, 其特征权重由 FA 模块自适应学习, 为重要特征赋予更大权重; 该结构还能保留浅层信息并传入深层。实验表明, FFA-Net 在定量与定性上都以巨大优势超越先前最先进的单图像去雾方法, 将 SOTS 室内测试集上的最佳已发表 PSNR 从 30.23 dB 提升到 36.39 dB。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**: 单幅图像去雾是计算机视觉中的基础低级视觉任务。大气中的烟、尘、雾等悬浮粒子会导致图像出现颜色失真、模糊、低对比度等质量退化, 使分类、跟踪、行人重识别、目标检测等高级视觉任务更难求解; 去雾常作为这些高级任务的预处理步骤。物理上, 去雾基于大气散射模型 `I(z)=J(z)t(z)+A(1-t(z))` (式1), 其中 `I` 为观测有雾图, `A` 为全局大气光, `t(z)` 为介质透射图, `J` 为无雾图; 在 `A` 与 `t(z)` 未知时这是一个欠定/病态问题。
- **之前方法的问题**: 1) **先验方法** (如 DCP 暗通道先验): 当场景物体颜色接近大气光时先验易被违背, 导致透射图估计不准, 在真实场景中可能失效。2) **已有 CNN 去雾方法**: 把通道特征与像素特征同等对待 (treat channel-wise and pixel-wise feature equally), 但雾在图像中分布不均匀 (薄雾与厚雾区域应有不同权重), 且 DCP 也指出不同颜色通道蕴含的加权信息完全不同; 同等对待会把大量资源浪费在次要信息的无谓计算上, 网络无法覆盖所有像素与通道, 严重限制表征能力。
- **核心矛盾**: **雾/通道信息的不均匀分布** 与 **现有网络对特征和像素的平等对待** 之间的矛盾。作者希望网络能自适应地把算力倾斜到更重要的信息 (厚雾区域、关键通道、高频纹理)。FA 模块的设计明确受 (Zhang et al. 2018, 即 RCAN 通道注意力) 启发, 并进一步引入像素注意力。

## 关键贡献

1.  **提出端到端特征融合注意力网络 (FFA-Net)**: 在单图像去雾上以巨大优势超越先前 SOTA, 在厚雾且纹理丰富的区域、以及图像细节与色彩保真度上表现尤为突出 (图1、图8)。
2.  **提出特征注意力 (FA) 模块**: 将 **通道注意力 (CA)** 与 **像素注意力 (PA)** 相结合, 为处理不同类型信息提供额外灵活性, 把更多注意力放在厚雾像素和更重要的通道信息上。
3.  **提出由局部残差学习 (LRL) + 特征注意力构成的基础块**: 局部残差让薄雾区域与低频信息经多条跳连被旁路, FA 进一步提升网络容量; 实验显示该结构还能改善训练稳定性。
4.  **提出基于注意力的特征融合 (FFA) 结构**: 既能保留浅层信息并传入深层, 又能自适应学习不同层级特征的权重 (由 FA 模块给出), 比直接人工指定权重的融合方式效果显著更好。

## 方法

- **整体框架** (图2): 输入有雾图像 → **浅层特征提取** → **N 个组结构 (Group Architecture, 含多条跳跃连接)** → 将 N 个组结构的输出在通道维拼接后, 经 **特征融合注意力 (FFA)** 自适应加权融合 → **重建部分 (两层卷积)** + **全局残差学习 (长跳连)** → 输出无雾图像。(注: 引言/框架描述用 "N 个组结构", 实现细节中实际取 G=3。)
- **输入输出**: 输入一张有雾 RGB 图像, 输出复原后的无雾 RGB 图像; 端到端, 不显式估计大气光 `A` 或透射图 `t(z)`。
- **关键模块**:
    1.  **特征注意力 (FA)** (图3) = 通道注意力 + 像素注意力, 串联 (先 CA 后 PA):
        - **通道注意力 (CA)**: 先全局平均池化把 C×H×W 压成 C×1×1 的通道描述符 `gc=Hp(Fc)` (式3), 再过两层卷积 (中间 ReLU, 末端 Sigmoid) 得权重 `CAc=σ(Conv(δ(Conv(gc))))` (式4), 与输入逐元素相乘 `Fc*=CAc⊗Fc` (式5)。CA 关注 "不同通道蕴含不同加权信息" (呼应 DCP)。
        - **像素注意力 (PA)**: 将 CA 输出 `Fc*` 送入两层卷积 (ReLU + Sigmoid), 形状由 C×H×W 变为 1×H×W, 得 `PA=σ(Conv(δ(Conv(Fc*))))` (式6); 再与 `Fc*` 逐元素相乘得 FA 输出 `F̃=Fc*⊗PA` (式7)。PA 让网络聚焦厚雾像素与高频区域 (边缘、纹理), 可视化见图4。
    2.  **基础块 (Basic Block)** (图6): 由局部残差学习 (LRL) 跳连 + 一个 FA 模块构成。LRL 让薄雾/低频等次要信息经跳连旁路, 使主干聚焦有效信息, 并改善训练稳定性 (图7)。
    3.  **组结构与全局残差学习**: 每个组结构由 **B 个基础块** + 跳连构成 (连续 B 块增加深度与表达力, 跳连缓解训练困难)。网络共 **G 个组结构**。末端用两层卷积的恢复部分 + 一条长跳连全局残差, 复原无雾图。
    4.  **特征融合注意力 (FFA)**: 把 G 个组结构输出在通道维拼接, 再乘以由 FA 自适应学习的权重做融合, 从而保留低层信息并传入深层, 让网络更关注厚雾区、高频纹理与色彩保真等有效信息。
- **损失函数**: 默认采用 **L1 损失** (式8) `L(Θ)=(1/N)Σ‖I_gt^i − FFA(I_haze^i)‖`。文中指出: MSE/L2 虽最常用, 但 (Lim et al. 2017) 发现许多图像复原任务用 L1 在 PSNR/SSIM 上更优, 故选 L1; 未采用感知损失或 GAN 损失。
- **超参数 (Implementation Details)**: G=3 个组结构; 每组 B=19 个基础块; 除通道注意力的卷积核为 **1×1** 外, 其余卷积核均为 **3×3**; 除 CA 模块外所有特征图尺寸保持不变; 每个组结构输出 **64** 个通道 (filters)。
- **训练**: 在 RGB 通道训练; 数据增强为随机旋转 (90/180/270°) + 水平翻转; 输入为 **240×240** 图像块; 室内训练 **5×10⁵** 步、室外 **1×10⁶** 步; Adam (β₁=0.9, β₂=0.999); 初始学习率 **1×10⁻⁴**, 采用余弦退火衰减至 0 (式9); PyTorch 实现, 单卡 RTX 2080Ti。
- **和已有方法的差异**: 与 DehazeNet、MSCNN 等 "先估计透射图再复原" 的范式不同, FFA-Net 端到端直接复原无雾图; 与 AOD-Net、GCANet 等同等对待全部特征/像素的网络不同, FFA-Net 用 FA/FFA 机制按雾分布与通道重要性自适应分配权重。

## 实验

- **数据集**: **RESIDE** (Li et al. 2018) 去雾基准, 合成雾图源自深度数据集 NYU Depth V2 (室内) 与 Middlebury 立体数据集 (室外)。训练用 **Indoor Training Set** (1399 张清晰图, 对应生成 13990 张有雾图; 全局大气光 0.8~1.0, 散射参数 0.04~0.2)。测试用 **SOTS (Synthetic Objective Testing Set)**, 含 **500 室内 + 500 室外** 合成雾图; 另在 **Realistic Hazy Images** 真实雾图上做主观评估。
- **指标**: **PSNR** 与 **SSIM** (指标值引自 Li et al. 2018 与 Qu et al. 2019)。
- **对比方法**: 表1 列出 DCP、AOD-Net、DehazeNet、GFN、GCANet; 结果章节的定性对比聚焦其中四个 SOTA (DCP、AOD-Net、DehazeNet、GCANet)。
- **主结果** (表1):
    - **SOTS 室内**: FFA-Net PSNR **36.39 dB** / SSIM **0.9886**, 较之前最好的 GCANet (30.23 dB / 0.9800) 提升 **6.16 dB**。
    - **SOTS 室外**: FFA-Net PSNR **33.57 dB** / SSIM **0.9840**。
    - 其余对比 (室内/室外 PSNR): DCP 16.62/19.13, AOD-Net 19.06/20.29, DehazeNet 21.14/22.46, GFN 22.30/21.55, GCANet 30.23/— (室外未报)。
    - 定性 (图8): DCP 因先验假设出现严重色偏并丢失景深细节; AOD-Net 去雾不彻底且偏暗; DehazeNet 偏亮; GCANet 在纹理、边缘、蓝天等高频细节欠佳。FFA-Net 在细节与色彩保真上更优, 真实雾图中甚至能 "复原" 出深处隐约的塔、湿润带纹理与雨滴的路面。
- **消融** (表2, 48×48 输入, 3×10⁵ 步, 其余配置同正式实现):
    - 仅 FA: **30.28 dB**;
    - FA + 局部残差学习 (LRL): **31.16 dB**;
    - FA + LRL + 特征融合注意力 (FFA): **32.44 dB**。
    - 说明: 此消融为缩小配置 (小块、少步数); 若按论文完整实现配置训练, PSNR 可达 **35.77 dB**。结论是每个组件都对性能有贡献, FFA 结构尤为关键, 且仅用 FA 也已颇具竞争力。
- **效率信息**: PDF 文本中**未明确给出** FFA-Net 的参数量、FLOPs 或推理速度 (仅说明使用单卡 RTX 2080Ti 训练)。

## 局限

1.  **数据依赖**: 训练与定量评测主要在合成雾图 (RESIDE) 上进行; 虽有真实雾图的主观测试, 但在真实世界复杂多变雾况下的泛化未做定量验证。
2.  **计算成本未量化**: 网络较深 (G=3, B=19, 共 57 个基础块, 每组 64 通道, 大量 FA 模块), 论文未提供参数量/FLOPs/运行时间等效率对比, 对部署不够友好。
3.  **物理假设的隐性局限**: 方法虽端到端隐式学习, 但问题本质仍源于大气散射模型; 在该模型不成立的极端场景 (非均匀雾、雾霾混合) 下可能失效。
4.  **消融设置与正式实现不一致**: 消融用更小图像块 (48×48) 与更少步数 (3×10⁵), 与正式实现 (240×240, 5×10⁵/1×10⁶ 步) 不同, 各组件在最终大模型中的真实贡献可能与消融数值有偏差。

## 个人评论

1.  **问题洞察精准**: 把 "雾分布不均匀" 与 "通道特征加权信息不同" 这两个被先前 CNN 去雾忽视的事实显式化, 并据此设计网络, 这种从问题本质 (而非堆模块) 出发的思路值得学习。
2.  **注意力的组合设计**: 不是单独用通道或空间注意力, 而是把二者串联 (先 CA 后 PA) 成 FA 模块; 这种 "通道选哪些图、像素选哪些位置" 的两段式选择, 对其他视觉任务的特征精炼有迁移价值。
3.  **信息分流 + 信息聚焦的耦合**: 基础块把局部残差 (让次要信息绕行) 与注意力 (让主干聚焦) 结合, 既稳训练又增表达, 是性价比很高的结构设计。
4.  **可学习的多层级融合**: FFA 让网络自学不同层级特征的融合权重, 优于人工指定或简单拼接; 这一 "用注意力做特征融合" 的思想可泛化到检测、分割等需要多尺度/多层级融合的任务。
5.  **强基线价值**: 模块虽多, 但整体仍是清晰的端到端映射, 易复现; 6.16 dB 的 PSNR 跃升使其成为后续去雾工作长期对标的强基线。

### 使用建议

- **快速了解**: 读摘要 + 引言末尾的四点贡献, 即可掌握核心思想。
- **复现**: 精读 "Fusion Feature Attention Network (FFA-Net)" (模块结构与式3~7) 与 "Implementation Details / Training Settings" (G=3, B=19, 64 通道, 1×1/3×3 卷积核, L1 损失, Adam, 1e-4 余弦退火, 240×240, 5e5/1e6 步)。
- **借鉴创新点**: 重点学 FA (CA+PA 串联)、基础块 (LRL+FA)、FFA (注意力加权融合) 三件套, 思考迁移到图像复原/增强乃至检测分割骨干。
- **写 Related Work**: 可放在 "单幅图像去雾" (对比 DCP、DehazeNet、AOD-Net、GCANet、GFN、EPDN) 与 "视觉注意力机制" (对比 SENet、CBAM、RCAN) 两节, 突出其 "通道+像素注意力 + 注意力做多层级融合" 的特色。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页:
> - [[E_图像复原_超分_去噪_去雨去雾]]
> - [[B_注意力算子模块]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文是计算机视觉**低级视觉**中的**单幅图像去雾 (single image dehazing)** 工作 (AAAI 2020)。它要解决的是: 给定一张有雾 RGB 图像, 端到端直接复原无雾图像, 不显式估计大气光与透射图。从方法论看, 论文的载体是图像复原网络, 故主题归入 **E_图像复原_超分_去噪_去雨去雾** 最贴切; 其核心技术创新 (FA 模块 = 通道注意力 + 像素注意力, 以及用注意力做特征融合) 又使它与 **B_注意力算子模块** 高度相关, 可作为注意力算子在复原任务上的代表性应用。

## 2. 一句话总结
FFA-Net 用 "通道注意力 + 像素注意力" 串联的特征注意力 (FA) 模块、"局部残差 + FA" 的基础块, 以及 "注意力自适应加权" 的多层级特征融合 (FFA), 实现端到端单图像去雾, 把 SOTS 室内 PSNR 从 30.23 dB 提到 36.39 dB。

## 3. 背景与问题
- **为什么要做**: 去雾是高级视觉任务 (分类/检测/跟踪/重识别) 的预处理。基于大气散射模型 `I=J·t+A·(1-t)` (式1), 在 `A`、`t(z)` 未知时是病态问题。
- **先验方法的问题**: DCP 等先验在物体颜色接近大气光时易失效, 透射图估计不准。
- **已有 CNN 的问题**: 把通道与像素特征同等对待, 但雾分布不均 (薄雾 vs 厚雾权重应不同), 不同通道蕴含的加权信息也完全不同 (DCP 佐证); 同等对待浪费算力、限制表征能力。
- **核心矛盾**: 信息分布的不均匀性 vs 网络的均匀处理。解决路径是引入按通道、按像素的自适应注意力。

## 4. 核心贡献
1.  端到端 FFA-Net, 大幅超越先前 SOTA, 尤擅厚雾 + 富纹理区与色彩保真。
2.  **FA 模块**: 通道注意力 (CA) + 像素注意力 (PA) 组合, 聚焦厚雾像素与重要通道。
3.  **基础块**: 局部残差学习 (LRL) + FA, 让次要信息绕行、主干聚焦, 并稳训练。
4.  **FFA 结构**: 注意力自适应学习多层级特征权重做融合, 保留浅层信息并优于人工指定权重。

## 5. 方法详解
- **框架** (图2): 有雾图 → 浅层特征提取 → N 个组结构 (多跳连) → 通道维拼接 → FFA 加权融合 → 两层卷积重建 + 全局残差长跳连 → 无雾图。实现中 G=3。
- **FA 模块** (图3, 先 CA 后 PA):
    - CA: 全局平均池化得 C×1×1 描述符 `gc=Hp(Fc)` (式3) → 两层卷积 (ReLU/Sigmoid) 得 `CAc=σ(Conv(δ(Conv(gc))))` (式4) → `Fc*=CAc⊗Fc` (式5)。
    - PA: 将 `Fc*` 过两层卷积得 1×H×W 的 `PA=σ(Conv(δ(Conv(Fc*))))` (式6) → `F̃=Fc*⊗PA` (式7)。PA 聚焦厚雾像素与高频区 (图4)。
- **基础块** (图6): LRL 跳连 + FA, 旁路薄雾/低频, 改善稳定性 (图7)。
- **组结构 + 全局残差**: 每组 B 个基础块 + 跳连; 末端两层卷积恢复 + 长跳连全局残差。
- **FFA**: G 个组结构输出在通道维拼接后乘以 FA 自适应权重融合。
- **损失**: L1 损失 (式8); 引用 (Lim 2017) 说明 L1 在 PSNR/SSIM 上常优于 L2, 故弃用 MSE/感知/GAN 损失。
- **超参**: G=3; B=19; CA 卷积核 1×1, 其余 3×3; 每组输出 64 通道; 除 CA 外特征图尺寸不变。

## 6. 实验与结果
- **数据集**: RESIDE。Indoor Training Set (1399 清晰 / 13990 有雾; 大气光 0.8~1.0, 散射参数 0.04~0.2)。测试 SOTS (500 室内 + 500 室外) + 真实雾图主观评估。
- **指标**: PSNR、SSIM (引自 Li 2018 / Qu 2019)。
- **对比方法**: DCP、AOD-Net、DehazeNet、GFN、GCANet (定性聚焦四个 SOTA)。
- **主结果 (表1, PSNR/SSIM)**:
    - 室内: Ours **36.39 / 0.9886**; GCANet 30.23/0.9800; GFN 22.30/0.8800; DehazeNet 21.14/0.8472; AOD-Net 19.06/0.8504; DCP 16.62/0.8179。
    - 室外: Ours **33.57 / 0.9840**; DehazeNet 22.46/0.8514; GFN 21.55/0.8444; AOD-Net 20.29/0.8765; DCP 19.13/0.8148; GCANet 室外未报。
    - 室内较 GCANet 提升 6.16 dB。
- **训练设置**: 240×240 块; 室内 5×10⁵ / 室外 1×10⁶ 步; Adam (0.9,0.999); lr 1e-4 余弦退火; PyTorch + RTX 2080Ti。
- **消融 (表2, 48×48, 3×10⁵ 步)**: FA 30.28 → FA+LRL 31.16 → FA+LRL+FFA 32.44; 完整配置可达 35.77 dB。FFA 贡献最关键, 仅 FA 也已具竞争力。
- **效率**: 参数量/FLOPs/速度在提取文本中未明确。

## 7. 这篇论文真正有价值的地方
1.  把 "雾不均匀 + 通道加权不同" 显式化, 并据此引入按通道/按像素的注意力——问题驱动的设计范式。
2.  FA 把通道注意力与像素注意力串联, 形成 "选图 + 选位置" 的两段式特征选择, 迁移性强。
3.  局部残差 (分流) 与注意力 (聚焦) 在基础块中耦合, 兼顾训练稳定与表征能力。
4.  用注意力做多层级特征融合 (FFA), 比人工指定权重更优, 思想可泛化到检测/分割的多尺度融合。
5.  6.16 dB 的客观提升 + 易复现的端到端结构, 使其成为去雾领域的强基线。

## 8. 局限与问题
1.  定量评测限于合成雾 (RESIDE), 真实雾仅主观, 真实世界泛化未定量验证。
2.  网络较深 (G=3, B=19, 共 57 基础块), 但无参数量/FLOPs/速度的效率报告。
3.  本质仍依托大气散射模型假设, 非均匀雾/雾霾混合等极端场景可能失效。
4.  消融用更小块 (48×48) 与更少步数 (3×10⁵), 与正式实现不一致, 各组件真实贡献可能有偏。

## 9. 我该怎么使用这篇论文
- **快速了解**: 摘要 + 引言四点贡献。
- **复现**: 精读 FFA-Net 方法节 (式3~7) 与 Implementation/Training Settings (G=3, B=19, 64 通道, 1×1/3×3 核, L1, Adam, 1e-4 余弦退火, 240×240, 5e5/1e6 步, RTX 2080Ti)。
- **借鉴创新点**: FA (CA+PA)、基础块 (LRL+FA)、FFA (注意力加权融合) 三件套, 迁移到图像复原/增强或检测分割骨干。
- **写 Related Work**: "单幅图像去雾" (DCP/DehazeNet/AOD-Net/GCANet/GFN/EPDN) 与 "视觉注意力" (SENet/CBAM/RCAN) 两节均可引用。

## 10. 和其他论文的关系
- **去雾谱系 (提取文本明确提及)**: 物理先验 DCP (He 2010)、颜色衰减先验 (Zhu 2015)、非局部先验 (Berman 2016); 学习方法 DehazeNet (Cai 2016)、MSCNN (Ren 2016)、AOD-Net (Li 2017)、GFN (Ren 2018)、GCANet (Chen 2019)、EPDN (Qu 2019)。FFA-Net 属 "端到端直接复原" 一支, 不显式估计透射图。
- **注意力血缘**: FA 模块的通道注意力明确受 (Zhang et al. 2018, RCAN) 启发, 并新增像素注意力; 与 SENet (通道注意力)、CBAM (通道+空间) 同源但更针对去雾任务。
- **特征融合**: FFA 的 "保留浅层并融入深层" 借鉴了 U-Net (Ronneberger 2015) 的多层级整合思想, 但用注意力做自适应加权而非简单拼接/跳连。

## 11. 关键词
单图像去雾, 特征注意力, 通道注意力, 像素注意力, 局部残差学习, 特征融合, 大气散射模型, 端到端复原, RESIDE/SOTS, PSNR/SSIM, L1 损失, FFA-Net

## 12. 可信度说明
本篇精读基于 FFA.pdf 的 8/8 页提取文本 (约 3130 字符/页, 质量良好, 含摘要、引言、方法全部公式 (式1~9)、Table 1/2 完整数值、实现细节)。所有模块描述、公式、超参数、数据集规模、PSNR/SSIM 数值均能在提取文本中逐条核对。提取文本在第 25000 字符处截断 (原文 32543 字符), 截断部分主要为结论/致谢, 不影响核心事实。本轮已修正的关键事项: 发表年份/会议 (原 frontmatter 误作 2019/乱码 venue, 据版权页改为 AAAI 2020)、作者署名乱码已清理、主题由 B 调整为 E (复原任务) 并保留 B 为次主题。仍存疑/未覆盖项已在正文标注 "未明确"。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 约 3130 字符/页, 8/8 页); 来源缓存: `.paper-cache/extracts/FFA.txt` (8/8 页, 第 25000 字符后截断); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。
<!-- AI_READING_NOTE_END -->
