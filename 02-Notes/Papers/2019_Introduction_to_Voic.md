---
title: "Introduction to Voice Presentation Attack Detection and Recent Advances"
authors:
  - "Md Sahidullah"
  - "Héctor Delgado"
  - "Massimiliano Todisco"
  - "Tomi Kinnunen"
  - "Nicholas Evans"
  - "Junichi Yamagishi"
  - "Kong-Aik Lee"
year: 2019
venue: "arXiv (Handbook of Biometric Anti-Spoofing 章节)"
doi: 
pdf: [[2019_Introduction_to_Voic.pdf]]
primary_topic: T_通用_NLP_其他
topics:
  - "T_通用_NLP_其他"
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2019_Introduction_to_Voic.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/41 pages"
---
# Introduction to Voice Presentation Attack Detection and Recent Advances

## 基本信息
- **PDF**: [[2019_Introduction_to_Voic.pdf]]
- **primary_topic**: `T_通用_NLP_其他`
- **topics**: `T_通用_NLP_其他`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Introduction to Voice Presentation Attack Detection and Recent Advances |
| **作者** | Md Sahidullah; Héctor Delgado; Massimiliano Todisco; Tomi Kinnunen; Nicholas Evans; Junichi Yamagishi; Kong-Aik Lee |
| **发表时间** | 2019 (arXiv:1901.01085v1, cs.SD, 2019-01-04) |
| **刊物/会议** | arXiv 预印本 / 《Handbook of Biometric Anti-Spoofing》一章 (前一版章节 [8] 的更新版) |
| **DOI** | 未明确 |

## 摘要

> **清理后英文原摘要**（据提取文本修复空格与连字符断裂）：
> Over the past few years significant progress has been made in the field of presentation attack detection (PAD) for automatic speaker recognition (ASV). This includes the development of new speech corpora, standard evaluation protocols and advancements in front-end feature extraction and back-end classifiers. The use of standard databases and evaluation protocols has enabled for the first time the meaningful benchmarking of different PAD solutions. This chapter summarises the progress, with a focus on studies completed in the last three years. The article presents a summary of findings and lessons learned from two ASVspoof challenges, the first community-led benchmarking efforts. These show that ASV PAD remains an unsolved problem and that further attention is required to develop generalised PAD solutions which have potential to detect diverse and previously unseen spoofing attacks.

> **中文翻译**：过去几年里，针对自动说话人识别（ASV）的呈现攻击检测（PAD）领域取得了显著进展，包括新语音语料库的建立、标准评估协议的制定，以及前端特征提取与后端分类器的改进。标准数据库与评估协议的使用首次让不同 PAD 方案之间得以进行有意义的基准比较。本章总结了这些进展，重点关注近三年完成的研究。文章汇总了两届 ASVspoof 挑战赛（业界首个社区主导的基准评测）的发现与经验教训。这些结果表明，ASV 的呈现攻击检测仍是一个未解决的问题，仍需进一步努力，开发出有潜力检测多样化、此前未见的欺骗攻击的、具备泛化能力的 PAD 方案。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：ASV（自动说话人验证）技术近年走向成熟，已广泛用于逻辑访问（互联网/电话远程身份认证、网银/手机银行）与物理访问（住宅、办公等敏感场所门禁）。随着智能手机和带麦克风的语音智能设备（智能个人助理等）普及，ASV 有望更加无处不在。但其对呈现攻击（presentation attacks, PA，亦称 spoofing）的脆弱性已被公认，严重削弱了人们对该技术的信心。
- **ASV 为何尤其脆弱**：相比基于不易获取生物特征的其他系统，语音样本极易被欺诈者通过面对面或电话交谈采集，再回放欺骗系统；更进阶的语音转换、语音合成只需少量目标语音数据即可生成极有效的攻击。ISO/IEC 30107-1 标准 [3] 定义了 ASV 系统中可能的攻击点（图 1 列出 9 个点），其中最脆弱的两处是点 1（麦克风/物理访问）和点 2（传输点/逻辑访问），本文聚焦这两类攻击。
- **之前方法的问题**：在 ASVspoof 挑战赛之前，研究存在三点不足：1) 缺乏大规模、标准化的公开数据库和评估协议，不同方法难以公平比较；2) 对各类攻击（尤其语音合成、语音转换）的威胁程度评估不充分；3) 对检测方法的泛化能力研究不足。
- **核心矛盾**：ASV 的便捷普及性 与 其对呈现攻击的内在脆弱性之间的矛盾。攻击者能以低成本（重放录音、开源 TTS）欺骗系统，防御方却需开发不仅能检测已知攻击、还能应对未知新攻击的通用方案。

## 关键贡献

1.  **系统分类与综述**：将针对 ASV 的呈现攻击分为四类——模仿（impersonation）、重放（replay）、语音合成（speech synthesis）、语音转换（voice conversion），并分别综述其攻击原理（"欺骗"）与防御（"对策"）的早期研究。
2.  **总结 ASVspoof 挑战赛发现**：基于作者共同组织的两届 ASVspoof 挑战赛及其两个最流行的公开数据库，总结主要成果与教训，这是业界首个社区主导的标准化基准评测。（按摘要明确为"两届 ASVspoof 挑战赛"；提取文本未直接给出年份，原笔记称 2015 与 2017，与补读记录中出现的 "ASVspoof 2015" 标题一致，年份据原文后续页，提取缓存未覆盖，待核。）
3.  **梳理技术进展**：综述 PAD 系统前端特征提取与后端分类器的最新工作，并系统梳理语音合成技术的演进（共振峰规则→双音素拼接→单元选择→HMM 统计参数→深度学习 DNN/RNN/GAN/WaveNet/SampleRNN/Tacotron）。
4.  **指出未来方向**：摘要与引言明确，开发能检测"多样化且此前未见"欺骗攻击的、泛化能力强的 PAD 方案，仍是核心挑战；ASV PAD 是"未解决的问题"。

## 方法

本文是一篇**综述/手册章节**，其"方法"在于组织和阐述该领域的知识体系，而非提出新检测模型。

- **整体框架**：先介绍 ASV 系统及其脆弱性（图 1 标出 9 个攻击点），将 PAD 形式化为假设检验（公式 1）；再按四类攻击分节综述（第 2 节"模仿/重放/语音合成/语音转换"，各含"欺骗"与"对策"两小节）；最后讨论研究挑战与未来方向（据提取文本，引言说明章节"以讨论 PAD for ASV 的研究挑战和未来方向作结"，但具体内容在提取缓存未覆盖的后续页）。
- **PAD 问题形式化（公式 1）**：给定语音信号 S，判断 S 是自然语音（H0）还是 PA 方法生成的语音（H1）。设 X={x1,…,xN} 为从 S 提取的 N 帧声学特征向量，对数似然比分数为
  Λ(X) = log p(X|λH0) − log p(X|λH1)
  其中 λH0、λH1 分别是自然语音与 PA 语音的声学模型，参数由各自训练数据估计。测试语音与在开发集上计算的阈值 θ 比较：分数 ≥ θ 接受为自然语音，否则拒为 PA（图 2 给出典型 PAD 系统框图）。
- **三类防 PA 思路**：引言列出三种防范途径——1) 文本提示系统（要求用户说出系统指定文本，配合 utterance verification [4]）；2) 模板匹配/音频指纹，利用人无法重现完全相同语音信号来识别重放 [5]；3) 对真实语音与攻击语音作统计声学刻画 [6]。本文聚焦第三类，因其对文本相关与文本无关 ASV 都更实用。
- **关键模块回顾**：综述各攻击的技术演进。例：语音合成由两部分组成——文本分析（前端，文本→音素等语言学表示）与波形生成（后端）；历史上每十年一次范式转变（1970s 共振峰规则 → 1980s 双音素拼接 → 1990s 单元选择 → late 2000s HMM 统计参数合成 + MLLR 自适应 → 2010s 深度学习），近年端到端系统（WaveNet、SampleRNN、Tacotron）合成语音已可与人声媲美。
- **评价体系**：标准评估指标为等错误率 EER（FAR=FRR 时的错误率，FAR=PA 语音被判为自然语音的概率，FRR=自然语音被误判为 PA 的概率）；有时也用半总错误率 HTER（用开发集阈值计算的 FAR 与 FRR 的平均，引文 [7]）。
- **与已有综述的差异**：本文是《Handbook of Biometrics》[9] 第一版中章节 [8] 的更新版（"a continuation of the chapter [8]"），重点涵盖近三年（约 2016–2018）以 ASVspoof 挑战赛为驱动的新研究与新数据库。

## 实验

本文是综述，**未进行自身实验**，但系统整理了引用研究的关键实验结果（以下数值均出自提取文本前 12 页）：

- **重放攻击的脆弱性证据**：
    - [19]（文本相关、HMM-based ASV）：FAR 由 1% 升至 89%（男）、5% 升至 100%（女）。
    - [20]（文本无关、JFA 基线、远场移动电话场景）：冒充访问被重放攻击替换后 EER 由 1% 升至近 70%。
    - [21]（物理访问场景，GMM-UBM）：重放攻击 FAR 达 93%。
    - [18]（AVspoof 数据库，total variability 系统）：重放语音 FAR 男 77.4%、女 69.4%；对应条件下真实试验（bona fide）EER 男 6.9%、女 17.5%；该库还含用语音转换/语音合成生成的回放攻击（高质量设备回放时 FAR 更高）。
- **重放攻击的对策证据**：
    - [5]（文本相关，比对新样本与历史样本相似度）：多数实验中降低了 EER。
    - [20]/[22]（测量远场录音引入的信道差异）：欺骗检测错误率 < 10%。
    - [21]（基于信道特征差异，两种对策对比）：受攻击下 GMM-UBM 基线 EER 40%，第一种对策降至 29%，第二种降至 10%。
    - [23]（采集 175 名受试者的重放数据库，借鉴音乐识别比对频谱图局部极大值对）：回放攻击检测 EER 低至 1.0%。
- **语音合成攻击的脆弱性证据**：
    - [60]（HMM 合成 + 文本提示 ASV，仅 20 名说话人）：对真人语音 FAR 0%、FRR 7%；遭合成语音攻击时 FAR 升至超过 70%。
    - [64]（Wall Street Journal 语料，约 300 名说话人，GMM-UBM 与基于高斯超矢量的 SVM 两套系统）：HMM 合成语音使 FAR 分别升至 86%（GMM-UBM）和 81%（SVM）。
    - [65]（针对取证级 ASV 工具 BATVOX 的 HMM 合成攻击）：结论类似。上述合成器后被选作 ASVspoof 2015 数据库的欺骗方法之一。
    - [66]：仅有一项较小规模实验涉及 WaveNet、SampleRNN、GAN 等先进合成方法的欺骗，对其攻击力尚未充分研究。
- **泛化能力**：被反复指出为核心挑战；现有研究多在已知攻击条件下评估，对未知攻击的泛化研究不足。
- **效率信息**：提取文本中未讨论检测模型速度、参数量等效率信息。

> 提取缓存仅覆盖前 12/41 页（终止于第 2.3.2 节语音合成对策开头）。语音转换章节、PAD 前端特征/后端分类器的系统对比、ASVspoof 2015/2017 挑战赛的详细数据集规模与结果、最终结论等数值，据原文后续页，提取缓存未覆盖，待核（补读记录中可见 ASVspoof 2015 说话人数 "25/35/46" 与 "10/8/24" 等表 1 线索，但属补读摘录、非完整提取）。

## 局限

1.  **综述的深度限制**：对单个技术（如 WaveNet、GAN、Tacotron）仅作概述，深度不及专门论文。
2.  **模仿攻击研究匮乏（原文明确）**：缺乏可供定量研究的大规模模仿语音语料；且因模仿者是产生完全自然语音的真人、不留录放设备或合成转换的信号痕迹，现有文献中没有任何针对模仿攻击的对策工作，对策设计本身也具挑战性。
3.  **时效性**：发表于 2019 年初，主要覆盖 2018 年及以前工作；此后端到端深度学习、自监督等新方法未涵盖。
4.  **评估侧重**：以特定挑战赛数据库性能为主，对真实复杂场景（不同信道、噪声环境、低质量语音）下的鲁棒性讨论相对不足（此为综合判断，提取文本未单独成节论述）。

## 个人评论

> 本节为 AI 综合评述，供参考。

1.  **全面的知识地图**：为初学者与研究者提供 ASV 欺骗与检测领域的全景图——从四类攻击、技术演进到评估协议，系统清晰，是快速进入该领域的优秀入门材料。
2.  **基于社区基准的洞察**：对 ASVspoof 挑战赛的总结有价值，因为它揭示了统一公平条件下不同方法的优劣；其核心结论"PAD 仍是未解决问题""需开发泛化能力强的方案"为后续数年研究定下基调。
3.  **研究范式的启发**：展示了良好的安全研究范式——攻防对抗视角、标准化评估框架、从具体攻击到通用防御的挑战升级。对设计类似安全研究（如图像/语音深度伪造检测）有借鉴意义。论文把检测问题清晰地形式化为对数似然比假设检验（公式 1），这一形式化值得借鉴。
4.  **指明技术瓶颈**：明确瓶颈不在特定攻击检测率，而在泛化到未见攻击的能力，启发后续关注特征不变性、模型鲁棒性与域自适应。

### 使用建议

- **如果快速了解**：读摘要 + 第 1 节引言（ASV 脆弱性与三类防范思路）+ 第 2.3 节语音合成的技术演进 + 末尾"研究挑战与未来方向"（提取缓存未覆盖，需查原文后续页）。可快速掌握问题背景、核心挑战与攻击分类。
- **如果复现**：本文为综述无需复现；应转向其引用的 ASVspoof 挑战赛基线系统论文与关键特征论文（如 CQCC）作为复现起点。
- **如果借鉴创新点**：学习 1) 将安全检测问题定义为对数似然比假设检验；2) 按"攻击—防御"逻辑组织安全子领域综述；3) 以公开挑战赛驱动领域标准化的研究范式。
- **如果写 Related Work**：放在"语音反欺骗/呈现攻击检测"小节，作为该子领域的重要早期综述引用，用于交代研究背景与基础问题定义。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_通用_NLP_其他]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**语音生物特征安全 / 自动说话人验证（ASV）反欺骗**方向，是一篇**综述（手册章节）**，是《Handbook of Biometrics》中早先章节 [8] 的更新版。它要解决的核心问题是：ASV 系统易受呈现攻击（presentation attacks / spoofing）。文章系统梳理四类攻击（模仿、重放、语音合成、语音转换）及其呈现攻击检测（PAD）方法，并以两届 ASVspoof 挑战赛为主线总结进展。由于它本质是语音处理领域的安全综述、不属任何具体 CV 主题，归入 **`T_通用_NLP_其他`** 是合适的（语音与 NLP 相邻；也与"安全/对抗"沾边，但全文围绕语音处理而非视觉对抗，故不归 CV/对抗类）。

## 2. 一句话总结
本文系统综述了针对自动说话人验证系统的四类呈现攻击及其检测（PAD）技术，将检测形式化为对数似然比假设检验，并以两届 ASVspoof 挑战赛为主线指出：开发能泛化到未见攻击的通用 PAD 仍是未解决的关键挑战。

## 3. 背景与问题
- **为什么要做**：ASV 已成熟并广泛用于逻辑访问（网银、电话/互联网远程认证）与物理访问（门禁），随语音智能设备普及将更普遍；但其对呈现攻击的脆弱性已被公认（ISO/IEC 30107-1 [3] 给出 9 个攻击点，最脆弱为麦克风点 1 与传输点 2），削弱了技术可信度。
- **ASV 为何尤其脆弱**：语音样本可经面对面或电话交谈轻易采集后回放；语音转换/合成只需少量目标语音即可生成有效攻击。
- **之前方法的问题**：ASVspoof 之前缺乏标准化大规模公开库与评估协议→难以公平比较；对合成/转换攻击威胁评估不足；泛化能力研究欠缺。
- **三类防范思路**：文本提示 + utterance verification [4]；模板匹配/音频指纹防重放 [5]；对真实/攻击语音作统计声学刻画 [6]（本文聚焦第三类）。

## 4. 核心贡献
1.  **四类攻击的系统分类与综述**：模仿、重放、语音合成、语音转换，各含"欺骗"与"对策"。
2.  **以两届 ASVspoof 挑战赛为主线总结**：基于作者共同组织、业界最流行的两个公开数据库，提炼成果与教训（年份 2015/2017 据原文后续页，提取缓存未覆盖，待核）。
3.  **技术进展梳理**：尤其完整梳理语音合成范式演进（共振峰规则→双音素→单元选择→HMM 统计参数→DNN/RNN/GAN/WaveNet/SampleRNN/Tacotron）。
4.  **指明未来方向**：泛化到"多样化且未见"的攻击是核心未解难题。

## 5. 方法详解
本文为综述，"方法"即知识体系的组织：
- **整体框架**：引入 ASV 脆弱性（图 1）→ PAD 形式化为假设检验（公式 1，图 2 框图）→ 四类攻击分节综述 → 研究挑战与未来方向作结。
- **PAD 形式化**：H0=自然语音、H1=PA 语音；X={x1,…,xN} 为 N 帧声学特征；对数似然比 Λ(X)=log p(X|λH0)−log p(X|λH1)（公式 1）；阈值 θ 在开发集上确定，Λ(X)≥θ 则接受为自然语音。
- **评估指标**：EER（FAR=FRR 处的错误率）；HTER（开发集阈值下 FAR、FRR 的平均，[7]）。
- **语音合成两部件**：文本分析（前端）+ 波形生成（后端）；十年一范式：1970s 共振峰规则、1980s 双音素拼接 + LP、1990s 单元选择、late 2000s HMM 统计参数 + MLLR 自适应、2010s 深度学习与端到端（WaveNet/SampleRNN/Tacotron），合成语音已近人声；技术对比可参考 Blizzard Challenge [57,58]。
- **定位**：是章节 [8] 的更新版，覆盖近三年以 ASVspoof 为驱动的新研究。

## 6. 实验与结果
综述自身无实验，整理引用结果（数值均出自提取文本前 12 页）：
- **重放-脆弱性**：[19] FAR 1→89%(男)/5→100%(女)；[20] JFA 下 EER 1%→近 70%；[21] GMM-UBM FAR 93%；[18] AVspoof FAR 男 77.4%/女 69.4%，bona fide EER 男 6.9%/女 17.5%。
- **重放-对策**：[5] 多数实验降低 EER；[20]/[22] 信道差异法欺骗检测错误率 <10%；[21] 受攻击 EER 40%→对策一 29%→对策二 10%；[23] 175 名受试者库，回放检测 EER 低至 1.0%。
- **合成-脆弱性**：[60] HMM 合成（仅 20 人）FAR 0%→>70%、真人 FRR 7%；[64] WSJ 约 300 人，FAR 升至 86%(GMM-UBM)/81%(SVM)；[65] 对取证工具 BATVOX 结论类似；[66] WaveNet/SampleRNN/GAN 欺骗仅小规模实验，尚未充分研究。
- **泛化**：被指为核心挑战，现有研究多评估已知攻击。
- **效率信息**：提取文本未讨论。
- 语音转换章节、PAD 特征/分类器系统对比、ASVspoof 详细数据集规模与挑战结果：据原文后续页，提取缓存未覆盖，待核。

## 7. 这篇论文真正有价值的地方
1.  **全面的知识地图**：四类攻击 + 技术演进 + 评估协议，系统清晰，入门首选。
2.  **基于社区基准的洞察**：ASVspoof 总结揭示统一条件下方法优劣，定下"PAD 未解决""需泛化"基调。
3.  **可迁移的安全研究范式**：攻防对抗视角 + 标准化评估 + 从具体攻击到通用防御的挑战升级 + 对数似然比假设检验形式化。
4.  **指明技术瓶颈**：瓶颈在泛化到未见攻击，而非单一攻击检测率。

## 8. 局限与问题
1.  **深度有限**：对 WaveNet/GAN/Tacotron 等仅概述。
2.  **模仿攻击研究匮乏（原文明确）**：无大规模模仿语料；模仿者是产生自然语音的真人、不留信号痕迹，文献中无任何针对模仿的对策。
3.  **时效性**：覆盖至 2018 年，端到端/自监督新方法未涵盖。
4.  **评估侧重**：偏挑战赛数据库性能，真实复杂场景鲁棒性讨论相对不足（综合判断，提取文本未单独成节）。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 第 1 节引言 + 第 2.3 节语音合成演进 + 末尾"研究挑战与未来方向"（后者在提取缓存未覆盖、需查原文）。
- **复现**：综述无需复现，转向其引用的 ASVspoof 基线系统与关键特征论文（如 CQCC）。
- **借鉴创新点**：1) 将安全检测形式化为对数似然比假设检验；2) 按"攻击—防御"组织安全综述；3) 以公开挑战赛驱动标准化。
- **写 Related Work**：放在"语音反欺骗/呈现攻击检测"小节，作为重要早期综述引用。

## 10. 和其他论文的关系
- 是 **ASVspoof Challenge 系列**研究的总结性章节，与后续 `[[ASVspoof 2019 Challenge]]` 直接相关（后者扩展了攻击类型与评估场景）。
- 作为综述，引用并总结大量基础工作，如 CQCC 特征论文与基于 GMM-UBM/JFA/total-variability 的基线系统。
- 与**生物特征识别安全**、**语音深度伪造检测**领域的其他综述相关。

## 11. 关键词
语音呈现攻击检测, 自动说话人验证, 呈现攻击/欺骗, 反欺骗对策, 模仿攻击, 重放攻击, 语音合成, 语音转换, ASVspoof, 等错误率 EER, HTER, 对数似然比假设检验, 泛化能力, 综述

## 12. 可信度说明
本精读笔记基于 PDF 提取文本生成。**提取缓存仅覆盖前 12/41 页**（终止于第 2.3.2 节语音合成对策的开头）。已覆盖的部分包括：标题、作者与单位、摘要、引言（ASV 脆弱性、ISO/IEC 30107-1 攻击点、三类防范思路）、PAD 假设检验形式化（公式 1）与系统框图、第 2 节基础（模仿与重放两类攻击的"欺骗+对策"完整综述、含全部引文数值）、以及语音合成技术演进与部分欺骗实验综述。文本提取质量良好（约 2086 字符/页）、逻辑连贯，足以支撑对论文研究背景、核心问题、基本框架、形式化方法与前述攻击类型实验结论的准确理解。**但**语音转换章节、PAD 前端特征/后端分类器的系统对比、ASVspoof 2015/2017 挑战赛的数据集规模与详细结果、以及最终结论与未来展望等，提取缓存未覆盖；笔记中涉及这些内容之处已逐一标注"据原文后续页，提取缓存未覆盖，待核"。本笔记为 AI 阅读稿（`ai_generated: true`），未经人工精读复核（`human_reviewed: false`）。

---

> **可信度补充**: PDF 提取质量 = **high** (提取文本质量好, 约 2086 字符/页; 但提取缓存仅覆盖前 12/41 页, 截断于第 2.3.2 节); 来源缓存: `.paper-cache/extracts/2019_Introduction_to_Voic.txt` (提取 12/41 页; 原 AI 主体 12/41 + 补读记录摘录 13-41); 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-41; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-41。
- **提取情况**: 缺失页 29 页, 其中 29 页提取到可读文本。缺失页包含正文、实验、讨论或附录内容, 已按页补读摘录。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Introduction to V oice Presentation Attack Detection and Re cent Advances 13
- p.13: Due to fact that majority of VC techniques operate at the shor t-term frame level,
- p.13: VC systems that consider long-term dependency such as recur rent or autoregressive
- p.13: After the ASVspoof challenges took place, new countermeasu res that works for
- p.13: The1initiative aims to overcome this bottleneck by making avail able standard
- p.14: 14 Authors Suppressed Due to Excessive Length
- p.14: Next, the evaluation set without any label indicating genui ne or spoofed speech was
- p.14: TERSPEECH conferences, which also involved sharing knowle dge and receiving
- p.14: 3.1 ASVspoof 2015
- p.15: Introduction to V oice Presentation Attack Detection and Re cent Advances 15
- p.15: Natural speech Recorded using high-quality microphone Recorded using different smart phones
- p.15: No of speakers 25 / 35 / 46 10 / 8 / 24

### 缺失页关键摘录

- p.13: ulation feature can also detect converted speech [123]. Ano ther experiment reported
- p.13: lack of publicly available corpora and evaluation protocol to help with comparing
- p.13: speech corpora consisting of a large number of spooﬁng attac ks, evaluation proto-
- p.13: cols, and metrics to support a common evaluation and the benc hmarking of different
- p.13: systems. The speech corpora were initially distributed by o rganising an evaluation
- p.14: Next, the evaluation set without any label indicating genui ne or spoofed speech was
- p.14: The evaluation keys were subsequently released to the chall enge participants. The
- p.14: challenges are shown in Table 1. In both the challenges, EER m etric was used to
- p.14: mixture of voice conversion and speech synthesis technique s [125]. The dataset was
- p.14: evaluation set, along with the known attacks. Thus, this pro vides the possibility of
- p.14: assessing the generalisability of the spooﬁng detectors. T he detailed evaluation plan
- p.15: Table 1: Summary of the datasets used in ASVspoof challenges .
<!-- AI_READING_NOTE_END -->
