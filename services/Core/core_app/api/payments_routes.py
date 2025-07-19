from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from iam_app.db.session import SessionLocal
from core_app.crud import payments as crud
from core_app.schemas import payment_schemas as schemas
from iam_app.core.dependencies import get_current_user

payment_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@payment_router.post("/", response_model=schemas.PaymentOut)
def create_payment(
    payment: schemas.PaymentCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    user_id = current_user.get("user_id") or current_user.get("sub")
    return crud.create_payment(db, payment, user_id=user_id)

@payment_router.get("/{payment_id}", response_model=schemas.PaymentOut)
def read_payment(
    payment_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    payment = crud.get_payment(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    if current_user["role"] != "admin" and payment.user_id != int(current_user.get("user_id", current_user.get("sub"))):
        raise HTTPException(status_code=403, detail="Not authorized")

    return payment

@payment_router.patch("/{payment_id}", response_model=schemas.PaymentOut)
def update_payment(
    payment_id: int,
    update_data: schemas.PaymentUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only")

    return crud.update_payment_status(db, payment_id, update_data)
