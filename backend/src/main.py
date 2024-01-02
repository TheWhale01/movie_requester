from include import *
from services.db import models
from services.db.database import engine
from services.themoviedb import TheMovieDB
from controllers import user, request, tmdb, telegram

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(request.router)
app.include_router(tmdb.router)
app.include_router(telegram.router)
