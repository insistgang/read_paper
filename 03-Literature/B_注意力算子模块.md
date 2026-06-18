# 注意力算子/模块 (`B_注意力算子模块`)

> 主题首页 / 索引页。包含这个主题下所有论文的入口, 建议阅读顺序, 关键问题, 方法分类。

## 主题定义

> TODO: 用 1-2 句话定义这个主题的范畴, 跟邻近主题的边界。

- **主题名**: 注意力算子/模块
- **代号**: `B_注意力算子模块`
- **论文数**: 80
- **年份分布**: 2024: 34, 2022: 14, 2023: 12, 2020: 9, 2018: 3, 2019: 3

## 论文列表 (按年份排序)

- 2006 [[ULSAM]]
- 2016 [[DWConv]]
- 2018 [[CBAM]]
- 2018 [[DA]]
- 2018 [[scSE]]
- 2019 [[CondConv]]
- 2019 [[SA]]
- 2019 [[dynamic_conv]]
- 2020 [[2020_Attention_Neural_Net]]
- 2020 [[DOConv]]
- 2020 [[GCTattention]]
- 2020 [[GhostModule]]
- 2020 [[PyConv]]
- 2020 [[SPConv]]
- 2020 [[cross_attention]]
- 2020 [[ffc]]
- 2020 [[rsablock3d]]
- 2021 [[LocalViT]]
- 2021 [[PAAblock]]
- 2021 [[axial]]
- 2022 [[Attention]]
- 2022 [[CCT]]
- 2022 [[ELAB]]
- 2022 [[FECAttention(时序预测)]]
- 2022 [[GhostModuleV2]]
- 2022 [[HAAM]]
- 2022 [[Inception_mixer]]
- 2022 [[MLA]]
- 2022 [[MSCA]]
- 2022 [[Parallel ViT]]
- 2022 [[TSConformerBlock]]
- 2022 [[TVConv]]
- 2022 [[WCMFandFACMA]]
- 2022 [[regionvit]]
- 2023 [[(GRN)ConvNeXtV2]]
- 2023 [[CLFT&UCDC]]
- 2023 [[CPCA]]
- 2023 [[DCA]]
- 2023 [[DLKA]]
- 2023 [[Dysample(上采样)]]
- 2023 [[GAB&GHPA]]
- 2023 [[HWD下采样]]
- 2023 [[IDC]]
- 2023 [[PConv]]
- 2023 [[RFAConv]]
- 2023 [[SwiftFormerEncoder&ConvEncoder]]
- 2024 [[(UIB)MobileNetV4]]
- 2024 [[AFF]]
- 2024 [[ASSA&FRFN]]
- 2024 [[CAFFN&MultiOrderGatedAggregation]]
- 2024 [[CAFM&MSFN&CAMixingBlock]]
- 2024 [[CPAM]]
- 2024 [[CRMSA]]
- 2024 [[DAB]]
- 2024 [[DSAM]]
- 2024 [[FADConv]]
- 2024 [[FEM&SCAM]]
- 2024 [[FMB]]
- 2024 [[FMS&MDAF]]
- 2024 [[FeatUp]]
- 2024 [[FreqFusion]]
- 2024 [[GAU]]
- 2024 [[GRSA]]
- 2024 [[GatedSlotAttention]]
- 2024 [[GlobalPMFSBlock]]
- 2024 [[LAE&MSFM&RFAConv]]
- 2024 [[LDConv]]
- 2024 [[MAB]]
- 2024 [[MATM&PS2A&MHIASA]]
- 2024 [[MLLA]]
- 2024 [[MSCB&MSACM&EUCB&LGAG]]
- 2024 [[RAMiT&HRAMi]]
- 2024 [[RCM&dpg_head]]
- 2024 [[SCSA]]
- 2024 [[SFFusion]]
- 2024 [[SHSA]]
- 2024 [[SLAB(prepbn&SLA)]]
- 2024 [[StarBlocks]]
- 2024 [[TSLANet(ICB&ASB)]]
- 2024 [[wtconv2d]]

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
WHERE primary_topic = "B_注意力算子模块"
SORT year DESC
```

如果想包含跨主题的论文 (topics 列表里有本主题代号的, 即多标签), 用 `contains`:

```dataview
TABLE year, primary_topic, status
FROM "02-Notes/Papers"
WHERE contains(topics, "B_注意力算子模块")
SORT year DESC
```

---

*此首页由 `scripts/generate_topic_index.py` 自动生成, TODO 段需要人工润色。*
