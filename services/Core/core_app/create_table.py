from core_app.db.base import Base
from core_app.db.models import Shipment,SpecialCake,ShoppingList,ShoppingListItem,Product,RateComment,Order,City,Location,DiscountCode,OrderDetail,Payment,CoreUsers,CoreAdmins
from core_app.db.session import engine


__all__ = [
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
    "CoreUsers",
    "CoreAdmins",
]

Base.metadata.create_all(bind=engine)