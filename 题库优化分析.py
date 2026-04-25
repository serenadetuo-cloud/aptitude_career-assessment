#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
题库优化方案:删除重复题目,增加行为场景题,平衡维度分布
"""

import json

# 读取现有题库
with open('public/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('题库优化分析')
print('='*60)

# 要删除的题目(重复/同质化)
questions_to_remove = [
    6,   # "你更喜欢什么样的工作环境？" - 与Q22重复
    13,  # "你更看重工作的什么？" - 与Q7重复
    15,  # "你更喜欢什么样的工作方式？" - 太宽泛
    17,  # "你更喜欢什么样的学习方式？" - 不够关键
    22,  # "你更喜欢在什么环境工作？" - 与Q6重复
    26,  # "你对工作时间的期望？" - 不够关键
    28,  # "你对职业转换的态度？" - 不够关键
    30,  # "你理想的工作状态是？" - 太宽泛
]

print(f'计划删除 {len(questions_to_remove)} 道重复/同质化题目:')
for q_id in questions_to_remove:
    q = next((q for q in data['questions'] if q['questionId'] == q_id), None)
    if q:
        print(f'  Q{q_id}: {q["questionText"]}')

print(f'\n优化后题目数: {len(data["questions"]) - len(questions_to_remove)} 道')

# 需要新增的行为场景题
new_behavior_questions = [
    {
        "questionId": 36,
        "questionCategory": "行为场景 - 问题解决",
        "questionText": "项目遇到技术难题,你会怎么做?",
        "questionType": "single_choice",
        "options": [
            {
                "optionId": "A",
                "optionText": "自己研究文档、查资料,一定要搞懂原理",
                "scoring": {"科研创新": 4, "工程制造": 2}
            },
            {
                "optionId": "B",
                "optionText": "快速找个能用的方案,先解决问题再说",
                "scoring": {"商业服务": 3, "自主创业": 2}
            },
            {
                "optionId": "C",
                "optionText": "请教有经验的同事或老师,学习他们的思路",
                "scoring": {"教育培训": 3, "医疗健康": 2}
            },
            {
                "optionId": "D",
                "optionText": "动手实验,通过试错找到解决方案",
                "scoring": {"工程制造": 4, "科研创新": 2}
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
                "scoring": {"科研创新": 3, "商业服务": 2}
            },
            {
                "optionId": "B",
                "optionText": "倾听各方意见,寻找能让大家都接受的折中方案",
                "scoring": {"教育培训": 4, "公共服务": 3}
            },
            {
                "optionId": "C",
                "optionText": "快速拍板决定,避免讨论浪费时间",
                "scoring": {"商业服务": 3, "自主创业": 3}
            },
            {
                "optionId": "D",
                "optionText": "做几个原型让大家试用,用实际效果说话",
                "scoring": {"工程制造": 3, "文化艺术": 2}
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
                "scoring": {"科研创新": 4, "医疗健康": 3}
            },
            {
                "optionId": "B",
                "optionText": "直接上手做项目,在实践中边做边学",
                "scoring": {"工程制造": 4, "自主创业": 2}
            },
            {
                "optionId": "C",
                "optionText": "找个老师或课程,跟着学习路径走",
                "scoring": {"教育培训": 3, "商业服务": 1}
            },
            {
                "optionId": "D",
                "optionText": "看优秀案例,模仿和改进别人的作品",
                "scoring": {"文化艺术": 4, "商业服务": 2}
            }
        ]
    }
]

print(f'\n计划新增 {len(new_behavior_questions)} 道行为场景题')
print(f'最终题目数: {len(data["questions"]) - len(questions_to_remove) + len(new_behavior_questions)} 道')
