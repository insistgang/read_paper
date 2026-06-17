---
title: Illegal Border Cross Detection and Warning System Using IR Sensor and Node MCU
authors:
  - "Afsana Tasnim"
  - "Shawan Shurid"
  - "AKM Bahalul Haque"
year: 2020
venue: International Journal of Information and Electronics Engineering, Vol. 10, No. 2, June 2020
doi: 10.18178/ijiee.2020.10.2.719
pdf: [[2020_Illegal_Border_Cross.pdf]]
primary_topic: T_安全_入侵检测
topics:
  - "T_安全_入侵检测"
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
ai_generated_at: 2026-06-04
extract_cache: .paper-cache/extracts/2020_Illegal_Border_Cross.txt
---

# Illegal Border Cross Detection and Warning System Using IR Sensor and Node MCU

## 基本信息
- **PDF**: [[2020_Illegal_Border_Cross.pdf]]
- **primary_topic**: `T_安全_入侵检测`
- **topics**: `T_安全_入侵检测`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Illegal Border Cross Detection and Warning System Using IR Sensor and Node MCU |
| **作者** | Afsana Tasnim; Shawan Shurid; AKM Bahalul Haque（North South University, Dhaka, Bangladesh） |
| **发表时间** | 2020 |
| **刊物/会议** | International Journal of Information and Electronics Engineering, Vol. 10, No. 2, June 2020 |
| **DOI** | 10.18178/ijiee.2020.10.2.719 |

## 摘要

> （清理后的英文原摘要）We often find illegal immigrants moving from one country to another. By means of land these illegal immigrants move over the fence, cut the border wires and move to the other part of the land. What do you think — our soldiers are not doing their job? It is not that, actually. It is very difficult to watch consistently over the border. Soldiers have a limited vision to check around the whole land mass. So for them we have come up with a solution: we have built a device that will sense the presence of an intruder (illegal immigrant). This device will be installed over the fences. When an intruder passes over the fence, this device will transmit the signal to the soldiers' smartphone app (BLYNK app). The soldier will be notified with the signal and, after receiving the signal, the soldier can switch on the alarm and the emergency lights via the app. By this, the soldiers in the camp will be alerted and can take their respective positions and arrest the intruder which was passing the border illegally. By this device we can alert the soldiers in the border to take more safety precautions to keep our country safe.
>
> **Index Terms**: Node MCU ESP32, infrared sensor, Blynk app.

> （中文翻译）我们常见非法移民在国与国之间迁移。他们通过陆路翻越围栏、剪断边境铁丝网，进入另一片土地。难道是士兵没有尽职吗？并非如此——持续不断地监视边境本身就极其困难，士兵的视野有限，无法覆盖整片土地。为此我们提出一个方案：制作一个能感知入侵者（非法移民）存在的装置，安装在围栏上。当入侵者翻越围栏时，该装置会把信号发送到士兵的智能手机 App（Blynk App）。士兵收到信号通知后，可通过 App 打开警报和应急灯。这样营地里的士兵就会被警示，可以各就各位、抓捕非法越境的入侵者。借助该装置，我们可以提醒边境士兵采取更多安全防范措施，保卫国家安全。
>
> **关键词**：Node MCU ESP32、红外传感器、Blynk App。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

*   **为什么要做**：论文以印度—孟加拉国边境为背景，指出边境与边境村庄长期面临安全威胁——其他部族越境进入、骚扰并劫掠平民。文中引用一项估计：2000 年印度境内非法孟加拉移民总数约达 1.5 crore（约 1500 万），且每年约有 3 lakhs（约 30 万）人越境进入；并称"每抓获 1 名非法入境者，就有 4 名成功越境"。由于孟加拉人与印度孟加拉族（Bengali）文化相近，容易冒充印度公民定居；从孟加拉到印度的偷渡是世界上最便宜的之一，一趟约 Rs.2000（约 30 美元，含"导游"费），伪造证件最低只需 Rs.200（约 3 美元）。即便有围栏（fence/boundary），对安全防护仍不够。
*   **核心矛盾**：士兵**人力监视的有限性**（视野有限、难以 24 小时全程值守）与**边境线漫长、越境行为隐蔽随机**之间的矛盾。作者主张用**电子化、自动化**手段补充人力，降低这类问题。
*   **之前方法的问题**（来自 Literature Review，逐条对应原文 II 节）：
    *   **监控摄像头（Security Cameras）**：可连续监控或录像回看，部分支持联网远程查看，但需要人力持续盯屏，部署/选型成本高（文中以家用监控为例展开）。
    *   **微波（Microwaves，Ref.[1] Yaskawa & M. Kim）**：红外传感器存在安全侵入问题、摄像机识别范围受限；微波若不阻断高强度能量精度会下降。该文用微波多径的时空特性 + 阵列波束成形提升检测概率。
    *   **GSM 短信报警（Ref.[2] R. Newlin Shebiah 等）**：把分类器接入流程，用动物数据库识别野生动物，识别到危险动物即通过 GSM 给农户发短信。缺点是难以覆盖广阔区域、不适合多目标/群体动物的跟踪。文中还引 Ref.[3]（Jyothsna & V. Prasad）介绍基于异常（Anomaly-based）的入侵识别思路。
    *   **击键分析（Keystroke，Ref.[4]）**：通过打字节奏认证用户、阻止入侵者访问系统；缺点是用户情绪波动会改变打字节奏导致登录失败。
    *   **动物检测（Ref.[5] Nidhi Daxini 等）**：基于 Viola-Jones 类算法做实时动物检测；若特征提取不当、训练集不足会出错。
    *   **人体入侵检测（Ref.[6]）**：用 IR 传感器 + Wi-Fi 模块（ESP-12e）+ Arduino Uno + ATmega328p + PIR + MQ135 气/烟感 + LM35 温度传感，通过 HTTP 把参数发到 IoT 平台（ubidots.com）触发报警。这是与本文**最接近的工作**，本文在其思路上做集成。
    *   **RFID（Ref.[7]）**：用无源 RFID 做门禁式数字安防，验证用户、记录登记日志；无源标签免电池、更轻更便宜。
    *   **停车系统（Ref.[8]）**：用 NodeMCU + IR 传感器 + LED 检测停车位空闲，经 Arduino IDE 把数据传到 Firebase 云、手机 App 远程查看。本文明确表示从该文学到了**IR 传感器 + NodeMCU + 云服务器**的组合用法。

## 关键贡献

> 说明：本文是工程/教学性原型论文，"贡献"以系统集成与功能演示为主，并非算法创新。以下据 III/IV 节归纳：
1.  **提出并搭建了一套端-云-用的边境入侵检测与告警系统原型**：IR 传感器 + NodeMCU ESP32 + Wi-Fi + Blynk 云服务器 + Blynk 智能手机 App，形成"检测→上云→推送→现场告警"的闭环。
2.  **基于阈值比较的越境检测逻辑**：入侵者遮挡/进入 IR 传感器检测范围时改变信号，NodeMCU 在 Arduino IDE 代码中将读数与设定范围比较，判定是否为有效入侵（原文 Fig.18、19 给出部分执行代码）。
3.  **云端中转与移动端实时推送**：NodeMCU 经 Wi-Fi 向 Blynk 云发 HTTP 请求，云端把通知推送到绑定的手机 App（Fig.11 展示通知弹窗）。
4.  **远程声光告警控制**：士兵在 App 中按下虚拟按钮即可远程开启现场蜂鸣器（Buzzer）与 LED 应急灯（Fig.12 展示 Buzzer 开关界面）。
5.  **强调低成本与易原型化**：使用常见廉价元件（NodeMCU、IR 传感器、Buzzer、LED、面包板、导线），结论称系统"成本高效、士兵易用"。

## 方法

*   **整体框架（III. METHODOLOGY，Fig.6 系统流程图）**：IR 传感器检测到变化→给 NodeMCU 信号→NodeMCU 把信号送到 Blynk 云→云端处理后传给 Android App→App 收到通知，并触发蜂鸣器与灯。这是典型"端-云-用"IoT 架构：**传感端**（IR+NodeMCU）感知采集，**云处理端**（Blynk 云）中转/存储/推送，**用户端**（Blynk App）接收通知与下发控制。
*   **输入输出**：
    *   **输入**：IR 传感器信号，经 NodeMCU 的 **A0 模拟引脚**读取（IR 检测范围约 2 cm–30 cm）。
    *   **输出**：(1) 手机 App 弹出入侵告警通知；(2) 现场蜂鸣器 + LED 灯被远程开启。
*   **关键模块**：
    1.  **红外（IR）传感器模块**：含 IR 发射管（transmitter）与接收管（receiver）。物体进入约 2–30 cm 范围时，红外光遇障碍被提前反射，接收信号发生变化（Fig.13 框图、Fig.14 人体遮挡示意）。注：原文在 IV 节材料部分又把它描述为"passive Infrared sensor（被动红外）"，与"发射+接收"的主动式描述存在自相矛盾——PDF 文本未澄清这一矛盾。
    2.  **NodeMCU 微控制器模块**：核心处理单元。材料部分声明用 **Node MCU ESP-32S（基于 ESP-WROOM-32、ESP32 芯片，集成 Wi-Fi/蓝牙/以太网/低功耗）**；但正文多处又写成 **esp8266 / ESP-12**——同一篇论文里 ESP32 与 ESP8266 表述混用，PDF 文本未统一。其 IO 电平 3.3V–5V，经 Arduino IDE 编程，把读数与范围比较后用 HTTP 请求发往 Blynk 云。
    3.  **Blynk 云服务器 + 移动 App 模块**：NodeMCU 始终经 Wi-Fi 连云并可发 HTTP 请求；通知存入服务器数据库与通知中心，更新后推送给用户 App；App 既显示通知，又提供虚拟按钮控制 NodeMCU 所连的物理设备（Buzzer、LED）。原文提到数据"按 NFS/CIFS 分类、存 Google 云 / 数据中心"以及"FCM 转发消息"等表述（Fig.15–17），但这些与 Blynk 自有云的关系叙述混乱，PDF 文本未理清。
*   **电路连接（Fig.9、10）**：
    *   电路一：NodeMCU 的 **D1 引脚** 接 Buzzer 与 LED 灯的 GND；
    *   电路二：IR 传感器接 NodeMCU 的 **3V、GND、A0（模拟）** 引脚。
*   **工作流程（III.A Layout + 文中场景描述）**：初始化连云认证→入侵者遮挡 IR 信号传输→NodeMCU 经 Wi-Fi 把信号送 Blynk 云→云推送通知到士兵手机→士兵在 App 点按打开 Buzzer/灯→现场声光告警，士兵赶赴现场处置。
*   **与已有方法的差异**：与综述中各方法相比，本系统**面向开放边境的线性周界**（而非封闭门禁或网络入侵），并把"检测—通知—远程现场告警"串成完整链条；明确借鉴了 Ref.[6]（人体入侵检测）与 Ref.[8]（IR+NodeMCU+云）的工程套路并加以集成。

## 实验

*   **使用的数据集**：论文**未使用任何公开/自建标准数据集**做性能评估；"实验"即原型搭建与功能演示。
*   **对比方法**：**未做系统性定量对比**。综述介绍了摄像头/微波/GSM 等技术，但未与本系统量化比较。
*   **评价指标**：**未报告任何定量指标**（无检测率、召回、误报率、响应时延、检测距离的实测数据）。
*   **主实验结果（定性）**：
    *   **系统流程/功能图**（Fig.6、8）：描述传感器→手机通知的数据流与各设备。
    *   **电路连接图**（Fig.9、10）：展示 D1→Buzzer/LED、A0→IR 的接线。
    *   **代码片段**（Fig.18、19）：含库引入、App 鉴权、按范围比较读数的部分执行代码。
    *   **界面/工作截图**（Fig.11、12、20）：手机收到"Motion detected"通知、Blynk App 中 Buzzer 开关状态、开关打开后系统工作。原文称"代码执行并正确搭建后系统工作正常"。
*   **消融/泛化实验**：**PDF 文本中未找到**。
*   **效率信息**：**未报告**功耗、成本（仅定性称"成本高效"）、检测延迟等数据。
*   **未来工作（III.B Discussion 末尾）**：拟加摄像头、用超声波传感器替代 IR 以扩大检测范围、用 Raspberry Pi 3 B+ 提升服务器请求速度、改进 Web/App 界面与数据库。

## 局限

*   **技术局限**：
    *   **传感器性能**：IR 检测范围仅 2–30 cm，对边境周界而言极短；易受天气与环境光干扰，误报/漏报风险高。
    *   **硬件表述自相矛盾**：ESP32 与 ESP8266、主动 IR 与"被动 IR"、Blynk 云与 Google 云/FCM 等描述前后不一致，反映工程严谨性不足。
    *   **功能单一**：仅能判断"有无遮挡"，无法区分人/动物/其他物体，也无法估计数量、速度或意图。
    *   **鲁棒性**：未处理网络不稳、断电、被遮挡绕过等异常。
*   **实验与评估不足**：无定量评估（检测率/误报率等）；仅演示基本功能，未考虑复杂地形、多传感器协同、大规模部署。
*   **假设与风险**：依赖士兵始终在线并及时响应 App；未讨论通信加密/设备认证等安全性，易被干扰或攻击；把"功能演示"等同于"问题解决"，实际边境环境远比演示复杂。

## 个人评论

本文价值不在算法创新，而在于提供了一个**问题驱动 + 现成 IoT 平台快速集成**的完整工程/教学案例：把 IR 传感器、NodeMCU、Blynk 云与手机 App 串成"检测—推送—远程声光告警"闭环。
*   **对做项目/原型开发的启发**：清晰展示了小型 IoT 安防原型的硬件选型（NodeMCU + IR + Buzzer/LED）、平台选择（Blynk 低代码 IoT）、电路接线（A0 读 IR、D1 驱动告警）与端到端流程，实践参考价值高。
*   **可借鉴的点**：用 Blynk 这类低代码平台快速打通"设备—云—App"；同时设计现场（蜂鸣器）与远程（手机）两种响应。
*   **需警惕之处**：论文的术语混乱（ESP32/ESP8266、主动/被动 IR、Blynk/Google/FCM）和缺乏定量评估，是引用时要明确标注的硬伤；2–30 cm 的 IR 用于真实边境周界并不现实，更接近"概念演示"而非可部署方案。

### 使用建议

*   **如果快速了解**：读**摘要**与**引言（I. INTRODUCTION）**即可掌握问题与整体方案。
*   **如果复现**：读 **III. METHODOLOGY** 与 **IV. MATERIALS AND METHODS**，重点看系统流程图（Fig.6）、电路图（Fig.9/10）与代码片段（Fig.18/19）。
*   **如果借鉴创新点**：学其**系统集成思路**，并考虑用更强传感器（超声波/毫米波雷达、摄像头+边缘 AI）替换 2–30 cm 的 IR。
*   **如果写 related work**：归入**物联网在周界安防/入侵检测中的应用**，作为"基础传感器 + 现成云平台"的早期/教学性案例引用。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[T_安全_入侵检测]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
本文属于**物联网（IoT）/嵌入式传感系统在周界安防与入侵检测中的应用研究**，聚焦**边境非法越境检测与告警**。技术路线是 **IR 红外传感器 + NodeMCU（声明 ESP32，正文混用 ESP8266）+ Blynk 云 + 智能手机 App** 的低成本自动化方案，核心是"检测—上云—推送—远程声光告警"的系统设计，**不涉及任何深度学习视觉目标检测**。因此其归类应为 **T_安全_入侵检测**，而非计算机视觉的目标检测主题（原 C2 归类与论文实质不符，本次已修正）。

## 2. 一句话总结
论文设计并搭建了一个基于红外传感器与 Blynk 物联网平台的低成本边境越境检测与实时告警原型系统，入侵者遮挡 IR 信号即触发手机推送，士兵可远程开启现场蜂鸣器与应急灯。

## 3. 背景与问题
*   **为什么要做**：以印度—孟加拉边境为背景，士兵难以 24 小时全覆盖监视，视野有限；非法越境频发。文中数据：2000 年印度境内非法孟加拉移民总数估约 **1.5 crore（约 1500 万）**，每年约 **3 lakhs（约 30 万）** 越境，"每抓 1 人有 4 人漏网"；偷渡一趟约 **Rs.2000（约 30 美元）**，伪造证件最低 **Rs.200（约 3 美元）**。围栏不足以保障安全，故主张电子化/自动化补充人力。
*   **之前方法及问题**（II 节文献综述，逐条对应）：摄像头（需人盯屏、成本高）、微波 Ref.[1]（精度依赖高强度能量）、GSM 动物报警 Ref.[2]（难覆盖广域、不适合多目标）、异常检测 Ref.[3]、击键认证 Ref.[4]（情绪影响节奏）、Viola-Jones 动物检测 Ref.[5]（依赖特征提取与训练集）、人体入侵检测 Ref.[6]（IR+PIR+ESP-12e+ATmega328p+气/温传感+ubidots，**与本文最接近**）、无源 RFID 门禁 Ref.[7]、IR+NodeMCU+Firebase 停车系统 Ref.[8]（**本文直接借鉴其 IR+NodeMCU+云组合**）。
*   **核心矛盾**：人力监视有限 vs. 边境漫长、越境隐蔽随机；需低成本、易部署、能自动检测并实时报警的手段。

## 4. 核心贡献
工程/教学性贡献，非算法创新：(1) 搭建端-云-用的越境检测告警原型（IR+NodeMCU ESP32+Wi-Fi+Blynk 云+手机 App）；(2) 基于阈值/范围比较的越境判定逻辑（Fig.18/19 部分代码）；(3) 云端中转 + 移动端实时推送（Fig.11 通知）；(4) 远程声光告警控制（App 按钮开 Buzzer/LED，Fig.12）；(5) 强调低成本、易原型化（结论称"成本高效、易用"）。

## 5. 方法详解
*   **整体框架（Fig.6）**：IR 检测变化→NodeMCU→Blynk 云处理→Android App 收通知→触发蜂鸣器与灯。端-云-用三段式 IoT 架构。
*   **输入输出**：输入为 IR 信号经 NodeMCU **A0 模拟引脚**读取（检测范围约 **2 cm–30 cm**）；输出为手机 App 入侵通知 + 现场 Buzzer/LED 被远程开启。
*   **关键模块**：
    1.  **IR 传感器**：含发射管与接收管，物体进入 2–30 cm 时红外光遇障提前反射、信号变化（Fig.13/14）。注：IV 节又称其为"passive Infrared sensor（被动红外）"，与主动式发射+接收描述自相矛盾，PDF 文本未澄清。
    2.  **NodeMCU**：材料声明 **Node MCU ESP-32S（ESP-WROOM-32/ESP32，集成 Wi-Fi/蓝牙/以太网/低功耗）**，但正文多处写 **esp8266/ESP-12**，全文 ESP32 与 ESP8266 混用；IO 电平 3.3–5V，Arduino IDE 编程，按范围比较读数后用 HTTP 发往 Blynk 云。
    3.  **Blynk 云 + App**：NodeMCU 经 Wi-Fi 长连并发 HTTP；通知入库与通知中心更新后推送 App；App 显示通知并提供虚拟按钮控制物理设备。原文夹杂 NFS/CIFS、Google 云、FCM 等表述（Fig.15–17），与 Blynk 自有云关系叙述混乱，PDF 文本未理清。
*   **电路（Fig.9/10）**：D1→Buzzer/LED 的 GND；IR→3V/GND/A0。
*   **工作流程**：初始化连云认证→入侵者遮挡 IR→NodeMCU 经 Wi-Fi 送 Blynk 云→云推送手机→士兵 App 点按开 Buzzer/灯→现场声光告警并赶赴处置。
*   **与已有方法差异**：面向开放边境线性周界（非门禁/网络入侵），把"检测—通知—远程现场告警"串成完整链条，并集成 Ref.[6]/Ref.[8] 的工程套路。

## 6. 实验与结果
*   **数据集**：**未使用任何标准数据集**；"实验"为原型搭建与功能演示。
*   **对比方法**：**未做定量对比**（综述介绍他法但未量化比较）。
*   **评价指标**：**未报告任何定量指标**（无检测率/召回/误报率/时延/检测距离实测）。
*   **主结果（定性）**：系统流程/功能图（Fig.6/8）、电路图（Fig.9/10）、代码片段（Fig.18/19，含库引入/鉴权/按范围比较）、界面与工作截图（Fig.11 "Motion detected" 通知、Fig.12 Buzzer 开关、Fig.20 开关打开后工作）。原文称"代码执行并正确搭建后系统工作正常"。
*   **消融/泛化**：**PDF 文本中未找到**。
*   **效率**：**未报告**功耗/成本/时延（仅定性称成本高效）。
*   **未来工作**：加摄像头、用超声波替代 IR 扩大范围、用 Raspberry Pi 3 B+ 加速服务器请求、改进 Web/App 与数据库。

## 7. 这篇论文真正有价值的地方
价值在于一个**问题驱动 + 现成 IoT 平台快速集成**的完整工程/教学案例，而非算法。它把传感器、微控制器、云服务、移动 App 串成可演示的安防闭环，并兼顾现场（蜂鸣器）与远程（手机）两种响应——对初学者搭建小型 IoT 安防原型的硬件选型、平台选择、电路接线与端到端流程有直接参考价值。

## 8. 局限与问题
*   **技术局限**：IR 检测范围仅 2–30 cm，对真实周界过短、易受天气/环境光干扰，误报漏报风险高；硬件与云的表述自相矛盾（ESP32/ESP8266、主动/被动 IR、Blynk/Google/FCM），严谨性不足；功能单一（仅判"有无遮挡"，不能识别目标类别/数量/速度/意图）；未处理网络不稳/断电/绕过等异常。
*   **评估不足**：无定量评估，仅演示基本功能，未考虑复杂地形、多传感器协同与大规模部署。
*   **假设与风险**：依赖士兵始终在线并及时响应；未讨论通信加密/设备认证等安全性，易被干扰攻击；把"功能演示"等同于"问题解决"。

## 9. 我该怎么使用这篇论文
*   **快速了解**：读摘要 + 引言（I）。
*   **复现**：读 III. METHODOLOGY 与 IV. MATERIALS AND METHODS，重点看 Fig.6 流程图、Fig.9/10 电路图、Fig.18/19 代码片段。
*   **借鉴创新点**：学其系统集成思路；考虑用超声波/毫米波雷达或摄像头+边缘 AI 替换 2–30 cm 的 IR。
*   **写 related work**：归入"物联网在周界安防/入侵检测中的应用"，作为基础传感器 + 现成云平台的早期/教学性案例引用。

## 10. 和其他论文的关系
*   与 II 节综述各文同属"安防/入侵检测"谱系：摄像头、微波 Ref.[1]、GSM 动物报警 Ref.[2]、异常检测 Ref.[3]、击键认证 Ref.[4]、动物检测 Ref.[5]、人体入侵检测 Ref.[6]、RFID 门禁 Ref.[7]、IR+NodeMCU 停车 Ref.[8]——本文尤以 Ref.[6]、Ref.[8] 为直接工程参照。
*   与基于深度学习视觉的行人/车辆检测论文目标相近（保障边境/敏感区安全），但技术路径完全不同，本文不含视觉/深度学习成分。
*   与无线传感器网络（WSN）在环境监测/安防中的应用、以及其他基于 IoT 的智能安防系统论文相关。

## 11. 关键词
非法越境检测，边境安全，入侵检测，红外（IR）传感器，NodeMCU ESP32，物联网（IoT），Blynk，远程告警，嵌入式系统，无线传感器网络

## 12. 可信度说明
本精读笔记**完全基于 PDF 提取文本（8/8 页，约 30730 字符，节选前 25000 字符可读）生成**。提取质量整体较好，但论文原文本身存在多处自相矛盾（ESP32 与 ESP8266 混用、IR 主动/被动描述冲突、Blynk 云与 Google 云/FCM 叙述混乱）以及大量机翻式英文表述——这些已在笔记中明确标注为论文自身问题，而非提取错误。论文**缺乏任何定量实验**，故"实验与结果"中对未提及项均标注"未提及/未报告/未找到"。结论（V）与利益冲突段落在提取文本中被截断（原文称作者之一提议使用 Raspberry Pi），但不影响对核心系统的理解。**重要更正**：原笔记题目误用了期刊名、作者漏列 AKM Bahalul Haque、主题误归为 C2 目标检测；本次据提取文本已修正题目/venue/作者，并将 primary_topic 改为更贴切的 T_安全_入侵检测。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好, 8/8 页, 约 3130 字符/页); 来源缓存: `.paper-cache/extracts/2020_Illegal_Border_Cross.txt`; 生成日期: 2026-06-04; 模式: LLM (mimo-v2.5-pro); 本轮深度重读据提取文本核对并修正题目/作者/venue/分类。
<!-- AI_READING_NOTE_END -->
