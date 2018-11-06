from docs import jwt_header, parameter


COMMENT_POST = {
    'tags': ['Comment'],
    'description': '댓글 작성',
    'parameters': [
        jwt_header,
        parameter('postId', '게시글 아이디', in_='uri'),
        parameter('content', '댓글 내용')
    ],

    'responses': {
        '201': {
            'description': '댓글 작성 완료'
        },
        '204': {
            'description': '게시글 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

COMMENT_PATCH = {
    'tags': ['Comment'],
    'description': '댓글 수정',
    'parameters': [
        jwt_header,
        parameter('commentId', '댓글 아이디', in_='uri'),
        parameter('content', '댓글 내용')
    ],

    'responses': {
        '201': {
            'description': '댓글 수정 완료'
        },
        '204': {
            'description': '댓글 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

COMMENT_DELETE = {
    'tags': ['Comment'],
    'description': '댓글 삭제',
    'parameters': [
        jwt_header,
        parameter('commentId', '댓글 아이디', in_='uri')
    ],

    'responses': {
        '201': {
            'description': '댓글 삭제 완료'
        },
        '204': {
            'description': '댓글 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
