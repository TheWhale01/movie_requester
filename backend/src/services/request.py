from include import *
from services.db import schemas, models
from services.db.database import get_db

class RequestService:
	def __init__(self):
		self.__db = next(get_db())

	def get_by_id(self, id: int):
		return self.__db.query(models.Request).filter(models.Request.id == id).first()

	def create(self, request: schemas.Request, user: schemas.User):
		request_status = None
		if user.privilege == Privilege.ADMIN:
			request_status = Status.ACCEPTED
		else:
			request_status = Status.PENDING
		db_request = models.Request(**request.dict(),
			user_id=user.id,
			date=datetime.now().strftime('%Y-%m-%d'),
			status=request_status,
		)
		self.__db.add(db_request)
		self.__db.commit()
		self.__db.refresh(db_request)
		return db_request

	def delete(self, id: int, user: schemas.User):
		db_request = self.get_by_id(id)
		if user.privilege != Privilege.ADMIN:
			raise HTTPException(status_code=401, detail='Only admins can delete requests')
		self.__db.delete(db_request)
		self.__db.commit()

	def update(self, id: int, user: schemas.User, status: int):
		if status != Status.PENDING and status != Status.ACCEPTED and status != Status.REFUSED:
			raise HTTPException(status_code=401, detail='Status not valid')
		db_request = self.get_by_id(id)
		if not db_request:
			raise HTTPException(status_code=401, detail='No such request')
		db_request.status = status;
		self.__db.commit()
		return db_request