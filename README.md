# python + instaloader + IDM批量下载instagram视频和图片

### 0. 安装instaloader
```bash
pip3 install instaloader
```

### 1. 通过shortcode下载post
- 运行get_posts_by_shortcodes.py，会得到posts.json, images.json, videos.json三个文件
- 复制images.json中的内容到IDM下载器下载图片
- 复制videos.json中的内容到IDM下载器下载视频
- 运行image_renamer.py重命名图片
- 运行video_renamer.py重命名视频

### 2. 下载某个博主的全部post
- 运行get_posts_by_profile.py，会得到posts.json, images.json, videos.json三个文件
- 之后下载和重命名操作步骤同上

### 3. 下载stories
运行download_highlights.py，会下载指定博主的所有stories highlights

### 4. 多线程下载
多线程下载比单线程快，但用来下载视频会有不完整的现象，适合只用来下载推文正文

get_captions_by_profile_multithread.py和get_captions_by_shortcodes_multithread分别用profile和shortcodes下载


### 参考
https://martechwithme.com/download-instagram-posts-stories-hashtags-highlights-python/
http://www.cxyzjd.com/article/w5688414/85175620
