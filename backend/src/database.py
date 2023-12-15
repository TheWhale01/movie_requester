import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = f'postgresql://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}/{os.environ["DB_NAME"]}'

engine = create_engine(
	DB_URL
)

SessionLocal =  sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
