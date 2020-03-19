import os

from flask_script import Manager

from app import create_app
from utils.sqlalchemy import Base, engine


app = create_app(os.getenv('FLASK_CONFIG') or 'prod')
manager = Manager(app)

Base.metadata.create_all(engine)

@manager.command
def run():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
  manager.run()
