from fastapi import FastAPI
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from libs.routing import ResponseTyp

def __set_routes(app, routes):
    for route in routes:
        if route.typ == ResponseTyp.json:
            app.add_api_route(
                path=route.path,
                endpoint=route.endpoint,
                methods=[route.method]
            )
        else:
            app.add_api_route(
                path=route.path,
                endpoint=route.endpoint,
                methods=[route.method],
                response_class=HTMLResponse
            )

def run_server(routes, debug=False):
    app = FastAPI(debug=debug)
    __set_routes(app, routes)
    return app
