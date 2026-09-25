from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
from sqlalchemy import select
from .config import settings
from jwt import jwt, PyJWTError
from datetime import UTC, datetime, timedelta
from ..models.user import User
from ..core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


# Extracts JWT from the Access Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")


async def get_user_by_id(user_id: str, db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(User).where(User.id == user_id))
    return query.scalar()


def create_access_token(data: dict):
    expire = datetime(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
 
    

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):
    credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        user = await get_user_by_id(user_id, db)
        if user is None:
            raise credentials_exception
        return user
    except PyJWTError:
        raise credentials_exception
