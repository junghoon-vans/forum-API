from flask import request
from flask_restplus import Resource

from app.dtos.board_dto import *
from app.services.board_service import create, get_board_list

api = BoardDto.api
_board = BoardDto.board


@api.route('/')
class Main(Resource):
    @api.doc('create a new board')
    @api.expect(_board, validate=True)
    def post(self):
        data = request.json
        return create(data)

    @api.doc('listview about board')
    @api.marshal_list_with(_board, envelope='data')
    def get(self):
        return get_board_list()
