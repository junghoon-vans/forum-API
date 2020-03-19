from flask import request
from flask_restplus import Resource

from utils.restplus import ArticleDto
from app.services.article_service import get_article_list, create_article

api = ArticleDto.api
_article = ArticleDto.article


@api.route('/<string:board_Name>')
class Main(Resource):
    @api.doc('listview about article')
    @api.marshal_list_with(_article, envelope='data')
    def get(self, board_Name):
        return get_article_list(board_Name)
    
    @api.doc('create a new article')
    @api.expect(_article, validate=True)
    def post(self, board_Name):
        data = request.json
        return create_article(data, board_Name)
