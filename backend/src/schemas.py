from pydantic import BaseModel

class UserBase(BaseModel):
	email: str
	username: str

class RequestBase(BaseModel):
	user_id: int
	theMovieDB: str
	date: str

class UserCreate(BaseModel):
	password: str
	token: str

class RequestCreate(BaseModel):
	pass

class Request(RequestBase):
	id: int
	status: int
	class COnfig:
		orm_mode = True

class User(UserBase):
	id: int
	requests: list[Request] = []
	privilege: int

	class Config:
		orm_mode = True
