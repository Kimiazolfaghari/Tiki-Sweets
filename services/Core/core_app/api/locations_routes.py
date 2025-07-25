from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from services.Core.core_app.db.session import SessionLocal
from services.Core.core_app.schemas.location_schemas import (
    CityCreate, CityOut, LocationCreate, LocationOut, LocationUpdate, CityBase)
from services.Core.core_app.crud import locations as crud_location
from services.Core.core_app.core.security import get_current_admin, get_current_user

router = APIRouter(prefix="/locations", tags=["locations"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cities/", response_model=CityOut, status_code=status.HTTP_201_CREATED)
def create_city(
    city_in: CityCreate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    return crud_location.create_city(db, city_in)


@router.get("/cities/", response_model=List[CityOut])
def read_cities(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return crud_location.get_all_cities(db, skip=skip, limit=limit)


@router.get("/cities/{city_id}", response_model=CityOut)
def read_city(
    city_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    city = crud_location.get_city(db, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@router.put("/cities/{city_id}", response_model=CityOut)
def update_city(
    city_id: int,
    city_in: CityBase,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    updated_city = crud_location.update_city(db, city_id, city_in)
    if not updated_city:
        raise HTTPException(status_code=404, detail="City not found")
    return updated_city


@router.delete("/cities/{city_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_city(
    city_id: int,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    deleted_city = crud_location.delete_city(db, city_id)
    if not deleted_city:
        raise HTTPException(status_code=404, detail="City not found")
    return None


# --------- Location Routes ---------

@router.post("/", response_model=LocationOut, status_code=status.HTTP_201_CREATED)
def create_location(
    location_in: LocationCreate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    return crud_location.create_location(db, location_in)


@router.get("/", response_model=List[LocationOut])
def read_locations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return crud_location.get_all_locations(db, skip=skip, limit=limit)


@router.get("/{location_id}", response_model=LocationOut)
def read_location(
    location_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    location = crud_location.get_location(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@router.put("/{location_id}", response_model=LocationOut)
def update_location(
    location_id: int,
    location_in: LocationUpdate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    updated_location = crud_location.update_location(db, location_id, location_in)
    if not updated_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return updated_location


@router.delete("/{location_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_location(
    location_id: int,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    deleted_location = crud_location.delete_location(db, location_id)
    if not deleted_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return None
