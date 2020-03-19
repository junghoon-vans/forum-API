from flask import session as web_session
from sqlalchemy.orm.session import sessionmaker

from utils.sqlalchemy import engine
from utils.redis import RedisSession

from app.models import User, Board


Session = sessionmaker(bind=engine)
session = Session()
redisSession = RedisSession()

def create_board(name):
    user_name = redisSession.open_session(web_session['session'])
    if user_name:
        user = session.query(User).filter_by(fullname=user_name).first()
        board = Board(
            name = name,
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

def update_board(new_name, old_name):
    if 'session' in web_session:
        user_name = redisSession.open_session(web_session['session'])
        if user_name:
            user = session.query(User).filter_by(fullname=user_name).first()
            board = session.query(Board).filter_by(name=old_name).first()
            if board.master == user.id:
                board.name = new_name
                save(board)
                response = {
                    'status': 'success',
                    'message': 'Successfully Changed'
                }
                return response, 200


def save(data):
    session.add(data)
    session.commit()