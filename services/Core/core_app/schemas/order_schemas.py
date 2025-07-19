from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderDetailBase(BaseModel):
    product_id: int
    quantity: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailOut(OrderDetailBase):
    id: int


class OrderBase(BaseModel):
    user_id: int
    location_id: Optional[int] = None
    special_cake_id: Optional[int] = None
    shipment_id: Optional[int] = None
    discount_code_id: Optional[int] = None
    total_price: float
    status: str

class OrderCreate(OrderBase):
    order_details: List[OrderDetailCreate]

class OrderOut(OrderBase):
    id: int
    date: datetime
    order_details: List[OrderDetailOut]

class Config:
    from_attributes = True
