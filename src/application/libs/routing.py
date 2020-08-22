from typing import Callable
from enum import Enum

class ResponseTyp(Enum):
    json = 'json'
    html = 'html'

class LibsRoute:
    path:str
    endpoint:Callable
    method:str
    typ:ResponseTyp

    def __init__(self, path='', endpoint=None, method='', typ=None):
        self.path = path
        self.endpoint = endpoint
        self.method = method
        self.typ = typ

class Route:
    @staticmethod
    def get(path:str, endpoint):
        return LibsRoute(path, endpoint=endpoint, method='GET', typ=ResponseTyp.json)

    @staticmethod
    def get_html(path:str, endpoint):
        return LibsRoute(path, endpoint=endpoint, method='GET', typ=ResponseTyp.html)

    @staticmethod
    def post(path:str, endpoint):
        return LibsRoute(path, endpoint=endpoint, method='POST', typ=ResponseTyp.json)

    @staticmethod
    def post_html(path:str, endpoint):
        return LibsRoute(path, endpoint=endpoint, method='POST', typ=ResponseTyp.html)

    @staticmethod
    def patch(path:str, endpoint):
        return LibsRoute(path, endpoint=endpoint, method='PATCH', typ=ResponseTyp.json)

    @staticmethod
    def patch_html(path:str, endpoint):
        return LibsRoute(path, endpoint=endpoint, method='PATCH', typ=ResponseTyp.html)

    @staticmethod
    def put(path:str, endpoint):
        return LibsRoute(path, endpoint=endpoint, method='PUT', typ=ResponseTyp.json)

    @staticmethod
    def put_html(path:str, endpoint):
        return LibsRoute(path, endpoint=endpoint, method='PUT', typ=ResponseTyp.html)

    @staticmethod
    def delete(path:str, endpoint):
        return LibsRoute(path, endpoint=endpoint, method='DELETE', typ=ResponseTyp.json)

    @staticmethod
    def delete_html(path:str, endpoint):
        return LibsRoute(path, endpoint=endpoint, method='DELETE', typ=ResponseTyp.html)


def get(path:str, endpoint):
    return LibsRoute(path, endpoint=endpoint, method='GET', typ=ResponseTyp.json)

def get_html(path:str, endpoint):
    return LibsRoute(path, endpoint=endpoint, method='GET', typ=ResponseTyp.html)

def post(path:str, endpoint):
    return LibsRoute(path, endpoint=endpoint, method='POST', typ=ResponseTyp.json)

def post_html(path:str, endpoint):
    return LibsRoute(path, endpoint=endpoint, method='POST', typ=ResponseTyp.html)

def patch(path:str, endpoint):
    return LibsRoute(path, endpoint=endpoint, method='PATCH', typ=ResponseTyp.json)

def patch_html(path:str, endpoint):
    return LibsRoute(path, endpoint=endpoint, method='PATCH', typ=ResponseTyp.html)

def put(path:str, endpoint):
    return LibsRoute(path, endpoint=endpoint, method='PUT', typ=ResponseTyp.json)

def put_html(path:str, endpoint):
    return LibsRoute(path, endpoint=endpoint, method='PUT', typ=ResponseTyp.html)

def delete(path:str, endpoint):
    return LibsRoute(path, endpoint=endpoint, method='DELETE', typ=ResponseTyp.json)

def delete_html(path:str, endpoint):
    return LibsRoute(path, endpoint=endpoint, method='DELETE', typ=ResponseTyp.html)
