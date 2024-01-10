from include import *
from services.db.schemas import UserCreate, User
from services.db import models
from services.db.database import get_db

class UserService:
	def __init__(self):
		self.__db = next(get_db())
	
	def partial(self, user: models.User):
		if not user:
			return ;
		pydantic_user = User.model_validate(user)
		return pydantic_user

	def get_by_id_full(self, user_id: int):
		return self.__db.query(models.User).filter(models.User.id == user_id).first()
	
	def get_by_username_full(self, username: str):
		return self.__db.query(models.User).filter(models.User.username == username).first()

	def get_by_id(self, user_id: int):
		return self.partial(self.get_by_id_full(user_id))
	
	def get_by_username(self, username: str):
		return self.partial(self.get_by_username_full(username))

	def create(self, user: UserCreate):
		# TODO: Check for password syntax
		hashedpwd = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
		db_user = models.User(
  	    	language='fr-FR',
        	privilege=Privilege.STANDARD,
			username=user.username,
			password = hashedpwd,
		)
		self.__db.add(db_user)
		self.__db.commit()
		self.__db.refresh(db_user)
		return db_user

	def login(self, user: UserCreate):
		from services.auth import create_jwt_token
		db_user: models.User = self.get_by_username_full(user.username)
		if not db_user:
			raise HTTPException(status_code=401, detail='No such user')
		if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
			raise HTTPException(status_code=401, detail='Wrong password')
		token = create_jwt_token(db_user.id)
		return self.partial(db_user), token

	def change_username(self, user: User, username: str):
		db_user = self.get_by_id_full(user.id)
		if self.get_by_username(username):
			raise HTTPException(status_code=401, detail='Username already taken')
		if not db_user:
			raise HTTPException(status_code=401, detail='No such user')
		db_user.username = username
		self.__db.commit()
		self.__db.refresh(db_user)
		return self.partial(db_user)
		 
	def change_password(self, user: User, old_password: str, new_password: str):
		if not bcrypt.checkpw(old_password.encode(), user.password.encode()):
			raise HTTPException(status_code=401, detail='Wrong password')
		user.password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
		self.__db.commit()
		return self.partial(user)
