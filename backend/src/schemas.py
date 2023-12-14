from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(BaseModel):
    password: str
    token: str

class User(UserBase):
    id: int
    #requests: list[Request] = []
    privilege: int

    class Config:
        orm_mode = True
