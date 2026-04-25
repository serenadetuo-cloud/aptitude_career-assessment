#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
打乱题目选项顺序,避免某些维度总是出现在固定位置
"""

import json
import random

# 读取题库
with open('public/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 设置随机种子以保证可复现
random.seed(42)

# 需要打乱选项的题目(排除Q0专业选择题)
shuffled_count = 0
for q in data['questions']:
    if q['questionId'] == 0:
        continue

    # 打乱选项顺序
    options = q['options']
    random.shuffle(options)

    # 重新分配optionId (A, B, C, D, E)
    option_ids = ['A', 'B', 'C', 'D', 'E']
    for i, opt in enumerate(options):
        opt['optionId'] = option_ids[i]

    q['options'] = options
    shuffled_count += 1

print(f"✓ 已打乱 {shuffled_count} 道题目的选项顺序")

# 保存
with open('public/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n完成!选项位置已随机化,避免维度位置偏向")
