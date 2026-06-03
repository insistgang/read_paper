# 论文主题分类清单

- **总计**: 499 份 PDF
- **已归类**: 499
- **未归类**: 0

> 说明：基于**文件名**做关键词匹配归类，未读 PDF 内容。
> 一个文件只归入第一个匹配上的主题（前缀优先级）。
> 主题代号：A=医学, B=算子, C=检测, D=3D, E=复原, F=分割, G=VLM, H=显著, I=文本, J=人脸, K=视频, L=数据集, M=行人, N=数学, O=安全, P=跨域, Q=自监督, R=综述, S=变化检测, T=其他, U=未归类, Z=杂项

## 主题分布

| 主题 | 数量 |
|------|------|
| Z_工具与杂项_figures | 18 |
| A1_医学图像_分割 | 17 |
| A1b_医学图像_小样本_综述 | 1 |
| A2_医学图像_分类_配准_生成 | 26 |
| A3_医学图像_配准_切片_张量_数学 | 3 |
| B_注意力算子模块 | 134 |
| C_目标检测_通用与旋转框 | 29 |
| C2_目标检测_违建_车辆_船舶_行人 | 23 |
| C3_目标检测_红外_可见光融合 | 1 |
| D_3D_点云_分类_分割_配准 | 28 |
| D2_3D_重建_神经辐射场_SLAM | 10 |
| E_图像复原_超分_去噪_去雨去雾 | 15 |
| F_图像分割_语义_实例_全景 | 15 |
| G_视觉基础模型_VLM_LLM | 16 |
| I_场景文本_OCR | 5 |
| J_人脸_表情_伪造_情感 | 7 |
| K_跟踪_视频_动作 | 4 |
| L_数据集_Benchmark | 8 |
| M_行人_重识别_检索 | 3 |
| N_雷达_无线电_张量_数学 | 22 |
| O_物理对抗_安全_鲁棒 | 2 |
| P_跨域_域自适应_联邦 | 2 |
| Q_自监督_对比学习_主动学习 | 5 |
| R_综述_Survey | 19 |
| S_变化检测_ChangeDetection | 7 |
| R1_遥感_高光谱_变化检测 | 4 |
| R2_控制_生物启发_其他跨学科 | 9 |
| T_通用_NLP_其他 | 66 |

## 详细清单

### Z_工具与杂项_figures（18）

- Author_Biography.pdf
- Cover_Letter.pdf
- benchmark_overview.pdf
- budget_fairness_accounting.pdf
- controlled_ablation.pdf
- dataset-imgs-QAs.pdf
- dataset.pdf
- dataset_analysis_12.pdf
- dataset_analysis_v5_img_dis.pdf
- dataset_analysis_v5_qst_length.pdf
- figure1.pdf
- illustration_v2.pdf
- parameter_sensitivity_scan.pdf
- results-question-type-radar.pdf
- scalability_overview.pdf
- supplemental_parameter_scans.pdf
- tradeoff_curve.pdf
- trigger_rate_validation.pdf

### A1_医学图像_分割（17）

- CMUNeXtBlock.pdf
- CoNIC-Challenge--Pushing-the-frontiers-of-nuclear-detectio_2024_Medical-Imag.pdf
- Content-Noise_Complementary_Learning_for_Medical_Image_Denoising.pdf
- Contrastive_and_Selective_Hidden_Embeddings_for_Medical_Image_Segmentation.pdf
- Dual_Adversarial_Attention_Mechanism_for_Unsupervised_Domain_Adaptive_Medical_Image_Segmentation.pdf
- Few-Shot_Medical_Image_Segmentation_via_Generating_Multiple_Representative_Descriptors.pdf
- HiFi-Mamba MRI重建 HiFi-Mamba MRI Reconstruction.pdf
- HiFi-MambaV2分层MRI HiFi-MambaV2 Hierarchical MRI.pdf
- LViT_Language_Meets_Vision_Transformer_in_Medical_Image_Segmentation.pdf
- LightM-UNet.pdf
- LocalViT.pdf
- Rethinking-masked-image-modelling-for-medical-image-r_2024_Medical-Image-Ana.pdf
- 全监督和弱监督图网络的病理图像分割.pdf
- 基于深度学习的医学图像分割方法综述.pdf
- 小波框架血管分割 Tight-Frame Vessel.pdf
- 框架管状结构分割 Framelet.pdf
- 直肠分割放疗 Deep Rectum.pdf

### A1b_医学图像_小样本_综述（1）

- 医学图像小样本学习 Medical Few-Shot.pdf

### A2_医学图像_分类_配准_生成（26）

- 2024_2405.04974_Diffusion_Brain_MRI.pdf
- A-comprehensive-survey-on-deep-active-learning-in-medi_2024_Medical-Image-An.pdf
- A-survey-on-deep-learning-in-medical-image-registration--Ne_2025_Medical-Ima.pdf
- A_Collaborative_Self-Supervised_Domain_Adaptation_for_Low-Quality_Medical_Image_Enhancement.pdf
- Anonymizing-medical-case-based-explanations-through-d_2024_Medical-Image-Ana.pdf
- Assessing_the_Ability_of_Generative_Adversarial_Networks_to_Learn_Canonical_Medical_Image_Statistics.pdf
- Beam-wise-dose-composition-learning-for-head-and-neck-can_2024_Medical-Image.pdf
- Deep-learning-based-synthesis-of-MRI--CT-and-PET--Revi_2024_Medical-Image-An.pdf
- Deep-learning-models-for-ischemic-stroke-lesion-seg_2024_Computers-in-Biolog.pdf
- Explainable-artificial-intelligence--XAI--in-deep-learni_2022_Medical-Image-.pdf
- Guest_Editorial_Annotation-Efficient_Deep_Learning_The_Holy_Grail_of_Medical_Imaging.pdf
- Interpretability-Guided-Inductive-Bias-For-Deep-Learnin_2022_Medical-Image-A.pdf
- Learning-image-representations-for-anomaly-detection--Applic_2024_Medical-Im.pdf
- Multi-source-multi-modal-markers-for-Bayesian-Networks--Ap_2024_Medical-Imag.pdf
- Quantitative-evaluation-of-Saliency-Based-Explainable-arti_2024_European-Jou.pdf
- Robust_Medical_Image_Classification_From_Noisy_Labeled_Data_With_Global_and_Local_Representation_Guided_Co-Training.pdf
- Semi-supervised-medical-image-classification-via-distance-c_2024_Medical-Ima.pdf
- Structure_and_Illumination_Constrained_GAN_for_Medical_Image_Enhancement.pdf
- Transforming-medical-imaging-with-Transformers--A-comparativ_2023_Medical-Im.pdf
- 医学图像分类 Medical Classification.pdf
- 医学报告生成IIHT Medical Report IIHT.pdf
- 可解释AI综述 XAI Survey.pdf
- 多层次可解释AI Multilevel XAI.pdf
- 密集挤压激励网络的多标签胸部X光片疾病分类.pdf
- 概念级XAI指标 Concept XAI.pdf
- 深度学习在医学影像中的应用综述.pdf

### A3_医学图像_配准_切片_张量_数学（3）

- A-prior-knowledge-guided-distributionally-robust-optimization_2024_Informati.pdf
- Correlated-and-individual-feature-learning-with-contrast-enha_2023_Pattern-R.pdf
- Robust-and-fast-stochastic-4D-flow-vector-field-signature-techn_2024_Medical.pdf

### B_注意力算子模块（134）

- (GRN)ConvNeXtV2.pdf
- (GSC)SegMamba.pdf
- (UIB)MobileNetV4.pdf
- ACF.pdf
- AFF.pdf
- AFPN.pdf
- ASSA&FRFN.pdf
- Attention.pdf
- CAA&PKIBlock.pdf
- CAFFN&MultiOrderGatedAggregation.pdf
- CAFM&MSFN&CAMixingBlock.pdf
- CBAM.pdf
- CBM.pdf
- CCT.pdf
- CGAFusion.pdf
- CLFT&UCDC.pdf
- CPA.pdf
- CPAM.pdf
- CPB.pdf
- CPB_visualisation.pdf
- CPCA.pdf
- CRMSA.pdf
- CSAttention.pdf
- CasDyFBlock&RMB&LFB.pdf
- CogM-Link.pdf
- CondConv.pdf
- DA.pdf
- DAB.pdf
- DA_Block.pdf
- DCA.pdf
- DICAM.pdf
- DLKA.pdf
- DOConv.pdf
- DSAM.pdf
- DWConv.pdf
- Dysample(上采样).pdf
- EFF.pdf
- EGA.pdf
- ELAB.pdf
- ENLTB.pdf
- FADConv.pdf
- FECAttention(时序预测).pdf
- FEM&SCAM.pdf
- FFA.pdf
- FMB.pdf
- FMM.pdf
- FMS&MDAF.pdf
- FSAS&DFFN.pdf
- FeatUp.pdf
- FreqFusion.pdf
- GAB&GHPA.pdf
- GAMED虚假新闻检测 GAMED Fake News.pdf
- GAU.pdf
- GCTattention.pdf
- GLSA.pdf
- GRSA.pdf
- GatedSlotAttention.pdf
- GhostModule.pdf
- GhostModuleV2.pdf
- GlobalPMFSBlock.pdf
- GraphLayer.pdf
- HAAM.pdf
- HFF.pdf
- HSE&FuGH&S3DSA.pdf
- HTB.pdf
- HWAB.pdf
- HWD下采样.pdf
- IDC.pdf
- Inception_mixer.pdf
- InfoNorm.pdf
- LAE&MSFM&RFAConv.pdf
- LDConv.pdf
- LMFLoss.pdf
- LMLT.pdf
- LPA&DMC.pdf
- MAB.pdf
- MASAG.pdf
- MATM&PS2A&MHIASA.pdf
- MDFM.pdf
- MFGM&PLM.pdf
- MLA.pdf
- MLAttention(文本分类).pdf
- MLLA.pdf
- MSAA.pdf
- MSAF.pdf
- MSCA.pdf
- MSCB&MSACM&EUCB&LGAG.pdf
- MSPLCK&EPA.pdf
- NAF.pdf
- OKM.pdf
- PAAblock.pdf
- PCBAM&SWA.pdf
- PConv.pdf
- PGM.pdf
- Parallel ViT.pdf
- PyConv.pdf
- RAB&HDRAB.pdf
- RAMiT&HRAMi.pdf
- RCM&dpg_head.pdf
- RFAConv.pdf
- RSSG.pdf
- SA.pdf
- SCKansformer.pdf
- SCSA.pdf
- SDM.pdf
- SFFusion.pdf
- SGFN&ASSA&ACSA.pdf
- SHSA.pdf
- SLAB(prepbn&SLA).pdf
- SMA&EMLP&Modulator.pdf
- SPConv.pdf
- ScaleGraphBlock.pdf
- StarBlocks.pdf
- SwiftFormerEncoder&ConvEncoder.pdf
- TIAM.pdf
- TIF.pdf
- TSConformerBlock.pdf
- TSLANet(ICB&ASB).pdf
- TVConv.pdf
- ULSAM.pdf
- WCMFandFACMA.pdf
- ar_residual_growth.pdf
- assemFormer&mcattn.pdf
- axial.pdf
- cleegn.pdf
- cross_attention.pdf
- dynamic_conv.pdf
- efficientViT3D.pdf
- ffc.pdf
- kan.pdf
- regionvit.pdf
- rsablock3d.pdf
- scSE.pdf
- wtconv2d.pdf

### C_目标检测_通用与旋转框（29）

- 2016_A_Survey_on_Object_D.pdf
- 2019_Object_detection_on.pdf
- 2020_DiResNet_Direction-.pdf
- 2022_Deep_object_detectio.pdf
- 2022_Object_Detection_in.pdf
- 2022_SODA_Site_Object_De.pdf
- 2023_Oriented_object_dete.pdf
- 2023_Super_Sparse_3D_Obje.pdf
- 2024_NBBOX_Noisy_Boundin.pdf
- 2024_PVAFN_Point-Voxel_A.pdf
- 2024_YOLOv5-Based_Object.pdf
- 2024_单帧红外图像多尺度小目标检测技术综述.pdf
- 2024_改进YOLOv7的交通标志识别模型.pdf
- 2025_Lightweight_Object_D.pdf
- 2025_Object_Detection_wit.pdf
- 2025_UAV-DETR_Efficient.pdf
- Mask_to_Height_YOLOv11_2510.27224.pdf
- PPA&DASI&MDCR(红外小目标检测).pdf
- cjig_图像识别_红外与可见光图像特征动态选择的目标检测网络.pdf
- cjig_目标检测_融合点云与图像的环境目标检测研究进展.pdf
- 一阶全卷积遥感图像倾斜目标检测.pdf
- 互补特征交互融合的RGB_D实时显著目标检测.pdf
- 光学遥感图像小目标检测深度学习算法综述.pdf
- 基于深度学习的有向目标检测研究进展_基于深度学习的有向目标检测研究进展.pdf
- 基于深度学习的视觉目标检测技术综述.pdf
- 增强小目标特征的航空遥感目标检测.pdf
- 无人机视角下的目标检测研究进展.pdf
- 适合跨域目标检测的雾霾图像增强.pdf
- 遥感影像小目标检测研究进展.pdf

### C2_目标检测_违建_车辆_船舶_行人（23）

- 2017_Building_Detection_f.pdf
- 2017_Fast_Vehicle_Detecti.pdf
- 2017_Real-Time_Illegal_Pa.pdf
- 2018_Mining_Illegal_Insid.pdf
- 2019_Anticipating_Illegal.pdf
- 2019_Building_Damage_Dete.pdf
- 2019_Building_change_dete.pdf
- 2019_The_Price_of_Free_Il.pdf
- 2020_Illegal_Border_Cross.pdf
- 2020_Predicting_Illegal_F.pdf
- 2021_Waste_detection_in_P.pdf
- 2022_Building_Height_Pred.pdf
- 2022_Detecting_A_Single_C.pdf
- 2022_Elastic_buildings_C.pdf
- 2022_Scrutinizing_Shipmen.pdf
- 2023_Building-road_Collab.pdf
- 2023_Detection_of_Illegal.pdf
- Illegal_Buildings_Detection_from_Satellite_Images_using_GoogLeNet_and_Cadastral_Map.pdf
- Liu2024_Illegal_Construction_Detection.pdf
- cjig_图像识别_多阶段空间感知道路损伤检测网络.pdf
- cjig_图像识别_融合密度和精细分数的行人检测.pdf
- cjig_图像识别_行人再识别技术研究进展.pdf
- 船舶匹配遥感 Ship Matching.pdf

### C3_目标检测_红外_可见光融合（1）

- 红外与可见光图像分组融合的视觉Transformer.pdf

### D_3D_点云_分类_分割_配准（28）

- 2025_2511.02142_3D_Growth_Trajectory_Reconstruction.pdf
- 2025_2511.18209_MotionDuet_3D_Motion_Generation.pdf
- 3DKMI Krawtchouk矩形状签名 3DKMI.pdf
- 3DfusionBlock.pdf
- 3D方向场变换 3D Orientation Field.pdf
- 3D树木分割图 3D Tree Segmentation.pdf
- 3D树木分割图割 3D Tree Graph Cut.pdf
- 3D树木描绘图割 3D Tree Delineation.pdf
- CornerPoint3D 3D检测新尺度 CornerPoint3D.pdf
- DFF(3d).pdf
- EPA3d.pdf
- MOGO 3D人体运动生成 MOGO Motion.pdf
- PE3d.pdf
- RobustPCA树木分类 Robust PCA Trees.pdf
- SLaT三阶段分割 SLaT Segmentation.pdf
- cjig_图像处理_深度学习点云质量增强方法综述.pdf
- cjig_点云_融合小样本元学习和原型对齐的点云分割算法.pdf
- cjig_计算机图形学_RGB-D图像多层特征提取算法综述.pdf
- cjig_计算机图形学_三维场景点云理解与重建技术.pdf
- pnp3d(点云).pdf
- 三维点云场景语义分割研究进展.pdf
- 多传感器树木制图 Multi-Sensor Trees.pdf
- 多功能传感器树木分类 Tree Species Classification.pdf
- 多特征融合与几何卷积的机载LiDAR点云地物分类.pdf
- 点云神经表示 Neural Varifolds.pdf
- 跨域LiDAR检测 Cross-Domain LiDAR.pdf
- 面向深度学习的三维点云补全算法综述.pdf
- 面向点云几何压缩的隐式编码网络.pdf

### D2_3D_重建_神经辐射场_SLAM（10）

- 2024_三维人脸成像及重建技术综述.pdf
- 2024_三维场景注视点渲染深度学习方法综述.pdf
- 2024_基于单目视觉惯性的同步定位与地图构建方法综述.pdf
- 2024_增量式尺度估计下的相机位置解算.pdf
- 2024_数字室内三维场景构建综述.pdf
- 2024_面向三维人体坐标及旋转角估计的注意力融合网络.pdf
- cjig_计算机图形学_三维重建场景纹理优化算法综述.pdf
- cjig_计算机图形学_几何属性引导的三维语义实例重建.pdf
- 基于神经辐射场和三维高斯泼溅的文本指导三维编辑综述.pdf
- 大规模室外图像3维重建技术研究进展.pdf

### E_图像复原_超分_去噪_去雨去雾（15）

- 2021_Image_Restoration_fo.pdf
- 2024_融合非局部特征表示的模糊图像复原.pdf
- DNCNet雷达去噪 DNCNet.pdf
- cjig_图像处理_轻量级注意力的束对齐网络的视频超分重建.pdf
- cjig_遥感_基于深度学习的光谱图像超分辨率综述.pdf
- 单幅图像去雨数据集和深度学习算法的联合评估与展望.pdf
- 图像去模糊研究综述.pdf
- 基于照度与场景纹理注意力图的低光图像增强.pdf
- 水下图像复原和增强方法研究进展.pdf
- 深度学习视频超分辨率技术综述.pdf
- 真实场景下图像超分辨技术现状与趋势.pdf
- 视觉模型及多模态大模型推进图像复原增强研究进展.pdf
- 面向图像复原的非因果选择性状态空间模型.pdf
- 面向透射文档图像复原的模糊扩散模型.pdf
- 高斯_维纳表示下的稠密焦栈图生成方法.pdf

### F_图像分割_语义_实例_全景（15）

- 2021_S2Looking_A_Satelli.pdf
- CenSegNet中心体 CenSegNet.pdf
- cjig_图像识别_弱监督语义分割方法综述.pdf
- cjig_图像识别_深度学习实时语义分割综述_完整版.pdf
- cjig_遥感_面向无人机海岸带生态系统监测的语义分割基准数据集.pdf
- 分割恢复联合模型 Segmentation Restoration.pdf
- 分割方法论总览 SaT Overview.pdf
- 变分分割基础Mumford-Shah与ROF Mumford-Shah ROF.pdf
- 多类ROF分割 Iterated ROF.pdf
- 注意力与方向特征增强的遥感图像语义分割.pdf
- 深度学习背景下的图像语义分割方法综述.pdf
- 球面小波分割 Wavelet Sphere.pdf
- 生物孔隙分割 Bio-Pores.pdf
- 语义比例分割 Semantic Proportions.pdf
- 跨层细节感知和分组注意力引导的遥感图像语义分割.pdf

### G_视觉基础模型_VLM_LLM（16）

- 2023_2307.00056_Proximal_Nested_Sampling.pdf
- 2023_OFAR_A_Multimodal_E.pdf
- 2023_Vision-Language_Mode.pdf
- 2024_Brain-Inspired_Onlin.pdf
- 2024_FreezeAsGuard_Mitig.pdf
- 2025_2508.08117_GRASPTrack_MultiObject_Tracking.pdf
- 2025_2510.09893_HIPPD_Brain-Inspired_Personality_Detection.pdf
- 2025_SAM2-ELNet_Label_En.pdf
- 2025_Vision-Language_Mode.pdf
- Scaling_Laws_for_Neural_Language_Models.pdf
- cjig_计算机视觉_分割一切模型SAM的潜力与展望.pdf
- 多模态大模型驱动的三维视觉理解技术前沿进展.pdf
- 大小模型端云协同进化技术进展.pdf
- 大模型高效微调CALM CALM Fine-tuning.pdf
- 视觉基础模型研究现状与发展趋势.pdf
- 高效PEFT微调 Less but Better PEFT.pdf

### I_场景文本_OCR（5）

- 2024_结合文本自训练和对抗学习的领域自适应工业场景文本检测.pdf
- 2024_融合场景先验的船名文本检测方法.pdf
- cjig_图像处理_深度伪造及其取证技术综述.pdf
- 大模型时代的光学文字识别_现状及展望.pdf
- 结合提示学习和视觉语义生成融合的东巴画图像描述.pdf

### J_人脸_表情_伪造_情感（7）

- 2024_人脸深度伪造检测方法综述.pdf
- 2024_自适应光流估计驱动的微表情识别.pdf
- 可见表面检测 Detect Closer Surfaces.pdf
- 情感感知人格检测 EmoPerso Emotion-Aware.pdf
- 情感计算与理解研究发展概述.pdf
- 注意力引导局部特征联合学习的人脸表情识别.pdf
- 融合ViT与对比学习的面部表情识别.pdf

### K_跟踪_视频_动作（4）

- TransNet动作识别 TransNet HAR.pdf
- cjig_图像处理_结合背景图的高分辨率视频人像实时抠图网络.pdf
- 单目标跟踪中的视觉智能评估技术综述.pdf
- 扩散模型生成视频数据集及其检测基准研究.pdf

### L_数据集_Benchmark（8）

- 2020_Aerial_Imagery_Pixel.pdf
- 2020_RSVQA_Visual_Questi.pdf
- 2020_TJU-DHD_A_Diverse_H.pdf
- 2024_Change-Agent_Toward.pdf
- 2024_MagicBathyNet_A_Mul.pdf
- 2025_Benchmarking_Suite_f.pdf
- 2025_SoccerSynth-Detectio.pdf
- cjig_计算机视觉_车路两端纯视觉鸟瞰图感知研究综述.pdf

### M_行人_重识别_检索（3）

- 2025_Remote_Sensing_Retri.pdf
- 深度学习的跨视角地理定位方法综述.pdf
- 预训练大模型技术在行人重识别的应用综述.pdf

### N_雷达_无线电_张量_数学（22）

- 2019_Thylakoid_Electron_Tomography.pdf
- 2023_2307.12248_Bilevel_Peer_Review.pdf
- 2023_2308.01480_Tensor_Train_Approximation.pdf
- 2023_2311.14733_Equalizing_Protected_Attributes.pdf
- ISAR卫星特征识别 ISAR.pdf
- PURIFY分布式优化 PURIFY.pdf
- Talk2Radar 雷达语言多模态 Talk2Radar.pdf
- Tucker近似 Tucker Approximation.pdf
- 分布式无线电优化 Distributed Radio Optimization.pdf
- 双面Sketching张量 Two-Sided Sketching.pdf
- 叶绿体电子断层扫描 Thylakoid.pdf
- 在线无线电干涉成像 Online Radio Imaging.pdf
- 张量CUR分解LoRA tCURLoRA.pdf
- 无线电干涉不确定性I Radio Interferometric I.pdf
- 无线电干涉不确定性II Radio Interferometric II.pdf
- 稀疏贝叶斯质量映射I Sparse Bayesian I.pdf
- 稀疏贝叶斯质量映射II Sparse Bayesian II.pdf
- 稀疏贝叶斯质量映射III Sparse Bayesian III.pdf
- 蛋白质结构网络图LL4G LL4G Graph.pdf
- 雷达工作模式识别 Radar Work Mode.pdf
- 高效变分分类 Efficient Variational.pdf
- 高维逆问题不确定性量化 Uncertainty Quantification.pdf

### O_物理对抗_安全_鲁棒（2）

- 2021_Physical_Adversarial.pdf
- 针对视觉深度学习模型的物理对抗攻击研究综述.pdf

### P_跨域_域自适应_联邦（2）

- cjig_图像识别_自适应异构联邦学习.pdf
- 跨域遥感场景解译研究进展.pdf

### Q_自监督_对比学习_主动学习（5）

- 2021_A_Survey_of_Self-Sup.pdf
- 2021_Active_learning_for.pdf
- 2022_Reinforcement-based.pdf
- 2022_Self-supervised_Lear.pdf
- 2024_Reinforcement_Learni.pdf

### R_综述_Survey（19）

- 2017_A_Comprehensive_Surv.pdf
- 2020_A_Comparison_of_Deep.pdf
- 2024_基于物理的可微渲染综述.pdf
- 2024_轻量化视觉定位技术综述.pdf
- 2024_面向增强现实的虚实遮挡技术综述.pdf
- cjig_图像识别_高质量超声成像与重建研究综述.pdf
- cjig_计算机视觉_无人集群系统协同决策与博弈控制综述.pdf
- cjig_计算机视觉_沉浸式环境和多场景中的视觉提示信息综述.pdf
- cjig_遥感_多模态遥感图像配准方法研究综述.pdf
- cjig_遥感_小样本SAR图像分类方法综述.pdf
- 人工智能在文物行业的应用与展望.pdf
- 图像重定向质量评价的研究进展.pdf
- 基于深度学习的图像融合方法综述.pdf
- 室内场景拟人交互研究进展.pdf
- 数据增强综述 Data Augmentation.pdf
- 无参考图像质量评价研究进展.pdf
- 深度学习单目深度估计研究进展.pdf
- 深度学习架构综述 CNNs RNNs Transformers.pdf
- 高光谱图像智能分类研究综述与展望.pdf

### S_变化检测_ChangeDetection（7）

- 2019_Change_Detection_and.pdf
- 2019_Object_Contour_and_E.pdf
- 2019_Semantic_Change_and.pdf
- 2020_A_computer-friendly.pdf
- 2023_An_Aligned_Multi-Tem.pdf
- 2023_Laplacian_Change_Poi.pdf
- cjig_遥感_高分遥感影像变化检测.pdf

### R1_遥感_高光谱_变化检测（4）

- 2017_Deep_learning_in_rem.pdf
- 2020_Detecting_the_Presen.pdf
- Deep-learning-based-hyperspectral-image-correction-and-unmixing-f_2024_iScie.pdf
- cjig_遥感_热红外高光谱遥感影像信息提取.pdf

### R2_控制_生物启发_其他跨学科（9）

- Biologically-Inspired_Iterative_Learning_Control_Design_A_Modular-Based_Approach.pdf
- EPAS_v5_中文终稿.pdf
- FINAL_VERSION.pdf
- RevIN(时序预测).pdf
- SmoothNet.pdf
- cjig_图像处理_基于t-SNE最大化的彩色图像灰度化.pdf
- 两阶段分类 Two-Stage.pdf
- 生物启发迭代学习控制 ILC.pdf
- 非负子空间小样本学习 Non-negative Subspace.pdf

### T_通用_NLP_其他（66）

- 1-s2.0-S0950705124009833-main.pdf
- 2005_Active_Amplification.pdf
- 2009_Embedded_Sensor_Syst.pdf
- 2010_A_Comparative_Study.pdf
- 2010_Detecting_Botnets_Th.pdf
- 2010_Implications_of_the.pdf
- 2013_Byzantine_Fault_Tole.pdf
- 2013_Quickest_Change_Poin.pdf
- 2014_Semantic-based_Detec.pdf
- 2014_Sequential_Detection.pdf
- 2015_Automatic_Channel_Ne.pdf
- 2015_Precipitation_extrem.pdf
- 2018_Application_of_a_sem.pdf
- 2018_Automatic_Pixelwise.pdf
- 2018_Deep_Learning_Approa.pdf
- 2018_Deep_learning_based.pdf
- 2018_Envision_of_an_integ.pdf
- 2019_Aggregated_Deep_Loca.pdf
- 2019_Efficient_ConvNet-ba.pdf
- 2019_Introduction_to_Voic.pdf
- 2019_R$^2$-CNN_Fast_Tiny.pdf
- 2019_Spectrum_Prediction.pdf
- 2019_The_Language_of_Lega.pdf
- 2020_Attention_Neural_Net.pdf
- 2020_Deep_Learning_for_Re.pdf
- 2020_Future_Climate_Chang.pdf
- 2020_Object_sieving_and_m.pdf
- 2021_An_Attention-Fused_N.pdf
- 2021_CFC-Net_A_Critical.pdf
- 2021_Exploring_Depth_Cont.pdf
- 2021_MPSN_Motion-aware_P.pdf
- 2021_Uncovering_the_Size.pdf
- 2021_What_Makes_Sound_Eve.pdf
- 2022_Algorithm_for_detect.pdf
- 2022_Improved_normal-boun.pdf
- 2022_Interpretability_in.pdf
- 2022_Recognising_the_impo.pdf
- 2023_A_Multi-scale_Genera.pdf
- 2023_A_Novel_Multi-scale.pdf
- 2023_Learning_Efficient_U.pdf
- 2023_Limpets_Computer_Vision_Frontiers.pdf
- 2024_A_Progressive_Image.pdf
- 2024_Call_to_Protect_the.pdf
- 2024_Correlation_of_Objec.pdf
- 2024_Extracting_Object_He.pdf
- 2024_Improving_the_Detect.pdf
- 2024_Physics-Informed_Rea.pdf
- 2024_Remote_Sensing_ChatG.pdf
- 2024_Remote_Sensing_Spati.pdf
- 2024_SOAR_Advancements_i.pdf
- 2024_布料与刚体模型间的空间网格碰撞检测方法.pdf
- 2024_超声波空中触觉图形呈现的时空调制方法.pdf
- 2025_Are_Open-Vocabulary.pdf
- 2025_Audit_of_takedown_de.pdf
- 2025_Cross-View_Open-Voca.pdf
- 2025_EdgeAI_Drone_for_Aut.pdf
- 2025_Genes_Shells_AI_Scientific_Reports.pdf
- 2026_Towards_Remote_Sensi.pdf
- cjig_paper_1.pdf
- cjig_paper_2.pdf
- cjig_paper_3.pdf
- cjig_paper_5.pdf
- 平衡神经网络搜索I Balanced NAS I.pdf
- 平衡神经网络搜索II Balanced NAS II.pdf
- 绿色AI的隐私保护与能量高效的分布式传感网络同步研究.pdf
- 自然历史馆藏错误标本能计算机视觉方法 Mislabelled Specimens.pdf
