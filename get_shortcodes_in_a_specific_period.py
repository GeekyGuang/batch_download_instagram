# 根据profile获取指定时间段内的shortcodes
from datetime import datetime
from itertools import dropwhile, takewhile
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

SINCE = datetime(2020, 4, 1)  # 开始时间
UNTIL = datetime(2020, 7, 1)  # 结束时间(不包含)

shortcodes = []
for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
    shortcodes.append(post.shortcode)

with open('shortcodes.json', 'w', encoding='utf-8') as f:
    json.dump(shortcodes, f)

print('succeed')
