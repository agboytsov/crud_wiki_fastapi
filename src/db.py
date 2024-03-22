import sys

from sqlalchemy import create_engine, desc, select, delete
from sqlalchemy.orm import Session

from models.models import *
from models.block_models import *
from database import engine
from handlers.block_funcs import *
from schema.fa_models import *


def get_class(class_name):  # не всегда работает нормально, зависит от путей
    return getattr(sys.modules[__name__], class_name)


def create_company(quniq_id=0):
    with Session(engine) as session:
        company = Companies(quniq_id=quniq_id)
        session.add(company)
        session.commit()
        return company.id


def create_article(
        title: str,
        description: str = None,
        blocks: list[dict] | None = None,
        company: int = 1,
        parent: int = None,
) -> tuple:
    """Создает статью"""
    errors = []
    with Session(engine) as session:
        created = datetime.datetime.now()
        article = Article(
            title=title,
            description=description,
            created_at=created,
            updated_at=created,
            company_id=company,
            parent_id=parent
        )
        try:
            session.add(article)
            session.commit()
            article_id = article.id
        except Exception as e:
            print(e)
            article_id = 0
            errors.append(('article error',e))

        if blocks:
            if article_id != 0:
                for i, block in enumerate(blocks):
                    pos = i+1
                    print(pos)
                    block = ArticleContentCreateModel(
                        article_id=article_id,
                        type=block['type'],
                        content=block['content'],
                        position=pos
                    )
                    try:
                        create_block(block)
                    except Exception as e:
                        errors.append(('block error', e))

    return article_id, errors


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


def delete_article(article: int):  # TBD: перевод в разряд не активных
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
                    'id': block[0].block_id,
                    'content': block_parser(block[0]),
                    'position': block[0].position
                })
            print(result)
            return result
        except Exception as e:
            print(e)
            return


funcs_and_models = {
    'BlockTexts': (BlockTexts_parser, BlockTexts),
}


def block_parser(block):
    func, model = funcs_and_models.get(block.block_model)
    with Session(engine) as session:
        result = func({'block_id': block.block_id}, model, session, add=False)
        return result


def create_block(block):
    with Session(engine) as session:
        new_block = ArticleContent(
            article_id=block.article_id,
            block_model=block.type,
            block_id=0,
            position=block.position
        )

        session.add(new_block)
        session.commit()
        print(new_block.id, block.content)

        func, model = funcs_and_models.get(block.type)  # протестировать

        block_to_parse = {'content': block.content, 'block_id': new_block.id}

        new_block.block_id = func(block_to_parse, model, session)

        session.add(new_block)
        session.commit()


def delete_blocks(art: int):
    with (Session(engine) as session):
        bl = delete(ArticleContent).filter(ArticleContent.article_id == art)
        bl = session.execute(bl)
        session.commit()
