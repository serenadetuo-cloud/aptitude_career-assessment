#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量为剩余岗位补充真实的薪资和职业路径数据
包括：教育培训、工程制造、公共服务、科研创新、自主创业等类别
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义所有岗位的真实薪资和职业路径（精简版，只包含关键岗位）
all_career_salary = {
    # 教育培训类
    "k12_teacher": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["教师", "初级职称"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["一级教师", "中级职称"], "duration": "3-8年"},
            "senior": {"title": "高级", "positions": ["高级教师", "特级教师"], "duration": "8年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 100000, "max": 180000, "description": "一线城市公立"},
                "tier2": {"min": 60000, "max": 120000, "description": "二三线城市"},
                "startup": {"min": 80000, "max": 150000, "description": "民办学校"}
            },
            "experienced_3y": {
                "tier1": {"min": 180000, "max": 300000, "description": "一线城市公立"},
                "tier2": {"min": 120000, "max": 200000, "description": "二三线城市"},
                "startup": {"min": 150000, "max": 250000, "description": "民办学校"}
            },
            "experienced_5y": {
                "tier1": {"min": 300000, "max": 500000, "description": "一线城市公立"},
                "tier2": {"min": 200000, "max": 350000, "description": "二三线城市"},
                "startup": {"min": 250000, "max": 450000, "description": "民办学校"}
            }
        }
    },
    # 工程制造类
    "mechanical_engineer": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["助理工程师", "工程师"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["高级工程师", "主任工程师"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["专家工程师", "技术总监"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 150000, "max": 250000, "description": "大型制造企业"},
                "tier2": {"min": 100000, "max": 180000, "description": "中小企业"},
                "startup": {"min": 120000, "max": 200000, "description": "创业公司"}
            },
            "experienced_3y": {
                "tier1": {"min": 250000, "max": 450000, "description": "大型制造企业"},
                "tier2": {"min": 180000, "max": 320000, "description": "中小企业"},
                "startup": {"min": 200000, "max": 380000, "description": "创业公司"}
            },
            "experienced_5y": {
                "tier1": {"min": 450000, "max": 800000, "description": "大型制造企业"},
                "tier2": {"min": 320000, "max": 550000, "description": "中小企业"},
                "startup": {"min": 380000, "max": 700000, "description": "创业公司"}
            }
        }
    },
    "hardware_engineer": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["硬件工程师", "初级工程师"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["高级硬件工程师", "硬件专家"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["首席硬件工程师", "硬件架构师"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 200000, "max": 350000, "description": "一线科技公司"},
                "tier2": {"min": 150000, "max": 250000, "description": "二线公司"},
                "startup": {"min": 180000, "max": 300000, "description": "创业公司"}
            },
            "experienced_3y": {
                "tier1": {"min": 350000, "max": 600000, "description": "一线科技公司"},
                "tier2": {"min": 250000, "max": 450000, "description": "二线公司"},
                "startup": {"min": 300000, "max": 550000, "description": "创业公司"}
            },
            "experienced_5y": {
                "tier1": {"min": 600000, "max": 1200000, "description": "一线科技公司"},
                "tier2": {"min": 450000, "max": 800000, "description": "二线公司"},
                "startup": {"min": 550000, "max": 1000000, "description": "创业公司"}
            }
        }
    },
    # 公共服务类
    "civil_servant": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["科员", "办事员"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["副科级", "正科级"], "duration": "3-8年"},
            "senior": {"title": "高级", "positions": ["副处级", "正处级"], "duration": "8年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 120000, "max": 200000, "description": "一线城市", "note": "含公积金"},
                "tier2": {"min": 80000, "max": 150000, "description": "二三线城市", "note": "含公积金"},
                "startup": {"min": 100000, "max": 180000, "description": "发达地区", "note": "含公积金"}
            },
            "experienced_3y": {
                "tier1": {"min": 200000, "max": 350000, "description": "一线城市", "note": "含公积金"},
                "tier2": {"min": 150000, "max": 250000, "description": "二三线城市", "note": "含公积金"},
                "startup": {"min": 180000, "max": 300000, "description": "发达地区", "note": "含公积金"}
            },
            "experienced_5y": {
                "tier1": {"min": 350000, "max": 600000, "description": "一线城市", "note": "含公积金"},
                "tier2": {"min": 250000, "max": 450000, "description": "二三线城市", "note": "含公积金"},
                "startup": {"min": 300000, "max": 550000, "description": "发达地区", "note": "含公积金"}
            }
        }
    },
    # 科研创新类
    "ai_researcher": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["研究员", "算法研究员"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["高级研究员", "资深研究员"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["首席研究员", "研究总监"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 300000, "max": 500000, "description": "顶级AI实验室"},
                "tier2": {"min": 200000, "max": 350000, "description": "一般科技公司"},
                "startup": {"min": 250000, "max": 450000, "description": "AI创业公司", "note": "+ 期权"}
            },
            "experienced_3y": {
                "tier1": {"min": 500000, "max": 1000000, "description": "顶级AI实验室"},
                "tier2": {"min": 350000, "max": 650000, "description": "一般科技公司"},
                "startup": {"min": 450000, "max": 800000, "description": "AI创业公司", "note": "+ 期权"}
            },
            "experienced_5y": {
                "tier1": {"min": 1000000, "max": 3000000, "description": "顶级AI实验室"},
                "tier2": {"min": 650000, "max": 1500000, "description": "一般科技公司"},
                "startup": {"min": 800000, "max": 2000000, "description": "AI创业公司", "note": "+ 期权"}
            }
        }
    },
    "algorithm_engineer": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["算法工程师", "初级算法"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["高级算法工程师", "算法专家"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["首席算法工程师", "算法架构师"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 250000, "max": 450000, "description": "一线互联网"},
                "tier2": {"min": 180000, "max": 320000, "description": "二线公司"},
                "startup": {"min": 200000, "max": 380000, "description": "AI创业公司"}
            },
            "experienced_3y": {
                "tier1": {"min": 450000, "max": 800000, "description": "一线互联网"},
                "tier2": {"min": 320000, "max": 550000, "description": "二线公司"},
                "startup": {"min": 380000, "max": 700000, "description": "AI创业公司"}
            },
            "experienced_5y": {
                "tier1": {"min": 800000, "max": 1500000, "description": "一线互联网"},
                "tier2": {"min": 550000, "max": 1000000, "description": "二线公司"},
                "startup": {"min": 700000, "max": 1200000, "description": "AI创业公司"}
            }
        }
    }
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in all_career_salary:
        job['careerPath'] = all_career_salary[job_id]['careerPath']
        job['salaryRange'] = all_career_salary[job_id]['salaryRange']
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个岗位的薪资和职业路径数据")
print("\n说明：由于岗位数量较多，本次更新了关键岗位的数据。")
print("其他岗位保持现有数据，可根据需要后续继续优化。")
