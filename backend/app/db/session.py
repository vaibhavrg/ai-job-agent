from app.db.database import Base
from app.db.database import engine

from app.models.user import User


def create_database():
    Base.metadata.create_all(bind=engine)