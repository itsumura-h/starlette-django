from libs.routing import Route
from libs.server import run_server
from app.controllers.user_controller import UserController

routes = [
    Route.get('/users', UserController.index),
    Route.post('/users', UserController.create),
    Route.get('/users/{id}', UserController.show)
]

app = run_server(routes, debug=True)
