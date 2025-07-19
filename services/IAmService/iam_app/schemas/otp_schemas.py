from pydantic import BaseModel, EmailStr


class OTPRequest(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True