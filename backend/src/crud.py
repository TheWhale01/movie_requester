from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    # TODO: Generate a token to create a user
    hashed_passwd = user.password + "hashed" #TODO: ABSOLUTELY CHANGE THIS !
    db_user = models.User(email=user.email, password=hashed_passwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

