from starlette.routing import Route

def get(path:str, endpoint):
    return Route(path, endpoint=endpoint, methods=['GET'])

def post(path:str, endpoint):
    return Route(path, endpoint=endpoint, methods=['POST'])

def patch(path:str, endpoint):
    return Route(path, endpoint=endpoint, methods=['PATCH'])

def put(path:str, endpoint):
    return Route(path, endpoint=endpoint, methods=['put'])

def delete(path:str, endpoint):
    return Route(path, endpoint=endpoint, methods=['DELETE'])
