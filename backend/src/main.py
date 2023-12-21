from include import *
from database import get_db, engine
import models
from schemas import UserCreate, RequestCreate
from crud import *
from auth import create_jwt_token, get_current_user
from themoviedb import TheMovieDB

from crud import create_user

models.Base.metadata.create_all(bind=engine)
themoviedb = TheMovieDB()

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get('/login')
async def login_from_token(current_user: dict = Depends(get_current_user)):
	return {'user': current_user}

@app.post('/login')
async def login(user: UserCreate, db: Session = Depends(get_db)):
	db_user = get_user_by_username(db, user.username)
	if not db_user:
		raise HTTPException(status_code=401, detail='No such user')
	if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
		raise HTTPException(status_code=401, detail='Wrong password')
	token = create_jwt_token(db_user.id)
	return {'user': db_user, 'token': token}

@app.get('/search')
async def search(query: str, include_adult: bool = False, requester: dict = Depends(get_current_user)):
	response = themoviedb.search(query, requester.language, include_adult)
	return response

@app.get('/get_tv_details')
async def get_tv_details(id: int, requester: dict = Depends(get_current_user)):
	response = themoviedb.get_tv_details(id, requester.language)
	return response

@app.post('request/add')
async def add_request(request: RequestCreate, db: Session = Depends(get_db)):
	pass

@app.post('/signup')
async def singup(user: UserCreate, db: Session = Depends(get_db)):
	create_user(db, user)