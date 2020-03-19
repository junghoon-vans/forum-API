from flask import session as flask_session
from sqlalchemy.orm.session import sessionmaker

from utils.sqlalchemy import engine
from utils.redis import RedisSession

from app.models.user_model import User


Session = sessionmaker(bind=engine)
session = Session()

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
    if not user:
        if user.verify_password(data['password']):
            redisSession = RedisSession()
            session_key = redisSession.create_session(user.fullname)
            flask_session['session'] = session_key

            response = {
                    'status': 'success',
                    'message': 'Successfully logged in'
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



def get_user_list():
    return session.query(User).all()

def save(data):
    session.add(data)
    session.commit()