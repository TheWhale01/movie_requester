from include import *
from services.auth import get_current_user, create_jwt_token
from services.db.database import get_db
from services.db.schemas import UserCreate, User
from services.user import get_user_by_username, get_user_by_id, create_user

router = APIRouter()

@router.get('/login')
async def login_from_token(current_user: dict = Depends(get_current_user)):
	return {'user': current_user}

@router.get('/user')
async def get_user(id: int, db: Session = Depends(get_db)):
	return {'user': get_user_by_id(db, id)}

@router.post('/login')
async def login(user: UserCreate, db: Session = Depends(get_db)):
	db_user = get_user_by_username(db, user.username)
	if not db_user:
		raise HTTPException(status_code=401, detail='No such user')
	if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
		raise HTTPException(status_code=401, detail='Wrong password')
	token = create_jwt_token(db_user.id)
	return {'user': db_user, 'token': token}

@router.post('/user/username')
async def change_username(username: str, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
	db_user = get_user_by_id(db, user.id)
	if get_user_by_username(db, username):
		raise HTTPException(status_code=401, detail='Username already taken')
	if not db_user:
		raise HTTPException(status_code=401, detail='No such user')
	db_user.username = username
	db.commit()
	db.refresh(db_user)
	return {'user': db_user}

@router.post('/user/create')
async def create_new_user(user: UserCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
	if current_user.privilege != Privilege.ADMIN:
		raise HTTPException(status_code=401, detail='Only admin can create new users')
	if get_user_by_username(db, user.username):
		raise HTTPException(status_code=401, detail='Username already taken')
	return create_user(db, user)

@router.post('/user/password')
async def change_password(params: dict,
						  user: User = Depends(get_current_user),
						  db: Session = Depends(get_db)):
	if not params.get('old_password') or not params.get('new_password'):
		raise HTTPException(status_code=401, detail='Missing body parameters: {"old_password": "", "new_password": ""}')
	if not bcrypt.checkpw(params['old_password'].encode(), user.password.encode()):
		raise HTTPException(status_code=401, detail='Wrong password')
	# TODO: Add verification for password syntax
	user.password = bcrypt.hashpw(params['new_password'].encode(), bcrypt.gensalt()).decode()
	db.commit()
	db.refresh(user)
	return {'user': user}
	