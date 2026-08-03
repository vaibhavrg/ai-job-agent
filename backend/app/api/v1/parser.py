from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.resume import Resume
from app.models.user import User
from app.schemas.parser import ResumeParseResponse
from app.services.parser_service import ParserService

router = APIRouter(prefix="/resumes", tags=["Resume Parser"])


@router.post("/{resume_id}/parse", response_model=ResumeParseResponse)
def parse_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    resume = (
        db.query(Resume)
        .filter(
            Resume.id == resume_id,
            Resume.user_id == current_user.id,
        )
        .first()
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    parser = ParserService()

    text = parser.extract_pdf_text(resume.filepath)

    return ResumeParseResponse(
        resume_id=resume.id,
        name=parser.extract_name(text),
        email=parser.extract_email(text),
        phone=parser.extract_phone(text),
        skills=parser.extract_skills(text),
    )