from __future__ import annotations
import datetime
from typing import List, Optional
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database import Base
from models.block_models import *

print('models')
class ArticleContent(Base):
    __tablename__ = 'article_content'

    id: Mapped[int] = mapped_column(primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey('articles.id'))
    # сохраняем модель, потом возьмем айди из модели
    block_model: Mapped[str]
    block_id: Mapped[int]
    position: Mapped[int]


class Companies(Base):
    __tablename__ = 'companies'

    id: Mapped[int] = mapped_column(primary_key=True)
    quniq_id: Mapped[int]


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    quniq_id: Mapped[int]
    


class Article(Base):
    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(2000), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(nullable=False)  # = created_at при создании
    deleted_at: Mapped[datetime.datetime] = mapped_column(nullable=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey('articles.id'), nullable=True)
    company_id: Mapped[int] = mapped_column(ForeignKey('companies.id'))
