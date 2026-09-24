from fastapi import APIRouter, Depends


router = APIRouter(
    tags=["Analysis"],
    prefix="/analysis"
)


@router.get("/")
async def get_analysis():
    return {
        "status": "success",
        "message": "Analysis endpoint is working fine.",
        "version": "1.0.0"
    }
    
