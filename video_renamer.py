import os
import json

with open('code_video.json') as f:
    videos = json.load(f)

with open('posts.json') as f:
    posts = json.load(f)

path = 'videos'  # 需要重命名文件夹路径
file_names = os.listdir(path)

print(file_names)

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
        if new_name[-6] != '_':
            new_name = new_name[:-4] + '_1' + '.mp4'
        else:
            file_names = os.listdir(path)
            i = 0
            for filename in file_names:
                if new_name in filename:
                    i += 1
            new_name = new_name[:-5] + str(i) + '.mp4'
            os.rename(old_name, new_name)


print('succeed')
