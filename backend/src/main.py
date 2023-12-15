import os
import uvicorn
from fastapi import FastAPI
from .database import SessionLocal, engine
from . import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def root():
	return {
		'message': 'Hello, World'
	}
