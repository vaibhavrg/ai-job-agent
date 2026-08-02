from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.schemas.resume import ResumeResponse
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/api/v1/resumes",
    tags=["Resumes"],
)


@router.post("/upload", response_model=ResumeResponse)
def upload_resume(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = ResumeService(db)

    try:
        return service.upload(file, current_user.id)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )