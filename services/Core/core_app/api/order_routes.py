from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union
from core_app.schemas.order_schemas import OrderCreate, OrderOut
from core_app.crud import order as crud
from iam_app.db.session import SessionLocal
from iam_app.core.dependencies import get_current_active_user_or_admin
from iam_app.schemas.user_schemas import UserOut
from iam_app.schemas.admin_schemas import AdminOut

order_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@order_router.post("/", response_model=OrderOut)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: UserOut = Depends(get_current_active_user_or_admin),
):
    if hasattr(current_user, "role") and current_user.role == "admin":
        raise HTTPException(status_code=403, detail="Admins cannot create orders")
    return crud.create_order(db, order, user_id=current_user.id)

@order_router.get("/{order_id}", response_model=OrderOut)
def read_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: Union[UserOut, AdminOut] = Depends(get_current_active_user_or_admin),
):
    db_order = crud.get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")

    if hasattr(current_user, "role") and current_user.role == "admin":
        return db_order

    if db_order.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access denied")

    return db_order

@order_router.get("/", response_model=list[OrderOut])
def read_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: Union[UserOut, AdminOut] = Depends(get_current_active_user_or_admin),
):
    if hasattr(current_user, "role") and current_user.role == "admin":
        return crud.get_all_orders(db, skip=skip, limit=limit)
    else:
        return crud.get_orders_by_user(db, user_id=current_user.id, skip=skip, limit=limit)
