import requests
from include import *
from services.themoviedb import TheMovieDB
from services.db.schemas import Request
from services.user import get_user_by_id
from services.db.database import get_db

class Telegram:
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
        username = get_user_by_id(next(get_db()), request.user_id).username
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
