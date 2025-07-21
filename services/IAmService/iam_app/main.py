import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from iam_app.api.admin_routes import admin_router
from iam_app.api.user_routes import router
from core_app.api.products_routes import products_router
from core_app.api.ratings_routes import ratings_router
from core_app.api.shopping_list_routes import shopping_list_router
from core_app.api.order_routes import order_router
from core_app.api.payments_routes import payment_router
from core_app.api.shipments_routes import  shipment_router
from core_app.api.discount_routes import  dis_router
from core_app.api.locations_routes import  location_router
from core_app.api.special_cake import  special_cake_router
from media_app.api.media_routes import router as media_router

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Tikisweets Media API",
        version="1.0.0",
        description="API for uploading and managing media files",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", []).append({"BearerAuth": []})
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
origins = [
    "http://localhost",
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, prefix="/users", tags=["users"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])
app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(ratings_router, prefix="/rating", tags=["rating"])
app.include_router(shopping_list_router, prefix="/shoppingList", tags=["shoppingList"])
app.include_router(order_router, prefix="/orders", tags=["orders"])
app.include_router(payment_router, prefix="/payments", tags=["payments"])
app.include_router(shipment_router, prefix="/shipment", tags=["shipment"])
app.include_router(dis_router,prefix="/discount", tags=["discount"])
app.include_router(location_router,prefix="/location", tags=["location"])
app.include_router(special_cake_router,prefix="/َSpecialCake", tags=["َSpecialCake"])
app.include_router(media_router, prefix="/media", tags=["Media"])

logging.basicConfig(level=logging.INFO)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")

    except Exception as first_error:
        print(f"Primary host failed: {first_error}")

        try:
            uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True, log_level="debug")

        except Exception as fallback_error:
            print(f"Fallback host also failed: {fallback_error}")