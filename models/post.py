from dataclasses import dataclass


@dataclass
class Post:
    user_id: int
    id: int
    title: str
    body: str

    def __init__(self, data: dict):
        self.user_id = data.get('userId')
        self.id = data.get('id')
        self.title = data.get('title')
        self.body = data.get('body')
