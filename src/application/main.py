from libs.routing import (
    get,
    post
)
from libs.server import run_server
from app.controllers.user_controller import UserController

routes = [
    get('/users', UserController.index),
    post('/users', UserController.create),
    get('/users/{id}', UserController.show)
]

app = run_server(routes, debug=True)
