from .todo_repository import TodoRepository
class TodoService:
    repository: TodoRepository

    def __init__(self):
        self.repository = TodoRepository()

    def get_todos(self):
        return self.repository.index()
