from fastapi import APIRouter
from db import get_article, get_blocks

router = APIRouter(tags=['articles'],  prefix='/wiki',)

@router.get('/')
async def start():
    return {'1':0}

@router.get('/articles/{art_id}')
async def article(art_id):
    article = get_article(art_id)
    if article:
        blocks = get_blocks(art_id)
        return {'id':art_id, 'title':article.title,'desc': article.description, 'blocks':blocks}