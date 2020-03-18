from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'fullname': fields.String(required=True, description='user fullname'),
        'password': fields.String(required=True, description='user password'),
        'email': fields.String(required=True, description='user email address'),
    })