#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为公共服务类岗位补充真实的 typicalDay 数据
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义公共服务类岗位的真实 typicalDay 数据
public_service_typical_day = {
    "civil_servant": [
        {"time": "09:00-10:00", "activity": "查看文件和通知，确认今天的工作安排"},
        {"time": "10:00-12:00", "activity": "起草政策文件或工作报告"},
        {"time": "14:00-16:00", "activity": "参加会议，讨论政策执行和问题"},
        {"time": "16:00-17:00", "activity": "接待群众来访，处理诉求"},
        {"time": "17:00-18:00", "activity": "整理材料，准备明天的汇报"}
    ],
    "policy_researcher": [
        {"time": "09:00-10:00", "activity": "查看最新政策动态和研究资料"},
        {"time": "10:00-12:00", "activity": "调研分析，收集数据和案例"},
        {"time": "14:00-16:00", "activity": "撰写政策研究报告和建议"},
        {"time": "16:00-17:00", "activity": "和领导或专家讨论研究成果"},
        {"time": "17:00-18:00", "activity": "阅读文献，学习政策理论"}
    ],
    "public_institution_staff": [
        {"time": "09:00-10:00", "activity": "查看工作安排，准备今天的任务"},
        {"time": "10:00-12:00", "activity": "办理业务，服务群众"},
        {"time": "14:00-16:00", "activity": "整理档案和材料"},
        {"time": "16:00-17:00", "activity": "参加培训或学习"},
        {"time": "17:00-18:00", "activity": "总结工作，准备明天的计划"}
    ],
    "social_worker": [
        {"time": "09:00-10:00", "activity": "查看服务对象情况，制定今天的访问计划"},
        {"time": "10:00-12:00", "activity": "上门走访，了解困难群众需求"},
        {"time": "14:00-16:00", "activity": "协调资源，帮助解决实际问题"},
        {"time": "16:00-17:00", "activity": "记录服务情况，更新档案"},
        {"time": "17:00-18:00", "activity": "参加督导会议，分享案例"}
    ],
    "community_worker": [
        {"time": "09:00-10:00", "activity": "巡视社区，了解居民需求"},
        {"time": "10:00-12:00", "activity": "处理居民事务，协调物业和相关部门"},
        {"time": "14:00-16:00", "activity": "组织社区活动，服务居民"},
        {"time": "16:00-17:00", "activity": "调解邻里纠纷，维护社区和谐"},
        {"time": "17:00-18:00", "activity": "整理社区档案，上报工作情况"}
    ],
    "ngo_worker": [
        {"time": "09:00-10:00", "activity": "查看项目进展，确认今天的任务"},
        {"time": "10:00-12:00", "activity": "执行公益项目，服务受助群体"},
        {"time": "14:00-16:00", "activity": "筹款和宣传，扩大项目影响"},
        {"time": "16:00-17:00", "activity": "和志愿者沟通，协调活动"},
        {"time": "17:00-18:00", "activity": "撰写项目报告，总结成果"}
    ],
    "police_officer": [
        {"time": "09:00-10:00", "activity": "交接班，了解辖区治安情况"},
        {"time": "10:00-12:00", "activity": "巡逻执勤，维护社会秩序"},
        {"time": "14:00-16:00", "activity": "处理报警，调查案件"},
        {"time": "16:00-17:00", "activity": "询问当事人，记录笔录"},
        {"time": "17:00-18:00", "activity": "整理案卷，准备移交"}
    ],
    "firefighter": [
        {"time": "09:00-10:00", "activity": "检查消防装备，确保随时可用"},
        {"time": "10:00-12:00", "activity": "训练演练，提升救援能力"},
        {"time": "14:00-16:00", "activity": "消防宣传，普及安全知识"},
        {"time": "16:00-17:00", "activity": "维护消防车辆和器材"},
        {"time": "17:00-18:00", "activity": "学习新的救援技术和案例"}
    ],
    "emergency_manager": [
        {"time": "09:00-10:00", "activity": "查看应急值班情况，确认预警信息"},
        {"time": "10:00-12:00", "activity": "制定应急预案，组织演练"},
        {"time": "14:00-16:00", "activity": "协调应急资源，检查物资储备"},
        {"time": "16:00-17:00", "activity": "培训应急队伍，提升响应能力"},
        {"time": "17:00-18:00", "activity": "总结应急案例，优化预案"}
    ],
    "urban_planner": [
        {"time": "09:00-10:00", "activity": "查看城市规划项目，确认设计任务"},
        {"time": "10:00-12:00", "activity": "设计城市空间布局，绘制规划图"},
        {"time": "14:00-16:00", "activity": "实地调研，了解现状和问题"},
        {"time": "16:00-17:00", "activity": "和政府部门沟通，汇报规划方案"},
        {"time": "17:00-18:00", "activity": "学习城市规划理论和案例"}
    ],
    "environmental_specialist": [
        {"time": "09:00-10:00", "activity": "查看环境监测数据，发现异常"},
        {"time": "10:00-12:00", "activity": "现场检查，评估环境影响"},
        {"time": "14:00-16:00", "activity": "制定环保方案，提出改进建议"},
        {"time": "16:00-17:00", "activity": "和企业沟通，督促整改"},
        {"time": "17:00-18:00", "activity": "撰写环境评估报告"}
    ],
    "transportation_planner": [
        {"time": "09:00-10:00", "activity": "查看交通数据，分析拥堵问题"},
        {"time": "10:00-12:00", "activity": "设计交通方案，优化路网布局"},
        {"time": "14:00-16:00", "activity": "实地调研，观察交通流量"},
        {"time": "16:00-17:00", "activity": "和交通部门沟通，推动方案实施"},
        {"time": "17:00-18:00", "activity": "学习交通规划新技术和案例"}
    ]
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in public_service_typical_day:
        job['typicalDay'] = public_service_typical_day[job_id]
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个公共服务类岗位的 typicalDay 数据")
