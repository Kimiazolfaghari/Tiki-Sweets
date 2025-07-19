from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SpecialCakeCreate(BaseModel):
    title: str
    sponge_flavor: Optional[str] = None
    filling_type: Optional[str] = None
    cream_flavor: Optional[str] = None
    layers: Optional[int] = None
    weight: Optional[float] = None
    dimension: Optional[str] = None
    shape: Optional[str] = None
    color: Optional[str] = None
    theme: Optional[str] = None
    message_on_cake: Optional[str] = None
    delivery_date: Optional[datetime] = None
    estimated_price: Optional[float] = None


class SpecialCakeOut(SpecialCakeCreate):
    id: int
    user_id: int
    status: str
    created_at: datetime


class SpecialCakeUpdateStatus(BaseModel):
    status: str


    class Config:
        from_attributes = True

