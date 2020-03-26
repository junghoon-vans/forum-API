from datetime import datetime
from utils import bcrypt
from utils.sqlalchemy import Base
import sqlalchemy as db


class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    
    def __init__(self, fullname, password, email):
        self.fullname = fullname
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.email = email

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Board(Base):
    __tablename__ = 'board'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    master = db.Column(db.Integer, db.ForeignKey('user.id'))

    articles = db.orm.relationship("Article", cascade="all, delete, save-update, delete-orphan")
    db.orm.relationship("User")

class Article(Base):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    board = db.Column(db.Integer, db.ForeignKey('board.id')) 
    writer = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    pub_date = db.Column(db.DateTime, default=datetime.now)

    db.orm.relationship("User")