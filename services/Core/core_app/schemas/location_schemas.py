from pydantic import BaseModel
from typing import Optional, List

class LocationBase(BaseModel):
    city_id: int
    user_id: int
    street_address: str
    alley_name: Optional[str] = None
    postal_code: Optional[str] = None

class LocationCreate(LocationBase):
    pass

class LocationUpdate(BaseModel):
    city_id: Optional[int]
    street_address: Optional[str]
    alley_name: Optional[str]
    postal_code: Optional[str]

class LocationOut(LocationBase):
    id: int

    class Config:
        from_attributes = True


class CityBase(BaseModel):
    name: str

class CityCreate(CityBase):
    pass

class CityOut(CityBase):
    id: int
    locations: List[LocationOut] = []

    class Config:
        from_attributes = True
