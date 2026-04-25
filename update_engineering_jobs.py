#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为工程制造类岗位补充真实的 typicalDay 数据
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义工程制造类岗位的真实 typicalDay 数据
engineering_typical_day = {
    "mechanical_engineer": [
        {"time": "09:00-10:00", "activity": "查看设计图纸，确认今天的设计任务"},
        {"time": "10:00-12:00", "activity": "用CAD设计机械零件，计算强度和尺寸"},
        {"time": "14:00-16:00", "activity": "和工艺工程师讨论可制造性，调整设计"},
        {"time": "16:00-17:00", "activity": "审核供应商提供的样件，检查质量"},
        {"time": "17:00-18:00", "activity": "学习新的机械设计标准和技术"}
    ],
    "process_engineer": [
        {"time": "09:00-10:00", "activity": "巡视生产线，检查工艺执行情况"},
        {"time": "10:00-12:00", "activity": "优化生产工艺，提升效率和良品率"},
        {"time": "14:00-16:00", "activity": "分析质量问题，制定改进方案"},
        {"time": "16:00-17:00", "activity": "培训操作工，确保工艺标准执行"},
        {"time": "17:00-18:00", "activity": "编写工艺文件，更新作业指导书"}
    ],
    "hardware_engineer": [
        {"time": "09:00-10:00", "activity": "查看测试报告，分析硬件问题"},
        {"time": "10:00-12:00", "activity": "设计电路板，选择芯片和元器件"},
        {"time": "14:00-16:00", "activity": "调试硬件，测试信号和功能"},
        {"time": "16:00-17:00", "activity": "和软件工程师对接，确认接口协议"},
        {"time": "17:00-18:00", "activity": "学习新的硬件技术和芯片方案"}
    ],
    "embedded_engineer": [
        {"time": "09:00-10:00", "activity": "查看设备日志，定位嵌入式系统问题"},
        {"time": "10:00-12:00", "activity": "编写嵌入式代码，实现硬件控制逻辑"},
        {"time": "14:00-16:00", "activity": "调试程序，测试传感器和执行器"},
        {"time": "16:00-17:00", "activity": "优化代码性能，降低功耗和内存占用"},
        {"time": "17:00-18:00", "activity": "学习RTOS和嵌入式开发新技术"}
    ],
    "electronic_engineer": [
        {"time": "09:00-10:00", "activity": "查看电路设计需求，确认技术指标"},
        {"time": "10:00-12:00", "activity": "设计模拟电路和数字电路"},
        {"time": "14:00-16:00", "activity": "仿真电路性能，调整参数"},
        {"time": "16:00-17:00", "activity": "制作PCB样板，进行功能测试"},
        {"time": "17:00-18:00", "activity": "学习电子技术新趋势和器件"}
    ],
    "architect": [
        {"time": "09:00-10:00", "activity": "和客户沟通，了解建筑需求和预算"},
        {"time": "10:00-12:00", "activity": "设计建筑方案，绘制平面图和立面图"},
        {"time": "14:00-16:00", "activity": "用BIM软件建模，展示设计效果"},
        {"time": "16:00-17:00", "activity": "和结构工程师讨论，确认结构可行性"},
        {"time": "17:00-18:00", "activity": "参观建筑项目，学习设计理念"}
    ],
    "structural_engineer": [
        {"time": "09:00-10:00", "activity": "查看建筑图纸，确认结构设计任务"},
        {"time": "10:00-12:00", "activity": "计算结构受力，设计梁柱配筋"},
        {"time": "14:00-16:00", "activity": "用结构软件建模，进行抗震分析"},
        {"time": "16:00-17:00", "activity": "审核施工图，检查结构安全"},
        {"time": "17:00-18:00", "activity": "学习结构设计规范和新技术"}
    ],
    "construction_manager": [
        {"time": "09:00-10:00", "activity": "巡视施工现场，检查进度和质量"},
        {"time": "10:00-12:00", "activity": "协调各工种，解决施工问题"},
        {"time": "14:00-16:00", "activity": "和监理、甲方开会，汇报进度"},
        {"time": "16:00-17:00", "activity": "审核材料进场，确认质量合格"},
        {"time": "17:00-18:00", "activity": "编制施工计划，安排明天工作"}
    ],
    "civil_engineer": [
        {"time": "09:00-10:00", "activity": "查看工程图纸，确认设计任务"},
        {"time": "10:00-12:00", "activity": "设计道路、桥梁或水利工程"},
        {"time": "14:00-16:00", "activity": "进行工程量计算和成本估算"},
        {"time": "16:00-17:00", "activity": "现场勘察，了解地质和环境条件"},
        {"time": "17:00-18:00", "activity": "学习土木工程新规范和技术"}
    ],
    "surveying_engineer": [
        {"time": "09:00-10:00", "activity": "准备测绘设备，确认今天的测量任务"},
        {"time": "10:00-12:00", "activity": "现场测量，采集地形和坐标数据"},
        {"time": "14:00-16:00", "activity": "处理测量数据，绘制地形图"},
        {"time": "16:00-17:00", "activity": "和设计师对接，提供测量成果"},
        {"time": "17:00-18:00", "activity": "学习新的测绘技术和软件"}
    ],
    "procurement_specialist": [
        {"time": "09:00-10:00", "activity": "查看采购需求，确认物料清单"},
        {"time": "10:00-12:00", "activity": "询价比价，选择供应商"},
        {"time": "14:00-16:00", "activity": "谈判价格和交期，签订合同"},
        {"time": "16:00-17:00", "activity": "跟踪订单进度，催促交货"},
        {"time": "17:00-18:00", "activity": "分析采购成本，优化供应商"}
    ],
    "logistics_manager": [
        {"time": "09:00-10:00", "activity": "查看物流数据，分析配送效率"},
        {"time": "10:00-12:00", "activity": "规划运输路线，优化配送方案"},
        {"time": "14:00-16:00", "activity": "协调仓库和运输，解决物流问题"},
        {"time": "16:00-17:00", "activity": "和客户沟通，确认交货时间"},
        {"time": "17:00-18:00", "activity": "分析物流成本，制定降本方案"}
    ],
    "supply_chain_analyst": [
        {"time": "09:00-10:00", "activity": "查看供应链数据，发现异常"},
        {"time": "10:00-12:00", "activity": "分析库存周转率和缺货风险"},
        {"time": "14:00-16:00", "activity": "建立预测模型，优化库存策略"},
        {"time": "16:00-17:00", "activity": "和采购、生产对接，调整计划"},
        {"time": "17:00-18:00", "activity": "制作供应链分析报告"}
    ],
    "quality_engineer": [
        {"time": "09:00-10:00", "activity": "查看质量数据，分析不良率"},
        {"time": "10:00-12:00", "activity": "制定质量标准和检验方案"},
        {"time": "14:00-16:00", "activity": "现场检查产品质量，记录问题"},
        {"time": "16:00-17:00", "activity": "分析质量问题根因，制定改进措施"},
        {"time": "17:00-18:00", "activity": "培训质检员，提升检验能力"}
    ],
    "qa_specialist": [
        {"time": "09:00-10:00", "activity": "查看测试计划，确认今天的测试任务"},
        {"time": "10:00-12:00", "activity": "执行功能测试，记录bug"},
        {"time": "14:00-16:00", "activity": "回归测试，验证bug修复"},
        {"time": "16:00-17:00", "activity": "编写测试报告，评估产品质量"},
        {"time": "17:00-18:00", "activity": "学习测试工具和自动化技术"}
    ],
    "production_manager": [
        {"time": "09:00-10:00", "activity": "查看生产计划，安排今天的生产任务"},
        {"time": "10:00-12:00", "activity": "巡视生产线，解决生产问题"},
        {"time": "14:00-16:00", "activity": "协调物料和人员，确保生产顺畅"},
        {"time": "16:00-17:00", "activity": "分析生产效率，制定改进方案"},
        {"time": "17:00-18:00", "activity": "总结当天生产情况，规划明天工作"}
    ],
    "lean_specialist": [
        {"time": "09:00-10:00", "activity": "观察生产流程，识别浪费环节"},
        {"time": "10:00-12:00", "activity": "设计精益改善方案，优化流程"},
        {"time": "14:00-16:00", "activity": "推动改善项目实施，培训员工"},
        {"time": "16:00-17:00", "activity": "评估改善效果，计算收益"},
        {"time": "17:00-18:00", "activity": "学习精益生产新方法和案例"}
    ],
    "safety_engineer": [
        {"time": "09:00-10:00", "activity": "巡视现场，检查安全隐患"},
        {"time": "10:00-12:00", "activity": "制定安全管理制度和应急预案"},
        {"time": "14:00-16:00", "activity": "培训员工安全知识，组织演练"},
        {"time": "16:00-17:00", "activity": "调查安全事故，分析原因"},
        {"time": "17:00-18:00", "activity": "学习安全法规和管理方法"}
    ]
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in engineering_typical_day:
        job['typicalDay'] = engineering_typical_day[job_id]
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个工程制造类岗位的 typicalDay 数据")
