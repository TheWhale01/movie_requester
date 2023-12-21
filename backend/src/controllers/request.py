from include import *
from services.request import RequestService
from services.db.schemas import User, RequestCreate
from services.db.database import get_db
from services.auth import get_current_user
from services.user import get_user_by_username

router = APIRouter()

@router.post('/request/add')
async def add_request(request: RequestCreate, user: User = Depends(get_current_user)):
	request = RequestService().create(request, user)
	return {'request': request}

@router.delete('/request/remove')
async def remove_request(id: int, user: User = Depends(get_current_user)):
	RequestService().delete(id, user)

@router.patch('/request/update')
async def update_request(id: int, status: int, user: User = Depends(get_current_user)):
	RequestService().update(id, user, status)
