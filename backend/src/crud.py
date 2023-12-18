from .include import *
from . import models, schemas
from .privilege import Privilege

def get_user_by_id(db: Session, user_id: int):
	return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
	return db.query(models.User).filter(models.User.username == username).first()

# def get_request_by_id(db: Session, request_id: int):
#	return db.query(models.Request).filter(models.Request.id == request_id).first()

# def create_request(db: Session, request: schemas.RequestCreate, user_id: int):
#	db_request = models.Request(**request.dict(), user_id=user_id)
#	db.add(db_request)
#	db.commit()
#	db.refresh(db_request)
#	return db_request
