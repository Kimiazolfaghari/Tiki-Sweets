from sqlalchemy.orm import Session
from core_app.db.models import Order, OrderDetail

def create_order(db: Session, order_data, user_id: int):
    order = Order(
        user_id=user_id,
        location_id=order_data.location_id,
        special_cake_id=order_data.special_cake_id,
        shipment_id=order_data.shipment_id,
        discount_code_id=order_data.discount_code_id,
        total_price=order_data.total_price,
        status=order_data.status,
    )
    db.add(order)
    db.flush()

    for detail in order_data.order_details:
        order_detail = OrderDetail(
            order_id=order.id,
            product_id=detail.product_id,
            quantity=detail.quantity,
        )
        db.add(order_detail)

    db.commit()
    db.refresh(order)
    return order


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def get_all_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()


def get_orders_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Order).filter(Order.user_id == user_id).offset(skip).limit(limit).all()
