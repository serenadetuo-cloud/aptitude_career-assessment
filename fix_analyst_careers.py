import json

# 读取岗位数据
with open('public/data/jobs-database.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 修复分析师类岗位的晋升路径
career_path_fixes = {
    '数据分析师': {
        'junior': {'positions': ['数据分析师', '初级数据分析师'], 'duration': '0-3年'},
        'mid': {'positions': ['高级数据分析师', '资深数据分析师'], 'duration': '3-7年'},
        'senior': {'positions': ['数据分析专家', '数据分析总监'], 'duration': '7年以上'}
    },
    '战略分析师': {
        'junior': {'positions': ['战略分析师', '初级战略分析师'], 'duration': '0-3年'},
        'mid': {'positions': ['高级战略分析师', '资深战略分析师'], 'duration': '3-7年'},
        'senior': {'positions': ['战略分析专家', '战略总监'], 'duration': '7年以上'}
    },
    '商业分析师': {
        'junior': {'positions': ['商业分析师', '初级商业分析师'], 'duration': '0-3年'},
        'mid': {'positions': ['高级商业分析师', '资深商业分析师'], 'duration': '3-7年'},
        'senior': {'positions': ['商业分析专家', '商业分析总监'], 'duration': '7年以上'}
    }
}

# 修复岗位
fixed_count = 0
for job in data['jobs']:
    if job['jobName'] in career_path_fixes:
        old_path = job.get('careerPath', {})
        job['careerPath'] = career_path_fixes[job['jobName']]
        fixed_count += 1
        print(f"✓ 修复 {job['jobName']}")
        if 'senior' in old_path:
            print(f"  旧: {old_path['senior'].get('positions', [])}")
            print(f"  新: {job['careerPath']['senior']['positions']}")

# 保存修复后的数据
with open('public/data/jobs-database.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n总共修复了 {fixed_count} 个分析师岗位的晋升路径")
