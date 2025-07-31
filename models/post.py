from pydantic import BaseModel
from datetime import datetime
from typing import List

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

    model_config = {
        "arbitrary_types_allowed": True
    }

post_list: List[Post] = []

def serialized_posts():
    return [
        {
            "author": post.author,
            "title": post.title,
            "content": post.content,
            "creation_datetime": post.creation_datetime.isoformat()
        }
        for post in post_list
    ]