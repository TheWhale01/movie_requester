# Movie Requester
This project is inspired by overseerr.
The goal of this project is to be a small and lighweight replacement
for the overseerr/jellyseerr project. For those who have some DNS filtering
server, maybe overseerr didn't work for you. So I came with this small
replacement. Hope you'll enjoy it.

## How to start ?
1) Requirements
	1. [docker](https://www.docker.com/)
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
