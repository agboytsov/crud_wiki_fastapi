from random import random

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
# from templater import *
from routers.wiki import router as wiki_rout
app = FastAPI()

app.include_router(wiki_rout)

@app.get("/")
async def home():
    return {'a':1}

# @app.get("/", response_class=HTMLResponse)
# async def read():
#     html = check()[0]
#     return HTMLResponse(content=html, status_code=200)


# @app.get("/article")
# async def all_articles():
#     total_articles = 5
#     lst = []
#     for i in range(1, total_articles+1):
#         lst.append(check(i)[1])
#     return lst
#
#
# @app.get("/article/{article}")
# async def read(article:int = None):
#     if not article:
#         article = random.randint(1, 5)
#     result = check(article)[1]
#     return result