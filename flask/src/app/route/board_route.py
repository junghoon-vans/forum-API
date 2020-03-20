from flask import request
from flask_restplus import Resource

from utils.restplus import BoardDto, DashBoardDto
from app.api.board_api import *

api = BoardDto.api
api2 = DashBoardDto.api
_board = BoardDto.board


@api.route('/')
@api.response(201, 'Create board successfully')
@api.response(401, 'Permission denied')
@api.response(403, 'Login required')
@api.response(409, 'Already existed board')
class CreateBoard(Resource):
    @api.doc('create a new board')
    @api.expect(_board, validate=True)
    def post(self):
        data = request.json
        return create_board(data['name'])

@api.route('/<int:page>')
class BoardList(Resource):
    @api.doc('listview about board')
    @api.marshal_list_with(_board, mask=None)
    def get(self, page):
        return get_board_list(page)

@api.route('/<string:board_name>')
@api.response(401, 'Permission denied')
@api.response(403, 'Login required')
@api.response(404, 'Undefined board')
class Board(Resource):
    @api.doc('update the board')
    @api.response(200, 'Update board successfully')
    @api.response(409, 'Already existed board')
    @api.expect(_board, validate=True)
    def put(self, board_name):
        data = request.json
        return update_board(data['name'], board_name)

    @api.doc('delete the board')
    @api.response(200, 'Delete board successfully')
    def delete(self, board_name):
        data = request.json
        return delete_board(board_name)

@api2.route('/all/<int:page>')
class Dashboard(Resource):
    @api2.doc('show dashboard')
    def get(self, page):
        return get_dashboard(page)