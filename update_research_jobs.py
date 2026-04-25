#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为科研创新类岗位补充真实的 typicalDay 数据
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义科研创新类岗位的真实 typicalDay 数据
research_typical_day = {
    "researcher": [
        {"time": "09:00-10:00", "activity": "查看实验数据，分析昨天的实验结果"},
        {"time": "10:00-12:00", "activity": "设计新实验方案，准备实验材料"},
        {"time": "14:00-16:00", "activity": "进行实验，记录数据和现象"},
        {"time": "16:00-17:00", "activity": "和导师讨论研究进展，调整方向"},
        {"time": "17:00-18:00", "activity": "阅读文献，学习最新研究成果"}
    ],
    "physics_researcher": [
        {"time": "09:00-10:00", "activity": "查看实验设备状态，校准仪器"},
        {"time": "10:00-12:00", "activity": "进行物理实验，测量数据"},
        {"time": "14:00-16:00", "activity": "分析实验数据，建立物理模型"},
        {"time": "16:00-17:00", "activity": "和团队讨论理论推导和实验设计"},
        {"time": "17:00-18:00", "activity": "撰写论文，整理研究成果"}
    ],
    "ai_researcher": [
        {"time": "09:00-10:00", "activity": "查看模型训练结果，分析性能指标"},
        {"time": "10:00-12:00", "activity": "设计新的算法架构，编写代码"},
        {"time": "14:00-16:00", "activity": "训练模型，调整超参数"},
        {"time": "16:00-17:00", "activity": "和团队讨论研究思路，分享进展"},
        {"time": "17:00-18:00", "activity": "阅读顶会论文，学习最新AI技术"}
    ],
    "algorithm_engineer": [
        {"time": "09:00-10:00", "activity": "查看算法性能指标，发现优化空间"},
        {"time": "10:00-12:00", "activity": "设计优化算法，编写代码实现"},
        {"time": "14:00-16:00", "activity": "测试算法效果，对比baseline"},
        {"time": "16:00-17:00", "activity": "和产品、工程团队对接，推动上线"},
        {"time": "17:00-18:00", "activity": "学习新的算法理论和优化技巧"}
    ],
    "data_scientist": [
        {"time": "09:00-10:00", "activity": "查看业务数据，发现异常和趋势"},
        {"time": "10:00-12:00", "activity": "清洗数据，进行特征工程"},
        {"time": "14:00-16:00", "activity": "建立预测模型，评估模型效果"},
        {"time": "16:00-17:00", "activity": "制作数据分析报告，给出业务建议"},
        {"time": "17:00-18:00", "activity": "学习新的数据分析方法和工具"}
    ],
    "rd_engineer": [
        {"time": "09:00-10:00", "activity": "查看研发项目进度，确认技术难点"},
        {"time": "10:00-12:00", "activity": "设计技术方案，进行原型开发"},
        {"time": "14:00-16:00", "activity": "测试验证，解决技术问题"},
        {"time": "16:00-17:00", "activity": "和团队讨论技术路线，评审方案"},
        {"time": "17:00-18:00", "activity": "学习新技术，关注行业动态"}
    ],
    "materials_engineer": [
        {"time": "09:00-10:00", "activity": "查看材料测试报告，分析性能数据"},
        {"time": "10:00-12:00", "activity": "设计新材料配方，准备样品"},
        {"time": "14:00-16:00", "activity": "进行材料合成和加工实验"},
        {"time": "16:00-17:00", "activity": "测试材料性能，记录实验结果"},
        {"time": "17:00-18:00", "activity": "学习材料科学新进展和应用"}
    ],
    "new_energy_engineer": [
        {"time": "09:00-10:00", "activity": "查看能源系统运行数据，发现问题"},
        {"time": "10:00-12:00", "activity": "设计新能源技术方案，计算效率"},
        {"time": "14:00-16:00", "activity": "进行实验测试，验证技术可行性"},
        {"time": "16:00-17:00", "activity": "和工程团队讨论，推动技术落地"},
        {"time": "17:00-18:00", "activity": "学习新能源技术和政策"}
    ],
    "lab_technician": [
        {"time": "09:00-10:00", "activity": "准备实验设备和试剂"},
        {"time": "10:00-12:00", "activity": "协助研究人员进行实验"},
        {"time": "14:00-16:00", "activity": "维护实验设备，确保正常运行"},
        {"time": "16:00-17:00", "activity": "整理实验数据，记录实验日志"},
        {"time": "17:00-18:00", "activity": "清洁实验室，管理试剂库存"}
    ],
    "research_project_manager": [
        {"time": "09:00-10:00", "activity": "查看项目进度，确认里程碑完成情况"},
        {"time": "10:00-12:00", "activity": "协调研究团队，解决资源和进度问题"},
        {"time": "14:00-16:00", "activity": "和合作方开会，对齐项目目标"},
        {"time": "16:00-17:00", "activity": "撰写项目报告，汇报研究进展"},
        {"time": "17:00-18:00", "activity": "规划下阶段工作，申请项目经费"}
    ],
    "tech_transfer_specialist": [
        {"time": "09:00-10:00", "activity": "评估科研成果的商业化潜力"},
        {"time": "10:00-12:00", "activity": "和企业对接，推介技术成果"},
        {"time": "14:00-16:00", "activity": "协助技术转化，解决落地问题"},
        {"time": "16:00-17:00", "activity": "处理知识产权和合同事务"},
        {"time": "17:00-18:00", "activity": "跟踪技术转化进展，评估效果"}
    ]
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in research_typical_day:
        job['typicalDay'] = research_typical_day[job_id]
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个科研创新类岗位的 typicalDay 数据")
