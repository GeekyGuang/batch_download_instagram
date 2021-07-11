import instaloader

L = instaloader.Instaloader()
L.login(user='', passwd='')  # 填入你的ins用户名和密码
# L.load_session_from_file(username='')
posts = instaloader.Profile.from_username(
    L.context, "lauren.jumps").get_posts()

for post in posts:
    L.download_post(post, target='Pics')
