import os
import json

with open('code_video.json') as f:
    videos = json.load(f)

with open('posts.json') as f:
    posts = json.load(f)

path = 'videos'  # 需要重命名文件夹路径
file_names = os.listdir(path)


def rename(old_name, new_name):
    file_names = os.listdir(path)
    index = new_name.index('/') + 1
    if new_name[-6] == '_':
        new_name_f = new_name[index:-6]
    else:
        new_name_f = new_name[index:-4]
    i = 0
    for filename in file_names:
        if new_name_f in filename:
            i += 1
    new_name = path + '/' + new_name_f + '_' + str(i) + '.mp4'
    os.rename(old_name, new_name)


for name in file_names:
    old_name = path + '/' + name
    for video in videos:
        if video['video_name'] == name:
            shortcode = video['shortcode']
            break
    if shortcode[-1] == '/':
        shortcode_f = shortcode[:-1]
        suffix = ''
    else:
        index = shortcode.index('/')
        shortcode_f = shortcode[:index]
        suffix = shortcode[index+1:].replace('#', '_')

    for post in posts:
        if post['shortcode'] == shortcode_f:
            new_name = path + '/' + \
                post['date'].replace(':', '-') + suffix + '.mp4'
            break
    try:
        os.rename(old_name, new_name)
    except FileExistsError:
        rename(old_name, new_name)


print('succeed')
