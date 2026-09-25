from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.oauth2 import get_current_user
from app.models.resume import Resume
from app.models.user import User
from app.services.storage import save_upload


router = APIRouter(
    tags=["Resumes"],
    prefix="/resume"
)


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_resume(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        storage_path = await save_upload(file, current_user.id)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)) from error

    resume = Resume(
        user_id=current_user.id,
        title=Path(file.filename or "resume").stem,
        storage_path=str(storage_path),
        file_name=file.filename or storage_path.name,
        file_type=file.content_type or "application/octet-stream",
    )
    db.add(resume)

    try:
        await db.commit()
        await db.refresh(resume)
    except Exception:
        await db.rollback()
        storage_path.unlink(missing_ok=True)
        raise

    return {
        "id": str(resume.id),
        "title": resume.title,
        "file_name": resume.file_name,
        "file_type": resume.file_type,
        "storage_path": resume.storage_path,
        "uploaded_at": resume.uploaded_at,
    }



