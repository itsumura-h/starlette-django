from starlette.requests import Request
from libs.controller import Controller
from app.domain.usecases.todo_usecase import TodoUsecase

class TodoController(Controller):
    async def index(self, request:Request):
        todo_usesace = TodoUsecase()
        todos = todo_usesace.index()
        return self.render('pages/todo/index.html', {'request':request})
