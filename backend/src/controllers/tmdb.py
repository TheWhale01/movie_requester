from include import *
from services.auth import get_current_user
from services.themoviedb import themoviedb
from services.db.models import User
from services.request import RequestService

router = APIRouter()

@router.get('/search')
async def search(query: str, include_adult: bool = False, requester: User = Depends(get_current_user)):
	response = themoviedb.search(query, requester.language, include_adult)
	data: dict = {
		'page': response['page'],
		'results': [],
		'total_pages': response['total_pages'],
		'total_results': response['total_results'],
	}
	for item in response['results']:
		title = ''
		type = Type.MOVIE
		nb_seasons = 0
		poster = 'https://artworks.thetvdb.com/banners/images/missing/movie.jpg'
		poster_found = False
		if item.get('poster_path') and item['poster_path']:
			poster = 'https://image.tmdb.org/t/p/original' + item['poster_path']
			poster_found = True	
		if item['media_type'] == 'movie':
			title = item['title']
		elif item['media_type'] == 'tv':
			title = item['name']	
			nb_seasons = themoviedb.get_tv_details(item['id'])['number_of_seasons']
			type = Type.TVSHOW
		data['results'].append({
			'title': title,
			'type': type,
			'nb_seasons': nb_seasons,
			'tmdb_id': item['id'],
			'poster': poster,
			'poster_found': poster_found,
			'requested': RequestService().is_already_in_db(item['id'])
		})
	return data

@router.get('/get_tv_details')
async def get_tv_details(id: int, requester: User = Depends(get_current_user)):
	response = themoviedb.get_tv_details(id, requester.language)
	return response

@router.get('/get_movie_details')
async def get_movie_details(id: int, requester: User = Depends(get_current_user)):
	response = themoviedb.get_movie_details(id, requester.language)
	return response