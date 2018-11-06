from docs import parameter, jwt_header

POST_LIST_GET = {
    'tags': ['Post'],
    'description': '게시물 목록 조회',
    'parameters': [jwt_header],

    'responses': {
        '200': {
            'description': '조회 성공',
            'examples': {
                '': {
                    'posts': [
                        {
                            'title': '제목',
                            'author': '작성자'
                        },
                        {
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
        jwt_header,
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
                            'author': '댓글 작성자',
                            'content': '댓글 내용'
                        },
                        {
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
