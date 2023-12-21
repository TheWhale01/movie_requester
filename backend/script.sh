#!/bin/bash

cd /workspace/src

# Start FastAPI server
python3 -m pip install -r ../requirements.txt
python3 -m uvicorn main:app --host ${HOST} --port ${PORT} --reload
