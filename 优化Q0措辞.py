#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
优化Q0专业选择题的措辞,添加"不限专业"选项
"""

import json

# 读取题库
with open('public/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 找到Q0并修改
q0 = next((q for q in data['questions'] if q['questionId'] == 0), None)
if q0:
    # 修改问题文本
    q0['questionText'] = "你的专业背景是?(可多选,如果不想从事专业对口工作可跳过)"

    # 修改选项I的文本
    for opt in q0['options']:
        if opt['optionId'] == 'I':
            opt['optionText'] = "不限专业/想探索更多可能性"
            opt['majorTag'] = "major_open"

    print("✓ 已优化Q0的措辞")
    print(f"  新问题: {q0['questionText']}")
    print(f"  选项I: {q0['options'][-1]['optionText']}")

# 保存
with open('public/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n完成!")
