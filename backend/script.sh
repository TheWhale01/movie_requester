#!/bin/bash

cd /workspace

# Start FastAPI server
python3 -m pip install -r requirements.txt
python3 -m uvicorn src.main:app --host ${HOST} --port ${PORT} --reload
