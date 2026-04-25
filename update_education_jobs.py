#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为教育培训类岗位补充真实的 typicalDay 数据
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义教育培训类岗位的真实 typicalDay 数据
education_typical_day = {
    "k12_teacher": [
        {"time": "08:00-09:00", "activity": "早读课，检查学生作业完成情况"},
        {"time": "09:00-12:00", "activity": "上课，讲解新知识点，组织课堂讨论和练习"},
        {"time": "14:00-16:00", "activity": "批改作业和试卷，记录学生学习情况"},
        {"time": "16:00-17:00", "activity": "辅导学生，解答疑问"},
        {"time": "17:00-18:00", "activity": "备课，准备明天的教学内容和课件"}
    ],
    "university_professor": [
        {"time": "09:00-10:00", "activity": "准备今天的课程，整理讲义和案例"},
        {"time": "10:00-12:00", "activity": "授课，讲解专业知识，引导学生讨论"},
        {"time": "14:00-16:00", "activity": "指导研究生，讨论论文进展和研究方向"},
        {"time": "16:00-17:00", "activity": "审阅学生论文，提出修改意见"},
        {"time": "17:00-18:00", "activity": "进行科研工作，撰写论文或申请课题"}
    ],
    "counselor": [
        {"time": "08:00-09:00", "activity": "查看学生考勤和班级通知"},
        {"time": "09:00-12:00", "activity": "处理学生事务，解决宿舍、选课等问题"},
        {"time": "14:00-16:00", "activity": "组织班会或主题教育活动"},
        {"time": "16:00-17:00", "activity": "和学生谈心，了解学习和生活状况"},
        {"time": "17:00-18:00", "activity": "整理学生档案，准备评优评奖材料"}
    ],
    "vocational_trainer": [
        {"time": "09:00-10:00", "activity": "了解学员背景和培训需求"},
        {"time": "10:00-12:00", "activity": "授课，讲解职业技能和实操方法"},
        {"time": "14:00-16:00", "activity": "指导学员实践操作，纠正错误"},
        {"time": "16:00-17:00", "activity": "评估学员学习效果，给出反馈"},
        {"time": "17:00-18:00", "activity": "更新培训内容，适应行业新变化"}
    ],
    "corporate_trainer": [
        {"time": "09:00-10:00", "activity": "和HR沟通，了解企业培训需求"},
        {"time": "10:00-12:00", "activity": "设计培训课程，准备案例和互动环节"},
        {"time": "14:00-16:00", "activity": "授课，培训员工技能或管理能力"},
        {"time": "16:00-17:00", "activity": "收集学员反馈，评估培训效果"},
        {"time": "17:00-18:00", "activity": "优化培训内容，制作新的课件"}
    ],
    "english_teacher": [
        {"time": "09:00-10:00", "activity": "备课，准备今天的英语教学内容"},
        {"time": "10:00-12:00", "activity": "上课，教授语法、词汇和口语表达"},
        {"time": "14:00-16:00", "activity": "批改作业和听写，记录学生进步"},
        {"time": "16:00-17:00", "activity": "一对一辅导，纠正发音和语法错误"},
        {"time": "17:00-18:00", "activity": "设计英语活动，提升学生学习兴趣"}
    ],
    "chinese_teacher_abroad": [
        {"time": "09:00-10:00", "activity": "准备汉语教学材料，设计文化体验活动"},
        {"time": "10:00-12:00", "activity": "教授汉语，讲解汉字、语法和文化背景"},
        {"time": "14:00-16:00", "activity": "组织中国文化体验，如书法、茶艺"},
        {"time": "16:00-17:00", "activity": "辅导学生，解答汉语学习疑问"},
        {"time": "17:00-18:00", "activity": "准备HSK考试辅导材料"}
    ],
    "music_teacher": [
        {"time": "09:00-10:00", "activity": "准备今天的音乐课程和乐器"},
        {"time": "10:00-12:00", "activity": "教授音乐理论和演奏技巧"},
        {"time": "14:00-16:00", "activity": "一对一指导学生练习，纠正指法和节奏"},
        {"time": "16:00-17:00", "activity": "排练合唱或乐队，准备演出"},
        {"time": "17:00-18:00", "activity": "选择新的教学曲目，编排教学计划"}
    ],
    "art_teacher": [
        {"time": "09:00-10:00", "activity": "准备美术课材料，布置教室"},
        {"time": "10:00-12:00", "activity": "教授绘画、雕塑或设计技巧"},
        {"time": "14:00-16:00", "activity": "指导学生创作，点评作品"},
        {"time": "16:00-17:00", "activity": "组织美术展览，展示学生作品"},
        {"time": "17:00-18:00", "activity": "研究艺术教育新方法，提升教学质量"}
    ],
    "education_consultant": [
        {"time": "09:00-10:00", "activity": "和家长沟通，了解学生情况和需求"},
        {"time": "10:00-12:00", "activity": "分析学生成绩和兴趣，制定升学规划"},
        {"time": "14:00-16:00", "activity": "研究院校信息和专业方向"},
        {"time": "16:00-17:00", "activity": "指导学生准备申请材料和面试"},
        {"time": "17:00-18:00", "activity": "跟进申请进度，调整规划方案"}
    ],
    "curriculum_designer": [
        {"time": "09:00-10:00", "activity": "研究教学大纲和学习目标"},
        {"time": "10:00-12:00", "activity": "设计课程结构和教学内容"},
        {"time": "14:00-16:00", "activity": "制作教学课件和学习资料"},
        {"time": "16:00-17:00", "activity": "和教师沟通，收集课程反馈"},
        {"time": "17:00-18:00", "activity": "优化课程设计，提升学习效果"}
    ],
    "education_product_manager": [
        {"time": "09:00-10:00", "activity": "查看用户数据，分析学习行为和完课率"},
        {"time": "10:00-12:00", "activity": "设计教育产品功能，优化学习体验"},
        {"time": "14:00-16:00", "activity": "和教研团队沟通，确认课程内容"},
        {"time": "16:00-17:00", "activity": "和技术团队对接，推动功能开发"},
        {"time": "17:00-18:00", "activity": "分析竞品，学习优秀教育产品设计"}
    ]
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in education_typical_day:
        job['typicalDay'] = education_typical_day[job_id]
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个教育培训类岗位的 typicalDay 数据")
