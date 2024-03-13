from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from templater import *

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read():
    html = check()
    return HTMLResponse(content=html, status_code=200)