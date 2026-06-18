---
title: LINKAGE BETWEEN PIECEWISE CONSTANT MUMFORD-SHAH
authors:
  - "Xiaohao Cai"
  - "Raymond Chan"
  - "Carola-Bibiane Schönlieb"
  - "Gabriele Steidl"
  - "Tieyong Zeng"
year: 2019
venue: "arXiv"
doi: 
pdf: [[变分分割基础Mumford-Shah与ROF Mumford-Shah ROF.pdf]]
primary_topic: F_图像分割_语义_实例_全景
topics:
  - "F_图像分割_语义_实例_全景"
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
extract_cache: .paper-cache/extracts/变分分割基础Mumford-Shah与ROF Mumford-Shah ROF.txt
full_text_covered: true
full_text_completed_at: 2026-06-08
full_text_completion_basis: "AI supplemental pass; original AI block 12/31 pages"
---
# LINKAGE BETWEEN PIECEWISE CONSTANT MUMFORD-SHAH

## 基本信息
- **PDF**: [[变分分割基础Mumford-Shah与ROF Mumford-Shah ROF.pdf]]
- **primary_topic**: `F_图像分割_语义_实例_全景`
- **topics**: `F_图像分割_语义_实例_全景`
- **状态**: read (已提取 PDF 内容, 待人工复核)
- **date_added**: 2026-06-03

## 文章信息

| 项目 | 内容 |
|------|------|
| **题目** | Linkage between Piecewise Constant Mumford-Shah Model and ROF Model and Its Virtue in Image Segmentation |
| **作者** | Xiaohao Cai; Raymond Chan; Carola-Bibiane Schönlieb; Gabriele Steidl; Tieyong Zeng |
| **发表时间** | 2019 (arXiv:1807.10194v2, 15 Oct 2019; math.NA) |
| **刊物/会议** | arXiv 预印本 (会议简版见 [17]) |
| **DOI** | 未明确 |

## 摘要

清理后英文原摘要（据 PDF 提取文本，已修复空格断裂与丢失的连字符/ligature）：

> The piecewise constant Mumford-Shah (PCMS) model and the Rudin-Osher-Fatemi (ROF) model are two important variational models in image segmentation and image restoration, respectively. In this paper, we explore a linkage between these models. We prove that for the two-phase segmentation problem a partial minimizer of the PCMS model can be obtained by thresholding the minimizer of the ROF model. A similar linkage is still valid for multiphase segmentation under specific assumptions. Thus it opens a new segmentation paradigm: image segmentation can be done via image restoration plus thresholding. This new paradigm, which circumvents the innate non-convex property of the PCMS model, therefore improves the segmentation performance in both efficiency (much faster than state-of-the-art methods based on the PCMS model, particularly when the phase number is high) and effectiveness (producing segmentation results with better quality) due to the flexibility of the ROF model in tackling degraded images, such as noisy images, blurry images or images with information loss. As a by-product of the new paradigm, we derive a novel segmentation method, called thresholded-ROF (T-ROF) method, to illustrate the virtue of managing image segmentation through image restoration techniques. The convergence of the T-ROF method is proved, and elaborate experimental results and comparisons are presented.

中文翻译：

> 分段常数 Mumford-Shah（PCMS）模型与 Rudin-Osher-Fatemi（ROF）模型分别是图像分割和图像恢复中两个重要的变分模型。本文探索二者之间的联系：我们证明，对于两相分割问题，PCMS 模型的一个**偏最小解（partial minimizer）**可以通过对 ROF 模型的最小解做阈值化得到；在特定假设下，这一联系对多相分割依然成立。由此开启了一种新的分割范式——图像分割可以通过"图像恢复 + 阈值化"来完成。该范式规避了 PCMS 模型固有的非凸性，因而在**效率**（远快于基于 PCMS 模型的现有方法，尤其当相位数较高时）和**有效性**（分割质量更好）两方面都提升了分割性能，这得益于 ROF 模型在处理退化图像（含噪、模糊、信息缺失图像）上的灵活性。作为该范式的副产品，我们导出一种新的分割方法，称为**阈值化 ROF（T-ROF）方法**，以展示借助图像恢复技术来管理图像分割的价值。文中证明了 T-ROF 方法的收敛性，并给出了详尽的实验结果与对比。
>
> 关键词（原文 Key words）：图像分割, 图像恢复, Mumford-Shah 模型, 分段常数 Mumford-Shah 模型, Chan-Vese 模型, total variation ROF 模型, 阈值化。

> **来源**: 据 PDF 提取文本整理。

## 研究背景与动机

- **为什么要做**：PCMS 模型（非凸，Mumford-Shah 模型 [33] 的特例）与 ROF 模型（凸，[37]）分别是图像分割与图像恢复中最著名的两类变分模型。论文要建立二者之间的联系，从而打通"分割"与"恢复"两个研究方向，并催生更高效的分割方法。
- **之前方法的问题**：PCMS 模型（K=2 时即 Chan-Vese 模型 [25]）是**非凸**的，直接求解（如 [25] 的活动轮廓、[38] 的多相 level set）容易陷入局部极小；其凸松弛（如 [23, 36, 5/13/16/31/32/35/39/40] 等非紧松弛）虽缓解了非凸性，但求解多相分割时计算量随相位数 K 增大而显著上升。
- **核心矛盾 / 切入点**：作者此前的 SaT（Smoothing and Thresholding，[15]）方法已经经验性地展示了"先平滑再阈值化"可做分割（第一阶段是 ROF 泛函再加一个光滑项 ∫|∇u|² dx），且无需重解即可改变相位数 K。但 SaT 的阈值是用 K-means 启发式选的，缺乏理论支撑。本文要补上这块理论：用 ROF（凸、易解、对退化图像鲁棒）严格地刻画 PCMS（非凸、难优化）的解。

## 关键贡献

1.  **K=2 的理论联系（定理 3.6）**：设 u 是 ROF 模型的解，对给定 0<m0<m1≤1，取 ~Σ={x: u(x) > (m1+m0)/2}，则在 λ:=(μ/2)(m1−m0) 下 ~Σ 是固定均值 m0,m1 的 Chan-Vese 模型 (1.4) 的最小解；进一步若 m0=meanf(Ω\~Σ)、m1=meanf(~Σ)，则 (~Σ,m0,m1) 是 (1.4) 的偏最小解。
2.  **T-ROF 模型与 PCMS 的等价（定理 3.4）**：K=2 时，T-ROF 模型 (3.7)–(3.8) 的解 (Σ*₁, τ*₁) 是 PCMS / Chan-Vese 模型 (1.4) 在参数 λ=(μ/2)(m*₁−m*₀) 下的偏最小解。
3.  **推广到多相（定理 3.7）**：当 K>2 且相邻阈值区域边界不相交（∂Σ_i ∩ ∂Σ_{i+1}=∅）时，T-ROF 模型的解是一个 **PCMS-V 模型 (3.16)** 的偏最小解；PCMS-V 是 PCMS 的变体，其正则化参数 ~λ_i（按 (3.17)）随相邻区域均值差自适应，比标准 PCMS 的固定 λ 更灵活。
4.  **提出 T-ROF 方法与自动阈值**：基于上述联系导出 thresholded-ROF（T-ROF）方法，遵循"图像恢复 + 迭代阈值化"范式；阈值由 (4.1) 规则 τ_i=(m_{i−1}+m_i)/2 自动更新，无需 K-means。
5.  **收敛性证明**：证明了 T-ROF 阈值自动选择迭代算法（算法 4.x）的收敛性。
6.  **效率优势**：只需**求解一次 ROF 模型**，对同一个 u 反复施加不同阈值即可，计算成本与相位数 K 无关；相比之下基于 PCMS 的方法随 K 增大而变得计算昂贵。
7.  **有效性优势**：得益于 ROF 对退化图像（含噪、模糊、信息缺失）的灵活性，新范式分割质量更好；尤其当各相强度接近（m_i 差很小）时，自适应的 λ 让其优于固定 λ 的 PCMS（见 Remark 3.5、Remark 3.8）。

## 方法

- **整体框架（两步范式）**：(1) **图像恢复**：用 ROF 模型 (1.7) 对输入图像 f 去噪/平滑，得到分段平滑函数 u。(2) **迭代阈值化**：对同一个 u 施加一组有序阈值 τ_1<…<τ_{K−1}，并按区域均值规则自动更新阈值直到满足条件 (3.8)。
- **输入输出**：输入是（退化的）灰度图像 f: Ω→[0,1]，Ω⊂R² 为有界、Lipschitz 边界开集。输出是 K 个两两不交、并集为 Ω 的区域 {Ω*_i}，构成图像分割。
- **关键模型与模块**：
    1.  **ROF 求解模块**：求解 min_{u∈BV(Ω)} { TV(u) + (μ/2)∫_Ω (u−f)² dx }（μ>0），得去噪图像 u。
    2.  **阈值化分割模块**：由 Lemma 3.2，对 0<τ_1<…<τ_{K−1}<1 阈值得到**嵌套**集合 Σ_1⊇Σ_2⊇…⊇Σ_{K−1}（Σ_i={x: u(x)>τ_i}）；设 Σ_0:=Ω、Σ_K:=∅，则 Γ_i:=Σ_i\Σ_{i+1}（i=0,…,K−1）两两不交且并集为 Ω。
    3.  **阈值自动更新模块（4.1）**：在第 k 次迭代，按当前分割算各区域均值 m_i^{(k)}=meanf(Σ_i^{(k)}\Σ_{i+1}^{(k)})，再令 τ_i^{(k+1)}=½(m_{i−1}^{(k)}+m_i^{(k)})，记作 τ^{(k+1)}=Ψ(Σ^{(k)},τ^{(k)})，反复对**同一个 u** 阈值化直到收敛。
- **数学联系的核心（命题 3.1 / 3.3，定理 3.4 / 3.6）**：
    1.  对固定 τ∈(0,1)，考虑能量 E(Σ,τ):=Per(Σ;Ω)+μ∫_Σ(τ−f) dx（式 3.1）。**命题 3.1**：其最小解可由求解凸问题 u=argmin{ TV(u)+∫_Ω(τ−f)u dx } 后令 Σ={x: u(x)>τ} 得到。
    2.  **命题 3.3**（引自 [20, Prop. 2.6]）：Σ={x: u(x)>τ} 对**每个** τ∈(0,1) 都解 E(·,τ)，当且仅当 u 解 ROF 模型 (1.7)。这正是"解一次 ROF、对所有阈值通用"的理论依据。
    3.  **定理 3.4 / 3.6**：通过补常数项 C=∫_Ω(m0−f)² dx，可把 E(Σ,(m1+m0)/2)+C 配成 Per(Σ;Ω)+λ(∫_Σ(m1−f)²+∫_{Ω\Σ}(m0−f)²)，即 Chan-Vese 能量 (1.4)，其中 λ=(μ/2)(m1−m0)。故对 ROF 解阈值化 = 求 PCMS 的（偏）最小解。
- **与已有方法的差异**：
    1.  与直接解 PCMS 相比：T-ROF 规避非凸性，且计算复杂度不随 K 增大。
    2.  与作者自己的 SaT [15] 相比：T-ROF 的阈值选择是**自动且理论驱动**的（源于与 PCMS 的等价性 / Remark 3.5），而非 K-means 启发式；这使其在各相强度接近时更有效。论文也指出 T-ROF 可视作 SaT 的一个特例，但"自动最优选阈值"是 SaT 未覆盖的。

## 实验

> 说明：PDF 文本提取缓存仅覆盖 p.1–12（摘要/引言/记号/Linkages/T-ROF 算法开头），实验在原文第 5 节（约 p.16 起）。以下条目据"全文补读记录"中从 p.18–22 抓到的零散线索整理，**提取缓存未覆盖正文细节，数值待核**。

- **实验设置（据引言 §1 末）**：在多种合成图像与真实图像上验证 T-ROF，并与代表性分割方法 [32, 35, 39, 30, 15] 比较。
- **对比方法**：state-of-the-art 的基于 PCMS / 凸松弛的方法 [32, 35, 39, 30] 以及作者自己的 SaT [15]。
- **评价指标**：分割精度 **SA（segmentation accuracy）** 与计算时间 computation time（据原文 p.18–19 线索，提取缓存未覆盖，待核）。
- **主实验结果（线索，待核）**：
    - 结果汇总于 **Table 5.1 / Table 5.2**（据原文后续页，提取缓存未覆盖，待核）。
    - p.19 线索："computation time, and SA for each method is given in Table 5.1"；p.20 线索称 Table 5.1 的定量结果显示本方法效果好，"all the results are very good except the result of method [32]"。
    - p.22 线索：Table 5.2 中 [35, 30] 与 T-ROF 相比，T-ROF "the fastest"，并在某相位数（"with K=8"）下给出最佳结果（Fig. 5.6(o)）（据原文后续页，提取缓存未覆盖，待核）。
- **效率信息**：论文强调 T-ROF "much faster" 且计算成本 "independent of the required number of phases K"；具体运行时间数值在提取缓存中未覆盖，待核。

## 局限

1.  **多相等价性的限制**：当 K>2 且 ∂Σ_i ∩ ∂Σ_{i+1}≠∅（相邻阈值区域边界相交）时，T-ROF 与 PCMS（-V）模型的等价性不再严格成立，只能得到 PCMS 的一个近似。论文指出这种边界相交源于 ROF 解 u 的跳跃（这些跳跃是原图 f 跳跃的子集，见 [20, Theorem 5]）。作者明确说明：等价性的缺失**不**意味着 T-ROF 比 PCMS 差，实验中某些情形 T-ROF 反而更好（§3.2 末）。
2.  **几何假设较强**：多相联系（定理 3.7）依赖 int(Σ_i)⊃closure(Σ_{i+1}) 即内层区域被外层严格包含（从而 ∂Σ_i∩∂Σ_{i+1}=∅），限制了理论普适性。
3.  **参数依赖**：阈值虽自动更新，但 ROF 仍有关键参数 μ 需设定。定理 3.6/3.7 表明 T-ROF 隐式定义了 PCMS 中的 λ=(μ/2)(m_i−m_{i−1})，且 λ 会自适应相邻区域强度差（Remark 3.5/3.8）；但 μ 的选择仍直接影响去噪解 u 的质量。
4.  **求解的非平凡性**：满足 (3.7) 又满足均值条件 (3.8) 的 (Σ,τ) 不直接可得，需要第 4 节的迭代算法；且 T-ROF 解 (3.7)–(3.8) 不同于在全部可行 τ 上直接最小化 (3.10)（不对所有 τ 取最小，见 [17, Remark 1]）。

## 个人评论

这篇论文最值得学习的是**把一个非凸优化问题（PCMS 分割）通过严格的理论联系，转化为一个凸优化问题（ROF 恢复）+ 一步后处理（阈值化）**的思路。

1.  **问题转化的启示**："搭桥"式研究——在两个不同领域的著名模型之间建立深刻联系，从而为难解问题设计出又快又好的新解法。这种方法论本身比单个算法更有价值。
2.  **算法设计范式**："去噪 + 阈值化"简洁高效，关键在于命题 3.3 保证**只需解一次 ROF**、对所有阈值通用，因此改相位数 K 不必重解——这和需要逐次迭代能量最小化的传统分割形成鲜明对比。
3.  **理论支撑实践**：本文为作者早先的启发式 SaT [15] 补上了理论（偏最小化、模型等价、λ 的自适应解释），使"先平滑再阈值"从经验技巧上升为有依据的范式，也更易扩展。
4.  **可改进处**：核心定理依赖较强几何假设（区域严格嵌套），K>2 一般情形只能近似；如何量化并缩小这个 gap，作者自己也列为 future work，是值得跟进的方向。

### 使用建议

- **快速了解**：读**摘要**与**引言**第一、二段及"Our contribution"段，即可掌握核心思想（恢复+阈值 = 分割）与三条理论联系。
- **复现**：精读**第 3 节（Linkages）**与**第 4 节（T-ROF 算法及收敛性）**，重点是命题 3.1/3.3、定理 3.4/3.6/3.7 的证明，以及阈值更新规则 (4.1) 与收敛性。
- **借鉴创新点**：学习"把非凸分割与凸恢复建立理论联系"的方法论；可思考能否把"恢复+阈值"范式迁到其他模型或模态（RGB、高光谱）。
- **写 Related Work**：可归入**基于变分方法的图像分割**（特别是 Mumford-Shah 及其凸松弛）或**分割与恢复的交叉研究**。

## 相关论文与链接

> 用 `[[]]` 链接到其他论文笔记或主题首页：
> - [[F_图像分割_语义_实例_全景]]
> - [[论文知识库总览]]

---

#paper #read

<!-- AI_READING_NOTE_START -->
# 论文精读

## 1. 论文定位
这是一篇**图像处理 / 应用数学**方向的论文，属于**变分模型**在**图像分割**与**图像恢复**交叉处的理论工作（arXiv:1807.10194v2, math.NA, 2019）。它建立分段常数 Mumford-Shah（PCMS，用于分割）与 Rudin-Osher-Fatemi（ROF，用于恢复）两个经典变分模型之间的理论联系，并据此提出"恢复 + 阈值化"的高效分割新范式与 T-ROF 方法。归入"图像分割_语义_实例_全景"主题，因其落脚点是图像分割方法（虽为经典变分而非深度学习范式）。

## 2. 一句话总结
对 ROF 去噪解做简单阈值化，即可得到 PCMS / Chan-Vese 分割模型的（偏）最小解；于是"图像分割 = 图像恢复 + 阈值化"，且只需解一次 ROF、计算成本与相位数 K 无关。

## 3. 背景与问题
- **为什么要做**：PCMS（非凸）与 ROF（凸）分别是分割与恢复中最著名的变分模型；建立二者联系既有理论意义，又能把 ROF 的可解性与鲁棒性迁移到难解的分割问题上。
- **之前方法的问题**：PCMS（K=2 即 Chan-Vese [25]，多相用 level set [38]）非凸、易陷局部极小；其凸松弛 [23,36,…] 在多相时计算量随 K 上升。作者自己的 SaT [15]（先 ROF+光滑项平滑、再阈值）已证经验有效，但阈值用 K-means 选，缺理论。
- **核心矛盾**：如何用凸、易解、对退化图像鲁棒的 ROF，严格地刻画并求解非凸的 PCMS 分割。

## 4. 核心贡献
1.  **K=2：ROF↔PCMS（定理 3.6）**：u 解 ROF，~Σ={x:u(x)>(m1+m0)/2} 在 λ=(μ/2)(m1−m0) 下是固定均值 Chan-Vese (1.4) 的最小解；满足均值自洽则为偏最小解。
2.  **K=2：T-ROF↔PCMS（定理 3.4）**：T-ROF 模型 (3.7)–(3.8) 的解就是 PCMS (1.4) 在 λ=(μ/2)(m*₁−m*₀) 下的偏最小解。
3.  **K>2：T-ROF↔PCMS-V（定理 3.7）**：在 ∂Σ_i∩∂Σ_{i+1}=∅ 假设下，T-ROF 的解是 PCMS 变体 PCMS-V (3.16) 的偏最小解，正则化参数 ~λ_i 按 (3.17) 随相邻均值差自适应。
4.  **T-ROF 方法 + 自动阈值**：导出 thresholded-ROF 方法，阈值由 (4.1) τ_i=½(m_{i−1}+m_i) 自动更新，免 K-means。
5.  **收敛性证明**：证明阈值自动选择迭代的收敛性。
6.  **效率**：只解一次 ROF，对同一个 u 反复阈值；成本与 K 无关。
7.  **有效性**：ROF 对退化图像灵活，分割质量更好；相强度接近时自适应 λ 优于固定 λ 的 PCMS（Remark 3.5/3.8）。

## 5. 方法详解
- **两步范式**：(1) 解 ROF (1.7) 得分段平滑 u；(2) 对同一个 u 用一组自动更新的有序阈值做嵌套阈值化得分割。
- **输入输出**：输入退化灰度图 f:Ω→[0,1]（Ω⊂R² 有界 Lipschitz 开集）；输出 K 个两两不交、并为 Ω 的区域 {Ω*_i}。
- **关键模块**：
    1.  **ROF 求解**：min_{u∈BV(Ω)} TV(u)+(μ/2)∫(u−f)²。
    2.  **嵌套阈值化**：由 Lemma 3.2，阈值 τ 增大对应集合单调收缩，得 Σ_1⊇…⊇Σ_{K−1}；Σ_0=Ω,Σ_K=∅，Γ_i=Σ_i\Σ_{i+1} 给出分割。
    3.  **阈值更新 (4.1)**：m_i^{(k)}=meanf(Σ_i\Σ_{i+1})，τ_i^{(k+1)}=½(m_{i−1}^{(k)}+m_i^{(k)})。
- **数学联系链条**：
    1.  能量 E(Σ,τ)=Per(Σ;Ω)+μ∫_Σ(τ−f)dx（3.1）。**命题 3.1**：其解 = 解凸问题 u=argmin{TV(u)+∫(τ−f)u dx} 再阈值 Σ={u>τ}。
    2.  **命题 3.3**（[20]）：Σ={u>τ} 对所有 τ∈(0,1) 解 E(·,τ) ⇔ u 解 ROF (1.7) ⇒ 解一次 ROF 通用于所有阈值。
    3.  **定理 3.4/3.6**：补常数 C=∫(m0−f)² 后 E(Σ,(m1+m0)/2)+C 配成 Chan-Vese 能量 (1.4)，λ=(μ/2)(m1−m0)。
    4.  **多相 (3.15)–(3.20)**：在边界不交假设下，∑Per(Σ_i∪…∪Σ_{K−1};Ω)=½∑Per(Ω_i;Ω)，把逐分量极小化拼成 PCMS-V (3.16) 的偏最小解。
- **与已有方法差异**：相对直接解 PCMS——避非凸、成本不随 K 增；相对 SaT [15]——阈值自动且理论驱动而非 K-means，对相强度接近的退化图更有效。

## 6. 实验与结果
> PDF 文本提取缓存仅覆盖 p.1–12，实验在第 5 节（约 p.16 起），以下据"全文补读记录"零散线索整理，**数值未在提取缓存中出现，待核**。
- **设置**：合成图像 + 真实图像，与 [32, 35, 39, 30, 15] 比较（据 §1 末）。
- **指标**：分割精度 SA + 计算时间（据 p.18–19 线索，提取缓存未覆盖，待核）。
- **主结果**：汇总于 Table 5.1 / Table 5.2（据原文后续页，提取缓存未覆盖，待核）。p.20 线索：Table 5.1 定量结果显示本方法很好，"all the results are very good except the result of method [32]"；p.22 线索：Table 5.2 中 T-ROF 比 [35,30] 更快（"the fastest"），并在 K=8 时给出最佳结果（Fig. 5.6(o)）。
- **效率**："much faster" 且成本 "independent of K"；具体时间数值提取缓存未覆盖，待核。

## 7. 这篇论文真正有价值的地方
1.  **问题转化的启示**：在分割（PCMS）与恢复（ROF）两个经典模型间"搭桥"，把非凸难题转成"凸优化 + 后处理"。这种方法论可迁移。
2.  **算法设计范式**：命题 3.3 保证只解一次 ROF、阈值通用，改 K 不重解——天然的多相高效路线。
3.  **理论支撑实践**：为早先启发式 SaT [15] 补上偏最小化 / 模型等价 / λ 自适应的理论解释，使范式更可靠、可扩展。

## 8. 局限与问题
1.  **K>2 等价性**：∂Σ_i∩∂Σ_{i+1}≠∅（源于 ROF 解的跳跃，[20, Thm 5]）时等价性失效，只得近似；但作者强调这不代表 T-ROF 更差，实验中有时反而更好。
2.  **强几何假设**：定理 3.7 需 int(Σ_i)⊃closure(Σ_{i+1})（区域严格嵌套），普适性受限。
3.  **参数依赖**：λ 由 (μ/2)(m_i−m_{i−1}) 隐式自适应，但 μ 仍需手设，直接影响去噪解 u。
4.  **求解非平凡**：满足 (3.7)+(3.8) 的 (Σ,τ) 不直接可得，需第 4 节迭代；且不同于在所有可行 τ 上直接最小化 (3.10)。

## 9. 我该怎么使用这篇论文
- **快速了解**：摘要 + 引言一、二段 + "Our contribution"。
- **复现**：精读第 3 节（命题 3.1/3.3、定理 3.4/3.6/3.7）与第 4 节（阈值更新 4.1 + 收敛性）。
- **借鉴创新点**：把"恢复 + 阈值"范式迁到其他模型/模态（RGB、高光谱）。
- **写 Related Work**：归入"基于变分方法的图像分割（Mumford-Shah 及其凸松弛）"或"分割与恢复的交叉研究"。

## 10. 和其他论文的关系
- `[[Chan-Vese Model]]`：K=2 的 PCMS 即 Chan-Vese（Active Contours Without Edges）[25]。
- `[[Mumford-Shah Model]]`：核心模型，本文研究其分段常数特例 [33]。
- `[[ROF Model / Total Variation Denoising]]`：另一核心模型，Rudin-Osher-Fatemi 1992 [37]。
- `[[Ambrosio-Tortorelli Approximation]]`：早期求解 Mumford-Shah 的椭圆逼近 [3]。
- `[[Smoothing and Thresholding (SaT) Method]]`：作者前作 [15]，本文为其有效性提供理论支撑；扩展见 Poisson/Gamma 噪声 [22] 与彩色图像 [14]。
- `[[Convex Relaxation of Chan-Vese Model]]`：固定均值下 CV 模型的凸松弛与全局最优解 [23]（另见 [7,11,12,36]）。

## 11. 关键词
图像分割, 图像恢复, Mumford-Shah 模型, 分段常数 Mumford-Shah 模型, Chan-Vese 模型, ROF 模型, total variation, 阈值化, 变分模型, 非凸优化, 凸松弛, 偏最小化(partial minimizer)

## 12. 可信度说明
本精读笔记主要基于 PDF 提取文本（缓存覆盖 p.1–12：摘要、引言、记号、核心理论联系即 PCMS↔ROF↔T-ROF 的证明、T-ROF 算法与收敛性开头）。这部分内容详实，足以准确支撑对论文**核心思想、理论贡献、方法框架与数学链条**的理解；本轮已据提取文本核对并修正了 λ=(μ/2)(m1−m0)、命题/定理编号、嵌套阈值化结构、能量配方式等细节。
**信息缺失部分**（提取缓存 p.13–31 未覆盖，仅"全文补读记录"留有零散行级线索，相关数值均标注"待核"）：
1.  完整实验设置与结果（数据集、Table 5.1/5.2 的具体数字、图表）。
2.  T-ROF 收敛性证明的后半部分（p.13–16 的 nosc-sequence / 排序论证）。
3.  与各对比方法更细的定量比较。
4.  结论（第 6 节）的具体内容。
因此第 6 节实验内容多以线索 + "待核"呈现，遵循严格不编造原则。

---

> **可信度补充**: PDF 提取质量 = **high** (PDF 提取质量好 (2086 字符/页), 提取缓存覆盖 12/31 页正文 p.1-12); 来源缓存: `.paper-cache/extracts/变分分割基础Mumford-Shah与ROF Mumford-Shah ROF.txt` (缓存标注 12/31 页; 原 AI 主体 p.1-12 + 全文补读线索 p.13-31); 生成日期: 2026-06-05; 本轮据提取文本复核优化: 摘要去乱码重建 + 理论细节(λ 公式/定理编号/嵌套阈值)核对; 模式: LLM (mimo-v2.5-pro)。
## 全文补读记录

- **补读日期**: 2026-06-08
- **补读范围**: PDF p.13-31; 原 AI 主体覆盖 p.1-12, 本记录补足到 p.1-31。
- **提取情况**: 缺失页 19 页, 其中 19 页提取到可读文本。缺失页包含正文/附录内容, 其中约 2 页偏参考文献。
- **状态说明**: 这是 AI 全文覆盖补读, 不是人工精读复核；`human_reviewed` 仍应保持 `false`。

### 缺失页章节线索

- p.13: Sincej
- p.13: Hence, from the
- p.13: Hence, we can only have one of the following orderings:
- p.14: To prove the convergence of the sequence (
- p.14: Kdo not change
- p.14: Speci
- p.15: Therefore we obtain for a sequence v(k)
- p.15: Here is an example:
- p.15: Ifm(k)
- p.15: Here is an example of the sign changes of a nosc-sequence containing two sign blocks
- p.15: In particular, accompanying the proof in part 1, we obtain that, if the whole
- p.16: Then we deduce

### 缺失页关键摘录

- p.18: term for all the methods by judging the segmentation accuracy (SA) de
- p.18: result) with = 1, which clearly shows the e
- p.18: are 418 and 6 (simply represented as 418 (6) in Table 5.1),
- p.19: computation time, and SA for each method is given in Table 5.1. We can see that the
- p.20: nal result), respectively, which again clearly show the e
- p.20: get good results. The quantitative results given in Table 5.1 show that our method is
- p.20: see that all the results are very good except the result of method [32]. From Table
- p.22: in Table 5.2, from which we can see that methods [35, 30] and our T-ROF method
- p.22: the fastest compared with methods [35, 30]. Moreover, Table 5.2 shows clearly the
- p.22: cantly increases inevitably). From Table 5.2, we also see that
- p.22: that our T-ROF method gives the best result, see Fig. 5.6 (o) (with = 8). In detail,
- p.22: results as the result of our T-ROF method given in Fig. 5.6 (o). More speci
<!-- AI_READING_NOTE_END -->
