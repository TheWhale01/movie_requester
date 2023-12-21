from pydantic import BaseModel

class RequestBase(BaseModel):
	tmdb_id: int
	user_id: int

class RequestCreate(RequestBase):
	pass

class Request(RequestBase):
	id: int
	date: str
	status: int

class UserBase(BaseModel):
	username: str

class UserCreate(UserBase):
	password: str

class User(UserBase):
	id: int
	language: str
	privilege: int
	profile_picture: str
	requests: list[Request] = []

	class Config:
		from_attributes = True
