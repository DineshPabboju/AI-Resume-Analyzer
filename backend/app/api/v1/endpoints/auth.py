from fastapi import APIRouter, Depends, HTTPException, status
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from ....schemas.user import UserRegister, UserLogin
from ....core.security import hash_password, verify_password
from sqlalchemy.future import select
from ....models.user import User
from ....core.oauth2 import create_access_token



router = APIRouter(
    tags=["Auth"],
    prefix="/auth"
)



@router.post("/sign-up")
async def signup(credentials:UserRegister , db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(User).where(User.email == credentials.email))
    existing_user = query.scalar()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    password = hash_password(credentials.password)
    db.add(User(full_name=credentials.name, email=credentials.email, password=password))
    await db.commit()

@router.post("/login")
async def login(credentials:UserLogin, db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(User).where(User.email == credentials.email))
    user = query.scalar()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return {"message": "Login successful", "access_token": access_token, "token_type": "bearer"}
