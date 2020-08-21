from starlette.routing import Route as StarletteRoute

class Route:
    @staticmethod
    def get(path:str, endpoint):
        return StarletteRoute(path, endpoint=endpoint, methods=['GET'])

    @staticmethod
    def post(path:str, endpoint):
        return StarletteRoute(path, endpoint=endpoint, methods=['POST'])

    @staticmethod
    def patch(path:str, endpoint):
        return StarletteRoute(path, endpoint=endpoint, methods=['PATCH'])

    @staticmethod
    def put(path:str, endpoint):
        return StarletteRoute(path, endpoint=endpoint, methods=['PUT'])

    @staticmethod
    def delete(path:str, endpoint):
        return StarletteRoute(path, endpoint=endpoint, methods=['DELETE'])

def get(path:str, endpoint):
    return StarletteRoute(path, endpoint=endpoint, methods=['GET'])

def post(path:str, endpoint):
    return StarletteRoute(path, endpoint=endpoint, methods=['POST'])

def patch(path:str, endpoint):
    return StarletteRoute(path, endpoint=endpoint, methods=['PATCH'])

def put(path:str, endpoint):
    return StarletteRoute(path, endpoint=endpoint, methods=['PUT'])

def delete(path:str, endpoint):
    return StarletteRoute(path, endpoint=endpoint, methods=['DELETE'])
