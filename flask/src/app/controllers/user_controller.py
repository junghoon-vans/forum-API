from flask import request
from flask_restplus import Resource

from app.dtos.user_dto import UserDto
from app.services.user_service import register, get_user_list


api = UserDto.api
_user = UserDto.user

@api.route('/')
class User(Resource):
    @api.doc('list_of_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return get_user_list()

@api.route('/register')
class User(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return register(data)
