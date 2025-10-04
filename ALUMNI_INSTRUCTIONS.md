# Alumni 模块使用说明

## 概述
已为 People 页面添加了全新的 Alumni（校友）模块，位于页面最底部，采用网格布局展示。

## 设计特点

### 布局
- **桌面端**：每行显示 5 人
- **中等屏幕**（1200px以下）：每行显示 4 人
- **小屏幕**（768px以下）：每行显示 3 人
- **移动端**（480px以下）：每行显示 2 人

### 样式
- **头像**：圆形头像（120px直径），带悬停效果
- **名字行**：显示姓名 + 在实验室的时间段（例如：John Doe (2020-2023)）
- **身份行**：显示当前身份/职位（例如：PhD Student）
- **学校行**：显示当前所在机构（例如：Stanford University）
- **字体大小**：较小字体（0.85rem 名字，0.65rem 身份和学校）确保信息不换行

## 如何添加 Alumni 成员

### 1. 在成员的 `_index.md` 文件中设置

在成员的个人信息文件中（`content/authors/[姓名]/_index.md`），添加或修改以下字段：

```yaml
# 用户组 - 改为 Alumni
user_groups:
  - Alumni

# 实验室开始时间（必填）
lab_start_date: "2020-09-01"

# 实验室结束时间（必填，用于计算 Duration）
lab_end_date: "2023-06-30"

# 当前身份/职位（必填，显示在名字下方第一行）
current_role: "PhD Student"

# 当前所在机构（必填，显示在名字下方第二行）
current_institution: "MIT"

# 其他字段保持不变
title: Zhang Wei
email: zhangwei@example.com
```

### 2. 必填字段说明

| 字段 | 说明 | 示例 |
|------|------|------|
| `user_groups` | 必须包含 "Alumni" | `- Alumni` |
| `lab_start_date` | 加入实验室的时间 | `"2020-09-01"` |
| `lab_end_date` | 离开实验室的时间 | `"2023-06-30"` |
| `current_role` | 当前身份/职位 | `"PhD Student"` |
| `current_institution` | 当前所在机构 | `"Stanford University"` |

### 3. 示例配置

```yaml
---
# Display name
title: Wei Zhang

# Full name (for SEO)
first_name: Wei
last_name: Zhang

# Username (this should match the folder name)
authors:
  - Wei-Zhang

# Is this the primary user of the site?
superuser: false

# Role/position
role: Former Research Assistant

# Organizations/Affiliations
organizations:
  - name: Peking University
    url: 'https://www.pku.edu.cn'

# Short bio (displayed in user profile at end of posts)
bio: Alumni of PKU Alignment Group

# Interests
interests:
  - Machine Learning
  - Natural Language Processing

# Education
education:
  courses:
    - course: BSc in Computer Science
      institution: Peking University
      year: 2023

# Social/Academic Networking
social:
  - icon: envelope
    icon_pack: fas
    link: 'mailto:zhangwei@example.com'
  - icon: github
    icon_pack: fab
    link: https://github.com/zhangwei

# 实验室时间信息
lab_start_date: "2020-09-01"
lab_end_date: "2023-06-30"

# 当前身份和机构
current_role: "PhD Student"
current_institution: "MIT"

# User groups - add Alumni
user_groups:
  - Alumni

# Highlight the author in author lists? (true/false)
highlight_name: false
---

Wei Zhang is a former research assistant at PKU Alignment Group.
```

## 时间格式

- `lab_start_date` 和 `lab_end_date` 使用 ISO 8601 格式：`"YYYY-MM-DD"`
- 显示格式会自动转换为：`2020-2023`（仅显示年份）

## 排序

Alumni 成员默认按照姓氏（`last_name`）字母顺序排列。

## 注意事项

1. **字体大小**：为了确保信息紧凑不换行，使用了较小的字体（0.85rem 名字，0.65rem 身份和学校）。如果文字过长，名字行会显示省略号（...）
2. **头像要求**：建议使用正方形头像图片，系统会自动裁剪为圆形
3. **信息分离**：`current_role` 和 `current_institution` 应该简洁明了，分别表示身份和机构
   - `current_role` 示例：`"PhD Student"`, `"Research Scientist"`, `"Assistant Professor"`
   - `current_institution` 示例：`"MIT"`, `"Stanford University"`, `"Google Research"`

## 文件结构

```
/layouts/partials/blocks/
├── people.html                    # 主文件，包含 Alumni 部分
└── people-alumni-card.html        # Alumni 卡片组件

/assets/scss/
└── template.scss                  # 样式文件，包含 Alumni 样式
```

## 效果预览

Alumni 模块会在 People 页面底部显示，具有以下特点：
- 清晰的 "Alumni" 标题
- 网格布局，整齐排列（桌面端每行5人）
- 圆形头像，视觉统一
- 三行信息显示：
  1. 名字 + 时间段（如：John Doe (2020-2023)）
  2. 身份（如：PhD Student）
  3. 机构（如：Stanford University）
- 小字体设计，信息紧凑
- 悬停时有轻微阴影效果
- 响应式设计，自适应不同屏幕尺寸

