from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index=True)
	email = Column(String, unique=True, index=True)
	username = Column(String, unique=True)
	password = Column(String)
	token = Column(String, unique=True)
	privilege = Column(Integer)
# 	requests = relationship("Requests", back_populates='owner')

# class Request(Base):
# 	__tablename__ = 'requests'
# 	id = Column(Integer, primary_key=True, index=True)
# 	user_id = Column(Integer, ForeignKey('users.id'))
# 	theMovieDB = Column(String, unique=True)
# 	date = Column(String)
# 	status = Column(Integer)

# 	user = relationship("User", back_populates='requests')
