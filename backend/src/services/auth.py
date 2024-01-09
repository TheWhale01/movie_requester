from include import *
from services.db.database import get_db
from services.db import models
from services.user import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def create_jwt_token(user_id: int):
    exp_time = datetime.utcnow() + timedelta(minutes=60)
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
    user = UserService().get_by_id_full(user_id) 
    if user is None:
        raise creds_exception
    return user

