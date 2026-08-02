from pydantic import BaseModel, ConfigDict


class ResumeResponse(BaseModel):
    id: int
    filename: str
    filepath: str

    model_config = ConfigDict(from_attributes=True)