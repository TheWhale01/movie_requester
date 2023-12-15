from pydantic import BaseModel

class UserBase(BaseModel):
	email: str
	username: str
	password: str

class UserCreate(UserBase):
	pass

class User(UserBase):
	id: int
	token: str
	# requests: list[Request] = []
	privilege: int

	class Config:
		orm_mode = True

# class RequestBase(BaseModel):
# 	user_id: int
# 	theMovieDB: str
# 	date: str

# class RequestCreate(RequestBase):
# 	pass

# class Request(RequestBase):
# 	id: int
# 	status: int
# 	class COnfig:
# 		orm_mode = True