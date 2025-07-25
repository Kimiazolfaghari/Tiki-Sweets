from sqlalchemy.orm import Session
from services.Core.core_app.db.models import Shipment
from services.Core.core_app.schemas import shipment_schemas

def create_shipment(db: Session, shipment: shipment_schemas.ShipmentCreate):
    db_shipment = Shipment(**shipment.dict())
    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    return db_shipment

def get_shipment(db: Session, shipment_id: int):
    return db.query(Shipment).filter(Shipment.id == shipment_id).first()

def update_shipment(db: Session, shipment_id: int, updates: shipment_schemas.ShipmentUpdate):
    shipment = db.query(Shipment).filter(Shipment.id == shipment_id).first()
    if not shipment:
        return None
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(shipment, field, value)
    db.commit()
    db.refresh(shipment)
    return shipment

def delete_shipment(db: Session, shipment_id: int):
    shipment = db.query(Shipment).filter(Shipment.id == shipment_id).first()
    if shipment:
        db.delete(shipment)
        db.commit()
    return shipment
