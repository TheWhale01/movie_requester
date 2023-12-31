from include import *
from services.auth import get_current_user
from services.themoviedb import themoviedb
from services.db.models import User

router = APIRouter()

@router.get('/search')
async def search(query: str, include_adult: bool = False, requester: User = Depends(get_current_user)):
	response = themoviedb.search(query, requester.language, include_adult)
	return response

@router.get('/get_tv_details')
async def get_tv_details(id: int, requester: User = Depends(get_current_user)):
	response = themoviedb.get_tv_details(id, requester.language)
	return response

@router.get('/get_movie_details')
async def get_movie_details(id: int, requester: User = Depends(get_current_user)):
	response = themoviedb.get_movie_details(id, requester.language)
	return response