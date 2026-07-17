from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://postgres:password@localhost:5432/infraportal"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass
