from .include import *

DB_URL = f'postgresql://{environ["DB_USERNAME"]}:{environ["DB_PASSWORD"]}@{environ["DB_HOST"]}/{environ["DB_NAME"]}'

engine = create_engine(
	DB_URL
)

SessionLocal =  sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
