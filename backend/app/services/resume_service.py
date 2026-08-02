import os
import shutil
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.repositories.resume_repository import ResumeRepository


class ResumeService:

    def __init__(self, db: Session):
        self.repo = ResumeRepository(db)

    def upload(self, file: UploadFile, user_id: int):

        extension = file.filename.split(".")[-1].lower()

        if extension not in ["pdf", "docx"]:
            raise ValueError("Only PDF and DOCX files are allowed.")

        unique_name = f"{uuid4()}.{extension}"

        save_path = os.path.join(
            "uploads",
            "resumes",
            unique_name,
        )

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        resume = Resume(
            user_id=user_id,
            filename=file.filename,
            filepath=save_path,
        )

        return self.repo.create(resume)