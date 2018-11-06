from flask_restful import Api


class Router:
    def __init__(self, app):
        self.app = app
        self.api = Api(app)

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
