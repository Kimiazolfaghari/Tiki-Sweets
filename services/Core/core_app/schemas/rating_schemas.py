from pydantic import BaseModel
from datetime import datetime

class RateCommentBase(BaseModel):
    comment: str
    rate_number: int

class RateCommentCreate(RateCommentBase):
    product_id: int
    user_id: int

class RateCommentOut(RateCommentBase):
    id: int
    date: datetime

class Config:
    from_attributes = True
