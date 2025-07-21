from datetime import datetime
from uuid import  uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, DateTime, Enum, Float, ForeignKey, String, Integer
from sqlalchemy.sql import func
from iam_app.db.base import Base
import enum


class OTP(Base):
    __tablename__ = "otp_codes"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, nullable=False)
    otp = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    image_url = Column(String, nullable=True)


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    image_url = Column(String, nullable=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    avg_rating = Column(Float)
    image_url = Column(String, nullable=True)

class MediaFile(Base):
    __tablename__ = "media_files"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    filename = Column(String, unique=True, nullable=False)
    original_filename = Column(String)
    size = Column(Integer)
    content_type = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    uploader_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    admin_uploader_id = Column(Integer, ForeignKey("admins.id"), nullable=True)


class RateComment(Base):
    __tablename__ = "rate_comments"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    comment = Column(String)
    rate_number = Column(Integer, nullable=False)
    image_url = Column(String, nullable=True)


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)



class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    street_address = Column(String, nullable=False)
    alley_name = Column(String)
    postal_code = Column(String)



class DiscountCode(Base):
    __tablename__ = "discount_codes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    code = Column(String, nullable=False, unique=True)
    description = Column(String)
    amount_of_discount = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    ending_date = Column(DateTime, nullable=False)
    used_count = Column(Integer, default=0)
    max_usage = Column(Integer, default=1)
    is_public = Column(Boolean, default=False)



class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    shipment_code = Column(String)
    estimated_days = Column(Integer)



class SpecialCake(Base):
    __tablename__ = "special_cakes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    sponge_flavor = Column(String)
    filling_type = Column(String)
    cream_flavor = Column(String)
    layers = Column(Integer)
    weight = Column(Float)
    dimension = Column(String)
    shape = Column(String)
    color = Column(String)
    theme = Column(String)
    message_on_cake = Column(String)
    title = Column(String, nullable=False)
    delivery_date = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    estimated_price = Column(Float)
    status = Column(String)
    image_url = Column(String, nullable=True)


class OrderStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"))
    special_cake_id = Column(Integer, ForeignKey("special_cakes.id"))
    shipment_id = Column(Integer, ForeignKey("shipments.id"))
    discount_code_id = Column(Integer, ForeignKey("discount_codes.id"))
    total_price = Column(Float, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)


class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)



class PaymentStatus(str, enum.Enum):
    pending = "pending"
    successful = "successful"
    failed = "failed"


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.pending)
    payment_date = Column(DateTime(timezone=True), server_default=func.now())
    discount_code = Column(String, ForeignKey("discount_codes.code"), nullable=True)


class ShoppingList(Base):
    __tablename__ = "shopping_lists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String, default="Created")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ShoppingListItem(Base):
    __tablename__ = "shopping_list_items"

    id = Column(Integer, primary_key=True, index=True)
    shopping_list_id = Column(Integer, ForeignKey("shopping_lists.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

