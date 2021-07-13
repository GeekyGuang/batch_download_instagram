# 下载指定博主的stories/hightlights

import instaloader
from instaloader import Post, Profile

L = instaloader.Instaloader(compress_json=False)

L.login(user='', passwd='')  # 填入你的ins用户名和密码
# L.load_session_from_file('')

profile = Profile.from_username(L.context, username="letsjumpla")  # 修改博主用户名

for highlight in L.get_highlights(user=profile):
    # highlight is a Highlight object
    for item in highlight.get_items():
        # item is a StoryItem object
        L.download_storyitem(
            item, '{}/{}'.format(highlight.owner_username, highlight.title))
