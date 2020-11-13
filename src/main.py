from datetime import datetime
from pathlib import Path

from feedparser import parse
from pytz import timezone


def update_footer() -> str:
    timestamp = datetime.now(timezone('America/Sao_Paulo')).strftime('%c')
    footer = Path('FOOTER.md').read_text()

    return footer.format(timestamp=timestamp)


def update_readme_medium_posts(feed: str, readme: str, join_on: str) -> str:
    posts = []
    d = parse(feed)

    for item in d.entries:
        if item.get('tags'):
            _link = item["link"]
            _title = item["title"]

            posts.append(f'- [{_title}]({_link})')

    posts_joined = '\n'.join(posts)

    readme_stories = readme[: readme.find(join_on)]
    readme_stories = readme_stories + f'{join_on}\n\n{posts_joined}\n\n'

    return readme_stories


def start() -> None:
    rss_url = 'https://medium.com/feed/@marcosleal.prd'
    rss_title = '### Stories by Marcos Vinicius on Medium'
    readme = Path('README.md').read_text()

    updated_readme = update_readme_medium_posts(rss_url, readme, rss_title)

    with open('README.md', 'w+') as f:
        f.write(updated_readme + update_footer())


if __name__ == '__main__':
    print(__file__)
    start()
