---
title: "EdgeAI Drone for Autonomous Construction Site Demonstrator*"
authors:
  - "Emre Girgin"
  - "Arda Taha Candan"
  - "Coşkun Anıl Zaman"
year: 2025
venue: "arXiv"
doi: 
pdf: [[2025_EdgeAI_Drone_for_Aut.pdf]]
primary_topic: R2_控制_生物启发_其他跨学科
topics:
  - "R2_控制_生物启发_其他跨学科"
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
extract_cache: .paper-cache/extracts/2025_EdgeAI_Drone_for_Aut.txt
---

# EdgeAI Drone for Autonomous Construction Site Demonstrator*

## 基本信息
- **PDF**: [[2025_EdgeAI_Drone_for_Aut.pdf]]
- **primary_topic**: `R2_控制_生物启发_其他跨学科`
- **topics**: `R2_控制_生物启发_其他跨学科`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | EdgeAI Drone for Autonomous Construction Site Demonstrator* |
| **作者** | Emre Girgin (Embry-Riddle 航空大学 / 项目期间任职于 TUBITAK BILGEM); Arda Taha Candan; Coşkun Anıl Zaman (均属 TUBITAK BILGEM 机器人与自主系统部, 土耳其 Gebze) |
| **发表时间** | 2025 (arXiv:2505.09837v1, cs.RO, 2025-05-14) |
| **刊物/会议** | arXiv 预印本 (案例研究 / demonstrator 论文) |
| **DOI** | 未明确 (arXiv 编号 2505.09837) |
| **代码/数据** | github.com/egirgin/storaige-b950 (公开数据集) |
| **资助** | ECSEL JU (No 101007321, Horizon 2020); TUBITAK 项目号 121N347 |

## 摘要

清理后英文原摘要 (据提取文本修复空格/连字符、剔除杂入字符):

> The fields of autonomous systems and robotics are receiving considerable attention in civil applications such as construction, logistics, and firefighting. Nevertheless, the widespread adoption of these technologies is hindered by the necessity for robust processing units to run AI models. Edge-AI solutions offer considerable promise, enabling low-power, cost-effective robotics that can automate civil services, improve safety, and enhance sustainability. This paper presents a novel Edge-AI-enabled drone-based surveillance system for autonomous multi-robot operations at construction sites. Our system integrates a lightweight MCU-based object detection model within a custom-built UAV platform and a 5G-enabled multi-agent coordination infrastructure. We specifically target the real-time obstacle detection and dynamic path planning problem in construction environments, providing a comprehensive dataset specifically created for MCU-based edge applications. Field experiments demonstrate practical viability and identify optimal operational parameters, highlighting our approach's scalability and computational efficiency advantages compared to existing UAV solutions. The present and future roles of autonomous vehicles on construction sites are also discussed, as well as the effectiveness of edge-AI solutions. We share our dataset publicly at github.com/egirgin/storaige-b950.

中文翻译:

> 自主系统与机器人正在建筑、物流、消防等民用领域受到广泛关注。然而, 运行 AI 模型所需的高性能处理单元成为这些技术大规模落地的障碍。边缘 AI (Edge-AI) 方案颇具前景: 它以低功耗、低成本的方式赋能机器人, 从而自动化民用服务、提升安全性并增强可持续性。本文提出一套新颖的、基于边缘 AI 的无人机监控系统, 用于建筑工地上的自主多机器人协同作业。该系统在自研无人机 (UAV) 平台中集成了轻量化、基于 MCU 的目标检测模型, 并配以 5G 支撑的多智能体协调基础设施。我们专门针对建筑环境中的实时障碍物检测与动态路径规划问题, 并提供了一个专为 MCU 边缘应用打造的完整数据集。现场实验验证了系统的实用可行性并确定了最优作业参数, 凸显出本方法相较现有 UAV 方案在可扩展性与计算效率上的优势。文中还讨论了自主车辆在建筑工地中当前与未来的角色, 以及边缘 AI 方案的有效性。数据集已公开于 github.com/egirgin/storaige-b950。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么做**：建筑业是劳动密集型、危险性高的行业, 长期面临生产率增长缓慢、劳动力成本高、生产低效等问题 (论文 Related Work 引文 [8][9])。自主系统 (无人机、无人车) 在建筑、物流、消防等民用领域前景广阔, 其更深层的社会价值在于自动化关键服务、降低人员风险, 而非仅面向消费端。
- **之前方法的问题**：关键瓶颈是对高性能算力的依赖。现有建筑机器人多依赖 CPU/GPU 等强算力平台, 成本高、功耗大; 已有自主挖掘机工作 (如 Jin et al. 的 AES, 论文 [14]) 局限于单挖掘机控制; 无人机在建筑中多用于"检查与规划" (inspection/planning, [16][17]) 而非实时作业协调。此外, MCU 输入分辨率极低, 使 VisDrone 等现有数据集因目标占帧比过小而效果不佳, 缺乏面向 MCU 边缘部署的专用数据集。
- **核心矛盾**：**建筑工地自动化对实时性、低成本、可扩展性的要求**, 与**传统 AI 模型对强算力的依赖**之间的矛盾。本文给出的答案是: 用为低功耗 MCU 量化的轻量 AI 模型, 以最小成本实现可扩展的实时部署。
## 关键贡献

论文 Introduction 末尾明确列出三条贡献:

1.  **多机器人协调系统**：提出一个专为动态建筑工地作业定制的多机器人协调系统, 集成自主车辆 (自主挖掘机、UGV) 与基于无人机的监控。
2.  **受限 MCU 硬件上的实时检测**：在受限的 MCU 硬件上用边缘 AI 实现障碍物与人员存在的实时检测, 并在由中央协调器软件管理的真实建筑环境中完成验证。
3.  **专用边缘 AI 数据集 TUBITAK-EdgeDrone**：创建并公开了一个为小尺寸边缘 AI 应用 (无人机实时建筑工地监控) 专门策划的新数据集。据正文, 该数据集约含 **25,000 张训练 + 5,000 张测试图像**, 附带 GNSS 元数据, 并另提供高分辨率图像集供更强平台使用。
## 方法

### 整体框架
系统目标是执行一次协同自主的"装载-倾倒 (load-dump)"作业。三大组成 (架构见论文 Figure 2): ① **中央协调器 (GCS)**：基于 ROS 的地面控制站, 负责全局规划、任务分配、状态监控与实时决策; 路径规划使用 **Voronoi 图 + A\*** 算法。② **地面车辆**：自主挖掘机与自研 UGV, 执行航点 (waypoint) 导航命令。③ **边缘 AI 无人机**：搭载 STM32 的自研六旋翼, 检测动态障碍物并把其全局位置发给 GCS 用于无碰撞路径规划, 形成闭环。所有实体通过 **5G 蜂窝网络**互联, 车辆与 GCS 间通信采用 **MQTT** (因其轻量、支持 QoS, 且可经 `mqtt bridge` 与 ROS 无缝集成)。

### 输入与输出
- **无人机 AI 模型输入**：机载相机拍摄的**俯视单目 RGB 图像帧** (vision node 经串口发给 MCU)。
- **AI 模型输出**：图像中障碍物 (尤其人员) 的检测结果 (类别 + 边界框)。
- **系统最终输出**：检测目标的**全局坐标**, 作为动态障碍物供 GCS 进行避障路径规划。

### 关键模块与连接
1.  **自主无人机设计 (六旋翼)**：Pixhawk 飞控 (FCU)、6 个 BLDC 无刷电机、模块化碳纤维机架 (初版用 3D 打印件原型化); 续航约 **10–11 分钟**; 视觉模块配独立供电以保证不间断处理与通信。机载集成: 通用机载计算机 (运行 ROS Noetic, 配 MAVROS 做飞控、MQTT 做系统间通信)、**STM32F769i-Discovery** MCU 板、5G 路由器、底座相机。机载计算机经串口把图像帧发给 MCU, MCU 跑量化模型推理后回传预测——这种"机载计算机 / MCU"抽象隔离了推理过程、降低主机算力负担。
    > 注: 提取文本未明确写出机载计算机型号, 但 Table I 的现场基准列为 "A72 (1.8 GHz)" 即 Raspberry Pi 4 (Cortex-A72), 现场测试即用其跑 AI。
2.  **中央协调器软件 (GCS)**：前后端分离的模块化架构, 利于可扩展与独立升级。
    - **前端**：基于 React + Redux 的响应式 Web 界面 (任意设备可访问), 集成 Mapbox 做站点可视化, 经 `roslibjs` 与 `mqtt bridge` 与 ROS 后端实时通信。
    - **后端**：基于 ROS, 核心节点含 operation manager (任务解析)、vehicle agents (车辆直接控制)、task planner (按就近原则分派任务)、path planner (Voronoi 图 + A\*)。通信遵循 **VDA5050 协议**以保证与 AGV 系统互操作。
3.  **边缘 AI 与数据收集**：
    - **模型部署**：MCU 在算力/内存/模型复杂度上限制很大, 故采用**量化**压缩模型。论文在通用 CPU、树莓派、STM32 MCU 上比较了多种轻量目标检测模型 (ST-SSD 系列、SSDv2、YoloLC、TinyYolo) 的速度。
    - **坐标转换 (关键创新)**：单目俯视相机因位姿多样性不足, 对传统 structure-from-motion 是病态问题。论文改用轻量实时方法:
        - **步骤1 RANSAC 模型**：在锥形标记 (cone-marked) 场地采集数据, 训练 RANSAC 回归模型, 学习"**每米对应的像素数**与**无人机高度**之间的关系" (即由像素尺度 + 高度反推真实距离)。比较了线性/二次/三次/四次多项式复杂度。
        - **步骤2 测地变换**：将 RANSAC 得到的局部坐标, 结合 GNSS 数据经测地变换 (geodesic transformation) 转为全局坐标, 使 GCS 可将检测目标视为动态障碍物。整条管线以 MCU 量化推理执行, 保持实时性而不过载机载资源。
    - **专用数据集 TUBITAK-EdgeDrone**：为解决 MCU 模型输入分辨率受限、VisDrone 等数据集目标占帧比过低的问题而创建。约 25,000 训练 + 5,000 测试图, 适配小输入尺寸; 含 GNSS 元数据 (支持视觉里程计等任务); 另含高分辨率工地图像集供更强平台。这种双层级数据集覆盖从轻量 MCU 部署到更广机器人/CV 研究的多种应用。

### 训练与推理流程
- **训练**：在通用计算机上, 用自定义数据集 (TUBITAK-EdgeDrone) 与公开数据集 (VisDrone, 论文 [19]) 训练多个目标检测模型; 训练后**量化**以适配 MCU。
- **推理流程**：
    1. 无人机相机捕获图像帧。
    2. 机载计算机 (ROS vision node) 经串口发送至 STM32 MCU。
    3. MCU 跑量化模型做目标检测。
    4. 检测结果回传机载计算机。
    5. 机载计算机用无人机高度 + 检测框像素尺寸, 经预训练 RANSAC 模型估算局部坐标, 再结合 GNSS 经测地变换转为全局坐标。
    6. 全局坐标经 5G 以 MQTT 消息发送给 GCS。

### 与已有方法的差异
与以往依赖高性能算力、或仅把无人机用于检查/规划 ([16][17]) 的方案不同, 也不同于常见的边缘 AI + 5G 无人机系统 ([18]), 本文**用轻量、为低功耗 MCU 量化的 AI 模型**, 强调无人机在动态场景中的**实时作业协调角色**, 与地面车辆协同, 构成从感知 (MCU AI) 到决策 (GCS) 再到执行 (车辆) 的闭环。
## 实验

实验分实验室环境与现场测试 (field tests) 两部分; 现场测试侧重集成全部成员后的定性洞察。

- **使用的数据集**：
    - **模型速度测试**：自定义 **TUBITAK-EdgeDrone** + 公开 **VisDrone** (论文 [19])。
    - **RANSAC 模型训练/测试**：锥形标记场地采集的数据 (已知两像素间真实距离)。
    - **现场测试场地**：TÜBİTAK Gebze 校园的 **OpenAirLab**, 约 5000 平方米 (50 米 × 100 米), 配备 WiFi、全覆盖固态 LIDAR (实时点云)、IP 摄像头、5G 蜂窝覆盖。
- **对比方法**：主要对比 (a) 不同量化目标检测模型在三种硬件 (i7-8700 / A72 / M7) 上的**速度**; (b) 不同阶数 RANSAC 多项式模型的**精度**。论文未与重型 AI 模型做准确率对比 (注: 论文称更高输入分辨率网络精度略好但差异不显著, 故未列入表)。
- **评价指标**：
    - **模型速度**：FPS (每秒帧数)。
    - **RANSAC 精度**：RMSE (厘米, 越低越好)。
    - **系统评估**：现场测试的定性观察与可行性。
- **主实验结果**：
    - **模型速度 (Table I, 量化模型 FPS)**：YoloLC-192 在 M7 上最快, 达 **0.85 FPS**; 其大小 339.3 KB, 在 i7-8700 上 796.6 FPS、A72 上 257.9 FPS。完整表如下:

      | 模型 (分辨率) | 大小 (KB) | i7-8700 (3.2GHz) | A72 (1.8GHz) | M7 (216MHz) |
      |---|---|---|---|---|
      | ST-SSDv1-192 | 594.4 | 365.1 | 124.7 | 0.39 |
      | ST-SSDv1-256 | 789.8 | 208.8 | 74.4 | 0.21 |
      | SSDv2-256 | 1559.2 | 66.4 | 33.6 | 0.13 |
      | SSDv2-416 | 1604.2 | 25.0 | 12.7 | 0.06 |
      | **YoloLC-192** | 339.3 | 796.6 | 257.9 | **0.85** |
      | YoloLC-256 | 339.3 | 447.1 | 131.2 | 0.44 |
      | TinyYolo-224 | 11105.5 | 74.7 | 18.2 | 0.13 |
      | TinyYolo-416 | 11105.5 | 22.0 | 5.4 | 0.05 |

    - **RANSAC 精度 (Table II, RMSE cm)**：随复杂度上升精度提高, **三次 (cubic) 多项式足够**且被选用于现场部署。各高度 RMSE:

      | 多项式阶数 | 5 m | 8 m | 10 m | 15 m |
      |---|---|---|---|---|
      | 线性 (1) | 46.9 | 3.2 | 26.5 | 32.3 |
      | 二次 (2) | 12.1 | 6.9 | 25.7 | 24.1 |
      | **三次 (3)** | 5.2 | **3.7** | 23.4 | 22.2 |
      | 四次 (4) | 5.6 | 2.7 | 24.2 | 29.4 |

    - **最优飞行高度 ≈ 8 米**：低空因重复检测同一锥标导致误差偏高, 高空因锥标变小难检测也误差偏高, 折中取约 8 米。
    - **现场测试 (Field Tests)**：在 OpenAirLab 执行挖掘机 + UGV 的"装载-倾倒"任务, 无人机航测并把检测到的人员位置转发给 GCS, GCS 据此调整重型车辆路线; 两车合计导航约 **250 米**。**因 MCU (M7) 检测速度 (0.85 FPS) 不满足实时要求, 现场实际改用 A72 (树莓派) 跑 AI。**
- **消融实验**：PDF 文本未明确传统意义上的消融实验 (移除模块看性能变化)。RANSAC 多项式阶数对比可视作一种参数消融。
- **泛化实验**：仅在 OpenAirLab 单一场地做集成验证, 未提及其他工地类型的泛化测试。
- **效率信息**：核心体现在**模型大小** (最优 YoloLC 仅 339.3 KB) 与 **MCU 推理速度** (最高 0.85 FPS); 现场因 MCU 速度不足, 退化到用 A72 运行。
## 局限

1.  **现场测试的妥协 (最关键)**：现场演示中 MCU (M7) 的 0.85 FPS 无法满足实时路径规划, 系统**实际改用算力更强的 A72 (Raspberry Pi 4, 257.9 FPS)** 跑 AI——这一点论文在 Field Tests 节明确承认。它削弱了"完全在 MCU 上实现"的论证, 凸显当前 MCU 算力与实时应用需求间的巨大差距。
2.  **检测精度未量化**：论文只报速度 (FPS), **未给检测精度** (如 mAP)。仅称高分辨率网络精度"略好但差异不显著"。动态工地下低帧率 + 未知精度对避障的及时性/可靠性是隐忧。
3.  **场景相对结构化**：现场仅"装载-倾倒"单一循环, 环境相对规整。更复杂、无序的真实工地下系统鲁棒性与可扩展性待验证。
4.  **缺乏长期与可靠性数据**：仅短期演示性测试 (无人机续航仅 10–11 分钟), 未涉及长期稳定性、通信中断处理、续航对整体作业时长的影响等工程问题。
5.  **位姿估计假设依赖**：RANSAC 坐标转换依赖相对平稳的飞行高度与可控相机参数; 8 米外/近地误差均上升, 剧烈姿态变化或颠簸时局部坐标估计可能失真。
## 个人评论

1.  **端到端的系统思维 (而非单点算法)**：论文最大价值不在某个新模型, 而在一个**从感知到协同决策的端到端集成 demonstrator**: 它清晰定义了无人机、地面车辆、GCS、5G/MQTT 在系统中的角色与交互, 给复杂环境的多机器人协同提供了可复用的架构参考 (含 VDA5050、Voronoi+A\* 等成熟工业组件的组合)。
2.  **面向约束的工程实践**：论文不盲目追 SOTA 精度, 而**正视 MCU 的算力天花板**, 围绕此约束做一连串工程取舍: 量化压模型、为低分辨率构建专用数据集、用 RANSAC + 高度反推距离替代重型视觉里程计/SfM。这种"在硬约束下解问题"的思路对工业落地很有启发——尽管最终现场仍退化到 A72, 反而诚实暴露了边缘 AI 当前的真实边界。
3.  **数据集贡献是实质性的**：专为低分辨率、MCU 边缘部署创建并公开 TUBITAK-EdgeDrone (约 3 万图 + GNSS 元数据 + 双分辨率层级), 填补了 VisDrone 等"目标占帧比过小"在 MCU 上的空白, 对无人机巡检方向的边缘 AI 研究有复用价值。
4.  **诚实但论证偏弱**：作为案例研究/demonstrator 论文, 其贡献偏"工程集成 + 数据集", 缺少与基线的定量对比和精度评估, 因此更适合作为工程参考与数据来源, 而非方法论 SOTA 引用。

### 使用建议

- **如果快速了解**：读 **Abstract**、**I. Introduction** (背景 + 三条贡献)、**III. Methodology** (系统架构)、**V. Conclusion**。
- **如果复现**：精读 **III.C/III.D** 与 **IV. Experiments**。核心是复现 RANSAC 坐标转换 (像素尺度 + 高度 → 真实距离 → 测地变换 → 全局坐标) 和 STM32 上量化模型部署 + 串口通信流程; 数据集可从 github.com/egirgin/storaige-b950 获取。
- **如果借鉴创新点**：
    - **系统集成**：学习"GCS (React/Redux + ROS, VDA5050, Voronoi+A\*) + 5G/MQTT + 边缘 AI 车辆"的多智能体架构。
    - **边缘部署策略**：模型选择 → 量化 → STM32 串口推理隔离的完整流程。
    - **轻量数据集构建**：如何针对低分辨率、小目标的边缘场景有针对性地采集/标注 (含 GNSS 元数据、双分辨率层级)。
- **如果写 Related Work**：可归入 1) 建筑机器人/自动化; 2) 无人机在建筑的应用 (强调实时作业协调而非仅检查); 3) 边缘计算/AI 在机器人中的应用; 4) MCU 嵌入式深度学习部署。
## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[R2_控制_生物启发_其他跨学科]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**自主系统 / 机器人学 (cs.RO)** 与**边缘人工智能 (Edge-AI)、计算机视觉**的交叉应用, 聚焦**建筑施工自动化**。它是一篇案例研究 / demonstrator 论文, 解决的问题是: 在动态建筑工地, 如何用低功耗、低成本的边缘计算 (MCU) 实现多机器人协同作业中的实时人员/障碍物检测、目标全局定位与避障路径规划。适合作为"边缘 AI 在工业机器人中的应用""建筑自动化与机器人""无人机实时监控系统"等主题下的参考案例 (本库归类为 R2_控制_生物启发_其他跨学科)。

## 2. 一句话总结
本文构建并现场演示了一套基于边缘 AI 的无人机监控系统: 在 STM32 MCU 上部署量化目标检测模型实时感知工地人员, 经 RANSAC + GNSS 测地变换得到障碍物全局坐标, 通过 5G/MQTT 与地面自主车辆 (挖掘机、UGV) 经 ROS 中央协调器 (GCS) 协同, 完成自主"装载-倾倒"作业。

## 3. 背景与问题
- **为什么做**：建筑业劳动密集、危险、生产率低 ([8][9]), 对自动化需求迫切; 自主系统在民用领域前景广阔, 但受限于运行 AI 模型所需的高性能算力。
- **之前方法的问题**：① 依赖 CPU/GPU 等高算力, 成本/功耗高; ② 已有自主挖掘机 (AES, [14]) 仅单机控制; ③ 无人机多用于检查/规划 ([16][17]) 而非实时作业协调; ④ MCU 输入分辨率极低, VisDrone 等数据集目标占帧比过小不适用, 缺乏 MCU 专用数据集。
- **核心矛盾**：实时性 + 低成本 + 可扩展 ⟷ 传统 AI 对强算力的依赖。作者答案: 用为低功耗 MCU 量化的轻量模型, 以最小成本实现可扩展实时部署。

## 4. 核心贡献
1.  **多机器人协调系统**：专为动态工地定制, 集成自主挖掘机、UGV 与无人机监控。
2.  **受限 MCU 上的实时检测**：用边缘 AI 在 STM32 上实现障碍物/人员实时检测, 并由中央协调器在真实工地环境中验证。
3.  **TUBITAK-EdgeDrone 数据集**：为小尺寸边缘 AI 应用专门策划并公开, 约 25,000 训练 + 5,000 测试图, 含 GNSS 元数据, 另含高分辨率层级。

## 5. 方法详解
### 整体框架
目标: 协同自主"装载-倾倒"作业 (Figure 2)。① **GCS**: ROS 地面控制站, 全局规划 (Voronoi+A\*)、任务分配、监控。② **地面车辆**: 自主挖掘机 + UGV, 执行航点导航。③ **边缘 AI 无人机**: STM32 六旋翼, 检测动态障碍物并发其全局位置给 GCS 做无碰撞规划。全系统 5G 互联, 车辆-GCS 间用 MQTT (经 `mqtt bridge` 与 ROS 集成)。

### 输入与输出
- **输入**: 无人机俯视单目 RGB 图像帧 (vision node 经串口送 MCU)。
- **AI 输出**: 障碍物/人员的类别 + 边界框。
- **系统输出**: 目标全局坐标, 作为动态障碍物供 GCS 避障。

### 关键模块与连接
1.  **无人机 (六旋翼)**：Pixhawk FCU、6 BLDC 电机、模块化碳纤维机架 (3D 打印原型), 续航 10–11 分钟, 视觉模块独立供电。机载: 通用机载计算机 (ROS Noetic + MAVROS + MQTT)、STM32F769i-Discovery MCU、5G 路由器、底座相机。机载计算机经串口发帧 → MCU 量化推理 → 回传预测, 借此隔离推理、降主机负载。
2.  **GCS 软件**：前后端分离。前端 React+Redux, 集成 Mapbox, 经 `roslibjs`/`mqtt bridge` 与 ROS 通信; 后端 ROS, 核心节点含 operation manager / vehicle agents / task planner (按就近分派) / path planner (Voronoi 图 + A\*), 遵循 VDA5050 协议保证 AGV 互操作。
3.  **边缘 AI 与数据**：
    - **量化部署**: 在 CPU / 树莓派 / STM32 上比较 ST-SSD、SSDv2、YoloLC、TinyYolo 等量化模型速度。
    - **坐标转换 (创新点)**: 单目俯视对 SfM 病态 → 改用"高度 + 目标像素尺寸"轻量法。RANSAC 在锥标场地学"每米对应像素数 vs 无人机高度", 得局部坐标; 再结合 GNSS 经测地变换得全局坐标, 整条管线在 MCU 上量化推理、保持实时不过载。
    - **TUBITAK-EdgeDrone**: 解决 MCU 低分辨率 + VisDrone 小目标问题; 约 3 万图, 含 GNSS 元数据, 双分辨率层级。

### 训练与推理流程
- **训练**: 通用机上用 TUBITAK-EdgeDrone + VisDrone 训多模型, 训后量化。
- **推理**: 相机捕帧 → 机载计算机经串口送 MCU → MCU 量化检测 → 回传 → 机载用高度+框尺寸经 RANSAC 估局部坐标、结合 GNSS 测地变换得全局坐标 → 经 5G/MQTT 发 GCS。

### 与已有方法的差异
不同于依赖高算力、或仅检查/规划用途 ([16][17]) 的方案, 也不同于常见边缘 AI+5G 无人机 ([18]), 本文用为低功耗 MCU 量化的轻量 AI 强调**实时作业协调**, 与地面车辆构成"感知→决策→执行"闭环。

## 6. 实验与结果
- **数据集**: 模型速度测试用 TUBITAK-EdgeDrone + VisDrone; RANSAC 用锥标场地数据; 现场测试在 OpenAirLab (TÜBİTAK Gebze, ~5000 ㎡ = 50×100 m, 配 WiFi/固态 LIDAR/IP 摄像头/5G)。
- **对比/指标**: 量化模型速度 (FPS, 跨 i7-8700/A72/M7); RANSAC 多项式精度 (RMSE cm); 系统层面定性可行性。未报检测 mAP。
- **主结果**:
    - **速度 (Table I)**: YoloLC-192 (339.3 KB) 在 M7 最快 **0.85 FPS** (i7 796.6 / A72 257.9); 最慢 TinyYolo-416 在 M7 仅 0.05 FPS。
    - **RANSAC (Table II)**: 三次多项式被选用, 8 m 处 RMSE **3.7 cm** (线性 3.2 / 二次 6.9 / 四次 2.7); 各高度看, 8 m 综合最优。
    - **最优高度 ≈ 8 m**: 低空重复检测同一锥标、高空锥标过小, 两端误差均升。
    - **现场**: 挖掘机+UGV 合计导航约 250 m, 无人机航测人员位置 → GCS 调整重型车路线。**因 MCU 0.85 FPS 不达实时, 现场实际用 A72 跑 AI。**
- **消融**: 无传统消融; RANSAC 阶数对比可视作参数研究。
- **泛化**: 仅单场地集成验证。

## 7. 这篇论文真正有价值的地方
1.  **端到端系统集成 demonstrator**: 价值不在单一模型, 而在把无人机感知、地面车辆执行、GCS 决策、5G/MQTT 通信、VDA5050/Voronoi+A\* 等组件组装成可运行闭环, 提供可复用的多机器人协同架构。
2.  **面向约束的工程取舍**: 正视 MCU 算力天花板, 用量化 + 专用低分辨率数据集 + RANSAC 高度反推距离 (替代重型 SfM/VIO) 来解题; 最终现场退化到 A72, 反而诚实暴露边缘 AI 的真实边界。
3.  **数据集贡献**: 公开 TUBITAK-EdgeDrone (低分辨率 + GNSS 元数据 + 双层级), 填补 VisDrone 在 MCU 小目标上的空白, 对无人机巡检边缘 AI 有实用价值。

## 8. 局限与问题
1.  **现场退化到 A72**: MCU (0.85 FPS) 不满足实时, 现场改用 A72 (257.9 FPS) 跑 AI, 削弱"完全在 MCU 实现"的论证。
2.  **精度未量化**: 只报 FPS, 无 mAP; 仅称高分辨率网络精度"略好但差异不显著"。
3.  **场景结构化**: 仅"装载-倾倒"单一循环, 复杂工地鲁棒性待验。
4.  **缺长期/可靠性数据**: 续航仅 10–11 分钟, 未测长期稳定性、通信中断、续航对作业时长影响。
5.  **位姿估计假设依赖**: RANSAC 依赖平稳高度与可控相机参数, 8 m 外/近地及姿态突变时误差上升。

## 9. 我该怎么使用这篇论文
- **快速了解**: Abstract + Introduction (贡献) + Methodology (架构) + Conclusion。
- **复现**: 精读 III.C/III.D + IV; 核心是 RANSAC 坐标转换与 STM32 量化部署 + 串口通信; 数据集见 github.com/egirgin/storaige-b950。
- **借鉴**: 多智能体架构 (GCS+5G+边缘 AI 车辆)、MCU 量化部署全流程、低分辨率小目标数据集构建。
- **写 Related Work**: 建筑机器人/自动化 · 无人机实时作业协调 · 边缘计算/AI 在机器人 · MCU 嵌入式深度学习部署。

## 10. 和其他论文的关系
- 与建筑机器人/移动操作机器人工作相关: Štibinger et al. 2021 (论文 [1])、Wu et al. 2022 综述 (论文 [10])。
- 与无人机在建筑的综述相关: Liang et al. 2023 (论文 [16])。
- 与自主挖掘机相关: Jin et al. 的 AES (论文 [14])——本文称其仅单机控制, 本文则集成多车型。
- 核心是边缘 AI 部署, 与更广的边缘计算/物联网研究相关。
- TUBITAK-EdgeDrone 数据集直接针对 VisDrone (Zhu et al. 2018, 论文 [19]) 在 MCU 上小目标占比不足的问题, 是其应用场景补充。

## 11. 关键词
边缘 AI, 建筑机器人, 无人机监控, 微控制器 (MCU/STM32), 目标检测, 模型量化, RANSAC 位姿估计, 实时系统, 多机器人协同, 5G/MQTT, VDA5050, 自主施工车辆, 数据集创建, 嵌入式系统

## 12. 可信度说明
本精读笔记**完全基于 PDF 提取文本** (共 4/4 页, 提取质量良好, 约 5244 字符/页)。信息来源覆盖 Abstract、I. Introduction、II. Related Work、III. Methodology、IV. Experiments、V. Conclusion 全部正文。Table I (FPS)、Table II (RMSE) 数据逐项与提取文本核对一致。"局限"部分中"现场改用 A72"为论文明确陈述, 其余局限为基于文本的合理推断。未在文本明确的信息 (检测 mAP、传统消融、其他工地泛化、机载计算机确切型号) 已标注"PDF 文本未明确"。本轮优化已修复原摘要乱码、补全数据集/代码/资助/场地/导航距离等细节, 并将分类由 T_通用_NLP_其他 修正为 R2_控制_生物启发_其他跨学科 (cs.RO 机器人系统/跨学科)。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 5244 字符/页, 4/4 页全覆盖); 来源缓存: `.paper-cache/extracts/2025_EdgeAI_Drone_for_Aut.txt`; 生成日期: 2026-06-05; 本轮人工对照优化: 2026-06-18; 模式: LLM (mimo-v2.5-pro) + 提取文本逐项核对。
<!-- AI_READING_NOTE_END -->
