from flask_restplus import Namespace, fields

class BoardDto():
    api = Namespace('board', description='board related operations')
    board = api.model('board', {
        'name': fields.String(required=True, description='board name'),
    })