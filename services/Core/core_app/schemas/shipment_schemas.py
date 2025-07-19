from pydantic import BaseModel
from typing import Optional

class ShipmentBase(BaseModel):
    method: str
    description: Optional[str] = None
    price: float
    shipment_code: Optional[str] = None
    estimated_days: Optional[int] = None

class ShipmentCreate(ShipmentBase):
    pass

class ShipmentUpdate(BaseModel):
    method: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    shipment_code: Optional[str] = None
    estimated_days: Optional[int] = None

class ShipmentOut(ShipmentBase):
    id: int

    class Config:
        from_attributes = True
