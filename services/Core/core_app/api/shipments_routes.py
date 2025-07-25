from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from services.Core.core_app.schemas import shipment_schemas
from services.Core.core_app.crud import shipments as crud_shipment
from services.Core.core_app.db.session import  SessionLocal
from services.Core.core_app.core.security import get_current_admin  # فقط ادمین میتونه اینارو مدیریت کنه

router = APIRouter(
    prefix="/shipments",
    tags=["shipments"]
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=shipment_schemas.ShipmentOut, status_code=status.HTTP_201_CREATED)
def create_shipment(
    shipment_in: shipment_schemas.ShipmentCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin)
):
    shipment = crud_shipment.create_shipment(db, shipment_in)
    return shipment


@router.get("/", response_model=List[shipment_schemas.ShipmentOut])
def list_shipments(
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin)
):
    shipments = db.query(crud_shipment.Shipment).all()
    return shipments


@router.get("/{shipment_id}", response_model=shipment_schemas.ShipmentOut)
def get_shipment(
    shipment_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin)
):
    shipment = crud_shipment.get_shipment(db, shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment


@router.put("/{shipment_id}", response_model=shipment_schemas.ShipmentOut)
def update_shipment(
    shipment_id: int,
    shipment_update: shipment_schemas.ShipmentUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin)
):
    shipment = crud_shipment.update_shipment(db, shipment_id, shipment_update)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment


@router.delete("/{shipment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shipment(
    shipment_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin)
):
    shipment = crud_shipment.delete_shipment(db, shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return
