from pydantic import BaseModel, EmailStr


class OTPRequest(BaseModel):
    email: EmailStr
    otp:str

    class Config:
        from_attributes = True