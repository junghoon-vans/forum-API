import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.urandom(16)
	DEBUG = False
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