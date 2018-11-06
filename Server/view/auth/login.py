from flasgger import swag_from
from flask import request, jsonify, abort
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from datetime import timedelta

from model.user import UserModel
from docs.user import LOGIN_POST


class Login(Resource):

    @swag_from(LOGIN_POST)
    def post(self):
        payload = request.json

        if UserModel.objects(id=payload['id'], pw=payload['password']).first():
            return jsonify({"accessTocken": create_access_token(identity=payload['id'], expires_delta=timedelta(days=1))})

        abort(401)
