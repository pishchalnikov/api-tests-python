from dataclasses import dataclass


@dataclass
class Comment:
    post_id: int
    id: int
    name: str
    email: str
    body: str

    def __init__(self, data: dict):
        self.post_id = data.get('postId')
        self.id = data.get('id')
        self.name = data.get('name')
        self.email = data.get('email')
        self.body = data.get('body')
