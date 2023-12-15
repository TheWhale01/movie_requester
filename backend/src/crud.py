from sqlalchemy.orm import Session
from . import models, schemas
from .privilege import Privilege

def get_user_by_id(db: Session, user_id: int):
	return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
	return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
	return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
	hashed_passwd = user.password + "hashed" #TODO: ABSOLUTELY CHANGE THIS !
	user_token = 'genreted_token' #TODO: ABSOLUTELY CHANGE THIS !
	db_user = models.User(
		email=user.email,
		password=hashed_passwd,
		username=user.username,
		token=user_token,
		privilege=Privilege.STANDARD
	)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user

# def get_request_by_id(db: Session, request_id: int):
# 	return db.query(models.Request).filter(models.Request.id == request_id).first()

# def create_request(db: Session, request: schemas.RequestCreate, user_id: int):
# 	db_request = models.Request(**request.dict(), user_id=user_id)
# 	db.add(db_request)
# 	db.commit()
# 	db.refresh(db_request)
# 	return db_request
