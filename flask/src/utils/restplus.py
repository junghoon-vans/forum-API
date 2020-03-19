from flask_restplus import Namespace, fields

class UserDto():
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'fullname': fields.String(required=True, description='user fullname'),
        'password': fields.String(required=True, description='user password'),
        'email': fields.String(required=True, description='user email address'),
    })
    auth = api.model('auth', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
    })
    
class BoardDto():
    api = Namespace('board', description='board related operations')
    board = api.model('board', {
        'name': fields.String(required=True, description='board name'),
    })