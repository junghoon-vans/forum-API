from flask import Flask
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from app.config import mode
from app.models import db

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(mode[config_name])
    app.app_context().push()

    api = Api(app, 
          version='1.0',
          title='Forum API',
          description='flask-based bulletin board service API',
          )

    db.init_app(app)
    return app