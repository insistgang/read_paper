# 跟踪/视频/动作 (`K_跟踪_视频_动作`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 跟踪/视频/动作
- **代号**: `K_跟踪_视频_动作`
- **论文数**: 4
- **年份分布**: _(暂未提取到年份)_

## 论文列表 (按年份排序)

- ???? [[TransNet动作识别 TransNet HAR]]
- ???? [[cjig_图像处理_结合背景图的高分辨率视频人像实时抠图网络]]
- ???? [[单目标跟踪中的视觉智能评估技术综述]]  _R_综述_Survey_
- ???? [[扩散模型生成视频数据集及其检测基准研究]]

## 建议阅读顺序 (TODO: 人工)

> 入门 -> 核心 -> 进阶 -> 综述
>
> 命名规则: filename 通常含 `YYYY_关键词`, 可按年份递进。
> 调研时建议先看 Survey / 综述 (主题里带 `_综述` 或 `Survey`), 再读近 2 年的方法。

### 入门
- TODO: 从列表里选 2-3 篇 survey/intro
### 核心
- TODO: 选近 2 年的 SOTA 方法 3-5 篇
### 进阶
- TODO: 选 1-2 篇 method 复杂 / 有数学推导
### 综述
- TODO: 找主题里 _综述 标签的论文

## 关键问题 (TODO: 人工)

> 读了几篇后, 把这个主题下反复出现的核心科学问题列出来。

1.
2.
3.

## 方法分类 (TODO: 人工)

> 按方法族 (CNN / Transformer / Mamba / Diffusion / 等) 或任务范式分类。

- **CNN-based**:
- **Transformer-based**:
- **Mamba/SSM**:
- **其他**:

## 待精读清单

> 还没读但计划要读的论文 (按优先级)。

- [ ] (优先级高) TODO
- [ ] (优先级中) TODO
- [ ] (优先级低) TODO

## Dataview 查询示例

```dataview
TABLE year, primary_topic, status
FROM "02-Notes/Papers"
WHERE primary_topic = "K_跟踪_视频_动作"
SORT year DESC
```

如果想包含跨主题的论文 (topics 列表里有本主题代号的, 即多标签), 用 `contains`:

```dataview
TABLE year, primary_topic, status
FROM "02-Notes/Papers"
WHERE contains(topics, "K_跟踪_视频_动作")
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
