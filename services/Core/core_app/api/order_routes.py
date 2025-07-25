from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from core_app.schemas.order_schemas import OrderCreate, OrderOut
from core_app.crud import order as crud_order
from core_app.db.session import SessionLocal
from core_app.core.security import get_current_user, get_current_admin

router = APIRouter(prefix="/orders", tags=["orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
def create_order(
    order_in: OrderCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    user_id = current_user["id"]

    if order_in.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed to create order for other users")

    order = crud_order.create_order(db, order_in, user_id)
    return order


@router.get("/", response_model=List[OrderOut])
def read_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin)
):
    return crud_order.get_all_orders(db, skip=skip, limit=limit)


@router.get("/me", response_model=List[OrderOut])
def read_my_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    user_id = current_user["id"]
    return crud_order.get_orders_by_user(db, user_id=user_id, skip=skip, limit=limit)


@router.get("/{order_id}", response_model=OrderOut)
def read_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
    admin=Depends(get_current_admin)
):
    order = crud_order.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    user_id = current_user["id"]
    if (order.user_id != user_id) and (admin is None):
        raise HTTPException(status_code=403, detail="Not enough permissions")

    return order
