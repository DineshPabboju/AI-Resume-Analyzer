from fastapi import APIRouter, Depends


router = APIRouter(
    tags=["Auth"],
    prefix="/auth"
)
