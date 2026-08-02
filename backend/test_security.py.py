from sqlalchemy import inspect

from app.db.database import engine

print("Database:", engine.url)

inspector = inspect(engine)

print("Tables:", inspector.get_table_names())