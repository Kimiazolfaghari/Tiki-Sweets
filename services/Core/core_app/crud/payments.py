from sqlalchemy.orm import Session
from services.Core.core_app.db.models import Payment, PaymentStatus, DiscountCode, Order, OrderStatus
from services.Core.core_app.schemas.payment_schemas import PaymentCreate, PaymentUpdate
from fastapi import HTTPException
from datetime import datetime

def create_payment(db: Session, payment: PaymentCreate):
    order = db.query(Order).filter(Order.id == payment.order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    discount_amount = 0.0
    if payment.discount_code:
        discount = db.query(DiscountCode).filter(
            DiscountCode.code == payment.discount_code,
            DiscountCode.start_date <= datetime.utcnow(),
            DiscountCode.ending_date >= datetime.utcnow()
        ).first()

        if not discount:
            raise HTTPException(status_code=400, detail="Invalid or expired discount code")

        if discount.user_id != order.user_id:
            raise HTTPException(status_code=400, detail="Discount code does not belong to this user")

        discount_amount = discount.amount_of_discount
        discount.used_count += 1
        db.add(discount)

    final_amount = payment.amount - discount_amount
    if final_amount < 0:
        final_amount = 0.0

    db_payment = Payment(
        amount=final_amount,
        payment_method=payment.payment_method,
        order_id=payment.order_id
    )

    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payment(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()

def update_payment_status(db: Session, payment_id: int, update_data: PaymentUpdate):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    if update_data.status == PaymentStatus.successful and db_payment.status != PaymentStatus.successful:
        order = db.query(Order).filter(Order.id == db_payment.order_id).first()
        if order:
            order.status = OrderStatus.paid
            db.add(order)

    db_payment.status = update_data.status
    db.commit()
    db.refresh(db_payment)
    return db_payment
