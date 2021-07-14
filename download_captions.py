# 下载整个博主的推文
import instaloader

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_video_thumbnails=False,
    compress_json=False)

# L.login(user='', passwd='')  
# 先用命令instaloader --login='你的用户名'登录，则会保存session
L.load_session_from_file('你的用户名')
profile_name = 'lauren.jumps'  # 博主用户名

posts = instaloader.Profile.from_username(
    L.context, profile_name).get_posts()

for post in posts:
    L.download_post(post, target='captions')
