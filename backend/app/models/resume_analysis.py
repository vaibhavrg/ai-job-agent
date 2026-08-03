from sqlalchemy import Column, ForeignKey, Integer, JSON, Text
from sqlalchemy.orm import relationship

from app.db.base import Base


class ResumeAnalysis(Base):
    __tablename__ = "resume_analyses"

    id = Column(Integer, primary_key=True, index=True)

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id"),
        nullable=False,
        unique=True,
    )

    summary = Column(Text)

    ats_score = Column(Integer)

    strengths = Column(JSON)

    missing_skills = Column(JSON)

    recommendations = Column(JSON)

    resume = relationship("Resume")