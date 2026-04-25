#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为有代表性前辈的岗位补充mentor数据
同时更新岗位库和mentor库
"""

import json

# 定义需要补充的代表性前辈
new_mentors = {
    # 金融投资类
    'warren_buffett': {
        'mentorId': 'warren_buffett',
        'name': '沃伦·巴菲特',
        'englishName': 'Warren Buffett',
        'avatar': '/avatars/warren_buffett.jpg',
        'title': '伯克希尔·哈撒韦CEO、投资家',
        'quote': '价值投资的本质是买入被低估的优质公司,然后长期持有。',
        'story': '从11岁开始投资股票,通过价值投资理念成为世界首富之一。他坚持"买入并持有"策略,专注于寻找具有护城河的优质企业,以合理价格买入并长期持有。他的投资哲学影响了全球无数投资者。',
        'coreAbilities': ['价值投资', '长期主义', '风险控制', '商业洞察'],
        'applicableJobs': ['investment_analyst', 'financial_advisor']
    },

    # 建筑设计类
    'zaha_hadid': {
        'mentorId': 'zaha_hadid',
        'name': '扎哈·哈迪德',
        'englishName': 'Zaha Hadid',
        'avatar': '/avatars/zaha_hadid.jpg',
        'title': '建筑师、普利兹克奖得主',
        'quote': '建筑应该是流动的、有机的,而不是僵硬的盒子。',
        'story': '首位获得普利兹克建筑奖的女性建筑师,以大胆的曲线设计和未来主义风格闻名。她的作品打破了传统建筑的直线思维,创造出流动、动感的空间。代表作包括广州大剧院、北京银河SOHO等。',
        'coreAbilities': ['创新设计', '空间想象', '美学表达', '工程实现'],
        'applicableJobs': ['architect', 'industrial_designer', 'interior_designer']
    },

    # 教育科技类
    'sal_khan': {
        'mentorId': 'sal_khan',
        'name': 'Sal Khan',
        'englishName': 'Salman Khan',
        'avatar': '/avatars/sal_khan.jpg',
        'title': 'Khan Academy创始人',
        'quote': '每个人都应该有机会免费获得世界一流的教育。',
        'story': '从为表妹辅导数学开始,创建了Khan Academy在线教育平台,提供超过10000个免费教学视频。他证明了技术可以让优质教育触达全球每个角落,改变了数百万学生的学习方式。',
        'coreAbilities': ['教学设计', '内容创作', '技术应用', '教育理念'],
        'applicableJobs': ['education_consultant', 'curriculum_designer', 'education_product_manager']
    },

    # 供应链物流类
    'jeff_bezos': {
        'mentorId': 'jeff_bezos',
        'name': '杰夫·贝佐斯',
        'englishName': 'Jeff Bezos',
        'avatar': '/avatars/jeff_bezos.jpg',
        'title': '亚马逊创始人',
        'quote': '客户至上,从长远思考,勇于创新。',
        'story': '从网上书店起步,将亚马逊打造成全球最大的电商和云计算公司。他建立了世界上最高效的物流配送体系,重新定义了零售业。他的"飞轮效应"理论和长期主义思维影响了整个科技行业。',
        'coreAbilities': ['战略思维', '客户导向', '运营效率', '创新精神'],
        'applicableJobs': ['logistics_manager', 'supply_chain_analyst', 'procurement_specialist']
    }
}

# 读取现有数据
with open('public/data/career-mentors.json', 'r', encoding='utf-8') as f:
    mentors_data = json.load(f)

with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    jobs_data = json.load(f)

# 1. 将新mentor添加到career-mentors.json
# 按类别分组
category_mapping = {
    'warren_buffett': '金融服务',
    'zaha_hadid': '设计创意',
    'sal_khan': '教育培训',
    'jeff_bezos': '商业服务'
}

for mentor_id, mentor_info in new_mentors.items():
    category = category_mapping[mentor_id]

    # 检查类别是否存在
    if category not in mentors_data['categories']:
        mentors_data['categories'][category] = {
            'categoryName': category,
            'mentors': []
        }

    # 检查mentor是否已存在
    existing_ids = [m['mentorId'] for m in mentors_data['categories'][category]['mentors']]
    if mentor_id not in existing_ids:
        mentors_data['categories'][category]['mentors'].append(mentor_info)
        print(f"✓ 添加mentor: {mentor_info['name']} 到 {category} 类别")

# 2. 更新岗位库中的mentorIds
job_mentor_mapping = {
    'investment_analyst': ['warren_buffett'],
    'financial_advisor': ['warren_buffett'],
    'architect': ['zaha_hadid'],
    'industrial_designer': ['zaha_hadid', 'yuan_yan_zai'],
    'interior_designer': ['zaha_hadid'],
    'education_consultant': ['sal_khan'],
    'curriculum_designer': ['sal_khan'],
    'education_product_manager': ['sal_khan', 'zhang_xiaolong'],
    'logistics_manager': ['jeff_bezos'],
    'supply_chain_analyst': ['jeff_bezos'],
    'procurement_specialist': ['jeff_bezos']
}

for job in jobs_data['jobs']:
    job_id = job['jobId']
    if job_id in job_mentor_mapping:
        job['mentorIds'] = job_mentor_mapping[job_id]
        print(f"✓ 更新岗位 {job['jobName']} 的mentorIds: {job['mentorIds']}")

# 保存数据
with open('public/data/career-mentors.json', 'w', encoding='utf-8') as f:
    json.dump(mentors_data, f, ensure_ascii=False, indent=2)

with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(jobs_data, f, ensure_ascii=False, indent=2)

print(f"\n完成！")
print(f"- 新增了 {len(new_mentors)} 位代表性前辈")
print(f"- 更新了 {len(job_mentor_mapping)} 个岗位的mentorIds")
