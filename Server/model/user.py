from mongoengine import *


class UserModel(Document):
    meta = {
        'collection': 'user'
    }

    id = StringField(
        primary_key=True
    )

    pw = StringField(
        required=True
    )
