import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from core_app.api.discount_routes import  router as dis_router
from core_app.api.locations_routes import router as location_router
from core_app.api.order_routes import router as order_router
from core_app.api.payments_routes import router as payment_router
from core_app.api.products_routes import router as products_router
from core_app.api.ratings_routes import router as ratings_router
from core_app.api.shopping_list_routes import router as  shopping_list_router
from core_app.api.shipments_routes import router as shipment_router
from core_app.api.special_cake import router as special_cake_router
from core_app.api.profile import profile_router


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(products_router)
app.include_router(ratings_router)
app.include_router(shopping_list_router)
app.include_router(order_router)
app.include_router(payment_router)
app.include_router(shipment_router)
app.include_router(dis_router)
app.include_router(location_router)
app.include_router(special_cake_router)
app.include_router(profile_router, prefix="", tags=["Profile"])


logging.basicConfig(level=logging.INFO)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Your API",
        version="1.0.0",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            # فرض کنیم همه endpoint هایی که auth دارن
            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


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