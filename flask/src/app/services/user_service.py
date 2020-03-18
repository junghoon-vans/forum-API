from app.models import db
from app.models.user_model import User


def register(data):
    user = User.query.filter_by(fullname=data['fullname']).first()
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
    return User.query.all()

def save(data):
    db.session.add(data)
    db.session.commit()