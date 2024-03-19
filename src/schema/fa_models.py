from typing import Union, List
from pydantic import BaseModel


class ArticleCreateModel(BaseModel):
    title: str
    description: str | None = None
    team: int | None = None
    parent: int | None = None
    lst: List | None = None


class ArticleUpdateModel(BaseModel):
    id: int
    title: str
    description: str | None = None
    parent: int | None = None
    lst: List | None = None
