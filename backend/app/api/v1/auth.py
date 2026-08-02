from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest, Token
from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])

@router.post("/login", response_model=Token)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    try:
        return service.login(
            data.email,
            data.password,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )

@router.post("/register", response_model=UserResponse)
def register(
    data: UserCreate,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    try:
        return service.register(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))