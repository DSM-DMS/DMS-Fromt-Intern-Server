from flasgger import swag_from
from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from bson import ObjectId


from docs.comment import *
from model.post import PostModel
from model.user import UserModel
from model.comment import CommentModel


class CommentView(Resource):

    @swag_from(COMMENT_POST)
    @jwt_required
    def post(self, id):
        user = UserModel.objects(id=get_jwt_identity()).first()
        post = PostModel.objects(_id=id).first()
        payload = request.json

        for key in ['content']:
            if key not in payload:
                abort(400)

        if not post:
            return Response('', 204)

        CommentModel(post, user, payload['content']).save()

        return Response('', 201)

    @swag_from(COMMENT_PATCH)
    @jwt_required
    def patch(self, id):
        user = UserModel.objects(id=get_jwt_identity()).first()
        comment = CommentModel.objects(_id=ObjectId(id)).first()
        payload = request.json

        for key in ['content']:
            if key not in payload:
                abort(400)

        if not comment:
            return Response('', 204)
        if user != comment.author: abort(403)

        comment.content = payload['content']
        comment.save()

        return Response('', 201)

    @swag_from(COMMENT_DELETE)
    @jwt_required
    def delete(self, id):
        user = UserModel.objects(id=get_jwt_identity()).first()
        comment = CommentModel.objects(_id=ObjectId(id)).first()

        if not comment:
            return Response('', 204)
        if user != comment.author:
            abort(403)

        comment.delete()

        return Response('', 201)
