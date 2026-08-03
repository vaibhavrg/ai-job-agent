from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import JSON

from datetime import datetime

from app.db.database import Base


class JobMatch(Base):
    __tablename__ = "job_matches"

    id = Column(Integer, primary_key=True, index=True)

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id"),
        nullable=False,
    )

    job_description = Column(Text, nullable=False)

    match_score = Column(Integer)

    matching_skills = Column(JSON)

    missing_skills = Column(JSON)

    recommendations = Column(JSON)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )