import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app
from app.models import db, user_model


app = create_app(os.getenv('FLASK_CONFIG') or 'prod')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
