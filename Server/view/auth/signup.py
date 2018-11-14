from flasgger import swag_from
from flask import request, Response, abort
from flask_restful import Resource

from docs.user import SIGNUP_POST
from model.user import UserModel


class SignupView(Resource):

    @swag_from(SIGNUP_POST)
    def post(self):

        payload = request.json
        for key in ['id', 'password']:
            if key not in payload:
                abort(400)

        if UserModel.objects(id=payload['id']).first():
            return Response('', 204)

        UserModel(id=payload['id'], pw=payload['password']).save()
        return Response('', 201)
