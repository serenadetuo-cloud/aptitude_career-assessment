#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动生成所有岗位的职业路径
根据岗位名称和类别智能生成合理的职业发展路径
"""

import json
import re

# 读取岗位数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def generate_career_path(job_name, job_id, category):
    """根据岗位名称生成职业路径"""

    # 提取岗位核心词
    core_name = job_name

    # 根据岗位类型生成路径
    if '工程师' in job_name or '开发' in job_name:
        return {
            "junior": {
                "title": "初级",
                "positions": [f"初级{core_name}", f"{core_name}"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"高级{core_name}", f"资深{core_name}"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": [f"{core_name.replace('工程师', '架构师')}", "技术总监"],
                "duration": "7年以上"
            }
        }

    elif '设计师' in job_name:
        return {
            "junior": {
                "title": "初级",
                "positions": [f"初级{core_name}", f"{core_name}"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"高级{core_name}", f"资深{core_name}"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": ["首席设计师", "设计总监"],
                "duration": "7年以上"
            }
        }

    elif '经理' in job_name or '管理' in job_name:
        base = job_name.replace('经理', '').replace('管理', '')
        return {
            "junior": {
                "title": "初级",
                "positions": [f"{base}专员", f"{base}经理"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"高级{base}经理", f"{base}高级经理"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": [f"{base}总监", f"{base}VP"],
                "duration": "7年以上"
            }
        }

    elif '运营' in job_name:
        base = job_name.replace('运营', '')
        return {
            "junior": {
                "title": "初级",
                "positions": [f"{base}运营专员", f"{base}运营"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"{base}运营经理", f"高级{base}运营"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": [f"{base}运营总监", "COO"],
                "duration": "7年以上"
            }
        }

    elif '医生' in job_name or '医师' in job_name:
        specialty = job_name.replace('医生', '').replace('医师', '')
        return {
            "junior": {
                "title": "初级",
                "positions": [f"{specialty}住院医师", f"{specialty}医师"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"{specialty}主治医师", f"{specialty}副主任医师"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": [f"{specialty}主任医师", "科室主任"],
                "duration": "7年以上"
            }
        }

    elif '教师' in job_name:
        subject = job_name.replace('教师', '')
        return {
            "junior": {
                "title": "初级",
                "positions": [f"{subject}教师", f"初级{subject}教师"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"骨干{subject}教师", f"高级{subject}教师"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": [f"特级{subject}教师", "教研组长"],
                "duration": "7年以上"
            }
        }

    elif '师' in job_name and '工程师' not in job_name:
        # 护士、药剂师、营养师等
        return {
            "junior": {
                "title": "初级",
                "positions": [f"{core_name}", f"初级{core_name}"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"主管{core_name}", f"高级{core_name}"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": [f"{core_name}长", f"{core_name}主任"],
                "duration": "7年以上"
            }
        }

    elif '专员' in job_name:
        base = job_name.replace('专员', '')
        return {
            "junior": {
                "title": "初级",
                "positions": [f"{base}专员", f"初级{base}专员"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"{base}经理", f"高级{base}经理"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": [f"{base}总监", f"{base}VP"],
                "duration": "7年以上"
            }
        }

    elif '分析师' in job_name or '顾问' in job_name:
        base = job_name.replace('分析师', '').replace('顾问', '')
        return {
            "junior": {
                "title": "初级",
                "positions": [f"{base}分析师", f"初级{base}顾问"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"高级{base}分析师", f"{base}经理"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": [f"{base}总监", "合伙人"],
                "duration": "7年以上"
            }
        }

    elif '研究员' in job_name:
        field = job_name.replace('研究员', '')
        return {
            "junior": {
                "title": "初级",
                "positions": [f"{field}研究助理", f"{field}研究员"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"副{field}研究员", f"高级{field}研究员"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": [f"首席{field}研究员", "研究所所长"],
                "duration": "7年以上"
            }
        }

    elif '创业者' in job_name:
        field = job_name.replace('创业者', '')
        return {
            "junior": {
                "title": "初级",
                "positions": [f"{field}创业者", "初创团队"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": ["成长期创业者", "连续创业者"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": ["成功创业者", "天使投资人"],
                "duration": "7年以上"
            }
        }

    # 特殊岗位
    elif job_name == '演员':
        return {
            "junior": {"title": "初级", "positions": ["群众演员", "配角演员"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["主要演员", "实力派演员"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["知名演员", "影帝/影后"], "duration": "7年以上"}
        }

    elif job_name == '主持人':
        return {
            "junior": {"title": "初级", "positions": ["主持人助理", "实习主持人"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["主持人", "资深主持人"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["知名主持人", "首席主持人"], "duration": "7年以上"}
        }

    elif job_name == '导演':
        return {
            "junior": {"title": "初级", "positions": ["导演助理", "副导演"], "duration": "0-3年"},
            "mid": {"title": "中级", "positions": ["导演", "资深导演"], "duration": "3-7年"},
            "senior": {"title": "高级", "positions": ["知名导演", "制片人"], "duration": "7年以上"}
        }

    # 默认通用路径
    else:
        return {
            "junior": {
                "title": "初级",
                "positions": [f"初级{core_name}", f"{core_name}"],
                "duration": "0-3年"
            },
            "mid": {
                "title": "中级",
                "positions": [f"高级{core_name}", f"资深{core_name}"],
                "duration": "3-7年"
            },
            "senior": {
                "title": "高级",
                "positions": [f"首席{core_name}", f"{core_name}总监"],
                "duration": "7年以上"
            }
        }

# 更新所有岗位
updated_count = 0
for job in data['jobs']:
    career_path = generate_career_path(job['jobName'], job['jobId'], job['category'])
    job['careerPath'] = career_path
    updated_count += 1
    print(f"✓ {job['jobName']}: {career_path['junior']['positions'][0]} → {career_path['mid']['positions'][0]} → {career_path['senior']['positions'][0]}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已为 {updated_count} 个岗位生成职业路径")
