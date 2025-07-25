from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core_app.core.config import settings

DATABASE_URL = (
    f"postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}"
    f"@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)