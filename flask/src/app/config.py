import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = os.environ['DATABASE_URL']


class Config:
	SECRET_KEY = os.urandom(16)
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = postgres_local_base
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SWAGGER_UI_DOC_EXPANSION = 'list'

class DevelopmentConfig(Config):
	DEBUG = True

class ProductionConfig(Config):
	DEBUG = False


mode = dict(
	dev=DevelopmentConfig,
	prod=ProductionConfig
)

key = Config.SECRET_KEY