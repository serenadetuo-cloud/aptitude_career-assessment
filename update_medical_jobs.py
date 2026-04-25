#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为医疗健康类岗位补充真实的 typicalDay 数据
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义医疗健康类岗位的真实 typicalDay 数据
medical_typical_day = {
    "clinical_doctor": [
        {"time": "08:00-09:00", "activity": "查房，了解住院患者的病情变化和检查结果"},
        {"time": "09:00-12:00", "activity": "门诊接诊，问诊、体格检查、开具检查单和处方"},
        {"time": "14:00-16:00", "activity": "分析检查报告，制定治疗方案，和患者沟通病情"},
        {"time": "16:00-17:00", "activity": "参加科室病例讨论会，学习疑难病例"},
        {"time": "17:00-18:00", "activity": "整理病历，更新电子病历系统"}
    ],
    "surgeon": [
        {"time": "08:00-09:00", "activity": "查房，检查术后患者恢复情况，调整治疗方案"},
        {"time": "09:00-12:00", "activity": "进行手术，专注操作，和助手配合"},
        {"time": "14:00-16:00", "activity": "门诊接诊，评估患者是否需要手术"},
        {"time": "16:00-17:00", "activity": "查看术后患者影像资料，确认恢复进度"},
        {"time": "17:00-18:00", "activity": "学习新的手术技术和文献"}
    ],
    "pediatrician": [
        {"time": "08:00-09:00", "activity": "查房，观察住院儿童的病情和生命体征"},
        {"time": "09:00-12:00", "activity": "门诊接诊，安抚哭闹的孩子，和家长沟通病情"},
        {"time": "14:00-16:00", "activity": "分析检查结果，制定儿童用药方案"},
        {"time": "16:00-17:00", "activity": "参加儿科病例讨论，学习罕见儿童疾病"},
        {"time": "17:00-18:00", "activity": "更新病历，准备明天的查房计划"}
    ],
    "psychiatrist": [
        {"time": "08:00-09:00", "activity": "查看住院患者的情绪状态和用药反应"},
        {"time": "09:00-12:00", "activity": "门诊心理评估，倾听患者诉说，进行心理测试"},
        {"time": "14:00-16:00", "activity": "心理治疗，使用认知行为疗法帮助患者"},
        {"time": "16:00-17:00", "activity": "调整药物治疗方案，监测副作用"},
        {"time": "17:00-18:00", "activity": "记录治疗笔记，学习最新心理治疗方法"}
    ],
    "dentist": [
        {"time": "08:00-09:00", "activity": "查看今天的预约患者，准备治疗器械"},
        {"time": "09:00-12:00", "activity": "口腔检查和治疗，补牙、拔牙、根管治疗"},
        {"time": "14:00-16:00", "activity": "继续接诊患者，进行牙齿美白和正畸"},
        {"time": "16:00-17:00", "activity": "和患者沟通治疗方案和费用"},
        {"time": "17:00-18:00", "activity": "消毒器械，整理诊室，学习新技术"}
    ],
    "nurse": [
        {"time": "08:00-09:00", "activity": "交接班，了解患者夜间情况"},
        {"time": "09:00-12:00", "activity": "执行医嘱，输液、换药、测量生命体征"},
        {"time": "14:00-16:00", "activity": "协助医生查房，记录患者病情变化"},
        {"time": "16:00-17:00", "activity": "健康宣教，指导患者用药和康复"},
        {"time": "17:00-18:00", "activity": "整理护理记录，准备交接班"}
    ],
    "head_nurse": [
        {"time": "08:00-09:00", "activity": "主持晨会，安排护士工作，强调注意事项"},
        {"time": "09:00-12:00", "activity": "巡视病房，检查护理质量，处理突发情况"},
        {"time": "14:00-16:00", "activity": "培训新护士，指导护理技能"},
        {"time": "16:00-17:00", "activity": "协调科室资源，处理患者投诉"},
        {"time": "17:00-18:00", "activity": "总结当天工作，制定改进计划"}
    ],
    "pharmacist": [
        {"time": "08:00-09:00", "activity": "检查药品库存，确认今天需要补充的药品"},
        {"time": "09:00-12:00", "activity": "审核处方，调配药品，指导患者用药"},
        {"time": "14:00-16:00", "activity": "药品管理，检查效期，处理过期药品"},
        {"time": "16:00-17:00", "activity": "参加药事会，讨论合理用药问题"},
        {"time": "17:00-18:00", "activity": "学习新药知识，更新药品信息"}
    ],
    "clinical_pharmacist": [
        {"time": "08:00-09:00", "activity": "查房，了解患者用药情况和不良反应"},
        {"time": "09:00-12:00", "activity": "审核医嘱，发现用药问题并和医生沟通"},
        {"time": "14:00-16:00", "activity": "制定个体化用药方案，监测血药浓度"},
        {"time": "16:00-17:00", "activity": "药学咨询，解答医生和患者的用药问题"},
        {"time": "17:00-18:00", "activity": "记录药学监护记录，学习临床药学文献"}
    ],
    "medical_technologist": [
        {"time": "08:00-09:00", "activity": "准备检验设备，校准仪器"},
        {"time": "09:00-12:00", "activity": "处理血液、尿液等标本，进行检验"},
        {"time": "14:00-16:00", "activity": "分析检验结果，发现异常值并复查"},
        {"time": "16:00-17:00", "activity": "出具检验报告，和临床医生沟通"},
        {"time": "17:00-18:00", "activity": "维护设备，学习新的检验技术"}
    ],
    "radiologist": [
        {"time": "08:00-09:00", "activity": "查看今天的检查预约，准备设备"},
        {"time": "09:00-12:00", "activity": "阅读X光、CT、MRI影像，写诊断报告"},
        {"time": "14:00-16:00", "activity": "继续阅片，发现疑难病例并会诊"},
        {"time": "16:00-17:00", "activity": "和临床医生讨论影像表现和诊断"},
        {"time": "17:00-18:00", "activity": "学习影像诊断新技术和病例"}
    ],
    "rehabilitation_therapist": [
        {"time": "08:00-09:00", "activity": "评估患者康复进度，调整治疗计划"},
        {"time": "09:00-12:00", "activity": "指导患者进行运动康复训练"},
        {"time": "14:00-16:00", "activity": "使用理疗设备，进行物理治疗"},
        {"time": "16:00-17:00", "activity": "记录康复效果，和医生沟通"},
        {"time": "17:00-18:00", "activity": "学习新的康复技术和方法"}
    ],
    "psychologist": [
        {"time": "08:00-09:00", "activity": "查看今天的咨询预约，准备咨询材料"},
        {"time": "09:00-12:00", "activity": "一对一心理咨询，倾听来访者困扰"},
        {"time": "14:00-16:00", "activity": "进行心理测评，分析测试结果"},
        {"time": "16:00-17:00", "activity": "制定心理干预方案，设计咨询目标"},
        {"time": "17:00-18:00", "activity": "记录咨询笔记，学习心理学新理论"}
    ],
    "health_manager": [
        {"time": "08:00-09:00", "activity": "查看客户健康数据，发现异常指标"},
        {"time": "09:00-12:00", "activity": "制定个性化健康管理方案"},
        {"time": "14:00-16:00", "activity": "电话随访客户，指导健康行为"},
        {"time": "16:00-17:00", "activity": "组织健康讲座，普及健康知识"},
        {"time": "17:00-18:00", "activity": "分析健康管理效果，优化方案"}
    ],
    "nutritionist": [
        {"time": "08:00-09:00", "activity": "评估客户饮食习惯和营养状况"},
        {"time": "09:00-12:00", "activity": "制定个性化营养方案和食谱"},
        {"time": "14:00-16:00", "activity": "营养咨询，解答饮食问题"},
        {"time": "16:00-17:00", "activity": "跟踪客户执行情况，调整方案"},
        {"time": "17:00-18:00", "activity": "学习营养学新知识，研究食物成分"}
    ],
    "drug_rd_engineer": [
        {"time": "08:00-09:00", "activity": "查看实验数据，分析药物活性"},
        {"time": "09:00-12:00", "activity": "设计新化合物，进行合成实验"},
        {"time": "14:00-16:00", "activity": "测试药物效果，记录实验结果"},
        {"time": "16:00-17:00", "activity": "和团队讨论研发进展，调整方案"},
        {"time": "17:00-18:00", "activity": "阅读文献，学习新的药物研发技术"}
    ],
    "medical_device_engineer": [
        {"time": "08:00-09:00", "activity": "查看设备测试报告，发现问题"},
        {"time": "09:00-12:00", "activity": "设计医疗器械，绘制工程图纸"},
        {"time": "14:00-16:00", "activity": "制作样机，进行功能测试"},
        {"time": "16:00-17:00", "activity": "和临床医生沟通，了解使用需求"},
        {"time": "17:00-18:00", "activity": "学习医疗器械法规和新技术"}
    ],
    "biotech_researcher": [
        {"time": "08:00-09:00", "activity": "准备实验材料，配置试剂"},
        {"time": "09:00-12:00", "activity": "进行基因编辑、细胞培养等实验"},
        {"time": "14:00-16:00", "activity": "分析实验数据，绘制图表"},
        {"time": "16:00-17:00", "activity": "和导师讨论研究进展，调整方案"},
        {"time": "17:00-18:00", "activity": "阅读生物技术文献，学习新方法"}
    ]
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in medical_typical_day:
        job['typicalDay'] = medical_typical_day[job_id]
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个医疗健康类岗位的 typicalDay 数据")
