from feedparser import parse

from marcosleal.settings import MEDIUM_FEED_URL, MEDIUM_MAX_POSTS


def update_medium_posts() -> str:
    posts = []
    posts_from_feed = parse(MEDIUM_FEED_URL)

    for post in posts_from_feed.entries[:MEDIUM_MAX_POSTS]:
        if post.get('tags') is None:
            continue

        link = post['link']
        title = post['title']

        posts.append(f'- [{title}]({link})')

    return '\n'.join(posts)
