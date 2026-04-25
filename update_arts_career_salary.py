#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为文化艺术类岗位补充真实的薪资和职业路径数据
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义文化艺术类岗位的真实薪资和职业路径
arts_career_salary = {
    "illustrator": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["插画助理", "初级插画师"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["插画师", "资深插画师"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["首席插画师", "艺术总监"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 120000, "max": 200000, "description": "一线大厂/知名工作室"},
                "tier2": {"min": 80000, "max": 150000, "description": "二线公司"},
                "startup": {"min": 100000, "max": 180000, "description": "创业公司/自由职业"}
            },
            "experienced_3y": {
                "tier1": {"min": 200000, "max": 350000, "description": "一线大厂/知名工作室"},
                "tier2": {"min": 150000, "max": 250000, "description": "二线公司"},
                "startup": {"min": 180000, "max": 300000, "description": "创业公司/自由职业"}
            },
            "experienced_5y": {
                "tier1": {"min": 350000, "max": 600000, "description": "一线大厂/知名工作室"},
                "tier2": {"min": 250000, "max": 450000, "description": "二线公司"},
                "startup": {"min": 300000, "max": 500000, "description": "创业公司/自由职业", "note": "顶级插画师可达百万"}
            }
        }
    },
    "writer_screenwriter": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["编剧助理", "初级编剧"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["编剧", "资深编剧"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["金牌编剧", "总编剧"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 100000, "max": 180000, "description": "影视公司/平台"},
                "tier2": {"min": 60000, "max": 120000, "description": "小型工作室"},
                "startup": {"min": 80000, "max": 150000, "description": "自由撰稿", "note": "按项目计费"}
            },
            "experienced_3y": {
                "tier1": {"min": 180000, "max": 400000, "description": "影视公司/平台"},
                "tier2": {"min": 120000, "max": 250000, "description": "小型工作室"},
                "startup": {"min": 150000, "max": 350000, "description": "自由撰稿", "note": "按项目计费"}
            },
            "experienced_5y": {
                "tier1": {"min": 400000, "max": 1000000, "description": "影视公司/平台"},
                "tier2": {"min": 250000, "max": 500000, "description": "小型工作室"},
                "startup": {"min": 350000, "max": 800000, "description": "自由撰稿", "note": "顶级编剧可达千万"}
            }
        }
    },
    "graphic_designer": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["设计助理", "初级设计师"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["设计师", "资深设计师"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["设计总监", "创意总监"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 150000, "max": 250000, "description": "一线互联网/4A广告"},
                "tier2": {"min": 100000, "max": 180000, "description": "二线公司"},
                "startup": {"min": 120000, "max": 200000, "description": "创业公司/工作室"}
            },
            "experienced_3y": {
                "tier1": {"min": 250000, "max": 450000, "description": "一线互联网/4A广告"},
                "tier2": {"min": 180000, "max": 300000, "description": "二线公司"},
                "startup": {"min": 200000, "max": 350000, "description": "创业公司/工作室"}
            },
            "experienced_5y": {
                "tier1": {"min": 450000, "max": 800000, "description": "一线互联网/4A广告"},
                "tier2": {"min": 300000, "max": 550000, "description": "二线公司"},
                "startup": {"min": 350000, "max": 650000, "description": "创业公司/工作室"}
            }
        }
    },
    "photographer": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["摄影助理", "初级摄影师"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["摄影师", "资深摄影师"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["首席摄影师", "摄影总监"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 100000, "max": 180000, "description": "知名工作室/媒体"},
                "tier2": {"min": 60000, "max": 120000, "description": "小型工作室"},
                "startup": {"min": 80000, "max": 150000, "description": "自由摄影师", "note": "按项目计费"}
            },
            "experienced_3y": {
                "tier1": {"min": 180000, "max": 350000, "description": "知名工作室/媒体"},
                "tier2": {"min": 120000, "max": 250000, "description": "小型工作室"},
                "startup": {"min": 150000, "max": 300000, "description": "自由摄影师", "note": "按项目计费"}
            },
            "experienced_5y": {
                "tier1": {"min": 350000, "max": 700000, "description": "知名工作室/媒体"},
                "tier2": {"min": 250000, "max": 450000, "description": "小型工作室"},
                "startup": {"min": 300000, "max": 600000, "description": "自由摄影师", "note": "顶级摄影师可达百万"}
            }
        }
    },
    "video_editor": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["剪辑助理", "初级剪辑师"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["剪辑师", "资深剪辑师"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["首席剪辑师", "后期总监"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 120000, "max": 200000, "description": "影视公司/平台"},
                "tier2": {"min": 80000, "max": 150000, "description": "小型工作室"},
                "startup": {"min": 100000, "max": 180000, "description": "自由剪辑师"}
            },
            "experienced_3y": {
                "tier1": {"min": 200000, "max": 400000, "description": "影视公司/平台"},
                "tier2": {"min": 150000, "max": 280000, "description": "小型工作室"},
                "startup": {"min": 180000, "max": 350000, "description": "自由剪辑师"}
            },
            "experienced_5y": {
                "tier1": {"min": 400000, "max": 800000, "description": "影视公司/平台"},
                "tier2": {"min": 280000, "max": 500000, "description": "小型工作室"},
                "startup": {"min": 350000, "max": 700000, "description": "自由剪辑师"}
            }
        }
    },
    "social_media_operator": {
        "careerPath": {
            "junior": {"title": "初级", "positions": ["新媒体专员", "内容运营"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["新媒体主管", "高级运营"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["新媒体总监", "内容负责人"], "duration": "7年以上"}
        },
        "salaryRange": {
            "freshGraduate": {
                "tier1": {"min": 120000, "max": 200000, "description": "一线互联网"},
                "tier2": {"min": 80000, "max": 150000, "description": "二线公司"},
                "startup": {"min": 100000, "max": 180000, "description": "创业公司"}
            },
            "experienced_3y": {
                "tier1": {"min": 200000, "max": 400000, "description": "一线互联网"},
                "tier2": {"min": 150000, "max": 280000, "description": "二线公司"},
                "startup": {"min": 180000, "max": 350000, "description": "创业公司"}
            },
            "experienced_5y": {
                "tier1": {"min": 400000, "max": 800000, "description": "一线互联网"},
                "tier2": {"min": 280000, "max": 500000, "description": "二线公司"},
                "startup": {"min": 350000, "max": 650000, "description": "创业公司"}
            }
        }
    }
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in arts_career_salary:
        job['careerPath'] = arts_career_salary[job_id]['careerPath']
        job['salaryRange'] = arts_career_salary[job_id]['salaryRange']
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个文化艺术类岗位的薪资和职业路径数据")
