from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.resume import Resume
from app.schemas.job_match import JobMatchRequest
from app.services.ai_service import AIService
from app.services.job_match_service import JobMatchService
from app.services.parser_service import ParserService

router = APIRouter(prefix="/match", tags=["Job Matching"])


@router.post("/{resume_id}")
def match_resume(
    resume_id: int,
    request: JobMatchRequest,
    db: Session = Depends(get_db),
):

    resume = db.query(Resume).filter(
        Resume.id == resume_id
    ).first()

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    parser = ParserService()

    resume_text = parser.extract_text(resume.filepath)

    ai = AIService()

    result = ai.match_resume_with_job(
        resume_text,
        request.job_description,
    )

    JobMatchService().save_match(
        db=db,
        resume_id=resume.id,
        job_description=request.job_description,
        result=result,
    )

    return result