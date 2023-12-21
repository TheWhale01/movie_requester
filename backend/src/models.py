from include import *
from database import Base

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String, unique=True, nullable=False)
	password = Column(String, nullable=False)
	privilege = Column(Integer, nullable=False)
	language = Column(String, nullable=False)
	profile_picture = Column(String)

	requests = relationship("Request", back_populates='user')

class Request(Base):
	__tablename__ = 'requests'

	id = Column(Integer, primary_key=True, index=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	tmdb_id = Column(Integer, nullable=False, unique=True)
	date = Column(String, nullable=False)
	status = Column(Integer, nullable=False)

	user = relationship("User", back_populates='requests')
