# 貌似没有用,请使用highlights
import instaloader
from instaloader import Post, Profile

L = instaloader.Instaloader()

# L.login(user='', passwd='')  
# 先用命令instaloader --login='你的用户名'登录，则会保存session
L.load_session_from_file('你的用户名')


profile = Profile.from_username(L.context, username="letsjumpla")

L.download_stories(userids=[profile.userid],
                   filename_target='{}/stories'.format(profile.username))
