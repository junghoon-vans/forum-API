from flask import session as web_session
from utils.sqlalchemy import engine, session, save, delete
from utils.redis import RedisSession

from app.models import Article


redisSession = RedisSession()

def create_article(data, board_Name):
    if 'session' in web_session:
        user_id = redisSession.open_session(web_session['session'])
        if user_id:
            article = Article(
                board = board_Name,
                writer = user_id,
                title = data['title'],
                content = data['content']
            )
            save(article)
            response = {
                'status': 'success',
                'message': 'Create article successfully'
            }
            return response, 201
        else:
            response = {
                'status': 'fail',
                'message': 'Permission denied'
            }
            return response, 401
    else:
        response = {
            'status': 'fail',
            'message': 'Login required'
        }
        return response, 403
    

def update_article(data, board_Name, article_id):
    article = get_article_one(board_Name, article_id)
    if article:
        if 'session' in web_session:
            user_id = redisSession.open_session(web_session['session'])
            if article.writer == int(user_id):
                article.title = data['title']
                article.content = data['content']
                save(article)
                response = {
                    'status': 'success',
                    'message': 'Update article successfully'
                }
                return response, 201
            else:
                response = {
                    'status': 'fail',
                    'message': 'Permission denied'
                }
                return response, 401
        else:
            response = {
                'status': 'fail',
                'message': 'Login required'
            }
            return response, 403
    else:
        response = {
            'status': 'fail',
            'message': 'Undefined article'
        }
        return response, 404

def delete_article(board_Name, article_id):
    article = get_article_one(board_Name, article_id)
    if article:
        if 'session' in web_session:
            user_id = redisSession.open_session(web_session['session'])
            if article.writer == int(user_id):
                delete(article)
                response = {
                    'status': 'success',
                    'message': 'Delete article successfully'
                }
                return response, 200
            else:
                response = {
                    'status': 'fail',
                    'message': 'Permission denied'
                }
                return response, 401
        else:
            response = {
                'status': 'fail',
                'message': 'Login required'
            }
            return response, 403
    else:
        response = {
            'status': 'fail',
            'message': 'Undefined article'
        }
        return response, 404

def get_article_one(board_Name, article_id):
    return session.query(Article).filter_by(board=board_Name, id=article_id).first()

def get_article(board_Name):
    return session.query(Article).filter_by(board=board_Name).order_by(Article.pub_date.desc())[0:5]

def get_article_list(board_Name, page):
    offset = 5
    return session.query(Article).filter_by(board=board_Name).order_by(Article.pub_date.desc())[page*5-offset:offset*page]