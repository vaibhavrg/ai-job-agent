from app.db.database import Base
from app.models.resume import Resume
# Import all models here so SQLAlchemy can discover them
from app.models.user import User
from app.models.resume_analysis import ResumeAnalysis
from app.models.job_match import JobMatch
__all__ = [
    "Base",
    "User",
    "Resume",
]