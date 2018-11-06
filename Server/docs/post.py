from docs import parameter, jwt_header

POST_LIST_GET = {
    'tags': ['Post'],
    'description': '게시물 목록 조회',
    'parameters': [],

    'responses': {
        '200': {
            'description': '조회 성공',
            'examples': {
                '': {
                    'posts': [
                        {
                            'postId': '게시글 아이디',
                            'title': '제목',
                            'author': '작성자'
                        },
                        {
                            'postId': '게시글 아이디1',
                            'title': '제목1',
                            'author': '작성자1'
                        }
                    ]
                }
            }
        },
        '204': {
            'description': '게시글 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}


POST_GET = {
    'tags': ['Post'],
    'description': '게시물 목록 조회',
    'parameters': [
        parameter('postId', '게시글 아이디', in_='uri')
    ],

    'responses': {
        '200': {
            'description': '조회 성공',
            'examples': {
                '': {
                    'author': '작성자',
                    'title': '제목',
                    'content': '내용',
                    'comments': [
                        {
                            'commentId': '댓글 아이디',
                            'author': '댓글 작성자',
                            'content': '댓글 내용'
                        },
                        {
                            'commentId': '댓글 아이디',
                            'author': '댓글 작성자1',
                            'content': '댓글 내용1'
                        }
                    ]
                }
            }
        },
        '204': {
            'description': '게시글 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}


POST_POST = {
    'tags': ['Post'],
    'description': '게시물 작성',
    'parameters': [
        jwt_header,
        parameter('title', '게시글 제목'),
        parameter('content', '게시글 내용')
    ],

    'responses': {
        '201': {
            'description': '게시글 작성 완료'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

POST_PATCH = {
    'tags': ['Post'],
    'description': '게시물 수정',
    'parameters': [
        jwt_header,
        parameter('postId', '게시글 아이디', in_='uri'),
        parameter('title', '게시글 제목'),
        parameter('content', '게시글 내용')
    ],

    'responses': {
        '201': {
            'description': '게시글 수정 완료'
        },
        '204': {
            'description': '게시글 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

POST_DELETE = {
    'tags': ['Post'],
    'description': '게시물 삭제',
    'parameters': [
        jwt_header,
        parameter('postId', '게시글 아이디', in_='uri')
    ],

    'responses': {
        '201': {
            'description': '삭제 성공'
        },
        '204': {
            'description': '게시글 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
