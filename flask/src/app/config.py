import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
	user=os.environ['POSTGRES_USER'],
	pw=os.environ['POSTGRES_PASSWORD'],
	url=os.environ['POSTGRES_URL'],
	db=os.environ['POSTGRES_DB']
	)

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