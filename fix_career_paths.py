import json

# 读取岗位数据
with open('public/data/jobs-database.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义正确的晋升路径
career_path_fixes = {
    '护士': {
        'junior': {'positions': ['护士', '初级护士'], 'duration': '0-2年'},
        'mid': {'positions': ['护师', '主管护师'], 'duration': '3-5年'},
        'senior': {'positions': ['副主任护师', '主任护师'], 'duration': '6-10年+'}
    },
    '护士长': {
        'junior': {'positions': ['护士长', '病区护士长'], 'duration': '0-3年'},
        'mid': {'positions': ['护理部副主任', '护理部主任'], 'duration': '4-8年'},
        'senior': {'positions': ['总护士长', '护理部总监'], 'duration': '9-15年+'}
    },
    '插画师': {
        'junior': {'positions': ['插画师', '初级插画师'], 'duration': '0-2年'},
        'mid': {'positions': ['资深插画师', '高级插画师'], 'duration': '3-5年'},
        'senior': {'positions': ['首席插画师', '艺术总监'], 'duration': '6-10年+'}
    },
    '摄影师': {
        'junior': {'positions': ['摄影师', '摄影助理'], 'duration': '0-2年'},
        'mid': {'positions': ['资深摄影师', '高级摄影师'], 'duration': '3-5年'},
        'senior': {'positions': ['首席摄影师', '摄影总监'], 'duration': '6-10年+'}
    },
    '影视摄影师': {
        'junior': {'positions': ['影视摄影师', '摄影助理'], 'duration': '0-2年'},
        'mid': {'positions': ['摄影指导', '资深摄影师'], 'duration': '3-6年'},
        'senior': {'positions': ['首席摄影师', '视觉总监'], 'duration': '7-12年+'}
    },
    '作家/编剧': {
        'junior': {'positions': ['编剧助理', '初级编剧'], 'duration': '0-2年'},
        'mid': {'positions': ['编剧', '资深编剧'], 'duration': '3-6年'},
        'senior': {'positions': ['首席编剧', '文学策划'], 'duration': '7-12年+'}
    },
    '公务员': {
        'junior': {'positions': ['科员', '办事员'], 'duration': '0-3年'},
        'mid': {'positions': ['副科级', '正科级'], 'duration': '4-8年'},
        'senior': {'positions': ['副处级', '正处级'], 'duration': '9-15年+'}
    },
    '警察': {
        'junior': {'positions': ['警员', '四级警长'], 'duration': '0-3年'},
        'mid': {'positions': ['三级警长', '二级警长'], 'duration': '4-8年'},
        'senior': {'positions': ['一级警长', '三级警督'], 'duration': '9-15年+'}
    },
    '消防员': {
        'junior': {'positions': ['消防员', '四级消防士'], 'duration': '0-3年'},
        'mid': {'positions': ['三级消防士', '二级消防士'], 'duration': '4-8年'},
        'senior': {'positions': ['一级消防士', '消防指挥员'], 'duration': '9-15年+'}
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

print(f"\n总共修复了 {fixed_count} 个岗位的晋升路径")
