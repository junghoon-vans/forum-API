from flask import session as web_session
from utils.sqlalchemy import engine, session, save, delete

from utils.sqlalchemy import engine
from utils.redis import RedisSession

from app.models import User


redisSession = RedisSession()

def register(data):
    user = session.query(User).filter_by(fullname=data['fullname']).first()
    if not user:
        new_user = User(
            fullname = data['fullname'],
            password = data['password'],
            email = data['email']
        )
        save(new_user)
        response = {
            'status': 'success',
            'message': 'Successfully registered'
        }
        return response, 201
    else:
        response = {
            'status': 'fail',
            'message': 'User already exists'
        }
        return response, 409

def login(data):
    user = session.query(User).filter_by(email=data['email']).first()
    if user:
        if user.verify_password(data['password']):
            session_key = redisSession.create_session(user.id)
            web_session['session'] = session_key

            response = {
                    'status': 'success',
                    'message': 'Successfully Logged in'
                }
            return response, 200
        else:
            response = {
            'status': 'fail',
            'message': 'Invalid Password'
            }
            return response, 409
    else:
        response = {
            'status': 'fail',
            'message': 'Undefined User'
        }
        return response, 404

def logout():
    if 'session' in web_session and redisSession.open_session(web_session['session']):
        redisSession.delete_session(web_session['session'])
        del web_session['session']
        response = {
            'status': 'success',
            'message': 'Successfully Logged out'
        }
        return response, 200
    else:
        response = {
            'status': 'fail',
            'message': 'Already Logged out'
        }
        return response, 404
