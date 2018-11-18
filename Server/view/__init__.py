from flask import Flask, abort
from flask_restful import Api
from jwt.exceptions import ExpiredSignatureError


class Router:
    def __init__(self, app: Flask):
        self.app = app
        self.api = Api(app)

    def exception_handler(self):
        self.app.register_error_handler(ExpiredSignatureError, expire_token_handlergi)

    def register(self):
        from view.auth.signup import SignupView
        from view.auth.login import LoginView
        self.api.add_resource(SignupView, '/signup')
        self.api.add_resource(LoginView, '/login')

        from view.post.comment import CommentView
        self.api.add_resource(CommentView, '/comment/<id>')

        from view.post.post import PostListView, PostView
        self.api.add_resource(PostListView, '/post_list')
        self.api.add_resource(PostView, '/post/<postId>')


def expire_token_handler(error):
    abort(403)
