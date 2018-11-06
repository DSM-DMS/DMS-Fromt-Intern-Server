from mongoengine import *

from model.post import PostModel
from model.user import UserModel


class CommentModel(Document):
    meta = {
        'collection': 'comment'
    }

    post = ReferenceField(
        document_type=PostModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    author = ReferenceField(
        document_type=UserModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    content = StringField(
        required=True
    )
