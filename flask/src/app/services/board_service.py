from flask import session as web_session
from sqlalchemy.orm.session import sessionmaker

from utils.sqlalchemy import engine
from utils.redis import RedisSession

from app.models import User, Board


Session = sessionmaker(bind=engine)
session = Session()
redisSession = RedisSession()

def create(data):
    user_name = redisSession.open_session(web_session['session'])
    if user_name:
        user = session.query(User).filter_by(fullname=user_name).first()
        board = Board(
            name = data['name'],
            master = user.id
        )
        save(board)
        response = {
            'status': 'success',
            'message': 'Successfully Created'
        }
        return response, 201
    else:
        response = {
            'status': 'fail',
            'message': 'Login Required'
        }
        return response, 400

def get_board_list():
    return session.query(Board).all()

def save(data):
    session.add(data)
    session.commit()