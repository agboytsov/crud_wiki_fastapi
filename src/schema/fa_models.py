from typing import Union, List
from pydantic import BaseModel


class ArticleCreateModel(BaseModel):
    title: str
    description: str | None = None
    company: int | None = None
    parent: int | None = None
    lst: List | None = None


class ArticleUpdateModel(BaseModel):
    id: int
    title: str
    description: str | None = None
    parent: int | None = None
    lst: List | None = None

class ArticleContentCreateModel(BaseModel):
    article_id: int
    type: str
    block_id:  int | None = None
    content: dict
