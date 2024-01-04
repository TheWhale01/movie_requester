from include import *
from services.auth import get_current_user
from services.db.schemas import UserCreate, User
from services.user import UserService

router = APIRouter()

@router.get('/login')
async def login_from_token(current_user = Depends(get_current_user)):
	return {'user': UserService().partial(current_user)}

@router.get('/user')
async def get_user(id: int):
	return {'user': UserService().get_by_id(id)}

@router.post('/login')
async def login(user: UserCreate):
	db_user, token = UserService().login(user)
	return {'user': db_user, 'token': token}
	
@router.post('/user/username')
async def change_username(username: str, user: User = Depends(get_current_user)):
	return {'user': UserService().change_username(user, username)}

@router.post('/user/create')
async def create_new_user(user: UserCreate, current_user: User = Depends(get_current_user)):
	if current_user.privilege != Privilege.ADMIN:
		raise HTTPException(status_code=401, detail='Only admin can create new users')
	if UserService().get_by_username(user.username):
		raise HTTPException(status_code=401, detail='Username already taken')
	return UserService().create(user)

@router.post('/user/password')
async def change_password(params: dict, user: User = Depends(get_current_user)):
	if not params.get('old_password') or not params.get('new_password'):
		raise HTTPException(status_code=401, detail='Missing body parameters: {"old_password": "", "new_password": ""}')
	return {'user': UserService().change_password(user, params['old_password'], params['new_password'])}	
	