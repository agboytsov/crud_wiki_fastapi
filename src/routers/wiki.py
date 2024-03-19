from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from db import get_article, get_blocks, create_article
from schema.fa_models import *

router = APIRouter(tags=['articles'], prefix='/wiki', )


@router.get('/')
async def start():
    return {'1': 0}


@router.get('/articles')
async def show_articles():
    """Возврашает н статьей"""
    pass


@router.post('/articles', status_code=status.HTTP_201_CREATED)
async def new_article(article: ArticleCreateModel):
    """Создаем новую статью"""
    a = create_article(title=article.title, description=article.description)
    return {'article_id': a}


@router.get('/articles/{art_id}')
async def article(art_id):
    '''Возврашает отдельную статью'''
    article = get_article(art_id)
    if article:
        blocks = get_blocks(art_id)
        return {'id': art_id, 'title': article.title, 'desc': article.description, 'blocks': blocks}
    else:
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={ "message": "Статья не найдена" })

# @router.put('/articles/{art_id}')
#
#
# @router.delete('/articles/{art_id}')
