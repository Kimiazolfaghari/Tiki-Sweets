from datetime import datetime
from pydantic import BaseModel, EmailStr, constr


class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    phone: constr(max_length =20)
    password: constr(min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str
    created_at: datetime

class UserUpdate(BaseModel):
    full_name: str | None = None
    password: str | None = None
    phone: str | None = None

class Config:
        from_attributes = True


