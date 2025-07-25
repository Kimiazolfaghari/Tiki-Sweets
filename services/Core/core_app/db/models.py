import enum
from sqlalchemy import Boolean, Column, DateTime, Enum, Float, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from services.Core.core_app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    avg_rating = Column(Float)

    rate_comments = relationship(
        "RateComment",
        back_populates="product",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

class RateComment(Base):
    __tablename__ = "rate_comments"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    comment = Column(String)
    rate_number = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="rate_comments")


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    locations = relationship("Location", back_populates="city", cascade="all, delete-orphan", passive_deletes=True)


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey("cities.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, nullable=False)
    street_address = Column(String, nullable=False)
    alley_name = Column(String)
    postal_code = Column(String)

    city = relationship("City", back_populates="locations")


class DiscountCode(Base):
    __tablename__ = "discount_codes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    code = Column(String, nullable=False, unique=True)
    description = Column(String)
    amount_of_discount = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    ending_date = Column(DateTime, nullable=False)
    used_count = Column(Integer, default=0)
    max_usage = Column(Integer, default=1)
    is_public = Column(Boolean, default=False)

    orders = relationship("Order", back_populates="discount_code_obj", cascade="all, delete-orphan", passive_deletes=True)
    payments = relationship("Payment", back_populates="discount_code_obj", cascade="all, delete-orphan", passive_deletes=True)


class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    shipment_code = Column(String)
    estimated_days = Column(Integer)

    orders = relationship("Order", back_populates="shipment", cascade="all, delete-orphan", passive_deletes=True)


class SpecialCake(Base):
    __tablename__ = "special_cakes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
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

    orders = relationship("Order", back_populates="special_cake", cascade="all, delete-orphan", passive_deletes=True)


class OrderStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id", ondelete="SET NULL"), nullable=True)
    special_cake_id = Column(Integer, ForeignKey("special_cakes.id", ondelete="SET NULL"), nullable=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id", ondelete="SET NULL"), nullable=True)
    discount_code_id = Column(Integer, ForeignKey("discount_codes.id", ondelete="SET NULL"), nullable=True)
    total_price = Column(Float, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)

    location = relationship("Location", passive_deletes=True)
    special_cake = relationship("SpecialCake", back_populates="orders", passive_deletes=True)
    shipment = relationship("Shipment", back_populates="orders", passive_deletes=True)
    discount_code_obj = relationship("DiscountCode", back_populates="orders", passive_deletes=True)
    order_details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan", passive_deletes=True)
    payment = relationship("Payment", back_populates="order", uselist=False, cascade="all, delete-orphan", passive_deletes=True)


class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", passive_deletes=True)


class PaymentStatus(str, enum.Enum):
    pending = "pending"
    successful = "successful"
    failed = "failed"


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.pending)
    payment_date = Column(DateTime(timezone=True), server_default=func.now())
    discount_code = Column(String, ForeignKey("discount_codes.code"), nullable=True)

    order = relationship("Order", back_populates="payment", passive_deletes=True)
    discount_code_obj = relationship("DiscountCode", back_populates="payments", passive_deletes=True)


class ShoppingList(Base):
    __tablename__ = "shopping_lists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    status = Column(String, default="Created")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    items = relationship("ShoppingListItem", back_populates="shopping_list", cascade="all, delete-orphan", passive_deletes=True)


class ShoppingListItem(Base):
    __tablename__ = "shopping_list_items"

    id = Column(Integer, primary_key=True, index=True)
    shopping_list_id = Column(Integer, ForeignKey("shopping_lists.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)

    shopping_list = relationship("ShoppingList", back_populates="items")
    product = relationship("Product", passive_deletes=True)


class CoreUsers(Base):
    __tablename__ = "core_users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)


class CoreAdmins(Base):
    __tablename__ = "core_admins"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
