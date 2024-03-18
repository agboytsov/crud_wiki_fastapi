from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from models import *


class BlockTexts(Base):
    __tablename__ = 'block_texts'

    id: Mapped[int] = mapped_column(primary_key=True)
    block_type: Mapped[int] = mapped_column(ForeignKey('article_blocks.id'))
    content: Mapped[str] = mapped_column(String(256), nullable=True)
    class_name: Mapped[str] = mapped_column(String(300), nullable=True)


class BlockImages(Base):
    __tablename__ = 'block_images'

    id: Mapped[int] = mapped_column(primary_key=True)
    block_type:Mapped[int] = mapped_column(ForeignKey('article_blocks.id'))
    src: Mapped[str] = mapped_column(String(256), nullable=True)
    alt: Mapped[str] = mapped_column(String(256), nullable=True)
    file: Mapped[int]
    class_name = mapped_column(String(300), nullable=True)


class BlockHeader(Base):
    __tablename__ = 'block_texts'

    id: Mapped[int] = mapped_column(primary_key=True)
    block_type: Mapped[int] = mapped_column(ForeignKey('article_blocks.id'))
    content: Mapped[str] = mapped_column(String(256), nullable=True)
    class_name: Mapped[str] = mapped_column(String(300), nullable=True)


class BlockVideo(Base):
    __tablename__ = 'block_images'

    id: Mapped[int] = mapped_column(primary_key=True)
    block_type: Mapped[int] = mapped_column(ForeignKey('article_blocks.id'))
    src: Mapped[str] = mapped_column(String(256), nullable=True)
    type: Mapped[str] = mapped_column(String(256), nullable=True)
    file: Mapped[int] mapped_column(ForeignKey('files.id'), nullable=True)
    class_name = mapped_column(String(300), nullable=True)
    controls: Mapped[bool]
    autoplay: Mapped[bool]

class BlockList(Base):
    __tablename__ = 'block_lists'

    id: Mapped[int] = mapped_column(primary_key=True)
    block_type: Mapped[int] = mapped_column(ForeignKey('article_blocks.id'))
    items: Mapped[List['ListsItems']] = relationship()
    class_name = mapped_column(String(300), nullable=True)

class ListsItems(Base):
    __tablename__ = 'lists_items'

    id: Mapped[int] = mapped_column(primary_key=True)
    list_id: Mapped[int] = mapped_column(ForeignKey('block_lists.id'))
    content: Mapped[str] = mapped_column(String(1000), nullable=True)

