from include import *
from services.user import get_user_by_id
from services.db.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# TODO: Generate JWT_SECRET instead of getting it from env
def create_jwt_token(user_id: int):
    exp_time = datetime.utcnow() + timedelta(minutes=15)
    payload = {'sub': str(user_id), 'exp': exp_time}
    token = jwt.encode(payload, environ['JWT_SECRET'], algorithm=environ['JWT_ALGORITHM'])
    return token

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    creds_exception = HTTPException(status_code=401,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'})
    try:
        payload = jwt.decode(token, environ['JWT_SECRET'], algorithms=[environ['JWT_ALGORITHM']])
        user_id: str = payload.get('sub')
        if user_id is None:
            raise creds_exception
    except jwt.PyJWTError:
        raise creds_exception
    user = get_user_by_id(db, user_id)
    if user is None:
        raise creds_exception
    return user

