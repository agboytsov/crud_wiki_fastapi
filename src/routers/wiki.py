from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from db import *
from schema.fa_models import *

router = APIRouter(tags=['articles'], prefix='/wiki', )


@router.get('/')
async def start():
    return {'description': 'База данных - статьи и прочая полезная инфа'}


@router.get('/articles')
async def show_articles():
    """Возврашает н статьей"""
    pass


@router.post('/articles', status_code=status.HTTP_201_CREATED)
async def new_article(article: ArticleCreateModel):
    """Создаем новую статью"""
    a = create_article(
        title=article.title,
        description=article.description,
        company=article.company,
        parent=article.parent,
        blocks=article.lst,
    )
    return {'article_id': a[0], 'errors': a[1]}


@router.get('/articles/{art_id}')
async def article(art_id):
    '''Возврашает отдельную статью'''
    article = get_article(art_id)
    if article:
        blocks = get_blocks(art_id)
        return {
            'id': art_id,
            'title': article.title,
            'desc': article.description,
            'blocks': blocks,
            'parent': article.parent_id,
            'created_at': article.created_at,
            'updated_at': article.updated_at
        }
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Статья не найдена"})


@router.post('/block')
async def cr_block(block: ArticleContentCreateModel):
    create_block(block)
    return block


@router.delete('/block/{art}')
async def blocks_del(art):
    delete_blocks(art)
    return art


@router.post('/company')
async def cr_company():
    create_company()


@router.get('/test')
async def test():
    tpl = './routers/test_article.html'
    with open(tpl, 'r', encoding='UTF-8') as f:
        result = f.read()
    return HTMLResponse(content=result)

# @router.put('/articles/{art_id}')
#
#
# @router.delete('/articles/{art_id}')
