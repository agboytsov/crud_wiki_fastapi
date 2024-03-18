from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

db = "sqlite:///new_1.db"
engine = create_engine(db)


class Base(DeclarativeBase):
    pass

Base.metadata.create_all(engine)