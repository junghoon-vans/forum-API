import os
basedir = os.path.abspath(os.path.dirname(__file__))
# postgres_local_base = os.environ['DATABASE_URL']


class Config:
	SECRET_KEY = os.urandom(16)
	DEBUG = False


class DevelopmentConfig(Config):
	DEBUG = True

class ProductionConfig(Config):
	DEBUG = False
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
	dev=DevelopmentConfig,
	prod=ProductionConfig
)

key = Config.SECRET_KEY