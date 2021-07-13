# 下载整个博主的推文
import instaloader

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_video_thumbnails=False,
    compress_json=False)

L.login(user='', passwd='')  # 填入你的ins用户名和密码
# L.load_session_from_file(username='')
profile_name = 'lauren.jumps'  # 博主用户名

posts = instaloader.Profile.from_username(
    L.context, profile_name).get_posts()

for post in posts:
    L.download_post(post, target='captions')
