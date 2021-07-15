from threading import Thread
from time import time, sleep
from queue import Queue
from datetime import datetime
import instaloader
from instaloader import Post
from datetime import datetime
from itertools import dropwhile, takewhile

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_video_thumbnails=False,
    compress_json=False
)

# L.login(user='', passwd='')
# 先用命令instaloader --login='你的用户名'登录，则会保存session
L.load_session_from_file('')

profile_name = 'jumpropegal_'  # 博主用户名

posts = instaloader.Profile.from_username(
    L.context, profile_name).get_posts()

SINCE = datetime(2016, 1, 1)  # 开始时间
UNTIL = datetime(2021, 1, 1)  # 结束时间(不包含)


def download_tweets(post):
    try:
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

    for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
        queue.put(post)
    queue.join()
    print('Took {}s'.format(time() - ts))
