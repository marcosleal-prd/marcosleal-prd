from pathlib import Path

from marcosleal.services.footer import update_footer
from marcosleal.services.medium import update_medium_posts
from marcosleal.services.site import update_site_posts
from marcosleal.services.youtube import update_youtube_videos
from marcosleal.settings import (
    MEDIUM_TEXT_MATCH,
    SITE_TEXT_MATCH,
    YOUTUBE_TEXT_MATCH,
)


def start() -> None:
    posts = update_site_posts()
    videos = update_youtube_videos()
    medium_posts = update_medium_posts()

    join_in = 'E muito mais...'
    current_readme = Path('README.md').read_text()

    readme = current_readme[: current_readme.find(join_in)]
    readme += f'{join_in}\n\n'
    readme += f'{YOUTUBE_TEXT_MATCH}\n\n{videos}\n\n'
    readme += f'{SITE_TEXT_MATCH}\n\n{posts}\n\n'
    readme += f'{MEDIUM_TEXT_MATCH}\n\n{medium_posts}\n\n'
    readme += f'{update_footer()}'

    with open('README.md', 'w+') as f:
        f.write(readme)


if __name__ == '__main__':
    start()
