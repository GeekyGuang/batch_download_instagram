# 根据shortcodes获取推文信息和images/videos下载地址

import instaloader
from instaloader import Post
import json
import re
from shortcodes import shortcodes

L = instaloader.Instaloader(
    compress_json=False
)

L.login(user='', passwd='')  # 填入你的ins用户名和密码
# L.load_session_from_file('x20920')

image_urls = []
video_urls = []
post_infos = []
multimedia_posts = []
image_patten = re.compile(r'[^/]*\.jpg')
video_patten = re.compile(r'[^/]*\.mp4')

for shortcode in shortcodes:
    print(shortcode)
    post = Post.from_shortcode(L.context, shortcode)
    post_info = {}
    if post.mediacount > 1:
        multimedia_posts.append(shortcode)
    else:
        post_info['shortcode'] = post.shortcode
        post_info['date'] = str(post.date)
        image_url = post.url
        image_urls.append(image_url)
        image_name = image_patten.findall(image_url)[0]
        post_info['image_name'] = image_name
        if post.is_video == True:
            video_url = post.video_url
            video_urls.append(video_url)
            video_name = video_patten.findall(video_url)[0]
        else:
            video_name = ''
        post_info['video_name'] = video_name
        post_infos.append(post_info)

with open('posts.json', 'w', encoding='utf-8') as f:
    json.dump(post_infos, f)

with open('images.json', 'w', encoding='utf-8') as f:
    json.dump(image_urls, f)

with open('videos.json', 'w', encoding='utf-8') as f:
    json.dump(video_urls, f)

with open('multi_media.json', 'w', encoding='utf-8') as f:
    json.dump(multimedia_posts, f)

print('succeed')
