from flasgger import swag_from
from flask import request, Response, abort
from flask_restful import Resource

from docs.user import SIGNUP_POST
from model.user import UserModel


class Signup(Resource):

    @swag_from(SIGNUP_POST)
    def post(self):

        payload = request.json

        if UserModel.objects(id=payload['id']).first():
            abort(205)

        UserModel(id=payload['id'], pw=payload['password']).save()
        return Response('', 201)
