from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from core_app.schemas.discount_schemas import DiscountCreate, DiscountUpdate, DiscountOut
from core_app.db.session import SessionLocal
from core_app.crud import discounts as crud_discount
from core_app.core.security import get_current_admin, get_current_user

router = APIRouter(prefix="/discounts", tags=["discounts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DiscountOut, status_code=status.HTTP_201_CREATED)
def create_discount(
    discount_in: DiscountCreate,
    db: Session = Depends(get_db),
    admin: dict = Depends(get_current_admin),
):
    existing = crud_discount.get_discount_by_code(db, discount_in.code)
    if existing:
        raise HTTPException(status_code=400, detail="Discount code already exists")
    discount = crud_discount.create_discount(db, discount_in)
    return discount


@router.get("/", response_model=List[DiscountOut])
def read_all_discounts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    admin: dict = Depends(get_current_admin),
):
    discounts = crud_discount.get_all_discounts(db, skip=skip, limit=limit)
    return discounts


@router.get("/{discount_id}", response_model=DiscountOut)
def read_discount(
    discount_id: int,
    db: Session = Depends(get_db),
    admin: dict = Depends(get_current_admin),
):
    discount = crud_discount.get_discount(db, discount_id)
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return discount


@router.put("/{discount_id}", response_model=DiscountOut)
def update_discount(
    discount_id: int,
    discount_in: DiscountUpdate,
    db: Session = Depends(get_db),
    admin: dict = Depends(get_current_admin),
):
    updated_discount = crud_discount.update_discount(db, discount_id, discount_in)
    if not updated_discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return updated_discount


@router.delete("/{discount_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_discount(
    discount_id: int,
    db: Session = Depends(get_db),
    admin: dict = Depends(get_current_admin),
):
    deleted_discount = crud_discount.delete_discount(db, discount_id)
    if not deleted_discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return None


@router.get("/validate/{code}", response_model=DiscountOut)
def validate_discount_code(
    code: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),  # احراز هویت کاربر عادی
):
    discount = crud_discount.get_discount_by_code(db, code)
    if not discount:
        raise HTTPException(status_code=404, detail="Discount code not found")

    if hasattr(discount, "is_expired") and discount.is_expired():
        raise HTTPException(status_code=400, detail="Discount code expired")

    if hasattr(discount, "usage_limit_reached") and discount.usage_limit_reached():
        raise HTTPException(status_code=400, detail="Discount code usage limit reached")

    return discount
