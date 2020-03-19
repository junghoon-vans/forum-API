from utils import bcrypt
from utils.sqlalchemy import Base
import sqlalchemy as db


class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String, nullable=False, unique=True)
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

    name = db.Column(db.String, primary_key=True)
    master = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.orm.relationship("User")