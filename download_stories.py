# 貌似没有用,请使用highlights
import instaloader
from instaloader import Post, Profile

L = instaloader.Instaloader()

# L.login(user='', passwd='')  # 填入你的ins用户名和密码
L.load_session_from_file('')


profile = Profile.from_username(L.context, username="letsjumpla")

L.download_stories(userids=[profile.userid],
                   filename_target='{}/stories'.format(profile.username))
