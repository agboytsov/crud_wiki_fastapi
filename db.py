from sqlalchemy import create_engine, desc
from sqlalchemy.orm import Session

from block_models import *
from models import *


db = "sqlite:///new_1.db"

engine = create_engine(db)

Base.metadata.create_all(engine)

def create_article(
        title: str,
        lst: list[dict],
        desc: str = None,
        team: str = None,
        parent: str = None,
) -> None:
    with Session(engine) as session:
        blocks_list = []
        for block in lst:
            bl_type = session.get()


        created = datetime.datetime.now()


        article = Article(
            title=title,
            description=desc,
            created=created,
            parent=parent,
            team=team,
            blocks=[]