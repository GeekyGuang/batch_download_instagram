# JS+imginn+instaloader+IDM+python下载instagram博主全部视频和图片

### 1. get_video_urls.js
打开https://imginn.com/,
输入博主的用户名，加载出全部要下载的图片和视频

Ctrl+Shift+J 打开控制台
复制粘贴get_video_urls.js文件里的代码，回车

得到2个文件：
- 下载链接.tx是所有视频的下载链接，复制进IDM下载,将下载好的视频放在videos文件夹
- code_video.json文件是shortcode和videoname的对应关系对象，稍后使用

### 2. instaloader
安装instaloader
```bash
pip3 install instaloader
```

### 3. download.py
运行download.py代码，得到2个文件：
- posts.json文件里有shortcode,date,imagename
- images.json文件里是所有图片的下载链接，复制进IDM下载，将下载好的图片放在images文件夹

### 4. download_captions.py
运行download_captions.py文件，得到所有推文的正文

### 5. image_renamer.py
运行image_renamer.py重命名图片

### 6. video_renamer.py
运行video_renamer.py重命名视频
