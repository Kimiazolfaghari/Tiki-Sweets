from pydantic import BaseModel, conint
from typing import List
from datetime import datetime

class ShoppingListItemBase(BaseModel):
    product_id: int
    quantity: conint(ge=1)

class ShoppingListItemCreate(ShoppingListItemBase):
    pass

class ShoppingListItemOut(ShoppingListItemBase):
    id: int

    class Config:
        from_attributes = True

class ShoppingListBase(BaseModel):
    pass

class ShoppingListCreate(ShoppingListBase):
    user_id: int
    items: List[ShoppingListItemCreate]

class ShoppingListOut(ShoppingListBase):
    id: int
    user_id: int
    created_at: datetime
    items: List[ShoppingListItemOut]


class ShoppingListItemAdd(BaseModel):
    product_id: int
    quantity: int

class StatusUpdate(BaseModel):
    status: str

class Config:
      from_attributes = True
