import instaloader
import datetime

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_video_thumbnails=False,
    compress_json=False)

# L.login(user='', passwd='')
# 先用命令instaloader --login='你的用户名'登录，则会保存session
L.load_session_from_file('')
profile_name = 'jumpropegal_'  # 博主用户名

posts = instaloader.Profile.from_username(
    L.context, profile_name).get_posts()

earliest_day = datetime.datetime.today()

for post in posts:
    if post.date < earliest_day:
        earliest_day = post.date

print(earliest_day)
