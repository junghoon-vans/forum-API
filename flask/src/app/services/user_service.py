from sqlalchemy.orm.session import sessionmaker
from utils.sqlalchemy import engine
from app.models.user_model import User

Session = sessionmaker(bind=engine)
session = Session()

def register(data):
    user = session.query(User).filter_by(fullname=data['fullname']).first()
    if not user:
        new_user = User(
            fullname = data['fullname'],
            password = data['password'],
            email = data['email']
        )
        save(new_user)
        response = {
            'status': 'success',
            'message': 'Successfully registered'
        }
        return response, 201
    else:
        response = {
            'status': 'fail',
            'message': 'User already exists'
        }
        return response, 409

def get_user_list():
    return session.query(User).all()

def save(data):
    session.add(data)
    session.commit()