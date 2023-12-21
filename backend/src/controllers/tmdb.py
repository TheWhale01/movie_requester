from include import *
from services.auth import get_current_user
from services.themoviedb import themoviedb

router = APIRouter()

@router.get('/search')
async def search(query: str, include_adult: bool = False, requester: dict = Depends(get_current_user)):
	response = themoviedb.search(query, requester.language, include_adult)
	return response

@router.get('/get_tv_details')
async def get_tv_details(id: int, requester: dict = Depends(get_current_user)):
	response = themoviedb.get_tv_details(id, requester.language)
	return response
