from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from app.controllers.sample_controller import SampleController
from app.controllers.user_controller import (
    UserEntireController,
    UserDetailController
)

routes = [
    Route('/', SampleController),
    Route('/users', UserEntireController),
    Route('/users/{id}', UserDetailController),
]

app = Starlette(debug=True, routes=routes)
