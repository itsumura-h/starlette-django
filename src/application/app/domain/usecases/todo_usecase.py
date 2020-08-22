from ..models.todo.todo_service import TodoService

class TodoUsecase:
    def index(self):
        todo_service = TodoService()
        return todo_service.get_todos()
