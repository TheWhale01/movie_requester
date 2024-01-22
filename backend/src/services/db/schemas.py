from pydantic import BaseModel

class TelegramSettingsBase(BaseModel):
	chat_id: str
	bot_id: str

class TelegramSettingsCreate(TelegramSettingsBase):
	pass

class TelegramSettings(TelegramSettingsBase):
	id: int
	active: bool

	class Config:
		from_attributes = True

class RequestBase(BaseModel):
	tmdb_id: int
	note: str | None
	type: int

class RequestCreate(RequestBase):
	pass

class Request(RequestBase):
	id: int
	date: str
	user_id: int
	status: int

class UserBase(BaseModel):
	username: str

class UserCreate(UserBase):
	password: str

class User(UserBase):
	id: int
	language: str
	privilege: int
	profile_picture: str | None

	class Config:
		from_attributes = True
