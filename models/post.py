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
    return [post.model_dump() for post in post_list]