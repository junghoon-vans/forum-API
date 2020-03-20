from flask import request
from flask_restplus import Resource

from utils.restplus import ArticleDto
from app.api.article_api import *

api = ArticleDto.api
_article = ArticleDto.article


@api.route('/<string:board_Name>')
@api.response(201, 'Create article successfully')
@api.response(401, 'Permission denied')
@api.response(403, 'Login required')
class CreateArticle(Resource):
    @api.doc('create a new article')
    @api.expect(_article, validate=True)
    def post(self, board_Name):
        data = request.json
        return create_article(data, board_Name)

@api.route('/<string:board_Name>/<int:page>')
class ArticleList(Resource):
    def get(self, board_Name, page):
        return get_article_list(board_Name, page)

@api.route('/<string:board_Name>/detail/<int:article_id>')
class Article(Resource):
    @api.doc('read the article')
    def get(self, board_Name, article_id):
        return get_article_one(board_Name, article_id)

    @api.doc('update the article')
    @api.response(200, 'Update article successfully')
    @api.response(401, 'Permission denied')
    @api.response(403, 'Login required')
    @api.response(404, 'Undefined article')
    @api.expect(_article, validate=True)
    def put(self, board_Name, article_id):
        data = request.json
        return update_article(data, board_Name, article_id)

    @api.doc('delete the article')
    @api.response(200, 'Delete article successfully')
    @api.response(401, 'Permission denied')
    @api.response(403, 'Login required')
    @api.response(404, 'Undefined article')
    def delete(self, board_Name, article_id):
        return delete_article(board_Name, article_id)