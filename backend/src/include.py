import re
import jwt
import sys
import json
import bcrypt
import requests
import urllib.parse
from os import environ, path
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Boolean, exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from enums.status import Status
from enums.type import Type
from enums.privilege import Privilege
from enums.languages import Languages
