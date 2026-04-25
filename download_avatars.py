#!/usr/bin/env python3
import json
import os
import urllib.request
import time

# 创建avatars目录
os.makedirs('public/avatars', exist_ok=True)

# 读取JSON文件
with open('public/data/career-mentors.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 下载所有头像
downloaded = 0
failed = []

for category_key, category_data in data['categories'].items():
    for mentor in category_data['mentors']:
        mentor_id = mentor['mentorId']
        avatar_url = mentor['avatar']

        # 跳过已经是本地路径的
        if avatar_url.startswith('/avatars/'):
            continue

        # 确定文件扩展名
        ext = '.jpg'
        if '.png' in avatar_url:
            ext = '.png'
        elif '.jpeg' in avatar_url:
            ext = '.jpeg'

        local_path = f'public/avatars/{mentor_id}{ext}'

        try:
            print(f"Downloading {mentor['name']} ({mentor_id})...")

            # 添加User-Agent避免被拒绝
            req = urllib.request.Request(
                avatar_url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )

            with urllib.request.urlopen(req, timeout=10) as response:
                with open(local_path, 'wb') as out_file:
                    out_file.write(response.read())

            # 更新JSON中的路径
            mentor['avatar'] = f'/avatars/{mentor_id}{ext}'
            downloaded += 1
            print(f"  ✓ Saved to {local_path}")

            # 避免请求过快
            time.sleep(0.5)

        except Exception as e:
            print(f"  ✗ Failed: {e}")
            failed.append((mentor['name'], avatar_url, str(e)))

# 写回JSON文件
with open('public/data/career-mentors.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Downloaded {downloaded} avatars")
if failed:
    print(f"\n❌ Failed to download {len(failed)} avatars:")
    for name, url, error in failed:
        print(f"  - {name}: {error}")
