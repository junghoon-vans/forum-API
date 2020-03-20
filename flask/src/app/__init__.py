from flask import Flask
from flask_restplus import Api

from app.config import mode

from app.route.user_route import api as user_ns
from app.route.board_route import api as board_ns
from app.route.board_route import api2 as dashboard_ns
from app.route.article_route import api as article_ns

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(mode[config_name])
    app.app_context().push()

    api = Api(app, 
          version='1.0',
          title='Forum API',
          description='flask-based bulletin board service API',
          )
    api.add_namespace(user_ns, path='/user')
    api.add_namespace(board_ns, path='/board')
    api.add_namespace(dashboard_ns, path='/board')
    api.add_namespace(article_ns, path='/board')

    return app