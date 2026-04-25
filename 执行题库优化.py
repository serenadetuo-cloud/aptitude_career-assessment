#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
执行题库优化:删除重复题目,新增行为场景题,平衡维度分布
"""

import json

# 读取现有题库
with open('public/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. 删除重复/同质化题目
questions_to_remove = [6, 13, 15, 17, 22, 26, 28, 30]
original_count = len(data['questions'])
data['questions'] = [q for q in data['questions'] if q['questionId'] not in questions_to_remove]
print(f"✓ 删除了 {len(questions_to_remove)} 道重复题目")

# 2. 新增行为场景题
new_questions = [
    {
        "questionId": 36,
        "questionCategory": "行为场景 - 问题解决",
        "questionText": "项目遇到技术难题,你会怎么做?",
        "questionType": "single_choice",
        "options": [
            {
                "optionId": "A",
                "optionText": "自己研究文档、查资料,一定要搞懂原理",
                "scoring": {"科研创新": 5, "工程制造": 2}
            },
            {
                "optionId": "B",
                "optionText": "快速找个能用的方案,先解决问题再说",
                "scoring": {"商业服务": 3, "自主创业": 3}
            },
            {
                "optionId": "C",
                "optionText": "请教有经验的同事或老师,学习他们的思路",
                "scoring": {"教育培训": 4, "医疗健康": 3}
            },
            {
                "optionId": "D",
                "optionText": "动手实验,通过试错找到解决方案",
                "scoring": {"工程制造": 5, "科研创新": 2}
            }
        ]
    },
    {
        "questionId": 37,
        "questionCategory": "行为场景 - 冲突处理",
        "questionText": "团队成员对方案有分歧,你会?",
        "questionType": "single_choice",
        "options": [
            {
                "optionId": "A",
                "optionText": "用数据和逻辑分析各方案的优劣,理性决策",
                "scoring": {"科研创新": 4, "商业服务": 2}
            },
            {
                "optionId": "B",
                "optionText": "倾听各方意见,寻找能让大家都接受的折中方案",
                "scoring": {"教育培训": 5, "公共服务": 4}
            },
            {
                "optionId": "C",
                "optionText": "快速拍板决定,避免讨论浪费时间",
                "scoring": {"商业服务": 3, "自主创业": 4}
            },
            {
                "optionId": "D",
                "optionText": "做几个原型让大家试用,用实际效果说话",
                "scoring": {"工程制造": 4, "文化艺术": 3}
            }
        ]
    },
    {
        "questionId": 38,
        "questionCategory": "行为场景 - 学习新技能",
        "questionText": "需要快速学习一个新技能,你会?",
        "questionType": "single_choice",
        "options": [
            {
                "optionId": "A",
                "optionText": "系统学习理论基础,从原理开始理解",
                "scoring": {"科研创新": 5, "医疗健康": 4}
            },
            {
                "optionId": "B",
                "optionText": "直接上手做项目,在实践中边做边学",
                "scoring": {"工程制造": 5, "自主创业": 3}
            },
            {
                "optionId": "C",
                "optionText": "找个老师或课程,跟着学习路径走",
                "scoring": {"教育培训": 4, "商业服务": 1}
            },
            {
                "optionId": "D",
                "optionText": "看优秀案例,模仿和改进别人的作品",
                "scoring": {"文化艺术": 5, "商业服务": 2}
            }
        ]
    }
]

data['questions'].extend(new_questions)
print(f"✓ 新增了 {len(new_questions)} 道行为场景题")

# 3. 调整部分题目的分数权重,平衡维度分布
# 降低商业服务的普遍性,提高其他维度的权重
adjustments = {
    1: {  # 自由时间做什么
        "A": {"商业服务": 1, "自主创业": 1},  # 降低商业服务
        "B": {"医疗健康": 3, "教育培训": 3, "公共服务": 4},  # 提高公共服务
    },
    5: {  # 组织活动
        "A": {"商业服务": 2, "自主创业": 2},  # 降低
        "C": {"公共服务": 4, "教育培训": 2},  # 提高公共服务
    },
    8: {  # 晋升管理岗
        "A": {"商业服务": 2, "自主创业": 2},  # 降低
        "C": {"科研创新": 4, "工程制造": 3},  # 提高科研
    },
    32: {  # 实习偏好
        "B": {"医疗健康": 5, "科研创新": 5, "工程制造": 4},  # 强化专业门槛
        "D": {"商业服务": 2, "自主创业": 2},  # 降低
    },
    33: {  # 课外活动
        "C": {"医疗健康": 4, "教育培训": 5, "公共服务": 5},  # 强化专业门槛
    },
    34: {  # 毕业规划
        "A": {"科研创新": 6, "医疗健康": 5, "工程制造": 3},  # 强化专业门槛
        "C": {"公共服务": 6, "教育培训": 3},  # 强化专业门槛
    },
    35: {  # 课程偏好
        "E": {"医疗健康": 6},  # 强化医学专业门槛
    }
}

for q_id, options_adj in adjustments.items():
    question = next((q for q in data['questions'] if q['questionId'] == q_id), None)
    if question:
        for opt_id, new_scoring in options_adj.items():
            option = next((opt for opt in question['options'] if opt['optionId'] == opt_id), None)
            if option:
                option['scoring'] = new_scoring

print(f"✓ 调整了 {len(adjustments)} 道题目的分数权重")

# 4. 更新元数据
data['meta']['totalQuestions'] = len(data['questions'])
data['meta']['lastUpdated'] = "2026-04-25"

# 保存
with open('public/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！")
print(f"  原题目数: {original_count}")
print(f"  删除: {len(questions_to_remove)} 道")
print(f"  新增: {len(new_questions)} 道")
print(f"  最终题目数: {len(data['questions'])} 道")
