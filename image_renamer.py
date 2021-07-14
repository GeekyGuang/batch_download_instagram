import os
import json

with open('posts.json') as f:
    posts = json.load(f)

path = 'images'  # 需要重命名文件夹路径
file_names = os.listdir(path)

print(file_names)

for name in file_names:
    old_name = path + '/' + name
    for post in posts:
        if post['image_name'] == name:
            if post['num'] != '':
                new_name = path + '/' + post['date'].replace(':', '-') + '_' + post['num'] + '.jpg'
            else:
                new_name = path + '/' + post['date'].replace(':', '-') + '.jpg'
            break
    os.rename(old_name, new_name)

print('succeed')
