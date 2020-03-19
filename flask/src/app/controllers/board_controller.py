from flask import request
from flask_restplus import Resource

from utils.restplus import BoardDto
from app.services.board_service import *

api = BoardDto.api
_board = BoardDto.board


@api.route('/')
class CreateBoard(Resource):
    @api.doc('create a new board')
    @api.expect(_board, validate=True)
    def post(self):
        data = request.json
        return create_board(data['name'])

@api.route('/<int:page>')
class BoardList(Resource):
    @api.doc('listview about board')
    @api.marshal_list_with(_board, envelope='data')
    def get(self, page):
        return get_board_list(page)

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

@api.route('/all/<int:page>')
class Dashboard(Resource):
    @api.doc('show dashboard')
    def get(self, page):
        return get_dashboard(page)