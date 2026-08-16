from .endpoints import analysis, auth, resumes
from fastapi import APIRouter

router = APIRouter(
    prefix="/v1"
)

router.include_router(analysis.router)
router.include_router(auth.router)
router.include_router(resumes.router)