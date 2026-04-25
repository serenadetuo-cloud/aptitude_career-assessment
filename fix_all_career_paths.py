#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复所有使用通用模板的岗位的职业路径数据
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义所有岗位的真实职业路径
career_paths = {
    # 商业服务类
    "product_manager": {
        "junior": {"title": "初级", "positions": ["产品助理", "初级产品经理"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["产品经理", "高级产品经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["产品总监", "首席产品官"], "duration": "7年以上"}
    },
    "user_growth": {
        "junior": {"title": "初级", "positions": ["增长专员", "用户运营"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["增长经理", "高级增长经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["增长总监", "CGO"], "duration": "7年以上"}
    },
    "user_operations": {
        "junior": {"title": "初级", "positions": ["运营专员", "用户运营"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["运营经理", "高级运营经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["运营总监", "COO"], "duration": "7年以上"}
    },
    "content_operations": {
        "junior": {"title": "初级", "positions": ["内容编辑", "内容运营"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["内容经理", "高级内容经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["内容总监", "内容负责人"], "duration": "7年以上"}
    },
    "data_analyst": {
        "junior": {"title": "初级", "positions": ["数据分析师", "初级分析师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级数据分析师", "数据专家"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["数据分析总监", "首席数据官"], "duration": "7年以上"}
    },
    "ui_designer": {
        "junior": {"title": "初级", "positions": ["UI设计师", "视觉设计师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级UI设计师", "资深设计师"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["设计总监", "创意总监"], "duration": "7年以上"}
    },
    "ux_designer": {
        "junior": {"title": "初级", "positions": ["UX设计师", "交互设计师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级UX设计师", "资深设计师"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["UX总监", "设计负责人"], "duration": "7年以上"}
    },
    "frontend_engineer": {
        "junior": {"title": "初级", "positions": ["前端工程师", "初级工程师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级前端工程师", "前端专家"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["前端架构师", "技术总监"], "duration": "7年以上"}
    },
    "backend_engineer": {
        "junior": {"title": "初级", "positions": ["后端工程师", "初级工程师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级后端工程师", "后端专家"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["后端架构师", "技术总监"], "duration": "7年以上"}
    },
    "sales_manager": {
        "junior": {"title": "初级", "positions": ["销售代表", "客户经理"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["销售经理", "高级销售经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["销售总监", "VP销售"], "duration": "7年以上"}
    },
    "bd": {
        "junior": {"title": "初级", "positions": ["BD专员", "商务拓展"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["BD经理", "高级BD经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["BD总监", "VP商务"], "duration": "7年以上"}
    },
    "csm": {
        "junior": {"title": "初级", "positions": ["客户成功专员", "CSM"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["客户成功经理", "高级CSM"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["客户成功总监", "VP客户成功"], "duration": "7年以上"}
    },
    "channel_manager": {
        "junior": {"title": "初级", "positions": ["渠道专员", "渠道经理"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级渠道经理", "渠道总监"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["渠道VP", "合作伙伴负责人"], "duration": "7年以上"}
    },
    "marketing_manager": {
        "junior": {"title": "初级", "positions": ["市场专员", "营销专员"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["市场经理", "高级市场经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["市场总监", "CMO"], "duration": "7年以上"}
    },
    "brand_manager": {
        "junior": {"title": "初级", "positions": ["品牌专员", "品牌经理"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级品牌经理", "品牌总监"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["品牌VP", "首席品牌官"], "duration": "7年以上"}
    },
    "digital_marketing": {
        "junior": {"title": "初级", "positions": ["数字营销专员", "投放专员"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["数字营销经理", "投放经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["数字营销总监", "增长营销负责人"], "duration": "7年以上"}
    },
    "pr": {
        "junior": {"title": "初级", "positions": ["公关专员", "PR专员"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["公关经理", "高级PR经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["公关总监", "VP公关"], "duration": "7年以上"}
    },
    "consultant": {
        "junior": {"title": "初级", "positions": ["咨询顾问", "分析师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级咨询顾问", "项目经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["合伙人", "董事总经理"], "duration": "7年以上"}
    },
    "strategy_analyst": {
        "junior": {"title": "初级", "positions": ["战略分析师", "分析师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级战略分析师", "战略经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["战略总监", "首席战略官"], "duration": "7年以上"}
    },
    "business_analyst": {
        "junior": {"title": "初级", "positions": ["商业分析师", "业务分析师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级商业分析师", "分析经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["分析总监", "首席分析官"], "duration": "7年以上"}
    },
    "investment_analyst": {
        "junior": {"title": "初级", "positions": ["投资分析师", "研究员"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级投资分析师", "投资经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["投资总监", "合伙人"], "duration": "7年以上"}
    },
    "financial_advisor": {
        "junior": {"title": "初级", "positions": ["理财顾问", "客户经理"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["高级理财顾问", "财富管理经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["财富管理总监", "私人银行家"], "duration": "7年以上"}
    },
    "risk_control": {
        "junior": {"title": "初级", "positions": ["风控专员", "风险分析师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["风控经理", "高级风控经理"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["风控总监", "首席风险官"], "duration": "7年以上"}
    },
    "hr": {
        "junior": {"title": "初级", "positions": ["HR专员", "招聘专员"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["HR经理", "HRBP"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["HR总监", "CHO"], "duration": "7年以上"}
    },
    "accountant": {
        "junior": {"title": "初级", "positions": ["会计", "财务专员"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["财务经理", "高级会计师"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["财务总监", "CFO"], "duration": "7年以上"}
    },

    # 文化艺术类
    "industrial_designer": {
        "junior": {"title": "初级", "positions": ["设计助理", "初级工业设计师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["工业设计师", "资深设计师"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["首席设计师", "设计总监"], "duration": "7年以上"}
    },
    "fashion_designer": {
        "junior": {"title": "初级", "positions": ["设计助理", "初级服装设计师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["服装设计师", "资深设计师"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["首席设计师", "创意总监"], "duration": "7年以上"}
    },
    "interior_designer": {
        "junior": {"title": "初级", "positions": ["设计助理", "初级室内设计师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["室内设计师", "资深设计师"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["首席设计师", "设计总监"], "duration": "7年以上"}
    },
    "animator": {
        "junior": {"title": "初级", "positions": ["动画助理", "初级动画师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["动画师", "资深动画师"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["首席动画师", "动画总监"], "duration": "7年以上"}
    },
    "director": {
        "junior": {"title": "初级", "positions": ["导演助理", "副导演"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["导演", "资深导演"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["知名导演", "制片人"], "duration": "7年以上"}
    },
    "cinematographer": {
        "junior": {"title": "初级", "positions": ["摄影助理", "摄影师"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["摄影指导", "资深摄影师"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["首席摄影师", "摄影总监"], "duration": "7年以上"}
    },
    "writer_screenwriter": {
        "junior": {"title": "初级", "positions": ["编剧助理", "初级编剧"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["编剧", "资深编剧"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["金牌编剧", "总编剧"], "duration": "7年以上"}
    },
    "copywriter": {
        "junior": {"title": "初级", "positions": ["文案", "初级文案策划"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["文案策划", "资深文案"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["创意总监", "首席文案"], "duration": "7年以上"}
    },
    "journalist": {
        "junior": {"title": "初级", "positions": ["实习记者", "记者"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["资深记者", "主任记者"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["首席记者", "总编辑"], "duration": "7年以上"}
    },
    "editor": {
        "junior": {"title": "初级", "positions": ["编辑助理", "编辑"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["资深编辑", "主编"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["总编辑", "出版人"], "duration": "7年以上"}
    },
    "social_media_operator": {
        "junior": {"title": "初级", "positions": ["新媒体专员", "内容运营"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["新媒体主管", "高级运营"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["新媒体总监", "内容负责人"], "duration": "7年以上"}
    },
    "actor": {
        "junior": {"title": "初级", "positions": ["群众演员", "配角演员"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["主要演员", "实力派演员"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["知名演员", "影帝/影后"], "duration": "7年以上"}
    },
    "host": {
        "junior": {"title": "初级", "positions": ["主持人助理", "实习主持人"], "duration": "0-3年"},
        "mid": {"title": "中级", "positions": ["主持人", "资深主持人"], "duration": "3-7年"},
        "senior": {"title": "高级", "positions": ["知名主持人", "首席主持人"], "duration": "7年以上"}
    }
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in career_paths:
        job['careerPath'] = career_paths[job_id]
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个岗位的职业路径数据")
