from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
from .config import settings
from pwdlib import PasswordHasher


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


hasher = PasswordHasher()



# Extracts JWT from the Access Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")


def create_access_token():
    pass

def verify_access_token():
    pass


def hash_password(password: str) -> str:
    return hasher.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return hasher.verify(plain_password, hashed_password)
    except Exception:
        return False


