import sys

from sqlalchemy import create_engine, desc, select
from sqlalchemy.orm import Session

from models.models import *
from models.block_models import *
from database import engine
from handlers.block_funcs import *


def get_class(class_name):
    return getattr(sys.modules[__name__], class_name)


def create_article(
        title: str,
        description: str = None,
        blocks: list[dict] | None = None,
        team: str = None,
        parent: int = None,
) -> Article:
    with Session(engine) as session:
        created = datetime.datetime.now()
        article = Article(
            title=title,
            description=description,
            created=created,
            # parent=parent,
            # team=team,
        )
        session.add(article)
        session.commit()
        article_id = article.id
    return article_id


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


def delete_article(article: int):
    with Session(engine) as session:
        article = session.get(Article, article)
        session.delete(article)
        session.commit()


def get_blocks(article):
    with Session(engine) as session:
        try:
            blocks = select(ArticleContent).where(ArticleContent.article_id == article)
            blocks = session.execute(blocks).all()

            result = []
            for block in blocks:
                result.append({
                    'type': block[0].block_model,
                    'id': block[0].block_id
                })
            print(result)
            return result
        except Exception as e:
            print(e)
            return


funcs_and_models = {
    'BlockTexts': (BlockTexts_parser, BlockTexts)
}


def create_block(block):
    with Session(engine) as session:
        new_block = ArticleContent(article_id=block.article_id, block_model=block.type, block_id=0)
        session.add(new_block)
        session.commit()
        func, model = funcs_and_models.get(block.type)  # протестировать
        block_to_parse = {'content': block.content, 'block_id': new_block.id}
        # block_id = func(block_to_parse, model, session)
        print(new_block.block_id)
        new_block.block_id = func(block_to_parse, model, session)
        print(new_block.block_id)
        session.add(new_block)
        session.commit()

        # model = get_class(block.type)
        # print(model)
        # func = get_class(block.type+'_parser')
        # print(model)
