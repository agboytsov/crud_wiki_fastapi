import sys

from sqlalchemy import create_engine, desc, select
from sqlalchemy.orm import Session

from models.models import *
from database import engine


def get_class(class_name):
    return getattr(sys.modules[__name__], class_name)


def create_article(
        title: str,
        desc: str = None,
        blocks: list[dict] | None = None,
        team: str = None,
        parent: int = None,
) -> None:
    with Session(engine) as session:
        created = datetime.datetime.now()
        article = Article(
            title=title,
            description=desc,
            created=created,
            parent=parent,
            team=team,
        )
        session.add(article)
        session.commit()


def get_article(article: int):
    with Session(engine) as session:
        return session.get(Article, article)


def update_article(article: int, new: dict):
    with Session(engine) as session:
        article = session.get(Article, article)
        article.title = new['title']
        article.description = new['desc']

        if new.get('blocks', None):
            print(new['blocks'])
            # article.blocks = ''
        article.edited = datetime.datetime.now()
        if new.get('parent', None):
            article.parent = new['parent']
        session.commit()


def delete_article(article):
    with Session(engine) as session:
        article = session.get(Article, article)
        session.delete(article)
        session.commit()


def get_blocks(article):
    print(article)
    with Session(engine) as session:
        article = session.get(Article, article)
        blocks = session.get(ArticleContent, article)
        return blocks
