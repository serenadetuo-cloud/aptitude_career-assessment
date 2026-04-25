#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为岗位库补充真实的 typicalDay 数据
"""

import json

# 读取现有数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义各岗位的真实 typicalDay 数据
typical_day_data = {
    "illustrator": [
        {"time": "09:00-10:00", "activity": "查看客户反馈，确认今天要修改的插画细节"},
        {"time": "10:00-12:00", "activity": "绘制新项目的草图，尝试3种不同的构图方案"},
        {"time": "14:00-16:00", "activity": "用数位板细化选定的方案，调整色彩和光影"},
        {"time": "16:00-17:00", "activity": "导出作品发给客户，讨论修改意见"},
        {"time": "17:00-18:00", "activity": "浏览Behance和Pinterest，收集灵感素材"}
    ],
    "writer_screenwriter": [
        {"time": "09:00-10:00", "activity": "回顾昨天写的剧本大纲，调整人物关系线"},
        {"time": "10:00-12:00", "activity": "专注写作，完成第3场戏的对话和场景描述"},
        {"time": "14:00-16:00", "activity": "和导演开会，讨论剧本的节奏和冲突点"},
        {"time": "16:00-17:00", "activity": "根据反馈修改第1-2场戏，强化主角动机"},
        {"time": "17:00-18:00", "activity": "阅读相关题材的书籍和影视作品，积累素材"}
    ],
    "graphic_designer": [
        {"time": "09:00-10:00", "activity": "查看项目进度，确认今天要交付的设计稿"},
        {"time": "10:00-12:00", "activity": "设计品牌VI系统，尝试5种logo方案"},
        {"time": "14:00-16:00", "activity": "制作海报和宣传物料，调整排版和视觉层次"},
        {"time": "16:00-17:00", "activity": "和客户开会，展示设计方案并收集反馈"},
        {"time": "17:00-18:00", "activity": "学习新的设计趋势和软件技巧"}
    ],
    "industrial_designer": [
        {"time": "09:00-10:00", "activity": "研究用户调研报告，提取产品设计需求"},
        {"time": "10:00-12:00", "activity": "用Rhino建模，设计产品的外观和结构"},
        {"time": "14:00-16:00", "activity": "和工程师讨论可制造性，调整设计方案"},
        {"time": "16:00-17:00", "activity": "制作渲染图和设计说明文档"},
        {"time": "17:00-18:00", "activity": "参观展览或工厂，了解材料和工艺"}
    ],
    "fashion_designer": [
        {"time": "09:00-10:00", "activity": "查看面料样品，确认本季服装的材质选择"},
        {"time": "10:00-12:00", "activity": "绘制服装设计图，设计新系列的款式和细节"},
        {"time": "14:00-16:00", "activity": "和打版师沟通，调整样衣的版型和尺寸"},
        {"time": "16:00-17:00", "activity": "试穿样衣，检查穿着效果和舒适度"},
        {"time": "17:00-18:00", "activity": "关注时尚周和潮流趋势，收集灵感"}
    ],
    "interior_designer": [
        {"time": "09:00-10:00", "activity": "和客户沟通，了解空间需求和预算"},
        {"time": "10:00-12:00", "activity": "用CAD绘制平面布局图，规划动线和功能分区"},
        {"time": "14:00-16:00", "activity": "选择家具、灯具和材料，制作材料板"},
        {"time": "16:00-17:00", "activity": "用3ds Max制作效果图，展示设计方案"},
        {"time": "17:00-18:00", "activity": "去建材市场或家具展厅，了解新产品"}
    ],
    "photographer": [
        {"time": "09:00-10:00", "activity": "和客户确认拍摄需求，准备拍摄清单"},
        {"time": "10:00-12:00", "activity": "布置拍摄场景，调试灯光和相机参数"},
        {"time": "14:00-16:00", "activity": "执行拍摄，指导模特姿势和表情"},
        {"time": "16:00-17:00", "activity": "用Lightroom筛选照片，挑选最佳作品"},
        {"time": "17:00-18:00", "activity": "用Photoshop精修照片，调整色调和细节"}
    ],
    "animator": [
        {"time": "09:00-10:00", "activity": "查看导演反馈，确认今天要修改的动画镜头"},
        {"time": "10:00-12:00", "activity": "用Maya制作角色动画，调整动作的timing和spacing"},
        {"time": "14:00-16:00", "activity": "渲染动画序列，检查运动轨迹和表情"},
        {"time": "16:00-17:00", "activity": "和团队开会，讨论动画风格和技术难点"},
        {"time": "17:00-18:00", "activity": "学习新的动画技巧和插件"}
    ],
    "director": [
        {"time": "09:00-10:00", "activity": "和编剧讨论剧本，调整故事节奏和人物弧光"},
        {"time": "10:00-12:00", "activity": "现场指导演员表演，调整走位和情绪"},
        {"time": "14:00-16:00", "activity": "和摄影师沟通镜头语言，设计拍摄角度和运镜"},
        {"time": "16:00-17:00", "activity": "查看样片，给剪辑师反馈"},
        {"time": "17:00-18:00", "activity": "准备明天的拍摄计划，协调各部门工作"}
    ],
    "video_editor": [
        {"time": "09:00-10:00", "activity": "导入素材，整理分类今天要剪辑的视频"},
        {"time": "10:00-12:00", "activity": "用Premiere剪辑视频，调整节奏和转场"},
        {"time": "14:00-16:00", "activity": "添加字幕、音效和背景音乐"},
        {"time": "16:00-17:00", "activity": "调色和特效处理，提升画面质感"},
        {"time": "17:00-18:00", "activity": "导出成片发给客户，收集修改意见"}
    ],
    "cinematographer": [
        {"time": "09:00-10:00", "activity": "和导演讨论今天的拍摄计划和镜头设计"},
        {"time": "10:00-12:00", "activity": "布置灯光，测试不同光位的效果"},
        {"time": "14:00-16:00", "activity": "操作摄影机拍摄，控制构图和运镜"},
        {"time": "16:00-17:00", "activity": "查看回放，确认画面质量和曝光"},
        {"time": "17:00-18:00", "activity": "整理设备，准备明天的拍摄"}
    ],
    "copywriter": [
        {"time": "09:00-10:00", "activity": "和客户开会，了解产品卖点和目标用户"},
        {"time": "10:00-12:00", "activity": "撰写广告文案，尝试5种不同的创意角度"},
        {"time": "14:00-16:00", "activity": "写公众号文章，设计标题和内容结构"},
        {"time": "16:00-17:00", "activity": "和设计师配合，调整文案和视觉的配合"},
        {"time": "17:00-18:00", "activity": "阅读优秀文案案例，积累创意素材"}
    ],
    "journalist": [
        {"time": "09:00-10:00", "activity": "查看新闻线索，确定今天要采访的选题"},
        {"time": "10:00-12:00", "activity": "外出采访，记录受访者的观点和故事"},
        {"time": "14:00-16:00", "activity": "整理采访录音，提取关键信息"},
        {"time": "16:00-17:00", "activity": "撰写新闻稿，确保事实准确和逻辑清晰"},
        {"time": "17:00-18:00", "activity": "和编辑沟通，修改稿件并准备发布"}
    ],
    "editor": [
        {"time": "09:00-10:00", "activity": "查看投稿邮箱，筛选有价值的稿件"},
        {"time": "10:00-12:00", "activity": "审稿，检查文章的逻辑、事实和文字"},
        {"time": "14:00-16:00", "activity": "和作者沟通，提出修改意见和建议"},
        {"time": "16:00-17:00", "activity": "策划选题，确定下期的内容方向"},
        {"time": "17:00-18:00", "activity": "排版和校对，准备发布"}
    ],
    "social_media_operator": [
        {"time": "09:00-10:00", "activity": "查看昨日数据，分析哪些内容表现好"},
        {"time": "10:00-12:00", "activity": "策划今天的内容，撰写文案和准备素材"},
        {"time": "14:00-16:00", "activity": "发布内容，监控评论和私信，及时回复用户"},
        {"time": "16:00-17:00", "activity": "分析竞品账号，学习优秀内容的创意"},
        {"time": "17:00-18:00", "activity": "制定下周的内容日历和选题计划"}
    ],
    "actor": [
        {"time": "09:00-10:00", "activity": "阅读剧本，分析角色的性格和动机"},
        {"time": "10:00-12:00", "activity": "排练台词和走位，和对手演员磨合"},
        {"time": "14:00-16:00", "activity": "拍摄现场表演，根据导演要求调整"},
        {"time": "16:00-17:00", "activity": "查看回放，总结表演中的问题"},
        {"time": "17:00-18:00", "activity": "练习台词和形体，保持表演状态"}
    ],
    "host": [
        {"time": "09:00-10:00", "activity": "准备节目流程，熟悉今天的话题和嘉宾"},
        {"time": "10:00-12:00", "activity": "彩排，调整节目节奏和互动环节"},
        {"time": "14:00-16:00", "activity": "录制或直播节目，控制现场气氛"},
        {"time": "16:00-17:00", "activity": "复盘节目效果，总结改进点"},
        {"time": "17:00-18:00", "activity": "练习口才和表达，保持主持状态"}
    ]
}

# 更新数据
updated_count = 0
for job in data['jobs']:
    job_id = job['jobId']
    if job_id in typical_day_data:
        job['typicalDay'] = typical_day_data[job_id]
        updated_count += 1
        print(f"✓ 已更新: {job['jobName']}")

# 保存数据
with open('public/data/行业岗位专业测评-岗位库-完整版-generated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n完成！已更新 {updated_count} 个岗位的 typicalDay 数据")
