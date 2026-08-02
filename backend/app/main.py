from fastapi import FastAPI

from app.core.settings import settings
from app.db.base import Base
from app.db.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
def home():
    return {
        "message": "AI Job Agent API",
        "version": settings.APP_VERSION,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }