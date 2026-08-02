from fastapi import FastAPI

from app.db.session import create_database

app = FastAPI(
    title="AI Job Agent",
    version="1.0.0"
)


@app.on_event("startup")
def startup():

    create_database()


@app.get("/")
def home():

    return {
        "message": "AI Job Agent Backend Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }