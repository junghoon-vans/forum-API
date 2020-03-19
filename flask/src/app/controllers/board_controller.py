from flask import request
from flask_restplus import Resource

from app.dtos.board_dto import *
from app.services.board_service import create

api = BoardDto.api
_board = BoardDto.board

@api.route('/')
class Create(Resource):
    @api.doc('create a new board')
    @api.expect(_board, validate=True)
    def post(self):
        data = request.json
        return create(data)