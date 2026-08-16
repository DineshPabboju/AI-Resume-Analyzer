from fastapi import APIRouter, Depends


router = APIRouter(
    tags=["Resumes"],
    prefix="/resume"
)
