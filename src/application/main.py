from libs.routing import Route
from libs.server import run_server
from app.controllers.user_controller import UserController
from app.controllers.todo_controller import TodoController

routes = [
    Route.get('/users', UserController.index),
    Route.post('/users', UserController.create),
    Route.get('/users/{id}', UserController.show),
    Route.get('/todo', TodoController().index),
]

app = run_server(routes, debug=True)
