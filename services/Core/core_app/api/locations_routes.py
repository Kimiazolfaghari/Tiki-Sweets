from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from iam_app.db.session import SessionLocal
from core_app.schemas import location_schemas
from core_app.crud import locations as crud
from iam_app.core.dependencies import get_current_admin, get_current_active_user_or_admin

location_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@location_router.post("/cities/", response_model=location_schemas.CityOut)
def create_city(
    city: location_schemas.CityCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin)
):
    return crud.create_city(db, city)

@location_router.get("/cities/{city_id}", response_model=location_schemas.CityOut)
def read_city(
    city_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_active_user_or_admin)
):
    city = crud.get_city(db, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@location_router.get("/cities/", response_model=list[location_schemas.CityOut])
def list_cities(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_active_user_or_admin)
):
    return crud.get_all_cities(db, skip, limit)

@location_router.patch("/cities/{city_id}", response_model=location_schemas.CityOut)
def update_city(
    city_id: int,
    update_data: location_schemas.CityCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin)
):
    city = crud.update_city(db, city_id, update_data)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@location_router.delete("/cities/{city_id}", response_model=location_schemas.CityOut)
def delete_city(
    city_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin)
):
    city = crud.delete_city(db, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@location_router.post("/", response_model=location_schemas.LocationOut)
def create_location(
    location: location_schemas.LocationCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin)
):
    return crud.create_location(db, location)

@location_router.get("/{location_id}", response_model=location_schemas.LocationOut)
def read_location(
    location_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_active_user_or_admin)
):
    location = crud.get_location(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@location_router.get("/", response_model=list[location_schemas.LocationOut])
def list_locations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_active_user_or_admin)
):
    return crud.get_all_locations(db, skip, limit)

@location_router.patch("/{location_id}", response_model=location_schemas.LocationOut)
def update_location(
    location_id: int,
    update_data: location_schemas.LocationUpdate,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin)
):
    location = crud.update_location(db, location_id, update_data)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@location_router.delete("/{location_id}", response_model=location_schemas.LocationOut)
def delete_location(
    location_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin)
):
    location = crud.delete_location(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location
