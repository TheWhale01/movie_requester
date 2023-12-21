from include import *
import models, schemas
from privilege import Privilege
from languages import Languages
from schemas import UserCreate, RequestCreate

def get_user_by_id(db: Session, user_id: int):
	return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
	return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: UserCreate):
	hashedpwd = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
	db_user = models.User(
		username=user.username,
		password = hashedpwd,
	)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)

def get_request_by_id(db: Session, request_id: int):
	return db.query(models.Request).filter(models.Request.id == request_id).first()

