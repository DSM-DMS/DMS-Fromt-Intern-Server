from mongoengine import *

from model.user import UserModel


class PostModel(Document):
    meta = {
        'collection': 'post'
    }

    postId = StringField(
        primary_key=True
    )

    author = ReferenceField(
        document_type=UserModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    title = StringField(
        required=True
    )

    content = StringField(
        required=True
    )
