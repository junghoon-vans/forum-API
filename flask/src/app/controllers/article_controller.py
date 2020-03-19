from flask import request
from flask_restplus import Resource

from utils.restplus import ArticleDto
from app.services.article_service import *

api = ArticleDto.api
_title = ArticleDto.title
_article = ArticleDto.article


@api.route('/<string:board_Name>')
class Main(Resource):
    @api.doc('listview about article')
    @api.marshal_list_with(_title)
    def get(self, board_Name):
        return get_article_list(board_Name)
    
    @api.doc('create a new article')
    @api.expect(_article, validate=True)
    def post(self, board_Name):
        data = request.json
        return create_article(data, board_Name)

@api.route('/<string:board_Name>/<int:article_id>')
class Detail(Resource):
    @api.doc('read the article')
    @api.marshal_with(_article)
    def get(self, board_Name, article_id):
        return get_article_one(board_Name, article_id)

    @api.doc('update the article')
    @api.expect(_article, validate=True)
    def put(self, board_Name, article_id):
        data = request.json
        return update_article(data, board_Name, article_id)

    @api.doc('delete the article')
    def delete(self, board_Name, article_id):
        return delete_article(board_Name, article_id)