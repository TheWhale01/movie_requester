from include import *
from services.db.database import Base

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String, unique=True, nullable=False)
	password = Column(String, nullable=False)
	privilege = Column(Integer, nullable=False)
	language = Column(String, nullable=False)
	profile_picture = Column(String)

	requests = relationship("Request", back_populates='user')
	telegram_settings = relationship('TelegramSettings', back_populates='user', uselist=False)

class Request(Base):
	__tablename__ = 'requests'

	id = Column(Integer, primary_key=True, index=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	note = Column(String)
	type = Column(Integer, nullable=False)
	tmdb_id = Column(Integer, nullable=False, unique=True, index=True)
	date = Column(String, nullable=False)
	status = Column(Integer, nullable=False)

	user = relationship("User", back_populates='requests')

class TelegramSettings(Base):
	__tablename__ = 'telegram_settings'

	id = Column(Integer, primary_key=True, index=True)
	chat_id = Column(String, nullable=False)
	bot_id = Column(String, nullable=False)
	active = Column(Boolean, nullable=False)
	user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False, index=True)

	user = relationship("User", back_populates='telegram_settings', uselist=False)
