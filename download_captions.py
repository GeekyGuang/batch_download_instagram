import instaloader

L = instaloader.Instaloader()

# acc = 'lauren.jumps'

# L.download_profile(acc, profile_pic_only=True)

L.load_session_from_file('x20920')
posts = instaloader.Profile.from_username(
    L.context, "lauren.jumps").get_posts()

for post in posts:
    L.download_post(post, target='Pics')
