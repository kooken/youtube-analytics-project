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

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel,indent=2, ensure_ascii=False))
