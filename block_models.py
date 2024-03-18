from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from models import *


class Block_texts(Base):
    __tablename__ = 'block_texts'

    id: Mapped[int] = mapped_column(primary_key=True)
    block_type:Mapped[int] = mapped_column(ForeignKey('article_blocks.id'))
    content = Column(String(256), nullable=True)
    class_name = Column(String(300), nullable=True)
