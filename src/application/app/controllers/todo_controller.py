from starlette.requests import Request
from libs.controller import render
from app.domain.usecases.todo_usecase import TodoUsecase

class TodoController:
    async def index(request:Request):
        todo_usesace = TodoUsecase()
        # todos = todo_usesace.index()
        return render('pages/todo/index.html', {'request':request})
