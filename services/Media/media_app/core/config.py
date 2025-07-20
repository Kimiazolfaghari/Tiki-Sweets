import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    storage_path: str = os.getenv("STORAGE_PATH", "storage")

settings = Settings()
