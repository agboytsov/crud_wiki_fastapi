# from __future__ import annotations
from dotenv import load_dotenv
import os
load_dotenv()
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

db_user = os.getenv('DB_USER')
db_name = os.getenv('DB_NAME')
db_password = os.getenv('DB_PASSWORD')
db_server = os.getenv('DB_SERVER')
db_port = os.getenv('DB_PORT')



# db = "sqlite:///new_1.db"
db = f"postgresql+psycopg2://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}"

engine = create_engine(db, echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

# Base.metadata.create_all(engine)
