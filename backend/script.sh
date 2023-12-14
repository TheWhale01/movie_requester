#!/bin/bash

cd /workspace

# Install psql (For client use)
#sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
#wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
#apt update ; apt upgrade -y ; apt install -y postgresql

# Start FastAPI server
python3 -m pip install -r requirements.txt
python3 -m uvicorn src.main:app --host ${HOST} --port ${PORT}
