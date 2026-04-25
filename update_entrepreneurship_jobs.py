#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为自主创业类岗位补充真实的 typicalDay 数据
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义自主创业类岗位的真实 typicalDay 数据
entrepreneurship_typical_day = {
    "tech_entrepreneur": [
        {"time": "09:00-10:00", "activity": "查看产品数据和用户反馈，确定今天的优先级"},
        {"time": "10:00-12:00", "activity": "和团队开会，讨论产品方向和技术难点"},
        {"time": "14:00-16:00", "activity": "见投资人或合作伙伴，推进融资或商务合作"},
        {"time": "16:00-17:00", "activity": "处理公司运营事务，招聘、财务、法务"},
        {"time": "17:00-18:00", "activity": "学习行业动态，思考战略方向"}
    ],
    "saas_entrepreneur": [
        {"time": "09:00-10:00", "activity": "查看SaaS产品的关键指标：MRR、流失率、NPS"},
        {"time": "10:00-12:00", "activity": "和客户沟通，了解需求和痛点"},
        {"time": "14:00-16:00", "activity": "优化产品功能和定价策略"},
        {"time": "16:00-17:00", "activity": "制定营销计划，拓展客户渠道"},
        {"time": "17:00-18:00", "activity": "研究竞品，学习SaaS运营方法"}
    ],
    "restaurant_entrepreneur": [
        {"time": "09:00-10:00", "activity": "检查食材库存和供应商送货"},
        {"time": "10:00-12:00", "activity": "准备营业，培训员工，检查卫生"},
        {"time": "14:00-16:00", "activity": "巡视餐厅，确保服务质量和顾客满意度"},
        {"time": "16:00-17:00", "activity": "分析经营数据，优化菜单和成本"},
        {"time": "17:00-18:00", "activity": "规划营销活动，吸引新客户"}
    ],
    "retail_entrepreneur": [
        {"time": "09:00-10:00", "activity": "查看销售数据，分析畅销和滞销商品"},
        {"time": "10:00-12:00", "activity": "选品进货，和供应商谈判价格"},
        {"time": "14:00-16:00", "activity": "管理店铺运营，培训员工，优化陈列"},
        {"time": "16:00-17:00", "activity": "制定促销活动，提升销售额"},
        {"time": "17:00-18:00", "activity": "研究市场趋势，寻找新的商机"}
    ],
    "media_entrepreneur": [
        {"time": "09:00-10:00", "activity": "查看内容数据，分析哪些选题受欢迎"},
        {"time": "10:00-12:00", "activity": "策划内容选题，创作或拍摄内容"},
        {"time": "14:00-16:00", "activity": "剪辑制作，发布内容到各平台"},
        {"time": "16:00-17:00", "activity": "和品牌方谈合作，拓展商业化渠道"},
        {"time": "17:00-18:00", "activity": "学习内容创作技巧，研究平台算法"}
    ],
    "knowledge_entrepreneur": [
        {"time": "09:00-10:00", "activity": "查看课程销售数据和学员反馈"},
        {"time": "10:00-12:00", "activity": "设计课程内容，录制视频或准备直播"},
        {"time": "14:00-16:00", "activity": "运营社群，解答学员问题"},
        {"time": "16:00-17:00", "activity": "制定营销策略，推广课程"},
        {"time": "17:00-18:00", "activity": "学习新知识，提升专业能力"}
    ],
    "ecommerce_entrepreneur": [
        {"time": "09:00-10:00", "activity": "查看店铺数据，分析流量和转化率"},
        {"time": "10:00-12:00", "activity": "选品和供应链管理，优化库存"},
        {"time": "14:00-16:00", "activity": "优化商品详情页，提升转化"},
        {"time": "16:00-17:00", "activity": "投放广告，分析ROI"},
        {"time": "17:00-18:00", "activity": "学习电商运营技巧，研究平台规则"}
    ]
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in entrepreneurship_typical_day:
        job['typicalDay'] = entrepreneurship_typical_day[job_id]
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个自主创业类岗位的 typicalDay 数据")
