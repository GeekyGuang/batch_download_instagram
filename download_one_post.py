# 一次下载一个shortcode对应的post

import instaloader
from instaloader import Post

L = instaloader.Instaloader(
    compress_json=False
)

L.login(user='', passwd='')  # 填入你的ins用户名和密码
# L.load_session_from_file('')

shortcode = 'CGKvz59MPsy'

post = Post.from_shortcode(L.context, shortcode)
L.download_post(post, target='onePost')

# target是目标文件夹
