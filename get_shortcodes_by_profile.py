# 根据profile获取所有shortcodes

import instaloader
from instaloader import Post
import json
import re

L = instaloader.Instaloader()

# L.login(user='', passwd='')
# 先用命令instaloader --login='你的用户名'登录，则会保存session
L.load_session_from_file('')

profile_name = 'jumpropegal_'  # 博主用户名

posts = instaloader.Profile.from_username(
    L.context, profile_name).get_posts()

shortcodes = []
for post in posts:
    shortcodes.append(post.shortcode)

with open('shortcodes.json', 'w', encoding='utf-8') as f:
    json.dump(shortcodes, f)

print('succeed')
