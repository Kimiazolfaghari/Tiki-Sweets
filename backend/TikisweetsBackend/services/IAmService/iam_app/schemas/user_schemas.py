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
    is_vip: bool
    image: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True


#class OTPVerify(BaseModel):
   # email: EmailStr
   # code: constr[min_length=4, max_length=4]

#class ResetPasswordRequest(BaseModel):
   # email: EmailStr

#class ResetPasswordConfirm(BaseModel):
   # email: EmailStr
   # code: constr(min_length=4, max_length=4)
   # new_password: constr[min_length=6]
