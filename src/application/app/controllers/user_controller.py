from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

class UserEntireController(HTTPEndpoint):
    async def get(self, request:Request):
        return JSONResponse({'method': 'get'})

    async def post(self, request:Request):
        return JSONResponse({'method': 'post'})

class UserDetailController(HTTPEndpoint):
    async def get(self, request:Request):
        id = request.path_params['id']
        return JSONResponse({'method': f'get {id}'})

    async def post(self, request:Request):
        id = request.path_params['id']
        return JSONResponse({'method': f'post {id}'})
