from flask import request
from flask_restplus import Resource

from utils.restplus import BoardDto
from app.services.board_service import create_board, get_board_list, update_board, delete_board

api = BoardDto.api
_board = BoardDto.board


@api.route('/')
class Main(Resource):
    @api.doc('create a new board')
    @api.expect(_board, validate=True)
    def post(self):
        data = request.json
        return create_board(data['name'])

    @api.doc('listview about board')
    @api.marshal_list_with(_board, envelope='data')
    def get(self):
        return get_board_list()

@api.route('/<string:board_name>')
class Detail(Resource):
    @api.doc('update the board')
    @api.expect(_board, validate=True)
    def put(self, board_name):
        data = request.json
        return update_board(data['name'], board_name)

    @api.doc('delete the board')
    def delete(self, board_name):
        data = request.json
        return delete_board(board_name)