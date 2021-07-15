# 一次下载一个shortcode对应的post,下载速度慢且易出错，不推荐

import instaloader
from instaloader import Post
import json

L = instaloader.Instaloader(
    compress_json=False
)

# L.login(user='', passwd='')
# 先用命令instaloader --login='你的用户名'登录，则会保存session
L.load_session_from_file('')

shortcode = 'CRJpOUKs3hR'

post = Post.from_shortcode(L.context, shortcode)
L.download_post(post, target='onePost')

# target是目标文件夹
