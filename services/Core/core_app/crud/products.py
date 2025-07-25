from sqlalchemy.orm import Session
from core_app.db.models import Product
from core_app.schemas.product_schemas import ProductCreate

def create_product(db: Session, product_in: ProductCreate) -> Product:
    product = Product(**product_in.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_all_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if product:
        db.delete(product)
        db.commit()
    return product
