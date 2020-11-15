from feedparser import parse

from marcosleal.settings import SITE_FEED_URL, SITE_MAX_POSTS


def update_site_posts() -> str:
    posts = []
    posts_from_feed = parse(SITE_FEED_URL)

    for post in posts_from_feed.entries[:SITE_MAX_POSTS]:
        link = post['link']
        title = post['title']

        posts.append(f'- [{title}]({link})')

    return '\n'.join(posts)
