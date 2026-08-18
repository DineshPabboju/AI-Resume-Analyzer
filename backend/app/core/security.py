from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
from .config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES





# Extracts JWT from the Access Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

