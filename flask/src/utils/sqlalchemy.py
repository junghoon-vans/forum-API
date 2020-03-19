import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

postgres_local_base = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
	user=os.environ['POSTGRES_USER'],
	pw=os.environ['POSTGRES_PASSWORD'],
	url=os.environ['POSTGRES_URL'],
	db=os.environ['POSTGRES_DB']
	)

engine = create_engine(postgres_local_base)
Base = declarative_base()