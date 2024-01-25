import os
import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        api_key: str = os.environ.get('YT_API_KEY')
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = self.channel["items"][0]["snippet"]["thumbnails"]["high"]["url"]
        self.subs_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.views_count = int(self.channel['items'][0]['statistics']['viewCount'])


    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.subs_count + other.subs_count

    def __sub__(self, other):
        return self.subs_count - other.subs_count

    def __gt__(self, other):
        return self.subs_count > other.subs_count

    def __ge__(self, other):
        return self.subs_count >= other.subs_count

    def __lt__(self, other):
        return self.subs_count < other.subs_count

    def __le__(self, other):
        return self.subs_count <= other.subs_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel,indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


    def to_json(self, filename):
        json_data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'descrition': self.description,
            'url': self.url,
            'subscriber_count': self.subs_count,
            'videoCount': self.video_count,
            'viewCount': self.views_count
        }
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json.dumps(json_data, ensure_ascii=False, indent=4))
