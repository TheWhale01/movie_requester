from include import *
from services.db.schemas import UserCreate
from services.db import models

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
