# Movie Requester
This project is inspired by overseerr.
The goal of this project is to be a small and lighweight replacement
for the overseerr/jellyseerr project. For those who have some DNS filtering
server, maybe overseerr didn't work for you. So I came with this small
replacement. Hope you'll enjoy it.

## How to start ?
1) Requirements
	- [docker](https://www.docker.com/)
    - Create a TheMovieDB API key [here](https://developer.themoviedb.org/docs/getting-started)
2) setup
```shell
git clone https://github.com/TheWhale01/movie_requester.git
cd movie_requester
mkdir .env
cd .env
touch backend.env frontend.env database.env pgadmin.env
cd ../
```
You will have to populate the *.env files with these environment variables
- backend.env
	- HOST=
	- PORT=
	- DB_NAME=
	- DB_USERNAME=
	- DB_PASSWORD=
	- DB_PORT=
	- DB_HOST=
    - JWT_SECRET=
    - JWT_ALGORITHM=
    - THE_MOVIE_DB_KEY=
- frontend.env
	- VITE_PORT=
	- VITE_HOST=
	- VITE_BACKEND_HOST=
	- VITE_BACKEND_PORT=
- database.env
	- POSTGRES_DB=
	- POSTGRES_USER=
	- POSTGRES_PASSWORD=

***optional***
- pgadmin.env
	- PGADMIN_DEFAULT_EMAIL=
	- PGADMIN_DEFAULT_PASSWORD=
3) start
```shell
docker compose up --build -d
```

## Migrations
Database migrations are powered by alembic.
Unfortunately, for now, the database migration are not automatically applied to
the database.

Here are the steps to follow:

```shell
docker exec -it movie_requester_backend /bin/bash
cd src
python3 -m alembic revision --autogenerate -m "" #Put a message (like a git commit)
python3 -m alembic upgrade head #Applying last migration
exit
```

## TODO
Add filter on request for admins to show all requests or not
Add Notifications
Send notification when request's status has been changed

## OPTIMISATIONS
Do not re fetch all the requests from a user when one is deleted
Make mutliple pages when admin want to see all requests (Do not import all rows of the table)