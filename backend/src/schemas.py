from pydantic import BaseModel

class UserBase(BaseModel):
	username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
	id: int
	# requests: list[Request] = []
	privilege: int

	class Config:
		from_attributes = True

# class RequestBase(BaseModel):
# 	user_id: int
# 	theMovieDB: str
# 	date: str

# class RequestCreate(RequestBase):
# 	pass

# class Request(RequestBase):
# 	id: int
# 	status: int
# 	class Config:
# 		from_attributes = True
