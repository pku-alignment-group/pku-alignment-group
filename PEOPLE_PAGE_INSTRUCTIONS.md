# People 页面更新说明

## 已完成的修改

### 1. 视觉改进
- ✅ **去掉背景框**：学生卡片不再有边框和背景色，直接融入页面
- ✅ **简洁排版**：左图右字布局，信息清晰展示
- ✅ **响应式设计**：适配桌面、平板和手机屏幕

### 2. 信息展示更新
每个学生现在显示以下信息：
- **姓名** (Name)
- **身份** (Role): Ph.D Student / Master Student / Research Intern / Others
- **加入时长** (Duration): 自动计算从 `lab_start_date` 到现在的时间
- **研究方向** (Research): 从 `interests` 字段获取
- **邮箱** (Email): 显示邮箱地址
- **研究使命** (Mission): 一句话描述（可选，最多20词）

### 3. 角色筛选功能
在老师和学生交界处添加了简洁的筛选按钮：
- **All**: 显示所有成员
- **Ph.D**: 只显示博士生
- **Master**: 只显示硕士生
- **Undergraduate**: 只显示本科生
- **Research Intern**: 只显示研究实习生
- **Others**: 显示其他角色

## 如何为学生添加研究使命

在学生的 `_index.md` 文件中添加 `research_mission` 字段：

```yaml
---
title: 学生姓名
role: Ph.D Student
lab_start_date: '2023-01-01'
interests:
  - Reinforcement Learning
  - AI Alignment

# 添加这一行（可选）
research_mission: "您的研究使命描述，建议不超过20个单词。"

email: 'student@example.com'
user_groups:
  - Group Members
---
```

## 示例

查看 `content/authors/Wenqi-Chen/_index.md` 文件，可以看到完整的配置示例。

## 角色识别规则

系统会自动识别以下角色类型：
- 包含 "Ph.D" 或 "PhD" → **Ph.D Student** (筛选器: phd)
- 包含 "Master" 或 "master" → **Master Student** (筛选器: master)
- 包含 "Undergraduate" 或 "undergraduate" → **Undergraduate Student** (筛选器: undergraduate)
- 包含 "Intern" 或 "intern" → **Research Intern** (筛选器: intern)
- 其他 → **Others** (筛选器: other)

## 时间计算

系统会自动根据 `lab_start_date` 和 `lab_end_date`（如果已设置）计算成员在实验室的时长：
- 如果 `lab_end_date` 未设置，则计算到当前时间
- 显示格式：`X year(s) Y month(s)` 或 `X month(s)`

## 文件修改列表

1. **layouts/partials/blocks/people.html** - HTML模板和JavaScript筛选逻辑
2. **assets/scss/template.scss** - 样式定义（去掉背景框，添加筛选器样式）
3. **content/authors/Wenqi-Chen/_index.md** - 示例文件（展示 research_mission 用法）

---

如有问题或需要调整，请随时修改配置文件。
