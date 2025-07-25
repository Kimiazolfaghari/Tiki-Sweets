from datetime import datetime

from pydantic import BaseModel, EmailStr


class AdminLogin(BaseModel):
    email: EmailStr
    password: str


class AdminOut(BaseModel):
    id: int
    email: str
    created_at: datetime


class Config:
    from_attributes = True