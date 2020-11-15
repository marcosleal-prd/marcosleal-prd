from googleapiclient.discovery import build

from marcosleal.settings import (
    YOUTUBE_API_KEY,
    YOUTUBE_CHANNEL_ID,
    YOUTUBE_MAX_VIDEOS,
)


def update_youtube_videos() -> str:
    videos = []
    youtube = build(
        serviceName='youtube', version='v3', developerKey=YOUTUBE_API_KEY
    )

    request = youtube.search().list(
        part='snippet',
        channelId=YOUTUBE_CHANNEL_ID,
        maxResults=YOUTUBE_MAX_VIDEOS,
        order='date',
        type='video',
        fields='pageInfo(totalResults,resultsPerPage),'
        + 'items(id(videoId),snippet(title))',
    )

    response = request.execute()
    for video in response.get('items', []):
        video_id = video['id']['videoId']
        title = video['snippet']['title']
        link = f'https://www.youtube.com/watch?v={video_id}'

        videos.append(f'- [{title}]({link})')

    return '\n'.join(videos)
