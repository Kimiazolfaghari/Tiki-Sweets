from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from iam_app.db.session import SessionLocal
from core_app.schemas import discount_schemas
from core_app.crud import discounts as crud
from iam_app.core.dependencies import get_current_admin, get_current_user, get_current_active_user_or_admin

dis_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@dis_router.post("/", response_model=discount_schemas.DiscountOut)
def create_discount(
    discount: discount_schemas.DiscountCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin)
):
    existing = crud.get_discount_by_code(db, discount.code)
    if existing:
        raise HTTPException(status_code=400, detail="Discount code already exists")
    return crud.create_discount(db, discount)

@dis_router.get("/{discount_id}", response_model=discount_schemas.DiscountOut)
def read_discount(
    discount_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_active_user_or_admin)
):
    discount = crud.get_discount(db, discount_id)
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return discount

@dis_router.get("/", response_model=list[discount_schemas.DiscountOut])
def list_discounts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin)
):
    return crud.get_all_discounts(db, skip, limit)

@dis_router.patch("/{discount_id}", response_model=discount_schemas.DiscountOut)
def update_discount(
    discount_id: int,
    update_data: discount_schemas.DiscountUpdate,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin)
):
    discount = crud.update_discount(db, discount_id, update_data)
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return discount

@dis_router.delete("/{discount_id}", response_model=discount_schemas.DiscountOut)
def delete_discount(
    discount_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(get_current_admin)
):
    discount = crud.delete_discount(db, discount_id)
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return discount
