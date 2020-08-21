from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

class SampleController(HTTPEndpoint):
    async def get(self, request:Request):
        return JSONResponse({'method': 'get'})

    async def post(self, request:Request):
        return JSONResponse({'method':'post'})
