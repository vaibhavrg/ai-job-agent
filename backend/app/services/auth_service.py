from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class AuthService:

    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register(self, data: UserCreate):

        existing = self.repo.get_by_email(data.email)

        if existing:
            raise ValueError("Email already registered")

        user = User(
            full_name=data.full_name,
            email=data.email,
            hashed_password=hash_password(data.password),
        )

        return self.repo.create(user)

    def login(self, email: str, password: str):

        user = self.repo.get_by_email(email)

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(password, user.hashed_password):
            raise ValueError("Invalid email or password")

        token = create_access_token(str(user.id))

        return {
            "access_token": token,
            "token_type": "bearer",
        }