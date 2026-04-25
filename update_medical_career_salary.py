#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为医疗健康类岗位补充真实的薪资和职业路径数据
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义医疗健康类岗位的真实薪资和职业路径
medical_career_salary = {
    "clinical_doctor": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["住院医师", "初级职称"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["主治医师", "中级职称"], "duration": "3-8年"},
            "senior": {"title": "高级", "positions": ["副主任医师", "主任医师"], "duration": "8年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 150000, "max": 250000, "description": "三甲医院"},
                "tier2": {"min": 100000, "max": 180000, "description": "二级医院"},
                "startup": {"min": 120000, "max": 200000, "description": "民营医院"}
            },
            "experienced_3y": {
                "tier1": {"min": 250000, "max": 450000, "description": "三甲医院"},
                "tier2": {"min": 180000, "max": 320000, "description": "二级医院"},
                "startup": {"min": 200000, "max": 380000, "description": "民营医院"}
            },
            "experienced_5y": {
                "tier1": {"min": 450000, "max": 800000, "description": "三甲医院"},
                "tier2": {"min": 320000, "max": 550000, "description": "二级医院"},
                "startup": {"min": 380000, "max": 700000, "description": "民营医院", "note": "含灰色收入"}
            }
        }
    },
    "surgeon": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["住院医师", "初级职称"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["主治医师", "中级职称"], "duration": "3-8年"},
            "senior": {"title": "高级", "positions": ["副主任医师", "主任医师"], "duration": "8年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 180000, "max": 300000, "description": "三甲医院"},
                "tier2": {"min": 120000, "max": 220000, "description": "二级医院"},
                "startup": {"min": 150000, "max": 250000, "description": "民营医院"}
            },
            "experienced_3y": {
                "tier1": {"min": 300000, "max": 600000, "description": "三甲医院"},
                "tier2": {"min": 220000, "max": 400000, "description": "二级医院"},
                "startup": {"min": 250000, "max": 500000, "description": "民营医院"}
            },
            "experienced_5y": {
                "tier1": {"min": 600000, "max": 1200000, "description": "三甲医院"},
                "tier2": {"min": 400000, "max": 800000, "description": "二级医院"},
                "startup": {"min": 500000, "max": 1000000, "description": "民营医院", "note": "顶级外科医生可达数百万"}
            }
        }
    },
    "nurse": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["护士", "护师"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["主管护师"], "duration": "3-8年"},
            "senior": {"title": "高级", "positions": ["副主任护师", "主任护师"], "duration": "8年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 80000, "max": 150000, "description": "三甲医院"},
                "tier2": {"min": 60000, "max": 100000, "description": "二级医院"},
                "startup": {"min": 70000, "max": 120000, "description": "民营医院"}
            },
            "experienced_3y": {
                "tier1": {"min": 150000, "max": 250000, "description": "三甲医院"},
                "tier2": {"min": 100000, "max": 180000, "description": "二级医院"},
                "startup": {"min": 120000, "max": 200000, "description": "民营医院"}
            },
            "experienced_5y": {
                "tier1": {"min": 250000, "max": 400000, "description": "三甲医院"},
                "tier2": {"min": 180000, "max": 300000, "description": "二级医院"},
                "startup": {"min": 200000, "max": 350000, "description": "民营医院"}
            }
        }
    },
    "pharmacist": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["药师", "初级职称"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["主管药师"], "duration": "3-8年"},
            "senior": {"title": "高级", "positions": ["副主任药师", "主任药师"], "duration": "8年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 100000, "max": 180000, "description": "三甲医院"},
                "tier2": {"min": 70000, "max": 120000, "description": "药店/诊所"},
                "startup": {"min": 80000, "max": 150000, "description": "医药公司"}
            },
            "experienced_3y": {
                "tier1": {"min": 180000, "max": 300000, "description": "三甲医院"},
                "tier2": {"min": 120000, "max": 200000, "description": "药店/诊所"},
                "startup": {"min": 150000, "max": 250000, "description": "医药公司"}
            },
            "experienced_5y": {
                "tier1": {"min": 300000, "max": 500000, "description": "三甲医院"},
                "tier2": {"min": 200000, "max": 350000, "description": "药店/诊所"},
                "startup": {"min": 250000, "max": 450000, "description": "医药公司"}
            }
        }
    },
    "psychologist": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["心理咨询师", "助理咨询师"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["资深咨询师", "督导"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["首席咨询师", "心理治疗专家"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 100000, "max": 180000, "description": "医院/机构"},
                "tier2": {"min": 60000, "max": 120000, "description": "小型工作室"},
                "startup": {"min": 80000, "max": 150000, "description": "自由执业", "note": "按小时计费"}
            },
            "experienced_3y": {
                "tier1": {"min": 180000, "max": 350000, "description": "医院/机构"},
                "tier2": {"min": 120000, "max": 250000, "description": "小型工作室"},
                "startup": {"min": 150000, "max": 300000, "description": "自由执业", "note": "按小时计费"}
            },
            "experienced_5y": {
                "tier1": {"min": 350000, "max": 700000, "description": "医院/机构"},
                "tier2": {"min": 250000, "max": 500000, "description": "小型工作室"},
                "startup": {"min": 300000, "max": 800000, "description": "自由执业", "note": "顶级咨询师可达百万"}
            }
        }
    }
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in medical_career_salary:
        job['careerPath'] = medical_career_salary[job_id]['careerPath']
        job['salaryRange'] = medical_career_salary[job_id]['salaryRange']
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个医疗健康类岗位的薪资和职业路径数据")
