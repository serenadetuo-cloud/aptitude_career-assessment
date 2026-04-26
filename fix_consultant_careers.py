import json

# 读取岗位数据
with open('public/data/jobs-database.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 修复咨询类岗位的晋升路径
career_path_fixes = {
    '心理咨询师': {
        'junior': {'positions': ['心理咨询师', '初级心理咨询师'], 'duration': '0-3年'},
        'mid': {'positions': ['资深心理咨询师', '高级心理咨询师'], 'duration': '3-7年'},
        'senior': {'positions': ['督导级心理咨询师', '心理咨询专家'], 'duration': '7年以上'}
    },
    '教育咨询师': {
        'junior': {'positions': ['教育咨询师', '初级教育咨询师'], 'duration': '0-3年'},
        'mid': {'positions': ['资深教育咨询师', '高级教育咨询师'], 'duration': '3-7年'},
        'senior': {'positions': ['首席教育咨询师', '教育咨询专家'], 'duration': '7年以上'}
    }
}

# 修复岗位
fixed_count = 0
for job in data['jobs']:
    if job['jobName'] in career_path_fixes:
        job['careerPath'] = career_path_fixes[job['jobName']]
        fixed_count += 1
        print(f"✓ 修复 {job['jobName']}")

# 保存修复后的数据
with open('public/data/jobs-database.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n总共修复了 {fixed_count} 个咨询类岗位的晋升路径")
