from flask import jsonify
from flask import session as web_session
from utils.sqlalchemy import engine, session, save, delete

from utils.sqlalchemy import engine
from utils.redis import RedisSession

from app.models import Board
from .article_service import get_article

import json


redisSession = RedisSession()

def create_board(name):
    if 'session' in web_session:
        user_id = redisSession.open_session(web_session['session'])
        if user_id:
            board = Board(
                name = name,
                master = user_id
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
                'message': 'Unauthorized'
            }
            return response, 401
    else:
        response = {
            'status': 'fail',
            'message': 'Required Login'
        }
        return response, 400

def update_board(new_name, old_name):
    if 'session' in web_session:
        user_id = redisSession.open_session(web_session['session'])
        board = session.query(Board).filter_by(name=old_name).first()
        if board.master == int(user_id):
            board.name = new_name
            save(board)
            response = {
                'status': 'success',
                'message': 'Successfully Changed'
            }
            return response, 200
        else:
            response = {
                'status': 'fail',
                'message': 'Unauthorized'
            }
            return response, 401
    else:
        response = {
            'status': 'fail',
            'message': 'Required Login'
        }
        return response, 400

def delete_board(board_name):
    if 'session' in web_session:
        user_id = redisSession.open_session(web_session['session'])
        board = session.query(Board).filter_by(name=board_name).first()
        if board.master == int(user_id):
            delete(board)
            response = {
                'status': 'success',
                'message': 'Successfully Deleted'
            }
            return response, 200
        else:
            response = {
                'status': 'fail',
                'message': 'Unauthorized'
            }
            return response, 401
    else:
        response = {
            'status': 'fail',
            'message': 'Required Login'
        }
        return response, 400

def get_dashboard(page):
    data = dict()
    for board in get_board_list(page):
        article_list = list()
        for article in get_article(board.name):
            article_list.append(article.title)
        data[board.name] = article_list
    return jsonify(data)

def get_board_list(page):
    offset = 5
    return session.query(Board).order_by(Board.name)[page*5-offset:offset*page]