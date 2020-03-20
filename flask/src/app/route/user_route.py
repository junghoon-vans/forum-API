from flask import request
from flask_restplus import Resource

from utils.restplus import UserDto
from app.api.user_api import register, login, logout


api = UserDto.api
_user = UserDto.user
_auth = UserDto.auth


@api.route('/register')
class Register(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return register(data)

@api.route('/login')
class Login(Resource):
    @api.doc('login user')
    @api.expect(_auth, validate=True)
    def post(self):
        data = request.json
        return login(data)

@api.route('/logout')
class Logout(Resource):
    @api.doc('logout user')
    def get(self):
        return logout()