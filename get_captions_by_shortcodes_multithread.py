from threading import Thread
from time import time, sleep
from queue import Queue
from datetime import datetime
import instaloader
# from shortcodes import shortcodes
from instaloader import Post
import json

with open('shortcodes.json', encoding='utf-8') as f:
    shortcodes = json.load(f)

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_video_thumbnails=False,
    compress_json=False
)

# L.login(user='', passwd='')
# 先用命令instaloader --login='你的用户名'登录，则会保存session
L.load_session_from_file('')


def download_tweets(shortcode):
    try:
        post = Post.from_shortcode(L.context, shortcode)
        if post.mediacount >= 1:
            L.download_post(post, target='captions')
    except Exception as e:
        print(e)
        fp = open("error.txt", "a")
        fp.write(str(e)+"\n")
        fp.close()


class DownloadWorker(Thread):

    def __init__(self, queue, sleep=1):
        Thread.__init__(self)
        self.queue = queue
        self.numPicrures = 0
        self.sleep = sleep

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            item = self.queue.get()
            if item is None:
                break
            # print(imageUrl)
            download_tweets(item)
            self.queue.task_done()
            sleep(self.sleep)


if __name__ == "__main__":
    ts = time()
    queue = Queue()
    for x in range(5):
        worker = DownloadWorker(queue, 2)
        # Setting daemon to True will let the main thread exit even though the
        # workers are blocking
        worker.daemon = True
        worker.start()

    for shortcode in shortcodes:
        queue.put(shortcode)
    queue.join()
    print('Took {}s'.format(time() - ts))
