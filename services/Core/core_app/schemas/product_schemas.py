from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    avg_rating: float

class Config:
    from_attributes = True
