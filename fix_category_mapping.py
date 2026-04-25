#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复岗位类别映射问题：将细分类别映射到8个测评维度
"""

import json

# 读取岗位数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义细分类别到测评维度的映射
category_to_dimension = {
    # 商业服务
    "互联网科技": "商业服务",
    "销售商务": "商业服务",
    "市场营销": "商业服务",
    "咨询服务": "商业服务",
    "金融服务": "商业服务",
    "职能支持": "商业服务",
    "供应链管理": "商业服务",

    # 医疗健康
    "临床医疗": "医疗健康",
    "医技科室": "医疗健康",
    "护理服务": "医疗健康",
    "药学服务": "医疗健康",
    "健康管理": "医疗健康",
    "生物医药": "医疗健康",

    # 教育培训
    "学校教育": "教育培训",
    "教育管理": "教育培训",
    "职业培训": "教育培训",
    "语言教育": "教育培训",
    "艺术教育": "教育培训",

    # 文化艺术
    "设计创意": "文化艺术",
    "视觉艺术": "文化艺术",
    "影视制作": "文化艺术",
    "文化传播": "文化艺术",
    "文学创作": "文化艺术",
    "表演艺术": "文化艺术",

    # 工程制造
    "电子工程": "工程制造",
    "建筑工程": "工程制造",
    "机械工程": "工程制造",
    "土木工程": "工程制造",
    "生产管理": "工程制造",
    "质量管理": "工程制造",

    # 公共服务
    "社会工作": "公共服务",
    "公共安全": "公共服务",
    "公共事业": "公共服务",
    "政府机关": "公共服务",
    "事业单位": "公共服务",

    # 科研创新
    "应用研发": "科研创新",
    "工程研发": "科研创新",
    "基础科研": "科研创新",
    "科研管理": "科研创新",
    "实验技术": "科研创新",

    # 自主创业
    "科技创业": "自主创业",
    "实体创业": "自主创业",
    "内容创业": "自主创业",
    "电商创业": "自主创业",
}

# 更新每个岗位的category
updated_count = 0
for job in data['jobs']:
    old_category = job['category']
    if old_category in category_to_dimension:
        new_category = category_to_dimension[old_category]
        job['category'] = new_category
        updated_count += 1
        print(f"✓ {job['jobName']}: {old_category} → {new_category}")
    else:
        print(f"⚠ {job['jobName']}: 未找到映射 ({old_category})")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个岗位的类别映射")

# 统计新的类别分布
from collections import Counter
new_categories = Counter([job['category'] for job in data['jobs']])
print("\n更新后的类别分布:")
for cat, count in new_categories.most_common():
    print(f"  {cat}: {count}个")
