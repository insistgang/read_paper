# Dataview查询示例

## 📊 论文统计

### 所有论文列表

```dataview
TABLE year, venue, rating, status
FROM #paper
SORT date_added DESC
```

### 按状态分组

```dataview
TABLE length(rows) AS "数量"
FROM #paper
GROUP BY status
```

### 按年份统计

```dataview
TABLE length(rows) AS "论文数"
FROM #paper
GROUP BY year
SORT year DESC
```

### 按会议/期刊统计

```dataview
TABLE length(rows) AS "论文数"
FROM #paper
GROUP BY venue
SORT length(rows) DESC
```

## 📖 阅读进度

### 未读论文

```dataview
LIST
FROM #paper AND #unread
SORT file.ctime DESC
```

### 正在阅读

```dataview
LIST
FROM #paper AND #reading
SORT file.ctime DESC
```

### 已读论文

```dataview
LIST
FROM #paper AND #read
SORT date_added DESC
```

### 高评分论文

```dataview
TABLE year, venue, rating
FROM #paper AND rating >= 4
SORT rating DESC
```

## 🏷️ 标签分析

### 所有标签统计

```dataview
TABLE length(rows) AS "使用次数"
FROM ""
FLATTEN tags AS tag
GROUP BY tag
SORT length(rows) DESC
```

### 按研究方向分组

```dataview
TABLE length(rows) AS "论文数"
FROM #paper
FLATTEN tags AS tag
WHERE tag != "paper"
GROUP BY tag
SORT length(rows) DESC
```

## 📅 时间线

### 最近添加的论文

```dataview
TABLE year, venue, status
FROM #paper
SORT date_added DESC
LIMIT 10
```

### 本周添加的论文

```dataview
TABLE year, venue, status
FROM #paper
WHERE date(date_added) >= date(today) - dur(7 days)
SORT date_added DESC
```

## 🔍 高级查询

### 包含特定关键词的论文

```dataview
LIST
FROM #paper
WHERE contains(file.name, "transformer") OR contains(file.name, "attention")
```

### 有AI生成笔记的论文

```dataview
LIST
FROM #paper
WHERE file.content contains "AI生成的笔记"
```

### 待完善的论文笔记

```dataview
LIST
FROM #paper
WHERE file.content contains "TODO" OR file.content contains "待补充"
```

## 📈 可视化数据

### 论文阅读日历

```dataview
TABLE date_added AS "添加日期", file.name AS "论文"
FROM #paper
SORT date_added DESC
```

### 研究方向分布饼图数据

```dataview
TABLE length(rows) AS "数量"
FROM #paper
FLATTEN tags AS tag
WHERE tag != "paper" AND tag != "unread" AND tag != "read"
GROUP BY tag
SORT length(rows) DESC
LIMIT 10
```

## 🎯 任务管理

### 待办事项

```dataview
TASK
FROM #paper
WHERE !completed
GROUP BY file.link
```

### 已完成的任务

```dataview
TASK
FROM #paper
WHERE completed
GROUP BY file.link
```

## 📝 笔记质量检查

### 缺少作者信息的论文

```dataview
LIST
FROM #paper
WHERE !contains(file.content, "authors:") OR file.content contains "authors: \n  -"
```

### 缺少年份的论文

```dataview
LIST
FROM #paper
WHERE !contains(file.content, "year:") OR file.content contains "year: \n"
```

### 缺少评分的论文

```dataview
LIST
FROM #paper
WHERE !contains(file.content, "rating:") OR file.content contains "rating: \n"
```

## 🔗 关联分析

### 相互引用的论文

```dataview
TABLE file.inlinks AS "被引用", file.outlinks AS "引用"
FROM #paper
WHERE length(file.inlinks) > 0 OR length(file.outlinks) > 0
```

### 孤立论文（无关联）

```dataview
LIST
FROM #paper
WHERE length(file.inlinks) = 0 AND length(file.outlinks) = 0
```