from sqlalchemy.orm import Session
from services.Core.core_app.db.models import City, Location
from services.Core.core_app.schemas.location_schemas import LocationCreate, LocationUpdate, CityCreate

def create_city(db: Session, city: CityCreate):
    db_city = City(name=city.name)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def get_city(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()

def get_all_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(City).offset(skip).limit(limit).all()

def update_city(db: Session, city_id: int, update_data: CityCreate):
    db_city = get_city(db, city_id)
    if not db_city:
        return None
    db_city.name = update_data.name
    db.commit()
    db.refresh(db_city)
    return db_city

def delete_city(db: Session, city_id: int):
    db_city = get_city(db, city_id)
    if not db_city:
        return None
    db.delete(db_city)
    db.commit()
    return db_city


# Location CRUD
def create_location(db: Session, location: LocationCreate):
    db_location = Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def get_location(db: Session, location_id: int):
    return db.query(Location).filter(Location.id == location_id).first()

def get_all_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Location).offset(skip).limit(limit).all()

def update_location(db: Session, location_id: int, update_data: LocationUpdate):
    db_location = get_location(db, location_id)
    if not db_location:
        return None
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(db_location, field, value)
    db.commit()
    db.refresh(db_location)
    return db_location

def delete_location(db: Session, location_id: int):
    db_location = get_location(db, location_id)
    if not db_location:
        return None
    db.delete(db_location)
    db.commit()
    return db_location
