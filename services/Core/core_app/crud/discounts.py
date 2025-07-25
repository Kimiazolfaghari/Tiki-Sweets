from sqlalchemy.orm import Session
from core_app.db.models import DiscountCode
from core_app.schemas import discount_schemas
from fastapi import HTTPException

def create_discount(db: Session, discount: discount_schemas.DiscountCreate):
    existing = get_discount_by_code(db, discount.code)
    if existing:
        raise HTTPException(status_code=400, detail="Discount code already exists")

    db_discount = DiscountCode(**discount.dict())
    db.add(db_discount)
    db.commit()
    db.refresh(db_discount)
    return db_discount

def get_discount(db: Session, discount_id: int):
    return db.query(DiscountCode).filter(DiscountCode.id == discount_id).first()

def get_discount_by_code(db: Session, code: str):
    return db.query(DiscountCode).filter(DiscountCode.code == code).first()

def get_all_discounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DiscountCode).offset(skip).limit(limit).all()

def update_discount(db: Session, discount_id: int, update_data: discount_schemas.DiscountUpdate):
    db_discount = get_discount(db, discount_id)
    if not db_discount:
        return None

    if update_data.code:
        existing = get_discount_by_code(db, update_data.code)
        if existing and existing.id != discount_id:
            raise HTTPException(status_code=400, detail="Discount code already exists")

    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(db_discount, field, value)
    db.commit()
    db.refresh(db_discount)
    return db_discount

def delete_discount(db: Session, discount_id: int):
    db_discount = get_discount(db, discount_id)
    if not db_discount:
        return None
    db.delete(db_discount)
    db.commit()
    return db_discount
