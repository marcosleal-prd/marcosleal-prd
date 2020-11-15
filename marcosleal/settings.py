from marcosleal.utils import getenv_or_raise

# YouTube
YOUTUBE_MAX_VIDEOS = 5
YOUTUBE_API_KEY = getenv_or_raise('YOUTUBE_API_KEY')
YOUTUBE_CHANNEL_ID = 'UC9ljALQ1KcfatYfoo_MqSgQ'
YOUTUBE_TEXT_MATCH = '### :clapper: Últimos Vídeos no YouTube'

# Site
SITE_MAX_POSTS = 5
SITE_FEED_URL = 'https://coderarena.com.br/index.xml'
SITE_TEXT_MATCH = '### :page_facing_up: Últimos Artigos no Site'

# Medium
MEDIUM_MAX_POSTS = 5
MEDIUM_FEED_URL = 'https://medium.com/feed/@marcosleal.prd'
MEDIUM_TEXT_MATCH = '### :scroll: Últimos Artigos no Medium'
