from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from iam_app.db.session import SessionLocal
from core_app.schemas import shipment_schemas
from core_app.crud import shipments as crud
from iam_app.core.dependencies import get_current_admin

shipment_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@shipment_router.post("/", response_model=shipment_schemas.ShipmentOut)
def create_shipment(
    shipment: shipment_schemas.ShipmentCreate,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    return crud.create_shipment(db, shipment)

@shipment_router.get("/{shipment_id}", response_model=shipment_schemas.ShipmentOut)
def get_shipment(
    shipment_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_admin)
):
    shipment = crud.get_shipment(db, shipment_id)
    if not shipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shipment not found")
    return shipment

@shipment_router.patch("/{shipment_id}", response_model=shipment_schemas.ShipmentOut)
def update_shipment(
    shipment_id: int,
    updates: shipment_schemas.ShipmentUpdate,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    shipment = crud.update_shipment(db, shipment_id, updates)
    if not shipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shipment not found")
    return shipment

@shipment_router.delete("/{shipment_id}", response_model=shipment_schemas.ShipmentOut)
def delete_shipment(
    shipment_id: int,
    db: Session = Depends(get_db),
    current_admin: dict = Depends(get_current_admin)
):
    shipment = crud.delete_shipment(db, shipment_id)
    if not shipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shipment not found")
    return shipment
