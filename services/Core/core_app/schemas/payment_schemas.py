from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class PaymentStatus(str, Enum):
    pending = "pending"
    successful = "successful"
    failed = "failed"

class PaymentBase(BaseModel):
    amount: float
    payment_method: str

class PaymentCreate(PaymentBase):
    order_id: int
    discount_code: Optional[str] = None

class PaymentUpdate(BaseModel):
    status: PaymentStatus

class PaymentOut(PaymentBase):
    id: int
    order_id: int
    status: PaymentStatus
    payment_date: datetime
    discount_code: Optional[str] = None

    class Config:
        from_attributes = True
