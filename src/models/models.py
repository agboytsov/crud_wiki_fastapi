from __future__ import annotations
import datetime
from typing import List, Optional
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from database import Base


class ArticleContent(Base):
    __tablename__ = 'article_content'

    id: Mapped[int] = mapped_column(primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey('articles.id'))
    #сохраняем модель, потом возьмем айди из модели
    block_model: Mapped[str]
    block_id: Mapped[int]


class Article(Base):
    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(2000), nullable=True)
    created: Mapped[datetime.datetime] = mapped_column(nullable=False)
    edited: Mapped[datetime.datetime] = mapped_column(nullable=True)
    # test: Mapped[str]
    # blocks: Mapped[Optional['ArticleContent']] = relationship(back_populates='Article')
    # team: Mapped[int] = mapped_column(nullable=True)

    # blocks = relationship('ArticleContent', back_populates='artic')
    # team: Mapped[int|None] = mapped_column(ForeignKey('teams.id'), nullable=True)  # пока что для теста может быть null



#
#
# class Teams(Base):
#     __tablename__ = 'teams'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     # name: Mapped[str] #Название команды ? нужно ли его хранить у нас в бд?
#     # parent: Mapped[int]  #подкоманды со своими правами?
#
#
# class ArticleBlocks(Base):
#     __tablename__ = 'article_blocks'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     article_id: Mapped[int] = mapped_column(ForeignKey('articles.id'), nullable=False)
#     block_type: Mapped[int] = mapped_column(ForeignKey('block_types.id'), nullable=False)
#     block_id: Mapped[int] = mapped_column(nullable=False)


# class BlockTypes(Base):
#     __tablename__ = 'block_types'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(250), nullable=False)  # название для отображения
#     model: Mapped[str] = mapped_column(String(250), nullable=False)
#     func: Mapped[str] = mapped_column(String(250), nullable=False)  # имя возвращаемой функции
#     main_class: Mapped[str] = mapped_column(String(250), nullable=True)  # класс для отображения на фронте
#     content_type: Mapped[int] = mapped_column(String(100), nullable=True)  # тип - строка, список, словарь

# class ContentTypes(Base):
#     __tablename__ = 'content_types'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(250), nullable=False)  # название для отображения
#     main_class: Mapped[str]
#     additional_class: Mapped[str]
#     type: Mapped[str]  # тип - строка, список, словарь
