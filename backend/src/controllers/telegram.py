from include import *
from services.telegram import Telegram
from services.db.schemas import User, Request
from services.db import models
from services.auth import get_current_user
from services.db.database import get_db

router = APIRouter()

@router.post('/telegram/new_request')
async def sendmsg(request: Request, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    setting = db.query(models.TelegramSettings).one()
    if not setting or not setting.active:
        raise HTTPException(401, detail='Could not find telegram setting. Please activate it')
    tlgrm = Telegram(setting.bot_id, setting.chat_id)
    return tlgrm.new_request(request)

@router.post('/telegram/activate')
async def activate(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if user.privilege != Privilege.ADMIN:
        raise HTTPException(401, detail='Only admins can modify telegram settings')
    db_setting = models.TelegramSettings(active=True)
    db.add(db_setting)
    db.commit()
    db.refresh(db_setting)
    return db_setting

@router.post('/telegram/disable')
async def disable(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if user.privilege != Privilege.ADMIN:
        raise HTTPException(401, detail='Only admins can modify telegram settings')
    db_setting = models.TelegramSettings(active=False)
    db.add(db_setting)
    db.commit()
    db.refresh(db_setting)
    return db_setting

@router.patch('/telegram/chat_update')
async def chat_update(id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if user.privilege != Privilege.ADMIN:
        raise HTTPException(401, detail='Only admins can modify telegram settings')
    setting = db.query(models.TelegramSettings).first()
    if not setting or not setting.active:
        raise HTTPException(401, detail='Coult not find telegram setting')
    setting.chat_id = id
    db.commit()
    return setting

@router.patch('/telegram/bot_update')
async def bot_update(id: str, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if user.privilege != Privilege.ADMIN:
        raise HTTPException(401, detail='Only admins can modify telegram settings')
    setting = db.query(models.TelegramSettings).one()
    if not setting or not setting.active:
        raise HTTPException(401, detail='Coult not find telegram setting')
    setting.bot_id = id
    db.commit()
    return setting
