from flasgger import swag_from
from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required


from docs.post import *
from model.post import PostModel
from model.user import UserModel
from model.comment import CommentModel


class PostListView(Resource):

    @swag_from(POST_LIST_GET)
    def get(self):
        posts = PostModel.objects()
        if not posts:
            abort(204)

        result = {
            'posts': [{
                'postId': str(post.id()),
                'title': post.title,
                'author': post.author.id
            } for post in posts]
        }
        return jsonify(result)


class PostView(Resource):

    @swag_from(POST_GET)
    def get(self, postId):
        post: PostModel = PostModel.objects(_id=postId).first()

        if not post:
            abort(204)

        result = {
            'postId': str(post.id()),
            'author': post.author.id,
            'title': post.title,
            'content': post.content,
            'comments': [
                {
                    'commentId': str(comment.id()),
                    'author': comment.author.id,
                    'content': comment.content
                } for comment in CommentModel.objects(post=post)
            ]
        }

        return jsonify(result)

    @swag_from(POST_POST)
    @jwt_required
    def post(self):
        user: UserModel = UserModel.objects(id=get_jwt_identity()).first()

        payload = request.json
        PostModel(user, payload['title'], payload['content']).save()

        return Response('', 201)

    @swag_from(POST_PATCH)
    @jwt_required
    def patch(self, postId):
        user: UserModel = UserModel.objects(id=get_jwt_identity()).first()

        payload = request.json
        post = PostModel.objects(_id=postId).first()

        if not post: abort(204)
        if user != post.author: abort(403)

        post.title = payload['title']
        post.content = payload['content']
        post.save()

        return Response('', 201)
