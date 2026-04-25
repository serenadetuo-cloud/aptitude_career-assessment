#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
优化题库：调整分数权重 + 新增5道题目
"""

import json

# 读取现有题库
with open('public/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 调整现有题目的分数权重
adjustments = {
    4: {  # Q4: 团队项目中，你更喜欢负责什么？
        "A": {"商业服务": 2, "自主创业": 2},  # 原：3, 2
        "B": {"商业服务": 1, "教育培训": 2, "医疗健康": 1}  # 原：2, 2
    },
    7: {  # Q7: 你更看重工作的什么？
        "A": {"科研创新": 4, "医疗健康": 4, "工程制造": 3},  # 原：3, 2, 2
        "E": {"商业服务": 3, "自主创业": 2}  # 原：2, 2
    },
    12: {  # Q12: 你对工作收入的期望？
        "A": {"商业服务": 3, "自主创业": 3},  # 原：3, 2
        "C": {"医疗健康": 4, "教育培训": 4, "公共服务": 4}  # 原：2, 2, 3
    }
}

# 应用调整
for q_id, options_adj in adjustments.items():
    question = next((q for q in data['questions'] if q['questionId'] == q_id), None)
    if question:
        for opt_id, new_scoring in options_adj.items():
            option = next((opt for opt in question['options'] if opt['optionId'] == opt_id), None)
            if option:
                option['scoring'] = new_scoring

# 新增5道题目
new_questions = [
    {
        "questionId": 31,
        "questionCategory": "专业门槛 - 学习周期",
        "questionText": "你能接受多久的专业学习和培训周期？",
        "questionType": "single_choice",
        "options": [
            {
                "optionId": "A",
                "optionText": "3-4年本科就够了，想快速工作",
                "scoring": {"商业服务": 2, "文化艺术": 2, "自主创业": 1}
            },
            {
                "optionId": "B",
                "optionText": "愿意读研深造2-3年，提升专业能力",
                "scoring": {"科研创新": 3, "工程制造": 2, "教育培训": 2}
            },
            {
                "optionId": "C",
                "optionText": "愿意本硕博连读7-10年，成为领域专家",
                "scoring": {"医疗健康": 5, "科研创新": 5, "教育培训": 3}
            },
            {
                "optionId": "D",
                "optionText": "边工作边学习就行，不想全职读书",
                "scoring": {"商业服务": 2, "自主创业": 2}
            }
        ]
    },
    {
        "questionId": 32,
        "questionCategory": "大学生场景 - 实习偏好",
        "questionText": "实习时，你更看重什么？",
        "questionType": "single_choice",
        "options": [
            {
                "optionId": "A",
                "optionText": "能快速上手，有成就感，看到成果",
                "scoring": {"商业服务": 2, "文化艺术": 2, "自主创业": 1}
            },
            {
                "optionId": "B",
                "optionText": "能学到扎实的专业技能，即使过程枯燥",
                "scoring": {"医疗健康": 4, "科研创新": 4, "工程制造": 3}
            },
            {
                "optionId": "C",
                "optionText": "工作氛围好，团队友善，导师负责",
                "scoring": {"教育培训": 2, "公共服务": 2, "医疗健康": 1}
            },
            {
                "optionId": "D",
                "optionText": "薪资待遇好，有转正机会",
                "scoring": {"商业服务": 3, "自主创业": 2}
            }
        ]
    },
    {
        "questionId": 33,
        "questionCategory": "大学生场景 - 课外活动",
        "questionText": "大学期间，你更愿意参加什么活动？",
        "questionType": "single_choice",
        "options": [
            {
                "optionId": "A",
                "optionText": "学科竞赛（ACM、数学建模、机器人大赛）",
                "scoring": {"科研创新": 4, "工程制造": 3}
            },
            {
                "optionId": "B",
                "optionText": "创业比赛、商业案例大赛、营销策划",
                "scoring": {"商业服务": 4, "自主创业": 3}
            },
            {
                "optionId": "C",
                "optionText": "志愿服务、支教活动、公益项目",
                "scoring": {"医疗健康": 3, "教育培训": 4, "公共服务": 4}
            },
            {
                "optionId": "D",
                "optionText": "艺术展览、文学社团、摄影协会",
                "scoring": {"文化艺术": 4}
            },
            {
                "optionId": "E",
                "optionText": "学生会、社团管理、活动组织",
                "scoring": {"商业服务": 2, "教育培训": 2, "公共服务": 2}
            }
        ]
    },
    {
        "questionId": 34,
        "questionCategory": "大学生场景 - 毕业规划",
        "questionText": "毕业后，你的首选规划是？",
        "questionType": "single_choice",
        "options": [
            {
                "optionId": "A",
                "optionText": "考研/读博，继续深造，做学术研究",
                "scoring": {"科研创新": 5, "医疗健康": 3, "工程制造": 2}
            },
            {
                "optionId": "B",
                "optionText": "直接工作，积累经验，快速成长",
                "scoring": {"商业服务": 3, "文化艺术": 2, "工程制造": 2}
            },
            {
                "optionId": "C",
                "optionText": "考公/考编，追求稳定和保障",
                "scoring": {"公共服务": 5, "教育培训": 2}
            },
            {
                "optionId": "D",
                "optionText": "创业/自由职业，做自己想做的事",
                "scoring": {"自主创业": 5, "文化艺术": 2}
            },
            {
                "optionId": "E",
                "optionText": "先工作几年，再根据情况决定",
                "scoring": {"商业服务": 2, "工程制造": 1}
            }
        ]
    },
    {
        "questionId": 35,
        "questionCategory": "专业门槛 - 课程偏好",
        "questionText": "如果让你选择一门选修课，你会选？",
        "questionType": "single_choice",
        "options": [
            {
                "optionId": "A",
                "optionText": "《Python数据分析》《机器学习入门》",
                "scoring": {"科研创新": 4, "工程制造": 2}
            },
            {
                "optionId": "B",
                "optionText": "《商业模式与创业》《市场营销》",
                "scoring": {"商业服务": 4, "自主创业": 3}
            },
            {
                "optionId": "C",
                "optionText": "《摄影艺术》《创意写作》《设计思维》",
                "scoring": {"文化艺术": 4}
            },
            {
                "optionId": "D",
                "optionText": "《心理咨询技巧》《教育学原理》",
                "scoring": {"教育培训": 4, "医疗健康": 2}
            },
            {
                "optionId": "E",
                "optionText": "《人体解剖学》《临床医学导论》",
                "scoring": {"医疗健康": 5}
            }
        ]
    }
]

# 添加新题目
data['questions'].extend(new_questions)

# 更新元数据
data['meta']['totalQuestions'] = len(data['questions'])
data['meta']['lastUpdated'] = "2026-04-25"

# 保存
with open('public/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ 题库优化完成！")
print(f"  - 调整了 {len(adjustments)} 道题目的分数权重")
print(f"  - 新增了 {len(new_questions)} 道题目")
print(f"  - 总题目数：{data['meta']['totalQuestions']}")
