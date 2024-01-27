import os
from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str):
        self.video_id = video_id
        # self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.channel = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                   id=self.video_id).execute()
        self.video_name = self.channel['items'][0]['snippet']['title']
        self.link = self.channel["items"][0]["snippet"]["thumbnails"]["high"]["url"]
        self.views = int(self.channel['items'][0]['statistics']['viewCount'])
        self.likes = int(self.channel['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return self.video_name

class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id