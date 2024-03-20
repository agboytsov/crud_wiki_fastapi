from sqlalchemy import create_engine, desc
from sqlalchemy.orm import Session
# from models import Article, Article_content, Base, ContentType
from src.models.models import *

db = "sqlite:///new_old.db"

engine = create_engine(db)

Base.metadata.create_all(engine)


def create_article(
        title: str,
        lst: list[dict],
        desc: str = None,
        team: str = None,
        badges: str = None,
        parent: str = None,
        category: str = None
) -> None:
    """Добавляем в базу статью и ее блоки"""
    with Session(engine) as session:
        # добавляем саму статью
        created = datetime.datetime.now()
        article = Article(
            title=title,
            team=team,
            description=desc,
            badges=badges,
            parent=parent,
            category=category,
            created=created
        )
        session.add(article)
        session.commit()

        # добавляем блоки
        content = []
        pos = 0
        for i in lst:
            cont = Article_content(article=article.id, type=i['type'], content=i['content'], position=pos)
            pos += 1
            content.append(cont)
        session.add_all(content)
        session.commit()


def get_articles(
        team: int = 1,
        date_desc: bool = False  # сортировка по убыванию дат?
) -> list:
    """Возвращает список всех статей, относящихся к команде"""
    with Session(engine) as session:
        if date_desc:
            team_arts = session.query(Article).filter(Article.team == team).order_by(desc(Article.created)).all()
        else:
            team_arts = session.query(Article).filter(Article.team == team).all()
    return team_arts


def get_article(
        article: int
):
    """Получаем конкретную статью по айди"""
    try:
        with Session(engine) as session:
            article = session.get(Article, article)
            content = session.query(Article_content).filter(Article_content.article == article.id).all()
        return article, content
    except AttributeError as e:
        return


def update_article(article: int, new: dict) -> None:
    with Session(engine) as session:
        article = session.get(Article, article)
        article.title = new['title']
        article.description = new.get('desc', None)
        article.badges = new.get('badges', None)
        article.parent = new.get('parent', None)
        article.category = new.get('category', None)
        article.updated = datetime.datetime.now()
        session.add(article)
        session.commit()

        old_content = session.query(Article_content).filter(Article_content.article == article.id).all()
        session.delete(old_content)
        session.commit()

        content = []
        pos = 0
        for i in new['content']:
            cont = Article_content(article=article.id, type=i['type'], content=i['content'], position=pos)
            pos += 1
            content.append(cont)
        session.add_all(content)
        session.commit()


def create_type(name,
                tpl,
                html=None,
                features=None,
                default_class=None,
                attrs=None
                ) -> None:
    """Добавляем тип блока"""
    with Session(engine) as session:
        # добавляем саму статью
        created = datetime.datetime.now()
        article = ContentType(
            name=name,
            html=html,
            tpl=tpl,
            features=features,
            default_class=default_class,
            attrs=attrs
        )
        session.add(article)
        session.commit()


def block_info(block):
    try:
        with Session(engine) as session:
            block_meta = session.query(ContentType).filter(ContentType.name == block).first()

        return block_meta
    except AttributeError as e:
        print(e)
        return

