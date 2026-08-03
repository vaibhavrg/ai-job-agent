from pydantic import BaseModel


class ResumeParseResponse(BaseModel):
    resume_id: int
    name: str | None
    email: str | None
    phone: str | None
    skills: list[str]