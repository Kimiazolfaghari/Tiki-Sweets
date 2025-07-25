from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core_app.schemas.payment_schemas import PaymentCreate, PaymentOut, PaymentUpdate
from core_app.crud import payments as crud_payment
from core_app.db.session import SessionLocal
from core_app.core.security import get_current_user, get_current_admin

router = APIRouter(prefix="/payments", tags=["payments"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PaymentOut, status_code=status.HTTP_201_CREATED)
def create_payment(
    payment_in: PaymentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # بررسی مالکیت سفارش (order) در create_payment موجود نیست، پس اینجا خودمان چک می‌کنیم
    # ابتدا سفارش را از DB بگیریم
    from core_app.crud import order as crud_order
    order = crud_order.get_order(db, payment_in.order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not allowed to pay for orders of other users")

    payment = crud_payment.create_payment(db, payment_in)
    return payment


@router.get("/{payment_id}", response_model=PaymentOut)
def get_payment(
    payment_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
    admin=Depends(get_current_admin)
):
    payment = crud_payment.get_payment(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    order_user_id = payment.order.user_id  # فرض بر این است که رابطه order در مدل Payment تعریف شده است
    if current_user["id"] != order_user_id and admin is None:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    return payment


@router.patch("/{payment_id}", response_model=PaymentOut)
def update_payment_status(
    payment_id: int,
    update_data: PaymentUpdate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    payment = crud_payment.update_payment_status(db, payment_id, update_data)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment