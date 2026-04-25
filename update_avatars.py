#!/usr/bin/env python3
import json

# 头像URL映射
avatar_urls = {
    "zhang_xiaolong": "https://imgslim.geekpark.net/uploads/image/file/a3/9b/a39b1fbe94dcba2a4c0a25ab99280b3c.jpg",
    "yu_jun": "https://img.traveldaily.cn/images/201607/d4e404be28385b7e.jpg",
    "liang_ning": "https://piccdn3.umiwi.com/img/202012/01/202012011711053519159802.jpeg",
    "ma_yun": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Jack_Ma_2008.jpg",
    "zhang_yiming": "https://imgslim.geekpark.net/uploads/image/file/c7/93/c793304ad891ce32afb77819b1e29595.jpg",
    "elon_musk": "https://upload.wikimedia.org/wikipedia/commons/3/34/Elon_Musk_Royal_Society_%28crop2%29.jpg",
    "linus_torvalds": "https://upload.wikimedia.org/wikipedia/commons/6/69/Linus_Torvalds.jpeg",
    "jeff_dean": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Jeff_Dean_in_2025_x.jpg/500px-Jeff_Dean_in_2025_x.jpg",
    "steve_jobs": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg",
    "kenya_hara": "https://i0.wp.com/www.printmag.com/wp-content/uploads/2016/12/2a34d8_34c73cf0f2104ecba706dc895af4e743mv2.jpg",
    "jony_ive": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Jonathan_Ive_%28OTRS%29.jpg",
    "dong_mingzhu": "https://media.bjnews.com.cn/image/2025/04/23/5579141710916693302.jpeg",
    "joe_girard": "https://p3-sdbk2-media.byteimg.com/tos-cn-i-xv4ileqgde/2266e990412a476ca9dd1f5d24bd3221~tplv-xv4ileqgde-resize-w:750.image",
    "grant_cardone": "https://muscleandhealth.com/wp-content/uploads/2022/11/GC_header.png",
    "tim_cook": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Tim_Cook_March_2026_%28cropped%29.jpg",
    "evan_you": "https://camo.githubusercontent.com/e6c6d569c08d3b8765233438f05cabf66e282f977f025bf3fc86cc3bbf354120/68747470733a2f2f70392d6a75656a696e2e62797465696d672e636f6d2f746f732d636e2d692d6b3375316662706663702f38323134643363366633346134336163613863323166356266303339613365367e74706c762d6b3375316662706663702d77617465726d61726b2e696d616765",
    "dan_abramov": "https://thediffpodcast.com/assets/images/dan-a-8d7a6d9e454582e77444d6d332035f60.png",
    "ma_huateng": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/%E9%A9%AC%E5%8C%96%E8%85%BE_Pony_Ma_2019.jpg/800px-%E9%A9%AC%E5%8C%96%E8%85%BE_Pony_Ma_2019.jpg",
    "andrew_ng": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Andrew_Ng_WSJ_%282%29.jpg/800px-Andrew_Ng_WSJ_%282%29.jpg",
    "dj_patil": "https://media.wired.com/photos/59328045aef9a462de983499/3:2/w_2240,c_limit/157166947.jpg",
    "lei_jun": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/%E9%9B%B7%E5%86%9B_2024-09-13.jpg/800px-%E9%9B%B7%E5%86%9B_2024-09-13.jpg",
    "wang_xing": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Wang_Xing_in_2009.jpg/800px-Wang_Xing_in_2009.jpg",
    "ren_zhengfei": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Ren_Zhengfei_2014.jpg/800px-Ren_Zhengfei_2014.jpg",
    "zhong_nanshan": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Zhong_Nanshan.jpg/800px-Zhong_Nanshan.jpg",
    "yuan_longping": "https://upload.wikimedia.org/wikipedia/commons/8/89/Yuan_Longping_in_1953.jpg",
    "tu_youyou": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Tu_Youyou_5012-1-2015.jpg/800px-Tu_Youyou_5012-1-2015.jpg",
    "warren_buffett": "https://upload.wikimedia.org/wikipedia/commons/5/51/Warren_Buffett_at_the_2015_SelectUSA_Investment_Summit.jpg",
    "peter_drucker": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Drucker5789.jpg",
    "salman_khan": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Salman_Khan_MV.jpg/800px-Salman_Khan_MV.jpg",
    "yu_minhong": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Yu_Minhong.jpg/800px-Yu_Minhong.jpg",
    "sheryl_sandberg": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Sheryl_Sandberg.jpg",
    "james_dyson": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/James_Dyson_4.jpg/800px-James_Dyson_4.jpg",
    "zaha_hadid": "https://cdn.britannica.com/98/193498-050-A71588D7/Zaha-Hadid.jpg",
    "jeff_bezos": "https://upload.wikimedia.org/wikipedia/commons/0/03/Jeff_Bezos_2016_%28cropped%29.jpg",
    "reid_hoffman": "https://upload.wikimedia.org/wikipedia/commons/1/19/Reid_Hoffman_in_SF_2011.jpg",
    "huang_zheng": "https://static-hk.hstong.com/public/cms/images/2024/08/10/1028999007119712257.jpg",
    "li_yongle": "https://www.tsinghua.org.cn/__local/A/FA/6F/26AA91803AF213EEDC371849F5F_34F20A72_446CC.png?e=.png",
    "zhang_wenhong": "https://wm-fs2.must.edu.mo/group1/M00/01/91/rBCE3mXuZjeAffLzABJb0GCsiU4654.jpg",
    "atul_gawande": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Atul_Gawande%2C_USAID_Assistant_Administrator.jpg/500px-Atul_Gawande%2C_USAID_Assistant_Administrator.jpg",
    "he_tingbo": "https://www-file.huawei.com/admin/asset/v1/pro/view/db67e78c71c94e4ca08a63365607f234.jpg"
}

# 读取JSON文件
with open('public/data/career-mentors.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 更新所有mentor的avatar字段
for category_key, category_data in data['categories'].items():
    for mentor in category_data['mentors']:
        mentor_id = mentor['mentorId']
        if mentor_id in avatar_urls:
            mentor['avatar'] = avatar_urls[mentor_id]
            print(f"Updated avatar for {mentor['name']} ({mentor_id})")

# 写回JSON文件
with open('public/data/career-mentors.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n✅ Avatar URLs updated successfully!")
