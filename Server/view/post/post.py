from flasgger import swag_from
from flask import request, jsonify, abort
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity


from docs.post import *
from model.post import PostModel
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

        post = {
            'author': post.author.id,
            'title': post.title,
            'content': post.content,
            'comments': [
                {
                    'commentId': comment.id(),
                    'author': comment.author.id,
                    'content': comment.content
                } for comment in CommentModel.objects(post=post)
            ]
        }

        return jsonify(post)
