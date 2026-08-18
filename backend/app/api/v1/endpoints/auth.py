from fastapi import APIRouter, Depends
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    tags=["Auth"],
    prefix="/auth"
)



@router.post("/sign-up")
async def signup(db: AsyncSession = Depends(get_db)):
    pass


@router.post("/login")
async def login(db: AsyncSession = Depends(get_db)):
    pass