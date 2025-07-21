from iam_app.db.base import Base
from iam_app.db.models import Admin, User,OTP,Product,RateComment,City,Location,DiscountCode,Shipment,SpecialCake,Order,OrderDetail,Payment,ShoppingList,ShoppingListItem,MediaFile
from iam_app.db.session import engine

__all__ = [
    "User",
    "Admin",
    "OTP",
    "Product",
    "RateComment",
    "City",
    "Location",
    "DiscountCode",
    "Shipment",
    "SpecialCake",
    "Order",
    "OrderDetail",
    "Payment",
    "ShoppingList",
    "ShoppingListItem",
    "MediaFile",
]

Base.metadata.create_all(bind=engine)