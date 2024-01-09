import requests
from include import *
from services.themoviedb import TheMovieDB
from services.db import models
from services.db.schemas import Request, TelegramSettingsCreate, User
from services.user import UserService
from services.db.database import get_db
from services.auth import get_current_user

class TelegramService:
	def __init__(self):
		self.__db: Session = next(get_db())
	
	def get_by_user_id(self, user_id: int):
		return self.__db.query(models.TelegramSettings).filter(models.TelegramSettings.user_id == user_id).first()
	
	def get_by_id(self, id: int):
		return self.__db.query(models.TelegramSettings).filter(models.TelegramSettings.id == id).first()

	def exists(self, id: int):
		return 

	def create(self, settings: TelegramSettingsCreate, user: User):
		if self.__db.query(exists().where(models.TelegramSettings.user_id == user.id)).scalar():
			return
		db_settings = models.TelegramSettings(
			**settings.model_dump(),
			active=True,
			user_id=user.id
		)
		self.__db.add(db_settings)
		self.__db.commit()
		self.__db.refresh(db_settings)
		return db_settings
	
	def deactivate(self, user_id: int):
		db_settings = self.get_by_user_id(user_id)	
		if not db_settings:
			raise HTTPException(status_code=401, detail='settings not found for user')
		elif not db_settings.active:
			raise HTTPException(status_code=401, detail='settings already deactivated')
		db_settings.active = False
		self.__db.commit()
		self.__db.refresh(db_settings)
		return db_settings
	
	def activate(self, user_id: int):
		db_settings = self.get_by_user_id(user_id)
		if not db_settings:
			raise HTTPException(status_code=401, detail='settings not found for user')
		elif db_settings.active:
			raise HTTPException(status_code=401, detail='settings already activated')
		db_settings.active = True
		self.__db.commit()
		self.__db.refresh(db_settings)
		return db_settings

	def update(self, user_id: int, settings: TelegramSettingsCreate):
		db_settings = self.get_by_user_id(user_id)
		db_settings.chat_id = settings.chat_id
		db_settings.bot_id = settings.bot_id
		self.__db.commit()
		self.__db.refresh(db_settings);
		return db_settings
	
	def new_request(self, request: Request):
		data = {"ok": True, "error": None, "user": None}
		admins = self.__db.query(models.User).filter(models.User.privilege == Privilege.ADMIN).all()
		for admin in admins:
			if admin.telegram_settings and admin.telegram_settings.active:
				helper = TelegramHelper(admin.telegram_settings.bot_id, admin.telegram_settings.chat_id)
				response = helper.new_request(request)
				if not response['ok']:
					data['ok'] = False
					data['error'] = response['detail']
					data['user'] = UserService.partial(admin)
		return data

class TelegramHelper:
    def __init__(self, bot_token, chat_id):
        self.__bot_token = bot_token
        self.__api_endpoint = f'https://api.telegram.org/bot{self.__bot_token}/sendPhoto'
        self.__chat_id = chat_id
    
    def new_request(self, request: Request):
        if not self.__bot_token or not self.__chat_id:
            raise HTTPException(401, detail='Could not get telegram settings')
        type, title, media, username, status = self.__get_media_infos(request)
        poster = 'https://image.tmdb.org/t/p/original' + media['poster_path']
        params = {
            'chat_id': self.__chat_id,
            'photo': poster,
            'caption': f"""*New {type} Request - {media[title]}*
{self.__escape_markdown(media['overview'])}

*Requested By:* {username}
*Request Status:* {status}""",
            'parse_mode': 'Markdown'
        }
        response = requests.post(self.__api_endpoint, params=params)
        return response.json()

    def __get_media_infos(self, request: Request):
        media = None
        status = ''
        type = ''
        title = ''
        username = UserService().get_by_id(request.user_id).username
        if request.type == Type.MOVIE:
            media = TheMovieDB().get_movie_details(request.tmdb_id)
            type = 'Movie'
            title = 'title'
        elif request.type == Type.TVSHOW:
            media = TheMovieDB().get_tv_details(request.tmdb_id)
            type = 'TV Show'
            title = 'name'
        if request.status == Status.ACCEPTED:
            status = 'Accepted'
        elif request.status == Status.FINISHED:
            status = 'Finished'
        elif request.status == Status.PENDING:
            status = 'Pending'
        elif request.status == Status.REFUSED:
            status = 'Refused'
        return (type, title, media, username, status)

    def __escape_markdown(self, text: str, version: int = 1, entity_type: str = None) -> str:
        if int(version) == 1:
            escape_chars = r'_*`['
        elif int(version) == 2:
            if entity_type in ['pre', 'code']:
                escape_chars = r'\`'
            elif entity_type == 'text_link':
                escape_chars = r'\)'
            else:
                escape_chars = r'_*[]()~`>#+-=|{}.!'
        else:
            raise ValueError('Markdown version must be either 1 or 2!')
        return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)
