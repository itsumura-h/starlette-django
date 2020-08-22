from starlette.templating import Jinja2Templates
from typing import Dict

templates = Jinja2Templates(directory='resources')

def render(path:str, params:Dict):
    return templates.TemplateResponse(path, params)
