# 根据profile获取推文信息和images/videos下载地址

import instaloader
from instaloader import Post
import json
import re
import copy

L = instaloader.Instaloader()

# L.login(user='', passwd='')
# 先用命令instaloader --login='你的用户名'登录，则会保存session
L.load_session_from_file('')

image_urls = []
video_urls = []
post_infos = []
image_patten = re.compile(r'[^/]*\.jpg')
video_patten = re.compile(r'[^/]*\.mp4')

profile_name = 'nate_kg'  # 博主用户名

posts = instaloader.Profile.from_username(
    L.context, profile_name).get_posts()

for post in posts:
    print(post.shortcode)
    post_info = {}
    post_info['shortcode'] = post.shortcode
    post_info['date'] = str(post.date)
    if post.typename == 'GraphSidecar':
        edges = post._field('edge_sidecar_to_children', 'edges')
        i = 0
        for item in edges:
            i += 1
            image_url = item['node']['display_url']
            image_urls.append(image_url)
            image_name = image_patten.findall(image_url)[0]
            post_info['image_name'] = image_name
            if item['node']["is_video"]:
                video_url = item['node']['video_url']
                video_urls.append(video_url)
                video_name = video_patten.findall(video_url)[0]
            else:
                video_name = ''
            post_info['video_name'] = video_name
            post_info['num'] = str(i)
            post_infos.append(copy.deepcopy(post_info))

    else:
        image_url = post.url
        image_urls.append(image_url)
        image_name = image_patten.findall(image_url)[0]
        post_info['image_name'] = image_name
        if post.is_video:
            video_url = post.video_url
            video_urls.append(video_url)
            video_name = video_patten.findall(video_url)[0]
        else:
            video_name = ''
        post_info['video_name'] = video_name
        post_info['num'] = ''
        post_infos.append(copy.deepcopy(post_info))


with open('posts.json', 'w', encoding='utf-8') as f:
    json.dump(post_infos, f)

with open('images.json', 'w', encoding='utf-8') as f:
    json.dump(image_urls, f)

with open('videos.json', 'w', encoding='utf-8') as f:
    json.dump(video_urls, f)

print('succeed')
