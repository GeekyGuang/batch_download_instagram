# 通过shortcode批量下载
import instaloader
from instaloader import Post
from shortcodes import shortcodes

L = instaloader.Instaloader(
    # download_pictures=False,
    # download_videos=False,
    # download_video_thumbnails=False,
    compress_json=False
)

L.login(user='', passwd='')  # 填入你的ins用户名和密码
# L.load_session_from_file('x20920')


for shortcode in shortcodes:
    post = Post.from_shortcode(L.context, shortcode)
    if post.mediacount >= 1:
        L.download_post(post, target='start here')

# target是目标文件夹
