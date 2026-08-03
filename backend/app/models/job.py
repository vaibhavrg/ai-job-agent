from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    company: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    location: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    salary: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )

    experience: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )

    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )

    source: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    posted_date: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )