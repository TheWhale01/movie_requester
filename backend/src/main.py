import os
import uvicorn
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from .database import SessionLocal, engine
from . import models
from .schemas import UserCreate, User
from .crud import create_user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@app.get('/')
async def root():
	return {
		'message': 'Hello, World'
	}

@app.post('/signup')
async def signup(user: UserCreate, db: Session = Depends(get_db)):
	return create_user(db, user)
