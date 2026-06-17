---
title: 面向人脸修复篡改检测的大规模数据集
authors:
  - "李伟"
  - "黄添强"
  - "黄丽清"
  - "郑翱鲲"
  - "徐超"
year: 2024
venue: "中国图象图形学报"
doi: 10.11834/jig.230422
pdf: [[cjig_图像识别_多阶段空间感知道路损伤检测网络.pdf]]
primary_topic: J_人脸_表情_伪造_情感
topics:
  - "J_人脸_表情_伪造_情感"
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
extract_cache: .paper-cache/extracts/cjig_图像识别_多阶段空间感知道路损伤检测网络.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/15 pages"
---
# 面向人脸修复篡改检测的大规模数据集

## 基本信息
- **PDF**: [[cjig_图像识别_多阶段空间感知道路损伤检测网络.pdf]]
- **primary_topic**: `J_人脸_表情_伪造_情感`
- **topics**: `J_人脸_表情_伪造_情感`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

> **文件名说明**：本笔记的文件词干（stem）为 `cjig_图像识别_多阶段空间感知道路损伤检测网络`，但据 PDF 提取文本，该 PDF 的实际内容是《面向人脸修复篡改检测的大规模数据集》（Large-scale datasets for facial tampering detection with inpainting techniques），与"道路损伤检测"无关。词干疑似命名串台，正文以 PDF 真实内容为准。

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | 面向人脸修复篡改检测的大规模数据集 (Large-scale datasets for facial tampering detection with inpainting techniques) |
| **作者** | 李伟; 黄添强; 黄丽清; 郑翱鲲; 徐超（福建师范大学计算机与网络空间安全学院等） |
| **发表时间** | 2024 |
| **刊物/会议** | 中国图象图形学报 (Journal of Image and Graphics), 29(07): 1834-1848 |
| **DOI** | 10.11834/jig.230422 |
| **数据集开源** | https://pan.baidu.com/s/1-9HIBya9X-geNDe5zcJldw (pwd=thli) |

## 摘要

**英文原摘要（据 PDF 提取文本整理，修复空格与连字符断裂、剔除杂入的图表/版式数字）：**

> **Objective** DeepFake technology, born with the continuous maturation of deep learning techniques, primarily utilizes neural networks to create non-realistic faces. This method has enriched people's lives as computer vision advances and deep learning technologies mature. It has revolutionized the film industry by generating astonishing visuals and reducing production costs. Similarly, in the gaming industry, it has facilitated the creation of smooth and realistic animation effects. However, the malicious use of image manipulation to spread false information poses significant risks to society, casting doubt on the authenticity of digital content in visual media. Forgery techniques encompass four main categories: face reenactment, face replacement, face editing, and face synthesis. Face editing, a commonly employed image manipulation method, involves falsifying facial features by modifying the information related to the five facial regions. As one of the commonly employed methods in facial editing, image inpainting technology involves utilizing known content from an image to fill in missing areas, aiming to restore the image in a way that aligns as closely as possible with human perception. In the context of facial forgery, image inpainting is primarily used for identity falsification. To support research on detection methods for such manipulations, this paper produced a large-scale dataset for face manipulation detection based on inpainting techniques.
> **Method** This paper utilizes two classic datasets: the high-quality CelebA-HQ dataset (25 000 high-resolution 1 024 × 1 024 celebrity face images) and the low-quality FF++ dataset (15 000 face images extracted from video frames). Facial feature regions (eyebrows, eyes, nose, mouth, and the entire facial area) are segmented and corresponding mask images are created. Two deep neural network-based inpainting methods — CTSDG (image inpainting via conditional texture and structure dual generation) and RFR (recurrent feature reasoning for image inpainting) — along with one traditional inpainting method, SC (struct completion), were employed, resulting in a large-scale dataset comprising 600 000 images.
> **Result** Experimental results indicate a 15% decrease in detection accuracy for images derived from the FF++ dataset under the ResNet-50 benchmark detection network, and a 5% decline under Xception-Net. Significant variations in detection accuracy are observed among different facial regions, with the lowest accuracy recorded in the eye region at 0.91. Generalization experiments suggest that inpainted images from the same source dataset exhibit a certain degree of generalization across different facial regions, while minimal generalization is observed among datasets created from different source data. Visualization tools (Grad-CAM, integrated gradient) demonstrate that the detection network indeed focuses on the inpainted facial regions.
> **Conclusion** The use of image inpainting techniques for tampering introduces a challenging scenario that can deceive conventional tampering detectors to a certain extent. The provided large-scale dataset, encompassing high- and low-quality images with three distinct inpainting methods and various facial regions, fills the gap in available datasets and provides a benchmark for the field of image inpainting tampering detection, also supporting research on the generalization of such methods.

**中文翻译：**

> **目的**：图像合成方法随着计算机视觉与深度学习的成熟为生活带来了丰富体验，但用于传播虚假信息的恶意篡改图像也可能危害社会、令人怀疑数字内容的真实性。面部编辑是常用的篡改手段，通过修改五官信息伪造人脸；图像修复（inpainting）是面部编辑常用的手段之一，主要用于身份造假。为给此类篡改的检测方法研究提供数据支持，本文制作了面向人脸修复篡改检测的大规模数据集。
> **方法**：选用不同质量的源数据集——高质量人脸图像数据集 CelebA-HQ（2.5 万幅、1024×1024）与低质量人脸视频数据集 FF++（1.5 万幅、抽帧获得），先用图像分割方法分割面部五官区域并制作掩膜，再使用两种深度修复方法 CTSDG、RFR 及一种传统修复方法 SC，生成总数达 60 万幅的大规模修复图像数据集。
> **结果**：由 FF++ 数据集生成的图像在基准检测网络 ResNet-50 下检测精度下降 15%，在 Xception-Net 下下降 5%；不同面部部位检测精度差异较大，其中眼睛部位最低，为 0.91。泛化性实验表明，同一源数据集生成的数据在不同部位间存在一定泛化性，而不同源数据集间几乎没有泛化性。可视化工具（Grad-CAM、积分梯度）显示检测网络确实关注了被修复的面部区域。
> **结论**：基于图像修复的篡改方式在一定程度上可以骗过现有篡改检测器，研究此类检测方法具有现实意义。该数据集填补了领域空白，可作为修复图像篡改检测的基准，并支持泛化性研究。
> **关键词**：图像篡改；深度学习；图像修复；数据集；基准

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：深度伪造（DeepFake）是一把双刃剑，恶意运用会带来政治抹黑、军事欺骗、经济犯罪等社会安全风险。伪造技术主要分为面部重现、面部替换、面部编辑、全脸合成四大类；其中**图像修复（inpainting）**作为面部编辑的常用手段，可通过改变五官达到"更换人脸"的身份造假目的，隐蔽性强、威胁大。
- **之前方法的问题**：现有的人脸篡改数据集（如 FF++、Celeb-DF、DFDC 等）主要覆盖 DeepFake、FaceSwap、Face2Face、Neural Textures 等面部替换/重现方法，**没有针对"图像修复"这一类型的篡改数据**，导致研究相关检测网络缺乏数据基础。
- **核心矛盾**：修复篡改技术有效且隐蔽，但缺乏对应的大规模、标准化检测数据与基准，构成"篡改手段发展"与"检测研究数据/标准支撑"之间的不平衡。论文目标即制作并发布这样一份基准数据集。

## 关键贡献

论文在引言中明确列出三条主要贡献：

1. **制作大规模修复篡改检测数据集**：以 FF++（1.5 万幅，低质量，视频抽帧）和 CelebA-HQ（2.5 万幅，高质量 1024×1024）为源数据，分割五官区域后用三种修复方法生成总计 **60 万幅**修复图像，为该领域研究提供数据基础。
2. **建立质量评估与检测基准**：用人眼分辨及 SSIM、PSNR 评估修复图像质量，并用基准检测网络 ResNet-50、MesoNet、Xception-Net 对篡改效果进行检测，证明数据集的质量与挑战性。
3. **提出修复图像篡改数据集基准**：将生成数据拓展为一个可供后续研究使用与扩展的基准（benchmark）。

## 方法

- **整体框架（图 1）**：三个串行阶段——**源数据准备 → 五官分割与掩膜制作 → 图像修复**。
- **输入输出**：输入原始人脸图像（CelebA-HQ 或 FF++），输出指定面部区域被修复后的篡改图像及对应掩膜。
- **关键模块**：
    1. **图像分割模块（2.2）**：采用语义分割经典轻量级网络 **BiSeNet**（bilateral segmentation network，Yu 等，2018a）分割五官，在计算量、参数量与精度间取得平衡，可实时分割。对深度修复方法需提供五官**掩膜（mask）**，对传统算法只需分割后的图像。分割区域包括眼睛、鼻子、嘴巴、眉毛 4 个区域。
    2. **图像修复模块（2.3）**：三种原理不同的修复算法——
        - **CTSDG**（Guo 等，2021，基于结构信息约束）：双流网络，以耦合方式对"结构约束的纹理合成"与"纹理边缘引导的结构重建"建模；设计双向门控特征融合（Bi-GFF）模块交换结构/纹理信息，并用上下文特征聚合（CFA）模块通过区域亲和学习与多尺度特征聚合细化生成内容。
        - **RFR**（RFR-Net，Li 等，2020a，基于注意力机制）：作用于特征层面的渐进式修复网络（循环特征推理网络），由递归特征推理（RFR）模块与知识一致注意力（KCA）模块构成，反复推理孔洞边界、逐步由易到难修复大型掩膜中心区域。
        - **SC**（struct completion，Huang 等，2014，传统）：基于平面结构指导的基于补丁的传统方法，先估计平面投影参数将已知区域分割为 3 个相互垂直平面，再用块偏移/变换先验作为软约束完成填补。
- **数据集构成（2.4）**：以 FF++ 1.5 万幅 + CelebA-HQ 2.5 万幅为基础，分别用 3 种修复方式，在 **5 种面部区域**（眉毛、眼睛、鼻子、嘴巴，以及 4 部位同时修复）上修复，最终生成 60 万幅。
- **训练方式**：分割网 BiSeNet 需先训练以准确分割五官；三种修复方法用于数据生成阶段（深度方法需掩膜、传统方法直接在分割图像上操作）。论文未明确说明修复网络是否重训练，但描述以推理生成数据为主（PDF 文本未明确给出修复网络的重训练细节）。
- **和已有方法的差异**：此前篡改数据集主要通过面部替换/重现生成，本文**首次系统性、大规模地**针对"修复"这一篡改方式构建数据集与基准，填补该细分类型空白。

## 实验

- **实现细节**：代码用 Python 编写，使用 **4 张 Tesla V100s** 显卡训练/测试。检测网络训练设置：batch_size=12，学习率 10⁻⁴（并用 10⁻⁵ 微调），训练轮次 100，训练集中 80% 训练 / 20% 验证。每个二分类任务取 10 000 幅真实 + 10 000 幅修复图像作训练，5 000 + 5 000 作测试；图像尺寸调整至 256×256。
- **使用的数据集**：本文构建的 **60 万幅修复图像数据集**；对比放入检测网络的经典篡改数据集包括 UADFV、DeepFakeTIMIT(LQ/HQ)、DFDC、FF++、Celeb-DF 等。
- **检测网络（基准）**：ResNet-50、MesoNet（Afchar 等，2018）、Xception-Net（Chollet，2017）。
- **评价指标**：图像质量 SSIM、PSNR；检测性能 ACC（准确率）。
- **修复质量（3.1，表 1/2）**：深度修复（CTSDG、RFR）的 SSIM/PSNR 略高于传统 SC，说明深度网络修复更合适；眉毛、眼睛部位占图比例小，其 SSIM/PSNR 较高；用 FF++（低分辨率）制作的图像评价指标高于 CelebA-HQ。CelebA-HQ 上 RFR 的 SSIM 普遍达 0.98–0.99、PSNR 约 34–41 dB（表 1）。
- **检测效果（3.2，表 3，ACC%）**：与原始篡改数据相比，修复图像在检测网络上的检测精度**普遍下降**——FF++(inpainting) 在 ResNet-50 上 **74.1%**（相对 FF++ 原始 91.2% 下降约 15 个百分点），在 Xception 上 87.5%（相对 92.1% 下降约 5 个百分点）；CelebA-HQ(inpainting) 在 ResNet-50/MesoNet/Xception 上分别为 88.3 / 86.4 / 90.7。检测效果差证明数据集制作质量高、有挑战性。
- **部位差异（3.3，图 4）**：眼睛部位在整幅图中占比最小、修复区域最少，检测精度**最低**（摘要给出 0.91）；修复整张面部时待修复区域大、检测精度最高；传统 SC 修复质量低、存在伪影，检测器易识别，故精度也偏高。
- **泛化性（3.4，表 4，ACC）**：以 CelebA-HQ 为对象、Xception-Net 为检测器。**同一源数据集内**，深度修复方法间（CTSDG↔RFR）泛化性较强（多在 0.8–0.95 区间），但深度方法与传统 SC 之间泛化性较弱、用 SC 数据训练的网络在深度修复数据上几乎无泛化（多在 0.5 附近）。**不同源数据集间**（CelebA-HQ↔FF++）几乎没有泛化性（ACC 普遍约 0.50，接近随机）。
- **可视化（3.5，图 5/6）**：用 Grad-CAM 与积分梯度（integrated gradient）展示可解释性，结果显示 ResNet-50 检测网络确实关注被修复的区域，佐证数据集的有效性与特殊性。
- **速度/参数量/FLOPs**：PDF 文本未明确给出检测/修复网络的参数量与 FLOPs。

## 局限

1. **修复方法代表性有限**：仅用 CTSDG、RFR、SC 三种方法，未涵盖当下最热的**扩散模型**修复（论文相关工作提到 Repaint 等扩散修复，但未纳入数据集生成），可能低估更先进修复手段的威胁。
2. **源数据集仅两个**：只用 FF++ 与 CelebA-HQ，数据多样性与域覆盖有限。
3. **检测模型较旧且数量少**：评估用 ResNet-50、MesoNet、Xception-Net 均为较早的 CNN 结构，未评估 ViT、频域分析等更新检测方法（论文相关工作虽提及频率感知/双流频域方法，但实验未采用）。
4. **泛化性是开放问题**：跨源数据集几乎无泛化、传统↔深度修复间泛化弱，论文揭示了问题但未给出解决方案。
5. **实现细节未尽**：PDF 文本未给出修复网络是否重训练、数据集划分/存储格式/使用协议等完整细节（仅给出百度网盘开源地址）。

## 个人评论

1. **填补关键数据空白**：本文是修复篡改（inpainting tampering）检测领域少有的大规模、多因素（高/低质量 × 3 种修复方法 × 5 个部位）基准数据集，解决了该细分方向"无米之炊"的问题，工程价值明确。
2. **问题定义清晰**：把"基于修复的面部篡改"作为独立研究子类提出，并配套质量评估（SSIM/PSNR）+ 检测基准（ACC）+ 可视化（Grad-CAM/积分梯度）的完整评估闭环，方法论上自洽。
3. **最有价值的发现是泛化困境**：实验不仅证明修复篡改能骗过现有检测器（ACC 显著下降），更揭示了检测器对源数据分布与修复模式的强依赖——跨源数据集 ACC 跌到约 0.5、传统↔深度修复间泛化崩塌。这点中了当前篡改检测"过拟合特定伪造痕迹"的要害，对后续研究更有启发。
4. **可改进处**：数据集构造与检测器都偏"现成组件拼装"，缺少新模型；且未纳入扩散修复与 Transformer 检测器，时效性上略有滞后。作为基准资源使用价值高于方法创新。

### 使用建议

- **如果快速了解**：读摘要、引言（第 0 节）、实验（第 3 节，重点表 3、图 4、表 4）和结论，即可掌握动机、贡献与"泛化困境"这一核心发现。
- **如果复现/造数据**：精读第 2 节（2.1 源数据、2.2 BiSeNet 分割、2.3 三种修复方法、2.4 数据构成）与第 3.2 节训练设置（batch_size=12、lr=10⁻⁴/微调 10⁻⁵、100 epoch、80/20 划分、256×256、4×V100s）。
- **如果借鉴创新点**：学习其"多源 × 多修复方法 × 多部位"的数据集系统构造法，以及跨方法/跨源的泛化性评估实验设计，可迁移到其他篡改/生成数据集构建。
- **如果写 related work**：放在"人脸篡改检测数据集"小节，与 FF++、Celeb-DF、DFDC、DeeperForensics-1.0、FakeAVCeleb 等并列，突出其针对"修复篡改"的独特定位。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[J_人脸_表情_伪造_情感]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于计算机视觉与数字媒体取证（image forensics）方向，聚焦**人脸图像篡改检测**，更具体地针对一种长期被忽视的篡改手段——**基于图像修复（inpainting）的面部伪造**。论文并非提出新的检测模型，而是**构建并发布一个大规模基准数据集**，并系统评估现有检测器在其上的表现。因此它在 taxonomy 中应归入"人脸/伪造"（J_人脸_表情_伪造_情感），而非原标注的"目标检测"。注意：本笔记文件词干含"道路损伤检测"，但 PDF 实际内容是人脸修复篡改数据集，属命名串台，一切以 PDF 为准。

## 2. 一句话总结
本文构建了一个含 60 万幅图像的大规模人脸修复篡改检测基准数据集（源自 CelebA-HQ 与 FF++，经 BiSeNet 五官分割后用 CTSDG/RFR/SC 三种方法修复），并通过 SSIM/PSNR 与 ResNet-50/MesoNet/Xception-Net 的检测实验，揭示了修复篡改可显著降低检测精度、且跨源数据集与跨修复方法泛化性极弱的关键事实。

## 3. 背景与问题
- **为什么要做**：图像修复用于人脸身份造假（改五官换脸）隐蔽性强、社会威胁大，但现有人脸篡改数据集都未覆盖"修复"这一篡改类型，使相关检测网络研究缺乏数据。
- **之前方法的问题**：FF++、Celeb-DF、DFDC 等主流数据集主要由 DeepFake/FaceSwap/Face2Face/Neural Textures 等替换/重现方法生成，缺乏修复篡改样本与统一基准。
- **核心矛盾**：修复篡改有效且隐蔽 ↔ 检测研究的数据与标准严重匮乏。本文以制作并发布基准数据集来填补这一缺口。

## 4. 核心贡献
论文引言列出三条贡献：
1. **制作大规模修复篡改检测数据集**：FF++（1.5 万幅）+ CelebA-HQ（2.5 万幅）为源，五官分割后用 CTSDG、RFR、SC 三法修复，覆盖 5 种面部区域，生成总计 60 万幅。
2. **质量评估 + 检测基准**：用 SSIM、PSNR 评估修复质量，用 ResNet-50、MesoNet、Xception-Net 检测篡改效果，证明数据集质量与挑战性。
3. **提出修复图像篡改数据集基准**：把数据拓展为可供后续研究与扩展的 benchmark。

## 5. 方法详解
- **整体框架（图 1）**：源数据准备 → BiSeNet 五官分割 + 掩膜制作 → 三种方法图像修复，串行流水线。
- **源数据（2.1）**：FF++ 取 1 000 个未压缩真实视频、每隔 16 帧抽 1 帧、人脸裁剪后得 1.5 万幅；CelebA-HQ 取 2.5 万幅高质量（1024×1024）图像未做修改。
- **分割（2.2）**：BiSeNet 轻量语义分割网络分割眼/鼻/嘴/眉 4 区域；深度修复需掩膜，传统修复只需分割图像。
- **修复（2.3）**：
    - **CTSDG**（结构信息约束的双流网络）：耦合纹理合成与结构重建，含 Bi-GFF 双向门控特征融合与 CFA 上下文特征聚合模块。
    - **RFR-Net**（注意力机制的渐进式修复）：递归特征推理（RFR）+ 知识一致注意力（KCA），由易到难逐步修复大掩膜中心。
    - **SC**（平面结构指导的传统基于补丁方法）：估计平面投影参数分割为 3 个垂直平面，再用块偏移/变换先验软约束填补。
- **数据集构成（2.4）**：5 种面部区域（眉、眼、鼻、嘴 + 4 部位同时修复）× 3 种修复方式 × 2 源数据集，共 60 万幅。

## 6. 实验与结果
- **实现**：Python，4×Tesla V100s；检测网训练 batch_size=12、lr=10⁻⁴（微调 10⁻⁵）、100 epoch、80/20 划分、图像 256×256、训练 10 000+10 000、测试 5 000+5 000。
- **检测网络**：ResNet-50、MesoNet、Xception-Net；指标 ACC、SSIM、PSNR。
- **修复质量（表 1/2）**：深度修复 SSIM/PSNR 略优于 SC；眉/眼部位指标更高（占比小）；FF++ 生成图像指标高于 CelebA-HQ。
- **检测效果（表 3，ACC%）**：FF++(inpainting) 在 ResNet-50 上 74.1（vs FF++ 91.2，降约 15 个点），Xception 上 87.5（vs 92.1，降约 5 个点）；CelebA-HQ(inpainting) 在三网络上 88.3 / 86.4 / 90.7。检测精度普遍下降即证明数据集质量与挑战性。
- **部位差异（图 4）**：眼睛部位占比最小、修复区域最少 → 检测精度最低（摘要值 0.91）；整脸修复区域大 → 精度最高；传统 SC 有伪影易被识别 → 精度也高。
- **泛化性（表 4，ACC）**：同源数据集内 CTSDG↔RFR 泛化较强（0.8–0.95），但深度↔传统 SC 泛化弱、SC 训练的网络在深度修复数据上几乎无泛化（~0.5）；跨源数据集（CelebA-HQ↔FF++）几乎无泛化（ACC ~0.50 接近随机）。
- **可视化（图 5/6）**：Grad-CAM 与积分梯度显示 ResNet-50 确实关注被修复区域。
- **速度/参数量/FLOPs**：PDF 文本未明确。

## 7. 这篇论文真正有价值的地方
1. **填补数据空白**：修复篡改检测领域首个大规模、多因素（高/低质量 × 3 方法 × 5 部位）基准数据集，工程价值高。
2. **问题独立化**：把"基于修复的面部篡改"明确定义为独立研究子类，并配套质量评估 + 检测基准 + 可解释性可视化的完整评估方案。
3. **揭示泛化困境**：相比"修复能骗过检测器"，更重要的发现是检测器对源数据分布与修复模式的强依赖——跨源 ACC 跌至约 0.5、跨修复范式（传统↔深度）泛化崩塌，点中现有篡改检测过拟合伪造痕迹的要害。

## 8. 局限与问题
1. **修复方法时效性**：仅 CTSDG/RFR/SC，未纳入扩散模型修复（相关工作提及 Repaint），可能低估更先进伪造的威胁。
2. **源数据集仅两个**：FF++ 与 CelebA-HQ，多样性与域覆盖有限。
3. **检测模型较旧**：均为早期 CNN，未评估 ViT、频域分析等新检测器。
4. **泛化性未解决**：揭示问题但未提解决方法。
5. **细节缺失**：PDF 文本未给出修复网络重训练情况、数据划分/格式/协议（仅给百度网盘地址）。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言 + 第 3 节（表 3、图 4、表 4）+ 结论。
- **复现/造数据**：精读第 2 节（源数据、BiSeNet 分割、三种修复、数据构成）+ 第 3.2 节训练设置。
- **借鉴创新点**：学习"多源 × 多修复方法 × 多部位"的数据集系统构造法与跨方法/跨源泛化性评估设计。
- **写 related work**：放入"人脸篡改检测数据集"小节，与 FF++、Celeb-DF、DFDC、DeeperForensics-1.0、FakeAVCeleb 并列，突出"修复篡改"定位。

## 10. 和其他论文的关系
本文属人脸伪造/篡改检测（J 类）方向：
- **人脸篡改数据集**：与 `[[FaceForensics++]]`（FF++）、`[[Celeb-DF]]`、`[[DFDC]]`、`[[DeeperForensics-1.0]]`、`[[FakeAVCeleb]]` 同类，但专注修复篡改。
- **图像修复方法**：应用了 `[[CTSDG]]`、`[[RFR-Net]]`、`[[SC]]`（struct completion）等修复算法。
- **篡改检测骨干**：评估用 `[[ResNet]]`、`[[MesoNet]]`、`[[Xception-Net]]` 等常用检测网络。

## 11. 关键词
图像篡改, 深度学习, 图像修复, 数据集, 基准, 人脸伪造, 修复篡改, 检测, 泛化性, CelebA-HQ, FF++, CTSDG, RFR, SC, Grad-CAM

## 12. 可信度说明
本精读基于 PDF 提取文本（前 12/15 页）撰写，方法描述与实验数字（60 万幅、ResNet-50 上 ACC 91.2→74.1 即降约 15%、Xception 92.1→87.5 即降约 5%、眼睛部位 0.91、表 4 泛化 ACC 约 0.5、SSIM/PSNR 区间等）均直接取自文本。修复网络是否重训练、参数量/FLOPs、完整数据集划分协议等 PDF 文本未明确，已在正文标注。重要更正：原笔记的 `primary_topic` 误标为 C2（目标检测），据 PDF 实际内容应为 J（人脸/伪造/篡改），已同步修正三处；文件词干"道路损伤检测"与内容不符，疑为命名串台。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页)); 来源缓存: `.paper-cache/extracts/cjig_图像识别_多阶段空间感知道路损伤检测网络.txt` (15/15 页; 原 AI 主体 12/15 + 全文补读 13-15); 生成日期: 2026-06-05; 模式: LLM (mimo-v2.5-pro)。本轮已据 PDF 提取文本重建乱码摘要、核对实验数值并修正主题分类（C2→J）。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-15; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-15。
- **提取情况**: 缺失页 3 页, 其中 3 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Table 5 The content of the inpainting datasets
- p.14: IEEE/CVF International Conference on Computer Vision Workshop
- p.14: Robust algorithm for exemplar -based image inpainting//Proceedings

### 缺失页关键摘录

- p.13: Table 5 The content of the inpainting datasets
- p.14: deepfake detection challenge （DFDC ） preview dataset ［EB/OL ］.
- p.14: 0： a large -scale dataset for real -world face forgery detection//Pro ⁃
- p.14: audio -video multimodal deepfake dataset ［EB/OL ］.［2023 -06-20］.
- p.14: large -scale challenging dataset for deepfake forensics//Proceedings
<!-- AI_READING_NOTE_END -->
