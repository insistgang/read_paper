#!/usr/bin/env python3
"""将论文按主题归类，输出 markdown 清单。

用法:
    python3 scripts/classify_papers.py                  # 默认扫 01-Papers/
    python3 scripts/classify_papers.py /path/to/papers  # 扫指定目录
    python3 scripts/classify_papers.py --out custom.md  # 自定义输出

退出码:
    0  正常
    1  目录不存在
    2  没有 PDF
"""
import argparse
import json
import re
import sys
from pathlib import Path

# 默认: 仓库根下的 01-Papers/, 跟 obsidian 论文库约定一致
DEFAULT_PDF_DIR = Path(__file__).resolve().parent.parent / "01-Papers"
DEFAULT_OUT = DEFAULT_PDF_DIR / "paper_classification.md"

# 主题定义：(主题名, 关键词列表, 优先级 1=高)
# 顺序就是优先级——前面优先匹配
TOPICS = [
    # ============== 工具/杂项/综述图 ==============
    ("Z_工具与杂项_figures", [
        r"^Cover_Letter\.pdf$",
        r"^Author_Biography\.pdf$",
        r"^figure1\.pdf$",
        r"^illustration_v2\.pdf$",
        r"^controlled_ablation\.pdf$",
        r"^benchmark_overview\.pdf$",
        r"^scalability_overview\.pdf$",
        r"^tradeoff_curve\.pdf$",
        r"^parameter_sensitivity_scan\.pdf$",
        r"^supplemental_parameter_scans\.pdf$",
        r"^trigger_rate_validation\.pdf$",
        r"^budget_fairness_accounting\.pdf$",
        r"^results-question-type-radar\.pdf$",
        r"^dataset-imgs-QAs\.pdf$",
        r"^dataset\.pdf$",
        r"^dataset_analysis",
        r"^final_check\.json$",  # 安全网
        r"^remote_check\.json$",
        r"^remote_status",
    ]),

    # ============== 医学图像 ==============
    ("A1_医学图像_分割", [
        r"Medical[-_ ]Image[-_ ][Aa]nal", r"医学图像分割", r"病理图像分割",
        r"Content-Noise.*Medical", r"Contrastive.*Medical",
        r"Dual_Adversarial.*Medical", r"Few-Shot_Medical_Image_Segmentation",
        r"LViT", r"LightM-UNet", r"CMUNeXt", r"CoNIC",
        r"HiFi-Mamba", r"Rethinking-masked-image-modelling.*medical",
        r"肝", r"直肠", r"血管分割", r"Framelet",
    ]),
    ("A1b_医学图像_小样本_综述", [
        r"医学图像小样本学习", r"医学图像分类 Medical_Classification",
    ]),
    ("A2_医学图像_分类_配准_生成", [
        r"medical.*classification", r"Medical[-_ ][Cc]lassification",
        r"医学图像分类", r"胸部X光", r"医疗.*分类",
        r"medical.*registration", r"医学报告生成", r"Medical_Report",
        r"Deep-learning-based-synthesis-of-MRI", r"Diffusion_Brain_MRI",
        r"Robust_Medical_Image_Classification", r"Semi-supervised-medical",
        r"Beam-wise-dose", r"ischemic-stroke",
        r"Assessing_the_Ability_of_Generative.*Medical",
        r"Structure_and_Illumination.*Medical",
        r"A_Collaborative_Self-Supervised.*Medical_Image_Enhancement",
        r"Anonymizing-medical", r"Multi-source-multi-modal-markers.*Medical",
        r"Interpretability-Guided.*Medical", r"Explainable-artificial.*Medical",
        r"Learning-image-representations.*Medical", r"Quantitative-evaluation.*Saliency",
        r"XAI", r"Guest_Editorial_Annotation-Efficient",
        r"医学影像中的应用综述", r"医学图像.*综述",
        r"A-comprehensive-survey-on-deep-active-learning",
        r"A-survey-on-deep-learning-in-medical-image-registration",
        r"Transforming-medical-imaging",
    ]),
    ("A3_医学图像_配准_切片_张量_数学", [
        r"Robust-and-fast-stochastic-4D-flow",
        r"A-prior-knowledge-guided-distributionally",
        r"Correlated-and-individual-feature",
    ]),

    # ============== 注意力 / 算子 / 模块 ==============
    ("B_注意力算子模块", [
        r"^CBAM\.pdf$", r"^ACF\.pdf$", r"^AFF\.pdf$", r"^AFPN\.pdf$",
        r"^ASSA&FRFN\.pdf$", r"^CAA&PKIBlock\.pdf$", r"^CAFFN&MultiOrderGatedAggregation\.pdf$",
        r"^CAFM&MSFN&CAMixingBlock\.pdf$", r"^CBM\.pdf$", r"^CCT\.pdf$",
        r"^CGAFusion\.pdf$", r"^CLFT&UCDC\.pdf$", r"^CPA\.pdf$", r"^CPAM\.pdf$",
        r"^CPB(?:_visualisation)?\.pdf$", r"^CPCA\.pdf$", r"^CRMSA\.pdf$",
        r"^CSAttention\.pdf$", r"^CasDyFBlock&RMB&LFB\.pdf$", r"^CogM-Link\.pdf$",
        r"^CondConv\.pdf$", r"^DA\.pdf$", r"^DAB\.pdf$", r"^DA_Block\.pdf$",
        r"^DCA\.pdf$", r"^DICAM\.pdf$", r"^DLKA\.pdf$", r"^DOConv\.pdf$",
        r"^DSAM\.pdf$", r"^DWConv\.pdf$", r"^Dysample", r"^EFF\.pdf$",
        r"^EGA\.pdf$", r"^ELAB\.pdf$", r"^ENLTB\.pdf$", r"^FADConv\.pdf$",
        r"^FECAttention", r"^FEM&SCAM\.pdf$", r"^FFA\.pdf$", r"^FMB\.pdf$",
        r"^FMM\.pdf$", r"^FMS&MDAF\.pdf$", r"^FSAS&DFFN\.pdf$", r"^FeatUp\.pdf$",
        r"^FreqFusion\.pdf$", r"^GAB&GHPA\.pdf$", r"^GAMED", r"^GAU\.pdf$",
        r"^GCTattention\.pdf$", r"^GLSA\.pdf$", r"^GRSA\.pdf$",
        r"^GatedSlotAttention\.pdf$", r"^GhostModule", r"^GlobalPMFSBlock\.pdf$",
        r"^GraphLayer\.pdf$", r"^HAAM\.pdf$", r"^HFF\.pdf$",
        r"^HSE&FuGH&S3DSA\.pdf$", r"^HTB\.pdf$", r"^HWAB\.pdf$",
        r"^HWD下采样\.pdf$", r"^IDC\.pdf$", r"^Inception_mixer\.pdf$",
        r"^InfoNorm\.pdf$", r"^LAE&MSFM&RFAConv\.pdf$", r"^LDConv\.pdf$",
        r"^LMFLoss\.pdf$", r"^LMLT\.pdf$", r"^LPA&DMC\.pdf$", r"^LocalViT\.pdf$",
        r"^MAB\.pdf$", r"^MASAG\.pdf$", r"^MATM&PS2A&MHIASA\.pdf$", r"^MDFM\.pdf$",
        r"^MFGM&PLM\.pdf$", r"^MLA\.pdf$", r"^MLAttention", r"^MLLA\.pdf$",
        r"^MSAA\.pdf$", r"^MSAF\.pdf$", r"^MSCA\.pdf$",
        r"^MSCB&MSACM&EUCB&LGAG\.pdf$", r"^MSPLCK&EPA\.pdf$", r"^NAF\.pdf$",
        r"^OKM\.pdf$", r"^PAAblock\.pdf$", r"^PCBAM&SWA\.pdf$", r"^PConv\.pdf$",
        r"^PGM\.pdf$",         r"^Parallel ViT\.pdf$", r"^PyConv\.pdf$",
        r"^Attention\.pdf$", r"^ar_residual_growth\.pdf$",
        r"^RAB&HDRAB\.pdf$", r"^RAMiT&HRAMi\.pdf$", r"^RCM&dpg_head\.pdf$",
        r"^RFAConv\.pdf$", r"^RSSG\.pdf$", r"^SA\.pdf$", r"^SCKansformer\.pdf$",
        r"^SCSA\.pdf$", r"^SDM\.pdf$", r"^SFFusion\.pdf$",
        r"^SGFN&ASSA&ACSA\.pdf$", r"^SHSA\.pdf$", r"^SLAB", r"^SMA&EMLP&Modulator\.pdf$",
        r"^SPConv\.pdf$", r"^ScaleGraphBlock\.pdf$", r"^StarBlocks\.pdf$",
        r"^SwiftFormer", r"^TIAM\.pdf$", r"^TIF\.pdf$", r"^TSConformerBlock\.pdf$",
        r"^TSLANet", r"^TVConv\.pdf$", r"^ULSAM\.pdf$", r"^WCMFandFACMA\.pdf$",
        r"^axial\.pdf$", r"^cleegn\.pdf$", r"^cross_attention\.pdf$",
        r"^dynamic_conv\.pdf$", r"^efficientViT3D\.pdf$", r"^ffc\.pdf$",
        r"^kan\.pdf$", r"^regionvit\.pdf$", r"^rsablock3d\.pdf$", r"^scSE\.pdf$",
        r"^wtconv2d\.pdf$", r"^assembledFormer&mcattn\.pdf$",  # 注：实际是 assemFormer
        r"^assembledFormer", r"^assemFormer", r"^MobilenetV4", r"^MobileNetV4",
        r"\(GRN\)ConvNeXtV2", r"\(GSC\)SegMamba", r"\(UIB\)MobileNetV4",
        r"^ConvNeXtV2", r"^SegMamba",
    ]),

    # ============== 目标检测 ==============
    ("C_目标检测_通用与旋转框", [
        r"[Oo]bject_[Dd]etection", r"[Oo]bject detection",
        r"目标检测", r"UAV-DETR", r"Lightweight_Object_D",
        r"YOLOv", r"GRN", r"NBBOX", r"SODA", r"PVAFN",
        r"Mask_to_Height", r"Object_Detection_wit",
        r"基于深度学习的有向目标检测", r"基于深度学习的视觉目标检测",
        r"光学遥感图像小目标检测", r"遥感影像小目标检测",
        r"无人机视角下的目标检测", r"增强小目标特征的航空遥感目标检测",
        r"一阶全卷积遥感图像倾斜", r"Oriented_object_dete",
        r"^2016_A_Survey_on_Object_D",
        r"Super_Sparse_3D_Obje",  # 3D 稀疏目标检测
        r"^2022_Deep_object_detectio",
        r"DiResNet",
    ]),
    ("C2_目标检测_违建_车辆_船舶_行人", [
        r"Illegal", r"违建", r"illegal", r"[Bb]uilding[_ ][Dd]etection",
        r"[Vv]ehicle", r"[Ss]hip", r"船舶",
        r"Illegal_Border", r"Illegal_Buildings", r"Liu2024_Illegal",
        r"Anticipating_Illegal", r"Predicting_Illegal",
        r"Detecting_the_Presen.*Illegal", r"Detection_of_Illegal",
        r"Mining_Illegal", r"The_Price_of_Free_Il",
        r"Real-Time_Illegal_Pa", r"Building_Damage",
        r"Building_change_dete", r"Building-road_Collab",
        r"2017_Building_Detection", r"2017_Fast_Vehicle_Detecti",
        r"2019_Building_Damage_Dete", r"2019_Building_change_dete",
        r"2022_Building_Height", r"2022_Detecting_A_Single_C",
        r"2022_Elastic_buildings", r"2022_Scrutinizing_Shipmen",
        r"2021_Waste_detection", r"船舶匹配", r"Ship_Matching",
        r"行人检测", r"行人再识别", r"Person_Re",
        r"cjig_目标检测_融合点云与图像",
        r"cjig_图像识别_融合密度和精细分数的行人",
        r"cjig_图像识别_多阶段空间感知道路损伤",
    ]),
    ("C3_目标检测_红外_可见光融合", [
        r"PPA&DASI&MDCR", r"红外小目标", r"单帧红外",
        r"红外与可见光图像", r"cjig_图像识别_红外与可见光图像特征",
        r"适合跨域目标检测的雾霾",
    ]),
    ("C4_目标检测_交通_标志_检测器", [
        r"交通标志", r"改进YOLOv7", r"FAST_R_CNN",
    ]),

    # ============== 3D / 点云 / 重建 / SLAM ==============
    ("D_3D_点云_分类_分割_配准", [
        r"3D", r"点云", r"LiDAR", r"PnP3D", r"CornerPoint3D", r"3DKMI",
        r"RobustPCA树木", r"3D树木", r"3D 树木", r"Tree",
        r"c[sCc]lamps", r"EPA3d", r"PE3d", r"rsablock3d",
        r"^\(3d\)", r"^DFF\(3d\)",
        r"3DfusionBlock", r"3D方向场", r"SLaT三阶段",
        r"三维点云场景", r"cjig_点云", r"cjig_计算机图形学_RGB-D",
        r"cjig_计算机图形学_三维场景", r"面向深度学习的三维点云补全",
        r"面向点云几何压缩", r"多特征融合与几何卷积",
        r"Multi-Sensor_Trees", r"Tree_Species_Classification",
        r"多传感器树木制图", r"多功能传感器树木分类",
    ]),
    ("D2_3D_重建_神经辐射场_SLAM", [
        r"3D重建", r"神经辐射场", r"三维高斯泼溅",
        r"NeRF", r"3D_Gaussian", r"神经表示",
        r"3D 重建", r"三维重建", r"基于单目视觉惯性.*SLAM",
        r"同步定位与地图构建", r"增量式尺度估计",
        r"数字室内三维场景", r"三维人脸",
        r"3D Growth", r"3D Motion", r"MOGO",
        r"MotionDuet", r"面向三维人体坐标",
        r"大规模室外图像3维", r"cjig_计算机图形学_三维重建场景",
        r"cjig_计算机图形学_几何属性引导",
        r"点云神经表示", r"三维场景注视点渲染",
    ]),

    # ============== 图像复原 ==============
    ("E_图像复原_超分_去噪_去雨去雾", [
        r"超分辨", r"超分辨率", r"[Ss]uper[-_ ][Rr]esolution",
        r"去雨", r"去模糊", r"去噪", r"[Dd]enoising",
        r"低光", r"[Ll]ow[-_ ][Ll]ight", r"低照度", r"照度",
        r"水下", r"[Uu]nderwater", r"图像复原", r"图像恢复",
        r"[Ii]mage [Rr]estoration", r"[Ii]mage [Rr]ecovery",
        r"面向图像复原", r"视觉模型.*图像复原",
        r"融合非局部特征.*模糊", r"面向透射文档图像",
        r"基于照度与场景纹理", r"高斯_维纳.*焦栈",
        r"cjig_图像处理_轻量级注意力的束对齐",
        r"cjig_遥感_基于深度学习的光谱图像超分辨率",
        r"^2021_Image_Restoration",
    ]),

    # ============== 图像分割 ==============
    ("F_图像分割_语义_实例_全景", [
        r"语义分割", r"[Ss]emantic [Ss]egmentation",
        r"实例分割", r"[Ii]nstanc", r"[Pp]anoptic",
        r"SLaT", r"SaT", r"变分分割", r"Mumford-Shah",
        r"ROF", r"[Ss]egmentation", r"分割方法论",
        r"分割恢复联合", r"球面小波分割", r"Wavelet Sphere",
        r"语义比例分割", r"Semantic_Proportions",
        r"CenSegNet", r"3DKMI", r"生物孔隙", r"Bio-Pores",
        r"Weakly.*[Ss]egment", r"弱监督语义",
        r"cjig_图像识别_弱监督语义分割",
        r"cjig_图像识别_深度学习实时语义分割",
        r"跨层细节感知.*遥感图像语义", r"注意力与方向特征.*遥感图像语义",
        r"深度学习背景下的图像语义分割",
    ]),

    # ============== 视觉基础模型 / 大模型 ==============
    ("G_视觉基础模型_VLM_LLM", [
        r"SAM", r"[Ss]egment [Aa]nything",
        r"Vision-Language", r"视觉语言", r"多模态大模型",
        r"[Bb]rain-[Ii]nspired", r"HIPPD", r"FreezeAsGuard",
        r"PEFT", r"CALM", r"Less but Better",
        r"Scaling_Laws", r"GPT", r"ChatGPT",
        r"大小模型端云", r"视觉基础模型", r"大模型高效微调",
        r"cjig_计算机视觉_分割一切模型",
        r"OFAR", r"OFA",  # OFA 多模态
        r"GRASPTrack",  # 多目标跟踪+基础模型
    ]),

    # ============== 显著性 / 小目标检测 ==============
    ("H_显著性_小目标", [
        r"[Ss]alien", r"显著", r"[Ss]mall [Oo]bject",
        r"小目标", r"细小目标", r"RGB.*显著",
        r"互补特征交互融合.*RGB_D", r"RGB_D实时显著",
    ]),

    # ============== 场景文本 / OCR ==============
    ("I_场景文本_OCR", [
        r"船名", r"文本检测", r"文本识别", r"光学文字识别",
        r"OCR", r"工业场景文本", r"东巴画",
        r"cjig_图像处理_深度伪造",  # 与伪造相关
    ]),

    # ============== 人脸 / 表情 / 伪造 ==============
    ("J_人脸_表情_伪造_情感", [
        r"人脸", r"[Ff]ace", r"[Ff]acial",
        r"深度伪造", r"伪造", r"[Ff]ake", r"[Dd]eepfake",
        r"表情", r"情感", r"[Ee]motion", r"[Ee]moPerso",
        r"情感感知", r"情感计算", r"微表情",
        r"融合ViT与对比学习.*面部表情",
        r"注意力引导局部特征.*人脸表情",
        r"人脸深度伪造检测",
        r"cjig_图像处理_深度伪造及其取证",
    ]),

    # ============== 跟踪 / 视频 / 动作 ==============
    ("K_跟踪_视频_动作", [
        r"[Tt]racking", r"跟踪", r"GRASPTrack",
        r"动作识别", r"[Aa]ction [Rr]ecognition", r"TransNet",
        r"视频超分", r"视频超分辨", r"video super",
        r"扩散模型生成视频", r"视频描述", r"高分辨率视频人像",
        r"单目标跟踪", r"cjig_图像处理_结合背景图的高分辨率",
    ]),

    # ============== 数据 / 数据集 / Benchmark ==============
    ("L_数据集_Benchmark", [
        r"[Bb]enchmark", r"[Dd]ataset", r"RSVQA",
        r"S2Looking", r"MagicBathyNet", r"TJU-DHD",
        r"Aerial_Imagery_Pixel", r"CoNIC",
        r"面向无人机海岸带", r"Change-Agent",
        r"cjig_遥感_面向无人机",
        r"cjig_计算机视觉_车路两端",
        r"SoccerSynth",
    ]),

    # ============== 行人 / 重识别 ==============
    ("M_行人_重识别_检索", [
        r"行人再识别", r"[Pp]erson [Rr]e",
        r"重识别", r"跨视角", r"跨域地理定位",
        r"Remote_Sensing_Retri", r"Retri",
        r"预训练大模型.*行人重识别",
    ]),

    # ============== 雷达 / 无线电 / 张量 / 数学 ==============
    ("N_雷达_无线电_张量_数学", [
        r"雷达", r"ISAR", r"Talk2Radar", r"DNCNet雷达",
        r"[Rr]adio", r"无线电",
        r"[Tt]ensor", r"张量", r"Sketching",
        r"高维逆问题", r"稀疏贝叶斯", r"[Ss]parse [Bb]ayesian",
        r"变分", r"[Vv]ariational", r"高斯_维纳",
        r"叶绿体电子断层", r"Thylakoid",
        r"蛋白质结构", r"LL4G",
        r"Beamed.*[Tt]ensor", r"分布式无线电",
        r"在线无线电干涉", r"Radio_Interferometric",
        r"面向图像复原的非因果",  # 状态空间模型
        r"2308.01480_Tensor", r"Tucker", r"Tensor_Train",
        r"PURIFY", r"UAT",  # 优化/张量
        r"Concept XAI", r"高效变分分类",  # 概念 XAI
        r"2307.00056_Proximal", r"2307.12248_Bilevel",  # 数学方法
        r"Equalizing_Protected", r"2311.14733",
    ]),

    # ============== 物理对抗 / 安全 / 鲁棒性 ==============
    ("O_物理对抗_安全_鲁棒", [
        r"[Pp]hysical [Aa]dversarial", r"物理对抗",
        r"针对视觉深度学习模型", r"[Bb]ackdoor",
        r"FreezeAsGuard", r"安全",
        r"Noise.*[Ll]abel", r"噪声标签",
        r"Robust_Medical",
        r"^2021_Physical_Adversarial",
    ]),

    # ============== 跨域 / 域自适应 ==============
    ("P_跨域_域自适应_联邦", [
        r"[Cc]ross[-_ ][Dd]omain", r"跨域", r"Domain_Adaptation",
        r"Domain[-_ ]Adaptive", r"跨层细节感知",
        r"Federated", r"联邦学习", r"异构联邦",
        r"cjig_图像识别_自适应异构联邦",
    ]),

    # ============== 自监督 / 对比学习 ==============
    ("Q_自监督_对比学习_主动学习", [
        r"[Ss]elf[-_ ][Ss]upervised", r"自监督",
        r"[Cc]ontrastive", r"对比学习",
        r"Active_Learning", r"主动学习",
        r"RL_", r"Reinforcement",
        r"2021_A_Survey_of_Self-Sup",
    ]),

    # ============== 综述 / Survey ==============
    ("R_综述_Survey", [
        r"^[12][09]{2}[0-9]_.+[Ss]urvey", r"^[12][09]{2}[09]_.+[Ss]urvey",
        r"[Aa]_Survey", r"[Ss]urvey",
        r"^[12][09]{2}_2017_A_Comprehensive",
        r"综述", r"研究进展", r"研究现状与发展",
        r"前沿进展", r"应用与展望",
        r"3D人脸成像", r"轻量化视觉定位", r"面向增强现实",
        r"Vision-Language_Mode",  # VLM 综述
        r"^2017_A_Comprehensive_Surv",
        r"^2020_A_Comparison_of_Deep",
    ]),

    # ============== 变化检测 ==============
    ("S_变化检测_ChangeDetection", [
        r"[Cc]hange[-_ ][Dd]etection", r"变化检测",
        r"Change-Agent", r"Laplacian_Change",
        r"Semantic_Change", r"Object_Contour",
        r"2020_A_computer-friendly", r"An_Aligned_Multi-Tem",
    ]),

    # ============== 知识/常识/通用NLP ==============
    ("R1_遥感_高光谱_变化检测", [
        r"Deep-learning-based-hyperspectral", r"高光谱图像智能",
        r"cjig_遥感_热红外高光谱", r"热红外高光谱",
        r"^2017_Deep_learning_in_rem",
        r"^2020_Detecting_the_Presen",
    ]),

    ("R2_控制_生物启发_其他跨学科", [
        r"Biologically-Inspired_Iterative", r"生物启发迭代学习控制",
        r"两阶段分类", r"非负子空间小样本学习",
        r"EPAS_v5_中文终稿", r"FINAL_VERSION",
        r"SmoothNet", r"RevIN",
        r"cjig_图像处理_基于t-SNE最大化",
    ]),

    ("T_通用_NLP_其他", [
        r"^[23]010_Efficient_ConvNet",
        r"^2019_Efficient_ConvNet",
        r"^2019_Introduction_to_Voic",
        r"^2010_A_Comparative_Study",
        r"^2010_Detecting_Botnets",
        r"^2010_Implications",
        r"^2013_Byzantine",
        r"^2013_Quickest_Change",
        r"^2014_Semantic-based_Detec",
        r"^2014_Sequential",
        r"^2015_Automatic_Channel",
        r"^2015_Precipitation",
        r"^2018_Application_of_a_sem",
        r"^2018_Automatic_Pixelwise",
        r"^2018_Deep_Learning_Approa",
        r"^2018_Deep_learning_based",
        r"^2018_Envision",
        r"^2018_Mining_Illegal",
        r"^2019_Aggregated_Deep_Loca",
        r"^2019_R\$.*-CNN",
        r"^2019_Spectrum_Prediction",
        r"^2019_The_Language_of_Lega",
        r"^2019_Thylakoid",
        r"^2020_Aerial_Imagery",
        r"^2020_Attention_Neural",
        r"^2020_Deep_Learning_for_Re",
        r"^2020_Future_Climate",
        r"^2020_Object_sieving",
        r"^2021_Active_learning",
        r"^2021_An_Attention-Fused",
        r"^2021_CFC-Net",
        r"^2021_Exploring_Depth",
        r"^2021_MPSN",
        r"^2021_Uncovering",
        r"^2021_What_Makes_Sound",
        r"^2022_Algorithm_for_detect",
        r"^2022_Improved_normal",
        r"^2022_Interpretability",
        r"^2022_Object_Detection",
        r"^2022_Recognising",
        r"^2022_Reinforcement",
        r"^2022_Self-supervised",
        r"^2022_SODA",
        r"^2024_Extracting_Object_He",
        r"^2024_Remote_Sensing_ChatG",
        r"^2024_Remote_Sensing_Spati",
        r"^2024_SOAR",
        r"^2024_Physics-Informed",
        r"^2024_Reinforcement_Learni",
        r"^2025_2508.08117",
        r"^2025_2510.09893",
        r"^2025_2511.02142",
        r"^2025_2511.18209",
        r"^2025_Are_Open-Vocabulary",
        r"^2025_Audit_of_takedown",
        r"^2025_Cross-View",
        r"^2025_EdgeAI_Drone",
        r"^2025_Genes_Shells",
        r"^2025_Object_Detection",
        r"^2025_Brain",
        r"^2024_Brain-Inspired",
        r"^2024_Call_to_Protect",
        r"^2024_Correlation",
        r"^2024_Improving",
        r"^2024_YOLOv5",
        r"^2024_A_Progressive",
        r"^2024_2405.04974",
        r"^2025_SAM2-ELNet",
        r"^2026_Towards",
        r"^2023_2311.14733",
        r"^2023_2307.00056",
        r"^2023_2307.12248",
        r"^2023_2308.01480",
        r"^2023_A_Multi-scale_Genera",
        r"^2023_A_Novel_Multi-scale",
        r"^2023_Learning_Efficient",
        r"^2023_Limpets",
        r"^2023_OFAR",
        r"^2023_Vision-Language",
        r"^2023_Detection_of_Illegal",
        r"^2023_Super_Sparse_3D",
        r"^1-s2\.0-S0950705124009833",
        r"^2005_Active_Amplification",
        r"^2009_Embedded_Sensor",
        r"深度学习架构综述", r"深度学习单目深度估计",
        r"平衡神经网络搜索", r"高效变分分类",
        r"绿色AI的隐私保护",
        r"^cjig_paper_[1-9]",
        r"^cjig_计算机视觉_无人集群",
        r"^cjig_计算机视觉_沉浸式",
        r"超声波空中触觉", r"布料与刚体",
        r"自然历史馆藏", r"Mislabelled_Specimens",
        r"跨视角地理定位",
    ]),

    # ============== 兜底 ==============
    ("U_未归类", []),
]


def classify(name: str) -> str:
    """返回 primary_topic (单标签, 兼容旧行为)."""
    base = Path(name).name
    for topic, patterns in TOPICS:
        for pat in patterns:
            if re.search(pat, base, flags=re.IGNORECASE):
                return topic
    return "U_未归类"


def classify_multi(name: str) -> tuple[str, list[str]]:
    """返回 (primary_topic, topics[])。

    primary_topic 是按优先级第一个匹配上的主题 (跟 classify() 兼容)。
    topics 是所有匹配上的主题列表, 去重并保留顺序, 给后续多标签场景用。
    """
    base = Path(name).name
    matched: list[str] = []
    seen: set[str] = set()
    for topic, patterns in TOPICS:
        for pat in patterns:
            if re.search(pat, base, flags=re.IGNORECASE):
                if topic not in seen:
                    seen.add(topic)
                    matched.append(topic)
                break  # 一个主题内多个 pattern 只算一次
    if not matched:
        return "U_未归类", ["U_未归类"]
    return matched[0], matched


def main():
    parser = argparse.ArgumentParser(
        description="将 01-Papers/ 下的 PDF 按主题关键词分类, 输出 paper_classification.md",
    )
    parser.add_argument(
        "pdf_dir", nargs="?", type=Path, default=DEFAULT_PDF_DIR,
        help=f"PDF 所在目录 (默认: {DEFAULT_PDF_DIR})",
    )
    parser.add_argument(
        "--out", type=Path, default=None,
        help="输出 .md 路径 (默认: <pdf_dir>/paper_classification.md)",
    )
    parser.add_argument(
        "--topics-json", type=Path, default=None,
        help="同时输出 paper -> topics 映射的 JSON 路径 (默认: <pdf_dir>/paper_topics.json)",
    )
    args = parser.parse_args()

    if not args.pdf_dir.is_dir():
        sys.exit(f"错误: 目录不存在: {args.pdf_dir}")

    pdfs = sorted(p for p in args.pdf_dir.iterdir() if p.suffix.lower() == ".pdf")
    if not pdfs:
        sys.exit(f"错误: {args.pdf_dir} 下没有 PDF")

    buckets = {t: [] for t, _ in TOPICS}
    paper_topics: dict[str, list[str]] = {}  # stem -> topics[]
    for p in pdfs:
        primary, topics = classify_multi(p.name)
        buckets[primary].append(p.name)
        paper_topics[p.stem] = topics

    out = args.out or (args.pdf_dir / "paper_classification.md")
    write_report(pdfs, buckets, paper_topics, out)

    # 副产物: JSON 映射, 给后续脚本 (generate_skeleton_notes) 读
    topics_json = args.topics_json or (args.pdf_dir / "paper_topics.json")
    topics_json.write_text(
        json.dumps(paper_topics, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"已写入 {topics_json}")


def write_report(pdfs, buckets, paper_topics, out):
    total = len(pdfs)
    classified = sum(len(v) for k, v in buckets.items() if k != "U_未归类")
    unclassified = len(buckets["U_未归类"])

    lines = []
    lines.append(f"# 论文主题分类清单")
    lines.append("")
    lines.append(f"- **总计**: {total} 份 PDF")
    lines.append(f"- **已归类**: {classified}")
    lines.append(f"- **未归类**: {unclassified}")
    lines.append("")
    lines.append("> 说明：基于**文件名**做关键词匹配归类，未读 PDF 内容。")
    lines.append("> 一个 PDF 可同时属于多个主题 (topics), primary_topic 决定它在哪个分桶。")
    lines.append("> 主题代号：A=医学, B=算子, C=检测, D=3D, E=复原, F=分割, G=VLM, H=显著, I=文本, J=人脸, K=视频, L=数据集, M=行人, N=数学, O=安全, P=跨域, Q=自监督, R=综述, S=变化检测, T=其他, U=未归类, Z=杂项")
    lines.append("")

    # 主题统计
    lines.append("## 主题分布")
    lines.append("")
    lines.append("| 主题 | 数量 |")
    lines.append("|------|------|")
    for topic, _ in TOPICS:
        n = len(buckets[topic])
        if n > 0:
            lines.append(f"| {topic} | {n} |")
    lines.append("")

    # 详细列表
    lines.append("## 详细清单")
    lines.append("")
    for topic, _ in TOPICS:
        items = sorted(buckets[topic])
        if not items:
            continue
        lines.append(f"### {topic}（{len(items)}）")
        lines.append("")
        for n in items:
            stem = Path(n).stem
            tops = paper_topics.get(stem, [topic])
            if len(tops) > 1:
                lines.append(f"- {n}  \n  topics: {', '.join(tops)}")
            else:
                lines.append(f"- {n}")
        lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"已写入 {out}")
    print(f"总计 {total} 份，已归类 {classified}，未归类 {unclassified}")


if __name__ == "__main__":
    main()
