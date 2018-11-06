from flask_restful import Api


class Router:
    def __init__(self, app):
        self.app = app
        self.api = Api(app)

    def register(self):
        pass
