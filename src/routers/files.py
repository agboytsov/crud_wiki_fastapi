from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from db import *
from schema.fa_models import *

router = APIRouter(tags=['files'], prefix='/files', )

@router.get('/')
async def show_files():
    """Отдаст список файлов?"""
    return {'files': 'no_files'}

@router.get('/{file}')
async def download_file(file):
    """Отдаст конкретный файл?"""
    pass

@router.post('/')
async def upload_file():
    """Загрузить файл"""
    pass