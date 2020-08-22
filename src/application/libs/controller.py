from starlette.templating import Jinja2Templates

class Controller:
    templates = Jinja2Templates(directory='resources')

    def render(self, path, params):
        return self.templates.TemplateResponse(path, params)
