from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.core.settings import settings
from app.db.base import Base
from app.db.database import engine
from app.api.v1.resume import router as resume_router
from app.api.v1 import parser
from app.api.routes import job_match
# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Job Agent Backend API",
)

# Register API routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(resume_router)
app.include_router(parser.router, prefix="/api/v1")
app.include_router(job_match.router)

@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Welcome to AI Job Agent API",
        "version": settings.APP_VERSION,
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
    }