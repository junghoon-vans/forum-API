from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import mode
from app.models import db

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(mode[config_name])
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app