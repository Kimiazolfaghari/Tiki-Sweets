from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MediaCreate(BaseModel):
    related_type: str
    related_id: int

class MediaOut(BaseModel):
    id: int
    filename: str
    filepath: str
    filetype: Optional[str]
    uploader_id: Optional[int]
    upload_date: datetime
    related_type: str
    related_id: int

    class Config:
        from_attributes = True
