from starlette.requests import Request

class UserController:
    @staticmethod
    async def index(request:Request):
        return {'method': 'get'}

    @staticmethod
    async def create(request:Request):
        return {'method': 'post'}

    @staticmethod
    async def show(request:Request):
        id = request.path_params['id']
        return {'id': id}
