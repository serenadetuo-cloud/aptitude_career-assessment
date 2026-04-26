import json

# 读取岗位数据
with open('public/data/jobs-database.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义需要添加专业要求的技术岗位
tech_job_major_requirements = {
    '数据分析师': ['cs', 'business', 'science'],  # 计算机、商科、理科都可以
    '软件工程师': ['cs'],
    '前端工程师': ['cs'],
    '后端工程师': ['cs'],
    '施工管理': ['engineering'],  # 需要工程背景
}

# 修复岗位
fixed_count = 0
for job in data['jobs']:
    if job['jobName'] in tech_job_major_requirements:
        old_majors = job['requiredMajors']
        job['requiredMajors'] = tech_job_major_requirements[job['jobName']]
        fixed_count += 1
        print(f"✓ 修复 {job['jobName']}: {old_majors} -> {job['requiredMajors']}")

# 保存修复后的数据
with open('public/data/jobs-database.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n总共修复了 {fixed_count} 个技术岗位的专业要求")
