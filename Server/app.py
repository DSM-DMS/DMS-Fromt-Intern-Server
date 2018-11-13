from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from flask_jwt_extended import JWTManager

import os
from mongoengine import connect

from config import Config
from view import Router


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    Router(app).register()
    JWTManager(app)
    CORS(app)

    connect('dms-intern')

    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    return app
