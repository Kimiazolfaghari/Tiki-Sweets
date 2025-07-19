from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DiscountBase(BaseModel):
    code: str
    description: Optional[str] = None
    amount_of_discount: float
    start_date: datetime
    ending_date: datetime

class DiscountCreate(DiscountBase):
    user_id: int

class DiscountUpdate(BaseModel):
    code: Optional[str]
    description: Optional[str]
    amount_of_discount: Optional[float]
    start_date: Optional[datetime]
    ending_date: Optional[datetime]

class DiscountOut(DiscountBase):
    id: int
    user_id: int
    used_count: int

    class Config:
        from_attributes = True
