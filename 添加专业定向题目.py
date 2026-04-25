#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
添加专业定向题目:根据用户专业背景显示不同的深度题目
"""

import json

# 读取现有题库
with open('public/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义专业定向题目
major_specific_questions = [
    # 医学专业定向题
    {
        "questionId": 39,
        "questionCategory": "医学专业 - 职业方向",
        "questionText": "在医学领域,你更倾向于?",
        "questionType": "single_choice",
        "requiredMajors": ["major_medical"],
        "options": [
            {
                "optionId": "A",
                "optionText": "临床一线,直接接触患者,诊断治疗",
                "scoring": {"医疗健康": 6}
            },
            {
                "optionId": "B",
                "optionText": "医学研究,探索疾病机理和新疗法",
                "scoring": {"科研创新": 5, "医疗健康": 4}
            },
            {
                "optionId": "C",
                "optionText": "公共卫生,预防医学和健康管理",
                "scoring": {"医疗健康": 4, "公共服务": 4}
            },
            {
                "optionId": "D",
                "optionText": "医疗器械/药物研发,用技术改善医疗",
                "scoring": {"医疗健康": 4, "工程制造": 3}
            }
        ]
    },

    # 计算机专业定向题
    {
        "questionId": 40,
        "questionCategory": "计算机专业 - 技术方向",
        "questionText": "在技术领域,你更感兴趣的是?",
        "questionType": "single_choice",
        "requiredMajors": ["major_cs"],
        "options": [
            {
                "optionId": "A",
                "optionText": "前端开发,做用户能看到的界面和交互",
                "scoring": {"商业服务": 4, "文化艺术": 2}
            },
            {
                "optionId": "B",
                "optionText": "后端架构,设计系统和处理复杂业务逻辑",
                "scoring": {"商业服务": 4, "工程制造": 3}
            },
            {
                "optionId": "C",
                "optionText": "算法/AI,研究机器学习和智能系统",
                "scoring": {"科研创新": 6, "工程制造": 2}
            },
            {
                "optionId": "D",
                "optionText": "产品技术,用技术解决用户问题",
                "scoring": {"商业服务": 5, "自主创业": 2}
            }
        ]
    },

    # 艺术设计专业定向题
    {
        "questionId": 41,
        "questionCategory": "艺术专业 - 创作方向",
        "questionText": "在设计/艺术领域,你更擅长?",
        "questionType": "single_choice",
        "requiredMajors": ["major_art"],
        "options": [
            {
                "optionId": "A",
                "optionText": "视觉设计,平面/UI/品牌等视觉表达",
                "scoring": {"文化艺术": 6}
            },
            {
                "optionId": "B",
                "optionText": "交互设计,关注用户体验和产品逻辑",
                "scoring": {"文化艺术": 4, "商业服务": 3}
            },
            {
                "optionId": "C",
                "optionText": "动画/影视,用动态影像讲故事",
                "scoring": {"文化艺术": 6}
            },
            {
                "optionId": "D",
                "optionText": "工业/产品设计,设计实体产品",
                "scoring": {"文化艺术": 4, "工程制造": 3}
            }
        ]
    },

    # 教育专业定向题
    {
        "questionId": 42,
        "questionCategory": "教育专业 - 教学方向",
        "questionText": "在教育领域,你更想做?",
        "questionType": "single_choice",
        "requiredMajors": ["major_education"],
        "options": [
            {
                "optionId": "A",
                "optionText": "学科教学,成为某个学科的优秀教师",
                "scoring": {"教育培训": 6}
            },
            {
                "optionId": "B",
                "optionText": "教育研究,探索更好的教学方法和理论",
                "scoring": {"教育培训": 4, "科研创新": 4}
            },
            {
                "optionId": "C",
                "optionText": "教育产品,用技术改善教育体验",
                "scoring": {"教育培训": 4, "商业服务": 3}
            },
            {
                "optionId": "D",
                "optionText": "教育管理,推动学校或机构的发展",
                "scoring": {"教育培训": 4, "公共服务": 3}
            }
        ]
    },

    # 工程专业定向题
    {
        "questionId": 43,
        "questionCategory": "工程专业 - 工程方向",
        "questionText": "在工程领域,你更倾向于?",
        "questionType": "single_choice",
        "requiredMajors": ["major_engineering"],
        "options": [
            {
                "optionId": "A",
                "optionText": "产品研发,设计和开发新产品",
                "scoring": {"工程制造": 6}
            },
            {
                "optionId": "B",
                "optionText": "工艺优化,提升生产效率和质量",
                "scoring": {"工程制造": 5, "商业服务": 2}
            },
            {
                "optionId": "C",
                "optionText": "技术研究,探索新材料新技术",
                "scoring": {"科研创新": 5, "工程制造": 3}
            },
            {
                "optionId": "D",
                "optionText": "项目管理,协调资源推动工程落地",
                "scoring": {"工程制造": 3, "商业服务": 4}
            }
        ]
    }
]

# 添加专业定向题目
data['questions'].extend(major_specific_questions)
print(f"✓ 新增了 {len(major_specific_questions)} 道专业定向题目")

# 更新元数据
data['meta']['totalQuestions'] = len(data['questions'])

# 保存
with open('public/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！")
print(f"  最终题目数: {len(data['questions'])} 道")
print(f"  其中专业定向题: {len(major_specific_questions)} 道")
print(f"\n专业定向题分布:")
for q in major_specific_questions:
    majors = ', '.join(q['requiredMajors'])
    print(f"  Q{q['questionId']}: {q['questionText'][:30]}... (需要: {majors})")
