def parameter(name, description, in_='json', type='str', required=True):
    return {
        'name': name,
        'description': description,
        'in': in_,
        'type': type,
        'required': required
    }


jwt_header = parameter('Authorization', 'JWT token (format: "Bearer 액세스 토큰")', 'header')
