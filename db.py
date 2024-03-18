import sys

from sqlalchemy import create_engine, desc, select
from sqlalchemy.orm import Session

from block_models import *
from models import *


db = "sqlite:///new_1.db"

engine = create_engine(db)

Base.metadata.create_all(engine)


def get_class(class_name):
    return getattr(sys.modules[__name__], class_name)



def create_article(
        title: str,
        lst: list[dict],
        desc: str = None,
        team: str = None,
        parent: str = None,
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

        blocks_list = []
        for block in lst:
            bl_type = select(BlockTypes).where(title == block['title'])
            bl = ArticleBlocks(article_id=article, block_type=bl_type)
            blocks_list.append(bl)
        session.add_all(blocks_list)
        session.commit()
            # model = get_class(bl_type.model)


def create_block_type(title, model, func, content_type):
    with Session(engine) as session:
        b = BlockTypes(title=title, model=model, func=func, content_type=content_type)
        session.add(b)
        session.commit()

create_block_type('Text', model='BlockTexts', func='BlockTexts_func', content_type='str')
# create_article(title='124',desc='asfa',lst=[{'title': 'Text'}])
