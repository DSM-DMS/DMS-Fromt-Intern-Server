import os


class Config:
    SERVICE_NAME = 'DMS Front Intern'

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': '/docs',
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'host': 'dms.istruly.sexy:792',
        'basePath': '/',
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Account',
                'description': '계정 관련 API'
            },
            {
                'name': 'Post',
                'description': '게시글 관련 API'
            },
            {
                'name': 'Comment',
                'description': '댓글 관련 API'
            }
        ]
    }

    JSON_AS_ASCII = False

    JWT_SECRET_KEY = os.getenv('SECRET_KEY', 'nerd-bear')
    SECRET_KEY = os.getenv('SECRET_KEY', 'nerd-bear')
