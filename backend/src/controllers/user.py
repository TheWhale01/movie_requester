from include import *
from services.auth import get_current_user, create_jwt_token
from services.db.database import get_db
from services.db.schemas import UserCreate
from services.user import get_user_by_username, get_user_by_id, create_user

router = APIRouter()

@router.get('/login')
async def login_from_token(current_user: dict = Depends(get_current_user)):
	return {'user': current_user}

@router.post('/login')
async def login(user: UserCreate, db: Session = Depends(get_db)):
	db_user = get_user_by_username(db, user.username)
	if not db_user:
		raise HTTPException(status_code=401, detail='No such user')
	if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
		raise HTTPException(status_code=401, detail='Wrong password')
	token = create_jwt_token(db_user.id)
	return {'user': db_user, 'token': token}

@router.post('/signup')
async def singup(user: UserCreate, db: Session = Depends(get_db)):
	create_user(db, user)

@router.get('/user')
async def get_user(id: int, db: Session = Depends(get_db)):
	return {'user': get_user_by_id(id)}
