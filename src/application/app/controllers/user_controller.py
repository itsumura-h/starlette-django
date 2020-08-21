from starlette.requests import Request
from starlette.responses import JSONResponse

class UserController:
    @staticmethod
    async def index(request:Request):
        return JSONResponse({'method': 'get'})

    @staticmethod
    async def create(request:Request):
        return JSONResponse({'method': 'post'})

    @staticmethod
    async def show(request:Request):
        id = request.path_params['id']
        return JSONResponse({'id': id})
