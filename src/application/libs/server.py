from fastapi import FastAPI
from fastapi.routing import APIRouter

def __set_routes(app, routes):
    for route in routes:
        app.add_api_route(
            path=route.path,
            endpoint=route.endpoint,
            methods=route.methods
        )

def run_server(routes, debug=False):
    app = FastAPI(debug=debug)
    __set_routes(app, routes)
    return app
