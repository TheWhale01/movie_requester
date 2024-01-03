from include import *
from services.db.schemas import UserCreate, User
from services.db import models

def get_user_by_id(db: Session, user_id: int):
	return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
	return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: UserCreate):
	#TODO: Check for password syntax (Raise HTTPException if not valid)
	hashedpwd = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
	db_user = models.User(
        language='fr-FR',
        privilege=Privilege.ADMIN,
		username=user.username,
		password = hashedpwd,
	)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user

def get_partial_user(user: models.User):
	pydantic_user = User.model_validate(user)
	return pydantic_user
