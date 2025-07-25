from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    SENDER_EMAIL: str
    SENDER_PASSWORD: str

    class Config:
        env_path = Path(__file__).resolve().parent.parent / ".env"
        load_dotenv(env_path)
        extra = "allow"


settings = Settings()
