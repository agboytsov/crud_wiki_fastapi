from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    team = Column(String(250), nullable=True)
    title = Column(String(250), nullable=False)
    description = Column(Text, nullable=True)
    badges = Column(Text, nullable=True)
    parent = Column(String(250), nullable=True)
    created = Column(DateTime, nullable=False)
    edited = Column(Text, nullable=True)
    category = Column(String(250), nullable=True)


class Article_content(Base):
    __tablename__ = 'article_content'

    id = Column(Integer, primary_key=True)
    article = Column(Integer, ForeignKey('articles.id'), nullable=False)
    type = Column(String(250), nullable=False)
    content = Column(Text, nullable=True)
    position = Column(Integer, nullable=False)
    add_class = Column(String(500), nullable=True)


class ContentType(Base):
    __tablename__ = 'content_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    html = Column(String(50), nullable=True)
    tpl = Column(String(250), nullable=False)
    features = Column(Text, nullable=True)
    default_class = Column(String(250), nullable=True)
    attrs = Column(String(500), nullable=True)


class Block_texts(Base):
    __tablename__ = 'block_texts'

    id = Column(Integer, primary_key=True)
    content = Column(String(2000), nullable=True)
    class_name = Column(String(300), nullable=True)