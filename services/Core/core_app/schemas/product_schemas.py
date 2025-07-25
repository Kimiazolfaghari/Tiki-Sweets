from typing import Optional

from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    avg_rating: Optional[float] = None

class Config:
    from_attributes = True
