
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse,PlainTextResponse

import sys
sys.path.insert(0, "/usr/src/app/skiptir")
from skiptir import hyphenate

__version__ = 0.1

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def home() -> str:
    return """
<html>
    <head><title>Icelandic hyphenation API</title></head>
    <body>
        <h1>Icelandic hyphenation API Server v{0}</h1>
        <ul><li><a href="/docs">Documentation</a></li></ul>
    </body>
</html>
""".format(__version__)

@app.post('/hyphenator', response_class=PlainTextResponse)
def hyphenator(text : str): 
    out = hyphenate(text, hyphenation_mode='pattern', hyphen_character='-')
    return out
