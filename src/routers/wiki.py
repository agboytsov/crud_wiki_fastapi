from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from db import get_article, get_blocks

router = APIRouter(tags=['articles'], prefix='/wiki', )


@router.get('/')
async def start():
    return {'1': 0}


@router.get('/articles')
async def show_articles():
    """Возврашает н статьей"""
    pass


@router.post('/articles')
async def new_article(data=Body()):
    """Создаем новую статью"""
    pass


@router.get('/articles/{art_id}')
async def article(art_id):
    '''Возврашает отдельную статью'''
    article = get_article(art_id)
    if article:
        # blocks = get_blocks(art_id)
        # print(blocks)
        blocks = []  #пока заглушка
        return {'id': art_id, 'title': article.title, 'desc': article.description, 'blocks': blocks}
    else:
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={ "message": "Статья не найдена" })

# @router.put('/articles/{art_id}')
#
#
# @router.delete('/articles/{art_id}')
