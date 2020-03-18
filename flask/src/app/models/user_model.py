from . import bcrypt
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db


Base = declarative_base()
class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    
    def __init__(self, fullname, password, email):
        self.fullname = fullname
        self.password = password
        self.email = email
    
    @property
    def password_hash(self):
        return self.password
        
    @password_hash.setter
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)