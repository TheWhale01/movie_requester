from include import *
from services.telegram import TelegramService
from services.db.schemas import *
from services.db import models
from services.auth import get_current_user
from services.db.database import get_db

router = APIRouter()

@router.get('/telegram/get')
async def get_settings(user: User = Depends(get_current_user)):
	return {'settings': TelegramService().get_by_user_id(user.id)}

@router.post('/telegram/new_request')
async def new_request(request: Request):
	return TelegramService().new_request(request)

@router.post('/telegram/activate')
async def activate(user: User = Depends(get_current_user)):
	return {'settings': TelegramService().activate(user.id)}
	
@router.post('/telegram/deactivate')
async def deactivate(user: User = Depends(get_current_user)):
	return {'settings': TelegramService().deactivate(user.id)}
	
@router.post('/telegram/create')
async def create(settings: TelegramSettingsCreate, user: User = Depends(get_current_user)):
	settings = TelegramService().create(settings, user)
	return {'settings': settings}

@router.post('/telegram/update')
async def update(settings: TelegramSettingsCreate, user: User = Depends(get_current_user)):
	return {'settings': TelegramService().update(user.id, settings)}